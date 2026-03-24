"""
T⁶ discovery engine — search for oscillation patterns matching
target particle properties.

Sits on top of lib/t6.py.  Provides:

  find_modes()              Search for modes matching a target
                            (mass, charge, spin).

  self_consistent_metric()  Build a metric where input particle
                            masses are exact at any cross-shear.

  self_consistent_metric_asym()  Same, with 12 independent σ_ij.

  multi_target_optimize()   Find parameter regions where multiple
                            targets are matched simultaneously.


TYPICAL USAGE
=============

    from lib.t6_solver import find_modes, self_consistent_metric

    # Find charge-0, spin-½ modes near the neutron mass
    results = find_modes(
        target_mass_MeV=939.565,
        target_charge=0,
        target_spin_halves=1,
        r_e=6.6, r_nu=5.0, r_p=6.6,
        sigma_ep=-0.3,
        n_max=5,
        mass_tolerance_MeV=5.0,
        self_consistent=True,
    )
    for r in results[:5]:
        print(r)

    # Optimize cross-shears to match neutron + muon simultaneously
    from lib.t6_solver import multi_target_optimize

    targets = [
        {'mass_MeV': 939.565, 'charge': 0, 'spin_halves': 1},
        {'mass_MeV': 105.658, 'charge': -1, 'spin_halves': 1},
    ]
    best = multi_target_optimize(targets, r_e=6.6, r_nu=5.0, r_p=6.6)


ORIGINS
=======
Created for R27 Track 2 to generalize the ad hoc searches of
R26 Track 4 and R27 Track 1 into a reusable discovery tool.
"""

import math
import numpy as np
from itertools import product as iproduct
from scipy.optimize import minimize, differential_evolution

from lib.t6 import (
    build_scaled_metric, compute_scales, mode_energy, mode_charge,
    mode_spin, is_positive_definite, hbar_c_MeV_fm,
    M_E_MEV, M_P_MEV, M_N_MEV, S34,
    alpha_kk, solve_shear_for_alpha, mu_12,
)


# Reference modes for self-consistency constraints
_N_ELECTRON = np.array([1, 2, 0, 0, 0, 0], dtype=float)
_N_PROTON   = np.array([0, 0, 0, 0, 1, 2], dtype=float)
_N_NU1      = np.array([0, 0, 1, 1, 0, 0], dtype=float)


# ══════════════════════════════════════════════════════════════════════
#  Self-consistent metric
# ══════════════════════════════════════════════════════════════════════

def _build_metric_from_L(L, s12, s34, s56, sigma_ep, sigma_enu, sigma_nup):
    """
    Build G̃ from explicit circumferences and shears.

    Like build_scaled_metric() but takes L directly instead of
    deriving it from aspect ratios.  Needed for the self-consistent
    solver where L is iteratively adjusted.

    Returns (Gtilde, Gtilde_inv) or (None, None) if not positive-definite.
    """
    S_within = np.zeros((6, 6))
    S_within[0, 1] = s12
    S_within[2, 3] = s34
    S_within[4, 5] = s56

    B = np.diag(L) @ (np.eye(6) + S_within)
    G_phys = B.T @ B

    Gtilde = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            if L[i] == 0 or L[j] == 0:
                return None, None
            Gtilde[i, j] = G_phys[i, j] / (L[i] * L[j])

    cross_pairs = {
        'enu': [(0, 2), (0, 3), (1, 2), (1, 3)],
        'ep':  [(0, 4), (0, 5), (1, 4), (1, 5)],
        'nup': [(2, 4), (2, 5), (3, 4), (3, 5)],
    }
    sigmas = {'enu': sigma_enu, 'ep': sigma_ep, 'nup': sigma_nup}
    for block, pairs in cross_pairs.items():
        sig = sigmas[block]
        for i, j in pairs:
            Gtilde[i, j] = sig
            Gtilde[j, i] = sig

    if not is_positive_definite(Gtilde):
        return None, None

    return Gtilde, np.linalg.inv(Gtilde)


