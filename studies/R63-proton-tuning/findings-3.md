# R63 Track 3: Pure p-sheet fitness heat map

**Scope.**  Replace Track 2's brittle binary-threshold match count
with a continuous fitness score; sweep `(ε_p, s_p)` on a fine grid
(81 × 51 = 4131 points, steps of 0.01) and produce visualizations
of the landscape.

**Fitness definition.**  For each of baseline's 7 target particles,
find the pure p-sheet Z₃-free mode with matching |Q| closest to the
observed mass, compute `Δm/m`, and define closeness as:

<!-- closeness = max(0, 1 − |Δm/m| / threshold) -->
$$
\text{closeness}_i \;=\; \max\!\Big(0,\ 1 - \frac{|\Delta m_i|/m_i}{\text{threshold}_i}\Big)
$$

Thresholds: 0.02 for most particles; 0.14 for π⁰ (per model-F
tolerance).  Total fitness = Σ closeness over the 7 targets.
Maximum possible: 7.0 (every particle exactly matched).

Ghost-region points (any sub-π⁰ ghost per Track 1's criterion) are
masked from the fitness map and drawn with a hatched overlay.

Script:
[`scripts/track3_fitness_heatmap.py`](scripts/track3_fitness_heatmap.py)
Outputs:
[`outputs/track3_fitness.png`](outputs/track3_fitness.png),
[`outputs/track3_ghost_count.png`](outputs/track3_ghost_count.png),
[`outputs/track3_mu36.png`](outputs/track3_mu36.png),
[`outputs/track3_grid.csv`](outputs/track3_grid.csv)

---

## F1. The landscape has two distinct high-fitness regions

The fitness heat map (`outputs/track3_fitness.png`) reveals a
landscape with two clear local maxima inside the ghost-free region:

| Region | Approx. location | Peak fitness |
|:-------|:-----------------|:------------:|
| **Primary peak**    | ε_p ≈ 0.73, s_p ≈ 0.34 | **4.93** / 7 |
| **Secondary peak**  | ε_p ≈ 0.89, s_p ≈ 0.01 | **4.82** / 7 |

The ghost-free region spans roughly 88% of the plotted area
(3634 / 4131 grid points).  The analytic ghost-free boundary
`μ(3, 6) = 8.09` (drawn as a red dashed curve) matches the grid's
ghost-count transition exactly — no surprises at the boundary.

Baseline `(0.55, 0.162)` sits in a relatively LOW-fitness region
(fitness ≈ 4.0), well inside the ghost-free area but not near
either local maximum.  **Baseline is not the fitness optimum.**

## F2. Baseline's "7 matches" claim was misleading

Track 2 reported that baseline "preserves all 7 baseline matches"
— a statement that is technically true at the 2% threshold but
masks serious near-edge matches.  The continuous-scoring
breakdown at baseline:

| Particle | Target (MeV) | Best match | Δm/m | Closeness |
|:--------:|-------------:|:-----------|-----:|----------:|
| p        | 938.27 | exact | +0.00% | **1.00** |
| π⁰       | 134.98 | (0, −1) = 121.0 MeV | +10.37% | 0.26 |
| η′       | 957.78 | (0, −8) = 967.8 MeV | +1.04% | 0.48 |
| Δ⁺       | 1232.0 | (−3, −9) = 1223.2 | +0.71% | 0.64 |
| Ξ⁻       | 1321.7 | (−3, +9) = 1323.7 | +0.15% | 0.92 |
| Ξ⁰       | 1314.9 | (0, −11) = 1330.7 | +1.20% | 0.40 |
| Ω⁻       | 1672.5 | (−3, +12) = 1648.3 | +1.44% | 0.28 |
| **Total** | | | | **3.98** |

All 7 targets match within threshold, but several are sitting near
the edge: π⁰ at 10.4% off (only 26% closeness inside the 14%
pion window), Ω⁻ at 1.44% (28% closeness inside the 2% window),
Ξ⁰ at 1.20% (40% closeness), η′ at 1.04% (48% closeness).  These
are legitimate matches, not ghosts, but not strong ones.

## F3. The secondary peak at (0.89, 0.01) dramatically improves the pion

The `(0.89, 0.01)` secondary peak with fitness 4.82 achieves
something model-F has struggled with for a year — a clean π⁰
match.  Breakdown:

| Particle | Target (MeV) | Best match | Δm/m | Closeness |
|:--------:|-------------:|:-----------|-----:|----------:|
| p        | 938.27 | exact | +0.00% | **1.00** |
| π⁰       | 134.98 | (0, −1) = 136.9 MeV | **+1.39%** | **0.90** |
| η′       | 957.78 | (0, −7) = 958.0 MeV | **+0.02%** | **0.99** |
| Δ⁺       | 1232.0 | (−6, −6) = 1229.7 | +0.19% | 0.91 |
| Ξ⁻       | 1321.7 | (−3, +9) = 1319.1 | +0.20% | 0.90 |
| Ξ⁰       | 1314.9 | (0, −10) = 1368.6 | +4.08% | 0.00 |
| Ω⁻       | 1672.5 | (−3, −12) = 1701.9 | +1.76% | 0.12 |
| **Total** | | | | **4.82** |

Highlights vs. baseline:

- **π⁰ at +1.39%** vs baseline's +10.37% — about 7× improvement.
  The pure p-sheet pion match at this geometry is comparable to
  other hadron matches.
- **η′ at +0.02%** vs baseline's +1.04% — near-exact.
- **Δ⁺, Ξ⁻ both improve** over baseline.
- **Ξ⁰ is lost** (4.08% off — outside the 2% window).
- **Ω⁻ degrades** (1.76% vs baseline's 1.44%, both still within
  threshold but closeness drops from 0.28 to 0.12).

Net: trades Ξ⁰ for much better π⁰ and η′ matches.  Structurally
similar to Track 21's goal (fixing the pion desert) but without
the sub-π⁰ ghosts that Track 21's extreme introduced.

## F4. The primary peak at (0.73, 0.34) is different in character

`(0.73, 0.34)` with fitness 4.93 takes a different trade-off:

| Particle | Target (MeV) | Best match | Δm/m | Closeness |
|:--------:|-------------:|:-----------|-----:|----------:|
| p        | 938.27 | exact | +0.00% | **1.00** |
| π⁰       | 134.98 | (0, −1) = 145.3 | +7.66% | 0.45 |
| η′       | 957.78 | (0, −7) = 1017.2 | +6.21% | **0.00** (lost) |
| Δ⁺       | 1232.0 | (−6, 0) = 1230.6 | +0.11% | 0.94 |
| Ξ⁻       | 1321.7 | (−6, −6) = 1325.8 | +0.31% | 0.85 |
| Ξ⁰       | 1314.9 | (0, −9) = 1307.9 | +0.53% | 0.73 |
| Ω⁻       | 1672.5 | (−6, +6) = 1670.8 | **+0.10%** | **0.95** |
| **Total** | | | | **4.93** |

Highlights: near-exact on Δ⁺ and Ω⁻ simultaneously (both at
~0.1%), decent Ξ⁰ and Ξ⁻.  η′ is lost entirely.

## F5. Three distinct configurations — three different stories

Side-by-side:

| Geometry | Fitness | π⁰ | η′ | Δ⁺ | Ξ⁻ | Ξ⁰ | Ω⁻ | Story |
|:---------|:-------:|:--:|:--:|:--:|:--:|:--:|:--:|:------|
| baseline (0.55, 0.162) | 3.98 | 10.4% | 1.0% | 0.7% | 0.2% | 1.2% | 1.4% | All 7 at threshold, several near edge |
| primary (0.73, 0.34) | 4.93 | 7.7% | **lost** | 0.1% | 0.3% | 0.5% | 0.1% | Excellent Δ⁺ / Ω⁻ / Ξ⁻, loses η′ |
| secondary (0.89, 0.01) | 4.82 | **1.4%** | **0.02%** | 0.2% | 0.2% | **lost** | 1.8% | Clean π⁰ and η′, loses Ξ⁰ |

The p-sheet has **structural tension**: no single `(ε_p, s_p)`
hits every target.  Different geometries offer different sets of
strong matches.  This is informative — the pure p-sheet's mass
ladder is rich but not infinitely tunable.

## F6. The ghost boundary is analytically exact

The ghost-count map (`outputs/track3_ghost_count.png`) shows the
sub-π⁰ ghost region on the left (ε_p < ~0.55), bounded exactly by
the analytic curve `μ(3, 6) = 8.09`.  The grid's discrete
ghost/no-ghost transition traces the curve with no gaps or
surprises — Track 1's algebraic derivation is vindicated at fine
resolution.

88% of the 4131 tested points are ghost-free.  The ghost-free
region has a clean curved lower-left boundary and extends
indefinitely to the upper right in the tested range.

---

## What Track 3 establishes

1. **The fitness landscape is structured, not flat.**  Two local
   maxima exist inside the ghost-free region, with fitnesses
   4.93 and 4.82 out of 7.
2. **Baseline is not the optimum.**  Under continuous scoring,
   baseline scores 3.98 — worse than 10+ of the top candidates.
   The "7 matches at 2% threshold" result hid the fact that
   most matches were near-edge.
3. **The pion problem is solvable by proton-sheet re-tuning
   without introducing ghosts.**  `(0.89, 0.01)` achieves π⁰
   at 1.4% off and η′ at 0.02% off while staying inside the
   ghost-free region.  Track 21's approach was right in
   principle but chose an inviable geometry; Track 3 finds a
   viable alternative.
4. **The p-sheet cannot fit every observed particle
   simultaneously** — there is intrinsic tension in the mass
   ladder.  Two distinct peaks at different (ε_p, s_p) match
   different subsets well.  This raises the question of whether
   "best" should be measured against a specific target set or
   against observation overall.
5. **The ghost-free boundary is structurally exact** and matches
   the analytic `μ(3, 6) = 8.09` derivation perfectly.

## Candidate shortlist (for downstream work)

Of the top fitness points, three are structurally distinct
candidates worth considering:

| Point | ε_p | s_p | L_ring_p | Fitness | Best for |
|:------|:---:|:---:|:--------:|:-------:|:---------|
| baseline | 0.55 | 0.162 | 47.29 | 3.98 | Historical; all 7 at threshold |
| **secondary peak** | **0.89** | **0.01** | 42.02 | **4.82** | **Solves the pion problem** |
| primary peak | 0.73 | 0.34 | 40.93 | 4.93 | Highest fitness, strong baryons, loses η′ |

## Implications for R63

Track 3 supersedes Track 2's claim that baseline is among the
best points.  Three concrete next questions:

- **Can `(0.89, 0.01)` survive the multi-sheet inventory check?**
  Its pure p-sheet π⁰ match is dramatically better than baseline;
  if the 14 of 16 non-pion matches from R60 T19 don't regress
  here, this is a candidate for an improved model-F baseline.
- **What does the primary peak `(0.73, 0.34)` lose on the
  multi-sheet inventory?**  Its pure p-sheet η′ loss might be
  compensated by a multi-sheet assignment.
- **Is there an even better point if we widen the target set?**
  Track 3 fitted only baseline's 7 matched particles.  Scoring
  against all ~20 observed matter particles might shift the
  optima further — pool item candidate.

The immediate recommendation is **pool item e (multi-sheet
inventory consistency)** tested at both peaks, with emphasis on
whether `(0.89, 0.01)` closes the pion problem without breaking
anything else.

## Status

**Phase A complete.**  Heat map produced; two local maxima
identified, baseline is not the optimum.  See Phase B for a
physically-principled re-scoring that changes the picture.

---

# Phase B — width-weighted thresholds (user-suggested refinement)

**Motivation.**  Phase A used flat thresholds (2% for most
particles, 14% for π⁰) — a convenience that treated pions
leniently because of model-F's known pion desert.  This is not
physically principled.  A more honest criterion uses each
particle's natural line width Γ = ℏ/τ as the scale.  Broad
resonances tolerate large fractional misses; narrow resonances
and stable particles demand precision.

**Width-weighted threshold** per target particle:

<!-- threshold_i = max(0.02, 2 · Γ_i / m_i) -->
$$
\text{threshold}_i \;=\; \max\!\Big(0.02,\ 2 \cdot \frac{\Gamma_i}{m_i}\Big)
$$

The 2% floor represents model-level precision (the geometry is
not perfect even for stable particles); the width-scaling
respects natural uncertainty in the observed masses.

Computed thresholds for the 7 target particles:

| Particle | τ | Γ / m | Threshold |
|:--------:|:--:|:-----:|:---------:|
| p | stable | 0 | **2.0%** (floor) |
| π⁰ | 8.4×10⁻¹⁷ s | 5.8×10⁻⁸ | **2.0%** (floor) |
| η′ | 3.4×10⁻²¹ s | 2.0×10⁻⁴ | **2.0%** (floor) |
| Δ⁺ | 5.6×10⁻²⁴ s | **9.5%** | **19.0%** (width) |
| Ξ⁻ | 1.6×10⁻¹⁰ s | ~10⁻¹⁵ | **2.0%** (floor) |
| Ξ⁰ | 2.9×10⁻¹⁰ s | ~10⁻¹⁵ | **2.0%** (floor) |
| Ω⁻ | 8.2×10⁻¹¹ s | ~10⁻¹⁵ | **2.0%** (floor) |

Only Δ⁺ has natural width large enough to push above the 2%
floor.  Notably, **π⁰'s threshold tightens from 14% (Phase A)
to 2%** — its natural width is tiny despite its short lifetime.

Script:
[`scripts/track3b_width_weighted.py`](scripts/track3b_width_weighted.py).
Outputs:
[`outputs/track3b_fitness_width.png`](outputs/track3b_fitness_width.png),
[`outputs/track3b_comparison.png`](outputs/track3b_comparison.png),
[`outputs/track3b_difference.png`](outputs/track3b_difference.png),
[`outputs/track3b_grid.csv`](outputs/track3b_grid.csv).

---

## F7. The optimum shifts to (0.80, 0.05)

Under width-weighted scoring the top 10 points cluster
differently, and the peak moves:

| Rank | ε_p | s_p | Fitness (/7) | μ(3,6) |
|:---:|:---:|:---:|:------------:|:------:|
| 1 | **0.80** | **0.05** | **4.946** | 6.95 |
| 2 | 0.82 | 0.03 | 4.877 | 6.95 |
| 3 | 0.72 | 0.18 | 4.865 | 6.87 |
| 4 | 0.53 | 0.19 | 4.832 | 7.84 |
| 5 | 0.72 | 0.17 | 4.822 | 6.89 |
| 6 | 0.63 | 0.32 | 4.807 | 6.93 |
| 7 | 0.72 | 0.16 | 4.756 | 6.92 |
| 8 | 0.81 | 0.05 | 4.726 | 6.92 |

**Under width-weighting, baseline (0.55, 0.162) falls to fitness
4.04 — not even in the top 50.**  Neither of Phase A's "best"
points (0.73, 0.34 and 0.89, 0.01) hold up either.

## F8. The width-weighted peak has a near-exact π⁰ match

Breakdown at the new width-weighted peak `(ε_p = 0.80, s_p = 0.05)`:

| Particle | Threshold | Δm/m | Closeness | Best mode |
|:--------:|:---------:|-----:|----------:|:----------|
| p | 2% | **0.000%** | 1.000 | (−3, −6) — exact |
| π⁰ | 2% | **+0.038%** | **0.981** | (0, −1) @ 135.0 MeV |
| η′ | 2% | +1.314% | 0.343 | (0, −7) @ 945.2 |
| Δ⁺ | 19% | +3.246% | 0.829 | (−6, −6) @ 1272.0 |
| Ξ⁻ | 2% | +0.066% | 0.967 | (−6, +6) @ 1322.6 |
| Ξ⁰ | 2% | +2.694% | 0.000 | (0, −10) @ 1350.3 |
| Ω⁻ | 2% | +0.349% | 0.826 | (−3, −12) @ 1678.3 |
| **Total** | | | **4.946** | |

**The π⁰ match is essentially exact at 0.038% off** — vs
baseline's 10.4% and Phase A's secondary peak (0.89, 0.01) at
1.4%.  The pure p-sheet at this geometry is ringing on the π⁰
mass to precision comparable to the stable proton match.

This is a striking result: the residual pion gap that has
puzzled model-F throughout its development closes completely at
`(ε_p = 0.80, s_p = 0.05)` on the pure p-sheet.

## F9. Every candidate trades something for something

Side-by-side breakdown of all key points under width-weighted
scoring:

| Geometry | Fit | π⁰ | η′ | Δ⁺ | Ξ⁻ | Ξ⁰ | Ω⁻ | Story |
|:---------|:---:|:--:|:--:|:--:|:--:|:--:|:--:|:------|
| baseline (0.55, 0.162) | 4.04 | 10.4% | 1.0% | 0.71% | 0.15% | 1.2% | 1.4% | Bad π⁰, several near-edge |
| **peak (0.80, 0.05)** | **4.95** | **0.04%** | 1.3% | 3.2% | 0.07% | 2.7% | 0.35% | **Exact π⁰**, loses Ξ⁰ barely |
| near-base (0.53, 0.19) | 4.83 | 11.4% | **0.09%** | 1.4% | 0.63% | **0.07%** | 1.4% | Near-exact η′ + Ξ⁰, bad π⁰ |
| old-prim (0.73, 0.34) | 4.53 | 7.7% | 6.2% | 0.11% | 0.31% | 0.53% | 0.10% | Excellent baryons, loses η′ |
| old-sec (0.89, 0.01) | 4.30 | 1.4% | **0.02%** | 0.19% | 0.20% | 4.1% | 1.8% | Good π⁰ + η′, loses Ξ⁰ |

The p-sheet genuinely cannot hit all 7 target particles
simultaneously.  Different geometries optimize different
subsets, and the "right" trade-off depends on what the model is
supposed to predict.

## F10. Difference map reveals where threshold choice matters

The `track3b_difference.png` map (fitness_width − fitness_flat)
shows:

- **Large positive regions (red)** in the upper-right quadrant
  (ε_p > 0.70, s_p > 0.20) — width-weighting rewards these
  geometries substantially because they exploit Δ⁺'s wide
  window and the flat threshold under-credited them.
- **Narrow blue streaks** — lines in parameter space where
  Phase A's flat 14% pion threshold was catching a π⁰ match
  that the tighter 2% width-weighted threshold rejects.  These
  appear as "cliffs" where fitness drops under stricter scoring.
- **Baseline sits in a nearly-neutral region** — its fitness
  is essentially unchanged by the threshold reframing (4.04
  either way).  Baseline was never getting much credit from
  the generous pion threshold.

## Revised candidate shortlist

Under physically-principled width-weighted scoring:

| Candidate | Fitness | Notable feature |
|:----------|:-------:|:---------------|
| **`(0.80, 0.05)`** | **4.95** | **π⁰ at 0.038%** — pion problem solved |
| `(0.72, 0.18)` | 4.87 | strong baryons, compact cluster |
| `(0.53, 0.19)` | 4.83 | near-baseline; η′ and Ξ⁰ near-exact |
| `(0.63, 0.32)` | 4.81 | alternative baryon-strong point |
| baseline `(0.55, 0.162)` | 4.04 | historical; middle of pack |

## What Phase B establishes

1. **The 14% π⁰ threshold was an artificial concession** that
   propped up baseline and obscured the true optimum.  Under
   physically-principled width-weighted thresholds, the peak
   moves to **`(0.80, 0.05)`** with a near-exact π⁰ match.
2. **Baseline is definitively not the optimum** — fitness 4.04
   out of 7, vs ~4.95 at the peak.  The "7 matches at
   threshold" claim from Tracks 1–2 was technically true but
   carried little physical weight at several edges.
3. **The pion desert is not structural** — it resolves
   completely at `(0.80, 0.05)` on the pure p-sheet.  This
   confirms what Track 21 gestured at but could not land
   without introducing ghosts.
4. **No single geometry hits every target.**  Even the peak
   loses Ξ⁰ barely.  The p-sheet is rich but not unboundedly
   tunable; multi-sheet participation is genuinely needed for
   some particles.

## Implications for R63

**Track 3 Phase B recommends `(ε_p = 0.80, s_p = 0.05)` as the
prime candidate for a proton-sheet re-optimization.**  It:

- Solves the pion problem completely (0.04% off).
- Keeps 5 of 7 target particles within the 2% threshold.
- Loses Ξ⁰ narrowly (2.7% off, just past 2%) — may be
  recoverable as a multi-sheet compound at this geometry.
- Sits safely inside the ghost-free region (μ(3,6) = 6.95,
  well below the 8.09 bound).
- L_ring_p ≈ 39 fm at this point (vs baseline's 47 fm) — a
  modest shift that nuclear scaling can likely accommodate.

The critical next test is whether the multi-sheet inventory
from R60 T19 survives at `(0.80, 0.05)` — the 14 of 16
hadron matches and nuclear scaling.  If yes, this geometry
becomes the strongest candidate for an improved model-F
baseline we've identified to date.

## Status

**Track 3 complete (Phase A + Phase B).**  Width-weighted
scoring reveals a new optimum at **`(0.80, 0.05)` with
fitness 4.95** and a near-exact pion match at 0.038%.  Baseline
(fitness 4.04) is not competitive under physically-principled
thresholds.  Next: multi-sheet inventory verification at this
and neighboring candidate points (pool item e).
