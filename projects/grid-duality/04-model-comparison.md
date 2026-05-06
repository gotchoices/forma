# Chapter 4: Model comparison and verdict

## §1. The chapter's job

Run the tests from chapter 3 against the four candidate models from chapter 2, report the numbers, and identify which model best carries light on the substrate. Gravity is a substrate property — the graph Laplacian's Green's function on the hex graph gives log(r) potential and 1/r force, independent of which model runs on the lattice (test G1). The comparison therefore turns on the *dynamic* tests — stability, dispersion, Y-junction scattering, linearity — which probe how each model handles wave propagation, junction physics, and energy conservation.

## §2. Results table

A pass / fail / partial reading at a glance. Numbers are rounded; full output lives in `scripts/output/`.

| Test | Telegrapher | Normalized | RelCos-both | Scattering |
|---|---|---|---|---|
| **S1** 2D pulse, energy ratio after 100 steps | 45,586× — fail | 1.89× — pass | 0.96× — pass | 1.000× — exact |
| **S2** 2D wavefront, energy ratio after 80 steps | 17,076× — fail | 1.35× — pass | 2.05× — borderline | 1.000× — exact |
| **L1** 1D group velocity v_g(k) at k = π/2 | not tested (S-fail) | 0.528 (dispersive) | 0.998 (near-non-dispersive) | 1.000 (non-dispersive at every k) |
| **L2** Y-junction reflection / transmission (theory: 1/9, 4/9, 4/9) | not tested (S-fail) | 0.1145 / 0.4428 / 0.4428; +11.6% energy drift | 0.268 / 0.406 / 0.326; arms 1/2 asymmetric, sum = 0.73 (energy lost) | 0.1111 / 0.4444 / 0.4444; 0.0000% drift |
| **L3** Linearity v_AB vs v_A + v_B (target R² = 1) | not tested | R² = 1.0000, std = 0.000 | R² = 0.005, mean ratio 1.51 with std 14.5 (Dirichlet pins unstable) | R² = 1.0000, std = 0.002 |
| **G1** Substrate Laplacian solve (gravity from lattice graph) | applies | applies | applies | applies |
| **G2** Dynamics relaxes to substrate's static solution | not tested | yes — match R² = 1.000, force p = −1.017 | no — energy diverges 60,000× under Dirichlet pinning | partial — match R² = 0.998 by ranking, but force p = −0.628 (field stays localized) |

## §3. What each test revealed

### Stability (S1, S2)

Telegrapher is unstable at coord 3 with unit time step, as the CFL diagnosis predicts: the discrete wave equation amplifies by a factor √N per junction, and at N = 3 the divergence is fast (energy ratio ≳ 10⁴ within 100 steps). The 1/N normalization in Normalized fixes this by reducing the effective time step at each node, satisfying CFL at any coordination. RelCos-both passes by a different mechanism — the cos sum-to-zero property of three 120°-spaced edge angles at a coord-3 node is exactly the Kirchhoff conservation needed for stability under uniform fields. Scattering is stable by construction: its update is a unitary matrix at every vertex, and energy is conserved exactly per step.

### Light propagation (L1, L2)

Test L1 separates the models by dispersion. Normalized's group velocity drops monotonically with k — the standard leapfrog dispersion of a discrete wave equation. Scattering is perfectly non-dispersive: at every wavevector k tested, the wavepacket centroid moves at exactly v_g = 1.000. The reason is structural: in 1D every node has coord 2, where the scattering matrix S = (2/2)·J − I reduces to the swap matrix, so each amplitude propagates one site per step regardless of frequency. RelCos-both is also near-non-dispersive in 1D (v_g(k) is between 0.99 and 1.00 across the tested range), because in 1D every edge has angle θ = 0, the cos weighting reduces to cos(v_node) ≈ 1 for small dials, and the model behaves like a near-perfect right-mover. This passes L1 cleanly.

