# grid-scattering

**What sets the rate at which energy crosses between GRID's compact sectors — and into space?**

**Type:** Exploratory project (see [../README.md](../README.md))
**Status:** Framing. No chapters, no code in the project yet. The first work item is a derivation, not a simulation.

Supporting material — glossary, the originating premises, obstructions, and the record of what has been discarded and why — is in [Appendix.md](Appendix.md). This file stays short on purpose.

---

## 1. The question

Energy demonstrably moves between forma's domains. Two gamma rays make an electron–positron pair. A neutron becomes a proton, an electron and an antineutrino. A charged particle radiates into space. The rates differ by many orders of magnitude, and the framework does not say why.

forma has the gap written down. [ma-domain leakage-rate.md](../ma-domain/work/leakage-rate.md) carries a foundational caveat against its own working assumption:

> *"That assumption is unverified and probably too strong… Coupling without a shared dimension demonstrably exists — a charged closure mode radiates energy into macroscopic space S at rate ~α with no shared dimension… the leakage graph is richer than the metric-sharing graph."*

And [threshold-dynamics.md](../ma-domain/work/threshold-dynamics.md) is parked behind six questions, of which §6.2 — *by what physical mechanism does energy reorganise from a background band into a discrete mode?* — is unanswered.

This project proposes a node-level answer and tests it.

## 2. Why the linear rule cannot supply one

GRID's scatter is linear and identical at every node. On a compact dimension that is periodic, such a rule **conserves the winding number exactly** — the integer counting how many wavelengths fit around the ring, which in Kaluza–Klein terms is the charge label. Energy travelling along an extended direction can never, under the linear rule alone, acquire winding around a compact one.
<!--EC Should define "winding number" briefly so the previous paragraph is not so confusing.  It is only a charge label if we are talking about a compound winding on a 2D sheet.  If the winding is 1D, we are only talking about mass (metric-mass). -->

That is a feature rather than a defect: it is charge conservation, and [leakage-rate.md §3.1](../ma-domain/work/leakage-rate.md) already derives it as a geometric selection rule. But it means **the linear substrate cannot make a particle.** Whatever does must be nonlinear.

<!--EC It seems we have lost the original terminology of the sheet-aware node.  Is that on purpose?  How/where did we slip into "winding conservation" and is it the same thing?  We are using conservation and winding numbers as an excuse for why energy doesn't normally leak into an orthogonal dimension.  But it feels like we have lost the intuitive sense of the energy "not turning 90 degrees" in favor of appealing to a "rule" (conservation) as opposed to an intuitive principle (something traveling in a direction, continues to travel in that direction).  Might be worth re-reading thoughts.md to see if we have lost any critical essence from the original thought piece. -->

## 3. The mechanism under test
<!--EC Might be worth stating that we are simplifying a known-complex landscape into just x,c so we can study the interaction between two sheets/spaces. -->
- **Arena.** A cylinder: an extended direction x, and a compact ring c at every point along x.
- **Normally.** The linear scatter runs. Winding around c is conserved; x and c do not exchange energy.
- **At saturation.** A node whose summed input exceeds a threshold clips, and the removed amount is ejected around the ring — half each way. The x–c connection exists *only* during the overflow and *only* at the node where it happens. Several nodes may overflow at once.
- **Result.** Two counter-propagating waves on the ring. If their wavelength fits the circumference they persist as a standing wave — the captive wave [metric-mass](../metric-mass/) identifies as a particle at rest. If it does not fit, the energy returns to x or disperses.

In standard terms this is a **parametric process**: a driven mode decaying into a pair of counter-propagating partners with opposite winding, +n and −n. The identification is worth making because it brings known machinery — the quantity to compute is a growth rate, and the conditions for one are well understood.

### What has to hold

- **The rule must be identical at every point around the ring.** If the *rule* singles out a position, winding stops being conserved — and since winding is charge, the mechanism would violate charge conservation. Only the *state* may break the symmetry.
<!--EC How so?  What is the support for the assertion that winding stops being conserved?  And winding isn't always charge, winding is promotion (reference?).  Seems like we are relying on a "rule" (winding conservation) rather than a symmetry argument which I think is more fundamental and intuitive. -->
- **The two waves must balance.** Total winding starts at zero and is conserved, so what gets created is +n and −n together.
- **The books must balance in amplitudes, not energy.** GRID nodes carry amplitudes; computing an energy and taking its square root is foreign to the substrate. Clipping implemented as a *rotation* between the x and c registers — the angle chosen to bring x down to the clip level — gives clip-and-dump behaviour, needs only amplitudes, and conserves energy exactly by construction.
<!--EC Is there any argument that if amplitude is equal to the "information in motion" on the GRID, that energy could be related to a function of:
  - The amplitude; and
  - The frequency
  (as opposed to simply amplitude squared)?
  For example, does it take more energy to oscillate a 1v p-p signal at 1khz than at 100hz?
   -->
