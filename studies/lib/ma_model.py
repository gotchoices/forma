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

    m = Ma(r_e=6.6, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906)
    m.energy((1, 2, 0, 0, 0, 0))       # electron energy (MeV)
    m.charge((1, 2, 0, 0, 0, 0))       # -1
    m.L                                  # circumferences (fm)

    # Self-consistent (m_e, m_p exact):
    m = Ma(r_e=6.6, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906,
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
Mode = namedtuple('Mode', ['n', 'E_MeV', 'charge', 'spin_halves'])


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
        '_self_consistent',
        '_L', '_Gt', '_Gti',
        '_converged', '_iterations',
    )

    def __init__(self, r_e, r_nu, r_p, *,
                 sigma_ep=0.0, sigma_enu=0.0, sigma_nup=0.0,
                 cross_shears=None, self_consistent=False):
        self._r_e = float(r_e)
        self._r_nu = float(r_nu)
        self._r_p = float(r_p)
        self._self_consistent = bool(self_consistent)

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
    def params(self):
        """Dict of all input parameters."""
        d = {
            'r_e': self._r_e, 'r_nu': self._r_nu, 'r_p': self._r_p,
            'sigma_ep': self.sigma_ep,
            'sigma_enu': self.sigma_enu,
            'sigma_nup': self.sigma_nup,
            'self_consistent': self._self_consistent,
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

        Parameters
        ----------
        n : tuple or array-like (6,) — integer quantum numbers
            (n₁, n₂, n₃, n₄, n₅, n₆).

        Returns
        -------
        float — energy in MeV.
        """
        return _mode_energy(n, self._Gti, self._L)

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
            E = _mode_energy(n, self._Gti, self._L)
            if E_max_MeV is not None and E > E_max_MeV:
                continue
            modes.append(Mode(n=n, E_MeV=E,
                              charge=_mode_charge(n),
                              spin_halves=_mode_spin(n)))
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
        }
        defaults.update(kwargs)
        return Ma(**defaults)

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
        lines = [
            "Ma geometry",
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
        return "\n".join(lines)

    def __repr__(self):
        sc = ", self_consistent=True" if self._self_consistent else ""
        return (f"Ma(r_e={self._r_e}, r_nu={self._r_nu}, r_p={self._r_p}, "
                f"sigma_ep={self.sigma_ep}{sc})")


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


def _stub_energy_decomp(self, n):
    """
    Decompose mode energy² into sheet and cross-coupling contributions.

    Partitions the quadratic form E² = (2πℏc)² ñᵀ G̃⁻¹ ñ into:

        E² = E²_e + E²_ν + E²_p + 2·E²_eν + 2·E²_ep + 2·E²_νp

    where each term uses the corresponding 2×2 block of G̃⁻¹.

    **Interpretation caveat:** These blocks come from the INVERSE
    metric, not the metric itself.  Due to the Schur complement,
    [G̃⁻¹]_{ee} includes information from all sheets.  The
    decomposition is mathematically well-defined (terms sum to E²)
    but "97% proton-sheet" means "97% of E² comes from the p-block
    of the inverse metric," not that the proton sheet contributes
    97% of the energy in some physical sense.

    Parameters
    ----------
    n : tuple (6,) — mode quantum numbers

    Returns
    -------
    EnergyDecomp namedtuple with fields:
        total (float, MeV), e_sheet, nu_sheet, p_sheet,
        ep_cross, enu_cross, nup_cross (all float, MeV²),
        fractions (dict str → float)
    """
    raise NotImplementedError(
        "Energy decomposition not yet implemented. "
        "See ma-model.md §Feature 3.")


def _stub_jacobian(self, n):
    """
    Analytical Jacobian ∂E/∂θ for a mode.

    Computes the derivative of mode energy with respect to each
    geometry parameter (r_e, r_nu, r_p, sigma_ep, sigma_enu,
    sigma_nup) using:

        ∂E/∂θ = (2πℏc)² / (2E) · ñᵀ (∂G̃⁻¹/∂θ) ñ

    For cross-shears: ∂G̃⁻¹/∂σ = −G̃⁻¹ (∂G̃/∂σ) G̃⁻¹, where
    ∂G̃/∂σ has only 4 nonzero entries per block.

    For aspect ratios: the chain r → s (implicit via
    solve_shear_for_alpha) → L → G̃ → G̃⁻¹ requires implicit
    differentiation: ∂s/∂r = −(∂α/∂r)/(∂α/∂s), both analytically
    available from the α formula.

    When self_consistent=True, L depends on σ through the
    fixed-point iteration.  The total derivative dE/dσ must
    include this indirect path.

    Parameters
    ----------
    n : tuple (6,) — mode quantum numbers

    Returns
    -------
    dict mapping parameter name → float (MeV per unit parameter).
    """
    raise NotImplementedError(
        "Analytical Jacobian not yet implemented. "
        "See ma-model.md §Feature 4.")


def _stub_sensitivity(self, n):
    """
    Human-readable sensitivity report for a mode.

    Wraps jacobian() into a formatted summary showing which
    parameters the mode energy depends on and how strongly.

    Example output:
        Neutron (0,−2,+1,0,0,+2)  E = 939.6 MeV
          r_e:        ∂E/∂r_e  = −0.02 MeV/unit   (weak)
          r_p:        ∂E/∂r_p  = −48.3 MeV/unit   (strong)
          sigma_ep:   ∂E/∂σ_ep = −14.2 MeV/unit   (strong)
          r_nu:       ∂E/∂r_ν  =  0.00 MeV/unit   (negligible)

    Parameters
    ----------
    n : tuple (6,) — mode quantum numbers

    Returns
    -------
    str — formatted report.
    """
    raise NotImplementedError(
        "Sensitivity report not yet implemented. "
        "See ma-model.md §Feature 6.")


def _stub_fit(cls, targets, free_params, fixed_params=None):
    """
    Inverse solver: find geometry parameters matching target masses.

    Uses Gauss-Newton / Levenberg-Marquardt with the analytical
    Jacobian (Feature 4) to minimize Σ (E_computed − E_target)².

    Handles degeneracies: when free_params > targets, reports the
    null space of the Jacobian (parameter combinations that leave
    all targets unchanged).

    Parameters
    ----------
    targets : list of Target(n, mass_MeV) — mode assignments + masses
    free_params : list of str — parameter names to optimize
    fixed_params : dict or None — fixed parameter values

    Returns
    -------
    FitResult with fields:
        params (dict), residuals (list), ma (Ma instance),
        jacobian (ndarray), cov (ndarray or None if underdetermined),
        null_space (ndarray or None)
    """
    raise NotImplementedError(
        "Inverse solver not yet implemented. "
        "See ma-model.md §Feature 5.")


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
