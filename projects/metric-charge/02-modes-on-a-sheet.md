# Chapter 2 — Modes on a sheet

**Status:** Sparse outline. Each section is one to three sentences describing the derivation step that section will perform. To be expanded into full prose once the outline is approved.

This chapter takes the givens of [Chapter 1](01-foundation.md) — the manifold M, the bare diagonal metric, the real scalar field φ, the massless wave equation □φ = 0, and the periodicity conditions on (u, w) — and works out which solutions the wave equation actually admits. The technical core is a Bloch decomposition on the 2-torus (u, w), which produces a discrete (m, n) mode family.

**Substantial inheritance from grid-duality.** The Bloch decomposition on a 2D periodic substrate, the band-extremum origin of mass, and the integer-quantization of winding numbers are all worked out in detail in [grid-duality §7](../grid-duality/07-wrap-promotion-modeling.md). This chapter does not re-derive them. We cite grid-duality and specialize its results to the metric-charge setting (continuum 2-torus rather than discrete lattice; spacetime embedding rather than abstract substrate).

**Inheritance from metric-mass.** The slow-motion inertial-mass argument (metric-mass §6 of Chapter 2) carries over with one extra integer index. Cited, not re-derived.

The chapter's distinctive job is the spacetime-side framing: identifying the (0, 0) zero mode with massless propagation in (S₁, S₂), naming the single-axis (m, 0) and (0, n) modes as **L2-embedded-in-L3** candidates for closure-failure mass-only states (the structural neutrino-class origin), and setting up the (m, n) labels for use in chapters 3–9.

---

## Bare outline

### 1. Setup: wave equation, separation, periodicity

Restate the wave equation from Chapter 1 §8 on the 5D manifold (t, S₁, S₂, u, w). Apply separation of variables — routine 5D extension of metric-mass §1. The (t, S₁, S₂) part gives continuous plane-wave/oscillator solutions; the (u, w) part is constrained by the periodicity boundary conditions of Chapter 1 §9.

The (u, w) sub-problem is a Bloch decomposition on a 2-torus. **Cite [grid-duality §7.3](../grid-duality/07-wrap-promotion-modeling.md) for the full Bloch machinery** (plane-wave decomposition, band structure, Brillouin zone). Specialize: in continuum (rather than lattice), the dispersion is exact and the (m, n) labels run over all of ℤ² rather than a finite set.

### 2. The (m, n) mode family

Periodicity in u quantizes k_u = 2π m/L_u with m ∈ ℤ; periodicity in w quantizes k_w = 2π n/L_w with n ∈ ℤ. The mode is labeled by an **integer pair (m, n)** — the winding numbers in u and w. This is the substrate for everything in chapters 3–9.

**Identification with grid-duality's winding pair.** The (m, n) labels of this chapter are exactly the (w_α, w_β) ∈ ℤ² of [grid-duality §7.5](../grid-duality/07-wrap-promotion-modeling.md) — the topological winding numbers that classify wave configurations on T². The integer-quantization is the same fact viewed from two sides: phase-pattern (here) and topology (there).

### 3. The dispersion relation and the rest-mass formula

Substituting the separated solutions into the wave equation produces:

ω²/c² = k_S² + (2π m/L_u)² + (2π n/L_w)²

with k_S² = k_{S₁}² + k_{S₂}² the magnitude of the spatial momentum in the (S₁, S₂) plane. Setting k_S = 0 gives the rest energy and rest mass:

m_(m,n) = (ℏ/c) · √((2π m/L_u)² + (2π n/L_w)²)

The (m, n) ≠ (0, 0) modes carry rest mass; the (0, 0) mode is massless.

**Connection to band-extremum mass.** In grid-duality's framework, mass arises from band curvature at extrema (m_eff = ℏ²/(d²ω/dk²) — see [grid-duality §4.3](../grid-duality/07-wrap-promotion-modeling.md)). For our continuum dispersion, each (m, n) sector has its own dispersion in k_S; the rest mass m_(m,n) is the "gap" at k_S = 0 in that sector. The two pictures (closed-form spacetime calculation vs. band-extremum lattice calculation) agree on the rest-mass formula for the simple bare-metric case treated here.

