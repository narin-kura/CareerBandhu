"""Crawlable career pages for search engines.

The main app is one JavaScript page, so on its own search engines see a single
page. This router adds plain server-rendered HTML for every career and career
family, plus robots.txt and sitemap.xml:

    /careers                              every career family, India and US
    /careers/india, /careers/usa          every career in a region, by family
    /careers/india/category/technology    one career family in a region
    /careers/india/data-analyst           one career: salary, outlook, skills, paths, sources

Wording (titles, descriptions, keywords) lives in seo_config.json; HTML in
templates/seo/. Set SITE_ORIGIN to change the canonical domain.
"""

from __future__ import annotations

import json
import os
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, Response
from jinja2 import Environment, FileSystemLoader, select_autoescape

BASE_DIR = Path(__file__).parent
CONFIG: dict = json.loads((BASE_DIR / "seo_config.json").read_text(encoding="utf-8"))
SITE: dict = CONFIG["site"]
ORIGIN: str = os.environ.get("SITE_ORIGIN", SITE["origin"]).rstrip("/")
CANONICAL_HOST: str = re.sub(r"^https?://", "", ORIGIN)
REGIONS: dict = CONFIG["regions"]
PAGES: dict = CONFIG["pages"]

_env = Environment(
    loader=FileSystemLoader(str(BASE_DIR / "templates" / "seo")),
    autoescape=select_autoescape(["html"]),
    trim_blocks=True,
    lstrip_blocks=True,
)

LEVELS = [("critical", "Must-have skills"), ("important", "Important skills"), ("helpful", "Helpful extras")]


# ---------- helpers ----------

def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def fill(template: str, **values) -> str:
    """Fill {{placeholders}} in a seo_config.json string; a missing value is a bug."""
    def sub(m: re.Match) -> str:
        key = m.group(1)
        if key not in values:
            raise KeyError(f"{template!r}: no value for {{{{{key}}}}}")
        return str(values[key])
    return re.sub(r"\{\{(\w+)\}\}", sub, template)


def indian_grouping(n: int) -> str:
    """1200000 -> 12,00,000 (lakh/crore grouping, as Indian readers expect)."""
    s = str(int(n))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    head = re.sub(r"(\d)(?=(\d\d)+$)", r"\1,", head)
    return f"{head},{tail}"


def format_salary(career: dict) -> dict:
    """Readable salary plus whether its currency actually matches the career's region."""
    sr = career.get("salary_range") or {}
    cur = (sr.get("currency") or "").upper()
    lo, hi = sr.get("min"), sr.get("max")
    if lo is None or hi is None:
        return {"text": "Not listed", "short": "not listed", "mismatch": False, "note": "", "currency": "", "period": "", "min": None, "max": None}
    if cur.startswith("INR"):
        text = f"₹{indian_grouping(lo)}–₹{indian_grouping(hi)}"
        code = "INR"
    else:
        text = f"${lo:,}–${hi:,}"
        code = "USD"
    # Plain "INR" is a yearly figure (the verified careers quote LPA, e.g. 350000 = 3.5 LPA).
    period = "month" if cur.endswith("/MONTH") else "year" if cur.endswith("/YEAR") or cur == "INR" else ""
    if period:
        text += f" per {period}"
    expected = REGIONS[career["region"]]["currency"]
    return {
        "text": text,
        "short": text,
        "mismatch": code != expected,
        "note": sr.get("note") or "",
        "currency": code,
        "period": period,
        "min": lo,
        "max": hi,
    }


def _abs(path: str) -> str:
    return ORIGIN + path


# ---------- the career index ----------

