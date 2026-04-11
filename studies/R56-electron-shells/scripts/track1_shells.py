"""
R56 Track 1: Electron shell structure from geometric packing

Model each electron as a uniform spherical shell of charge -e
at radius R_eff.  Nucleus is +Ze point charge at origin.

Energy:
  E_total = Σ_i V_ne(r_i) + Σ_{i<j} V_ee(r_i, r_j)

where:
  V_ne = electron-nucleus (attraction, modified inside R_eff)
  V_ee = electron-electron (repulsion, soft when overlapping)

Shell-by-shell buildup:
  Shell 1: polar electrons (N = 1..4)
  Shell 2: equatorial ring (N_ring = 2..12, with 2 polar fixed)
  Shell 3: groove rings (N_groove = 2..6 per ring, with 2+8 fixed)
"""

import numpy as np
from scipy.optimize import minimize
import math

# ════════════════════════════════════════════════════════════════
#  Physical constants
# ════════════════════════════════════════════════════════════════

ALPHA = 1.0 / 137.036
HC = 197.3269804  # MeV·fm
A0 = 52917.7  # Bohr radius in fm
E_HARTREE = ALPHA**2 * 0.511  # ~27.2 eV in MeV → 2.72e-5 MeV

# Electron radii to test (fm)
R_MODEL_A = 4717.0 / (2 * math.pi)  # L_tube / 2π = 751 fm
R_MODEL_B = HC / 0.511              # ℏ/mc = reduced Compton = 386 fm


# ════════════════════════════════════════════════════════════════
#  Interaction potentials for spherical-shell electrons
# ════════════════════════════════════════════════════════════════

def V_nucleus_electron(r, Z, R_e):
    """
    Coulomb energy between a point nucleus +Ze at origin and a
    spherical shell of charge -e at radius R_e centered at
    distance r from origin.

    Shell theorem:
      r > R_e: V = -Z α ℏc / r  (same as point-point)
      r < R_e: V = -Z α ℏc / R_e (electron encloses nucleus)
    """
    if r > R_e:
        return -Z * ALPHA * HC / r
    else:
        return -Z * ALPHA * HC / R_e


def V_electron_electron(d, R_e):
    """
    Coulomb energy between two spherical shells of charge -e,
    each of radius R_e, separated by distance d (center-to-center).

    Shell theorem:
      d > 2R_e: V = α ℏc / d  (same as point-point)
      d = 0: V = α ℏc / R_e  (concentric shells)
      0 < d < 2R_e: smooth interpolation (shells overlap)

    For overlapping shells, we use the exact result for two
    uniform spherical shells.  The potential of shell 1 at a
    point inside it is constant = α ℏc / R_e.  Shell 2's center
    is at distance d.  The energy is the integral of shell 2's
    charge in the potential of shell 1.

    For simplicity (and speed), we use a smooth interpolation:
      V(d) = α ℏc / max(d, R_e)  for d > R_e
      V(d) = α ℏc / R_e          for d < R_e

    This is actually exact for the case of one shell inside the
    other (d < R_e → the outer shell sees the inner as a point
    at its center, and the inner sees a uniform potential from
    the outer).  For partial overlap (R_e < d < 2R_e), this
    slightly overestimates repulsion compared to the full
    integral, which is conservative (makes packing harder).
    """
    if d > R_e:
        return ALPHA * HC / d
    else:
        return ALPHA * HC / R_e


def total_energy(positions, Z, R_e):
    """
    Total energy of N electrons at given positions around +Ze nucleus.
    positions: array of shape (N, 3)
    """
    N = len(positions)
    E = 0.0

    # Electron-nucleus
    for i in range(N):
        r = np.linalg.norm(positions[i])
        E += V_nucleus_electron(r, Z, R_e)

    # Electron-electron
    for i in range(N):
        for j in range(i + 1, N):
            d = np.linalg.norm(positions[i] - positions[j])
            E += V_electron_electron(d, R_e)

    return E


# ════════════════════════════════════════════════════════════════
#  Shell 1: polar electrons
# ════════════════════════════════════════════════════════════════

def optimize_shell1(N, Z, R_e):
    """
    N electrons around +Ze nucleus with no constraints.
    For N=1: one electron at optimal r.
    For N=2: two electrons on opposite sides (polar axis).
    For N>2: free optimization.
    """
    def energy(params):
        positions = params.reshape(-1, 3)
        return total_energy(positions, Z, R_e)

    best = None
    for trial in range(20):
        # Random initial positions at ~Bohr radius
        x0 = np.random.randn(N, 3) * A0 * 0.5 / Z
        result = minimize(energy, x0.flatten(), method='L-BFGS-B')
        if best is None or result.fun < best.fun:
            best = result

    positions = best.x.reshape(-1, 3)
    radii = np.linalg.norm(positions, axis=1)
    return best.fun, positions, radii


