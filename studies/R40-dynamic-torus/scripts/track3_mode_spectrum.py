#!/usr/bin/env python3
"""
R40 Track 3: Mode spectrum on the self-consistent shape.

Takes the optimal cross-section from Track 2 (a₂/a = +0.056,
a₄/a = -0.196) and computes the eigenvalue spectrum for a range of
modes (n₁, n₂).  Compares to the circular-torus spectrum.

Key question: which modes have LOWER energy on the deformed shape
(they "fit" the shape) and which have HIGHER energy (they fight it)?
Modes that fight the shape are candidates for geometric suppression
— the ghost filter.

We also check: does each mode's own pressure profile match the
equilibrium shape?  A mode is "compatible" if it would drive a
similar deformation; "incompatible" if it drives a conflicting one.
"""

import sys
import os
import math

import numpy as np
from scipy import linalg
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model import solve_shear_for_alpha, mu_12, M_P_MEV

HBAR_C_FM = 197.3269804


# ══════════════════════════════════════════════════════════════════════
#  Geometry and shape functions (from Track 2)
# ══════════════════════════════════════════════════════════════════════

R_P = 8.906
s56 = solve_shear_for_alpha(R_P)
mu_p = mu_12(R_P, s56)
E0_p = M_P_MEV / mu_p
L_ring = 2 * math.pi * HBAR_C_FM / E0_p
L_tube = R_P * L_ring
R_major = L_ring / (2 * math.pi)
a_minor = L_tube / (2 * math.pi)

# Track 2 optimal shape
A2_OPT = +0.056426 * a_minor   # fm
A4_OPT = -0.195744 * a_minor   # fm
A0_OPT = 3.4411                 # fm (from Track 2)

N_GRID = 256


def cross_section_radius(theta1, a0, coeffs):
    r = np.full_like(theta1, a0, dtype=float)
    for i, ak in enumerate(coeffs):
        k = 2 * (i + 1)
        r = r + ak * np.cos(k * theta1)
    return r


def solve_eigenvalues(a0, coeffs, R, n2, N_grid, n_eigs=20):
    """
    Solve the Sturm-Liouville problem for all tube modes at a given
    ring winding number n₂.

    Returns sorted eigenvalues (lowest first).
    """
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
        return None

    p_half_plus = np.array([(p[j] + p[(j+1) % N_grid]) / 2
                             for j in range(N_grid)])
    p_half_minus = np.array([(p[j] + p[(j-1) % N_grid]) / 2
                              for j in range(N_grid)])

    S_mat = np.zeros((N_grid, N_grid))
    W_mat = np.diag(w)

    for j in range(N_grid):
        jm = (j - 1) % N_grid
        jp = (j + 1) % N_grid
        S_mat[j, jm] = -p_half_minus[j] / h**2
        S_mat[j, j] = (p_half_minus[j] + p_half_plus[j]) / h**2 + q[j]
        S_mat[j, jp] = -p_half_plus[j] / h**2

    try:
        eigvals = linalg.eigh(S_mat, W_mat, eigvals_only=True)
    except Exception:
        return None

    return eigvals[:n_eigs]


def pressure_fourier(a0, coeffs, R, n1, n2, N_pts=2000, n_harmonics=8):
    """
    Compute the Fourier decomposition of the radiation pressure
    for a specific (n1, n2) mode on a given shape.

    Returns A_k array (cosine coefficients, k=0..n_harmonics).
    """
    t = np.linspace(0, 2 * math.pi, N_pts, endpoint=False)
    dt = t[1] - t[0]
    th1 = n1 * t
    th2 = n2 * t

    r_vals = cross_section_radius(th1, a0, coeffs)
    dr = np.zeros_like(th1)
    for i, ak in enumerate(coeffs):
        k = 2 * (i + 1)
        dr = dr - k * ak * np.sin(k * th1)

    rho = R + r_vals * np.cos(th1)

    # 3D tangent
    dxdt = n1 * (-r_vals * np.sin(th1) + dr * np.cos(th1)) * np.cos(th2) \
           - n2 * rho * np.sin(th2)
    dydt = n1 * (-r_vals * np.sin(th1) + dr * np.cos(th1)) * np.sin(th2) \
           + n2 * rho * np.cos(th2)
    dzdt = n1 * (r_vals * np.cos(th1) + dr * np.sin(th1))

    speed = np.sqrt(dxdt**2 + dydt**2 + dzdt**2)
    T_hat = np.stack([dxdt, dydt, dzdt], axis=-1) / speed[:, None]

    # Curvature vector
    dT = np.zeros_like(T_hat)
    for j in range(3):
        dT[:, j] = np.gradient(T_hat[:, j], dt)
    kappa_vec = dT / speed[:, None]

    # Outward radial unit vector in tube cross-section
    e_r = np.stack([
        np.cos(th1) * np.cos(th2),
        np.cos(th1) * np.sin(th2),
        np.sin(th1),
    ], axis=-1)

    kappa_radial = np.sum(kappa_vec * e_r, axis=1)
    F_radial = -kappa_radial * speed  # positive = outward

    # Bin by θ₁
    N_BINS = 256
    theta1_bins = np.linspace(0, 2 * math.pi, N_BINS, endpoint=False)
    F_binned = np.zeros(N_BINS)
    counts = np.zeros(N_BINS)
    th1_mod = th1 % (2 * math.pi)
    for i in range(N_pts):
        bin_idx = int(th1_mod[i] / (2 * math.pi) * N_BINS) % N_BINS
        F_binned[bin_idx] += F_radial[i]
        counts[bin_idx] += 1
    mask = counts > 0
    F_binned[mask] /= counts[mask]

    # Fourier
    A_k = np.zeros(n_harmonics + 1)
    A_k[0] = np.mean(F_binned[mask])
    for k in range(1, n_harmonics + 1):
        A_k[k] = 2 * np.mean(F_binned[mask] * np.cos(k * theta1_bins[mask]))
    return A_k


