# Chapter 1 — Foundation

This chapter is the entry point for sheet-proton's mathematical derivation. It states the central question, declares the inputs the rest of the arc rests on, fixes coordinates and conventions, and commits to the *framing* — what kind of object a baryon is in this framework and what kind of structure a quark is — that every subsequent chapter inherits. It also draws the scope: the construction models one quark generation (u, d), and its form is generation-agnostic in a sense that hands off cleanly to [ma-domain](../ma-domain/).

**Prerequisites.**

- [metric-charge/](../metric-charge/) — the generic 2-D-sheet framework that this project specialises. In particular [Ch 1](../metric-charge/01-foundation.md) (the scalar field on T²), [Ch 4](../metric-charge/04-the-closure-condition.md) (closure), [Ch 6](../metric-charge/06-handedness-and-pairs.md) (Z₂×Z₂ structure on closure-satisfying modes), and [Ch 11](../metric-charge/11-modeling-foundation.md) (picture A and the G1 per-arc curvature bridge) are assumed as reference.
- [metric-mass/](../metric-mass/) — the single-compact-dimension precursor. Standing-wave reading of mass.
- [metric-binding/](../metric-binding/) — the generic multi-knot framework. This project is the proton-sheet specialisation.

The chapter is **structural and declarative**. The math lives in chapters 2–6. Chapter 1 says what we are about to do and why; it does not yet build the substrate (Ch 2), find the modes (Ch 3), compute charges (Ch 4), or derive masses (Ch 5).

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

The closure-satisfying inventory of a generic T² is a discrete set of (m, n) pairs. This project's construction picks out a specific subset of those — the (1/2, 1) modes — and inherits closure as the rule that justifies the choice. Half-integer m is unusual; it requires the substrate to carry a matching half-twist that makes the boundary identification well-defined. Chapter 2 builds that half-twist into the substrate; Chapter 3 confirms the (1/2, 1) modes are closure-satisfying on it.

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

Their product, (m, n) ↔ (−m, n), is the other Z₂. This Z₂ × Z₂ structure is inherited without modification. Chapter 6 of sheet-proton picks it up on the specific baryon modes (1/2, ±1) and discusses how it organises proton vs neutron and matter vs antimatter on this substrate.

### 2.5 metric-binding as the home of multi-knot composition

[metric-binding](../metric-binding/) is the framework's general multi-knot project. Sheet-proton is the *single-knot* specialisation to the proton sheet — the proton and neutron are each one (1/2, 1) mode on the substrate, not a composite of three independent modes. metric-binding's machinery becomes relevant in this arc only at the multi-sheet handoff (mentioned in Chapter 7) where multi-flavor hadrons like Λ, Σ would require cross-sheet composition.

---

## 3. Coordinates and conventions

A short reference section. Notation only; the rest of the arc cites back to this section.

### 3.1 Substrate coordinates

The construction uses two compact coordinates:

| Symbol | Domain | Role |
|---|---|---|
| **t** | t ∈ [0, 2π), wraps | The *tube* (cross-section) direction. At fixed θ, varying t traces the cross-section curve. |
| **θ** | θ ∈ [0, 2π), wraps | The *ring* (major-circle) direction. Sweeping the cross-section around the major ring with θ generates the embedded surface. |

The substrate also carries an extended-space embedding into (X, Y, Z) ∈ ℝ³, which Chapter 2 builds explicitly. The (t, θ) coordinates are the intrinsic coordinates; (X, Y, Z) is just where the substrate sits in 3-D when rendered.

**Correspondence with metric-charge's (u, w).** metric-charge writes the generic 2-torus coordinates as (u, w). In the proton-sheet construction, t plays the role of u (it is the direction with cross-section structure) and θ plays the role of w (it is the direction with the ring topology and the half-twist). Both notations appear in this arc; whichever is clearer in context is used, and equivalence with metric-charge results is by the (u, w) ↔ (t, θ) correspondence.

### 3.2 Cross-section vs ring direction

