# Chapter 9 — Closing Summary

This project set out to develop a mathematical model of the GRID lattice's primitive — the smallest unit at which edges, nodes, and ultimately the lattice itself are modeled. Chapters 1–8 worked through the model in production form. This chapter consolidates what was established, what was discovered along the way (sometimes against early expectations), what was ruled out, and what remains for follow-up.

---

## 1. The arc of the project

The project's central question, from [README.md](README.md):

> *What is the simplest mathematical object that, assembled into a 2D periodic lattice, supplies the common base from which Maxwell's equations and the entropic-gravity story already established at the lattice scale remain derivable — and where, in that object, does α appear?*

The answer the project arrived at is a specific geometric primitive — a 2D cylindrical tube with two coupled internal fields, on a 2D hexagonal lattice with wye-junction node continuity. The cylinder is the substrate-level "edge" of GRID; the lattice it forms is the GRID lattice at one level of granularity below where Maxwell and gravity are derived. The chapter-by-chapter arc:

- **Chapters 1–3** established the cylinder primitive, its wave dynamics, and the lattice-cadence constraints. The matched-chirality structure (chapter 1 §8) is the critical foundational commitment that makes the rest work.
- **Chapter 4** confirmed the entropic 1/r force scaling for 2D gravity, with three independent simulation tests in [scripts/](scripts/) at the percent level.
- **Chapter 5** assembled the cylinder primitives into a hexagonal lattice and confirmed clean photon propagation at *c* with no anomalies.
- **Chapters 6–7** built the bridges to grid/maxwell.md and grid/gravity.md, supplying the inputs each takes (cell-level phase θ, link-level connection *A_μ*, and the 2D analog ζ_2D = 1/3 of the per-cell information capacity).
- **Chapter 8** examined the wrap-and-α question. The result was *inconclusive*: a candidate physical picture for α (the kink-loss fraction per closed wrap) and a sharper target for follow-up calculation, but no controlled structural form. The leading-order kink-loss formula has order-unity expansion parameter at the relevant *N* and assumes incoherent kink summation that is not appropriate for a coherent closed loop, so the chapter walked back its earlier "structural ratio with one free variable" claim to a conditional candidate.

The project did not produce either a numerical prediction of α or an established structural form. What it did produce is a sharper *target* for a future α-relevant calculation, contingent on prerequisites this project did not establish.

---

## 2. Established results

The project established the following at the level of derivation supported by the chapter-by-chapter analysis (and where flagged, by simulation):

### The cylinder primitive (chapter 1)

- Each edge of the lattice is a 2D cylindrical tube with length *L* and cross-section radius *r*.
- The cylinder hosts a 2D internal stress vector ψ at every cross-section, parameterized in polar coordinates as magnitude *e(x, t)* and azimuthal direction *φ(x, t)*. The underlying object is a complex-scalar field ψ = *e* exp(*i φ*).
- The cylinder is a *distributed* primitive (state varies along its length), not a lumped one. Nodes (wye junctions) are passive continuity boundaries with no state of their own.
- The cylinder's dynamics are governed by two 2 × 2 matrices: a stiffness matrix *M* and an inertia matrix *D*. Both have the same chiral structure ("matched chirality"), characterized by a single dimensionless parameter χ̃ ∈ (0, 1).
- The matched chirality has a natural physical origin under the fractal-microgrid interpretation: the same helical microstructure that produces *K_eφ* (chiral stiffness) also produces *D_eφ* (chiral inertia). Substrate inertia is itself an emergent KK-style quantity from the cross-section circumference, structurally parallel to particle rest mass in [metric-mass](../metric-mass/) at a different scale.

### Wave dynamics (chapter 2)

- The wave equation *D* ∂_t² **u** = *M* ∂_x² **u** has, under matched chirality + bare-speed equality, the simple form ω = *c* |*k*|. Both polarizations propagate at *c*, with no birefringence at the propagation level.
- The natural shear value χ̃ = 1/√2 is the geometric center of the stable range. Under matched chirality, χ̃ governs internal channel coupling but does not affect the propagation speed.
- The stable range is χ̃ ∈ (0, 1) strictly. Both *M* and *D* must be positive-definite for the energy to be bounded below.
- Bidirectional propagation symmetry holds: ω² depends on *k* only through *k*², so left-going and right-going waves propagate at identical speeds. The medium has no Faraday-like effect.
- The wave equations are linear; superposition holds, and two opposing pulses pass through each other intact.

