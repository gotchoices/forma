# R63 Track 1: Pure p-sheet ghost audit — validation at two points

**Scope.**  Enumerate pure p-sheet modes `(0, 0, 0, 0, n_pt, n_pr)`
and classify each against the observed particle spectrum at two
specific `(ε_p, s_p)` points: the model-F baseline and Track 21's
pion-optimal candidate.  Test R60 Track 16's prediction that free
p-sheet modes require `n_pt ≡ 0 (mod 3)` produces a clean spectrum.

Script:
[`scripts/track1_proton_ghost_audit.py`](scripts/track1_proton_ghost_audit.py)

Classification (charge-and-mass only; spin is realized by 1-sheet
vs compound SU(2) composition per R62 7d):

- **observed** — mode mass matches an observed particle at
  compatible |Q| within model-F threshold (2%, or 14% for pions).
- **split-dominated** — unmatched, but above the lightest observed
  particle of matching |Q| and above the electron-emission
  threshold `|Q| × m_e`.  Plausible short-lived resonance.
- **ghost-sub-observed** — predicted mass is BELOW the lightest
  observed particle of matching |Q|.  The model says "there's a
  particle here" and nature says "there isn't."

**Important limitation.**  Track 1 tested only two specific
`(ε_p, s_p)` points.  It does NOT characterize the full range of
viable values.  That requires Track 2.

---

## F1. At model-F baseline, R60 T16's Z₃ rule produces a clean spectrum

At `(ε_p, s_p) = (0.55, 0.162037)`, `L_ring_p = 47.29 fm`:

Enumerating pure p-sheet modes in `(n_pt, n_pr)` with
`|n_pt| ≤ 12, |n_pr| ≤ 18` yields 355 distinct modes below
2.5 GeV.  Applying the Z₃ filter (`n_pt ≡ 0 mod 3`):

| | Count |
|---|---:|
| Z₃-confined constituents (not free) | 239 |
| Z₃-free candidates | 116 |
| &nbsp;&nbsp;&nbsp;&nbsp;— observed | 8 |
| &nbsp;&nbsp;&nbsp;&nbsp;— split-dominated | 108 |
| &nbsp;&nbsp;&nbsp;&nbsp;— **sub-observed ghosts** | **0** |

**Baseline passes the audit.**  R60 T16's Z₃ rule + natural
matter-decay availability produces a clean pure-p-sheet spectrum.
The user's recollection — "we eliminated ghosts below 3 × (1, 2)
modes working together in 3-phase orientation" — is validated at
this specific point.

## F2. Pure p-sheet rings on 7 observed particles at baseline

At baseline, mass+charge matches to known particles (spin-
agnostic, since pure-p single-sheet is spin ½ but compound
realizations can give any allowed SU(2) spin):

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

Notable: **Δ⁺ at 1232 MeV — previously flagged "topologically
forbidden" in model-F** — shows up naturally as the `(3, 9)` Z₃
composite at 1223 MeV (0.71% off), parallel to the proton's
`(3, 6)` as three (1, 2) quarks.  `(3, 12)` at 1648 MeV sits
near Ω⁻ (1.44% off).  These are mass-level coincidences; physical
spin realization (spin 3/2 for Δ⁺ and Ω⁻) needs multi-sheet
composition.

## F3. The sub-proton region is structurally clean at baseline

Below the proton (938 MeV), every Z₃-free mode is either
observed (π⁰) or matter-decay-dominated:

- Neutral modes (0, −1) through (0, −7) at 121, 242, 363, 484,
  605, 726, 847 MeV: all split-dominated.
- Charged modes (−3, 0), (−3, ±1), (−3, ±2), etc. at 662–936
  MeV: all split-dominated via matter decay to lighter
  observed products.
- Nothing below π⁰ (135 MeV) has spin-1/2 nature predicted
  where none is observed.

## F4. Track 21's extreme pion-shift introduces sub-π⁰ ghosts

At `(ε_p, s_p) = (0.15, 0.05)` — Track 21's pion-optimal
candidate — `L_ring_p` grows from 47 fm to 127 fm.  The p-ring
mode spacing drops from ~121 MeV (baseline) to ~45 MeV.
Re-running the audit:

| | Count |
|---|---:|
| Z₃-free candidates | 92 |
| &nbsp;&nbsp;&nbsp;&nbsp;— observed | 9 |
| &nbsp;&nbsp;&nbsp;&nbsp;— split-dominated | 81 |
| &nbsp;&nbsp;&nbsp;&nbsp;— **sub-observed ghosts** | **2** |

