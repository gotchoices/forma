#!/usr/bin/env python3
"""
R40 Track 8: Free-r optimization — Dynamic Ma equilibrium from scratch.

The static model (R27) pins the proton aspect ratio r_p = 8.906 from
the neutron mass constraint.  But that derivation assumed a flat torus.
In Dynamic Ma the mode energy depends on the 3D shape, so the
equilibrium r may be completely different.

This track treats r = a/R as a FREE parameter alongside the cross-
section shape (a₂, a₄).  The only fixed inputs are:
  1. Proton mass: 938.272 MeV → Compton wavelength λ_C
  2. Mode winding: (n₁, n₂) = (1, 2)

For each r, we:
  1. Set L_tube = 2πa, L_ring = 2πR with a = r × R
  2. Scale overall size so the flat-geodesic path length = λ_C
  3. Solve the Sturm-Liouville eigenvalue for the (1,2) mode
  4. Optimize the cross-section shape (a₂, a₄) to minimize eigenvalue
  5. For r < 1, also compute the Clairaut geodesic and its path length

The Dynamic Ma equilibrium is the (r, a₂, a₄) that minimizes mode
energy on the embedded surface at fixed Compton path length.
"""

import sys
import os
import math

import numpy as np
from scipy.optimize import minimize, brentq
from scipy import linalg

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

HBAR_C_FM = 197.3269804
TWO_PI = 2 * math.pi
M_PROTON = 938.272046
LAMBDA_C = TWO_PI * HBAR_C_FM / M_PROTON

n1, n2 = 1, 2
N_THETA = 256


def cross_section_radius(theta1, a0, coeffs):
    r = np.full_like(theta1, a0, dtype=float)
    for i, ak in enumerate(coeffs):
        k = 2 * (i + 1)
        r = r + ak * np.cos(k * theta1)
    return r


def cross_section_dr(theta1, coeffs):
    dr = np.zeros_like(theta1, dtype=float)
    for i, ak in enumerate(coeffs):
        k = 2 * (i + 1)
        dr = dr - k * ak * np.sin(k * theta1)
    return dr


def flat_geodesic_path_length(a0, coeffs, R, N=2000):
    t = np.linspace(0, TWO_PI, N, endpoint=False)
    dt = TWO_PI / N
    th1 = n1 * t
    th2 = n2 * t

    r_vals = cross_section_radius(th1, a0, coeffs)
    dr = cross_section_dr(th1, coeffs)
    rho = R + r_vals * np.cos(th1)

    dx = n1 * (-r_vals * np.sin(th1) + dr * np.cos(th1)) * np.cos(th2) \
         - n2 * rho * np.sin(th2)
    dy = n1 * (-r_vals * np.sin(th1) + dr * np.cos(th1)) * np.sin(th2) \
         + n2 * rho * np.cos(th2)
    dz = n1 * (r_vals * np.cos(th1) + dr * np.sin(th1))

    speed = np.sqrt(dx**2 + dy**2 + dz**2)
    return np.sum(speed) * dt


def mode_eigenvalue(a0, coeffs, R, N_grid=256):
    theta1 = np.linspace(0, TWO_PI, N_grid, endpoint=False)
    h = TWO_PI / N_grid

    r_vals = cross_section_radius(theta1, a0, coeffs)
    dr = cross_section_dr(theta1, coeffs)

    A = np.sqrt(r_vals**2 + dr**2)
    rho = R + r_vals * np.cos(theta1)
    B = np.abs(rho)

    p = B / A
    w = A * B
    q = n2**2 * A / B

    if np.any(B < 1e-10) or np.any(A < 1e-10) or np.any(w <= 0):
        return 1e10

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

    if np.any(np.diag(W_mat) <= 0):
        return 1e10

    try:
        eigvals = linalg.eigh(S_mat, W_mat, eigvals_only=True)
    except Exception:
        return 1e10

    idx = 2 * n1
    if idx >= len(eigvals):
        return 1e10

    return eigvals[idx]


