#!/usr/bin/env python3
"""
R40 Track 5: Surface tension estimate and low-pass filter effect.

Surface tension creates a restoring pressure P = σ × κ, where κ is the
curvature of the cross-section.  For a perturbation at Fourier harmonic
k on a circle of radius a₀:

    κ(θ₁) ≈ 1/a₀ + (k² - 1) aₖ cos(kθ₁) / a₀²

So the restoring pressure for harmonic k is:

    P_restore(k) = σ (k² - 1) aₖ / a₀²

This is a LOW-PASS FILTER: the restoring force grows as k².

    k=2: restoring ∝ 3   (elliptical — easiest to deform)
    k=4: restoring ∝ 15  (square — 5× harder)
    k=6: restoring ∝ 35  (hexagonal — 12× harder)

We can estimate σ from the Track 1 pressure and Track 2 shape:
at equilibrium, P_rad(k) = σ (k² - 1) aₖ / a₀², so:

    σ = P_rad(k) × a₀² / ((k² - 1) × aₖ)

If this gives a consistent σ across harmonics, surface tension is
a valid restoring model.  Then we can predict how the shape changes
with surface tension, and quantify the ghost suppression.
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

# ── Geometry ──────────────────────────────────────────────────────

R_P = 8.906
s56 = solve_shear_for_alpha(R_P)
mu_p = mu_12(R_P, s56)
E0_p = M_P_MEV / mu_p
L_ring = 2 * math.pi * HBAR_C_FM / E0_p
L_tube = R_P * L_ring
R_major = L_ring / (2 * math.pi)
a_minor = L_tube / (2 * math.pi)

n1_mode, n2_mode = 1, 2
N_GRID = 256

# ── Track 1 pressure Fourier coefficients (recomputed) ───────────

def compute_pressure_fourier(a0, coeffs, R, n1, n2, N_pts=4000):
    """Compute radiation pressure and return Fourier cosine coefficients."""
    t = np.linspace(0, 2 * math.pi, N_pts, endpoint=False)
    dt = t[1] - t[0]
    th1 = n1 * t
    th2 = n2 * t

    r_vals = a0 + sum(ak * np.cos(2*(i+1)*th1) for i, ak in enumerate(coeffs)) \
             if coeffs else np.full(N_pts, a0)

    dr = sum(-2*(i+1)*ak * np.sin(2*(i+1)*th1) for i, ak in enumerate(coeffs)) \
         if coeffs else np.zeros(N_pts)

    rho = R + r_vals * np.cos(th1)

    dxdt = n1 * (-r_vals * np.sin(th1) + dr * np.cos(th1)) * np.cos(th2) \
           - n2 * rho * np.sin(th2)
    dydt = n1 * (-r_vals * np.sin(th1) + dr * np.cos(th1)) * np.sin(th2) \
           + n2 * rho * np.cos(th2)
    dzdt = n1 * (r_vals * np.cos(th1) + dr * np.sin(th1))

    speed = np.sqrt(dxdt**2 + dydt**2 + dzdt**2)
    T_hat = np.stack([dxdt, dydt, dzdt], axis=-1) / speed[:, None]

    dT = np.zeros_like(T_hat)
    for j in range(3):
        dT[:, j] = np.gradient(T_hat[:, j], dt)
    kappa_vec = dT / speed[:, None]

    e_r = np.stack([
        np.cos(th1) * np.cos(th2),
        np.cos(th1) * np.sin(th2),
        np.sin(th1),
    ], axis=-1)

    kappa_radial = np.sum(kappa_vec * e_r, axis=1)
    F_outward = -kappa_radial * speed

    # Bin by θ₁
    N_BINS = 256
    theta1_bins = np.linspace(0, 2 * math.pi, N_BINS, endpoint=False)
    F_binned = np.zeros(N_BINS)
    counts = np.zeros(N_BINS)
    th1_mod = th1 % (2 * math.pi)
    for i in range(N_pts):
        idx = int(th1_mod[i] / (2 * math.pi) * N_BINS) % N_BINS
        F_binned[idx] += F_outward[i]
        counts[idx] += 1
    mask = counts > 0
    F_binned[mask] /= counts[mask]

    # Fourier
    A = {}
    A[0] = np.mean(F_binned[mask])
    for k in range(1, 9):
        A[k] = 2 * np.mean(F_binned[mask] * np.cos(k * theta1_bins[mask]))
    return A


# ── Shape optimization with surface tension ───────────────────────

def cross_section_radius(theta1, a0, coeffs):
    r = np.full_like(theta1, a0, dtype=float)
    for i, ak in enumerate(coeffs):
        k = 2 * (i + 1)
        r = r + ak * np.cos(k * theta1)
    return r


def geodesic_path_length(a0, coeffs, R, n1, n2, N=1000):
    t = np.linspace(0, 2 * math.pi, N, endpoint=False)
    dt = t[1] - t[0]
    th1 = n1 * t; th2 = n2 * t
    r_vals = cross_section_radius(th1, a0, coeffs)
    dr = sum(-2*(i+1)*ak * np.sin(2*(i+1)*th1) for i, ak in enumerate(coeffs)) \
         if coeffs else np.zeros(N)
    rho = R + r_vals * np.cos(th1)
    dx = n1*(-r_vals*np.sin(th1)+dr*np.cos(th1))*np.cos(th2) - n2*rho*np.sin(th2)
    dy = n1*(-r_vals*np.sin(th1)+dr*np.cos(th1))*np.sin(th2) + n2*rho*np.cos(th2)
    dz = n1*(r_vals*np.cos(th1)+dr*np.sin(th1))
    return np.sum(np.sqrt(dx**2+dy**2+dz**2)) * dt


def solve_eigenvalue(a0, coeffs, R, n1, n2, N_grid=256):
    theta1 = np.linspace(0, 2*math.pi, N_grid, endpoint=False)
    h = 2*math.pi/N_grid
    r_vals = cross_section_radius(theta1, a0, coeffs)
    dr = sum(-2*(i+1)*ak*np.sin(2*(i+1)*theta1) for i, ak in enumerate(coeffs)) \
         if coeffs else np.zeros(N_grid)
    A_m = np.sqrt(r_vals**2 + dr**2)
    rho = R + r_vals*np.cos(theta1)
    B_m = np.abs(rho)
    p = B_m/A_m; w = A_m*B_m; q = n2**2*A_m/B_m
    if np.any(B_m < 1e-10) or np.any(w <= 0): return 1e10
    php = np.array([(p[j]+p[(j+1)%N_grid])/2 for j in range(N_grid)])
    phm = np.array([(p[j]+p[(j-1)%N_grid])/2 for j in range(N_grid)])
    S = np.zeros((N_grid, N_grid)); W = np.diag(w)
    for j in range(N_grid):
        S[j,(j-1)%N_grid] = -phm[j]/h**2
        S[j,j] = (phm[j]+php[j])/h**2 + q[j]
        S[j,(j+1)%N_grid] = -php[j]/h**2
    try:
        eigvals = linalg.eigh(S, W, eigvals_only=True)
    except: return 1e10
    idx = 2*n1
    return eigvals[idx] if idx < len(eigvals) else 1e10


def perimeter_of_cross_section(a0, coeffs, N=500):
    """Perimeter of the cross-section curve (for surface tension energy)."""
    theta1 = np.linspace(0, 2*math.pi, N, endpoint=False)
    dt = 2*math.pi/N
    r_vals = cross_section_radius(theta1, a0, coeffs)
    dr = sum(-2*(i+1)*ak*np.sin(2*(i+1)*theta1) for i, ak in enumerate(coeffs)) \
         if coeffs else np.zeros(N)
    # ds = √(r² + r'²) dθ  (for a curve r(θ) in polar-like coords)
    ds = np.sqrt(r_vals**2 + dr**2)
    return np.sum(ds) * dt


# ══════════════════════════════════════════════════════════════════════

print("=" * 70)
print("R40 Track 5: Surface tension and low-pass filter")
print("=" * 70)
print()

# ── Section 1: Estimate σ from Track 1 pressure + Track 2 shape ──

print("-" * 70)
print("Section 1: Surface tension estimate from pressure/deformation ratio")
print("-" * 70)
print()

# Track 1 pressure on circular torus
P_fourier = compute_pressure_fourier(a_minor, [], R_major, n1_mode, n2_mode)

# Track 2 optimal shape
a2_track2 = +0.056426 * a_minor
a4_track2 = -0.195744 * a_minor
a0_track2 = 3.4411

print(f"  Track 1 pressure Fourier on circular torus:")
print(f"    P₀ (mean) = {P_fourier[0]:.6e}")
print(f"    P₂ (k=2)  = {P_fourier[2]:.6e}")
print(f"    P₄ (k=4)  = {P_fourier[4]:.6e}")
print(f"    P₆ (k=6)  = {P_fourier[6]:.6e}")
print()
print(f"  Track 2 deformation amplitudes:")
print(f"    a₂ = {a2_track2:+.4f} fm  ({a2_track2/a_minor:+.4f} a)")
print(f"    a₄ = {a4_track2:+.4f} fm  ({a4_track2/a_minor:+.4f} a)")
print()

# Surface tension model: at equilibrium on the deformed shape,
# P_rad(k) = σ (k² - 1) aₖ / a₀²
#
# Linearized (small deformation): use the circular-torus pressure
# as the driving force and the Track 2 amplitudes as the response.

print(f"  Surface tension low-pass filter:")
print(f"  P_restore(k) = σ × (k²-1) × aₖ / a₀²")
print()
print(f"  {'k':>4}  {'k²-1':>6}  {'Pₖ':>12}  {'aₖ (fm)':>10}  "
      f"{'σ estimate':>12}  {'filter':>8}")
print(f"  {'─'*4}  {'─'*6}  {'─'*12}  {'─'*10}  {'─'*12}  {'─'*8}")

sigma_estimates = []
for k, ak in [(2, a2_track2), (4, a4_track2)]:
    Pk = P_fourier[k]
    k2m1 = k**2 - 1
    if abs(ak) > 1e-10:
        sigma = Pk * a0_track2**2 / (k2m1 * ak)
        sigma_estimates.append(sigma)
        filt = f"1/{k2m1}"
    else:
        sigma = float('nan')
        filt = "—"
    print(f"  {k:4d}  {k2m1:6d}  {Pk:12.6e}  {ak:+10.4f}  {sigma:12.4e}  {filt:>8}")

print()
if len(sigma_estimates) >= 2:
    s2, s4 = sigma_estimates[0], sigma_estimates[1]
    print(f"  σ from k=2: {s2:.4e}")
    print(f"  σ from k=4: {s4:.4e}")
    print(f"  Ratio σ₄/σ₂: {s4/s2:.4f}" if s2 != 0 else "")
    print()
    if abs(s4/s2 - 1) < 0.3:
        print(f"  σ is roughly CONSISTENT across harmonics.")
        print(f"  Surface tension is a plausible restoring model.")
        sigma_mean = (s2 + s4) / 2
    else:
        print(f"  σ VARIES across harmonics (ratio ≠ 1).")
        print(f"  Pure surface tension is not the full story,")
        print(f"  but the k² scaling still provides a low-pass filter.")
        sigma_mean = abs(s2)  # use k=2 as reference


# ── Section 2: Low-pass filter effect on ghost modes ─────────────

print()
print("-" * 70)
print("Section 2: Low-pass filter effect on mode stability")
print("-" * 70)
print()

print(f"  The surface tension restoring force scales as (k²-1).")
print(f"  For each mode, the DOMINANT pressure harmonic determines")
print(f"  which deformation it drives.  Higher-k modes fight stronger")
print(f"  restoring force → harder to deform → higher energy penalty.")
print()

# For each mode, compute its pressure Fourier spectrum and
# determine the dominant harmonic.  The "deformation cost" is
# proportional to (k_dominant² - 1) relative to the (1,2) mode's k=2.

modes_to_test = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
    (2, 2), (2, 3), (2, 4),
    (3, 2), (3, 3),
]

print(f"  {'(n₁,n₂)':>8}  {'k_dom':>6}  {'|Pₖ|/P₀':>10}  "
      f"{'k²-1':>6}  {'filter penalty':>15}  {'suppressed?':>12}")
print(f"  {'─'*8}  {'─'*6}  {'─'*10}  {'─'*6}  {'─'*15}  {'─'*12}")

ref_filter = 3  # k=2, k²-1=3 (the (1,2) mode's dominant harmonic)

for n1_t, n2_t in modes_to_test:
    P = compute_pressure_fourier(a_minor, [], R_major, n1_t, n2_t)

    # Find dominant harmonic (among even k, which are the ones that
    # preserve the symmetry)
    harmonics = {}
    for k in [2, 4, 6, 8]:
        if abs(P[0]) > 1e-15:
            harmonics[k] = abs(P[k]) / abs(P[0])
        else:
            harmonics[k] = 0

    k_dom = max(harmonics, key=harmonics.get)
    Pk_rel = harmonics[k_dom]
    k2m1 = k_dom**2 - 1
    penalty = k2m1 / ref_filter

    suppressed = "YES" if penalty > 2.0 else ("mild" if penalty > 1.3 else "no")

    print(f"  ({n1_t},{n2_t})     {k_dom:6d}  {Pk_rel:10.4f}  "
          f"{k2m1:6d}  {penalty:15.1f}×  {suppressed:>12}")


# ── Section 3: Shape optimization WITH surface tension ────────────

print()
print("-" * 70)
print("Section 3: Optimal shape with surface tension penalty")
print("-" * 70)
print()

# Add a surface tension energy to the mode eigenvalue:
#   E_total = λ_mode + σ_eff × (perimeter - perimeter_circle)
#
# The surface tension penalizes shapes whose cross-section perimeter
# exceeds the circle's.

perimeter_circ = 2 * math.pi * a_minor
path_circ = geodesic_path_length(a_minor, [], R_major, n1_mode, n2_mode)
lambda_circ = solve_eigenvalue(a_minor, [], R_major, n1_mode, n2_mode, N_GRID)

# Try several values of σ_eff to see the effect
sigma_values = [0.0, 0.01, 0.05, 0.1, 0.5, 1.0, 5.0]

print(f"  σ_eff sweep: minimize (λ_mode + σ × ΔPerimeter) at constant path length")
print(f"  Reference: circular λ = {lambda_circ:.6f}, perimeter = {perimeter_circ:.4f} fm")
print()
print(f"  {'σ_eff':>8}  {'a₂/a':>8}  {'a₄/a':>8}  {'λ_mode':>10}  "
      f"{'ΔPerim':>8}  {'E_total':>10}  {'ΔE/E₀':>10}")
print(f"  {'─'*8}  {'─'*8}  {'─'*8}  {'─'*10}  {'─'*8}  {'─'*10}  {'─'*10}")

for sigma_eff in sigma_values:
    def objective_st(params):
        a2 = params[0] * a_minor
        a4 = params[1] * a_minor
        coeffs = [a2, a4]

        theta_test = np.linspace(0, 2*math.pi, 100)
        r_test = cross_section_radius(theta_test, a_minor, coeffs)
        if np.any(r_test < 0.05 * a_minor):
            return 1e10

        try:
            a0 = brentq(
                lambda a0_t: geodesic_path_length(a0_t, coeffs, R_major, n1_mode, n2_mode) - path_circ,
                0.1*a_minor, 4.0*a_minor, xtol=1e-6)
        except:
            return 1e10

        lam = solve_eigenvalue(a0, coeffs, R_major, n1_mode, n2_mode, N_GRID)
        if lam > 1e9:
            return 1e10

        perim = perimeter_of_cross_section(a0, coeffs)
        d_perim = perim - perimeter_circ

        return lam + sigma_eff * d_perim

    res = minimize(objective_st, [0.0, 0.0], method='Nelder-Mead',
                   options={'xatol': 1e-5, 'fatol': 1e-8, 'maxiter': 300})

    a2_opt = res.x[0]
    a4_opt = res.x[1]
    coeffs_opt = [a2_opt * a_minor, a4_opt * a_minor]

    try:
        a0_f = brentq(
            lambda a0_t: geodesic_path_length(a0_t, coeffs_opt, R_major, n1_mode, n2_mode) - path_circ,
            0.1*a_minor, 4.0*a_minor, xtol=1e-6)
    except:
        a0_f = a_minor

    lam_f = solve_eigenvalue(a0_f, coeffs_opt, R_major, n1_mode, n2_mode, N_GRID)
    perim_f = perimeter_of_cross_section(a0_f, coeffs_opt)
    d_perim = perim_f - perimeter_circ
    E_total = lam_f + sigma_eff * d_perim
    dE = (E_total - lambda_circ) / lambda_circ

    print(f"  {sigma_eff:8.3f}  {a2_opt:+8.4f}  {a4_opt:+8.4f}  {lam_f:10.6f}  "
          f"{d_perim:+8.3f}  {E_total:10.6f}  {dE:+10.4f}")


# ══════════════════════════════════════════════════════════════════════
#  Summary
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("Track 5 Summary")
print("=" * 70)
print()
print(f"1. SURFACE TENSION ESTIMATE")
print(f"   From k=2 pressure/deformation: σ₂ = {sigma_estimates[0]:.4e}" if sigma_estimates else "")
print(f"   From k=4 pressure/deformation: σ₄ = {sigma_estimates[1]:.4e}" if len(sigma_estimates) > 1 else "")
print()
print(f"2. LOW-PASS FILTER")
print(f"   Restoring force scales as k²−1:")
print(f"     k=2 (elliptical): 3  (reference)")
print(f"     k=4 (square):     15 (5× harder)")
print(f"     k=6 (hexagonal):  35 (12× harder)")
print(f"     k=8:              63 (21× harder)")
print(f"   High-n₂ modes that drive k=4+ deformations are penalized.")
print()
print(f"3. EFFECT ON DEFORMATION")
print(f"   Surface tension suppresses high-k shape harmonics,")
print(f"   making the equilibrium shape smoother (more elliptical,")
print(f"   less 4-lobed) and closer to circular at high σ.")
print(f"   At high σ, the (1,2) mode's own shape advantage vanishes")
print(f"   and all modes live on near-circular tori.")
