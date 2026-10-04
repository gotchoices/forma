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

- **P2 — Sheets are closed, and this is a theorem rather than a posit.** Sheets are mutually **orthogonal** — every edge of one sheet is orthogonal to every edge of every other — so leaving a sheet is always a 90° turn. The operative content of that picture is not geometric, though; it is a **symmetry**. A sheet is a pair of compact dimensions, and a mode living on it has winding number zero along every other compact dimension. If the update rule is invariant under translation along a compact axis, and the state carries no winding on that axis, then by equivariance the state **can never acquire any** — the dynamics and the initial condition share a symmetry, so the solution keeps it.

  Numerically, on a periodic three-axis lattice seeded with a state uniform along the compact axis: the energy in every non-zero compact winding stays at **exactly zero**, to machine precision, for the whole run. The result is stronger than linearity — it survives a **nonlinearity too**, provided the nonlinearity is itself translation-invariant along that axis. A node-level saturation rule applied uniformly also produced exactly zero winding.

  So the geometric intuition is sound and the reason is sharper than the geometry: **orthogonal sheets are orthogonal subspaces of the mode space, and a symmetric rule cannot connect them.** This supersedes an earlier draft of this premise, which argued from momentum conservation and was wrong on two counts — momentum is conserved at the uniform scatter at every coordination tested (trivalent 120°, square, triangular, cubic 3D) whether or not energy crosses sheets, so it discriminates nothing; and the apparent counterexample that suggested it did was a *localized pulse*, which contains every wavenumber from the start, rather than a mode.

  **Coordination is left open.** Whether a sheet meets a node with 3 edges at 120° (simplicial / honeycomb), 4 (square), or 6 (triangular) is not settled in the repo — [grid/compact-dimensions.md](../../grid/compact-dimensions.md) carries both a 3-neighbour simplex count and a 6-neighbour triangular sheet, while the simulations use squares. The symmetry argument holds for all of them, so nothing downstream depends on the choice. One incidental fact worth recording, since it is easy to get backwards: the scatter always leaves a **reflection** of −(1 − 2/N) on the arrival edge — −1/3 at N = 3, −1/2 at N = 4, −2/3 at N = 6 — and momentum balances *because of* that term, not despite it.

- **P3 — Saturation *amplifies* cross-sheet transfer; it does not open the channel.** The original premise was that saturation opens the channel. P2's theorem rules that out: a translation-invariant nonlinearity preserves winding exactly as a linear one does. What a nonlinearity demonstrably does, once a symmetry-breaking seed is present, is **amplify** the transfer — about 2,500× over the linear control in a first test with an energy-conserving rule, saturating after ~50 ticks. The mechanism is therefore two-stage, and the stages have different jobs: a seed supplies the symmetry breaking, the nonlinearity supplies a **bounded** gain. The rule must be energy-conserving for the measurement to mean anything (§2.1a).

- **P4 — Transfer is pairwise, and gated by fit *within a width*.** Because the spill is symmetric, energy enters a new sheet *in both directions at once* — a candidate account of why particles arrive in particle/antiparticle pairs. The arriving energy must also **fit** a mode the target sheet can host: an exact fit makes a particle; less than a whole quantum merges into that sheet's background; more than a whole quantum leaves the surplus as momentum in S.

  **One caution on the pairing, learned from a first test.** Generated compact windings do come out exactly balanced between +n and −n. That is *not* evidence for particle/antiparticle pairing: a real-valued field has Hermitian Fourier symmetry, so |F(−n)|² = |F(+n)|² identically, whatever the dynamics. The balance is automatic and carries no physics. A genuine test needs a **complex** field, where +n and −n are distinct states and charge is the winding, as [metric-charge](../metric-charge/) and the Kaluza–Klein reading both require. Until that is run, P4's pairing claim is unsupported rather than supported.

  "Fit" should mean **close enough to happen**, not exactly degenerate. Exact degeneracy is never the physical condition — a mode with a finite lifetime has a finite width, and transitions proceed across that width. The project therefore needs a width as well as a centre, and the width is itself a prediction: it should come out of the geometry rather than being fitted. Note the width is a *separate* mechanism from the phase-space spreading of §3's fourth correction, and the two must not be conflated: a width decides **which** channels open, phase space decides **how** the energy distributes once one has.

