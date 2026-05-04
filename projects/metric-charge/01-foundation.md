# Chapter 1 — Foundation

**Status:** Sparse outline. To be expanded into full prose.

---

## Purpose

Establish the *manifold*, *metric*, *field*, *periodicity*, and *closure rule* on which the rest of the project rests. This is the only chapter where we **assume** things; every later chapter derives its claims from what is stated here.

## Prerequisites

- [primers/metric.md](../../primers/metric.md) — metric machinery (covered in metric-mass)
- [metric-mass/01-foundation.md](../metric-mass/01-foundation.md) — predecessor chapter; we pick up from where it ends

Wherever metric-mass already established something, we cite it rather than re-derive.

## Tone

Slow, deliberate, table-driven — match metric-mass's pacing. Every concept introduced here gets reused as-is for the rest of the project.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | Coordinates: (t, S₁, S₂, u, w) and their domains |
| 2 | The bare metric on the 2D sheet |
| 3 | Aspect ratio ε ≡ L_u / L_w |
| 4 | Off-diagonal shear σ_uw (deferred to ch. 7) |
| 5 | Visualization disposition (45° rendering) |
| 6 | The wave field φ |
| 7 | Why a scalar field is enough — and what we choose not to track |
| 8 | The wave equation on the manifold |
| 9 | Periodicity in (u, w) |
| 10 | The closure condition (axiomatic) |
| 11 | Explicit non-assumptions |
| 12 | Summary of givens |

---

## §1. Coordinates

Five coordinates: t, S₁, S₂, u, w. Domain table (extended ℝ for t, S₁, S₂; periodic S¹ for u and w).

**Why two extended (vs. one in metric-mass):** single-knot derivations in this project largely don't need S₂ — most results work in S₁ alone. S₂ is carried for continuity with [metric-binding](../metric-binding/), where it becomes essential (two knots at different (S₁, S₂) positions).

**Why two compact (vs. one in metric-mass):**
1. Knots — a 1D compact direction has no knot family; 2D does
2. Closure condition — needs winding in *both* u and w
3. Polarization — see §7

Manifold notation: M = ℝ × ℝ × ℝ × S¹ × S¹.

## §2. The bare metric

Simplest Lorentzian metric on M:

ds² = −c² dt² + dS₁² + dS₂² + du² + dw²

Diagonal, all coefficients 1, periodicity carries the geometric content.

## §3. Aspect ratio ε ≡ L_u / L_w

Free parameter. Lives in the periodicities (L_u and L_w), not in the metric components in the bare form. ε = 1 is the symmetric Clifford torus; ε ≪ 1 is "thin," ε ≫ 1 is "fat." Will be swept in chapter 6.

## §4. Off-diagonal shear σ_uw

Optional non-zero g_uw entry. With shear:

ds² = −c² dt² + dS₁² + dS₂² + du² + 2 σ_uw du dw + dw²

Geometric meaning: u and w are no longer orthogonal in the metric sense. σ tilts them. Returns in chapter 7 as the symmetry-breaking parameter (matter/antimatter bias, three-phase population).

## §5. Visualization disposition

Lift from [README.md](README.md). Compact directions exaggerated, sheet sits at ~45° in 3D rendering with u's normal toward (+y, +z) and w's normal toward (−y, +z). The (x, y, z) display axes are not metric coordinates — just where on the screen each coordinate is drawn.

## §6. The wave field

We work with a scalar field φ(t, S₁, S₂, u, w). Same kind of object as metric-mass's φ(t, S, u), now on the larger manifold.

## §7. Why a scalar field is enough — and what we choose not to track

> **This section is the seam between metric-mass and metric-charge on the polarization question. It's deliberately structural and short. The full vector-field story is parallel to our work, not part of it, and lives downstream in [grid/](../../grid/).**

### §7.1 Scalar suffices for our derivations

Everything chapters 2–9 will derive — winding numbers (m, n), knot topology, the closure condition, fractional charge from multi-phase wraps, mass-only modes from closure failure — operates on the **phase pattern** of φ. It does not require a polarization vector.

A scalar field is the right level of abstraction for this project's derivation chain.

### §7.2 What metric-mass quietly elided

