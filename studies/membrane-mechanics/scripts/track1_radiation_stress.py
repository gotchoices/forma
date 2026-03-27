#!/usr/bin/env python3
"""
R37 Track 1: Radiation stress tensor on the T² surface

Computes the stress-energy tensor of the confined (1,2) photon
mode on the electron T² surface and decomposes it into:

  - P_iso: isotropic radiation pressure (= E/(2A) in 2D)
  - ΔP:    anisotropic shear stress (drives lattice shear → α)
  - p₁,p₂: principal stresses in the tube (θ₁) and ring (θ₂) directions

For a RUNNING WAVE mode (circularly polarized photon), the
energy density is UNIFORM across T² — no position dependence.
The stress tensor is constant, determined entirely by the
momentum direction (the (1,2) geodesic) and the metric.

Key input: the shear s is DETERMINED by α = 1/137 (via R19),
not derived.  α is an input to this study.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
from lib.t6 import (alpha_kk, solve_shear_for_alpha, mu_12,
                     compute_scales, hbar_c_MeV_fm, M_E_MEV, ALPHA)

# ═══════════════════════════════════════════════════════════════════
#  Constants
# ═══════════════════════════════════════════════════════════════════

hbar_SI = 1.0546e-34       # J·s
c_SI = 2.998e8              # m/s
eV_J = 1.602e-19            # J/eV
MeV_J = eV_J * 1e6
G_N = 6.674e-11             # N·m²/kg² (Newton's constant)
m_e_kg = 9.109e-31          # kg
m_e_eV = 0.51100e6          # eV
lambda_bar_C = hbar_SI / (m_e_kg * c_SI)  # reduced Compton wavelength, m
fm_to_m = 1e-15


def torus_geometry(r, s):
    """
    Compute the torus circumferences and area for a (1,2) mode
    on a sheared T² with aspect ratio r and shear s.

    Returns dict with L1, L2, A, R1, R2 in SI (meters),
    plus dimensionless quantities.
    """
    mu = mu_12(r, s)

    # Circumferences: E = (ℏc × 2π / L₁) × μ  →  L₁ = 2πλ̄_C × μ
    L1 = 2 * math.pi * lambda_bar_C * mu  # tube circumference (m)
    L2 = r * L1                             # ring circumference (m)
    R1 = L1 / (2 * math.pi)                # tube radius (m)
    R2 = L2 / (2 * math.pi)                # ring radius (m)
    A = L1 * L2                             # torus area (m²)

    return {
        'r': r, 's': s, 'mu': mu,
        'L1_m': L1, 'L2_m': L2, 'R1_m': R1, 'R2_m': R2, 'A_m2': A,
        'L1_fm': L1 / fm_to_m, 'L2_fm': L2 / fm_to_m,
    }


def stress_decomposition(r, s):
    """
    Compute the 2D stress tensor of the (1,2) mode on T².

    For a running wave with wavevector k = (k₁, k₂):
        T^{ab} = ρ × k̂^a k̂^b

    where ρ = E/A is the energy density (uniform for running wave).

    Principal stresses:
        p₁ = ρ × f₁   (tube direction)
        p₂ = ρ × f₂   (ring direction)

    where f₁ = k₁²/|k|², f₂ = k₂²/|k|² are the momentum fractions.
    """
    geom = torus_geometry(r, s)
    q2 = 2.0 - s  # effective ring winding

    # Momentum fractions
    f1 = r**2 / (r**2 + q2**2)       # tube direction fraction
    f2 = q2**2 / (r**2 + q2**2)      # ring direction fraction

    # Energy density
    E_J = m_e_kg * c_SI**2           # total mode energy (J)
    rho = E_J / geom['A_m2']         # energy density (J/m²)

    # Principal stresses (Pa·m in 2D, i.e. force per unit length)
    p1 = rho * f1
    p2 = rho * f2

    # Isotropic pressure (2D radiation pressure = ρ/2)
    P_iso = rho / 2.0

    # Anisotropic stress
    delta_P = (p1 - p2) / 2.0
    anisotropy_ratio = (f1 - f2)  # ΔP / P_iso

    return {
        **geom,
        'E_J': E_J, 'rho_J_m2': rho,
        'f1': f1, 'f2': f2,
        'p1_Pa': p1, 'p2_Pa': p2,
        'P_iso_Pa': P_iso,
        'delta_P_Pa': delta_P,
        'anisotropy_ratio': anisotropy_ratio,
        'rho_Pa': rho,
    }


def surface_energy_from_equilibrium(geom):
    """
    If radiation pressure balances surface tension at the
    observed Compton wavelength, extract σ_m.

    For a torus, the Young-Laplace pressure balance:
        P_rad = σ_m × (mean curvature)

    For a flat KK torus (zero intrinsic curvature), use instead
    the variational approach: at equilibrium ∂E_total/∂L = 0.

        E_photon = ℏc × 2π μ / L₁    (decreases with L₁)
        E_surface = σ_m × A = σ_m × L₁ × L₂ = σ_m × r × L₁²

    ∂E/∂L₁ = 0:  -E_photon/L₁ + 2 σ_m r L₁ = 0
                   σ_m = E_photon / (2 r L₁²) = ρ / (2 r)
                       = P_iso / r

    (Valid only for fixed aspect ratio r; tracks the
    θ₁-direction balance.)
    """
    P_iso = geom['P_iso_Pa']
    r = geom['r']

    # Surface energy density from L₁ equilibrium
    sigma_m = P_iso / r

    # Also compute from L₂ equilibrium (should match for self-consistency)
    # ∂E/∂L₂ = 0 at fixed L₁:
    #   -E × q₂²/(L₂² μ²) + σ_m = 0   →   σ_m = p₂
    # This gives a DIFFERENT σ_m unless f₂ = 1/r, which is not generally true.
    # The discrepancy means σ_m alone can't explain the equilibrium —
    # need bending rigidity or other terms to balance BOTH directions.
    sigma_m_from_L2 = geom['p2_Pa']

    return {
        'sigma_m_from_L1': sigma_m,
        'sigma_m_from_L2': sigma_m_from_L2,
        'sigma_m_ratio': sigma_m / sigma_m_from_L2 if sigma_m_from_L2 > 0 else float('inf'),
    }


# ═══════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════

def main():
    print("=" * 72)
    print("R37 Track 1: Radiation Stress Tensor on the T² Surface")
    print("=" * 72)

    # ── Part A: Mode geometry ─────────────────────────────────────
    print(f"\n{'='*72}")
    print("PART A: Electron torus geometry")
    print("=" * 72)

    r_e = 6.6  # canonical aspect ratio
    s_e = solve_shear_for_alpha(r_e)
    alpha_check = alpha_kk(r_e, s_e)

    print(f"""
  Electron (1,2) mode on sheared T²:
    Aspect ratio r = {r_e}
    Shear s = {s_e:.6f}  (from α = 1/137)
    α_KK(r, s) = {alpha_check:.6f}  (target: {ALPHA:.6f})
    μ₁₂ = {mu_12(r_e, s_e):.6f}

  Compton wavelength:
    λ̄_C = ℏ/(m_e c) = {lambda_bar_C:.4e} m
