# architecture.md — ma-6 metric layout, nomenclature, and operational rules

**Status:** Phase 0 deliverable (per [plan.md](plan.md)). Pins the conventions used by everything downstream — the 11-component metric ordering, the mode-label nomenclature, and the operational rules that translate a 6-dim Ma domain into closure analysis on dim-pairs.

This file does **not** yet specify the cross-term sparsity pattern (which off-diagonals carry τ-twists, which carry R53 shears, which are zero). That is the second half of Phase 0 and comes after the conventions below are stable.

---

## 1. The 11-component metric ordering

Order the 11 metric components Material → Space → Time, top to bottom:

| # | Component | Type | Role |
|---:|---|---|---|
| 1 | aleph | Material — sub-Ma | mediator dim from R55 / R59; not particle-bearing |
| 2 | m1 | Material — Ma dim 1 (smallest) | smallest compact circumference; hosts the heaviest mass scales |
| 3 | m2 | Material — Ma dim 2 | ... |
| 4 | m3 | Material — Ma dim 3 | ... |
| 5 | m4 | Material — Ma dim 4 | ... |
| 6 | m5 | Material — Ma dim 5 | ... |
| 7 | m6 | Material — Ma dim 6 (largest) | largest compact circumference; hosts the lightest mass scales (ν-region) |
| 8 | Sx | Space | spatial extent |
| 9 | Sy | Space | spatial extent |
| 10 | Sz | Space | spatial extent |
| 11 | t | Time | time |

**Conventions:**

- **Size order in Material** (smallest → largest): aleph, m1, m2, m3, m4, m5, m6. By construction, aleph is sub-Planck and is always the smallest; the 6 Ma dims (m1..m6) are size-ordered with m1 smallest among them.
- **Material → Space → Time** reading top to bottom. Matches the [R60 metric-11](../../../studies/R60-metric-11/) ordering. Reads backward from the usual relativity convention (which puts t first), but the user's preference is for the present "Material-Space-Time" sequence and we adopt it project-wide.
- **Signature** to be pinned alongside the cross-term matrix (Phase 0 second half). The R60 11D work uses a specific signature with exactly one negative eigenvalue; we inherit unless the cross-term structure forces otherwise.

The 11×11 metric tensor under this convention is conventionally written with the diagonal entries reading down the labels above in order; off-diagonals (15 in the Material block plus various Material↔Space, Material↔Time entries) are the project's free architectural content.

---

## 2. Mode nomenclature

A mode is labelled by an 11-tuple of integer windings in the order above:

    { n_aleph, n_1, n_2, n_3, n_4, n_5, n_6, n_x, n_y, n_z, n_t }

Brackets `{ ... }` distinguish the new convention from earlier work's `(n, m)` 2-tuples and the studies' 6-tuple `(e_r, e_t, v_r, v_t, p_r, p_t)` notation (which was sheet-grouped and not size-ordered).

For everyday compact-domain analysis, the spatial and time entries are usually zero and the aleph entry is conventionally fixed (mediator structure, not particle winding). So the typical particle label collapses to the 6-tuple of Ma windings:

    { n_1, n_2, n_3, n_4, n_5, n_6 }   (with n_aleph = 0 and Sx,Sy,Sz,t entries dropped)

**Optional sheet-region hints.** The 6 Ma dims may carry a mnemonic subscript indicating their dominant particle-region: m1p, m2p (proton/quark region), m3e, m4e (electron/charged-lepton region), m5v, m6v (neutrino region). Example: { aleph, m1p, m2p, m3e, m4e, m5v, m6v, Sx, Sy, Sz, t }. **These subscripts are mnemonic only** — they reflect the *primary* access pattern; under the 6-dim-pool reading, a single dim may participate in modes belonging to particles from any region. Drop them if they become misleading.

**Smallest first.** Within any pair `(a, b)` referenced in closure or coupling analysis, the convention is `m_a` smaller than `m_b` — i.e., `a < b` in the index order. (Section 3.1 below.)

---

## 3. Operational rules