def clairaut_geodesic(a0, coeffs, R, N=8000):
    """Clairaut geodesic path length (only valid for non-self-intersecting)."""
    theta1 = np.linspace(0, TWO_PI, N, endpoint=False)
    dth = TWO_PI / N

    r_vals = cross_section_radius(theta1, a0, coeffs)
    dr_vals = cross_section_dr(theta1, coeffs)

    g11 = r_vals**2 + dr_vals**2
    sqrt_g11 = np.sqrt(g11)
    rho = R + r_vals * np.cos(theta1)

    rho_min = np.min(rho)
    if rho_min <= 1e-10:
        return None, None, False

    target_winding = TWO_PI * n2 / n1

    def winding_residual(C):
        rho2_minus_C2 = np.maximum(rho**2 - C**2, 1e-30)
        denom = np.sqrt(rho2_minus_C2)
        integrand = C * sqrt_g11 / (rho * denom)
        return np.sum(integrand) * dth - target_winding

    C_max = rho_min * (1 - 1e-6)
    try:
        val_lo = winding_residual(1e-12)
        val_hi = winding_residual(C_max)
        if val_lo * val_hi > 0:
            return None, None, False
        C_opt = brentq(winding_residual, 1e-12, C_max, xtol=1e-14, maxiter=500)
    except (ValueError, RuntimeError):
        return None, None, False

    rho2_minus_C2 = np.maximum(rho**2 - C_opt**2, 1e-30)
    denom = np.sqrt(rho2_minus_C2)
    ds_dth1 = sqrt_g11 * rho / denom
    L1 = np.sum(ds_dth1) * dth

    return C_opt, n1 * L1, True


# ══════════════════════════════════════════════════════════════════════
#  Section 1: Sweep r on circular cross-section
# ══════════════════════════════════════════════════════════════════════

print("=" * 70)
print("R40 Track 8: Free-r optimization (Dynamic Ma from scratch)")
print("=" * 70)
print()
print(f"  Inputs:")
print(f"    Proton mass:       {M_PROTON:.3f} MeV")
print(f"    Compton λ_C:       {LAMBDA_C:.6f} fm")
print(f"    Mode:              ({n1},{n2})")
print(f"    Aspect ratio r:    FREE")
print()

print("-" * 70)
print("Section 1: Mode eigenvalue vs r — circular cross-section")
print("-" * 70)
print()
print("  For each r, scale the torus so the flat-geodesic path length")
print("  equals λ_C.  Then compute the Sturm-Liouville eigenvalue.")
print()

r_values = [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0,
            5.0, 7.0, 8.906, 10.0, 15.0, 20.0]

print(f"  {'r':>8}  {'a (fm)':>10}  {'R (fm)':>10}  {'L_flat':>10}  "
      f"{'a/R':>6}  {'λ_SL':>12}  {'self-int?':>10}")
print(f"  {'─'*8}  {'─'*10}  {'─'*10}  {'─'*10}  "
      f"{'─'*6}  {'─'*12}  {'─'*10}")

sweep_data = []
for r in r_values:
    # For a circular torus with aspect ratio r = L_tube/L_ring:
    #   L_tube = 2πa,  L_ring = 2πR,  r = a/R
    #   Flat geodesic path length = √((n₁ L_tube)² + (n₂ L_ring)²)
    #     = √((2πa)² + (4πR)²) = 2π √(a² + 4R²) = 2πR √(r² + 4)
    #   Setting this = λ_C:  R = λ_C / (2π √(r² + 4))
    R_val = LAMBDA_C / (TWO_PI * math.sqrt(r**2 + n2**2))
    a_val = r * R_val
    L_flat = flat_geodesic_path_length(a_val, [], R_val)
    lam = mode_eigenvalue(a_val, [], R_val)
    si = "YES" if a_val > R_val else "no"

    print(f"  {r:8.3f}  {a_val:10.6f}  {R_val:10.6f}  {L_flat:10.6f}  "
          f"{a_val/R_val:6.3f}  {lam:12.6f}  {si:>10}")
    sweep_data.append((r, a_val, R_val, L_flat, lam))

print()

# Find minimum
min_idx = min(range(len(sweep_data)), key=lambda i: sweep_data[i][4])
r_best, a_best, R_best, L_best, lam_best = sweep_data[min_idx]
print(f"  Minimum eigenvalue at r = {r_best:.3f}")
print(f"    a = {a_best:.6f} fm, R = {R_best:.6f} fm, a/R = {a_best/R_best:.4f}")
print(f"    λ = {lam_best:.6f}")
si_best = "self-intersecting" if a_best > R_best else "non-self-intersecting"
print(f"    Geometry: {si_best}")


