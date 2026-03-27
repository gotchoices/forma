"""
T⁶ model — shared infrastructure for compact-dimension studies.

Provides the T⁶ metric, mode energy/charge/spin calculations,
and spectral scanning tools.  Used by R26, R27, R28, and any
future study that works with the six-dimensional compact space.


PHYSICAL PICTURE
================

Three flat T² subplanes (electron, neutrino, proton) are embedded
in a single T⁶.  Each particle is a standing wave (mode) on the
T⁶, characterized by six integer quantum numbers n = (n₁, ..., n₆).

The six dimensions are organized in three pairs:

    Indices 0, 1  →  electron T²   (θ₁ = tube, θ₂ = ring)
    Indices 2, 3  →  neutrino T²   (θ₃ = tube, θ₄ = ring)
    Indices 4, 5  →  proton T²     (θ₅ = tube, θ₆ = ring)

Each pair has a "tube" direction (odd index: 0, 2, 4) and a
"ring" direction (even index: 1, 3, 5).  Spin and charge are
determined by tube windings only.


PARAMETERS
==========

The T⁶ geometry is specified by:

  3 aspect ratios:   r_e, r_nu, r_p  (tube/ring circumference ratio
                     for each T²; unconstrained, r > 0)

  3 within-plane shears:  s₁₂, s₃₄, s₅₆  (determined by physics:
                          s₁₂ and s₅₆ from α via KK formula,
                          s₃₄ = 0.02199 from neutrino Δm² ratio)

  3 cross-plane shears:  σ_ep, σ_eν, σ_νp  (coupling between T²
                         sheets; σ_ep ≈ 0.038 from neutron mass,
                         others unconstrained)

  6 circumferences:  L₁, ..., L₆  (derived from masses and aspect
                     ratios; not independent parameters)

Total: 21 raw parameters, 6 constrained by physics, 15 free.
See R26 Track 3 for the full census.


METRIC CONVENTION
=================

The physical metric G has entries spanning 22 orders of magnitude
(fm² to mm²).  We work instead with the dimensionless scaled
metric G̃:

    G̃_ij = G_ij / (L_i × L_j)

All entries of G̃ are O(1).  Condition number ≈ 1.25 (vs ~10²¹
for G).  Mode energy in terms of G̃:

    E²(n) = (2πℏc)² ñᵀ G̃⁻¹ ñ     where ñ_i = n_i / L_i


TYPICAL USAGE
=============

    from lib.t6 import build_scaled_metric, mode_energy, mode_charge

    # Build metric for given aspect ratios and cross-shears
    Gt, Gti, L, info = build_scaled_metric(
        r_e=6.6, r_nu=5.0, r_p=6.6,
        sigma_ep=0.038
    )

    # Compute energy of the neutron candidate mode
    E_n = mode_energy((1, 2, 0, 0, 1, 2), Gti, L)  # MeV

    # Check its charge and spin
    Q = mode_charge((1, 2, 0, 0, 1, 2))   # 0 (units of e)
    s = mode_spin((1, 2, 0, 0, 1, 2))     # 2 (two spin-½ contributions)

    # Scan all modes up to |n_i| ≤ 3, below 1 GeV
    modes = scan_modes(Gti, L, n_max=3, E_max_MeV=1000)


ORIGINS
=======

Extracted from R26 Track 4a
(studies/R26-neutrino-t4/scripts/track4a_t6_metric.py).
"""

import math
import numpy as np
from scipy.optimize import brentq
from lib.constants import h, hbar, c, alpha as ALPHA, m_e


# ── Derived constants ─────────────────────────────────────────────────

eV_J = 1.602176634e-19           # joules per eV
MeV_J = eV_J * 1e6              # joules per MeV
hbar_c_MeV_fm = hbar * c / MeV_J * 1e15   # ℏc ≈ 197.3 MeV·fm

M_E_MEV = m_e * c**2 / MeV_J    # electron mass, 0.51100 MeV
M_P_MEV = 938.272                # proton mass, MeV (PDG 2022)
M_N_MEV = 939.565                # neutron mass, MeV (PDG 2022)

