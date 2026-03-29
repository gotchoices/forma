"""
Ma model engine — next-generation replacement for ma.py.

Provides an immutable ``Ma`` class that holds the full geometry state
(aspect ratios, shears, circumferences, metric) and exposes mode
energy, charge, spin, scanning, and serialization.

See ``ma-model.md`` for the design spec.

No dependency on legacy ma.py — all physics reimplemented from first
principles using the same formulas.  Validated by running the same
regression tests as the legacy code.


PHYSICAL PICTURE
================

Three flat material sheets Ma_e, Ma_ν, Ma_p (electron, neutrino,
proton) form a 6-torus Ma.  Each particle is a standing wave (mode)
characterized by six integer quantum numbers n = (n₁, ..., n₆).

The six dimensions are organized in three pairs:

    Indices 0, 1  →  Ma_e  (θ₁ = tube, θ₂ = ring)
    Indices 2, 3  →  Ma_ν  (θ₃ = tube, θ₄ = ring)
    Indices 4, 5  →  Ma_p  (θ₅ = tube, θ₆ = ring)

Tube directions have even indices (0, 2, 4).  Ring directions have
odd indices (1, 3, 5).  Charge and spin are determined by tube
windings.


TYPICAL USAGE
=============

    from lib.ma_model import Ma

    # r_p = 8.906 and σ_ep = -0.0906 are pinned by R27 (neutron + muon).
    # r_e and r_nu are FREE — values below are starting guesses.
    # R37 F7 prefers r_e ≈ 0.5 (energy minimization); 6.6 is historical.
    m = Ma(r_e=0.5, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906)
    m.energy((1, 2, 0, 0, 0, 0))       # electron energy (MeV)
    m.charge((1, 2, 0, 0, 0, 0))       # -1
    m.L                                  # circumferences (fm)

    # Self-consistent (m_e, m_p exact):
    m = Ma(r_e=0.5, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906,
           self_consistent=True)

    # Parameter sweep:
    m2 = m.with_params(sigma_ep=-0.10)

    # Brute-force scan (same as legacy; Fincke-Pohst planned):
    modes = m.scan_modes(n_max=3, E_max_MeV=1000)

    # Serialization:
    d = m.to_dict()
    m3 = Ma.from_dict(d)
"""

import math
from collections import namedtuple
from itertools import product as iproduct

import numpy as np
from scipy.optimize import brentq

from lib.constants import (
    h, hbar, c, e as _eV_J, alpha as ALPHA, m_e,
)

# ── Derived constants ─────────────────────────────────────────────

_MeV_J = _eV_J * 1e6
_hbar_c_MeV_fm = hbar * c / _MeV_J * 1e15    # ≈ 197.3 MeV·fm

M_E_MEV = m_e * c**2 / _MeV_J                 # electron mass (MeV)
M_P_MEV = 938.272                              # proton mass (PDG 2022)
M_N_MEV = 939.565                              # neutron mass (PDG 2022)

DM2_21 = 7.53e-5    # Δm²₂₁ in eV² (solar neutrino mass splitting)
S34_DEFAULT = 0.02199   # neutrino within-plane shear from Δm² ratio

# Sheet index map: name → (tube_index, ring_index)
_SHEET_INDICES = {'e': (0, 1), 'nu': (2, 3), 'p': (4, 5)}

# Cross-block index pairs
_CROSS_BLOCKS = {
    'ep':  [(0, 4), (0, 5), (1, 4), (1, 5)],
    'enu': [(0, 2), (0, 3), (1, 2), (1, 3)],
    'nup': [(2, 4), (2, 5), (3, 4), (3, 5)],
}

# Reference modes for self-consistency
_N_ELECTRON = np.array([1, 2, 0, 0, 0, 0], dtype=float)
_N_PROTON = np.array([0, 0, 0, 0, 1, 2], dtype=float)

# Mode namedtuple for scan results
Mode = namedtuple('Mode', ['n', 'E_MeV', 'charge', 'spin_halves', 'delta_E_MeV'])
Mode.__new__.__defaults__ = (None,)

# Energy decomposition result
EnergyDecomp = namedtuple('EnergyDecomp', [
    'total',       # float — total energy (MeV)
    'e_sheet',     # float — E² contribution from electron block (MeV²)
    'nu_sheet',    # float — E² contribution from neutrino block (MeV²)
    'p_sheet',     # float — E² contribution from proton block (MeV²)
    'ep_cross',    # float — E² from electron-proton cross block (MeV²)
    'enu_cross',   # float — E² from electron-neutrino cross block (MeV²)
    'nup_cross',   # float — E² from neutrino-proton cross block (MeV²)
    'fractions',   # dict — fractional contributions to E²
])


# Pressure harmonics result (per-sheet, per-mode)
PressureHarmonics = namedtuple('PressureHarmonics', [
    'c_k',        # ndarray — Fourier amplitudes |c_k| for k=0..n_harm
    'delta_r_k',  # ndarray — wall deformation δr_k/a per harmonic
    'phi_k',      # ndarray — phases atan2(B_k, A_k)
    'A_k',        # ndarray — cosine Fourier coefficients
    'B_k',        # ndarray — sine Fourier coefficients
])

# Wall cross-section shape
WallShape = namedtuple('WallShape', [
    'theta',        # ndarray (N,) — tube angles [0, 2π)
    'r_over_a',     # ndarray (N,) — wall radius / tube radius
    'eccentricity', # float — (max-min)/(max+min)
])

# Dynamic correction for a 6D mode
DynamicCorrection = namedtuple('DynamicCorrection', [
    'delta_E_over_E',  # float — total δE/E (weighted across sheets)
    'per_sheet',       # dict: 'e'→float, 'nu'→float, 'p'→float
    'dominant_k',      # int — coupling harmonic on dominant sheet
    'filter_factor',   # float — suppression vs (1,2) fundamental
])

# Target for inverse solver
Target = namedtuple('Target', ['n', 'mass_MeV'])

# Fit result
FitResult = namedtuple('FitResult', [
    'params',       # dict — optimal parameter values
    'residuals',    # ndarray — (E_computed − E_target) for each target (MeV)
    'ma',           # Ma — instance at the optimal point
    'jacobian',     # ndarray (n_targets, n_params) — Jacobian at solution
    'cov',          # ndarray or None — parameter covariance (None if underdetermined)
    'null_space',   # ndarray or None — null-space columns (None if fully determined)
    'converged',    # bool
    'iterations',   # int
])


# ══════════════════════════════════════════════════════════════════════
#  Alpha formula (R19 Track 8)
# ══════════════════════════════════════════════════════════════════════

def alpha_ma(r, s):
    """
    Fine-structure constant from sheared material sheet geometry.

    α(r, s) = r² μ sin²(2πs) / (4π(2−s)²)

    where μ = √(1/r² + (2−s)²) is the dimensionless (1,2) mode energy.

    Parameters
    ----------
    r : float — aspect ratio (tube/ring circumference)
    s : float — within-plane shear, 0 < s < 0.5

    Returns
    -------
    float — predicted fine-structure constant

    Notes
    -----
    Derived in R19 Track 8 (F35-F43).  For each r > ~0.25 there
    exists an s giving α = 1/137.036.
    """
    mu = math.sqrt(1 / r**2 + (2 - s)**2)
    return r**2 * mu * math.sin(2 * math.pi * s)**2 / (4 * math.pi * (2 - s)**2)


def solve_shear_for_alpha(r, alpha_target=ALPHA):
    """
    Find the shear s that produces a target α for a given aspect ratio r.

    Parameters
    ----------
    r : float — aspect ratio
    alpha_target : float — target α (default: measured α ≈ 1/137.036)

    Returns
    -------
    float or None — shear s ∈ (0, 0.5), or None if no solution exists.
    """
    s_scan = np.linspace(0.001, 0.49, 3000)
    a_scan = np.array([alpha_ma(r, s) for s in s_scan])
    for i in range(len(s_scan) - 1):
        if (a_scan[i] - alpha_target) * (a_scan[i + 1] - alpha_target) < 0:
            return brentq(lambda s: alpha_ma(r, s) - alpha_target,
                          s_scan[i], s_scan[i + 1])
    return None


def mu_12(r, s):
    """
    Dimensionless energy of the (1,2) mode: μ₁₂ = √(1/r² + (2−s)²).

    The physical energy is E = E₀ × μ₁₂ where E₀ = 2πℏc / L_ring.
    """
    return math.sqrt(1 / r**2 + (2 - s)**2)


