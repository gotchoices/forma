#!/usr/bin/env python3
"""
R28 Track 2: Mode census below 2 GeV.

Enumerate ALL Ma modes with energy below 2000 MeV at the
pinned parameter point.  For each, classify as:
  - Matched to a known particle (within threshold)
  - Ghost mode (no known counterpart)

This answers: is the Ma spectrum economical (few ghosts)
or over-predictive (many ghosts)?
"""

import sys
import os
import math
import numpy as np
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_solver import self_consistent_metric
from lib.ma import (
    mode_energy, mode_charge, mode_spin,
    M_P_MEV, M_E_MEV, M_N_MEV,
)

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064
E_MAX = 2000.0  # MeV

KNOWN_PARTICLES = [
    # (name, mass_MeV, charge, spin_halves, lifetime_category)
    # spin_halves: mode_spin count of odd tube windings
    # lifetime_category: 'stable', 'weak', 'em', 'strong'
    ("e⁻",     0.511,   -1,  1, "stable"),
    ("p",    938.272,    +1,  1, "stable"),
    ("n",    939.565,     0,  1, "weak"),
    ("μ⁻",   105.658,   -1,  1, "weak"),
    ("τ⁻",  1776.86,    -1,  1, "weak"),
    ("π⁺",   139.570,   +1,  0, "weak"),
    ("π⁰",   134.977,    0,  0, "em"),
    ("K⁺",   493.677,   +1,  0, "weak"),
    ("K⁰",   497.611,    0,  0, "weak"),
    ("η",    547.862,    0,  0, "strong"),
    ("η′",   957.78,     0,  0, "strong"),
    ("ρ⁰",   775.26,     0,  2, "strong"),
    ("ρ⁺",   775.26,    +1,  2, "strong"),
    ("ω",    782.66,     0,  2, "strong"),
    ("K*⁺",  891.67,    +1,  2, "strong"),
    ("K*⁰",  895.55,     0,  2, "strong"),
    ("φ",   1019.461,    0,  2, "strong"),
    ("Λ",   1115.683,    0,  1, "weak"),
    ("Σ⁺",  1189.37,    +1,  1, "weak"),
    ("Σ⁰",  1192.642,    0,  1, "em"),
    ("Σ⁻",  1197.449,   -1,  1, "weak"),
    ("Ξ⁰",  1314.86,     0,  1, "weak"),
    ("Ξ⁻",  1321.71,    -1,  1, "weak"),
    ("Δ⁺⁺", 1232.0,     +2,  3, "strong"),
    ("Δ⁺",  1232.0,     +1,  3, "strong"),
    ("Δ⁰",  1232.0,      0,  3, "strong"),
    ("Δ⁻",  1232.0,     -1,  3, "strong"),
    ("Σ*⁺", 1382.80,    +1,  3, "strong"),
    ("Σ*⁰", 1383.70,     0,  3, "strong"),
    ("Σ*⁻", 1387.20,    -1,  3, "strong"),
    ("Ξ*⁰", 1531.80,     0,  3, "strong"),
    ("Ξ*⁻", 1535.0,     -1,  3, "strong"),
    ("Ω⁻",  1672.45,    -1,  3, "weak"),
    ("f₀",   990.0,      0,  0, "strong"),
    ("a₀",   980.0,      0,  0, "strong"),
    ("f₂",  1275.5,      0,  0, "strong"),  # spin 2, but mode_spin=0 possible
    ("N*",  1440.0,      +1,  1, "strong"),  # N(1440) Roper resonance
    ("N*",  1520.0,      +1,  3, "strong"),  # N(1520)
    ("N*",  1535.0,      +1,  1, "strong"),  # N(1535)
    ("N*",  1675.0,      +1,  1, "strong"),  # N(1675)
    ("N*",  1680.0,      +1,  3, "strong"),  # N(1680)
]

MATCH_THRESHOLD = 0.05  # 5% to count as matched


def section(num, title):
    print(f"\n{'='*70}")
    print(f"  SECTION {num}: {title}")
    print(f"{'='*70}\n")


