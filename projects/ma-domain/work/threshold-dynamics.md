# threshold-dynamics.md — outline of a threshold-based mechanism for decay and production

**Status:** PRELIMINARY — parked, not yet developed. This is an early-stage outline, deliberately not built out. It frames the architecture, names the central open questions, and sets up the production-from-injection scenario whose resolution would be the framework's load-bearing result. **Do not expand the file body until the mechanism questions in §6 have working answers** (see §11 for the gating preparatory work). This is a file to return to at the right time, not an active workstream.

This is the threshold-theory parallel to [leakage-rate.md](leakage-rate.md). Where leakage-rate computes decay rates from the complex pole of a Green's function under standard quantum-mechanical assumptions, threshold-dynamics aims to derive particle creation and decay as **band-energy reorganization into eigenmode quanta** on continuous-amplitude wave dynamics — providing a concrete physical mechanism rather than a statistical postulate.

**Cross-references:**
- [grid-saturation](../../grid-saturation/) — the concrete computational testbed for this mechanism: a 1D-space + 1D-compact **(x,c) cylinder** in which head-on photons drive the substrate to **saturation**, redirecting energy S→c (pair production). Treats the saturation bound as *the* nonlinearity and proposes an energy-conserving **spillover** node (excess on a saturated edge spills into the orthogonal edge). This file's γ→e⁺e⁻ "production-from-injection" test is grid-saturation's milestone M2.
- [zpe_derivation.md](zpe_derivation.md) — the companion deriving ½ℏω₁ as the sub-fundamental band's average preload baseline; this file's two postulates are stated there
- [mode-stability.md](mode-stability.md) — the leakage-mechanism planning document
- [leakage-rate.md](leakage-rate.md) — the resonance-pole / FGR calculation, the framework's other parallel
- [architecture.md §3.3.1](architecture.md) — closure condition T(1, n) partitioning eigenmodes into particle and non-particle
- [../../../primers/threshold-theory.md](../../../primers/threshold-theory.md) — the Reiter loading-theory primer this framework's program inherits

---

## 1. Goal

The framework aims to establish:

> **Particle creation and decay are physical reorganizations of continuous sub-eigenmode band energy into and out of discrete eigenmode quanta, not statistical postulates of quantum measurement. Under specific energy-injection conditions, the framework predicts particle production deterministically (not probabilistically), subject to conservation laws.**

If the framework can show that injected sub-eigen band energy snaps into a particle quantum when conservation conditions are met, threshold dynamics earns its place as a **concrete mechanism** for both decay and production — replacing or grounding the standard statistical picture.

---

## 2. The corrected architecture

The architecture that the previous draft got wrong is now laid out plainly.

### 2.1 Eigenmodes are amplitude-quantized

On a compact periodic dimension of circumference L, single-valuedness restricts the eigenmode spectrum to integer-n with frequencies ω_n = n·ω₁ where ω₁ = 2πv/L. **Per Postulate 1 (de Broglie per-cycle action = h), the amplitude of any stable eigenmode is quantized.** Each cycle of the wave at frequency ω carries energy ℏω; for N quanta the amplitude is A_N = √N · √(2ℏ/ω). The eigenmode either holds 0, 1, 2, ... integer quanta — never a fractional occupation.

This is the framework's foundational consequence of Postulate 1. No "continuous amplitude on the fundamental" is possible. Eigenmode amplitudes are discrete.

### 2.2 Sub-eigen frequency bands carry continuous reservoirs

Between adjacent eigenmode frequencies (0 ↔ ω₁; ω₁ ↔ ω₂; ω₂ ↔ ω₃; ...) lie continuous bands of frequencies at which no stable mode can exist. Waves at these frequencies are **transient virtual fluctuations** — they fail the periodic boundary condition and dissipate without forming stable modes.

The individual fluctuations are discrete (each carries ℏω at its own frequency per Postulate 1). The **band as a continuum of frequencies** provides the continuous reservoir: the sum of fluctuation energies across the band's frequency range can take any continuous total value, even though each fluctuation contributes a discrete amount.

The continuity is in the *frequency variable*, not in the per-frequency amplitudes.

### 2.3 Snap is a band-to-eigenmode reorganization

When the integrated energy in a sub-eigen band crosses the relevant eigenmode threshold (ℏω_n for the next quantum at mode n), the continuum of transient fluctuations can collapse coherently into one quantum of the eigenmode. The eigenmode amplitude jumps from A_N to A_{N+1} in a discrete step. The band's energy is consumed.