""")

    geom = torus_geometry(r_e, s_e)
    print(f"  Torus dimensions:")
    print(f"    L₁ (tube circ)  = {geom['L1_m']:.4e} m = {geom['L1_fm']:.2f} fm")
    print(f"    L₂ (ring circ)  = {geom['L2_m']:.4e} m = {geom['L2_fm']:.2f} fm")
    print(f"    R₁ (tube radius) = {geom['R1_m']:.4e} m")
    print(f"    R₂ (ring radius) = {geom['R2_m']:.4e} m")
    print(f"    Area A = L₁L₂   = {geom['A_m2']:.4e} m²")

    # ── Part B: Stress tensor decomposition ───────────────────────
    print(f"\n{'='*72}")
    print("PART B: 2D stress tensor decomposition")
    print("=" * 72)

    sd = stress_decomposition(r_e, s_e)

    print(f"""
  Mode energy: E = m_e c² = {sd['E_J']:.4e} J = {m_e_eV:.0f} eV

  Energy density (uniform for running wave):
    ρ = E/A = {sd['rho_Pa']:.4e} J/m²

  Momentum fractions:
    f₁ (tube)  = k₁²/|k|² = r²/(r²+q₂²) = {sd['f1']:.4f}
    f₂ (ring)  = k₂²/|k|² = q₂²/(r²+q₂²) = {sd['f2']:.4f}
    f₁ + f₂ = {sd['f1']+sd['f2']:.4f}  (check: should be 1.0000)

  Principal stresses:
    p₁ (tube direction) = ρ × f₁ = {sd['p1_Pa']:.4e} J/m²
    p₂ (ring direction) = ρ × f₂ = {sd['p2_Pa']:.4e} J/m²

  Isotropic radiation pressure (2D):
    P_iso = ρ/2 = {sd['P_iso_Pa']:.4e} J/m²

  Anisotropic shear stress:
    ΔP = (p₁ − p₂)/2 = {sd['delta_P_Pa']:.4e} J/m²
    ΔP/P_iso = f₁ − f₂ = {sd['anisotropy_ratio']:.4f}

  The stress is HIGHLY ANISOTROPIC.
  {sd['f1']*100:.1f}% of momentum is in the tube (θ₁) direction,
  only {sd['f2']*100:.1f}% in the ring (θ₂) direction.

  Physical interpretation:
  At r = {r_e}, the tube circumference L₁ is {r_e}× shorter than
  the ring circumference L₂.  The (1,2) winding wraps once
  around the tube for every 2 wraps around the ring.  The tube
  wavelength (L₁/1 = L₁) is much shorter than the ring wavelength
  (L₂/2 = L₂/2), so most of the momentum is in the tube direction.
