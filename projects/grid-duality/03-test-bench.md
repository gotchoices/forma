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

### Test L1 — 1D dispersion / group velocity

Sweep the carrier wavevector k from 0.1 to ~π on a 256-node ring. For each k, launch a Gaussian wavepacket, track the envelope centroid over 80 steps via the circular-mean trick (z = Σ |v|² · e^{i·2π x/n}), and linear-fit centroid-vs-step to extract the group velocity v_g(k).

- **Reference**: a non-dispersive medium gives v_g(k) = c constant.
- **What it diagnoses**: whether the model carries waves of different wavelengths at the same speed — the defining feature of light.
- **Script**: [scripts/test_1d_dispersion.py](scripts/test_1d_dispersion.py).

### Test L2 — Y-junction reflection / transmission

A Y-tree with three 60-node arms meeting at one coord-3 vertex. A Gaussian wavepacket is launched on arm 0, travels inward, scatters at the junction, and clears into the other arms. Per-arm energy is measured at every step.

- **Reference**: matched-impedance scattering at coord N = 3 gives R = −1/3 reflected and T = +2/3 transmitted into each branch, so the energy fractions are R² = 1/9 reflected, T² = 4/9 per transmitted branch, with total Σ = 1 (energy conservation). Both v-i and scattering paradigms predict the same coefficients in the matched-impedance limit; this is the canonical test for whether a model treats junctions correctly.
- **What it diagnoses**: junction-level energy flow — the structural property that makes a hex lattice (every node coord 3) a viable light carrier.
- **Script**: [scripts/test_y_junction.py](scripts/test_y_junction.py).

### Test L3 — Linearity / superposition

On a 25×25 hex torus, three Dirichlet-pinned configurations: source A only; source B only; both A and B. After running each to a settled state under small damping, compare the field v_AB to the sum v_A + v_B over the unpinned interior.

- **Reference**: a linear medium satisfies v_AB = v_A + v_B exactly. Per-node correlation and rescaled-fit R² near 1 confirm linearity; deviation diagnoses nonlinearity in the update rule.
- **What it diagnoses**: linear superposition — required for any wave-equation interpretation, and required for gravity to add over multiple sources.
- **Script**: [scripts/test_2d_superposition.py](scripts/test_2d_superposition.py).

## §6. Gravity test — substrate part

### Test G1 — graph Laplacian solve (paradigm-neutral)

On a 25×25 hex torus, a source node is pinned to v = +0.3 at the centre, and a sink ring (all nodes at distance ≥ 9.0) is pinned to v = 0. Solve the graph Laplacian system L_ff · v_free = −L_fc · v_fixed by direct sparse linear algebra. Fit the resulting field to log(r) potential and r⁻¹ force.

- **Reference**: in continuum 2D, the Laplacian Green's function around a localized source decays as log(r), giving a force gradient that decays as 1/r. The 2D analog of Newton.
- **What it diagnoses**: whether the lattice graph itself supports gravitational behavior. This test runs on the substrate alone — no model dynamics are involved. It mirrors the static solve in [grid/sim-gravity-2/run_scalar.py](../../grid/sim-gravity-2/run_scalar.py).
- **Script**: Part A of [scripts/test_2d_static_field.py](scripts/test_2d_static_field.py).

The substrate test is the gravity-emergence claim. Any candidate model that lives on this lattice inherits gravity for free, by computing the static Laplacian directly when needed (the same way grid does).

## §7. Gravity test — dynamics-convergence part

### Test G2 — does each model relax to the substrate's static solution?

Same Dirichlet pins as test G1, but instead of solving the graph Laplacian directly, run each model's dynamic update rule for 800 steps with a small damping factor (0.02 per step on the through variable). Time-average the field over the last quarter of the run. Compare to the static solution from G1: log fit, force fit, per-node rescaled R².

- **Pass condition**: the dynamic-averaged field matches the static solution shape (rescaled R² near 1, force exponent near −1).
- **What it diagnoses**: whether the model's dynamics, with damping, relax toward the graph Laplacian's harmonic ground state. A model whose static limit is the graph Laplacian will pass; a model that is unitary by construction (energy-conserving wave equation) need not pass — its dynamics propagate but do not relax to a Dirichlet-pinned static state without an explicit static solver step.
- **Note**: this test is informative, not gating. Gravity emergence comes from G1; G2 tells us about the model's relaxation behavior under simulated boundaries.
- **Script**: Part B of [scripts/test_2d_static_field.py](scripts/test_2d_static_field.py).

## §8. Observables and metrics

A test result is one or more numbers extracted from a run. The bench uses the following observables consistently:

- **Total energy.** For v-i models: 0.5 · Σ v² + 0.5 · Σ i². For Scattering: 0.5 · Σ (a_fwd² + a_bwd²). Both reduce to the wave-equation energy norm.
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
