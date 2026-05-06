# grid-primitive

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** A mathematical model of the GRID lattice's primitive — the smallest unit at which edges, nodes, and ultimately the lattice itself are modeled.
**Method:** Mathematical derivation as discovery; visualization where it sharpens intuition; minimal computation.
**Status:** All chapters drafted. Three numerical fail-fast tests in [scripts/](scripts/) confirm the chapter-4 prediction (1/r force scaling on the 2D lattice). Chapters 1–7 establish the cylinder primitive's consistency with vacuum Maxwell and entropic gravity at the lattice scale. Chapter 8's α exercise is *inconclusive*: a candidate picture and a sharpened follow-up target, but no controlled structural form for α at *N* = 6 (see chapter 8 §4 and §9).

## Why this project exists

The GRID framework derives Maxwell's equations, Einstein's field equations, charge quantization, and entropic gravity from a 4D causal lattice with cell-level phase, gauge connection, and an information-resolution parameter ζ (see [grid/foundations.md](../../grid/foundations.md)). Those derivations treat the lattice as a whole — they do not commit to what an *individual primitive* is, only that there are edges and nodes whose collective behavior produces the observed physics.

This project takes up the primitive itself. The central question:

> *What is the simplest mathematical object that, assembled into a 2D periodic lattice, supplies the common base from which Maxwell's equations and the entropic-gravity story already established at the lattice scale remain derivable — and where, in that object, does α appear?*

The dialog [`dialogs/grid-3.md`](../../dialogs/grid-3.md) brainstormed several candidate primitives and converged on a particular one: a **2D cylindrical tube** with two coupled internal degrees of freedom — longitudinal strain and azimuthal phase. This project develops that primitive in production form: checking that it works, where it doesn't, and what it implies for charge, mass, and gravity.

## The primitive

The grid is built from edges and nodes, arranged on a 2D sheet (for compact dimensions or MaSt sheets) or a 3D extent (for the spatial lattice S). Each edge is modeled as a small **2D cylindrical tube** — nanotube-like in structure, but with no commitment to atomic-scale carbon-nanotube physics.

