#!/usr/bin/env python3
"""
R31 Track 5: R³ vs T⁶ — the electron-proton energy landscape.

Two binding regimes:
  R³ binding (atom):     separate T⁶ modes, Coulomb across R³
  T⁶ merger  (neutron):  single T⁶ mode, same R³ point

Which is lower energy?  What's the energy landscape between them?
"""

import sys, os, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6_solver import self_consistent_metric
from lib.t6 import mode_energy, mode_charge, mode_spin, M_P_MEV, M_E_MEV, ALPHA, hbar_c_MeV_fm

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064

sc = self_consistent_metric(R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
Gti = sc['Gtilde_inv']
L = sc['L']


print("=" * 72)
print("R31 TRACK 5: R³ vs T⁶ — ELECTRON-PROTON ENERGY LANDSCAPE")
print("=" * 72)


# ── Section 1: Energy comparison ─────────────────────────────────

print("\n\n── Section 1: Two binding regimes ──\n")

E_proton = mode_energy([0, 0, 0, 0, 1, 2], Gti, L)
E_electron = mode_energy([1, 2, 0, 0, 0, 0], Gti, L)
E_neutron = mode_energy([0, -2, 1, 0, 0, 2], Gti, L)

E_H_separated = E_proton + E_electron  # at infinite separation
E_H_bound = E_proton + E_electron - 13.6e-6  # hydrogen ground state

print(f"  Regime 1: R³ SEPARATION (atom)")
print(f"    Proton mode energy:    {E_proton:.6f} MeV")
print(f"    Electron mode energy:  {E_electron:.6f} MeV")
print(f"    Sum (∞ separation):    {E_H_separated:.6f} MeV")
print(f"    Coulomb binding:       −{13.6e-6*1e6:.1f} eV")
print(f"    Hydrogen ground state: {E_H_bound:.6f} MeV")
print()
print(f"  Regime 2: T⁶ MERGER (neutron)")
print(f"    Neutron mode energy:   {E_neutron:.6f} MeV")
print(f"    Mode: (0, −2, 1, 0, 0, 2)")
print()

delta = E_neutron - E_H_bound
print(f"  Energy difference: neutron − hydrogen = {delta:.4f} MeV")
print(f"                                        = {delta*1e3:.1f} keV")
print(f"                                        = {delta*1e6:.0f} eV")
print()
print(f"  THE ATOM IS {delta:.3f} MeV LOWER ENERGY THAN THE NEUTRON.")
print(f"  This is why hydrogen is stable and neutrons decay.")


# ── Section 2: What happens at each separation? ─────────────────

print("\n\n── Section 2: Energy vs separation ──\n")

print("  As electron approaches proton in R³:\n")

a0_fm = hbar_c_MeV_fm / (M_E_MEV * ALPHA)  # Bohr radius in fm
L_tube_e = L[0]  # electron tube circumference
L_ring_e = L[1]  # electron ring circumference
L_tube_p = L[4]  # proton tube
L_ring_p = L[5]  # proton ring

print(f"  Key length scales:")
print(f"    Bohr radius:        a₀ = {a0_fm:,.0f} fm = {a0_fm*1e-4:.2f} Å")
print(f"    Electron tube:      L₁ = {L_tube_e:,.0f} fm")
print(f"    Electron ring:      L₂ = {L_ring_e:,.0f} fm")
print(f"    Proton tube:        L₅ = {L_tube_p:.1f} fm")
print(f"    Proton ring:        L₆ = {L_ring_p:.2f} fm")
print(f"    Proton 'radius':    ~{L_ring_p/2:.1f} fm")
print()

separations = [1e6, 1e5, a0_fm, 1e4, 1e3, L_tube_e, L_ring_e,
               100, L_tube_p, 10, L_ring_p, 1, 0.1, 0]

print(f"  {'r (fm)':>12s} {'V_Coulomb (eV)':>15s} {'Regime':>30s}")
print(f"  {'─'*60}")

for r in separations:
    if r > 0:
        V = -ALPHA * hbar_c_MeV_fm / r * 1e6  # eV
    else:
        V = float('-inf')

    if r > 10 * a0_fm:
        regime = "free particles"
    elif r > a0_fm / 10:
        regime = "atomic (Coulomb)"
    elif r > L_tube_e:
        regime = "sub-atomic, above e-tube"
    elif r > L_ring_e:
        regime = "at electron tube scale"
    elif r > L_tube_p:
        regime = "between e and p scales"
    elif r > L_ring_p:
        regime = "at proton tube scale"
    elif r > 0:
        regime = "inside proton ring"
    else:
        regime = "MERGED → neutron"

    if r > 0:
        print(f"  {r:12.1f} {V:15.1f}  {regime}")
    else:
        print(f"  {'0 (merged)':>12s} {'N/A':>15s}  {regime}")


# ── Section 3: The merger barrier ────────────────────────────────

print("\n\n── Section 3: The merger barrier ──\n")

print("  At infinite separation:")
print(f"    E = m_p + m_e = {E_H_separated:.6f} MeV")
print()
print("  At Bohr radius (a₀ = {:.0f} fm):".format(a0_fm))
V_bohr = -ALPHA * hbar_c_MeV_fm / a0_fm
print(f"    E = m_p + m_e + V_Coulomb = {E_H_separated + V_bohr:.6f} MeV")
print(f"    V_Coulomb = {V_bohr*1e6:.1f} eV = {V_bohr:.9f} MeV")
print()
print("  At merger (r → 0, becomes neutron):")
print(f"    E = m_n = {E_neutron:.6f} MeV")
print()

merger_cost = E_neutron - E_H_separated
print(f"  Energy to go from separated → merged:")
print(f"    ΔE = m_n − (m_p + m_e) = {merger_cost:.4f} MeV")
print(f"       = {merger_cost*1e3:.1f} keV")
print()

print("  Even at r = 0 (fully merged), the Coulomb potential is:")
V_at_ring = -ALPHA * hbar_c_MeV_fm / L_ring_p
print(f"    V(r = L₆) = {V_at_ring:.3f} MeV  (at proton ring scale)")
V_classical_0 = -ALPHA * hbar_c_MeV_fm / 0.1
print(f"    V(r = 0.1 fm) = {V_classical_0:.1f} MeV")
print()

print("  The Coulomb potential reaches ~{:.0f} MeV at r ~ proton scale.".format(abs(V_at_ring)))
print(f"  But the quantum reality is different: the electron cannot")
print(f"  be localized to < λ_e (Compton wavelength ≈ {2*math.pi*hbar_c_MeV_fm/M_E_MEV:.0f} fm)")
print(f"  without creating pairs.  The classical 'falling in' picture")
print(f"  breaks down long before r = 0.")
print()

print("  TRANSITION PICTURE:")
print("  ───────────────────")
print(f"  r > a₀ ({a0_fm:.0f} fm):     Free e + p, barely interacting")
print(f"  r ~ a₀:                      Hydrogen atom (Coulomb bound)")
print(f"  r ~ L₁ ({L_tube_e:.0f} fm):  Electron 'sees' compact geometry")
print(f"  r ~ L₂ ({L_ring_e:.0f} fm):  Electron wave overlaps with ring")
print(f"  r ~ L₅ ({L_tube_p:.1f} fm):  Proton tube scale (nuclear physics)")
print(f"  r ~ L₆ ({L_ring_p:.2f} fm):  Proton ring scale (deep nuclear)")
print(f"  r → 0:                        T⁶ merger → neutron")
print()
print(f"  The merger costs {merger_cost:.3f} MeV.  This energy must come")
print(f"  from somewhere — in nuclear physics, it comes from a")
print(f"  high-energy collision or weak interaction.  In our model,")
print(f"  it corresponds to the energy difference between the")
print(f"  separated T⁶ modes and the merged neutron mode.")


# ── Section 4: Why hydrogen doesn't collapse ────────────────────

print("\n\n── Section 4: Why hydrogen doesn't collapse into a neutron ──\n")

print("  The hydrogen atom has total energy:")
print(f"    E_H = m_p + m_e − 13.6 eV = {E_H_bound:.6f} MeV")
print()
print("  The neutron has energy:")
print(f"    E_n = {E_neutron:.6f} MeV")
print()
print(f"  E_n − E_H = {delta:.4f} MeV = {delta*1e6:.0f} eV")
print()
print("  The neutron is HEAVIER than hydrogen by {:.3f} MeV.".format(delta))
print("  To convert hydrogen → neutron requires:")
print("    1. Supplying {:.3f} MeV of energy".format(delta))
print("    2. Emitting a neutrino (to conserve lepton number)")
print()
print("  This is INVERSE beta decay: p + e → n + ν_e")
print(f"  Threshold energy: {delta:.3f} MeV")
print(f"  This only happens in extreme environments (supernovae,")
print(f"  neutron star formation) where ~MeV energies are available.")
print()
print("  At room temperature, kT = 0.026 eV — ten million times")
print("  below the merger threshold.  Hydrogen is stable because")
print("  the T⁶ merger state (neutron) costs 0.8 MeV more energy.")


# ── Section 5: The two-tier physics summarized ───────────────────

print("\n\n── Section 5: Two-tier physics — complete picture ──\n")

print("  TIER 1: T⁶ (compact geometry)")
print("  ─────────────────────────────")
print("  - Determines WHAT particles exist (mode spectrum)")
print("  - Sets particle masses (circumferences + shear)")
print("  - Sets nuclear masses (nuclei = T⁶ modes)")
print("  - Energy scale: MeV to GeV")
print("  - Free variable: α (shear) — not yet determined")
print()
print("  TIER 2: R³ (extended space)")
print("  ─────────────────────────────")
print("  - Determines HOW particles interact (Coulomb, etc.)")
print("  - Creates atomic structure (electron orbits)")
print("  - Determines nuclear stability (which isotopes survive)")
print("  - Energy scale: eV to keV")
print("  - Requires: α from Tier 1")
print()
print("  THE BRIDGE: α connects the tiers.")
print("  α is a property of T⁶ geometry (shear) that determines")
print("  the strength of R³ interactions (Coulomb).  It emerges")
print("  from the compact geometry but governs extended-space physics.")
print()
print("  To derive α is to understand HOW T⁶ produces R³ forces.")
print("  The KK reduction MECHANISM is understood (R29 Track 1).")
print("  The STRENGTH (specific value of α) is not yet predicted.")


# ── Summary ──────────────────────────────────────────────────────

print("\n\n── Summary ──\n")

print(f"  1. Hydrogen (R³ bound) is {delta:.3f} MeV lighter than")
print(f"     the neutron (T⁶ merged).  This is WHY atoms exist")
print(f"     and are stable — the separated state is lower energy.")
print()
print(f"  2. The energy landscape has TWO regimes:")
print(f"     - Coulomb (R³): deepens as 1/r, reaches −13.6 eV at a₀")
print(f"     - Merger (T⁶): costs +{merger_cost:.3f} MeV, produces neutron")
print()
print(f"  3. The merger barrier ({delta:.3f} MeV) is ~60,000× the")
print(f"     atomic binding energy (13.6 eV).  Atoms are stable")
print(f"     against collapse by a factor of 60,000.")
print()
print(f"  4. The two-tier picture is self-consistent:")
print(f"     - T⁶ makes particles and nuclei (MeV scale)")
print(f"     - R³ makes atoms (eV scale)")
print(f"     - α bridges the two (geometry → force strength)")
print()
print(f"  5. Deriving α is deriving the bridge between")
print(f"     compact geometry and extended-space physics.")
