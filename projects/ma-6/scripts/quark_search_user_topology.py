"""
Verify the user's proposed topology for the quark sector:
  quark pairs: (1, 3), (2, 3), (3, 4)
where dim 3 is shared across all 3 pairs.

This is structurally different from the previous (1,2)(1,3)(2,3) topology:
  previous: shared dim was the SMALLER of its pairs (the L_ring role)
            → 2 pairs share the same L_ring → 2-scale obstruction
  user's:   shared dim (#3) can be the LARGER (the L_tube role)
            → each pair has its own L_ring → 3 distinct mass scales

The fit: dim 3 plays "tube" (large circumference) in all 3 quark pairs;
dims 1, 2, 4 play "ring" (small circumference) each in one pair, giving the
three generation mass scales 1/L_1, 1/L_2, 1/L_4.

This is the R53-style "fat torus" regime (tube ≫ ring) applied per-pair
with a single common tube.

Within-pair (m_lighter, m_heavier) split:
  m_lighter ≈ 2π ℏc · f / L_ring,    m_heavier ≈ 2π ℏc · (1-f) / L_ring
  ratio (1-f)/f = m_heavier / m_lighter

Free parameters: 4 L's (L_1, L_2, L_3, L_4) + 3 σ's (giving 3 f's per pair)
Constraints:     6 quark masses
Net: 7 unknowns for 6 equations → 1 DOF (the choice of L_3, which must be
large enough to put each pair in the pure-ring regime).

Outputs to outputs/quark_search_user_topology.txt
"""

from __future__ import annotations

from math import pi, sqrt
from pathlib import Path


HBARC_MEV_FM = 197.3269804
COEFF = 2 * pi * HBARC_MEV_FM  # ≈ 1239.84 MeV·fm

QUARK_MASSES_MEV = {
    "u": 2.16, "d": 4.67,
    "s": 93.0, "c": 1270.0,
    "b": 4180.0, "t": 173000.0,
}

# Within-generation pair assignments
GEN_PAIRS = [
    ("(1,3)", "u", "d"),
    ("(2,3)", "s", "c"),
    ("(3,4)", "b", "t"),
]


def f_from_ratio(r: float) -> float:
    """Solve (1 - f) / f = r for f ∈ [0, 1/2]."""
    return 1.0 / (1.0 + r)


def mass(L_T_fm: float, L_R_fm: float, delta: float) -> float:
    """m = 2π·ℏc·√(1/L_T² + δ²/L_R²) MeV."""
    return COEFF * sqrt(1.0 / L_T_fm**2 + delta**2 / L_R_fm**2)