The cylinder is a **distributed** primitive: it has length *L*, and the state at each cross-section is a 2D internal stress vector. In polar coordinates, the stress vector has magnitude *e(x, t)* (the strength of longitudinal compression/tension) and azimuthal direction *φ(x, t)* (the angular location around the cross-section where that stress is concentrated). A perturbation at one end takes transit time τ = *L*/*c* to reach the other. A wall-shear coupling *K_eφ* between magnitude and azimuth makes the two coordinates drive each other along the cylinder, which is what allows the edge to carry a propagating wave.

Mechanical intuition: a rubber cylinder reinforced with helical fibers in its wall, glued to its neighbors at the endpoints. Imagine pushing on the end of the cylinder *off-center* — at some azimuthal location around the rim. The push exerts a longitudinal compressive force at that location. The helical fibers couple this off-center longitudinal load to a transverse bow of the cylinder body, which propagates along the length and emerges as a perturbation in the (*e*, *φ*) stress vector for the next cylinder to receive. The cylinder body does not rotate; the off-center loading is what carries the directional information.

Nodes are passive junctions where multiple cylinders meet. They hold no state of their own; their role is to impose continuity — the (*e*, *φ*) values match across a junction where adjacent cylinder endpoints connect. There is no node update rule.

The cylinder is *deemed continuous* at this level of description. The dialog notes that the cylinder wall could itself be a finer-grained grid (a wrapped microgrid with shear), making the primitive a fractal recursion. This recursion is acknowledged but not pursued — at some level the description must stop, and we stop at the cylinder.

## Layer relationship

This project sits one layer below the GRID lattice scale where Maxwell and gravity are already derived:

```
MaSt (particles, masses, charges)
   ↑
GRID lattice (Maxwell, Jacobson, ζ, α-as-input)         ← grid/maxwell.md, grid/gravity.md
   ↑
GRID primitive (this project — cylinder, e, φ, shear)
   ↑
[sub-cylinder microgrid — acknowledged, not pursued]
```

The grid/ derivations take phase θ on cells, gauge connection A_μ on links, and information capacity ζ per cell as inputs. This project does not redo those derivations; it shows what supplies their inputs. The primitive's (*e*, *φ*) coarse-grain to (θ, A_μ); the cylinder's compact circumference is what makes the per-cell information capacity ζ finite — a precondition the GRID axioms required (see [grid/foundations.md](../../grid/foundations.md) §A5) but did not construct.

For charge emergence the relationship is different. [grid/charge-emergence.md](../../grid/charge-emergence.md) is candid that its account of the coupling magnitude is unfinished. Chapter 8 of this project takes another pass at the same question with the cylinder primitive in hand and may produce a tighter mechanism — in which case it supersedes charge-emergence.md rather than supplying its inputs.

## Notation

| Symbol | Role | Type |
|---|---|---|
| *e(x, t)* | Longitudinal stress magnitude at cross-section *x* | Real, signed (+ tension, − compression) |
| *φ(x, t)* | Azimuthal direction where stress is concentrated at cross-section *x* | Angle, periodic mod 2π |
| *K_ee, K_φφ* | Diagonal stiffnesses (longitudinal, azimuthal) — substrate-level coefficients | Real, positive |
| *K_eφ* | Off-diagonal shear coupling between *e* and *φ* | Real |
| ρ, *I_φ* | Diagonal substrate-level inertia coefficients — what *D*'s diagonal entries are. *Not* particle rest mass (which is a metric-mass-style emergent quantity, not present at this scale) | Real, positive |
| *D_eφ* | Off-diagonal substrate-level inertia (matched chirality counterpart of *K_eφ*) | Real |
| *χ̃* | Dimensionless chirality: χ̃ = K_eφ / √(K_ee K_φφ) = D_eφ / √(ρ I_φ) (matched chirality) | Real, ∈ (0, 1) |
| *L* | Cylinder length (one lattice spacing) | Length |
| *r* | Cylinder cross-section radius | Length |
| *τ* | Transit time across one cylinder: τ = *L*/*c* | Time |
| *N* | Discretization count when a sheet is wrapped into a torus | Integer |
| *c* | Lattice signal speed (one cell per tick, GRID axiom A1) | Speed |

A note on inertia at the substrate scale. The "inertia matrix" *D* is *not* arbitrary, and it is *not* a category-error analogy with particle rest mass. Under the fractal-microgrid interpretation (the cylinder primitive is itself a wrapped 2D microgrid), waves circulating around the cylinder cross-section have quantized transverse momentum (Kaluza-Klein style), and those modes manifest as substrate inertia for waves propagating along the cylinder's axis. The mechanism is **structurally identical** to the rest-mass story in [metric-mass](../metric-mass/) — both are momentum-on-compact-direction → mass-analog. They differ in scale (sub-Planck cross-section here vs Compton-scale compact dimension *u* in metric-mass) and in topology (1D circumference wrap here vs 1D compact dimension in metric-mass; both produce mass-analog only, not charge — charge requires the 2D-sheet-into-torus wrap of chapter 8). In MaSt terminology, the substrate inertia is a *dark-mass*-like contribution at the substrate level: real mass-analog from a compact wrap, but not directly observable at the lattice scale and not a particle. In GRID's natural units (*c* = ℏ = 1), the matched-chirality + bare-speed condition collapses *M* and *D* into a single matched-chirality matrix.

The earlier viz model ([viz/grid-lab/](../../viz/grid-lab.md)) treated edges and nodes as separate *lumped* primitives — one magnitude per edge, one periodic phase per node — connected by a discrete two-phase clock. The cylinder primitive folds both roles into a single *distributed* object: state varies continuously along the cylinder's length, and propagation is direct rather than mediated by a clock. The viz remains useful for building intuition about wave propagation, but is superseded by the cylinder for the foundational model.

## Ground rules

1. **Discovery, not proof.** Do mathematics that *yields* a result rather than asserts it. Where a result is already known from MaSt or GRID, the chapter arc should still let the math reveal it.

2. **The primitive is a hypothesis under test.** This project does not assume the cylinder primitive works. Each chapter checks one consequence; if a consequence fails, the project either pivots or rescopes.

