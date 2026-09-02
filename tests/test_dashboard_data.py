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
