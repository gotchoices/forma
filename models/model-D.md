# Model: model-D (Filtered model — `ma_model_d.py`) ⟵ ACTIVE

**Status:** Active — R50 particle census complete (Tracks 1–4)  
**Code / implementation:** [`studies/lib/ma_model_d.py`](../studies/lib/ma_model_d.py) (~1,100-line Ma engine with 6×6 coupled metric, waveguide filtering, dual proton hypothesis support — (1,3) default, (3,6) via `n_p` parameter)  
**Study range:** **R45 (catalyst) → R46, R47, R48, R49, R50** (see [`studies/STATUS.md`](../studies/STATUS.md))  
**Supersedes:** [model-C](model-C.md) (`ma_model.py`, R39–R44)

---

## Summary

Model-D is a **deliberate restart from first principles**. Rather than
inheriting model-C's pinned geometry (r_p = 8.906, σ_ep = −0.091 from
R27) and adding corrections, model-D goes back to the three
fundamental particles — electron, proton, neutrino — and rebuilds
each from scratch, asking what the torus geometry actually requires.

The key motivations for the restart:

1. **R45 showed** that single-sheet geodesic-tilting cannot explain
   proton or neutron magnetic moments — the proton's g = 5.586 needs
   multi-component or composite structure, not parameter tweaks.
2. **R46 discovered** waveguide cutoff on toroidal cavities: a hard
   mode-selection rule that model-C entirely lacks. This eliminates
   the (1,1) ghost at the physics level, not by ad hoc filtering.
3. **R47 found** that the (1,2) proton is inadequate (spindle
   ceiling, no quark phenomenology).  The **(3,6) composite** (three
   (1,2) strands) wins 8/11 criteria vs (1,2), but its composite
   charge formula breaks for nuclei.  The **(1,3) fundamental** mode
   was later reinstated when the topological spin rule (odd tube
   winding → ½) replaced the WvM ratio rule — it is now the
   **leading candidate**, solving the charge formula problem and
   paralleling the electron's ghost-killing pattern.
4. **R49 revealed** that finite-ε spin deviates significantly from
   the thin-torus formula s = n₁/n₂ used throughout models B and C.
   At large ε the deviation is qualitative, not just perturbative.

These are not incremental improvements — they change the foundations.
The old parameter pinning (r_p from neutron + muon) was **premature**:
it assumed (1,2) proton, thin-torus spin, and no waveguide filtering.
Model-D retracts those pins and treats them as predictions to be
recovered (or not) from the new physics.

Model-D is also the first model to **incorporate GRID** as more than
background.  In models A–C, Maxwell's equations were assumed as
inputs; GRID was developed in parallel but did not feed back into
MaSt physics.  Model-D closes that loop:

- **Charge as topological winding** (R48 F5): a traveling wave
  circling the tube advances its phase by 2π — this IS the GRID
  topological winding (axiom A3).  Standing waves carry zero net
  circulation and therefore zero charge (R48 F4).
- **Waveguide boundary from GRID** (R46 T5): the torus wall is a
  physical structure with GRID reflection coefficient ~(1−α) ≈ 0.993,
  close to the conducting limit.  This turns mode filtering from an
  ad hoc selection rule into a consequence of the substrate.
- **Shear chirality ↔ circulation imbalance** (R48 F5): charge
  requires more energy flowing one way around the tube than the
  other.  The embedding shear provides this asymmetry — unifying
  the R19 shear mechanism with GRID's phase-winding picture.

**Root-level documentation** ([`README.md`](../README.md),
[`STATUS.md`](../STATUS.md), [`Taxonomy.md`](../studies/Taxonomy.md))
currently describes model-C's state and should be updated to reflect
model-D's quantitative benchmarks from R50.

---

## Parameter scorecard

**Total metric parameters:** 21 (symmetric 6×6 metric on Ma)

**Philosophy:** no premature pinning.  Parameters are swept,
constrained by data, or derived from inputs — never locked
from a single particle fit.

#### Measured inputs (from experiment — not derived)

| # | Parameter | Value | What it sets |
|---|-----------|-------|-------------|
| 1 | m_e | 0.511 MeV | L₂ (electron ring circumference) |
| 2 | m_p | 938.272 MeV | L₆ (proton ring circumference) |
| 3 | Δm²₂₁ | 7.53 × 10⁻⁵ eV² | L₄ (neutrino ring circumference) |
| 4 | α | 1/137.036 | s₁₂ and s₅₆ (within-plane shears, given ε values) |

Same four inputs as model-C.

#### Derived from inputs (no additional measurement needed)

