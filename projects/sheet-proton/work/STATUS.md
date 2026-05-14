# STATUS — sheet-proton work file tracker

Tracks the project's active work files, their states, dependencies, and next actions. Living document — update as work progresses.

**Project state:** Work-file-driven exploration. The proton sheet's specific structure (geometry, quark content, mediator physics) is being investigated through focused work files; chapter-level prose emerges only after work files converge on stable conclusions.

---

## Restart from first principles — checklist

The clover-quarks and clover-mass development accumulated terminology drift, conflated wave-mode labels with path-winding labels, and didn't separately account for continuous shear σ vs discrete twist τ. Starting 2026-05-14 we are working through both files from first principles, updating in place. Steps in suggested order; check off as completed.

### Phase 0 — Nomenclature reset

- [ ] Adopt `(n_t, n_r)` (tube-first per metric-charge) for path winding numbers
- [ ] Adopt a distinct notation for wave-mode quantum labels (currently conflated with path windings)
- [ ] Clarify the **σ vs τ** distinction (open question; pin during Phase 1):
  - **τ** (discrete twist, locked to k/3): a rotation of the cross-section by 2π/3 per ring revolution. Changes the **boundary identification** on the surface — that's a topological operation, which forces Bloch sectors and m mod 3 constraints. Discreteness is forced by Z₃ symmetry of the profile.
  - **σ** (continuous internal sheet shear, free parameter): an intrinsic **metric** property of the sheet before rolling. Affects only the off-diagonal g_θφ coupling; does *not* change boundary identifications.
  - **From the wave's perspective:** both appear in the mass formula additively in something like σ_eff = σ + 2τ. So a wave alone cannot distinguish geometric origin from topological — only the *spectrum's discreteness* (sector structure) carries τ's topological fingerprint.
