#!/usr/bin/env python3
"""
R39 Track 5: Charge distribution model comparison.

Compares three models for how charge is distributed on the proton
torus, and their effect on the near-field interaction:

  Model A — Uniform line charge along the (1,2) geodesic
            (traveling wave / WvM model; what Tracks 1-4 used)

  Model B — Standing-wave modulated line charge along the geodesic
            (cos² modulation along the path → nodes & antinodes)

  Model C — Uniform charge on the full 2D torus surface
            (KK wave mechanics: |ψ|² = 1 everywhere)

The question: does the charge distribution model change whether
phase-dependent near-field effects exist?

NOTE: This is ELECTROSTATIC ONLY.  The circulating charge also
creates a magnetic field (current loop → magnetic dipole).  The
magnetic interaction is not computed here — see Track 6 (planned).
"""

import sys
import os
import math
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model import solve_shear_for_alpha, mu_12, M_P_MEV
from lib.embedded import (
    EmbeddedSheet, interaction_energy,
)

# ── Proton sheet geometry ────────────────────────────────────────

R_P = 8.906
HBAR_C = 197.3269804

s56 = solve_shear_for_alpha(R_P)
mu_p = mu_12(R_P, s56)
E0_p = M_P_MEV / mu_p
L_ring = 2 * math.pi * HBAR_C / E0_p
L_tube = R_P * L_ring

p_sheet = EmbeddedSheet.from_circumferences(L_tube, L_ring)

R = p_sheet.R
a = p_sheet.a

print("=" * 70)
print("R39 Track 5: Charge distribution model comparison")
print("=" * 70)
print()
print(f"Proton sheet: a = {a:.4f} fm, R = {R:.4f} fm, a/R = {p_sheet.aspect:.3f}")
print()

N1, N2 = 1, 2
N_SEG = 500
Q = 1.0


# ══════════════════════════════════════════════════════════════════
#  Model A: Uniform line charge on geodesic (traveling wave)
# ══════════════════════════════════════════════════════════════════

def model_a(phi):
    """Uniform charge along geodesic."""
    return p_sheet.charge_segments(N1, N2, N=N_SEG, phi=phi, Q=Q)


# ══════════════════════════════════════════════════════════════════
#  Model B: Standing-wave modulated line charge on geodesic
# ══════════════════════════════════════════════════════════════════

def model_b(phi):
    """
    cos² modulated charge along geodesic.

    The standing wave ψ = cos(n₁θ₁ + n₂θ₂) has |ψ|² = cos²(...)
    with nodes and antinodes.  The phase parameter shifts where
    the antinodes fall.
    """
    t = np.linspace(0, 2 * math.pi, N_SEG, endpoint=False)
    theta1 = N1 * t + phi
    theta2 = N2 * t
    # Standing wave: the "wave" has spatial frequency along the
    # geodesic parameter t.  For a (1,2) mode on a torus, the
    # wave completes gcd(1,2)=1 distinct cycle, but the combined
    # winding is n₁+n₂=3 oscillations in angle space.
    # Use the tube angle as the oscillation coordinate:
    weights = np.cos(theta1) ** 2
    # Avoid zero total weight (shouldn't happen for N large)
    weights = np.maximum(weights, 1e-15)
    pos = p_sheet.torus_point(theta1, theta2)
    dq = Q * weights / weights.sum()
    return pos, dq


# ══════════════════════════════════════════════════════════════════
#  Model C: Uniform surface charge on the 2D torus
# ══════════════════════════════════════════════════════════════════

def model_c_surface(N_theta1=50, N_theta2=50):
    """
    Uniform charge on the torus surface.

    |ψ|² = 1 everywhere → charge density ∝ surface area element.
    The Jacobian for a torus of revolution is (R + a cos θ₁) × a,
    so more charge sits on the outer equator (θ₁ = 0) than the
    inner part (θ₁ = π).

    This has NO phase parameter — the charge distribution is
    the same regardless of φ.
    """
    theta1 = np.linspace(0, 2 * math.pi, N_theta1, endpoint=False)
    theta2 = np.linspace(0, 2 * math.pi, N_theta2, endpoint=False)
    T1, T2 = np.meshgrid(theta1, theta2, indexing='ij')
    T1_flat = T1.ravel()
    T2_flat = T2.ravel()

    pos = p_sheet.torus_point(T1_flat, T2_flat)

    # Surface area element: dA = (R + a cos θ₁) × a × dθ₁ dθ₂
    dA = (R + a * np.cos(T1_flat)) * a
    dA = np.maximum(dA, 0.0)  # handle self-intersection (R + a cos θ₁ < 0)
    dq = Q * dA / dA.sum()

    return pos, dq


# ══════════════════════════════════════════════════════════════════
#  Comparison: interaction at nuclear distances
# ══════════════════════════════════════════════════════════════════

d_values = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0, 15.0, 30.0]
phi_values = [0.0, math.pi / 4, math.pi / 2, 3 * math.pi / 4]

print("─" * 70)
print("Model A: Uniform line charge on geodesic (traveling wave / WvM)")
print("─" * 70)
print()
print(f"  {'d (fm)':>8}  {'d/a':>6}", end="")
for phi in phi_values:
    print(f"  {'Δφ=%.2fπ' % (phi/math.pi):>12}", end="")
print(f"  {'spread':>10}")
print(f"  {'─'*8}  {'─'*6}", end="")
for _ in phi_values:
    print(f"  {'─'*12}", end="")
