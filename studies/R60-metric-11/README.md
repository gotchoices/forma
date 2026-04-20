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

### Track 5 — Proton on shearless electron + α-decoupling locus

**Goal.**  Two complementary pieces, run together because they
inform each other:

1. **Numerical: confirm Q1.**  Show that with the electron sheet
   left shearless (s_e = 0), the proton sheet at any reasonable
   (ε_p, s_p) inside Track 4's working region can be calibrated
   to m_p with α_p = α via per-sheet diagonal compensation k_p.
   The Track 4 Smoke 1 (clean) and Smoke 2 (T3 best) points
   already suggest this works; Track 5 maps the proton viable
   region against a fixed shearless-e baseline.

2. **Analytical: derive the α-decoupling locus.**  Track 4 F19
   discovered that at s_e = n_r/n_t for the electron's reference
   mode (specifically s_e = 2 for the (1, 2) electron), the α
   extraction Q_e cancels to zero independent of k_e.  Derive
   the closed-form condition Q_e = 0 in (ε, s) so we know which
   curves to avoid in *every* later (ε, s) scan.  This is the
   pool-item-f analytical complement to the numerical work.

The two pieces share infrastructure (Track 1 solver) and
context, so combining them keeps the analysis coherent.

**Strategy.**

*Part 1 (numerical).*

Fix the electron sheet at (ε_e = 1, s_e = 0).  This sits inside
Track 4's confirmed-working region (Smoke 1 reproduces R59 F59
exactly there).  Vary the proton sheet (ε_p, s_p) over a 2D grid
spanning Track 3's Region D.  At each grid point:

- Run Track 4's joint solver over (L_ring_e, k_e, L_ring_p, k_p)
  against (m_e, m_p, α_e=α, α_p=α).
- Record convergence, signature, residuals, k values.
- Map the proton viable region under shearless e-sheet.

If the viable region is wide and includes natural starting
points (e.g., model-E's (0.55, 0.162) or analytically nice
choices like (1.0, 0.0) or (0.5, 0.5)), Q1 is confirmed and we
have a clean baseline for Track 6 (ν-sheet).

*Part 2 (analytical).*

Compute Q_e symbolically for the electron mode (1, 2) on the
e-sheet alone (other sheets uncoupled, sign_e = +1).  The
expression

    Q_e = (n_e_tube/L_e_tube · G⁻¹[e_t, t]) +
          (n_e_ring/L_e_ring · G⁻¹[e_r, t])

depends on the inverse metric block.  With the 2×2 sheet block
`k·[[1, sε], [sε, 1+(sε)²]]`, the e-tube and e-ring entries of
G⁻¹[:, t] propagate through the (e-tube ↔ ℵ ↔ t) chain.  Find
the (ε, s) curve where the two terms cancel.

Hypothesis (from F19 evidence): the curve is `s = n_r/n_t = 2`
for the (1, 2) mode, independent of ε — but we should derive
this rather than assume.  Generalize for arbitrary (n_t, n_r).

If derivable, the result tells us:
- Which (ε, s) curves to avoid for *each* sheet (e-sheet, p-sheet,
  ν-sheet) given that sheet's reference mode.
- Whether the locus is exactly s = n_r/n_t or has corrections.
- How "wide" the pathology is (sharp curve vs broad band).

**Tactics.**

- Part 1: extend [scripts/track4_diagonal_compensation.py]
  with a (ε_p, s_p) grid scan at fixed shearless e.  ~15×15 grid
  should suffice.
- Part 2: write `scripts/track5_decoupling_locus.py` that does
  the symbolic derivation either by hand-derived closed form
  or via `sympy` for the 11D inverse metric.  Cross-check
  numerically against the actual Q_e from `alpha_coulomb`.

**Smoke cross-checks.**

- Part 1: at (ε_e=1, s_e=0, ε_p=1, s_p=0), reproduce Track 4
  Smoke 1 (k_e=k_p=1/(8π), all targets exact).
- Part 2: at (ε=0.5, s=2.0) the derived Q_e should equal zero
  (matches Track 4 F19); at (ε=1, s=0) it should be nonzero.

**Deliverables.**

- `scripts/track5_proton_shearless_e.py` — Part 1 grid scan
- `scripts/track5_decoupling_locus.py` — Part 2 derivation
- findings F22 (Part 1 results), F23 (Part 2 derivation), F24
  (combined interpretation: viable proton region + pathological
  curves)

**Acceptance criteria.**

- Part 1: viable region for (ε_p, s_p) under shearless e is
  characterized; at least three concrete candidate proton
  configurations identified.
- Part 2: closed-form expression for the Q_e = 0 locus on a
  single sheet with reference mode (n_t, n_r), validated against
  numerical Q_e from the Track 1 extractor.

**Possible outcomes.**

