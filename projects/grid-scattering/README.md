# grid-scattering

**What sets the rate at which energy crosses between GRID's compact sectors — and into space?**

**Type:** Exploratory project (see [../README.md](../README.md))
**Status:** Framing. No chapters, no code in the project yet. The first work item is a simulation — get a standing wave onto the ring, then look at what the energy did.

**Scope.** The point is to test one mechanism: **saturation and overflow as the means by which energy crosses a sheet boundary.** The project is not required to stay harmonious with earlier forma work — where it departs, it says so and the departure is part of what is being tested. If the mechanism works it changes how several things are read; if it fails, it gets parked and the failure is the result. Supporting material is in [Appendix.md](Appendix.md).

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

**This is less of a departure than it first looks.** forma's sheet architecture already treats sheets as *separate objects* with coupling supplied by something else — [model-A](../../models/model-A.md) has three material sheets joined by cross-shears, and [leakage-rate.md](../ma-domain/work/leakage-rate.md) assumes energy moves between sheets only through a leakage channel whose law is unknown. The per-sheet node is that same picture written at node level: separate in the ordinary run, coupled by a specific named event. What is new is only the event. What any such rule still owes is a pass on [grid-duality's test bench](../grid-duality/03-test-bench.md) — it has to keep giving wave behaviour inside a sheet.

## 3. What makes the groups talk

GRID is **discrete and finite**. That is a foundational commitment, not a modelling convenience, and it has a consequence: a register can only hold so much. Below that ceiling the scatter is linear and the groups stay separate. Above it they cannot, because a ceiling is not a linear function. Saturation is not an extra ingredient — it is what "discrete and finite" means, and with a base-2 register it is unavoidable.

So the picture is a pipe with a side branch. Fire a shotgun down the main pipe and the shot sails past the junction: one signal, under the ceiling, stays in its plane. Fire a shotgun from **each** end so the shot meets at the junction and the sum exceeds what the junction can carry. Only there does the medium stop being linear, and only there can pellets run off sideways down the branch.

When a node overflows, the excess has to go somewhere, and the places left are the edges of the *other* groups. It goes **both ways at once** — which is what keeps momentum balanced across a ninety-degree turn, since equal amounts leave in opposite directions.

**And that bidirectional spill is not a cancellation. It is the particle.** Equal energy running both ways around a ring is a standing wave, and a standing wave captive on a loop is exactly what [metric-mass](../metric-mass/) identifies as a particle at rest — the ±n superposition, one particle rather than two. The thing that looks like perfect balance is the thing being made.

**The compact dimension is the capacitor.** Earlier attempts at a discrete substrate had to invent storage *inside* the node — a carry register holding the overflow and dispensing it over later ticks — to keep the books. grid-matter's verdict on that was that it is faithful on average but inert: it recovers ordinary dispersion and traps nothing. Here the storage is somewhere physical instead. Overflow jumps into c, sits there as a standing wave, and comes back down into x later when c itself saturates. Discreteness and conservation stop pulling against each other, because the excess was never discarded — it was parked.

**So the mechanism runs both ways, and the reverse direction is decay.** x → c on overflow makes a particle; c → x on overflow in the ring returns it to radiation. One rule, two processes, and no separate account of decay is needed.

**And it should be running all the time.** If background fluctuation is always present, saturation events are not rare dramatic episodes but a steady low-level traffic in both directions, continuously settling energy mismatches between a sheet and the space around it. That predicts an *equilibrium* between sheets rather than a one-way flow — which is a testable thing to look for, and a place the model could fail outright if the traffic runs only one way.

Mass follows from how much circulates. *Charge* is a later matter, reached only at the next wrap where a second closed direction is added ([grid-duality ch. 7](../grid-duality/07-wrap-promotion-modeling.md)); on a single ring there is mass and no charge.

**Honest footing.** The principle is forced; the implementation is open. [grid-duality ch. 5](../grid-duality/05-substrate-quantization.md) found naive rounding breaks the dynamics and declined to commit; [grid-matter](../grid-matter/work/results-m1-m2.md) found hard rounding froze its lattice outright. Building a saturating rule that neither freezes nor leaks is the first hazard, and a concrete thing this project could contribute.

### The arena, cut down

Many compact dimensions and several sheets, reduced to **two** so the interaction can be studied with nothing else in the way.

