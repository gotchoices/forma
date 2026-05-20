# architecture.md — ma-domain metric layout, nomenclature, and operational rules

**Status:** Phase 0 deliverable (per [STATUS.md](STATUS.md)). Pins the conventions used by everything downstream — the metric ordering, mode-label and pair-label nomenclature, and the operational rules that translate a multi-dim Ma domain into closure analysis on dim-pairs.

This file does **not** yet specify the cross-term sparsity pattern (which off-diagonals carry τ-twists, which carry shears, which are zero). That is the second half of Phase 0 and comes after the conventions below are stable.

The working dim count is N = 6; the architecture is not bound to that count and 5 or 7 are permitted if the structure demands it. Most concrete worked examples below use N = 6 (so a 6×6 Material block); the size-ordering and labelling conventions extend uniformly.

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
- **Material → Space → Time** reading top to bottom. Matches the [R60 metric-11](../../../studies/R60-metric-11/) ordering. Reads backward from the usual relativity convention (which puts t first); the present "Material-Space-Time" sequence is adopted project-wide.
- **Signature** to be pinned alongside the cross-term matrix (Phase 0 second half). The R60 11D work uses a specific signature with exactly one negative eigenvalue; we inherit unless the cross-term structure forces otherwise.

The 11×11 metric tensor under this convention is conventionally written with the diagonal entries reading down the labels above in order; off-diagonals (15 in the Material block plus various Material↔Space, Material↔Time entries) are the project's free architectural content.

---

## 2. Mode nomenclature

A mode is labelled by an 11-tuple of integer windings in the order above:

    { n_aleph, n_1, n_2, n_3, n_4, n_5, n_6, n_x, n_y, n_z, n_t }

Brackets `{ ... }` distinguish the new convention from earlier work's `(n, m)` 2-tuples and the studies' 6-tuple `(e_r, e_t, v_r, v_t, p_r, p_t)` notation (which was sheet-grouped and not size-ordered).

For everyday compact-domain analysis, the spatial and time entries are usually zero and the aleph entry is conventionally fixed (mediator structure, not particle winding). So the typical particle label collapses to the 6-tuple of Ma windings:

    { n_1, n_2, n_3, n_4, n_5, n_6 }   (with n_aleph = 0 and Sx,Sy,Sz,t entries dropped)

**Optional sheet-region hints.** The Ma dims may carry a mnemonic subscript indicating their dominant particle-region: m1p, m2p (proton/quark region), m3e, m4e (electron/charged-lepton region), m5v, m6v (neutrino region). Example: { aleph, m1p, m2p, m3e, m4e, m5v, m6v, Sx, Sy, Sz, t }. **These subscripts are mnemonic only** — they reflect the *primary* access pattern; under the dim-pool reading, a single dim may participate in modes belonging to particles from any region. Drop them if they become misleading.

**Smallest first.** Within any pair `Ma(i, j)` referenced in closure or coupling analysis, the convention is `m_i` smaller than `m_j` — i.e., `i < j` in the index order. (Section 3.1 below.)

### 2.1 Pair-label notation: Ma(i, j)

A dim-pair is written `Ma(i, j)` with the two dim indices size-ordered (`i < j`). A set of pairs (a topology) is written `Ma((i₁, j₁), (i₂, j₂), …)`. Examples:

- `Ma(1, 5)` — the pair built from dims m1 and m5.
- `Ma((1, 5), (3, 5), (4, 5))` — the wye/star topology with hub at m5 and spokes at m1, m3, m4 (the quark wye in [candidates.md](candidates.md)).
- `Ma((2, 4), (2, 5), (4, 5))` — the delta/triangle topology on dims m2, m4, m5 (the electron delta in [candidates.md](candidates.md)).

