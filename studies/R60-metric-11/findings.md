# R60 Findings

Track index:

| Track | Scope | F-range | Status |
|-------|-------|---------|--------|
| 1 | Solver infrastructure — 11D metric builder, signature check, mode energy, α_Coulomb extractor, least-squares fitter + smoke tests | F1–F4 | complete |
| 2 | Electron sheet viability map — (ε_e, s_e) region where ghost-order and signature-under-R59-F59-α-knobs both hold | F5–F10 | complete |
| 3 | Proton sheet viability map — (ε_p, s_p) region under R59 F59 α with e-sheet active at several Track 2 anchors | F11–F16 | complete |
| 4 | Per-sheet diagonal compensation — joint solve for (L_e, k_e, L_p, k_p) hitting (m_e, m_p, α_e=α, α_p=α) | F17–F21 | complete |
| 5 | Proton on shearless-electron baseline + analytical α-decoupling locus | F22–F26 | complete |
| 6 | Joint e+p+ν solver with ν architecturally coupled (sign_nu=+1) on R61 candidate ν-sheet geometries | F27–F31 | complete |
| 7 | Ring↔ℵ structural cancellation test — adds σ_ra = sε·σ_ta to dissolve shear-induced α mode-dependence | F32–F34 | complete |
| 7b | Re-solve on augmented metric — magnitude lock + cross-check Track 7's structural prediction survives | F35–F37 | complete |

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

---

## Track 3: Proton sheet viability map

**Scope.**  Same idea as Track 2 but for the proton sheet.
Characterize the (ε_p, s_p) range where R59 F59 α is signature-OK
with the proton sheet active alongside the e-sheet.  Test multiple
e-sheet anchors to see if the e-sheet choice changes the p-region.
Verify R59 F45 universality (α_p / α_e ≈ 1) on the joint metric.
L_ring_p derived from m_p (closed form); free knobs only ε_p, s_p.

Script: [scripts/track3_proton_sheet.py](scripts/track3_proton_sheet.py).

### Review of variables

- **Region C** — p-sheet alone, e-sheet uncoupled (sign_e = 0).
  Analogue of Region B from Track 2 but for the proton.
- **Region D** — joint e+p signature-OK with both sheets active
  at R59 F59 α knobs (sign_e = +1, sign_p = −1, |σ_ta| = √α
  on both tubes).  Depends on the chosen e-sheet anchor.
- **R59 F45 universality** — claim that α_e / α_p = 1 is
  structural at k_e = k_p = 1/(8π) for any |n_tube| = 1 mode.
  Demonstrated in R59 on a *shearless* clean Ma metric.  Track 3
  tests whether it survives nonzero internal shears.

### F11. Smoke check reveals immediate universality breakdown

Joint metric with e-sheet at (ε_e=1, s_e=3/2) and p-sheet at
model-E (ε_p=0.55, s_p=0.162037), R59 F59 α knobs on:

| Quantity | Value | Ratio to α |
|----------|-------|------------|
| α_e | 3.45 × 10⁻³ | 0.473 |
| α_p | 3.03 × 10⁻² | 4.154 |
| α_p / α_e | 8.78 | (R59 F45 said 1.0) |

Signature OK, masses exact by L_ring derivation.  But
**universality is broken by nearly an order of magnitude, and α
magnitude on each sheet is far from observed**.  R59 F59's
"structural universality" was a property of the shearless clean
Ma metric.  As soon as nonzero internal shears (s_e ≥ 3/2 from
Track 2 ghost order; s_p arbitrary) are introduced, both
universality and α magnitude break.

This is a **major negative finding** for the R60 program.  See
F15 for the mechanism and F16 for implications.

### F12. Region C (p-sheet alone) is identical in form to Region B

Boundary refinement on the p-sheet-only configuration
(sign_e = sign_nu = 0, sign_p = −1) reproduces the Track 2
hyperbolic bound exactly:

| s_p | ε_p_max at cliff | s_p · ε_p |
|----:|:--------:|:------:|
| 0.50 | 4.2419 | 2.1209 |
| 1.00 | 2.1209 | 2.1209 |
| 1.50 | 1.4140 | 2.1209 |
| 2.00 | 1.0605 | 2.1209 |
| 2.50 | 0.8484 | 2.1209 |
| 3.00 | 0.7070 | 2.1209 |

**Region C boundary**: `s_p · ε_p ≤ 3/√2 ≈ 2.121`.

Identical to Region B (Track 2 e-sheet alone).  The single-sheet
signature bound is sheet-symmetric — depends only on |σ_ta|, not
on which tube it's on.  Region C covers 32.4% of the scan grid
(same as Region B).

### F13. Region D (joint e+p) is anchor-dependent and tighter

Joint signature scans for four representative e-sheet anchors:

| e-anchor | (s_e ε_e) | s_p · ε_p bound | Region D pts | Model-E p (0.55, 0.162) included? |
|----------|-----------|-----------------|-------------:|:---------------------------------:|
| (1.0, 1.5) corner-1.0   | 1.5  | **1.1173** | 1897 (25.7%) | yes (margin 2.6e-3) |
| (1.4, 1.5) corner-edge  | 2.1  | **0.0**    | 0 (0.0%)     | **no** |
| (0.1, 1.5) high-margin  | 0.15 | **1.8644** | 2293 (31.1%) | yes (margin 2.4e-2) |
| (0.5, 2.0) mid-shear    | 1.0  | **1.5806** | 2161 (29.3%) | yes (margin 8.1e-3) |

**Two structural findings:**

(a) **The joint bound is consistently lower than 2.121**, and it
varies sharply with the e-anchor.  The "corner-edge" anchor
(near the Track 2 signature boundary) collapses Region D to
empty.  Choosing the e-anchor near Track 2's hyperbola eats all
the margin.

(b) **The model-E p-sheet (0.55, 0.162) is included in 3 of 4
e-anchors** with various margins.  The architecture *does*
admit model-E's proton geometry — but only when the e-sheet sits
comfortably inside Track 2's overlap, not at its edge.

### F14. The joint signature bound has an exact algebraic form

Combining the four e-anchor measurements with the single-sheet
result (Region C boundary = 2.121² = 9/2):

| (s_e ε_e)² | (s_p · ε_p)²_max | Sum |
|------------|------------------|-----|
| 0.0000  | 9/2  = 4.500 | 4.500 |
| 0.0225  | 1.864² = 3.475 | 3.498 |
| 1.0000  | 1.581² = 2.499 | 3.499 |
| 2.2500  | 1.117² = 1.249 | 3.499 |
| 4.4100  | (infeasible)   | — |

When *both* tubes carry σ_ta, the joint signature bound is

    (s_e · ε_e)² + (s_p · ε_p)² ≤ **7/2**

(consistent to 4 digits across the four anchors tested).  The
single-active-tube bound is 9/2; adding a second active tube
costs exactly **1**.  Likely an exact algebraic identity arising
from the specific R59 F59 knob set (k = 1/(8π), σ_ta = √α,
σ_at = 4πα, g_aa = 1).  Derivation deferred to pool item **f**.

The "1" budget per tube has a natural interpretation: each
σ_ta = √α coupling pulls one unit of "negative-eigenvalue
budget" from the Lorentzian t direction.  At zero coupling, the
9/2 bound is the full budget; each additional active tube spends
one unit.

For three coupled tubes (e + p + ν, if we ever turn on
sign_nu = ±1) the predicted bound would be (s_e ε_e)² + (s_p
ε_p)² + (s_ν ε_ν)² ≤ 5/2.  In R59 F59 the ν-tube is uncoupled,
so this remains a prediction to test only if/when ν coupling is
considered.

### F15. α universality and α magnitude both fail under shears

Universality and magnitude reported across (e-anchor) × (p-candidate)
combinations on the joint metric:

