"""
Model-D engine — filtered Ma model  (``ma_model_d.py``)

Clean replacement for ``ma_model.py`` (model-C).  Designed around
the filtering results from R46 (electron), R47 (proton), and
R49 (neutrino).

Key differences from model-C (``ma_model.py``):
  - No hard-coded r_p, σ_ep, or S34_DEFAULT
  - No assumption that the proton is (1,2)
  - Per-sheet waveguide cutoff built in
  - Finite-ε spin (numerical path integral, numpy only)
  - No scipy dependency
  - All parameters are explicit inputs, not derived from
    hard-coded formulas

PHYSICAL PICTURE
================

Three flat material sheets Ma_e, Ma_ν, Ma_p form a 6-torus Ma.
Each sheet is a 2-torus with aspect ratio ε = a/R (tube/ring
circumference ratio) and within-plane shear s.

    Indices 0, 1  →  Ma_e  (θ₁ = tube, θ₂ = ring)
    Indices 2, 3  →  Ma_ν  (θ₃ = tube, θ₄ = ring)
    Indices 4, 5  →  Ma_p  (θ₅ = tube, θ₆ = ring)

Tube directions have even indices (0, 2, 4).  Ring directions have
odd indices (1, 3, 5).  Charge and spin are determined by tube
windings.

TYPICAL USAGE
=============

    from lib.ma_model_d import MaD

    # All parameters explicit:
    m = MaD(
        eps_e=0.5,   s_e=...,   L_ring_e=...,
        eps_nu=5.0,  s_nu=0.022, L_ring_nu=...,
        eps_p=1/3,   s_p=...,   L_ring_p=...,
    )
    m.energy((1, 2, 0, 0, 0, 0))       # electron energy (MeV)
    m.charge((1, 2, 0, 0, 0, 0))       # -1

    # Or use the from_physics() constructor:
    m = MaD.from_physics(eps_e=0.5, eps_nu=5.0, eps_p=1/3)
    modes = m.scan_modes(n_max=3, E_max_MeV=2000)

    # Near-miss search:
    hits = m.nearest_modes(target_MeV=939.565, n_max=3, top_k=5)
"""

import math
from collections import namedtuple
from itertools import product as iproduct

import numpy as np

from lib.constants import (
    hbar, c, e as _eV_J, alpha as ALPHA, m_e,
)

# ── Derived constants ─────────────────────────────────────────────

_MeV_J = _eV_J * 1e6
_hbar_c_MeV_fm = hbar * c / _MeV_J * 1e15       # ≈ 197.3 MeV·fm
_TWO_PI = 2 * math.pi
_TWO_PI_HC = _TWO_PI * _hbar_c_MeV_fm            # 2πℏc in MeV·fm

M_E_MEV = m_e * c**2 / _MeV_J                    # 0.51100 MeV
M_P_MEV = 938.272                                 # proton mass (PDG 2022)

# Neutrino mass-squared splittings (eV²)
DM2_21 = 7.53e-5
DM2_31 = 2.530e-3

# ── Named tuples ──────────────────────────────────────────────────

Mode = namedtuple('Mode', [
    'n',              # tuple(6,) — quantum numbers
    'E_MeV',          # float — energy in MeV
    'charge',         # int — electric charge in units of e
    'spin',           # float — topological spin (0.0, 0.5, 1.0, 1.5)
    'spin_halves',    # int — number of spin-½ contributions (raw count)
    'spin_Lz',        # float or None — classical L_z/ℏ diagnostic (if computed)
    'propagates',     # bool — True if all active sheets pass waveguide cutoff
    'sheets_active',  # str — which sheets carry winding ('e', 'nu', 'p')
])

NearMiss = namedtuple('NearMiss', [
    'mode',           # Mode
    'residual_MeV',   # float — E_mode − E_target
    'residual_frac',  # float — |residual| / E_target
])


# ══════════════════════════════════════════════════════════════════
#  Alpha formula (R19 Track 8)
# ══════════════════════════════════════════════════════════════════

def alpha_from_geometry(eps, s):
    """
    Fine-structure constant from sheared torus geometry.

    α(ε, s) = ε² μ sin²(2πs) / (4π(2−s)²)

    where μ = √(1/ε² + (2−s)²) is the dimensionless (1,2) mode energy
    on a sheet with aspect ratio ε and shear s.

    Parameters
    ----------
    eps : float — aspect ratio (tube circumference / ring circumference)
    s : float — within-plane shear, 0 < s < 0.5

    Returns
    -------
    float — predicted fine-structure constant
    """
    mu = math.sqrt(1 / eps**2 + (2 - s)**2)
    return eps**2 * mu * math.sin(_TWO_PI * s)**2 / (4 * math.pi * (2 - s)**2)


def solve_shear_for_alpha(eps, alpha_target=ALPHA, n_scan=3000):
    """
    Find the shear s that produces a target α for a given aspect ratio ε.

    Uses a coarse scan followed by bisection (no scipy).

    **Returns the POSITIVE branch (magnitude only).**  The α formula
    is sign-asymmetric, so two solution branches exist.  This function
    returns only the positive one.  For the signed alternative, see
    `solve_shear_for_alpha_signed`.

    Parameters
    ----------
    eps : float — aspect ratio
    alpha_target : float — target α (default: measured α ≈ 1/137.036)
    n_scan : int — number of scan points

    Returns
    -------
    float or None — shear s ∈ (0, 0.5), or None if no solution exists.
    """
    s_scan = np.linspace(0.001, 0.49, n_scan)
    a_scan = np.array([alpha_from_geometry(eps, s) for s in s_scan])

    for i in range(len(s_scan) - 1):
        if (a_scan[i] - alpha_target) * (a_scan[i + 1] - alpha_target) < 0:
            lo, hi = s_scan[i], s_scan[i + 1]
            for _ in range(60):
                mid = (lo + hi) / 2
                if (alpha_from_geometry(eps, mid) - alpha_target) * \
                   (alpha_from_geometry(eps, lo) - alpha_target) < 0:
                    hi = mid
                else:
                    lo = mid
            return (lo + hi) / 2
    return None


