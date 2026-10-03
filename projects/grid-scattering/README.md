# grid-scattering

**Does a GRID node couple every dimension equally — and if not, what rule governs when energy crosses from one sheet to another?**

**Type:** Exploratory project (see [../README.md](../README.md))
**Scope:** The node-level update rule at a point where several compact sheets meet. What keeps energy inside one sheet under ordinary conditions, what opens a channel between sheets, and what rate that channel carries.
**Status:** Framing only. No chapters, no code. Two precursor experiments are queued in *other* projects (see [§5](#5-precursor-experiments-in-other-projects)) and should run before this project's own work starts.

---

## 1. The question, and why it is open

GRID's canonical update rule is the **impedance scatter**. A node of coordination N holds one register per incident edge; each tick it replaces the registers with

  S = (2/N)·J − I

where J is the all-ones matrix and I the identity. Written out, each outgoing value is (2/N)·(sum of all registers) minus that register's own content. The rule treats **all N registers identically** — it has no notion of which dimension an edge points along.

That uniformity is not an assumption anyone chose and later abandoned. It is the default everywhere in the repo, and [grid-duality ch. 6](../grid-duality/06-3d-extension-and-lattice-closures.md) established it as a general result — in that project's own summary, *"Scattering generalizes to any coordination and any dimension by the algebraic properties of S = (2/N)·J − I"* ([grid-duality README](../grid-duality/README.md)). Every multi-axis simulation in forma inherits it — grid-matter's (x, compact-c) cylinder at N = 4, its three-axis two-slit lab at N = 6.

**The trouble is downstream.** Treating every dimension alike predicts modes that are not observed. [ma-domain 3-torus.md](../ma-domain/work/3-torus.md) found that a sheet with three compact dimensions produces a dense tower of **1D-line modes** — modes exciting only one compact direction — sitting *below* the modes meant to be the particle generations. Roughly 134 of them. They are harmless only if they carry no electric charge, and whether they do depends on a **charge-selection rule** the project could not derive. The candidate that does the needed job, "Candidate III," assigns each 2D plane of the sheet a circulation

<!-- C_ij = ∮ over the boundary of the (L_i x L_j) cell of [ (d_i psi) du_j - (d_j psi) du_i ] -->
$$
C_{ij} \;=\; \oint_{\partial(L_i \times L_j)\text{-cell}} \bigl[ (\partial_i \psi)\, du_j \;-\; (\partial_j \psi)\, du_i \bigr]
$$

which for a plane wave comes out proportional to **n_i · n_j** — non-zero only when the mode winds in *at least two* dimensions, which is exactly what kills the 1D tower. The file is explicit that this is a posit: *"The script does not derive which candidate is physical."* Its verdict is recorded as **conditionally open, not failed**.

**Meanwhile, energy demonstrably does cross between domains.** Two gamma rays of sufficient energy produce an electron–positron pair; a neutron decays to a proton plus an electron and an antineutrino; an electron and positron annihilate back to light. Whatever the rule is, it permits these and forbids a great deal else.

**And forma has no such rule.** [ma-domain leakage-rate.md](../ma-domain/work/leakage-rate.md) carries a foundational caveat on exactly this point: the working assumption that energy leaks only between sheets sharing a dimension is *"unverified and probably too strong,"* because coupling without a shared dimension *"demonstrably exists — a charged closure mode radiates energy into macroscopic space S at rate ~α with no shared dimension."* It concludes: *"the leakage graph is richer than the metric-sharing graph."* Separately, [ma-domain threshold-dynamics.md](../ma-domain/work/threshold-dynamics.md) is parked behind six questions, of which §6.2 — *by what physical mechanism does energy reorganize from a background band into a discrete mode?* — is unanswered.

So there is a hole with a precise shape, and several projects are waiting on it.

---

## 2. The proposal

One modification to the node rule, from which the rest is meant to follow.

> **A node's edges carry a sheet label. Under ordinary conditions scattering is closed within a sheet. A named condition — the working candidate is saturation — opens a channel between sheets.**

"Sheet" here follows [ma-domain](../ma-domain/)'s reading: a sheet is the 2D surface formed by a *pair* of compact dimensions, not a dimension on its own. A node participates in many sheets at once; what the proposal adds is that its edges are **partitioned** among them rather than pooled.

This is a deliberate departure from grid-duality ch. 6's generalization. That project is closed and its result stands as stated; this one proposes a variant for the specific case of a node where several sheets meet, and should be benchmarked against grid-duality's existing [test bench](../grid-duality/03-test-bench.md).

### 2.1 Guiding premises (the concepts to be tested)

Stated as premises so each can be tested or discarded on its own.

- **P1 — One grid, sheet-labelled edges.** There are not separate lattices per domain. Every node has access to every dimension; its edges are partitioned by sheet.

- **P2 — Ordinary scattering is sheet-closed, by momentum.** Information entering a node on one edge scatters out on the other edges *of the same sheet*. It does not reverse, because the rule subtracts the register's own prior content. It does not turn into an orthogonal sheet, because a 90° turn does not conserve momentum: the two outgoing legs of a plane sit at complementary angles and each takes its share, which balances exactly. Orthogonal sheets see none of it.

- **P3 — Saturation is what opens the cross-sheet channel.** A node summing its inputs can receive more than it can redistribute. In a mechanical or fluid analogue, an over-pressured accumulator must spill, and it spills in every direction including orthogonal ones — a small explosion rather than a redirection. Momentum survives because the spill is symmetric: whatever leaves in one direction is matched by an equal amount leaving the other way.

- **P4 — Transfer is pairwise, and gated by fit.** Because the spill is symmetric, energy enters a new sheet *in both directions at once* — a candidate account of why particles arrive in particle/antiparticle pairs. The arriving energy must also **fit** a mode the target sheet can host: an exact fit makes a particle; less than a whole quantum merges into that sheet's background; more than a whole quantum leaves the surplus as momentum in S.
<!--EC I wonder if the explosion leaves in _three_ directions at once (rather than 2).  IOW, if our grid model is correct, each sheet meets at each node by 3 edges.  Not sure if we need to be that explicit.  The energy does leave in 2 directions, but it might do so via 3 nodes (120 degrees apart). -->

- **P5 — Background fluctuation is the stochastic trigger.** A mode already circulating on its sheet has nowhere to go under P2 alone, which is why it persists. Zero-point fluctuation pushes nodes over the saturation threshold intermittently and at random. A decay happens when a fluctuation coincides with an exit that satisfies every conservation law at once. Decay is therefore a **coincidence** process — which is the right statistical shape, since coincidence processes are memoryless and give the observed exponential decay law, whereas a steadily accumulating load would not.

- **P6 — Domains are ordered by state density, not by energy.** Energy is conserved at every transition; what changes is the number of states the energy can occupy. S is the **widest** destination, not the lowest — for a given total energy, putting it into momentum buys vastly more phase space than putting it into rest mass, because phase-space volume grows as p² dp and rest mass contributes no momentum at all. High-energy modes decay quickly because wider destinations are always available; the neutron is slow because few exits are open; ordinary matter endures because its exits are closed.

- **P7 — What closes an exit is a conservation law, not a lack of room.** The proton has somewhere energetically lower to go (p → e⁺ + π⁰ is far downhill in rest mass) and does not go there. What forbids it is baryon-number conservation; what protects the electron is charge, a topological winding. The ladder of P6 sets *direction*; conservation sets *reachability*. A model that explains stability by "nothing lower is available" predicts proton decay and is wrong.
<!--EC If I understand it correctly, proton decay _is_ predicted by current physics but it is just very very rare and slow (billions of years?).  Seems like our model supports this notion too (there are "lower" or "wider" states but the chance of such a state opening up is so rare, it is effectively impossible). -->

### 2.2 What the proposal would buy

If P1–P3 hold, three things that forma currently assumes become derived:

1. **The charge-selection rule.** A mode confined to a single dimension never takes part in the two-edge split that defines a plane, so it has no circulation and no electromagnetic coupling. That is Candidate III's "winding in at least two dimensions," obtained from the dynamics instead of posited — and it decides 3-torus.md's open verdict.
2. **Plane-over-diagonal.** [ma-domain architecture.md §3.3](../ma-domain/work/architecture.md) rules that particles live on 2D dim-pairs and that fully 3D-mixed modes are dark. Its justification today is an energy count. P2 would make a sheet *dynamically* closed rather than merely expensive — a mechanism where there is currently only a cost argument.
3. **Why inter-sheet coupling is weak.** If cross-sheet transfer happens only on overflow, its weakness is structural rather than fitted. [sheet-proton clover-quarks.md](../sheet-proton/work/clover-quarks.md) names this as a thing the framework needs: *"showing that the inter-sheet coupling factor naturally gives the observed weak coupling strength g_W."*

---

## 3. Corrections already folded in

The premises above are a revised form of the originating notes. Four things in the first formulation did not survive scrutiny and have been changed rather than carried forward.

| Original | Problem | Replaced by |
|---|---|---|
| S is the "lowest," most economical state for energy | A 511 keV photon and an electron at rest are *exactly* energy-degenerate; S is not lower | P6 — S is the **widest** state; the ordering is by state count, and the preference scales as ln(V/λ³) |
| The proton is stable because "there is nothing lower" | False — p → e⁺ + π⁰ is hugely downhill in rest mass | P7 — stability is **baryon number**, flagged in [mode-stability.md §3](../ma-domain/work/mode-stability.md) as assumed, not derived |
| Emitting in both directions at once explains particle **pairs** | Back-to-back emission gives *linear* momentum balance only; it does not forbid emitting one fermion | Open — see [§4](#4-known-obstructions) |
| In β decay the electron and neutrino energies "just fit" the neutron–proton gap | They do not: the gap is 1.293 MeV, the electron 0.511 MeV, the neutrino ≈ 0, and the remaining 0.782 MeV is a *continuous* spectrum | Fit governs **whether** a channel opens (a threshold: the gap must exceed m_e); S then absorbs whatever is left over, always and continuously |
<!--EC I wonder if, in lieu of "just fit" we need a notion of "fits closely enough to happen" -->

The fourth correction is the sharpest constraint on the whole family of threshold models and is worth stating plainly: **a fit-based mechanism may gate the rate, but it must not imprint structure on the partition.** The measured β spectrum is smooth from zero to its endpoint, and that smoothness is precisely how the third body was inferred in the first place.

---

## 4. Known obstructions

Named up front, because each is a recorded result that this project has to get past rather than rediscover.

- **The pump.** grid-matter tried two saturation responses (clip, spillover) and neither moved energy durably into the compact sector: they are *"per-edge, per-tick responses; they do not phase-lock energy into the stable n ≥ 1 eigenmode, and the linear scatter undoes their redirection each tick"* ([results-m1-m2.md](../grid-matter/work/results-m1-m2.md)). **Candidate answer from P2:** if ordinary scattering is sheet-closed, the return trip also requires an overflow, so the next tick cannot simply undo the transfer. The channel is ratcheted in the sense that both directions are gated. Net direction then comes from which side saturates less often — a statistical answer, which lands back on P6 and makes the ladder a consequence rather than a postulate.

- **Node, not edge.** The same file found that *"head-on does not raise the per-edge amplitude… The collision's specialness lives in the **node** (larger scatter sum T), not on any edge."* Any saturation condition must therefore be stated on the node's summed input T, not per edge. This is the single design decision that separates a new attempt from the one that failed.

- **Discreteness versus the scatter.** The only energy-conserving integer matrices are signed permutations, and (2/N)·J − I is not one, so *"'the Maxwell scatter, but with indivisible ±1 edges' is not a consistent object."* A sigma-delta node that carries the remainder forward is faithful on average but *"recovers dispersion → does **not** trap."* The variant worth testing is a **delocalized** remainder — parked in a compact sheet or its background rather than in a per-node register — since a delocalized remainder can accumulate coherently where a local one cannot. That does not evade the matrix theorem; it changes where the remainder lives, and whether that is enough is an open question.

- **Fermion pairs.** Linear-momentum balance is not what forces pairs. **Fermion parity** is: in a Lorentz-invariant local theory a term with an odd number of fermion fields cannot be a scalar, so fermion number changes only in even steps. Angular momentum says the same thing from another side — a spin-½ initial state cannot become an integer-spin final state. Both route through **spin**, which forma has not settled: [conservation-as-momentum.md §5](../ma-domain/work/conservation-as-momentum.md) records two competing accounts and adopts neither. This is the premise most likely to resist a purely geometric derivation.

- **Baryon and lepton number.** The intuition that these are momenta underneath is already forma's working hypothesis — [conservation-as-momentum.md](../ma-domain/work/conservation-as-momentum.md) proposes exactly that, and [baryon-number.md](../ma-domain/work/baryon-number.md) offers baryon number as a cut-space invariant of a dim-graph with lepton number as the orthogonal cycle-space invariant. Two cautions: that programme is incomplete by its own account, and lepton number is not exactly conserved in the first place. **B − L** is the defensible target.

- **Tracks.** A decay picture in which a quantum is "stuck on its track" should note that [sheet-proton lb-mode-localization.md](../sheet-proton/work/lb-mode-localization.md) is a **negative result**: no low-lying eigenmode of the modulated clover localises on the tracks. Tracks survive only under a reading in which each quantum is assigned one by Pauli exclusion — a posit, not a consequence of the wave equation.

---

## 5. Precursor experiments in other projects

Two experiments should run **before** this project's own chapters, in the projects that own the relevant history and infrastructure. Both have pre-registered predictions. Neither requires the sheet rule, so both are informative whatever happens here.

### 5.1 The pump test — in [grid-matter](../grid-matter/)

grid-matter owns the saturation history, the (x, compact-c) cylinder testbed, the vacuum-noise flag, and the same-seed differencing control that caught a false positive on an earlier pass. This is the next entry in its M2 line, not a new line.

- **Setup.** Two waves launched from opposite ends of the extended axis, colliding at a point. Saturation condition stated on the node's summed input T. Measure energy retained in the compact sector long after the drive is gone, differenced against a same-seed control so the static background floor cancels.
- **Prediction.** Energy that crosses into the compact sector persists, rather than being re-mixed away within a few ticks.
<!--EC I suspect it only "remains" if it fits the quantum size of the sheet (so the sheet can stay self-consisten).  If it doesn't "fit", I'm guessing it will eventually merge into the ZPE and any excess will either fall back down the ladder (or eventually get absorbed upward into other particle creations). -->
- **If it fails.** The transfer thesis joins grid-matter's instructive negatives, and this project continues on chapters 2–3, which do not depend on it.

### 5.2 The background-spectrum test — in [grid-quantization](../grid-quantization/)

What happens to energy that does not fit a resonant mode is that project's charter, and its Tier 2 is unstarted.

- **Setup.** Inject broadband, deliberately non-resonant energy into a compact dimension. A wave whose wavelength does not divide the circumference must become self-consistent on returning to its starting point. Watch what disperses back out, and what continues to circulate.
- **Prediction.** The residual converges on a mean energy of ½ℏω₁ — half the fundamental.
- **Why it matters.** [ma-domain zpe_derivation.md](../ma-domain/work/zpe_derivation.md) obtains that value from two postulates, of which the second — a uniform spectral density across the sub-fundamental band — is flagged *"not derived, but it has a clean informational justification."* A positive result turns a postulate into a consequence of the dynamics. A negative one is equally informative.
- **A note on the extended axis.** The same argument applied to S requires S to be periodic, if very large. That is not a free assumption — it is one forma already makes without saying so: [ma-domain architecture.md §2](../ma-domain/work/architecture.md) labels modes with *integer* windings on the spatial axes, which only a compact S admits. A result here would give that silent assumption a job.
<!--EC would be interesting if we end up backing into an indirect proof of space's periodicity. -->

---

## 6. Chapter arc — preliminary

Deliberately provisional; the ordering past chapter 3 depends on what §5 returns. Status flags follow grid-matter's convention: **[D]** derivable now · **[C]** computationally demonstrated · **[P]** posited link · **[O]** open.

| # | Chapter | Rests on | State |
|---|---|---|---|
| 1 | **The rule.** Sheet-labelled edges and sheet-closed scattering, written as a candidate update rule in the format of [grid-duality's model notes](../grid-duality/models/), and run against that project's test bench for stability and fidelity. | P1, P2 | **[O]** |
| 2 | **Selection rule I — the 1D tower.** Does sheet-closed scattering dynamically suppress the electromagnetic coupling of 1D-line modes? A pass derives Candidate III and settles 3-torus.md's open verdict. Needs no saturation. | ch. 1 | **[O]** |
| 3 | **Selection rule II — plane over diagonal.** Does node-level momentum conservation make a 2D sheet dynamically closed, replacing architecture §3.3's energy-cost argument with a mechanism? Needs no saturation. | ch. 1 | **[O]** |
| 4 | **The channel.** What opens cross-sheet transfer, and does the transfer survive the next tick. Gated on §5.1. | P3, §5.1 | **[O]** |
| 5 | **The rate.** The leakage law [leakage-rate.md](../ma-domain/work/leakage-rate.md) is missing: what sets the cross-sheet rate, and does it give ~α on the electromagnetic channel and the right smallness on the weak one. | ch. 4 | **[O]** |
| 6 | **Direction and balance.** Does an overflow-only channel respect microreversibility, and does the net direction come out as the state-density ordering of P6 rather than needing to be imposed. | ch. 4, P6 | **[O]** |

Chapters 2 and 3 are independent of saturation. If the channel work fails, those two still stand on their own and still deliver something ma-domain needs.

---

## 7. What success looks like

- **Minimum.** A derived selection rule replacing Candidate III's posit — i.e. chapters 2 and 3 pass, and 3-torus.md's conditional verdict resolves one way or the other.
- **Full.** A leakage law that reproduces ~α on the electromagnetic channel and the observed smallness of the weak one, from geometry rather than fit.
- **Also a result.** A clean negative. If sheet-closed scattering does not suppress the 1D tower, Candidate III loses its most natural mechanism and 3-torus.md's picture is in trouble — which is worth knowing, and is the kind of instructive negative [grid-matter ch. 2](../grid-matter/02-why-simple-binding-fails.md) shows can carry a chapter.

---

## 8. Relation to other projects

**This is not a revival of grid-saturation.** grid-matter was renamed from `grid-saturation` because its entry hypothesis — that the saturation bound *binds a particle* — was refuted: a cap on a linear amplitude is a wall, walls harden, and hardening is defocusing. That refutation concerns **binding**. The thesis here concerns **transfer**, and grid-matter's own work file keeps it open in as many words: *"This is 'not yet,' not 'refuted.' The thesis (saturation → S→c transfer → a rest particle) is intact; the specific clip/spillover realizations don't pump."* The distinction is recorded here so it does not have to be re-litigated.

- [grid-duality](../grid-duality/) — closed; supplies the uniform-scatter result this project proposes a variant of, the candidate-model format, and the test bench.
- [grid-matter](../grid-matter/) — owns the saturation history, the cylinder testbed, and precursor §5.1.
- [grid-quantization](../grid-quantization/) — owns precursor §5.2.
- [grid-primitive](../grid-primitive/) — the edge/node primitive this rule modifies.
- [ma-domain](../ma-domain/) — the principal consumer: [3-torus.md](../ma-domain/work/3-torus.md) (Candidate III), [architecture.md §3.3](../ma-domain/work/architecture.md) (plane over diagonal), [leakage-rate.md](../ma-domain/work/leakage-rate.md) (the missing leakage law), [threshold-dynamics.md §6.2](../ma-domain/work/threshold-dynamics.md) (the coupling mechanism), [zpe_derivation.md](../ma-domain/work/zpe_derivation.md) (Postulate 2).
- [sheet-proton](../sheet-proton/) — consumer: [clover-quarks.md](../sheet-proton/work/clover-quarks.md) needs inter-sheet coupling to give g_W its observed smallness.
- [grid-gravity](../grid-gravity/) — not a consumer. Its carrier couples to energy and is *"blind to which sheet or winding"* ([README](../grid-gravity/README.md)), which is why it could progress without this question being settled.

---

## 9. Next steps

1. Run **§5.1** (pump test) in grid-matter and **§5.2** (background spectrum) in grid-quantization. They are independent and can go in either order or together.
2. Draft chapter 1's rule as a model note, and check it on grid-duality's test bench for stability and wave fidelity before asking it to do any physics.
3. Revisit this arc once §5 returns. Chapters 4–6 are provisional and should be re-cut around what the precursors show.