| e-anchor | p-candidate | α_e/α | α_p/α | α_p/α_e |
|----------|-------------|------:|------:|--------:|
| (1.0, 1.5) | model-E (0.55, 0.162)  | 0.473 |  4.154 | 8.78 |
| (1.0, 1.5) | high-margin (0.1, 0.1) | 0.468 |  7.043 | 15.06 |
| (0.1, 1.5) | model-E (0.55, 0.162)  | 0.531 |  0.558 | 1.05 |
| (0.1, 1.5) | (1.0, 1.5)             | 4.045 | 12.107 | 2.99 |
| (0.1, 1.5) | high-margin (0.1, 0.1) | 0.529 |  0.953 | 1.80 |
| (0.5, 2.0) | model-E (0.55, 0.162)  | ~0    |  1.071 | huge (numerical) |

**Three observations:**

1. **R59 F45 universality breaks immediately** when shears are on.
   Best ratio observed (0.1, 1.5)e + (0.55, 0.162)p gives
   α_p / α_e = 1.05 — better than 8.78 but still *not* structural.
2. **α magnitude is wrong** on every test point.  α_e ranges from
   0.47×α to 4.05×α; α_p from 0.56×α to 12.1×α.  Neither is
   close to R59 F59's clean-metric value of 1.000061×α.