# ══════════════════════════════════════════════════════════════════════
#  Main
# ══════════════════════════════════════════════════════════════════════

print("=" * 70)
print("R40 Track 3: Mode spectrum on the self-consistent shape")
print("=" * 70)
print()
print(f"Proton torus: a = {a_minor:.4f} fm, R = {R_major:.4f} fm")
print(f"Optimal shape: a₀ = {A0_OPT:.4f}, a₂ = {A2_OPT:+.4f}, a₄ = {A4_OPT:+.4f} fm")
print()


# ── Section 1: Eigenvalue spectrum comparison ─────────────────────

print("-" * 70)
print("Section 1: Eigenvalue spectrum — circular vs optimal shape")
print("-" * 70)
print()

coeffs_opt = [A2_OPT, A4_OPT]
coeffs_circ = []

print(f"  {'n₂':>4}  {'n₁':>4}  {'λ_circ':>12}  {'λ_opt':>12}  "
      f"{'Δλ/λ_circ':>12}  {'lower?':>8}")
print(f"  {'─'*4}  {'─'*4}  {'─'*12}  {'─'*12}  {'─'*12}  {'─'*8}")

n_lower = 0
n_higher = 0
n_total = 0

for n2 in range(0, 7):
    eigs_circ = solve_eigenvalues(a_minor, coeffs_circ, R_major, n2, N_GRID, 14)
    eigs_opt = solve_eigenvalues(A0_OPT, coeffs_opt, R_major, n2, N_GRID, 14)

    if eigs_circ is None or eigs_opt is None:
        print(f"  n₂={n2}: eigenvalue solve FAILED")
        continue

    # Pair eigenvalues by index (they correspond to the same n₁ family)
    n_show = min(7, len(eigs_circ), len(eigs_opt))
    for i in range(n_show):
        lc = eigs_circ[i]
        lo = eigs_opt[i]
        if lc > 1e-6:
            delta = (lo - lc) / lc
            lower = "YES" if delta < -0.005 else ("no" if delta > 0.005 else "~same")
        else:
            delta = 0.0
            lower = "—"

        # Approximate n₁: the i-th eigenvalue at n₂ corresponds to
        # tube mode number roughly i//2 (cos/sin pairs)
        n1_approx = i // 2

        if n1_approx <= 3 or i < 4:
            print(f"  {n2:4d}  {n1_approx:4d}  {lc:12.4f}  {lo:12.4f}  "
                  f"{delta:+12.6f}  {lower:>8}")

        n_total += 1
        if delta < -0.005:
            n_lower += 1
        elif delta > 0.005:
            n_higher += 1

print()
print(f"  Summary: {n_lower} modes lower, {n_higher} modes higher, "
      f"{n_total - n_lower - n_higher} unchanged (out of {n_total})")


# ── Section 2: Pressure compatibility ─────────────────────────────

print()
print("-" * 70)
print("Section 2: Pressure profile compatibility")
print("-" * 70)
print()

# The equilibrium shape was determined by the (1,2) mode's pressure.
# For other modes, compute THEIR pressure profile and compare.
# A mode is "compatible" if its dominant pressure harmonic matches
# the equilibrium shape's (k=4 dominant).

