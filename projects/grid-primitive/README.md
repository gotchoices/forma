# grid-primitive

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** A mathematical model of the GRID lattice's primitive — the smallest unit at which edges, nodes, and ultimately the lattice itself are modeled.
**Method:** Mathematical derivation as discovery; visualization where it sharpens intuition; minimal computation.
**Status:** Framing complete. Awaiting first chapter.

## Why this project exists

The GRID framework derives Maxwell's equations, Einstein's field equations, charge quantization, and entropic gravity from a 4D causal lattice with cell-level phase, gauge connection, and an information-resolution parameter ζ (see [grid/foundations.md](../../grid/foundations.md)). Those derivations treat the lattice as a whole — they do not commit to what an *individual primitive* is, only that there are edges and nodes whose collective behavior produces the observed physics.

This project takes up the primitive itself. The central question:

> *What is the simplest mathematical object that, assembled into a 2D periodic lattice, supplies the common base from which Maxwell's equations and the entropic-gravity story already established at the lattice scale remain derivable — and where, in that object, does α appear?*

The dialog [`dialogs/grid-3.md`](../../dialogs/grid-3.md) brainstormed several candidate primitives and converged on a particular one: a **2D cylindrical tube** with two coupled internal degrees of freedom — longitudinal strain and azimuthal phase. This project develops that primitive in production form: checking that it works, where it doesn't, and what it implies for charge, mass, and gravity.

## The primitive

The grid is built from edges and nodes, arranged on a 2D sheet (for compact dimensions or MaSt sheets) or a 3D extent (for the spatial lattice S). Each edge is modeled as a small **2D cylindrical tube** — nanotube-like in structure, but with no commitment to atomic-scale carbon-nanotube physics.

The cylinder is a **distributed** primitive: it has length *L*, and the state — longitudinal strain *e(x, t)* and azimuthal phase *φ(x, t)* — varies along the cylinder's length *x* ∈ [0, *L*]. A perturbation at one end takes transit time τ = *L*/*c* to reach the other. A wall-shear coupling *K_eφ* between strain and phase makes the two fields drive each other along the cylinder, which is what allows the edge to carry a propagating wave.

Mechanical intuition: a rubber cylinder with fibrous shear in the wall, glued to its neighbors at the endpoints. Under tension it stretches; under torque it twists; the fibers couple stretching and twisting so that a perturbation at one end propagates as a coupled stretch-and-twist along the cylinder, emerging at the far end as a perturbation in (*e*, *φ*) for the next cylinder to receive.

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
| *e(x, t)* | Longitudinal strain field along cylinder, *x* ∈ [0, *L*] | Real, signed |
| *φ(x, t)* | Azimuthal phase field along cylinder, *x* ∈ [0, *L*] | Compact: φ ∈ [0, 2π) |
| *K_ee, K_φφ* | Diagonal stiffnesses (longitudinal, azimuthal) | Real, positive |
| *K_eφ* | Off-diagonal shear coupling between *e* and *φ* | Real |
| *χ̃* | Dimensionless shear ratio: χ̃ = K_eφ / √(K_ee K_φφ) | Real, ∈ (0, 1) |
| *L* | Cylinder length (one lattice spacing) | Length |
| *r* | Cylinder cross-section radius | Length |
| *τ* | Transit time across one cylinder: τ = *L*/*c* | Time |
| *N* | Discretization count when a sheet is wrapped into a torus | Integer |
| *c* | Lattice signal speed (one cell per tick, GRID axiom A1) | Speed |

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

1. **Two DoF suffice per edge.** A cylindrical primitive with longitudinal strain field *e(x, t)* and azimuthal phase field *φ(x, t)* — distributed along the cylinder's length — is rich enough to carry both magnitude-type (E-like) and phase-type (B-like) information on a single edge.

2. **Shear is necessary for propagation.** With K_eφ = 0, strain and phase decouple and the cylinder supports no propagating waves. K_eφ > 0 is structurally required.

3. **Stability bounds the shear.** The stiffness matrix must remain positive-definite, giving K_eφ² < K_ee · K_φφ. The upper limit χ̃ = 1 is degenerate (wave speed → 0); the natural propagating regime sits strictly inside (0, 1).

4. **Equipartition picks the natural shear.** Equal energy in strain and phase channels gives χ̃ = 1/√2 as the geometrically natural value — the geometric mean inside the stable range, where the two fields carry equal share of the wave's content.

5. **Bidirectional propagation symmetry holds despite shear.** Although shear makes the cylinder chiral and creates a handedness distinction in the *mode basis* (L-circular vs R-circular polarization), it does *not* create directional asymmetry in *propagation*: L-going and R-going waves travel at the same speed, and two pulses launched from opposite ends pass through each other and exit with their waveforms intact. *Negative result candidate:* if the algebra produces direction-dependent group velocity, the cylinder primitive is incompatible with vacuum Maxwell.

6. **The lattice signal speed *c* emerges from the cylinder's internal dynamics.** In the distributed picture, a perturbation traverses one cylinder in transit time τ = *L*/*c*. The internal wave speed is set by the stiffness scales, the cross-section radius *r*, the length *L*, and the shear χ̃. Imposing this speed = c is a real algebraic constraint (not a tautology) that relates the primitive's geometry to the lattice cadence. *Open question:* does this constraint pin χ̃ uniquely (leaving a length scale free), pin a length given χ̃ = 1/√2, or admit a one-parameter family?

