# Q142. Does GRID's absolute lattice frame falsify relativity?

**Status:** Answered — no. An undetectable preferred frame is not a
refutation; it is Lorentz ether theory, which is empirically
indistinguishable from special relativity. The real obligations are
(a) deriving the compensations rather than assuming them and
(b) universality.
**Related:**
  [Q141](Q141-emergent-lorentz-invariance-from-grid.md) (emergent Lorentz invariance — this entry narrows its §5),
  [Q117](Q117-relativistic-effects-from-velocity-partition.md) (velocity-partition mechanism),
  [Q144](Q144-euclidean-vs-lorentzian-orthogonality.md) (why path geometry does not supply contraction),
  [Q76](Q76-origin-of-metric-signature.md) (origin of metric signature),
  [`primers/relativity-on-a-lattice.md`](../primers/relativity-on-a-lattice.md) (the full operational derivation),
  [`grid/sim-lorentz/`](../grid/sim-lorentz/) (the measurements),
  [`grid/foundations.md`](../grid/foundations.md) (A1, A2)

---

## 1. The question

GRID posits a discrete lattice with a definite rest frame — the
frame in which the lattice sits still and the tick advances
uniformly. Relativity is usually summarised as *"there is no
preferred frame."* These look contradictory.

The sharpest form of the challenge is the one that motivated this
entry: two observers moving at different speeds relative to a light
emitter both measure the same light speed c. On a lattice, light
moves at a fixed number of cells per tick **in the lattice frame**.
A moving observer is chasing it. Surely they must measure less.

Does GRID fail this test?

## 2. Short answer

No — but not for the reason usually given, and the correct reason
is weaker than the usual one.

The usual move is: *"the measuring instruments are themselves made
of lattice excitations, so they contract and dilate by exactly the
right amount, and the lattice becomes undetectable."* That is the
right shape of answer, but as stated it is an assertion, not an
argument — it names the conclusion as the mechanism. The honest
version has three parts:

1. **Relativity's empirical content is about round trips, not one-way
   speeds.** A one-way speed cannot be measured without first
   synchronising two separated clocks, and synchronising them
   requires already knowing a one-way speed. This is a structural
   circularity, not a technological limitation (§5).
2. **A round-trip measurement on a moving apparatus really does take
   longer** — by exactly γ², derived in the lattice frame with no
   relativity assumed. It reports c anyway only if the rod is short
   by γ **and** the clock is slow by γ. Two independent
   compensations, each of which GRID must *produce*, not assume
   (§4).
3. **If it produces them, the lattice frame exists but is
   undetectable.** That position has a name and a history: Lorentz
   ether theory (§6).

The full derivation — the γ² delay, why the longitudinal and
transverse cases demand different numbers, and what is left over —
is in [`primers/relativity-on-a-lattice.md`](../primers/relativity-on-a-lattice.md).
This entry states the framework-level consequence.

## 3. What "falsify relativity" would actually require

Relativity is not the claim *"no frame is distinguished by
anything."* It is the claim that **no experiment distinguishes
one inertial frame from another.** Those differ.

To falsify it you would need a measurable, frame-dependent
quantity. Candidates:

| Candidate signature | What it would look like | Current status |
|---|---|---|
| Round-trip light speed depends on direction | Michelson–Morley fringe shift | Null to ~10⁻¹⁷ |
| Round-trip light speed depends on lab velocity | Kennedy–Thorndike null result | Null |
| Clock rate vs. γ departs from prediction | Ives–Stilwell / ion-storage | Confirms γ |
| Different sectors dilate by *different* γ | Clock-comparison (Hughes–Drever type) | Null at extraordinary precision |
| Dispersion: high-energy photons arrive late | Gamma-ray burst timing | Null |

These are the legs of the **Robertson / Mansouri–Sexl test
theory**, the standard framework for parameterising *how* a theory
could deviate from relativity. Note the shape of the list: every
entry is a comparison of two measurements made in the same lab.
None of them measures a one-way speed, because none of them can.

GRID predicts null results on the first three by construction *if*
the compensations hold. The fourth is where it is genuinely
exposed (§7). The fifth it predicts at
~(ℓ_Planck/λ)² ≈ 10⁻⁴⁰ — far below any measurement.

## 4. The γ² delay and the two compensations

