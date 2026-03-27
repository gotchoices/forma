#!/usr/bin/env python3
"""
R28 Track 1: σ_eν and σ_νp exploration.

R27 set σ_eν = σ_νp = 0 throughout.  These cross-shears
couple the neutrino sheet to the electron and proton sheets.
Nonzero values might shift mode energies enough to improve
the pion (14% off), tau (5.6%), and strange baryons.

Strategy:
1. Sweep σ_eν and σ_νp over their allowed ranges
2. At each point, recompute self-consistent metric
3. Rerun the particle catalog from R27
4. Find the (σ_eν, σ_νp) that minimizes total error
"""

import sys
import os
import math
import numpy as np
from itertools import product

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6_solver import self_consistent_metric
from lib.t6 import (
    mode_energy, mode_charge, mode_spin,
    M_P_MEV, M_E_MEV, M_N_MEV,
)

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064

PARTICLES = [
    # (name, mass_MeV, charge, spin_halves, pinning)
    # pinning: True = used to set parameters, False = prediction
    ("e⁻",    0.511,    -1,  1,  True),
    ("p",     938.272,   +1,  1,  True),
    ("n",     939.565,    0,  1,  True),
    ("μ⁻",    105.658,   -1,  1,  True),

    ("τ⁻",   1776.86,    -1,  1,  False),
    ("π⁺",    139.570,   +1,  0,  False),
    ("π⁰",    134.977,    0,  0,  False),
    ("K⁺",    493.677,   +1,  0,  False),
    ("K⁰",    497.611,    0,  0,  False),
    ("η",     547.862,    0,  0,  False),
    ("η′",    957.78,     0,  0,  False),
    ("ρ⁰",    775.26,     0,  2,  False),
    ("ω",     782.66,     0,  2,  False),
    ("φ",    1019.461,    0,  2,  False),
    ("Λ",    1115.683,    0,  1,  False),
    ("Σ⁺",   1189.37,    +1,  1,  False),
    ("Ξ⁰",   1314.86,     0,  1,  False),
    ("Δ⁺⁺",  1232.0,     +2,  3,  False),
]


def spin_achievable(n1, n5, target_spin):
    n1_odd = abs(n1) % 2
    n5_odd = abs(n5) % 2
    base_odd = n1_odd + n5_odd

    for n3_try in [0, 1]:
        total = base_odd + n3_try
        if total == target_spin:
            return True, n3_try
        if target_spin == 0 and total == 2:
            return True, n3_try
    return False, None


def find_nearest_mode(target_mass, target_charge, target_spin,
                      Gti, L, n_max_ep=8, n_max_p=8):
    best = None
    best_err = float('inf')

    rng_e = range(-n_max_ep, n_max_ep + 1)
    rng_p = range(-n_max_p, n_max_p + 1)

    for n1 in rng_e:
        for n5 in rng_p:
            if -n1 + n5 != target_charge:
                continue
            ok, n3_parity = spin_achievable(n1, n5, target_spin)
            if not ok:
                continue
            n3 = 0 if n3_parity == 0 else 1

            for n2 in rng_e:
                for n6 in rng_p:
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
                        }
    return best


def catalog_error(Gti, L):
    """Compute total squared fractional error for non-pinning particles."""
    total_sq = 0.0
    errors = {}
    for name, mass, charge, spin, pinning in PARTICLES:
        if pinning:
            continue
        match = find_nearest_mode(mass, charge, spin, Gti, L)
        if match is None:
            errors[name] = 1.0
            total_sq += 1.0
        else:
            frac = abs(match['frac_gap'])
            errors[name] = frac
            total_sq += frac**2
    return math.sqrt(total_sq / len([p for p in PARTICLES if not p[4]])), errors


def section(num, title):
    print(f"\n{'='*70}")
    print(f"  SECTION {num}: {title}")
    print(f"{'='*70}\n")


