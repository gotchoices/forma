# R19. Shear-induced charge on T² → T³

**Questions:** [Q58](../../qa/INBOX.md) (shear breaks φ-symmetry),
[Q18](../../qa/Q18-deriving-alpha.md) (deriving α),
Q34 Path 7 (charge mechanism)
**Type:** analytical + compute
**Depends on:** R12 (shear unconstrained, two-domain picture),
R15 (forward charge, what determines σ),
R18 (geometric deformation ruled out),
R14 (universal geometry — T³ for quarks, linking)

---

## Motivation

Every mechanism tested for deriving α — Coulomb soliton (R15 F9),
centrifugal radiation pressure (R17), geometric torus deformation
(R18) — has been blocked by the same obstruction: the charge
integral of the (1,2) mode cos(θ+2φ) vanishes when integrated
over a full φ period.  This is the **φ-symmetry protection**.

But on a **sheared T²** (lattice vectors non-orthogonal), the
(1,2) mode acquires a non-integer effective winding number
q_eff = 2 − s in the embedding coordinates, where s = δ/(2πa)
is the fractional shear.  The charge integral becomes:

    Q ∝ sin(2πs) / (2 − s)

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

### The paradigm shift: particle-like → wave

Studies R2–R18 modeled the photon semi-classically: it has a
*position* on the geodesic, its E-field "points outward" at
that position, and charge arises from the time-averaged monopole
moment of the rotating field pattern (the WvM picture).  In
that model:

- A fully delocalized wave → charge = 0 (exact cancellation)
- Charge requires partial localization (σ < ∞)
- σ is a quantum-state parameter, not geometric
- "What determines σ?" was the central unsolved question

The shear mechanism changes this fundamentally.  The photon is
now treated as a proper **wave** on the flat T².  Charge comes
from the **geometry of the space** (non-orthogonal lattice
vectors), not from the wave's state (localization):

- A fully delocalized wave → charge ≠ 0 (q_eff non-integer)
- No localization parameter σ needed
- The free parameter is shear s, which is *geometric* (metric)
- Different winding numbers on the same lattice produce
  different charges (see "Generalized q_eff" below)

### Generalized q_eff: different windings → different charges

On the sheared T², a general (n,m) mode has:

    q_eff(n,m) = m − n·s

The charge factor for each mode is:

    Q ∝ sin(2π n s) / (m − n s)

This means different winding configurations on the **same**
sheared lattice produce different charge values:

| Mode    | q_eff    | Charge factor            |
|---------|----------|--------------------------|
| (1,2)   | 2 − s    | sin(2πs) / (2−s)         |
| (1,1)   | 1 − s    | sin(2πs) / (1−s)         |
| (1,3)   | 3 − s    | sin(2πs) / (3−s)         |
| (2,1)   | 1 − 2s   | sin(4πs) / (1−2s)        |
| (n,m)   | m − ns   | sin(2πns) / (m−ns)       |

This is critical for the T³ extension: the electron, up quark,
and down quark may be **different winding configurations** on a
**single fixed geometry**, with their charges (e, 2e/3, e/3)
emerging from different (n,m) values, not from different shear
parameters.

### From T² to T³: two roles, now separated

R14 originally proposed T³ for two purposes:

1. **Charge fractionalization** — linking of photon geodesics
   on T³ would fractionalize each photon's charge projection,
   producing quark charges 2e/3 and e/3.

2. **Confinement** — topological linking (Borromean) prevents
   individual quarks from separating.

With the shear mechanism, these two roles separate:

- **Charge** now comes from the shear + winding numbers.
  Different particles are different (n,m) modes on the same
  sheared T³.  No linking is needed for charge.

- **Confinement** still requires linking topology.  Geodesics
  in different planes of T³ can be topologically linked,
  preventing separation.  This role is unchanged from R14.

The shear mechanism makes fractional charges a *kinematic*
consequence of the lattice geometry, not a *topological*
consequence of linking.  This is simpler and more testable.

---

## Tracks

