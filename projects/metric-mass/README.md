# metric-mass

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** Mass generation only. Charge will be a separate project.
**Method:** Mathematical derivation first; computation only if a
  question can't be settled on paper.

## Why this project exists

Standard Kaluza-Klein theory ([primers/kaluza-klein.md](../../primers/kaluza-klein.md))
takes two big things for granted before it begins:

1. **Gravity exists.** KK assumes 4D general relativity already works —
   that mass curves spacetime via Einstein's equations.
2. **Mass exists.** KK builds particles by giving them rest mass and
   then asking what an extra dimension would do for them.

Given those two starting assumptions, KK then *produces* electromagnetism
as a geometric consequence of adding one compact extra dimension. That
is its whole punchline: EM falls out of geometry once you already have
mass and gravity.

This project goes the other way. We assume only **light** — a
massless propagating wave — exists. No mass, no gravity, no
electromagnetism. We don't try to derive EM (that's a future project's
job). We ask the much narrower question:

> *If light is all we have, and the manifold has one compact extra
> dimension, what does the metric have to look like? In particular,
> are the off-diagonal (cross) terms zero, or does light's behavior
> on the manifold force them to be nonzero?*

This is a back-up question relative to the production R-track
([R60-metric-11](../../studies/R60-metric-11/), through
[R64-nuclear-harmonic-stack](../../studies/R64-nuclear-harmonic-stack/)),
which works in 11D with many metric components moving at once. The
production track is where new physics gets pushed; this project is
where intuition for *what each metric component does* gets built.

The goal isn't new physics. It's making every entry of every metric
we ever write feel obvious, not mysterious.

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
2. [02-mass-from-u.md](02-mass-from-u.md) — Solve the wave equation
   on M. Outline currently in place; full chapter to be filled out
   from that outline.

### Tentative downstream arc

The chapters below are *plausible follow-ups*, not commitments.
The project is allowed to redirect based on what each chapter's
math actually reveals. None of these is asserting an answer —
they are framing questions to be examined.

3. **Visualization of the solutions.** Render the modes found in
   chapter 2 as helices / standing waves on the (S, u, t) Cartesian
   embedding. Build intuition for what the field looks like at
   different mode numbers and motion states.
4. **Self-consistency of the bare metric.** Examine more carefully
   whether the diagonal-and-constant metric of chapter 1 remains
   internally consistent with the solutions chapter 2 produced —
   or whether the solutions force any modification.
5. **Position-dependent g_uu.** If chapter 4 reveals tension, one
   natural relaxation is letting g_uu become a function of S
   (the "dilaton-style" possibility from §3 of the foundation).
   Examine the consequences.
6. **Off-diagonal terms.** Examine whether any g_tu, g_Su cross
   term is forced or admitted by the solutions, and what physical
   meaning such a term would carry on this minimal manifold.
7. **Closing summary.** Whatever chapter 4–6 reveal, restate the
   project's findings in plain language: what the math actually
   established, and what it left open for follow-up projects
   (charge, sheets, gravity).

If chapter 4 establishes that the diagonal metric is fine on its
own, chapters 5–6 may not be needed. If it reveals tension, the
arc continues. We pick up the next chapter once the previous one's
findings are in.

Each chapter is added one at a time. The arc is a sketch, not a
contract.

## What this project is not trying to do

- Not deriving α (that's [studies/R31-alpha-derivation/](../../studies/R31-alpha-derivation/)
  and [Q137](../../qa/Q137-alpha-as-aleph-aspect-ratio.md))
- Not searching for particles (that's the R-track)
- Not replacing the 11D production metric (that's [R60](../../studies/R60-metric-11/))
- Not modeling charge — that's a separate future project
- Not claiming 2+1D is fundamental — it's a teaching ladder

The output is intuition. Anything else is a bonus.
