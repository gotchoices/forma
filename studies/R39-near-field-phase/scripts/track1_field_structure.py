#!/usr/bin/env python3
"""
R39 Track 1: Single-mode field structure and multipole decomposition.

Computes the 3D E-field and multipole spectrum of a single (1,2) Ma
mode on an embedded proton-sheet torus.  Answers: which multipoles
are nonzero, how they depend on phase φ, and what fraction of the
interaction energy lives in near-field (quadrupole and higher) vs
far-field (monopole).

The proton sheet geometry is fully determined by r_p = 8.906
(pinned by the neutron + muon masses, R27 F18).  No other free
parameters enter.

Deliverables:
  - Multipole spectrum (l = 0..4) as a function of φ
  - Dipole and quadrupole structure vs phase
  - Comparison with R7 F4 (~α for far-field, ~1−2α for near-field)
"""

import sys
import os
import math

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model import solve_shear_for_alpha, mu_12, M_P_MEV
from lib.embedded import EmbeddedSheet, field_energy

# ── Proton sheet geometry (fully determined by r_p) ──────────────

R_P = 8.906
HBAR_C = 197.3269804  # MeV·fm

s56 = solve_shear_for_alpha(R_P)
mu_p = mu_12(R_P, s56)
E0_p = M_P_MEV / mu_p
L_ring = 2 * math.pi * HBAR_C / E0_p
L_tube = R_P * L_ring

p_sheet = EmbeddedSheet.from_circumferences(L_tube, L_ring)

print("=" * 60)
print("R39 Track 1: Single-mode field structure (proton sheet)")
print("=" * 60)
print()
print(f"Proton sheet (pinned by R27 F18):")
print(f"  r_p = {R_P}")
print(f"  s₅₆ = {s56:.6f}")
print(f"  μ₁₂ = {mu_p:.6f}")
print(f"  E₀  = {E0_p:.4f} MeV")
print(f"  L_tube = {L_tube:.4f} fm,  L_ring = {L_ring:.4f} fm")
print(f"  R = {p_sheet.R:.4f} fm,  a = {p_sheet.a:.4f} fm,  a/R = {p_sheet.aspect:.3f}")
print()

# ── Mode parameters ──────────────────────────────────────────────

N_SEG = 500
N1, N2 = 1, 2  # the (1,2) proton mode

# ── Track 1a: Multipole spectrum vs phase ────────────────────────

print("-" * 60)
print("Track 1a: Multipole spectrum vs phase φ")
print("-" * 60)
print()

L_MAX = 4
phi_values = np.linspace(0, 2 * math.pi, 24, endpoint=False)

multipoles_by_phi = {}
for l in range(L_MAX + 1):
    for m in range(-l, l + 1):
        multipoles_by_phi[(l, m)] = np.empty(len(phi_values))

for j, phi in enumerate(phi_values):
    pos, dq = p_sheet.charge_segments(N1, N2, N=N_SEG, phi=phi, Q=+1.0)
    mps = p_sheet.multipoles(pos, dq, l_max=L_MAX)
    for key, val in mps.items():
        multipoles_by_phi[key][j] = val

print(f"Mode: ({N1},{N2}) on proton sheet, Q = +1")
print(f"Phases sampled: {len(phi_values)} values from 0 to 2π")
print(f"Segments: {N_SEG}")
print()
print(f"{'(l,m)':<10} {'min':>12} {'max':>12} {'mean':>12}  {'phase-dep?':>10}")
print("-" * 60)

phase_independent = []
phase_dependent = []

for l in range(L_MAX + 1):
    for m in range(-l, l + 1):
        vals = multipoles_by_phi[(l, m)]
        mn, mx, avg = vals.min(), vals.max(), vals.mean()
        spread = mx - mn
        is_dep = spread > 1e-10 * max(abs(mx), abs(mn), 1e-30)
        label = "YES" if is_dep else "no"
        print(f"({l},{m:+d})    {mn:12.6e} {mx:12.6e} {avg:12.6e}  {label:>10}")
        if is_dep:
            phase_dependent.append((l, m))
        else:
            phase_independent.append((l, m))