- **P5 — Background fluctuation is not merely the trigger; it is structurally required.** P2's theorem says a symmetric rule acting on a symmetric state produces no cross-sheet transfer *ever*. The symmetry has to be broken by something, and the only candidate on offer is the background. This promotes P5 from a story about randomness to a load-bearing part of the mechanism: **without a seed there is no cross-sheet physics at all**, and grid-matter reached the same conclusion empirically when it had to add a vacuum-noise field to see anything. A mode already circulating on its sheet has nowhere to go under P2 alone, which is why it persists. Zero-point fluctuation pushes nodes over the saturation threshold intermittently and at random. A decay happens when a fluctuation coincides with an exit that satisfies every conservation law at once. Decay is therefore a **coincidence** process — which is the right statistical shape, since coincidence processes are memoryless and give the observed exponential decay law, whereas a steadily accumulating load would not.

- **P6 — Domains are ordered by state density, not by energy.** Energy is conserved at every transition; what changes is the number of states the energy can occupy. S is the **widest** destination, not the lowest — for a given total energy, putting it into momentum buys vastly more phase space than putting it into rest mass, because phase-space volume grows as p² dp and rest mass contributes no momentum at all. High-energy modes decay quickly because wider destinations are always available; the neutron is slow because few exits are open; ordinary matter endures because its exits are closed.

- **P7 — What closes an exit is a conservation law, not a lack of room.** The proton has somewhere energetically lower to go (p → e⁺ + π⁰ is far downhill in rest mass) and does not go there. What forbids it is baryon-number conservation; what protects the electron is charge, a topological winding. The ladder of P6 sets *direction*; conservation sets *reachability*.

  **How absolutely it is closed is an open fork, and the two branches are distinguishable.** Grand Unified Theories do predict proton decay, at lifetimes of order 10³⁴–10³⁶ years; the Standard Model on its own does not, since baryon number is an accidental symmetry there, broken only by non-perturbative effects at utterly unobservable rates. Experiment has not seen it — Super-Kamiokande bounds the p → e⁺π⁰ channel above ~10³⁴ years. So:

  - **(a) Hard law.** Baryon number is a topological invariant and cannot change at all; the rate is exactly zero. This is what [baryon-number.md](../ma-domain/work/baryon-number.md)'s cut-space account would give, since a cut invariant cannot change continuously.
  - **(b) Astronomically narrow channel.** Nothing forbids it absolutely; the configuration that would allow it is merely so improbable that the lifetime is enormous. This is what P3 and P5 give naturally, since a coincidence process has no exactly-zero rate.

  The framework's existing candidate points at (a) and this project's mechanism points at (b), which is a **genuine internal tension to resolve rather than paper over**. It is also the project's sharpest potential prediction: under (b) the proton lifetime is a number to be computed, and the target is ≳ 10³⁴ years — about 10⁶⁵ internal cycles, or a per-cycle probability below ~10⁻⁶⁵.

### 2.1a Where the difficulty actually sits

P2 being a theorem is good news and bad news in equal measure. Good: sheet-closure needs no postulate. Bad: **it closes the sheets too well.** If a translation-invariant rule can never generate compact winding, then saturation cannot open the channel either, however hard it is driven — and that is not a conjecture, it is the same equivariance argument run forwards. A perfectly symmetric lattice in a perfectly symmetric state has no cross-sheet physics at all: no decay, no pair production, nothing.

This explains grid-matter's negative result at theorem level rather than as a failed implementation. It also matches what that project observed directly: *"The symmetry-breaking must be present **at** the collision — which is physical: real pair production is seeded by vacuum fluctuations, not carried in on the beam."*

So the project's real question moves, and sharpens:

> **What breaks the symmetry, and can a seed-plus-amplification mechanism reach observed rates?**

A first measurement says the two-stage picture is alive, with one methodological lesson attached.

A **clipping** saturation rule appears to raise the winding *fraction* 24-fold — and that reading is an artifact. Clipping is lossy, and it destroys the zero-winding sector faster than the winding sector, so the ratio climbs while the **absolute** winding content *falls* (25.4 → 5.4 over the run). A lossy rule cannot distinguish transfer from selective dissipation, and no ratio taken across one is evidence of either.

Repeating it with an **energy-conserving** nonlinearity settles it. Replacing the clip with a Givens rotation whose angle grows above threshold — manifestly orthogonal, so exactly lossless — gives, with total energy held to a drift of 1.4 × 10⁻¹⁴:

| run | winding content, start → end |
|---|---|
| conserving rule, symmetric seed | **0 → 0**, exactly |
| conserving rule, symmetry-broken seed | 61.8 → **6.2 × 10⁴** |
| linear control, same broken seed | 23.9 → 25.4 (flat) |

