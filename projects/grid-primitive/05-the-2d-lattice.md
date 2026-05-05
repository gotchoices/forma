# Chapter 5 — 2D Lattice Assembly and the Slow-Mode Question

Chapters 1–3 established the cylinder primitive on a single edge. Chapter 4 established that a 2D lattice of these primitives produces logarithmic Green's functions and 1/r force scaling, but it did so without formally deriving the lattice from the single-primitive equations. This chapter does that derivation, and then takes up a substantive question that chapter 3 left unresolved: **the slow-mode tension**.

The cylinder primitive supports two propagating modes at speeds *c*_+ = *c* (the lattice signal speed) and *c*_− ≈ 0.414 *c* (a slower mode). Vacuum Maxwell has only one photon speed. This chapter examines what happens to the slow mode when many cylinders are assembled into a 2D *hexagonal* lattice — the geometry that [grid/hexagonal.md](../../grid/hexagonal.md) identifies as preferred for waves and that gives ζ_2D = 1/3 from a wye-junction count.

The chapter does not invoke "mass" as the slow-mode interpretation. The mass-from-compact-dimensions story belongs to [metric-mass](../metric-mass/), not to this project. Three non-mass candidate resolutions are in scope: (i) emergent Lorentz symmetry, (ii) longitudinal/non-radiative coarse-graining, and (iii) Planck-scale band gap. The chapter examines (iii) directly; (i) and (ii) are downstream questions.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The hexagonal lattice geometry — wye junctions, hexagonal faces |
| 2 | The wave equation on the 2D lattice |
| 3 | The long-wavelength continuum limit — recovering chapter 2's two modes |
| 4 | The Brillouin zone and band structure of the lattice |
| 5 | Are there acoustic vs. optical bands? |
| 6 | The slow-mode fate at long wavelengths |
| 7 | Scale separation: where the 18-orders-of-magnitude argument helps |
| 8 | Where the resolution must come from |
| 9 | Risks and unresolved issues |
| 10 | Summary of givens |

---

## 1. The hexagonal lattice — wye junctions and hexagonal faces

The 2D periodic lattice we work with is the **hexagonal (honeycomb) lattice** — the one familiar from graphene, carbon nanotubes, and benzene rings. The relevant features:

- **Vertices** (nodes) of the lattice are points where three edges meet at 120° — a *wye junction*. Each node has exactly 3 incident edges.
- **Faces** of the lattice are hexagons.
- **Edges** are the line segments between adjacent nodes; each edge is one cylinder primitive.

The two "sublattices" of the honeycomb (the A-sublattice and the B-sublattice — 3-coordinated nodes whose neighbors come from the other sublattice) form a 2-site unit cell. Each unit cell has 1 A-node, 1 B-node, and 3 edges (the three connecting the central A to its three nearest-B neighbors, equivalently). 3 edges × 2 cylinder DoF (*e*, *φ*) per edge = 6 DoF per unit cell.

Why hexagonal and not triangular? Per [grid/hexagonal.md](../../grid/hexagonal.md), the hexagonal lattice has cleaner wave propagation (89% energy transmitted per junction vs. 56% for triangular), supports curvature naturally through pentagonal defects, and gives the cleanest analog to Planck-scale carbon-nanotube physics. Per [grid/lattice-geometry.md](../../grid/lattice-geometry.md), the wye-junction count under Model B (cell-IS-its-edges) gives ζ_2D = 1/3, the 2D analog of GRID's 3D ζ = 1/4. Triangular would have given different numbers; hexagonal is the natural choice.

Periodic boundary conditions close the lattice into a torus, eliminating boundary effects.

---

## 2. The wave equation on the 2D lattice

Each edge carries a cylinder primitive whose dynamics are chapter 2's wave equation. Each node enforces continuity of (*e*, *φ*) across all incident edges (chapter 1 §5). Together, these give the lattice equations of motion.

### Long-wavelength continuum

For wavelengths much larger than the lattice spacing *a*, the lattice "looks" continuous, and the wave equation reduces to the form chapter 4 §4 already wrote down:

<!-- D ∂_t² u = M (∂_x² + ∂_y²) u = M ∇² u -->
$$
D\, \partial_t^2\, \mathbf{u} \;=\; M\, (\partial_x^2 + \partial_y^2)\, \mathbf{u} \;=\; M\, \nabla^2\, \mathbf{u}
$$

where **u**(*x*, *y*, *t*) = (*e*, *φ*)ᵀ is the stress vector field, *D* is the inertia matrix, and *M* is the stiffness matrix. The 2D Laplacian ∇² replaces the 1D ∂_x² of a single cylinder; the matrices *D* and *M* are unchanged.