# ════════════════════════════════════════════════════════════════
#  Shell 2: equatorial ring with fixed polar electrons
# ════════════════════════════════════════════════════════════════

def optimize_shell2(N_ring, Z, R_e, r_polar):
    """
    2 polar electrons (fixed at ±r_polar on z-axis) plus
    N_ring electrons in the xy-plane (equatorial ring).
    Optimize ring radius and angular positions.
    """
    polar = np.array([[0, 0, r_polar], [0, 0, -r_polar]])

    def energy(params):
        r_ring = abs(params[0])
        angles = params[1:N_ring + 1]
        ring_pos = np.column_stack([
            r_ring * np.cos(angles),
            r_ring * np.sin(angles),
            np.zeros(N_ring)
        ])
        all_pos = np.vstack([polar, ring_pos])
        return total_energy(all_pos, Z, R_e)

    best = None
    for trial in range(20):
        r0 = A0 / Z * (0.3 + 0.7 * np.random.rand())
        angles0 = np.linspace(0, 2 * np.pi, N_ring, endpoint=False)
        angles0 += np.random.randn(N_ring) * 0.1
        x0 = np.concatenate([[r0], angles0])
        result = minimize(energy, x0, method='L-BFGS-B')
        if best is None or result.fun < best.fun:
            best = result

    r_ring = abs(best.x[0])
    return best.fun, r_ring


# ════════════════════════════════════════════════════════════════
#  Shell 3: groove rings with fixed shell 1 + 2
# ════════════════════════════════════════════════════════════════

def optimize_shell3(N_per_groove, Z, R_e, r_polar, r_ring):
    """
    2 polar + 8 equatorial (fixed) + 2 groove rings at ±latitude.
    Each groove has N_per_groove electrons.
    Optimize: groove latitude (theta), groove radius, angles.
    """
    polar = np.array([[0, 0, r_polar], [0, 0, -r_polar]])
    eq_angles = np.linspace(0, 2 * np.pi, 8, endpoint=False)
    equatorial = np.column_stack([
        r_ring * np.cos(eq_angles),
        r_ring * np.sin(eq_angles),
        np.zeros(8)
    ])
    fixed = np.vstack([polar, equatorial])

    def energy(params):
        r_g = abs(params[0])
        theta = params[1]  # latitude angle from equator
        angles_top = params[2:2 + N_per_groove]
        angles_bot = params[2 + N_per_groove:2 + 2 * N_per_groove]

        z_top = r_g * np.sin(theta)
        rho_top = r_g * np.cos(theta)
        z_bot = -z_top

        top = np.column_stack([
            rho_top * np.cos(angles_top),
            rho_top * np.sin(angles_top),
            np.full(N_per_groove, z_top)
        ])
        bot = np.column_stack([
            rho_top * np.cos(angles_bot),
            rho_top * np.sin(angles_bot),
            np.full(N_per_groove, z_bot)
        ])
        all_pos = np.vstack([fixed, top, bot])
        return total_energy(all_pos, Z, R_e)

    best = None
    for trial in range(20):
        r0 = r_ring * (1.0 + 0.5 * np.random.rand())
        theta0 = 0.5 + 0.3 * np.random.randn()
        ang_top = np.linspace(0, 2 * np.pi, N_per_groove, endpoint=False)
        ang_top += np.random.randn(N_per_groove) * 0.1
        ang_bot = ang_top + np.pi / N_per_groove  # staggered
        ang_bot += np.random.randn(N_per_groove) * 0.1
        x0 = np.concatenate([[r0, theta0], ang_top, ang_bot])
        result = minimize(energy, x0, method='L-BFGS-B')
        if best is None or result.fun < best.fun:
            best = result

    return best.fun


# ════════════════════════════════════════════════════════════════
#  Main
# ════════════════════════════════════════════════════════════════

