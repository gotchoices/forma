# R50: Filtered multi-sheet mode search

**Status:** Active — Track 8 in progress (Tracks 1–7 complete)
**Questions:** Q16 (mass spectrum)
**Type:** compute
**Depends on:** R29 (nuclei as Ma modes), R46 (electron filter),
R47 (proton filter), R49 (neutrino filter)

---

## Motivation

Ma is **one** six-dimensional material space: Ma_e, Ma_ν, and Ma_p are
three coupled sheets, not three independent laboratories.  A physical
mode is always a full six-tuple **n** = (n₁, …, n₆); "single-sheet"
stories are projections for intuition, not separate search spaces.
**This study models the joint system** — parameters, metric, and
searches are over **coupled** modes only.

Prior work already treated nuclei that way at the **pre-filter**
geometry: **R29 Track 3** ([`track3_nuclear_modes.py`](../R29-atoms-and-nuclei/scripts/track3_nuclear_modes.py))
searched for Ma modes matching nuclei from the deuteron through
heavier benchmarks (see findings **F16**, nuclear scaling
n₅ = A, n₆ = 2A).  A neutron mode and a deuteron mode are the same
kind of object — **more complex windings on the same unified torus**,
not a different theory of "particles" vs "nuclei."

R27 produced a zero-parameter particle catalog that matched
5 particles within 1.5% and showed a lifetime-gap correlation
(r = −0.84) supporting the off-resonance hypothesis.  But it
used a model with assumptions that subsequent studies have
revised or challenged:

- Proton as (1,2) at r_p = 8.906 — R47 now favors (3,6)
  composite with geometric confinement and SU(6) quark
  structure
- Neutrino parameters pinned from neutron/muon fits —
  R49 shows ε_ν is broadly viable (0.1–5+), not tightly
  constrained
- No waveguide filtering — R46 established waveguide cutoff
  as a hard mode selection rule on Ma_e and Ma_p
- No spin filtering at finite ε — R49 showed spin deviates
  significantly from ½ at large ε

This study builds a **new joint metric and search** from scratch,
incorporating the filtering rules from R46/R47/R49, sweeps
parameters without premature pinning, and asks which **full 6D**
modes survive as candidates for hadrons, leptons, and **composite
nuclear states** (neutron in vacuum, n+p in nuclei, …) under the same
rules.


## Philosophy

1. **One system.**  The object of study is the **coupled** 6×6 metric
   and modes in ℤ⁶.  We do **not** treat per-sheet particle catalogs as
   primary deliverables; sheet-wise filters are **constraints on
   components of n**, not invitations to search three separate spectra.

2. **No premature pinning.**  Parameters (ε, s, cross-shears)
   are swept, not fitted to specific particles.  A parameter
   set is "good" if it accommodates many known **joint** modes
   simultaneously, not if it nails one.

3. **Ephemeral states are near-misses.**  Unstable particles
   (neutron, pion, muon, etc.) are not expected to sit exactly
   on a Ma eigenmode.  They are expected to be *near* an
   eigenmode, with the decay rate reflecting how far off
   resonance they are.  A particle with a 10⁻¹⁰ second
   lifetime is a closer match than one with a 10⁻²³ second
   lifetime.

4. **Filtered modes only.**  Waveguide cutoff, finite-ε spin, and
   (where applicable) charge rules are applied to **full modes** (each
   rule names the sheet whose winding pair must satisfy the inequality).
   Ghost modes that don't survive filtering are excluded from the
   candidate list.

5. **The neutron is not a calibration target.**  R27 used the
   neutron to pin r_p and σ_ep.  This study treats the neutron
   as a *prediction* to be checked, not an input.  The neutron
   is unstable (τ ≈ 880 s) — it should be a near-miss, not an
   exact eigenmode.

6. **Decay rate ↔ near-miss distance.**  If the off-resonance
   hypothesis is correct, shorter-lived particles should have
   larger mass residuals (farther from the nearest eigenmode).
   This correlation is a key diagnostic.

7. **Nuclei are mode combinations, not a separate program.**  If the
   model can represent a free neutron, it must admit **richer**
   six-tuples for bound systems (e.g. deuteron, α) in the same
   framework — as in R29 Track 3, now revisited with R46–R49 filters.