This is the operational core, stated compactly. Work entirely in
the lattice frame; assume only that light moves at c cells per tick
there, and that the apparatus moves at v.

Send light along a rod of lattice-frame length L, from one end to a
mirror and back. Outbound, the mirror is running away, so the
closing speed is c − v. Inbound, the near end is running to meet
it, closing speed c + v. Total time:

<!-- T = L/(c-v) + L/(c+v) = (2L/c) / (1 - v^2/c^2) = (2L/c) gamma^2 -->
$$
T = \frac{L}{c-v} + \frac{L}{c+v} = \frac{2L/c}{1 - v^2/c^2} = \frac{2L}{c}\gamma^2
$$

The delay is **real** and it is γ², not γ. The apparatus computes a
speed as 2L′/T′, where L′ is the length it believes its rod has and
T′ is what its own clock reports. To get c back it needs

> (L′/L) × (T/T′) = γ²

and the only way to get that factor out of two physical effects is

- **the rod is short by γ**: L′ = L/γ is what the lattice-frame
  observer measures, so the moving observer's own ruler says L′γ…
  equivalently, the proper length exceeds the lattice-frame length
  by γ; and
- **the clock is slow by γ**: T′ = T/γ.

Each contributes one factor of γ. **Neither alone suffices.** This
is why *"time dilation plus length contraction"* is not a
redundant pair of requirements but exactly the two factors needed,
and why demonstrating only one would leave GRID off by γ.

Turn the apparatus sideways and the arithmetic changes: the
transverse round trip picks up only one factor of γ geometrically,
so it demands contraction of exactly **1** across the motion.
Contraction must therefore be *directional* — 1/γ along, 1 across.
A mechanism that shrank things isotropically would fail.

## 5. Why the one-way speed is not measurable even in principle

This is the point that makes the whole position coherent, and it is
standard physics, not a GRID claim.

To measure a one-way speed you need a clock at each end,
synchronised. The standard procedure (Einstein synchronisation) is
to send a light signal from A to B and declare it arrived at the
midpoint of A's send and receive times — which **assumes** the
outbound and inbound speeds are equal. That is the thing you were
trying to measure. Transporting a clock from A to B instead does
not help: the transported clock's reading depends on its own
dilation history, which depends on the same unknown.

Reichenbach formalised this as the **conventionality of
simultaneity**: the split of a measured round-trip time into
outbound and inbound legs is a free parameter ε ∈ (0,1), fixed by
convention rather than measurement. Einstein's choice is ε = ½.
A lattice-frame-based choice is a different ε. **No experiment
distinguishes them.**

So "the lattice has a preferred frame" and "light is isotropic in
every frame" are not in conflict. The first is a statement about a
convention-dependent quantity; the second is about round trips.

## 6. Lorentz ether theory: the position GRID actually occupies

Before Einstein, Lorentz and Poincaré had a complete theory in
which there **is** a rest frame (the ether), and moving objects
genuinely contract and moving clocks genuinely slow, as dynamical
effects of motion through it. The resulting transformations are the
Lorentz transformations — the same ones. Every prediction matches
special relativity.

That theory was not refuted. It was **set aside** on grounds of
parsimony: if the frame can never be detected, Einstein's version
says the same things without postulating it. Mathematically they
are the same theory in different clothes.

GRID is in Lorentz's position, with one advantage and one debt:

- *Advantage.* Lorentz had to **postulate** the contraction (the
  "Lorentz–FitzGerald contraction hypothesis") as a property of
  matter in motion through the ether. GRID has an actual substrate
  whose dynamics can be computed, so contraction is in principle a
  **derivable** consequence rather than a posit. See §8.
- *Debt.* Everything in [`grid/`](../grid/) that treats "no
  preferred frame" as established is, until those derivations land,
  asserting what Lorentz postulated.

**The framework consequence: an absolute lattice is not a defect to
be explained away.** It is an explicit commitment to the LET branch
of an empirically undetermined choice. That is a legitimate
position and should be stated as one, rather than apologised for or
quietly dropped.

## 7. Where GRID is genuinely exposed: universality

The compensations have to be **the same for everything**. Not
approximately — exactly, and for every sector of the theory.

