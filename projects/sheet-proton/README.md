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

4. **Mass mechanism.** Path-length: m = 2πℏc/L_track. The mass ratio
   m_n/m_p is matched exactly at ring radius R_major ≈ 36.17. R_major
   remains the one free parameter the framework does not yet derive.

5. **Discrete symmetries.** Z₂ × Z₂ — geometric chirality
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
   field on the substrate. The same upgrade addresses two
   downstream needs: (a) identifying geometric chirality with
   Dirac γ⁵; (b) supplying the fermionic Pauli structure that
   underlies Reading β (three quark-quanta, one per phase track),
   which the LB-localisation computation
   ([work/lb-mode-localization.md](work/lb-mode-localization.md))
   makes the natural single-quantum account. Forward-looking,
   but identifying these two needs as one structural step is
   itself a finding of the present iteration.

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

### Framing — two readings, and what the computation says about them

Throughout the arc we work in two languages:

- **Wave-on-substrate (cavity).** The substrate is a 2-D resonator
  (a closed Riemannian surface). Particles are eigenmodes of the
  Laplace–Beltrami operator on it. Charges come from the Noether
  current; masses come from LB eigenvalues. This is the framing
  inherited from [metric-charge Ch 11 picture A](../metric-charge/11-modeling-foundation.md).
- **Particle-on-track (semi-classical).** A particle's wavefunction
  is assumed to localise to a **characteristic curve** — for our
  construction the (1/2, 1) torus knots on the modulated-clover.
  Charge along that curve is the per-arc curvature integral (under
  G1); mass is the closed-loop wavelength 2πℏc/L. This is the
  framing the modulated-clover work files have used to actually
  pin charges and the mass ratio.

The framework had taken these to be **two languages for the same
physics**, with the particle-on-track picture as the
semi-classical projection of the wave picture. Direct computation
(see the next subsection) shows that this equivalence does **not
hold on the modulated-clover surface at the proton's energy
scale.** The chapter arc treats the particle-on-track calibration
as the empirically working description, and the wave-on-substrate
reading as a structural target the framework will reach only
under a spinor upgrade (Reading β).

### A known reconciliation gap — status updated by direct computation

The framework had assumed that the proton/neutron correspond
to track-localised modes of the 2D Laplace–Beltrami operator on
the modulated-clover. The direct computation in
[work/lb-mode-localization.md](work/lb-mode-localization.md)
returns a **negative answer** to that assumption on this surface:

- No individual LB eigenmode (up to √λ ≈ 1.5) is appreciably
  track-localised — the modes are stripes spanning (t, θ)
  parameter space, with enrichment never exceeding ~7 % of
  perfect track confinement.
- Even allowing arbitrary low-energy *superpositions* of LB
  modes, the best achievable localisation at the proton's energy
  (√⟨H⟩ = 2π/L_track ≈ 0.028 in script units) has depth < 1 %.
  Modest localisation (≳ 5 %) costs ≈ 3 × the proton's energy;
  substantial localisation (≳ 30 %) costs ≈ 30 × the proton's
  energy. The trade-off has the expected Heisenberg shape, and
  the cost on this substrate is far higher than the proton can
  pay.

So the two readings — *wave-on-substrate* (2-D LB) and
*particle-on-track* (path-length) — do **not** agree on this
surface at the proton's energy scale. The particle-on-track
calibration is empirically correct (charge +1/0, mass ratio).
The wave-on-substrate reading is not reachable from it by a
semi-classical limit on this surface.

**No reconciliation is currently in hand.** Reading β
(introduced below) is a *reinterpretation* that sidesteps the
gap rather than a derivation of equivalence — it gives up on
"one wave-quantum localised on the proton's three tracks" and
replaces it with "three wave-quanta, one per track, held in
distinct states by Pauli exclusion under a fermionic spinor
upgrade." That keeps the framework operating in the
wave-on-substrate picture, but each track-quantum now carries
the *constituent-quark* mass (~313 MeV), not the proton mass,
and R_major rescales by ~3×. So Reading β does not equate the
two readings; it makes Reading α unnecessary at the cost of
re-calibrating the construction.

Routes that have *not* been tried and could in principle still
close the gap: (a) high-eigenvalue scarring on closed geodesics
(√λ ≫ 1 — does not help the proton specifically but matters for
heavier baryons); (b) a *restricted* Laplacian on a specific
Z₃ irrep, where the proton might appear as the ground state of
a constrained operator rather than the full LB; (c) Husimi /
phase-space localisation rather than position-space; (d) a
different metric on the same substrate with sharper "tubes"
around each track. None of these has been worked out.

The chapter arc therefore: *reports* the negative LB result as
a finding, *adopts* the particle-on-track calibration with its
assumptions made explicit, *records* Reading β as the working
sidestep, and *flags* the remaining mathematical routes as open
work.

Two further gaps remain open and are carried in Chapter 5 with
their status:

1. **Semi-classical localisation not derived** (now known not to
   exist on this surface for the proton — the framework has to
   work without it).
2. **Color-singlet structure is informal.** The three Z₃-related
   phase tracks are *interpreted* as three color states whose
   singlet combination is the observable proton, but the framework
   does not derive the antisymmetric singlet structure or any
   binding-into-singlet mechanism.

### A second reading we keep on the table

The multi-geodesic case (3 Z₃-related phase tracks per baryon)
naturally admits **two distinct readings** that the framework's
current scalar-field structure does not pick between:

- **Reading α — single quantum in three-mode superposition.** One
  proton-quantum has support on all three phase tracks; energy
  ⟨H⟩ = E (the single-mode energy by Z₃ degeneracy); mass = m_baryon;
  R_major ≈ 36.17. This is what a bosonic field naturally gives,
  and it's the reading our current construction has been calibrated
  to.
