#!/usr/bin/env python3
"""
R27 Track 5: Systematic particle catalog.

For every well-measured particle, find the nearest Ma mode with
matching charge and spin at the pinned parameter point
(r_p = 8.906, σ_ep = −0.09064).  Record:
  - Nearest mode quantum numbers
  - Mode energy (parameter-free prediction)
  - Gap = observed mass − mode energy
  - Fractional gap
  - Measured lifetime

This catalog feeds Track 6 (lifetime-gap correlation) and
Track 7 (reaction energetics).

All results are parameter-free: r_p and σ_ep are already
determined by the neutron and muon.
"""

import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_solver import self_consistent_metric
from lib.ma import (
    mode_energy, mode_charge, mode_spin,
    M_P_MEV, M_E_MEV, M_N_MEV,
)

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064


# ── Particle catalog ──────────────────────────────────────────────
# (name, full_name, mass_MeV, charge, spin_halves, lifetime_s)
# spin_halves: 0 = spin-0, 1 = spin-½, 2 = spin-0 or 1, 3 = spin-½ or 3/2
# (matches mode_spin() return convention)

PARTICLES = [
    # Stable (reference particles — gap should be ~0)
    ("e⁻",    "electron",          0.51100,  -1,  1,  float('inf')),
    ("p",     "proton",          938.272,    +1,  1,  float('inf')),
    ("n",     "neutron",         939.565,     0,  1,  878.4),

    # Charged leptons
    ("μ⁻",    "muon",            105.658,    -1,  1,  2.197e-6),
    ("τ⁻",    "tau",            1776.86,     -1,  1,  2.903e-13),

    # Pseudoscalar mesons (spin 0 → mode_spin = 0 or 2)
    ("π⁺",    "pion (charged)",  139.570,    +1,  0,  2.603e-8),
    ("π⁰",    "pion (neutral)",  134.977,     0,  0,  8.52e-17),
    ("K⁺",    "kaon (charged)",  493.677,    +1,  0,  1.238e-8),
    ("K⁰",    "kaon (neutral)",  497.611,     0,  0,  None),
    ("η",     "eta meson",       547.862,     0,  0,  5.02e-19),
    ("η′",    "eta prime",       957.78,      0,  0,  3.32e-21),

    # Vector mesons (spin 1 → mode_spin = 2)
    ("ρ⁰",    "rho meson",       775.26,      0,  2,  4.5e-24),
    ("ω",     "omega meson",     782.66,      0,  2,  7.75e-23),
    ("φ",     "phi meson",      1019.461,     0,  2,  1.55e-22),

    # Baryons (spin ½ → mode_spin = 1 or 3)
    ("Λ",     "lambda baryon",  1115.683,     0,  1,  2.632e-10),
    ("Σ⁺",    "sigma plus",    1189.37,     +1,  1,  8.018e-11),
    ("Ξ⁰",    "xi zero",       1314.86,      0,  1,  2.90e-10),

    # Baryons (spin 3/2 → mode_spin = 3)
    ("Δ⁺⁺",   "delta baryon",   1232.0,     +2,  3,  5.63e-24),
    ("Ω⁻",    "omega baryon",   1672.45,    -1,  3,  8.21e-11),
]


def spin_achievable(n1, n5, target_spin):
    """
    Can we choose n3 (neutrino tube) to achieve the target mode_spin?

    mode_spin counts odd tube windings across indices 0, 2, 4.
    n3 is index 2; its parity is what we control (energy cost is negligible).

    Returns (True, best_n3) or (False, None).
    """
    n1_odd = abs(n1) % 2
    n5_odd = abs(n5) % 2
    base_odd = n1_odd + n5_odd   # 0, 1, or 2

    # With n3 even: total = base_odd
    # With n3 odd:  total = base_odd + 1
    for n3_try in [0, 1]:   # 0 = even contribution, 1 = odd contribution
        total = base_odd + n3_try
        if total == target_spin:
            n3_val = n3_try  # 0 stays 0, 1 is any odd n3
            return True, (0 if n3_try == 0 else 1)
        # Spin 0 can also come from 2 odd windings (paired)
        if target_spin == 0 and total == 2:
            return True, (0 if n3_try == 0 else 1)
        # Spin 1 can come from 2+1=3 (→ spin ½ or 3/2)
        # Actually mode_spin returns the raw count; the caller filters
    return False, None


