#!/usr/bin/env python3
"""
R7 Track B. Surface-charge integration model.

Distributes Q = e uniformly over the torus SURFACE (not the
geodesic path).  Computes the 3D Coulomb field energy.
Compares with Track A (line source along geodesic) to confirm
the energy shortfall is independent of the charge distribution.
"""

import sys, os, math, time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import (h, hbar, c, eps0, e, alpha, m_e, lambda_C)

U_target = 0.5 * m_e * c**2


def torus_surface_points(R, a, N_theta, N_phi):
    """
    Generate surface elements on the torus.
    Returns lists: x, y, z (center of each element) and dA (area).

    The torus surface area element:
      dA = (R + a cos θ) × a × dθ × dφ
    """
    xs, ys, zs, dAs = [], [], [], []
    d_theta = 2.0 * math.pi / N_theta
    d_phi = 2.0 * math.pi / N_phi

    for i in range(N_theta):
        theta = (i + 0.5) * d_theta
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        rho = R + a * cos_t
        dA = rho * a * d_theta * d_phi

        for j in range(N_phi):
            phi = (j + 0.5) * d_phi
            cos_p = math.cos(phi)
            sin_p = math.sin(phi)

            xs.append(rho * cos_p)
            ys.append(rho * sin_p)
            zs.append(a * sin_t)
            dAs.append(dA)

    return xs, ys, zs, dAs


def compute_field_energy_surface(R, a, N_src_theta, N_src_phi,
                                 grid_bounds, N_grid, d_min):
    """
    Compute total E-field energy from uniform surface charge Q = e
    on the torus.
    """
    Q_total = e
    xs, ys, zs, dAs = torus_surface_points(R, a, N_src_theta, N_src_phi)
    N_src = len(xs)

    A_total = sum(dAs)
    sigma = Q_total / A_total  # uniform surface charge density

    # charge per element
    dqs = [sigma * dA for dA in dAs]

    rho_max, z_max = grid_bounds
    N_rho, N_z, N_phi_obs = N_grid

    d_rho = rho_max / N_rho
    d_z = 2.0 * z_max / N_z

    U_total = 0.0

    for i_phi in range(N_phi_obs):
        phi_obs = math.pi * i_phi / N_phi_obs
        cos_phi = math.cos(phi_obs)
        sin_phi = math.sin(phi_obs)

        for i_rho in range(1, N_rho + 1):
            rho = (i_rho - 0.5) * d_rho

            for i_z in range(N_z + 1):
                z_obs = -z_max + i_z * d_z

                Px = rho * cos_phi
                Py = rho * sin_phi
                Pz = z_obs

                Ex, Ey, Ez = 0.0, 0.0, 0.0
                for j in range(N_src):
                    dx = Px - xs[j]
                    dy = Py - ys[j]
                    dz = Pz - zs[j]
                    dist2 = dx*dx + dy*dy + dz*dz
                    dist = math.sqrt(dist2)

                    if dist < d_min:
                        continue

                    factor = dqs[j] / (4.0 * math.pi * eps0 * dist2 * dist)
                    Ex += factor * dx
                    Ey += factor * dy
                    Ez += factor * dz

                E2 = Ex*Ex + Ey*Ey + Ez*Ez

                d_phi_obs = math.pi / N_phi_obs
                dV = rho * d_rho * d_z * d_phi_obs * 2.0

                U_total += 0.5 * eps0 * E2 * dV

    return U_total


def main():
    t_start = time.time()
    print("R7 Track B: Surface-Charge Integration")
    print("=" * 55)
    print()
    print(f"Constants:")
    print(f"  λ_C      = {lambda_C:.6e} m")
    print(f"  e        = {e:.6e} C")
    print(f"  U_target = {U_target:.6e} J")
    print(f"  α        = {alpha:.6e}")
    print()

    # Source: torus surface elements
    N_src_theta = 24
    N_src_phi = 48
    N_src_total = N_src_theta * N_src_phi

    # Observation grid
    N_rho = 30
    N_z = 30
    N_phi_obs = 12
    d_min_factor = 0.3   # fraction of smallest source spacing

    grid_factor = 8.0

    print(f"Source: {N_src_theta}×{N_src_phi} = {N_src_total} "
          f"surface elements")
    print(f"Grid:   N_rho={N_rho}, N_z={N_z}, N_phi={N_phi_obs}")
    print(f"Grid extent: {grid_factor}× torus size")
    print()

    r_values = [0.5, 1.0, 2.0, 4.0, 4.29, 6.60, 10.0]

    print(f"{'r':>8s}  {'R (m)':>12s}  {'a (m)':>12s}  "
          f"{'U_E (J)':>12s}  {'U/U_tgt':>9s}  {'time':>6s}")
    print("-" * 65)

    results = []
    for r in r_values:
        R = lambda_C / (2.0 * math.pi * math.sqrt(4 + r**2))
        a = r * R

        rho_max = grid_factor * (R + a)
        z_max = grid_factor * a
        if z_max < grid_factor * R:
            z_max = grid_factor * R

        # d_min from source element spacing
        min_spacing = min(2*math.pi*a/N_src_theta,
                          2*math.pi*R/N_src_phi)
        d_min = d_min_factor * min_spacing

        t0 = time.time()
        U_E = compute_field_energy_surface(
            R, a, N_src_theta, N_src_phi,
            (rho_max, z_max), (N_rho, N_z, N_phi_obs), d_min
        )
        dt = time.time() - t0

        ratio = U_E / U_target
        results.append((r, R, a, U_E, ratio))
        print(f"{r:8.2f}  {R:12.4e}  {a:12.4e}  "
              f"{U_E:12.4e}  {ratio:9.6f}  {dt:5.1f}s")
        sys.stdout.flush()

    print()
    print("=" * 55)
    print("Comparison with Track A (line source):")
    print()
    print(f"{'r':>8s}  {'Surface U/U_tgt':>15s}  {'Line U/U_tgt':>15s}")
    print("-" * 45)

    # Track A results (from torus_charge.py run)
    track_a = {
        0.5:  0.018016,
        1.0:  0.015759,
        2.0:  0.015362,
        4.0:  0.012104,
        4.29: 0.012212,
        6.60: 0.010773,
        10.0: 0.010668,
    }

    for r, R, a, U_E, ratio in results:
        ta = track_a.get(r, None)
        ta_str = f"{ta:15.6f}" if ta else "           N/A"
        print(f"{r:8.2f}  {ratio:15.6f}  {ta_str}")

    print()
    print(f"Analytical prediction: U/U_target ≈ 2α = {2*alpha:.6f}")
    print()
    t_total = time.time() - t_start
    print(f"Total runtime: {t_total:.1f}s")


if __name__ == '__main__':
    main()
