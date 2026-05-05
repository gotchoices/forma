# Chapter 5 — 2D Lattice Assembly and the Slow-Mode Question

**Status:** outline — sections are framed but not yet infilled. Awaiting review before the algebra is written out.

Chapters 1–3 established the cylinder primitive on a single edge: its energy, its wave dynamics, and the constraints that the lattice signal speed *c* + the natural shear χ̃ = 1/√2 place on its parameters. Chapter 4 already used a 2D lattice's static and thermal behavior to confirm the entropic 1/r force scaling, but it did so without formally deriving the 2D lattice from the single-primitive equations. This chapter does that derivation, and then takes up a substantive question that chapter 3 left unresolved: **the slow-mode tension**.

Chapter 3 found that imposing *c*_+ = *c* (Candidate A) leaves the slow mode at *c*_− ≈ 0.414 *c*. Vacuum Maxwell has two photon polarizations both at *c*; the cylinder primitive has two modes at *c* and ≈0.414 *c*. This chapter is where we figure out what happens to the slow mode when many cylinders are assembled into a 2D periodic lattice.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The 2D lattice geometry: nodes, cylinders, neighbors |
| 2 | Periodic boundary conditions and the lattice as a torus |
| 3 | From single-primitive equations to 2D lattice equations |
| 4 | The Brillouin zone — the natural setting for lattice modes |
| 5 | Two bands: fast and slow |
| 6 | The slow-mode fate: gap, persistence, or averaging |
| 7 | What chapter 6 needs from this chapter |
| 8 | Risks and unresolved issues |
| 9 | Summary of givens |

---

## 1. The 2D lattice geometry

Goal: pick a specific 2D lattice geometry and describe the connectivity. Options to consider: square (4 neighbors per node), triangular (6 neighbors per node), hexagonal (3 neighbors per node). Each gives a different lattice mode structure; the choice affects chapter 7's coefficient match.

*To infill:* a definite choice with motivation, including a brief comparison to GRID's lattice geometry in [grid/lattice-geometry.md](../../grid/lattice-geometry.md). Diagram showing the chosen lattice with cylinders along edges and nodes at vertices.

---

## 2. Periodic boundary conditions and the lattice as a torus

Goal: state the periodic-BC prescription. The lattice is a *torus*: the rightmost column of nodes is identified with the leftmost; the topmost row with the bottommost. This eliminates boundary effects and gives a clean translation symmetry.

*To infill:* the formal statement of periodicity, with a brief note on why open boundaries are unsuitable (carry asymmetries that the physical lattice does not have — ground rule 7).

---

## 3. From single-primitive equations to 2D lattice equations

Goal: derive the wave equation that governs the lattice as a whole, by combining the single-cylinder equations of chapter 2 with the node-continuity boundary conditions of chapter 1 §5.

*To infill:* the assembly of many single-cylinder PDEs into a single lattice PDE; the long-wavelength continuum limit recovering the matrix wave equation *D* ∂_t² **u** = *M* (∂_x² + ∂_y²) **u** introduced in chapter 4 §4. Show the algebra connecting single-cylinder dynamics to the 2D continuum equation, including how *M* on each bond combines into the same *M* in the lattice equation.

---

## 4. The Brillouin zone — the natural setting for lattice modes

Goal: introduce Brillouin-zone (k-space) analysis as the standard tool for lattice physics. For each wavevector **k** in the Brillouin zone, the lattice supports plane-wave modes of the form **u** = **A** exp(i(**k** · **r** − ω*t*)).

*To infill:* the Brillouin-zone structure for the chosen lattice; the dispersion relation ω²(**k**) replacing ω²(*k*) of chapter 2; brief reminder of what an engineer needs to know about k-space (it is just the spatial Fourier domain — a way of analyzing lattices one wavelength at a time, like mode analysis for a vibrating drumhead).

---

## 5. Two bands: fast and slow

Goal: derive the two-band structure of the 2D lattice, generalizing chapter 2's two-mode result. Each branch ω²_±(**k**) = |**k**|² · λ_± gives a *band* — a 2D surface over the Brillouin zone.

