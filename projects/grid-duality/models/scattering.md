# Scattering (sim-maxwell)

**One-line:** Two wave amplitudes per edge, no node state, single-phase clock with unitary scattering at vertices. This is the model used in [grid/sim-maxwell](../../../grid/sim-maxwell/).

## State

| Where | Symbol | Domain | Role |
|---|---|---|---|
| Node | — | none | nodes are pure scatterers; no internal state |
| Edge | (a_fwd, a_bwd) | ℝ × ℝ | forward and backward traveling-wave amplitudes |

The edge state is a pair: a_fwd is the amplitude propagating in the tail-to-head direction; a_bwd is the amplitude propagating head-to-tail.

## Clock

Single-phase. One scatter step per cycle. There is no two-phase staggering.

## Update rules

At each clock cycle, every vertex applies the **scattering matrix** S = (2/N)·J − I, where N is the vertex's coordination, J is the all-ones matrix, and I is the identity:

> outgoing_e = (2/N) · total_incoming − incoming_e

For each edge incident at a vertex:
- *incoming_e* = a_bwd if this vertex is at the edge's tail, else a_fwd
- *outgoing_e* = a_fwd if this vertex is at the edge's tail, else a_bwd
- *total_incoming* = Σ_e incoming_e (sum over incident edges)

The new outgoing values become the next step's edge state. Each vertex updates locally; updates at all vertices are independent.

## Topology

No built-in topological invariants in the model's state. Plaquette flux can be *measured* by tracing wave amplitudes around a closed loop over time (e.g., the phase relationship between successive edges as a wave traverses), but it is a derived observable, not stored.

## Stability

**Unitary.** S is a unitary matrix for any N — eigenvalues on the unit circle, energy (Σ a²) conserves exactly per step. Unit time step is stable for any coordination with no normalization needed.

For N = 3 (hex):
- Reflection coefficient (diagonal): −1/3
- Transmission to each other edge: +2/3
- Energy: (1/3)² + 2·(2/3)² = 1/9 + 8/9 = 1 ✓

## Notes

- This is the **transmission-line scattering paradigm**, distinct from the bond-graph paradigm of Telegrapher. State lives on edges as wave amplitudes; vertices are coupling elements with no memory.
- Phase information is *implicit* in the time-history of amplitudes, not stored explicitly. To detect phase circulation around a hexagon, the simulation must run forward in time and the phase relationship is recovered from the temporal pattern.
- Reproduces grid/sim-maxwell exactly (this is its model). Therefore "fidelity to sim-maxwell" is trivially 100% for this candidate — the bridge to grid is the model itself.
- The trade-off vs. Telegrapher: clean per-step energy conservation in exchange for no per-vertex state. Topological invariants must be observed dynamically rather than stored.
- Single-phase clock means information ratchets through the lattice in one update per cycle, in contrast to the two-phase staggering of bond-graph models.
