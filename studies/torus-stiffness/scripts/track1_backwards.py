#!/usr/bin/env python3
"""
R18 Track 1: Backwards calculation — stiffness from known α.

Given α = 1/137, work backwards to find the stiffness κ of the
compact space that would produce the right charge through the
mode-coupling mechanism.

Uses analytical perturbation theory with flat-space modes to
avoid numerical eigenvalue issues on the embedded torus.

The chain:
  1. Q = e  →  mode coupling amplitude ε
  2. ε  →  cos(2φ) deformation amplitude δ  (perturbation theory)
  3. δ  →  EM driving pressure P
  4. κ = P / δ  →  stiffness of the compact space
  5. Express κ in fundamental constants → check for match
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import (h, hbar, c, eps0, mu0, e, alpha as alpha_em,
                            m_e, lambda_C, G)


def run_track1(r_val):
    """Run the full backwards calculation for aspect ratio r."""

    # ── Geometry ──
    R = lambda_C / (2 * np.pi * np.sqrt(4 + r_val**2))
    a = r_val * R
    L_path = 4 * np.pi * np.sqrt((a / 2)**2 + R**2)
    E_mc2 = m_e * c**2

    print(f"\n{'='*65}")
    print(f"R18 Track 1: Backwards Calculation of Stiffness")
    print(f"  r = {r_val:.4f}   R = {R:.4e} m   a = {a:.4e} m")
    print(f"{'='*65}")

    # ═══════════════════════════════════════════════════════════
    # STEP 1: Energy normalization → E₀
    # ═══════════════════════════════════════════════════════════
    # ½ε₀ E₀² × V_eff = m_e c²/2
    # V_eff ≈ ½ × (surface area) × (skin depth)
    #       = ½ × 4π²Ra × a = 2π²Ra²
    V_eff = 2 * np.pi**2 * R * a**2
    E0_sq = E_mc2 / (eps0 * V_eff)
    E0 = np.sqrt(E0_sq)

    print(f"\n  STEP 1: Energy normalization")
    print(f"  V_eff = 2π²Ra² = {V_eff:.4e} m³")
    print(f"  E₀ = {E0:.4e} V/m")

    # ═══════════════════════════════════════════════════════════
    # STEP 2: Required coupling ε from Q = e
    # ═══════════════════════════════════════════════════════════
    # The (1,0) mode cos(θ) has charge integral:
    #   Q_{1,0} = ε₀ E₀ ∫∫ cos θ × a(R + a cos θ) dθ dφ
    # θ-integral: ∫ cos θ (R + a cos θ) dθ = 0 + aπ = aπ
    # φ-integral: ∫ dφ = 2π
    #   Q_{1,0} = ε₀ E₀ × a × aπ × 2π = 2π²ε₀E₀a²
    #
    # For the mixed mode ψ ≈ cos(θ+2φ) + ε cos θ:
    #   Q = ε × 2π²ε₀E₀a²

    Q_10_coeff = 2 * np.pi**2 * eps0 * E0 * a**2
    epsilon_required = e / Q_10_coeff

    print(f"\n  STEP 2: Required mode coupling")
    print(f"  Q = ε × 2π²ε₀E₀a² = e")
    print(f"  2π²ε₀E₀a² = {Q_10_coeff:.4e} C")
    print(f"  ε = {epsilon_required:.6e}")
    print(f"  |ε|² = {epsilon_required**2:.6e}  ({epsilon_required**2*100:.2f}% of energy in (1,0))")

    # ═══════════════════════════════════════════════════════════
    # STEP 3: Mode eigenvalues (flat-space approximation)
    # ═══════════════════════════════════════════════════════════
    # On the flat T², the eigenvalues are:
    #   ω²_{p,q}/c² = p²/a² + q²/R²
    #
    # For (1,2): ω²/c² = 1/a² + 4/R²
    # For (1,0): ω²/c² = 1/a²

    omega2_12 = (1.0 / a**2 + 4.0 / R**2)
    omega2_10 = 1.0 / a**2
    Delta_omega2 = omega2_12 - omega2_10  # = 4/R²

    E_12 = hbar * c * np.sqrt(omega2_12)
    E_10 = hbar * c * np.sqrt(omega2_10)

    print(f"\n  STEP 3: Mode eigenvalues (flat T²)")
    print(f"  ω²_{'{1,2}'}/c² = 1/a² + 4/R² = {omega2_12:.4e} m⁻²")
    print(f"  ω²_{'{1,0}'}/c² = 1/a²         = {omega2_10:.4e} m⁻²")
    print(f"  Δ(ω²/c²) = 4/R²            = {Delta_omega2:.4e} m⁻²")
    print(f"  E_{'{1,2}'} = {E_12:.4e} J = {E_12/E_mc2:.4f} m_ec²")
    print(f"  E_{'{1,0}'} = {E_10:.4e} J = {E_10/E_mc2:.4f} m_ec²")

    # ═══════════════════════════════════════════════════════════
    # STEP 4: Perturbation matrix element (analytical)
    # ═══════════════════════════════════════════════════════════
    # The cos(2φ) deformation R → R + δcos(2φ) perturbs the
    # φ-kinetic part of the Laplacian:
    #
    # Original: L_φ = q²/(R + a cos θ)²
    # Perturbed: L_φ → q²/(R + δcos(2φ) + a cos θ)²
    #          ≈ q²/ρ² × (1 - 2δcos(2φ)/ρ)
    #
    # Perturbation: ΔL = -2q²δ cos(2φ) / ρ³
    # For ψ_{1,2} with q=2: ΔL ψ_{1,2} = -8δ cos(2φ) / ρ³ × ψ_{1,2}
    #
    # Matrix element (using flat-space modes, inner product ∫∫ dθdφ):
    # V = ∫∫ cos θ × [-8δcos(2φ)/ρ³] × cos(θ+2φ) × dθ dφ
    #
    # φ-integral: ∫ cos(2φ)cos(θ+2φ) dφ = π cos θ
    #
    # So: V = -8πδ ∫ cos²θ / ρ³ dθ
    #
    # With the WEIGHTED inner product (weight = aρ for the
    # embedded torus metric):
    # V_w = ∫∫ cos θ × [-8δcos(2φ)/ρ³] × cos(θ+2φ) × aρ dθ dφ
    #      = -8aπδ ∫ cos²θ / ρ² dθ

    N_theta = 10000
    theta = np.linspace(0, 2 * np.pi, N_theta, endpoint=False)
    dtheta = theta[1] - theta[0]
    rho = R + a * np.cos(theta)

    # Key integral: I₁ = ∫ cos²θ / ρ² dθ
    I1 = np.sum(np.cos(theta)**2 / rho**2) * dtheta

    # Unweighted matrix element per unit δ:
    V_unweighted_per_delta = -8 * np.pi * I1

    # Weighted matrix element per unit δ:
    V_weighted_per_delta = -8 * a * np.pi * I1

    # Mode norms (weighted):
    # <cos θ|cos θ>_w = ∫∫ cos²θ × aρ dθ dφ = 2π × a ∫ cos²θ ρ dθ
    # <cos(θ+2φ)|cos(θ+2φ)>_w = 2π × a ∫ ... dθ (same by symmetry)
    norm_sq_10 = 2 * np.pi * a * np.sum(np.cos(theta)**2 * rho) * dtheta
    norm_sq_12 = np.pi * a * np.sum(rho) * dtheta  # ∫cos²(θ+2φ)dφ = π for any θ

    # Normalized coupling per unit δ:
    V_norm_per_delta = V_weighted_per_delta / np.sqrt(norm_sq_10 * norm_sq_12)

    print(f"\n  STEP 4: Coupling matrix element")
    print(f"  I₁ = ∫ cos²θ/ρ² dθ = {I1:.6e} m⁻²")
    print(f"  V_w/δ (weighted) = {V_weighted_per_delta:.4e} m⁻¹")
    print(f"  ‖ψ_{'{1,0}'}‖² = {norm_sq_10:.4e} m²")
    print(f"  ‖ψ_{'{1,2}'}‖² = {norm_sq_12:.4e} m²")
    print(f"  V_norm/δ = {V_norm_per_delta:.4e} m⁻¹")

    # ═══════════════════════════════════════════════════════════
    # STEP 5: Required deformation δ
    # ═══════════════════════════════════════════════════════════
    # From first-order perturbation theory:
    #   ε = V_norm × δ / Δ(ω²/c²)
    #
    # But we need to be careful about the perturbation formula.
    # For the Hamiltonian H = c²L, the energy perturbation is:
    #   ε = c² <1,0|ΔL|1,2> δ / (E_{1,2}² - E_{1,0}²)
    #     = c² V_norm δ / (ℏ²c²(ω²_{1,2} - ω²_{1,0}))
    #     = V_norm δ / (ℏ² Δ(ω²/c²) / c² × c²) ... hmm
    #
    # Actually, perturbation theory for a generalized eigenvalue
    # problem gives:
    #   ε = <n|ΔH|m> / (E_m - E_n)
    #
    # For a massless particle, E = ℏω = ℏc√(ω²/c²).
    # <1,0|ΔH|1,2> = ℏ²c² × V_norm × δ  (ΔH = -c²ΔL × ℏ²? no...)
    #
    # Let me use a simpler approach.  The Hamiltonian operator is:
    # H = ℏc √(-∇²)  (for a massless particle)
    # This is NON-LOCAL, making perturbation theory awkward.
    #
    # For the SQUARED operator H² = ℏ²c² (-∇²):
    # H² ψ_n = E_n² ψ_n
    #
    # First-order perturbation on H²:
    # δE² = <n|ΔH²|n> = ℏ²c² <n|ΔL|n>
    #
    # Mode coupling (off-diagonal):
    # ε = ℏ²c² <1,0|ΔL|1,2> δ / (E_{1,2}² - E_{1,0}²)
    #   = ℏ²c² V_norm δ / (ℏ²c²Δ(ω²/c²))
    #   = V_norm δ / Δ(ω²/c²)

    delta_required = epsilon_required * Delta_omega2 / V_norm_per_delta

    print(f"\n  STEP 5: Required deformation")
    print(f"  ε = V_norm × δ / Δ(ω²/c²)")
    print(f"  δ = ε × Δ(ω²/c²) / V_norm")
    print(f"  δ = {delta_required:.4e} m")
    print(f"  δ/a = {delta_required/a:.6f}")
    print(f"  δ/R = {delta_required/R:.6f}")
    print(f"  |δ|/a = {abs(delta_required)/a:.6f}")

    # ═══════════════════════════════════════════════════════════
    # STEP 6: EM driving pressure
    # ═══════════════════════════════════════════════════════════
    # The perturbed mode ψ ≈ cos(θ+2φ) + ε cos θ has energy density:
    # u ∝ [cos(θ+2φ) + ε cos θ]²
    #   = cos²(θ+2φ) + 2ε cos(θ+2φ)cos θ + ε²cos²θ
    #
    # Cross term: 2ε cos(θ+2φ)cos θ = ε[cos(2θ+2φ) + cos(2φ)]
    #
    # The cos(2φ) component of the energy density:
    #   u_{cos2φ} = ε × ε₀E₀²/2
    #
    # Radiation pressure ≈ energy density:
    #   P_{cos2φ} = ε × ε₀E₀²/2

    P_total = eps0 * E0_sq / 2
    P_cos2phi = abs(epsilon_required) * P_total

    print(f"\n  STEP 6: EM driving pressure")
    print(f"  P_total = ε₀E₀²/2 = {P_total:.4e} Pa")
    print(f"  P_cos(2φ) = |ε| × P_total = {P_cos2phi:.4e} Pa")

    # ═══════════════════════════════════════════════════════════
    # STEP 7: Stiffness  κ = P / |δ|
    # ═══════════════════════════════════════════════════════════
    delta_abs = abs(delta_required)
    kappa = P_cos2phi / delta_abs

    print(f"\n  STEP 7: Stiffness")
    print(f"  κ = P_cos(2φ) / |δ| = {kappa:.4e} Pa/m")

    # ═══════════════════════════════════════════════════════════
    # STEP 8: Express in fundamental constants
    # ═══════════════════════════════════════════════════════════
    print(f"\n  STEP 8: Identification")
    print(f"  {'='*55}")

    # Build candidate expressions and check ratios
    candidates = [
        ("ε₀",                          eps0),
        ("μ₀",                          mu0),
        ("1/(μ₀c²) = ε₀",              1/(mu0*c**2)),
        ("ε₀E₀²/R",                    eps0*E0_sq/R),
        ("ε₀E₀²/a",                    eps0*E0_sq/a),
        ("ε₀E₀²/(2a)",                 eps0*E0_sq/(2*a)),
        ("m_ec²/(2π²R²a²)",            E_mc2/(2*np.pi**2*R**2*a**2)),
        ("m_ec²/(4π²Ra³)",             E_mc2/(4*np.pi**2*R*a**3)),
        ("m_ec²/(4π²R²a²)",            E_mc2/(4*np.pi**2*R**2*a**2)),
        ("m_ec²/(R⁴)",                 E_mc2/R**4),
        ("m_ec²/(a⁴)",                 E_mc2/a**4),
        ("m_ec²/(R³a)",                E_mc2/(R**3*a)),
        ("m_ec²/(R²a²)",               E_mc2/(R**2*a**2)),
        ("ℏc/R⁴",                      hbar*c/R**4),
        ("ℏc/(R²a²)",                  hbar*c/(R**2*a**2)),
        ("e²/(4πε₀R⁴)",               e**2/(4*np.pi*eps0*R**4)),
        ("e²/(4πε₀a⁴)",               e**2/(4*np.pi*eps0*a**4)),
        ("α×m_ec²/R³",                 alpha_em*E_mc2/R**3),
        ("α×ε₀E₀²/R",                 alpha_em*eps0*E0_sq/R),
        ("m_e⁵c⁶/ℏ⁴",                 m_e**5*c**6/hbar**4),
        ("m_e⁴c⁵/ℏ³",                 m_e**4*c**5/hbar**3),
    ]

    print(f"  κ = {kappa:.6e} Pa/m\n")
    matches = []
    for name, value in candidates:
        ratio = kappa / value
        log_ratio = np.log10(abs(ratio))
        tag = ""
        if abs(log_ratio) < 0.1:
            tag = "  ◀◀ EXACT"
            matches.append((name, ratio))
        elif abs(log_ratio) < 0.3:
            tag = "  ◀ MATCH"
            matches.append((name, ratio))
        elif abs(log_ratio) < 0.7:
            tag = "  ~ close"
        print(f"  κ / ({name:25s}) = {ratio:12.6e}{tag}")

    # ═══════════════════════════════════════════════════════════
    # STEP 9: Analytical derivation attempt
    # ═══════════════════════════════════════════════════════════
    print(f"\n  STEP 9: Analytical structure")
    print(f"  {'-'*55}")

    # Substitute everything in terms of R, a, m_e, c, ε₀, ℏ:
    #
    # ε = e / (2π²ε₀E₀a²)
    # E₀² = m_ec² / (ε₀ × 2π²Ra²)  →  E₀ = √(m_ec²/(2π²ε₀Ra²))
    # ε = e / (2π²ε₀a² × √(m_ec²/(2π²ε₀Ra²)))
    #   = e × √(2π²ε₀Ra²) / (2π²ε₀a² × √(m_ec²))
    #   = e × √(2π²ε₀R) / (2π²ε₀a × √(m_ec²))
    #   = e / (a × √(2π²ε₀m_ec²/R))
    #   = e / (a × √(2π²ε₀m_ec²/R))

    eps_analytical = e / (a * np.sqrt(2 * np.pi**2 * eps0 * E_mc2 / R))
    print(f"  ε (analytical) = {eps_analytical:.6e}  (check: {epsilon_required:.6e})")

    # V_norm/δ = -8aπ I₁ / √(norm10 × norm12)
    # For flat-space modes (ρ ≈ R):
    #   I₁ ≈ ∫ cos²θ/R² dθ = π/R²
    #   norm10 ≈ 2πa × π × R = 2π²aR (ρ ≈ R)
    #   norm12 ≈ πa × 2πR = 2π²aR (same)
    #   V_norm/δ ≈ -8aπ(π/R²) / (2π²aR) = -8π²a/(R² × 2π²aR) = -4/R³

    V_approx = -4.0 / R**3
    print(f"  V_norm/δ (flat approx)  = {V_approx:.4e} m⁻¹")
    print(f"  V_norm/δ (numerical)    = {V_norm_per_delta:.4e} m⁻¹")
    print(f"  ratio = {V_norm_per_delta/V_approx:.4f}")

    # Δ(ω²/c²) = 4/R²
    # δ = ε × 4/R² / (-4/R³) = -ε × R  (for flat approx)
    delta_approx = -eps_analytical * R
    print(f"  δ (flat approx) = {delta_approx:.4e} m  (exact: {delta_required:.4e})")

    # P = |ε| × ε₀E₀²/2 = |ε| × m_ec²/(4π²Ra²)
    P_approx = abs(eps_analytical) * E_mc2 / (4 * np.pi**2 * R * a**2)
    print(f"  P (flat approx) = {P_approx:.4e} Pa  (exact: {P_cos2phi:.4e})")

    # κ = P/|δ| = |ε| × m_ec²/(4π²Ra²) / (|ε|R) = m_ec²/(4π²R²a²)
    kappa_approx = E_mc2 / (4 * np.pi**2 * R**2 * a**2)
    print(f"\n  κ (flat approx) = m_ec²/(4π²R²a²) = {kappa_approx:.4e}")
    print(f"  κ (numerical)   = {kappa:.4e}")
    print(f"  ratio           = {kappa/kappa_approx:.6f}")

    # Express m_ec²/(4π²R²a²) in terms of fundamental constants:
    # R = ℏ/(m_ec√(4+r²)), a = rR
    # R² a² = r² R⁴ = r² ℏ⁴/(m_e⁴c⁴(4+r²)²)
    # κ = m_ec² × m_e⁴c⁴(4+r²)² / (4π²r²ℏ⁴)
    #   = m_e⁵c⁶(4+r²)² / (4π²r²ℏ⁴)

    kappa_fundamental = m_e**5 * c**6 * (4 + r_val**2)**2 / (4 * np.pi**2 * r_val**2 * hbar**4)
    print(f"\n  κ = m_e⁵c⁶(4+r²)² / (4π²r²ℏ⁴)")
    print(f"    = {kappa_fundamental:.4e}  (check: {kappa_approx:.4e})")

    # Check: is ε cancelled in κ?  YES!
    # κ = P/δ = (ε × P_0) / (ε × R) = P_0/R = ε₀E₀²/(2R)
    # This means κ is INDEPENDENT of ε (and hence α)!
    print(f"\n  KEY INSIGHT: ε cancels in κ = P/|δ|")
    print(f"  κ = (|ε| × ε₀E₀²/2) / (|ε| × R) = ε₀E₀²/(2R)")
    print(f"  ε₀E₀²/(2R) = {eps0*E0_sq/(2*R):.4e}")
    print(f"  κ numerical = {kappa:.4e}")
    print(f"  ratio = {kappa/(eps0*E0_sq/(2*R)):.6f}")

    print(f"\n  The stiffness does NOT depend on α!")
    print(f"  It is purely geometric: κ = m_ec²/(4π²R²a²)")
    print(f"  = ε₀E₀²/(2R) = (EM energy density) / (major radius)")

    # ═══════════════════════════════════════════════════════════
    # STEP 10: What determines α then?
    # ═══════════════════════════════════════════════════════════
    print(f"\n  STEP 10: Where does α enter?")
    print(f"  {'-'*55}")

    # If κ doesn't depend on α, what does?
    # The deformation δ depends on the coupling ε, which depends
    # on Q = e (i.e., α).  But the BALANCE κδ = P gives:
    #   κ × (εR) = ε × ε₀E₀²/2
    #   κR = ε₀E₀²/2
    # This is satisfied for ANY ε (and hence any α).
    #
    # In the flat-space approximation, the perturbation theory
    # gives δ = -εR for any ε.  The pressure P = ε × ε₀E₀²/2
    # and the restoring force κδ = ε₀E₀²/(2R) × εR = ε × ε₀E₀²/2.
    # So P = κδ identically — the balance is trivially satisfied.
    #
    # This means the backwards calculation is DEGENERATE in the
    # flat-space approximation.  The stiffness adjusts to match
    # any α.  To determine α, we need CORRECTIONS beyond the
    # flat-space approximation — the curvature of the embedded
    # torus matters.

    print(f"""
  In the flat-space approximation:
    δ = -ε R     (deformation scales linearly with coupling)
    P = ε × P₀   (pressure scales linearly with coupling)
    κ = P₀/R     (stiffness is independent of ε)

  The force balance κδ = P is satisfied for ANY ε (any α).
  This is because both P and δ scale linearly with ε,
  so their ratio κ = P/δ is ε-independent.

  To DETERMINE α, we need the relationship between ε and δ
  to be NONLINEAR — which happens when we include the
  curvature corrections from the embedded torus.

  In the full calculation (not flat-space):
    V_norm/δ = {V_norm_per_delta:.4e}  (numerical, includes curvature)
    vs  -4/R³ = {V_approx:.4e}  (flat-space)
    ratio = {V_norm_per_delta/V_approx:.4f}

  The curvature correction factor is {V_norm_per_delta/V_approx:.4f}.
  This deviation from 1 is what breaks the degeneracy and
  could potentially determine α.