### Lattice-cadence constraints (chapter 3)

- Imposing the cylinder's internal propagation speed equal to the lattice signal speed *c* (axiom A1) plus matched chirality plus the bare-speed condition (*K_ee*/ρ = *K_φφ*/*I_φ* = *c*²) gives a clean reduction: the matrices satisfy *M* = *c*² *D*.
- The dimensionless stiffness-and-inertia ratios are pinned by *c* together with χ̃. The cylinder length *L*, the cross-section radius *r*, and an overall stiffness scale remain as free parameters.

### Entropic gravity scaling (chapter 4)

- In static equilibrium on the 2D lattice, each component of the stress vector field independently satisfies the 2D Laplace equation. The chiral coupling drops out at static; each component decays as the 2D Laplacian Green's function.
- The Laplacian Green's function is logarithmic: *G*(*r*) = (1/2π) log(*R*/*r*). The gradient gives a 1/r force law, the 2D analog of gravity's 1/r² force law.
- At finite temperature, Gaussian fluctuations of the linear field produce a logarithmic *variance shadow* around any pinned inclusion. Integrated along any horizon-analog curve, this gives an entropy that scales linearly with the curve's length — exactly the area-scaling Jacobson's argument requires.
- Three independent simulation tests (static field decay, thermal variance shadow, two-body force-vs-separation) confirm the predictions at the percent level.

### 2D lattice assembly (chapter 5)

- The hexagonal (honeycomb) lattice with wye-junction node continuity is the natural geometry, matching grid-docs preferences ([grid/hexagonal.md](../../grid/hexagonal.md), [grid/lattice-geometry.md](../../grid/lattice-geometry.md)).
- The hexagonal-lattice analog of the per-cell information capacity is ζ_2D = 1/3, from the wye-junction count under Model B.
- Under matched chirality, the lattice's collective modes have a single dispersion ω = *c* |**k**| at long wavelengths. The Brillouin-zone band structure has 6 bands per BZ point, but they are zone-folded copies of the single dispersion — no anomalies, no slow-mode persistence, no extra physical excitations.

### Bridge to Maxwell (chapter 6)

- The cylinder's complex stress-vector field ψ = *e* exp(*i φ*) is the matter field that grid/maxwell.md takes as input. At each lattice node, *φ* is the cell phase θ; along each edge, ∂_μ *φ* is the link-level gauge connection *A_μ*.
- Local U(1) gauge invariance is automatic in the cylinder primitive — it is the polar-coordinate freedom on the 2D stress vector. We do not impose gauge invariance as an extra axiom; it is built into the foundation.
- The cylinder primitive's two propagating polarizations correspond to Maxwell's transverse photon (radiative) and longitudinal/Coulomb component (gauge-fixable, non-radiative under Coulomb gauge). Both propagate at *c* in the unfixed formulation.

### Bridge to gravity (chapter 7)

- The cylinder primitive's continuum entropy coefficient is 1/(2π) per log(distance), set by the 2D Laplacian Green's function.
- This continuum coefficient is consistent with ζ_2D = 1/3: a lattice-geometry factor of order unity (specifically, 2π/3) bridges the two, and the chapter-7 consistency check confirms no obstruction stands in the way. The factor itself is not computed in this project.
- A full numerical match across all O(1) factors is a well-defined but tedious calculation, deferred to follow-up.

### α as an inconclusive candidate picture (chapter 8)

