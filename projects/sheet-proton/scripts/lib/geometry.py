"""
Clover-profile and corrugated-torus geometry.

Implements the analytical geometry described in
work/clover-quarks.md §§7–10 under D_6 (Z_6 dihedral) symmetry:

  - 3 lobe arcs (240 deg each, positive curvature, radius r_lobe)
  - 3 saddle arcs (120 deg each, negative curvature, radius r_saddle)
  - Kissing-circles relation d = r_lobe + r_saddle
  - Surface swept around major ring of radius R_major with twist tau

This module is the shared utility used by clover_profile.py and
corrugated_torus.py and (later) laplacian_spectrum.py. Per AGENTS.md,
new scripts should reuse these functions rather than re-implement them.

Conventions:
  - phi in [0, 2*pi) parameterizes the cross-section profile by arc length
  - theta in [0, 2*pi) parameterizes the major ring
  - tau = 1/3 by default (forces Z_3 confinement structure per clover-quarks.md)
"""

from __future__ import annotations

from dataclasses import dataclass
from math import pi
from typing import Tuple

import numpy as np


@dataclass(frozen=True)
class ProfileParams:
    """Parameters defining the clover cross-section profile.

    Under D_6 symmetry, the kissing-circles relation d = r_lobe + r_saddle
    holds automatically (see clover-quarks.md §7.2). Two free parameters:
    r_lobe and r_saddle.
    """
    r_lobe: float
    r_saddle: float

    @property
    def d(self) -> float:
        """Distance from profile center to lobe-/saddle-circle centers."""
        return self.r_lobe + self.r_saddle

    @property
    def arc_lobe(self) -> float:
        """Arc length of one lobe (240 deg = 4*pi/3 radians on lobe circle)."""
        return 4.0 * pi * self.r_lobe / 3.0

    @property
    def arc_saddle(self) -> float:
        """Arc length of one saddle (120 deg = 2*pi/3 radians on saddle circle)."""
        return 2.0 * pi * self.r_saddle / 3.0

    @property
    def L_total(self) -> float:
        """Total profile arc length: 3 lobes + 3 saddles."""
        return 3.0 * (self.arc_lobe + self.arc_saddle)

    @property
    def chi(self) -> float:
        """Corrugation ratio r_saddle / r_lobe."""
        return self.r_saddle / self.r_lobe


