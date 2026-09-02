#!/usr/bin/env python3
"""Assemble the daily brief from data/prices-DATE.json and data/news-DATE.json.

Tier 0 (always): prices + spreads tables and raw headlines by sector.
Tier 1 (if ANTHROPIC_API_KEY is set): Claude reads the Tier 0 data pack, runs a bounded
number of web searches, and writes the analytical brief using prompts/brief-analysis.md.
The Tier 0 tables are appended as an appendix so every number can be audited.

Writes briefs/DATE.md and prints it.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import fetch_news  # noqa: E402
import fetch_prices  # noqa: E402

DATA_DIR = ROOT / "data"
BRIEFS_DIR = ROOT / "briefs"
PROMPT_PATH = ROOT / "prompts" / "brief-analysis.md"
DEFAULT_MODEL = "claude-opus-5"
MAX_SEARCHES = 15


def load(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def tier0(date: str, prices: dict | None, news: dict | None) -> str:
    now = dt.datetime.now(dt.timezone.utc).strftime("%H:%M")
    L = [f"# Commodities Brief - {date} (as of {now} UTC)", ""]
    if prices:
        md = fetch_prices.to_markdown(prices)
        # drop the H1 line of the prices doc, keep the tables
        body = md.split("\n", 1)[1] if "\n" in md else md
        L += ["## 1. Headline numbers", "", body.replace("## Spreads and structure", "## 2. Spreads and structure")]
    else:
        L += ["## 1. Headline numbers", "", "n/a - no prices file for this date.", "",
              "## 2. Spreads and structure", "", "n/a", ""]
    L += ["## 3. Headlines by sector", ""]
    if news:
        for sector, items in news["sectors"].items():
            L.append(f"### {sector}")
            if not items:
                L.append("- n/a")
            for it in items:
                L.append(f"- [{it['title']}]({it['link']}) - {it['source']} {it['published']}")
            L.append("")
        if news.get("errors"):
            L += ["Errors: " + "; ".join(news["errors"]), ""]
    else:
        L += ["n/a - no news file for this date.", ""]
    L += ["---", "Indicative prices from public sources, not tradeable quotes. Data-only brief "
          "(set ANTHROPIC_API_KEY to enable the analysis tier).", ""]
    return "\n".join(L)


def tier1(date: str, data_pack: str, model: str) -> str:
    import anthropic

    client = anthropic.Anthropic()
    system = PROMPT_PATH.read_text()
    now = dt.datetime.now(dt.timezone.utc).strftime("%H:%M")
    user = (f"DATE: {date}\nTIME: {now} UTC\n\nDATA PACK (authoritative, do not alter numbers):\n\n"
            f"{data_pack}\n\nWrite the brief now.")
    tools = [{"type": "web_search_20260209", "name": "web_search", "max_uses": MAX_SEARCHES}]
    messages = [{"role": "user", "content": user}]

    for _ in range(6):  # pause_turn continuations
        with client.messages.stream(model=model, max_tokens=16000, system=system,
                                    tools=tools, messages=messages) as stream:
            response = stream.get_final_message()
        if response.stop_reason == "pause_turn":
            messages = [{"role": "user", "content": user}, {"role": "assistant", "content": response.content}]
            continue
        break

    if response.stop_reason == "refusal":
        raise RuntimeError("model declined the request (stop_reason=refusal)")
    text = "".join(b.text for b in response.content if b.type == "text").strip()
    if not text.startswith("#"):
        # tolerate a stray lead-in line
        idx = text.find("# Commodities Brief")
        text = text[idx:] if idx >= 0 else text
    return text + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", default=dt.date.today().isoformat())
    ap.add_argument("--model", default=os.environ.get("BRIEF_MODEL", DEFAULT_MODEL))
    ap.add_argument("--no-ai", action="store_true", help="force Tier 0 even if a key is set")
    ap.add_argument("--no-write", action="store_true")
    ap.add_argument("--force", action="store_true", help="overwrite an existing brief for this date")
    a = ap.parse_args()

    target = BRIEFS_DIR / f"{a.date}.md"
    if target.exists() and not a.force and not a.no_write:
        print(f"briefs/{a.date}.md already exists; not overwriting (use --force)", file=sys.stderr)
        return 0

    prices = load(DATA_DIR / f"prices-{a.date}.json")
    news = load(DATA_DIR / f"news-{a.date}.json")
    base = tier0(a.date, prices, news)
    out = base
    tier = "tier0"

    if os.environ.get("ANTHROPIC_API_KEY") and not a.no_ai:
        try:
            analysed = tier1(a.date, base, a.model)
            appendix = "\n\n---\n\n## Appendix: raw data pack\n\n" + base.split("\n", 1)[1]
            out = analysed + appendix
            tier = f"tier1 ({a.model})"
        except Exception as exc:  # never lose the data-only brief
            print(f"Tier 1 failed, keeping Tier 0: {exc.__class__.__name__}: {exc}", file=sys.stderr)
            out = base + f"\n<!-- tier1 failed: {exc.__class__.__name__}: {exc} -->\n"

    print(out)
    if not a.no_write:
        BRIEFS_DIR.mkdir(exist_ok=True)
        target.write_text(out)
        print(f"wrote briefs/{a.date}.md [{tier}]", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
