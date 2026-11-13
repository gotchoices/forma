# Q145. Is time the compact circulation, and can the compact direction carry a shear in t?

**Status:** Open — split verdict. The *untwisted* reading is
already GRID's structure and needs no new posit. The *twisted*
(sheared) version is a well-defined construction with two costs,
neither yet paid.
**Related:**
  [Q138](Q138-time-as-peer-dimension-or-bookkeeping-balance.md) (time as peer dimension vs. bookkeeping balance),
  [Q76](Q76-origin-of-metric-signature.md) (origin of metric signature),
  [Q144](Q144-euclidean-vs-lorentzian-orthogonality.md) (the compact direction is spatial — the evidence),
  [Q142](Q142-absolute-lattice-frame-vs-relativity.md) (what a detectable preferred frame would cost),
  [Q117](Q117-relativistic-effects-from-velocity-partition.md) (circulation rate as the particle's clock),
  [`grid/foundations.md`](../grid/foundations.md) (A2 — the tick; A3 — compact phase, winding),
  [`projects/grid-fields/`](../projects/grid-fields/) V8,
  [`primers/relativity-on-a-lattice.md`](../primers/relativity-on-a-lattice.md) §9

---

## 1. The question

Two related proposals, which should be separated because they fare
very differently.

**(a) The untwisted reading.** What if a complete circuit around a
compact dimension *literally is* a unit of time — not an analogy
for a clock but the thing itself? This would give time a mechanical
description rather than a primitive one.

**(b) The twisted reading.** What if the compact dimension is woven
into t with a slight **shear**, so that each trip around arrives
not at the same t but at a small offset Δ? Going around would then
advance time by construction, and time would be *generated* by
circulation rather than merely measured by it.

## 2. First, two notions of time already in GRID

Before judging either, it is worth noticing that GRID already
carries two distinct things called time, and that conflating them
is the source of most of the confusion here.

| | What it is | Whose | Behaviour under motion |
|---|---|---|---|
| **The tick** | A2's single causal dimension; one update of the lattice | Shared by everything; absolute | Unchanged — the lattice updates at one rate, by definition |
| **The winding phase** | A3's compact phase, advanced by a winding excitation | Each particle's own | Runs slow by 1/γ relative to the tick |

The tick is the substrate's own bookkeeping. The winding phase is
**proper time** — what a clock made of that particle would read.

## 3. Verdict on (a): already true, and not a new posit

The untwisted reading is not a proposal. It is a description of
what A3 already says.

[A3](../grid/foundations.md) gives each cell a compact phase, and a
winding excitation on a compact sheet carries a conserved winding
number. The circulation rate **is** the particle's mass, via

> E = ℏω  and  E = mc²

so one circuit already equals one tick of that particle's own
clock. Nothing further is needed to make circulation temporal in
the proper-time sense.

The ratio between the two columns of §2 is time dilation, and it is
derivable rather than assumed. A particle's total propagation speed
through the lattice is capped; moving in x leaves less available
for circulating, by the Pythagorean budget, so the circulation rate
drops by 1/γ. That derivation is carried out in
[`primers/relativity-on-a-lattice.md`](../primers/relativity-on-a-lattice.md)
§9, where the velocity budget is taken from the *measured*
isotropy of the lattice rather than postulated — which is what
separates it from
[Q117](Q117-relativistic-effects-from-velocity-partition.md) §3,
whose version assumes the budget it then reads γ off.

So: **the mechanical account of time that (a) asks for is already
in hand.** What (a) usefully does is name it clearly.

## 4. Verdict on (b): well-defined, and it costs two things

The shear is a real mathematical object: a **twisted
compactification**. Formally, instead of identifying points that
differ by one circuit of the compact direction,

> (x, c, t) ~ (x, c + L_c, t)

one identifies

> (x, c, t) ~ (x, c + L_c, t + Δ)

where L_c is the circumference and Δ the shear. This is the same
construction that turns a cylinder into a Möbius-like twisted
bundle, and such identifications appear routinely in string
compactifications (Scherk–Schwarz twists). It is not ill-formed.

It has two costs.

### Cost 1 — isotropy, or causality

The compact direction has no preferred direction of travel.
Circulating one way advances t by +Δ; circulating the other way
advances it by −Δ. Either:

- the two directions are genuinely equivalent, in which case a
  winding excitation running the "wrong" way carries time
  **backward**, and A2's causal ordering is violated; or
- the two directions are *not* equivalent, which breaks the
  isotropy of a dimension that A1/A2 treat as having none, and
  requires a mechanism that selects the sense.

The second is not fatal — a chirality in the compact sector is
exactly the sort of thing forma entertains elsewhere (see
[Q139](Q139-anomalous-magnetic-moment-from-primitive-chirality.md),
[Q137](Q137-alpha-as-aleph-aspect-ratio.md)) — but it is a
structural commitment, not a free parameter.

### Cost 2 — a detectable preferred frame

This is the heavier cost.

The identification (x, c, t) ~ (x, c + L_c, t + Δ) is a statement
about which t a circuit returns to. Boost along x and t mixes with
x, so the identification acquires an **x-shift** it did not have:
in the boosted frame, a circuit returns to a different *place* as
well as a different time. The twist is "pure" in exactly one frame
— the one in which it was specified.

That frame is then not merely a substrate frame but an
**observable** one, because the winding structure differs
measurably between frames. [Q142](Q142-absolute-lattice-frame-vs-relativity.md)
sets out why this matters: GRID's existing position is Lorentz
ether theory, in which the lattice frame is real but *undetectable*
— and that position survives precisely because nothing in the
observable physics distinguishes it. A twist with a frame-dependent
signature forfeits that, and must then explain why no experiment
has found it.

Note the contrast with the compact direction's ordinary spatial
status, which [Q144](Q144-euclidean-vs-lorentzian-orthogonality.md)
§5 establishes from the measured dispersion ω² = c²k_x² + ω₀²: the
compact momentum enters on the mass side with a **plus** sign, the
signature of a spatial direction. The shear proposal does not
contradict that — it keeps the direction spatial and adds a bundle
twist — but it means the proposal cannot be motivated by "the
compact direction is secretly temporal." It is not.

## 5. What the shear was hoped to buy, and whether it does

The shear was introduced in part to rescue a length-contraction
argument: if a particle does not *run around* the tube but **lives
at all points around it at once** as a standing wave, then the
helix picture changes, and a stick set in motion might have its
ends placed on slanted paths.

Two observations:

- **The standing-wave reading is correct and does not need the
  shear.** A winding mode is already delocalised around the compact
  direction; "running around the tube" is a picture of the phase
  velocity, not of a point particle in orbit. This changes nothing
  about the compact direction's signature, and so does not rescue
  the construction — [Q144](Q144-euclidean-vs-lorentzian-orthogonality.md)
  §4 shows the obstruction is the signature, not the particle's
  localisation.
- **The acceleration-wave intuition is sound and is already
  known.** The idea that a stick set in motion has some of its
  parts start before others, with the disturbance travelling
  through the stick, is **Born rigidity**. The proper-acceleration
  profile a rigid rod must follow is

<!-- a(x) = a0 / (1 + a0 x / c^2) -->
$$
a(x) = \frac{a_0}{1 + a_0 x / c^2}
$$

  — the trailing end accelerates harder than the leading end, which
  is exactly what shortens the rod. This is standard relativity and
  it is where forma's contraction mechanism actually lives
  ([primer §11](../primers/relativity-on-a-lattice.md)). It needs
  no shear.

So the shear's motivating work is done by other means, which lowers
the value side of the ledger considerably.

## 6. What would make the shear worth paying for

The costs in §4 are worth paying only if the twist buys something
nothing else does. Candidates, none evaluated:

- **A derived arrow of time.** If the sense of circulation is
  selected by a chirality already needed elsewhere in the model,
  the twist would supply a direction for t rather than assuming
  one — which is a standing gap, not a manufactured one.
- **A quantisation condition.** A twisted bundle admits fewer
  consistent winding modes than an untwisted one. If Δ were fixed
  by requiring the spectrum to close, it would become a prediction
  rather than a parameter.
- **A route into Q138's Reading B.** If t is generated by
  circulation, time stops being a peer dimension and becomes a
  derived balance — which is exactly the reading
  [Q138](Q138-time-as-peer-dimension-or-bookkeeping-balance.md)
  holds open.

Absent one of these, the untwisted reading of §3 does the
explanatory work at no cost, and the shear should be recorded as a
specific construction that was defined and set aside — not as an
idea refuted.

---

*Appeal classification: §4's twisted compactification and §5's
Born-rigidity profile are **standard physics**. §2, §3 and the
cost analysis are **GRID-specific**, resting on A2, A3 and the
measured dispersion.*

*Connects to: Q138 (what time is), Q76 (signature), Q144 (the
compact direction is spatial), Q142 (the cost of a detectable
frame), grid-fields V8*
