# STATUS.md — ma-domain checklist and work plan

**Status:** Phased plan for the Ma-domain investigation. Hypotheses develop as work files in this `work/` folder; the gate for promoting to the top-level `ma-domain/` (for the mathematical derivation) is a settled, self-consistent architecture.

**Where things stand:** The quark and charged-lepton sectors are solved — the **QY + ED candidate family** ([cand-QY-ED.md](cand-QY-ED.md)) fits all 9 fundamental fermion masses at machine precision, with the K4 member (share-3 spokes) the standout: 4 dims, DOF 1, R1-compliant. The neutrino sector is in active development. The **shear-cleanup** below — truing up a σ_eff over-read that propagated through several files — is done; Phase 4 (tighten and verify the candidate), the decay-rate program (Phase 5), and promotion to derivation (Phase 6) follow.

Notation: `Ma(i, j)` for a dim-pair; `T(m_t, m_r)` for a closure mode. See [architecture.md §2.1](architecture.md).

---

## Shear-cleanup — un-pinning σ_eff — ✓ done

A σ_eff over-read propagated through several files and has been trued up — 11 edits across 6 files. Section retained as the error record and because its closing question feeds Phase 4.

**The error.** "σ_eff = 2 on every sheet — the R53 magic-shear value, structurally forced by the topology" was an over-read. σ_eff is a *free per-sheet fit parameter* — the mass formula contains it (δ = m_r − σ_eff·m_t), and the solver fits one σ_eff per sheet. The K4 report rounds σ_eff to four decimals; reading "2.0000" as exact, and reading the quark sheets' wide ranges as "≈ 2", manufactured a false universal value. **Honest reading:** electron-sheet σ_eff are fit-pinned *near* 2 (to ~10⁻⁴, sheet-dependent — and those 10⁻⁴ deviations are load-bearing, they carry the e/μ/τ mass splits); quark-sheet σ_eff range over O(1) ([1.68, 2.86] etc.). σ_eff = 2 *exactly* is in fact falsified by K4's own fit — it would force m_e = m_μ.

**Scope — no file is useless.** Every work file is a sound excursion; the σ_eff = 2 reading is a framing error layered on real topologies, real machine-precision mass fits, and sound geometric constructions. The cleanup is a *true-up*, not an archival — no `old/` folder is needed.

**True-up todos — all complete:**

- [x] **cand-QY-ED.md** — most affected. Corrected §3, §4, and §5 (family-table row + narrative). Replaced with: σ_eff is a free per-sheet fit parameter; electron-sheet values pin near 2 with load-bearing ~10⁻⁴ structure; the "structural R53" reading is withdrawn. (5 edits.)
- [x] **candidates.md** — dropped the "pins all three electron σ_eff to ≈ 2 structurally" clause from the K4-standout sentence.
- [x] **baryon-number.md** — dropped the "structural σ_eff = 2" citation as a third K4-distinguishing reason; the cut/cycle argument stands without it.
- [x] **electron-tube.md** — clarified σ_eff = 2 is the *clean value of the mass formula* (δ = 0 for T(1, 2)), which the electron sheets land *near* — not a structurally-forced exact value.
- [x] **config-electron.md** — kept σ_eff = 2 only as an optional constraint one *could* impose; noted the "structural" over-read is withdrawn.
- [x] **tube-function.md (§5.1)** — added a note pointing at this section. **leakage-rate.md** — verified (grep) to need no edit: it never asserts σ_eff = 2 and is already caveated.

**Confirmed solid — no action.** These either treat σ_eff correctly (as a free per-pair fit parameter) or do not touch it: architecture.md, cand-QY-EL.md, cand-QY-EY.md (which already carries the correct caution that underdetermined-fit σ_eff values are "not a structural result"), cand-QD-EY.md, config-quark.md (explicitly "not load-bearing for QY's fit"), config-neutrino.md, mode-stability.md, neutrino-1D.md, quark-search.md, anomalous-moment.md, 3-torus.md, ma-share.md.

**The deeper question this leaves open** (not a cleanup task — feeds the Phase 4 cross-term item): is σ_eff genuinely a free per-sheet metric parameter, or determined by independent physics? If determined, K4 is over-determined (4 dims vs 9 masses) — a real pass/fail test.