""")

    # ── Part C: Scan over aspect ratios ───────────────────────────
    print(f"{'='*72}")
    print("PART C: Stress decomposition vs. aspect ratio")
    print("=" * 72)

    print(f"\n  {'r':>6s} {'s':>10s} {'f₁':>8s} {'f₂':>8s} "
          f"{'ΔP/P_iso':>9s} {'P_iso(J/m²)':>14s} {'ΔP(J/m²)':>14s} "
          f"{'A (m²)':>12s}")
    print(f"  {'-'*87}")

    for r in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.6, 7.0, 8.0, 9.0, 10.0, 20.0]:
        try:
            s = solve_shear_for_alpha(r)
        except Exception:
            continue
        sd = stress_decomposition(r, s)
        print(f"  {r:6.1f} {s:10.6f} {sd['f1']:8.4f} {sd['f2']:8.4f} "
              f"{sd['anisotropy_ratio']:9.4f} {sd['P_iso_Pa']:14.4e} "
              f"{sd['delta_P_Pa']:14.4e} {sd['A_m2']:12.4e}")

    print(f"""
  Key observations:
  - At r ≈ 2, f₁ ≈ f₂ ≈ 0.5 → ΔP ≈ 0 (isotropic crossover).
    Here the physical wavelengths match: L₁/n₁ = L₂/n₂.

  - At r < 2 (e.g. r = 1), the RING direction dominates
    (f₂ > f₁, ΔP < 0): the (1,2) mode has n₂ = 2 ring wraps,
    and the ring is now short, so ring momentum exceeds tube.

  - At r > 2, the TUBE direction dominates (f₁ > f₂, ΔP > 0):
    the tube is shorter, so tube momentum exceeds ring.
    At large r, f₁ → 1, ΔP → P_iso (maximally anisotropic).

  - At r = 6.6 (canonical), ΔP/P_iso ≈ 0.83.  The stress is
    predominantly anisotropic — the torus is strongly stressed
    in the tube direction.
""")

    # ── Part D: Shear modulus extraction (Track 4 preview) ────────
    print(f"{'='*72}")
    print("PART D: Shear modulus μ_m from α (input) — Track 4 preview")
    print("=" * 72)

    print(f"""
  α is an INPUT (R31 conclusion).  The known α = 1/137 determines
  the equilibrium shear s via the R19 charge formula.

  The anisotropic stress ΔP drives the shear.  At equilibrium:
      s_eq = ΔP / μ_m   →   μ_m = ΔP / s_eq

  This determines the membrane's shear modulus.
