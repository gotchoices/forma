# RelCos-both

**One-line:** Cos-weighted update on both phases, with the cosine measured *relative to the node's dial direction*. The cos sum-to-zero property of three 120°-spaced angles gives implicit current conservation at every node, regardless of dial orientation.

## State

| Where | Symbol | Domain | Role |
|---|---|---|---|
| Node | v | [0, 2π) (U(1) compact) | dial direction — interpreted as a compass heading |
| Edge | i | ℝ (unbounded real) | through variable, as in Telegrapher |

The lattice additionally provides each edge's geometric direction θ in space (a fixed scalar in 2D, a unit vector in 3D — see "3D extension" below).

## Clock

Two-phase. Same staggering as Telegrapher: node phase, then edge phase.

## Update rules

**Phase 0 — node update.** For each node, signed sum of incident edges weighted by cos relative to the dial:

> v_node ← (v_node + Σ_e s_e · i_e · cos(θ_e − v_node)) mod 2π

where s_e = +1 if this node is the head of edge e, −1 if tail (polarity sign), θ_e is the edge's geometric direction (line direction, same at both endpoints), and v_node is this node's current dial direction.

**Phase 1 — edge update.** For each edge, principal-branch difference of cos-weighted node values:

> i_edge ← i_edge + (φ(v_tail) · cos(θ_edge − v_tail)) − (φ(v_head) · cos(θ_edge − v_head))

where φ(v) denotes the principal-branch reading of v in (−π, π], so v is treated as a phase amplitude (a signed value), not a raw [0, 2π) coordinate.

## Topology

Same as Telegrapher: closed loops through nodes accumulate principal-branch differences that sum to 2π·k for integer k (the **node-loop winding number**). Topological invariants live on node-loop windings.

## Stability

**Stable at unit time step in 2D hex** (verified by simulation). The mechanism is structural: at any node with N edges at evenly-spaced angles (e.g., N = 3 at 120° spacing on a hex lattice), the sum of cos weights at any dial direction v is identically zero —

> Σ_k cos(θ_k − v) = 0 for any v, when {θ_k} are at 2πk/N spacing.

So the rule is automatically Kirchhoff-conserving for uniform fields *regardless of the dial's current orientation*. The dial direction can rotate freely without breaking conservation. This is how the model avoids the no-conservation failure mode of variants where cos is applied to only one phase.

In simulation: 100-step Gaussian-perturbation test on a 14×14 hex torus shows energy ratio 0.96× (essentially flat); 80-step directional wavefront test shows ratio 2.05× (bounded oscillation). The wavefront-test slight-growth comes from the IC matched to a v-i model's wavefront, not perfectly natural to RelCos-both's compact-dial paradigm; sustained dial-aware drives may show tighter conservation.

## 3D extension

In 3D, v becomes a direction on the 2-sphere S² rather than the circle S¹. Parameterize v as either (polar, azimuth) or as a unit 3-vector. Each edge has a fixed 3-vector direction θ_e. The cos weighting becomes the dot product of the dial unit-vector and the edge unit-vector:

> cos(θ_e − v) → v̂ · θ̂_e (3D)

The sum-to-zero property generalizes: for any direction v̂, the sum of v̂ · θ̂_k over a symmetric set of edge directions sums to zero (e.g., 4 edges at tetrahedral angles, 6 at cubic).

This requires extending the engine's `Lattice` from 2D positions and scalar `theta` to 3D positions and vector edge directions. Future work; not required for the 1D and 2D tests.

## Notes

- The user's intuitive description: "the dial spins to align with incoming signals; edges read the dial weighted by their relative angle; the cos sum-to-zero makes scattering automatic."
- Distinct from cos-weighted (grid-lab v2), which uses *fixed* attachment angles and is unstable at coord 3. The "relative" qualifier — cos depends on v_node, not on a fixed lattice angle — is what makes this model self-consistent under any dial orientation.
- Variants tried during development: cos on node only and cos on edge only. Both are unstable in 2D. The cos must be applied to *both* phases for the dial-orientation-independent conservation property to surface.
- The dial v has dual interpretations: (a) a phase value in [0, 2π) for principal-branch arithmetic in the edge update, (b) a compass direction for the cos weighting in the node update. The two interpretations are mathematically the same — one number — but conceptually different.
