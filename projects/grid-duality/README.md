# grid-duality

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** A digital-first model of the GRID lattice with two structural primitive types — node and edge. The project does not pre-commit to a specific update rule or state structure; instead, it tests several **candidate models** against a standardized **test bench** and selects the one with the best combination of stability and fidelity to grid's existing simulations. sim-maxwell's model is one of the candidates, so the historical "bridge to grid" question becomes implicit in the model selection.
**Method:** Mathematical derivation as discovery; computational verification via head-to-head model comparison; minimum verbosity.
**Status:** Chapters 1–5 complete. Chapter-4 verdict: Scattering is the substrate's dynamics; gravity emerges from the substrate's graph Laplacian directly ([04-model-comparison.md](04-model-comparison.md)). Chapter-5 finding: real-valued Scattering survives naive quantization down to ~6 bits per cell; below that it breaks under naive rounding, and recovery requires bit-conservative Boolean rules (deferred). The project continues with the real-valued model as effective theory ([05-substrate-quantization.md](05-substrate-quantization.md)).

## Why this project exists

[grid-primitive](../grid-primitive/) modeled the GRID lattice analog-first: a single distributed object (the cylinder primitive) carrying both magnitude and phase on one continuous body. A digital-first counterpart would be a graph of discrete primitives, with local update rules at each, evolving under a clock.

The first attempt at a digital-first project — [grid-couplet](../grid-couplet/) — committed prematurely to one specific update rule and accumulated drift before the rule's 2D behavior was verified. Its findings are preserved in [couplet.md](couplet.md). grid-duality is a fresh start that takes a different approach: pin the *substrate* (lattice geometry + primitive types + clock concept) clearly, but leave the update rules and state structure as a discovery target. Multiple candidate models are tested side-by-side; the winner is the one that produces stable, wave-like behavior across 1D and 2D and matches the observable dynamics of [grid/sim-maxwell](../../grid/sim-maxwell/) and [grid/sim-gravity-2](../../grid/sim-gravity-2/).

The central question:

> *Which discrete-lattice model — chosen from a small set of physically motivated candidates — best reproduces grid's wave-propagation and static-field behavior, and what does the wrap-promotion ladder look like under it?*

## Layer relationship

```
MaSt (particles, masses, charges)
   ↑
GRID lattice (Maxwell, gravity, charge-emergence, ζ)
   ↑
grid-duality (this project)        ← parallel to grid-primitive
```

Same layer as grid-primitive, different model: analog-first cylinder vs. digital-first graph. Both feed grid's lattice abstractions. The discrete graph at this scale is what the project converges on through its model-comparison process.

## The setup in brief

The lattice has two structural primitive types:

- **Nodes** — vertices in the lattice graph. Whether a node holds one scalar, multiple values, internal spatial structure, or no state at all is model-dependent.
- **Edges** — connections between two nodes. Whether an edge holds one value, a pair of values at its two ends, or something else is model-dependent.

Some models read a per-edge **polarity** (head and tail) as a sign in their update rules; this is paradigm-specific and not a property of the substrate itself. The Scattering model does not use polarity — its registers are unordered. Edge orientations are standardized in a common direction (1D rightward; 2D hex three-direction; 3D analog deferred) for the v-i models that need them.

Beyond this substrate, the *state* held at each primitive type and the *update rules* governing their dynamics are **model-dependent**. Different candidate models make different choices, and bounding choices in particular have structural consequences. After an initial round of 2D simulation, the **active candidates** are:

- **Telegrapher** ([models/telegrapher.md](models/telegrapher.md)) — across variable bounded on nodes (U(1)); through variable unbounded on edges (ℝ); two-phase clock with signed-sum at nodes. *Failure mode at coord > 2 — energy diverges ×45,000 in 100 steps on 2D hex. Kept as the contrast that motivates Normalized.*
- **Normalized telegrapher** ([models/normalized.md](models/normalized.md)) — Telegrapher with 1/N factor on the node update. *Stable, linear, Y-junction within 0.5% of matched-impedance theory but with non-trivial energy drift; strongly dispersive. Static limit IS the graph Laplacian, so its dynamics (with damping) relax to the same gravity field the substrate solve produces directly. Documented as the pedagogically useful baseline, not the winner.*
- **RelCos-both** ([models/relcos-both.md](models/relcos-both.md)) — cos-weighted node update **and** edge update, with cos taken relative to the node's dial direction. *Stable for free wave propagation in 2D, but unstable under Dirichlet pinning — energy diverges ×60,000. Removed from the active candidate set.*
- **Scattering** ([models/scattering.md](models/scattering.md)) — A network of N-register processors (nodes) connected by two-ended transmission lines (edges). Each register is the meeting point of one edge end with one node. The clock has two phases: an *inhale* in which each node samples its registers, applies S = (2/N)·J − I, and overwrites them; and an *exhale* in which each edge swaps the values in its two registers. One exhale = one edge transit = the speed of light c on the lattice. **The winning model.** Unitary by construction (zero energy drift), non-dispersive at coord 2 (v_g = 1.000 at every k) and mildly dispersive at coord 3 (v_g = 0.35 ± 0.06 across the tested k range), matched-impedance Y-junction scattering to four decimals (0.1111 / 0.4444 / 0.4444 vs theory 1/9, 4/9, 4/9). The "two values per edge" of sim-maxwell is the same thing as the two registers of an edge, viewed from a different angle. Gravity is computed on the substrate's graph Laplacian directly, the same way [grid/sim-gravity-2/run_scalar.py](../../grid/sim-gravity-2/run_scalar.py) does, separately from the dynamics.

