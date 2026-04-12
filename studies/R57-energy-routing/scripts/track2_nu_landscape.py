"""
R57 Track 2: Neutrino-scale energy landscape

When energy enters the ν-sheet (e.g., THz radiation at neutrino
frequencies), where does it go?  Does it:
  (a) Create new neutrinos (populate active modes at new S locations)
  (b) Excite dark modes on the ν-sheet (accumulate in Ma)
  (c) Bleed into S as radiation

Map the mode density around each active neutrino.  Count how many
dark modes are within reach.  Compute the routing at each step
of energy accumulation.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.metric import Metric
from lib.routing import RoutingEngine


def main():
    print("=" * 70)
    print("R57 Track 2: Neutrino-scale energy landscape")
    print("=" * 70)
    print()

    m = Metric.model_E()
    engine = RoutingEngine(m, n_ranges=[
        (-3, 3), (-5, 5),     # e-sheet (modest range)
        (-10, 10), (-10, 10), # ν-sheet (wide — this is the focus)
        (-3, 3), (-5, 5),     # p-sheet (modest)
    ])

    # ── The three active neutrinos ─────────────────────────────
    nu1 = (0, 0, 1, 1, 0, 0)
    nu2 = (0, 0, -1, 1, 0, 0)
    nu3 = (0, 0, 1, 2, 0, 0)

    print("Active neutrinos:")
    for label, mode in [("ν₁", nu1), ("ν₂", nu2), ("ν₃", nu3)]:
        E = m.mode_energy(mode)
        print(f"  {label} = {mode}  E = {E*1e3:.6f} keV  ({E:.9f} MeV)")
    print()

    # ── Mode census at the ν scale ─────────────────────────────
    print("=" * 70)
    print("Mode census: all modes below 1 MeV")
    print("=" * 70)
    print()

    all_modes = engine.mode_census(E_max_MeV=1.0)

    # Classify
    active_set = {nu1, nu2, nu3}
    n_active = 0
    n_sterile_half = 0
    n_dark_boson = 0
    for mode in all_modes:
        if mode.n in active_set:
            n_active += 1
        elif mode.sh in (1, 3):
            n_sterile_half += 1
        else:
            n_dark_boson += 1

    print(f"  Total modes below 1 MeV: {len(all_modes)}")
    print(f"    Active neutrinos: {n_active}")
    print(f"    Sterile fermions (odd n_t, not active): {n_sterile_half}")
    print(f"    Dark bosons (even n_t): {n_dark_boson}")
    print(f"    Dark/Active ratio: {(n_sterile_half + n_dark_boson)/max(n_active,1):.0f}:1")
    print()

    # ── Neighborhood of each active neutrino ───────────────────
    print("=" * 70)
    print("Neighborhood of each active neutrino (±10% in energy)")
    print("=" * 70)
    print()

    for label, nu_mode in [("ν₁", nu1), ("ν₂", nu2), ("ν₃", nu3)]:
        E_nu = m.mode_energy(nu_mode)
        tolerance = E_nu * 0.10  # 10%

        neighbors = engine.modes_near(E_nu, tolerance_MeV=tolerance)

        n_dark_near = sum(1 for n in neighbors
                         if n.n not in active_set and n.sh in (0, 2))
        n_sterile_near = sum(1 for n in neighbors
                            if n.n not in active_set and n.sh in (1, 3))

        print(f"  {label} at {E_nu*1e3:.4f} keV (±{tolerance*1e3:.4f} keV):")
        print(f"    Total neighbors: {len(neighbors)}")
        print(f"    Dark bosons: {n_dark_near}")
        print(f"    Sterile fermions: {n_sterile_near}")
        print(f"    Active: {sum(1 for n in neighbors if n.n in active_set)}")
        print()

        # Show the 10 closest
        print(f"    Closest 10 modes:")
        print(f"    {'E (keV)':>10s}  {'gap%':>7s}  {'mode':>25s}  {'type':>12s}")
        print(f"    {'─'*10}  {'─'*7}  {'─'*25}  {'─'*12}")
        for n in neighbors[:10]:
            gap = (n.E - E_nu) / E_nu * 100
            if n.n in active_set:
                mtype = "ACTIVE"
            elif n.sh in (1, 3):
                mtype = "sterile-½"
            else:
                mtype = "dark-boson"
            print(f"    {n.E*1e3:>10.4f}  {gap:>+6.2f}%  {str(n.n):>25s}  {mtype:>12s}")
        print()

    # ── Single-step transitions from ν₁ ────────────────────────
    print("=" * 70)
    print("Single-step transitions from ν₁")
    print("=" * 70)
    print()

    trans = engine.transitions_from(nu1, E_max_delta=0.1)  # 100 keV
    print(f"  Transitions within ±100 keV: {len(trans)}")
    print()

    up = [t for t in trans if t.delta_E > 1e-9]
    down = [t for t in trans if t.delta_E < -1e-9]
    zero = [t for t in trans if abs(t.delta_E) <= 1e-9]

    print(f"  Zero-cost (ν additions): {len(zero)}")
    print(f"  Upward (cost energy): {len(up)}")
    print(f"  Downward (release energy): {len(down)}")
    print()

    if up:
        print(f"  Cheapest upward transitions from ν₁:")
        for t in up[:5]:
            Q = m.charge(t.target)
            sh = m.spin_half_count(t.target)
            mtype = "active" if t.target in active_set else (
                "sterile" if sh % 2 == 1 else "dark")
            print(f"    → {t.target}  ΔE={t.delta_E*1e3:+.4f} keV  "
                  f"Q={Q}  sh={sh}  {mtype}  Δn={t.delta_n}")
        print()

    # ── Energy accumulation pathway ────────────────────────────
    print("=" * 70)
    print("Energy accumulation: how far can dark modes reach?")
    print("=" * 70)
    print()

    print("  Starting from ν₁, what is the maximum energy reachable")
    print("  by stepping through single-quantum transitions?")
    print()

    # Greedy upward walk from ν₁
    current = nu1
    total_E = m.mode_energy(current)
    steps = 0
    max_E = total_E
    path_modes = [current]

    for _ in range(100):
        trans = engine.transitions_from(current, E_max_delta=500)
        up = [t for t in trans if t.delta_E > 1e-6]
        if not up:
            break
        # Take the cheapest upward step
        best = up[0]
        current = best.target
        total_E = m.mode_energy(current)
        if total_E > max_E:
            max_E = total_E
        steps += 1
        path_modes.append(current)
        if total_E > 1.0:  # stop at 1 MeV
            break

    print(f"  From ν₁ ({m.mode_energy(nu1)*1e3:.4f} keV):")
    print(f"  Reached {max_E*1e3:.2f} keV in {steps} steps")
    print(f"  Electron threshold: {m.mode_energy((1,2,0,0,0,0))*1e3:.2f} keV")
    print(f"  Ratio: {max_E / m.mode_energy((1,2,0,0,0,0)):.1f}×")
    print()

    # Show the path
    print(f"  First 15 steps of accumulation path:")
    print(f"  {'step':>5s}  {'E (keV)':>10s}  {'mode':>30s}  {'type':>10s}")
    print(f"  {'─'*5}  {'─'*10}  {'─'*30}  {'─'*10}")
    for i, mode in enumerate(path_modes[:15]):
        E = m.mode_energy(mode)
        sh = m.spin_half_count(mode)
        mtype = "active" if mode in active_set else (
            "sterile" if sh % 2 == 1 else "dark")
        print(f"  {i:>5d}  {E*1e3:>10.4f}  {str(mode):>30s}  {mtype:>10s}")

    print()

    # ── Routing decision at each energy scale ──────────────────
    print("=" * 70)
    print("Routing: at each energy, Ma accumulation vs S separation?")
    print("=" * 70)
    print()

    print("  At each energy scale, compare:")
    print("    Ma: cost of next dark mode above current energy")
    print("    S:  cost of creating a new particle at that energy")
    print("        (= the mode energy itself, since you need to")
    print("         duplicate the mode at a new S location)")
    print()

    energies_keV = [0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0, 511.0]
    print(f"  {'E (keV)':>10s}  {'next Ma (keV)':>14s}  {'S duplicate':>12s}  {'route':>10s}")
    print(f"  {'─'*10}  {'─'*14}  {'─'*12}  {'─'*10}")

    for E_keV in energies_keV:
        E_MeV = E_keV / 1e3
        # Next mode above this energy (any type)
        next_mode = engine.next_above(E_MeV)
        if next_mode:
            ma_cost = (next_mode.E - E_MeV) * 1e3  # keV
        else:
            ma_cost = float('inf')

        # S duplication cost = the mode energy (create a copy)
        s_cost = E_keV

        route = "Ma" if ma_cost < s_cost else "S"

        ma_str = f"{ma_cost:.4f}" if ma_cost < 1e6 else "∞"
        print(f"  {E_keV:>10.2f}  {ma_str:>14s}  {s_cost:>12.2f}  {route:>10s}")

    print()
    print("Track 2 complete.")


if __name__ == '__main__':
    main()