def find_nearest_mode(target_mass, target_charge, target_spin,
                      Gti, L, n_max_ep=8, n_max_p=8):
    """
    Find the nearest Ma mode matching charge and spin.

    Strategy: sweep n1, n2 (electron), n5, n6 (proton) and pick
    n3 parity to match spin.  n4 = 0 (negligible energy).
    n3's energy contribution is negligible, so the best n3 is
    whichever parity satisfies spin.
    """
    best = None
    best_err = float('inf')

    rng_e = range(-n_max_ep, n_max_ep + 1)
    rng_p = range(-n_max_p, n_max_p + 1)

    for n1 in rng_e:
        for n5 in rng_p:
            charge = -n1 + n5
            if charge != target_charge:
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
                            'frac_gap': (target_mass - E) / target_mass if target_mass > 0 else 0,
                            'spin_count': mode_spin(n),
                            'charge': mode_charge(n),
                        }

    return best


def fmt_lifetime(lt):
    if lt is None:
        return "—"
    if lt == float('inf'):
        return "stable"
    if lt >= 1:
        return f"{lt:.0f} s"
    if lt >= 1e-3:
        return f"{lt*1e3:.1f} ms"
    if lt >= 1e-6:
        return f"{lt*1e6:.2f} μs"
    if lt >= 1e-9:
        return f"{lt*1e9:.1f} ns"
    if lt >= 1e-12:
        return f"{lt*1e12:.2f} ps"
    if lt >= 1e-15:
        return f"{lt*1e15:.1f} fs"
    if lt >= 1e-18:
        return f"{lt*1e18:.1f} as"
    return f"{lt:.1e} s"


def section(n, title):
    print(f"\n{'='*70}")
    print(f"  SECTION {n}: {title}")
    print(f"{'='*70}\n")


