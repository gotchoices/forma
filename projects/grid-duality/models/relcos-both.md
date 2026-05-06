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

**Failure mode: Dirichlet pinning.** When source and sink nodes are pinned to constant values (the gravity-style static-field test), RelCos-both is *unstable*: energy diverges 60,000× over 800 steps and the time-averaged field bears no resemblance to the analytical Laplacian solution. The likely cause is that the pinned dial directions break the cos sum-to-zero property at the boundary nodes — at a pinned node the dial is held fixed instead of relaxing, so the implicit conservation no longer applies. Free-wave propagation is fine; static-source / static-defect problems are not. This disqualifies RelCos-both for gravity-style emergence tests.

## Bounded vs unbounded phase

The model inherits Telegrapher's compact U(1) phase by default — v lives in [0, 2π) with mod 2π applied each step and a principal-branch reduction in the edge update. Setting `wrap_node = False` on an instance turns v into an unbounded ℝ variable. The test [scripts/test_unbounded_phase.py](../scripts/test_unbounded_phase.py) probes whether the wrap is what makes the cos sum-to-zero conservation work, or whether it is dynamically inert in stable regimes.

Result for RelCos-both: two probes.

| Variant | 2D pulse, 100 steps (energy ratio) | Dirichlet-pinned, 800 steps (peak energy) |
|---|---|---|
| wrap_node=True (default) | 0.96× (stable) | ≈ 7 × 10⁴ (diverges) |
| wrap_node=False | 0.96× (stable, identical) | overflow to inf |

Two facts come out of this:

- *In the stable free-wave regime, the wrap is invisible.* The bounded and unbounded versions are bit-identical because v stays small enough that mod 2π never fires. The cos sum-to-zero conservation is doing all the work; the wrap is "armed but not firing."
- *Under Dirichlet pinning, the wrap is a soft cap on a divergence the model already has.* Without the wrap, the energy accumulation explodes to numerical infinity rather than to "merely" 70,000× the initial value. The wrap doesn't fix the failure — pinning still breaks the cos sum-to-zero condition — but it bounds the magnitude. As with Telegrapher, the wrap is a symptom-suppressor here, not a stabilizer.

The user's hypothesis that the wrap discards winding entropy and thereby enables thermodynamic-style cooling is not borne out by these probes. RelCos-both has no relaxation behavior in any regime tested; whether v is wrapped or unbounded changes only the numerical scale of the failures. Cooling in the v-i family, where it appears, comes from damping plus a static-limit-equals-Laplacian property (Normalized) — neither of which RelCos-both has.

## 3D extension

In 3D, v becomes a direction on the 2-sphere S² rather than the circle S¹. Parameterize v as either (polar, azimuth) or as a unit 3-vector. Each edge has a fixed 3-vector direction θ_e. The cos weighting becomes the dot product of the dial unit-vector and the edge unit-vector:

> cos(θ_e − v) → v̂ · θ̂_e (3D)

The sum-to-zero property generalizes: for any direction v̂, the sum of v̂ · θ̂_k over a symmetric set of edge directions sums to zero (e.g., 4 edges at tetrahedral angles, 6 at cubic).

This requires extending the engine's `Lattice` from 2D positions and scalar `theta` to 3D positions and vector edge directions. Future work; not required for the 1D and 2D tests.

## Notes

- The user's intuitive description: "the dial spins to align with incoming signals; edges read the dial weighted by their relative angle; the cos sum-to-zero makes scattering automatic."
- Distinct from cos-weighted (grid-lab v2), which uses *fixed* attachment angles and is unstable at coord 3. The "relative" qualifier — cos depends on v_node, not on a fixed lattice angle — is what makes this model self-consistent under any dial orientation.
- Variants tried during development: cos on node only and cos on edge only. Both are unstable in 2D. The cos must be applied to *both* phases for the dial-orientation-independent conservation property to surface.
- The dial v has dual interpretations: (a) a phase value in [0, 2π) for principal-branch arithmetic in the edge update, (b) a compass direction for the cos weighting in the node update. The values are mathematically the same number, but the dynamics depends on which interpretation is in force when v grows: the edge update treats v as a phase amplitude (via φ(v) in (−π, π]), while the node update treats v as a heading (via cos(θ − v)). The two interpretations agree in the linear small-v regime but diverge nonlinearly when v rotates substantially under driving.

## Symmetries

### v=0 init implies a preferred direction

The default `init_state` returns v = 0 on every node, inherited from Telegrapher. Under the compass-dial interpretation, this means *every dial points along the +x axis* (the zero of θ in 2D). The lattice has a built-in preferred direction in vacuum, which is structurally suspicious for a model that claims to support isotropic propagation. A randomized-v init (each node's v uniform on [0, 2π)) would be a more honest "no preferred direction" starting state, but has not been tested. The default-IC bias is not addressed by any test in chapter 3.

### Gauge non-invariance under v → v + c

A model with a "compass dial" interpretation should be invariant under a global rotation of all dials by the same constant c (no preferred zero of v). RelCos-both is *not* invariant under v → v + c. Two reasons, both visible in the edge update:

- **The cos factor depends on the absolute angle.** cos(θ − v − c) ≠ cos(θ − v) in general; it equals cos(θ − v) only when c is a multiple of 2π.
- **The principal-branch reduction is non-linear in c.** φ(v + c) is not equal to φ(v) + c — the wrap modulates the amplitude factor in a way that depends on the absolute value of v.

So the dynamics has a *preferred zero of v*, even though the compass-dial picture would suggest otherwise. This is the structural reason the L3 superposition test fails so badly even in the linearized regime: the model's response depends on the absolute value of v, not just on differences. The other v-i candidates (Telegrapher, Normalized) *are* invariant under v → v + c, since their dynamics depend only on differences of v and on i.

The non-invariance is a real symmetry-structure problem with the compass-dial interpretation: if v is genuinely a direction, the dynamics should not care which direction is called "zero."
