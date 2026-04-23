# R63 Track 4: E-sheet parallel audit

**Scope.**  Apply Tracks 1–3b methodology to the electron sheet:
pure e-sheet ghost audit at R53 Solution D (Phase A), then
`(ε_e, s_e)` grid sweep (Phase B).  Goal: validate the e-sheet
to the same level of precision as the p-sheet before any
multi-sheet inventory work.

**Classification** same as p-sheet: observed / split-dominated /
ghost-sub-observed / ghost-no-decay.  Width-weighted thresholds
(floor 2%; all three charged leptons are narrow resonances so the
floor dominates).

Script:
[`scripts/track4_e_sheet_audit.py`](scripts/track4_e_sheet_audit.py)
Outputs:
[`outputs/track4_fitness.png`](outputs/track4_fitness.png),
[`outputs/track4_ghost_breakdown.png`](outputs/track4_ghost_breakdown.png),
[`outputs/track4_grid.csv`](outputs/track4_grid.csv).

**Bug-fix along the way.**  `match_observed` in Track 1's
module had a 1 MeV mass floor that filtered out the electron
itself as a valid match target.  Fixed to name-based filter
(excludes γ and ν only); Track 1 and Track 3 results are
unaffected because no p-sheet mode was below 1 MeV, but Track 4
depends on matching the electron.

---

## F1. R53 Solution D matches electron, muon, AND tau

The pure e-sheet audit at `(ε_e = 397.074, s_e = 2.004200)`,
`L_ring_e = 54.83 fm` (calibrated to m_e at the (1, 2) mode)
finds clean lepton matches:

| Lepton | Best mode | Predicted mass | Observed | Δm/m | Closeness |
|:------:|:---------:|---------------:|---------:|-----:|----------:|
| e  | (−1, −2) | 0.511 MeV | 0.511 MeV | +0.00% | **1.000** |
| μ  | (−1, −1) | 104.78 MeV | 105.66 MeV | +0.83% | 0.586 |
| τ  | **(−1, +15)** | 1774.3 MeV | 1776.9 MeV | **+0.14%** | **0.928** |

**Tau does not require the high-n (n ≈ 3478, 6956) assignment.**
A clean 1-sheet tau match exists at `(n_et = −1, n_er = 15)` —
well inside our |n_er| ≤ 30 enumeration — with 0.14% accuracy.
R53 Solution D gives a working three-generation assignment at
low winding.  (A second muon match at `(−1, −3)` = 103.9 MeV
appears at 1.66% off; (−1, −1) is better.)

Lepton fitness at baseline: **2.51 / 3.0** — reasonable but not
as tight as the p-sheet's best (4.95 / 7.0 ≈ 0.71 per particle
vs e-sheet's 0.84 per particle).  The e-sheet matches leptons
moderately well; baseline is a decent, not exceptional, point
for the three charged leptons.

## F2. But the e-sheet also predicts structural ghost modes

The audit flags **4 sub-observed ghosts** at R53 Solution D:

| Mode | E (MeV) | |Q| | Problem |
|:----:|--------:|:--:|:--------|
| (−2, −4) | 1.022 | 2 | no observed |Q|=2 particle; no decay path |
| (−3, −6) | 1.533 | 3 | no observed |Q|=3 particle; no decay path |
| (−4, −8) | 2.044 | 4 | no observed |Q|=4 particle; no decay path |
| (0, −1) | 104.35 | 0 | below π⁰ (135 MeV), no neutral match |

The first three are the `(n, 2n)` family of "doubled, tripled,
quadrupled" electron modes.  At exact shear resonance
`s_e = 2`, all (n, 2n) have ring detuning `2n − n·s_e = 0`, so
μ(n, 2n) ≈ n/ε_e and their masses scale as n × m_e.

- (1, 2) = electron at 1 × m_e (observed) ✓
- (2, 4) = 2 × m_e = 1.02 MeV (|Q|=2) ✗ — no observed particle
- (3, 6) = 3 × m_e = 1.53 MeV (|Q|=3) ✗
- (4, 8) = 4 × m_e = 2.04 MeV (|Q|=4) ✗

These modes are structural predictions of the current
architecture at the e-sheet's shear-resonance line.  **They
correspond to no observed particles** and have no decay path
below their own mass under matter-only decay rules.

The fourth ghost, `(0, −1)` at 104 MeV, is a pure-ring mode
with Q_eff = 0 — a sub-π⁰ neutral spin-½ prediction that
matches nothing in the observed spectrum between the neutrino
(meV) and the neutron (939 MeV).

## F3. The ghost problem is UNIVERSAL across the tested grid

Phase B's 41 × 56 = 2296-point grid shows:

> **Zero points are sub-observed-ghost-free.**

Not a single `(ε_e, s_e)` in the tested range `ε_e ∈ [250, 650]`,
`s_e ∈ [1.95, 2.06]` produces an e-sheet spectrum without sub-
observed ghosts.  This is a **structural feature of the current
architecture**, not a property of R53 Solution D specifically.

The ghost count map (`outputs/track4_ghost_breakdown.png` left
panel) does show structure:

- **Ghost count is MINIMIZED near `s_e ≈ 2.00`** (4 ghosts at
  baseline) — R53 Solution D happens to sit in a local valley
  of ghost count, as tight as the e-sheet gets without a
  selection rule.
