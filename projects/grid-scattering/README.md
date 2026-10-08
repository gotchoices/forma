# grid-scattering

**What sets the rate at which energy crosses between GRID's compact sectors — and into space?**

**Type:** Exploratory project (see [../README.md](../README.md))
**Status: parked on a stated obstruction.** The mechanism makes a particle and the crossing is resonant, both measured with an exactly conserving rule. But **a particle made here cannot move through space**, and that is not a gap — it is measured ([work/measurements.md](work/measurements.md) §M4) and it has a structural cause (§3b). Checklist and revival conditions: [work/STATUS.md](work/STATUS.md).

**Scope.** The point is to test one mechanism: **saturation and overflow as the means by which energy crosses a sheet boundary.** The project is not required to stay harmonious with earlier forma work — where it departs, it says so and the departure is part of what is being tested. If the mechanism works it changes how several things are read; if it fails, it gets parked and the failure is the result. Supporting material is in [Appendix.md](Appendix.md).

---

## 1. The question

Energy demonstrably moves between forma's domains. Two gamma rays make an electron–positron pair; a neutron becomes a proton, an electron and an antineutrino; a charged particle radiates into space. The rates differ by many orders of magnitude and the framework does not say why.

forma has the gap written down twice. [ma-domain leakage-rate.md](../ma-domain/work/leakage-rate.md) files a caveat against its own working assumption — coupling without a shared dimension *"demonstrably exists"*, so *"the leakage graph is richer than the metric-sharing graph"* — and [threshold-dynamics.md](../ma-domain/work/threshold-dynamics.md) sits parked on its §6.2: by what physical mechanism does energy reorganise from a background band into a discrete mode? This project proposes a node-level answer and tests it.

## 2. The junction, and what it is allowed to do

A node where space meets a compact direction carries four registers — two space, two compact. The question is what it may do with them, and the answer is less constrained than an earlier draft of this project claimed. Working: [work/junction-geometry.md](work/junction-geometry.md).

