# Telegrapher

**One-line:** Bounded across (voltage-like) on nodes; unbounded through (current-like) on edges. Two-phase clock with signed-sum at nodes and principal-branch difference at edges.

## State

| Where | Symbol | Domain | Role |
|---|---|---|---|
| Node | v | [0, 2π) (U(1) compact) | across variable — "voltage" / "level" / "potential," bounded |
| Edge | i | ℝ (unbounded real) | through variable — "current" / "flow," unbounded |

## Clock

Two-phase. One full clock cycle is one node-phase followed by one edge-phase. Nodes and edges never update simultaneously.

## Update rules

**Phase 0 — node update.** For each node:

> v_node ← (v_node + Σ_e s_e · i_e) mod 2π

where the sum runs over edges incident at this node, i_e is the value of edge e, and s_e = +1 if this node is the *head* of edge e, −1 if this node is the *tail*. The sign reflects Kirchhoff-style continuity: incoming flow increases the node's level, outgoing flow decreases it.

**Phase 1 — edge update.** For each edge:

> i_edge ← i_edge + (v_tail − v_head)_pb

where (·)_pb denotes principal-branch reduction to (−π, π]. The reduction is necessary because both endpoints live in [0, 2π); without it, the literal difference can range over (−2π, 2π) and the integration becomes ambiguous near the wrap-around.

## Topology

Closed loops *through nodes* accumulate principal-branch differences that sum to 2π·k for integer k — the **node-loop winding number**. Topological invariants live on these node-loop windings.

This is matter-field-on-nodes flavor: the node hosts a U(1) compact phase analogous to a Higgs-style scalar field. The gauge structure is implicit in the edge values rather than stored as a U(1) link variable.

## Stability

- **1D linear array** (coord 2): marginally stable at unit time step. Eigenvalues on the unit circle.
- **2D hex** (coord 3): unstable at unit time step. CFL bound γ ≤ √(2/N) violated. Per-step changes at junctions are large; transient dynamics become erratic.
- **Higher coordination**: progressively worse without normalization.

## Notes

- This is the bond-graph telegrapher's-equations discretization with implicit L = C = 1 per primitive.
- Power conservation in steady state: at any node, Σ s_e · i_e = 0 implies Kirchhoff balance. For a sustained drive at a Y-junction with one input and two outputs, steady state has i_in = i_out_1 + i_out_2 (current splits equally if symmetric).
- Single-pulse 2D transients show amplification at junctions because the rule lets edges read the full v_node onto their integration, doubling apparent amplitude. This is the issue the comparison test bench will measure.
- Without 2D regularization, this model is expected to fail the 2D wavefront and 2D Y-junction tests. See the Normalized variant for one fix.
