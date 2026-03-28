#!/usr/bin/env python3
"""
R38 Track 2: Neutrino mode census on Ma_ν.

Enumerates all modes on Ma_ν, focusing on |n₃| = 1 modes that
carry weak charge (per R26 F35).  Computes how many independent
weakly-charged neutrino species exist below various energy cutoffs.

Uses R26 Assignment A parameters: s₃₄ = 0.02199, ε = r = 5.0.
"""

import math
import numpy as np


S34 = 0.02199       # neutrino within-plane shear
R_NU = 5.0          # neutrino aspect ratio (ε = a/R = tube/ring)

DM2_21 = 7.53e-5    # eV², solar mass splitting
E0_SQ = DM2_21 / (4 * S34)   # eV²
E0 = math.sqrt(E0_SQ)         # energy scale in eV
E0_MEV = E0 * 1e-6


def mu_sq(n3, n4, s=S34, r=R_NU):
    """Dimensionless mass-squared for mode (n₃, n₄) on Ma_ν."""
    return (n3 / r)**2 + (n4 - n3 * s)**2


def mass_eV(n3, n4):
    """Physical mass in eV for mode (n₃, n₄)."""
    return E0 * math.sqrt(mu_sq(n3, n4))


def is_weakly_charged(n3):
    """Per R26 F35: weak charge requires |n₃| = 1 (tube winding = 1)."""
    return abs(n3) == 1


def cpt_conjugate(n3, n4):
    """CPT conjugate flips all quantum numbers."""
    return (-n3, -n4)