class Index:
    """URL slugs and groupings for every career, built once from careers.json."""

    def __init__(self, careers: list[dict]):
        self.careers = careers
        self.by_region: dict[str, list[dict]] = {r: [] for r in REGIONS}
        self.slug_of: dict[str, str] = {}
        self.by_slug: dict[tuple[str, str], dict] = {}
        # careers.json has a few same-region near-duplicates (e.g. two "Plumber" entries in
        # different families). The first keeps the plain title; later ones point their
        # canonical URL at it and stay out of the sitemap, so they don't compete in search.
        self.duplicate_of: dict[str, dict] = {}
        first_by_title: dict[tuple[str, str], dict] = {}
        for c in sorted(careers, key=lambda c: (c["title"].lower(), c["id"])):
            if c.get("region") not in REGIONS:
                continue
            key = (c["region"], c["title"].lower())
            if key in first_by_title:
                self.duplicate_of[c["id"]] = first_by_title[key]
            else:
                first_by_title[key] = c
            slug = slugify(c["title"]) or slugify(c["id"])
            if (c["region"], slug) in self.by_slug or slug == "category":
                slug = f"{slug}-{slugify(c['id'])}"
            self.slug_of[c["id"]] = slug
            self.by_slug[(c["region"], slug)] = c
            self.by_region[c["region"]].append(c)
        self.categories: dict[str, dict[str, list[dict]]] = {}
        for r, cs in self.by_region.items():
            cats: dict[str, list[dict]] = {}
            for c in cs:
                cats.setdefault(c["category"], []).append(c)
            self.categories[r] = dict(sorted(cats.items()))

    def career_path(self, c: dict) -> str:
        return f"/careers/{REGIONS[c['region']]['path']}/{self.slug_of[c['id']]}"

    @staticmethod
    def category_path(region: str, category: str) -> str:
        return f"/careers/{REGIONS[region]['path']}/category/{slugify(category)}"

    @staticmethod
    def region_path(region: str) -> str:
        return f"/careers/{REGIONS[region]['path']}"

    def region_from_path(self, path_part: str) -> Optional[str]:
        return next((r for r, cfg in REGIONS.items() if cfg["path"] == path_part), None)

    def all_paths(self) -> list[str]:
        paths = ["/careers"]
        for r in REGIONS:
            paths.append(self.region_path(r))
            paths += [self.category_path(r, cat) for cat in self.categories[r]]
            paths += [self.career_path(c) for c in self.by_region[r] if c["id"] not in self.duplicate_of]
        return paths

    def page_paths(self) -> list[str]:
        """Every page that exists, including near-duplicates left out of the sitemap."""
        return self.all_paths() + [self.career_path(c) for c in self.careers if c["id"] in self.duplicate_of]


# ---------- page builders ----------

def _base_ld(trail: list[tuple[str, str]]) -> list[dict]:
    return [
        {"@type": "WebSite", "@id": f"{ORIGIN}/#website", "name": SITE["name"], "alternateName": SITE["alternateNames"],
         "url": f"{ORIGIN}/", "publisher": {"@id": f"{SITE['makerUrl']}/#org"}},
        {"@type": "Organization", "@id": f"{SITE['makerUrl']}/#org", "name": SITE["makerName"], "url": SITE["makerUrl"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": label, "item": _abs(href)} for i, (label, href) in enumerate(trail)
        ]},
    ]


def _render(template: str, *, path: str, title: str, description: str, trail: list[tuple[str, str]],
            ld: list[dict], sources: list[dict], canonical_path: Optional[str] = None, **ctx) -> str:
    graph = {"@context": "https://schema.org", "@graph": _base_ld(trail) + ld}
    return _env.get_template(template).render(
        site=SITE, canonical=_abs(canonical_path or path), title=title, description=description, trail=trail,
        jsonld=json.dumps(graph, ensure_ascii=False).replace("</", "<\\/"), sources=sources, **ctx,
    )


def _career_card(idx: Index, c: dict) -> dict:
    sal = format_salary(c)
    return {"href": idx.career_path(c), "title": c["title"], "category": c["category"],
            "salary": sal["text"], "salary_mismatch": sal["mismatch"], "growth": c.get("growth_outlook") or "",
            "desc": (c.get("description") or "").split(". ")[0].rstrip(".") + "."}


