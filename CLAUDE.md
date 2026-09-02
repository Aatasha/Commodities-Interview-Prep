# Commodities Interview Prep

Toolkit for preparing for commodities trading interviews (built for a Glencore candidate;
works for Trafigura, Vitol, Mercuria, Gunvor). It produces a daily market brief, keeps a
question bank, and runs mock interviews.

## Layout

- `briefs/YYYY-MM-DD.md` - daily brief. The latest = highest-dated file. Read it first in any session.
- `data/prices-DATE.{json,md}`, `data/news-DATE.json` - raw inputs behind each brief.
- `scripts/fetch_prices.py` - Yahoo Finance futures (+ optional OilPriceAPI) -> prices + spreads.
- `scripts/fetch_news.py` - Google News RSS + GDELT headlines by sector, no keys.
- `scripts/build_brief.py` - assembles the brief; Tier 1 analysis if `ANTHROPIC_API_KEY` is set.
- `scripts/spreads.py` - pure spread maths (unit tested in `tests/`).
- `prompts/brief-analysis.md` - the prompt used for the Tier 1 brief. Edit to change the brief.
- `questions/*.md` - technical, market-view, behavioural, mental-maths banks.
- `networking/tuesday-cheatsheet.md` - company facts, questions to ask, intro template.
- `.claude/skills/mock-interview/SKILL.md` - `/mock-interview` skill.
- `.github/workflows/daily-brief.yml` - runs the pipeline daily and commits the brief.
- `docs/index.html` - the dashboard (single file). `scripts/build_dashboard_data.py` writes `site/data.json` for it;
  `--inline` embeds the data for an artifact preview. `.github/workflows/dashboard.yml` deploys `site/` to Pages.
- `.mcp.json` - OilPriceAPI MCP server for live oil/gas prices in Claude Code sessions.

## Rules for Claude in this repo

- Never invent a price. Quote from the latest brief or a tool result, with its as-of date. Otherwise say "n/a".
- Prices are indicative (Yahoo ~15 min delayed, web-sourced numbers may be older). Say so when it matters.
- Official LME settlements are not free; COMEX copper is the proxy. Label it.
- Facts about companies must carry a source link and date. Do not state 2026 facts from memory.
- Do not edit `briefs/` by hand except to fix a broken file; the workflow owns it.

## Unit conversions (memorise)

- 1 bbl = 42 US gal. Brent-type crude ~7.33 bbl/t (heavy crude ~6.3).
- $/bbl -> $/MMBtu: divide by 5.8. EUR/MWh -> $/MMBtu: x EURUSD / 3.412.
- COMEX copper $/lb x 2204.62 = $/t. CBOT cents/bu / 100 = $/bu; wheat 36.74 bu/t, corn 39.37 bu/t.
- 3-2-1 crack = (2 x RBOB x 42 + ULSD x 42) / 3 - WTI. Time spread M1-M2 > 0 = backwardation.
- 1 NYMEX/ICE oil lot = 1,000 bbl. 1 LME copper lot = 25 t.

## Running things

```
pip install -r requirements-dev.txt
python -m pytest tests -q
python scripts/fetch_prices.py && python scripts/fetch_news.py && python scripts/build_brief.py
```
