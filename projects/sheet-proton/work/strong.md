# strong.md — Yukawa-mediator path to the strong force

**Status:** Exploratory work file. Captures the working hypothesis for deriving a strong-force regime in metric-binding via wave-mediator analysis. Not yet chapter-level prose; expect this file to evolve, fork into focused sub-files (`mediator-mass.md`, `qm-gate.md`, `multi-nucleon.md`), and eventually crystallize into chapter 3–5 content.

**Tone:** Discovery-driven. Mark open questions with **TODO:**. Mark candidate-not-confirmed conclusions with *italics*. Mark dependencies on other work with cross-references.

---

## 1. Problem framing

metric-binding's stated promise: force laws emerge from sheet geometry rather than being imported. Specifically, the question for this work file is whether a **strong-force regime** (short-range, strongly attractive, going to zero at large separation) can be derived from the same geometric structure that gives EM Coulomb at long range.

The wave-only commitment: no "glue particles." Force-mediating excitations are wave modes on the sheet (or related sheets) with definite Compton wavelengths. The pion's role in Yukawa's 1935 theory is the right starting frame — the pion *as a field* gives the strong force its range; the pion *as a particle* is a later QFT reinterpretation.

Working hypothesis: there exists a **mediator mode** on the proton sheet (or accessible to it) with Compton wavelength λ_m ≈ 1.4 fm. Two-nucleon interactions on the sheet feel a Yukawa-shaped attraction mediated by this mode at short range, plus the standard Coulomb-α interaction at long range. The regime crossover happens at r ≈ λ_m.

The structure to derive:

<!-- V_total(r) = α·ℏc·q₁q₂/r - g²·exp(-r/λ_m)/r -->
$$
V_{\mathrm{total}}(r) \;=\; \frac{\alpha\, \hbar c\, q_1 q_2}{r} \;-\; g^2\, \frac{e^{-r/\lambda_m}}{r}
$$

The hard question is not the form (Yukawa was right about that) but **where m_mediator and g come from in MaSt's geometric language**.

---

## 2. Five-step derivable path

The development structure to follow, in dependency order:

### Step 1 — Identify the mediator mode in the proton-sheet spectrum

**Question:** Does the proton sheet's mode spectrum contain a configuration at ~140 MeV that could naturally mediate between nucleons?

**Computation:** Sweep the mode spectrum μ²(n_t, n_r) = (n_t/ε)² + (n_r − s·n_t)² at R64's proton-sheet (ε, s) parameters (both Point A and Point B). Catalog all closure-satisfying configurations by mass.

