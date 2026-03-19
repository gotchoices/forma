#!/usr/bin/env python3
"""
R18 Track 2: Forward energy balance — does deformation pay?

For the photon on the torus, compute the total energy as a
function of cos(2φ) deformation amplitude δ:

    E_total(δ) = E_photon(δ) + E_Coulomb(δ)

The photon energy is E = hc/L(δ), where L is the path length
on the deformed torus.  The Coulomb energy is Q²/(4πε₀R_eff),
where Q comes from the mode coupling induced by δ.

If E_total has a minimum at finite δ, the torus spontaneously
deforms and charge emerges.  If E_total monotonically increases,
the symmetric torus is stable and the mechanism fails.
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import (h, hbar, c, eps0, mu0, e, alpha as alpha_em,
                            m_e, lambda_C)


def run_track2(r_val, N_delta=60):
    R = lambda_C / (2 * np.pi * np.sqrt(4 + r_val**2))
    a = r_val * R
    E_mc2 = m_e * c**2

    print(f"\n{'='*65}")
    print(f"R18 Track 2: Forward Energy Balance")
    print(f"  r = {r_val:.4f}   R = {R:.4e} m   a = {a:.4e} m")
    print(f"{'='*65}")

    S0 = np.sqrt((a / 2)**2 + R**2)
    L0 = 4 * np.pi * S0

    # ═══════════════════════════════════════════════════════════
    # SECTION 1: Path length on deformed torus
    # ═══════════════════════════════════════════════════════════
    # On the deformed torus (R → R + δcos(2φ)), the (1,2)
    # geodesic has arc-length element:
    # ds/dφ = √(a²/4 + (R + δcos(2φ))²)
    #
    # Path length: L(δ) = ∫₀⁴π ds/dφ dφ

    N_phi = 4000
    phi = np.linspace(0, 4 * np.pi, N_phi, endpoint=False)
    dphi = phi[1] - phi[0]

    delta_max = 0.3 * a
    delta_arr = np.linspace(0, delta_max, N_delta)

    L_arr = np.zeros(N_delta)
    for i, delta in enumerate(delta_arr):
        rho_def = R + delta * np.cos(2 * phi)
        ds = np.sqrt((a / 2)**2 + rho_def**2)
        L_arr[i] = np.sum(ds) * dphi

    E_photon_arr = h * c / L_arr
    dE_photon = E_photon_arr - E_photon_arr[0]

    print(f"\n  SECTION 1: Photon energy from path length")
    print(f"  L₀ = {L0:.6e} m = λ_C = {lambda_C:.6e} m")
    print(f"  E₀ = hc/L₀ = {E_photon_arr[0]:.6e} J = {E_photon_arr[0]/E_mc2:.6f} m_ec²")
    print(f"\n  {'δ/a':>8s}  {'L/L₀':>10s}  {'ΔE/m_ec²':>12s}")
    for idx in [0, N_delta//6, N_delta//3, N_delta//2, 2*N_delta//3, N_delta-1]:
        d = delta_arr[idx]
        print(f"  {d/a:8.4f}  {L_arr[idx]/L0:10.8f}  {dE_photon[idx]/E_mc2:12.4e}")

    # Analytical check: L(δ) ≈ L₀(1 + a²δ²/(16S₀⁴))
    coeff_analyt = a**2 / (16 * S0**4)
    print(f"\n  Analytical: ΔL/L₀ ≈ {coeff_analyt:.4e} × δ²")
    print(f"  → ΔE/m_ec² ≈ {-E_mc2*coeff_analyt/E_mc2:.4e} × δ²")

    # ═══════════════════════════════════════════════════════════
    # SECTION 2: Charge from mode coupling
    # ═══════════════════════════════════════════════════════════
    # The cos(2φ) deformation couples the field pattern
    # cos(θ+2φ) to cos θ through the area element.
    #
    # The charge Q(δ) comes from the cos(2φ) × cos(θ+2φ)
    # cross-term in the area element on the deformed torus.
    #
    # From the analytical derivation:
    # Q = ε₀E₀ × a × δ × ∫∫ cos(θ+2φ)cos(2φ)(R+a cos θ) dθ dφ
    #   = ε₀E₀ × a × δ × aπ²
    #
    # Wait — this integral needs careful treatment.  The field
    # pattern is cos(θ+2φ).  On the deformed torus, the area
    # element includes (R + δcos2φ + a cos θ).  The charge:
    #
    # Q = ε₀E₀ ∫∫ cos(θ+2φ) × a(R + δcos2φ + a cos θ) dθ dφ
    #
    # = ε₀E₀a [R ∫∫cos(θ+2φ)dθdφ
    #           + δ ∫∫cos(θ+2φ)cos(2φ)dθdφ
    #           + a ∫∫cos(θ+2φ)cos θ dθ dφ]
    #
    # Term 1: ∫cos(θ+2φ)dθ = 0 for any φ → 0
    # Term 2: ∫cos(θ+2φ)dθ = 0 for any φ → 0
    # Term 3: ∫cos(θ+2φ)cos θ dθ = π cos(2φ)
    #          then ∫cos(2φ)dφ = 0 → 0
    #
    # ALL THREE TERMS ARE ZERO.
    #
    # The charge of the pure cos(θ+2φ) mode is zero even on
    # the deformed torus.  The cos(2φ) deformation changes the
    # area element but NOT the angular structure of the mode.
    #
    # To get charge, we need the MODE PATTERN to change —
    # i.e., the field must deviate from pure cos(θ+2φ).
    # This happens through the wave equation's mode coupling.
    #
    # On the deformed torus, the eigenmode closest to (1,2)
    # has corrections from mode coupling.  The q=0 admixture
    # (cos θ component) carries charge.
    #
    # From Track 1: ε = V₀δ/Δ(ω²/c²), Q = Q₀ε
    # But those used 2D eigenvalues, not the physical photon.
    #
    # The correct energy to use is the PHYSICAL photon energy
    # m_ec², not the 2D eigenvalue 5.8 m_ec².
    #
    # However, the COUPLING is determined by the 2D geometry
    # (the overlap integral), which is geometry-dependent and
    # correct regardless of which energy we use.
    #
    # The charge Q(δ) = Q₀ × ε(δ) where:
    # ε(δ) = V₀_norm × δ / Δ(ω²/c²)

    # Compute V₀ and Q₀ from Track 1
    N_theta = 10000
    theta = np.linspace(0, 2 * np.pi, N_theta, endpoint=False)
    dtheta = theta[1] - theta[0]
    rho = R + a * np.cos(theta)

    I1 = np.sum(np.cos(theta)**2 / rho**2) * dtheta
    V_weighted = -8 * a * np.pi * I1
    norm_sq = np.pi * a * np.sum(rho) * dtheta  # same for both modes
    V_norm = V_weighted / norm_sq  # per unit δ

    Delta_omega2 = 4.0 / R**2

    V_eff = 2 * np.pi**2 * R * a**2
    E0_sq = E_mc2 / (eps0 * V_eff)
    E0 = np.sqrt(E0_sq)
    Q0 = 2 * np.pi**2 * eps0 * E0 * a**2

    epsilon_arr = V_norm * delta_arr / Delta_omega2
    Q_arr = Q0 * epsilon_arr
    E_Coulomb_arr = Q_arr**2 / (4 * np.pi * eps0 * R)

    print(f"\n  SECTION 2: Charge and Coulomb energy")
    print(f"  V_norm/δ = {V_norm:.4e} m⁻¹")
    print(f"  Q₀ = {Q0:.4e} C")
    print(f"  E₀ = {E0:.4e} V/m")
    print(f"\n  {'δ/a':>8s}  {'ε':>10s}  {'Q/e':>8s}  {'E_C/m_ec²':>12s}")
    for idx in [0, N_delta//6, N_delta//3, N_delta//2, 2*N_delta//3, N_delta-1]:
        d = delta_arr[idx]
        print(f"  {d/a:8.4f}  {epsilon_arr[idx]:10.4e}  "
              f"{Q_arr[idx]/e:8.4f}  {E_Coulomb_arr[idx]/E_mc2:12.4e}")

    # ═══════════════════════════════════════════════════════════
    # SECTION 3: Total energy and stability
    # ═══════════════════════════════════════════════════════════
    E_total = dE_photon + E_Coulomb_arr  # relative to δ=0

    print(f"\n  SECTION 3: Energy balance (no external stiffness)")
    print(f"  {'δ/a':>8s}  {'ΔE_phot':>12s}  {'E_Coulomb':>12s}  "
          f"{'E_total':>12s}  {'Q/e':>8s}")

    for idx in [0, N_delta//6, N_delta//3, N_delta//2, 2*N_delta//3, N_delta-1]:
        d = delta_arr[idx]
        print(f"  {d/a:8.4f}  {dE_photon[idx]/E_mc2:12.4e}  "
              f"{E_Coulomb_arr[idx]/E_mc2:12.4e}  "
              f"{E_total[idx]/E_mc2:12.4e}  "
              f"{Q_arr[idx]/e:8.4f}")

    # Check: at what δ does Q = e?
    idx_Qe = np.argmin(np.abs(np.abs(Q_arr) - e))
    if idx_Qe > 0:
        print(f"\n  At Q = e (α = 1/137):")
        print(f"    δ/a = {delta_arr[idx_Qe]/a:.4f}")
        print(f"    ΔE_photon = {dE_photon[idx_Qe]/E_mc2:.4e} m_ec²")
        print(f"    E_Coulomb = {E_Coulomb_arr[idx_Qe]/E_mc2:.4e} m_ec²")
        print(f"    E_total   = {E_total[idx_Qe]/E_mc2:.4e} m_ec²")
        ratio = abs(E_Coulomb_arr[idx_Qe] / dE_photon[idx_Qe]) if dE_photon[idx_Qe] != 0 else float('inf')
        print(f"    |E_Coulomb/ΔE_photon| = {ratio:.0f}×")

    # ═══════════════════════════════════════════════════════════
    # SECTION 4: Energy scale comparison
    # ═══════════════════════════════════════════════════════════
    print(f"\n  SECTION 4: Energy scale comparison")
    print(f"  {'-'*55}")

    # At δ/a = 0.2 (moderate deformation):
    idx_02 = np.argmin(np.abs(delta_arr/a - 0.2))
    d02 = delta_arr[idx_02]

    print(f"  At δ/a = {d02/a:.3f}:")
    print(f"    Path length change: ΔL/L = {(L_arr[idx_02]-L0)/L0:.2e}")
    print(f"    Photon energy change: {dE_photon[idx_02]/E_mc2:.2e} m_ec²")
    print(f"    Coulomb energy:       {E_Coulomb_arr[idx_02]/E_mc2:.2e} m_ec²")
    print(f"    Charge:               Q = {Q_arr[idx_02]/e:.2f} e")

    # The photon energy change from path length is SECOND ORDER
    # in δ and TINY.  The Coulomb energy is also second order
    # but MUCH LARGER.
    C_path = abs(dE_photon[idx_02]) / d02**2 if d02 > 0 else 0
    C_coul = E_Coulomb_arr[idx_02] / d02**2 if d02 > 0 else 0
    print(f"\n  Energy coefficients (E = C × δ²):")
    print(f"    C_path   = {C_path:.4e} J/m²  (energy SAVED by longer path)")
    print(f"    C_Coulomb = {C_coul:.4e} J/m²  (energy COST from charge)")
    print(f"    C_Coulomb / C_path = {C_coul/C_path:.0f}×")

    # ═══════════════════════════════════════════════════════════
    # SECTION 5: Verdict
    # ═══════════════════════════════════════════════════════════
    print(f"\n{'='*65}")
    print(f"VERDICT")
    print(f"{'='*65}")

    # Is E_total monotonically increasing?
    dE = np.diff(E_total)
    all_increasing = np.all(dE >= -1e-30)

    if all_increasing:
        print(f"""
  NEGATIVE RESULT.  E_total(δ) is monotonically increasing.

  The symmetric torus (δ = 0, Q = 0) is STABLE.
  Geometric deformation cannot spontaneously produce charge.

  Why it fails — energy scale mismatch:

  The photon's energy saving from a longer path is:
    ΔE_photon ≈ -m_ec² × a²δ²/(16S₀⁴) ≈ {-E_mc2*coeff_analyt:.2e} × δ²

  The Coulomb cost of the charge produced is:
    E_Coulomb = Q²/(4πε₀R) ≈ {C_coul:.2e} × δ²

  Ratio: Coulomb/path = {C_coul/C_path:.0f}×

  The Coulomb energy cost DWARFS the photon energy saving
  by a factor of ~{C_coul/C_path:.0f}.  There is no energy advantage
  to deformation.

  Physical reason: the path length changes only at ORDER δ²
  (because ∫cos(2φ)dφ = 0 eliminates the first-order term).
  The resulting energy change is proportional to (δ/S₀)²,
  which is tiny because S₀ ~ R ~ 10⁻¹³ m while δ ~ 10⁻¹⁴ m.
  Meanwhile, the Coulomb energy grows as Q² ∝ δ², with a
  much larger coefficient set by e²/(4πε₀R) ~ α × m_ec².