def self_consistent_metric(r_e, r_nu, r_p,
                           sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0,
                           tol=1e-12, max_iter=50):
    """
    Build a T⁶ metric where input particle masses are exact.

    Iteratively adjusts L₂ (electron ring), L₄ (neutrino ring),
    and L₆ (proton ring) so that:
        E(1,2,0,0,0,0) = m_e
        E(0,0,0,0,1,2) = m_p

    at the given cross-shear values.  Neutrino scales are also
    adjusted to preserve Δm²₂₁.

    Parameters
    ----------
    r_e, r_nu, r_p : float
        Aspect ratios.
    sigma_ep, sigma_enu, sigma_nup : float
        Cross-plane shear parameters.
    tol : float
        Convergence tolerance (relative mass error).
    max_iter : int
        Maximum iterations.

    Returns
    -------
    dict with keys:
        'Gtilde'     : ndarray (6,6) — dimensionless metric
        'Gtilde_inv' : ndarray (6,6) — inverse metric
        'L'          : ndarray (6,)  — circumferences in fm
        's12', 's34', 's56' : float — within-plane shears
        'converged'  : bool
        'iterations' : int
    """
    L, s12, s34, s56 = compute_scales(r_e, r_nu, r_p)

    for iteration in range(max_iter):
        Gt, Gti = _build_metric_from_L(
            L, s12, s34, s56, sigma_ep, sigma_enu, sigma_nup)

        if Gt is None:
            return {'converged': False, 'iterations': iteration,
                    'reason': 'metric not positive-definite'}

        E_e = mode_energy(_N_ELECTRON, Gti, L)
        E_p = mode_energy(_N_PROTON, Gti, L)

        err_e = abs(E_e - M_E_MEV) / M_E_MEV
        err_p = abs(E_p - M_P_MEV) / M_P_MEV

        if err_e < tol and err_p < tol:
            return {
                'Gtilde': Gt, 'Gtilde_inv': Gti, 'L': L.copy(),
                's12': s12, 's34': s34, 's56': s56,
                'converged': True, 'iterations': iteration + 1,
            }

        L[1] *= E_e / M_E_MEV
        L[0] = r_e * L[1]
        L[5] *= E_p / M_P_MEV
        L[4] = r_p * L[5]

    return {'converged': False, 'iterations': max_iter,
            'reason': 'max iterations reached'}


# ══════════════════════════════════════════════════════════════════════
#  Asymmetric cross-shear metric
# ══════════════════════════════════════════════════════════════════════

# Indices for the 12 independent cross-shear entries.
# e-p block:  (0,4)=σ₁₅  (0,5)=σ₁₆  (1,4)=σ₂₅  (1,5)=σ₂₆
# e-ν block:  (0,2)=σ₁₃  (0,3)=σ₁₄  (1,2)=σ₂₃  (1,3)=σ₂₄
# ν-p block:  (2,4)=σ₃₅  (2,5)=σ₃₆  (3,4)=σ₄₅  (3,5)=σ₄₆

CROSS_INDICES = {
    'ep':  [(0, 4), (0, 5), (1, 4), (1, 5)],
    'enu': [(0, 2), (0, 3), (1, 2), (1, 3)],
    'nup': [(2, 4), (2, 5), (3, 4), (3, 5)],
}


def _build_metric_asym(L, s12, s34, s56, cross_shears):
    """
    Build G̃ with individually specified cross-shear entries.

    Parameters
    ----------
    L : ndarray (6,) — circumferences in fm.
    s12, s34, s56 : float — within-plane shears.
    cross_shears : dict mapping (i,j) tuples to float values.
        Keys are pairs like (0,4), (0,5), etc.  Missing entries
        default to zero.

    Returns
    -------
    (Gtilde, Gtilde_inv) or (None, None) if not positive-definite.
    """
    S_within = np.zeros((6, 6))
    S_within[0, 1] = s12
    S_within[2, 3] = s34
    S_within[4, 5] = s56

    B = np.diag(L) @ (np.eye(6) + S_within)
    G_phys = B.T @ B

    Gtilde = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            if L[i] == 0 or L[j] == 0:
                return None, None
            Gtilde[i, j] = G_phys[i, j] / (L[i] * L[j])

    for (i, j), val in cross_shears.items():
        Gtilde[i, j] = val
        Gtilde[j, i] = val

    if not is_positive_definite(Gtilde):
        return None, None

    return Gtilde, np.linalg.inv(Gtilde)