def _dalpha_dr(r, s):
    """
    Partial derivative ∂α/∂r at fixed s.

    α = r² μ sin²(2πs) / (4π(2−s)²)  where μ = √(1/r² + (2−s)²).
    Let C = sin²(2πs) / (4π(2−s)²)  (s-dependent constant).
    α = r² μ C.
    ∂α/∂r = C × (2r μ + r² ∂μ/∂r)
    ∂μ/∂r = (1/μ) × (−1/r³)
    """
    mu = math.sqrt(1 / r**2 + (2 - s)**2)
    C = math.sin(2 * math.pi * s)**2 / (4 * math.pi * (2 - s)**2)
    dmu_dr = -1 / (r**3 * mu)
    return C * (2 * r * mu + r**2 * dmu_dr)


def _dalpha_ds(r, s):
    """
    Partial derivative ∂α/∂s at fixed r.

    α = r² μ sin²(2πs) / (4π(2−s)²)  where μ = √(1/r² + (2−s)²).
    Use the product rule on three s-dependent factors: μ, sin², (2−s)⁻².
    """
    mu = math.sqrt(1 / r**2 + (2 - s)**2)
    sin2 = math.sin(2 * math.pi * s)**2
    q = 2 - s
    # ∂μ/∂s = (1/μ) × (2−s) × (−1) = −(2−s)/μ
    dmu_ds = -q / mu
    # ∂(sin²(2πs))/∂s = 2 sin(2πs) cos(2πs) × 2π = 2π sin(4πs)
    dsin2_ds = 2 * math.pi * math.sin(4 * math.pi * s)
    # ∂((2−s)⁻²)/∂s = 2(2−s)⁻³
    # But we have (2−s)² in denominator, so factor = 1/(4π(2−s)²)
    # d/ds [sin²/(4π q²)] = (1/4π) × [dsin2/ds × q⁻² + sin² × 2q⁻³]

    pref = r**2 / (4 * math.pi)
    # α = pref × μ × sin² / q²
    # ∂α/∂s = pref × [dmu/ds × sin²/q² + μ × dsin2/ds / q² + μ × sin² × 2/q³]
    return pref * (dmu_ds * sin2 / q**2
                   + mu * dsin2_ds / q**2
                   + mu * sin2 * 2 / q**3)


# ══════════════════════════════════════════════════════════════════════
#  Dynamic model: pressure harmonics (R40 Track 11)
# ══════════════════════════════════════════════════════════════════════

_N_HARM_DEFAULT = 8
_N_SAMPLES_DEFAULT = 4000
_N_WALL_PTS = 360

def _compute_pressure_harmonics(n_tube, n_ring, r,
                                n_samples=_N_SAMPLES_DEFAULT,
                                n_harm=_N_HARM_DEFAULT):
    """
    Speed-weighted pressure harmonics for mode (n_tube, n_ring) on a
    torus with aspect ratio r = a/R.

    Uses the flat-torus geodesic (θ₁ = n₁ t, θ₂ = n₂ t) projected onto
    the 3D embedding.  The Clairaut geodesic does not exist for a/R > 1
    (R40 F19-F22); the flat-torus path is physically correct.

    Returns PressureHarmonics namedtuple.  Harmonics depend only on
    (|n_tube|, |n_ring|, r), not on absolute scale or sign.
    """
    zeros = np.zeros(n_harm + 1)
    null = PressureHarmonics(c_k=zeros.copy(), delta_r_k=zeros.copy(),
                             phi_k=zeros.copy(), A_k=zeros.copy(),
                             B_k=zeros.copy())
    n1 = abs(n_tube)
    n2 = abs(n_ring)
    if n1 == 0 or n2 == 0:
        return null

    R_val = 1.0
    a_val = r

    N = n_samples
    t = np.linspace(0, 2 * math.pi, N, endpoint=False)
    dt = t[1] - t[0]

    theta1 = n1 * t
    theta2 = n2 * t
    rho = R_val + a_val * np.cos(theta1)

    x = rho * np.cos(theta2)
    y = rho * np.sin(theta2)
    z = a_val * np.sin(theta1)

    dx = (-n1 * a_val * np.sin(theta1) * np.cos(theta2)
          - n2 * rho * np.sin(theta2))
    dy = (-n1 * a_val * np.sin(theta1) * np.sin(theta2)
          + n2 * rho * np.cos(theta2))
    dz = n1 * a_val * np.cos(theta1)
    speed = np.sqrt(dx**2 + dy**2 + dz**2)

    T_hat = np.stack([dx, dy, dz], axis=-1) / speed[:, None]

    dT = np.zeros_like(T_hat)
    for j in range(3):
        dT[:, j] = np.gradient(T_hat[:, j], dt)
    kappa_vec = dT / speed[:, None]

    e_r = np.stack([
        np.cos(theta1) * np.cos(theta2),
        np.cos(theta1) * np.sin(theta2),
        np.sin(theta1),
    ], axis=-1)

    kappa_radial_raw = np.sum(kappa_vec * e_r, axis=1)
    kappa_outward = -kappa_radial_raw

    N_BINS = 256
    theta1_bins = np.linspace(0, 2 * math.pi, N_BINS, endpoint=False)
    kout_speed_binned = np.zeros(N_BINS)
    counts = np.zeros(N_BINS)

    theta1_mod = theta1 % (2 * math.pi)
    for i in range(N):
        idx = int(theta1_mod[i] / (2 * math.pi) * N_BINS) % N_BINS
        kout_speed_binned[idx] += kappa_outward[i] * speed[i]
        counts[idx] += 1

    mask = counts > 0
    kout_speed_binned[mask] /= counts[mask]

    th = theta1_bins[mask]
    signal = kout_speed_binned[mask]

    A_k = np.zeros(n_harm + 1)
    B_k = np.zeros(n_harm + 1)
    A_k[0] = np.mean(signal)
    for k in range(1, n_harm + 1):
        A_k[k] = 2 * np.mean(signal * np.cos(k * th))
        B_k[k] = 2 * np.mean(signal * np.sin(k * th))

    c0 = abs(A_k[0])
    c_k = np.zeros(n_harm + 1)
    c_k[0] = c0
    phi_k = np.zeros(n_harm + 1)
    delta_r_k = np.zeros(n_harm + 1)

    for k in range(1, n_harm + 1):
        c_k[k] = math.sqrt(A_k[k]**2 + B_k[k]**2)
        phi_k[k] = math.atan2(B_k[k], A_k[k])
        if c0 > 0:
            delta_r_k[k] = ALPHA * (c_k[k] / c0) / k**2

    return PressureHarmonics(c_k=c_k, delta_r_k=delta_r_k,
                             phi_k=phi_k, A_k=A_k, B_k=B_k)


def _compute_wall_shape(harm):
    """Reconstruct the wall cross-section from pressure harmonics."""
    theta = np.linspace(0, 2 * math.pi, _N_WALL_PTS, endpoint=False)
    r_wall = np.ones_like(theta)
    for k in range(1, len(harm.delta_r_k)):
        r_wall += harm.delta_r_k[k] * np.cos(k * theta - harm.phi_k[k])
    rmin, rmax = r_wall.min(), r_wall.max()
    ecc = (rmax - rmin) / (rmax + rmin) if (rmax + rmin) > 0 else 0.0
    return WallShape(theta=theta, r_over_a=r_wall, eccentricity=ecc)


# ══════════════════════════════════════════════════════════════════════
#  Metric construction (internal)
# ══════════════════════════════════════════════════════════════════════

def _compute_scales(r_e, r_nu, r_p):
    """
    Derive the 6 circumferences and 3 within-plane shears from
    aspect ratios.

    Returns (L, s12, s34, s56) where L is ndarray(6,) in fm.

    Raises ValueError if no shear solution exists for r_e or r_p.
    """
    s12 = solve_shear_for_alpha(r_e)
    if s12 is None:
        raise ValueError(f"No shear solution for r_e = {r_e} (need r > ~0.25)")
    s56 = solve_shear_for_alpha(r_p)
    if s56 is None:
        raise ValueError(f"No shear solution for r_p = {r_p} (need r > ~0.25)")
    s34 = S34_DEFAULT

    # Electron sheet
    mu_e = mu_12(r_e, s12)
    E0_e = M_E_MEV / mu_e
    L2 = 2 * math.pi * _hbar_c_MeV_fm / E0_e
    L1 = r_e * L2

    # Neutrino sheet
    E0_nu_sq = DM2_21 / (4 * s34)        # eV²
    E0_nu = math.sqrt(E0_nu_sq) * 1e-6   # eV → MeV
    L4 = 2 * math.pi * _hbar_c_MeV_fm / E0_nu
    L3 = r_nu * L4

    # Proton sheet
    mu_p = mu_12(r_p, s56)
    E0_p = M_P_MEV / mu_p
    L6 = 2 * math.pi * _hbar_c_MeV_fm / E0_p
    L5 = r_p * L6

    L = np.array([L1, L2, L3, L4, L5, L6])
    return L, s12, s34, s56