8. **Defaults, not pins** (model-D.md §Parameter strategy).
   Every geometry parameter has a documented default with a stated
   source and confidence level.  When a single data point constrains
   a parameter (e.g. σ_ep from the neutron mass), record the
   constraint with a width — don't lock the value.  Keep free
   variables free: later data points may prefer a slightly different
   value, and the model should accommodate the tension rather than
   break.  See `ma_model_d.py` `from_physics()` for the full
   provenance table.


## New library: `ma_model_d`

Implement as `studies/lib/ma_model_d.py`.  The name pairs with the
**mast_c** model line in [`models/README.md`](../../models/README.md)
(supersedes `studies/lib/ma_model.py` from the mast_b-era stack for new
work).  Same role as before: code for the joint filtered metric
(R46/R47/R49) on the **full** six-tuple.

### Inputs (per sheet — all feed one G̃)

| Parameter | Symbol | Status |
|-----------|--------|--------|
| Electron aspect ratio | ε_e | Swept (R37 prefers ~0.5) |
| Electron shear | s₁₂ | Derived from α(ε_e, s₁₂) = 1/137 |
| Neutrino aspect ratio | ε_ν | Swept (R49: viable 0.1–5+) |
| Neutrino shear | s₃₄ | Swept or derived from Δm² ratio |
| Proton aspect ratio | ε_p | Swept (R47: (3,6) composite) |
| Proton shear | s₅₆ | Derived from α(ε_p, s₅₆) = 1/137 |
| Cross-shears | σ_ep, σ_eν, σ_νp | Swept (small) |

### Mode filtering rules

These are **predicates on full modes** n; each line names the sheet
whose winding pair must satisfy the inequality.

**Ma_e (electron sheet, indices 1–2):**
- Waveguide cutoff: n₂ > |n₁|/ε_e
- Spin ½: |L_z/ℏ − 0.5| < tolerance
- Charge: |n₁| = 1 for EM-charged modes
- Reference mode: electron = (1, 2)

**Ma_ν (neutrino sheet, indices 3–4):**
- Waveguide cutoff: n₄ > |n₃|/ε_ν
- Spin ½ (finite ε formula)
- No charge requirement (neutral sheet)
- Reference: Assignment A = (1,1), (−1,1), (1,2) if
  confirmed; otherwise left open

**Ma_p (proton sheet, indices 5–6):**
- Waveguide cutoff: n₆ > |n₅|/ε_p
- Spin ½ (finite ε formula)
- Charge: |n₅| = 1 for EM-charged modes (but (3,6)
  composite carries charge from (1,2) strands)
- Reference mode: proton = (3, 6) composite of 3×(1,2)

### Energy formula

For a 6D mode n = (n₁, ..., n₆):

> E² = Σᵢⱼ G̃ⁱʲ nᵢ nⱼ × (ℏc)² / (L_ref)²

where G̃ is the dimensionless metric built from the
aspect ratios and shears.  The metric is block-diagonal
(3 sheets) plus off-diagonal cross-shear blocks.

### Charge and spin

- Charge Q = −n₁ + n₅ in units of e; for composites,
  Q = (−n₁ + n₅/gcd(n₅,n₆)) (R47 Track 7 F4)
- Spin: L_z/ℏ = S(ε)/q for each sheet, using the finite-ε
  path integral formula


## Targets

All targets are **joint** 6D mode identities in the coupled system.

### Tier 1: Stable particles (must accommodate)

| Particle | Mass (MeV) | Charge | Spin | Lifetime |
|----------|-----------|--------|------|----------|
| Electron | 0.511 | −1 | ½ | Stable |
| Proton | 938.272 | +1 | ½ | Stable (>10³⁴ yr) |
| Neutrinos | ~meV | 0 | ½ | Stable |

### Tier 2: Long-lived (should be near-misses)

| Particle | Mass (MeV) | Charge | Spin | Lifetime |
|----------|-----------|--------|------|----------|
| Neutron | 939.565 | 0 | ½ | 879 s |
| Muon | 105.658 | −1 | ½ | 2.2 μs |
| Charged pion | 139.570 | ±1 | 0 | 26 ns |
| Neutral pion | 134.977 | 0 | 0 | 8.4 × 10⁻¹⁷ s |
| Charged kaon | 493.677 | ±1 | 0 | 12 ns |
| Λ | 1115.683 | 0 | ½ | 263 ps |

