"""Offline pipeline test: canned Yahoo closes -> prices json -> Tier 0 brief."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import build_brief  # noqa: E402
import fetch_prices  # noqa: E402

FIXTURE = Path(__file__).parent / "fixtures" / "yahoo_sample.json"


def canned_yahoo(tickers, period, errors):
    data = json.loads(FIXTURE.read_text())
    out = {t: data[t] for t in tickers if t in data}
    for t in tickers:
        if t not in data:
            errors.append(f"{t}: no data returned")
    return out


def test_build_prices_with_fixture(monkeypatch):
    monkeypatch.setattr(fetch_prices, "fetch_yahoo", canned_yahoo)
    monkeypatch.delenv("OILPRICEAPI_KEY", raising=False)
    d = fetch_prices.build("2026-09-02", "15d")
    by = {r["key"]: r for r in d["instruments"]}
    assert by["brent"]["last"] == 95.68
    assert abs(by["brent"]["day_pct"] - (95.68 - 94.65) / 94.65 * 100) < 1e-9
    assert by["jkm"]["last"] is None  # not on Yahoo, no OilPriceAPI key
    assert by["brent"]["history"][-1] == {"date": "2026-09-01", "close": 95.68}
    assert by["wti"]["history"] == []
    assert "history" not in by["brent"]["yahoo"]
    s = d["spreads"]
    assert abs(s["brent_wti"] - (95.68 - 91.85)) < 1e-9
    assert abs(s["crack_321"] - ((2 * 2.60 * 42 + 3.00 * 42) / 3 - 91.85)) < 1e-9
    # curve: CLV26 and CLX26 have the latest date; CLU26 is stale (expired) and ignored
    assert d["structure"]["wti"]["m1"] == 91.85
    assert d["structure"]["wti"]["m2"] == 91.10
    assert d["structure"]["wti"]["label"] == "backwardation"
    assert d["structure"]["brent"]["label"] == "n/a"
    assert any("JKM" in e or "no data" in e for e in d["errors"])
    md = fetch_prices.to_markdown(d)
    assert "| Brent crude (ICE, M1) | 95.68 |" in md
    assert "n/a" in md  # missing rows are explicit


def test_tier0_brief(monkeypatch, tmp_path):
    monkeypatch.setattr(fetch_prices, "fetch_yahoo", canned_yahoo)
    monkeypatch.delenv("OILPRICEAPI_KEY", raising=False)
    prices = fetch_prices.build("2026-09-02", "15d")
    news = {"date": "2026-09-02", "sectors": {"Oil": [{"title": "OPEC+ holds output", "link": "https://example.com/a",
                                                        "published": "Tue, 01 Sep 2026", "source": "Reuters"}],
                                              "Metals": []}, "errors": []}
    md = build_brief.tier0("2026-09-02", prices, news)
    assert md.startswith("# Commodities Brief - 2026-09-02")
    assert "## 1. Headline numbers" in md and "## 2. Spreads and structure" in md
    assert "[OPEC+ holds output](https://example.com/a)" in md
    assert "### Metals\n- n/a" in md
    assert "not tradeable" in md


def test_tier0_without_files():
    md = build_brief.tier0("2026-01-01", None, None)
    assert "no prices file" in md and "no news file" in md