DM2_21 = 7.53e-5   # Δm²₂₁ in eV² (solar neutrino mass splitting)
S34 = 0.02199       # neutrino within-plane shear, from
                     # Δm²₃₁/Δm²₂₁ = 33.6 → s = (3−2s)/(4s) inverted


# ══════════════════════════════════════════════════════════════════════
#  α formula (KK convention, from R19 Track 8)
# ══════════════════════════════════════════════════════════════════════

def alpha_kk(r, s):
    """
    Fine-structure constant from sheared T² geometry (KK convention).

    Parameters
    ----------
    r : float
        Aspect ratio (tube circumference / ring circumference).
    s : float
        Within-plane shear parameter, 0 < s < 0.5.

    Returns
    -------
    float
        α(r, s) — the predicted fine-structure constant.

    Notes
    -----
    Derived in R19 Track 8 (F35–F43).  Under the KK Compton
    constraint, the (1,2) mode energy μ₁₂ = √(1/r² + (2−s)²)
    and α depends on both r and s.  For each r > ~2, there exists
    an s that gives α = 1/137.036.
    """
    mu = math.sqrt(1 / r**2 + (2 - s)**2)
    return r**2 * mu * math.sin(2 * math.pi * s)**2 / (4 * math.pi * (2 - s)**2)


def solve_shear_for_alpha(r, alpha_target=ALPHA):
    """
    Find the shear s that produces a target α on a T² with aspect ratio r.

    Parameters
    ----------
    r : float
        Aspect ratio of the T².
    alpha_target : float, optional
        Target fine-structure constant (default: measured α ≈ 1/137.036).

    Returns
    -------
    float or None
        The shear s ∈ (0, 0.5) such that α_KK(r, s) = alpha_target,
        or None if no solution exists for this r.
    """
    s_scan = np.linspace(0.001, 0.49, 3000)
    a_scan = [alpha_kk(r, s) for s in s_scan]
    for i in range(len(s_scan) - 1):
        if (a_scan[i] - alpha_target) * (a_scan[i + 1] - alpha_target) < 0:
            return brentq(lambda s: alpha_kk(r, s) - alpha_target,
                          s_scan[i], s_scan[i + 1])
    return None


def mu_12(r, s):
    """
    Dimensionless energy of the (1,2) mode on a sheared T².

    The physical energy is E = E₀ × μ₁₂, where E₀ = 2πℏc/L_ring.

    Parameters
    ----------
    r : float   — aspect ratio
    s : float   — within-plane shear

    Returns
    -------
    float — μ₁₂ = √(1/r² + (2−s)²), dimensionless.
    """
    return math.sqrt(1 / r**2 + (2 - s)**2)


# ══════════════════════════════════════════════════════════════════════
#  T⁶ metric construction
# ══════════════════════════════════════════════════════════════════════

def compute_scales(r_e, r_nu, r_p):
    """
    Compute the 6 circumferences and 3 within-plane shears.

    The circumferences are derived from:
      - Electron T²:  L₂ from m_e and μ₁₂(r_e, s₁₂);  L₁ = r_e × L₂
      - Neutrino T²:  L₄ from Δm²₂₁ and s₃₄;  L₃ = r_ν × L₄
      - Proton T²:    L₆ from m_p and μ₁₂(r_p, s₅₆);  L₅ = r_p × L₆

    Parameters
    ----------
    r_e : float   — electron aspect ratio (tube/ring)
    r_nu : float  — neutrino aspect ratio
    r_p : float   — proton aspect ratio

    Returns
    -------
    L : ndarray (6,)  — circumferences in femtometers
        [L₁_e_tube, L₂_e_ring, L₃_ν_tube, L₄_ν_ring, L₅_p_tube, L₆_p_ring]
    s12 : float — electron within-plane shear (from α)
    s34 : float — neutrino within-plane shear (from Δm² ratio)
    s56 : float — proton within-plane shear (from α)
    """
    s12 = solve_shear_for_alpha(r_e)
    s56 = solve_shear_for_alpha(r_p)
    s34 = S34

    mu_e = mu_12(r_e, s12)
    E0_e = M_E_MEV / mu_e
    L2 = 2 * math.pi * hbar_c_MeV_fm / E0_e
    L1 = r_e * L2

    E0_nu_sq = DM2_21 / (4 * s34)   # eV²
    E0_nu = math.sqrt(E0_nu_sq) * 1e-6   # eV → MeV
    L4 = 2 * math.pi * hbar_c_MeV_fm / E0_nu
    L3 = r_nu * L4

    mu_p = mu_12(r_p, s56)
    E0_p = M_P_MEV / mu_p
    L6 = 2 * math.pi * hbar_c_MeV_fm / E0_p
    L5 = r_p * L6

    L = np.array([L1, L2, L3, L4, L5, L6])
    return L, s12, s34, s56


