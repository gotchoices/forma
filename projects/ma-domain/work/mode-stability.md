# mode-stability.md — the leakage mechanism and the decay-rate derivation strategy

**Status:** Solution-path document. Carries the dynamic "leakage" reading of mode stability and the phased plan for deriving decay rates from geometry. Extracted from the former sym-ladder.md §5–§8 and made candidate-agnostic.

**The goal it serves:**
- The proton (and the u, d quark modes that bind into it) and the electron are **stable** — they have no accessible lower-energy target.
- μ, τ, c, s, b, t and the neutron are valid modes but **unstable** — they decay, not because the modes are detuned (off eigenvalue) but because more favorable modes elsewhere *steal* the energy through shared-dimension channels.

This file gives the mechanism that makes that computable, and a five-phase plan to test it against observed lifetimes.

---

## 1. The leakage principle

A static reading treats each leg of a candidate as a closed cavity whose eigenmodes are stable particle states. The dynamic reading reverses this: the candidate is one connected manifold whose sheets share dims, and

> **A closure mode |ψ_A⟩ on a sheet A is dynamically stable if and only if no lower-energy mode |ψ_B⟩ exists on any sheet B such that A and B share at least one dim and the matrix element ⟨ψ_B | V | ψ_A⟩ is non-zero. Otherwise the mode decays, with rate Γ_{A→B} set by the matrix element and the density of states on B.**

The decay is not exotic — it is the standard route by which energy finds a more favorable configuration in any coupled-cavity system. "More favorable" is energetic (lower mass); "accessible" is geometric (a shared dim with non-zero overlap). The proton and electron are stable because they are the lowest modes of their conserved-quantum-number sectors and no lower target exists; every heavier mode in a sector with an accessible lighter target leaks.

This is the *expected* behavior of any geometrically-connected mode spectrum — every Standard Model particle heavier than the lightest in its sector decays, lifetimes spanning 26 orders of magnitude, the *fact* of decay robust whenever a lower-energy state with the right quantum numbers exists. The non-trivial task is not to postulate leakage but to show the **geometric leakage rates match the observed lifetimes**.

---

## 2. The resonance-pole formalism

A "particle" is a **pair-localized wavepacket** — a state concentrated mostly on one sheet, with small-amplitude tails reaching through shared dims into adjacent sheets. Such a state is generally *not* an eigenstate of the full manifold's Laplace–Beltrami operator (the true eigenstates are delocalized). Time-evolved under the full Hamiltonian, the localized wavepacket's amplitude on its source sheet decays exponentially, at a rate set by the **complex resonance pole** of the full manifold's Green's function:

<!-- Γ = -2 Im(E_resonance) / ℏ -->
$$
\Gamma \;=\; -\frac{2\,\mathrm{Im}(E_{\text{resonance}})}{\hbar}
$$

This is the Gamow / quasi-stationary-state formalism — purely geometric, derived from the wave equation on the connected manifold with no external rate axiom. Three ingredients together produce a non-zero Im(E_resonance):

1. **A shared dim m_k.** Two sheets must overlap geometrically at ≥ 1 dim; without overlap the pole stays on the real axis (no decay).
2. **Mode-overlap at the shared dim.** ψ_A and ψ_B must have non-zero overlap on m_k. For Bloch-labelled modes this means matching k_θ modulo Bloch-sector mismatch; off-diagonal σ-coupling provides the sector mixing.
3. **Lower-energy targets accessible.** E_B < E_A for some target. Energy conservation forces Im(E_resonance) = 0 if no lower continuum is available.

In the **weak-coupling limit** (small σ at junctions, narrow overlap regions) the resonance-pole rate reduces to the familiar Fermi's-golden-rule expression:

<!-- Γ_{A→B} ≈ (2π/ℏ) · |⟨ψ_B|V_k|ψ_A⟩|² · ρ_B(E_A) -->
$$
\Gamma_{A \to B} \;\approx\; \frac{2\pi}{\hbar} \,\bigl| \langle \psi_B \,|\, V_k \,|\, \psi_A \rangle \bigr|^2 \, \rho_B(E_A)
$$