""")
    else:
        idx_min = np.argmin(E_total)
        print(f"  E_total has a minimum at δ/a = {delta_arr[idx_min]/a:.4f}")
        alpha_pred = Q_arr[idx_min]**2 / (4 * np.pi * eps0 * hbar * c)
        print(f"  Q = {Q_arr[idx_min]/e:.4f} e")
        print(f"  α = {alpha_pred:.4e}  (1/α = {1/alpha_pred:.1f})")

    # ═══════════════════════════════════════════════════════════
    # SECTION 6: What about Track 1's 2D mode analysis?
    # ═══════════════════════════════════════════════════════════
    print(f"  SECTION 6: Reconciliation with Track 1")
    print(f"  {'-'*55}")

    omega2_12 = 1.0 / a**2 + 4.0 / R**2
    omega2_10 = 1.0 / a**2
    E_12 = hbar * c * np.sqrt(omega2_12)
    E_10 = hbar * c * np.sqrt(omega2_10)

    A_coeff = V_norm**2 * hbar**2 * c**2 / Delta_omega2
    C1_2D = A_coeff / (2 * E_12)

    print(f"""
  Track 1 used 2D Laplacian eigenvalues:
    E_{{1,2}} = {E_12/E_mc2:.2f} m_ec²   (2D eigenvalue, NOT m_ec²)
    E_{{1,0}} = {E_10/E_mc2:.2f} m_ec²
    ΔE² = {E_12**2 - E_10**2:.2e} J²

  The 2D mode energy lowering coefficient:
    C₁(2D) = {C1_2D:.2e} J/m²

  The physical photon energy is m_ec² = {1.00} m_ec².
  The 2D eigenvalues are {E_12/E_mc2:.1f}× larger.

  The 2D mode coupling is real (it's a geometric property),
  but the ENERGY available for mode transfer is limited to
  the physical photon energy m_ec², not the 2D eigenvalue.

  The correct energy saving is the PATH-LENGTH effect:
    C_path = {C_path:.2e} J/m²  ({C_path/C1_2D:.1e} × C₁(2D))

  The path-length coefficient is ~{C1_2D/C_path:.0f}× smaller than the
  2D mode-coupling coefficient.  Track 1's "degeneracy" was
  hiding this mismatch — the stiffness κ = P/δ was correct
  but the energy denominator was wrong.
""")


def main():
    print("=" * 65)
    print("R18 Track 2: Forward Energy Balance")
    print("=" * 65)
    run_track2(0.50)


if __name__ == '__main__':
    main()
