"""Tests for backend/news.py (no network: feeds are fake, the clock is fixed).

    python -m unittest discover -s tests -v
"""
from __future__ import annotations

import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.news import KeywordMatcher, NewsStore, parse_feed  # noqa: E402

NOW = datetime(2026, 11, 9, 12, 0, tzinfo=timezone.utc)


def rss(*items: tuple[str, str, str, str]) -> bytes:
    """items: (title, link, pubDate, description)"""
    body = "".join(
        f"<item><title>{t}</title><link>{l}</link><pubDate>{d}</pubDate><description>{s}</description></item>"
        for t, l, d, s in items)
    return f'<?xml version="1.0"?><rss version="2.0"><channel><title>x</title>{body}</channel></rss>'.encode()


ATOM = b"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <title type="html">Kubernetes 2.0 &amp;amp; friends</title>
    <link rel="replies" href="https://example.org/comments"/>
    <link rel="alternate" type="text/html" href="https://example.org/k8s"/>
    <updated>2026-11-09T08:00:00Z</updated>
    <summary>Container news</summary>
  </entry>
</feed>"""

CAREERS = [
    {"id": "devops_in", "title": "DevOps Engineer", "category": "Technology", "region": "IN",
     "required_skills": [{"skill": "Docker & Kubernetes", "level": "critical"}, {"skill": "Linux", "level": "important"}]},
    {"id": "sre_us", "title": "Site Reliability Engineer", "category": "Technology", "region": "US",
     "required_skills": [{"skill": "Kubernetes", "level": "important"}]},
    {"id": "guard_in", "title": "Security Guard", "category": "Security", "region": "IN",
     "required_skills": [{"skill": "Security Systems", "level": "critical"}]},
    {"id": "chef_in", "title": "Chef", "category": "Food", "region": "IN",
     "required_skills": [{"skill": "Cooking", "level": "critical"}]},
]

CONFIG = {
    "window_days": 7,
    "refresh_minutes": 30,
    "feeds": [
        {"name": "Global Tech", "region": "global", "url": "https://g.example/feed", "site": "https://g.example"},
        {"name": "India Tech", "region": "IN", "url": "https://in.example/feed", "site": "https://in.example"},
        {"name": "Broken", "region": "US", "url": "https://broken.example/feed", "site": "https://broken.example"},
    ],
    "story_types": [{"label": "Layoffs", "words": ["layoff", "job cuts"]}],
    "skip_headlines": ["shares"],
    "topics": [
        {"label": "Kubernetes & containers", "news": ["kubernetes", "k8s"], "skills": ["kubernetes", "k8s"]},
        {"label": "Linux", "news": ["linux"], "skills": ["linux"]},
        {"label": "Cybersecurity", "news": ["ransomware", "hacker"], "skills": ["security"],
         "skills_exclude": ["Security Systems"]},
    ],
}

FEEDS = {
    "https://g.example/feed": rss(
        ("Kubernetes adds new scheduler", "https://g.example/a", "Mon, 09 Nov 2026 10:00:00 +0000", "Big release"),
        ("Cloud costs rise", "https://g.example/b", "Mon, 09 Nov 2026 09:00:00 +0000", "Teams moving to linux and k8s"),
        ("Old kubernetes story", "https://g.example/old", "Mon, 26 Oct 2026 09:00:00 +0000", ""),
        ("Shares of kubernetes vendor jump", "https://g.example/stock", "Mon, 09 Nov 2026 08:00:00 +0000", ""),
        ("Gardening tips", "https://g.example/garden", "Mon, 09 Nov 2026 08:00:00 +0000", "Nothing technical"),
        ("Ransomware hits a hospital", "https://g.example/r", "Mon, 09 Nov 2026 07:00:00 +0000", ""),
    ),
    "https://in.example/feed": rss(
        # same story syndicated with a tracking query string: must not appear twice
        ("Kubernetes adds new scheduler", "https://www.g.example/a/?utm=x", "Mon, 09 Nov 2026 10:05:00 +0000", ""),
        ("IT firm announces layoff of 500 staff", "https://in.example/l", "Mon, 09 Nov 2026 06:00:00 +0000", ""),
    ),
}


def fake_fetch(url: str) -> bytes:
    if url not in FEEDS:
        raise OSError("connection refused")
    return FEEDS[url]


def make_store() -> NewsStore:
    store = NewsStore(CONFIG, CAREERS, fetch=fake_fetch, clock=lambda: NOW)
    store.refresh()
    return store


class KeywordRules(unittest.TestCase):
    def test_lowercase_matches_any_case(self):
        self.assertEqual(KeywordMatcher(["python"]).find("New Python release"), "Python")

    def test_capitals_match_exactly(self):
        m = KeywordMatcher(["AI"])
        self.assertEqual(m.find("The AI boom"), "AI")
        self.assertIsNone(m.find("Ai+ launches a phone"))
        self.assertIsNone(m.find("she said it was fine"))

    def test_whole_words_only(self):
        m = KeywordMatcher(["Go", "java"])
        self.assertIsNone(m.find("Google expands"))
        self.assertIsNone(m.find("JavaScript turns 30"))

    def test_trailing_s_allowed(self):
        self.assertEqual(KeywordMatcher(["robot"]).find("Robots are coming"), "Robots")

    def test_keywords_ending_in_symbols(self):
        self.assertEqual(KeywordMatcher(["CI/CD"]).find("Faster CI/CD pipelines"), "CI/CD")


class FeedParsing(unittest.TestCase):
    def test_rss_entities_and_html_are_cleaned(self):
        items = parse_feed(rss(("Apple&#8217;s &lt;b&gt;new&lt;/b&gt; chip", "https://x.example/1",
                                "Mon, 09 Nov 2026 10:00:00 +0530", "<p>Hello &amp;amp; bye</p>")))
        self.assertEqual(items[0]["title"], "Apple’s new chip")
        self.assertEqual(items[0]["summary"], "Hello & bye")
        self.assertEqual(items[0]["published"], datetime(2026, 11, 9, 4, 30, tzinfo=timezone.utc))

    def test_atom_uses_alternate_link(self):
        items = parse_feed(ATOM)
        self.assertEqual(items[0]["url"], "https://example.org/k8s")
        self.assertEqual(items[0]["title"], "Kubernetes 2.0 & friends")

    def test_unsafe_links_and_undated_items_are_dropped(self):
        raw = rss(("Bad link", "javascript:alert(1)", "Mon, 09 Nov 2026 10:00:00 +0000", ""),
                  ("No date", "https://x.example/2", "", ""))
        self.assertEqual(parse_feed(raw), [])


class Store(unittest.TestCase):
    def setUp(self):
        self.store = make_store()

    def titles(self, region=None, topic=None):
        return [it["title"] for it in self.store.feed(region=region, topic=topic)["items"]]

    def test_keeps_tagged_recent_stories_only(self):
        titles = self.titles()
        self.assertIn("Kubernetes adds new scheduler", titles)
        self.assertIn("Cloud costs rise", titles)                     # tagged from its summary
        self.assertIn("IT firm announces layoff of 500 staff", titles)  # story type only
        self.assertNotIn("Old kubernetes story", titles)              # older than window_days
        self.assertNotIn("Gardening tips", titles)                    # mentions no skill
        self.assertNotIn("Shares of kubernetes vendor jump", titles)  # skip_headlines

    def test_syndicated_copy_appears_once(self):
        self.assertEqual(self.titles().count("Kubernetes adds new scheduler"), 1)

    def test_broken_feed_does_not_stop_the_rest(self):
        self.assertTrue(self.store.feed_status["Broken"].startswith("error"))
        self.assertTrue(self.store.ready)

    def test_region_filter(self):
        self.assertIn("IT firm announces layoff of 500 staff", self.titles(region="IN"))
        self.assertNotIn("IT firm announces layoff of 500 staff", self.titles(region="US"))

    def test_topic_links_careers_through_their_skills(self):
        d = self.store.feed(region="IN", topic="Kubernetes & containers")
        self.assertEqual([c["id"] for c in d["topic"]["careers"]], ["devops_in"])
        self.assertEqual(d["topic"]["careers"][0]["skill"], "Docker & Kubernetes")
        self.assertEqual(d["items"][0]["careers"], [{"id": "devops_in", "title": "DevOps Engineer"}])

    def test_skills_exclude_keeps_unrelated_careers_out(self):
        d = self.store.feed(region="IN", topic="Cybersecurity")
        self.assertEqual(d["topic"]["careers"], [])              # not the security guard
        self.assertEqual(self.store.career_news("guard_in")["items"], [])

    def test_career_news_ranks_headline_matches_first(self):
        d = self.store.career_news("devops_in")
        self.assertEqual(d["items"][0]["title"], "Kubernetes adds new scheduler")
        self.assertEqual(d["items"][0]["matched"][0]["skill"], "Docker & Kubernetes")

    def test_career_without_tech_skills_gets_nothing(self):
        self.assertEqual(self.store.career_news("chef_in")["items"], [])

    def test_trending_counts(self):
        trend = {t["label"]: t["count"] for t in self.store.feed()["trending"]}
        self.assertEqual(trend["Kubernetes & containers"], 2)
        self.assertEqual(trend["Linux"], 1)


class ShippedConfig(unittest.TestCase):
    """The real news_topics.json loads, and every topic reaches at least one career."""

    def test_every_topic_reaches_a_career(self):
        import json
        data = Path(__file__).resolve().parent.parent / "backend" / "data"
        careers = json.loads((data / "careers.json").read_text(encoding="utf-8"))
        store = NewsStore.from_files(data, careers)
        empty = [label for label, cs in store.topic_careers.items() if not cs]
        self.assertEqual(empty, [], f"topics that reach no career: {empty}")


if __name__ == "__main__":
    unittest.main()
