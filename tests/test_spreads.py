import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import spreads as s  # noqa: E402


def approx(a, b, tol=1e-6):
    return math.isclose(a, b, abs_tol=tol)


def test_brent_wti():
    assert approx(s.brent_wti(95.68, 91.85), 3.83)
    assert s.brent_wti(None, 91.85) is None


def test_time_spread_and_label():
    assert approx(s.time_spread(95.68, 94.90), 0.78)
    assert s.structure_label(0.78) == "backwardation"
    assert s.structure_label(-0.40) == "contango"
    assert s.structure_label(0.02) == "flat"
    assert s.structure_label(None) == "n/a"


def test_crack_321_hand_checked():
    # 2*2.60*42 = 218.4 ; 3.00*42 = 126 ; (218.4+126)/3 = 114.8 ; minus 90 = 24.8
    assert approx(s.crack_321(90.0, 2.60, 3.00), 24.8)
    assert s.crack_321(90.0, None, 3.00) is None


def test_simple_crack():
    assert approx(s.simple_crack(2.60, 90.0), 19.2)


def test_ttf_conversion():
    # 35 EUR/MWh at 1.10 EURUSD = 38.5 $/MWh / 3.412 = 11.284 $/MMBtu
    assert approx(s.eur_mwh_to_usd_mmbtu(35.0, 1.10), 38.5 / 3.412)
    assert approx(s.gas_spread(11.284, 3.0), 8.284)


def test_copper_and_grains():
    assert approx(s.usd_lb_to_usd_tonne(4.50), 9920.79)
    assert approx(s.cents_bu_to_usd_bu(550.25), 5.5025)


def test_oil_parity_gas():
    assert approx(s.usd_bbl_to_usd_mmbtu(58.0), 10.0)


def test_pct_change():
    assert approx(s.pct_change(110, 100), 10.0)
    assert s.pct_change(110, 0) is None
    assert s.pct_change(None, 100) is None


def test_fmt():
    assert s.fmt(None) == "n/a"
    assert s.fmt(1234.5678) == "1,234.57"
    assert s.fmt_signed(1.5, 1, "%") == "+1.5%"
    assert s.fmt_signed(-0.25) == "-0.25"