### Discrete lattice

At the scale of a few lattice spacings, the discrete structure matters. The wave equation becomes a system of coupled difference equations: each edge's (*e*, *φ*) at the next time step is determined by the values at neighboring edges according to the cylinder dynamics, with node continuity enforced at each vertex.

Solving the lattice problem in full requires Bloch-wave analysis (the discrete analog of plane waves), introduced in §4. The continuum limit of §3 is the long-wavelength projection of that analysis.

---

## 3. The long-wavelength continuum limit

In the continuum equation *D* ∂_t² **u** = *M* ∇² **u**, look for plane-wave solutions in 2D:

<!-- u(x, y, t) = A exp(i(k·r - ωt)) -->
$$
\mathbf{u}(x, y, t) \;=\; \mathbf{A}\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}
$$

with **k** = (*k_x*, *k_y*) the 2D wavevector and **A** the amplitude vector. The Laplacian ∇² applied to this ansatz brings down a factor of −|**k**|² where |**k**|² = *k_x*² + *k_y*².

Substituting into the wave equation:

<!-- ω² D A = |k|² M A -->
$$
\omega^2\, D\, \mathbf{A} \;=\; |\mathbf{k}|^2\, M\, \mathbf{A}
$$

This is identical in form to chapter 2's eigenvalue problem, with |**k**|² replacing *k*². The dispersion relation becomes:

<!-- ω²(k) = |k|² λ_± -->
$$
\omega^2(\mathbf{k}) \;=\; |\mathbf{k}|^2\, \lambda_{\pm}
$$

