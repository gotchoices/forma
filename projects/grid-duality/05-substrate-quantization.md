# Chapter 5: Substrate quantization

## §1. The chapter's job

The chapter-4 winning model (Scattering) carries real-valued amplitudes in its registers — one floating-point number per edge-end. The Forma framework's substrate, however, is informational: GRID's axiom A5 assigns ζ ≈ 1/4 bit per Planck cell, anchored in the Bekenstein–Hawking bound. If cells are taken seriously as the smallest informational units, real-valued amplitudes are an effective theory and the fundamental dynamics should be in terms of bits — or at most a few bits per cell.

This chapter asks: under what conditions does Scattering with quantized state recover the chapter-4 test-bench results? Two specific questions:

1. *Does naive rounding to a finite alphabet survive?* For each level count N, run the test bench and measure how much the result deviates from the continuous baseline.
2. *Does lattice refinement compensate for low precision?* If quantization noise averages out over many cells, refining the lattice (more cells per macroscopic feature) should recover continuum behavior at any N.

The answers turn out to be more nuanced than the prior at [grid-quantizing.md](grid-quantizing.md) §6.1 anticipated, and they bear on which version of the substrate hypothesis the project should commit to going forward. Decision at the end: continue with real-valued Scattering as effective theory; treat the binary-substrate hypothesis as an open question requiring a different methodology than naive rounding.

## §2. The quantizer

The implementation is in [scripts/models.py](scripts/models.py) under `QuantizedScattering`. After every clock cycle, each register's value is rounded to the nearest level in a fixed set of N values, symmetrically distributed about zero with spacing amp_max / ((N − 1) / 2):

> levels = { −amp_max, …, −2·step, −step, 0, +step, +2·step, …, +amp_max }
>
> step = amp_max / ((N − 1) / 2)

For N = 3: levels = {−amp_max, 0, +amp_max} (one positive level, one negative, plus zero).
For N = 5: {−amp_max, −amp_max/2, 0, +amp_max/2, +amp_max}.
For N = 257: 257 levels with spacing amp_max / 128 ≈ 0.008·amp_max — effectively continuous.

N must be odd for zero to be representable; even N degenerates to N − 1 in practice. (A pathology of even-N naive quantization: any zero-init register snaps to ±amp_max because there is no level at zero, instantly inflating the energy by orders of magnitude. Odd N avoids this trivially.)

This is **naive** quantization in the sense of [grid-quantizing.md](grid-quantizing.md) §6.1: round, don't enforce bit-count conservation per scattering event. The lattice-gas-automaton tradition uses Boolean rules that conserve bit count per junction exactly (FHP-style); those are physically more natural and avoid noise compounding, but require explicit collision-rule design for each coordination. Naive rounding is the diagnostic baseline.

The `amp_max` parameter is set per experiment to match the actual signal amplitude scale, so quantization granularity tracks signal range. Setting amp_max much larger than the typical signal makes most levels unused; setting it much smaller clamps the dynamics. A factor of unity between amp_max and IC peak amplitude is the working choice.

## §3. Experimental program

Four experiments on the existing chapter-3 test bench, in [scripts/test_quantization_sweep.py](scripts/test_quantization_sweep.py):

- **A** — *Stability vs N at fixed lattice.* The S1 2D-pulse test on a 14×14 hex torus, 100 steps, IC amplitude 0.5, amp_max = 0.5. Sweep N ∈ {∞, 257, 65, 17, 9, 5, 3}. Measure final/initial energy ratio.
- **B** — *Stability with lattice refinement at fixed low N.* Same test as A, fix N = 17, sweep lattice scale s ∈ {1, 2, 3, 4} (lattice sizes 14×14, 28×28, 42×42, 56×56). The pulse width is scaled with s so it occupies a constant fraction of the lattice. If naive quantization noise averages out spatially, the energy ratio should approach 1.0 as s grows.
- **C** — *Y-junction matched impedance vs N.* The L2 test on a Y-tree with three 60-cell arms, 90 steps, IC amplitude 0.3, amp_max = 0.4. Sweep N. Measure the per-arm energy fractions; matched-impedance theory gives 1/9, 4/9, 4/9.
- **D** — *Y-junction with arm-length scaling at low N.* Fix N = 17, sweep arm length ∈ {60, 120, 240, 480} with wavepacket parameters scaled proportionally (so the wave fills the same fraction of an arm). Tests whether longer arms help recover theory at fixed precision.

