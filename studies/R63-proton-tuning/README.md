# R63: Proton-sheet tuning — disciplined audit and sweep

**Status:** Tracks 1–8 complete.  Track 9 complete: phases 9a
(linear cross-shear dressing), 9b (non-additive deuteron tuple
search), and 9c (mass-formula validity at high n_pt) each
falsified their respective candidate mechanisms cleanly.
**Track 10 active.**  The reviewer reframed Phase 9d as a
dedicated track around Pauli-saturated multi-strand coherence
(3 colors × 2 spins = 6 strand capacity per p-sheet tuple).
Phase 10a executed: the (1, 2) eigenmode geometry on the curved
p-sheet is characterized (FWHM ≈ 83°), but R60 T16's 2ω
back-reaction U₂ does not distinguish Z₆, 2 × Z₃, or Pauli-
saturated arrangements at N = 6 — all give U₂ = −3.  Higher
harmonics distinguish inconsistently and lack framework
selection.  **Pending decision** between Reading A (close R63;
binding requires framework extension), B (extend R60 T16 to
higher harmonics), or C (binding belongs to S-space).
See [findings-10.md](findings-10.md).
R63 is developing the **g-candidate** — the
evolving parameter set and rule set that is intended to become
model-G if and when it demonstrates clear superiority over
model-F across multiple axes.  The rule-set piece of the g-candidate is
[Q132 v2](../../qa/Q132-promotion-chain-principle.md) (the `v2`
is the version of the rule; the overall "what R63 is assembling"
is the g-candidate).  So far the g-candidate delivers a coherent
refinement of model-F: tighter discipline, preserved inventory
accuracy, same pion position, and a compound-mode nuclear
description that stays coherent across the full known chain.
Details by track in [findings-1.md](findings-1.md) through
[findings-7.md](findings-7.md).

### Terminology

- **g-candidate** (or just **g**) — the R63-developed candidate
  for an eventual model-G: parameter working values + rule
  refinements, held as "current best" but explicitly not pinned
  until a study-level review warrants it.
- **Q132 v2** — the rule-set version adopted by R63 (v1 was the
  initial, overly-restrictive draft).  Always kept as `v2` to
  distinguish from v1.
- **model-F** — the baseline model R63 is refining.  Fixed
  reference point for comparisons.

Earlier findings files (-5, -6) sometimes use "v2" as a shorthand
for the whole g-candidate; the intent was always the
g-candidate, and the two terms are used interchangeably in the
earlier writeups.

**Type:** theoretical + compute
**Depends on:** R60 (especially Tracks 7, 12, 21), R59, R53, R49, R61, model-F

---

## Objectives

R60 established model-F's architecture but deferred a systematic
re-examination of the variables that remain free under it.  Track
21 made the consequences concrete: the model-E-inherited
`(ε_p, s_p) = (0.55, 0.162)` is no longer pinned by the R19
constraint under σ_ra, and shifting to `(ε_p ≈ 0.15, s_p ≈ 0.05)`
closes the pion mass desert at baseline.

Before adopting that shift — or any other parameter change — the
proton sheet deserves the same discipline the electron sheet
already received via R53.  On the e-sheet, parameters were chosen
so that **every charged mode below some energy is an observed
lepton, and every mode above that is naturally routing-
suppressed** (R56/R57 argue spatial separation is cheaper than
mode-loading).  No ad hoc ghost filter is needed; the shear
resonance IS the filter.

The p-sheet has not had this treatment.  R19 pinned `(ε_p, s_p)`
on the α formula.  R60 preserved those values through the (3, 6)
Z₃ pivot.  R60 T19 ran an **observed → mode** inventory search
(for each known particle, find the best tuple), not the reverse.
R28 reported ~900 modes below 2 GeV against ~40 known particles;
whether the ~860-mode excess is legitimately routing-suppressed
or contains ghosts was never audited.

R63 addresses this gap in a **proton-focused** way:

1. **Track 1 (now):** restricted to the proton sheet.  Enumerate
   p-sheet-involving modes, classify each as
   observed / split-dominated / ghost, and try to eliminate any
   remaining **light ghosts** by modifying `(ε_p, s_p)` alone.
   Ghosts that exist but are above the routing-cost splitting
   threshold are acceptable — they're naturally suppressed.
   Other free variables (`ε_ν`, cross-sheet σ) are not moved in
   Track 1 even if the neutron or other compound fits want to.
2. **Subsequent tracks (chosen later):** if Track 1 leaves
   residual issues that `(ε_p, s_p)` alone cannot fix, promote
   pool items to bring in other free variables — in particular,
   `ε_ν` movement is acceptable in a later track if it is the
   price of a clean neutron fit.

R63 is explicitly disciplined: observable-anchored sweeps do not
run until the target observables are approved by the user and
their correspondence to MaSt geometry is argued out.

---

## Open variables under model-F

Canonical list from model-F card and R60 Tracks 7, 12, 14, 21:

| Variable | Status | Current value |
|----------|:-------|:--------------|
| `ε_e`, `s_e` | **Pinned** by R53 generations + R60 T17 exemption | 397.074, 2.004200 |
| `ε_p`, `s_p` | **Free** (R19 legacy no longer binding) | 0.55, 0.162 |
| `ε_ν` | **Effectively free**; only two discrete points tested | 2.0 (R61 #1) |
| `s_ν` | **Pinned** by Δm² ratio 33.6 | 0.022 |
| `k` (single-k) | **Structurally fixed** (R60 T14) | 1.1803/(8π) |
| `σ_ta`, `σ_at`, `g_aa` | **Fixed at R59 F59 natural form** | √α, 4πα, 1 |
| `σ_ra` per sheet | **Derived** (R60 T7): (sε)·σ_ta | — |
| `σ_ep`, `σ_eν`, `σ_νp` (cross-sheet) | **Unexplored**; pool item **h** | 0, 0, 0 |
| `L_ring_e`, `L_ring_p`, `L_ring_ν` | **Derived from masses via chosen anchoring mode** | see model-F card |

Free continuous axes: `ε_p`, `s_p`, `ε_ν`, and up to three
cross-sheet σ entries.  Anchoring-mode choice is a discrete
parameter worth auditing separately.

---

## Observables to consider (for the observable-anchored tracks)

Listed here so the pool items can reference them.  Commitment is
deferred; the user has flagged specific concerns noted below.

### Strong candidates (high precision, structural correlation plausible)

Neutron-related — neutron at ~15 minutes lifetime is nearly
stable on particle-physics terms.  The user has flagged the
neutron specifically as the preferred anchor.

| Observable | Value | Precision |
|------------|-------|-----------|
| Neutron mass `m_n` | 939.56542 MeV | ~10⁻⁸ |
| n−p mass difference `Δm` | 1.29333 MeV | ~10⁻⁶ |
| Neutron decay Q-value | 782.331 keV | ~10⁻⁵ |
| Neutron lifetime | ~879 s | ~0.5% |

**Nuclear masses / binding energies** — ~100+ stable isotopes
known to MeV or better; current model-F `n_pt = 3A, n_pr = 6A,
n_et = 1 − Z` scaling gives a multi-point constraint.

**Inventory-wide spectrum** — 14 of 16 non-pion hadrons at
sub-1.1% at baseline; re-run at each sweep point checks whether
pion improvements regress elsewhere.

### Gut-check only (do not use to pin)

**Proton and nuclear charge radii** — `r_p ≈ 0.8414 fm`, known
to ~1%.  Sensitive to L_ring_p in principle.  But the ~60–240×
gap between compact-dimension circumference (50–200 fm) and
measured 3D extent (0.84 fm) reflects an unresolved projection-
geometry relationship.  Using this as a primary anchor would
bake the unknown into the baseline.  Compute it, compare it,
but don't fit to it.

### Not yet usable (defer)

**Anomalous magnetic moments** — MaSt currently leaves these to
S-domain QED corrections.  No native Ma-domain mechanism exists;
using them to pin parameters would mix domains.
**Short-lived particles** (μ, τ, ephemeral mesons) — weak
gap-size-to-lifetime correlation; risk over-fitting to
transient states.  Use as cross-checks only.
**Cosmological observables** — out of scope.

---

## Track 1 — Proton-sheet ghost audit and adjustment

**Motivation.**  The electron sheet is already self-cleaning:
R53 tuned `(ε_e, s_e)` so that electron, muon, tau are the
three lowest charged modes, with higher modes heavy enough that
R56/R57 routing dominates.  The historically-worrisome (1, 1)
ghost is not filtered — it *is* the muon.  The shear resonance
substitutes for an explicit filter.

The proton sheet has not been audited this way.  Track 1 applies
the e-sheet discipline to the proton sheet.  Scope is **strictly
proton-focused**: only `(ε_p, s_p)` is moved in Track 1.  Other
free variables are left at baseline even if compound-mode fits
suggest they want to move — those movements are pool items for
future tracks.

**Scope.**

- **In:** single p-sheet modes `(0, 0, 0, 0, n_pt, n_pr)` under
  the Z₃ rule (`n_pt ≡ 0 mod 3`); compound modes with nonzero
  p-sheet activity (2-sheet `{e+p, ν+p}` and 3-sheet).
- **Out of Track 1 scope:** pure e-sheet modes (R53-validated),
  pure ν-sheet modes (only the (1, 0) item, which lives in pool
  **k**), and any proposed movement of `ε_ν`, `s_ν`, cross-sheet
  σ, or anchoring-mode choice.

**Goal.**  For each in-scope mode in ascending mass order,
classify as:

- (a) **observed particle** — match within the model-F threshold
      (tolerate the current 10–13% on pions per Track 21, on the
      understanding Track 21's `(ε_p, s_p)` shift closes them);
- (b) **split-dominated** — `E_mode > min(sum(E_obs_i) +
      V_separation)` per R56/R57 routing, so naturally
      suppressed and acceptable per the user's criterion;
- (c) **light ghost** — a mode below the splitting threshold
      that matches no observed particle.  These are the only
      problems Track 1 must eliminate.

If light ghosts are found, Track 1 then attempts to eliminate
them by moving `(ε_p, s_p)` alone.

**Phases.**

### Phase 1 — Audit at baseline

Enumerate in-scope modes up to a bounded energy (initially
2 GeV, extensible).  Classify each.  Output the ordered
per-scope ghost list.  If empty, Phase 2/3 short-circuit to
"no action required" and Track 21's pion shift becomes a
free-floating optimization (pool items **c**–**f**).

### Phase 2 — `(ε_p, s_p)` adjustment to eliminate light ghosts

For each light ghost identified in Phase 1, characterize the
direction in `(ε_p, s_p)` that either:
- relocates the ghost onto an observed particle (mirrors R53's
  "(1, 1) → muon" mechanism on the e-sheet), or
- lifts the ghost above its splitting threshold (reclassifying
  it as split-dominated).

Sweep a targeted `(ε_p, s_p)` region — initially a grid around
baseline, refined toward any region that simultaneously
addresses all ghosts.  Track 21's already-identified sweet
spot `(ε_p ≈ 0.15, s_p ≈ 0.05)` is a natural candidate to
evaluate first.

### Phase 3 — Observed-particle preservation check

At any candidate `(ε_p, s_p)` from Phase 2, verify that no
observed particle is degraded below model-F's current match.
The proton mass is always preserved (L_ring_p re-derives), but
the neutron and compound-mode matches are not guaranteed.  If
observed particles are degraded, Phase 2's direction is
incompatible — flag for pool items that bring additional
variables into play.

**Tactics.**

- Reuse R60 T20 Phase D enumeration (Z₃ + charge + composite α
  + spin filters), restricted to in-scope tuples.
- New primitive `splitting_threshold(mode, metric)` returns the
  minimum `sum(E_obs_i) + V_separation` over decompositions
  into observed lighter particles, with V_separation from the
  R56/R57 routing cost model.
- Rebuild metric (σ_ra auto-updates) at each `(ε_p, s_p)`
  candidate; re-run the audit.
- One script: `track1_proton_ghost_audit.py` with Phase 1/2/3
  as functions sharing the enumeration engine.
- Outputs: markdown + CSV ghost-list per phase.

**Acceptance.**

- Phase 1 produces an unambiguous classification of every
  in-scope mode below 2 GeV at baseline.
- If Phase 1 finds no light ghosts: Track 1 closes with
  "proton-sheet clean at baseline; Track 21's shift is a
  free optimization".
- If Phase 1 finds light ghosts AND Phase 2 finds a `(ε_p, s_p)`
  that eliminates all of them while Phase 3 preserves observed
  particles: Track 1 closes with a recommended parameter
  shift, and pool items proceed at the new baseline.
- If Phase 1 finds light ghosts AND no `(ε_p, s_p)` eliminates
  them cleanly in Phase 2/3: Track 1 closes with a precise
  obstacle report, and pool items **h** (cross-sheet) or other
  multi-variable options come into scope.

**What Track 1 is NOT.**

- Not an e-sheet audit.  R53 already did it.  (Pool item **l**
  can re-validate if needed.)
- Not a ν-sheet audit.  The (1, 0) item is pool **k**.
- Not an observable-anchored sweep.  Uses only the known
  particle list and R56/R57 routing cost.
- Not multi-variable.  Only `(ε_p, s_p)` is adjusted.  If
  fixing the proton sheet requires other knobs to move,
  Track 1 reports the obstacle and stops.

---

## Track 2 — Pure p-sheet viable-region map

**Goal.**  Characterize the full range of `(ε_p, s_p)` values
that preserve the pure p-sheet cleanness Track 1 established at
baseline.  Produce a 2D map showing which points are viable
(no sub-observed ghosts + observed matches preserved) and which
are not.

**Motivation.**  Track 1 tested only two `(ε_p, s_p)` points
(baseline and Track 21's extreme).  The analytical bound
`μ(3, 6) ≤ 8.09` separates them cleanly but does not tell us:

- How large the viable region actually is.
- Whether the 7 baseline observed-particle matches survive
  throughout the region, or only at baseline.
- Whether any point in the region offers a natural improvement
  on open issues (e.g., pion matches, nuclear scaling) without
  introducing ghosts elsewhere.

**Strategy.**  Sweep `(ε_p, s_p)` over a 2D grid; at each
point, rebuild the metric (σ_ra auto-updates), calibrate
L_ring_p from the (3, 6) proton, and run Track 1's audit.
Output a viability map and a shortlist of candidates.

**Tactics.**

1. **Grid definition.**  ε_p ∈ [0.2, 2.0] with log-ish spacing;
   s_p ∈ [0.0, 0.5] linear.  Roughly 15 × 11 = 165 points.
   Extensible on boundaries if the viable region extends
   further.
2. **Per-point evaluation.**  Reuse Track 1's
   `enumerate_pure_p_modes` and `classify_z3_free_mode`.  Add:
   - Sub-observed ghost count (primary viability gate).
   - Number of the 7 baseline-matched observed particles that
     remain within their threshold at this point.
   - μ(3, 6) and L_ring_p for reference.
3. **Output.**
   - CSV grid with per-point metrics.
   - Viability map (pass/fail on ghost criterion).
   - Shortlist of "clean + all 7 matches preserved" candidates.
   - If any candidate has a better pion match than baseline's
     10.37%, flag it.

**Acceptance.**

- Viable region clearly delineated (not just "baseline is
  viable").
- Baseline falls inside the viable region with measurable
  slack in all directions.
- Track 21's extreme falls clearly outside.
- Shortlist of candidate points for observable-anchored
  tracks (pool items b–g).

**What Track 2 does NOT do.**

- Does not test observables beyond the 7 baseline matches.
  Observable-anchored sweeps are pool item **c** onward.
- Does not touch `ε_ν` or cross-sheet σ.  Still proton-only.
- Does not re-run the multi-sheet inventory (14 of 16 from
  R60 T19).  That full inventory check is a later track if
  Track 2's candidates look interesting.

**Payoff.**

- Knowing the boundary of viable `(ε_p, s_p)` shapes every
  downstream decision about parameter movement.
- The shortlist of viable candidates feeds directly into
  pool items b–g (observable-anchored sweeps).
- If any candidate naturally improves the pion match without
  breaking anything else, that's a strong recommendation
  path.

---

## Track 4 — E-sheet parallel audit (validation for multi-sheet searches)

**Goal.**  Apply Tracks 1–3b's methodology to the electron sheet,
so the e-sheet is validated to the same level of precision the
p-sheet just received.  This is a **prerequisite for any
multi-sheet search** (pool items c, d, e): trusting a multi-sheet
inventory requires knowing each sheet's own mode ladder is clean.

**Motivation.**  The e-sheet's current `(ε_e, s_e) =
(397.074, 2.004200)` comes from R53 Solution D — an **algebraic
constraint solve** (two equations `m_μ/m_e ≈ 207, m_τ/m_e ≈ 3477`
in two unknowns), not a sweep + fitness analysis.  R33's earlier
ghost census preceded the σ_ra + per-sheet Dirac–Kähler
architecture.  R63 Track 1 deliberately **skipped** the e-sheet on
the assumption "R53 already handled it."  Track 3b's dramatic
p-sheet result (fitness 4.95 vs baseline's 4.04, near-exact π⁰
match at a completely different geometry than the historical
baseline) raises a legitimate doubt: the same discipline applied
to the e-sheet may reveal similar surprises.

**Scope — strictly e-sheet.**  Only `(ε_e, s_e)` is swept in
Track 4.  Cross-sheet σ, ν-sheet geometry, and p-sheet
parameters are held fixed at their current model-F values.  If
the e-sheet needs other variables, that is noted as obstacle
(parallel to Track 1's p-sheet result) rather than pursued in
Track 4.

**Target particles and thresholds.**  All three charged leptons
are narrow; no broad-resonance case like Δ⁺.  Under width-
weighted thresholds (floor 2%):

| Particle | τ | Γ / m | Threshold |
|:--------:|:--:|:-----:|:---------:|
| electron | stable | 0 | 2.0% |
| muon | 2.2 μs | 3×10⁻¹⁹ | 2.0% (floor) |
| tau | 2.9×10⁻¹³ s | 2×10⁻¹⁴ | 2.0% (floor) |

All three are essentially exact-match targets.

### Phase A — Pure e-sheet ghost audit at baseline

Enumerate pure e-sheet modes `(n_et, n_er, 0, 0, 0, 0)` up to a
bounded energy cap (initially 5 GeV to cover tau at 1777 MeV
with headroom).  For each, compute:

- Effective charge `Q = −n_et` (pure e-sheet, no p-sheet
  contribution).
- Mass via the p-sheet-analogous formula with L_ring_e
  calibrated to the electron at `(1, 2)`.
- Classification: observed, split-dominated, or sub-observed
  ghost.

**Explicit questions for Phase A:**

1. Are there sub-observed ghosts below the electron (Q = ±1,
   spin-½, mass < m_e)?  There shouldn't be — the electron is
   supposed to be the lightest charged mode — but the R33-era
   selection rules (n_tube = ±1 filter) are worth re-verifying
   under the current architecture.
2. Are there `Q = 0` spin-½ modes on the e-sheet with no
   observed counterpart?  E.g., `(n_et = 0, n_er > 0)` modes
   — these would have the quantum numbers of sub-proton
   spin-½ neutrals.  If the architecture doesn't implicitly
   suppress them, they're a problem the p-sheet audit didn't
   expose.
3. Are there `|Q| ≥ 2` modes at low mass with no observed
   counterpart?  Parallel to the "|Q| = 4" ghosts my broader
   Track 1 draft found before narrowing scope.
4. Does tau actually appear as a low-order `(1, n)` mode at
   the R53 values, or is it high-n (R53 notes n ≈ 3478 is
   needed)?  If the latter, the tau match is a distant
   high-winding assignment — worth noting.

### Phase B — (ε_e, s_e) viable-region map

Sweep `(ε_e, s_e)` around R53 Solution D.  Grid design is
non-trivial because the e-sheet lives in extreme geometry:

- ε_e ≈ 397 is very large; small ε_e changes produce huge
  μ(1, 2) changes.  Use **log-spaced** ε_e over a ±30% range,
  maybe ε_e ∈ [250, 600] at log-spaced steps.
- s_e ≈ 2.004 is near the shear-resonance line `s_e = n_r/n_t`
  for the electron's (1, 2).  Small s_e changes produce
  significant detuning changes.  Use fine linear spacing,
  maybe s_e ∈ [1.98, 2.03] at step 0.001 (50 values).

That's roughly 30 × 50 = 1500 grid points at this resolution.
Expand if the viable region extends beyond.

Compute continuous width-weighted fitness against electron,
muon, tau.  Per the p-sheet experience, baseline is likely a
sharp local maximum (because R53 solved the two mass ratios
exactly) but the **shape of the peak** and any secondary
features are what we want to see.

### Phase C — Thresholds and interpretation

If baseline is a sharp peak:  
→ R53 Solution D validated; confidence for multi-sheet searches.

If baseline is in a ridge with comparable neighbors:  
→ Multiple viable e-sheet geometries exist; multi-sheet
searches should pick among them based on additional criteria.

If baseline is NOT the local optimum under width-weighted
scoring:  
→ Same finding as Track 3b on the p-sheet: the algebraic
pinning may be hiding a better fit.  Would require serious
reconsideration before committing to multi-sheet work.

### Deliverables

- `scripts/track4_e_sheet_audit.py` — Phase A ghost audit
- `scripts/track4b_e_sheet_sweep.py` — Phase B sweep + heat maps
- `outputs/track4_*.png` — ghost map, fitness map, difference
  map (vs baseline scoring)
- `findings-4.md` — full write-up

### Acceptance

- Phase A either validates the e-sheet is clean or produces a
  ranked ghost list.
- Phase B produces a viable-region map of (ε_e, s_e) with
  baseline marked and peaks identified.
- Phase C makes a clean recommendation about whether R53
  Solution D is robust under continuous-fitness scoring.

### What Track 4 does NOT do

- Does not touch cross-sheet σ, ν-sheet, or p-sheet values.
- Does not re-derive R53's mass-ratio constraint — it treats
  the lepton masses as targets and sees whether R53's values
  are optimal under the sweep.
- Does not re-open the question of whether |n_et| > 1 should
  be allowed; the sub-observed ghost criterion will flag any
  problem modes, and suppression is an architecture question
  for a separate track.

### Time estimate

Phase A: ~30 seconds (enumeration + classification at one point).
Phase B: ~1–2 minutes (1500-point grid, same inner loop as
Track 3).  Phase C: analysis only.

Approximate total: a few minutes of compute plus writeup.

---

## Track 5 — E-sheet fitness landscape under Q132

**Goal.**  Re-render Track 4's `(ε_e, s_e)` sweep using the
Q132 promotion-chain principle's updated ghost criterion.
Under Track 4's old rule every grid point was ghost-masked;
under Q132 the mask shrinks dramatically and the underlying
lepton-fitness topography (which has been there all along)
becomes visible.

**Motivation.**  Track 4's fitness heat map was almost entirely
hatched because the strict criterion flagged (0, n_r) and
(1, 0) modes as ghosts.  Q132 reinterprets these as **valid
neutral massive particles** (dark-matter / sterile-neutrino
candidates), not ghosts.  Only `|n_et| ≥ 2` multi-event modes
remain as true ghosts on the e-sheet — and these are filtered
structurally.  The fitness landscape that was hidden is the
one we actually care about.

**Scope — strictly e-sheet re-classification.**  Track 5
reuses Track 4's grid, metric builders, and mode enumeration;
only the `classify_z3_free_mode` function changes to match
Q132.  No new parameters are swept.

**Phase A — Q132 re-classification.**  Mode classification
refactored to reflect Q132's typology:

| Pattern | Old classification (Track 4) | New classification (Q132) |
|:-------:|:-----------------------------|:--------------------------|
| (0, n_r ≠ 0), Q=0 | ghost-sub-observed | **valid neutral particle (dark candidate)** |
| (1, 0), Q≠0 | ghost-sub-observed | **valid neutral particle (tube-only, self-mass)** |
| (\|n_et\| ≥ 2, any n_er) | ghost-no-decay | **still ghost** (multi-event forbidden) |
| (1, n_r ≠ 0), Q≠0 | observed/split | unchanged |

**Phase B — updated fitness heat map.**  Re-score with the new
ghost mask.  Expected result: the 2296-point grid is mostly
clean, with ghosts confined to a thin region of the (ε_e, s_e)
plane where low-n_er modes happen to produce sub-electron
charged candidates.  The lepton-fit topography around R53
Solution D becomes visible.

**Phase C — interpretation.**  Identify:

- Where the lepton-fit peak actually is under clean
  classification (may or may not be exactly R53 Solution D).
- The predicted dark-mode spectrum at the peak: what neutral
  ring-only and tube-only modes are predicted, at what masses.
  These become R42-class dark-matter candidates; the sweep
  should report them as outputs, not just ignore them.
- How wide the "comfortable" (ε_e, s_e) range is once ghost
  mask shrinks — likely much wider than R53's algebraic solve
  would suggest.

**Deliverables.**

- `scripts/track5_e_sheet_q132.py` — refactored classification
  + sweep + heat map generation.
- `outputs/track5_fitness_q132.png` — heat map under new rules.
- `outputs/track5_dark_modes.csv` — catalog of predicted
  neutral modes per (ε_e, s_e) shortlist candidate.
- `findings-5.md` — Phase A/B/C writeup.

**Acceptance.**

- Heat map shows an interpretable fitness topography (not
  ghost-dominated).
- R53 Solution D assessed against the new topography — is it
  a peak, a ridge, or off-peak?
- Dark-mode catalog produced for any candidate (ε_e, s_e)
  points that deserve attention.

**Time estimate.**  Re-using Track 4 infrastructure: ~5
minutes total (enumeration is already fast; only the
classifier changes).

---

## Track 6 — Joint Q132 compound-mode audit across all three sheets

**Goal.**  Check that the full observed inventory of particles
is compatible with per-sheet Q132 (the promotion-chain rule),
and find the combinations of sheet ratios that give the best
joint fit to the inventory under that rule.  This track
supersedes the original pool item **n** (p-sheet-only re-
render) and pool item **p** (joint compound search) by
merging them: Q132 changes how compound-mode assignments are
evaluated across sheets, so p-sheet re-evaluation and compound
search are naturally the same task.

**Why this is one track and not two.**  Q132 is a per-sheet
rule: each sheet's winding pair `(n_t, n_r)` must fall into
one of the allowed cells (ring-only neutral, tube-only
neutral, charged, or null).  A compound-mode particle assigns
a `(n_t, n_r)` pair to each of three sheets.  Checking Q132
compatibility is therefore inherently compound — you can't
evaluate a particle's legality one sheet at a time in
isolation.

### Ratios: status going in

All ratios carry forward **as ranges**, pinned only where
prior analysis forced pinning.  Prior candidate points (R53
Solution D on the e-sheet; Track 3b's (0.80, 0.05) on the
p-sheet) are data points to include in the search, not
coordinates to impose.

| Sheet | Variable | Status entering Track 6 | Source |
|:---:|:---|:---|:---|
| e | `s_e` | **Narrow-pinned** at 2.0 ± ~0.005 | Track 5 showed fitness collapses outside the shear-resonance ridge |
| e | `ε_e` | **Open** across ~280–460 | Track 5 found a wide ridge with multiple local peaks |
| p | `s_p` | **Open** | Track 3b's peak at 0.05 was under strict ghost rules; Q132 loosens the landscape and the peak may move |
| p | `ε_p` | **Open** | same reasoning; Track 3b's 0.80 is a candidate, not a pin |
| ν | `s_ν` | Previously pinned at 0.022 from Δm² ratio 33.6 | R61 pinning; revisit only if Phase 6B shows sensitivity |
| ν | `ε_ν` | **Open** | never constrained by fitness analysis |

### Baryon reinterpretation under v2

Q132 v2 replaces v1's "|n_t| ≤ 1 or forbidden" rule with a
gcd-based decomposition: `(n_t, n_r)` is k copies of a primitive
`(p_t, p_r)` with `gcd = 1`, and the primitive's type determines
the mode's classification.  A baryon with p-sheet `(n_pt, n_pr)
= (3, 6)` decomposes as 3 × primitive `(1, 2)` — three quark-like
strands bound by Z₃ into one color singlet.  The e-sheet side
inherits the same 3-fold structure when the tuple assigns
`(n_et, n_er)` with `gcd = 3`.

v2 distinguishes two cases that v1 conflated:
- **gcd > 1 with primitive `|p_t| = 1`:** k copies of a bright
  charged primitive.  Bound by Z₃ on the p-sheet, unbound on
  the e-sheet (hence free-particle scattering).
- **gcd = 1 with `|p_t| > 1`:** a single dark primitive.  Phase
  cancellation (ω-sum) gives zero charge; mass-only contribution.

### Phases

- **6a** — per-sheet v2 classification and compound charge check
  against R60 T19's inventory.
- **6b** — constrained tuple re-derivation for any particle whose
  R60 T19 tuple gives the wrong compound charge under v2.
- **6b-pion** — focused characterization of what v2 predicts for
  the pion position at model-F baseline.
- **6c** — marginal ratio scans per sheet, width-weighted against
  the resulting v2-certified tuple set.
- **6d, 6e** — (optional) joint ratio search and dark-mode
  compound catalog; see below.

Results live in [findings-6.md](findings-6.md).

### Deliverables

- `scripts/track6_phase6a_compatibility.py`,
  `scripts/track6_phase6b_rederivation.py`,
  `scripts/track6_phase6b_pion.py`,
  `scripts/track6_phase6c_marginal_scans.py`.
- `outputs/track6_phase6a_v2.csv` — Phase 6a classification.
- `outputs/track6_phase6b_rederivation.csv` — Phase 6b candidates.
- `outputs/track6_phase6b_pion_candidates.csv` — 6b-pion output.
- `outputs/track6_phase6c_*` — 6c scans and peaks.
- `outputs/track6_dark_catalog.csv` — Phase 6e predictions
  per shortlisted candidate (pending).

### What Track 6 does NOT do

- Does not commit to a single ratio combination.
- Does not formally derive Q132 v2 from GRID axioms — that is
  an R62 target.
- Does not touch cross-sheet σ values (pool item **h**) or
  anchoring-mode choice (pool item **i**).
- Does not create `models/model-G.md` — per the R63 discipline,
  a model letter change is deferred until R63 closes with a
  demonstrable improvement over model-F across multiple axes.

---

## Track 7 — Compound-mode vs. spatial separation audit

**Goal.**  Test whether MaSt's compound-mode description of
nuclei holds across the stable chain, and — if it holds — whether
it naturally predicts the Fe binding peak and the observed
stability boundary as emergent features of the framework.

**Motivation.**  R63's inventory work has relied on the
compound-mode hypothesis: a nucleus of (A, Z) is one particle
with winding `(1−Z, 0, 0, 0, 3A, 6A)` rather than A spatially-
separated nucleons.  R60 T19 Phase 2 verified this at ~1%
accuracy for d, ⁴He, ¹²C, and ⁵⁶Fe but never extended above Fe
and never compared directly to the spatial-separation
alternative.  Before tightening ε or cross-sheet σ values
further, R63 should verify the structural hypothesis: does
compound-mode hold all the way up, or does it break at some A —
and if so, does it break exactly where observation says nuclei
stop being stable?

This is a **structural question, not a parametric one**.  In
MaSt, the compound-mode mass scales linearly in A
(`μ(3A, 6A) = 3A·μ(1, 2)`), so changes to ε_p or s_p shift every
nucleus by the same fraction and leave the *relative* pattern —
which is what Track 7 tests — invariant at leading order.  No
parameter pinning is needed or produced.

### Parameters

Track 7 runs against the **g-candidate parameter set** R63 has
been developing: the sheet shears and aspect ratios sit at the
values that emerged from Track 6c's joint-fitness peak
(numerically the same as model-F's, but treated as *working*
values, not pins).  Free variables remain free.  Where the
answer is known to be ratio-invariant at leading order — and
it is, for Track 7's comparisons — variables are held at their
current working values for compute convenience, not as
commitments.

`s_ν` and `ε_ν` are held at R61 central values on the basis
that Track 6c demonstrated the ν-sheet is passive for the
hadronic inventory.

### Phase 7a — H → Fe

Compute compound-mode predicted mass for ~15 stable nuclei
spanning Z=1 to Z=26 using the A-scaling tuple.  Compare to
observed mass; tabulate miss vs. binding energy.  R60 T19's
four data points showed miss correlating with total binding,
growing slowly with A; 7a extends this to the full light chain
so the trend is visible at resolution.

**Acceptance.**  A coherent miss-vs-binding curve across the
light chain, establishing that compound mode tracks observation
up through the Fe peak.

### Phase 7b — Fe → hypothetical element 137

Extend the same calculation through the stable-heavy chain up
to ²⁰⁸Pb (Z=82), then continue into the trans-uranium regime
and beyond — up to the hypothetical element 137 as a far-field
probe.  Questions to answer:

- Does the compound-mode miss stay within the binding-energy
  envelope all the way up, or does it start to diverge?
- If it diverges, where?  Does the divergence coincide with the
  observed end of primordial stability (~Bi, Z=83)?
- What does MaSt predict for elements that cannot be stably
  assembled in nature?

**Acceptance.**  The miss-vs-binding curve extends past Fe into
the known-stable-heavy regime and into the hypothetical.  Any
divergence is characterized by location and magnitude.

### Phase 7c — Compound-vs-separated crossover

Using the 7b miss pattern, estimate the A at which MaSt's
compound-mode cost exceeds the cost of spatially-separated
nucleons plus the observed nuclear binding.  Compare the
crossover location to the observed Fe peak of binding-per-
nucleon and to the observed stability boundary.

**Possible outcomes.**

- Crossover at Fe → MaSt naturally predicts the Fe peak as the
  transition between "compact-dimension stacking is favored" and
  "spatial separation is favored."  Major structural result.
- Crossover at Bi (Z=83) → MaSt predicts the observed primordial
  stability boundary.  Also major.
- Crossover elsewhere → cleanly identifies where MaSt differs
  from observation and what the missing physics is.
- No clean crossover → the compound-mode picture holds throughout
  the computed range; A-scaling is structurally confirmed at all
  scales, and the Fe peak is produced by something else (a
  candidate for follow-up).

**Acceptance.**  A compound-vs-separated energy comparison
produced across the computed A range with a specific crossover
point (or documented absence thereof), and its relationship to
the Fe peak and the stability boundary characterized.

### Deliverables

- `scripts/track7_compound_vs_separated.py` — compound-mode
  mass calculation for the Z=1 → 137 chain plus the separated-
  energy comparison.
- `outputs/track7_mass_chain.csv` — per-nucleus prediction and
  miss data.
- `outputs/track7_binding_vs_miss.png` — miss-vs-binding curve.
- `outputs/track7_crossover.png` — compound vs. separated energy
  comparison with crossover point.
- `findings-7.md` — writeup.

### What Track 7 does NOT do

- Does not pin ε_p, s_p, or any other ratio.  The ratio-invariant
  nature of the comparison is the point.
- Does not modify the v2 rule set.
- Does not attempt a precision fit.  Pool item **q** (32-nucleus
  precision survey) is the follow-up if 7 validates the picture.
- Does not create `models/model-G.md`.

### Time estimate

Each nucleus is one metric evaluation.  30–40 nuclei plus
plotting: under a minute of compute.  The writeup is the
larger effort.

---

## Track 8 — Decay-conservation audit and additive tuple refinement

**Goal.**  Adopt winding conservation across decays as the core
principle for composite-particle tuple assignment, substitute
the β-decay-derived neutron tuple for R60 T19's mass-fitted
choice, apply additive composition to nuclei, and audit the
rest of the particle zoo against the same principle.

**Motivation.**  Earlier-framed Track 8 (bound-state tuple
search) was withdrawn.  It was attempting to discover new
quantum numbers for each stable nucleus by brute-force tuple
search — but the nucleus already IS a proton and a neutron, not
a particle with unknown quantum numbers.  The right question
is: what are the nucleon tuples, and how do they combine when
nucleons sit near each other?

A cleaner principle emerged from discussion: **winding
conservation across decays**.  β-decay is `n → p + e⁻ + ν̄`;
if MaSt windings are conserved, then `n_tuple = p_tuple + e_tuple
+ ν̄_tuple = (1, 2, 1, 1, 3, 6)`.  This tuple:

- matches observed neutron mass to the same accuracy as the
  R60 T19-picked `(−3, −6, 1, −6, −3, −6)` (0.14% miss, both);
- has a clean physical reading (neutron as a bound combination
  of proton + electron + antineutrino);
- shares p-sheet windings with the proton, so the two can be
  *added* to give composite-nucleus tuples without cancellation
  nonsense.

Applying additive composition to nuclei (Z copies of proton +
(A−Z) copies of the new neutron):

| Nucleus | A-scaling miss | Additive miss |
|---|:-:|:-:|
| ³He | +0.505% | **+0.229%** |
| ⁴He | +0.846% | **+0.690%** |
| ¹²C | +1.189% | **+0.755%** |
| ⁴⁰Ca | +1.413% | **+0.850%** |
| ⁵⁶Fe | +1.369% | **+0.871%** |

Additive beats A-scaling across the chain by ~0.4 percentage
points.  The residual (~0.9% at Fe) is cleanly the observed
binding energy, giving a sharp diagnostic for the missing
binding mechanism.

This is the direction Track 8 pursues.

### Note on photons and other massless products

Some decays emit photons (π⁰ → γγ, Σ⁰ → Λγ, η → γγ, etc.).
Photons in MaSt are level-1 promotions — energy, but no
compact-dimension windings in the sense we're using.  So
photons **carry no windings to the additive sum**; they carry
away the decay's kinetic energy (Q-value) but leave winding
conservation intact among the massive particles.

Similarly, neutrinos have windings (as ν₁, ν₂, ν₃) but have
tiny masses — their windings matter for the tuple sum but
their mass contribution is negligible in the mass arithmetic.

### Phase 8a — Neutron substitution and nuclear verification

Substitute the β-decay neutron tuple `(1, 2, 1, 1, 3, 6)` into
the g-candidate inventory.  Re-run the Phase 6a charge check
and the Track 7a nuclear mass check under additive composition.
Verify:

1. The neutron still passes v2 charge arithmetic (as a
   fundamental-mode check).
2. The nuclear chain under additive composition reproduces the
   improvement shown in the quick-verify dialogue: better miss
   across the H → Fe chain than A-scaling gave.
3. Compound-charge consistency for nuclei: we adopt the
   **ingredient-sum** rule (nucleus charge = Z·Q_p + (A−Z)·Q_n
   = Z·(+1) + (A−Z)·0 = Z) rather than re-applying v2's
   per-sheet primitive rule to the summed compound tuple.
   Clarify this extension of v2 in the findings.

**Acceptance.**  Neutron charge still 0 under v2 at the
fundamental level; every H-to-Fe nucleus's mass under additive
composition is at or better than its A-scaling prediction.

### Phase 8b — Hadron-zoo decay audit

For each decay listed below, compute
`Δ = parent_tuple − Σ daughter_tuples`
and `mass_residual = parent_mass_from_metric − Σ daughter_masses`,
under current g-candidate tuples.  Photons carry no winding and
no mass contribution to the residual.  Report:

- Whether Δ = 0 (winding conservation holds for current tuples).
- The mass residual, which (when Δ = 0) is MaSt's estimate of
  the decay Q-value.
- Comparison to observed Q-values.

Candidate decays:

| Parent | Products | Type |
|:---|:---|:---|
| n | p + e⁻ + ν̄_e | β decay (canonical) |
| Λ | p + π⁻ | weak, 64% |
| Λ | n + π⁰ | weak, 36% |
| Σ⁻ | n + π⁻ | weak |
| Σ⁺ | p + π⁰ | weak |
| Σ⁺ | n + π⁺ | weak |
| Ξ⁻ | Λ + π⁻ | weak |
| Ξ⁰ | Λ + π⁰ | weak |
| ρ⁰ | π⁺ + π⁻ | strong |
| K_S⁰ | π⁺ + π⁻ | weak |
| K⁻ | μ⁻ + ν̄_μ | weak (leptonic) |
| π⁻ | μ⁻ + ν̄_μ | weak (leptonic) |
| π⁰ | γ + γ | EM (photon-only products) |
| η | γ + γ | EM (photon-only products) |

Special cases:

- **Photon-only products** (π⁰ → γγ, η → γγ): parent's winding
  sum should be zero if winding conservation holds and photons
  carry no windings.  If the parent tuple is non-trivial,
  either the tuple violates the principle or photons carry some
  winding we haven't accounted for.  Both possibilities are
  interesting.
- **Neutrino flavor mixing**: ν_e, ν_μ, ν_τ (flavor
  eigenstates) are superpositions of ν₁, ν₂, ν₃ (mass
  eigenstates).  A decay emits a flavor eigenstate; the tuple
  sum should reflect whichever mass-eigenstate basis we've
  adopted.  Handle as a bookkeeping caveat, not a show-stopper.
- **Weak decays with flavor change**: at the quark level, β
  decay involves d → u via W.  In MaSt with nucleon-level
  tuples, whether d→u breaks winding conservation is an open
  question.  The audit will expose the pattern.

**Acceptance.**  For each decay, a clear verdict: current
tuples are winding-conservation-consistent (Δ = 0) or not
(Δ ≠ 0, identifying which tuples are suspect).

### Phase 8c — Tuple refinement from decay constraints

For each decay where Δ ≠ 0 under current tuples, use the
constraint to propose a revised tuple for one of the particles
involved, prioritizing:

1. Conservation consistency across all that particle's decays.
2. Mass match to observation (within width-weighted threshold).
3. v2 charge arithmetic at the fundamental level.
4. Physical interpretability (clean composition mapping).

**Acceptance.**  A revised tuple set that maximizes
decay-conservation consistency while preserving Track 5 and
Track 6 mass-match quality.  Any irreducible inconsistencies
flagged as framework-level open questions (likely signatures
of flavor-changing weak processes).

### Phase 8d — Synthesis

- If all (or nearly all) decays pass winding conservation under
  a consistent tuple set: MaSt's windings are conserved
  observables, and the tuple set is structurally principled.
- If a subset systematically fails: identifies which decay
  types MaSt's framework cannot yet accommodate (most likely
  weak flavor-change processes), pointing at the specific
  extension needed.
- Either way: the Q-value predictions per decay become a new
  set of observables — MaSt predicting experimental quantities
  not yet used in the fit.

### Deliverables

- `scripts/track8_phase8a_neutron_and_nuclei.py` — substitutes
  neutron tuple, re-runs charge check and nuclear chain.
- `scripts/track8_phase8b_decay_audit.py` — winding and mass
  audit over the zoo decays.
- `scripts/track8_phase8c_refinement.py` — tuple revision under
  decay constraints.
- `outputs/track8_*.csv` / `*.png` — per-particle and
  per-decay results.
- `findings-8.md` — writeup.

### What Track 8 does NOT do

- Does not pin ε_p, s_p, or any other ratio.  The g-candidate
  working parameters are held constant; Track 8 is combinatoric
  over integer windings.
- Does not attempt to model S-space configuration energies.
  That remains a framework-extension question for a successor
  study.
- Does not resolve the pion mass (10% miss per Track 6b-pion);
  the residual is the expected ephemeral-echo signature.
- Does not create `models/model-G.md`.

### Time estimate

Phase 8a: minutes (substitution + re-run of existing scripts).
Phase 8b: minutes to hours (combinatoric checks over ~14
decays).  Phase 8c: the real work, since tuple revisions may
be interlocked.  Phase 8d: analysis + writeup.

### Outcome

Track 8 closed with **Phases 8a and 8b complete in R63**; 8c and
8d promoted to successor-study scope.  See
[findings-8.md](findings-8.md) for results and the
close-out section FR-1 … FR-5 for the directions for future
refinement.

---

## Track 9 — Nuclear binding mechanism in Ma

**Working premise.**  Forces in S arise from lowest-energy
states in Ma.  The nuclear "strong force" — what makes bound
nuclei lower-energy than their separated nucleons — must be
produced by some Ma mechanism.  Track 9 investigates which one.

**The sharp target.**  Under Phase 8a's additive composition,
the predicted deuteron mass is 1876.54 MeV.  Observed is
1875.61 MeV — 2.2 MeV lighter.  **For the bound neutron inside
the deuteron to be stable against β decay** (as observed),
m(d) < 2m_p + m_e = 1877.6 MeV is required.  The additive
prediction 1876.54 MeV clears this by only ~1 MeV, and without
the observed 2.2 MeV binding, MaSt is on the wrong side of the
β-stability threshold.  Binding in Ma is **structurally
required**, not a refinement to pursue for accuracy.  Track 9
must find the mechanism or conclude the framework needs
extension.

### Phase 9a — Cross-shear dressing (EXECUTED; falsified as candidate)

Tested whether turning on cross-sheet σ entries in the 11D
metric produces nuclear binding.  Method: scan all ten
cross-shear placements (e↔p, ν↔p, e↔ν tube/ring pairs) at five
magnitudes each within the signature-preserving range; compute
`B = Σ E(nucleons) − E(compound)` for the additive-composition
tuple at each point.

**Result**: binding stays at `~10⁻⁴ MeV` (numerical noise)
regardless of placement or magnitude.  Linear cross-shear
dressing of additive tuples does not produce binding.

**Scope of the falsification.**  The proof rests on two
assumptions: (1) additive composition is the correct compound
tuple; (2) cross-shear dressing is a linear rank-1 perturbation.
Both are *specific to the test*, not theorems.  Mechanisms that
violate either assumption remain viable — see Phase 9b onward.

See [findings-9.md](findings-9.md) Phase 9a for details.

### Phase 9b — Non-additive tuple search for the deuteron (NEXT)

**Premise.**  Phase 9a's cancellation exploits the assumption
that the bound nucleus has the additive-composition tuple.  If
a different Ma-mode (different windings, same observable
content) has lower mass, *that* mode is the bound state and
the additive tuple is the "reference" separated configuration.

**Sharp target.**  Deuteron: observed mass 1875.61 MeV;
additive prediction 1876.54 MeV; gap 2.2 MeV (= observed
binding) = what Phase 9b needs to find by identifying a
v2-compatible tuple with mass ≤ observed.

**Method.**  Brute-force scan the Ma tuple lattice within a
moderate envelope around the additive deuteron tuple
`(1, 2, −1, −1, 6, 12)`.  For each candidate:

- Z₃ constraint on p-sheet: `n_pt` multiple of 3.
- Compute mass via g-candidate metric.
- Check ingredient-sum charge consistency with Q(deuteron) = +1.
- Rank by mass closeness to observed 1875.61 MeV and by
  structural plausibility (how close to the additive tuple).

If the search finds a v2-compatible tuple at or below
1875.61 MeV, that's the deuteron bound state and binding is in
Ma via non-additive tuple selection.  If the search returns
only the additive tuple (or heavier), Path A (non-additive
bound tuples) is falsified for the deuteron and we proceed to
Phase 9c.

### Phase 9c — Mass-formula validity at high n_pt (EXECUTED; falsified)

Path B audit.  Derivation 4 of R62 gives MaSt's mass formula
`μ² = (n_t/ε)² + (n_r − s·n_t)²` as a closed-form consequence
of the photon-on-T² geometry; no n-dependent approximation is
used in the derivation.  Numerical verification: `μ(kn_t, kn_r)
= k·μ(n_t, n_r)` holds to double-precision (1.5×10⁻¹⁶ relative)
across `k ∈ {1 … 200}`.  Full 11D metric at σ_cross = 0 gives
compound-vs-separated agreement to ~10⁻³ MeV through ²⁰⁸Pb —
orders of magnitude short of observed binding.

See [findings-9.md §Phase 9c](findings-9.md) for details.

### Phase 9d — Z₃ multi-strand phase coherence at k > 3

**Final remaining Ma-internal candidate.**  If 9a, 9b, 9c all
falsify their respective mechanisms, Phase 9d is the last
Ma-level hypothesis.  The reviewer frames it precisely: current
MaSt treats `(6, 12)` via `μ(6, 12) = 2·μ(3, 6)` irrespective
of whether the six strands are arranged as two independent Z₃
triplets or as a coherent Z₆ hexagon.  **Phase 9b's tuple
search cannot distinguish these** — they have the same
windings.  If coherent arrangements have lower mass, that's
nuclear binding in Ma.

#### Origin of Z₃ on the p-sheet (R60 T16)

Z₃ confinement on the p-sheet was derived in R60 Track 16 from
a **density-fluctuation-cancellation argument** applied to a
single (1, 2) mode under the real-field (spin 7b) picture:

- Real-field charge density ρ_Q = φ² on a single (1, 2) mode has
  a 2ω Fourier harmonic (time-dependent density fluctuation).
- Three copies of the mode at 120°-offset internal phases —
  a Z₃-symmetric arrangement — cancel the 2ω harmonic exactly.
- Therefore free single quark-like (1, 2) modes are forbidden;
  minimum stable composite is `n_pt = 3` with three Z₃-coherent
  strands.

**The Z₃ rule is not a postulate — it emerges from density
cancellation.**  This is the handle Phase 9d must exploit.

#### Extending to k = 3A: 2×Z₃ vs Z₆ for A = 2

For the deuteron (A = 2, k = 6), six strands must arrange
themselves to keep density cancellation.  Two candidate
arrangements:

- **2 × Z₃** — two independent triplets, each internally
  Z₃-coherent, with arbitrary relative phase between triplets.
- **Z₆ hexagon** — six strands at 60°-offset phases
  `(0, 60°, 120°, 180°, 240°, 300°)`.  Still Z₃-singlet (the
  2ω cancellation argument works at this level too since
  `1 + ω² + ω⁴ = 0` for ω = exp(i·60°)`).

At the level of R60 T16's 2ω cancellation, **both arrangements
satisfy the selection rule**.  The current mass formula treats
them identically.

The question Phase 9d asks: **is there a higher-harmonic or
collective-phase energy that distinguishes Z₆ from 2×Z₃, and
can it supply the deuteron's 2.2 MeV binding?**

#### What Phase 9d needs to produce

1. **A principled ansatz** for a phase-coherence term in the
   compound mass formula.  Candidates to consider:
   - **4ω cancellation** at k = 6: does Z₆ cancel 4ω where
     2×Z₃ does not?  If yes, Z₆ has lower power oscillation
     → lower effective mass.
   - **Inter-triplet phase correlation energy**: if MaSt
     geometry penalizes relative phase between triplets in a
     2×Z₃ arrangement, Z₆ has zero such penalty (all 60°) and
     binds lower.
   - **Ring-direction phase summation**: extend Q132 v2's ω-sum
     (currently single-mode) to multi-strand compounds.  Natural
     candidate: `ω-sum_multi = Σ_k exp(i · 2π · n_pr,k / n_pt,k)`
     over strand-specific windings.  If configurations differ,
     energies differ.

2. **A test against a sharp target**: the deuteron 2.2 MeV
   binding.  One number.  Extends to ³He (7.7 MeV), ⁴He
   (28.3 MeV), ¹²C (92 MeV) if the first number lands.

3. **A consistency check**: the ansatz should give **zero
   correction at k = 3** (single baryon, already Z₃-coherent)
   and non-zero at k = 6, 9, 12, ... .  The mass formula for
   isolated baryons is empirically fine as-is.

#### Why this needs framing work before execution

Unlike 9a-9c, Phase 9d is not a numerical experiment on an
existing framework.  It requires **proposing new structure in
MaSt** — specifically a phase-coherence extension to the mass
formula — and then testing it.  The structural proposal needs
discussion before coding.

The user's intuition: "protons in the nucleus need neutrons to
keep the nucleus stable, and there could be something about
having 6 quarks on the p-sheet that is the strong force magic"
— maps directly to this hypothesis.  A deuteron has 6 p-sheet
strands (3 from p, 3 from n).  Whether those 6 strands arrange
differently than 2 independent 3-strand sets is the question.

#### Status

Phase 9d as originally framed (generic "Z₃ phase coherence" search)
has been **superseded by Track 10**, which the reviewer promoted
into a dedicated track around the deterministic Pauli-saturated
variant.  See Track 10 below.

---

## Track 10 — Pauli-saturated multi-strand coherence

**The reframed mechanism.**  Each (1, 2) p-sheet primitive carries a
Z₃ color (3 values, from R60 T16) and a Dirac–Kähler spin (2 values,
from D7d's per-sheet spinor structure).  Pauli antisymmetry caps
strand-occupancy of a single tuple at 3 × 2 = 6 — the
**Pauli-saturated** configuration.  Six matches the deuteron's quark
count (proton uud + neutron udd = 6 quarks); the hypothesis is that
the saturated compound has lower mass than "two free nucleons" by
the deuteron binding 2.22 MeV, with no free parameters.

The 1s-orbital analogy is load-bearing: two electrons fit `(n,l,m)
= (1,0,0)` because spin distinguishes them; a third electron must
go to 2s.  MaSt's nuclear analog: six p-sheet strands fit one
compactification slot; a seventh requires a radial excitation.

### Phase 10a — Eigenmode geometry and back-reaction capacity (EXECUTED)

Two structural questions, both computable directly:

1. **Geometric**: does the (1, 2) eigenmode profile permit six
   coexisting strands at the g-candidate baseline?
2. **Mechanistic**: does R60 T16's 2ω back-reaction U₂ distinguish
   candidate N = 6 phase arrangements (Z₆ vs 2×Z₃ at various
   inter-triplet angles)?

**Result**: eigenmode is well-defined (FWHM ≈ 83° at θ₁ ≈ 80°);
"ribbon overlap" geometric criterion is wrong (would forbid the
proton); R60 T16's U₂ saturates at −3 for *every* Z₃-coherent N = 6
arrangement, including Pauli-saturated.  The framework's existing
mechanism does not derive a deuteron binding.

See [findings-10.md](findings-10.md) Phase 10a.

### Decision pending

Three readings of Phase 10a, choice belongs to user/reviewer:

- **Reading A** — Honest closure: framework's rigidity exhausted at
  N = 3; binding requires framework extension.  R63 closes here.
- **Reading B** — Extend R60 T16's density-cancellation argument to
  higher harmonics (φ³, φ⁴ contributions to ρ_Q); a Phase 10b
  derivation of effective coherence weights `w_m` from higher-order
  back-reaction.  Stays in Ma; not a free-parameter fit.
- **Reading C** — Binding belongs to S-space configuration energy
  (T8 FR-4 second bullet); R63 documents the closed Ma-internal
  exhaustion and defers binding to a successor study.

If Reading B is selected, Phase 10b runs next.  Otherwise R63 closes
with the binding observable as the explicit open question.

### Exit criteria

- **Success (9d)**: a principled phase-coherence ansatz
  reproduces the deuteron's 2.2 MeV binding within a factor
  of 2, and extends sensibly to heavier nuclei.
- **9d doesn't deliver**: all three Ma-internal candidates
  (9a, 9b/9c, 9d) will then have been tested and falsified.
  The "binding requires framework extension" conclusion from
  F9a.6 becomes earned.  Follow-on study candidates:
  S-space overlap machinery (T8 FR-4 second bullet), dynamical
  L_ring, or a fundamentally new binding physics direction.

### Reusable assets

- Track 6 Phase 6b's tuple-search infrastructure.
- Track 8's additive-composition nucleus tuples as the
  reference to beat.
- `build_aug_metric` from R60 (as-is).
- R60 T16's density-cancellation argument as the template for
  extending phase-coherence reasoning to k > 3.
- The 2.2 MeV deuteron gap as the primary numerical benchmark.

---

## Next-track pool (after Track 6)

Tracks after Track 5.  Sequence decided from its findings.
Entries are sketches; the chosen one is elaborated to full-
track detail when promoted.

**a. Sweep infrastructure.**  Build a parameterized sweep engine
(`ParameterPoint` × `ObservableScorer`) that composes Track 1's
classifier with external observable matching.  Reuse R60
`track1_solver.py` + `build_aug_metric`.

**b. Observable correlation audit.**  For each candidate
observable, estimate `dPrediction/dParameter` numerically at
baseline.  Rank observables by total sensitivity and by
orthogonality (how independently each constrains different
variables).  Informs which observables can realistically pin
what before any observable-anchored sweep runs.

**c. Neutron-anchored sweep.**  With sensitivity map from
**b**, sweep `(ε_p, s_p, ε_ν, σ_xx)` scoring on neutron
observables (mass, Δm, decay Q, lifetime).  Superseded in
priority by Track 7 + pool **q** (the stable-nuclei chain
offers more observables with sharper stability than the
marginally-stable neutron alone).  Kept as a possible
complement.

**d. [Promoted / reframed.]**  The original
"nuclear-scaling-anchored sweep" idea splits into Track 7
(compound-mode vs. separation structural audit, no pinning)
and pool **q** (32-nucleus precision survey, follow-on
pinning).  See Track 7 above.

**e. Inventory consistency sweep.**  Within the region of
agreement from **c** and **d**, verify that no non-pion hadron
regresses below model-F's current accuracy.  **Now superseded
by Track 6** (joint Q132 compound-mode audit) — kept for
legacy reference, but Track 6's joint-optimization approach is
more principled now that sheet-level shortlists exist for
all three sheets.

**f. Charge-radius gut-check.**  Compute r_p and nuclear charge
radii at each sweep point; compare to measurement.
**Informational only; does not pin.**  Documents whether the
circumference-to-radius relationship is consistent across the
sweep.

**g. ε_ν continuous sweep.**  Separable from hadron physics at
leading order (ν-sheet contributes < 10⁻¹⁰ MeV per winding to
hadron modes) but affects the neutrino-oscillation comb and
Majorana predictions.  Run when R61-facing questions resurface,
or when Track 1 / pool item **c** indicates ν-sheet movement
is needed.

**h. Cross-sheet σ exploration.**  R60 T7c found most
cross-sheet activations break α universality, but R60's own
pool item **h** proposes a structural triangular prescription
(σ_ep, σ_eν, σ_νp all nonzero at derived values) that may
preserve it.  Explore only if `(ε_p, s_p)` alone plus at most
`ε_ν` movement leaves meaningful residual constraints.

**i. Anchoring-mode audit.**  L_ring_p is derived by calibrating
the (3, 6) proton to m_p.  Does pinning on a different mode
(e.g., a compound with the proton role) give a meaningfully
different L_ring_p?  Sanity check on the anchoring choice.

**k. ν-sheet (1, 0) ghost audit.**  The ν-sheet has a known
low-mode ghost at `(n_νt, n_νr) = (1, 0)` flagged in model-F's
open questions.  Apply Track 1's discipline to the ν-sheet
specifically: is it observed, split-dominated, or does `ε_ν`
(or `s_ν`, already pinned) need to move to relocate it?
Composes with pool item **g**.

**l. [Promoted to Track 4.]**  E-sheet parallel audit — see
Track 4 section above.

**m. [Captured by Q132 v2.]**  E-sheet winding restriction:
the promotion-chain principle (phase-locked 2π traversals,
ω-sum charge cancellation for gcd=1 primitives with |p_t|>1)
supersedes R33's empirical |n_tube|=±1 as a corollary.
Formalization is an **R62 derivation target**.  R63 adopts
Q132 v2 as the working rule set.

**n. [Absorbed into Track 6.]**  P-sheet re-render under Q132
v2 is part of Track 6 Phase 6a + 6b.

**o. ν-sheet standalone audit (Q132 v2 rules).**  A dedicated
ν-sheet sweep against the three observed ν mass eigenstates
plus v2 dark-mode catalog.  Track 6 Phase 6c will evaluate
whether `ε_ν` meaningfully affects inventory fitness; if so,
this item becomes urgent and runs immediately after Track 6.
If 6c shows no ν-sheet sensitivity for the inventory, **o**
stays as a loose-end cleanup aimed at neutrino observables
rather than hadron inventory.  `s_ν` previously pinned at 0.022
from Δm² ratio 33.6; `ε_ν` undetermined between R61 #1 (2.0)
and R49 Family A (5.0).

**p. [Absorbed into Track 6 Phase 6d.]**  The joint three-
sheet compound-mode search is Phase 6d of Track 6, running
after the per-sheet marginal scans of 6c narrow the joint
product space.

**q. 32-nucleus precision survey.**  Once Track 7 settles the
compound-mode hypothesis structurally, run a finer survey
against ~32 experimentally-known stable-isotope masses
spanning Z=1 to Z=82 (light chain, mid-chain, and up through
²⁰⁸Pb).  Computes per-nucleus residuals at the working
candidate parameter set; tabulates and plots the residual-
vs-(Z, A, binding-energy) pattern.  Because the A-scaling
compound-mode mass is ratio-invariant at leading order, the
survey by itself is NOT a strong ratio-pinning tool on
`(ε_p, s_p)` — all nuclei shift together.  Its power is as a
**discriminating probe for cross-sheet σ_ep** (pool **h**):
σ_ep couples the e-sheet `(1−Z)` contribution to the p-sheet,
producing Z-dependent shifts that distinguish nuclei with
different Z/A ratios.  If σ_ep is admitted as a free variable,
the 32-nucleus survey becomes the discriminating observable.
Dependent on Track 7; composes with pool **h**.

**z. Closeout.**  After chosen pool items execute: if a
coherent set of parameters + Q132 v2 tuple assignments emerges
that (i) closes the pion gap, (ii) passes the v2 ghost audit,
(iii) matches the 19-particle inventory as well as or better
than model-F, (iv) is consistent with cross-observable checks
— recommend a **model-G** formulation (not a model-F patch,
since Q132 v2 changes the rule set).  If no such set exists,
document the obstacle precisely for follow-up work.

---

## Discipline constraints

User-imposed rules R63 should follow throughout execution:

1. **No observable-anchored sweeps before the observable set is
   approved.**  Track 1 does not use external observables and
   is free to run.
2. **No single-ephemeral-particle pin.**  Multiple observables,
   cross-validated.  Pions are a success criterion, not a pin.
3. **Acknowledge the ~60–240× unknown between compact-dimension
   size and measured 3D size** in any track that uses radii.
4. **Anomalous magnetic moments off the table** until MaSt has
   a native Ma-domain mechanism.
5. **Neutron is preferred** as a "stable enough" anchor over
   shorter-lived particles.

---

## Next steps

**R63 active — Track 10 pending decision.**  Tracks 1–9 complete;
Phase 10a executed.  Per-track results in
[findings-1.md](findings-1.md) through
[findings-10.md](findings-10.md); outputs in [`outputs/`](outputs/).

The g-candidate (R63's refinement of model-F) carries:
- Q132 v2 rule set (gcd decomposition + phase-lock).
- e-sheet ghost-free under v2.
- Inventory tuples re-derived where v2 required.
- β-decay-consistent neutron tuple and additive nuclear
  composition.
- Ingredient-sum rule for composite charge.

Track 9 **falsified all three Ma-internal candidate mechanisms**
that don't require new framework structure: cross-shear dressing
(9a), non-additive deuteron tuples (9b), and high-winding mass
formula corrections (9c).  Track 10 reframes the last candidate
(Z₃ multi-strand phase coherence) under a Pauli-saturation rule
(3 colors × 2 spins per p-sheet tuple → 6-strand capacity = the
deuteron).  Phase 10a finds the (1, 2) eigenmode geometry is
computable but R60 T16's 2ω back-reaction does not distinguish
candidate N = 6 arrangements; the framework's existing rigidity
gives no binding-energy difference between "Pauli-saturated
deuteron compound" and "two free nucleons".  Higher harmonics
distinguish but inconsistently and without framework selection.
The deuteron's 2.2 MeV binding remains the open observable.

Directions for future refinement — as successor studies rather
than additional R63 tracks — captured in the close-out sections
of [findings-7.md](findings-7.md),
[findings-8.md](findings-8.md), and
[findings-9.md](findings-9.md).  In brief:

- **Nuclear binding mechanism** (Track 9 successor): four
  framework-extension options — non-additive compound tuples,
  S-space configuration energy, non-linear mass formula,
  dynamical L_ring — each a viable but speculative path.  See
  findings-9 §F9a.4.
- **Systematic tuple optimization under decay constraints**
  (Phase 8c promoted) — least-squares refinement of hadron
  tuples to maximize winding conservation.
- **PMNS neutrino flavor-mixing bookkeeping** (T8 FR-2) —
  proper flavor-eigenstate treatment for leptonic decays.
- **Chiral-anomaly mechanism in MaSt** (T8 FR-3) — first-
  principles derivation of π⁰ → γγ and η → γγ rates.
- **ν-sheet standalone audit** (pool **o**) — open for
  neutrino-sector observables independent of hadronic fit.

**Model-G** remains deferred.  The g-candidate as it stands is
the input to the model-letter-change decision, not the
decision itself.  A second refinement pass — a **model-H** or
a **nuclear-binding-focused successor study** — would be
needed before the full "better than model-F on nuclear
observables" claim can be made.

Open items that could become future R63 tracks or successor
studies:

- **Pool item q** (32-nucleus precision survey) — follow-on
  to Track 7; discriminating for cross-sheet σ_ep in
  composition with pool **h**.
- **Phase 6e** (dark-mode compound catalog) — enumerate v2-valid
  compound dark modes across the three sheets, for future
  phenomenological cross-checks.
- **Pool items h, i, o** — cross-sheet σ exploration,
  anchoring-mode audit, ν-sheet standalone audit.  Each is an
  independent line of work that Tracks 1–6 did not require.
- **Chiral-correction mechanism** — the ~10% pion miss under v2
  sits at the expected ephemeral-echo position (nearest v2
  winding is 121 MeV; observed pions at 135 / 140 MeV).  A
  dedicated study of whether a principled chiral-style
  correction on the p-sheet reproduces the 14 MeV offset would
  be natural R62 or successor work.
- **Model-G** — deferred; a model letter change is warranted
  only if a coherent set of findings is demonstrably superior to
  model-F across multiple criteria.  R63 delivers the g-candidate
  as a
  candidate rule set; the broader judgment call is deferred to
  study-level review.
