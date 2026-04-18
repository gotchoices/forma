# R60 Findings

Track index:

| Track | Scope | F-range | Status |
|-------|-------|---------|--------|
| 1 | Solver infrastructure — 11D metric builder, signature check, mode energy, α_Coulomb extractor, least-squares fitter + smoke tests | F1–F4 | complete |
| 2 | Electron sheet viability map — (ε_e, s_e) region where ghost-order and signature-under-R59-F59-α-knobs both hold | F5–F10 | complete |

---

## Track 1: Solver infrastructure

**Scope.**  Build and validate the primitives every later track needs:
a parametric 11D metric builder, signature check, mode-energy computation,
α_Coulomb extractor, and a thin `scipy.optimize.least_squares`-based
joint fitter.  No physics conclusions — only tested machinery.

Script: [scripts/track1_solver.py](scripts/track1_solver.py).  Run via
`.venv/bin/python studies/R60-metric-11/scripts/track1_solver.py`.

### Review of variables

- **11D metric** — the 11-index layout is (ℵ, p_t, p_r, e_t, e_r, ν_t,
  ν_r, S_x, S_y, S_z, t).  Time index `I_T = 10` carries the Lorentzian
  −1 diagonal; the three S indices are Euclidean +1; the ℵ diagonal is
  `g_aa` (default 1); the 6-index Ma slice `MA_SLICE = [1..6]` holds the
  three 2×2 sheet blocks.
- **Sheet block (dimensionless)** — for a sheet with aspect ratio ε,
  shear s, and diagonal scale k, the 2×2 dimensionless block is
  `k · [[1, s·ε], [s·ε, 1 + (s·ε)²]]`.  Derived from
  `G_phys = B^T B` with `B = diag(L_tube, L_ring)(I + [[0, s], [0, 0]])`
  then normalized by `L_i L_j`.
- **k (diagonal scale)** — R59 F53 found α_Coulomb scales roughly as 1/k²
  at fixed σ_ta.  The model-E normalization is k = 1; the R59 F59
  natural-form α match requires k = 1/(8π) ≈ 0.040 on the charged sheets.
- **σ_ta** — tube↔ℵ off-diagonal magnitude.  Signed per sheet: +1 for e,
  −1 for p, 0 for ν (charge neutrality).  Natural value √α (R59 F59).
- **σ_at** — ℵ↔t off-diagonal.  Natural value 4πα (R59 F59).
- **α_Coulomb extraction** — `Q = (ñ_Ma · G⁻¹[Ma, t]) × (−G⁻¹[t, t])`,
  then `α = Q² / (4π)`.  This is the R59 track3g formula; it reports the
  effective Coulomb coupling that would be felt in S by a static mode.

### F1. T1 — 11D reproduces model-E masses when α knobs are off

Build the 11D metric with model-E Ma parameters (R53 Solution D on e,
R54 on p, R49 Family A on ν), all α-coupling knobs set to zero, k = 1
on every sheet.  Compute mode energies of the electron (1, 2, 0, 0, 0, 0)
and proton (0, 0, 0, 0, 1, 3) on the Ma subspace.

| Quantity | Expected | Computed | Relative error |
|----------|----------|----------|----------------|
| E(electron) | 0.5109989461 MeV | 0.5109989461 MeV | 1.7 × 10⁻¹¹ |
| E(proton)   | 938.272 MeV      | 938.272 MeV      | 1.2 × 10⁻¹⁶ |
| signature_ok | True (1 neg eig) | True | — |

**Interpretation.**  The 11D embedding does not disturb model-E's mass
predictions when the new dimensions (ℵ, t, S) are decoupled from Ma.
The sheet block formula `k · [[1, sε], [sε, 1 + (sε)²]]` reproduces
model-E's `μ_sheet = √((n_t/ε)² + (n_r − s·n_t)²)` exactly.

**What this means.**  The Ma-mass arm of every later track will reduce
to the model-E computation when the α knobs are off, and perturbatively
shift as they are turned on.  Any mass-prediction disagreement with
model-E will come from α coupling, not from the 11D wrapping.

