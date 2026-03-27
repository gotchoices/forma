#!/usr/bin/env python3
"""
field_profile.py — Guided-wave field profile analysis (R6).

Part A: Self-consistency of the charge formula with R2 geometry.
Part B: Charge integral for different field profiles.
Part C: Fresnel zone / diffraction connection.

Reference: findings.md, S2 findings F1/F6, R2 findings F3–F5.
Run:  python3 studies/R6-field-profile/scripts/field_profile.py
"""

import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, e, eps0, alpha, m_e, lambda_C


import time
_t0 = time.time()

def banner(title):
    dt = time.time() - _t0
    print()
    print("=" * 68)
    print(f"  {title}  [{dt:.2f}s]")
    print("=" * 68)
    sys.stdout.flush()


def section(title):
    print(f"\n--- {title} ---\n")
    sys.stdout.flush()


# ── Derived constants ─────────────────────────────────────────

e_sq   = e**2
hc     = h * c
U_E    = m_e * c**2 / 2   # E-field energy = half the photon energy


# ══════════════════════════════════════════════════════════════
#  PART A: Self-consistency of S2 charge formula with R2 geometry
# ══════════════════════════════════════════════════════════════

banner("Part A: Self-consistency check")

section("S2's charge formula (from S2-toroid-geometry F1, F6)")

print("  The WvM charge formula with torus volume V = 2π²Ra²:")
print("    q² = 16π²ε₀ R⁴ hc / (λ V)")
print("       = 8 ε₀ R³ hc / (λ a²)")
print()
print("  Setting q = e and solving for (a/R)²:")
print("    (a/R)² = 4R / (α λ_C)        ... (*)")
print()
print("  This depends on R. S2 used R = λ_C/(4π) (WvM limit).")

# S2's result (non-self-consistent)
R_wvm = lambda_C / (4 * math.pi)
r_s2 = 1 / math.sqrt(math.pi * alpha)

print(f"\n  S2 result (R = λ_C/(4π) = {R_wvm:.4e} m):")
print(f"    (a/R)² = 4R/(αλ_C) = 4/(4πα) = 1/(πα)")
print(f"    a/R = 1/√(πα) = {r_s2:.4f}")

section("R2's geometry: R depends on r")

print("  From R2: R = λ_C / (2π√(4 + r²))  where r = a/R")
print("  Substituting into (*):")
print("    r² = 4/(αλ_C) × λ_C/(2π√(4+r²))")
print("    r² = 2/(πα√(4+r²))")
print("    r² √(4+r²) = 2/(πα)")

target = 2 / (math.pi * alpha)
print(f"\n  Target: r²√(4+r²) = 2/(πα) = {target:.4f}")

section("Solving for self-consistent r")

# Newton's method on f(r) = r²√(4+r²) - 2/(πα) = 0
r = 4.0  # initial guess
for _ in range(20):
    s = math.sqrt(4 + r**2)
    f = r**2 * s - target
    # f'(r) = 2r√(4+r²) + r³/√(4+r²) = r(2(4+r²) + r²)/√(4+r²)
    #       = r(8 + 3r²)/√(4+r²)
    fp = r * (8 + 3 * r**2) / s
    r = r - f / fp

r_sc = r
R_sc = lambda_C / (2 * math.pi * math.sqrt(4 + r_sc**2))
a_sc = r_sc * R_sc
L_phi_sc = lambda_C / math.sqrt(4 + r_sc**2)
L_theta_sc = r_sc * L_phi_sc
path_sc = math.sqrt(4 * L_phi_sc**2 + L_theta_sc**2)

print(f"  Self-consistent r = {r_sc:.5f}")
print(f"  S2 r              = {r_s2:.5f}")
print(f"  Ratio             = {r_sc/r_s2:.4f}")

# Verify charge
q_sq = 8 * eps0 * R_sc**3 * hc / (lambda_C * a_sc**2)
print(f"\n  Verification:")
print(f"    q² (computed) = {q_sq:.6e}")
print(f"    e²            = {e_sq:.6e}")
print(f"    q/e           = {math.sqrt(q_sq/e_sq):.6f}")

section("Self-consistent geometry")

print(f"  {'Quantity':<24} {'S2 (R=λ/(4π))':<20} {'Self-consistent':<20}")
print(f"  {'─'*24} {'─'*20} {'─'*20}")

R_s2_val = R_wvm
a_s2_val = r_s2 * R_wvm