- A candidate physical picture for α: the per-loop fractional energy loss when a 2D sheet of cylinder primitives is wrapped into a closed polygonal surface.
- A sharpened target for follow-up: the matched-chirality scattering problem at a lattice-level kink, summed coherently around an *N*-kink loop. If carried out with a concrete kink model and a coherent-summation treatment, this calculation would either produce a controlled structural form for α or rule the kink-loss picture out.
- Two limitations of the leading-order treatment surface at *N* = 6: the (Δθ)² perturbative expansion has order-unity expansion parameter ((π/3)² ≈ 1.10), and the η_loop = *N* · η_kink rule assumes incoherent kink summation that does not apply to a coherent closed loop. Either limitation can change the leading-order form qualitatively at the *N* of interest. The leading-order formula α ≈ (2π²/3) · *K*(1/√2) is therefore a *placeholder*, marked conditional throughout chapter 8, not a controlled result.
- The fractal-recursion observation: the cylinder primitive's cross-section wrap (one fractal level below the sheet wrap that motivates α) produces mass-analog (substrate inertia, "dark mass" in MaSt terminology) via the standard KK mechanism. The 1D circumference wrap cannot produce charge (charge requires a 2D wrap of a sheet into a closed surface); any radial leakage at the cross-section level is dynamic and time-averages to zero. This is qualitative — it explains why the cross-section wrap doesn't add an unaccounted feature, not why it produces any specific quantity.

---

## 3. Mid-project discoveries

Some results emerged through the chapter-by-chapter work that were not anticipated at the outset of the project. Worth recording explicitly.

### The slow-mode tension was not real

Early drafts of chapters 2–5 worked with a *diagonal* inertia matrix *D* = diag(ρ, *I_φ*) and a non-diagonal stiffness matrix *M*. That setup produced two propagating modes at different speeds — a fast mode at *c* and a slow mode at ≈ 0.414 *c*. The slow mode was an apparent prediction of vacuum birefringence, incompatible with experiment.

The resolution was to recognize that an honest model of a chirally-structured medium must have *both* matrices carry the chirality — *matched chirality*. The diagonal-*D* simplification was inconsistent: a medium whose helical microstructure produces chiral coupling in the elastic energy should also produce chiral coupling in the kinetic energy. With matched chirality, the matrices satisfy *M* = *c*² *D*, the eigenvalue degeneracy becomes exact, and both polarizations propagate at *c*.

The discovery here was that what looked like a real slow-mode tension (significant enough that chapter 5 and the README originally framed it as a load-bearing risk) was actually an artifact of an inconsistent simplification at the foundation. Once the simplification was corrected, the tension dissolved without trace.

### Linear-Gaussian theory carries the entropy account

Chapter 4 was originally framed around the question of whether topological vortex defects in the 2D stress vector field could supply enough entropy for Jacobson's gravity. The chapter's discovery was that *they are not needed*: the linear-Gaussian theory's Laplacian Green's function structure already produces 1/r force scaling, with the right area-scaling for Jacobson. The argument runs in either polar or Cartesian fluctuation coordinates around a non-zero stress-vector background (Ch4 §4 establishes the equivalence), so the simulations — which work in Cartesian — test the right physics.

Topological defects remain in the picture as a possible refinement at the coefficient level, and as the structural element on which chapter 8's wrap picture would depend. But for the entropy account itself, the linear-Gaussian theory is sufficient. This was not the original expectation.

### Substrate inertia is mass-analog by KK mechanism

Chapters 1–5 originally framed the cylinder primitive's inertia matrix *D* as substrate-level coefficients distinct from particle rest mass — a category-error guard against conflating with [metric-mass](../metric-mass/)'s rest-mass-from-compact-dimension story. Late in the project, that framing was reversed: substrate inertia is, in fact, *the same KK-style mass-from-compact-wrap mechanism* as particle rest mass, just at a different scale (sub-Planck cross-section of the cylinder vs Compton-scale compact dimension *u* of metric-mass). The cylinder primitive's *D* matrix is a mass-analog quantity, "dark mass" in MaSt terminology.

This unifies the project's foundations with metric-mass cleanly: both are mass-from-compact-wrap stories. They differ in scale, not in mechanism.

### α — controlled-regime free-variable count is not the regime of interest

Per the user's reframing of chapter 8: the α outcome was to be assessed by how many free variables α reduces to. The leading-order analysis *would* give a single-free-variable outcome — α ≈ (2π²/3) · *K*(1/√2), with the geometric prefactor coming from the hexagonal lattice and the natural shear, and only the kink-loss coefficient *K*(1/√2) free — *if* the leading-order formula were controlled at *N* = 6.

