# grid-couplet

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** A digital-first model of the GRID lattice. Sibling to [grid-primitive](../grid-primitive/), which works the same questions analog-first.
**Method:** Mathematical derivation as discovery; visualization in [viz/grid-lab](../../viz/grid-lab.md) where it sharpens intuition; minimal computation.
**Status:** Framing complete. Awaiting first chapter.

## Why this project exists

[grid-primitive](../grid-primitive/) collapsed the GRID lattice's internal structure into a single distributed object — a *cylinder primitive* carrying both magnitude and phase on one continuous body. That model is *analog-first*: continuous, mechanical, with state varying along a 1D extent and propagation by direct elasticity.

grid-couplet takes the opposite stance — *digital-first*. The lattice is built from explicit structural types whose dynamics are governed by a discrete two-phase clock. The earlier viz [viz/grid-lab](../../viz/grid-lab.md) implements those dynamics; this project supplies the analytic theorems on top.

Where grid-primitive's success at the cylinder level invited the question of what's beneath, this project answers from a different angle: the cylinder's continuous behavior is what one sees when a digital structure of points, edges, and emergent dials is coarse-grained.

The central question:

> *What structural properties emerge when couplet chains close into dials, and at which level of a wrap-promotion ladder (raw → light → mass → charge) does each known phenomenon appear?*

[`01-foundation.md`](01-foundation.md) defines the model — point, edge, couplet, dial, master clock, update rule, junction, the macro "node = dial" convention, and the wrap-promotion ladder. [`02-closure-and-bounding.md`](02-closure-and-bounding.md) derives the entropic-bounding closure mechanism that converts an open couplet chain's continuous magnitude into a dial's bounded phase plus a discrete winding number.

## Layer relationship

```
MaSt (particles, masses, charges)
   ↑
GRID lattice (Maxwell, gravity, charge-emergence, ζ)
   ↑
grid-couplet (this project)        ← parallel to grid-primitive
```

Same layer as grid-primitive, different model. grid-primitive's analog-first cylinder primitive has physical dimensions: its length L sets the lattice signal speed c via the cylinder's transit time τ = L/c, so the model has a metric scale built in. grid-couplet's digital-first model treats edge length as logical, not topological — edges are graph-edges (connectivity plus stored state), and propagation speed is set by the clock cadence (one couplet per cycle). The two models converge structurally — grid-primitive's distributed cylinder is what one obtains, under coarse-graining, by closing grid-couplet's couplet chains into dials — but they handle scale differently, and grid-couplet correspondingly does not require any sub-scale recursion below its primitives.

If the project lands cleanly, a natural outgrowth is to extend grid-lab so it can render 2D dial sheets wrapped as tori (matching the chapter-7 setup).

## Ground rules

1. **Discovery, not proof.** Mathematics that *yields* results, not asserts them. Where a result is already known, the chapter arc should still let the math reveal it.

2. **No required sub-scale.** Points are 0D, edges are 1D — these are the model's structural primitives. Edge length is logical, not topological; nothing inside points or edges is required by the model. The thickness question that arises in chapter 7's α discussion is a separate modeling decision about whether wraps fold across emergent extent, not a question about opening any sub-scale recursion.

3. **Variables stay symbolic.** Don't pin numerical values until the algebra forces it.

4. **One topic per chapter.**

5. **Computation only when forced.** Paper math first. Use [viz/grid-lab](../../viz/grid-lab.md) where visualization is the only way to see the geometry.

6. **2D and periodic for foundational claims.** 1D constructions are intuition aids; theorems must hold in 2D periodic settings to be load-bearing.

7. **Closures are calculable.** The entropic-bounding argument that distinguishes open chains from closed loops is *derivable*, not posited. Chapter 2 carries it out.

## Goals

### Theories to test

Claims to examine — derived where possible, stated explicitly when taken as input, and falsified explicitly if the math doesn't support them.