The two sub-observed ghosts:

| Mode | E (MeV) | |Q| | Problem |
|:----:|-------:|:---:|:--------|
| (0, −1) | 45.03 | 0 | below lightest Q=0 observed (π⁰ at 135) |
| (0, −2) | 90.05 | 0 | below π⁰ |

**Track 21's naive shift fails the sub-observed ghost test.**  The
same geometry that closes the pion desert also predicts phantom
neutral modes at 45 and 90 MeV where nature has nothing.

## F5. Structural boundary: `μ(3, 6) ≤ 8.09`

The sub-pion ghost problem appears when the lowest Q=0 pure
p-sheet mode `(0, −1)` drops below π⁰'s lower match threshold
(116 MeV, i.e. 14% below 135).  Since L_ring_p is always
calibrated to put (3, 6) at the proton mass, the energy of
(0, −1) is:

<!-- E(0, -1) = 938 × μ(0, -1) / μ(3, 6) = 938 / μ(3, 6) -->
$$
E(0, -1) \;=\; m_p \cdot \frac{\mu(0, -1)}{\mu(3, 6)}
\;=\; \frac{m_p}{\mu(3, 6)}
$$

For `E(0, -1) ≥ 116 MeV` (i.e., (0, -1) at worst still matches
π⁰ within pion threshold):

<!-- μ(3, 6) ≤ 938/116 = 8.09 -->
$$
\mu(3, 6) \;\le\; \frac{m_p}{116 \text{ MeV}} \;\approx\; 8.09
$$

where `μ²(3, 6) = (3/ε_p)² + (6 − 3 s_p)²`.  Checking the two
tested points:

- Baseline (0.55, 0.162): μ(3, 6) = **7.76** ✓ (inside bound)
- Track 21 (0.15, 0.05): μ(3, 6) = **20.84** ✗ (way outside)

This bound defines a 2D region in `(ε_p, s_p)` space, not a single
point.  A coarse back-of-envelope along slices of s_p:

| s_p | minimum ε_p (μ(3,6) ≤ 8.09) |
|----:|----------------------------:|
| 0.00 | ≥ 0.552 |
| 0.16 | ≥ 0.506 (baseline: 0.55, margin ~9%) |
| 0.30 | ≥ 0.477 |
| 0.50 | ≥ 0.446 |
| 1.00 | ≥ 0.399 |

Baseline sits well inside the viable region — it is not a
knife-edge; there is comfortable slack in both directions.
**But exactly how far the region extends and which points
preserve the 7 baseline observed matches is NOT characterized
by Track 1.**

## F6. What Track 1 did NOT establish

Explicitly, Track 1 does not tell us:

- Whether other points within the `μ(3, 6) ≤ 8.09` region give
  additional observed-particle matches or lose them.
- Whether the nuclear scaling `d → ⁵⁶Fe` at ≤ 1.4% is preserved
  across the viable region.
- Whether the multi-sheet inventory matches (14 of 16 within
  1.12% from R60 T19) survive parameter variation.
- Whether there is a specific point in the viable region that
  improves the pion match without introducing sub-π⁰ ghosts.

These are Track 2's questions.

---

## What this means

**`(ε_p, s_p)` is not pinned by Track 1.**  What Track 1
establishes is:

1. Model-F's baseline `(0.55, 0.162)` is a viable point.  R60
   T16's Z₃ discipline works as designed at this geometry.
2. Track 21's extreme `(0.15, 0.05)` is infeasible.  The naive
   pion-fix shift introduces sub-π⁰ neutral ghosts and must be
   rejected.
3. The structural bound `μ(3, 6) ≤ 8.09` cleanly separates these
   two data points and defines a 2D region — not a single point.

The full range of viable `(ε_p, s_p)` values under the complete
set of constraints (ghost-clean + observed-match preservation +
nuclear scaling + multi-sheet inventory) remains to be mapped.

## Status

**Track 1 complete** — positive result at baseline, negative
result at Track 21's extreme, structural boundary identified.

**Next step: Track 2** — systematic sweep of `(ε_p, s_p)` across
the structural bound, with per-point validation against the
full constraint set.  Output: a viable-region map and the
best candidate(s) for subsequent observable-anchored work.