- **Arena.** A cylinder: an extended direction x, and a compact ring c at every point along x. Two groups per node — the x-group and the c-group.
- **Below the ceiling.** The groups are separate. Energy runs along x and the ring stays empty.
- **At saturation.** A node whose summed input exceeds the ceiling clips, and the excess is ejected into the c-group, half each way around the ring. The connection exists *only* during the overflow and *only* at that node. Several nodes may overflow at once.
- **Result.** Two counter-propagating waves. A wavelength that fits the circumference persists; one that does not returns to x or disperses.

**Energy conservation is to be measured, not engineered.** Clipping x and moving the excess onto the c-edges will not conserve energy exactly, since energy goes as amplitude squared and equal amplitudes are not equal energy. That is fine for now: run it, measure the total before and after, and let the size and sign of the discrepancy be data.

## 4. Objectives

1. **Make a particle, then get it back.** Drive the collision to overflow and see whether a standing wave establishes on the ring and outlives the drive — which modes take the energy, and does a non-fitting wavelength really fail to persist. Then the reverse: does the ring eventually saturate and return its energy to x? Creation and decay from one rule.
2. **Find out how fast it builds.** Whether repeated overflow **accumulates**, and how that depends on drive strength and ring size. A rate, not a final amount.
3. **Check the rate against ones forma already gets right.** [leakage-rate.md §4](../ma-domain/work/leakage-rate.md) recovers Sargent's rule — weak decay rates rising as the fifth power of the energy released — and lepton universality to about 0.2%, from counting available final states alone. Any mechanism here has to reproduce that, or show how it combines with that counting to give it. The neutron's 880 s lifetime is the anchor.
4. **Say what the mechanism forbids.** A rule that permits everything explains nothing.

**Success** is objective 1 with a clear answer on 2. **A failure worth having** is a rate that demonstrably cannot span the observed couplings, or traffic that runs only one way — either, reported as such, is a result.

## 5. First work item

**Simulate, then model.** [AGENTS.md](../AGENTS.md) prefers a derivation where one is available, and allows computation first where the insight to derive is missing. It is missing here: the overflow rule is not yet written down concretely enough to analyse, and the cheapest way to find out what it does is to run it.

Run §3a and watch three things that are easy to confuse:

- **Does it ring?** Energy landing on the loop should start oscillating within about one trip around. The easy part; it would be surprising if it failed.
- **Does it stay?** After the pulses pass, does the ring keep its wave? Sweep circumference against drive wavelength — a fit should persist, a misfit decay.
- **Does it build?** With repeated overflows, does the ring's content grow, and how fast? This is the one that becomes a rate.

Control with clipping switched off. Report rates, not final amounts: where a nonlinearity stops says nothing about how fast it got there, and a ratio against a flat baseline just grows with run length.

## 6. Next steps

1. **Build the saturating rule and run §5.** A clip that freezes the lattice or bleeds energy is no use; clearing that is step one of step one.
2. Then rates, and only then. Two deferred questions — when the substrate must stop being real-valued, and how the per-sheet node behaves once sheets share a dimension — are parked in [Appendix.md](Appendix.md). Neither blocks the simulation, and per the scope note above neither has to be settled in forma's existing terms first.

## 7. Relation to other projects

**Not a revival of grid-saturation.** grid-matter was renamed from `grid-saturation` because its entry hypothesis — that the saturation bound *binds a particle* — was refuted. This project concerns **transfer**, not binding, and grid-matter's own work file keeps that distinction open: *"This is 'not yet,' not 'refuted.'"*

- [ma-domain](../ma-domain/) — the principal consumer: [leakage-rate.md](../ma-domain/work/leakage-rate.md) names the missing law, [threshold-dynamics.md §6.2](../ma-domain/work/threshold-dynamics.md) the missing mechanism.
- [grid-matter](../grid-matter/) — the saturation history and the (x, c) cylinder testbed; its M1 run verified the cylinder as a faithful arena.
- [metric-mass](../metric-mass/) — the target object: a particle is a standing wave around the compact dimension, the ±n superposition, one particle rather than two.
- [grid-duality](../grid-duality/) — closed; the scatter, the candidate-model format and the test bench any new rule must pass.
- [grid-primitive](../grid-primitive/), [grid-quantization](../grid-quantization/) — the edge/node primitive, and the home for any zero-point question that survives.
