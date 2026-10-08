# grid-scattering

**What sets the rate at which energy crosses between GRID's compact sectors — and into space?**

**Type:** Exploratory project (see [../README.md](../README.md))
**Status: active.** The mechanism makes a particle, the crossing is resonant, and the rule conserves energy exactly. The motion obstruction that parked this project briefly is **resolved** (§3b): a coupling keyed to the compact winding gives wound modes a mass and sub-luminal propagation while leaving light exactly massless. Checklist: [work/STATUS.md](work/STATUS.md); all numbers with provenance in [work/measurements.md](work/measurements.md).

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

## 3b. Motion — the obstruction, and what resolved it

For a while this project could not move a particle, and that looked structural. It was not; it was a statement about two rules.

**What failed, and why.** A particle bound by saturation at its core contradicts the ceiling calibration — by "light must pass", an electron's core sits *below* the ceiling. And a **constant** rotation between the register groups gives light a mass gap equal to the rotation angle: at θ = 0.1, light at k = 0 sits at ω = 0.1 instead of 0. Both withdrawn.

**What works.** Make the coupling angle **g·(1 − cos k_c)** — a second difference along the compact direction. It is exactly zero for a field that does not wind, and grows with the winding. A constant rotation is algebraically a *mass* term; one carrying a c-difference is a *derivative* coupling, and that is the whole difference.

Measured two independent ways, simulation agreeing with exact Bloch analysis to ~3 × 10⁻⁴ ([work/measurements.md](work/measurements.md) §M5):

| | |
|---|---|
| light (unwound) | ω = \|k_x\| **exactly**, at every wavenumber — no gap |
| wound rest frequency | 0.2968, 0.7375, 1.3329 for n = 1, 2, 3 — a mass tower |
| dispersion against √(k² + ω₀²) | 0.0%, 0.7%, 0.5%, −0.6% |
| group velocity | **+0.159** — between 0 and 1 |
| energy drift | 3.55 × 10⁻¹⁶ |

So a wound mode has inertia and travels below the speed of light, while light itself is untouched. That is the Kaluza–Klein structure, with the separation posit intact for light and relaxed only in proportion to winding.

**What this costs the posit.** Space and a sheet no longer exchange *nothing* below the ceiling; they exchange in proportion to how much the field twists. Light still passes through exactly untouched, so the original framing survives where it was motivated. Saturation keeps its own job: the bulk crossing that makes and unmakes a particle.

**Two things it owes.** Each winding splits into **two** branches, and the lower one is nearly massless (ω = 0.035 at n = 1) — an unexplained light state of the same shape as the unobserved-mode problem in [3-torus.md](../ma-domain/work/3-torus.md). And the coupling is applied in the c-Fourier basis, where its real-space kernel decays fast but is not finitely supported, so strict node-locality is unproven. A travelling *packet* also has not been demonstrated — three attempts failed on seeding, though the dispersion it must obey is now measured.

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
2. **Make it move.** The linear half is done (§3b): wound modes have mass and travel sub-luminally, light stays massless. What remains is a travelling *packet*, and the same with saturation switched on.
3. **Find out how fast it builds.** Whether repeated overflow accumulates, and how that depends on drive strength and ring size. A rate, not a final amount.
4. **Long-range: reach the observed rates.** Sargent's Q⁵ law, lepton universality and the neutron's 880 s lifetime are what [leakage-rate.md](../ma-domain/work/leakage-rate.md) already recovers from phase space. They are **not reachable from this arena** — it has one ring, no lepton or hadron sheets, no neutrino line, and no quanta — and no correspondence is yet stated between a classical overflow rate and "matrix element × phase space". Carried as the eventual target, not as a near-term test.

**Success** is objective 2 end to end: a bound object that moves, with inertia, under the full rule. The linear sector now delivers the inertia; the nonlinear sector is untested.

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
