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

### Track 5. Relaxed hypothesis: non-uniform shear  *(complete — ruled out)*

Relaxed to three independent shear values s₁₂ ≠ s₂₃ ≠ s₁₃.
The charge equations are solvable (factor-of-2 disappears), but
the mass constraint kills the model: quark energies come out as
1–12 m_e instead of 612 m_e.  The charge and mass constraints
are fundamentally incompatible for (1,−6) single-photon quarks.

Combined with Track 4: no shear configuration (uniform or not)
can make (1,−6) quarks work.  The single-photon quark hypothesis
is ruled out (F24).  Quark charges likely require a different
mechanism (linking fractionalization, Track 6).

### Track 6. 3D geodesic charge on sheared T³  *(complete)*

Tracks 4–5 showed that the 2D charge formula (derived for
modes confined to a plane of T³) cannot produce quarks: the
mass and charge constraints are incompatible.  But this formula
was always a 2D result extended to T³ by assumption.

Track 6 asks the more fundamental question: **what does the
charge formula look like for a 3D geodesic on a sheared T³?**

On T³, a photon can wind in all three compact dimensions:
winding numbers (n₁, n₂, n₃) with all nᵢ ≠ 0.  Such a path
is a genuine 3D curve, not confined to any 2D subplane.

Key differences from the 2D case:
- The charge integral is over all three compact coordinates
- The n=1 selection rule (F17) was derived from a 2D angular
  integral; it may not hold in 3D
- Three shear parameters (s₁₂, s₁₃, s₂₃) ALL affect the mode,
  not just the one in "its" plane
- The geodesic length includes contributions from all three
  circumferences, providing additional mass

Physical picture:
- Electron = (1, 2, 0): confined to a plane (n₃ = 0), lowest
  energy spin-½ state.  The 2D formula applies.
- Quark = (1, 2, k) or other 3D winding: wraps all three
  dimensions.  Heavier (longer geodesic), potentially different
  charge (3D integral differs from 2D).

Steps:
0. Map the T³ mode energy landscape (F25–F28) — **complete**.
   (1,2,k≠0) modes are lighter than the electron.  Planarity
   requires a charge selection rule, not energetics.
1. Derive the 3D charge integral (F29–F34) — **complete**.
   Q ∝ sin(πs₁₂)sin(πs₁₃)/((n₂−s₁₂)(n₃−s₁₃)).
   n₁=1 rule persists (F30).  s₂₃ irrelevant for charge (F29).
   At s₁₃=0: only n₃=0 carries charge (F31) — electron is
   automatically planar.  But s₁₃≠0 creates sub-electron
   charged particles (F32), ruling out shear-based quark
   charges (F33–F34).

**Conclusion:** The 3D charge integral does NOT provide a
path to quark charges from shear alone.  Instead, it delivers
a clean selection rule (F31) that protects the electron and
pushes quark charges to the linking mechanism (Track 7/R14).

### Track 7. Linking + shear hybrid  *(contingency)*

If 3D geodesics (Track 6) don't produce fractional charges,
the remaining option is R14's topological linking mechanism
combined with shear.  In this picture:
- Shear sets the overall charge scale (α) via the electron
- Linking fractionalizes it for multi-photon quark states
- Confinement is topological (Borromean linking)

This is the most conservative hypothesis: it preserves the
electron result from Tracks 1–3 and defers quark charges to
R14's topological mechanism.  See Q64, Q66.

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

**Electron (Tracks 1–3): essentially complete.**
The electron's charge comes from shear on T² (F1–F16).
Self-consistent geometry gives a one-parameter family in r.
The free parameter r requires external constraint (→ R14).

**Quark program (Tracks 4–6): complete, negative.**
All single-photon shear approaches to quark charges are ruled out.
Track 4: uniform shear fails (T³ consistency, F21).
Track 5: non-uniform shear fails (mass, F23–F24).
Track 6: 3D charge integral fails (sub-electron particles, F31–F34).
Key positive result: F31 predicts no charged particle lighter than
the electron, explaining why the electron is confined to a 2D plane
on T³ despite lighter modes existing.

**Next:** quark charges from topological linking → R14 Track 1.

New inbox entries: Q60–Q66 document unexplored directions.
