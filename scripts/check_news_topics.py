"""Review backend/data/news_topics.json before shipping an edit.

    python scripts/check_news_topics.py          # every topic -> the career skills and careers it reaches
    python scripts/check_news_topics.py --live   # also fetch the feeds and show how today's stories get tagged

Read the output for wrong links (a topic catching an unrelated skill) and add the
skill to that topic's "skills_exclude", or tighten the keyword.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from backend.news import NewsStore  # noqa: E402

DATA = ROOT / "backend" / "data"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    careers = json.loads((DATA / "careers.json").read_text(encoding="utf-8"))
    config = json.loads((DATA / "news_topics.json").read_text(encoding="utf-8"))
    store = NewsStore(config, careers)

    problems = 0
    for topic in store.topics:
        links = store.topic_careers[topic.label]
        skills = Counter(c["skill"] for c in links)
        regions = Counter(c["region"] for c in links)
        print(f"\n== {topic.label}  ({len(links)} careers: {dict(regions)})")
        if not links:
            print("   !! reaches no career - check its 'skills' keywords")
            problems += 1
        for skill, n in skills.most_common():
            print(f"   {n:3d} x {skill}")

    if "--live" in sys.argv:
        store.refresh()
        print("\n\n== Feeds")
        for name, status in store.feed_status.items():
            print(f"   {name}: {status}")
            if status.startswith("error"):
                problems += 1
        print("\n== Stories kept")
        for it in store._current(None):
            tags = ", ".join(f"{t['label']} [{t['keyword']}]" for t in it["topics"])
            types = f"  <{', '.join(it['types'])}>" if it["types"] else ""
            print(f"   {it['source']}: {it['title'][:90]}\n        -> {tags or '-'}{types}")
        trend = store.feed()["trending"]
        print("\n== Topic counts:", ", ".join(f"{t['label']} {t['count']}" for t in trend))

    print(f"\n{problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
