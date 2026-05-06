# grid-duality

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** A digital-first model of the GRID lattice using two primitives — edge and node — with the simplest local update rules. Aims to reproduce the wave propagation observed in [grid/sim-maxwell](../../grid/sim-maxwell/) and the static-field behavior of [grid/sim-gravity-2](../../grid/sim-gravity-2/), then construct the wrap-promotion ladder (information → light → mass → charge) from successive lattice closures.
**Method:** Mathematical derivation as discovery; computational verification against grid's existing simulations; minimum verbosity.
**Status:** Framing complete. Awaiting first chapter.

## Why this project exists

[grid-primitive](../grid-primitive/) modeled the GRID lattice analog-first: a single distributed object (the cylinder primitive) carrying both magnitude and phase on one continuous body. That model produced clean derivations for wave propagation, entropic gravity scaling, and a structural-ratio account of α.

A digital-first counterpart would be a graph of discrete primitives, with local update rules at each, evolving under a clock. The earlier viz [viz/grid-lab](../../viz/grid-lab.md) sketched such a model but used a cos-weighted update rule that turns out to be unstable at 2D coordination.

The first attempt at a digital-first project — [grid-couplet](../grid-couplet/) — accumulated foundational drift before producing a stable framework. Its findings are preserved in [couplet.md](couplet.md). grid-duality is a fresh start, pinning the foundation deliberately:

- Two primitives — edge and node — with named bond-graph roles (across / through).
- The simplest local update rules consistent with stable wave propagation at any coordination.
- Edge orientations standardized in a common direction across the lattice.
- Bridges to grid's existing simulations verified operationally before any deep theory work.

The central question:

> *What is the simplest two-primitive discrete lattice model that reproduces grid's wave-propagation and static-field behavior, and what does the wrap-promotion ladder look like under it?*

## Layer relationship

```
MaSt (particles, masses, charges)
   ↑
GRID lattice (Maxwell, gravity, charge-emergence, ζ)
   ↑
grid-duality (this project)        ← parallel to grid-primitive
```

Same layer as grid-primitive, different model: analog-first cylinder vs. digital-first edge+node graph. Both feed grid's lattice abstractions. grid-primitive's cylinder is a coarse-grained continuous object; grid-duality's nodes-and-edges are the discrete graph at the same scale. Where they meet, they should agree on observables.

## The model in brief

Two primitives with distinct physical roles:

- **Node** — a 0D scalar accumulator holding an *across*-like value. Its state is a phase in [0, 2π) (a U(1) element). The bounded-phase character is a deliberate commitment, not derived.
- **Edge** — a 1D relational object connecting two nodes, holding a *through*-like value. Its state is an unbounded real-valued accumulator (the integrated history of the difference between its endpoints). Edges have polarity (head and tail), set when placed in the lattice.

Edge orientations across the lattice are standardized in a common direction (1D right; 2D hex with three uniform directions; 3D analog deferred unless needed).

A master clock alternates two phases. On one phase, nodes update by signed sum of incident edges (sign from tail-vs-head incidence at this node), modulo 2π. On the other phase, edges update by the principal-branch difference of their endpoints' values, accumulated. CFL stability at coord > 2 requires either a sub-unit time step or a 1/N-style normalization — to be settled in chapter 1.

Full definitions, the update rule's exact form, and lattice-construction conventions are the content of chapters 1 and 2.

## Ground rules

1. **Discovery, not proof.** Mathematics that *yields* results, not asserts them.
2. **Two primitives only.** Edge and node. No third type promoted to primitive — emergent compound objects (loops, dials, plaquettes) are derived, not posited.
3. **Physical role named before update rule.** Each primitive's bond-graph role (across / through) is named in chapter 1 §2-§3 before any update rule is written.
4. **Update rules tested in 2D early.** Whatever rule chapter 1 commits to must be verified stable at coord 3 before chapter work goes deep. The cos-weighted-instability lesson from [couplet.md](couplet.md) is the precedent.
5. **Variables stay symbolic.** Don't pin numerical values until the algebra forces it.
6. **Computation only when forced.** Paper math first; simulation where verification requires it.
7. **Operational bridges to grid.** Bridges to [grid/sim-maxwell](../../grid/sim-maxwell/) and [grid/sim-gravity-2](../../grid/sim-gravity-2/) are verified by simulation showing equivalent observable behavior, not by notational substitution.

