# mode-stability.md — why modes decay: conservation, leakage, and the decay-rate strategy

**Status:** Solution-path document. Carries the dynamic reading of mode stability — a mode decays by leaking its energy through shared dims to a lower configuration — grounds that picture in conservation laws, and lays out the phased plan for deriving decay rates from geometry. Originally extracted from the deprecated sym-ladder.md §5–§8; this revision adds the governing-law framing (§1, §3) and the continuum-reservoir / neutrino-sink mechanism (§5).

**The goal it serves:**
- The electron, and the u, d quark modes that bind into the proton, are **stable** — no decay configuration is accessible to them.
- μ, τ, c, s, b, t and the neutron are valid modes but **unstable** — they decay, not because the modes are detuned (off eigenvalue) but because their energy can disperse, through shared-dimension channels, into a lower configuration.

This file gives the mechanism that makes that computable and a five-phase plan to test it against observed lifetimes.

---

## 1. The governing law: conservation of energy

The substrate is a wave medium ([grid-primitive](../../grid-primitive/)): its dynamics follow a wave equation derived from a Lagrangian, and that equation is invariant under translation in time. By Noether's theorem, **total energy is exactly conserved** — every process the framework admits, decay included, holds the total energy fixed. This is the one law this document leans on as a first principle; §3 returns to which *other* conservations are equally fundamental and which are not.

Two consequences shape the whole decay picture.

**A decay does not lower energy — it disperses it.** A heavy mode and the set of light modes it decays into carry the *same* total energy. What changes is how that energy is distributed: one concentrated mode (the muon, 105.7 MeV on a single sheet) becomes several modes sharing that same 105.7 MeV. "Decay" is energy moving from a concentrated configuration to a dispersed one, at fixed total.

**The direction is set by phase space, not by energy.** Conservation of energy is time-symmetric; on its own it does not say which way a process runs. But a heavy mode is a *single* state, while the dispersed final configurations at the same energy are vastly more numerous. A transition therefore runs overwhelmingly toward the dispersed side — the rate into it is large, the rate back negligible — for the same statistical reason heat flows from hot to cold. Decay is conservation of energy *plus* the second law: the energy is conserved, and it spreads.

**Stability, precisely.** A mode is stable when the set of configurations its energy could disperse into — same total energy, same conserved charges (§3), reachable through the geometry (§2) — is *empty*. It is unstable when that set is non-empty; its lifetime is then set by the rate (§4). "Least-energy modes are stable" is the corollary: a mode that is the lightest carrier of its conserved charges has nothing lighter to disperse into, so its set is empty by construction.

---

## 2. The leakage principle

Section 1 is substrate-level. Its geometric realization in a candidate topology is **leakage through shared dims**.

A static reading treats each sheet of a candidate as a closed cavity whose eigenmodes are stable particle states. The dynamic reading reverses this: a candidate is one connected manifold whose sheets share dims, and energy concentrated on one sheet leaks through any shared dim toward a lower configuration elsewhere.

> **A closure mode |ψ_A⟩ on a sheet A is dynamically stable if and only if there is no configuration of lower modes — reachable from A through shared dims with non-zero mode overlap, at the same total energy and the same conserved charges — for its energy to disperse into. Otherwise the mode decays, at a rate Γ set by the overlap matrix elements and the density of available final states.**

"Accessible" is geometric (a shared dim with non-zero overlap); "favorable" is the §1 statement (a dispersed configuration at the same energy and charge exists). The electron and the proton's u/d modes are stable because their configuration set is empty; every heavier mode whose set is non-empty leaks.

This is the *expected* behavior of any geometrically-connected mode spectrum — every Standard Model particle heavier than the lightest in its sector decays, lifetimes spanning 26 orders of magnitude, the *fact* of decay robust whenever a lower configuration with the right conserved quantities exists. The non-trivial task is not to postulate leakage but to show the **geometric leakage rates match the observed lifetimes**.

---

## 3. What is conserved — and how fundamentally

A decay is gated by conservation laws: a final configuration must match the initial one in every conserved quantity, not energy alone. It matters whether each such law is a first principle or an assumption — a law derived from fundamentals constrains the framework, a label preserved by fiat is a plug. This document keeps the four relevant conservations stratified.

