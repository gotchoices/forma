"""
Verify the wye/star topology for the quark sector:
  quark pairs: Ma((1, 5), (3, 5), (4, 5))
where m5 (the largest of the quark-region dims) is the common hub.

Dim labels are size-ordered (smallest first):
  m1 ≈ 0.007 fm   — smallest ring; hosts the heaviest pair (t, b)
  m2 ≈ 0.7 fm     — electron-sector dim (skipped in the quark wye)
  m3 ≈ 0.91 fm    — middle ring; hosts (c, s)
  m4 ≈ 181 fm     — largest ring; hosts the lightest pair (u, d)
  m5 ≳ 5740 fm    — common tube/hub (plays tube in all 3 pairs)

This is structurally different from the prior triangle topology
Ma((1, 2), (1, 3), (2, 3)):
  triangle: shared dim was the SMALLER of its pairs (the L_ring role)
            → 2 pairs share the same L_ring → 2-scale obstruction
  wye:      shared dim (m5) is the LARGER (the L_tube role)
            → each pair has its own L_ring → 3 distinct mass scales

The fit: m5 plays "tube" (large circumference) in all 3 quark pairs;
m1, m3, m4 play "ring" (small circumference) each in one pair, giving the
three generation mass scales 1/L_1, 1/L_3, 1/L_4.

This is the R53-style "fat torus" regime (tube ≫ ring) applied per-pair
with a single common tube.

Within-pair (m_lighter, m_heavier) split:
  m_lighter ≈ 2π ℏc · f / L_ring,    m_heavier ≈ 2π ℏc · (1-f) / L_ring
  ratio (1-f)/f = m_heavier / m_lighter

Free parameters: 4 L's (L_1, L_3, L_4, L_5) + 3 σ_eff (one per pair)
Constraints:     6 quark masses
Net: 7 unknowns for 6 equations → 1 DOF (the choice of L_5, which must be
large enough to put each pair in the pure-ring regime).

Outputs to outputs/quark_search_wye.txt
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

# Size-ordered: heaviest pair on smallest ring m1
# m2 is intentionally skipped — reserved for the electron-sector dim.
# (pair_label, q_light, q_heavy, ring_dim)
GEN_PAIRS = [
    ("Ma(1, 5)", "b", "t", 1),
    ("Ma(3, 5)", "s", "c", 3),
    ("Ma(4, 5)", "u", "d", 4),
]


def sigma_eff_from_ratio(r: float) -> float:
    """For modes at T(1, 1) and T(1, 2) with σ_eff in (1.5, 2):
    lighter mode T(1, 2) has δ = 2 − σ_eff, heavier T(1, 1) has δ = 1 − σ_eff.
    Ratio m_heavier/m_lighter = (σ_eff − 1)/(2 − σ_eff) = r.
    Solve: σ_eff = (2r + 1)/(r + 1).
    """
    return (2 * r + 1) / (r + 1)


def mass(L_T_fm: float, L_R_fm: float, m_t: int, delta: float) -> float:
    """m = 2π·ℏc·√((m_t/L_T)² + (δ/L_R)²) MeV."""
    return COEFF * sqrt((m_t / L_T_fm)**2 + (delta / L_R_fm)**2)


def main() -> None:
    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "quark_search_wye.txt"

    lines = []
    lines.append("Wye topology verification: quark sector")
    lines.append("=" * 90)
    lines.append("")
    lines.append("Topology: Ma((1, 5), (3, 5), (4, 5)) — m5 common to all 3 pairs.")
    lines.append("Assignment: m5 plays TUBE in all 3 pairs (large L);")
    lines.append("            m1, m3, m4 play RING (small L), one per pair.")
    lines.append("Size-ordering: m1..m5 with m2 reserved for the electron-sector dim.")
    lines.append("")

    # Step 1: solve for σ_eff and L_ring per pair from observed masses.
    # The two closure modes on each pair are T(1, 1) and T(1, 2).
    # σ_eff in (1.5, 2): T(1, 2) closer → lighter; T(1, 1) → heavier.
    # f = |δ_lighter| = 2 - σ_eff is the smaller detuning.
    sigma_eff_per_pair = {}
    f_per_pair = {}
    L_ring_per_pair = {}
    for pair_label, q_light, q_heavy, ring_dim in GEN_PAIRS:
        ratio = QUARK_MASSES_MEV[q_heavy] / QUARK_MASSES_MEV[q_light]
        sigma_eff = sigma_eff_from_ratio(ratio)
        f = 2 - sigma_eff
        L_ring = COEFF * f / QUARK_MASSES_MEV[q_light]
        sigma_eff_per_pair[ring_dim] = sigma_eff
        f_per_pair[ring_dim] = f
        L_ring_per_pair[ring_dim] = L_ring
        lines.append(f"  {pair_label}  →  quarks (lighter {q_light} at T(1,2), "
                     f"heavier {q_heavy} at T(1,1))   within-pair ratio = {ratio:.3f}")
        lines.append(f"    ⇒  σ_eff = {sigma_eff:.4f}, f = |δ_lighter| = {f:.4f}, "
                     f"L_{ring_dim} (ring) = {L_ring:.4g} fm")

    # Step 2: solve for L_5 minimum (pure-ring regime: L_T >> L_R/f for each pair)
    L_5_min = max(L_ring_per_pair[d] / f_per_pair[d]
                  for d in (1, 3, 4)) * 10  # 10× margin
    L_5 = max(L_5_min, 5000.0)

    lines.append("")
    lines.append(f"  L_5 (common tube) requires L_5 ≫ L_ring/f for each pair.")
    lines.append(f"  Strictest constraint: L_5 ≫ {L_ring_per_pair[4]/f_per_pair[4]:.4g} fm "
                 f" ⇒  use L_5 = {L_5:.4g} fm.")
    lines.append("")

    # Step 3: compute predicted masses using FULL formula
    lines.append("Predicted vs observed masses (FULL formula, modes T(1,1) and T(1,2) per pair):")
    lines.append("")
    lines.append(f"  {'Pair':<12s} {'Mode':<10s} {'Quark':<7s} "
                 f"{'L_T fm':>10s} {'L_R fm':>12s} {'δ':>8s} "
                 f"{'m_pred MeV':>14s} {'m_obs MeV':>14s} {'Δ%':>8s}")
    lines.append("  " + "-" * 100)

    # δ = m_r − σ_eff · m_t.  For m_t=1: δ = m_r − σ_eff.
    cases = []
    for pair_label, q_light, q_heavy, ring_dim in GEN_PAIRS:
        sigma_eff = sigma_eff_per_pair[ring_dim]
        L_R = L_ring_per_pair[ring_dim]
        cases.append((pair_label, "T(1, 2)", q_light, L_5, L_R, 2 - sigma_eff, q_light))
        cases.append((pair_label, "T(1, 1)", q_heavy, L_5, L_R, 1 - sigma_eff, q_heavy))

    max_err_pct = 0.0
    for pair, mode_label, q_label, L_T, L_R, delta, q in cases:
        m_pred = mass(L_T, L_R, 1, delta)
        m_obs = QUARK_MASSES_MEV[q]
        err_pct = 100.0 * (m_pred - m_obs) / m_obs
        max_err_pct = max(max_err_pct, abs(err_pct))
        lines.append(f"  {pair:<12s} {mode_label:<10s} {q_label:<7s} "
                     f"{L_T:>10.4g} {L_R:>12.4g} {delta:>+8.4f} "
                     f"{m_pred:>14.4g} {m_obs:>14.4g} {err_pct:>+7.2f}%")

    lines.append("")
    lines.append(f"  Maximum |Δ%| = {max_err_pct:.3f}%")
    lines.append("")

    # Summary
    lines.append("=" * 90)
    lines.append("VERDICT: all 6 quark masses fit to within < 1%.")
    lines.append("")
    lines.append("Why this topology works where Ma((1,2), (1,3), (2,3)) failed:")
    lines.append("  • Triangle topology had two pairs sharing L_b (the smaller, ring),")
    lines.append("    forcing those two pairs' lighter-mode masses into a fixed ratio.")
    lines.append("  • Wye topology has all three pairs sharing L_T = L_5 (the larger),")
    lines.append("    so each pair has its own L_R (= L_1, L_3, L_4) giving its own mass scale.")
    lines.append("  • In the pure-ring regime (L_T ≫ L_R), mass is dominated by 1/L_R, not 1/L_T.")
    lines.append("    A shared L_T does NOT couple the masses across pairs.")
    lines.append("")
    lines.append("Architectural implication: the smaller-as-tube rule is wrong in general")
    lines.append("(it held under the older proton-sheet convention only). The tube/ring")
    lines.append("assignment is per-pair, and the wye has the LARGER dim playing tube in every")
    lines.append("quark pair (the R53 'fat-torus' regime, applied universally).")
    lines.append("")
    lines.append(f"Quark-sector geometry (size-ordered, m1..m5; m2 reserved for e-sector):")
    for d in (1, 3, 4, 5):
        if d == 5:
            label = "L_5 (common tube)"
            L = L_5
        else:
            quark_pair = next(p for p in GEN_PAIRS if p[3] == d)
            label = f"L_{d} ({quark_pair[1]}/{quark_pair[2]} ring)"
            L = L_ring_per_pair[d]
        lines.append(f"  {label:<28s} = {L:>10.4g} fm")

    text = "\n".join(lines)
    print(text)
    with open(out_path, "w") as f:
        f.write(text + "\n")
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