7. **Cylinder circumference is the entropy reservoir.** Rotations around the 2π cross-section play, on the cylinder primitive, the role that the bounded periodic phase played at a node in the earlier viz model: a compact periodic variable whose wraps lose information. *This is a load-bearing bet, and it specifically distinguishes this model from [grid/sim-gravity/](../../grid/sim-gravity/)'s failed spring lattice.* That earlier attempt failed because every degree of freedom was R-valued (unbounded position vector) — the lattice produced the elastic 1/r² strain field rather than the entropic 1/r force. Here, although strain *e* is similarly unbounded, the azimuthal phase *φ* is compact (∈ [0, 2π)), so wraps lose information by construction. The hope is that this single-bounded-DoF distinction supplies what springs alone could not. If circumference rotations cannot supply the entropy that [grid/sim-gravity-2/](../../grid/sim-gravity-2/) sourced from a tower of ℵ-line modes, the project must pivot the entropy mechanism or fall back to a discrete primitive. Chapter 4 is the fail-fast check.

8. **The lattice of primitives establishes the common base for [grid/maxwell.md](../../grid/maxwell.md).** Coarse-graining the primitive's (*e*, *φ*) over the lattice yields the cell-phase θ and link gauge connection A_μ that maxwell.md takes as input. Maxwell's E and B emerge as the strain-channel and phase-channel components of the wave, with the staggering across coupled edges playing the role of Yee's E/H staggering. The project does not re-derive Maxwell; it shows that maxwell.md's inputs are well-founded.

9. **The cylinder's circumference establishes the common base for [grid/gravity.md](../../grid/gravity.md).** With the entropy from §7 in hand, the per-cell information capacity ζ that gravity.md requires for Jacobson's argument is supplied by the primitive itself. Jacobson's argument runs unchanged on top; the project does not re-derive G.

10. **α is the kink-loss fraction of a wrapped sheet — and this is the project's centerpiece.** When a 2D sheet of primitives is folded into a torus, its discretization N and effective shear χ jointly determine a fractional energy leak per wrap. Two candidate mechanisms are in scope: a *discrete-kink* picture giving η_loop = 4π² K(χ)/N, and a *continuous-bend* picture in which inner-compression / outer-tension on the cylinder wall produces a per-radian leak rate. The deliverable: derive the functional form of α as a geometric ratio, identify the (χ, N) menu that admits 1/137, and decide whether any natural selection principle picks a value inside the menu. The *value* α ≈ 1/137 is not predicted, but the *form* of α as a function of primitive geometry is. If this chapter lands, it becomes a more authoritative explanation of charge emergence than [grid/charge-emergence.md](../../grid/charge-emergence.md), which is candid that its current account is hand-wavey on the magnitude.

### Open questions

1. Does the lattice signal speed *c* fix χ̃ uniquely, or does it leave one free length scale (*L* or *r*)? (Theory 6.)

2. Can rotations around the 2π circumference supply the entropy that sim-gravity-2 sourced from a ℵ-line mode tower? (Theory 7 — early-validation candidate, gating chapter 4.)

3. What is the precise relationship between the two distinct "wraps" the dialog uses — wraps of the *cylinder cross-section* (small scale, primitive-internal) and wraps of a *2D sheet of primitives* (MaSt scale, where charge lives per [grid/charge-emergence.md](../../grid/charge-emergence.md))?

