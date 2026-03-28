#!/usr/bin/env python3
"""
R40 Track 2: Self-consistent tube cross-section shape.

Find the cross-section that minimizes mode energy subject to a fixed
total path length (Compton constraint).  The photon "wants" to live
on the shape where its radiation pressure is most uniformly
distributed — that's the energy minimum.

METHOD
======
1. Parameterize the cross-section as a Fourier series in θ₁:
     ρ(θ₁) = a₀ + Σ aₖ cos(kθ₁)
   (sin terms omitted: top-bottom symmetry from F4 kills odd k
    and sin components).

2. Build the surface of revolution from this cross-section.

3. Compute the (1,2) geodesic path length on the surface.
   Rescale ρ so the path length = λ_C (Compton constraint).

4. Solve the 1D wave equation (Helmholtz on the cross-section)
   for the (1,2) mode.

5. Compute the mode energy (eigenvalue).

6. Minimize the mode energy over the shape parameters (a₂, a₄).

The key insight: on a FLAT torus, the mode energy is fixed by the
Compton constraint.  On a DEFORMED surface, modes on different shapes
at the same path length have different energies.  The shape that
minimizes energy is the equilibrium.
"""

import sys
import os
import math

import numpy as np
from scipy.optimize import minimize
from scipy import linalg

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model import solve_shear_for_alpha, mu_12, M_P_MEV

HBAR_C_FM = 197.3269804


# ══════════════════════════════════════════════════════════════════════
#  Proton sheet geometry
# ══════════════════════════════════════════════════════════════════════

R_P = 8.906
s56 = solve_shear_for_alpha(R_P)
mu_p = mu_12(R_P, s56)
E0_p = M_P_MEV / mu_p
L_ring = 2 * math.pi * HBAR_C_FM / E0_p
L_tube = R_P * L_ring

R_major = L_ring / (2 * math.pi)
a_minor = L_tube / (2 * math.pi)

n1, n2 = 1, 2
N_THETA = 256   # angular grid for the cross-section


print("=" * 70)
print("R40 Track 2: Self-consistent cross-section shape")
print("=" * 70)
print()
print(f"Proton torus: a = {a_minor:.4f} fm, R = {R_major:.4f} fm, a/R = {a_minor/R_major:.3f}")
print(f"Mode: ({n1},{n2})")
print()


# ══════════════════════════════════════════════════════════════════════
#  Cross-section parameterization
# ══════════════════════════════════════════════════════════════════════

def cross_section_radius(theta1, a0, coeffs):
    """
    Cross-section radius as a function of tube angle.

    r(θ₁) = a₀ + Σ aₖ cos(kθ₁) for k = 2, 4, 6, ...

    Only even cosine terms (top-bottom and left-right symmetry).

    Parameters
    ----------
    theta1 : ndarray — tube angles
    a0 : float — mean radius
    coeffs : list/array — [a₂, a₄, a₆, ...]

    Returns
    -------
    ndarray — radius at each angle
    """
    r = np.full_like(theta1, a0)
    for i, ak in enumerate(coeffs):
        k = 2 * (i + 1)   # k = 2, 4, 6, ...
        r = r + ak * np.cos(k * theta1)
    return r


def geodesic_path_length(a0, coeffs, R, n1, n2, N=1000):
    """
    Path length of the (n1, n2) geodesic on the deformed torus.

    The surface of revolution has cross-section radius r(θ₁).
    The major radius at tube angle θ₁ is ρ(θ₁) = R + r(θ₁) cos θ₁.
    (This is the standard torus parameterization with non-circular
    cross-section.)

    The geodesic θ₁ = n₁t, θ₂ = n₂t has path element:
      ds² = (n₁ r'(θ₁))² + (n₁ r(θ₁))² + (n₂ ρ(θ₁))²   [approx]

    More precisely, for the surface parameterized as:
      x = ρ(θ₁) cos θ₂,  y = ρ(θ₁) sin θ₂,  z = r(θ₁) sin θ₁

    Actually, for a general cross-section r(θ₁), the 3D position is:
      x = (R + r(θ₁) cos θ₁) cos θ₂
      y = (R + r(θ₁) cos θ₁) sin θ₂
      z = r(θ₁) sin θ₁

    ds/dt for the geodesic θ₁ = n₁t, θ₂ = n₂t:
      dx/dt = d/dt[(R + r cos θ₁) cos θ₂]
            = [(-r sin θ₁ + r' cos θ₁) n₁ cos θ₂ - (R + r cos θ₁) n₂ sin θ₂]
    etc.  Compute numerically.
    """
    t = np.linspace(0, 2 * math.pi, N, endpoint=False)
    dt = t[1] - t[0]
    th1 = n1 * t
    th2 = n2 * t

    r_vals = cross_section_radius(th1, a0, coeffs)

    # dr/dθ₁ (derivative of cross-section radius)
    dr = np.zeros_like(th1)
    for i, ak in enumerate(coeffs):
        k = 2 * (i + 1)
        dr = dr - k * ak * np.sin(k * th1)

    rho = R + r_vals * np.cos(th1)

    # 3D position derivatives
    dx = n1 * (-r_vals * np.sin(th1) + dr * np.cos(th1)) * np.cos(th2) \
         - n2 * rho * np.sin(th2)
    dy = n1 * (-r_vals * np.sin(th1) + dr * np.cos(th1)) * np.sin(th2) \
         + n2 * rho * np.cos(th2)
    dz = n1 * (r_vals * np.cos(th1) + dr * np.sin(th1))

    speed = np.sqrt(dx**2 + dy**2 + dz**2)
    return np.sum(speed) * dt


