#!/usr/bin/env python3
"""
R20 Track 5: Three-mode neutrino packet from neutron decay.

QUESTION
========
If the neutrino is ejected harmonic energy (1.531 m_e) from
neutron decay, still trapped on T², it decomposes into eigenmodes.
Can three such modes reproduce the observed neutrino oscillation
parameter ratio |Δm²₃₂|/Δm²₂₁ ≈ 33?

The absolute mass scale is wrong (modes are ~keV, neutrinos are
~eV), but the ratio is dimensionless and could match independently.

APPROACH
========
1. Build catalog of all uncharged modes on the electron's T²
   with E < 2 m_e (since three modes must sum to ~1.531 m_e).
2. Enumerate all triplets summing to 1.531 ± tolerance.
3. For each triplet, compute the Δm² ratio.
4. Report near-matches to the target ratio ≈ 33.
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq
from itertools import combinations_with_replacement

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, alpha, m_e, lambda_C

m_p = 1.67262192369e-27
m_n = 1.67492749804e-27
mass_ratio_pe = m_p / m_e
mass_ratio_ne = m_n / m_e

m_e_eV = m_e * c**2 / 1.602176634e-19

DM2_21 = 7.53e-5   # eV², solar
DM2_32 = 2.453e-3  # eV², atmospheric (absolute value)
TARGET_RATIO = abs(DM2_32 / DM2_21)  # ≈ 32.6

NEUTRON_EXCESS = mass_ratio_ne - mass_ratio_pe - 1.0  # 1.531 m_e


def alpha_mode_2d(r, s, m):
    q = m - s
    sn = math.sin(2 * math.pi * s)
    if abs(sn) < 1e-15 or abs(q) < 1e-15:
        return 0.0
    d = math.sqrt(r**2 * (1 + m * s)**2 + m**2)
    return r**2 * sn**2 / (4 * math.pi * q**2 * d)


def solve_electron_s(r):
    def f(s):
        return alpha_mode_2d(r, s, 2) - alpha
    ss = np.linspace(0.001, 0.499, 5000)
    fs = [f(s) for s in ss]
    for i in range(len(fs) - 1):
        if fs[i] * fs[i + 1] < 0:
            return brentq(f, ss[i], ss[i + 1], xtol=1e-14)
    return None


def energy_ratio(n1, n2, r, s):
    """E(n1,n2)/E(1,2) in momentum picture."""
    def k_sq(a, b):
        return (a / 1.0)**2 + ((b - a * s) / r)**2
    k_e = k_sq(1, 2)
    k_m = k_sq(n1, n2)
    if k_e == 0:
        return float('inf')
    return math.sqrt(k_m / k_e)


def spin_of_mode(n1, n2):
    if n2 == 0:
        return None
    return abs(n1 / n2)


def main():
    r = 1.0
    s = solve_electron_s(r)
    print(f"Electron geometry: r = {r}, s₁₂ = {s:.10f}")
    print(f"Neutron excess energy: {NEUTRON_EXCESS:.4f} m_e "
          f"= {NEUTRON_EXCESS * m_e_eV / 1e6:.4f} MeV")
    print(f"Target Δm² ratio: |Δm²₃₂|/Δm²₂₁ = {TARGET_RATIO:.1f}")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 1: Uncharged mode catalog (E < 1.6 m_e)")
    print("=" * 72)
    print()

    max_E = NEUTRON_EXCESS + 0.05
    modes = []
    for n1 in range(-10, 11):
        for n2 in range(-20, 21):
            if n1 == 0 and n2 == 0:
                continue
            if abs(n1) == 1:
                continue
            E = energy_ratio(n1, n2, r, s)
            if E < max_E:
                sp = spin_of_mode(n1, n2)
                sp_str = f"{sp:.2f}" if sp is not None else "undef"
                modes.append((n1, n2, E, sp))

    modes.sort(key=lambda x: x[2])

    # Deduplicate: (n1,n2) and (-n1,-n2) have the same energy
    seen = set()
    unique_modes = []
    for n1, n2, E, sp in modes:
        key = tuple(sorted([(n1, n2), (-n1, -n2)]))
        if key not in seen:
            seen.add(key)
            unique_modes.append((n1, n2, E, sp))

    print(f"{'Mode':>12s}  {'E/m_e':>10s}  {'E (keV)':>10s}  {'Spin':>8s}")
    print("-" * 50)
    for n1, n2, E, sp in unique_modes:
        sp_str = f"{sp:.3f}" if sp is not None else "undef"
        print(f"({n1:+3d},{n2:+3d})  {E:10.6f}  {E * m_e_eV / 1e3:10.3f}  {sp_str:>8s}")

    print(f"\nTotal unique uncharged modes with E < {max_E:.2f} m_e: "
          f"{len(unique_modes)}")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 2: Triplet search")
    print("=" * 72)
    print()

    target = NEUTRON_EXCESS
    tol = 0.02  # tolerance in m_e

    print(f"Target sum: {target:.4f} m_e (tolerance ±{tol} m_e)")
    print(f"Searching triplets from {len(unique_modes)} uncharged modes...")
    print()

    energies = [E for _, _, E, _ in unique_modes]
    triplets = []

    for i in range(len(unique_modes)):
        for j in range(i, len(unique_modes)):
            E_ij = unique_modes[i][2] + unique_modes[j][2]
            if E_ij > target + tol:
                continue
            for k in range(j, len(unique_modes)):
                E_total = E_ij + unique_modes[k][2]
                if abs(E_total - target) < tol:
                    triplets.append((i, j, k, E_total))

    print(f"Found {len(triplets)} triplets within tolerance.")
    print()

    if not triplets:
        print("No triplets found. Expanding tolerance...")
        tol = 0.05
        for i in range(len(unique_modes)):
            for j in range(i, len(unique_modes)):
                E_ij = unique_modes[i][2] + unique_modes[j][2]
                if E_ij > target + tol:
                    continue
                for k in range(j, len(unique_modes)):
                    E_total = E_ij + unique_modes[k][2]
                    if abs(E_total - target) < tol:
                        triplets.append((i, j, k, E_total))
        print(f"Found {len(triplets)} triplets with tolerance ±{tol} m_e.")
        print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 3: Δm² ratio analysis")
    print("=" * 72)
    print()

    results = []
    for i, j, k, E_total in triplets:
        m1, m2, m3 = (unique_modes[i][2], unique_modes[j][2],
                       unique_modes[k][2])
        masses = sorted([m1, m2, m3])
        dm2_21 = masses[1]**2 - masses[0]**2
        dm2_32 = masses[2]**2 - masses[1]**2

        if abs(dm2_21) < 1e-15:
            ratio = float('inf')
        else:
            ratio = dm2_32 / dm2_21

        modes_str = (f"({unique_modes[i][0]:+d},{unique_modes[i][1]:+d}) + "
                     f"({unique_modes[j][0]:+d},{unique_modes[j][1]:+d}) + "
                     f"({unique_modes[k][0]:+d},{unique_modes[k][1]:+d})")

        spins = [unique_modes[x][3] for x in [i, j, k]]
        results.append((ratio, E_total, masses, modes_str, spins))

    results.sort(key=lambda x: abs(x[0] - TARGET_RATIO))

    print(f"Target ratio: {TARGET_RATIO:.1f}")
    print()

    if results:
        print("Top 20 closest matches to target ratio:")
        print(f"{'Ratio':>8s}  {'Δ':>8s}  {'E_tot/m_e':>10s}  "
              f"{'m₁':>8s}  {'m₂':>8s}  {'m₃':>8s}  Modes")
        print("-" * 100)
        for ratio, E_total, masses, modes_str, spins in results[:20]:
            delta = ratio - TARGET_RATIO
            print(f"{ratio:8.2f}  {delta:+8.2f}  {E_total:10.4f}  "
                  f"{masses[0]:8.4f}  {masses[1]:8.4f}  {masses[2]:8.4f}  "
                  f"{modes_str}")
        print()

        # Highlight exact or near matches
        close_matches = [(r, e, m, ms, sp) for r, e, m, ms, sp in results
                         if abs(r - TARGET_RATIO) < 2.0]
        if close_matches:
            print(f"Matches within ±2 of target ({TARGET_RATIO:.1f}):")
            print("-" * 100)
            for ratio, E_total, masses, modes_str, spins in close_matches:
                dm2_21 = masses[1]**2 - masses[0]**2
                dm2_32 = masses[2]**2 - masses[1]**2
                print(f"  Ratio = {ratio:.4f}")
                print(f"  Modes: {modes_str}")
                print(f"  Masses: {masses[0]:.6f}, {masses[1]:.6f}, "
                      f"{masses[2]:.6f} m_e")
                print(f"  Δm²₂₁ = {dm2_21:.6f} m_e²  "
                      f"({dm2_21 * m_e_eV**2:.2f} eV²)")
                print(f"  Δm²₃₂ = {dm2_32:.6f} m_e²  "
                      f"({dm2_32 * m_e_eV**2:.2f} eV²)")
                sp_strs = []
                for sp in spins:
                    sp_strs.append(f"{sp:.2f}" if sp is not None else "undef")
                print(f"  Spins: {', '.join(sp_strs)}")
                print()
        else:
            print(f"No triplets within ±2 of target ratio {TARGET_RATIO:.1f}.")
            print()
            print("Distribution of ratios:")
            ratios = [r for r, _, _, _, _ in results]
            bins = [0, 1, 5, 10, 20, 30, 35, 40, 50, 100, 1000]
            for lo, hi in zip(bins[:-1], bins[1:]):
                count = sum(1 for r in ratios if lo <= r < hi)
                if count > 0:
                    print(f"  [{lo:5d}, {hi:5d}): {count:4d} triplets")
            over = sum(1 for r in ratios if r >= 1000)
            if over:
                print(f"  [1000,  inf): {over:4d} triplets")
            neg = sum(1 for r in ratios if r < 0)
            if neg:
                print(f"  negative:     {neg:4d} triplets")
    else:
        print("No triplets to analyze.")

    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 4: Doublet analysis (two modes + kinetic energy)")
    print("=" * 72)
    print()
    print("Alternative: the neutrino is TWO modes on T², with the")
    print("remaining energy as kinetic energy of the electron.")
    print("This gives a two-component oscillation model.")
    print()

    doublets = []
    for i in range(len(unique_modes)):
        for j in range(i, len(unique_modes)):
            E_total = unique_modes[i][2] + unique_modes[j][2]
            if E_total < target + tol and E_total > 0.3:
                doublets.append((i, j, E_total))

    print(f"Found {len(doublets)} doublets with E < {target + tol:.2f} m_e.")
    print()

    doublet_results = []
    for i, j, E_total in doublets:
        m1 = min(unique_modes[i][2], unique_modes[j][2])
        m2 = max(unique_modes[i][2], unique_modes[j][2])
        dm2 = m2**2 - m1**2
        modes_str = (f"({unique_modes[i][0]:+d},{unique_modes[i][1]:+d}) + "
                     f"({unique_modes[j][0]:+d},{unique_modes[j][1]:+d})")
        doublet_results.append((dm2, m1, m2, modes_str, E_total))

    doublet_results.sort(key=lambda x: x[0])

    print("Smallest Δm² doublets (most degenerate pairs):")
    print(f"{'Δm²/m_e²':>12s}  {'Δm² (eV²)':>12s}  {'m₁':>8s}  {'m₂':>8s}  "
          f"{'E_tot':>8s}  Modes")
    print("-" * 90)
    for dm2, m1, m2, modes_str, E_total in doublet_results[:15]:
        print(f"{dm2:12.8f}  {dm2 * m_e_eV**2:12.2f}  {m1:8.4f}  {m2:8.4f}  "
              f"{E_total:8.4f}  {modes_str}")
    print()

    # ==================================================================
    print("=" * 72)
    print("SECTION 5: Summary")
    print("=" * 72)
    print()

    print("F19. Three-mode neutrino packet: Δm² ratio test")
    if results:
        best = results[0]
        print(f"     Best ratio match: {best[0]:.2f} "
              f"(target: {TARGET_RATIO:.1f}, Δ = {best[0] - TARGET_RATIO:+.2f})")
        print(f"     Modes: {best[3]}")
        close_count = sum(1 for r, _, _, _, _ in results
                          if abs(r - TARGET_RATIO) < 5)
        print(f"     Triplets within ±5 of target: {close_count}")
    else:
        print("     No triplets found.")
    print()

    print("F20. Mass scale problem persists")
    print("     Individual mode masses: 0.48–1.0 m_e = 245–511 keV")
    print("     Neutrino mass: < 0.8 eV")
    print("     Scale gap: ~10⁶")
    print("     A ratio match would be numerologically interesting but")
    print("     does not resolve the mass problem.")
    print()

    print("F21. Physical interpretation")
    print("     If the neutrino IS ejected harmonic energy on T²:")
    print("     - It carries ~1.5 m_e of rest mass (not < 0.8 eV)")
    print("     - Flavor oscillation would come from mode interference")
    print("     - The 'mass' measured at beta decay endpoints would be")
    print("       the invariant mass of the packet, not a single mode")
    print("     This picture is inconsistent with observed neutrino mass.")
    print("     The neutrino likely requires a mechanism beyond KK modes")
    print("     on the electron's T².")


if __name__ == "__main__":
    main()
