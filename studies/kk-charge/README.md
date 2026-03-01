# KK Charge Comparison  *(draft)*

Does WvM's charge derivation reduce to the Kaluza-Klein charge
quantum? This determines whether the compact-dimension framework
is the right theoretical foundation for the project.

## Why this is first

Every study after this depends on the answer. If WvM reduces to
KK, we have a principled framework (5D geodesics, Noether charge,
established math). If it doesn't, we need to understand exactly
where the gap is before building further.

## The two charge derivations

**WvM (1997):** Confine a photon of wavelength λ to a sphere of
diameter λ. Average E-field inside: ⟨E⟩ = √(6hc / πε₀λ⁴).
Match to Coulomb field at r = λ/4π:

    q_WvM = (1/2π) √(3ε₀ℏc) ≈ 0.91e

**Kaluza-Klein:** Momentum in a compact dimension of circumference
L is quantized: p_w = nℏ/L. This momentum manifests as charge:

    q_KK = n · ℏ / (R_KK · c)

where R_KK = L/(2π) is the compact radius and n is the winding
number.

## What to check

1. **Algebraic comparison.** Set q_WvM = q_KK and solve for R_KK.
   Does the implied compact radius relate to any WvM length scale
   (λ_C/4π, λ_C/2, the torus parameters)?

2. **Dimensional analysis.** Both formulas produce a charge from
   ℏ and c. Are they algebraically the same expression with
   different names for the geometric parameters, or are they
   structurally different?

3. **If they match:** the compact dimension circumference L is
   determined. What is it in terms of λ_C? Does it correspond to
   the path length (λ_C), the orbital circumference (λ_C/2), or
   something else?

4. **If they don't match:** what specifically differs? Is WvM's
   charge an approximation to KK's (with geometric corrections)?
   Or are they different mechanisms entirely?

5. **The α connection.** Our study 2 found a/R = 1/√(πα) gives
   q = e exactly (by inverting the WvM formula). In KK, α = e²/(4πε₀ℏc)
   relates the charge quantum to the compact radius. Do these two
   appearances of α unify?

## Expected outcomes

- **Best case:** WvM charge = KK charge with a specific
  identification of the compact radius. The entire WvM model
  becomes a specific KK solution. Confinement dissolves.

- **Partial match:** WvM charge ≈ KK charge with geometric
  corrections (the ~9% deficit maps to a specific geometric
  factor). The framework is KK but the details need refinement.

- **No match:** The mechanisms are structurally different. The
  compact dimension hypothesis needs independent justification,
  or WvM is not a KK theory at all.

## Approach

This is pure algebra — no computation needed. Read the KK charge
derivation carefully, substitute the WvM parameters, and compare.
The result is either an identity, an approximation, or a
contradiction.

Key references:
- WvM paper §3 (charge derivation): `ref/WvM.pdf`
- KK charge quantization: standard reference (Kaluza 1921,
  Klein 1926, or any modern review)
- A7 §4 (our KK summary): `answers/A7-flat-compact-dimensions.md`
