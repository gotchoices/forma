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

### clover-mass.md — analytical mass spectrum on the corrugated torus

**Topic:** Derive m(ε, χ, τ; embedding) analytically by reducing the 2D Laplacian on the corrugated torus to a 1D Hill equation (via the helical translation symmetry of clover-quarks §10.3), expanding perturbatively in η = r_lobe/R_major around the constant-radius flat-twisted-torus limit, and inverting two observables (m_p, m_n) to extract two unknowns (ε, χ).

**Status:** Phase-A complete through O(η²) + independent numerical validation. Zeroth-order formula μ² = (n − 2m/3)² + (m/ε)² validated to machine precision. First-order vanishing validated. Second-order PT formula (§6.3) found INCORRECT — failed to restrict to Bloch sector; corrected to use intra-sector (1/w) coupling. Numerical Bloch-restricted Fourier solver (scripts/laplacian_spectrum.py) confirms candidate pairs like ((1, 2), (2, 2)) at ε ≈ 0.2 give m_n/m_p within 0.03% of observation. Earlier "negative result" reversed. Framework PASSES qualitative test.

**Dependencies:**
- *Upstream:* clover-quarks (the surface, the metric, the path-winding identifications)
- *Sister files:* clover-quarks (mode-particle identification is a shared open question)

**Next actions:**
1. Solve the Hill equation directly (non-perturbatively) on a small grid of (ε, χ) — scipy 1D ODE eigenvalues, very cheap.
2. Expand the (n, m) search to higher integers (smaller second-order shifts).
3. Redo for embedding B (rotation) and compare.
4. Check wavefunction overlaps with lobe/saddle regions for the candidate modes.

**Why this matters:** This is the first concrete falsifiable test of the corrugated-torus geometry as a particle-physics substrate. Phase A (qualitative results: charges, Z₃ confinement, β-decay topology) succeeded. Phase C (quantitative: mass ratio) so far fails. If the non-perturbative ODE solve also fails, the geometry as currently specified cannot produce the standard model's mass spectrum, and the next step is to either modify the geometry (different τ, different profile, different embedding) or accept that this surface explains the *qualitative* structure but the masses come from elsewhere.

---

### clover-quarks.md — corrugated 3-lobed torus as quark substrate

**Topic:** Develops a candidate geometric construction: a torus whose cross-section is a clover-leaf (3 lobes + 3 saddles) and whose ring sweep includes a 120° chiral twist per revolution. Quarks identified with single arcs (u = 1 lobe, d = 1 saddle); protons/neutrons identified with composite paths (uud = 2 lobes + 1 saddle, udd = 1 lobe + 2 saddles).

**Status:** **Phases A and B complete** (analytical math, §§7–12). Phase A headline result: per-arc charge integration gives Q_lobe = +2/3 and Q_saddle = −1/3 directly — the standard QCD fractional charges fall out as the per-radian curvature content of profile segments. Phase B established: clean quark identifications, path closure under literal-arc parameterization (proton in 2 ring revolutions, neutron in 1), neutron decay as topological q-shift (1 saddle → 1 lobe), and energy considerations for proton stability. Phase C (numerical mode spectrum) deferred.

**Dependencies:**
- *Upstream:* metric-charge chapter 4 (closure rule) + chapter 7 (aspect ratio character)
- *Sister files (in sheet-proton):* quark-flavor (path topology depends on quark mapping)
- *Sister files (in metric-binding):* fractional-charge (partial-knot picture; Phases A-B are the concrete geometric realization), color-confinement (Z₃ structure derived from twist topology)

**Next actions:**
1. Verify geometric closure of the clover profile (plot, confirm smooth) — simple sanity check.
2. Implement corrugated-torus embedding in 3D; render to inspect.
3. Catalog excited states (higher-energy paths beyond the canonical proton and neutron) — might match observed baryon resonances (Δ⁺⁺, Δ⁺, Δ⁰, Δ⁻, N* states).
4. **Phase C numerical work:** implement the Laplacian, compute the mode spectrum at representative (ε, χ); compare to flat-T² baseline; predict the u-d and p-n mass splits.

**Why this might matter:** Phases A and B provide a structural derivation of (a) fractional quark charges (lobe vs saddle per-radian content), (b) three-quark baryon structure (full-profile coverage requires 3 arcs), (c) Z₃ confinement (closure forces integer-summing combinations), (d) the up/down quark distinction (lobe vs saddle), (e) proton and neutron structure (2-lobe+1-saddle vs 1-lobe+2-saddle paths), and (f) a topological mechanism for neutron decay (q-shift converting one saddle to one lobe). Whether Phase C yields quantitatively correct masses (quark, proton, neutron, mass splits) is the remaining empirical test.

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

- **Is the 1/3 twist of clover-quarks tunable, or is it forced?** The twist value τ = 1/3 produces the third-integer charge fractions of QCD. Other rational twists (1/2, 1/4) would predict different fractional structures not seen in nature. **Affects:** clover-quarks specifically; the framework's prediction depends on τ = 1/3 being structurally singled out, not just tunable.

- **Path-closure asymmetry between up and down.** The proton path (2 lobes + 1 saddle) and neutron path (1 lobe + 2 saddles) close in different numbers of ring revolutions (2 vs 1 under literal-arc parameterization). Whether this asymmetry has empirical consequences (e.g., for the u-d mass split) is a Phase C question for clover-quarks.

- **Generation structure: c, s, t, b mappings.** [clover-quarks](clover-quarks.md) currently identifies u = 1 lobe, d = 1 saddle. Where do the heavier quarks (charm, strange, top, bottom) live? Three candidate mappings tracked but unresolved:
  - **(A) Higher harmonics on the same surface:** s, c, b, t are higher-q modes of the same proton sheet. Pro: simple. Con: doesn't naturally produce QCD's wide mass hierarchy.
  - **(B) Different sheets for different generations:** each generation lives on its own corrugated torus with different (ε, χ). Pro: parameter freedom. Con: requires positing extra sheets.
  - **(C) Sub-corrugation:** modes with additional internal structure. Pro: novel. Con: unsketched.
  - **Affects:** the project's complete theory of quark flavors. **Likely needs its own work file** (`three-generations.md` or similar) to develop.

- **Energy mechanism for n → p decay.** Under [clover-quarks §12.4](clover-quarks.md), the d → u transition is structurally a "q-shift" (one saddle becomes one lobe) — a topological transition rather than a direction reversal. The energy released (~0.78 MeV) is consistent with the observed β-decay Q-value. **Open:** whether the topology alone or substrate asymmetry (from [work-strong](strong.md) / grid-primitive ch 9) dominates the n-p mass split (1.29 MeV).

- **Why is the proton stable and the neutron unstable?** Under clover-quarks, the proton path (2 lobes + 1 saddle) is energetically preferred to the neutron path (1 lobe + 2 saddles). This requires either (i) intrinsic energy asymmetry between lobes and saddles (Candidate A) or (ii) substrate-level chirality asymmetry beyond the topology (Candidate B). **Affects:** clover-quarks's Phase C numerical work; cross-references work-strong's substrate-asymmetry hypothesis.

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
