# R41. Dynamic torus model — full implementation

**Status:** Active
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

### Track 4: Fresh parameter determination

Starting from scratch (no r_p input):
- Fix α = 1/137.036 (measured)
- Fix observed masses: m_e, m_p, m_n, m_μ
- Solve for r_e, r_nu, r_p, σ_ep, σ_eν, σ_νp
- Compare to static model's R27 solution

### Track 5: Ghost census (dynamic)

- Enumerate modes with E < 10 GeV on all three sheets
- For each: compute dynamic suppression factor
- Compare ghost count: static model vs dynamic model
- Identify modes that are dynamically forbidden but statically allowed

### Track 6: Generation structure

- On the electron sheet: scan for multiple (1,2) equilibria
- On the proton sheet: scan for multiple (1,2) equilibria
- If multiple equilibria exist, do they correspond to generations?

### Track 7: Particle table and verdict

- Compile full table
- Quantitative comparison: dynamic vs static
- List of predictions that differ between models


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