The two directions are not symmetric in this construction. Only the ring direction carries the half-twist identification (introduced in Ch 2). The tube direction is the one whose shape — the cross-section curve — encodes the substrate's geometric content. This asymmetry is structural, not just a labelling choice.

### 3.3 Mode labels (m, n)

A closure-satisfying mode is labelled by winding numbers (m, n):

- **m** = tube winding. The number of times the mode wraps the cross-section as θ goes once around the ring.
- **n** = ring winding. The number of times the mode wraps the ring as t goes once around the cross-section.

The baryon modes of this project are (m, n) = (1/2, ±1) — half-integer tube winding, full ring winding, in either of two handedness choices. The 1/2 in m is *not* a fractional integer of the type m mod 1; it is the half-twist topology's distinguishing label. The half-twist makes (1/2, 1) a well-defined closed mode by identifying (t, θ + 2π) ~ (t + π, θ) — derived in Ch 2.

### 3.4 Sign conventions

- **Chirality:** (m, n) ↔ (m, −n).
- **C-conjugation:** (m, n) ↔ (−m, −n).
- Their product: (m, n) ↔ (−m, n).

The framework's chirality is *geometric* — a property of the helical phase advance on the substrate. It is *not* yet the γ⁵-chirality of Dirac spinors; identifying the two requires a spinor upgrade and is forward-looking.

### 3.5 Greek letters in the construction

A small reference table the arc cites back to:

| Symbol | Role |
|---|---|
| α(θ) | Twist rate around the ring. In this construction α(θ) = θ/2 — the *half-twist*. |
| κ_g | Geodesic curvature of a closed curve on the substrate; the input to G1. |
| ρ | Overall cross-section scale. |
| R_major | Major-ring radius of the embedding. |
| t₀ | Track label; the proton's track is at t₀ = −π/6, the neutron's at t₀ = +π/6. |
| (a₁, b₁, a₂, b₂) | Modulation coefficients of the cross-section harmonic content. |

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

gives the topological integer charge of the mode. For the proton track Q = +1; for the neutron track Q = 0. Chapter 4 derives this from the modulated-clover's specific modulation; here we just record that the construction's *charge mechanism* is this integral, that its integer total is the baryon's electric charge in units of |e|, and that *fractional partials* of the integral over sub-arcs of the closed track are what we identify with quark substructure (§4.4).

The integral is *Berry-phase-like*: it depends on how the cross-section tangent winds along the curve, not on where the wave's amplitude is concentrated. This is the structural compatibility between (i) the spread-amplitude wave-quantum of §4.1 and (ii) the per-arc charge content that distinguishes proton from neutron. The amplitude can be global while the charge content is along-the-track.

### 4.3 Mass from the closed-track wavelength

The wave-quantum's rest mass is set by the closed-track standing-wave wavelength:

<!-- m = 2π ℏ c / L_track -->
$$
m \;=\; \frac{2\pi\,\hbar c}{L_{\text{track}}}
$$

where L_track is the arc length of the closed (1/2, 1) curve on the embedded surface. The ratio m_n / m_p is therefore L_p / L_n — a purely geometric ratio that depends on the substrate's modulation and the ring radius R_major. Chapter 5 derives this; for orientation, the modulated-clover with the symmetric Step-7 modulation and R_major ≈ 36.17 (in script units) reproduces the observed m_n / m_p = 1.001 378 4 to machine precision.

R_major itself is a free parameter of the construction. It sets the *absolute* mass scale but the construction does not currently derive it from a deeper principle. This is named openly in the README as one of the project's two open questions inside its scope.

### 4.4 Quark substructure as a three-arc-piece series

The closed (1/2, 1) track on the symmetric modulated-clover passes through three arc-pieces of the cross-section in series. The cross-section has six arc-pieces total (3 convex *lobes* + 3 concave *saddles* under the Z₂ × Z₃ symmetry); the (1/2, 1) track samples three of them as θ runs from 0 to 2π:

