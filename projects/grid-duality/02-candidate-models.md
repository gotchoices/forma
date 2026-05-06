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

### Scattering (a-fwd / a-bwd)

Inspired by sim-maxwell's vertex-scattering construction. Nodes hold no state; each edge carries a pair (a_fwd, a_bwd) — the traveling-wave amplitudes in the tail→head and head→tail directions. The clock is single-phase: at each step, every vertex applies a scattering matrix S = (2/N)·J − I to its incoming amplitudes, producing the outgoing amplitudes. Energy is conserved exactly per step (S is unitary). Topological invariants live on edge cycles, not node loops.

This is the model used in [grid/sim-maxwell](../../grid/sim-maxwell/).

## §3. Comparative table

A reading guide. Rows are model properties; columns are candidates.

| Property | Telegrapher | Normalized | RelCos-both | Scattering |
|---|---|---|---|---|
| Node state | v ∈ [0, 2π) | v ∈ [0, 2π) | v ∈ [0, 2π) | none |
| Edge state | i ∈ ℝ | i ∈ ℝ | i ∈ ℝ | (a_fwd, a_bwd) ∈ ℝ² |
| Clock | two-phase | two-phase | two-phase | single-phase |
| Node update | Σ s·i | (1/N)·Σ s·i | Σ s·i·cos(θ−v) | (vertex scatter) |
| Edge update | (v_t − v_h)_pb | (v_t − v_h)_pb | cos-weighted Δv | tail/head amplitude swap |
| Static limit | graph Laplacian | graph Laplacian | nonlinear | not applicable (no node state) |
| Energy conservation | linear (approximate) | linear (approximate) | nonlinear | exact (unitary by construction) |
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

State on edges only, two amplitudes per edge: (a_fwd, a_bwd). At each vertex, the new outgoing amplitudes are determined from the incoming ones by

> outgoing = (2/N) · total_incoming − incoming

which is the matrix S = (2/N)·J − I applied to the incoming-amplitude vector. S is unitary, so total energy 0.5·Σ (a_fwd² + a_bwd²) is conserved exactly per step, with no roundoff drift in principle.

The clock is single-phase: every vertex updates simultaneously per cycle, swapping outgoing into the neighboring edges' incoming slots. No node state, no two-phase staggering.

This is the model used in [grid/sim-maxwell](../../grid/sim-maxwell/), and it sits at the heart of the "bridge to grid" question. Spec: [models/scattering.md](models/scattering.md).

## §8. Deferred and scrapped

Two further candidates were considered:

- **Gauge** — a compact gauge field on edges, real on nodes, with sin(A) coupling. Implementation requires more careful thought about the coupling form than the active candidates need. *Deferred until a later round if the active candidates leave open questions.* Spec: [models/gauge.md](models/gauge.md).
- **Cos-weighted (grid-lab v2)** — fixed-angle cos node update, where θ_edge is referenced from a fixed lattice axis (not from the node's dial direction). The cos-on-one-phase variant fails at coord 3: the cos sum at fixed angles does not have the sum-to-zero property in general, and the model diverges within tens of steps in 2D. *Scrapped.* The fail-mode is preserved in [models/cos-weighted.md](models/cos-weighted.md) for reference.

Two intermediate variants of the cos-relative idea — RelCos-node-only and RelCos-edge-only — were tried during early development and confirmed unstable. The "cos must apply to both phases" condition is the structural reason RelCos-both works where the partial variants don't; this is documented in [models/relcos-both.md](models/relcos-both.md).

## §9. Closing pointer

Four active candidates: Telegrapher, Normalized, RelCos-both, Scattering. Two paradigms: v-i and scattering. The substrate from chapter 1 supports all four. The test bench in chapter 3 defines what they are tested on, and chapter 4 reports the comparison.

The chapter sequence is summarized in the project [README](README.md).
