# STATUS.md — ma-domain checklist and work plan

**Status:** Phased plan for the 6-dim Ma domain investigation. Each phase produces concrete work files in this directory; coherence across phases is the gate for promoting from `work/` to the top level `ma-domain/` (Phase 5).

---

## Phase 0 — Nomenclature & setup

- [x] **Naming convention** for the 11-component metric (4 spacetime + 7 Material = aleph + 6 Ma dims), with Material → Space → Time top-to-bottom and size-ordering within Material. Mode 11-tuple `{ n_aleph, n_1, ..., n_6, n_x, n_y, n_z, n_t }`. Done in [architecture.md §1–§2](architecture.md).
- [x] **Operational rules** for the per-pair tube/ring assignment, the smallest-as-tube closure convention, and the plane-over-diagonal (2D-planar preferred over 3D-mixed) sheet-constraining rule. Done in [architecture.md §3](architecture.md).
- [ ] **Cross-term sparsity pattern**: which of the 15 off-diagonals in the 6×6 Material block are non-zero, and what type (τ-twist, R53-shear, other) each carries. Provisional list:
  - 3 cross-terms with τ = 1/3 → quark planes
  - Up to 3 cross-terms with R53-shear → charged-lepton planes
  - Remaining cross-terms = 0 → orthogonal dim pairs
  
  See [architecture.md §4](architecture.md) for the open questions this resolution will address.

## Phase 1 — Quark sector

Two parallel paths now run in parallel:

### Path A (preferred): user's 4-dim topology (1,3)(2,3)(3,4)

- [x] **First-cut attempt: 3-dim topology (1,2)(1,3)(2,3).** Analytically + numerically falsified in [quark-search.md §1–§7](quark-search.md). The dim-sharing constraint was the obstruction.
- [x] **User's alternative topology: 4 dims with pairs (1,3), (2,3), (3,4) — dim 3 common, plays tube in all three. FITS ALL 6 QUARKS to < 1%.** Documented in [quark-search.md §9](quark-search.md); verified by [scripts/quark_search_user_topology.py](../scripts/quark_search_user_topology.py). Max |Δ%| = **0.499%**. Geometry: L_4 = 0.007 fm, L_2 = 0.91 fm, L_1 = 181 fm, L_3 ≳ 5740 fm. **All 6 quarks at (m_t, m_r) ∈ {(1, 1), (1, 2)} — the valid closure modes per [sheet-proton clover-quarks §12](../../sheet-proton/work/clover-quarks.md).** Lighter quark of each gen at (1, 2), heavier at (1, 1). σ_eff per pair = 1.684, 1.932, 1.976 (the heaviest pair sits essentially at R53's σ_eff ≈ 2 magic-shear value).
- [x] **Architectural implication**: tube/ring is per-pair structural choice, not size-determined ([architecture.md §3.1, §3.2](architecture.md) updated).
- [ ] **Cross-term sparsity pattern**: the fit pins each pair's σ_eff = σ + 2τ; many (σ, τ ∈ {±1/3, ±2/3}) combinations give the same f. Choose the canonical assignment.
- [ ] **Phase 2 prep**: e-sector inherits L_2, L_3, L_4. Electron pairs (2,4), (3,5), (4,5) must reproduce (m_e, m_μ, m_τ) using these + L_5 + per-pair (σ, τ, χ).
- [ ] **ν-sector viability concern (raised by user)**: ν masses (30–60 meV) require L_R ≳ mm in any regime. If Phase 2 fits L_5 at fm–pm scale (likely from electron-mass constraints), the ν pair (5, 6) needs L_6 to be macroscopic (mm or larger), which is a 10⁶× jump from the rest of the spectrum. See [quark-search.md §11](quark-search.md). To be addressed during Phase 3 once Phase 2 pins L_5.

### Path B (fallback): 3-dim topology with relaxations

- [x] **Relaxation 1 (allow m_t = 2 as second-lowest mode per pair) + per-pair tube/ring**: tested across 384 configurations on the original (1,2)(1,3)(2,3) topology. Documented in [quark-search.md §10](quark-search.md); verified by [scripts/quark_search_relaxation_1.py](../scripts/quark_search_relaxation_1.py).
- Result: **5 configurations fit all 6 quarks within 5%** (best: 3.97%). All require both relaxations simultaneously; neither alone closes the obstruction. L's span 7 orders of magnitude (L_1 = 0.0073 fm, L_2 = 1.05 fm, L_3 = 80 μm). Less clean than Path A (4× worse fit, more complex per-pair choices) but viable.
- Kept as fallback in case Path A runs into trouble in Phase 2/3 (e.g., the ν concern above).

## Phase 2 — Electron sector