def solve_shear_for_alpha_signed(eps, alpha_target=ALPHA, sign=+1, n_scan=3000):
    """
    Signed variant of `solve_shear_for_alpha`.

    The α_from_geometry formula is **NOT symmetric in s** — at the
    same aspect ratio ε, α(ε, +s) ≠ α(ε, −s).  Two solution branches
    therefore exist:

    - **Positive branch (sign=+1):** s ∈ (0, 0.5), small magnitude.
      This is what `solve_shear_for_alpha` (the unsigned version)
      returns.  All existing model-D scripts use this branch.

    - **Negative branch (sign=−1):** s ∈ (−0.5, 0), magnitude
      typically 3–10× larger than the positive branch at the same ε.
      Different μ value, hence different particle mass at the same
      L_ring calibration.  Used by R52 Track 4f to test the
      "opposite sign for opposite charge" conjecture (Q114 §7).

    The two branches are PHYSICALLY DISTINCT — they correspond to
    different (ε, s) calibrations and would give different particle
    masses if substituted into existing scripts without rescaling
    L_ring.  The unsigned function preserves the existing
    calibration; this signed version is for exploration of alternate
    conventions.

    Parameters
    ----------
    eps : float — aspect ratio
    alpha_target : float — target α (default: measured α ≈ 1/137.036)
    sign : int — +1 (positive branch, default) or −1 (negative branch)
    n_scan : int — number of scan points

    Returns
    -------
    float or None — signed shear s, or None if no solution exists on
    the requested branch.

    Raises
    ------
    ValueError — if sign is not +1 or −1.

    Notes
    -----
    Like `solve_shear_for_alpha`, this function uses the (1,2) mode
    α formula (`alpha_from_geometry`).  When called for the proton's
    aspect ratio with the actual proton mode being (1,3) or (3,6),
    the result is the shear that would give α = 1/137 IF the proton
    were a (1,2) mode.  See Q114 §3 for discussion of this
    mode-hardcoding limitation.

    Convention adopted by R52 Track 4f:
        - Electron (negative charge): sign = −1
        - Proton (positive charge):   sign = +1
    The physical justification for this convention is the user's
    intuition that within-plane shear sign should track the charge
    sign of the particle (since both originate from the same tube
    winding direction).  This is documented but not derived; see
    Q114 §7.
    """
    if sign not in (+1, -1):
        raise ValueError(f"sign must be +1 or -1, got {sign}")

    if sign == +1:
        s_scan = np.linspace(0.001, 0.49, n_scan)
    else:
        s_scan = np.linspace(-0.49, -0.001, n_scan)

    a_scan = np.array([alpha_from_geometry(eps, s) for s in s_scan])

    for i in range(len(s_scan) - 1):
        if (a_scan[i] - alpha_target) * (a_scan[i + 1] - alpha_target) < 0:
            lo, hi = s_scan[i], s_scan[i + 1]
            for _ in range(60):
                mid = (lo + hi) / 2
                if (alpha_from_geometry(eps, mid) - alpha_target) * \
                   (alpha_from_geometry(eps, lo) - alpha_target) < 0:
                    hi = mid
                else:
                    lo = mid
            return (lo + hi) / 2
    return None


def mu_mode(n_tube, n_ring, eps, s):
    """
    Dimensionless energy-squared of a single-sheet mode.

    μ²(n_tube, n_ring) = (n_tube/ε)² + (n_ring − n_tube·s)²

    Parameters
    ----------
    n_tube : int — tube winding number
    n_ring : int — ring winding number
    eps : float — aspect ratio
    s : float — within-plane shear

    Returns
    -------
    float — μ² (dimensionless energy-squared)
    """
    return (n_tube / eps)**2 + (n_ring - n_tube * s)**2


# ══════════════════════════════════════════════════════════════════
#  Spin
# ══════════════════════════════════════════════════════════════════
#
#  Physical spin is TOPOLOGICAL: it depends only on whether each
#  tube winding number is odd or even.  Odd n_tube → spin ½ on
#  that sheet.  This is exact and cannot deviate from half-integers.
#  Use spin_halves() or spin_inferred() for the physical spin.
#
#  The path-integral "spin_Lz" below is a CLASSICAL DIAGNOSTIC:
#  it computes the orbital angular momentum of a geodesic on the
#  torus surface.  This is NOT the quantum spin — it's an embedding-
#  dependent classical quantity that was explored in R49 Track 1.
#  It is retained as a diagnostic tool but should not be used for
#  filtering or treated as the physical spin.
# ══════════════════════════════════════════════════════════════════


def spin_inferred(n_tube, n_ring):
    """
    Inferred spin from topology (exact).

    Spin is determined by whether the tube winding is odd:
      odd n_tube  → spin ½  (fermion)
      even n_tube → spin 0  (boson, or higher integer spin)

    This is a topological invariant — it does not depend on ε,
    shear, or any continuous parameter.  A mode with n_tube = 1
    is spin ½ regardless of the torus geometry.

    Parameters
    ----------
    n_tube : int — tube winding number
    n_ring : int — ring winding number (unused, for API symmetry)

    Returns
    -------
    float — 0.5 if n_tube is odd, 0.0 if even or zero
    """
    return 0.5 if (abs(n_tube) % 2 == 1) else 0.0


