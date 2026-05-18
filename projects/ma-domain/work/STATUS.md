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

### Path A (preferred): wye/star topology Ma((1,4), (2,4), (3,4))

- [x] **First-cut attempt: 3-dim triangle topology `Ma((1,2), (1,3), (2,3))`.** Analytically + numerically falsified in [quark-search.md §1–§7](quark-search.md). The dim-sharing constraint was the obstruction.
- [x] **Wye topology: 4 dims with pairs `Ma((1,4), (2,4), (3,4))` — m4 is the common hub, plays tube in all three pairs. FITS ALL 6 QUARKS to < 1%.** Documented in [quark-search.md §9](quark-search.md); verified by [scripts/quark_search_wye.py](../scripts/quark_search_wye.py). Max |Δ%| = **0.499%**. Geometry: L_1 = 0.007 fm, L_2 = 0.91 fm, L_3 = 181 fm, L_4 ≳ 5740 fm. **All 6 quarks at (m_t, m_r) ∈ {(1, 1), (1, 2)} — the valid closure modes per [sheet-proton clover-quarks §12](../../sheet-proton/work/clover-quarks.md).** Lighter quark of each gen at T(1, 2), heavier at T(1, 1). σ_eff per pair = 1.684, 1.932, 1.976 (the heaviest pair sits essentially at R53's σ_eff ≈ 2 magic-shear value).
- [x] **Architectural implication**: tube/ring is per-pair structural choice, not size-determined ([architecture.md §3.1, §3.2](architecture.md) updated).
- [ ] **Cross-term sparsity pattern**: the fit pins each pair's σ_eff = σ + 2τ; many (σ, τ ∈ {±1/3, ±2/3}) combinations give the same f. Choose the canonical assignment.
- [ ] **Phase 2 prep**: e-sector inherits some subset of L_1, L_2, L_3, L_4. Electron pairs (chosen from the dim pool) must reproduce (m_e, m_μ, m_τ) using these + L_5 + per-pair (σ, τ, χ).
- [ ] **ν-sector viability concern**: ν masses (30–60 meV) require L_R ≳ mm in any regime. If Phase 2 fits L_5 at fm–pm scale (likely from electron-mass constraints), the ν pair (and/or any additional ν dims) needs at least one macroscopic dim, a 10⁶× jump from the rest of the spectrum. See [quark-search.md §11](quark-search.md). Resolved in Candidate C by giving the ν sector its own ν-region dims (m6, m7) free of inherited e-scale constraints.

### Path B (fallback): 3-dim topology with relaxations

- [x] **Relaxation 1 (allow m_t = 2 as second-lowest mode per pair) + per-pair tube/ring**: tested across 384 configurations on the original triangle topology `Ma((1,2), (1,3), (2,3))`. Documented in [quark-search.md §10](quark-search.md); verified by [scripts/quark_search_relaxation_1.py](../scripts/quark_search_relaxation_1.py).
- Result: **5 configurations fit all 6 quarks within 5%** (best: 3.97%). All require both relaxations simultaneously; neither alone closes the obstruction. L's span 7 orders of magnitude. Less clean than Path A (4× worse fit, more complex per-pair choices) but viable.
- Kept as fallback in case Path A runs into trouble in Phase 2/3.

---

## Active candidate comparison ([candidates.md](candidates.md))

Three current Path A topology variants tracked. Numerics in [outputs/candidate_fits.txt](../outputs/candidate_fits.txt); driver in [scripts/candidate_fits.py](../scripts/candidate_fits.py). All use size-ordered dim labels (m1 smallest).

| Candidate | Quark | Electron | ν | Total dims |
|---|---|---|---|---:|
| **A — wye + path** | `Ma((1,4),(2,4),(3,4))` | `Ma((1,2),(1,5),(4,5))` (4-dim path) | `Ma(5,6)` | 6 |
| **B — wye + delta** | `Ma((1,4),(2,4),(3,4))` | `Ma((1,2),(1,5),(2,5))` (delta) | `Ma(5,6)` | 6 |
| **C — wye + delta + delta** | `Ma((1,4),(2,4),(3,4))` | `Ma((1,2),(1,5),(2,5))` (delta) | `Ma((5,6),(5,7),(6,7))` (delta) | 7 |

| Sector | A | B | C |
|---|:---:|:---:|:---:|
| Quark fit | ✓ 0.5% | ✓ 0.5% | ✓ 0.5% |
| Electron fit | not tested | ✓ 0.0% | ✓ 0.0% |
| ν fit (strict modes) | ✗ (1 pair → 2 modes < 3 ν) | ✗ same | ✓ 0.0% |
| ν fit (sign-flipped modes, L_5 ≳ cm) | unknown | ~1% (spot check) | not needed |

**Working choice:** **Candidate C** as the active topology. Cleanest fit, no mode-relaxations needed in any sector. Cost: 1 extra dim (7 vs 6). Candidate B held as a 6-dim fallback.

### Open: refactor candidates for natural mass-scale ↔ dim-size matching

- [ ] **Revisit which quark dims the electron sector reuses.** The current `Ma((1,2), (1,5), (2,5))` topology in B/C uses the two SMALLEST quark rings (m1 = 0.007 fm, m2 = 0.91 fm). That mathematically closes to machine precision but only by driving σ_eff to within ~10⁻⁶ of the R53 magic-shear value 2 — an extreme fine-tuning. The physically natural pairing would put the electron sector on m3 (181 fm, ≈ electron Compton scale) and m4 (5740 fm, the quark hub): topology `Ma((3,4), (3,5), (4,5))`. That alternative would give σ_eff ≈ 1.92 — comfortably off-resonance — matching the quark-sector σ_eff range. Untested.
- [ ] **Guiding principle to apply when redoing the candidate set:** smallest dims associate with the heaviest particles, largest dims with the lightest. The quark wye already satisfies this within its own sector (m1 hosts t/b, m3 hosts u/d). The same principle should pick which quark dims propagate into the e-sector and ν-sector.
- [ ] **Define the refreshed candidate set in-place** in [candidates.md](candidates.md) — don't spawn new variant files. Replace or augment the A/B/C set with the natural-scale variants; preserve the historical numbers but flag them clearly as superseded.

## Phase 2 — Electron sector

- [x] **Working topology**: electron delta `Ma((1,2), (1,5), (2,5))` under Candidates B/C — three pairs hosting one charged lepton each at T(1, 2). All three (m_e, m_μ, m_τ) fit to machine precision via the per-pair σ_eff with L_5 in the 10⁵-fm (~0.1 mm) range. The system is underdetermined, so multiple lepton↔pair assignments work; e.g. τ → `Ma(1, 2)`, e → `Ma(1, 5)`, μ → `Ma(2, 5)`.
- [ ] Verify the electron-sector dim assignment is structurally coherent with the quark sector's shared dims (m1 and m2 are also quark rings; the e-sector reuses them as one tube + one ring per e-pair).
- [ ] Determine whether the electron dim-pairs need **clover-style internal structure** (e.g., a doublet analog of the lobe/saddle distinction in the quark sector). Open question — the current fit treats each pair as a single-mode host (one lepton per pair), no doublet required.
- [ ] Determine whether the electron dim-pairs need their own **twist** (a τ-equivalent for the e-sheet). The current fit uses σ_eff per pair without separately resolving (σ, τ); R53's mechanism uses *shear* (σ ≈ 2), not τ, so the answer may be "no twist, only shear" — but worth confirming.
- [ ] Promote the e-sector results from [candidates.md](candidates.md) into a dedicated `work/electron-sector.md`.

## Phase 3 — Neutrino sector

- [x] **Working topology (Candidate C)**: ν delta `Ma((5,6), (5,7), (6,7))` — three pairs each hosting one ν mass eigenstate at T(1, 2). Fit closes to machine precision with L_5 inherited from e-sector; L_6 and L_7 land in the cm–m range (one valid solution has L_6 ≈ 260 m, L_7 ≈ 4 cm; the m6–m7 labelling is symmetric so the two free parameters can swap across runs).
- [ ] **Alternative (Candidate B fallback)**: single ν pair `Ma(5, 6)` with sign-flipped modes per metric-charge ch. 4 (T(1, 1), T(−1, 1), T(1, 2)) — viable to ~1% with L_5 ≳ 4 cm; trade-off documented in [candidates.md §4](candidates.md).
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
