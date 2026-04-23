# R63 Track 2: Pure p-sheet viable-region map

**Scope.**  Sweep `(ε_p, s_p)` over a 2D grid (17 × 13 = 221
points).  At each point, build the metric with σ_ra auto-updated,
calibrate L_ring_p to the (3, 6) proton, then run Track 1's pure
p-sheet audit.  Report: sub-observed ghost count, how many of
baseline's 7 observed-particle matches are preserved, and what
new matches may appear.

Grid:
- ε_p ∈ {0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60,
  0.65, 0.70, 0.80, 0.90, 1.00, 1.20, 1.50, 2.00}
- s_p ∈ {0.00, 0.05, 0.10, 0.14, 0.162, 0.18, 0.20, 0.25, 0.30,
  0.35, 0.40, 0.45, 0.50}

Script:
[`scripts/track2_viable_region.py`](scripts/track2_viable_region.py)
Grid data: [`outputs/track2_grid.csv`](outputs/track2_grid.csv)

---

## F1. The viable region is bounded cleanly by μ(3, 6) ≤ 8.09

**137 of 221 grid points (62%) produce zero sub-observed
ghosts.**  The ghost-free boundary in (ε_p, s_p) space traces
almost exactly the analytical bound derived in Track 1:

| ε_p | Ghost-free range of s_p |
|:---:|:------------------------|
| 0.20 – 0.40 | (no clean points) |
| 0.45 | only s_p = 0.50 |
| 0.50 | s_p ≥ 0.20 |
| 0.55 | s_p ≥ 0.05 |
| 0.60 and above | all tested s_p |

Cross-checking against the bound `μ(3, 6) = √[(3/ε_p)² +
(6 − 3·s_p)²] ≤ 8.09`:

- Below the bound → always clean (matches grid).
- Above the bound → always 1 sub-π⁰ ghost from the `(0, −1)`
  mode falling under π⁰'s 14%-match window.

The bound is the correct structural boundary.  Baseline `(0.55,
0.162)` sits at μ(3, 6) = 7.76 — well inside the viable region,
with ~4% slack to the bound.

## F2. Two points preserve all 7 baseline observed matches

Strict criterion — **zero ghosts AND all 7 baseline-matched
particles still within threshold** — finds 2 grid points:

| ε_p | s_p | L_ring_p (fm) | μ(3,6) | Baseline matches | Total | Extras gained |
|:---:|:---:|:-------------:|:------:|:----------------:|:-----:|:--------------|
| 0.55 | 0.162 | 47.29 | 7.756 | 7 / 7 | **7** | — (baseline itself) |
| **0.55** | **0.180** | **47.06** | **7.718** | **7 / 7** | **8** | **Λ** ← extra match |

The second point — `(ε_p, s_p) = (0.55, 0.180)` — is a **strict
improvement over baseline**: it preserves every observed match
baseline had AND picks up an additional Λ match, from a pure
p-sheet mode landing within 2% of the observed Λ(1115).

## F3. Broader shortlist: 7 points at ≥6/7 baseline matches

Relaxing to ≥ 6 of 7 baseline matches + 0 ghosts yields 7
points:

| ε_p | s_p | μ(3,6) | Baseline matched | Total | Lost | Gained |
|:---:|:---:|:------:|:----------------:|:-----:|:----:|:------:|
| 0.55 | 0.180 | 7.72 | 7 | **8** | — | Λ |
| 0.55 | 0.162 | 7.76 | 7 | 7 | — | — |
| **0.70** | **0.400** | **6.44** | 6 | **8** | η′ | **τ, φ** |
| **0.90** | **0.000** | **6.86** | 6 | **8** | Ξ⁰ | **Λ, η** |
| 0.60 | 0.300 | 7.14 | 6 | 7 | η′ | ρ |
| 0.55 | 0.100 | 7.89 | 6 | 6 | Ω⁻ | — |
| 0.55 | 0.140 | 7.80 | 6 | 6 | Ω⁻ | — |

Two points — `(0.70, 0.40)` and `(0.90, 0.00)` — also give
**total match count of 8**, but at different trade-offs:

- `(0.70, 0.40)` loses η′ but gains **τ AND φ** — two new
  particles the p-sheet naturally rings at this geometry.
- `(0.90, 0.00)` loses Ξ⁰ but gains Λ and η.

## F4. Broadest shortlist: 33 points at ≥5/7 baseline matches