- Moving away from `s_e = 2.00`, ghost count grows rapidly to
  10–16 as more `(n, 2n)`-family modes cross into sub-observed
  territory.

**R53 Solution D is a local minimum, not a zero.**  The ghost
problem on the e-sheet is architectural.

## F4. Sub-electron ghosts appear scattered

The right panel of `track4_ghost_breakdown.png` shows a scatter
pattern of 1s and 0s for the sub-electron criterion (charged
modes below 0.511 MeV).  Roughly half of grid points have zero
sub-electron ghosts; the other half have exactly one.  Baseline
is in a 0-count region (electron is the lightest charged mode,
as R53 intended).

The scatter pattern suggests no smooth structural explanation —
it's driven by exactly where specific low-winding modes land on
the μ(n_et, n_er) surface.  Not a primary concern given
baseline avoids it.

## F5. The peak-fitness plot is dominated by the ghost mask

Because sub-observed ghosts are present at every grid point,
the masked fitness heat map
(`outputs/track4_fitness.png`) is almost entirely
hatched.  Only a few corner points (high-s_e, high-ε_e) remain
un-hatched, and their fitness is low (only the electron
calibration contributes).  **The heat map is not interpretable
as a search aid in this form** — it is, however, a visually
striking confirmation that the e-sheet has systemic ghost
problems across parameter space.

## F6. Interpretation — R33's n_tube = ±1 filter was doing
      real work

The (2, 4), (3, 6), (4, 8) ghost modes are specifically
`|n_et| ≥ 2` modes.  R33's earlier-era **n_tube = ±1 selection
rule** would eliminate them by fiat, reducing the ghost list to
just the `(0, −1)` Q=0 mode.

This rule was stated by R33 as an observation about the charge
formula — real particles have tube winding ±1 — but it was
never formally encoded in the model-F architecture.  R60 T17's
e-sheet exemption from Z₃ didn't substitute for it (Z₃
addressed confinement, not winding restriction).

Track 4's audit is effectively **rediscovering the need for
R33's rule**.  Without it, the e-sheet admits a "tower" of
|Q|=2, 3, 4, ... ghost modes at multiples of m_e.  With it,
these are filtered out and only the |n_et|=1 lepton ladder
remains.

## F7. Where this leaves R63

The finding is significant: **the e-sheet has been assuming
R33's n_tube = ±1 filter all along, but that filter is not
stated in model-F's current architecture.**  Multi-sheet
searches (pool item e) effectively include this filter
implicitly — the "compound α formula" only gives a clean
charge when |n_et| = 1 on the e-sheet side.  But the pure
single-sheet audit exposes the architectural gap.

Two paths forward are defensible:

**A. Formally adopt R33's n_tube = ±1 rule on the e-sheet.**

Add it to model-F as a principled selection rule (analogous to
Z₃ on the p-sheet).  The physical justification needs work —
R33's argument was based on KK charge formula / CP phase
structure, which could be re-derived under current
architecture.  Once adopted:

- E-sheet charged modes have |Q| = 1 by construction.
- The (n, 2n) ghost tower at 2m_e, 3m_e, 4m_e disappears.
- Tracks 1–3b's p-sheet work stands unchanged.
- The (0, −1) Q=0 ghost remains and needs separate attention
  (ν-sheet-analogous filter?).

**B. Revisit the architecture.**

If n_tube = ±1 is not derivable from first principles, then the
|Q|≥2 ghost tower is a real prediction that clashes with
observation.  This would require a new mechanism — perhaps
analogous to the Z₃ density-fluctuation cancellation on the
p-sheet, but adapted to the e-sheet's extreme-shear regime.

Either way, **this is a prerequisite question for multi-sheet
work**.  If we proceed to pool item e (multi-sheet inventory
at the p-sheet's `(0.80, 0.05)` peak) without resolving it,
we're implicitly making choice A without acknowledging it.

## What Track 4 establishes

1. **R53 Solution D is a local minimum of ghost count on the
   e-sheet, not zero.**  4 sub-observed ghosts exist at baseline.
2. **Tau matches well at low winding** — (−1, +15) at 0.14%
   off — so the R53 three-generation assignment works cleanly
   within |n_er| ≤ 30.
3. **Sub-observed ghosts are ubiquitous on the e-sheet** (100%
   of the 2296-point grid).  The problem is architectural, not
   parametric.
4. **The ghost tower at `|Q| = 2, 3, 4, ...` is specifically
   the `(n, 2n)` shear-resonance family** at multiples of m_e.
5. **R33's n_tube = ±1 selection rule would eliminate these**
   but has not been formally preserved in model-F.
6. **Multi-sheet searches implicitly assume this filter** via
   the composite α formula's unit-charge reading.

## Status

**Track 4 complete.**  The e-sheet is NOT as ghost-clean as
the p-sheet under the current architecture.  R53 Solution D is
a local minimum but not ghost-free.  **R33's n_tube = ±1
selection rule needs to be formally adopted or re-derived**
before multi-sheet searches (pool item e) can proceed with
full confidence that the component sheets are clean.

Pool item **m** (e-sheet winding restriction / high-|n_et|
filter) is the natural follow-up — no longer a speculative
backup but a concrete architectural task: formalize R33's
rule in model-F's language.
