#!/usr/bin/env python3
"""
02_knot_charge.py — Compute the apparent electric charge for (p,q) torus knots.

For each knot, parameterize the path on a torus, propagate a circularly
polarized photon's E-field along the path using parallel transport of the
polarization frame, and compute the time-averaged radial component of the
E-field. The ratio of this radial component to the (1,2) baseline gives
the effective charge fraction.

The approach is model-first: no target charges are assumed. We compute
what each knot produces and compare against known particles afterward.

Bears on theory.md P2 (charge variation), findings F3.
"""

import math
import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib import constants as C


def knot_path(p, q, R, a, N=10000):
    """
    Parameterize a (p,q) torus knot.
    Returns arrays of (x,y,z) positions and the parameter t.

    The path winds q times around the major axis (φ direction)
    and p times around the tube (θ direction).
    """
    t = np.linspace(0, 2 * np.pi, N, endpoint=False)
    theta = p * t
    phi = q * t

    x = (R + a * np.cos(theta)) * np.cos(phi)
    y = (R + a * np.cos(theta)) * np.sin(phi)
    z = a * np.sin(theta)

    return t, np.column_stack([x, y, z])


def compute_frame(pos):
    """
    Compute the Frenet-like frame along the path.
    Returns tangent (T), normal (N), binormal (B) at each point.

    T = dpos/ds (unit tangent)
    N = dT/ds / |dT/ds| (principal normal)
    B = T × N (binormal)
    """
    N_pts = len(pos)
    dp = np.roll(pos, -1, axis=0) - np.roll(pos, 1, axis=0)
    T = dp / np.linalg.norm(dp, axis=1, keepdims=True)

    dT = np.roll(T, -1, axis=0) - np.roll(T, 1, axis=0)
    dT_norm = np.linalg.norm(dT, axis=1, keepdims=True)
    dT_norm = np.maximum(dT_norm, 1e-30)
    N_vec = dT / dT_norm

    B = np.cross(T, N_vec)
    B = B / np.linalg.norm(B, axis=1, keepdims=True)

    N_vec = np.cross(B, T)

    return T, N_vec, B


def propagate_polarization(T, N_vec, B, pos, p, q, N_pts):
    """
    Propagate a circularly polarized E-field along the path.

    The E-field is perpendicular to T (the propagation direction).
    For circular polarization, E rotates in the N-B plane as the
    wave propagates. The rotation rate is set by the photon's
    wavelength: one full rotation per wavelength.

    The photon wavelength equals the path length (one wavelength
    fits the closed path). The wave phase advances by 2π over the
    full path.

    Returns the E-field direction (unit vector) at each point.
    """
    ds = np.linalg.norm(np.diff(pos, axis=0, append=pos[:1]), axis=1)
    s = np.cumsum(ds)
    s = s - s[0]
    L = s[-1] + ds[-1]
    phase = 2 * np.pi * s / L

    E = np.cos(phase)[:, None] * N_vec + np.sin(phase)[:, None] * B

    return E, L


def radial_direction(pos):
    """
    Compute the radial unit vector (pointing away from the torus
    symmetry axis, which is the z-axis) at each point on the path.

    rho_hat = (x, y, 0) / |(x, y, 0)|
    """
    rho = np.column_stack([pos[:, 0], pos[:, 1], np.zeros(len(pos))])
    rho_norm = np.linalg.norm(rho, axis=1, keepdims=True)
    rho_norm = np.maximum(rho_norm, 1e-30)
    return rho / rho_norm


def outward_radial(pos, R):
    """
    Compute the outward radial direction from the torus tube center
    (the direction a point charge at the tube center would produce).

    For a point at (x,y,z) on a torus with major radius R along
    the z-axis as symmetry axis, the tube center is at
    (R*cos(φ), R*sin(φ), 0) where φ = atan2(y,x).

    The outward direction is from tube center toward the point.
    """
    phi = np.arctan2(pos[:, 1], pos[:, 0])
    center = np.column_stack([R * np.cos(phi), R * np.sin(phi), np.zeros(len(pos))])
    dr = pos - center
    dr_norm = np.linalg.norm(dr, axis=1, keepdims=True)
    dr_norm = np.maximum(dr_norm, 1e-30)
    return dr / dr_norm


def compute_monopole_moment(E, pos):
    """
    Compute the monopole moment of the E-field distribution.

    For a distant observer, the apparent charge is proportional to
    the average of E · r̂ over the path, where r̂ is the direction
    from the torus center (origin) to the observation point.

    Since the path has azimuthal symmetry when time-averaged over
    the full orbit, we compute the average radial component in
    spherical coordinates. For a monopole, this is the same in
    all directions.

    We compute <E · r̂_point> where r̂_point = pos/|pos| is the
    direction from the origin to each path point. This gives the
    "self-consistent" monopole: what charge would a distant observer
    infer from the field at the particle's own surface?
    """
    r = pos / np.linalg.norm(pos, axis=1, keepdims=True)
    return np.mean(np.sum(E * r, axis=1))


def compute_axial_radial_moment(E, pos):
    """
    Compute the average E · ρ̂ (cylindrical radial component).
    This measures how much of the E-field points away from the
    symmetry axis — the dominant contributor to apparent charge
    at large distances.
    """
    rho_hat = radial_direction(pos)
    return np.mean(np.sum(E * rho_hat, axis=1))


