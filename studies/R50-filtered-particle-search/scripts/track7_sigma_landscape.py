"""
R50 Track 7: σ_ep landscape — full-spectrum optimization

Sweeps σ_ep across [−0.3, +0.3] for both (1,3) and (3,6) proton
hypotheses, running the full particle target match at each point.
No waveguide filter (Track 6 methodology).

PURPOSE:
Tracks 2–6 chose σ_ep based on the neutron alone.  This track maps
the full landscape — how does the entire particle spectrum respond
to σ_ep?  The result is a fair side-by-side comparison of both
hypotheses at their respective optimal σ_ep, with σ_ep remaining
a free parameter (constrained, not pinned).
"""

import sys
import os
import math
from itertools import product as iproduct

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np

from lib.ma_model_d import (
    MaD, M_E_MEV, M_P_MEV, DM2_21,
    _TWO_PI_HC, _build_circumferences, _build_metric,
    solve_shear_for_alpha,
)

# ── Constants ─────────────────────────────────────────────────────

EPS_E, EPS_NU, EPS_P = 0.65, 5.0, 0.55
S_NU_DEFAULT = 0.022
E_MAX = 2000.0

PROTON_MODES = [(1, 3), (3, 6)]

# Targets: (name, mass_MeV, charge, spin, tau_s, tier)
TARGETS = [
    ('e⁻',       0.511,     -1, 0.5,  float('inf'), 1),
    ('p',        938.272,    +1, 0.5,  float('inf'), 1),
    ('n',        939.565,     0, 0.5,  879.4,        2),
    ('μ⁻',      105.658,    -1, 0.5,  2.197e-6,     2),
    ('π⁰',     134.977,     0, 0.0,  8.43e-17,     2),
    ('K⁰',      497.611,     0, 0.0,  8.954e-11,    2),
    ('η',       547.862,     0, 0.0,  5.02e-19,     2),
    ('η′',      957.78,      0, 0.0,  3.32e-21,     2),
    ('φ',      1019.461,     0, 1.0,  1.55e-22,     3),
    ('Λ',      1115.683,     0, 0.5,  2.632e-10,    2),
    ('Σ⁺',    1189.37,     +1, 0.5,  8.018e-11,    3),
    ('Ξ⁰',    1314.86,      0, 0.5,  2.90e-10,     3),
    ('Ω⁻',    1672.45,     -1, 1.5,  8.21e-11,     3),
    ('Δ⁰',     1232.0,      0, 1.5,  5.63e-24,     3),
    ('ρ⁰',      775.26,     0, 1.0,  4.51e-24,     3),
    ('τ⁻',    1776.86,     -1, 0.5,  2.903e-13,    3),
]


def is_qs_possible(Q, spin):
    """Check if (Q, spin) is topologically realizable."""
    k = int(2 * spin)
    if k == 0 or k == 3:
        return Q % 2 == 0
    return True


# Precompute which targets have possible quantum numbers
POSSIBLE_TARGETS = [t for t in TARGETS if is_qs_possible(t[2], t[3])]
IMPOSSIBLE_TARGETS = [t for t in TARGETS if not is_qs_possible(t[2], t[3])]


def build_corrected_model(n_p, sigma_ep=0.0):
    """Build MaD with L_ring derived self-consistently."""
    s_e = solve_shear_for_alpha(EPS_E)
    # NOTE (Q114 §11.5): pass proton mode through; this script tests
    # both (1,3) and (3,6) hypotheses, each requires its own shear.
    s_p = solve_shear_for_alpha(EPS_P, n_tube=n_p[0], n_ring=n_p[1])
    s_nu = S_NU_DEFAULT

    if s_e is None or s_p is None:
        return None, {}

    L_dummy = _build_circumferences(
        EPS_E, s_e, 1.0, EPS_NU, s_nu, 1.0, EPS_P, s_p, 1.0)
    Gt, Gti = _build_metric(
        L_dummy, s_e, s_nu, s_p, sigma_ep=sigma_ep)
    if Gt is None:
        return None, {}

    n_e_d = np.array([1.0 / EPS_E, 2.0, 0, 0, 0, 0])
    mu_eff_e = math.sqrt(float(n_e_d @ Gti @ n_e_d))
    L_ring_e = _TWO_PI_HC * mu_eff_e / M_E_MEV

    n_p_d = np.array([0, 0, 0, 0, float(n_p[0]) / EPS_P, float(n_p[1])])
    mu_eff_p = math.sqrt(float(n_p_d @ Gti @ n_p_d))
    L_ring_p = _TWO_PI_HC * mu_eff_p / M_P_MEV

    E0_nu_MeV = math.sqrt(DM2_21 / (4 * s_nu)) * 1e-6
    L_ring_nu = _TWO_PI_HC / E0_nu_MeV

    try:
        model = MaD(
            eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
            s_e=s_e, s_nu=s_nu, s_p=s_p,
            L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
            sigma_ep=sigma_ep)
        model._n_p = n_p
    except ValueError:
        return None, {}

    return model, {'L_ring_p': L_ring_p}


