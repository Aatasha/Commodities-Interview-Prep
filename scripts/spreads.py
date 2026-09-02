"""Pure spread and unit-conversion maths for the commodities brief.

No network access here so it can be unit-tested anywhere. All functions accept
floats (or None) and return None when any input is missing, so callers can
print "n/a" instead of guessing.
"""
from __future__ import annotations

from typing import Optional

BBL_PER_TONNE_CRUDE = 7.33      # rough Brent-type crude; varies 6.3-7.9 by grade
GAL_PER_BBL = 42
MMBTU_PER_MWH = 3.412           # 1 MWh = 3.412 MMBtu
MMBTU_PER_BBL_CRUDE = 5.8       # energy content of a barrel of crude
LB_PER_TONNE = 2204.62
BU_PER_TONNE_WHEAT = 36.74
BU_PER_TONNE_CORN = 39.37


def _ok(*vals) -> bool:
    return all(v is not None for v in vals)


def brent_wti(brent: Optional[float], wti: Optional[float]) -> Optional[float]:
    """Brent minus WTI in $/bbl. Wide = US export arb open, transatlantic freight/quality."""
    return brent - wti if _ok(brent, wti) else None


def time_spread(m1: Optional[float], m2: Optional[float]) -> Optional[float]:
    """Front month minus second month. Positive = backwardation, negative = contango."""
    return m1 - m2 if _ok(m1, m2) else None


def structure_label(spread: Optional[float], flat_band: float = 0.05) -> str:
    if spread is None:
        return "n/a"
    if spread > flat_band:
        return "backwardation"
    if spread < -flat_band:
        return "contango"
    return "flat"


def product_gal_to_bbl(price_per_gal: Optional[float]) -> Optional[float]:
    """RBOB / heating oil trade in $/gal on NYMEX; convert to $/bbl."""
    return price_per_gal * GAL_PER_BBL if _ok(price_per_gal) else None


def crack_321(wti_bbl: Optional[float], rbob_gal: Optional[float], ho_gal: Optional[float]) -> Optional[float]:
    """3-2-1 crack spread in $/bbl: 3 bbl crude -> 2 bbl gasoline + 1 bbl distillate."""
    if not _ok(wti_bbl, rbob_gal, ho_gal):
        return None
    return (2 * rbob_gal * GAL_PER_BBL + ho_gal * GAL_PER_BBL) / 3 - wti_bbl


def simple_crack(product_gal: Optional[float], crude_bbl: Optional[float]) -> Optional[float]:
    """Single-product crack, $/bbl (e.g. gasoline crack = RBOB*42 - WTI)."""
    if not _ok(product_gal, crude_bbl):
        return None
    return product_gal * GAL_PER_BBL - crude_bbl


def eur_mwh_to_usd_mmbtu(eur_mwh: Optional[float], eurusd: Optional[float]) -> Optional[float]:
    """TTF is quoted in EUR/MWh; Henry Hub and JKM in $/MMBtu."""
    if not _ok(eur_mwh, eurusd):
        return None
    return eur_mwh * eurusd / MMBTU_PER_MWH


def gas_spread(a_mmbtu: Optional[float], b_mmbtu: Optional[float]) -> Optional[float]:
    """Generic $/MMBtu spread (e.g. TTF - Henry Hub, JKM - TTF)."""
    return a_mmbtu - b_mmbtu if _ok(a_mmbtu, b_mmbtu) else None


def usd_lb_to_usd_tonne(price_lb: Optional[float]) -> Optional[float]:
    """COMEX copper is $/lb; LME is $/tonne."""
    return price_lb * LB_PER_TONNE if _ok(price_lb) else None


def cents_bu_to_usd_bu(price_c: Optional[float]) -> Optional[float]:
    """CBOT grains quote in cents per bushel."""
    return price_c / 100 if _ok(price_c) else None


def usd_bbl_to_usd_mmbtu(price_bbl: Optional[float]) -> Optional[float]:
    """Oil-parity for gas: $/bbl divided by ~5.8 MMBtu per bbl."""
    return price_bbl / MMBTU_PER_BBL_CRUDE if _ok(price_bbl) else None


def pct_change(latest: Optional[float], prior: Optional[float]) -> Optional[float]:
    if not _ok(latest, prior) or prior == 0:
        return None
    return (latest - prior) / prior * 100


def fmt(v: Optional[float], nd: int = 2, suffix: str = "") -> str:
    """Format a number or return 'n/a'."""
    if v is None:
        return "n/a"
    return f"{v:,.{nd}f}{suffix}"


def fmt_signed(v: Optional[float], nd: int = 2, suffix: str = "") -> str:
    if v is None:
        return "n/a"
    return f"{v:+,.{nd}f}{suffix}"