| # | Parameter | Derived from | Status |
|---|-----------|-------------|--------|
| 5 | s₁₂ | α + ε_e | Determined once ε_e is set |
| 6 | s₅₆ | α + ε_p | Determined once ε_p is set |
| 7 | s₃₄ | Δm²₃₁/Δm²₂₁ = 33.6 | 0.022 (Family A); other values for other families |
| 8 | L₂ | m_e + μ(ε_e, s₁₂) | Varies with ε_e |
| 9 | L₄ | Δm²₂₁ + μ(ε_ν, s₃₄) | Varies with ε_ν |
| 10 | L₆ | m_p + μ(ε_p, s₅₆) | Varies with ε_p |
| 11–13 | L₁, L₃, L₅ | ε × L_ring for each sheet | Varies with ε |

#### Constrained by data (not pinned — swept with documented width)

| # | Parameter | Working value | Constraint source | Range | Confidence |
|---|-----------|--------------|-------------------|-------|------------|
| 14 | σ_ep | −0.13 | Neutron mass (R50 T2) | ±0.01 | Constrained |
| 15 | ε_e | 0.65 | Waveguide: must kill (1,1), pass (1,2) | ~0.5–0.8 | Working |
| 16 | ε_p | 0.55 | Waveguide: must kill (1,1)+(1,2), pass (1,3) | ~0.33–0.6 | Working |

#### Open — under active investigation

| # | Parameter | Working value | Status | Studies |
|---|-----------|--------------|--------|---------|
| 17 | ε_ν | 5.0 (Family A) | Broadly viable 0.1–5+; 22 solutions | R49 |
| 18 | σ_νp | 0 (default) | R50 F11 suggests ~−0.13 may be nonzero | R50 T2, Q89 |
| 19 | Proton mode | (1,3) | Leading; (3,6) viable alternative | R47, R50 |

#### Set to zero (default — not tested beyond R50 T2)

| # | Parameters | Count | Justification |
|---|-----------|-------|---------------|
| 20 | σ_eν | 1 | R50 F13: zero effect on proton-scale modes |
| 21–28 | Remaining cross-shear components | 8 | No prior data; default zero baseline |

#### Genuinely free

| # | Parameter | Constraint | Note |
|---|-----------|-----------|------|
| — | r_e (= ε_e) | May be fixed by waveguide filter | If filter pins ε_e, this drops to zero free |
| — | r_ν (= ε_ν) | Cosmological Σm_ν < 120 meV | 22 viable solutions remain |

#### Pinned from unstable particles

**None.**  This is model-D's key philosophical difference from
model-C.  The neutron and muon are predictions, not calibration
targets.  No parameter is locked to a specific unstable particle
mass.

#### Summary

| Category | Count | Change from model-C |
|----------|------:|:-------------------:|
| Measured from experiment | 4 | Same |
| Derived from inputs | 9 | Same |
| Constrained (swept with width) | 3 | **New** (was 0 in model-C) |
| Open / under investigation | 3 | **New** |
| Set to zero | 9 | Reduced from 11 (σ_ep now constrained) |
| Pinned from unstable particles | **0** | **Was 2** (r_p, σ_ep from neutron + muon) |
| Genuinely free | 0–2 | Same range, but may reach 0 if filters constrain ε |

**Effective free parameters:** 0 if waveguide cutoff pins both
aspect ratios, or 2 if it doesn't.  Either way, no parameters
are fitted to unstable particle masses — all MeV-scale
predictions are genuine.

**Proton mode:** (1,3) fundamental — leading candidate.
Universal charge formula Q = −n₁ + n₅ works for particles
AND nuclei.  (3,6) composite remains a viable alternative
but requires a different charge formula that breaks for
nuclear modes.

---

## Outcomes

*Established results from foundational studies (R45–R49) plus the
R50 particle census.  Inherited results from models B/C that remain
valid under model-D's assumptions are noted as such.*

### What model-D has established so far

#### Electron sheet (R46)

- **Waveguide cutoff** eliminates the (1,1) ghost — the most
  problematic mode in models B/C (charged boson at half m_e,
  unobserved). The (1,2) electron is the **first surviving mode**
  above cutoff for n₁ = 1 on the electron sheet.
- **Aperture / slot mechanism** can produce δμ/μ = α/(2π) (the
  anomalous magnetic moment) with charge perturbation < 0.03%.
  Optimal slot geometry: h ≈ 0.98° × w ≈ 9.78° at ε = 0.5.
- **Phase-locked node filtering**: ghost (1,1) drops to < 1%
  survival; electron (1,2) retains ~100% with shear-adjusted
  slot spacing (~92.65°).