### F2. T2 — R59 F59 natural-form point gives α_Coulomb = α to 60 ppm

Build the clean metric R59 Track 3g used (shearless Ma, k = 1/(8π) on
charged sheets, g_aa = 1, σ_ta = √α with signs +/−/0, σ_at = 4πα),
compute α_Coulomb for the electron and proton reference modes.

| Quantity | Value | Ratio to α |
|----------|-------|------------|
| α_e      | 0.007297798 | 1.000061 |
| α_p      | 0.007297798 | 1.000061 |
| α_e / α_p | 1.000000000 | — |
| α_ν      | 0 (exact)   | 0 |

**Interpretation.**  The α extractor reproduces R59 F59 at 60 ppm —
matching the R59 headline result to the reported precision.  Universality
is exact to floating point (α_e = α_p to 10+ digits), consistent with
R59 F45 (structural universality from |n_tube| = 1).  ν is exactly
neutral because sign_nu = 0 zeros the ν-tube↔ℵ entry.

**What this means.**  The α arm of every later track starts from a
validated extractor and a known reference point.  Any deviation from
60 ppm in future fits is signal about the geometry, not about the tool.

### F3. T3 — F41 signature rejection on shear-saturated e-tube

Build the model-E metric plus tube↔ℵ coupling at σ_ta = √α and σ_at = 4πα.
Expect signature failure (R59 F41: model-E's s_e = 2.004 saturates the
e-tube against any additional tube coupling).

| Configuration | Neg eigs | signature_ok |
|---------------|---------:|:-------------|
| Model-E Ma + σ_ta = √α, σ_at = 4πα | 2 | False |
| Model-E Ma + σ_ta = σ_at = 0.01    | 2 | False |

**Interpretation.**  Any tube↔ℵ coupling — even at σ = 0.01 — pushes a
second eigenvalue negative on model-E geometry.  This is R59 F41
exactly: the shear-saturated e-tube will not tolerate additional ℵ
coupling on top of the in-sheet shear.

**What this means for R60.**  R60 cannot run the R59 F59 α architecture
directly on model-E.  Either (i) find a smaller s_e that preserves the
lepton-generation ratios (pool item **a**), or (ii) move α to a
different architecture (pool item **g**).  This track confirms the
obstruction computationally; it does not yet point to a resolution.

### F4. T4 — Single-knob solve of L_ring_e converges cleanly

Start from model-E Ma geometry but with L_ring_e = 1000 fm (deliberately
bad initial guess, two orders of magnitude off).  One residual (m_e
fractional error), one free knob (L_ring_e), bounds [1, 10⁶] fm.

| Quantity | Closed-form | Solver result | Relative error |
|----------|-------------|---------------|----------------|
| L_ring_e | 11.88209756 fm | 11.88209756 fm | 1.6 × 10⁻¹⁰ |
| residual(m_e) | 0 | −1.4 × 10⁻¹⁰ | — |

scipy.optimize.least_squares converged to the analytical
`L_ring = 2π ℏc · μ / m · √k⁻¹` value at floating-point precision,
reaching `gtol` termination.

**Interpretation.**  The fitter wraps scipy correctly, responds to a
poor initial guess, and hits the analytical answer to floating-point
precision on a target with a known closed form.

**What this means.**  The solver can be trusted for well-posed
single-knob fits.  Multi-knob fits will be tested once later tracks
start using them against particle targets.

### Sanity (not part of acceptance): electron at α-on

An auxiliary run confirms the solver works end-to-end with α coupling
active: clean Ma (s=0), k_e = k_p = 1/(8π), σ_ta = √α, σ_at = 4πα,
eps_e fixed at 1.5, fit L_ring_e against m_e.

| Quantity | Value |
|----------|-------|
| L_ring_e (fit) | 25643.36 fm |
| E_e (at fit)   | 0.5109989462 MeV (target 0.5109989461) |
| α_e / α       | 1.00006 |