- [ ] Define key mathematical terms in a "Conventions" block at the top of clover-quarks.md: **Hill equation** (1D ODE of the form ψ'' + p(u)ψ' + q(u)ψ = 0 with periodic coefficients, named after George William Hill); **Sturm–Liouville form**; **helical translation symmetry**; **Bloch sector** (subspace of wavefunctions sharing a single twist-identification phase); **zeroth/first/second-order perturbation theory** (zeroth = unperturbed eigenvalues; first/second-order = correction in powers of the small parameter η = r_lobe/R_major)
- [ ] Add the Conventions section to clover-quarks.md
- [ ] Sweep all existing files (clover-quarks, clover-mass, quark-flavor, meson-spectrum, 3-gen, strong) and scripts (corrugated_torus, laplacian_spectrum, spectrum_vs_pdg, validate_mass_formula) for terminology consistency

### Phase 1 — Generalized clover-torus geometry (new: σ + τ as independent parameters)

- [ ] Document the rolled-leaf construction in clover-quarks §7 (or new subsection):
  - Sheared parallelogram sheet → leaf (central 4π/3 convex lobe arc + 2 × π/3 concave half-saddle arcs = full 2π leaf)
  - 3 leaves replicated around a centerline → straight clover tube (jagged ends due to σ)
  - Wrap centerline as ring spine → jagged ends meet continuously (clover torus with intrinsic σ)
  - Add the discrete 2π/3 twist τ on top → torus with **both** continuous σ and discrete τ
- [ ] **Compatibility check:** verify the σ → 0 limit of the rolled-leaf construction reduces to the existing clover-quarks model (§§7–10). If it doesn't, reconcile or retract.
- [ ] Resolve whether σ and τ are truly independent or interrelated. Working hypothesis: independent (σ from sheet's internal metric, τ from how the rolled tube is closed). Document the rolled-leaf algebra that proves it (or identify the coupling, if found).
- [ ] Re-derive metric components (clover-quarks §10) with σ and τ as separate inputs
- [ ] Update `scripts/corrugated_torus.py` to accept σ as a separate CLI flag (independent of τ)
- [ ] Render visualization comparisons at (σ, τ) = (0, 1/3), (small σ, 1/3), (moderate σ, 1/3) to verify the picture

### Phase 2 — Mass formula re-derivation

(Definitions of *Hill equation* and *zeroth/first/second order* are added to clover-quarks's Conventions section in Phase 0; this phase uses them.)

- [ ] Re-derive Hill equation reduction with the σ + τ metric (clover-mass §2)
- [ ] Recompute zeroth-order spectrum (= eigenvalues of the *unperturbed*, flat-twisted-torus limit where the corrugation P_x has vanishing amplitude): derive μ²(n_t, n_r, ε, σ, τ) explicitly
- [ ] State explicitly when higher orders enter — first/second-order corrections are series in η = r_lobe/R_major (corrugation depth measured relative to the ring scale); for the η-values we care about, document when truncation is justified
- [ ] Determine effective shear σ_eff (combination of intrinsic σ and twist τ)
- [ ] Update clover-mass §§3–4 with the generalized formula
- [ ] Re-validate numerically: extend `scripts/validate_mass_formula.py` to test σ-dependence

### Phase 3 — Three generations (the strategic priority)

- [ ] Review the various candidate mechanisms in 3-gen.md (A: compartments, B: excitation tower, C: hybrid, D: wave count + amplitude focus)
- [ ] Implement χ-sweep in `scripts/laplacian_spectrum.py` to expose band structure
- [ ] Compute wavefunction localization patterns (whole-circumference, lobe-localized, saddle-localized)
- [ ] Run Mechanism-D doublet test (the sharpest discriminator: for each m ∈ {1, 2, 3}, look for lobe-focused / saddle-focused antinode pairs)
- [ ] Identify the surviving mechanism; pin (σ, τ, ε, χ, r_lobe, r_saddle) from the 6 quark masses
- [ ] Update 3-gen.md to document the selected mechanism (or rule them all out)
- [ ] Update clover-quarks.md §12 with the 6-quark identification

### Phase 4 — Other particles via SM recipes

- [ ] Build mesons (q + q̄) using the pinned quark identifications
- [ ] Build other baryons (Λ, Σ, Ξ, Δ, ...) using SM 3-quark recipes
- [ ] Cross-reference predictions with PDG via `scripts/spectrum_vs_pdg.py`
- [ ] Update meson-spectrum.md with results
- [ ] Update quark-flavor.md to reflect the generalized framework

### Phase 5 — Cleanup and consolidation

- [ ] Verify all work files use consistent terminology
- [ ] Verify scripts produce outputs consistent with the new framework
- [ ] Archive or delete old/inconsistent outputs in `outputs/`
- [ ] Retire this checklist by updating STATUS.md to reflect the post-restart state

---

## Work files — pending todos

One-line per file, plus only todos we are tracking *here*. Detailed status, dependencies, and rationale live inside the files themselves.

### [clover-quarks.md](clover-quarks.md) — corrugated 3-lobed torus as quark substrate
- Restart todos: covered by the Phase 0–3 checklist above. No additional standalone todos at present.

### [clover-mass.md](clover-mass.md) — analytical mass spectrum on the corrugated torus
- Restart todos: covered by the Phase 0, 2, 3 checklist above. No additional standalone todos at present.

### [3-gen.md](3-gen.md) — three-generation candidate mechanisms (A/B/C/D)
- Restart todos: covered by Phase 3 above (review mechanisms; pick the surviving one; update with conclusion).

### [quark-flavor.md](quark-flavor.md) — quark structure as canceling primitives
- [ ] Pending restart work: update terminology and Mapping Clover to match the new (n_t, n_r) + (σ, τ) framework once Phase 0–3 settle.

### [meson-spectrum.md](meson-spectrum.md) — light mesons as 2-component compounds
- [ ] Pending restart work: covered by Phase 4 (build mesons via SM recipes once quark identifications are pinned in Phase 3).

### [strong.md](strong.md) — Yukawa-mediator path to the strong force
- [ ] Implement `mode-spectrum-sweep.py` (catalogue mediator-mode candidates on the proton sheet)
- [ ] Implement `qq-bar-compound.py` (2-component compound masses)
- [ ] Coulomb+Yukawa Schrödinger solver against R64 Phase 7d's QM gate
- [ ] Test the deuteron-binding-as-mode-coexistence hypothesis (strong.md §6a) once Phase 3 pins parameters

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

## Open architectural questions

Cross-cutting issues not owned by a single work file. The restart checklist (above) addresses several of these; others remain open.

- **R64 two-point proton fit (Point A vs Point B).** Which (ε, σ_uw) parameters does sheet-proton adopt? Open across all files.
- **Mass-vs-charge framing** (metric-mass ch. 5 standing-wave reading). Cross-cuts quark-flavor, meson-spectrum, strong.
- **Cross-sheet mediator exchange** — strong is sheet-internal, weak is cross-sheet. See strong.md for details.
- **Is τ = 1/3 tunable or forced?** See clover-quarks; restart Phase 1 may reframe.
- **Why is the proton stable and the neutron unstable?** See clover-quarks §12.5–12.6; restart Phase 3 may resolve via quark identification.
- **Weak and strong forces as least-energy calculus** (hypothesis). See clover-quarks §12.4.1 (weak) and strong.md §6a (strong / deuteron). First test: deuteron prediction.

Items now subsumed by the restart checklist: smooth-vs-corrugated geometry (Phase 1 commits to clover with σ + τ); path-closure asymmetry (Phase 2/3); generation structure (Phase 3 + 3-gen.md).

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

2026-05-14 — Restart from first principles initiated. Added a 6-phase checklist (Phase 0 nomenclature → Phase 5 cleanup) at the top; slimmed the Work files section to one-line + open todos (per the user's principle that STATUS.md tracks todos, not duplicates other files' content); retired the obsolete "Project priorities" section (now superseded by the restart checklist); slimmed Open architectural questions to bullets. Next milestone: complete restart Phase 0 (nomenclature reset and Conventions section in clover-quarks.md).
