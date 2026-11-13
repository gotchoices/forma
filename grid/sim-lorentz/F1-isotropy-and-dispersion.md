# F1 — Wave speed is isotropic (T1)

**Verdict:** ✅ Requirement 1 met. Light on the honeycomb has one
speed in every direction, to 3 parts in 10¹¹ at long wavelength.

## Why this matters

A crystal has axes. The natural worry about any lattice model is
that waves run faster along a lattice direction than diagonally,
which would appear immediately as a direction-dependent speed of
light — the thing Michelson and Morley looked for and did not find.

This is the one requirement a lattice might be expected to fail
outright, so it is worth settling first.

## Method

Exact Bloch analysis — no time evolution, no numerical error beyond
machine precision. The one-tick operator for the GRID impedance
scatter S = (2/N)J − I on a true honeycomb (two cells per unit
cell, three edges each) is a 6×6 matrix at each Bloch wavevector k.
Its eigenvalues are unit-modulus; their phases are the mode
frequencies in radians per tick. The lowest propagating branch
gives the wave speed ω(k)/|k|.

Sampled over a 60° wedge, which is the full symmetry-inequivalent
range of directions on a honeycomb.

```
scripts/lattice_lorentz.py --isotropy
```

## Result

```
     |k|  lambda/cells   min speed   max speed   anisotropy
   0.020         314.2  0.40824772  0.40824772    2.778e-11
   0.200          31.4  0.40819144  0.40819155    2.787e-07
   1.000           6.3  0.40673151  0.40680834    1.889e-04
   2.000           3.1  0.40060185  0.40220606    3.996e-03

long-wavelength speed c = 0.40824829   (1/sqrt(6) = 0.40824829, diff 1.56e-11)
```

## Reading

**Anisotropy falls as roughly the fourth power of (spacing/λ).**
Each 10× in wavelength buys about 10⁴ in isotropy: 2.8 × 10⁻¹¹ at
314 cells, 2.8 × 10⁻⁷ at 31 cells. The mechanism is averaging — a
long wave samples many cells and washes out the lattice's angular
structure, the same reason a polycrystalline steel beam has no
grain direction at engineering scale.

**The lattice speed appears to be exactly 1/√6.** Measured
0.40824829 against 1/√6 = 0.40824829, agreeing to 1.6 × 10⁻¹¹ —
which is the numerical floor, not a discrepancy. This has **not
been derived**; it is a numerical observation worth a derivation.

**Two numbers in the repo need reconciling.**
[qa/Q141](../../qa/Q141-emergent-lorentz-invariance-from-grid.md)
quotes ω ≈ 0.41·k from grid-quantization, which agrees. But
[INBOX.md](../INBOX.md) lines 365–372 quote ≈0.73 edges/tick for a
hexagonal lattice. That is presumably a different convention
(edges traversed rather than cells advanced, or a triangular rather
than honeycomb lattice), but the repo should settle on one number
with its units stated.

## Scope

This measures the **raw lattice operator** — no reduction, no
hand-added terms, no continuum approximation. The result carries no
model caveat.

It also does not settle much on its own. One speed in every
direction means a *stationary* apparatus sees no
direction-dependence. The question of what a *moving* apparatus
reads is T2 and T3.
