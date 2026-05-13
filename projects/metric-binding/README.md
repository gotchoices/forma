# metric-binding

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** Multi-knot interactions on a 2D compact sheet — energy at separation, force laws, bound-state regimes. Single-knot charge generation is covered in [metric-charge](../metric-charge/).
**Method:** Mathematical derivation as discovery; minimal computation.
**Status:** Framing complete. Awaiting first chapter.

## Why this project exists

[metric-charge](../metric-charge/) established how a single knot on a 2D compact sheet can promote mass to charge via the closure condition, and how varying ε and σ_uw sorts the admissible knot family into qualitatively different particle classes. This project picks up the next question: when two such knots inhabit the same sheet, what does their interaction look like?

The naive next step would be to import standard EM and ask how two charged objects interact via Coulomb's law. We don't take that step. The geometry of the sheet should *produce* the force law, not have it imposed. The interesting payoff is whether a single sheet's geometry can host more than one regime — Coulomb-like at large separation, confining at short range, harmonic stacks in Ma — without putting any of them in by hand.

The central question:

> *Given two knots on the same 2D compact sheet, what does the energy of the configuration depend on, and what regimes (bound, partially separated, free) does the math support?*

### Underlying targets

The framework should illuminate, without explicitly hunting for any of them:

- **A force law from geometry.** Two knots at separation r have an interaction energy. What does the curve E(r) look like? Where does it look Coulomb-like, where does it look confining?
- **Bound vs. free, partial vs. complete separation.** Identify the regimes where the configuration's ground state has the knots stacked in Ma, partially separated in S, or fully separated. Where does each regime apply in parameter space?
- **A candidate strong-force mechanism.** If the same sheet's geometry produces both a long-range 1/r-like behavior *and* a short-range confinement, the strong force is a structural prediction of the framework, not an additional ingredient that has to be postulated.
- **Pair behavior at zero separation.** When two opposite-handedness knots collide, do they pass through (linear superposition), annihilate (mass-energy released), or refuse to overlap (configuration forbidden)? This is the multi-knot version of the pass-through question metric-mass Chapter 4 raised in 1D.

The framework is not on the hunt for nuclear binding specifically. The strong-force-like regime is one of the things the math should reveal *if* it's there.

## Coordinates and notation

Same coordinate set as [metric-charge](../metric-charge/), now with both spatial dimensions actively in play:

| Symbol | Role | Type |
|---|---|---|
| **t** | Time | Extended, real |
| **S₁** | First spatial extension | Extended, real (rendered along x) |
| **S₂** | Second spatial extension | Extended, real (rendered along y) |
| **u** | First compact coordinate on the 2D sheet | Compact: u ~ u + L_u |
| **w** | Second compact coordinate on the 2D sheet | Compact: w ~ w + L_w |

- **Aspect ratio:** ε ≡ L_u / L_w. Inherited from metric-charge.
- **Shear:** σ_uw inherited from metric-charge.
- **Separation:** **r** = √((ΔS₁)² + (ΔS₂)²) is the spatial separation between two knots in S. The energy E(r) of a two-knot configuration is the central object of study.

