#!/usr/bin/env python3
"""
R40 Track 4: Per-mode self-consistent shapes and physical consequences.

Each particle (mode) shapes its own torus differently.  A (1,2) proton
creates a different equilibrium than a (1,4) ghost mode would.

This track:
  1. Finds the optimal shape for each (n₁, n₂) mode independently
  2. Compares the energy on the per-mode shape vs the circular shape
  3. Checks if some modes have NO valid equilibrium (unstable)
  4. Computes the effective mass spectrum on self-consistent shapes
  5. Assesses ghost suppression from the per-mode perspective
"""

import sys
import os
import math

import numpy as np
from scipy.optimize import minimize, brentq
from scipy import linalg

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model import solve_shear_for_alpha, mu_12, M_P_MEV

HBAR_C_FM = 197.3269804


# ══════════════════════════════════════════════════════════════════════
#  Geometry (from Track 1-2)
# ══════════════════════════════════════════════════════════════════════

R_P = 8.906
s56 = solve_shear_for_alpha(R_P)
mu_p = mu_12(R_P, s56)
E0_p = M_P_MEV / mu_p
L_ring = 2 * math.pi * HBAR_C_FM / E0_p
L_tube = R_P * L_ring
R_major = L_ring / (2 * math.pi)
a_minor = L_tube / (2 * math.pi)

N_GRID = 256


# ══════════════════════════════════════════════════════════════════════
#  Shape and eigenvalue functions (from Track 2-3)
# ══════════════════════════════════════════════════════════════════════

def cross_section_radius(theta1, a0, coeffs):
    r = np.full_like(theta1, a0, dtype=float)
    for i, ak in enumerate(coeffs):
        k = 2 * (i + 1)
        r = r + ak * np.cos(k * theta1)
    return r


def geodesic_path_length(a0, coeffs, R, n1, n2, N=1000):
    t = np.linspace(0, 2 * math.pi, N, endpoint=False)
    dt = t[1] - t[0]
    th1 = n1 * t
    th2 = n2 * t

    r_vals = cross_section_radius(th1, a0, coeffs)
    dr = np.zeros_like(th1)
    for i, ak in enumerate(coeffs):
        k = 2 * (i + 1)
        dr = dr - k * ak * np.sin(k * th1)

    rho = R + r_vals * np.cos(th1)
    dx = n1 * (-r_vals * np.sin(th1) + dr * np.cos(th1)) * np.cos(th2) \
         - n2 * rho * np.sin(th2)
    dy = n1 * (-r_vals * np.sin(th1) + dr * np.cos(th1)) * np.sin(th2) \
         + n2 * rho * np.cos(th2)
    dz = n1 * (r_vals * np.cos(th1) + dr * np.sin(th1))

    speed = np.sqrt(dx**2 + dy**2 + dz**2)
    return np.sum(speed) * dt


def solve_eigenvalue(a0, coeffs, R, n1, n2, N_grid=256):
    """Return the eigenvalue for a specific (n1, n2) mode on the shape."""
    theta1 = np.linspace(0, 2 * math.pi, N_grid, endpoint=False)
    h = 2 * math.pi / N_grid

    r_vals = cross_section_radius(theta1, a0, coeffs)
    dr = np.zeros_like(theta1)
    for i, ak in enumerate(coeffs):
        k = 2 * (i + 1)
        dr = dr - k * ak * np.sin(k * theta1)

    A = np.sqrt(r_vals**2 + dr**2)
    rho = R + r_vals * np.cos(theta1)
    B = np.abs(rho)

    p = B / A
    w = A * B
    q = n2**2 * A / B

    if np.any(B < 1e-10) or np.any(A < 1e-10) or np.any(w <= 0):
        return 1e10
    if np.any(r_vals < 0.01 * a_minor):
        return 1e10

    p_hp = np.array([(p[j] + p[(j+1) % N_grid]) / 2 for j in range(N_grid)])
    p_hm = np.array([(p[j] + p[(j-1) % N_grid]) / 2 for j in range(N_grid)])

    S_mat = np.zeros((N_grid, N_grid))
    W_mat = np.diag(w)

    for j in range(N_grid):
        jm = (j - 1) % N_grid
        jp = (j + 1) % N_grid
        S_mat[j, jm] = -p_hm[j] / h**2
        S_mat[j, j] = (p_hm[j] + p_hp[j]) / h**2 + q[j]
        S_mat[j, jp] = -p_hp[j] / h**2

    try:
        eigvals = linalg.eigh(S_mat, W_mat, eigvals_only=True)
    except Exception:
        return 1e10

    idx = 2 * n1  # sin-like mode
    if idx >= len(eigvals):
        return 1e10
    return eigvals[idx]


