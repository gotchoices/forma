# Ch. 3 — The modes of light

**Status:** Draft (prose, first pass). Part of the [presentation arc](README.md#presentation-arc).
**Grade:** [derived] — computed band structure and measured properties.
**Role:** map which excitations the lattice supports, and establish that each is a clean (linear) oscillator.

Chapter 2 showed that a disturbance propagates as light. The next
question is *which* waves the lattice supports, and what kind of
oscillator each one is. The answers — a continuum of propagating "photon"
modes, a class of trapped non-propagating ones, and the fact that every
mode is an exact linear oscillator — come straight from diagonalizing the
update rule of Chapter 1. All of it is computed; the scripts are named at
the end.

## 3.0 Vocabulary

A few standard terms, defined plainly before use (no solid-state physics
assumed):

- **Wavevector k** — a wave's spatial frequency, how fast its phase turns
  with distance. Large k is a short wavelength λ = 2π/k; small k a long
  one.
- **Dispersion relation ω(k)** — the rule tying a wave's temporal
  frequency ω to its wavevector k: the medium's menu of which waves are
  allowed.
- **Bloch mode** — on a repeating lattice, a wave-like mode labelled by a
  single k (its pattern repeats cell to cell with a fixed phase step).
  These are the lattice's natural waves.
- **Brillouin zone** — the range of *distinct* k. Because the lattice is
  discrete, any k outside this range just repeats one inside it, so the
  zone holds every distinct wave exactly once.
- **Band** — for each k several ω may be allowed; following one across
  all k traces a *band*. A **dispersive** band has ω changing with k (the
  wave moves); a **flat** band has ω the same for every k.
- **Group velocity, dω/dk** — the speed at which a wave packet, and the
  energy it carries, actually travels. Dispersive bands have non-zero
  group velocity (they propagate); a flat band has *zero* (it sits still).

## 3.1 The band structure

Treating the one-tick update as an operator and diagonalizing it mode by
mode across the Brillouin zone gives the lattice's full menu of waves.
The honeycomb edge-network carries six bands per unit cell, in two kinds
(`scripts/band_structure.py`, cross-checked against direct real-space
diagonalization — [tier2-design.md](work/tier2-design.md) §3):

- **four dispersive bands** — ω changes with k, so these waves propagate;
- **two flat bands** — ω constant across the whole zone, one at ω = 0 and
  one at ω = π (the fastest the clock allows).

The flat bands are found not by their width — they sit at the *edges* of
the dispersive bands, so width measures miss them — but by counting modes
per frequency: a flat band appears as a spike in the **density of states**
(the number of modes in a frequency interval). Exactly one-sixth of all
modes pile up at ω = 0 and one-sixth at ω = π.

## 3.2 The dispersive bands are the free photons

The dispersive bands are the propagating modes — free light. They carry
non-zero group velocity (up to ≈ 0.86 of the lattice speed) and span a
continuous range of frequencies. That continuum is the answer to *which
frequencies exist* — the piece the arc labels **P1**. The slope of the
lowest dispersive band at small k is exactly the ω ≈ 0.41·k phase velocity
measured in Chapter 2: the long-wavelength photon and the band-structure
photon are one object, seen two ways.

## 3.3 The flat bands are trapped modes — not mass

A flat band has zero group velocity, so its modes do not travel: they are
**localized**, sitting where they are put. Such a mode is a **compact
localized state** (CLS). The flat bands therefore predict trapped,
non-radiating excitations, and the simulation finds them: a circulating
excitation placed on a single hexagon deposits about half of itself into
a non-propagating mode that then persists indefinitely, while the rest
radiates away in one tick (`run_recirculation.py --test bound`; the
surviving state is a CLS on the ω = 0 flat band). Flat-band localized
states are familiar from other edge / line-graph networks; what is new
here is only their reading inside GRID.

Two cautions, both load-bearing:

- **This is not a massive particle.** The demonstrated CLS sits at
  ω = 0 — it is *static*, and a static excitation carries zero energy
  (E = ℏω = 0). A massive particle would be a localized mode at a
  *finite* (Compton) frequency, and the lattice has **no** localized mode
  at a generic finite ω (the flat bands lie only at ω = 0 and ω = π). So
  this is a genuine bound / zero-mode, not the rest-energy of matter;
  mass proper belongs to the MaSt sheet construction, not here.
- **The ~½ is not the zero-point ½.** Projecting excitations exactly onto
  the bound subspace gives 0.571, and the figure depends on the
  excitation (a random state hits 1/3) — it is not a universal one-half,
  and the vacuum zero-point ½ is a different quantity entirely
  (`mode_projection.py`). The numerical near-coincidence was only that.

## 3.4 Each mode is an exact linear oscillator

The lattice dynamics are exactly linear: disturbances add without
interacting (exact superposition, confirmed in sim-maxwell). So every
mode above — dispersive or flat — is an exact **harmonic oscillator**: a
clean, independent sinusoid at its own frequency, with no mixing into
other modes. This is the piece the arc labels **P2**, and it is not a
small thing: it is what makes each frequency a sharp, self-contained
degree of freedom rather than one smeared into its neighbours.

## 3.5 The photon band is scale-free

How linear is the photon band? Its deviation from a straight line ω = v·k
falls as ~k² toward long wavelength — about 0.1% at λ ≈ 9 lattice units,
1% at λ ≈ 4 (`scripts/scale_invariance.py`). Real light has wavelengths
vastly longer than a lattice cell, so across any observable range the
dispersion is **scale-free**: no preferred length scale in the
low-frequency (infrared) behaviour — a property called an **IR fixed
point** — with scale-dependence appearing only near the lattice scale
itself. The trapped fraction of §3.3 is scale-free in the same sense: it
stays ~½ whatever the size of the loop excited (`loop_scaling.py`). This
scale-freedom is reported here as a measured property of the spectrum;
what, if anything, it implies for the constants is not pursued in this
chapter.

---

The lattice's menu is now in hand: a continuum of propagating photon
modes, a class of trapped zero-/band-edge modes, every one an exact
linear oscillator, on a scale-free photon band. The arc continues (see
the [arc](README.md#presentation-arc)).

## Sources

- `scripts/band_structure.py` — the bands; the density-of-states flat-band detector
- `scripts/run_recirculation.py` (`bound`, `circ`) — the bound state; circulation
- `scripts/loop_scaling.py`, `scripts/mode_projection.py`, `scripts/scale_invariance.py`
- [tier2-design.md](work/tier2-design.md) §1–§3 — the findings and methodology

## Claim discipline

[derived] / computed. Flat-band compact-localized states are known
network physics; the contribution is the GRID reading (dispersive = free
photon, flat = trapped mode). The ω = 0 bound mode is **not** mass (zero
energy; no localized mode at generic finite ω), and the ~½ is **not** the
zero-point ½. Scale-invariance is a measured spectral property; no claim
about ℏ or its universality is drawn from it here.