with λ_± the two eigenvalues of *D*⁻¹*M* — the same eigenvalues from chapter 2. The mode speeds are the same: *c*_+ = √λ_+ = *c* (after chapter 3's constraint) and *c*_− = √λ_− ≈ 0.414 *c*.

So at long wavelengths, the 2D lattice supports the *same* two modes that chapter 2 derived for a single cylinder. Each mode propagates isotropically (in any direction in 2D) at its own speed.

**The 2D lattice does not modify the long-wavelength continuum result.** The slow mode is present at long wavelengths exactly as the single-primitive analysis predicted.

---

## 4. The Brillouin zone and band structure

The discrete lattice's modes are described by *Bloch waves* — plane waves modulated by the lattice's periodic structure. For each Bloch wavevector **k** in the **Brillouin zone** (a hexagonal region in **k**-space, 2π/*a* across), the lattice supports a discrete set of frequencies — the **bands** of the dispersion relation.

The number of bands per **k**-point equals the number of independent degrees of freedom in the unit cell. For our hexagonal lattice with 3 edges per unit cell × 2 cylinder DoF per edge:

> Number of bands per Brillouin-zone point = 6.

These 6 bands form 6 surfaces ω_n(**k**) (n = 1, …, 6) over the Brillouin zone.

A plane-wave solution at long wavelengths corresponds to **k** near the zone center (**k** ≈ 0). Near zone center, the bands take the form ω_n(**k**) ≈ *c*_n |**k**| if the band is **acoustic** (gapless, ω(0) = 0) or ω_n(**k**) ≈ ω_n(0) + … if the band is **optical** (gapped, ω(0) > 0).

The acoustic/optical distinction is the key question for the slow-mode fate.

---

## 5. Are there acoustic vs. optical bands?

In a typical phononic system (graphene, ionic crystals, etc.) with a multi-atom unit cell, some bands are acoustic and others are optical. The optical bands arise from internal oscillations *within* the unit cell — modes where parts of the cell oscillate against each other at finite frequency even at **k** = 0.

For our cylinder lattice with **identical** cylinders on every edge and node continuity as the only inter-cylinder coupling, the situation is different. The 6 bands per **k**-point are *not* genuinely separate physical modes; they are a relabeling of the long-wavelength continuum's 2 modes via Brillouin-zone folding.

Here is the algebra in outline. The long-wavelength continuum equation has 2 mode solutions (chapter 2's fast and slow modes). When we write this equation on the discrete hexagonal lattice with a 6-DoF unit cell, the same 2 modes appear at every Brillouin-zone wavevector — but the unit-cell structure forces the 2 modes to "fold" into 6 bands per **k**-point. The folding is a consequence of periodic boundary conditions and the unit-cell choice; it does not generate new physics.

In particular, the bands are gapless at **k** = 0: all 6 bands have ω(**k** = 0) = 0. There are no optical (gapped) bands. The 6 bands, at long wavelengths, are 6 zone-folded copies of the 2 modes from chapter 2.

This is a substantive negative finding. It says: the hexagonal lattice with identical cylinders and passive node continuity *does not gap the slow mode*. The slow mode propagates at long wavelengths at *c*_− ≈ 0.414 *c*.

For the slow mode to be gapped, the lattice would need additional structure that we have not introduced — a non-trivial potential V(*e*, *φ*), an asymmetry between the two sublattices, a multi-cylinder interaction at nodes, or some other internal cost for differential oscillations within the unit cell. Without one of these, the lattice cannot gap the slow mode.

This is candidate (iii) from the README — the "Planck-scale gap" candidate — turning out *not* to be automatically delivered by the hexagonal lattice's geometry.

---

## 6. The slow-mode fate at long wavelengths

The honest result of §3–§5 is that the slow mode persists as a propagating wave at long wavelengths, at speed *c*_− ≈ 0.414 *c*. The 2D lattice geometry does not, by itself, gap or remove it.

This is a real prediction of the cylinder-primitive model in its current form. It is not a calculation artifact, and it does not factor out cleanly under the lattice analysis the chapter just performed.

The implications are:

- **For chapters 6–8.** The Maxwell bridge (chapter 6) and the gravity bridge (chapter 7) inherit the slow mode as a feature of the lattice they are bridging from. Chapter 6 has to decide whether the slow mode coarse-grains to a Maxwell field component or to a separate physical degree of freedom — that is candidate (ii) from the README.
- **For experimental match to vacuum Maxwell.** Vacuum Maxwell has only the photon at *c*. A second propagating mode at 0.414 *c* would be an observable prediction. Pulsar arrival times, supernova light curves, and dispersion measurements would see it as a trailing component of any electromagnetic signal. Existing bounds are tight; a literal, isolated slow mode at the cylinder primitive's predicted speed would be falsified.

So either the slow mode does not couple to electromagnetic observables (candidate ii — the slow mode is a non-radiative, gauge-fixable, or otherwise hidden component of the field), or the cylinder primitive model has an open anomaly that requires repair.

---

## 7. Scale separation: where the 18-orders-of-magnitude argument helps

The cylinder primitive is at Planck scale (*L*_P ≈ 10⁻³⁵ m). Observable electromagnetic radiation is at scales 18+ orders of magnitude larger (atomic-emission wavelengths ~10⁻⁷ m; pulsar dispersion measured at radio wavelengths ~10⁻¹ to 10² m; etc.). This scale separation has two distinct effects.

**Where it helps.** If the slow mode acquired a *gap* at lattice scale — ω_−(**k** = 0) ≈ 1/τ_P (the Planck frequency) — that gap would correspond to an energy gap of order the Planck energy *E*_P ≈ 1.2 × 10¹⁹ GeV. At observable energies (electronic transitions ~ eV; gamma-ray ~ MeV–GeV), the gap is enormous compared to any available energy: the slow mode is energetically frozen out, completely invisible to all known experiments. This would be the "*Planck-scale gap*" candidate — option (iii).

**Where it does not help.** If the slow mode is *gapless* — the situation §5 actually delivered for our model — then it propagates at all wavelengths. There is no scale at which it decouples; pulsar dispersion at meter wavelengths would see it as readily as Planck-scale physics would. The 18-orders-of-magnitude argument does not bury a gapless mode.

So our chapter-5 finding (the slow mode is gapless on the hexagonal lattice with identical cylinders) is exactly the case where the scale-separation argument *does not save us*. The resolution has to come from somewhere other than scale separation alone.

---

## 8. Where the resolution must come from

Three options are available, none of them resolved by chapter 5 alone.

### Option (i): emergent Lorentz symmetry

In vacuum Maxwell, both photon polarizations travel at *c* because Lorentz symmetry exactly enforces it. On our lattice, Lorentz symmetry is only emergent at long wavelengths; it is not a property of the discrete lattice itself. The two-speed split could be a discrete-lattice artifact that is averaged out as Lorentz symmetry emerges in the continuum limit.

The chapter-5 finding is unfavorable to this option: the long-wavelength continuum *already* shows the two-speed split (§3 of this chapter). If Lorentz symmetry were going to remove it, the continuum limit is exactly where it would happen, and it has not. So option (i) is ruled out by the chapter-5 calculation.

### Option (ii): longitudinal/non-radiative coarse-graining

Maxwell's electromagnetic field has more degrees of freedom than just two transverse photon polarizations. In Coulomb gauge, the longitudinal component of **A** and the scalar potential are non-radiative: they do not propagate as waves; they are fixed by sources via Gauss's law. The slow mode might coarse-grain to one of these non-propagating degrees of freedom.

For this to work, when chapter 6 coarse-grains the cylinder primitive's (*e*, *φ*) to Maxwell's (θ on cells, *A*_μ on links), the slow mode would have to project onto the non-radiative subspace — the components of *A*_μ that get gauge-fixed away. The fast mode would project onto the transverse photon polarizations.

This is the most physically plausible resolution remaining. It depends on the details of how (*e*, *φ*) coarse-grains to Maxwell's field components, which is exactly chapter 6's task.

### Option (iii): Planck-scale gap (not delivered by lattice geometry alone)

A Planck-scale gap on the slow mode would solve the problem cleanly via scale separation (§7). The hexagonal-lattice analysis of §5 did not produce one. A gap could still emerge from additional physics not yet in the model:

- A potential V(|**ψ**|) suppressing |**ψ**| = 0 (Mexican-hat / Higgs-like). This adds a "mass term" to the slow mode in the field-theory sense (a gap in the dispersion at **k** = 0), at the cost of breaking the strict linearity of chapter 1's primitive.
- A non-trivial node interaction beyond simple continuity, costing energy for the slow-mode-like configurations within a unit cell.
- A hidden constraint on the (*e*, *φ*) field that has the same effect.

Each of these requires *adding* something to the model. The minimal cylinder primitive of chapters 1–4 does not deliver a Planck-scale gap on its own.

### Combination resolution

The most likely final picture is a combination of (ii) and (iii): the slow mode's coarse-graining onto Maxwell may project most of it onto non-radiative components (option ii), with any residual radiative component being suppressed by lattice-scale physics (option iii) — even if the gap is sub-Planck and not strictly forbidden. Both mechanisms work together.

---

## 9. Risks and unresolved issues

- **Risk A — slow mode persists.** Chapter 5's primary calculation finds the slow mode is gapless on the hexagonal lattice. The chapter does not resolve the slow-mode-vs-vacuum-Maxwell tension on its own. Candidate resolutions (ii) and (iii) above push the resolution to chapter 6 (longitudinal/non-radiative coarse-graining) or to a model addition (a potential or constraint). A worst-case outcome is option (d): document the anomaly clearly. Per the user's "optimal computational substrate" framing, the cylinder primitive is a model of an idealized lattice, not a real material — it is permitted to have features that no rubber substance would have, and the slow-mode anomaly may be one such feature that an "optimal computational lattice" exhibits in our specific geometry. If chapter 6 cannot resolve cleanly, the project should document the anomaly and the conditions under which it would or would not be observable, and continue with the parts of the project (chapter 4's entropic gravity scaling, chapter 8's α derivation) that are unaffected.
- **Risk B — choice of hexagonal lattice.** This chapter committed to the hexagonal lattice based on grid/hexagonal.md's analysis. A different lattice (triangular, square) could have given different band-structure results. We are not exploring those alternatives in this chapter; if chapter 6 fails to resolve the slow-mode tension, returning to consider lattice-geometry alternatives may be warranted.
- **Risk C — model robustness.** The chapter-5 result is robust to the specific choice of stiffness parameters: the slow mode is gapless for *any* χ̃ ∈ (0, 1) in the simplifying special case. This means no parameter tuning saves us; the slow mode is structural to the cylinder primitive's design, not a one-time accident.

---

## 10. Summary of givens

What this chapter establishes:

- The 2D *hexagonal* lattice with cylinder primitives on edges and wye-junction node continuity is the natural substrate, matching grid-docs preferences and giving ζ_2D = 1/3.
- The long-wavelength continuum limit of the lattice equations of motion reproduces chapter 2's two-mode result: a fast mode at *c* and a slow mode at *c*_− ≈ 0.414 *c*. Both modes are gapless.
- Lattice-scale Bloch analysis of the hexagonal lattice with identical cylinders gives 6 bands per Brillouin-zone point, but these are *zone-folded copies* of the 2 long-wavelength modes — there are no genuinely optical (gapped) bands. The hexagonal lattice with passive node continuity *does not* gap the slow mode.
- The 18-orders-of-magnitude scale separation between Planck length and observable wavelengths *does* save the model if the slow mode acquires a Planck-scale gap, but the chapter shows the lattice does not deliver such a gap automatically.
- The slow-mode tension is therefore not resolved by chapter 5. Resolution must come from either chapter 6 (the slow mode coarse-grains to a Maxwell non-radiative component — candidate ii) or from a small extension to the cylinder-primitive model (a potential or constraint that gaps the slow mode — candidate iii).

The next chapter takes up Maxwell coarse-graining and asks how the cylinder primitive's two modes project onto Maxwell's field components — the place where candidate (ii) is decided.