def render_career(idx: Index, c: dict) -> str:
    rg = REGIONS[c["region"]]
    sal = format_salary(c)
    path = idx.career_path(c)
    skills = c.get("required_skills") or []
    must = [s["skill"] for s in skills if s.get("level") == "critical"] or [s["skill"] for s in skills]
    primary = idx.duplicate_of.get(c["id"])
    shown_title = f'{c["title"]} ({c["category"]})' if primary else c["title"]
    values = dict(title=shown_title, in_=rg["in"], title_in=rg["title_in"], salary=sal["text"],
                  growth=(c.get("growth_outlook") or "unknown").lower(), skills=", ".join(must[:4]))
    values["in"] = values.pop("in_")
    title = fill(PAGES["career"]["title"], **values)
    description = fill(PAGES["career"]["description"], **values)

    related = [x for x in idx.categories[c["region"]].get(c["category"], []) if x["id"] != c["id"]]
    shared = {s["skill"] for s in skills}
    related.sort(key=lambda x: (-len(shared & {s["skill"] for s in x.get("required_skills") or []}), x["title"]))
    other_region = next((x for r, cs in idx.by_region.items() if r != c["region"]
                         for x in cs if x["title"].lower() == c["title"].lower()), None)

    verification = c.get("verification") or {}
    verified = verification.get("status") == "verified"
    claim_sources = [
        {"field": field.replace("_", " "), **src} for field, src in (verification.get("sources") or {}).items()
        if isinstance(src, dict) and src.get("url")
    ]
    sources = [{"label": s["source"], "url": s["url"]} for s in claim_sources] + rg["sources"]

    occupation = {
        "@type": "Occupation",
        "name": c["title"],
        "description": c.get("description") or "",
        "occupationalCategory": c["category"],
        "occupationLocation": [{"@type": "Country", "name": rg["country"]}],
        "skills": ", ".join(s["skill"] for s in skills),
        "qualifications": "; ".join(c.get("qualifications") or []),
        "mainEntityOfPage": _abs(path),
    }
    if not sal["mismatch"] and sal["min"] is not None:
        occupation["estimatedSalary"] = [{
            "@type": "MonetaryAmountDistribution", "name": "base", "currency": sal["currency"],
            "duration": {"month": "P1M", "year": "P1Y"}.get(sal["period"], "P1Y"),
            "minValue": sal["min"], "maxValue": sal["max"],
        }]
    trail = [("Home", "/"), ("Careers", "/careers"), (f"Careers {rg['in']}", idx.region_path(c["region"])),
             (c["category"], idx.category_path(c["region"], c["category"])), (c["title"], path)]
    return _render(
        "career.html", path=path, title=title, description=description, trail=trail, ld=[occupation], sources=sources,
        canonical_path=idx.career_path(primary) if primary else None,
        c=c, region=rg, salary=sal, levels=[(lv, label, [s["skill"] for s in skills if s.get("level") == lv]) for lv, label in LEVELS],
        verified=verified, verified_at=verification.get("verified_at"), claim_sources=claim_sources,
        related=[_career_card(idx, x) for x in related[:8]],
        category_href=idx.category_path(c["region"], c["category"]),
        other_region=other_region and {"href": idx.career_path(other_region), "name": REGIONS[other_region["region"]]["name"]},
        app_href=f"/#career={c['id']}",
    )


def render_category(idx: Index, region: str, category: str) -> str:
    rg = REGIONS[region]
    cs = idx.categories[region][category]
    path = idx.category_path(region, category)
    values = {"category": category, "in": rg["in"], "title_in": rg["title_in"], "count": len(cs),
              "examples": ", ".join(c["title"] for c in cs[:3])}
    others = [{"href": idx.category_path(region, cat), "label": cat, "count": len(v)}
              for cat, v in idx.categories[region].items() if cat != category]
    trail = [("Home", "/"), ("Careers", "/careers"), (f"Careers {rg['in']}", idx.region_path(region)), (category, path)]
    return _render(
        "list.html", path=path, title=fill(PAGES["category"]["title"], **values),
        description=fill(PAGES["category"]["description"], **values), trail=trail,
        ld=[{"@type": "CollectionPage", "name": fill(PAGES["category"]["h1"], **values)}], sources=rg["sources"],
        h1=fill(PAGES["category"]["h1"], **values), intro=fill(PAGES["category"]["intro"], **values),
        groups=[{"id": "careers", "heading": None, "cards": [_career_card(idx, c) for c in cs]}],
        tiles_heading=f"Other career families {rg['in']}", tiles=others,
    )


