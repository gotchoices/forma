# Chapter 3: Test bench

## §1. The chapter's job

Define what each candidate model is tested on. The test bench has to do three things:

1. **Translate paradigm-neutral inputs** into each model's native state, so a "Gaussian pulse" or "right-moving wavepacket" means the same physical configuration in v-i form (Telegrapher / Normalized / RelCos-both) and in scattering form (Scattering).
2. **Probe the lattice as a light carrier**: stable, near-non-dispersive wave propagation; matched-impedance scattering at coord-3 vertices; superposition.
3. **Probe the lattice as a gravity carrier**: log(r) potential and 1/r force decay around a pinned defect, the 2D analog of Newton.

A small but important distinction runs through the chapter. Light is a *dynamic* phenomenon — it requires running the model's update rule and watching waves propagate. Gravity, in the way [grid/sim-gravity-2](../../grid/sim-gravity-2/) demonstrates it, is a *substrate* phenomenon — it is computed by solving the graph Laplacian on the lattice directly, without running any model's dynamics. The light tests therefore depend on the model; the gravity test depends on the lattice graph alone (with optional dynamics-convergence checks per model).

All test scripts live in [scripts/](scripts/) and produce output under `scripts/output/`.

## §2. Substrate

All tests run on one of three lattices:

- **1D periodic ring** — n nodes connected by n right-pointing edges, one wraparound. Used for clean wave propagation and dispersion measurements where 2D effects would muddy the signal. Constructor: `make_1d_periodic(n)`.
- **2D hex torus** — nx × ny unit cells, two sublattices A and B per cell, three edges per A-node pointing to neighboring B-nodes. Periodic in both lattice directions. Coord 3 at every node, so every node is a Y-junction. Constructor: `make_2d_hex_torus(nx, ny)`.
- **Y-tree** — three linear arms of `arm_length` nodes meeting at a central coord-3 node. Used to isolate scattering at a single coord-3 vertex. Constructor: `make_y_tree(arm_length)`.

The first two are periodic and have no boundary; the Y-tree has free ends, which the wavepacket tests take care not to reach within the simulation window.

## §3. Signal translation between paradigms

A test specifies an initial configuration in physically meaningful terms — for instance, "a Gaussian-modulated cosine wavepacket of carrier wavevector k centered at position x0, moving in direction +x." The test bench translates this into each model's native state:

### v-i paradigm (Telegrapher / Normalized / RelCos-both)

A 1D right-moving wavepacket sets `v(x) = A · exp(−(x − x0)²/2σ²) · cos(k(x − x0))` on every node and `i(x_edge) = v(x_edge)` on every edge (matching the right-mover relation `i = v` for a unit-impedance line). A left-moving wavepacket flips the i sign. A 2D directional wavepacket projects the node-coordinate onto the propagation direction k̂, computes the same Gaussian-cosine, and sets per-edge i = v · cos(θ_edge − direction) so that the through variable aligns with the propagation direction at each edge.

### Scattering paradigm

The same wavepacket maps to traveling-wave amplitudes per edge:

> a_fwd = (v + i) / 2,  a_bwd = (v − i) / 2

For a right-mover (v = i), this gives a_fwd = v, a_bwd = 0 — all the energy is in the forward channel. For a left-mover (v = −i), a_fwd = 0 and a_bwd = v.

Both translations preserve the same physical wavepacket: same total energy, same propagation direction, same envelope shape. The dispatch lives in each test script's initialization function (`init_directional_wavefront`, `init_packet_1d`, `init_inbound_packet`).

For pinning a node to a fixed value (Dirichlet boundary condition, used in the gravity test): in the v-i paradigm, simply set `v[idx] = value` each step. In the scattering paradigm, set `a_fwd = a_bwd = value/2` on every edge incident to the pinned node, which makes the node-equivalent observable `(a_fwd + a_bwd)` equal to `value`. The scattering interpretation of Dirichlet pinning is more constrained than the v-i interpretation — this matters for the dynamics-convergence check in §7.

## §4. Stability tests

### Test S1 — 2D Gaussian pulse

