"""
Embedded torus geometry and near-field calculations.

Computes how Ma modes project into 3D space: charge distributions,
E-fields, multipole moments, and interaction energies between
particles.

See embedded.md for the full design spec.


PHYSICAL PICTURE
================

A material sheet (Ma_e, Ma_p, or Ma_ν) is a flat 2-torus with
circumferences L_tube and L_ring.  In 3D it embeds as a torus of
revolution with major radius R = L_ring/(2π) and minor radius
a = L_tube/(2π).

A mode (n₁, n₂) is represented as a charge distribution along the
flat-torus geodesic θ₁ = n₁·t + φ, θ₂ = n₂·t, projected onto the
embedded surface.  This is NOT the true geodesic of the torus of
revolution (see R12 Track 2); it is the physically meaningful path
on the intrinsic flat manifold.

Charge is distributed with uniform weight per parameter step dt
(uniform energy density on the flat torus).


TYPICAL USAGE
=============

    from lib.embedded import EmbeddedSheet, field_at, interaction_energy

    sheet = EmbeddedSheet.from_ma(L, sheet='e')
    pos, dq = sheet.charge_segments(n1=1, n2=2, N=500, Q=-1.0)
    Ex, Ey, Ez = field_at(pos, dq, point=[10.0, 0.0, 0.0])
"""

import math
import numpy as np
from lib.constants import hbar, c, e as _eV_J

# ℏc in MeV·fm (e in constants.py is elementary charge in C = 1 eV in J)
_hbar_c_MeV_fm = hbar * c / (_eV_J * 1e6) * 1e15   # ≈ 197.3 MeV·fm


# ══════════════════════════════════════════════════════════════════════
#  EmbeddedSheet
# ══════════════════════════════════════════════════════════════════════

