# Copyright (c) 2025-2026 K.N.Narin (github.com/narin-kura). All rights reserved.
# Non-commercial use only. Commercial use requires written permission: github.com/narin-kura
# See LICENSE for full terms.
"""CareerBandhu — Career Guidance API"""

from __future__ import annotations
import json
import logging
import os
import sqlite3
from pathlib import Path
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

try:
    import anthropic
    _ANTHROPIC_AVAILABLE = True
except ImportError:
    _ANTHROPIC_AVAILABLE = False

try:
    import google.generativeai as genai
    _GEMINI_AVAILABLE = True
except ImportError:
    _GEMINI_AVAILABLE = False

try:
    from backend.auth import get_current_user, supabase, SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_CONFIGURED
except ImportError:
    from auth import get_current_user, supabase, SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_CONFIGURED

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
UI_DIR = BASE_DIR / "static"
DB_PATH = BASE_DIR / "ratings.db"

app = FastAPI(title="CareerBandhu API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def _client_ip(request: Request) -> str:
    """Real client IP from X-Forwarded-For (Cloud Run / HF proxy), else peer IP."""
    xff = request.headers.get("x-forwarded-for")
    if xff:
        return xff.split(",")[0].strip()
    return get_remote_address(request)


# Per-client rate limiting (in-memory). Applied per-route on the write/LLM paths.
limiter = Limiter(key_func=_client_ip)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.mount("/static", StaticFiles(directory=str(UI_DIR)), name="static")

# --- Load data ---
with open(DATA_DIR / "careers.json") as f:
    CAREERS: list[dict] = json.load(f)

with open(DATA_DIR / "skills.json") as f:
    SKILLS_DATA: dict = json.load(f)

with open(DATA_DIR / "resources.json") as f:
    RESOURCES: dict = json.load(f)

CAREERS_BY_ID: dict[str, dict] = {c["id"]: c for c in CAREERS}


# --- Database ---
def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            career_id TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
            comment TEXT,
            pursuing INTEGER DEFAULT 0,
            skills_context TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.commit()
    conn.close()


init_db()


# --- Models ---
class RecommendRequest(BaseModel):
    skills: list[str]
    experience_level: str = "any"
    target_career: Optional[str] = None
    region: Optional[str] = None


class GapRequest(BaseModel):
    skills: list[str]


class RatingRequest(BaseModel):
    career_id: str
    rating: int
    comment: Optional[str] = None
    pursuing: bool = False
    skills: list[str] = []


class ProfileUpdateRequest(BaseModel):
    skills: list[str] = []
    region: Optional[str] = None


class BookmarkRequest(BaseModel):
    career_id: str


class ProgressUpdateRequest(BaseModel):
    learned_skills: list[str] = []


# --- Core logic ---
def _normalize(s: str) -> str:
    return s.strip().lower()


def _matches(skill_name: str, user_lower: set[str]) -> bool:
    return _normalize(skill_name) in user_lower


def calculate_match(user_skills: list[str], career: dict) -> dict:
    user_lower = {_normalize(s) for s in user_skills}
    required = career.get("required_skills", [])

    by_level = {"critical": [], "important": [], "helpful": []}
    for s in required:
        by_level.setdefault(s["level"], []).append(s)

    weights = {"critical": 3, "important": 2, "helpful": 1}
    total_weight = sum(len(by_level[l]) * w for l, w in weights.items())
    if total_weight == 0:
        return {"score": 0, "matching_skills": [], "gaps": []}

    earned = 0
    matching, gaps = [], []
    for level, w in weights.items():
        for s in by_level[level]:
            if _matches(s["skill"], user_lower):
                earned += w
                matching.append({"skill": s["skill"], "level": level})
            else:
                gaps.append({"skill": s["skill"], "level": level})

    score = round((earned / total_weight) * 100, 1)
    return {"score": score, "matching_skills": matching, "gaps": gaps}


def get_resources_for(skill: str) -> list[dict]:
    if skill in RESOURCES:
        return RESOURCES[skill]
    skill_lower = skill.lower()
    for key, res in RESOURCES.items():
        if key.lower() == skill_lower:
            return res
    return []


def get_ai_advice(skills: list[str], career: dict, score: float, gaps: list[dict]) -> Optional[str]:
    top_gaps = [g["skill"] for g in gaps if g["level"] in ("critical", "important")][:5]
    prompt = f"""A person wants to become a {career['title']}.
Current skills: {', '.join(skills) if skills else 'none listed'}.
Match score: {score}%.
Critical/important skills still needed: {', '.join(top_gaps) if top_gaps else 'none — great match!'}.

Give 3 specific, actionable tips (2-3 sentences each) to help them transition into this career.
Be encouraging, practical, and mention realistic timelines. Start directly with Tip 1."""

    gemini_key = os.environ.get("GEMINI_API_KEY")
    if _GEMINI_AVAILABLE and gemini_key:
        try:
            return _ai_advice_gemini(prompt, gemini_key)
        except Exception:
            logger.exception("Gemini AI advice failed; falling back to Anthropic")

    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    if _ANTHROPIC_AVAILABLE and anthropic_key:
        try:
            return _ai_advice_anthropic(prompt, anthropic_key)
        except Exception:
            logger.exception("Anthropic AI advice failed; returning no advice")

    if not gemini_key and not anthropic_key:
        logger.warning("get_ai_advice: no GEMINI_API_KEY or ANTHROPIC_API_KEY set")
    return None


def _ai_advice_gemini(prompt: str, api_key: str) -> str:
    # REST transport: default gRPC channels hang silently on Cloud Run's gVisor sandbox
    genai.configure(api_key=api_key, transport="rest")
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt, request_options={"timeout": 30})
    return response.text


