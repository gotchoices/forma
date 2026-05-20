# STATUS.md — ma-domain checklist and work plan

**Status:** Phased plan for the Ma domain investigation (working dim count N = 6, with N = 5 or 7 admissible if the structure demands it). Each phase produces concrete work files in this directory; coherence across phases is the gate for promoting from `work/` to the top level `ma-domain/` (Phase 5).

Pair notation: `Ma(i, j)` for a single pair (size-ordered, `i < j`); `Ma((i,j), (k,l), …)` for a set of pairs. Dim labels m1..m_N are size-ordered, smallest first. See [architecture.md §2.1](architecture.md).

---

## Phase 0 — Nomenclature & setup

- [x] **Naming convention** for the 11-component metric (4 spacetime + 7 Material = aleph + 6 Ma dims), with Material → Space → Time top-to-bottom and size-ordering within Material. Mode 11-tuple `{ n_aleph, n_1, ..., n_6, n_x, n_y, n_z, n_t }`. Done in [architecture.md §1–§2](architecture.md).
- [x] **Pair-label notation `Ma(i, j)`** distinct from mode-tuple `T(m_t, m_r)`. Done in [architecture.md §2.1](architecture.md).
- [x] **Operational rules** for the per-pair tube/ring assignment and the plane-over-diagonal (2D-planar preferred over 3D-mixed) sheet-constraining rule. Done in [architecture.md §3](architecture.md).
- [ ] **Cross-term sparsity pattern**: which of the 15 off-diagonals in the 6×6 Material block are non-zero, and what type (τ-twist, shear, other) each carries. Provisional list:
  - 3 cross-terms with τ = 1/3 → quark planes
  - Up to 3 cross-terms with shears → charged-lepton planes
  - Remaining cross-terms = 0 → orthogonal dim pairs
  
  See [architecture.md §4](architecture.md) for the open questions this resolution will address.

## Phase 1 — Quark sector

Two parallel paths now run in parallel:

### Path A (preferred): wye/star topology Ma((1,5), (3,5), (4,5))

