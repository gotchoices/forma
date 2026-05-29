# Ch. 3 — The modes of light

**Status:** Outline (no prose yet). Part of the [presentation arc](README.md#presentation-arc).
**Grade:** [derived]
**Role:** map the spectrum — which excitations exist, and that each is a clean oscillator.

## Outline

- **3.1 The Bloch band structure.** 2 flat bands (ω = 0, π) + 4 dispersive
  bands (built empirically from `scatter_step`; cross-checked real-space).
- **3.2 Dispersive bands = free photons** (P1: which ω exist); small-k
  slope = the 0.41 phase velocity.
- **3.3 Flat bands (ω = 0, π) = localized, non-propagating bound modes**
  (the `bound` test; ~½ trapped; *not* the ZPE ½). **Not a massive
  particle:** ω = 0 is zero-energy, and there is *no* localized mode at
  generic finite ω — a bound / zero-mode, not "mass" (mass proper is
  MaSt, elsewhere).
- **3.4 Each mode an exact harmonic oscillator** (P2): exact superposition.
- **3.5 Scale-invariance.** Linear dispersion as an IR fixed point;
  trapped fraction size-independent.

## Sources

- `scripts/band_structure.py` — the bands, the flat-band detector (DOS)
- `scripts/run_recirculation.py` (`bound`, `circ`) — the bound state, circulation
- `scripts/loop_scaling.py`, `scripts/mode_projection.py`, `scripts/scale_invariance.py`
- [work/tier2-design.md](work/tier2-design.md) §1–§3

## Claim discipline

Flat-band compact-localized states are known network physics; the
contribution is the GRID reading (free photon vs bound mode). Do **not**
call the ω = 0 bound mode "mass."