def self_consistent_metric_asym(r_e, r_nu, r_p, cross_shears,
                                tol=1e-12, max_iter=50):
    """
    Self-consistent metric with 12 independent cross-shear entries.

    Like self_consistent_metric() but takes a dict of individual
    cross-shear values instead of 3 collective parameters.

    Parameters
    ----------
    r_e, r_nu, r_p : float
        Aspect ratios.
    cross_shears : dict
        Maps (i,j) index pairs to float values.  For example:
        {(0,4): -0.08, (0,5): -0.10, (1,4): -0.05, (1,5): -0.09}
        Missing cross-block entries default to zero.
    tol : float
        Convergence tolerance (relative mass error).
    max_iter : int
        Maximum iterations.

    Returns
    -------
    dict with keys:
        'Gtilde', 'Gtilde_inv', 'L', 's12', 's34', 's56',
        'converged', 'iterations'
    """
    L, s12, s34, s56 = compute_scales(r_e, r_nu, r_p)

    for iteration in range(max_iter):
        Gt, Gti = _build_metric_asym(L, s12, s34, s56, cross_shears)

        if Gt is None:
            return {'converged': False, 'iterations': iteration,
                    'reason': 'metric not positive-definite'}

        E_e = mode_energy(_N_ELECTRON, Gti, L)
        E_p = mode_energy(_N_PROTON, Gti, L)

        err_e = abs(E_e - M_E_MEV) / M_E_MEV
        err_p = abs(E_p - M_P_MEV) / M_P_MEV

        if err_e < tol and err_p < tol:
            return {
                'Gtilde': Gt, 'Gtilde_inv': Gti, 'L': L.copy(),
                's12': s12, 's34': s34, 's56': s56,
                'converged': True, 'iterations': iteration + 1,
            }

        L[1] *= E_e / M_E_MEV
        L[0] = r_e * L[1]
        L[5] *= E_p / M_P_MEV
        L[4] = r_p * L[5]

    return {'converged': False, 'iterations': max_iter,
            'reason': 'max iterations reached'}


# ══════════════════════════════════════════════════════════════════════
#  Single-target mode search
# ══════════════════════════════════════════════════════════════════════

def find_modes(target_mass_MeV, target_charge=None, target_spin_halves=None,
               r_e=6.6, r_nu=5.0, r_p=6.6,
               sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0,
               n_max=5, mass_tolerance_MeV=10.0,
               self_consistent=True, max_results=50):
    """
    Search for T⁶ modes matching target properties.

    Parameters
    ----------
    target_mass_MeV : float
        Target mass in MeV.
    target_charge : int or None
        Required charge in units of e.  None = any charge.
    target_spin_halves : int or None
        Required spin-½ count (1 = fermion).  None = any spin.
    r_e, r_nu, r_p : float
        Aspect ratios.
    sigma_ep, sigma_enu, sigma_nup : float
        Cross-plane shears.
    n_max : int
        Maximum |n_i| to scan.
    mass_tolerance_MeV : float
        Only return modes within this tolerance of target mass.
    self_consistent : bool
        If True, adjust circumferences so m_e and m_p are exact.
    max_results : int
        Maximum number of results to return.

    Returns
    -------
    list of dict, sorted by mass error (ascending):
        [{'n': tuple, 'E_MeV': float, 'charge': int,
          'spin_halves': int, 'mass_error_MeV': float}, ...]
    """
    if self_consistent:
        result = self_consistent_metric(
            r_e, r_nu, r_p, sigma_ep, sigma_enu, sigma_nup)
        if not result['converged']:
            return []
        Gti = result['Gtilde_inv']
        L = result['L']
    else:
        _, Gti, L, _ = build_scaled_metric(
            r_e, r_nu, r_p, sigma_ep, sigma_enu, sigma_nup)

    matches = []
    rng = range(-n_max, n_max + 1)

    for n in iproduct(rng, repeat=6):
        if all(ni == 0 for ni in n):
            continue

        if target_charge is not None:
            Q = mode_charge(n)
            if Q != target_charge:
                continue

        if target_spin_halves is not None:
            s = mode_spin(n)
            if s != target_spin_halves:
                continue

        E = mode_energy(n, Gti, L)
        err = abs(E - target_mass_MeV)
        if err > mass_tolerance_MeV:
            continue

        matches.append({
            'n': n,
            'E_MeV': E,
            'charge': mode_charge(n),
            'spin_halves': mode_spin(n),
            'mass_error_MeV': err,
        })

    matches.sort(key=lambda m: m['mass_error_MeV'])
    return matches[:max_results]


