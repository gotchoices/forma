#!/usr/bin/env python3
"""
R38 Track 1: Charged lepton census above the tau.

Enumerates all DISTINCT charge −1, spin ½ energy levels on Ma from
0 to 45 GeV at the R27 pinned parameter point (r_p = 8.906,
σ_ep = −0.0906).

Key insight: for charge −1 (n₅ = n₁ − 1), spin ½ requires n₃ even.
The neutrino dimensions (n₃, n₄) add negligible energy (~meV vs MeV),
so the distinct energy levels are set by (n₁, n₂, n₆) alone.
We fix n₃ = n₄ = 0 and note the neutrino degeneracy separately.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from lib.ma_solver import self_consistent_metric
from lib.ma import mode_energy

R_E = 6.6
R_NU = 5.0
R_P = 8.906
SIGMA_EP = -0.0906

E_MAX = 45000.0  # 45 GeV in MeV
N_MAX = 15


def main():
    print("=" * 70)
    print("R38 Track 1: Charged lepton energy levels (Q = -1, spin = ½)")
    print("=" * 70)

    result = self_consistent_metric(
        r_e=R_E, r_nu=R_NU, r_p=R_P, sigma_ep=SIGMA_EP)

    if not result['converged']:
        print("FAILED: metric did not converge")
        return

    Gti = result['Gtilde_inv']
    L = result['L']

    print(f"\nParameter point: r_p = {R_P}, σ_ep = {SIGMA_EP}")
    print(f"Circumferences (fm):")
    labels = ['L₁(e-tube)', 'L₂(e-ring)', 'L₃(ν-tube)', 'L₄(ν-ring)',
              'L₅(p-tube)', 'L₆(p-ring)']
    for lbl, val in zip(labels, L):
        print(f"  {lbl:15s} = {val:.4e} fm")
    print(f"\nSearch: |n₁|,|n₂|,|n₆| ≤ {N_MAX}, n₃=n₄=0, n₅=n₁−1")
    print(f"Neutrino dims frozen (add ~meV, negligible at MeV scale)")

    twopi_hbarc = 2 * math.pi * 197.3269804
    Linv = 1.0 / L

    levels = []  # (energy, n1, n2, n5, n6)

    for n1 in range(-N_MAX, N_MAX + 1):
        n5 = n1 - 1
        if abs(n5) > N_MAX:
            continue

        for n2 in range(-N_MAX, N_MAX + 1):
            for n6 in range(-N_MAX, N_MAX + 1):
                n = (n1, n2, 0, 0, n5, n6)
                if all(ni == 0 for ni in n):
                    continue
                nt = np.array([n1*Linv[0], n2*Linv[1], 0, 0,
                               n5*Linv[4], n6*Linv[5]])
                E2 = twopi_hbarc**2 * (nt @ Gti @ nt)
                if E2 > E_MAX**2:
                    continue
                E = math.sqrt(max(E2, 0.0))
                levels.append((E, n1, n2, n5, n6))

    levels.sort(key=lambda x: x[0])

    # Collapse near-degenerate levels (within 0.01 MeV)
    distinct = []
    for E, n1, n2, n5, n6 in levels:
        merged = False
        for d in distinct:
            if abs(E - d[0]) < 0.01:
                d[2] += 1  # increment degeneracy
                merged = True
                break
        if not merged:
            distinct.append([E, (n1, n2, n5, n6), 1])

    print(f"\nTotal modes: {len(levels)}")
    print(f"Distinct energy levels: {len(distinct)}")

    # Known particles
    known = [
        ('e⁻', 0.511),
        ('μ⁻', 105.658),
        ('τ⁻', 1776.86),
    ]

    print(f"\n{'#':>4}  {'E (MeV)':>12}  {'n₁':>4} {'n₂':>4} {'n₅':>4} {'n₆':>4}"
          f"  {'Degen':>6}  {'Nearest':>6}  {'Gap (MeV)':>10}  {'Gap%':>8}")
    print("-" * 85)

    for i, (E, ns, deg) in enumerate(distinct[:80]):
        n1, n2, n5, n6 = ns
        nearest_name = ''
        nearest_gap = float('inf')
        for name, mass in known:
            gap = E - mass
            if abs(gap) < abs(nearest_gap):
                nearest_name = name
                nearest_gap = gap

        gap_pct = nearest_gap / known[0][1] * 100 if nearest_name == 'e⁻' else \
                  nearest_gap / dict(known)[nearest_name] * 100

        print(f"{i+1:4d}  {E:12.3f}  {n1:4d} {n2:4d} {n5:4d} {n6:4d}"
              f"  {deg:6d}  {nearest_name:>6}  {nearest_gap:+10.1f}  {gap_pct:+7.1f}%")

    # Energy band summary
    print("\n" + "=" * 70)
    print("ENERGY BAND SUMMARY (distinct levels)")
    print("=" * 70)
    bands = [
        (0, 0.511, "Below electron"),
        (0.511, 106, "Electron to muon"),
        (106, 938, "Muon to proton mass"),
        (938, 1877, "Proton to tau candidate"),
        (1877, 3000, "Above tau candidate"),
        (3000, 10000, "3–10 GeV"),
        (10000, 45000, "10–45 GeV"),
    ]
    for lo, hi, label in bands:
        count = sum(1 for E, _, _ in distinct if lo <= E < hi)
        print(f"  {label:30s}  ({lo:.0f}–{hi:.0f} MeV):  {count:6d} levels")

    # Focus on charged leptons: where are the first few?
    # The electron is at 0.511. The muon at 105.7. The tau at 1877.
    # What comes next?
    print("\n" + "=" * 70)
    print("CHARGED LEPTON CANDIDATES (modes near known masses)")
    print("=" * 70)

    for name, mass in known:
        nearby = [(E, ns, deg) for E, ns, deg in distinct
                  if abs(E - mass) / mass < 0.10]
        print(f"\n  {name} region (±10% of {mass:.1f} MeV):")
        if not nearby:
            print(f"    No modes within 10%")
        for E, ns, deg in nearby[:5]:
            n1, n2, n5, n6 = ns
            gap_pct = (E - mass) / mass * 100
            print(f"    E = {E:.3f} MeV  ({n1},{n2},0,0,{n5},{n6})  "
                  f"gap = {gap_pct:+.2f}%  degen = {deg}")

    # Above the tau: what's the next rung?
    print(f"\n  Above tau (> 1877 MeV), first 10 levels:")
    above_tau = [(E, ns, deg) for E, ns, deg in distinct if E > 1877]
    for i, (E, ns, deg) in enumerate(above_tau[:10]):
        n1, n2, n5, n6 = ns
        print(f"    E = {E:.1f} MeV  ({n1},{n2},0,0,{n5},{n6})  degen = {deg}")

    # The proton-scale energy ladder
    print("\n" + "=" * 70)
    print("PROTON-SCALE ENERGY LADDER (n₁=1, n₂ small, n₅=0)")
    print("=" * 70)
    print("Modes with n₁=1, n₅=0, varying n₆ (pure proton-tube rungs):")
    for n6 in range(-8, 9):
        for n2 in [2]:  # electron (1,2) winding
            n = (1, n2, 0, 0, 0, n6)
            E = mode_energy(n, Gti, L)
            if E < E_MAX:
                print(f"  (1, {n2}, 0, 0, 0, {n6:+d}):  E = {E:.1f} MeV")

    # Count: how many charge -1, spin 1/2 energy levels below 45 GeV?
    print("\n" + "=" * 70)
    print(f"FINAL COUNT: {len(distinct)} distinct charge −1, spin ½ energy levels "
          f"below 45 GeV")
    print("=" * 70)
    print("(Each level has additional degeneracy from neutrino spectator")
    print("quantum numbers, but all at effectively the same energy.)")


if __name__ == '__main__':
    main()
