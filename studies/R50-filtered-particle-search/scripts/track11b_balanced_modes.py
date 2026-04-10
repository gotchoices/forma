"""
R50 Track 11b: Balanced harmonic modes for the muon

Search for Q = -1, spin ½ modes where the tube:ring ratio
on each active sheet is a clean harmonic (1:2, 1:3, 2:3, etc.)
rather than the extreme (1, 506) found in Track 11.

The idea: if the electron is (1,2) and the proton is (1,3),
the muon should be an equally elegant mode — perhaps a higher
harmonic of one of these patterns, with p-sheet compensation
to keep Q = -1.
"""

import sys
import os
import math
from itertools import product as iproduct

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from lib.ma_model_d import MaD


def main():
    print("=" * 78)
    print("R50 Track 11b: Balanced harmonic modes for the muon")
    print("=" * 78)
    print()

    m = MaD.from_physics()
    target = 105.658

    # ── Strategy ────────────────────────────────────────────────────
    # For Q = -n₁ + n₅ = -1:
    #   n₁ = 1, n₅ = 0: pure e-sheet (forces unbalanced n₂)
    #   n₁ = 3, n₅ = 2: e+p compound, 3:n₂ on e-sheet
    #   n₁ = 5, n₅ = 4: e+p compound, 5:n₂ on e-sheet
    #   n₁ = 7, n₅ = 6: etc.
    #   n₁ = 2, n₅ = 1: e+p, even e-tube → spin from p only
    #
    # For spin ½: need odd count of odd tube windings
    #   n₁ odd, n₅ even → ½ from e alone
    #   n₁ even, n₅ odd → ½ from p alone
    #   n₁ odd, n₅ odd, n₃ odd → 3/2 or ½ (count = 3 → ½ if we take min)
    #
    # Balanced ratios to try on each sheet:
    #   1:2, 1:3, 1:4, 2:3, 2:5, 3:4, 3:5, 3:7
    # ────────────────────────────────────────────────────────────────

    e_ratios = [(1,2), (1,3), (1,4), (1,5), (2,3), (2,5), (3,4),
                (3,5), (3,7), (5,7), (3,8), (5,8), (4,7), (5,12),
                (7,12)]
    p_ratios = [(0,0), (1,2), (1,3), (1,4), (2,3), (2,5), (3,5),
                (2,6), (3,6), (4,6), (1,6), (2,4), (3,4), (3,7),
                (3,9), (4,9), (5,9), (4,12), (5,12)]

    # Also allow sign variations
    signs_e = [+1, -1]
    signs_p = [+1, -1]

    results = []

    for (nt_e, nr_e) in e_ratios:
        for (nt_p, nr_p) in p_ratios:
            for se in signs_e:
                for sp in signs_p:
                    n1 = se * nt_e
                    n2 = se * nr_e  # keep ratio, flip sign together
                    n5 = sp * nt_p
                    n6 = sp * nr_p
                    # Also try ring sign independent
                    for n2s in [se * nr_e, -se * nr_e]:
                        for n6s in [sp * nr_p, -sp * nr_p]:
                            n = (n1, n2s, 0, 0, n5, n6s)
                            Q = MaD.charge(n)
                            if Q != -1:
                                continue
                            spin = MaD.spin_total(n)
                            if spin != 0.5:
                                continue
                            try:
                                E = m.energy(n)
                            except ValueError:
                                continue
                            delta = abs(E - target)
                            rel = delta / target
                            # Also try scaling the WHOLE mode by small integers
                            # (i.e. (k*n₁, k*n₂, 0, 0, k*n₅, k*n₆))
                            # NO — that changes Q by factor k
                            results.append({
                                'n': n, 'E': E, 'delta': delta,
                                'rel': rel, 'Q': Q, 'spin': spin,
                                'e_ratio': f"{abs(n1)}:{abs(n2s)}",
                                'p_ratio': f"{abs(n5)}:{abs(n6s)}" if nt_p > 0 else "—",
                            })

    # Also try: scale the e-sheet pattern while keeping Q = -1
    # by adjusting p-sheet to compensate
    # e.g., electron pattern ×k: (k, 2k), p-sheet: (k-1, n₆)
    # Q = -k + (k-1) = -1  ✓
    # spin: k odd → ½ from e; k-1 even → 0 from p. Total ½.
    #       k even → 0 from e; k-1 odd → ½ from p. Total ½.
    print("Scaled electron-pattern modes: (k, 2k, 0, 0, k-1, n₆)")
    print("with Q = -k + (k-1) = -1, spin ½")
    print()
    print(f"  {'k':>3s}  {'n₆':>4s}  {'mode':>30s}  {'E (MeV)':>10s}  "
          f"{'Δm/m':>8s}  {'e-ratio':>8s}  {'p-ratio':>8s}  {'prop':>5s}")
    print(f"  {'─'*3}  {'─'*4}  {'─'*30}  {'─'*10}  {'─'*8}  "
          f"{'─'*8}  {'─'*8}  {'─'*5}")

    scaled_results = []
    for k in range(1, 30):
        n1 = k
        n2_base = 2 * k  # electron 1:2 pattern
        n5 = k - 1
        for n6 in range(-30, 31):
            for n2_sign in [+1, -1]:
                n = (n1, n2_sign * n2_base, 0, 0, n5, n6)
                if MaD.charge(n) != -1:
                    continue
                if MaD.spin_total(n) != 0.5:
                    continue
                try:
                    E = m.energy(n)
                except ValueError:
                    continue
                delta = abs(E - target)
                rel = delta / target
                prop = m.propagates(n)
                scaled_results.append({
                    'k': k, 'n6': n6, 'n': n, 'E': E,
                    'delta': delta, 'rel': rel, 'prop': prop,
                })

    # Sort by proximity to muon
    scaled_results.sort(key=lambda x: x['delta'])
    for r in scaled_results[:25]:
        n = r['n']
        propmark = '✓' if r['prop'] else '✗'
        print(f"  {r['k']:>3d}  {r['n6']:>4d}  {str(n):>30s}  "
              f"{r['E']:>10.3f}  {r['rel']*100:>7.3f}%  "
              f"{abs(n[0])}:{abs(n[1]):>5d}  "
              f"{abs(n[4])}:{abs(n[5]):>5d}  {propmark:>5s}")
    print()

    # ── Also try proton 1:3 pattern scaled ──────────────────────────
    print("Scaled proton-pattern modes: (k, 3k, 0, 0, k-1, n₆)")
    print()
    print(f"  {'k':>3s}  {'n₆':>4s}  {'mode':>30s}  {'E (MeV)':>10s}  "
          f"{'Δm/m':>8s}  {'prop':>5s}")
    print(f"  {'─'*3}  {'─'*4}  {'─'*30}  {'─'*10}  {'─'*8}  {'─'*5}")

    scaled_13 = []
    for k in range(1, 30):
        n1 = k
        n2_base = 3 * k
        n5 = k - 1
        for n6 in range(-30, 31):
            for n2_sign in [+1, -1]:
                n = (n1, n2_sign * n2_base, 0, 0, n5, n6)
                if MaD.charge(n) != -1:
                    continue
                if MaD.spin_total(n) != 0.5:
                    continue
                try:
                    E = m.energy(n)
                except ValueError:
                    continue
                delta = abs(E - target)
                rel = delta / target
                prop = m.propagates(n)
                scaled_13.append({
                    'k': k, 'n': n, 'E': E,
                    'delta': delta, 'rel': rel, 'prop': prop,
                })

    scaled_13.sort(key=lambda x: x['delta'])
    for r in scaled_13[:25]:
        n = r['n']
        propmark = '✓' if r['prop'] else '✗'
        print(f"  {r['k']:>3d}  {n[5]:>4d}  {str(n):>30s}  "
              f"{r['E']:>10.3f}  {r['rel']*100:>7.3f}%  {propmark:>5s}")
    print()

    # ── Unscaled balanced ratios near muon ──────────────────────────
    print("=" * 78)
    print("All balanced-ratio modes within 10% of muon mass")
    print("=" * 78)
    print()
    results.sort(key=lambda x: x['delta'])
    shown = 0
    for r in results:
        if r['rel'] > 0.10:
            break
        n = r['n']
        print(f"  {str(n):>30s}  E={r['E']:>10.3f}  Δm/m={r['rel']*100:>7.3f}%  "
              f"e={r['e_ratio']}  p={r['p_ratio']}")
        shown += 1
    if shown == 0:
        print("  (none within 10%)")
    print()

    # ── Assessment ──────────────────────────────────────────────────
    print("=" * 78)
    print("Assessment")
    print("=" * 78)
    print()
    if scaled_results and scaled_results[0]['rel'] < 0.05:
        best = scaled_results[0]
        print(f"  Best scaled-electron mode: {best['n']}")
        print(f"  E = {best['E']:.3f} MeV, Δm/m = {best['rel']*100:.3f}%")
    if scaled_13 and scaled_13[0]['rel'] < 0.05:
        best = scaled_13[0]
        print(f"  Best scaled-proton mode: {best['n']}")
        print(f"  E = {best['E']:.3f} MeV, Δm/m = {best['rel']*100:.3f}%")
    print()
    print("Track 11b complete.")


if __name__ == '__main__':
    main()