This notation is deliberately distinct from the mode-winding tuple `T(m_t, m_r)` (per metric-charge's torus-knot mode labels), so a pair `Ma(1, 2)` and a mode `T(1, 2)` are never confused.

When pairs are tabulated in prose without the `Ma()` wrapper, the size-ordered form `(m_i, m_j)` is used. The mode tuple is always written `T(m_t, m_r)` or `(m_t, m_r)` with explicit `m_t`/`m_r` headers when ambiguity is possible.

---

## 3. Operational rules

### 3.1 Tube and ring are per-pair structural roles (not size-determined)

There is **no global tube/ring assignment** under the dim-pool reading. The role is *per-pair* and is a **structural choice** carried by the pair's cross-term content, not determined by which dim is smaller. In any pair `Ma(i, j)`:

- One of the two dims is assigned the **tube** role (analog of MaSt's topological / cross-term-bearing / charge-coupled dim — winds m_t).
- The other dim is assigned the **ring** role (analog of MaSt's mass-bearing dim — winds m_r and carries the cross-term-driven shift to (m_r − σ_eff m_t)).

A single dim can therefore play tube in one pair and ring in another. The role assignment is part of the pair-triplet specification (cf. §3.4 working hypothesis) and emerges from the cross-term structure, not from the dim sizes per se.

**Convention from prior MaSt work** held that the smaller dim plays tube. This is true at the proton-sheet operating point (ε_p ≈ 0.55, thin torus) but does *not* generalize: the R53 charged-lepton fit has ε_e ≈ 397 (fat torus), with the *larger* dim playing tube. The quark-sector wye topology in [quark-search.md §9](quark-search.md) similarly requires the *larger* dim (the common hub m4) to play tube in all 3 quark pairs. So the smaller-as-tube assumption is a special case, not a rule. **Per-pair tube/ring assignment is free** and must be specified by the cross-term structure for each pair.

**Two natural rule-of-thumb consequences** that survive even without smaller-as-tube:

- **The mass scale of the lowest mode is set by the smaller dim of the pair** (the L_R in the formula `m² ≈ (2π ℏc)² · ((1/L_T)² + (δ/L_R)²)`, which dominates when L_T ≫ L_R and which is also the relevant scale when L_T ≈ L_R).
- **Within-pair mass splits are controlled by the detuning f**, and become observable when L_T/L_R is large enough that (δ/L_R)² ≫ (1/L_T)² for the smallest physical δ.

### 3.2 The tube dim governs closure

For closure analysis on a dim-pair `Ma(i, j)`, the tube role (per §3.1, per-pair-assigned) governs the topological / closure side:

- The **tube** dim counts tube windings, hosts the boundary identification, carries any τ-twist.
- The **ring** dim governs the mass side — its winding contributes the mode's mass-energy budget via the (m_r − σ_eff m_t)/L_ring term.

Whether the tube dim is *smaller* or *larger* than the ring dim is a per-pair structural choice; both regimes appear in successful particle fits (thin-torus proton sheet vs fat-torus R53 charged leptons vs the quark wye topology in [quark-search.md §9](quark-search.md) with one fat common tube).

### 3.3 Plane over diagonal (2D-planar preferred over 3D-mixed)

A wave that uses *two* dimensions has lower energy than a wave that uses *three* dimensions of the same domain at comparable windings, because the 3D-mixed mode pays a quadratic energy cost in the third dim's winding. From the [3-torus.md §5.1](3-torus.md) Test A results at L_a : L_b : L_c = 1 : 580 : 78,000, the lowest 3D-mixed mode sits at 78,000× the lowest 1D-line mode and 580× the lowest 2D-planar mode.

**Rule (working hypothesis):** particles form on 2D-planar modes (dim-pairs `Ma(i, j)`); 3D-mixed modes (full triple-dim excitations) are energy-unfavored and reduce to the *dark / unobserved* class. This is the **sheet-constraining rule** for the project: a particle = a mode on a single dim-pair from the multi-dim Ma pool.

The companion rule from [3-torus.md §3.2–§3.3](3-torus.md) — that *1D-line* modes are also unphysical (no EM coupling) under the Candidate-III R19 extension — completes the picture: physical particles are exactly the 2D-planar modes on dim-pairs that have the right cross-term structure.

#### 3.3.1 Closure-satisfying mode inventory per pair (from metric-charge)

The valid (m_t, m_r) windings on each dim-pair come from [metric-charge chapter 4](../../metric-charge/04-the-closure-condition.md), specifically §1–§4. The operational closure rule is:

  **m_t | m_r with both nonzero.**

I.e., m_t must divide m_r, and neither m_t nor m_r is zero. This is equivalent to the chirality form (a chirally-trivial knot under R_u) and to the topological form (the gcd-reduced primitive is T(1, n′) for some integer n′ ≥ 1).

Consequences relevant to ma-domain mode searches:

- **Closure-satisfying primitives are exactly T(1, n) for n ≥ 1.** So per-pair, the closure-satisfying modes at m_t = 1 are T(1, 1), T(1, 2), T(1, 3), … indefinitely. Lowest two are **T(1, 1)** and **T(1, 2)**.
- **T(m_t, 0) and T(0, m_r) both fail.** Single-axis modes are closure-failing (no chirality structure to test).
- **T(2, 3), T(3, 2), T(3, 4), …** (genuine torus knots with gcd-primitive p, q ≥ 2) fail closure — chirally distinct from their mirrors. They are mass-only (no EM charge) per metric-charge §4.2.
- **Multi-component links T(k, k·n) for k ≥ 2, n ≥ 1** are closure-satisfying (k-component repetitions of T(1, n)). T(3, 6) for example is closure-satisfying as 3 copies of T(1, 2) — this is the (3, 6) proton-as-3-quark identification in model-F.

For ma-domain Phase 1+ work, this means: when picking the "lowest two closure modes" per pair `Ma(i, j)`, the candidates are T(1, 1) and T(1, 2) — *not* T(1, 0) (closure-failing) and *not* T(2, 3) (genuine knot, mass-only). Earlier ma-domain analyses that used T(1, 0) as a candidate mode have been corrected to use T(1, 1) and T(1, 2).

### 3.4 How a single dim can be simple ring in one context, complicated tube in another (working hypothesis)

[sheet-proton clover-quarks.md](../../sheet-proton/work/clover-quarks.md) explains the quark sector via a clover-shaped corrugated cross-section (3 lobes of 240° + 3 saddles of 120°, Z₃ symmetric). Under the dim-pool reading, that clover shape cannot belong to a single dim — a single dim is just a circle of size L. The shape has to be a property of how two dims combine, so that one of those dims can be a *plain ring* when paired with a different partner.

**Working hypothesis: pair-triplet (σ, τ, P).** Replace the scalar cross-term σ_{ij} between two dims of a pair `Ma(i, j)` with a triplet:

  - **σ_{ij}** — the constant off-diagonal shear (scalar; the metric off-diagonal entry as in current MaSt).
  - **τ_{ij}** — the discrete topological twist (scalar; k/3 for some integer k, or 0).
  - **P_{ij}(u)** — a *shape function* periodic on the helical coordinate u = u_i + τ_{ij} u_j; it is the position-varying part of the off-diagonal entry, and it carries the sheet's cross-section shape.

The pair-metric is then

  g_{ii}^{(ij)} = L_i² ,
  g_{jj}^{(ij)} = L_j² ,
  g_{ij}^{(ij)} = (σ_{ij} + τ_{ij}) L_j² + P_{ij}(u) ,

a regauged form of [clover-quarks.md §10.3](../../sheet-proton/work/clover-quarks.md). The diagonal entries are the plain dimension sizes; the off-diagonal carries the shear, the twist, and — through P_{ij}(u) — the shape. P_{ij} = 0 gives a flat twisted torus on the pair (constant off-diagonal: pure shear + twist); a non-zero P_{ij} curves it — a 3-lobe profile gives the quark clover, a 2-lobe profile the electron ellipse.

**Shape is the pair's curvature, and it is per-sheet.** What is invariant is the Gaussian curvature K(u) of the pair's 2-torus — that scalar function *is* the clover, or the ellipse. Which metric component is written as a function to realize a given K(u) is a gauge choice; the form above adopts the gauge that keeps every diagonal entry a plain L². That gauge is deliberate: a dimension then contributes the *same* diagonal entry L_i² to every sheet it joins, and each shape sits in an off-diagonal component g_{ij} that belongs to exactly one pair. Sheets sharing a dimension therefore share only its size L — never a shape (see §4, per-pair consistency). The clover is a property of the **pair `Ma(i, j)`**, not of either dim alone.

A quark-sector pair then maps to some `Ma(i, j)` with τ_{ij} = 1/3 and P_{ij} = clover. The same m_i paired with a different m_k could have P_{ik} = 0 and host a plain electron-region mode.

**Adopted as the project standard for now**, on the strength of:

  - It is the most direct way to extend the existing MaSt cross-section machinery to the pool reading without re-deriving anything.
  - It transports the per-arc curvature charges (Q_lobe = +2/3, Q_saddle = −1/3) unchanged, because the geodesic-curvature integral is a property of P_{ab} on the pair's 2-torus — it doesn't care whether P "belongs to" a dim or to a pair.
  - It keeps the diagonal entries at the plain sizes L_a², so a dimension contributes one and the same diagonal entry to every sheet it joins — making shared-dim consistency manifest (§4). The R60 signature analysis applies pointwise, the off-diagonal now varying with position.

**But it is one possible mechanism, not the only one.** Several alternatives could produce the same dual-role behavior; the math may reveal that one of these is the correct deeper structure. Candidates to keep in mind:

1. **Mode-resolution / wavelength filtering** ([3-gen.md §3.5.1](../../sheet-proton/work/3-gen.md)). The dim *does* have a fixed underlying shape, but modes of long wavelength "average over" the corrugation and see a smooth ring, while short-wavelength modes resolve the lobes/saddles. In this reading, the clover shape is "always there" on m_a, but only the modes that fit inside it see it.

2. **Effective metric from a deeper substrate.** The 6 dims are simple at the metric level, but the wave equation on top of them lives on a richer substrate (GRID lattice, sub-Planck aleph structure, R55–R59 mediator chain). The "clover" emerges as the effective potential the wave equation sees in a particular regime, not as a fundamental metric feature.

3. **GRID / lattice fingerprint.** Each dim's compact circle is paved by a discrete GRID lattice. In some pairings, the lattice's site spacing matches the wave's wavelength and imprints the clover-like 3-fold periodicity; in others it doesn't and the dim looks smooth.

4. **Composite dim structure.** What we call a single dim m_a is actually a compound — multiple sub-circles with internal structure. The clover is the envelope of the compound; some pairings resolve the envelope, others see only the gross structure.

5. **Symmetry-broken pair coupling.** The dim has multiple possible shapes in superposition, and the pairing context selects one via a symmetry-breaking interaction.

The working hypothesis (pair-triplet) is **provisional** and chosen because it makes Phases 1–4 of the work plan immediately tractable. If a downstream derivation (Phase 5 mathematical work, or earlier inconsistencies surfaced by the per-pair consistency check in §4 open questions) forces one of the alternatives, we swap to that mechanism without changing the project's scientific content — the per-arc charges and the proton-mass results survive any of these readings, because they all reduce to "there is a clover-shaped influence on the proton-bearing pair's modes," differing only in *what underlying object* hosts that influence.

---

## 4. Open questions deferred to later phases

- **Cross-term sparsity pattern** (second half of Phase 0). Which off-diagonals are non-zero, and which carry τ-twists vs R53 shears vs other coupling types? See [STATUS.md §1](STATUS.md) for the working assumption (3 τ-twists for the quark sector, some shears for the e-sector, rest zero).
- **Whether the sheet-region subscripts (p, e, v) survive** as the architecture matures. If the cross-term pattern reveals a single dim participating in (say) both a quark-bearing pair and a charged-lepton-bearing pair, the subscript becomes misleading and should be dropped in favor of plain `m1..m6`.
- **Signature pinning** for the 11×11 metric. R60 used exactly one negative eigenvalue; whether that survives the 6-dim-pool reformulation needs checking once the cross-terms are specified.
- **The aleph entry's coupling structure**. R59 / R60 derive α from the tube↔ℵ↔t chain. Under the per-pair tube reading of §3.1, each Ma dim might individually couple to aleph (with strength σ_ta — the model-F symbol). Whether the 6 dims share one σ_ta or each has its own is a Phase 0-or-1 question depending on how the cross-term template is read.
- **Pair-shape mechanism** (§3.4). Pair-triplet (σ, τ, P) is adopted as the working hypothesis; if the math reveals that mode-resolution filtering, GRID-lattice fingerprinting, or another mechanism is the correct deeper structure, the architecture swaps to that without losing the per-arc charges or the proton-mass results.
- **Per-pair consistency at shared dims** (§3.4) — *resolved.* The pair-metric of §3.4 keeps every diagonal entry at the plain size L_i², so a shared dimension contributes one identical diagonal entry to every sheet through it; each shape sits in an off-diagonal P_{ij} belonging to exactly one pair. Shape is the sheet's Gaussian curvature, and the curvatures of distinct sheets are independent — they never collide. The only quantity a shared dimension imposes on its sheets is its size L. Worked for the K4 candidate in [cand-QY-ED.md §4.2](cand-QY-ED.md).

---

## 5. Cross-references

- [STATUS.md](STATUS.md) — phased work plan; this file is the Phase 0 first-half deliverable.
- [3-torus.md](3-torus.md) — supports §3.3 (plane-over-diagonal) and §3.2 (smallest-as-tube) operational rules.
- [ma-share.md](ma-share.md) — establishes the dim-pool topology this file's nomenclature serves.
- [../../../studies/R60-metric-11/](../../../studies/R60-metric-11/) — 11D metric ordering precedent (Material → Space → Time inherited from there).
- [../../../studies/R59-clifford-torus/](../../../studies/R59-clifford-torus/) — aleph dim introduction and the α-coupling chain.