*To infill:* explicit expressions for ω_+(**k**) and ω_−(**k**) in the long-wavelength limit (the cylinder's chapter-2 result, with k replaced by |**k**|); discussion of band edges and band shape; identification of the fast band (slope *c* = *c*_+) and the slow band (slope ≈ 0.414 *c*).

---

## 6. The slow-mode fate: gap, persistence, or averaging

Goal: this is the chapter's central question. Three candidate outcomes for the slow band, each with different implications for chapter 6:

- **(a) Gap.** Lattice-scale physics gives the slow mode a mass: ω_−(**k** = 0) ≠ 0. At low frequencies the mode is non-propagating; vacuum Maxwell sees only the fast mode (two photon polarizations at *c*).
- **(b) Persistence.** The slow mode remains a propagating wave at low frequencies. Then it is some non-photon physical excitation — possibly a longitudinal/non-radiative degree of freedom, or a separately observable mode.
- **(c) Averaging.** Lattice geometry averages the two single-primitive speeds into a single effective lattice mode at *c*. Both polarizations recover Maxwell.

*To infill:* the actual calculation of the slow-mode dispersion at the band edge — does ω_−(**k** = 0) come out to zero (mode is gapless, scenario b or c), or to a finite frequency (gapped, scenario a)? Possible mechanisms for gap formation: interaction terms from node geometry that don't appear in single-cylinder dynamics, periodic-lattice umklapp effects, etc. If the result is scenario (b), describe the physical interpretation of the slow mode at lattice scale.

---

## 7. What chapter 6 needs from this chapter

Goal: spell out the handoff to the Maxwell bridge.

*To infill:* a clean statement of (i) the 2D lattice equation that survives in the long-wavelength limit, (ii) which mode (or both) plays the role of "the photon," (iii) the polarization structure of the photon-like mode(s), and (iv) any extra physical content (slow mode fate, lattice-geometry-specific terms).

---

## 8. Risks and unresolved issues

The chapter's load-bearing risk is **Risk A — the slow mode**. Concrete fail-fast outcomes:

- *Scenario (a) — slow mode gaps out.* Photon recovers cleanly; chapter 6 proceeds with a clean Maxwell match. Best outcome.
- *Scenario (b) — slow mode persists.* The cylinder primitive carries an additional physical excitation beyond the photon. Chapter 6 has to decide what physical role this excitation plays (matter-like, non-radiative, dark) and whether it has observable consequences.
- *Scenario (c) — averaged.* Both polarizations end up at *c*; chapter 6 proceeds, but the chapter-3 "two-mode" picture is replaced by a single effective lattice mode.

Any of (a), (b), (c) is a valid outcome; none constitutes a project failure. (b) is the least clean but most informative — the cylinder primitive would be predicting an additional physical degree of freedom that has to be reconciled with experiment.

A secondary risk: the choice of 2D lattice geometry (§1) affects band structure in detail. If different geometries give qualitatively different slow-mode fates, the chapter must justify its choice or examine multiple geometries.

---

## 9. Summary of givens

What this chapter delivers:

- The 2D lattice equation governing collective modes.
- The two-band dispersion ω_±(**k**) as functions of Brillouin-zone wavevector.
- The fate of the slow band — gapped, persistent, or averaged — and the implications for the Maxwell bridge.
- The cleanest single-mode (or single-pair-of-modes) framework that chapter 6 can use to coarse-grain to (θ, A_μ).

The next chapter takes this lattice framework and shows how coarse-graining recovers the inputs to [grid/maxwell.md](../../grid/maxwell.md).

---

## Decisions to confirm before infill

1. **Lattice geometry.** Square (simplest), triangular (matches GRID's hexagonal-related geometry better), or hexagonal (matches the dialog's nanotube intuition)? The choice affects §1, §4, §5, §6 and downstream chapters. Default: square for simplicity unless GRID's preferred geometry argues otherwise.
2. **Slow-mode treatment depth.** Full Brillouin-zone calculation with explicit ω(**k**) functional forms, or order-of-magnitude estimates with leading-order behavior? Default: enough Brillouin-zone analysis to settle gap-vs-gapless cleanly, deferring detailed band-shape questions.
3. **Long-wavelength regime.** The chapter's analysis lives in the regime where lattice spacing ≪ wavelength of interest. Edge cases (very-short-wavelength lattice modes, regimes where lattice discreteness matters) are noted but not pursued.