So the transfer is real — roughly **2,500×** the linear control at matched seed and normalisation — and it **plateaus by about 50 ticks** rather than running away. The gain is bounded, which is the number that decides whether vacuum-scale seeding can reach physical rates.

**Two things this does not show, and they are the project's actual content.** The rotation was applied between a chosen pair of registers: *which* sheets couple, and by what angle law, was put in by hand rather than derived. And the plateau height depends on parameters that were picked arbitrarily. The demonstration is that a conserving, symmetry-respecting nonlinearity *can* transfer; everything about how much and between what remains open.

**Methodological rule adopted from this.** No transfer claim in this project rests on a ratio unless it is measured against an energy-conserving control. The clipping artifact above is the second time in this line of work that a ratio moved for the wrong reason — the first being a fringe-spacing statistic in grid-matter that tracked an envelope rather than the quantity named.

### 2.2 What the proposal would buy

If P1–P3 hold, three things that forma currently assumes become derived:

1. **The charge-selection rule.** The hoped-for argument is that a mode confined to a single dimension never takes part in the two-edge split that defines a plane, so it has no circulation and hence no electromagnetic coupling — which would give Candidate III's "winding in at least two dimensions" from the dynamics instead of positing it, and decide 3-torus.md's open verdict. **This is a target, not a result, and P2's calculation makes it harder than it first looked:** under the uniform rule a 1D-line mode still scatters at every node, so the argument cannot simply be "it does not participate." It has to show the circulation integral vanishes for n_j = 0 *for a reason other than restating the formula*. Chapter 2 is where that is attempted, and failing it is a real possible outcome.
2. **Plane-over-diagonal.** [ma-domain architecture.md §3.3](../ma-domain/work/architecture.md) rules that particles live on 2D dim-pairs and that fully 3D-mixed modes are dark. Its justification today is an energy count. P2's equivariance theorem would make a sheet *dynamically* closed rather than merely expensive — a mechanism where there is currently only a cost argument, and one that holds for nonlinear rules too.
3. **Why inter-sheet coupling is weak.** If cross-sheet transfer happens only on overflow, its weakness is structural rather than fitted. [sheet-proton clover-quarks.md](../sheet-proton/work/clover-quarks.md) names this as a thing the framework needs: *"showing that the inter-sheet coupling factor naturally gives the observed weak coupling strength g_W."*

---

## 3. Corrections already folded in

The premises above are a revised form of the originating notes. Four things in the first formulation did not survive scrutiny and have been changed rather than carried forward.

