# sheet-proton

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** Detailed exploration of what the proton sheet might uniquely look like — geometry, internal structure, quark content, mediator physics, strong-force mechanism. The proton-specific complement to [metric-binding](../metric-binding/), which addresses general multi-knot binding on a generic sheet.
**Method:** Mathematical derivation as discovery; geometric construction; minimal computation. Work-file-driven (see [work/](work/)), with chapter-level prose emerging only after work files converge on stable conclusions.
**Status:** Active. Initial work files drafted; first computational results pending.

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

### Theories to test

The work files each test specific theories about the proton sheet:

1. **Quark-flavor mapping.** Which (m, n) primitive on the proton sheet is the up quark? The down quark? Empirical fit pins R64's (1, ±2); alternative mappings exist. See [work/quark-flavor.md](work/quark-flavor.md).

2. **Strong-force mechanism.** Does the strong force emerge as Yukawa exchange via a wave mediator on the proton sheet, with the mediator's Compton wavelength setting the force range? See [work/strong.md](work/strong.md).

3. **Light-meson spectrum.** Are mesons 2-component qq̄ compounds on the proton sheet? Does the framework's dispersion give the right meson masses (π, K, η, ρ, ω, φ)? See [work/meson-spectrum.md](work/meson-spectrum.md).

4. **Sheet geometry — corrugation.** Is the proton sheet flat (as metric-charge assumed) or corrugated (3-lobe profile with 120° twist)? Does corrugation provide a natural geometric realization of Z₃ confinement, fractional charges, and the up/down quark distinction? See [work/clover-quarks.md](work/clover-quarks.md).

### Open questions

1. **The R64 two-point fit (Point A vs Point B).** Which (ε, σ_uw) parameterization does the proton sheet adopt? Or is there a unified picture that recovers both regimes?

2. **Heavy-nucleus binding (the 88% deficit).** R64's current model accounts for only ~12% of nuclear binding energy beyond the deuteron. What's the structural mechanism for the rest?

3. **Generation structure.** Does the proton sheet host all six quark flavors (u, d, s, c, b, t), or do heavier flavors live on different sheets? See [R53-three-generations](../../studies/R53-three-generations/).

4. **Cross-sheet mediator exchange.** Strong force is sheet-internal; weak force is cross-sheet (proton-electron-neutrino). What's the structural difference?

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

## Chapters

To be filled in once work files converge on stable enough conclusions to graduate to chapter-level prose. The chapter outline will emerge from the work; it is not committed in advance.