# ══════════════════════════════════════════════════════════════════════
#  Multi-target optimizer
# ══════════════════════════════════════════════════════════════════════

def _best_match_error(targets, Gti, L, n_max=5):
    """
    For each target, find the best-matching mode and return
    the total weighted mass error.

    Uses a greedy assignment (each mode can match at most one target).
    """
    total_error = 0.0
    used_modes = set()

    for t in targets:
        best_err = float('inf')
        best_n = None

        rng = range(-n_max, n_max + 1)
        for n in iproduct(rng, repeat=6):
            if all(ni == 0 for ni in n):
                continue
            if n in used_modes:
                continue

            if t.get('charge') is not None and mode_charge(n) != t['charge']:
                continue
            if t.get('spin_halves') is not None and mode_spin(n) != t['spin_halves']:
                continue

            E = mode_energy(n, Gti, L)
            err = abs(E - t['mass_MeV']) / t['mass_MeV']
            if err < best_err:
                best_err = err
                best_n = n

        if best_n is not None:
            used_modes.add(best_n)
            total_error += best_err**2
        else:
            total_error += 1.0  # penalty for no match

    return total_error


def multi_target_optimize(targets, r_e=6.6, r_nu=5.0, r_p=6.6,
                          n_max=5, sigma_bounds=(-0.5, 0.5),
                          self_consistent=True):
    """
    Find cross-shear parameters that best match multiple targets.

    Parameters
    ----------
    targets : list of dict
        Each dict has 'mass_MeV' (required), and optionally
        'charge' (int) and 'spin_halves' (int).
    r_e, r_nu, r_p : float
        Aspect ratios (fixed during optimization).
    n_max : int
        Maximum |n_i| for mode search.
    sigma_bounds : tuple (lo, hi)
        Bounds for each cross-shear parameter.
    self_consistent : bool
        If True, use self-consistent circumferences.

    Returns
    -------
    dict with keys:
        'sigma_ep', 'sigma_enu', 'sigma_nup' : float — optimal values
        'total_error' : float — sum of (relative mass errors)²
        'matches' : list of dict — best mode for each target
        'success' : bool
    """
    lo, hi = sigma_bounds

    def objective(params):
        s_ep, s_enu, s_nup = params

        if self_consistent:
            result = self_consistent_metric(
                r_e, r_nu, r_p, s_ep, s_enu, s_nup)
            if not result['converged']:
                return 1e6
            Gti = result['Gtilde_inv']
            L = result['L']
        else:
            Gt, Gti, L, _ = build_scaled_metric(
                r_e, r_nu, r_p, s_ep, s_enu, s_nup)
            if not is_positive_definite(Gt):
                return 1e6

        return _best_match_error(targets, Gti, L, n_max=n_max)

    bounds = [(lo, hi)] * 3
    result = differential_evolution(objective, bounds,
                                   seed=42, maxiter=100,
                                   tol=1e-8, polish=True)

    s_ep, s_enu, s_nup = result.x

    # Reconstruct the matches at the optimal point
    if self_consistent:
        sc = self_consistent_metric(r_e, r_nu, r_p, s_ep, s_enu, s_nup)
        if not sc['converged']:
            return {'success': False}
        Gti = sc['Gtilde_inv']
        L = sc['L']
    else:
        _, Gti, L, _ = build_scaled_metric(r_e, r_nu, r_p, s_ep, s_enu, s_nup)

    matches = []
    used = set()
    for t in targets:
        best = find_modes(
            t['mass_MeV'],
            target_charge=t.get('charge'),
            target_spin_halves=t.get('spin_halves'),
            r_e=r_e, r_nu=r_nu, r_p=r_p,
            sigma_ep=s_ep, sigma_enu=s_enu, sigma_nup=s_nup,
            n_max=n_max, mass_tolerance_MeV=t['mass_MeV'] * 0.5,
            self_consistent=self_consistent, max_results=10,
        )
        matched = None
        for m in best:
            if m['n'] not in used:
                matched = m
                used.add(m['n'])
                break
        matches.append({
            'target': t,
            'match': matched,
        })

    return {
        'sigma_ep': s_ep, 'sigma_enu': s_enu, 'sigma_nup': s_nup,
        'total_error': result.fun,
        'matches': matches,
        'success': result.success,
    }