def batch_energies(candidates_arr, L, Gti):
    """Vectorized energy for many modes."""
    n_over_L = candidates_arr / L
    E2 = _TWO_PI_HC**2 * np.sum((n_over_L @ Gti) * n_over_L, axis=1)
    return np.sqrt(np.maximum(E2, 0))


def generate_candidates(n_ranges, charge_target=None, spin_target=None):
    """Generate 6-tuples (no waveguide filter)."""
    ranges = [range(lo, hi + 1) for lo, hi in n_ranges]
    out = []
    for n in iproduct(*ranges):
        if all(ni == 0 for ni in n):
            continue
        if charge_target is not None and MaD.charge(n) != charge_target:
            continue
        if spin_target is not None and MaD.spin_total(n) != spin_target:
            continue
        out.append(n)
    return out


def match_targets_at_sigma(n_p, sigma_ep, cand_pools):
    """
    Match all possible targets at a given σ_ep.

    Returns dict: target_name → {best_n, best_E, dm, frac, propagates}
    or None if model fails.
    """
    model, info = build_corrected_model(n_p, sigma_ep=sigma_ep)
    if model is None:
        return None

    results = {}
    for target in POSSIBLE_TARGETS:
        name, mass, Q, spin, tau, tier = target
        key = (Q, spin)
        if key not in cand_pools:
            continue

        cands, arr = cand_pools[key]
        if len(cands) == 0:
            continue

        energies = batch_energies(arr, model.L, model.metric_inv)
        mask = energies <= E_MAX
        if not mask.any():
            continue

        diffs = np.abs(energies - mass)
        diffs[~mask] = 1e30
        best_idx = np.argmin(diffs)
        best_E = float(energies[best_idx])
        dm = best_E - mass
        frac = abs(dm) / mass

        results[name] = {
            'best_n': cands[best_idx],
            'best_E': best_E,
            'dm': dm,
            'frac': frac,
            'propagates': model.propagates(cands[best_idx]),
        }

    return results


def landscape_metrics(results):
    """Compute summary metrics from a match result dict."""
    if results is None:
        return None

    fracs = [r['frac'] for r in results.values()]
    if not fracs:
        return None

    # Exclude stable references (e⁻, p) from the metric
    unstable_fracs = [r['frac'] for name, r in results.items()
                      if name not in ('e⁻', 'p', 'ν₁')]

    n_good = sum(1 for f in unstable_fracs if f < 0.02)
    n_fair = sum(1 for f in unstable_fracs if 0.02 <= f < 0.10)
    n_poor = sum(1 for f in unstable_fracs if f >= 0.10)

    # Median absolute fractional residual (robust to outliers)
    median_frac = float(np.median(unstable_fracs)) if unstable_fracs else 1.0

    # Mean excluding the two worst (muon and pion, typically)
    sorted_fracs = sorted(unstable_fracs)
    trimmed = sorted_fracs[:-2] if len(sorted_fracs) > 4 else sorted_fracs
    trimmed_mean = float(np.mean(trimmed)) if trimmed else 1.0

    neutron_frac = results.get('n', {}).get('frac', 1.0)

    return {
        'n_good': n_good,
        'n_fair': n_fair,
        'n_poor': n_poor,
        'median_frac': median_frac,
        'trimmed_mean': trimmed_mean,
        'neutron_frac': neutron_frac,
    }