def mode_energy_on_shape(a0, coeffs, R, n1, n2, N_grid=256):
    """
    Compute the (n1, n2) mode energy on a deformed torus.

    The deformed torus has cross-section radius r(θ₁) and major
    radius ρ(θ₁) = R + r(θ₁) cos θ₁.

    The metric on the surface of revolution is:
      ds² = g₁₁ dθ₁² + g₂₂ dθ₂²
    where:
      g₁₁ = (dr/dθ₁ cos θ₁ - r sin θ₁)² + (dr/dθ₁ sin θ₁ + r cos θ₁)²
           = r² + (dr/dθ₁)²
      g₂₂ = ρ² = (R + r cos θ₁)²

    For ψ = f(θ₁) e^{in₂θ₂}, the eigenvalue equation is:
      -1/√g d/dθ₁[√g g²²/g₁₁ df/dθ₁] + n₂² g₁₁/g₂₂ f = λ f

    Actually, in Sturm-Liouville form for a surface of revolution:
      d/dθ₁[p(θ₁) df/dθ₁] + [λ w(θ₁) - q(θ₁)] f = 0
    where:
      p = ρ / √g₁₁  (= √g₂₂ / √g₁₁ × something)

    Let me use the standard form.  The Laplacian on a surface of
    revolution with metric ds² = A(θ₁)² dθ₁² + B(θ₁)² dθ₂² is:
      Δψ = 1/(AB) [∂/∂θ₁(B/A ∂ψ/∂θ₁) + ∂/∂θ₂(A/B ∂ψ/∂θ₂)]

    With ψ = f(θ₁) e^{in₂θ₂}:
      1/(AB) [d/dθ₁(B/A df/dθ₁) - n₂² A/B f] = -k² f

    Multiply by AB:
      d/dθ₁(B/A df/dθ₁) - n₂² A²/B f = -k² AB f

    Rearrange to S-L form:
      d/dθ₁[p df/dθ₁] + [λ w - q] f = 0

    where p = B/A, w = AB (= √det g), q = n₂² A/B,  λ = k².

    Here:
      A = √g₁₁ = √(r² + r'²)
      B = √g₂₂ = |ρ| = |R + r cos θ₁|
    """
    theta1 = np.linspace(0, 2 * math.pi, N_grid, endpoint=False)
    h = 2 * math.pi / N_grid

    r_vals = cross_section_radius(theta1, a0, coeffs)

    # dr/dθ₁
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

    # Check for problematic values
    if np.any(B < 1e-10) or np.any(A < 1e-10):
        return 1e10  # invalid shape

    if np.any(w <= 0):
        return 1e10

    # Build S-L matrices
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

    # Check W positive-definite
    if np.any(np.diag(W_mat) <= 0):
        return 1e10

    try:
        eigvals = linalg.eigh(S_mat, W_mat, eigvals_only=True)
    except Exception:
        return 1e10

    # The n₁=1 sin-like mode is at index 2
    idx = 2 * n1
    if idx >= len(eigvals):
        return 1e10

    return eigvals[idx]


# ══════════════════════════════════════════════════════════════════════
#  Section 1: Validate on the circular cross-section
# ══════════════════════════════════════════════════════════════════════

print("-" * 70)
print("Section 1: Baseline — circular cross-section")
print("-" * 70)
print()

path_circ = geodesic_path_length(a_minor, [], R_major, n1, n2)
lambda_circ = mode_energy_on_shape(a_minor, [], R_major, n1, n2, N_THETA)