**Inertial behavior.** The slow-motion proof that m_(m,n) acts operationally as inertial mass is identical in form to metric-mass §6, with one extra integer index. Cite metric-mass; do not re-derive.

### 4. Three mode classes

The (m, n) mode family naturally partitions into three classes, each playing a distinct role in chapters 4–9:

- **(0, 0): the zero mode.** No winding in either direction. Dispersion ω = c · k_S, massless, propagates at speed c through (S₁, S₂). The field is independent of both u and w. *This is ordinary light* in spacetime — it is unaware of the compact structure. Doesn't satisfy the closure condition (chapter 1 §10) and doesn't source any compact-direction off-diagonal metric entries.

- **Single-axis modes (m, 0) and (0, n).** Wind in *one* compact direction only. Carry mass given by the formula in §3 with the other winding zero. Have *one* of (w_α, w_β) nonzero — in [grid-duality](../grid-duality/07-wrap-promotion-modeling.md) terms, these are **L2 phenomena** (mass-only) embedded in the L3 substrate. Per Chapter 1 §10's three-view formulation, they fail the closure condition: the topological view says one winding is zero; the phase-pattern view says one of u or w lacks a complete standing wave; the metric view (chapter 5) says the off-diagonals don't form a valid gauge potential. **Candidate structural origin of neutrino-class neutrality** — flagged for chapter 4 to interrogate.

- **Diagonal modes (m, n) with both nonzero.** Wind in both compact directions. Have both (w_α, w_β) nonzero — proper L3 charged-state candidates. Whether a given (m, n) actually carries observable EM depends on whether it satisfies the standing-wave alignment requirement in addition to the winding requirement (chapter 1 §10's phase-pattern statement). Chapter 4 examines which (m, n) pairs survive.

### 5. Energy and momentum

The four-momentum components for a generic (m, n) mode are a routine extension of metric-mass §5:

E = ℏω,  p_S = ℏ k_S  (in the (S₁, S₂) plane)

and the **compact-direction momenta**:

p_u = (2π ℏ/L_u) m,   p_w = (2π ℏ/L_w) n

The energy-momentum relation reads

E² = (p_S c)² + (m_(m,n) c²)²

with the compact-direction momenta absorbed into m_(m,n). This is the standard relativistic form, as expected.

**The compact-direction momenta are the topological windings.** In [grid-duality §7.5.2](../grid-duality/07-wrap-promotion-modeling.md), the conserved invariants on T² are the line integrals of the wavevector around each cycle: w_α = (1/2π) ∮_α k · dx. For our Bloch modes, this evaluates exactly to (m, n). So p_u and p_w (in physical-momentum units) are p_u = ℏ · (2π/L_u) · w_α and similarly for w_β — the same quantity expressed two ways. This identification is the bridge between the spacetime-momentum view (this chapter) and the topological-charge view (grid-duality §7.5, used in chapter 5 of this project).

### 6. What's next

[Chapter 3 — Knots on the torus](03-knots-on-the-torus.md). Take the (m, n) mode family derived here and reframe it geometrically as closed curves traversing the (u, w) sheet. grid-duality §7.5.1 establishes the topology side (π₁(T²) = ℤ², integer windings); chapter 3's distinctive job is the *geometric visualization* of these topological classes as actual torus knots, the mapping between (m, n) labels and standard torus-knot terminology, and any non-self-intersection constraints that pick out a sub-family of the full ℤ² label set.

---

## What this chapter does **not** do (deliberately)

- **Does not re-derive Bloch decomposition.** Cite grid-duality §7.3.
- **Does not re-derive band-extremum mass.** Cite grid-duality §7.4.3.
- **Does not re-derive integer-quantization of windings.** Cite grid-duality §7.5.4.
- **Does not derive the inertial proof.** Cite metric-mass Chapter 2 §6.
- **Does not develop the metric-side picture of charge.** That is chapter 5's job.
- **Does not classify which (m, n) survive the closure condition.** That is chapter 4's job.