| Original | Problem | Replaced by |
|---|---|---|
| S is the "lowest," most economical state for energy | A 511 keV photon and an electron at rest are *exactly* energy-degenerate; S is not lower | P6 — S is the **widest** state; the ordering is by state count, and the preference scales as ln(V/λ³) |
| The proton is stable because "there is nothing lower" | False — p → e⁺ + π⁰ is hugely downhill in rest mass | P7 — stability is **baryon number**, flagged in [mode-stability.md §3](../ma-domain/work/mode-stability.md) as assumed, not derived |
| Emitting in both directions at once explains particle **pairs** | Back-to-back emission gives *linear* momentum balance only; it does not forbid emitting one fermion | Open — see [§4](#4-known-obstructions) |
| In β decay the electron and neutrino energies "just fit" the neutron–proton gap | They do not: the gap is 1.293 MeV, the electron 0.511 MeV, the neutrino ≈ 0, and the remaining 0.782 MeV is a *continuous* spectrum | Fit governs **whether** a channel opens — a threshold (the gap must exceed m_e), satisfied *within a width* rather than exactly (P4). S then absorbs whatever is left over, always and continuously |

The fourth correction is the sharpest constraint on the whole family of threshold models and is worth stating plainly: **a fit-based mechanism may gate the rate, but it must not imprint structure on the partition.** The measured β spectrum is smooth from zero to its endpoint, and that smoothness is precisely how the third body was inferred in the first place.

---

## 4. Known obstructions

Named up front, because each is a recorded result that this project has to get past rather than rediscover.

- **The pump.** grid-matter tried two saturation responses (clip, spillover) and neither moved energy durably into the compact sector: they are *"per-edge, per-tick responses; they do not phase-lock energy into the stable n ≥ 1 eigenmode, and the linear scatter undoes their redirection each tick"* ([results-m1-m2.md](../grid-matter/work/results-m1-m2.md)). **Now explained, and the explanation is worse than the symptom.** P2's equivariance theorem says *no* translation-invariant rule, linear or not, can move energy across sheets — so the missing pump was not a defect of clip and spillover but a consequence of symmetry. The route forward is therefore not a better nonlinearity but a **symmetry-breaking seed plus amplification** (P5, P3). The pump test must supply the seed explicitly; without one its result is predetermined.

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

- **Setup.** Two waves launched from opposite ends of the extended axis, colliding at a point. Saturation condition stated on the node's summed input T. **A symmetry-breaking background must be switched on** — per P2 the run is predetermined to return exactly zero without one, so a null result from an unseeded run would mean nothing. Measure energy retained in the compact sector long after the drive is gone, differenced against a same-seed control so the static background floor cancels.
- **Measure the gain, against a conserving control.** The informative quantity is the compact-sector content with the nonlinearity against the same run without it, at the same seed — and the nonlinearity must be energy-conserving, or the comparison measures dissipation rather than transfer (§2.1a). A bench test on a bare periodic lattice gives ≈ 2,500× with a plateau; whether that survives the collision geometry, and how the plateau scales with seed amplitude and nonlinear strength, is the result.
- **Prediction, in the sharper form.** Not merely that energy persists, but that **the retained amount is quantized to the compact sector's mode ladder.** Only a portion matching a mode the sheet can host self-consistently should stay; the remainder should disperse back out or settle into the background. The discriminating signature is therefore a **staircase**: retained energy versus drive amplitude should show plateaus at the sheet's mode spacing, not a smooth rise. That also reframes an earlier result — grid-matter's amplitude sweep found retention *"peaks at ~2% then falls to 0%,"* read at the time as the opposite of a soliton; under this prediction the quantity to look for in such a sweep is plateaus, not monotonic growth.
- **Why the sharper form is better.** "Does energy persist" can be satisfied by ordinary slow leakage and by a static background floor — the latter already produced one false positive on this testbed. Quantized retention cannot be faked by either.
- **If it fails.** The transfer thesis joins grid-matter's instructive negatives, and this project continues on chapters 2–3, which do not depend on it.

### 5.2 The background-spectrum test — in [grid-quantization](../grid-quantization/)

What happens to energy that does not fit a resonant mode is that project's charter, and its Tier 2 is unstarted.

- **Setup.** Inject broadband, deliberately non-resonant energy into a compact dimension. A wave whose wavelength does not divide the circumference must become self-consistent on returning to its starting point. Watch what disperses back out, and what continues to circulate.
- **Prediction.** The residual converges on a mean energy of ½ℏω₁ — half the fundamental.
- **Why it matters.** [ma-domain zpe_derivation.md](../ma-domain/work/zpe_derivation.md) obtains that value from two postulates, of which the second — a uniform spectral density across the sub-fundamental band — is flagged *"not derived, but it has a clean informational justification."* A positive result turns a postulate into a consequence of the dynamics. A negative one is equally informative.
- **A note on the extended axis.** The same argument applied to S requires S to be periodic, if very large. That is not a free assumption — it is one forma already makes without saying so: [ma-domain architecture.md §2](../ma-domain/work/architecture.md) labels modes with *integer* windings on the spatial axes, which only a compact S admits. A result here would give that silent assumption a job.

  **What periodicity can and cannot supply.** The attractive reading is that zero-point energy simply *is* what random non-resonant waves do in a closed space — which would make it an artifact of periodicity and back into evidence for a periodic S. That reading needs splitting in two, because the halves have different standing.

  - **Shape — plausibly derivable.** Periodicity is what makes "sub-fundamental" a meaningful category at all: in a closed compact dimension there are no modes below ω₁, so the band below it has no resonances and no structure. That is exactly the premise [zpe_derivation.md](../ma-domain/work/zpe_derivation.md) needs for Postulate 2's flat spectral density, and it is what this test can see.
  - **Amount — not derivable this way.** Periodicity gives a discrete *spectrum*; it does not give a non-zero *occupation*. A classical linear periodic lattice has a zero-energy ground state, and sharing injected energy out classically gives kT per mode, not ℏω/2 — the Rayleigh–Jeans result, not the quantum one. The step to ½ℏω₁ runs through Postulate 1's action quantum per cycle, which is where ℏ enters as a unit. Per the project's principle-versus-scale rule, that is not a failure; it just means the amount is set elsewhere.

  So the defensible version of the idea is: **periodicity sets the spectrum's shape, initial conditions set its amount.** That has a sharp falsifiable consequence this test can check — the predicted *shape*, and hence the ½ω₁ mean in units of the fundamental, should be **independent of how much energy is injected**. If the mean drifts with injection, the picture is wrong.

  Two further notes. The claim would in any case be **consistency with** periodicity rather than proof, since vacuum energy arises in mechanisms needing no closed topology. And there is an empirical bound to respect: searches for matched circle pairs in the cosmic microwave background have found none, placing any fundamental domain at or beyond the scale of the observable universe — so the prediction to make is about the spectrum, not the size of S. A related thread already exists in the repo: [threshold-dynamics.md §11](../ma-domain/work/threshold-dynamics.md) proposes using Casimir-effect scaling to discriminate between preload hypotheses, and the Casimir effect is the standard case of vacuum energy responding to boundary and topology.

---

## 6. Chapter arc — preliminary

Deliberately provisional; the ordering past chapter 3 depends on what §5 returns. Status flags follow grid-matter's convention: **[D]** derivable now · **[C]** computationally demonstrated · **[P]** posited link · **[O]** open.

| # | Chapter | Rests on | State |
|---|---|---|---|
| 1 | **The rule.** Sheet-labelled edges and sheet-closed scattering, written as a candidate update rule in the format of [grid-duality's model notes](../grid-duality/models/), and run against that project's test bench for stability and fidelity. | P1, P2 | **[O]** |
| 2 | **Selection rule I — the 1D tower.** Does sheet-closed scattering dynamically suppress the electromagnetic coupling of 1D-line modes? A pass derives Candidate III and settles 3-torus.md's open verdict. Needs no saturation. | ch. 1 | **[O]** |
| 3 | **Selection rule II — plane over diagonal.** [architecture.md §3.3](../ma-domain/work/architecture.md) rules 3D-mixed modes dark on an energy count. P2's equivariance theorem looks like the missing mechanism — a mode with zero winding on the third axis cannot acquire any — so the chapter's job is to check that it covers the *3D-mixed* case as stated there, and to say what residual work the energy count is still doing. Needs no saturation. | ch. 1, P2 | **[O]** |
| 4 | **The channel.** What opens cross-sheet transfer, and does the transfer survive the next tick. Gated on §5.1. | P3, §5.1 | **[O]** |
| 5 | **The rate.** The leakage law [leakage-rate.md](../ma-domain/work/leakage-rate.md) is missing: what sets the cross-sheet rate, and does it give ~α on the electromagnetic channel and the right smallness on the weak one. | ch. 4 | **[O]** |
| 6 | **Direction and balance.** Does an overflow-only channel respect microreversibility, and does the net direction come out as the state-density ordering of P6 rather than needing to be imposed. | ch. 4, P6 | **[O]** |

Chapters 2 and 3 are independent of saturation. If the channel work fails, those two still stand on their own and still deliver something ma-domain needs.

---

## 7. What success looks like

- **Floor.** A symmetry-breaking seed with a defensible origin, and a measured amplification factor. P2 is settled; what replaces it as the foundational question is whether seed-plus-gain can reach physical rates at all. A mechanism that needs a seed larger than the vacuum plausibly supplies is a dead end, and finding that out early is worth more than any downstream fit.
- **Minimum.** A derived selection rule replacing Candidate III's posit — chapters 2 and 3 pass, and 3-torus.md's conditional verdict resolves one way or the other.
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

Ordered cheapest-and-most-decisive first. The precursor experiments of §5 are **not** the place to start: both are more expensive than the gating question, and §5.1 in particular is currently uninterpretable, since the saturation rules in its lineage (clip, spillover) are lossy and a lossy rule cannot separate transfer from selective dissipation.

1. **The bounded-gain test** — the real first experiment, and a prototype already runs. On a bare periodic three-axis lattice with an energy-conserving nonlinearity and a symmetry-breaking seed, measure absolute winding content against time, and map the **plateau height** as a function of seed amplitude and nonlinear strength. *Pre-registered question:* does the plateau scale in a way that lets a vacuum-scale seed reach physical rates, or is it capped near the seed? A cap is a kill result and is worth having in an afternoon rather than after a collision rig is built.
2. **Write up the equivariance result** — the project's first real finding, arrived at before any chapter was drafted. It reframes grid-matter's missing pump as a symmetry consequence rather than an implementation failure, and it belongs in a work file with the numerics attached.
3. **Re-run the P4 pairing check on a complex field**, since the real-field balance observed so far is Hermitian symmetry and carries no physics.
4. **Then** §5.1 (pump) and §5.2 (background spectrum), re-scoped around whatever step 1 returns — §5.1 with a conserving rule and an explicit seed.
5. Draft chapter 1's rule as a model note, and check it on grid-duality's test bench for stability and wave fidelity before asking it to do any physics.
6. Revisit this arc. Chapters 4–6 are provisional and should be re-cut around what steps 1–3 show.
