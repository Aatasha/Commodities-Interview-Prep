#!/usr/bin/env python3
"""Fetch commodity and geopolitics headlines with no API keys.

Sources: Google News RSS (per-sector queries) and the GDELT 2.0 doc API.
Writes data/news-YYYY-MM-DD.json: {"sectors": {name: [item...]}, "errors": [...]}.
Each item: title, link, published, source, query.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
UA = "Mozilla/5.0 (compatible; commodities-brief/1.0)"

# Edit freely. Each sector: list of Google News queries. Keep them specific.
SECTORS = {
    "Oil": ["OPEC+ output decision", "Brent crude oil prices", "Russia oil sanctions tanker", "Middle East oil supply Strait of Hormuz"],
    "Metals": ["LME copper price", "cobalt DRC export", "China copper demand smelter", "aluminium tariffs"],
    "Gas & LNG": ["TTF gas price Europe storage", "LNG cargo Asia JKM", "Qatar LNG"],
    "Coal": ["Newcastle thermal coal price", "coal exports Indonesia Australia India demand"],
    "Agri": ["wheat prices Black Sea", "corn soybean prices weather Brazil", "Bunge Viterra grain trading"],
    "Macro & geopolitics": ["Federal Reserve rate decision commodities", "China stimulus commodities demand", "US dollar index commodities"],
    "Glencore": ["Glencore"],
    "Trading houses": ["Trafigura OR Vitol OR Mercuria OR Gunvor trading profit"],
}
PER_QUERY = 6
PER_SECTOR = 10


def google_news(query: str, errors: list[str]) -> list[dict]:
    import feedparser
    url = "https://news.google.com/rss/search?" + urllib.parse.urlencode(
        {"q": query, "hl": "en-GB", "gl": "GB", "ceid": "GB:en"})
    try:
        feed = feedparser.parse(url, agent=UA)
        if getattr(feed, "bozo", False) and not feed.entries:
            raise RuntimeError(getattr(feed, "bozo_exception", "parse error"))
    except Exception as exc:
        errors.append(f"Google News '{query}': {exc.__class__.__name__}: {exc}")
        return []
    items = []
    for e in feed.entries[:PER_QUERY]:
        src = ""
        if getattr(e, "source", None):
            src = e.source.get("title", "") if isinstance(e.source, dict) else getattr(e.source, "title", "")
        items.append({
            "title": e.get("title", "").strip(),
            "link": e.get("link", ""),
            "published": e.get("published", ""),
            "source": src or "Google News",
            "query": query,
        })
    return items


def gdelt(query: str, errors: list[str], hours: int = 48) -> list[dict]:
    import requests
    try:
        r = requests.get(
            "https://api.gdeltproject.org/api/v2/doc/doc",
            params={"query": f"{query} sourcelang:english", "mode": "artlist", "maxrecords": PER_QUERY,
                    "format": "json", "timespan": f"{hours}h", "sort": "datedesc"},
            headers={"User-Agent": UA}, timeout=25)
        r.raise_for_status()
        arts = r.json().get("articles", []) if r.text.strip() else []
    except Exception as exc:
        errors.append(f"GDELT '{query}': {exc.__class__.__name__}: {exc}")
        return []
    return [{"title": a.get("title", "").strip(), "link": a.get("url", ""), "published": a.get("seendate", ""),
             "source": a.get("domain", "GDELT"), "query": query} for a in arts]


def dedupe(items: list[dict]) -> list[dict]:
    seen, out = set(), []
    for it in items:
        k = it["title"].lower()[:80]
        if k and k not in seen:
            seen.add(k)
            out.append(it)
    return out


def build(date: str, use_gdelt: bool) -> dict:
    errors: list[str] = []
    sectors = {}
    for sector, queries in SECTORS.items():
        items = []
        for q in queries:
            items += google_news(q, errors)
        if use_gdelt and len(items) < 3:
            for q in queries[:2]:
                items += gdelt(q, errors)
        sectors[sector] = dedupe(items)[:PER_SECTOR]
    return {"date": date, "fetched_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "sectors": sectors, "errors": errors}


def to_markdown(d: dict) -> str:
    L = [f"# Headlines {d['date']} (fetched {d['fetched_at_utc']})", ""]
    for sector, items in d["sectors"].items():
        L.append(f"## {sector}")
        if not items:
            L.append("- n/a")
        for it in items:
            L.append(f"- [{it['title']}]({it['link']}) - {it['source']} {it['published']}")
        L.append("")
    if d["errors"]:
        L += ["## Errors", ""] + [f"- {e}" for e in d["errors"]]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", default=dt.date.today().isoformat())
    ap.add_argument("--no-gdelt", action="store_true")
    ap.add_argument("--no-write", action="store_true")
    a = ap.parse_args()
    d = build(a.date, not a.no_gdelt)
    print(to_markdown(d))
    if not a.no_write:
        DATA_DIR.mkdir(exist_ok=True)
        (DATA_DIR / f"news-{a.date}.json").write_text(json.dumps(d, indent=2))
    total = sum(len(v) for v in d["sectors"].values())
    if total == 0:
        print("WARNING: no headlines fetched (network blocked?)", file=sys.stderr)
    return 0 if total else 2


if __name__ == "__main__":
    sys.exit(main())
