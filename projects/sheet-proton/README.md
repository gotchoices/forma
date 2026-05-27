# sheet-proton

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** Detailed exploration of what the proton sheet might uniquely look like — geometry, internal structure, quark content, mediator physics, strong-force mechanism. The proton-specific complement to [metric-binding](../metric-binding/), which addresses general multi-knot binding on a generic sheet.
**Method:** Mathematical derivation as discovery; geometric construction; minimal computation. Work-file-driven (see [work/](work/)), with chapter-level prose emerging only after work files converge on stable conclusions.
**Status:** Active. Work files have settled on the **modulated-clover construction** ([work/modulated-clover.md](work/modulated-clover.md), [work/derived-clover.md](work/derived-clover.md)) as the candidate proton-sheet substrate. Under named hypotheses (C1–C6 + G1) the construction *fits* the integer baryon charges Q_p = +1, Q_n = 0 and the mass ratio m_n / m_p exactly — by tuning the modulation amplitudes and the major-ring radius R_major — while preserving exact Z₂ × Z₃ symmetry and a Z₂ × Z₂ chirality × matter-antimatter structure. The formal chapter arc (below) begins drafting from this groundwork; see [work/STATUS.md](work/STATUS.md) for the current per-file state.

## Why this project exists

The MaSt framework treats each particle as a knot or compound on a 2D compact sheet (T²), with the sheet's parameters (aspect ratio ε, shear σ_uw) determining the sheet's *character*. [metric-mass](../metric-mass/) developed mass from a single compact dimension; [metric-charge](../metric-charge/) extended to the 2D sheet and identified charge as topological winding; [metric-binding](../metric-binding/) takes up the multi-knot interaction question on a generic sheet.

