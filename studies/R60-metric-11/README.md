# R60: Metric-11 — particle spectrum on R59's α-derivable 11D architecture

**Status:** Framed — Track 1 ready
**Type:** theoretical + compute
**Depends on:** R59 (tube↔ℵ↔t architecture, F54 + F59), R53 (generations),
  R49 (neutrinos), R54 (compound modes), model-E

---

## Objectives

R59 closed with a viable 11D architecture for α coupling
(tube↔ℵ↔t) that produces α_Coulomb = α (within 60 ppm) at the
natural-form parameter point:

- σ_ta = √α (e-tube to ℵ at +√α; p-tube to ℵ at −√α)
- σ_at = 4πα (single ℵ to t entry)
- g_aa = 1 (ℵ diagonal)
- k = 1/(8π) ≈ 0.040 (Ma sheet diagonal scale, k_e = k_p)

Universality (α_e/α_p = 1.000) and ν neutrality (α_ν = 0) are
structural properties of the architecture, not tuning choices.

But the metric requires Ma diagonals at k = 1/(8π) — far smaller
than the model-E normalization of 1.  Model-E's internal shears
(especially s_e = 2.004) actively block this architecture.

R60 asks: can a metric configuration be found that simultaneously:

1. Implements R59's α architecture (k = 1/(8π), σ_ta = √α,
   σ_at = 4πα, g_aa = 1)
2. Reproduces the model-E particle spectrum (electron, proton,
   neutron, three lepton generations, neutrino mass eigenstates,
   hadron inventory)
3. Identifies which model-E mechanisms survive and which need
   replacement

If yes, R60 produces a successor candidate (potentially "model-F"
— though the model designation is deferred until viability is
established).  If no, R60 documents specifically which constraint
blocks it — narrowing the search for an alternative α mechanism.

