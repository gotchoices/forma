"""
Numerical spot-check of work/quark-search.md §4 negative result.

For 3 dims (m1 < m2 < m3) and 3 pairs (P12, P13, P23), pairs P12 and P13
share L_b = L1.  In the pure-ring regime, the lighter-mode mass on a pair
is m_A ≈ 2π·ℏc·f/L_b where f ∈ [0, 1/2] is the detuning of the closest
m_r integer to σ_eff.  The within-pair mass ratio m_B/m_A = (1−f)/f fixes
f from the observed within-generation mass ratio.

If we assign two generations to P12 and P13, the sharing constraint
L_b(P12) = L_b(P13) = L1 forces the L_b values *derived from each pair's
lighter quark mass* to agree.  This script enumerates all three (P12, P13)
assignments and reports the inconsistency.

Outputs to outputs/quark_search_sharing_check.txt.
"""

from __future__ import annotations

from math import pi
from pathlib import Path


HBARC_MEV_FM = 197.3269804
COEFF = 2 * pi * HBARC_MEV_FM  # ~ 1239.84 MeV·fm

QUARK_MASSES_MEV = {
    "u": 2.16,    "d": 4.67,
    "s": 93.0,    "c": 1270.0,
    "b": 4180.0,  "t": 173000.0,
}


def f_from_ratio(r: float) -> float:
    """Solve (1 - f) / f = r for f in [0, 1/2]."""
    return 1.0 / (1.0 + r)


def Lb_from_lighter(m_lighter_MeV: float, f: float) -> float:
    """Pure-ring regime: m ≈ 2π·ℏc·f/L_b → L_b = 2π·ℏc·f/m."""
    return COEFF * f / m_lighter_MeV


def main() -> None:
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "quark_search_sharing_check.txt"

    assignments = [
        ("A", ("u", "d"), ("s", "c"), "(u,d) on P12, (s,c) on P13"),
        ("B", ("u", "d"), ("b", "t"), "(u,d) on P12, (b,t) on P13"),
        ("C", ("s", "c"), ("b", "t"), "(s,c) on P12, (b,t) on P13"),
    ]

    lines = []
    lines.append("Sharing-constraint spot-check for work/quark-search.md §4")
    lines.append("=" * 90)
    lines.append("")
    lines.append("For each assignment, derive L_b from the lighter quark of each pair, "
                 "given f from the within-pair mass ratio.")
    lines.append("Sharing requires L_b(P12) = L_b(P13) = L_1.  Inconsistency falsifies "
                 "the 3-dim hypothesis.")
    lines.append("")
    lines.append(f"{'A':<3s} {'P12 gen':<12s} {'P13 gen':<12s} "
                 f"{'f_{12}':>10s} {'f_{13}':>10s} "
                 f"{'L_b from P12':>16s} {'L_b from P13':>16s} {'ratio':>10s} {'OK?':>6s}")
    lines.append("-" * 95)
    for label, (q1, q2), (q3, q4), _desc in assignments:
        r12 = QUARK_MASSES_MEV[q2] / QUARK_MASSES_MEV[q1]
        r13 = QUARK_MASSES_MEV[q4] / QUARK_MASSES_MEV[q3]
        f12 = f_from_ratio(r12)
        f13 = f_from_ratio(r13)
        Lb12 = Lb_from_lighter(QUARK_MASSES_MEV[q1], f12)
        Lb13 = Lb_from_lighter(QUARK_MASSES_MEV[q3], f13)
        ratio = max(Lb12, Lb13) / min(Lb12, Lb13)
        ok = "yes" if ratio < 1.05 else f"NO"
        lines.append(f"{label:<3s} ({q1},{q2}){'':<6s} ({q3},{q4}){'':<6s} "
                     f"{f12:>10.4f} {f13:>10.4f} "
                     f"{Lb12:>14.4f}fm {Lb13:>14.4f}fm {ratio:>10.1f} {ok:>6s}")
    lines.append("")
    lines.append("Verdict: every assignment fails by ≥100×. The 3-dim ground rules "
                 "(lowest-mode windings + per-pair σ/χ/τ + 3 dims) cannot fit the "
                 "6 observed quark masses.")

    text = "\n".join(lines)
    print(text)
    with open(out_path, "w") as f:
        f.write(text + "\n")
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