This project takes up the specific question: **what does the *proton* sheet look like uniquely?** Not "how do generic knots interact on a generic sheet" (metric-binding's job), but "what specific geometric structure, what specific quark assignments, what specific binding mechanism characterize the sheet that hosts the proton, neutron, and the nuclear-scale physics that lives on it?"

The central question:

> *Given that observed nuclear physics is hosted on what MaSt calls the proton sheet, what specific structural commitments — sheet geometry, primitive (m, n) assignments, mediator-mode content, composite-mode binding mechanism — must the proton sheet make in order to reproduce the observed phenomenology?*

The empirical reference points the project is built around:

- **Proton:** charge +1, mass 938.27 MeV, composite of three quarks (uud), with Z₃ confinement.
- **Neutron:** charge 0, mass 939.57 MeV, composite (udd), unstable with τ ≈ 880 s.
- **Quarks:** u and d carry fractional charges (+2/3, −1/3); other flavors (s, c, b, t) are heavier siblings.
- **Pion** and other light mesons: 2-component qq̄ compounds; π mass ≈ 140 MeV.
- **Strong force:** Yukawa-shaped, range ≈ 1.4 fm (the pion's Compton wavelength), much stronger than EM at short range.
- **Nuclear binding:** from 2.2 MeV/nucleon for deuteron to ~8.8 MeV/nucleon for medium-mass nuclei.

Each of these constrains the proton sheet's character. The project's work files investigate the constraints from different angles.

### The C1–C6 + G1 hypothesis chain

The construction's named hypotheses, in one place (full statements in [work/derived-clover.md](work/derived-clover.md)):

| | Hypothesis | One-line statement |
|---|---|---|
| **C1** | Substrate topology | The substrate is a 2-torus T² with one tube direction t and one ring direction θ. (Inherited from [metric-charge Ch 1](../metric-charge/01-foundation.md).) |
| **C2** | Color → cross-section 3-fold symmetry | The cross-section has 3-fold rotational symmetry, realised through harmonic content cos 3t, cos 6t (and sin equivalents). |
| **C3** | Closure → surface twist | The closed (1/2, 1) baryon tracks require the surface to carry a matching twist α(θ); the half-twist α = θ/2 is the choice this construction commits to. |
| **C4** | Ring-axis 3-fold symmetry | The 3-D-embedded surface is invariant under 120° rotation around the major-ring axis. This pins the modulation harmonics to the Z₂ × Z₃-symmetric subspace. |
| **C5** | Per-arc charge under G1 | Along each (1/2, 1) track, the integrated geodesic curvature gives the integer winding number; signed sub-arc contributions give a fractional partial structure (this is hypothesis **G1** of [metric-charge Ch 11 §6](../metric-charge/11-modeling-foundation.md)). |
| **C6** | Proton / neutron identification | The two distinct (1/2, 1) tracks at t₀ = ∓π/6 are the proton and neutron; the Z₂ × Z₃ orbit of one fundamental track is the 6 baryon replicas (3 colors × 2 isospin). |

## Coordinates and notation

The modulated-clover construction uses the following parameters
and coordinates (developed in [work/derived-clover.md](work/derived-clover.md)
and [work/modulated-clover.md](work/modulated-clover.md)):

| Symbol | Role | Type |
|---|---|---|
| **t** | Tube (cross-section) direction; the (1/2, 1) tracks vary t with θ | Compact: t ∈ [0, 2π), wraps |
| **θ** | Ring (major-circle) direction | Compact: θ ∈ [0, 2π), wraps |
| **(m, n)** | Winding pair (m = tube winding, n = ring winding) | Half-integer/integer pair; baryon modes are (1/2, ±1) |
| **α(θ)** | Twist rate around the ring; α(θ) = θ/2 here (half-twist) | Function of θ |
| **a₁(θ), b₁(θ)** | k = 1 cross-section modulation amplitudes (Z₂ × Z₃-symmetric subspace) | Each = Ac₁ cos(3θ/2) + As₁ sin(3θ/2); 4 parameters total |
| **a₂, b₂** | k = 2 cross-section backbone amplitudes (3-fold-symmetric Z_6 dihedral) | Real |
| **ρ** | Overall cross-section scale | Sets the tube-radius unit |
| **R_major** | Major-ring radius, *in units of ρ* | Sets the absolute mass scale via m ∝ 1/R_major; the construction fits the baryon doublet at R_major ≈ 36.17 (dimensionless ratio R_major / ρ) |
| **t₀** | Track-label; proton's track at t₀ = −π/6, neutron's at t₀ = +π/6 | Real |

The dimensionless R_major ≈ 36.17 in script units is the
*ratio* of the major-ring radius to the cross-section scale ρ. To
fix an absolute physical scale, one would set ρ so that the resulting
m = 2π ℏ c / L_track matches the observed nucleon mass; the
construction does not yet derive ρ from a deeper principle.

**Predecessor notation.** [metric-charge](../metric-charge/) generic
sheets use (u, w) coordinates with aspect ratio ε = L_u / L_w and
shear σ_uw. The (u, w) ↔ (t, θ) correspondence is u ↔ t (tube), w ↔ θ
(ring); the (ε, σ_uw) parameterisation is not the operative
parameterisation in this construction. Earlier proton-sheet (ε, σ_uw)
parameter fits from R-studies (R64 Point A, R64 Point B) are
historical precedents whose relationship to the modulated-clover is
not currently load-bearing for the arc; see §What we don't predict
for the open reconciliation.

## Ground rules

1. **Inherit from foundational projects.** The framework's prior projects ([metric-mass](../metric-mass/), [metric-charge](../metric-charge/), [metric-binding](../metric-binding/), [grid-duality](../grid-duality/)) are taken as established input. Closure rule, charge promotion, sheet-character framework, wrap-promotion ladder, α-coupling — cite where used; don't re-derive.

2. **Discovery, not proof.** Let the math reveal what specific commitments the proton sheet requires.

3. **Empirically anchored.** Each work file targets a specific empirical observation. Predictions must engage with measured values; "looks structurally right" is not enough.

4. **Variables stay symbolic where possible.** Pin numerical values only when the algebra (or empirical comparison) forces it. Per the no-premature-pinning rule.

5. **Work-file-driven.** The project develops via work files in [work/](work/), which crystallize into chapter-level prose only after their hypotheses are tested.

6. **Computation when required.** Paper math first; scripts only when verification of a hypothesis or comparison against empirical data requires it.

## Goals

### Overriding goal

A 2D compact sheet (T² substrate with shaped cross-section) that hosts
**every observed quark-based particle drawn from a single quark
generation** — i.e., the full u-d hadron spectrum — together with
clean structural identifications for every associated quantum number
(charge, mass, spin, isospin, color, parity, baryon number, matter/
antimatter). Heavier-quark generations are presumed to live on
separate sheets and are out of scope, *except* that the construction
must not depend anywhere on "every baryon lives on exactly one sheet"
(see Chapter 7's multi-sheet caveat).

### Generation-agnostic form, generation-specific parameters

The construction's *form* — the half-twist τ = 1/2 modulated-clover
with N = 3 cross-section and Z₂ × Z₃-symmetric modulation subspace
— is **not** specific to the u-d generation. It is a structural
geometry whose features (two (1/2, 1) tracks at t₀ = ∓π/6, six
baryon replicas, the per-arc charge bridge) are inherited from the
topology and the symmetry group, not from any quark-generation
choice. The *parameters* (R_major fixing the absolute mass scale,
modulation amplitudes fixing the proton/neutron-analog mass split)
are generation-specific.

For generation 1 (u-d): R_major ≈ 36.17 and the symmetric Step-7
modulation fit the proton + neutron mass ratio to numerical
precision. For generations 2 and 3, *different* parameter values
would be needed, and whether the construction's parameter range
actually extends to the much wider heavier-generation mass ratios
(m_s/m_c ≈ 0.07, m_b/m_t ≈ 0.024) is **an empirical open question**,
deferred to [ma-domain](../ma-domain/). The form is
generation-agnostic; whether it accommodates *all* three
generations is for ma-domain to test.

## Status of the construction

What the work files have settled — distinguishing *what is fit* from
*what is derived* throughout.

### What the construction commits to

1. **Sheet geometry — modulated-clover substrate.** N=3 harmonic
   cross-section (3 major + 3 minor lobes; 6 equal pieces) swept with
   a **half-twist** α(θ) = θ/2 and a **θ-dependent modulation** of the
   3-fold harmonics restricted to the Z₂×Z₃-symmetric subspace.
   ([work/modulated-clover.md](work/modulated-clover.md),
   [work/derived-clover.md](work/derived-clover.md))

2. **Proton and neutron tracks.** The two distinct (1/2, 1) torus
   knots at t₀ = ∓π/6 — closing in one ring revolution via the
   half-twist identification. The Z₂ × Z₃ orbit of one fundamental
   track is the six baryon replicas (3 colors × 2 isospin).

3. **Charge mechanism.** Per-arc geodesic curvature integrated along
   the track, under hypothesis G1 (per [metric-charge Ch 11 §6](../metric-charge/11-modeling-foundation.md)).
   The integer baryon charges Q_p = +1, Q_n = 0 are reached by a
   *two-parameter tuning* of the modulation amplitudes (the cos- and
   sin-harmonics fix Q_p + Q_n = 1 and Q_p − Q_n = 1 respectively).
   This is a fit to the targets, not a derivation that the integers
   must take those values; the construction shows the targets are
   achievable with two free parameters, not that they are forced.

4. **Quark substructure.** The (1/2, 1) track passes through three
   arc-pieces in series: lobe-saddle-lobe (proton, uud-ordered) or
   saddle-lobe-saddle (neutron, udd-ordered). A quark is one such
   arc-piece; the constituent-quark mass is m_baryon / 3. Under G1
   the per-arc charges are +2/3 (lobe, u) and −1/3 (saddle, d) on
   the piecewise-circular (kissing-circles) idealisation. On the
   smooth Fourier-series cross-section actually used by the
   construction, the per-arc readings are *smeared* away from these
   discrete values (numerically ~+0.59 / ~−0.26 per arc) while the
   *integer* baryon charges Q_p = +1, Q_n = 0 are preserved exactly.
   The relationship between the smooth-substrate per-arc values and
   the standard-model ±2/3, ∓1/3 — well established by DIS, R-ratio,
   parton distributions — is open. The construction does not
   currently *predict* the standard-model values; whether the
   smooth-substrate values are empirically tolerated depends on
   which observables they actually feed.

5. **Color identification.** The three Z₃-related phase tracks of a
   single baryon are its three color states. Color is read here as
   the discrete Z₃ orbit on the substrate. This is a *structural
   analog* of the standard-model SU(3) gauge group — they share the
   3-fold confinement-like structure but are different mathematical
   objects (SU(3) is continuous, with 8 generators; Z₃ is discrete,
   with 1 generator). Promoting from the Z₃ analog to full SU(3)
   gauge structure is a route the framework lacks a mechanism for
   and is deferred. See [metric-charge Ch 11 §7](../metric-charge/11-modeling-foundation.md)
   for parallel language on this distinction.

6. **Mass mechanism.** Path-length:

   <!-- m = 2π ℏ c / L_track -->
   $$
   m \;=\; \frac{2\pi\,\hbar c}{L_{\text{track}}}
   $$

   treating the closed (1/2, 1) track as a standing wave whose
   wavelength equals the track's arc length. The mass-ratio sign
   m_n > m_p falls out of the construction directly (the neutron's
   modulation gives a slightly shorter track than the proton's); the
   ratio's *magnitude* m_n / m_p ≈ 1.001 378 is a one-parameter fit,
   set by the major-ring radius R_major ≈ 36.17. R_major itself is
   not derived from a deeper principle; the *absolute* baryon mass
   scale m_p remains calibration, not prediction.

7. **Discrete symmetries.** Z₂ × Z₂ — geometric chirality
   ((m, n) ↔ (m, −n)) × matter/antimatter (C, (m, n) ↔ (−m, −n)).
   Identification with γ⁵-chirality requires a spinor upgrade and is
   deferred.

### Open questions inside the construction's scope

These are gaps the arc *can in principle* close with further work
on the modulated-clover, the per-arc integral, or the LB spectrum.

1. **(1/2, 1) winding outside standard closure.** The half-integer
   tube winding of the baryon tracks sits outside the closure-mode
   derivation of [metric-charge Ch 4](../metric-charge/04-the-closure-condition.md).
   The construction works around this by building a matching
   half-twist into the substrate's surface identification
   (t, θ + 2π) ~ (t + π, θ), so the (1/2, 1) tracks close in one
   ring revolution. Whether the (1/2, 1) modes are closure-satisfying
   *in the substrate-extended sense* — and what the precise
   substrate-extended closure rule is — is a real foundational gap.
   Flagged in [work/modulated-clover.md §6](work/modulated-clover.md).

2. **Closed-form charge integral.** Push M(t₀) = Q(t₀) − ½ to an
   analytical expression in (Ac₁, As₁, Bc₁, Bs₁, a₂, b₂) via
   Weierstrass substitution. Currently first-order expansion +
   numerical verification at full amplitudes.

3. **R_major as a free parameter.** Identify an independent input
   that pins R_major (e.g., a Compton-scale identification for the
   lightest stable baryon, or a relation to the substrate's
   gravitational scale). Without that, m_p is calibration, not
   prediction.

### What we don't predict

Topics outside the construction's reach at the scalar-field level.
Each is a flagged limitation rather than a derivable consequence.

- **Absolute baryon mass scale.** R_major is a free parameter; the
  construction matches m_n/m_p but not m_p itself.
- **Spin and magnetic moments.** A scalar field on the substrate
  has no spin structure; spin-½ and the proton's magnetic moment
  require a *spinor upgrade* (promote the substrate field to a
  spin-½ Dirac field with the substrate's spin structure). Standard
  technique, but a real piece of machinery, deferred.
- **Δ baryons** (spin-3/2 u-d baryons). Their mass split from the
  nucleon (Δ−N ≈ 293 MeV) is a hyperfine-structure prediction that
  also needs the spinor upgrade.
- **Light mesons** (π, η, ρ, ω). These are qq̄ compound modes that
  require a *multi-mode* construction on the same substrate; the
  framework has not yet built the compound-mode machinery.
- **Multi-sheet hadrons** (Λ, Σ, Ξ, Ω). These require a coupling
  mechanism between sheets of different quark generations; the
  mechanism lives in [metric-binding](../metric-binding/) and/or
  [ma-domain](../ma-domain/), not on this sheet.
- **Standard-model intrinsic parity P** as distinct from geometric
  chirality. The scalar-field framework collapses these into one
  Z₂; distinguishing them requires the spinor upgrade.
- **The strong force** as a derived interaction with Yukawa shape and
  ≈ 1.4 fm range. Currently a target for the construction (see
  [work/strong.md](work/strong.md)) but not derived.
- **Nuclear binding curves** (R64 Point A vs Point B). The deuteron
  / mid-mass nuclei binding fits in [studies/R64-nuclear-harmonic-stack](../../studies/R64-nuclear-harmonic-stack)
  use different (ε, σ) parameters than the modulated-clover
  construction; reconciling those parameter readings with the
  modulated-clover is open work.

### Handoff to ma-domain

[ma-domain](../ma-domain/) is the multi-generation reframe in which
this sheet (one u-d generation) becomes one cross-term in an N-dim
compact domain. Sheet-proton has settled on the **half-twist
τ = 1/2** modulated-clover as the operative geometry; ma-domain's
multi-generation architecture should adapt to that rather than to
the older τ = 1/3 clover-quarks precedent (`work/clover-quarks.md`,
which is superseded by `work/modulated-clover.md` and
`work/derived-clover.md`). The proton-sheet construction's job is
to *be one cross-term* cleanly; the multi-cross-term composition
is ma-domain's problem.

## Background reading

**Foundational projects.** Inherited results used by the arc:

- [metric-charge/](../metric-charge/) — single-knot framework on a 2D sheet; closure conditions, sheet character, the G1 per-arc curvature → charge bridge (Ch 11 §6).
- [metric-mass/](../metric-mass/) — single-compact-dimension precursor; standing-wave reading.
- [metric-binding/](../metric-binding/) — general multi-knot binding framework, sibling project; sheet-proton is the specific application to the proton sheet.
- [grid-duality/](../grid-duality/) — substrate-level framework; α-coupling.
- [ma-domain/](../ma-domain/) — multi-generation reframe; downstream of this project.

**Historical precedents.** Earlier readings of the proton sheet that
predate the modulated-clover construction. These are useful orientation
but are *not* load-bearing for the chapter arc, and the arc does not
promise to reconcile their parameter choices with the modulated-clover.

- [studies/R64-nuclear-harmonic-stack/](../../studies/R64-nuclear-harmonic-stack/) — proton-sheet (ε, σ) Point A / Point B fits; harmonic-stack reading.
- [studies/R63-proton-tuning/](../../studies/R63-proton-tuning/) — proton/neutron pair tuning, complementary nodes.
- [studies/R53-three-generations/](../../studies/R53-three-generations/) — three-generation structure; quark flavor identification.
- [studies/R54-compound-modes/](../../studies/R54-compound-modes/) — cross-sheet compound modes (model-E alternative).

## Work files

See [work/](work/) for active explorations. [work/STATUS.md](work/STATUS.md) tracks the current per-file state, dependencies, and next actions in detail. For quick orientation:

| File | Role |
|---|---|
| [modulated-clover.md](work/modulated-clover.md) | The operative substrate construction. Steps 1–7. |
| [derived-clover.md](work/derived-clover.md) | Formal derivation framework: C1–C6, per-arc charge integral, symmetric finding, discrete symmetries. |
| [lb-mode-localization.md](work/lb-mode-localization.md) | Computational test — no LB track localisation. Folded into the framing. |
| [quark-decomposition.md](work/quark-decomposition.md) | First test of 3-quarks-in-series; per-arc charges live in cross-section, not track integral. |
| [quark-wannier-decomposition.md](work/quark-wannier-decomposition.md) | *Exploratory record (demoted).* Wannier formalisation agreed with the simpler picture; piecewise-circular vs smooth-Fourier finding folded in. |
| [clover-quarks.md](work/clover-quarks.md) | *Predecessor (superseded).* τ = 1/3 with piecewise-circular arcs; not load-bearing for the arc. |
| Other work files | Frontier / out-of-scope for current arc. See [work/STATUS.md](work/STATUS.md) for the full per-file breakdown. |

## Framing — one wave-quantum per baryon, with quark substructure along the track

A baryon is one wave-quantum on the modulated-clover. Its charge
comes from the per-arc curvature integral along its (1/2, 1)
characteristic curve under hypothesis G1 (inherited from
[metric-charge Ch 11](../metric-charge/11-modeling-foundation.md));
its mass comes from the closed-track wavelength
m = 2π ℏ c / L_track. The wave equation lives on the substrate;
the characteristic curve is where the curvature integral is taken.
A baryon is one wave-quantum, not three quark-quanta, not a
track-localised LB eigenmode.

The *quark substructure* of a baryon lives inside the per-arc
curvature integral along one track. A closed (1/2, 1) track on
the symmetric modulated-clover passes through the cross-section
in series — alternating convex (lobe) and concave (saddle)
arcs. The proton track at t₀ = −π/6 passes through lobe-saddle-lobe
(uud-ordered); the neutron track at t₀ = +π/6 passes through
saddle-lobe-saddle (udd-ordered). A **quark** is identified with
one arc-piece in this series; the proton's three quark-segments
sum to its total integer charge +1, the neutron's to 0.

Per-quark *fractional* charge values depend on the cross-section
representation. On the idealised piecewise-circular kissing-circles
clover (constant geodesic curvature κ = ±1/r on each 240° / 120°
arc), the per-arc reading gives exactly +2/3 (lobe, u) and −1/3
(saddle, d). On the smooth Fourier-series cross-section actually
built by `modulated_clover.py`, the per-arc reading is smeared
(~+0.59 per arc for the proton, ~−0.26 for the neutron) because
the continuous-curvature distribution doesn't concentrate the
winding at sharp arc boundaries. The integer baryon charges
Q_p = +1, Q_n = 0 — the empirical anchors — are recovered in both
representations by tuning the modulation amplitudes. The
relationship between the smooth-substrate per-arc values and the
standard-model ±2/3 / ∓1/3, which are well-established empirically
(DIS, R-ratio, parton distributions), is an **open identification
question**, not a derivation the construction has yet completed.

The Z₃ ring-axis screw maps each baryon's closed track onto two
3-fold-related copies. These three Z₃-related phase tracks are
three *color states* of the same baryon. **Color is read here as
the discrete Z₃ orbit** — a structural analog of the standard-model
SU(3) gauge group, sharing its 3-fold confinement-like structure
but a discrete rather than continuous mathematical object. The
relationship to full SU(3) gauge theory is the same open
identification question that [metric-charge Ch 11 §7](../metric-charge/11-modeling-foundation.md)
flags between the framework's Z₃ structural analog and gauge
SU(3); see that section for parallel language.

### The Berry-phase-style reading of the charge integral

The per-arc charge integral has a structural feature worth naming
explicitly. Its integrand is the geodesic-curvature 1-form along
the (1/2, 1) characteristic curve — a property of *how the
cross-section tangent winds* along the curve, not of *where the
wave's amplitude is concentrated*. In this respect the integral
is **Berry-phase-like**: its value comes from the curve's
geometric content, not from a probability-density weight.

This compatibility is needed because the LB-mode-localisation test
([work/lb-mode-localization.md](work/lb-mode-localization.md))
showed that no LB eigenmode and no low-energy superposition is
appreciably track-localised on the modulated-clover at the
proton's energy scale (depth < 1% at √⟨H⟩ = 2π/L_track). The
wave-quantum's amplitude is global, but its charge content can
still be along-the-track if the integral does not weight by
amplitude.

The Berry-phase-like reading is an **additional structural
commitment** on top of hypothesis G1, not a consequence of it. G1
states that local geodesic curvature equals local charge density;
the framing here states that the integral along the characteristic
curve gives the wave-quantum's charge without amplitude weighting.
The framework currently asserts this reading; it has not been
derived from first principles. Treating it as an open structural
claim — not yet a theorem — is the honest position. Chapter 5
names the assertion and flags it as such.

## Chapter arc

The arc proceeds from inputs → substrate → modes → charge →
mass-and-quarks → symmetries → limits-and-handoff. Seven chapters,
each backed by settled work files. Topics that the construction
doesn't yet derive (Δ baryons, mesons, magnetic moments, absolute
mass scale, multi-sheet hadrons) are declared as deferred in the
final chapter, not promised as content.

| # | Title | Role |
|---|---|---|
| 1 | **Foundation** | Inputs from [metric-charge](../metric-charge/) (picture A, the wave-equation framework, the per-arc charge bridge under G1); coordinates and conventions; the central question this project answers ("what specific 2D substrate hosts the u-d hadron generation?"); the framing — one wave-quantum per baryon, with quark substructure organised in series along its characteristic curve. |
| 2 | **The modulated-clover substrate** | The harmonic N = 3 cross-section family (3 major + 3 minor lobes, six equal pieces). Closure of the surface: allowed twists are multiples of 1/6; the **half-twist** τ = 1/2 is the operative case. Modulation a₁(θ), b₁(θ) restricted to the Z₂ × Z₃-symmetric subspace. The substrate is set up as a *resonator* (the cavity language), not a particle space. |
| 3 | **Modes and their characteristic curves** | The wave-quantum's characteristic curve — the (1/2, 1) torus knot on the modulated-clover, closing under the half-twist identification. The (1/2, 1) winding sits outside metric-charge Ch 4's closure-mode derivation; the chapter names the substrate-extended closure as an open structural claim. The two distinct curves at t₀ = ∓π/6 — proton and neutron. The Z₂ × Z₃ orbit gives 6 baryon replicas: 3 color phases of the proton and 3 of the neutron. The characteristic curve is where the per-arc charge integral is taken, not where the wave-quantum's amplitude is concentrated (see Ch 5). |
| 4 | **Charge from per-arc curvature** | The per-arc reading of charge along the characteristic curve, under G1 (inherited). The clean identity Q(t₀) = ½ + M(t₀). Solving the symmetric modulation for M(±π/6) = ±½. Result: the integer baryon charges Q_p = +1, Q_n = 0 are reached by a *two-parameter fit* to the modulation amplitudes — the targets are achievable, not forced. The **series structure** of convex (lobe) and concave (saddle) contributions along one track is the input to Chapter 5's quark decomposition. |
| 5 | **Mass and quark substructure** | The path-length mass m = 2π ℏ c / L_track on the (1/2, 1) tracks, treating the closed track as a standing wave. The closed track passes through **three arc-pieces in series**: lobe-saddle-lobe = uud-ordered (proton) and saddle-lobe-saddle = udd-ordered (neutron). Each arc-piece is one constituent quark; constituent-quark mass = m_baryon / 3 ≈ 313 MeV. Per-quark fractional charges: ±2/3 / ∓1/3 on the piecewise-circular idealisation; smeared on the smooth Fourier construction (see Framing above for the open identification question). Color identification: Z₃ structural analog of SU(3). LB-localisation result reported as a finding; Berry-phase-like reading of the charge integral named as an open structural claim. Mass-ratio fit m_n / m_p ≈ 1.001 378 at R_major ≈ 36.17. R_major's status as the one undetermined free parameter that the construction does not yet derive. |
| 6 | **Symmetries — chirality, isospin, color, C** | The Z₂ × Z₂ structure on baryon modes: chirality ((m, n) ↔ (m, −n)) and matter/antimatter ((m, n) ↔ (−m, −n)). The Z₃ ring-axis rotation = color (Z₃ structural analog of SU(3) gauge structure). The Z₂ proton/neutron swap = isospin I_3 = ±½. Geometric chirality (the framework's only handedness at the scalar-field level) vs γ⁵-chirality (requires the deferred spinor upgrade). Baryon number = track winding count. |
| 7 | **Limits, handoff, and closing summary** | What the construction *establishes* under named hypotheses (charge fit, mass-ratio fit, quark substructure, color analog, chirality, baryon number). What it *does not predict* (see §What we don't predict). Single-generation scope. Multi-sheet hadrons (Λ, Σ, Ξ, Ω) need a coupling mechanism in [metric-binding](../metric-binding/) and/or [ma-domain](../ma-domain/). The handoff to ma-domain: τ = 1/2 modulated-clover is sheet-proton's settled geometry; ma-domain's multi-generation architecture is free to adapt to it rather than the τ = 1/3 clover-quarks precedent. Parallel in role to [metric-charge Ch 10](../metric-charge/10-closing-summary.md). |

### Appendix A — Closed-form analytical machinery

A planned appendix companion to the chapter arc, parallel in role
to [metric-charge Ch 11](../metric-charge/11-modeling-foundation.md):
the Weierstrass-substitution evaluation of M(t₀), the parameter-family
structure of the charge-correct symmetric modulation, and the
analytical form of the track-length integral.
