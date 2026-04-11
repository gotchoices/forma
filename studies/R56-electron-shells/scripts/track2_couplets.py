"""
R56 Track 2: Couplet packing

An electron couplet = two electrons at the same S coordinate with
opposite tube winding (+1 and -1).  Properties:
  - Charge: -2e
  - Spin: 0
  - Magnetic moment: 0 (dipoles cancel)
  - Size: Compton-scale sphere (same as one electron)

Shell model:
  - Shell 0: one couplet co-centric with nucleus (= helium core)
  - Shell 1: a ring of N couplets around the core
  - Question: is there a natural energy minimum at N = 4 (= 8 electrons)?

We test: for a nucleus of charge +Ze, with one couplet at the center,
how does the energy per additional couplet change as we add more to
a ring?  Is there a discontinuity at 4?

Also test without a central couplet: just N couplets around a bare
nucleus.  Does the FIRST couplet prefer to be at the center?
"""

import numpy as np
from scipy.optimize import minimize
import math

ALPHA = 1.0 / 137.036
HC = 197.3269804  # MeV·fm
A0 = 52917.7  # Bohr radius in fm

R_EFF = 4717.0 / (2 * math.pi)  # 751 fm (model-E electron)
Q_COUPLET = 2.0  # charge magnitude (in units of e)


def V_ne(r, Z, R_e):
    """Nucleus (+Ze) to couplet (-2e) attraction."""
    if r > R_e:
        return -Z * Q_COUPLET * ALPHA * HC / r
    else:
        return -Z * Q_COUPLET * ALPHA * HC / R_e


def V_cc(d, R_e):
    """Couplet-couplet repulsion (both charge -2e)."""
    if d > R_e:
        return Q_COUPLET**2 * ALPHA * HC / d
    else:
        return Q_COUPLET**2 * ALPHA * HC / R_e


def total_energy(positions, Z, R_e, fixed_positions=None):
    """Total energy of mobile couplets + any fixed couplets."""
    all_pos = list(positions)
    if fixed_positions is not None:
        all_pos = list(fixed_positions) + all_pos
    N = len(all_pos)
    N_fixed = len(fixed_positions) if fixed_positions is not None else 0

    E = 0.0
    for i in range(N):
        r = np.linalg.norm(all_pos[i])
        E += V_ne(r, Z, R_e)
    for i in range(N):
        for j in range(i + 1, N):
            d = np.linalg.norm(np.array(all_pos[i]) - np.array(all_pos[j]))
            E += V_cc(d, R_e)
    return E


def optimize_ring(N_ring, Z, R_e, fixed_core=True):
    """
    Optimize N_ring couplets in a ring, optionally with a fixed
    couplet at the origin (the helium core).
    """
    fixed = [np.array([0.0, 0.0, 0.0])] if fixed_core else None

    def energy(params):
        r_ring = abs(params[0])
        theta = params[1]  # tilt angle of ring plane from xy
        angles = params[2:2 + N_ring]
        # Ring in a plane tilted by theta from xy
        cos_t, sin_t = math.cos(theta), math.sin(theta)
        positions = []
        for a in angles:
            x = r_ring * math.cos(a)
            y = r_ring * math.sin(a) * cos_t
            z = r_ring * math.sin(a) * sin_t
            positions.append(np.array([x, y, z]))
        return total_energy(positions, Z, R_e, fixed)

    best = None
    for trial in range(30):
        r0 = A0 / Z * (0.3 + np.random.rand())
        theta0 = np.random.rand() * math.pi
        angles0 = np.linspace(0, 2 * math.pi, N_ring, endpoint=False)
        angles0 += np.random.randn(N_ring) * 0.2
        x0 = np.concatenate([[r0, theta0], angles0])
        result = minimize(energy, x0, method='L-BFGS-B')
        if best is None or result.fun < best.fun:
            best = result

    return best.fun, abs(best.x[0])


def optimize_free(N_total, Z, R_e):
    """Freely optimize N couplets with no constraints."""
    def energy(params):
        positions = [np.array(params[3*i:3*i+3]) for i in range(N_total)]
        return total_energy(positions, Z, R_e)

    best = None
    for trial in range(30):
        x0 = np.random.randn(3 * N_total) * A0 / Z * 0.5
        result = minimize(energy, x0, method='L-BFGS-B')
        if best is None or result.fun < best.fun:
            best = result

    positions = [best.x[3*i:3*i+3] for i in range(N_total)]
    radii = [np.linalg.norm(p) for p in positions]
    return best.fun, positions, radii


