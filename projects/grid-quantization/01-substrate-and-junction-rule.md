# Ch. 1 — The substrate and the junction rule

**Status:** Outline (no prose yet). Part of the [presentation arc](README.md#presentation-arc).
**Grade:** [derived]
**Role:** establish the discrete medium and its local update — the stage on which everything else happens.

## Outline

- **1.1 The honeycomb lattice.** Edges as cells, nodes as 3-valent
  junctions; the geometry and why N = 3.
- **1.2 The cell state — a periodic, bounded phase (A3).** A point on a
  circle; only phase *differences* are physical; magnitude pinned.
  *(Introduce the compact phase before any use of it.)*
- **1.3 The clock (A2).** Discrete ticks; one update per tick; signal
  limit one edge per tick.
- **1.4 The junction rule** `out_i = (2/3)·total − in_i`, from energy
  conservation + equal impedance; the −1/3 reflection / 2/3 transmission.
- **1.5 No Maxwell input.** Geometry + impedance only.

## Sources

- [../../grid/hexagonal.md](../../grid/hexagonal.md) — N=3 scattering, the 2/3 / −1/3 coefficients
- [../../grid/foundations.md](../../grid/foundations.md) — A2 (time), A3 (compact phase)
- [../../grid/sim-maxwell/](../../grid/sim-maxwell/) — the substrate simulation this is adapted from
- `scripts/lib.py` — the project's lattice / scatter / evolve machinery

## Claim discipline

Inherited / standard — cite, don't re-derive. This chapter is setup; no
quantum content yet.