def render_region(idx: Index, region: str) -> str:
    rg = REGIONS[region]
    cs = idx.by_region[region]
    path = idx.region_path(region)
    values = {"in": rg["in"], "title_in": rg["title_in"], "count": len(cs),
              "example1": cs[0]["title"] if cs else "", "example2": cs[-1]["title"] if cs else ""}
    groups = [{"id": slugify(cat), "heading": cat, "href": idx.category_path(region, cat),
               "cards": [_career_card(idx, c) for c in v]} for cat, v in idx.categories[region].items()]
    other = [{"href": idx.region_path(r), "label": f"All careers {REGIONS[r]['in']}", "count": len(idx.by_region[r])}
             for r in REGIONS if r != region]
    trail = [("Home", "/"), ("Careers", "/careers"), (f"Careers {rg['in']}", path)]
    return _render(
        "list.html", path=path, title=fill(PAGES["region"]["title"], **values),
        description=fill(PAGES["region"]["description"], **values), trail=trail,
        ld=[{"@type": "CollectionPage", "name": fill(PAGES["region"]["h1"], **values)}], sources=rg["sources"],
        h1=fill(PAGES["region"]["h1"], **values), intro=fill(PAGES["region"]["intro"], **values),
        groups=groups, jump=[{"href": f"#{g['id']}", "label": g["heading"]} for g in groups],
        tiles_heading="Other regions", tiles=other,
    )


def render_hub(idx: Index) -> str:
    total = sum(len(v) for v in idx.by_region.values())
    cat_count = len({c["category"] for c in idx.careers})
    values = {"count": f"{total:,}", "categories": cat_count}
    sections = [{
        "heading": f"Careers {REGIONS[r]['in']}",
        "all_href": idx.region_path(r),
        "all_label": f"All {len(idx.by_region[r])} careers {REGIONS[r]['in']}",
        "tiles": [{"href": idx.category_path(r, cat), "label": cat, "count": len(v)} for cat, v in idx.categories[r].items()],
    } for r in REGIONS]
    return _render(
        "hub.html", path="/careers", title=fill(PAGES["hub"]["title"], **values),
        description=fill(PAGES["hub"]["description"], **values), trail=[("Home", "/"), ("Careers", "/careers")],
        ld=[{"@type": "CollectionPage", "name": fill(PAGES["hub"]["h1"], **values)}],
        sources=[s for r in REGIONS.values() for s in r["sources"]],
        h1=fill(PAGES["hub"]["h1"], **values), intro=fill(PAGES["hub"]["intro"], **values), sections=sections,
    )


def render_home(index_html: str, idx: Index) -> str:
    """The app's index.html with a real title, description, canonical URL, social tags,
    structured data, up-to-date hero counts and crawlable links into /careers."""
    total = len(idx.careers)
    description = fill(CONFIG["home"]["description"], count=f"{(total // 100) * 100:,}+")
    head = _env.get_template("home_head.html").render(
        site=SITE, title=CONFIG["home"]["title"], description=description, canonical=f"{ORIGIN}/",
        jsonld=json.dumps({"@context": "https://schema.org", "@graph": [
            {"@type": "WebSite", "@id": f"{ORIGIN}/#website", "name": SITE["name"], "alternateName": SITE["alternateNames"],
             "url": f"{ORIGIN}/", "publisher": {"@id": f"{SITE['makerUrl']}/#org"}},
            {"@type": "Organization", "@id": f"{SITE['makerUrl']}/#org", "name": SITE["makerName"], "url": SITE["makerUrl"]},
            {"@type": "WebApplication", "name": SITE["name"], "url": f"{ORIGIN}/", "description": description,
             "applicationCategory": "EducationalApplication", "operatingSystem": "Web", "isAccessibleForFree": True,
             "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"}, "publisher": {"@id": f"{SITE['makerUrl']}/#org"}},
        ]}, ensure_ascii=False).replace("</", "<\\/"),
    )
    links = _env.get_template("home_links.html").render(links=CONFIG["homeLinks"])
    html = re.sub(r"<title>.*?</title>\s*<meta name=\"description\"[^>]*>", lambda _: head, index_html, count=1, flags=re.S)
    skills = {s["skill"] for c in idx.careers for s in c.get("required_skills") or []}
    stats = {"stat-c": f"{(total // 100) * 100}+", "stat-s": f"{(len(skills) // 100) * 100:,}+",
             "stat-f": f"{len({c['category'] for c in idx.careers})}+"}
    for el_id, value in stats.items():
        html = re.sub(rf'(<b id="{el_id}">)[^<]*(</b>)', rf"\g<1>{value}\g<2>", html, count=1)
    return html.replace("<!-- seo:browse-links -->", links, 1)


