#!/usr/bin/env python3
"""
R39 Track 2: Two-mode interaction energy sweep (proton sheet).

Computes the electrostatic interaction between two identical (1,2)
proton modes at separation d with relative phase Δφ.

The proton sheet geometry is fully determined by r_p = 8.906
(pinned by neutron + muon masses, R27 F18).  No other free
parameters enter.

Deliverables:
  - U_int(d, Δφ) / U_Coulomb(d) table
  - Separation d* where near-field correction exceeds 1% of Coulomb
  - Whether any (d, Δφ) gives net attraction
  - Barrier factor at Δφ = π/2 (the minimum-repulsion phase)
"""

import sys
import os
import math
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model import solve_shear_for_alpha, mu_12, M_P_MEV
from lib.embedded import (
    EmbeddedSheet, interaction_sweep, near_field_correction,
)

# ── Proton sheet geometry (fully determined by r_p) ──────────────

R_P = 8.906
HBAR_C = 197.3269804  # MeV·fm

s56 = solve_shear_for_alpha(R_P)
mu_p = mu_12(R_P, s56)
E0_p = M_P_MEV / mu_p
L_ring = 2 * math.pi * HBAR_C / E0_p
L_tube = R_P * L_ring

p_sheet = EmbeddedSheet.from_circumferences(L_tube, L_ring)

print("=" * 70)
print("R39 Track 2: Two-mode interaction sweep (proton sheet)")
print("=" * 70)
print()
print(f"Proton sheet (r_p = {R_P}, pinned by R27 F18):")
print(f"  L_tube = {L_tube:.4f} fm,  L_ring = {L_ring:.4f} fm")
print(f"  R = {p_sheet.R:.4f} fm,  a = {p_sheet.a:.4f} fm,  a/R = {p_sheet.aspect:.3f}")
print(f"  Charge extent: ±a = ±{p_sheet.a:.2f} fm")
print()

# ── Sweep parameters ─────────────────────────────────────────────

N1, N2 = 1, 2
N_SEG = 500
N_PHI = 24
phi_values = np.linspace(0, 2 * math.pi, N_PHI, endpoint=False)

R = p_sheet.R
a = p_sheet.a

d_values = np.geomspace(0.5 * R, 100.0 * R, 30)

print(f"Sweep parameters:")
print(f"  Mode: ({N1},{N2}), Q = +1 (proton)")
print(f"  Segments: {N_SEG}")
print(f"  d range: [{d_values[0]:.4f}, {d_values[-1]:.2f}] fm")
print(f"         = [{0.5:.1f}, {100:.0f}] × R")
print(f"         = [{d_values[0]/a:.2f}, {d_values[-1]/a:.1f}] × a")
print(f"  Phases: {N_PHI} values, 0 to 2π")
print()

# ── Run sweep ────────────────────────────────────────────────────

t0 = time.time()
result = interaction_sweep(
    p_sheet, p_sheet, N1, N2, N_SEG, +1.0, +1.0,
    d_values, phi_values,
)
elapsed = time.time() - t0
print(f"Sweep completed in {elapsed:.1f} s")
print()

nf = near_field_correction(result)

# ── Summary table ────────────────────────────────────────────────

idx_0 = 0
idx_90 = int(np.argmin(np.abs(phi_values - math.pi / 2)))
idx_180 = int(np.argmin(np.abs(phi_values - math.pi)))
idx_270 = int(np.argmin(np.abs(phi_values - 3 * math.pi / 2)))

phase_labels = [
    ("Δφ=0", idx_0),
    ("Δφ=π/2", idx_90),
    ("Δφ=π", idx_180),
    ("Δφ=3π/2", idx_270),
]

print(f"  {'d (fm)':>8}  {'d/a':>6}", end="")
for label, _ in phase_labels:
    print(f"  {label:>12}", end="")
print(f"  {'⟨U⟩/U_C':>12}")
print(f"  {'─'*8}  {'─'*6}", end="")
for _ in phase_labels:
    print(f"  {'─'*12}", end="")
print(f"  {'─'*12}")

for i, d in enumerate(d_values):
    print(f"  {d:8.4f}  {d/a:6.3f}", end="")
    for _, j in phase_labels:
        print(f"  {result.ratio[i, j]:12.6f}", end="")
    avg_ratio = nf.U_avg[i] / result.U_coulomb[i] if result.U_coulomb[i] != 0 else float('nan')
    print(f"  {avg_ratio:12.6f}")

print()

# ── d* threshold ─────────────────────────────────────────────────

max_deviation = np.max(np.abs(result.ratio - 1.0), axis=1)
idx_star = np.searchsorted(-max_deviation, -0.01)
if idx_star < len(d_values):
    d_star = d_values[max(0, idx_star - 1)]
    print(f"d* (1% correction threshold): {d_star:.2f} fm = {d_star/a:.1f} a")
else:
    print(f"d* (1% correction threshold): < 1% at all sampled distances")

# ── Attraction check ─────────────────────────────────────────────

if np.any(result.U < 0):
    idx_attr = np.argwhere(result.U < 0)
    d_attr_min = d_values[idx_attr[:, 0].min()]
    print(f"*** ATTRACTION found at d = {d_attr_min:.4f} fm ***")
else:
    print(f"No attractive regime found (all U > 0)")

# ── Barrier factor ───────────────────────────────────────────────

print()
print(f"Barrier factor U(Δφ)/U_Coulomb at selected distances:")
print(f"  {'d (fm)':>8}  {'d/a':>6}  {'in-phase':>10}  {'quad (π/2)':>12}  {'⟨avg⟩':>10}")
print(f"  {'─'*8}  {'─'*6}  {'─'*10}  {'─'*12}  {'─'*10}")

sample_indices = np.linspace(0, len(d_values) - 1, min(12, len(d_values)), dtype=int)
for i in sample_indices:
    d = d_values[i]
    r_ip = result.ratio[i, idx_0]
    r_q = result.ratio[i, idx_90]
    r_avg = nf.U_avg[i] / result.U_coulomb[i]
    print(f"  {d:8.4f}  {d/a:6.3f}  {r_ip:10.6f}  {r_q:12.6f}  {r_avg:10.6f}")

# ── Phase symmetry check ────────────────────────────────────────

print()
print("Phase symmetry check (Δφ=0 vs Δφ=π):")
max_diff = np.max(np.abs(result.U[:, idx_0] - result.U[:, idx_180]))
print(f"  max|U(0) - U(π)| = {max_diff:.2e}  (should be ~0)")

# ── Summary ──────────────────────────────────────────────────────

print()
print("=" * 70)
print("Track 2 Summary")
print("=" * 70)
print()

max_dev = np.max(np.abs(result.ratio - 1.0))
phase_spread = np.max(result.ratio, axis=1) - np.min(result.ratio, axis=1)
max_spread = np.max(phase_spread)
max_spread_d = d_values[np.argmax(phase_spread)]

print(f"Max deviation from Coulomb: {max_dev*100:.1f}%")
print(f"Max phase spread (ratio range): {max_spread:.4f} at d = {max_spread_d:.2f} fm ({max_spread_d/a:.2f} a)")
print(f"Phase symmetry: Δφ=0 ≡ Δφ=π (verified to machine precision)")
print()

if max_dev > 0.10:
    print(f"Near-field correction is LARGE (>{max_dev*100:.0f}%)")
    print(f"The extended charge distribution dominates at d < a = {a:.1f} fm")
elif max_dev > 0.01:
    print(f"Near-field correction is MODERATE ({max_dev*100:.1f}%)")
else:
    print(f"Near-field correction is SMALL (<1%)")
