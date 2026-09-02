#!/usr/bin/env python3
"""Fetch commodity prices and compute spreads.

Layer 1 (always): Yahoo Finance futures via yfinance - free, no key, ~15 min delayed.
Layer 2 (optional): OilPriceAPI overlay when OILPRICEAPI_KEY is set - source-timestamped
                    spot values for Brent, WTI, Henry Hub, TTF, JKM, coal, EU carbon.

Writes data/prices-YYYY-MM-DD.json and .md and prints the markdown. Every failure is
recorded in the "errors" list and shown as "n/a" - nothing is ever guessed.

Usage:
  python scripts/fetch_prices.py                # today, write files
  python scripts/fetch_prices.py --no-write     # print only
  python scripts/fetch_prices.py --date 2026-09-02
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import spreads as sp  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

# ---------------------------------------------------------------------------
# Instrument table. Edit this to add or remove instruments.
#   key    : stable id used in JSON and spreads
#   yf     : Yahoo Finance ticker (None = not on Yahoo)
#   opa    : OilPriceAPI commodity code (None = not requested from OilPriceAPI)
#   unit   : unit of the native quote
#   group  : section in the table
# ---------------------------------------------------------------------------
INSTRUMENTS = [
    {"key": "brent",   "name": "Brent crude (ICE, M1)",     "yf": "BZ=F",     "opa": "BRENT_CRUDE_USD", "unit": "$/bbl",    "group": "Oil"},
    {"key": "wti",     "name": "WTI crude (NYMEX, M1)",     "yf": "CL=F",     "opa": "WTI_USD",         "unit": "$/bbl",    "group": "Oil"},
    {"key": "rbob",    "name": "RBOB gasoline (NYMEX)",     "yf": "RB=F",     "opa": None,              "unit": "$/gal",    "group": "Oil"},
    {"key": "ho",      "name": "ULSD / heating oil (NYMEX)","yf": "HO=F",     "opa": None,              "unit": "$/gal",    "group": "Oil"},
    {"key": "hh",      "name": "Henry Hub gas (NYMEX)",     "yf": "NG=F",     "opa": "NATURAL_GAS_USD", "unit": "$/MMBtu",  "group": "Gas"},
    {"key": "ttf",     "name": "TTF gas (ICE Endex)",       "yf": "TTF=F",    "opa": "DUTCH_TTF_EUR",   "unit": "EUR/MWh",  "group": "Gas"},
    {"key": "jkm",     "name": "JKM LNG (Asia)",            "yf": None,       "opa": "JKM_LNG_USD",     "unit": "$/MMBtu",  "group": "Gas"},
    {"key": "coal",    "name": "Newcastle thermal coal",    "yf": None,       "opa": "NEWCASTLE_COAL_USD", "unit": "$/t",   "group": "Coal"},
    {"key": "carbon",  "name": "EU carbon (EUA)",           "yf": None,       "opa": "EU_CARBON_EUR",   "unit": "EUR/t",    "group": "Coal"},
    {"key": "copper",  "name": "Copper (COMEX, LME proxy)", "yf": "HG=F",     "opa": None,              "unit": "$/lb",     "group": "Metals"},
    {"key": "alu",     "name": "Aluminium (COMEX)",         "yf": "ALI=F",    "opa": None,              "unit": "$/t",      "group": "Metals"},
    {"key": "gold",    "name": "Gold (COMEX)",              "yf": "GC=F",     "opa": "GOLD_USD",        "unit": "$/oz",     "group": "Metals"},
    {"key": "wheat",   "name": "Wheat (CBOT)",              "yf": "ZW=F",     "opa": None,              "unit": "c/bu",     "group": "Agri"},
    {"key": "corn",    "name": "Corn (CBOT)",               "yf": "ZC=F",     "opa": None,              "unit": "c/bu",     "group": "Agri"},
    {"key": "eurusd",  "name": "EUR/USD",                   "yf": "EURUSD=X", "opa": None,              "unit": "",         "group": "Macro"},
    {"key": "dxy",     "name": "US dollar index",           "yf": "DX-Y.NYB", "opa": None,              "unit": "",         "group": "Macro"},
    {"key": "us10y",   "name": "US 10y yield",              "yf": "^TNX",     "opa": None,              "unit": "%",        "group": "Macro"},
]

# Explicit futures contracts for M1-M2 structure. Yahoo symbols look like CLV26.NYM.
MONTH_CODES = "FGHJKMNQUVXZ"
CURVE_ROOTS = {"wti": "CL", "brent": "BZ"}


def month_contracts(root: str, start: dt.date, n: int = 5) -> list[tuple[str, str]]:
    """Return [(label, yahoo_symbol)] for the next n delivery months from `start`."""
    out = []
    y, m = start.year, start.month
    for _ in range(n):
        code = MONTH_CODES[m - 1]
        out.append((f"{root}{code}{y % 100:02d}", f"{root}{code}{y % 100:02d}.NYM"))
        m += 1
        if m > 12:
            m, y = 1, y + 1
    return out


# ---------------------------------------------------------------------------
# Layer 1: yfinance
# ---------------------------------------------------------------------------

def _closes_from_download(df, ticker):
    """Extract a clean close series for `ticker` from a yf.download frame."""
    import pandas as pd  # local import so --help works without deps

    if df is None or df.empty:
        return None
    if isinstance(df.columns, pd.MultiIndex):
        if ticker not in df.columns.get_level_values(0):
            return None
        sub = df[ticker]
    else:
        sub = df
    if "Close" not in sub:
        return None
    s = sub["Close"].dropna()
    return s if not s.empty else None


def fetch_yahoo(tickers: list[str], period: str, errors: list[str]) -> dict:
    """Return {ticker: {"last", "prior", "week_ago", "asof"}} for tickers that worked."""
    if not tickers:
        return {}
    try:
        import yfinance as yf
        df = yf.download(tickers, period=period, interval="1d", group_by="ticker",
                         auto_adjust=False, progress=False, threads=True)
    except Exception as exc:  # network blocked, library error, etc.
        errors.append(f"yfinance download failed: {exc.__class__.__name__}: {exc}")
        return {}
    out = {}
    for t in tickers:
        try:
            s = _closes_from_download(df, t)
            if s is None:
                errors.append(f"{t}: no data returned")
                continue
            out[t] = {
                "last": float(s.iloc[-1]),
                "prior": float(s.iloc[-2]) if len(s) >= 2 else None,
                "week_ago": float(s.iloc[-6]) if len(s) >= 6 else None,
                "asof": str(s.index[-1].date()),
            }
        except Exception as exc:
            errors.append(f"{t}: {exc.__class__.__name__}: {exc}")
    return out


# ---------------------------------------------------------------------------
# Layer 2: OilPriceAPI (optional)
# ---------------------------------------------------------------------------

def fetch_oilpriceapi(codes: list[str], errors: list[str]) -> dict:
    key = os.environ.get("OILPRICEAPI_KEY")
    if not key or not codes:
        return {}
    import requests
    out = {}
    for code in codes:
        try:
            r = requests.get(
                "https://api.oilpriceapi.com/v1/prices/latest",
                params={"by_code": code},
                headers={"Authorization": f"Token {key}", "Content-Type": "application/json"},
                timeout=20,
            )
            r.raise_for_status()
            d = r.json().get("data") or {}
            price = d.get("price")
            if price is None:
                errors.append(f"OilPriceAPI {code}: no price in response")
                continue
            out[code] = {"last": float(price), "asof": d.get("created_at"), "currency": d.get("currency")}
        except Exception as exc:
            errors.append(f"OilPriceAPI {code}: {exc.__class__.__name__}: {exc}")
    return out


# ---------------------------------------------------------------------------
# Assemble
# ---------------------------------------------------------------------------

def build(date: str, period: str) -> dict:
    errors: list[str] = []
    yf_tickers = [i["yf"] for i in INSTRUMENTS if i["yf"]]
    today = dt.date.fromisoformat(date)
    curve = {k: month_contracts(root, today) for k, root in CURVE_ROOTS.items()}
    curve_syms = [sym for pairs in curve.values() for _, sym in pairs]

    yahoo = fetch_yahoo(yf_tickers + curve_syms, period, errors)
    opa = fetch_oilpriceapi([i["opa"] for i in INSTRUMENTS if i["opa"]], errors)

    rows = []
    by_key = {}
    for inst in INSTRUMENTS:
        y = yahoo.get(inst["yf"]) if inst["yf"] else None
        o = opa.get(inst["opa"]) if inst["opa"] else None
        row = {
            "key": inst["key"], "name": inst["name"], "unit": inst["unit"], "group": inst["group"],
            "yahoo": y, "oilpriceapi": o,
        }
        # Preferred value: Yahoo (exchange close, with history for % change); OilPriceAPI fills gaps.
        if y:
            row.update({"last": y["last"], "day_pct": sp.pct_change(y["last"], y["prior"]),
                        "week_pct": sp.pct_change(y["last"], y["week_ago"]),
                        "asof": y["asof"], "source": f"Yahoo Finance {inst['yf']}"})
        elif o:
            row.update({"last": o["last"], "day_pct": None, "week_pct": None,
                        "asof": o.get("asof"), "source": f"OilPriceAPI {inst['opa']}"})
        else:
            row.update({"last": None, "day_pct": None, "week_pct": None, "asof": None, "source": None})
        rows.append(row)
        by_key[inst["key"]] = row

    def v(key):
        return by_key[key]["last"] if key in by_key else None

    # Curve structure: keep contracts that have a close on the latest date seen.
    structure = {}
    for k, pairs in curve.items():
        pts = [(label, yahoo[sym]) for label, sym in pairs if sym in yahoo]
        if not pts:
            structure[k] = {"m1": None, "m2": None, "spread": None, "label": "n/a", "contracts": []}
            continue
        latest = max(p["asof"] for _, p in pts)
        live = [(label, p) for label, p in pts if p["asof"] == latest]
        m1 = live[0][1]["last"] if len(live) >= 1 else None
        m2 = live[1][1]["last"] if len(live) >= 2 else None
        spread = sp.time_spread(m1, m2)
        structure[k] = {
            "m1": m1, "m2": m2, "spread": spread, "label": sp.structure_label(spread),
            "contracts": [{"label": label, "last": p["last"], "asof": p["asof"]} for label, p in live],
        }

    ttf_mmbtu = sp.eur_mwh_to_usd_mmbtu(v("ttf"), v("eurusd"))
    spreads_out = {
        "brent_wti": sp.brent_wti(v("brent"), v("wti")),
        "brent_m1_m2": structure["brent"]["spread"],
        "brent_structure": structure["brent"]["label"],
        "wti_m1_m2": structure["wti"]["spread"],
        "wti_structure": structure["wti"]["label"],
        "crack_321": sp.crack_321(v("wti"), v("rbob"), v("ho")),
        "gasoline_crack": sp.simple_crack(v("rbob"), v("wti")),
        "distillate_crack": sp.simple_crack(v("ho"), v("wti")),
        "ttf_usd_mmbtu": ttf_mmbtu,
        "ttf_minus_hh": sp.gas_spread(ttf_mmbtu, v("hh")),
        "jkm_minus_ttf": sp.gas_spread(v("jkm"), ttf_mmbtu),
        "brent_oil_parity_mmbtu": sp.usd_bbl_to_usd_mmbtu(v("brent")),
        "copper_usd_t": sp.usd_lb_to_usd_tonne(v("copper")),
        "wheat_usd_bu": sp.cents_bu_to_usd_bu(v("wheat")),
        "corn_usd_bu": sp.cents_bu_to_usd_bu(v("corn")),
    }

    return {
        "date": date,
        "fetched_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "sources": {"yahoo": bool(yahoo), "oilpriceapi": bool(opa)},
        "instruments": rows,
        "structure": structure,
        "spreads": spreads_out,
        "errors": errors,
    }


READ_THROUGH = {
    "brent_wti": "Wide = US export arb open / transatlantic freight bid; narrow = US crude tight.",
    "brent_m1_m2": "Backwardation = prompt tightness, storage draws; contango = surplus, storage pays.",
    "wti_m1_m2": "Watch Cushing stocks; steep backwardation rewards holding spot barrels.",
    "crack_321": "Refinery margin proxy. High cracks = product tightness, refiners run hard.",
    "ttf_minus_hh": "US LNG arb to Europe (needs roughly $3-4/MMBtu to cover liquefaction + shipping).",
    "jkm_minus_ttf": "Positive = Asia pulls cargoes away from Europe.",
    "brent_oil_parity_mmbtu": "Oil-indexed LNG contracts reference this; compare with TTF/JKM.",
}


def to_markdown(d: dict) -> str:
    L = [f"# Prices {d['date']} (fetched {d['fetched_at_utc']})", ""]
    L += ["| Instrument | Last | Unit | Day % | Week % | As of | Source |", "|---|---|---|---|---|---|---|"]
    for r in d["instruments"]:
        L.append(f"| {r['name']} | {sp.fmt(r['last'], 4 if r['unit'] in ('$/gal', '') else 2)} | {r['unit']} | "
                 f"{sp.fmt_signed(r['day_pct'], 1, '%')} | {sp.fmt_signed(r['week_pct'], 1, '%')} | "
                 f"{r['asof'] or 'n/a'} | {r['source'] or 'n/a'} |")
    s = d["spreads"]
    L += ["", "## Spreads and structure", "", "| Spread | Value | Read-through |", "|---|---|---|"]
    rows = [
        ("Brent - WTI", sp.fmt(s["brent_wti"], 2, " $/bbl"), READ_THROUGH["brent_wti"]),
        ("Brent M1-M2", f"{sp.fmt_signed(s['brent_m1_m2'], 2, ' $/bbl')} ({s['brent_structure']})", READ_THROUGH["brent_m1_m2"]),
        ("WTI M1-M2", f"{sp.fmt_signed(s['wti_m1_m2'], 2, ' $/bbl')} ({s['wti_structure']})", READ_THROUGH["wti_m1_m2"]),
        ("3-2-1 crack (WTI/RBOB/ULSD)", sp.fmt(s["crack_321"], 2, " $/bbl"), READ_THROUGH["crack_321"]),
        ("Gasoline crack", sp.fmt(s["gasoline_crack"], 2, " $/bbl"), "RBOB x 42 - WTI"),
        ("Distillate crack", sp.fmt(s["distillate_crack"], 2, " $/bbl"), "ULSD x 42 - WTI"),
        ("TTF in $/MMBtu", sp.fmt(s["ttf_usd_mmbtu"], 2), "EUR/MWh x EURUSD / 3.412"),
        ("TTF - Henry Hub", sp.fmt(s["ttf_minus_hh"], 2, " $/MMBtu"), READ_THROUGH["ttf_minus_hh"]),
        ("JKM - TTF", sp.fmt(s["jkm_minus_ttf"], 2, " $/MMBtu"), READ_THROUGH["jkm_minus_ttf"]),
        ("Brent oil parity", sp.fmt(s["brent_oil_parity_mmbtu"], 2, " $/MMBtu"), READ_THROUGH["brent_oil_parity_mmbtu"]),
        ("Copper in $/t", sp.fmt(s["copper_usd_t"], 0), "COMEX $/lb x 2204.62 (LME proxy)"),
        ("Wheat / corn $/bu", f"{sp.fmt(s['wheat_usd_bu'])} / {sp.fmt(s['corn_usd_bu'])}", "CBOT cents/bu / 100"),
    ]
    for name, val, note in rows:
        L.append(f"| {name} | {val} | {note} |")
    for k in ("brent", "wti"):
        c = d["structure"][k]["contracts"]
        if c:
            L.append("")
            L.append(f"{k.upper()} curve: " + ", ".join(f"{x['label']} {sp.fmt(x['last'])}" for x in c))
    if d["errors"]:
        L += ["", "## Errors (shown as n/a above)", ""] + [f"- {e}" for e in d["errors"]]
    L += ["", "_Indicative prices from public sources (Yahoo Finance ~15 min delayed"
          + (", OilPriceAPI" if d["sources"]["oilpriceapi"] else "") + "). Not tradeable quotes._"]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", default=dt.date.today().isoformat())
    ap.add_argument("--period", default="15d", help="yfinance history window (default 15d)")
    ap.add_argument("--no-write", action="store_true")
    a = ap.parse_args()

    d = build(a.date, a.period)
    md = to_markdown(d)
    print(md)
    if not a.no_write:
        DATA_DIR.mkdir(exist_ok=True)
        (DATA_DIR / f"prices-{a.date}.json").write_text(json.dumps(d, indent=2))
        (DATA_DIR / f"prices-{a.date}.md").write_text(md)
        print(f"wrote data/prices-{a.date}.json and .md", file=sys.stderr)
    ok = any(r["last"] is not None for r in d["instruments"])
    if not ok:
        print("WARNING: no instrument returned a price (network blocked?)", file=sys.stderr)
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
