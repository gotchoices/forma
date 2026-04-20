"""
R60 Track 15 — Phase 3: nuclear scaling under (3, 6) proton base.

Using the (3, 6) calibration from Phase 1 and the composite α rule
from Phase 2, test whether nuclear masses for d, ⁴He, ¹²C, ⁵⁶Fe
can be reproduced with the new scaling law:

    n_pt = 3A, n_pr = 6A, n_et = 1 − Z

This was model-D's historical dealbreaker for (3, 6).
Tests whether model-F's σ_ra-augmented architecture rescues it.

Sandboxed.  No changes to model-F.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok,
    alpha_coulomb, mode_6_to_11, derive_L_ring,
    L_vector_from_params, mode_energy,
    ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI, M_E_MEV, M_P_MEV,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF, modelF_baseline
from track15_phase2_alpha import alpha_sum_composite, gcd_safe


NUCLEI = [
    ("d (²H)",   2,   1,  1875.6128),
    ("⁴He",      4,   2,  3727.379),
    ("¹²C",     12,   6, 11177.929),
    ("⁵⁶Fe",    56,  26, 52089.77),
]


def main():
    print("=" * 72)
    print("R60 Track 15 — Phase 3: nuclear scaling on (3, 6) base")
    print("=" * 72)
    print()

    # Recalibrated L_ring_p for (3, 6) proton at m_p (Phase 1 Option A.2)
    L_ring_p_36 = derive_L_ring(M_P_MEV, 3, 6, 0.55, 0.162037, K_MODELF)
    print(f"  Using (3, 6) proton calibration:")
    print(f"    (ε_p, s_p) = (0.55, 0.162037)")
    print(f"    L_ring_p = {L_ring_p_36:.4f} fm")
    print(f"    k = {K_MODELF:.4e}")
    print()

    # Build the (3, 6)-calibrated metric
    p = modelF_baseline(L_ring_p=L_ring_p_36)
    G = build_aug_metric(p)
    L = L_vector_from_params(p)

    if not signature_ok(G):
        print("  WARNING: signature broken on (3, 6) baseline.  Abort.")
        return

    # Verify proton mass
    E_p_check = mode_energy(G, L, mode_6_to_11((0, 0, 0, 0, 3, 6)))
    print(f"  Proton mass check: {E_p_check:.4f} MeV  (target {M_P_MEV})")
    print()

    # ── Primary nuclear scaling test ──
    print("─" * 72)
    print("Primary: (n_et, n_pt, n_pr) = (1-Z, 3A, 6A)")
    print("─" * 72)
    print()
    print(f"  {'Nucleus':<10s}  {'A':>3s}  {'Z':>3s}  "
          f"{'(n_et,n_pt,n_pr)':<20s}  "
          f"{'E predicted':>12s}  {'target':>12s}  "
          f"{'Δ':>9s}  {'α comp':>8s}  {'α bare':>8s}")

    for label, A, Z, target in NUCLEI:
        n_et = 1 - Z
        n_pt = 3 * A
        n_pr = 6 * A
        n6 = (n_et, 0, 0, 0, n_pt, n_pr)
        n11 = mode_6_to_11(n6)
        E_pred = mode_energy(G, L, n11)
        rel = (E_pred - target) / target

        # α check under composite rule
        a_comp_sum = alpha_sum_composite(n6)
        a_comp = a_comp_sum ** 2
        a_bare_sum = n6[0] - n6[4] + n6[2]
        a_bare = a_bare_sum ** 2

        tuple_str = f"({n_et},{n_pt},{n_pr})"
        print(f"  {label:<10s}  {A:>3d}  {Z:>3d}  {tuple_str:<20s}  "
              f"{E_pred:>12.4f}  {target:>12.4f}  {rel:>+9.4%}  "
              f"{a_comp:>8d}  {a_bare:>8d}")
    print()

    # ── Decoration search ──
    print("─" * 72)
    print("Decorated search: best (n_er, n_νr) per nucleus (±3 range)")
    print("─" * 72)
    print()
    print(f"  {'Nucleus':<10s}  {'primary Δ':>12s}  "
          f"{'best decoration':<24s}  {'decorated Δ':>14s}")

    for label, A, Z, target in NUCLEI:
        n_et = 1 - Z
        n_pt = 3 * A
        n_pr = 6 * A
        best = None
        for n_er in range(-3, 4):
            for n_nur in range(-3, 4):
                n6 = (n_et, n_er, 0, n_nur, n_pt, n_pr)
                n11 = mode_6_to_11(n6)
                E = mode_energy(G, L, n11)
                rel = abs(E - target) / target
                if best is None or rel < best[0]:
                    best = (rel, n6, E)
        rel_pri, _, E_pri = None, None, None
        # Get primary too
        n6_pri = (n_et, 0, 0, 0, n_pt, n_pr)
        E_pri = mode_energy(G, L, mode_6_to_11(n6_pri))
        rel_pri = (E_pri - target) / target

        rel_dec, n6_dec, E_dec = best
        sign = "+" if E_dec > target else "-"
        dec_str = f"n_er={n6_dec[1]:+d}, n_νr={n6_dec[3]:+d}"
        print(f"  {label:<10s}  {rel_pri*100:>+11.4f}%  {dec_str:<24s}  "
              f"{sign}{rel_dec*100:>13.4f}%")
    print()

    # ── Summary comparison with model-F Track 11 ──
    print("─" * 72)
    print("Comparison: (3, 6) vs (1, 3) nuclear scaling accuracy")
    print("─" * 72)
    print()
    print(f"  {'Nucleus':<10s}  {'Model-F (1,3) Δ':>16s}  "
          f"{'(3,6) primary Δ':>16s}  {'(3,6) decorated Δ':>18s}")

    # Model-F Track 11 results (from findings-11)
    modelF_primary = {"d (²H)": 0.67, "⁴He": 1.31, "¹²C": 1.35, "⁵⁶Fe": 1.59}
    modelF_decorated = {"d (²H)": 0.05, "⁴He": 0.73, "¹²C": 1.08, "⁵⁶Fe": 1.52}

    for label, A, Z, target in NUCLEI:
        # Re-compute our numbers
        n_et = 1 - Z
        n_pt = 3 * A
        n_pr = 6 * A
        E_pri = mode_energy(G, L, mode_6_to_11(
            (n_et, 0, 0, 0, n_pt, n_pr)))
        rel_pri = abs(E_pri - target) / target

        best = None
        for n_er in range(-3, 4):
            for n_nur in range(-3, 4):
                n6 = (n_et, n_er, 0, n_nur, n_pt, n_pr)
                E = mode_energy(G, L, mode_6_to_11(n6))
                rel = abs(E - target) / target
                if best is None or rel < best:
                    best = rel

        mF_p = modelF_primary.get(label, 0)
        mF_d = modelF_decorated.get(label, 0)
        print(f"  {label:<10s}  {mF_d:>15.2f}%  {rel_pri*100:>15.4f}%  "
              f"{best*100:>17.4f}%")
    print()

    print("Phase 3 complete.")


if __name__ == "__main__":
    main()