A localized Gaussian perturbation at the centre of a 14×14 hex torus. Run for 100 steps. Track total energy.

- **Pass condition**: energy ratio (final / initial) stays bounded near unity. A model that amplifies waves at junctions will diverge within tens of steps.
- **What it diagnoses**: CFL stability at coord 3.
- **Script**: [scripts/test_2d_pulse.py](scripts/test_2d_pulse.py).

### Test S2 — 2D directional wavefront

A Gaussian-enveloped cosine launched in a chosen direction on a 20×12 hex torus. Run for 80 steps. Track wavefront propagation and total energy.

- **Pass condition**: bounded energy and recognizable wavefront shape (no spurious dispersion or amplification).
- **What it diagnoses**: anisotropy, directional stability, and wavefront integrity over many junctions.
- **Script**: [scripts/test_2d_wavefront.py](scripts/test_2d_wavefront.py).

## §5. Light-carrier tests

### Test L1a — 1D dispersion / group velocity (coord 2)

Sweep the carrier wavevector k from 0.1 to ~π on a 256-node ring. For each k, launch a Gaussian wavepacket, track the envelope centroid over 80 steps via the circular-mean trick (z = Σ |v|² · e^{i·2π x/n}), and linear-fit centroid-vs-step to extract the group velocity v_g(k).

- **Reference**: a non-dispersive medium gives v_g(k) = c constant.
- **What it diagnoses**: dispersion of the model on a coord-2 lattice. Note: at coord 2, the Scattering matrix S = (2/2)·J − I reduces to a swap, so this test is a pure transport probe and does not exercise junction scattering — the L1b coord-3 test below is the more demanding probe.
- **Script**: [scripts/test_1d_dispersion.py](scripts/test_1d_dispersion.py).

### Test L1b — 2D dispersion / group velocity (coord 3)

On a 40×40 hex torus, launch a directional Gaussian-modulated cosine wavepacket along +x. Project each node's position onto the propagation axis, take the |v|²-weighted centroid, and linear-fit centroid-vs-step over a window before any periodic-wraparound effect. Sweep k.

- **Reference**: a coord-3 lattice with bounded dispersion gives v_g(k) ≈ constant within ≈ 20% spread; perfect non-dispersion is not expected, since the Y-junction scattering at every node introduces some k-dependence in any model whose scattering matrix is not the trivial swap.
- **What it diagnoses**: dispersion under realistic hex-lattice scattering. Scattering's coord-2 perfect non-dispersion (test L1a) is a special-case artifact; this test confirms whether the model still carries waves of different wavelengths at *comparable* speeds when junction scattering is real.
- **Script**: [scripts/test_2d_dispersion.py](scripts/test_2d_dispersion.py).

### Test L2 — Y-junction reflection / transmission

A Y-tree with three 60-node arms meeting at one coord-3 vertex. A Gaussian wavepacket is launched on arm 0, travels inward, scatters at the junction, and clears into the other arms. Per-arm energy is measured at every step.

*Matched impedance* in this context is the transmission-line analog: when N identical lossless lines meet at a junction, voltage continuity (all incident lines see the same potential) and Kirchhoff current conservation uniquely determine how an inbound wave splits. For N lines, R = (2 − N)/N and T = 2/N per branch. At N = 3 this gives R = −1/3, T = +2/3, energy fractions R² = 1/9 reflected and T² = 4/9 per transmitted branch (total Σ = 1, energy conservation). The same coefficients arise in acoustic-network and microwave-network analysis.

- **Reference**: matched-impedance scattering at coord N = 3 gives R² = 1/9, T² = 4/9 each. Both v-i and scattering paradigms predict these in the matched-impedance limit; this is the canonical test for whether a model treats junctions correctly.
- **What it diagnoses**: junction-level energy flow — the structural property that makes a hex lattice (every node coord 3) a viable light carrier.
- **Script**: [scripts/test_y_junction.py](scripts/test_y_junction.py).

### Test L3a — Linearity / superposition under Dirichlet pinning

On a 25×25 hex torus, three Dirichlet-pinned configurations: source A only; source B only; both A and B. After running each to a settled state under small damping, compare the field v_AB to the sum v_A + v_B over the unpinned interior.