def _ai_advice_anthropic(prompt: str, api_key: str) -> str:
    client = anthropic.Anthropic(api_key=api_key, timeout=30.0, max_retries=1)
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text


# --- Routes ---
@app.get("/")
async def root():
    index = UI_DIR / "index.html"
    if index.exists():
        return FileResponse(str(index), media_type="text/html")
    return {"name": "CareerBandhu API", "version": "1.0.0", "status": "running"}


@app.get("/api/health")
async def health():
    return {"name": "CareerBandhu API", "version": "1.0.0", "status": "running"}


@app.get("/api/config")
async def get_config():
    return {
        "supabase_url": SUPABASE_URL,
        "supabase_anon_key": SUPABASE_ANON_KEY,
        "auth_enabled": SUPABASE_CONFIGURED,
    }


@app.get("/api/skills")
async def list_skills():
    return SKILLS_DATA


@app.get("/api/careers")
async def list_careers(region: Optional[str] = None):
    careers = CAREERS
    if region:
        careers = [c for c in CAREERS if c.get("region", "IN") == region]
    return {
        "region": region,
        "careers": [
            {
                "id": c["id"],
                "title": c["title"],
                "category": c["category"],
                "region": c.get("region", "IN"),
                "collar": c.get("collar", "white"),
                "growth_outlook": c.get("growth_outlook"),
                "tags": c.get("tags", []),
            }
            for c in careers
        ]
    }