print(f"  {'r = a/R':<24} {r_s2:<20.4f} {r_sc:<20.4f}")
print(f"  {'R (m)':<24} {R_s2_val:<20.4e} {R_sc:<20.4e}")
print(f"  {'a (m)':<24} {a_s2_val:<20.4e} {a_sc:<20.4e}")
print(f"  {'L_φ (m)':<24} {'—':<20} {L_phi_sc:<20.4e}")
print(f"  {'L_θ (m)':<24} {'—':<20} {L_theta_sc:<20.4e}")
print(f"  {'Path length (m)':<24} {'—':<20} {path_sc:<20.4e}")
print(f"  {'λ_C (m)':<24} {lambda_C:<20.4e} {lambda_C:<20.4e}")
print(f"  {'Path/λ_C':<24} {'—':<20} {path_sc/lambda_C:<20.10f}")

section("Why S2 and self-consistent differ")

print(f"  S2 assumed R = λ_C/(4π), the WvM thin-torus value.")
print(f"  But when r = a/R > 0, the path-length constraint gives a")
print(f"  SMALLER R.  The charge formula q ∝ R^(3/2) / a then needs")
print(f"  a different a/R to compensate.")
print(f"\n  S2's R:               {R_wvm:.4e} m")
print(f"  Self-consistent R:    {R_sc:.4e} m")
print(f"  Ratio:                {R_sc/R_wvm:.4f}")
print(f"\n  The self-consistent R is {R_sc/R_wvm:.1%} of S2's R.")
print(f"  Despite this, the field extent a is similar:")
print(f"  S2 a:                 {a_s2_val:.4e} m")
print(f"  Self-consistent a:    {a_sc:.4e} m")
print(f"  Ratio:                {a_sc/a_s2_val:.4f}")


# ══════════════════════════════════════════════════════════════
#  PART B: Charge for different field profiles
# ══════════════════════════════════════════════════════════════

banner("Part B: Charge integral for different field profiles")

section("Setup")

print("  The WvM charge formula matches an average field E₀ to the")
print("  Coulomb field at radius r_c = R:")
print()
print("    E₀ = √(2 U_E / (ε₀ V))     (field strength from energy)")
print("    E₀ = q / (4πε₀ R²)          (Coulomb field at R)")
print()
print("  For a non-uniform profile E(ρ), the effective volume changes.")
print("  Define V_eff such that U_E = (ε₀/2) E_peak² V_eff.")
print("  Then the charge formula becomes:")
print("    q² = 16π²ε₀ R⁴ hc / (λ V_eff)")

R = R_sc  # use self-consistent R

print(f"\n  Using self-consistent R = {R:.4e} m")
print(f"  Path length λ_C = {lambda_C:.4e} m")


def charge_from_Veff(V_eff, R_val):
    """Compute q from V_eff and R using the WvM formula."""
    q_sq = 16 * math.pi**2 * eps0 * R_val**4 * hc / (lambda_C * V_eff)
    return math.sqrt(q_sq)


def find_sigma_for_qe(profile_Veff_func, R_val, sigma_guess=1e-13):
    """Find sigma such that q = e for a given profile V_eff function."""
    # q² = 16π²ε₀R⁴hc/(λ V_eff(σ))
    # q = e  →  V_eff = 16π²ε₀R⁴hc/(λ e²)
    V_target = 16 * math.pi**2 * eps0 * R_val**4 * hc / (lambda_C * e_sq)

    # Bisection to find σ where V_eff(σ) = V_target
    lo, hi = 1e-16, 1e-10
    for _ in range(200):
        mid = (lo + hi) / 2
        V = profile_Veff_func(mid)
        if V < V_target:
            lo = mid
        else:
            hi = mid
    return mid


section("Profile 1: Uniform field in torus V = 2π²Ra²")

def V_uniform(sigma):
    """Torus volume with tube radius = sigma."""
    return 2 * math.pi**2 * R * sigma**2

sigma_uniform = find_sigma_for_qe(V_uniform, R)
q_check = charge_from_Veff(V_uniform(sigma_uniform), R)

print(f"  V_eff = 2π²Rσ²   (σ plays the role of tube radius a)")
print(f"  σ for q = e:  {sigma_uniform:.4e} m")
print(f"  a/R:          {sigma_uniform/R:.4f}")
print(f"  q check:      {q_check/e:.6f} e")


section("Profile 2: Gaussian E = E₀ exp(-ρ²/(2σ²))")

def V_gaussian(sigma):
    """Effective volume for Gaussian profile on circular orbit.

    E² ∝ exp(-ρ²/σ²).  Cross-sectional integral of E²:
    ∫₀^∞ ∫₀^2π exp(-ρ²/σ²) ρ dρ dχ = πσ².
    Integrated along orbit of length λ_C:
    V_eff = πσ² × λ_C.

    But this ignores the toroidal correction (field at distance ρ
    from the orbit sees a Jacobian factor due to curvature).
    For now, use the local (straight orbit) approximation.
    """
    return math.pi * sigma**2 * lambda_C

sigma_gauss = find_sigma_for_qe(V_gaussian, R)
q_check = charge_from_Veff(V_gaussian(sigma_gauss), R)