### Tier 3: Short-lived (expect larger misses)

| Particle | Mass (MeV) | Charge | Spin | Lifetime |
|----------|-----------|--------|------|----------|
| Σ⁺ | 1189.37 | +1 | ½ | 80 ps |
| Ξ⁰ | 1314.86 | 0 | ½ | 290 ps |
| Ω⁻ | 1672.45 | −1 | 3/2 | 82 ps |
| Δ(1232) | 1232 | 0,±1,±2 | 3/2 | ~6 × 10⁻²⁴ s |
| ρ(770) | 775 | 0,±1 | 1 | ~4 × 10⁻²⁴ s |
| τ lepton | 1776.86 | −1 | ½ | 290 fs |

### Tier 4: Nuclear systems (joint modes — R29 Track 3 precedent)

Same formalism as hadrons, with higher winding on Ma_p (and
matching quantum numbers on other sheets as required).  R29 F16
listed deuteron through ⁵⁶Fe (and heavy benchmarks).  R50 revisits
a subset under **filtered** metrics to see which nuclear targets
remain good fits when R46–R49 rules are enforced on **n**.


## Tracks

### Track 1: Build `ma_model_d`

**Status:** Complete

**Goal:** Implement `studies/lib/ma_model_d.py` with filtering built in.
No scipy dependency.  **All** energy/charge/spin APIs take full
**n** ∈ ℤ⁶; there is no public "single-sheet spectrum" API that
could be mistaken for a separate search space.

**Deliverables:**
- Energy, charge, spin for arbitrary 6D modes
- Per-sheet waveguide cutoff applied to components of **n**
- Spin at finite ε (numerical path integral, numpy only)
- Mode scan with filtering over **joint** modes
- Parameter sweep utilities

### Track 2: Cross-shear sweep — neutron as first cross-sheet test

**Status:** Complete — re-run under (1,3) proton reveals structural tension

**Goal:** Sweep cross-shear parameters (σ_ep, σ_eν, σ_νp) and find
where modes near the neutron mass (939.565 MeV) appear.  Geometry
closure (positive-definite metric, reference masses preserved) is
verified as a byproduct — not a separate track.

**Re-run note (post-Track 5):** After the (1,3) proton became
the leading hypothesis, Track 2 was re-run.  The (1,3) proton's
smaller L_ring_p (4.51 fm vs 10.39 fm) creates a 275 MeV mode
spacing on the proton ring — 2.3× coarser than (3,6).  No integer
mode lands near the neutron mass.  The best (1,3) candidate is
13.6 MeV off at extreme σ_ep and unphysically high electron ring
winding (n₂ = 200).  This creates an unresolved tension:
(1,3) wins on nuclear charge formulae (Track 5) but (3,6) wins
on neutron proximity.  See findings F11–F16 addendum for details.

**Parameter discipline** (see model-D.md §Parameter strategy):

- Set default cross-shears at zero; document why (no prior data,
  sheets decouple, provides a clean baseline).
- Sweep each σ independently first, then jointly, over a generous
  range.  Record the **landscape** (how energy varies with σ), not
  just the best-fit point.
- If a cross-shear value that places the neutron near 939.565 MeV
  exists, record it as "constrained by neutron mass" with a width
  (sensitivity δm/δσ), NOT as a determined constant.
- Do **not** pin σ_ep from this single data point.  Future tracks
  will provide additional constraints (muon, pion, etc.) that may
  prefer a slightly different value.  Keep σ_ep as a free parameter
  in the model; treat the neutron constraint as one input into a
  later joint fit.
- The neutron is NOT stable (τ = 879 s).  It should be a near-miss,
  not an exact eigenmode.  If the sweep places it exactly on a mode,
  verify — something may be over-constrained.

**Deliverables:**
- σ landscape plots for each cross-shear
- Neutron candidate mode(s) with mass residual and quantum numbers
- Metric health check at candidate parameter values
- Sensitivity table: δm/δσ for each parameter

