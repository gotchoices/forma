# STATUS — sheet-proton work file tracker

Tracks the project's active work files, their states, dependencies, and next actions. Living document — update as work progresses.

**Project state:** Work-file-driven exploration. The proton sheet's specific structure (geometry, quark content, mediator physics) is being investigated through focused work files; chapter-level prose emerges only after work files converge on stable conclusions.

---

## Work files

### strong.md — Yukawa-mediator path to strong force

**Topic:** Derive strong force as Yukawa exchange via a wave-mediator on the proton sheet. The mediator's Compton wavelength sets the force range; Coulomb-α applies at long range; the two regimes combine smoothly.

**Status:** Drafted; full 9-section outline complete. Ready for computational work.

**Dependencies:**
- *Upstream:* metric-charge (sheet structure, closure rule); metric-mass chapter 5 (standing-wave reading); metric-binding (general binding framework)
- *Sister files (in sheet-proton):* quark-flavor, meson-spectrum, clover-quarks
- *Sister files (in metric-binding):* mass-from-cancellation, standing-wave-vs-mediator

**Next actions:**
1. Implement `mode-spectrum-sweep.py` — catalog proton-sheet mode spectrum at R64 parameters; find candidate mediator modes.
2. Implement `qq-bar-compound.py` — compute 2-component compound masses.
3. Run phenomenological Compton-switching probe in parallel as sanity check.
4. Build Coulomb+Yukawa Schrödinger solver and test against R64 Phase 7d's QM gate.

---

### quark-flavor.md — quark structure as canceling primitives

**Topic:** Catalog candidate (m, n) mappings for u and d quarks on the proton sheet. Test each against observed proton/neutron mass, mass split, decay structure.

**Status:** Drafted. Four candidate mappings identified: R64 (n-flipped), User-1 (m-flipped), User-2 (full sign-flip), Alternative-3 (independent primitives).

**Dependencies:**
- *Upstream:* metric-charge chapter 4 (closure rule), R64 empirical fit
- *Sister files (in sheet-proton):* strong, meson-spectrum, clover-quarks
- *Sister files (in metric-binding):* mass-from-cancellation, fractional-charge, color-confinement

**Next actions:**
1. Implement `quark-mapping-spectrum.py` — compute proton and neutron predicted masses for all four mappings.
2. Rank mappings by empirical fit.
3. Check closure compatibility for the top-ranked mapping(s).
4. Feed result into strong (mediator content depends on quark mapping) and meson-spectrum.

---

### meson-spectrum.md — light mesons as 2-component compounds

**Topic:** Identify light mesons (π, K, η, ρ, ω, φ) as 2-component qq̄ compounds in MaSt. Naive dispersion mass predictions; structural questions about pion's small mass; strangeness assignment.

**Status:** Drafted. Naive predictions tabulated; significant gaps identified (pion mass mechanism, strangeness assignment, spin-0/spin-1 splittings).

**Dependencies:**
- *Upstream:* metric-charge chapter 8 (σ_uw shear effects); R53 (three-generation structure)
- *Sister files (in sheet-proton):* strong, quark-flavor, clover-quarks
- *Sister files (in metric-binding):* mass-from-cancellation

**Next actions:**
1. Compute naive dispersion masses for all light mesons at R64 parameters. Identify gaps.
2. Test σ_uw shear effects on (0, 0)-summed-winding compounds (might lift pion mass from zero).
3. Frame strangeness as T(1, +3) on proton sheet; compute kaon mass.
4. Investigate spin-0 vs spin-1 splitting mechanism.

---

### clover-quarks.md — corrugated 3-lobed torus as quark substrate

**Topic:** Develops a candidate geometric construction: a torus whose cross-section is a clover-leaf (3 lobes + 3 saddles) and whose ring sweep includes a 120° chiral twist per revolution. Tests whether quarks correspond to specific path classes on this surface, with the 1/3 twist providing the natural Z₃ precession for proton-as-3-quark closure.

**Status:** Drafted. Geometric construction laid out; profile closure verified via Gauss-Bonnet; closure conditions for "up-quark" (2 lobes + 1 saddle) and "down-quark" (2 saddles + 1 lobe) paths posed but not fully verified.

**Dependencies:**
- *Upstream:* metric-charge chapter 4 (closure rule) + chapter 7 (aspect ratio character)
- *Sister files (in sheet-proton):* quark-flavor
- *Sister files (in metric-binding):* fractional-charge (partial-knot picture; corrugated torus is candidate geometric realization), color-confinement (Z₃ structure emerges from 3-lobe profile)

**Next actions:**
1. Verify geometric closure of the clover profile (plot, confirm smooth).
2. Implement corrugated-torus embedding in 3D; render to inspect.
3. Work out path closure for up-quark and down-quark hypotheses; determine which parameterization is right.
4. Develop wave equation on the corrugated torus; compute mode spectrum.

