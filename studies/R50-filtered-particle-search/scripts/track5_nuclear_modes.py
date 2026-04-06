#!/usr/bin/env python3
"""
R50 Track 5: Nuclear modes under model-D geometry.

Tests both proton hypotheses — (1,3) fundamental and (3,6) composite —
against the R29 nuclear benchmark set (d through ⁵⁶Fe).

For each hypothesis, adapts the R29 nuclear scaling law:
  n₁ = N (neutron count)
  n₂ = optimized for mass (electron ring winding)
  n₃ = chosen for spin parity
  n₅ = A (mass number)
  n₆ = ratio × A  (proton ring winding; ratio = n₆_p/n₅_p)

The ring ratio depends on the proton mode:
  (1,3) proton → n₆/n₅ = 3 → nuclear n₆ = 3A
  (3,6) proton → n₆/n₅ = 2 → nuclear n₆ = 2A  (per-strand view)
  R29 baseline  (1,2) proton → n₆ = 2A

Charge formula check:
  Fundamental: Q = −n₁ + n₅ = −N + A = Z  ✓ (universal)
  Composite:   Q = −n₁ + n₅/gcd(n₅, n₆)  — tested for each case

Waveguide propagation is checked for each nuclear mode.
"""

import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model_d import MaD

SIGMA_EP = -0.13

# R29 benchmark nuclei:
# (symbol, A, Z, mass_MeV, spin_halves, R29_gap_pct)
NUCLEI = [
    ("d",     2,   1,   1875.613,  2,  0.02),
    ("³He",   3,   2,   2808.391,  1,  0.21),
    ("t",     3,   1,   2808.921,  1,  None),
    ("⁴He",   4,   2,   3727.379,  0,  0.67),
    ("⁶Li",   6,   3,   5601.518,  2,  0.49),
    ("⁷Li",   7,   3,   6533.833,  3,  0.51),
    ("⁹Be",   9,   4,   8392.750,  3,  0.61),
    ("¹²C",  12,   6,  11174.862,  0,  0.75),
    ("¹⁴N",  14,   7,  13040.203,  2,  0.73),
    ("¹⁶O",  16,   8,  14895.079,  0,  0.78),
    ("⁵⁶Fe", 56,  26,  52089.808,  0,  0.87),
]


def build_nuclear_mode(A, Z, spin_halves, ring_ratio, n2_range=20):
    """
    Construct nuclear mode quantum numbers using R29 scaling law,
    optimizing n₂ (electron ring winding) for energy.

    Returns list of candidate modes (n₁, n₂, n₃, n₄, n₅, n₆) with
    different n₂ values.
    """
    N = A - Z
    n1 = N
    n5 = A
    n6 = ring_ratio * A

    n1_odd = abs(n1) % 2
    n5_odd = abs(n5) % 2
    base_odd = n1_odd + n5_odd

    candidates = []
    for n3 in [0, 1]:
        total_odd = base_odd + n3
        spin_ok = False
        if spin_halves == 0 and total_odd % 2 == 0:
            spin_ok = True
        elif total_odd == spin_halves:
            spin_ok = True
        elif spin_halves == 0 and total_odd == 2:
            spin_ok = True

        if not spin_ok:
            continue

        for n2 in range(-n2_range, n2_range + 1):
            candidates.append((n1, n2, n3, 0, n5, n6))

    return candidates


def find_best_mode(model, target_mass, candidates):
    """Find the candidate mode closest to target_mass."""
    best = None
    best_err = float('inf')

    for n in candidates:
        E = model.energy(n)
        err = abs(E - target_mass)
        if err < best_err:
            best_err = err
            best = n
            best_E = E

    if best is None:
        return None

    gap = best_E - target_mass
    return {
        'n': best,
        'E_MeV': best_E,
        'gap_MeV': gap,
        'gap_pct': abs(gap / target_mass) * 100,
        'Q_fund': model.charge(best),
        'Q_comp': model.charge_composite(best),
        'spin_h': model.spin_halves(best),
        'spin_total': model.spin_total(best),
        'propagates': model.propagates(best),
    }