- The *proton* track at t₀ = −π/6 passes through *lobe → saddle → lobe* — three arc-pieces in the sequence (u, d, u), i.e. uud-ordered.
- The *neutron* track at t₀ = +π/6 passes through *saddle → lobe → saddle* — sequence (d, u, d), i.e. udd-ordered.

A **quark** is identified with one arc-piece in this series. The proton's three quark-pieces are two u's (the two lobes) and one d (the saddle). The neutron's are one u and two d's. The constituent-quark mass is m_baryon / 3 (~ 313 MeV when m_baryon = m_proton).

The per-arc *fractional charge values* (±2/3 / ∓1/3) deserve a careful statement, since the framework's textbook values come out only in a specific idealised limit. On the piecewise-circular kissing-circles clover — three 240° lobe arcs of constant geodesic curvature κ = +1/r and three 120° saddle arcs of constant κ = −1/r — the per-arc integral gives exactly +2/3 (lobe, u) and −1/3 (saddle, d). On the smooth Fourier-series cross-section that the construction actually uses (a₁(θ) cos 3t + a₂ cos 6t and its imaginary counterpart), the per-arc readings are *smeared* (numerically ~+0.59 per arc on the proton, ~−0.26 per arc on the neutron) because the continuous-curvature distribution does not concentrate the winding at sharp arc boundaries. The *integer* baryon charges Q_p = +1 and Q_n = 0 are preserved exactly in both representations.

This arc treats the smeared per-arc values as a *structural prediction* of the smooth construction, not as a fitting failure. The textbook ±2/3 / ∓1/3 are the kissing-circles limit; the construction's actual values would need to be checked against integrated observables (the R-ratio analog, magnetic-moment ratios, parton-distribution shapes) in future work to see whether the smearing is empirically tolerated. Chapter 5 develops the per-arc machinery; the work file [quark-decomposition.md](work/quark-decomposition.md) records the computational evidence.

### 4.5 Color as the Z₃ phase-track index

The modulated-clover substrate has exact Z₃ rotational symmetry around the major-ring axis — a 120° rotation of the 3-D embedding maps the surface to itself. Under this Z₃, the proton's closed track maps to two other 3-fold-related closed tracks (and similarly for the neutron). These three Z₃-related closed tracks are not three different particles; they are three *color states* of the same baryon.

**Color is geometric in this framework.** It labels which of the three Z₃-related phase tracks the wave-quantum is currently observed on. It is not an internal Hilbert-space quantum number bolted onto the wave-quantum from outside; it is a substrate-level structural feature. The standard-model color SU(3) and our construction's Z₃ are different objects — SU(3) is continuous while Z₃ is discrete — and identifying them rigorously is an open structural item. What the construction does deliver is the discrete 3-fold structure that the standard-model SU(3) collapses to in the *color-singlet* sector.

### 4.6 The framing this arc commits to, and the alternatives that were tried

The framing is: *single wave-quantum per baryon, with charge content organised as a 3-arc-piece series along its characteristic curve, and three Z₃-related color states by substrate symmetry*.

This was not the first framing the framework tried. The work files [lb-mode-localization.md](work/lb-mode-localization.md), [quark-decomposition.md](work/quark-decomposition.md), and [quark-wannier-decomposition.md](work/quark-wannier-decomposition.md) record the alternatives that were explored before this reading settled:

- *Single quantum as a track-localised LB eigenmode.* Ruled out by direct numerical computation — no LB eigenmode and no low-energy superposition is appreciably track-localised on the substrate.
- *Three quark-quanta combined as a Slater determinant.* Would require a fermionic spinor upgrade of the substrate field; held in reserve for downstream work that the scalar-field construction cannot reach.
- *Nine wave functions in a 3×3 quark × color matrix, with Wannier-function localisation on each track.* Agreed with the simpler 3-arc-piece-in-series reading without adding predictive content; demoted to exploratory record.

