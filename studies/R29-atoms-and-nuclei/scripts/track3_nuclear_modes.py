#!/usr/bin/env python3
"""
R29 Track 3: Light nuclei as T⁶ modes.

The neutron was predicted as a single T⁶ mode, not derived from a
proton-electron binding force.  This track applies the same approach
to nuclei: can stable nuclei be found as modes of the T⁶ compact space?

For each target nucleus, we search the full quantum number space
for the T⁶ mode with matching charge and spin closest in energy.

Targets include all stable light nuclei up to ¹⁶O, plus a few
heavier benchmarks.
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

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064

# ── Nuclear targets ──────────────────────────────────────────────
# (symbol, name, mass_MeV, charge, spin_halves, binding_per_nucleon_MeV)
# spin_halves: 0=spin-0, 1=spin-½, 2=spin-1, 3=spin-3/2, etc.
#              matched against mode_spin (count of odd tube windings)
# mass is the ATOMIC mass minus electron masses

NUCLEI = [
    # Single nucleons (reference)
    ("p",      "proton",         938.272,    +1,  1,   0.0),
    ("n",      "neutron",        939.565,     0,  1,   0.0),

    # A = 2
    ("d",      "deuteron",      1875.613,    +1,  2,   1.112),

    # A = 3
    ("³He",    "helion",        2808.391,    +2,  1,   2.573),
    ("t",      "triton",        2808.921,    +1,  1,   2.827),

    # A = 4
    ("⁴He",    "alpha",         3727.379,    +2,  0,   7.074),

    # A = 6
    ("⁶Li",    "lithium-6",     5601.518,    +3,  2,   5.332),

    # A = 7
    ("⁷Li",    "lithium-7",     6533.833,    +3,  3,   5.606),

    # A = 9
    ("⁹Be",    "beryllium-9",   8392.750,    +4,  3,   6.463),

    # A = 12
    ("¹²C",    "carbon-12",    11174.862,    +6,  0,   7.680),

    # A = 14
    ("¹⁴N",    "nitrogen-14",  13040.203,    +7,  2,   7.476),

    # A = 16
    ("¹⁶O",    "oxygen-16",    14895.079,    +8,  0,   7.976),

    # Heavy benchmarks
    ("⁵⁶Fe",   "iron-56",      52089.808,   +26, 0,   8.790),
    ("²³⁸U",   "uranium-238",  221695.8,    +92, 0,   7.570),
]


def find_nearest_mode(target_mass, target_charge, target_spin,
                      Gti, L, n_max=12):
    """
    Find the T⁶ mode closest to target_mass with matching charge and spin.

    Charge = -n₁ + n₅ (must match exactly).
    Spin = count of odd tube windings among n₁, n₃, n₅ (must match).

    Searches n₁, n₂, n₅, n₆ up to ±n_max.
    n₃ parity chosen to match spin.  n₄ = 0.
    """
    best = None
    best_err = float('inf')

    for n1 in range(-n_max, n_max + 1):
        for n5 in range(-n_max, n_max + 1):
            if -n1 + n5 != target_charge:
                continue

            n1_odd = abs(n1) % 2
            n5_odd = abs(n5) % 2
            base_odd = n1_odd + n5_odd

            candidates_n3 = []
            for n3_try in [0, 1]:
                total_odd = base_odd + n3_try
                if total_odd == target_spin:
                    candidates_n3.append(n3_try)
                elif target_spin == 0 and total_odd == 2:
                    candidates_n3.append(n3_try)

            if not candidates_n3:
                continue

            for n2 in range(-n_max, n_max + 1):
                for n6 in range(-n_max, n_max + 1):
                    for n3 in candidates_n3:
                        n = np.array([n1, n2, n3, 0, n5, n6], dtype=float)
                        E = mode_energy(n, Gti, L)
                        err = abs(E - target_mass)
                        if err < best_err:
                            best_err = err
                            best = {
                                'n': tuple(int(x) for x in n),
                                'E_MeV': E,
                                'gap_MeV': target_mass - E,
                                'frac_gap': (target_mass - E) / target_mass,
                                'spin_count': mode_spin(n),
                                'charge': mode_charge(n),
                            }

    return best


def section(num, title):
    print(f"\n{'='*70}")
    print(f"  SECTION {num}: {title}")
    print(f"{'='*70}\n")


def main():
    sc = self_consistent_metric(R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
    Gti = sc['Gtilde_inv']
    L = sc['L']

    # ── Section 1: Energy ladder reference ────────────────────────────
    section(1, "Proton-scale energy ladder")

    print("  The T⁶ energy spectrum is dominated by proton-sheet")
    print("  quantum numbers (n₅, n₆).  Key energy levels:\n")

    ref_modes = [
        ((0, 0, 0, 0, 0, 1), "ring-1"),
        ((0, 0, 0, 0, 1, 0), "tube-1"),
        ((0, 0, 0, 0, 0, 2), "ring-2"),
        ((0, 0, 0, 0, 1, 1), "tube-1,ring-1"),
        ((0, 0, 0, 0, 1, 2), "proton"),
        ((0, 0, 0, 0, 0, 3), "ring-3"),
        ((0, 0, 0, 0, 2, 0), "tube-2"),
        ((0, 0, 0, 0, 0, 4), "ring-4"),
        ((0, 0, 0, 0, 2, 2), "tube-2,ring-2"),
        ((0, 0, 0, 0, 1, 4), "tube-1,ring-4"),
        ((0, 0, 0, 0, 2, 4), "tube-2,ring-4"),
        ((0, 0, 0, 0, 3, 6), "tube-3,ring-6"),
        ((0, 0, 0, 0, 4, 8), "tube-4,ring-8"),
    ]

    print(f"  {'Mode':>20s}  {'(n₅,n₆)':>8s}  {'E (MeV)':>12s}")
    print(f"  {'-'*45}")
    for n_tuple, label in ref_modes:
        n = np.array(n_tuple, dtype=float)
        E = mode_energy(n, Gti, L)
        print(f"  {label:>20s}  ({int(n[4])},{int(n[5])}):  {E:12.1f}")

    # ── Section 2: Nuclear mode search ────────────────────────────────
    section(2, "Nuclear mode search")

    print(f"  {'Nucleus':>8s}  {'Mass (MeV)':>12s}  {'Q':>3s}  {'S':>3s}  "
          f"{'Mode':>20s}  {'E_mode (MeV)':>14s}  {'Gap (MeV)':>12s}  "
          f"{'Gap %':>8s}")
    print(f"  {'-'*95}")

    results = []
    for sym, name, mass, charge, spin, bpn in NUCLEI:
        if mass > 15000:
            n_max = 20
        elif mass > 5000:
            n_max = 16
        else:
            n_max = 12

        match = find_nearest_mode(mass, charge, spin, Gti, L, n_max=n_max)
        if match:
            gap = match['gap_MeV']
            frac = abs(match['frac_gap']) * 100
            mode_str = f"({','.join(str(x) for x in match['n'])})"
            print(f"  {sym:>8s}  {mass:12.1f}  {charge:+3d}  {spin:3d}  "
                  f"{mode_str:>20s}  {match['E_MeV']:14.1f}  "
                  f"{gap:+12.1f}  {frac:7.2f}%")
            results.append((sym, name, mass, charge, spin, match))
        else:
            print(f"  {sym:>8s}  {mass:12.1f}  {charge:+3d}  {spin:3d}  "
                  f"{'(no match)':>20s}")
            results.append((sym, name, mass, charge, spin, None))

    # ── Section 3: Binding energy analysis ────────────────────────────
    section(3, "Binding energy from T⁶ modes")

    print("  If a nucleus IS a T⁶ mode, its mass should be LESS than")
    print("  the sum of constituent nucleon masses.  The deficit is the")
    print("  binding energy.\n")

    print("  Does the mode energy fall between the free-nucleon sum")
    print("  and the observed nuclear mass?\n")

    print(f"  {'Nucleus':>8s}  {'Z×m_p + N×m_n':>14s}  {'M_obs':>12s}  "
          f"{'E_mode':>12s}  {'Mode − obs':>12s}  {'Mode < sum?':>12s}")
    print(f"  {'-'*80}")

    for sym, name, mass, charge, spin, bpn in NUCLEI:
        if sym in ('p', 'n'):
            continue
        match = None
        for s, n2, m, c, sp, mtch in results:
            if s == sym:
                match = mtch
                break
        if match is None:
            continue

        Z = charge
        A_approx = round(mass / 938)
        N = A_approx - Z
        free_sum = Z * M_P_MEV + N * M_N_MEV

        E_mode = match['E_MeV']
        diff = E_mode - mass

        below_sum = "YES" if E_mode < free_sum else "no"

        print(f"  {sym:>8s}  {free_sum:14.1f}  {mass:12.1f}  "
              f"{E_mode:12.1f}  {diff:+12.1f}  {below_sum:>12s}")

    # ── Section 4: Mode structure analysis ────────────────────────────
    section(4, "Mode structure of matched nuclei")

    print("  Examining whether nuclear modes show systematic patterns.\n")

    print(f"  {'Nucleus':>8s}  {'A':>3s}  {'Z':>3s}  "
          f"{'n₁':>4s}  {'n₂':>4s}  {'n₃':>4s}  {'n₄':>4s}  "
          f"{'n₅':>4s}  {'n₆':>4s}  {'n₅/Z':>6s}  {'n₆/(2Z)':>8s}")
    print(f"  {'-'*70}")

    for sym, name, mass, charge, spin, match in results:
        if match is None:
            continue
        n = match['n']
        Z = charge
        A_approx = max(1, round(mass / 938))

        n5_ratio = n[4] / Z if Z != 0 else 0
        n6_ratio = n[5] / (2 * Z) if Z != 0 else 0

        print(f"  {sym:>8s}  {A_approx:3d}  {Z:3d}  "
              f"{n[0]:4d}  {n[1]:4d}  {n[2]:4d}  {n[3]:4d}  "
              f"{n[4]:4d}  {n[5]:4d}  {n5_ratio:6.2f}  {n6_ratio:8.2f}")

    # ── Section 5: Can nuclei be distinguished from single particles? ─
    section(5, "Nuclear masses vs proton-scale ladder")

    print("  Nuclear masses in units of the proton mass:\n")

    print(f"  {'Nucleus':>8s}  {'M/m_p':>8s}  {'Nearest int':>12s}  "
          f"{'Deficit %':>10s}")
    print(f"  {'-'*45}")

    for sym, name, mass, charge, spin, bpn in NUCLEI:
        ratio = mass / M_P_MEV
        nearest = round(ratio)
        deficit = (nearest - ratio) / ratio * 100
        print(f"  {sym:>8s}  {ratio:8.3f}  {nearest:12d}  {deficit:+10.3f}%")

    # ── Section 6: Summary ────────────────────────────────────────────
    section(6, "Summary")

    total = len([r for r in results if r[5] is not None])
    close = len([r for r in results if r[5] is not None
                 and abs(r[5]['frac_gap']) < 0.02])
    print(f"  Modes found: {total}/{len(NUCLEI)}")
    print(f"  Within 2%:   {close}/{len(NUCLEI)}")


if __name__ == '__main__':
    main()
