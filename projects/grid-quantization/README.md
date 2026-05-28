# grid-quantization

**Type:** Exploratory / speculative project (see [../README.md](../README.md))
**Scope:** A GRID-only account of why light is quantized — and whether
h and α can be *derived* (not assumed) from lattice recirculation.
**Method:** Working hypothesis first; computational probes where they
settle a question; mathematical derivation as the eventual target.
**Status:** Tier 1 + band structure + scale-invariance complete;
the countability question (P3) has a candidate derivation sketch.
**Headline:** GRID recirculation derives the photon's mode structure,
spin, α (1/129.7), bound modes, and the quantization *structure*
(harmonic ⇒ uniform quanta; scale-invariance ⇒ ℏ universal). ℏ's
scale is a unit, not a prediction. **Countability** (integer
occupation — the lone imported piece) now has a candidate derivation
from A3+A5 via the dual-of-a-circle theorem (U(1)↔ℤ), resting on one
interpretive reading of A5 — *the same reading that already gives
GRID its gravity.* So finite information (A5) would be the single
root of both gravity and quantum discreteness. Net: the quantum is
*reduced* to one interpretive question + one unit, not left a
mystery. (Derives countability, not yet all of QM.)
<!--EC Seems like a stretch to say that we have "found alpha".  Would you agree?  We have found that the amount of light current that recirculates around the loops appears to be close to alpha and this has hinted in other works at being associated with the "leakage", charge, phenomena.  But not sure we've closed the loop yet on "this is alpha".  Push back if you disagree. -->
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
<!--EC Is it grid-duality where we develop the edge/node update rules in some detail?  Wondering if we should refer to the sign-flipped reflection if that is where it is best documented?  Or maybe sim-maxwell does this too? -->
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