The 3-arc-piece-in-series reading is what this arc commits to. The demoted alternatives remain in the work files; if downstream chapters (Δ baryons, mesons, magnetic moments) require richer structure than the scalar-field construction supports, those work files are the entry points to revisiting the framing.

---

## 5. Scope — single generation, generation-agnostic form

A short declarative section that draws the scope.

### 5.1 In scope: the u-d hadron generation

The arc derives the proton and neutron as the two (1/2, ±1) baryon modes of one modulated-clover substrate, with one set of parameter values (R_major ≈ 36.17 and the symmetric Step-7 modulation coefficients). Subsequent chapters add the per-arc charge derivation (Ch 4), the path-length mass derivation (Ch 5), and the discrete symmetries (Ch 6). The arc does not extend to the Δ baryons, the light mesons, or multi-flavor hadrons; these are listed in the README's §What we don't predict.

### 5.2 The construction's form is structural

The construction's form — half-twist τ = 1/2, N = 3 cross-section, Z₂ × Z₃-symmetric modulation, two (1/2, ±1) tracks at t₀ = ∓π/6, six baryon replicas in the Z₂ × Z₃ orbit — is set by the topology and the symmetry group. None of these structural features depends on the choice of quark generation. The same form would in principle host any quark-generation baryon pair, with different parameter values.

### 5.3 Generation-specific parameters

Only the *parameter values* of the modulation are generation-specific. R_major sets the absolute mass scale of the baryon doublet on this sheet; the modulation amplitudes (Ac₁, As₁, Bc₁, Bs₁, a₂, b₂) set the mass split between the proton-analog and the neutron-analog. Generation 1 (u-d) gets R_major ≈ 36.17 and the symmetric Step-7 coefficients reported in [modulated-clover.md](work/modulated-clover.md). Whether the construction's parameter range extends to the much wider mass ratios of generations 2 (c-s, with m_s/m_c ≈ 0.07) and 3 (t-b, with m_b/m_t ≈ 0.024) is an empirical open question. The form is generation-agnostic; whether it accommodates *all* three generations is for downstream work to test.

### 5.4 Handoff to ma-domain

[ma-domain](../ma-domain/) is the project that takes the single-generation result and asks whether three generations + the charged-lepton sector + the neutrino sector can be hosted in one multi-dimensional compact domain, with each sheet emerging as one cross-term in a sparse N×N metric. Sheet-proton supplies the *worked example* of one generation on one cross-term. The half-twist τ = 1/2 modulated-clover that this project settles on supersedes the older τ = 1/3 clover-quarks precedent that ma-domain's current scaffolding inherits; ma-domain's multi-generation architecture should adapt to τ = 1/2 rather than the older convention.

---

## 6. Summary

The chapter sets up what every subsequent chapter inherits.

- The arc's *empirical target* is the u-d hadron generation, with the quantum numbers listed in §1.
- The arc's *foundational inputs* are picture A (the scalar wave equation on T²), the closure condition, the Z₂ × Z₂ handedness structure, and the load-bearing hypothesis G1 (per-arc geodesic curvature = local charge density). All inherited from metric-charge (§2).
- The arc's *coordinates* are the substrate (t, θ), the mode labels (m, n) with the (1/2, ±1) baryon modes, and the sign conventions for geometric chirality and C-conjugation (§3).
- The arc's *framing* is: each baryon is one wave-quantum on the substrate; its electric charge is a per-arc geodesic-curvature integral along its closed (1/2, 1) characteristic curve; its mass is the closed-track standing-wave wavelength; its quark substructure is the series of three arc-pieces the track passes through (lobe-saddle-lobe = uud for the proton, saddle-lobe-saddle = udd for the neutron); its three color states are the three Z₃-related phase tracks. The framing is a commitment, not yet a derivation — chapters 2–6 derive that the commitment is *consistent* (§4).
- The arc's *scope* is one generation, with a structurally generation-agnostic form whose parameter range may or may not accommodate the heavier generations — that question is left to ma-domain (§5).

The next chapter builds the substrate.