3. **Stop at the cylinder.** The cylinder may be a fractal recursion of a finer grid, but infinite regression is fruitless. The cylinder's internal dynamics are described by a stiffness matrix with symbolic entries; we do not derive those entries from sub-cylinder geometry.

4. **Variables stay symbolic.** Don't pin numerical values until the algebra forces it. K_ee, K_φφ, K_eφ, L, r remain symbolic.

5. **One topic per chapter.** Bundling defeats the discovery arc.

6. **Computation only when forced.** Paper math first; scripts only where the algebra becomes intractable or visualization is the only way to see the geometry.

7. **2D and periodic from the start.** A working lattice must be at least 2D and periodic — open boundaries and 1D chains carry asymmetries the physical lattice doesn't have. Lower-dimensional toys are intuition aids, not derivation surfaces.

8. **The primitive is distributed, not lumped.** State (*e*, *φ*) varies continuously along the cylinder's length; a perturbation at one end takes transit time τ = *L*/*c* to reach the other. Nodes serve as continuity boundary conditions where adjacent endpoints meet — they hold no state and have no update rule. *Fallback:* if the distributed continuous-spring model proves intractable or fails the entropy check (chapter 4), the project pivots to a discrete phase-based primitive in the spirit of the viz model.

## Goals

### Theories to test

Claims to examine — derived where possible, stated explicitly when taken as input, falsified explicitly if the math doesn't support them.

1. **Two DoF suffice per edge.** A cylindrical primitive whose state at each cross-section is a 2D internal stress vector (with magnitude *e* and azimuthal direction *φ* as its two real components) is rich enough to carry both magnitude-type (E-like) and phase-type (B-like) information on a single edge. *[Chapter 2 — confirmed.]*

2. **Shear is necessary for *coupled* propagation.** With K_eφ = 0, strain and phase decouple and propagate as two unrelated independent waves. K_eφ > 0 is structurally required for the cylinder to be a coupled-wave medium where stretching and twisting drive each other (rather than two unrelated channels). *[Chapter 2 — confirmed.]*

3. **Stability bounds the shear.** Both *M* and *D* must be positive-definite for the energy to be bounded below, giving χ̃ ∈ (0, 1) strictly. Under matched chirality + bare-speed equality, both polarizations propagate at *c* throughout the stable range (the χ̃ = 1 boundary is where the matrices become singular together, but their proportionality *M* = *c*² *D* persists, so the wave speed does *not* collapse to zero — that "wave speed → 0" framing was a diagonal-*D* artifact and has been retired). The natural propagating regime is the open interval (0, 1). *[Chapter 2 — confirmed.]*

4. **A natural midpoint for the shear.** χ̃ = 1/√2 sits at the value where K_eφ² is at the arithmetic mean of 0 and the stability ceiling K_ee K_φφ — at this point the chiral coupling is well-engaged (well away from zero) and the stability margin is substantial (well below 1). This is a *natural midpoint argument*, not a derivation: nothing in chapter 2 alone forces χ̃ to take this value. (Earlier drafts used the labels "equipartition" and "geometric mean" for this point; both are incorrect — equipartition would equate kinetic and potential energy contributions, and the geometric mean of 0 and 1 is 0, not 1/√2. The arithmetic-mean characterization is what the math actually delivers.) *[Chapter 2 — confirmed as a natural midpoint, not as a derived value.]*

5. **Bidirectional propagation symmetry holds despite chirality.** Both *M* and *D* are real and symmetric, so the dispersion ω² depends on k only through k². L-going and R-going waves travel at the same speed; two pulses launched from opposite ends pass through each other and exit with their waveforms intact. *Negative result candidate:* if the algebra produces direction-dependent group velocity, the cylinder primitive is incompatible with vacuum Maxwell. *[Chapter 2 — confirmed; ω² depends on k² only.]*

