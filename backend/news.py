"""Skills in the news: recent tech and jobs headlines matched to CareerCompass skills.

How a story reaches a career, step by step:
  1. Read the publisher RSS/Atom feeds listed in data/news_topics.json.
  2. Keep only the headline, link, publisher and date. The article text is never
     stored or shown; readers follow the link to the publisher.
  3. Tag the story with every topic whose "news" keywords appear in its headline
     or short summary, and with story types (Layoffs, Hiring, ...) found in the headline.
  4. A topic links to a career when one of its "skills" keywords appears in a skill
     that career lists in careers.json.

Every link is a plain keyword match, so the UI can always say which word matched
and which career skill it connects to. Nothing here is written or guessed by AI.
"""
from __future__ import annotations

import html
import json
import logging
import re
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Callable, Optional
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

log = logging.getLogger("careerbandhu.news")

LEVEL_WEIGHT = {"critical": 3, "important": 2, "helpful": 1}
MAX_FEED_BYTES = 3 * 1024 * 1024
FETCH_TIMEOUT_S = 10
SUMMARY_CHARS = 400          # only the start of a summary is used for matching
USER_AGENT = "Mozilla/5.0 (compatible; CareerCompassNews/1.0; +https://careercompass.vigyatri.com)"


# --- Keyword matching ---------------------------------------------------------

def _keyword_pattern(word: str) -> str:
    """Whole-word pattern; a trailing 's' is allowed so 'robot' also finds 'robots'."""
    pat = re.escape(word)
    if word[0].isalnum():
        pat = r"(?<![A-Za-z0-9])" + pat
    if word[-1].isalnum():
        pat = pat + r"s?(?![A-Za-z0-9])"
    return pat


class KeywordMatcher:
    """Lowercase keywords match any capitalisation; keywords with capitals match exactly."""

    def __init__(self, words: list[str]):
        words = sorted({w.strip() for w in words if w and w.strip()}, key=len, reverse=True)
        any_case = [w for w in words if w == w.lower()]
        exact = [w for w in words if w != w.lower()]
        self._rx = [
            re.compile("|".join(_keyword_pattern(w) for w in exact)) if exact else None,
            re.compile("|".join(_keyword_pattern(w) for w in any_case), re.IGNORECASE) if any_case else None,
        ]

    def find(self, text: str) -> Optional[str]:
        """Return the first keyword found in text, as it appears in the text."""
        for rx in self._rx:
            if rx is not None:
                m = rx.search(text)
                if m:
                    return m.group(0)
        return None


class Topic:
    def __init__(self, spec: dict):
        self.label: str = spec["label"]
        self.news = KeywordMatcher(spec.get("news", []))
        self.skills = KeywordMatcher(spec.get("skills", []))
        excl = spec.get("skills_exclude", [])
        self.exclude = KeywordMatcher(excl) if excl else None

    def covers_skill(self, skill_name: str) -> bool:
        if self.exclude is not None and self.exclude.find(skill_name):
            return False
        return self.skills.find(skill_name) is not None


def build_topic_index(topics: list[Topic], careers: list[dict]):
    """Work out which careers each topic reaches, through the careers' own skills.

    Returns (career_topics, topic_careers):
      career_topics[career_id][topic] = {"skill": <career skill>, "level": <its level>}
      topic_careers[topic] = [{"id","title","category","region","level","skill"}, ...]
    """
    skill_cache: dict[str, list[str]] = {}
    career_topics: dict[str, dict[str, dict]] = {}
    topic_careers: dict[str, list[dict]] = {t.label: [] for t in topics}

    for c in careers:
        best: dict[str, dict] = {}
        for req in c.get("required_skills", []):
            name = req.get("skill", "")
            level = req.get("level", "helpful")
            if name not in skill_cache:
                skill_cache[name] = [t.label for t in topics if t.covers_skill(name)]
            for label in skill_cache[name]:
                cur = best.get(label)
                if cur is None or LEVEL_WEIGHT.get(level, 0) > LEVEL_WEIGHT.get(cur["level"], 0):
                    best[label] = {"skill": name, "level": level}
        if best:
            career_topics[c["id"]] = best
            for label, link in best.items():
                topic_careers[label].append({
                    "id": c["id"], "title": c["title"], "category": c.get("category", ""),
                    "region": c.get("region", "IN"), "level": link["level"], "skill": link["skill"],
                })

    for lst in topic_careers.values():
        lst.sort(key=lambda x: (-LEVEL_WEIGHT.get(x["level"], 0), x["title"]))
    return career_topics, topic_careers