### 3.1 Smaller dim = tube; larger dim = ring (per dim-pair)

There is **no global tube/ring assignment** under the 6-dim-pool reading. The role is *per-pair*: in any pair `(m_a, m_b)` with `m_a < m_b` (size order, so L_{m_a} < L_{m_b}):

- m_a plays the **tube** role (analog of MaSt's small / topological / charge-bearing dim).
- m_b plays the **ring** role (analog of MaSt's large / dynamical / mass-bearing dim).

A single dim can therefore be the *tube* for one particle's pair (e.g., m3 paired with m5) and the *ring* for another particle's pair (e.g., m3 paired with m1). This is intentional and a consequence of the pool reading.

### 3.2 Smallest dim as tube governs closure

For closure analysis on a dim-pair `(m_a, m_b)`:

- The smaller dim **m_a** governs the topological / closure side — counts tube windings, hosts the boundary identification, carries any τ-twist.
- The larger dim **m_b** governs the mass side — its winding contributes the mode's mass-energy budget.

This is the natural extension of how MaSt 2D sheets work (where the tube and ring roles are fixed per-sheet) to the per-pair convention of the pool reading.

### 3.3 Plane over diagonal (2D-planar preferred over 3D-mixed)

A wave that uses *two* dimensions has lower energy than a wave that uses *three* dimensions of the same domain at comparable windings, because the 3D-mixed mode pays a quadratic energy cost in the third dim's winding. From the [3-torus.md §5.1](3-torus.md) Test A results at L₁:L₂:L₃ = 1:580:78,000, the lowest 3D-mixed mode sits at 78,000× the lowest 1D-line mode and 580× the lowest 2D-planar mode.

**Rule (working hypothesis):** particles form on 2D-planar modes (dim-pairs); 3D-mixed modes (full triple-dim excitations) are energy-unfavored and reduce to the *dark / unobserved* class. This is the **sheet-constraining rule** for the project: a particle = a mode on a single dim-pair from the 6-dim pool.

The companion rule from [3-torus.md §3.2–§3.3](3-torus.md) — that *1D-line* modes are also unphysical (no EM coupling) under the Candidate-III R19 extension — completes the picture: physical particles are exactly the 2D-planar modes on dim-pairs that have the right cross-term structure.

---

## 4. Open questions deferred to later phases

- **Cross-term sparsity pattern** (second half of Phase 0). Which off-diagonals are non-zero, and which carry τ-twists vs R53 shears vs other coupling types? See [plan.md §1](plan.md) for the working assumption (3 τ-twists for the quark sector, some shears for the e-sector, rest zero).
- **Whether the sheet-region subscripts (p, e, v) survive** as the architecture matures. If the cross-term pattern reveals a single dim participating in (say) both a quark-bearing pair and a charged-lepton-bearing pair, the subscript becomes misleading and should be dropped in favor of plain `m1..m6`.
- **Signature pinning** for the 11×11 metric. R60 used exactly one negative eigenvalue; whether that survives the 6-dim-pool reformulation needs checking once the cross-terms are specified.
- **The aleph entry's coupling structure**. R59 / R60 derive α from the tube↔ℵ↔t chain. Under the per-pair tube reading of §3.1, each Ma dim might individually couple to aleph (with strength σ_ta — the model-F symbol). Whether the 6 dims share one σ_ta or each has its own is a Phase 0-or-1 question depending on how the cross-term template is read.

---

## 5. Cross-references

- [plan.md](plan.md) — phased work plan; this file is the Phase 0 first-half deliverable.
- [3-torus.md](3-torus.md) — supports §3.3 (plane-over-diagonal) and §3.2 (smallest-as-tube) operational rules.
- [ma-share-6.md](ma-share-6.md) — establishes the 6-dim-pool topology this file's nomenclature serves.
- [../../../studies/R60-metric-11/](../../../studies/R60-metric-11/) — 11D metric ordering precedent (Material → Space → Time inherited from there).
- [../../../studies/R59-clifford-torus/](../../../studies/R59-clifford-torus/) — aleph dim introduction and the α-coupling chain.
