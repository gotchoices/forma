# Chapter 3 — Shear and *c*

**Status:** outline — sections are framed but not yet infilled. Awaiting review before the algebra is written out.

This chapter takes the wave dynamics derived in [02-wave-on-a-primitive.md](02-wave-on-a-primitive.md) — two propagating modes with speeds *c*_± = √λ_± — and confronts them with the lattice signal speed *c* required by GRID axiom A1. The question is whether the constraint that perturbations cross one cylinder in transit time τ = *L*/*c* fixes the primitive's parameters uniquely or leaves a one-parameter family of solutions.

This chapter settles open question 1 of [README.md](README.md).

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The constraint: cylinder transit time matches lattice cadence |
| 2 | Two modes, two speeds — which one is *c*? |
| 3 | Three candidate identifications and what each implies |
| 4 | Imposing the constraint algebraically |
| 5 | Combining with equipartition (χ̃ = 1/√2) |
| 6 | What pins, what stays free |
| 7 | The two-modes vs vacuum-Maxwell tension — flagged for resolution |
| 8 | Summary of givens |

---

## 1. The constraint — cylinder transit time matches lattice cadence

Goal: state the constraint cleanly. The lattice signal speed *c* is set by axiom A1 (one cell per tick, one lattice spacing per time step). For the cylinder primitive of length *L*, the transit time τ = *L*/*c* is what the lattice cadence requires for information to traverse the cylinder. This must equal the time the cylinder's *internal* dynamics actually take to transmit a perturbation.

*To infill:* the precise statement of the constraint, distinguishing definitional τ = *L*/*c* (always true by definition) from the substantive equality between the cylinder's internal wave speed and *c* (which is a real algebraic constraint).

---

## 2. Two modes, two speeds — which one is *c*?

Goal: surface the choice that has to be made. Chapter 2 derived two natural mode speeds *c*_+ and *c*_− with *c*_+ > *c*_− whenever χ̃ > 0 (chirality splits them). The lattice signal speed *c* is a single number. So at most one of *c*_± can equal *c* directly; alternatively, *c* could be some effective combination.

*To infill:* the framing of the question — three candidate readings of "the cylinder propagates at *c*":

- Identify *c* with *c*_+ (the fast mode is light).
- Identify *c* with *c*_− (the slow mode is light).
- Identify *c* with an effective average (both modes contribute).

Each has consequences. The chapter examines each in turn.

---

## 3. Three candidate identifications

Goal: lay out the three candidates side by side.

*To infill, for each:*

- **Candidate A: *c*_+ = *c*.** The fast mode is identified as light; the slow mode is something else (a "matter-like" excitation that does not propagate at *c* and may not show up as light at the lattice scale). Implications: there is a second mode at every cylinder, but its physics is distinct from photon physics.

- **Candidate B: *c*_− = *c*.** The slow mode is light; the fast mode is some superluminal excitation. This is unphysical for vacuum Maxwell and is rejected on physical grounds, but it is worth showing why.

- **Candidate C: *c*_+ = *c*_− = *c*.** Both modes propagate at the same speed. This requires the matrix *M* to have degenerate eigenvalues; given χ̃ > 0, the only way to get degeneracy in our 2 × 2 *M* is at the stability boundary (χ̃ = 1), where one mode collapses. So Candidate C is incompatible with the stable-range commitment of theory 3.

*To infill:* the elimination of B and C, leaving A as the working choice (with a flag in §7 about whether the residual second mode causes trouble for vacuum Maxwell).

---

## 4. Imposing the constraint algebraically

Goal: with Candidate A fixed (*c*_+ = *c*), write the constraint equation and solve symbolically.

*To infill:* using the closed form λ_+ from chapter 2 §4 with the simplifying assumption ρ = *I_φ* and *K_ee* = *K_φφ* ≡ *K* (kept consistent with chapter 2's treatment), the constraint reduces to:

*c*² = (*K*/ρ)(1 + χ̃)

(or equivalently in terms of *L*, *r*, the underlying material constants — to be worked out).

This is one equation in five symbolic constants (*K_ee*, *K_φφ*, *K_eφ*, ρ, *I_φ*) — or, after the simplifying reduction, in three (*K*, ρ, χ̃). One constraint among multiple parameters does not pin everything; it pins one combination.

---

## 5. Combining with equipartition (χ̃ = 1/√2)

Goal: combine the *c* constraint from §4 with the equipartition value from chapter 2 §7.

*To infill:* substituting χ̃ = 1/√2 into the *c* constraint gives:

*K*/ρ = *c*² / (1 + 1/√2)

This pins the ratio *K*/ρ in terms of *c*. Combined with χ̃ = 1/√2 (which pins *K_eφ*/*K* = 1/√2), all stiffness-and-inertia *ratios* in the simplifying special case are now fixed by *c* and the equipartition principle.

What is *not* pinned: the absolute scale of *K* (and correspondingly ρ), the cylinder length *L*, and the cross-section radius *r*. These remain free.

---

## 6. What pins, what stays free

Goal: enumerate the parameters and their status after applying *c* + equipartition.

*To infill:* a table summarizing:

| Parameter | Status |
|---|---|
| *K_eφ* / *K* | Pinned to 1/√2 (equipartition) |
| *K*/ρ | Pinned by *c*² / (1 + 1/√2) |
| Absolute scale of *K* (and ρ) | Free |
| Cylinder length *L* | Free |
| Cylinder cross-section radius *r* | Free |
| Slow-mode speed *c*_− | Determined: *c*_− = √(*K*/ρ)(1 − 1/√2) ≈ 0.42 × *c*_+ — concrete value flagged for §7 |

Three free parameters survive: an overall stiffness scale, *L*, and *r*. The next chapters will examine whether the entropy account (chapter 4), Maxwell recovery (chapter 6), or α (chapter 8) further constrains these.

---

## 7. The two-modes vs vacuum-Maxwell tension

Goal: confront the lingering issue that Candidate A leaves unresolved. With *c*_+ = *c* and *c*_− ≠ *c*, the cylinder has a second mode that propagates at a *different* speed — slower than the lattice cadence *c*. Vacuum Maxwell, by contrast, has *both* photon polarizations at exactly *c*.

*To infill:* this is a genuine tension and the chapter should not paper over it. Possible resolutions to be examined briefly (with full treatment deferred):

- The slow mode is real but is identified as a *non-photon* excitation — possibly a massive mode, a dispersive mode that does not appear as long-wavelength light, or an excitation that decouples in the continuum limit.
- The slow mode is suppressed by some property of the lattice assembly (chapter 5) that does not exist on a single primitive — collective effects in a 2D lattice may average the two speeds or suppress one of them.
- The slow mode is a real prediction — testable as a tiny deviation from the vacuum Maxwell two-equal-speed prediction. (This is unlikely to match observation but is logically possible.)

The chapter flags the issue and notes that resolution is deferred to chapter 5 (lattice assembly) or chapter 6 (Maxwell base). It is not a foundation-level failure of the primitive; it is a downstream question.

---

## 8. Summary of givens

Goal: consolidate what chapter 3 establishes.

*To infill:* a brief recap. The constraint *c*_+ = *c* together with equipartition χ̃ = 1/√2 pins all dimensionless stiffness ratios in the simplifying special case, leaving an overall stiffness scale, *L*, and *r* as free parameters. The slow mode *c*_− has a determined value strictly less than *c*; whether this conflicts with vacuum Maxwell or is benign at the lattice scale is flagged for downstream chapters. Chapter 4 takes up whether the topological-defect entropy story is enough to source Jacobson's gravity.
