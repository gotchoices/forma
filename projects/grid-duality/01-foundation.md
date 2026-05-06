# Chapter 1: Foundation

## §1. The chapter's job

Establish the **lattice substrate** for grid-duality: the structural elements every candidate model shares. The substrate is a graph of two primitive types — nodes and edges — with a polarity convention on edges, an orientation convention across the lattice, and a master-clock concept governing discrete updates.

The chapter deliberately stops there. **What state each primitive holds and what update rules govern its dynamics is not a foundational question — it is a model-specific question.** Different candidate models make different choices, and the choice between them is settled empirically by the test bench (chapter 3) and the comparison (chapter 4).

This chapter contains no update rules and no commitments to compact-vs-real state, single-vs-two-phase clock, or one paradigm of dynamics over another. Those live in the per-model specifications under [models/](models/) and are surveyed in chapter 2.

## §2. Nodes and edges

The lattice has two primitive types:

- **Node** — a vertex in the lattice graph. Edges meet at nodes. *What* state a node holds — a single scalar, multiple scalars, internal spatial structure (e.g., angular attachment information for incident edges), or no state at all — is model-dependent.
- **Edge** — a connection between two nodes. *What* state an edge holds — a single scalar, a pair of values at its two ends, or something else — is also model-dependent.

A lattice is fully specified by:
- Its set of nodes,
- Its set of edges (each edge connecting two nodes).

Nodes and edges are the only structural objects; everything else (loops, plaquettes, sheets, wraps) is a derived configuration of them. Whether the lattice carries any *additional geometric structure* — for instance, the angular positions of edges incident at each node, useful only to models like cos-weighted that read those angles — is a property of the lattice's spatial embedding, separate from the abstract graph.

### The register

Some models naturally locate their state at the *meeting point* between an edge end and a node — neither inside the node nor inside the edge but at the docking between them. We call this meeting point a **register**. A register is the structural element formed where one end of an edge docks into a node:

- An edge contributes two registers (one at each end).
- A node hosts one register per incident edge.
- A register holds whatever value the model puts there (typically a single scalar).

The register is *not* a third primitive — it is a derived structural element built from the substrate's existing two primitives, the way an edge of a polyhedron is built from two of its faces. Models that read register state include the Scattering model in chapter 2, where the registers are the entirety of the lattice's state. Models that locate state purely on nodes or purely on edges (such as the v-i candidates) do not need the register concept; for those models the register reduces to a node-edge interaction without separate identity.

## §3. Edge polarity and orientation

Some models read a per-edge **polarity** — a designation of one endpoint as the tail and the other as the head — and use it as a sign in their update rules. Polarity is paradigm-specific:

- The **v-i paradigm** (Telegrapher, Normalized, RelCos-both) uses polarity load-bearingly: at every incident edge, the node update reads s_e = +1 (head here) or s_e = −1 (tail here) and forms a signed sum.
- The **register / scattering paradigm** does not use polarity. Each edge's two registers are unordered, and neither the inhale (local register scatter) nor the exhale (register swap) reads which end is "tail." On the Scattering model, polarity is inert.

Polarity is therefore a *labeling convention* the substrate makes available, not a structural primitive every model has to honour.

Across the lattice, when polarity is used, it is standardized in a **common direction**:

- **1D linear array** — every edge points rightward. Tail at the left endpoint, head at the right.
- **2D hex sheet** — three lattice directions correspond to the three axes of hexagonal symmetry. Each edge falls into one of these direction classes; within each class, all edges are oriented uniformly. *Caveat:* the bipartite A → B orientation used in the engine implementation gives every A-node all-outgoing edges (s_e = −1 throughout the node-update sum) and every B-node all-incoming (s_e = +1 throughout). The two sublattices therefore play structurally asymmetric roles in any v-i model — a property of this particular bipartite convention rather than of the hex geometry. Other orientation choices (for instance, mixed orientations within each direction class) would not have this asymmetry.
- **3D lattices** — orientation conventions are sketched only when 3D geometry is introduced later. Nothing in the early chapters depends on this being settled.

The choice of common-direction pattern is a convention, not a derivation. For models that *do* read polarity, different choices produce equivalent dynamics up to overall edge-amplitude sign. For models that *do not* read polarity (Scattering), the choice has no dynamical content.

## §4. The master clock

The lattice evolves under a **master clock** — a discrete update scheduler. At each clock cycle, primitives apply their update rules. The clock is what makes the model dynamical.

The number of phases per cycle (one or two) and the order of updates within a cycle (nodes-first vs. edges-first vs. all-at-once) are **model-dependent**:

- Two-phase models (e.g., Telegrapher) alternate node updates and edge updates on consecutive phases. The two-phase staggering keeps node and edge updates causally separated — at any moment, only one primitive type is active.
- Single-phase models (e.g., Scattering) do all updates in one shot per cycle; a unitary or near-unitary update at vertices is the structural reason this can be stable.

The substrate posits *that there is a clock* and *that a clock cycle is the lattice's fundamental temporal grain*. The specific structure of the cycle is left to each candidate.

## §5. What's foundational and what's per-model

To make the substrate-vs-model split explicit:

### Foundational (this chapter)

- The lattice is a graph of nodes connected by edges.
- Edge polarity is a labeling convention the substrate makes available; whether a model uses it is paradigm-specific.
- The register (where an edge end docks into a node) is a derived structural element, available to models that locate state at the meeting point.
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