def _build_metric(L, s12, s34, s56, cross_shears):
    """
    Build the dimensionless metric G̃ and its inverse.

    Within-plane shears enter through the lattice matrix B = diag(L)(I + S).
    Cross-plane shears are injected directly into the off-diagonal blocks
    of G̃.

    Parameters
    ----------
    L : ndarray(6,) — circumferences in fm
    s12, s34, s56 : float — within-plane shears
    cross_shears : dict — maps block name ('ep', 'enu', 'nup') to float,
                   OR maps (i,j) tuples to individual float values.

    Returns
    -------
    (Gt, Gti) — dimensionless metric and its inverse, or
    (None, None) if the metric is not positive-definite.
    """
    # Within-plane shear matrix (upper triangular)
    S = np.zeros((6, 6))
    S[0, 1] = s12
    S[2, 3] = s34
    S[4, 5] = s56

    # Lattice matrix and physical metric
    B = np.diag(L) @ (np.eye(6) + S)
    G_phys = B.T @ B

    # Scale to dimensionless metric
    Gt = np.empty((6, 6))
    for i in range(6):
        for j in range(6):
            Gt[i, j] = G_phys[i, j] / (L[i] * L[j])

    # Inject cross-shears
    for key, val in cross_shears.items():
        if isinstance(key, str):
            # Block name: set all 4 entries
            for i, j in _CROSS_BLOCKS[key]:
                Gt[i, j] = val
                Gt[j, i] = val
        else:
            # Individual (i, j) pair
            i, j = key
            Gt[i, j] = val
            Gt[j, i] = val

    # Positive-definite check
    eigvals = np.linalg.eigvalsh(Gt)
    if np.any(eigvals <= 0):
        return None, None

    Gti = np.linalg.inv(Gt)
    return Gt, Gti


def _self_consistent_iteration(L, r_e, r_nu, r_p, s12, s34, s56,
                                cross_shears, tol=1e-12, max_iter=50):
    """
    Iteratively adjust L so that E(electron) = m_e and E(proton) = m_p.

    Returns (Gt, Gti, L, converged, iterations).
    """
    L = L.copy()
    for iteration in range(max_iter):
        Gt, Gti = _build_metric(L, s12, s34, s56, cross_shears)
        if Gt is None:
            return None, None, L, False, iteration

        E_e = _mode_energy(_N_ELECTRON, Gti, L)
        E_p = _mode_energy(_N_PROTON, Gti, L)

        err_e = abs(E_e - M_E_MEV) / M_E_MEV
        err_p = abs(E_p - M_P_MEV) / M_P_MEV

        if err_e < tol and err_p < tol:
            return Gt, Gti, L, True, iteration + 1

        # Fixed-point rescaling: E ∝ 1/L, so L *= E/M_target
        L[1] *= E_e / M_E_MEV
        L[0] = r_e * L[1]
        L[5] *= E_p / M_P_MEV
        L[4] = r_p * L[5]

    return Gt, Gti, L, False, max_iter


# ══════════════════════════════════════════════════════════════════════
#  Mode property functions (internal, no state)
# ══════════════════════════════════════════════════════════════════════

def _mode_energy(n, Gti, L):
    """Mode energy in MeV from the quadratic form on G̃⁻¹."""
    n = np.asarray(n, dtype=float)
    ntilde = n / L
    E2 = (2 * math.pi * _hbar_c_MeV_fm)**2 * ntilde @ Gti @ ntilde
    if E2 < 0:
        raise ValueError(
            f"Negative E² = {E2:.4e} for mode {tuple(n.astype(int))}. "
            "Check that the metric is positive-definite.")
    return math.sqrt(E2)


def _mode_charge(n):
    """Electric charge Q = −n₁ + n₅ (KK compact momentum)."""
    return int(-n[0] + n[4])


def _mode_spin(n):
    """Count of spin-½ contributions from odd tube windings."""
    return sum(abs(n[i]) % 2 for i in (0, 2, 4))


def _mode_spin_label(n):
    """Human-readable spin classification."""
    s = _mode_spin(n)
    if s == 0:
        return "boson"
    elif s == 1:
        return "fermion (½)"
    elif s == 2:
        return "2×½ → 0 or 1"
    else:
        return "3×½ → ½ or 3/2"


# ══════════════════════════════════════════════════════════════════════
#  Ma class
# ══════════════════════════════════════════════════════════════════════

