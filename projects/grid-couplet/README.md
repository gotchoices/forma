# grid-couplet

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** A digital-first model of the GRID lattice using two distinct primitives (edge and node) connected by a two-phase master clock. Tests structural questions that grid-primitive's analog-first cylinder model did not address: edge/node primacy, exact tiling by couplets, and where in a wrap-promotion ladder each known phenomenon (light, mass, charge, α, leakage) appears.
**Method:** Mathematical derivation as discovery; visualization in [viz/grid-lab](../../viz/grid-lab.md) where it sharpens intuition; minimal computation.
**Status:** Framing complete. Awaiting first chapter.

## Why this project exists

[grid-primitive](../grid-primitive/) collapsed edges and nodes into a single distributed *cylinder* — one primitive carrying both linear (magnitude) and circular (phase) state. That model is analog-first: continuous, mechanical, with state varying along a 1D extent and propagation by direct elasticity. It produced a working derivation of Maxwell-readiness and entropic-gravity scaling.

But success at the cylinder level invited a question grid-primitive set aside (ground rule 3, "stop at the cylinder"): what if the continuous mechanical behavior is itself a coarse-grained description of *discrete* digital activity at a finer scale? grid-primitive deliberately did not open that door. This project does — in a constrained way.

The earlier visualization [viz/grid-lab.md](../../viz/grid-lab.md) already implements a digital-first model: edges and nodes as separate primitives, a two-phase master clock alternating their updates (Yee-staggered), and explicit update rules (v1 phase-replacement and v2 additive). What grid-lab cannot prove on its own are the **theorems** about that model's structure — whether edges and nodes are dual or asymmetric, whether the (edge, node) couplet tiles a 2D sheet exactly, what the edge-node junction *is* as a coupling object, and where α and leakage sit in a hierarchy of wraps. This project supplies those theorems.

The central question:

> *Treating edge and node as two distinct primitives gated by a two-phase clock, what structural properties emerge — and at which level of a wrap-promotion ladder (raw → light → mass → charge) does each known phenomenon appear?*

## The model

The grid is built from two candidate primitives, examined as separate objects whose relationship is a discovery target rather than a posit:

- **Edge** — a linear, real-valued, signed magnitude with head/tail polarity. Unbounded.
- **Node** — a circular, periodic phase in [0, 2π). Bounded.

A **master clock** runs in two alternating phases:

- **Inhale** (yin, reflective): nodes gather information from connected edges.
- **Exhale** (yang, assertive): edges assert new values from connected nodes.

This is the staggered scheme already specified in [viz/grid-lab.md](../../viz/grid-lab.md) §"Clock" and §"Update rules" (v1 and v2). The project takes those rules as given for the model and analyzes consequences.

The **edge-node junction** is the coupling object between the two primitives. Each clock phase rectifies information flow in one direction across it (inhale: edge → node; exhale: node → edge), making the junction analogous to a bidirectional diode whose forward direction toggles with the clock. Whether the diode analogy is literal (with analogs of forward conduction, reverse blocking, breakdown, and leakage) or only suggestive is itself a question the project examines.

A **couplet** is one (edge, node) pair, posited as the candidate functional building block at the lattice scale. Whether the couplet tiles 2D sheets exactly — without orphan edges or nodes appearing at any scale — is one of the project's central early questions.

## Layer relationship

```
MaSt (particles, masses, charges)
   ↑
GRID lattice (Maxwell, gravity, charge-emergence, ζ)
   ↑
grid-couplet (this project — digital-first, edge + node + clock)   ← parallel to grid-primitive
   ↑
[fractal recursion below the working scale — acknowledged, not pursued]
```

This project sits parallel to grid-primitive — same layer, different model: analog cylinder vs. digital edge+node+clock. Both feed the same GRID lattice abstractions. Where grid-primitive's distributed continuous primitive was analyzed by paper math, grid-couplet's two-primitive model can also be exercised in [viz/grid-lab](../../viz/grid-lab.md) — analytic theorems are the project's deliverable, but the implementation is already in place.

If the project lands cleanly, a natural outgrowth is to extend grid-lab so it can render 2D couplet sheets wrapped as tori (matching the chapter-7 setup).

## Notation

| Symbol | Role | Type |
|---|---|---|
| edge | Linear primitive: signed magnitude with head/tail polarity | Real |
| node | Circular primitive: periodic phase | Real, mod 2π |
| inhale / exhale | The two clock phases (yin / yang) | Discrete state {0, 1} |
| k | Translation factor between magnitude and phase units (per grid-lab v2) | Real, default 1 |
| junction | The edge-node coupling at one end of an edge | Composite |
| couplet | One (edge, node) pair — candidate functional unit | Composite |
| N | Number of edges wrapped into a node (or couplets around a loop) | Integer, ≥ 2 |

