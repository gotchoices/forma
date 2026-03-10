#!/usr/bin/env python3
"""
R7. Charge from Torus Geometry — line-source integration model.

Physical picture:
  A circularly polarized photon travels along the (1,2) geodesic
  on a torus (major radius R, minor radius a).  Synchronized CP
  produces constant outward E at the photon's location.  We model
  this as total charge Q = e distributed uniformly along the
  geodesic path.

Method:
  For each aspect ratio r = a/R:
    1. Path constraint fixes R(r), a(r)
    2. Parameterize the (1,2) torus knot in 3D
    3. Distribute Q = e uniformly along the path (line charge)
    4. Compute E(P) at sample points in 3D by summing contributions
       from all path segments
    5. Numerically integrate U_E = ½ε₀ ∫ E² dV
    6. Compare U_E to m_e c²/2

  Sweep r to find where U_E = m_e c²/2.
"""

import sys, os, math, time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import (h, hbar, c, eps0, e, alpha, m_e, lambda_C)

# ── Target energy ────────────────────────────────────────────────
U_target = 0.5 * m_e * c**2

# ── Torus knot geometry ──────────────────────────────────────────

def torus_knot_points(R, a, p, q, N):
    """
    Return (x, y, z) arrays for N points on a (p,q) torus knot.
    p = windings around minor circle, q = windings around major circle.
    Parameter t goes from 0 to 2π.
    """
    xs, ys, zs = [], [], []
    for i in range(N):
        t = 2.0 * math.pi * i / N
        theta = p * t
        phi = q * t
        x = (R + a * math.cos(theta)) * math.cos(phi)
        y = (R + a * math.cos(theta)) * math.sin(phi)
        z = a * math.sin(theta)
        xs.append(x)
        ys.append(y)
        zs.append(z)
    return xs, ys, zs


def torus_normal(R, a, p, q, t):
    """Outward surface normal at parameter t on the (p,q) torus knot."""
    theta = p * t
    phi = q * t
    nx = math.cos(theta) * math.cos(phi)
    ny = math.cos(theta) * math.sin(phi)
    nz = math.sin(theta)
    return nx, ny, nz


def path_length_element(R, a, p, q, N):
    """
    Return the arc length of one segment (assuming uniform parameterization).
    Total path length = 2π√((pq... actually compute from derivatives.
    """
    # dl/dt for (p,q) torus knot:
    # dx/dt, dy/dt, dz/dt from parametric equations
    # Total path length ℓ = ∫₀²π |dr/dt| dt
    # For uniform segments: ds = ℓ / N
    ell = 2.0 * math.pi * math.sqrt((q * R)**2 + (p * a)**2)
    return ell / N


# ── Field computation ────────────────────────────────────────────

def compute_field_energy(R, a, p, q, N_path, grid_bounds, N_grid, d_min):
    """
    Compute total E-field energy from a line charge Q = e along
    the (p,q) torus knot.

    Uses a 3D grid in cylindrical coordinates (rho, z) with
    azimuthal symmetry exploited: integrate over (rho, z) and
    multiply by 2π × rho.

    Returns U_E in joules.
    """
    Q_total = e
    xs, ys, zs = torus_knot_points(R, a, p, q, N_path)
    ds = path_length_element(R, a, p, q, N_path)
    lam = Q_total / (N_path * ds)  # linear charge density

    # Charge per segment
    dq = Q_total / N_path

    # For the (1,2) knot, the path has q-fold rotational symmetry
    # in phi. We can compute the field on a 2D (rho, z) slice and
    # integrate azimuthally, but the path itself is NOT azimuthally
    # symmetric (it's a knot, not a ring).
    #
    # Instead: compute E at sample points on a 2D (rho, z) grid
    # at MULTIPLE phi values, average over phi, then integrate.
    # For q=2 symmetry, phi from 0 to π suffices.

    rho_max, z_max = grid_bounds
    N_rho, N_z, N_phi = N_grid

    d_rho = rho_max / N_rho
    d_z = 2.0 * z_max / N_z

    U_total = 0.0

    for i_phi in range(N_phi):
        phi_obs = math.pi * i_phi / N_phi  # 0 to π (half-turn, q=2 symmetry)
        cos_phi = math.cos(phi_obs)
        sin_phi = math.sin(phi_obs)

        for i_rho in range(1, N_rho + 1):
            rho = (i_rho - 0.5) * d_rho

            for i_z in range(N_z + 1):
                z_obs = -z_max + i_z * d_z

                # Observation point in Cartesian
                Px = rho * cos_phi
                Py = rho * sin_phi
                Pz = z_obs

                # Sum E contributions from all path segments
                Ex, Ey, Ez = 0.0, 0.0, 0.0
                for j in range(N_path):
                    dx = Px - xs[j]
                    dy = Py - ys[j]
                    dz = Pz - zs[j]
                    dist2 = dx*dx + dy*dy + dz*dz
                    dist = math.sqrt(dist2)

                    if dist < d_min:
                        continue  # skip near-field singularity

                    # Coulomb field from point charge dq
                    factor = dq / (4.0 * math.pi * eps0 * dist2 * dist)
                    Ex += factor * dx
                    Ey += factor * dy
                    Ez += factor * dz

                E2 = Ex*Ex + Ey*Ey + Ez*Ez

                # Volume element in cylindrical: rho * d_rho * d_z * d_phi
                # We sample N_phi points over π and multiply by 2 (symmetry)
                d_phi = math.pi / N_phi
                dV = rho * d_rho * d_z * d_phi * 2.0

                U_total += 0.5 * eps0 * E2 * dV

    return U_total


# ── Main sweep ───────────────────────────────────────────────────