The mid-project discovery was that it isn't. The (Δθ)² expansion has order-unity expansion parameter at *N* = 6, and the incoherent-summation rule assumed in the leading-order formula is not appropriate for the coherent closed loop where α-relevant physics lives. The clean "1 free variable" count holds only in the controlled regime (large *N*, small Δθ), and in that regime the kink-loss vanishes — no α to count.

The honest position: the count at *N* = 6 is *unestablished*. Whether α reduces to one parameter, several, or none — and in what functional form — is not settled by this project. This was a more conservative outcome than the "interesting ratio" hope of the original calibration, but it is what the math actually supports.

---

## 4. Ruled out

Some candidates that the project examined and rejected:

- **The slow mode as a real prediction.** Resolved at the foundation level via matched chirality (chapter 1 §8). Both polarizations are at *c*; there is no slow-mode physical entity.
- **Topological defects as the primary entropy mechanism.** The linear-Gaussian theory's Green's function structure is sufficient for Jacobson scaling (chapter 4). Defects survive as a possible refinement and as structural input for chapter 8.
- **Charge from the cylinder cross-section.** The 1D circumference wrap is the wrong topology for charge. Charge requires the 2D-sheet-into-torus wrap of chapter 8. The cross-section wrap produces mass-analog only.
- **Independent diagonal-*D* and non-diagonal-*M*.** This combination is inconsistent for a chirally-structured medium. Matched chirality is the only physically motivated choice.
- **A "true derivation" of α from the cylinder primitive.** No such derivation emerged.
- **A controlled structural form for α at *N* = 6.** The leading-order kink-loss formula is not a controlled approximation in the regime where α would live. What chapter 8 produced is a candidate physical picture and a sharper target for follow-up calculation — not a controlled structural form.

---

## 5. Open questions and follow-up work

Several questions are well-defined but not resolved in this project; they are available as follow-up.

### Calculations available as follow-up

- **The α follow-up is a multi-step calculation, not just a single coefficient.** To make the chapter-8 picture concrete one must (i) specify a lattice-level kink model (which edges are bent on the hexagonal lattice and what matching conditions apply at the bend), (ii) solve the matched-chirality scattering problem at that kink to obtain *K*₂(χ̃), *K*₄(χ̃), … or, ideally, the full η_kink(Δθ), and (iii) sum *coherently* around the *N*-kink loop. Steps (ii) and (iii) together would either produce a controlled structural form for α or rule the kink-loss picture out at *N* = 6. The chapter-8 leading-order formula is the *first term* of step (ii), not a complete answer.
- **Full numerical match of the gravity coefficient.** Chapter 7's structural-form match (1/(2π) × 2π/3 = 1/3) is sufficient at the structural level. A full O(1)-factor calculation would give a definite numerical comparison and either confirm or call attention to a residual discrepancy.

### Conceptual extensions

- **3D extension of the cylinder primitive lattice.** The project commits to 2D per ground rule 7. A 3D extension (cylinders along edges of a 3D lattice, e.g., simplicial or cubic) would give Maxwell its full 3+1D form (two transverse photon polarizations) and gravity its standard 1/r² force law. This is the natural next step.
- **Specific MaSt-particle structures.** Chapter 8 fixed *N* = 6 by the hexagonal lattice's symmetry, but actual physical particles in MaSt have specific compact-dimension structures that may require different *N* (or *χ̃*, or some other parameter combination). The "which particle's α?" question is unresolved.
- **The fractal recursion in detail.** The cylinder primitive's microstructure (the wrapped microgrid that gives it inertia and chirality) is acknowledged but not pursued (ground rule 3). A serious treatment of the next fractal level would derive the cylinder's *D* and *M* matrices from microgrid geometry, possibly producing additional structural constraints.

### Further questions

- **The 2D entanglement-entropy log violation.** Free 2D fields have entanglement entropy that is not strictly area-scaling — there is a logarithmic correction. Whether this affects the Jacobson argument's applicability in 2D is a subtlety flagged in chapter 7 §8. The natural 3D extension would resolve this.
- **The non-precise shear question.** If χ̃ ≠ 1/√2 (say, due to a future constraint from downstream physics), the asymmetry between strain and azimuthal channels would land somewhere observable. Whether this is a real consequence or a calculation artifact is open.

