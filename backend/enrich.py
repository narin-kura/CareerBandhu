# Copyright (c) 2025-2026 K.N.Narin (github.com/narin-kura). All rights reserved.
# Non-commercial use only. See LICENSE for full terms.
"""Career detail enrichment — derives richer, structured detail from the existing
career fields so every one of the 304 careers gains depth without hand-editing
each entry. Pure functions, no external dependencies.
"""

from __future__ import annotations
from typing import Optional

# Rough self-study time per required skill, by importance level (weeks).
_WEEKS_PER_SKILL = {"critical": 4, "important": 3, "helpful": 2}

_PHASES = [
    ("critical", "Foundation", "Master these first — you can't do the job without them."),
    ("important", "Core", "Build real competence — what employers expect day to day."),
    ("helpful", "Edge", "Stand out — the extras that set strong candidates apart."),
]


def time_to_learn(level: str) -> int:
    """Estimated self-study weeks for a single skill at the given level."""
    return _WEEKS_PER_SKILL.get(level, 3)


def _fmt_weeks(weeks: int) -> str:
    if weeks <= 0:
        return "Ready now"
    if weeks < 8:
        return f"~{weeks} weeks"
    months = round(weeks / 4.3)
    return f"~{months} month{'s' if months != 1 else ''}"


def learning_roadmap(skills: list[dict]) -> dict:
    """Group required skills into Foundation/Core/Edge phases with time estimates.

    `skills` is a list of {"skill": str, "level": str}. Works for either a full
    career's required_skills or just a user's remaining gaps.
    """
    phases = []
    total_weeks = 0
    for level, name, blurb in _PHASES:
        items = [s["skill"] for s in skills if s.get("level") == level]
        if not items:
            continue
        weeks = sum(_WEEKS_PER_SKILL.get(level, 3) for _ in items)
        total_weeks += weeks
        phases.append({
            "level": level,
            "name": name,
            "blurb": blurb,
            "skills": items,
            "weeks": weeks,
            "estimate": _fmt_weeks(weeks),
        })
    return {
        "phases": phases,
        "total_weeks": total_weeks,
        "total_estimate": _fmt_weeks(total_weeks),
    }


def job_ladder(career: dict) -> list[dict]:
    """A plausible seniority ladder for the role, branched on blue/white collar."""
    title = career["title"]
    collar = career.get("collar", "white")
    if collar == "blue":
        rungs = [
            ("Apprentice / Trainee", "Learning on the job under supervision."),
            (title, "Fully qualified and working independently."),
            (f"Senior / Master {title}", "Trusted for complex jobs; may train others."),
            ("Supervisor / Contractor", "Runs teams or an independent business."),
        ]
    else:
        rungs = [
            (f"Junior {title}", "0–2 yrs — building fundamentals with guidance."),
            (title, "2–5 yrs — delivering independently."),
            (f"Senior {title}", "5–8 yrs — owning hard problems, mentoring."),
            (f"Lead / Principal {title}", "8+ yrs — setting direction and standards."),
        ]
    return [{"title": t, "note": n} for t, n in rungs]


def _skill_set(career: dict) -> set:
    return {s["skill"].lower() for s in career.get("required_skills", [])}


def related_careers(career: dict, all_careers: list[dict], limit: int = 5) -> list[dict]:
    """Find the most similar careers by category, shared tags, and shared skills."""
    my_tags = {t.lower() for t in career.get("tags", [])}
    my_skills = _skill_set(career)
    my_cat = career.get("category")
    scored = []
    for other in all_careers:
        if other["id"] == career["id"]:
            continue
        shared_skills = my_skills & _skill_set(other)
        shared_tags = my_tags & {t.lower() for t in other.get("tags", [])}
        score = (
            (3 if other.get("category") == my_cat else 0)
            + 2 * len(shared_skills)
            + len(shared_tags)
        )
        if score <= 0:
            continue
        scored.append((score, len(shared_skills), other))
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return [
        {
            "id": o["id"],
            "title": o["title"],
            "category": o["category"],
            "growth_outlook": o.get("growth_outlook", "Good"),
            "shared_skills": n,
        }
        for _score, n, o in scored[:limit]
    ]


def career_detail(career: dict, all_careers: list[dict]) -> dict:
    """Bundle of computed + surfaced detail for a single career."""
    return {
        "collar": career.get("collar", "white"),
        "region": career.get("region", "IN"),
        "qualifications": career.get("qualifications", []),
        "job_ladder": job_ladder(career),
        "roadmap": learning_roadmap(career.get("required_skills", [])),
        "related": related_careers(career, all_careers),
    }