## Goals

### Theories to test

Claims to examine — derived where possible, stated explicitly when taken as input, falsified explicitly if the math doesn't support them.

1. **Two primitives suffice for stable wave propagation in 1D, 2D, 3D.** Edge and node, with the simplest local update rule, support a discrete wave equation on graphs of any coordination, given proper CFL handling.

2. **Edge orientations standardize cleanly in a common direction.** A global orientation pattern (1D rightward; 2D hex three-direction; 3D analog) gives every node enough local information to apply its update rule by tail/head bookkeeping alone, without needing a sublattice label.

3. **Signed sum at nodes reproduces wave dynamics.** Nodes updating by signed sum of incident edges (sign by tail/head) — without cos-weighting — gives stable wave propagation when paired with the principal-branch-difference edge update.

4. **Dynamics on a 2D hex lattice reproduce sim-maxwell's wave propagation.** The 2D hex model under chapter 1's update rule produces directional wave propagation matching [grid/sim-maxwell](../../grid/sim-maxwell/) in observable behavior — speed, directionality ratio, energy conservation.

5. **The 2D static-field model reproduces sim-gravity-2's 1/r force law.** The static (frozen-clock) configuration of the 2D hex model with a pinned defect produces a logarithmic field decay, matching [grid/sim-gravity-2](../../grid/sim-gravity-2/) and giving 1/r force scaling.

6. **The wrap-promotion ladder maps to lattice closures.** L0 = single node or single edge; L1 = open 1D edge chain; L2 = closed 1D loop in the graph (1D wrap); L3 = 2D-sheet wrap into a torus. Each level corresponds to a topologically distinct closure operation on the lattice graph.

7. **α appears at a specific level of the ladder, related to a specific kind of wrap.** Conjecture: α emerges at L3 (the 2D wrap), corresponding to the second-order wrap framing carried over from couplet.md. To be tested rather than posited.

8. **Bridge to grid maps cleanly.** (Node phase, edge accumulator) maps to grid's (cell phase θ, link gauge connection A_link), with E and B emerging from differences and circulations of these.

### Open questions

To answer or sharpen along the way:

1. **CFL handling.** Sub-unit time step Δt = √(2/N) or 1/N normalization on the node update — pick one based on which keeps the model's structure cleaner.

2. **Edge orientation in 3D.** Tetrahedral, diamond, or cubic — each has a different natural common-direction scheme. Settle when 3D becomes a topic.

3. **Where in the ladder does α appear?** Theory 7 conjectures L3. To be verified, refined, or refuted.

4. **Operational equivalence with sim-maxwell.** sim-maxwell stores two amplitudes per edge with no per-node state and a single-phase clock. grid-duality stores one phase per node, one accumulator per edge, and uses a two-phase clock. The bridge is a transmission-line-style duality — verifying it requires showing the two paradigms produce the same observables under the same drives, not the same internal state.

5. **Which primitive is more fundamental?** Bonus question, deferred to the closing chapters.

## Background

### What was tried before

- [grid-couplet](../grid-couplet/) — earlier digital-first attempt; lessons captured in [couplet.md](couplet.md). The couplet (1 edge + 1 node) was posited as the lattice's building block but does not generalize beyond 1D. The cos-weighted update rule from grid-lab is unstable at coord 3.
- [grid-primitive](../grid-primitive/) — analog-first sibling. Established Maxwell-readiness and entropic-gravity scaling for a single distributed cylinder primitive. Sets the bar grid-duality should match in observable behavior.
- [viz/grid-lab](../../viz/grid-lab.md) — the original digital-first sketch. Adopted as inspiration but not as authority; its v2 cos-weighted update rule is the one couplet.md identifies as 2D-unstable.
- [grid/sim-maxwell](../../grid/sim-maxwell/) — wave-propagation simulation on hex and triangular lattices using vertex scattering S = (2/N)·J − I with traveling-wave amplitudes on edges. Bridge target.
- [grid/sim-gravity-2](../../grid/sim-gravity-2/) — static-field simulation showing logarithmic decay (1/r force) from a pinned defect. Bridge target.

### What this project is not trying to do

