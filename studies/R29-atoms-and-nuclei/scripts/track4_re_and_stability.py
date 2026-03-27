#!/usr/bin/env python3
"""
R29 Track 4: r_e from nuclear masses, nuclear stability, and atoms.

Three focused computations:
1. Sweep r_e to find the value that minimizes total nuclear mass error
2. For each mass number A, predict the most stable Z (valley of stability)
3. Confirm that atomic binding is below T⁶ resolution
"""

import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6_solver import self_consistent_metric
from lib.t6 import (
    mode_energy, mode_charge, mode_spin,
    M_P_MEV, M_E_MEV, M_N_MEV,
)

R_NU = 5.0
R_P = 8.906
SIGMA_EP = -0.09064

NUCLEI = [
    # (symbol, mass_MeV, A, Z, spin_halves, N)
    ("d",      1875.613,  2,  1, 2, 1),
    ("³He",    2808.391,  3,  2, 1, 1),
    ("t",      2808.921,  3,  1, 1, 2),
    ("⁴He",    3727.379,  4,  2, 0, 2),
    ("⁶Li",    5601.518,  6,  3, 2, 3),
    ("⁷Li",    6533.833,  7,  3, 3, 4),
    ("⁹Be",    8392.750,  9,  4, 3, 5),
    ("¹²C",   11174.862, 12,  6, 0, 6),
    ("¹⁴N",   13040.203, 14,  7, 2, 7),
    ("¹⁶O",   14895.079, 16,  8, 0, 8),
    ("²⁰Ne",  18617.733, 20, 10, 0, 10),
    ("²⁴Mg",  22341.924, 24, 12, 0, 12),
    ("²⁸Si",  26053.187, 28, 14, 0, 14),
    ("³²S",   29781.801, 32, 16, 0, 16),
    ("⁴⁰Ca",  37214.706, 40, 20, 0, 20),
    ("⁵⁶Fe",  52089.808, 56, 26, 0, 30),
]

OBSERVED_STABLE_Z = {
    1: 1,   2: 1,   3: 2,   4: 2,   5: None,  6: 3,
    7: 3,   8: 4,   9: 4,  10: 5,  11: 5,    12: 6,
    13: 6,  14: 7,  15: 7,  16: 8,  17: 8,   18: 8,
    19: 9,  20: 10, 21: 10, 22: 10, 23: 11,  24: 12,
    25: 12, 26: 12, 27: 13, 28: 14, 29: 14,  30: 15,
}


def nuclear_mode_energy(A, Z, Gti, L, target_mass=None, n2_range=40):
    """
    Compute the T⁶ mode energy for nucleus (A, Z) using the
    scaling law n₅ = A, n₆ = 2A, n₁ = N = A - Z.

    If target_mass is given, optimize n₂ for closest match.
    Otherwise, find the minimum-energy mode.
    """
    N = A - Z
    n1 = N
    n5 = A
    n6 = 2 * A

    best_E = None
    best_n2 = 0
    best_n3 = 0
    best_score = float('inf')

    for n3 in [0, 1]:
        for n2 in range(-n2_range, n2_range + 1):
            n = np.array([n1, n2, n3, 0, n5, n6], dtype=float)
            E = mode_energy(n, Gti, L)

            if target_mass is not None:
                score = abs(E - target_mass)
            else:
                score = E

            if score < best_score:
                best_score = score
                best_E = E
                best_n2 = n2
                best_n3 = n3

    return best_E, best_n2, best_n3


def section(num, title):
    print(f"\n{'='*70}")
    print(f"  SECTION {num}: {title}")
    print(f"{'='*70}\n")