### Track 1. Backwards: derive required shear from known α  *(complete)*

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

### Track 2. Energy analysis: is non-zero shear stable?  *(complete — viable but free)*

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

### Track 3. Self-consistent geometry + normalization  *(self-consistency complete; normalization pending)*

Self-consistent Compton constraint with shear:
L(s) = 2π√(a²(1+2s)² + 4R²) = λ_C adjusts (a, R) for
nonzero shear, feeding back into the charge formula.

Complete: the self-consistent α formula
    α = r²sin²(2πs) / (4π(2−s)²√(r²(1+2s)²+4))
is solved for all r.  Result: s shifts up ~5% from Track 1 values.
All properties verified: L/λ_C = 1, Q/e = 1 exactly.
The electron is a one-parameter family in r (F15).

Remaining: normalization reconciliation (E₀ conventions) to
confirm which coupling applies.  Previous calculations show
full E₀ gives clean results while κ-suppression kills the
mechanism (F5).

### Track 4. T³ quark charges: most constrained hypothesis  *(complete — ruled out, near-misses)*

**Hypothesis:** A single T³ metric (three circumferences L₁, L₂,
L₃ and a uniform shear s₁₂ = s₂₃ = s₁₃ = s) supports all three
particles as different winding configurations:

- **Electron:** (1, 2, 0) winding in the (1,2) plane → Q = e
- **Up quark:** some (n, 0, m) in the (1,3) plane → Q = 2e/3
- **Down quark:** some (0, n, m) in the (2,3) plane → Q = e/3

Steps:
1. Generalize the self-consistent charge formula to T³ with
   three circumferences and uniform shear.
2. For each candidate winding (n,m), compute the charge as a
   function of the plane's aspect ratio and shear.
3. Solve simultaneously: electron charge = e, up = 2e/3,
   down = e/3.  Can these be satisfied by one (L₁, L₂, L₃, s)?
4. If yes: check masses.  The geodesic lengths determine
   photon energies → quark masses → proton mass.  Does
   m_p ≈ 3 × 612 × m_e (R14 F3)?
5. If yes: count free parameters vs. constraints.
   Is the geometry fully determined?

**Success criterion:** One T³ geometry produces all three
charges from different windings, with mass ratios consistent
with observations.

### Track 5. Relaxed hypothesis: non-uniform shear  *(contingency)*

If Track 4 fails (uniform shear cannot produce the right charge
ratios), relax to three independent shear values s₁₂ ≠ s₂₃ ≠ s₁₃.
Each plane then has its own effective charge formula.  More free
parameters but still constrained by multi-particle consistency.

### Track 6. Linking + shear hybrid  *(contingency)*

If neither Track 4 nor 5 produces fractional charges from
kinematics alone, revisit R14's topological linking mechanism
in combination with shear.  In this picture:
- Shear provides the *base* charge (integer-like)
- Linking fractionalizes it (topology modifies the projection)
- The combination determines the quark charges

This would retain R14's linking for both confinement AND
charge fractionalization, with shear providing the overall
charge scale (α).

---

## Key facts

### One shear parameter on T², three on T³

A flat T² metric has three independent components: g₁₁, g₂₂
(the two circumferences) and g₁₂ (the shear).  Only ONE
independent shear parameter exists.  "Shearing θ along φ" and
"shearing φ along θ" are different descriptions of the same
geometric tilt.

On T³, by contrast, there are THREE independent shear
parameters (g₁₂, g₁₃, g₂₃) — one per pair of axes.

### T³ does not embed in ℝ³

T² embeds in ℝ³ (the familiar donut).  T³ cannot — it
requires at minimum ℝ⁴.  But in the Kaluza-Klein framework,
the compact space is ADDITIONAL to 3D, not sitting inside it.
At every point in physical 3D space, a copy of T² (or T³)
is attached as a fiber.  Going from T² to T³ means going
from a (3+2)D spacetime to a (3+3)D spacetime.  No embedding
obstruction arises.

### T³ geometry: parameters and constraints