A real photon is a vector potential A_μ with E and B fields perpendicular to k. metric-mass's scalar abstraction collapsed this away — it didn't need polarization for the mass-from-u derivation, so it didn't include it.

If we naively promote metric-mass's setup to a real photon: a photon traveling along u has its polarization perpendicular to u. With only u as a compact direction, "perpendicular to u" means S or t — observable spacetime. That would put an oscillating E into S at every massive object's Compton frequency. We don't observe this. So the naive promotion fails.

The scalar abstraction in metric-mass is therefore not just a simplification — it's a way of avoiding a structural deficiency: **one compact dimension is too few to host the photon's polarization internally.**

### §7.3 What the 2D sheet buys

With both u and w compact, a photon traveling along u has w as a perpendicular direction *within the sheet*. E along w is internal to the compact structure. This is the minimum compact geometry on which one of the photon's polarization components has an internal home — independent of the (already sufficient) topological reasons for jumping to 2D.

### §7.4 What still leaks

B = k × E. With k along u and E along w, B is perpendicular to both — out of the sheet plane. So even on a 2D sheet, *one* of {E, B} wants to live outside the sheet. This is plausibly the structural opening through which bound photons couple to S, and the candidate quantity that α measures (Q137, grid/alpha-derivation).

### §7.5 What this chapter commits to

We use a scalar φ throughout. Wherever later chapters say "the wave winds 2π on w," "the wave forms a knot," or "the closure condition is satisfied," we mean *the phase pattern of φ*. The polarization-leakage question is parallel to this work, deferred to grid/, and flagged as an open structural question rather than a derivation step.

If a later chapter forces the issue (a closure-condition prediction that depends on polarization structure), we will revisit. So far we don't expect that.

## §8. The wave equation on M

□φ = 0 on the 5D manifold. Explicit form of the d'Alembertian with the bare metric of §2. Routine extension of metric-mass's wave equation; main novelty is the Laplacian on the (u, w) torus.

## §9. Periodicity in (u, w)

φ(t, S₁, S₂, u + L_u, w) = φ(t, S₁, S₂, u, w)
φ(t, S₁, S₂, u, w + L_w) = φ(t, S₁, S₂, u, w)

This is what makes (u, w) a 2-torus. With σ ≠ 0 (chapter 7), the periodicity lattice is sheared — note the consistency requirement and defer the full treatment.

## §10. The closure condition (axiomatic)

The centerpiece of the project. State cleanly:

> **Closure condition.** A wave configuration on the 2D sheet promotes its mass mode to a charge mode when, during a single closed traversal of the phase pattern, **both** of the following are satisfied:
> 1. The phase completes a full 2π winding on w.
> 2. The phase completes a complete standing wave (full period — node-to-antinode-to-node) on both u and w.
>
> Mini-step traversals are allowed; what matters is that the closure pattern locks during one full traversal of the knot.

This is **stated, not derived**. The "why" — the α-coupling-strength derivation that explains the *strength* of the resulting charge — lives in [grid/](../../grid/), to be developed there.

Variants to keep open for chapter 4:
- 2π winding on u (instead of w) — different particle class?
- Standing wave on only one direction
- Multiple knots collectively satisfying closure but no single one individually

## §11. Explicit non-assumptions

What this chapter does *not* commit to:

- No claim that electron, proton, or neutrino sheets exist as separate species (this project has one sheet)
- No commitment to a numerical value of α (taken as given when needed; derived elsewhere)
- No claim that the closure condition of §10 is unique (alternatives examined in chapter 4)
- No tracking of full vector polarization for the EM field — see §7
- No claim that the scalar abstraction loses *no* information beyond polarization (we leave room for surprises)
- No quantum field theory; classical field analysis only
- No backreaction of the field on the metric (linearized regime; deferred)

## §12. Summary of givens

Recap table of:
- Coordinates and domains
- Bare metric
- Parameters: ε, σ_uw
- Field: scalar φ
- Periodicities
- The closure condition
- Visualization convention

This is the working set chapter 2 begins from.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---------------|
| Does the polarization leakage out of the sheet quantify α? | grid/alpha-derivation |
| Is the scalar abstraction lossy beyond polarization? | watch for surprises in chapters 2–9 |
| Is the closure condition unique, or one of several? | chapter 4 |
| Does periodicity remain consistent under shear? | chapter 7 |
