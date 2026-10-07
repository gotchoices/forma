# grid-scattering

**What sets the rate at which energy crosses between GRID's compact sectors — and into space?**

**Type:** Exploratory project (see [../README.md](../README.md))
**Status:** Arena built and running. Energy crosses on overflow, the crossing is resonant, and the junction geometry is settled analytically. Nothing yet shows a particle that *moves* — that is objective 2 and the next thing to find out. Checklist: [work/STATUS.md](work/STATUS.md).

**Scope.** The point is to test one mechanism: **saturation and overflow as the means by which energy crosses a sheet boundary.** The project is not required to stay harmonious with earlier forma work — where it departs, it says so and the departure is part of what is being tested. If the mechanism works it changes how several things are read; if it fails, it gets parked and the failure is the result. Supporting material is in [Appendix.md](Appendix.md).

---

## 1. The question

Energy demonstrably moves between forma's domains. Two gamma rays make an electron–positron pair; a neutron becomes a proton, an electron and an antineutrino; a charged particle radiates into space. The rates differ by many orders of magnitude and the framework does not say why.

forma has the gap written down twice. [ma-domain leakage-rate.md](../ma-domain/work/leakage-rate.md) files a caveat against its own working assumption — coupling without a shared dimension *"demonstrably exists"*, so *"the leakage graph is richer than the metric-sharing graph"* — and [threshold-dynamics.md](../ma-domain/work/threshold-dynamics.md) sits parked on its §6.2: by what physical mechanism does energy reorganise from a background band into a discrete mode? This project proposes a node-level answer and tests it.

## 2. The junction, and what it is allowed to do

A node where space meets a compact sheet has four edges, not three — an **X** junction rather than a **Y**. That difference turns out to decide everything, and it is settled analytically in [work/junction-geometry.md](work/junction-geometry.md).

**At a symmetric Y junction there is no freedom.** The uniform rule S = (2/N)·J − I is the only symmetric rule that conserves both energy and momentum. The intuitive alternative — reflect a little, split the rest evenly between the two outgoing edges — balances momentum but loses a quarter of the energy. So the uniform rule is not momentum-preserving by accident; it is forced, and there is nothing at a Y junction for a node to be "aware" of. (It also does backscatter: −1/3 of the amplitude returns along the arrival edge, and that term is exactly what balances the momentum.)

**At an X junction there is freedom.** Pure **straight-through** — in on +x, out on +x, nothing crossing into c — is equally unitary and equally momentum-conserving. But the freedom is **discrete**: scanning every symmetric real rule that satisfies both conservation laws yields exactly four, isolated. There is no continuous knob, so "the orthogonal edges get a little, but not much" cannot be written as a symmetric linear rule.

### The posit, stated as one

> **Below the ceiling, the rule between space and a sheet is straight-through. Within space, and within a sheet, the ordinary scatter is unchanged.**

The partition is **space against a sheet**, not dimension against dimension. Space stays the GRID already shown to give Maxwell; nodes mix their spatial edges exactly as before. Compact dimensions simply do not participate until the dynamics goes nonlinear.

What is forced and what is posited should be kept apart. Being discrete and finite forces a **bound** — a register holds only so much. It does not force the excess to **redirect** into another group; a bounded register could equally clip and discard, or wrap. That the excess crosses into the other group is this project's posit, and it is the thing under test.

## 3. What crosses, and what it makes

**Scope of the ceiling (posit).** Each node has two degrees of freedom: it can saturate in its space group, in its sheet group, or in both. The test is on each group's own sum — not per edge, which grid-matter ruled out, and not on the node as a whole. A whole-node test is the live alternative, and it would let a ring wave and a passing space wave push a node over together; that is a different model and is not what is implemented.

**What the overflow does.** The excess leaves the saturating group and enters the other at one point, half each way, so it departs in both directions at once and meets itself on the far side of the ring. It must also **carry its x-momentum with it** — otherwise every particle is created at rest, which by §2 it could never leave. *This part of the rule is stated but not yet implemented; the current script injects symmetrically, so it can only make particles at rest. Implementing it is the first step of objective 2.*

**Energy bookkeeping, honestly.** Splitting an excess e into e/2 each way carries e²/2, not e², so the rule loses energy on every overflow with a fixed sign. That drift is a known bias rather than a measurement. The obvious repair — e/√2 each way — overshoots: it injects more amplitude than it removed and runs away once the reverse channel opens (tested; the ring reaches 10¹⁶). Exact conservation needs either explicit energy accounting, which imports a square root into an amplitude substrate, or a rotation. The drift is reported and the repair is queued.

**What forms.** Two counter-propagating waves on the ring. Equal energy both ways around a loop is a standing wave, and a standing wave captive on a loop is what [metric-mass](../metric-mass/) commits to as a particle at rest — the ±n superposition, one particle rather than two.

**And it can move.** Straight-through alone would leave an x-travelling wave and a circulating wave simply coexisting, shearing apart within a few ticks. What binds them is the nonlinearity: at a particle's core the amplitude is above the ceiling, so the groups exchange there continuously, and that exchange holds x-momentum and compact winding together as one object. **A moving particle would then be a soliton held together by saturation.** That is an argument, not yet a demonstration — it is exactly what objective 2 tests. In the tails, below the ceiling, nothing crosses — which is why sheets stay separate in ordinary propagation. One mechanism does creation, decay, and binding.

**Two conditions, not one.** Saturation is only the first: enough amplitude for energy to leak into a sheet at all. It does not make a particle. The second is **frequency** — the drive must resonate with the ring, or the leaked energy sloshes in and comes straight back. The resonant frequency is set by the ring and nothing else: measured at ω = 2π/nc across four ring sizes, with 12–58× more energy retained than at 8% detuning.