- **CP shear formula**: α_CP = μ sin²(2πs) / (4π q²), which
  relates to the R19 scalar formula as α_CP = α_R19 / r² — a
  unified charge–α relation across representations.
- **Energy partition** confirmed: ~48.5% E-field / ~51.5% B-field
  (close to 50/50, consistent with WvM).
- **Working assumption**: ε_e ≈ 0.5 if the waveguide filter fixes
  the tube-to-ring ratio. This is new — model-C left r_e
  unconstrained.

#### Proton sheet (R47, updated post-R50)

Three hypotheses have been tested.  Current status:

- **(1,2) abandoned**: spindle mechanism ceiling at g ≈ 4 vs target
  5.586.  No quark substructure, bare moment 64% too low.  Loses
  8/11 criteria vs (3,6).

- **(3,6) composite — viable alternative**: wins 8/11 criteria vs
  (1,2).  SU(6) moments μ_p = 3.000 μ_N (+7.4%), μ_n = −2.000 μ_N
  (+4.5%).  Constituent mass m_p/3 = 313 MeV.  Geometric confinement
  at ε = 1/3.  **Problem:** composite charge formula
  Q = −n₁ + n₅/gcd breaks for nuclear modes — gcd(A, 2A) = A
  collapses proton-sheet charge to 1 for all nuclei.

- **(1,3) fundamental — leading candidate**: reinstated after
  Model-D's topological spin rule (odd tube winding → ½) was
  recognized as the correct rule (replacing the WvM ratio n₁/n₂).
  Universal charge formula Q = −n₁ + n₅ works for all particles and
  nuclei.  Nuclear scaling: n₅ = A, n₆ = 3A.  Parallels the
  electron: (1,2) ghost killed by waveguide, (1,3) is first surviving
  charged mode.  Bare moment ≈ 3 μ_N.  Ring radius R ≈ 0.59 fm
  (70% of charge radius 0.84 fm).  Quarks explained as degenerate
  ringings of the 3-fold ring symmetry, probed in DIS — not
  physical substructure.  Under active testing (R50 Track 5).

  **Irreducibility argument (R33 Track 9, Q109):** gcd(1,3) = 1,
  so the mode is irreducible — its three antinodes are features of
  one standing wave, not separable sub-modes.  Confinement is
  automatic (no free quarks because there are no free antinodes).
  This contrasts with (3,6) where gcd = 3 → three separable (1,2)
  strands that require an external confinement mechanism.  The same
  criterion explains why (n, 2n) electron harmonics don't exist as
  free particles: gcd = n → n separable (1,2) strands → Coulomb
  fission.

  | Criterion | (1,2) | (3,6) | (1,3) |
  |-----------|-------|-------|-------|
  | Spin | ½ ✓ | ½ ✓ | ½ ✓ |
  | Charge formula | fundamental | composite (breaks nuclei) | **fundamental (universal)** |
  | Magnetic moment μ_p | 1.000 μ_N (−64%) | 3.000 μ_N (+7.4%) | ~3 μ_N (+7%) |
  | Constituent mass | — | m_p/3 = 313 MeV ✓ | from ring symmetry |
  | Nuclear scaling | — | charge formula tension | **n₅ = A, n₆ = 3A (clean)** |
  | Ghost killing | ε-dependent | ε = 1/3 cuts (1,2) | **ε > 1/3 cuts (1,2)** |
  | Quark structure | None | 3 strands | **3-fold ring pattern** |
  | **Status** | **abandoned** | **viable** | **leading** |

- **Slot-only κ_p ruled out**: producing κ_p = 1.793 requires
  > 100% of the sheet area as slot — physically impossible. The
  proton's anomalous moment must come from cross-sheet coupling.

#### Neutrino sheet (R49)

- **ε_ν broadly viable** across 0.1–5+ from oscillation data alone.
  Three solution families identified:
  - **Family A** (R26 assignment): (1,1), (−1,1), (1,2) at ε = 5.0,
    s = 0.022. Σm = 117.8 meV. 26 sterile modes.
  - **Family B**: ε = 0.1, Σm ≈ 65 meV. 120–128 sterile modes.
  - **Family C**: ε = 0.2, s = 0.3–0.4, Σm ≈ 63 meV. 73–82 steriles.
- **Oscillation data does not uniquely pin ε_ν** — extra physics
  (production rules, topology, weak selection) is needed.
- **Waveguide cutoff** on Ma_ν: at ε ≤ 0.2 nothing propagates (in
  the open-boundary model). Sets a floor but does not select exactly
  3 modes.
- **Finite-ε spin**: deviates from n₁/n₂ at large ε. Family A spins
  ~0.36–0.37 (deviation from ½); Family B has mixed spins (0.50 and
  0.40). Spin tolerance is a significant filter.