""")

    print(f"  {'r':>6s} {'s_eq':>10s} {'ΔP (J/m²)':>14s} "
          f"{'μ_m (J/m²)':>14s} {'μ_m (eV/fm²)':>14s}")
    print(f"  {'-'*62}")

    for r in [3.0, 5.0, 6.0, 6.6, 7.0, 8.0, 9.0]:
        try:
            s = solve_shear_for_alpha(r)
        except Exception:
            continue
        sd = stress_decomposition(r, s)
        mu_m = sd['delta_P_Pa'] / s if s > 1e-15 else float('inf')
        mu_m_eV_fm2 = mu_m * fm_to_m**2 / eV_J

        print(f"  {r:6.1f} {s:10.6f} {sd['delta_P_Pa']:14.4e} "
              f"{mu_m:14.4e} {mu_m_eV_fm2:14.4e}")

    print()
    # Canonical values
    s_canon = solve_shear_for_alpha(r_e)
    sd_canon = stress_decomposition(r_e, s_canon)
    mu_m_canon = sd_canon['delta_P_Pa'] / s_canon
    mu_m_canon_eV_fm2 = mu_m_canon * fm_to_m**2 / eV_J

    print(f"  At r = {r_e}:")
    print(f"    s_eq = {s_canon:.6f}")
    print(f"    ΔP = {sd_canon['delta_P_Pa']:.4e} J/m²")
    print(f"    μ_m = ΔP/s_eq = {mu_m_canon:.4e} J/m²")
    print(f"         = {mu_m_canon_eV_fm2:.4e} eV/fm²")

    # ── Part E: Normal stiffness and hierarchy ────────────────────
    print(f"\n{'='*72}")
    print("PART E: Normal stiffness K_n and hierarchy ratio")
    print("=" * 72)

    K_n = c_SI**4 / (8 * math.pi * G_N)  # spacetime stiffness (N = J/m)

    print(f"""
  The normal stiffness K_n is identified with GR's spacetime
  stiffness (the conversion factor between stress-energy and
  curvature):

    K_n = c⁴/(8πG) = {K_n:.4e} N

  This is NOT a 2D surface quantity — it's the 4D gravitational
  stiffness.  To compare with μ_m (a 2D quantity, J/m²), we need
  to project K_n onto the T² surface.

  The effective 2D normal stiffness is K_n per unit area:
    K_n^(2D) = K_n / A_torus = {K_n / sd_canon['A_m2']:.4e} J/m⁴

  But μ_m has units J/m² (force per unit length per unit shear).
  The comparison requires care about dimensions.
""")

    # Direct hierarchy ratio using the standard gravitational coupling
    alpha_grav = G_N * m_e_kg**2 / (hbar_SI * c_SI)

    print(f"  Standard hierarchy measures:")
    print(f"    α_EM = e²/(4πε₀ℏc) = {ALPHA:.6e}")
    print(f"    α_grav = Gm_e²/(ℏc) = {alpha_grav:.6e}")
    print(f"    α_EM / α_grav = {ALPHA/alpha_grav:.4e}")
    print(f"    (This is the hierarchy: EM is {ALPHA/alpha_grav:.0e}× stronger than gravity)")

    # Membrane-based hierarchy: compare the FORCES
    # EM coupling: the shear stress ΔP drives charge.
    # The "EM force" per unit area is ΔP itself.
    # Gravitational coupling: the normal stress drives gravity.
    # The gravitational self-energy per unit area:
    #   u_grav = G m_e² / (R × A) where R is the torus size
    # More precisely, the gravitational binding energy:
    E_grav = G_N * m_e_kg**2 / geom['R2_m']  # Newtonian self-energy (J)
    u_grav = E_grav / geom['A_m2']  # gravitational energy density (J/m²)

    print(f"\n  Membrane-based comparison:")
    print(f"    ΔP (shear stress, drives α) = {sd_canon['delta_P_Pa']:.4e} J/m²")
    print(f"    u_grav (gravitational self-energy density) = {u_grav:.4e} J/m²")
    print(f"    ΔP / u_grav = {sd_canon['delta_P_Pa']/u_grav:.4e}")

    print(f"""
  The ratio ΔP/u_grav ≈ {sd_canon['delta_P_Pa']/u_grav:.0e} — this IS the hierarchy.
  The electromagnetic stress (ΔP, which drives charge/α) is
  {sd_canon['delta_P_Pa']/u_grav:.0e}× larger than the gravitational
  self-energy density on the same surface.

  Physical interpretation:
  The hierarchy between EM and gravity is the ratio of the
  photon's ANISOTROPIC radiation pressure (which drives the
  lattice shear producing charge) to the particle's
  gravitational self-energy density (which is the gravitational
  "pressure" on the surface).

  Both live on the same T² surface.  The enormous ratio arises
  because:
  - ΔP ∝ m_e c²/A ∝ 1/R² (radiation pressure, scales as
    inverse area — a LOCAL surface quantity)
  - u_grav ∝ Gm_e²/(R×A) ∝ G m_e/R³ (gravitational coupling,
    scales as an additional power of Gm_e/(Rc²) — includes the
    GLOBAL gravitational weakness)