A **promotion ladder** organizes the wraps the project examines:

| Level | Wrap | What is expected to emerge | Where examined |
|---|---|---|---|
| L0 | None | Raw information (isolated edge magnitude or node phase) | Chapter 1 |
| L1 | Open 1D edge chain | Coherent traveling perturbation — directional information ("light"-analog) | Chapter 5 |
| L2 | 1D edge chain → 2π wrap into a node | Mass-analog from compact wrap (KK-style, per grid-primitive ch. 8) | Chapter 7 |
| L3 | 2D sheet → torus | Charge — already established in [grid/charge-emergence.md](../../grid/charge-emergence.md) | Cited, not re-derived |

Each level may admit a *leakage* analog — the fraction of information that escapes the wrap. Whether leakage exists at L1 and L2, or only at L3, is one of the project's open questions.

## Ground rules

1. **Discovery, not proof.** Mathematics that *yields* results, not asserts them. Where a result is already known, the chapter arc should still let the math reveal it.

2. **Edge/node primacy is a discovery target, not a posit.** Whether edges are foundational and nodes emergent (the bounded-from-unbounded asymmetry the brainstorm hypothesized), or whether the two are dual views of one underlying property, is examined directly in chapter 2. The rest of the arc adapts to that chapter's outcome.

3. **Stop at the working scale.** The fractal recursion below — whether nodes are sub-edge wraps or vice versa, whether primitives have thickness from sub-primitive structure — is acknowledged structurally but not opened, mirroring grid-primitive's "stop at the cylinder" rule. The exception is where a chapter argues that thickness or its absence is *consequential at the working scale* (chapter 7).

4. **Variables stay symbolic.** Don't pin numerical values until the algebra forces it.

5. **One topic per chapter.**

6. **Computation only when forced.** Paper math first. Use [viz/grid-lab](../../viz/grid-lab.md) where visualization is the only way to see the geometry.

7. **2D and periodic for foundational claims.** 1D arrays are intuition aids; theorems must hold in 2D periodic settings to be load-bearing.

8. **Blocking discoveries early.** Chapters 2 and 4 are framed as decision points. If their negative-result candidates fire, the project rescopes before continuing to the dynamics chapters.

## Goals

### Theories to test

Claims to examine — derived where possible, stated explicitly when taken as input, and falsified explicitly if the math doesn't support them.

1. **Two-primitive model is dynamically equivalent to the cylinder.** With the v2 update rules of [viz/grid-lab](../../viz/grid-lab.md), a 1D periodic array of (edge, node) couplets reproduces the wave dynamics derived in grid-primitive chapter 2 — same dispersion, same bidirectional propagation symmetry, same stability bounds. *Negative result candidate:* if the digital model differs from the cylinder in non-trivial ways, identify whether the difference is granularity, clock structure, or a deeper modeling divergence.

2. **Edge/node duality vs. asymmetry (blocking).** A node can be assembled from N edges wrapped head-to-tail in a 2π loop, with self-consistency constraints on internal state (the second half of the loop must hold complementary values to the first). The reverse construction — assembling an edge from a chain of nodes — is either possible (in which case edge and node are dual views of one property) or structurally impossible (in which case there is an entropy argument grounding the asymmetry: bounding loses information that decompactification cannot recover). *This is a blocking question*: which outcome holds shapes the rest of the arc.

3. **The junction is a clock-rectified coupling.** The edge-node junction transmits information edge → node on inhale and node → edge on exhale, behaving as a bidirectional rectifier whose direction toggles with the clock. Examine whether the diode analogy extends to forward-conduction thresholds, reverse-blocking, breakdown, and leakage — and whether the *junction* (rather than the edge or node alone) is in fact the model's foundational object.

4. **The couplet tiles a 2D hex sheet exactly (blocking).** Building from a single (edge, node) couplet by recursive 120°/240° splits, the 2D hex sheet (per [grid/hexagonal.md](../../grid/hexagonal.md)) admits a periodic wrap in both directions in which every edge belongs to exactly one couplet's edge slot and every node to exactly one couplet's node slot — no orphans. *Negative result candidate:* if some hex configurations admit no exact couplet tiling, the "couplet as building block" framing requires revision before continuing.

5. **A couplet carries a fully characterized directional perturbation.** One (edge, node) pair holds enough state to encode a propagating wavelet in either direction along an array — magnitude on the edge, phase on the node, together specifying both amplitude and direction. This is the digital analog of the cylinder's (e, φ) stress vector.

6. **The promotion ladder organizes wraps.** Each successive wrap promotes information one level: raw → light (open 1D chain → directional traveling perturbation) → mass-analog (1D wrap into node → KK-style compact-direction inertia) → charge (2D sheet → torus, already established in [grid/charge-emergence.md](../../grid/charge-emergence.md)). Each level may admit a leakage analog; whether it does is examined per level.

