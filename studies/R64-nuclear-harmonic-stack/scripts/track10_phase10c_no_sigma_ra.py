"""
R64 Track 10 Phase 10c — Architecture test: σ_ra = 0, with direct sheet-S
couplings replacing the role σ_ra plays in R60.

Premise (user proposal): the architectural picture might simplify if
aleph mediates ONLY the charge (tube) sector, while the mass (ring)
sector couples to S directly.  R60 T7 derived σ_ra = (s·ε)·σ_ta to
preserve α universality.  This phase tests whether σ_ra can be set to
zero AND replaced by direct sheet-S couplings (σ_pS_tube + σ_pS_ring)
that jointly preserve α.

Tests:

1. Baseline check: does setting σ_ra = 0 (with no other change) break
   α universality?  (Expected yes per R60 T7c.)

2. Compensation search: with σ_ra = 0, find σ_pS_tube and σ_pS_ring
   values that restore α universality.  If a prescription exists, the
   user's architectural simplification works.

3. Magnitude check: compare the resulting σ_eff at signature boundary
   to Phases 9 and 10a.  Does dropping σ_ra and using sheet-S directly
   give us more headroom?

Outputs:
  outputs/track10_phase10c_no_sigma_ra.csv
  outputs/track10_phase10c_no_sigma_ra.png
"""

import os
import sys
import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

R60_SCRIPTS = Path(__file__).resolve().parent.parent.parent / "R60-metric-11" / "scripts"
sys.path.insert(0, str(R60_SCRIPTS))