class EmbeddedSheet:
    """
    One material sheet embedded as a torus of revolution in 3D.

    Immutable after construction.  Holds the embedding geometry
    (R, a) and provides methods to create charge distributions
    and compute multipole moments.

    Parameters
    ----------
    L_tube : float
        Tube circumference in fm (the "minor" circle).
    L_ring : float
        Ring circumference in fm (the "major" circle).
    """

    __slots__ = ('_L_tube', '_L_ring', '_R', '_a')

    def __init__(self, L_tube, L_ring):
        if L_tube <= 0 or L_ring <= 0:
            raise ValueError(
                f"Circumferences must be positive, got L_tube={L_tube}, "
                f"L_ring={L_ring}")
        self._L_tube = float(L_tube)
        self._L_ring = float(L_ring)
        self._R = L_ring / (2 * math.pi)
        self._a = L_tube / (2 * math.pi)

    # ── Properties ────────────────────────────────────────────────

    @property
    def L_tube(self):
        """Tube circumference (fm)."""
        return self._L_tube

    @property
    def L_ring(self):
        """Ring circumference (fm)."""
        return self._L_ring

    @property
    def R(self):
        """Major radius (fm): R = L_ring / (2π)."""
        return self._R

    @property
    def a(self):
        """Minor radius (fm): a = L_tube / (2π)."""
        return self._a

    @property
    def aspect(self):
        """Aspect ratio a/R = L_tube/L_ring."""
        return self._a / self._R

    @property
    def surface_area(self):
        """Torus surface area 4π²Ra (fm²)."""
        return 4 * math.pi**2 * self._R * self._a

    # ── Constructors ──────────────────────────────────────────────

    @classmethod
    def from_circumferences(cls, L_tube, L_ring):
        """Create from explicit circumferences in fm."""
        return cls(L_tube, L_ring)

    @classmethod
    def from_ma(cls, L, sheet='e'):
        """
        Create from a 6-element circumference array (from ma.py).

        Parameters
        ----------
        L : array-like (6,)
            Circumferences [L1, L2, L3, L4, L5, L6] in fm.
        sheet : str
            'e' for electron (L[0], L[1]),
            'nu' for neutrino (L[2], L[3]),
            'p' for proton (L[4], L[5]).
        """
        idx = {'e': (0, 1), 'nu': (2, 3), 'p': (4, 5)}
        if sheet not in idx:
            raise ValueError(f"sheet must be 'e', 'nu', or 'p', got {sheet!r}")
        i_tube, i_ring = idx[sheet]
        return cls(L[i_tube], L[i_ring])

    @classmethod
    def from_aspect_ratio(cls, r, scale_MeV):
        """
        Create from aspect ratio and an energy scale.

        The ring circumference is derived from:
            L_ring = 2πℏc / scale_MeV

        Parameters
        ----------
        r : float
            Aspect ratio (tube/ring = a/R).
        scale_MeV : float
            Energy scale E₀ such that L_ring = 2πℏc / E₀.
        """
        L_ring = 2 * math.pi * _hbar_c_MeV_fm / scale_MeV
        L_tube = r * L_ring
        return cls(L_tube, L_ring)

    # ── Geometry ──────────────────────────────────────────────────

    def torus_point(self, theta1, theta2):
        """
        Map torus angles to 3D Cartesian coordinates.

        Parameters
        ----------
        theta1 : float or ndarray
            Tube angle(s) (poloidal).
        theta2 : float or ndarray
            Ring angle(s) (toroidal).

        Returns
        -------
        ndarray (..., 3) — (x, y, z) positions in fm.
        """
        theta1 = np.asarray(theta1, dtype=float)
        theta2 = np.asarray(theta2, dtype=float)
        cos1 = np.cos(theta1)
        sin1 = np.sin(theta1)
        cos2 = np.cos(theta2)
        sin2 = np.sin(theta2)
        rho = self._R + self._a * cos1
        x = rho * cos2
        y = rho * sin2
        z = self._a * sin1
        return np.stack([x, y, z], axis=-1)

    # ── Charge distribution ───────────────────────────────────────

    def geodesic(self, n1, n2, N=500, phi=0.0):
        """
        Positions along the (n1, n2) flat-torus geodesic.

        Parameters
        ----------
        n1 : int — tube winding number
        n2 : int — ring winding number
        N : int — number of sample points
        phi : float — phase offset (radians)

        Returns
        -------
        ndarray (N, 3) — 3D positions in fm.
        """
        t = np.linspace(0, 2 * math.pi, N, endpoint=False)
        theta1 = n1 * t + phi
        theta2 = n2 * t
        return self.torus_point(theta1, theta2)

    def charge_segments(self, n1, n2, N=500, phi=0.0, Q=1.0,
                        weights=None):
        """
        Discrete charge distribution along the (n1, n2) geodesic.

        Parameters
        ----------
        n1, n2 : int — winding numbers
        N : int — number of charge segments
        phi : float — phase offset (radians)
        Q : float — total charge (units of e)
        weights : ndarray (N,) or None
            Custom per-segment weights.  If None, uniform weight
            (= uniform energy density on the flat torus).  Weights
            are normalized so that Σ dq = Q.

        Returns
        -------
        pos : ndarray (N, 3) — segment midpoints in fm
        dq : ndarray (N,) — charge per segment (units of e)
        """
        pos = self.geodesic(n1, n2, N, phi)
        if weights is None:
            dq = np.full(N, Q / N)
        else:
            weights = np.asarray(weights, dtype=float)
            if weights.shape != (N,):
                raise ValueError(
                    f"weights shape {weights.shape} != ({N},)")
            dq = Q * weights / weights.sum()
        return pos, dq

    # ── Multipoles ────────────────────────────────────────────────

    def monopole(self, pos, dq):
        """Total charge (units of e)."""
        return float(np.sum(dq))

    def dipole(self, pos, dq):
        """
        Electric dipole moment about the torus center (origin).

        Returns
        -------
        ndarray (3,) — dipole vector d = Σ dq_i × r_i (units of e·fm).
        """
        pos = np.asarray(pos, dtype=float)
        dq = np.asarray(dq, dtype=float)
        return dq @ pos

    def quadrupole(self, pos, dq):
        """
        Traceless electric quadrupole tensor about the origin.

        Returns
        -------
        ndarray (3, 3) — Q_ij = Σ dq_k (3 r_ki r_kj − r_k² δ_ij)
                          (units of e·fm²).
        """
        pos = np.asarray(pos, dtype=float)
        dq = np.asarray(dq, dtype=float)
        r2 = np.sum(pos**2, axis=1)                  # (N,)
        # outer product per charge element, weighted
        Q_raw = np.einsum('k,ki,kj->ij', dq, pos, pos)  # (3,3)
        trace_part = np.einsum('k,k->', dq, r2)          # scalar
        return 3 * Q_raw - trace_part * np.eye(3)

    def multipoles(self, pos, dq, l_max=4):
        """
        Spherical multipole moments q_lm about the origin.

        Uses the real spherical harmonic expansion.  For l=0 this
        is the monopole; l=1 the dipole; l=2 the quadrupole.

        Parameters
        ----------
        pos : ndarray (N, 3)
        dq : ndarray (N,)
        l_max : int — maximum multipole order

        Returns
        -------
        dict mapping (l, m) → float (real spherical harmonic coefficient,
        units of e·fm^l).
        """
        pos = np.asarray(pos, dtype=float)
        dq = np.asarray(dq, dtype=float)
        r = np.sqrt(np.sum(pos**2, axis=1))
        # Avoid division by zero for charges at origin
        r_safe = np.where(r > 0, r, 1.0)
        cos_theta = np.where(r > 0, pos[:, 2] / r_safe, 0.0)
        phi_angle = np.arctan2(pos[:, 1], pos[:, 0])

        from scipy.special import sph_harm_y

        result = {}
        theta_polar = np.arccos(np.clip(cos_theta, -1, 1))
        for l in range(l_max + 1):
            for m in range(-l, l + 1):
                # sph_harm_y(l, m, theta, phi) — complex spherical harmonic
                Y = sph_harm_y(l, abs(m), theta_polar, phi_angle)
                if m < 0:
                    Yr = np.sqrt(2) * (-1)**m * Y.imag
                elif m == 0:
                    Yr = Y.real
                else:
                    Yr = np.sqrt(2) * (-1)**m * Y.real
                result[(l, m)] = float(np.sum(dq * r**l * Yr))
        return result

    def __repr__(self):
        return (f"EmbeddedSheet(L_tube={self._L_tube:.4f}, "
                f"L_ring={self._L_ring:.4f}, "
                f"a/R={self.aspect:.3f})")