def main():
    sc = self_consistent_metric(R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
    Gti = sc['Gtilde_inv']
    L = sc['L']

    # ── Section 1: Enumerate all modes below E_MAX ────────────────────
    section(1, f"All Ma modes below {E_MAX:.0f} MeV")

    all_modes = []
    n_max = 10

    for n1 in range(-n_max, n_max + 1):
        for n2 in range(-n_max, n_max + 1):
            for n3 in [0, 1]:  # n3 parity only matters
                for n5 in range(-n_max, n_max + 1):
                    for n6 in range(-n_max, n_max + 1):
                        n = np.array([n1, n2, n3, 0, n5, n6], dtype=float)
                        E = mode_energy(n, Gti, L)
                        if E < E_MAX and E > 0.001:
                            charge = mode_charge(n)
                            spin = mode_spin(n)
                            all_modes.append({
                                'n': tuple(int(x) for x in n),
                                'E': E,
                                'Q': int(charge),
                                'S': int(spin),
                            })

    all_modes.sort(key=lambda m: m['E'])

    unique_modes = {}
    for m in all_modes:
        key = (round(m['E'], 1), m['Q'], m['S'])
        if key not in unique_modes:
            unique_modes[key] = m

    modes_list = sorted(unique_modes.values(), key=lambda m: m['E'])
    print(f"  Total modes found: {len(all_modes)}")
    print(f"  Unique (E, Q, S): {len(modes_list)}")

    # ── Section 2: Classify modes ─────────────────────────────────────
    section(2, "Mode classification")

    matched = []
    ghosts = []

    for mode in modes_list:
        best_match = None
        best_frac = float('inf')

        for name, mass, charge, spin, cat in KNOWN_PARTICLES:
            if charge != mode['Q']:
                continue
            if spin != mode['S']:
                continue
            frac = abs(mode['E'] - mass) / mass
            if frac < best_frac:
                best_frac = frac
                best_match = (name, mass, cat, frac)

        if best_match and best_frac < MATCH_THRESHOLD:
            matched.append({**mode, 'particle': best_match[0],
                           'p_mass': best_match[1], 'frac': best_frac,
                           'cat': best_match[2]})
        else:
            closest = best_match if best_match else None
            ghosts.append({**mode, 'closest': closest})

    print(f"  Matched to known particles: {len(matched)}")
    print(f"  Ghost modes (unmatched):    {len(ghosts)}")
    print(f"  Ratio ghosts/matched:       {len(ghosts)/max(1,len(matched)):.1f}")

    # ── Section 3: Matched modes ──────────────────────────────────────
    section(3, "Matched modes")

    print(f"  {'E (MeV)':>10s}  {'Q':>3s}  {'S':>3s}  {'Particle':>10s}  "
          f"{'P_mass':>10s}  {'Gap%':>7s}  {'Mode':>20s}")
    print(f"  {'-'*70}")

    for m in matched:
        mode_str = f"({','.join(str(x) for x in m['n'])})"
        print(f"  {m['E']:10.1f}  {m['Q']:+3d}  {m['S']:3d}  "
              f"{m['particle']:>10s}  {m['p_mass']:10.1f}  "
              f"{m['frac']*100:6.2f}%  {mode_str:>20s}")

    # ── Section 4: Ghost modes ────────────────────────────────────────
    section(4, "Ghost modes (no known counterpart within 5%)")

    print(f"  {'E (MeV)':>10s}  {'Q':>3s}  {'S':>3s}  "
          f"{'Nearest':>10s}  {'Nearest mass':>12s}  {'Gap%':>7s}  "
          f"{'Mode':>20s}")
    print(f"  {'-'*82}")

    for m in ghosts:
        mode_str = f"({','.join(str(x) for x in m['n'])})"
        if m['closest']:
            print(f"  {m['E']:10.1f}  {m['Q']:+3d}  {m['S']:3d}  "
                  f"{m['closest'][0]:>10s}  {m['closest'][1]:12.1f}  "
                  f"{m['closest'][3]*100:6.1f}%  {mode_str:>20s}")
        else:
            print(f"  {m['E']:10.1f}  {m['Q']:+3d}  {m['S']:3d}  "
                  f"{'(none)':>10s}  {'':>12s}  {'':>7s}  {mode_str:>20s}")

    # ── Section 5: Energy distribution ────────────────────────────────
    section(5, "Energy distribution of modes")

    bins = [(0, 100), (100, 200), (200, 500), (500, 1000),
            (1000, 1500), (1500, 2000)]

    print(f"  {'Range (MeV)':>16s}  {'Total':>6s}  {'Matched':>8s}  "
          f"{'Ghosts':>7s}  {'Ghost%':>7s}")
    print(f"  {'-'*50}")

    for lo, hi in bins:
        n_tot = len([m for m in modes_list if lo <= m['E'] < hi])
        n_mat = len([m for m in matched if lo <= m['E'] < hi])
        n_gho = len([m for m in ghosts if lo <= m['E'] < hi])
        pct = n_gho / max(1, n_tot) * 100
        print(f"  {lo:6d}–{hi:4d}      {n_tot:6d}  {n_mat:8d}  "
              f"{n_gho:7d}  {pct:6.0f}%")

    # ── Section 6: Charge/spin census ─────────────────────────────────
    section(6, "Modes by charge and spin")

    cs_counts = defaultdict(int)
    for m in modes_list:
        cs_counts[(m['Q'], m['S'])] += 1

    print(f"  {'(Q, S)':>8s}  {'Count':>6s}  {'Spin':>8s}")
    print(f"  {'-'*28}")
    for (q, s), count in sorted(cs_counts.items()):
        spin_label = {0: "0", 1: "1/2", 2: "1", 3: "3/2"}.get(s, str(s))
        print(f"  ({q:+d}, {s})   {count:6d}  {spin_label:>8s}")

    # ── Section 7: Summary ────────────────────────────────────────────
    section(7, "Summary")

    print(f"  Ma modes below {E_MAX:.0f} MeV: {len(modes_list)}")
    print(f"  Matched to known particles: {len(matched)}")
    print(f"  Ghost modes:                {len(ghosts)}")
    print(f"  Ghost fraction:             {len(ghosts)/len(modes_list)*100:.0f}%")
    print()
    if len(ghosts) > len(matched):
        print("  The Ma spectrum OVER-PREDICTS: more ghost modes than")
        print("  matched particles.  This is expected for a geometry that")
        print("  supports many oscillation patterns — most are off-resonance")
        print("  excitations that decay quickly or don't manifest as")
        print("  observable particles.")
    else:
        print("  The Ma spectrum is ECONOMICAL: fewer ghost modes than")
        print("  matched particles.")


if __name__ == '__main__':
    main()
