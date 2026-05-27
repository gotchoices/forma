# STATUS — sheet-proton work file tracker

Tracks the project's active work files, their states, dependencies, and next actions. Living document — update as work progresses.

**Project state:** **On hold** as of 2026-05-16. The dim-sharing reframe explored in 3-torus.md and ma-share.md (both since moved to [ma-domain](../../ma-domain/)) suggested that the three-sheet architecture should be reconceived as a single multi-dim Ma domain with sparse cross-terms. The new architecture is being developed in [ma-domain](../../ma-domain/); sheet-proton's clover-quarks 1/3-twist mechanism and R53 / model-F charged-lepton fit are inherited as working results there. This project resumes when ma-domain either converges on the unified architecture (in which case sheet-proton is retired or refactored) or finds the reframe untenable (in which case sheet-proton picks up where it left off).

**Project state (pre-hold):** Work-file-driven exploration. The proton sheet's specific structure (geometry, quark content, mediator physics) is being investigated through focused work files; chapter-level prose emerges only after work files converge on stable conclusions.

---

## Restart from first principles — checklist

The clover-quarks and clover-mass development accumulated terminology drift, conflated wave-mode labels with path-winding labels, and didn't separately account for continuous shear σ vs discrete twist τ. Starting 2026-05-14 we are working through both files from first principles, updating in place. Steps in suggested order; check off as completed.

### Phase 0 — Nomenclature reset

- [x] Adopt `(n_t, n_r)` (tube-first per metric-charge) for path winding numbers
- [x] Adopt a distinct notation for wave-mode quantum labels: **(m_t, m_r)** tube-first
- [x] Clarify the **σ vs τ** distinction (open question; pin during Phase 1):
  - **τ** (discrete twist, locked to k/3): a rotation of the cross-section by 2π/3 per ring revolution. Changes the **boundary identification** on the surface — that's a topological operation, which forces Bloch sectors and m mod 3 constraints. Discreteness is forced by Z₃ symmetry of the profile.
  - **σ** (continuous internal sheet shear, free parameter): an intrinsic **metric** property of the sheet before rolling. Affects only the off-diagonal g_θφ coupling; does *not* change boundary identifications.
  - **From the wave's perspective:** both appear in the mass formula additively in something like σ_eff = σ + 2τ. So a wave alone cannot distinguish geometric origin from topological — only the *spectrum's discreteness* (sector structure) carries τ's topological fingerprint.
