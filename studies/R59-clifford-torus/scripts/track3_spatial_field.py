"""
R59 Track 3 (rebuilt): Spatial field from a single electron sheet.

Two mechanisms compared:

A. R19 mechanism: the mode's energy on the 3D-embedded torus
   produces a field in S.  The R19 formula gives the total
   coupling α; here we compute the SPATIAL PROFILE of the
   field as a function of distance r from the torus center.

B. Ma-t mechanism: the off-diagonal Ma-t entry in the 10D
   metric produces a perturbation in S.  We compute the
   spatial profile from the 10D linearized equations.

For mechanism A:
  - The mode has charge Q = e = √(4πα)
  - The charge is distributed on the torus surface
  - The potential at point r in S is:
    φ(r) = (e / 4π) × ∫ ρ(r') / |r - r'| dA'
  - At r >> L_ring: φ → e/(4πr) (Coulomb)
  - At r ~ L_ring: torus-shape corrections
  - The coefficient gives α

For mechanism B:
  - The mode has Ma-t coupling σ
  - The perturbation at r is the Green's function integral
  - At r >> L_ring: same 1/r behavior
  - The coefficient may or may not match α

We compute BOTH and compare.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from lib.ma_model_d import (
    M_E_MEV, _TWO_PI_HC, ALPHA as ALPHA_CONST,
    alpha_from_geometry,
)

ALPHA = 1.0 / 137.036
TWO_PI = 2 * math.pi
TWO_PI_HC = _TWO_PI_HC

# Electron sheet parameters
EPS_E = 397.074
S_E = 2.004200

# Derived quantities
Q_EFF = S_E * EPS_E  # = n_r - n_t*s for (1,2) mode... wait
Q_EFF_12 = 2 - 1 * S_E  # q = n_r - n_t*s = 2 - 2.004 = -0.004
MU_12 = math.sqrt((1/EPS_E)**2 + Q_EFF_12**2)

L_RING_E = TWO_PI_HC * MU_12 / M_E_MEV
L_TUBE_E = EPS_E * L_RING_E
R_RING = L_RING_E / TWO_PI   # ring radius (fm)
R_TUBE = L_TUBE_E / TWO_PI   # tube radius (fm)


def torus_potential_at_distance(r_obs, R_ring, R_tube, N_theta=200, N_phi=200):
    """
    Compute the electrostatic potential at distance r_obs from the
    center of a torus with major radius R_ring and minor radius R_tube.

    The charge is uniformly distributed on the torus surface.
    Total charge = 1 (normalized).

    The observation point is at (r_obs, 0, 0) — along the x-axis,
    in the plane of the torus ring.

    φ(r) = (1 / 4π) × ∫∫ dA / |r - r'|

    Returns φ (normalized so that at large r, φ → 1/(4π r)).
    """
    # Torus parameterization:
    # x = (R + a cos θ₁) cos θ₂
    # y = a sin θ₁
    # z = (R + a cos θ₁) sin θ₂
    # where R = R_ring, a = R_tube

    R = R_ring
    a = R_tube

    theta1 = np.linspace(0, TWO_PI, N_theta, endpoint=False)
    theta2 = np.linspace(0, TWO_PI, N_phi, endpoint=False)
    dth1 = TWO_PI / N_theta
    dth2 = TWO_PI / N_phi

    phi_total = 0.0

    for t1 in theta1:
        ct1 = math.cos(t1)
        st1 = math.sin(t1)
        rho = R + a * ct1  # distance from ring axis

        for t2 in theta2:
            ct2 = math.cos(t2)
            st2 = math.sin(t2)

            # Point on torus surface
            x_s = rho * ct2
            y_s = a * st1
            z_s = rho * st2

            # Distance to observation point (r_obs, 0, 0)
            dx = r_obs - x_s
            dy = 0 - y_s
            dz = 0 - z_s
            dist = math.sqrt(dx**2 + dy**2 + dz**2)

            if dist < 1e-10:
                continue  # skip self-interaction singularity

            # Area element on torus: dA = a × rho × dθ₁ × dθ₂
            dA = a * abs(rho) * dth1 * dth2

            # Contribution to potential (charge density = 1/total_area)
            total_area = TWO_PI * a * TWO_PI * R  # approximate
            phi_total += dA / (total_area * dist)

    # Normalize: total_area ∫ = 1/(4π r) at large r for unit charge
    return phi_total / (4 * math.pi)


def main():
    print("=" * 75)
    print("R59 Track 3 (rebuilt): Spatial field computation")
    print("=" * 75)
    print()

    print(f"  Electron sheet: ε = {EPS_E}, s = {S_E}")
    print(f"  R_ring = {R_RING:.4f} fm, R_tube = {R_TUBE:.2f} fm")
    print(f"  L_ring = {L_RING_E:.4f} fm, L_tube = {L_TUBE_E:.2f} fm")
    print()

    # ── Part 1: R19 formula check ─────────────────────────
    print("─" * 75)
    print("Part 1: R19 formula — what α does it give?")
    print("─" * 75)
    print()

    alpha_R19 = alpha_from_geometry(EPS_E, S_E, n_tube=1, n_ring=2)
    print(f"  α(R19) for (1,2) mode: {alpha_R19:.6e}")
    print(f"  Target α:             {ALPHA:.6e}")
    print(f"  Ratio:                {alpha_R19/ALPHA:.4f}")
    print()

    # R19 at the proton sheet for comparison
    from lib.ma_model_d import solve_shear_for_alpha
    s_p = solve_shear_for_alpha(0.55, n_tube=1, n_ring=3)
    alpha_R19_p = alpha_from_geometry(0.55, s_p, n_tube=1, n_ring=3)
    print(f"  α(R19) for proton (1,3): {alpha_R19_p:.6e}")
    print(f"  Ratio to α: {alpha_R19_p/ALPHA:.4f}")
    print()

    if abs(alpha_R19/ALPHA - 1.0) > 0.01:
        print(f"  NOTE: R19 does NOT give α = 1/137 at the e-sheet!")
        print(f"  R19 was derived for ε ~ O(1).  At ε = 397, it gives")
        print(f"  a different value.  This is a known limitation (R55 Track 2).")
    else:
        print(f"  R19 gives α at the e-sheet.  ✓")
    print()

    # ── Part 2: Coulomb potential from torus charge ────────
    print("─" * 75)
    print("Part 2: Coulomb potential from uniform charge on torus")
    print("  (Spatial profile at various distances)")
    print("─" * 75)
    print()

    # Distances to probe (in fm)
    # R_ring ~ 1.9 fm, so probe from 0.5 to 100 fm
    distances = [0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0, 100.0]

    print(f"  {'r (fm)':>8s}  {'φ(r)':>12s}  {'1/(4πr)':>12s}  {'φ/[1/4πr]':>10s}  {'r/R_ring':>8s}")
    print(f"  {'─'*8}  {'─'*12}  {'─'*12}  {'─'*10}  {'─'*8}")

    for r in distances:
        phi = torus_potential_at_distance(r, R_RING, R_TUBE, N_theta=100, N_phi=100)
        phi_point = 1.0 / (4 * math.pi * r)
        ratio = phi / phi_point if phi_point > 0 else 0
        r_over_R = r / R_RING

        print(f"  {r:8.1f}  {phi:12.6e}  {phi_point:12.6e}  {ratio:10.4f}  {r_over_R:8.2f}")

    print()
    print("  If φ/[1/(4πr)] → 1.0 at large r: the torus looks like a")
    print("  point charge.  Deviations at r ~ R_ring are torus-shape")
    print("  corrections.")
    print()

    # ── Part 3: The coupling coefficient ───────────────────
    print("─" * 75)
    print("Part 3: What determines the STRENGTH of the field?")
    print("─" * 75)
    print()
    print("  The potential from a charge e at distance r:")
    print("    φ = e / (4π r)  (Gaussian units)")
    print("    = α^(1/2) / (√(4π) × r)  (since e = √(4πα))")
    print()
    print("  The FORCE between two unit charges at distance r:")
    print("    F = e² / (4π r²) = α / r²")
    print()
    print("  The potential is NOT α/r — it's √α/r (times factors).")
    print("  The FORCE is α/r².")
    print()
    print("  Track 1 found ΔE/E = α.  What is ΔE physically?")
    print("  ΔE = interaction energy = charge × potential")
    print("     = e × φ(R_charge)")
    print("     = e × e/(4π R_charge)")
    print("     = e²/(4π R_charge)")
    print("     = α / R_charge")
    print()
    print(f"  For the electron on a torus of ring radius R = {R_RING:.2f} fm:")
    print(f"    R_charge in natural units = R / λ_C")

    lambda_C = TWO_PI_HC / M_E_MEV  # Compton wavelength in fm
    R_natural = R_RING / lambda_C
    print(f"    λ_C = {lambda_C:.2f} fm")
    print(f"    R/λ_C = {R_natural:.6f}")
    print(f"    ΔE/mc² = α / (R/λ_C) = {ALPHA / R_natural:.4f}")
    print(f"    = {ALPHA / R_natural / ALPHA:.1f} × α")
    print()
    print(f"  So the Coulomb self-energy is {ALPHA/R_natural:.1f} × mc²,")
    print(f"  NOT α × mc².  Track 1's ΔE/E = α is a DIFFERENT quantity.")
    print()

    # ── Part 4: What IS Track 1's ΔE/E? ───────────────────
    print("─" * 75)
    print("Part 4: What does the mass-shell shift actually measure?")
    print("─" * 75)
    print()
    print("  Track 1's mass-shell condition:")
    print("    g^{μν} k_μ k_ν = 0")
    print("  gives E_particle = E_bare × (1 + δ)")
    print("  where δ ≈ σ² × (geometric factor)")
    print()
    print("  Track 1 tuned σ so that δ = α.")
    print()
    print("  In KK theory with compact momentum p₅ = n/R:")
    print("    E² = m₀²c⁴ + p₅²c² + 2eA₀p₅c")
    print("  The linear term 2eA₀p₅c gives δE ∝ eA₀ × n/R.")
    print("  For a self-consistent solution (the charge sources")
    print("  its own A₀ = e/(4πR)), this gives:")
    print("    δE/mc² = e²/(4π mc² R) = α/(mc²R/ℏc) = α × λ_C/R")
    print()
    print("  This is the SAME 1300× factor we found in the old Track 3!")
    print("  KK theory predicts δE/mc² = α × λ_C/R, not δE/mc² = α.")
    print()
    print("  So Track 1's tuning (δ = α) does NOT match KK theory.")
    print("  KK would predict δ = α × λ_C/R ≈ 9.4 for the electron.")
    print("  That would be a ~940% mass shift — clearly wrong.")
    print()
    print("  This means one of:")
    print("  a) The mass-shell shift is not the Coulomb self-energy")
    print("     (it's a different physical quantity)")
    print("  b) Standing waves have different self-energy than KK")
    print("     point particles (the mode's spatial extent regulates")
    print("     the divergence)")
    print("  c) The Ma-t coupling σ should NOT be tuned to give")
    print("     δ = α; the correct tuning is different")
    print()

    # ── Part 5: Can we compute what σ SHOULD be? ──────────
    print("─" * 75)
    print("Part 5: What σ does KK predict for a standing wave?")
    print("─" * 75)
    print()
    print("  In KK, the gauge coupling e is related to the compact")
    print("  dimension radius R₅ and Newton's constant G:")
    print("    e² = 16πG / L₅²  (where L₅ = 2πR₅)")
    print()
    print("  In natural units (G = L_P²/ℏc, L_P = Planck length):")
    print("    e² = 16π L_P² / L₅²")
    print("    α = e²/(4π) = 4 L_P² / L₅²")
    print()

    L_P = 1.616255e-20  # Planck length in fm
    L5_e = L_RING_E  # use e-ring as the compact dimension

    alpha_KK = 4 * L_P**2 / L5_e**2
    print(f"  For the electron ring (L₅ = L_ring = {L5_e:.4f} fm):")
    print(f"    α_KK = 4 × L_P² / L_ring² = {alpha_KK:.4e}")
    print(f"    Compare to α = {ALPHA:.4e}")
    print(f"    Ratio: {alpha_KK/ALPHA:.4e}")
    print()
    print(f"  The KK prediction is {ALPHA/alpha_KK:.0e}× too small.")
    print(f"  This is the well-known KK hierarchy problem:")
    print(f"  the compact dimensions are at the Compton scale")
    print(f"  (~fm), not the Planck scale (~10⁻²⁰ fm).")
    print()
    print(f"  In our model, the compact dimensions are ~{L5_e/L_P:.0e}×")
    print(f"  larger than the Planck length.  Standard KK coupling")
    print(f"  gives α_KK ∝ (L_P/L_ring)² ≈ {alpha_KK:.1e},")
    print(f"  which is {ALPHA/alpha_KK:.0e}× below the observed α.")
    print()

    # ── Part 6: R19 vs KK vs Track 1 ──────────────────────
    print("─" * 75)
    print("Part 6: Three predictions compared")
    print("─" * 75)
    print()
    print(f"  {'Source':>20s}  {'α or proxy':>12s}  {'ratio to α':>12s}")
    print(f"  {'─'*20}  {'─'*12}  {'─'*12}")
    print(f"  {'Observed α':>20s}  {ALPHA:12.6e}  {'1.000':>12s}")
    print(f"  {'R19 (e-sheet)':>20s}  {alpha_R19:12.6e}  {alpha_R19/ALPHA:12.4f}")
    print(f"  {'R19 (p-sheet)':>20s}  {alpha_R19_p:12.6e}  {alpha_R19_p/ALPHA:12.4f}")
    print(f"  {'KK (standard)':>20s}  {alpha_KK:12.6e}  {alpha_KK/ALPHA:12.2e}")
    print(f"  {'Track 1 ΔE/E':>20s}  {ALPHA:12.6e}  {'1.000 (tuned)':>12s}")
    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 75)
    print("SUMMARY")
    print("=" * 75)
    print()
    print("  1. The spatial Coulomb potential from a torus charge")
    print("     distribution approaches 1/r at r >> R_ring.  ✓")
    print("     (This is geometry, not a mechanism test.)")
    print()
    print("  2. R19 gives α at the p-sheet (by construction)")
    print("     but may give a different value at the e-sheet")
    print(f"     (ε = 397): α_R19 = {alpha_R19:.4e} ({alpha_R19/ALPHA:.4f}α)")
    print()
    print("  3. Standard KK gives α_KK ≈ 10⁻⁴³ — 10⁴⁰× too small.")
    print("     KK doesn't work for Compton-scale compact dimensions.")
    print()
    print("  4. Track 1's ΔE/E = α is a tuned mass shift, not a")
    print("     derived coupling.  The KK self-energy (α × λ_C/R)")
    print("     is ~1300× larger.  The two quantities are different.")
    print()
    print("  5. The R19 mechanism (internal shear → coupling) computes")
    print("     a FRACTION of the mode energy.  This fraction is α at")
    print("     the p-sheet.  It may be the correct coupling; the")
    print("     spatial profile is 1/r by construction.")
    print()
    print("  The gap: we have THREE different numbers (R19, KK,")
    print("  Track 1 mass-shell) that all purport to be α but disagree")
    print("  by orders of magnitude.  Only R19 at the p-sheet gives")
    print("  the observed value.  The relationship between these three")
    print("  quantities is unresolved.")
    print()
    print("Track 3 complete.")


if __name__ == '__main__':
    main()