def main():
    print("=" * 70)
    print("R56 Track 2: Couplet packing")
    print("=" * 70)
    print()
    print("Each couplet: charge = -2e, spin = 0, moment = 0")
    print(f"R_eff = {R_EFF:.1f} fm")
    print()

    # ── Test 1: Free packing (no assumed shell structure) ──────
    print("TEST 1: Free packing of N couplets around Z=10 nucleus")
    print("(No assumed shell structure — let optimizer find geometry)")
    print()

    Z = 10
    print(f"  {'N_coup':>6s}  {'N_elec':>6s}  {'E (keV)':>10s}  "
          f"{'E/coup':>10s}  {'ΔE':>10s}  {'radii (pm)':>30s}")
    print(f"  {'─'*6}  {'─'*6}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*30}")

    prev_E = 0
    for N in range(1, 8):
        E, positions, radii = optimize_free(N, Z, R_EFF)
        E_keV = E * 1e3
        dE = E_keV - prev_E
        prev_E = E_keV
        radii_sorted = sorted(radii)
        radii_str = ', '.join(f'{r/100:.1f}' for r in radii_sorted)
        print(f"  {N:>6d}  {2*N:>6d}  {E_keV:>10.2f}  "
              f"{E_keV/N:>10.2f}  {dE:>+10.2f}  {radii_str}")

    print()

    # ── Test 2: Ring around core ───────────────────────────────
    print("TEST 2: Ring of N couplets around a core couplet (Z=10)")
    print("(One couplet fixed at origin = helium core)")
    print()

    print(f"  {'N_ring':>6s}  {'N_total':>7s}  {'E (keV)':>10s}  "
          f"{'E/total':>10s}  {'ΔE/coup':>10s}  {'r_ring (pm)':>12s}")
    print(f"  {'─'*6}  {'─'*7}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*12}")

    prev_E = None
    for N_ring in range(1, 9):
        N_total = 1 + N_ring
        E, r_ring = optimize_ring(N_ring, Z, R_EFF, fixed_core=True)
        E_keV = E * 1e3
        if prev_E is None:
            # Baseline: just the core couplet
            E_core, _, _ = optimize_free(1, Z, R_EFF)
            prev_E = E_core * 1e3
        dE = (E_keV - prev_E) / N_ring if N_ring > 0 else 0
        prev_E = E_keV
        print(f"  {N_ring:>6d}  {N_total:>7d}  {E_keV:>10.2f}  "
              f"{E_keV/N_total:>10.2f}  {dE:>+10.2f}  {r_ring/100:>12.2f}")

    print()

    # ── Test 3: Higher Z to see shell structure more clearly ───
    print("TEST 3: Free packing at Z=18 (argon = 9 couplets)")
    print()

    Z = 18
    print(f"  {'N_coup':>6s}  {'E (keV)':>10s}  {'ΔE':>10s}  "
          f"{'radii (pm)':>40s}")
    print(f"  {'─'*6}  {'─'*10}  {'─'*10}  {'─'*40}")

    prev_E = 0
    for N in range(1, 12):
        E, positions, radii = optimize_free(N, Z, R_EFF)
        E_keV = E * 1e3
        dE = E_keV - prev_E
        prev_E = E_keV
        radii_sorted = sorted(radii)
        # Show radii grouped by shell (cluster by proximity)
        radii_str = ', '.join(f'{r/100:.1f}' for r in radii_sorted[:6])
        if len(radii_sorted) > 6:
            radii_str += f' ... +{len(radii_sorted)-6} more'
        print(f"  {N:>6d}  {E_keV:>10.2f}  {dE:>+10.2f}  {radii_str}")

    print()

    # ── Test 4: Does the first couplet prefer the center? ──────
    print("TEST 4: Does the first couplet sit AT the nucleus?")
    print()

    Z = 10
    E1, pos1, radii1 = optimize_free(1, Z, R_EFF)
    print(f"  Z={Z}, 1 couplet: r = {radii1[0]/100:.4f} pm")
    print(f"  R_eff = {R_EFF/100:.4f} pm")
    if radii1[0] < R_EFF:
        print(f"  → Couplet is INSIDE its own radius — it encloses the nucleus")
        print(f"    (the electron bubble sits on top of the nucleus)")
    else:
        print(f"  → Couplet is outside its own radius")
    print()

    print("Track 2 complete.")


if __name__ == '__main__':
    main()
