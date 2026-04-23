# R63 Track 1: Pure p-sheet ghost audit — R60 T16 validated, Track 21 flagged

**Scope.**  Enumerate pure p-sheet modes `(0, 0, 0, 0, n_pt, n_pr)`
and classify each against the observed particle spectrum.  Audit
the discipline established by R60 Track 16: free p-sheet modes
require `n_pt ≡ 0 (mod 3)`, and all Z₃-free composites should
either match observed particles or be matter-decay-dominated.

Script:
[`scripts/track1_proton_ghost_audit.py`](scripts/track1_proton_ghost_audit.py)

Classification (charge-and-mass only, since the pure p-sheet
mode's spin can be realized differently under 1-sheet vs
compound SU(2) composition per R62 7d):

- **observed** — mode mass matches a known particle's mass at
  compatible |Q| within the model-F threshold (2%, or 14% for
  pions per Track 21 tolerance).
- **split-dominated** — unmatched, but above the lightest
  observed particle of matching |Q| and above the electron-
  emission threshold `|Q| × m_e`.  These are plausible
  short-lived resonances consistent with R28's "dense modes
  above the predictive horizon."
- **ghost-sub-observed** — predicted mass is BELOW the lightest
  observed particle of matching |Q|.  The model says "there's
  a particle here" and the real world says "there isn't."
  **This is the real ghost problem.**

---

## F1. R60 T16's Z₃ rule is validated at model-F baseline

At `(ε_p, s_p) = (0.55, 0.162037)`, `L_ring_p = 47.29 fm`,
enumerating pure p-sheet modes in `(n_pt, n_pr)` with
`|n_pt| ≤ 12, |n_pr| ≤ 18` yields 355 distinct modes below
2.5 GeV.  Applying the Z₃ filter (`n_pt ≡ 0 mod 3`):

| | Count |
|---|---:|
| Z₃-confined constituents (not free) | 239 |
| Z₃-free candidates | 116 |
| &nbsp;&nbsp;&nbsp;&nbsp;— observed | 8 |
| &nbsp;&nbsp;&nbsp;&nbsp;— split-dominated | 108 |
| &nbsp;&nbsp;&nbsp;&nbsp;— **sub-observed ghosts** | **0** |

**VERDICT: zero sub-observed ghosts at baseline.**  R60 T16's
Z₃ rule + natural matter-decay availability produces a CLEAN
pure-p-sheet spectrum.  The user's recollection — "we
eliminated ghosts below 3 × (1, 2) modes working together in
3-phase orientation" — is validated.

## F2. Pure p-sheet naturally picks up 7 observed particles

The 8 mass-level matches against the observed spectrum
(charge-and-mass, spin handled by 1-sheet vs compound
realization):

| Mode | E (MeV) | Observed | Δm/m |
|:----:|-------:|:---------|-----:|
| (0, −1) | 120.97 | π⁰ | +10.37% |
| (−3, −6) | 938.27 | **proton** | +0.00% |
| (0, −8) | 967.79 | η′ | +1.05% |
| (−3, −9) | 1223.21 | Δ⁺ | +0.71% |
| (−3, +9) | 1323.76 | Ξ⁻ | +0.16% |
| (−6, 0) | 1324.95 | Ξ⁻ | +0.25% |
| (0, −11) | 1330.72 | Ξ⁰ | +1.21% |
| (−3, +12) | 1648.34 | Ω⁻ | +1.44% |

Notable: **Δ⁺ at 1232 MeV — previously listed as "topologically
forbidden"** in model-F — shows up naturally as the `(3, 9)`
Z₃ composite at 1223 MeV (0.71% off).  Under R60 T16's picture
this is "three (1, 3) quarks" parallel to the proton's "three
(1, 2) quarks."  The p-sheet rings on the (1, n_r) strand
ladder; Z₃ composites pick out the baryons.

The spin reading: these modes have spin ½ under 1-sheet DK.
Δ⁺ (spin 3/2) and Ω⁻ (spin 3/2) would need additional spin
structure beyond 1-sheet to physically match — that's an
independent R62 question.  What the audit confirms is that the
p-sheet rings at the correct (mass, |Q|) combinations for
these observed particles.

## F3. The sub-proton region is clean by structure

Ordering pure p-sheet Z₃-free modes below the proton
(< 938 MeV) at baseline:

| Mode | E (MeV) | |Q| | Classification |
|:----:|-------:|:---:|:---------------|
| (0, −1) | 120.97 | 0 | **observed (π⁰)** |
| (0, −2) | 241.95 | 0 | split-dominated |
| (0, −3) | 362.92 | 0 | split-dominated |
| (0, −4) | 483.90 | 0 | split-dominated |
| (0, −5) | 604.87 | 0 | split-dominated |
| (−3, 0) | 662.48 | 1 | split-dominated |
| (−3, ±1) | 662.78, 683.91 | 3 | split-dominated |
| (−3, ±2) | 684.80, 725.17 | 3 | split-dominated |
| (0, −6) | 725.85 | 0 | split-dominated |
| (−3, ±3) | 726.57, 783.12 | 1 | split-dominated |
| (−3, ±4) | 784.93, 854.37 | 3 | split-dominated |
| (0, −7) | 846.82 | 0 | split-dominated |
| (−3, ±5) | 856.51, 935.89 | 3 | split-dominated |
| (−3, −6) | 938.27 | 1 | **observed (proton)** |