def section(title):
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def run_hypothesis(label, model, ring_ratio):
    """Run nuclear mode search for one proton hypothesis."""
    section(f"{label}  (ring ratio = {ring_ratio}, σ_ep = {SIGMA_EP})")

    proton_mode = model.proton_mode
    print(f"  Proton mode: {proton_mode}")
    print(f"  L_ring_p = {model.L_ring[2]:.6e} fm")

    proton_n = (0, 0, 0, 0, proton_mode[0], proton_mode[1])
    E_p = model.energy(proton_n)
    print(f"  Proton energy: {E_p:.3f} MeV (obs: 938.272 MeV)")
    print()

    header = (f"  {'Nucleus':>6s}  {'A':>3s}  {'Z':>3s}  "
              f"{'Mode':>24s}  {'E_mode':>10s}  {'M_obs':>10s}  "
              f"{'Gap%':>7s}  {'Q_f':>4s}  {'Q_c':>4s}  "
              f"{'Spin':>5s}  {'Prop':>5s}  {'R29%':>6s}")
    print(header)
    print(f"  {'-' * (len(header) - 2)}")

    results = []
    for sym, A, Z, mass, spin_h, r29_gap in NUCLEI:
        candidates = build_nuclear_mode(A, Z, spin_h, ring_ratio)
        match = find_best_mode(model, mass, candidates)

        if match is None:
            print(f"  {sym:>6s}  {A:3d}  {Z:3d}  {'(no match)':>24s}")
            results.append((sym, A, Z, mass, spin_h, r29_gap, None))
            continue

        n = match['n']
        mode_str = f"({n[0]},{n[1]},{n[2]},{n[3]},{n[4]},{n[5]})"
        r29_str = f"{r29_gap:.2f}" if r29_gap is not None else "  —"
        prop_str = "yes" if match['propagates'] else "NO"
        charge_ok = "✓" if match['Q_fund'] == Z else "✗"

        print(f"  {sym:>6s}  {A:3d}  {Z:3d}  "
              f"{mode_str:>24s}  {match['E_MeV']:10.1f}  {mass:10.1f}  "
              f"{match['gap_pct']:6.2f}%  "
              f"{match['Q_fund']:+3d}{charge_ok}  {match['Q_comp']:+3d}   "
              f"{match['spin_total']:4.1f}  {prop_str:>5s}  {r29_str:>6s}")
        results.append((sym, A, Z, mass, spin_h, r29_gap, match))

    return results


def compare_results(results_13, results_36):
    """Print side-by-side comparison."""
    section("COMPARISON: (1,3) vs (3,6) vs R29")

    print(f"  {'Nucleus':>6s}  {'A':>3s}  {'R29%':>6s}  "
          f"{'(1,3)%':>7s}  {'(3,6)%':>7s}  {'Winner':>8s}  "
          f"{'(1,3) prop':>10s}  {'(3,6) prop':>10s}  "
          f"{'Q_f=Z?':>7s}")
    print(f"  {'-' * 85}")

    for r13, r36 in zip(results_13, results_36):
        sym = r13[0]
        A = r13[1]
        Z = r13[2]
        r29_gap = r13[5]
        m13 = r13[6]
        m36 = r36[6]

        r29_str = f"{r29_gap:.2f}" if r29_gap is not None else "  —"

        if m13 is None or m36 is None:
            print(f"  {sym:>6s}  {A:3d}  {r29_str:>6s}  (missing match)")
            continue

        g13 = m13['gap_pct']
        g36 = m36['gap_pct']

        if g13 < g36:
            winner = "(1,3)"
        elif g36 < g13:
            winner = "(3,6)"
        else:
            winner = "tie"

        p13 = "yes" if m13['propagates'] else "NO"
        p36 = "yes" if m36['propagates'] else "NO"
        q_ok = "✓" if m13['Q_fund'] == Z else "✗"

        print(f"  {sym:>6s}  {A:3d}  {r29_str:>6s}  "
              f"{g13:6.2f}%  {g36:6.2f}%  {winner:>8s}  "
              f"{p13:>10s}  {p36:>10s}  "
              f"{q_ok:>7s}")


