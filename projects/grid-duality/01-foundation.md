# Chapter 1: Foundation

## §1. The chapter's job

Establish the **lattice substrate** for grid-duality: the structural elements every candidate model shares. The substrate is a graph of two primitive types — nodes and edges — with a polarity convention on edges, an orientation convention across the lattice, and a master-clock concept governing discrete updates.

The chapter deliberately stops there. **What state each primitive holds and what update rules govern its dynamics is not a foundational question — it is a model-specific question.** Different candidate models make different choices, and the choice between them is settled empirically by the test bench (chapter 3) and the comparison (chapter 4).

This chapter contains no update rules and no commitments to compact-vs-real state, single-vs-two-phase clock, or one paradigm of dynamics over another. Those live in the per-model specifications under [models/](models/) and are surveyed in chapter 2.

## §2. Nodes and edges

The lattice has two primitive types:

- **Node** — a 0D vertex. A point in the lattice graph at which edges meet. Each node holds some state, but *what* state is model-dependent.
- **Edge** — a 1D directed segment connecting two nodes. Each edge holds some state, again model-dependent.

A lattice is fully specified by:
- Its set of nodes,
- Its set of edges (each edge connecting two nodes),
- Each edge's polarity (which endpoint is the tail, which is the head).

Nodes and edges are the only structural objects; everything else (loops, plaquettes, sheets, wraps) is a derived configuration of them.

## §3. Edge polarity and orientation

Every edge has a fixed **polarity**: a tail and a head, set when the edge is placed in the lattice and never changing afterward. Polarity is structural and does not update under any model. Its role is to give each edge a directional sense, so that at any node the edge is either *incoming* (its head is here) or *outgoing* (its tail is here).

Across the lattice, edge polarities are standardized in a **common direction**:

- **1D linear array** — every edge points rightward. Tail at the left endpoint, head at the right.
- **2D hex sheet** — three lattice directions correspond to the three axes of hexagonal symmetry. Each edge falls into one of these direction classes; within each class, all edges are oriented uniformly. The choice of which orientation per class is conventional but consistent across the lattice.
- **3D lattices** — orientation conventions are sketched only when 3D geometry is introduced later. Nothing in the early chapters depends on this being settled.

Standardization gives every node enough *local* information — for each incident edge, whether its tail is here or its head is here — to apply any model's update rule from the edge's polarity alone, without consulting a sublattice label or a global orientation map. It also lets the project state propagation conventions cleanly across dimensions.

The choice of common-direction pattern is a convention, not a derivation. Different choices produce equivalent dynamics up to overall edge-amplitude sign.

## §4. The master clock

The lattice evolves under a **master clock** — a discrete update scheduler. At each clock cycle, primitives apply their update rules. The clock is what makes the model dynamical.

The number of phases per cycle (one or two) and the order of updates within a cycle (nodes-first vs. edges-first vs. all-at-once) are **model-dependent**:

- Two-phase models (e.g., Telegrapher) alternate node updates and edge updates on consecutive phases. The two-phase staggering keeps node and edge updates causally separated — at any moment, only one primitive type is active.
- Single-phase models (e.g., Scattering) do all updates in one shot per cycle; a unitary or near-unitary update at vertices is the structural reason this can be stable.

The substrate posits *that there is a clock* and *that a clock cycle is the lattice's fundamental temporal grain*. The specific structure of the cycle is left to each candidate.

## §5. What's foundational and what's per-model

To make the substrate-vs-model split explicit:

### Foundational (this chapter)

- The lattice is a graph of nodes connected by directed edges.
- Each edge has a fixed polarity (tail and head).
- Edge polarities are standardized in a common direction across the lattice (1D rightward, 2D hex three-direction, 3D deferred).
- A master clock drives discrete dynamics; one clock cycle is the temporal grain.

### Per-model (chapter 2 and [models/](models/))

- What state each node holds (a single scalar? a phase ∈ U(1)? a real ∈ ℝ? nothing at all?).
- What state each edge holds (one value? two? compact or unbounded?).
- The clock-phase structure (one phase per cycle? two? more?).
- The update rules at nodes and edges.
- Whether topological invariants (winding numbers, plaquette flux) live on node loops or edge cycles.

Because the substrate fixes only the structural skeleton, every candidate model is a self-consistent instantiation of it. The candidates differ in their choices of state and rules, and chapter 4's comparison decides which choice best reproduces the dynamics grid is expected to support.

## §6. Closing pointer

The substrate is now stated. Per-model details live in [models/](models/), the candidate-model tour is in chapter 2, the test bench is in chapter 3, and the comparison verdict is in chapter 4. Chapters 5 onwards build on the winning model.

The chapter sequence is summarized in the project [README](README.md).