7. **α and member thickness — a conditional prediction.** Whether α-type phenomena appear at the L2 wrap depends on whether the model gives primitives *thickness*. If primitives are truly 1D and infinitely thin, no leakage occurs at L2 — α belongs at L3 (the 2D-sheet wrap) only. If thickness emerges from fractal sub-structure that influences the working-scale model, an α-analog appears at L2 and the relationship to the L3 α (from charge-emergence) becomes the substantive question. The framing is conditional: the chapter may conclude "no testable proposition at this scale" if the model does not commit to thickness.

8. **Bridge to grid/.** The convention "edge holds a magnitude, junction holds the coupling" maps to the [grid/fields.md](../../grid/fields.md) convention "E on edges, B at junctions." The mapping is provided where it is not obvious. A subsidiary check: [grid/](../../grid/) appears to *assume* cell phases (clock faces) and *implicitly compute* edges as differences between them. If true, that is the inverse of grid-couplet's stance (edges as primary observables, phases as derived) and the bridge must reconcile the two viewpoints.

### Open questions

To answer or sharpen along the way:

1. **Edge/node primacy.** Theory 2's blocking question. The brainstorm's hunch is asymmetry by an entropy argument; the proof or disproof is chapter 2's job.

2. **Couplet exact-tiling.** Theory 4's blocking question. May be answerable from existing hex-tiling combinatorics without writing a full chapter — worth checking the literature before drafting. The minimal-torus routine already in viz (referenced in the brainstorm) is likely a starting point.

3. **Where in the ladder does α appear?** Same α at every level, distinct α's at different levels, or α only at L3? Conditional on theory 7's thickness question.

4. **What is the leakage analog at L1 and L2?** L3 has a clean leakage account in [grid/charge-emergence.md](../../grid/charge-emergence.md). Whether the lower-level wraps admit anything analogous depends on the same thickness question.

5. **Diode analogy extent.** Is the bidirectional rectification at the junction literal (with measurable forward thresholds, breakdown, leakage), suggestive (a useful pedagogical metaphor), or both? The chapter on the junction should land somewhere definite.

6. **Phase-first vs. edge-first conventions in grid/.** Theory 8's subsidiary question. Where in the [grid/](../../grid/) derivations does the choice of primary variable matter, and where is it just bookkeeping?

7. **What does the couplet look like in 3D?** All chapters here work in 1D arrays and 2D sheets per the lattice geometry. Whether a 3D extension to the spatial lattice S preserves the couplet structure, and what new objects appear if it doesn't, is left open.

## Background

### What was tried before

- [viz/grid-lab.md](../../viz/grid-lab.md) — the existing implementation of the two-primitive, two-phase clock model. Provides v1 phase-replacement and v2 Yee-style additive update rules, periodic and open chains, and visualization. This project's chapter 1 takes grid-lab's specification as the model definition rather than re-deriving it.

- [grid-primitive](../grid-primitive/) — the analog-first sibling project that collapsed edges and nodes into a single distributed cylinder primitive. Established (chapters 1–4 confirmed; 5–9 framed) the Maxwell-readiness and entropic-1/r-scaling consequences. Many of its results inform grid-couplet's setup; in particular, chapter 8's α = (2π²/3)·K(1/√2) at N = 6 hex symmetry is the quantitative reference for grid-couplet's L2 thickness question.

- [grid/charge-emergence.md](../../grid/charge-emergence.md) — establishes the L3 wrap (2D hex sheet → torus) producing charge with α as the per-junction coupling magnitude. This project does not re-derive it; the L3 row of the promotion ladder cites it.

- [grid/sim-impedance/](../../grid/sim-impedance/) (Tracks 1–12) — concluded that α cannot be derived from junction geometry alone. The framing here is consistent: theory 7 is conditional on whether thickness gives the model a degree of freedom sim-impedance did not have access to.

### What this project is not trying to do

- **Not re-implementing grid-lab.** The implementation exists; the project supplies analytic theorems on top.
- **Not deriving the value of α.** Theory 7's question is *where* α-type phenomena appear in the ladder, not what value they take.
- **Not committing to which primitive is primary.** Edge, node, and junction are all candidates; theories 2 and 3 examine them.
- **Not opening the fractal recursion.** Per ground rule 3.
- **Not re-deriving Maxwell, gravity, or charge emergence.** [grid/maxwell.md](../../grid/maxwell.md), [grid/gravity.md](../../grid/gravity.md), and [grid/charge-emergence.md](../../grid/charge-emergence.md) remain authoritative.

## Background reading

