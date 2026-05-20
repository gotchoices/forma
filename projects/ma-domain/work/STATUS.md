# STATUS.md — ma-domain checklist and work plan

**Status:** Phased plan for the Ma-domain investigation. Hypotheses develop as work files in this `work/` folder; the gate for promoting to the top-level `ma-domain/` (for the mathematical derivation) is a settled, self-consistent architecture.

**Where things stand:** The quark and charged-lepton sectors are solved — the **QY + ED candidate family** ([cand-QY-ED.md](cand-QY-ED.md)) fits all 9 fundamental fermion masses at machine precision, with the K4 member (share-3 spokes) the standout: 4 dims, DOF 1, R1-compliant. The neutrino sector is in active development. The immediate work is Phase 4 — tighten and verify the candidate. The decay-rate program (Phase 5) and promotion to derivation (Phase 6) follow.

Notation: `Ma(i, j)` for a dim-pair; `T(m_t, m_r)` for a closure mode. See [architecture.md §2.1](architecture.md).

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

The quark+electron architecture is the **QY + ED family** ([cand-QY-ED.md](cand-QY-ED.md)): the electron delta shares 1, 2, or 3 quark-wye spokes; **K4 (share-3)** is the standout — 4 dims, DOF 1, R1-compliant, electron σ_eff structurally pinned to ≈ 2. [candidates.md](candidates.md) holds the formation rules (R1) and the candidate index; the solver is [scripts/cand_solver.py](../scripts/cand_solver.py).

Remaining work to pin and verify the candidate:

- [ ] **σ/τ decomposition.** The solver fits a composite σ_eff per sheet; σ_eff = σ + (monodromy)·τ. Decompose it into shear σ and twist τ using each sector's posited cross-section construction (quark clover τ = 1/3 → Z₃ monodromy; electron ellipse τ = 2 → trivial monodromy), and check consistency — the electron sheets should decompose to the electron-tube's σ = 0. *(Active — solver now reports the decomposition; see [outputs/](../outputs/).)*
- [ ] **Shared-dim metric consistency.** [architecture.md §3.4](architecture.md)'s open question: at a shared dim the diagonal metric g_ii must reduce consistently to *every* sheet's shape function P. K4 shares every spoke across three sheets — verify a single self-consistent 4-dim metric exists. This is the real structural test of K4.
- [ ] **Cross-term sparsity / what fixes σ, τ.** Which off-diagonals are non-zero, and what structural rule (if any) fixes the σ, τ values per pair. Informed by the σ/τ decomposition above.

**Note on DOF.** K4's DOF = 1 is the benign hub-style freedom — one dimension is free above a size floor (it enters the masses only through a negligible 1/L term), exactly as the quark wye's hub is. The topology, the particle→leg assignment, and the small dims are all pinned. So K4 is effectively determined for architectural purposes; the σ/τ and metric-consistency checks verify self-consistency rather than remove the free direction.

## Phase 5 — Decay-rate program

[mode-stability.md](mode-stability.md) — the leakage mechanism and a five-phase plan for deriving decay rates from geometry. Decay rates and lifetimes are the over-constraining observable set (26 orders of magnitude, measured to < 1%) that will further pin the architecture. Phase 1 of that plan — deriving the leakage rate from the resonance pole — is itself mathematical-derivation work and would be an early chapter of the parent-folder arc.

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
| Electron tube: convex ellipse, τ = 2, σ = 0 → σ_eff = 2 puts T(1, 2) at the floor | [electron-tube.md](electron-tube.md) | Adopted for charged-lepton sheets. |
| α = α_Coulomb structural from the tube↔ℵ↔t chain | [models/model-F.md](../../models/model-F.md) | Useful guide; the project may rederive the EM-coupling chain. |
| Z₃ confinement and the (3, 6) proton interpretation | [R60](../../studies/R60-metric-11) | Adopted as the proton-as-bound-state rule. |

## Inherited open questions

- What *enforces* the cross-term sparsity pattern in the metric? (GRID lattice rule? compact-dim topology?)
- What *enforces* the specific σ, τ values per pair? (The σ/τ decomposition in Phase 4 is the first concrete attack on this.)
- What is the GRID-level mechanism that produces the N compact Ma dimensions?

## Out of scope

- Mass derivation from first principles (Planck → fermion masses with no input). The numerical mass scales are fitted; this project unifies the fitting under one architecture.
- Compound-mode (meson, baryon) physics beyond the inherited Z₃ proton structure.
- Dark-matter inventory under the Compton-window hypothesis — downstream of the architectural question.