""")

    # Compute δ with the full curvature-corrected V_norm
    delta_full = epsilon_required * Delta_omega2 / V_norm_per_delta
    kappa_full = P_cos2phi / abs(delta_full)

    print(f"  With curvature corrections:")
    print(f"    δ_full = {delta_full:.4e} m  (vs δ_flat = {delta_approx:.4e})")
    print(f"    κ_full = {kappa_full:.4e}  (vs κ_flat = {kappa_approx:.4e})")
    print(f"    κ_full/κ_flat = {kappa_full/kappa_approx:.6f}")

    # ═══════════════════════════════════════════════════════════
    # SUMMARY
    # ═══════════════════════════════════════════════════════════
    print(f"\n{'='*65}")
    print(f"SUMMARY")
    print(f"{'='*65}")
    print(f"""
  The backwards calculation reveals a DEGENERACY in the
  flat-space limit:

  1. The stiffness κ = m_ec²/(4π²R²a²) = ε₀E₀²/(2R) is
     independent of α.  It equals the EM energy density
     divided by the major radius.

  2. Both the driving pressure P and the deformation δ
     scale linearly with the coupling ε, so κ = P/δ
     is ε-independent.

  3. The force balance is trivially satisfied for ANY α.
     The flat-space model cannot determine α.

  4. The curvature correction factor
     V_actual/V_flat = {V_norm_per_delta/V_approx:.4f}
     breaks the linear scaling and could determine α.

  NEXT: Track 2 should compute the SELF-CONSISTENT equilibrium
  including curvature corrections.  The nonlinearity from
  the embedded metric is what selects a specific α.

  Physical interpretation: the stiffness {kappa_approx:.2e} Pa/m
  = m_ec²/(4π²R²a²) is the photon's own radiation pressure
  per unit displacement.  The compact space resists deformation
  with the same force that creates the deformation.
""")

    return {
        'r': r_val, 'R': R, 'a': a,
        'epsilon': epsilon_required,
        'delta_flat': delta_approx,
        'delta_full': delta_full,
        'kappa_flat': kappa_approx,
        'kappa_full': kappa_full,
        'V_ratio': V_norm_per_delta / V_approx,
    }


def main():
    print("=" * 65)
    print("R18 Track 1: Backwards Calculation of Stiffness from Known α")
    print("=" * 65)

    for r_val in [0.50]:
        run_track1(r_val)


if __name__ == '__main__':
    main()