- **Mode density to m_e**: ~17.5 × 10⁶ modes on Ma_ν reach m_e
  energy (N ≈ 17.5M diagonal modes). Compton window λ̄_C ≈ 6.6 μm
  encompasses ~10¹³ atoms — relevant for neutrino-domain storage
  hypothesis (Q85).
- **Assignment A implies Majorana neutrinos** via C-conjugate mixing
  (Q105). Testable prediction: 0νββ at |m_ββ| ≈ 10–30 meV.

#### Helicity and charge (R48)

- **n₁ = ±1 derived geometrically** from circular polarization tube
  synchronization: only n₁ = ±1 gives a non-oscillating tube factor
  in the traveling-wave Gauss flux.
- **Helicity does NOT discriminate (1,1) vs (1,2)** — both carry
  identical charge in this model. Q104 answered negatively. Ghost
  elimination requires waveguide or slot filtering, not helicity.
- **Proton charge**: for the (1,3) proton (leading hypothesis),
  n₁ = 1 gives direct charge via the standard mechanism (same as
  electron).  For the (3,6) composite (alternative), the n₁ = 3
  tube factor oscillates → no direct charge; charge comes from
  three (1,2) strands with gcd(3,6) = 3, each carrying e/3.

#### GRID integration (R46, R48)

Previous models treated Maxwell's equations as an assumed input.
Model-D is the first to use GRID results as active physics:

- **Charge = topological winding** (R48 F5): the 2π phase advance
  of a traveling wave around the tube is GRID axiom A3 made
  concrete.  This replaces the R19 field-integral picture with a
  topological one — charge is exact because topology is exact.
- **Torus wall = GRID lattice boundary** (R46 T5): the material
  sheet has reflection coefficient ~(1−α) ≈ 0.993. This makes
  waveguide cutoff a consequence of the substrate, not an ad hoc
  filter.  Modes below cutoff cannot propagate — they are
  evanescent on the lattice.
- **Standing waves carry zero charge** (R48 F4): the Gauss integral
  is exactly zero for any standing-wave mode with n₂ ≠ 0.  Charge
  requires net circulation (a traveling-wave component), which is
  provided by shear chirality.  This unifies WvM (circulating CP
  wave), GRID (topological winding), and the shear mechanism
  (broken circulation symmetry) into a single picture.

#### Magnetic moments (R45 — catalyst for model-D)

- **Geodesic tilting via σ_ep dead**: standing wave |ψ|² is uniform
  → no classical orbit. ⟨L₆⟩ = ℏn₆ → μ = n₆ μ_N → g = 4 for
  (1,2), not 5.586. Cross-shear cannot change n₆. Tracks 1, 2,
  4 dead.
- **Surviving direction**: Track 3 — self-consistent dressed /
  multi-sheet composite angular momentum.
- **Implication**: explaining g_p, μ_n, and g_e − 2 requires
  composite or aperture physics, not single-mode adjustments.

### Retracted from models B/C

| What | Old value | Why retracted |
|------|-----------|---------------|
| **r_p = 8.906** | Pinned by neutron + muon (R27 F18) | Assumed (1,2) proton, thin-torus spin, no waveguide. Model-D treats r_p (now ε_p) as swept. |
| **σ_ep = −0.091** | Pinned jointly with r_p | Same — premature pinning. Model-D treats σ_ep as swept. |
| **Proton as (1,2)** | Model-B/C assumption | (1,3) fundamental (leading); (3,6) composite (alternative).  Both win decisively vs (1,2). |
| **Thin-torus spin s = n₁/n₂** | Used for all predictions | Finite-ε spin deviates significantly (R49). |
| **Muon as exact fit target** | R27 F18 | Off-resonance hypothesis says muon should have ~0.3% gap. Using it as exact target was inconsistent. |

### Particle spectrum (R50 — σ_ep = −0.13, ε_e = 0.65, ε_p = 0.55)

Geometry: joint 6D metric with waveguide filtering and (1,3)
proton (leading) or (3,6) composite (alternative).  Electron and
proton masses are inputs (set by
ring circumferences L_ring_e, L_ring_p); all other particles are
predictions.  No parameters pinned to unstable particle masses.