def main():
    sc = self_consistent_metric(R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
    assert sc['converged'], "Metric did not converge"
    Gti = sc['Gtilde_inv']
    L = sc['L']

    print(f"  Circumferences L (fm):  {['%.4e' % x for x in L]}")
    print(f"  r_p = {R_P}, r_e = {R_E}, r_nu = {R_NU}")
    print(f"  σ_ep = {SIGMA_EP}")

    # ── Section 1: Full catalog ───────────────────────────────────────
    section(1, "Systematic particle catalog")

    results = []

    hdr = (f"  {'Sym':>6s}  {'Name':>18s}  {'Obs MeV':>10s}  "
           f"{'Mode':>28s}  {'Mode MeV':>10s}  {'Gap MeV':>10s}  "
           f"{'Gap%':>8s}  {'τ':>12s}")
    print(hdr)
    print(f"  {'-'*(len(hdr)+4)}")

    for sym, name, mass, charge, spin_h, lifetime in PARTICLES:
        result = find_nearest_mode(mass, charge, spin_h, Gti, L)

        if result is None:
            print(f"  {sym:>6s}  {name:>18s}  {mass:10.3f}  {'— no match —':>28s}")
            results.append({
                'sym': sym, 'name': name, 'mass': mass,
                'charge': charge, 'spin_halves': spin_h,
                'lifetime': lifetime, 'match': None,
            })
            continue

        n = result['n']
        n_str = f"({n[0]:+d},{n[1]:+d},{n[2]:+d},{n[3]:+d},{n[4]:+d},{n[5]:+d})"
        gap_pct = result['frac_gap'] * 100

        print(f"  {sym:>6s}  {name:>18s}  {mass:10.3f}  {n_str:>28s}  "
              f"{result['E_MeV']:10.3f}  {result['gap_MeV']:+10.3f}  "
              f"{gap_pct:+7.2f}%  {fmt_lifetime(lifetime):>12s}")

        results.append({
            'sym': sym, 'name': name, 'mass': mass,
            'charge': charge, 'spin_halves': spin_h,
            'lifetime': lifetime, 'match': result,
        })

    # ── Section 2: Lifetime vs gap (unstable only) ────────────────────
    section(2, "Lifetime-gap data (unstable particles)")

    pairs = []
    for r in results:
        if r['match'] is None:
            continue
        lt = r['lifetime']
        if lt is None or lt == float('inf'):
            continue
        gap = abs(r['match']['gap_MeV'])
        fgap = abs(r['match']['frac_gap'])
        pairs.append((r['sym'], r['name'], r['mass'], gap, fgap, lt))

    pairs.sort(key=lambda x: x[3])

    print(f"  {'Sym':>6s}  {'Name':>18s}  {'Mass':>10s}  {'|Gap|':>10s}  "
          f"{'|Gap%|':>8s}  {'τ':>12s}  {'log₁₀(τ/s)':>12s}")
    print(f"  {'-'*90}")

    for sym, name, mass, gap, fgap, lt in pairs:
        log_lt = math.log10(lt)
        print(f"  {sym:>6s}  {name:>18s}  {mass:10.1f}  {gap:10.3f}  "
              f"{fgap*100:7.2f}%  {lt:12.2e}  {log_lt:+12.1f}")

    # ── Section 3: Correlation test ───────────────────────────────────
    section(3, "Correlation: log|gap| vs log(lifetime)")

    if len(pairs) >= 3:
        log_gaps = np.array([math.log10(max(p[3], 0.001)) for p in pairs])
        log_lts = np.array([math.log10(p[5]) for p in pairs])

        corr = np.corrcoef(log_gaps, log_lts)[0, 1]
        print(f"  N = {len(pairs)} particles")
        print(f"  Pearson r(log|gap|, log τ) = {corr:+.4f}")
        print()
        if corr < -0.3:
            print("  → NEGATIVE correlation: larger gap ↔ shorter lifetime.")
            print("    Supports the off-resonance hypothesis.")
        elif corr > 0.3:
            print("  → POSITIVE correlation: larger gap ↔ longer lifetime.")
            print("    Contradicts simple off-resonance picture.")
        else:
            print("  → WEAK or no correlation.")
            print("    Off-resonance picture may need refinement.")

        print()
        slope, intercept = np.polyfit(log_gaps, log_lts, 1)
        print(f"  Best-fit line: log(τ) = {slope:+.2f} × log|gap| + ({intercept:+.2f})")

    # ── Section 4: Reaction energy balance ────────────────────────────
    section(4, "Reaction energy balance (mode energies)")

    mode_e = {}
    for r in results:
        if r['match'] is not None:
            mode_e[r['sym']] = r['match']['E_MeV']
    mode_e['ν'] = 0.0

    reactions = [
        ("n → p + e⁻ + ν̄",       ['n'], ['p', 'e⁻', 'ν'],   "beta decay"),
        ("π⁺ → μ⁺ + ν",          ['π⁺'], ['μ⁻', 'ν'],       "pion decay"),
        ("K⁺ → μ⁺ + ν",          ['K⁺'], ['μ⁻', 'ν'],       "kaon decay"),
        ("K⁺ → π⁺ + π⁰",        ['K⁺'], ['π⁺', 'π⁰'],     "kaon → 2π"),
        ("τ⁻ → μ⁻ + ν + ν̄",     ['τ⁻'], ['μ⁻', 'ν', 'ν'], "tau → muon"),
        ("Λ → p + π⁻",           ['Λ'],  ['p', 'π⁺'],       "lambda decay"),
    ]

    print(f"  {'Reaction':>22s}  {'ΣE_in':>10s}  {'ΣE_out':>10s}  "
          f"{'ΔE':>10s}  Note")
    print(f"  {'-'*72}")

    for label, ins, outs, note in reactions:
        E_in = sum(mode_e.get(p, None) or 0 for p in ins)
        E_out = sum(mode_e.get(p, None) or 0 for p in outs)
        all_found = all(p in mode_e for p in ins + outs)
        if all_found and E_in > 0:
            delta = E_in - E_out
            print(f"  {label:>22s}  {E_in:10.3f}  {E_out:10.3f}  "
                  f"{delta:+10.3f}  {note}")
        else:
            missing = [p for p in ins + outs if p not in mode_e]
            print(f"  {label:>22s}  {'—':>10s}  {'—':>10s}  "
                  f"{'—':>10s}  missing: {missing}")

    # ── Section 5: Summary ────────────────────────────────────────────
    section(5, "Summary statistics")

    n_total = len(results)
    n_found = sum(1 for r in results if r['match'] is not None)
    n_exact = sum(1 for r in results
                  if r['match'] and abs(r['match']['frac_gap']) < 0.001)
    n_close = sum(1 for r in results
                  if r['match'] and 0.001 <= abs(r['match']['frac_gap']) < 0.05)
    n_rough = sum(1 for r in results
                  if r['match'] and 0.05 <= abs(r['match']['frac_gap']) < 0.15)
    n_poor = sum(1 for r in results
                 if r['match'] and abs(r['match']['frac_gap']) >= 0.15)

    print(f"  Particles searched:   {n_total}")
    print(f"  Modes found:          {n_found}")
    print(f"  Exact (<0.1%):        {n_exact}")
    print(f"  Close (0.1%–5%):      {n_close}")
    print(f"  Rough (5%–15%):       {n_rough}")
    print(f"  Poor (>15%):          {n_poor}")

    print()
    print("  All energies computed at pinned point (r_p=8.906, σ_ep=−0.0906).")
    print("  No free parameters were tuned to fit any particle besides e, p, n, μ.")


if __name__ == '__main__':
    main()
