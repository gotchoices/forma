# Scattering (sim-maxwell)

**One-line:** A network of N-register processors (nodes) connected by two-ended transmission lines (edges). One clock cycle has two phases: an *inhale* in which each node scatters the values in its registers, and an *exhale* in which each edge propagates its end values to the opposite end. This is the model used in [grid/sim-maxwell](../../../grid/sim-maxwell/).

## State

| Where | What | Domain | Role |
|---|---|---|---|
| Register (one per edge-end) | one real value | ℝ | the state of one end of one edge, hosted at the node it docks into |

A **register** is the structural element formed where one end of an edge docks into a node. It is owned jointly: the edge contributes the *end*, the node contributes the *socket*. Each edge contributes two registers (one at each end). Each node hosts one register per incident edge — so a node of coordination N has N registers.

The register is not a separate primitive. It is the *meeting point* of the substrate's two primitives (edge and node). The lattice's total state is exactly 2·|edges| real numbers — equivalently, Σ_node (coordination of node) values, since every edge contributes to two nodes.

The model has no separate node state and no separate edge state outside of the registers.

## Clock

Two-phase. One full clock cycle is one *inhale* followed by one *exhale*.

- **Inhale.** Each node samples its registers, computes new values from them, and overwrites the registers. This is a node-local computation.
- **Exhale.** Each edge transmits the values at its two ends to one another along the edge body. Synchronously across the lattice, the value at end A propagates to end B and vice versa, which has the effect of swapping the values in the two registers an edge connects.

The exhale is what gives the lattice its **speed of light**: one exhale = one edge transit. Information cannot move from node to node faster than one edge per cycle. This is structurally analogous to the propagation delay of a real transmission line.

## Update rules

**Inhale (node).** At each node of coordination N with registers r₁, …, r_N (in any local ordering):

> r_i ← (2/N) · (r₁ + r₂ + … + r_N) − r_i      for each i = 1, …, N

This is the matrix S = (2/N)·J − I applied to the register vector, where J is the N×N all-ones matrix and I is the N×N identity. S is the *unique* solution to two physical constraints that any junction must enforce: voltage continuity (all incident lines see the same potential at the node) and Kirchhoff current conservation. It is not an arbitrary update rule; it is what those two constraints require.

S is unitary for any N, so the inhale preserves the energy norm Σ r_i² locally at every node.

**Exhale (edge).** For each edge with end-A register r_A (hosted at one node) and end-B register r_B (hosted at the other node):

> r_A ← r_B,  r_B ← r_A      (synchronous swap)

The exhale preserves the energy norm trivially — it is a pure relabeling.

A full cycle (inhale + exhale) is therefore a unitary operation on the global state vector. Energy is conserved exactly per step.

## Equivalent (a_fwd, a_bwd) labeling

For readers coming from sim-maxwell or transmission-line theory, the two registers of an edge can equivalently be relabeled by direction:

- a_fwd[edge] = the register hosted at the edge's *head* node (the value just emitted from the tail and currently arriving at the head)
- a_bwd[edge] = the register hosted at the edge's *tail* node (the value just emitted from the head and currently arriving at the tail)

The combined inhale + exhale of one cycle then matches sim-maxwell's update exactly. The two notations are redundant; the register reading is preferred here because it is paradigm-neutral about edge polarity.

## Edge polarity

Polarity (which end is "tail," which is "head") is structurally inert under this model. The two registers of an edge are unordered; the inhale uses only the local register vector at each node, and the exhale is a symmetric swap. Polarity is retained in the substrate as a labeling convention — useful for v-i models that *do* read s_e = ±1 from polarity — but the Scattering dynamics does not use it.

## Topology

The model carries no built-in topological invariants in its register state. Plaquette flux and winding can be *measured* by tracing register values around a closed loop over time, but they are derived observables, not stored quantities. Topological invariants for Scattering live on edge cycles (paths of register-to-register propagation), not on node loops as in the v-i paradigm.

## Stability

**Unitary by construction.** Each cycle is a composition of two unitary operations (the local inhale at each node, and the global swap of the exhale), so the global state evolution is unitary. Energy (Σ r²) conserves exactly per cycle. Unit time step is stable for any coordination with no normalization needed.

For N = 3 (hex):
- Reflection coefficient (diagonal of S): −1/3
- Transmission to each other edge (off-diagonal of S): +2/3
- Energy split per Y-junction: (1/3)² + 2·(2/3)² = 1/9 + 8/9 = 1 ✓

## Notes

- This is the **register / transmission-line paradigm**, distinct from the bond-graph paradigm of Telegrapher. Each edge is a 1D wave-carrier; each node is an active processor enforcing junction physics; each register is the meeting point.
- Two values per edge is what 1D wave physics requires (two real degrees of freedom per spatial location, like position+velocity in mechanics or d'Alembert's left- and right-moving characteristics on a string). It is not a doubling of state; it is the natural minimum.
- Reproduces grid/sim-maxwell exactly (this is its model). The "bridge to grid" is the model itself.
- Phase information is implicit in the time-history of register values, not stored explicitly. Phase circulation around a hexagon is recovered from the temporal pattern of registers as a wave traverses.
- The two-phase clock makes the speed of light explicit: c = (one edge length) / (one exhale duration). In a uniform lattice this is constant; in a lattice with varying edge lengths or transit times, c could vary spatially — a possible direction for future work.