# ---------- router ----------

def build_router(careers: list[dict], index_file: Path) -> APIRouter:
    idx = Index(careers)
    router = APIRouter()

    def on_canonical_host(request: Request) -> bool:
        return request.headers.get("host", "").split(":")[0] == CANONICAL_HOST

    @lru_cache(maxsize=None)
    def home_html() -> str:
        return render_home(index_file.read_text(encoding="utf-8"), idx)

    @lru_cache(maxsize=2048)
    def page(path: str) -> Optional[str]:
        parts = path.strip("/").split("/")
        if parts == ["careers"]:
            return render_hub(idx)
        region = idx.region_from_path(parts[1]) if len(parts) >= 2 else None
        if not region:
            return None
        if len(parts) == 2:
            return render_region(idx, region)
        if len(parts) == 3:
            c = idx.by_slug.get((region, parts[2]))
            return render_career(idx, c) if c else None
        if len(parts) == 4 and parts[2] == "category":
            cat = next((k for k in idx.categories[region] if slugify(k) == parts[3]), None)
            return render_category(idx, region, cat) if cat else None
        return None

    def html_response(body: str, request: Request, max_age: int = 3600) -> HTMLResponse:
        headers = {"Cache-Control": f"public, max-age={max_age}"}
        if not on_canonical_host(request):   # test copies (HF Space, run.app): don't let them compete
            headers["X-Robots-Tag"] = "noindex"
        return HTMLResponse(body, headers=headers)

    @router.get("/", include_in_schema=False)
    async def home(request: Request):
        return html_response(home_html(), request, max_age=300)  # short: index.html changes every release

    @router.get("/careers", include_in_schema=False)
    @router.get("/careers/{a}", include_in_schema=False)
    @router.get("/careers/{a}/{b}", include_in_schema=False)
    @router.get("/careers/{a}/{b}/{c}", include_in_schema=False)
    async def careers_page(request: Request):
        path = request.url.path.rstrip("/") or "/"
        body = page(path)
        if body is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return html_response(body, request)

    @router.get("/robots.txt", include_in_schema=False)
    async def robots(request: Request):
        if not on_canonical_host(request):
            return PlainTextResponse("User-agent: *\nDisallow: /\n")
        return PlainTextResponse(f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {ORIGIN}/sitemap.xml\n")

    @router.get("/sitemap.xml", include_in_schema=False)
    async def sitemap():
        urls = ["/"] + idx.all_paths()
        body = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "\n".join(f"  <url><loc>{_abs(u)}</loc></url>" for u in urls) + "\n</urlset>\n")
        return Response(body, media_type="application/xml")

    @router.get("/llms.txt", include_in_schema=False)
    async def llms():
        """Plain-text summary of the site for AI assistants."""
        regions = [{
            "in": REGIONS[r]["in"], "count": len(idx.by_region[r]), "href": idx.region_path(r),
            "categories": [{"name": cat, "href": idx.category_path(r, cat), "count": len(v)}
                           for cat, v in idx.categories[r].items()],
        } for r in REGIONS]
        body = _env.get_template("llms.txt").render(
            site=SITE, origin=ORIGIN, keywords=CONFIG["keywords"], regions=regions,
            total=len(idx.careers), category_count=len({c["category"] for c in idx.careers}))
        return PlainTextResponse(body)

    router.index = idx  # for tests
    return router