_spin_cache = {}
_N_SPIN_SAMPLES = 2048


def _path_integral_I(p, q, eps):
    """
    Path-length integral I(ε) for a (p, q) geodesic on a torus with
    aspect ratio ε.

    I = ∫₀²π √(p²ε² + q²(1 + ε cos(pt))²) dt

    This is the arc length of the classical geodesic, used only
    for the classical angular momentum diagnostic (spin_Lz).
    """
    t = np.linspace(0, _TWO_PI, _N_SPIN_SAMPLES, endpoint=False)
    dt = _TWO_PI / _N_SPIN_SAMPLES
    rho = 1.0 + eps * np.cos(p * t)
    integrand = np.sqrt(p**2 * eps**2 + q**2 * rho**2)
    return float(np.sum(integrand) * dt)


def spin_Lz(n_tube, n_ring, eps):
    """
    Classical orbital angular momentum L_z/ℏ (DIAGNOSTIC ONLY).

    Computes the angular momentum of a classical geodesic on the
    torus surface using the path-integral formula from R49.
    This is NOT the physical spin — see spin_inferred() for that.

    Retained as a diagnostic: deviations from the topological spin
    may indicate something about the geometry, but the physical
    spin is always an exact half-integer from topology.

    Parameters
    ----------
    n_tube : int — tube winding number (sign irrelevant)
    n_ring : int — ring winding number (sign irrelevant)
    eps : float — aspect ratio

    Returns
    -------
    float — classical L_z/ℏ, or 0.0 if n_ring = 0
    """
    p, q = abs(n_tube), abs(n_ring)
    if q == 0:
        return 0.0
    if p == 0:
        return 0.0

    key = (p, q, round(eps, 6))
    if key in _spin_cache:
        return _spin_cache[key]

    I = _path_integral_I(p, q, eps)
    S = 2 * math.pi**2 * q**2 * (2 + eps**2) / I**2
    Lz = S / q

    _spin_cache[key] = Lz
    return Lz


# ══════════════════════════════════════════════════════════════════
#  Waveguide cutoff (R46)
# ══════════════════════════════════════════════════════════════════

def waveguide_propagates(n_tube, n_ring, eps):
    """
    Does a mode propagate on this sheet?

    Waveguide cutoff condition (open boundary):
      n_ring > |n_tube| / ε

    Modes below this threshold are evanescent and cannot sustain
    standing waves on the torus.  Discovered in R46 for Ma_e,
    confirmed for Ma_p (R47) and Ma_ν (R49).

    Parameters
    ----------
    n_tube : int — tube winding number
    n_ring : int — ring winding number
    eps : float — aspect ratio

    Returns
    -------
    bool — True if mode propagates (above cutoff)
    """
    if n_tube == 0 and n_ring == 0:
        return False
    if n_tube == 0:
        return True
    if eps <= 0:
        return False
    return abs(n_ring) >= abs(n_tube) / eps


# ══════════════════════════════════════════════════════════════════
#  6×6 metric construction
# ══════════════════════════════════════════════════════════════════

def _build_circumferences(eps_e, s_e, L_ring_e,
                          eps_nu, s_nu, L_ring_nu,
                          eps_p, s_p, L_ring_p):
    """
    Assemble the 6-vector of circumferences (fm) from per-sheet params.

    L = [L_tube_e, L_ring_e, L_tube_nu, L_ring_nu, L_tube_p, L_ring_p]

    where L_tube = ε × L_ring for each sheet.
    """
    return np.array([
        eps_e * L_ring_e, L_ring_e,
        eps_nu * L_ring_nu, L_ring_nu,
        eps_p * L_ring_p, L_ring_p,
    ])


def _build_metric(L, s_e, s_nu, s_p, sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0):
    """
    Build the 6×6 dimensionless metric G̃ and its inverse.

    Within-plane shears enter through the lattice matrix
    B = diag(L)(I + S), where S has off-diagonal entries
    s₁₂, s₃₄, s₅₆ (upper triangular, tube→ring shear).

    Cross-plane shears σ_ep, σ_eν, σ_νp are injected into
    the off-diagonal blocks of G̃.

    Parameters
    ----------
    L : ndarray(6,) — circumferences in fm
    s_e, s_nu, s_p : float — within-plane shears
    sigma_ep, sigma_enu, sigma_nup : float — cross-plane shears

    Returns
    -------
    (Gt, Gti) — dimensionless metric and its inverse,
    or (None, None) if the metric is not positive-definite.
    """
    S = np.zeros((6, 6))
    S[0, 1] = s_e
    S[2, 3] = s_nu
    S[4, 5] = s_p

    B = np.diag(L) @ (np.eye(6) + S)
    G_phys = B.T @ B

    Gt = np.empty((6, 6))
    for i in range(6):
        for j in range(6):
            Gt[i, j] = G_phys[i, j] / (L[i] * L[j])

    # Cross-shear blocks: ep = (0:2)×(4:6), enu = (0:2)×(2:4), nup = (2:4)×(4:6)
    _CROSS_PAIRS = {
        'ep':  [(0, 4), (0, 5), (1, 4), (1, 5)],
        'enu': [(0, 2), (0, 3), (1, 2), (1, 3)],
        'nup': [(2, 4), (2, 5), (3, 4), (3, 5)],
    }
    for (label, val) in [('ep', sigma_ep), ('enu', sigma_enu), ('nup', sigma_nup)]:
        if val != 0.0:
            for (i, j) in _CROSS_PAIRS[label]:
                Gt[i, j] += val
                Gt[j, i] += val

    eigs = np.linalg.eigvalsh(Gt)
    if np.any(eigs <= 0):
        return None, None

    Gti = np.linalg.inv(Gt)
    return Gt, Gti


