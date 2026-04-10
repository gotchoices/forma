"""
R50 Track 9: Paired-mode meson search

Track 8 (F58) found that charged pions and kaons cannot exist as
single 6-tuples in the linear MaD spectrum because the topological
spin-charge constraint forces |Q| = 1 ⇒ spin ≥ ½, but π± and K±
have spin 0.

This track tests the natural rescue: **pairs of spin-½ modes
coupled antisymmetrically into a spin-0 singlet**.  This is exactly
how the standard model treats mesons (qq̄ pairs in singlet
configurations).  In the MaD formalism it amounts to:

  meson_mass ≈ E(mode_A) + E(mode_B)
  meson_charge = Q(mode_A) + Q(mode_B)
  meson_spin = 0  (from the singlet coupling of two spin-½ modes)

We enumerate pairs (A, B) of single-mode candidates and look for
the closest pair-sum to each meson target.

This track also tests whether the desert that kills the muon at
the single-mode level kills it again at the pair-sum level — i.e.,
whether two-mode composites can reach 105.7 MeV when single modes
cannot.
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
#  Targets — particles for which paired-mode search is interesting
# ════════════════════════════════════════════════════════════════════

PAIRED_TARGETS = [
    # Mesons that fail as single modes
    ('pi+',     139.57039,  +1, 'meson'),
    ('pi-',     139.57039,  -1, 'meson'),
    ('K+',      493.677,    +1, 'meson'),
    ('K-',      493.677,    -1, 'meson'),
    ('pi0',     134.9768,    0, 'meson'),
    ('K0',      497.611,     0, 'meson'),
    # Lepton retest: can a pair reach the muon?
    ('muon',    105.65837,  -1, 'lepton'),
    ('mu+',     105.65837,  +1, 'lepton'),
    # Sanity: tau as a pair
    ('tau',     1776.86,    -1, 'lepton'),
]


# ════════════════════════════════════════════════════════════════════
#  Geometry defaults — same as Tracks 6/7/8
# ════════════════════════════════════════════════════════════════════

EPS_E = 0.65
EPS_NU = 5.0
EPS_P = 0.55
S_NU_DEFAULT = 0.022
N_E_REF = (1, 2)
N_P_REF = (1, 3)


def build_calibrated_model(s_e_sign=+1, s_p_sign=+1,
                           sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0):
    """Same as Track 8.  Pinned electron + proton on chosen branch."""
    s_e = solve_shear_for_alpha_signed(EPS_E, sign=s_e_sign,
                                        n_tube=N_E_REF[0], n_ring=N_E_REF[1])
    s_p = solve_shear_for_alpha_signed(EPS_P, sign=s_p_sign,
                                        n_tube=N_P_REF[0], n_ring=N_P_REF[1])
    s_nu = S_NU_DEFAULT
    if s_e is None or s_p is None:
        return None

    L_dummy = _build_circumferences(
        EPS_E, s_e, 1.0, EPS_NU, s_nu, 1.0, EPS_P, s_p, 1.0)
    Gt, Gti = _build_metric(
        L_dummy, s_e, s_nu, s_p,
        sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)
    if Gt is None:
        return None

    n_e_d = np.array([N_E_REF[0] / EPS_E, N_E_REF[1], 0, 0, 0, 0])
    mu_eff_e = math.sqrt(float(n_e_d @ Gti @ n_e_d))
    L_ring_e = _TWO_PI_HC * mu_eff_e / M_E_MEV

    n_p_d = np.array([0, 0, 0, 0, N_P_REF[0] / EPS_P, N_P_REF[1]])
    mu_eff_p = math.sqrt(float(n_p_d @ Gti @ n_p_d))
    L_ring_p = _TWO_PI_HC * mu_eff_p / M_P_MEV

    E0_nu_MeV = math.sqrt(DM2_21 / (4 * s_nu)) * 1e-6
    L_ring_nu = _TWO_PI_HC / E0_nu_MeV

    try:
        return MaD(
            eps_e=EPS_E, eps_nu=EPS_NU, eps_p=EPS_P,
            s_e=s_e, s_nu=s_nu, s_p=s_p,
            L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
            sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup)
    except ValueError:
        return None


def generate_modes_by_charge(n_ranges):
    """Group all spin-½ candidates by charge."""
    by_q = {-2: [], -1: [], 0: [], +1: [], +2: []}
    for n in iproduct(*[range(lo, hi + 1) for lo, hi in n_ranges]):
        if all(ni == 0 for ni in n):
            continue
        if MaD.spin_total(n) != 0.5:
            continue
        q = MaD.charge(n)
        if q in by_q:
            by_q[q].append(n)
    return by_q


def batch_energies(cand_arr, L, Gti):
    n_over_L = cand_arr / L
    E2 = _TWO_PI_HC ** 2 * np.sum((n_over_L @ Gti) * n_over_L, axis=1)
    return np.sqrt(np.maximum(E2, 0))


# ════════════════════════════════════════════════════════════════════
#  Pair search
# ════════════════════════════════════════════════════════════════════

def best_pair(modes_by_q, energies_by_q, q_target, target_mass,
              max_each=2000, mass_cap=None):
    """
    Find the spin-½ pair (A, B) with Q(A)+Q(B) = q_target
    minimizing |E(A) + E(B) - target_mass|.

    To keep the pair-count tractable, we cap each per-Q list at
    `max_each` modes (the lightest ones).  We also cut off at
    `mass_cap` if provided (defaults to 2× target_mass).
    """
    if mass_cap is None:
        mass_cap = 2.5 * target_mass + 50.0  # generous

    decompositions = []
    for q_a in (-2, -1, 0, +1, +2):
        q_b = q_target - q_a
        if q_b not in modes_by_q:
            continue
        if q_a > q_b:  # avoid double-counting symmetric pairs
            continue
        decompositions.append((q_a, q_b))

    best = None
    for (q_a, q_b) in decompositions:
        # Light-first list, capped
        idx_a = np.argsort(energies_by_q[q_a])
        idx_b = np.argsort(energies_by_q[q_b])

        # Filter by mass cap
        e_a_full = energies_by_q[q_a][idx_a]
        e_b_full = energies_by_q[q_b][idx_b]
        mask_a = e_a_full < mass_cap
        mask_b = e_b_full < mass_cap
        idx_a = idx_a[mask_a][:max_each]
        idx_b = idx_b[mask_b][:max_each]

        if len(idx_a) == 0 or len(idx_b) == 0:
            continue

        e_a = energies_by_q[q_a][idx_a]
        e_b = energies_by_q[q_b][idx_b]

        # Pair sum matrix; broadcasting
        sums = e_a[:, None] + e_b[None, :]
        diffs = np.abs(sums - target_mass)

        # If we're searching same-Q pairs, exclude i==j (a mode pairing
        # with itself).  Allow i<j, count each pair once.
        if q_a == q_b:
            iu = np.triu_indices(len(idx_a), k=1)
            diffs_flat = diffs[iu]
            sums_flat = sums[iu]
            ai_flat = idx_a[iu[0]]
            bi_flat = idx_b[iu[1]]
        else:
            diffs_flat = diffs.ravel()
            sums_flat = sums.ravel()
            mesh_a, mesh_b = np.meshgrid(idx_a, idx_b, indexing='ij')
            ai_flat = mesh_a.ravel()
            bi_flat = mesh_b.ravel()

        if len(diffs_flat) == 0:
            continue
        i_min = int(np.argmin(diffs_flat))
        e_pair = float(sums_flat[i_min])
        delta = e_pair - target_mass
        rel = abs(delta) / target_mass
        mode_a = modes_by_q[q_a][int(ai_flat[i_min])]
        mode_b = modes_by_q[q_b][int(bi_flat[i_min])]
        e_a_indiv = energies_by_q[q_a][int(ai_flat[i_min])]
        e_b_indiv = energies_by_q[q_b][int(bi_flat[i_min])]

        entry = {
            'q_a': q_a, 'q_b': q_b,
            'mode_a': mode_a, 'mode_b': mode_b,
            'E_a': float(e_a_indiv), 'E_b': float(e_b_indiv),
            'E_pair': e_pair,
            'delta': delta, 'rel': rel,
        }
        if best is None or rel < best['rel']:
            best = entry
    return best


# ════════════════════════════════════════════════════════════════════
#  Main
# ════════════════════════════════════════════════════════════════════

BRANCHES = [
    ('++', +1, +1),
    ('+-', +1, -1),
    ('-+', -1, +1),
    ('--', -1, -1),
]


def verdict(rel_err):
    if rel_err <= 0.01:
        return 'EXCELLENT'
    if rel_err <= 0.05:
        return 'viable   '
    if rel_err <= 0.10:
        return 'marginal '
    if rel_err <= 0.30:
        return 'distant  '
    return 'NO MATCH '


def main():
    print("=" * 78)
    print("R50 Track 9: Paired-mode meson search")
    print("=" * 78)
    print()
    print("Question: can charged pions/kaons (and the muon) be reached as")
    print("the spin-singlet sum of two spin-½ MaD modes, escaping the")
    print("topological spin-charge constraint that forbids them as single")
    print("6-tuples?")
    print()

    # Wider winding range; we want the lightest few thousand spin-½ modes
    # in each charge bucket.
    n_ranges = [
        (-3, 3),    # n₁
        (-10, 10),  # n₂
        (-3, 3),    # n₃
        (-3, 3),    # n₄
        (-6, 6),    # n₅
        (-16, 16),  # n₆
    ]

    print("Generating spin-½ candidates by charge...")
    modes_by_q = generate_modes_by_charge(n_ranges)
    for q in sorted(modes_by_q.keys()):
        print(f"  Q = {q:+d}:  {len(modes_by_q[q]):,} spin-½ modes")
    print()

    # Convert to arrays once
    arr_by_q = {q: np.array(modes_by_q[q], dtype=float) for q in modes_by_q}

    sigma_grid = np.linspace(-0.20, +0.20, 11)

    # ── Per branch × σ_eν, compute energies and search ─────────────
    all_results = {name: None for name, *_ in PAIRED_TARGETS}

    print("Searching pair sums across all branches and σ_eν grid...")
    print()

    for branch_label, s_e_sign, s_p_sign in BRANCHES:
        for sigma in sigma_grid:
            m = build_calibrated_model(
                s_e_sign=s_e_sign, s_p_sign=s_p_sign,
                sigma_enu=float(sigma))
            if m is None:
                continue

            # Compute energies once for each Q-bucket
            energies_by_q = {}
            for q in modes_by_q:
                if len(arr_by_q[q]) > 0:
                    energies_by_q[q] = batch_energies(
                        arr_by_q[q], m.L, m.metric_inv)
                else:
                    energies_by_q[q] = np.array([])

            for name, mass, q_target, _ in PAIRED_TARGETS:
                bp = best_pair(modes_by_q, energies_by_q,
                               q_target, mass, max_each=1500)
                if bp is None:
                    continue
                bp['branch'] = branch_label
                bp['sigma_enu'] = float(sigma)

                cur = all_results[name]
                if cur is None or bp['rel'] < cur['rel']:
                    all_results[name] = bp

        # Progress
        print(f"  Branch {branch_label} done")
    print()

    # ── Report ──────────────────────────────────────────────────────
    print("=" * 78)
    print("Best paired-mode candidates")
    print("=" * 78)
    print()
    print(f"{'Particle':>9s}  {'M_obs':>9s}  Q  "
          f"{'E_pair':>10s}  {'Δm/m':>8s}  {'br':>3s}  "
          f"{'σ':>6s}  decomposition")
    print(f"{'─'*9}  {'─'*9}  {'─'}  {'─'*10}  {'─'*8}  "
          f"{'─'*3}  {'─'*6}  {'─'*60}")
    for name, mass, q_target, kind in PAIRED_TARGETS:
        r = all_results[name]
        if r is None:
            print(f"{name:>9s}  {mass:>9.3f}  {q_target:+d}  "
                  f"{'—':>10s}  {'—':>8s}  {'—':>3s}  "
                  f"{'—':>6s}  (no pairs found)")
            continue
        v = verdict(r['rel'])
        decomp = (f"Q{r['q_a']:+d}({r['E_a']:6.2f})·Q{r['q_b']:+d}"
                  f"({r['E_b']:6.2f})")
        print(f"{name:>9s}  {mass:>9.3f}  {q_target:+d}  "
              f"{r['E_pair']:>10.3f}  {r['rel']*100:>7.3f}%  "
              f"{r['branch']:>3s}  {r['sigma_enu']:>+6.2f}  "
              f"{v}  {decomp}")
    print()

    # ── Detailed dumps for the most interesting cases ──────────────
    print("=" * 78)
    print("Mode detail for key candidates")
    print("=" * 78)
    print()
    for name in ('pi+', 'K+', 'pi0', 'muon'):
        r = all_results.get(name)
        if r is None:
            print(f"  {name}: no pair found")
            continue
        print(f"  {name}  (target {dict((n, m) for n, m, _, _ in PAIRED_TARGETS)[name]:.3f} MeV)")
        print(f"    decomposition: ({r['mode_a']}) + ({r['mode_b']})")
        print(f"    Q: {r['q_a']:+d} + {r['q_b']:+d} = "
              f"{r['q_a'] + r['q_b']:+d}")
        print(f"    E: {r['E_a']:.3f} + {r['E_b']:.3f} = "
              f"{r['E_pair']:.3f} MeV  (Δ = {r['delta']:+.3f}, "
              f"{r['rel']*100:.3f}%)")
        print(f"    branch {r['branch']}, σ_eν = {r['sigma_enu']:+.2f}")
        print()

    # ── Assessment ──────────────────────────────────────────────────
    print("=" * 78)
    print("Assessment")
    print("=" * 78)
    print()

    pi_p = all_results.get('pi+')
    k_p = all_results.get('K+')
    mu = all_results.get('muon')
    pi_0 = all_results.get('pi0')

    print(f"  pi+:   best Δm/m = {pi_p['rel']*100:.3f}%  "
          f"({verdict(pi_p['rel']).strip()})")
    print(f"  K+:    best Δm/m = {k_p['rel']*100:.3f}%  "
          f"({verdict(k_p['rel']).strip()})")
    print(f"  pi0:   best Δm/m = {pi_0['rel']*100:.3f}%  "
          f"({verdict(pi_0['rel']).strip()})")
    print(f"  muon:  best Δm/m = {mu['rel']*100:.3f}%  "
          f"({verdict(mu['rel']).strip()})")
    print()
    print("Track 9 complete.")


if __name__ == '__main__':
    main()