**The snap is a physical event in the field, not a measurement projection.** It happens because the reorganized configuration (one quantum at the eigenmode) is the available lower-free-energy state once the band has accumulated enough energy. The reverse — eigenmode quantum unloading into sub-eigen band — is decay.

### 2.4 Detection on the embedding side

Particle modes (closure-satisfying T(1, n) per [architecture.md §3.3.1](architecture.md)) couple to embedding-space detectors via per-arc charge structure. A snap event at a particle mode registers as a "particle observed" by S-side detectors. Non-particle modes (closure-failing T(m_t, 0), T(0, m_r), T(p ≥ 2, q ≥ 2)) carry their own eigenmode quanta but do not register as particles — candidates for dark-sector content.

Detector observation is the embedding-space readout of which eigenmodes currently carry quanta. It is downstream of the snap, not the snap itself.

---

## 3. The two postulates

The framework's two non-classical postulates are stated and defended in [zpe_derivation.md §3–§4](zpe_derivation.md). Restated for reference:

- **Postulate 1 (de Broglie):** Each full cycle of any wave on the medium carries one quantum of action h. Equivalently, energy per cycle = ℏω.
- **Postulate 2 (spectral symmetry):** Sub-fundamental fluctuations on the compact dim have uniform spectral density across [0, ω₁].

Whether Postulate 2 extends to all sub-eigen bands or only to the sub-fundamental band [0, ω₁] is the central open question — see §5.

---

## 4. What follows from the postulates so far

Given the architecture (§2) and the two postulates (§3), the following are established (via [zpe_derivation.md](zpe_derivation.md) and basic geometry):

- The eigenmode spectrum ω_n = n·ω₁ is geometric (Layer 1)
- Eigenmode amplitudes are quantized in √N steps (Postulate 1 + classical wave energy)
- Sub-fundamental fluctuations carry energy ℏω each (Postulate 1)
- The average energy of a typical sub-fundamental fluctuation, integrated over the uniformly-sampled band [0, ω₁], is ½ℏω₁ (Postulates 1 + 2)
- The closure condition partitions eigenmodes into particle (T(1, n)) and non-particle classes (topological)

What is *not* yet established by these alone:

- The temporal lifetime and dissipation behavior of a transient sub-eigen fluctuation
- The mechanism and rate by which sub-eigen band energy reorganizes into an eigenmode quantum (the snap)
- Whether the random preload reservoir exists in all sub-eigen bands or only in [0, ω₁]
- The conservation accounting at a snap event (specifically, how charge and momentum are conserved when band energy at many frequencies collapses to one)
- The selection rule for which eigenmode receives the snap when multiple are kinematically allowed

These are the open mechanism questions of §6.

---

## 5. The central open question: where does the preload reservoir live?

The framework currently does not commit to where the random sub-eigen preload reservoir actually resides. Three candidate hypotheses:

**Hypothesis A — All sub-eigen bands.** The random background fluctuations live in every band between adjacent eigenmodes: [0, ω₁], [ω₁, ω₂], [ω₂, ω₃], and so on. Each band is independently fed by the vacuum and independently accumulates preload toward its own next-quantum threshold. Above the first quantum, additional snaps can occur at higher harmonics independently of the fundamental's state.

**Hypothesis B — Only [0, ω₁].** The random background fluctuations live only in the sub-fundamental band. Once the fundamental has a quantum, additional preload above the first quantum must come from coherent injection (not random background) and lives in [ω₁, ω₂] only when actively driven from outside. The vacuum baseline is entirely below ω₁.

**Hypothesis C — Some other structure.** For example, the random fluctuations live in a single global band [0, ∞) and the partitioning into sub-eigen segments emerges from a different mechanism. Or the bands' fluctuation intensities scale with frequency in some structured way that breaks Postulate 2's uniform-density claim for higher bands.

The maximum-entropy argument for Postulate 2 in [zpe_derivation.md §4](zpe_derivation.md) does not by itself decide between these — it argues for uniformity *within* a band whose boundaries are given, but does not say which bands carry random fluctuations at all.

**This question may not be decidable from first principles within the current framework.** It might require:
- A specific physical model of the background source (what produces the fluctuations)
- An experimental constraint (e.g., does Casimir-effect scaling match Hypothesis A's spectrum or Hypothesis B's?)
- A consistency check with conservation laws under high-energy injection

The framework can be developed in parallel under both A and B, with the hope that downstream consequences distinguish them.

---

