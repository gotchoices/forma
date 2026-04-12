"""
R57 Track 4: Multi-mode accumulation

Key question: can many small dark modes at the same S location
accumulate enough energy to trigger a p → n transition?

The pieces:
  - Proton at some S coordinate: (0, 0, 0, 0, 1, 3) at 938.3 MeV
  - Electron co-located: (1, 2, 0, 0, 0, 0) at 0.511 MeV
  - Need: 0.624 MeV additional to reach neutron mass

Dark bosons on the ν-sheet:
  - Each at ~0.03 keV = 3×10⁻⁵ MeV
  - Need: 0.624 MeV / 3×10⁻⁵ MeV ≈ 20,800 dark bosons

Questions:
  A. Can dark bosons stack at the same S location? (No Pauli exclusion)
  B. What is the mode density — how many DISTINCT dark bosons exist?
  C. What is the accumulation rate at a given input power?
  D. Is there a leakage rate (do dark modes decay)?
  E. What experimental conditions would reach the threshold?
"""

import sys
import os
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.metric import Metric
from lib.routing import RoutingEngine


def main():
    print("=" * 70)
    print("R57 Track 4: Multi-mode accumulation")
    print("=" * 70)
    print()

    m = Metric.model_E()
    engine = RoutingEngine(m, n_ranges=[
        (-1, 1), (-2, 2),         # e-sheet (minimal)
        (-10, 10), (-10, 10),     # ν-sheet (wide)
        (-1, 1), (-3, 3),        # p-sheet (minimal)
    ])

    # ════════════════════════════════════════════════════════════
    # PART A: Dark boson stacking — the rules
    # ════════════════════════════════════════════════════════════

    print("Part A: Can dark bosons stack?")
    print("=" * 70)
    print()
    print("  Dark bosons have even tube winding → integer spin.")
    print("  Bosons obey Bose-Einstein statistics: unlimited")
    print("  occupancy per mode.  There is NO Pauli exclusion.")
    print()
    print("  A single dark mode (e.g., (0,0,2,0,0,0) on the ν-sheet)")
    print("  can be occupied by any number of quanta.  Each quantum")
    print("  adds one unit of mode energy to the location.")
    print()
    print("  Fermions (odd tube, spin ½) are limited to 2 per mode")
    print("  (tube winding ±1).  But dark bosons have no such limit.")
    print()

    # ════════════════════════════════════════════════════════════
    # PART B: Dark boson inventory near the ν scale
    # ════════════════════════════════════════════════════════════

    print("Part B: Dark boson inventory near the ν scale")
    print("=" * 70)
    print()

    # Count distinct dark boson modes
    dark_bosons = engine.mode_census(E_max_MeV=0.001, Q=0, spin=0.0)
    print(f"  Distinct dark boson modes below 1 keV: {len(dark_bosons)}")
    print()

    # What is the energy of each?
    energies = {}
    for mode in dark_bosons:
        E_keV = mode.E * 1e3
        E_bin = round(E_keV, 4)
        if E_bin not in energies:
            energies[E_bin] = []
        energies[E_bin].append(mode)

    print(f"  Distinct energy levels: {len(energies)}")
    print(f"  {'E (keV)':>10s}  {'count':>6s}  {'example':>25s}")
    print(f"  {'─'*10}  {'─'*6}  {'─'*25}")
    for E_keV in sorted(energies.keys())[:15]:
        modes = energies[E_keV]
        print(f"  {E_keV:>10.4f}  {len(modes):>6d}  {str(modes[0].n):>25s}")
    print()

    # ════════════════════════════════════════════════════════════
    # PART C: Accumulation arithmetic
    # ════════════════════════════════════════════════════════════

    print("Part C: Accumulation arithmetic")
    print("=" * 70)
    print()

    # The neutron threshold
    E_threshold = 0.624  # MeV needed above proton + electron

    # Lightest dark boson
    if dark_bosons:
        lightest = dark_bosons[0]
        E_quant = lightest.E  # MeV
        E_quant_keV = E_quant * 1e3
    else:
        E_quant = 3e-5  # fallback
        E_quant_keV = 0.03

    N_needed = math.ceil(E_threshold / E_quant) if E_quant > 0 else float('inf')

    print(f"  Neutron threshold above (proton + electron): {E_threshold*1e3:.1f} keV")
    print(f"  Lightest dark boson: {E_quant_keV:.4f} keV")
    print(f"  Quanta needed: {N_needed:,}")
    print()

    # But: each DISTINCT mode can hold unlimited quanta.
    # With N_distinct modes, each holding k quanta:
    # Total energy = Σ (k_i × E_i)
    # Simplest: all modes identical → N_needed quanta of one mode
    # More realistic: spread across distinct modes

    print(f"  Stacking options:")
    print(f"    Single mode × {N_needed:,} quanta = {E_threshold*1e3:.1f} keV ✓")
    print(f"    {len(dark_bosons)} modes × {N_needed//max(len(dark_bosons),1):,} quanta each "
          f"= {len(dark_bosons) * (N_needed//max(len(dark_bosons),1)) * E_quant_keV:.1f} keV")
    print()

    # ════════════════════════════════════════════════════════════
    # PART D: Accumulation rate
    # ════════════════════════════════════════════════════════════

    print("Part D: Accumulation rate estimates")
    print("=" * 70)
    print()

    print("  The rate depends on the Ma-S coupling (how efficiently")
    print("  external energy populates Ma dark modes).  This coupling")
    print("  is the subject of R55 and hasn't been quantified.")
    print()
    print("  We can estimate bounds:")
    print()

    # If coupling is α (electromagnetic strength):
    # Power absorbed into Ma = α × incident power on mode
    # For THz at 7 THz (ν₁ frequency) with 1 mW power:
    P_incident_mW = 1.0  # milliwatt
    P_incident_eV_s = P_incident_mW * 1e-3 / 1.602e-19  # eV/s
    alpha = 1.0 / 137

    # Energy per photon at 7 THz
    h_eV = 4.136e-15  # eV·s
    f_THz = 7.0e12  # Hz
    E_photon_eV = h_eV * f_THz  # ~29 meV
    E_photon_keV = E_photon_eV * 1e-3

    photon_rate = P_incident_eV_s / E_photon_eV  # photons/s

    print(f"  THz source at 7 THz, 1 mW:")
    print(f"    Photon energy: {E_photon_eV*1e3:.1f} meV = {E_photon_keV:.4f} keV")
    print(f"    Photon rate: {photon_rate:.2e} photons/s")
    print()

    # If each photon has probability α² of exciting a dark mode
    # (the coupling goes through Ma-S twice: photon→Ma and Ma→dark)
    for coupling_label, coupling in [("α", alpha), ("α²", alpha**2),
                                      ("α³", alpha**3)]:
        rate = photon_rate * coupling  # dark mode excitations per second
        E_per_s_keV = rate * E_photon_keV  # keV deposited per second
        time_to_threshold = E_threshold * 1e3 / E_per_s_keV if E_per_s_keV > 0 else float('inf')

        print(f"  Coupling = {coupling_label} ({coupling:.2e}):")
        print(f"    Dark mode rate: {rate:.2e} /s")
        print(f"    Energy deposit: {E_per_s_keV:.2e} keV/s")
        if time_to_threshold < 1e10:
            if time_to_threshold < 60:
                print(f"    Time to threshold: {time_to_threshold:.1f} seconds")
            elif time_to_threshold < 3600:
                print(f"    Time to threshold: {time_to_threshold/60:.1f} minutes")
            elif time_to_threshold < 86400:
                print(f"    Time to threshold: {time_to_threshold/3600:.1f} hours")
            else:
                print(f"    Time to threshold: {time_to_threshold/86400:.1f} days")
        else:
            print(f"    Time to threshold: {time_to_threshold:.1e} seconds (impractical)")
        print()

    # ════════════════════════════════════════════════════════════
    # PART E: Leakage — do dark modes persist?
    # ════════════════════════════════════════════════════════════

    print("Part E: Dark mode persistence")
    print("=" * 70)
    print()

    print("  Dark bosons (even tube winding) have:")
    print("    - Zero electric charge (Q = 0)")
    print("    - Zero magnetic moment")
    print("    - No electromagnetic coupling to S")
    print()
    print("  If the Ma-S coupling for the ν-sheet is truly zero")
    print("  (as model-E assumes for neutral modes), dark bosons")
    print("  CANNOT radiate.  They persist indefinitely once excited.")
    print("  Energy accumulates without leakage.")
    print()
    print("  However: if there is ANY nonzero ν-S coupling (even tiny),")
    print("  dark modes slowly radiate.  The accumulation race is:")
    print("    Input rate (from external source) vs Leakage rate")
    print("  If input > leakage: accumulation succeeds.")
    print("  If input < leakage: energy bleeds away, threshold unreachable.")
    print()
    print("  The leakage rate is unknown — it depends on the ν-S")
    print("  coupling strength, which is the subject of R55 and L04.")
    print()

    # ════════════════════════════════════════════════════════════
    # PART F: The co-location scenario
    # ════════════════════════════════════════════════════════════

    print("Part F: The co-location scenario for p → n")
    print("=" * 70)
    print()

    print("  In a hydrogen-loaded palladium lattice:")
    print("    - Protons sit at interstitial sites (~2.9 Å apart)")
    print("    - Electrons are delocalized in the conduction band")
    print("    - Both are co-located at nuclear scale")
    print()
    print("  The neutron transition requires:")
    print(f"    - Proton content: n₅=1, n₆=3 (already present)")
    print(f"    - Electron content: n₁~0, n₂~−4 (electron provides)")
    print(f"    - Neutrino content: n₃=−1, n₄=2 (from dark modes)")
    print(f"    - Energy: +{E_threshold*1e3:.0f} keV (from accumulated dark modes)")
    print()
    print("  The transition sequence:")
    print("    1. Dark bosonic ν modes accumulate at the proton site")
    print("    2. Energy builds toward the 624 keV threshold")
    print("    3. When threshold is reached, the co-located p + e + ν")
    print("       system rearranges into a neutron (mode change in Ma)")
    print("    4. The neutron, being unstable (near-miss), either:")
    print("       a. Decays back (n → p + e + ν, releasing the energy)")
    print("       b. Fuses with a neighboring proton (n + p → d + γ)")
    print()

    # Deuteron formation energy
    m_d = 1875.613  # MeV
    m_p = 938.272
    m_n = 939.565
    binding = (m_p + m_n) - m_d  # MeV
    print(f"  If fusion occurs (n + p → d):")
    print(f"    Deuteron binding energy: {binding:.3f} MeV = {binding*1e3:.0f} keV")
    print(f"    Released as: γ ray at {binding:.1f} MeV")
    print(f"    This is the signature of a successful LENR event.")
    print()
    print(f"  Energy budget:")
    print(f"    Input:  {E_threshold*1e3:.0f} keV (to make the neutron)")
    print(f"    Output: {binding*1e3:.0f} keV (from deuteron binding)")
    print(f"    Net gain: {(binding - E_threshold)*1e3:.0f} keV per event")
    print(f"    Gain ratio: {binding/E_threshold:.1f}×")
    print()

    # ════════════════════════════════════════════════════════════
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("  1. Dark bosons CAN stack without limit (Bose-Einstein)")
    print(f"  2. ~{N_needed:,} quanta at {E_quant_keV:.3f} keV reach the threshold")
    print(f"  3. At coupling α: threshold in ~{photon_rate*alpha*E_photon_keV/(E_threshold*1e3):.0e}⁻¹ s with 1 mW THz")
    print(f"  4. Dark modes may persist indefinitely (no EM coupling)")
    print(f"  5. Co-located p + e + ν → n costs only 624 keV")
    print(f"  6. Subsequent n + p → d releases {binding*1e3:.0f} keV")
    print(f"  7. Net energy gain: {(binding-E_threshold)*1e3:.0f} keV per event ({binding/E_threshold:.1f}×)")
    print()
    print("  The feasibility hinges on TWO unknowns:")
    print("    - The Ma-S coupling for ν dark modes (R55)")
    print("    - The dark mode leakage rate (L04 can test)")
    print()
    print("Track 4 complete.")


if __name__ == '__main__':
    main()
