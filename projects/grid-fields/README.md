# grid-fields — Does a particle occupy every point, and is that what a field is?

**Status:** Framed. No chapters yet; the posit and its open
questions are stated and the first discriminating test is
specified.

## The question

Textbook physics carries two separate objects for every particle:

- the **particle** itself, more or less localized, and
- the **field** it sources — a Coulomb field, a gravitational
  field — reaching outward to infinity.

This project explores a posit that merges them:

> A massive particle does not occupy a point. It occupies **every**
> point, with a diminishing amplitude outward, while still
> possessing a definite **locus** — a centre where most of its
> energy sits. What is conventionally called the particle's *field*
> is simply the outer part of the particle itself.

The founding statement of the posit, in the author's own words, is
preserved verbatim at
[work/founding-posit.md](work/founding-posit.md). This README
restates it, lays out the variations it has developed, and records
which parts have support, which have objections, and which are
untested.

## Why the posit is not obviously wrong

Three things already favour it, and they are worth stating because
they are easy to lose.

**The wavefunction in forma is stuff, not knowledge.** In textbook
quantum mechanics |ψ|² is a probability density, so a "spread
wavefunction" means spread *information* about where a point
particle is. Forma takes a different position:
[grid-matter's Born-rule work](../grid-matter/work/born-detection-theorem.md)
establishes that |ψ|² is an **energy density** — an identity, not
an interpretation. If the wavefunction is literally where the
energy is, then a spread wavefunction *is* a spread physical
object. The posit's central requirement is therefore already a
framework commitment rather than a new assumption.

**The lattice already produces half of it.** Measurements in
[grid-scattering](../grid-scattering/) show that the pooled
impedance scatter spreads a massive mode out along the extended
direction x while its circulation around the compact direction
stays coherent. "Spreads in x, keeps its internal character" is
measured behaviour, not speculation.

**The observer is made of the same material.** Forma holds that
matter is light in a more complicated configuration. In a two-slit
experiment the screen, the barrier and the slits are all light, so
the experiment is light interacting with light. There is no
external, objective observer standing outside the physics — which
is the right starting point for any account of measurement.

## What is not yet established

**The locus.** The lattice spreads a massive mode, but the measured
profiles melted into a structureless spread; they did not develop a
persistent core with tails. And there is a general reason to expect
that: on a **linear** dispersive medium, a free wavepacket's
long-time behaviour is universal — stationary phase gives a peak
amplitude decaying as t^(−1/2) in one dimension with the width
growing linearly, and **no persistent core survives**. A locus
requires either a nonlinearity or a trapping potential. The sinc
function was raised as a candidate shape and does not escape this;
sinc is a linear-superposition profile and disperses like any
other.

So the posit, as written, needs the nonlinear sector. That puts it
on the same hook as
[grid-scattering](../grid-scattering/)'s saturation/overflow work,
rather than offering a route around it.

### The discriminating test

One cheap measurement separates the posit from ordinary dispersion.
Run the cylinder and plot the **actual x-profile on a log scale**
at long times — not an rms width, which repeatedly misread two
separated pulses as one broad distribution during the
grid-scattering work. Then ask:

| Observation | Interpretation |
|---|---|
| peak amplitude falls as t^(−1/2), featureless tails | ordinary spreading; no locus; posit needs the nonlinear sector to work at all |
| peak amplitude settles to a constant, tails show structure | persistent core plus tails; the posit, measured |

This is the first thing to run.

## The variations

The posit has developed several distinct branches. They are
separable, and some are in tension with each other.

### V1 — Fields as the outer part of the particle

The core claim. Status: **the strongest branch.** It needs the
locus (above) to be more than a restatement of dispersion.

One quantitative caution to design around: a wavefunction and a
Coulomb field are not obviously the same object. Confining an
electron tightly narrows its wavefunction while leaving its
Coulomb field reaching to infinity as before, and the two have
different falloffs — a bound wavefunction decays exponentially, a
Coulomb energy density as 1/r⁴. A steelman exists: in quantum field
theory the physical electron is "dressed" by a cloud of soft
photons which genuinely does carry a 1/r⁴ energy tail, so a real
particle *is* extended. But that cloud and the electron's own
wavefunction have different origins, and merging them is the work.

### V2 — Light rides on the fields of other particles

The proposal that GRID carries the spreading fields, the fields
carry the light, and therefore every particle has a private
transmission medium — its own frame of reference, which would
dissolve the preferred-frame problem.

Status: **one objection withdrawn, one standing.**

*Withdrawn:* that light's propagation would then depend on local
matter density, contradicted by light crossing intergalactic voids
unchanged. Under the posit, local dense matter adds a *near-miss*
correction on top of a baseline carried by the near-uniform sum of
all matter fields — and that correction is exactly refractive
index. Refraction becomes a prediction of the posit rather than a
counterexample.

*Standing:* the sum of all matter fields is isotropic in exactly
**one** frame, and that frame is observable — the CMB dipole gives
the solar system's motion against it as roughly 370 km/s. So the
branch replaces GRID's lattice frame with a cosmic matter frame,
which is worse, because the lattice frame is unobservable while the
cosmic one is in the data.

A second standing objection: the privacy spares a contradiction
*during* flight but not the consistency requirement *after*. Two
detectors side by side, moving differently, can compare notes about
a single objective arrival event, so a transformation law between
their accounts is still owed — and that law is the entire content
of relativity.

**What V2 was reaching for is available without it.** A moving
observer measures c not because light adapts to them but because
their ruler is short by γ and their clock slow by γ, which exactly
cancels a genuine γ² delay. That mechanism is derived in
[primers/relativity-on-a-lattice.md](../../primers/relativity-on-a-lattice.md)
and tested in [grid/sim-lorentz](../../grid/sim-lorentz/). It needs
no private media and attracts none of the objections above.

### V3 — Collapse as interference into a new state

Refined during development from "cancel" to "interfere": when a
spread photon and a spread electron come into alignment, the two
wavefunctions interfere, the energy concentrates into the signature
of the resulting state (an excited electron), and the original
photon wavefunction is swallowed into that result and can no longer
react with any other observer. The particle *does* have a location;
what collapses is the outer part.

Status: **the mechanism is close to standard absorption; the energy
accounting is the open problem.**

In favour: interaction strength really is governed by the overlap
of the two wavefunctions, so interactions genuinely are
concentrated where both are large. And absorption into a bound
state really does depopulate the photon mode. Both standard.

Two objections:

*Different fields do not superpose.* A photon and an electron
carry different quantum numbers and cannot be added; they interact
(scattering) rather than cancel. The forma steelman is that at the
GRID level everything is light differing only by winding, so they
*could* superpose — but then they could superpose generally, and
electrons would annihilate against passing photons, which they do
not. A reason the alignment only fires at detection is owed, and
that is the original mystery restated.

*The energy accounting.* Because |ψ|² is energy here, the photon's
energy was genuinely spread across a region at least as wide as the
slit separation — in astronomy, light-years. Afterwards it is
inside one atom, in femtoseconds. That is not mildly superluminal.

### V4 — The fork that has to be chosen

V3's energy problem has two candidate fixes and **they are
mutually exclusive.** This is the most consequential open item in
the project.

| | Position | Cost |
|---|---|---|
| **A** | Energy is genuinely spread, as |ψ|² = energy density requires | Absorption must re-gather real energy from a large volume to a point, faster than light |
| **B** | Wheeler–Feynman / transactional: nothing happens in between; emission and absorption are a direct handshake | No re-gathering problem, because the energy never was out there — but then |ψ|² is *not* energy density for a photon in flight, and [the Born-rule derivation](../grid-matter/work/born-detection-theorem.md), which runs through energy density = |ψ|², must be rebuilt from something else |

Both are live. Neither is free. Choosing is a project in itself.

### V5 — Three interaction types

The posit organizes interactions into three kinds, each with its
own status:

- **photon–photon.** Superposition means photons mostly ignore each
  other, with rare exceptions such as pair production. A lattice
  nonlinearity (saturation) is a candidate mechanism, developed in
  [grid-scattering](../grid-scattering/).
- **photon–matter.** V3 above: two-slit, hidden variables,
  collapse.
- **matter–matter.** Gravity and charge, below.

### V6 — Forces from overlapping tails

The sketch: two massive particles whose spread waves overlap
interfere additively in the space between them and subtractively
elsewhere, so each locus becomes slightly more concentrated toward
the other and the two migrate together. Gravity. Charged particles
have extra compact degrees of freedom and so are polarized, giving
attraction or repulsion by orientation.

Status: **promising instinct, with one hard constraint to build
around.**

The constraint: **the sign of a force is set by the spin of the
exchanged quantum.**

| exchanged quantum | like charges |
|---|---|
| spin 0 (scalar) | attract |
| spin 1 (vector) | **repel** |
| spin 2 (tensor) | attract |

A generic "waves interfere constructively between them" picture
produces the scalar case — always attractive — so it can model
gravity but **cannot** produce like-repels-like at any tuning. A
genuine vector index is required. Encouragingly, the polarization
idea points straight at this: polarization *is* a vector index. The
thing to check is whether the compact structure yields spin 1 for
the charge sector and spin 2 for the mass sector, since that is
what fixes the signs — not the interference pattern.

### V7 — A compact extended direction

The question of whether x, like the compact direction, might also
be periodic — and whether that makes a matter wave finite.

Status: **two gains, two costs.**

*Gains.* Finiteness, trivially: a finite domain means a wave spread
over all of x has finite total energy at finite density, which is
the same trick the compact direction already performs. Momentum
also quantizes. And more interestingly, **revivals** — on a finite
periodic domain a dispersing packet spreads, wraps, and (for a
commensurate spectrum) reassembles. This is real, observed physics
in Rydberg atoms and cold-atom lattices, and it is a genuine route
to "spreads *and* has a locus" **without** nonlinearity: the
particle would be a breathing object, delocalized most of the time
and periodically re-forming.

*Costs.* Revival time scales as L². For an electron with L = 1 m it
is hours; at the cosmological scale forced by CMB matched-circle
searches (which bound any compactification above the observable
horizon) it exceeds the age of the universe by something like 10¹⁹.
So revivals buy normalizability, not coherence. And compactifying a
*spatial* direction breaks **global** Lorentz invariance: there is
a preferred frame, the one in which the loop closes
simultaneously, and in any other frame going once around returns to
a different time.

### V8 — Compact circulation as the mechanical origin of time

The idea that going once around the compact direction *is* a unit
of time, possibly with a slight shear so that each circuit arrives
at an offset in t — giving a mechanical description of time rather
than an intuitive one.

Status: **the good version is already the structure; the shear
version has costs.**

*Already true.* [A3](../../grid/foundations.md) gives each cell a
compact phase, and a winding excitation on a compact sheet carries
a conserved winding number. The circulation rate *is* the mass via
E = ℏω. So one circuit already equals one tick of that particle's
own clock — its proper time. GRID therefore already carries two
notions of time: the **tick** (A2's single causal dimension,
shared and absolute) and the **winding phase** (each particle's own
clock, running at 1/γ relative to the tick). The ratio is time
dilation, derived in
[primers/relativity-on-a-lattice.md](../../primers/relativity-on-a-lattice.md)
§9.

*The shear version* — identifying (x, c, t) ~ (x, c + L_c, t + Δ) —
is a well-defined twisted compactification with two costs. It
breaks A2's spatial isotropy or permits backward causal flow, since
circulating the other way around a direction with "no preferred
direction" would advance t by −Δ. And it installs a detectable
preferred frame: boosting the twist along x gives it an x-shift it
did not have, so the twist is "pure" in only one frame.

## Phases

**Phase 1 — Does the lattice produce a locus?** Run the
discriminating test above. Log-scale x-profiles at long times,
peak-amplitude scaling, tail structure. Linear sector first, then
with the saturation nonlinearity. This is the gate: V1 and most of
what follows depend on it.

**Phase 2 — Choose the V4 fork.** Work out what each position
costs in full. For A, whether any local mechanism can re-gather
energy, or whether the framework must accept non-local energy
transport and say so plainly. For B, what replaces energy
density = |ψ|² as the basis of the Born rule.

**Phase 3 — Interaction overlap, quantitatively.** Whether the
overlap of two spread waves reproduces known interaction rates, and
whether photon–matter alignment can be made selective enough to
fire only at detection.

**Later (pool, unordered).** Spin structure of the compact sector
and whether it delivers spin 1 for charge and spin 2 for mass (V6).
Revival timescales for a compact x under forma's own scale
assumptions (V7). Relation to decoherence theory, which is the
incumbent account of apparent collapse and the nearest existing
competitor to V3.

## What success looks like

Not a number. A clear answer to: **is a particle in forma one
object that reaches everywhere, or a localized object plus a
separate field?** Either answer is a result. The posit is worth
developing because it is the first framing in the project that
makes "field" a derived notion rather than a primitive.

A secondary success would be making the V4 fork explicit enough
that every future collapse proposal in forma has to declare which
side it is on.

## Relations

- [work/founding-posit.md](work/founding-posit.md) — the posit as originally written, verbatim
- [grid-scattering/](../grid-scattering/) — whether the scatter spreads or keeps a lump; the saturation nonlinearity
- [grid-matter/](../grid-matter/) — the Born-rule derivation, the sine-Gordon reduction, the wave-until-interaction thesis
- [primers/relativity-on-a-lattice.md](../../primers/relativity-on-a-lattice.md) — why V2 is not needed for the frame problem
- [grid/sim-lorentz/](../../grid/sim-lorentz/) — the measurements that replace V2's motivation
- [grid/foundations.md](../../grid/foundations.md) — A2 (tick, causal dimension), A3 (compact phase, winding)
- [grid/fields.md](../../grid/fields.md) — the existing GRID-level treatment of fields, which this project proposes to re-found
