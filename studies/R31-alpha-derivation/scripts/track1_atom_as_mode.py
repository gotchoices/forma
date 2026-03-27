#!/usr/bin/env python3
"""
R31 Track 1: Is the hydrogen atom a Ma mode?

Hydrogen: m_p + m_e - 13.6 eV = 938.783 MeV, Q = 0, spin = ½.
Search for Ma modes near this mass.  The proton-sheet energy
ladder has ~53 MeV spacing — if no mode lands within ~1 eV of
938.783 MeV, atomic binding CANNOT be a Ma phenomenon.
"""

import sys, os, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_solver import self_consistent_metric
from lib.ma import mode_energy, mode_charge, mode_spin, M_P_MEV, M_E_MEV

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064

sc = self_consistent_metric(R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
Gti = sc['Gtilde_inv']
L = sc['L']

M_HYDROGEN = M_P_MEV + M_E_MEV - 13.6e-6  # 938.783 MeV
BINDING_EV = 13.6  # eV

print("=" * 72)
print("R31 TRACK 1: IS THE HYDROGEN ATOM A Ma MODE?")
print("=" * 72)


# ── Section 1: Energy scale comparison ───────────────────────────

print("\n\n── Section 1: Energy scale comparison ──\n")

E0_proton_tube = 2 * math.pi * 197.3269804 / L[4]
E0_proton_ring = 2 * math.pi * 197.3269804 / L[5]
E0_electron_tube = 2 * math.pi * 197.3269804 / L[0]
E0_electron_ring = 2 * math.pi * 197.3269804 / L[1]

print(f"  Energy scales of Ma dimensions:")
print(f"    Proton tube (L₅ = {L[4]:.2f} fm):    {E0_proton_tube:.1f} MeV per step")
print(f"    Proton ring (L₆ = {L[5]:.2f} fm):    {E0_proton_ring:.1f} MeV per step")
print(f"    Electron tube (L₁ = {L[0]:.1f} fm):  {E0_electron_tube:.4f} MeV per step")
print(f"    Electron ring (L₂ = {L[1]:.1f} fm):  {E0_electron_ring:.4f} MeV per step")
print()
print(f"  Hydrogen binding energy:  {BINDING_EV} eV = {BINDING_EV*1e-6:.9f} MeV")
print(f"  Smallest Ma step:        {E0_electron_tube*1e6:.0f} eV (electron tube)")
print(f"  Ratio:  {E0_electron_tube / (BINDING_EV * 1e-6):.0f}× coarser")
print()
print(f"  The FINEST energy resolution available in Ma is the electron tube")
print(f"  at {E0_electron_tube*1e6:.0f} eV.  The hydrogen binding energy (13.6 eV)")
print(f"  is {E0_electron_tube / (BINDING_EV * 1e-6):.0f}× smaller than this.")
print(f"  No Ma mode can match hydrogen's mass to eV precision.")


# ── Section 2: Search for modes near hydrogen mass ───────────────

print("\n\n── Section 2: Modes near hydrogen mass (938.783 MeV) ──\n")

target = M_HYDROGEN
window = 5.0  # MeV search window

print(f"  Target: {target:.6f} MeV")
print(f"  Window: ±{window} MeV")
print(f"  Charge: Q = 0, Spin: ½")
print()

N_MAX = 8
matches = []

for n1 in range(-N_MAX, N_MAX + 1):
    for n5 in range(-N_MAX, N_MAX + 1):
        if -n1 + n5 != 0:
            continue
        n1_odd = abs(n1) % 2
        n5_odd = abs(n5) % 2
        for n3 in [0, 1]:
            spin_count = n1_odd + n5_odd + (abs(n3) % 2)
            if spin_count != 1:
                continue
            for n2 in range(-N_MAX, N_MAX + 1):
                for n6 in range(-N_MAX, N_MAX + 1):
                    n = np.array([n1, n2, n3, 0, n5, n6], dtype=float)
                    E = mode_energy(n, Gti, L)
                    if abs(E - target) < window:
                        gap = E - target
                        matches.append({
                            'n': tuple(int(x) for x in n),
                            'E': E, 'gap_MeV': gap,
                            'gap_eV': gap * 1e6,
                        })

matches.sort(key=lambda m: abs(m['gap_MeV']))

print(f"  Found {len(matches)} modes within ±{window} MeV (Q=0, spin=½):\n")

if matches:
    print(f"    {'Mode':>24s} {'E (MeV)':>12s} {'Gap (MeV)':>10s} {'Gap (eV)':>12s}")
    print(f"    {'─'*62}")
    for m in matches[:20]:
        print(f"    {str(m['n']):>24s} {m['E']:12.4f} {m['gap_MeV']:+10.4f}"
              f" {m['gap_eV']:+12.0f}")

    closest = matches[0]
    print(f"\n  Closest mode: gap = {closest['gap_eV']:+.0f} eV")
    print(f"  Hydrogen binding: −13.6 eV")
    print(f"  The closest Ma mode is {abs(closest['gap_eV'])/BINDING_EV:.0f}× "
          f"farther from the hydrogen mass")
    print(f"  than the binding energy itself.")
else:
    print(f"  No modes found!")


# ── Section 3: What about the proton mode + small corrections? ──

print("\n\n── Section 3: Proton mode + electron corrections ──\n")

E_proton = mode_energy([0, 0, 0, 0, 1, 2], Gti, L)
print(f"  Proton mode energy: {E_proton:.6f} MeV")
print(f"  Hydrogen mass:      {target:.6f} MeV")
print(f"  Difference:         {(target - E_proton)*1e6:.0f} eV")
print()

print("  Could we ADD electron energy to a proton mode?")
print(f"  m_e = {M_E_MEV*1e6:.0f} eV — adding electron mass to proton")
print(f"  gives {(E_proton + M_E_MEV):.6f} MeV = {(E_proton + M_E_MEV)*1e6:.0f} eV above hydrogen mass")
print(f"  The electron adds 511,000 eV but binding removes only 13.6 eV.")
print()
print("  In Ma mode language, including electron windings (n₁, n₂ ≠ 0)")
print("  adds AT MINIMUM {:.0f} eV (electron tube step).".format(E0_electron_tube*1e6))
print("  This is {:.0f}× the binding energy.".format(E0_electron_tube*1e6/BINDING_EV))
print()
print("  There is no combination of quantum numbers that can produce")
print("  a 13.6 eV energy shift.  The Ma mode spectrum is quantized")
print("  in steps thousands of times larger than the binding energy.")


# ── Section 4: Mode density near proton mass ─────────────────────

print("\n\n── Section 4: Mode density near proton mass ──\n")

all_modes = []
for n5 in range(-4, 5):
    for n6 in range(-4, 5):
        for n1 in range(-2, 3):
            for n3 in [0, 1]:
                n = np.array([n1, 0, n3, 0, n5, n6], dtype=float)
                E = mode_energy(n, Gti, L)
                if 900 < E < 980:
                    Q = mode_charge(n)
                    S = mode_spin(n)
                    all_modes.append((E, Q, S, tuple(int(x) for x in n)))

all_modes.sort()

# Find gaps between successive modes
energies = sorted(set(round(E, 2) for E, _, _, _ in all_modes))
if len(energies) > 1:
    gaps = [energies[i+1] - energies[i] for i in range(len(energies)-1)]
    print(f"  Distinct energy levels near proton mass (900–980 MeV): {len(energies)}")
    print(f"  Average spacing: {np.mean(gaps):.1f} MeV")
    print(f"  Minimum spacing: {min(gaps):.3f} MeV = {min(gaps)*1e6:.0f} eV")
    print(f"  Maximum spacing: {max(gaps):.1f} MeV")
    print()

    closest_spacing = min(gaps)
    print(f"  Even the CLOSEST pair of modes is {closest_spacing*1e6:.0f} eV apart.")
    print(f"  Hydrogen binding = 13.6 eV.")
    print(f"  The mode spectrum cannot resolve atomic energy scales.")
else:
    print(f"  Only {len(energies)} distinct energies found — need wider search.")


# ── Summary ──────────────────────────────────────────────────────

print("\n\n── Summary ──\n")

print("  1. The Ma energy spectrum has no structure at the eV scale.")
print("     The finest step (electron tube) is ~39,000 eV — 2,900×")
print("     coarser than the 13.6 eV hydrogen binding energy.")
print()
print("  2. The closest Ma mode to the hydrogen mass is thousands")
print("     of eV away.  No mode can match to eV precision.")
print()
print("  3. CONCLUSION: The hydrogen atom is NOT a Ma mode.")
print("     Atomic binding is irreducibly an R³ phenomenon.")
print()
print("  4. This confirms the two-tier picture (R29 F26):")
print("       Ma → particles and nuclei (MeV scale)")
print("       R³ → atoms and chemistry (eV scale)")
print()
print("  5. To understand atoms, we MUST understand the R³")
print("     interaction — which means understanding α.")
print("     This is why deriving α is essential.")
