# The EM slot — charge as a time *shear*, beside gravity's time *stretch*

**Status:** Open slot, held for later. Not part of the mechanism 3 validation
plan; nothing here has been computed. It records where an electromagnetic
effect would fit in the approach, why the gravity carrier itself cannot supply
one, and how it would be tested — so the option is not lost while the gravity
line is finished.

Grades: **[argument]**, **[from the repo]**, **[expectation]**, **[open]**.

---

## 1. Why the gravity carrier cannot do it [argument]

Two results from the gravity line close the obvious route.

- **The source has no sign.** In [action-and-gamma.md](action-and-gamma.md) §4
  the carrier couples to the wave through squares, so its source is energy. There
  is nothing to be "negative".
- **A signed rate would push the wrong way.** Suppose a charge-like quantity did
  speed up or slow down the local clock rate, with a sign. A rate is a scalar
  quantity, and a scalar mediator makes *like* sources attract. Like charges
  would attract and opposite charges repel — backwards. Neutral matter would
  also fall toward or away from charges, because a rate acts on everything.

The general rule behind this: whether like sources attract or repel is fixed by
the kind of mediator. Scalar and tensor mediators attract likes; a vector
mediator repels them. Electromagnetism needs a vector-like field with a signed
source.

## 2. Where it fits: tilting time into the compact direction [argument]

The loading K of step 3 *stretches* time and space; that is gravity. The other
thing that can be done to time is to *tilt* it into the compact direction: let a
node's clock phase shift by a small amount per lap around the compact loop —
gained going one way round, lost going the other.

| mode | effect of the tilt |
|---|---|
| circulating one way round the compact loop | frequency raised by a fixed amount |
| circulating the other way | lowered by the same amount |
| standing wave (both ways at once) | no net shift — neutral |
| photon (no compact circulation) | none |

This is the *additive, signed, winding-selective* frequency offset of
[sync-carrier-mechanism.md](sync-carrier-mechanism.md) §12. Force is still the
gradient of local frequency (the ray equation), so it is the same kind of
mechanism — a modulation of time — of a different order:

| | gravity | charge |
|---|---|---|
| what is modulated | the clock **rate** | the clock **offset per compact lap** |
| frequency shift | fractional, δω ∝ ω | additive, ± a fixed amount |
| seen by | everything | circulating (wound) modes only |
| parity under reversing the circulation | even | odd |
| metric language | the time–time and space–space entries | the time–compact entry |

In metric language this is Kaluza–Klein: the electric potential *is* the
time–compact entry of the metric. [metric-charge](../../metric-charge/) ch. 5
already has the continuum form (one gauge potential B_μ = h_μw, charge = momentum
along the tube), and its closing chapter lists the time–compact shears σ_tu,
σ_tw as "not engaged anywhere". That is the hook. **[from the repo]**

Three things follow without further input:

- **A signed source.** The same argument as step 3 — whatever multiplies the
  mediator in the action is its source — now gives the *compact momentum
  density*, i.e. circulation, which has a sign.
- **Shielding.** Offsets of opposite sign cancel; rates cannot. A neutral body
  presents no net offset.
- **Agreement with the breathing-source flag.** Step 3 found that the particle
  with a static gravitational source is the one that *travels* around a compact
  cycle ([action-and-gamma.md](action-and-gamma.md) §6); metric-charge's charged
  particle is exactly that ("stands in the ring, travels in the tube"). Standing
  ↔ neutral and travelling ↔ charged come out of both lines independently.

## 3. Why likes would then repel [argument]

A signed source is necessary, not sufficient. The repulsion comes from the
mediator being vector-like: its time part is a *constraint* (Gauss's law) rather
than a free wave, and that reverses the sign of the interaction energy relative
to a scalar.

On the lattice the constraint has a natural origin: the freedom to choose, at
each node and each tick, where that node's compact loop "starts". A mismatch in
that choice between neighbouring nodes is a link phase — GRID's axiom A4, from
which [grid/maxwell.md](../../../grid/maxwell.md) already derives Maxwell's
equations. So the spatial half of this field is already in GRID. What this
reading adds is the interpretation of the electric potential as a lap-offset of
the clock, which places it in the same family as the gravity carrier.

## 4. In circuit terms

Gravity is **reciprocal reactive loading** — shunt capacitance at nodes, series
inductance on edges: it slows everything and cannot tell direction. The charge
coupling is a **non-reciprocal element in the compact loop** — a gyrator or
circulator: lossless, but it advances one circulation sense and retards the
other. Both are lossless and local; they differ in being even or odd under
reversing the circulation. This is the *even → gravity, odd → charge* split of
[aleph-grounding.md](aleph-grounding.md), now attached to concrete lattice
elements.

## 5. How it would be tested (a ladder mirroring the gravity one)

| # | Test | Pass looks like |
|---|---|---|
| E1 | **Uniform offset.** A concrete lossless rule for the odd element; exact spectrum with the offset uniform. | the two circulation senses split by ± a fixed amount; standing modes and the photon untouched; the photon stays gapless; a uniform offset is otherwise unobservable |
| E2 | **Drop test.** A static gradient of the offset on the (x, c) lattice. | the two senses accelerate oppositely; standing modes and photons do not move |
| E3 | **Sign of the force** between two sources, from the link-phase (A4) dynamics. | likes repel, opposites attract, 1/r² |

## 6. Open [open]

- Whether a lattice rule for the odd element exists that is lossless and leaves
  the photon gapless, as the two storage registers turned out to be.
- The relative strength of the two forces: there are two independent stiffnesses
  (the carrier's κ; the link-phase coupling, α) and nothing here relates them.
- Whether the constraint character of the time part — which is what flips the
  sign of the force — emerges from a lattice rule or has to be imposed.

## Grades summary

- **[argument]** §1 (no sign; a signed rate attracts likes); §2 (time shear ⇒
  additive signed offset, signed source, shielding); §3 (vector character ⇒
  likes repel; link phases as the spatial half); §4.
- **[from the repo]** metric-charge's gauge potential and its unengaged
  time–compact shears; A4 → Maxwell; the even/odd split.
- **[open]** Everything in §5–§6. Nothing computed.