print(f"  Mode pressure Fourier decomposition on circular torus:")
print(f"  (normalized: |Aₖ|/A₀ for each mode)")
print()
print(f"  {'(n₁,n₂)':>8}  {'A₀ sign':>8}  {'k=1':>8}  {'k=2':>8}  "
      f"{'k=3':>8}  {'k=4':>8}  {'dominant':>8}")
print(f"  {'─'*8}  {'─'*8}  {'─'*8}  {'─'*8}  {'─'*8}  {'─'*8}  {'─'*8}")

modes_to_test = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
    (2, 1), (2, 2), (2, 3), (2, 4),
    (3, 2), (3, 3), (3, 4),
    (0, 1), (0, 2), (0, 3),
]

reference_A4 = None  # will set from (1,2) mode

for n1_test, n2_test in modes_to_test:
    if n1_test == 0 and n2_test == 0:
        continue
    try:
        A_k = pressure_fourier(a_minor, [], R_major, n1_test, n2_test)
    except Exception:
        continue

    if abs(A_k[0]) < 1e-15:
        continue

    sign = "+" if A_k[0] > 0 else "−"
    rel = [abs(A_k[k]) / abs(A_k[0]) if k <= len(A_k)-1 else 0
           for k in range(1, 5)]

    dom_k = max(range(1, 5), key=lambda k: abs(A_k[k]))

    if n1_test == 1 and n2_test == 2:
        reference_A4 = A_k[4] / A_k[0]  # sign matters for compatibility

    print(f"  ({n1_test},{n2_test})     {sign:>8}  {rel[0]:8.4f}  {rel[1]:8.4f}  "
          f"{rel[2]:8.4f}  {rel[3]:8.4f}  k={dom_k:d}")


# ── Section 3: Ghost filter assessment ────────────────────────────

print()
print("-" * 70)
print("Section 3: Ghost filter assessment")
print("-" * 70)
print()

# Compare the eigenvalue shift for different mode families.
# Modes that go UP in energy on the deformed shape are "punished"
# by the shape — they're less stable.
# Modes that go DOWN are "rewarded" — they fit the shape.

print(f"  Energy shift by mode family (optimal vs circular):")
print()
print(f"  {'n₂':>4}  {'n₁=0':>10}  {'n₁=1':>10}  {'n₁=2':>10}  {'n₁=3':>10}")
print(f"  {'─'*4}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*10}")

for n2 in range(0, 7):
    eigs_circ = solve_eigenvalues(a_minor, coeffs_circ, R_major, n2, N_GRID, 8)
    eigs_opt = solve_eigenvalues(A0_OPT, coeffs_opt, R_major, n2, N_GRID, 8)

    if eigs_circ is None or eigs_opt is None:
        continue

    shifts = []
    for n1_idx in range(4):
        # Index into eigenvalue array: cos/sin pairs
        # n₁=0 is index 0, n₁=1 is index 1 or 2, etc.
        if n1_idx == 0:
            idx = 0
        else:
            idx = 2 * n1_idx  # sin-like mode

        if idx < len(eigs_circ) and idx < len(eigs_opt):
            lc = eigs_circ[idx]
            lo = eigs_opt[idx]
            if lc > 1e-6:
                shift = (lo - lc) / lc * 100
                shifts.append(f"{shift:+10.2f}%")
            else:
                shifts.append(f"{'—':>10}")
        else:
            shifts.append(f"{'—':>10}")

    print(f"  {n2:4d}  {'  '.join(shifts)}")


# ══════════════════════════════════════════════════════════════════════
#  Summary
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("Track 3 Summary")
print("=" * 70)
print()
print(f"Modes examined: {n_total}")
print(f"  Lowered by deformation:  {n_lower} ({n_lower/n_total*100:.0f}%)"
      if n_total > 0 else "")
print(f"  Raised by deformation:   {n_higher} ({n_higher/n_total*100:.0f}%)"
      if n_total > 0 else "")
print(f"  Roughly unchanged:       {n_total - n_lower - n_higher}")
print()
print(f"The (1,2) mode (the proton/electron) is the mode whose pressure")
print(f"DEFINED the equilibrium shape.  It should have the largest energy")
print(f"reduction.  Other modes may be raised or lowered depending on")
print(f"whether their pressure profiles are compatible with the 4-lobed")
print(f"equilibrium.")
print()

if n_higher > n_lower:
    print(f"More modes are RAISED than lowered → the deformation acts as a")
    print(f"selective filter, penalizing most modes while rewarding the (1,2).")
    print(f"This is the ghost suppression mechanism.")
elif n_lower > n_higher:
    print(f"More modes are LOWERED than raised → the deformation benefits")
    print(f"many modes, not just (1,2).  The ghost filter is weak.")
else:
    print(f"Roughly equal numbers raised and lowered — mixed result.")
