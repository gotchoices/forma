"""
R64 Track 9 Phase 9d — Multi-parameter signature-extension search.

Phase 9c found H2 prescription (σ_aS = -1.819·σ_pS_tube) preserves α
universality, but the signature band stays at ±0.07 — the same as
σ_pS_tube alone.  σ_eff at boundary ≈ 0.54, ~200× too weak for Phase
7c-class strong force.

Phase 9d tests whether *richer* compensation structures can extend the
signature band beyond ±0.07, allowing larger σ_pS_tube and thus larger
σ_eff.  Hypothesis: σ_pS_tube destabilizes a specific spatial
eigenvalue; additional companion entries (beyond just σ_aS) might
stabilize that eigenvalue and let σ_pS_tube grow further.

Hypotheses tested:

  H6 (3-param)  σ_pS_ring + σ_aS jointly compensate σ_pS_tube
  H7 (4-param)  H6 + σ_at modification
  H8 (5-param)  H7 + σ_eS_tube (e-sheet symmetric companion)
  H9 (6-param)  H8 + σ_νS_tube (full 3-sheet symmetric)
  H10 (full)    All sheet-S entries (tube + ring) + σ_aS + σ_at

For each: scan σ_pS_tube upward, optimize compensation params at each
step, find the maximum σ_pS_tube where signature stays Lorentzian AND
α universality is preserved (spread < 1e-9).  Compare σ_eff at the
boundary.

Outputs:
  outputs/track9_phase9d_extension.csv
  outputs/track9_phase9d_extension.png
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


def build_aug_with_block(p, **entries):
    """Augment R60 metric with arbitrary sheet-S, aleph-S, and σ_at modifications.

    Parameters (all default 0 except σ_at, which has a baseline):
      sigma_pS_tube, sigma_pS_ring,
      sigma_eS_tube, sigma_eS_ring,
      sigma_νS_tube, sigma_νS_ring,
      sigma_aS,
      sigma_at_offset (added to baseline σ_at)
    """
    sigma_at_offset = entries.pop('sigma_at_offset', 0.0)
    p_modified = p.copy_with(sigma_at=p.sigma_at + sigma_at_offset)
    G = build_aug_metric(p_modified).copy()

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


def alpha_spread(G):
    values = []
    for label, tup in TEST_MODES:
        n11 = mode_6_to_11(tup)
        alpha = alpha_coulomb(G, n11)
        sq = expected_alpha_sum_squared(tup)
        if sq > 0:
            values.append(alpha / (ALPHA * sq))
    if not values:
        return float('inf')
    return max(values) - min(values)


def schur_effective_sigma_pS(G):
    G_inv = np.linalg.inv(G)
    g_pp = G[I_P_TUBE, I_P_TUBE]
    g_SS = G[I_SX, I_SX]
    return -G_inv[I_P_TUBE, I_SX] * g_pp * g_SS


# ─── Hypothesis cost functions ──────────────────────────────────────

def cost_factory(hypothesis_name):
    """Return cost function and param spec for a given hypothesis."""
    if hypothesis_name == "H6":
        # σ_pS_tube + a·σ_pS_ring + b·σ_aS
        def cost(coeffs, sigma_pS_tube, p):
            a, b = coeffs
            G = build_aug_with_block(
                p,
                sigma_pS_tube=sigma_pS_tube,
                sigma_pS_ring=a * sigma_pS_tube,
                sigma_aS=b * sigma_pS_tube,
            )
            if num_negative_eigs(G) != 1:
                return 1.0 + abs(sigma_pS_tube)
            return alpha_spread(G)

        def metric(coeffs, sigma_pS_tube, p):
            a, b = coeffs
            return build_aug_with_block(
                p,
                sigma_pS_tube=sigma_pS_tube,
                sigma_pS_ring=a * sigma_pS_tube,
                sigma_aS=b * sigma_pS_tube,
            )
        return cost, metric, ['a', 'b'], np.array([1.535, -1.819])

    if hypothesis_name == "H7":
        # H6 + c·σ_at_offset
        def cost(coeffs, sigma_pS_tube, p):
            a, b, c = coeffs
            G = build_aug_with_block(
                p,
                sigma_pS_tube=sigma_pS_tube,
                sigma_pS_ring=a * sigma_pS_tube,
                sigma_aS=b * sigma_pS_tube,
                sigma_at_offset=c * sigma_pS_tube,
            )
            if num_negative_eigs(G) != 1:
                return 1.0 + abs(sigma_pS_tube)
            return alpha_spread(G)

        def metric(coeffs, sigma_pS_tube, p):
            a, b, c = coeffs
            return build_aug_with_block(
                p,
                sigma_pS_tube=sigma_pS_tube,
                sigma_pS_ring=a * sigma_pS_tube,
                sigma_aS=b * sigma_pS_tube,
                sigma_at_offset=c * sigma_pS_tube,
            )
        return cost, metric, ['a', 'b', 'c'], np.array([1.535, -1.819, 0.0])

    if hypothesis_name == "H8":
        # H7 + d·σ_eS_tube
        def cost(coeffs, sigma_pS_tube, p):
            a, b, c, d = coeffs
            G = build_aug_with_block(
                p,
                sigma_pS_tube=sigma_pS_tube,
                sigma_pS_ring=a * sigma_pS_tube,
                sigma_aS=b * sigma_pS_tube,
                sigma_at_offset=c * sigma_pS_tube,
                sigma_eS_tube=d * sigma_pS_tube,
            )
            if num_negative_eigs(G) != 1:
                return 1.0 + abs(sigma_pS_tube)
            return alpha_spread(G)

        def metric(coeffs, sigma_pS_tube, p):
            a, b, c, d = coeffs
            return build_aug_with_block(
                p,
                sigma_pS_tube=sigma_pS_tube,
                sigma_pS_ring=a * sigma_pS_tube,
                sigma_aS=b * sigma_pS_tube,
                sigma_at_offset=c * sigma_pS_tube,
                sigma_eS_tube=d * sigma_pS_tube,
            )
        return cost, metric, ['a', 'b', 'c', 'd'], np.array([1.535, -1.819, 0.0, 1.0])

    if hypothesis_name == "H9":
        # H8 + e·σ_νS_tube
        def cost(coeffs, sigma_pS_tube, p):
            a, b, c, d, e = coeffs
            G = build_aug_with_block(
                p,
                sigma_pS_tube=sigma_pS_tube,
                sigma_pS_ring=a * sigma_pS_tube,
                sigma_aS=b * sigma_pS_tube,
                sigma_at_offset=c * sigma_pS_tube,
                sigma_eS_tube=d * sigma_pS_tube,
                sigma_νS_tube=e * sigma_pS_tube,
            )
            if num_negative_eigs(G) != 1:
                return 1.0 + abs(sigma_pS_tube)
            return alpha_spread(G)

        def metric(coeffs, sigma_pS_tube, p):
            a, b, c, d, e = coeffs
            return build_aug_with_block(
                p,
                sigma_pS_tube=sigma_pS_tube,
                sigma_pS_ring=a * sigma_pS_tube,
                sigma_aS=b * sigma_pS_tube,
                sigma_at_offset=c * sigma_pS_tube,
                sigma_eS_tube=d * sigma_pS_tube,
                sigma_νS_tube=e * sigma_pS_tube,
            )
        return cost, metric, ['a', 'b', 'c', 'd', 'e'], \
               np.array([1.535, -1.819, 0.0, 1.207, -0.207])

    if hypothesis_name == "H10":
        # Full sheet-S block + aleph: 6 free params
        # σ_pS_ring(a), σ_aS(b), σ_at_offset(c),
        # σ_eS_tube(d), σ_νS_tube(e), σ_eS_ring(f)
        def cost(coeffs, sigma_pS_tube, p):
            a, b, c, d, e, f = coeffs
            G = build_aug_with_block(
                p,
                sigma_pS_tube=sigma_pS_tube,
                sigma_pS_ring=a * sigma_pS_tube,
                sigma_aS=b * sigma_pS_tube,
                sigma_at_offset=c * sigma_pS_tube,
                sigma_eS_tube=d * sigma_pS_tube,
                sigma_νS_tube=e * sigma_pS_tube,
                sigma_eS_ring=f * sigma_pS_tube,
            )
            if num_negative_eigs(G) != 1:
                return 1.0 + abs(sigma_pS_tube)
            return alpha_spread(G)

        def metric(coeffs, sigma_pS_tube, p):
            a, b, c, d, e, f = coeffs
            return build_aug_with_block(
                p,
                sigma_pS_tube=sigma_pS_tube,
                sigma_pS_ring=a * sigma_pS_tube,
                sigma_aS=b * sigma_pS_tube,
                sigma_at_offset=c * sigma_pS_tube,
                sigma_eS_tube=d * sigma_pS_tube,
                sigma_νS_tube=e * sigma_pS_tube,
                sigma_eS_ring=f * sigma_pS_tube,
            )
        return cost, metric, ['a', 'b', 'c', 'd', 'e', 'f'], \
               np.array([1.535, -1.819, 0.0, 1.207, -0.207, 0.0])

    raise ValueError(f"Unknown hypothesis: {hypothesis_name}")


# ─── Find max σ_pS_tube under each hypothesis ──────────────────────

def find_max_sigma(p, hypothesis_name,
                   sigma_test_range=np.linspace(0.001, 5.0, 80),
                   alpha_threshold=1e-7):
    """Scan σ_pS_tube upward, optimize compensation, find max where both
    signature is OK and α universality is preserved."""
    cost_fn, metric_fn, param_names, x0 = cost_factory(hypothesis_name)

    last_good = None
    for sigma in sigma_test_range:
        # Optimize at this σ_pS_tube
        result = minimize(
            cost_fn, x0,
            args=(sigma, p),
            method='Nelder-Mead',
            options={'xatol': 1e-10, 'fatol': 1e-13, 'maxiter': 10000},
        )
        # Check whether result is OK
        if result.fun < alpha_threshold:
            G = metric_fn(result.x, sigma, p)
            if num_negative_eigs(G) == 1:
                last_good = (sigma, result.x.copy(), result.fun, G)
                # Continue with current optimum as warm start
                x0 = result.x.copy()
                continue
        break

    return last_good, param_names


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 9 Phase 9d — Multi-parameter signature-extension search")
    print("=" * 100)
    print()

    p = track9_params()

    print("Goal: extend signature-OK σ_pS_tube band beyond ±0.07 (Phase 9c) by")
    print("adding richer compensation structures.  Boost σ_eff at the boundary.")
    print()
    print(f"Reference points:")
    print(f"  H2 (Phase 9b): max σ_pS ≈ ±0.07, σ_eff at boundary ≈ ±0.54")
    print(f"  Phase 7c target: σ_t ≈ ±116 for strong-force trough")
    print()

    hypotheses = ["H6", "H7", "H8", "H9", "H10"]
    results = []

    for hyp in hypotheses:
        print(f"=" * 80)
        print(f"  {hyp}")
        print(f"=" * 80)
        cost_fn, metric_fn, param_names, x0 = cost_factory(hyp)
        n_params = len(param_names)
        print(f"  Parameters ({n_params}): {param_names}")
        print(f"  Initial guess: {x0}")
        print()

        # Scan upward
        last_good_pos, _ = find_max_sigma(
            p, hyp,
            sigma_test_range=np.linspace(0.001, 5.0, 100),
        )
        # Scan downward
        cost_fn2, metric_fn2, _, x0_2 = cost_factory(hyp)
        last_good_neg, _ = find_max_sigma(
            p, hyp,
            sigma_test_range=np.linspace(-0.001, -5.0, 100),
        )

        for direction, last_good in [("positive", last_good_pos),
                                       ("negative", last_good_neg)]:
            if last_good is None:
                print(f"  No σ_pS in {direction} direction passes α-universality.")
                continue
            sigma, coeffs, spread, G = last_good
            sigma_eff = schur_effective_sigma_pS(G)
            print(f"  Max σ_pS_tube ({direction}): {sigma:+.6f}")
            print(f"    Optimal coeffs: " +
                  ", ".join(f"{n}={v:+.4f}" for n, v in zip(param_names, coeffs)))
            print(f"    α-spread:       {spread:.4e}")
            print(f"    σ_eff (Schur):  {sigma_eff:+.6f}")
            print(f"    σ_eff/σ_pS:     {sigma_eff/sigma:+.2f}")
            results.append({
                'hypothesis': hyp,
                'n_params': n_params,
                'direction': direction,
                'max_sigma_pS_tube': sigma,
                'sigma_eff_at_max': sigma_eff,
                'amplification_factor': sigma_eff / sigma,
                'alpha_spread_at_max': spread,
                **{f'param_{n}': float(v) for n, v in zip(param_names, coeffs)},
            })
        print()

    # ─── Summary table ───
    print("=" * 100)
    print("SUMMARY")
    print("=" * 100)
    print()
    print(f"  {'Hyp':<5s}  {'n_param':>7s}  {'max σ_pS':>10s}  "
          f"{'σ_eff':>10s}  {'amp':>6s}  {'α-spread':>12s}")
    print("  " + "─" * 70)
    for r in results:
        print(f"  {r['hypothesis']:<5s}  {r['n_params']:>7d}  "
              f"{r['max_sigma_pS_tube']:>+10.4f}  {r['sigma_eff_at_max']:>+10.4f}  "
              f"{r['amplification_factor']:>+6.2f}  {r['alpha_spread_at_max']:>12.2e}")
    print()
    print(f"  Phase 7c target σ_eff = -116 (or +116, depending on sign).")
    print(f"  Best result: ", end="")
    best = max(results, key=lambda x: abs(x['sigma_eff_at_max']))
    print(f"{best['hypothesis']} with σ_eff = {best['sigma_eff_at_max']:+.4f} "
          f"({100*abs(best['sigma_eff_at_max'])/116:.2f}% of Phase 7c target)")
    print()

    # ─── CSV ───
    csv_path = out_dir / "track9_phase9d_extension.csv"
    if results:
        all_keys = sorted(set().union(*(r.keys() for r in results)))
        with open(csv_path, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=all_keys)
            w.writeheader()
            for r in results:
                w.writerow(r)
        print(f"  CSV: {csv_path}")

    # ─── Plot ───
    fig, ax = plt.subplots(figsize=(10, 6))
    pos = [r for r in results if r['direction'] == 'positive']
    neg = [r for r in results if r['direction'] == 'negative']
    if pos:
        names = [r['hypothesis'] for r in pos]
        sigmas = [r['max_sigma_pS_tube'] for r in pos]
        sigma_effs = [r['sigma_eff_at_max'] for r in pos]
        x = np.arange(len(names))
        ax.bar(x - 0.2, sigmas, 0.4, label='max σ_pS_tube (positive)')
        ax.bar(x + 0.2, sigma_effs, 0.4, label='σ_eff at max')
        ax.set_xticks(x)
        ax.set_xticklabels(names)
        ax.legend()
        ax.set_ylabel('value')
        ax.set_title('Phase 9d: signature band and σ_eff under richer compensation')
        ax.axhline(0.54, color='black', linestyle=':', alpha=0.5,
                   label='H2 baseline σ_eff = 0.54')
        ax.grid(alpha=0.3)
    fig_path = out_dir / "track9_phase9d_extension.png"
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {fig_path}")

    # ─── Verdict ───
    print()
    print("=" * 100)
    print("VERDICT — Phase 9d signature-extension search")
    print("=" * 100)
    print()
    max_sigma_eff_abs = max(abs(r['sigma_eff_at_max']) for r in results)
    if max_sigma_eff_abs > 50:
        print(f"  → Phase 9d EXTENDED the signature band substantially.")
        print(f"    Best σ_eff = {max_sigma_eff_abs:.2f} reaches a meaningful")
        print(f"    fraction of Phase 7c's 116 strong-force scale.")
        print(f"    Outcome A: strong force may yet live in the metric.")
    elif max_sigma_eff_abs > 5:
        print(f"  → Phase 9d extended the band moderately.")
        print(f"    Best σ_eff = {max_sigma_eff_abs:.2f} is bigger than H2's 0.54")
        print(f"    but still ~10-100× short of Phase 7c.")
        print(f"    Richer compensation helps quantitatively but not enough.")
    else:
        print(f"  → Phase 9d did not extend the band significantly.")
        print(f"    Max |σ_eff| = {max_sigma_eff_abs:.2f}, similar to H2's 0.54.")
        print(f"    The signature constraint is fundamental — no amount of")
        print(f"    compensation richness gets σ_eff close to Phase 7c.")
        print(f"    Strong force structurally cannot live in the metric;")
        print(f"    Outcome B+C confirmed; propagator route required.")


if __name__ == "__main__":
    main()