Test L2 separates the models more decisively. On a coord-3 Y-junction, matched-impedance scattering predicts R = −1/3, T = +2/3 per branch — energy fractions of 1/9, 4/9, 4/9. Scattering hits these to four decimals (0.1111 / 0.4444 / 0.4444) with literally zero energy drift over 90 steps. Normalized comes within 0.5% of the same fractions but accumulates +11.6% energy drift: the model is approximately correct on junction scattering but is not strictly unitary in the way Scattering is. The 11.6% drift comes from the way the 1/N factor interacts with non-uniform coordination (coord-2 along arms, coord-3 at the junction); on a uniform-coord lattice this would be smaller. RelCos-both *fails* L2 in two ways at once. First, the reflected fraction (0.27) is 2.4× the matched-impedance prediction. Second, the two transmission arms — geometrically symmetric under arm-1 ↔ arm-2 swap — receive different energy fractions (0.41 vs 0.33). The geometric symmetry is broken because the central node's dial direction v evolves during the scattering event, and the cos(θ_edge − v) weighting is not invariant under arm swap once v has rotated. The model also leaks ≈ 18% of the total system energy over the 90-step run, so the scattering is non-conservative as well as asymmetric. The Y-junction test is the precise place where RelCos-both's dial-aware update rule shows itself as incompatible with the matched-impedance light-carrier requirement.

### Linearity (L3)

Normalized and Scattering are linear with R² = 1.0000. Per-node standard deviations are 0.000 (Normalized) and 0.002 (Scattering). Superposition holds — required for any wave-equation interpretation, and required for gravity to add linearly across multiple sources. RelCos-both fails the test (R² = 0.005), but the failure is downstream of its Dirichlet-pinning instability rather than an intrinsic nonlinearity in the free-wave regime: the settled v_A and v_B fields it produces are not meaningful starting points for a superposition comparison, because the underlying dynamics has already diverged.

### Gravity (G1, G2)

The substrate test G1 confirms what grid/sim-gravity-2 already shows: solving the graph Laplacian directly on the hex lattice with Dirichlet pins gives log(r) potential and 1/r force law. Numerically, the analytical solve gives log fit slope −0.0743 with R² = 0.9999 and force-law exponent p = −1.0216 with R² = 0.9770 — clean log decay and clean 1/r decay. This emergence depends on the graph alone, not on any model's dynamics, so it applies equally to every candidate.

The dynamics-convergence check G2 splits the models. Normalized's static limit *is* the graph Laplacian: at a node where Σ s · i has equilibrated, the equation reduces to (M·Mᵀ·v)_node = 0, the same operator G1 inverts. So Normalized's damped dynamics relax to the same field G1 produces analytically, and the force-law exponent is reproduced (p = −1.017). RelCos-both's static limit is a nonlinear cos-weighted balance, not the standard Laplacian, and pinning a node fixes its dial direction, which breaks the cos sum-to-zero property the model depends on for stability — energy diverges by ×60,000 under Dirichlet pinning. Scattering has no node state to relax to a Dirichlet-pinned static configuration; the dynamic field around a pinned source stays localized near the pin (force p ≈ −0.6 instead of −1) because the model is a unitary wave equation, not a relaxation. This is not a flaw in Scattering — it is a category error in the test. For gravity, Scattering uses the substrate's graph Laplacian directly (G1), the same way grid/sim-gravity-2 does, separately from the dynamics that handle Maxwell.

## §4. Synthesis

Three of the four candidates fail something. Only Scattering fails nothing.