The only genuine per-node constraint is **unitarity** — energy in equals energy out. Momentum need not balance at a node, because the lattice is fixed and can absorb it; that is what crystal momentum means. (An earlier version of this project imposed per-node momentum conservation, using a measure that was itself wrong — a wave's momentum goes with energy flux, as amplitude *squared*, not as amplitude. Both errors are retracted in the working file.)

Requiring only unitarity leaves a **continuous family** of rules, with cross-coupling between the two groups tunable smoothly from zero. So the project's posit is one end of a dial rather than a rival to the usual scatter:

> **Below the ceiling, space and a sheet exchange little or nothing. The ideal node exchanges exactly nothing; a physical one may leak slightly. Above the ceiling, overflow carries energy across in bulk.**

The partition is **space against a sheet**, not dimension against dimension. Within space the ordinary scatter applies unchanged, so the spatial sector — and Maxwell with it — is untouched. Compact directions simply take little part until the dynamics goes nonlinear.

What is forced and what is posited should be kept apart. Being discrete and finite forces a **bound**: a register holds only so much. It does not force the excess to **redirect** into the other group rather than being clipped away or wrapped. That redirection is this project's posit and the thing under test.

## 3. What crosses, and what it makes

**Scope of the ceiling (posit).** Each node has two degrees of freedom: it can saturate in its space group, in its sheet group, or in both. The test is on each group's own sum — not per edge, which grid-matter ruled out, and not on the node as a whole. A whole-node test is the live alternative, and it would let a ring wave and a passing space wave push a node over together; that is a different model and is not what is implemented.

**What the overflow does.** The excess rotates out of the saturating group into the other, at the node where it happens, and runs both ways around the ring to meet itself on the far side. It does not carry x-momentum across; see §3b for why that could not be patched.

**Energy bookkeeping.** The crossing is a rotation between the register groups, which is exactly energy-conserving by construction and accounts for whatever the ring already holds. Audited drift is ~10⁻¹⁶. An earlier rule moved *amplitude* instead, which destroyed energy on every overflow — most of it off resonance — and corrupted a whole round of measurements.

**What forms.** Two counter-propagating waves on the ring. Equal energy both ways around a loop is a standing wave, and a standing wave captive on a loop is what [metric-mass](../metric-mass/) commits to as a particle at rest — the ±n superposition, one particle rather than two.

**But it cannot move.** See §3b. Two attempts to supply motion have been withdrawn: a soliton bound by saturation at its core (which contradicts this project's own ceiling calibration), and a weak always-on rotation between the groups (which gives the photon a mass gap equal to the coupling angle). The second is measured, not argued: at θ = 0.1 light at k = 0 sits at ω = 0.1 instead of 0.

**Two conditions, not one.** Saturation is only the first: enough amplitude for energy to leak into a sheet at all. It does not make a particle. The second is **frequency** — the drive must resonate with the ring. Measured, with the conserving rule and over three seeds: the winding fraction at the resonant circumference is **0.045 against 0.006–0.014** around it, so roughly **5×**, with a 3× spread between seeds ([work/measurements.md](work/measurements.md) §M3).

If that holds up it would mean each sheet carries its own threshold, set by its own circumference — and since the ring size fixes both the particle's mass and the wavelength that fits it, the threshold would land at the particle's own mass scale automatically. It would also say why an intense laser makes no pairs: it saturates easily and energy crosses, but an optical frequency is nowhere near the electron ring's resonance.

**This is a lead, not a result.** A 5× selection with that much seed scatter is not strong enough to gate a threshold, and the amplitude-versus-frequency problem of §3a is therefore still open. Earlier figures of 12–58× and 50–100× are **withdrawn** — they came from a lossy rule whose losses were largest off resonance.

**The ceiling is not a free parameter.** Any ordinary travelling photon is by definition below it — otherwise light would saturate as it propagates and the vacuum would not be transparent. The ceiling is calibrated by an observable: *light must pass*. Three things follow with no further assumption. A lone photon never saturates, which is why pair production needs **two** photons, or a photon plus a nucleus's field standing in for the second. A collision is special precisely because two amplitudes sum at one node. And the **Schwinger limit becomes a prediction** rather than an input — it is where a single field, with no collision, finally reaches the ceiling alone.

### The arena, cut down

A **cylinder**: one extended direction x and one compact direction c as a product lattice, so every node sits on both the x line and the c ring through it, and rings at neighbouring x are joined along x. That last point is what lets anything made on a ring afterwards move.

A photon is uniform around c, so if every c-position saturates together the injection is uniform and the winding is zero. The rule therefore lets only the single largest-|T| position at each x overflow, with the tie broken by the background. The symmetry is broken by the **state**, never by the rule — which keeps winding conserved, and winding is charge once the field is complex.

*(An earlier arena hung a ring off each x position at a fixed point. That was wrong twice: it gave every ring a privileged attachment, breaking the translation symmetry along c whose conserved quantity is the winding; and its ring nodes had no x-edges, so nothing made there could ever travel.)*

### What has been measured

On the cylinder, with an **exactly energy-conserving** overflow rule (a rotation between the register groups; drift 0.0 to machine precision):

- Nothing crosses with no drive, and nothing crosses below the ceiling. ✓
- Above the ceiling energy crosses, and with one-point overflow **99.95%** of it circulates rather than sitting in the non-circulating mode. ✓
- **Resonance survives, but weakly.** At the predicted circumference the winding fraction is a clean local maximum — 0.370 at nc = λ against 0.252 and 0.250 either side — about **1.5×**, against a background that itself wanders between 0.25 and 0.31. It needs averaging over seeds before it can be called settled.

**Earlier figures of 50–100× are withdrawn.** They were measured with a lossy rule that destroyed more energy than the system held, and destroyed most of it *off* resonance — so the ratio was reading differential dissipation, not selection. An external audit caught it; the project's own Appendix G rule ("no transfer claim from a ratio unless measured against an energy-conserving control") should have caught it first. Details and the full retraction: [work/first-run.md](work/first-run.md).

## 3b. The obstruction the project is parked on

**A particle made in this arena cannot travel through space.** Measured, not inferred ([work/measurements.md](work/measurements.md) §M4): a ring excitation at rest radiates symmetrically and decays in place, its x-centroid moving 0.0000 at every amplitude tried; and one launched *with* x-momentum shears apart — the x content travels 41 nodes while the compact content stays at 0.

The cause is structural, and it is the project's own posit. Motion of a compact-sector mode needs space and the compact direction joined in **one wave operator** — the shared Laplacian that gives ω² = c²k² + ω₀² and makes compact momentum behave as inertia. Strict separation removes exactly that. The two are mutually exclusive, and no weak-coupling compromise bridges them: a rotation between register groups is algebraically a *mass* term, not a derivative coupling, so making it small gives a small photon mass rather than approaching the right dispersion.

**What is missing is a binding mechanism, not a transfer mechanism.** Saturation moves energy across a boundary; it does not hold a lump together. [grid-matter](../grid-matter/work/focusing-from-phase.md) has the other half — on the same (x, compact-c) lattice it demonstrates a **stable, mobile breather** (speed 0.15, translating coherently, surviving the Peierls–Nabarro barrier). Its binding comes from the field *value* being a compact phase, so the potential m²(1 − cos φ) is focusing. That is a property of the field, not of a ceiling, and this arena does not have it: its field is a real amplitude.

So the revival condition is specific rather than vague: **a binding nonlinearity on the field value, combined with saturation as the transfer channel.** Whether that belongs here or in grid-matter is an open question — grid-matter already owns the binding half.

## 3a. What this arena cannot settle

Named here rather than discovered later.

- **The one bridge still owed: amplitude against frequency per quantum.** The ceiling has to sit *below* two colliding 511 keV gammas and *above* a bright optical beam — a tight constraint, and the thing that separates them cannot be photon count, since the beam has vastly more. It has to be frequency. The bridge is that a single quantum ℏω localised in about one wavelength carries energy density ∝ ω⁴, hence amplitude ∝ ω²: a gamma then has ~10¹¹ times an optical photon's amplitude *per quantum*, which puts two of them in the same range as a bright beam of ~10²⁰ optical photons. Self-consistent, and it is what makes the calibration above possible — but it imports ℏ into a classical arena. That is [grid-quantization](../grid-quantization/)'s territory, and by this project's principle-versus-scale rule ℏ enters as a unit rather than as something derived here.

- **Resonance width, unmeasured.** A resonance gives a *peak*, not a step. Real pair production is peaked too — Breit–Wheeler rises above threshold and falls — but broadly. The arena's width has never been measured, only its height (~5×, §M3), so there is nothing yet to compare.
- **Carried over and still unanswered:** at 2× and 3× the threshold frequency the ring takes an n = 2 or 3 *rest* mode rather than a moving pair; two threshold photons make one ±n object where Bethe–Heitler needs a single photon of 2mₑc²; the resonance condition uses lab-frame frequencies rather than the invariant √(ω₁ω₂); and the Schwinger "prediction" is fixed by dimensional analysis up to a convention factor of about 16, so it is weaker than the index claimed.

- **Equipartition.** A classical nonlinear lattice relaxes toward equal energy per degree of freedom, which here would mean roughly half of all light becoming ring content. The state-density ordering that would prevent it ([Appendix.md](Appendix.md), P6) is a *quantum* counting argument and needs the quantum above. So the two-way-traffic equilibrium cannot be interpreted yet.
- **Nothing protects a particle.** A single real-valued ring has no conserved quantity shielding a mode, so any lifetime measured here is that of an unprotected neutral excitation — closer to a π⁰ than a neutron.
- **The seed has no size.** Without a quantum there is no mapping from amplitude to ½ℏω, so the background's magnitude in simulation units is arbitrary.

## 4. Objectives

1. **Make a particle, then get it back.** Drive the collision to overflow; does a standing wave establish on the ring and outlive the drive, and does the ring later saturate and return its energy to the line? Creation and decay from one rule. *(Done for creation; the return channel is seen but not characterised.)*
2. **Make it move.** ~~Attempted and failed~~ — see §3b. This is the obstruction the project is parked on, and it is where any revival starts.
3. **Find out how fast it builds.** Whether repeated overflow accumulates, and how that depends on drive strength and ring size. A rate, not a final amount.
4. **Long-range: reach the observed rates.** Sargent's Q⁵ law, lepton universality and the neutron's 880 s lifetime are what [leakage-rate.md](../ma-domain/work/leakage-rate.md) already recovers from phase space. They are **not reachable from this arena** — it has one ring, no lepton or hadron sheets, no neutrino line, and no quanta — and no correspondence is yet stated between a classical overflow rate and "matrix element × phase space". Carried as the eventual target, not as a near-term test.

**The outcome so far is the second of the two anticipated here:** a bound state that cannot be made to move. That was pre-registered as a failure worth having, and it is the one that occurred.

**Deferred, and listed so the narrowing is visible.** The originating notes also set out the energy ladder and the durability of ordinary matter, neutron decay, simultaneous creation of an electron and a neutrino, and the stability ordering across particle classes. None has an objective here. They need sheets this arena does not have, and in most cases the quantum of §3a.

## 5. Where the work stands

The arena is built, the rule conserves exactly, and the measurements have provenance in [work/measurements.md](work/measurements.md). What was established: nothing crosses below the ceiling or without a background; above it energy crosses and circulates; the crossing is resonant at the predicted circumference at roughly 5×; and the reverse channel runs unprompted. What was not: a particle that moves (§3b).

## 6. Revival conditions

The project is parked rather than closed. It would be worth restarting on any of these:

1. **A binding nonlinearity on the field value.** The specific missing piece (§3b). grid-matter's compact-phase potential already produces a mobile particle on this lattice; combining that with saturation as the transfer channel is the obvious experiment, and it may belong in grid-matter rather than here.
2. **A coupling that leaves k = 0 alone.** Motion needs a derivative coupling whose strength grows with compact wavenumber, so that light stays massless while a wound mode acquires inertia. Whether such a rule exists, and whether it can still be called weak, is a well-posed question nobody has answered.
3. **A reason the ceiling is not global.** The obstruction depends on a particle's core sitting below the ceiling, which follows from calibrating the ceiling so ordinary light passes. A per-sheet or per-group ceiling would change that, and would need its own justification.

## 7. Relation to other projects

**Not a revival of grid-saturation.** grid-matter was renamed from `grid-saturation` because its entry hypothesis — that the saturation bound *binds a particle* — was refuted. This project concerns **transfer**, not binding, and grid-matter's own work file keeps that distinction open: *"This is 'not yet,' not 'refuted.'"*

- [ma-domain](../ma-domain/) — the principal consumer: [leakage-rate.md](../ma-domain/work/leakage-rate.md) names the missing law, [threshold-dynamics.md §6.2](../ma-domain/work/threshold-dynamics.md) the missing mechanism.
- [grid-matter](../grid-matter/) — the saturation history, the (x, c) cylinder testbed, and **the binding half this project lacks**: its compact-phase potential produces a stable, mobile breather on this lattice. Its M1 run verified the *pooled* scatter, not the rule used here.
- [metric-mass](../metric-mass/) — the target object: a particle is a standing wave around the compact dimension, the ±n superposition, one particle rather than two.
- [grid-duality](../grid-duality/) — closed; the scatter, the candidate-model format and the test bench any new rule must pass.
- [grid-primitive](../grid-primitive/), [grid-quantization](../grid-quantization/) — the edge/node primitive, and the home for any zero-point question that survives.