## 6. Mechanism questions to resolve before further development
<!--EC Don't refer to previous drafts.  Just draft this version to stand on its own. -->
The previous draft of this file went into deep mechanism without these answered. Doing it again would be premature. The questions:

**6.1 Transient fluctuation lifetime.** Sub-eigen fluctuations cannot persist as eigenmodes. For how long do they exist before dissipating? The answer sets the rate at which preload accumulates and the timescale on which preload is "available" for a snap. Without a model of fluctuation lifetime, "preload reservoir" has no temporal structure.

**6.2 Band-to-eigenmode coupling mechanism.** When sub-eigen band energy snaps into an eigenmode quantum, by what physical mechanism does the reorganization occur? Candidates: nonlinear coupling (twist-induced curvature K ∝ τ·P″ from [architecture.md §3.4](architecture.md)); parametric resonance; phase-locked feedback (a lasing-style threshold transition). Each candidate predicts a different snap rate and sharpness.

**6.3 Conservation at the snap.** The sub-eigen band's energy is distributed across many frequencies. The eigenmode quantum is at one specific frequency ω_n. When the snap occurs, the frequency distribution must be reconciled — energy is conserved but what about momentum and the spectral content? Candidate answer: the snap consumes only the *integrated energy* matching ℏω_n, while the band's frequency-distributed remainder remains as preload. But this requires a precise accounting.

**6.4 Snap selection rule.** When the accumulated band energy can support a snap at multiple targets — say, the fundamental's second quantum (adding ℏω₁ at n=1) or the second harmonic's first quantum (adding ℏω₂ at n=2) — which one wins? This is the analog of a branching-ratio question and the framework needs a prediction.

**6.5 Injection mechanism for production.** §7 below sketches the production-by-injection scenario. To make it concrete, the framework needs: how does external energy couple to the sub-eigen band of a target sheet? At what rate? With what spectral structure?

**6.6 Conservation gating for production.** For a snap to produce a particle, conservation laws (charge, baryon number, etc.) must be satisfied. Random neutral background can only produce charge-balanced configurations. Charged injection sources are required for single-particle production. The framework needs to make this gating explicit and predict the cross-sections.

These six questions are the gate. Until each has a working answer (or a clearly-flagged provisional answer), expanding this file further is premature.

---

## 7. The production-by-injection scenario (the load-bearing test)

If the framework can deliver on §6, the central scenario to nail down is:

> **External energy is injected into a target sheet's sub-eigen band(s). Energy accumulates in the band. When accumulation crosses the snap threshold and conservation laws are satisfied, a particle quantum appears on the corresponding eigenmode. The detector registers a particle creation event.**

This scenario, if it works, gives:

- A **concrete physical mechanism** for particle production, not a statistical postulate
- A **deterministic prediction** for when production occurs (when injected energy + ambient preload crosses threshold, with conservation satisfied), modulo ignorance of the instantaneous preload state
- A **natural account of cross-section thresholds** (production turns on when injection rate × time crosses the snap threshold)
- A **symmetric account of decay** (particle eigenmode loses energy to its sub-eigen band; band fails to maintain threshold; particle decays)
- A **bridge to observed production cross-sections** (the framework should reproduce known threshold structure in collider data without putting it in by hand)

The scenario is the framework's load-bearing test. If §6's mechanism questions have answers and §7's scenario goes through quantitatively, threshold dynamics earns its place. If not, it doesn't.

---

## 8. The symmetric decay scenario

By the same architecture, decay is:

> **A snapped eigenmode quantum bleeds energy into its surrounding sub-eigen band(s) through nonlinear coupling. The band fails to maintain the snap threshold. The eigenmode amplitude drops from A_N to A_{N-1} in a discrete reverse-snap. The detector registers a particle decay event.**

The decay rate is set by:
- The nonlinear-coupling matrix element between the eigenmode and the sub-eigen band
- The rate at which the band dissipates the bled energy (back into the vacuum or onto coupled sheets)
- Any conservation constraints that block specific decay channels

Decay and production are then symmetric under time-reversal. The neutron lifetime, muon lifetime, etc. become predictable from the same mechanism that predicts production thresholds.

---

## 9. Conservation laws as cascade and snap constraints

Independent of the threshold mechanism, the standard conservation laws apply:

- **Energy** — exact. Total field energy is conserved across snap events.
- **Charge** — topological per [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md). A snap from neutral background preload can only produce charge-balanced configurations (particle-antiparticle pairs); single charged-particle production requires a charged injection source.
- **Baryon number** — per [baryon-number.md](baryon-number.md), the cut-space invariant of the K4 dim-graph; gates which decay channels are allowed.