3. **Mechanism: ring-mediated indirect t coupling.**  R59 F45
   universality required the only Ma-t coupling to come through
   tube↔ℵ entries.  With shear `s·ε ≠ 0`, the ring inherits
   indirect t coupling via the sheet block's `(ring, tube)`
   off-diagonal `s·ε` (R59 F43 noted this in a different
   context).  The ring contribution scales with `n_ring / L_ring`,
   which differs between sheets (electron `n_er = 2`, proton
   `n_pr = 3`, with different L's), so the ring leakage is
   species-dependent.  Universality dies.

The (0.5, 2.0)e + model-E p case shows α_e numerically zero —
likely the shear-induced ring leakage cancels the tube
contribution exactly at this geometry.  Catastrophic for the
electron's α extraction; symptomatic of the bigger problem.

### F16. Track 3 status and what this means for R60

Track 3 passes its **stated** acceptance: Region D is nonempty for
3 of 4 e-anchors, model-E's p-sheet is included in 3 of 4, the
joint bound is characterized analytically (F14).  But the
**physically more important** finding is F15: the R59 F59
architecture's α universality and magnitude do **not** survive
internal shears.  This was an unstated assumption of R60 and is
now refuted.

**What R60 has learned through Track 3:**

1. The R59 F59 architecture works only on a *shearless* Ma metric.
2. Particle spectrum requires shears (electron generations, ghost
   ordering, proton mode placement).
3. **These two conditions are incompatible.**  Either α universality
   and magnitude are sacrificed (Track 3's actual result), or
   shears are sacrificed (no spectrum).

**What's still possible:**

- **Re-tune the α knobs in the presence of shears.**  R59 F59's
  natural-form values (k = 1/(8π), σ_ta = √α, σ_at = 4πα) were
  found by scanning a *shearless* metric.  In R60, with shears,
  a different combination might restore universality and
  magnitude.  Searching for it is a new track (call it
  pool item **h** — shear-aware α tuning).
- **Re-derive the joint-bound identity** (F14) analytically.
  A clean derivation might suggest a per-sheet renormalization
  that restores universality.  Pool item **f**.
- **Try smaller shears.**  At low (s ε), F15 shows universality
  drifting back toward 1.  The high-margin anchor (0.1, 1.5)e
  + model-E p gave α_p/α_e = 1.05, only 5% off.  Maybe a
  parameter region exists where shears are large enough for
  ghost order but small enough that R59 F59 universality
  approximately survives.

**What's likely dead:**

- **R59 F59's claim of *structural* universality does not extend
  to the model-E spectrum.**  At best we can recover *approximate*
  universality at small (s ε); structural exactness is gone.
- **The natural-form value σ_ta = √α may not give α magnitude
  on shears.**  σ_ta will need to be tuned per shear configuration
  if α magnitude is required.

### Status

Complete.  Scope deliverables met.  But the architectural surprise
in F11/F15 is significant enough that R60 needs a strategy
decision before Track 4 (ν-sheet).  Pause here.

### Decision point

Three paths forward, in order of cost:

**(a) Accept approximate universality and continue.**  At small
(s ε) anchors, α_p/α_e is within ~5% of 1.  If we can find a
spectrum-compatible region where this holds for all charged
particles, the model-F program is intact (with weaker α claims).
Next: Track 4 = ν-sheet on the same lines, then a wider survey.

**(b) Pivot to shear-aware α retuning.**  Pool item **h**: scan
the α-knobs (k, σ_ta, σ_at, g_aa) in the presence of model-E-like
shears, looking for a configuration where α_e = α_p = α holds
even with shears on.  If found, R60 has a new natural-form
target.  If not, we know R59 F59 is irretrievably
shear-incompatible.

**(c) Pivot to analytical derivation first.**  Pool item **f**:
derive (i) the joint signature bound (s_e ε_e)² + (s_p ε_p)² ≤
7/2 in closed form, and (ii) the universality-breaking formula.
Could reveal whether (b) has any chance of succeeding before we
spend search effort on it.

I'd argue for **(c) → (b) → (a)**: cheap analytical work first,
then targeted search informed by it, then either continue or
adapt.  But this is a strategic call — your decision.

---

## Track 4: Per-sheet diagonal compensation for α universality

**Scope.**  Test whether allowing per-sheet `k_e ≠ k_p` (instead
of R59 F59's identical assumption) recovers both α universality
(α_e = α_p = α) and α magnitude (= observed α) on a metric with
internal shears active.  Free knobs: (L_ring_e, k_e, L_ring_p,
k_p).  Targets: (E_e=m_e, E_p=m_p, α_e=α, α_p=α).  Joint solve
via `scipy.optimize.least_squares` on the Track 1 solver; per-sheet
solves run in parallel as diagnostic.

Script: [scripts/track4_diagonal_compensation.py](scripts/track4_diagonal_compensation.py).

### F17. Smoke 1 — joint solver recovers R59 F59 on shearless clean

At (ε_e, s_e, ε_p, s_p) = (1, 0, 1, 0) the joint 4×4 solve
recovers `k_e = k_p = 3.978951e-2 ≈ 1/(8π)` to floating-point
precision, with all residuals at 10⁻¹⁴.  α_e/α = α_p/α = 1.000
exactly, masses exact.  Confirms the solver is well-posed and
finds the known answer without prompting.

### F18. Smoke 2 (Track 3 best) — per-sheet compensation works cleanly

At (ε_e, s_e, ε_p, s_p) = (0.1, 1.5, 0.55, 0.162037) — Track 3's
best universality point (1.05 ratio at uniform k):

| Quantity | Per-sheet solve | Joint solve | R59 F59 ref |
|----------|----------------|-------------|-------------|
| k_e | 2.572e-2 (0.646× nat) | **3.277e-2 (0.824× nat)** | 3.979e-2 |
| k_p | 2.607e-2 (0.655× nat) | **3.359e-2 (0.844× nat)** | 3.979e-2 |
| k_e / k_p | 0.987 | **0.976** | 1.0 |
| α_e/α at solve | 1.000000 | 1.000000 | — |
| α_p/α at solve | 1.000000 | 1.000000 | — |
| Universality | exact | exact | — |
| Sig OK | yes | yes (margin 2.6e-3) | — |

**Three observations:**

1. **Per-sheet diagonal compensation works.**  The user's
   hypothesis is confirmed at this point: tuning k per-sheet to
   compensate for shear-induced α distortion gives α_e = α_p = α
   exactly with signature preserved.

2. **The joint solve gives different k values than the
   independent per-sheet solves.**  Independent solves push k
   ~35% below natural; joint solve only ~17% below.  The
   difference is the cross-sheet contamination — each sheet's
   α extraction depends on the joint inverse metric, so the
   "right" k for each sheet depends on the other sheet too.
   Joint solve is the correct one to trust.

3. **k_e/k_p stays close to 1 at this point.**  R59 F59's
   identical-k assumption is approximately preserved (0.976
   ratio).  This isn't always the case — F20 shows it can vary
   wildly elsewhere.

### F19. Stress + pathology — two distinct failure modes

**Stress (Track 3 worst, ε_e=1.0, s_e=1.5, ε_p=0.55, s_p=0.162):**
Joint solve fails — converges at residual 100 (signature penalty)
because no (k_e, k_p) restores α magnitude without breaking
signature.  At this point `s_e · ε_e = 1.5` puts the e-sheet near
Track 2's hyperbolic boundary; the joint signature budget (F14)
collapses too tight for k retuning.  **Failure mode: signature
breach.**

**Pathology (ε_e=0.5, s_e=2.0, ε_p=0.55, s_p=0.162):**  Joint
solve "converges" but with α_e/α = 0 stuck at zero, residual −1.
Per-sheet e-only solve confirms α_e = 0 at *any* k_e — there is
no k that restores it.

**Mechanism:** the electron mode (1, 2) at `s_e = 2 = n_r/n_t` is
exactly on the shear cancellation point.  R53's argument was that
this makes the electron the lightest charged mode (μ → 1/ε
because the ring detuning vanishes).  We now find that **the same
condition makes Q_e = 0** — the e-tube and shear-induced e-ring
contributions to G⁻¹[:, t] cancel for the (1, 2) mode.

So the mechanism that produces R53's electron lightness is **the
same mechanism that decouples the electron from S** under the
R59 F59 architecture.  Profound and probably general:
*generation resonance ↔ electromagnetic decoupling on the same
sheet.*

This is a structural finding worth its own follow-up — flagged
as a candidate for a focused study (perhaps "R53/R59
incompatibility theorem"); deferred for now.

**Failure mode: structural sign-flip cancellation.**  No k can
rescue.

### F20. Grid map — per-sheet k is NOT a function of own (ε, s) alone

3×3×3×3 grid scan (81 points) over (ε_e, s_e) ∈ {0.1, 0.5, 1.0} ×
{1.5, 2.0, 2.5} and (ε_p, s_p) ∈ {0.1, 0.55, 1.0} × {0.1, 0.5,
1.0}.  **54 of 81 points (66%) converge cleanly** with α_e = α_p
= α exact and signature OK.

**Failure clusters:**

- All `(ε_e=1.0, s_e=2.0)` and `(ε_e=1.0, s_e=2.5)` — signature
  breaks (`s_e · ε_e ≥ 2.0`, near or over Track 2 boundary).
- All `(ε_e=0.5, s_e=2.0)` — α_e = 0 cancellation (the F19
  pathology generalized to ε_e = 0.5).

**k_e dependence on cross-sheet parameters.**  For (ε_e=0.1,
s_e=1.5) at fixed e-anchor across 9 different (ε_p, s_p)
combinations: k_e values range 3.10e-2 to 5.16e-2 — **54%
spread**.  The joint k_e is *not* a clean function of (ε_e, s_e)
alone; it depends meaningfully on the other sheet via shared ℵ.

Same pattern for k_p, with even larger spread (~200% across
e-anchors at fixed (ε_p, s_p)).

**Implication.**  R59 F59's `k = 1/(8π)` was a *global* natural
constant on a clean metric.  In R60 with shears, k is a
*per-configuration* derived value with no clean closed form in
terms of one sheet's (ε, s) alone.  The per-sheet compensation
mechanism works — but the values aren't elegantly determined.

### F21. Net of Track 4 — partial rescue, real but not clean

**What's positive:**

- **Per-sheet diagonal compensation rescues α universality and
  magnitude in 66% of tested (ε, s) configurations.**  R59 F59's
  α architecture is more general than its clean-metric demonstration
  suggested — it can absorb shears via per-sheet k retuning.
- **Track 3's best point (0.1, 1.5)e + (0.55, 0.162)p is fully
  rescued.**  Joint solve gives an exact, signature-OK
  configuration with both α targets met and k_e/k_p close to 1.
- **R59 F59 reproduces exactly at the shearless reference.**

**What's negative:**

- **k is no longer a single global constant.**  Each
  configuration has its own per-sheet k values, and they depend
  on the joint geometry (54% spread for k_e at fixed (ε_e, s_e)
  across different p-sheets).  The "natural-form" elegance of
  R59 F59's `1/(8π)` is lost in the joint setting.
- **A structural pathology exists at the R53 generation
  resonance.**  Whenever `s · ε = n_r/n_t · ε` for the
  reference mode, that sheet's α_Coulomb cancels to zero and no
  k can restore it.  Likely general: **the R53 generation
  mechanism and the R59 α architecture are partially
  incompatible at the resonant point itself.**
- **Joint signature constraint (F14) bounds the viable region.**
  At `s · ε ≈ 2`, signature breaks even with k retuning.

**What this means for R60.**

- The viable (ε, s) region for model-F is narrower than Track 2/3
  suggested: it must avoid both the Track 2 signature cliff AND
  the R53-resonance α-decoupling pathology.  At minimum: stay
  *off* the strict resonance `s_e = n_r/n_t` (probably want
  `s_e` modestly above 3/2 but not equal to 2 or other integer
  ratios).
- The model-F architecture has now been validated as **viable in
  principle** at one or more configurations.  Pool item **c**
  (joint metric search across all targets) becomes much more
  tractable knowing that the α machinery rescues at most points.
- The "elegance" of R59 F59's natural-form values (k = 1/(8π))
  is downgraded from "exact constant" to "approximate at small
  shears, varies by tens of percent at moderate shears."  Still
  natural-form-ish at typical points, but not algebraic.

**Recommendation for next steps.**

The user's per-sheet hypothesis is confirmed in spirit.  Three
options:

1. **Proceed to Track 5 (ν-sheet)** with the rescue mechanism in
   hand.  Join all three sheets and solve for (k_e, k_p, k_ν,
   L_e, L_p, L_ν) against a wider target set.  Practical, builds
   on the working machinery.
2. **Pool item f (analytical derivation)** of the cancellation
   condition `Q_e = 0 at s_e = 2 with (1,2) mode`.  If derivable,
   it tells us exactly which (ε, s) curves to avoid — a
   structural map of the pathology.  Cheap, high-leverage.
3. **Investigate R53/R59 incompatibility** as a focused study.
   The discovery in F19 that generation resonance and α
   decoupling coincide is too important to leave as a footnote;
   it may have implications for whether the R53 picture survives
   in any α-coupled architecture.  Probably warrants its own
   study (R61 or sub-track).

I'd recommend **2 → 1**.  Get the analytical map of the
α-decoupling locus first (cheap), then proceed to ν-sheet with
known no-go regions marked.

---

## Track 5: Proton on shearless electron + α-decoupling locus

**Scope.**  Two complementary pieces: (Part 1) numerical scan
of the proton sheet at fixed shearless e, (Part 2) closed-form
derivation of the α-decoupling locus for any single-sheet mode.

Scripts:
- [scripts/track5_proton_shearless_e.py](scripts/track5_proton_shearless_e.py)
- [scripts/track5_decoupling_locus.py](scripts/track5_decoupling_locus.py)

### F22. Part 2 — closed-form α-decoupling locus

For a single sheet with mode (n_t, n_r) coupled to ℵ via
σ_ta = √α and to t via σ_at = 4πα (other sheets uncoupled),
the α extraction Q = 0 iff

    n_r/n_t = (s·ε) + 1/(s·ε)

equivalently  `n_t · u² − n_r · u + n_t = 0` with u = s·ε,
giving

    u = (n_r ± √(n_r² − 4 n_t²)) / (2 n_t).

Real roots exist iff `n_r² ≥ 4 n_t²`.

The result follows from cofactor expansion of the 4×4
sub-metric (e_t, e_r, ℵ, t):

    G⁻¹[e_t, t] = +σ k τ (1 + u²) / det
    G⁻¹[e_r, t] = −σ k u τ / det
    Q = (σ k τ / det) · [n_t (1+u²) − n_r u]

So Q vanishes whenever the bracket vanishes.

**Numerical verification.**  At the predicted decoupling points,
α_Coulomb returned 10⁻³¹ to 10⁻³² (zero to floating-point
precision):

| Mode | Predicted u = s·ε | Numerical α/α at predicted u |
|------|-------------------|-------------------------------|
| (1, 2) | 1.000 (single root) | 1.31e−31 ≈ 0 ✓ |
| (1, 3) | 0.382 or 2.618 | 3.29e−32 ≈ 0 (at 0.382); signature fails at 2.618 |
| (1, 1) | (no real root) | always nonzero across tested (ε, s) ✓ |

**Key practical implications:**

| Mode | Used by | Decoupling sε | Action for R60 |
|------|---------|---------------|----------------|
| (1, 1) | ν₁, ν₂ (R49 Family A) | none — never decouples | ν-sheet at (1,1) is α-safe everywhere |
| (1, 2) | electron, ν₃ (R49 Family A) | s·ε = 1 (exactly) | e-sheet must avoid sε = 1; ν₃ at sε = 1 too |
| (1, 3) | proton | s·ε ≈ 0.382 or 2.618 | p-sheet must avoid these |
| (n_t ≤ n_r/2) compound modes | μ, τ, hadrons | n_r/n_t = u + 1/u | check on a per-mode basis |

The **(1, 1) ν exemption** is structural (n_r² < 4 n_t² has no
real solution).  This is fortunate: R49 Family A's lightest two
neutrinos are (1, 1) modes, so they never decouple regardless of
ν-sheet (ε, s).  ν₃ at (1, 2) is constrained like the electron.

The locus formula is exact and computed for *single-sheet*
coupling.  In the joint multi-sheet case the precise location may
shift slightly, but Track 4 F19 and Part 1 below show the
single-sheet locus is an excellent predictor.

### F23. Part 1 — proton viability under shearless electron

Joint solve for (L_e, k_e, L_p, k_p) against (m_e, m_p, α_e=α,
α_p=α) at fixed (ε_e=1, s_e=0), scanning (ε_p, s_p) over an
11×13 grid:

- 104 / 143 grid points (72.7%) converged with all four targets
  hit at α_e = α_p = α exactly and signature OK.
- Failures cluster at (a) signature breach when sε_p ≳ 1.87
  (joint Track 4 F14 bound with shearless e: (sε_p)² ≤ 7/2,
  so sε_p ≤ √3.5 ≈ 1.87); and (b) the (1, 3) decoupling locus
  at sε_p ≈ 0.382 (e.g., (ε_p=0.770, s_p=0.50) → sε = 0.385,
  α_p falls to 0.33).
- At s_p = 0 (any ε_p): k_e = k_p = 1/(8π) exactly recovered;
  L_ring_p ranges 20–69 fm depending on ε_p.

Selected candidate proton configurations (sorted by closeness
of k values to natural 1/(8π)):

| ε_p | s_p | s·ε | k_e | k_p | L_ring_p (fm) |
|----:|----:|----:|----:|----:|--------------:|
| 0.10 | 0.00 | 0.00 | 1/(8π) | 1/(8π) | 69.2 |
| 0.55 | 0.00 | 0.00 | 1/(8π) | 1/(8π) | 23.3 |
| 1.00 | 0.00 | 0.00 | 1/(8π) | 1/(8π) | 20.8 |
| 0.10 | 0.50 | 0.05 | 4.10e−2 | 3.50e−2 | (≈ 14× scale) |
| 0.55 | 1.00 | 0.55 | 5.98e−2 | 2.05e−2 | (compensated) |

**Headline:** Q1 confirmed.  With shearless electron, the proton
sheet has a **wide viable region** at any reasonable (ε_p, s_p)
away from the signature cliff (sε > 1.87) and the (1,3)
decoupling locus (sε ≈ 0.382).  Per-sheet k compensation is
mild (~5–30%) for moderate shears, only diverges near the
pathological curves.

### F24. The "trivial baseline": shearless e + shearless p

The simplest converged point is (ε_e=1, s_e=0, ε_p=any, s_p=0):

- Both sheets shearless → no decoupling pathology, no
  signature pressure
- k_e = k_p = 1/(8π) exactly (recovers R59 F59)
- α_e = α_p = α exactly
- L_ring_e ≈ 27,200 fm, L_ring_p depends on ε_p (~20–70 fm)

This is the "no surprises" foundation for Tracks 6+.  Adding
shears (small ones) is fine; the architecture deforms gracefully.

### F25. Joint vs single-sheet locus — single-sheet is a good predictor

Track 4 F19 saw α_e = 0 at (0.5, 2.0)e + (0.55, 0.162)p.  Part 2
predicts (1, 2) decoupling at sε = 1.0; (0.5, 2.0) gives sε = 1.0.
Match.

Part 1 grid: failure points near sε_p ≈ 0.382 (e.g., (0.770,
0.50), (0.141, 2.75)) match the predicted (1, 3) decoupling
curve.  Near-misses (sε_p = 0.39 vs predicted 0.382) sometimes
converge — the curve is sharp but not perfectly knife-edged in
the joint case.

**Practical rule:** treat the single-sheet decoupling formula as
defining "no-go curves" with ~1–3% buffer on either side.

### F26. Track 5 status and what's ready for Track 6

**Completed.**

- **Closed-form decoupling locus** (F22): per-mode rule for any
  sheet.  Avoid `s·ε = (n_r ± √(n_r² − 4n_t²)) / (2 n_t)` for
  the sheet's reference mode.
- **Proton viability under shearless e** (F23): wide region with
  many candidate (ε_p, s_p) configurations, per-sheet k
  compensation works.
- **Q1 from user's proposal validated.**  The shearless-e +
  compensated-p approach gives clean configurations across most
  of the (ε_p, s_p) space.

**Ready for Track 6.**

- Choose a Track 5 candidate proton configuration as the working
  baseline (recommend `(ε_p, s_p) = (1, 0)` for maximum
  simplicity; or model-E-like `(0.55, 0)` if continuity is
  preferred).
- Add ν-sheet on the same architecture: free `(L_ν, k_ν)` and
  σ_ta on ν-tube with sign convention TBD; targets m_ν and
  α_ν = α.
- ν₁, ν₂ at (1, 1) are α-safe (never decouple); ν₃ at (1, 2)
  must avoid sε_ν = 1 — same constraint as electron.
- The joint signature bound generalizes: with three coupled
  tubes, Track 4 F14 predicts (sε_e)² + (sε_p)² + (sε_ν)² ≤ 5/2.
  Each sheet now spends one unit of the budget.  Conservative
  starting point: keep all three sheets at small sε.

### Decision point

Recommend proceeding to Track 6 (ν-sheet inclusion) using:

- e-sheet: (ε_e, s_e) = (1, 0) — shearless baseline
- p-sheet: (ε_p, s_p) = (1, 0) — also shearless baseline
- ν-sheet: TBD from R49 Family A or R61 candidates;
  carefully choose (ε_ν, s_ν) to satisfy joint signature bound
  and the per-mode decoupling avoidance for ν₁, ν₂, ν₃.

The R53 generation mechanism is now **structurally retired** for
R60 — there's no single-sheet (ε_e, s_e) that gives both (a) the
R53 generation ratios *and* (b) Track 4 universality at α.
Generations must come from compound modes per the model-E
inventory style.  Track 7 (compound modes) will revisit this.

---

## Track 6: Joint e+p+ν solver

**Scope.**  Add the ν-sheet on the same architectural footing as
e and p (sign_nu = +1, full σ_ta coupling).  Joint solve for six
free knobs (L_x, k_x for each sheet) against six targets (three
masses, three α_x = α).  Test against R61's top-4 candidate ν
geometries.

Script: [scripts/track6_three_sheet_solve.py](scripts/track6_three_sheet_solve.py).

### Review of variables

- **sign_nu = +1**: same convention as electron (R55-consistent).
  Activates the ν-tube↔ℵ entry at +√α.
- **Wide k bounds (10⁻⁶ to 10⁶)**: per the user observation that
  physical sheet ring scales span L_p ~ fm to L_ν ~ μm to mm,
  per-sheet diagonal scales should be allowed to span similarly
  wide ranges without being treated as "unnatural."
- **R61 candidates**: top-ranked ν-sheet geometries from R61's
  taxonomy, each specifying (ε_ν, s_ν) and a triplet of mode
  assignments for ν₁, ν₂, ν₃.

### F27. Smoke check — three-sheet metric is well-posed at defaults

Built the 11D metric with Track 5 baseline (e: ε=1, s=0; p: ε=1,
s=0) plus R61 #1 ν-sheet (ε=2, s=0.022) at uncalibrated R59 F59
defaults (k = 1/(8π) for all three sheets):

- **Signature OK** — exactly one negative eigenvalue (the t
  direction).  No structural breakage from adding the ν-sheet.
- Masses come out at targets by construction (L_ring derived
  from each mass at uniform k = 1/(8π)).
- α_e/α = α_p/α = 1.943 — universality between e and p exact,
  but magnitude inflated by ~94% above target.  This is
  expected because k = 1/(8π) was tuned for two-sheet e+p, not
  three-sheet.
- α_ν₁/α = 1.78 — close to e/p value, signaling that the
  three-sheet system needs joint retuning (not a structural
  problem).
- L_ring scales: L_ring_e = 27,200 fm, L_ring_p = 21 fm,
  L_ring_ν = 2.1 × 10¹¹ fm = 0.21 mm.  Span of ~10¹⁰ fm
  between proton and neutrino — consistent with the user's
  physical-scale intuition.

### F28. Phase 1 — R61 #1 converges cleanly with universal α = α

Joint solve at R61 candidate #1: triplet `(+1,+1)(-1,+1)(+1,+2)`,
ε_ν = 2.0, s_ν = 0.022, m_ν₁ = 32.1 meV.  Wide k bounds, g_aa = 1
(R59 F59 fixed).

| Quantity | Value | Target / Reference |
|----------|-------|---------------------|
| k_e | 4.73 × 10⁻² | 1.19× R59 F59 |
| k_p | 4.73 × 10⁻² | 1.19× R59 F59 |
| k_ν | 4.53 × 10⁻² | 1.14× R59 F59 |
| L_ring_e | 24,948 fm | derived |
| L_ring_p | 19.2 fm | derived |
| L_ring_ν | 1.99 × 10¹¹ fm | derived |
| E(electron) | 0.5109989461 MeV | exact |
| E(proton)   | 938.272 MeV | exact |
| E(ν₁)       | 32.100 meV | exact (target) |
| E(ν₂)       | 33.250 meV | predicted (R61: 33.3) |
| E(ν₃)       | 59.624 meV | predicted (R61: 59.7) |
| Δm²₃₁/Δm²₂₁ | 33.59 | passive check vs R49 33.6 ✓ |
| α_e/α       | 1.000000 | target ✓ |
| α_p/α       | 1.000000 | target ✓ |
| α_ν₁/α      | 1.000000 | target ✓ |
| α_ν₂/α      | 1.192 | predicted (not targeted) |
| α_ν₃/α      | 0.910 | predicted (not targeted) |
| Cost (½‖r‖²) | 1.18 × 10⁻²⁶ | residual at floating-point limit |

**Headline:** the architecture works.  All three sheets sit on a
single 11D metric with α universality across the targeted modes
and signature preserved.  k values cluster at ~1.19× R59 F59 for
the charged sheets and 1.14× for the neutrino — small,
consistent shift from the natural-form value.  The Δm² ratio
matches R49 to 4 digits without being targeted.

**Note on ν₂, ν₃ α deviations.**  α_ν₂ = 1.19α and α_ν₃ = 0.91α
— neither equals α despite ν₁ being targeted to α.  The reason:
α_Coulomb depends on the specific mode's (n_t, n_r), not just
the sheet's (ε, s, k).  Different ν modes on the *same* sheet
get different α values.  This is a structural feature, not a
bug.  Whether it conflicts with R61's "Majorana cancellation"
mechanism (which expects ν₁/ν₂ to behave as a charge-conjugate
pair) is a Track 7 / R61-feedback question.

### F29. Phase 1.5 — three of four R61 candidates converge cleanly

| Candidate | (ε_ν, s_ν) | k_e/k_p (× nat) | k_ν (× nat) | α_ν₁/α | converged? |
|-----------|------------|----------------:|------------:|-------:|:----------:|
| #1 `(+1,+1)(-1,+1)(+1,+2)` | (2.0, 0.022) | 1.19 | 1.14 | 1.000 | YES |
| #2 `(+1,+1)(-2,+1)(+1,+2)` | (8.5, 0.0078) | 1.19 | 1.12 | 1.000 | YES |
| #3 `(+2,+1)(-1,+1)(-1,+2)` | (10.0, 0.0207) | 1.09 | 1.26 | 3.42 | partial |
| #4 `(+1,+1)(+2,+1)(+1,+4)` | (2.5, 0.0193) | 1.19 | 1.13 | 1.000 | YES |

R61 #1, #2, #4 all converge with the full α_e = α_p = α_ν₁ = α
universality and Δm² ratio cross-checking against R49.  The k
values cluster around 1.19× R59 F59 for the charged sheets and
1.13–1.14× for the neutrino — robust across very different ν
geometries.

R61 #3 fails because its ν₁ mode is `(+2, +1)` (n_t = 2, not 1).
The α extraction formula scales differently with `n_t`, so the
"α_ν₁ = α" target sits in a harder-to-reach region of
parameter space.  This is consistent with the R59 F45/F45
universality result: structural universality holds for
|n_tube| = 1; modes with |n_tube| = 2 (or higher) couple
differently and may need different k to hit α exactly.

**Practical implication for R61 feedback:** ν candidates with
all three modes at |n_tube| = 1 (i.e., #1, #4) integrate
cleanly into R60.  Candidates using even-tube modes (R61's
"R48 dark" mechanism for charge neutrality, like #3's ν₁ at
(2, 1)) need either different k handling or a different α
target structure.  R61's "dark" interpretation may need
extension to address how α should be set for these modes.

### F30. Per-sheet L scales span 10 orders of magnitude

The converged R61 #1 configuration:

| Sheet | L_ring (fm) | L_ring (m) |
|-------|-------------|------------|
| Proton | 19.2 | 1.92 × 10⁻¹⁴ m |
| Electron | 24,948 | 2.49 × 10⁻¹¹ m (~ Compton scale) |
| Neutrino | 1.99 × 10¹¹ | 2.0 × 10⁻⁴ m (~ 0.2 mm) |

L_e/L_p ≈ 1,300; L_ν/L_e ≈ 8 × 10⁶.  The proton-to-electron
ratio is below the user's "10⁴" rule of thumb (because the
e-sheet here is shearless and not at the model-E generation
resonance — the electron's μ value is ~1, not ~0.005).  The
electron-to-neutrino ratio is much larger than 10⁴ because the
ν is at meV scale (~10⁹ smaller than electron in mass), giving
L_ν proportionally larger.

**The wide L spread is physically sensible** — it tracks the
mass hierarchy m_p > m_e > m_ν₁.  Importantly, the *k* values
(per-sheet diagonal scales) stay close together (within 5%
across all three sheets), so the metric does not require
per-sheet normalization tricks to make the joint solver work.
**The wide-k-bounds policy paid off**: the solver was free to
explore but landed on naturally close k values for this
geometry, validating the R59 F59 architecture as approximately
correct (to ~20%) without needing global-normalization
re-derivation.

### F31. Track 6 status and next steps

**Completed.**

- Joint e+p+ν solver works at R59 F59 architecture (g_aa = 1)
  with no Phase 2 fallback needed.
- Three of four R61 ν-sheet candidates produce clean
  configurations with all six targets met.
- α universality (α_e = α_p = α_ν₁ = α) is achievable across
  all three sheets when the targeted ν mode has |n_tube| = 1.
- ν₂, ν₃ masses and the Δm² ratio cross-check correctly without
  being targeted.
- Per-sheet diagonal scales (k) cluster within ~20% of R59 F59
  natural value for charged sheets — the natural-form story
  survives in the three-sheet setting.
- Per-sheet L scales naturally span 10+ orders of magnitude as
  expected from the mass hierarchy.

**Working baseline for Track 7.**  R61 #1 configuration:

| Knob | Value |
|------|-------|
| (ε_e, s_e) | (1, 0) |
| (ε_p, s_p) | (1, 0) |
| (ε_ν, s_ν) | (2, 0.022) |
| ν triplet | (+1,+1) (-1,+1) (+1,+2) |
| k_e = k_p | 4.73 × 10⁻² |
| k_ν | 4.53 × 10⁻² |
| L_ring_e | 24,948 fm |
| L_ring_p | 19.2 fm |
| L_ring_ν | 1.99 × 10¹¹ fm |
| g_aa | 1.0 (default) |
| σ_ta | √α (default) |
| σ_at | 4πα (default) |

**Notes for Track 7 (compound modes — μ, τ, neutron, hadrons).**

- Use the F31 baseline configuration as the starting metric.
- Compound modes will combine windings across sheets (e.g.,
  muon as e+ν compound per model-E inventory).
- Compound mode α_Coulomb may be species-dependent — the F28
  observation about α_ν₂ ≠ α_ν₁ shows this happens even within
  the same sheet for different (n_t, n_r).  Track 7 should
  document this carefully and not assume universality across
  compound modes.
- The R61 "Majorana pair cancellation" interpretation
  (ν₁ + ν₂ → 0 net charge when both excited) is testable on
  this baseline — Track 7 or a side study could verify.
- R61 candidate #3 (and other |n_tube|=2 ν configurations)
  may need separate treatment; flag back to R61 if their
  taxonomy wants to retain those candidates.

### Decision point

Track 6 is a clean positive result.  R60's full architecture
(11D, R59 F59 α, three sheets, per-sheet diagonal scales) is
validated as compatible with the model-E spectrum's three-sheet
foundation.

Recommend proceeding to **Track 7 — compound mode search** for
muon, tau, neutron, and hadrons.  Use F31 baseline as input.
Test whether model-E's compound modes (e.g., muon =
(1, 1, −2, −2, 0, 0)) land on observed masses on the new metric,
or whether Track 7 finds different compound modes.  Either
outcome is informative.

---

## Track 7: Ring↔ℵ structural cancellation test

**Scope.**  Test the algebraic conjecture (post-Track 6 dialog)
that adding ring↔ℵ entries with the structural prescription
σ_ra = (s × ε) × sign × σ_ta on each sheet cancels the
shear-induced α mode-dependence found in Track 6 F28.

Script: [scripts/track7_ring_aleph.py](scripts/track7_ring_aleph.py).

### Background

Track 6 F28 reported that with the ν-sheet at (ε=2, s=0.022) and
the joint solver tuning k_ν to make α_ν₁ = α exactly, the other
two ν modes did not get α: ν₂ landed at 1.192α and ν₃ at 0.910α
— a 28% spread across modes on the *same* sheet.  Algebraic
analysis attributed this to an indirect ring-to-time leakage
chain: shear couples ring to tube, the tube couples to ℵ, ℵ
couples to t.  The leakage strength depends on (n_t, n_r), so
different modes get different α even on the same sheet.

The conjectured fix: add a *direct* ring↔ℵ entry σ_ra at the
specific value σ_ra = (s · ε) · σ_ta.  Algebraically this
cancels the indirect leak, leaving Q ∝ n_t for all modes —
mode-independent.

R59 had ruled out ring-based ℵ mediation as a *replacement* for
tube coupling (F39) and direct ring↔t added on top of tube↔ℵ↔t
(F43).  But ring↔ℵ as a *structural supplement* with the
specific (sε)-tracking value was not in R59's tested
architectures.

### F32. Structural fix restores ν-mode universality to floating point

Took Track 6 F28 baseline (k_e = k_p = 4.73 × 10⁻², k_ν = 4.53 ×
10⁻², all L's from F28).  Added σ_ra entries:

| Sheet | s · ε | σ_ra value |
|-------|------:|-----------:|
| e | 0 | 0 |
| p | 0 | 0 |
| ν | 0.044 | +3.76 × 10⁻³ |

(Only ν gets a nonzero entry because e and p are shearless in
this baseline.)  Built the augmented 11D metric.

Comparison:

| Mode | α_base/α | α_aug/α |
|------|---------:|--------:|
| electron (1, 2) | 1.000 | 0.9989 |
| proton   (1, 3) | 1.000 | 0.9989 |
| ν₁ (+1, +1) | 1.000 | 1.0885 |
| ν₂ (−1, +1) | 1.192 | 1.0885 |
| ν₃ (+1, +2) | 0.910 | 1.0885 |
| **ν-mode spread** | **28.2 %** | **0.0000 %** |

Signature OK in both cases (one negative eigenvalue, the t
direction).

### F33. Interpretation

**The conjecture holds at floating-point precision.**  The σ_ra =
(s·ε) · σ_ta prescription cancels the n_r-dependent term in the
α extraction *exactly*, not approximately.  All three ν modes —
including ν₃ at (1, 2) which had the largest deviation in the
base case — collapse to the same α.

The remaining issue is the **overall magnitude shift**: the
single value all three ν modes converge to is 1.0885α, not
α exactly, and the e/p modes shift slightly to 0.9989α.  The
metric changed (new entries added) and we didn't re-solve the
free knobs (k_e, k_p, k_ν).  A fresh joint solve on the
augmented metric would adjust the k values and shift everyone
back to exactly α.  The structural cancellation persists under
re-tuning (it's coordinate-independent), so the magnitude fix
is a separate, easily-handled problem.

**This solves the mode-dependence problem identified in Track 6.**
R60's α universality story is restored — not just across
sheets, but across modes within a sheet.  R59 F45's "structural
universality" extends to the sheared case, provided the
ring↔ℵ entry is set to its structurally-determined value.

### F34. Status and what's resolved

R60 now has:

1. **R59 F59 architecture** with three sheets, all coupled via
   tube↔ℵ↔t.
2. **Per-sheet diagonal compensation k_x** (Track 4) that
   adjusts to make each sheet's lead mode hit α exactly.
3. **Per-sheet ring↔ℵ entry σ_ra_x** (Track 7) at structural
   value (sε)_x · σ_ta_x that cancels mode-dependence on
   sheared sheets.

Together these give: α_e = α_p = α_ν = α (across sheets, by
universality of |n_tube|=1 + per-sheet k tuning) and α independent
of (n_t, n_r) within each sheet (by the σ_ra cancellation).
Both axes of universality are now achieved.

Per-sheet "natural" values for the augmented architecture (at
the Track 6/7 baseline geometry, post-resolve — not yet
explicitly computed):

| Knob | Value |
|------|-------|
| σ_ta_x | sign × √α (per sheet) |
| σ_at | 4πα |
| g_aa | 1 |
| k_x | tunable per sheet, ~5% of unity for charged sheets at moderate shears |
| **σ_ra_x** | **(sε)_x · σ_ta_x  (NEW, derived)** |

### Caveats and open questions

- **Mass impact not verified.**  The mode_energy formula in
  Track 1 uses only the Ma sub-block; ring↔ℵ entries sit
  outside Ma so they don't enter that approximation.  A full
  Schur-corrected mass calculation would shift masses slightly.
  Likely small (the σ_ra values are small) but should be
  verified.
- **No re-solve done.**  Track 7 used Track 6's k and L values
  unchanged.  A clean joint solve on the augmented metric would
  give the post-fix natural-form k values and show the magnitude
  shift collapses.  Easy follow-up.
- **Cross-sheet effects.**  My derivation was for a single
  sheet in isolation.  On the joint e+p+ν metric, the σ_ra
  cancellation might have small cross-sheet residuals.  The
  numerical result here (spread 0.0000%) suggests cross-sheet
  effects are also cancelled or extremely small.  Notable.
- **Generalizes to sheared e and p.**  The Track 6/7 baseline
  has e and p shearless.  If we ever turn on shear there
  (e.g., for ghost suppression or compound mode placement), the
  σ_ra prescription should still apply: σ_ra_e = (s·ε)_e · σ_ta_e
  cancels the e-sheet's leak.  Worth testing once we add
  e-sheet shear.
- **Compound modes.**  Compound modes span multiple sheets;
  their α extraction involves contributions from each sheet.
  The single-sheet structural fix should work per sheet, so
  compound mode α should also be mode-independent on the
  augmented metric.  Track 8 (compound mode search) will test.

### Decision point

**The mode-dependence concern flagged in the Open Question
section above is now resolved structurally.**  The three
candidate next-step tracks I outlined (7a, 7b, 7c) are
superseded by Track 7's actual result.  The original "Track 7d"
(compound mode search for μ, τ, neutron, hadrons) becomes the
natural next step.

Recommend: re-solve the joint system on the augmented metric
(quick post-fix calibration), then proceed to compound mode
search.

---

## Track 7b: Re-solve on the ring↔ℵ augmented metric

**Scope.**  Track 7 demonstrated structural ν-mode universality
(spread 0.0000%) but with α magnitude shifted to 1.0885α because
Track 6's k values were used unchanged on a metric that had
changed.  Track 7b runs the full joint solver on the augmented
metric to bring magnitude back to α exactly while preserving the
structural cancellation.

Script: [scripts/track7b_resolve.py](scripts/track7b_resolve.py).

### F35. Re-solve converges with all six targets at floating-point precision

Joint solver on the augmented metric (tube↔ℵ + structural
ring↔ℵ + ℵ↔t).  6 free knobs (L_x, k_x per sheet), 6 targets
(m_x, α_x = α for x ∈ {e, p, ν₁}).  Same Track 6 sheet inputs
(R61 #1: e/p shearless, ν at ε=2, s=0.022).

| Knob | Value |
|------|-------|
| k_e  | 4.696442 × 10⁻²  (1.1803× R59 F59) |
| k_p  | 4.696442 × 10⁻²  (1.1803× R59 F59) |
| k_ν  | 4.696442 × 10⁻²  (1.1803× R59 F59) |
| L_ring_e | 25,035 fm |
| L_ring_p | 19.28 fm |
| L_ring_ν | 1.96 × 10¹¹ fm |

| Target | Value | Precision |
|--------|-------|-----------|
| E_e | 0.5109989461 MeV | 10⁻¹⁵ |
| E_p | 938.272 MeV | 10⁻¹⁴ |
| E_ν₁ | 32.100 meV | 10⁻¹⁴ |
| α_e / α | 1.0000000000 | 10⁻¹⁵ |
| α_p / α | 1.0000000000 | 10⁻¹⁵ |
| α_ν₁ / α | 1.0000000000 | 10⁻¹⁴ |
| Signature | OK | one neg eig (the t direction) |

### F36. Track 7's structural prediction is confirmed at floating-point exactness

ν₂ and ν₃ were not targeted in the solve.  Track 7 predicted
that, regardless of the converged (L, k) values, the structural
σ_ra cancellation would make all three ν modes give the same α.

| Mode | α_x / α |
|------|---------|
| ν₁ (+1, +1) — targeted | 1.0000000000 |
| ν₂ (−1, +1) — *not targeted* | 1.0000000000 |
| ν₃ (+1, +2) — *not targeted* | 1.0000000000 |
| **ν-mode α spread** | **0.00e+00** |

The cancellation is a property of the augmented metric structure,
not of any specific operating point.  Track 7's algebraic
derivation is fully validated.

### F37. The augmented architecture has a single-k symmetry

A striking observation from F35: the joint solver — with three
*independent* per-sheet k knobs — converged on **k_e = k_p = k_ν**
to floating-point precision.  Track 6's solver had given values
within ~5% of each other (~1.19× nat for charged sheets, 1.14× for
ν).  The augmented metric pins them to one common value (1.1803×
R59 F59 = 0.04696).

This suggests that adding the ring↔ℵ entries restores a deeper
symmetry between sheets.  In the un-augmented (Track 6) metric,
the per-sheet k differed because shear-induced ring leakage was
species-dependent (different n_r per sheet).  With the
cancellation, that asymmetry is gone, and one global k handles
all three sheets.

**Practical consequence:** the model has *one* diagonal-scale
parameter, not three.  k = 1.1803 × 1/(8π) = 4.696 × 10⁻² is the
new candidate "natural" value for the augmented architecture.
Whether this value has a clean closed form (analogous to R59
F59's 1/(8π)) is open; numerically 1.1803 is suggestive but
hasn't been pattern-matched yet.  Worth analytical follow-up.

### F38 (cross-checks). Δm² ratio and ν masses fall out automatically

| Quantity | Value | R49/R61 reference |
|----------|-------|-------------------|
| E(ν₂) | 33.250 meV | R61 #1: 33.3 |
| E(ν₃) | 59.624 meV | R61 #1: 59.7 |
| Δm²₃₁ / Δm²₂₁ | 33.5909 | R49 target: 33.6 |

The Δm² ratio matches to 4 digits without being targeted —
consistent with R49's mechanism (the ratio is a function of
(ε_ν, s_ν) alone).  R61 candidate #1's ν₂ and ν₃ masses are
also reproduced, confirming the R61 taxonomy is internally
consistent with our metric.

### Status

R60 architecture is now FULLY validated as compatible with the
model-E three-sheet foundation:

- α universal across sheets ✓ (Track 4)
- α universal across modes within a sheet ✓ (Track 7 + 7b)
- Three-sheet metric works with one global k ✓ (Track 7b F37)
- All masses calibrated correctly ✓
- Δm² ratio cross-checks ✓

**Working baseline for Track 8 (compound modes):**

| Knob | Value |
|------|-------|
| (ε_e, s_e) | (1, 0) |
| (ε_p, s_p) | (1, 0) |
| (ε_ν, s_ν) | (2, 0.022) |
| ν triplet | R61 #1: (+1,+1)(-1,+1)(+1,+2) |
| k (all sheets) | 4.696 × 10⁻² (1.1803/(8π)) |
| L_ring_e | 25,035 fm |
| L_ring_p | 19.28 fm |
| L_ring_ν | 1.96 × 10¹¹ fm |
| g_aa | 1 |
| σ_ta | √α (signs +1, −1, +1 for e, p, ν) |
| σ_at | 4πα |
| **σ_ra (NEW)** | **(sε)·σ_ta per sheet (derived, not free)** |

### Open follow-ups

- Analytical derivation of the natural-form value k = 1.1803/(8π).
  R59 F59 found k = 1/(8π); the augmented architecture wants
  k = 1.1803/(8π).  Pattern? Analytical identity? (Cheap analysis.)
- Mass impact of σ_ra entries via Schur correction.  Track 7b's
  joint solve uses mode_energy on the Ma sub-block only; a
  full Schur calculation would shift masses by O(σ_ra²) ≈ 10⁻⁵.
  Likely small enough to ignore but worth a check.
- Test the augmented architecture with non-shearless e or p
  sheets.  The σ_ra prescription should generalize cleanly, but
  Track 7 only verified for ν having shear and e/p shearless.

### Decision point

**The Track 7+7b ring↔ℵ structural fix is a real architectural
advance.**  R60's α universality is now established on both axes
(across sheets AND across modes).  The compound-mode question
(Track 8) is the next natural step — this is the original "Track
7d" from the now-superseded Open Question section.

Recommend proceeding to Track 8 (compound modes — μ, τ, neutron,
hadrons) on this baseline.

---

## Open question (resolved by Tracks 7 + 7b — kept for history): mode-dependent α and possible compound mass splitting

### What we found

Track 6 surfaced that α_Coulomb is **mode-dependent** on any
sheared sheet under R59 F59.  The closed-form formula is

    Q(n_t, n_r) ∝ n_t · (1 + u²) − n_r · u   with u = s · ε.

At u = 0 (shearless), Q ∝ n_t — so all |n_tube|=1 modes get
identical Q regardless of n_r.  At u ≠ 0, the n_r·u term breaks
this and different (n_t, n_r) on the same sheet get different α.

In our Track 6 baseline this only manifested on the ν-sheet
(s_ν = 0.022), where ν₁ at α target gave ν₂ at 1.19α and ν₃ at
0.91α.  e and p sheets are shearless in the baseline so didn't
exhibit mode-dependence.

### Why this matters

Standard physics has α as a universal constant (1/137 for every
charged particle).  If the model predicts different α for
different particles on the same sheet, it is not faithful to
observation — at least not without reinterpreting what α
*means* in MaSt.

### Two candidate resolutions

**(a) Reinterpret α as a mode-dependent coupling strength
modulated by topological charge.**  Integer EM charge in MaSt
is topological (Q_charge = −n_e_tube + n_p_tube).  Our extracted
"α_Coulomb = Q²/(4π)" might be a per-mode coupling parameter
(weak-interaction analog?), not the universal EM coupling.  The
electron's value happens to equal observed α; other modes have
related-but-different values.  Physical support: neutrinos *do*
have different scattering rates per flavor.  But: the standard
model treats α as universal across charged leptons, and any MaSt
reinterpretation needs a compensating story for charged modes
(which we didn't test because e and p stayed shearless).

**(b) Eliminate sheared sheets entirely.**  If no sheet has
internal shear, mode-dependence vanishes everywhere and α is
strictly universal across |n_tube|=1 modes.  But this requires
finding non-shear mechanisms for everything shear currently does.

### What shear currently does in MaSt (load-bearing)

Per user assessment plus review of model-D/E/R49:

1. **Neutrino oscillation matching.**  R26's `s_ν ≈ 0.022` gives
   `Δm²₃₁/Δm²₂₁ = 33.6` exactly via `(3−2s)/(4s)`.  Without
   shear, all (n_t, n_r) modes on a shearless sheet have masses
   determined only by μ = √((n_t/ε)² + n_r²) — a fixed
   geometric pattern.  Whether *any* shearless ν-sheet
   geometry gives the right mass triplet 32.1/33.3/59.7 meV is
   open and unlikely without auxiliary mechanism.
2. **Generation structure (R53).**  Already retired in R60
   (Track 4 F19 incompatibility with R59 F59 α).  Replaced by
   compound modes per model-E inventory.
3. **Ghost suppression on charged sheets.**  Multiple
   alternatives exist (R46 waveguide cutoff, R47 gcd
   irreducibility, R56 mode routing, R61 (1,1) filter on
   ν-sheet).  Not strictly shear-dependent.

### Compound mass splitting — what it would look like

In the current single-sheet picture, ν₁/ν₂/ν₃ are three
different (n_t, n_r) on the same (ε_ν, s_ν, L_ring_ν) sheet.
Mass differences come entirely from the geometric formula at
nonzero shear.

In a compound picture, ν₁/ν₂/ν₃ would each be a 6-tuple
spanning multiple sheets:

| Eigenstate | Possible compound mode (illustrative) |
|------------|---------------------------------------|
| ν₁ | `(0, 0, 1, 1, 0, 0)` — pure ν-sheet (1, 1) |
| ν₂ | `(1, 0, 1, 1, 0, 0)` — ν₁ + small e-sheet (1, 0) leak |
| ν₃ | `(0, 0, 1, 1, 1, 0)` — ν₁ + small p-sheet (1, 0) leak |

Each compound mode's mass comes from `E² ∝ ñ G̃⁻¹ ñ` summing
across all touched sheets.  Cross-sheet σ entries (which were
zeroed in the R60 baseline) provide the inter-sheet coupling.
Different compounds get different masses **even on shearless
sheets**, because their cross-sheet contributions differ.

### Possible next-step tracks (deferred — R60 paused for analysis)

If R60 resumes after the analysis dialog the user has planned,
candidate tracks to investigate this question:

**Track 7a — mode-dependence audit.**  Catalog α_Coulomb for a
representative set of (n_t, n_r) modes on each sheet at the
Track 6 baseline.  Quantify how big the deviation gets across
the modes we'd want to label as ν₁/ν₂/ν₃ and across compound
modes that might represent muon/tau/neutron.  Outcome: a sharp
characterization of how serious the mode-dependence problem is
across the whole spectrum.

**Track 7b — shearless ν compound mass splitting attempt.**
Set s_ν = 0.  Search compound 6-tuples (e + ν, p + ν, e + ν + p
combinations) whose energies could be assigned to ν₁/ν₂/ν₃.
Use cross-sheet σ entries (currently zeroed) as the splitting
mechanism.  Test whether *any* configuration produces
m_ν₂/m_ν₁ and m_ν₃/m_ν₁ ratios consistent with observed
oscillation data (Δm²₃₁/Δm²₂₁ = 33.6).  If yes: shear can be
dropped from ν-sheet, mode-dependence vanishes, R60 program
strengthens.  If no: shear is genuinely required for ν
oscillations and we must address mode-dependence on its own
terms.

**Track 7c — α reinterpretation feasibility.**  Take the
mode-dependence as physical and ask what it would predict.
Compute α_e for the electron (1, 2) on the *currently
shearless* e-sheet (always equals α — no test).  Then add a
small s_e and recompute α for the (1, 1) ghost mode and (1, 3)
hypothetical mode to see how mode-dependence behaves on the
e-sheet.  Compare to standard QED predictions for any related
observable.  Outcome: indicates whether the mode-dependent α
could survive as a physical prediction or is incompatible with
known data.

**Track 7d (the original "Track 7" before this question
arose) — compound mode search for μ, τ, neutron, hadrons.**
Resume the F31 baseline and search for compound modes matching
the model-E inventory.  Defer α universality concerns; just
check whether mass spectrum reproduces.  Could be useful as
parallel work even if 7a–c are still in question.

### Status

R60 paused at end of Track 6 for further analysis dialog with
user.  No commitment to which (if any) of the above tracks to
pursue; depends on outcome of analysis.
