# F3 — A boosted bound state contracts by 1/γ and coasts without radiating (T3, T4)

**Verdict:** ✅ Both met. Contraction matches 1/γ to 0.1% for
v ≤ 0.8c; the residual at higher v is lattice discreteness, not
Lorentz violation. Energy is constant to 2 × 10⁻⁵ over six internal
periods.

**Scope caveat up front:** this runs on a discrete sine-Gordon
chain, which is grid-matter's *reduction* of the compact-phase
sector, **not** the raw GRID impedance scatter. See §Scope. The
result is about the sector forma uses to model bound matter, not
about the scatter.

## Why this matters

[F2](F2-boost-and-universality.md) measured a plane-wave dispersion
relation, which is **necessary but not sufficient**. A dispersion
curve of the right shape says nothing about how a *composite*
object transforms. A bound state's contraction involves its
binding, and the binding has lattice corrections of its own.

This is the step from "the dispersion relation looks relativistic"
to "a moving object is actually shorter." It is the test
[synthesis.md](../synthesis.md) named and never ran.

And T4 is the sharpest available falsifier. In relativity, uniform
motion is indistinguishable from rest, so a free particle **cannot**
radiate or decelerate. Lattice solitons generically shed energy
into surrounding modes and get snagged by the Peierls–Nabarro
barrier. A bound state that slows while coasting is a Lorentz
violation requiring no interpretation at all.

## Method

Discrete sine-Gordon chain, φ_tt = φ_xx − m² sin φ, integrated with
Verlet. The exact continuum breather — a bound, oscillating,
spatially localized solution — is Lorentz-boosted to velocity v and
sampled at two adjacent times to start the integrator.

The measurement is then: **is that profile a stable travelling
solution of the lattice, and what is its actual width?**

This is a genuine test rather than an assumption of the answer. A
non-Lorentzian lattice is free to reject the imposed profile — it
would broaden, radiate, or travel at the wrong speed. All three are
measured.

Three precautions, each learned the hard way during the
grid-scattering work:

- **Width is the FWHM of the energy envelope, interpolated to
  sub-cell resolution.** Counting cells above half-max quantises
  the width to ±1 cell, which is ±3% on a 30-cell envelope —
  coarser than the effect being measured.
- **The envelope is averaged over one full internal period,**
  because a breather's width oscillates.
- **The actual profile is printed, not just a summary statistic.**
  An rms or second-moment width reads two separated pulses as one
  broad distribution, and did so three times in earlier work.

```
scripts/lattice_lorentz.py --contraction --vs 0.0 0.3 0.6 0.8 0.9 0.95
scripts/lattice_lorentz.py --contraction --m 0.025 --nx 16000 --vs 0.0 0.9 0.95
scripts/lattice_lorentz.py --contraction --vs 0.0 0.8 --profiles --half 70
```

## Result

Rest envelope ~28 lattice units (m = 0.05, ω = 0.7), chain of 8000:

```
     v   gamma     width  w(0)/gam    w err    speed    v err       dE/E
  0.00  1.0000     75.14     75.14    +0.0%  -0.0000    +0.0%    -0.002%
  0.30  1.0483     71.67     71.68    -0.0%   0.2999    -0.0%    -0.001%
  0.60  1.2500     60.07     60.12    -0.1%   0.5998    -0.0%    -0.000%
  0.80  1.6667     45.03     45.09    -0.1%   0.7993    -0.1%    +0.000%
  0.90  2.2942     32.33     32.75    -1.3%   0.8984    -0.2%    +0.001%
  0.95  3.2026     22.61     23.46    -3.6%   0.9465    -0.4%    +0.000%
```

`width` is measured; `w(0)/gam` is the rest width divided by γ —
what exact contraction predicts. `w err` is the discrepancy.

The envelope is a single clean peak at every velocity, visibly
narrower when boosted and the same shape — no splitting, no
growing tails:

```
   envelope at v=0.0                        envelope at v=0.8
   |             #                          |            #
   |      ####################              |        #############
   |   #########################            |      ###############
   | ###########################            |     ################
```

## Is the high-v deviation a real Lorentz violation?

No. Halving m doubles the breather's width in lattice units,
making it closer to the continuum. If the deviation were a genuine
violation it would stay; if it is discreteness it should shrink.

| v | err at ~28-cell rest width | err at ~56-cell rest width | improvement |
|---|---|---|---|
| 0.90 | −1.3% | **−0.3%** | 4.3× |
| 0.95 | −3.6% | **−1.4%** | 2.6× |

Doubling the width improves the v = 0.9 agreement by 4.3×, and
2.04² = 4.2. **The error scales as (spacing/width)²** — the same
k² signature as the dispersion correction measured in
[F1](F1-isotropy-and-dispersion.md).

So contraction is **exact in the continuum limit**, with a
discreteness correction that vanishes as the state is made large
compared to the cell spacing. That is the expected and desired
behaviour.

## Reading

**Requirement 2 of the specification is met.** A boosted bound
state really is shorter by 1/γ, and this was not imposed — the
lattice sustained the contracted profile as a stable travelling
solution, at the right speed, for six internal periods.

**Requirement T4 is met, decisively.** Energy drift is at most
0.002%, and it does not grow with velocity. The state coasts. No
radiation into the surrounding modes, no deceleration, no
Peierls–Nabarro trapping. This was the test most likely to fail
and it did not.

**The realised speed matches the imposed velocity** to 0.1% up to
v = 0.8, drifting to 0.4% at v = 0.95 — consistent with the same
discreteness correction.

Taken with [F1](F1-isotropy-and-dispersion.md) and
[F2](F2-boost-and-universality.md), the operational specification
in
[primers/relativity-on-a-lattice.md](../../primers/relativity-on-a-lattice.md)
§8 is met in the long-wavelength limit by measurement rather than
by assumption.

## Scope — what this does not license

**This is not a verdict on the GRID scatter.** The on-site cosine
term in φ_tt = φ_xx − m² sin φ was added by hand in the grid-matter
reduction. That project's own work file is explicit:

> *"The scatter cannot, by itself, produce any on-site cosine —
> nonlinearity is not in it."*
> — [reduction-cosine-from-scatter.md](../../projects/grid-matter/work/reduction-cosine-from-scatter.md)

So F3 establishes that **the sine-Gordon sector is Lorentzian**.
Since sine-Gordon is a relativistic field theory in the continuum,
that outcome was expected — the content of the measurement is that
*discretization does not spoil it*, with the error scaling
measured. Whether the GRID scatter produces this sector remains
open and is tracked in
[grid-scattering](../../projects/grid-scattering/).

**The initial condition was a pre-contracted profile.** The test
asks whether the lattice *sustains* it, which it does. A stronger
version would find the lattice's own travelling solution
independently — by relaxation at fixed momentum — and measure its
width without reference to the continuum answer. Worth doing.

**Transverse contraction is untested** (T6). The specification
requires contraction along the motion and *none* across it; only
the first has been measured. This needs a genuinely 2D run.

**Born-rigid acceleration is untested** (T5). F3 boosts a state
that is already moving. It does not watch a state *accelerate* into
the contracted configuration, which is the mechanism question:
accelerate a bound pair through its own internal coupling and
check that the separation relaxes to d₀/γ. That is Bell's string
run on the lattice, and it would test the resonance mechanism of
[the primer](../../primers/relativity-on-a-lattice.md) §11 rather
than only its endpoint.