print(f"  V_eff = πσ² λ_C  (local Gaussian, straight-orbit approx)")
print(f"  σ for q = e:  {sigma_gauss:.4e} m")
print(f"  σ/R:          {sigma_gauss/R:.4f}")
print(f"  q check:      {q_check/e:.6f} e")


section("Profile 3: Exponential E = E₀ exp(-ρ/σ)")

def V_exponential(sigma):
    """Effective volume for exponential profile.

    E² ∝ exp(-2ρ/σ).  Cross-sectional integral of E²:
    ∫₀^∞ ∫₀^2π exp(-2ρ/σ) ρ dρ dχ = 2π × σ²/4 = πσ²/2.
    Along orbit: V_eff = (πσ²/2) × λ_C.
    """
    return math.pi * sigma**2 / 2 * lambda_C

sigma_exp = find_sigma_for_qe(V_exponential, R)
q_check = charge_from_Veff(V_exponential(sigma_exp), R)

print(f"  V_eff = (π/2)σ² λ_C  (local exponential, straight-orbit)")
print(f"  σ for q = e:  {sigma_exp:.4e} m")
print(f"  σ/R:          {sigma_exp/R:.4f}")
print(f"  q check:      {q_check/e:.6f} e")


section("Profile comparison summary")

print(f"  {'Profile':<20} {'σ for q=e (m)':<18} {'σ/R':<10} {'σ (× 10⁻¹³)':<14}")
print(f"  {'─'*20} {'─'*18} {'─'*10} {'─'*14}")
print(f"  {'Uniform (torus)':<20} {sigma_uniform:<18.4e} {sigma_uniform/R:<10.4f}"
      f" {sigma_uniform*1e13:<14.4f}")
print(f"  {'Gaussian':<20} {sigma_gauss:<18.4e} {sigma_gauss/R:<10.4f}"
      f" {sigma_gauss*1e13:<14.4f}")
print(f"  {'Exponential':<20} {sigma_exp:<18.4e} {sigma_exp/R:<10.4f}"
      f" {sigma_exp*1e13:<14.4f}")

print(f"\n  All profiles need σ in the range {min(sigma_uniform,sigma_gauss,sigma_exp)*1e13:.2f}"
      f"–{max(sigma_uniform,sigma_gauss,sigma_exp)*1e13:.2f} × 10⁻¹³ m")


# ══════════════════════════════════════════════════════════════
#  PART C: Fresnel zone / diffraction connection
# ══════════════════════════════════════════════════════════════

banner("Part C: Fresnel zone connection")

section("Fresnel zone radius")

print("  For a wave of wavelength λ curving along a path of radius R,")
print("  the transverse spread due to diffraction is of order:")
print("    σ_Fresnel = √(λ R)")
print()
print("  This is the Fresnel zone radius — the distance at which the")
print("  path-length difference equals λ/2 (first Fresnel zone).")

sigma_fresnel = math.sqrt(lambda_C * R_sc)
sigma_fresnel_s2 = math.sqrt(lambda_C * R_wvm)

print(f"\n  Using self-consistent R = {R_sc:.4e} m:")
print(f"    σ_Fresnel = √(λ_C × R) = {sigma_fresnel:.4e} m")

print(f"\n  Using S2's R = {R_wvm:.4e} m:")
print(f"    σ_Fresnel = √(λ_C × R) = {sigma_fresnel_s2:.4e} m")

section("Comparison with field extents")

print(f"  {'Scale':<30} {'Value (m)':<14} {'Ratio to σ_Fresnel'}")
print(f"  {'─'*30} {'─'*14} {'─'*18}")
print(f"  {'σ_Fresnel (self-cons R)':<30} {sigma_fresnel:<14.4e} {'1.000'}")
print(f"  {'σ_Fresnel (S2 R)':<30} {sigma_fresnel_s2:<14.4e}"
      f" {sigma_fresnel_s2/sigma_fresnel:.4f}")
print(f"  {'a (self-consistent)':<30} {a_sc:<14.4e} {a_sc/sigma_fresnel:.4f}")
print(f"  {'a (S2)':<30} {a_s2_val:<14.4e} {a_s2_val/sigma_fresnel:.4f}")
print(f"  {'σ_uniform for q=e':<30} {sigma_uniform:<14.4e}"
      f" {sigma_uniform/sigma_fresnel:.4f}")
print(f"  {'σ_Gaussian for q=e':<30} {sigma_gauss:<14.4e}"
      f" {sigma_gauss/sigma_fresnel:.4f}")
print(f"  {'σ_exponential for q=e':<30} {sigma_exp:<14.4e}"
      f" {sigma_exp/sigma_fresnel:.4f}")

section("Fresnel zone vs S2's a (original observation)")