| Particle | Ma mode | Predicted (MeV) | Observed (MeV) | |Δm|/m | Grade |
|----------|---------|----------------:|---------------:|------:|-------|
| e⁻ | (1, 2, 0, 0, 0, 0) | 0.511 | 0.511 | input | reference |
| p | (0, 0, 0, 0, 3, 6) | 938.272 | 938.272 | input | reference |
| φ | (−1, 6, \*, \*, −2, −8) | 1019.9 | 1019.5 | 0.05% | good |
| n | (0, 6, \*, \*, 0, 8) | 939.3 | 939.6 | 0.03% | good |
| Ω⁻ | (−2, −6, \*, \*, −3, 13) | 1673.1 | 1672.5 | 0.04% | good |
| τ⁻ | (2, 5, \*, \*, 1, −15) | 1780.0 | 1776.9 | 0.18% | good |
| Σ⁺ | (−2, −5, \*, \*, −1, −10) | 1187.1 | 1189.4 | 0.19% | good |
| Δ⁰ | (1, −6, \*, \*, 2, 10) | 1237.0 | 1232.0 | 0.41% | good |
| Λ | (−2, 6, \*, \*, −2, −9) | 1127.7 | 1115.7 | 1.1% | good |
| Ξ⁰ | (0, 6, \*, \*, 0, 11) | 1291.4 | 1314.9 | 1.8% | good |
| η′ | (0, −6, \*, \*, 0, −8) | 939.3 | 957.8 | 1.9% | good |
| ρ⁰ | (1, −6, \*, \*, 1, −6) | 742.3 | 775.3 | 4.3% | fair |
| K⁰ | (0, −6, \*, \*, 0, −4) | 469.7 | 497.6 | 5.6% | fair |
| η | (0, 6, \*, \*, 0, −5) | 586.8 | 547.9 | 7.1% | fair |
| μ⁻ | (1, 6, \*, \*, 0, −1) | 117.2 | 105.7 | 10.9% | poor |
| π⁰ | (0, 6, \*, \*, 0, −1) | 117.5 | 135.0 | 12.9% | poor |
| π± | — | — | 139.6 | — | J impossible |
| K± | — | — | 493.7 | — | J impossible |

Neutrino quantum numbers marked `*` freely vary (Ma_ν contributes
< 0.001% of the energy at hadron scales).  Grade: good = |Δm|/m < 2%;
fair = 2–10%; poor = > 10%.

**10 of 16 unstable targets with allowed quantum numbers matched
within 2%.**  Best predictions: φ (0.05%), Ω⁻ (0.04%), n (0.03%).

### Comparison to model-C

| Property | Model-C (R27) | Model-D (R50) |
|----------|---------------|---------------|
| Free parameters | 0 at MeV scale (2 pinned: r_p, σ_ep) | 0 at MeV scale (0 pinned) |
| Proton model | (1,2) single mode | (1,3) fundamental (leading) / (3,6) composite |
| Waveguide filter | None | Per-sheet cutoff |
| Neutron | pinned (exact) | predicted (0.03%) |
| Muon | pinned (~0.3%) | predicted (10.9% — mass desert) |
| Tau | near-miss (5.6%) | 0.18% |
| Ω⁻ | structurally forbidden | 0.04% (via composite loophole) |
| φ | 0.8% | 0.05% |
| K⁰ | 1.2% | 5.6% (degraded) |
| η | 0.6% | 7.1% (degraded) |
| η′ | 0.3% | 1.9% |
| Lifetime-gap r | −0.84 (N ≈ 7) | −0.45 (N = 7, weak − muon) |
| Power law β | −2.7 | −2.7 (weak − muon, exact match) |
| Charged J = 0 mesons | 14% error (π) | topologically forbidden |
| Ghost (1,1) | ~20× overprediction | eliminated by waveguide |

**Model-D wins:** τ (31× better), Ω⁻ (impossible → 0.04%),
φ (16× better), ghost elimination, no pinned parameters.

**Model-C wins:** K⁰ (5× better), η (12× better), η′ (6× better),
muon (pinned vs mass desert), stronger lifetime correlation.

**Structural difference:** Model-C's meson accuracy came from
parameters (r_p = 8.906, σ_ep = −0.091) that were tuned to the
neutron and muon, which also happened to place meson harmonics well.
Model-D's unpinned geometry (ε_p = 0.55, σ_ep = −0.13) shifts
harmonic spacing, improving some particles and degrading others.

### Off-resonance hypothesis (R50 Track 4)

Unstable particles are near-misses to Ma eigenmodes.  The
hypothesis is **qualitatively confirmed** (correct sign in every
subset tested) and **quantitatively insufficient** as a single-
variable predictor.

The neutron–Ω⁻ paradox: both have |Δm/m| ≈ 0.035% but lifetimes
differ by 10¹³ — proving that mass gap alone cannot predict
lifetime.  Coupling strength and phase space must be included.

The power law exponent β = −2.7 (from R27) is recovered exactly
in the weak-decay subset (excluding the muon), suggesting the
functional form is real even though the absolute scale is not
predictable from mass gap alone.

