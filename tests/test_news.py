import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import fetch_news as fn  # noqa: E402


def test_recent_sorted_filters_and_orders():
    now = dt.datetime(2026, 9, 2, 22, 0, tzinfo=dt.timezone.utc)
    items = [
        {"title": "old", "published": "Mon, 06 Jul 2026 00:52:16 GMT"},
        {"title": "yesterday", "published": "Tue, 01 Sep 2026 08:00:00 GMT"},
        {"title": "today", "published": "Wed, 02 Sep 2026 14:00:00 +0000"},
        {"title": "gdelt", "published": "20260901T120000Z"},
        {"title": "undated", "published": ""},
    ]
    out = [i["title"] for i in fn.recent_sorted(items, now=now)]
    assert out == ["today", "gdelt", "yesterday", "undated"]


def test_dedupe():
    items = [{"title": "Same headline"}, {"title": "same HEADLINE"}, {"title": "Other"}]
    assert [i["title"] for i in fn.dedupe(items)] == ["Same headline", "Other"]