- **Reference**: a linear medium satisfies v_AB = v_A + v_B exactly. Per-node correlation and rescaled-fit R² near 1 confirm linearity; deviation diagnoses nonlinearity in the update rule.
- **What it diagnoses**: linear superposition under boundary-driven static fields. Failures here can indicate either intrinsic nonlinearity in the update rule *or* downstream effects of Dirichlet-pinning instability — see L3b for the disambiguating test.
- **Script**: [scripts/test_2d_superposition.py](scripts/test_2d_superposition.py).

### Test L3b — Free-wave superposition (no pins)

Two Gaussian-modulated cosine wavepackets launched in opposite directions on a 20×20 hex torus, no Dirichlet pinning, no damping, 60 steps. Three independent runs: A only; B only; both A and B with initial state set to the additive sum of A's and B's initial states. Compare v_AB(t) to v_A(t) + v_B(t) per step.

- **Reference**: a linear update rule gives v_AB = v_A + v_B at every step, to machine precision.
- **What it diagnoses**: intrinsic nonlinearity of the update rule, separated from boundary-condition effects. Together with L3a, this distinguishes "nonlinear in vacuum" from "nonlinear only when boundary-pinned."
- **Script**: [scripts/test_2d_freewave_superposition.py](scripts/test_2d_freewave_superposition.py).

### Test L4 — Dial-aware IC fair-shake (RelCos-both only)

The standard IC translation in §3 above treats v as a wave amplitude (v(x) = A·env·cos(k·x), i matched). RelCos-both's compass-dial interpretation, however, treats v as a *heading*. A natural alternative IC under that interpretation is v = constant (the direction of intended motion) and i alone carrying the wave envelope. This test reruns the wavefront and Y-junction probes for RelCos-both with both ICs to check whether the model's failures are intrinsic or specific to the v-amplitude IC.

- **Reference**: if a model performs comparably under both ICs, the failures are intrinsic. If the dial-aware IC dramatically improves the result, the v-amplitude IC was unfair.
- **What it diagnoses**: whether RelCos-both's L2 / L3 failures are bench artifacts.
- **Script**: [scripts/test_relcos_dial_ic.py](scripts/test_relcos_dial_ic.py).

## §6. Gravity test — substrate part

### Test G1 — graph Laplacian solve (paradigm-neutral)

On a 25×25 hex torus, a source node is pinned to v = +0.3 at the centre, and a sink ring (all nodes at distance ≥ 9.0) is pinned to v = 0. Solve the graph Laplacian system L_ff · v_free = −L_fc · v_fixed by direct sparse linear algebra. Fit the resulting field to log(r) potential and r⁻¹ force.

- **Reference**: in continuum 2D, the Laplacian Green's function around a localized source decays as log(r), giving a force gradient that decays as 1/r. The 2D analog of Newton.
- **What it diagnoses**: whether the lattice graph itself supports gravitational behavior. This test runs on the substrate alone — no model dynamics are involved. It mirrors the static solve in [grid/sim-gravity-2/run_scalar.py](../../grid/sim-gravity-2/run_scalar.py).
- **Script**: Part A of [scripts/test_2d_static_field.py](scripts/test_2d_static_field.py).

The substrate test is the gravity-emergence claim. Any candidate model that lives on this lattice inherits gravity for free, by computing the static Laplacian directly when needed (the same way grid does).

## §7. Gravity test — dynamics-convergence part

### Note on the paradigm-dependence of "pinning"

"Pin v on a node at value V" sounds paradigm-neutral but is not. The bench has to choose one interpretation per model, and the choices differ in physical content:

- **v-i Telegrapher / Normalized.** Pinning v means *fixing the across variable at the node*, the natural Dirichlet boundary condition for a node-level scalar — like grounding a node in a circuit. The through variable i on incident edges is free.
- **RelCos-both.** Pinning v means fixing the *dial direction* at that node — a stronger constraint, since the cos(θ − v) factor in the update sees a frozen v while neighboring nodes' v evolves. This breaks the cos sum-to-zero condition at the boundary, which is the structural cause of RelCos-both's pinning instability.
- **Scattering.** No node state exists in the model, so "pinning v" has no direct meaning. The bench uses `a_fwd = a_bwd = V/2` on every incident edge of the pinned node, making the node-equivalent observable `(a_fwd + a_bwd)` equal to V. This is one of several possible interpretations (e.g., one could pin only the *outgoing* amplitudes from the node, or pin some other linear combination), and choosing a different one would change G2's outcome for Scattering.