1. **The digital model is dynamically equivalent to grid-primitive's cylinder.** A 1D periodic couplet chain reproduces grid-primitive chapter-2 wave dynamics in coarse-grained form: same dispersion, same bidirectional propagation symmetry, same stability bounds.

2. **Entropic-bounding produces the dial.** A closed 2π loop of N couplets, viewed externally, presents a bounded phase plus a discrete winding-number label. The closure operation discards the cumulative continuous magnitude that an open chain carries, mapping it to an integer winding sector.

3. **The asymmetry is one-directional.** Open chains can be closed into dials; dials cannot produce continuous unbounded magnitudes from their bounded state alone. This is the entropy of bounding made structural.

4. **The dial is the natural lattice node.** In a 2D hex tiling, each lattice vertex is a 2D dial whose connection multiplicity matches the lattice coordination (3 in hex), per [grid/hexagonal.md](../../grid/hexagonal.md), giving ζ_2D = 1/3.

5. **The junction is a clock-rectified coupling.** The edge-node interface transmits in alternating directions on alternating clock phases — a bidirectional rectifier whose direction toggles with the clock. Whether the diode analogy extends to forward thresholds, breakdown, and leakage is open.

6. **The promotion ladder.** Each successive wrap promotes information one level: raw → light (open chain → directional traveling perturbation) → mass-analog (1D wrap → emergent dial) → charge (2D dial sheet → torus, per [grid/charge-emergence.md](../../grid/charge-emergence.md)). Each level may admit a leakage analog; whether it does is examined per level.

7. **α is a second-order-wrap phenomenon.** α-type coupling emerges only when a wrap operation folds across a dimension that already has extent. The L2 wrap (open chain → 1D dial) folds across a 0D point — no extent to fold across, no α. The L3 wrap (2D dial sheet → torus) folds across the dial's 1D extent inherited from L2 — and that is where α enters. The *fact* of folding-across-extent matters; the *amount* of extent (the torus's minor radius) does not, consistent with grid-primitive chapter 8's α coming from a structural ratio rather than from a length scale.

8. **Bridge to grid/.** The convention "edge holds magnitude, node holds value" maps to [grid/fields.md](../../grid/fields.md)'s "E on edges, B at junctions." A subsidiary check: [grid/](../../grid/) appears to use cell phases as primary observables and to compute edges as differences. The bridge confirms or refines this mapping.

### Open questions

1. **Couplet exact-tiling.** Whether the couplet admits exact tiling of a 2D hex sheet, with no orphans, when built by recursive 120°/240° splits and wrapped periodically. May be answerable from existing hex-tiling combinatorics; the minimal-torus routine in viz is a starting point.

2. **Where in the ladder does α appear?** Same α at every level, distinct α's at different levels, or α only at L3? Conditional on theory 7's thickness question.

3. **Diode analogy extent.** Is the bidirectional rectification at the junction literal, suggestive, or both?

4. **Dial connection multiplicity beyond the lattice coordination.** The project default is N matching the lattice coordination number. Whether finer dials (larger N) admit additional leakage analogs at L2 is open.

5. **Phase-first vs. edge-first conventions in grid/.** Where does the choice of primary variable matter, and where is it just bookkeeping?

6. **3D extension.** All chapters work in 1D and 2D. Whether a 3D extension preserves the dial structure, or requires a richer object, is left open.

## Background

### What was tried before

- [viz/grid-lab.md](../../viz/grid-lab.md) — the existing implementation. Its v2 (Yee-style additive) update rule is the dynamics this project uses; the earlier v1 phase-replacement variant is dropped as memory-less and structurally inconsistent.

- [grid-primitive](../grid-primitive/) — the analog-first sibling. Established (chapters 1–4 confirmed) Maxwell-readiness and entropic-1/r-scaling for a single distributed cylinder primitive. Chapter-8's α derivation at hex symmetry is the quantitative reference for grid-couplet's L2 thickness question.