def run_hypothesis(n_p, sigma_range, cand_pools):
    """Sweep σ_ep for one proton hypothesis, return landscape."""
    label = f"({n_p[0]},{n_p[1]})"
    print(f"\n{'='*72}")
    print(f"  Proton hypothesis: {label}")
    print(f"{'='*72}")

    landscape = []

    for sigma_val in sigma_range:
        results = match_targets_at_sigma(n_p, sigma_val, cand_pools)
        metrics = landscape_metrics(results)
        if metrics is None:
            landscape.append(None)
            continue
        landscape.append({
            'sigma': sigma_val,
            'results': results,
            'metrics': metrics,
        })

    # Print landscape table
    valid = [l for l in landscape if l is not None]
    print(f"\n  σ_ep landscape ({len(valid)} valid of {len(sigma_range)} points):\n")
    print(f"  {'σ_ep':>7s}  {'Good':>4s}  {'Fair':>4s}  {'Poor':>4s}  "
          f"{'Median':>8s}  {'Trim mean':>9s}  {'n gap':>8s}")
    print(f"  {'─'*7}  {'─'*4}  {'─'*4}  {'─'*4}  "
          f"{'─'*8}  {'─'*9}  {'─'*8}")

    for l in valid:
        m = l['metrics']
        print(f"  {l['sigma']:+7.3f}  {m['n_good']:4d}  {m['n_fair']:4d}  "
              f"{m['n_poor']:4d}  {m['median_frac']*100:7.2f}%  "
              f"{m['trimmed_mean']*100:8.2f}%  {m['neutron_frac']*100:7.3f}%")

    # Find optimal by different criteria
    by_good = max(valid, key=lambda l: (l['metrics']['n_good'],
                                        -l['metrics']['trimmed_mean']))
    by_median = min(valid, key=lambda l: l['metrics']['median_frac'])
    by_trimmed = min(valid, key=lambda l: l['metrics']['trimmed_mean'])
    by_neutron = min(valid, key=lambda l: l['metrics']['neutron_frac'])

    print(f"\n  Optimal σ_ep by criterion:")
    print(f"    Max good matches:   σ_ep = {by_good['sigma']:+.3f}  "
          f"({by_good['metrics']['n_good']} good)")
    print(f"    Min median |Δm/m|:  σ_ep = {by_median['sigma']:+.3f}  "
          f"(median {by_median['metrics']['median_frac']*100:.2f}%)")
    print(f"    Min trimmed mean:   σ_ep = {by_trimmed['sigma']:+.3f}  "
          f"(mean {by_trimmed['metrics']['trimmed_mean']*100:.2f}%)")
    print(f"    Min neutron gap:    σ_ep = {by_neutron['sigma']:+.3f}  "
          f"(n gap {by_neutron['metrics']['neutron_frac']*100:.3f}%)")

    # Detail at best overall (by trimmed mean)
    best = by_trimmed
    print(f"\n  Detail at best σ_ep = {best['sigma']:+.3f} (trimmed mean):")
    print(f"  {'Particle':>8s}  {'m (MeV)':>10s}  {'Best E':>10s}  "
          f"{'Δm':>10s}  {'|Δm/m|':>8s}  {'P':>1s}  {'Grade':>6s}")
    print(f"  {'─'*8}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'}  {'─'*6}")

    for target in POSSIBLE_TARGETS:
        name = target[0]
        mass = target[1]
        if name not in best['results']:
            continue
        r = best['results'][name]
        grade = ('ref' if r['frac'] < 0.001
                 else 'good' if r['frac'] < 0.02
                 else 'fair' if r['frac'] < 0.10
                 else 'poor')
        pflag = '✓' if r['propagates'] else '✗'
        print(f"  {name:>8s}  {mass:10.3f}  {r['best_E']:10.3f}  "
              f"{r['dm']:+10.3f}  {r['frac']*100:7.3f}%  {pflag}  {grade:>6s}")

    return {
        'n_p': n_p,
        'landscape': landscape,
        'by_good': by_good,
        'by_median': by_median,
        'by_trimmed': by_trimmed,
        'by_neutron': by_neutron,
    }


def compare_hypotheses(results_list):
    """Side-by-side comparison at each hypothesis's best σ_ep."""
    print(f"\n{'='*72}")
    print("COMPARISON at each hypothesis's best σ_ep (trimmed mean)")
    print(f"{'='*72}\n")

    headers = []
    bests = []
    for r in results_list:
        label = f"({r['n_p'][0]},{r['n_p'][1]})"
        best = r['by_trimmed']
        headers.append(f"{label} σ={best['sigma']:+.2f}")
        bests.append(best)

    print(f"  {'Particle':>8s}  ", end='')
    for h in headers:
        print(f"{'|Δm/m|':>10s}  ", end='')
    print("  Better")

    print(f"  {'─'*8}  ", end='')
    for _ in headers:
        print(f"{'─'*10}  ", end='')
    print(f"  {'─'*8}")

    # Header row with σ values
    print(f"  {'':>8s}  ", end='')
    for h in headers:
        print(f"{h:>10s}  ", end='')
    print()

    wins = [0] * len(results_list)

    for target in POSSIBLE_TARGETS:
        name = target[0]
        if name in ('e⁻', 'p'):
            continue

        fracs = []
        for best in bests:
            if name in best['results']:
                fracs.append(best['results'][name]['frac'])
            else:
                fracs.append(1.0)

        print(f"  {name:>8s}  ", end='')
        for f in fracs:
            print(f"{f*100:9.3f}%  ", end='')

        if len(fracs) >= 2:
            if fracs[0] < fracs[1] * 0.9:
                print(f"  ← {headers[0][:5]}")
                wins[0] += 1
            elif fracs[1] < fracs[0] * 0.9:
                print(f"  → {headers[1][:5]}")
                wins[1] += 1
            else:
                print(f"  ≈ tie")
        else:
            print()

    print(f"\n  Wins: ", end='')
    for i, h in enumerate(headers):
        print(f"{h}: {wins[i]}  ", end='')
    print()

    # Summary metrics
    print(f"\n  Summary metrics at optimal σ_ep:")
    print(f"  {'Metric':>20s}  ", end='')
    for h in headers:
        print(f"{h:>12s}  ", end='')
    print()
    print(f"  {'─'*20}  ", end='')
    for _ in headers:
        print(f"{'─'*12}  ", end='')
    print()

    metrics = [
        ('Good (< 2%)', lambda m: str(m['n_good'])),
        ('Fair (2-10%)', lambda m: str(m['n_fair'])),
        ('Poor (> 10%)', lambda m: str(m['n_poor'])),
        ('Median |Δm/m|', lambda m: f"{m['median_frac']*100:.2f}%"),
        ('Trimmed mean', lambda m: f"{m['trimmed_mean']*100:.2f}%"),
        ('Neutron gap', lambda m: f"{m['neutron_frac']*100:.3f}%"),
    ]

    for label, fn in metrics:
        print(f"  {label:>20s}  ", end='')
        for best in bests:
            print(f"{fn(best['metrics']):>12s}  ", end='')
        print()