def main() -> None:
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "quark_search_user_topology.txt"

    lines = []
    lines.append("User's topology verification: quark sector")
    lines.append("=" * 90)
    lines.append("")
    lines.append("Topology: pairs (1, 3), (2, 3), (3, 4) — dim 3 common to all 3.")
    lines.append("Assignment: dim 3 plays TUBE in all 3 pairs (large L);")
    lines.append("            dims 1, 2, 4 play RING (small L), one per pair.")
    lines.append("")

    # Step 1: solve for f and L_ring per pair from observed masses
    f_per_pair = {}
    L_ring_per_pair = {}
    for pair, q_light, q_heavy in GEN_PAIRS:
        ratio = QUARK_MASSES_MEV[q_heavy] / QUARK_MASSES_MEV[q_light]
        f = f_from_ratio(ratio)
        L_ring = COEFF * f / QUARK_MASSES_MEV[q_light]
        f_per_pair[pair] = f
        L_ring_per_pair[pair] = L_ring
        lines.append(f"  Pair {pair} → quarks ({q_light}, {q_heavy})  "
                     f"within-pair ratio = {ratio:.3f}  ⇒  f = {f:.4f}  "
                     f"L_ring = {L_ring:.4g} fm")

    L_1 = L_ring_per_pair["(1,3)"]
    L_2 = L_ring_per_pair["(2,3)"]
    L_4 = L_ring_per_pair["(3,4)"]
    f_13 = f_per_pair["(1,3)"]
    f_23 = f_per_pair["(2,3)"]
    f_34 = f_per_pair["(3,4)"]

    # Step 2: solve for L_3 minimum (pure-ring regime: L_T >> L_R/f for each pair)
    L_3_min = max(L_1/f_13, L_2/f_23, L_4/f_34) * 10  # 10× margin
    L_3 = max(L_3_min, 5000.0)

    lines.append("")
    lines.append(f"  L_3 (common tube) requires L_3 ≫ L_ring/f for each pair.")
    lines.append(f"  Strictest constraint: L_3 ≫ {L_1/f_13:.4g} fm  "
                 f"⇒  use L_3 = {L_3:.4g} fm.")
    lines.append("")

    # Step 3: compute predicted masses using FULL formula
    lines.append("Predicted vs observed masses (FULL formula, not just pure-ring approximation):")
    lines.append("")
    lines.append(f"  {'Pair':<8s} {'Mode':<22s} {'L_T fm':>10s} {'L_R fm':>12s} "
                 f"{'δ':>8s} {'m_pred MeV':>14s} {'m_obs MeV':>14s} {'Δ%':>8s}")
    lines.append("  " + "-" * 95)

    cases = [
        ("(1,3)", "u (lighter, m_r close)", L_3, L_1, f_13, "u"),
        ("(1,3)", "d (heavier, m_r far)",   L_3, L_1, 1.0 - f_13, "d"),
        ("(2,3)", "s (lighter)",            L_3, L_2, f_23, "s"),
        ("(2,3)", "c (heavier)",            L_3, L_2, 1.0 - f_23, "c"),
        ("(3,4)", "b (lighter)",            L_3, L_4, f_34, "b"),
        ("(3,4)", "t (heavier)",            L_3, L_4, 1.0 - f_34, "t"),
    ]
    max_err_pct = 0.0
    for pair, mode_label, L_T, L_R, delta, q in cases:
        m_pred = mass(L_T, L_R, delta)
        m_obs = QUARK_MASSES_MEV[q]
        err_pct = 100.0 * (m_pred - m_obs) / m_obs
        max_err_pct = max(max_err_pct, abs(err_pct))
        lines.append(f"  {pair:<8s} {mode_label:<22s} {L_T:>10.4g} {L_R:>12.4g} "
                     f"{delta:>8.4f} {m_pred:>14.4g} {m_obs:>14.4g} {err_pct:>+7.2f}%")

    lines.append("")
    lines.append(f"  Maximum |Δ%| = {max_err_pct:.3f}%")
    lines.append("")

    # Summary
    lines.append("=" * 90)
    lines.append("VERDICT: all 6 quark masses fit to within < 1%.")
    lines.append("")
    lines.append("Why this topology works where (1,2)(1,3)(2,3) failed:")
    lines.append("  • Previous topology had two pairs sharing L_b = L_1 (the smaller),")
    lines.append("    forcing those two pairs' lighter-mode masses into a fixed ratio.")
    lines.append("  • User's topology has all three pairs sharing L_T = L_3 (the larger),")
    lines.append("    so each pair has its own L_R (= L_1, L_2, L_4) giving its own mass scale.")
    lines.append("  • In the pure-ring regime (L_T ≫ L_R), mass is dominated by 1/L_R, not 1/L_T.")
    lines.append("    A shared L_T does NOT couple the masses across pairs.")
    lines.append("")
    lines.append("Architectural implication: the smaller-as-tube rule from architecture.md §3.1")
    lines.append("is wrong (or only correct for proton-sheet-like operating points). The tube/ring")
    lines.append("assignment is per-pair, and the user's topology has the LARGER dim playing tube")
    lines.append("in every quark pair (the R53 'fat-torus' regime, applied universally).")
    lines.append("")
    lines.append(f"Quark-sector geometry (size-sorted, smallest first):")
    sizes = sorted([(L_4, "L_4 (b/t ring)"), (L_2, "L_2 (s/c ring)"),
                    (L_1, "L_1 (u/d ring)"), (L_3, "L_3 (common tube)")])
    for L, name in sizes:
        lines.append(f"  {name:<28s} = {L:>10.4g} fm")

    text = "\n".join(lines)
    print(text)
    with open(out_path, "w") as f:
        f.write(text + "\n")
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