- **A classical field needs a seed, and the seed is not a free parameter.** Classically, a perfectly uniform state cannot spontaneously produce the pair. Quantum mechanically it can, and the semiclassical stand-in is a zero-point background whose amplitude is fixed at ½ℏω per mode.
<!--EC Again, this seems unsubstantiated.  What is a seed and why is it needed? -->

## 4. Objectives

In priority order. The first is the project's reason to exist; the others are what would make it count.

1. **Derive the growth rate.** Linearise about the driven state, find which (+n, −n) pairs are unstable, and obtain the rate as a function of drive amplitude, nonlinear strength and geometry.
<!--EC Growth rate of what?  I think our objective is to simulate saturation and overflow into orthogonal dimensions and see if we can generate a standing wave in c, correct? -->
2. **Check it against rates forma already reproduces.** [leakage-rate.md §4](../ma-domain/work/leakage-rate.md) recovers Sargent's rule (weak decay rate ∝ Q⁵) and lepton universality to ~0.2% from phase space alone. Any mechanism proposed here must reproduce that scaling, or show how it combines with phase space to give it. The neutron's 880 s lifetime is the anchor.
3. **Reach the coupling hierarchy.** ~α on the electromagnetic channel and the observed smallness of the weak one, from geometry rather than fit.
4. **Say what the mechanism forbids.** A rate law that permits everything explains nothing.
<!--EC I don't really understand the whole prior section.  It needs to be more clear. -->

**Success** is objective 1 plus a defensible answer on 2. **A failure worth having** is a growth rate that demonstrably cannot span the observed hierarchy, reported as such.

## 5. First work item
<!--EC Again, I don't understand "growth rate".  If we have energy of a certain frequency in x and it spills over into c, it seems like it should begin to oscillate after the first cycle around c.  Are you suggesting some standard physics analysis of this or can we do it computationally first and then develop a mathematical model to explain what we observed? -->
**A derivation, not a simulation.** Linearise the saturating-node rule about a uniform driven state on the (x, c) cylinder and solve for the growth rate of the ±n pair. [AGENTS.md](../AGENTS.md) prefers derivation where it is available, and here it is — the calculation is standard parametric-instability analysis applied to this rule.

Simulation follows as a check, on the geometry of §3: two pulses meeting on the line, overflow into the ring, measuring which ring modes populate and how quickly. Two controls — the same run with clipping disabled, and a run with the seed removed.

What *not* to measure: a plateau height, or a ratio against a flat control. A saturated instability plateaus at a level set by the nonlinearity regardless of the seed, and a ratio against a flat baseline grows with run length. Neither is a rate.

## 6. Status and next steps

1. Write the §5 derivation.
2. **Restate the motivating problem in ma-domain's current architecture.** The unobserved-mode-tower problem this project originally set out from comes from [3-torus.md](../ma-domain/work/3-torus.md), which describes itself as historical and predates the dim-pool reading now in use. Until it is restated, it is not clear the project is solving a problem ma-domain still has.
3. **Settle whether the substrate stays real-valued.** A real field cannot carry the *sign* of a winding, so it cannot distinguish +n from −n and cannot speak to charge at all. [grid-primitive](../grid-primitive/) already carries two real degrees of freedom per edge (e, φ); adopting that changes the primitive and would need checking against [grid-duality's test bench](../grid-duality/03-test-bench.md).
4. Then the simulation — and only then any claim about rates.
<!--EC I'm not sure windings have signs in metric-mass (1D compact dimensions). Seems like the direction is indeterminate (both directions at once, 2 solutions) -->

## 7. Relation to other projects

**Not a revival of grid-saturation.** grid-matter was renamed from `grid-saturation` because its entry hypothesis — that the saturation bound *binds a particle* — was refuted. This project concerns **transfer**, not binding, and grid-matter's own work file keeps that distinction open: *"This is 'not yet,' not 'refuted.'"*

- [ma-domain](../ma-domain/) — the principal consumer. [leakage-rate.md](../ma-domain/work/leakage-rate.md) names the missing law; [threshold-dynamics.md §6.2](../ma-domain/work/threshold-dynamics.md) names the missing mechanism.
- [grid-matter](../grid-matter/) — owns the saturation history and the (x, c) cylinder testbed the simulation would use.
- [metric-mass](../metric-mass/) — supplies the target object: a particle is a standing wave around the compact dimension, the ±n superposition, and is **one** particle rather than two.
- [grid-duality](../grid-duality/) — closed; supplies the uniform scatter, the candidate-model format and the test bench.
- [grid-primitive](../grid-primitive/) — the edge/node primitive, and the two-real-DOF option in step 3.
- [grid-quantization](../grid-quantization/) — would own any zero-point-spectrum question, if one survives (see [Appendix.md](Appendix.md)).