- [grid/charge-emergence.md](../../grid/charge-emergence.md) — establishes the L3 wrap (2D hex sheet → torus) producing charge with α as the per-junction coupling magnitude. This project does not re-derive it.

- [grid/sim-impedance/](../../grid/sim-impedance/) (Tracks 1–12) — concluded α cannot be derived from junction geometry alone. Theory 7 is consistent with that conclusion: it asks where α-type phenomena *appear* in the ladder, not what value they take.

### What this project is not trying to do

- **Not re-implementing grid-lab.** The implementation exists; this project supplies analytic theorems on top.
- **Not deriving the value of α.** Theory 7 asks where α-type phenomena appear in the ladder, not what value they take.
- **Not opening the fractal recursion.** Per ground rule 2.
- **Not re-deriving Maxwell, gravity, or charge emergence.** [grid/maxwell.md](../../grid/maxwell.md), [grid/gravity.md](../../grid/gravity.md), and [grid/charge-emergence.md](../../grid/charge-emergence.md) remain authoritative.

## Background reading

- [viz/grid-lab.md](../../viz/grid-lab.md) — model specification and update rule
- [grid-primitive/README.md](../grid-primitive/README.md) — analog-first sibling project
- [grid-primitive/08-wrap-and-alpha.md](../grid-primitive/08-wrap-and-alpha.md) — quantitative reference for the L2 thickness question
- [grid/charge-emergence.md](../../grid/charge-emergence.md) — L3 wrap, taken as input
- [grid/foundations.md](../../grid/foundations.md) — GRID axioms
- [grid/lattice-geometry.md](../../grid/lattice-geometry.md), [grid/hexagonal.md](../../grid/hexagonal.md) — hex lattice geometry
- [grid/fields.md](../../grid/fields.md) — E-on-edges / B-at-junctions convention used in the bridge

## Chapters

The arc is a sketch. Early chapters are framed in detail; later chapters as questions. The project may redirect when a chapter reveals something unexpected.

1. **`01-foundation.md`** — Define the model and its conventions: point, edge, couplet, dial, junction, master clock, update rule, the macro "node = dial" convention, the promotion ladder, posits, and discovery targets.

2. **`02-closure-and-bounding.md`** — *The closure derivation.* Show how an open 1D couplet chain carries continuous unbounded magnitude as an emergent edge, and how closing it into a 2π loop maps that magnitude into a discrete winding sector while leaving a bounded phase pattern — the emergent dial. Derive the information-capacity asymmetry. Establish that the asymmetry is one-directional.

3. **`03-the-junction-as-diode.md`** — Examine the edge-node interface as the model's coupling object. Test the bidirectional-diode framing: clock-rectified information flow, analogs of forward conduction, reverse blocking, breakdown, and leakage.

4. **`04-couplet-tiling.md`** — Whether the couplet admits exact tiling of a 2D hex sheet when built by recursive 120°/240° splits and wrapped periodically.

5. **`05-the-1d-array.md`** — Wave dynamics on a 1D periodic couplet chain. Recover the dispersion and bidirectional propagation symmetry of grid-primitive chapter 2 in digital form. Confirm equivalence under coarse-graining.

6. **`06-the-2d-sheet.md`** — 2D hex sheet of couplets. Derive the 2D wave equation, confirm hexagonal structure, recover ζ_2D = 1/3. Show how E and B fields emerge — bridging to [grid/fields.md](../../grid/fields.md).

7. **`07-promotion-ladder.md`** — Formalize the L0 → L1 → L2 → L3 ladder. Examine each level's wrap, what emerges, and whether a leakage analog exists. The α question (theory 7) is the central content.

8. **`08-bridge-to-grid.md`** — Bridge to [grid/](../../grid/). Map node values and edge magnitudes to the cell phases θ and link connections A_μ used in grid/'s derivations.

9. **`09-closing-summary.md`** — Consolidate established results, ruled-out items, and unexpected findings. Compare with grid-primitive.

Each chapter is added one at a time. The arc is a sketch, not a contract.
