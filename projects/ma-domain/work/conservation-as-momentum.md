# conservation-as-momentum.md — conservation laws as geometric momenta

**Status:** Working hypothesis / program document. Proposes that every conserved quantity which gates a decay is a *momentum* — the Noether charge of a translation along some geometric axis — living at some level of the MaSt structure; and that the decay phase space ρ is the volume of the full momentum space surviving once every conservation law is imposed as a momentum-matching constraint. This document sets out the basic theory and **enumerates** the quantities to be worked. Identifying the level and axis of each is the systematic program that follows — it is *not* done here.

**Cross-references:**
- [mode-stability.md §3](mode-stability.md) — the conservation-law stratification (energy/charge fundamental, baryon assumed, flavor emergent); the gap this document reframes
- [leakage-rate.md](leakage-rate.md) — the decay-rate calculation; §3.1 the selection rules; ρ as a momentum integral
- [baryon-number.md](baryon-number.md) — baryon number as a graph-level cut, and the level-dependence (graph vs. sheet-internal) this document generalizes
- [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md) — electric charge as a winding: a prior-art candidate, to be evaluated, not assumed
- [electron-tube.md §6](electron-tube.md), [models/model-F.md](../../../models/model-F.md) — two competing accounts of spin (see §5)
- [architecture.md](architecture.md) — the dim / sheet / `Ma(i,j)` structure and the levels §3 enumerates

---

## 1. The thesis

A decay is allowed only when every conserved quantity balances, and its rate is Γ = (2π/ℏ)·|M|²·ρ, with ρ the phase space. [mode-stability.md §3](mode-stability.md) stratified the conservation laws by how fundamentally each is grounded — energy and charge fundamental, baryon number assumed, flavor emergent. This document proposes a reframing meant to unify them.

**The thesis.** Every conserved quantity that gates a decay is a **momentum** — the Noether charge of translation along some geometric axis, the axis being either *linear* or *rotational*. And ρ is the volume of the **full** momentum space — spacetime momenta and compact/internal momenta together — that survives once *every* conservation law is imposed as a momentum-matching constraint. Then:

- a decay is **allowed** exactly when that volume is non-zero — there exists a final configuration whose momenta, along every axis, match the initial one's;
- a mode is **stable** exactly when the volume is zero — no such configuration exists.

Under the thesis, conservation laws and ρ are not two things. ρ *is* the conservation laws, integrated: "compute ρ" becomes "impose every momentum-matching constraint and measure what is left."

**Why it would be worth having.** If it holds: the selection rules — which conservation laws gate which decays — would be *derived* from geometry rather than postulated; decay and stability would become one geometric statement; and the hard/soft stratification of mode-stability §3 would turn into a statement about *which level* each momentum lives at and whether its generating symmetry is visible there (§4).

---

## 2. Why momentum — the anchors

Three reasons the thesis is worth taking seriously. They are **motivations**, not completed identifications.

- **Noether's theorem.** Every continuous symmetry yields a conserved quantity, and the conserved quantity of a *translation* symmetry is a *momentum*. So if a conserved quantity exists at all, some symmetry generates it, and the open question is only "translation along which axis."
- **Kaluza-Klein** is the prototype that the thesis is even possible: an internal quantum number (electric charge) realized as a literal momentum — momentum around a compact dimension. It establishes that an internal charge *can* be a geometric momentum.
- **ρ is, without exception, an integral of momenta.** The phase space is ∫ ∏ᵢ d³pᵢ over the final-state momenta, cut by the conservation δ-functions. ρ is already, manifestly, a momentum-space volume. The thesis only extends the same statement to the conserved quantities not yet written as momenta.

**A discipline note.** This document does **not** assume the geometric identity of any particular conserved quantity. The framework carries prior-art candidates — metric-charge treats charge as a winding; WvM and Model-F give *competing* accounts of spin — but those are *inputs to be evaluated* by the §5 program, not conclusions adopted here.

---

## 3. Levels — momentum is scale-dependent

A momentum is "about an axis," but the axis lives at some **level** of the MaSt structure — and the same conserved quantity can present differently at different levels. [baryon-number.md §8–§9](baryon-number.md) shows this directly: baryon number reads as a *cut* (a flux) at the dim-graph level, while the quark sheet carries a literal *helix* — the τ = 1/3 clover twist — one level down. A "flux" at a coarse level can be a "circulation" at a finer one. So identifying a conserved quantity as a momentum is incomplete until its **level** is named.

