import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import build_dashboard_data as bd  # noqa: E402

SAMPLE_BANK = """# Technical

Intro paragraph.

### Q1. What is contango?
**Difficulty:** 1
**Model answer:** Forward price above spot; carry = storage + finance.
Second line.
**Pushback:**
- Why would it ever pay to store?
- What flips it?
**Red flags:** Confusing it with backwardation.

### Q2. Hedge a cargo
**Difficulty:** 2
**Model answer:** Sell 700 lots.
**Pushback:** - Basis risk?
**Red flags:** No lot maths.
"""


def test_parse_questions():
    qs = bd.parse_questions(SAMPLE_BANK)
    assert [q["n"] for q in qs] == [1, 2]
    assert qs[0]["question"] == "What is contango?"
    assert qs[0]["difficulty"] == 1
    assert qs[0]["model_answer"].startswith("Forward price above spot")
    assert "Second line." in qs[0]["model_answer"]
    assert qs[0]["pushback"].startswith("- Why would it ever pay")
    assert qs[0]["red_flags"] == "Confusing it with backwardation."
    assert qs[1]["difficulty"] == 2


def test_build_from_tmp_repo(tmp_path):
    (tmp_path / "data").mkdir(); (tmp_path / "briefs").mkdir(); (tmp_path / "questions").mkdir(); (tmp_path / "networking").mkdir()
    for date, brent in (("2026-09-01", 94.0), ("2026-09-02", 95.35)):
        (tmp_path / "data" / f"prices-{date}.json").write_text(json.dumps({
            "date": date, "instruments": [{"key": "brent", "last": brent, "history": [{"date": date, "close": brent}]},
                                          {"key": "wti", "last": brent - 4.6}],
            "spreads": {"brent_wti": 4.6, "brent_m1_m2": 3.7, "crack_321": 61.0, "ttf_usd_mmbtu": 24.9},
            "structure": {}, "errors": []}))
    (tmp_path / "data" / "news-2026-09-02.json").write_text(json.dumps({"date": "2026-09-02", "sectors": {"Oil": []}}))
    (tmp_path / "briefs" / "2026-09-01.md").write_text("# old")
    (tmp_path / "briefs" / "2026-09-02.md").write_text("# Commodities Brief - 2026-09-02")
    (tmp_path / "questions" / "technical.md").write_text(SAMPLE_BANK)
    (tmp_path / "networking" / "tuesday-cheatsheet.md").write_text("# cheat")
    d = bd.build(tmp_path)
    assert d["prices"]["date"] == "2026-09-02"
    assert d["brief"]["date"] == "2026-09-02" and d["briefs_index"] == ["2026-09-01", "2026-09-02"]
    assert [r["date"] for r in d["daily"]] == ["2026-09-01", "2026-09-02"]
    assert d["daily"][1]["brent"] == 95.35 and d["daily"][1]["crack_321"] == 61.0
    assert d["history"]["brent"][0]["close"] == 94.0 or d["history"]["brent"][-1]["close"] == 95.35
    assert len(d["questions"]["technical"]) == 2 and d["questions"]["behavioural"] == []
    assert d["cheatsheet"] == "# cheat"
    html = bd.inline("<title>x</title><body></body>", d)
    assert html.startswith("<title>x</title>\n<script>window.__DATA__ = {")


def test_real_repo_banks_parse():
    d = bd.build()
    for bank in bd.BANKS:
        assert len(d["questions"][bank]) == 20, bank
        assert all(q["model_answer"] and q["pushback"] for q in d["questions"][bank]), bank


def _hist(vals):
    return [{"date": d, "close": v} for d, v in vals]