def run_model(R_e, label):
    print(f"\n{'='*70}")
    print(f"  {label}: R_eff = {R_e:.1f} fm ({R_e/A0*100:.2f}% of Bohr radius)")
    print(f"{'='*70}\n")

    Z = 20  # Use a moderate Z for clear shell structure

    # ── Shell 1 ────────────────────────────────────────────────
    print(f"  SHELL 1: N polar electrons around Z={Z} nucleus")
    print(f"  {'N':>4s}  {'E_total (keV)':>14s}  {'E/N (keV)':>12s}  "
          f"{'ΔE (keV)':>10s}  {'r_avg (pm)':>10s}")
    print(f"  {'─'*4}  {'─'*14}  {'─'*12}  {'─'*10}  {'─'*10}")

    shell1_energies = []
    r_polar_best = None
    for N in range(1, 6):
        E, pos, radii = optimize_shell1(N, Z, R_e)
        E_keV = E * 1e3  # MeV → keV
        E_per = E_keV / N
        dE = E_keV - shell1_energies[-1] if shell1_energies else E_keV
        r_avg = np.mean(radii)
        shell1_energies.append(E_keV)
        if N == 2:
            r_polar_best = np.max(radii)
        print(f"  {N:>4d}  {E_keV:>14.4f}  {E_per:>12.4f}  "
              f"{dE:>+10.4f}  {r_avg/100:>10.2f}")

    print()
    print(f"  Energy cost of Nth electron (ΔE):")
    print(f"  Minimum at N where adding next electron costs more.")
    print(f"  If ΔE jumps up sharply at N=3, shell 1 closes at 2.")
    print()

    if r_polar_best is None:
        r_polar_best = A0 / Z

    # ── Shell 2 ────────────────────────────────────────────────
    print(f"  SHELL 2: equatorial ring (2 polar fixed at r={r_polar_best/100:.2f} pm)")
    print(f"  {'N_ring':>6s}  {'N_total':>7s}  {'E_total (keV)':>14s}  "
          f"{'E/N (keV)':>12s}  {'ΔE (keV)':>10s}  {'r_ring (pm)':>12s}")
    print(f"  {'─'*6}  {'─'*7}  {'─'*14}  {'─'*12}  {'─'*10}  {'─'*12}")

    shell2_energies = []
    r_ring_best = None
    prev_E = shell1_energies[1]  # baseline = 2 electrons
    for N_ring in range(2, 14, 2):
        N_total = 2 + N_ring
        E, r_ring = optimize_shell2(N_ring, Z, R_e, r_polar_best)
        E_keV = E * 1e3
        E_per = E_keV / N_total
        dE = E_keV - prev_E
        dE_per = dE / N_ring if N_ring > 0 else 0
        shell2_energies.append((N_ring, E_keV, r_ring))
        prev_E = E_keV
        if N_ring == 8:
            r_ring_best = r_ring
        print(f"  {N_ring:>6d}  {N_total:>7d}  {E_keV:>14.4f}  "
              f"{E_per:>12.4f}  {dE:>+10.4f}  {r_ring/100:>12.2f}")

    if r_ring_best is None and shell2_energies:
        r_ring_best = shell2_energies[-1][2]

    print()

    # ── Shell 3 ────────────────────────────────────────────────
    print(f"  SHELL 3: groove rings (2 polar + 8 equatorial fixed)")
    print(f"  {'N/groove':>8s}  {'N_total':>7s}  {'E_total (keV)':>14s}  "
          f"{'E/N (keV)':>12s}  {'ΔE (keV)':>10s}")
    print(f"  {'─'*8}  {'─'*7}  {'─'*14}  {'─'*12}  {'─'*10}")

    base_E = None
    for s2 in shell2_energies:
        if s2[0] == 8:
            base_E = s2[1]
    if base_E is None:
        base_E = shell2_energies[-1][1] if shell2_energies else 0

    prev_E = base_E
    for N_groove in range(2, 8):
        N_total = 2 + 8 + 2 * N_groove
        E = optimize_shell3(N_groove, Z, R_e, r_polar_best, r_ring_best)
        E_keV = E * 1e3
        E_per = E_keV / N_total
        dE = E_keV - prev_E
        prev_E = E_keV
        print(f"  {N_groove:>8d}  {N_total:>7d}  {E_keV:>14.4f}  "
              f"{E_per:>12.4f}  {dE:>+10.4f}")

    print()


def main():
    print("=" * 70)
    print("R56: Electron shell structure from geometric packing")
    print("=" * 70)
    print()
    print("Each electron is a spherical shell of charge at radius R_eff.")
    print("Nucleus is a point charge +Ze.")
    print("Energy minimization determines packing geometry.")
    print()

    run_model(R_MODEL_A, "Model A (L_tube/2π = 751 fm)")
    run_model(R_MODEL_B, "Model B (ℏ/mc = 386 fm)")

    print("=" * 70)
    print("R56 Track 1 complete.")
    print("=" * 70)


if __name__ == '__main__':
    main()
