# grid-quantization

**Type:** Exploratory / speculative project (see [../README.md](../README.md))
**Scope:** A GRID-only account of why light is quantized — and whether
h and α can be *derived* (not assumed) from lattice recirculation.
**Method:** Working hypothesis first; computational probes where they
settle a question; mathematical derivation as the eventual target.
**Status:** Tier 1 + band structure + scale-invariance complete;
the countability question (P3) has a candidate derivation sketch.
**Headline:** GRID recirculation derives the photon's mode structure,
spin, an α-*scale* leakage coupling (1/129.7, inside α's running
range — *not* a closed derivation of α, which is an axiom (A6); see
[Q140 §5](../../qa/Q140-light-quantization-from-recirculation.md) for
the exponent/running caveats), bound modes, and the quantization *structure*
(harmonic ⇒ uniform quanta; scale-invariance ⇒ ℏ universal). ℏ's
scale is a unit, not a prediction. **Countability** (integer
occupation — the lone imported piece) now has a candidate derivation
from A3+A5 via the dual-of-a-circle theorem (U(1)↔ℤ), resting on one
interpretive reading of A5 — *plausibly the same finite-information
principle that underwrites GRID's gravity, though that the two
readings are literally the same is unproven (see
[work/countability-from-information.md](work/countability-from-information.md)
§8).* So finite information (A5) may be a shared root of both gravity
and quantum discreteness. Net: the quantum is *reduced* to one
interpretive question + one unit, not left a mystery. (Derives
countability, not yet all of QM.)

## Why this project exists

GRID derives Maxwell's equations and Newton's G from a discrete
lattice ([../../grid/](../../grid/)), but it does **not** derive two
things it leans on:

- **h** is set to 1 by the natural-unit convention and is an *input*
  to the gravity chain (it sits inside the Unruh temperature and the
  Bekenstein–Hawking entropy). It is never an output.
- **light quantization** (every free-space frequency carrying integer
  ℏω quanta) is asserted via a de Broglie postulate, the same place
  standard QM inserts h.

This project pursues a single conjecture that would close both gaps
*without* invoking MaSt particle sheets — light is a promotion
phenomenon of the substrate itself:

> Light quantization arises from **closed recirculation loops** in
> the GRID lattice. A propagating wave is dressed by recirculating
> components at every loop scale (the lattice is self-similar). Loop
> single-valuedness forces integer winding, which quantizes the
> action carried per cycle; loop leakage at the smallest scale sets
> the coupling α.

The conjecture is captured in
[Q140](../../qa/Q140-light-quantization-from-recirculation.md). This
project is its development home.

## Presentation arc

The exploratory phase has converged. A clean linear derivation — *how
information becomes light, and why light is quantized, from GRID* —
runs in seven chapters. Each is tagged by what it actually delivers:
**[derived]** (from GRID axioms + computation), **[reduced]** (standard
physics shown to rest on a single GRID ingredient), or **[conjecture]**
(graded, open). The honest result is a *reduction*, not a new physics:
the quantization *structure* is grid-native, ℏ is a unit, and "light is
quantized" collapses to one named hinge reached two independent ways.

1. **The substrate and the junction rule** — *[derived]* the honeycomb
   lattice; the periodic, bounded phase cell (A3); the equal-impedance
   rule `outgoing = (2/3)·total − incoming` and its −1/3 restoring term.
2. **Information becomes a wave** — *[derived]* the restoring term turns
   an injected static perturbation into a travelling oscillation; linear
   dispersion (ω ≈ 0.41·k); the helical Y-junction eigenmodes as the two
   photon helicities (spin/polarization). *Answers "how information
   becomes light."*
3. **The modes of light** — *[derived]* the Bloch band structure:
   dispersive bands (free photons) and flat bands (compact-localized /
   bound, the mass-like limit); which frequencies exist (P1); each mode
   an exact harmonic oscillator (P2); scale-invariance as an IR fixed
   point.