**The trapped fraction is ~½ independent of loop size** (this is the
energy on the loop edges; the *total* bound fraction including the
mode's spill onto spokes is 0.571 — see below). So a bigger loop is
*not* lossier for the coherent mode (only a single traveling pulse
is, exponentially as (2/3)^(2P)). The binding efficiency is the same
at every loop size — i.e. every frequency scale. This is a concrete
instance of the **scale-invariance** the h-universality argument
needs (Q140 §3a): supportive, though not yet proof (that still
requires the per-cycle *action*, Tier 2).

### Is the ~½ the zero-point ½? (`mode_projection.py`) — No

Projecting excitations exactly onto the bound (flat-band) subspace:

| excitation | trapped fraction |
|---|---|
| flat-band subspace dimension | 0.338 (2 of 6 bands ≈ 1/3) |
| random state | 0.337 |
| single edge | 0.338 |
| hexagon circulation | **0.571** |
| bound pattern [+,+,−,−,−,+] | 1.000 (pure eigenmode ✓) |

The precise circulation figure is **0.571, not 0.5**, and it is
**excitation-dependent** (a random state hits the subspace fraction
1/3) — so there is no structural/universal ½. The ZPE ½ of
[zpe_derivation.md](../ma-domain/work/zpe_derivation.md) comes from a
*spectral average over a band* and is a *vacuum* quantity — a
different object. The two ½'s were a loose coincidence.
What *is* real: a circulating (photon-like) excitation couples to the
bound sector **~1.7× more than random**, and that ratio is
scale-invariant.

## Tier 2: the quantization principle, and where h comes from

Tier 2 was meant to measure the **per-cycle action** vs ω and test
whether h is frequency-independent. Working through the *definition*
of that quantity (the gate, work/tier2-design.md §4a) hits a wall
worth stating plainly:
<!--EC if h is unity by definition, which it should be in natural units, then why are we focused on the value of h? -->
**The scale of ℏ was never the right target** — it is a *unit* (the
action unit, = 1 by construction, like c), not a dimensionless
prediction. Expecting it to "fall out" was a category error. The
meaningful target is the dimensionless *principle* of quantization,
which decomposes — and the grid supplies most of it:

| piece of "light is quantized" | source |
|---|---|
| **P1** which frequencies exist | grid-derived |
| **P2** each mode is a *harmonic* (linear) oscillator | grid-derived (exact superposition) |
| **P3** occupation *countable* (n ∈ ℤ at all) | the one genuine import |
| **P4** quanta *uniform* (ℏω each) + ℏ *universal* across ω | grid-derived (harmonic ⇒ even ladder; scale-invariance) |
| scale of ℏ | a unit, not a prediction |

P2+P4 are not trivial: *harmonic* oscillators quantize into **even**
ladders — that is *why* every photon of frequency ω is identical with
energy exactly ℏω (an anharmonic medium would give uneven rungs and
no clean photon). The exact linearity of the lattice guarantees the
clean photon picture; the scale-invariance below makes ℏ universal.

**The one imported piece is P3 — countability** (the [a,a†]=1 step).
This now has a **candidate derivation sketch**
([work/countability-from-information.md](work/countability-from-information.md)):
the dual of the compact U(1) phase (A3) is the integers ℤ
[*rigorous* — the same fact as charge quantization, applied to a
mode's **oscillation** phase instead of a spatial loop, which gives
**occupation number** instead of charge], and A5's *informational*
state (a distribution/amplitude over that compact phase, not a sharp
classical value) is what triggers it [*interpretive* — the one
load-bearing assumption]. Integer occupation then follows. A5's
finiteness further predicts a (huge, in-principle) **maximum
occupation per mode** — a GRID deviation from QFT's unbounded ladder.

This also corrects an earlier mistake: "winding only gives charge"
killed the wrong target — photon number is the integer dual of a
*different* compact phase (the mode's oscillation angle).

**Striking corollary:** A5 is the *same* axiom that gives gravity
(entropy → Jacobson → G, gravity.md). So finite information would be
the single root of **both** gravity and quantum discreteness.

**Verdict:** not "failed to derive h" but **"reduced the quantum to
one interpretive reading of A5 (is the substrate's state informational
= a distribution over the compact phase?) plus one unit (ℏ)."** Given
that reading — the same one gravity already uses — integer occupation
is forced by a theorem. Caveat: this derives *countability*, not all
of QM (complex amplitudes / interference / Born rule are a further,
unestablished step).

### Scale-invariance (`scale_invariance.py`) — an IR fixed point

The photon band is **linear, ω ≈ 0.41·k**, with deviation falling as
~k²: 0.1% at λ≈9 L, 1% at λ≈4 L. Real photons (λ/L_P ≳ 10²⁰) see a
scale-free dispersion to ~10⁻⁴⁰ — an excellent IR fixed point, with
scale-invariance breaking only at the Planck scale. So the substrate
supplies the *universality*; it does not supply the *quantum*.

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
| [lib.py](lib.py) | Self-contained honeycomb lattice + junction scatter + evolve (adapted from grid/sim-maxwell/run_hex.py) |
| [run_recirculation.py](run_recirculation.py) | Tier 1 measurements: loop leakage, bound state, circulation, dispersion |
| [band_structure.py](band_structure.py) | Bloch band structure (empirical U(k) from scatter_step); flat-band / bound-state analysis |
| [loop_scaling.py](loop_scaling.py) | Trapped (bound) fraction vs loop size — the scale-invariance check |
| [mode_projection.py](mode_projection.py) | Exact projection of excitations onto the bound subspace (settles the "is it the ZPE ½?" question — no) |
| [scale_invariance.py](scale_invariance.py) | Dispersion linearity vs wavelength — the IR-fixed-point / scale-invariance check |
| [work/tier2-design.md](work/tier2-design.md) | The bound-state finding, the band structure, the principle-vs-scale reframe, and the Tier 2 plan |
| [work/countability-from-information.md](work/countability-from-information.md) | Derivation sketch: countability (P3) from A3 (compact phase) + A5 (informational state) via U(1)↔ℤ |
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

Optional clean follow-ups: construct the CLS explicitly from the ω=0
flat-band states (does a *larger* CLS tower exist — Q140 §3a?); and a
block-spin / decimation RG to test the fixed point more rigorously
than the dispersion-linearity proxy.