Not a physics claim.  Only shows the pipeline composes: α extraction,
mass computation, and fitting all work together inside one Params
construction.  The eps_e = 1.5 choice is arbitrary; a physics run
would vary it too.

## Track 1 status

Complete.  All four smoke tests pass.  The 11D metric builder,
signature check, mode-energy formula, α_Coulomb extractor, and
least-squares fitter are validated against known reference points
(model-E masses, R59 F59, R59 F41).

### What's ready for next tracks

- `build_metric_11(params) → 11×11 array`
- `signature_ok(G) → bool`
- `mode_energy(G, L, n11) → float MeV`
- `alpha_coulomb(G, n11) → float`
- `solve(params0, free, targets) → SolveResult`
- `Params` dataclass with model-E defaults and R59 α-knob fields

All importable from
[scripts/track1_solver.py](scripts/track1_solver.py).

### What's not yet built

- Coupled mass shift from α-on: the mode energy currently uses the Ma
  subspace in isolation.  R59 F13 reported ~1.3% shift when ℵ coupling
  turns on; this back-reaction must be modeled before any α-on mass
  target is interpreted physically.  Deferred until a later track
  actually needs it — most "find a particle at α-off, then check mass
  shift at α-on" tracks can use the current primitive.
- Cross-sheet σ (R54 neutron-region entries σ₄₅, σ₄₆) is supported by
  the Params interface but not yet exercised by a smoke test.
- No ν-sheet mass calibration yet — L_ring_ν is a 1 fm placeholder.
  Later tracks that touch neutrino physics will need to add that.

### Decision point

Next track pool items (a, b, c, d, e, f, g) in
[README.md](README.md) are unchanged.  Recommendation: pick **a**
(smallest-s_e resonance solution) next — it directly targets the F3
obstruction.  If a low-|s_e| solution that preserves m_μ/m_e and
m_τ/m_e exists, F3 is unblocked and Tracks c–e become straightforward.
If it doesn't, we pivot to **g** (alternative α architecture).

---

## Track 2: Electron sheet viability map

**Scope.**  Characterize the electron sheet alone as a 2D
parameter problem in (ε_e, s_e).  Report the region where (1,2) is
the lightest charged e-sheet mode (ghost-order favorable) and the
region where the R59 F59 α knobs preserve Lorentzian signature,
then take their overlap.  No muon, no tau, no mass ratios — those may
require ν and p sheets (Tracks 3–4).

Script: [scripts/track2_electron_sheet.py](scripts/track2_electron_sheet.py).

### Review of variables

- **Region A (ghost-order favorable)**: `μ(1,1) ≥ μ(1,2)` on the
  single-sheet energy formula.  Closed-form reduction: `s ≥ 1.5`
  (independent of ε).  A half-plane on the (ε, s) grid.
- **Region B (signature-OK)**: the 11D metric with the R59 F59 α
  knobs (k_e = 1/(8π), σ_ta = √α on e-tube, g_aa = 1, σ_at = 4πα)
  has exactly one negative eigenvalue.  ν and p sheets are
  uncoupled identity placeholders.
- **Margin to cliff**: the smallest positive eigenvalue of the 11D
  metric.  Larger = more room before signature fails.

### F5. Smoke cross-checks reproduce prior results

At R53 Solution D (ε_e = 397.074, s_e = 2.004200):
- `μ(1,2) = 0.004897`, `μ(1,1) = 1.004203` — (1,2) is 205× lighter
  than (1,1), consistent with R53's claim that the electron is at
  a shear cancellation point (ring detuning ≈ 0.004).
- With the R59 F59 α knobs on, signature has 2 negative
  eigenvalues — reproduces Track 1 T3 exactly.

At clean (ε_e = 1, s_e = 0), R59 F59 α on: signature OK with
`min_pos = 0.0323` — same order of magnitude as R59's "small but
positive" margin.

### F6. Region A (ghost order): the analytical boundary s = 1.5