6. **Matched chirality + bare-speed equality + lattice cadence pin the cylinder's ratios.** The cylinder primitive carries *two* postulates of equal status, both stated at the foundation level: (i) *matched chirality* (chapter 1 §8 — *K_eφ*/√(*K_ee K_φφ*) = *D_eφ*/√(ρ *I_φ*) = χ̃) and (ii) *bare-speed equality* (chapter 2 §4 / chapter 3 §2 — *K_ee*/ρ = *K_φφ*/*I_φ* ≡ *c*², the common bare propagation speed of the two diagonal channels, identified with the lattice signal speed). Together they yield *M* = *c*² *D*, and the cylinder propagates *both* polarizations at *c* (no slow-mode split, no birefringence). Drop either postulate and the two-speed split returns. The dimensionless stiffness ratios are pinned by *c* together with χ̃; an overall stiffness scale, cylinder length *L*, and cross-section radius *r* remain free. *[Chapters 2–3 — confirmed.]*

7. *[Chapter 4 — confirmed for scaling; coefficient deferred to chapter 7.]* **Linear-Gaussian fluctuations on the 2D lattice supply the entropic 1/r force scaling.** The cylinder primitive's stress vector field, at static equilibrium, satisfies the 2D Laplace equation (each component independently — the stiffness matrix *M* factors out at static). The 2D Laplacian Green's function is logarithmic, giving a 1/*r* force law as a generic consequence. At finite temperature, Gaussian fluctuations of the linear field produce a logarithmic *variance shadow* around any localized inclusion — a per-area entropy structure that satisfies the area-scaling requirement of Jacobson's argument. **The chapter-4 discovery is that this is the load-bearing mechanism**: where theory 7 originally hypothesized topological vortex defects (BKT-style) as the entropy source, the actual story turns out to be simpler — ordinary Gaussian fluctuations of the linear theory already produce the correct logarithmic Green's function structure that gives 1/*r* force scaling. Confirmed by three independent simulation tests in [scripts/](scripts/) (static field decay, thermal variance shadow, two-body force-vs-separation). The coefficient match to ζ = 1/4 requires careful normalization between the cylinder primitive's symbolic constants and the lattice geometry, deferred to the bridge chapter for [grid/gravity.md](../../grid/gravity.md). Topological defects remain in the picture as a possible refinement for the coefficient and as a structural element for the charge-emergence chapter (chapter 8) — but they are not the engine of the entropy account.

8. **The lattice of primitives establishes the common base for [grid/maxwell.md](../../grid/maxwell.md).** Coarse-graining the primitive's (*e*, *φ*) over the lattice yields the cell-phase θ and link gauge connection A_μ that maxwell.md takes as input. Maxwell's E and B emerge as the strain-channel and phase-channel components of the wave. The project does not re-derive Maxwell; it shows that maxwell.md's inputs are well-founded — and decides what role (if any) the slow mode plays at the lattice scale (a non-Maxwell excitation, a gapped/massive mode, or a real prediction of vacuum birefringence). *[Chapter 6 — pending.]*

9. **The lattice of primitives establishes the common base for [grid/gravity.md](../../grid/gravity.md), with the coefficient ζ = 1/4 matched.** Chapter 4 confirmed the 1/r force *scaling*; chapter 7 carries out the *coefficient* calculation, matching the cylinder primitive's continuum Green's-function coefficient against the per-cell information capacity ζ = 1/4 derived from cell geometry in [grid/foundations.md](../../grid/foundations.md) §A5. Jacobson's argument runs unchanged on top; the project does not re-derive G. *[Chapter 7 — pending.]*

10. **α as a kink-loss fraction of a wrapped sheet — candidate picture only, inconclusive at the *N* of interest.** When a 2D sheet of primitives is folded into a closed surface, its discretization N and effective shear χ̃ would jointly determine a fractional energy leak per wrap, *if* the leading-order kink-loss treatment were controlled. Chapter 8 attempts the polygonal-wrap formulation η_loop ≈ 4π² K(χ̃)/N and arrives at an inconclusive result: at *N* = 6 the natural perturbative parameter (Δθ)² = (π/3)² ≈ 1.10 is order unity, and the assumed incoherent-summation rule does not apply to a coherent closed loop. The leading-order formula is therefore a *placeholder*, not a controlled structural form. What chapter 8 *does* deliver is a sharper *target* for a follow-up calculation: matched-chirality kink-scattering plus coherent loop summation, with a concrete lattice-level kink model. Until that calculation is performed, the cylinder primitive does not establish a structural form for α and does not improve on [grid/charge-emergence.md](../../grid/charge-emergence.md)'s account of the α magnitude. *[Chapter 8 — inconclusive.]*

### Open questions

1. ~~Does the lattice signal speed *c* fix χ̃ uniquely, or does it leave one free length scale?~~ *[Resolved in chapter 3.]* The combination of *c*_+ = *c* and equipartition χ̃ = 1/√2 pins two ratios; an overall stiffness scale, *L*, and *r* remain free.

2. ~~**The slow-mode interpretation.**~~ *[Resolved in chapters 1 §8 / 2 / 3 via matched chirality.]* The slow-mode tension that appeared in earlier drafts (a propagating mode at *c*_− ≈ 0.414 *c* alongside the photon at *c*) was a consequence of an implicit diagonal-inertia simplification that broke the cylinder primitive's chiral self-consistency. With the inertia matrix *D* properly carrying the matched chiral cross-term *D_eφ* (matched in magnitude to the stiffness cross-term *K_eφ*), and with the bare-speed condition *K_ee*/ρ = *K_φφ*/*I_φ* = *c*², the matrices satisfy *M* = *c*² *D*, the eigenvalue degeneracy is exact, and both polarizations propagate at *c*. No slow mode at the single-primitive level, none at the lattice level (chapter 5).

3. **The coefficient ζ.** Chapter 4 confirmed the cylinder primitive's *scaling* matches Jacobson's requirement (linear-Gaussian fluctuations on the 2D lattice → 1/r force law). Whether the *coefficient* in *S* = ζ · *A* matches GRID's geometrically-derived ζ = 1/4 exactly, or requires refinements (topological-defect contributions, lattice geometry corrections), is the substantive task of chapter 7.

4. **Two wraps, one project.** What is the precise relationship between the two distinct "wraps" the dialog uses — wraps of the *cylinder cross-section* (small scale, primitive-internal) and wraps of a *2D sheet of primitives* (MaSt scale, where charge lives per [grid/charge-emergence.md](../../grid/charge-emergence.md))? Chapter 8 has to settle this, since the α-kink-loss derivation lives at the sheet-wrap scale but borrows machinery from the cylinder cross-section.

5. **Tube thickness.** Does the cylinder primitive admit a "tube thickness" derivation from optimal shear? The dialog raises this; whether it produces a meaningful constraint is unclear. Possible chapter-8 question.

6. **sim-impedance constraints on chapter 8.** [grid/sim-impedance/](../../grid/sim-impedance/) (Tracks 1–12) systematically tested whether α could be derived from junction geometry alone and concluded it could not. The project does not claim to predict α's *value*, but if chapter 8's kink-loss derivation constrains α to a discrete menu, sim-impedance's enumeration becomes directly relevant — and worth re-examining for what it actually rules out.

7. **Non-precise shear.** If χ̃ ≠ 1/√2 (say, due to a future constraint from chapter 5/6/7 that pins it elsewhere), the strain and azimuthal channels would carry unequal shares of the wave content. That asymmetry could land somewhere observable — possibly in the relative roles of B and H. Open whether this is a real consequence or a calculation artifact.

## Background

### What was tried before

- The earlier viz model treated edges and nodes as serially-arranged separate primitives, with a discrete two-phase clock alternating updates. That model is preserved in [viz/grid-lab/](../../viz/grid-lab.md) and remains useful for propagation intuition. It is *not* the foundational model for this project — the cylinder collapses both roles into a single object.

- [grid/sim-gravity/](../../grid/sim-gravity/) tried a spring lattice and got the elastic 1/r² strain field — the wrong power law for gravity. The cause was that the field at each lattice site was a *vector* displacement satisfying the Navier (elastic) equation rather than a scalar one satisfying the Laplace equation; the elastic Navier Green's function falls off as 1/r² in 2D, while the Laplacian Green's function falls off as log(r) (giving 1/r force). [grid/sim-gravity-2/](../../grid/sim-gravity-2/) succeeded by adding a tower of standing-wave modes (n = 1, 2, …) on the ℵ-line as the entropy reservoir. **The cylinder primitive's static behavior is, surprisingly, just like a 2D scalar Laplacian** — the stiffness matrix *M* factors out of the static equation, leaving each component to satisfy ∇²ψ = 0 independently. This is what saves it from sim-gravity's elastic failure. Chapter 4 establishes this connection in detail; three simulations in [scripts/](scripts/) confirm the prediction.

- [grid/sim-impedance/](../../grid/sim-impedance/) (Tracks 1–12) systematically tested whether α could be derived from junction geometry alone and concluded that it could not. The framing here is more guarded — the project takes another pass at *understanding* α, not deriving its value, and reads sim-impedance's enumeration as a constraint on the menu rather than a closed verdict.

- [grid/charge-emergence.md](../../grid/charge-emergence.md) frames charge as CP-synchronized leakage from a bent sheet but is candid that the magnitude of the coupling cannot be derived from junction geometry alone. Chapter 8 of this project takes another pass at the same question with the cylinder primitive in hand. If the kink-loss mechanism produces a clean derivation of η_loop with explicit χ-dependence, charge-emergence.md becomes back-reference rather than primary source.

### What this project is not trying to do

- Not deriving the *value* of α. A range of (χ, N) hits 1/137; selecting which one nature chose is outside scope.
- Not modeling real carbon nanotubes. The cylinder is a pictorial primitive whose stiffness matrix has symbolic entries; nanotube-specific physics is not used.
- Not replacing GRID's axioms. The primitive must be consistent with axioms A1–A6 of [grid/foundations.md](../../grid/foundations.md); it is a *layer* under those axioms, not a substitute for them.
- Not re-deriving Maxwell or Jacobson gravity. [grid/maxwell.md](../../grid/maxwell.md) and [grid/gravity.md](../../grid/gravity.md) remain authoritative; this project supplies their inputs.
- Not treating [grid/charge-emergence.md](../../grid/charge-emergence.md) as authoritative. That document is the previous, less-rigorous attempt at this question; chapter 8 of this project may revise or replace its conclusions.
- Not committing to the fractal recursion of cylinder-walls-as-grids. Acknowledged as possible, not pursued.
- Not doing 1D. Lower-dimensional toys are intuition aids, but no foundational claim rests on a 1D lattice.

## Background reading

- [`dialogs/grid-3.md`](../../dialogs/grid-3.md) — the brainstorming dialog from which the cylinder primitive emerged. The chiral-tube and shear discussions (lines 2050–3990) are the most directly relevant.
- [primers/alpha-in-grid.md](../../primers/alpha-in-grid.md) — α in the GRID picture; the project takes this framing as input.
- [grid/foundations.md](../../grid/foundations.md) — axioms the primitive must respect.
- [grid/charge-emergence.md](../../grid/charge-emergence.md) — previous attempt at charge emergence at the MaSt-scale wrap; chapter 8 of this project may supersede it.
- [grid/maxwell.md](../../grid/maxwell.md) — Maxwell-from-the-lattice derivation. This project supplies its inputs (θ, A_μ); does not re-derive.
- [grid/gravity.md](../../grid/gravity.md) — Jacobson derivation of G. This project supplies its input (ζ); does not re-derive.
- [grid/sim-gravity-2/README.md](../../grid/sim-gravity-2/README.md) — the working entropic-1/r model whose entropy mechanism this project must match (or replace).
- [viz/grid-lab.md](../../viz/grid-lab.md) — superseded discrete-clock primitive, retained for propagation intuition.

## Chapters

The arc below is a *sketch*. Early chapters are framed in detail; later chapters are framed as questions to examine. The project may redirect when a chapter's math reveals something unexpected.

1. **`01-foundation.md`** — Axioms and givens. The cylinder primitive as a *distributed* 1D object with strain field *e(x, t)* and azimuthal phase field *φ(x, t)* along its length, the stiffness matrix, the role of nodes as passive continuity-boundary junctions, and the relationship to the earlier discrete-clock viz model. State explicitly what is taken as input from GRID and what the project will derive.

2. **`02-wave-on-a-primitive.md`** — Solve the dynamics on a single primitive. Derive the dispersion relation from the stiffness matrix, identify the propagating modes, locate the stability boundary at K_eφ² = K_ee K_φφ, show why χ̃ = 1/√2 is the equipartition point, and *prove bidirectional propagation symmetry* — that L-going and R-going waves travel at equal speeds despite the chiral shear, and that two opposing pulses pass through each other intact. (Theory 5 is the falsifiability check.)

3. **`03-shear-and-c.md`** — Impose the lattice signal speed *c* on the cylinder's internal wave dynamics. Determine whether matching cylinder transit time τ = *L*/*c* against the lattice cadence fixes χ̃ uniquely (and which length scale stays free) or admits a family. Settles open question 1.