- **Telegrapher** fails stability at coord ≥ 3. It is kept as the baseline failure mode that motivates Normalized.
- **RelCos-both** is stable for free wave propagation and is even near-non-dispersive in 1D, but it fails in two distinct directions when probed more carefully. At a coord-3 Y-junction (test L2) it scatters with the wrong reflection coefficient (0.27 vs 1/9) and breaks the geometric arm-1 ↔ arm-2 symmetry because the central node's evolving dial direction enters the cos weighting. Under Dirichlet pinning (tests L3 and G2) it diverges — the dial-aware update rule loses the cos sum-to-zero property at pinned nodes. Both are structural problems, not tuning problems. The model is removed from the active set.
- **Normalized** passes everything that does not require strict unitarity. It is dispersive (test L1) — meaning short-wavelength waves travel slower than long-wavelength ones, the standard signature of a dispersive medium rather than vacuum. It is approximately matched-impedance at coord-3 junctions but not exactly, with non-trivial energy drift over many steps. Its dynamics happen to relax to the graph Laplacian — a nice property pedagogically, but redundant: the substrate test G1 already gives the Laplacian solution by direct linear algebra.
- **Scattering** passes the *light-propagation* tests cleanly. It is unitary by construction, exactly non-dispersive in the regimes tested, and meets the matched-impedance prediction to four decimals at coord-3 vertices. It does not relax to a Dirichlet-pinned static field under its own dynamics — its static limit is a wave equation, not a Laplacian — but gravity does not need the model's dynamics to do this work; gravity emerges from the substrate's graph Laplacian, computed by direct linear algebra (test G1, the same approach used by [grid/sim-gravity-2/run_scalar.py](../../grid/sim-gravity-2/run_scalar.py)). The "no static limit, by design" property is a feature of a wave equation, not a flaw, once gravity is understood as a substrate computation rather than a dynamics-relaxation outcome.

## §5. Verdict

**Scattering is the winning candidate.** Three reasons, in order of importance.

1. *Light carrier viability on the metrics.* Scattering's dispersion test gives v_g = 1.000 at every wavevector. Its Y-junction test reproduces matched-impedance theory to four decimals with literally zero energy drift. Its 2D-pulse and wavefront stability tests give energy ratios of 1.000× exact. Its superposition test gives R² = 1.0000. These are the cleanest possible signatures of a non-dispersive, energy-conserving, linear wave medium — and no other candidate matches them. The verdict is on the test results first; everything below is downstream.

2. *Naturalness — Scattering is the lattice's transmission-line network.* The model can be described in physically primitive terms: each node is an N-register processor (one register per incident edge, where a register is the meeting point of an edge end with a node — owned jointly); each edge is a two-ended transmission line; each clock cycle has an *inhale* (each node samples its registers, applies S = (2/N)·J − I, overwrites them) and an *exhale* (each edge swaps the values in its two registers). One exhale = one edge transit = the speed of light c on the lattice. The matrix S is not an arbitrary update rule — it is the unique solution to two physical constraints any junction must enforce (voltage continuity, Kirchhoff current conservation). Energy conservation is structurally obvious: the inhale is a local unitary, the exhale is a relabeling. Edge polarity is inert (registers are unordered). The "two values per edge" is what every 1D wave-carrier needs (two real degrees of freedom per spatial location); this closes the "two-channel cheating" concern definitively. Scattering is not a contrived discretization; it is what a transmission-line network looks like on a graph.

3. *Bridge to grid is downstream of (1).* Scattering happens to be the model used in [grid/sim-maxwell](../../grid/sim-maxwell/). The bridge to grid is therefore trivial in the sense that observable equivalence with sim-maxwell is built in. But the *win* is established by (1) and (2) — the metrics and the physical naturalness — independent of grid identity. If Scattering were not also sim-maxwell's model, it would still win on these grounds.

**Normalized** is the discrete wave equation in the v-i paradigm, regularized by 1/N to satisfy CFL stability at any coordination. It passes light-propagation tests approximately but not exactly (energy drift, dispersion). Its dynamics happen to relax to the substrate's graph Laplacian under Dirichlet pinning, which would be useful if gravity required a relaxation route — but grid's gravity story does not require that route; the substrate Laplacian solve is direct. So Normalized's static-limit-equals-Laplacian property is a redundant strength, not a unique one. It is preserved as a pedagogically clean v-i contrast, not as a competing winner.