def main():
    # ── Section 1: Baseline at σ_eν = σ_νp = 0 ───────────────────────
    section(1, "Baseline: σ_eν = σ_νp = 0")

    sc = self_consistent_metric(R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
    Gti = sc['Gtilde_inv']
    L = sc['L']

    print(f"  Parameters: r_e={R_E}, r_ν={R_NU}, r_p={R_P}")
    print(f"  σ_ep = {SIGMA_EP}, σ_eν = 0, σ_νp = 0\n")

    print(f"  {'Particle':>8s}  {'M_obs':>10s}  {'E_mode':>10s}  "
          f"{'Gap%':>8s}  {'Mode':>20s}")
    print(f"  {'-'*62}")

    for name, mass, charge, spin, pinning in PARTICLES:
        match = find_nearest_mode(mass, charge, spin, Gti, L)
        if match:
            mode_str = f"({','.join(str(x) for x in match['n'])})"
            frac = abs(match['frac_gap']) * 100
            tag = " [pin]" if pinning else ""
            print(f"  {name:>8s}  {mass:10.1f}  {match['E_MeV']:10.1f}  "
                  f"{frac:7.2f}%  {mode_str:>20s}{tag}")

    rms_base, errors_base = catalog_error(Gti, L)
    print(f"\n  RMS fractional error (predictions only): {rms_base:.4f}")

    # ── Section 2: σ_eν sweep (σ_νp = 0) ─────────────────────────────
    section(2, "σ_eν sweep (σ_νp = 0)")

    print(f"  {'σ_eν':>8s}  {'RMS':>8s}  {'τ':>8s}  {'π⁺':>8s}  "
          f"{'K⁺':>8s}  {'Λ':>8s}  {'Σ⁺':>8s}")
    print(f"  {'-'*58}")

    for sigma_enu in np.arange(-0.20, 0.21, 0.02):
        try:
            sc = self_consistent_metric(R_E, R_NU, R_P,
                                         sigma_ep=SIGMA_EP,
                                         sigma_enu=sigma_enu)
            Gti = sc['Gtilde_inv']
            L = sc['L']
            rms, errs = catalog_error(Gti, L)
            print(f"  {sigma_enu:+8.3f}  {rms:8.4f}  "
                  f"{errs.get('τ⁻', 0)*100:7.2f}%  "
                  f"{errs.get('π⁺', 0)*100:7.2f}%  "
                  f"{errs.get('K⁺', 0)*100:7.2f}%  "
                  f"{errs.get('Λ', 0)*100:7.2f}%  "
                  f"{errs.get('Σ⁺', 0)*100:7.2f}%")
        except Exception as e:
            print(f"  {sigma_enu:+8.3f}  FAILED: {e}")

    # ── Section 3: σ_νp sweep (σ_eν = 0) ─────────────────────────────
    section(3, "σ_νp sweep (σ_eν = 0)")

    print(f"  {'σ_νp':>8s}  {'RMS':>8s}  {'τ':>8s}  {'π⁺':>8s}  "
          f"{'K⁺':>8s}  {'Λ':>8s}  {'Σ⁺':>8s}")
    print(f"  {'-'*58}")

    for sigma_nup in np.arange(-0.20, 0.21, 0.02):
        try:
            sc = self_consistent_metric(R_E, R_NU, R_P,
                                         sigma_ep=SIGMA_EP,
                                         sigma_nup=sigma_nup)
            Gti = sc['Gtilde_inv']
            L = sc['L']
            rms, errs = catalog_error(Gti, L)
            print(f"  {sigma_nup:+8.3f}  {rms:8.4f}  "
                  f"{errs.get('τ⁻', 0)*100:7.2f}%  "
                  f"{errs.get('π⁺', 0)*100:7.2f}%  "
                  f"{errs.get('K⁺', 0)*100:7.2f}%  "
                  f"{errs.get('Λ', 0)*100:7.2f}%  "
                  f"{errs.get('Σ⁺', 0)*100:7.2f}%")
        except Exception as e:
            print(f"  {sigma_nup:+8.3f}  FAILED: {e}")

    # ── Section 4: 2D grid ────────────────────────────────────────────
    section(4, "2D grid: σ_eν × σ_νp")

    grid_vals = np.arange(-0.15, 0.16, 0.05)
    best_rms = rms_base
    best_pair = (0.0, 0.0)

    print(f"  {'σ_eν':>8s}  {'σ_νp':>8s}  {'RMS':>8s}  {'τ%':>7s}  "
          f"{'π⁺%':>7s}  {'K⁺%':>7s}")
    print(f"  {'-'*50}")

    for s_en, s_np in product(grid_vals, grid_vals):
        try:
            sc = self_consistent_metric(R_E, R_NU, R_P,
                                         sigma_ep=SIGMA_EP,
                                         sigma_enu=s_en,
                                         sigma_nup=s_np)
            Gti = sc['Gtilde_inv']
            L = sc['L']
            rms, errs = catalog_error(Gti, L)
            if rms < best_rms:
                best_rms = rms
                best_pair = (s_en, s_np)
            print(f"  {s_en:+8.3f}  {s_np:+8.3f}  {rms:8.4f}  "
                  f"{errs.get('τ⁻', 0)*100:6.1f}%  "
                  f"{errs.get('π⁺', 0)*100:6.1f}%  "
                  f"{errs.get('K⁺', 0)*100:6.1f}%")
        except Exception:
            pass

    print(f"\n  Best: σ_eν = {best_pair[0]:+.3f}, σ_νp = {best_pair[1]:+.3f}, "
          f"RMS = {best_rms:.4f}")
    print(f"  Baseline RMS: {rms_base:.4f}")
    improvement = (rms_base - best_rms) / rms_base * 100
    print(f"  Improvement: {improvement:.1f}%")

    # ── Section 5: Full catalog at best point ─────────────────────────
    if best_pair != (0.0, 0.0):
        section(5, f"Full catalog at best point σ_eν={best_pair[0]:+.3f}, σ_νp={best_pair[1]:+.3f}")

        sc = self_consistent_metric(R_E, R_NU, R_P,
                                     sigma_ep=SIGMA_EP,
                                     sigma_enu=best_pair[0],
                                     sigma_nup=best_pair[1])
        Gti = sc['Gtilde_inv']
        L = sc['L']

        print(f"  {'Particle':>8s}  {'M_obs':>10s}  {'E_mode':>10s}  "
              f"{'Gap%':>8s}  {'Δ from base':>12s}")
        print(f"  {'-'*52}")

        for name, mass, charge, spin, pinning in PARTICLES:
            match = find_nearest_mode(mass, charge, spin, Gti, L)
            if match:
                frac = abs(match['frac_gap']) * 100
                base_frac = errors_base.get(name, 0) * 100
                delta = frac - base_frac if not pinning else 0
                tag = " [pin]" if pinning else ""
                print(f"  {name:>8s}  {mass:10.1f}  {match['E_MeV']:10.1f}  "
                      f"{frac:7.2f}%  {delta:+11.2f}%{tag}")
    else:
        section(5, "No improvement found — baseline is optimal")
        print("  σ_eν = σ_νp = 0 remains the best point.")

    # ── Section 6: Summary ────────────────────────────────────────────
    section(6, "Summary")

    print(f"  Baseline RMS (σ_eν = σ_νp = 0): {rms_base:.4f}")
    print(f"  Best RMS:                        {best_rms:.4f}")
    print(f"  Best σ_eν = {best_pair[0]:+.3f}, σ_νp = {best_pair[1]:+.3f}")


if __name__ == '__main__':
    main()