Relaxing further (≥ 5 / 7 matches + 0 ghosts) yields 33 points
across the ε_p ∈ [0.50, 1.00], s_p ∈ [0.00, 0.50] region —
about 15% of the grid.  Among these:

- **(0.70, 0.25)** with μ(3, 6) = 6.78 matches **9 particles
  total**: keeps 5 of baseline's 7, gains Λ, Σ⁻, η, τ.  The
  highest-count geometry found but loses Δ⁺ and Ξ⁰.
- Several other geometries (0.60, 0.14; 0.80, 0.10; 0.90,
  0.162; etc.) reach 8 total matches with different losses
  and gains.

The trade-offs are real: as (ε_p, s_p) moves, resonances
shift relative to the 2% match threshold.  Different geometries
"pick up" different subsets of the observed spectrum.

## F5. Track 21's point is definitively outside the viable region

Track 21's candidate `(ε_p, s_p) = (0.15, 0.05)` is below the
grid's lower boundary (ε_p = 0.20), but the nearby points
confirm the structural incompatibility: every point with
ε_p ≤ 0.40 has at least 1 sub-observed ghost, and the lightest
ghost moves below π⁰ as ε_p decreases.  Under any Q=0 pion
match criterion — even the relaxed 14% pion threshold —
Track 21's geometry is inviable.

## F6. Recommendation: (0.55, 0.180) as the proton-sheet candidate

The clean win is `(ε_p, s_p) = (0.55, 0.180)`:

- **Zero ghosts** ✓
- **All 7 baseline matches preserved** ✓
- **One additional match (Λ) gained** — strict improvement
- **Sits next to baseline** — only s_p shifts by ~10% from 0.162
  to 0.180.  L_ring_p changes by 0.5% (from 47.29 to 47.06 fm).
- **Nuclear scaling likely preserved** (L_ring_p essentially
  unchanged).

This is a natural first candidate for an "improved proton-sheet"
point.  Validating it requires:

1. Re-run the multi-sheet inventory (R60 T19's 14-of-16 analysis)
   to confirm the other hadron matches don't regress.
2. Check nuclear scaling (d → ⁵⁶Fe at ≤ 1.4%) at the new
   L_ring_p.
3. Re-examine the ν-sheet dependencies if any.

Alternative interesting candidates: `(0.70, 0.40)` and
`(0.90, 0.00)` both reach 8 matches with different trade-offs
— these are worth exploring if `(0.55, 0.180)` fails a
downstream check.

---

## What Track 2 establishes

1. **The viable region in `(ε_p, s_p)` is bounded below by
   μ(3, 6) ≤ 8.09** (equivalently, roughly ε_p ≥ 0.55 for
   modest s_p).  The analytical Track 1 bound is confirmed
   by the grid.
2. **62% of tested grid points are ghost-free.**  Baseline is
   not knife-edge; comfortable slack exists in all directions.
3. **Two grid points preserve all 7 baseline matches**:
   baseline itself and `(0.55, 0.180)`.  The latter is a
   strict improvement (gains Λ).
4. **Multiple alternative viable geometries** exist with
   different trade-offs — some ring on τ, some on φ, some on
   Λ or η.  This suggests the p-sheet is genuinely rich in
   particle matches, not narrowly tuned.
5. **Track 21's extreme point is clearly outside the viable
   region** — confirms the rejection from Track 1.

## Implications for R63

The viable region is now characterized.  Next questions to
pursue from the pool are in a different framing than before:

- **Pool item a (sweep infrastructure)** — less critical now;
  we have a working Track 2 sweep.  Upgrade to observable-
  scoring sweep.
- **Pool item c (neutron-anchored sweep)** — now a natural
  next step.  The 7–8-match shortlist gives concrete
  candidates; neutron physics (3-sheet compound) should
  discriminate among them.
- **Pool item e (inventory consistency sweep)** — essential
  before adopting `(0.55, 0.180)`.  Verify the R60 T19
  14-of-16 matches don't regress at the new point.

## Status

**Track 2 complete.**  Viable-region map produced; the
structural bound μ(3, 6) ≤ 8.09 confirmed; baseline sits
comfortably inside; one candidate `(0.55, 0.180)` emerges as
a strict improvement (adds Λ without losing anything).  Several
alternative viable geometries identified.  Ready to hand off
to pool items c (neutron-anchored) or e (inventory consistency)
for further validation.