---

## 6. The cylinder primitive in context

A few framings worth recording.

### What the cylinder primitive is

The cylinder primitive is a *hypothetical computational element* — a substrate-level structure that, when assembled into a 2D hexagonal lattice, supplies all the inputs required for grid/maxwell.md and grid/gravity.md to produce their respective derivations. It is *not* claimed to be made of any particular material; the rubber-cylinder mechanical analog is an intuition-builder, not a substance claim. It is closer to an idealized computational substrate — what the lattice's information-processing machinery looks like at one level below the cells where Maxwell and gravity are derived.

The qualities the cylinder primitive is *required* to have, for the model to work, are stated explicitly across chapters 1–3:

- A 2D internal stress vector at every cross-section, parameterized in polar coordinates as (*e*, *φ*).
- A 2 × 2 stiffness matrix *M* and a 2 × 2 inertia matrix *D*, both real symmetric and positive-definite.
- Matched chirality between *M* and *D*, characterized by a single parameter χ̃ ∈ (0, 1).
- Bare-speed equality: *K_ee*/ρ = *K_φφ*/*I_φ* = *c*² (the lattice signal speed).
- The wye-junction node continuity (continuous stress vector across meeting endpoints).
- The 2D hexagonal lattice geometry.

These are the qualities we postulated. Stating them clearly is part of the project's product. A different cylinder primitive (different qualities) would give different physics; the cylinder primitive *we built* is the one that produces vacuum-Maxwell-style propagation and 2D-Jacobson gravity at the lattice scale.

### What this project added relative to GRID

The grid/ derivations work at the lattice scale and take cell-level phase θ, link-level connection *A_μ*, and information capacity ζ as inputs. This project supplied those inputs from one level of granularity below — from a primitive that, when assembled, produces the inputs grid/maxwell.md and grid/gravity.md need.

What the project did *not* do: it did not re-derive Maxwell or gravity. Those derivations live in grid/maxwell.md and grid/gravity.md respectively, and run unchanged on top of the lattice this project supplies.

What the project did add: a substrate-level mechanical (or computational, if the rubber analog is too suggestive) picture of the lattice. Where GRID's foundations posit cells with phase θ and links with connection *A_μ*, this project says: a cell is a wye junction, a link is a cylinder primitive, and the matter field ψ = *e* · exp(*i φ*) at each node *is* the matter field with phase θ that grid/maxwell.md takes as input. The gauge connection *A_μ* is *not* directly supplied by the cylinder primitive in its current 2D form (Ch6 §4); it is motivated by the cylinder primitive's U(1) gauge symmetry but enters as an additional field in grid/maxwell.md's gauge sector. The matter sector and the gauge symmetry are supplied; the gauge field itself awaits the 3D extension or topological winding (Ch8) to enter directly.

### What the project added relative to grid/charge-emergence.md

[grid/charge-emergence.md](../../grid/charge-emergence.md) was candid that its account of the α magnitude was hand-wavey. Chapter 8 of this project does not improve on that magnitude either, and the analysis it does provide is conditional on prerequisites that have not been satisfied at the *N* of interest. What chapter 8 *does* add is a sharper *target* for a follow-up calculation: a specific candidate physical picture (kink-loss on a closed wrap), a specific calculation that would settle whether the picture is right (matched-chirality scattering plus coherent loop summation), and a specific regime where the calculation is non-trivial (order-unity Δθ, *N* of order few). Whether this constitutes an improvement over charge-emergence.md depends on whether the follow-up calculation is performed and what it produces; this project does not settle the question.

### Closing thought

The project's primary deliverable was a substrate-level picture that produces vacuum-Maxwell-style propagation and 2D-Jacobson gravity at the lattice scale. The chapters 1–7 analysis delivers that picture, and three numerical tests confirm the gravity scaling. The α question of chapter 8 was equal-priority but separate; its outcome is inconclusive — a candidate physical picture and a sharpened follow-up target, but no controlled structural form at the lattice configuration of interest. Whether the cylinder primitive is *the* right substrate or one of several is a question the project does not settle.