# ══════════════════════════════════════════════════════════════════════
#  Free functions — fields, interactions
# ══════════════════════════════════════════════════════════════════════

def field_at(pos, dq, point, eps=0.0):
    """
    Electric field at a point from a charge distribution.

    E(P) = Σ_i dq_i (P − r_i) / (|P − r_i|² + ε²)^{3/2}

    Parameters
    ----------
    pos : ndarray (N, 3) — source positions (fm)
    dq : ndarray (N,) — charges (units of e)
    point : array-like (3,) — field point (fm)
    eps : float — softening length (fm).  Use 0 for inter-particle
          fields; nonzero only for self-energy.

    Returns
    -------
    ndarray (3,) — E-field in units of e/(4πε₀ fm²).

    Notes
    -----
    The 1/(4πε₀) prefactor is NOT included.  The returned value is
    the "geometric" field: multiply by e/(4πε₀) to get SI units.
    """
    pos = np.asarray(pos, dtype=float)
    dq = np.asarray(dq, dtype=float)
    point = np.asarray(point, dtype=float)
    dr = point - pos                                   # (N, 3)
    dist2 = np.sum(dr**2, axis=1) + eps**2             # (N,)
    inv_dist3 = dist2**(-1.5)                          # (N,)
    return np.einsum('i,ij,i->j', dq, dr, inv_dist3)  # (3,)


