# Chapter 2: Candidate models

## §1. The chapter's job

Tour the candidate models that will be put through the test bench. Each candidate is a self-contained instantiation of the substrate from chapter 1 — a choice of *what state each primitive holds* and *what update rules govern it*. The full specifications live in [models/](models/); this chapter gives a one-page map.

There is no commitment in this chapter to which model is right. The comparison happens in chapter 4.

## §2. Two paradigms

The candidates fall into two paradigms by where they put their dynamical state.

### Across-and-through (v-i)

Inspired by bond-graph and transmission-line analogies. Each node carries an **across** variable (voltage-like, "level") and each edge carries a **through** variable (current-like, "flow"). The clock alternates two phases: nodes update from incident-edge flows; edges update from end-node level differences. Topological invariants live on closed loops through nodes — accumulated principal-branch differences sum to 2π·k for integer k (the **node-loop winding number**).

Three v-i candidates differ only in the node-update rule:
- **Telegrapher** — plain signed sum.
- **Normalized telegrapher** — signed sum divided by the node's coordination.
- **RelCos-both** — signed sum weighted by cos(θ_edge − v_node), and the edge phase is also cos-weighted.

The two-phase clock and the v ∈ [0, 2π) / i ∈ ℝ state structure are common to all three.

### Scattering (register / transmission-line network)

A network of N-register processors connected by two-ended transmission lines. Each node has one **register** per incident edge, where a register is the structural meeting point of an edge end with a node — owned jointly by both, contributing one real value to the lattice's state. A node of coordination N hosts N registers; an edge contributes two (one at each end node). The total state is exactly 2·|edges| real numbers.

The clock is two-phase: an **inhale** in which each node samples its registers, applies the scattering matrix S = (2/N)·J − I locally, and overwrites the registers; and an **exhale** in which each edge transmits its end values to one another, swapping the values in the two registers it connects. The inhale enforces junction physics (voltage continuity + Kirchhoff current conservation, which together uniquely determine S); the exhale is a pure relabeling. Each phase is unitary, so energy is conserved exactly per cycle.

The exhale duration sets the **speed of light** for the lattice: information moves at most one edge per cycle. Edge polarity is structurally inert under this model — the registers are unordered and neither phase reads polarity.

This is the model used in [grid/sim-maxwell](../../grid/sim-maxwell/), and the (a_fwd, a_bwd) labeling commonly seen there is an equivalent direction-by-direction relabeling of the registers.

## §3. Comparative table

A reading guide. Rows are model properties; columns are candidates.

| Property | Telegrapher | Normalized | RelCos-both | Scattering |
|---|---|---|---|---|
| Node state | v ∈ [0, 2π) | v ∈ [0, 2π) | v ∈ [0, 2π) | N registers per node (joint with edges) |
| Edge state | i ∈ ℝ | i ∈ ℝ | i ∈ ℝ | two registers per edge (joint with nodes) |
| Clock | two-phase | two-phase | two-phase | two-phase (inhale + exhale) |
| Node update | Σ s·i | (1/N)·Σ s·i | Σ s·i·cos(θ−v) | scatter S = (2/N)·J − I on registers |
| Edge update | (v_t − v_h)_pb | (v_t − v_h)_pb | cos-weighted Δv | swap end-register values |
| Static limit | graph Laplacian | graph Laplacian | nonlinear | wave equation (no relaxation) |
| Energy conservation | linear (approximate) | linear (approximate) | nonlinear | exact (unitary by construction) |
| Edge polarity used by dynamics? | yes (s_e = ±1) | yes (s_e = ±1) | yes (s_e = ±1) | no (registers unordered) |
| Gauge invariance under v → v + c | yes | yes | no | trivially (no v) |
| Lattice geometry needed | graph only | graph only | edge angles θ | graph only |
| Reference spec | [telegrapher.md](models/telegrapher.md) | [normalized.md](models/normalized.md) | [relcos-both.md](models/relcos-both.md) | [scattering.md](models/scattering.md) |

The "static limit" row is significant: a model whose v̇ = 0 condition reduces to the graph Laplacian inherits the lattice's harmonic-function behavior automatically. RelCos-both does not — its static condition is a nonlinear cos-weighted balance, distinct from the standard Laplacian. Scattering has no node state to relax to a static configuration; static fields, in the scattering paradigm, are computed on the substrate's graph Laplacian directly, separately from the dynamics.

## §4. Telegrapher — the baseline

The simplest v-i model: at each node, sum the signed flows on incident edges, add to the node's level, take mod 2π. At each edge, take the principal-branch difference of end-node levels, add to the edge's flow.