def charge_formula_analysis(results_13, results_36):
    """Demonstrate the charge formula problem for (3,6)."""
    section("CHARGE FORMULA ANALYSIS")

    print("  Under the (1,3) hypothesis, the fundamental charge formula")
    print("  Q = −n₁ + n₅ gives correct nuclear charge for ALL nuclei.")
    print("  The composite formula also gives Q = −n₁ + n₅ (since gcd = 1")
    print("  for odd n₅ with n₆ = 3·n₅ at A odd, etc.).\n")

    print("  Under the (3,6) hypothesis (per-strand scaling n₅=A, n₆=2A):\n")

    print(f"  {'Nucleus':>6s}  {'n₅':>4s}  {'n₆':>4s}  {'gcd':>4s}  "
          f"{'Q_fund':>7s}  {'Q_comp':>7s}  {'Q_obs':>6s}  {'Fund OK?':>9s}  {'Comp OK?':>9s}")
    print(f"  {'-' * 70}")

    for r36 in results_36:
        sym, A, Z, mass, spin_h, r29_gap, m36 = r36
        if m36 is None:
            continue
        n = m36['n']
        n5, n6 = n[4], n[5]
        g = math.gcd(abs(n5), abs(n6)) if n5 and n6 else max(abs(n5), abs(n6))
        Q_fund = m36['Q_fund']
        Q_comp = m36['Q_comp']
        f_ok = "✓" if Q_fund == Z else "✗"
        c_ok = "✓" if Q_comp == Z else "✗"
        print(f"  {sym:>6s}  {n5:4d}  {n6:4d}  {g:4d}  "
              f"{Q_fund:+6d}   {Q_comp:+6d}   {Z:+5d}  "
              f"{'  ' + f_ok:>9s}  {'  ' + c_ok:>9s}")


def binding_energy_analysis(results, label, model):
    """Analyze binding energy captured by Ma modes."""
    section(f"BINDING ENERGY — {label}")

    M_P = 938.272
    M_N = 939.565

    print(f"  {'Nucleus':>6s}  {'Z·m_p+N·m_n':>12s}  {'M_obs':>10s}  "
          f"{'E_mode':>10s}  {'BE_obs':>8s}  {'BE_mode':>8s}  "
          f"{'Captured':>8s}")
    print(f"  {'-' * 75}")

    for sym, A, Z, mass, spin_h, r29_gap, match in results:
        if match is None or A < 2:
            continue
        N = A - Z
        free_sum = Z * M_P + N * M_N
        BE_obs = free_sum - mass
        BE_mode = free_sum - match['E_MeV']
        captured = BE_mode / BE_obs * 100 if BE_obs > 0 else 0

        print(f"  {sym:>6s}  {free_sum:12.1f}  {mass:10.1f}  "
              f"{match['E_MeV']:10.1f}  {BE_obs:8.1f}  {BE_mode:8.1f}  "
              f"{captured:7.1f}%")


def summary_statistics(results, label):
    """Print summary stats for one hypothesis."""
    gaps = [r[6]['gap_pct'] for r in results if r[6] is not None]
    props = [r[6]['propagates'] for r in results if r[6] is not None]
    charges_ok = [r[6]['Q_fund'] == r[2] for r in results if r[6] is not None]

    n = len(gaps)
    avg_gap = sum(gaps) / n if n else 0
    max_gap = max(gaps) if gaps else 0
    n_prop = sum(props)
    n_charge = sum(charges_ok)
    n_sub1 = sum(1 for g in gaps if g < 1.0)

    print(f"\n  {label}:")
    print(f"    Nuclei matched:        {n}/{len(results)}")
    print(f"    All charges correct:   {n_charge}/{n}")
    print(f"    All propagate:         {n_prop}/{n}")
    print(f"    Within 1%:             {n_sub1}/{n}")
    print(f"    Average gap:           {avg_gap:.3f}%")
    print(f"    Worst gap:             {max_gap:.3f}%")