The flat T³ metric has 6 independent parameters:
- 3 circumferences: L₁, L₂, L₃
- 3 shears: s₁₂, s₁₃, s₂₃

After fixing the overall scale (one circumference sets the
electron mass), there are 5 free parameters (2 independent
aspect ratios + 3 shears).

Constraints available:
- 3 charge equations (Q_e = e, Q_u = 2e/3, Q_d = e/3)
- Mass constraints from geodesic lengths
- Possibly: topological constraints from linking (confinement)

The most constrained sub-case (Track 4) sets all shears equal
(s₁₂ = s₂₃ = s₁₃ = s), leaving 3 parameters (2 aspect ratios
+ 1 shear) vs 3 charge equations.  This is exactly determined.

### Different charges from different windings (not different shears)

Historically (S3, R14), different particle charges were
attributed to different winding numbers (knots) on the compact
space.  S3 found that on an *unsheared* T², only (1,2) gives
nonzero charge — other knots are blocked by φ-symmetry.

With shear, this restriction is lifted.  ALL modes on a sheared
lattice have nonzero charge, with the charge depending on
the winding numbers through q_eff(n,m) = m − ns.  This
rehabilitates R14's original vision of different windings
producing different particles, now with a concrete formula
for each charge.

---

## Key equations

**Convention:** Define s ≡ δ/(2πa) as the fractional shear
(dimensionless, 0 ≤ s < 1), where δ is the linear shear
displacement.  This matches R12's `shear_frac = δ/L_θ`.

**Sheared T² lattice:**

    e₁ = (L₁, 0)    where L₁ = 2πa
    e₂ = (δ, L₂)    where L₂ = 2πR
    s  = δ/L₁

Identification: (x,y) ~ (x + L₁, y) ~ (x + δ, y + L₂)

**Mode on sheared T²:**

The (1,2) mode (n=1 winding in θ, m=2 in φ) has wavevector:

    k_θ = 1/a,  k_φ = (2 − s)/R

In embedding coordinates (Θ = x/a, Φ = y/R):

    ψ(Θ,Φ) = exp[i(Θ + q_eff Φ)]
    q_eff = 2 − s = 2 − δ/(2πa)

**Generalized (n,m) mode on sheared T²:**

For a general (n,m) mode, periodicity under both lattice
identifications gives:

    k_x = 2πn/L₁,   k_y = 2π(m − ns)/L₂

    q_eff(n,m) = m − n·s

The charge factor is:

    Q ∝ sin(2π n s) / (m − n s)

Note: sin(2π(m − ns)) = sin(−2πns) × cos(2πm) = −sin(2πns)
for integer m, so the numerator depends on n·s, not on m.

**Charge integral (electron, n=1, m=2):**

    Q = ε₀ E₀ a²π × sin(2πs) / (2 − s)

**Self-consistent α formula (from Track 3):**

    α = r² sin²(2πs) / (4π (2−s)² √(r²(1+2s)²+4))

**Generalized charge ratio (any (n,m) vs electron (1,2)):**

    Q(n,m) / Q(1,2) = [sin(2πns) / (m−ns)] / [sin(2πs) / (2−s)]
                     × [normalization ratio from energies/geometry]

The normalization ratio accounts for different photon energies
(different geodesic lengths) and different torus volumes in
different planes of T³.

---

## Status

**Created:** 2026-03-01
**Status:** Phase 1 (T² electron) essentially complete (F16).
Tracks 1–3 (self-consistency part) complete.  Track 1 positive (δ ≈ a for r=1).
Track 2: shear is energetically favorable but free (no specific value selected on flat T²).
Track 3: self-consistent geometry confirmed (~5% correction to s); normalization part pending.
Track 4 (complete): uniform shear + different windings on T³ ruled out.
Key findings: n=1 required; same-plane impossible; mass forces m≈−6;
s≈1/6 near-miss (1%); T³ consistency fails (r₁₂=2 vs 1). Near-misses
suggest correct picture is close. Tracks 5–6 are next options.