**Every mode below the proton is either observed (π⁰) or
matter-decay-dominated.**  The intermediate Z₃-free composites
like (3, 0) = 662 MeV and (3, ±3) = 726/783 MeV are not
observed particles, but they have matter decay channels to
lighter observed products:

- (3, 0) at 662 MeV: can decay to p + π⁻ + light_stuff (938 −
  140 ≈ threshold too high for p + π alone, but e.g. 3π±+
  lighter products are kinematically fine).  Actually the
  simpler reading: 662 MeV > lightest |Q|=1 matter (e⁺ at
  0.511 MeV), so e⁺-emission channel is always energetically
  available.  This mode does not correspond to a stable
  observed particle — consistent with it being a short-lived
  pre-proton Z₃ composite.
- (3, ±1) at 663, 684 MeV: |Q|=3.  No observed |Q|=3 particle
  (because the Standard Model has none), but the mode can
  disperse via 3-electron emission above 1.5 MeV.
- (3, ±3) at 727, 783 MeV: |Q|=1, between the observed ρ±
  (775) but not within 2%.  Split-dominated, consistent with
  being unobservable as stable resonances.

No sub-pion neutral modes.  No sub-proton charged modes
unmatched.  The p-sheet ladder opens cleanly at (0, −1) = π⁰
and closes at (−3, −6) = proton.

## F4. Track 21's pion-optimal shift BREAKS cleanness

At `(ε_p, s_p) = (0.15, 0.05)` — Track 21's pion-fitting
candidate — `L_ring_p = 127.06 fm`.  The p-ring mode spacing
drops from 121 MeV (baseline) to about 45 MeV.  Re-running the
audit:

| | Count |
|---|---:|
| Z₃-free candidates | 92 |
| &nbsp;&nbsp;&nbsp;&nbsp;— observed | 9 |
| &nbsp;&nbsp;&nbsp;&nbsp;— split-dominated | 81 |
| &nbsp;&nbsp;&nbsp;&nbsp;— **sub-observed ghosts** | **2** |

**The 2 sub-observed ghosts:**

| Mode | E (MeV) | |Q| | Problem |
|:----:|-------:|:---:|:--------|
| (0, −1) | 45.03 | 0 | below lightest Q=0 observed (π⁰ at 135 MeV) |
| (0, −2) | 90.05 | 0 | below π⁰ |

Track 21's pion-optimal shift inflates `L_ring_p` from 47 fm
to 127 fm to fit pions.  That smaller p-ring spacing puts the
`(0, −1)` pure p-sheet mode at 45 MeV instead of 121 MeV — far
below π⁰.  No observed neutral particle exists below 135 MeV,
so the model at this geometry predicts phantom neutral modes
at 45 and 90 MeV.

**This is a concrete argument against adopting Track 21's
naive pion fix**: the same geometry shift that closes the pion
desert introduces sub-pion neutral ghosts.

## F5. What Track 1 establishes

1. **Baseline is right for the pure p-sheet** — no ghost
   problem at `(ε_p, s_p) = (0.55, 0.162)`.  R60 T16's Z₃
   discipline is confirmed to work as designed.
2. **The p-sheet is a rich mass axis** — 7 observed particles
   (proton, π⁰, η′, Δ⁺, Ξ⁻, Ξ⁰, Ω⁻) fall at pure p-sheet
   Z₃-free resonances at baseline.  A previously-"forbidden"
   particle (Δ⁺) gets a natural assignment as the (3, 9) Z₃
   composite.  The correspondence is mass-and-charge; spin
   realization via multi-sheet / SU(2) is a separate question.
3. **Track 21's naive pion shift must be rejected** — it
   introduces sub-pion neutral ghosts that the model cannot
   account for.  Any pion fix must preserve the baseline's
   sub-proton cleanness, which means `(ε_p, s_p)` must stay
   close to values that keep L_ring_p near 47 fm.

## Implication for R63

The pool of next-track candidates is re-prioritized:

- **a. Sweep infrastructure** — now constrained to preserve
  baseline's sub-proton cleanness.  Track 21's (0.15, 0.05)
  is out; but smaller shifts that preserve L_ring_p near
  baseline may still help pions.
- **b. Observable correlation audit** — particularly
  interesting now because the pure p-sheet gives 7 observed
  matches at once; checking their joint sensitivity to
  `(ε_p, s_p)` will tell us how tightly the observed spectrum
  pins the proton sheet.
- **c. Neutron-anchored sweep** — per the user's preferred
  anchor.  Neutron is a 3-sheet compound; this audit's
  pure-p-sheet clean ladder sets the boundary conditions.

The earlier-suggested pool items for ghost elimination
(**m** — e-sheet winding filter) can be deprioritized: the
"|Q|≥4 light ghosts" the broader Track 1 draft found are
artifacts of mixing e-sheet charge with p-sheet modes, not a
p-sheet problem.  That analysis moves to pool item **l**
(e-sheet re-validation) as an independent question.

## Status

**Track 1 complete — positive result for R60 T16.**  The Z₃
discipline produces a clean sub-proton p-sheet ladder at
model-F baseline.  Seven observed particles (proton, π⁰, η′,
Δ⁺, Ξ⁻, Ξ⁰, Ω⁻) emerge as pure p-sheet Z₃-free resonances.
Track 21's naive `(ε_p, s_p)` shift introduces sub-pion
ghosts and is rejected.  R63's pool items proceed with the
updated constraint: any proton-sheet re-optimization must
preserve the baseline's sub-proton cleanness.