from track1_solver import (    # noqa: E402
    Params, alpha_coulomb, mode_6_to_11, num_negative_eigs,
    ALPHA, SQRT_ALPHA, FOUR_PI, HBAR_C_MEV_FM,
    I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING, I_NU_TUBE, I_NU_RING,
    I_ALEPH, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import track9_params    # noqa: E402


TEST_MODES = [
    ("electron", (1, 2, 0, 0, 0, 0)),
    ("muon",     (1, 1, -2, -2, 0, 0)),
    ("proton",   (0, 0, 0, 0, 1, 3)),
    ("neutron",  (0, -4, -1, 2, 0, -3)),
    ("Lambda",   (-1, 2, -1, 2, -1, 3)),
    ("Sigma_-",  (-1, 2, -2, 2, -2, -2)),
    ("pi0",      (0, -1, -2, -2, 0, 0)),
    ("pi_pm",    (-1, -1, -3, -3, 0, 0)),
    ("K_pm",     (-1, -6, -2, 2, 0, 1)),
    ("rho",      (-1, 5, -2, 2, 0, 1)),
]


def expected_alpha_sum_squared(tup):
    n_et, _, n_νt, _, n_pt, _ = tup
    return (n_et - n_pt + n_νt) ** 2


def alpha_spread(G):
    values = []
    for label, tup in TEST_MODES:
        n11 = mode_6_to_11(tup)
        a = alpha_coulomb(G, n11)
        sq = expected_alpha_sum_squared(tup)
        if sq > 0:
            values.append(a / (ALPHA * sq))
    if not values:
        return float('inf')
    return max(values) - min(values)


def build_metric_no_sigma_ra(p, **entries):
    """Build R60 metric, then ZERO OUT σ_ra entries on all sheets,
    then add direct sheet-S couplings."""
    sigma_at_offset = entries.pop('sigma_at_offset', 0.0)
    p_modified = p.copy_with(sigma_at=p.sigma_at + sigma_at_offset)
    G = build_aug_metric(p_modified).copy()

    # Zero σ_ra entries: these are at G[I_X_RING, I_ALEPH] for each sheet
    for ring_idx in (I_E_RING, I_P_RING, I_NU_RING):
        G[ring_idx, I_ALEPH] = 0.0
        G[I_ALEPH, ring_idx] = 0.0

    # Add direct sheet-S couplings as before
    def add(idx_a, idx_b, value):
        if value:
            G[idx_a, idx_b] += value
            G[idx_b, idx_a] += value

    for s_idx in (I_SX, I_SY, I_SZ):
        add(I_P_TUBE, s_idx, entries.get('sigma_pS_tube', 0.0))
        add(I_P_RING, s_idx, entries.get('sigma_pS_ring', 0.0))
        add(I_E_TUBE, s_idx, entries.get('sigma_eS_tube', 0.0))
        add(I_E_RING, s_idx, entries.get('sigma_eS_ring', 0.0))
        add(I_NU_TUBE, s_idx, entries.get('sigma_νS_tube', 0.0))
        add(I_NU_RING, s_idx, entries.get('sigma_νS_ring', 0.0))
        add(I_ALEPH, s_idx, entries.get('sigma_aS', 0.0))

    return G


def schur_effective_sigma_pS_tube(G):
    G_inv = np.linalg.inv(G)
    g_pp = G[I_P_TUBE, I_P_TUBE]
    g_SS = G[I_SX, I_SX]
    return -G_inv[I_P_TUBE, I_SX] * g_pp * g_SS


def schur_effective_sigma_pS_ring(G):
    G_inv = np.linalg.inv(G)
    g_pr = G[I_P_RING, I_P_RING]
    g_SS = G[I_SX, I_SX]
    return -G_inv[I_P_RING, I_SX] * g_pr * g_SS


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 10 Phase 10c — σ_ra = 0 + direct sheet-S coupling test")
    print("=" * 100)
    print()

    p = track9_params()

    # ─── Part 1: σ_ra = 0 alone ───
    print("=" * 80)
    print("Part 1 — Baseline: zero out σ_ra, no other change")
    print("=" * 80)
    print()
    G_no_ra = build_metric_no_sigma_ra(p)
    sig_ok = num_negative_eigs(G_no_ra) == 1
    spread = alpha_spread(G_no_ra)
    print(f"  Signature OK (one negative eigenvalue): {sig_ok}")
    print(f"  α universality spread: {spread:.4e}")
    print()

    # Mode-by-mode α/α_expected
    print(f"  {'mode':<10s}  {'α/α_expected':>14s}")
    for label, tup in TEST_MODES:
        n11 = mode_6_to_11(tup)
        a = alpha_coulomb(G_no_ra, n11)
        sq = expected_alpha_sum_squared(tup)
        if sq > 0:
            ratio = a / (ALPHA * sq)
            print(f"  {label:<10s}  {ratio:>14.6f}")
        else:
            print(f"  {label:<10s}  (uncharged)")
    print()
    if spread < 1e-6:
        print("  → Surprisingly, σ_ra = 0 ALONE preserves α universality.")
        print("    R60 T7's σ_ra prescription may be redundant for this")
        print("    inventory.  Skipping compensation search.")
        sigma_ra_redundant = True
    else:
        print(f"  → σ_ra = 0 breaks α universality with spread {spread:.4e}.")
        print("    This is the expected R60 T7c finding.  Now searching for")
        print("    direct sheet-S compensation that restores universality.")
        sigma_ra_redundant = False
    print()

    # ─── Part 2: Compensation search with σ_ra = 0 ───
    print("=" * 80)
    print("Part 2 — Compensation: with σ_ra = 0, find sheet-S entries")
    print("                       that restore α universality")
    print("=" * 80)
    print()

    # Search hypotheses
    def cost_C1(coeffs, dummy, p):
        # σ_pS_tube + σ_pS_ring jointly
        a, b = coeffs
        G = build_metric_no_sigma_ra(
            p, sigma_pS_tube=a, sigma_pS_ring=b,
        )
        if num_negative_eigs(G) != 1:
            return 1.0
        return alpha_spread(G)

    def cost_C2(coeffs, dummy, p):
        # σ_pS_tube + σ_pS_ring + σ_aS
        a, b, c = coeffs
        G = build_metric_no_sigma_ra(
            p, sigma_pS_tube=a, sigma_pS_ring=b, sigma_aS=c,
        )
        if num_negative_eigs(G) != 1:
            return 1.0
        return alpha_spread(G)

    def cost_C3(coeffs, dummy, p):
        # All three sheets' tube and ring + σ_aS
        # 3-sheet symmetric extension of C1
        a, b = coeffs   # σ_pS_tube · 1, σ_pS_ring · 1; e and ν follow R60-T7-style
        # Use the R64 H5 prescription proportions: c_e = 1.207, c_ν = -0.207
        sigma_p_tube = a
        sigma_p_ring = b
        sigma_e_tube = 1.207 * a
        sigma_e_ring = (p.s_e * p.eps_e) * sigma_e_tube  # R60-T7 style
        sigma_n_tube = -0.207 * a
        sigma_n_ring = (p.s_nu * p.eps_nu) * sigma_n_tube  # R60-T7 style
        G = build_metric_no_sigma_ra(
            p,
            sigma_pS_tube=sigma_p_tube, sigma_pS_ring=sigma_p_ring,
            sigma_eS_tube=sigma_e_tube, sigma_eS_ring=sigma_e_ring,
            sigma_νS_tube=sigma_n_tube, sigma_νS_ring=sigma_n_ring,
        )
        if num_negative_eigs(G) != 1:
            return 1.0
        return alpha_spread(G)

    HYPS = {
        "C1: σ_pS_tube + σ_pS_ring":
            (cost_C1, ['a', 'b'], np.array([0.01, 0.01])),
        "C2: σ_pS_tube + σ_pS_ring + σ_aS":
            (cost_C2, ['a', 'b', 'c'], np.array([0.01, 0.01, 0.01])),
        "C3: 3-sheet symmetric (R60-T7 style ring companions)":
            (cost_C3, ['a', 'b'], np.array([0.01, 0.01])),
    }

    best_global = None
    if not sigma_ra_redundant:
        for hyp_name, (cost_fn, params, x0) in HYPS.items():
            print(f"  --- {hyp_name} ---")
            param_header = "  ".join(f"{n:>10s}" for n in params)
            print(f"    {param_header}  {'α-spread':>12s}")
            # Try multiple starting points to avoid local minima
            best_for_hyp = None
            for trial in range(5):
                x0_trial = x0 + np.random.randn(len(x0)) * 0.05
                result = minimize(
                    cost_fn, x0_trial,
                    args=(None, p),
                    method='Nelder-Mead',
                    options={'xatol': 1e-12, 'fatol': 1e-14,
                              'maxiter': 20000},
                )
                if best_for_hyp is None or result.fun < best_for_hyp.fun:
                    best_for_hyp = result
            params_str = "  ".join(f"{v:+10.6f}" for v in best_for_hyp.x)
            verdict = ("exact" if best_for_hyp.fun < 1e-9 else
                       "good" if best_for_hyp.fun < 1e-3 else "fail")
            print(f"    {params_str}  {best_for_hyp.fun:>12.4e}  {verdict}")
            print()

            if best_global is None or best_for_hyp.fun < best_global[2]:
                best_global = (hyp_name, best_for_hyp.x, best_for_hyp.fun, params)

    # ─── Part 3: Verdict ───
    print("=" * 100)
    print("VERDICT — Phase 10c: σ_ra = 0 with direct sheet-S replacement")
    print("=" * 100)
    print()
    if sigma_ra_redundant:
        print("  σ_ra = 0 surprisingly preserves α universality with no")
        print("  compensation needed.  The R60 T7 prescription σ_ra = (s·ε)·σ_ta")
        print("  may not be necessary at the working parameters used here.")
        print("  Architectural implication: aleph row simplifies — only σ_ta and")
        print("  σ_at non-zero.  Ring sector entirely outside aleph.")
    elif best_global is not None and best_global[2] < 1e-9:
        hyp, coeffs, spread, params = best_global
        print(f"  Best prescription: {hyp}")
        print(f"    Coefficients: " +
              ", ".join(f"{n}={v:+.6f}" for n, v in zip(params, coeffs)))
        print(f"    α-spread: {spread:.4e}")
        print()
        print("  The user's architectural proposal works: σ_ra = 0 can be")
        print("  replaced by direct sheet-S couplings.  The aleph row no longer")
        print("  needs the ring entries, simplifying the structure.")

        # Test signature band under this prescription
        if hyp.startswith("C1"):
            a, b = coeffs
            G_test = build_metric_no_sigma_ra(p, sigma_pS_tube=a, sigma_pS_ring=b)
            sigma_eff_t = schur_effective_sigma_pS_tube(G_test)
            sigma_eff_r = schur_effective_sigma_pS_ring(G_test)
            print(f"    σ_eff_tube = {sigma_eff_t:+.6f}")
            print(f"    σ_eff_ring = {sigma_eff_r:+.6f}")
    else:
        if best_global is not None:
            hyp, coeffs, spread, params = best_global
            print(f"  Best prescription found: {hyp}")
            print(f"    α-spread: {spread:.4e} (not exact)")
        print("  Direct sheet-S coupling does NOT cleanly replace σ_ra.")
        print("  σ_ra appears structurally necessary for α universality —")
        print("  R60 T7's prescription is genuine, not redundant.")
        print()
        print("  The user's architectural proposal does not survive this test.")
    print()


if __name__ == "__main__":
    main()
