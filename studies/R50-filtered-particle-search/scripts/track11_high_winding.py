"""
R50 Track 11: High ring-winding modes

The user's insight: instead of exotic mechanisms (back-reaction,
fabric tension, compound modes), the muon might simply be a
high ring-winding mode on the electron sheet.  The (1,2) electron
has E = 0.511 MeV.  What about (1, 506)?  Energy scales roughly
as n₂ for large n₂, so (1, ~506) should give ~105.7 MeV.

This script:
1. Computes E(1, n₂) for n₂ = 2 through 10,000
2. Finds the n₂ closest to each particle target
3. Checks Q, spin, and propagation
4. Reports the viability of the "high winding" picture
5. Also checks Q=0 spin-0 modes (0, n₂) for pions
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np

from lib.ma_model_d import MaD


def main():
    print("=" * 78)
    print("R50 Track 11: High ring-winding modes on the electron sheet")
    print("=" * 78)
    print()
    print("Question: can the muon be (1, ~506, 0, 0, 0, 0) — a high")
    print("ring-winding mode on Ma_e — instead of a compound or")
    print("back-reaction state?")
    print()

    # Build baseline model
    m = MaD.from_physics()

    # ── Section 1: E(1, n₂) for the lepton series ──────────────────
    print("=" * 78)
    print("Section 1: Q = -1, spin-½ modes: (1, n₂, 0, 0, 0, 0)")
    print("=" * 78)
    print()
    print("  These are pure e-sheet modes with:")
    print("  - n₁ = 1 (odd) → spin ½ ✓")
    print("  - Q = -n₁ + n₅ = -1 + 0 = -1 ✓")
    print("  - Propagation: n₂ > |n₁|/ε_e = 1.54, so n₂ ≥ 2 propagates ✓")
    print()

    # Compute energies for a range of n₂
    targets = [
        ('electron', 0.51099895),
        ('muon', 105.65837),
        ('tau', 1776.86),
    ]

    print(f"  {'n₂':>6s}  {'E (MeV)':>12s}  {'closest to':>10s}")
    print(f"  {'─'*6}  {'─'*12}  {'─'*10}")

    # Sample some n₂ values
    sample_n2 = list(range(2, 20)) + list(range(20, 100, 10)) + \
                list(range(100, 600, 50)) + list(range(600, 10000, 500))

    for n2 in sample_n2:
        n = (1, n2, 0, 0, 0, 0)
        E = m.energy(n)
        # Find closest target
        closest = min(targets, key=lambda t: abs(E - t[1]))
        label = closest[0] if abs(E - closest[1]) / closest[1] < 0.05 else ''
        print(f"  {n2:>6d}  {E:>12.4f}  {label:>10s}")
    print()

    # ── Section 2: Exact matches for each lepton ────────────────────
    print("=" * 78)
    print("Section 2: Best n₂ for each lepton")
    print("=" * 78)
    print()

    for name, target_mass in targets:
        best_n2 = None
        best_E = None
        best_delta = float('inf')
        for n2 in range(2, 20000):
            E = m.energy((1, n2, 0, 0, 0, 0))
            delta = abs(E - target_mass)
            if delta < best_delta:
                best_delta = delta
                best_n2 = n2
                best_E = E
        rel = best_delta / target_mass * 100
        print(f"  {name:>8s}: n₂ = {best_n2:>6d}  E = {best_E:>12.4f} MeV  "
              f"(target {target_mass:.4f}, Δm/m = {rel:.4f}%)")
    print()

    # ── Section 3: Q = 0, spin 0 modes for pions ───────────────────
    print("=" * 78)
    print("Section 3: Q = 0, spin-0 modes: (0, n₂, 0, 0, 0, 0)")
    print("=" * 78)
    print()
    print("  n₁ = 0 (even) → spin 0")
    print("  Q = -0 + 0 = 0")
    print("  Propagation: n₂ > 0/ε_e = 0 → always propagates")
    print()

    pion_targets = [
        ('pi0', 134.9768),
        ('eta', 547.862),
        ('eta-prime', 957.78),
        ('K0', 497.611),
    ]

    for name, target_mass in pion_targets:
        best_n2 = None
        best_E = None
        best_delta = float('inf')
        for n2 in range(1, 10000):
            E = m.energy((0, n2, 0, 0, 0, 0))
            delta = abs(E - target_mass)
            if delta < best_delta:
                best_delta = delta
                best_n2 = n2
                best_E = E
        rel = best_delta / target_mass * 100
        print(f"  {name:>10s}: n₂ = {best_n2:>6d}  E = {best_E:>12.4f} MeV  "
              f"(target {target_mass:.4f}, Δm/m = {rel:.4f}%)")
    print()

    # ── Section 4: What about charged pions? ────────────────────────
    print("=" * 78)
    print("Section 4: Can high n₂ help charged pions?")
    print("=" * 78)
    print()
    print("  π⁺ needs Q = +1, spin = 0.")
    print("  Q = -n₁ + n₅ = +1.")
    print("  For pure e-sheet (n₅=0): n₁ = -1 → Q = +1.")
    print("  Spin: n₁ = -1 (odd) → spin ½.  NOT spin 0.")
    print("  Adding p-sheet: n₁ = 0, n₅ = 1 → Q = +1.")
    print("  Spin: n₅ = 1 (odd) → spin ½.  NOT spin 0.")
    print("  n₁ = 1, n₅ = 2 → Q = +1. n₁ odd (½) + n₅ even (0) = ½.")
    print("  n₁ = 2, n₅ = 3 → Q = +1. n₁ even (0) + n₅ odd (½) = ½.")
    print()
    print("  → The spin-charge constraint persists at ANY n₂.")
    print("    Q = ±1 forces at least one odd tube winding → spin ≥ ½.")
    print("    High ring winding does NOT solve π±.")
    print()

    # ── Section 5: Mode density and the ghost problem ───────────────
    print("=" * 78)
    print("Section 5: Mode density — the ghost problem at high n₂")
    print("=" * 78)
    print()

    # Count Q=-1, spin-½ modes (1, n₂, 0, 0, 0, 0) in mass ranges
    bins = [(0.5, 5), (5, 50), (50, 106), (106, 200), (200, 500),
            (500, 1000), (1000, 1777), (1777, 2000)]
    print("  Q = -1, spin-½ modes (1, n₂, 0, 0, 0, 0) by mass range:")
    print()
    print(f"  {'Range (MeV)':>15s}  {'Count':>6s}  {'spacing (MeV)':>14s}")
    print(f"  {'─'*15}  {'─'*6}  {'─'*14}")
    for lo, hi in bins:
        count = 0
        for n2 in range(2, 20000):
            E = m.energy((1, n2, 0, 0, 0, 0))
            if lo <= E < hi:
                count += 1
        if count > 0:
            spacing = (hi - lo) / count
            print(f"  {lo:>6.1f}–{hi:<6.1f}  {count:>6d}  {spacing:>14.3f}")
        else:
            print(f"  {lo:>6.1f}–{hi:<6.1f}  {count:>6d}  {'—':>14s}")
    print()

    # ── Section 6: Energy per unit n₂ ───────────────────────────────
    print("=" * 78)
    print("Section 6: Energy per unit n₂ (asymptotic spacing)")
    print("=" * 78)
    print()
    E2 = m.energy((1, 2, 0, 0, 0, 0))
    E100 = m.energy((1, 100, 0, 0, 0, 0))
    E500 = m.energy((1, 500, 0, 0, 0, 0))
    E1000 = m.energy((1, 1000, 0, 0, 0, 0))
    print(f"  E(1, 2)    = {E2:.6f} MeV")
    print(f"  E(1, 100)  = {E100:.4f} MeV  → {E100/100:.4f} MeV per n₂")
    print(f"  E(1, 500)  = {E500:.4f} MeV  → {E500/500:.4f} MeV per n₂")
    print(f"  E(1, 1000) = {E1000:.4f} MeV  → {E1000/1000:.4f} MeV per n₂")
    print()
    print(f"  Asymptotic: E/n₂ → {_TWO_PI_HC(m):.4f} MeV")
    print()

    # ── Assessment ──────────────────────────────────────────────────
    print("=" * 78)
    print("Assessment")
    print("=" * 78)
    print()
    print("  The muon and tau are trivially matched by high ring-winding")
    print("  modes on the electron sheet.  The 'mass desert' was an")
    print("  artifact of the n₂ ≤ 10 search range in Track 8.")
    print()
    print("  But this creates a severe ghost problem: there are ~500")
    print("  Q = -1, spin-½ modes between the electron and muon, each")
    print("  separated by ~0.21 MeV.  Why is the muon at n₂ ≈ 506")
    print("  special, and not n₂ = 505 or 507?")
    print()
    print("  The π⁰ is also trivially matched by (0, ~647, 0, 0, 0, 0).")
    print("  But π± remains forbidden — the spin-charge constraint is")
    print("  independent of n₂.")
    print()
    print("Track 11 complete.")


def _TWO_PI_HC(model):
    """Asymptotic energy per unit n₂."""
    L_ring_e = model.L_ring[0]
    from lib.ma_model_d import _TWO_PI_HC as TPC
    return TPC / L_ring_e


if __name__ == '__main__':
    main()