- **Wide proton region + clean locus formula.**  Best case.  R60
  has a simple rule for choosing (ε, s) per sheet ("stay off
  s = n_r/n_t for the reference mode"), and the proton has many
  options.  Proceed to Track 6 confidently.
- **Narrow proton region or messy locus.**  Constraints tighter
  than expected; we need to be more careful about (ε_p, s_p)
  choice.  Report and proceed.
- **Empty proton region.**  Surprising; would indicate the
  shearless-e + compensated-p approach is itself blocked.
  Pivot needed.

---

### Track 6 — Add the ν-sheet (joint e+p+ν solver)

**Goal.**  Add the ν-sheet on the same architectural footing as
e and p, then joint-solve for all six free knobs (per-sheet
L_ring and k) against six targets (three masses, three α's).
Confirm a working e+p+ν configuration exists.  This is the first
all-three-sheets test of R60's architecture.

**Background.**

- **ν architectural coupling.**  Earlier tracks set `sign_nu = 0`
  (ν-tube uncoupled from ℵ), giving α_ν = 0 by construction.
  That was a simplification, not a physics statement — R55 had
  α_ν ≈ 0.92α via inherited geometry, and R61's neutrino
  taxonomy treats the ν-sheet as architecturally coupled
  with charge-zero arising from topology (Q_charge = −n_e_tube +
  n_p_tube = 0 for pure ν modes, regardless of the ν-tube↔ℵ
  coupling magnitude).  Track 6 turns the architecture on:
  `sign_nu = +1` (same convention as the electron, per R55).
- **(1, 1) immunity.**  Track 5 F22 showed (1, 1) modes never
  decouple — fortunate, because R61's top ν candidates all use
  (1, 1) for ν₁ and ν₂.  No per-mode pathology to dodge for the
  light eigenstates.
- **Wide k ranges expected.**  Sheet ring scales: L_p ~ fm,
  L_e ~ 10⁴ × L_p, L_ν ~ 10⁴ × L_e, L_ℵ possibly ~10⁻¹⁸ × L_p.
  In any normalization that respects this, the per-sheet
  diagonal scales (k) and the ℵ diagonal (g_aa) span many orders
  of magnitude.  R59 F59's `k = 1/(8π), g_aa = 1` was *one*
  self-consistent natural-form choice; other configurations
  involving very different k values are physically reasonable.
  Solver bounds should be wide.

**Strategy.**

Use Track 4's joint solver, extended to three sheets.  Hold the
α-architecture global knobs at R59 F59 natural-form values for
the first attempt, with `sign_nu = +1`.  Free knobs and targets:

| Free knob | Bound (loose) |
|-----------|---------------|
| L_ring_e | (10⁻³, 10⁹) fm |
| L_ring_p | (10⁻³, 10⁹) fm |
| L_ring_ν | (10⁻³, 10⁹) fm |
| k_e | (10⁻⁶, 10⁶) |
| k_p | (10⁻⁶, 10⁶) |
| k_ν | (10⁻⁶, 10⁶) |

| Target | Source |
|--------|--------|
| E(electron mode) = m_e | input |
| E(proton mode) = m_p | input |
| E(ν₁ mode) = m_ν₁ | derived from Δm²₂₁ |
| α_Coulomb(electron) = α | architecture |
| α_Coulomb(proton) = α | architecture |
| α_Coulomb(ν₁) = α | architecture (R55-consistent) |

Six knobs, six targets — square system.  ε and s for each sheet
are *inputs*, chosen from Track 5 baseline (e, p) and R61 (ν).

**Sheet inputs.**

| Sheet | (ε, s) | Mode | Source |
|-------|--------|------|--------|
| e | (1, 0) | (1, 2) | Track 5 baseline |
| p | (1, 0) | (1, 3) | Track 5 baseline |
| ν | (2, 0.022) | (1, 1) for ν₁ | R61 top candidate (`+1,+1)(-1,+1)(+1,+2)`) |

The ν candidate has s_ν · ε_ν = 0.044 — far from any decoupling
locus and well within any reasonable signature budget.  ν₂ at
(−1, 1) and ν₃ at (1, 2) inherit the same (ε_ν, s_ν).

**ν₁ mass target.**  Take m_ν₁ = 32.1 meV from R61 candidate 1
(calibrated to Δm²₂₁ = 7.53 × 10⁻⁵ eV²).  Δm²₃₁/Δm²₂₁ = 33.6
should follow automatically from (ε_ν=2, s_ν=0.022) — verify as
a passive check, don't target.

**Tactics.**

1. **Phase 1: natural-form g_aa.**  Solve at g_aa = 1, R59 F59
   defaults for σ_ta = √α, σ_at = 4πα.  Wide k bounds.
2. **Phase 1.5: rescan against other R61 ν candidates.**  If
   Phase 1 succeeds, also try R61 candidates 2, 3, 4 to see
   how robust the result is across ν geometry choices.
3. **Phase 2 (only if Phase 1 fails for all R61 candidates).**
   Free g_aa as a 7th knob, add a soft target (signature margin
   ≥ some value) or accept a slight Phase 1 residual to make
   the system square.  Document any g_aa deviation from 1 as a
   "natural-form cost."
4. **Cross-checks.**  At any successful configuration: confirm
   ν₂ and ν₃ masses come out at predicted values (no separate
   targeting needed — they share (ε_ν, s_ν)), and confirm
   Δm²₃₁/Δm²₂₁ ≈ 33.6.

**Smoke check before scan.**

Build the metric with Track 5 baseline + R61 #1 ν, R59 F59 α
knobs, sign_nu = +1.  Confirm signature OK, all three sheets
contribute to the inverse metric, no obvious numerical
breakage.  Report initial (uncalibrated) α_ν to see if it's in
the right ballpark.

**Deliverables.**

- `scripts/track6_three_sheet_solve.py` — joint solver, smoke
  + Phase 1 + Phase 1.5; Phase 2 wired but only invoked if
  Phase 1 fails.
- findings.md F27 (smoke + Phase 1 result), F28 (R61 candidate
  rescan), F29 (Phase 2 if needed), F30 (interpretation +
  candidate config for Track 7).

**Acceptance criteria.**

- Joint solver converges on at least one R61 ν candidate with
  all six targets met to ≤ 1% (mass) and 1% (α universality).
- Signature OK at the converged configuration.
- ν₂, ν₃ masses and the Δm² ratio cross-check correctly.
- A specific (L_e, k_e, L_p, k_p, L_ν, k_ν) configuration is
  identified as the working baseline for Track 7 (compound modes).

**Possible outcomes.**

- **Phase 1 succeeds.**  R60 has a clean three-sheet baseline
  at full natural-form values.  Architecture is fully validated;
  proceed to Track 7 with confidence.
- **Phase 1.5 differentiates ν candidates.**  Some R61
  candidates work, others don't.  Identifies the most viable ν
  geometry — feeds back into R61.
- **Phase 2 needed.**  We have to deviate from g_aa = 1 to make
  it work.  Documents the cost.  Still likely viable, but
  slightly less elegant.
- **Phase 2 also fails.**  ν-sheet inclusion at full α coupling
  is structurally blocked.  Reconsider sign_nu choice or revisit
  the ν architectural coupling assumption.

---

### Track 7 — Ring↔ℵ structural cancellation test

**Goal.**  Test the conjecture (post-Track 6 dialog) that adding
ring↔ℵ entries with the structural prescription
σ_ra = sε · σ_ta on each sheet cancels the shear-induced α
mode-dependence, restoring universality across all (n_t, n_r)
modes on a sheared sheet.

**Background.**  Track 6 found that on sheared sheets, different
modes get different α values via an indirect ring-to-t leak
(ring ↔ tube via shear, tube ↔ ℵ via σ_ta, ℵ ↔ t via σ_at).
Algebraic derivation suggests the ring↔ℵ entry σ_ra at value
sε · σ_ta exactly cancels the leak, leaving Q ∝ n_t (mode-
independent).  R59 ruled out ring-based ℵ mediation as a
*replacement* for tube coupling (F39, F43) but did NOT test
ring↔ℵ as a *supplement* with this specific structural relation.

**Strategy.**  Use the Track 6 F28 baseline (R61 #1 ν, e/p
shearless, k_e = k_p = 4.73 × 10⁻², k_ν = 4.53 × 10⁻²).
Compute σ_ra per sheet, build the augmented metric, compare α
extraction for ν₁/ν₂/ν₃ between base and augmented.

**Tactics.**

- σ_ra prescription: σ_ra_x = (s × ε)_x × sign_x × σ_ta
  - σ_ra_e = 0 (e shearless)
  - σ_ra_p = 0 (p shearless)
  - σ_ra_ν = 0.044 × √α ≈ 3.76 × 10⁻³ (the ν-sheet shear
    is what produces mode-dependence in the first place)
- Build augmented 11D metric with these new ring↔ℵ entries
- Verify signature still OK
- Compute α for electron, proton, ν₁, ν₂, ν₃; report base vs
  augmented values

**Acceptance criteria.**

- Augmented metric: signature OK preserved
- α_ν₁ / α_ν₂ / α_ν₃ all equal each other to ≤ 0.1%
  (Track 6 had spread 0.91× to 1.19× of α — i.e., 28%)
- α_e and α_p unchanged (their σ_ra = 0)

**Possible outcomes.**

- **Universality restored.**  Architectural fix works.
  Mode-dependence problem retired.  R60's program proceeds
  with the augmented architecture.
- **Universality partially restored.**  First-order cancellation
  works but residual cross-sheet effects remain.  Refine.
- **Universality not restored.**  Derivation had a wrinkle.
  Re-examine.

---

### Track 15 — Sandboxed (3, 6) proton viability test

**Motivation.**  R62 derivation 7b derives the WvM ratio rule
`s = n_t/n_r` from CP field rotation on the 2-torus, giving spin
1/3 for the (1, 3) mode model-F currently uses for the proton.
The parity rule "odd n_t → spin ½" used in R50–R61 was introduced
without formal derivation.  If the ratio rule is correct, model-F's
proton assignment is invalid and (3, 6) becomes the natural
candidate (3 quarks at 120° phase, gcd=3, spin = 3/6 = ½).

A parallel effort (derivation 7c, "always 1/2 for emergent
particles") may rescue (1, 3) with a different derivation.  Both
directions need to stay open until one is definitively settled.

Track 15 is a **sandboxed empirical test** of (3, 6) proton
viability on the existing R60 / model-F architecture.  No
changes to model-F, no changes to findings-1 through findings-14,
no changes to any prior scripts.  New scripts use a `track15_`
prefix.  Binary outcome per option: **viable / not viable**
under specific architectural tests.  Output: `findings-15.md`.

**Goal.**  Determine whether a (3, 6) proton could be substituted
for (1, 3) in model-F's architecture without catastrophic
breakage of the spectrum or nuclear scaling.  Keep both options
open in parallel with 7c's progress.

**Scope — 5 phases, ~half day of work.**

### Phase 1 — proton mass on (3, 6)

**Question:** can (3, 6) reach m_p = 938.272 MeV on model-F's
Track 12 baseline (ε_p = 0.55, s_p = 0.162) or does it need
geometry changes?

**Method:**
1. Evaluate (0, 0, 0, 0, 3, 6) on existing Track 12 metric
   (expected result: ~2160 MeV — too heavy by 2.3×).
2. Recalibrate L_ring_p alone to give 938.272 MeV for (3, 6).
   Report: new L_ring_p.
3. Alternative: switch to magic shear for (1, 2) quark base
   (s_p = 2), pick ε_p such that quark mass = m_p/3 = 313 MeV.
   Report (ε_p, L_ring_p, k) for this configuration.

**Acceptance:** both options converge to clean mass fit.
Document the (L_ring_p, possibly ε_p, s_p) values.

### Phase 2 — α_Coulomb for (3, 6) proton

**Question:** does the proton land at α_Coulomb = α under a
composite interpretation (gcd-aware charge), or does the bare
α-sum formula give 9α as expected?

**Method:**
1. Compute bare α_Coulomb for (0, 0, 0, 0, 3, 6) on model-F
   metric with Phase 1's calibration.  Expected: 9α (R47 Track
   7 analog confirms the model-F α-sum rule gives 9α for n_pt=3
   bare).
2. Propose and test a **composite α-sum rule**:
   `α_sum = −n_et + n_pt/gcd(n_pt, n_pr) + n_νt` (new rule,
   gcd-aware).  Compute α_Coulomb under this rule.  Expected
   for bare (3, 6): α = α.
3. Verify the composite rule reduces to the current rule for
   gcd = 1 modes (all of model-F's current inventory).  Should
   be backward-compatible for existing modes.
4. For nuclei (A, Z) under the natural (3, 6)-based scaling
   `n_pt = 3A, n_pr = 6A`: compute α_Coulomb with composite
   rule.  Expected: α = Z² α for any Z (if the composite rule
   generalizes correctly).

**Acceptance:** composite α rule gives α = α for proton and
α = Z²α for Z-nuclei.  Or: document what it gives instead.

### Phase 3 — nuclear scaling on (3, 6) base

**Question:** can nuclear masses still be reproduced under a
(3, 6)-based scaling law?  This is the historical dealbreaker
(model-D set aside (3, 6) for this reason).

**Method:**
1. Define candidate nuclear scaling laws:
   - Scheme A: `n_pt = 3A, n_pr = 6A, n_et = (something)_Z`
     — A copies of a 3-quark bundle
   - Scheme B: `n_pt = A·(3 or custom), n_pr = A·(6 or custom)`
     — other scalings
2. Compute d, ⁴He, ¹²C, ⁵⁶Fe masses for each scheme.
   Compare to Track 11's model-F accuracy (0.05–1.5%).
3. If no clean scheme works: document the failure mode
   (same as model-D, or different?).

**Acceptance:** at least one scheme gives ≤ 2% on all four
nuclei, and α = Z²α under the composite rule.  Or: document
the blocker.

### Phase 4 — quick comparison with (1, 2) proton alternative

**Question:** is (1, 2) on the p-sheet even cheaper than (3, 6)?
It's ratio-rule spin ½ and simpler topology.

**Method:** compute (0, 0, 0, 0, 1, 2) on model-F metric with
recalibrated L_ring_p.  Report mass, α (bare and composite —
gcd(1,2) = 1 so they should agree), and quick nuclear check.

**Acceptance:** binary viable/not viable finding for (1, 2).

### Phase 5 — three-way verdict

**Question:** across (1, 3), (3, 6), (1, 2) proton candidates,
which are viable on model-F architecture *without* spin-rule
commitment?

**Method:** summary table per candidate of:
- Proton mass fit achievable
- α = α under applicable formula (bare, composite)
- Nuclear scaling status
- Compound mode spin assignments (ratio rule vs 7c if known)

**Output:** findings-15.md with verdicts, plus a short section
on "what would need to change in model-F if this candidate is
adopted."

## Implementation plan

**New scripts (under `scripts/` with `track15_` prefix):**

- `track15_baseline_36.py` — Phase 1 (mass fit for 3, 6)
- `track15_composite_alpha.py` — Phase 2 (composite α rule)
- `track15_nuclear_36.py` — Phase 3 (nuclear scaling)
- `track15_alternatives.py` — Phase 4 (1, 2) check
- `track15_verdict.py` — Phase 5 (summary)

**Reused from existing scripts (no modification):**

- `track1_solver.py` — metric builder, signature, α extraction
  primitives
- `track7b_resolve.py` — joint solver helpers, augmented metric
- `track11_nuclear_scaling.py` — nuclear-mode helpers (may need
  alternate versions in Phase 3)

**Acceptance criteria for Track 15 as a whole:**

- Phase 1 completes with a concrete (ε_p, s_p, L_ring_p) for
  each viable proton candidate
- Phase 2 definitively shows the bare α-sum rule gives 9α and
  proposes (or rules out) a composite alternative
- Phase 3 determines whether (3, 6) nuclear scaling can match
  model-F's Track 11 accuracy
- Phase 4 checks the (1, 2) alternative
- Phase 5 gives a three-way verdict table

**What Track 15 does NOT do:**

- Doesn't change `model-F.md`, Track 1–14 findings, or prior
  scripts
- Doesn't rework R60's main inventory
- Doesn't resolve the spin rule question — that's derivation 7c's
  job
- Doesn't commit to any replacement; just evaluates viability

---

### Track 16 — Z₃ confinement derivation for (3, 6) proton

**Motivation.**  Track 15 showed that (3, 6) is a mechanically
viable proton mode on model-F's architecture — mass, α_Coulomb,
and nuclear scaling all work with a composite (gcd-aware) α
rule.  What Track 15 did *not* answer is **why (3, 6) should be
observable as a free particle when (1, 2) and (2, 4), the
lighter modes on the same ratio ray, are not.**  On a single
sheet no shear makes (3, 6) lightest — at magic shear s = 2 the
ratio-2 ray gives μ(1, 2) < μ(2, 4) < μ(3, 6), with (1, 2) one
third of (3, 6)'s mass.  A confinement mechanism is required:
a structural reason why (1, 2) exists only as a confined
constituent ("quark") and (3, 6) as the free composite.

The motivating analogy is three-phase electrical power.  A
single sinusoidal phase carries instantaneous power that
oscillates at 2ω — a generator pulsates, a motor chatters.
Two phases at 180° *reinforce* the pulsation; two phases at
90° cancel it only by secretly being a 4-phase system.  Three
phases at 120° are the true minimum count at which the 2ω
power fluctuation cancels.  Mathematically:

<!-- Σ_{k=0..N−1} cos(2ωt + 4πk/N) = 0  iff  N does not divide 2 -->
$$
\sum_{k=0}^{N-1} \cos\!\left(2\omega t + \tfrac{4\pi k}{N}\right)
\;=\; 0
\qquad \Longleftrightarrow\qquad
N \nmid 2,
$$

so N = 1 and N = 2 fail; N = 3 is the minimum cancelling N.

Porting the same argument to MaSt: if a single (1, 2) standing
wave on the p-sheet has an energy (or charge) density that
oscillates at 2ω, then a **lone (1, 2) mode is not a stationary
state of its own field** — it drives a 2ω back-reaction or
radiation channel.  Three (1, 2) modes at 120° phase offsets
have constant total density and *are* stationary.  Pairs cannot
achieve this, matching the "diquarks are not observed" feature
of QCD.

If this argument closes rigorously, it derives a **Z₃ selection
rule on the p-sheet**: free modes require n_t ≡ 0 (mod 3);
others exist only as confined constituents of a Z₃-singlet
triplet.  That would give (3, 6) a principled footing, not just
a phenomenological one.

**Goal.**  Determine whether a physically rigorous Z₃
confinement mechanism exists on the p-sheet that:

1. Identifies a 2ω density fluctuation associated with a
   single (1, 2) standing-wave mode
2. Shows N = 3 is the minimum copy count that cancels that
   fluctuation under uniform phase offsets
3. Shows the 120° offsets are dynamically preferred (an
   energy minimum) rather than postulated
4. Yields the selection rule `n_t ≡ 0 (mod 3)` for free modes
   on the p-sheet
5. Does not impose an equivalent rule on the e-sheet or
   ν-sheet (so their observed single-strand particles remain
   free)

If all five hold, (3, 6) is put on solid ground and the
confinement story for the p-sheet is derived, not postulated.
If any step fails, document the blocker; (3, 6) stays
phenomenologically viable but not derived.

**Scope — 4 phases, half-day to full day.**

### Phase 1 — identify the 2ω density fluctuation

**Question:** for a single (1, 2) standing-wave mode on the
p-sheet (model-F metric, Track 12 geometry: ε_p = 0.55,
s_p = 0.162), what physical density oscillates at 2ω, and
what is its coupling to the α channel?

**Method:**

1. Write the mode field on the p-sheet as a real standing
   wave: ψ_{1,2}(y_t, y_r, t) = A·cos(y_t/R_t)·cos(2 y_r/R_r − ωt)
   (or the complex rotating equivalent, whichever matches the
   6D field content assumed in F7 / F11 / R59).
2. Compute candidate density quantities:
   - Amplitude squared ψ² (oscillates at 2ω)
   - Energy density (kinetic + compact-momentum; typically
     oscillates at 2ω for a real standing wave)
   - Charge density ρ_Q ∝ n_t · ψ² (the source of the α
     coupling through the tube↔ℵ channel)
3. Identify which of these is the *physically relevant* source
   for the radiation / back-reaction channel.  The charge
   density ρ_Q is the natural candidate: it couples to the KK
   gauge potential via minimal coupling (F14), and oscillation
   of ρ_Q at 2ω produces a 2ω current that sources photon
   emission in the low-energy limit.
4. Report: symbolic form of the 2ω-oscillating part of ρ_Q,
   its amplitude, and its coupling strength to the α sector.

**Acceptance:** an explicit symbolic expression for a 2ω
oscillating density on a single (1, 2) mode, with a clear
argument for why it represents a non-stationary state (i.e.,
the mode is not a self-consistent standing wave against its
own gauge back-reaction).

### Phase 2 — N-copy cancellation

**Question:** summing N identical (1, 2) modes at uniform
temporal phase offsets 2πk/N (k = 0, …, N−1), for which N
does the 2ω density fluctuation cancel?

**Method:**

1. For each N ∈ {1, 2, 3, 4, 5, 6}, compute the total density
   Σ_{k=0}^{N−1} ρ_Q(t + kT/N) symbolically and decompose
   into constant + 2ω oscillating parts.
2. Show that the 2ω oscillating part vanishes iff N does not
   divide 2 — i.e., for N ∈ {3, 4, 5, 6, …} but not N ∈ {1, 2}.
3. Highlight the N = 2 case explicitly: two (1, 2) copies at
   180° offset *do not* cancel — they reinforce the 2ω
   fluctuation (matching "diquarks are confined" in QCD).
4. Confirm N = 3 is the minimum cancelling N, and that
   higher multiples 6, 9, … are also cancelling (predicting
   (6, 12), (9, 18) as potential resonance states).

**Acceptance:** closed-form proof of the cancellation pattern
N ∤ 2; numerical verification on the model-F p-sheet geometry
agrees to floating-point precision.

### Phase 3 — dynamical selection of 120° offsets

**Question:** why do three (1, 2) copies prefer exactly 120°
offsets?  Is this dynamically selected (an energy minimum) or
must it be postulated via a p-sheet Z₃ structure?

**Method:**

1. Write the pairwise interaction energy between two (1, 2)
   modes on the p-sheet.  Natural candidates:
   - **Coulomb-like self-coupling** through the shared α
     channel: E_int(φ) ∝ ∫ρ_Q,1(t)·ρ_Q,2(t + φ/ω) dt,
     which is maximally negative at some specific phase offset.
   - **Overlap term** through the Ma sheet metric (mode–mode
     coupling from off-diagonal entries).
2. For three copies at phase offsets (0, φ_A, φ_B), compute
   total interaction energy E_int(φ_A, φ_B) and locate its
   minima.  Expected under 2ω-dominated coupling: minima at
   (φ_A, φ_B) = (120°, 240°) and cyclic permutations.
3. If minima are at 120°/240° → dynamically derived.  If not,
   fall back to postulating Z₃ phase structure on the p-sheet
   as an architectural axiom (still a valid path, but adds an
   axiom rather than deriving one).
4. Document whichever path closes.

**Acceptance:** either (a) a clean dynamical derivation of
120° offsets from interaction-energy minimization, or (b) a
well-framed postulate of p-sheet Z₃ structure with
justification from the sheet's (ε, s) geometry.  Path (a) is
stronger; path (b) still supports the Z₃ confinement story.

### Phase 4 — selection rule and compatibility with Track 15 + model-F

**Question:** does the selection rule `free p-sheet modes
require n_t ≡ 0 (mod 3)` preserve all of Track 15's findings
and model-F's compound-mode inventory?

**Method:**

1. Apply the rule to Track 15's proton inventory:
   - (3, 6) free ✓
   - (1, 2), (2, 4) confined (not free particles, consistent
     with "quark" interpretation) ✓
   - (6, 12) candidate free resonance — identify as Δ-like if
     mass matches
2. Apply to Track 15's nuclear scaling (n_pt = 3A, n_pr = 6A):
   always divisible by 3 ✓
3. Apply to model-F's 18-entry compound inventory from
   Tracks 10 and 12:
   - Enumerate p-sheet contribution (n_pt, n_pr) for each
     particle
   - For entries with n_pt ≢ 0 (mod 3): search for a Z₃-
     compatible alternative tuple with same charge Q, spin,
     and α_sum_composite
   - Report the rule's compatibility fraction
4. Check e-sheet and ν-sheet: the rule should NOT apply
   there.  Justification: the Z₃ selection emerges from the
   p-sheet's specific (ε, s) regime (or from its 3-phase
   "quark" compactification), not from the KK mechanism
   generically.  Verify by showing the e-sheet's single-(1, 2)
   electron does not suffer the same 2ω fluctuation problem,
   or that the problem is cured differently (e.g., by the
   parity structure of e-sheet's spin).

**Acceptance:** the n_t ≡ 0 (mod 3) rule is consistent with
Track 15 and with ≥ 80% of model-F's compound inventory under
its natural tuple assignments; any incompatible entries have
Z₃-compatible alternatives within a tuple-search window
|n_i| ≤ 6.  Clear account of why the rule is p-sheet-specific.

## Implementation plan

**New scripts (under `scripts/` with `track16_` prefix):**

- `track16_phase1_density.py` — single-mode 2ω density
  computation (partly symbolic via sympy, partly numeric on
  the p-sheet metric)
- `track16_phase2_cancellation.py` — N-copy cancellation
  proof and verification
- `track16_phase3_dynamics.py` — interaction-energy
  minimization over phase offsets
- `track16_phase4_selection.py` — selection-rule consistency
  check across Track 15 and model-F inventory

**Reused from existing scripts (no modification):**

- `track1_solver.py` — metric builder, mode energy primitives
- `track7b_resolve.py` — augmented-metric helpers
- `track15_*.py` — (3, 6) baseline and composite α helpers
- `track10_hadron_inventory.py` — model-F compound inventory
  for Phase 4 consistency checks

**Acceptance criteria for Track 16 as a whole:**

- Phase 1 identifies a physically-motivated 2ω density
  fluctuation for the single (1, 2) mode
- Phase 2 proves N = 3 is the minimum cancelling N
  (matching 3-phase power mathematics)
- Phase 3 either derives the 120° offsets or postulates them
  with geometric justification
- Phase 4 demonstrates the selection rule is compatible
  with Track 15 + model-F

**What Track 16 does NOT do:**

- Doesn't replace derivations 7a/7b/7c.  Track 16 is about
  *confinement* (which modes exist as free particles), which
  is orthogonal to *spin* (the SO(1,3) representation content).
  Any of 7a/7b/7c that makes (1, 2) spin-½ is compatible with
  the Z₃ confinement derivation.
- Doesn't promote to model-G.  That would be a separate
  decision based on (a) Track 16's outcome, (b) a migration
  plan from model-F's (1, 3) proton and bare α rule, and
  (c) re-running Tracks 10–13 under the new inventory
  constraint.
- Doesn't settle the proton-mode question across the
  architecture.  Even if Track 16 succeeds, the choice
  between (3, 6) and (1, 2) as the proton depends on whether
  the confinement story permits the composite or the simplex.

**If Track 16 succeeds (all 4 phases close):**

- (3, 6) has a principled confinement-based justification
- Model-G becomes the active candidate for the working model
  (Track 15 mechanical viability + Track 16 derivation
  together form its foundation)
- Pool item **k** below is promoted to "resolved by Track 16"

**If Track 16 fails (Phase 1 or 2 or 3 doesn't close):**

- (3, 6) remains phenomenologically-viable (Track 15) but
  without a derived confinement mechanism
- Model-F with (1, 3) stays the working model pending
  alternative resolution of the spin-rule question
- Failure mode is documented as a blocker for the model-G
  candidate, with pool item **k** updated to reflect the
  specific obstruction

---

### Track 17 — e-sheet single-phase proof

**Motivation.**  Track 16 closed the Z₃ confinement argument on
the p-sheet: a single (1, 2) real-field mode has 2ω density
fluctuation; three copies at 120° offsets cancel it; therefore
(3, 6) is the minimum free composite.  But the argument is
*generic* — any real-field KK mode has the 2ω fluctuation.  If
the rule applied universally, the electron (a (1, 2) mode on
the e-sheet) would be confined too, which contradicts
observation.

Track 16 Phase 4 documented three candidate mechanisms that
could suppress Z₃ confinement specifically on the e-sheet:
geometry (extreme s·ε), scale suppression, and σ_ta sign
structure.  Track 17 makes the geometry argument **quantitative**.

**Working hypothesis.**  The Z₃ binding energy U_bind(ε, s) is a
computable function of the sheet's geometry.  On the p-sheet
(s·ε ≈ 0.089, near-diagonal) it gives the −3/2 per-triplet
binding that Track 16 Phase 3 found.  On the e-sheet (s·ε ≈ 795,
shear-saturated) the 2ω source term is either redirected into
propagating ring-modes (effectively radiated away) or reduced
by a factor that scales with 1/(s·ε)^α for some exponent α,
bringing U_bind to zero at the extreme.

If this picture is right, there is a threshold sheet geometry
above which Z₃ binding is absent — a "phase boundary" between
confined and free single-strand modes.  Electrons and neutrinos
sit on one side, quarks on the other.

**Goal.**  Derive a quantitative expression for U_bind(ε, s) on
a generic sheet and confirm:

1. U_bind(p-sheet) ≈ −3/2 (or the corresponding back-reaction
   energy reduction of Track 16 Phase 3)
2. U_bind(e-sheet) ≈ 0 (or bounded by << p-sheet value)
3. A clear threshold (sharp or smooth) separates the two
4. ν-sheet falls on the unconfined side for reasons consistent
   with observation (free neutrinos)

**Scope — 3 phases, ~half day.**

### Phase 1 — Sheet-dependent 2ω source strength

**Question:** how does the amplitude of the 2ω density
fluctuation depend on sheet geometry (ε, s)?

**Method:**

1. Generalize Track 16 Phase 1's ρ_Q computation to arbitrary
   (ε, s).  On a sheared sheet, the (1, 2) mode wavefunction in
   Fourier form has modified dispersion through the inverse
   metric G⁻¹.  Compute ρ_Q(t) at the peak spatial point for a
   (1, 2) mode on a parameterized (ε, s, k) geometry.
2. Extract the 2ω Fourier amplitude A_2ω(ε, s) as a function.
   Plot over a grid spanning the three sheets' regimes:
   - (ε, s) = (0.55, 0.16) [p-sheet]
   - (ε, s) = (2, 0.022) [ν-sheet]
   - (ε, s) = (397, 2.004) [e-sheet]
   - Plus sampled points to show the shape of A_2ω(ε, s)
3. Report: closed-form or semi-analytic expression for A_2ω(ε, s);
   numeric values on each of the three sheets.

**Acceptance:** A_2ω is well-defined and sheet-dependent.  The
e-sheet value is either zero (proven) or dramatically smaller
than the p-sheet (quantified).

### Phase 2 — Binding energy threshold

**Question:** given the sheet-dependent 2ω source, what is the
binding energy for three-copy Z₃ configurations on each sheet?
Where is the confined/free threshold?

**Method:**

1. Extend Track 16 Phase 3's U(φ_1, φ_2) calculation to include
   the A_2ω(ε, s) weighting.  The penalty becomes

       U_total(ε, s) = (A_2ω(ε, s))² · U_phases({φ_k})

   Under Z₃-symmetric configuration, U_total = −(3/2) ·
   (A_2ω(ε, s))².
2. Plot U_bind(ε, s) over the (ε, s) plane.  Identify the
   threshold contour where U_bind is, say, 1% of the p-sheet
   value (chosen to be below any reasonable natural-form
   binding-energy threshold).
3. Place the three sheets on the plot.  Confirm that
   p-sheet is in the strongly-binding region; e- and ν-sheets
   are in the unbinding region (or, for ν, in the suppressed
   region compatible with free propagation).

**Acceptance:** a clean map of U_bind(ε, s) that places e-sheet
below threshold, p-sheet above, and ν-sheet in whichever
region is consistent with free propagation.

### Phase 3 — Mechanism classification

**Question:** of the three candidate mechanisms (geometry,
scale, sign), which one does the quantitative analysis
identify as responsible for the e-sheet exemption?

**Method:**

1. Decompose A_2ω(ε, s) into its contributing factors:
   - Geometric prefactors from the sheet block's inverse-metric
     entries
   - Scale factors from L_ring (converting dimensionless mode
     frequencies to physical ω)
   - Sign-dependent factors from σ_ta couplings
2. Identify which factor is responsible for the e-sheet's
   suppression.  Most likely candidate: the (1 + (s·ε)²) entry
   in the sheet block, which diverges at large s·ε and absorbs
   the 2ω source into a spectator mode.
3. Document: the mechanism is **geometric** (Phase 3 Option 1
   if that's the answer); or **scale** (Option 2); or **sign**
   (Option 3); or some mixture.

**Acceptance:** a clear, derivation-level explanation of why
e-sheet is Z₃-exempt, grounded in the sheet block's functional
form.

## Implementation plan

**New scripts (under `scripts/` with `track17_` prefix):**

- `track17_phase1_source.py` — A_2ω(ε, s) computation
- `track17_phase2_binding.py` — U_bind(ε, s) map
- `track17_phase3_mechanism.py` — decomposition + interpretation

**Reused from existing scripts (no modification):**

- `track1_solver.py` — metric builder
- `track7b_resolve.py` — augmented metric
- `track16_*.py` — phase-offset machinery

**Acceptance criteria for Track 17 as a whole:**

- Quantitative U_bind(ε, s) map produced
- e-sheet confirmed in the unbinding region
- p-sheet confirmed in the strongly-binding region
- ν-sheet placed consistent with either free propagation
  (Track 18 pursues the alternative interpretation)
- Mechanism classification: geometric / scale / sign identified

**What Track 17 does NOT do:**

- Doesn't resolve the ν-sheet three-phase question
  (Track 18's job)
- Doesn't re-run the inventory or update model-F
  (Track 19 / closeout's job)

---

### Track 18 — ν-sheet structure: oscillation and charge = 0

**Reframed scope.**  Track 18 does not try to settle whether
ν is a Z₃ composite (Track 17's picture (a)) or three separate
modes (current model-F picture (b)).  Either interpretation is
acceptable so long as it accommodates the two empirical
requirements:

1. **Neutrino oscillation.**  Three mass eigenstates with
   Δm²₃₁/Δm²₂₁ ≈ 33.6 and an approximate PMNS mixing matrix.
2. **Electric charge = 0.**  Neutrinos carry no observable
   electric charge.

Under model-F's current architecture:

- Oscillation is handled by R61 triplet (+1,+1)(−1,+1)(+1,+2)
  on ν-sheet with s_ν = 0.022 and ε_ν = 2, giving
  Δm²₃₁/Δm²₂₁ = 33.59 (which matches 33.6).
- Charge = 0 is **definitional** in the sign convention
  Q = −n_et + n_pt (ν-tube doesn't contribute).

Track 18 asks: can we DERIVE the charge-zero property from a
physical mechanism rather than leaving it definitional?  And
can the oscillation structure be shown to be compatible with
either the composite or the three-mode reading?

**Known constraints on ν-sheet geometry.**

- **s_ν = 0.022 is constrained** by the Δm² ratio.  Derivation:
  for the triplet (+1,+1)(−1,+1)(+1,+2), the ratio
  Δm²₃₁/Δm²₂₁ = (3 − 2s)/(4s) depends only on s, not ε.
  Setting this to 33.6 gives s = 0.022 uniquely.
- **ε_ν is free** from oscillation.  ε and L_ring_ν are
  jointly constrained only by the absolute ν mass scale
  (one equation, one free parameter), so ε can be traded
  for L_ring freely.

This means Track 18 has one dimension of geometric freedom
(ε_ν) to play with, which invites exploration of small-ε_ν
regimes for the charge-zero derivation.

**User observations that motivate the approach.**

1. **p-sheet and e-sheet appear architecturally optimized for
   their respective modes** — each sheet's (ε, s) independently
   satisfies multiple constraints at one point (Track 17
   showed this for e-sheet).  A similar self-consistency may
   be available for the ν-sheet.
2. **Earlier studies showed that small tube-to-ring ratio
   (small ε) supports a very dense mode spectrum.**  On a
   sheet with ε → 0, the number of modes below any fixed μ
   grows without bound.
3. **Candidate mechanisms for charge = 0:**
   (i) **No odd ring-winding modes** admitted on ν-sheet
   (ii) **Modes appear in (n_t, n_r)(−n_t, n_r) conjugate pairs**
        that net to zero charge
   (iii) **Topological obstruction** at the ν-sheet's large scale
        prevents localized charge structures from forming
4. **The 4-slot waveguide cutoff from an earlier study** (R46-era)
   eliminated the (1, 1) ghost by pinning wave nodes at four
   equatorial locations.  This is phenomenological (what makes
   the slots?) but available as a backup rule if intrinsic
   mechanisms don't suffice.

**Goal.**  Produce a coherent ν-sheet architecture that:

1. Gives charge = 0 for observed neutrinos via a physical
   mechanism (not just the Q formula's definitional omission).
2. Accommodates observed oscillation phenomenology (Δm² ratio,
   approximate PMNS) in either the composite or three-mode
   reading (whichever drops out cleanly).
3. Fits into model-F's architecture without disrupting the
   e-sheet, p-sheet, or α structure.

**Scope — 4 phases, ~half to full day.**

### Phase 1 — conjugate-pair structure at small ε_ν

**Question:** does the ν-sheet's geometry naturally produce
(n_t, n_r)(−n_t, n_r) conjugate pairs that cancel charge, and
is this amplified by small ε_ν?

**Method:**

1. For ν-sheet geometries with ε_ν ∈ {0.01, 0.1, 0.5, 1, 2, 5}
   at fixed s_ν = 0.022 (oscillation-constrained), enumerate
   the lightest ~20 modes and identify conjugate-pair
   degeneracies.
2. Conjugate pair test: are (n_t, n_r) and (−n_t, n_r) at
   the same μ?  Check:
     μ²(n_t, n_r, ε, s) = (n_t/ε)² + (n_r − n_t s)²
     μ²(−n_t, n_r, ε, s) = (n_t/ε)² + (n_r + n_t s)²
   These differ by 4 n_r n_t s, so they're equal iff s = 0 or
   n_r n_t = 0.  At s_ν = 0.022, the pairs are SPLIT by a
   small amount 4 n_r n_t · 0.022 = 0.088 n_r n_t.
3. For small n_r n_t, the split is tiny (e.g., 0.088 for
   n_r = n_t = 1).  The conjugate pair is near-degenerate.
4. Quantify: for each enumerated ν-sheet geometry, compute
   the mean absolute conjugate-pair split as fraction of μ.
   Small fraction → effective conjugate pairing → charge
   cancellation hypothesis supported.
5. Also check: does small ε_ν amplify the pairing effect
   (by pushing μ higher, making the relative split smaller)?

**Acceptance:** quantitative answer on whether small ε_ν
favors conjugate pairing; recommend an ε_ν value (if any)
where pairing is dominant.

### Phase 2 — mode density at small ε_ν

**Question:** does small ε_ν indeed produce a dense mode
spectrum as suggested by earlier work?  If so, how do we
interpret the resulting infinity of ν-like states?

**Method:**

1. For the same range of ε_ν values, count modes (n_t, n_r)
   with μ below various thresholds (e.g., 2, 5, 10, 100).
2. Extrapolate to ε_ν → 0: does the count diverge?
3. Identify physical interpretation:
   - An infinite tower of ν states (KK-like): most are heavy
     and decouple from low-energy physics; only the lightest
     three are observed
   - A continuous band: the ν sector is essentially a
     continuum of states, and "three flavors" labels only
     the three lightest pairs
   - A degenerate spectrum: many modes at nearly-the-same μ
     that form a superposition observable as a single
     effective flavor
4. Report which interpretation is geometrically favored at
   small ε_ν.

**Acceptance:** clear count vs ε_ν showing the density
behavior; a physical reading of what "dense spectrum" means
for neutrino phenomenology.

### Phase 3 — oscillation compatibility under both readings

**Question:** under the three-mode reading (current model-F)
and under the composite reading (Track 17's geometric
permission), is the observed oscillation phenomenology
reproducible?

**Method:**

1. **Three-mode (model-F current).**
   - Δm²₃₁/Δm²₂₁ = 33.59 from R61 triplet at s = 0.022.  ✓
   - PMNS mixing is freely adjustable by R-matrix structure
     (no internal constraint from ν-sheet).
   - Report compatibility: high (this is the working model).

2. **Composite (three Z₃-bound copies of one (n_t, n_r) mode).**
   - The three phase components of a Z₃ composite are
     initially DEGENERATE.  To match observed Δm², need a
     perturbation mechanism that splits them by the right
     amounts.
   - Candidate perturbations:
     - Small breaking of Z₃ by residual geometry asymmetry
     - Cross-sheet σ coupling (pool item **h** structure)
     - Mode-dependent back-reaction (higher harmonics)
   - Can any of these reproduce the 33.6 ratio?
   - What PMNS structure does Z₃ symmetry predict?
     (Democratic / tribimaximal gives θ₁₂ = 35.3°, θ₂₃ = 45°,
     θ₁₃ = 0 — the last conflicts with observed 8.5°.)

3. Compare the two readings side by side.

**Acceptance:** document both readings with explicit
compatibility status.  The three-mode reading is expected to
win on flexibility; the composite reading is expected to
struggle with θ₁₃ unless a natural Z₃-breaking perturbation
provides the 8.5° deviation.

### Phase 4 — charge = 0 derivation and slot fallback

**Question:** can we derive charge = 0 from a structural
mechanism — or must we accept the Q formula's definitional
approach, optionally backstopped by the 4-slot waveguide rule?

**Method:**

1. Evaluate the three candidate mechanisms:
   - **(i) No odd ring modes:** is there a geometric reason
     (sheet topology, parity) that forbids odd n_r on ν-sheet?
   - **(ii) Conjugate pairs always form:** does Phase 1's
     analysis support this at the chosen ε_ν?  What physical
     mechanism forces the observed ν to always be a pair
     superposition rather than a single tube-winding?
   - **(iii) Topological obstruction at large L_ring:** does
     the macroscopic ring scale prevent localized charge from
     persisting?  (Compton wavelength / L_ring analog of
     Track 17's mechanism, in reverse.)
2. If any of (i)-(iii) closes, it becomes the charge
   derivation.  If none do cleanly, document the status:
   Q = 0 is definitional under model-F's sign convention,
   and that convention is self-consistent without further
   derivation.
3. **Slot fallback.**  If (1, 1)-type ghost modes are a concern
   (i.e., they would otherwise be observable ν states but
   aren't), document the 4-slot waveguide rule as an
   available architectural mechanism: pin wave nodes at 4
   equatorial points, killing (1, 1) by destructive
   interference.  This is phenomenological but deployable if
   needed.

**Acceptance:** either a derivation of charge = 0 (preferred),
or a clean statement that Q = 0 is definitional and the slot
rule handles any leftover ghost mode concerns.

## Implementation plan

**New scripts (under `scripts/` with `track18_` prefix):**

- `track18_phase1_conjugate.py` — conjugate-pair structure vs ε_ν
- `track18_phase2_density.py` — mode density vs ε_ν
- `track18_phase3_oscillation.py` — oscillation compatibility
- `track18_phase4_charge.py` — charge = 0 mechanisms + slot fallback

**Reused from existing scripts (no modification):**

- `track1_solver.py` — metric builder
- `track13b_nu_sweep.py` — ν-candidate helpers
- `track17_phase1_source.py`, `track17_phase2_binding.py`
  — sheet spectrum helpers and R_loc logic

**Acceptance criteria for Track 18 as a whole:**

- Phase 1 quantifies conjugate-pair structure at the ν-sheet
- Phase 2 characterizes the dense-spectrum behavior at small ε_ν
- Phase 3 documents oscillation compatibility under both readings
- Phase 4 produces a charge-derivation outcome or a clean
  fallback statement

**What Track 18 does NOT do:**

- Doesn't commit to a composite-ν or three-mode-ν architecture
  (both are acceptable)
- Doesn't change model-F yet (that's Track 19 / closeout)
- Doesn't derive the 4-slot waveguide mechanism from first
  principles (pool item, acknowledged backup rule)

**Possible outcomes:**

- **Clean charge derivation + both readings compatible:** good
  close.  Ν-sheet architecture is documented with an explicit
  charge mechanism and an option for the composite vs
  three-mode interpretation.
- **Definitional charge + one reading compatible:** Q = 0 stays
  definitional; the favored reading (likely three-mode) becomes
  the recommended model-F interpretation for ν.
- **Slot fallback required:** document the rule as "used" and
  note it as a pending derivation target (pool item).

---

### Track 19 — Inventory re-sweep under the (3, 6) interpretation

**Goal.**  Confirm that the full model-F inventory (masses,
α values, nuclear scaling) is preserved when the (3, 6) proton
interpretation is adopted.  This is a verification pass over
the work done by Tracks 10–13, using existing scripts against
the Track 15 Option A calibration (L_ring_p = 47.29 fm).

**Why this track exists.**  Tracks 15–18 derived the (3, 6)
interpretation as a coherent extension of model-F.  Track 15
Phase 2 already showed the composite α rule is backward-
compatible with 17 of 18 model-E inventory tuples.  Track 19
does the empirical check: does the calibrated architecture
actually reproduce the observed masses to the same accuracy
model-F achieved with the (1, 3) reading?

If yes → proceed to model-F update with confidence.
If no → diagnose the specific tuples that diverge and decide
whether they need R60-native alternatives or represent a
blocker.

**Scope — 3 phases, ~2 hours.**

### Phase 1 — Rerun Track 10 inventory on (3, 6) baseline

**Question:** with L_ring_p recalibrated so (3, 6) lands at
the proton mass, and all other parameters unchanged, does
the 18-particle inventory still match within the same accuracy
as Track 10 reported?

**Method:**

1. Build the augmented metric with Track 15 Option A parameters
   (keep everything from Track 12 baseline except L_ring_p =
   47.29 fm).
2. For each of the 18 model-E inventory tuples, compute mass
   and α_Coulomb on the new metric.
3. Compare to the Track 10 reported values.  For each particle,
   note: matches / degrades / improves.
4. Apply the composite α rule for any tuple where the bare rule
   would give α ≠ α; confirm the composite rule keeps α = α.

**Acceptance:** all matched particles stay within the same
accuracy ±0.5% (tight) or ±2% (loose).

### Phase 2 — Rerun Track 11 nuclear scaling

**Question:** does the nuclear scaling law n_pt = 3A, n_pr = 6A,
n_et = 1 − Z give the Track 11 accuracy (d, ⁴He, ¹²C, ⁵⁶Fe
within 0.05–1.5%) on the recalibrated baseline?

**Method:**

1. Use the same metric as Phase 1.
2. Evaluate deuterium, ⁴He, ¹²C, ⁵⁶Fe masses using the
   (3A, 6A) scaling.
3. Compare against Track 15 Phase 3's reported accuracies
   (d 0.05%, ⁴He 0.69%, ¹²C 0.94%, ⁵⁶Fe 1.31%).

**Acceptance:** nuclear masses within Track 15's reported
accuracies.

### Phase 3 — Re-verify α universality

**Question:** does the single-k symmetry (k = 1.1803/(8π) on
all three sheets) still hold under the (3, 6) calibration, and
do the three targeted particles (e, p, ν₁) all land at α = α?

**Method:**

1. Build the augmented metric with Track 15 Option A parameters.
2. Compute α_Coulomb for (1, 2) electron, (3, 6) proton, and
   ν₁ = (1, 1) on the ν-sheet.
3. Verify all three give α_Coulomb = α to floating-point
   precision (as Track 7 established).

**Acceptance:** α universality preserved.

## Implementation plan

**New scripts (under `scripts/` with `track19_` prefix):**

- `track19_phase1_inventory.py` — rerun Track 10 inventory on
  (3, 6) baseline
- `track19_phase2_nuclear.py` — rerun Track 11 nuclear scaling
- `track19_phase3_universality.py` — α universality check

**Reused from existing scripts (no modification):**

- `track1_solver.py` — solver primitives
- `track7b_resolve.py` — augmented metric builder
- `track10_hadron_inventory.py` — inventory and helpers
- `track11_nuclear_scaling.py` — nuclear helpers
- `track15_*.py` — (3, 6) calibration helpers
- `track16_*.py` — Z₃ analysis (for documentation)

**Acceptance criteria for Track 19 as a whole:**

- Phase 1 confirms inventory accuracy within ±2%
- Phase 2 confirms nuclear scaling accuracy within Track 15's
  reported values
- Phase 3 confirms α universality

**What Track 19 does NOT do:**

- Doesn't update model-F yet — that's the next step after
  Track 19 closes positively.
- Doesn't derive anything new; purely a verification pass.

**If Track 19 passes:** proceed to model-F update, which
consists of:
1. Update `models/model-F.md` with (3, 6) proton, composite
   α rule, Z₃ confinement, nuclear scaling, ν-sheet derivation
2. Update R60 STATUS / closeout
3. Note Tracks 15–18 as the derivation chain backing the
   revised architecture

**If Track 19 fails on specific tuples:** diagnose, document
as issues to resolve before model-F update; potentially extend
Track 19 with a Phase 4 re-sweep using R60-native alternatives
for the divergent tuples.

---

### Track 20 — Spin-rule investigation for compound modes

**Motivation.**  Track 19 surfaced an inconsistency: the working
inventory (original Track 10 / model-F and the new Track 19
Z₃-compliant version) uses the R50-era **parity rule** ("odd
count of odd tube windings → spin ½") to filter tuples, but the
claimed spin derivation is **7b's ratio rule** (spin = n_t/n_r),
which applies strictly only to single-sheet modes.  Under strict
7b + any obvious additive composition, only 1–5 of 18 inventory
tuples satisfy the spin target.

Track 20 investigates which compound-mode spin-composition rule
(if any) is both **consistent** with observed spins across the
inventory and **tractable** when used as a search filter.

**Scope — 4 phases + documentation.**  Exploratory, not
commitment.  Goal is to find a rule that works (or confirm no
single rule closes cleanly and accept the parity rule as an
empirical stand-in).

### Phase A — Enumerate candidate rules

Each rule is a function from 6-tuple (n_et, n_er, n_νt, n_νr,
n_pt, n_pr) to a predicted total spin (compared to the target
spin for acceptance).

Core candidates:

1. **Strict per-sheet 7b**: every active sheet has n_r = 2·n_t
2. **Sum-all**: Σᵢ (n_t/n_r)ᵢ = target spin
3. **e+p additive, ν paired off**: (n_t/n_r)_e + (n_t/n_r)_p
4. **Parity rule** (current baseline): odd count of odd tube windings
5. **Vector magnitude**: √(s_e² + s_p² + s_ν²) with per-sheet
   ratio components (orthogonal-sheet Cartesian picture)
6. **L-∞ norm**: max(|s_e|, |s_p|, |s_ν|)
7. **Unit-spin per active sheet**: spin value determined by
   number of sheets with nonzero content via angular-momentum
   addition |s_a ± s_b ± s_c|
8. **Total-winding ratio**: (Σ n_t) / (Σ n_r)
9. **gcd-reduced per-sheet**: use (n_t/gcd_sheet)/(n_r/gcd_sheet)
10. **Integer-ratios-null-out**: sheets with integer n_t/n_r
    contribute 0; only fractional ratios sum
11. **Fractional-part sum**: Σ (ratio mod 1)
12. **Tensor-product allowed**: spin is in the set |s_e ⊗ s_p ⊗ s_ν|

### Phase B — Audit existing inventories

Apply each rule to both the original model-E / Track 10
inventory and the Track 19 Z₃-compliant inventory, marking
pass/fail per tuple.  Tabulate per-rule pass counts.

### Phase C — Identify tractable rules

Criteria:
- **Consistency**: no spin-0 tuple passes a rule predicting spin ½ or vice versa
- **Coverage**: what fraction of inventory passes?
- **Distinguishability**: rule doesn't give the same prediction
  for physically distinct spins

### Phase D — Re-search inventory with top rules

For each rule that emerges from Phase B/C as promising, rerun
the α-filtered brute force with the rule as the spin filter.
Measure mass accuracy per particle.  A rule is **tractable** if
most inventory targets match within 2% under its constraint.

### Phase E — Document verdict

Recommend a working rule (or confirm none) and document as
either:
- **Derived rule found** → integrate into model-F update
- **Empirical stand-in** → parity rule documented as such,
  compound-spin derivation becomes pool item

## Implementation plan

**New scripts (`track20_` prefix):**

- `track20_phase_ab.py` — enumerate rules + audit inventories
- `track20_phase_d.py` — re-search with top rules

**Reused (no modification):** track1, track7b, track10, track15, track19 helpers.

**Acceptance:** Phase A enumerates ≥ 10 rules; Phase B produces
audit grid; Phase C identifies top 2-3 rules; Phase D rerun
reports accuracy per rule; Phase E writes up verdict.

**What Track 20 does NOT do:**

- Doesn't commit to a new rule until user approves.
- Doesn't re-run Tracks 1–19; it's a spin-analysis add-on.
- Doesn't derive the winning rule from first principles; that
  remains a pool-item derivation target if identified.

---

### Track 14 — Analytical derivation of k = 1.1803/(8π)

**Goal.**  Derive the single-k value that the joint solver
finds across all tested geometries.  Is k = 1.1803/(8π) a fixed
point determined by the solver's target set, or an artifact of
the initial guess?  If a fixed point, does it have a closed-form
expression?

**Strategy.**

Phase 1 — **Empirical.**  Rerun the joint solve with different
initial k values (k_init = 0.5/(8π), 1/(8π), 2/(8π), etc.).  If
solver always converges to the same k, it's a fixed point.  If
it depends on init, it's an artifact.

Phase 2 — **Symbolic (sympy).**  With σ_ra = (sε)·σ_ta active,
the α extraction Q = n_t · σ_ta at structural cancellation.  The
full formula α_Coulomb = Q²/(4π) · (−G⁻¹[t,t])² gives an implicit
equation in k at the targeted α_Coulomb = α.  Solve for k
symbolically.

Phase 3 — **Natural form match.**  Given the solved k value (a
numeric constant), search for a closed-form expression involving
α, π, and small integers.

**Acceptance.**

- Phase 1 establishes whether k is a true fixed point
- Phase 2 produces a closed-form or explicit formula for k
- Phase 3 either finds a clean natural-form expression or
  documents that it doesn't exist

---

### Track 13a — R60-native α-universal inventory on Track 12 baseline

**Goal.**  Ten of model-E's 18 compound tuples have α ≠ α on
Track 12's metric (α_sum ∈ {±2, ±3, ±4}).  For each, search for
an α-universal alternative (α_sum = ±1) within |n_i| ≤ 6 and
report mass accuracy.  Produces a clean "model-F canonical
inventory" ready for the model-F writeup.

**Strategy.**  α-filtered brute force per target, enforcing
α_sum² = 1 and correct Q and spin.  Report top-3 per target.

**Acceptance.**  Every non-pion compound gets an α-universal
tuple within reasonable accuracy (say ≤ 5%).  Pion remains a
known failure (out of scope).

---

### Track 13b — ν-candidate sweep

**Goal.**  Test R61 candidates #1–5 on Track 12 architecture.
For each: does the joint solve converge?  What inventory
accuracy does it give?  Nuclear scaling?  Any candidate
meaningfully better or worse for specific hadrons?

**Strategy.**  For each R61 candidate:
- Run Track 12-style joint solve with that (ε_ν, s_ν) and
  ν-triplet
- Compute inventory accuracy (summary numbers only)
- Rank candidates by composite

**Outcome.**  Either one candidate clearly wins (pick it for
model-F) or multiple are viable (model-F documents them all).

---

### Track 12 — Proton sheet alignment with model-E

**Goal.**  Replace Track 9's magic-shear p-sheet (ε_p = 0.4,
s_p = 3.0) with model-E's proton geometry (ε_p = 0.55,
s_p = 0.162) and re-run the joint solve + inventory audits.
Hypothesis: model-E's p-sheet values are better-tuned for the
hadron inventory and nuclear scaling; reverting to them should
tighten Tracks 10 and 11 accuracies toward model-E's numbers.

**Strategy.**

Phase 1 — joint re-solve with the model-E p-sheet.  Same six
free knobs (L, k per sheet), same six targets.  Check:
- Signature holds (s_p · ε_p = 0.089, well under any bound)
- α universality preserved
- Single-k symmetry preserved (solver should again find
  k_e = k_p = k_ν)

Phase 2 — inventory re-evaluation.  Plug model-E's compound
tuples into the new metric.  Many should now match their
model-E accuracy since the p-sheet is the same.

Phase 3 — nuclear re-audit.  d, ⁴He, ¹²C, ⁵⁶Fe on the new
metric.

**Expected outcomes.**

- **Clean alignment.**  Track 10 accuracy improves to near
  model-E levels for the tuples that failed before; nuclear
  scaling tightens to ≤ 1.1% like model-E.  R60 now matches
  model-E across the full inventory and nuclei, with α
  universality as a structural bonus.
- **Partial alignment.**  Some things improve, some don't.
  Track 12 identifies which hadron/nuclear fits are sensitive
  to p-sheet geometry specifically.
- **Regression.**  p-sheet change breaks something we previously
  had working (unlikely given the structural architecture holds,
  but possible).

---

### Track 11 — Nuclear scaling audit

**Goal.**  Test R29 / model-E's nuclear scaling law (n_5 = A,
n_6 = 3A, with n_et = A − Z for charge Z) on the Track 9 augmented
baseline.  Model-E matched d (0.05%), ⁴He (0.69%), ¹²C (0.76%),
⁵⁶Fe (1.05%) with this scaling.  Does R60 inherit the result?

**Strategy.**

For each nucleus (d, ⁴He, ¹²C, ⁵⁶Fe):
- Construct tuple (A − Z, 0, 0, 0, A, 3A)
- Compute predicted mass on Track 9 metric
- Compute α_Coulomb — for Z-charged nuclei, should naturally be
  Z² × α (since α_sum = −Z by construction)
- Compare to observed nuclear mass

Secondary: vary n_er and n_νr within small range (|n| ≤ 5) to
see if small decorations improve accuracy.

**Expected.**  If nuclear scaling works, this is another major
validation of R60's architecture.  Nuclear masses are independent
of particle-inventory fits (different quantum-number regime, very
different scale).  Success here means the single scaling law
covers ~60 stable nuclei from hydrogen to iron.

---

### Track 10 — Broader hadron inventory on Track 9 baseline

**Goal.**  Having reproduced muon, tau, neutron on the Track 9
extreme-e baseline (Track 9 F54, F55), test R60's coverage of
model-E's broader inventory: Λ, η′, Σ, Ξ, Ξ⁰, φ, ρ, K, η, π.
Two questions: (a) do model-E's tuples evaluate well on Track 9
metric? (b) when they don't, does α-filtered brute force find
an R60-native alternative close to observed?

**Strategy.**

Phase 1 — verbatim: plug each model-E tuple into the Track 9
metric, tabulate E_predicted vs observed and α_Coulomb vs α.
Group by whether tuple matches.

Phase 2 — α-filtered brute-force search for non-matching targets,
enforcing α_sum = (n_et − n_pt + n_νt) with |α_sum| = 1 for
unit charge and |α_sum| = 0 for Q = 0 (checking quantization
pattern on Q=0 hadrons).

Phase 3 — tabulate R60 vs model-E accuracy across the full
inventory.  Flag near-misses and apparent failures.

**Acceptance.**

- All model-E tuples evaluated on Track 9 baseline
- α_Coulomb reported per mode
- For each target, either the model-E tuple matches (within
  model-E's own accuracy ± small residual) or a Track 9 native
  tuple is found

**Possible outcomes.**

- **Most model-E tuples survive.**  R60's architecture plus
  extreme-e revival gives back model-E's spectrum cleanly.
  Major win.
- **Split result.**  Some survive, some need R60-native tuples.
  Document where and why (probably p-sheet geometry difference).
- **Few survive.**  Track 9's p-sheet magic shear is too
  different from model-E's; hadrons need a p-sheet re-tune.

---

### Track 8 — Compound mode search (μ, τ, neutron)

**Goal.**  With the Track 7d magic-shear baseline established
(all three sheets calibrated, α universal across sheets and
modes, ghost ordering on e and p), search for compound modes
— 6-tuples spanning multiple sheets — whose energies match
observed muon, tau, and neutron masses.  First pass: no
cross-sheet σ.  Second pass only if needed.

**Background.**

Model-E's inventory listed the compounds:

| Particle | Observed (MeV) | Model-E 6-tuple | Model-E accuracy |
|----------|---------------:|:----------------|:-----------------|
| muon (μ⁻) | 105.658 | (1, 1, −2, −2, 0, 0) | 0.83% |
| tau (τ⁻) | 1776.86 | (3, −6, 2, −2, 2, 3) | 0.05% |
| neutron (n) | 939.565 | (0, −4, −1, 2, 0, −3) | 0.07% |

Ordering: `(n_et, n_er, n_νt, n_νr, n_pt, n_pr)`.

Each mode satisfies MaSt constraints:
- **Charge:** `Q = −n_et + n_pt`  (=−1, −1, 0 above ✓)
- **Spin-½:** odd total tube-winding parity on at least one sheet
- **Reality:** metric eigenvalue must be positive (mode is physical)

Model-E used these specific 6-tuples with R19-era α (not the R59
F59 architecture we have now).  Whether they land at observed
masses on the Track 7d R60 metric is an open question — the metric
has changed (magic shear geometry, ring↔ℵ entries, single-k
symmetry, different L values).  Track 8 tests this empirically.

**Strategy.**

Three phases, gated on results:

**Phase 1 — direct check of model-E tuples.**  Take each
model-E compound 6-tuple verbatim; compute its mass on the Track
7d baseline.  If residuals < 5%, compound modes "survive the
transition" and we have a good story.  If > 5%, Phase 2.

**Phase 2 — search for alternative 6-tuples.**  For each target
(μ, τ, n), do a bounded brute-force search over 6-tuples `|n_i|
≤ N_max` satisfying the (Q, spin) constraints.  Report the
closest-mass candidates and document the best match.  Compare
to model-E: same mode, different, or no clean match?

**Phase 3 — α audit on compound modes.**  For each compound
mode that matches a target mass, compute α_Coulomb.  Track 7
only verified α universality for simple single-sheet modes;
compound modes span multiple sheets and might have
mode-dependent α.  Report.

If Phase 3 shows compound modes have α ≠ α universally, this
tells us whether pool item **h** (cross-sheet α cancellation
prescription) is needed or whether we accept mode-dependent α
on compounds as a feature.

**Tactics.**

- Enumerate 6-tuples with `|n_i| ≤ 10` (~2M candidates, tractable)
- Apply Q and spin filters before computing mass (fast reject)
- Compute `mode_energy` on the Track 7d metric for filtered
  candidates
- Rank by `|E_predicted − E_target| / E_target`
- Report top-10 per target particle
- Compute α_Coulomb for the top-1 match; flag if not at α

**Smoke cross-checks before scan.**

- Confirm model-E's tuples load correctly and give the expected
  charge/spin assignments on our code
- Confirm Track 7d's stable particles (e, p, ν₁, ν₂, ν₃) still
  give exact masses + α = α

**Deliverables.**

- `scripts/track8_compound_modes.py` — Phase 1 + Phase 2 search
  + Phase 3 α audit
- findings-8.md — results per target particle, best match summary
- Updated candidate baseline for Track 9 (if compound results
  indicate pool item h is needed)

**Acceptance criteria.**

- Phase 1 completes: three model-E compound tuples evaluated on
  Track 7d metric; residuals reported
- Phase 2 completes: alternative 6-tuple candidates found within
  5% of each target, or documented as not achievable at current
  metric
- Phase 3 completes: α status of each matched compound mode
  reported (universal at α, or mode-dependent with specific
  deviation)

**Possible outcomes.**

- **Best case.**  Model-E tuples land within 1% on Track 7d, α
  universal across compounds.  R60 architecture is validated end
  to end — the model-E spectrum transfers cleanly.  Promote to
  model-F candidate.
- **Mixed.**  Some compounds match, others need different
  6-tuples.  Catalog the differences; R60 inventory is slightly
  different from model-E but equally justified.
- **α mode-dependence on compounds.**  Compounds have α ≠ α.
  Pool item **h** becomes the natural next track.  Decide
  between "derive cancellation prescription" and "accept
  mode-dependent compound α" based on severity.
- **No compound matches close enough.**  Major issue — would
  indicate the Track 7d geometry is wrong, or that compound
  modes in MaSt need a richer mechanism (e.g. cross-sheet σ is
  not just a correction but is load-bearing).  Significant
  replanning.

---

### Track 7d — Magic-shear baseline re-solve (ghost ordering)

**Goal.**  Replace Track 7b's shearless (ε=1, s=0) baseline for
the e and p sheets with magic-shear geometries that make each
sheet's target mode the *lightest* charged mode on that sheet
— restoring ghost ordering as a built-in structural feature.
Verify that Track 7b's α universality survives the change.

**Background.**  At Track 7b's (ε=1, s=0) baseline, the mode
(1, 1) on each charged sheet is lighter than the target mode
((1, 2) electron, (1, 3) proton) — violating ghost ordering.
We deferred this to "other mechanisms" but it raises the
diagnostic complexity of Track 8.  "Magic shear" — setting
`s_x = n_r / n_t` for each sheet's target — makes the target
mode have ring energy `(n_r − s·n_t)² = 0` and thus minimal
μ = 1/ε, lighter than all other (1, *) modes on the same sheet.

**Sheet configuration.**

| Sheet | Target mode | Magic shear | Proposed (ε, s) | sε | Decoupling check |
|-------|:-----------:|:-----------:|:---------------:|:--:|:----------------:|
| e | (1, 2) | s_e = 2 | (0.4, 2.0) | 0.8 | off sε = 1 locus ✓ |
| p | (1, 3) | s_p = 3 | (0.4, 3.0) | 1.2 | off sε ∈ {0.382, 2.618} ✓ |
| ν | (1, 1) target | s_ν from R49 Δm² | (2.0, 0.022) | 0.044 | (1,1) never decouples ✓ |

Joint signature budget check: `Σ(sε)² = 0.64 + 1.44 + 0.002 =
2.08` < predicted 5/2 three-tube bound.

**Strategy.**

- Fix the (ε, s) values above.  Free knobs remain (L_e, k_e,
  L_p, k_p, L_ν, k_ν) as in Track 7b.
- Architecture: ring↔ℵ structural σ_ra entries active (Track 7
  prescription).
- Targets: same six (masses + α universality) as Track 7b.
- Verify after convergence:
  1. All targets met to floating-point precision
  2. Ghost ordering confirmed on each sheet (compute
     μ(1,1), μ(1,2), μ(1,3) per sheet at final values)
  3. α universality across modes preserved (α_ν₂, α_ν₃ = α)
  4. Signature OK (joint three-tube bound respected)

**Deliverables.**

- `scripts/track7d_magic_shear.py` — re-solve + verification +
  ghost-ordering audit on each sheet
- findings-7.md §F42–F44 entries
- Updated baseline numbers for Track 8

**Possible outcomes.**

- **All targets met + ghost ordering + universality preserved.**
  Magic-shear baseline works.  Track 8 has a cleaner starting
  configuration.
- **Signature violation.**  Budget too tight at these (ε, s)
  values.  Shrink ε further.
- **α universality breaks.**  Structural fix doesn't survive
  the geometry change.  Needs investigation (likely ν
  mode-symmetry interaction we didn't anticipate).
- **Ghost ordering fails.**  Unexpected — magic shear is
  algebraically guaranteed to make target mode lightest.
  Sanity check.

---

### Track 7c — Inter-sheet shear compatibility check (post-Track 7b)

**Goal.**  Quick sanity check: does activating Ma cross-sheet σ
entries (R54's σ₄₅ = −0.18 and σ₄₆ = +0.10, or analogs) break
Track 7b's clean α universality?

**Strategy.**  Take the Track 7b baseline metric (α universal to
floating point across all three sheets).  Add cross-sheet σ
entries at (a) small values (0.01), (b) R54's historical values
(±0.18, ±0.10), (c) several intermediate values.  At each
configuration, compute α_e, α_p, α_ν₁/₂/₃ and check signature.
Optionally re-solve (L, k) to absorb any shift.

**Acceptance.**  If α universality survives activation of
cross-sheet σ (within tolerance reachable by re-solve), we have
a usable free knob for compound-mode fine-tuning.  If it breaks,
we need to extend the structural prescription to cover the
cross-sheet case (a natural follow-up — likely σ_cross ↔ ℵ
entries by analogy with σ_ra).

---

### Track 7b — Re-solve on the augmented metric (magnitude lock)

**Goal.**  Track 7 demonstrated that adding σ_ra entries collapses
the ν-mode spread from 28% to 0% — but the converged value drifted
to 1.0885α (not exactly α) because we used Track 6's k values
unchanged on a metric that had changed.  Track 7b re-solves the
joint system on the augmented metric to bring the magnitude back
to α exactly while preserving the structural universality.

**Strategy.**  Same six free knobs as Track 6 (L_e, k_e, L_p, k_p,
L_ν, k_ν), same six targets (three masses + α_e = α_p = α_ν₁ = α),
but with the metric builder modified to include the structural
σ_ra entries.  The σ_ra values are *not* free knobs — they're
derived from σ_ra_x = (sε)_x · σ_ta on each sheet.

**Acceptance criteria.**

- Joint solve converges with all six targets met to ≤ 1e-6.
- α_ν₂ and α_ν₃ (untargeted) come out within 1e-6 of α — i.e.,
  Track 7's structural universality is preserved at the new
  k values.
- Δm²₃₁/Δm²₂₁ ≈ 33.6 cross-check still holds.
- Final k values are the "natural-form" baseline for the
  augmented architecture, ready for Track 8 (compound modes).

---

## Next-track pool

Candidates after Track 7b.  Sequence decided as we go.

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

**h. Cross-sheet α cancellation structural prescription.**
Extend the Track 7 ring↔ℵ σ_ra = (sε)·σ_ta cancellation to
cross-sheet σ entries.  Derive (analytically or numerically)
the counter-entry relationship that cancels cross-sheet
shear-induced α leakage on the joint metric.  Prerequisite
for compound-mode search using cross-sheet σ as free knobs.

**Counting argument (Track 7d dialog):** each cross-sheet edge
creates α leakage on *both* sheets it connects.  To cancel
leakage on all three sheets simultaneously requires **all three
edges of the triangle** (e↔p, e↔ν, p↔ν) active at specific
derived values — a "3-phase" / circular arrangement.  Linear
chains (only two edges) are structurally underdetermined.
Model-E used only the p↔ν edge; it sacrificed α universality to
get neutron placement right.  Under R59 F59's universality
requirement, partial triangles are incompatible; either full
triangle with prescription, or zero cross-sheet σ.

**i. Alternative ghost-suppression mechanisms** (raised
post-Track 7c).  If we don't use magic shear on every sheet,
we need other filters for the (1, 1) and (1, 2) ghosts.
Candidates: (a) R46-style waveguide cutoff at specific ε; (b)
R61-style Majorana-pair cancellation (requires ±n_tube
partners for existence); (c) "too heavy" energy-routing
argument (R56/R57 — spatial separation cheaper than Ma
stacking).  Document as fallback in case magic-shear geometry
becomes unworkable elsewhere.

**j. ν-sheet ghost audit.**  At R61 #1 (ε=2, s=0.022), mode
(1, 0) is lighter than (1, 1) by μ calculation.  Investigate
whether (1, 0) modes are filtered in R49/R61 taxonomy
(candidate: modes with n_ring=0 may be structurally excluded
or absorbed into dark-mode classification).  Required before
claiming ν₁ is the lightest on that sheet.

**k. Z₃ confinement on the p-sheet.**  Being pursued as
Track 16.  The motivation: Track 15 left (3, 6) proton
mechanically viable but without a principled reason why
(1, 2) and (2, 4) on the same ratio ray should not be
observable as free particles.  The "three-phase power"
analogy gives a candidate mechanism — a single (1, 2)
mode has 2ω density fluctuation that cancels only when
three copies combine at 120° offsets (mathematically:
Σ_{k<N} cos(2ωt + 4πk/N) = 0 iff N ∤ 2, so N = 3 is the
minimum).  If Track 16 closes, the resulting selection
rule `free p-sheet modes require n_t ≡ 0 (mod 3)` is
derived rather than postulated, and (3, 6) has a clean
foundation for model-G.  If Track 16 fails, alternative
fallbacks are (a) postulate the Z₃ rule as a p-sheet
architectural axiom, (b) the waveguide-cutoff approach
of R47 Track 7 / pool item **i**, or (c) abandon (3, 6)
entirely.

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
