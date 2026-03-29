# R41. Dynamic torus model — full implementation

**Status:** Done
**Depends on:** R40 (α-impedance model, low-pass filter),
  R27 (neutron/muon constraint on r_p, σ_ep),
  R15/R19 (α derivation), R33 (ghost census)
**Motivates:** Q34 (what selects r?), Q77 (ghost suppression),
  Q86 (three generations), Q91 (V_compact)


## Premise

R40 established the α-impedance model: the torus wall is the
(1−α) energy contour of the photon mode.  The key deliverables —
elliptical cross-section, 1/k² low-pass filter, geometric vacuum
polarization — are independent of the aspect ratio r.

R41 takes this from a theoretical finding to a working model:
refactor `lib/ma_model.py` to incorporate the dynamic torus
physics, re-derive the particle spectrum from scratch, and test
whether the dynamic model improves on the static one.


## Goals

1. **Refactor `lib/ma-model.md` and `lib/ma_model.py`** to support
   the dynamic model alongside the existing static model.  The
   dynamic model adds:
   - The α-impedance energy partition: E_inside = (1−α)E,
     E_outside = αE
   - The force balance: tube expansion vs vacuum spring →
     equilibrium tube radius a*
   - The elliptical cross-section from the mode's pressure profile
   - The low-pass filter eigenvalue correction for each mode
   - Running α(E): wall transparency as a function of mode energy

2. **Code, test, validate** the new dynamic engine.  The static
   model must still work unchanged.  The dynamic model extends it,
   not replaces it.  Regression tests must pass.

3. **Re-derive the expected particles from scratch.**  Start with
   ZERO assumptions from the static model — no r_p = 8.906, no
   σ_ep = −0.0906.  Inputs are only:
   - Three sheets (Ma_e, Ma_ν, Ma_p)
   - The (n₁, n₂) = (1, 2) winding for charged modes
   - α = 1/137.036
   - Observed particle masses (electron, proton, neutron, muon)
   - The dynamic force balance

   Determine what the dynamic model predicts for the free parameters
   (r_e, r_nu, r_p, cross-shears).

4. **Check: does r_p = 8.906 re-emerge?**  If the dynamic model
   (force balance + Compton + α condition) reproduces the static
   model's r_p, this is a non-trivial confirmation.  If not,
   understand why.

5. **Ghost census.**  Enumerate all modes below 10 GeV on each
   sheet.  For each mode, compute the dynamic correction (low-pass
   filter eigenvalue shift).  Does the dynamic model suppress
   ghosts that the static model doesn't?  Quantify the suppression.

6. **Three generations.**  The electron, muon, and tau have the
   same quantum numbers but different masses.  Can the dynamic
   model produce three distinct (1,2) solutions on the electron
   sheet — three equilibrium shapes at different r values?  Or
   does the equilibrium pick exactly one?

7. **Full particle table.**  Compile a table of all dynamically
   allowed modes, with:
   - Quantum numbers (n₁, ..., n₆)
   - Mass (static model, dynamic model, observed)
   - Charge, spin
   - Low-pass filter suppression factor
   - Dynamic stability (is the equilibrium a minimum or saddle?)

8. **Verdict: dynamic vs static.**  Summarize what the dynamic
   model adds, what it gets right, and what it gets wrong compared
   to the static model.


## Approach

### Track 1: Design spec update [DONE]

Updated `lib/ma-model.md` Feature 10 (Dynamic model).  Covers:
- Mode-dependent pressure harmonics and cross-section shape
- Per-sheet eigenvalue corrections weighted by E² fractions
- Low-pass filter from elastic 1/k² response
- Running α(E) (qualitative; formula TBD)
- Full API: `pressure_harmonics`, `wall_shape`, `dynamic_correction`,
  `filter_factor`, `energy_static`, integration with scan/fit
- Harmonic caching by (n_tube, n_ring, r)
- Updated testing strategy (6 new tests for dynamic model)

### Track 2: Implementation [DONE]

Extended `Ma` with dynamic flag.  Two solution methods:

- **`dynamic='full'`** (or `True`): Iterative force-balance solve.
  Repeats pressure → shape → pressure until the wall converges.
  Convergence is geometric with ratio ~α; 2–3 iterations to
  machine precision.  This IS the self-consistent solution.

- **`dynamic='shortcut'`**: One-shot perturbation on the circular
  cross-section.  Fast (iteration zero of the full solve).  Agrees
  with full to O(α⁴) in energy.

New code:
- `_compute_pressure_harmonics()` — accepts optional shape deformation;
  analytical derivatives for deformed cross-section
- `_iterative_force_balance()` — shape → pressure → shape loop
- `pressure_harmonics()` dispatches to iterative or one-shot
- `dynamic_correction()`, `filter_factor()` — per-sheet eigenvalue shifts
- `energy()`, `energy_static()` — dynamic vs flat-torus energy
- `dynamic_method` property: 'off', 'shortcut', or 'full'
- Wired through `scan_modes`, `with_params`, `fit`, `to_dict`,
  `from_dict`, `summary`, `__repr__`
- 42 new tests (125 total), all passing

Verified numerically: full-solve converged result is self-consistent
to 5×10⁻¹⁴ (one more iteration changes nothing).  Full vs shortcut
differ by ~10⁻⁷ relative energy — the code discovers this rather
than assuming it.

### Track 3: Validation [DONE]

Full vs shortcut comparison (`scripts/track3_full_vs_shortcut.py`):

