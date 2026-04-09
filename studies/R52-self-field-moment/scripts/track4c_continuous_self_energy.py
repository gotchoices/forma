"""
R52 Track 4c: Continuous standing-wave self-energy.

HYPOTHESIS:
Treat ψ(θ_tube, θ_ring) = cos(n_tube*θ_tube) * cos(n_ring*θ_ring) as
a real-valued classical charge density (with SIGNED values, not |ψ|²)
and compute its Coulomb self-energy by integration over the embedded
torus surface.  The sign of U_self differs between (1,2) and (1,3)
because the cos·cos structure has + and − regions of differing
geometric arrangement.

METHOD:
1. Discretize the torus surface as a grid of (θ_tube, θ_ring) cells.
2. For each cell, compute the area dA and the SIGNED charge
   ρ × dA = q × cos(n_tube*θ_tube) × cos(n_ring*θ_ring) × dA.
3. Compute the Coulomb self-energy:
     U_self = (1/2) Σ_{i ≠ j} (ρ_i dA_i)(ρ_j dA_j) / |r_i - r_j|
   where |r_i - r_j| is the chord distance through 3D space.
4. Use a softening length ε to handle the diagonal singularity.
5. Compare U_self for (1,2) vs (1,3) modes.

CONVENTIONS:
- Lib: n1 = tube (poloidal), n2 = ring (toroidal)
- Mode (1, n_ring) means n1 = 1, n2 = n_ring

ASSUMPTIONS (frozen):
- Standing wave basis: ψ = cos(θ_tube) * cos(n_ring * θ_ring)
- Charge density: ρ = q × ψ (signed, NOT |ψ|²)
- Embedded torus geometry with major radius R, minor radius a
- Chord distances through 3D space
- Softening: ε = 0.05 × (mean cell size) to handle r → r' singularity
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ── Surface discretization ─────────────────────────────────────────

def torus_grid(R, a, n_tube_cells, n_ring_cells):
    """
    Discretize the embedded torus surface as a grid of (θ_tube, θ_ring) cells.

    Returns:
      pos:  (N_tube, N_ring, 3) — 3D positions of cell centers
      dA:   (N_tube, N_ring) — surface area element of each cell
      theta_tube: (N_tube,) — tube angles
      theta_ring: (N_ring,) — ring angles
    """
    theta_tube = (np.arange(n_tube_cells) + 0.5) * (2 * np.pi / n_tube_cells)
    theta_ring = (np.arange(n_ring_cells) + 0.5) * (2 * np.pi / n_ring_cells)

    tt, tr = np.meshgrid(theta_tube, theta_ring, indexing='ij')

    cos_t = np.cos(tt)
    sin_t = np.sin(tt)
    cos_r = np.cos(tr)
    sin_r = np.sin(tr)

    rho = R + a * cos_t
    x = rho * cos_r
    y = rho * sin_r
    z = a * sin_t
    pos = np.stack([x, y, z], axis=-1)

    # Surface area element of a torus: dA = a × (R + a cos θ_tube) dθ_tube dθ_ring
    dtheta_t = 2 * np.pi / n_tube_cells
    dtheta_r = 2 * np.pi / n_ring_cells
    dA = a * rho * dtheta_t * dtheta_r

    return pos, dA, theta_tube, theta_ring


def signed_charge_density(theta_tube, theta_ring, n_tube=1, n_ring=2):
    """
    Compute signed charge density ψ = cos(n_tube*θ_tube) * cos(n_ring*θ_ring).
    """
    tt, tr = np.meshgrid(theta_tube, theta_ring, indexing='ij')
    return np.cos(n_tube * tt) * np.cos(n_ring * tr)


# ── Self-energy computation ─────────────────────────────────────────

def coulomb_self_energy(pos, charge, eps):
    """
    Compute U_self = (1/2) Σ_{i ≠ j} q_i q_j / |r_i - r_j|

    pos: (N, 3) flattened positions
    charge: (N,) flattened signed charges (q_i = ρ_i × dA_i)
    eps: softening length

    Returns the total self-energy (in units determined by R and charge).
    """
    n = len(charge)
    # Pairwise distances
    diff = pos[:, None, :] - pos[None, :, :]  # (N, N, 3)
    dist = np.linalg.norm(diff, axis=-1)  # (N, N)
    np.fill_diagonal(dist, np.inf)  # exclude self-terms

    # Apply softening
    dist_safe = np.maximum(dist, eps)

    # Compute U = (1/2) Σ q_i q_j / d
    qq = charge[:, None] * charge[None, :]
    U = 0.5 * np.sum(qq / dist_safe)
    return U


def compute_self_energy(R, a, n_tube, n_ring, n_tube_cells, n_ring_cells, eps_factor=0.5):
    """
    Compute the continuous self-energy for a (n_tube, n_ring) mode.
    """
    pos, dA, theta_tube, theta_ring = torus_grid(R, a, n_tube_cells, n_ring_cells)
    psi = signed_charge_density(theta_tube, theta_ring, n_tube, n_ring)
    charge = psi * dA  # signed charge per cell

    # Flatten
    pos_flat = pos.reshape(-1, 3)
    charge_flat = charge.flatten()

    # Mean cell length scale (for softening)
    mean_cell_size = np.sqrt(dA.mean())
    eps = eps_factor * mean_cell_size

    U = coulomb_self_energy(pos_flat, charge_flat, eps)
    return U, mean_cell_size, eps


# ── Sign test ───────────────────────────────────────────────────────

def run_sign_test(r_aspect, R=1.0, n_tube_cells=24, n_ring_cells=48, label=""):
    """
    Compute self-energy for (1,2) and (1,3) at the same aspect ratio.
    """
    a = r_aspect * R

    print(f"\n── {label} (r = a/R = {r_aspect}) ──")
    print(f"  R = {R}, a = {a}")
    print(f"  Grid: {n_tube_cells} × {n_ring_cells} cells")

    results = {}
    for n_ring in [2, 3]:
        U, mcs, eps = compute_self_energy(
            R, a, n_tube=1, n_ring=n_ring,
            n_tube_cells=n_tube_cells, n_ring_cells=n_ring_cells)
        results[n_ring] = U

        print(f"\n  Mode (1, {n_ring}):")
        print(f"    Mean cell size: {mcs:.4f}")
        print(f"    Softening eps:  {eps:.4f}")
        print(f"    U_self:         {U:+.6f}")

    print(f"\n  Sign test:")
    print(f"    U(1,2) = {results[2]:+.6f}")
    print(f"    U(1,3) = {results[3]:+.6f}")

    if results[2] > 0 and results[3] < 0:
        print(f"    *** PREDICTED PATTERN: + for (1,2), - for (1,3) ***")
    elif results[2] < 0 and results[3] > 0:
        print(f"    REVERSED: - for (1,2), + for (1,3)")
    else:
        print(f"    SAME-SIGN: both have sign({np.sign(results[2])})")

    return results


def aspect_scan(r_values, n_tube_cells=20, n_ring_cells=40):
    """Scan U_self vs aspect ratio for both modes."""
    R = 1.0
    U2_arr = np.zeros(len(r_values))
    U3_arr = np.zeros(len(r_values))

    for i, r in enumerate(r_values):
        a = r * R
        for n_ring, arr in [(2, U2_arr), (3, U3_arr)]:
            U, _, _ = compute_self_energy(
                R, a, n_tube=1, n_ring=n_ring,
                n_tube_cells=n_tube_cells, n_ring_cells=n_ring_cells)
            arr[i] = U

    return U2_arr, U3_arr


# ── Test variant: |ψ|² instead of ψ ────────────────────────────────

def signed_charge_density_psi_squared(theta_tube, theta_ring, n_tube=1, n_ring=2):
    """
    Standard QM probability density: ρ = |ψ|² = cos²(n_tube*θ_tube) × cos²(n_ring*θ_ring).
    Always non-negative.  For comparison with the signed-ψ approach.
    """
    tt, tr = np.meshgrid(theta_tube, theta_ring, indexing='ij')
    return (np.cos(n_tube * tt) * np.cos(n_ring * tr)) ** 2


def compute_self_energy_psi_squared(R, a, n_tube, n_ring, n_tube_cells, n_ring_cells, eps_factor=0.5):
    """Self-energy with |ψ|² (always-positive) charge density."""
    pos, dA, theta_tube, theta_ring = torus_grid(R, a, n_tube_cells, n_ring_cells)
    psi_sq = signed_charge_density_psi_squared(theta_tube, theta_ring, n_tube, n_ring)
    # Normalize to total charge = 1
    norm = np.sum(psi_sq * dA)
    charge = psi_sq * dA / norm  # always positive
    pos_flat = pos.reshape(-1, 3)
    charge_flat = charge.flatten()
    mean_cell_size = np.sqrt(dA.mean())
    eps = eps_factor * mean_cell_size
    return coulomb_self_energy(pos_flat, charge_flat, eps)


# ── Main ───────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("R52 Track 4c: Continuous standing-wave self-energy")
    print("=" * 70)
    print(__doc__)

    print("\n" + "=" * 70)
    print("PART 1: Sign test (signed ψ as charge density)")
    print("=" * 70)

    for r in [0.5, 2.0, 8.906]:
        if r == 8.906:
            label = "Proton aspect ratio (R27 F18)"
        else:
            label = f"r = {r}"
        run_sign_test(r, label=label, n_tube_cells=20, n_ring_cells=40)

    print("\n" + "=" * 70)
    print("PART 2: Aspect ratio scan (signed ψ)")
    print("=" * 70)

    r_values = np.linspace(0.3, 15.0, 25)
    U2, U3 = aspect_scan(r_values, n_tube_cells=16, n_ring_cells=32)

    print(f"\n  {'r':>6s}  {'U(1,2)':>12s}  {'U(1,3)':>12s}  {'sign2':>6s}  {'sign3':>6s}")
    print("  " + "─" * 55)
    for i in range(0, len(r_values), 2):
        print(f"  {r_values[i]:6.2f}  {U2[i]:+12.6f}  {U3[i]:+12.6f}  "
              f"{int(np.sign(U2[i])):+6d}  {int(np.sign(U3[i])):+6d}")

    sign_diff = np.sum(np.sign(U2) != np.sign(U3))
    print(f"\n  Aspect ratios with sign difference: {sign_diff} / {len(r_values)}")

    print("\n" + "=" * 70)
    print("PART 3: Comparison with |ψ|² (probability density)")
    print("=" * 70)

    print("\n  At proton aspect ratio (r = 8.906):")
    R, a = 1.0, 8.906
    for n_ring in [2, 3]:
        U_signed = compute_self_energy(R, a, 1, n_ring, 20, 40)[0]
        U_psi2 = compute_self_energy_psi_squared(R, a, 1, n_ring, 20, 40)
        print(f"    (1, {n_ring}):")
        print(f"      Signed ψ:  U = {U_signed:+.6f}")
        print(f"      |ψ|²:       U = {U_psi2:+.6f}")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    ax = axes[0]
    ax.plot(r_values, U2, 'b-o', label='(1, 2) electron', markersize=5)
    ax.plot(r_values, U3, 'r-^', label='(1, 3) proton', markersize=5)
    ax.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax.axvline(8.906, color='g', linestyle=':', alpha=0.5, label='r_p = 8.906')
    ax.set_xlabel('Aspect ratio r = a/R')
    ax.set_ylabel('U_self (signed ψ)')
    ax.set_title('Continuous self-energy vs aspect ratio')
    ax.legend()
    ax.grid(alpha=0.3)

    ax = axes[1]
    ax.plot(r_values, np.sign(U2), 'bo-', label='sign(U(1,2))', markersize=5)
    ax.plot(r_values, np.sign(U3), 'r^-', label='sign(U(1,3))', markersize=5)
    ax.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax.set_xlabel('Aspect ratio r = a/R')
    ax.set_ylabel('Sign')
    ax.set_title('Sign of U_self vs aspect ratio')
    ax.set_ylim(-1.5, 1.5)
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    out = Path(__file__).parent.parent / "track4c_results.png"
    plt.savefig(out, dpi=120)
    print(f"\n  Plot saved to {out}")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    R, a = 1.0, 8.906
    U2_p = compute_self_energy(R, a, 1, 2, 24, 48)[0]
    U3_p = compute_self_energy(R, a, 1, 3, 24, 48)[0]

    print(f"\nAt proton aspect ratio (r = 8.906), high-resolution grid:")
    print(f"  (1, 2):  U_self = {U2_p:+.6f}")
    print(f"  (1, 3):  U_self = {U3_p:+.6f}")

    if U2_p > 0 and U3_p < 0:
        print("\n  *** SUCCESS: predicted sign pattern (+ for (1,2), - for (1,3)) ***")
        print("  *** Sub-track 4c CONFIRMS the three-phase rule ***")
    elif U2_p < 0 and U3_p > 0:
        print("\n  REVERSED")
    elif np.sign(U2_p) == np.sign(U3_p):
        print(f"\n  SAME-SIGN: both have sign({np.sign(U2_p):+.0f})")
        print("  Sub-track 4c does not differentiate the modes")


if __name__ == "__main__":
    main()