**Why this might matter:** if the corrugated torus picture survives, it provides a *single* geometric construction that addresses Z₃ confinement, fractional charge, three-quark structure, and the up/down quark distinction simultaneously. Each of these is currently a separate open question (some in metric-binding, some here). A unifying geometric mechanism would be a substantial structural contribution.

---

## Dependency graph

```
metric-charge ch 4 ─┬─→ quark-flavor (sheet-proton) ──┬──→ strong (sheet-proton)
                    │                                  │
                    ├─→ clover-quarks (sheet-proton) ──┤
                    │                                  │
                    └─→ meson-spectrum (sheet-proton) ─┘
                          ↑                         ↑
                          │                         │
                          └─ R64, R53, R63          │
                                                    │
metric-binding/work/ ──→ general framework ─────────┘
   (color-confinement, fractional-charge,
    mass-from-cancellation, standing-wave-vs-mediator)
```

**Critical-path observation:** quark-flavor.md is the bottleneck for several other files. Resolving the (m, n) assignment unblocks mass calculations in meson-spectrum, mediator identification in strong, and structural interpretation in clover-quarks.

**Cross-cutting candidate:** clover-quarks.md. If the corrugated-torus geometry holds up, it provides one structural answer to questions that are otherwise distributed across multiple work files (quark-flavor, color-confinement in metric-binding, fractional-charge in metric-binding). Potential "unification" work file.

---

## Project priorities

**Phase 1 (immediate):** Resolve the quark-flavor question.

1. **quark-flavor.md** — implement `quark-mapping-spectrum.py`; determine which mapping fits.
2. **clover-quarks.md** (parallel track) — verify geometric closure of the clover profile; render the corrugated-torus surface; work out up-quark and down-quark path closure conditions. If the geometric construction holds, it may obsolete or refocus several other work files.

**Phase 2 (medium-term):** Build the Yukawa-mediator picture.

3. **strong.md** — identify the mediator mode; compute Coulomb+Yukawa potential; pass R64 Phase 7d's QM gate.
4. **meson-spectrum.md** — predict the light-meson spectrum; check pion mass mechanism.

---

## Open architectural questions

Issues that span multiple work files:

- **The R64 two-point proton fit (Point A vs Point B).** Which (ε, σ_uw) parameters does sheet-proton adopt? Point A fits the deuteron; Point B fits heavy nuclei. The two are mutually exclusive in R64. **Affects:** all work files here.

- **Smooth vs corrugated proton-sheet geometry.** Is the proton sheet flat (metric-charge's assumption) or corrugated (clover-quarks's hypothesis)? **Affects:** all work files; commitment shifts the whole project.

- **Mass-vs-charge framing.** Per metric-mass chapter 5: the project's choice to read compact-direction momentum as mass-generating is a framing choice. How does this interact with the proton sheet's charge structure? **Affects:** quark-flavor, meson-spectrum, strong.

- **Cross-sheet mediator exchange.** Strong force is sheet-internal; weak force (β decay) is cross-sheet. Two different coupling mechanisms. **Affects:** strong (specifically the strong-vs-weak distinction in the framework).

---

## Cross-reference: files in sibling projects

The general-framework work files live in [../../metric-binding/work/](../../metric-binding/work/):

- **mass-from-cancellation.md** — general cancellation mechanism for compound masses; applies to any sheet's compounds
- **fractional-charge.md** — general partial-knot framework
- **color-confinement.md** — general Z₃ structural question
- **standing-wave-vs-mediator.md** — general framework vocabulary, foundational

When work files in this project cite framework mechanisms (cancellation, partial knots, Z₃), they reference these general files; the proton-specific application of each mechanism lives here.

---

## Notes on workflow

1. Work files are *exploratory*. They evolve. Don't be afraid to retire bad hypotheses or merge files.
2. When a work file's main hypothesis converges (verified or refuted), graduate the content to chapter-level prose in this project's chapter outline.
3. Computational scripts referenced in work files should go in `sheet-proton/scripts/` (to be created when needed). Use Python with standard scientific libraries (numpy, scipy).
4. Cross-reference liberally between work files in this project AND in sibling projects. The dependency structure is real — changes cascade.
5. Each work file should have a clear *next action* listed. If a file is stuck, escalate to a brainstorming session before pushing computation.

---

## Last updated

Initial set up of sheet-proton with four proton-specific work files inherited from metric-binding. General-framework files (mass-from-cancellation, fractional-charge, color-confinement, standing-wave-vs-mediator) remain in metric-binding. Next milestone: first computational result from quark-flavor or clover-quarks.