The directory is named "metric-11" because the 11D structure
(adding ℵ to model-E's 9D Ma+S+t) is what's being explored;
whether this becomes model-F depends on R60's outcome.

---

## Execution plan

Tracks are added one at a time.  Only the currently-executing
track is numbered; candidates for "next track" live in the pool
below as lettered items and get numbered when chosen.  This keeps
the plan responsive to what each track actually reveals.

### Track 1 — Solver infrastructure (framed)

**Goal.**  Build and validate the 11D metric + joint-fit toolkit
that later tracks will use to search for particles one at a time.
No physics conclusions in this track — only tested machinery.

**Strategy.**

Implement four primitives and a thin fitting wrapper, each with
a smoke test against a known result.  Keep the API small; grow
it only when a later track needs something.

**Tactics.**

1. **Metric builder.**  `build_metric_11(params)` returns the
   11×11 array using the R59 index ordering ℵ, p_t, p_r, e_t,
   e_r, ν_t, ν_r, S_x, S_y, S_z, t.  Incorporates per-sheet
   in-sheet shear via B = diag(L)(I + S), per-sheet diagonal
   scaling k, tube↔ℵ entries with sign pattern (+, −, 0) for
   (e, p, ν), and the ℵ↔t entry.

2. **Signature check.**  `signature_ok(G)` — exactly one negative
   eigenvalue (the t direction).  Rules out knob combinations
   that break Lorentzian structure.

3. **Mode energy.**  `mode_energy(G, n_11)` for an 11-vector mode
   with zeros in the S and t slots.  Same quadratic form that
   R59 and model-E use, generalized to 11D.

4. **α_Coulomb extractor.**  `alpha_coulomb(G, n_11)` reproduces
   R59 track3g's formula:
   Q = (ñ · G⁻¹[:, t]) × (−G⁻¹[t, t]), then α = Q² / (4π).

5. **Joint fitter.**  `solve(params_free, params_fixed, targets)
   → (params, residuals, jacobian_info)` using
   `scipy.optimize.least_squares`.  Targets are a generic list of
   residual functions so later tracks can supply their own
   (mass residual, α residual, ratio residual).  This track does
   not hard-code the model-E target list.

**Smoke tests (infrastructure only).**

| # | Test | Expected outcome |
|---|------|-----------------|
| T1 | `build_metric_11` with all α knobs = 0 and model-E Ma params reproduces model-E's 6×6 mode energies | m_e, m_p agree with [lib/metric.py:model_E()](../lib/metric.py) to < 10⁻¹⁰ relative |
| T2 | `alpha_coulomb` on the R59 F59 clean metric (k = 1/(8π), g_aa = 1, σ_at = 4πα, σ_ta = √α) | α_Coulomb = α to < 100 ppm (matches R59 F59) |
| T3 | `signature_ok` rejects the F41 failure cases (model-E Ma + any tube↔ℵ entry) | returns False as expected |
| T4 | `solve` fits L_ring_e to a target m_e, all else fixed | converges to the same value as the closed-form expression L = 2πℏc μ / m_e |

**Deliverables.**

- `scripts/track1_solver.py` — primitives + `solve` wrapper + the
  four smoke tests above, runnable as `python track1_solver.py`.
- findings.md entries F1–F4 recording smoke-test results.

**Acceptance criteria.**

- All four smoke tests pass at the tolerances listed.
- The API is small enough to document in a few lines; later
  tracks import from this script (not copy-paste).

**Prototyping note.**  Lives in
[scripts/track1_solver.py](scripts/) only.  Promotion to `lib/`
is deferred until 2–3 later tracks have imported from it with
no changes — that's when the API is stable enough to share.

---

### Track 2 — Electron sheet viability map

**Goal.**  Characterize the electron sheet by itself, as a 2D
parameter problem in (ε_e, s_e).  Report:

1. The locus where the electron (1, 2) can be calibrated to m_e
   (trivial: any (ε_e, s_e) with L_ring_e free).
2. The region where (1, 2) is the lightest charged e-sheet mode —
   i.e., where the (1, 1) ghost sits above (1, 2).
3. The region where the R59 F59 α knobs (k_e = 1/(8π), σ_ta = √α
   on e-tube, g_aa = 1, σ_at = 4πα) preserve Lorentzian signature.
4. The overlap of (2) and (3), if any.

Stop here.  Muon and tau are compound in model-E (muon = e+ν,
tau = e+ν+p) and need the other sheets — they cannot be tested
before Tracks 3 (ν-sheet) and 4 (p-sheet) are built.

**Background.**  Track 1 T3 showed that R53 Solution D
(ε_e = 397.074, s_e = 2.004200) breaks signature under the R59
F59 α knobs.  It is unknown whether (a) a nearby (ε_e, s_e) works,
(b) the viable region is elsewhere entirely, or (c) no region
exists.  Track 2 answers this without committing to any
generation-ratio hypothesis.

**Strategy.**  Two independent constraints evaluated on the same
(ε_e, s_e) grid:

- **Ghost-order constraint.**  At each (ε_e, s_e), compute the
  single-sheet mode energies μ(1, 1, ε, s) = √(1/ε² + (1 − s)²)
  and μ(1, 2, ε, s) = √(1/ε² + (2 − s)²).  Ghost-order favorable
  iff μ(1, 1) ≥ μ(1, 2).  (Equivalently: |1 − s| ≥ |2 − s|,
  i.e., s ≥ 1.5.  Independent of ε.  Worth confirming by direct
  computation anyway.)
- **Signature constraint.**  Build the full 11D metric with only
  the electron sheet as the active material block (set ν and p
  sheets to identity placeholders, uncoupled) and the R59 F59 α
  knobs on.  Signature OK iff exactly one negative eigenvalue
  (the t direction).

The overlap of these two regions is the viable zone for Track 2's
purposes.  Track 2 does **not** test mass ratios, ghost
suppression beyond simple ordering, or compound modes.

**Tactics.**

1. Scan (ε_e, s_e) on a 2D grid: ε_e ∈ [0.1, 1000] log-spaced,
   s_e ∈ [−3, 3] linear.  At each point evaluate:
   (i) μ(1, 1) vs μ(1, 2) on the bare single sheet (fast, closed form).
   (ii) signature of the 11D metric with R59 F59 α knobs on.
   (iii) smallest-eigenvalue margin (how close to the signature
        cliff) at the passing points.
2. Plot the two regions and their overlap.  Mark the R53 Solution
   D point (397.074, 2.004200) and the R53 Solution B point
   (~330, ~3.00) for reference.
3. Report the overlap region in a form useful for Track 3:
   bounded box + a handful of representative (ε_e, s_e) points,
   with signature margin at each.

**Smoke cross-checks before the scan.**

- At (397.074, 2.004200) with α off: μ(1, 2) < μ(1, 1) (ghost OK
  per R53).
- At (397.074, 2.004200) with α on: signature fails (reproduces
  Track 1 T3).

**Deliverables.**

- `scripts/track2_electron_sheet.py` — grid scan + overlap report.
- findings.md F5 (ghost-order region), F6 (signature-OK region),
  F7 (overlap and representative points).
- No plot required unless the overlap is non-obvious; a clear
  textual description of the boundary is enough if it's a simple
  inequality in (ε_e, s_e).

**Acceptance criteria.**

- Ghost-order region and signature-OK region both reported over
  the full scan range.
- Overlap region identified (empty, bounded, or open).
- At least three representative (ε_e, s_e) points from the
  overlap (if nonempty) with signature margin listed, so Track 3
  has candidates to build on.

**Possible outcomes.**

- **Overlap nonempty.**  Track 3 (ν-sheet) proceeds against one
  of the candidate points.  We don't commit to a specific
  (ε_e, s_e) yet — just pick a point with comfortable margin and
  continue.
- **Overlap empty.**  R59 F59 α knobs are incompatible with a
  ghost-ordered e-sheet.  R60 revisits whether the α knobs can
  be relaxed (e.g., smaller σ_ta, different sign pattern) or
  whether a different α architecture is needed.  This is the
  model-F-existence question answered sharply at the first gate.

---

### Track 3 — Proton sheet viability map

**Goal.**  Same idea as Track 2 but for the proton sheet.
Characterize the (ε_p, s_p) range under which the R59 F59 α
architecture remains signature-OK with the proton sheet active
alongside an already-fixed electron sheet.  Calibrate L_ring_p
from m_p inside that range.  Constrain ranges where no single
preferred value is yet identified.

The proton in model-E is effectively a pure single-sheet (1, 3)
mode (its ν content is decorative; cross-sheet σ₄₅, σ₄₆ are
neutron knobs and don't move the proton).  Three quarks are
"ringings" of the n_pr = 3 ring symmetry — emergent, not separate
modes.  So the proton sheet can be characterized by its own
(ε_p, s_p) without invoking the ν or e sheets.

**Use model-E as a guide, not a pin.**  Model-E's (ε_p = 0.55,
s_p = 0.162) gives s · ε ≈ 0.089 — well inside the 3/√2 ≈ 2.12
Track 2 boundary, so almost certainly inside the joint
e+p signature region too.  Track 3 starts there as a smoke
check, then maps the actual range.

**Note on s_p being free.**  In model-E, s_p was fixed by R19
(`solve_shear_for_alpha(0.55, 1, 3) = 0.162`) — i.e., s_p was
the value that made R19 give α at that ε_p.  In R60 the α
mechanism has moved to Ma↔ℵ↔t coupling (R59 F59), so the R19
constraint is gone.  s_p is now genuinely free until pinned by
something else (compound modes, neutron, hadron near-misses —
all later tracks).

**Strategy.**

1. Fix the electron sheet at a representative Track 2 candidate.
   Recommended: (ε_e = 1, s_e = 3/2) — the analytic corner of
   the Track 2 overlap.  L_ring_e calibrated to m_e.
2. Scan (ε_p, s_p) over a 2D grid with the same span as Track 2.
3. At each (ε_p, s_p):
   (i)   Compute L_ring_p so that E(0,0,0,0,1,3) = m_p exactly
         (closed form, always achievable).
   (ii)  Build the full 11D metric with e+p sheets active, ν
         identity placeholder, R59 F59 α knobs on with sign_p
         = −1 on p-tube.
   (iii) Check signature.
   (iv)  Compute α_Coulomb on the proton mode (0,0,0,0,1,3) —
         universality demands α_p / α_e ≈ 1 by R59 F45.
4. Report Region C (signature-OK, p-sheet alone) and Region D
   (signature-OK with e-sheet active at the chosen point).
   Compare; characterize whether adding the p-sheet meaningfully
   tightens the signature region or not.

**Tactics.**

- Boundary refinement by bisection in ε_p along several s_p
  lines, parallel to Track 2's analysis.  Look for an analogous
  s · ε boundary; it may differ because the joint e+p
  configuration places more demand on ℵ.
- Smoke check at model-E (0.55, 0.162): expect signature OK,
  α_p / α_e ≈ 1 to 60 ppm, mass exact by construction.
- Compare Region D against several different e-sheet anchors
  (e.g., also (0.1, 1.5)) to see if the e-sheet choice
  materially changes the p-sheet viable range.

**Smoke cross-check before scan.**

- Model-E (ε_p, s_p) = (0.55, 0.162) with e-sheet at (1, 3/2):
  signature OK, α_p / α_e ≈ 1.

**Deliverables.**

- `scripts/track3_proton_sheet.py` — scan + boundary refinement +
  candidate report.
- findings.md F11 (smoke), F12 (Region C: p-sheet alone), F13
  (Region D: joint e+p), F14 (interpretation, candidate range,
  comparison to model-E).

**Acceptance criteria.**

- Region D characterized over the scan range with a clear
  bounded form (analytical inequality if it falls out, otherwise
  a numerical region with representative points).
- α_Coulomb universality verified on the joint metric: α_p / α_e
  within 1% across the viable region.
- At least three representative (ε_p, s_p) points reported,
  including one near model-E and one with maximum signature
  margin.

**Scope.**

- Only ε_p and s_p are varied; L_ring_p is derived from m_p.
- Ghost-ordering on p-sheet is **not** a Track 3 constraint
  (matches the Track 2 convention; (1,1) ghost suppression is
  handled by other mechanisms — waveguide, irreducibility, R47
  Track 7 gcd argument).
- No quark mass-ratio test (quarks are ringings of n_pr = 3,
  not separate modes; no R60 lever for them).
- No compound modes (neutron, mesons) — those are later tracks.

**Possible outcomes.**

- **Region D is wide.**  Proton sheet poses no architectural
  constraint; model-E's (0.55, 0.162) is comfortably inside.
  Carry forward and proceed to Track 4 (ν-sheet).
- **Region D is narrow but nonempty.**  Constrains the proton
  geometry but lets us pick a comfortable point.  Carry forward.
- **Region D excludes model-E.**  Proton sheet has a different
  viable range than model-E used.  Document and carry forward
  with a new working (ε_p, s_p).
- **Region D is empty.**  Joint e+p with R59 F59 α is
  structurally infeasible.  Major problem; revisit α
  architecture or e-sheet choice.

---

### Track 4 — Per-sheet diagonal compensation for α universality

**Goal.**  Test whether allowing the per-sheet diagonal scale to
differ between sheets (k_e ≠ k_p) can recover both α universality
(α_e = α_p = α) and α magnitude (= observed α) on a metric with
internal shears active.  Track 3 showed that R59 F59's identical-k
assumption is fragile under shear — this track checks whether the
fragility is the assumption or the architecture.

**Background.**  R59 F59 found that on a *shearless* clean Ma
metric, `k_e = k_p = 1/(8π)` with σ_ta = √α and σ_at = 4πα gives
α_Coulomb = α to 60 ppm with α_e = α_p exactly.  R59 F57
established that universality requires `k_e = k_p` *on that
metric*.  Track 3 showed that with shears on (s_e ≥ 3/2 from
ghost order, s_p free) both universality and magnitude break
even at identical k.  Working hypothesis: identical k was never
the real symmetry — what's required is *whatever per-sheet k
makes that sheet's α extraction land on observed α*.  In the
shearless case, that happens to be 1/(8π) for both sheets; with
shears, k_e ≠ k_p.

**Strategy.**

For fixed (ε_e, s_e, ε_p, s_p), solve for the four-knob vector
(L_ring_e, k_e, L_ring_p, k_p) such that:

| Target | Source |
|--------|--------|
| E(electron mode) = m_e        | mass calibration |
| E(proton mode)   = m_p        | mass calibration |
| α_Coulomb(electron) = α       | α magnitude (e-sheet) |
| α_Coulomb(proton)   = α       | α magnitude (p-sheet) |

Universality (α_e = α_p) follows automatically when both α
targets are met.

The solve is a 4×4 nonlinear system with `scipy.optimize.least_squares`
on the Track 1 solver.  Run in two modes for diagnostic value:

1. **Per-sheet independent.**  Two 2×2 solves: (L_ring_e, k_e)
   against (m_e, α_e), then (L_ring_p, k_p) against (m_p, α_p),
   each with the *other* sheet's α coupling turned off (sign = 0).
   Gives "what each sheet wants in isolation."
2. **Joint.**  One 4×4 solve with both sheets active.  The
   "right" answer because in the joint metric each sheet's α
   extraction depends on the other sheet (via the shared ℵ).
   Compare to (1) to quantify cross-sheet contamination.

**Tactics.**

1. **Smoke at shearless clean.**  At (ε_e, s_e, ε_p, s_p) =
   (1, 0, 1, 0), the solver should converge to k_e = k_p = 1/(8π)
   with both α targets met (R59 F59 reproduction).  Sanity that
   the joint solve recovers known-good values.
2. **Smoke at Track 3 best point.**  At (ε_e=0.1, s_e=1.5,
   ε_p=0.55, s_p=0.162), Track 3 found α_p/α_e = 1.05 already.
   Joint solver should pull this to exactly 1 with mild k
   adjustments.
3. **Stress at Track 3 worst point.**  At (ε_e=1.0, s_e=1.5,
   ε_p=0.55, s_p=0.162), Track 3 reported α_p/α_e = 8.78.
   Solver either converges with very different k_e, k_p, or
   fails — either outcome is informative.
4. **Pathology check.**  At (ε_e=0.5, s_e=2.0, ε_p=0.55,
   s_p=0.162), Track 3 reported α_e ≈ 0 (sign-flip cancellation).
   The α_e target may have no real-k solution; document the
   failure mode.
5. **Map k_e/k_p as a function of (ε, s).**  For a small grid of
   (ε_e, s_e) and (ε_p, s_p) pairs inside the Track 3 viable
   region, run the joint solve and tabulate the resulting k_e
   and k_p.  Look for patterns (e.g., does k_x scale with
   (ε_x · s_x) in a clean way?  Does the ratio k_e/k_p depend
   only on the difference between sheets?).

**Smoke cross-checks before search.**

- Build the shearless clean metric with the R59 F59 knobs, run
  `alpha_coulomb` — should give 1.000061×α (matches Track 1 T2).
- Initial guess for joint solve: k_e = k_p = 1/(8π) and
  L_ring_x derived from m_x at that k.  At a viable point, the
  solver should improve from this seed.

**Deliverables.**

- `scripts/track4_diagonal_compensation.py` — independent + joint
  solves at the four representative points above, plus the (ε, s)
  map.
- findings.md F17 (smoke at clean), F18 (per-sheet vs joint
  diagnostic), F19 (results across representative points), F20
  (k_e/k_p patterns and what they imply).

**Acceptance criteria.**

- The joint solve converges at the shearless clean point to
  R59 F59's k = 1/(8π) within solver tolerance.
- At least one (ε, s) pair inside Track 3's viable region yields
  α_e = α_p = α to ≤ 1% with a real, signature-OK metric.
- The solver's failure modes (where they occur) are clearly
  characterized: sign-flip pathology, no-real-k region,
  signature breach, etc.

**Possible outcomes.**

- **Clean convergence everywhere.**  Per-sheet k *is* a function
  of that sheet's (ε, s) — α universality is recovered at the
  cost of an extra knob per sheet (no longer assumed identical).
  R59 F59 generalizes cleanly; model-F program is alive.
  Promote pool item **f** (analytical derivation of k(ε, s)).
- **Convergence in some regions, failure in others.**  R59 F59
  is *partially* generalizable.  Model-F is constrained to the
  regions where Track 4 succeeds.  Map them.
- **No convergence anywhere with shears.**  R59 F59's natural
  α-knob set is irretrievably shear-incompatible.  R60 must
  either accept approximate universality (path a in Track 3
  decision) or pivot to a different α architecture (pool item g).

---

## Next-track pool

Candidates after Track 4.  Sequence decided as we go.

**a.** (absorbed into Track 2)

**b. Smallest-shear neutrino solution.**  Same exercise for s_ν
from R49's Δm²₃₁/Δm²₂₁ = 33.6.  R26 Family A uses s_ν = 0.022
(already small, probably compatible), but confirm across
neutrino families and identify any constraints on ε_ν.

**c. Joint metric search.**  With s_e and s_ν bounds known from
Tracks a/b, run the Track 1 solver over (ε, s, σ_cross) to find
a single 11D metric satisfying all targets.  This is the "does
model-F exist?" computation.

**d. Re-derived particle inventory.**  Given a viable joint
solution, re-solve for mode tuples across the model-E 18/20
particle inventory on the new metric.  Check that neutron compound
still works (0.07%), hadron near-misses still near, and Q = −n₁ +
n₅ still integer-valued.

**e. Survival audit of model-E results.**  Systematically check
each model-E prediction on the R60 metric: charge formula, neutron
compound mode, nuclear scaling (n₅ = A, n₆ = 3A), three neutrino
eigenstates, shell structure (R56), energy routing (R57).  Any
prediction that survives at the same accuracy is carried into
model-F; any that degrades flags a conceptual cost.

**f. Analytical derivation of α match.**  Verify that α_Coulomb
= α at (k = 1/(8π), g_aa = 1, σ_at = 4πα, σ_ta = √α) is an exact
algebraic identity, not a numerical coincidence.  Derive the
inverse-metric expression in closed form and check the 60 ppm
residual is a floating-point artifact.  If true, α is *derived*.

**g. Fallback — alternative α architecture.**  If Track c shows
the tube↔ℵ↔t architecture cannot coexist with the model-E
spectrum, investigate an alternative α mechanism compatible with
the preserved spectrum (extended R19, moduli potential, GRID
lattice scale).  Only relevant if c fails.

**z. Closeout.**  After the chosen pool items execute: if
viability holds, promote to model-F candidate with a migration
document from model-E.  If not, document the specific blocking
constraint so future work can target it directly.

---

## Files

| File | Purpose |
|------|---------|
| README.md | This framing document |
| scripts/ | Computation scripts (per track) |
| findings.md | Results (after computation) |