def main():
    t_start = time.time()
    print("R7. Charge from Torus Geometry")
    print("=" * 50)
    print()
    print(f"Constants:")
    print(f"  λ_C      = {lambda_C:.6e} m")
    print(f"  e        = {e:.6e} C")
    print(f"  m_e c²   = {m_e * c**2:.6e} J")
    print(f"  U_target = {U_target:.6e} J")
    print(f"  α        = {alpha:.6e}")
    print()

    p, q_knot = 1, 2

    # ── Parameters ───────────────────────────────────────────
    N_path = 200       # segments along geodesic
    N_rho = 40         # radial grid points
    N_z = 40           # vertical grid points (half-space)
    N_phi = 16         # azimuthal samples
    d_min_factor = 0.1 # d_min = factor × smallest segment length

    # Grid extent as multiples of torus size
    grid_factor = 8.0

    print(f"Grid: N_path={N_path}, N_rho={N_rho}, N_z={N_z}, "
          f"N_phi={N_phi}")
    print(f"Grid extent: {grid_factor}× torus size")
    print()

    # ── Coarse sweep ─────────────────────────────────────────
    r_values = [0.5, 1.0, 2.0, 3.0, 4.0, 4.29, 5.0, 6.0, 6.60, 8.0, 10.0]

    print(f"{'r':>8s}  {'R (m)':>12s}  {'a (m)':>12s}  "
          f"{'U_E (J)':>12s}  {'U_E/U_target':>12s}")
    print("-" * 70)

    results = []
    for r in r_values:
        R = lambda_C / (2.0 * math.pi * math.sqrt(4 + r**2))
        a = r * R

        # Grid bounds
        rho_max = grid_factor * (R + a)
        z_max = grid_factor * a

        ds = path_length_element(R, a, p, q_knot, N_path)
        d_min = d_min_factor * ds

        t0 = time.time()
        U_E = compute_field_energy(
            R, a, p, q_knot, N_path,
            (rho_max, z_max), (N_rho, N_z, N_phi), d_min
        )
        dt = time.time() - t0

        ratio = U_E / U_target
        results.append((r, R, a, U_E, ratio))
        print(f"{r:8.2f}  {R:12.4e}  {a:12.4e}  "
              f"{U_E:12.4e}  {ratio:12.6f}  ({dt:.1f}s)")
        sys.stdout.flush()

    print()

    # ── Find crossing ────────────────────────────────────────
    # Look for where U_E/U_target crosses 1.0
    print("Looking for r where U_E = U_target ...")
    crossings = []
    for i in range(len(results) - 1):
        r1, _, _, _, rat1 = results[i]
        r2, _, _, _, rat2 = results[i + 1]
        if (rat1 - 1.0) * (rat2 - 1.0) < 0:
            # Linear interpolation
            r_cross = r1 + (r2 - r1) * (1.0 - rat1) / (rat2 - rat1)
            crossings.append(r_cross)
            print(f"  Crossing between r={r1:.2f} and r={r2:.2f}, "
                  f"interpolated: r ≈ {r_cross:.4f}")

    if not crossings:
        print("  No crossing found in the swept range.")
        print("  U_E/U_target values suggest the solution may be "
              "outside [0.5, 10.0]")
        # Check if all above or all below
        ratios = [r[4] for r in results]
        if all(x > 1 for x in ratios):
            print("  All U_E > U_target: need larger r (weaker field)")
        elif all(x < 1 for x in ratios):
            print("  All U_E < U_target: need smaller r (stronger field)")
    else:
        # Refine with bisection
        print()
        print("Refining with bisection ...")
        for r_est in crossings:
            r_lo = r_est - 1.0
            r_hi = r_est + 1.0

            for iteration in range(20):
                r_mid = 0.5 * (r_lo + r_hi)
                R = lambda_C / (2.0 * math.pi * math.sqrt(4 + r_mid**2))
                a = r_mid * R
                rho_max = grid_factor * (R + a)
                z_max = grid_factor * a
                ds = path_length_element(R, a, p, q_knot, N_path)
                d_min = d_min_factor * ds

                U_E = compute_field_energy(
                    R, a, p, q_knot, N_path,
                    (rho_max, z_max), (N_rho, N_z, N_phi), d_min
                )
                ratio = U_E / U_target

                if ratio > 1.0:
                    r_lo = r_mid
                else:
                    r_hi = r_mid

                if abs(ratio - 1.0) < 1e-4 or (r_hi - r_lo) < 1e-4:
                    break

                print(f"  iter {iteration+1:2d}: r = {r_mid:.6f}, "
                      f"U_E/U_target = {ratio:.6f}")
                sys.stdout.flush()

            r_final = 0.5 * (r_lo + r_hi)
            R_final = lambda_C / (2.0 * math.pi * math.sqrt(4 + r_final**2))
            a_final = r_final * R_final

            print()
            print("=" * 50)
            print(f"RESULT: r = a/R = {r_final:.6f}")
            print(f"  R = {R_final:.6e} m")
            print(f"  a = {a_final:.6e} m")
            print(f"  a/R = {r_final:.6f}")
            print()
            print(f"Comparison with known expressions:")
            print(f"  1/√(πα) = {1.0/math.sqrt(math.pi * alpha):.6f}  (S2)")
            print(f"  R6 self-consistent = 4.29")
            print(f"  π√2 = {math.pi * math.sqrt(2):.6f}")
            print(f"  π = {math.pi:.6f}")
            print(f"  2π = {2*math.pi:.6f}")
            print(f"  √(2/α) = {math.sqrt(2.0/alpha):.6f}")

    t_total = time.time() - t_start
    print()
    print(f"Total runtime: {t_total:.1f}s")


if __name__ == '__main__':
    main()