## §4. Results

### Experiment A — stability vs N

| N | bits/cell | initial energy | final energy | ratio (target ≈ 1) |
|---|---|---|---|---|
| ∞ (Scattering) | 64 | 6.010 | 6.010 | **1.000×** |
| 257 | 8.0 | 5.988 | 6.157 | 1.03× |
| 65 | 6.0 | 6.268 | 6.564 | 1.05× |
| 17 | 4.1 | 6.305 | 15.727 | 2.49× |
| 9 | 3.2 | 5.250 | 30.328 | 5.78× |
| 5 | 2.3 | 8.250 | 40.125 | 4.86× |
| 3 | 1.6 | 0.000 | 0.000 | n/a (IC vanished) |

At N = 257 (8 bits) the dynamics is indistinguishable from continuous to within 5%. At N = 65 (6 bits) it is still within 5%. At N ≤ 17 (≤ 4 bits) drift becomes substantial — energy grows by 2.5× to 6×. At N = 3 (1.6 bits) the IC itself rounds to zero and there is no signal.

The drift is *systematic*: log–log fit of (ratio − 1) vs 1/N over the recoverable range gives a slope steeper than 1/N (closer to 1/N² near the breakdown), but the data span is too narrow for a clean exponent. The qualitative picture is clear — at high precision, drift is negligible; at low precision, drift compounds super-linearly.

### Experiment B — stability with lattice refinement at N = 17

| Lattice | initial energy | final energy | ratio |
|---|---|---|---|
| 14×14 (s=1) | 6.305 | 15.727 | 2.49× |
| 28×28 (s=2) | 26.859 | 76.793 | 2.86× |
| 42×42 (s=3) | 56.555 | 163.195 | 2.89× |
| 56×56 (s=4) | 101.508 | 267.645 | 2.64× |

Refining the lattice does **not** reduce the relative drift. The ratio stays roughly constant at 2.5–3× across all four lattice sizes. The absolute drift grows in proportion to the system size (the wavepacket is scaled with the lattice), but the relative noise contribution is unchanged.

This is the key negative finding. The hypothesis of [grid-quantizing.md](grid-quantizing.md) §5.2 was that quantization noise averages out under spatial coarse-graining, with M ∝ 1/N². That argument assumes *random*, spatially independent noise. Naive rounding produces *correlated* noise — neighboring cells have similar continuous values that round in the same direction, so spatial averaging does not cancel them. The error is systematic, and the analog-averaging recovery does not happen under naive rounding.

To get spatial coarse-graining to work, the rule must conserve bit count exactly per scattering event (FHP-style Boolean rules). Naive rounding cannot reach the regime where the binary-substrate hypothesis is supposed to hold.

### Experiment C — Y-junction matched impedance vs N

| N | arm 0 (R²) | arm 1 (T²) | arm 2 (T²) |
|---|---|---|---|
| ∞ (theory: 0.1111 / 0.4444 / 0.4444) | 0.1111 | 0.4444 | 0.4444 |
| 257 | 0.1118 | 0.4441 | 0.4441 |
| 65 | 0.1039 | 0.4481 | 0.4481 |
| 17 | 0.1011 | 0.4494 | 0.4494 |
| 9 | 0.2121 | 0.3939 | 0.3939 |
| 5 | 0.0000 | 0.5000 | 0.5000 |
| 3 | 0.0000 | 0.5000 | 0.5000 |

Matched-impedance scattering survives down to N = 17 (4 bits) within ~10% of theory. Below N = 9 the reflection vanishes entirely — the inbound wave splits 50/50 into the two transmission arms with no reflected component. This is a different failure than experiment A: the Y-junction's local linearity is preserved, but the level spacing becomes too coarse to represent the small reflected fraction (1/9 of the wave amplitude after one scattering event).

### Experiment D — Y-junction with arm-length scaling at N = 17