# ══════════════════════════════════════════════════════════════════
#  Ring circumference from particle mass
# ══════════════════════════════════════════════════════════════════

def ring_circumference_fm(mass_MeV, eps, s, n_tube, n_ring):
    """
    Compute the ring circumference L_ring (fm) such that mode
    (n_tube, n_ring) on a sheet with aspect ratio ε and shear s
    has the given mass.

    From E = (2πℏc / L_ring) × μ, where μ = √((n_tube/ε)² + (n_ring − n_tube·s)²):

      L_ring = 2πℏc × μ / E

    Parameters
    ----------
    mass_MeV : float — target mass in MeV
    eps : float — aspect ratio
    s : float — within-plane shear
    n_tube, n_ring : int — mode quantum numbers

    Returns
    -------
    float — ring circumference in fm
    """
    mu2 = mu_mode(n_tube, n_ring, eps, s)
    if mu2 <= 0:
        raise ValueError(f"Mode ({n_tube},{n_ring}) has μ² ≤ 0")
    mu = math.sqrt(mu2)
    return _TWO_PI_HC * mu / mass_MeV


# ══════════════════════════════════════════════════════════════════
#  MaD class — the Model-D engine
# ══════════════════════════════════════════════════════════════════

class MaD:
    """
    Model-D Ma geometry.

    All parameters are explicit — nothing is derived from hard-coded
    assumptions.  Each sheet has its own aspect ratio (ε), shear (s),
    and ring circumference (L_ring).

    Parameters
    ----------
    eps_e, eps_nu, eps_p : float — aspect ratios (tube/ring)
    s_e, s_nu, s_p : float — within-plane shears
    L_ring_e, L_ring_nu, L_ring_p : float — ring circumferences (fm)
    sigma_ep : float — electron-proton cross-shear (default 0)
    sigma_enu : float — electron-neutrino cross-shear (default 0)
    sigma_nup : float — neutrino-proton cross-shear (default 0)
    """

    __slots__ = (
        '_eps', '_s', '_L_ring', '_L',
        '_sigma_ep', '_sigma_enu', '_sigma_nup',
        '_Gt', '_Gti',
        '_n_p',
    )

    def __init__(self, *,
                 eps_e, eps_nu, eps_p,
                 s_e, s_nu, s_p,
                 L_ring_e, L_ring_nu, L_ring_p,
                 sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0):

        self._eps = (float(eps_e), float(eps_nu), float(eps_p))
        self._s = (float(s_e), float(s_nu), float(s_p))
        self._L_ring = (float(L_ring_e), float(L_ring_nu), float(L_ring_p))
        self._sigma_ep = float(sigma_ep)
        self._sigma_enu = float(sigma_enu)
        self._sigma_nup = float(sigma_nup)

        self._L = _build_circumferences(
            eps_e, s_e, L_ring_e,
            eps_nu, s_nu, L_ring_nu,
            eps_p, s_p, L_ring_p,
        )

        Gt, Gti = _build_metric(
            self._L, s_e, s_nu, s_p,
            sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup,
        )
        if Gt is None:
            raise ValueError(
                "Metric is not positive-definite at these parameters. "
                "Reduce cross-shear magnitudes.")
        self._Gt = Gt
        self._Gti = Gti
        self._n_p = None  # set by from_physics(); None for raw construction

    # ── Convenience constructors ──────────────────────────────────

    @classmethod
    def from_physics(cls, *,
                     eps_e=0.65, eps_nu=5.0, eps_p=0.55,
                     s_nu=None,
                     n_e=(1, 2), n_p=(1, 3), n_nu=(1, 1),
                     sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0):
        """
        Construct from physical constraints.

        Derives within-plane shears s_e, s_p from α = 1/137 (R19
        formula) and ring circumferences from reference mode masses.

        PARAMETER PROVENANCE (see model-D.md §Parameter strategy)
        ─────────────────────────────────────────────────────────
        These are defaults, not pins.  Each can be overridden.

        eps_e = 0.65   Working value.  Must be > 0.5 for electron
                       (1,2) to clear waveguide cutoff.  R46 suggested
                       ~0.5; raised to 0.65 for 30% margin (R50 F3).
                       Confidence: LOW — not independently constrained.

        eps_nu = 5.0   R49 Assignment A value.  Broadly viable from
                       0.1 to 5+ (R49 F2).  Confidence: LOW — three
                       neutrino families remain viable.

        eps_p = 0.55   For (1,3): must be > 1/3 so the (1,2) ghost is
                       cut and (1,3) is the first surviving mode.  0.55
                       gives good margin.  For (3,6): must be ≥ 0.5 for
                       strands to propagate.  Confidence: LOW.

        s_e, s_p       Derived from α(ε, s) = 1/137.036 (R19).
                       Confidence: HIGH — α is precisely measured and
                       the R19 formula is validated.

        s_nu = 0.022   From R49 Assignment A: Δm²₂₁/(4·Δm²₃₁/ratio).
                       Confidence: MEDIUM — depends on neutrino family.

        n_e = (1,2)    Electron mode.  Confidence: HIGH — established
                       since model-A, waveguide-validated (R46).

        n_p = (1,3)    Leading candidate.  Fundamental mode — gcd = 1,
                       so charge formula is universal (no composite
                       exception needed).  Spin ½ from topological rule
                       (odd tube).  Bare moment ~3 μ_N (−7% correction
                       needed).  Nuclear scaling: n₅ = A, n₆ = 3A.
                       Parallels the electron: first surviving charged
                       mode after (1,2) ghost is killed by waveguide.
                       Confidence: MEDIUM — under active testing (R50
                       Track 5).
                       Alternative: (3,6) composite.  Gives quark
                       substructure (gcd = 3 → three strands) but
                       requires composite charge formula that breaks
                       for nuclear modes (R50 review).  Still viable
                       if charge formula tension is resolved.

        n_nu = (1,1)   Neutrino ν₁ (Assignment A).  Confidence: MEDIUM
                       — depends on neutrino family selection.

        sigma_*= 0.0   Cross-shears.  Confidence: N/A — these are the
                       primary FREE parameters for the particle search.
                       Sweep, don't pin.

        Parameters
        ----------
        eps_e, eps_nu, eps_p : float — aspect ratios
        s_nu : float or None — neutrino shear (None = derive from Δm²)
        n_e : tuple(2,) — electron reference mode
        n_p : tuple(2,) — proton reference mode
        n_nu : tuple(2,) — neutrino reference mode
        sigma_ep, sigma_enu, sigma_nup : float — cross-shears

        Returns
        -------
        MaD instance
        """
        s_e = solve_shear_for_alpha(eps_e)
        if s_e is None:
            raise ValueError(f"No shear solution for eps_e = {eps_e}")
        s_p = solve_shear_for_alpha(eps_p)
        if s_p is None:
            raise ValueError(f"No shear solution for eps_p = {eps_p}")

        L_ring_e = ring_circumference_fm(M_E_MEV, eps_e, s_e, n_e[0], n_e[1])
        L_ring_p = ring_circumference_fm(M_P_MEV, eps_p, s_p, n_p[0], n_p[1])

        if s_nu is None:
            s_nu = DM2_21 / (4 * DM2_31 / (DM2_31 / DM2_21))
            # Simplified: s_nu ≈ 0.022 for Assignment A.
            # More precisely: from R49, s₃₄ such that ratio = 33.6.
            # For (1,1) as ν₁: Δm²₂₁ = 4·s·μ²₁₁ in dimensionless units.
            s_nu = 0.022  # default from R49 Assignment A

        # Neutrino scale: from Δm²₂₁ = 7.53e-5 eV²
        # E₀_ν² = Δm²₂₁ / (4·s_nu)  in eV², then convert to MeV
        E0_nu_sq_eV2 = DM2_21 / (4 * s_nu)
        E0_nu_MeV = math.sqrt(E0_nu_sq_eV2) * 1e-6
        mu2_nu = mu_mode(n_nu[0], n_nu[1], eps_nu, s_nu)
        mu_nu = math.sqrt(mu2_nu)
        L_ring_nu = _TWO_PI_HC * mu_nu / (E0_nu_MeV * mu_nu)
        # Simplifies to: L_ring_nu = 2πℏc / E0_nu
        L_ring_nu = _TWO_PI_HC / E0_nu_MeV

        inst = cls(
            eps_e=eps_e, eps_nu=eps_nu, eps_p=eps_p,
            s_e=s_e, s_nu=s_nu, s_p=s_p,
            L_ring_e=L_ring_e, L_ring_nu=L_ring_nu, L_ring_p=L_ring_p,
            sigma_ep=sigma_ep, sigma_enu=sigma_enu, sigma_nup=sigma_nup,
        )
        inst._n_p = n_p
        return inst

    # ── Properties ────────────────────────────────────────────────

    @property
    def eps(self):
        """Aspect ratios (ε_e, ε_ν, ε_p)."""
        return self._eps

    @property
    def shears(self):
        """Within-plane shears (s_e, s_ν, s_p)."""
        return self._s

    @property
    def L(self):
        """Circumferences [L₁, L₂, L₃, L₄, L₅, L₆] in fm."""
        return self._L.copy()

    @property
    def L_ring(self):
        """Ring circumferences (L_ring_e, L_ring_ν, L_ring_p) in fm."""
        return self._L_ring

    @property
    def sigma_ep(self):
        return self._sigma_ep

    @property
    def sigma_enu(self):
        return self._sigma_enu

    @property
    def sigma_nup(self):
        return self._sigma_nup

    @property
    def proton_mode(self):
        """Proton reference mode (n_tube, n_ring), e.g. (1,3) or (3,6).

        None if constructed via raw __init__ without from_physics().
        """
        return self._n_p

    @property
    def is_composite_proton(self):
        """True if proton mode has gcd > 1 (e.g. (3,6) → 3 strands)."""
        if self._n_p is None:
            return False
        return math.gcd(abs(self._n_p[0]), abs(self._n_p[1])) > 1

    @property
    def metric(self):
        """Dimensionless metric G̃ (6×6)."""
        return self._Gt.copy()

    @property
    def metric_inv(self):
        """Inverse dimensionless metric G̃⁻¹ (6×6)."""
        return self._Gti.copy()

    # ── Mode energy ───────────────────────────────────────────────

    def energy(self, n):
        """
        Mode energy in MeV.

        E² = (2πℏc)² × (n/L)ᵀ G̃⁻¹ (n/L)

        Parameters
        ----------
        n : tuple or array-like (6,) — integer quantum numbers

        Returns
        -------
        float — energy in MeV
        """
        n_arr = np.asarray(n, dtype=float)
        n_tilde = n_arr / self._L
        E2 = _TWO_PI_HC**2 * n_tilde @ self._Gti @ n_tilde
        if E2 < 0:
            raise ValueError(
                f"Negative E² = {E2:.4e} for mode {tuple(int(x) for x in n_arr)}. "
                "Metric may not be positive-definite.")
        return math.sqrt(E2)

    def energy_decomp(self, n):
        """
        Decompose E² into per-sheet and cross-sheet contributions.

        Returns dict with keys: 'total_MeV', 'e', 'nu', 'p',
        'ep', 'enu', 'nup' (all in MeV²), and 'fractions' (dict).
        """
        n_arr = np.asarray(n, dtype=float)
        n_tilde = n_arr / self._L

        blocks = {
            'e':   (slice(0, 2), slice(0, 2)),
            'nu':  (slice(2, 4), slice(2, 4)),
            'p':   (slice(4, 6), slice(4, 6)),
            'ep':  (slice(0, 2), slice(4, 6)),
            'enu': (slice(0, 2), slice(2, 4)),
            'nup': (slice(2, 4), slice(4, 6)),
        }

        E2_total = _TWO_PI_HC**2 * n_tilde @ self._Gti @ n_tilde
        parts = {}
        for key, (r, c_) in blocks.items():
            sub = n_tilde[r] @ self._Gti[r, c_] @ n_tilde[c_]
            cross_factor = 2.0 if key in ('ep', 'enu', 'nup') else 1.0
            parts[key] = _TWO_PI_HC**2 * sub * cross_factor

        total = math.sqrt(max(E2_total, 0))
        fracs = {k: v / E2_total if E2_total > 0 else 0.0 for k, v in parts.items()}

        return {
            'total_MeV': total,
            **parts,
            'fractions': fracs,
        }

    # ── Charge ────────────────────────────────────────────────────

    @staticmethod
    def charge(n):
        """
        Electric charge in units of e (for fundamental modes).

        Q = −n₁ + n₅

        The electron sheet tube winding n₁ carries negative charge
        (electron has n₁ = +1, Q = −1).  The proton sheet tube
        winding n₅ carries positive charge (proton has n₅ = +1,
        Q = +1).  The neutrino sheet (n₃) does not contribute
        — see Q102 (neutrino neutrality from sheet size).

        Under the (1,3) proton hypothesis, this is the only charge
        formula needed (gcd(1,3) = 1 → no composite correction).
        Under the (3,6) proton hypothesis, use charge_composite()
        for modes with gcd > 1.

        Parameters
        ----------
        n : tuple or array-like (6,)

        Returns
        -------
        int — net charge
        """
        return int(-n[0] + n[4])

    @staticmethod
    def charge_composite(n):
        """
        Electric charge for composite modes, in units of e.

        Q = (−n₁ + n₅) / gcd(|n₅|, |n₆|)    [proton sheet composite]

        Only relevant under the (3,6) proton hypothesis.  The (3,6)
        proton is a composite of gcd(3,6) = 3 strands; each strand
        carries charge e/3 (fractional quark charge).  Total charge:
        3 × (e/3) = e → Q = +1.

        Falls back to charge() when gcd = 1 (fundamental mode,
        including the (1,3) proton) or when n₅ = n₆ = 0 (no proton
        sheet winding).

        WARNING: This formula gives incorrect results for nuclear
        modes under the R29 scaling law (n₅ = A, n₆ = 2A), because
        gcd(A, 2A) = A collapses the proton contribution.  See
        R50 Track 5 for details.

        See R47 Track 7 F4 for derivation.

        Parameters
        ----------
        n : tuple or array-like (6,)

        Returns
        -------
        int — net charge (may be fractional for individual strands,
              but integer for full composites)
        """
        Q_raw = int(-n[0] + n[4])
        n5, n6 = abs(int(n[4])), abs(int(n[5]))
        if n5 == 0 and n6 == 0:
            return Q_raw
        g = math.gcd(n5, n6) if (n5 > 0 and n6 > 0) else max(n5, n6)
        if g <= 1:
            return Q_raw
        # Composite: divide proton-sheet contribution by strand count
        Q_e = -int(n[0])           # electron sheet contribution (unchanged)
        Q_p = int(n[4]) // g       # proton sheet: per-strand charge
        return Q_e + Q_p

    # ── Spin ──────────────────────────────────────────────────────

    @staticmethod
    def spin_halves(n):
        """
        Count of spin-½ contributions from odd tube windings.

        Each sheet contributes ½ when its tube winding is odd.
        Total: 0 → boson, 1 → fermion (½), 2 → 0 or 1, 3 → ½ or 3/2.

        This is the TOPOLOGICAL spin — it depends only on whether
        winding numbers are odd or even.  It is always exact and
        always gives half-integers.  Use this for filtering.

        Parameters
        ----------
        n : tuple or array-like (6,)

        Returns
        -------
        int — number of spin-½ contributions
        """
        return sum(abs(n[i]) % 2 for i in (0, 2, 4))

    @staticmethod
    def spin_total(n):
        """
        Total inferred spin from topology (exact half-integer).

        For composite modes (gcd > 1), uses per-strand tube winding.
        E.g. (3,6) proton → strand (1,2); n_tube = 1 is odd → ½.
        For the (1,3) proton, n_tube = 1 is directly odd → ½.

        Parameters
        ----------
        n : tuple or array-like (6,)

        Returns
        -------
        float — total spin (0.0, 0.5, 1.0, 1.5)
        """
        total = 0.0
        for i_tube, i_ring in [(0, 1), (2, 3), (4, 5)]:
            nt, nr = abs(int(n[i_tube])), abs(int(n[i_ring]))
            if nt == 0 and nr == 0:
                continue
            g = math.gcd(nt, nr) if (nt > 0 and nr > 0) else 1
            strand_tube = nt // g if g > 1 else nt
            total += 0.5 if (strand_tube % 2 == 1) else 0.0
        return total

    def spin_Lz_total(self, n):
        """
        Classical angular momentum diagnostic (NOT the physical spin).

        Computes L_z/ℏ from the path integral on the torus surface.
        This is a continuous quantity that depends on ε and will
        never exactly equal a half-integer.  Use spin_total() or
        spin_halves() for the physical (topological) spin.

        For composite modes, computes per-strand.

        Parameters
        ----------
        n : tuple or array-like (6,)

        Returns
        -------
        float — classical L_z/ℏ (diagnostic)
        """
        total = 0.0
        sheets = [(0, 1, 0), (2, 3, 1), (4, 5, 2)]
        for i_tube, i_ring, i_sheet in sheets:
            nt, nr = int(n[i_tube]), int(n[i_ring])
            if nt == 0 and nr == 0:
                continue
            ant, anr = abs(nt), abs(nr)
            g = math.gcd(ant, anr) if (ant > 0 and anr > 0) else 1
            if g > 1:
                total += spin_Lz(nt // g, nr // g, self._eps[i_sheet])
            else:
                total += spin_Lz(nt, nr, self._eps[i_sheet])
        return total

    # ── Waveguide filtering ───────────────────────────────────────

    def propagates(self, n):
        """
        Does mode n propagate on all active sheets?

        A sheet is "active" if either of its quantum numbers is nonzero.
        For each active sheet, checks the waveguide cutoff condition:
          n_ring >= |n_tube| / ε

        For composite modes (gcd(n_tube, n_ring) > 1), checks
        per-strand propagation.  E.g. a (3,6) composite is three
        (1,2) strands; each strand must individually propagate.

        For the (1,3) proton (gcd = 1), the mode is fundamental
        and the standard cutoff applies: n_ring ≥ n_tube/ε → 3 ≥ 1/ε
        → ε ≥ 1/3.  With ε_p = 0.55 this easily propagates.

        A mode with pure n_ring winding (n_tube = 0) always propagates.
        The zero mode (all zeros) does not propagate.

        Parameters
        ----------
        n : tuple or array-like (6,)

        Returns
        -------
        bool
        """
        sheets = [(0, 1, 0), (2, 3, 1), (4, 5, 2)]
        any_active = False
        for i_tube, i_ring, i_sheet in sheets:
            nt, nr = int(n[i_tube]), int(n[i_ring])
            if nt == 0 and nr == 0:
                continue
            any_active = True
            ant, anr = abs(nt), abs(nr)
            g = math.gcd(ant, anr) if (ant > 0 and anr > 0) else 1
            if g > 1:
                # Composite: check per-strand
                if not waveguide_propagates(nt // g, nr // g, self._eps[i_sheet]):
                    return False
            else:
                if not waveguide_propagates(nt, nr, self._eps[i_sheet]):
                    return False
        return any_active

    def active_sheets(self, n):
        """
        Which sheets carry winding for mode n?

        Returns
        -------
        str — concatenation of active sheet labels, e.g. 'e+p', 'nu', 'e+nu+p'
        """
        labels = []
        names = ['e', 'nu', 'p']
        for idx, (i_tube, i_ring) in enumerate([(0, 1), (2, 3), (4, 5)]):
            if n[i_tube] != 0 or n[i_ring] != 0:
                labels.append(names[idx])
        return '+'.join(labels) if labels else 'none'

    # ── Mode scan ─────────────────────────────────────────────────

    def scan_modes(self, n_max=3, E_max_MeV=None,
                   charge=None, spin=None, spin_halves_filter=None,
                   propagating_only=True,
                   compute_spin_Lz=False):
        """
        Brute-force 6D mode scan with filtering.

        Parameters
        ----------
        n_max : int — maximum |nᵢ| per dimension (default 3).
            Complexity is O((2n+1)⁶), so n_max > 4 gets slow.
        E_max_MeV : float or None — energy ceiling
        charge : int or None — required charge (None = any)
        spin : float or None — required topological spin (0.0, 0.5, 1.0, 1.5)
        spin_halves_filter : int or None — required spin-½ count (raw)
        propagating_only : bool — if True (default), exclude modes
            that fail waveguide cutoff on any active sheet
        compute_spin_Lz : bool — if True, compute classical L_z/ℏ
            diagnostic for each mode (slower, not used for filtering)

        Returns
        -------
        list of Mode, sorted by energy
        """
        modes = []
        rng = range(-n_max, n_max + 1)
        for n in iproduct(rng, repeat=6):
            if all(ni == 0 for ni in n):
                continue

            if charge is not None and self.charge(n) != charge:
                continue
            if spin is not None and self.spin_total(n) != spin:
                continue
            if spin_halves_filter is not None and self.spin_halves(n) != spin_halves_filter:
                continue

            prop = self.propagates(n)
            if propagating_only and not prop:
                continue

            try:
                E = self.energy(n)
            except ValueError:
                continue
            if E_max_MeV is not None and E > E_max_MeV:
                continue

            Lz = self.spin_Lz_total(n) if compute_spin_Lz else None

            modes.append(Mode(
                n=n,
                E_MeV=E,
                charge=self.charge(n),
                spin=self.spin_total(n),
                spin_halves=self.spin_halves(n),
                spin_Lz=Lz,
                propagates=prop,
                sheets_active=self.active_sheets(n),
            ))

        modes.sort(key=lambda m: m.E_MeV)
        return modes

    # ── Near-miss finder ──────────────────────────────────────────

    def nearest_modes(self, target_MeV, n_max=3,
                      top_k=10, charge=None, spin=None,
                      spin_halves_filter=None,
                      propagating_only=True, compute_spin_Lz=False):
        """
        Find the modes closest to a target mass.

        Returns the top_k modes sorted by |E − target|.

        Parameters
        ----------
        target_MeV : float — target mass in MeV
        n_max : int — scan range
        top_k : int — how many to return
        charge, spin, spin_halves_filter, propagating_only,
        compute_spin_Lz : same as scan_modes()

        Returns
        -------
        list of NearMiss, sorted by |residual|
        """
        all_modes = self.scan_modes(
            n_max=n_max, E_max_MeV=target_MeV * 3,
            charge=charge, spin=spin,
            spin_halves_filter=spin_halves_filter,
            propagating_only=propagating_only,
            compute_spin_Lz=compute_spin_Lz,
        )

        near = []
        for m in all_modes:
            resid = m.E_MeV - target_MeV
            near.append(NearMiss(
                mode=m,
                residual_MeV=resid,
                residual_frac=abs(resid) / target_MeV if target_MeV > 0 else float('inf'),
            ))

        near.sort(key=lambda x: abs(x.residual_MeV))
        return near[:top_k]

    # ── Immutable update ──────────────────────────────────────────

    def with_params(self, **kwargs):
        """
        Create a new MaD with some parameters changed.

        Accepts any constructor keyword argument.  Unspecified
        parameters are inherited from this instance.

        Returns
        -------
        MaD — new instance with updated parameters.
        """
        defaults = {
            'eps_e': self._eps[0],
            'eps_nu': self._eps[1],
            'eps_p': self._eps[2],
            's_e': self._s[0],
            's_nu': self._s[1],
            's_p': self._s[2],
            'L_ring_e': self._L_ring[0],
            'L_ring_nu': self._L_ring[1],
            'L_ring_p': self._L_ring[2],
            'sigma_ep': self._sigma_ep,
            'sigma_enu': self._sigma_enu,
            'sigma_nup': self._sigma_nup,
        }
        defaults.update(kwargs)
        return MaD(**defaults)

    # ── String representation ─────────────────────────────────────

    def __repr__(self):
        return (
            f"MaD(eps=({self._eps[0]:.4f}, {self._eps[1]:.4f}, {self._eps[2]:.4f}), "
            f"shears=({self._s[0]:.5f}, {self._s[1]:.5f}, {self._s[2]:.5f}), "
            f"σ_ep={self._sigma_ep:.4f}, σ_eν={self._sigma_enu:.4f}, "
            f"σ_νp={self._sigma_nup:.4f})"
        )

    def summary(self):
        """Print a human-readable geometry summary."""
        names = ['Ma_e', 'Ma_ν', 'Ma_p']
        print(f"Model-D Ma geometry")
        print(f"{'─' * 60}")
        for i, name in enumerate(names):
            L_tube = self._L[2 * i]
            L_ring = self._L[2 * i + 1]
            print(f"  {name}:  ε = {self._eps[i]:.4f},  "
                  f"s = {self._s[i]:.5f},  "
                  f"L_ring = {L_ring:.4e} fm,  "
                  f"L_tube = {L_tube:.4e} fm")
        print(f"  Cross-shears: σ_ep = {self._sigma_ep:.4f}, "
              f"σ_eν = {self._sigma_enu:.4f}, "
              f"σ_νp = {self._sigma_nup:.4f}")

        # Reference energies (single-sheet, no cross-coupling)
        print(f"\n  Reference modes (single-sheet energies):")
        n_p = self._n_p or (1, 3)
        for label, n6, name in [
            ('electron', (1, 2, 0, 0, 0, 0), 'e⁻'),
            ('proton',   (0, 0, 0, 0, n_p[0], n_p[1]), 'p'),
            ('ν₁ (A)',   (0, 0, 1, 1, 0, 0), 'ν₁'),
        ]:
            E = self.energy(n6)
            prop = self.propagates(n6)
            Q = self.charge(n6)
            Qc = self.charge_composite(n6)
            sh = self.spin_halves(n6)
            E_str = (f"{E * 1e9:.2f} meV" if E < 1e-3
                     else f"{E:.6f} MeV")
            Q_str = f"Q = {Q:+d}" if Q == Qc else f"Q = {Qc:+d} (raw {Q:+d})"
            print(f"    {name} = {n6}:  E = {E_str},  "
                  f"{Q_str},  spin_½s = {sh},  "
                  f"propagates = {prop}")
        print(f"{'─' * 60}")

    def to_dict(self):
        """Serialize to dict."""
        d = {
            'eps_e': self._eps[0], 'eps_nu': self._eps[1], 'eps_p': self._eps[2],
            's_e': self._s[0], 's_nu': self._s[1], 's_p': self._s[2],
            'L_ring_e': self._L_ring[0], 'L_ring_nu': self._L_ring[1],
            'L_ring_p': self._L_ring[2],
            'sigma_ep': self._sigma_ep, 'sigma_enu': self._sigma_enu,
            'sigma_nup': self._sigma_nup,
        }
        if self._n_p is not None:
            d['n_p'] = list(self._n_p)
        return d

    @classmethod
    def from_dict(cls, d):
        """Reconstruct from dict."""
        d2 = {k: v for k, v in d.items() if k != 'n_p'}
        inst = cls(**d2)
        if 'n_p' in d:
            inst._n_p = tuple(d['n_p'])
        return inst
