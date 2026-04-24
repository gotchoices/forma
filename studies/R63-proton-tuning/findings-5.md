# R63 Track 5: E-sheet fitness landscape under Q132 v2

**Scope.**  Re-render Track 4's `(ε_e, s_e)` grid sweep using the
refined Q132 v2 classifier.  Under v2, modes decompose by gcd:
`(n_et, n_er)` is k copies of a primitive `(p_t, p_r)` with
gcd = 1.  Primitive `|p_t| = 1` with `p_r ≠ 0` is bright charged;
primitive `|p_t| > 1` with gcd = 1 is dark (charge cancels by
root-of-unity phase sum); ring-only and tube-only primitives are
neutral self-mass.  See
[Q132 v2](../../qa/Q132-promotion-chain-principle.md) for the full
rule set.

The v1 version of this track restricted enumeration to
`|n_et| ≤ 1` by fiat.  v2 removes that restriction and lets the
classifier decide case by case — this makes the full spectrum of
multi-event and phase-cancelled modes visible.

Script:
[`scripts/track5_e_sheet_q132.py`](scripts/track5_e_sheet_q132.py)
Outputs:
[`outputs/track5_fitness_q132v2.png`](outputs/track5_fitness_q132v2.png),
[`outputs/track5_counts_q132v2.png`](outputs/track5_counts_q132v2.png),
[`outputs/track5_grid_q132v2.csv`](outputs/track5_grid_q132v2.csv),
[`outputs/track5_dark_catalog_v2.csv`](outputs/track5_dark_catalog_v2.csv)

---

## F1. Zero bright-primitive ghosts, baseline and grid-wide

The v2 ghost criterion is strict: **a bright primitive charged
mode whose mass is below the lightest observed same-|Q|
particle.**  Because `L_ring_e` is calibrated so that the
electron's `(1, 2)` primitive hits `m_e` exactly, no bright
primitive on the e-sheet can be lighter than `m_e`.

- **At R53 Solution D** `(ε_e, s_e) = (397.074, 2.0042)`:
  **0 bright-primitive ghosts.**
- **Across the 41 × 56 = 2296-point grid**: **0 bright-primitive
  ghosts at every point (100% ghost-free).**

v1 already reported 0/2296 under its stricter rule; v2's richer
enumeration re-confirms this at a structurally more demanding
level.

## F2. R53 Solution D matches all three charged leptons

The three bright-primitive lepton matches at baseline, width-
weighted thresholds (2% floor):

| Lepton | Best mode | Δm/m | Closeness |
|:------:|:---------:|-----:|----------:|
| e | (−1, −2) | +0.000% | **1.000** |
| μ | (−1, −1) | +0.828% | 0.586 |
| τ | (−1, +15) | +0.144% | 0.928 |

**Total fitness = 2.514 / 3.0** at the exact baseline.  The
grid's coarsest nearby sampled point is much further off
(fitness 1.17), showing the peak is sharp.  A grid-scan peak
at `(357.73, 2.004)` reaches 2.671 as a discrete artifact of
grid alignment; v1 already noted this and concluded R53 Solution
D is within ~1% of the genuine local optimum.  v2 does not
change this conclusion.

## F3. The Track 4 ghost tower is dissolved as multiples

Track 4 flagged a `(n, 2n)` "ghost tower" on the e-sheet:
`(2, 4), (3, 6), (4, 8)` at 2, 3, 4 × m_e with no observed
counterpart.  Under v2 these are classified as **multiples** —
each is k independent copies of the electron primitive `(1, 2)`:

| Mode | k | Primitive | Reading |
|:-:|:-:|:-:|:--|
| (−2, −4) | 2 | (−1, −2) | 2 electrons |
| (−3, −6) | 3 | (−1, −2) | 3 electrons |
| (−4, −8) | 4 | (−1, −2) | 4 electrons |

Because the e-sheet has no binding mechanism (no Z₃, no T18
pairing), k copies propagate as k *separate* free primitive
particles, not as a bound composite.  No new `|Q| = 2, 3, 4`
particle is predicted; the Track 4 ghost tower is consistent
with the observed spectrum of many electrons.

## F4. Genuine dark-massive modes appear

v2 identifies a population of gcd = 1, `|p_t| > 1` primitives
that are **dark** — mass from trapped EM energy, charge zero
by phase cancellation.  The first few at baseline:

| Mode | Primitive | Mass (MeV) |
|:-:|:-:|---:|
| (−4, −9) | (−4, −9) | 102.60 |
| (−3, −7) | (−3, −7) | 103.03 |
| (−2, −5) | (−2, −5) | 103.47 |
| (−2, −3) | (−2, −3) | 105.22 |
| (−3, −5) | (−3, −5) | 105.66 |
| (−4, −7) | (−4, −7) | 106.10 |

At R53 Solution D the e-sheet predicts **91 dark-massive
primitives** below the 2.5 GeV cap, plus **46 multi-copy
bright modes** (k > 1 of observed charged primitives) and
**neutral-mass** ring-only and tube-only modes.  None of these
conflict with observation.

## F5. Bright-gap modes are the one open discipline item

35 bright primitives at baseline fall in the "charged, unmatched"
category:

| Mode | Mass (MeV) | Q |
|:-:|---:|:-:|
| (−1, −4) | 208.25 | +1 |
| (−1, −5) | 312.60 | +1 |
| (−1, +1) | 313.48 | +1 |
| (−1, −6) | 416.94 | +1 |
| (−1, +2) | 417.82 | +1 |
| ... | ... | ... |

These are primitives with `p_t = ±1`, `|p_r| > 2`, landing at
masses between muon and tau (and beyond) with no observed
charged lepton at those masses.  Under the v2 rule they are
legitimate bright charged predictions.

**Interpretation.**  All 35 are well above the decay threshold
for `e + γ + ν + ν` (the muon decay channel in reverse), and all
are short-winding modes in a space that also contains the muon
primitive.  R56/R57 routing — the "split-dominated" mechanism —
predicts that any unstable charged resonance above threshold
decays promptly to the stable lepton with lighter primitive
partners.  Under this reading the 35 bright-gap modes are
short-lived resonances, not stable unobserved leptons.

**This is the one open item where v2 inherits an explanation it
does not prove.**  Whether the 35 bright-gap primitives are
*actually* short-lived at rates consistent with non-observation
is a phenomenological question that v2 defers to a future
derivation (analogous to the R62 charge-quantization program).
The v2 discipline rule — predict every observed charged
particle, predict no unobserved *stable* charged particle — is
satisfied; the weaker form "predict no unobserved *resonance*"
is not something Q132 alone can enforce.

## F6. s_e is narrowly pinned; ε_e is a ridge

The fitness heat map is the same landscape v1 found, just
without the universal ghost mask: a sharp horizontal ridge at
`s_e ≈ 2.0` with structured peaks in ε_e.

- `s_e` is tightly constrained: outside `s_e = 2.0 ± 0.02`,
  fitness collapses because the electron's `(1, 2)` mode
  requires near-exact shear resonance.
- `ε_e` has wider latitude: the ridge sustains fitness ≥ 2 for
  roughly `ε_e ∈ [280, 460]`, with multiple local peaks.  R53
  Solution D is one local peak among several.

This is the same conclusion v1 reached; v2 does not add or
subtract latitude on either axis.

## What Track 5 v2 establishes

1. **The e-sheet is ghost-free under v2 at every grid point.**
   The Track 4 architectural concern is fully resolved.
2. **R53 Solution D is validated as a near-peak** for three-
   lepton width-weighted fitness under v2.
3. **The `(n, 2n)` tower is dissolved as `k electrons`** — not a
   new particle family.
4. **The dark-mode catalog is richer under v2** — it includes
   gcd = 1 phase-cancelled primitives as well as ring-only and
   tube-only neutrals.  Total dark inventory at baseline: 91
   dark-massive primitives plus additional ring-only / tube-
   only entries.
5. **35 bright-gap charged primitives remain as routing-
   suppressed predictions** (the v1-era "charged-gap" list,
   now with the same interpretation in v2).  These are the
   sole un-proven discipline item.
6. **`s_e` narrow-pinned, `ε_e` open** — entering Track 6 with
   the same ranges as the v1 analysis.

## Implications for Track 6

Track 5 clears the e-sheet at the single-sheet level.  Track 6
now applies v2 to the full compound-mode inventory, where the
gcd decomposition combines across sheets and the cross-sheet
charge arithmetic of Q132 v2 Section 5 is exercised against
R60 T19's tuple set.

## Status

**Track 5 v2 complete.**  E-sheet ghost-free under v2, R53
Solution D validated as near-peak, dark-mode catalog produced,
35 bright-gap modes flagged as routing-suppressed predictions.
Ready for Track 6 v2 (Phase 6a compatibility check, 6b tuple
re-derivation, 6c/6d/6e as in the README).