# The close match between √(λ_C × R_S2) and a_S2
print(f"  S2 noted a/R = 1/√(πα).  With R_S2 = λ/(4π):")
print(f"    a_S2 = R_S2/√(πα) = {a_s2_val:.6e} m")
print(f"    √(λ_C R_S2)       = {sigma_fresnel_s2:.6e} m")
print(f"    Ratio a_S2/√(λR)  = {a_s2_val/sigma_fresnel_s2:.6f}")
print()

# Check if this is exact algebraically
# a_S2 = R/√(πα) = λ_C/(4π√(πα))
# √(λ_C R) = √(λ_C²/(4π)) = λ_C/(2√π)
# a_S2 / √(λ_C R) = (λ_C/(4π√(πα))) / (λ_C/(2√π))
#                  = 2√π / (4π√(πα)) = 1/(2π√α) = 1/(2√(π²α))
ratio_analytic = 1 / (2 * math.sqrt(math.pi**2 * alpha))
print(f"  Analytical: a_S2 / √(λR) = 1/(2π√α) = {ratio_analytic:.6f}")
print(f"  This is NOT 1 — the Fresnel match was approximate ({ratio_analytic:.1%} of exact).")


# ══════════════════════════════════════════════════════════════
#  PART D: Self-consistent solution with each profile
# ══════════════════════════════════════════════════════════════

banner("Part D: Self-consistent solutions")

section("For each profile, find (r, R, σ) satisfying both:")
print("  1. Path constraint: √(4L_φ² + L_θ²) = λ_C")
print("  2. Charge formula with profile V_eff: q = e")
print("  3. σ is the physical field extent")
print()
print("  NOTE: In the uniform-torus case, σ = a = rR, so the system")
print("  is fully coupled.  For Gaussian/exponential, σ is the profile")
print("  width and may differ from rR = the compact dimension extent.")
print("  The question is: does the wave equation select σ?")

# For the uniform torus case, we already found r_sc above.
# Let's also report what geometry this implies.

section("Uniform torus (self-consistent)")

print(f"  r = a/R = {r_sc:.5f}")
print(f"  R       = {R_sc:.4e} m")
print(f"  a       = {a_sc:.4e} m")
print(f"  L_φ     = {L_phi_sc:.4e} m")
print(f"  L_θ     = {L_theta_sc:.4e} m")
print(f"  Path    = {path_sc:.4e} m = λ_C ✓")
print(f"  q/e     = 1.000 (by construction)")

# Spin check
print(f"\n  Spin: ℏ/2 (topological, always exact)")

# g-factor
g_val = 2 * (1 + alpha / (2 * math.pi))
print(f"  g-factor: {g_val:.6f} (depends on α, not geometry)")

# Magnetic moment
mu_B = e * hbar / (2 * m_e)
mu_calc = g_val * mu_B / 2
mu_exp = 9.2847647043e-24
print(f"  μ_calc / μ_exp = {mu_calc/mu_exp:.6f}")


# ══════════════════════════════════════════════════════════════
#  PART E: Summary and implications
# ══════════════════════════════════════════════════════════════

banner("Summary")

print(f"""
  KEY FINDING: S2's a/R = 1/√(πα) ≈ 6.60 used the WvM orbital
  radius R = λ_C/(4π), which is only valid for the thin-torus
  limit (r → 0).  The self-consistent solution — satisfying both
  the charge formula and the path-length constraint — gives:

    r = a/R ≈ {r_sc:.2f}   (not 6.60)
    R ≈ {R_sc:.3e} m   (not {R_wvm:.3e} m)
    a ≈ {a_sc:.3e} m   (not {a_s2_val:.3e} m)

  Both R and a change significantly from S2's values (R to
  {R_sc/R_wvm:.0%}, a to {a_sc/a_s2_val:.0%}).  The charge formula
  is very sensitive to R (q ∝ R^(3/2)/a), so using the correct R
  matters.

  The Fresnel zone radius √(λ_C R) = {sigma_fresnel:.3e} m is
  {sigma_fresnel/a_sc:.1f}× the self-consistent a — same order
  of magnitude but not an exact match.

  IMPLICATIONS:
  1. R2's conclusion (zero free parameters) still holds, but
     with r ≈ {r_sc:.2f} instead of 6.60.
  2. The charge formula is approximate (uniform field, Coulomb
     matching).  The PROFILE SHAPE matters: Gaussian needs
     σ/R ≈ {sigma_gauss/R_sc:.1f}, uniform needs a/R ≈ {r_sc:.1f},
     exponential needs σ/R ≈ {sigma_exp/R_sc:.1f}.
  3. A wave-equation solution for the actual mode profile would
     determine which σ (and which a/R) is physical.

  STATUS: The self-consistent uniform-torus solution is found.
  The next step is solving the mode equation to determine the
  actual field profile shape.
""")
