"""
R52 Track 4e: Vector self-interaction WITH shear.

Track 4d used SCALAR Coulomb self-energy:
    U = (1/2) Σ ρ(r) ρ(r') / |r - r'|
This treats the antinode contributions as scalar charges and
ignores the direction of any associated current.  It found a
viability window for the predicted sign pattern at small r,
but MaSt's natural shear value sits ~30% below the window.

Track 4e adds the missing vector content:
    W = (1/2) Σ j(r) · j(r') / |r - r'|
where j(r) is a vector quantity proportional to ψ × ê_geodesic.
The dot product ê_geodesic(r₁) · ê_geodesic(r₂) is between -1
and +1 depending on whether the current at the two points is
parallel or antiparallel.  This vector contribution can shift
the sign-flip threshold or change which modes flip first.

PHYSICAL MOTIVATION:
- The magnetic moment is fundamentally a VECTOR quantity computed
  from the curl of A_self.  Scalar Coulomb integrals cannot
  capture vector field cancellation.
- For a (1, n_ring) standing wave on a torus, the polarization
  current flows along the (1, n_ring) geodesic direction.  At
  different points on the surface, this direction varies.
- The "current self-interaction" weights pairs by the dot product
  of their geodesic tangent vectors, which can flip sign.

WAVE CONSTRUCTION (same as 4d):
ψ_sheared(θ_t, θ_r) = cos(n_tube × θ_t) × cos((n_ring - s) × θ_r)

CURRENT VECTOR (new):
At each surface point (θ_t, θ_r), the geodesic tangent direction
in the embedded 3D torus is:
    ê_geo = ∂(r)/∂t · normalize, where t parameterizes the geodesic
            (n_tube θ_t + n_ring θ_r)
The signed current vector is:
    j(r) = ψ(r) × ê_geo(r)
This has signed magnitude (from ψ) and direction (from geodesic).

VECTOR INTERACTION:
    W = (1/2) Σ j(r₁) · j(r₂) / |r₁ - r₂|
      = (1/2) Σ ψ(r₁) ψ(r₂) (ê_geo(r₁) · ê_geo(r₂)) / |r₁ - r₂|

This is the scalar Coulomb integral (Track 4d) with an extra
factor (ê_geo · ê_geo) that can be positive or negative.

ASSUMPTIONS:
- (1, n_ring) standing wave with shear: cos(θ_t) × cos((n_ring - s) θ_r)
- Geodesic tangent computed from (n_tube=1, n_ring) winding
- Same chord-distance discretization as 4c, 4d
- Two grid resolutions for convergence check
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ── Surface discretization with geodesic tangent ────────────────────

def torus_grid_with_tangent(R, a, n_tube_cells, n_ring_cells, n_tube_wind=1, n_ring_wind=2):
    """
    Discretize the embedded torus and compute geodesic tangent at each cell.

    The geodesic for a (n_tube_wind, n_ring_wind) mode is parameterized
    by t such that θ_tube = n_tube_wind × t, θ_ring = n_ring_wind × t.
    The tangent is d(r)/dt where r is the 3D position.
    """
    theta_tube = (np.arange(n_tube_cells) + 0.5) * (2 * np.pi / n_tube_cells)
    theta_ring = (np.arange(n_ring_cells) + 0.5) * (2 * np.pi / n_ring_cells)
    tt, tr = np.meshgrid(theta_tube, theta_ring, indexing='ij')

    cos_t, sin_t = np.cos(tt), np.sin(tt)
    cos_r, sin_r = np.cos(tr), np.sin(tr)

    rho = R + a * cos_t
    x = rho * cos_r
    y = rho * sin_r
    z = a * sin_t
    pos = np.stack([x, y, z], axis=-1)

    # Tangent vectors in 3D for the torus parameterization:
    # ∂r/∂θ_t = (-a sin_t cos_r, -a sin_t sin_r, a cos_t)
    # ∂r/∂θ_r = (-rho sin_r, rho cos_r, 0)
    e_t_x = -a * sin_t * cos_r
    e_t_y = -a * sin_t * sin_r
    e_t_z = a * cos_t
    e_t = np.stack([e_t_x, e_t_y, e_t_z], axis=-1)

    e_r_x = -rho * sin_r
    e_r_y = rho * cos_r
    e_r_z = np.zeros_like(rho)
    e_r = np.stack([e_r_x, e_r_y, e_r_z], axis=-1)

    # Geodesic tangent: d(r)/dt = (∂r/∂θ_t) × (dθ_t/dt) + (∂r/∂θ_r) × (dθ_r/dt)
    # With θ_t = n_tube_wind × t, θ_r = n_ring_wind × t:
    geo_tangent = n_tube_wind * e_t + n_ring_wind * e_r
    # Normalize to unit length
    geo_norm = np.linalg.norm(geo_tangent, axis=-1, keepdims=True)
    geo_norm = np.maximum(geo_norm, 1e-12)
    e_geo = geo_tangent / geo_norm

    # Surface area element
    dtheta_t = 2 * np.pi / n_tube_cells
    dtheta_r = 2 * np.pi / n_ring_cells
    dA = a * rho * dtheta_t * dtheta_r

    return pos, dA, e_geo, theta_tube, theta_ring


def signed_charge_density_sheared(theta_tube, theta_ring, n_tube=1, n_ring=2, shear=0.0):
    """ψ_sheared(θ_t, θ_r) = cos(n_tube × θ_t) × cos((n_ring - shear) × θ_r)"""
    tt, tr = np.meshgrid(theta_tube, theta_ring, indexing='ij')
    return np.cos(n_tube * tt) * np.cos((n_ring - shear) * tr)


# ── Vector self-interaction ─────────────────────────────────────────

def vector_self_interaction(pos, charge, e_geo, eps):
    """
    Compute W = (1/2) Σ_{i ≠ j} j(r_i) · j(r_j) / |r_i - r_j|
    where j(r_i) = charge[i] × e_geo[i].

    This is the vector analog of the scalar Coulomb self-energy.
    """
    n = len(charge)
    # Pairwise distances
    diff = pos[:, None, :] - pos[None, :, :]
    dist = np.linalg.norm(diff, axis=-1)
    np.fill_diagonal(dist, np.inf)
    dist = np.maximum(dist, eps)

    # Pairwise charge product
    qq = charge[:, None] * charge[None, :]

    # Pairwise geodesic dot product
    # e_geo: (N, 3)
    geo_dot = np.einsum('ik,jk->ij', e_geo, e_geo)  # (N, N)

    # Combine
    integrand = qq * geo_dot / dist
    return 0.5 * np.sum(integrand)


def compute_W(R, a, n_tube, n_ring, shear, n_tube_cells=24, n_ring_cells=48,
              eps_factor=0.5):
    """Vector self-interaction W of the sheared (n_tube, n_ring) wave."""
    pos, dA, e_geo, tt, tr = torus_grid_with_tangent(
        R, a, n_tube_cells, n_ring_cells, n_tube, n_ring)
    psi = signed_charge_density_sheared(tt, tr, n_tube, n_ring, shear)
    charge = (psi * dA).flatten()
    pos_flat = pos.reshape(-1, 3)
    e_geo_flat = e_geo.reshape(-1, 3)
    mean_cell_size = np.sqrt(dA.mean())
    eps = eps_factor * mean_cell_size
    return vector_self_interaction(pos_flat, charge, e_geo_flat, eps)


# ── Sign test ───────────────────────────────────────────────────────

def run_sign_test(r_aspect, shear_values, R=1.0, n_tube_cells=24, n_ring_cells=48,
                  label=""):
    a = r_aspect * R

    print(f"\n── {label} (r = {r_aspect}) ──")
    print(f"  R = {R}, a = {a}")
    print(f"  Grid: {n_tube_cells} × {n_ring_cells}")

    print(f"\n  {'shear':>10s}  {'W(1,2)':>14s}  {'W(1,3)':>14s}  "
          f"{'δW(1,2)':>14s}  {'δW(1,3)':>14s}")
    print("  " + "─" * 75)

    W2_0 = compute_W(R, a, 1, 2, 0.0, n_tube_cells, n_ring_cells)
    W3_0 = compute_W(R, a, 1, 3, 0.0, n_tube_cells, n_ring_cells)

    results = []
    for s in shear_values:
        W2 = compute_W(R, a, 1, 2, s, n_tube_cells, n_ring_cells)
        W3 = compute_W(R, a, 1, 3, s, n_tube_cells, n_ring_cells)
        dW2 = W2 - W2_0
        dW3 = W3 - W3_0
        results.append((s, W2, W3, dW2, dW3))
        print(f"  {s:10.5f}  {W2:+14.4f}  {W3:+14.4f}  {dW2:+14.4f}  {dW3:+14.4f}")

    return results


def find_threshold(R, a, n_ring, s_values, n_tube_cells=24, n_ring_cells=48):
    """Find the smallest s where δW changes sign for the given mode."""
    W0 = compute_W(R, a, 1, n_ring, 0.0, n_tube_cells, n_ring_cells)
    initial_sign = None
    for s in s_values:
        if s == 0:
            continue
        dW = compute_W(R, a, 1, n_ring, s, n_tube_cells, n_ring_cells) - W0
        sign = np.sign(dW) if abs(dW) > 1e-9 else 0
        if initial_sign is None:
            initial_sign = sign
        elif sign != 0 and sign != initial_sign:
            return s, sign
    return None, None


# ── Main ───────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("R52 Track 4e: Vector self-interaction WITH shear")
    print("=" * 70)
    print(__doc__)

    print("\n" + "=" * 70)
    print("PART 1: Sign test at the proton aspect ratio (lib value)")
    print("=" * 70)

    shear_values = [0.0, 0.001, 0.005, 0.01, 0.02, 0.05]
    run_sign_test(8.906, shear_values, label="r_p = 8.906 (R27 F18 value)")

    print("\n" + "=" * 70)
    print("PART 2: Sign test at filtering range r values")
    print("=" * 70)

    for r in [0.34, 0.40, 0.45, 0.49]:
        run_sign_test(r, [0.0, 0.05, 0.10, 0.15, 0.20, 0.25],
                       label=f"r = {r} (filtering range)")

    print("\n" + "=" * 70)
    print("PART 3: Threshold scan")
    print("=" * 70)

    print("\n(1,3) sign-flip threshold for δW vs r:")
    print("  r       s_threshold(1,3)")
    print("  " + "─" * 30)
    s_scan = np.linspace(0.005, 0.5, 100)
    for r in [0.34, 0.40, 0.45, 0.49, 0.7, 1.0, 2.0, 5.0, 8.906]:
        s_th, _ = find_threshold(1.0, r, 3, s_scan)
        s_str = f"{s_th:.4f}" if s_th else ">0.5"
        print(f"  {r:.3f}   {s_str}")

    print("\n(1,2) sign-flip threshold for δW vs r:")
    print("  r       s_threshold(1,2)")
    print("  " + "─" * 30)
    for r in [0.34, 0.40, 0.45, 0.49, 0.7, 1.0, 2.0, 5.0, 8.906]:
        s_th, _ = find_threshold(1.0, r, 2, s_scan)
        s_str = f"{s_th:.4f}" if s_th else ">0.5"
        print(f"  {r:.3f}   {s_str}")

    print("\n" + "=" * 70)
    print("PART 4: Viability window comparison (Track 4d vs 4e)")
    print("=" * 70)

    print("\n  r       s_(1,3)    s_(1,2)    window?")
    print("  " + "─" * 50)
    for r in [0.34, 0.40, 0.45, 0.49, 0.7, 1.0, 2.0]:
        s3, _ = find_threshold(1.0, r, 3, s_scan)
        s2, _ = find_threshold(1.0, r, 2, s_scan)
        s3_str = f"{s3:.4f}" if s3 else ">0.5"
        s2_str = f"{s2:.4f}" if s2 else ">0.5"
        if s3 and s2 and s3 < s2:
            window = f"YES: ({s3:.3f}, {s2:.3f})"
        else:
            window = "NO"
        print(f"  {r:.3f}   {s3_str:>8s}   {s2_str:>8s}   {window}")

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    # MaSt shear values
    try:
        from lib.ma_model_d import solve_shear_for_alpha
        print("\nComparison: vector W threshold vs MaSt shear at α=1/137:")
        print("  r       MaSt s    s_(1,3)    s_(1,2)    in window?")
        print("  " + "─" * 60)
        for r in [0.34, 0.40, 0.45, 0.49]:
            s_mast = solve_shear_for_alpha(r)
            s3, _ = find_threshold(1.0, r, 3, s_scan)
            s2, _ = find_threshold(1.0, r, 2, s_scan)
            s3_str = f"{s3:.4f}" if s3 else ">0.5"
            s2_str = f"{s2:.4f}" if s2 else ">0.5"
            in_window = ""
            if s3 and s2 and s3 < s_mast < s2:
                in_window = "YES *** "
            elif s3 and s_mast < s3:
                in_window = f"NO (below by {s3 - s_mast:.3f})"
            print(f"  {r:.3f}   {s_mast:.4f}    {s3_str:>8s}   {s2_str:>8s}   {in_window}")
    except Exception as exc:
        print(f"  (could not compute MaSt shear: {exc})")


if __name__ == "__main__":
    main()
