#!/usr/bin/env python3
"""Assemble site/data.json for the dashboard (docs/index.html).

Reads the latest data/prices-*.json and data/news-*.json, every data/prices-*.json for the
multi-day spread series, the highest-dated briefs/*.md, networking/tuesday-cheatsheet.md and
the four questions/*.md banks. Nothing is fetched here.

  python scripts/build_dashboard_data.py                       # -> site/data.json + site/index.html
  python scripts/build_dashboard_data.py --inline docs/index.html --out site/preview.html
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR, BRIEFS_DIR, Q_DIR = ROOT / "data", ROOT / "briefs", ROOT / "questions"
CHEATSHEET = ROOT / "networking" / "tuesday-cheatsheet.md"
BANKS = ["technical", "market-view", "behavioural", "mental-maths"]

Q_RE = re.compile(r"^### Q(\d+)\.\s*(.+?)\s*$", re.M)
FIELD_RE = re.compile(r"^\*\*(Difficulty|Model answer|Pushback|Red flags):\*\*\s*", re.M)


def latest(pattern: str, directory: Path) -> Path | None:
    files = sorted(directory.glob(pattern))
    return files[-1] if files else None


def parse_questions(text: str) -> list[dict]:
    """Split a bank file into question dicts. Tolerates missing fields."""
    out = []
    heads = list(Q_RE.finditer(text))
    for i, h in enumerate(heads):
        body = text[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(text)]
        q = {"n": int(h.group(1)), "question": h.group(2).strip(), "difficulty": None,
             "model_answer": "", "pushback": "", "red_flags": ""}
        parts = FIELD_RE.split(body)
        # parts = [pre, name, content, name, content, ...]
        for name, content in zip(parts[1::2], parts[2::2]):
            key = {"Difficulty": "difficulty", "Model answer": "model_answer",
                   "Pushback": "pushback", "Red flags": "red_flags"}[name]
            content = content.strip()
            if key == "difficulty":
                m = re.search(r"\d", content)
                q[key] = int(m.group()) if m else None
            else:
                q[key] = content
        out.append(q)
    return out


def daily_series(files: list[Path]) -> list[dict]:
    rows = []
    for f in files:
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        by = {r["key"]: r.get("last") for r in d.get("instruments", [])}
        s = d.get("spreads", {})
        rows.append({"date": d.get("date"), "brent": by.get("brent"), "wti": by.get("wti"),
                     "brent_wti": s.get("brent_wti"), "brent_m1_m2": s.get("brent_m1_m2"),
                     "wti_m1_m2": s.get("wti_m1_m2"), "crack_321": s.get("crack_321"),
                     "ttf_usd_mmbtu": s.get("ttf_usd_mmbtu"), "ttf_minus_hh": s.get("ttf_minus_hh"),
                     "copper_usd_t": s.get("copper_usd_t")})
    rows.sort(key=lambda r: r["date"] or "")
    return rows


def build(root: Path = ROOT) -> dict:
    data_dir, briefs_dir, q_dir = root / "data", root / "briefs", root / "questions"
    prices_file = latest("prices-*.json", data_dir)
    news_file = latest("news-*.json", data_dir)
    prices = json.loads(prices_file.read_text()) if prices_file else None
    news = json.loads(news_file.read_text()) if news_file else None

    history = {}
    if prices:
        for r in prices.get("instruments", []):
            if r.get("history"):
                history[r["key"]] = r["history"]

    brief_files = sorted(briefs_dir.glob("*.md"))
    brief = None
    if brief_files:
        brief = {"date": brief_files[-1].stem, "markdown": brief_files[-1].read_text()}

    cheat = root / "networking" / "tuesday-cheatsheet.md"
    questions = {}
    for bank in BANKS:
        f = q_dir / f"{bank}.md"
        questions[bank] = parse_questions(f.read_text()) if f.exists() else []

    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "prices": prices,
        "history": history,
        "daily": daily_series(sorted(data_dir.glob("prices-*.json"))),
        "news": news,
        "brief": brief,
        "briefs_index": [f.stem for f in brief_files],
        "cheatsheet": cheat.read_text() if cheat.exists() else "",
        "questions": questions,
        "sources_note": "Indicative prices from public sources (Yahoo Finance ~15 min delayed; "
                        "web-sourced figures may be older). Not tradeable quotes.",
    }


def inline(html: str, data: dict) -> str:
    """Embed data as window.__DATA__ right after <title> so the page needs no fetch."""
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    tag = f"<script>window.__DATA__ = {payload};</script>"
    if "</title>" in html:
        return html.replace("</title>", "</title>\n" + tag, 1)
    return tag + "\n" + html


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", default="site", help="output directory (default site/)")
    ap.add_argument("--html", default="docs/index.html")
    ap.add_argument("--inline", metavar="HTML", help="write a single self-contained HTML with data embedded")
    ap.add_argument("--out", help="output path for --inline (default site/preview.html)")
    a = ap.parse_args()

    data = build()
    site = ROOT / a.site
    site.mkdir(parents=True, exist_ok=True)
    if a.inline:
        out = Path(a.out) if a.out else site / "preview.html"
        out.write_text(inline(Path(a.inline).read_text(), data))
        print(f"wrote {out}", file=sys.stderr)
    else:
        (site / "data.json").write_text(json.dumps(data, ensure_ascii=False))
        shutil.copy(ROOT / a.html, site / "index.html")
        print(f"wrote {site}/data.json and index.html", file=sys.stderr)
    print(f"prices {data['prices']['date'] if data['prices'] else 'n/a'}; brief {data['brief']['date'] if data['brief'] else 'n/a'}; "
          f"questions {sum(len(v) for v in data['questions'].values())}; daily rows {len(data['daily'])}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
