"""
R64 Track 9 Phases 9a/9b — σ_pS structural-prescription search.

Goal: find σ_pS_tube as a function of other R60 metric entries such that
α universality is preserved across the inventory at non-zero σ_pS_tube.

Strategy: hypothesize candidate compensation structures (analogous to
R60 T7's σ_ra = (s·ε)·σ_ta), search numerically for compensation
coefficients that minimize the universality deviation, examine the
result for clean structural form.

Hypotheses tested (in order of structural simplicity):

  H1  σ_pS_tube + σ_pS_ring (single companion on the same sheet)
      σ_pS_ring = a · σ_pS_tube — single-coefficient search

  H2  σ_pS_tube + σ_aS (aleph-mediated companion)
      σ_aS = b · σ_pS_tube — single-coefficient search

  H3  σ_pS_tube + σ_pS_ring + σ_aS (joint two-coefficient)
      σ_pS_ring = a · σ_pS_tube,  σ_aS = b · σ_pS_tube

  H4  3-sheet symmetric: σ_eS_tube and σ_νS_tube parallel to σ_pS_tube
      σ_eS_tube = c · σ_pS_tube,  σ_νS_tube = d · σ_pS_tube

  H5  H4 + ring-companion on each sheet (full 6-parameter sheet-S block)
      σ_xS_tube = c_x · σ_pS_tube,  σ_xS_ring = (s_x·ε_x)·σ_xS_tube
      analogous to σ_ra = (s·ε)·σ_ta on each sheet

For each hypothesis: scipy.optimize.minimize finds the coefficients
that minimize max α-deviation across the 10-mode inventory.  If a
hypothesis achieves machine-precision universality across a range
of σ_pS_tube test values with consistent coefficients, we have a
structural prescription.

Outputs:
  outputs/track9_prescription_search.csv
  outputs/track9_universality_curves.png
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
    alpha_coulomb, mode_6_to_11, num_negative_eigs,
    ALPHA, SQRT_ALPHA, FOUR_PI,
    I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING, I_NU_TUBE, I_NU_RING,
    I_ALEPH, I_SX, I_SY, I_SZ, I_T,
)
from track7b_resolve import build_aug_metric    # noqa: E402
from track10_hadron_inventory import track9_params    # noqa: E402


# ─── Test modes (model-F inventory, same as Phase 7e) ──────────────

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
    """Bare α-formula: α/α₀ = (n_et − n_pt + n_νt)²."""
    n_et, _, n_νt, _, n_pt, _ = tup
    return (n_et - n_pt + n_νt) ** 2


# ─── Augmented metric with companions ──────────────────────────────

def build_augmented_metric(
    p,
    sigma_pS_tube=0.0,
    sigma_pS_ring=0.0,
    sigma_aS=0.0,
    sigma_eS_tube=0.0,
    sigma_eS_ring=0.0,
    sigma_νS_tube=0.0,
    sigma_νS_ring=0.0,
):
    """R60 model-F baseline + arbitrary sheet-S off-diagonals."""
    G = build_aug_metric(p).copy()
    for s_idx in (I_SX, I_SY, I_SZ):
        if sigma_pS_tube:
            G[I_P_TUBE, s_idx] += sigma_pS_tube
            G[s_idx, I_P_TUBE] += sigma_pS_tube
        if sigma_pS_ring:
            G[I_P_RING, s_idx] += sigma_pS_ring
            G[s_idx, I_P_RING] += sigma_pS_ring
        if sigma_aS:
            G[I_ALEPH, s_idx] += sigma_aS
            G[s_idx, I_ALEPH] += sigma_aS
        if sigma_eS_tube:
            G[I_E_TUBE, s_idx] += sigma_eS_tube
            G[s_idx, I_E_TUBE] += sigma_eS_tube
        if sigma_eS_ring:
            G[I_E_RING, s_idx] += sigma_eS_ring
            G[s_idx, I_E_RING] += sigma_eS_ring
        if sigma_νS_tube:
            G[I_NU_TUBE, s_idx] += sigma_νS_tube
            G[s_idx, I_NU_TUBE] += sigma_νS_tube
        if sigma_νS_ring:
            G[I_NU_RING, s_idx] += sigma_νS_ring
            G[s_idx, I_NU_RING] += sigma_νS_ring
    return G


def compute_alpha_ratios(G):
    """For each test mode, compute α(mode) / expected_baseline.

    Returns: list of (label, ratio).  Ratio = 1.0 means exact universality.
    """
    out = []
    for label, tup in TEST_MODES:
        n11 = mode_6_to_11(tup)
        alpha = alpha_coulomb(G, n11)
        expected_sum_sq = expected_alpha_sum_squared(tup)
        # Baseline α for this mode: α₀ * (n_et − n_pt + n_νt)²
        if expected_sum_sq > 0:
            expected_alpha = ALPHA * expected_sum_sq
            ratio = alpha / expected_alpha
        else:
            # Mode with bare formula α=0 (uncharged); skip in universality check
            ratio = None
        out.append((label, ratio))
    return out


def universality_max_deviation(G):
    """Return max |ratio - 1| across modes, ignoring undefined ratios."""
    ratios = compute_alpha_ratios(G)
    values = [r for _, r in ratios if r is not None and math.isfinite(r)]
    if not values:
        return float('inf')
    return max(abs(v - 1.0) for v in values)


def universality_spread(G):
    """Return max(ratios) - min(ratios) — universality holds if this is 0."""
    ratios = compute_alpha_ratios(G)
    values = [r for _, r in ratios if r is not None and math.isfinite(r)]
    if not values:
        return float('inf')
    return max(values) - min(values)


# ─── Hypotheses ────────────────────────────────────────────────────

def cost_H1(coeffs, sigma_pS_tube, p):
    """H1: σ_pS_ring = a · σ_pS_tube."""
    a, = coeffs
    G = build_augmented_metric(
        p,
        sigma_pS_tube=sigma_pS_tube,
        sigma_pS_ring=a * sigma_pS_tube,
    )
    if num_negative_eigs(G) != 1:
        return 1.0
    return universality_spread(G)


def cost_H2(coeffs, sigma_pS_tube, p):
    """H2: σ_aS = b · σ_pS_tube."""
    b, = coeffs
    G = build_augmented_metric(
        p,
        sigma_pS_tube=sigma_pS_tube,
        sigma_aS=b * sigma_pS_tube,
    )
    if num_negative_eigs(G) != 1:
        return 1.0
    return universality_spread(G)


def cost_H3(coeffs, sigma_pS_tube, p):
    """H3: σ_pS_ring = a · σ_pS_tube AND σ_aS = b · σ_pS_tube."""
    a, b = coeffs
    G = build_augmented_metric(
        p,
        sigma_pS_tube=sigma_pS_tube,
        sigma_pS_ring=a * sigma_pS_tube,
        sigma_aS=b * sigma_pS_tube,
    )
    if num_negative_eigs(G) != 1:
        return 1.0
    return universality_spread(G)


def cost_H4(coeffs, sigma_pS_tube, p):
    """H4: 3-sheet symmetric tubes; σ_eS_tube = c·σ, σ_νS_tube = d·σ."""
    c, d = coeffs
    G = build_augmented_metric(
        p,
        sigma_pS_tube=sigma_pS_tube,
        sigma_eS_tube=c * sigma_pS_tube,
        sigma_νS_tube=d * sigma_pS_tube,
    )
    if num_negative_eigs(G) != 1:
        return 1.0
    return universality_spread(G)


def cost_H5(coeffs, sigma_pS_tube, p):
    """H5: 3-sheet with R60 T7-style ring companions on each sheet.

    σ_pS_ring = (s_p · ε_p) · σ_pS_tube
    σ_eS_tube = c · σ_pS_tube;  σ_eS_ring = (s_e · ε_e) · σ_eS_tube
    σ_νS_tube = d · σ_pS_tube;  σ_νS_ring = (s_ν · ε_ν) · σ_νS_tube
    """
    c, d = coeffs
    sigma_pS_ring = (p.s_p * p.eps_p) * sigma_pS_tube
    sigma_eS_tube = c * sigma_pS_tube
    sigma_eS_ring = (p.s_e * p.eps_e) * sigma_eS_tube
    sigma_νS_tube = d * sigma_pS_tube
    sigma_νS_ring = (p.s_nu * p.eps_nu) * sigma_νS_tube
    G = build_augmented_metric(
        p,
        sigma_pS_tube=sigma_pS_tube,
        sigma_pS_ring=sigma_pS_ring,
        sigma_eS_tube=sigma_eS_tube,
        sigma_eS_ring=sigma_eS_ring,
        sigma_νS_tube=sigma_νS_tube,
        sigma_νS_ring=sigma_νS_ring,
    )
    if num_negative_eigs(G) != 1:
        return 1.0
    return universality_spread(G)


HYPOTHESES = {
    "H1: σ_pS_ring = a·σ":
        (cost_H1, ['a'], np.array([0.0])),
    "H2: σ_aS = b·σ":
        (cost_H2, ['b'], np.array([0.0])),
    "H3: σ_pS_ring=a·σ, σ_aS=b·σ":
        (cost_H3, ['a', 'b'], np.array([0.0, 0.0])),
    "H4: σ_eS_tube=c·σ, σ_νS_tube=d·σ":
        (cost_H4, ['c', 'd'], np.array([1.0, 1.0])),
    "H5: 3-sheet w/ R60-T7 ring companions":
        (cost_H5, ['c', 'd'], np.array([1.0, 1.0])),
}


# ─── Main search ───────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 9 — σ_pS structural-prescription search")
    print("=" * 100)
    print()

    p = track9_params()

    # ─── Baseline check ───
    print("Baseline (σ_pS_tube = 0):")
    G_base = build_aug_metric(p)
    ratios_base = compute_alpha_ratios(G_base)
    print(f"  {'mode':<10s}  {'α/α_expected':>14s}")
    for label, ratio in ratios_base:
        if ratio is None:
            print(f"  {label:<10s}  (uncharged baseline)")
        else:
            print(f"  {label:<10s}  {ratio:>14.10f}")
    base_spread = universality_spread(G_base)
    print(f"  Universality spread (max-min): {base_spread:.2e}")
    print()
    if base_spread > 1e-6:
        print(f"  WARNING: baseline universality is not exact at machine precision.")
        print(f"  This is expected with R60's α-formula on the model-F inventory")
        print(f"  (some modes deviate slightly from the ideal universal formula).")
        print()

    # ─── Phase 7e baseline: σ_pS_tube alone ───
    print("=" * 80)
    print("Phase 7e baseline: σ_pS_tube alone (no companion)")
    print("=" * 80)
    print(f"  {'σ_pS_tube':>10s}  {'α-spread':>12s}  {'mode-by-mode max α/α₀':>20s}")
    for sigma in [0.001, 0.005, 0.01, 0.025, 0.05, 0.10]:
        G = build_augmented_metric(p, sigma_pS_tube=sigma)
        if num_negative_eigs(G) != 1:
            print(f"  {sigma:>10.4f}  signature broken")
            continue
        spread = universality_spread(G)
        ratios = compute_alpha_ratios(G)
        max_r = max((r for _, r in ratios if r is not None), default=float('nan'))
        print(f"  {sigma:>+10.4f}  {spread:>12.4e}  {max_r:>20.4f}")
    print()
    print("  Confirms Phase 7e: σ_pS_tube alone breaks α universality.")
    print()

    # ─── Search each hypothesis ───
    test_sigmas = [0.001, 0.005, 0.01, 0.025, 0.05]
    csv_rows = []

    for hyp_name, (cost_fn, param_names, x0) in HYPOTHESES.items():
        print("=" * 80)
        print(f"  {hyp_name}")
        print("=" * 80)
        param_header = "  ".join(f"{n:>10s}" for n in param_names)
        print(f"  {'σ_pS_tube':>10s}  {param_header}  "
              f"{'α-spread':>12s}  {'verdict':>15s}")

        coeffs_at_each_sigma = []
        for sigma in test_sigmas:
            result = minimize(
                cost_fn, x0,
                args=(sigma, p),
                method='Nelder-Mead',
                options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 5000},
            )
            cost = result.fun
            params_str = "  ".join(f"{v:>+10.6f}" for v in result.x)
            verdict = (
                "exact (≤1e-6)" if cost < 1e-6 else
                "good (≤1e-3)" if cost < 1e-3 else
                "no help"
            )
            print(f"  {sigma:>+10.4f}  {params_str}  "
                  f"{cost:>12.4e}  {verdict:>15s}")
            coeffs_at_each_sigma.append({
                'hypothesis': hyp_name,
                'sigma_pS_tube': sigma,
                **{f'param_{n}': float(v) for n, v in zip(param_names, result.x)},
                'alpha_spread': cost,
                'verdict': verdict,
            })
            csv_rows.extend([{**coeffs_at_each_sigma[-1]}])

        # Check if coefficients are consistent across σ_pS_tube values
        if len(coeffs_at_each_sigma) >= 3:
            for i, name in enumerate(param_names):
                vals = [r[f'param_{name}'] for r in coeffs_at_each_sigma]
                rel_var = (max(vals) - min(vals)) / (abs(np.mean(vals)) + 1e-15)
                if abs(np.mean(vals)) > 1e-6:
                    consistency = "consistent" if rel_var < 0.05 else "inconsistent"
                    print(f"    {name}: mean = {np.mean(vals):+.6f}, "
                          f"rel-var = {rel_var:.2e}  [{consistency}]")
        print()

    # ─── Save CSV ───
    csv_path = out_dir / "track9_prescription_search.csv"
    with open(csv_path, 'w', newline='') as f:
        if csv_rows:
            all_keys = sorted(set().union(*(r.keys() for r in csv_rows)))
            w = csv.DictWriter(f, fieldnames=all_keys)
            w.writeheader()
            for r in csv_rows:
                w.writerow(r)
    print(f"  CSV: {csv_path}")
    print()

    # ─── Verdict ───
    print("=" * 100)
    print("VERDICT — Phase 9a/9b prescription search")
    print("=" * 100)
    print()

    # Find the hypothesis that achieved the smallest spread at largest sigma
    best_results = {}
    for r in csv_rows:
        h = r['hypothesis']
        s = r['sigma_pS_tube']
        if s == max(test_sigmas):
            best_results[h] = r['alpha_spread']

    print(f"  Best universality spread at σ_pS_tube = {max(test_sigmas)}:")
    for h, spread in sorted(best_results.items(), key=lambda x: x[1]):
        consistency_str = ""
        marker = "✓" if spread < 1e-6 else ("~" if spread < 1e-3 else "✗")
        print(f"    {marker} {h:<45s}: {spread:.4e}")

    print()
    if min(best_results.values()) < 1e-6:
        print("  → A structural prescription EXISTS that preserves α universality")
        print("    to machine precision at non-trivial σ_pS_tube.")
        print("    Outcome A or D (per Track 9 framing).")
    elif min(best_results.values()) < 1e-3:
        print("  → A close-to-universal prescription was found, but not exact.")
        print("    Either higher-order terms exist, or no clean closed form.")
    else:
        print("  → No tested hypothesis preserves α universality.")
        print("    This supports Outcome C: σ_pS structurally must be zero")
        print("    under any single- or two-parameter compensation.")
        print("    Q135's hub-and-spoke principle is reinforced.")
        print()
        print("    Phase 9 would then need to:")
        print("    - Test more elaborate multi-parameter compensations")
        print("    - Or accept Outcome C and move to propagator-based formalism")
        print("      (R64 pool item m).")


if __name__ == "__main__":
    main()