- [x] Define key mathematical terms in a "Conventions" block at the top of clover-quarks.md: **Hill equation** (1D ODE of the form ψ'' + p(u)ψ' + q(u)ψ = 0 with periodic coefficients, named after George William Hill); **Sturm–Liouville form**; **helical translation symmetry**; **Bloch sector** (subspace of wavefunctions sharing a single twist-identification phase); **zeroth/first/second-order perturbation theory** (zeroth = unperturbed eigenvalues; first/second-order = correction in powers of the small parameter η = r_lobe/R_major)
- [x] Add the Conventions section to clover-quarks.md (now §0 — see Conventions block; includes a migration table mapping old (n, m) → new (m_t, m_r) tube-first)
- [x] Sweep all existing files (clover-quarks, clover-mass, quark-flavor, meson-spectrum) and scripts (spectrum_vs_pdg, validate_mass_formula) for terminology consistency. 3-gen and strong already had no old-convention usage; corrugated_torus and laplacian_spectrum use coordinate names (k_v, k_θ, k_φ) that don't require renaming.

### Phase 1 — Generalized clover-torus geometry (new: σ + τ as independent parameters)

- [x] Document the rolled-leaf construction in clover-quarks (now §1.3 — placed adjacent to §1.2's swept-profile construction as a parallel "alternative origin" subsection):
  - Sheared parallelogram sheet → leaf (central 4π/3 convex lobe arc + 2 × π/3 concave half-saddle arcs = full 2π leaf)
  - 3 leaves replicated around a centerline → straight clover tube (jagged ends due to σ)
  - Wrap centerline as ring spine → jagged ends meet continuously (clover torus with intrinsic σ)
  - Add the discrete 2π/3 twist τ on top → torus with **both** continuous σ and discrete τ
- [x] **Compatibility check:** σ → 0 reduces line-by-line to §§7–10. Verified by direct inspection in clover-quarks.md §10.3: setting σ = 0 in the combined boxed metric g_θθ = (R + P_x)² + τ²c², g_θφ = (σ+τ)c², g_φφ = c² recovers the τ-only formula of (the old) §10.2 exactly. The boundary identification, the parameter shift u = φ + τθ, and the 3D embedding A are all unchanged by σ = 0.
- [x] Resolve whether σ and τ are truly independent or interrelated. **Independent.** Documented in clover-quarks.md §10.5 with the asymmetry that proves it: τ enters u, g_θθ, g_θφ, and the boundary identification (so it is forced to k/3 by the profile's Z₃ symmetry); σ enters only g_θφ (so it is not subject to any quantization constraint). The geometric origin of the asymmetry is that τ rides the 3D embedding's chain rule while σ rides the intrinsic sheet metric.
- [x] Re-derive metric components (clover-quarks §10) with σ and τ as separate inputs. Done — §10 restructured: §10.1 tangent vectors (unchanged), §10.2 metric components for embedding A τ-only (unchanged, now framed as the σ = 0 special case), §10.3 rolled-leaf overlay adds σ c² to g_θφ, §10.4 helical translation symmetry (still holds because σ is a constant), §10.5 σ/τ independence. Determinant gets a small σ(σ+2τ) c² correction; leading-order inverse-metric structure makes σ_eff = σ + 2τ the cross-term coefficient in the mass formula.
- [x] Update `scripts/corrugated_torus.py` to accept σ as a separate CLI flag (independent of τ). Done — `--sigma SIGMA` flag added, threaded through `lib/geometry.py:corrugated_torus_surface()`. Implementation note: σ is purely an off-diagonal metric overlay and has no strict isometric realization in ℝ³, so for visualization the script uses an effective twist (σ + τ) for the parameter-shift / rotation rate. This conflates σ and τ at the visible-shape level (the σ vs τ distinction is in the metric structure and the boundary identification, not the 3D shape). Documented in the script and `lib/geometry.py` docstrings.
- [x] Render visualization comparisons at (σ, τ) = (0, 1/3), (small σ, 1/3), (moderate σ, 1/3) to verify the picture. Done — three renderings saved to `outputs/torus_chi1.00_R5.0_pshift_phi-band[_sigmaXXX]_helices6.png`. The σ ≠ 0 renderings show the helical phi-bands wrapping more tightly than σ = 0, confirming that σ surfaces as an additional shear rate in the visible geometry.

### Phase 2 — Mass formula re-derivation

(Definitions of *Hill equation* and *zeroth/first/second order* are added to clover-quarks's Conventions section in Phase 0; this phase uses them.)

- [x] Re-derive Hill equation reduction with the σ + τ metric (clover-mass §2). The helical-coord metric now has a residual constant off-diagonal g_vu = σ c² (since σ doesn't change the symmetry direction); the σ piece appears as a "magnetic" vector-potential term in the Hill equation (imaginary first-derivative coefficient) absorbable by a gauge transformation. Helical translation symmetry survives because the σ contribution is constant.
- [x] Recompute zeroth-order spectrum. At P_x → 0 the spectrum is exactly **μ² = (m_r − (σ + 2τ) m_t)² + (m_t/ε)²** — the σ-generalisation of the τ-only formula, with σ_eff = σ + 2τ as the cross-term coefficient. Derived in clover-mass.md §4; verified numerically by extending the Bloch-restricted Fourier-basis Hill solver (`scripts/laplacian_spectrum.py:hill_eigenvalues`) with σ as a parameter.
- [x] State explicitly when higher orders enter. The η-expansion is unchanged in structure: corrections are series in η = r_lobe/R_major = ε/(2 + χ), with first-order vanishing by Z₃ symmetry (∫ P_x du = 0) and second-order entering at O(η²). σ-corrections to the second-order PT formula enter at O(σ × η²) — small for small σ, and deferred. A separate higher-order-in-ε correction shifts the cross-term squared by a factor 1/(1 − σ σ_eff ε²); this is the next subdominant σ effect. Documented in clover-mass.md §4.
- [x] Determine σ_eff = σ + 2τ. The factor of 2 on τ comes from τ appearing twice in the spectrum derivation (once in the boundary identification k_θ = m_r − τ m_t, once in the inverse-metric cross-term coupling); σ appears once (only in g_θφ off-diagonal, not in the boundary identification). For τ = 1/3: σ_eff = σ + 2/3.
- [x] Update clover-mass §§1–4 with the generalised formula. §1 metric updated to g_θφ = (σ + τ) c²; §2 Hill reduction extended for σ ≠ 0; §3 Bloch conditions noted as unchanged (σ doesn't enter identification); §4 boxed zeroth-order formula now carries σ_eff = σ + 2τ with the σ = 0, τ = 1/3 special case spelled out alongside it; §4.1 table reframed as the σ = 0 special case. §§5–6 noted to apply at σ = 0; first-order vanishing argument extends to σ ≠ 0 unchanged; second-order σ-corrections deferred.
- [x] Re-validate numerically. `scripts/laplacian_spectrum.py:hill_eigenvalues` extended with `sigma` and `tau` parameters (derivation in the docstring; Bloch-restricted Fourier basis, σ enters via the full σ-modified determinant W̃ = w² − σ(σ + 2τ)ε²). `scripts/validate_mass_formula.py` extended with a new test **C6 σ-dependence**: at small η, the numerical spectrum at σ ∈ {0, 0.05, 0.10, 0.20, 0.30} matches the analytical (k_v − σ p)² + (p/ε)² formula to ~10⁻⁷ relative error — validating the §4 σ-generalisation. (C4 and C5 statuses are unchanged from before Phase 2 — the C4 "FAIL" reproduces a pre-existing documented bug in the §6.3 analytical PT formula; C5 finds candidate (p, n) pairs at the right neighbourhood, also pre-existing.)

### Phase 3 — Three generations (the strategic priority)

**Outcome: 2D-surface picture structurally rules out the hierarchy; 3D wave-guide + nested corrugation (Mechanism E) is the leading candidate.** See [3-gen.md §12](3-gen.md) for the synthesis. Investigation proceeded in three stages: (1) a numerical attempt at finding compartmentalized band structure in the 2D Hill spectrum (sparse 15-point sweep; found no compartmentalized structure); (2) analytical follow-on in [clover-modes-analytical.md](clover-modes-analytical.md) explaining the negative result structurally — in the 2D Hill equation, lobes are *wells* in the effective potential and lobe-localized states sit *below* the plane-wave continuum, opposite of "smaller cavity → higher frequency"; (3) analytical work in [tube-waveguide.md](tube-waveguide.md) showing the 3D wave-guide extension recovers the hierarchy qualitatively, plus a natural fractal-nested extension (added to 3-gen.md as Mechanism E §5.5) that **fits all 6 observed quark masses on a single sheet** with three nested geometric scales (parent corrugation + sub-corrugation + sub-sub-corrugation, with 5 parameters fitting 5 independent mass ratios and the 6th falling out by structural relation). Mechanism E resolves the within-generation flavor-ordering anomaly via the closure-vs-openness distinction between the outermost level (closure-Gauss-Bonnet-constrained) and inner sub-levels (open modules with free χ).

The framework's one-generation results (per-arc curvature charges Q_lobe = +2/3, Q_saddle = −1/3; Z₃ Bloch-sector structure) are unaffected by either analysis.

> **⚠ Closure-problem annotation (2026-05-22).** One previously-listed "unaffected"
> result — the **proton/neutron path-winding structure** of [clover-quarks.md §12](clover-quarks.md)
> — has since been found to have a closure problem: the literal piecewise-arc baryon
> paths never wrap a whole tube (φ-displacement stays in (2π/3, 4π/3)), so they do not
> close. It has accordingly been removed from the sentence above. The replacement
> construction — proton and neutron as closing tracks on a smooth modulated, half-twisted
> clover — is [modulated-clover.md](modulated-clover.md), the **current best candidate**:
> its charge construction works exactly (Q = +1, 0), and a path-length mass mechanism
> reproduces the nucleon mass-difference sign and ratio (the ratio as a one-parameter
> consistency fit). The per-arc charge result and the curvature-based mass fits are
> independent of path closure and still stand.

- [x] Review the various candidate mechanisms in 3-gen.md. Done — mechanisms A/B/C/D reviewed in [3-gen.md §5](3-gen.md). Under the 2D-surface interpretation all four fail (per [§12.4](3-gen.md)'s reassessment table); under the 3D wave-guide interpretation A, C, D are qualitatively viable, B remains bounded.
- [x] Implement χ-sweep infrastructure in `scripts/laplacian_spectrum.py`. Done — `--sweep-chi CHI_MIN,CHI_MAX,N_STEPS` flag added; reusable for future 2D-surface numerical work.
- [x] Build wavefunction localization classifier. Done — new script `scripts/wavefunction_viz.py`. Computes lobe/saddle overlap fractions with geometric-baseline subtraction, Z₃-alignment Re(c₃/c₀) of |ψ|², and lobe-focused/saddle-focused/whole-circumference classification. Reusable for future 2D-surface work; the natural follow-on for the 3D picture is a separate 2D Helmholtz solver (see below).
- [x] Numerical 2D Hill spectrum sweep. Done at ε ∈ {0.5, 1.5, 3.0}, χ ∈ {0.3, 1.0, 3.0}. Found no compartmentalized band structure in the lowest few eigenvalues; inter-m ratios bounded at ~3 in this regime. *Cluttery outputs from the sweep have been deleted; the sweep prompted the analytical follow-on rather than producing a final answer.*
- [x] Analytical follow-on: 2D Hill structural analysis ([clover-modes-analytical.md](clover-modes-analytical.md)). Showed structurally why the 2D Hill equation can't produce the user's hierarchy (lobes are wells, not cavities; localized states are *lighter* than plane-waves). Numerical absence of compartmentalized structure is the expected result, not a sparse-sweep artifact.
- [x] Analytical follow-on: 3D wave-guide extension ([tube-waveguide.md](tube-waveguide.md)). Showed that the natural 3D-interior extension recovers the hoped-for hierarchy qualitatively. Cross-section asymmetry χ ~ 0.01–0.1 gives mass ratios in the 10²–10³ range — sufficient for gen-1↔gen-2 quark mass ratios on a single sheet, short of the gen-3 ratios which more naturally come from cross-sheet structure.
- [x] Update 3-gen.md to document the outcome. Done — [3-gen.md §12](3-gen.md) is the synthesis (numerical attempt → analytical 2D-only ruling-out → analytical 3D-extension recovery → next-step recommendation). Status banner reframed accordingly.
- [ ] **Next: implement 2D Helmholtz solver for the clover cross-section.** This is the natural follow-on for the 3D wave-guide picture — replaces [tube-waveguide.md](tube-waveguide.md)'s disc-approximation estimates with accurate clover-domain eigenvalues. ~1 day of focused numerical work. Would consume geometry utilities from `scripts/lib/` with a 2D meshing step instead of the 1D u-grid used by `laplacian_spectrum.py`.
- [ ] ~~Update clover-quarks.md §12 with the 6-quark identification.~~ **Still skipped** — the 3D wave-guide picture, while qualitatively viable, isn't yet quantitatively validated. Pinning a 6-quark identification would be premature pending the 2D Helmholtz solver.

### Phase 4 — Other particles via SM recipes

(Reframed by Phase 3's verdict: the clover sheet hosts the light (u, d) generation only. Heavier quarks reside on separate sheets in the [metric-binding](../../metric-binding/) framework. So Phase 4 splits into a "this sheet" part — building mesons and baryons from u and d — and a "cross-sheet" part covered by future work in the metric-binding project.)

- [ ] Build mesons (q + q̄) on the clover sheet using u, d only (π⁰, π±, ρ, η-like states)
- [ ] Build proton-sheet baryons (p, n, Δ⁺⁺, Δ⁻) using 3-light-quark recipes — extends [clover-mass.md §9.1 Concern B](clover-mass.md) tests
- [ ] Cross-reference predictions with PDG via `scripts/spectrum_vs_pdg.py`
- [ ] Update meson-spectrum.md with results (proton-sheet mesons only)
- [ ] Update quark-flavor.md to reflect the generalized framework AND the cross-sheet placement of c, s, t, b
- [ ] Defer to metric-binding: where do the heavier-quark sheets live, and what is the cross-sheet mediator mechanism (links to [strong.md](strong.md) cross-sheet question)

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

### [derived-clover.md](derived-clover.md) — formal derivation of the modulated-clover substrate
- Status: groundwork complete (C1–C6 hypothesis chain, per-arc charge integral, Z₂ × Z₃ symmetric finding, discrete symmetries, wave/track reconciliation status).  Feeds the chapter arc in the parent [README.md](../README.md).

### [lb-mode-localization.md](lb-mode-localization.md) — 2-D LB localization test on the modulated-clover
- Status: complete.  Direct computation (`scripts/track_localization.py`) showing that no LB eigenmode and no low-energy superposition track-localises at the proton's energy scale on this surface.  Reframed under the single-quantum-with-along-track-substructure reading: the LB amplitude doesn't need to be track-localised because the per-arc charge integral is Berry-phase-like, not amplitude-weighted.

### [quark-decomposition.md](quark-decomposition.md) — 3-quarks-in-series test on the per-arc track integral
- Status: first pass complete.  The simplest reading (equal-θ segments of the existing track-charge integral yield per-quark +2/3 / −1/3 charges) does *not* work — Z₃ screw symmetry of the substrate forces all 3 segments to integrate identically.  Two refined repairs identified (cross-section per-arc integral vs Z₃-irrep decomposition); neither tested yet.  **Action item:** test Repair A before drafting Chapter 5.

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
- **Is τ = 1/3 tunable or forced?** See clover-quarks; Phase 1's σ + τ separation made τ a discrete *topological* parameter forced to k/3 by Z₃ profile symmetry, while σ remained continuous. τ = 1/3 is therefore "forced" once we commit to the 3-lobe / 3-saddle profile structure. Settled.
- **Why is the proton stable and the neutron unstable?** See clover-quarks §12.5–12.6; **not resolved** by Phase 3 (which gave a negative result on multi-generation structure). Remains an open question; may be resolved by the cross-sheet weak-interaction structure in [metric-binding](../../metric-binding/).
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

2026-05-14 — Restart from first principles initiated. Added a 6-phase checklist (Phase 0 nomenclature → Phase 5 cleanup) at the top; slimmed the Work files section to one-line + open todos; retired the obsolete "Project priorities" section; slimmed Open architectural questions to bullets. **Phase 3 verdict: negative — none of Mechanisms A/B/C/D produce the observed multi-generation mass hierarchy.** The bare clover spectrum's inter-m mass ratios max at ~3 (vs observed 580 for m_c/m_u, 78,000 for m_t/m_u); the Mechanism-D doublet appears only at m = 3 and with zero mass split. The one-generation results (Q_lobe = +2/3, Q_saddle = −1/3, proton/neutron paths) are unaffected. Phase 4 is reframed: heavier quarks live on other sheets, not on this one. **Phase 0 complete:** clover-quarks.md §0 Conventions section drafted; (n_t, n_r) for path windings and (m_t, m_r) for wave-mode labels adopted with tube-first convention; clover-quarks.md, clover-mass.md, quark-flavor.md, meson-spectrum.md, scripts/spectrum_vs_pdg.py, scripts/validate_mass_formula.py swept for consistency. **Phase 1 complete:** rolled-leaf construction documented as clover-quarks.md §1.3; σ → 0 compatibility verified by inspection; σ/τ independence proven via the asymmetry that τ enters u, g_θθ, g_θφ, and the boundary identification while σ enters only g_θφ (clover-quarks.md §10.5); §10 fully re-derived with σ alongside τ (combined boxed metric g_θθ = (R+P_x)² + τ²c², g_θφ = (σ+τ)c², g_φφ = c²; helical translation symmetry survives because σ is constant; σ_eff = σ + 2τ emerges as the leading cross-term coefficient in the generalized mass formula); scripts/corrugated_torus.py extended with `--sigma` CLI flag (threaded through lib/geometry.py); three σ-comparison visualizations rendered at (σ, τ) = (0, 1/3), (0.10, 1/3), (0.30, 1/3) — the σ ≠ 0 cases show visibly tighter helical phi-bands, confirming σ acts as additional shear rate in the embedded shape. **Phase 2 complete:** mass formula generalised to σ + τ across clover-mass.md §§1–4 (§1 metric, §2 Hill-reduction with σ-induced "magnetic" first-derivative term absorbable by gauge transform, §3 Bloch unchanged, §4 new boxed formula μ² = (m_r − (σ + 2τ) m_t)² + (m_t/ε)² with σ_eff = σ + 2τ); σ-corrections to first-order vanish (∫ P_x du = 0 by Z₃ symmetry — independent of σ); σ-corrections to second-order PT enter at O(σ × η²) and are deferred; `scripts/laplacian_spectrum.py:hill_eigenvalues` extended with `sigma` and `tau` parameters via the full σ-modified determinant W̃ = w² − σ(σ+2τ)ε²; `scripts/validate_mass_formula.py` extended with new test C6 σ-dependence which validates the (k_v − σ p)² + (p/ε)² formula to ~10⁻⁷ at η ≈ 0.017 across σ ∈ {0, 0.05, 0.10, 0.20, 0.30}. **Phase 3 complete (negative verdict):** all four mechanisms (A: compartments, B: excitation tower, C: hybrid, D: wave count + amplitude focus) tested against the numerical eigenvalue spectrum; `scripts/laplacian_spectrum.py` extended with `--sweep-chi` mode (returns the lowest eigenvalues vs χ) and `hill_eigenvalues` extended to return eigenvectors; new `scripts/wavefunction_viz.py` evaluates eigenfunctions on a u-grid, computes lobe/saddle overlap fractions L with the proper geometric baseline L_baseline = 2/(2+χ), classifies modes by |L − L_baseline|, and runs the Mechanism-D doublet test across m ∈ {1, 2, 3}; outputs/ contains χ-sweep CSVs/PNGs at ε ∈ {0.5, 1.5, 3.0}, doublet-test CSVs/PNGs at representative (ε, χ), and `outputs/mass_ratio_survey.csv` summarising the bound; key result is that inter-m mass ratios across the explored (ε, χ) grid are bounded by ~3, whereas observed m_c/m_u ≈ 580 and m_t/m_u ≈ 78,000, so the bare clover-torus eigenvalue spectrum cannot host the heavy quarks under any of Mechanisms A/B/C/D; the m = 3 doublet structurally predicted by Mechanism D exists (one lobe-focused, one saddle-focused eigenstate at the same Bloch sector p = ±3) but its two members are exactly degenerate in μ² so the doublet adds no observable mass split; 3-gen.md §12 documents the verdict, including the reframing of Phase 4 to treat heavier quarks as living on separate sheets in the [metric-binding](../../metric-binding/) framework. Next milestone: Phase 4 (mesons + proton-sheet baryons from u, d only; cross-sheet questions deferred to metric-binding).