The reason is that γ cancels out of a measurement only if the ruler
and the clock and the thing being measured all carry the same γ. If
the electromagnetic sector dilated by γ_EM and the compact-phase
(mass) sector by a slightly different γ_Ma, the ratio γ_EM/γ_Ma
would be a measurable, velocity-dependent, frame-dependent number.
Comparing two clocks built on different physics while the lab's
velocity changes over a year is precisely the Hughes–Drever
clock-comparison experiment, and it is null at extraordinary
precision.

This is a real vulnerability for GRID specifically, because GRID
has *several structurally different sectors* — space modes, compact
windings, the ℵ line — and nothing yet forces them to share one γ.
It is the one requirement on the list that a lattice theory could
plausibly fail.

First measurement, in
[`F2`](../grid/sim-lorentz/F2-boost-and-universality.md): rest mass
is boost-invariant to **0.003%** at small momentum, degrading at
the lattice scale. The light and heavy sectors degrade at different
*relative* rates, though the light sector's **absolute** drift is
the smaller of the two. Universality therefore holds in the
long-wavelength limit and is untested outside it.

## 8. What has now been measured

[`grid/sim-lorentz/`](../grid/sim-lorentz/) exists to replace
assertion with measurement on exactly these points:

| Requirement | Result | Caveat |
|---|---|---|
| One wave speed, every direction | isotropic to 2.8 × 10⁻¹¹ at ~300-cell wavelength | raw lattice operator — no caveat |
| ω² − c²k² invariant under boost | 0.003% at small k | raw lattice operator — no caveat |
| Contraction 1/γ along motion | 0.1% for v ≤ 0.8c; residual shown to be discreteness | sine-Gordon reduction, not raw scatter |
| Coasting without radiating | energy constant to 2 × 10⁻⁵ | same caveat |
| Contraction 1 across motion | **not yet run** | — |
| Universality across sectors | long-wavelength only | — |

The caveat matters and is stated in full in that directory's
README: the contraction result runs on grid-matter's sine-Gordon
*reduction*, whose on-site nonlinearity was added by hand. It
establishes that **the sector forma uses to model bound matter is
Lorentzian**. Whether the raw GRID scatter produces that sector is
a separate open question.

## 9. Correction to Q141 §5

[Q141](Q141-emergent-lorentz-invariance-from-grid.md) §5 opens
*"The recovery is complete,"* and supports Lorentz contraction with
*"Same source — same evidence, same MaSt-level mechanism via
Q117."*

That is narrower than stated. The evidence cited in Q141 §3 is the
**linear photon dispersion** ω ≈ 0.41·k. Linear isotropic
dispersion gives requirement 1 — one wave speed, every direction.
It does not, by itself, give contraction or dilation, which are
properties of *bound states* moving through the lattice, not of the
dispersion relation of free light. Q141 inherits those from Q117,
and Q117 §5 supplies a picture ("wave crests pile up in the
direction of motion") rather than a derivation.

The repair is not to retract Q141's conclusion but to re-base it:
contraction is now **measured** in
[`F3`](../grid/sim-lorentz/F3-contraction-and-coasting.md) rather
than inherited, and the status of the claim is "measured in the
sine-Gordon sector, open for the raw scatter."

## 10. What would change the answer

GRID's relativity claim would be in real trouble if any of these
landed:

- **A sector-dependent γ** survives into the long-wavelength limit
  (§7). This is the live one.
- **Transverse contraction is not exactly 1** (T6, unrun). A
  mechanism producing isotropic shrinkage would be the wrong
  mechanism even if it got the longitudinal factor right.
- **A coasting bound state radiates** at the lattice scale in a way
  that does not vanish as (spacing/width)². Uniform motion would
  then be distinguishable from rest — the sharpest possible
  Lorentz violation, requiring no interpretation. First measurement
  says it does not, within the reduction.

Conversely, none of the following would falsify anything: the
existence of the lattice frame, the lattice frame being
mathematically specifiable, or the one-way speed differing between
frames under a non-Einstein convention. Those are features of the
LET branch, not bugs.

---

*Appeal classification: §3, §5, §6 are **standard physics** (test
theories, conventionality of simultaneity, Lorentz ether theory).
§4 is a derivation carried out in the lattice frame, assuming only
a fixed lattice-frame light speed. §7, §8, §9 are **GRID-specific**
claims and measurements.*

*Connects to: Q141 (narrowed by §9), Q117 (mechanism), Q144
(signature), Q76 (why the signature is Lorentzian at all),
primers/relativity-on-a-lattice.md, grid/sim-lorentz/*
