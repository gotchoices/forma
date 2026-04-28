# metric-mass

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** Mass generation only. Charge will be a separate project.
**Method:** Mathematical derivation first; computation only if a
  question can't be settled on paper.

## Why this project exists

The R-track has been working in 11D ([R60-metric-11](../../studies/R60-metric-11/),
through [R64-nuclear-harmonic-stack](../../studies/R64-nuclear-harmonic-stack/)).
That's where the production work lives, but it's a lot of metric
components moving at once, and most of the time we plug constants
into the metric and read out a number.

This project backs all the way up. We start from the smallest metric
that can generate mass at all and derive every step. The goal isn't
new physics — it's making every entry of every metric we ever write
feel obvious, not mysterious.

## Coordinates and notation

| Symbol | Role | Type |
|---|---|---|
| **t** | Time | Extended, real |
| **S** | Spatial extension | Extended, real (1D in this project) |
| **u** | Compact, mass-generating | Compact: u ~ u + L_u |
| **w** | Compact, charge-generating | (out of scope — future project) |
| **v** | Reserved | (possible third compact direction) |

x, y, z are reserved for Cartesian visualization axes when we render
results, and are *not* metric coordinates.

**Coordinate vs. observable.** u is a *coordinate*. The
mass-from-u story is: momentum along u, when quantized by
periodicity, plays the role of mass. "u is the mass dimension" is
shorthand for "momentum-along-u is mass." The coordinate is not
mass.

## Ground rules

1. **Derivation first.** Each chapter is a self-contained piece of
   mathematics. State assumptions, derive consequences, mark
   anything dropped or approximated.

2. **Computation only when forced.** If a question can be answered
   by paper math, do it on paper. Reserve scripts for cases where
   the algebra becomes too tangled or a visualization is the only
   way to see the geometry.

3. **Side-paths welcome.** Per [../README.md](../README.md),
   projects are educational. If a tangent illuminates what the
   metric is doing, follow it. The cost of a wrong turn here is
   small; the value of intuition is large.

4. **One topic per chapter.** Don't bundle. If a chapter starts
   asking two questions, split it.

5. **Variables stay symbolic.** Don't pin numerical values until
   the algebra forces it. Keep ℏ, c, L_u explicit (per the
   feedback rule on no-premature-pinning).

## Background reading

- [primers/kaluza-klein.md](../../primers/kaluza-klein.md) — the
  standard KK story (compact dim → charge)
- [primers/alpha-in-grid.md](../../primers/alpha-in-grid.md) —
  how α appears in the GRID lattice
- [studies/R60-metric-11/README.md](../../studies/R60-metric-11/README.md) —
  the 11D metric we're backing up from

## Chapters

1. [01-foundation.md](01-foundation.md) — Axioms and givens. The
   minimal manifold, metric, and wave field on which the rest of
   the project rests.
2. *02 — coming next:* deriving the mass spectrum from a standing
   wave in u.

Each chapter is added one at a time. We don't sketch a full
table-of-contents up front because the project is allowed to grow
in directions we haven't anticipated.

## What this project is not trying to do

- Not deriving α (that's [studies/R31-alpha-derivation/](../../studies/R31-alpha-derivation/)
  and [Q137](../../qa/Q137-alpha-as-aleph-aspect-ratio.md))
- Not searching for particles (that's the R-track)
- Not replacing the 11D production metric (that's [R60](../../studies/R60-metric-11/))
- Not modeling charge — that's a separate future project
- Not claiming 2+1D is fundamental — it's a teaching ladder

The output is intuition. Anything else is a bonus.