- [ ] Identify the **3 dims that electrons access** (which may include some shared with the quark sector — the e-p sharing hypothesis from [ma-share.md §2](ma-share.md)).
- [ ] **Solve for the electron, muon, and tau modes** using the lowest-closure-mode rule (per the working assumption that lowest-closure-meeting modes are the observable particles).
- [ ] Determine whether the electron dim-pairs need **clover-style internal structure** (e.g., a doublet analog of the lobe/saddle distinction in the quark sector). Open question — may or may not be needed depending on whether all 3 charged leptons can be reached with just the bare 2D-mode formula.
- [ ] Determine whether the electron dim-pairs need their own **twist** (a τ-equivalent for the e-sheet). Currently unclear; R53's mechanism uses *shear* (σ ≈ 2), not τ, so the answer may be "no twist, only shear" — but worth checking explicitly.
- [ ] Write `work/electron-sector.md` with the dim assignment, mass-prediction, and verdict on doublet / twist questions.

## Phase 3 — Neutrino sector

- [ ] **Keep the neutrino sheet at 2 dimensions** until evidence forces extension. The existing R49 / R61 / model-F mass eigenstate structure (3 modes from a 2-torus with shear s ≈ 0.022) is taken as the starting point.
- [ ] Check whether the ν-sector dims share with any of the quark or electron sectors. The [ma-share.md §5.3](ma-share.md) result says simple bare sharing fails; the ν-sector may be fully isolated, or share via a dim that doesn't directly participate in the ν-modes.
- [ ] Document the verdict in `work/neutrino-sector.md`.

## Phase 4 — Coherence check

- [ ] Compare the quark / electron / neutrino sector results: do they fit together into a consistent 6-dim domain?
- [ ] Check that the cross-term matrix from Phase 0 is consistent with the dim assignments from Phases 1–3 and the mass-prediction results.
- [ ] Identify the remaining open structural questions (typically: what *enforces* the specific cross-term sparsity pattern? what *enforces* τ = 1/3 vs other k/3 values? what *enforces* the R53 shear values?).
- [ ] Write `work/coherence.md` with the cross-sector summary.

## Phase 5 — Promotion to math derivation

If Phases 1–4 produce coherent preliminary results:

- [ ] Promote from `work/` to `ma-domain/` proper.
- [ ] Establish the project's chapter outline (analogous to how [metric-charge](../../metric-charge/) and [metric-binding](../../metric-binding/) are organized).
- [ ] Begin formal mathematical derivation: GRID lattice → 6-dim compact Ma domain → cross-term sparsity rules → particle spectrum → SM phenomenology.

If preliminary results do *not* cohere, document the obstructions and consider:

- Whether the 6-dim count is wrong (try 5 or 7).
- Whether the cross-term template needs different structure (more or fewer non-zero off-diagonals; different types).
- Whether the architectural reframe should be abandoned and sheet-proton un-paused.

---

## Inherited working assumptions

These are imported from sheet-proton / model-F and used as given by this project:

| Mechanism | Source | Treatment in ma-domain |
|---|---|---|
| τ = 1/3 twist gives Q_lobe = +2/3, Q_saddle = −1/3 per-arc charges (clover-quarks) | [sheet-proton clover-quarks.md §11](../../sheet-proton/work/clover-quarks.md) | Inherited; applied to 3 quark-bearing dim-pairs. |
| Proton, neutron path-windings (1, 2), (1, 1) in (n_t, n_r) tube-first | [sheet-proton clover-quarks.md §12](../../sheet-proton/work/clover-quarks.md) | Inherited as the baryon-composition rule. |
| R53 shear-resonance produces three charged-lepton masses from a single sheet at (ε_e, s_e) | [studies/R53-three-generations](../../studies/R53-three-generations) | Inherited; applied to the e-sector dim assignment. |
| Three neutrino mass eigenstates from R49 / R61 2-torus | [studies/R49](../../studies/), [studies/R61](../../studies/) | Inherited as the ν-sector starting point. |
| α = α_Coulomb structural from tube↔ℵ↔t chain (model-F) | [models/model-F.md](../../models/model-F.md) | Inherited as the EM-coupling framework. |
| Z₃ confinement and the (3, 6) proton interpretation | [R60 Track 16, 19](../../studies/R60-metric-11) | Inherited as the proton-as-bound-state rule. |

## Inherited open questions

These remain open in this project and may be resolved here or remain open:

- What *enforces* the cross-term sparsity pattern in the 6×6 metric? (GRID lattice rule? Compact-dim topology? Other?)
- What *enforces* the specific shear values (s_e ≈ 2 for charged leptons; s_ν ≈ 0.022 for neutrinos; the various τ = k/3 values)?
- What is the GRID-level mechanism that produces the 6 compact Ma dimensions (cf. [studies/R59-clifford-torus](../../studies/R59-clifford-torus))?

---

## Out of scope

- Mass derivation from first principles (Planck → fermion masses without input). The numerical mass scales are still fitted; this project aims to *unify* the fitting under one architecture, not to remove the fits.
- Neutrino oscillation phenomenology beyond the existing R49 picture.
- Compound-mode (meson, baryon) physics beyond the inherited Z₃ proton structure. The inherited mass formula from clover-mass.md continues to apply where needed.
- Dark-matter inventory under the Compton-window / Q94 hypothesis. Relevant but downstream of the architectural question this project addresses.