def find_optimal_shape(n1, n2, k_max_pairs=2):
    """
    Find the cross-section shape that minimizes mode energy for
    a specific (n1, n2) mode at constant path length.

    Returns (a0, coeffs, eigenvalue, success).
    """
    # Reference path length (circular torus)
    path_circ = geodesic_path_length(a_minor, [], R_major, n1, n2)
    lambda_circ = solve_eigenvalue(a_minor, [], R_major, n1, n2, N_GRID)

    if path_circ < 1e-6 or lambda_circ > 1e9:
        return a_minor, [], lambda_circ, False

    def objective(params):
        coeffs = [p * a_minor for p in params]

        # Check cross-section stays positive
        theta_test = np.linspace(0, 2 * math.pi, 100)
        r_test = cross_section_radius(theta_test, a_minor, coeffs)
        if np.any(r_test < 0.05 * a_minor):
            return 1e10

        # Rescale a₀ for constant path length
        try:
            a0 = brentq(
                lambda a0_t: geodesic_path_length(a0_t, coeffs, R_major, n1, n2) - path_circ,
                0.1 * a_minor, 4.0 * a_minor, xtol=1e-6)
        except Exception:
            return 1e10

        return solve_eigenvalue(a0, coeffs, R_major, n1, n2, N_GRID)

    x0 = np.zeros(k_max_pairs)
    result = minimize(objective, x0, method='Nelder-Mead',
                      options={'xatol': 1e-5, 'fatol': 1e-8, 'maxiter': 300})

    coeffs_opt = [p * a_minor for p in result.x]

    # Get final a₀
    try:
        a0_opt = brentq(
            lambda a0_t: geodesic_path_length(a0_t, coeffs_opt, R_major, n1, n2) - path_circ,
            0.1 * a_minor, 4.0 * a_minor, xtol=1e-6)
    except Exception:
        return a_minor, [], lambda_circ, False

    return a0_opt, coeffs_opt, result.fun, result.success


# ══════════════════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════════════════

print("=" * 70)
print("R40 Track 4: Per-mode self-consistent shapes")
print("=" * 70)
print()
print(f"Proton torus: a = {a_minor:.4f} fm, R = {R_major:.4f} fm")
print()


# ── Section 1: Find optimal shape for each mode ──────────────────

print("-" * 70)
print("Section 1: Optimal shape for each (n₁, n₂) mode")
print("-" * 70)
print()

modes = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
    (2, 1), (2, 2), (2, 3), (2, 4),
    (3, 2), (3, 3),
]

print(f"  {'(n₁,n₂)':>8}  {'λ_circ':>10}  {'λ_opt':>10}  {'Δλ/λ':>10}  "
      f"{'a₂/a':>8}  {'a₄/a':>8}  {'shape':>10}")
print(f"  {'─'*8}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'*8}  {'─'*10}")

results_table = []

for n1, n2 in modes:
    lambda_circ = solve_eigenvalue(a_minor, [], R_major, n1, n2, N_GRID)

    if lambda_circ > 1e9:
        print(f"  ({n1},{n2})     {'FAIL':>10}")
        continue

    a0_opt, coeffs, lambda_opt, success = find_optimal_shape(n1, n2)

    if not success or lambda_opt > 1e9:
        print(f"  ({n1},{n2})     {lambda_circ:10.4f}  {'NO OPT':>10}")
        continue

    delta = (lambda_opt - lambda_circ) / lambda_circ

    a2_frac = coeffs[0] / a_minor if len(coeffs) > 0 else 0
    a4_frac = coeffs[1] / a_minor if len(coeffs) > 1 else 0

    if abs(a2_frac) < 0.01 and abs(a4_frac) < 0.01:
        shape = "circular"
    elif abs(a4_frac) > abs(a2_frac):
        shape = "4-lobed"
    else:
        shape = "elliptic"

    print(f"  ({n1},{n2})     {lambda_circ:10.4f}  {lambda_opt:10.4f}  "
          f"{delta:+10.4f}  {a2_frac:+8.4f}  {a4_frac:+8.4f}  {shape:>10}")

    results_table.append({
        'n1': n1, 'n2': n2,
        'lambda_circ': lambda_circ, 'lambda_opt': lambda_opt,
        'delta': delta,
        'a2_frac': a2_frac, 'a4_frac': a4_frac,
        'shape': shape,
    })