def main():
    print("=" * 72)
    print("R50 Track 7: σ_ep landscape — full-spectrum optimization")
    print("=" * 72)
    print()
    print("Both proton hypotheses, unfiltered, σ_ep swept.")
    print("σ_ep remains a free parameter — reporting the landscape.")

    # Generate candidate pools (shared across σ values)
    N_RANGES = [
        (-3, 3),     # n₁
        (-6, 6),     # n₂
        (-3, 3),     # n₃
        (-3, 3),     # n₄
        (-6, 6),     # n₅
        (-16, 16),   # n₆
    ]

    print(f"\nGenerating candidate pools (no waveguide filter)...")
    qs_needed = set()
    for t in POSSIBLE_TARGETS:
        qs_needed.add((t[2], t[3]))

    cand_pools = {}
    for Q, J in sorted(qs_needed):
        cands = generate_candidates(N_RANGES, charge_target=Q, spin_target=J)
        arr = np.array(cands, dtype=float) if cands else np.zeros((0, 6))
        cand_pools[(Q, J)] = (cands, arr)
        print(f"  (Q={Q:+d}, J={J:.1f}): {len(cands):>6d} candidates")

    sigma_range = np.linspace(-0.3, 0.3, 31)
    print(f"\nσ_ep sweep: {len(sigma_range)} points in [{sigma_range[0]:.2f}, {sigma_range[-1]:.2f}]")

    print(f"\nImpossible targets (skipped):")
    for t in IMPOSSIBLE_TARGETS:
        print(f"  {t[0]}: Q={t[2]:+d}, J={t[3]} — topologically forbidden")

    # Run each hypothesis
    all_results = []
    for n_p in PROTON_MODES:
        r = run_hypothesis(n_p, sigma_range, cand_pools)
        all_results.append(r)

    # Comparison
    compare_hypotheses(all_results)

    # Sensitivity analysis: how much does σ_ep matter?
    print(f"\n{'='*72}")
    print("σ_ep sensitivity: how much does the optimum matter?")
    print(f"{'='*72}")

    for r in all_results:
        label = f"({r['n_p'][0]},{r['n_p'][1]})"
        valid = [l for l in r['landscape'] if l is not None]
        trimmed_vals = [l['metrics']['trimmed_mean'] for l in valid]
        sigmas = [l['sigma'] for l in valid]
        best_tm = min(trimmed_vals)
        best_sig = sigmas[trimmed_vals.index(best_tm)]

        # Width: range of σ where trimmed mean is within 1.5× of best
        threshold = best_tm * 1.5
        in_range = [s for s, tm in zip(sigmas, trimmed_vals) if tm <= threshold]
        if in_range:
            width = max(in_range) - min(in_range)
            print(f"\n  {label}:")
            print(f"    Best σ_ep = {best_sig:+.3f}  "
                  f"(trimmed mean = {best_tm*100:.2f}%)")
            print(f"    σ_ep range within 1.5× of best: "
                  f"[{min(in_range):+.3f}, {max(in_range):+.3f}]  "
                  f"(width = {width:.3f})")
            print(f"    Trimmed mean range: "
                  f"{min(trimmed_vals)*100:.2f}% – {max(trimmed_vals)*100:.2f}%")

    print(f"\n{'='*72}")
    print("Track 7 complete.")
    print(f"{'='*72}")


if __name__ == '__main__':
    main()
