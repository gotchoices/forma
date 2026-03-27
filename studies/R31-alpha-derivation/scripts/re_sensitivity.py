#!/usr/bin/env python3
"""
Quick analysis: which known particles are sensitive to L₁ (electron tube)?
If none are, r_e is structurally unconstrained.
"""

import sys, os, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.t6_solver import self_consistent_metric
from lib.t6 import mode_energy, hbar_c_MeV_fm

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064

sc = self_consistent_metric(R_E, R_NU, R_P, sigma_ep=SIGMA_EP)
Gti = sc['Gtilde_inv']
L = sc['L']

TWO_PI_HC = 2 * math.pi * hbar_c_MeV_fm

print("Electron tube sensitivity analysis")
print("=" * 60)
print(f"\nL₁ (electron tube) = {L[0]:,.0f} fm")
print(f"L₂ (electron ring) = {L[1]:,.0f} fm")
print(f"L₅ (proton tube)   = {L[4]:.2f} fm")
print(f"L₆ (proton ring)   = {L[5]:.2f} fm")
print(f"\nEnergy per step:")
print(f"  n₁ step: {TWO_PI_HC/L[0]*1e6:.0f} eV")
print(f"  n₂ step: {TWO_PI_HC/L[1]*1e6:.0f} eV")
print(f"  n₅ step: {TWO_PI_HC/L[4]*1e6:.0f} eV")
print(f"  n₆ step: {TWO_PI_HC/L[5]*1e6:.0f} eV")

particles = [
    ("electron", [1, 2, 0, 0, 0, 0], 0.511),
    ("muon", [-1, 5, 0, 0, -2, 0], 105.658),
    ("tau", [-1, 8, 0, 0, -2, -4], 1776.9),
    ("neutron", [0, -2, 1, 0, 0, 2], 939.565),
    ("proton", [0, 0, 0, 0, 1, 2], 938.272),
    ("pion+", [2, -8, 1, 0, 3, 0], 139.570),
    ("kaon+", [1, -5, 1, 0, 2, 2], 493.7),
]

print(f"\n{'Particle':>10s} {'n₁':>4s} {'E_total':>10s}"
      f" {'E_tube frac':>12s} {'n₁ contrib':>12s}")
print(f"{'─'*52}")

for name, mode, m_obs in particles:
    E = mode_energy(mode, Gti, L)
    n1 = mode[0]
    if n1 != 0:
        # Energy contribution from electron tube alone
        mode_no_tube = list(mode)
        mode_no_tube[0] = 0
        E_no_tube = mode_energy(mode_no_tube, Gti, L)
        tube_contrib = E - E_no_tube
        frac = abs(tube_contrib) / E * 100
        print(f"  {name:>10s} {n1:4d} {E:10.3f} MeV"
              f" {frac:10.4f}% {tube_contrib*1e3:+10.1f} keV")
    else:
        print(f"  {name:>10s} {n1:4d} {E:10.3f} MeV"
              f" {'0':>12s} {'0':>12s}")

print(f"\n\nSweeping r_e: how does each particle mass change?")
print(f"{'─'*70}")

for r_e_test in [1.0, 3.0, 6.6, 10.0, 20.0, 50.0]:
    sc2 = self_consistent_metric(r_e_test, R_NU, R_P, sigma_ep=SIGMA_EP)
    Gti2 = sc2['Gtilde_inv']
    L2 = sc2['L']

    print(f"\n  r_e = {r_e_test}:  L₁ = {L2[0]:,.0f} fm, L₂ = {L2[1]:,.0f} fm")
    for name, mode, m_obs in particles:
        E = mode_energy(mode, Gti2, L2)
        diff = E - m_obs
        print(f"    {name:>10s}: {E:10.3f} MeV (Δ = {diff*1e3:+8.1f} keV)")
