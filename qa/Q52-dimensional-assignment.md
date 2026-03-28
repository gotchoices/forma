# Q52. Dimensional assignment constrains the aspect ratio

**Status:** open — r = 1/2 checked; clean but doesn't determine α
**Source:** user question on dimensional assignment
**Connects to:** R15 F5, Q51, Q34

---

## The asymmetry

On flat Ma_e, the two periodic dimensions L₁ and L₂ are
internally symmetric.  But the embedding and the charge
mechanism break this symmetry: the WvM commensurability
condition (p = 1 → E always outward) requires the single
winding to be in the TUBE direction (where the surface
normal rotates).  This forces:

    L₁ = 2πa (tube, p = 1 winding)
    L₂ = 2πR (ring, q = 2 windings)

The assignment is NOT arbitrary — swapping gives p = 2 in
the tube, which destroys the charge mechanism (R13).

## Candidate constraints on r = a/R

- **Equal distance per winding:**
  tube: 2πa per 1 winding = 2πa
  ring: 2πR per 2 windings = πR
  Equal → 2πa = πR → r = 1/2

- **Equal transit time per winding:** same argument if v = c
  in both directions.  Gives r = 1/2.

- **Radiation pattern determines tube shape (Q51):** the
  non-isotropic leakage into 3D shapes the tube, fixing r
  through self-consistency with the field equations.

If any of these fix r, the entire geometry is determined:
R and a follow from the path constraint ℓ = λ_C, with zero
free continuous parameters.

## Quick check for r = 1/2

    R = λ_C / (2π√(4 + 1/4)) = λ_C / (2π√(17/4))
      = λ_C / (π√17) ≈ 5.93 × 10⁻¹⁴ m
    a = R/2 ≈ 2.97 × 10⁻¹⁴ m

Results (check_r_half.py):
- R = λ_C/(π√17) ≈ 1.87 × 10⁻¹³ m ≈ 0.485 λ̄_C ≈ 66.5 r_e
- a = R/2 ≈ 9.37 × 10⁻¹⁴ m
- Equal distance per winding confirmed: 2πa/1 = 2πR/2 ✓
- Coulomb energy = α × m_e c² (same as every Compton-scale
  torus — r doesn't change this)
- Classical current-loop μ/μ_B = 2/(4 + r²) = 8/17 ≈ 0.471
  (but classical approach is wrong; g = 2 comes from the
  spin-1 → spin-½ topology, not from the loop area)
- Does NOT connect to α or any measured quantity

## Verdict

r = 1/2 is a clean geometric choice (equal arc per winding,
R = λ_C/(π√17), etc.) and eliminates the aspect ratio as a
free parameter, but it does not determine α.  α still
requires deriving σ (R15) or the embedding deformation (Q51).
The value r = 1/2 is plausible as a background constraint.