| Arm length | arm 0 (R²) | arm 1 (T²) | arm 2 (T²) |
|---|---|---|---|
| 60 (s=1) | 0.1011 | 0.4494 | 0.4494 |
| 120 (s=2) | 0.1000 | 0.4500 | 0.4500 |
| 240 (s=4) | 0.0959 | 0.4520 | 0.4520 |
| 480 (s=8) | 0.0991 | 0.4504 | 0.4504 |

At N = 17 the result is already close to theory regardless of arm length — there is no significant improvement from longer arms. This is consistent with experiment B: lattice refinement does not help under naive rounding. At N = 17 the dynamics is *good enough* that no further help is needed; below N = 17 nothing helps.

The plot is in [scripts/output/quantization-sweep.png](scripts/output/quantization-sweep.png).

## §5. What this means for the substrate hypothesis

Two findings, in order:

### Finding 1: real-valued Scattering is robust to moderate quantization

Down to roughly 6 bits per register (N ≈ 65), naive rounding preserves the chapter-4 test bench within a few percent. Down to ~4 bits (N ≈ 17) the matched-impedance test still passes; the stability test drifts by ~2.5× over 100 steps but does not blow up. The chapter-4 verdict survives any quantization that retains at least ~6 bits of precision per cell, which includes any practical floating-point computation and many embedded-hardware representations.

For the project's downstream purposes — chapters 6 onward, where the wrap-promotion ladder and α questions are addressed — this is a clean clearance: the real-valued Scattering model used in those chapters is a faithful effective theory at any reasonable computational precision.

### Finding 2: naive rounding cannot reach the binary substrate

Below ~4 bits per register, naive quantization breaks down in two distinct ways: stability fails (energy grows uncontrolled) and matched impedance fails (reflection coefficient drops to zero). Lattice refinement does not recover the result, because the rounding noise is systematic, not random. Refining the lattice by a factor of 4 keeps the relative drift constant, contrary to the analog-averaging prediction.

The reason is structural. The analog-averaging argument of [grid-quantizing.md](grid-quantizing.md) §5.2 assumes spatially independent noise, which can be reduced by averaging over many cells. Naive rounding produces *correlated* noise — neighboring cells with similar values round in the same direction, so spatial coarse-graining does not cancel the noise.

To reach the binary substrate as the doc envisioned — bit-level dynamics with continuous behavior emerging in the macroscopic limit — the update rule must be **bit-count-conservative** per scattering event. The lattice-gas-automaton tradition (FHP, lattice Boltzmann, quantum lattice gas) has the technology: design a deterministic Boolean rule mapping incoming bit configurations at a Y-junction to outgoing configurations such that bit count, parity, and lattice symmetries are all conserved. Such rules exist but require explicit construction and are not the same as rounding the continuous Scattering update.

This is the open work. It is a real research program, not a quick refinement of this project.

## §6. Decision for chapters 6 and beyond

The chapters that follow (3D extension, wrap-promotion modeling, α, node decomposition) have two possible substrate footings:

- **Real-valued Scattering** (the chapter-4 model). Effective theory, well-understood, robust under moderate quantization. Continuous mathematics applies directly.
- **Bit-conservative Boolean Scattering** (the FHP-style binary substrate). Physically more natural under axiom A5, but its construction is open work that this chapter has not done.

The decision: **continue with real-valued Scattering as the effective theory.** The chapter-4 verdict carries forward unchanged; chapters 6 onward use the continuous model and its standard mathematics. The binary-substrate question is acknowledged as a deeper-substrate hypothesis that this project does not commit to but does not preclude. If a future project develops the bit-conservative rules and shows continuum recovery at lattice scales, the chapter-4 verdict will become an effective-theory limit of that deeper model — without revision.

This decision keeps the project's scope focused on the wrap-promotion / α questions while honestly acknowledging that the substrate-quantization question is open. It is neither a refutation nor a confirmation of the binary-substrate hypothesis. It is an empirical note that *naive* rounding is in the wrong noise regime for spatial averaging to recover continuum behavior, and that bit-conservative rules are the path to a meaningful binary substrate.

## §7. Closing pointer

Real-valued Scattering survives quantization down to ~6 bits per cell. Naive rounding to fewer bits accumulates systematic, non-averaging error. The binary-substrate hypothesis remains open and requires bit-conservative Boolean rules, which this chapter does not develop. The project continues with the real-valued model.

The chapter sequence is summarized in the project [README](README.md).