- [viz/grid-lab.md](../../viz/grid-lab.md) — model specification and update rules
- [grid-primitive/README.md](../grid-primitive/README.md) — analog-first sibling project
- [grid-primitive/08-wrap-and-alpha.md](../grid-primitive/08-wrap-and-alpha.md) — quantitative reference for the L2 thickness question
- [grid/charge-emergence.md](../../grid/charge-emergence.md) — L3 wrap, taken as input
- [grid/foundations.md](../../grid/foundations.md) — GRID axioms the model must respect
- [grid/lattice-geometry.md](../../grid/lattice-geometry.md), [grid/hexagonal.md](../../grid/hexagonal.md) — hex lattice geometry and ζ_2D = 1/3
- [grid/fields.md](../../grid/fields.md) — E-on-edges / B-at-junctions convention used in the bridge

## Chapters

The arc puts blocking discoveries early. Chapters 2 and 4 are decision points: if their negative-result candidates fire, the project rescopes before continuing.

1. **`01-foundation.md`** — Define edge and node as digital primitives. State the two-phase clock and adopt the v1 and v2 update rules from [viz/grid-lab](../../viz/grid-lab.md) without re-deriving them. Establish notation, conventions (yin/yang, inhale/exhale), and ground rules. Posit the couplet as a candidate functional unit *without* committing to which primitive — edge, node, or junction — is foundational. Define the promotion ladder.

2. **`02-edge-node-symmetry.md`** — *Blocking discovery: edge/node primacy.* Construct a node from N edges wrapped head-to-tail in a 2π loop. Identify the self-consistency constraint on internal state (complementary values around the loop). Then attempt the reverse: construct an edge from a chain of nodes. If the reverse works, develop the duality and adapt the rest of the arc to "edge and node are two views of one property." If it fails, formalize the entropy argument that bounds the failure structurally and proceed with edge-as-primitive (with nodes emergent). Either outcome shapes everything downstream.

3. **`03-the-junction-as-diode.md`** — Examine the edge-node junction in isolation, treating it as the model's coupling object. Test the bidirectional-diode framing: clock-rectified information flow, analogs of forward conduction, reverse blocking, breakdown, and leakage. Decide whether the junction (rather than the edge or node) may be the model's foundational object — a possibility chapter 2's outcome may have already addressed, or may have left open.

4. **`04-couplet-tiling.md`** — *Blocking discovery: does the couplet tile a 2D hex sheet exactly?* Starting from a single couplet and applying recursive 120°/240° splits, with periodic wrap in both directions, examine whether every edge and every node belongs to exactly one couplet — no orphans at any scale. Use the existing minimal-torus routine in viz where helpful. If the answer is no, the "couplet as building block" framing needs revision before continuing.

5. **`05-the-1d-array.md`** — Linear array of couplets, periodic and open. Recover the wave dynamics of grid-primitive chapter 2 in digital form: dispersion, bidirectional symmetry, stability. Confirm (theory 1) that the digital and analog models agree on the dynamics. Identify any structural differences and trace them to clock granularity, update-rule choice, or genuine modeling divergence.

6. **`06-the-2d-sheet.md`** — 2D hex sheet of couplets with wye-junction continuity. Derive the 2D wave equation, confirm hexagonal structure, and recover ζ_2D = 1/3. Show how the digital model's E and B fields emerge — bridging to [grid/fields.md](../../grid/fields.md) and confirming the edge-magnitude / junction-curvature mapping.

7. **`07-promotion-ladder.md`** — Formalize the L0 → L1 → L2 → L3 ladder. Examine each level's wrap, what emerges, and whether a leakage analog exists. The α question (theory 7) is the central content: does an α-analog emerge at L2 only when members have thickness? If primitives are truly 1D, what does the *absence* of leakage at L2 imply about α's true home? Compare with grid-primitive chapter 8's quantitative L2 derivation. The chapter may legitimately conclude "no testable proposition at the working scale" — that outcome is itself informative.

8. **`08-bridge-to-grid.md`** — Bridge to [grid/](../../grid/). Establish the mapping from edge values and node phases to the cell phases θ and link connections A_μ used in [grid/maxwell.md](../../grid/maxwell.md) and [grid/foundations.md](../../grid/foundations.md). Reconcile the apparent edge-first stance here with the phase-first stance in grid/. Confirm consistency with [grid/charge-emergence.md](../../grid/charge-emergence.md)'s L3 result.

9. **`09-closing-summary.md`** — Consolidate established results, ruled-out items, and unexpected findings. Compare with grid-primitive: where did the analog-first and digital-first models agree, where did they diverge, and what does each see that the other missed? Hand off to follow-ups (including grid-lab extension to 2D toroidal rendering if the project lands cleanly).

Each chapter is added one at a time. The arc is a sketch, not a contract.