**Refined hypothesis (stratified off-resonance):** Within each
decay-channel class (strong / EM / weak-ΔS / weak-leptonic /
weak-β), the correlation may hold.  Current sample sizes are too
small to confirm within-class correlations.

### Neutrino predictions

| Property | Model-D range | Model-C value | Experiment |
|----------|--------------|---------------|------------|
| Σm_ν | 63–118 meV (family-dependent) | 117.8 meV | < 120 meV (Planck 95% CL) |
| Δm²₃₁/Δm²₂₁ | 33.6 ± 0.9 (all families) | 33.6 (exact) | 33.6 ± 0.9 |
| Ordering | Normal (all families) | Normal | Favored |
| Majorana? | Yes (Assignment A, Q105) | Not addressed | 0νββ testable |
| |m_ββ| | ~10–30 meV | — | Next-gen experiments |

---

## Goals

- **Rebuild from scratch**: model electron, proton, neutrino
  individually with their own waveguide and geometric constraints
  before coupling them via cross-shears.
- **No premature pinning**: all geometry parameters (ε_e, ε_p, ε_ν,
  s, σ) are **swept**, not fixed from model-B/C's R27. The neutron
  is a **prediction**, not a calibration target.
- **Waveguide-filtered census** (R50): joint 6D mode search under
  the new rules. Compare against the full particle spectrum below
  ~2 GeV. Do the old model-B/C successes (kaon, eta, lambda, etc.)
  survive? Do new successes appear? Do ghost modes decrease?
- **Proton internal structure**: under the (1,3) hypothesis, explain
  DIS and jets from 3-fold ring symmetry.  Under (3,6), understand
  as three confined (1,2) strands.  Derive quark charges, confinement, and DIS
  structure from geometry.
- **Anomalous moments**: aperture / slot mechanism for electron
  (R46); composite / cross-sheet mechanism for proton and neutron
  (R45 Track 3, R47).
- **Pin ε_ν**: use physics beyond oscillation data (weak coupling,
  waveguide, sterile bounds) to select among the three families.

---

## Assumptions

Model-D deliberately makes **fewer** assumptions than its predecessors:

- **GRID provides the substrate** — Maxwell's equations and the
  lattice structure are derived, not assumed. The torus wall is a
  GRID boundary with reflection coefficient ~(1−α). Charge is
  topological winding (GRID axiom A3). This is new to model-D.
- **Three flat periodic sheets** (Ma_e, Ma_ν, Ma_p) — inherited,
  unchanged.
- **Particles are standing EM waves** on Ma — inherited, but
  refined: charge requires a **traveling-wave** (circulating)
  component, not a pure standing wave (R48 F4).
- **Charge from shear + topology** — the shear provides a
  circulation imbalance (more energy going one way than the other),
  which produces the GRID topological winding. For the (1,3)
  proton, charge comes directly from n₁ = 1 (same mechanism as
  electron).  For the (3,6) alternative, charge comes from strand
  sub-structure (three (1,2) with e/3 each).
- **Aspect ratio ε is physically meaningful** and may be constrained
  by waveguide cutoff (new). Working assumptions: ε_e ~ 0.5,
  ε_p ~ 0.55 (working value), ε_ν uncertain (0.1–5+).
- **Proton is (1,3) fundamental** (leading) or (3,6) composite
  (alternative) — not a simple (1,2) mode (new).
- **No pinned cross-sheet parameters**: σ_ep, σ_eν, σ_νp are swept
  in the census (new).
- **Waveguide cutoff** applies on each sheet: n_tube > |n_ring| / ε
  in the open-boundary model (new).

### What is NOT assumed (unlike models B/C)

- r_p = 8.906 (retracted)
- σ_ep = −0.091 (retracted)
- Thin-torus spin s = n₁/n₂ (replaced by topological spin)
- Muon as exact fit target (replaced by near-miss philosophy)
- Proton as (1,2) single mode (replaced by (1,3) / (3,6))

### Parameter strategy

Model-C's failure mode was **premature pinning**: r_p = 8.906 and
σ_ep = −0.091 were locked from a single neutron+muon fit (R27 F18),
then treated as known constants in all subsequent work.  When the
proton model changed from (1,2) to (1,3)/(3,6), those pins became
wrong but had already propagated into dozens of calculations.

Model-D's parameter discipline:

1. **Defaults, not pins.**  Every parameter in `ma_model_d.py` has
   a default value, but defaults are working assumptions — not
   measured constants.  Each default has a documented *reason* and
   a stated *confidence*.

2. **Provenance.**  Every default records WHERE it came from (which
   study, which finding) so that when the source is revised, the
   downstream consequences are traceable.

