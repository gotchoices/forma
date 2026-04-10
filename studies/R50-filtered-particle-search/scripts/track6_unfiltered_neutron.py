"""
R50 Track 6: Unfiltered neutron search — compound-structure approach

Drops the single-torus waveguide cutoff filter and searches ALL
Q = 0, spin-½ six-tuples for neutron candidates.  Tests all three
proton hypotheses side by side: (1,2), (1,3), (3,6).

MOTIVATION:
Tracks 2 and 5 revealed a tension — (1,3) wins on nuclear charge
formulae but has coarse proton-ring mode spacing that prevents a
close neutron match.  (3,6) has finer spacing but fails on nuclear
charges.  This tension arose because Tracks 1–5 imposed the
waveguide cutoff filter (designed on isolated tori).

KEY INSIGHT:
The ghost-elimination mechanism may emerge from the compound
structure (cross-shear coupling between sheets) rather than from
per-sheet waveguide cutoff.  A "ghost" on one sheet could drain
into a dark mode on another sheet via cross-shear coupling.

APPROACH:
  1. Generate ALL Q = 0, spin-½ modes (no waveguide filter)
  2. For each proton hypothesis, derive L_ring_p from
     E(proton_mode) = 938.272 MeV
  3. Sweep σ_ep and find best neutron candidates
  4. Compare filtered vs unfiltered results
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

M_NEUTRON = 939.565  # MeV (PDG 2022)

EPS_E, EPS_NU, EPS_P = 0.65, 5.0, 0.55
S_NU_DEFAULT = 0.022  # R49 Assignment A

PROTON_MODES = [(1, 2), (1, 3), (3, 6)]


def build_corrected_model(n_p, sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0,
                          eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P):
    """
    Build MaD with L_ring derived self-consistently for given proton mode.

    G̃ depends on (ε, s, σ) but not on L.  So:
      1. Build G̃ from geometry + σ
      2. Compute μ_eff for reference modes from G̃⁻¹
      3. Derive L_ring = 2πℏc × μ_eff / M_target

    Returns (model, info_dict) or (None, info_dict) if metric fails.
    """
    s_e = solve_shear_for_alpha(eps_e)
    # NOTE (Q114 §11.5): pass proton mode through; this script tests
    # multiple proton hypotheses, each requires its own shear.
    s_p = solve_shear_for_alpha(eps_p, n_tube=n_p[0], n_ring=n_p[1])
    s_nu = S_NU_DEFAULT

    if s_e is None or s_p is None:
        return None, {'reason': 'no shear solution'}

    L_dummy = _build_circumferences(
        eps_e, s_e, 1.0, eps_nu, s_nu, 1.0, eps_p, s_p, 1.0)
    Gt, Gti = _build_metric(
        L_dummy, s_e, s_nu, s_p,
        sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)

    if Gt is None:
        return None, {'reason': 'not positive definite'}

    n_e_d = np.array([1.0 / eps_e, 2.0, 0, 0, 0, 0])
    mu_eff_e = math.sqrt(float(n_e_d @ Gti @ n_e_d))
    L_ring_e = _TWO_PI_HC * mu_eff_e / M_E_MEV

    n_p_d = np.array([0, 0, 0, 0, float(n_p[0]) / eps_p, float(n_p[1])])
    mu_eff_p = math.sqrt(float(n_p_d @ Gti @ n_p_d))
    L_ring_p = _TWO_PI_HC * mu_eff_p / M_P_MEV

    E0_nu_MeV = math.sqrt(DM2_21 / (4 * s_nu)) * 1e-6
    L_ring_nu = _TWO_PI_HC / E0_nu_MeV

    try:
        model = MaD(
            eps_e=eps_e, eps_nu=eps_nu, eps_p=eps_p,
            s_e=s_e, s_nu=s_nu, s_p=s_p,
            L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
            sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)
        model._n_p = n_p
    except ValueError:
        return None, {'reason': 'model construction failed'}

    info = {
        'mu_eff_e': mu_eff_e, 'mu_eff_p': mu_eff_p,
        'L_ring_e': L_ring_e, 'L_ring_p': L_ring_p,
        'L_ring_nu': L_ring_nu,
        'E0_p': _TWO_PI_HC / L_ring_p,
    }
    return model, info


def generate_candidates(n_ranges, charge_target=0, spin_target=0.5):
    """
    Generate all 6-tuples satisfying charge and spin constraints.
    No waveguide filter — all modes are candidates.
    """
    ranges = [range(lo, hi + 1) for lo, hi in n_ranges]
    out = []
    for n in iproduct(*ranges):
        if all(ni == 0 for ni in n):
            continue
        if MaD.charge(n) != charge_target:
            continue
        if MaD.spin_total(n) != spin_target:
            continue
        out.append(n)
    return out


def batch_energies(candidates_arr, L, Gti):
    """Vectorized energy for many modes."""
    n_over_L = candidates_arr / L
    E2 = _TWO_PI_HC**2 * np.sum((n_over_L @ Gti) * n_over_L, axis=1)
    return np.sqrt(np.maximum(E2, 0))


def classify_propagation(candidates, model):
    """Tag each candidate as propagating or non-propagating."""
    return [model.propagates(n) for n in candidates]


def run_hypothesis(n_p, candidates, cand_arr, sigma_range):
    """
    Full neutron search for one proton hypothesis.

    Returns dict with baseline info, sweep results, and best candidates.
    """
    label = f"({n_p[0]},{n_p[1]})"
    print(f"\n{'='*72}")
    print(f"  Proton hypothesis: {label}")
    print(f"{'='*72}")

    # Baseline (σ = 0)
    m0, info0 = build_corrected_model(n_p)
    if m0 is None:
        print(f"  FAILED: {info0['reason']}")
        return None

    E0_p = info0['E0_p']
    L_ring_p = info0['L_ring_p']
    n_p_full = (0, 0, 0, 0, n_p[0], n_p[1])

    print(f"  L_ring_p = {L_ring_p:.4f} fm")
    print(f"  E₀_p (mode spacing) = {E0_p:.1f} MeV")
    print(f"  E(proton) = {m0.energy(n_p_full):.3f} MeV")

    # Tag propagation status
    prop_flags = classify_propagation(candidates, m0)
    n_prop = sum(prop_flags)
    n_nonprop = len(candidates) - n_prop
    print(f"  Candidates: {len(candidates)} total "
          f"({n_prop} propagating, {n_nonprop} non-propagating)")

    # Baseline energies
    E0 = batch_energies(cand_arr, m0.L, m0.metric_inv)

    # Top candidates at σ = 0
    diffs0 = np.abs(E0 - M_NEUTRON)
    order0 = np.argsort(diffs0)[:15]

    print(f"\n  Top 15 nearest Q = 0, spin-½ modes to neutron at σ = 0:")
    print(f"  {'Mode':>30s}  {'E (MeV)':>10s}  {'Δm':>10s}  "
          f"{'Δm/m':>8s}  {'Prop?':>5s}  {'Sheets':>8s}")
    print(f"  {'─'*30}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'*5}  {'─'*8}")
    for i in order0:
        n = candidates[i]
        sheets = m0.active_sheets(n)
        dm = E0[i] - M_NEUTRON
        pflag = '✓' if prop_flags[i] else '✗'
        print(f"  {str(n):>30s}  {E0[i]:10.3f}  {dm:+10.3f}  "
              f"{abs(dm)/M_NEUTRON*100:7.3f}%  {pflag:>5s}  {sheets:>8s}")

    # σ_ep sweep
    print(f"\n  σ_ep sweep ({len(sigma_range)} points):")
    best_overall = None
    sweep_data = []

    for sigma_val in sigma_range:
        m, info = build_corrected_model(n_p, sigma_ep=sigma_val)
        if m is None:
            sweep_data.append(None)
            continue

        energies = batch_energies(cand_arr, m.L, m.metric_inv)
        diffs = np.abs(energies - M_NEUTRON)
        best_idx = np.argmin(diffs)
        best_E = energies[best_idx]
        best_dm = best_E - M_NEUTRON
        best_n = candidates[best_idx]
        best_prop = m.propagates(best_n)

        entry = {
            'sigma': sigma_val,
            'best_n': best_n,
            'best_E': best_E,
            'best_dm': best_dm,
            'best_prop': best_prop,
            'L_ring_p': info['L_ring_p'],
        }
        sweep_data.append(entry)

        if best_overall is None or abs(best_dm) < abs(best_overall['best_dm']):
            best_overall = entry

    # Print sweep highlights
    valid = [d for d in sweep_data if d is not None]
    step = max(1, len(valid) // 12)
    print(f"  {'σ_ep':>8s}  {'Mode':>30s}  {'E (MeV)':>10s}  "
          f"{'Δm':>10s}  {'Prop?':>5s}")
    print(f"  {'─'*8}  {'─'*30}  {'─'*10}  {'─'*10}  {'─'*5}")
    for d in valid[::step]:
        pflag = '✓' if d['best_prop'] else '✗'
        print(f"  {d['sigma']:+8.3f}  {str(d['best_n']):>30s}  "
              f"{d['best_E']:10.3f}  {d['best_dm']:+10.3f}  {pflag:>5s}")

    if best_overall:
        pflag = '✓' if best_overall['best_prop'] else '✗'
        print(f"\n  ★ Best overall: {best_overall['best_n']}")
        print(f"    E = {best_overall['best_E']:.3f} MeV  "
              f"(Δ = {best_overall['best_dm']:+.3f} MeV, "
              f"{abs(best_overall['best_dm'])/M_NEUTRON*100:.3f}%)")
        print(f"    σ_ep = {best_overall['sigma']:+.3f}")
        print(f"    Propagates (single-torus)? {pflag}")
        print(f"    Sheets: {m0.active_sheets(best_overall['best_n'])}")
        print(f"    Q = {MaD.charge(best_overall['best_n'])}, "
              f"spin = {MaD.spin_total(best_overall['best_n'])}")

    # Also find the best PROPAGATING candidate for comparison
    best_prop_overall = None
    for d in valid:
        if d is not None and d['best_prop']:
            if (best_prop_overall is None or
                    abs(d['best_dm']) < abs(best_prop_overall['best_dm'])):
                best_prop_overall = d

    # Sweep again looking only at propagating modes for fair comparison
    print(f"\n  Best propagating-only candidate (for Track 2 comparison):")
    prop_indices = [i for i, p in enumerate(prop_flags) if p]
    if prop_indices:
        prop_arr = cand_arr[prop_indices]
        best_prop_result = None
        for sigma_val in sigma_range:
            m, info = build_corrected_model(n_p, sigma_ep=sigma_val)
            if m is None:
                continue
            energies = batch_energies(prop_arr, m.L, m.metric_inv)
            diffs = np.abs(energies - M_NEUTRON)
            bi = np.argmin(diffs)
            be = energies[bi]
            bdm = be - M_NEUTRON
            orig_idx = prop_indices[bi]
            bn = candidates[orig_idx]
            if best_prop_result is None or abs(bdm) < abs(best_prop_result[2]):
                best_prop_result = (bn, be, bdm, sigma_val)

        if best_prop_result:
            bn, be, bdm, bsig = best_prop_result
            print(f"    Mode: {bn}")
            print(f"    E = {be:.3f} MeV  (Δ = {bdm:+.3f} MeV, "
                  f"{abs(bdm)/M_NEUTRON*100:.3f}%)")
            print(f"    σ_ep = {bsig:+.3f}")
    else:
        print(f"    (no propagating candidates)")

    return {
        'n_p': n_p,
        'L_ring_p': L_ring_p,
        'E0_p': E0_p,
        'best_overall': best_overall,
        'best_prop_result': best_prop_result if prop_indices else None,
        'sweep_data': sweep_data,
    }


def comparison_table(results):
    """Side-by-side comparison of all proton hypotheses."""
    print(f"\n{'='*72}")
    print("COMPARISON: All proton hypotheses — unfiltered neutron search")
    print(f"{'='*72}")

    print(f"\n  {'':>20s}  ", end='')
    for r in results:
        if r is None:
            continue
        label = f"({r['n_p'][0]},{r['n_p'][1]})"
        print(f"{'':>3s}{label:>12s}  ", end='')
    print()

    print(f"  {'─'*20}  ", end='')
    for r in results:
        if r is None:
            continue
        print(f"{'':>3s}{'─'*12}  ", end='')
    print()

    rows = [
        ('L_ring_p (fm)', lambda r: f"{r['L_ring_p']:.4f}"),
        ('E₀_p (MeV)', lambda r: f"{r['E0_p']:.1f}"),
    ]

    for label, fn in rows:
        print(f"  {label:>20s}  ", end='')
        for r in results:
            if r is None:
                continue
            print(f"{'':>3s}{fn(r):>12s}  ", end='')
        print()

    # Best unfiltered
    print(f"\n  Unfiltered best:")
    print(f"  {'Mode':>20s}  ", end='')
    for r in results:
        if r is None or r['best_overall'] is None:
            print(f"{'':>3s}{'—':>12s}  ", end='')
            continue
        n = r['best_overall']['best_n']
        print(f"{'':>3s}{str(n):>12s}  ", end='')
    print()
    print(f"  {'Δm (MeV)':>20s}  ", end='')
    for r in results:
        if r is None or r['best_overall'] is None:
            print(f"{'':>3s}{'—':>12s}  ", end='')
            continue
        dm = r['best_overall']['best_dm']
        print(f"{'':>3s}{dm:+12.3f}  ", end='')
    print()
    print(f"  {'Δm/m':>20s}  ", end='')
    for r in results:
        if r is None or r['best_overall'] is None:
            print(f"{'':>3s}{'—':>12s}  ", end='')
            continue
        dm = r['best_overall']['best_dm']
        pct = abs(dm) / M_NEUTRON * 100
        print(f"{'':>3s}{pct:11.3f}%  ", end='')
    print()
    print(f"  {'σ_ep':>20s}  ", end='')
    for r in results:
        if r is None or r['best_overall'] is None:
            print(f"{'':>3s}{'—':>12s}  ", end='')
            continue
        sig = r['best_overall']['sigma']
        print(f"{'':>3s}{sig:+12.3f}  ", end='')
    print()
    print(f"  {'Propagates?':>20s}  ", end='')
    for r in results:
        if r is None or r['best_overall'] is None:
            print(f"{'':>3s}{'—':>12s}  ", end='')
            continue
        p = '✓' if r['best_overall']['best_prop'] else '✗'
        print(f"{'':>3s}{p:>12s}  ", end='')
    print()

    # Best filtered (Track 2 comparison)
    print(f"\n  Filtered best (Track 2 comparison):")
    print(f"  {'Mode':>20s}  ", end='')
    for r in results:
        if r is None or r.get('best_prop_result') is None:
            print(f"{'':>3s}{'—':>12s}  ", end='')
            continue
        n = r['best_prop_result'][0]
        print(f"{'':>3s}{str(n):>12s}  ", end='')
    print()
    print(f"  {'Δm (MeV)':>20s}  ", end='')
    for r in results:
        if r is None or r.get('best_prop_result') is None:
            print(f"{'':>3s}{'—':>12s}  ", end='')
            continue
        dm = r['best_prop_result'][2]
        print(f"{'':>3s}{dm:+12.3f}  ", end='')
    print()

    # Does unfiltered find something the filter missed?
    print(f"\n  Filter impact:")
    for r in results:
        if r is None or r['best_overall'] is None:
            continue
        label = f"({r['n_p'][0]},{r['n_p'][1]})"
        bo = r['best_overall']
        if bo['best_prop']:
            print(f"    {label}: Best candidate propagates — "
                  f"filter has no impact")
        else:
            bp = r.get('best_prop_result')
            if bp:
                improvement = abs(bp[2]) - abs(bo['best_dm'])
                print(f"    {label}: ★ Best candidate does NOT propagate — "
                      f"filter hides it!")
                print(f"           Unfiltered: Δ = {bo['best_dm']:+.3f} MeV  "
                      f"vs  Filtered: Δ = {bp[2]:+.3f} MeV  "
                      f"(improvement: {improvement:.1f} MeV)")
            else:
                print(f"    {label}: ★ Best candidate does NOT propagate — "
                      f"filter hides it! (no propagating candidate found)")


def main():
    print("=" * 72)
    print("R50 Track 6: Unfiltered neutron search — compound-structure approach")
    print("=" * 72)
    print()
    print("Methodology: NO waveguide cutoff filter applied.")
    print("All Q = 0, spin = ½ modes are neutron candidates.")
    print("All three proton hypotheses tested side by side.")

    # Generate candidates (no propagation filter)
    n_ranges = [
        (-3, 3),    # n₁ (electron tube)
        (-4, 4),    # n₂ (electron ring)
        (-2, 2),    # n₃ (neutrino tube)
        (-2, 2),    # n₄ (neutrino ring)
        (-6, 6),    # n₅ (proton tube)
        (-10, 10),  # n₆ (proton ring)
    ]

    total_search = 1
    for lo, hi in n_ranges:
        total_search *= (hi - lo + 1)

    print(f"\nCandidate generation:")
    print(f"  Search space: {total_search:,} 6-tuples")

    candidates = generate_candidates(n_ranges, charge_target=0, spin_target=0.5)
    print(f"  Q = 0, spin = ½: {len(candidates):,} candidates (ALL — no filter)")

    cand_arr = np.array(candidates, dtype=float)
    sigma_range = np.linspace(-0.3, 0.3, 61)

    # Run each proton hypothesis
    results = []
    for n_p in PROTON_MODES:
        r = run_hypothesis(n_p, candidates, cand_arr, sigma_range)
        results.append(r)

    # Comparison
    comparison_table(results)

    # Summary
    print(f"\n{'='*72}")
    print("Summary")
    print(f"{'='*72}")

    any_hidden = False
    for r in results:
        if r is None or r['best_overall'] is None:
            continue
        if not r['best_overall']['best_prop']:
            any_hidden = True

    if any_hidden:
        print("\n  ★ FINDING: The waveguide cutoff filter HIDES the best "
              "neutron candidate")
        print("    for at least one proton hypothesis.  This supports the")
        print("    compound-structure filtration hypothesis: the filter")
        print("    mechanism is not per-sheet waveguide cutoff.")
    else:
        print("\n  The best candidates all propagate on isolated tori.")
        print("  The waveguide filter does not affect the neutron search.")

    # Key question: does any hypothesis achieve < 1 MeV gap?
    print(f"\n  Neutron proximity by hypothesis:")
    for r in results:
        if r is None or r['best_overall'] is None:
            continue
        label = f"({r['n_p'][0]},{r['n_p'][1]})"
        dm = abs(r['best_overall']['best_dm'])
        quality = "excellent" if dm < 1 else "good" if dm < 5 else "marginal" if dm < 20 else "poor"
        print(f"    {label}: |Δm| = {dm:.3f} MeV ({quality})")

    print(f"\n{'='*72}")
    print("Track 6 complete.")
    print(f"{'='*72}")


if __name__ == '__main__':
    main()