- **Not deriving the value of α.** Theory 7 asks where α-type phenomena appear in the ladder, not what value α takes.
- **Not reimplementing grid-lab.** Where grid-duality's update rule diverges from grid-lab's, grid-duality takes precedence; grid-lab can be updated downstream if needed.
- **Not committing to a specific charge-from-edges or mass-from-edges story before the foundation is solid.** The wrap-promotion ladder is examined per-level, not asserted globally.
- **Not opening sub-primitive structure.** Nodes are 0D, edges are 1D. No fractal recursion required by the model.
- **Not re-deriving Maxwell or gravity from scratch.** [grid/maxwell.md](../../grid/maxwell.md) and [grid/gravity.md](../../grid/gravity.md) remain authoritative; grid-duality supplies clean discrete inputs to those derivations.

## Background reading

- [couplet.md](couplet.md) — lessons from the prior project, kept as standalone reference
- [grid-primitive/README.md](../grid-primitive/README.md) — analog-first sibling
- [grid/sim-maxwell/README.md](../../grid/sim-maxwell/README.md) — bridge target for wave propagation
- [grid/sim-gravity-2/README.md](../../grid/sim-gravity-2/README.md) — bridge target for static field
- [grid/foundations.md](../../grid/foundations.md) — GRID axioms the model must respect
- [grid/charge-emergence.md](../../grid/charge-emergence.md) — where the L3 charge-from-wrap story currently lives
- [viz/grid-lab.md](../../viz/grid-lab.md) — earlier digital-first sketch

## Chapters

The arc below is a sketch. Early chapters are framed in detail; later chapters are framed as questions. The project may redirect when a chapter's math reveals something unexpected.

1. **`01-foundation.md`** — Define the two primitives. Name physical roles (node = across, edge = through). State the simplest update rules (signed sum at nodes mod 2π; principal-branch difference at edges, accumulated). Settle CFL handling. Standardize edge orientation in 1D and 2D. Define the two-phase clock.

2. **`02-lattice-construction.md`** — How to assemble lattices in 1D, 2D, and (sketched) 3D from the two primitives with standardized edge orientations. Worked examples: 1D periodic loop, 2D hex sheet on a torus, brief 3D outline. Connection geometry, neighbor relations, periodic boundary handling.

3. **`03-wave-dynamics.md`** — Wave propagation on 1D and 2D lattices. Verify dispersion, stability, propagation speed, bidirectional symmetry. Confirm that the chapter 1 update rule produces a discrete wave equation on the graph. CFL verification at coord 3.

4. **`04-bridge-to-maxwell.md`** — Compare the 2D hex dynamics to [grid/sim-maxwell](../../grid/sim-maxwell/). Operational equivalence test: under matched drive conditions, do both models produce the same propagation speed, directional preference, and energy behavior? If yes, the duality between phase-on-vertices (grid-duality) and amplitude-on-edges (sim-maxwell) is verified. If no, characterize the discrepancy.

5. **`05-bridge-to-gravity.md`** — Static-field test: pin a defect at the center of a 2D hex lattice, freeze the dynamics, solve for the equilibrium field. Compare to [grid/sim-gravity-2](../../grid/sim-gravity-2/)'s logarithmic decay and 1/r force scaling. Verify the entropic-gravity input is reproduced.

6. **`06-wrap-promotion-ladder.md`** — Map L0 → L1 → L2 → L3 onto specific lattice closures: open chains, 1D loops in the graph, 2D-sheet wraps into a torus. Identify what emerges at each level. Connect to grid's charge-from-wrap account at L3.

7. **`07-where-alpha-appears.md`** — Test theory 7: does α emerge at L3 only (second-order wrap), or at L2 as well, or somewhere else? Concrete derivation or simulation evidence.

8. **`08-edges-vs-nodes.md`** — Bonus chapter. Can a functional node be constructed from a configuration of edges? Can a functional edge be constructed from nodes? If yes, what are the mutation rules? If no, what makes each primitive structurally unique? This is the original [grid-couplet](../grid-couplet/) brainstorm's central question, settled cleanly now that the foundation is solid.

9. **`09-closing-summary.md`** — Consolidate established results, ruled-out items, unexpected findings. Compare with grid-primitive: where the analog-first cylinder and digital-first graph models converge / diverge. Hand off to follow-ups.

Each chapter is added one at a time. The arc is a sketch, not a contract.