def compute_tube_radial_moment(E, pos, R):
    """
    Compute the average E · r̂_tube (tube-outward component).
    This is the WvM mechanism: E-field pointing radially outward
    from the tube center produces the Coulomb-like field.
    """
    r_tube = outward_radial(pos, R)
    return np.mean(np.sum(E * r_tube, axis=1))


def main():
    R = 1.0
    a = 0.01  # a << R limit (thin torus, where spin derivation holds)

    N_pts = 100000

    print("=" * 78)
    print("Torus Knot Charge Survey")
    print("=" * 78)
    print()
    print(f"  Torus: R = {R}, a = {a} (a/R = {a/R})")
    print(f"  Path points: {N_pts}")
    print()
    print("  Computing E-field charge fractions for (p,q) knots.")
    print("  The E-field is circularly polarized, propagated along the")
    print("  path using the Frenet frame. Three charge measures:")
    print("    M_sph  = <E · r̂>     (spherical radial, monopole moment)")
    print("    M_cyl  = <E · ρ̂>     (cylindrical radial)")
    print("    M_tube = <E · r̂_tube> (tube-outward, WvM mechanism)")
    print()

    baseline_sph = None
    baseline_cyl = None
    baseline_tube = None

    print("─" * 78)
    print(f"  {'(p,q)':>6s}  {'Type':>8s}  {'Spin':>6s}  "
          f"{'M_sph':>10s}  {'M_cyl':>10s}  {'M_tube':>10s}  "
          f"{'Q_sph':>8s}  {'Q_cyl':>8s}  {'Q_tube':>8s}")
    print("─" * 78)

    knots = []
    for q in [1, 2, 3]:
        for p in range(1, 10):
            if math.gcd(p, q) != 1:
                continue
            knots.append((p, q))

    for p, q in knots:
        t, pos = knot_path(p, q, R, a, N=N_pts)
        T, N_vec, B = compute_frame(pos)
        E, L = propagate_polarization(T, N_vec, B, pos, p, q, N_pts)

        m_sph = compute_monopole_moment(E, pos)
        m_cyl = compute_axial_radial_moment(E, pos)
        m_tube = compute_tube_radial_moment(E, pos, R)

        if (p, q) == (1, 2):
            baseline_sph = m_sph
            baseline_cyl = m_cyl
            baseline_tube = m_tube

        fb = "fermion" if p % 2 == 1 else "boson"
        spin = f"1/{q}" if q > 1 else "1"

        q_sph = m_sph / baseline_sph if baseline_sph and baseline_sph != 0 else float('nan')
        q_cyl = m_cyl / baseline_cyl if baseline_cyl and baseline_cyl != 0 else float('nan')
        q_tube = m_tube / baseline_tube if baseline_tube and baseline_tube != 0 else float('nan')

        print(f"  ({p},{q}){' ':>{4-len(str(p))-len(str(q))}s}  {fb:>8s}  {spin:>6s}  "
              f"{m_sph:>10.6f}  {m_cyl:>10.6f}  {m_tube:>10.6f}  "
              f"{q_sph:>8.4f}  {q_cyl:>8.4f}  {q_tube:>8.4f}")

    print("─" * 78)
    print()

    print("=" * 78)
    print("Focus: Spin-½ fermions (q=2, odd p)")
    print("=" * 78)
    print()
    print(f"  {'(p,2)':>6s}  {'Q_sph':>10s}  {'Q_cyl':>10s}  {'Q_tube':>10s}  "
          f"{'Match?':>20s}")
    print("  " + "─" * 64)

    known_charges = {1.0: "electron (1)", 2/3: "up quark (2/3)",
                     1/3: "down quark (1/3)", 0.0: "neutrino (0)"}

    for p, q in knots:
        if q != 2 or p % 2 == 0:
            continue

        t, pos = knot_path(p, q, R, a, N=N_pts)
        T, N_vec, B = compute_frame(pos)
        E, L = propagate_polarization(T, N_vec, B, pos, p, q, N_pts)

        ms = compute_monopole_moment(E, pos)
        mc = compute_axial_radial_moment(E, pos)
        mt = compute_tube_radial_moment(E, pos, R)

        qs = ms / baseline_sph if baseline_sph else float('nan')
        qc = mc / baseline_cyl if baseline_cyl else float('nan')
        qt = mt / baseline_tube if baseline_tube else float('nan')

        match = ""
        for kc, name in known_charges.items():
            if abs(abs(qt) - kc) < 0.05:
                match = name
                break

        print(f"  ({p},2)    {qs:>10.4f}  {qc:>10.4f}  {qt:>10.4f}  {match:>20s}")

    print()

    print("=" * 78)
    print("Sensitivity check: varying a/R")
    print("=" * 78)
    print()
    print("  Testing whether charge fractions depend on torus aspect ratio.")
    print()

    for a_ratio in [0.001, 0.01, 0.1, 0.3, 0.5]:
        a_test = a_ratio * R
        print(f"  a/R = {a_ratio}:")
        print(f"    {'(p,2)':>6s}  {'Q_tube':>10s}")

        bl = None
        for p in [1, 3, 5, 7]:
            t, pos = knot_path(p, 2, R, a_test, N=N_pts)
            T, N_vec, B = compute_frame(pos)
            E, L = propagate_polarization(T, N_vec, B, pos, p, 2, N_pts)
            m = compute_tube_radial_moment(E, pos, R)
            if p == 1:
                bl = m
            q_frac = m / bl if bl else float('nan')
            print(f"    ({p},2)    {q_frac:>10.4f}")
        print()


if __name__ == "__main__":
    main()
