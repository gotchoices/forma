# Chapter 1 — Foundation

**Status:** Draft. Reviewed (see [01-foundation-review.md](01-foundation-review.md) for issues addressed). Iteration ongoing.

This chapter is the entry point for sheet-proton's mathematical derivation. It states the central question, declares the inputs the rest of the arc rests on, fixes coordinates and conventions, and commits to the *framing* — what kind of object a baryon is in this framework and what kind of structure a quark is — that every subsequent chapter inherits. It also draws the scope: the construction models one quark generation (u, d), and its form is generation-agnostic in a sense that hands off cleanly to [ma-domain](../ma-domain/).

**Prerequisites.**

- [metric-charge/](../metric-charge/) — the generic 2-D-sheet framework that this project specialises. In particular [Ch 1](../metric-charge/01-foundation.md) (the scalar field on T²), [Ch 4](../metric-charge/04-the-closure-condition.md) (closure), [Ch 6](../metric-charge/06-handedness-and-pairs.md) (Z₂×Z₂ structure on closure-satisfying modes), and [Ch 11](../metric-charge/11-modeling-foundation.md) (picture A and the G1 per-arc curvature bridge) are assumed as reference.
- [metric-mass/](../metric-mass/) — the single-compact-dimension precursor. Standing-wave reading of mass.
- [metric-binding/](../metric-binding/) — the generic multi-knot framework. This project is the proton-sheet specialisation.

This chapter is the *framing chapter*. It declares the equations and hypotheses the rest of the arc inherits — the per-arc charge integral, the path-length mass formula, hypothesis G1, the (1/2, 1) baryon modes — but does not derive their *consequences*. The derivations live in chapters 2–6, which take the commitments here and build the substrate, find the modes, compute the charges, and derive the masses from them.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The central question |
| 2 | Inputs from foundational projects |
| 3 | Coordinates and conventions |
| 4 | The framing — one wave-quantum, quark substructure, color |
| 5 | Scope — single generation, generation-agnostic form |
| 6 | Summary |

---

## 1. The central question

The framework's prior projects answer general questions about a 2-D compact sheet:

- *metric-mass* — how does mass emerge from a single compact dimension?
- *metric-charge* — how does electromagnetic charge emerge from the topology of a closed mode on a 2-D compact sheet, and what is "a sheet"?
- *metric-binding* — how do multiple modes interact on a generic sheet?

The proton sheet is not a generic sheet. The hadrons it hosts make specific demands on the sheet's geometry. We list the empirical reference points first, since the arc's job is to *reach* them:

| Quantity | Observed value |
|---|---|
| Proton charge | +1 (exact integer) |
| Proton mass | 938.272 MeV/c² |
| Neutron charge | 0 (exact integer) |
| Neutron mass | 939.565 MeV/c² |
| m_n / m_p | 1.001 378… |
| Number of constituent quarks per baryon | 3 (uud for proton, udd for neutron) |
| Number of color states per quark | 3 |
| Constituent quark mass (approximate) | ≈ 313 MeV |
| Standard u-quark electric charge | +2/3 (in units of |e|) |
| Standard d-quark electric charge | −1/3 |

(Particle Data Group; numerical values follow the PDG conventions and are quoted to a precision the arc actually engages with. The constituent quark mass is the standard model-dependent working value, not a directly-measured observable like m_p.)

The central question this project answers is:

> *What 2-D substrate, with what cross-section shape, mode topology, modulation, and parameter values, hosts the observed u-d hadron generation, in the sense that every quantum number the standard model assigns to a u-d hadron has a clean structural identification on this substrate?*

This is sharper than metric-charge's question (which is about charge in general, on any sheet) and sharper than metric-binding's question (which is about how knots interact, on any sheet). The proton-sheet question commits to a specific *empirical target* — the u-d hadron generation — and asks what specific structural choices the sheet must make to reach it.