# --- Feed reading -------------------------------------------------------------

def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _child(el: ET.Element, *names: str) -> Optional[ET.Element]:
    for ch in el:
        if _local(ch.tag) in names:
            return ch
    return None


def _text(el: Optional[ET.Element]) -> str:
    return "".join(el.itertext()) if el is not None else ""


def clean_text(s: str) -> str:
    """Plain text: decode entities (feeds often double-encode them), drop HTML tags."""
    s = html.unescape(html.unescape(s or ""))
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _parse_date(s: str) -> Optional[datetime]:
    s = (s or "").strip()
    if not s:
        return None
    try:
        dt = parsedate_to_datetime(s)                       # RSS: "Mon, 09 Nov 2026 16:12:28 +0000"
    except (TypeError, ValueError, IndexError):
        try:
            dt = datetime.fromisoformat(s.replace("Z", "+00:00"))   # Atom: ISO 8601
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _entry_link(entry: ET.Element) -> str:
    for ch in entry:
        if _local(ch.tag) != "link":
            continue
        href = ch.get("href")
        if href:                                            # Atom <link href="..."/>
            if ch.get("rel", "alternate") == "alternate":
                return href.strip()
            continue
        if (ch.text or "").strip():                         # RSS <link>url</link>
            return ch.text.strip()
    guid = _child(entry, "guid", "id")
    g = _text(guid).strip()
    return g if g.startswith("http") else ""


def parse_feed(raw: bytes) -> list[dict]:
    """RSS 2.0, RSS 1.0 and Atom entries as {title, url, summary, published}."""
    root = ET.fromstring(raw)
    out = []
    for el in root.iter():
        if _local(el.tag) not in ("item", "entry"):
            continue
        title = clean_text(_text(_child(el, "title")))
        url = _entry_link(el)
        published = _parse_date(_text(_child(el, "pubDate", "published", "updated", "date")))
        if not title or not url or published is None:
            continue
        if urlsplit(url).scheme not in ("http", "https"):
            continue
        summary = clean_text(_text(_child(el, "description", "summary")))[:SUMMARY_CHARS]
        out.append({"title": title, "url": url, "summary": summary, "published": published})
    return out


def http_get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml"})
    with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT_S) as resp:
        data = resp.read(MAX_FEED_BYTES + 1)
    if len(data) > MAX_FEED_BYTES:
        raise ValueError("feed larger than size limit")
    return data


def _url_key(url: str) -> str:
    p = urlsplit(url)
    return (p.netloc.lower().removeprefix("www.") + p.path.rstrip("/")).lower()