class Ma:
    """
    Immutable Ma geometry object.

    Holds all geometry state (aspect ratios, shears, circumferences,
    metric) and provides mode energy, charge, spin, scanning, and
    serialization.

    Construction computes and caches the metric and its inverse.
    To explore a different geometry, create a new Ma via
    ``with_params()`` or direct construction.

    Parameters
    ----------
    r_e : float — electron sheet aspect ratio (tube/ring)
    r_nu : float — neutrino sheet aspect ratio
    r_p : float — proton sheet aspect ratio
    sigma_ep : float — electron-proton cross-shear (default 0)
    sigma_enu : float — electron-neutrino cross-shear (default 0)
    sigma_nup : float — neutrino-proton cross-shear (default 0)
    cross_shears : dict or None — individual cross-shear entries
        as {(i,j): value} pairs.  Overrides sigma_ep/enu/nup for
        the specified entries.
    self_consistent : bool — if True, iterate L until E(electron)
        and E(proton) match their measured masses exactly.
    """

    __slots__ = (
        '_r_e', '_r_nu', '_r_p',
        '_s12', '_s34', '_s56',
        '_cross_shears',
        '_self_consistent', '_dynamic',
        '_L', '_Gt', '_Gti',
        '_converged', '_iterations',
        '_harm_cache',
    )

    def __init__(self, r_e, r_nu, r_p, *,
                 sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0,
                 cross_shears=None, self_consistent=False,
                 dynamic=False):
        self._r_e = float(r_e)
        self._r_nu = float(r_nu)
        self._r_p = float(r_p)
        self._self_consistent = bool(self_consistent)
        self._dynamic = bool(dynamic)
        self._harm_cache = {}

        # Compute circumferences and within-plane shears
        L, s12, s34, s56 = _compute_scales(r_e, r_nu, r_p)
        self._s12 = s12
        self._s34 = s34
        self._s56 = s56

        # Build cross-shear dict
        cs = {}
        if sigma_ep != 0.0:
            cs['ep'] = sigma_ep
        if sigma_enu != 0.0:
            cs['enu'] = sigma_enu
        if sigma_nup != 0.0:
            cs['nup'] = sigma_nup
        if cross_shears is not None:
            # Individual entries override block values
            cs.update(cross_shears)
        self._cross_shears = cs

        if self_consistent:
            Gt, Gti, L, conv, iters = _self_consistent_iteration(
                L, r_e, r_nu, r_p, s12, s34, s56, cs)
            self._converged = conv
            self._iterations = iters
        else:
            Gt, Gti = _build_metric(L, s12, s34, s56, cs)
            self._converged = None
            self._iterations = None

        if Gt is None:
            raise ValueError(
                "Metric is not positive-definite at the given parameters. "
                "Reduce cross-shear magnitudes.")

        self._L = L
        self._Gt = Gt
        self._Gti = Gti

    # ── Properties ────────────────────────────────────────────────

    @property
    def r_e(self):
        """Electron sheet aspect ratio."""
        return self._r_e

    @property
    def r_nu(self):
        """Neutrino sheet aspect ratio."""
        return self._r_nu

    @property
    def r_p(self):
        """Proton sheet aspect ratio."""
        return self._r_p

    @property
    def s12(self):
        """Electron within-plane shear (from α)."""
        return self._s12

    @property
    def s34(self):
        """Neutrino within-plane shear (from Δm² ratio)."""
        return self._s34

    @property
    def s56(self):
        """Proton within-plane shear (from α)."""
        return self._s56

    @property
    def sigma_ep(self):
        """Electron-proton cross-shear."""
        return self._cross_shears.get('ep', 0.0)

    @property
    def sigma_enu(self):
        """Electron-neutrino cross-shear."""
        return self._cross_shears.get('enu', 0.0)

    @property
    def sigma_nup(self):
        """Neutrino-proton cross-shear."""
        return self._cross_shears.get('nup', 0.0)

    @property
    def L(self):
        """Circumferences [L₁, L₂, L₃, L₄, L₅, L₆] in fm (read-only copy)."""
        return self._L.copy()

    @property
    def Gt(self):
        """Dimensionless metric G̃ (read-only copy)."""
        return self._Gt.copy()

    @property
    def Gti(self):
        """Inverse dimensionless metric G̃⁻¹ (read-only copy)."""
        return self._Gti.copy()

    @property
    def self_consistent(self):
        """Whether self-consistency iteration was requested."""
        return self._self_consistent

    @property
    def converged(self):
        """Whether self-consistency converged (None if not requested)."""
        return self._converged

    @property
    def iterations(self):
        """Number of self-consistency iterations (None if not requested)."""
        return self._iterations

    @property
    def dynamic(self):
        """Whether dynamic (α-impedance) corrections are enabled."""
        return self._dynamic

    @property
    def params(self):
        """Dict of all input parameters."""
        d = {
            'r_e': self._r_e, 'r_nu': self._r_nu, 'r_p': self._r_p,
            'sigma_ep': self.sigma_ep,
            'sigma_enu': self.sigma_enu,
            'sigma_nup': self.sigma_nup,
            'self_consistent': self._self_consistent,
            'dynamic': self._dynamic,
        }
        # Include any individual cross-shear entries
        for key, val in self._cross_shears.items():
            if isinstance(key, tuple):
                d[f'sigma_{key[0]}{key[1]}'] = val
        return d

    # ── Mode properties ───────────────────────────────────────────

    def energy(self, n):
        """
        Mode energy in MeV.

        When dynamic=True, returns the force-balance energy (via the
        perturbative shortcut E_static × (1 + δE/E)).  When
        dynamic=False (default), returns the flat-torus energy.

        Parameters
        ----------
        n : tuple or array-like (6,) — integer quantum numbers
            (n₁, n₂, n₃, n₄, n₅, n₆).

        Returns
        -------
        float — energy in MeV.
        """
        E_st = _mode_energy(n, self._Gti, self._L)
        if not self._dynamic:
            return E_st
        corr = self.dynamic_correction(n)
        return E_st * (1 + corr.delta_E_over_E)

    def energy_static(self, n):
        """
        Flat-torus mode energy in MeV (always, regardless of dynamic flag).

        Parameters
        ----------
        n : tuple or array-like (6,) — integer quantum numbers.

        Returns
        -------
        float — static energy in MeV.
        """
        return _mode_energy(n, self._Gti, self._L)

    def energy_decomp(self, n):
        """
        Decompose mode energy² into sheet and cross-coupling contributions.

        Partitions E² = (2πℏc)² ñᵀ G̃⁻¹ ñ into six terms using the
        block structure of G̃⁻¹:

            E² = E²_e + E²_ν + E²_p + 2·E²_eν + 2·E²_ep + 2·E²_νp

        where E²_e uses the (0:2, 0:2) block, E²_ep uses the (0:2, 4:6)
        block, etc.

        **Interpretation caveat:** These are blocks of the INVERSE metric,
        not the metric itself.  The Schur complement means [G̃⁻¹]_{ee}
        incorporates information from all sheets (it accounts for how
        the electron block is modified by cross-coupling to the other
        sheets).  So "95% proton-sheet" means "95% of E² comes from the
        proton block of G̃⁻¹," which is a well-defined mathematical
        statement but not identical to "the proton sheet alone contributes
        95% of the energy."  When cross-shears are small (|σ| < 0.1),
        the distinction is minor.

        Parameters
        ----------
        n : tuple or array-like (6,) — integer quantum numbers

        Returns
        -------
        EnergyDecomp namedtuple with fields:
            total (MeV), e_sheet (MeV²), nu_sheet (MeV²), p_sheet (MeV²),
            ep_cross (MeV²), enu_cross (MeV²), nup_cross (MeV²),
            fractions (dict)
        """
        n_arr = np.asarray(n, dtype=float)
        ntilde = n_arr / self._L
        prefactor = (2 * math.pi * _hbar_c_MeV_fm)**2
        Gti = self._Gti

        # Diagonal blocks: ñ_sheet^T [G̃⁻¹]_{sheet,sheet} ñ_sheet
        def block_E2(i_start, j_start, i_end, j_end):
            nt_i = ntilde[i_start:i_end]
            nt_j = ntilde[j_start:j_end]
            block = Gti[i_start:i_end, j_start:j_end]
            return float(prefactor * nt_i @ block @ nt_j)

        e_sheet  = block_E2(0, 0, 2, 2)
        nu_sheet = block_E2(2, 2, 4, 4)
        p_sheet  = block_E2(4, 4, 6, 6)

        # Cross blocks: ñ_i^T [G̃⁻¹]_{ij} ñ_j  (factor of 2 for symmetry)
        ep_cross  = 2 * block_E2(0, 4, 2, 6)
        enu_cross = 2 * block_E2(0, 2, 2, 4)
        nup_cross = 2 * block_E2(2, 4, 4, 6)

        E2_total = e_sheet + nu_sheet + p_sheet + ep_cross + enu_cross + nup_cross
        total = math.sqrt(max(E2_total, 0.0))

        fractions = {}
        if E2_total > 0:
            fractions = {
                'e': e_sheet / E2_total,
                'nu': nu_sheet / E2_total,
                'p': p_sheet / E2_total,
                'ep': ep_cross / E2_total,
                'enu': enu_cross / E2_total,
                'nup': nup_cross / E2_total,
            }

        return EnergyDecomp(
            total=total,
            e_sheet=e_sheet, nu_sheet=nu_sheet, p_sheet=p_sheet,
            ep_cross=ep_cross, enu_cross=enu_cross, nup_cross=nup_cross,
            fractions=fractions,
        )

    # ── Dynamic model (α-impedance) ─────────────────────────────────

    _SHEET_R_MAP = {'e': '_r_e', 'nu': '_r_nu', 'p': '_r_p'}
    _SHEET_TUBE = {'e': 0, 'nu': 2, 'p': 4}
    _SHEET_RING = {'e': 1, 'nu': 3, 'p': 5}

    def pressure_harmonics(self, n_tube, n_ring, r):
        """
        Pressure harmonics for mode (n_tube, n_ring) on a torus with
        aspect ratio r = a/R.  Cached by (|n_tube|, |n_ring|, r).

        Returns PressureHarmonics namedtuple.
        """
        key = (abs(n_tube), abs(n_ring), r)
        if key not in self._harm_cache:
            self._harm_cache[key] = _compute_pressure_harmonics(*key)
        return self._harm_cache[key]

    def wall_shape(self, n_tube, n_ring, r):
        """
        Wall cross-section r(θ₁)/a for mode (n_tube, n_ring) at aspect
        ratio r.

        Returns WallShape namedtuple with theta, r_over_a, eccentricity.
        """
        harm = self.pressure_harmonics(n_tube, n_ring, r)
        return _compute_wall_shape(harm)

    def dynamic_correction(self, n):
        """
        Dynamic (α-impedance) eigenvalue correction for a 6D mode.

        Computes the per-sheet corrections weighted by E² fractions.
        Only sheets with nonzero tube winding contribute.

        Returns DynamicCorrection namedtuple.
        """
        n_arr = np.asarray(n, dtype=int)
        per_sheet = {}
        dominant_k = 0
        dominant_weight = 0.0

        decomp = self.energy_decomp(n)
        E2_total = decomp.total**2
        sheet_frac_keys = {'e': 'e', 'nu': 'nu', 'p': 'p'}

        delta_total = 0.0
        for sheet in ('e', 'nu', 'p'):
            nt = int(n_arr[self._SHEET_TUBE[sheet]])
            nr = int(n_arr[self._SHEET_RING[sheet]])
            if nt == 0:
                per_sheet[sheet] = 0.0
                continue

            r = getattr(self, self._SHEET_R_MAP[sheet])
            harm = self.pressure_harmonics(nt, nr, r)
            k_coupling = 2 * abs(nt)
            if k_coupling < len(harm.delta_r_k):
                eps_k = harm.delta_r_k[k_coupling]
            else:
                eps_k = 0.0
            dEE_sheet = eps_k / 2.0
            per_sheet[sheet] = dEE_sheet

            w = decomp.fractions.get(sheet, 0.0)
            delta_total += w * dEE_sheet

            if w > dominant_weight:
                dominant_weight = w
                dominant_k = k_coupling

        fund_dEE = self._fundamental_dEE(dominant_k, dominant_weight,
                                         decomp, n_arr)
        ff = abs(delta_total / fund_dEE) if fund_dEE != 0 else 0.0

        return DynamicCorrection(
            delta_E_over_E=delta_total,
            per_sheet=per_sheet,
            dominant_k=dominant_k,
            filter_factor=ff,
        )

    def _fundamental_dEE(self, dominant_k, dominant_weight, decomp, n_arr):
        """δE/E for the (1,2) fundamental on the dominant sheet."""
        best_sheet = None
        best_w = 0.0
        for sheet in ('e', 'nu', 'p'):
            w = decomp.fractions.get(sheet, 0.0)
            if w > best_w:
                best_w = w
                best_sheet = sheet
        if best_sheet is None:
            return 0.0
        r = getattr(self, self._SHEET_R_MAP[best_sheet])
        fund_harm = self.pressure_harmonics(1, 2, r)
        if len(fund_harm.delta_r_k) > 2:
            return fund_harm.delta_r_k[2] / 2.0
        return 0.0

    def filter_factor(self, n):
        """
        Low-pass filter suppression factor for mode n.

        Returns |δE/E(n)| / |δE/E(fundamental)| on the dominant sheet.
        Values < 1 mean this mode is suppressed relative to (1,2).
        """
        return self.dynamic_correction(n).filter_factor

    @staticmethod
    def charge(n):
        """
        Electric charge in units of e.

        Q = −n₁ + n₅ (KK compact momentum formula).

        Parameters
        ----------
        n : tuple or array-like (6,)

        Returns
        -------
        int — net charge.
        """
        return _mode_charge(n)

    @staticmethod
    def spin(n):
        """
        Count of spin-½ contributions from odd tube windings.

        0 → boson, 1 → fermion (½), 2 → 0 or 1, 3 → ½ or 3/2.

        Parameters
        ----------
        n : tuple or array-like (6,)

        Returns
        -------
        int — number of spin-½ contributions.
        """
        return _mode_spin(n)

    @staticmethod
    def spin_label(n):
        """Human-readable spin classification string."""
        return _mode_spin_label(n)

    # ── Jacobian and sensitivity ──────────────────────────────────

    def jacobian(self, n):
        """
        Analytical Jacobian ∂E/∂θ for a mode.

        Computes the derivative of mode energy with respect to each
        geometry parameter: r_e, r_nu, r_p, sigma_ep, sigma_enu, sigma_nup.

        The derivation uses:

            E² = (2πℏc)² ñᵀ G̃⁻¹ ñ
            ∂E/∂θ = (2πℏc)² / (2E) · ñᵀ (∂G̃⁻¹/∂θ) ñ

        For cross-shears:
            ∂G̃⁻¹/∂σ = −G̃⁻¹ (∂G̃/∂σ) G̃⁻¹

        For aspect ratios the chain is:
            r → s (implicit: α(r,s) = α_target, so ∂s/∂r = −(∂α/∂r)/(∂α/∂s))
            r, s → L (Compton constraint)
            L → G̃_within (B = diag(L)(I + S), then G̃ = BᵀB / (L_i L_j))
            G̃ → G̃⁻¹

        Parameters
        ----------
        n : tuple or array-like (6,) — integer quantum numbers

        Returns
        -------
        dict mapping parameter name → float (∂E/∂θ in MeV per unit θ).
        """
        n_arr = np.asarray(n, dtype=float)
        ntilde = n_arr / self._L
        prefactor = (2 * math.pi * _hbar_c_MeV_fm)**2
        E = self.energy(n)
        if E < 1e-30:
            # Zero mode: all derivatives are zero
            return {p: 0.0 for p in
                    ('r_e', 'r_nu', 'r_p', 'sigma_ep', 'sigma_enu', 'sigma_nup')}

        Gti = self._Gti
        result = {}

        # ── Cross-shears: analytical ──────────────────────────────
        # ∂G̃/∂σ has nonzero entries only in the cross-block.
        # ∂G̃⁻¹/∂σ = −G̃⁻¹ (∂G̃/∂σ) G̃⁻¹
        # ∂E/∂σ = prefactor/(2E) · ñᵀ (∂G̃⁻¹/∂σ) ñ

        for name, pairs in _CROSS_BLOCKS.items():
            dGt = np.zeros((6, 6))
            for i, j in pairs:
                dGt[i, j] = 1.0
                dGt[j, i] = 1.0
            dGti = -Gti @ dGt @ Gti
            dE = prefactor / (2 * E) * ntilde @ dGti @ ntilde
            param_name = 'sigma_' + name
            result[param_name] = float(dE)

        # ── r_nu: simple (only L₃ changes) ───────────────────────
        # L₃ = r_nu × L₄,  L₄ is constant.
        # ∂L₃/∂r_nu = L₄.  All other L unchanged.
        # Need ∂G̃/∂r_nu via ∂G̃/∂L₃.
        result['r_nu'] = float(self._dE_dr_simple(
            n_arr, ntilde, E, prefactor, sheet_idx=2, L_ring=self._L[3]))

        # ── r_e: implicit chain through α ─────────────────────────
        result['r_e'] = float(self._dE_dr_charged(
            n_arr, ntilde, E, prefactor,
            r=self._r_e, s=self._s12,
            tube_idx=0, ring_idx=1, M_MeV=M_E_MEV))

        # ── r_p: implicit chain through α ─────────────────────────
        result['r_p'] = float(self._dE_dr_charged(
            n_arr, ntilde, E, prefactor,
            r=self._r_p, s=self._s56,
            tube_idx=4, ring_idx=5, M_MeV=M_P_MEV))

        return result

    def _dE_dr_simple(self, n_arr, ntilde, E, prefactor, sheet_idx, L_ring):
        """
        ∂E/∂r for a sheet where only L_tube = r × L_ring changes.

        Used for r_nu where L₄ is fixed and L₃ = r_nu × L₄.
        The within-plane shear s₃₄ is a constant (not r-dependent).
        """
        tube_idx = sheet_idx  # e.g., index 2 for neutrino tube
        # ∂L_tube/∂r = L_ring.  All other L unchanged.
        # Use finite-difference on the metric as a cross-check:
        # rebuild with L_tube ± δ and compute ∂G̃/∂L_tube numerically.
        # But we can do this analytically.

        # The dimensionless metric G̃_ij = G_phys_ij / (L_i L_j)
        # where G_phys = BᵀB, B = diag(L)(I+S).
        # G̃ depends on L only through the within-plane block.
        # For the neutrino block: B[2,2] = L₃, B[2,3] = L₃ × s₃₄
        # So G̃ for the (2,3) block depends on L₃ only through
        # the normalization.  Actually G̃_ij = (BᵀB)_ij / (L_i L_j),
        # and the within-plane G̃ entries are L-independent (they're
        # just 1, s, s, 1+s² etc).  So ∂G̃_within/∂L = 0.

        # But ñ_tube = n_tube / L_tube depends on L_tube!
        # ∂ñ_tube/∂L_tube = -n_tube / L_tube²
        # ∂ñ_tube/∂r = (∂ñ_tube/∂L_tube)(∂L_tube/∂r) = -n_tube/(L_tube²) × L_ring

        # E² = prefactor × ñᵀ G̃⁻¹ ñ
        # ∂E²/∂r = prefactor × 2 × (∂ñ/∂r)ᵀ G̃⁻¹ ñ
        #        (since G̃⁻¹ doesn't depend on L for within-plane)

        dntilde_dr = np.zeros(6)
        L_tube = self._L[tube_idx]
        dntilde_dr[tube_idx] = -n_arr[tube_idx] / (L_tube**2) * L_ring

        dE2_dr = prefactor * 2 * dntilde_dr @ self._Gti @ ntilde
        return dE2_dr / (2 * E)

    def _dE_dr_charged(self, n_arr, ntilde, E, prefactor,
                       r, s, tube_idx, ring_idx, M_MeV):
        """
        ∂E/∂r for a charged sheet (electron or proton) where s depends
        on r through α(r,s) = α_target.

        The chain: r → s (implicit), r,s → μ → E₀ → L_ring → L_tube.

        Both L_tube and L_ring change with r.
        """
        # ── Step 1: ∂s/∂r via implicit function theorem ──────────
        # α(r, s) = α_target  ⟹  ∂s/∂r = −(∂α/∂r) / (∂α/∂s)
        da_dr = _dalpha_dr(r, s)
        da_ds = _dalpha_ds(r, s)
        if abs(da_ds) < 1e-30:
            return 0.0
        ds_dr = -da_dr / da_ds

        # ── Step 2: ∂μ/∂r where μ = √(1/r² + (2-s)²) ───────────
        mu = mu_12(r, s)
        dmu_dr = (1 / mu) * (-1 / r**3 + (2 - s) * (-1) * ds_dr)
        # = (-1/r³ − (2−s) ds/dr) / μ

        # ── Step 3: ∂L_ring/∂r ────────────────────────────────────
        # L_ring = 2πℏc × μ / M_MeV  (from E₀ = M/μ, L = 2πℏc/E₀)
        # ∂L_ring/∂r = 2πℏc/M × ∂μ/∂r
        dLring_dr = 2 * math.pi * _hbar_c_MeV_fm / M_MeV * dmu_dr

        # ── Step 4: ∂L_tube/∂r ────────────────────────────────────
        # L_tube = r × L_ring
        # ∂L_tube/∂r = L_ring + r × ∂L_ring/∂r
        L_ring = self._L[ring_idx]
        dLtube_dr = L_ring + r * dLring_dr

        # ── Step 5: ∂ñ/∂r ────────────────────────────────────────
        # ñ_i = n_i / L_i.  Only L_tube and L_ring change.
        L_tube = self._L[tube_idx]
        dntilde_dr = np.zeros(6)
        dntilde_dr[tube_idx] = -n_arr[tube_idx] / (L_tube**2) * dLtube_dr
        dntilde_dr[ring_idx] = -n_arr[ring_idx] / (L_ring**2) * dLring_dr

        # ── Step 6: ∂G̃/∂r via ∂s/∂r ─────────────────────────────
        # G̃ within-plane from B = diag(L)(I+S), G̃_ij = G_phys_ij/(L_i L_j):
        #   G̃[tube,ring] = r × s
        #   G̃[ring,ring] = 1 + r² × s²
        #   G̃[tube,tube] = 1  (no s dependence)
        # Derivatives w.r.t. r (including chain through s(r)):
        #   ∂G̃[tube,ring]/∂r = s + r × ds/dr
        #   ∂G̃[ring,ring]/∂r = 2r s² + 2r² s × ds/dr
        dGt = np.zeros((6, 6))
        dGt[tube_idx, ring_idx] = s + r * ds_dr
        dGt[ring_idx, tube_idx] = s + r * ds_dr
        dGt[ring_idx, ring_idx] = 2 * r * s**2 + 2 * r**2 * s * ds_dr

        dGti = -self._Gti @ dGt @ self._Gti

        # ── Step 7: combine ───────────────────────────────────────
        # ∂E²/∂r = prefactor × [2 (∂ñ/∂r)ᵀ G̃⁻¹ ñ  +  ñᵀ (∂G̃⁻¹/∂r) ñ]
        dE2_from_ntilde = prefactor * 2 * dntilde_dr @ self._Gti @ ntilde
        dE2_from_metric = prefactor * ntilde @ dGti @ ntilde
        dE2_dr = dE2_from_ntilde + dE2_from_metric

        return dE2_dr / (2 * E)

    def sensitivity(self, n):
        """
        Human-readable sensitivity report for a mode.

        Shows how strongly the mode energy depends on each geometry
        parameter, classified as strong/moderate/weak/negligible.

        Parameters
        ----------
        n : tuple or array-like (6,) — integer quantum numbers

        Returns
        -------
        str — formatted report.

        Example
        -------
        >>> m.sensitivity((0, -2, 1, 0, 0, 2))
        Neutron (0,−2,+1,0,0,+2)  E = 946.8 MeV
          r_e:        ∂E/∂r_e    =  −0.02 MeV/unit   (negligible)
          r_nu:       ∂E/∂r_ν    =   0.00 MeV/unit   (negligible)
          r_p:        ∂E/∂r_p    = −48.30 MeV/unit   (strong)
          sigma_ep:   ∂E/∂σ_ep   = −14.20 MeV/unit   (strong)
          sigma_enu:  ∂E/∂σ_eν   =   0.00 MeV/unit   (negligible)
          sigma_nup:  ∂E/∂σ_νp   =   0.00 MeV/unit   (negligible)
        """
        J = self.jacobian(n)
        E = self.energy(n)
        n_str = ','.join(f'{int(x):+d}' for x in n)

        lines = [f"Mode ({n_str})  E = {E:.3f} MeV"]

        display_names = {
            'r_e': 'r_e', 'r_nu': 'r_ν', 'r_p': 'r_p',
            'sigma_ep': 'σ_ep', 'sigma_enu': 'σ_eν', 'sigma_nup': 'σ_νp',
        }
        order = ['r_e', 'r_nu', 'r_p', 'sigma_ep', 'sigma_enu', 'sigma_nup']

        for key in order:
            val = J.get(key, 0.0)
            # Classify strength relative to the mode energy
            if E > 0:
                rel = abs(val) / E
            else:
                rel = 0.0
            if rel > 0.05:
                strength = "strong"
            elif rel > 0.005:
                strength = "moderate"
            elif rel > 0.0005:
                strength = "weak"
            else:
                strength = "negligible"
            name = display_names.get(key, key)
            lines.append(f"  {name:12s} ∂E/∂{name:5s} = {val:+10.3f} MeV/unit   ({strength})")

        return "\n".join(lines)

    # ── Scanning ──────────────────────────────────────────────────

    def scan_modes(self, n_max=3, E_max_MeV=None,
                   charge=None, spin_halves=None):
        """
        Enumerate Ma modes by brute-force hypercube scan.

        Scans all |n_i| ≤ n_max, excluding the zero mode.  Optionally
        filters by energy ceiling, charge, and spin.

        Parameters
        ----------
        n_max : int — maximum |n_i| per dimension (default 3)
        E_max_MeV : float or None — discard modes above this energy
        charge : int or None — required charge (None = any)
        spin_halves : int or None — required spin-½ count (None = any)

        Returns
        -------
        list of Mode namedtuples, sorted by energy.

        Notes
        -----
        This is O((2n+1)⁶) brute force.  For n_max > 5, use the
        Fincke-Pohst ellipsoid enumeration in ``modes()`` instead
        (not yet implemented — see Phase 2 stubs below).
        """
        modes = []
        rng = range(-n_max, n_max + 1)
        for n in iproduct(rng, repeat=6):
            if all(ni == 0 for ni in n):
                continue
            if charge is not None and _mode_charge(n) != charge:
                continue
            if spin_halves is not None and _mode_spin(n) != spin_halves:
                continue
            E = self.energy(n)
            if E_max_MeV is not None and E > E_max_MeV:
                continue
            dE = None
            if self._dynamic:
                E_st = _mode_energy(n, self._Gti, self._L)
                dE = E - E_st
            modes.append(Mode(n=n, E_MeV=E,
                              charge=_mode_charge(n),
                              spin_halves=_mode_spin(n),
                              delta_E_MeV=dE))
        modes.sort(key=lambda m: m.E_MeV)
        return modes

    # ── Metric diagnostics ────────────────────────────────────────

    def is_positive_definite(self):
        """Check that the metric has all positive eigenvalues."""
        return bool(np.all(np.linalg.eigvalsh(self._Gt) > 0))

    # ── Immutable update ──────────────────────────────────────────

    def with_params(self, **kwargs):
        """
        Create a new Ma with some parameters changed.

        Accepts any constructor keyword argument.  Unspecified
        parameters are inherited from this instance.

        Returns
        -------
        Ma — new instance with updated parameters.

        Example
        -------
        >>> m2 = m.with_params(sigma_ep=-0.10)
        >>> m3 = m.with_params(r_p=9.0, self_consistent=True)
        """
        defaults = {
            'r_e': self._r_e,
            'r_nu': self._r_nu,
            'r_p': self._r_p,
            'sigma_ep': self.sigma_ep,
            'sigma_enu': self.sigma_enu,
            'sigma_nup': self.sigma_nup,
            'self_consistent': self._self_consistent,
            'dynamic': self._dynamic,
        }
        defaults.update(kwargs)
        return Ma(**defaults)

    # ── Inverse solver ─────────────────────────────────────────────

    @classmethod
    def fit(cls, targets, free_params, fixed_params=None,
            tol=1e-8, max_iter=50, damping=1.0, dynamic=False):
        """
        Find geometry parameters that best reproduce target masses.

        Uses Gauss-Newton iteration with the analytical Jacobian.
        At each step: compute residuals (E_computed − E_target),
        build the Jacobian matrix, solve the linear system for
        parameter updates, and create a new Ma at the updated point.

        When there are more free parameters than targets, the system
        is underdetermined.  The solver uses the minimum-norm solution
        (via pseudoinverse) and reports the null space — parameter
        directions that leave all target energies unchanged.

        Parameters
        ----------
        targets : list of Target(n, mass_MeV)
            Mode assignments and their target masses.
        free_params : list of str
            Parameter names to optimize.  Must be from:
            'r_e', 'r_nu', 'r_p', 'sigma_ep', 'sigma_enu', 'sigma_nup'.
        fixed_params : dict or None
            Fixed parameter values.  Any parameter not in free_params
            and not in fixed_params uses its default (r=6.6/5.0/8.906,
            sigma=0).
        tol : float
            Convergence tolerance on max |residual| in MeV.
        max_iter : int
            Maximum Gauss-Newton iterations.
        damping : float
            Step damping factor (0 < damping ≤ 1).  At 1.0 the full
            Gauss-Newton step is taken.  Reduce if oscillating.

        Returns
        -------
        FitResult namedtuple.

        Examples
        --------
        Re-derive R27's parameters from neutron + muon:

        >>> result = Ma.fit(
        ...     targets=[
        ...         Target(n=(0,-2,1,0,0,2), mass_MeV=939.565),  # neutron
        ...         Target(n=(-1,5,0,0,-2,0), mass_MeV=105.658), # muon
        ...     ],
        ...     free_params=['r_p', 'sigma_ep'],
        ...     fixed_params={'r_e': 0.5, 'r_nu': 5.0},  # r_e is free; 0.5 is a guess
        ... )
        >>> result.params  # should recover r_p ≈ 8.906, σ_ep ≈ -0.0906
        """
        VALID_PARAMS = ('r_e', 'r_nu', 'r_p', 'sigma_ep', 'sigma_enu', 'sigma_nup')
        for p in free_params:
            if p not in VALID_PARAMS:
                raise ValueError(f"Unknown parameter {p!r}. "
                                 f"Must be one of {VALID_PARAMS}")

        # Default starting point.
        #   r_p = 8.906, σ_ep = -0.0906: pinned by R27 (neutron + muon)
        #   r_e, r_nu: FREE parameters — these are starting guesses only.
        #     r_e = 0.5 follows R37 F7 (energy minimization prefers fat torus).
        #     r_nu = 5.0 is a conventional starting point (unconstrained).
        #   Callers should set these explicitly via fixed_params when known.
        defaults = {
            'r_e': 0.5, 'r_nu': 5.0, 'r_p': 8.906,
            'sigma_ep': -0.0906, 'sigma_enu': 0.0, 'sigma_nup': 0.0,
        }
        if fixed_params:
            defaults.update(fixed_params)

        # Current parameter vector (only the free ones)
        param_vec = np.array([defaults[p] for p in free_params])
        n_params = len(free_params)
        n_targets = len(targets)

        def _build_ma(pvec):
            kw = dict(defaults)
            for i, p in enumerate(free_params):
                kw[p] = float(pvec[i])
            # Remove non-constructor keys
            kw.pop('self_consistent', None)
            try:
                return Ma(**kw, self_consistent=True, dynamic=dynamic)
            except ValueError:
                return None

        converged = False
        for iteration in range(max_iter):
            m = _build_ma(param_vec)
            if m is None:
                # Metric not positive-definite; shrink the step
                param_vec = param_vec * 0.9 + np.array(
                    [defaults[p] for p in free_params]) * 0.1
                continue

            # Compute residuals
            residuals = np.array([
                m.energy(t.n) - t.mass_MeV for t in targets
            ])

            if np.max(np.abs(residuals)) < tol:
                converged = True
                break

            # Build Jacobian matrix numerically: J[i,j] = ∂E_i/∂θ_j
            # Uses finite differences on the full self-consistent Ma,
            # which captures the indirect L-adjustment path that the
            # analytical Jacobian (computed at fixed L) misses.
            J = np.zeros((n_targets, n_params))
            h_jac = 1e-6
            for j in range(n_params):
                pvec_p = param_vec.copy(); pvec_p[j] += h_jac
                pvec_m = param_vec.copy(); pvec_m[j] -= h_jac
                m_p = _build_ma(pvec_p)
                m_m = _build_ma(pvec_m)
                if m_p is None or m_m is None:
                    continue
                for i, t in enumerate(targets):
                    J[i, j] = (m_p.energy(t.n) - m_m.energy(t.n)) / (2 * h_jac)

            # Levenberg-Marquardt step: solve (JᵀJ + λI) δ = -Jᵀr
            # λ adapts: start moderate, reduce on success, increase on failure.
            JtJ = J.T @ J
            Jtr = J.T @ residuals

            if iteration == 0:
                lam = 0.01 * max(np.diag(JtJ).max(), 1e-6)

            for _ in range(10):  # inner loop: try different λ
                try:
                    delta = np.linalg.solve(JtJ + lam * np.eye(n_params), -Jtr)
                except np.linalg.LinAlgError:
                    lam *= 10
                    continue

                candidate = param_vec + damping * delta
                m_try = _build_ma(candidate)
                if m_try is not None:
                    r_try = np.array([m_try.energy(t.n) - t.mass_MeV
                                      for t in targets])
                    if np.sum(r_try**2) < np.sum(residuals**2):
                        param_vec = candidate
                        lam = max(lam * 0.3, 1e-12)
                        break
                lam = min(lam * 5, 1e20)
            else:
                # All inner steps failed; accept anyway with heavy damping
                param_vec = param_vec + 0.1 * damping * delta

        # Final state
        m = _build_ma(param_vec)
        if m is None:
            return FitResult(
                params={}, residuals=np.array([]),
                ma=None, jacobian=np.array([]),
                cov=None, null_space=None,
                converged=False, iterations=iteration + 1)

        residuals = np.array([m.energy(t.n) - t.mass_MeV for t in targets])

        # Final Jacobian
        J = np.zeros((n_targets, n_params))
        for i, t in enumerate(targets):
            jac_dict = m.jacobian(t.n)
            for j, p in enumerate(free_params):
                J[i, j] = jac_dict.get(p, 0.0)

        # Parameter covariance (from J): cov ≈ (JᵀJ)⁻¹ × σ²
        # where σ² is estimated from residuals
        cov = None
        null_space = None
        if n_params <= n_targets:
            JtJ = J.T @ J
            eigvals = np.linalg.eigvalsh(JtJ)
            if np.min(eigvals) > 1e-20:
                sigma2 = np.sum(residuals**2) / max(n_targets - n_params, 1)
                cov = np.linalg.inv(JtJ) * sigma2
        else:
            # Underdetermined: report null space
            U, S, Vt = np.linalg.svd(J, full_matrices=True)
            rank = np.sum(S > 1e-10 * S[0])
            if rank < n_params:
                null_space = Vt[rank:].T  # columns are null-space basis

        final_params = {p: float(param_vec[i]) for i, p in enumerate(free_params)}
        final_params.update({k: v for k, v in defaults.items()
                            if k not in free_params})

        return FitResult(
            params=final_params,
            residuals=residuals,
            ma=m,
            jacobian=J,
            cov=cov,
            null_space=null_space,
            converged=converged,
            iterations=iteration + 1,
        )

    # ── Serialization ─────────────────────────────────────────────

    def to_dict(self):
        """
        Serialize to a JSON-compatible dict.

        Includes all input parameters plus derived quantities
        (L, shears, convergence info).  Sufficient to reconstruct
        the Ma instance via ``from_dict()``.
        """
        d = {
            'r_e': self._r_e, 'r_nu': self._r_nu, 'r_p': self._r_p,
            'sigma_ep': self.sigma_ep,
            'sigma_enu': self.sigma_enu,
            'sigma_nup': self.sigma_nup,
            'self_consistent': self._self_consistent,
            'dynamic': self._dynamic,
            # Derived (for reference, not used in reconstruction)
            's12': self._s12, 's34': self._s34, 's56': self._s56,
            'L': self._L.tolist(),
            'L_units': 'fm',
        }
        if self._converged is not None:
            d['converged'] = self._converged
            d['iterations'] = self._iterations
        return d

    @classmethod
    def from_dict(cls, d):
        """
        Reconstruct a Ma instance from a dict (from ``to_dict()``).
        """
        return cls(
            r_e=d['r_e'], r_nu=d['r_nu'], r_p=d['r_p'],
            sigma_ep=d.get('sigma_ep', 0.0),
            sigma_enu=d.get('sigma_enu', 0.0),
            sigma_nup=d.get('sigma_nup', 0.0),
            self_consistent=d.get('self_consistent', False),
            dynamic=d.get('dynamic', False),
        )

    # ── Legacy interop ────────────────────────────────────────────

    @classmethod
    def from_legacy(cls, Gtilde_inv, L):
        """
        Wrap legacy ma.py output (Gti, L) into a Ma object.

        This creates a Ma instance that uses the provided metric
        directly, without recomputing from aspect ratios.  Useful
        for validating new code against legacy results.

        The resulting object has full functionality (energy, charge,
        spin, scan) but ``with_params()`` and ``to_dict()`` will
        reflect the inferred parameters, not the originals.

        Parameters
        ----------
        Gtilde_inv : ndarray (6, 6) — inverse dimensionless metric
        L : ndarray (6,) — circumferences in fm
        """
        obj = object.__new__(cls)
        L = np.asarray(L, dtype=float)
        Gti = np.asarray(Gtilde_inv, dtype=float)
        Gt = np.linalg.inv(Gti)
        obj._L = L.copy()
        obj._Gt = Gt
        obj._Gti = Gti.copy()
        obj._r_e = L[0] / L[1] if L[1] != 0 else 0.0
        obj._r_nu = L[2] / L[3] if L[3] != 0 else 0.0
        obj._r_p = L[4] / L[5] if L[5] != 0 else 0.0
        obj._s12 = Gt[0, 1] / Gt[0, 0] if Gt[0, 0] != 0 else 0.0
        obj._s34 = S34_DEFAULT
        obj._s56 = Gt[4, 5] / Gt[4, 4] if Gt[4, 4] != 0 else 0.0
        obj._cross_shears = {}
        obj._self_consistent = False
        obj._dynamic = False
        obj._harm_cache = {}
        obj._converged = None
        obj._iterations = None
        return obj

    def to_legacy(self):
        """
        Export for use with legacy ma.py functions.

        Returns
        -------
        (Gtilde_inv, L) — the two arrays that legacy functions expect.
        """
        return self._Gti.copy(), self._L.copy()

    # ── Summary ───────────────────────────────────────────────────

    def summary(self):
        """Human-readable summary of the geometry."""
        label = "Ma geometry (dynamic)" if self._dynamic else "Ma geometry"
        lines = [
            label,
            f"  r_e = {self._r_e:.4f}   r_ν = {self._r_nu:.4f}   r_p = {self._r_p:.4f}",
            f"  s₁₂ = {self._s12:.6f}  s₃₄ = {self._s34:.5f}  s₅₆ = {self._s56:.6f}",
            f"  σ_ep = {self.sigma_ep:.4f}  σ_eν = {self.sigma_enu:.4f}  σ_νp = {self.sigma_nup:.4f}",
            f"  L = [{', '.join(f'{x:.4f}' for x in self._L)}] fm",
        ]
        if self._self_consistent:
            lines.append(f"  self-consistent: converged={self._converged}, "
                         f"iterations={self._iterations}")
        E_e = self.energy(_N_ELECTRON)
        E_p = self.energy(_N_PROTON)
        lines.append(f"  E(electron) = {E_e:.6f} MeV")
        lines.append(f"  E(proton)   = {E_p:.3f} MeV")
        if self._dynamic:
            corr_e = self.dynamic_correction(_N_ELECTRON)
            corr_p = self.dynamic_correction(_N_PROTON)
            lines.append(f"  δE/E(electron) = {corr_e.delta_E_over_E:.6e}")
            lines.append(f"  δE/E(proton)   = {corr_p.delta_E_over_E:.6e}")
        return "\n".join(lines)

    def __repr__(self):
        sc = ", self_consistent=True" if self._self_consistent else ""
        dyn = ", dynamic=True" if self._dynamic else ""
        return (f"Ma(r_e={self._r_e}, r_nu={self._r_nu}, r_p={self._r_p}, "
                f"sigma_ep={self.sigma_ep}{sc}{dyn})")