print(f"  Circular: a₀ = {a_minor:.4f} fm")
print(f"  Path length: {path_circ:.4f} fm")
print(f"  Mode eigenvalue λ: {lambda_circ:.6f}")
print()

# Flat-torus reference
eps = a_minor / R_major
lambda_flat = n1**2 + eps**2 * n2**2
print(f"  Flat-torus eigenvalue: {lambda_flat:.6f}")
print(f"  Curved/flat ratio: {lambda_circ/lambda_flat:.6f}")
print()


# ══════════════════════════════════════════════════════════════════════
#  Section 2: Energy landscape — sweep a₂ deformation
# ══════════════════════════════════════════════════════════════════════

print("-" * 70)
print("Section 2: Energy landscape — sweep elliptical deformation a₂")
print("-" * 70)
print()

# The k=2 harmonic (cos 2θ₁) makes the cross-section elliptical.
# Positive a₂: wider at θ₁ = 0, π (equators); narrower at π/2, 3π/2.
# Negative a₂: narrower at equators, wider at poles.

print(f"  Sweeping a₂ from -0.4a to +0.4a, rescaling a₀ to preserve")
print(f"  path length at each point.")
print()
print(f"  {'a₂/a':>8}  {'a₀ (fm)':>10}  {'path (fm)':>10}  {'λ':>12}  {'Δλ/λ₀':>10}")
print(f"  {'─'*8}  {'─'*10}  {'─'*10}  {'─'*12}  {'─'*10}")

a2_fractions = np.linspace(-0.4, 0.4, 21)
results = []

for a2_frac in a2_fractions:
    a2 = a2_frac * a_minor
    coeffs = [a2]

    # Rescale a₀ to preserve path length
    # Simple approach: binary search for a₀ that gives the right path length
    target_path = path_circ

    def path_residual(a0_trial):
        return geodesic_path_length(a0_trial, coeffs, R_major, n1, n2) - target_path

    # Bracket
    a0_lo, a0_hi = 0.1 * a_minor, 2.0 * a_minor
    from scipy.optimize import brentq
    try:
        a0_opt = brentq(path_residual, a0_lo, a0_hi, xtol=1e-6)
    except Exception:
        continue

    path = geodesic_path_length(a0_opt, coeffs, R_major, n1, n2)
    lam = mode_energy_on_shape(a0_opt, coeffs, R_major, n1, n2, N_THETA)

    if lam > 1e9:
        continue

    delta = (lam - lambda_circ) / lambda_circ
    print(f"  {a2_frac:+8.3f}  {a0_opt:10.4f}  {path:10.4f}  {lam:12.6f}  {delta:+10.6f}")
    results.append((a2_frac, a0_opt, lam, delta))

results = np.array(results)

if len(results) > 3:
    # Find the minimum
    min_idx = np.argmin(results[:, 2])
    print()
    print(f"  Minimum λ at a₂/a = {results[min_idx, 0]:+.3f}")
    print(f"    a₀ = {results[min_idx, 1]:.4f} fm")
    print(f"    λ = {results[min_idx, 2]:.6f}")
    print(f"    Δλ/λ₀ = {results[min_idx, 3]:+.6f} ({results[min_idx, 3]*100:+.4f}%)")

    # Is the minimum at a₂ = 0 (circular) or elsewhere?
    if abs(results[min_idx, 0]) < 0.01:
        print()
        print("  → The circular cross-section IS the energy minimum.")
        print("    The surface does not want to deform (at constant path length).")
    else:
        print()
        print(f"  → The energy minimum is at a₂/a = {results[min_idx, 0]:+.3f}.")
        print(f"    The surface WANTS to become elliptical.")
        ellipticity = results[min_idx, 0]
        if ellipticity > 0:
            print(f"    Elongated at equators (θ₁ = 0, π), compressed at poles.")
        else:
            print(f"    Compressed at equators, elongated at poles.")


# ══════════════════════════════════════════════════════════════════════
#  Section 3: Two-parameter optimization (a₂, a₄)
# ══════════════════════════════════════════════════════════════════════

print()
print("-" * 70)
print("Section 3: Two-parameter optimization (a₂, a₄)")
print("-" * 70)
print()

def objective(params):
    """Minimize mode energy at fixed path length."""
    a2_frac, a4_frac = params
    a2 = a2_frac * a_minor
    a4 = a4_frac * a_minor
    coeffs = [a2, a4]

    # Check that cross-section stays positive everywhere
    theta_test = np.linspace(0, 2 * math.pi, 100)
    r_test = cross_section_radius(theta_test, a_minor, coeffs)
    if np.any(r_test < 0.05 * a_minor):
        return 1e10

    # Rescale a₀ to preserve path length
    target_path = path_circ

    def path_residual(a0_trial):
        return geodesic_path_length(a0_trial, [a2, a4], R_major, n1, n2) - target_path

    try:
        a0_opt = brentq(path_residual, 0.2 * a_minor, 3.0 * a_minor, xtol=1e-6)
    except Exception:
        return 1e10

    lam = mode_energy_on_shape(a0_opt, [a2, a4], R_major, n1, n2, N_THETA)
    return lam