### Track 3: Full joint mode sweep

**Status:** Complete

**Goal:** At viable parameter sets from Track 2, scan **6D** modes
up to ~2 GeV (and nuclear mass targets as needed) and match against
the tier lists.

**Diagnostics:**
- For each known target: nearest mode, mass residual,
  charge/spin match
- Lifetime-residual correlation (R27's r = −0.84 result)
- Mode overcounting: how many predicted modes have no
  known physical interpretation?

### Track 4: Decay rate ↔ near-miss correlation

**Status:** Complete

**Goal:** Quantify the relationship between mass residual
(distance from nearest eigenmode) and measured lifetime.
If the off-resonance hypothesis is correct:

- log(τ) should correlate with −log(|δm|/m) or similar
- Stable particles (e, p) should sit on exact eigenmodes
- The neutron (τ = 879 s) should be a very close near-miss
- The Δ(1232) (τ ~ 10⁻²⁴ s) should be a distant near-miss

**Results (F25–F30):**
Correlation is consistently negative (correct direction)
across all 8 subsets tested, but never significant at p < 0.05.
Best subset r = −0.65 (excl. strong + muon, N = 7).  The
neutron–Ω⁻ paradox (both at |Δm/m| ≈ 0.035%, lifetimes
differ by 10¹³) proves that mass gap alone cannot predict
lifetime.  Refined hypothesis: stratified off-resonance,
where the correlation holds within each decay-channel class.

### Track 5: Nuclear modes under model-D geometry

**Status:** Complete

**Goal:** Test both proton hypotheses — (1,3) fundamental and
(3,6) composite — against R29's nuclear benchmark set (d through
⁵⁶Fe).  Resolve the charge formula tension identified in the
Track 5 framing.

**Results (F31–F36):**

The (1,3) proton hypothesis passes the nuclear test decisively:

- At σ_ep = 0, the nuclear scaling n₅ = A, n₆ = 3A reproduces
  R29's mass benchmarks to < 1% (d: 0.05%, ⁴He: 0.69%,
  ¹²C: 0.76%, ⁵⁶Fe: 0.87%).
- The fundamental charge formula Q = −n₁ + n₅ = −N + A = Z
  gives correct charge for ALL nuclei — no composite exception
  needed.
- At σ_ep = −0.13, all gaps inflate by ~3% due to uniform
  cross-shear shift — a systematic effect, not a nuclear failure.

The (3,6) hypothesis has a **structural charge problem**:

- Proportional scaling (n₅ = 3A, n₆ = 6A) gives identical
  energies to (1,3) but wrong charges with both formulas.
- Per-strand scaling (n₅ = A, n₆ = 2A) gives correct
  fundamental charges but 65% mass errors.
- No consistent scaling law works for both charge and mass.

**Key finding (F32):** The two hypotheses give **exactly
identical** nuclear energies when quantum numbers scale
proportionally.  The charge formula is the sole discriminator,
and it decisively favors (1,3).

Two nuclei (³He, ⁷Li) cannot be matched under strict R29
scaling due to topological spin parity constraints (F36).


### Track 6: Unfiltered neutron search — compound-structure approach

**Status:** Complete

**Motivation:** Tracks 2 and 5 created a tension: the (1,3) proton
wins on nuclear charge formulae but its coarse proton-ring mode
spacing (275 MeV) prevents any integer mode from landing near
the neutron mass.  The (3,6) proton has finer spacing (119 MeV)
and places a mode close to the neutron, but fails on nuclear
charges.

This tension arises because Tracks 1–5 imposed the **waveguide
cutoff filter** (`propagates()`) — a per-sheet mechanism designed
on isolated tori.  Track 6 drops this assumption.

**Key insight:** The ghost-elimination mechanism may not operate
on each torus in isolation.  When tori are coupled via cross-shears
(σ ≠ 0), energy can flow between sheets.  A "ghost" mode on one
sheet need not be destroyed by a slot — it may drain into a dark
mode on another sheet (e.g. the (1,1) electron ghost falling into
a neutrino-sheet dark winding, invisible to electromagnetism).

**Approach:**

1. **No waveguide filter.**  All Q = 0, spin-½ six-tuples are
   candidates, including modes that fail single-torus propagation.
   We assume a filtration mechanism exists but defer its form.