@app.post("/api/recommend")
@limiter.limit("40/minute")
async def recommend(request: Request, req: RecommendRequest):
    if not req.skills and not req.target_career:
        raise HTTPException(400, "Provide at least one skill or a target career")

    # Target-first mode: user knows the career, wants gap analysis
    if req.target_career:
        career = CAREERS_BY_ID.get(req.target_career)
        if not career:
            for c in CAREERS:
                if req.target_career.lower() in c["title"].lower():
                    career = c
                    break
        if not career:
            raise HTTPException(404, f"Career not found: {req.target_career}")
        match = calculate_match(req.skills, career)
        return {
            "mode": "target",
            "career": career,
            "score": match["score"],
            "matching_skills": match["matching_skills"],
            "gaps": match["gaps"],
            "resources": {g["skill"]: get_resources_for(g["skill"]) for g in match["gaps"]},
        }

    # Skills-first mode: recommend careers based on skills
    pool = CAREERS
    if req.region:
        pool = [c for c in CAREERS if c.get("region", "IN") == req.region]
    scored = []
    for career in pool:
        match = calculate_match(req.skills, career)
        if match["score"] == 0:
            continue
        scored.append({
            "career": {
                "id": career["id"],
                "title": career["title"],
                "category": career["category"],
                "collar": career.get("collar", "white"),
                "description": career["description"],
                "salary_range": career.get("salary_range"),
                "growth_outlook": career.get("growth_outlook", "Good"),
                "work_style": career.get("work_style", []),
                "tags": career.get("tags", []),
            },
            "score": match["score"],
            "matching_skills": match["matching_skills"],
            "top_gaps": match["gaps"][:3],
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return {
        "mode": "skills",
        "recommendations": scored[:8],
        "total_skills_submitted": len(req.skills),
    }


@app.get("/api/career/{career_id}")
async def get_career(career_id: str):
    career = CAREERS_BY_ID.get(career_id)
    if not career:
        raise HTTPException(404, "Career not found")

    conn = get_db()
    row = conn.execute(
        "SELECT AVG(rating) as avg_r, COUNT(*) as cnt FROM ratings WHERE career_id = ?",
        (career_id,)
    ).fetchone()
    comments = conn.execute(
        """SELECT rating, comment, pursuing, created_at FROM ratings
           WHERE career_id = ? AND comment IS NOT NULL AND comment != ''
           ORDER BY created_at DESC LIMIT 10""",
        (career_id,)
    ).fetchall()
    conn.close()

    return {
        "career": career,
        "avg_rating": round(row["avg_r"], 1) if row["avg_r"] else None,
        "rating_count": row["cnt"],
        "recent_feedback": [dict(c) for c in comments],
    }


@app.post("/api/career/{career_id}/gap")
@limiter.limit("20/minute")
async def gap_analysis(request: Request, career_id: str, req: GapRequest):
    career = CAREERS_BY_ID.get(career_id)
    if not career:
        raise HTTPException(404, "Career not found")

    match = calculate_match(req.skills, career)
    gap_resources = {g["skill"]: get_resources_for(g["skill"]) for g in match["gaps"]}
    # threadpool: LLM call must not block the event loop
    ai_advice = await run_in_threadpool(get_ai_advice, req.skills, career, match["score"], match["gaps"])

    return {
        "career_id": career_id,
        "career_title": career["title"],
        "score": match["score"],
        "matching_skills": match["matching_skills"],
        "gaps": match["gaps"],
        "resources": gap_resources,
        "ai_advice": ai_advice,
        "entry_paths": career.get("entry_paths", []),
    }


@app.post("/api/rate")
@limiter.limit("20/minute")
async def submit_rating(request: Request, req: RatingRequest):
    if not (1 <= req.rating <= 5):
        raise HTTPException(400, "Rating must be 1–5")
    if req.career_id not in CAREERS_BY_ID:
        raise HTTPException(404, "Career not found")

    conn = get_db()
    conn.execute(
        "INSERT INTO ratings (career_id, rating, comment, pursuing, skills_context) VALUES (?,?,?,?,?)",
        (req.career_id, req.rating, req.comment, int(req.pursuing), json.dumps(req.skills))
    )
    conn.commit()
    row = conn.execute(
        "SELECT AVG(rating) as avg_r, COUNT(*) as cnt FROM ratings WHERE career_id = ?",
        (req.career_id,)
    ).fetchone()
    conn.close()

    return {
        "success": True,
        "new_avg_rating": round(row["avg_r"], 1),
        "total_ratings": row["cnt"],
    }


@app.get("/api/career/{career_id}/stats")
async def career_stats(career_id: str):
    conn = get_db()
    row = conn.execute(
        """SELECT AVG(rating) as avg_r, COUNT(*) as total,
           SUM(pursuing) as pursuing_count
           FROM ratings WHERE career_id = ?""",
        (career_id,)
    ).fetchone()
    conn.close()
    return {
        "career_id": career_id,
        "avg_rating": round(row["avg_r"], 1) if row["avg_r"] else None,
        "total_ratings": row["total"],
        "pursuing_count": row["pursuing_count"] or 0,
    }


# --- Personalization (requires Supabase auth) ---
@app.get("/api/profile")
async def get_profile(user_id: str = Depends(get_current_user)):
    resp = supabase.table("profiles").select("*").eq("user_id", user_id).execute()
    if resp.data:
        return resp.data[0]
    return {"user_id": user_id, "skills": [], "region": "IN"}


@app.put("/api/profile")
async def update_profile(req: ProfileUpdateRequest, user_id: str = Depends(get_current_user)):
    payload = {"user_id": user_id, "skills": req.skills}
    if req.region:
        payload["region"] = req.region
    resp = supabase.table("profiles").upsert(payload).execute()
    return resp.data[0] if resp.data else payload


@app.get("/api/bookmarks")
async def list_bookmarks(user_id: str = Depends(get_current_user)):
    resp = (
        supabase.table("bookmarks")
        .select("career_id, created_at")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    careers = []
    for row in resp.data:
        c = CAREERS_BY_ID.get(row["career_id"])
        if not c:
            continue
        careers.append({
            "id": c["id"],
            "title": c["title"],
            "category": c["category"],
            "collar": c.get("collar", "white"),
            "region": c.get("region", "IN"),
            "growth_outlook": c.get("growth_outlook"),
            "tags": c.get("tags", []),
            "bookmarked_at": row["created_at"],
        })
    return {"bookmarks": careers}


@app.post("/api/bookmarks")
async def add_bookmark(req: BookmarkRequest, user_id: str = Depends(get_current_user)):
    if req.career_id not in CAREERS_BY_ID:
        raise HTTPException(404, "Career not found")
    supabase.table("bookmarks").upsert({"user_id": user_id, "career_id": req.career_id}).execute()
    return {"success": True}


@app.delete("/api/bookmarks/{career_id}")
async def remove_bookmark(career_id: str, user_id: str = Depends(get_current_user)):
    supabase.table("bookmarks").delete().eq("user_id", user_id).eq("career_id", career_id).execute()
    return {"success": True}


@app.get("/api/career/{career_id}/progress")
async def get_progress(career_id: str, user_id: str = Depends(get_current_user)):
    career = CAREERS_BY_ID.get(career_id)
    if not career:
        raise HTTPException(404, "Career not found")

    resp = (
        supabase.table("career_progress")
        .select("learned_skills")
        .eq("user_id", user_id)
        .eq("career_id", career_id)
        .execute()
    )
    learned = resp.data[0]["learned_skills"] if resp.data else []
    match = calculate_match(learned, career)
    return {"career_id": career_id, "learned_skills": learned, "score": match["score"], "gaps": match["gaps"]}


@app.put("/api/career/{career_id}/progress")
async def update_progress(career_id: str, req: ProgressUpdateRequest, user_id: str = Depends(get_current_user)):
    career = CAREERS_BY_ID.get(career_id)
    if not career:
        raise HTTPException(404, "Career not found")

    supabase.table("career_progress").upsert({
        "user_id": user_id,
        "career_id": career_id,
        "learned_skills": req.learned_skills,
    }).execute()
    match = calculate_match(req.learned_skills, career)
    return {"success": True, "score": match["score"]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