# ══════════════════════════════════════════════════════════════════════
#  Section 2: Finer sweep around the minimum
# ══════════════════════════════════════════════════════════════════════

print()
print("-" * 70)
print("Section 2: Fine sweep around the minimum")
print("-" * 70)
print()

# Determine sweep range around the minimum
if r_best <= 0.1:
    r_fine = np.linspace(0.01, 0.5, 50)
elif r_best >= 15:
    r_fine = np.linspace(5, 30, 50)
else:
    r_lo = max(0.01, r_best / 3)
    r_hi = min(30, r_best * 3)
    r_fine = np.linspace(r_lo, r_hi, 60)

fine_data = []
for r in r_fine:
    R_val = LAMBDA_C / (TWO_PI * math.sqrt(r**2 + n2**2))
    a_val = r * R_val
    lam = mode_eigenvalue(a_val, [], R_val)
    fine_data.append((r, a_val, R_val, lam))

fine_min_idx = min(range(len(fine_data)), key=lambda i: fine_data[i][3])
r_opt, a_opt, R_opt, lam_opt = fine_data[fine_min_idx]

print(f"  Fine-grid minimum at r = {r_opt:.4f}")
print(f"    a = {a_opt:.6f} fm, R = {R_opt:.6f} fm")
print(f"    λ = {lam_opt:.8f}")
print(f"    Self-intersecting: {'YES' if a_opt > R_opt else 'no'}")
print()