The model is stable in 1D under unit time step. In 2D it amplifies by a factor of order √N at every junction (where N is the node's coordination), so on a hex lattice with N = 3 it diverges within tens of steps. The standard CFL diagnosis applies: at coord N, the discrete wave equation requires Δt ≤ √(2/N) for stability with this particular discretization. Telegrapher uses Δt = 1, which exceeds the bound at any coord ≥ 3.

Telegrapher is kept as the baseline failure mode — the contrast that motivates the normalized variant. Spec: [models/telegrapher.md](models/telegrapher.md).

## §5. Normalized telegrapher

Telegrapher with one tweak: divide the node-update sum by N, the node's coordination. The 1/N factor reduces the effective time step at each node so that CFL is satisfied at any coordination, with unit time step everywhere.

The propagation speed is no longer 1 — group velocity drops below unity and varies with wavevector (standard leapfrog dispersion). On a hex lattice, the model is stable. Its static limit is the graph Laplacian, the same operator that defines harmonic functions on the lattice graph: at a node where v̇ = 0, the Σ s·i sum vanishes, which reduces to (M·Mᵀ·v)_node = 0 once edges have equilibrated.

Spec: [models/normalized.md](models/normalized.md).

## §6. RelCos-both

A variant motivated by a "compass dial" picture: each node's v is interpreted not just as a phase but as a heading, and each incident edge contributes to the node's update weighted by cos(θ_edge − v_node), where θ_edge is the edge's geometric direction. Both phases (node update and edge update) are cos-weighted in this way.

The model exploits the cos sum-to-zero property: for N edge directions evenly spaced by 2π/N, Σ_k cos(θ_k − v) = 0 for any v. This gives implicit current conservation at every regular junction, regardless of dial orientation. Free wave propagation in 2D is stable, with bounded oscillation.

Static-source / Dirichlet problems are a different story: pinning a node fixes its v, which removes the cos sum-to-zero property at the boundary, and the model destabilizes. This is documented in [models/relcos-both.md](models/relcos-both.md).

The lattice for RelCos-both must carry per-edge angles θ — additional geometric structure beyond the abstract graph.

## §7. Scattering

State lives in **registers**: one real value per docking of an edge end into a node. A node of coordination N has N registers; an edge contributes two registers (one at each end). Each register is owned jointly by an edge and a node — it is the structural meeting point of the substrate's two primitives, not a separate primitive. The total state is exactly 2·|edges| real numbers.

The clock is two-phase. **Inhale.** Each node samples its registers, applies the scattering matrix S = (2/N)·J − I locally, and overwrites the registers:

> r_i ← (2/N) · (r₁ + … + r_N) − r_i      for each register i at the node

S is the unique solution to two physical constraints at any junction — voltage continuity (all incident lines see the same potential) and Kirchhoff current conservation. It is not an arbitrary update rule; it is what those constraints require. S is unitary for any N, so the inhale preserves energy locally.

**Exhale.** Each edge swaps the values in its two registers (one at each end node), as if the value at one end has propagated across the edge body to the other end. One exhale = one edge transit; this defines the **speed of light** for the lattice. The exhale preserves energy trivially — it is a pure relabeling.

A full cycle is therefore unitary, and energy is conserved exactly per step.

Edge polarity is structurally inert under Scattering: the registers are unordered and neither phase reads polarity. This is the model used in [grid/sim-maxwell](../../grid/sim-maxwell/); the (a_fwd, a_bwd) labeling sometimes seen there is an equivalent direction-by-direction relabeling of the registers. Spec: [models/scattering.md](models/scattering.md).

## §8. Deferred and scrapped

Two further candidates were considered:

- **Gauge** — a compact gauge field on edges, real on nodes, with sin(A) coupling. Implementation requires more careful thought about the coupling form than the active candidates need. *Deferred until a later round if the active candidates leave open questions.* Spec: [models/gauge.md](models/gauge.md).
- **Cos-weighted (grid-lab v2)** — fixed-angle cos node update, where θ_edge is referenced from a fixed lattice axis (not from the node's dial direction). The cos-on-one-phase variant fails at coord 3: the cos sum at fixed angles does not have the sum-to-zero property in general, and the model diverges within tens of steps in 2D. *Scrapped.* The fail-mode is preserved in [models/cos-weighted.md](models/cos-weighted.md) for reference.

Two intermediate variants of the cos-relative idea — RelCos-node-only and RelCos-edge-only — were tried during early development and confirmed unstable. The "cos must apply to both phases" condition is the structural reason RelCos-both works where the partial variants don't; this is documented in [models/relcos-both.md](models/relcos-both.md).

## §9. Closing pointer

Four active candidates: Telegrapher, Normalized, RelCos-both, Scattering. Two paradigms: v-i and scattering. The substrate from chapter 1 supports all four. The test bench in chapter 3 defines what they are tested on, and chapter 4 reports the comparison.

The chapter sequence is summarized in the project [README](README.md).
