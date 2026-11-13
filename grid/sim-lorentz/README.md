# sim-lorentz — Testing the Lorentz properties that A2 assumes

**Status:** Active. Three of five tests done; two open.

## Scope — deliberately narrow

Axiom **A2** of [foundations.md](../foundations.md) *asserts* a
Lorentzian signature:

> Of the four lattice dimensions, exactly one is **timelike** — it
> carries a causal ordering... In the continuum limit, the metric
> signature is (−, +, +, +).

Everywhere else in [grid/](../) this is taken as given, and the
consequences — no preferred frame, time dilation, length
contraction — are asserted from it rather than measured. The
argument in [INBOX.md](../INBOX.md) §"No preferred frame" is
circular with respect to the question, since it derives the absence
of a preferred frame *from* A2.

[synthesis.md](../synthesis.md) names both the gap and this test:

> *"Can Lorentz invariance be derived rather than assumed?
> **Promising** — if all observers are lattice excitations, their
> instruments contract/dilate by exactly γ, making the lattice
> undetectable... Physical argument is strong; mathematical rigor
> not yet established. Partially computable (sim-lorentz: boost a
> bound state, check γ contraction)."*

**This directory does only that.** It measures whether the lattice
dynamics deliver the observable consequences of A2. It does not
revisit the axiom, propose alternatives, or touch anything else in
`grid/`.

## What has to be true

The specification is derived operationally in
[primers/relativity-on-a-lattice.md](../../primers/relativity-on-a-lattice.md).
Summary: a round-trip light-speed measurement on a moving apparatus
suffers a genuine **γ² delay**, and reports c only because the rod
is short by γ and the clock is slow by γ. So:

| # | Requirement | Value |
|---|---|---|
| 1 | one wave speed, every direction | isotropic |
| 2 | contraction along the motion | exactly 1/γ |
| 3 | contraction across the motion | exactly 1 (none) |
| 4 | clock rate | exactly 1/γ |
| 5 | same γ for every sector (**universality**) | — |

Plus one requirement that is not about γ at all: a coasting
particle must **not radiate**. In relativity uniform motion is
indistinguishable from rest, so a free particle cannot lose energy.
Lattice solitons generically shed energy into surrounding modes and
decelerate, which would be a Lorentz violation needing no
interpretation.

Note that **relativistic velocity addition is not an independent
test** for a free particle: additivity of rapidity is algebraically
equivalent to constancy of ω² − c²k², so test T2 already covers it.

## Tests

| | Test | Status |
|---|---|---|
| T1 | Wave speed vs. direction, several wavelengths | ✅ [F1](F1-isotropy-and-dispersion.md) |
| T2 | ω² − c²k² constant along a boost (rest mass) | ✅ [F2](F2-boost-and-universality.md) |
| T3 | Boosted bound state contracts by 1/γ | ✅ [F3](F3-contraction-and-coasting.md) |
| T4 | Coasting bound state does not radiate | ✅ [F3](F3-contraction-and-coasting.md) |
| T5 | Bell's string: accelerate a bound pair through its own coupling, check it relaxes to d₀/γ | ⬜ open |
| T6 | Transverse case: no contraction across the motion | ⬜ open |

## Headline results

- Wave speed is isotropic to **2.8 × 10⁻¹¹** at ~300-cell
  wavelength, with anisotropy falling as ~(spacing/λ)⁴. The
  long-wavelength speed is **0.40824829 cells/tick**, matching
  1/√6 to 1.6 × 10⁻¹¹.
- Rest mass is boost-invariant to **0.003%** at small momentum and
  degrades steeply at the lattice scale. The light and heavy
  sectors degrade at **different rates**, so requirement 5
  (universality) holds only in the long-wavelength limit.
- A boosted bound state **contracts by 1/γ to within 0.1%** for
  v ≤ 0.8c. Residual deviation at higher v was shown to be lattice
  discreteness, not Lorentz violation: it shrinks as
  (spacing/width)² when the state is made wider.
- The same state **coasts without radiating** — energy constant to
  2 × 10⁻⁵ over six internal periods, speed correct to 0.1%.

## What these results do and do not license

**They do not license a verdict on GRID.** T3 and T4 run on a
discrete sine-Gordon chain, which is grid-matter's *reduction* of
the compact-phase sector, not the raw impedance scatter. The
on-site cosine in that reduction was added by hand;
[grid-matter's own work file](../../projects/grid-matter/work/reduction-cosine-from-scatter.md)
states the position plainly:

> *"The scatter cannot, by itself, produce any on-site cosine —
> nonlinearity is not in it."*

So T3/T4 establish that **the sine-Gordon sector is Lorentzian**,
which is the sector forma uses to model bound matter. Whether the
GRID scatter produces that sector is a separate, open question
tracked in [grid-scattering](../../projects/grid-scattering/).

T1 and T2 *are* measurements on the raw lattice operator and carry
no such caveat.

## Files

- [F1-isotropy-and-dispersion.md](F1-isotropy-and-dispersion.md) — T1
- [F2-boost-and-universality.md](F2-boost-and-universality.md) — T2
- [F3-contraction-and-coasting.md](F3-contraction-and-coasting.md) — T3, T4
- [scripts/lattice_lorentz.py](scripts/lattice_lorentz.py) — all three modes

## Relations

- [primers/relativity-on-a-lattice.md](../../primers/relativity-on-a-lattice.md) — the derivation these tests check
- [foundations.md](../foundations.md) — A1 (lattice, tick), A2 (signature)
- [synthesis.md](../synthesis.md) — names this test
- [qa/Q142](../../qa/Q142-absolute-lattice-frame-vs-relativity.md) — the framework-level answer these tests serve: an undetectable lattice frame is Lorentz ether theory, not a refutation; §8 tabulates these results
- [qa/Q141](../../qa/Q141-emergent-lorentz-invariance-from-grid.md) — the earlier framework answer; its §5 has been narrowed, since the photon-dispersion evidence supports isotropy only
- [qa/Q117](../../qa/Q117-relativistic-effects-from-velocity-partition.md) — the velocity-partition account of time dilation; §3 and §5 amended against these results
- [qa/Q144](../../qa/Q144-euclidean-vs-lorentzian-orthogonality.md) — why contraction had to be measured rather than read off path geometry
- [projects/grid-matter](../../projects/grid-matter/) — source of the sine-Gordon reduction used in T3/T4