What the arc commits to derive is the list above (charge values, mass ratio, three-quark substructure, three colors, and the discrete symmetries that organise them). What it does not promise — spin, magnetic moments, the absolute mass scale, the Δ baryons, light mesons, multi-sheet hadrons, and several other items — is enumerated in the [README §What we don't predict](README.md#what-we-dont-predict). The distinction between *in scope* and *out of scope* is named explicitly there and is load-bearing for honesty about the arc.

---

## 2. Inputs from foundational projects

This section recaps the results sheet-proton inherits. Nothing here is re-derived; each result is named, its load-bearing role flagged, and its source cited.

### 2.1 The scalar wave equation on T² (picture A)

The framework's fundamental object is a real scalar field φ on a 2-torus T² = S¹ × S¹, governed by the standard wave equation derived from the substrate's metric. A particle is a closure-satisfying eigenmode of the corresponding Laplace–Beltrami operator on T². From [metric-charge Ch 11 §3](../metric-charge/11-modeling-foundation.md), this framing is *picture A* — the canonical quantization of the framework's actual physics, as distinct from the harmonic-oscillator analogy (*picture B*) sometimes borrowed as a calculational tool.

Picture A is the operative framing throughout sheet-proton. When this arc says "the proton is one wave-quantum on the substrate," the wave-quantum is a picture-A object — an eigenmode of the wave equation on T².

### 2.2 The closure condition and the closure-satisfying inventory

[metric-charge Ch 4](../metric-charge/04-the-closure-condition.md) defines the closure condition that selects which (m, n) winding configurations on T² correspond to observable physical modes. The closure rule has equivalent chirality, synchronization, topological, and metric-side formulations; this project uses whichever formulation is cleanest in each chapter's context.

The closure-satisfying inventory of a generic T² is a discrete set of *integer* (m, n) pairs. This project's construction picks out the *half-integer*-m modes (1/2, 1) — modes that sit **outside** metric-charge Ch 4's standard closure derivation. The construction works around this by building a matching half-twist into the substrate so that the boundary identification

<!-- (t, θ + 2π) ~ (t + π, θ) -->
$$
(t,\, \theta + 2\pi) \;\sim\; (t + \pi,\, \theta)
$$

makes the (1/2, 1) modes close in one ring revolution. Under this substrate-extended boundary identification, the (1/2, 1) modes are closure-satisfying. But whether the half-twist substrate is the *unique* extension of the closure rule to half-integer m, and what the precise substrate-extended closure rule says about non-(1/2, 1) half-integer modes, is a real foundational gap — flagged in [work/modulated-clover.md §6](work/modulated-clover.md) as the construction's open question 1 and carried in the project's [README §Open questions](README.md#open-questions-inside-the-constructions-scope). The arc commits to this extension without deriving its uniqueness.

### 2.3 The per-arc curvature bridge — hypothesis G1

This is the *load-bearing* inherited hypothesis. The entire arc rests on it, so we name it precisely.

[metric-charge Ch 11 §6](../metric-charge/11-modeling-foundation.md) introduces:

> **Hypothesis G1.** The local geodesic curvature of a closure-satisfying mode's characteristic curve in the substrate is identified with the local electromagnetic charge density carried by that mode.

The integrated curvature along the closed curve gives the topological total charge (an integer). The integral over any sub-arc of the closed curve gives a *fractional partial* — a per-arc contribution that admits sign tracking (convex / concave) and that, in the idealised piecewise-circular setting, takes the discrete values +2/3 (for a 240° convex arc) and −1/3 (for a 120° concave arc). These fractional partials are the bridge from the sheet's geometric shape to quark substructure in this project's reading.

G1 is a hypothesis, not a theorem. metric-charge introduced it on the basis that it is the simplest local-density reading consistent with the integer-total-charge constraint. The G1 reading is what this project commits to, and "under G1" is a phrase the arc uses whenever the per-arc bridge is invoked.

### 2.4 The Z₂ × Z₂ handedness and matter–antimatter structure

From [metric-charge Ch 6](../metric-charge/06-handedness-and-pairs.md): on any closure-satisfying mode (m, n) with both windings nonzero, the four sign-combinations (±m, ±n) organise as a Z₂ × Z₂ group. The two Z₂ factors are:

- **Geometric chirality:** (m, n) ↔ (m, −n). Flipping the sign of one winding while keeping the other fixed reverses the handedness of the helical phase advance on the substrate.
- **Matter / antimatter (C-conjugation):** (m, n) ↔ (−m, −n). Flipping both signs is the substrate-level antiparticle operation.

Their product, (m, n) ↔ (−m, n), is the other Z₂.

[metric-charge Ch 6](../metric-charge/06-handedness-and-pairs.md) builds the Z₂ × Z₂ on integer (m, n). For the half-integer-m baryon modes (1/2, ±1), the same Z₂ × Z₂ action — flipping ± signs on m and n independently — lifts to the substrate-extended modes through the half-twist gluing of §2.2. The flips remain well-defined geometric operations on the modulated-clover (a sign flip of m is a t-reflection; a sign flip of n is a θ-reflection), and they commute with the half-twist identification (t, θ + 2π) ~ (t + π, θ). The chapter inherits the Z₂ × Z₂ structure on (1/2, ±1) baryon modes on this basis (use on baryon modes: Ch 6).

### 2.5 metric-binding as the home of multi-knot composition

[metric-binding](../metric-binding/) is the framework's general multi-knot project. Sheet-proton is the *single-knot* specialisation to the proton sheet — the proton and neutron are each one (1/2, 1) mode on the substrate, not a composite of three independent modes. (The three quarks introduced in §4.4 are *sub-track structure* of one mode — three pieces of the same closed curve — not three independent modes.) metric-binding's machinery becomes relevant in this arc only at the multi-sheet handoff (Ch 7) where multi-flavor hadrons like Λ, Σ would require cross-sheet composition.

---

## 3. Coordinates and conventions

A short reference section. Notation only; the rest of the arc cites back to this section.

### 3.1 Substrate coordinates

The construction uses two compact coordinates:

| Symbol | Domain | Role |
|---|---|---|
| **t** | t ∈ [0, 2π), wraps | The *tube* (cross-section) direction. At fixed θ, varying t traces the cross-section curve. |
| **θ** | θ ∈ [0, 2π), wraps | The *ring* (major-circle) direction. Sweeping the cross-section around the major ring with θ generates the embedded surface. |

The substrate also carries an extended-space embedding into (X, Y, Z) ∈ ℝ³ (construction: Ch 2). The (t, θ) coordinates are the intrinsic coordinates; (X, Y, Z) is just where the substrate sits in 3-D when rendered.

**Correspondence with metric-charge's (u, w).** metric-charge writes the generic 2-torus coordinates as (u, w). In the proton-sheet construction, t plays the role of u (it is the direction with cross-section structure) and θ plays the role of w (it is the direction with the ring topology and the half-twist). Both notations appear in this arc; whichever is clearer in context is used, and equivalence with metric-charge results is by the (u, w) ↔ (t, θ) correspondence.

### 3.2 Cross-section vs ring direction

The two directions are not symmetric in this construction. Only the ring direction carries the half-twist identification (introduced in Ch 2). The tube direction is the one whose shape — the cross-section curve — encodes the substrate's geometric content. This asymmetry is structural, not just a labelling choice.

### 3.3 Mode labels (m, n)

A closure-satisfying mode is labelled by winding numbers (m, n):

- **m** = tube winding. The number of times the mode wraps the cross-section as θ goes once around the ring.
- **n** = ring winding. The number of times the mode wraps the ring as t goes once around the cross-section.

The baryon modes of this project are (m, n) = (1/2, ±1) — half-integer tube winding, full ring winding, in either of two handedness choices. The "1/2" in m is *not* a generic non-integer rational; it is the half-twist topology's distinguishing label. The substrate's half-twist identification (t, θ + 2π) ~ (t + π, θ) makes (1/2, 1) a well-defined closed mode on the modulated-clover (Ch 2).

### 3.4 Sign conventions

- **Chirality:** (m, n) ↔ (m, −n).
- **C-conjugation:** (m, n) ↔ (−m, −n).
- Their product: (m, n) ↔ (−m, n).

The framework's chirality is *geometric* — a property of the helical phase advance on the substrate. It is *not* yet the γ⁵-chirality of Dirac spinors; identifying the two requires a spinor upgrade and is forward-looking.

### 3.5 Greek letters and modulation parameters in the construction

A small reference table the arc cites back to:

| Symbol | Role |
|---|---|
| α(θ) | Twist rate around the ring. In this construction α(θ) = θ/2 — the *half-twist*. |
| κ_g | Geodesic curvature of a closed curve on the substrate; the input to G1. |
| ρ | Overall cross-section scale; sets the tube-radius unit. |
| R_major | Major-ring radius of the embedding, *measured in units of ρ*. The dimensionless ratio R_major / ρ is what the construction works with; a physical scale is set by choosing ρ. |
| t₀ | Track label; the proton's track is at t₀ = −π/6, the neutron's at t₀ = +π/6 (convention discussed in §3.6). |
| a₁(θ), b₁(θ) | k = 1 cross-section modulation amplitudes (real and imaginary parts). Each = Ac₁ cos(3θ/2) + As₁ sin(3θ/2) in the Z₂ × Z₃-symmetric subspace; together they carry four real parameters Ac₁, As₁, Bc₁, Bs₁. |
| a₂, b₂ | k = 2 cross-section backbone amplitudes (3-fold-symmetric Z₆ dihedral). Real constants. |

The full Z₂ × Z₃-symmetric modulation thus has six real parameters: (Ac₁, As₁, Bc₁, Bs₁, a₂, b₂). Together with R_major (the seventh free parameter setting the absolute mass scale), this is the construction's full parameter space. The fit values that hit the empirical baryon doublet are reported in §4.3.

### 3.6 The t₀ convention

The two operative track labels in this arc are t₀ = ∓π/6 — chosen so that the (1/2, 1) track at that t₀ passes through exactly three full arc-pieces of the cross-section over θ ∈ [0, 2π]: lobe-saddle-lobe for the proton, saddle-lobe-saddle for the neutron. This is the convention §4.4 uses to make the three-quark substructure clean.

An equivalent labelling appears in [work/modulated-clover.md](work/modulated-clover.md), which anchors the proton track at t₀ ∈ {0, 2π/3, 4π/3} (each lobe centre) and the neutron at t₀ ∈ {π/3, π, 5π/3} (each saddle centre). These are *different starting points on the same closed track*, related by a π/6 shift in the t₀ label. Both conventions describe the same closed 3-D curve; this arc uses t₀ = ∓π/6 throughout.

---

## 4. The framing — one wave-quantum, quark substructure, color

This is the chapter's most consequential section. It declares what kind of object a baryon is and what kind of structure a quark is. Every subsequent chapter inherits this framing.

### 4.1 One wave-quantum per baryon

A baryon — proton or neutron — is one wave-quantum on the modulated-clover substrate. This is the picture-A reading: the baryon is an eigenmode of the wave equation on T², with the substrate's specific metric (Ch 2 builds it). It is *not* three independent quark-quanta combined in a Slater determinant, and it is *not* a track-localised eigenmode of the 2-D Laplace–Beltrami operator.

The second non-identification deserves a moment, because the framework once entertained it. The work file [lb-mode-localization.md](work/lb-mode-localization.md) reports a direct numerical computation of LB eigenmodes on the modulated-clover and tests whether any eigenmode — or any low-energy superposition of them — is appreciably concentrated along the proton or neutron track. The result is negative: no track localisation is observed at the proton's energy scale on this substrate. The wave-quantum's amplitude is therefore *spread* over the substrate (as a low-lying LB mode would be), not localised on a 1-D curve.

That negative result is not a problem for the construction, because the construction never required spatial track localisation. What it requires is a *charge integral along the track* — a quantity that depends on how the cross-section tangent winds along the curve, not on where the wave's amplitude sits. The next subsection makes this precise.

### 4.2 Charge as a per-arc curvature integral

Under hypothesis G1 (§2.3), the wave-quantum's charge is the integrated geodesic curvature of its characteristic curve. For a closure-satisfying mode on the modulated-clover, the characteristic curve is the closed (1/2, 1) torus knot — the curve t(θ) = t₀ + θ/2 traced once around the ring.

The total integral

<!-- Q = (1/2π) ∫_track κ_g ds -->
$$
Q \;=\; \frac{1}{2\pi}\!\int_{\text{track}}\!\kappa_g(s)\,ds
$$

gives the topological integer charge of the mode. For the proton track Q = +1; for the neutron track Q = 0 (derivation: Ch 4). The construction's *charge mechanism* is this integral; its integer total is the baryon's electric charge in units of |e|; and *fractional partials* of the integral over sub-arcs of the closed track are what the framework identifies with quark substructure (§4.4).

The integral has one further structural feature the arc relies on. Its integrand is the geodesic-curvature 1-form along the characteristic curve — a property of *how the cross-section tangent winds* along the curve, not of *where the wave's amplitude is concentrated*. In this respect the integral is **Berry-phase-like**: its value comes from the curve's geometric content, not from a probability-density weight. This is what makes the per-arc reading compatible with the global-amplitude wave-quantum of §4.1.

The Berry-phase-like reading is an **additional structural commitment on top of G1**, not a consequence of G1 alone. G1 identifies the local geodesic curvature with the local charge density; the additional claim here is that the integral over the closed characteristic curve gives the wave-quantum's electric charge *without amplitude weighting*. The framework currently asserts this; deriving it from first principles is open work, and the assertion is named as such in the project's [README §Framing](README.md#framing--one-wave-quantum-per-baryon-with-quark-substructure-along-the-track).

### 4.3 Mass from the closed-track wavelength

The wave-quantum's rest mass is set by the closed-track standing-wave wavelength. Treating the closed (1/2, 1) track as a 1-D standing wave whose wavelength equals the track's arc length L_track, the de Broglie / Compton relation E = h c / λ at the standing-wave wavelength gives the rest energy and therefore the rest mass:

<!-- m = 2π ℏ c / L_track -->
$$
m \;=\; \frac{2\pi\,\hbar c}{L_{\text{track}}}
$$

Here L_track is the arc length of the closed (1/2, 1) curve on the *embedded* substrate surface in ℝ³. It is computed by integrating the induced 1-D metric along t(θ) = t₀ + θ/2 from θ = 0 to θ = 2π; the construction's specific recipe is in [work/derived-clover.md §Per-arc charge integral](work/derived-clover.md) and [work/modulated-clover.md Step 7](work/modulated-clover.md).

The ratio m_n / m_p is therefore L_p / L_n — a purely geometric ratio that depends on the substrate's modulation and on R_major. The *sign* m_n > m_p (equivalently L_p > L_n) is forced by the construction's symmetric modulation; the *magnitude* m_n / m_p is a one-parameter fit on R_major. For orientation: in the symmetric Step-7 modulation with R_major ≈ 36.17 (in units of ρ), the construction fits the observed m_n / m_p = 1.001 378 4 at numerical precision. This is a fit, not a prediction; the *absolute* baryon mass scale m_p remains calibration (derivation and fit details: Ch 5).

R_major itself is a free parameter of the construction; the framework does not yet derive it from a deeper principle. This is named openly in the [README §Open questions](README.md#open-questions-inside-the-constructions-scope) as one of the construction's open items.

### 4.4 Quark substructure as a three-arc-piece series along the single mode

The single-wave-quantum reading of §4.1 and the three-quark substructure of this section need to be reconciled explicitly, because they sound contradictory on first reading: one knot, but three quarks? The reading is *one knot, with sub-track structure exposed by the per-arc charge integral*. The wave-quantum is one mode on the substrate; the *integral along its closed track* decomposes into three sub-integrals, one per arc-piece, that the framework identifies with three quarks. There are not three independent quark-quanta; there are three sub-track contributions to the single mode's charge content.

Concretely: the closed (1/2, 1) track on the symmetric modulated-clover passes through three arc-pieces of the cross-section in series. The cross-section has six arc-pieces total (3 convex *lobes* + 3 concave *saddles* under the Z₂ × Z₃ symmetry); the (1/2, 1) track samples three of them as θ runs from 0 to 2π:

- The *proton* track at t₀ = −π/6 passes through *lobe → saddle → lobe* — three arc-pieces in the sequence (u, d, u), i.e. uud-ordered.
- The *neutron* track at t₀ = +π/6 passes through *saddle → lobe → saddle* — sequence (d, u, d), i.e. udd-ordered.

A **quark** is identified with one arc-piece in this series. The proton's three quark-pieces are two u's (the two lobes) and one d (the saddle); the neutron's are one u and two d's. By construction, the constituent-quark mass is m_baryon / 3 — this is the framework's *definition*, not a derived result. The numerical value m_proton / 3 ≈ 312.8 MeV is in the same range as the "constituent quark mass" (~ 313 MeV) used in the constituent-quark model of QCD; the comparison is to that model-dependent working value rather than to a directly-measured observable.

The per-arc *fractional charge values* (±2/3 / ∓1/3) come out only in a specific idealised limit. On the piecewise-circular kissing-circles clover — three 240° lobe arcs of constant geodesic curvature κ = +1/r and three 120° saddle arcs of constant κ = −1/r — the per-arc integral gives exactly +2/3 (lobe, u) and −1/3 (saddle, d). On the smooth Fourier-series cross-section that the construction actually uses, the per-arc readings are *smeared* (numerically ~+0.59 per arc on the proton, ~−0.26 per arc on the neutron) because the continuous-curvature distribution does not concentrate the winding at sharp arc boundaries. The *integer* baryon charges Q_p = +1 and Q_n = 0 are preserved exactly in both representations.

The relationship between the smooth-substrate per-arc values and the standard-model ±2/3 / ∓1/3 — which are well-established empirically (DIS, R-ratio, parton distributions) — is an **open identification question**, not a derivation the construction has yet completed. The arc records the construction's smooth-substrate values; whether they are empirically tolerated depends on which observables they actually feed and on whether the smearing matches what those observables resolve. Work file: [quark-decomposition.md](work/quark-decomposition.md).

### 4.5 Color: the substrate's Z₃ as a structural analog of SU(3)

The substrate's exact Z₃ rotational symmetry around the major-ring axis produces three structurally-equivalent track families. Under the Z₃ screw, the proton's closed track maps to two other 3-fold-related closed tracks (and similarly for the neutron). The framework identifies these three families with what the standard model calls color, with one important caveat: the standard-model color group is the continuous SU(3) gauge group (8 generators); the substrate's symmetry is the discrete Z₃ (1 generator). These are different mathematical objects. The framework recovers the **structural analog of color** that survives gauge-fixing to a color singlet — the 3-fold confinement-like structure — but it does *not* construct SU(3) gauge theory.

This is the same distinction [metric-charge Ch 11 §7](../metric-charge/11-modeling-foundation.md) draws between the framework's Z₃ structural analog and the standard-model gauge SU(3); see that section for parallel language. The promotion from the Z₃ analog to full SU(3) gauge structure is a route the framework lacks a mechanism for and is deferred.

Under this reading, "color" labels which Z₃-related phase track the wave-quantum is currently observed on — a substrate-level structural feature, not an internal Hilbert-space quantum number bolted on from outside.

### 4.6 The framing this arc commits to

The framing this chapter commits to is: *single wave-quantum per baryon, with charge content organised as a 3-arc-piece series along its characteristic curve, and three Z₃-related color states by substrate symmetry*.

Three earlier framings were considered and set aside (track-localised LB eigenmode; three quark-quanta in a Slater determinant; nine wave functions in a 3 × 3 quark × color Wannier matrix); their records are in [work/lb-mode-localization.md](work/lb-mode-localization.md), [work/quark-decomposition.md](work/quark-decomposition.md), and [work/quark-wannier-decomposition.md](work/quark-wannier-decomposition.md). If downstream chapters require richer structure than the scalar-field construction supports, those work files are the entry points to revisiting the framing. See [work/STATUS.md](work/STATUS.md) for the full work-file index.

---

## 5. Scope — single generation, generation-agnostic form

A short declarative section that draws the scope.

### 5.1 In scope: the u-d hadron generation

The arc derives the proton and neutron as the two (1/2, ±1) baryon modes of one modulated-clover substrate, with one set of parameter values (R_major ≈ 36.17 and the symmetric Step-7 modulation coefficients). The Δ baryons, the light mesons, and multi-flavor hadrons are deferred — see the [README §What we don't predict](README.md#what-we-dont-predict) for the full list.

### 5.2 The construction's form is structural

The construction's form — half-twist τ = 1/2, N = 3 cross-section, Z₂ × Z₃-symmetric modulation, two (1/2, ±1) tracks at t₀ = ∓π/6, six baryon replicas in the Z₂ × Z₃ orbit — is set by the topology and the symmetry group. None of these structural features depends on the choice of quark generation. The same form would in principle host any quark-generation baryon pair, with different parameter values.

### 5.3 Generation-specific parameters

Only the *parameter values* of the modulation are generation-specific. R_major sets the absolute mass scale of the baryon doublet on this sheet; the modulation amplitudes (Ac₁, As₁, Bc₁, Bs₁, a₂, b₂) set the mass split between the proton-analog and the neutron-analog. Generation 1 (u-d) gets R_major ≈ 36.17 and the symmetric Step-7 coefficients reported in [modulated-clover.md](work/modulated-clover.md). Whether the construction's parameter range extends to the much wider mass ratios of generations 2 (c-s, with m_s/m_c ≈ 0.07) and 3 (t-b, with m_b/m_t ≈ 0.024) is an empirical open question. The form is generation-agnostic; whether it accommodates *all* three generations is for downstream work to test.

### 5.4 Handoff to ma-domain

[ma-domain](../ma-domain/) is the project that takes the single-generation result and asks whether three generations + the charged-lepton sector + the neutrino sector can be hosted in one multi-dimensional compact domain, with each sheet emerging as one cross-term in a sparse N×N metric. Sheet-proton supplies the *worked example* of one generation on one cross-term. The half-twist τ = 1/2 modulated-clover that this project settles on supersedes the older τ = 1/3 clover-quarks precedent that ma-domain's current scaffolding inherits; ma-domain may adapt its multi-generation architecture to τ = 1/2 rather than the older convention, as a coordination decision between the two projects.

---

## 6. Summary

The chapter sets up what every subsequent chapter inherits.

- The arc's *empirical target* is the u-d hadron generation, with the quantum numbers listed in §1.
- The arc's *foundational inputs* are picture A (the scalar wave equation on T²), the closure condition, the Z₂ × Z₂ handedness structure, and the load-bearing hypothesis G1 (per-arc geodesic curvature = local charge density). All inherited from metric-charge (§2).
- The arc's *coordinates* are the substrate (t, θ), the mode labels (m, n) with the (1/2, ±1) baryon modes, and the sign conventions for geometric chirality and C-conjugation (§3).
- The arc's *framing* is: each baryon is one wave-quantum on the substrate; its electric charge is a per-arc geodesic-curvature integral along its closed (1/2, 1) characteristic curve; its mass is the closed-track standing-wave wavelength; its quark substructure is the series of three arc-pieces the track passes through (lobe-saddle-lobe = uud for the proton, saddle-lobe-saddle = udd for the neutron); its three color states are the three Z₃-related phase tracks (a structural analog of standard-model color SU(3), not gauge SU(3) itself). The framing is a commitment, not a derivation — its consistency is what subsequent chapters develop (§4).
- The arc's *scope* is one generation, with a structurally generation-agnostic form whose parameter range may or may not accommodate the heavier generations — that question is left to ma-domain (§5).

The next chapter builds the substrate.