**Telegrapher** and **RelCos-both** are documented failure modes. Telegrapher motivates the 1/N regularization that Normalized adds. RelCos-both is the cautionary tale about cos-weighted dial-aware update rules — promising in symmetry arguments, breaking under both Dirichlet pinning (the cos sum-to-zero condition fails) and coherent Y-junction scattering (the model is nonlinear and gauge-non-invariant under v → v + c, so the geometric arm-swap symmetry is broken at the junction).

A note on gravity. Both Normalized and Scattering live on the same lattice graph, so both *inherit* gravity from the substrate's graph Laplacian (test G1) — the substrate test is paradigm-neutral. The dynamics-convergence test G2 is informative about the model's relaxation behavior but is not gating: a model can be a perfectly good light carrier while having no relaxation-style static limit, since gravity is computed on the substrate directly. RelCos-both's energy divergence under Dirichlet pinning is a strike against it, but as a free-standing stability concern (the model loses conservation when its dial-direction symmetry is broken), not as a gravity-test failure.

## §6. What this verdict closes and what it leaves open

Closed by the test bench:

- *The model question.* Scattering is the lattice's dynamics.
- *The light-carrier viability question.* The hex lattice with Scattering dynamics passes every light-propagation test that matters: stability, dispersion-free propagation, matched-impedance scattering, linearity, energy conservation.
- *The "two values per edge feels like cheating" concern.* Under the register reading, the two values are at the edge's two physical ends — what every 1D wave-carrier needs to represent its instantaneous state, the same way position and velocity describe a mechanical oscillator. There is no parallel-channel doubling.
- *Edge polarity as a substrate primitive.* For Scattering, polarity is inert; the registers are unordered. Polarity is retained in the substrate as a labeling convention available to v-i models, not as a structural feature of the lattice graph.
- *The basic gravity-emergence question.* The graph Laplacian on the hex lattice produces log(r) potential and 1/r force, independent of the dynamic model. Gravity comes from the substrate, not from running Scattering forward in time.
- *The bridge to grid.* Scattering is sim-maxwell's model, so observable equivalence with sim-maxwell is built in. Note that the win in §5 is established on metric grounds first; the bridge identity is a downstream consequence.

Left open by the test bench:

- *3D extension.* The substrate is currently formalized in 1D and 2D hex. A 3D lattice with the same Scattering dynamics is structurally straightforward — the inhale (S = (2/N)·J − I) applies in any dimension, and the exhale is dimension-agnostic — but the geometry conventions for 3D edge orientation and per-edge displacement vectors are not pinned down.
- *Topological invariants under Scattering.* The natural invariants for Scattering live on edge cycles (paths of register-to-register propagation), not on node loops as in the v-i paradigm. The translation between these two homological setups is not yet worked out.
- *Bounded vs unbounded phase, and where charge enters.* Bounded phase (mod 2π on a node-level variable) was a feature of the v-i candidates and motivated their compactness story. Bounded phase is *not* required for either light propagation (Scattering does not have a phase variable) or gravity emergence (the substrate Laplacian solve and the entropic gravity story both work on unbounded fields). Bounded phase is motivated by **charge emergence** — U(1) gauge structure, winding numbers around closed loops, charge quantization — which is a downstream question, not a chapter-4 question.
- *Where in the wrap-promotion ladder α appears.* The conjecture is L3 (second-order wrap). Scattering supports the topological invariants needed to define the ladder; whether α appears at L3 specifically is not yet tested.

## §7. Closing pointer

Scattering is the model. Failed candidates (Telegrapher, RelCos-both) and deferred ones (Gauge, cos-weighted) remain documented in [models/](models/) but are not extended further.

The chapter sequence is summarized in the project [README](README.md).
