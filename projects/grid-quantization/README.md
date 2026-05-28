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

Run: `python run_recirculation.py [--test loop|bound|circ|disp|all]`
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
- **bound** — *the surprise.* A generic circulating excitation on one
  hexagon deposits **~51% into a non-radiating compact localized
  state** that persists indefinitely (flat to t=300; verified
  wraparound-free); the rest radiates in one tick. The bound pattern
  has amplitudes ±1/√3, ∓(1−1/√3). **Loops genuinely trap energy** —
  the bound/standing (massive-particle-like) limit, coexisting with
  the propagating photon band. This overturned the pre-sim guess that
  loops are overdamped. Caveat: one localized eigenmode is not yet
  "quantization at every frequency" — see
  [work/tier2-design.md](work/tier2-design.md) §2.
- **circ** — a trapped single-hexagon loop mode carries peak
  circulation 6× its amplitude; a propagating wavefront ≈ 2×.
  Circulation concentrates in recirculating energy and cancels for
  clean propagation (the zigzag-cancellation picture).
- **disp** — plane-wave dispersion is linear, ω ≈ 0.41·k, across the
  long-wavelength regime: the injected static perturbation becomes a
  travelling oscillation with a definite (non-dispersive) dispersion
  relation. (0.41 is the phase velocity along x; it need not equal
  sim-maxwell's ≈0.73 pulse-centroid speed.)

### Band structure (`band_structure.py`) — explains the bound state

Diagonalizing the one-tick Bloch operator over the Brillouin zone
(built empirically from `scatter_step`; cross-checked against
real-space diagonalization) gives **2 flat bands (ω = 0 and ω = π) +
4 dispersive bands**. The flat bands (group velocity 0) host the
compact localized states — so the **bound** test's trapped mode is
explained: it is a CLS on the **ω = 0 flat band** (static). The
dispersive bands are the propagating modes (max group velocity ≈0.86;
small-k slope = the 0.41 phase velocity).

This answers the loss-vs-frequency question: **Q is non-monotonic in
ω** — effectively infinite at the flat bands (ω = 0, π) and low
mid-band where group velocity (radiative coupling) peaks; *not* a
simple "Q down with frequency." *(Lesson: the first detector —
per-band bandwidth — wrongly reported "no flat band" because the flat
bands coincide with dispersive band edges; density-of-states is the
right detector. See [work/tier2-design.md](work/tier2-design.md) §3.)*

### Loop-size scaling (`loop_scaling.py`) — a scale-invariance hint

Exciting the **boundary of a patch of K hexagons** as a coherent
circulating mode and measuring the trapped (non-radiating) fraction:

| hexagons | perimeter P | trapped fraction |
|---:|---:|---:|
| 1 | 6 | 0.509 |
| 7 | 20 | 0.507 |
| 19 | 34 | 0.509 |
| 37 | 46 | 0.509 |

**The trapped fraction is ~½ independent of loop size.** So a bigger
loop is *not* lossier for the coherent mode (only a single traveling
pulse is, exponentially as (2/3)^(2P)). The binding efficiency is the
same at every loop size — i.e. every frequency scale. This is a
concrete instance of the **scale-invariance** the h-universality
argument needs (Q140 §3a): supportive, though not yet proof (that
still requires the per-cycle *action*, Tier 2).

## What Tier 1 does NOT yet show

- **That the bound state means quantization.** The compact localized
  state shows loops *can* trap energy; it is not yet integer
  occupation or ℏω-per-quantum. That linkage is Tier 2.
- **Running coupling.** Whether the cumulative coupling of a *row* of
  plaquettes runs from the bare 1/129.7 toward 1/137 (Q140 §5
  prediction b) is really about the *virtual* recirculatory dressing,
  which a lossless scalar model does not expose as energy transfer —
  so it is a Tier 2 (phasor) question, not a clean Tier 1 one.
- **Exponent robustness.** The count is unambiguously 12 for the
  isolated path (6 edges × 2), since T = 2/3 is confirmed
  path-independent; the open part is whether the *physically relevant*
  coupling is the bare path or a dressed value (Tier 2).
- **Anything about h.** Tier 1 is energy ratios only; the
  frequency-independence of the per-cycle action is Tier 2.

## Files

| File | Contents |
|------|----------|
| [README.md](README.md) | This document |
| [lib.py](lib.py) | Self-contained honeycomb lattice + junction scatter + evolve (adapted from grid/sim-maxwell/run_hex.py) |
| [run_recirculation.py](run_recirculation.py) | Tier 1 measurements: loop leakage, bound state, circulation, dispersion |
| [band_structure.py](band_structure.py) | Bloch band structure (empirical U(k) from scatter_step); flat-band / bound-state analysis |
| [loop_scaling.py](loop_scaling.py) | Trapped (bound) fraction vs loop size — the scale-invariance check |
| [work/tier2-design.md](work/tier2-design.md) | The bound-state finding, the confirmed band structure, and the Tier 2 (h-universality) plan |
| [outputs/](outputs/) | Figures (`recirc_*.png`, `band_structure.png`, `loop_scaling.png`) and `loop_decay.csv` data |

## Background and cross-references

- [Q140](../../qa/Q140-light-quantization-from-recirculation.md) — the conjecture, in full, with the α arithmetic and caveats
- [grid/foundations.md](../../grid/foundations.md) — axioms; Q1 (block-spin RG fixed point) is the same question as Tier 2's h-universality
- [grid/maxwell.md](../../grid/maxwell.md) — junction → Maxwell; charge as the 2π vortex (the single-valuedness rule reused here)
- [grid/fields.md](../../grid/fields.md) — Y-junction symmetric/helical (E ± iB) eigenmodes; the spin/polarization story
- [grid/hexagonal.md](../../grid/hexagonal.md) — N=3 vs N=6 junction scattering; the 2/3 transmission used here
- [grid/sim-maxwell/](../../grid/sim-maxwell/) — the completed substrate study this project's lattice code is adapted from
- [grid/compact-dimensions.md](../../grid/compact-dimensions.md) — the *other* (torus-wrapping) route to α, which found α a "designer's choice"; this project pursues the leakage route instead (INBOX items D/F)

## Next steps

Detailed plan in [work/tier2-design.md](work/tier2-design.md). In order:

1. ~~**Band structure**~~ — **done** (`band_structure.py`): 2 flat
   bands (ω=0, π) + 4 dispersive; the bound state is the ω=0 flat-band
   CLS.
2. **Resolve the per-cycle-action definition** on paper (the main
   Tier 2 design risk — work/tier2-design.md §5). This is the gate.
3. **Tier 2**: complex amplitudes + helical (E ± iB) mode decomposition;
   measure circulation-mode action per cycle vs ω, and test the
   h-universality / RG-fixed-point prediction (with the block-spin
   cross-check). Substantial; its own module here.

Smaller clean follow-up now available: construct the CLS explicitly
from the ω=0 flat-band states and check whether *larger* compact
localized states exist (bears on the "loop tower" of Q140 §3a).
