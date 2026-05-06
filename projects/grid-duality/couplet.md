# Couplet — reference and lessons learned

This file captures what was learned during the [grid-couplet](../grid-couplet/) exploration that preceded grid-duality. It is *not* part of grid-duality's chapter sequence; it serves as a standalone reference. The grid-couplet directory will eventually be deleted, and this file is the surviving record. Anyone who wants more detail than is captured here can consult the git history.

## What grid-couplet was

A digital-first lattice model with two primitives — an *edge* (linear, integrated history) and a *node* (phase, bounded). A "couplet" was a single (edge, node) pair, posited as the lattice's building block. The project's stated goals: establish the two primitives, determine whether one can be derived from the other, construct a wrap-promotion ladder of physical phenomena from successive lattice closures, and bridge the result to grid's existing derivations.

## What worked

- Two primitives — edge and node — as the basis for a discrete wave-on-graph model.
- A two-phase clock alternating node and edge updates (Yee-style staggering).
- Closed loops with mod-2π node phases producing topological winding numbers — the seed of U(1) gauge structure.
- The "two pieces of information" intuition: wave direction encoded in the (node, edge) pair locally, not in separate per-edge directional channels.
- The wrap-promotion ladder concept (information → light → mass → charge from successive closures) as a structural organizing principle.

## What did not work, and what to do instead

**The couplet 1:1 ratio fails for coord > 2.** In a regular graph with coordination N, E/V = N/2. This is 1 only in 1D linear arrays. In 2D hex (N=3) it is 1.5; in 3D tetrahedral (N=4) it is 2. The couplet, as a 1-edge-plus-1-node lattice tile, does not generalize.

> *Lesson for grid-duality:* keep edges and nodes as the two primitives; drop "the couplet as the lattice building block." Each *node-edge incidence* is locally a (node, edge) pair, but there is no global 1:1 pairing.

**The cos-weighted node update is unstable at coord 3.** The rule φ ← φ + Σᵢ eᵢ·cos(φ_attach,ᵢ), at hex Y-junctions with attach angles 0, ±2π/3, has eigenvalues outside the unit circle. Driven simulation diverges to −10⁶ in ~1200 steps.

> *Lesson:* the cos-weighted form imported a *vector-field* intuition (node as directional sensor) into a *scalar-on-graph* model (node as accumulator). The right rule is signed sum of incident edges, with sign from each edge's tail/head orientation, not cos-weighting.

**Phase-on-vertices and amplitude-on-edges are different paradigms.** Grid's [sim-maxwell](../../grid/sim-maxwell/) uses traveling-wave amplitudes (a_fwd, a_bwd) on edges with vertex scattering S = (2/N)·J − I, no per-vertex state, and a single-phase clock. The grid-couplet paradigm placed phase on nodes with integrated history on edges and used a two-phase clock. The two paradigms are related by transmission-line duality but the discrete update rules don't match by notation alone.

> *Lesson:* bridges to grid's simulations should be *operational equivalence* (same observable behavior under same drives), verified by simulation, not asserted by notational substitution.

**Naive leapfrog at unit time step is CFL-unstable for coord > 2.** Stability requires Δt ≤ √(2/N). At unit Δt this fails for N ≥ 3, which means any 2D lattice without normalization. The cos-weighted instability above is one symptom of this same constraint.

> *Lesson:* the simplest update rule needs CFL-compliant time-step or 1/N normalization. Pick one deliberately rather than inheriting unit Δt without checking.

**Bond-graph variables clarify the physics.** Calling the node value "phase" and the edge value "magnitude" was abstract and led to repeated taxonomy revisions. The bond-graph framing — node as an *across* variable (potential-like), edge as a *through* variable (flow-like) — makes the physical interpretation precise; the update rules then follow naturally from continuity at nodes and Faraday-like coupling along edges.

> *Lesson:* name each primitive's physical role before writing update rules.

**Don't conflate scalar nodes with structured "dials".** The grid-couplet exploration cycled through point, dial, node taxonomies trying to give the node angular structure. The clean answer: a node is a 0D scalar accumulator. Closed loops of nodes-and-edges *can* be coarse-grained into emergent compound objects, but the primitive node has no internal extent.

> *Lesson:* keep the node simple. If an emergent compound object is wanted later, derive it; don't bake it into the primitive.

**Fractal-recursion language was unnecessary.** grid-couplet imported "stop at the working scale" from grid-primitive. In a discrete graph model with 0D nodes and 1D edges, no sub-scale recursion is required — that *is* the structural floor.

> *Lesson:* don't carry framing from grid-primitive (where the cylinder primitive could be a sub-grid) into a model where it doesn't apply.

**"Closure forces bounded phase" is a posit, not a derivation.** Grid-couplet's chapter 2 attempted to derive mod-2π boundedness from closed-loop topology. The argument is partially sound but is interpretive — bounded phase is what you commit to by treating node values as U(1) (compact) rather than ℝ (unbounded real). The choice has consequences (winding numbers; topological invariants) that are real, but the choice itself is a modeling decision.

> *Lesson:* state the U(1) vs ℝ choice for node values explicitly, as a posit.

**Don't import update rules from grid-lab without 2D verification.** grid-couplet adopted grid-lab's v2 cos-weighted rule on the assumption it generalized from 1D to 2D. It does not.

> *Lesson:* whatever update rule grid-duality settles on must be tested at 2D coordination before chapter work goes deep.

## Open questions inherited

These were posed by grid-couplet but did not reach a clean resolution. They are open for grid-duality:

- Where in the wrap-promotion ladder does α appear? grid-couplet sketched a "second-order wrap" hypothesis (α emerges only when wrapping across a dimension that already has extent) but did not test it.
- Can a functional node be constructed from edges, or vice versa? grid-couplet wandered through this for several reframings without an answer. With a stable foundation, grid-duality may settle it cleanly. Bonus chapter material.

## What grid-duality should carry forward in one paragraph

Two primitives, edge and node, with named bond-graph roles (node = across, edge = through). Nodes hold a U(1) phase; edges hold an unbounded real-valued accumulator. Edges have polarity, standardized in a common direction across the lattice. Two-phase clock; nodes update by signed sum of incident edges (sign by tail/head, mod 2π); edges update by principal-branch difference of endpoint nodes (accumulated). CFL handled by sub-unit time step or 1/N normalization, decided once and applied consistently. Bridges to [sim-maxwell](../../grid/sim-maxwell/) and [sim-gravity-2](../../grid/sim-gravity-2/) verified by simulation, not asserted by name.
