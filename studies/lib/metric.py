"""
Pluggable metric for the Ma × S manifold.

A Metric encapsulates the full 9×9 (or 6×6 Ma-only) geometry:
  - 6 circumferences (L₁…L₆)
  - 3 in-sheet shears (s_e, s_ν, s_p)
  - 12 cross-sheet entries (individual σ_ij)
  - 18 Ma-S entries (optional, for α coupling)

Usage:
    from lib.metric import Metric

    # Use a preset
    m = Metric.model_E()

    # Or build custom
    m = Metric(eps_e=397, s_e=2.004, ..., sigma={(1,4): -0.18})

    # Get mode energy
    E = m.mode_energy((1, 2, 0, 0, 0, 0))

    # Get the raw G̃ and G̃⁻¹
    Gt, Gti = m.Gt, m.Gti

Design: the Metric is immutable after construction.  To vary
a parameter, create a new Metric.  This prevents accidental
mutation during searches.
"""

import math
import numpy as np

from lib.ma_model_d import (
    M_E_MEV, M_P_MEV, DM2_21, ALPHA,
    _TWO_PI_HC,
    solve_shear_for_alpha,
    alpha_from_geometry,
)


class Metric:
    """
    Immutable metric for the compact T⁶ manifold.

    Parameters
    ----------
    eps_e, eps_nu, eps_p : float
        Aspect ratios (tube/ring) for each sheet.
    s_e, s_nu, s_p : float
        Within-sheet shears.
    L_ring_e, L_ring_nu, L_ring_p : float or None
        Ring circumferences in fm.  If None, derived from
        reference masses (m_e, m_p, Δm²₂₁) using the given
        (ε, s) and reference modes.
    n_e, n_p, n_nu : tuple(int, int)
        Reference modes for each sheet (used to derive L_ring
        if not provided).
    sigma : dict
        Cross-sheet entries as {(i, j): value} where i, j are
        0-indexed dimension indices.  e.g., {(1, 4): -0.18}
        for e-ring ↔ p-tube.  Missing entries default to 0.
    """

    __slots__ = (
        '_eps', '_s', '_L_ring', '_L', '_sigma',
        '_Gt', '_Gti', '_n_ref', '_valid',
    )

    def __init__(self, *,
                 eps_e, eps_nu, eps_p,
                 s_e, s_nu, s_p,
                 L_ring_e=None, L_ring_nu=None, L_ring_p=None,
                 n_e=(1, 2), n_p=(1, 3), n_nu=(1, 1),
                 sigma=None):

        self._eps = (float(eps_e), float(eps_nu), float(eps_p))
        self._s = (float(s_e), float(s_nu), float(s_p))
        self._n_ref = (n_e, n_nu, n_p)
        self._sigma = dict(sigma) if sigma else {}

        # Derive L_ring from reference masses if not provided
        if L_ring_e is None:
            mu_e = _mu_mode(n_e[0], n_e[1], eps_e, s_e)
            L_ring_e = _TWO_PI_HC * mu_e / M_E_MEV
        if L_ring_p is None:
            mu_p = _mu_mode(n_p[0], n_p[1], eps_p, s_p)
            L_ring_p = _TWO_PI_HC * mu_p / M_P_MEV
        if L_ring_nu is None:
            E0_nu = math.sqrt(DM2_21 / (4 * s_nu)) * 1e-6
            L_ring_nu = _TWO_PI_HC / E0_nu

        self._L_ring = (float(L_ring_e), float(L_ring_nu), float(L_ring_p))

        # Build circumference vector
        self._L = np.array([
            eps_e * L_ring_e, L_ring_e,
            eps_nu * L_ring_nu, L_ring_nu,
            eps_p * L_ring_p, L_ring_p,
        ])

        # Build 6×6 metric
        Gt, Gti = _build_metric_individual(
            self._L, s_e, s_nu, s_p, self._sigma)

        if Gt is None:
            self._valid = False
            self._Gt = None
            self._Gti = None
        else:
            self._valid = True
            self._Gt = Gt
            self._Gti = Gti

    # ── Properties ──────────────────────────────────────────────

    @property
    def valid(self):
        """True if the metric is positive-definite."""
        return self._valid

    @property
    def Gt(self):
        """Dimensionless 6×6 metric G̃ (read-only copy)."""
        return self._Gt.copy() if self._Gt is not None else None

    @property
    def Gti(self):
        """Inverse metric G̃⁻¹ (read-only copy)."""
        return self._Gti.copy() if self._Gti is not None else None

    @property
    def L(self):
        """Circumference vector (6,) in fm (read-only copy)."""
        return self._L.copy()

    @property
    def L_ring(self):
        """Ring circumferences (e, ν, p) in fm."""
        return self._L_ring

    @property
    def eps(self):
        """Aspect ratios (e, ν, p)."""
        return self._eps

    @property
    def shears(self):
        """In-sheet shears (s_e, s_ν, s_p)."""
        return self._s

    @property
    def sigma(self):
        """Cross-sheet entries as dict (read-only copy)."""
        return dict(self._sigma)

    # ── Mode computations ───────────────────────────────────────

    def mode_energy(self, n):
        """
        Energy of a 6-tuple mode in MeV.

        Parameters
        ----------
        n : tuple or array-like (6,)

        Returns
        -------
        float — energy in MeV
        """
        if not self._valid:
            raise ValueError("Metric is not positive-definite")
        n_arr = np.asarray(n, dtype=float)
        n_tilde = n_arr / self._L
        E2 = _TWO_PI_HC ** 2 * n_tilde @ self._Gti @ n_tilde
        return math.sqrt(max(E2, 0))

    def mode_energy_decomp(self, n):
        """
        Decompose E² into per-sheet and cross-sheet contributions.

        Returns dict with keys: 'total_MeV', 'e', 'nu', 'p',
        'ep', 'enu', 'nup' (all in MeV²), and 'fractions'.
        """
        if not self._valid:
            raise ValueError("Metric is not positive-definite")
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

        E2_total = _TWO_PI_HC ** 2 * n_tilde @ self._Gti @ n_tilde
        parts = {}
        for key, (r, c) in blocks.items():
            sub = n_tilde[r] @ self._Gti[r, c] @ n_tilde[c]
            cross = 2.0 if key in ('ep', 'enu', 'nup') else 1.0
            parts[key] = _TWO_PI_HC ** 2 * sub * cross

        total = math.sqrt(max(E2_total, 0))
        fracs = {k: v / E2_total if E2_total > 0 else 0 for k, v in parts.items()}
        return {'total_MeV': total, **parts, 'fractions': fracs}

    @staticmethod
    def charge(n):
        """Electric charge Q = -n₁ + n₅."""
        return int(-n[0] + n[4])

    @staticmethod
    def spin_half_count(n):
        """Count of odd tube windings (0, 1, 2, or 3)."""
        return sum(1 for i in (0, 2, 4) if abs(n[i]) % 2 == 1)

    @staticmethod
    def sheets(n):
        """Which sheets have nonzero windings."""
        s = []
        if any(n[i] != 0 for i in (0, 1)):
            s.append('e')
        if any(n[i] != 0 for i in (2, 3)):
            s.append('ν')
        if any(n[i] != 0 for i in (4, 5)):
            s.append('p')
        return '+'.join(s) if s else 'empty'

    # ── Constructors with varied parameters ─────────────────────

    def with_sigma(self, **updates):
        """
        Return a new Metric with updated cross-sheet entries.

        Usage: m2 = m.with_sigma(**{(1,4): -0.20, (3,5): 0.15})
        """
        new_sigma = dict(self._sigma)
        new_sigma.update(updates)
        return Metric(
            eps_e=self._eps[0], eps_nu=self._eps[1], eps_p=self._eps[2],
            s_e=self._s[0], s_nu=self._s[1], s_p=self._s[2],
            L_ring_e=self._L_ring[0], L_ring_nu=self._L_ring[1],
            L_ring_p=self._L_ring[2],
            n_e=self._n_ref[0], n_nu=self._n_ref[1], n_p=self._n_ref[2],
            sigma=new_sigma,
        )

    # ── Named presets ───────────────────────────────────────────

    @classmethod
    def model_E(cls, sigma=None):
        """
        Model-E geometry (R53/R54).

        E-sheet: ε=397.074, s=2.004200 (R53 Solution D)
        P-sheet: ε=0.55, s=0.162037 (from α at ε_p)
        ν-sheet: ε=5.0, s=0.022 (R49 Family A)

        Cross-shears: σ₄₅=-0.18, σ₄₆=+0.10 (soft, neutron region)
        """
        s_p = solve_shear_for_alpha(0.55, n_tube=1, n_ring=3)
        default_sigma = {(3, 4): -0.18, (3, 5): 0.10}
        if sigma:
            default_sigma.update(sigma)
        return cls(
            eps_e=397.074, eps_nu=5.0, eps_p=0.55,
            s_e=2.004200, s_nu=0.022, s_p=s_p,
            n_e=(1, 2), n_p=(1, 3), n_nu=(1, 1),
            sigma=default_sigma,
        )

    @classmethod
    def model_D(cls, sigma_ep=-0.13):
        """
        Model-D geometry (R50).

        E-sheet: ε=0.65, s from α
        P-sheet: ε=0.55, s from α
        ν-sheet: ε=5.0, s=0.022
        """
        s_e = solve_shear_for_alpha(0.65, n_tube=1, n_ring=2)
        s_p = solve_shear_for_alpha(0.55, n_tube=1, n_ring=3)
        sig = {}
        if sigma_ep != 0:
            for i, j in [(0, 4), (0, 5), (1, 4), (1, 5)]:
                sig[(i, j)] = sigma_ep
        return cls(
            eps_e=0.65, eps_nu=5.0, eps_p=0.55,
            s_e=s_e, s_nu=0.022, s_p=s_p,
            n_e=(1, 2), n_p=(1, 3), n_nu=(1, 1),
            sigma=sig,
        )

    def __repr__(self):
        return (f"Metric(ε=({self._eps[0]:.1f},{self._eps[1]:.1f},"
                f"{self._eps[2]:.2f}), "
                f"s=({self._s[0]:.4f},{self._s[1]:.4f},{self._s[2]:.4f}))")


# ════════════════════════════════════════════════════════════════
#  Internal helpers
# ════════════════════════════════════════════════════════════════

def _mu_mode(nt, nr, eps, s):
    """Dimensionless single-sheet mode energy."""
    return math.sqrt((nt / eps) ** 2 + (nr - nt * s) ** 2)


def _build_metric_individual(L, s_e, s_nu, s_p, sigma):
    """
    Build the 6×6 dimensionless metric with individual cross entries.
    Returns (Gt, Gti) or (None, None) if not positive-definite.
    """
    S = np.zeros((6, 6))
    S[0, 1] = s_e
    S[2, 3] = s_nu
    S[4, 5] = s_p

    B = np.diag(L) @ (np.eye(6) + S)
    Gt = B.T @ B
    for i in range(6):
        for j in range(6):
            Gt[i, j] /= (L[i] * L[j])

    for (i, j), val in sigma.items():
        if val != 0.0:
            Gt[i, j] += val
            Gt[j, i] += val

    eigs = np.linalg.eigvalsh(Gt)
    if np.any(eigs <= 0):
        return None, None

    Gti = np.linalg.inv(Gt)
    return Gt, Gti