FGR is a *derived consequence* of the resonance pole in the weak-coupling regime — a tool for hand calculation, not a foundation. At strong coupling, near level crossings, or where target spectra are sparse, FGR breaks down and the resonance-pole formulation is needed directly. The matrix element (the residue of the pole) depends on: L_k (shared-dim size — affects normalisation); the σ values on both sheets (off-diagonal m_t mixing); the cross-section shape on both sheets (lobe/saddle geometry at the junction); and the Bloch-sector mismatch (zero unless σ-coupling bridges source and target sectors).

---

## 3. Channel classes

When the source mode is charged and the target is uncharged, charge is carried away by a byproduct. Three byproduct classes give three channel classes, each with its own geometric prefactor:

- **Weak channels** — byproduct is leptons (electron, neutrino). The path traverses the electron and neutrino sheets; the rate factors into per-sheet overlap integrals at each shared dim — the geometric analog of the Fermi coupling G_F. Sargent's m⁵ scaling for 3-body decays emerges from the phase-space integration over the byproducts, not from G_F.
- **EM channels** — byproduct is photons. The rate carries a factor α. Under [model-F](../../../models/model-F.md), α is a *derived* geometric ratio (cross-section / ring radius on a photon sheet), not a free constant.
- **Strong channels** — internal rearrangement within a sheet's bound-state structure (hadronisation). The rate carries α_S, much larger than α.

Every decay rate factors as

<!-- Γ = (geometric coupling factor) × (phase space) × (matrix-element overlap) -->
$$
\Gamma \;=\; (\text{geometric coupling factor}) \,\times\, (\text{phase space}) \,\times\, (\text{matrix-element overlap})
$$