def main():
    print("=" * 70)
    print("R38 Track 2: Neutrino mode census on Ma_ν")
    print("=" * 70)
    print(f"\nParameters: s₃₄ = {S34}, r_ν = ε = {R_NU}")
    print(f"Energy scale: E₀ = {E0*1000:.3f} meV")

    # The three identified neutrinos (R26 Assignment A)
    nu_modes = [(1, 1), (-1, 1), (1, 2)]
    print("\nIdentified neutrinos (R26 Assignment A):")
    for n3, n4 in nu_modes:
        m = mass_eV(n3, n4) * 1000  # meV
        cn3, cn4 = cpt_conjugate(n3, n4)
        m_conj = mass_eV(cn3, cn4) * 1000
        print(f"  ({n3:+d}, {n4:+d})  m = {m:.2f} meV   "
              f"CPT: ({cn3:+d}, {cn4:+d})  m = {m_conj:.2f} meV")

    print(f"\nν₃ mass: {mass_eV(1, 2)*1000:.2f} meV")

    # Enumerate ALL |n₃| = 1 modes up to various cutoffs
    cutoffs_eV = [0.1, 0.5, 1.0, 10.0, 100.0, 1000.0]
    n4_max = 500  # generous upper bound

    print("\n" + "=" * 70)
    print("|n₃| = 1 MODES (weakly charged) — census")
    print("=" * 70)

    # Collect all |n₃| = 1 modes
    all_weak_modes = []
    for n3 in [1, -1]:
        for n4 in range(-n4_max, n4_max + 1):
            if n3 == 0 and n4 == 0:
                continue
            m = mass_eV(n3, n4)
            all_weak_modes.append((n3, n4, m))

    all_weak_modes.sort(key=lambda x: x[2])

    # Identify independent species (group particle + antiparticle)
    # CPT: (n₃, n₄) ↔ (−n₃, −n₄) — same mass, same species
    species = {}
    for n3, n4, m in all_weak_modes:
        cn3, cn4 = cpt_conjugate(n3, n4)
        key = tuple(sorted([(n3, n4), (cn3, cn4)]))
        if key not in species:
            species[key] = m

    species_list = sorted(species.items(), key=lambda x: x[1])

    print(f"\nTotal |n₃| = 1 modes below {cutoffs_eV[-1]} eV: {len(all_weak_modes)}")
    print(f"Independent species (particle ≠ antiparticle): {len(species_list)}")

    print(f"\n{'Cutoff':>12}  {'Species':>10}  {'Modes':>10}")
    print("-" * 40)
    for cutoff in cutoffs_eV:
        n_species = sum(1 for _, m in species_list if m < cutoff)
        n_modes = sum(1 for _, _, m in all_weak_modes if m < cutoff)
        print(f"{cutoff:>10.1f} eV  {n_species:>10d}  {n_modes:>10d}")

    # Show the first 30 species
    print("\n" + "=" * 70)
    print("FIRST 30 WEAKLY-CHARGED NEUTRINO SPECIES (by mass)")
    print("=" * 70)
    print(f"{'#':>4}  {'Mode':>12}  {'CPT':>12}  {'Mass (meV)':>12}  {'Note':>20}")
    print("-" * 65)

    nu_set = set(nu_modes)
    antinu_set = set(cpt_conjugate(*m) for m in nu_modes)

    for i, (key, m) in enumerate(species_list[:30]):
        (n3a, n4a), (n3b, n4b) = key
        mode_str = f"({n3a:+d},{n4a:+d})"
        cpt_str = f"({n3b:+d},{n4b:+d})"
        m_meV = m * 1000

        note = ""
        if (n3a, n4a) in nu_set or (n3b, n4b) in nu_set:
            note = "← IDENTIFIED ν"
        elif (n3a, n4a) in antinu_set or (n3b, n4b) in antinu_set:
            note = "← IDENTIFIED ν̄"

        print(f"{i+1:4d}  {mode_str:>12}  {cpt_str:>12}  {m_meV:12.2f}  {note:>20}")

    # The critical question: how many species are between ν₃ and some cutoff?
    m_nu3 = mass_eV(1, 2)  # ν₃ mass
    print(f"\nν₃ mass: {m_nu3*1000:.2f} meV")

    above_nu3 = [(k, m) for k, m in species_list if m > m_nu3 * 1.001]
    print(f"Weakly-charged species ABOVE ν₃:")

    print(f"\n{'Cutoff':>12}  {'Additional species':>20}")
    print("-" * 40)
    for cutoff in [0.1, 0.5, 1.0, 10.0, 100.0, 1000.0]:
        n_above = sum(1 for _, m in above_nu3 if m < cutoff)
        print(f"{cutoff:>10.1f} eV  {n_above:>20d}")

    # Z width comparison
    print("\n" + "=" * 70)
    print("Z WIDTH COMPARISON")
    print("=" * 70)
    m_Z_half = 45600  # m_Z/2 in MeV ≈ 45.6 GeV
    m_Z_half_eV = m_Z_half * 1e6  # in eV

    n_species_below_Z = sum(1 for _, m in species_list if m < m_Z_half_eV)
    print(f"Light neutrino species (m < m_Z/2 = {m_Z_half_eV/1e9:.1f} GeV): {n_species_below_Z}")
    print(f"Experimental value (Z width): N_ν = 2.996 ± 0.007")
    print(f"Tension: model predicts {n_species_below_Z} vs observed 3")

    # Check: is (−1, 2) truly an independent mode?
    print("\n" + "=" * 70)
    print("CRITICAL MODE: (−1, 2) — the would-be 4th neutrino")
    print("=" * 70)
    m_12 = mass_eV(1, 2)
    m_m12 = mass_eV(-1, 2)
    print(f"  ν₃ = (1, 2):   mass = {m_12*1000:.4f} meV")
    print(f"  (−1, 2):       mass = {m_m12*1000:.4f} meV")
    print(f"  Splitting:     Δm = {(m_m12 - m_12)*1000:.4f} meV")
    print(f"  |n₃| = 1:     {is_weakly_charged(-1)} → weakly charged")
    print(f"  CPT of (−1,2): (1,−2), mass = {mass_eV(1,-2)*1000:.4f} meV")
    print(f"  Is (−1,2) = CPT of any identified ν? "
          f"{'YES' if (-1,2) in antinu_set else 'NO'}")

    # How the number of species grows with n₄
    print("\n" + "=" * 70)
    print("SPECIES COUNT GROWTH")
    print("=" * 70)
    print("The number of |n₃|=1 species grows linearly with the")
    print("maximum |n₄| value, since each n₄ gives a new mode.")
    print()
    for n4_limit in [2, 5, 10, 20, 50, 100]:
        count = 0
        for n3 in [1, -1]:
            for n4 in range(-n4_limit, n4_limit + 1):
                key = tuple(sorted([(n3, n4), (-n3, -n4)]))
                if key not in species:
                    continue
                count += 1
        # Simpler: count unique species with |n₄| ≤ n4_limit
        sp = set()
        for n3 in [1, -1]:
            for n4 in range(-n4_limit, n4_limit + 1):
                key = tuple(sorted([(n3, n4), (-n3, -n4)]))
                sp.add(key)
        print(f"  |n₄| ≤ {n4_limit:3d}:  {len(sp)} independent species")


if __name__ == '__main__':
    main()
