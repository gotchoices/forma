# Grid Duality
Brainstorming

## Premise
Two primitives: **edge** and **node**. The duality of these two is the project's subject. Build the simplest discrete lattice model from them; bridge the result cleanly to the existing [grid](../../grid/) derivations.

## Origin
This project is a fresh start after [grid-couplet](../grid-couplet/) drifted during foundational exploration. Three lessons carry forward:
- The cos-weighted node update inherited from grid-lab is unstable at 2D coordination; do not import it without checking.
- The couplet (1 edge + 1 node) only pairs 1:1 in 1D — the ratio E/V = coordination/2 makes that pairing impossible at coord > 2. The couplet is *not* the lattice's building block.
- Each primitive's physical role should be named before any update rule is written.

## Hypotheses to test
- Two primitives — edge and node — suffice for stable wave propagation in 1D, 2D, and 3D lattices.
- Edges are polarized (head and tail). Edge orientations across the lattice can be standardized in a "common direction":
  - 1D: all edges point right.
  - 2D hex: 3 distinct directions, each oriented uniformly.
  - 3D: 4 (tetrahedral) or 6 (cubic) directions, each oriented uniformly.
- Nodes hold a value that wraps mod 2π. Edges hold an unbounded real-valued accumulator.
- The simplest local update rule:
  - Node update: signed sum of incident edge values (sign by whether this node is the edge's head or tail), mod 2π.
  - Edge update: principal-branch difference of endpoint node values, accumulated.
- The two-phase clock alternates the two updates: nodes first, then edges (or the reverse — to be settled by the math).
- The dynamics, on a 2D hex lattice, reproduce [grid/sim-maxwell](../../grid/sim-maxwell/)'s wave propagation in observable behavior — not necessarily the same internal rule.
- The static-field dynamics, in 2D, reproduce [grid/sim-gravity-2](../../grid/sim-gravity-2/)'s logarithmic decay (giving 1/r force scaling).
- The wrap-promotion ladder (information → light → mass → charge) maps to successive closures of the lattice graph: open chains, 1D loops, 2D plaquettes, 2D-sheet wraps into a torus.

## Questions to answer
- What is the simplest update rule that's stable at coord > 2 (where naive unit time-step leapfrog fails CFL)? Sub-unit time step, 1/N normalization, or some other regularization?
- How do we choose edge orientations in 2D hex and 3D for a clean global pattern?
- Does the 2D model reproduce sim-maxwell's directional wave propagation?
- Does the 2D static-field model reproduce sim-gravity-2's 1/r force law?
- How do (node phases, edge accumulators) map to grid's (θ, A_link, E, B)?
- Where in the wrap-promotion ladder does α appear?

## Bonus question — settle last
- Can a functional node be constructed from a configuration of edges?
- Can a functional edge be constructed from a configuration of nodes?
- If yes: what are the mutation rules?
- If no: what is the structural reason each primitive is irreducible?
- This was the original [grid-couplet](../grid-couplet/) brainstorm's central question. Preserved here as a closing exercise to clarify what makes each primitive unique.

## Plan
1. Define the two primitives precisely. Name their physical roles.
2. State the simplest update rules.
3. Construct example lattices in 1D, 2D, 3D with standardized edge orientations.
4. Bridge: dynamics on a 2D hex lattice reproduce [grid/sim-maxwell](../../grid/sim-maxwell/).
5. Bridge: static field in 2D reproduces [grid/sim-gravity-2](../../grid/sim-gravity-2/).
6. Map the wrap-promotion ladder to closed loops in the lattice graph.
7. Bonus: construct node-from-edges and edge-from-nodes — or prove impossibility.
8. Absorb the relevant findings from grid-couplet's STATUS.md, then delete grid-couplet.

## Status
Awaiting first chapter.