Two further candidates have been **deferred or scrapped**:

- **Gauge** — different state structure (compact gauge field on edges, real on nodes). Implementation requires more thought on the sin(A) coupling form. *Deferred until a later round if the active candidates leave open questions.*
- **cos-weighted (grid-lab v2)** — fixed-angle cos node update. *Scrapped:* the cos-on-one-phase failure mode is already documented (RelCos-node and RelCos-edge variants tried during development both diverge in 2D within ~10 steps). Spec retained for reference but no longer actively tested.

Each candidate is a full self-contained model: state + clock + update rules. Chapter 2 specifies each precisely. Chapter 3 defines the test bench (standardized inputs, observables, and signal translation between paradigms). Chapter 4 runs the comparison and selects a winner. Chapters 5 onwards build on the winning model.

The "bridge to grid" — verifying that the project's model reproduces grid's observable dynamics — is **implicit in the model comparison**: sim-maxwell's model is one of the candidates, and observable equivalence with sim-maxwell is one of the comparison metrics.

## Ground rules

1. **Discovery, not proof.** Mathematics that *yields* results, not asserts them.
2. **Two primitive types only.** Node and edge. Both are present in every candidate model, even if some models leave one of them stateless.
3. **Substrate is shared; models differ.** Lattice geometry and the master clock concept are foundational. Edge polarity and common-direction orientation are labeling conventions the substrate makes available — used by the v-i paradigm (Telegrapher / Normalized / RelCos-both, which read s_e = ±1 from polarity) and inert under Scattering (whose registers are unordered). State structure, update rules, and clock-phase count are model-dependent.
4. **No pre-commitment to a winning model.** The model selection is the substantive output of chapter 4, not a chapter-1 posit.
5. **Variables stay symbolic.** Don't pin numerical values until algebra or simulation forces it.
6. **Computation only when forced.** Paper math first; the test bench drives the substantive comparison.
7. **Operational fidelity to grid.** Bridges to [grid/sim-maxwell](../../grid/sim-maxwell/) and [grid/sim-gravity-2](../../grid/sim-gravity-2/) are verified by simulation showing equivalent observable behavior under matched drives.
8. **All test infrastructure local.** Engine, model implementations, tests, and outputs live under `projects/grid-duality/scripts/`. [viz/grid-lab](../../viz/grid-lab.md) is independent for the duration of model selection; once the project converges, grid-lab may import the winning model from this project.

## Goals

### Theories to test

Claims to examine — supported or refuted by the test bench in chapter 4.

1. **Foundational substrate suffices.** The substrate (nodes, edges, polarity, common-direction orientation, two- or single-phase clock) supports stable, wave-like dynamics in 1D for at least one candidate model.
2. **At least one candidate is stable in 2D.** Some candidate produces stable, wave-like dynamics on a 2D hex lattice without per-step amplification at junctions.
3. **At least one candidate gives matched-impedance scattering at Y-junctions.** Reflection and transmission coefficients (−1/3 and +2/3 in the matched case) are reproduced by the candidate's steady-state behavior.
4. **At least one candidate reproduces sim-maxwell.** Operational fidelity: under matched drives, the candidate's observables agree with [grid/sim-maxwell](../../grid/sim-maxwell/)'s within tolerance.
5. **At least one candidate reproduces sim-gravity-2.** Static field around a pinned defect shows logarithmic decay, matching [grid/sim-gravity-2](../../grid/sim-gravity-2/).
6. **The wrap-promotion ladder maps onto the winning model.** L0 → L1 → L2 → L3 corresponds to specific lattice closures (open chains, 1D loops, 2D plaquettes, 2D-sheet wraps). The ladder structure is meaningful regardless of which candidate wins.
7. **α appears at a specific level of the ladder.** Conjecture: α emerges at L3 only (second-order wrap). To be tested.
8. **Bridge to grid is operational.** If sim-maxwell's model wins, the bridge is trivially the model itself. If a different model wins, the bridge is the operational equivalence verified in chapter 4.