**Update — uniform-shear test run** ([scripts/uniform_shear_test.py](../scripts/uniform_shear_test.py), [outputs/uniform_shear_test.txt](../outputs/uniform_shear_test.txt)): all three QY-ED members were re-fit with the shear tied to a *single* value — both as one bare shear σ (σ_eff = σ + c·τ per sector) and as one σ_eff shared verbatim — sweeping every discrete combo. Every member fails: best worst-mass error 39–243%, against machine precision when σ_eff is free per sheet. So a *globally uniform* shear is excluded outright, and the per-sheet shear freedom is confirmed load-bearing — not a fit artifact. The open question narrows: σ_eff is either a genuinely free per-sheet parameter, or fixed by physics that **varies per sheet**; a single shear constant is dead. The model-F mass-formula discrepancy still needs settling.

---

## Phase 0 — Nomenclature & setup — ✓ done

- Metric naming convention, pair-label `Ma(i, j)` notation, per-pair tube/ring rule, plane-over-diagonal sheet-constraining rule. [architecture.md §1–§3](architecture.md).

## Phase 1 — Quark sector — ✓ done

- **QY (quark wye)** — 4 dims, hub + 3 spokes — hosts all 6 quarks at machine precision. [config-quark.md](config-quark.md), [quark-search.md §9](quark-search.md).
- **QD (quark delta)** — falsified: a 3-dim delta cannot host the 6 quark masses; the compound-3D-mode rescue fails at 1784%. [config-quark.md](config-quark.md) QD, [cand-QD-EY.md](cand-QD-EY.md).

## Phase 2 — Electron sector — ✓ done

- **ED (electron delta)** — three pairs, one charged lepton each at T(1, 2) — hosts e, μ, τ at machine precision. [config-electron.md](config-electron.md), [cand-QY-ED.md](cand-QY-ED.md).
- **EL (electron path)** and **EY (electron wye)** catalogued as alternatives; ED is the working choice.

## Phase 3 — Neutrino sector — in progress

- Config options **NS** (2D sheet), **NC** (1D shaped curve), **ND** (delta) catalogued in [config-neutrino.md](config-neutrino.md); the 1D-substrate route developed in [neutrino-1D.md](neutrino-1D.md).
- [ ] Settle the neutrino topology and how it couples to the charged sectors (working hypothesis: coupling to the three corners of the electron delta).

## Phase 4 — Candidate consolidation & constraint-tightening — current work

The quark+electron architecture is the **QY + ED family** ([cand-QY-ED.md](cand-QY-ED.md)): the electron delta shares 1, 2, or 3 quark-wye spokes; **K4 (share-3)** is the standout — 4 dims, DOF 1, R1-compliant. [candidates.md](candidates.md) holds the formation rules (R1) and the candidate index; the solver is [scripts/cand_solver.py](../scripts/cand_solver.py).

Remaining work to pin and verify the candidate:

- [x] **σ/τ decomposition.** The solver fits a composite σ_eff per sheet and reports the split σ_eff = σ + (monodromy)·τ per sector (quark clover τ = 1/3, c = 2; electron ellipse τ = 2, c = 1). The decomposition *machinery* is sound. **Its earlier conclusion — "electron σ ≈ 0; a universal σ_eff = 2" — is withdrawn as an over-read** (see the shear-cleanup section). Honest reading: σ_eff is a free per-sheet fit parameter — electron-sheet values pin near 2 to ~10⁻⁴, quark-sheet values range over O(1).
- [x] **Shared-dim metric consistency.** Worked for K4 in [cand-QY-ED.md §4.2](cand-QY-ED.md). Shape is the sectional curvature of a sheet's 2-torus, so the shapes of distinct sheets sharing a dimension are independent curvature components; the only genuine requirement is one size L per dimension, which the solver already enforces — so **K4 passes**, as do all family members. Lesson for the cross-term step and Phase 6: [architecture.md §3.4](architecture.md)'s pair-metric form writes the shape into a per-dimension diagonal entry; it should be revised or demoted so the metric carries shape per sheet (pair).
- [ ] **Cross-term sparsity / what fixes σ, τ.** *Open — the earlier "working answer" (σ_eff = 2 on every sheet) is withdrawn; see the shear-cleanup section.* The question is now sharper: **is σ_eff a genuinely free per-sheet metric parameter, or is it determined by independent physics?** The solver treats it as free — which is the whole reason K4 carries a DOF-1 family (10 fitted parameters: 4 dims + 6 σ_eff, against 9 masses). If σ_eff is instead determined, K4 becomes 4 dims vs 9 masses — over-determined by 5. **Partial result:** the uniform-shear test ([scripts/uniform_shear_test.py](../scripts/uniform_shear_test.py), [outputs/uniform_shear_test.txt](../outputs/uniform_shear_test.txt)) has run the constrained-shear fit — a single shear value across the topology fails the whole QY-ED family by 39–243%, against machine precision with σ_eff free per sheet. A uniform shear *law* is therefore excluded; if σ_eff is determined, the determining physics must vary per sheet. Settling this also needs the model-F mass-formula discrepancy resolved (does model-F pin a sheet's diagonal shear-independently, as recalled?). The off-diagonal *sparsity* pattern proper — which g_{ij} vanish — is downstream of this.

**Note on DOF.** K4's DOF = 1 — 10 fitted parameters (4 dims + 6 σ_eff) against 9 masses — is the benign hub-style freedom: the one free direction is a dimension free above a size floor, entering the masses only through a negligible 1/L term. But the count *includes the 6 shears as free parameters* (see the Cross-term item above). "K4 is effectively determined" holds only if the shears are genuinely free metric parameters; if they are determined by other physics, the count — and the claim — change.

## Phase 5 — Decay-rate program

[mode-stability.md](mode-stability.md) — the leakage mechanism and a five-phase plan for deriving decay rates from geometry. Decay rates and lifetimes are the over-constraining observable set (26 orders of magnitude, measured to < 1%) that will further pin the architecture. Phase 1 of that plan — deriving the leakage rate from the resonance pole — is itself mathematical-derivation work and would be an early chapter of the parent-folder arc.

A second precision-observable thread — the anomalous magnetic moment — is scoped in [anomalous-moment.md](anomalous-moment.md): a parked hypothesis file, **off the critical path**, gated on the per-sheet spin account being carried onto the shaped tubes. Its one ungated, useful computation now is mapping the cross-section shape ranges the charge constraints admit.

## Phase 6 — Promotion to math derivation

When the architecture is settled (Phases 3–4 closed):

- [ ] Promote from `work/` to `ma-domain/` proper; establish the chapter outline (analogous to [metric-charge](../../metric-charge/), [metric-binding](../../metric-binding/)).
- [ ] Formal derivation: GRID lattice → N-dim compact Ma domain → cross-term structure → particle spectrum → decay rates → SM phenomenology.

If the architecture does *not* cohere, document the obstructions and reconsider the dim count, the cross-term template, or the architectural reframe itself.

---

## Inherited working assumptions

Imported from sheet-proton / model-F and used as given:

| Mechanism | Source | Treatment |
|---|---|---|
| τ = 1/3 twist gives Q_lobe = +2/3, Q_saddle = −1/3 per-arc charges | [sheet-proton clover-quarks §11](../../sheet-proton/work/clover-quarks.md) | Adopted; applied to the quark-bearing pairs. |
| Proton, neutron path-windings T(1, 2), T(1, 1) tube-first | [sheet-proton clover-quarks §12](../../sheet-proton/work/clover-quarks.md) | Adopted as the baryon-composition rule. |
| Electron tube: convex ellipse; σ_eff = 2 is the clean value where T(1, 2) sits at the floor (δ = 0) | [electron-tube.md](electron-tube.md) | A naturalness reference — *not* an exact pinning. Fitted electron σ_eff land near 2 (~10⁻⁴ off), not at it; see the shear-cleanup section. |
| α = α_Coulomb structural from the tube↔ℵ↔t chain | [models/model-F.md](../../models/model-F.md) | Useful guide; the project may rederive the EM-coupling chain. |
| Z₃ confinement and the (3, 6) proton interpretation | [R60](../../studies/R60-metric-11) | Adopted as the proton-as-bound-state rule. |

## Inherited open questions

- What *enforces* the cross-term sparsity pattern in the metric? (GRID lattice rule? compact-dim topology?)
- What *enforces* the specific σ, τ values per pair? (Still open. The Phase 4 σ/τ decomposition was a first attempt; its "σ_eff = 2" answer was withdrawn — see the shear-cleanup section.)
- What is the GRID-level mechanism that produces the N compact Ma dimensions?

## Out of scope

- Mass derivation from first principles (Planck → fermion masses with no input). The numerical mass scales are fitted; this project unifies the fitting under one architecture.
- Compound-mode (meson, baryon) physics beyond the inherited Z₃ proton structure.
- Dark-matter inventory under the Compton-window hypothesis — downstream of the architectural question.
