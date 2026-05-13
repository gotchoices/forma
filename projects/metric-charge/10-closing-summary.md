# Chapter 10 — Closing summary

The project's nine prior chapters develop a single-sheet model of charge generation from compact-direction wave dynamics on a 2-torus. This final chapter consolidates what those chapters establish, names what is forwarded, and hands off to [metric-binding](../metric-binding/) for multi-knot work.

The chapter is *recap*, not new content. It cites each earlier chapter's main payload rather than re-deriving it; the consolidation below is built for navigation and reference, not pedagogy.

**Inheritance.** All nine prior chapters.

- *From [Chapter 1](01-foundation.md):* the (t, S₁, S₂, u, w) manifold, the bare metric with parameters ε and σ_uw, the wave-field axiom, the wrap-order convention (m = tube winding, n = ring winding), and the closure condition stated axiomatically (chirality criterion with operational synchronization m | n).
- *From [Chapter 2](02-modes-on-a-sheet.md):* the (m, n) mode family and the dispersion relation; single-axis modes flagged as closure-failure candidates.
- *From [Chapter 3](03-knots-on-the-torus.md):* the knot-family reframing; weak knots (T(1, n) unknots) vs genuine torus knots T(p, q) with p, q ≥ 2.
- *From [Chapter 4](04-the-closure-condition.md):* the closure condition derived from the chirality criterion; T(1, n') primitives and multi-component links k × T(1, n').
- *From [Chapter 5](05-metric-self-consistency.md):* the wrap-order-asymmetric standing-wave construction; the natural particle's surviving cross-term h_μw = B_μ; the four-property gauge-potential test at σ = 0 and σ ≠ 0.
- *From [Chapter 6](06-handedness-and-pairs.md):* three discrete reflections and three neutrality mechanisms; the charge-sign rule from p^w; σ_uw biases chirality within particles, not matter/antimatter populations.
- *From [Chapter 7](07-aspect-ratio-and-character.md):* the ε sweep; three aspect-ratio regimes; mass-tower structure across (m, n).
- *From [Chapter 8](08-shear-and-fractional-charge.md):* the σε product as structural lever; the single-Bloch-mode natural particle under shear; Configuration Y for multi-component links; the mixed-orientation compound inventory.
- *From [Chapter 9](09-ratio-and-shear.md):* the combined (σ_uw, ε) landscape; three sheet types (lepton-like, neutrino-like, hadronic-like); the σ → 1 principal-axis suppression mechanism.

**Distinctive job.** Three: (i) state the central derivation in compact form; (ii) catalog the structural inventory the framework produces; (iii) name the open questions and route each to its downstream home.

---

## Concepts in this chapter

| § | Concept |
|---|---------|
| 1 | The central derivation in compact form |
| 2 | The closure-satisfying inventory |
| 3 | Three neutrality mechanisms |
| 4 | Metric parameters and the (σ, ε) landscape |
| 5 | Structural commitments — what is derived |
| 6 | Forwarded — open questions and their downstream homes |
| 7 | Structural extensions not explored |
| 8 | Hand-off to metric-binding |

---

## 1. The central derivation in compact form