2. **All three proton modes on the table.**  (1,2), (1,3), and
   (3,6) each define a different L_ring_p (derived from
   E(proton_mode) = 938.272 MeV).  All are searched.

3. **Cross-shear sweep.**  σ_ep swept over [−0.3, +0.3] for
   each proton mode.  The compound structure is where the
   interesting physics happens.

4. **Catalog-first.**  Rather than filtering modes to match a
   theory of elimination, we find what modes are needed to
   explain the neutron.  If a successful candidate requires a
   mode that would fail single-torus propagation, that
   constrains the filter mechanism (it cannot be per-sheet).

**Deliverables:**
- Best neutron candidate for each proton mode (with and without
  waveguide filter, for comparison)
- Mode spacing and nearest-mode analysis per proton hypothesis
- Cross-shear landscape for unfiltered candidates
- Assessment of whether unfiltered modes resolve the Track 2
  tension

**Depends on:** Track 2 (original results for comparison),
Track 5 (charge formula constraints).

**Script:** `scripts/track6_unfiltered_neutron.py`


### Track 7: σ_ep landscape — full-spectrum optimization

**Status:** Complete

**Motivation:** Tracks 2–6 each chose σ_ep based on a single
criterion: the neutron mass gap.  This gave σ_ep = −0.13 for (3,6)
and σ_ep = −0.27 for (1,3).  But neither value has been tested
against the **full particle spectrum**.  A different σ_ep might
trade a slightly worse neutron for significantly better mesons or
baryons — or vice versa.  Without this landscape, comparisons
between (1,3) and (3,6) are biased by the choice of σ_ep.

**Approach:**

1. **Both hypotheses, side by side.**  (1,3) and (3,6), both
   unfiltered (Track 6 methodology).  Each defines its own
   L_ring_p from E(proton_mode) = 938.272 MeV.

2. **σ_ep sweep.**  For each hypothesis, sweep σ_ep over
   [−0.3, +0.3] at fine resolution.  At each σ_ep value, run
   the full Track 3 target-matching against all 19 particles.

3. **Landscape metrics.**  At each σ_ep, report:
   - Mean |Δm/m| across all targets with allowed quantum numbers
   - Number of "good" matches (< 2%)
   - Neutron gap specifically
   - Best and worst individual matches
   This produces a landscape showing how each σ_ep trades off
   different particles.

4. **σ_ep remains free.**  Report the optimal σ_ep for each
   hypothesis as a "constrained by spectrum" value with a width,
   not a pinned constant.  Future data (nuclei, higher-energy
   particles) may prefer a different value.

**Deliverables:**
- σ_ep landscape plots (metric vs σ_ep) for both hypotheses
- Optimal σ_ep for each hypothesis with width/sensitivity
- Fair side-by-side comparison at each hypothesis's best σ_ep
- Assessment of how many particles drive the optimum vs how
  many are insensitive to σ_ep

**Depends on:** Track 3 (target list and methodology),
Track 6 (unfiltered approach).

**Script:** `scripts/track7_sigma_landscape.py`


### Track 8: Lepton viability search — does the geometry support the muon?

**Status:** Active

**Motivation:** Tracks 1–7 of R50 (and R52) all left an open question:
under the corrected mode-aware shear formula and the four sign branches,
**is there any 6-tuple in the linear ℤ⁶ spectrum that could plausibly
be the muon?**  Earlier full-inventory sweeps (F23–F28) reported a "mass
desert": zero Q = −1, spin-½ modes between 5 and 200 MeV at the default
σ = 0.  But those sweeps were not focused on the muon — they swept
parameter sets and used a single coarse n-range.  We have not yet
asked the *focused* question: with broad winding ranges, all four sign
branches, and a σ grid, **can the linear spectrum reach 105.658 MeV
with the right quantum numbers at all?**

This is a different bar from Tracks 1–7.  Those tracks tried to find
*good* mass matches.  Track 8 asks the much weaker question: **does
the geometry admit any candidate at all, even a loose one?**  The
answer matters because:

1. If a viable candidate exists (Δm/m ≲ 5%, correct Q and spin), then
   the muon is geometrically possible in the linear picture.  We can
   move on without needing a compound-mode back-reaction engine.
2. If no viable candidate exists for the muon at any sign branch / σ
   value with reasonable winding ranges, then the linear ℤ⁶ spectrum
   is structurally unable to host the muon.  That is a hard result
   pointing to a missing physics ingredient — most likely a back-reaction
   ("compound mode" in the user's sense) that the current MaD engine
   does not model.  The next study would build that engine.

Either outcome is informative.  This track exists to settle which one
we are in.

**Philosophy: viable ≠ exact.**  R50's existing philosophy already
treats unstable particles as near-misses (point 3 of the philosophy
list above).  Track 8 takes that one step further: for the muon and
tau (and for completeness, the full inventory), we do **not** require
a precise match.  We require only that **at least one** mode in the
search space lands within a stated tolerance.  A 3% miss is a
"viable candidate".  A 30% miss is "no candidate".  Anything in
between we report and let the reader judge.

**Approach:**

1. **Wide candidate generation.**  6-tuples over a generous integer
   range allowing (1,1), (1,2), and (1,3) base modes on each sheet.
   Filter only by charge and spin — no waveguide filter (per Track 6
   methodology).

2. **All four sign branches.**  s_e ∈ {+, −}, s_p ∈ {+, −}.  At
   each branch, the calibration via `build_corrected_model` ensures
   the electron and proton stay pinned to their measured masses.

3. **σ_eν grid.**  Cross-shear σ_eν is the most physically natural
   coupling for a "compound mode" picture (electron base + ν dressing).
   Sweep σ_eν over a generous range; record the best candidate at
   each σ value.

4. **Per-particle search.**  For each target in the inventory
   (muon, tau, π±, π⁰, K±, η, η′, ρ, etc.) record the best candidate
   *across all branches and σ values*.  Tag with: mode, energy,
   Δm/m, branch, σ, propagation flag, active sheets.

5. **Verdict per particle.**  Apply a tolerance ladder
   (≤1% = excellent, ≤5% = viable, ≤10% = marginal, > 10% = no
   candidate).  Report a single viability table for the inventory.

**What this track does NOT do:**

- Does not claim the chosen modes are *the* correct identification
  of these particles — only that the geometry can host them.
- Does not score lifetime/stability correlation (R50 Track 4
  handles that, and mixing it in here would muddy the goal).
- Does not implement back-reaction.  If the linear spectrum fails
  to host a particle, we report that as a finding and defer the
  back-reaction engine to a future study.

**Deliverables:**

- Per-particle viability table (one row per inventory entry, one
  column per sign branch, plus an overall verdict).
- Best mode for the muon and tau, with full diagnostics.
- Histogram of Q = −1, spin-½ modes in the 5–500 MeV window
  (does the desert hold up under the wider search?).
- Honest assessment: are we in the "linear spectrum is sufficient"
  world or the "we need a compound engine" world?

**Depends on:** Track 6 (unfiltered methodology, build_corrected_model
pattern), Track 7 (σ landscape understanding), R52 (sign branch
discovery).

**Script:** `scripts/track8_lepton_viability.py`


## Design notes for `ma_model_d`

### What NOT to carry over from `ma_model.py`

- `r_p = 8.906` hard-coded
- `S34_DEFAULT` hard-coded
- Proton = (1,2) assumption
- Self-consistent iteration (useful but couples assumptions)
- scipy dependency
- Pressure harmonics and dynamic corrections (deferred)

### What to keep (reimplemented)

- 6×6 metric construction from (ε, s, σ)
- Energy from metric: E² = nᵢ G̃ⁱʲ nⱼ × scale²
- Charge formula: Q = −n₁ + n₅ (composite: divide by gcd)
- Brute-force mode scan with energy ceiling

### What to add (new)

- Per-sheet waveguide cutoff filter (on components of **n**)
- Spin at finite ε (path integral, per sheet contribution)
- Mode annotation: which sheet(s) carry winding, propagation
  status, spin value
- Near-miss finder: for a target mass, find the N closest
  **joint** modes and report residuals
- No assumptions about which modes are "the" electron,
  proton, or neutrino — those are outputs, not inputs