Grid scan confirms `μ(1,1) ≥ μ(1,2)` holds iff `s_e ≥ 1.5`,
independent of ε.  Derivation:

    (1 − s)² ≥ (2 − s)²  ⇔  1 − 2s ≥ 4 − 4s  ⇔  s ≥ 3/2

1891 of 7381 scan points (25.6%) fall in Region A.

### F7. Region B (signature under α knobs): the hyperbolic boundary s·ε ≤ 3/√2

Grid scan + bisection refinement shows the signature cliff is at
an **exact** product `s·ε = 3/√2 ≈ 2.1213`, i.e. `(s·ε)² ≤ 9/2`.

Boundary bisection (s = 1.5 side):

| s    | ε_max at signature cliff | s·ε |
|-----:|:--------:|:------:|
| 1.50 | 1.4140 | 2.121 |
| 1.60 | 1.3256 | 2.121 |
| 1.70 | 1.2476 | 2.121 |
| 1.80 | 1.1783 | 2.121 |
| 2.00 | 1.0605 | 2.121 |
| 2.50 | 0.8484 | 2.121 |
| 3.00 | 0.7070 | 2.121 |

Boundary bisection (fixed-ε side):

| ε    | s_max at signature cliff | s·ε |
|-----:|:--------:|:------:|
| 0.30 | 7.0698 | 2.121 |
| 0.50 | 4.2419 | 2.121 |
| 1.00 | 2.1209 | 2.121 |
| 1.50 | 1.4140 | 2.121 |
| 2.00 | 1.0605 | 2.121 |

The constant is consistent to 4+ digits across an order of
magnitude in ε — strong evidence for an exact algebraic identity
of the R59 F59 knob set, deferred to pool item **f** for
analytical derivation.

### F8. Overlap (A ∩ B) is a bounded triangular region

The two constraints together:
- ghost-order: `s ≥ 3/2`
- signature:   `s · ε ≤ 3/√2`
→ overlap:    `s ≥ 3/2` **and** `ε ≤ 3/(√2 · s) ≤ √2`.

The overlap is an open region bounded by:
- horizontal edge `s = 3/2`
- hyperbolic edge `s·ε = 3/√2`
- ε → 0 (unbounded toward thin torus)

Corner at (ε = √2 ≈ 1.414, s = 3/2).  473 of 7381 scan points
(6.4%) in the overlap.

Representative candidate points (highest signature margin first):

| ε_e | s_e | margin | μ(1,1)/μ(1,2) |
|----:|----:|-------:|---------:|
| 0.10 | 1.50 | 2.92e−2 | 1.0000 |
| 0.10 | 1.60 | 2.89e−2 | 1.0010 |
| 0.10 | 1.70 | 2.86e−2 | 1.0020 |
| 0.10 | 1.80 | 2.83e−2 | 1.0030 |
| 0.12 | 1.50 | 2.85e−2 | 1.0000 |

Margin is essentially constant at `min_pos ≈ 0.03` for the whole
overlap — a thin "shelf" rather than a deep well.  The ghost gap
`μ(1,1)/μ(1,2)` at these points is barely above 1 (marginal
ordering) because the points sit near the `s = 3/2` edge.

### F9. Model-E (and R53) are far outside the overlap

Compare the R53 solutions to the F7 boundary `s·ε = 3/√2 ≈ 2.12`:

| Source | ε_e | s_e | s·ε | Over the boundary by |
|--------|----:|----:|----:|---:|
| R53 Solution D | 397.074 | 2.004200 |  795.9 | **375× over** |
| R53 Solution B | 330.1   | 3.003841 |  991.3 | **467× over** |
| Overlap corner | √2 ≈ 1.41 | 1.5 | 2.12 | (at cliff) |

The R59 F59 α architecture is incompatible with any fat-torus
electron geometry (ε ≫ 1).  Model-E's e-sheet parameterization
cannot be lifted into the R60 metric without breaking signature —
confirming and sharpening F3.

### F10. Interpretation and what Track 2 has and has not decided

