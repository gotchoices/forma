# R63: Proton-sheet tuning — disciplined audit and sweep

**Status:** Tracks 1 and 2 complete.  Viable-region map produced;
the analytical bound `μ(3, 6) ≤ 8.09` (≈ 62% of the tested grid)
is confirmed.  Baseline `(0.55, 0.162)` sits comfortably inside
with slack.  One strict-improvement candidate identified:
**`(0.55, 0.180)` preserves all 7 baseline matches and adds a Λ
match** (8 total).  Next: pool item **c** (neutron-anchored
sweep) or **e** (multi-sheet inventory consistency check) to
validate the improvement candidate before any model-F update.
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

## Next-track pool (after Track 2)

Tracks after Track 2.  Sequence decided from Track 2's findings
and the user's observable-set decision.  Entries are sketches;
the chosen one is elaborated to full-track detail when promoted.

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
observables (mass, Δm, decay Q, lifetime).  User's preferred
anchor.  `ε_ν` may move in this track if required by the
neutron fit.

**d. Nuclear-scaling-anchored sweep.**  Same as **c** but
scoring on nuclear masses across the stable-isotope chart.
Cross-validates **c**; agreement is strong evidence.

**e. Inventory consistency sweep.**  Within the region of
agreement from **c** and **d**, verify that no non-pion hadron
regresses below model-F's current accuracy.  Final gate before
recommending a parameter update.

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

**l. e-sheet re-validation.**  R53 already pinned `(ε_e, s_e)`
so that electron/muon/tau are the three lowest charged modes.
Re-run the Track 1 methodology on the e-sheet as a sanity
check that the e-sheet still satisfies the ghost criterion
after any downstream metric updates.  **Now more urgent after
Track 1's obstacle finding** — test whether R53's e-sheet
itself passes the ghost discipline, or whether it only pins
the |n_et| = 1 sector and leaves |n_et| ≥ 4 as a latent
issue.

**m. E-sheet winding restriction / high-n filter.**  Track 1
F5 identified this as the natural response to the light-ghost
obstacle: any mode with effective |Q| > 3 has no matter-decay
path below ~2 GeV, and the audit finds such modes at
|n_et| = 4, 5 on the e-sheet.  Need a principled selection
rule that restricts |n_et| ≤ some cap (probably 3), analogous
to Z₃ on the p-sheet.  Candidates:
  (i) derived-from-geometry rule (some waveguide or resonance
      argument that makes |n_et| ≥ 4 exponentially suppressed);
  (ii) cross-sheet σ_ep that promotes high-|n_et| + p-sheet
       combinations to energies above the cap (composes with
       pool **h**);
  (iii) explicit R56/R57 routing analysis at higher N-body
        decays that shows the ghosts are actually split-
        dominated under more sophisticated accounting.

**z. Closeout.**  After chosen pool items execute: if a
coherent parameter shift emerges that (i) closes the pion gap,
(ii) passes ghost audit, (iii) preserves inventory, (iv) is
consistent with observable matches — recommend a model-F
baseline update.  If no such shift exists, document the
obstacle precisely for follow-up work.

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

- **Tracks 1 and 2 complete.**  Viable region characterized;
  `(0.55, 0.180)` identified as a strict improvement over
  baseline.  See [findings-1.md](findings-1.md),
  [findings-2.md](findings-2.md).
- **Natural next step: pool item c or e** to validate
  `(0.55, 0.180)` against additional constraints (neutron
  physics or multi-sheet inventory).  If both pass, it
  becomes the recommended new baseline for model-F.
- **Pool items a, b, d, f–l remain available** — sequence
  depends on user preference and observable-set decisions.