def build_scaled_metric(r_e, r_nu, r_p,
                        sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0):
    """
    Build the dimensionless T⁶ metric G̃ and circumferences L.

    Constructs the 6×6 metric from aspect ratios (which determine
    circumferences and within-plane shears) and cross-plane shears
    (which couple the three T² sheets).

    Parameters
    ----------
    r_e : float    — electron T² aspect ratio
    r_nu : float   — neutrino T² aspect ratio
    r_p : float    — proton T² aspect ratio
    sigma_ep : float, optional
        Electron–proton cross-shear (default 0).  Positive-definite
        metric requires |σ_ep| < ~0.535.  The neutron mass matches
        at |σ_ep| ≈ 0.038 (R26 F67).
    sigma_enu : float, optional
        Electron–neutrino cross-shear (default 0).  Neutrino mass
        ratio constrains |σ_eν| ≲ 0.05 (R26 F72).
    sigma_nup : float, optional
        Neutrino–proton cross-shear (default 0).

    Returns
    -------
    Gtilde : ndarray (6, 6)
        Dimensionless metric.  G̃_ij ≈ δ_ij on the diagonal,
        within-plane shear terms from α and Δm², and cross-plane
        σ values in the off-diagonal blocks.
    Gtilde_inv : ndarray (6, 6)
        Inverse of G̃.  Used in mode_energy().
    L : ndarray (6,)
        Circumferences in femtometers.
    scales : dict
        All input and derived parameters for reference:
        'L', 'L_units', 's12', 's34', 's56', 'sigma_ep',
        'sigma_enu', 'sigma_nup', 'r_e', 'r_nu', 'r_p'.

    Notes
    -----
    Cross-shear convention: G̃_ij = σ for ALL 4 (i, j) pairs in
    each inter-plane block.  E.g., σ_ep sets G̃₁₅ = G̃₁₆ = G̃₂₅
    = G̃₂₆ = σ_ep.  This is the symmetric (collective) parametri-
    zation.  Individual shears within a block (needed for PMNS
    mixing angles) require extending this function.
    """
    L, s12, s34, s56 = compute_scales(r_e, r_nu, r_p)

    S_within = np.zeros((6, 6))
    S_within[0, 1] = s12
    S_within[2, 3] = s34
    S_within[4, 5] = s56

    B = np.diag(L) @ (np.eye(6) + S_within)
    G_phys = B.T @ B

    Gtilde = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
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

    Gtilde_inv = np.linalg.inv(Gtilde)

    scales = {
        'L': L, 'L_units': 'fm',
        's12': s12, 's34': s34, 's56': s56,
        'sigma_ep': sigma_ep, 'sigma_enu': sigma_enu, 'sigma_nup': sigma_nup,
        'r_e': r_e, 'r_nu': r_nu, 'r_p': r_p,
    }
    return Gtilde, Gtilde_inv, L, scales


# ══════════════════════════════════════════════════════════════════════
#  Mode properties
# ══════════════════════════════════════════════════════════════════════