- [x] **First-cut attempt: 3-dim triangle topology `Ma((1,2), (1,3), (2,3))`.** Analytically + numerically falsified in [quark-search.md §1–§7](quark-search.md). The dim-sharing constraint was the obstruction.
- [x] **Wye topology: 4 dims with pairs `Ma((1,5), (3,5), (4,5))` — m5 is the common hub (m2 is reserved for the e-sector). FITS ALL 6 QUARKS to < 1%.** Documented in [quark-search.md §9](quark-search.md); verified by [scripts/cand_solver.py](../scripts/cand_solver.py). Max |Δ%| = **0.499%** (pure-ring analytic estimate; the joint solve closes it to machine precision). Geometry: L_1 = 0.007 fm, L_3 = 0.91 fm, L_4 = 181 fm, L_5 ≳ 5740 fm. **All 6 quarks at (m_t, m_r) ∈ {(1, 1), (1, 2)} — the valid closure modes per [sheet-proton clover-quarks §12](../../sheet-proton/work/clover-quarks.md).** Lighter quark of each gen at T(1, 2), heavier at T(1, 1). σ_eff per pair = 1.684, 1.932, 1.976 (the heaviest pair sits essentially at R53's σ_eff ≈ 2 magic-shear value).
- [x] **Architectural implication**: tube/ring is per-pair structural choice, not size-determined ([architecture.md §3.1, §3.2](architecture.md) updated).
- [ ] **Cross-term sparsity pattern**: the fit pins each pair's σ_eff = σ + 2τ; many (σ, τ ∈ {±1/3, ±2/3}) combinations give the same f. Choose the canonical assignment.
- [x] **Phase 2 prep**: e-sector reuses L_4, L_5 from the quark wye and adds L_2 ≈ 0.7 fm. e-delta `Ma((2,4), (2,5), (4,5))` fits to machine precision with σ_eff in the natural range. Details in [candidates.md §2, §3](candidates.md).
- [x] **ν-sector viability concern**: resolved in Candidate C by giving the ν-delta its own fresh dims `Ma((6,7), (6,8), (7,8))` decoupled from the e-sector. L_6, L_7, L_8 land in the cm-m range.

### Path B (fallback): 3-dim topology with relaxations

- [x] **Relaxation 1 (allow m_t = 2 as second-lowest mode per pair) + per-pair tube/ring**: tested across 384 configurations on the original triangle topology `Ma((1,2), (1,3), (2,3))`. Documented in [quark-search.md §10](quark-search.md); verified by [scripts/quark_search_relaxation_1.py](../scripts/quark_search_relaxation_1.py).
- Result: **5 configurations fit all 6 quarks within 5%** (best: 3.97%). All require both relaxations simultaneously; neither alone closes the obstruction. L's span 7 orders of magnitude. Less clean than Path A (4× worse fit, more complex per-pair choices) but viable.
- Kept as fallback in case Path A runs into trouble in Phase 2/3.

---

## Active candidate comparison ([candidates.md](candidates.md))

Three current Path A topology variants tracked. Solved by [scripts/cand_solver.py](../scripts/cand_solver.py) from per-candidate specs in [scripts/cand_specs/](../scripts/cand_specs/); reports written to `outputs/cand_<name>.txt`. All use size-ordered dim labels (m1 smallest, m8 largest in C).

| Candidate | Quark | Electron | ν | Total dims |
|---|---|---|---|---:|
| **A — wye + path** | `Ma((1,5),(3,5),(4,5))` | `Ma((1,3),(1,2),(2,5))` (4-dim path) | `Ma(6,7)` | 7 |
| **B — wye + delta** | `Ma((1,5),(3,5),(4,5))` | `Ma((2,4),(2,5),(4,5))` (delta) | `Ma(6,7)` | 7 |
| **C — wye + delta + delta** | `Ma((1,5),(3,5),(4,5))` | `Ma((2,4),(2,5),(4,5))` (delta) | `Ma((6,7),(6,8),(7,8))` (delta) | 8 |

| Sector | A | B | C |
|---|:---:|:---:|:---:|
| Quark fit | ✓ 0.5% | ✓ 0.5% | ✓ 0.5% |
| Electron fit (natural σ_eff) | not tested | ✓ 0.0% | ✓ 0.0% |
| ν fit (strict modes) | ✗ (1 pair → 2 modes < 3 ν) | ✗ same | ✓ 0.0% |
| ν fit (sign-flipped modes, L_6 ≳ cm) | unknown | ~1% (spot check) | not needed |

**Working choice:** **Candidate C** as the active topology. All twelve charged fermions + 3 ν mass eigenstates fit to machine precision (modulo 0.5% on u). σ_eff values in a natural range (1.00 to 1.98) across all sectors. No mode-relaxations needed. Cost: 8 dims. Candidate B held as a 7-dim fallback.

### Refactor for natural mass-scale ↔ dim-size matching

- [x] **Revisit which quark dims the electron sector reuses.** Done. The e-delta in B/C is now `Ma((2,4), (2,5), (4,5))` using the larger quark-region dims (m4 = 181 fm, m5 = 5740 fm) plus a new m2 ≈ 0.7 fm (lepton-scale). Closes to machine precision with σ_eff = 1.932, 1.000, 1.941 — all natural, no R53 fine-tuning. Details in [candidates.md §2, §3](candidates.md).
- [x] **Re-fit C's ν-delta on fresh dims.** Done. The ν-delta is now `Ma((6,7), (6,8), (7,8))` (8 dims total). Closes to machine precision with L_6 ≈ 7 cm, L_7 ≈ 2 cm, L_8 ≈ 4 cm.
- [x] **Apply a strict size-ordering relabeling pass.** Done. The size hierarchy is now m1 = 0.007 fm; m2 = 0.7 fm; m3 = 0.91 fm; m4 = 181 fm; m5 = 5740 fm; m6..m8 = ν dims. All `Ma(i, j)` references throughout the project use these labels.

## Phase 2 — Electron sector

- [x] **Working topology**: electron delta `Ma((2,4), (2,5), (4,5))` under Candidates B/C — three pairs hosting one charged lepton each at T(1, 2). All three (m_e, m_μ, m_τ) fit to machine precision via the per-pair σ_eff with L_2 ≈ 0.7 fm (set by the τ Compton wavelength). Assignment: τ → `Ma(2, 4)`, μ → `Ma(2, 5)`, e → `Ma(4, 5)`.
- [x] The shared pair `Ma(4, 5)` (in both the quark wye and the e-delta) hosts two different cross-section modes — quark clover (u, d) with σ_eff = 1.684, and electron ellipse with σ_eff = 1.932. Consistent with the pair-triplet (σ, τ, P) hypothesis where the cross-section P is per-mode, not per-pair.
- [ ] Determine whether the electron dim-pairs need **clover-style internal structure** (e.g., a doublet analog of the lobe/saddle distinction in the quark sector). Open question — the current fit treats each pair as a single-mode host (one lepton per pair), no doublet required.
- [ ] Determine whether the electron dim-pairs need their own **twist** (a τ-equivalent for the e-sheet). The current fit uses σ_eff per pair without separately resolving (σ, τ); R53's mechanism uses *shear* (σ ≈ 2), not τ, so the answer may be "no twist, only shear" — but worth confirming.
- [ ] Promote the e-sector results from [candidates.md](candidates.md) into a dedicated `work/electron-sector.md`.

## Phase 3 — Neutrino sector

- [x] **Working topology (Candidate C)**: ν delta `Ma((6,7), (6,8), (7,8))` on fresh dims (decoupled from the e-sector). Three pairs each host one ν mass eigenstate at T(1, 2). Fit closes to machine precision with L_6 ≈ 7 cm, L_7 ≈ 2 cm, L_8 ≈ 4 cm (one valid solution; the indices can swap across seeds since the three pairs are symmetric).
- [ ] **Alternative (Candidate B fallback)**: single ν pair `Ma(6, 7)` with sign-flipped modes per metric-charge ch. 4 (T(1, 1), T(−1, 1), T(1, 2)) — viable to ~1% with L_6 ≳ 4 cm; trade-off documented in [candidates.md §4](candidates.md).
- [ ] **Alternative (1D-curve substrate)**: neutrinos on a 1D closed curve with N=3 shape; the lowest band carries 1 singlet + 1 doublet, matching the three-generation count, with the doublet split by a small C_3 breaking. Unifies with charged leptons via the tiny-tube limit (per-generation Ma(i,j) pair with charged lepton at m_t=1 and neutrino at m_t=0). Theory and development strategy in [neutrino-1D.md](neutrino-1D.md).
- [ ] Check whether the ν-sector dim sizes (cm–m scale) admit a structural justification or are simply free parameters of the architecture.
- [ ] Promote the ν-sector results from [candidates.md](candidates.md) into a dedicated `work/neutrino-sector.md`.

## Phase 4 — Coherence check

- [ ] Compare the quark / electron / neutrino sector results: do they fit together into a consistent N-dim domain?
- [ ] Check that the cross-term matrix from Phase 0 is consistent with the dim assignments from Phases 1–3 and the mass-prediction results.
- [ ] Identify the remaining open structural questions (typically: what *enforces* the specific cross-term sparsity pattern? what *enforces* τ = 1/3 vs other k/3 values? what *enforces* the shear values?).
- [ ] Write `work/coherence.md` with the cross-sector summary.

## Phase 5 — Promotion to math derivation

If Phases 1–4 produce coherent preliminary results:

- [ ] Promote from `work/` to `ma-domain/` proper.
- [ ] Establish the project's chapter outline (analogous to how [metric-charge](../../metric-charge/) and [metric-binding](../../metric-binding/) are organized).
- [ ] Begin formal mathematical derivation: GRID lattice → N-dim compact Ma domain → cross-term sparsity rules → particle spectrum → SM phenomenology.

If preliminary results do *not* cohere, document the obstructions and consider:

- Whether the working dim count is wrong (move from 6 to 5 or 7 — Candidate C already at 7).
- Whether the cross-term template needs different structure (more or fewer non-zero off-diagonals; different types).
- Whether the architectural reframe should be abandoned and sheet-proton un-paused.

---

## Inherited working assumptions

These are imported from sheet-proton / model-F and used as given by this project:

| Mechanism | Source | Treatment in ma-domain |
|---|---|---|
| τ = 1/3 twist gives Q_lobe = +2/3, Q_saddle = −1/3 per-arc charges (clover-quarks) | [sheet-proton clover-quarks.md §11](../../sheet-proton/work/clover-quarks.md) | Adopted as input; applied to the quark-bearing dim-pairs. |
| Proton, neutron path-windings T(1, 2), T(1, 1) tube-first | [sheet-proton clover-quarks.md §12](../../sheet-proton/work/clover-quarks.md) | Adopted as the baryon-composition rule. |
| R53 shear-resonance suggests three charged-lepton masses from a single sheet at extreme (ε, s) | [studies/R53-three-generations](../../studies/R53-three-generations) | Used as orientation; this project's e-sector instead uses a delta of 3 pairs each hosting one lepton. |
| Three neutrino mass eigenstates from R49 / R61 2-torus | [studies/R49](../../studies/), [studies/R61](../../studies/) | Used as orientation; Candidate C's ν-sector uses a delta of 3 pairs each hosting one mass eigenstate (no shear-resonance trio required). |
| α = α_Coulomb structural from tube↔ℵ↔t chain (model-F) | [models/model-F.md](../../models/model-F.md) | Useful guide; the project may rederive the EM-coupling chain in its own architecture. |
| Z₃ confinement and the (3, 6) proton interpretation | [R60 Track 16, 19](../../studies/R60-metric-11) | Adopted as the proton-as-bound-state rule. |

## Inherited open questions

These remain open in this project and may be resolved here or remain open:

- What *enforces* the cross-term sparsity pattern in the N×N metric? (GRID lattice rule? Compact-dim topology? Other?)
- What *enforces* the specific shear values (σ_eff ≈ 2 for charged leptons; the various τ = k/3 values for quarks; the cm-scale L's for neutrinos)?
- What is the GRID-level mechanism that produces the N compact Ma dimensions (cf. [studies/R59-clifford-torus](../../studies/R59-clifford-torus))?

---

## Out of scope

- Mass derivation from first principles (Planck → fermion masses without input). The numerical mass scales are still fitted; this project aims to *unify* the fitting under one architecture, not to remove the fits.
- Neutrino oscillation phenomenology beyond what falls out of the chosen ν topology.
- Compound-mode (meson, baryon) physics beyond the inherited Z₃ proton structure. The inherited mass formula from clover-mass.md continues to apply where needed.
- Dark-matter inventory under the Compton-window / Q94 hypothesis. Relevant but downstream of the architectural question this project addresses.