4. **ℏ is a unit, not a target** — *[reduced]* the principle-vs-scale
   reframe; ℏ = dW·τ and c = L/τ as grain-combinations (Planck-unit
   structure; the absolute scale is pinned by ζ via gravity — an
   identification, not a theorem); h is not derivable from α (a pure
   number cannot fix a dimensionful quantity). The dimensionless content
   is ζ and α.
5. **Why light is quantized: periodicity, not discreteness** —
   *[reduced]* single-valuedness on the compact phase gives a discrete
   (integer) spectrum (Fourier series / U(1)↔ℤ), and that integer is the
   occupation number (P3 + P4). Two independent routes — topological
   (countability) and energetic (bounded substrate + conserved count) —
   converge on this one fact. Continuous phase → unbounded ladder (QED);
   finite phase (A5) → bounded ladder (a GRID deviation). *Answers "why
   light is quantized."*
6. **The one imported piece, and the shared root** — *[conjecture]* the
   lone hinge: the substrate's state must be an amplitude/distribution
   over the phase (A5's informational reading), not a sharp classical
   value. This is the same finite-information axiom that gives GRID its
   gravity — so finite information would be a shared root of gravity and
   quantum discreteness (unproven; the equivalence of the two A5 readings
   is the open task). The α-scale leakage coupling (1/129.7) and the
   bounded ladder enter here as graded GRID-specific signatures.
7. **The honest ledger** — *[scope]* what is derived (info → light;
   P1, P2, P4; ℏ as a unit; P3 reduced to one hinge), what is imported /
   conjectured (the A5 reading; α; the shared root), and what is out of
   scope (full QM — interference, the Born rule). Open computational
   probes: the bit-conserving sigma-delta substrate rule, and
   loop-closure / emergent-photon sectors.

The raw material for these chapters already exists in the work files
(below); the arc is the order in which to present it as a derivation.

## The mechanism in one paragraph

The honeycomb (N=3) junction rule `outgoing = (2/3)·total − incoming`
is the discrete wave equation; its sign-flipped reflection (−1/3 —
derived in [grid/hexagonal.md](../../grid/hexagonal.md) and simulated
in [grid/sim-maxwell/](../../grid/sim-maxwell/)) is the restoring
"spring," so an injected static perturbation oscillates and
propagates. At every junction the wave also spawns a closed
recirculation loop. Two consequences are conjectured:

- **Quantization.** A dense tower of loop sizes acts as a near-
  infinite set of *virtual compact dimensions*; every frequency finds
  a resonant loop, and single-valuedness (∮∂θ = 2πn, the same rule
  GRID already uses for charge) forces integer winding. Self-
  similarity across scales would make the per-cycle action — i.e. h —
  frequency-independent. This is the same question as foundations Q1
  ("is the junction rule a block-spin RG fixed point?"). *(Caveat: the
  band structure below puts the trapped/bound modes only at ω=0 and
  ω=π — not at a frequency-matched tower — so the "resonant loop per
  frequency" picture is this conjecture's most speculative element,
  not a sim result.)*
- **Coupling.** A propagating wave is dressed at each vertex it passes
  by a *virtual* recirculatory component — a per-vertex coupling, the
  lattice form of a dressed propagator. (In the lossless linear sim
  this dressing is virtual phase, not real shed energy: a clean
  propagating eigenmode leaves nothing trapped in its wake — the
  permanent trapping in the **bound** test below requires a
  deliberately-injected non-propagating mode, not a passing photon.)
  The single-hexagon energy-return fraction is the bare coupling:
  (2/3)¹² = 1/129.75, which sits inside α's physical running range
  (1/137 low-E, 1/128 at the Z mass).

Spin/polarization come from the same structure: the helical
circulation eigenmodes of the Y-junction are the two photon
helicities — so this needs no ℵ-line.

## Two tiers

| Tier | Question | State variable | Status |
|------|----------|----------------|--------|
| **1** | Single-loop leakage ≈ α? Why does it oscillate? | Real scalar amplitudes (energy ratios) | **Done** — see below |
| **2** | Is the per-cycle action (h) frequency-independent? (RG fixed point) | Complex/phasor amplitudes (phase winding) | Not started |

Tier 1 needs only energy ratios, which real amplitudes give. Tier 2
needs to track *integer phase winding* and the symmetric/helical mode
decomposition, which requires complex amplitudes and a modified
scatter rule — the reason this project keeps its own
[lib.py](scripts/lib.py) rather than importing the grid/ substrate code.

## Computational results

The computational arc is complete — Tier 1 (loop leakage, the bound
state, circulation, dispersion), the Bloch **band structure** (2 flat
bands + 4 dispersive — the flat band explains the bound state), the
**loop-size scaling** (trapped fraction ~½, scale-invariant), the
**mode-projection** check (the ~½ is *not* the zero-point ½), and the
**scale-invariance** of the photon band (linear ω ≈ 0.41·k, an IR
fixed point). The conclusions are in the Headline above; the full
results, tables, methodology, and caveats live in the work files.

**Run** (with the repo `.venv` active, from this project folder):

    python scripts/run_recirculation.py [--test loop|bound|circ|disp|all]
    python scripts/band_structure.py
    python scripts/loop_scaling.py
    python scripts/mode_projection.py
    python scripts/scale_invariance.py

Figures and data land in [outputs/](outputs/).

**Where the results are written up:**

- [work/tier2-design.md](work/tier2-design.md) §1–§3 — Tier 1, the
  bound-state finding, the band structure, and the loop-size /
  scale-invariance results.
- [work/tier2-design.md §4](work/tier2-design.md) — the
  principle-vs-scale reframe and the P1–P4 decomposition of "light is
  quantized."
- [work/countability-from-information.md](work/countability-from-information.md)
  — the P3 (countability) derivation sketch from A3 + A5 via U(1)↔ℤ.
- [work/energy-and-coherence.md](work/energy-and-coherence.md) — a
  second route to P3 and ℏ's scale from a bounded ±1 substrate.

## What this project does NOT show

- **Full QM** (complex amplitudes, interference, the Born rule). The
  P3 sketch derives *countability* (integer occupation) from A5+A3,
  not the complex-amplitude structure. Whether A5's informational
  state must be a complex amplitude (⇒ interference) or only a real
  distribution (⇒ countability alone) is open
  (work/countability-from-information.md §8).
- **A rigorous A5 reading.** The P3 sketch's one load-bearing step —
  A5's state is a distribution over the compact phase — is graded
  *interpretive*; hardening it (showing it is the same reading A5 gets
  in the gravity derivation) is the next foundational task.

## Files

| File | Contents |
|------|----------|
| [README.md](README.md) | This document |
| [lib.py](scripts/lib.py) | Self-contained honeycomb lattice + junction scatter + evolve (adapted from grid/sim-maxwell/run_hex.py) |
| [run_recirculation.py](scripts/run_recirculation.py) | Tier 1 measurements: loop leakage, bound state, circulation, dispersion |
| [band_structure.py](scripts/band_structure.py) | Bloch band structure (empirical U(k) from scatter_step); flat-band / bound-state analysis |
| [loop_scaling.py](scripts/loop_scaling.py) | Trapped (bound) fraction vs loop size — the scale-invariance check |
| [mode_projection.py](scripts/mode_projection.py) | Exact projection of excitations onto the bound subspace (settles the "is it the ZPE ½?" question — no) |
| [scale_invariance.py](scripts/scale_invariance.py) | Dispersion linearity vs wavelength — the IR-fixed-point / scale-invariance check |
| [work/tier2-design.md](work/tier2-design.md) | The bound-state finding, the band structure, the principle-vs-scale reframe, and the Tier 2 plan |
| [work/countability-from-information.md](work/countability-from-information.md) | Derivation sketch: countability (P3) from A3 (compact phase) + A5 (informational state) via U(1)↔ℤ |
| [work/energy-and-coherence.md](work/energy-and-coherence.md) | Second route to P3 + ℏ's scale: a bounded ±1 substrate with a fixed flip-cost forces E ∝ ω and fixes the action unit ℏ = dW·τ; conservation carries the discrete total through dispersion, leaving a bit-conserving-dynamics gate + the topological per-mode lock |
| [outputs/](outputs/) | Figures (`recirc_*.png`, `band_structure.png`, `loop_scaling.png`) and `loop_decay.csv` data |

## Background and cross-references

- [Q140](../../qa/Q140-light-quantization-from-recirculation.md) — the conjecture, in full, with the α arithmetic and caveats
- [grid/foundations.md](../../grid/foundations.md) — axioms; Q1 (block-spin RG fixed point) is the same question as Tier 2's h-universality
- [grid/maxwell.md](../../grid/maxwell.md) — junction → Maxwell; charge as the 2π vortex (the single-valuedness rule reused here)
- [grid/fields.md](../../grid/fields.md) — Y-junction symmetric/helical (E ± iB) eigenmodes; the spin/polarization story
- [grid/hexagonal.md](../../grid/hexagonal.md) — N=3 vs N=6 junction scattering; the 2/3 transmission used here
- [grid/sim-maxwell/](../../grid/sim-maxwell/) — the completed substrate study this project's lattice code is adapted from
- [grid/compact-dimensions.md](../../grid/compact-dimensions.md) — the *other* (torus-wrapping) route to α, which found α a "designer's choice"; this project pursues the leakage route instead (INBOX items D/F)
- [projects/grid-duality/grid-quantizing.md](../grid-duality/grid-quantizing.md) — why a *discrete* substrate does not by itself quantize amplitude: a binary lattice gas (FHP) yields continuous macro-physics, and a substrate "photon" is a coarse-grained bit pattern with near-continuous amplitude — so occupation quantization is a separate ingredient, not a consequence of digitization

## Next steps

The computational arc (Tier 1, band structure, scale-invariance) is
done; the conceptual frontier (countability) now has a candidate
derivation. What remains is to **harden the one interpretive step**
(work/countability-from-information.md §8):

1. **Pin the A5 reading.** Show that "A5's state = a distribution over
   the compact phase" is the *same* reading of A5 used in gravity.md's
   entropy counting — which would upgrade the P3 sketch's load-bearing
   step from *interpretive* toward *rigorous* and make the
   gravity↔quantization shared-root claim precise.
2. **Stochastic vs quantum.** Decide whether the informational state
   must be a *complex amplitude* (⇒ interference, more of QM) or only
   a *real distribution* (⇒ countability alone). This bounds how much
   of QM the substrate delivers.
3. **The bounded-ladder prediction.** Compute the per-mode occupation
   cutoff ~2^{Nζ} for a concrete mode; confirm it is unobservably high
   (consistency) and whether any regime makes it matter.

These are foundational reasoning, not sims. The optional lattice
follow-ups remain available (explicit CLS construction; block-spin RG).

A second, complementary route to P3 is developed in
[work/energy-and-coherence.md](work/energy-and-coherence.md): a bounded
±1 substrate with a fixed per-flip work forces E ∝ ω and fixes ℏ's
scale as a substrate unit, reducing light-quantization to a single
coherence hinge. Its first concrete probe is a vertex / height-model
test of whether loop-closure constraints on the ±1 honeycomb admit
discrete winding sectors.

Optional clean follow-ups: construct the CLS explicitly from the ω=0
flat-band states (does a *larger* CLS tower exist — Q140 §3a?); and a
block-spin / decimation RG to test the fixed point more rigorously
than the dispersion-linearity proxy.