**What Track 2 establishes.**  Track 2 passes its stated
acceptance: the overlap is nonempty.  The architecture is
viable *if* the electron sheet sits at `(ε_e, s_e)` with
`s ≥ 3/2` and `s·ε ≤ 3/√2`.  Representative candidate for
Track 3: any (ε, s) within the triangle; high-margin choices
cluster at ε ≪ 1, s just above 1.5.

**What Track 2 does not decide.**  Whether the R53 generation
mechanism (off-resonance modes (3, 8), (3, −8) on the e-sheet
producing exact m_μ/m_e and m_τ/m_e) survives at these small-ε
points.  At R53 Solution D the ratios came out exact because the
electron lives at the shear cancellation point `n_r = s · n_t`
with large ε (so the `(n_r − s·n_t)²` term dominates and
cancels).  At ε ≤ 1.4, the `1/ε²` term is comparable or larger
and the mode spectrum spacing is different.  Whether any
single-sheet generation mechanism exists in this regime is an
open question for a later track — **not** a Track 2 blocker by
the agreed scope.

**What Track 2 implies for model-F.**  A model built on the R59
F59 α architecture must use a thin or near-symmetric electron
torus (ε_e ≤ √2, with shear s_e ≥ 3/2).  This is a significant
structural change from model-E's ε_e = 397.  Three possibilities
for the generation mechanism in this regime:

1. **Generations from e-sheet alone in the thin-torus regime.**
   Requires identifying modes whose energy ratios match
   m_μ/m_e = 206.768 and m_τ/m_e = 3477.23 at `(ε_e, s_e)`
   inside the overlap.  To be tested.
2. **Generations from compound modes.**  Per model-E's
   inventory, μ = e+ν compound and τ = all three sheets.  These
   emerge once the ν and p sheets are sized (Tracks 3, 4).  No
   requirement that e-sheet alone explain generations.
3. **Generation mechanism replaced entirely.**  Different
   physics in this regime may bear different modes as lowest
   energies.

## Track 2 status

Complete.  Overlap is a bounded triangular region in (ε_e, s_e),
characterized by the exact inequalities

    s_e ≥ 3/2,   s_e · ε_e ≤ 3/√2.

Model-E's e-sheet parameters violate the second inequality by
~375×.  Track 2 passes acceptance but exposes a significant
structural constraint: the R59 F59 α architecture requires a
thin-torus (ε ≤ √2) electron geometry.

### What's ready for Track 3

- The overlap triangle as the allowed (ε_e, s_e) region for any
  downstream model-F candidate.
- The sharp `s·ε = 3/√2` boundary as a known analytical identity
  (derivation deferred to pool item **f**).
- Representative candidate points at the high-margin corner
  (ε ~ 0.1, s ~ 1.5–2.0) if Track 3 needs a starting (ε, s).

### What's not yet built

- ν-sheet sizing (Track 3).  Must also satisfy `s·ε` signature
  constraint — open whether ν-sheet ghost-order concerns apply
  since ν-tube is uncoupled in the R59 F59 architecture.
- Generation-mechanism question: whether m_μ/m_e and m_τ/m_e
  can be realized by any mechanism compatible with the overlap.
  Deferred pending Tracks 3, 4 (to see if compound modes give
  them "for free").

### Decision point

Recommend pause here per original Track 2 agreement.  Open
questions for user to weigh before Track 3:

- **Should pool item f (analytical derivation of the s·ε = 3/√2
  boundary) run before Track 3?**  Might reveal whether the
  boundary is an α-architecture constant or a deeper structural
  identity.  Cheap.
- **Does the thin-torus electron (ε ≤ √2) conflict with any
  model-E result we care about?**  R46's electron waveguide used
  ε = 0.5 (thin-torus was the working assumption in model-D).
  R53 moved to ε = 397 specifically for generations.  If
  generations are allowed to come from compounds, thin-torus is
  fine and we proceed to Track 3.
- **Track 3 (ν-sheet) framing:**  start from small-margin
  corner of overlap (ε_e ≈ 0.1, s_e ≈ 1.5) or an analytically
  nicer point (e.g., ε_e = 1, s_e = 1.5)?  Pick before running.