# Show the landscape
print(f"  {'r':>8}  {'λ_SL':>12}  {'Δλ/λ_min':>10}")
print(f"  {'─'*8}  {'─'*12}  {'─'*10}")
for i in range(0, len(fine_data), max(1, len(fine_data) // 20)):
    r, a, R, lam = fine_data[i]
    dlam = (lam - lam_opt) / lam_opt * 100
    marker = " ← min" if abs(r - r_opt) < 0.01 else ""
    print(f"  {r:8.4f}  {lam:12.6f}  {dlam:+10.4f}%{marker}")


# ══════════════════════════════════════════════════════════════════════
#  Section 3: Shape optimization at each r
# ══════════════════════════════════════════════════════════════════════

print()
print("-" * 70)
print("Section 3: Shape optimization (a₂, a₄) at selected r values")
print("-" * 70)
print()

test_rs = [0.1, 0.3, 0.5, 0.8, 1.0, 2.0, 5.0, r_opt]
if r_opt not in test_rs:
    test_rs.append(r_opt)
test_rs = sorted(set(test_rs))

print(f"  {'r':>8}  {'λ_circ':>12}  {'λ_opt':>12}  {'Δλ/λ_circ':>10}  "
      f"{'a₂/a':>8}  {'a₄/a':>8}  {'self-int?':>10}")
print(f"  {'─'*8}  {'─'*12}  {'─'*12}  {'─'*10}  "
      f"{'─'*8}  {'─'*8}  {'─'*10}")

shape_data = []
for r in test_rs:
    R_val = LAMBDA_C / (TWO_PI * math.sqrt(r**2 + n2**2))
    a_val = r * R_val
    lam_circ = mode_eigenvalue(a_val, [], R_val)
    L_target = flat_geodesic_path_length(a_val, [], R_val)

    def obj(params, _a_nom=a_val, _R=R_val, _L_tgt=L_target):
        a2f, a4f = params
        a2 = a2f * _a_nom
        a4 = a4f * _a_nom
        coeffs = [a2, a4]

        theta_test = np.linspace(0, TWO_PI, 100)
        r_test = cross_section_radius(theta_test, _a_nom, coeffs)
        if np.any(r_test < 0.05 * _a_nom):
            return 1e10

        try:
            a0 = brentq(lambda a0t: flat_geodesic_path_length(a0t, coeffs, _R) - _L_tgt,
                         0.2 * _a_nom, 3.0 * _a_nom, xtol=1e-6)
        except Exception:
            return 1e10
        return mode_eigenvalue(a0, coeffs, _R)

    res = minimize(obj, [0.0, 0.0], method='Nelder-Mead',
                   options={'xatol': 1e-5, 'fatol': 1e-8, 'maxiter': 500})

    a2f, a4f = res.x
    dE = (res.fun - lam_circ) / lam_circ * 100 if lam_circ > 0 else 0
    si = "YES" if a_val > R_val else "no"

    print(f"  {r:8.4f}  {lam_circ:12.6f}  {res.fun:12.6f}  {dE:+10.4f}%  "
          f"{a2f:+8.4f}  {a4f:+8.4f}  {si:>10}")
    shape_data.append((r, lam_circ, res.fun, dE, a2f, a4f, R_val, a_val))

print()

# Find the global minimum across all (r, shape) combinations
global_min = min(shape_data, key=lambda x: x[2])
r_gmin = global_min[0]
lam_gmin = global_min[2]
a2_gmin = global_min[4]
a4_gmin = global_min[5]
R_gmin = global_min[6]
a_gmin = global_min[7]

print(f"  Global minimum: r = {r_gmin:.4f}")
print(f"    λ_opt = {lam_gmin:.8f}")
print(f"    a₂/a = {a2_gmin:+.4f},  a₄/a = {a4_gmin:+.4f}")
print(f"    a = {a_gmin:.6f} fm, R = {R_gmin:.6f} fm")
print(f"    Self-intersecting: {'YES' if a_gmin > R_gmin else 'no'}")


# ══════════════════════════════════════════════════════════════════════
#  Section 4: Joint (r, a₂, a₄) optimization
# ══════════════════════════════════════════════════════════════════════

print()
print("-" * 70)
print("Section 4: Joint optimization over (r, a₂, a₄)")
print("-" * 70)
print()

def joint_objective(params):
    r_trial, a2_frac, a4_frac = params
    if r_trial < 0.01 or r_trial > 50:
        return 1e10

    R_val = LAMBDA_C / (TWO_PI * math.sqrt(r_trial**2 + n2**2))
    a_val = r_trial * R_val
    a2 = a2_frac * a_val
    a4 = a4_frac * a_val
    coeffs = [a2, a4]

    theta_test = np.linspace(0, TWO_PI, 100)
    r_test = cross_section_radius(theta_test, a_val, coeffs)
    if np.any(r_test < 0.05 * a_val):
        return 1e10

    L_target = LAMBDA_C

    try:
        a0 = brentq(lambda a0t: flat_geodesic_path_length(a0t, coeffs, R_val) - L_target,
                     0.1 * a_val, 5.0 * a_val, xtol=1e-6)
    except Exception:
        return 1e10

    return mode_eigenvalue(a0, coeffs, R_val)


# Start from several initial guesses
best_result = None
for r0, a2_0, a4_0 in [(0.5, 0.0, 0.0), (1.0, 0.0, 0.0), (5.0, 0.0, 0.0),
                         (r_gmin, a2_gmin, a4_gmin),
                         (0.1, 0.0, 0.0), (8.906, 0.0, 0.0)]:
    res = minimize(joint_objective, [r0, a2_0, a4_0], method='Nelder-Mead',
                   options={'xatol': 1e-5, 'fatol': 1e-10, 'maxiter': 2000})
    if best_result is None or res.fun < best_result.fun:
        best_result = res

r_final, a2_final, a4_final = best_result.x
R_final = LAMBDA_C / (TWO_PI * math.sqrt(r_final**2 + n2**2))
a_final = r_final * R_final

print(f"  Joint optimization result:")
print(f"    r = {r_final:.6f} (aspect ratio = a/R)")
print(f"    a₂/a = {a2_final:+.6f}")
print(f"    a₄/a = {a4_final:+.6f}")
print(f"    λ = {best_result.fun:.10f}")
print(f"    a = {a_final:.6f} fm, R = {R_final:.6f} fm")
print(f"    L_tube = {TWO_PI * a_final:.4f} fm")
print(f"    L_ring = {TWO_PI * R_final:.4f} fm")
print(f"    Self-intersecting: {'YES' if a_final > R_final else 'no'}")
print(f"    Converged: {best_result.success}")
print()

# Clairaut check for non-self-intersecting result
if a_final < R_final:
    C, L_clair, ok = clairaut_geodesic(a_final, [a2_final * a_final, a4_final * a_final], R_final)
    L_flat = flat_geodesic_path_length(a_final, [a2_final * a_final, a4_final * a_final], R_final)
    if ok:
        print(f"  Clairaut geodesic (non-self-intersecting — exists!):")
        print(f"    C = {C:.6f} fm")
        print(f"    L_flat = {L_flat:.4f} fm, L_Clairaut = {L_clair:.4f} fm")
        print(f"    ΔL/L = {(L_clair - L_flat) / L_flat * 100:+.2f}%")
    else:
        print(f"  Clairaut geodesic: computation failed (near turning point)")
else:
    print(f"  Clairaut geodesic: N/A (self-intersecting)")


# ══════════════════════════════════════════════════════════════════════
#  Section 5: Physical interpretation
# ══════════════════════════════════════════════════════════════════════

print()
print("-" * 70)
print("Section 5: Comparison with static model")
print("-" * 70)
print()

# Static model values
R_P_STATIC = 8.906
from lib.ma_model import solve_shear_for_alpha, mu_12, M_P_MEV
s56 = solve_shear_for_alpha(R_P_STATIC)
mu_p = mu_12(R_P_STATIC, s56)
E0_static = M_P_MEV / mu_p
L_ring_static = TWO_PI * HBAR_C_FM / E0_static
L_tube_static = R_P_STATIC * L_ring_static
R_static = L_ring_static / TWO_PI
a_static = L_tube_static / TWO_PI

print(f"  Static model (R27, flat torus):")
print(f"    r = {R_P_STATIC}")
print(f"    a = {a_static:.6f} fm, R = {R_static:.6f} fm")
print(f"    L_tube = {L_tube_static:.4f} fm, L_ring = {L_ring_static:.4f} fm")
print()
print(f"  Dynamic Ma equilibrium (this track):")
print(f"    r = {r_final:.6f}")
print(f"    a = {a_final:.6f} fm, R = {R_final:.6f} fm")
print(f"    L_tube = {TWO_PI * a_final:.4f} fm, L_ring = {TWO_PI * R_final:.4f} fm")
print(f"    a₂/a = {a2_final:+.4f}, a₄/a = {a4_final:+.4f}")
print()

if abs(r_final - R_P_STATIC) / R_P_STATIC < 0.1:
    print(f"  Dynamic Ma selects r ≈ {r_final:.2f}, close to the static value.")
    print(f"  The shape deformation is the primary effect; the aspect ratio")
    print(f"  is secondary.")
elif r_final < 1:
    print(f"  Dynamic Ma selects r = {r_final:.4f} < 1.")
    print(f"  The torus is NON-SELF-INTERSECTING.")
    print(f"  The photon path is mostly ring-dominated (tube is thin).")
    print(f"  This resolves the self-intersection problem (F20, F22).")
    print(f"  All Clairaut geodesic analysis applies (Track 6).")
else:
    print(f"  Dynamic Ma selects r = {r_final:.4f} > 1 but ≠ 8.906.")
    print(f"  Still self-intersecting but less extreme than the static model.")


# ══════════════════════════════════════════════════════════════════════
#  Summary
# ══════════════════════════════════════════════════════════════════════

print()
print()
print("=" * 70)
print("Track 8 Summary")
print("=" * 70)
print()
print(f"  The Sturm-Liouville eigenvalue on the embedded torus depends on r.")
print(f"  On a circular cross-section, the minimum eigenvalue is at r ≈ {r_opt:.2f}.")
print(f"  With shape optimization (a₂, a₄), the joint minimum is at")
print(f"  r ≈ {r_final:.4f}, a₂/a ≈ {a2_final:+.4f}, a₄/a ≈ {a4_final:+.4f}.")
print()
if r_final < 1:
    print(f"  KEY RESULT: Dynamic Ma equilibrium is NON-SELF-INTERSECTING.")
    print(f"  The self-intersection problem (F20) is resolved when r is free.")
    print(f"  The Clairaut geodesic exists, and the '3D embedding = physics'")
    print(f"  premise is self-consistent.")
elif r_final > 1:
    print(f"  The Dynamic Ma equilibrium is still self-intersecting (r > 1).")
    print(f"  The eigenvalue minimum on the embedded metric drives r toward")
    print(f"  large values. The self-intersection problem persists.")
print()
print(f"  NOTE: This optimization minimizes the embedded-metric eigenvalue.")
print(f"  A physical equilibrium also requires a restoring force model.")
print(f"  Without a restoring force, the eigenvalue always decreases with")
print(f"  deformation (the photon can always find a more comfortable shape).")
print(f"  The true equilibrium balances eigenvalue reduction against the")
print(f"  restoring force cost — this requires future work.")