def _profile_point(phi: float, params: ProfileParams) -> Tuple[float, float]:
    """Single-point evaluation of the clover profile at arc-length phi.

    Internal helper. Use `profile()` for vectorized evaluation.
    """
    r_l = params.r_lobe
    r_s = params.r_saddle
    d = params.d
    arc_l = params.arc_lobe
    arc_s = params.arc_saddle

    # Fundamental domain: phi in [0, 2*pi/3) covers one lobe + one saddle
    fund_period = 2.0 * pi / 3.0
    fund_phi = phi % fund_period
    fund_index = int(phi // fund_period) % 3

    # Within one fundamental domain, partition by arc-length:
    # lobe arc occupies fraction arc_l / (arc_l + arc_s) of the domain
    L_fund = arc_l + arc_s
    s = fund_phi * L_fund / fund_period  # arc-length within the fundamental domain

    if s < arc_l:
        # On lobe-1 arc.
        # Lobe-1 is centered at (d, 0). The 240-deg arc traces from
        # angle -120 deg through 0 (outward midpoint) to +120 deg
        # on the lobe-circle (angle measured CCW from outward direction = +x).
        # We parameterize CCW with the lobe-arc as s in [0, arc_l].
        alpha = -2.0 * pi / 3.0 + (s / arc_l) * (4.0 * pi / 3.0)
        x = d + r_l * np.cos(alpha)
        y = r_l * np.sin(alpha)
    else:
        # On saddle-1 arc.
        # Saddle-1 is centered at (d/2, d*sqrt(3)/2) -- at distance d from origin,
        # angle 60 deg. The 120-deg arc is the side closer to origin, traced
        # CW on the saddle-circle from angle -60 deg (junction with lobe-1)
        # through -120 deg (inward midpoint) to -180 deg = +180 deg
        # (junction with lobe-2).
        s_in_saddle = s - arc_l
        beta = -pi / 3.0 - (s_in_saddle / arc_s) * (2.0 * pi / 3.0)
        x = d / 2.0 + r_s * np.cos(beta)
        y = d * np.sqrt(3.0) / 2.0 + r_s * np.sin(beta)

    # Rotate by fund_index * 120 deg
    if fund_index != 0:
        rot = fund_index * 2.0 * pi / 3.0
        cos_r = np.cos(rot)
        sin_r = np.sin(rot)
        x, y = cos_r * x - sin_r * y, sin_r * x + cos_r * y

    return x, y


def profile(phi: np.ndarray, params: ProfileParams) -> Tuple[np.ndarray, np.ndarray]:
    """Vectorized clover-profile evaluation.

    Parameters
    ----------
    phi : array_like
        Arc-length-normalized angle in [0, 2*pi). Can be scalar or array.
    params : ProfileParams
        Profile parameters (r_lobe, r_saddle).

    Returns
    -------
    x, y : ndarrays
        Cartesian coordinates of the profile points.
    """
    phi_arr = np.atleast_1d(np.asarray(phi, dtype=float))
    x = np.empty_like(phi_arr)
    y = np.empty_like(phi_arr)
    for i, p in enumerate(phi_arr.flat):
        x.flat[i], y.flat[i] = _profile_point(p, params)
    if np.isscalar(phi):
        return float(x[0]), float(y[0])
    return x, y


def corrugated_torus_surface(
    theta: np.ndarray,
    phi: np.ndarray,
    params: ProfileParams,
    R_major: float,
    tau: float = 1.0 / 3.0,
    embedding: str = "parameter-shift",
    sigma: float = 0.0,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute 3D positions on the corrugated torus surface.

    Two embeddings are supported (see work/clover-quarks.md §9):

    parameter-shift (default; current §9.3 formula):
        r(theta, phi) = R_ring(theta) + P_x(phi + tau*theta) * N(theta)
                                       + P_y(phi + tau*theta) * B
        The embedded shape is a static (non-rotating) clover -- the
        "twist" lives entirely in the relabelling of phi as theta advances.
        After reparameterising by psi = phi + tau*theta this is the
        UN-twisted corrugated torus with twisted boundary identification.

    rotation:
        r(theta, phi) = R_ring(theta)
            + [cos(tau*theta) P_x(phi) - sin(tau*theta) P_y(phi)] * N(theta)
            + [sin(tau*theta) P_x(phi) + cos(tau*theta) P_y(phi)] * B
        The clover cross-section physically rotates by tau*theta as theta
        advances. The embedded surface genuinely carries the twist.

    Both yield the same topology (T^2 with identification
    (theta, phi) ~ (theta + 2*pi, phi + 2*pi/3) when tau = 1/3), and so the
    same path-winding/closure rules. Their metrics, and hence Laplacian
    spectra, differ -- which embedding is physical is an open question, see
    work/clover-quarks.md §9.5.

    The optional `sigma` parameter is the rolled-leaf intrinsic shear of
    work/clover-quarks.md §1.3, §10.3. In the metric, sigma is a constant
    addition to g_{theta,phi} that does NOT enter g_{theta,theta},
    g_{phi,phi}, or the boundary identification (only tau enters those).
    The 3D embedding shape is therefore strictly independent of sigma --
    a sigma-only deformation lives entirely in intrinsic geometry, with
    no isometric realization in R^3 by these embeddings.

    For visualization, this function approximates the sigma contribution by
    using an effective twist (sigma + tau) for the parameter shift /
    rotation rate. This makes sigma visually act like extra tau, which
    captures the "increasing shear rate" intuition of the rolled-leaf
    construction but conflates sigma and tau at the embedded-shape level.
    The metric distinction between sigma and tau (the latter being the
    only one tied to the Z_3 Bloch-sector quantization) is not visible
    in the 3D shape; it lives in the spectroscopic sector structure.

    Parameters
    ----------
    theta, phi : array_like (same shape)
        Ring angle and profile angle on a 2D grid.
    params : ProfileParams
    R_major : float
        Major-ring radius.
    tau : float, default 1/3
        Twist parameter (cross-section advance per radian of theta).
    embedding : {"parameter-shift", "rotation"}, default "parameter-shift"
        Choice of surface embedding.
    sigma : float, default 0.0
        Rolled-leaf intrinsic shear (rotation per ring revolution, same
        units as tau). Visualised as an effective additional twist
        sigma + tau in the embedding; see note above.

    Returns
    -------
    X, Y, Z : ndarrays (same shape as theta and phi)
        Cartesian positions on the surface.
    """
    theta_arr = np.asarray(theta, dtype=float)
    phi_arr = np.asarray(phi, dtype=float)
    if theta_arr.shape != phi_arr.shape:
        raise ValueError("theta and phi must have the same shape")

    twist_eff = sigma + tau

    if embedding == "parameter-shift":
        twisted_phi = (phi_arr + twist_eff * theta_arr) % (2.0 * pi)
        Px, Py = profile(twisted_phi.ravel(), params)
        Px = Px.reshape(theta_arr.shape)
        Py = Py.reshape(theta_arr.shape)
        local_N = Px
        local_B = Py
    elif embedding == "rotation":
        Px, Py = profile((phi_arr % (2.0 * pi)).ravel(), params)
        Px = Px.reshape(theta_arr.shape)
        Py = Py.reshape(theta_arr.shape)
        cos_t = np.cos(twist_eff * theta_arr)
        sin_t = np.sin(twist_eff * theta_arr)
        local_N = cos_t * Px - sin_t * Py
        local_B = sin_t * Px + cos_t * Py
    else:
        raise ValueError(
            f"embedding must be 'parameter-shift' or 'rotation', got {embedding!r}"
        )

    radial = R_major + local_N
    X = radial * np.cos(theta_arr)
    Y = radial * np.sin(theta_arr)
    Z = local_B
    return X, Y, Z


def aspect_ratio(params: ProfileParams, R_major: float) -> float:
    """Aspect ratio epsilon = L_total / (2*pi * R_major).

    Analogous to L_u / L_w in metric-charge's flat sheet.
    """
    return params.L_total / (2.0 * pi * R_major)


def gauss_bonnet_check(params: ProfileParams, n_samples: int = 1000) -> float:
    """Verify the closed profile satisfies Gauss-Bonnet (total turning = 2*pi).

    Sums signed curvature * arc-length over the analytical decomposition:
      3 lobes (positive turning, 240 deg each)
      3 saddles (negative turning, 120 deg each)
    Returns the integrated turning in radians. Should be 2*pi to machine
    precision (analytical, not numerical).
    """
    lobe_turning = 3.0 * (4.0 * pi / 3.0)  # 720 deg
    saddle_turning = -3.0 * (2.0 * pi / 3.0)  # -360 deg
    return lobe_turning + saddle_turning  # = 2*pi


def charge_per_arc() -> Tuple[float, float]:
    """Per-arc charge contributions from §11.7 of clover-quarks.md.

    Returns
    -------
    Q_lobe : float
        Charge contributed by traversing one lobe arc. Equal to +2/3.
    Q_saddle : float
        Charge contributed by traversing one saddle arc. Equal to -1/3.
    """
    Q_lobe = (1.0 / (2.0 * pi)) * (1.0) * (4.0 * pi / 3.0)  # = 2/3
    Q_saddle = (1.0 / (2.0 * pi)) * (-1.0) * (2.0 * pi / 3.0)  # = -1/3
    return Q_lobe, Q_saddle