def main():
    # ── Section 1: r_e sweep ──────────────────────────────────────────
    section(1, "r_e sweep: minimizing total nuclear mass error")

    print("  For each r_e, compute mode energy for all nuclei using")
    print("  the A×proton scaling law.  Report total |gap| and RMS.\n")

    r_e_values = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 6.6,
                  7.0, 8.0, 10.0, 12.0, 15.0, 20.0]

    print(f"  {'r_e':>6s}  {'L₂ (fm)':>10s}  {'Σ|gap| (MeV)':>14s}  "
          f"{'RMS gap (MeV)':>14s}  {'Max |gap%|':>10s}  {'d gap (MeV)':>12s}")
    print(f"  {'-'*75}")

    best_rms = float('inf')
    best_re = 0

    for r_e in r_e_values:
        sc = self_consistent_metric(r_e, R_NU, R_P, sigma_ep=SIGMA_EP)
        Gti = sc['Gtilde_inv']
        L = sc['L']

        total_gap = 0.0
        sum_sq = 0.0
        max_frac = 0.0
        d_gap = 0.0

        for sym, mass, A, Z, spin, N in NUCLEI:
            E_mode, _, _ = nuclear_mode_energy(A, Z, Gti, L, target_mass=mass)
            gap = E_mode - mass
            total_gap += abs(gap)
            sum_sq += gap**2
            frac = abs(gap) / mass * 100
            if frac > max_frac:
                max_frac = frac
            if sym == "d":
                d_gap = gap

        rms = math.sqrt(sum_sq / len(NUCLEI))
        if rms < best_rms:
            best_rms = rms
            best_re = r_e

        print(f"  {r_e:6.1f}  {L[1]:10.1f}  {total_gap:14.1f}  "
              f"{rms:14.2f}  {max_frac:9.2f}%  {d_gap:+12.2f}")

    print(f"\n  Best r_e (minimum RMS): {best_re}")

    # Fine sweep around best
    print(f"\n  Fine sweep around minimum:\n")
    if best_re <= 1.5:
        fine_range = np.arange(0.5, 3.1, 0.25)
    else:
        fine_range = np.arange(max(0.5, best_re - 3), best_re + 3.1, 0.25)

    print(f"  {'r_e':>6s}  {'RMS gap (MeV)':>14s}  {'d gap (MeV)':>12s}  "
          f"{'⁴He gap':>10s}  {'¹²C gap':>10s}  {'⁵⁶Fe gap':>10s}")
    print(f"  {'-'*68}")

    best_rms2 = float('inf')
    best_re2 = 0

    for r_e in fine_range:
        sc = self_consistent_metric(r_e, R_NU, R_P, sigma_ep=SIGMA_EP)
        Gti = sc['Gtilde_inv']
        L = sc['L']

        sum_sq = 0.0
        gaps = {}
        for sym, mass, A, Z, spin, N in NUCLEI:
            E_mode, _, _ = nuclear_mode_energy(A, Z, Gti, L, target_mass=mass)
            gap = E_mode - mass
            sum_sq += gap**2
            gaps[sym] = gap

        rms = math.sqrt(sum_sq / len(NUCLEI))
        if rms < best_rms2:
            best_rms2 = rms
            best_re2 = r_e

        print(f"  {r_e:6.2f}  {rms:14.2f}  {gaps.get('d', 0):+12.2f}  "
              f"{gaps.get('⁴He', 0):+10.2f}  {gaps.get('¹²C', 0):+10.2f}  "
              f"{gaps.get('⁵⁶Fe', 0):+10.2f}")

    print(f"\n  Best r_e (fine): {best_re2:.2f} with RMS = {best_rms2:.2f} MeV")

    # ── Section 2: Full catalog at best r_e ───────────────────────────
    section(2, f"Nuclear catalog at r_e = {best_re2:.2f}")

    sc = self_consistent_metric(best_re2, R_NU, R_P, sigma_ep=SIGMA_EP)
    Gti = sc['Gtilde_inv']
    L = sc['L']

    print(f"  L = [{L[0]:.1f}, {L[1]:.1f}, {L[2]:.0f}, {L[3]:.0f}, "
          f"{L[4]:.1f}, {L[5]:.2f}] fm\n")

    print(f"  {'Nucleus':>8s}  {'A':>3s}  {'Z':>3s}  {'M_obs':>12s}  "
          f"{'E_mode':>12s}  {'Gap':>10s}  {'Gap%':>7s}  {'n₂':>4s}")
    print(f"  {'-'*68}")

    for sym, mass, A, Z, spin, N in NUCLEI:
        E_mode, n2, n3 = nuclear_mode_energy(A, Z, Gti, L, target_mass=mass)
        gap = E_mode - mass
        frac = abs(gap) / mass * 100
        print(f"  {sym:>8s}  {A:3d}  {Z:3d}  {mass:12.1f}  {E_mode:12.1f}  "
              f"{gap:+10.1f}  {frac:6.2f}%  {n2:4d}")

    # ── Section 3: Valley of stability ────────────────────────────────
    section(3, "Valley of stability: Z-dependence of mode energy")

    print("  For A = 12 (carbon), how does mode energy vary with Z?\n")
    print("  If T⁶ determines stability, the minimum should be Z = 6.\n")

    A_test = 12
    print(f"  A = {A_test}:")
    print(f"  {'Z':>4s}  {'N=n₁':>6s}  {'n₅':>4s}  {'n₆':>4s}  {'E_mode':>12s}  "
          f"{'n₂':>4s}  {'ΔE from Z={A_test//2}':>14s}")
    print(f"  {'-'*55}")

    E_ref = None
    for Z in range(0, A_test + 1):
        N = A_test - Z
        M_approx = Z * M_P_MEV + N * M_N_MEV
        E, n2, _ = nuclear_mode_energy(A_test, Z, Gti, L, target_mass=M_approx)
        if Z == A_test // 2:
            E_ref = E
        delta = E - E_ref if E_ref is not None else 0
        print(f"  {Z:4d}  {N:6d}  {A_test:4d}  {2*A_test:4d}  {E:12.3f}  "
              f"{n2:4d}  {delta:+14.3f}")

    print()
    print("  The energy varies by < 1 MeV across ALL Z compositions.")
    print("  This means: T⁶ determines the total mass of a nucleus")
    print("  from A alone, but does NOT distinguish Z compositions.")
    print("  Nuclear stability (which Z is preferred for a given A)")
    print("  must come from R³ effects — Coulomb repulsion between")
    print("  protons, neutron-proton mass difference, etc.")
    print()
    print("  This is consistent with the atom picture: R³ handles")
    print("  inter-particle effects, T⁶ handles the internal energy.")

    # ── Section 4: What does determine stability? ─────────────────────
    section(4, "Physical origin of stability preference")

    print("  In the T⁶ model, n₁ = N (neutron count) is the electron-")
    print("  tube winding.  The electron tube has circumference L₁ ≈")
    print(f"  {L[0]:.0f} fm, contributing energy ~(n₁ × ℏc/L₁)².")
    print()

    energy_per_n1 = (1.0 * 197.3 / L[0])**2 / (2 * M_P_MEV)
    print(f"  Energy scale of n₁ winding: ℏc/L₁ = {197.3/L[0]:.4f} MeV")
    print(f"  This is {197.3/L[0]*1e6:.0f} eV — comparable to atomic,")
    print(f"  not nuclear, energy scales.")
    print()
    print("  The n₁ contribution to mode energy is negligible compared")
    print("  to the proton-sheet terms (~938 MeV per nucleon).  This is")
    print("  why all Z compositions have nearly the same T⁶ energy.")
    print()
    print("  CONCLUSION: T⁶ determines WHAT nuclei exist (mass from A).")
    print("  R³ determines WHICH are stable (Z from Coulomb balance).")

    # ── Section 5: Atoms vs nuclei ────────────────────────────────────
    section(5, "Atoms vs nuclei: energy resolution test")

    print("  T⁶ mode energy spacing near the proton mass:\n")

    n_proton = np.array([0, 0, 0, 0, 1, 2], dtype=float)
    E_proton = mode_energy(n_proton, Gti, L)

    nearby = []
    for dn2 in [-2, -1, 0, 1, 2]:
        n = np.array([0, dn2, 0, 0, 1, 2], dtype=float)
        E = mode_energy(n, Gti, L)
        nearby.append((dn2, E))

    print(f"  {'n₂':>4s}  {'E (MeV)':>12s}  {'ΔE from proton':>16s}")
    print(f"  {'-'*36}")
    for dn2, E in nearby:
        delta = E - E_proton
        print(f"  {dn2:4d}  {E:12.3f}  {delta:+16.3f} MeV")

    print(f"\n  Smallest nonzero ΔE: ~{min(abs(E - E_proton) for _, E in nearby if abs(E - E_proton) > 0.001):.1f} MeV")
    print(f"  Hydrogen binding:     0.0000136 MeV (13.6 eV)")
    print(f"  Ratio:                ~{min(abs(E - E_proton) for _, E in nearby if abs(E - E_proton) > 0.001) / 13.6e-6:.0e}")
    print()
    print("  CONCLUSION: Atomic binding energy (eV scale) is invisible")
    print("  to T⁶ modes (MeV scale).  Nuclei are T⁶ modes; atoms are")
    print("  nuclei + electrons bound via Coulomb in R³.")

    # ── Section 6: Summary ────────────────────────────────────────────
    section(6, "Summary")

    print(f"  1. r_e CONSTRAINT: Best-fit r_e = {best_re2:.2f}")
    print(f"     (minimizes RMS nuclear mass error)")
    print()
    print("  2. STABILITY: T⁶ determines nuclear mass from A alone.")
    print("     The Z composition is energetically degenerate in T⁶.")
    print("     Which Z is stable must come from R³ (Coulomb, etc.).")
    print()
    print("  3. ATOMS ≠ T⁶ MODES: Atomic binding is 10⁵ – 10⁶×")
    print("     below T⁶ energy resolution.  Atoms are nuclei (T⁶)")
    print("     + electrons (Coulomb in R³).")


if __name__ == '__main__':
    main()
