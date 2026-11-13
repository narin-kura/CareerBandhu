"""Tests for backend/seo.py: crawlable career pages, sitemap and robots.txt.

    python -m unittest discover -s tests -v
"""
from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from backend import seo  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent / "backend"
CAREERS = json.loads((ROOT / "data" / "careers.json").read_text(encoding="utf-8"))
HOST = {"host": seo.CANONICAL_HOST}


def make_client() -> tuple[TestClient, seo.Index]:
    app = FastAPI()
    router = seo.build_router(CAREERS, ROOT / "static" / "index.html")
    app.include_router(router)
    return TestClient(app), router.index


class HelperTests(unittest.TestCase):
    def test_indian_grouping(self):
        self.assertEqual(seo.indian_grouping(999), "999")
        self.assertEqual(seo.indian_grouping(8000), "8,000")
        self.assertEqual(seo.indian_grouping(1200000), "12,00,000")
        self.assertEqual(seo.indian_grouping(125000000), "12,50,00,000")

    def test_salary_formats(self):
        inr = seo.format_salary({"region": "IN", "salary_range": {"min": 8000, "max": 50000, "currency": "INR/month"}})
        self.assertEqual(inr["text"], "₹8,000–₹50,000 per month")
        self.assertFalse(inr["mismatch"])
        usd_in = seo.format_salary({"region": "IN", "salary_range": {"min": 70000, "max": 180000, "currency": "USD"}})
        self.assertEqual(usd_in["text"], "$70,000–$180,000")
        self.assertTrue(usd_in["mismatch"], "a USD salary on an India career must be flagged, not shown as an India figure")
        lpa = seo.format_salary({"region": "IN", "salary_range": {"min": 350000, "max": 1200000, "currency": "INR"}})
        self.assertEqual(lpa["text"], "₹3,50,000–₹12,00,000 per year")
        usd = seo.format_salary({"region": "US", "salary_range": {"min": 50000, "max": 90000, "currency": "USD/year"}})
        self.assertEqual(usd["text"], "$50,000–$90,000 per year")
        self.assertFalse(usd["mismatch"])

    def test_slugify(self):
        self.assertEqual(seo.slugify("Carpenter / Furniture Maker"), "carpenter-furniture-maker")
        self.assertEqual(seo.slugify("3D Printing & Additive Manufacturing"), "3d-printing-additive-manufacturing")


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client, cls.idx = make_client()
        cls.pages: dict[str, str] = {}
        for path in cls.idx.page_paths():
            r = cls.client.get(path, headers=HOST)
            cls.pages[path] = r.text
            assert r.status_code == 200, (path, r.status_code)

    def test_every_career_has_a_page(self):
        regional = [c for c in CAREERS if c["region"] in seo.REGIONS]
        career_pages = [p for p in self.pages if p.count("/") == 3 and "/category/" not in p]
        self.assertEqual(len(career_pages), len(regional))

    def test_titles_descriptions_canonical(self):
        titles = set()
        for path, html in self.pages.items():
            title = re.search(r"<title>(.*?)</title>", html).group(1)
            self.assertNotIn(title, titles, f"duplicate title on {path}")
            titles.add(title)
            desc = re.search(r'<meta name="description" content="([^"]*)"', html).group(1)
            self.assertGreater(len(desc), 50, path)
            canonical = re.search(r'<link rel="canonical" href="([^"]*)">', html).group(1)
            if canonical != f"{seo.ORIGIN}{path}":   # a near-duplicate career points at its twin
                self.assertIn(canonical.removeprefix(seo.ORIGIN), self.pages, path)
            self.assertNotRegex(html, r"\{\{\s*\w")
            json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S).group(1))

    def test_internal_links_resolve(self):
        known = set(self.pages) | {"/"}
        for path, html in self.pages.items():
            for href in re.findall(r'href="(/[^"#?]*)', html):
                if href.startswith("/static/"):
                    continue
                self.assertIn(href, known, f"broken link {href} on {path}")

    def test_occupation_salary_only_when_currency_matches_region(self):
        sw = next(c for c in CAREERS if c["region"] == "IN" and (c["salary_range"] or {}).get("currency") == "USD")
        html = self.pages[self.idx.career_path(sw)]
        self.assertIn("has not yet been checked for India", html)
        self.assertNotIn("estimatedSalary", html)
        ok = next(c for c in CAREERS if c["region"] == "IN" and (c["salary_range"] or {}).get("currency") == "INR/month")
        self.assertIn('"duration": "P1M"', self.pages[self.idx.career_path(ok)])

    def test_verified_career_shows_its_sources(self):
        da = next(c for c in CAREERS if (c.get("verification") or {}).get("status") == "verified")
        html = self.pages[self.idx.career_path(da)]
        self.assertIn("Verified", html)
        for src in da["verification"]["sources"].values():
            self.assertIn(src["url"].replace("&", "&amp;"), html)

    def test_unknown_pages_404(self):
        for path in ["/careers/india/not-a-real-career", "/careers/mars", "/careers/india/category/nope"]:
            self.assertEqual(self.client.get(path, headers=HOST).status_code, 404, path)

    def test_sitemap_and_robots(self):
        sm = self.client.get("/sitemap.xml", headers=HOST)
        self.assertEqual(sm.headers["content-type"], "application/xml")
        locs = re.findall(r"<loc>(.*?)</loc>", sm.text)
        self.assertEqual(len(locs), len(self.idx.all_paths()) + 1)
        self.assertGreater(len(self.pages), len(self.idx.all_paths()), "near-duplicates exist but are not in the sitemap")
        self.assertEqual(len(set(locs)), len(locs))
        robots = self.client.get("/robots.txt", headers=HOST).text
        self.assertIn(f"Sitemap: {seo.ORIGIN}/sitemap.xml", robots)
        self.assertIn("Disallow: /\n", self.client.get("/robots.txt", headers={"host": "knnarin-careerbandhu.hf.space"}).text)
        self.assertEqual(self.client.get("/careers", headers={"host": "x.run.app"}).headers.get("x-robots-tag"), "noindex")
        self.assertIsNone(self.client.get("/careers", headers=HOST).headers.get("x-robots-tag"))

    def test_home_page_tags_counts_and_links(self):
        html = self.client.get("/", headers=HOST).text
        self.assertIn(f"<title>{seo.CONFIG['home']['title'].replace('&', '&amp;')}</title>", html)
        self.assertEqual(html.count("<title>"), 1)
        self.assertEqual(html.count('name="description"'), 1)
        self.assertIn(f'<link rel="canonical" href="{seo.ORIGIN}/" />', html)
        self.assertNotIn(">65+<", html)
        self.assertNotIn("seo:browse-links", html)
        for link in seo.CONFIG["homeLinks"]["links"]:
            self.assertIn(f'href="{link["href"]}"', html)
            self.assertIn(link["href"], set(self.pages) | {"/"}, f"home link {link['href']} has no page")
        for el_id in ("stat-c", "stat-s", "stat-f"):
            self.assertIn(f'id="{el_id}"', html)


if __name__ == "__main__":
    unittest.main()