print("  Optimizing over (a₂/a, a₄/a) with a₀ adjusted for constant path length...")
print()

result = minimize(objective, [0.0, 0.0], method='Nelder-Mead',
                  options={'xatol': 1e-5, 'fatol': 1e-8, 'maxiter': 500})

a2_opt, a4_opt = result.x
print(f"  Optimal a₂/a = {a2_opt:+.6f}")
print(f"  Optimal a₄/a = {a4_opt:+.6f}")
print(f"  Mode eigenvalue: {result.fun:.8f}")
print(f"  Circular eigenvalue: {lambda_circ:.8f}")
print(f"  Energy change: {(result.fun - lambda_circ)/lambda_circ*100:+.6f}%")
print(f"  Converged: {result.success}")
print()

# Reconstruct the optimal shape
a2_fm = a2_opt * a_minor
a4_fm = a4_opt * a_minor
coeffs_opt = [a2_fm, a4_fm]

def path_res_opt(a0):
    return geodesic_path_length(a0, coeffs_opt, R_major, n1, n2) - path_circ

try:
    a0_final = brentq(path_res_opt, 0.2 * a_minor, 3.0 * a_minor, xtol=1e-6)
except Exception:
    a0_final = a_minor

print(f"  Final shape parameters:")
print(f"    a₀ = {a0_final:.4f} fm (mean radius)")
print(f"    a₂ = {a2_fm:+.4f} fm ({a2_opt*100:+.3f}% of a)")
print(f"    a₄ = {a4_fm:+.4f} fm ({a4_opt*100:+.3f}% of a)")

# Show the cross-section shape
theta_plot = np.linspace(0, 2 * math.pi, 36, endpoint=False)
r_opt = cross_section_radius(theta_plot, a0_final, coeffs_opt)
r_circ = np.full_like(theta_plot, a_minor)

print()
print(f"  Cross-section radius r(θ₁):")
print(f"  {'θ₁/π':>8}  {'r_circle':>10}  {'r_opt':>10}  {'Δr/a':>10}  location")
print(f"  {'─'*8}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*12}")

for i, (th, rc, ro) in enumerate(zip(theta_plot, r_circ, r_opt)):
    dr = (ro - rc) / a_minor
    loc = ""
    if abs(th) < 0.1 or abs(th - 2*math.pi) < 0.1:
        loc = "outer eq."
    elif abs(th - math.pi/2) < 0.1:
        loc = "top"
    elif abs(th - math.pi) < 0.1:
        loc = "inner eq."
    elif abs(th - 3*math.pi/2) < 0.1:
        loc = "bottom"
    if i % 3 == 0:
        print(f"  {th/math.pi:8.4f}  {rc:10.4f}  {ro:10.4f}  {dr:+10.4f}  {loc}")


# ══════════════════════════════════════════════════════════════════════
#  Summary
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("Track 2 Summary")
print("=" * 70)
print()

energy_shift = (result.fun - lambda_circ) / lambda_circ * 100

if abs(a2_opt) < 0.001 and abs(a4_opt) < 0.001:
    print("The circular cross-section IS the energy minimum (to within 0.1%).")
    print("The torus does not want to deform at constant path length.")
    print("The flat-torus approximation is validated.")
elif abs(energy_shift) < 0.01:
    print(f"The optimal shape has a₂/a = {a2_opt:+.4f}, a₄/a = {a4_opt:+.4f}.")
    print(f"But the energy change is only {energy_shift:+.4f}% — negligible.")
    print(f"The circular shape is nearly optimal; deformation is a tiny correction.")
else:
    print(f"The optimal shape is MEASURABLY non-circular:")
    print(f"  a₂/a = {a2_opt:+.4f} (elliptical deformation)")
    print(f"  a₄/a = {a4_opt:+.4f} (square deformation)")
    print(f"  Energy shift: {energy_shift:+.4f}%")
    print()
    if a2_opt > 0:
        print(f"The tube cross-section elongates at the equators (θ₁ = 0, π)")
        print(f"and compresses at the poles (θ₁ = π/2, 3π/2).")
    else:
        print(f"The tube cross-section compresses at the equators")
        print(f"and elongates at the poles.")