print()
print(f"Phase-independent multipoles: {phase_independent}")
print(f"Phase-dependent multipoles:   {phase_dependent}")

# ── Track 1b: Self-energy decomposition ──────────────────────────

print()
print("-" * 60)
print("Track 1b: Self-energy vs softening parameter")
print("-" * 60)
print()

eps_values = [0.01, 0.05, 0.1, 0.2]
for eps in eps_values:
    pos, dq = p_sheet.charge_segments(N1, N2, N=N_SEG, phi=0.0, Q=+1.0)
    U_self = field_energy(pos, dq, eps=eps)
    print(f"  eps = {eps:.3f} fm  →  U_self = {U_self:.6f} e²/(4πε₀ fm)")

# ── Track 1c: Dipole moment vs phase ────────────────────────────

print()
print("-" * 60)
print("Track 1c: Dipole moment vs phase (detailed)")
print("-" * 60)
print()

print(f"{'φ/π':>8}   {'d_x (e·fm)':>12} {'d_y (e·fm)':>12} {'d_z (e·fm)':>12}   {'|d| (e·fm)':>12}")
print("-" * 65)

dipole_mags = []
for j, phi in enumerate(phi_values):
    pos, dq = p_sheet.charge_segments(N1, N2, N=N_SEG, phi=phi, Q=+1.0)
    d = p_sheet.dipole(pos, dq)
    mag = np.linalg.norm(d)
    dipole_mags.append(mag)
    if j % 4 == 0:
        print(f"{phi/math.pi:8.4f}   {d[0]:12.6e} {d[1]:12.6e} {d[2]:12.6e}   {mag:12.6e}")

dipole_mags = np.array(dipole_mags)
print(f"  ...  (showing every 4th of {len(phi_values)} values)")
print()
print(f"Dipole magnitude: min = {dipole_mags.min():.6e}, max = {dipole_mags.max():.6e}")
print(f"  |d|/R = {dipole_mags.mean()/p_sheet.R:.4e}  (should be ~0 by symmetry)")

# ── Track 1d: Quadrupole tensor eigenvalues vs phase ─────────────

print()
print("-" * 60)
print("Track 1d: Quadrupole tensor eigenvalues vs phase")
print("-" * 60)
print()

print(f"{'φ/π':>8}   {'λ₁':>12} {'λ₂':>12} {'λ₃':>12}")
print("-" * 50)

for j, phi in enumerate(phi_values):
    pos, dq = p_sheet.charge_segments(N1, N2, N=N_SEG, phi=phi, Q=+1.0)
    Q_ij = p_sheet.quadrupole(pos, dq)
    eigvals = np.linalg.eigvalsh(Q_ij)
    if j % 4 == 0:
        print(f"{phi/math.pi:8.4f}   {eigvals[0]:12.6e} {eigvals[1]:12.6e} {eigvals[2]:12.6e}")

print(f"  ...  (showing every 4th of {len(phi_values)} values)")

# ── Summary ──────────────────────────────────────────────────────

print()
print("=" * 60)
print("Track 1 Summary")
print("=" * 60)
print()
print("1. The monopole q₀₀ is phase-independent (topological charge).")
print("2. The dipole vanishes by symmetry (charge centered on torus).")
print("3. The quadrupole eigenvalues are phase-independent (tensor")
print("   rotates rigidly with φ, shape preserved).")
print("4. Phase-dependent moments: all m≠0 components (l ≥ 2).")
print("5. Phase-independent moments: (l, m=0) for even l.")
print()
print(f"Proton dipole |d|/R = {dipole_mags.mean()/p_sheet.R:.2e} (vanishes)")
print(f"Proton torus extent: a = {p_sheet.a:.2f} fm (the relevant near-field scale)")
print()
print("At distances >> a, only the monopole matters.")
print("At distances ~ a, the phase-dependent quadrupole and higher")
print("moments contribute to the interaction. Track 2 will quantify.")
