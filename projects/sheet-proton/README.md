# sheet-proton

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** Detailed exploration of what the proton sheet might uniquely look like — geometry, internal structure, quark content, mediator physics, strong-force mechanism. The proton-specific complement to [metric-binding](../metric-binding/), which addresses general multi-knot binding on a generic sheet.
**Method:** Mathematical derivation as discovery; geometric construction; minimal computation. Work-file-driven (see [work/](work/)), with chapter-level prose emerging only after work files converge on stable conclusions.
**Status:** Active. Work files have converged on the **modulated-clover construction** ([work/modulated-clover.md](work/modulated-clover.md), [work/derived-clover.md](work/derived-clover.md)) as the candidate proton-sheet substrate. The construction reproduces proton/neutron charges and mass ratio exactly under named hypotheses (C1–C6 + G1), respects exact Z₂ × Z₃ symmetry, and supports a Z₂ × Z₂ space of chirality × matter-antimatter discrete symmetries. The formal chapter arc (below) begins drafting from this groundwork.

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

## Coordinates and notation

Inherited from [metric-charge §Coordinates and notation](../metric-charge/README.md#coordinates-and-notation):

| Symbol | Role | Type |
|---|---|---|
| **t** | Time | Extended, real |
| **S₁, S₂** | Spatial extension | Extended, real |
| **u** | First compact coordinate on the proton sheet | Compact: u ~ u + L_u |
| **w** | Second compact coordinate on the proton sheet | Compact: w ~ w + L_w |
| **ε** | Aspect ratio L_u / L_w | Free parameter of the sheet |
| **σ_uw** | Shear (off-diagonal metric entry coupling u and w) | Free parameter of the sheet |
| **(m, n)** | Winding pair of a knot on the sheet | Integer pair |

The (ε, σ_uw) parameterisation is the proton-sheet character at the
metric-charge / metric-binding level; the modulated-clover
construction this project develops works in a different
parameterisation (cross-section harmonic content + R_major +
modulation amplitudes; see [work/derived-clover.md](work/derived-clover.md)).
Earlier proton-sheet (ε, σ_uw) parameter fits from R-studies
(R64 Point A, R64 Point B) are *historical precedents* whose
relationship to the modulated-clover is not currently load-bearing
for the arc; see §What we don't predict for the open reconciliation.

## Ground rules

1. **Inherit from metric-charge and metric-binding.** Closure rule, charge promotion, sheet-character framework are all taken as established. Cite where used; don't re-derive.

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
(see Chapter 9's multi-sheet caveat).

### Theories that have converged

The work files have settled (or are within a single iteration of
settling) on:

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
   the track, under hypothesis G1 (per metric-charge Ch 11 §6). Yields
   Q_proton = +1, Q_neutron = 0 exactly in the symmetric subspace.

4. **Quark substructure.** The (1/2, 1) track passes through three
   arc-pieces in series: lobe-saddle-lobe (proton, uud-ordered) or
   saddle-lobe-saddle (neutron, udd-ordered). A quark is one such
   arc-piece; the constituent-quark mass is m_baryon/3. Under G1
   the per-arc charges are +2/3 (lobe, u) and −1/3 (saddle, d) on
   the piecewise-circular (kissing-circles) idealisation; on the
   smooth Fourier-series cross-section the per-arc readings are
   smeared away from these discrete values while the integer
   baryon charges Q_p = +1, Q_n = 0 are preserved exactly. See
   Chapter 5 for the explicit position the construction takes.

5. **Color identification.** The three Z₃-related phase tracks of
   a single baryon are its three color states. Color is geometric
   (phase index on the substrate), not an internal Hilbert-space
   label.

6. **Mass mechanism.** Path-length: m = 2πℏc/L_track. The mass ratio
   m_n/m_p is matched exactly at ring radius R_major ≈ 36.17. R_major
   remains the one free parameter the framework does not yet derive.

7. **Discrete symmetries.** Z₂ × Z₂ — geometric chirality
   ((m, n) ↔ (m, −n)) × matter/antimatter (C, (m, n) ↔ (−m, −n)).
   Identification with γ⁵-chirality requires a spinor upgrade and is
   deferred.

### Open questions inside the construction's scope

These are gaps the arc *can* close with further work on the
modulated-clover, the per-arc integral, or the LB spectrum.

1. **Closed-form charge integral.** Push M(t₀) = Q(t₀) − ½ to an
   analytical formula in (A, B, φ, a₂, b₂) via Weierstrass
   substitution. Currently we have the first-order expansion and the
   numerical verification at full amplitudes.

2. **R_major as a free parameter.** Is there an independent input
   that pins R_major (e.g., a Compton-scale identification for the
   lightest stable baryon)? Without that, m_n/m_p is calibration, not
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

See [work/](work/) for active explorations. [work/STATUS.md](work/STATUS.md) tracks the current state of each file, its dependencies, and next actions.

## Chapter arc

The arc proceeds from inputs → substrate → modes → charge →
mass-and-quarks → symmetries → limits-and-handoff. Seven chapters,
each backed by settled work files. Topics that the construction
doesn't yet derive (Δ baryons, mesons, magnetic moments, absolute
mass scale, multi-sheet hadrons) are declared as deferred in the
final chapter, not promised as content.

### Framing — one wave-quantum per baryon, with quark substructure along the track

A baryon is one wave-quantum on the modulated-clover. Charges
come from the per-arc curvature integral along the (1/2, 1)
characteristic curve under hypothesis G1 (inherited from
[metric-charge Ch 11](../metric-charge/11-modeling-foundation.md));
mass comes from the closed-track wavelength m = 2πℏc/L. Both
readings of the construction — "wave-on-substrate" (the
cavity, the field that lives on the surface) and
"particle-on-track" (the (1/2, 1) characteristic curve along
which the per-arc curvature is integrated) — describe the
*same single wave-quantum*. They are not two species of object.

The *quark substructure* of a baryon lives inside the per-arc
curvature integral along one track. A closed (1/2, 1) track on
the symmetric modulated-clover passes through the cross-section
in series — alternating convex (lobe) and concave (saddle)
arcs. The proton track at t₀ = −π/6 passes through lobe-saddle-lobe
(uud-ordered); the neutron track at t₀ = +π/6 passes through
saddle-lobe-saddle (udd-ordered). A **quark** is identified with
one arc-piece in this series; the proton's three quark-segments
add to its total charge +1 (under G1), and similarly the
neutron's add to 0.

Per-quark *fractional* charge values depend on the cross-section
representation. On the idealised piecewise-circular kissing-circles
clover (constant geodesic curvature κ = ±1/r on each 240° / 120°
arc), the per-arc reading gives exactly +2/3 (lobe, u) and −1/3
(saddle, d). On the smooth Fourier-series cross-section actually
built by `modulated_clover.py`, the per-arc reading is *smeared*
(~+0.59 per arc for the proton, ~−0.26 per arc for the neutron)
because the continuous-curvature distribution doesn't concentrate
the winding at sharp arc boundaries. The integer baryon charges
Q_p = +1 and Q_n = 0 are exact in both representations — they
come from the topological (1/2, 1) track integral, which is
invariant under the piecewise-circular ↔ smooth-Fourier change of
representation.

Chapter 5 takes this as a *structural prediction* of the framework:
the construction's per-quark fractional charges are not literally
the textbook ±2/3 / ∓1/3 — those values are the kissing-circles
limit. Observables that depend on the discrete fractional values
(e.g. R-ratio analogs, magnetic-moment ratios, parton distribution
shapes) would need to be checked against the smooth-substrate
predictions in future work.

The Z₃ ring-axis screw maps the proton track onto its two
Z₃-related copies (and similarly for the neutron). These three
phase tracks are not three different particles — they are three
*color states* of the same baryon, related by the substrate's
exact Z₃ symmetry. **Color = which of the three Z₃-related phase
tracks the wave-quantum is currently observed on.** The proton
exists in three color states; the observable proton is whichever
color label one chooses to gauge-fix.

Single quantum on the substrate; per-arc charge integral along
its track decomposes into three series quark-segments (uud or
udd); Z₃ ring symmetry gives three colors of each baryon. All
three identifications are geometric.

### The LB result, in context

The framework was at one point trying to identify each baryon
with a *2-D Laplace–Beltrami eigenmode localised on its track*.
Direct computation in [work/lb-mode-localization.md](work/lb-mode-localization.md)
ruled that out: no individual LB eigenmode and no low-energy
superposition is appreciably track-localised on the
modulated-clover at the proton's energy scale (depth < 1 % at
√⟨H⟩ = 2π/L_track).