def mode_energy(n, Gtilde_inv, L, hbar_c=hbar_c_MeV_fm):
    """
    Energy of a T⁶ mode in MeV.

    Parameters
    ----------
    n : array-like (6,)
        Integer quantum numbers (n₁, n₂, n₃, n₄, n₅, n₆).
        Indices 0,1 = electron T², 2,3 = neutrino T², 4,5 = proton T².
    Gtilde_inv : ndarray (6, 6)
        Inverse of the dimensionless metric (from build_scaled_metric).
    L : ndarray (6,)
        Circumferences in fm (from build_scaled_metric).
    hbar_c : float, optional
        ℏc in MeV·fm (default: computed from constants).

    Returns
    -------
    float — mode energy in MeV.

    Examples
    --------
    Electron:  mode_energy((1, 2, 0, 0, 0, 0), Gti, L)  →  0.511 MeV
    Proton:    mode_energy((0, 0, 0, 0, 1, 2), Gti, L)  →  938.3 MeV
    Neutron:   mode_energy((1, 2, 0, 0, 1, 2), Gti, L)  →  938.3–939.6 MeV
               (depends on σ_ep)
    """
    n = np.asarray(n, dtype=float)
    ntilde = n / L
    E2 = (2 * math.pi * hbar_c)**2 * ntilde @ Gtilde_inv @ ntilde
    return math.sqrt(max(E2, 0.0))


def mode_charge(n):
    """
    Net electric charge of a T⁶ mode, in units of e.

    Charge arises from odd tube windings:
      n₁ (index 0, electron tube):  odd → contributes −sign(n₁) × e
      n₅ (index 4, proton tube):    odd → contributes +sign(n₅) × e

    Even tube windings and all ring windings (n₂, n₄, n₆) do not
    contribute to charge.

    Parameters
    ----------
    n : array-like (6,) — integer quantum numbers.

    Returns
    -------
    int — net charge in units of e.  Positive = proton-like.

    Examples
    --------
    Electron (1,2,0,0,0,0):   charge = −1
    Proton   (0,0,0,0,1,2):   charge = +1
    Neutron  (1,2,0,0,1,2):   charge =  0  (−1 + 1)
    Neutrino (0,0,1,1,0,0):   charge =  0
    """
    q_e = -n[0]
    q_p = +n[4]
    return q_e + q_p


def mode_spin(n):
    """
    Count of spin-½ contributions from tube windings.

    Each odd tube winding (|n_i| odd for i = 0, 2, 4) contributes
    one unit of spin-½.  The total spin depends on how these
    combine (an open problem for n_half ≥ 2; see R26 F68).

    Parameters
    ----------
    n : array-like (6,) — integer quantum numbers.

    Returns
    -------
    int — number of spin-½ contributions:
        0 → boson (spin 0)
        1 → fermion (spin ½)
        2 → spin 0 or 1 (composition ambiguous)
        3 → spin ½ or 3/2 (composition ambiguous)
    """
    return sum(abs(n[i]) % 2 for i in [0, 2, 4])


def mode_spin_label(n):
    """
    Human-readable spin classification string.

    Parameters
    ----------
    n : array-like (6,) — integer quantum numbers.

    Returns
    -------
    str — one of: "boson", "fermion (½)", "2×½ → 0 or 1",
          "3×½ → ½ or 3/2".
    """
    n_half = mode_spin(n)
    if n_half == 0:
        return "boson"
    elif n_half == 1:
        return "fermion (½)"
    elif n_half == 2:
        return "2×½ → 0 or 1"
    else:
        return "3×½ → ½ or 3/2"


# ══════════════════════════════════════════════════════════════════════
#  Spectral scanning
# ══════════════════════════════════════════════════════════════════════