3. **Free variables stay free.**  When a parameter is constrained
   by one data point (e.g., σ_ep from the neutron mass), record
   it as "constrained by X" — not "determined."  A second data
   point might prefer a slightly different value, and the model
   should accommodate that tension rather than break.

4. **Sweep before pin.**  Before treating any parameter as fixed,
   sweep it across a range and look at the sensitivity landscape.
   If the landscape is flat (many values work equally well), the
   parameter is not actually constrained.  If it's steep, the
   constraint is real — but record the width, not just the peak.

5. **Ephemeral targets are near-misses.**  Unstable particles
   should NOT sit on exact eigenmodes.  Using them to pin
   parameters forces exact agreement where nature gives a near-
   miss.  Decay rate ∝ distance from resonance; pinning to zero
   distance contradicts the model's own prediction.

This strategy is implemented in `ma_model_d.py`'s `from_physics()`
constructor, where each default is documented with its source and
confidence level.

---

## Strategies / approach

| Study | Focus | Status |
|-------|-------|--------|
| **R45** | Magnetic moments — found single-sheet geodesic tilting dead; motivated composite / aperture direction | On hold (catalyst) |
| **R46** | Electron filter — waveguide cutoff, slot mechanism for g−2, ghost elimination, CP shear formula | Complete (T1–T5) |
| **R47** | Proton geometry — (1,2) abandoned, (1,3) reinstated as leading, (3,6) viable alternative, spindle ruled out, SU(6) moments | Track 7 complete |
| **R48** | Helicity and charge — n₁ = ±1 derived geometrically, helicity doesn't discriminate ghosts | Complete (T1–T2) |
| **R49** | Neutrino sheet — ε_ν sweep, three families, waveguide, spin at finite ε, Majorana prediction | Tracks 1–2a complete, on hold |
| **R50** | **Filtered multi-sheet mode search** — joint 6D census under all new rules | **Track 4 complete** — 19-particle spectrum established |

### R50 design (the census)

R50 is the integration study where model-D produced its first
quantitative particle predictions. Key design choices:

- **One system**: Ma treated as a single coupled 6D metric, not
  three independent sheet catalogs.
- **Joint metric**: E² = Σᵢⱼ G̃ⁱʲ nᵢnⱼ × (ℏc/L_ref)², with
  cross-shear blocks active.
- **Per-sheet filters**: waveguide cutoff on Ma_e, Ma_ν, Ma_p;
  n₁ = ±1 for charged EM modes on Ma_e.
- **Charge**: Q = −n₁ + n₅ (fundamental — used for (1,3) proton and
  all nuclear modes).  Q = −n₁ + n₅/gcd(n₅,n₆) for composites like
  (3,6) proton (R47 F4), but this formula breaks for nuclei.
- **Parameters swept**: ε_e, ε_p, ε_ν, s₁₂, s₃₄, s₅₆, σ_ep, σ_eν,
  σ_νp — with α and particle masses as constraints.
- **Neutron as prediction**: not used to pin parameters. Success
  criterion: does a neutron-like mode (Q = 0, spin ½, m ≈ 939.6 MeV)
  appear without being forced?
- **Targets**: electron (input), proton (input), then — as
  predictions — neutron, muon, kaon, eta, eta prime, phi, lambda,
  sigma, neutrino triplet, nuclei (R29 scaling law).

---

## Limitations

### From R50 census

- **Charged pseudoscalar mesons (π±, K±) are topologically
  forbidden.**  The additive spin rule (J = number of odd per-strand
  tube windings × ½) forces Q to be even when J = 0.  Charged J = 0
  modes cannot exist.  The proposed resolution — QM spin addition
  (antiparallel alignment of two spin-½ components) — is standard
  quantum mechanics, but whether the torus geometry supports two
  strands with opposite tube orientations within a single mode is
  unresolved.  This is model-D's most significant structural failure.
- **Muon mass desert.**  No eigenmode exists between ~0.2 MeV
  (electron ring scale) and ~116 MeV (proton ring scale).  The muon
  (105.7 MeV) sits in this gap with a 10.9% residual.  This is
  structural — it follows from m_e/m_p ≈ 1/1836 — and no parameter
  adjustment within the current three-sheet geometry can fix it.
  Model-C avoided this by pinning the muon as a fitted parameter.
- **K⁰ and η degraded.**  These model-C successes (1.2%, 0.6%)
  degrade to 5.6% and 7.1% under model-D's unpinned geometry.
  Whether σ_ep or ε_p optimization can recover them without
  degrading the baryon matches is an open question.
