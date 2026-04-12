"""
R57 Track 3: Proton-to-neutron pathway — cross-sheet analysis

Two questions:
  A. Are there compound dark modes (spanning multiple sheets) that
     fill the energy desert between ν-scale and nuclear-scale?
  B. Is there a least-energy path from p + e + ν → n that goes
     through these compound modes?

This track uses the SINGLE-MODE picture: one 6-tuple transitions
to another.  Track 4 will address multi-mode accumulation.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
from itertools import product as iproduct
from lib.metric import Metric
from lib.routing import RoutingEngine


def main():
    print("=" * 70)
    print("R57 Track 3: Proton-to-neutron cross-sheet pathway")
    print("=" * 70)
    print()

    m = Metric.model_E()
    engine = RoutingEngine(m, n_ranges=[
        (-3, 3), (-8, 8),
        (-3, 3), (-3, 3),
        (-3, 3), (-10, 10),
    ])

    proton = (0, 0, 0, 0, 1, 3)
    neutron = (0, -4, -1, 2, 0, -3)
    electron = (1, 2, 0, 0, 0, 0)

    E_p = m.mode_energy(proton)
    E_n = m.mode_energy(neutron)
    E_e = m.mode_energy(electron)
    delta_pn = E_n - E_p

    print(f"  Proton:   {proton}  E = {E_p:.3f} MeV")
    print(f"  Neutron:  {neutron}  E = {E_n:.3f} MeV")
    print(f"  Electron: {electron}  E = {E_e:.6f} MeV")
    print(f"  n-p difference: {delta_pn*1e3:.1f} keV ({delta_pn:.3f} MeV)")
    print()

    # ════════════════════════════════════════════════════════════
    # PART A: Compound dark modes in the desert
    # ════════════════════════════════════════════════════════════

    print("=" * 70)
    print("Part A: Compound dark modes spanning the energy desert")
    print("  (modes with windings on 2+ sheets, filling 0.1-100 MeV)")
    print("=" * 70)
    print()

    # Find all Q=0 modes in the desert range
    desert_modes = engine.mode_census(E_max_MeV=200, Q=0)
    desert_modes = [md for md in desert_modes if md.E > 0.1]

    # Classify by sheet content
    multi_sheet = [md for md in desert_modes
                   if md.sheets.count('+') >= 1]  # spans 2+ sheets
    single_sheet = [md for md in desert_modes
                    if '+' not in md.sheets]

    print(f"  Q=0 modes in 0.1-200 MeV range: {len(desert_modes)}")
    print(f"    Single-sheet: {len(single_sheet)}")
    print(f"    Multi-sheet: {len(multi_sheet)}")
    print()

    # Energy distribution
    bins = [(0.1, 1), (1, 10), (10, 50), (50, 100), (100, 200)]
    print(f"  Energy distribution of Q=0 multi-sheet modes:")
    print(f"  {'Range (MeV)':>15s}  {'count':>6s}  {'dark':>6s}  {'sterile':>8s}")
    print(f"  {'─'*15}  {'─'*6}  {'─'*6}  {'─'*8}")
    for lo, hi in bins:
        band = [md for md in multi_sheet if lo <= md.E < hi]
        dark = sum(1 for md in band if md.sh in (0, 2))
        sterile = sum(1 for md in band if md.sh in (1, 3))
        print(f"  {lo:>6.1f}-{hi:<6.1f}  {len(band):>6d}  {dark:>6d}  {sterile:>8d}")
    print()

    # Show examples in each range
    print(f"  Sample compound dark modes:")
    print(f"  {'E (MeV)':>10s}  {'mode':>30s}  {'sh':>3s}  {'sheets':>8s}")
    print(f"  {'─'*10}  {'─'*30}  {'─'*3}  {'─'*8}")
    shown = set()
    for md in multi_sheet:
        E_bin = int(md.E)
        if E_bin not in shown and len(shown) < 20:
            shown.add(E_bin)
            print(f"  {md.E:>10.2f}  {str(md.n):>30s}  {md.sh:>3d}  {md.sheets:>8s}")
    print()

    # ════════════════════════════════════════════════════════════
    # PART B: The p → n pathway (detailed)
    # ════════════════════════════════════════════════════════════

    print("=" * 70)
    print("Part B: Detailed proton → neutron pathway")
    print("=" * 70)
    print()

    path = engine.find_pathway(proton, neutron, max_steps=30)
    if path:
        print(f"  Path found: {len(path)} steps")
        print()
        print(f"  {'step':>5s}  {'mode':>30s}  {'E (MeV)':>10s}  {'ΔE':>10s}  "
              f"{'cum ΔE':>10s}  {'Q':>3s}  {'sh':>3s}  {'sheets':>8s}")
        print(f"  {'─'*5}  {'─'*30}  {'─'*10}  {'─'*10}  {'─'*10}  "
              f"{'─'*3}  {'─'*3}  {'─'*8}")

        cum = 0
        print(f"  {'start':>5s}  {str(proton):>30s}  {E_p:>10.3f}  "
              f"{'—':>10s}  {'—':>10s}  "
              f"{m.charge(proton):>3d}  {m.spin_half_count(proton):>3d}  "
              f"{m.sheets(proton):>8s}")

        max_E = E_p
        min_E = E_p
        barrier = 0

        for i, t in enumerate(path):
            E = m.mode_energy(t.target)
            cum += t.delta_E
            Q = m.charge(t.target)
            sh = m.spin_half_count(t.target)
            sheets = m.sheets(t.target)
            if E > max_E:
                max_E = E
            if E < min_E:
                min_E = E

            print(f"  {i+1:>5d}  {str(t.target):>30s}  {E:>10.3f}  "
                  f"{t.delta_E:>+10.3f}  {cum:>+10.3f}  "
                  f"{Q:>3d}  {sh:>3d}  {sheets:>8s}")

        print()
        print(f"  Summary:")
        print(f"    Start: {E_p:.3f} MeV (proton)")
        print(f"    End:   {E_n:.3f} MeV (neutron)")
        print(f"    Net:   {cum:+.3f} MeV")
        print(f"    Max E along path: {max_E:.3f} MeV")
        print(f"    Min E along path: {min_E:.3f} MeV")
        print(f"    Ma barrier: {max_E - E_p:.3f} MeV above start")
        print()

        # Compare to Coulomb barrier
        # For p + e → n + ν_e (electron capture):
        # The Coulomb barrier for an electron to penetrate a proton is
        # approximately α × m_e × c² ≈ 3.7 keV (classical turning point)
        # But for p + p → d + e⁺ + ν_e (fusion), the Coulomb barrier is
        # ~ Z₁Z₂ α ℏc / r_nuclear ≈ 1 × 197 / 1.2 ≈ 164 keV
        coulomb_pp = 197.3 / 1.2  # keV, pp fusion
        coulomb_pe = 1.0 / 137 * 511  # keV, electron capture

        print(f"    Coulomb barriers for comparison:")
        print(f"      p + p fusion: ~{coulomb_pp:.0f} keV")
        print(f"      e capture:    ~{coulomb_pe:.1f} keV")
        print(f"      Ma pathway:   {(max_E - E_p)*1e3:.0f} keV (or 0 if barrier is below start)")
    else:
        print("  No path found in 30 steps")

    print()

    # ════════════════════════════════════════════════════════════
    # PART C: Is the pathway barrier-free?
    # ════════════════════════════════════════════════════════════

    print("=" * 70)
    print("Part C: Energy profile of the pathway")
    print("=" * 70)
    print()

    if path:
        print("  The path energy profile tells us whether there's a")
        print("  barrier in Ma space.  If the energy DECREASES from")
        print("  proton to some intermediate, then increases to neutron,")
        print("  the barrier is the highest point above the start.")
        print()

        # Check: does the path go through zero energy?
        goes_low = min_E < 1.0  # goes below 1 MeV
        if goes_low:
            print(f"  ⚠ The path goes as low as {min_E:.3f} MeV")
            print(f"    (step where E approaches 0 represents the mode")
            print(f"     dissolving — all windings unwound — before")
            print(f"     rebuilding as the neutron)")
            print()
            print(f"  This means the greedy pathway DISMANTLES the proton")
            print(f"  completely (to nearly zero energy) then rebuilds the")
            print(f"  neutron from scratch.  The barrier is NOT the issue")
            print(f"  — the issue is that {E_p:.0f} MeV must be released")
            print(f"  and then re-supplied.")
            print()
            print(f"  A DIRECT transition (simultaneous rearrangement of")
            print(f"  all 6 quantum numbers) would cost only the net")
            print(f"  difference: {delta_pn*1e3:+.1f} keV.  But single-step")
            print(f"  transitions can't do this — they change one quantum")
            print(f"  number at a time.")
        else:
            print(f"  The path stays above {min_E:.1f} MeV throughout.")
            print(f"  Ma barrier = {(max_E - E_p)*1e3:.0f} keV above start.")

    print()

    # ════════════════════════════════════════════════════════════
    # PART D: Direct transition energy
    # ════════════════════════════════════════════════════════════

    print("=" * 70)
    print("Part D: Direct (simultaneous) transition cost")
    print("=" * 70)
    print()

    print(f"  If all 6 quantum numbers change simultaneously:")
    print(f"    proton {proton} → neutron {neutron}")
    print(f"    ΔE = {delta_pn*1e3:+.1f} keV")
    print(f"    Δn = {tuple(neutron[i]-proton[i] for i in range(6))}")
    print()
    print(f"  This is the MINIMUM energy cost.  No intermediate states,")
    print(f"  no barrier.  The 0.6 MeV is just the mass difference.")
    print()
    print(f"  In the S picture: electron capture requires the electron")
    print(f"  to penetrate the proton's Coulomb field (~{coulomb_pe:.1f} keV barrier).")
    print()
    print(f"  In the Ma picture: the transition is a mode rearrangement")
    print(f"  on the T⁶.  Cost = net mass difference only ({delta_pn*1e3:.1f} keV).")
    print(f"  No Coulomb barrier because the rearrangement happens in Ma,")
    print(f"  not in S.")
    print()

    # The question: can the simultaneous transition happen?
    print(f"  Can the simultaneous transition happen?")
    print(f"  In the single-mode picture: NO — you can only change")
    print(f"  one quantum number at a time, which means dismantling")
    print(f"  and rebuilding (the greedy path).")
    print()
    print(f"  In the multi-mode picture (Track 4): POSSIBLY — if many")
    print(f"  small modes accumulate at the same S location and their")
    print(f"  combined effect is equivalent to the quantum number")
    print(f"  rearrangement.  The neutrino dark modes (0.03 keV each)")
    print(f"  could provide the ν-sheet content; the electron provides")
    print(f"  the e-sheet content; the proton provides the p-sheet")
    print(f"  content.  The question is whether their CO-LOCATION")
    print(f"  triggers the rearrangement.")
    print()

    print("Track 3 complete.")


if __name__ == '__main__':
    main()