### Open questions

1. **Which candidate model wins?** And does it win uniquely, or do multiple candidates pass all tests with comparable fidelity?
2. **Signal translation between paradigms.** What's the canonical way to translate "a unit pulse" or "a sinusoidal wave" between, e.g., (v, i) and (a_fwd, a_bwd) representations? The test bench has to define this.
3. **CFL handling.** If the winning model needs a stability factor (sub-unit time step or 1/N normalization), is that a feature of the model or a regularization?
4. **Where in the ladder does α appear?** Posited at L3; to be tested.
5. **Are nodes and edges genuinely independent primitives?** Bonus question for the closing chapters.

## Background

### What was tried before

- [grid-couplet](../grid-couplet/) — earlier digital-first project; lessons in [couplet.md](couplet.md). Adopted a single update rule (cos-weighted) without 2D verification; the rule turned out to be unstable at coord 3. The lesson is what motivates the test-multiple-models approach here.
- [grid-primitive](../grid-primitive/) — analog-first sibling. Sets the bar grid-duality's winning model should match in observable behavior.
- [viz/grid-lab](../../viz/grid-lab.md) — earlier digital-first sketch. Inspiration for the substrate, but its specific update rule (cos-weighted v2) is one of the candidates being tested rather than an authoritative reference.
- [grid/sim-maxwell](../../grid/sim-maxwell/) — wave-propagation simulation using vertex scattering with traveling-wave amplitudes. Its model is a candidate in the comparison.
- [grid/sim-gravity-2](../../grid/sim-gravity-2/) — static-field simulation. Its 1/r force law is a fidelity benchmark.

### What this project is not trying to do

- **Not deriving the value of α.** The α question is *where* in the ladder it appears, not what value it takes.
- **Not reimplementing grid-lab.** grid-lab stays where it is. After model convergence, grid-lab may eventually import the winning model from grid-duality; that's a future cleanup, not a project goal.
- **Not pre-selecting a winning model.** Even though some candidates are favored on physical grounds, the test bench in chapter 4 produces the verdict.
- **Not opening sub-primitive structure.** Nodes are 0D, edges are 1D. No fractal recursion required by any candidate.
- **Not re-deriving Maxwell or gravity from scratch.** [grid/maxwell.md](../../grid/maxwell.md) and [grid/gravity.md](../../grid/gravity.md) remain authoritative.

## Background reading

- [couplet.md](couplet.md) — lessons from the prior project
- [grid-primitive/README.md](../grid-primitive/README.md) — analog-first sibling
- [grid/sim-maxwell/README.md](../../grid/sim-maxwell/README.md) — candidate model #3 (Scattering)
- [grid/sim-gravity-2/README.md](../../grid/sim-gravity-2/README.md) — fidelity benchmark for static fields
- [grid/foundations.md](../../grid/foundations.md) — GRID axioms
- [grid/charge-emergence.md](../../grid/charge-emergence.md) — where the L3 charge-from-wrap story currently lives
- [viz/grid-lab.md](../../viz/grid-lab.md) — earlier digital-first sketch (cos-weighted v2)

## Project layout

```
projects/grid-duality/
├── README.md                       this file
├── couplet.md                      lessons from prior project
├── 01-foundation.md                lattice substrate
├── 02-candidate-models.md          model overview / tour
├── 03-test-bench.md                tests and observables
├── 04-model-comparison.md          comparison results, winner selection
├── 05-substrate-quantization.md    bit-level substrate; does the verdict survive?
├── 06-3d-extension-and-lattice-closures.md  3D lattice + closure topology (TODO)
├── 07-wrap-promotion-modeling.md   mass / charge as observables on closures (TODO)
├── 08-where-alpha-appears.md       locating α on the ladder (TODO)
├── 09-node-decomposition.md        Y-tree decomposition; edge ≠ node (TODO)
├── 10-closing-summary.md           closing summary (TODO)
├── models/                         per-model specifications
│   ├── telegrapher.md
│   ├── normalized.md
│   ├── relcos-both.md              ← primary candidate, stable in 2D
│   ├── scattering.md
│   ├── gauge.md                    (deferred)
│   └── cos-weighted.md             (scrapped — kept for reference)
└── scripts/
    ├── engine.py                   lattice engine (1D ring, 2D hex torus)
    ├── models.py                   Python implementations of each model
    ├── test_pulse.py               1D pulse test (delta, Gaussian, traveling wave)
    ├── test_2d_pulse.py            2D Gaussian-perturbation comparison
    ├── test_2d_wavefront.py        2D directional-wavefront comparison
    ├── test_2d_static_field.py     gravity test (substrate Laplacian + dynamics convergence)
    ├── test_1d_dispersion.py       1D group-velocity sweep (light-vs-medium signature)
    ├── test_2d_superposition.py    linearity check: does v_A + v_B = v_AB?
    ├── test_y_junction.py          Y-tree matched-impedance reflection/transmission
    ├── test_unbounded_phase.py     side-test: bounded (mod 2π) vs unbounded v in v-i models
    ├── test_relcos_dial_ic.py      RelCos-both fair-shake: dial-aware IC vs standard IC
    ├── test_2d_freewave_superposition.py    free-wave superposition (no pins)
    ├── test_2d_dispersion.py       2D group-velocity sweep at coord 3
    ├── test_quantization_sweep.py  chapter-5 substrate-quantization experiments
    └── output/                     plots and notes
```

