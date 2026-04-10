"""
R52 Track 4d: Continuous self-energy WITH shear.

EXTENSION OF TRACK 4c.
Track 4c computed the Coulomb self-energy of a signed standing wave
ψ = cos(θ_tube) × cos(n_ring × θ_ring) and found it gave same-sign
results for n_ring = 2 and n_ring = 3 at the proton's aspect ratio.

This track adds SHEAR to the wave: instead of integer ring winding
n_ring, the wave has effective ring winding (n_ring - s) where s is
the shear that gives α via the standard MaSt formula.

PHYSICAL MOTIVATION:
- Charge is an artifact of integer tube windings (cannot be sheared).
- Magnetic moment comes from ring trips, which CAN have non-integer
  shear corrections.
- Track 2 found a residual ∝ s²/n_ring from shear in the B-field
  surface integral (always positive — quadratic measure can't flip
  sign).
- This track tests whether the SAME shear, applied to the SCALAR
  signed-ψ self-energy, produces sign-dependent corrections.

WAVE CONSTRUCTION:
ψ_sheared(θ_t, θ_r) = cos(n_tube × θ_t) × cos((n_ring - s) × θ_r)

For (1, 2) electron: cos(θ_t) × cos((2 - s_e) θ_r)
For (1, 3) proton:   cos(θ_t) × cos((3 - s_p) θ_r)

The shear breaks the integer periodicity in θ_r — the wave does not
return to itself after one ring trip.

ASSUMPTIONS:
- Shear values from MaSt: s_e = α (small), s_p = α' (depends on r_p)
- For now, use small literal shear values to test sensitivity
- Same chord-distance discretization as Track 4c
- Two grid resolutions to check convergence
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from lib.ma_model_d import alpha_from_geometry as alpha_ma, solve_shear_for_alpha


# ── Surface discretization (same as 4c) ────────────────────────────

def torus_grid(R, a, n_tube_cells, n_ring_cells):
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
    dtheta_t = 2 * np.pi / n_tube_cells
    dtheta_r = 2 * np.pi / n_ring_cells
    dA = a * rho * dtheta_t * dtheta_r
    return pos, dA, theta_tube, theta_ring


def signed_charge_density_sheared(theta_tube, theta_ring, n_tube=1, n_ring=2, shear=0.0):
    """
    Sheared signed charge density:
        ρ ∝ cos(n_tube × θ_t) × cos((n_ring - shear) × θ_r)
    """
    tt, tr = np.meshgrid(theta_tube, theta_ring, indexing='ij')
    return np.cos(n_tube * tt) * np.cos((n_ring - shear) * tr)


# ── Self-energy computation ─────────────────────────────────────────

def coulomb_self_energy(pos, charge, eps):
    """U = (1/2) Σ_{i≠j} q_i q_j / |r_i - r_j| with softening eps."""
    diff = pos[:, None, :] - pos[None, :, :]
    dist = np.linalg.norm(diff, axis=-1)
    np.fill_diagonal(dist, np.inf)
    dist = np.maximum(dist, eps)
    qq = charge[:, None] * charge[None, :]
    return 0.5 * np.sum(qq / dist)


def compute_self_energy(R, a, n_tube, n_ring, shear, n_tube_cells=24, n_ring_cells=48,
                         eps_factor=0.5):
    """Self-energy of the sheared wave."""
    pos, dA, tt, tr = torus_grid(R, a, n_tube_cells, n_ring_cells)
    psi = signed_charge_density_sheared(tt, tr, n_tube, n_ring, shear)
    charge = (psi * dA).flatten()
    pos_flat = pos.reshape(-1, 3)
    mean_cell_size = np.sqrt(dA.mean())
    eps = eps_factor * mean_cell_size
    return coulomb_self_energy(pos_flat, charge, eps)


# ── Sign test ───────────────────────────────────────────────────────

def run_sign_test(r_aspect, shear_values, R=1.0, n_tube_cells=24, n_ring_cells=48,
                  label=""):
    """
    Compute self-energy for (1,2) and (1,3) at multiple shear values.

    Compare U(shear) - U(0) for each mode.  Sign of the SHEAR
    contribution might differ between modes.
    """
    a = r_aspect * R

    print(f"\n── {label} (r = {r_aspect}) ──")
    print(f"  R = {R}, a = {a}")
    print(f"  Grid: {n_tube_cells} × {n_ring_cells}")

    print(f"\n  {'shear':>10s}  {'U(1,2)':>14s}  {'U(1,3)':>14s}  "
          f"{'δU(1,2)':>14s}  {'δU(1,3)':>14s}")
    print("  " + "─" * 75)

    U2_0 = compute_self_energy(R, a, 1, 2, 0.0, n_tube_cells, n_ring_cells)
    U3_0 = compute_self_energy(R, a, 1, 3, 0.0, n_tube_cells, n_ring_cells)

    results = []
    for s in shear_values:
        U2 = compute_self_energy(R, a, 1, 2, s, n_tube_cells, n_ring_cells)
        U3 = compute_self_energy(R, a, 1, 3, s, n_tube_cells, n_ring_cells)
        dU2 = U2 - U2_0
        dU3 = U3 - U3_0
        results.append((s, U2, U3, dU2, dU3))
        print(f"  {s:10.5f}  {U2:+14.4f}  {U3:+14.4f}  {dU2:+14.4f}  {dU3:+14.4f}")

    # Sign test on δU
    print(f"\n  Sign test on δU = U(s) - U(0):")
    for s, U2, U3, dU2, dU3 in results[:3]:
        if s == 0:
            continue
        sign2 = np.sign(dU2)
        sign3 = np.sign(dU3)
        marker = ""
        if sign2 > 0 and sign3 < 0:
            marker = "  *** PREDICTED PATTERN ***"
        elif sign2 < 0 and sign3 > 0:
            marker = "  REVERSED"
        elif sign2 == sign3:
            marker = f"  same sign ({int(sign2):+d})"
        print(f"    s={s:.4f}: sign(δU2)={int(sign2):+d}, sign(δU3)={int(sign3):+d}{marker}")

    return results


# ── Shear scan ──────────────────────────────────────────────────────

def shear_scan(r_aspect, R=1.0, n_tube_cells=20, n_ring_cells=40):
    """Scan over shear values to look for sign transitions."""
    a = r_aspect * R
    s_values = np.linspace(-0.05, 0.05, 21)

    U2_arr = np.zeros(len(s_values))
    U3_arr = np.zeros(len(s_values))

    for i, s in enumerate(s_values):
        U2_arr[i] = compute_self_energy(R, a, 1, 2, s, n_tube_cells, n_ring_cells)
        U3_arr[i] = compute_self_energy(R, a, 1, 3, s, n_tube_cells, n_ring_cells)

    return s_values, U2_arr, U3_arr


# ── Main ───────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("R52 Track 4d: Continuous self-energy WITH shear")
    print("=" * 70)
    print(__doc__)

    print("\n" + "=" * 70)
    print("PART 1: Sign test at proton aspect ratio with various shear")
    print("=" * 70)

    # Use realistic shear values: small (test convergence), moderate, large
    shear_values = [0.0, 0.001, 0.005, 0.01, 0.02, 0.05]

    run_sign_test(8.906, shear_values, label="Proton aspect ratio")

    print("\n" + "=" * 70)
    print("PART 2: Shear scan at proton aspect ratio")
    print("=" * 70)

    s_values, U2, U3 = shear_scan(8.906, n_tube_cells=24, n_ring_cells=48)

    print(f"\n  {'shear':>8s}  {'U(1,2)':>14s}  {'U(1,3)':>14s}  "
          f"{'sign2':>6s}  {'sign3':>6s}")
    print("  " + "─" * 60)
    for i in range(len(s_values)):
        print(f"  {s_values[i]:+8.4f}  {U2[i]:+14.4f}  {U3[i]:+14.4f}  "
              f"{int(np.sign(U2[i])):+6d}  {int(np.sign(U3[i])):+6d}")

    sign_diff = np.sum(np.sign(U2) != np.sign(U3))
    print(f"\n  Shear values with sign difference: {sign_diff} / {len(s_values)}")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    ax = axes[0]
    ax.plot(s_values, U2, 'b-o', label='(1, 2) electron', markersize=5)
    ax.plot(s_values, U3, 'r-^', label='(1, 3) proton', markersize=5)
    ax.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax.axvline(0, color='k', linestyle=':', alpha=0.3)
    ax.set_xlabel('Shear s')
    ax.set_ylabel('U_self')
    ax.set_title('U_self vs shear at r = 8.906')
    ax.legend()
    ax.grid(alpha=0.3)

    # Plot δU = U(s) - U(0)
    ax = axes[1]
    U2_0 = U2[len(s_values) // 2]  # at s = 0
    U3_0 = U3[len(s_values) // 2]
    dU2 = U2 - U2_0
    dU3 = U3 - U3_0
    ax.plot(s_values, dU2, 'b-o', label='δU(1,2)', markersize=5)
    ax.plot(s_values, dU3, 'r-^', label='δU(1,3)', markersize=5)
    ax.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax.axvline(0, color='k', linestyle=':', alpha=0.3)
    ax.set_xlabel('Shear s')
    ax.set_ylabel('δU = U(s) - U(0)')
    ax.set_title('Shear-induced correction to U_self')
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    out = Path(__file__).parent.parent / "track4d_results.png"
    plt.savefig(out, dpi=120)
    print(f"\n  Plot saved to {out}")

    # ── Summary ──
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    # Compute with realistic shear values if MaSt API allows
    print("\nAt proton aspect ratio (r=8.906) with realistic shear:")
    try:
        s_e = solve_shear_for_alpha(0.5)  # electron r ≈ 0.5
        s_p = solve_shear_for_alpha(8.906)  # proton r ≈ 8.906
        print(f"  s_e (from MaSt) = {s_e:.6f}")
        print(f"  s_p (from MaSt) = {s_p:.6f}")

        U2_e = compute_self_energy(1.0, 0.5, 1, 2, s_e, 24, 48)
        U2_e0 = compute_self_energy(1.0, 0.5, 1, 2, 0.0, 24, 48)
        U3_p = compute_self_energy(1.0, 8.906, 1, 3, s_p, 24, 48)
        U3_p0 = compute_self_energy(1.0, 8.906, 1, 3, 0.0, 24, 48)

        print(f"\n  Electron at r=0.5, s={s_e:.4f}:")
        print(f"    U(s)  = {U2_e:+.4f}")
        print(f"    U(0)  = {U2_e0:+.4f}")
        print(f"    δU    = {U2_e - U2_e0:+.6f}")
        print(f"    sign  = {int(np.sign(U2_e - U2_e0)):+d}")

        print(f"\n  Proton at r=8.906, s={s_p:.4f}:")
        print(f"    U(s)  = {U3_p:+.4f}")
        print(f"    U(0)  = {U3_p0:+.4f}")
        print(f"    δU    = {U3_p - U3_p0:+.6f}")
        print(f"    sign  = {int(np.sign(U3_p - U3_p0)):+d}")

        if np.sign(U2_e - U2_e0) > 0 and np.sign(U3_p - U3_p0) < 0:
            print("\n  *** PREDICTED PATTERN: + for electron, - for proton ***")
        elif np.sign(U2_e - U2_e0) < 0 and np.sign(U3_p - U3_p0) > 0:
            print("\n  REVERSED")
        else:
            print(f"\n  SAME-SIGN: both have sign({np.sign(U2_e - U2_e0):+.0f})")
    except Exception as exc:
        print(f"  (could not compute realistic shear: {exc})")


if __name__ == "__main__":
    main()