- **Convergence**: 3–4 iterations, ratio ≈ 0.003 (geometric, ~α²/2).
  Self-consistent to 217× machine epsilon.
- **Accuracy**: Full and shortcut agree to O(α⁴) in energy.
  Proton difference: 8.7×10⁻⁴ MeV (10⁻⁷ relative).
- **Speed**: Full costs ~4.5× per unique harmonic (~20 ms vs ~4.5 ms).
  scan_modes is only ~15% slower (caching amortizes the cost).
- All 125 tests pass; Track 11 results reproduced.
- Findings: F27 (convergence), F28 (accuracy), F29 (timing).

### Track 4: Fresh parameter determination [DONE]

Re-derived r_p and σ_ep from neutron + muon masses using static,
shortcut, and full dynamic models (`scripts/track4_fresh_params.py`):

- **Result**: Dynamic model reproduces static R27 solution to 7
  significant figures (Δr_p = 2×10⁻⁷, Δσ_ep = 2×10⁻¹⁰).
  The fit targets (neutron, muon) have negligible dynamic corrections.
- **Non-target shifts**: Dynamic model predicts E(electron) and E(proton)
  are ~10⁻⁴ higher than bare torus values — a geometric correction.
- **3-target fit bug**: Adding electron as a target fails to converge
  because self-consistent L-rescaling targets static energy while
  fit residuals use dynamic energy.  Fixable but not blocking.
- Findings: F30 (parameters unchanged), F31 (non-target shifts),
  F32 (L-rescaling inconsistency), F33 (robustness).

### Track 5: Ghost census (dynamic) [DONE]

Enumerated 117,648 modes below 2 GeV (`scripts/track5_ghost_census.py`):

- **No change in mode count**: Energy shifts are O(10⁻⁴); no modes
  cross the 2 GeV threshold.  93.7% remain ghosts.
- **The (1,1) ghost persists**: FF ≈ 0.46 — only 2× suppressed vs
  the electron. Same tube winding → same coupling harmonic.
- **High-tube suppression works**: |n_tube|=2 modes have median
  FF ≈ 0.005 (200× suppressed), |n_tube|=3 → 0.0002 (5000×).
  Reinforces R33's charge selection rule but targets the same modes.
- **Verdict**: Dynamic model does NOT solve the ghost problem.
  The (1,1) boson remains the critical tension.
- Findings: F34–F37.

### Track 5c: Three-category census & generation identification [DONE]

The n_max=3 census (Track 5) missed the muon and tau.  Redone
with n_max=5 (1.45M modes → 131,769 families, collapsing only
the degenerate n₄).  Proper taxonomy replaces blunt "ghost" label:

- **Cat A** (known matches): 8,633 families → 14 particle types
  including all 3 charged lepton generations (e, μ, τ).
- **Cat B** (high harmonics): 120,863 families → killed by
  low-pass filter + R33 charge rule.  92% of all families.
- **Cat C** (unmatched resonances): 2,273 families → the real
  problem.  The (1,1) boson persists (FF ≈ 0.46).

Generation structure: the low-pass filter distinguishes
generations via their tube windings.  FF ordering:
electron (1.00) > tau (0.025) > muon (0.0002).

Findings: F38–F41.

### Track 6: Generation structure

- On the electron sheet: scan for multiple (1,2) equilibria
- On the proton sheet: scan for multiple (1,2) equilibria
- If multiple equilibria exist, do they correspond to generations?

### Track 7: Particle table and verdict [DONE]

Compiled full table of all 12 canonical mode assignments — 4 anchors
(e, p, n, μ), 1 generation (τ), 7 hadron predictions (K±, K⁰, η,
η′, φ, Λ, Σ⁺) — comparing static vs dynamic energies, filter factors,
and observed masses (`scripts/track7_particle_table.py`).

**Result**: 0 predictions improved, 2 trivially worsened (e, p shift
+0.03%), 10 unchanged.  Dynamic corrections (O(α²) ≈ 10⁻⁴) are 100×
smaller than structural errors (1–6%).  Hadrons get zero correction
(tube windings ≥ 3 → deeply suppressed).

**Verdict**: The dynamic model is a CONCEPTUAL advance (geometry,
generation hierarchy, 92% mode elimination) but not a QUANTITATIVE
one (no mass improvement, (1,1) ghost persists, free parameters
unchanged).  Retain as the correct physical picture; use static
for practical calculations.

Findings: F42–F43.


## Caveats

- The low-pass filter from R40 gives eigenvalue SHIFTS, not
  mode elimination.  The suppression is ~40× per step in n₁,
  but this is a relative shift, not a hard cutoff.  Whether this
  constitutes "ghost suppression" depends on the magnitude.

- The dynamic model's force balance requires a spring constant
  (from the vacuum EM impedance).  The exact form of this spring
  determines the equilibrium.  R40 used P_in ∝ a (Hooke's law);
  the actual dependence may differ.

- r remains free in the dynamic model (R40 F26) unless V_compact
  can be derived from the compact geometry (Q91).  Track 4 may
  find that the dynamic model reproduces r_p = 8.906 from the
  observed masses (same as the static model) without independently
  fixing r.


## Tools

- `lib/ma_model.py` — extended with dynamic model
- `lib/ma-model.md` — updated design spec
- `lib/test_ma_model.py` — extended regression tests
- R40 Track 1 (`track1_pressure_profile.py`) — pressure computation
- R40 Track 11 (`track11_alpha_shape.py`) — deformation and filter
