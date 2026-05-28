# grid-quantization

**Type:** Exploratory / speculative project (see [../README.md](../README.md))
**Scope:** A GRID-only account of why light is quantized — and whether
h and α can be *derived* (not assumed) from lattice recirculation.
**Method:** Working hypothesis first; computational probes where they
settle a question; mathematical derivation as the eventual target.
**Status:** Tier 1 complete (single-loop leakage, circulation,
dispersion). Tier 2 (phase winding / per-cycle action / RG fixed
point) not yet started.

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

## The mechanism in one paragraph

The honeycomb (N=3) junction rule `outgoing = (2/3)·total − incoming`
is the discrete wave equation; its sign-flipped reflection (−1/3) is
the restoring "spring," so an injected static perturbation oscillates
and propagates. At every junction the wave also spawns a closed
recirculation loop. Two consequences are conjectured:

- **Quantization.** A dense tower of loop sizes acts as a near-
  infinite set of *virtual compact dimensions*; every frequency finds
  a resonant loop, and single-valuedness (∮∂θ = 2πn, the same rule
  GRID already uses for charge) forces integer winding. Self-
  similarity across scales would make the per-cycle action — i.e. h —
  frequency-independent. This is the same question as foundations Q1
  ("is the junction rule a block-spin RG fixed point?").
- **Coupling.** A propagating wave leaves a linear array of low-Q
  loops along its path — a per-vertex coupling, the lattice form of a
  dressed propagator. The single-hexagon energy-return fraction is
  the bare coupling: (2/3)¹² = 1/129.75, which sits inside α's
  physical running range (1/137 low-E, 1/128 at the Z mass).

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
[lib.py](lib.py) rather than importing the grid/ substrate code.

## Tier 1 results

Run: `python run_recirculation.py [--test loop|circ|disp|all]`
(from the repo root, with `.venv` active). Outputs in
[outputs/](outputs/).

- **loop** — a single pulse sent around one hexagon decays as
  *exactly* (2/3)ᵏ for the first three junctions (ratio 1.000 to
  machine precision; see [outputs/loop_decay.csv](outputs/loop_decay.csv)).
  Per-junction transmission **T = 2/3** confirmed ⇒ isolated single-
  loop **energy return (2/3)¹² = 1/129.75**, inside α's running range.
  Ticks 4–6 are contaminated by returning short reflected walks, so
  the clean number is the early single-step transmission extrapolated
  as T¹².
- **circ** — a trapped single-hexagon loop mode carries peak
  circulation 6× its amplitude; a propagating wavefront ≈ 2×.
  Circulation concentrates in recirculating energy and cancels for
  clean propagation (the zigzag-cancellation picture).
- **disp** — plane-wave dispersion is linear, ω ≈ 0.41·k, across the
  long-wavelength regime: the injected static perturbation becomes a
  travelling oscillation with a definite (non-dispersive) dispersion
  relation. (0.41 is the phase velocity along x; it need not equal
  sim-maxwell's ≈0.73 pulse-centroid speed.)

## What Tier 1 does NOT yet show

- **Running coupling.** Does the cumulative coupling of a *row* of
  plaquettes accumulate from the bare 1/129.7 toward the low-energy
  1/137? (Q140 §5 prediction b — tractable in this same script.)
- **Exponent robustness.** Does the count stay 12 under careful
  entry/exit bookkeeping, or do the −1/3 reflections / re-injection
  shift it? (Q140 §5 caveat 1.)
- **Anything about h.** Tier 1 is energy ratios only; the
  frequency-independence of the per-cycle action is Tier 2.

## Files

| File | Contents |
|------|----------|
| [README.md](README.md) | This document |
| [lib.py](lib.py) | Self-contained honeycomb lattice + junction scatter + evolve (adapted from grid/sim-maxwell/run_hex.py) |
| [run_recirculation.py](run_recirculation.py) | Tier 1 measurements: loop leakage, circulation, dispersion |
| [outputs/](outputs/) | Figures and `loop_decay.csv` data |

## Background and cross-references

- [Q140](../../qa/Q140-light-quantization-from-recirculation.md) — the conjecture, in full, with the α arithmetic and caveats
- [grid/foundations.md](../../grid/foundations.md) — axioms; Q1 (block-spin RG fixed point) is the same question as Tier 2's h-universality
- [grid/maxwell.md](../../grid/maxwell.md) — junction → Maxwell; charge as the 2π vortex (the single-valuedness rule reused here)
- [grid/fields.md](../../grid/fields.md) — Y-junction symmetric/helical (E ± iB) eigenmodes; the spin/polarization story
- [grid/hexagonal.md](../../grid/hexagonal.md) — N=3 vs N=6 junction scattering; the 2/3 transmission used here
- [grid/sim-maxwell/](../../grid/sim-maxwell/) — the completed substrate study this project's lattice code is adapted from
- [grid/compact-dimensions.md](../../grid/compact-dimensions.md) — the *other* (torus-wrapping) route to α, which found α a "designer's choice"; this project pursues the leakage route instead (INBOX items D/F)

## Next steps

1. Add a row-of-plaquettes cumulative-coupling measurement to
   `run_recirculation.py` and test whether it runs toward 1/137.
2. Settle the exponent-robustness question (entry/exit bookkeeping).
3. Stand up Tier 2: complex amplitudes + helical mode decomposition,
   measure circulation-mode action per cycle vs ω, and test the
   fixed-point (h-universality) prediction. This is a substantial
   extension and will live in its own module/work folder here.
