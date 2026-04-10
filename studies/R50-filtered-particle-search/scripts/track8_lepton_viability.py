"""
R50 Track 8: Lepton viability search

Asks the *minimum* question for each particle in the inventory:

  Does the linear ℤ⁶ spectrum admit ANY 6-tuple with the right
  charge and spin within a stated tolerance of the observed mass?

This is "viability" — not "best identification".  A 5% miss is a
viable candidate.  A 30% miss is not.  We do NOT score lifetime
correlation here (Track 4 already does that and mixing the goals
would muddy this track).

The motivation is the muon mass desert: earlier sweeps reported
zero Q = -1, spin-½ modes between 5 and 200 MeV at default σ.
This track sweeps wider winding ranges, all four sign branches of
the within-plane shears, AND a σ_eν grid (the cross-shear most
naturally interpreted as electron+ν compound coupling), and asks
whether ANY combination produces a viable muon candidate.

If yes → the geometry hosts the muon, no compound engine needed yet.
If no  → we have a structural result that motivates building the
         compound back-reaction engine in a future study.

The same machinery is run against the rest of the inventory so we
get a complete viability table at the end.
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
    solve_shear_for_alpha_signed,
)


# ════════════════════════════════════════════════════════════════════
#  Inventory: standard-model particles to check for viability
# ════════════════════════════════════════════════════════════════════
#
#  Each entry: (name, mass_MeV, charge, spin_total)
#  We include only particles whose Q and topological spin are
#  representable as a 6-tuple in the current charge/spin formalism.
#
#  Spin convention: spin_total() = 0.5 means odd number of odd
#  tube windings (one of n₁, n₃, n₅).  Spin 0 = zero or two.
#  Spin 1 and 3/2 require special handling (no clean topological
#  invariant); we record those but don't filter on them — instead
#  we look for any candidate with at least the right charge.
# ════════════════════════════════════════════════════════════════════

INVENTORY = [
    # Tier 1: stable references (sanity checks — should be exact)
    ('electron',   0.51099895,    -1, 0.5),
    ('proton',     938.27208,     +1, 0.5),

    # Tier 2: long-lived
    ('muon',       105.65837,     -1, 0.5),
    ('neutron',    939.56542,      0, 0.5),
    ('pi+/-',      139.57039,     +1, 0.0),
    ('pi0',        134.9768,       0, 0.0),
    ('K+/-',       493.677,       +1, 0.0),
    ('K0',         497.611,        0, 0.0),
    ('Lambda',     1115.683,       0, 0.5),

    # Tier 3: shorter-lived
    ('eta',        547.862,        0, 0.0),
    ('eta-prime',  957.78,         0, 0.0),
    ('Sigma+',     1189.37,       +1, 0.5),
    ('Sigma0',     1192.642,       0, 0.5),
    ('Sigma-',     1197.449,      -1, 0.5),
    ('Xi0',        1314.86,        0, 0.5),
    ('Xi-',        1321.71,       -1, 0.5),
    ('tau',        1776.86,       -1, 0.5),

    # Spin 1, 3/2 — we accept any matching-charge mode
    ('rho',        775.26,        +1, None),  # also 0, but +1 is easiest
    ('Delta+',     1232.0,        +1, None),
    ('Omega-',     1672.45,       -1, None),
]


# ════════════════════════════════════════════════════════════════════
#  Geometry defaults (unchanged from Track 6/7)
# ════════════════════════════════════════════════════════════════════

EPS_E = 0.65
EPS_NU = 5.0
EPS_P = 0.55
S_NU_DEFAULT = 0.022
N_E_REF = (1, 2)
N_P_REF = (1, 3)


def build_calibrated_model(s_e_sign=+1, s_p_sign=+1,
                           sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0):
    """
    Build a MaD with:
      - within-plane shears on the chosen sign branches (s_e_sign,
        s_p_sign each ±1)
      - cross-shears as specified
      - L_ring_e, L_ring_p calibrated so the electron (1,2) mode hits
        0.511 MeV and the proton (1,3) mode hits 938.272 MeV at the
        chosen geometry

    Returns (model, info) or (None, info) on failure.
    """
    s_e = solve_shear_for_alpha_signed(EPS_E, sign=s_e_sign,
                                        n_tube=N_E_REF[0], n_ring=N_E_REF[1])
    s_p = solve_shear_for_alpha_signed(EPS_P, sign=s_p_sign,
                                        n_tube=N_P_REF[0], n_ring=N_P_REF[1])
    s_nu = S_NU_DEFAULT

    if s_e is None or s_p is None:
        return None, {'reason': 'no shear solution'}

    # Build a dummy metric (independent of L) to compute μ_eff
    L_dummy = _build_circumferences(
        EPS_E, s_e, 1.0, EPS_NU, s_nu, 1.0, EPS_P, s_p, 1.0)
    Gt, Gti = _build_metric(
        L_dummy, s_e, s_nu, s_p,
        sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)
    if Gt is None:
        return None, {'reason': 'metric not positive-definite'}

    # Calibrate L_ring_e from the electron reference mode
    n_e_d = np.array([N_E_REF[0] / EPS_E, N_E_REF[1], 0, 0, 0, 0])
    mu_eff_e = math.sqrt(float(n_e_d @ Gti @ n_e_d))
    L_ring_e = _TWO_PI_HC * mu_eff_e / M_E_MEV

    # Calibrate L_ring_p from the proton reference mode
    n_p_d = np.array([0, 0, 0, 0, N_P_REF[0] / EPS_P, N_P_REF[1]])
    mu_eff_p = math.sqrt(float(n_p_d @ Gti @ n_p_d))
    L_ring_p = _TWO_PI_HC * mu_eff_p / M_P_MEV

    E0_nu_MeV = math.sqrt(DM2_21 / (4 * s_nu)) * 1e-6
    L_ring_nu = _TWO_PI_HC / E0_nu_MeV

    try:
        model = MaD(
            eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
            s_e=s_e, s_nu=s_nu, s_p=s_p,
            L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
            sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)
        model._n_p = N_P_REF
    except ValueError:
        return None, {'reason': 'model construction failed'}

    info = {
        's_e': s_e, 's_p': s_p, 's_nu': s_nu,
        'L_ring_e': L_ring_e, 'L_ring_p': L_ring_p,
        'L_ring_nu': L_ring_nu,
    }
    return model, info


# ════════════════════════════════════════════════════════════════════
#  Candidate generation
# ════════════════════════════════════════════════════════════════════

def generate_candidates(n_ranges, charge_target, spin_target):
    """
    Generate all 6-tuples whose charge equals charge_target.

    spin_target may be 0.5, 0.0, or None (don't filter on spin).
    No waveguide filter is applied.
    """
    out = []
    for n in iproduct(*[range(lo, hi + 1) for lo, hi in n_ranges]):
        if all(ni == 0 for ni in n):
            continue
        if MaD.charge(n) != charge_target:
            continue
        if spin_target is not None and MaD.spin_total(n) != spin_target:
            continue
        out.append(n)
    return out


def batch_energies(cand_arr, L, Gti):
    """Vectorized energy for many modes."""
    n_over_L = cand_arr / L
    E2 = _TWO_PI_HC ** 2 * np.sum((n_over_L @ Gti) * n_over_L, axis=1)
    return np.sqrt(np.maximum(E2, 0))


# ════════════════════════════════════════════════════════════════════
#  Verdict helper
# ════════════════════════════════════════════════════════════════════

def verdict(rel_err):
    """Tolerance ladder."""
    if rel_err <= 0.01:
        return 'EXCELLENT'
    if rel_err <= 0.05:
        return 'viable   '
    if rel_err <= 0.10:
        return 'marginal '
    if rel_err <= 0.30:
        return 'distant  '
    return 'NO MATCH '


# ════════════════════════════════════════════════════════════════════
#  Main search
# ════════════════════════════════════════════════════════════════════

# Branch labels
BRANCHES = [
    ('++', +1, +1),
    ('+-', +1, -1),
    ('-+', -1, +1),
    ('--', -1, -1),
]


def search_one_particle(name, target_mass, charge, spin,
                        candidates_by_charge, models):
    """
    Search across all branches and σ_eν grid for the best candidate
    matching this particle.

    Returns dict with best result and a per-branch breakdown.
    """
    if charge not in candidates_by_charge:
        return {'name': name, 'target': target_mass, 'charge': charge,
                'spin': spin, 'best': None, 'per_branch': None,
                'forbidden': 'no_candidates_for_charge'}

    cands = candidates_by_charge[charge]['cands']
    cand_arr = candidates_by_charge[charge]['arr']

    # If spin filter applies, sub-select
    if spin is not None:
        spin_mask = np.array([MaD.spin_total(n) == spin for n in cands])
        cand_arr = cand_arr[spin_mask]
        cands = [c for c, m in zip(cands, spin_mask) if m]

    if len(cands) == 0:
        # No 6-tuples in the search range satisfy this (Q, spin) combo.
        # For Q = ±1, spin = 0 this is the topological spin-charge
        # constraint (R50 F17): odd Q forces an odd number of odd
        # tube windings, which forces total spin ≥ ½.
        return {'name': name, 'target': target_mass, 'charge': charge,
                'spin': spin, 'best': None, 'per_branch': None,
                'forbidden': 'topological_spin_charge_constraint'}

    best_overall = None
    best_per_branch = {}

    for branch_label, _, _ in BRANCHES:
        best_branch = None
        for (sigma_enu, model) in models[branch_label]:
            energies = batch_energies(cand_arr, model.L, model.metric_inv)
            diffs = np.abs(energies - target_mass)
            i_best = int(np.argmin(diffs))
            E_best = float(energies[i_best])
            dm = E_best - target_mass
            rel = abs(dm) / target_mass

            entry = {
                'mode': cands[i_best],
                'E': E_best,
                'dm': dm,
                'rel': rel,
                'branch': branch_label,
                'sigma_enu': sigma_enu,
                'prop': model.propagates(cands[i_best]),
                'sheets': model.active_sheets(cands[i_best]),
            }
            if best_branch is None or rel < best_branch['rel']:
                best_branch = entry
            if best_overall is None or rel < best_overall['rel']:
                best_overall = entry
        best_per_branch[branch_label] = best_branch

    return {
        'name': name,
        'target': target_mass,
        'charge': charge,
        'spin': spin,
        'best': best_overall,
        'per_branch': best_per_branch,
    }


def histogram_qm1_spin_half(model, n_ranges, edges):
    """Build a histogram of Q=-1 spin-½ mode energies."""
    cands = generate_candidates(n_ranges, charge_target=-1, spin_target=0.5)
    cand_arr = np.array(cands, dtype=float)
    energies = batch_energies(cand_arr, model.L, model.metric_inv)
    counts, _ = np.histogram(energies, bins=edges)
    return counts, len(cands)


def main():
    print("=" * 78)
    print("R50 Track 8: Lepton viability search")
    print("=" * 78)
    print()
    print("Question: under the corrected mode-aware shear formula and")
    print("all four sign branches, does the linear ℤ⁶ spectrum admit a")
    print("viable candidate (Δm/m ≤ 5%) for every particle in the inventory?")
    print()

    # ── Candidate generation ─────────────────────────────────────────
    n_ranges = [
        (-3, 3),    # n₁  electron tube
        (-10, 10),  # n₂  electron ring  (wide enough for (1,1)..(1,10))
        (-3, 3),    # n₃  neutrino tube
        (-3, 3),    # n₄  neutrino ring
        (-6, 6),    # n₅  proton tube
        (-16, 16),  # n₆  proton ring
    ]

    total_search = 1
    for lo, hi in n_ranges:
        total_search *= (hi - lo + 1)
    print(f"Search space: {total_search:,} 6-tuples")
    print(f"  n₁ ∈ [{n_ranges[0][0]}, {n_ranges[0][1]}]   "
          f"n₂ ∈ [{n_ranges[1][0]}, {n_ranges[1][1]}]   "
          f"(includes (1,1), (1,2), (1,3), (1,4)... e-base)")
    print(f"  n₃ ∈ [{n_ranges[2][0]}, {n_ranges[2][1]}]   "
          f"n₄ ∈ [{n_ranges[3][0]}, {n_ranges[3][1]}]   "
          f"(allows ν dressing)")
    print(f"  n₅ ∈ [{n_ranges[4][0]}, {n_ranges[4][1]}]   "
          f"n₆ ∈ [{n_ranges[5][0]}, {n_ranges[5][1]}]   "
          f"(allows p-sheet windings)")
    print()

    # Group candidates by charge so we don't regenerate per particle
    candidates_by_charge = {}
    for q in (-1, 0, +1):
        cands = generate_candidates(n_ranges, charge_target=q, spin_target=None)
        candidates_by_charge[q] = {
            'cands': cands,
            'arr': np.array(cands, dtype=float),
        }
        print(f"  Q = {q:+d}: {len(cands):,} candidates (no spin filter yet)")
    print()

    # ── Build calibrated models on a σ_eν grid for each branch ──────
    sigma_grid = np.linspace(-0.20, +0.20, 21)
    print(f"σ_eν grid: {len(sigma_grid)} points in [{sigma_grid[0]:+.2f}, "
          f"{sigma_grid[-1]:+.2f}]")
    print()

    print("Building calibrated models for each (sign branch, σ_eν)...")
    models = {label: [] for label, _, _ in BRANCHES}
    for label, s_e_sign, s_p_sign in BRANCHES:
        n_built = 0
        for sigma in sigma_grid:
            m, info = build_calibrated_model(
                s_e_sign=s_e_sign, s_p_sign=s_p_sign,
                sigma_enu=float(sigma))
            if m is not None:
                models[label].append((float(sigma), m))
                n_built += 1
        print(f"  Branch {label}: {n_built}/{len(sigma_grid)} models built")
    print()

    # Sanity check: print baseline electron and proton energies for ++
    m_pp, _ = build_calibrated_model(+1, +1)
    if m_pp is not None:
        E_e = m_pp.energy((N_E_REF[0], N_E_REF[1], 0, 0, 0, 0))
        E_p = m_pp.energy((0, 0, 0, 0, N_P_REF[0], N_P_REF[1]))
        print(f"Baseline (++ branch, σ=0):")
        print(f"  E({N_E_REF}) = {E_e:.6f} MeV  (target: {M_E_MEV:.6f})")
        print(f"  E({N_P_REF}) = {E_p:.4f} MeV  (target: {M_P_MEV:.4f})")
        print()

    # ── Per-particle search ─────────────────────────────────────────
    print("=" * 78)
    print("Per-particle viability search")
    print("=" * 78)
    print()

    results = []
    for name, mass, q, spin in INVENTORY:
        r = search_one_particle(
            name, mass, q, spin, candidates_by_charge, models)
        results.append(r)

    # ── Viability table ─────────────────────────────────────────────
    print(f"{'Particle':>11s}  {'M_obs':>9s}  Q  {'spin':>5s}  "
          f"{'Best E':>10s}  {'Δm/m':>8s}  {'mode':>22s}  "
          f"{'br':>3s}  {'σ_eν':>6s}  {'verdict':>10s}")
    print(f"{'─'*11}  {'─'*9}  {'─'}  {'─'*5}  {'─'*10}  {'─'*8}  "
          f"{'─'*22}  {'─'*3}  {'─'*6}  {'─'*10}")
    for r in results:
        if r is None:
            continue
        spin_str = (f"{r['spin']:.1f}" if r['spin'] is not None else 'any')
        if r['best'] is None:
            reason = r.get('forbidden', 'no_candidates')
            print(f"{r['name']:>11s}  {r['target']:>9.3f}  "
                  f"{r['charge']:+d}  {spin_str:>5s}  "
                  f"{'—':>10s}  {'—':>8s}  "
                  f"{'(no candidates)':>22s}  {'—':>3s}  "
                  f"{'—':>6s}  FORBIDDEN ({reason})")
            continue
        b = r['best']
        v = verdict(b['rel'])
        propmark = '✓' if b['prop'] else '✗'
        print(f"{r['name']:>11s}  {r['target']:>9.3f}  "
              f"{r['charge']:+d}  {spin_str:>5s}  "
              f"{b['E']:>10.3f}  {b['rel']*100:>7.3f}%  "
              f"{str(b['mode']):>22s}  {b['branch']:>3s}  "
              f"{b['sigma_enu']:>+6.2f}  {v}{propmark}")
    print()

    # ── Lepton focus ────────────────────────────────────────────────
    print("=" * 78)
    print("Lepton focus: muon and tau")
    print("=" * 78)
    print()
    for target_name in ('muon', 'tau'):
        r = next(r for r in results if r is not None and r['name'] == target_name)
        print(f"  {target_name.upper()}  (M_obs = {r['target']:.4f} MeV)")
        print(f"  {'─' * 70}")
        for branch, _, _ in BRANCHES:
            e = r['per_branch'][branch]
            propmark = '✓' if e['prop'] else '✗'
            print(f"    branch {branch}:  mode={str(e['mode']):>22s}  "
                  f"E={e['E']:>10.3f}  Δm/m={e['rel']*100:>7.3f}%  "
                  f"σ={e['sigma_enu']:>+5.2f}  prop={propmark}  "
                  f"sheets={e['sheets']}")
        b = r['best']
        print(f"    BEST:  {verdict(b['rel'])}  {b['rel']*100:.3f}%  "
              f"on branch {b['branch']}  σ={b['sigma_enu']:+.2f}")
        print()

    # ── Mass-desert histogram (the original question) ───────────────
    print("=" * 78)
    print("Mass-desert histogram: Q = −1, spin-½ modes")
    print("=" * 78)
    print()
    hist_edges = np.array([0, 1, 5, 20, 50, 100, 150, 200, 300, 500, 750, 1000,
                            1500, 2000, 3000])
    print(f"  bins (MeV): {list(hist_edges)}")
    print()
    print(f"  {'branch':>6s}  ", end='')
    for i in range(len(hist_edges) - 1):
        print(f"{hist_edges[i]:>4d}-{hist_edges[i+1]:<4d} ", end='')
    print()
    print(f"  {'─'*6}  ", end='')
    for _ in range(len(hist_edges) - 1):
        print("─" * 9 + " ", end='')
    print()
    for branch, s_e_sign, s_p_sign in BRANCHES:
        m, _ = build_calibrated_model(s_e_sign, s_p_sign, sigma_enu=0.0)
        if m is None:
            continue
        counts, total = histogram_qm1_spin_half(m, n_ranges, hist_edges)
        print(f"  {branch:>6s}  ", end='')
        for c in counts:
            print(f"{c:>9d} ", end='')
        print(f" (total in window: {sum(counts)} of {total})")
    print()

    # ── Final assessment ────────────────────────────────────────────
    print("=" * 78)
    print("Assessment")
    print("=" * 78)
    print()
    have_best = [r for r in results if r and r['best'] is not None]
    forbidden = [r for r in results if r and r['best'] is None]
    n_excellent = sum(1 for r in have_best if r['best']['rel'] <= 0.01)
    n_viable = sum(1 for r in have_best if r['best']['rel'] <= 0.05)
    n_marginal = sum(1 for r in have_best if r['best']['rel'] <= 0.10)
    n_distant = sum(1 for r in have_best if r['best']['rel'] <= 0.30)
    n_total = len(have_best) + len(forbidden)
    print(f"  Inventory: {n_total} particles")
    print(f"    Excellent  (≤  1%):    {n_excellent}")
    print(f"    Viable     (≤  5%):    {n_viable}")
    print(f"    Marginal   (≤ 10%):    {n_marginal}")
    print(f"    Distant    (≤ 30%):    {n_distant}")
    print(f"    NO MATCH   (> 30%):    {len(have_best) - n_distant}")
    print(f"    FORBIDDEN  (Q,spin):   {len(forbidden)}")
    if forbidden:
        names = ', '.join(r['name'] for r in forbidden)
        print(f"      ({names} — topological spin-charge constraint, R50 F17)")
    print()

    muon = next(r for r in results if r and r['name'] == 'muon')
    tau = next(r for r in results if r and r['name'] == 'tau')
    print(f"  Muon best:  {muon['best']['rel']*100:.3f}%  "
          f"({verdict(muon['best']['rel']).strip()})")
    print(f"  Tau best:   {tau['best']['rel']*100:.3f}%  "
          f"({verdict(tau['best']['rel']).strip()})")
    print()
    if muon['best']['rel'] <= 0.05:
        print("  → MUON IS VIABLE in the linear spectrum.")
        print("    Compound back-reaction engine NOT required for muon.")
    elif muon['best']['rel'] <= 0.10:
        print("  → Muon is marginal — borderline case.")
        print("    Compound engine would help but is not strictly required.")
    else:
        print("  → MUON IS NOT VIABLE in the linear spectrum.")
        print("    The linear ℤ⁶ picture cannot host the muon at any sign")
        print("    branch or σ_eν value tested.  This is a structural")
        print("    result motivating the compound back-reaction engine.")
    print()
    print("Track 8 complete.")


if __name__ == '__main__':
    main()