This does **not** undermine the framing above. The per-arc
charge integral along the (1/2, 1) characteristic curve doesn't
require the wave-quantum to be spatially concentrated on the
curve — it is a Berry-phase-style integral whose value is
determined by how the cross-section tangent winds, not by where
the wave's amplitude sits. The LB result tells us that the
wave-quantum's *amplitude* is spread over the whole substrate
(as the LB ground-state would be), while the *charge content*
is still organised in series along the characteristic curve.
The proton is one quantum whose probability density is global
and whose charge structure is along-the-track.

That said, the LB result *does* close one open question (could
the proton be derived as a track-localised mode? no) and leaves
one open question (which LB eigenmode, if any, is the proton?).
Chapter 5 carries this result as a finding rather than as a gap
to be closed.

| # | Title | Role |
|---|---|---|
| 1 | **Foundation** | Inputs from [metric-charge](../metric-charge/) (picture A, the wave-equation framework, the per-arc charge bridge under G1); coordinates and conventions; the central question this project answers ("what specific 2D substrate hosts the u-d hadron generation?"); the framing — one wave-quantum per baryon, with quark substructure organised in series along its characteristic curve. |
| 2 | **The modulated-clover substrate** | The harmonic N = 3 cross-section family (3 major + 3 minor lobes, six equal pieces). Closure of the surface: allowed twists are multiples of 1/6; the **half-twist** τ = 1/2 is the operative case. Modulation a₁(θ), b₁(θ) restricted to the Z₂ × Z₃-symmetric subspace. The substrate is set up as a *resonator* (the cavity language), not a particle space. |
| 3 | **Modes and their characteristic curves** | The wave-quantum's characteristic curve — the (1/2, 1) torus knot on the modulated-clover, closing under the half-twist identification. The two distinct curves at t₀ = ∓π/6 — proton and neutron. The Z₂ × Z₃ orbit gives 6 baryon replicas: 3 color phases of the proton and 3 of the neutron. The characteristic curve is where the per-arc charge integral is taken, not where the wave-quantum's amplitude is concentrated (see Ch 5). |
| 4 | **Charge from per-arc curvature** | The per-arc reading of charge along the characteristic curve, under G1 (inherited). The clean identity Q(t₀) = ½ + M(t₀). Solving the symmetric modulation for M(±π/6) = ±½. Result: Q_proton = +1, Q_neutron = 0 exactly. The **series structure** of convex (lobe) and concave (saddle) contributions along one track is the input to Chapter 5's quark decomposition. The discrete per-arc values (+2/3 / −1/3) belong to the piecewise-circular idealisation; Chapter 5 reports what the smooth Fourier substrate actually produces. |
| 5 | **Mass and quark substructure** | The path-length mass m = 2πℏc/L_track on the (1/2, 1) tracks. The closed track passes through **three arc-pieces in series**: lobe-saddle-lobe = uud-ordered (proton) and saddle-lobe-saddle = udd-ordered (neutron). Each arc-piece is one constituent quark; constituent-quark mass = m_baryon / 3 ≈ 313 MeV. Color = which of the three Z₃-related phase tracks. Per-quark fractional charges: ±2/3 / ∓1/3 on the piecewise-circular idealisation; smeared (~+0.59 / −0.26) on the smooth Fourier construction the scripts use — chapter states this as a structural prediction rather than a fit failure (see [work/quark-decomposition.md](work/quark-decomposition.md), [work/quark-wannier-decomposition.md](work/quark-wannier-decomposition.md)). Integer baryon charges are exact in both representations. Direct LB-localisation computation ([work/lb-mode-localization.md](work/lb-mode-localization.md)) reported as a finding: the wave-quantum is *not* spatially track-localised, but the per-arc charge integral does not require it to be. Mass-ratio match m_n/m_p = L_p/L_n at R_major ≈ 36.17. R_major's status as the one undetermined free parameter. |
| 6 | **Symmetries — chirality, isospin, color, C** | The Z₂ × Z₂ structure on baryon modes: chirality ((m, n) ↔ (m, −n)) and matter/antimatter ((m, n) ↔ (−m, −n)). The Z₃ ring-axis rotation = color. The Z₂ proton/neutron swap = isospin I_3 = ±½. Geometric chirality (the framework's only handedness at the scalar-field level) vs γ⁵-chirality (requires the deferred spinor upgrade). Baryon number = track winding count. |
| 7 | **Limits, handoff, and closing summary** | What the construction *establishes* under named hypotheses (charge, mass ratio, quark substructure, color, chirality, baryon number). What it *does not predict* (see the §What we don't predict section above). The single-generation scope: heavier-quark generations live elsewhere; multi-sheet hadrons (Λ, Σ, Ξ, Ω) need a coupling mechanism in [metric-binding](../metric-binding/) and/or [ma-domain](../ma-domain/). The handoff to ma-domain: τ = 1/2 modulated-clover is sheet-proton's settled geometry; ma-domain's multi-generation architecture is free to adapt to it rather than the τ = 1/3 clover-quarks precedent. Parallel in role to [metric-charge Ch 10](../metric-charge/10-closing-summary.md). |

Possible appendix (if useful):

- **A. Closed-form analytical machinery.** The Weierstrass-substitution evaluation of M(t₀), the parameter-family structure of the charge-correct symmetric modulation, the analytical form of the track-length integral. Parallel to [metric-charge Ch 11](../metric-charge/11-modeling-foundation.md).