print(f"  {'─'*10}")

pos1_a, dq1_a = model_a(0.0)

for d in d_values:
    U_C = Q * Q / d
    ratios = []
    for phi in phi_values:
        pos2, dq2 = model_a(phi)
        pos2_shifted = pos2.copy()
        pos2_shifted[:, 2] += d
        U = interaction_energy(pos1_a, dq1_a, pos2_shifted, dq2)
        ratios.append(U / U_C)
    spread = max(ratios) - min(ratios)
    print(f"  {d:8.3f}  {d/a:6.2f}", end="")
    for r in ratios:
        print(f"  {r:12.6f}", end="")
    print(f"  {spread:10.4f}")

print()
print("─" * 70)
print("Model B: Standing-wave modulated (cos² weights)")
print("─" * 70)
print()
print(f"  {'d (fm)':>8}  {'d/a':>6}", end="")
for phi in phi_values:
    print(f"  {'Δφ=%.2fπ' % (phi/math.pi):>12}", end="")
print(f"  {'spread':>10}")
print(f"  {'─'*8}  {'─'*6}", end="")
for _ in phi_values:
    print(f"  {'─'*12}", end="")
print(f"  {'─'*10}")

pos1_b, dq1_b = model_b(0.0)

for d in d_values:
    U_C = Q * Q / d
    ratios = []
    for phi in phi_values:
        pos2, dq2 = model_b(phi)
        pos2_shifted = pos2.copy()
        pos2_shifted[:, 2] += d
        U = interaction_energy(pos1_b, dq1_b, pos2_shifted, dq2)
        ratios.append(U / U_C)
    spread = max(ratios) - min(ratios)
    print(f"  {d:8.3f}  {d/a:6.2f}", end="")
    for r in ratios:
        print(f"  {r:12.6f}", end="")
    print(f"  {spread:10.4f}")

print()
print("─" * 70)
print("Model C: Uniform 2D surface charge (KK wave mechanics)")
print("─" * 70)
print()

pos1_c, dq1_c = model_c_surface()
N_surface = len(dq1_c)
print(f"  Surface samples: {N_surface} ({int(math.sqrt(N_surface))}×{int(math.sqrt(N_surface))})")
print(f"  No phase parameter — charge is φ-independent")
print()

print(f"  {'d (fm)':>8}  {'d/a':>6}  {'U/U_C':>12}")
print(f"  {'─'*8}  {'─'*6}  {'─'*12}")

for d in d_values:
    U_C = Q * Q / d
    pos2_c = pos1_c.copy()
    pos2_c[:, 2] += d
    U = interaction_energy(pos1_c, dq1_c, pos2_c, dq1_c)
    print(f"  {d:8.3f}  {d/a:6.2f}  {U/U_C:12.6f}")

# ══════════════════════════════════════════════════════════════════
#  Summary comparison
# ══════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("Summary: Model comparison at nuclear distances")
print("=" * 70)
print()

print(f"  {'d (fm)':>8}  {'Model A avg':>12}  {'Model B avg':>12}  "
      f"{'Model C':>10}  {'B spread':>10}  {'A spread':>10}")
print(f"  {'─'*8}  {'─'*12}  {'─'*12}  {'─'*10}  {'─'*10}  {'─'*10}")

for d in d_values:
    U_C = Q * Q / d

    # Model A
    ratios_a = []
    for phi in phi_values:
        pos2, dq2 = model_a(phi)
        pos2_shifted = pos2.copy()
        pos2_shifted[:, 2] += d
        U = interaction_energy(pos1_a, dq1_a, pos2_shifted, dq2)
        ratios_a.append(U / U_C)

    # Model B
    ratios_b = []
    for phi in phi_values:
        pos2, dq2 = model_b(phi)
        pos2_shifted = pos2.copy()
        pos2_shifted[:, 2] += d
        U = interaction_energy(pos1_b, dq1_b, pos2_shifted, dq2)
        ratios_b.append(U / U_C)

    # Model C
    pos2_c = pos1_c.copy()
    pos2_c[:, 2] += d
    U_c = interaction_energy(pos1_c, dq1_c, pos2_c, dq1_c) / U_C

    avg_a = np.mean(ratios_a)
    avg_b = np.mean(ratios_b)
    spread_a = max(ratios_a) - min(ratios_a)
    spread_b = max(ratios_b) - min(ratios_b)

    print(f"  {d:8.3f}  {avg_a:12.6f}  {avg_b:12.6f}  "
          f"{U_c:10.6f}  {spread_b:10.4f}  {spread_a:10.4f}")

print()
print("Interpretation:")
print("  Model A: WvM traveling wave — uniform along geodesic")
print("  Model B: Standing wave — cos² modulated along geodesic")
print("           (stronger phase effects from charge concentration)")
print("  Model C: KK wave mechanics — uniform on 2D surface")
print("           (no phase parameter exists; purely geometric)")
print()
print("If Models A and C give similar ⟨U⟩/U_C, the near-field")
print("suppression is geometric (independent of charge model).")
print("If Model B shows larger phase spread, standing-wave")
print("structure enhances phase-dependent effects.")
print()
print("NOTE: All three models are ELECTROSTATIC ONLY.")
print("The circulating charge also produces a MAGNETIC field")
print("(current loop → N/S poles).  The magnetic dipole-dipole")
print("interaction is attractive for aligned poles and could")
print("create local minima that this calculation misses.")