## Chapters

The arc below is a sketch. Early chapters are framed in detail; later chapters as questions. The project may redirect when a chapter's results require it.

1. **`01-foundation.md`** — The lattice substrate. Define the two primitive types (node, edge), edge polarity, common-direction orientation conventions, and the master-clock concept. Establish what is shared across all candidate models versus what is left to per-model specification. No update rules; no specific state structure.

2. **`02-candidate-models.md`** — Tour of the candidate models. One-sentence summary per model, pointing at each model's full specification under [models/](models/). Comparative table of state structure, clock structure, expected stability, expected topological behavior. Identifies where each model is expected to succeed and where to fail.

3. **`03-test-bench.md`** — Standardized test inputs and observables. Defines signal translation: how a paradigm-neutral "unit pulse" is realized in each model's native state. Defines paradigm-neutral observables (energy in a region, propagation speed, reflection/transmission coefficients, field decay laws). Each test specifies inputs, outputs, and metrics. Tests planned: 1D pulse propagation, 2D Y-junction scattering, 2D wavefront, 2D static-field with defect, sim-maxwell fidelity.

4. **`04-model-comparison.md`** — Run all candidate models on all tests. Tabulate results. Identify which models pass / fail / partially-pass. Select the winning model. Document any model-specific surprises and how they affect downstream chapters.

5. **`05-substrate-quantization.md`** — Replace each register's real-valued state with integers from a finite alphabet, eventually a single bit. At what alphabet size and lattice resolution does the chapter-4 test bench still pass? Lattice-gas-automaton scaling: does continuum behavior re-emerge by "zooming out" from a Planck-scale bit substrate to a Compton-scale effective theory? Decision point at the end: continue the rest of the project with the real-valued model as effective theory, or commit to bit-level dynamics. Subsumes [grid-quantizing.md](grid-quantizing.md).

6. **`06-3d-extension-and-lattice-closures.md`** — Extend Scattering to 3D. Pick a 3D lattice (cubic, FCC, or diamond) and work out the edge-orientation conventions; verify the S-matrix S = (2/N)·J − I gives stable propagation at the new coordination. Define the lattice closures that anchor the wrap-promotion ladder: open chain (L0), ring (L1), plaquette (L2), 2-sheet wrap / torus (L3). Mostly mathematical / structural, with computational verification at the end.

7. **`07-wrap-promotion-modeling.md`** — Mathematical modeling of each wrap level. For each closure: what observable on Scattering's dynamics corresponds to the physical phenomenon (mass at L1 / L2, charge at L3)? Computational tests where feasible — for instance, does Scattering on a closed ring host a stable circulating wavepacket whose effective mass can be read off the dispersion curve? Honest about what we *establish* (specific observables on specific closures) versus what we *interpret* (their identification with mass / charge).

8. **`08-where-alpha-appears.md`** — Locate α on the wrap-promotion ladder. Working hypothesis: α lives at L3 only (mass → charge wrap). Identify candidate lattice invariants — combinatorial factors, ratios of winding numbers, fixed points of an RG-like flow — and check which (if any) approximate 1/137. Honest scope: this chapter probably proposes a candidate observable rather than deriving α exactly.

9. **`09-node-decomposition.md`** — Y-tree decomposition: any N-port S-matrix factors into a network of 3-port S-matrices joined by zero-length internal edges. So a coord-N node *is* a configuration of mini-edges and mini-nodes inside a bubble. The reverse — building an edge from nodes — turns out to be asymmetric: edges are pure swap, with no internal degrees of freedom to decompose. This asymmetry is the substantive answer to the original grid-couplet question of whether the two primitives are genuinely distinct.

10. **`10-closing-summary.md`** — Consolidate established results, ruled-out items, unexpected findings. Compare with grid-primitive: where the analog-first cylinder and digital-first winning-model converge / diverge.

Each chapter is added one at a time. The arc is a sketch, not a contract.