def field_at_points(pos, dq, points, eps=0.0):
    """
    Electric field at multiple points (vectorized).

    Parameters
    ----------
    pos : ndarray (N, 3) — source positions
    dq : ndarray (N,) — charges
    points : ndarray (M, 3) — field points
    eps : float — softening length

    Returns
    -------
    ndarray (M, 3) — E-field at each point.
    """
    pos = np.asarray(pos, dtype=float)
    dq = np.asarray(dq, dtype=float)
    points = np.asarray(points, dtype=float)
    # dr[m, n, :] = points[m] - pos[n]
    dr = points[:, None, :] - pos[None, :, :]       # (M, N, 3)
    dist2 = np.sum(dr**2, axis=2) + eps**2           # (M, N)
    inv_dist3 = dist2**(-1.5)                        # (M, N)
    # E[m, j] = Σ_n dq[n] * dr[m, n, j] * inv_dist3[m, n]
    weighted = dq[None, :] * inv_dist3               # (M, N)
    return np.einsum('mn,mnj->mj', weighted, dr)     # (M, 3)


def potential_at(pos, dq, point, eps=0.0):
    """
    Electric potential at a point from a charge distribution.

    V(P) = Σ_i dq_i / √(|P − r_i|² + ε²)

    Parameters
    ----------
    pos : ndarray (N, 3) — source positions (fm)
    dq : ndarray (N,) — charges (units of e)
    point : array-like (3,) — field point (fm)
    eps : float — softening length (fm)

    Returns
    -------
    float — potential in units of e/(4πε₀ fm).
    """
    pos = np.asarray(pos, dtype=float)
    dq = np.asarray(dq, dtype=float)
    point = np.asarray(point, dtype=float)
    dr = point - pos
    dist = np.sqrt(np.sum(dr**2, axis=1) + eps**2)
    return float(np.sum(dq / dist))


def field_energy(pos, dq, eps):
    """
    Electrostatic self-energy of a charge distribution.

    U = ½ Σ_{i≠j} dq_i dq_j / |r_i − r_j|

    Parameters
    ----------
    pos : ndarray (N, 3)
    dq : ndarray (N,)
    eps : float — softening length (required; must be > 0 for
          self-energy to be finite)

    Returns
    -------
    float — self-energy in units of e²/(4πε₀ fm).
    """
    if eps <= 0:
        raise ValueError("eps must be > 0 for self-energy calculation")
    pos = np.asarray(pos, dtype=float)
    dq = np.asarray(dq, dtype=float)
    N = len(dq)
    U = 0.0
    # Use pairwise to avoid N² memory for large N
    for i in range(N):
        dr = pos[i + 1:] - pos[i]                       # (N-i-1, 3)
        dist = np.sqrt(np.sum(dr**2, axis=1) + eps**2)  # (N-i-1,)
        U += np.sum(dq[i] * dq[i + 1:] / dist)
    return float(U)


def interaction_energy(pos1, dq1, pos2, dq2):
    """
    Electrostatic interaction energy between two charge distributions.

    U = Σ_i Σ_j dq1_i × dq2_j / |r1_i − r2_j|

    No softening (eps=0): the distributions are on different particles
    so no coincident points.

    Parameters
    ----------
    pos1 : ndarray (N1, 3), dq1 : ndarray (N1,)
    pos2 : ndarray (N2, 3), dq2 : ndarray (N2,)

    Returns
    -------
    float — interaction energy in units of e²/(4πε₀ fm).
    """
    pos1 = np.asarray(pos1, dtype=float)
    dq1 = np.asarray(dq1, dtype=float)
    pos2 = np.asarray(pos2, dtype=float)
    dq2 = np.asarray(dq2, dtype=float)
    # dr[i, j, :] = pos1[i] - pos2[j]
    dr = pos1[:, None, :] - pos2[None, :, :]     # (N1, N2, 3)
    dist = np.sqrt(np.sum(dr**2, axis=2))         # (N1, N2)
    # dq1[i] * dq2[j] / dist[i, j], summed
    return float(np.einsum('i,j,ij->', dq1, dq2, 1.0 / dist))