def sigma_sweep(model_13_0, ring_ratio=3):
    """Show how cross-shear systematically shifts nuclear gaps."""
    section("CROSS-SHEAR SENSITIVITY (1,3) proton")

    print("  Nuclear gaps are dominated by proton-sheet energy, which")
    print("  shifts uniformly with σ_ep.  At σ_ep = 0, the proton mass")
    print("  is exact (by calibration), and nuclear gaps match R29.\n")

    benchmarks = [
        ("p",    1, 1, 938.272),
        ("d",    2, 1, 1875.613),
        ("⁴He",  4, 2, 3727.379),
        ("¹²C", 12, 6, 11174.862),
        ("⁵⁶Fe",56,26, 52089.808),
    ]

    header = f"  {'σ_ep':>8s}"
    for sym, *_ in benchmarks:
        header += f"  {sym:>8s}"
    print(header)
    print(f"  {'-' * (10 + 10 * len(benchmarks))}")

    for sep in [0.0, -0.05, -0.10, -0.13, -0.15]:
        m = MaD.from_physics(n_p=(1, 3), sigma_ep=sep)
        row = f"  {sep:+8.2f}"
        for sym, A, Z, mass in benchmarks:
            N = A - Z
            n = (N, 0, 0, 0, A, ring_ratio * A)
            E = m.energy(n)
            gap = abs(E - mass) / mass * 100
            row += f"  {gap:7.2f}%"
        print(row)


def energy_identity_test():
    """Show that (1,3) and (3,6) give identical nuclear energies
    when quantum numbers are scaled proportionally."""
    section("ENERGY IDENTITY: (1,3) vs (3,6) direct scaling")

    print("  When nuclear quantum numbers scale with the proton mode")
    print("  ((1,3)→n₆=3A; (3,6)→n₆=6A,n₅=3A), the energies are")
    print("  IDENTICAL.  Only the charge formula differs.\n")

    m13 = MaD.from_physics(n_p=(1, 3), sigma_ep=0.0)
    m36 = MaD.from_physics(n_p=(3, 6), sigma_ep=0.0)

    nuclei = [
        ("p",    1, 1,   938.272),
        ("d",    2, 1,  1875.613),
        ("⁴He",  4, 2,  3727.379),
        ("¹²C", 12, 6, 11174.862),
        ("⁵⁶Fe",56,26, 52089.808),
    ]

    print(f"  {'Nuc':>5s}  {'(1,3) mode':>20s}  {'E_13':>10s}  "
          f"{'(3,6) mode':>20s}  {'E_36':>10s}  {'ΔE':>8s}  "
          f"{'Q₁₃':>4s}  {'Q₃₆f':>5s}  {'Q₃₆c':>5s}  {'Z':>3s}")
    print(f"  {'-' * 100}")

    for sym, A, Z, mass in nuclei:
        N = A - Z
        n13 = (N, 0, 0, 0, A, 3 * A)
        n36 = (N, 0, 0, 0, 3 * A, 6 * A)
        E13 = m13.energy(n13)
        E36 = m36.energy(n36)
        dE = abs(E13 - E36)
        Q13 = m13.charge(n13)
        Q36f = m36.charge(n36)
        Q36c = m36.charge_composite(n36)

        n13_str = f"({N},0,0,0,{A},{3*A})"
        n36_str = f"({N},0,0,0,{3*A},{6*A})"
        print(f"  {sym:>5s}  {n13_str:>20s}  {E13:10.1f}  "
              f"{n36_str:>20s}  {E36:10.1f}  {dE:8.3f}  "
              f"{Q13:+3d}{'✓' if Q13==Z else '✗'}  "
              f"{Q36f:+4d}{'✗' if Q36f!=Z else '✓'}  "
              f"{Q36c:+4d}{'✗' if Q36c!=Z else '✓'}  {Z:+3d}")


def main():
    print("R50 Track 5: Nuclear modes under model-D")
    print(f"σ_ep = {SIGMA_EP}")
    print()

    model_13 = MaD.from_physics(n_p=(1, 3), sigma_ep=SIGMA_EP)
    model_36 = MaD.from_physics(n_p=(3, 6), sigma_ep=SIGMA_EP)

    results_13 = run_hypothesis(
        "(1,3) PROTON — nuclear scaling: n₅ = A, n₆ = 3A",
        model_13, ring_ratio=3)

    results_36 = run_hypothesis(
        "(3,6) PROTON — nuclear scaling: n₅ = A, n₆ = 2A (per-strand)",
        model_36, ring_ratio=2)

    compare_results(results_13, results_36)
    charge_formula_analysis(results_13, results_36)
    energy_identity_test()
    sigma_sweep(model_13)
    binding_energy_analysis(results_13, "(1,3) proton", model_13)

    section("SUMMARY")
    summary_statistics(results_13, "(1,3) proton [n₆ = 3A]")
    summary_statistics(results_36, "(3,6) proton [n₆ = 2A, per-strand]")


if __name__ == '__main__':
    main()
