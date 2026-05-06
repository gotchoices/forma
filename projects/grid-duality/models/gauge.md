# Gauge

**One-line:** Unbounded level on nodes; bounded gauge field on edges. Topological invariants live on plaquette flux around closed edge cycles.

## State

| Where | Symbol | Domain | Role |
|---|---|---|---|
| Node | θ | ℝ (unbounded real) | level — "accumulator" or "phase" of a matter field |
| Edge | A | [0, 2π) (U(1) compact) | gauge field — the integrated phase difference along the edge, bounded |

## Clock

Two-phase. Same staggering as Telegrapher: node-phase, then edge-phase.

## Update rules

**Phase 0 — node update.** For each node:

> θ_node ← θ_node + Σ_e s_e · sin(A_e)

where s_e = +1 / −1 by tail/head orientation. The use of sin(A) rather than A reflects that A is a U(1) element (not a real); sin(A) is the natural ℝ-valued "current" derived from the gauge phase. This is structurally analogous to the gauge-coupling term in lattice gauge theories.

**Phase 1 — edge update.** For each edge:

> A_edge ← (A_edge + (θ_tail − θ_head)) mod 2π

The edge's bounded phase accumulates the difference of node levels, with mod 2π reducing the result back into [0, 2π). The mod is not just a stability convention — it's the model's structural commitment that A lives in U(1).

## Topology

Closed cycles of edges (plaquettes — smallest closed loops in the graph) accumulate edge values: Σ_loop A_e = Φ_plaquette mod 2π. This is the **Wilson-loop / magnetic-flux** topological invariant. For a hex lattice, the smallest plaquette is the 6-cycle around one hexagon.

Because the gauge field is bounded mod 2π, plaquette flux is naturally quantized — the lattice analog of magnetic flux quantization.

This is gauge-field-on-edges flavor: the lattice carries a compact gauge structure whose topology is exposed by closed edge cycles, not node loops.

## Stability

- **1D**: stable, but uninteresting — 1D has no plaquettes, so no gauge structure surfaces.
- **2D hex**: stability depends on the form of the sin(A) coupling. The compact (mod 2π) edge update doesn't grow unboundedly, but linearization around small A may have CFL constraints similar to Telegrapher.
- **Higher coordination**: TBD.

## Notes

- This is the lattice-gauge-theory flavor. Pure gauge dynamics (without matter — i.e., θ frozen or absent) reduces to compact U(1) Yang-Mills on the lattice.
- The "node = current accumulator" framing maps loosely here: the node holds an unbounded ℝ-valued "level" that integrates contributions from neighboring edges, while the edge holds a bounded "phase" that's the natural lattice link variable.
- Distinct from Telegrapher because *which lattice structure carries the bound* is different. Telegrapher: nodes bounded → node-loop winding. Gauge: edges bounded → plaquette flux.
- Whether this model reproduces sim-maxwell-like wave propagation is an open question — it depends on the linearized small-A regime and how plaquette dynamics interact with traveling-wave propagation.
