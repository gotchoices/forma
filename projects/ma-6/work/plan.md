# plan.md — ma-6 work plan

**Status:** Phased plan for the 6-dim Ma domain investigation. Each phase produces concrete work files in this directory; coherence across phases is the gate for promoting from `work/` to the top level `ma-6/` (Phase 5).

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

- [ ] Identify the **3 dims that the quarks access**. These are the dim-pairs that carry the τ = 1/3 twist (per the inherited clover-quarks 1/3-twist mechanism from [sheet-proton clover-quarks.md](../../sheet-proton/work/clover-quarks.md)).
- [ ] Decide whether the 3 twists are **independent** (one τ per pair, different k allowed) or **mutually constrained** (all three τ = 1/3, same k forced by some structural rule). Working hypothesis: mutually constrained, since the quark generations all have the same Z₃-singlet structure.
- [ ] Find the **range of scales** for the three p-dims that works for the three quark generations. Constraints:
  - Each generation's (tube, ring) dim-pair must give a 2D-mode mass at the right scale.
  - Up vs down within a generation comes from the clover-arc charge mechanism (+2/3 lobe / −1/3 saddle), per [sheet-proton clover-quarks.md §11](../../sheet-proton/work/clover-quarks.md). Inherited from sheet-proton, not re-derived.
- [ ] Determine whether the 3 quark dims **completely pin** the scale ratios or leave degrees of freedom. (Hopefully not fully pinned — leaves room for the electron and ν sectors to share dims.)
- [ ] Write `work/quark-sector.md` with the dim assignment, the mass-prediction, and the (ε, χ, σ) free-parameter analysis.

## Phase 2 — Electron sector

- [ ] Identify the **3 dims that electrons access** (which may include some shared with the quark sector — the e-p sharing hypothesis from [ma-share-6.md §2](ma-share-6.md)).
- [ ] **Solve for the electron, muon, and tau modes** using the lowest-closure-mode rule (per the working assumption that lowest-closure-meeting modes are the observable particles).
- [ ] Determine whether the electron dim-pairs need **clover-style internal structure** (e.g., a doublet analog of the lobe/saddle distinction in the quark sector). Open question — may or may not be needed depending on whether all 3 charged leptons can be reached with just the bare 2D-mode formula.
- [ ] Determine whether the electron dim-pairs need their own **twist** (a τ-equivalent for the e-sheet). Currently unclear; R53's mechanism uses *shear* (σ ≈ 2), not τ, so the answer may be "no twist, only shear" — but worth checking explicitly.
- [ ] Write `work/electron-sector.md` with the dim assignment, mass-prediction, and verdict on doublet / twist questions.

## Phase 3 — Neutrino sector

- [ ] **Keep the neutrino sheet at 2 dimensions** until evidence forces extension. The existing R49 / R61 / model-F mass eigenstate structure (3 modes from a 2-torus with shear s ≈ 0.022) is taken as the starting point.
- [ ] Check whether the ν-sector dims share with any of the quark or electron sectors. The [ma-share-6.md §5.3](ma-share-6.md) result says simple bare sharing fails; the ν-sector may be fully isolated, or share via a dim that doesn't directly participate in the ν-modes.
- [ ] Document the verdict in `work/neutrino-sector.md`.

## Phase 4 — Coherence check

- [ ] Compare the quark / electron / neutrino sector results: do they fit together into a consistent 6-dim domain?
- [ ] Check that the cross-term matrix from Phase 0 is consistent with the dim assignments from Phases 1–3 and the mass-prediction results.
- [ ] Identify the remaining open structural questions (typically: what *enforces* the specific cross-term sparsity pattern? what *enforces* τ = 1/3 vs other k/3 values? what *enforces* the R53 shear values?).
- [ ] Write `work/coherence.md` with the cross-sector summary.

## Phase 5 — Promotion to math derivation

If Phases 1–4 produce coherent preliminary results:

- [ ] Promote from `work/` to `ma-6/` proper.
- [ ] Establish the project's chapter outline (analogous to how [metric-charge](../../metric-charge/) and [metric-binding](../../metric-binding/) are organized).
- [ ] Begin formal mathematical derivation: GRID lattice → 6-dim compact Ma domain → cross-term sparsity rules → particle spectrum → SM phenomenology.

If preliminary results do *not* cohere, document the obstructions and consider:

- Whether the 6-dim count is wrong (try 5 or 7).
- Whether the cross-term template needs different structure (more or fewer non-zero off-diagonals; different types).
- Whether the architectural reframe should be abandoned and sheet-proton un-paused.

---

## Inherited working assumptions

These are imported from sheet-proton / model-F and used as given by this project:

| Mechanism | Source | Treatment in ma-6 |
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