The threshold mechanism adds to these — it does not override them. A snap is allowed only when both the threshold is met *and* the conservation laws are satisfied. Otherwise the band continues to accumulate until a compatible configuration is reachable.

---

## 10. Comparison with leakage-rate.md

The two frameworks compute the same observables (decay rates / lifetimes / cross-sections) but from different ontologies. They are positioned as **complementary descriptions at different abstraction levels**, not as competitors.

| | leakage-rate (resonance pole / FGR) | threshold-dynamics (band snap / unsnap) |
|---|---|---|
| Ontology | Standard QM amplitudes on multi-sheet manifold | Eigenmode-quantized amplitudes + continuous sub-eigen bands |
| What "decay" is | Exponential leakage of amplitude to a continuum | Eigenmode unloading into sub-eigen band, threshold drop |
| What "production" is | Vertex coupling in Feynman calculus | Band accumulation crossing snap threshold |
| Source of randomness | QM amplitude squared | Preload value at moment of snap (deterministic but unknown) |
| Source of h | Imported from QM | Postulate 1 |
| Status of discreteness | Imported postulate | Derived from amplitude quantization (eigenmodes carry integer N) |
| Weak-coupling agreement | Expected | Predicted, requires verification |

The frameworks should agree numerically in the regime where standard QM is well-tested. Where they could distinguish: injection-dependent production thresholds, environment-dependent decay rates from preload variation, sub-threshold field signatures (Reiter coincidences).

---

## 11. Next steps

Strictly gated on resolving the §6 mechanism questions. No file body expansion should occur until then.

Concrete preparatory work that can begin now:

- **Survey nonlinear coupling on Ma sheets** to constrain the band-to-eigenmode coupling mechanism (§6.2). The twist-induced curvature K ∝ τ·P″ from [architecture.md §3.4](architecture.md) and cross-shear σ from [STATUS.md](STATUS.md) Phase 4 are the candidate vehicles. A computation of the relevant matrix elements on a single sheet would clarify whether the snap rate is even in the right ballpark.
- **Decide between Hypothesis A and B for §5** by examining whether observed Casimir-effect scaling is consistent with multi-band preload or sub-fundamental-only preload. If the standard QFT Casimir result requires preload in all bands, Hypothesis A is forced; if [0, ω₁] is sufficient, Hypothesis B is viable.
- **Frame the production-by-injection scenario quantitatively** for at least one simple case (e.g., photon-induced pair production γ → e⁺e⁻ on an electron sheet) so that the conservation-gating and snap-threshold conditions can be written down explicitly. The scenario is currently qualitative; making it quantitative is the precondition for §7 being load-bearing.

Once these preparatory steps yield concrete numbers, the §6 mechanism questions can be revisited with empirical anchors, and the file can be developed in detail.

---

## 12. What this outline deliberately does NOT do

To prevent repeating the previous draft's overreach, this outline explicitly avoids:

- Treating any eigenmode amplitude as continuous (contradicts Postulate 1)
- Asserting the snap mechanism without naming the coupling channel
- Claiming Born-rule emergence without a derivation
- Asserting that all sub-eigen bands carry random preload (Hypothesis A) or that none do above the fundamental (Hypothesis B) — both remain open
- Folding interpretive material (hidden variables, ER=EPR analogs, vacuum-sloshing identifications) into the mechanics — those belong in a separate file when warranted
- Predicting specific lifetimes or cross-sections before the mechanism questions of §6 are resolved

The body of the file should not grow until the gating questions have answers.

---

## Cross-references

- [zpe_derivation.md](zpe_derivation.md) — the two postulates and the ½ℏω₁ derivation
- [mode-stability.md](mode-stability.md) — leakage-mechanism planning document
- [leakage-rate.md](leakage-rate.md) — the resonance-pole / FGR calculation
- [architecture.md](architecture.md) — closure condition and pair-triplet (σ, τ, P) machinery
- [baryon-number.md](baryon-number.md) — cut/cycle topological account of baryon-number conservation
- [cand-QY-ED.md](cand-QY-ED.md) — the K4 candidate the framework's worked example would run on
- [../../../primers/threshold-theory.md](../../../primers/threshold-theory.md) — the Reiter loading-theory primer
- [../../sheet-proton/work/clover-quarks.md §11](../../sheet-proton/work/clover-quarks.md) — per-arc charge structure distinguishing particle from non-particle eigenmodes