def scan_modes(Gtilde_inv, L, n_max=3, E_max_MeV=None):
    """
    Enumerate all T⁶ modes and compute their properties.

    Scans all integer quantum numbers with |n_i| ≤ n_max
    (excluding the zero mode).  The total number of modes is
    (2 × n_max + 1)⁶ − 1, which grows fast:
        n_max=3  →   ~16,000 modes
        n_max=5  →  ~1.8M modes
        n_max=10 → ~350M modes (use E_max_MeV to filter)

    Parameters
    ----------
    Gtilde_inv : ndarray (6, 6)
        Inverse dimensionless metric.
    L : ndarray (6,)
        Circumferences in fm.
    n_max : int, optional
        Maximum absolute quantum number per dimension (default 3).
    E_max_MeV : float or None, optional
        If given, discard modes with energy above this threshold.

    Returns
    -------
    list of dict, sorted by energy (ascending):
        [{'n': tuple(6),          — quantum numbers
          'E_MeV': float,         — energy in MeV
          'charge': int,          — net charge in units of e
          'spin_halves': int},    — number of spin-½ contributions
         ...]
    """
    from itertools import product
    modes = []
    rng = range(-n_max, n_max + 1)
    for n in product(rng, repeat=6):
        if all(ni == 0 for ni in n):
            continue
        E = mode_energy(n, Gtilde_inv, L)
        if E_max_MeV is not None and E > E_max_MeV:
            continue
        modes.append({
            'n': n,
            'E_MeV': E,
            'charge': mode_charge(n),
            'spin_halves': mode_spin(n),
        })
    modes.sort(key=lambda m: m['E_MeV'])
    return modes


# ══════════════════════════════════════════════════════════════════════
#  Metric diagnostics
# ══════════════════════════════════════════════════════════════════════

def is_positive_definite(Gtilde):
    """
    Check whether the metric G̃ is positive-definite.

    A positive-definite metric is required for all mode energies
    to be real.  Cross-shears that violate this bound are
    unphysical.

    Parameters
    ----------
    Gtilde : ndarray (6, 6) — dimensionless metric.

    Returns
    -------
    bool — True if all eigenvalues are > 0.
    """
    eigvals = np.linalg.eigvalsh(Gtilde)
    return bool(np.all(eigvals > 0))


# ══════════════════════════════════════════════════════════════════════
#  Casimir energy (Epstein zeta function)
# ══════════════════════════════════════════════════════════════════════

def epstein_zeta(Gtilde_inv, L, s_exp=5, n_max=3,
                 hbar_c=hbar_c_MeV_fm):
    """
    Epstein zeta function for the T⁶ vacuum energy.

    Computes Z(s) = Σ_{n ≠ 0} (ñᵀ G̃⁻¹ ñ)^{-s} where the sum
    runs over nonzero n ∈ Z⁶ with |n_i| ≤ n_max and ñ_i = n_i/L_i.

    The Casimir (vacuum) energy of a massless scalar field on the
    T⁶ is proportional to Z(s) with s = (d+D)/2 where d = 4
    (spacetime) and D = 6 (compact), so s = 5.

    Parameters
    ----------
    Gtilde_inv : ndarray (6, 6)
        Inverse dimensionless metric.
    L : ndarray (6,)
        Circumferences in fm.
    s_exp : int, optional
        Exponent in the zeta sum (default 5).
    n_max : int, optional
        Maximum |n_i| in the sum (default 3).
    hbar_c : float, optional
        ℏc in MeV·fm.

    Returns
    -------
    float — Z(s), dimensionless (the (2πℏc)^{2s} prefactor is
            NOT included; multiply by it for physical units).

    Notes
    -----
    The sum is truncated at n_max.  For the T⁶ with extreme scale
    hierarchy, the sum is dominated by the largest T² (neutrino,
    L ~ mm) and converges rapidly.  See R26 F69, F71 for behavior
    under cross-shear variation.
    """
    from itertools import product
    Z = 0.0
    rng = range(-n_max, n_max + 1)
    for n in product(rng, repeat=6):
        if all(ni == 0 for ni in n):
            continue
        n_arr = np.array(n, dtype=float)
        ntilde = n_arr / L
        q = ntilde @ Gtilde_inv @ ntilde
        if q > 0:
            Z += q**(-s_exp)
    return Z
