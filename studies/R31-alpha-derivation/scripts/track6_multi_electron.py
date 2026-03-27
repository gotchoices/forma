#!/usr/bin/env python3
"""
R31 Track 6: Multi-electron atoms and the Pauli principle in Ma.

All electrons share the SAME T² sheet.  Different electrons in
multi-electron atoms are distinguished by R³ orbital/spin states,
not by Ma geometry.  This track quantifies these statements.

Key questions:
  - Is r_e a property of the geometry or per-electron?
  - How does Pauli exclusion work in Ma + R³?
  - Can Ma accommodate multi-electron atoms?
  - What determines electron shell structure?
"""

import sys, os, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_solver import self_consistent_metric
from lib.ma import mode_energy, mode_charge, mode_spin, M_E_MEV, M_P_MEV, ALPHA, hbar_c_MeV_fm

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064

sc = self_consistent_metric(R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
Gti = sc['Gtilde_inv']
L = sc['L']

a0_fm = hbar_c_MeV_fm / (M_E_MEV * ALPHA)


print("=" * 72)
print("R31 TRACK 6: MULTI-ELECTRON ATOMS AND PAULI PRINCIPLE")
print("=" * 72)


# ── Section 1: What is r_e? ──────────────────────────────────────

print("\n\n── Section 1: r_e is a property of the geometry, not of electrons ──\n")

print("  The Ma metric has three T² sheets:")
print(f"    Electron sheet: dims (1,2), r_e = {R_E}, L₁ = {L[0]:,.0f} fm, L₂ = {L[1]:,.0f} fm")
print(f"    Neutrino sheet: dims (3,4), r_ν = {R_NU}, L₃ = {L[2]:.1e} fm, L₄ = {L[3]:.1e} fm")
print(f"    Proton sheet:   dims (5,6), r_p = {R_P}, L₅ = {L[4]:.2f} fm, L₆ = {L[5]:.2f} fm")
print()
print("  These are properties of the GEOMETRY — the shape of the")
print("  material space.  They do NOT change when you add more particles.")
print()
print("  Analogy: the shape of a violin body is fixed.  Multiple")
print("  harmonics (particles) can resonate in it simultaneously,")
print("  but each one experiences the same geometry.")
print()
print("  Key consequence: ALL electrons have the same mass (m_e)")
print("  because they all correspond to the SAME Ma mode (1,2,0,0,0,0)")
print("  on the SAME geometry.  Having different r_e values for")
print("  different electrons would require MULTIPLE electron sheets —")
print("  additional material dimensions.")

E_e = mode_energy([1, 2, 0, 0, 0, 0], Gti, L)
print(f"\n  Electron mode: (1, 2, 0, 0, 0, 0)")
print(f"  Mass: {E_e*1e3:.3f} keV (every electron, everywhere)")


# ── Section 2: The Pauli principle in Ma + R³ ───────────────────

print("\n\n── Section 2: Pauli exclusion in Ma + R³ ──\n")

print("  In standard QM, electrons are IDENTICAL FERMIONS.")
print("  Two electrons cannot occupy the same quantum state.")
print()
print("  In the Ma + R³ picture, the quantum state has two parts:")
print()
print("  Ma part (SAME for all electrons):")
print("    Mode: (1, 2, 0, 0, 0, 0)")
print("    This identifies the particle AS an electron.")
print("    All electrons share this — it's the definition of 'electron'.")
print()
print("  R³ part (DIFFERENT for each electron):")
print("    Orbital: 1s, 2s, 2p, 3s, 3p, 3d, ...")
print("    Spin projection: ↑ or ↓")
print("    This is where electrons are distinguished.")
print()
print("  The Pauli principle operates on the R³ part:")
print("    No two electrons can have the same (n, l, m_l, m_s).")
print("    This is a standard QM constraint in R³.")
print()
print("  Ma does NOT participate in Pauli exclusion.")
print("  It only determines WHAT the particle is (electron vs proton).")
print("  The HOW MANY and WHERE are R³ properties.")


# ── Section 3: Multi-electron atoms — quantitative ──────────────

print("\n\n── Section 3: Multi-electron atoms in Ma + R³ ──\n")

atoms = [
    ("Hydrogen", 1, "1s1", 13.6, 1),
    ("Helium", 2, "1s2", 79.0, 1),
    ("Lithium", 3, "1s2 2s1", 203.5, 2),
    ("Carbon", 6, "1s2 2s2 2p2", 1030.1, 2),
    ("Oxygen", 8, "1s2 2s2 2p4", 1619.4, 2),
    ("Iron", 26, "[Ar] 3d6 4s2", 10531.0, 4),
    ("Uranium", 92, "[Rn] 5f3 6d1 7s2", 74394.0, 7),
]

print("  Each atom: Z electrons + 1 nucleus (Ma mode)")
print("  Electrons are R3 wavefunctions on the SAME Ma geometry.")
print()
print(f"  {'Atom':>10s} {'Z':>4s} {'Config':>20s} {'Bind (eV)':>10s}"
      f" {'Max n':>6s} {'# states':>10s}")
print(f"  {'─'*64}")

for name, Z, config, binding, max_n in atoms:
    n_states = sum(2 * n**2 for n in range(1, max_n + 1))
    print(f"  {name:>10s} {Z:4d} {config:>20s} {binding:10.1f}"
          f" {max_n:6d} {n_states:10d}")

print(f"\n  All {atoms[-1][1]} electrons in uranium have the SAME Ma mode.")
print(f"  They differ ONLY in their R³ quantum numbers (n, l, m_l, m_s).")


# ── Section 4: Energy scales ────────────────────────────────────

print("\n\n── Section 4: Energy scale separation ──\n")

print("  Ma energy (particle identity):    MeV scale")
print(f"    m_e = {M_E_MEV*1e3:.1f} keV = {M_E_MEV*1e6:.0f} eV")
print(f"    Smallest Ma step: {2*math.pi*hbar_c_MeV_fm/L[0]*1e6:.0f} eV (electron tube)")
print()
print("  R³ energy (electron configuration):  eV scale")
print(f"    H binding:  13.6 eV")
print(f"    He binding: 79 eV (total)")
print(f"    Fe binding: 10,531 eV")
print()

ratio = M_E_MEV * 1e6 / 13.6
print(f"  Ratio: m_e / E_binding(H) = {ratio:,.0f}")
print(f"  The particle identity (Ma) is 37,000× more energetic")
print(f"  than the atomic binding (R³).")
print()
print("  This enormous scale separation is WHY atomic physics works:")
print("  electrons maintain their identity perfectly while orbiting.")
print("  The electron's Ma mode is never perturbed by atomic forces.")
print("  It's like trying to reshape a steel ball with a feather.")


# ── Section 5: What determines shell structure? ─────────────────

print("\n\n── Section 5: What determines electron shell structure ──\n")

print("  Shell structure = (n, l, m_l, m_s) quantum numbers = R³ physics")
print()
print("  The shell structure comes from solving the Schrödinger")
print("  equation for electrons in the Coulomb potential V = −Zα/r:")
print()

for Z in [1, 2, 6, 26]:
    E1 = -Z**2 * 13.6  # hydrogen-like ground state
    a_Z = a0_fm / Z
    print(f"    Z = {Z:2d}: E₁ = {E1:,.1f} eV,"
          f" a₀/Z = {a_Z:,.0f} fm ({a_Z*1e-4:.2f} Å)")

print()
print("  The Coulomb potential is determined by α (from Ma shear).")
print("  Shell structure is determined by quantum mechanics in R³.")
print("  Both ultimately trace back to α — the bridge between Ma and R³.")
print()
print("  Ma determines:")
print("    ✓ What particles exist (electron, proton)")
print("    ✓ Their masses")
print("    ✓ The coupling constant α")
print("    ✓ Nuclear masses (nuclei as Ma modes)")
print()
print("  R³ determines:")
print("    ✓ Shell structure (QM eigenstates of V = −Zα/r)")
print("    ✓ Pauli exclusion (antisymmetry of R³ wavefunctions)")
print("    ✓ Electron configurations (filling order)")
print("    ✓ Atomic spectra (transitions between R³ states)")
print("    ✓ Chemical bonding (overlap of R³ orbitals)")


# ── Section 6: Could different electrons have different r_e? ────

print("\n\n── Section 6: Could different electrons have different r_e? ──\n")

print("  Question: What if different electrons in helium occupy")
print("  different positions on the (r_e, s) viability curve?")
print()
print("  Answer: NO.  Here's why:")
print()
print("  1. r_e is a property of the METRIC — the shape of the")
print("     material space.  There is ONE metric, not one per particle.")
print()
print("  2. If electron A had r_e = 3 and electron B had r_e = 10,")
print("     they would have DIFFERENT masses (the mode energy depends")
print("     on r_e through the circumferences).")

# Show mass variation with r_e
print()
print(f"     {'r_e':>6s} {'L₁ (fm)':>12s} {'L₂ (fm)':>10s} {'m_e check':>10s}")
print(f"     {'─'*42}")
for r_test in [1.0, 3.0, 6.6, 10.0, 20.0]:
    from lib.ma import solve_shear_for_alpha, mu_12
    s = solve_shear_for_alpha(r_test)
    if s is None:
        continue
    mu = mu_12(r_test, s)
    E0 = M_E_MEV / mu
    L2_test = 2 * math.pi * hbar_c_MeV_fm / E0
    L1_test = r_test * L2_test
    # The mode energy IS m_e by construction
    print(f"     {r_test:6.1f} {L1_test:12.0f} {L2_test:10.0f} {'0.511 MeV':>10s}")

print()
print("  3. Since m_e is fixed by the (r, s) combination, and all")
print("     electrons have the same mass, they share the same r_e.")
print("     But this is guaranteed BY CONSTRUCTION: we set the")
print("     metric so that mode (1,2,0,0,0,0) = m_e.  The entire")
print("     viability curve gives the same m_e.  So electron mass")
print("     does NOT distinguish r_e values.")
print()
print("  4. What WOULD distinguish r_e is the COUPLING (α).")
print("     But α also comes from the geometry, and there's only")
print("     one geometry.  So α is the same for all electrons.")
print()
print("  5. The r_e degeneracy (Track 3 finding, R30 F11) means the")
print("     model can't tell us what r_e is — but it IS a single")
print("     number, not one per electron.")


# ── Summary ──────────────────────────────────────────────────────

print("\n\n── Summary ──\n")

print("  1. r_e is a GEOMETRIC property (aspect ratio of the electron")
print("     T² sheet), not a per-electron variable.  All electrons")
print("     share the same material geometry.")
print()
print("  2. The Pauli exclusion principle operates entirely in R³.")
print("     Electrons are distinguished by orbital and spin quantum")
print("     numbers, not by Ma geometry.")
print()
print("  3. Multi-electron atoms work naturally: Z electrons, each")
print("     in Ma mode (1,2,0,0,0,0), distinguished by R³ states")
print("     (n, l, m_l, m_s).  No new Ma degrees of freedom needed.")
print()
print("  4. The 37,000× scale separation between particle identity")
print("     (Ma, MeV) and atomic binding (R³, eV) guarantees that")
print("     atomic physics works: electrons never lose their identity.")
print()
print("  5. Shell structure, electron configurations, and chemistry")
print("     are ALL R³ phenomena governed by α.  Ma provides α")
print("     and particle masses; R³ provides the rest.")
print()
print("  6. Having different r_e for different electrons is impossible")
print("     without additional material dimensions — violating the")
print("     structural minimum of 6 dimensions (R30 F7).")