The levels the framework currently distinguishes:

- **Embedding spacetime** (3 + 1 D) — where particles propagate. Ordinary linear momentum, energy, and orbital angular momentum live here.
- **The dim-graph** — dims as nodes, sheets as edges (the K4 of QY-ED-share3). baryon-number.md's cut/cycle decomposition lives here.
- **The 2D sheet** — a torus `Ma(i,j)` with windings T(m_t, m_r), twist τ, shear σ, and a cross-section. metric-charge's winding k_θ lives here.
- **The cross-section / sub-sheet** — the cross-section curve itself, its lobes and arcs (the clover, the ellipse — [tube-function.md](tube-function.md)).
- **The substrate microstructure** — the grid itself ([grid-primitive](../../grid-primitive/)), acknowledged to carry finer, possibly fractal, structure.

The program must, for each conserved quantity, find both the **level** and the **axis** — and stay open to a quantity being a momentum at one level whose coarse-grained image, at a higher level, no longer looks like one.

---

## 4. The method

For each conserved quantity, the systematic working-through (to follow this document) should establish:

1. **Precise statement** — what is conserved, written in the framework's own variables.
2. **Level(s)** — at which level of §3 to look.
3. **Axis** — translation along what direction generates it? *Linear* (an extended or a compact translation) or *rotational* (a twist / winding)?
4. **Momentum check** — is it genuinely the Noether charge of that translation — an integer or continuous momentum along that axis? Or does it resist a momentum reading?
5. **Classification** — once placed: is the generating symmetry *manifest* at the level the decay dynamics operate (a "hard" law) or *buried* at a finer level (a "soft"/accidental one)? This recasts the mode-stability §3 hard/soft split as a statement about the visibility of the axis.

**Discipline.** Do not assume the answer. Some quantities will resolve cleanly; some will not. A quantity that genuinely resists a momentum reading is a *result*, not a failure — it would bound the thesis.

---

## 5. Enumeration — the quantities to be worked

The conserved quantities that gate decays. Each is listed as an **entry to be worked**: its precise statement and any prior-art candidate, with the level/axis identification deliberately left open for the program of §4.

1. **Energy.** *Conserved:* total energy of the field configuration; gates every decay. *Prior-art candidate:* the Noether charge of time-translation invariance (mode-stability §3 grounds it this way). *Status:* the most secure entry — but still to be placed explicitly in the level scheme of §3, and its axis (a translation along time) stated as such.

2. **Momentum** (3-momentum). *Conserved:* total spatial momentum. *Prior-art candidate:* the Noether charge of spatial translation in the embedding spacetime — a linear axis. *Status:* already built into ρ as the δ³(Σp); to be placed in the level scheme and confirmed as the model entry of a "linear momentum."

3. **Angular momentum** (orbital + spin). *Conserved:* total angular momentum. *Orbital part:* the Noether charge of rotation in the embedding spacetime — a rotational axis; relatively clear. *Spin part — geometric origin unsettled, and noted here deliberately:* [electron-tube.md §6](electron-tube.md) records the **WvM** account — spin-½ as a consequence of the (1, 2) double-loop topology specifically (the q = 2 ring winding gives a 720° closure → fermion; a (1, 1) could not). [models/model-F.md](../../../models/model-F.md) (R62) takes a **different** view — spin-½ from a per-sheet Dirac–Kähler field on *every* flat 2-torus, automatic for *all* windings (n_t, n_r), not tied to (1, 2). The two disagree; neither is established. *Status:* an open entry with two competing prior candidates — the systematic work must not adopt either by default.

4. **Electric charge.** *Conserved:* total electric charge. *Prior-art candidate:* [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md) treats it as a winding k_θ = m_r − τ·m_t on a sheet's cross-section; Kaluza-Klein independently realizes charge as momentum around a compact dimension — i.e. a rotational/winding momentum at the 2D-sheet level. *Status:* the most-developed candidate — to be evaluated by §4, not assumed.

5. **Colour charge.** *Conserved* (and confined). *Prior-art candidate:* the framework carries the N = 3 clover's Z₃ structure ([clover-quarks.md](../../sheet-proton/work/clover-quarks.md), tube-function); whether "colour" *is* that Z₃, or something else, is undeveloped. *Status:* open.

