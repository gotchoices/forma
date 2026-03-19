# R19. Shear-induced charge on T²

**Questions:** [Q58](../../qa/INBOX.md) (shear breaks φ-symmetry),
[Q18](../../qa/Q18-deriving-alpha.md) (deriving α),
Q34 Path 7 (charge mechanism)
**Type:** analytical + compute
**Depends on:** R12 (shear unconstrained, two-domain picture),
R15 (forward charge, what determines σ),
R18 (geometric deformation ruled out)

---

## Motivation

Every mechanism tested for deriving α — Coulomb soliton (R15 F9),
centrifugal radiation pressure (R17), geometric torus deformation
(R18) — has been blocked by the same obstruction: the charge
integral of the (1,2) mode cos(θ+2φ) vanishes when integrated
over a full φ period.  This is the **φ-symmetry protection**.

But on a **sheared T²** (lattice vectors non-orthogonal), the
(1,2) mode acquires a non-integer effective winding number
q_eff = 2 − δ/L₁ in the embedding coordinates.  The charge
integral becomes:

    Q ∝ sin(πq_eff) / q_eff

which is **nonzero** for non-integer q_eff.  This is the first
mechanism found that produces charge from a **fully delocalized**
wave, without requiring wavepacket localization (σ < ∞).

The shear δ is a geometric parameter of the compact-space metric.
R12 F5 showed it is **unconstrained** by the flat-T² wave
equation — exactly the condition where an external constraint
(T³ geometry, embedding curvature, topological consistency)
could determine it.

If shear determines charge, then:
- The question "what determines σ?" is replaced by
  "what determines δ?"
- δ is geometric (metric parameter), not quantum-state
- α = Q²/(4πε₀ℏc) becomes a function of δ alone
- The same T³ geometry needed for quark confinement (R14)
  may constrain the shear, thereby fixing α

---

## Tracks

### Track 1. Backwards: derive required shear from known α  *(planned)*

Input the known α = 1/137.036... and solve for the shear δ
that produces Q = e.

Steps:
1. Set up the charge integral on the sheared T² with the
   (1,2) mode field pattern, using the correct E₀ normalization
   (photon energy m_e c² distributed over the torus volume).
2. Compute Q(δ) analytically and/or numerically.
3. Solve Q(δ) = e for δ.
4. Express δ in natural geometric units: δ/a, δ/R, δ/λ_C.
5. Check: does the required shear "make sense"?
   - Is it a small perturbation (δ ≪ a) or a large distortion?
   - Does it correspond to a recognizable angle (e.g., related
     to the aspect ratio, winding number, or topology)?
   - Is it consistent with the flat-space approximation
     (shear must not induce significant curvature)?
   - Does it match any known geometric quantity from R12?

**Success criterion:** The required δ is a "natural" value —
small enough to be a perturbation, with a recognizable geometric
interpretation.

### Track 2. Energy analysis: is non-zero shear stable?  *(planned)*

On the flat T², mode energy is shear-independent (R12 F5), so
the Coulomb self-energy of the charge makes δ = 0 the energy
minimum.  But:
- The T² is embedded in 3D with specific curvature
- Gravitational (or metric) effects from the embedding may
  contribute a term that favors nonzero shear
- T³ constraints (R14) may impose shear externally

Investigate whether any energy contribution can stabilize
a nonzero shear:
1. Compute E_Coulomb(δ) = Q(δ)²/(4πε₀ R_eff)
2. Check if embedding curvature contributes a δ-dependent
   energy term (from the extrinsic curvature of T² in 3D)
3. If T³ topology constrains the shear moduli space, identify
   the constraint and its effect on δ

### Track 3. Normalization reconciliation  *(planned)*

Previous calculations have shown a persistent discrepancy in
the absolute charge normalization (~0.46e vs. 8e for max shear)
depending on whether E₀ uses a line-source or volume-averaged
convention.  Establish the correct E₀ normalization from first
principles:
1. Total photon energy = m_e c² = ∫(ε₀E² + B²/μ₀)dV / 2
2. Solve for E₀ given the mode structure and torus volume
3. Recompute Q(δ) with the correct normalization
4. Verify consistency with R15's charge calculation

### Track 4. Connection to T³ and quark charges  *(deferred)*

If T³ has three shear parameters (one per pair of axes), and
the electron uses one of them:
- Does the shear that gives Q = e also give fractional charges
  Q = e/3, 2e/3 for the other two shear directions?
- Is this connected to R14's quark-confinement geometry?

This track depends on the T³ framing (R14) and is deferred
until Tracks 1–3 produce definitive results.

---

## Key equations

**Sheared T² metric:**

    ds² = dθ² + 2(δ/a) dθ dφ + (1 + (δ/a)²) dφ²

where θ ∈ [0, 2πa), φ ∈ [0, 2πR), and δ is the shear
displacement (θ-direction offset per φ-period).

**Mode on sheared T²:**

    ψ(θ,φ) = exp[i(m θ/a + n φ/R)]

For the (1,2) knot: m=1, n=2.  In embedding coordinates
(where the charge integral is defined), the effective
φ-winding becomes q_eff = n − m δ/a = 2 − δ/a.

**Charge integral:**

    Q = (2ε₀ E₀ / R) × ∫∫ cos(θ/a + q_eff φ/R) √g dθ dφ

For q_eff ∉ ℤ, this is proportional to sin(2π q_eff)/q_eff ≠ 0.

---

## Status

**Created:** 2026-03-01
**Status:** framed — ready for Track 1