A closed wave configuration T(m, n) on a 2-torus T² carries observable EM if and only if it satisfies the **closure condition**: the gcd-reduced primitive has tube winding 1 (chirality criterion), equivalently the operational synchronization m divides n with both nonzero. Under the **wrap-order convention** of [Chapter 1 §10](01-foundation.md), the first index m is the tube winding and the second index n is the ring winding; closure-satisfying primitives take the form T(1, n') with n' a positive integer.

Given a closure-satisfying mode, the natural particle is constructed by the **wrap-order-asymmetric standing-wave** procedure of [Chapter 5 §4](05-metric-self-consistency.md): standing in the ring direction u (with R_u-symmetrization at σ = 0; single Bloch mode under shear per [Ch 8 §2.2](08-shear-and-fractional-charge.md)), traveling in the tube direction w. The linearized Einstein analysis on this configuration produces a unique surviving spacetime↔compact cross-term:

<!-- h_{μw} = B_μ — the unique surviving gauge potential -->
$$
h_{\mu w} \;=\; B_\mu
$$

This is the framework's single gauge potential, derived from the metric rather than postulated. The four-property test of [Ch 5 §4.6](05-metric-self-consistency.md) confirms it satisfies the standard requirements of an EM gauge potential at both σ = 0 and σ ≠ 0 under a single framing — wrap-order enforcement at the gauge-identification level.

Charge sign falls out of the same construction. The Lorentz-force coupling derived in [Ch 5 §4.6.4](05-metric-self-consistency.md) gives charge sign = sign of p^w = sign of the tube winding m. The four discrete reflections of the closure-satisfying primitive T(±1, ±n') tabulate cleanly per [Ch 6 §2.4](06-handedness-and-pairs.md).

Under shear, the **σε product** is the structural lever for primitive selection: n_opt = round(σε) selects the lightest closure-satisfying primitive, with mass exactly M ≡ (ℏ/c)·(2π/L_w) at integer σε ([Ch 8 §2.3](08-shear-and-fractional-charge.md)).

This is the chapter-1-through-8 thread in compact form: an axiomatic closure condition becomes the operational rule m | n, the rule's content forces a specific natural-particle construction, and that construction selects exactly one gauge potential.

---

## 2. The closure-satisfying inventory

The configurations the framework predicts as charge-carrying:

**Primitives T(1, n').** Single-component closure-satisfying modes. The mass tower scales with ring winding n' ([Ch 7 §3](07-aspect-ratio-and-character.md)), with T(1, 1) lightest at fixed ε. MaSt model-F proposes T(1, 2) as the reference target for what standard physics calls the electron — a candidate identification, not a framework commitment ([Ch 3 §3.1](03-knots-on-the-torus.md), [Ch 4 §4.2](04-the-closure-condition.md)).

**Multi-component links k × T(1, n').** k phased copies of a primitive at relative phases 2π·j/k for j = 0, ..., k−1. Under the **Configuration Y** commitment of [Ch 8 §5](08-shear-and-fractional-charge.md), each component contributes its own h_μw cross-term and carries 1/k of the link's integer total charge. Individual components are not closure-satisfying alone — only the collective k-link closes — and this structural non-isolability is the framework's confinement-like consequence per [Ch 8 §7.2](08-shear-and-fractional-charge.md).

**Mixed-orientation compounds.** The mode-language inventory also admits configurations where different components carry different orientations of the primitive (e.g., 2 × T(+1, n') + 1 × T(−1, n')), available by linear superposition without new mechanism. External integer charge follows the tube-winding-sum rule ([Ch 8 §7.4](08-shear-and-fractional-charge.md)); a 2:1 mixed compound has external integer charge ±1, a structural building block for the candidate proton-like state. Stability of mixed-orientation compounds is forwarded — the framework supplies the inventory item but does not pick out which compounds are dynamically realized.

---

## 3. Three neutrality mechanisms

The framework predicts three structurally distinct routes by which a mode-language configuration carries mass but no observable EM:

**Single-axis modes (m, 0) or (0, n).** One winding is exactly zero; the closure rule has nothing to test on the absent winding. The natural particle reduces to a metric-mass-style standing wave on the single nonzero direction, with no surviving spacetime↔compact cross-term ([Ch 5 §5.1](05-metric-self-consistency.md)).

**Genuine torus knots T(p, q), p, q ≥ 2, gcd = 1.** The closed curve is chirally distinct from its mirror in 3-space; neither R_u nor R_w is a topological symmetry. The natural particle falls back to R_J-symmetrization, which cancels both spacetime↔compact cross-terms but doubles the compact↔compact entry T_uw — mass plus a chirality-encoding field, no gauge potential ([Ch 5 §5.2](05-metric-self-consistency.md)).

**Sign-conjugate cancellation pairs.** A single field configuration containing both (m, n) and (−m, −n) at equal amplitude on a closure-satisfying mode — voluntary R_J-symmetrization instead of the natural R_u — cancels the spacetime↔compact gauge potential and produces 2× the single-mode mass plus the chirality field T_uw ([Ch 6 §4](06-handedness-and-pairs.md)). Distinct from the previous two mechanisms in being *tunable* via the relative amplitude α/β.

Each mechanism produces a massive but EM-neutral state by a different structural route. Specific MaSt-correspondence identifications — which standard-physics neutral particle (neutrinos, neutral hadrons, the Higgs, dark matter candidates) sits in which mechanism — is downstream comparison work.

---

## 4. Metric parameters and the (σ, ε) landscape

The framework operates with five structural parameters that organize the closure-eligible inventory (recap of [Ch 8 §8](08-shear-and-fractional-charge.md)'s parameter table):

| Parameter | What it controls |
|---|---|
| (m, n) integer labels | Primary mode identity |
| Closure satisfaction (m divides n) | Charge vs no-charge |
| Handedness sign | Matter/antimatter candidate axis |
| Aspect ratio ε ≡ L_u/L_w | Sheet character regime |
| Shear σ_uw, with \|σ_uw\| < 1 | Primitive selection via the σε product; chirality bias; multi-link energetics |

[Chapter 9](09-ratio-and-shear.md) brings ε and σ_uw together. The (σ, ε) plane partitions into structural regimes that map onto three qualitative sheet types — **hadronic-like** (small ε with moderate σ), **neutrino-like** (ε ≈ 1 with small σ), and **lepton-like** (large ε with substantial σ). The σ → 1 boundary mechanism of [Ch 9 §3](09-ratio-and-shear.md) is the framework's principal-axis-suppression candidate for resolving how the lepton-like regime survives single-axis competition at large ε.

The combined landscape supports a downstream inversion exercise: given a sheet's measured properties, derive the (ε, σ_uw) values for that sheet. [Chapter 9 §7](09-ratio-and-shear.md) sets up the substrate; [shear-ratio.md](shear-ratio.md) records current production-study estimates for the empirically-targeted sheets (electron, neutrino, proton). Sheet-specific quantitative inversion is downstream work.

---

## 5. Structural commitments — what is derived

The framework's derived results, with chapter pointers for the reader who wants the full argument:

- **Single gauge potential per closure-satisfying particle.** The R_u-symmetrized natural particle's surviving cross-term h_μw is identified with B_μ ([Ch 5 §4](05-metric-self-consistency.md)). The four-property gauge-potential test runs cleanly at both σ regimes under wrap-order enforcement ([Ch 5 §4.6](05-metric-self-consistency.md)).

- **Closure-rule operational form.** m divides n (m | n) with both nonzero is equivalent to the gcd-reduced primitive having tube winding 1; equivalent to the chirality criterion (achiral curve + R_u as topological symmetry); equivalent to the synchronization test on phase advances ([Ch 4](04-the-closure-condition.md), [Ch 1 §10](01-foundation.md)).

- **σε product as structural lever.** n_opt = round(σε) selects the lightest T(1, n') primitive; level crossings at half-integer σε; no simultaneous three-fold degeneracy ([Ch 8 §2.3](08-shear-and-fractional-charge.md)).

- **Charge sign rule.** Sign of p^w = sign of the tube winding m, derived from the Lorentz-force structure of [Ch 5 §4.6.4](05-metric-self-consistency.md). The four-mode reflection table in [Ch 6 §2.4](06-handedness-and-pairs.md) tabulates charge and mass for T(±1, ±n').

- **σ_uw biases chirality, not matter/antimatter.** The shear cross-term k_u·k_w is invariant under joint sign flip; the R_u-conjugate and R_w-conjugate pairs split by 4σ\|mn\|/ε in μ², while R_J-conjugates remain mass-degenerate at any σ ([Ch 6 §6](06-handedness-and-pairs.md), [Ch 8 §3](08-shear-and-fractional-charge.md)).

- **Configuration Y mode-language structure.** k × T(1, n') reads as k phased copies with k surviving h_μw cross-terms and 1/k charge per component ([Ch 8 §5](08-shear-and-fractional-charge.md)); confinement-like behavior follows from individual components failing closure ([§7.2](08-shear-and-fractional-charge.md)).

- **Mixed-orientation compound inventory.** External integer charge by tube-winding sum, available by linear superposition without new mechanism ([Ch 8 §7.4](08-shear-and-fractional-charge.md)).

- **σ → 1 principal-axis suppression.** Near the metric boundary, the (1−σ²)⁻¹ factor scales single-axis masses up faster than closure-satisfying masses, supporting closure-satisfying dominance at extreme ε ([Ch 9 §3](09-ratio-and-shear.md)).

- **Three sheet-type qualitative inventory.** The (σ, ε) landscape supports three structurally distinct sheet characters; the qualitative shape is committed, quantitative correspondence to specific empirical sheets is downstream ([Ch 9 §5](09-ratio-and-shear.md)).

The framework's negative findings are equally part of the structural commitment: linear scalar-field theory does not select a preferred k for fractional-charge multi-links ([Ch 8 §6](08-shear-and-fractional-charge.md)); σ_uw alone cannot produce a matter/antimatter bias ([Ch 6 §6.7](06-handedness-and-pairs.md)). These are honest reports of what the framework's machinery does and does not do.

---

## 6. Forwarded — open questions and their downstream homes

What the framework does *not* settle, with explicit routing:

| Question | Downstream home |
|---|---|
| k-selection for fractional-charge multi-links | [metric-binding](../metric-binding/) (φ⁴ inter-component dynamics) or [grid-duality §8](../grid-duality/08-where-alpha-appears.md) (substrate Z_k) |
| Stability of mixed-orientation compounds | [metric-binding](../metric-binding/) |
| Neutron analog (no 3-component compound has external charge 0) | [metric-binding](../metric-binding/) + downstream phenomenology |
| Integer vs fractional charge reading (±1 framework-units vs ±1/3 standard-model-units) | Downstream phenomenology |
| Reconciliation with R-track mode-by-mode quark assignments | [metric-binding](../metric-binding/) + R-track resolution of the two-shear puzzle ([R53 F16](../../studies/R53-three-generations/)) |
| Multi-sheet metric composition (TODO-Disc1, TODO-Disc2) | [metric-binding](../metric-binding/) |
| Matter/antimatter bias mechanism | Substrate level ([grid-primitive](../grid-primitive/) / [grid-duality](../grid-duality/)) or a different shear mode not currently in the metric |
| Multi-knot pass-through, annihilation, and bound states | [metric-binding](../metric-binding/) |
| Specific MaSt-correspondence identifications | Sheet-specific downstream work; treated as reference targets only in this project |
| Quantitative (σ_uw, ε) values for specific empirical sheets | Sheet-specific downstream work; [shear-ratio.md](shear-ratio.md) records current production-study estimates |
| Quantitative α derivation | [grid/](../../grid/); structural location of α settled in [grid-duality §8](../grid-duality/08-where-alpha-appears.md) |

The table above is the canonical record of what metric-charge does not settle and where each forwarded item lives.

The matter/antimatter bias question is the framework's one location where a property standard physics treats as physically meaningful has no derived mechanism in this project. σ_uw cannot produce it; whether substrate-level chirality at grid-primitive supplies the missing ingredient, or whether a different shear mode in the metric does, is the project-direction question that follows out of metric-charge.

---

## 7. Structural extensions not explored

The framework's commitments characterize a single closure-satisfying primitive on a single 2D compact sheet with **constant** (ε, σ_uw) — scalar parameters, the same numbers everywhere. Several structural extensions of this setup are mathematically available and likely relevant for downstream work; this section enumerates the most likely-relevant ones so future work knows where to look when constant (ε, σ_uw) cannot accommodate a modeling target.

### 7.1 Non-constant metric parameters

Both ε and σ_uw can be promoted from scalar constants to **functions of one or more coordinates**:

- **Functions of (S₁, S₂)** — the sheet's aspect ratio or shear varies with position in extended space. Different regions of space then host effectively different sheet characters; transitions between regions support edge-like and interface phenomena. Likely-relevant whenever multi-knot interactions, sheet defects, or position-dependent species need modeling (metric-binding territory).
- **Functions of t** — time-evolving compactification. Comparable to cosmological radion or modulus fields.
- **Functions of (u, w)** — parameters varying around the compact sheet itself ("warped" compactification). The mode spectrum is no longer clean integer pairs; modes become solutions of a Schrödinger-like equation on the varying compact metric, with potential mode localization, mode-mixing, and trapping.

Both ε and σ_uw admit this promotion. Promoting either makes the linearized Einstein equations nontrivial in the compact directions, breaks the clean integer-mode picture, and introduces mode coupling. The framework's derivations would need to be redone for any specific function form. **This is probably the first place to look when constant-(ε, σ_uw) analysis cannot describe a target phenomenon** — it preserves the general framework while admitting position- or time-dependence.

### 7.2 Additional metric components

The framework's metric uses one off-diagonal entry (σ_uw, the compact-compact shear). Other off-diagonals are mathematically available:

- **Extended-compact shears σ_Su, σ_Sw** — between an extended dimension (S₁, S₂) and a compact one. metric-mass Ch 7 uses σ_Su to derive a sign-reflection bias mechanism on a 1D-compact substrate; either σ_Su or σ_Sw is a candidate matter/antimatter bias mechanism per [Ch 6 §6.7](06-handedness-and-pairs.md).
- **Time-compact shears σ_tu, σ_tw** — between time and a compact direction. Not engaged anywhere in the framework's stack.
- **Extended-extended shear σ_S₁S₂** — observable gravitational curvature in standard GR.

Each of these is an additional free parameter that could vary independently, and (per §7.1) each could itself be a function rather than a constant.

### 7.3 Boundary conditions and field content

- **Twisted periodicities / spin structures.** The framework assumes strict periodicity: φ(u + L_u, w) = φ(u, w) and similarly in w. Anti-periodic boundary conditions (φ(u + L_u, w) = −φ(u, w)) shift the integer spectrum to half-integers; phase-twisted conditions (φ(u + L_u, w) = e^{iα} φ(u, w)) introduce a continuous twist. T² admits four distinct spin structures (PP, PA, AP, AA); in standard field theory these are how fermion fields acquire different mode families than boson fields. Engagement with spin structure is the natural place to look for fermion-like content within this framework's scope.
- **Non-scalar field content.** φ is currently a real scalar. Vector, spinor, and tensor fields on T² carry internal polarization indices and richer mode families. Polarization is explicitly forwarded to [grid/](../../grid/) per [Ch 1 §7](01-foundation.md); engagement with non-scalar field content on the sheet would lift that elision.

### 7.4 Substrate topology

- **Non-trivial T² fibration over extended space.** Currently the manifold is M = ℝ × ℝ × ℝ × T² — a trivial product. If the T² fiber were "twisted" as a function of (S₁, S₂) (Möbius-like bundle structure), compact and extended directions would couple in ways no single (ε, σ_uw) captures.
- **Higher-genus compact substrate.** Going beyond T² to genus-2 (double-torus) or higher. π₁ becomes non-abelian; knot/winding structure changes substantially. A deep structural extension, not just a parameter addition.

### 7.5 Multiple coupled fields

Two or more φ fields on the same sheet with a coupling term produce mixed modes. The φ⁴ self-interaction of [Ch 8 §6.3](08-shear-and-fractional-charge.md) — forwarded to metric-binding for k-selection — is the framework's one explicit case. Other couplings (φ₁·φ₂², φ²·ψ, gauge-couplings, etc.) are structurally available and may be relevant for inter-species interactions in metric-binding.

### Summary

| Extension | Likely-relevant question it bears on |
|---|---|
| Non-constant (ε, σ_uw) as functions of (S₁, S₂, t, u, w) | Spatial / temporal inhomogeneities; mode localization |
| σ_Su / σ_Sw (extended-compact shears) | Matter/antimatter bias |
| σ_tu / σ_tw (time-compact shears) | Untouched |
| Twisted periodicities / spin structures | Fermion-vs-boson distinction |
| Non-scalar field content | Polarization, electromagnetic vector structure (→ grid) |
| Non-trivial T² fibration | Coupling compact and extended sectors |
| Higher-genus substrate | Non-abelian topology, exotic species |
| Multiple coupled compact fields | Inter-species interactions in metric-binding |

These are *structural neighborhoods* outside the current commitment, not items the framework will eventually engage with. The non-constant parameter promotion of §7.1 is the most general and the least disruptive — it preserves the framework's structure while admitting position or time dependence. The remaining extensions add new parameters or change the manifold itself, and engaging them is a substantive structural commitment beyond the scope of this project.

---

## 8. Hand-off to metric-binding

[metric-binding](../metric-binding/) inherits the binding-mechanism work that metric-charge forwards: k-selection through the φ⁴ inter-component calculation, stability of mixed-orientation compounds as candidate baryon-like structures, multi-knot interaction (pass-through, annihilation, bound states), and the architectural commitments on multi-sheet composition flagged in [Ch 1 §11](01-foundation.md) as non-assumptions (substrate sharing, diagonal normalization for multi-species). The R-track studies — [R53](../../studies/R53-three-generations/), [R54](../../studies/R54-compound-modes/), [R63](../../studies/R63-proton-tuning/), [R64](../../studies/R64-nuclear-harmonic-stack/) — supply the empirical companion thread for that work; their unresolved two-shear puzzle (R53 F16) is a downstream binding-side concern that metric-binding's architectural framing will need to engage.

metric-charge's deliverable to that work is the structural inventory of this chapter: which configurations the framework's mode-language admits, what their per-component and external-charge structure is, and which questions belong on the binding side rather than the metric side. metric-charge's job ends with the inventory and the scope boundary; the binding-side investigation begins in metric-binding.

---

## What this chapter does **not** do

- **Does not introduce new derivations.** All structural content lives in Chapters 1–9; this chapter cites rather than re-derives.
- **Does not settle questions left open in earlier chapters.** Open questions remain open here; §6 routes them downstream without resolving them.
- **Does not commit to MaSt-correspondence identifications.** Reference targets named in earlier chapters — T(1, 2) as electron candidate, 2:1 mixed compound as proton candidate, ε ≈ 1 sheets as neutrino candidates — remain reference targets, not commitments.
- **Does not engage downstream phenomenology.** The integer-vs-fractional-charge reading, specific quark masses and mixing angles, and the empirical (ε, σ_uw) values for individual sheets are downstream work flagged at §6.
- **Does not preview metric-binding's mechanisms.** §8 names what metric-binding picks up; how metric-binding handles each item is metric-binding's chapter arc to develop.

---

## What's next

[metric-binding](../metric-binding/). End of metric-charge's single-sheet derivation arc.