**Expected:** Single primitives T(1, n') sit near μ ≈ 1/ε ≈ 13.7 → mass ≈ 320 MeV (in framework units where μ = 41 ≈ 938 MeV). This is way above 140 MeV. So the pion is likely **not** a single primitive on the proton sheet.

**Implication:** The mediator must be either a multi-component compound (lighter than constituents due to binding) or a mode on a different sheet (electron sheet has very different ε; might admit lighter modes).

**TODO:** Compute the full mode spectrum at (ε_p, s_p) = (0.073, 0.194). List all closure-satisfying configurations under μ < 10. None? Few? Many?

### Step 2 — Derive the mediator's mass

**Question:** Why does the mediator come out at ~140 MeV rather than some other value?

**Three candidate paths, all worth tracking:**

- **2a. Chiral-symmetry-breaking analog.** In QCD, the pion is a (pseudo-)Goldstone boson of spontaneously broken chiral symmetry. Its small mass is structurally protected. In MaSt: is there a sheet-level symmetry that, when spontaneously broken, gives a light "rolling mode"? Candidates: the (m, n) → (−m, n) chirality reflection, or the (m, n) → (m, −n) handedness reflection. If one of these is approximately a symmetry but slightly broken (by σ_uw shear, perhaps), the corresponding mode would be light. **TODO:** Examine the proton sheet's symmetry group at R64 (ε, s) parameters. Identify candidate spontaneously broken symmetries.

- **2b. Specific compound from mode spectrum.** Per Step 1: the mediator might be a multi-component compound. The qq̄ structure of QCD pions maps in MaSt to a 2-component compound T(m, n) + T(−m, −n) (particle + sign-reflected antiparticle). The naive summed winding is (0, 0), so the dispersion mass is zero. What lifts it to 140 MeV? Possible: internal phase structure, sheet anisotropy, σ_uw shear. **TODO:** Compute the energy of a (T(1, 2) + T(−1, −2)) compound on the proton sheet, including any binding/sheet-coupling corrections. Does it land near 140 MeV?

- **2c. Phenomenological fit.** Treat m_mediator as a free parameter and fit it to nuclear binding data. The fitted value gives a target for the geometric derivation. Cleaner-honest fallback if 2a and 2b don't yield.

The honest framing: **2a is the deepest, 2b is the most computable, 2c is the most pragmatic**. Run 2c in parallel as a sanity check; pursue 2b actively; keep 2a as a long-term target.

### Step 3 — Two-body Schrödinger with Coulomb + Yukawa

Once λ_m is determined (from any of 2a/2b/2c), compute bound-state spectra for two-nucleon configurations.

**Computation:** Schrödinger equation:

<!-- -ℏ²/(2μ) ∇²ψ + V(r)ψ = Eψ -->
$$
-\frac{\hbar^2}{2\mu_{\mathrm{red}}}\, \nabla^2 \psi \;+\; V(r)\, \psi \;=\; E\, \psi
$$

with μ_red the reduced mass and V(r) from §1. Standard radial-equation eigensolver in 3D.

**Implementation:** ~100 lines of Python with a numerical eigensolver. Reuse R64 Track 7's E(r) machinery (already computes the kinetic and cross-coupling terms); add the Yukawa exchange piece.

**TODO:** Implement and test. Reference: scripts/work_strong_qm.py (to be written).

### Step 4 — Pass the QM gate

The deuteron + pp + nn three-test gate that R64 Phase 7d *failed*:

| System | Observation | Test |
|---|---|---|
| Deuteron (pn, spin-1) | 1 bound state at −2.224 MeV | Must reproduce |
| Pn singlet (spin-0) | Unbound (no s-wave bound state) | Must reproduce |
| pp (any spin) | Unbound | Must reproduce |
| nn | Unbound | Must reproduce |

R64 Phase 7d failed by predicting 3 pn bound states and spurious pp/nn binding. **The Yukawa-with-exponential-cutoff form has more flexibility than R64's 1/r² + α/r model** — the exponential suppression beyond λ_m should naturally kill pp/nn at typical nucleon separations.

**Specific prediction to check:** At what value of (g², λ_m) does the QM gate pass with exactly the right deuteron binding energy and no spurious bound states?

**TODO:** Run the gate. If it passes for some (g², λ_m) without arbitrary tuning, that's substantive evidence. If it fails everywhere, the Yukawa picture has the same problem as the R64 cross-coupling picture.

### Step 5 — Extend to nuclear chart

If the two-body gate passes, scale to A ≥ 3 (deuteron-like cluster, ³He, ⁴He, then heavier). This is where R64 currently has the 88% binding-energy deficit.

**Open question:** does the Yukawa form, combined with multi-body harmonic-stack effects, account for nuclear binding through the chart, or does it fail in the same place R64 fails?

**TODO:** Defer until Steps 1–4 are settled. Likely needs a separate work file (`multi-nucleon.md`).

---

## 3. The mediator-mass question — the central open issue

Among the five steps, **Step 2 is the load-bearing one**. Steps 1, 3, 4 are computational and tractable. Step 5 is heavy lifting but doesn't change the framework. Step 2 is where the structural argument lives.

**Three things to keep separate in the work:**

- **Why a mediator mode at all?** (geometric necessity)
- **Why this particular mass?** (mass calibration)
- **Why this coupling strength g²?** (vertex calibration)

Standard QCD has answers to all three: confinement gives mediators (gluons, gluon condensates); chiral symmetry breaking gives small pion mass; the coupling is renormalization-running. MaSt needs analogs for each.

**Tracking-table for the candidate derivations:**

| Question | 2a Chiral-analog | 2b Compound mode | 2c Phenomenological |
|---|---|---|---|
| Existence of mediator | Goldstone of broken symmetry | T(m,n) + T(−m,−n) compound | Fitted |
| Mass ~140 MeV | Protected by approx symmetry | From compound energetics | Fitted |
| Coupling g² | Symmetry-breaking scale | Compound-nucleon overlap | Fitted |
| Difficulty | Hard (deep MaSt structure) | Medium (computational) | Easy |
| Falsifiability | High | Medium | Low |

The right priority: **start with 2b** (most computable, real falsifiability), **run 2c in parallel** (sanity check), **frame 2a as long-term target**.

---

## 4. Computational plan

Scripts to write, in order:

1. `mode-spectrum-sweep.py` — compute the full closure-satisfying mode spectrum at given (ε, s). List all configurations under some mass cutoff. (Step 1)

2. `qq-bar-compound.py` — compute the energy of 2-component compounds T(m, n) + T(−m, −n) on the proton sheet. Test whether any land near 140 MeV. (Step 2b)

3. `coulomb-yukawa-bound-states.py` — Schrödinger solver with V_total(r) from §1. Outputs bound-state energies as a function of (g², λ_m). (Step 3)

4. `qm-gate.py` — runs the three-test gate (deuteron + pn singlet + pp/nn) using output of script 3. Reports pass/fail at each (g², λ_m). (Step 4)

5. `nuclear-chart.py` — many-body extension; deferred. (Step 5)

**Reusable from R64:**
- Track 7's E(r) framework already computes nucleon configurations on the proton sheet
- Track 7e's α-decoupling check gives baseline for α-handling
- Track 11's harmonic-stack mass formula is reusable for the compound-energetics piece

**New components:**
- Yukawa exchange term (not in R64's existing model)
- Mediator mode identification
- QM gate (R64 Phase 7d implementation exists; need to adapt to new V(r))

---

## 5. Compton-scale switching — the phenomenological parallel track

Earlier in development, the user proposed a simpler model: two regimes (common-mode in Ma vs S-separated), switching at a Compton-like distance. The Yukawa-mediator path is the structural derivation of this idea; the Compton-switching is the phenomenological probe.

**Run both in parallel:**

- **Phenomenological:** posit V(r) with a sharp switch at r* (free parameter); fit r* to nuclear binding; see what value comes out.
- **Structural:** derive the Yukawa mediator from steps 1–2; predict λ_m from MaSt geometry; check if it matches the fitted r*.

If the phenomenological r* lands near the structurally-derived λ_m, that's evidence the derivation has the right physics. If they disagree by an order of magnitude, something's off.

**TODO:** Implement the phenomenological model first (it's easier). Use it to bracket the expected λ_m before pursuing the harder structural derivation.

---

## 6. Open structural concerns to track

A running list of issues that aren't fully resolved and might bite:

- **Does the proton-sheet mode spectrum actually contain a mediator at the right mass?** (Step 1 might come up empty.) If so, the mediator is on a different sheet or is a multi-sheet compound, and the analysis gets harder.

- **Does the framework's closure rule support multi-sheet mediator exchange?** [metric-charge chapter 4](../../metric-charge/04-the-closure-condition.md) handles single-sheet multi-links. Multi-sheet exchange (pion crossing between proton-sheet and proton-sheet via some bridge) is not in chapter 4's scope. Might need extension.

- **How does the standing-wave reading of nucleons interact with the propagating mediator?** Per [metric-mass chapter 5](../../metric-mass/05-metric-self-consistency.md), particles are *directionless* standing waves — they don't have an internal direction of propagation. The mediator, by contrast, is a propagating mode (it has direction). How do these two pictures interact mathematically? Specifically: when a mediator wave passes through a standing-wave nucleon configuration, what's the coupling?

- **The R64 88% binding-energy deficit for heavy nuclei.** Even if the Yukawa picture passes Step 4 (two-body), Step 5 (multi-body) faces the same hard question R64 currently faces. Maybe Yukawa solves it, maybe not.

- **Mass-vs-charge framing.** Per [metric-mass chapter 5 §6](../../metric-mass/05-metric-self-consistency.md): the project's choice to read u as mass-generating (vs KK's charge-generating) is a framing choice with consequences. The mediator's coupling to the nucleon involves both compact directions; how does the m-vs-charge interpretation affect the mediator-nucleon vertex?

- **Compatibility with R64's two-point proton fit.** Point A and Point B fit different observables (deuteron vs heavy nuclei) but are mutually exclusive. The mediator analysis needs to commit to one (or unify them). Which?

---

## 6a. Strong force as least-energy multi-baryon coexistence (hypothesis)

The Yukawa-mediator picture (§§1–4) treats the strong force as a propagator exchange between two distinct nucleons. A complementary structural reading is available, especially relevant once the clover-substrate picture from [clover-quarks.md](clover-quarks.md) and [clover-mass.md](clover-mass.md) is in play:

**The strong force is the least-energy calculus of multi-baryon mode coexistence on a shared (or coupled) compact-dimension space.**

The leading test case is the deuteron (np bound state, binding energy 2.224 MeV). Under the clover picture each nucleon is a wave-mode configuration on a corrugated torus. The deuteron would then be a configuration where:

- Both a proton-like (uud, 2 lobes + 1 saddle) and a neutron-like (udd, 1 lobe + 2 saddles) mode coexist on *the same* corrugated torus (or two strongly coupled tori).
- The total energy of this joint configuration is *lower* than the sum of two isolated nucleons by exactly 2.224 MeV.
- The binding is a structural feature — modes that share the surface naturally reorganize to a lower-energy collective state.

If this reading is correct, the strong force is **not** a separate field with its own mediator-particle in the usual QFT sense. It is the geometric tendency of compatible wave modes to lower their total energy when sharing a compact-dimension substrate. The "Yukawa propagator" of §§1–4 would then be the long-wavelength approximation of this geometric tendency, valid at distances large compared to the surface scale.

**Concrete consequences if this framing holds:**

1. **The deuteron binding 2.224 MeV is computable** from a single mass-eigenvalue calculation on a "two-nucleon-sharing" surface, with no free coupling constant. Compare to the proton-mass setup of clover-mass.md §6.
2. **Nuclear binding energies of larger nuclei** follow the same calculus: A nucleons share a (suitably enlarged) surface; the total mode-energy of the collective configuration is the bound-state energy.
3. **The strong force range** ≈ 1.5 fm emerges as the surface size — modes farther apart than that can't share the same substrate efficiently.
4. **The "pion as mediator"** picture (§§1–4) is then a particle-physics phenomenology: when nucleons exchange long-range disturbances, those disturbances look like pion-shaped wavepackets. But the *underlying* physics is geometric coexistence, not particle exchange.

**Status:** Hypothesis. To develop, we would need to:

- Define what "two nucleons sharing a surface" means geometrically — a larger corrugated torus? Two surfaces with cross-coupling? A direct sum of two clover spaces?
- Compute the lowest-energy mode of this joint configuration and verify it differs from 2 × m_nucleon by ~2.2 MeV.
- Show that the predicted scaling for larger A matches the semi-empirical mass formula (volume, surface, asymmetry, Coulomb, pairing terms).

These are not done. The first concrete step is the deuteron — one extra constraint on top of the m_p/m_n inversion already worked through in clover-mass.md.

**Relationship to Yukawa (§§1–4):** the two are not mutually exclusive. The Yukawa picture is *empirically* well-tested at distances ≳ 1 fm and matches phenomenology; the least-energy-coexistence picture is *structurally* simpler and matches the framework's geometric foundation. Both should converge if correct — the Yukawa exchange should fall out of the long-wavelength limit of the geometric calculation.

---

## 7. Connection to the standing-wave reading

The metric-mass chapter 5 commitment — particles are directionless standing waves, not single-direction traveling modes — should carry through into metric-binding. In the Yukawa-mediator picture:

- **Nucleons** = standing-wave configurations on the proton sheet, at specific (m, n) windings.
- **Mediator** = a propagating mode that couples between nucleon configurations. The mediator *does* have a direction of propagation (it propagates between two nucleons); it's not directionless.

So the framework distinguishes:
- **Particles** (standing waves, directionless, localized)
- **Mediators** (propagating waves, directional, ranged)

This distinction matches the QFT distinction between *particles* (field excitations bound to a location) and *virtual exchange particles* (propagating disturbances mediating interactions). MaSt's wave reading makes this more natural: a mediator wave isn't a "virtual particle"; it's an actual propagating perturbation, with its own wavelength and propagation speed.

**TODO:** Make this distinction explicit in chapter 3 or 5. Nucleons and mediators are different *kinds* of mode on the same sheet.

---

## 8. Pointers to R-track studies

The Yukawa-mediator path engages directly with several R64 findings:

- [R64 Phase 7b](../../../studies/R64-nuclear-harmonic-stack/) — Yukawa-fit analysis showing E(r) follows neither pure Yukawa nor pure Coulomb in R64's current model. **Relevance:** the Yukawa picture needs to either explain why pure Yukawa doesn't fit (e.g., because both Yukawa and Coulomb contribute), or improve on R64's existing parameterization.

- [R64 Phase 7d](../../../studies/R64-nuclear-harmonic-stack/) — QM gate failure with R64's 1/r² + α/r model. **Relevance:** the Yukawa picture must pass this gate.

- [R64 Phase 7e](../../../studies/R64-nuclear-harmonic-stack/scripts/track7_phase7e_alpha_integration.py) — α decoupling from σ_pS_tube coupling. **Relevance:** confirms α stays at baseline; the mediator-coupling g² is independent of α. Different physics from EM.

- [R64 Phase 11c](../../../studies/R64-nuclear-harmonic-stack/) — Walked-back "strong force in the metric" attempt via metric singular limit. **Relevance:** previous geometric attempt; Yukawa picture is the alternative.

- [R64 STATUS](../../../studies/R64-nuclear-harmonic-stack/STATUS.md) — Three open paths for strong force: Pool item m (Yukawa propagator with geometric reading), compound-mode internal structure, standard nuclear physics overlay. **Relevance:** this work file pursues Pool item m, but does so within metric-binding rather than R64.

The Yukawa-mediator path can be viewed as the structural complement to R64's empirical fitting: R64 measures E(r) and tries various coefficient combinations; this work file derives E(r) from a specific mediator picture and predicts the coefficients. If both converge on the same answer, the framework is robust.

---

## 9. Next actions

In order, to make the work file develop:

1. **Identify candidate mediator modes** (Step 1 computation, `mode-spectrum-sweep.py`). Concrete deliverable: a list of mode configurations under mass M_max on the proton sheet at R64 parameters.

2. **Compute qq̄ compound masses** (Step 2b computation). Concrete deliverable: does any 2-component compound land near 140 MeV?

3. **Run the phenomenological Compton-switching probe** in parallel (§5). Concrete deliverable: fitted r* compared to expected λ_π.

4. **Implement Coulomb-Yukawa QM solver** (Step 3 + Step 4). Concrete deliverable: pass/fail on the deuteron QM gate, with the parameters that work (if any).

5. **Iterate.** Update this file as findings come in. Spawn focused sub-files (`mediator-mass.md`, `qm-gate.md`) as needed.

---

## Glossary / shorthand

- **Mediator mode**: a wave mode on the sheet that propagates between localised nucleon configurations and produces the strong force at short range. The MaSt-language analog of the QCD pion.
- **QM gate**: the three-test compatibility check (deuteron bound, pn singlet unbound, pp/nn unbound). A model that fails this gate predicts the wrong bound-state spectrum and is ruled out.
- **λ_m**: Compton wavelength of the mediator. Sets the range of the strong-force regime.
- **g²**: coupling strength of the mediator to nucleons. Sets the depth of the Yukawa well.
- **R64 Phase 7d**: the specific R64 calculation that failed the QM gate with the previous cross-coupling model.
- **Compton-switching probe**: phenomenological model with a sharp regime switch at characteristic distance; runs in parallel to the structural Yukawa derivation as a sanity check.