For full notation conventions including the visualization disposition, see [metric-charge §Coordinates and notation](../metric-charge/README.md#coordinates-and-notation).

**Why S₂ matters here** (whereas it was carried as forward-looking infrastructure in metric-charge): with both spatial dimensions, two knots can sit at different (S₁, S₂) positions and we can compute energies and forces *as functions of r*. The classification of bound vs. free states, the emergence of a force law, and the confinement question all live on this two-dimensional spatial substrate.

## Ground rules

1. **Inherit from metric-charge.** The 2D sheet, closure condition, knot family, charge promotion, and sheet-character results from metric-charge are all taken as established. We don't re-derive them. Cite where needed.

2. **Discovery, not proof.** Same rule as metric-mass and metric-charge — let the math reveal results rather than confirming them.

3. **Force laws emerge from energy.** Don't import Coulomb or any other force law. Compute E(r) from the field configuration, and read off the force from −dE/dr. Whatever the answer is — Coulomb, confining, oscillatory, none of the above — is what the framework predicts.

4. **One topic per chapter.** Bundling defeats the discovery arc.

5. **Variables stay symbolic.** Don't pin numerical values until the algebra forces it.

6. **Computation only when forced.** Paper math first; scripts only when the algebra becomes intractable or visualization is the only way to see the geometry.

## Goals

### Theories to test

1. **Multi-knot superposition at zero separation.** Two knots on the same sheet at the same (S₁, S₂):
   - same handedness, same closure pattern → stack as a harmonic in Ma (or fail to stack)
   - opposite handedness → may cancel in w (neutral pair), pass through, or annihilate
   - shear-aligned complementary modes → proton/neutron-style splitting
   
   The math should classify which of these outcomes the sheet's geometry actually permits.

2. **Pass-through vs. annihilation.** The linear-superposition pass-through result of metric-mass Chapter 4 was a 1D-compact, single-knot result. When two distinct knots on a 2D sheet meet, do they pass through, annihilate, or refuse to overlap? This is the question that distinguishes "two real knots" from "a single field with both handednesses."

3. **Energy at finite separation.** The energy E(r) of a two-knot configuration as a function of spatial separation r is the central technical object. Compute it for representative closure types, handedness combinations, and aspect ratios.

4. **Bound-state regimen (the strong-force candidate).** From the shape of E(r), identify regimes:
   - **Stack in Ma** — two similar knots fit together as a higher harmonic of the same compact pattern. Ground state has zero separation.
   - **Stack but not separable in S** — opposite-handedness knots that lock in Ma without flying apart in S. Candidate confined-pair state.
   - **Partial S-separation, bound** — knots separated in (S₁, S₂) but unable to escape to infinity. Coulomb-bound or strong-force-bound.
   - **Free** — knots fully separated, energy-unbound.
   
   The promise: a geometric prediction of when each regime is the ground state, including a candidate strong-force mechanism without postulating one.

5. **Force-law transitions.** As parameters (ε, σ_uw, knot quantum numbers) vary, where in parameter space does the force law transition from Coulomb-like to confining? Is the transition smooth, or does it correspond to a structural change in the knot configuration?

6. **Asymptotic behaviors.** What does E(r) do at large r (far separation)? At small r (near coincidence)? At specific resonant separations? The asymptotic structure should constrain what physical force laws the geometry can support.

7. **Mixed-orientation compounds as candidate baryons.** Metric-charge's [work-L5](../metric-charge/work-L5.md) records that the framework's mode-language admits compound configurations on a single sheet with non-uniform per-component orientations — for instance, 2 × T(+1, n') + 1 × T(−1, n') with per-component charges (+1, +1, −1) and external integer charge +1 (the proton's external charge by tube-winding sum). The structural existence of such compounds is in metric-charge's scope; **whether any such compound is stable, what binds it, and which compound (if any) realizes the observed proton are downstream questions native to this project.** Open structural questions feeding in:
   - **Why a 2:1 mix and not 3:0 or other ratios?** The uniform 3 × T(+1, n') compound has external charge +3 (or, per Configuration Y, internally distributed as +1/3 per component summing to +1 in scaled units). The 2:1 mix gives external +1 with non-uniform per-component sign. Which is the ground state for a given sheet's (ε, σ_uw)? Is there a binding-energetics reason for one mix to be favored?
   - **What forces three primitives to bind as one object?** Three independent primitives on the same sheet are not automatically bound. The binding mechanism — inter-component interaction, confinement-like potential, or substrate-level constraint — is the central thing to derive.
   - **The neutron analog.** Among 3-component compounds of T(±1, n') primitives on a single sheet, the available external integer charges by tube-winding sum are {−3, −1, +1, +3}. Charge 0 is *not* among them. A neutral 3-component baryon would require either a different mode-content (e.g., zero net tube winding from non-(±1, n') primitives, or cross-sheet structure per R54), or a different reading of the baryon composition altogether. This is a structural puzzle worth taking up here.
   - **Fractional vs integer per-component charge.** The compound-inventory picture has each primitive carrying integer charge ±1 in framework units. Standard-model quarks have fractional charges (±2/3, ±1/3). Is the framework's primitive charge units-different from the SM charge, or does the binding mechanism redistribute charge non-uniformly among components, or is the SM fractional reading itself a binding-state artifact (deep-inelastic averaging, anomalous moment)? Open downstream question.
   - **Mass approximation to single-mode T(1, 3n').** At small ε, the 3-component compound's mass approximates that of a single Bloch mode at the summed windings (1, 3n'). Is this near-degeneracy structural, or coincidental? Could the compound be the *substructure* of an apparently-single mode at large mass? Relevant to proton internal-structure questions.
   
   See also the alternative R-track empirical reading ([R53](../../studies/R53-three-generations/), [R54](../../studies/R54-compound-modes/), [R63](../../studies/R63-proton-tuning/)) in which each quark is its own (m, n) mode rather than a component of a single-sheet compound — a different structural picture that this project's binding analysis should engage with or choose between.

### Open questions

To answer or sharpen along the way:

1. **Predicting harmonics-in-Ma vs. separation-in-S.** Develop a regimen for predicting, in advance from (ε, σ, knot quantum numbers), whether two knots will stack in Ma (zero spatial separation) or split into two spatially separated objects in S.

2. **What does S₂ actually buy?** Be explicit about which results require the second spatial dimension and which would already work in S₁ alone. (We expect anisotropic effects from a non-rotationally-symmetric two-knot configuration in S to force S₂'s involvement.)

3. **What carries momentum through S when a knot moves?** Rigid translation, internal deformation, or precession? Relevant for the dynamical question of whether bound states orbit, oscillate, or sit static.

4. **Is the linear-superposition pass-through of metric-mass Chapter 4 still valid here?** That was a 1D-compact, single-mode result. Multi-knot on a 2D sheet may behave differently — particularly when handedness or closure patterns differ between the two knots.

5. **Does the strong-force-like regime predict confinement in the QCD sense?** If we find a regime where E(r) → ∞ as r → ∞, that's confinement. If we find a regime where the knots can't separate beyond some r_max, that's a different (but related) confinement. Distinguish the two and identify which the geometry actually produces.

6. **What sets the energy scale of the bound states?** The Compton wavelength of the constituent knots is the obvious scale, but the binding energy might be set by something else (e.g., overlap integrals depending on aspect ratio).

## Background reading

- [metric-charge/](../metric-charge/) — the immediate predecessor; closure condition, charge from geometry, sheet character (single-knot)
- [metric-charge/work-L5.md](../metric-charge/work-L5.md) — fractional-charge sign-tracing audit + mixed-orientation compound inventory; hands off the H3b stability and identification questions (proton/neutron candidate compounds) to this project
- [metric-mass/](../metric-mass/) — the grand-predecessor; mass-from-u, ±n superposition pass-through (Chapter 4)
- [studies/R64-nuclear-harmonic-stack/](../../studies/R64-nuclear-harmonic-stack/) — multi-knot harmonics on the p-sheet, nuclear binding context
- [studies/R63-proton-tuning/](../../studies/R63-proton-tuning/) — proton/neutron pair structure, complementary nodes
- [studies/R53-three-generations/](../../studies/R53-three-generations/) — empirical mode-by-mode quark identification; alternative reading to the mixed-orientation compound picture (R-track's two-shear puzzle is the live downstream issue)
- [studies/R54-compound-modes/](../../studies/R54-compound-modes/) — cross-sheet couplings as candidate resolution mechanism
- [grid/](../../grid/) — α-coupling derivation (taken as input)

## Chapters

The arc below is a *sketch*. Early chapters are framed in detail; later chapters are framed as questions to examine. The project may redirect when a chapter's math reveals something unexpected.

1. **`01-foundation.md`** — What metric-binding inherits from metric-charge. Brief recap of the 2D sheet, closure condition, knot family, and charge promotion. State the multi-knot setup, the energy quantities to be computed, the methods (configuration-space integrals, separation-dependent overlap), and what is taken as given vs. derived.

2. **`02-multi-knot-at-zero-separation.md`** — Two knots at the same (S₁, S₂). Tackle the algebraic baseline before introducing separation:
   - When do two knots stack as a higher harmonic in Ma?
   - When do they cancel or refuse to coexist?
   - Pass-through vs. annihilation for opposite-handedness collisions.
   - Phase-offset configurations: two distinct (m, n) modes at the same position with arbitrary phase relationships on the torus — when does the combined configuration relax to one component, when does it stabilize as a coexistence?
   
   Establishes the zero-separation limit that chapter 3's E(r) must approach as r → 0.

### Tentative downstream arc

The chapters below are plausible follow-ups, not commitments.

3. **`03-energy-at-finite-separation.md`** — Two knots at different (S₁, S₂). Compute E(r) — the configuration energy as a function of spatial separation — for representative closure types and handedness combinations. The technical core: separation-dependent overlap integrals on the 2D sheet, evaluated for several (ε, σ) regimes. Identify the qualitative shape (decay, growth, oscillation, plateau).

4. **`04-regime-classification.md`** — From E(r), classify the regimes: stack-in-Ma, stack-but-bound, partial-separation-bound, free. Map each regime onto a region of parameter space (ε, σ, closure type, handedness). Identify the boundaries and what happens at them.

5. **`05-force-laws-and-confinement.md`** — From the E(r) shape, derive force vs. separation behavior. Identify Coulomb-like 1/r regimes, confinement-like regimes, and how the geometry produces both. Frame the strong-force candidate explicitly: a confinement-like regime that emerges from sheet geometry alone. Examine whether the confinement is "knots can't separate at all" or "knots can separate up to r_max."

6. **`06-closing-summary.md`** — Consolidate what the project established, ruled out, and unexpectedly found. Open questions made legible. Hand off to follow-up projects (multi-sheet structure, dynamics of bound knots, full nuclear binding).

Each chapter is added one at a time. The arc is a sketch, not a contract.