def test_daily_from_history_and_override():
    prices = {
        "date": "2026-09-03",
        "instruments": [
            {"key": "brent", "last": 96.0, "history": _hist([("2026-09-01", 94.0), ("2026-09-02", 95.0), ("2026-09-03", 96.0)])},
            {"key": "wti", "last": 91.0, "history": _hist([("2026-09-01", 90.0), ("2026-09-02", 90.5), ("2026-09-03", 91.0)])},
            {"key": "rbob", "last": 3.0, "history": _hist([("2026-09-01", 3.0), ("2026-09-02", 3.0), ("2026-09-03", 3.0)])},
            {"key": "ho", "last": 4.5, "history": _hist([("2026-09-01", 4.5), ("2026-09-02", 4.5), ("2026-09-03", 4.5)])},
            {"key": "ttf", "last": 70.0, "history": _hist([("2026-09-01", 68.24), ("2026-09-03", 70.0)])},
            {"key": "eurusd", "last": 1.0, "history": _hist([("2026-09-01", 1.0), ("2026-09-02", 1.0), ("2026-09-03", 1.0)])},
            {"key": "hh", "last": 3.0, "history": _hist([("2026-09-01", 3.0), ("2026-09-03", 3.0)])},
            {"key": "copper", "last": 4.0, "history": _hist([("2026-09-03", 4.0)])},
        ],
        "structure": {"brent": {"contracts": [
            {"label": "BZX26", "last": 96.0, "history": _hist([("2026-09-01", 94.0), ("2026-09-03", 96.0)])},
            {"label": "BZZ26", "last": 92.0, "history": _hist([("2026-09-01", 91.0), ("2026-09-03", 92.0)])}]},
            "wti": {"contracts": []}},
        "spreads": {}, "errors": [],
    }
    rows, note = bd.daily_from_history(prices)
    assert [r["date"] for r in rows] == ["2026-09-01", "2026-09-02", "2026-09-03"]
    r1, r2, r3 = rows
    assert abs(r1["brent_wti"] - 4.0) < 1e-9
    assert abs(r1["crack_321"] - ((2 * 3.0 * 42 + 4.5 * 42) / 3 - 90.0)) < 1e-9
    assert abs(r1["ttf_usd_mmbtu"] - 68.24 / 3.412) < 1e-9 and abs(r1["ttf_minus_hh"] - (68.24 / 3.412 - 3.0)) < 1e-9
    assert r2["ttf_usd_mmbtu"] is None and r2["brent_m1_m2"] is None  # no TTF or contract close that day
    assert abs(r1["brent_m1_m2"] - 3.0) < 1e-9 and abs(r3["brent_m1_m2"] - 4.0) < 1e-9
    assert r3["wti_m1_m2"] is None and abs(r3["copper_usd_t"] - 4.0 * 2204.62) < 1e-6
    assert "3 days recomputed" in note and "BZX26-BZZ26" in note


def test_build_merges_committed_rows_over_history(tmp_path):
    (tmp_path / "data").mkdir(); (tmp_path / "briefs").mkdir(); (tmp_path / "questions").mkdir(); (tmp_path / "networking").mkdir()
    (tmp_path / "data" / "prices-2026-09-03.json").write_text(json.dumps({
        "date": "2026-09-03",
        "instruments": [{"key": "brent", "last": 96.5, "history": _hist([("2026-09-02", 95.0), ("2026-09-03", 96.0)])},
                        {"key": "wti", "last": 91.5, "history": _hist([("2026-09-02", 90.5), ("2026-09-03", 91.0)])}],
        "spreads": {"brent_wti": 5.0}, "structure": {}, "errors": []}))
    d = bd.build(tmp_path)
    assert [r["date"] for r in d["daily"]] == ["2026-09-02", "2026-09-03"]
    assert d["daily"][0]["source"] == "history" and abs(d["daily"][0]["brent_wti"] - 4.5) < 1e-9
    assert d["daily"][1]["source"] == "daily" and d["daily"][1]["brent"] == 96.5 and d["daily"][1]["brent_wti"] == 5.0
    assert "2 days recomputed" in d["daily_note"] and "1 day(s) from the committed" in d["daily_note"]