**Energy — fundamental.** Noether's theorem applied to the substrate's time-translation invariance (§1). Exact; not negotiable, not plugged.

**Electric charge — fundamental.** In the metric-charge framework, charge is a *topological winding number* of a Bloch state (k_θ = m_r − τ·m_t — see [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md)). A winding number cannot change under continuous evolution of a smooth field; it can change only where the field amplitude passes through zero, unwinding the phase. The substrate evolves the field continuously, so the *total* winding over the whole connected manifold is conserved. Charge conservation is therefore not a selection rule imposed by hand — it is topology. A decay redistributes winding among sheets (the source sheet's winding flows through a shared dim onto the products), but the total is locked.

So the two laws this document treats as hard constraints — energy and charge — are both genuine: one from symmetry, one from topology. Neither is a plug.

**Baryon-number-like conservation — assumed, not derived.** Proton stability needs more than energy and charge. Energy and charge alone would *allow* p → e⁺ + (neutral products): the positron is far lighter than the proton and carries the proton's +1 charge. That decay is not observed. Forbidding it requires a further conserved quantity — a baryon-number analog. The framework does not currently derive such a quantity from fundamentals. **This document flags it as an open assumption, not a law** (§10), and notes the asymmetry it creates: the electron's stability rests entirely on fundamentals (energy + topological charge), whereas the proton's rests partly on a conservation law the framework has not yet delivered. A candidate topological account — baryon number as a cut-space invariant of the K4 dim-graph — is developed in [baryon-number.md](baryon-number.md).

**Generation / lepton-flavor labels — not conserved here.** There is no "muon number." μ → e is simply leakage from one electron-delta sheet to a lower one (§2). The Standard Model's approximate lepton-flavor conservation is, in this picture, not a law at all but the smallness of certain overlap matrix elements and the absence of certain shared-dim paths (this is why μ → e + γ is suppressed — see §8 Phase 5). Nothing is plugged in; the apparent conservation is an *output* of the topology.

In short: **energy and charge are natural laws here — one Noether, one topological; everything else is either an honest open question (baryon number) or an emergent consequence of geometry (flavor).** The rate machinery of §4 onward uses only energy and charge as hard gates.

---

## 4. The resonance-pole formalism

A "particle" is a **pair-localized wavepacket** — a state concentrated mostly on one sheet, with small-amplitude tails reaching through shared dims into adjacent sheets. Such a state is generally *not* an eigenstate of the full manifold's Laplace–Beltrami operator (the true eigenstates are delocalized). Time-evolved under the full Hamiltonian, the localized wavepacket's amplitude on its source sheet decays exponentially, at a rate set by the **complex resonance pole** of the full manifold's Green's function:

<!-- Γ = -2 Im(E_resonance) / ℏ -->
$$
\Gamma \;=\; -\frac{2\,\mathrm{Im}(E_{\text{resonance}})}{\hbar}
$$

This is the Gamow / quasi-stationary-state formalism — purely geometric, derived from the wave equation on the connected manifold with no external rate axiom. Three ingredients together produce a non-zero Im(E_resonance):

1. **A shared dim m_k.** Two sheets must overlap geometrically at ≥ 1 dim; without overlap the pole stays on the real axis (no decay).
2. **Mode-overlap at the shared dim.** ψ_A and ψ_B must have non-zero overlap on m_k. For Bloch-labelled modes this means matching k_θ modulo Bloch-sector mismatch; off-diagonal σ-coupling provides the sector mixing.
3. **Lower-energy targets accessible.** E_B < E_A for some target. Energy conservation forces Im(E_resonance) = 0 if no lower *continuum* is available to receive the energy — the structural requirement §5 develops.

In the **weak-coupling limit** (small σ at junctions, narrow overlap regions) the resonance-pole rate reduces to the familiar Fermi's-golden-rule expression:

<!-- Γ_{A→B} ≈ (2π/ℏ) · |⟨ψ_B|V_k|ψ_A⟩|² · ρ_B(E_A) -->
$$
\Gamma_{A \to B} \;\approx\; \frac{2\pi}{\hbar} \,\bigl| \langle \psi_B \,|\, V_k \,|\, \psi_A \rangle \bigr|^2 \, \rho_B(E_A)
$$

FGR is a *derived consequence* of the resonance pole in the weak-coupling regime — a tool for hand calculation, not a foundation. At strong coupling, near level crossings, or where target spectra are sparse, FGR breaks down and the resonance-pole formulation is needed directly. The matrix element (the residue of the pole) depends on: L_k (shared-dim size — affects normalisation); the σ values on both sheets (off-diagonal m_t mixing); the cross-section shape on both sheets (lobe/saddle geometry at the junction); and the Bloch-sector mismatch (zero unless σ-coupling bridges source and target sectors).

---

## 5. The continuum reservoir: the neutrino sink

Section 4's rate carries a density of final states ρ_B(E_A). This section is about where a non-zero ρ_B comes from — and it turns out to be a structural requirement, not a detail.

**A decay between compact sheets generically cannot conserve energy.** Each sheet's mode spectrum is discrete — that is what compact dims buy, discrete masses. Leakage from sheet A to a sheet B alone, both compact, needs a B-mode at *exactly* E_A. Discrete levels generically do not line up; ρ_B(E_A) is then zero and Γ is zero — the mode is exactly stable. A framework of compact sheets and nothing else would predict *everything* stable.

**Decay needs a continuum to receive the mismatch.** Conservation of energy (§1) demands the final configuration sit at exactly E_A. For that to be possible for an arbitrary E_A, some component of the final state must offer a continuum — or a quasi-continuum — of available states, so that whatever energy the discrete light products cannot exactly absorb is taken up by that component. Without such a reservoir there is no decay.

**The reservoir must be charge-neutral.** A charged heavy mode decays to a lighter charged mode — which balances the charge ledger (§3) — plus the energy remainder. The remainder-carrier must itself carry Q = 0; otherwise it would unbalance the charge the light product already accounts for. So the reservoir is specifically a **Q = 0 continuum**.

**The neutrino line is exactly such a reservoir.** Per [config-neutrino.md §NC](config-neutrino.md), the neutrino substrate is a macroscopic 1D line, L ≳ cm. Its mode spacing ~ ℏc/L is of order µeV — against MeV-scale decays, a continuum for every practical purpose. And it is Q = 0 *structurally* (config-neutrino §NC.3 — a 1D dim count leaves no slot for a charge label). A macroscopic, charge-neutral quasi-continuum is precisely the sink a decay needs.

**This reframes a Standard-Model fact.** Weak decays emit neutrinos — in the Standard Model, because "the weak interaction couples to them." Here: a decay *must* shed its energy-conservation remainder into a Q = 0 continuum, and the neutrino line is the framework's Q = 0 quasi-continuum. Neutrino emission is not a choice the interaction makes; it is the only way a discrete heavy mode can satisfy conservation of energy while handing its charge cleanly to a discrete light product.

**One object, two roles.** The same macroscopic L that places the three neutrino mass eigenstates at the meV scale (config-neutrino §NC.5) also makes the line's higher modes a quasi-continuum: the three discrete low modes *are* the neutrino particles; the dense high modes *are* the sink.

**The neutrino line is not the only reservoir.** The photon field is also a Q = 0 continuum, and it is the reservoir for the EM channel class (§6); strong-channel decays disperse energy among a sheet's own dense internal modes. The neutrino line is specifically the **weak-channel** reservoir — the one internal to the ma-domain dim structure. Which reservoir a given decay draws on is the channel-class question of §6.

**Placement on a candidate.** On a maximally-connected candidate — QY-ED-share3, the K4 topology of [cand-QY-ED.md §4](cand-QY-ED.md) — attaching the neutrino line to the corners of the electron delta puts the sink one shared dim from every sheet, lepton and quark alike, since the delta corners are also the quark spokes. One reservoir then serves every decay channel in the candidate. How the 1D line attaches (its own topology, and the cross-sector coupling left open in config-neutrino §NC) is a development question — see §10.

---

## 6. Channel classes

A decay's byproducts fall into three classes, each drawing on its own Q = 0 reservoir (§5) and each carrying its own geometric prefactor:

- **Weak channels** — byproduct is leptons (electron, neutrino); the reservoir is the neutrino line. The path traverses the electron and neutrino sheets; the rate factors into per-sheet overlap integrals at each shared dim — the geometric analog of the Fermi coupling G_F. Sargent's m⁵ scaling for 3-body decays emerges from the phase-space integration over the byproducts, not from G_F.
- **EM channels** — byproduct is photons; the reservoir is the photon field. The rate carries a factor α. Under [model-F](../../../models/model-F.md), α is a *derived* geometric ratio (cross-section / ring radius on a photon sheet), not a free constant.
- **Strong channels** — internal rearrangement within a sheet's bound-state structure (hadronisation). The rate carries α_S, much larger than α.

Every decay rate factors as

<!-- Γ = (geometric coupling factor) × (phase space) × (matrix-element overlap) -->
$$
\Gamma \;=\; (\text{geometric coupling factor}) \,\times\, (\text{phase space}) \,\times\, (\text{matrix-element overlap})
$$

— the first factor distinguishing weak/EM/strong, the second purely kinematic, the third the wavefunction overlap at shared dims. Many empirical regularities (Sargent's rule, the α-suppression of radiative decays, the α_S enhancement of hadronic widths) are statements about *which factor dominates* in a channel, not separate inputs. A multi-sheet decay multiplies an overlap factor at *every* shared-dim hop — so β-decay (n → p + e + ν̄), which traverses the quark, electron, and neutrino sectors, is a *three-sheet* process whose matrix element is a product of overlaps at two hops.

---

## 7. The channel map (build per candidate)

The shared-dim topology of a candidate defines exactly which leakage transitions are geometrically allowed: **every shared dim is an allowed channel; every observed pair-to-pair leakage is one channel or a chain of them.** The first concrete task for any candidate is to build its channel map — a table of (source sheet, target sheet, shared dim, physical process) — directly from its topology graph. A mode's set of outgoing channels, together with §4's rate, determines whether it is stable (no downhill channel) or its lifetime (1/ΣΓ over channels).

---

## 8. Development strategy — five phases

Ordered to minimize new computation early (reusing already-fitted L and σ) and to maximize falsifiability.

### Phase 1 — Formalize the leakage rate from the resonance pole

The fundamental object is the resonance pole of the Green's function (§4). Two formulations:
- **A — direct resonance pole.** Construct G(E) for the full manifold's wave operator, find its complex pole nearest each pair-localized state, extract Γ = −2 Im(E_pole)/ℏ. Exact at any coupling; needs complex-scaling or numerical contour analysis.
- **B — FGR limit.** Weak coupling + dense target spectra; expand the pole's imaginary part to leading order. Analytically tractable for closed-form sheet geometries.

**Approach:** use B as the working tool, validate against A in a tractable test case (two sheets, one shared dim, one mode each). FGR is not an axiom — it is B's regime of A.

Phase 1 must produce:
- **V_k explicit** — the junction operator from the Laplacian's matching condition at the shared dim (ψ and normal derivative continuous); ⟨ψ_B|V_k|ψ_A⟩ is then an integral over m_k of ψ_A* ψ_B times a junction factor.
- **ρ_B(E_A) explicit** — density of states on B at E_A. Per §5 this must include a continuum component; for a 2D Helmholtz spectrum ρ_B ~ L_T·L_R/E (2D Weyl law), refined by Bloch sector and cross-section shape, and for the weak channel the neutrino-line quasi-continuum.
- **Small parameters** — the Bloch-sector mismatch between source and accessible target modes; zero matrix element without σ-coupling, scaling as σ^|Δm_t| with successive sector hops.
- **Channel-class factorization** (§6) — Γ as (coupling factor) × (phase space) × (overlap).
- **Sargent emergence** — for 3-body lepton decays, check the phase-space integral reproduces the m⁵/192π³ scaling *without it being put in by hand*. If m⁵ does not fall out, the formulation is wrong.

**Deliverable:** a closed-form Γ that factors transparently, each factor traceable to a geometric ingredient.

### Phase 2 — Test on the electron sector (lepton lifetimes)

The charged-lepton sheets are the cleanest test bed: geometry already fitted (machine-precision (e, μ, τ) fit), decay rates precisely measured (τ_τ = 2.903×10⁻¹³ s, τ_μ = 2.197×10⁻⁶ s), no QCD complications.

Tests: (1) **magnitude** — does the Phase 1 Γ give τ_τ ≈ 0.3 ps, τ_μ ≈ 2 μs? (2) **ratio** — Γ_τ/Γ_μ ≈ 1.7×10⁷; phase space (m⁵) gives ≈ 4.5×10⁵, the rest from couplings — does the formula reproduce both? (3) **branching** — μ has one channel (~100%); τ has e (~17%), μ (~17%), hadronic (~64%) — does the leakage map predict these?

**Deliverable:** a script that takes the fitted (L, σ) and outputs Γ_τ, Γ_μ and τ branching ratios, compared to PDG.

### Phase 3 — The quark sector (heavy-quark lifetimes)

If Phase 2 succeeds, the same machinery applies to the quark sheets. Even where a quark-sector geometry is not statically fitted, the rate formula can be *inverted* from observed lifetimes to infer (L, σ).

Tests: (1) the **s/c/b/t lifetime hierarchy** — Γ scales steeply with mode energy; reproduce the ~12-order spread from K (~10⁻⁸ s) to t (~10⁻²⁵ s). (2) **why t doesn't bind** — τ_t ≈ 10⁻²⁵ s is below the QCD hadronization time (~10⁻²³ s); predict the energy above which leakage outpaces localisation, and check it falls between b and t. (3) **no stable heavy baryon** — a "uudt"-type baryon has predicted lifetime ≈ Γ_t⁻¹, far below any bound-state formation time, so heavy baryons are predicted not to exist as stable particles — as observed.

### Phase 4 — Cross-sector decays (β-decay)

n → p + e⁻ + ν̄_e is the canonical multi-sheet leakage: the neutron's downward transition on the quark sheet emits an electron (path through the electron sheets) and an antineutrino (into the neutrino-line reservoir, §5) — a three-sheet path, two shared-dim hops.

Tests: (1) **lifetime** — does the full three-sheet Γ give τ_n ≈ 880 s? (2) **Q-value** — 0.78 MeV n-p difference; already reproduced by the mass fit, and the leakage picture constrains only the rate. (3) **why n is so long-lived** — longest of all unstable particles by 8+ orders; in the leakage reading because n → p needs a *three-sheet* transition, each hop a small matrix-element factor. The lifetime hierarchy should track the number of sheet-hops.

### Phase 5 — Predictions

If Phases 2–4 close to measurement precision:
- **Forbidden decays as missing channels.** Any decay not in a candidate's channel map is predicted not to occur at tree level — e.g. lepton-flavor-violating μ → e + γ requires a path the topology does not provide.
- **Neutrino oscillation rates.** The same §4 formula applied within the neutrino sector predicts the PMNS angles (θ_12, θ_23, θ_13, δ_CP) from the ν-sector geometry — a 3-parameters-from-3+-observations test.
- **Decay structure.** Angular distributions, polarisations, kinematic correlations follow from the wavefunction overlap integrals, not just |⟨B|V|A⟩|² — testable against collider data.
- **The dark sector.** Anything not captured by the channel map is genuinely undecaying. Pure ring modes (m_t = 0) are non-closure — not particles in the standard sense, but may carry energy non-radiatively: candidates for the dark sector.

---

## 9. Empirical anchors

Reference values for testing during development (PDG conventions; rest-frame lifetimes).

| Particle | Mass (MeV) | Lifetime (s) | Note |
|---|---:|---:|---|
| u | 2.16 | stable | quark-sector ground (T(1, 2)) |
| d | 4.67 | stable | quark-sector excited (T(1, 1)) |
| s (in K) | 93 | ~10⁻⁸ | heavy-quark leg → light leg |
| c (in D) | 1270 | ~4×10⁻¹³ | heavy-quark leg → light leg |
| b (in B) | 4180 | ~1.5×10⁻¹² | heavy-quark leg → light leg |
| t (free) | 173000 | ~5×10⁻²⁵ | heavy-quark leg → light leg |
| e | 0.511 | stable | electron-sector ground (T(1, 2)) |
| μ | 105.7 | 2.20×10⁻⁶ | electron-leg → e via shared dim |
| τ | 1776.9 | 2.90×10⁻¹³ | electron-leg → e via shared dim |
| ν₁, ν₂, ν₃ | < 1 eV | stable (mass eigenstates) | neutrino sector |
| n | 939.6 | 880 | quark T(1,1) → T(1,2) + three-sheet path |

The lifetime span is 26 orders of magnitude — the framework must reproduce that dynamic range from one formula evaluated on different geometries.

---

## 10. Open questions

1. **The origin of baryon-number conservation.** §3 flags that proton stability needs a conserved quantity beyond energy and charge that the framework does not derive. [baryon-number.md](baryon-number.md) develops a candidate answer — baryon number as the cut-space invariant of the K4 dim-graph of QY-ED-share3, with lepton number as the orthogonal cycle-space invariant. Open within that account: a precise integer-valued definition, the clover normalization, and the B − L / anomaly question. Until those close, electron stability rests on firmer ground (energy + topological charge, both fundamental) than proton stability.
2. **The neutrino line's topology and attachment.** §5 uses the macroscopic neutrino line as the weak-channel reservoir. Its 1D topology (closed loop vs. theta/Y-graph) and how it attaches to the electron-delta corners — the cross-sector coupling left open in config-neutrino §NC — set the density of states ρ and therefore enter every weak rate.
3. **Bound states.** Quarks appear only in hadrons; the leakage rate is computed on free quark modes. Translating to D, B, K lifetimes needs either a bound-state correction (a hadronization-probability factor) or a derivation directly on the bound-state geometry.
4. **Decay structure beyond scalar matrix elements.** Real decays have spin structure, angular distributions, helicity dependence. Including these requires extending the mass-formula derivation to spinor fields (Dirac–Kähler-style on the sheets, per [model-F.md](../../../models/model-F.md)).
5. **Higher modes in the leakage picture.** Compound 3D modes and Relaxation-1 (m_t = 2) modes are higher-energy excitations on legs; the leakage picture expects them to decay even faster than m_t = 1 modes. Are they observed as ultra-short resonances at the right energies?
6. **What sets the σ values.** The leakage rate depends on σ through the matrix element. Are there structural constraints (gauge-symmetry-like, or geometric like the rolled-leaf intrinsic shear) that fix σ from first principles?
7. **EM coupling α.** §6's EM channels carry α; under model-F α is a derived geometric ratio. Validating that derivation is a sub-program of the rate calculation.

---

## Cross-references

- [grid-primitive](../../grid-primitive/) — the wave substrate; the time-translation invariance behind §1's conservation of energy
- [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md) — charge as a topological winding number (§3)
- [candidates.md](candidates.md) — the candidate topologies whose channel maps (§7) and mode spectra this analysis uses
- [cand-QY-ED.md](cand-QY-ED.md) — the QY-ED family; share-3 (K4) is the maximally-connected testbed of §5
- [baryon-number.md](baryon-number.md) — the topological account of baryon-number conservation, the candidate answer to §10 open question 1
- [cand-QD-EY.md](cand-QD-EY.md) — the QD-EY ladder, whose §2 negative result is *re-read* by §2: "no stable c/s/b/t modes" is the leakage prediction, not a fit failure
- [config-neutrino.md](config-neutrino.md) — the neutrino sector; §NC is the macroscopic 1D line used as the weak-channel reservoir (§5)
- [neutrino-1D.md](neutrino-1D.md) — development of the neutrino curve, including its topology and cross-sector coupling
- [architecture.md](architecture.md) — winding / closure conventions
- [scripts/cand_solver.py](../scripts/cand_solver.py) — supplies the fitted (L, σ) and mode wavefunctions the Phase 1–2 calculator consumes
- [models/model-F.md](../../../models/model-F.md) — the photon-sheet derivation of α (§6 EM channels)