6. **Baryon number.** *Conserved* (soft / accidental). *Prior-art candidate:* [baryon-number.md](baryon-number.md) proposes it as a cut-space invariant of the dim-graph; that document's §8–§9 flag that it may instead — or also — be a sheet-internal helix (the τ = 1/3 clover twist). *Status:* open, and the explicit test case for the level-dependence of §3 (is the graph-level cut the coarse-graining of a sheet-level helix?).

7. **Lepton number.** *Conserved* (soft / accidental). *Prior-art candidate:* baryon-number.md's complementary cycle-space invariant. *Status:* open.

**Not enumerated — the non-laws.** Parity (P), charge-conjugation (C), CP, the individual quark flavours (strangeness, charm, …) and lepton flavour are **not** gates: the weak interaction violates the first three, and neutrino oscillations violate lepton flavour. The program concerns only the genuine gates above.

---

## 6. Connection to ρ and decay

This is where the intuition of "energy polarized by a sheet's shape, needing compatible exits" gets pinned to the thesis.

A sheet's **character** is its set of geometric labels — windings, twist τ, shear σ, cross-section shape. A mode on the sheet carries those labels; that is what "the energy is polarized by the sheet" means, made precise. For energy to leave one sheet for another, the labels that must match across the junction are exactly the conserved momenta of §5 — the transition can proceed into an exit channel only if every momentum matches, or it pays to shed a mismatch (the σ-suppression of [leakage-rate.md §3.1](leakage-rate.md)). So "look for exit paths of compatible character" is, precisely, "look for exit channels that conserve every momentum."

That is ρ under the thesis: **ρ counts the momentum-compatible exits.** leakage-rate §3.1 already has the k_θ version of this selection rule (leakage allowed at leading order only between equal-k_θ modes). The thesis generalizes it — every conserved quantity of §5 contributes one matching condition, and ρ is the volume that survives all of them. The "character / compatibility" picture is therefore not a new mechanism; it is the thesis applied to ρ.

---

## 7. What the program must produce, and what is open

**Deliverables of the systematic working-through:**

- The completed §5 enumeration — each quantity placed at a level and an axis per §4, or honestly marked as resisting a momentum reading.
- A precise statement of ρ as the post-conservation momentum volume, with the spacetime constraints and the compact/internal constraints written uniformly.
- The hard/soft stratification recast as axis-visibility (§4, step 5).

**Open and central:**

- **Baryon number's level** — graph-level cut vs. sheet-internal helix (baryon-number.md §9). The test case for §3.
- **Spin's geometric origin** — WvM's (1, 2)-loop account vs. Model-F's per-sheet Dirac–Kähler account. Unsettled; not to be assumed.
- Whether the thesis yields an actual *derivation* of the selection rules, or remains a reframing. It earns promotion to the project's derivation track only if the completed enumeration closes and the selection rules fall out of it.

**Honest status.** This is a working hypothesis. Its anchors — Noether, Kaluza-Klein, and the fact that ρ is already a momentum integral — are real. Its completion is not done. A conserved quantity that genuinely resists the momentum reading would not break the program; it would bound it, and that bound would itself be a result.

---

## Cross-references

- [mode-stability.md](mode-stability.md) — §3 stratifies the conservation laws; this document reframes that stratification as a question of momenta and levels
- [leakage-rate.md](leakage-rate.md) — the decay-rate calculation; §3.1 selection rule; ρ as a momentum integral (§6)
- [baryon-number.md](baryon-number.md) — baryon number as a dim-graph cut; the graph-vs-sheet level-dependence generalized in §3
- [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md) — charge as a winding (a §5 candidate to evaluate)
- [electron-tube.md §6](electron-tube.md) — the WvM (1, 2)-loop account of spin (§5 entry 3)
- [models/model-F.md](../../../models/model-F.md) — the per-sheet Dirac–Kähler account of spin (§5 entry 3)
- [tube-function.md](tube-function.md) — twist τ, shear σ, cross-section shape: the sheet-level structure §3 and §6 draw on
- [architecture.md](architecture.md) — the dim / sheet / `Ma(i,j)` structure and the level hierarchy of §3
