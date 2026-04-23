# R63: Proton-sheet tuning — disciplined audit and sweep

**Status:** Framed — Track 1 ready; subsequent tracks chosen from
the pool based on Track 1's outcome.
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

R63 addresses this gap:

1. **Track 1 (now):** enumerate every physical-filter-compliant
   p-sheet and compound mode in order of energy at the current
   baseline; classify each as observed / split-dominated / ghost.
2. **Subsequent tracks (chosen later):** depending on what
   Track 1 finds, target parameter adjustments, observable-
   anchored sweeps, cross-sheet explorations, or all of the
   above.

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

## Track 1 — Mode-by-mode ghost audit (intrinsic-first tuning)

**Motivation.**  The electron sheet is self-cleaning: R53 tuned
`(ε_e, s_e)` so that electron, muon, tau are the three lowest
charged modes, with higher modes heavy enough that R56/R57
routing dominates.  The historically-worrisome (1, 1) ghost is
not filtered — it *is* the muon.  The shear resonance substitutes
for an explicit filter.

The proton sheet has not been audited this way.  Track 1 applies
the e-sheet discipline to the p-sheet and to compound modes at
the current model-F baseline.

**Goal.**  For each sheet and each compound class, enumerate
every physical-filter-compliant mode in ascending mass order.
Classify each as:

- (a) **observed particle** — match within the model-F threshold
      (tolerate the current 10–13% on pions per Track 21),
- (b) **split-dominated** — `E_mode > min(sum(E_obs_i) +
      V_separation)` per R56/R57 routing, so the mode is
      naturally suppressed,
- (c) **genuine ghost** — neither observed nor split-dominated;
      requires explanation or parameter adjustment (pool
      item **a**).

**Strategy.**

1. Single-sheet audits first: e-sheet (validate), p-sheet
   (expected open items), ν-sheet (the known (1, 0) item).
2. Compound audits next: 2-sheet (mesons), 3-sheet (baryons).
3. Splitting-threshold evaluation for each unexplained mode:
   `E_mode` vs `min_split(sum(E_obs_i) + V_separation)` with
   V_separation from the R56/R57 cost model.
4. Output: per-scope ordered list of (mode, energy,
   classification, notes).  Feeds pool item **a** if non-empty.

**Tactics.**

- Reuse R60 T20 Phase D enumeration (Z₃ on p-sheet + charge +
  composite α + spin filters); extend with energy-ordered
  output up to a bounded cap (initially 2 GeV; extensible).
- New primitive `splitting_threshold(mode, metric)` returns
  the minimum split cost over decompositions into observed
  lighter particles.
- One script per audit scope; each produces markdown + CSV.

**Acceptance.**

- e-sheet: (1, 2) = electron, (1, 1) = muon, high-n tau; no
  lighter charged mode; no intermediate charged modes.
- p-sheet: either clean or produces a ranked ghost list.
- ν-sheet: characterizes (1, 0) and related low modes.
- Compound audits: ordered lists with observed-particle tags.

**What Track 1 is NOT.**

- Not a parameter sweep.  Inventory-at-baseline.
- Not dependent on external observables.  Uses only the known
  particle list and R56/R57 routing cost.

**Payoff.**

- **If the p-sheet is clean:** `(ε_p, s_p)` does not need to
  move for intrinsic reasons.  Track 21's pion fix becomes a
  free-floating optimization against external observables
  (pool items **b**–**f**).
- **If the p-sheet has ghosts:** pool item **a** becomes a
  targeted geometry adjustment, potentially aligned with
  Track 21's shift, potentially not.  Either outcome is
  informative.

---

## Next-track pool

Tracks after Track 1.  Sequence decided from Track 1's findings
and the user's observable-set decision.  Entries are sketches;
the chosen one is elaborated to full-track detail when promoted.

**a. Targeted parameter adjustment against ghost list.**  If
Track 1 identifies p-sheet (or compound) ghosts, mirror R53's
e-sheet methodology: for each ghost, identify the `(ε_p, s_p)`
direction that relocates it onto an observed particle or lifts
it above the splitting threshold, without breaking existing
matches.  Composes with Track 21's pion-driven shift.

**b. Sweep infrastructure.**  Build a parameterized sweep
engine (`ParameterPoint` × `ObservableScorer`) that composes
Track 1's classifier with external observable matching.
Reuse R60 `track1_solver.py` + `build_aug_metric`.

**c. Observable correlation audit.**  For each candidate
observable, estimate `dPrediction/dParameter` numerically at
baseline.  Rank observables by total sensitivity and by
orthogonality (how independently each constrains different
variables).  Informs which observables can realistically pin
what before any observable-anchored sweep runs.

**d. Neutron-anchored sweep.**  With sensitivity map from
**c**, sweep `(ε_p, s_p, ε_ν, σ_xx)` scoring on neutron
observables (mass, Δm, decay Q, lifetime).  User's preferred
anchor.

**e. Nuclear-scaling-anchored sweep.**  Same as **d** but
scoring on nuclear masses across the stable-isotope chart.
Cross-validates **d**; agreement is strong evidence.

**f. Inventory consistency sweep.**  Within the region of
agreement from **d** and **e**, verify that no non-pion
hadron regresses below model-F's current accuracy.  Final
gate before recommending a parameter update.

**g. Charge-radius gut-check.**  Compute r_p and nuclear
charge radii at each sweep point; compare to measurement.
**Informational only; does not pin.**  Documents whether the
circumference-to-radius relationship is consistent across
the sweep.

**h. Cross-sheet σ exploration.**  R60 T7c found most
cross-sheet activations break α universality, but its own
pool item **h** proposes a structural triangular prescription
(σ_ep, σ_eν, σ_νp all nonzero at derived values) that may
preserve it.  Explore only if Tracks **a**–**f** leave
meaningful residual constraints.

**i. Anchoring-mode audit.**  L_ring_p is derived by
calibrating the (3, 6) proton to m_p.  Does pinning on a
different mode give a meaningfully different L_ring_p?
Sanity check on the anchoring choice.

**j. ε_ν continuous sweep.**  Separable from hadron physics at
leading order (ν-sheet contributes < 10⁻¹⁰ MeV per winding to
hadron modes) but affects the neutrino-oscillation comb and
Majorana predictions.  Run when R61-facing questions resurface.

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

- **Track 1 is ready to execute now.**  Self-contained,
  intrinsic to model-F, no external observables required.
  Produces the ghost map that informs which pool items are
  worth promoting.
- **Pool items b–j await Track 1's outcome and user decisions**
  about the observable set.