— the first factor distinguishing weak/EM/strong, the second purely kinematic, the third the wavefunction overlap at shared dims. Many empirical regularities (Sargent's rule, the α-suppression of radiative decays, the α_S enhancement of hadronic widths) are statements about *which factor dominates* in a channel, not separate inputs. A multi-sheet decay multiplies an overlap factor at *every* shared-dim hop — so β-decay (n → p + e + ν̄), which traverses the quark, electron, and neutrino sectors, is a *three-sheet* process whose matrix element is a product of overlaps at two hops.

---

## 4. The channel map (build per candidate)

The shared-dim topology of a candidate defines exactly which leakage transitions are geometrically allowed: **every shared dim is an allowed channel; every observed pair-to-pair leakage is one channel or a chain of them.** The first concrete task for any candidate is to build its channel map — a table of (source sheet, target sheet, shared dim, physical process) — directly from its topology graph. A mode's set of outgoing channels, together with §2's rate, determines whether it is stable (no downhill channel) or its lifetime (1/ΣΓ over channels).

---

## 5. Development strategy — five phases

Ordered to minimize new computation early (reusing already-fitted L and σ) and to maximize falsifiability.

### Phase 1 — Formalize the leakage rate from the resonance pole

The fundamental object is the resonance pole of the Green's function (§2). Two formulations:
- **A — direct resonance pole.** Construct G(E) for the full manifold's wave operator, find its complex pole nearest each pair-localized state, extract Γ = −2 Im(E_pole)/ℏ. Exact at any coupling; needs complex-scaling or numerical contour analysis.
- **B — FGR limit.** Weak coupling + dense target spectra; expand the pole's imaginary part to leading order. Analytically tractable for closed-form sheet geometries.

**Approach:** use B as the working tool, validate against A in a tractable test case (two sheets, one shared dim, one mode each). FGR is not an axiom — it is B's regime of A.

Phase 1 must produce:
- **V_k explicit** — the junction operator from the Laplacian's matching condition at the shared dim (ψ and normal derivative continuous); ⟨ψ_B|V_k|ψ_A⟩ is then an integral over m_k of ψ_A* ψ_B times a junction factor.
- **ρ_B(E_A) explicit** — density of states on B at E_A; for a 2D Helmholtz spectrum ρ_B ~ L_T·L_R/E (2D Weyl law), refined by Bloch sector and cross-section shape.
- **Small parameters** — the Bloch-sector mismatch between source and accessible target modes; zero matrix element without σ-coupling, scaling as σ^|Δm_t| with successive sector hops.
- **Channel-class factorization** (§3) — Γ as (coupling factor) × (phase space) × (overlap).
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

n → p + e⁻ + ν̄_e is the canonical multi-sheet leakage: the neutron's downward transition on the quark sheet emits an electron (path through the electron sheets) and an antineutrino (path through the neutrino sheets) — a three-sheet path, two shared-dim hops.

Tests: (1) **lifetime** — does the full three-sheet Γ give τ_n ≈ 880 s? (2) **Q-value** — 0.78 MeV n-p difference; already reproduced by the mass fit, and the leakage picture constrains only the rate. (3) **why n is so long-lived** — longest of all unstable particles by 8+ orders; in the leakage reading because n → p needs a *three-sheet* transition, each hop a small matrix-element factor. The lifetime hierarchy should track the number of sheet-hops.

### Phase 5 — Predictions

If Phases 2–4 close to measurement precision:
- **Forbidden decays as missing channels.** Any decay not in a candidate's channel map is predicted not to occur at tree level — e.g. lepton-flavor-violating μ → e + γ requires a path the topology does not provide.
- **Neutrino oscillation rates.** The same §2 formula applied within the neutrino sector predicts the PMNS angles (θ_12, θ_23, θ_13, δ_CP) from the ν-sector geometry — a 3-parameters-from-3+-observations test.
- **Decay structure.** Angular distributions, polarisations, kinematic correlations follow from the wavefunction overlap integrals, not just |⟨B|V|A⟩|² — testable against collider data.
- **The dark sector.** Anything not captured by the channel map is genuinely undecaying. Pure ring modes (m_t = 0) are non-closure — not particles in the standard sense, but may carry energy non-radiatively: candidates for the dark sector.

---

## 6. Empirical anchors

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

## 7. Open questions

1. **Bound states.** Quarks appear only in hadrons; the leakage rate is computed on free quark modes. Translating to D, B, K lifetimes needs either a bound-state correction (a hadronization-probability factor) or a derivation directly on the bound-state geometry.
2. **Decay structure beyond scalar matrix elements.** Real decays have spin structure, angular distributions, helicity dependence. Including these requires extending the mass-formula derivation to spinor fields (Dirac–Kähler-style on the sheets, per [model-F.md](../../../models/model-F.md)).
3. **Higher modes in the leakage picture.** Compound 3D modes and Relaxation-1 (m_t = 2) modes are higher-energy excitations on legs; the leakage picture expects them to decay even faster than m_t = 1 modes. Are they observed as ultra-short resonances at the right energies?
4. **The neutrino sector.** Whether one ν-sector geometry can simultaneously fit the three ν masses, the PMNS angles, and the β-decay emission rate is a tight multi-observation test.
5. **What sets the σ values.** The leakage rate depends on σ through the matrix element. Are there structural constraints (gauge-symmetry-like, or geometric like the rolled-leaf intrinsic shear) that fix σ from first principles?
6. **EM coupling α.** §3's EM channels carry α; under model-F α is a derived geometric ratio. Validating that derivation is a sub-program of the rate calculation.

---

## Cross-references

- [candidates.md](candidates.md) — the candidate topologies whose channel maps (§4) and mode spectra this analysis uses
- [cand-QD-EY.md](cand-QD-EY.md) — the QD-EY ladder, whose §2 negative result is *re-read* by §1: "no stable c/s/b/t modes" is the leakage prediction, not a fit failure
- [config-neutrino.md](config-neutrino.md) — the neutrino sector, the weak-channel carrier reservoir
- [architecture.md](architecture.md) — winding / closure conventions
- [scripts/cand_solver.py](../scripts/cand_solver.py) — supplies the fitted (L, σ) and mode wavefunctions the Phase 1–2 calculator consumes
- [models/model-F.md](../../../models/model-F.md) — the photon-sheet derivation of α (§3 EM channels)