4. Does the cylinder primitive admit a "tube thickness" derivation from optimal shear? The dialog raises this; whether it produces a meaningful constraint is unclear.

5. Where does [grid/sim-impedance/](../../grid/sim-impedance/)'s negative result (α not derivable from junction geometry alone) constrain this project? The project does not claim to predict α, but if the primitive constrains α to a discrete menu, sim-impedance's enumeration becomes directly relevant — and worth re-examining for what it actually rules out.

6. The non-precise shear χ̃ ≠ 1/√2 may imply that the strain and phase channels carry unequal shares of the wave content. If so, that asymmetry would land somewhere observable — possibly in the relative roles of B and H. Open whether this is a real consequence or a calculation artifact.

## Background

### What was tried before

- The earlier viz model treated edges and nodes as serially-arranged separate primitives, with a discrete two-phase clock alternating updates. That model is preserved in [viz/grid-lab/](../../viz/grid-lab.md) and remains useful for propagation intuition. It is *not* the foundational model for this project — the cylinder collapses both roles into a single object.

- [grid/sim-gravity/](../../grid/sim-gravity/) tried a spring lattice and got the elastic 1/r² strain field — the wrong power law for gravity. The cause was that all degrees of freedom were R-valued (unbounded position vectors); without a compact periodic variable, the lattice had no information loss to source entropy from. [grid/sim-gravity-2/](../../grid/sim-gravity-2/) succeeded by adding a tower of standing-wave modes (n = 1, 2, …) on the ℵ-line as the entropy reservoir. The cylinder primitive does not carry such a tower; instead, theory 7 is the bet that 2π-circumference rotations of the bounded *φ* — the structural difference between this primitive's "spring model" and sim-gravity's — supply the entropy in a different way. Chapter 4 is the explicit check, and a negative result triggers fallback to a discrete phase-based primitive (ground rule 8).

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

### Tentative downstream arc

The chapters below are plausible follow-ups, not commitments.

4. **`04-circumference-as-entropy.md`** — The fail-fast validation. Examine whether 2π-circumference rotations on the cylinder supply the entropy that sim-gravity-2 sourced from a ℵ-line mode tower — i.e., whether the bounded azimuthal phase *φ* alone (in contrast to sim-gravity's all-unbounded springs) is enough. A negative result here triggers the fallback in ground rule 8 (pivot to a discrete phase-based primitive) before further chapters; a positive result clears the path to chapters 7–8.

5. **`05-the-2d-lattice.md`** — Assemble primitives into a 2D periodic lattice. Establish the boundary-free discipline, the staggering of strain and phase across coupled edges, and the relationship to Yee's E/H staggering.

6. **`06-base-for-maxwell.md`** — Bridge to [grid/maxwell.md](../../grid/maxwell.md). Show that coarse-graining the primitive's (*e*, *φ*) over the lattice yields the cell-phase θ and link connection A_μ that maxwell.md takes as input. Identify which field components live in strain and which in phase, and how the shear coupling produces the curl relations. Cite maxwell.md to run from there. Short bridge — the project's contribution is the projection, not Maxwell itself.

7. **`07-base-for-gravity.md`** — Bridge to [grid/gravity.md](../../grid/gravity.md). Show that the entropy density derived in chapter 4 supplies the per-cell information capacity ζ that gravity.md requires for Jacobson's argument. Cite gravity.md to run from there. Short bridge — the project's contribution is the entropy reservoir, not the Jacobson derivation.

8. **`08-wrap-and-alpha.md`** — The project's centerpiece. Fold a 2D sheet of primitives into a torus and examine two candidate mechanisms for the leakage:
   - **Discrete-kink picture:** η_joint = K(χ)(Δθ)², η_loop = 4π² K(χ)/N
   - **Continuous-bend picture:** inner-compression / outer-tension on the cylinder wall, energy concentration, leak rate per radian

   Compare the two, derive the functional form of α as a geometric ratio, identify the (χ, N) menu that admits 1/137, and decide whether any natural selection principle picks a value inside the menu. Make explicit what is and is not predicted. If solid, this chapter becomes a more authoritative account of charge emergence than [grid/charge-emergence.md](../../grid/charge-emergence.md).

9. **`09-closing-summary.md`** — Consolidate what the project established, ruled out, and unexpectedly found. Hand off to follow-up projects.

Each chapter is added one at a time. The arc is a sketch, not a contract.