- **Reading β — three quanta, one per color mode.** Three
  quark-quanta, each on its own phase track. Total mass 3E with
  E = m_constituent_quark ≈ 313 MeV; track lengths and R_major
  ~3× larger (~108). This is the QCD-natural reading
  (Pauli-exclusion-forced 3-quark structure), and is the natural
  outcome of a **fermionic spinor upgrade** of the field — the
  same upgrade that γ⁵ chirality would require. The two open
  questions (multi-quantum baryon, γ⁵ chirality) are aspects of
  one structural extension.

Reading α is what the construction has been calibrated *to*.
Reading β was kept on the table in case the Chapter-5 wave/track
reconciliation proved unreachable. The direct LB-localisation
computation (above) has shown that it is unreachable on this
surface at the proton's energy scale, which moves Reading β
from "alternative kept open" to **the natural single-quantum
account for the framework going forward**. The chapter arc should
treat α as the current particle-on-track calibration (the work
files have used it; the construction reproduces the right
numbers under it) and β as the wave-on-substrate-level reading
the framework will need once the spinor upgrade is in place —
with the connecting observation that **the same spinor upgrade
addresses both Reading β and γ⁵ chirality**.

| # | Title | Role |
|---|---|---|
| 1 | **Foundation** | Inputs from [metric-charge](../metric-charge/) (picture A, the wave-equation framework, the per-arc charge bridge under G1); coordinates and conventions; the central question this project answers ("what specific 2D substrate hosts the u-d hadron generation?"); the **dual framing** (wave-on-substrate as fundamental, particle-on-track as calculational tool) and its open reconciliation gap. |
| 2 | **The modulated-clover substrate** | The harmonic N = 3 cross-section family (3 major + 3 minor lobes, six equal pieces). Closure of the surface: allowed twists are multiples of 1/6; the **half-twist** τ = 1/2 is the operative case. Modulation a₁(θ), b₁(θ) restricted to the Z₂ × Z₃-symmetric subspace. The substrate is set up as a *resonator* (the cavity language), not a particle space. |
| 3 | **Modes and their characteristic curves** | Eigenmodes of the substrate's Laplace–Beltrami operator; the (1/2, 1) torus knots as the *characteristic curves* of localised modes; closure under the half-twist identification. The two distinct tracks at t₀ = ∓π/6 — proton and neutron. The Z₂ × Z₃ orbit gives 6 baryon replicas (3 color phases × 2 isospin states). |
| 4 | **Charge from per-arc curvature** | The per-arc reading of charge along a mode's characteristic curve, under G1 (inherited). The clean identity Q(t₀) = ½ + M(t₀). Solving the symmetric modulation for M(±π/6) = ±½. Result: Q_proton = +1, Q_neutron = 0 exactly. Per-piece (per-quark) charges as the idealised labelling the smooth construction approximates. |
| 5 | **Mass and the wave/track reconciliation** | The path-length mass m = 2πℏc/L_track on the (1/2, 1) tracks. Direct LB-localisation computation (per [work/lb-mode-localization.md](work/lb-mode-localization.md)): the 2-D LB picture does *not* localise on the tracks at the proton's energy scale. Consequence: the framework adopts the particle-on-track calibration with its assumptions made explicit, and Reading β (multi-quantum, fermionic) becomes the natural wave-on-substrate account once the spinor upgrade is in place. The mass-ratio match m_n/m_p = L_p/L_n at R_major ≈ 36.17 under the path-length reading. R_major's status as the one undetermined free parameter. **This is the honesty chapter — the framework's central interpretive commitment lives here.** |
| 6 | **Symmetries — chirality, isospin, color, C** | The Z₂ × Z₂ structure on baryon modes: chirality ((m, n) ↔ (m, −n)) and matter/antimatter ((m, n) ↔ (−m, −n)). The Z₃ ring-axis rotation = color. The Z₂ proton/neutron swap = isospin I_3 = ±½. Geometric chirality vs. γ⁵-chirality (deferred to spinor-upgrade). |
| 7 | **Beyond proton and neutron — frontier** | Extending the construction to the rest of the u-d hadron spectrum: Δ⁺⁺/Δ⁺/Δ⁰/Δ⁻ (spin-3/2 baryons; candidates: higher mode excitations or different track topologies), and the light mesons π/ρ/η (compound qq̄ readings). Exploratory first-draft, iterating with [work/meson-spectrum.md](work/meson-spectrum.md), [work/clover-mass.md](work/clover-mass.md), [work/strong.md](work/strong.md). |
| 8 | **Observables** | Computed observables from the construction: magnetic moments (from the wave's current distribution), parity (from substrate enantiomers), baryon number (from track-winding count). Comparison with measured values where possible. Where the construction is silent or makes only qualitative predictions, flag clearly. |
| 9 | **Limits and handoff** | What's *not* on this sheet: heavier-quark generations (deferred to other sheets / [metric-binding](../metric-binding/)); leptons (deferred to separate substrates). Multi-sheet hadrons (Λ, Σ, Ξ, Ω) require a coupling mechanism that lives in metric-binding; this chapter states the interface and the constraints the proton-sheet construction places on whatever multi-sheet mechanism is eventually adopted. |
| 10 | **Closing summary** | What the project established under named hypotheses; what remains open; how the construction's claims map onto the framework's broader structure. Parallel to [metric-charge Ch 10](../metric-charge/10-closing-summary.md). |

Possible appendix (if useful):

- **A. Closed-form analytical machinery.** The Weierstrass-substitution evaluation of M(t₀), the parameter-family structure of the charge-correct symmetric modulation, the analytical form of the track-length integral. Parallel to [metric-charge Ch 11](../metric-charge/11-modeling-foundation.md).
