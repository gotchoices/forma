# cos-weighted (reference, expected to fail)

**One-line:** grid-lab v2 rule. Node update weights each edge by cos(φ_attach). Known unstable at coord 3; included as a baseline failure mode.

## State

| Where | Symbol | Domain | Role |
|---|---|---|---|
| Node | v | [0, 2π) (U(1) compact) | across variable, bounded |
| Edge | i | ℝ (unbounded real) | through variable, unbounded |

In addition, the lattice carries **angular structure** at each node: for every edge incident at a node, the angle φ_attach at which the edge connects (measured from the node's intrinsic zero direction) is part of the model's input. This angular structure is part of the lattice's spatial embedding, not part of the node's dynamic state.

## Clock

Two-phase.

## Update rules

**Phase 0 — node update.** For each node:

> v_node ← (v_node + Σ_e i_e · cos(φ_attach,e)) mod 2π

where φ_attach,e is the angle at which edge e attaches to this node. The cos factor implements a directional projection of each edge's contribution.

**Phase 1 — edge update.** Same as Telegrapher:

> i_edge ← i_edge + (v_tail − v_head)_pb

## Topology

Same as Telegrapher: node-loop windings (in principle).

## Stability

**Unstable at coord 3 with hex-natural attach angles** (0, ±2π/3). The linearized update matrix has eigenvalues outside the unit circle. Direct simulation diverges to ~−10⁶ within 1200 steps under sustained drive.

Stable at coord 2 (1D linear, attach angles 0, π) — the cos values reduce to ±1, recovering the signed-sum rule of Telegrapher.

## Notes

- This is the rule [viz/grid-lab](../../../viz/grid-lab.md) uses (its v2 update). It generalizes the 1D Telegrapher rule by projecting each edge's contribution onto the node via cos(φ_attach), apparently a vector-style inner product.
- Imports a *vector-field intuition* (node as directional sensor with intrinsic zero) into a *scalar-on-graph model* (node as accumulator). The mismatch is what produces the instability at coord > 2.
- Included as a candidate primarily for comparison: when the test bench runs it on 1D tests, it should match Telegrapher; on 2D tests, it should fail conspicuously. This anchors the comparison and demonstrates that grid-lab's rule, while a useful 1D sketch, doesn't scale.
- See [couplet.md](../couplet.md) for the original analysis.