# ══════════════════════════════════════════════════════════════════════
#  Interaction sweep and force
# ══════════════════════════════════════════════════════════════════════

class SweepResult:
    """
    Result of an interaction energy sweep over distance and phase.

    Attributes
    ----------
    d_values : ndarray (Nd,) — separation distances (fm)
    phi_values : ndarray (Nphi,) — phase offsets (radians)
    U : ndarray (Nd, Nphi) — interaction energy at each (d, Δφ)
        in units of e²/(4πε₀ fm)
    U_coulomb : ndarray (Nd,) — point-charge Coulomb energy Q1*Q2/d
    ratio : ndarray (Nd, Nphi) — U / U_coulomb
    """

    __slots__ = ('d_values', 'phi_values', 'U', 'U_coulomb', 'ratio')

    def __init__(self, d_values, phi_values, U, U_coulomb):
        self.d_values = d_values
        self.phi_values = phi_values
        self.U = U
        self.U_coulomb = U_coulomb
        with np.errstate(divide='ignore', invalid='ignore'):
            self.ratio = np.where(U_coulomb[:, None] != 0,
                                  U / U_coulomb[:, None],
                                  np.nan)


def interaction_sweep(sheet1, sheet2, n1, n2, N, Q1, Q2,
                      d_values, phi_values, axis=2):
    """
    Sweep interaction energy over separation and relative phase.

    Computes U(d, Δφ) for all combinations.  Particle 1 is at the
    origin with phase φ=0.  Particle 2 is displaced by d along the
    specified axis with phase Δφ.

    Uses the phase-reuse optimization: precompute trig arrays once,
    then for each Δφ use angle-addition identities instead of
    recomputing the full geodesic.

    Parameters
    ----------
    sheet1, sheet2 : EmbeddedSheet
        Geometry for particles 1 and 2 (may be different sheets).
    n1, n2 : int
        Winding numbers (same for both particles).
    N : int
        Number of charge segments per particle.
    Q1, Q2 : float
        Total charges (units of e).
    d_values : array-like (Nd,)
        Separation distances (fm).
    phi_values : array-like (Nphi,)
        Relative phase offsets (radians).
    axis : int (0, 1, or 2)
        Separation axis: 0=x, 1=y, 2=z (default z).

    Returns
    -------
    SweepResult
    """
    d_values = np.asarray(d_values, dtype=float)
    phi_values = np.asarray(phi_values, dtype=float)

    # Particle 1: fixed at origin, phase 0
    pos1, dq1 = sheet1.charge_segments(n1, n2, N, phi=0.0, Q=Q1)

    # Precompute trig bases for particle 2 phase rotation
    t = np.linspace(0, 2 * math.pi, N, endpoint=False)
    n1t = n1 * t
    cos_n1t = np.cos(n1t)
    sin_n1t = np.sin(n1t)
    cos_n2t = np.cos(n2 * t)
    sin_n2t = np.sin(n2 * t)

    Nd = len(d_values)
    Nphi = len(phi_values)
    U = np.empty((Nd, Nphi))

    for j, phi in enumerate(phi_values):
        # Angle-addition: cos(n1*t + phi), sin(n1*t + phi)
        cos_phi = math.cos(phi)
        sin_phi = math.sin(phi)
        cos_th1 = cos_n1t * cos_phi - sin_n1t * sin_phi
        sin_th1 = sin_n1t * cos_phi + cos_n1t * sin_phi

        # Build particle 2 positions at this phase
        rho2 = sheet2.R + sheet2.a * cos_th1
        x2 = rho2 * cos_n2t
        y2 = rho2 * sin_n2t
        z2 = sheet2.a * sin_th1
        pos2 = np.stack([x2, y2, z2], axis=-1)       # (N, 3)
        dq2 = np.full(N, Q2 / N)

        for i, d in enumerate(d_values):
            pos2_shifted = pos2.copy()
            pos2_shifted[:, axis] += d
            U[i, j] = interaction_energy(pos1, dq1, pos2_shifted, dq2)

    U_coulomb = Q1 * Q2 / d_values

    return SweepResult(d_values, phi_values, U, U_coulomb)