def _title_key(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


# --- The store ----------------------------------------------------------------

class NewsStore:
    """Fetches feeds in the background and answers feed / per-career queries from memory.

    Stories are merged across refreshes and kept for `window_days`, so the window
    fills up while the server runs (a restart starts again from what feeds list now).
    """

    def __init__(self, config: dict, careers: list[dict],
                 fetch: Callable[[str], bytes] = http_get,
                 clock: Callable[[], datetime] = lambda: datetime.now(timezone.utc)):
        self.feeds: list[dict] = config["feeds"]
        self.topics = [Topic(t) for t in config["topics"]]
        self.types = [(s["label"], KeywordMatcher(s["words"])) for s in config.get("story_types", [])]
        self.skip = KeywordMatcher(config.get("skip_headlines", []))
        self.window = timedelta(days=config.get("window_days", 7))
        self.ttl_s = config.get("refresh_minutes", 30) * 60
        self._fetch = fetch
        self._now = clock

        self.careers_by_id = {c["id"]: c for c in careers}
        self.career_topics, self.topic_careers = build_topic_index(self.topics, careers)

        self._items: dict[str, dict] = {}
        self._lock = threading.Lock()
        self._refreshing = False
        self._updated_mono = 0.0
        self.updated_at: Optional[datetime] = None
        self.feed_status: dict[str, str] = {}
        self._ready = threading.Event()

    @classmethod
    def from_files(cls, data_dir: Path, careers: list[dict]) -> "NewsStore":
        with open(data_dir / "news_topics.json", encoding="utf-8") as f:
            return cls(json.load(f), careers)

    # -- refreshing --

    def tag_story(self, title: str, summary: str) -> tuple[list[dict], list[str]]:
        topics = []
        for t in self.topics:
            kw = t.news.find(title)
            in_title = kw is not None
            if not in_title:
                kw = t.news.find(summary)
            if kw:
                topics.append({"label": t.label, "keyword": kw, "in_title": in_title})
        types = [label for label, m in self.types if m.find(title)]
        return topics, types

    def _load_feed(self, feed: dict) -> list[dict]:
        try:
            entries = parse_feed(self._fetch(feed["url"]))
        except Exception as e:  # one broken feed must never stop the others
            self.feed_status[feed["name"]] = f"error: {type(e).__name__}"
            log.warning("news feed %s failed: %s", feed["name"], e)
            return []
        cutoff = self._now() - self.window
        items = []
        for e in entries:
            if e["published"] < cutoff:
                continue
            topics, types = self.tag_story(e["title"], e["summary"])
            if not topics and not types:
                continue
            if not types and self.skip.find(e["title"]):   # market chatter, not career news
                continue
            items.append({
                "title": e["title"], "url": e["url"], "source": feed["name"],
                "region": feed.get("region", "global"),
                "published": min(e["published"], self._now()),
                "topics": topics, "types": types,
            })
        self.feed_status[feed["name"]] = f"ok: {len(entries)} entries, {len(items)} kept"
        return items

    def refresh(self) -> None:
        with ThreadPoolExecutor(max_workers=8) as pool:
            batches = list(pool.map(self._load_feed, self.feeds))
        cutoff = self._now() - self.window
        with self._lock:
            merged = {k: v for k, v in self._items.items() if v["published"] >= cutoff}
            seen_titles = {_title_key(v["title"]) for v in merged.values()}
            for batch in batches:
                for it in batch:
                    key, tkey = _url_key(it["url"]), _title_key(it["title"])
                    if key in merged:
                        merged[key] = it          # newer copy of the same story
                    elif tkey not in seen_titles:
                        merged[key] = it
                        seen_titles.add(tkey)
            self._items = merged
            self.updated_at = self._now()
            if any(batches):
                self._updated_mono = time.monotonic()
            else:                                  # every feed failed: try again in ~2 minutes
                self._updated_mono = time.monotonic() - self.ttl_s + 120
        self._ready.set()
        log.info("news refreshed: %d stories (%s)", len(merged), self.feed_status)

    def _refresh_in_background(self) -> None:
        try:
            self.refresh()
        except Exception:
            log.exception("news refresh failed")
            self._ready.set()
        finally:
            with self._lock:
                self._refreshing = False

    def ensure_fresh(self) -> None:
        """Start a background refresh if the stories are older than refresh_minutes."""
        with self._lock:
            if self._refreshing or (self._updated_mono and time.monotonic() - self._updated_mono < self.ttl_s):
                return
            self._refreshing = True
        threading.Thread(target=self._refresh_in_background, name="news-refresh", daemon=True).start()

    def wait_ready(self, timeout: float) -> bool:
        return self._ready.wait(timeout)

    @property
    def ready(self) -> bool:
        return self._ready.is_set()

    # -- queries --

    def _current(self, region: Optional[str]) -> list[dict]:
        cutoff = self._now() - self.window
        with self._lock:
            items = [v for v in self._items.values() if v["published"] >= cutoff]
        if region:
            items = [v for v in items if v["region"] in ("global", region)]
        items.sort(key=lambda v: v["published"], reverse=True)
        return items

    def _careers_for(self, topic_labels: list[str], region: Optional[str], limit: int) -> tuple[list[dict], int]:
        score: dict[str, int] = {}
        for label in topic_labels:
            for c in self.topic_careers.get(label, []):
                if region and c["region"] != region:
                    continue
                score[c["id"]] = score.get(c["id"], 0) + LEVEL_WEIGHT.get(c["level"], 0)
        ranked = sorted(score, key=lambda cid: (-score[cid], self.careers_by_id[cid]["title"]))
        return [{"id": cid, "title": self.careers_by_id[cid]["title"]} for cid in ranked[:limit]], len(ranked)

    def _public(self, it: dict) -> dict:
        return {
            "title": it["title"], "url": it["url"], "source": it["source"],
            "published": it["published"].isoformat(), "topics": it["topics"], "types": it["types"],
        }

    def _sources(self, region: Optional[str]) -> list[dict]:
        return [{"name": f["name"], "site": f["site"]} for f in self.feeds
                if not region or f.get("region", "global") in ("global", region)]

    def feed(self, region: Optional[str] = None, topic: Optional[str] = None, limit: int = 40) -> dict:
        items = self._current(region)
        counts: dict[str, int] = {}
        for it in items:
            for t in it["topics"]:
                counts[t["label"]] = counts.get(t["label"], 0) + 1
        trending = [{"label": k, "count": v} for k, v in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]

        topic_info = None
        if topic:
            items = [it for it in items if any(t["label"] == topic for t in it["topics"])]
            links = [c for c in self.topic_careers.get(topic, []) if not region or c["region"] == region]
            topic_info = {"label": topic, "careers": [
                {"id": c["id"], "title": c["title"], "category": c["category"], "level": c["level"], "skill": c["skill"]}
                for c in links]}

        out = []
        for it in items[:limit]:
            careers, total = self._careers_for([t["label"] for t in it["topics"]], region, 3)
            out.append({**self._public(it), "careers": careers, "more_careers": max(0, total - len(careers))})

        return {
            "ready": self.ready,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "window_days": self.window.days,
            "story_count": len(items),
            "trending": trending,
            "topic": topic_info,
            "items": out,
            "sources": self._sources(region),
        }

    def career_news(self, career_id: str, limit: int = 4) -> dict:
        career = self.careers_by_id.get(career_id)
        links = self.career_topics.get(career_id, {})
        if career is None or not links:
            return {"ready": self.ready, "topics": [], "items": []}
        region = career.get("region", "IN")
        scored = []
        for it in self._current(region):
            hits = [t for t in it["topics"] if t["label"] in links]
            if hits:
                # a skill named in the headline counts double: the story is more likely about it
                weight = sum(LEVEL_WEIGHT.get(links[t["label"]]["level"], 0) * (2 if t["in_title"] else 1) for t in hits)
                matched = [{"label": t["label"], "keyword": t["keyword"], "skill": links[t["label"]]["skill"]} for t in hits]
                scored.append((weight, it, matched))
        # most relevant first (critical skills, named in the headline), then newest
        scored.sort(key=lambda s: (-s[0], -s[1]["published"].timestamp()))
        return {
            "ready": self.ready,
            "topics": [{"label": k, **v} for k, v in sorted(links.items(), key=lambda kv: -LEVEL_WEIGHT.get(kv[1]["level"], 0))],
            "items": [{**self._public(it), "matched": matched} for _, it, matched in scored[:limit]],
            "story_count": len(scored),
        }