Each sheet therefore carries its own threshold, because each has its own circumference. And since the ring size fixes both the particle's mass and the wavelength that fits it, that threshold lands at the particle's own mass scale automatically — forced, not fitted. It also says why an intense laser makes no pairs: it saturates easily and energy does cross, but an optical frequency is nowhere near the electron ring's resonance, so nothing launches and the energy returns.

**The ceiling is not a free parameter.** Any ordinary travelling photon is by definition below it — otherwise light would saturate as it propagates and the vacuum would not be transparent. The ceiling is calibrated by an observable: *light must pass*. Three things follow with no further assumption. A lone photon never saturates, which is why pair production needs **two** photons, or a photon plus a nucleus's field standing in for the second. A collision is special precisely because two amplitudes sum at one node. And the **Schwinger limit becomes a prediction** rather than an input — it is where a single field, with no collision, finally reaches the ceiling alone.

### The arena, cut down

One linear array x; a ring at every x coordinate; line and ring joined only during an overflow, at one point. A product (nx × nc) grid is *wrong* — it is nc parallel lines, so a photon saturates every ring at once and injects uniformly, giving winding zero and no particle.

### What has been measured

Transfer happens, and it is **resonant**: 50–100× enhancement when the circumference is a whole multiple of the drive wavelength, sharp enough that one node either side kills it, selecting exactly the predicted mode (nc/λ = 1, 2, 3 → n = 1, 2, 3). At the strongest resonance the reverse channel opens unprompted. Details and the two bugs found on the way: [work/first-run.md](work/first-run.md).

This answers a standing objection that the arena has no selection mechanism — that a lossless ring accepts every pattern, so sweeping circumference measures nothing. That is correct for a **single pulse**, and was measured: ring content was identical at every circumference from 8 to 40. It is false under a **sustained** drive, where successive injections interfere. The selection is not the ring rejecting a pattern; it is coherent accumulation.

## 3a. What this arena cannot settle

Named here rather than discovered later.

- **The one bridge still owed: amplitude against frequency per quantum.** The ceiling has to sit *below* two colliding 511 keV gammas and *above* a bright optical beam — a tight constraint, and the thing that separates them cannot be photon count, since the beam has vastly more. It has to be frequency. The bridge is that a single quantum ℏω localised in about one wavelength carries energy density ∝ ω⁴, hence amplitude ∝ ω²: a gamma then has ~10¹¹ times an optical photon's amplitude *per quantum*, which puts two of them in the same range as a bright beam of ~10²⁰ optical photons. Self-consistent, and it is what makes the calibration above possible — but it imports ℏ into a classical arena. That is [grid-quantization](../grid-quantization/)'s territory, and by this project's principle-versus-scale rule ℏ enters as a unit rather than as something derived here.

- **A prediction this creates, which could fail.** A resonance gives a *peak*, not a step. Real pair production is also peaked — the Breit–Wheeler cross-section rises above threshold and falls again — but broadly, where the measured resonance here is sharp (12–58× over 8%). The ring in the arena is lossless and strongly driven, so its sharpness is a free parameter that the reverse channel should broaden. Whether the width can be made to match is a real test.

- **Equipartition.** A classical nonlinear lattice relaxes toward equal energy per degree of freedom, which here would mean roughly half of all light becoming ring content. The state-density ordering that would prevent it ([Appendix.md](Appendix.md), P6) is a *quantum* counting argument and needs the quantum above. So the two-way-traffic equilibrium cannot be interpreted yet.
- **Nothing protects a particle.** A single real-valued ring has no conserved quantity shielding a mode, so any lifetime measured here is that of an unprotected neutral excitation — closer to a π⁰ than a neutron.
- **The seed has no size.** Without a quantum there is no mapping from amplitude to ½ℏω, so the background's magnitude in simulation units is arbitrary.

## 4. Objectives

1. **Make a particle, then get it back.** Drive the collision to overflow; does a standing wave establish on the ring and outlive the drive, and does the ring later saturate and return its energy to the line? Creation and decay from one rule. *(Done for creation; the return channel is seen but not characterised.)*
2. **Make it move.** Inject into both groups at once — most of the shot going straight, a component turning — and see whether the result travels as one object. Then whether its energy follows ω² = c²k² + ω₀², the relation that makes compact momentum behave as mass. This is the direct test of §3's soliton claim.
3. **Find out how fast it builds.** Whether repeated overflow accumulates, and how that depends on drive strength and ring size. A rate, not a final amount.
4. **Long-range: reach the observed rates.** Sargent's Q⁵ law, lepton universality and the neutron's 880 s lifetime are what [leakage-rate.md](../ma-domain/work/leakage-rate.md) already recovers from phase space. They are **not reachable from this arena** — it has one ring, no lepton or hadron sheets, no neutrino line, and no quanta — and no correspondence is yet stated between a classical overflow rate and "matrix element × phase space". Carried as the eventual target, not as a near-term test.

**Success** is objective 2: a bound object that moves and has inertia. **A failure worth having** is a bound state that cannot be made to move, or one whose energy does not follow the relativistic form.

**Deferred, and listed so the narrowing is visible.** The originating notes also set out the energy ladder and the durability of ordinary matter, neutron decay, simultaneous creation of an electron and a neutrino, and the stability ordering across particle classes. None has an objective here. They need sheets this arena does not have, and in most cases the quantum of §3a.

## 5. First work item

**Simulate, then model.** [AGENTS.md](../AGENTS.md) prefers a derivation where one is available, and allows computation first where the insight to derive is missing. It is missing here: the overflow rule is not yet written down concretely enough to analyse, and the cheapest way to find out what it does is to run it.

Run the arena of §3 and watch three things that are easy to confuse:

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