# ══════════════════════════════════════════════════════════════════════
#  Phase 2 stubs — fast ellipsoid enumeration
#
#  These are NOT yet implemented.  They raise NotImplementedError
#  with a description of what they will do and why, so that callers
#  discover the intended API when they need it.
#
#  See ma-model.md §Feature 2 (Fincke-Pohst), §Feature 3
#  (energy decomposition), §Feature 4 (Jacobian), §Feature 5
#  (inverse solver), §Feature 6 (sensitivity), §Feature 7
#  (spectrum queries) for the full design.
# ══════════════════════════════════════════════════════════════════════

def _fincke_pohst_enumerate(M, R_sq):
    """
    Enumerate integer lattice points inside an ellipsoid.

    Finds all n ∈ Z⁶ (n ≠ 0) satisfying nᵀ M n ≤ R².

    Uses the Fincke-Pohst algorithm:
    1. Cholesky-decompose M = LLᵀ.
    2. Enumerate dimension-by-dimension, using Cholesky rows to
       bound each coordinate given the partial sums from higher
       dimensions.
    3. At each level, compute residual radius budget; only recurse
       if positive.

    For Ma with extreme scale hierarchy (L_ν/L_e ~ 10⁸), the
    ellipsoid is highly elongated.  Consider a two-stage approach:
    enumerate heavy directions (e, p) first, then analytically
    bound neutrino quantum numbers per heavy assignment.

    Parameters
    ----------
    M : ndarray (6, 6) — positive-definite energy kernel
        M_ij = G̃⁻¹_ij / (L_i L_j)
    R_sq : float — squared energy bound (E_max / (2πℏc))²

    Returns
    -------
    list of tuples — integer 6-vectors inside the ellipsoid.

    References
    ----------
    Fincke & Pohst (1985), "Improved methods for calculating vectors
    of short length in a lattice."
    """
    raise NotImplementedError(
        "Fincke-Pohst enumeration not yet implemented. "
        "Use scan_modes(n_max=...) for brute-force scanning. "
        "See ma-model.md §Feature 2 for the design.")