def interaction_force(pos1, dq1, pos2, dq2, axis=2, eps_d=0.01):
    """
    Force between two charge distributions along an axis.

    F(d) = −∂U/∂d, computed by central finite difference.

    Parameters
    ----------
    pos1, dq1 : source particle 1
    pos2, dq2 : source particle 2 (at current separation)
    axis : int — axis along which to compute force (0=x, 1=y, 2=z)
    eps_d : float — finite difference step (fm)

    Returns
    -------
    float — force in units of e²/(4πε₀ fm²).  Positive = repulsive
            (pushes particle 2 further along axis).
    """
    pos2_plus = np.array(pos2, dtype=float)
    pos2_minus = np.array(pos2, dtype=float)
    pos2_plus[:, axis] += eps_d
    pos2_minus[:, axis] -= eps_d
    U_plus = interaction_energy(pos1, dq1, pos2_plus, dq2)
    U_minus = interaction_energy(pos1, dq1, pos2_minus, dq2)
    return -(U_plus - U_minus) / (2 * eps_d)


# ══════════════════════════════════════════════════════════════════════
#  Near-field correction extraction
# ══════════════════════════════════════════════════════════════════════

class NearFieldResult:
    """
    Near-field correction extracted from a sweep.

    Attributes
    ----------
    U_avg : ndarray (Nd,)
        Phase-averaged interaction energy ⟨U⟩_φ at each distance.
    delta_U : ndarray (Nd, Nphi)
        Deviation from phase average: U(d, Δφ) − ⟨U⟩_φ(d).
    delta_U_pi : ndarray (Nd,) or None
        delta_U at the Δφ closest to π (if π is in the sweep).
    barrier_factor : ndarray (Nd,)
        U at Δφ nearest π, divided by U_coulomb.  Values < 1 mean
        the anti-phase configuration reduces the Coulomb barrier.
    """

    __slots__ = ('U_avg', 'delta_U', 'delta_U_pi', 'barrier_factor')

    def __init__(self, U_avg, delta_U, delta_U_pi, barrier_factor):
        self.U_avg = U_avg
        self.delta_U = delta_U
        self.delta_U_pi = delta_U_pi
        self.barrier_factor = barrier_factor


def near_field_correction(result):
    """
    Extract phase-dependent near-field corrections from a sweep.

    Parameters
    ----------
    result : SweepResult

    Returns
    -------
    NearFieldResult
    """
    U_avg = np.mean(result.U, axis=1)                     # (Nd,)
    delta_U = result.U - U_avg[:, None]                    # (Nd, Nphi)

    # Find the phi index closest to π
    idx_pi = int(np.argmin(np.abs(result.phi_values - math.pi)))
    delta_U_pi = delta_U[:, idx_pi]                        # (Nd,)

    U_at_pi = result.U[:, idx_pi]
    with np.errstate(divide='ignore', invalid='ignore'):
        barrier_factor = np.where(
            result.U_coulomb != 0,
            U_at_pi / result.U_coulomb,
            np.nan)

    return NearFieldResult(U_avg, delta_U, delta_U_pi, barrier_factor)