# ── Section 2: Energy spectrum on self-consistent shapes ─────────

print()
print("-" * 70)
print("Section 2: Does each mode prefer a DIFFERENT shape?")
print("-" * 70)
print()

if len(results_table) > 1:
    # Compare the optimal a₂, a₄ across modes
    a2_vals = [r['a2_frac'] for r in results_table]
    a4_vals = [r['a4_frac'] for r in results_table]

    a2_spread = max(a2_vals) - min(a2_vals)
    a4_spread = max(a4_vals) - min(a4_vals)

    print(f"  a₂/a range across modes: [{min(a2_vals):+.4f}, {max(a2_vals):+.4f}]  "
          f"(spread: {a2_spread:.4f})")
    print(f"  a₄/a range across modes: [{min(a4_vals):+.4f}, {max(a4_vals):+.4f}]  "
          f"(spread: {a4_spread:.4f})")
    print()

    if a4_spread > 0.1:
        print("  Different modes prefer DIFFERENT shapes.")
        print("  Each particle would live on its own torus geometry.")
        print("  The mass spectrum must be recomputed per-mode.")
    else:
        print("  Modes prefer similar shapes (spread < 10%).")
        print("  A single equilibrium shape is a good approximation.")


# ── Section 3: Ghost suppression assessment ──────────────────────

print()
print("-" * 70)
print("Section 3: Ghost suppression from per-mode optimization")
print("-" * 70)
print()

print(f"  {'(n₁,n₂)':>8}  {'Δλ/λ (own shape)':>18}  {'stabilized?':>12}")
print(f"  {'─'*8}  {'─'*18}  {'─'*12}")

n_stabilized = 0
n_destabilized = 0

for r in results_table:
    d = r['delta']
    if d < -0.005:
        status = "YES (lower)"
        n_stabilized += 1
    elif d > 0.005:
        status = "NO (higher)"
        n_destabilized += 1
    else:
        status = "~neutral"

    print(f"  ({r['n1']},{r['n2']})     {d:+18.4f}  {status:>12}")

print()
print(f"  Stabilized by own optimal shape: {n_stabilized}/{len(results_table)}")
print(f"  Destabilized: {n_destabilized}/{len(results_table)}")
print()

# A mode is a genuine particle candidate only if its own optimal
# shape gives a lower eigenvalue than the circular torus.
# If even on its own best shape the energy goes UP, the mode is
# intrinsically unstable — no shape can help it.

any_raised = [r for r in results_table if r['delta'] > 0.005]
if any_raised:
    print("  Modes that are RAISED even on their own optimal shape:")
    for r in any_raised:
        print(f"    ({r['n1']},{r['n2']}): Δλ/λ = {r['delta']:+.4f}")
    print()
    print("  These modes cannot be stabilized by ANY cross-section")
    print("  deformation (at constant path length).  They are")
    print("  geometrically forbidden — genuine ghost suppression.")
else:
    print("  All modes can find a stabilizing shape — no geometric")
    print("  suppression from per-mode optimization alone.")


# ══════════════════════════════════════════════════════════════════════
#  Summary
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("Track 4 Summary")
print("=" * 70)
print()

if len(results_table) > 0:
    # Group by n1
    for n1_val in sorted(set(r['n1'] for r in results_table)):
        modes_n1 = [r for r in results_table if r['n1'] == n1_val]
        print(f"  n₁ = {n1_val} family (charge {'±' + str(n1_val) if n1_val > 0 else '0'}, "
              f"spin {'½' if n1_val % 2 == 1 else 'int'}):")
        for r in sorted(modes_n1, key=lambda x: x['n2']):
            print(f"    (n₁,n₂) = ({r['n1']},{r['n2']}): Δλ = {r['delta']:+.1%}, "
                  f"shape = {r['shape']}")
        print()
