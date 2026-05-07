# Chapter 10: Closing summary

This project set out to build a digital-first model of the GRID lattice — a graph of discrete primitives (nodes and edges) with local update rules at each, evolving under a master clock. The framing was a comparison: rather than commit to one update rule a priori, hold the substrate fixed and test multiple candidate models against a standardized test bench. Chapters 1–9 worked through the substrate, the candidates, the comparison, and the structural consequences. This chapter consolidates what was established, what came as a surprise, what was ruled out, and what remains open.

---

## §1. The arc of the project

The project's central question, from [README.md](README.md):

> *Which discrete-lattice model — chosen from a small set of physically motivated candidates — best reproduces grid's wave-propagation and static-field behavior, and what does the wrap-promotion ladder look like under it?*

The chapter-by-chapter arc:

- **Chapter 1** established the substrate without committing to dynamics. Two primitive types — node and edge — with edge polarity (later demoted to a v-i-paradigm convention only) and a master clock concept.
- **Chapter 2** toured four candidate models: Telegrapher and Normalized (v-i with discrete wave-equation flavor), RelCos-both (cos-weighted dial-aware variant), and Scattering (sim-maxwell-style register exchange). All four are well-defined on the same substrate; the comparison decides which one the substrate's dynamics actually is.
- **Chapter 3** defined the test bench: stability, dispersion, Y-junction matched-impedance scattering, linearity, and gravity from the substrate's graph Laplacian. Each test specifies a paradigm-neutral input, a measurable observable, and a pass criterion.
- **Chapter 4** ran the comparison. **Scattering won**: exactly unitary, near-non-dispersive, matched-impedance to four decimals at coord-3 junctions, linear in superposition. Telegrapher fails CFL stability at coord ≥ 3. RelCos-both fails three independent failure modes (junction nonlinearity, Dirichlet instability, free-wave nonlinearity). Normalized passes most tests approximately but is dispersive and non-unitary. Gravity emerges from the substrate's graph Laplacian directly, independent of which model runs on the lattice.
- **Chapter 5** tested whether the chapter-4 verdict survives at the bit-substrate scale. Naive rounding fails (correlated noise doesn't average out under spatial coarse-graining), but stochastic rounding works: the M ∝ 1/(N − 1)²/ε² holographic-window scaling is recovered, with **N = 2 (1 bit per cell) as the absolute floor** of substrate resolution. The continuous Scattering model is the effective theory of a binary-bit substrate at Planck scale.
- **Chapter 6** generalized Scattering to arbitrary coordination and dimension. The S = (2/N)·J − I matrix is unitary at any N (S² = I); the matched-impedance coefficients R = (2 − N)/N, T = 2/N satisfy energy conservation algebraically. On 3D diamond (the natural bipartite analog of 2D hex), R = −1/2 and T = +1/2 per branch. Four lattice closures — open chain (L0), ring (L1), plaquette (L2), torus (L3) — anchor the wrap-promotion ladder.
- **Chapter 7** mapped each rung of the ladder to a physical phenomenon. L0 → L1: light, by closing the substrate. L1 → L2: mass, by embedding the ring in 2D (where coord ≥ 3 unlocks band-extremum eigenstates). L2 → L3: charge, by closing the second direction (where the torus's π₁ = ℤ² provides U(1) × U(1) topological windings). A speculative L4 third winding was identified — the simplest extension if the universe is a 3-torus.
- **Chapter 8** located α on the ladder. The structural argument: α first becomes available at L3 because that is the first rung where two independent topological invariants exist for cross-coupling. α is plausibly a categorical invariant of the second-wrap operation rather than a geometric ratio of lattice constants; geometric-ratio searches across many lattice constructions have not produced 1/137 in any natural way.
- **Chapter 9** showed that a node's functional behavior can be built from bare edges plus *cooperative context* — a triangle of inner micro-edges performing Givens rotations whose angles are *jointly* chosen to compose to S, with no central register or coordinator at runtime but with the cooperation built into the angle parameters at construction time. The reverse direction (edges from nodes) does not work the same way; edges have spatial extent that nodes lack. Edges are more fundamental than nodes, but edges alone are not enough: cooperation among multiple edges is a real and fundamental third ingredient.

The primary deliverable — *a substrate-level digital lattice where Scattering is the dynamics and the wrap-promotion ladder structurally maps to substrate / light / mass / charge* — is made. Chapter 8's α exercise is structural rather than numerical; the value 1/137 is identified as L3 work needing categorical / topological / RG machinery beyond this project's scope.

---

## §2. Established results

The project established the following, with the level of derivation supported by chapter-by-chapter analysis and where flagged by simulation in [scripts/](scripts/).

### The substrate (chapter 1, refined through chapters 6 and 9)

- Two structural ingredients of different kinds: **bare edges** (dynamic) and **connectivity** (static). The bare edge has two end-registers and one operation — swap during the exhale. Connectivity says which edges meet at which junctions.
- A node is *not* a primitive in the dynamic sense. A node is the **compound** that emerges when N bare edges meet at a junction whose connectivity says they meet there. The S-matrix is implicit in the compound's structure.
- Edge polarity is paradigm-specific (used by v-i models, inert under Scattering); not a universal substrate primitive.
- The master clock has two phases per cycle: **inhale** (each compound applies S = (2/N)·J − I to its registers) and **exhale** (each edge swaps its two end-registers). One exhale = one edge transit = the lattice's speed of light.

### The Scattering dynamics (chapter 4)

- **Exact unitarity per cycle.** S = (2/N)·J − I satisfies S² = I (chapter 6 §2.1) and the swap is a permutation; the full cycle is orthogonal, so the energy norm Σ r² is conserved exactly. Empirical confirmation: zero energy drift over 100 steps in test S1.
- **Matched-impedance scattering at every junction.** Coord-3 R = −1/3, T = +2/3, energy fractions 1/9 and 4/9 each, summing to 1. Empirical confirmation to four decimals in test L2.
- **Near-non-dispersive in 1D, mildly dispersive at coord 3.** v_g = 1.000 at every k in the 1D test (a coord-2 swap-matrix artifact); v_g = 0.35 ± 0.06 across k ∈ [0.2, 2.6] at coord 3 (test L1b). Bounded dispersion is a structural property of physical lattices.
- **Linear (perfect superposition).** R² = 1.0000 in both pinned and free-wave variants of test L3.
- **Bridge to grid: trivial.** Scattering is sim-maxwell's model. Observable equivalence with [grid/sim-maxwell](../../grid/sim-maxwell/) is built in.

### Gravity from the substrate (chapter 4 §3)

- The graph Laplacian on the hex lattice, with Dirichlet pins at a defect and zero at the boundary, gives log(r) potential and r⁻¹ force law (test G1). This emergence depends on the lattice graph alone, not on which dynamic model runs on it.
- Both Normalized and Scattering inherit gravity from this substrate computation. The chapter-4 verdict on light (Scattering wins) is independent of, and compatible with, the gravity result.
- **Bridge to grid/sim-gravity-2 is direct.** The substrate Laplacian solve is exactly what [grid/sim-gravity-2/run_scalar.py](../../grid/sim-gravity-2/run_scalar.py) computes.

### Substrate quantization (chapter 5)

- **Naive rounding fails.** At low N (≤ 4 bits per cell), naive rounding of the Scattering update produces correlated noise that does not average out under spatial coarse-graining. Lattice refinement does not help (test confirmed).
- **Stochastic rounding works.** Unbiased per-cell rounding produces independent noise that averages by 1/√M under windowed averaging (central limit theorem). The predicted M ∝ 1/(N − 1)²/ε² scaling is empirically confirmed at N from 257 down to 2 (test_holographic_recovery.py).
- **The minimum per-cell resolution is 1 bit.** N = 2 (a single signed bit, levels {−amp_max, +amp_max}) is the floor; below that, no information is carried. At N = 2 with macroscopic precision ε = 10⁻⁶, the holographic window contains 10¹² cells. The Planck-to-Compton scale ratio is ≈ 10²⁵, so available cell budget exceeds requirement by 13 orders of magnitude.
- **The continuous Scattering model is the effective theory of a binary-bit substrate.** This is consistent with GRID's axiom A5 (1/4 bit per cell as fundamental information capacity). The chapter-4 verdict survives the deeper substrate without modification.

### Wrap-promotion structure (chapters 6, 7)

- Each lattice closure carries a physical phenomenon as the simplest new conserved observable that the new topology supports:
  - L0 (open chain, π₁ = 0): substrate / information.
  - L1 (ring, π₁ = ℤ): light. Conservation: energy + crystal momentum.
  - L2 (plaquette, π₁ = ℤ embedded in ≥ 2D): mass. Conservation: + rest mass m_eff (from band curvature) + plaquette flux.
  - L3 (2-torus, π₁ = ℤ²): charge. Conservation: + (w_α, w_β) winding pair.
  - L4 (3-torus, π₁ = ℤ³, speculative): unidentified third invariant.
- **Mass requires a higher-dimensional context to exist.** Coord-2 (1D) lattices have linear dispersion (no band extrema), so no mass eigenstates. The L1 → L2 wrap simultaneously closes a second dimension and raises coord ≥ 3, which is what unlocks mass.
- **Periodicity is structurally preferred at every rung, including L0 → L1.** Three independent self-consistency arguments — boundary effects on open lattices, dispersion needing translation invariance, and Bekenstein-bound finiteness — all push toward compact-with-wraps. The "universe is plausibly a 3-torus at the largest scale" reading falls out as the natural cosmological consequence.
- **The α question is structural, not yet numerical.** α first becomes available at L3 because L3 is the first rung where two independent topological invariants exist for cross-coupling. Geometric-ratio searches have failed to produce 1/137; the candidates that fit the wrap-of-a-wrap framing are categorical / topological / RG-fixed-point invariants. The specific value remains open work.

### Edges plus cooperative context (chapter 9)

- Nodes have functional models in *edge-and-cooperative-context* terms (the triangle construction of chapter 9 §4): three inner micro-edges arranged as a triangle, each performing one Givens rotation whose angle is *jointly* chosen with the other two so that the composition equals S. No central register, no central coordinator; coordination at runtime is zero, but cooperation is built into the off-line agreement on parameters.
- The reverse — edges from nodes — does not work the same way. Edges have spatial extent (transit during exhale); nodes do not. Constructions of "edges from nodes" terminate at smaller edges, not pure nodes. The asymmetry is real.
- The original [grid-couplet](../grid-couplet/) symmetry-of-primitives framing is settled in the negative — nodes and edges are not on the same footing — but edges alone are not the whole story either. The substrate's minimal structure is *bare edges + connectivity + cooperative context*. Cooperation is a real and fundamental third ingredient: not a runtime coordinator, not a smuggled-in node, but a structural condition on the parameters that lets bare edges produce node behavior collectively.

---

## §3. Ruled out and demoted along the way

### Models eliminated

- **Telegrapher** — fails CFL stability at coord ≥ 3 (energy ratio 4.6 × 10⁴ over 100 steps on 2D hex). Documented as the failure mode that motivates Normalized's 1/N regularization. The model is not viable on its own; it is kept as a pedagogical contrast.
- **RelCos-both** — fails on three independent grounds: (i) junction scattering at coord 3 gives wrong reflection coefficient and breaks geometric symmetry under arm-swap (the central node's evolving dial direction enters the cos weighting nonlinearly); (ii) Dirichlet pinning destabilizes the dynamics (energy diverges 60,000×); (iii) free-wave dynamics is intrinsically nonlinear (R² = 0.88 on free-wave superposition vs Normalized and Scattering at machine precision). A "fair-shake" test using a dial-aware IC (mirroring the model's compass-dial interpretation) made the failures *worse*, ruling out IC translation as the cause. Documented implementation issues: gauge non-invariance under v → v + c, and v = 0 default IC imposing a preferred direction. Removed from the active candidate set.
- **Normalized telegrapher** — passes basic tests but with non-trivial energy drift (+11.6% in the Y-junction test) and strong dispersion (v_g varies from 0.7 at low k to 0 at k = π). Its static limit equals the graph Laplacian, which makes its dynamics relax to the substrate gravity solution under damping — a pedagogically clean property, but redundant since chapter 4 establishes that gravity comes from the substrate Laplacian directly. Preserved as the discrete-wave-equation contrast to Scattering, not as a competing winner.
- **Cos-weighted (grid-lab v2)**, the fixed-angle precursor to RelCos-both — diverges in 2D within tens of steps. Scrapped before the candidate pool.
- **Gauge** (compact gauge field on edges, sin(A) coupling) — deferred without active testing. The active candidates left no open question that gauge would have addressed.

### Hypotheses ruled out

- **Naive rounding for substrate quantization.** Predicted to give M ∝ 1/N²/ε² scaling under spatial coarse-graining (per the analog-averaging analysis). Did not — naive rounding produces correlated noise that does not average out. Stochastic rounding does work; bit-conservative Boolean rules (FHP-style) would also work and are the physically natural form for long-time dynamics.
- **α as a geometric ratio of lattice constants.** Substantial prior search has not produced 1/137 from any natural ratio of edge lengths, packing densities, cell counts per unit volume, or similar geometric invariants. The chapter-8 framing explicitly redirects: α is plausibly a categorical invariant of the wrap-of-a-wrap operation, not a function of the lattice's specific dimensions.
- **The "node and edge as symmetric halves of one primitive" framing from grid-couplet.** Refuted by the chapter-9 asymmetry: nodes have functional models in edge-plus-context terms, edges do not have the analogous reduction.
- **The original outline's Y-Δ network reduction as a clean "all nodes vanish" claim.** Y-Δ on a periodic lattice reorganizes topology locally but does not decrease total node count globally. The real reduction is "the node is a compound (bare edges + connectivity)," not "the node is electrically equivalent to a triangle of impedance-3Z lines."

---

## §4. Unexpected findings

Items the project did not anticipate at the outset.

### Light and gravity emerge from different layers

Chapter 4's gravity test (G1) was originally designed as a head-to-head comparison of how each model handles static fields. The result was clarifying in an unexpected way: gravity does *not* come from a model's dynamics — it comes from the substrate's graph Laplacian, computed by direct linear algebra. Every candidate inherits gravity for free; no model "wins" on gravity, and no model "loses" gravity if its dynamics are unitary rather than relaxational. Light comes from the dynamics; gravity comes from the substrate. The two layers are independent.

This was not a hypothesis going in. It became clear once the dynamics-convergence test (G2) showed that Scattering's unitarity prevents relaxation to the static solution, which initially looked like a failure but is actually a structural feature of a wave equation rather than a relaxation equation.

### Mass is unavailable on 1D substrates

Chapter 7 §4.1 derived this directly: mass eigenstates require band extrema (where v_g = 0); band extrema require coord ≥ 3 (multi-sublattice Bloch matrices); coord ≥ 3 requires ≥ 2D substrate. L1 (the 1D ring) is structurally massless. The L1 → L2 wrap is *the first rung where the substrate has anywhere for inertia to live*. This is the structural reason the wrap-promotion ladder has the rungs it does — the phenomena are not a posited list but the simplest new conserved observables that each topology unlocks.

The parallel argument for α at L3 (chapter 8) — first rung with two topological invariants for cross-coupling — was suggested by the mass-at-L2 argument and reinforces the structural pattern: each rung makes available the simplest new observable that requires that rung's topology.

### Stochastic, not deterministic, rounding gives the holographic recovery

Chapter 5's first round of experiments tested deterministic rounding (round each register to the nearest of N levels per tick). It did not work — relative drift was constant across lattice scales, contrary to the analog-averaging prediction. The reason: deterministic rounding produces *correlated* noise (neighboring cells with similar values round in the same direction), and spatial averaging cannot cancel correlated noise.

Stochastic rounding (probabilistic, with E[R(v)] = v) was added in a second round and recovered the predicted M ∝ 1/√M scaling cleanly down to N = 2. The prior at [grid-quantizing.md](grid-quantizing.md) §6.1 had not anticipated that the rounding scheme would matter so much. This was the chapter's main course-correction.

### Edges plus cooperative context: the actual minimal structure

The original [grid-couplet](../grid-couplet/) framing had nodes and edges as symmetric halves of one underlying primitive. Chapter 9 refuted *that specific symmetry*: edges have spatial extent that nodes lack, the reduction goes one way (nodes from edges-plus-context) but not the other (edges cannot be built from nodes). The asymmetry is real.

But the project would be misleading if it left the impression that edges alone are sufficient. The chapter-9 triangle construction needs three inner edges *whose rotation angles are jointly chosen* to compose to S. The angles are not properties of any single edge in isolation — they are constrained by a self-consistency condition that involves all three edges together. This *cooperative context* — the requirement that the edges' parameters fit each other, that runtime behavior emerges from off-line agreement among multiple edges — is itself a real and fundamental ingredient. It is not a runtime coordinator (no central element issues commands during the inhale; each edge runs its own angle independently), but it is also not nothing. It is the binding structure that lets bare edges produce a node's behavior collectively.

So the honest hierarchy is: *edges plus cooperative context* is the minimal structure that supports a node's behavior. Edges are more fundamental than nodes (edges-from-nodes does not work), but edges alone are not enough — they need the cooperation context, which is structurally substantive. The triangle construction's structural integrity comes from *how* the cooperation is achieved: through self-consistent parameters fixed at compound-construction time, with each edge running its own rotation independently at runtime. No edge orchestrates the others. This is what distinguishes "edges plus cooperative context" from "edges plus a tiny coordinator" — the cooperation is built into the parameters, not enforced by a runtime element.

This refines but does not overturn the chapter-9 result. The original [grid-couplet](../grid-couplet/) "node and edge as symmetric primitives" framing is still settled in the negative — nodes are not on the same footing as edges. But the replacement framing is *not* "edges first, nodes derived from edges alone." The replacement is "bare edges plus connectivity plus cooperative context produces nodes-as-compounds; edges are more fundamental than nodes; cooperation is a real and fundamental third ingredient that should not be glossed over."

### Cosmological reading: the universe is plausibly a 3-torus

Chapter 7 §2 developed three independent self-consistency arguments — boundary effects, dispersion / Brillouin structure, and Bekenstein finiteness — all of which prefer a periodic substrate. Chapter 7 §2.5 noted that this implies the universe at the largest scale is plausibly a compact 3-manifold, with apparent flatness being the local-tangent-space approximation. The simplest such manifold is the 3-torus.

This was not a hypothesis the project set out to test. It arose as a structural consequence of substrate self-consistency. Chapter 8 §6 picked it up again with the L4 speculation: if the universe is a 3-torus, the third winding might host a third conserved invariant of which α would be a coupling. Both readings are speculative; the project notes them and does not commit.

---

## §5. Comparison with grid-primitive

[grid-primitive](../grid-primitive/) is the analog-first sibling project. The two arrived at strongly convergent substrate structures from very different starting points.

### Where they converge

- **Edges are the primary active element; nodes are derived.** grid-primitive's cylinder is a 2D distributed object with two coupled internal fields (e, φ); grid-duality's edge is a 1D pair of registers. Both treat the edge as the primary active element of the substrate. Grid-primitive's nodes are passive continuity boundaries with no state of their own; grid-duality's nodes are compounds derived from edges and a cooperative-context binding structure. *Both projects converge on edges as more fundamental than nodes, with neither project treating nodes as primitives in the dynamic sense.* Both projects also share the structural feature that nodes' coherence at runtime is enforced by cooperation among incident edges (continuity in grid-primitive, self-consistent angle parameters in grid-duality), not by any node-level computation.
- **Lattice geometry: 2D hex with wye-junction continuity.** Both projects landed on the hexagonal lattice with coord-3 wye junctions as the natural substrate at this level. grid-primitive cited grid-docs preferences; grid-duality derived the choice from chapter-4 stability and chapter-6 bipartite-orientation arguments. The convergence is structural, not coincidental.
- **Speed of light is set by the substrate's clock structure.** grid-primitive's *c* is the cylinder's internal propagation speed; grid-duality's c = one edge per exhale. Both projects locate c at the substrate level, not as an emergent quantity to be derived from finer dynamics.
- **Light propagates without dispersion at long wavelengths.** grid-primitive's matched-chirality wave equation gives ω = c·|k|; grid-duality's dispersion test (test L1) gives v_g → 1 in the small-k limit on coord-2 (and bounded v_g at coord 3). Both produce the same long-wavelength dispersion-free behavior.
- **Gravity emerges from the substrate's static structure, not from the dynamics.** grid-primitive's chapter 4 derived 1/r force scaling from the 2D Laplacian Green's function in static equilibrium; grid-duality's chapter 4 G1 test confirmed log(r) potential from the graph Laplacian solve. Both projects reach gravity through the substrate's harmonic-function structure, not through a dynamic update rule.
- **Charge is plausibly a topological invariant on closed loops.** grid-primitive's chapter 8 examined α as a structural property of wrapping; grid-duality's chapter 8 located α at L3 as the wrap-of-a-wrap rung. Both projects identify topology — not lattice geometry — as the natural carrier of charge and α. Both projects are inconclusive on the specific value 1/137.

### Where they diverge

- **Continuous vs discrete substrate.** grid-primitive treats the cylinder as a *continuous* primitive, with state varying continuously along its length. grid-duality treats the edge as *discrete*: two end-registers, with a clock-driven swap. The two are connected by chapter 5: real-valued Scattering is the effective theory of a binary-bit substrate at Planck scale, recovered via spatial averaging. grid-duality's framework supplies the bit-substrate that grid-primitive's continuous-cylinder description coarse-grains over.
- **Internal structure: chiral fields vs registers.** grid-primitive's cylinder has two coupled internal fields with a chirality parameter χ̃ governing the coupling. grid-duality's edge has two scalar registers with no internal structure beyond their values. The chirality structure of the cylinder primitive maps onto grid-duality's compound-node parameters (the rotation angles of the triangle construction in chapter 9 §4) — both encode the directional information that breaks the would-be symmetry of pure averaging.
- **Where the matched-impedance scattering comes from.** In grid-primitive, the wye-junction continuity is enforced by the continuous-field boundary conditions (the cylinder's e and φ values must match at the junction). In grid-duality, the same matched-impedance behavior arises from the S-matrix's unique-solution-to-junction-physics structure (chapter 6 §2.2). The two derivations are structurally equivalent but use different mathematical machinery.
- **Treatment of α.** grid-primitive's chapter 8 explored α as a kink-loss fraction per closed wrap and arrived at an inconclusive candidate. grid-duality's chapter 8 explored α as a categorical invariant of the wrap-of-a-wrap operation and arrived at an inconclusive candidate. The two paths reached convergent inconclusiveness through different reasoning. *Both project agree α first becomes available at the second-wrap rung but neither derives 1/137.*

The convergence is more striking than the divergence. Two independent design paths — analog-first continuous cylinders vs digital-first discrete edges — landed on the same substrate-level structure: edge-primary, wye-junction lattice, c set by substrate clocks, gravity from substrate Laplacian, charge from topological wrap, α at the second-wrap rung. The convergence is positive evidence that the substrate has the structure both projects describe, not a feature of either project's specific approach.

---

## §6. What remains open

### Open by design (not project failures)

- **Specific value of α.** Both this project and grid-primitive identify α as a quantity that lives at the second-wrap rung but neither derives 1/137. The candidate observables for α (categorical invariants of the wrap-twice operation, RG fixed points, anomaly coefficients) are well-defined targets for future work.
- **L4 third invariant.** If the universe is a 3-torus, what does the third winding correspond to? Candidates include a third gauge charge, spin, generation number, or a cosmologically scaled invariant. None has been identified as the right answer.
- **3-torus vs 4-torus.** Whether time itself is a wrap dimension at the cosmological scale is a question the project flags but does not answer.

### Open work that requires machinery beyond this project

- **Bit-conservative Boolean rules for substrate quantization.** Chapter 5 used naive stochastic rounding to demonstrate the holographic-recovery scaling. The physically natural form for long-time dynamics is bit-conservative Boolean rules (FHP-style), which conserve bit count exactly per junction and avoid noise accumulation. Designing these rules for the hex Y-junction and 3D diamond cubic-junction is well-defined but tedious; the construction is not done in this project.
- **Higher-coord parameter computations for chapter 9's triangle construction.** Coord-N nodes decompose into trees of coord-3 sub-junctions, each implemented by the triangle. Working out the explicit angle parameters for coord ≥ 4 cases is well-defined but not done.
- **3D dispersion explicit band structure.** Chapter 6 §6 sketched the dispersion on diamond using bounds (v_g ∈ [1/√3, 1] across symmetry directions) without computing the full 8 × 8 Bloch matrix's eigenvalues. The full band structure is well-known in solid-state physics; its specific form is not needed for the project's claims but would be needed for any future quantitative work on diamond.

### Open questions that could become future projects

- **Building the substrate-quantization bit-conservative rules.** Chapter 5's "honest scope" statement notes that this is a separate research program. It would fit naturally as the next sibling project after this one and grid-primitive.
- **Categorical / topological derivation of α.** Chapter 8's framing identifies the right kind of candidates but does not compute any of them. A focused project on lattice-gauge-theory of charge at L3, with categorical invariants of the second wrap calculated explicitly, would be the natural next step on α.
- **Cosmological-topology test bench.** The chapter-7 §2.5 universe-as-3-torus reading suggests observable signatures (matched-pair correlations in the CMB, repeating cosmic structure). Building a test bench for these signatures and applying it to actual cosmological data is well outside this project's scope but is a natural follow-up direction.

---

## §7. Closing

The project's primary deliverable is in place: a digital-first lattice substrate with Scattering as the dynamics, gravity from the substrate's graph Laplacian, and a wrap-promotion ladder that maps each closure (open chain → ring → plaquette → torus) to a physical phenomenon (substrate → light → mass → charge) by accreting one new conserved observable per wrap. The framework supports a 1-bit Planck-scale substrate via stochastic rounding, with the macroscopic continuous-field description being the effective theory at scales much larger than the cell spacing. Nodes are derived compounds, edges are more fundamental than nodes, and cooperative context — the structural condition on parameters that lets multiple edges produce node behavior collectively — is a third structural ingredient that the substrate cannot do without.

The α question is left open at its specific value but located structurally on the ladder. The L4 / cosmological questions are flagged as natural extensions and acknowledged as outside the project's scope. The substrate is consistent with [grid-primitive](../grid-primitive/)'s analog-first cylinder primitive at the level of overall structure, despite very different starting points — the two projects converge on the same substrate-level picture from opposite directions.

This closes the project. Subsequent work on α, on bit-conservative substrate dynamics, and on cosmological topology can proceed against this substrate without re-deriving the substrate itself.

The chapter sequence is summarized in the project [README](README.md).
