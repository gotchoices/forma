# F2 — Rest mass under boost, and what it says about universality (T2)

**Verdict:** ✅ Requirement 4 met at long wavelength (0.003%),
lost at the lattice scale. Requirement 5 (universality) holds in
the same limit — but the mechanism is narrower than it first looks,
and §"Correction" below matters.

## Why this matters

A particle's rest mass must not depend on how fast it is moving. In
wave language, a mode winding the compact direction has a rest
frequency ω₀, and boosting it along x should leave

> ω² − c²k_x² = ω₀²

unchanged. Any drift in that quantity is a Lorentz violation,
directly.

This single test also covers **relativistic velocity addition**,
which is not independent for a free particle: additivity of
rapidity is algebraically equivalent to constancy of ω² − c²k².

## Method

Same exact Bloch operator as [F1](F1-isotropy-and-dispersion.md),
with one wavevector component treated as the compact-direction
momentum k_c (fixing the rest mass) and the other as the boost
momentum k_x. Lattice c taken from F1.

```
scripts/lattice_lorentz.py --boost
```

## Result

```
  compact momentum kc = 0.05   rest frequency w0 = 0.020412   (light)
      kx      omega    w^2-c^2kx^2      drift
    0.00   0.020412     0.00041666    +0.000%
    0.05   0.028867     0.00041664    -0.005%
    0.10   0.045642     0.00041649    -0.042%
    0.20   0.084150     0.00041457    -0.501%
    0.40   0.164477     0.00038600    -7.358%
    0.80   0.326498    -0.00006597  -115.832%

  compact momentum kc = 0.5    rest frequency w0 = 0.203944   (heavy)
      kx      omega    w^2-c^2kx^2      drift
    0.00   0.203944     0.04159316    +0.000%
    0.05   0.204960     0.04159175    -0.003%
    0.10   0.207976     0.04158743    -0.014%
    0.20   0.219625     0.04156869    -0.059%
    0.40   0.261030     0.04147020    -0.296%
    0.80   0.383877     0.04069525    -2.159%
```

## Reading

Rest mass is invariant to **0.003–0.005% at small k_x** and
degrades as roughly k_x². At the lattice scale it fails
completely — the light mode's invariant goes *negative* by
k_x = 0.8, which would be an imaginary rest mass.

## Correction: this is not two different behaviours

The obvious reading of the two tables — that the light sector
dilates very differently from the heavy one, so universality fails
badly — overstates it. Comparing **absolute** rather than
fractional drift:

| k_x | absolute drift, light | absolute drift, heavy | ratio |
|---|---|---|---|
| 0.20 | 0.0000021 | 0.0000245 | 0.09 |
| 0.40 | 0.0000307 | 0.0001230 | 0.25 |
| 0.80 | 0.0004826 | 0.0008979 | 0.54 |

The light mode's absolute drift is **2–11× smaller** than the heavy
mode's. Its catastrophic −116% comes almost entirely from dividing
a modest absolute error by a tiny ω₀².

So the honest statement is:

> The lattice adds a roughly common absolute correction to ω². That
> correction is a **larger fractional** perturbation for lighter
> states, because they have less rest mass to perturb.

Universality does still fail at the lattice scale — two clocks
built from different sectors would acquire different fractional
corrections, and that is what a clock-comparison experiment
detects. But the cause is one shared correction seen against
different baselines, not two distinct mechanisms. Both vanish
together as k → 0.

## Scope

Measured on the **raw lattice operator** — no reduction or
hand-added terms. Carries no model caveat.

What it does *not* establish: that a composite, bound object
transforms correctly. A dispersion relation of the right shape is
necessary but not sufficient — see
[F3](F3-contraction-and-coasting.md).