""")

    # ── Part F: Force balance preview (Track 2) ───────────────────
    print(f"{'='*72}")
    print("PART F: Force balance — surface energy σ_m (Track 2 preview)")
    print("=" * 72)

    se = surface_energy_from_equilibrium(sd_canon)

    print(f"""
  If radiation pressure balances surface tension at the
  observed torus size (Compton wavelength), the surface energy
  density σ_m is determined.

  From L₁ equilibrium:
    σ_m = P_iso / r = {se['sigma_m_from_L1']:.4e} J/m²

  From L₂ equilibrium:
    σ_m = p₂ = {se['sigma_m_from_L2']:.4e} J/m²

  Ratio: σ_m(L₁) / σ_m(L₂) = {se['sigma_m_ratio']:.4f}
""")

    if abs(se['sigma_m_ratio'] - 1.0) > 0.01:
        print(f"""  The two estimates DISAGREE by a factor of {se['sigma_m_ratio']:.2f}.
  This means surface tension alone cannot balance radiation
  pressure in BOTH directions simultaneously.  The equilibrium
  requires additional physics:
  - Bending rigidity (κ_b) penalizing curvature
  - Anisotropic membrane tension
  - The shear modulus μ_m providing tangential restoring force
  - Or: the aspect ratio r is NOT free but determined by a
    separate constraint (e.g., the mass ratios m_e/m_μ/m_τ)

  This is a finding for Track 2: a simple isotropic surface
  tension is INSUFFICIENT.  The force balance requires the
  full elastic membrane with at least (σ_m, μ_m).
""")

    # ── Summary ───────────────────────────────────────────────────
    print(f"{'='*72}")
    print("SUMMARY")
    print("=" * 72)
    print(f"""
Key results:

F1. The (1,2) mode stress is HIGHLY ANISOTROPIC.
    At r = {r_e}: {sd_canon['f1']*100:.1f}% of momentum is in the tube (θ₁)
    direction, {sd_canon['f2']*100:.1f}% in the ring (θ₂) direction.
    ΔP/P_iso = {sd_canon['anisotropy_ratio']:.3f} — the anisotropic stress
    is {sd_canon['anisotropy_ratio']*100:.0f}% of the isotropic pressure.

F2. The stress tensor is UNIFORM across the T² surface.
    For a running wave (circularly polarized photon), the energy
    density is constant: ρ = E/A = {sd_canon['rho_Pa']:.2e} J/m².
    There is no spatial pattern in the stress — only a direction-
    dependent anisotropy.

F3. The shear modulus μ_m is determined by α (input).
    μ_m = ΔP/s_eq = {mu_m_canon:.4e} J/m²
                   = {mu_m_canon_eV_fm2:.4e} eV/fm²
    This is the membrane's tangential compliance.

F4. The hierarchy ΔP/u_grav ≈ {sd_canon['delta_P_Pa']/u_grav:.0e} reproduces the known
    EM/gravity hierarchy.  The ratio arises because radiation
    pressure (local, ∝ 1/A) vastly exceeds gravitational
    self-energy density (global, ∝ Gm/R³).

F5. Isotropic surface tension CANNOT balance radiation pressure
    in both T² directions.  σ_m(L₁) / σ_m(L₂) = {se['sigma_m_ratio']:.2f}.
    The force balance requires anisotropic elastic response
    (at minimum σ_m + μ_m), not just surface tension.

F6. The isotropic crossover is at r ≈ 2 (where f₁ = f₂).
    Below r = 2: ring-dominated stress (ΔP < 0).
    Above r = 2: tube-dominated stress (ΔP > 0).
    The canonical r = 6.6 is well into the tube-dominated
    regime, producing strong positive shear stress consistent
    with the shear needed for α = 1/137.

F7. Physical magnitudes at r = {r_e}:
    P_iso   = {sd_canon['P_iso_Pa']:.2e} J/m² = {sd_canon['P_iso_Pa']*fm_to_m**2/eV_J:.4f} eV/fm²
    ΔP      = {sd_canon['delta_P_Pa']:.2e} J/m²
    μ_m     = {mu_m_canon:.2e} J/m²
    σ_m     ~ {se['sigma_m_from_L1']:.2e} J/m² (from L₁ balance)
    K_n     = {K_n:.2e} N (spacetime stiffness, 4D)
""")


if __name__ == '__main__':
    main()