4. **`04-entropy-from-defects.md`** — *The Entropy Account.* Establishes that the cylinder primitive on a 2D lattice produces the entropic 1/r force scaling required for Jacobson's gravity. The chapter's discovery: where topological vortex defects were originally hypothesized as the entropy mechanism, the actual story is simpler — the linear theory's Gaussian fluctuations of the stress vector field already produce the logarithmic Laplacian Green's function structure (and hence 1/*r* force scaling) on their own. Confirmed by three independent simulation tests in [scripts/](scripts/). The coefficient match to ζ = 1/4 is a downstream calculation; topological defects survive as a possible refinement for the coefficient and as structural input for chapter 8.

### Remaining chapters

The chapters below are still in roadmap form — the questions are framed but the chapters are not yet drafted.

5. **`05-the-2d-lattice.md`** — Assemble cylinder primitives into a 2D *hexagonal* lattice (per [grid/hexagonal.md](../../grid/hexagonal.md), giving ζ_2D = 1/3) with wye-junction node continuity. Derive the wave equation in 2D and confirm that the matched-chirality structure of chapter 1 §8 produces a clean photon at *c* with two polarizations and no anomalies at the lattice scale. (An earlier draft of this chapter had to address a slow-mode tension; that tension was resolved at the foundation level by adopting matched chirality.)

6. **`06-base-for-maxwell.md`** — Bridge to [grid/maxwell.md](../../grid/maxwell.md). Show that coarse-graining the primitive's (*e*, *φ*) over the lattice yields the cell-phase θ and link connection A_μ that maxwell.md takes as input. Identify which field components live in strain and which in azimuthal direction, and how the shear coupling produces the curl relations. Decide what role (if any) the slow mode plays at the lattice scale: a non-Maxwell excitation (matter-like? non-radiative?), a gapped mode that doesn't propagate at long wavelengths, or a feature visible in vacuum birefringence experiments. Cite maxwell.md to run from there.

7. **`07-base-for-gravity.md`** — Bridge to [grid/gravity.md](../../grid/gravity.md), with the **coefficient calculation** as the substantive content. Chapter 4 settled the entropic 1/r *scaling*; this chapter computes the actual coefficient on the per-cell information capacity ζ from the cylinder primitive's continuum Green's function, normalizes the lattice geometry, and matches to ζ = 1/4 from [grid/foundations.md](../../grid/foundations.md) §A5. If the coefficient comes out cleanly, theory 9 lands. If there is a residual discrepancy, this is where topological-defect refinements (chapter 4 §9) get pulled back in. Cite gravity.md to run from there.

8. **`08-wrap-and-alpha.md`** — Fold a 2D sheet of primitives into a torus and examine two candidate mechanisms for the leakage:
   - **Discrete-kink picture:** η_joint = K(χ)(Δθ)², η_loop = 4π² K(χ)/N
   - **Continuous-bend picture:** inner-compression / outer-tension on the cylinder wall, energy concentration, leak rate per radian

   Compare the two, derive the functional form of α as a geometric ratio, identify the (χ, N) menu that admits 1/137, and decide whether any natural selection principle picks a value inside the menu. Make explicit what is and is not predicted. If solid, this chapter becomes a more authoritative account of charge emergence than [grid/charge-emergence.md](../../grid/charge-emergence.md).

9. **`09-closing-summary.md`** — Consolidate what the project established, ruled out, and unexpectedly found. Hand off to follow-up projects.

Each chapter is added one at a time. The arc is a sketch, not a contract.
