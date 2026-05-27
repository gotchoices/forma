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

Additional notation specific to the proton sheet:

- **R64 Point A:** ε = 0.073, σ_uw = 0.194 (fits deuteron + p/n mass ratio)
- **R64 Point B:** ε = 0.2052, σ_uw = 0.025 (fits Ca→Sn nuclear binding curve)
- The two points are mutually exclusive; resolution is one of the project's central open questions.

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

4. **Quark substructure.** The per-arc integral along one track
   decomposes into three series segments — convex (lobe) arcs at
   +2/3, concave (saddle) arcs at −1/3 under G1 — yielding the
   uud series (proton, +1) and udd series (neutron, 0). A quark
   is one such segment; the constituent-quark mass is m_baryon/3.

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

### Open questions for the formal derivation

1. **Closed-form charge integral.** Push M(t₀) = Q(t₀) − ½ to an
   analytical formula in (A, B, φ, a₂, b₂) via Weierstrass
   substitution. Currently we have the first-order expansion and the
   numerical verification at full amplitudes.

2. **R_major as a free parameter.** Is there an independent input
   that pins R_major (e.g., a Compton-scale identification for the
   lightest stable baryon)? Without that, m_n/m_p is calibration, not
   prediction.

3. **Beyond p and n.** Extending the construction to Δ⁺⁺, Δ⁺, Δ⁰,
   Δ⁻ (spin-3/2 baryons) and to the light mesons (π, η, ρ, ω). Mode
   tower / higher harmonics? Compound modes? Work files cover framing
   but not detailed derivation. See Chapter 7 below.

4. **Multi-sheet hadrons** (Λ, Σ, Ξ, Ω with strange quarks): require
   a coupling between sheets of different generations. Deferred to
   metric-binding; the proton-sheet construction must remain
   compatible with whatever multi-sheet mechanism is adopted there.

5. **Spinor upgrade.** Currently the framework carries a scalar
   field on the substrate. A spinor upgrade is needed to identify
   geometric chirality with Dirac γ⁵, and may also be needed for
   a future generalisation of the baryon mode beyond the
   single-quantum reading. Forward-looking.

## Background reading

- [metric-binding/](../metric-binding/) — general multi-knot binding framework, sibling project; sheet-proton is the specific application to the proton sheet
- [metric-charge/](../metric-charge/) — single-knot framework on a 2D sheet; closure conditions and sheet character
- [metric-mass/](../metric-mass/) — single-compact-dimension precursor; standing-wave reading
- [grid-duality/](../grid-duality/) — substrate-level framework; α-coupling
- [studies/R64-nuclear-harmonic-stack/](../../studies/R64-nuclear-harmonic-stack/) — current proton-sheet parameter fits (Point A, Point B); harmonic-stack reading
- [studies/R63-proton-tuning/](../../studies/R63-proton-tuning/) — proton/neutron pair tuning, complementary nodes
- [studies/R53-three-generations/](../../studies/R53-three-generations/) — three-generation structure; quark flavor identification
- [studies/R54-compound-modes/](../../studies/R54-compound-modes/) — cross-sheet compound modes (model-E alternative)

## Work files

See [work/](work/) for active explorations. [work/STATUS.md](work/STATUS.md) tracks the current state of each file, its dependencies, and next actions.

## Chapter arc

The arc proceeds from inputs → substrate → modes → charge → mass →
symmetries → spectrum extension → observables → handoff. Chapters
1–6 are the core derivation; chapters 7–9 are exploratory and will
be sketchier on first draft, iterating with the work files. Chapter
10 is the closing summary, parallel to metric-charge Ch 10.

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
arcs. Under G1 each convex arc contributes a +2/3 fractional
charge unit and each concave arc a −1/3 unit; the series sums
to +1 for the proton track (uud) and 0 for the neutron track
(udd). A **quark** is identified with one segment of this
series; the proton's three quark-segments add to its total
charge, and similarly for the neutron.

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
| 4 | **Charge from per-arc curvature** | The per-arc reading of charge along the characteristic curve, under G1 (inherited). The clean identity Q(t₀) = ½ + M(t₀). Solving the symmetric modulation for M(±π/6) = ±½. Result: Q_proton = +1, Q_neutron = 0 exactly. Convex (lobe) arcs contribute +2/3, concave (saddle) arcs −1/3 to the integral; the **series structure** of these contributions along one track is the input to Chapter 5's quark decomposition. |
| 5 | **Mass and quark substructure** | The path-length mass m = 2πℏc/L_track on the (1/2, 1) tracks. The per-arc curvature integral along a single track decomposes into **three quark-segments in series**, summing to +1 (uud) for the proton track and 0 (udd) for the neutron. Each constituent-quark mass = m_baryon / 3 ≈ 313 MeV. Color = which of the three Z₃-related phase tracks. Direct LB-localisation computation ([work/lb-mode-localization.md](work/lb-mode-localization.md)) reported as a finding: the wave-quantum is *not* spatially track-localised, but the charge integral does not require it to be. Mass-ratio match m_n/m_p = L_p/L_n at R_major ≈ 36.17. R_major's status as the one undetermined free parameter. |
| 6 | **Symmetries — chirality, isospin, color, C** | The Z₂ × Z₂ structure on baryon modes: chirality ((m, n) ↔ (m, −n)) and matter/antimatter ((m, n) ↔ (−m, −n)). The Z₃ ring-axis rotation = color. The Z₂ proton/neutron swap = isospin I_3 = ±½. Geometric chirality vs. γ⁵-chirality (deferred to spinor-upgrade). |
| 7 | **Beyond proton and neutron — frontier** | Extending the construction to the rest of the u-d hadron spectrum: Δ⁺⁺/Δ⁺/Δ⁰/Δ⁻ (spin-3/2 baryons; candidates: higher mode excitations or different track topologies), and the light mesons π/ρ/η (compound qq̄ readings). Exploratory first-draft, iterating with [work/meson-spectrum.md](work/meson-spectrum.md), [work/clover-mass.md](work/clover-mass.md), [work/strong.md](work/strong.md). |
| 8 | **Observables** | Computed observables from the construction: magnetic moments (from the wave's current distribution), parity (from substrate enantiomers), baryon number (from track-winding count). Comparison with measured values where possible. Where the construction is silent or makes only qualitative predictions, flag clearly. |
| 9 | **Limits and handoff** | What's *not* on this sheet: heavier-quark generations (deferred to other sheets / [metric-binding](../metric-binding/)); leptons (deferred to separate substrates). Multi-sheet hadrons (Λ, Σ, Ξ, Ω) require a coupling mechanism that lives in metric-binding; this chapter states the interface and the constraints the proton-sheet construction places on whatever multi-sheet mechanism is eventually adopted. |
| 10 | **Closing summary** | What the project established under named hypotheses; what remains open; how the construction's claims map onto the framework's broader structure. Parallel to [metric-charge Ch 10](../metric-charge/10-closing-summary.md). |

Possible appendix (if useful):

- **A. Closed-form analytical machinery.** The Weierstrass-substitution evaluation of M(t₀), the parameter-family structure of the charge-correct symmetric modulation, the analytical form of the track-length integral. Parallel to [metric-charge Ch 11](../metric-charge/11-modeling-foundation.md).