- **Mode overcounting (~30,000:1).**  ~567,000 propagating modes
  below 2 GeV for 19 target particles.  Most are label-degenerate
  (varying neutrino/electron dressings at negligible energy), but
  even after removing label degeneracy, ~200–400 physically distinct
  energy levels remain for ~19 targets (15–25× overcounting).
- **Neutron decomposition concern.**  The best neutron candidate
  (0, 6, \*, \*, 0, 8) has n₁ = 0 — no tube winding on the electron
  sheet.  Beta decay (n → p + e⁻ + ν̄_e) requires a charged electron
  (n₁ = 1).  Whether "dark" electron-ring winding can redistribute
  into charged components when cross-sheet coupling is removed is
  an open question.
- **Off-resonance hypothesis insufficient as single-variable
  predictor.**  The neutron and Ω⁻ have nearly identical |Δm/m|
  (~0.035%) but lifetimes differing by 10¹³.  Mass gap alone cannot
  predict lifetime; coupling strength and phase space must be
  included.

### Pre-existing (from R45–R49)

- **α still circular**: shear s is still reverse-engineered from α,
  not derived from geometry. The CP shear formula (R46) unifies
  representations but does not break the circularity.
- **Proton mode selection**: two hypotheses remain — (1,3)
  fundamental (leading, solves charge formula problem) and (3,6)
  composite (viable, strong quark phenomenology).  For (3,6), how
  three (1,2) strands bind is described but not derived from first
  principles.  The waveguide cutoff at ε = 1/3 is suggestive but the eigenmode
  structure of a composite toroidal cavity is unresolved.  R33 Track 9
  adds a structural argument for (1,3): its irreducibility
  (gcd = 1) makes confinement automatic, while (3,6) (gcd = 3)
  requires an external mechanism to prevent strand separation (Q109).
- **Flavor (u/d quarks)**: the model produces three strands with
  e/3 charge but does not yet explain two quark flavors or the
  u/d mass splitting.
- **Finite-ε spin**: the deviation from n₁/n₂ is characterized but
  the correct spin formula at arbitrary ε is not yet settled. This
  affects which modes pass the spin-½ filter.
- **ε_ν not pinned**: three solution families remain viable. More
  physics is needed to select.
- **Sterile neutrino tension**: all families predict 15–128 sterile
  modes on Ma_ν, but N_eff = 3 from cosmology requires sharp weak
  coupling to suppress them. Mechanism not yet modeled.
- **Inherited open problems**: α from first principles, Compton
  window Q factor, hierarchy problem, moduli potential — all
  unchanged from model-C.
- **Root documentation lag**: README.md, STATUS.md, and Taxonomy.md
  still describe model-C.

---

## Notation changes from model-C

| model-C | model-D | Reason |
|---------|---------|--------|
| r_e, r_p, r_ν (aspect ratio = a/R, can be > 1) | ε_e, ε_p, ε_ν (same quantity, new symbol) | Align with Taxonomy §2.1; ε ≤ 1 for ring tori, avoids overloading "r" |
| Proton mode (1,2) | Proton mode (1,3) fundamental (leading) / (3,6) composite | R47 Track 7, R50 review |
| r_p = 8.906 (pinned) | ε_p swept (working value 0.55) | Premature pinning retracted |
| σ_ep = −0.091 (pinned) | σ_ep swept | Premature pinning retracted |
| spin = n₁/n₂ | spin from finite-ε formula | R49 |

---

## References

- **Studies (model-D era):**
  [R45](../studies/R45-magnetic-moments/README.md) (catalyst),
  [R46](../studies/R46-electron-filter/README.md),
  [R47](../studies/R47-proton-filter/README.md),
  [R48](../studies/R48-helicity-charge/README.md),
  [R49](../studies/R49-neutrino-filter/README.md),
  [R50](../studies/R50-filtered-particle-search/README.md)

- **Predecessor:** [model-C.md](model-C.md) (R39–R44, `ma_model.py`)

- **Code:**
  [`studies/lib/ma_model_d.py`](../studies/lib/ma_model_d.py) (~1,100 lines)

- **Key QA:**
  [Q100 (aperture moment)](../qa/Q100-aperture-moment-enhancement.md),
  [Q104 (helicity and charge)](../qa/Q104-helicity-forces-n2.md),
  [Q105 (Majorana from C-conjugate)](../qa/Q105-majorana-from-c-conjugate-mixing.md),
  [Q102 (neutrino neutrality)](../qa/Q102-neutrino-neutrality-from-sheet-size.md),
  [Q103 (anomalous moment from defect)](../qa/Q103-anomalous-magnetic-moment-from-defect-cost.md),
  [Q109 (mode stability and fission)](../qa/Q109-mode-stability-and-composite-fission.md)
