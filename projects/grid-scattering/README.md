# grid-scattering

**What sets the rate at which energy crosses between GRID's compact sectors — and into space?**

**Type:** Exploratory project (see [../README.md](../README.md))
**Status:** Framing. No chapters, no code in the project yet. The first work item is a simulation — get a standing wave onto the ring, then look at what the energy did.

Supporting material — glossary, the originating premises, obstructions, and the record of what has been discarded and why — is in [Appendix.md](Appendix.md). This file stays short on purpose.

---

## 1. The question

Energy demonstrably moves between forma's domains. Two gamma rays make an electron–positron pair; a neutron becomes a proton, an electron and an antineutrino; a charged particle radiates into space. The rates differ by many orders of magnitude and the framework does not say why.

forma has the gap written down twice. [ma-domain leakage-rate.md](../ma-domain/work/leakage-rate.md) files a caveat against its own working assumption — coupling without a shared dimension *"demonstrably exists"*, so *"the leakage graph is richer than the metric-sharing graph"* — and [threshold-dynamics.md](../ma-domain/work/threshold-dynamics.md) sits parked on its §6.2: by what physical mechanism does energy reorganise from a background band into a discrete mode? This project proposes a node-level answer and tests it.

## 2. The proposal: a node's edges are grouped by sheet

GRID's scatter is normally written as though a node pools **all** its edges into one operation — S = (2/N)·J − I across every register it has — so a share of whatever arrives goes out along every edge, including edges pointing into other sheets.

This project proposes something else:

> **A node's edges are grouped by the sheet they belong to, and each group scatters on its own.** A node taking part in three sheets runs three independent scatters, not one large one.

Inside a group the rule is the familiar one. Information arriving on one edge of a Y junction splits between the other two edges **of that same sheet**, and does not travel back the way it came, because the rule subtracts the register's own prior content.

The consequence is the whole point. **In linear operation, orthogonal sheets see none of each other's energy** — not a small amount that cancels out, none at all. Information keeps going the way it was going, in the plane it was going in. Reaching another sheet would mean turning ninety degrees, and nothing in linear operation turns a corner.

This is new. Nothing in the repo proposes a per-sheet node, and nothing in it rules one out either; the uniform form is simply what has always been written. Replacing it is this project's substantive claim, and [grid-duality's test bench](../grid-duality/03-test-bench.md) is where any such rule has to prove it still gives wave behaviour.
<!--EC In fact, I'd venture that some past efforts have assumed that nodes belong only to a given sheet and then there is some yet-unknown leakage that transfers energy (at alpha rate) between various sheets. -->

## 3. What makes the groups talk

GRID is **discrete and finite**. That is a foundational commitment, not a modelling convenience, and it has a consequence: a register can only hold so much. Below that ceiling the scatter is linear and the groups stay separate. Above it they cannot, because a ceiling is not a linear function. Saturation is not an extra ingredient — it is what "discrete and finite" means, and with a base-2 register it is unavoidable.
<!--EC and in past efforts, we had to invent a storage mechanism inside the node to store the overflow and dispense it on subsequent cycles in order to conserve energy.  In this proposed regime, the compact dimension becomes the capacitor.  Overflow can jump into c and, at some random moment, jump back down (consequence of a saturation in c) into x.  Energy conserved (possibly). -->

So the picture is a pipe with a side branch. Fire a shotgun down the main pipe and the shot sails past the junction: one signal, under the ceiling, stays in its plane. Fire a shotgun from **each** end so the shot meets at the junction and the sum exceeds what the junction can carry. Only there does the medium stop being linear, and only there can pellets run off sideways down the branch.

When a node overflows, the excess has to go somewhere, and the places left are the edges of the *other* groups. It goes **both ways at once** — which is what keeps momentum balanced across a ninety-degree turn, since equal amounts leave in opposite directions.

**And that bidirectional spill is not a cancellation. It is the particle.** Equal energy running both ways around a ring is a standing wave, and a standing wave captive on a loop is exactly what [metric-mass](../metric-mass/) identifies as a particle at rest — the ±n superposition, one particle rather than two. The thing that looks like perfect balance is the thing being made.

Mass follows from how much circulates. *Charge* is a later matter, reached only at the next wrap where a second closed direction is added ([grid-duality ch. 7](../grid-duality/07-wrap-promotion-modeling.md)); on a single ring there is mass and no charge.

**Honest footing.** The principle is forced; the implementation is open, and two projects have hit the wall already. [grid-duality ch. 5](../grid-duality/05-substrate-quantization.md) tested a discrete-level substrate, found naive rounding breaks the dynamics, and declined to commit either way; [grid-matter](../grid-matter/work/results-m1-m2.md) found hard rounding froze its lattice outright. Both name the same unbuilt path — a bit-conservative, lattice-gas-style collision rule. Supplying a saturating rule that neither freezes nor leaks is a concrete contribution this project could make, and it is the first hazard the simulation must clear.

