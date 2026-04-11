"""
R56 Track 3b: Clean diameter sweep

The Track 3 optimizer was noisy because:
1. L-BFGS-B found local minima, not global
2. The ring parameterization (r, z, angles) had too many
   equivalent configurations that confused the optimizer
3. Energy differences between N and N+1 were smaller than
   the optimization error

Fix: for a RING of N couplets, the lowest-energy configuration
is KNOWN analytically — equally spaced at some radius r in the
equatorial plane.  There's no angular optimization needed.
The ONLY free parameter is the ring radius r.

So: at each (R_eff, N_ring), do a 1D sweep of r_ring and find
the minimum energy.  This is noise-free — no optimizer needed,
just a grid search on one variable.
"""

import numpy as np
import math

ALPHA = 1.0 / 137.036
HC = 197.3269804  # MeV·fm
A0 = 52917.7  # Bohr radius in fm


def V_ne(r, Z, Q, R_e):
    if r < 1.0:
        r = 1.0  # avoid singularity
    if r > R_e:
        return -Z * Q * ALPHA * HC / r
    else:
        return -Z * Q * ALPHA * HC / R_e


def V_cc(d, Q, R_e):
    if d < 1.0:
        d = 1.0
    if d > R_e:
        return Q**2 * ALPHA * HC / d
    else:
        return Q**2 * ALPHA * HC / R_e


def ring_energy_analytic(N_ring, r_ring, Z, R_e, Q=2.0):
    """
    Energy of N_ring couplets equally spaced on a ring of radius
    r_ring in the xy-plane, plus one core couplet at the origin.

    All positions are determined by N_ring and r_ring — no
    optimization needed.
    """
    E = 0.0

    # Core couplet at origin
    E += V_ne(0.5, Z, Q, R_e)  # small offset to avoid r=0

    # Core-ring interactions
    for i in range(N_ring):
        # Each ring couplet at distance r_ring from origin
        E += V_ne(r_ring, Z, Q, R_e)
        # Core-ring repulsion
        E += V_cc(r_ring, Q, R_e)

    # Ring-ring interactions
    angles = np.linspace(0, 2*math.pi, N_ring, endpoint=False)
    for i in range(N_ring):
        for j in range(i+1, N_ring):
            # Distance between two points on a ring
            da = angles[j] - angles[i]
            d = 2 * r_ring * abs(math.sin(da / 2))
            E += V_cc(d, Q, R_e)

    return E


def find_optimal_r(N_ring, Z, R_e, Q=2.0):
    """1D grid search for optimal ring radius. Noise-free."""
    # Search from just outside R_e to several times the Bohr radius
    r_min = max(R_e * 0.5, 10.0)
    r_max = A0 / Z * 3
    r_values = np.linspace(r_min, r_max, 2000)

    best_E = None
    best_r = None
    for r in r_values:
        E = ring_energy_analytic(N_ring, r, Z, R_e, Q)
        if best_E is None or E < best_E:
            best_E = E
            best_r = r

    # Refine around best
    r_lo = max(best_r - (r_max - r_min) / 2000, r_min)
    r_hi = min(best_r + (r_max - r_min) / 2000, r_max)
    for r in np.linspace(r_lo, r_hi, 1000):
        E = ring_energy_analytic(N_ring, r, Z, R_e, Q)
        if E < best_E:
            best_E = E
            best_r = r

    return best_E, best_r


def main():
    print("=" * 70)
    print("R56 Track 3b: Clean diameter sweep (analytic ring, 1D search)")
    print("=" * 70)
    print()

    Z = 10  # neon

    R_values = np.concatenate([
        np.linspace(10, 100, 10),
        np.linspace(150, 500, 8),
        np.linspace(600, 1000, 5),
        np.linspace(1500, 5000, 8),
        np.linspace(6000, 15000, 5),
    ])

    print(f"  Z = {Z}")
    print()
    print(f"  {'R_eff':>7s}  {'R/A0':>6s}  ", end='')
    for n in range(1, 8):
        print(f"{'ΔE_'+str(n):>8s} ", end='')
    print(f"  {'j4→5':>8s}  {'r4→5':>5s}")

    print(f"  {'(fm)':>7s}  {'(%)':>6s}  ", end='')
    for n in range(1, 8):
        print(f"{'(keV)':>8s} ", end='')
    print(f"  {'(keV)':>8s}  {'ratio':>5s}")

    print(f"  {'─'*7}  {'─'*6}  " + ("─"*8 + " ") * 7 +
          f"  {'─'*8}  {'─'*5}")

    # For clean incremental energy: compute E(N) - E(N-1) at each N
    # where E(N) is the TOTAL energy with N ring couplets + 1 core

    best_jump = None

    for R_eff in R_values:
        marginals = []
        prev_E = ring_energy_analytic(0, 0, Z, R_eff)  # just the core

        for N_ring in range(1, 8):
            E, r = find_optimal_r(N_ring, Z, R_eff)
            dE = (E - prev_E) * 1e3  # keV
            marginals.append(dE)
            prev_E = E

        jump = marginals[4] - marginals[3] if len(marginals) >= 5 else 0
        ratio = marginals[4] / marginals[3] if (len(marginals) >= 5
                and marginals[3] != 0) else 0

        pct = R_eff / A0 * 100

        print(f"  {R_eff:>7.0f}  {pct:>5.1f}%  ", end='')
        for dE in marginals:
            print(f"{dE:>+8.2f} ", end='')
        print(f"  {jump:>+8.2f}  {ratio:>5.2f}")

        if best_jump is None or jump > best_jump[1]:
            best_jump = (R_eff, jump, ratio, marginals)

    print()
    print(f"  Largest 4→5 jump: R_eff = {best_jump[0]:.0f} fm "
          f"({best_jump[0]/A0*100:.2f}% of Bohr radius)")
    print(f"    jump = {best_jump[1]:+.2f} keV, ratio = {best_jump[2]:.2f}")
    print(f"    marginals: {['%.2f' % m for m in best_jump[3]]}")
    print()

    # ── Key physical radii ─────────────────────────────────────
    print("  Reference radii:")
    print(f"    Classical electron radius:  {2.818:.0f} fm")
    print(f"    Reduced Compton (ℏ/mc):     {386:.0f} fm")
    print(f"    Compton wavelength:         {2426:.0f} fm")
    print(f"    Model-E L_tube/2π:          {751:.0f} fm")
    print(f"    Bohr radius:                {A0:.0f} fm")
    print()

    print("Track 3b complete.")


if __name__ == '__main__':
    main()
