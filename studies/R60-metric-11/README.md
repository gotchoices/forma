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

## Next-track pool

Candidates for the next track after Track 1.  Sequence will be
decided from Track 1's outcome.  These entries are sketches; the
chosen one will be elaborated to full-track detail when promoted.

**a. Smallest-s_e resonance solution.**  Re-solve R53's generation
resonance equation (m_μ/m_e, m_τ/m_e exact) with s_e as the
variable, looking for the smallest |s_e| compatible with the
tube↔ℵ architecture.  R53 Solution D uses s_e = 2.004 — near the
PD saturation.  A low-|s_e| solution (if it exists) unblocks R60.

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
