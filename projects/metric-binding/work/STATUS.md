# STATUS — metric-binding work file tracker

Tracks the project's active work files, their states, dependencies, and next actions. Living document — update as work progresses.

**Project state:** General multi-knot binding framework. Proton-specific exploration has been factored out to [sheet-proton](../../sheet-proton/) (see [sheet-proton/work/STATUS.md](../../sheet-proton/work/STATUS.md) for that project's tracker). This project retains the general-framework work files that apply to any sheet, not just the proton's.

**Project state (project-level):** Chapters not yet started; work files are the active development substrate. The project is currently in a holding pattern while sheet-proton's specific exploration advances. metric-binding will be revisited once sheet-proton's proton-specific findings inform the general binding framework.

---

## Work files (general framework, sheet-agnostic)

### mass-from-cancellation.md — mass from residual full-ring terms

**Topic:** Hypothesis that composite-particle mass emerges from the *residual* (un-cancelled) full-ring components of a multi-knot compound after partial-turn cancellations between constituents. Generalizes the n-linear cross-term cancellation of metric-mass chapter 5 §7 to multi-(m,n) compounds.

**Status:** Drafted. Worked example for R64's proton (3, +2) compound outlined; cancellation pattern conjectured but not verified.

**Dependencies:**
- *Upstream:* metric-mass chapter 5 §7 (the prototype cancellation result)
- *Sister files (in metric-binding):* fractional-charge
- *Sister files (in sheet-proton):* quark-flavor (cancellation pattern depends on quark mapping)

**Next actions:**
1. Compute T_total for the R64 proton compound (1,+2) + (1,+2) + (1,−2). Identify which cross-terms vanish.
2. Verify that surviving stress-energy disperses at μ²(3, +2).
3. Test User-1's alternative compound (1,+2) + (1,+2) + (−1,+2) → (1, +6).
4. Compare mass predictions for both compounds against proton mass.

---

### fractional-charge.md — fractional charge as partial knots

**Topic:** Develop the hypothesis that fractional charges (±1/3, ±2/3) emerge from *partial knots* — sub-configurations that satisfy closure only when combined into 3-component compounds. Connects fractional charge to Z₃ confinement structurally.

**Status:** Drafted. Four candidate formalizations identified (2a fractional winding, 2b synchronized arcs, 2c sub-windings of parent closure, 2d constrained quasi-particles).

**Dependencies:**
- *Upstream:* metric-charge chapter 4 (closure decomposition)
- *Sister files (in metric-binding):* color-confinement
- *Sister files (in sheet-proton):* quark-flavor (depends on formalization chosen here), clover-quarks (candidate geometric realization of partial knots)

**Next actions:**
1. Choose a formalization to develop concretely. Recommend 2c (most computable).
2. Formalize what "fractional charge" means mathematically — what does it mean for an arc on T² to carry fractional winding?
3. Verify chapter-4 decomposition T(3, 3n') = 3 × T(1, n') matches the partial-knot picture.
4. Test against R60 Track 16's Z₃ derivation.

---

### color-confinement.md — Z₃ confinement as structural

**Topic:** Derive the Z₃ structure of QCD (baryons = 3-component, mesons = 2-component) from MaSt geometry rather than borrowing it from SU(3) color symmetry. Deepest question of the project.

**Status:** Drafted. Four candidate structural origins (3a torus topology, 3b mode spectrum, 3c σ_uw residual symmetry, 3d fractional-charge complement).

**Dependencies:**
- *Upstream:* R60 Track 16 (Z₃ derivation); metric-charge chapter 4 (closure)
- *Sister files (in metric-binding):* fractional-charge
- *Sister files (in sheet-proton):* quark-flavor (assignment depends on Z₃ structure), clover-quarks (3-lobe geometry as candidate realization)

**Next actions:**
1. Pick one candidate origin and develop it concretely.
2. Examine R60 Track 16's existing Z₃ derivation — what mechanism does it use?
3. Catalog all closure-satisfying multi-link counts (2, 3, 4, 5, ...) — is 3 actually special?

---

### standing-wave-vs-mediator.md — particle/mediator distinction

**Topic:** Foundational vocabulary for the wave-only reading. Distinguishes *particles* (standing waves, directionless, localized) from *mediators* (propagating waves, directional, ranged). Both are wave modes of the same substrate but with different boundary conditions.

**Status:** Drafted. Conceptual structure laid out; specific computational implications identified.

**Dependencies:**
- *Upstream:* metric-mass chapter 5 (standing-wave commitment); primers/maxwell-primer (classical wave reading of EM)
- *Sister files (in sheet-proton):* strong (uses the distinction operationally)

**Next actions:**
1. Formalize the boundary-condition distinction between particle and mediator wave solutions.
2. Compute the coupling between particle's standing wave and mediator's propagating wave (overlap integral).
3. Derive source-mediated force law (Yukawa V(r)) from this coupling.

**Promotion candidate:** if mature, this work file's content likely belongs in a primer rather than living in metric-binding's work-files. Defer the promotion decision until the file converges.

---

## Cross-reference: files in sibling projects

The proton-specific work files have moved to [sheet-proton/work/](../../sheet-proton/work/):

- **strong.md** — Yukawa-mediator path to strong force on the proton sheet
- **quark-flavor.md** — u/d quark (m, n) mappings on the proton sheet
- **meson-spectrum.md** — light mesons as 2-component compounds on the proton sheet
- **clover-quarks.md** — corrugated 3-lobed torus as candidate proton-sheet geometry

When work files in this project cite proton-specific applications, they reference those files in sheet-proton; the general-framework mechanism lives here.

---

## Dependency graph

```
metric-mass ch 5 ─→ mass-from-cancellation (metric-binding)
                  └→ standing-wave-vs-mediator (metric-binding)

metric-charge ch 4 ─┬─→ fractional-charge (metric-binding)
                    ├─→ color-confinement (metric-binding)
                    └─→ (proton-specific files in sheet-proton)
                          [strong, quark-flavor, meson-spectrum, clover-quarks]
```

---

## Open architectural questions (general framework)

Issues that span the framework's general structure:

- **The (m, n) → (−m, n) vs (m, n) → (−m, −n) distinction.** [metric-charge chapter 6](../../metric-charge/06-handedness-and-pairs.md) discusses handedness pairs; the full antimatter reflection is (−m, −n). What's the structural difference? **Affects:** fractional-charge, color-confinement (and proton-specific files in sheet-proton).

- **Inter-sheet coupling strength.** Per metric-charge open issues + STATUS analysis: sheet-to-sheet coupling is much weaker than sheet-to-S (Fermi vs α). What's the structural mechanism? **Affects:** standing-wave-vs-mediator (for cross-sheet mediator exchange), neutron-decay analysis.

- **Standing-wave construction extension to T².** [metric-mass chapter 5](../../metric-mass/05-metric-self-consistency.md) developed standing-wave construction for 1D compact. The 2D T² extension is implicit but not formalized. **Affects:** mass-from-cancellation; also proton-specific files in sheet-proton.

---

## Notes on workflow

1. Work files are *exploratory*. They evolve. Don't be afraid to retire bad hypotheses or merge files.
2. When a work file's main hypothesis converges (verified or refuted), graduate the content to chapter-level prose in metric-binding's chapter outline.
3. Computational scripts should go in `metric-binding/scripts/` (to be created when needed). Use Python with standard scientific libraries (numpy, scipy).
4. Cross-reference liberally between work files within and across projects. The dependency structure is real — changes cascade.

---

## Last updated

Project restructured: proton-specific work files (strong, quark-flavor, meson-spectrum, clover-quarks) moved to sheet-proton/. metric-binding retains the four general-framework files (mass-from-cancellation, fractional-charge, color-confinement, standing-wave-vs-mediator). Project is in holding pattern while sheet-proton's specific exploration advances.