# The following are method stubs that would be added to the Ma class.
# They are defined here as standalone documentation; the actual
# implementation will add them as methods when the phase is built.

def _stub_modes(self, E_max_MeV, charge=None, spin_halves=None):
    """
    Fast mode enumeration using Fincke-Pohst ellipsoid search.

    Unlike scan_modes() which iterates over a hypercube of
    (2n+1)⁶ points, this visits only lattice points inside the
    energy ellipsoid nᵀ M n ≤ (E_max/(2πℏc))².

    Expected speedup: 100-1000× over scan_modes at n_max ≥ 5.
    At n_max = 15 (where brute force is infeasible at 900M points),
    this should complete in seconds for ~14,000 modes below 10 GeV.

    CPT note: exploiting n → −n symmetry (same energy, opposite
    charge) halves the enumeration.  The symmetry also serves as
    a sanity check: mode_count by charge should be symmetric.

    Parameters
    ----------
    E_max_MeV : float — energy ceiling
    charge : int or None — filter by charge
    spin_halves : int or None — filter by spin

    Returns
    -------
    list of Mode namedtuples, sorted by energy.
    """
    raise NotImplementedError(
        "Fast mode enumeration not yet implemented. "
        "Use scan_modes(n_max=...) for brute-force scanning. "
        "See ma-model.md §Feature 2.")






def _stub_spectrum(self, E_max_MeV, charge=None, spin_halves=None):
    """
    Rich spectrum query with filtering (delegates to modes()).

    Parameters
    ----------
    E_max_MeV : float
    charge : int or None
    spin_halves : int or None

    Returns
    -------
    list of Mode — filtered and sorted.
    """
    raise NotImplementedError(
        "Spectrum queries not yet implemented. "
        "See ma-model.md §Feature 7.")


def _stub_mode_count(self, E_max_MeV, by='charge'):
    """
    Count modes below an energy ceiling, grouped by a property.

    Parameters
    ----------
    E_max_MeV : float
    by : str — 'charge' or 'spin'

    Returns
    -------
    dict mapping int → int (property value → count).
    """
    raise NotImplementedError(
        "Mode counting not yet implemented. "
        "See ma-model.md §Feature 7.")


def _stub_nearest(self, mass_MeV, charge=None, spin_halves=None):
    """
    Find the mode nearest to a target mass.

    Parameters
    ----------
    mass_MeV : float
    charge : int or None
    spin_halves : int or None

    Returns
    -------
    Mode — the closest match.
    """
    raise NotImplementedError(
        "Nearest-mode lookup not yet implemented. "
        "See ma-model.md §Feature 7.")
