"""
R59 Track 3: Does the metric produce a Coulomb field?

The question: a charged mode on Ma (standing wave with tube
winding n₁ = 1) sits at the origin in S.  Through the Ma-t
coupling, it perturbs the spacetime metric.  Does this
perturbation:
  a) Fall off as 1/r in S? (= Coulomb potential φ ∝ 1/r)
  b) Have strength proportional to α?
  c) Depend on the sign of the winding (±n₁)?

This is NOT a KK reduction.  It's a direct computation:
  1. The mode has energy E = mc² on Ma
  2. This energy is a source in the stress-energy tensor T_μν
  3. T_μν perturbs the metric: δg_μν = f(T_μν)
  4. The perturbation includes a Ma-t component δg_{Ma,t}
  5. This component IS the electrostatic potential φ

In linearized gravity (weak field):
  δg_μν = -(16πG/c⁴) × ∫ T_μν / |r-r'| d³r'

For a point source at the origin with energy E:
  T₀₀ = E δ³(r)
  δg₀₀ = -(16πG/c⁴) × E / r = -2GM/r = -2φ_grav/c²

The gravitational potential is φ_grav = -GM/r.

For the electromagnetic potential, we need the Ma-t component:
  T_{Ma,t} = (mode energy in Ma) × (Ma-t coupling) × δ³(r)
  δg_{Ma,t} ∝ (coupling × E) / r

If coupling = √α (from the Ma-t off-diagonal):
  δg_{Ma,t} ∝ √α × E / r

The force on a test charge with winding n₁ = 1 is:
  F = n₁ × ∂(δg_{Ma,t})/∂r ∝ n₁ × √α × E / r²

For the force to equal the Coulomb force:
  F = α × E / r² (in natural units)

This gives: coupling = √α, consistent with what we found
in Track 1 (σ ≈ 0.0084 ≈ √(α × geometric_factor)).

Let's verify this numerically.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from lib.ma_model_d import M_E_MEV, M_P_MEV, _TWO_PI_HC

ALPHA = 1.0 / 137.036
TWO_PI_HC = _TWO_PI_HC


def main():
    print("=" * 75)
    print("R59 Track 3: Does the metric produce a Coulomb field?")
    print("=" * 75)
    print()

    # ── Part 1: The argument from linearized gravity ───────
    print("─" * 75)
    print("Part 1: Linearized gravity argument")
    print("─" * 75)
    print()
    print("  In linearized gravity, a point source with stress-energy T_μν")
    print("  produces a metric perturbation:")
    print()
    print("    δg_μν(r) = -(16πG/c⁴) × T_μν / (4π r)")
    print()
    print("  For gravity (T₀₀ = Mc², the mass-energy):")
    print("    δg₀₀ = -2GM/(c² r) = -2φ_grav/c²")
    print("    → Newtonian potential φ_grav = -GM/r  ✓")
    print()
    print("  For electromagnetism, the source is not T₀₀ but the")
    print("  CROSS component T_{Ma,t} — the mode's energy in Ma")
    print("  coupled to the time direction.")
    print()
    print("  If the Ma-t coupling strength is σ, then the effective")
    print("  stress-energy in the Ma-t component is:")
    print("    T_{Ma,t} ∝ σ × Mc²")
    print()
    print("  And the metric perturbation in the Ma-t direction is:")
    print("    δg_{Ma,t}(r) ∝ σ × GM/(c² r)")
    print()
    print("  A test particle with winding n₁ on Ma feels a force:")
    print("    F = n₁ × ∂(δg_{Ma,t})/∂r ∝ n₁ × σ × GM/r²")
    print()
    print("  The sign of n₁ determines attraction vs repulsion:")
    print("    n₁ = +1 (same as source): force is repulsive")
    print("    n₁ = -1 (opposite):       force is attractive")
    print()

    # ── Part 2: Compare to Coulomb's law ───────────────────
    print("─" * 75)
    print("Part 2: Match to Coulomb's law")
    print("─" * 75)
    print()
    print("  Coulomb's law (natural units, c = ℏ = 1):")
    print("    F = α × e₁ × e₂ / r²")
    print("    where e₁, e₂ are charges in units of e = √(4πα)")
    print()
    print("  From the metric perturbation:")
    print("    F = n₁ × σ² × (GM/r²)")
    print()
    print("  For a charged particle with Q = n₁ = ±1:")
    print("    F = σ² × GM/r²")
    print()
    print("  For this to equal the Coulomb force F = α/r² (in units")
    print("  where e² = 4πα, and the source has Q = 1):")
    print("    σ² × GM = α")
    print()
    print("  In natural units (G = 1, M = particle mass in Planck units):")
    print("    σ² × M_Planck_units = α")
    print()

    # ── Part 3: What Track 1 found vs what Coulomb requires ─
    print("─" * 75)
    print("Part 3: What Track 1 found vs what Coulomb requires")
    print("─" * 75)
    print()

    # Track 1d found: σ = 0.00843 on the ring-t entry
    # This gives ΔE/E = α for the electron (particle root)
    sigma_D1 = 0.00843

    print(f"  Track 1d found: σ = {sigma_D1:.5f}")
    print(f"  σ² = {sigma_D1**2:.6e}")
    print(f"  α = {ALPHA:.6e}")
    print(f"  σ²/α = {sigma_D1**2/ALPHA:.4f}")
    print(f"  σ/√α = {sigma_D1/math.sqrt(ALPHA):.4f}")
    print()

    # In the mass-shell computation, the coupling appears as
    # the cross-term b in a ω² + b ω + c = 0.
    # The splitting δω ≈ b/(2a) ≈ σ × (geometric factor).
    # The mass shift ΔE/E ≈ δω/ω₀.

    # The Coulomb self-energy of a point charge:
    #   U_Coulomb = α × mc² / (2 R_charge)
    # For a torus of ring circumference L_ring:
    #   R_charge ~ L_ring / (2π)
    #   U_Coulomb ~ α × mc² × (2π) / L_ring × (something)

    # But what Track 1 actually computed is:
    #   ΔE/E = α (tuned)
    # This is the FRACTIONAL mass shift, not the absolute coupling.

    print("  The key question: is ΔE/E = α the SAME as the Coulomb")
    print("  coupling α?")
    print()
    print("  In standard physics, the Coulomb self-energy of the electron:")
    print("    U_Coulomb = (3/5) × α × mc² / R")
    print("  where R is the charge radius.  For a point charge, R → 0")
    print("  and U → ∞ (the classical self-energy divergence).")
    print()
    print("  For a torus of size L_ring:")
    print(f"    R ~ L_ring/(2π) = {11.88/(2*math.pi):.2f} fm (electron)")
    print(f"    U_Coulomb ~ α × mc² × (mc² / (ℏc/R))")

    # More precisely: the Coulomb self-energy of a charge e
    # distributed uniformly on a ring of radius R is:
    #   U = e²/(4πε₀) × (1/R) × (logarithmic correction)
    # In natural units:
    #   U = α / R
    # And U/mc² = α / (mc² R / ℏc) = α / (R / λ_Compton)

    R_ring = 11.88 / (2 * math.pi)  # fm
    lambda_C = 2 * math.pi * 197.3 / M_E_MEV  # Compton wavelength in fm
    print(f"    R/λ_C = {R_ring / lambda_C:.4f}")
    print(f"    U/mc² = α / (R/λ_C) = {ALPHA / (R_ring/lambda_C):.4f}")
    print()
    print("  Hmm — this gives U/mc² ≈ α × (λ_C/R), not α.")
    print(f"  λ_C/R = {lambda_C/R_ring:.2f}")
    print(f"  So U/mc² ≈ {ALPHA * lambda_C/R_ring:.4f}, not {ALPHA:.4f}")
    print()
    print("  The Track 1 result ΔE/E = α is NOT the Coulomb self-energy")
    print("  of a charge distributed on the torus.  It's something else")
    print("  — a metric coupling effect that HAPPENS to equal α.")
    print()

    # ── Part 4: What ΔE/E = α actually means ──────────────
    print("─" * 75)
    print("Part 4: What ΔE/E = α actually means")
    print("─" * 75)
    print()
    print("  The mass-shell condition gives:")
    print("    E_particle = E_bare × (1 + δ)")
    print("    E_antiparticle = E_bare × (1 - δ)")
    print()
    print(f"  We tuned σ so that δ = α = {ALPHA:.6f}")
    print()
    print("  What IS δ physically?  It's the fractional energy shift")
    print("  caused by the Ma-t coupling.  The coupling mixes the")
    print("  Ma winding with the time direction, creating a charge-")
    print("  dependent energy offset.")
    print()
    print("  In KK theory, this offset IS the gauge coupling.")
    print("  A particle with compact momentum p₅ = n/R has energy:")
    print("    E² = m₀² + p₅² + 2 e A₀ p₅ + e² A₀²")
    print("  where A₀ is the electrostatic potential and e is the")
    print("  gauge coupling.  The linear term (2 e A₀ p₅) gives the")
    print("  charge-dependent energy shift.")
    print()
    print("  But our model uses standing waves, not compact momentum.")
    print("  The question remains: does our δ = α produce the correct")
    print("  SPATIAL field (1/r² Coulomb) or just a self-energy shift?")
    print()

    # ── Part 5: The spatial field test ─────────────────────
    print("─" * 75)
    print("Part 5: Can we test the spatial dependence?")
    print("─" * 75)
    print()
    print("  The Track 1 computation puts the mode at one point in S")
    print("  and asks: what is its energy?  This is a GLOBAL (integrated)")
    print("  quantity — it doesn't tell us about the SPATIAL PROFILE")
    print("  of the field in S.")
    print()
    print("  To test 1/r² spatial dependence, we would need to:")
    print("  1. Place a source mode at the origin")
    print("  2. Compute the metric perturbation at various distances r")
    print("  3. Verify δg_{Ma,t}(r) ∝ 1/r")
    print()
    print("  This requires a spatially-extended computation — not just")
    print("  the single-point mass-shell condition.  The metric")
    print("  perturbation is a FIELD in S sourced by the mode's energy")
    print("  density on Ma.")
    print()
    print("  In linearized gravity, the perturbation is:")
    print("    δg_μν(x) = -4G × ∫ T_μν(x') / |x - x'| d³x'")
    print()
    print("  For a point source at the origin: T(x') = T₀ δ³(x')")
    print("  → δg(r) = -4G × T₀ / r")
    print()
    print("  For a torus-shaped source: T(x') is distributed on the torus.")
    print("  At distances r >> L_ring: looks like a point source → 1/r.")
    print("  At r ~ L_ring: corrections from the torus shape.")
    print("  At r << L_ring: inside the torus, field structure changes.")
    print()
    print("  The key prediction: at r >> L_ring (which is all of")
    print("  classical physics), the field is 1/r (potential) and")
    print("  1/r² (force), regardless of the torus shape.  The shape")
    print("  only matters at the Compton scale.")
    print()

    # ── Part 6: What can we conclude? ──────────────────────
    print("─" * 75)
    print("Part 6: Conclusions")
    print("─" * 75)
    print()
    print("  What Track 1 established:")
    print("    - The Ma-t coupling produces a charge-dependent energy")
    print("      offset δE = ±α × mc² (particle vs antiparticle)")
    print("    - The offset is universal to 1.8% across e and p sheets")
    print("    - The offset has the correct sign (particle heavier)")
    print()
    print("  What Track 3 adds:")
    print("    - The linearized gravity argument shows that a localized")
    print("      source with Ma-t coupling produces a 1/r perturbation")
    print("      in S — this is the Coulomb potential")
    print("    - The 1/r dependence follows from the Green's function")
    print("      of the 3D Laplacian, which is a property of S (3D space),")
    print("      not of the coupling mechanism")
    print("    - The STRENGTH of the perturbation is proportional to")
    print("      σ × M, where σ is the Ma-t coupling and M is the mass")
    print("    - The SIGN depends on the winding number n₁ (charge)")
    print()
    print("  What remains uncertain:")
    print("    - The exact relationship between σ (metric entry) and")
    print("      α (coupling constant): is σ = √α, σ = α, or something")
    print("      else?  Track 1 tuned σ to give ΔE/E = α, but the")
    print("      Coulomb self-energy on a torus gives a different number")
    print("    - The KK reduction for standing waves (vs compact momentum)")
    print("      has not been done — the argument above uses the")
    print("      linearized gravity framework, which treats the source")
    print("      as a point, not as a standing wave")
    print()
    print("  Bottom line: the Ma-t metric coupling produces the right")
    print("  QUALITATIVE behavior (1/r spatial dependence, charge sign,")
    print("  universality).  The QUANTITATIVE relationship between σ")
    print("  and α requires either a full KK reduction for standing")
    print("  waves or a numerical computation of the spatial field")
    print("  profile.  Both are beyond the current track's scope.")
    print()
    print("Track 3 complete.")


if __name__ == '__main__':
    main()