## 3a. The arena, cut down

Many compact dimensions and several sheets, reduced to **two** so the interaction can be studied with nothing else in the way.

- **Arena.** A cylinder: an extended direction x, and a compact ring c at every point along x. Two groups per node — the x-group and the c-group.
- **Below the ceiling.** The groups are separate. Energy runs along x and the ring stays empty.
- **At saturation.** A node whose summed input exceeds the ceiling clips, and the excess is ejected into the c-group, half each way around the ring. The connection exists *only* during the overflow and *only* at that node. Several nodes may overflow at once.
- **Result.** Two counter-propagating waves on the ring. If their wavelength fits the circumference they persist as a standing wave — a particle at rest. If it does not fit, the energy returns to x or disperses.

**Energy conservation is to be measured, not engineered.** Clipping x and moving the excess onto the c-edges will not conserve energy exactly, since energy goes as amplitude squared and equal amplitudes are not equal energy. That is fine for now: run it, measure the total before and after, and let the size and sign of the discrepancy be data.

## 4. Objectives

1. **Make a particle.** Drive the collision hard enough to overflow and see whether a standing wave establishes on the ring and outlives the drive. Which ring modes take the energy, and does a non-fitting wavelength really fail to persist? The plainest question, and the first.
2. **Find out how fast it builds.** Whether repeated overflow **accumulates**, and how that depends on drive strength and ring size. A rate, not a final amount.
3. **Check the rate against ones forma already gets right.** [leakage-rate.md §4](../ma-domain/work/leakage-rate.md) recovers Sargent's rule — weak decay rates rising as the fifth power of the energy released — and lepton universality to about 0.2%, from counting available final states alone. Any mechanism here has to reproduce that, or show how it combines with that counting to give it. The neutron's 880 s lifetime is the anchor.
4. **Say what the mechanism forbids.** A rule that permits everything explains nothing.

**Success** is objective 1 with a clear answer on 2. **A failure worth having** is a buildup rate that demonstrably cannot span the range of observed couplings — reported as such.

## 5. First work item

**Simulate, then model.** [AGENTS.md](../AGENTS.md) prefers a derivation where one is available, and allows computation first where the insight to derive is missing. It is missing here: the overflow rule is not yet written down concretely enough to analyse, and the cheapest way to find out what it does is to run it.

Run §3a and watch three things that are easy to confuse:

- **Does it ring?** Energy landing on the loop should start oscillating within about one trip around. The easy part; it would be surprising if it failed.
- **Does it stay?** After the pulses pass, does the ring keep its wave? Sweep circumference against drive wavelength — a fit should persist, a misfit decay.
- **Does it build?** With repeated overflows, does the ring's content grow, and how fast? This is the one that becomes a rate.

Control with clipping switched off. Report rates, not final amounts: where a nonlinearity stops says nothing about how fast it got there, and a ratio against a flat baseline just grows with run length.

## 6. Next steps

1. **Build the saturating rule and run §5.** The first hazard is the one §2 names: a clip that freezes the lattice or bleeds energy is no use. Clearing that is step one of step one.
2. **Restate the motivating problem in ma-domain's current architecture.** The unobserved-mode-tower problem this project set out from comes from [3-torus.md](../ma-domain/work/3-torus.md), which calls itself historical and predates the dim-pool reading now in use. Until it is restated it is not clear the project is solving a problem ma-domain still has.
3. Only then, any claim about rates. Two deferred questions — when the substrate must stop being real-valued, and whether a node rule could carry directional preference — are parked in [Appendix.md](Appendix.md); neither blocks the simulation.

## 7. Relation to other projects

**Not a revival of grid-saturation.** grid-matter was renamed from `grid-saturation` because its entry hypothesis — that the saturation bound *binds a particle* — was refuted. This project concerns **transfer**, not binding, and grid-matter's own work file keeps that distinction open: *"This is 'not yet,' not 'refuted.'"*

- [ma-domain](../ma-domain/) — the principal consumer. [leakage-rate.md](../ma-domain/work/leakage-rate.md) names the missing law; [threshold-dynamics.md §6.2](../ma-domain/work/threshold-dynamics.md) names the missing mechanism.
- [grid-matter](../grid-matter/) — owns the saturation history and the (x, c) cylinder testbed the simulation would use.
- [metric-mass](../metric-mass/) — supplies the target object: a particle is a standing wave around the compact dimension, the ±n superposition, and is **one** particle rather than two.
- [grid-duality](../grid-duality/) — closed; supplies the uniform scatter, the candidate-model format and the test bench.
- [grid-primitive](../grid-primitive/) — the edge/node primitive, and the two-real-DOF option in step 3.
- [grid-quantization](../grid-quantization/) — would own any zero-point-spectrum question, if one survives (see [Appendix.md](Appendix.md)).
