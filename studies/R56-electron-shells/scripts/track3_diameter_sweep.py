"""
R56 Track 3: Sweep effective electron diameter

Does a specific electron diameter produce clean shell closure
at 4 couplets (8 electrons) in shell 2?

If so, we back into the effective EM diameter of the electron
from the observed shell structure.

We sweep R_eff from 10 fm to 10,000 fm and at each value:
  1. Fix 1 core couplet at origin
  2. Add ring couplets one at a time (N = 1 to 8)
  3. Compute the MARGINAL cost of each additional couplet
  4. Look for a sharp jump at N = 4 (shell 2 full at 8 electrons)

The idea: at some R_eff, the geometry of 4 couplets in a ring
around a core is special — a 5th couplet costs much more.
"""

import numpy as np
from scipy.optimize import minimize
import math

ALPHA = 1.0 / 137.036
HC = 197.3269804  # MeV·fm
A0 = 52917.7  # Bohr radius in fm


def V_ne(r, Z, Q_c, R_e):
    """Nucleus to couplet attraction."""
    if r > R_e:
        return -Z * Q_c * ALPHA * HC / r
    else:
        return -Z * Q_c * ALPHA * HC / R_e


def V_cc(d, Q_c, R_e):
    """Couplet-couplet repulsion."""
    if d > R_e:
        return Q_c**2 * ALPHA * HC / d
    else:
        return Q_c**2 * ALPHA * HC / R_e


def ring_energy(N_ring, Z, R_e, r_core=0.0):
    """
    Energy of N_ring couplets in a ring around z-axis, plus
    one core couplet at the origin.

    Optimizes ring radius and z-offset.
    """
    Q = 2.0  # couplet charge

    def energy(params):
        r_ring = abs(params[0])
        z_ring = params[1]
        angles = np.linspace(0, 2*math.pi, N_ring, endpoint=False)

        E = 0.0
        # Core couplet at origin
        E += V_ne(0.001, Z, Q, R_e)  # avoid r=0 singularity

        # Ring couplets
        positions = []
        for a in angles:
            pos = np.array([r_ring * math.cos(a),
                           r_ring * math.sin(a), z_ring])
            positions.append(pos)
            r = np.linalg.norm(pos)
            E += V_ne(r, Z, Q, R_e)

        # Core-ring interactions
        for pos in positions:
            d = np.linalg.norm(pos)
            E += V_cc(d, Q, R_e)

        # Ring-ring interactions
        for i in range(N_ring):
            for j in range(i+1, N_ring):
                d = np.linalg.norm(positions[i] - positions[j])
                E += V_cc(d, Q, R_e)

        return E

    best = None
    for trial in range(20):
        r0 = A0 / Z * (0.2 + 0.8 * np.random.rand())
        z0 = (np.random.rand() - 0.5) * r0 * 0.5
        x0 = np.array([r0, z0])
        result = minimize(energy, x0, method='L-BFGS-B',
                         bounds=[(R_e * 0.1, A0), (-A0, A0)])
        if best is None or result.fun < best.fun:
            best = result

    return best.fun, abs(best.x[0])


def main():
    print("=" * 70)
    print("R56 Track 3: Sweep effective electron diameter")
    print("=" * 70)
    print()
    print("For each R_eff, add ring couplets one at a time around")
    print("a core couplet.  Look for a jump in marginal energy at")
    print("N_ring = 4 → 5 (shell 2 full at 8 electrons).")
    print()

    Z = 10  # neon: 5 couplets = 10 electrons

    # Sweep R_eff
    R_values = [10, 30, 50, 100, 200, 386, 500, 751, 1000,
                1500, 2000, 3000, 5000, 7500, 10000]

    print(f"  Z = {Z} (neon)")
    print()

    # For each R_eff, compute marginal energy of ring couplets 1-7
    print(f"  {'R_eff':>7s}  ", end='')
    for n in range(1, 8):
        print(f"{'ΔE_'+str(n):>9s}  ", end='')
    print(f"  {'jump_4→5':>10s}  {'ratio':>6s}")

    print(f"  {'(fm)':>7s}  ", end='')
    for n in range(1, 8):
        print(f"{'(keV)':>9s}  ", end='')
    print(f"  {'(keV)':>10s}  {'':>6s}")

    print(f"  {'─'*7}  " + "─"*9 + "  " * 6 + f"  {'─'*10}  {'─'*6}")

    results = []

    for R_eff in R_values:
        energies = []
        # Baseline: just core
        E_core = V_ne(0.001, Z, 2.0, R_eff)  # crude core energy
        prev_E = E_core

        marginals = []
        for N_ring in range(1, 8):
            E_total, r_ring = ring_energy(N_ring, Z, R_eff)
            dE = (E_total - prev_E) * 1e3  # MeV → keV
            marginals.append(dE)
            prev_E = E_total

        # The jump at 4→5: how much more expensive is the 5th vs 4th
        if len(marginals) >= 5:
            jump = marginals[4] - marginals[3]
            ratio = marginals[4] / marginals[3] if marginals[3] != 0 else 0
        else:
            jump = 0
            ratio = 0

        results.append((R_eff, marginals, jump, ratio))

        print(f"  {R_eff:>7.0f}  ", end='')
        for dE in marginals:
            print(f"{dE:>+9.2f}  ", end='')
        print(f"  {jump:>+10.2f}  {ratio:>6.2f}")

    print()

    # Find R_eff where the 4→5 jump is largest
    best_jump = max(results, key=lambda x: x[2])
    print(f"  Largest jump at 4→5: R_eff = {best_jump[0]:.0f} fm "
          f"(jump = {best_jump[2]:+.2f} keV)")
    print()

    # Also check: where is the ratio marginal[5]/marginal[4] largest?
    best_ratio = max(results, key=lambda x: x[3])
    print(f"  Largest ratio ΔE_5/ΔE_4: R_eff = {best_ratio[0]:.0f} fm "
          f"(ratio = {best_ratio[3]:.2f})")
    print()

    # ── Fine sweep around the best region ──────────────────────
    if best_jump[0] > 30:
        lo = max(10, best_jump[0] * 0.3)
        hi = best_jump[0] * 3
    else:
        lo, hi = 10, 1000

    print(f"  Fine sweep: R_eff in [{lo:.0f}, {hi:.0f}] fm")
    print()

    fine_R = np.linspace(lo, hi, 30)
    print(f"  {'R_eff':>7s}  {'ΔE_4':>9s}  {'ΔE_5':>9s}  "
          f"{'jump':>9s}  {'ratio':>6s}")
    print(f"  {'─'*7}  {'─'*9}  {'─'*9}  {'─'*9}  {'─'*6}")

    for R_eff in fine_R:
        E4, _ = ring_energy(4, Z, float(R_eff))
        E3, _ = ring_energy(3, Z, float(R_eff))
        E5, _ = ring_energy(5, Z, float(R_eff))

        dE4 = (E4 - E3) * 1e3
        dE5 = (E5 - E4) * 1e3
        jump = dE5 - dE4
        ratio = dE5 / dE4 if dE4 != 0 else 0

        print(f"  {R_eff:>7.0f}  {dE4:>+9.2f}  {dE5:>+9.2f}  "
              f"{jump:>+9.2f}  {ratio:>6.2f}")

    print()
    print("Track 3 complete.")


if __name__ == '__main__':
    main()