Conclusion: G2 is not the same test across paradigms. Within a paradigm it tests a well-defined property; across paradigms it should be read as "each model's response to *its* most natural Dirichlet-pinning interpretation," which is informative but not paradigm-neutral.

### Test G2 — does each model relax to the substrate's static solution?

Same Dirichlet pins as test G1, but instead of solving the graph Laplacian directly, run each model's dynamic update rule for 800 steps with a small damping factor (0.02 per step on the through variable). Time-average the field over the last quarter of the run. Compare to the static solution from G1: log fit, force fit, per-node rescaled R².

- **Pass condition**: the dynamic-averaged field matches the static solution shape (rescaled R² near 1, force exponent near −1).
- **What it diagnoses**: whether the model's dynamics, with damping, relax toward the graph Laplacian's harmonic ground state. A model whose static limit is the graph Laplacian will pass; a model that is unitary by construction (energy-conserving wave equation) need not pass — its dynamics propagate but do not relax to a Dirichlet-pinned static state without an explicit static solver step.
- **Note on gating.** As a *gravity* test, G2 is informative-only: gravity emergence is established by G1 (the substrate Laplacian solve), independent of any model's dynamics. A model that fails to relax to the static solution under G2 is not failing the gravity test; gravity is computed on the substrate directly.
- However, G2 is *separately* a **stability test** for any v-i model whose static limit is the graph Laplacian. Such a model's dynamics, under damping and Dirichlet pinning, should converge to the static solution. If the energy diverges instead, that is a free-standing stability failure of the model, with nothing to do with gravity. Failures in this mode (RelCos-both's 60,000× energy divergence under pinning) are gating as stability concerns, not as gravity-test failures. The chapter-4 verdict treats them as the former.
- **Script**: Part B of [scripts/test_2d_static_field.py](scripts/test_2d_static_field.py).

## §8. Observables and metrics

A test result is one or more numbers extracted from a run. The bench uses the following observables consistently:

- **Total energy.** For v-i models: 0.5 · Σ v² + 0.5 · Σ i² (sum over nodes for v, over edges for i). For Scattering: 0.5 · Σ (a_fwd² + a_bwd²) (sum over edges). Both reduce to the wave-equation energy norm. *Cross-paradigm note:* the absolute values differ by a constant factor (≈ 0.65 for typical wavepackets on a 2D hex, since v-i energy counts both nodes and edges while Scattering counts edges only). Cross-paradigm comparisons therefore use *energy ratios* (final / initial) and matched-impedance fractions, which are dimensionless and paradigm-comparable; not absolute energies, which are not.
- **Per-node v-equivalent.** For v-i models: v itself, mapped to (−π, π] for symmetric reading. For Scattering: (a_fwd + a_bwd) averaged over incident edges per node — the scattering-paradigm node-level observable.
- **Per-edge i-equivalent.** For v-i models: i. For Scattering: a_fwd − a_bwd (the directed-flow component, tail-to-head).
- **Group velocity v_g(k).** Slope of envelope-centroid versus time on a ring.
- **Reflection/transmission fractions.** Per-arm energy at the end of a Y-junction run, divided by total final energy.
- **Force-law exponent.** Log-log slope of |∇v|(r), where the gradient is estimated as the per-node RMS of |v_tail − v_head| over incident edges.
- **Per-node rescaled R².** Linear-regression goodness-of-fit between a model's settled field and the analytical Laplacian solve, with one rescaling parameter (a, b) absorbed.

A pass on a metric does not imply a pass overall; chapter 4 weighs each test in context.

## §9. Closing pointer

The bench's tests are now defined. Chapter 4 runs them and reports the comparison.

The chapter sequence is summarized in the project [README](README.md).
