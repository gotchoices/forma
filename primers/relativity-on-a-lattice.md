# Relativity on a Lattice — Why a Discrete Substrate Can Still Look Lorentzian

A self-contained walk-through of the one objection every
discrete-spacetime model has to answer:

> A lattice has a rest frame. Relativity says there is no such
> thing. How can both be true?

This primer answers it operationally — not by appealing to a
symmetry principle, but by following a real measurement through,
step by step, and watching the lattice frame become undetectable.
The arithmetic is deliberately elementary: nothing beyond square
roots is needed.

**Prerequisite:** none. [metric.md](metric.md) covers the same
territory from the *geometry* side — the metric tensor, the light
cone, interval classification — and the two are complementary.
The metric primer says *"spacetime has this geometry, here is what
follows."* This primer says *"here is an apparatus, here is what it
reads, and here is why it cannot see the lattice."* Either can be
read first.

---

## Concepts introduced in this primer

| § | Concept |
|---|---------|
| 1 | The puzzle: a substrate with a rest frame |
| 2 | What a lattice gives for free: one speed, every direction |
| 3 | How the speed of light is actually measured |
| 4 | The measurement at rest in the lattice |
| 5 | The measurement in motion — the γ² delay |
| 6 | The two compensations, and why they cancel exactly |
| 7 | The same measurement, turned sideways |
| 8 | The specification: three exact numbers |
| 9 | Where clocks get their γ: circulation on a compact dimension |
| 10 | Why path geometry cannot supply length contraction |
| 11 | Where length contraction does come from |
| 12 | The third requirement: universality |
| 13 | Simultaneity is a convention, not an ingredient |
| 14 | Lorentz ether theory: an undetectable frame is not a refutation |
| 15 | Scoreboard: measured, derived, assumed, open |
| 16 | The essential insight |

---

## 1. The puzzle: a substrate with a rest frame

GRID posits that space is a discrete lattice — a regular array of
cells, each talking only to its neighbours, updating in discrete
steps. The update step is called a **tick**. One tick moves
information exactly one cell, which fixes a speed: c = L/τ, where
L is the cell spacing and τ the tick duration.

A lattice like this plainly has a **rest frame**: the frame in
which the cells sit still. Call it the **lattice frame**. In that
frame the lattice looks like a neat crystal. Viewed from a frame
moving through it, the cells stream past.

That looks fatal. Special relativity's founding claim is that no
experiment can single out one inertial frame as "the" frame at
rest — and here is a model with a frame visibly at rest. Worse,
the nineteenth century already ran this experiment. Michelson and
Morley looked for the Earth's motion through a light-carrying
medium and found nothing, to a precision that embarrassed the
medium out of physics.

A crystal is not rescued by being fundamental, either. A quartz
crystal is not embedded in anything else and it still has a
perfectly good rest frame. "The lattice *is* space, so there is no
outside to move through" sounds like an answer but is not one: an
observer can still move relative to the cells, and the question is
whether any instrument notices.

The resolution is more interesting than either "the lattice is
undetectable because it is small" or "relativity is built in." It
is that the measurement itself is distorted, by exactly the amount
needed to hide the distortion. Working that out is the business of
this primer.

A term that will be needed throughout: an **inertial frame** is a
point of view moving at constant velocity, carrying its own rulers
and clocks. The whole question is what those rulers and clocks
read.

---

## 2. What a lattice gives for free: one speed, every direction

Before the hard part, one piece of good news that a lattice really
does supply.

A crystal is not isotropic in the obvious sense — it has axes,
corners, preferred directions. The natural worry is that waves
travel faster along a lattice axis than diagonally, which would
show up immediately as a direction-dependent speed of light.

This is checkable, and on GRID's honeycomb lattice it has been
checked. The lattice-scale result: waves whose wavelength is long
compared to the cell spacing travel at the same speed in every
direction, to extraordinary precision.

| wavelength (in cells) | direction-dependence of wave speed |
|---|---|
| ~300 | 2.8 × 10⁻¹¹ |
| ~30 | 2.8 × 10⁻⁷ |
| ~6 | 1.9 × 10⁻⁴ |
| ~3 | 4.0 × 10⁻³ |

The direction-dependence falls as roughly the **fourth power** of
(cell spacing / wavelength). The measured long-wavelength speed on
the honeycomb is 0.40824828 cells per tick, numerically
indistinguishable from 1/√6 — suggesting a closed form rather than
a numerical accident, though that has not been derived.

Why does the anisotropy vanish? Because a long wave averages over
many cells, and averaging washes out the lattice's angular
structure. This is the same reason a steel beam has no grain
direction at engineering scale even though it is polycrystalline.

The practical upshot: **at long wavelength, light on the lattice
has one speed, in every direction.** That single fact is the only
physical input the rest of this primer needs. Everything else is
arithmetic.

It is worth being precise about what this does *not* settle. One
speed in every direction means a stationary apparatus sees no
direction-dependence. It says nothing yet about an apparatus in
motion, which is the actual question.

---

## 3. How the speed of light is actually measured

Any measurement of light speed, in any laboratory, has the same
three parts: something that marks out a distance, something that
marks out a time, and a signal that traverses the distance.

The cleanest version is a **round trip**:

```
        clock
          |
      [  A  ]-------- L₀ --------[ mirror ]
          |
      pulse out  ----------------->
      pulse back <-----------------
```

A pulse leaves point A, bounces off a mirror a distance L₀ away,
and returns to A. One clock, at A, reads the elapsed time T. The
reported speed is

> c_measured = 2L₀ / T

Two features of this arrangement matter enormously, and both are
easy to overlook.

**It uses one clock, not two.** The pulse leaves from A and
returns to A. There is never any need to decide whether a clock at
A and a clock at the mirror are showing the same time. That
question — clock synchronization — is deferred entirely, and §13
returns to it.

**Every real experiment has this shape.** Michelson–Morley,
interferometers of every kind, radar ranging, spectroscopy, the
timing loops inside GPS: all closed loops, signal out and signal
back to the same clock. There is a reason for that, also covered
in §13: a genuine one-way measurement turns out not to be
available even in principle.

So the question "what does a moving observer measure for the speed
of light?" becomes the concrete question: **what does this
particular apparatus read when the whole thing is moving through
the lattice?**

The quantity L₀ deserves a name. It is the rod's **rest length** —
its length as measured by rulers moving along with it. Whether
that is also its length as measured in the lattice frame is
exactly what is at issue.

---

## 4. The measurement at rest in the lattice

Start with the easy case. The apparatus sits still in the lattice
frame.

Light crosses the rod at speed c in each direction — that is §2's
result, and here the rod is not going anywhere, so there is
nothing further to account for. The pulse covers L₀ out and L₀
back:

> T = 2L₀ / c

and the measurement reports 2L₀ / (2L₀/c) = **c**.

Unremarkable, but it establishes the baseline. The next two
sections repeat the identical calculation with the apparatus in
motion, and the whole content of relativity falls out of the
difference.

---

## 5. The measurement in motion — the γ² delay

Now set the entire apparatus moving through the lattice at speed
v, with the rod pointed **along** the direction of travel.

The key move — and the reason this derivation needs no relativity
as an input — is to compute everything **in the lattice frame**,
where there is no mystery at all. In the lattice frame, light
simply goes at c (§2), and the rod is simply a moving object.
Nothing more is assumed.

```
   lattice frame, rod of length L moving right at v:

   pulse out:   A ----->                [mirror] -->
                        the mirror is running away

   pulse back:  A -->          <----- [mirror]
                        the back end is rushing to meet it
```

**Outbound.** The pulse leaves the back end at speed c. The mirror
is retreating at v. The gap between them therefore closes at rate
(c − v), and the gap to close is L, the rod's length *in the
lattice frame*:

> t_out = L / (c − v)

**Return.** The pulse heads back at speed c while the rod's back
end advances to meet it at v. Closing rate (c + v):

> t_back = L / (c + v)

Adding them, and writing the result over a common denominator:

<!-- T = L/(c-v) + L/(c+v) = 2Lc/(c^2 - v^2) = (2L/c) * 1/(1 - v^2/c^2) -->
$$
T = \frac{L}{c-v} + \frac{L}{c+v}
  = \frac{2Lc}{c^{2}-v^{2}}
  = \frac{2L}{c}\cdot\frac{1}{1 - v^{2}/c^{2}}
$$

That trailing factor appears so often it gets a name. Define the
**Lorentz factor**:

<!-- gamma = 1 / sqrt(1 - v^2/c^2) -->
$$
\gamma = \frac{1}{\sqrt{1 - v^{2}/c^{2}}}
$$

γ equals 1 when v = 0, grows slowly at first (γ = 1.005 at
v = 0.1c), reaches 1.25 at v = 0.6c, and runs away to infinity as
v approaches c. In terms of γ:

> **T = (2L / c) · γ²**

**This is the central fact of the whole primer.** A moving
apparatus really does take γ² longer for the round trip than a
stationary one of the same lattice-frame length. The delay is not
an illusion, not a matter of interpretation, and not small: at
v = 0.6c it is 56% longer.

Notice also what the two legs look like separately. Outbound, the
pulse closes on the mirror at (c − v). Inbound, at (c + v). The
speed of light *relative to the apparatus* is not c in either
direction. The intuition that a moving observer ought to see light
going at some speed other than c is not wrong — in the lattice
frame it is exactly right.

And yet the observer reports c. The next section shows why.

---

## 6. The two compensations, and why they cancel exactly

The observer computes 2L₀ / T using *their own* rod length and
*their own* clock. Neither is trustworthy, and the two failures
have a specific size.

**Compensation one: the rod is shorter.** Suppose a rod moving
through the lattice is physically contracted along its direction
of motion, so that a rod of rest length L₀ occupies only

> L = L₀ / γ

of lattice-frame length. Substituting into §5's result removes one
factor of γ:

> T = (2L₀ / c) · γ² / γ = (2L₀ / c) · γ

**Compensation two: the clock is slow.** Suppose a clock moving
through the lattice ticks slowly by the same factor γ. Then the
lattice-frame duration T registers on that clock as only T / γ:

> T_read = (2L₀ / c) · γ / γ = **2L₀ / c**

**And the observer still calls the rod L₀ long.** This step is
easy to skip and essential. The rod contracted — but so did every
other ruler the observer owns, including the one used to measure
the rod. By their own metrology the rod is unchanged. There is no
uncontracted ruler anywhere in their laboratory to catch the
discrepancy.

Putting it together:

> c_measured = 2L₀ / (2L₀ / c) = **c**

**Two factors of γ have eaten the γ².** That is the mechanism, and
it is worth stating in words because the algebra makes it look
slighter than it is:

> Light genuinely takes γ² longer to make the round trip. The
> observer's ruler is short by γ and their clock is slow by γ.
> The product of the two errors is γ², which is exactly the
> delay. The measurement comes out to c for the wrong reasons,
> and no instrument in the laboratory can detect that.

For readers with an instrumentation background, the situation is
familiar: measuring a signal's transit time with a ruler that has
shrunk and a timebase that has slowed, where both have drifted by
the same factor as the calibration standard. The reading is
"right," the apparatus is wrong, and there is no second reference
to reveal it.

Nothing in this argument requires the lattice to be small, or the
corrections to be tiny, or the observer to be ignorant. It
requires exactly two things to be true about moving matter:
contraction by γ and dilation by γ.

---

## 7. The same measurement, turned sideways

One case remains, and it carries more weight than it first
appears to. Point the rod **across** the direction of travel.

```
   lattice frame, rod transverse to motion:

        [mirror]        [mirror]
           ^               ^  \
           |                \  \     light must travel
           |                 \  \    diagonally to catch
           |                  \  \   a mirror that is
        [  A  ]  -->        [  A  ]  moving sideways
```

The mirror is no longer running away — it is sliding sideways. But
the pulse must still *catch* it, so the pulse travels a diagonal
path, longer than the rod.

Let T be the lattice-frame round-trip time. In half that time the
apparatus has moved sideways by v·T/2, while the pulse has
travelled c·T/2 along its diagonal. The rod's length is the third
side of a right triangle:

<!-- (cT/2)^2 = L0^2 + (vT/2)^2  ->  T = 2 L0 / sqrt(c^2 - v^2) = (2 L0/c) gamma -->
$$
\left(\frac{cT}{2}\right)^{2} = L_{0}^{2} + \left(\frac{vT}{2}\right)^{2}
\quad\Longrightarrow\quad
T = \frac{2L_{0}}{\sqrt{c^{2}-v^{2}}} = \frac{2L_{0}}{c}\,\gamma
$$

The transverse rod is written as L₀ with no contraction factor,
because transverse lengths are *not* contracted. The delay here is
γ, not γ², and the clock's single factor of γ absorbs it exactly:

> T_read = (2L₀ / c) · γ / γ = 2L₀ / c → reports **c**

So both orientations report c — but they need **different**
amounts of help:

| rod orientation | lattice-frame delay | length change required | clock change required |
|---|---|---|---|
| along the motion | γ² | **1/γ** | 1/γ |
| across the motion | γ | **1** (none) | 1/γ |

This asymmetry is not a curiosity; it is the whole reason
Michelson–Morley came out null. Michelson's interferometer
compares a longitudinal arm against a transverse arm. If both arms
contracted, or neither did, the two would disagree and the fringes
would shift. The specific combination — contract along the motion,
leave the transverse alone — is what makes them agree.

It also means **one adjustable parameter cannot do this job.** A
model that slows clocks but leaves lengths alone fails the
longitudinal case. A model that contracts lengths isotropically
fails the transverse case. The two effects are independent
requirements with independently specified values.

---

## 8. The specification: three exact numbers

Sections 5 through 7 have converted a philosophical worry into an
engineering specification. For a lattice to hide its rest frame
from this apparatus, moving matter must satisfy:

| # | Requirement | Value |
|---|---|---|
| 1 | contraction along the direction of motion | exactly 1/γ |
| 2 | contraction across the direction of motion | exactly 1 (none) |
| 3 | slowing of clocks | exactly 1/γ |

"Exactly" is doing real work. The compensations must multiply to
γ², and γ² is what the delay is — no more, no less. A model
delivering contraction of 1/γ^0.99 would leave a residue that
grows with v and shows up as a fringe shift.

There is a fourth requirement, invisible in the table because it
is a condition *on* the first three rather than a fourth
phenomenon. It is important enough to get its own section (§12).

The remaining question is whether a lattice actually delivers
these numbers. Sections 9 through 11 take the clock and the ruler
in turn.

---

## 9. Where clocks get their γ: circulation on a compact dimension

This section needs one structural idea from the forma framework: a
**compact dimension**. The picture is a long cylinder. Along its
length runs ordinary space, written x. Around its circumference
runs a second direction, small and closed on itself, written c.
Travel far enough around c and the starting point returns. (See
[metric.md](metric.md) §12 and
[kaluza-klein.md](kaluza-klein.md) for the full treatment.)

In this picture a **massive particle** is a wave that circulates
around the compact direction — a standing wave wrapped around the
cylinder's circumference, rather than a little ball. Its
circulation rate is its mass: a faster-circulating wave is a
heavier particle, through E = ℏω.

The important consequence is that **such a particle is a clock.**
Not a clock by analogy — the circulation is a periodic process
with a definite rate, which is what a clock is. One circuit is one
tick of that particle's own time.

Now set the particle moving along x. Its wave still travels at the
lattice speed c — §2, and it has nothing else to travel at. But
that speed must now be shared between two directions: some of it
goes into advancing along x, and only what remains goes into
getting around c. The path traced on the cylinder is no longer a
circle but a **helix**.

```
   at rest:  a circle          moving:  a helix (longer way round)

     .-''-.                      .-''-.
    /      \                    /      \___
   |        |                  |            \___
    \      /                    \_              \___
     `-..-'                        `-.._             \___
                                        `-..__           \__
    x fixed                          -------- x ---------->
```

Speed on the surface is fixed at c, so the components satisfy
Pythagoras in the surface:

> v_x² + v_c² = c²

With v_x = v, the compact-direction speed is

> v_c = c·√(1 − v²/c²) = c / γ

Getting around c once means covering the circumference L_c at
speed v_c, so the time per circuit is

> T_circuit = L_c / v_c = **γ · (L_c / c)**

**The clock runs slow by exactly γ.** Requirement 3 of §8 is met,
and not by assumption — by the geometry of a fixed-speed wave
sharing its speed between two directions.

Note what this derivation needs: only that the lattice carries
waves at one speed in every direction (§2). It does not assume the
spacetime metric, which would be circular. The decomposition
v_x² + v_c² = c² is Pythagoras applied to a velocity in a surface,
and it holds because the surface speed is isotropic — which was
measured, not posited.

Two cautions.

**A limiting case worth noticing.** As v → c, v_c → 0: the wave
travels straight along the cylinder and never gets around at all.
That is a wave with no circulation, hence no mass — light. The
framework's claim that a massive particle cannot reach c becomes
the statement that it cannot stop being a clock.

**A frequency that is easy to confuse.** A moving particle's wave
has a *lab* frequency of γω₀, which is faster, not slower. That
number is also correct, and it describes something else: the rate
at which the phase of the whole wave advances in the lattice
frame, which is the de Broglie phase and runs faster than light.
The circulation rate computed above, ω₀/γ, is the particle's
internal clock — the quantity that governs how long an unstable
particle survives. Both are real; they answer different questions.

---

## 10. Why path geometry cannot supply length contraction

Having got the clock from geometry, the natural hope is to get the
ruler the same way. A measuring rod is two particles held apart.
At rest each traces a circle around the cylinder; in motion each
traces a helix. Perhaps the helices come closer together.

They do, in one precise sense — and the sense in which they do is
instructive, because it is not the sense that matters.

Unroll the cylinder into a flat strip, with x running one way and
arc length around the compact direction running the other. Each
particle's path becomes a straight line at an angle α from the
x-axis, where cos α = v/c and therefore sin α = 1/γ. Two particles
offset by d along x trace two **parallel** lines.

The perpendicular distance between two parallel lines offset by d
along x is d·sin α:

> perpendicular distance = d · sin α = **d / γ**

That is a correct calculation and the factor is exactly right.
Confirmed numerically: at v = 0.6c it gives 0.800000 for d = 1
against d/γ = 0.800000; at v = 0.99c, 0.141067 against 0.141067.

And yet this is not length contraction, for two reasons.

**The separation along x never changes.** Parametrize the two
paths: particle 1 at (vt, v_c t), particle 2 at (d + vt, v_c t +
offset). The x-separation is d at every instant, at every
velocity, forever. Stretch the helices out until they are nearly
straight lines and they are still d apart. Helical pitch does not
draw them together; it unwinds them into *parallel* lines, not the
same line.

**The perpendicular connects two different times.** Computing
where the perpendicular from particle 1's position lands on
particle 2's path gives a point that particle 2 occupies at time
−vd/c², not at the same moment. The perpendicular distance is the
distance between two events separated in time. A length is a
separation measured at **one** moment.

There is a deeper reason this attempt cannot work, and it is worth
naming because it is a trap that catches many people.

**The signature trap.** Projecting onto the slice perpendicular to
a worldline is the right *idea*. But "perpendicular" has to be
defined by the right geometry. The unrolled (x, compact) strip is
a plane of two **spatial** directions, so perpendicularity there
is ordinary Euclidean perpendicularity. Relativity's slices are
defined by the spacetime metric, which carries a minus sign on the
time component. The two give different answers — and not slightly:

| | Euclidean perpendicular | relativistic (Minkowski) slice |
|---|---|---|
| time offset of the landing point | −vd/c² | +γ²·vd/c² |
| resulting separation | **d/γ** | **γd** |

The answers are **reciprocal**. At v = 0.9c that is 0.436 versus
2.294 — a factor of γ² = 5.3 apart, with opposite signs on the
offset. The factor γ appears in both because both come from the
same right triangle; which side of the fraction it lands on is
decided entirely by whether the hypotenuse relation carries a plus
or a minus.

This failure mode has a literature. The "everything moves at c
through 4D Euclidean space" picture reproduces γ-factors in form
and is appealing enough to be rediscovered regularly; it diverges
from relativity on velocity addition and on the invariant interval,
for exactly this reason.

In GRID the relevant plane really is Euclidean. Time in GRID is
the *tick* — axiom A2's single causal dimension (see
[grid/foundations.md](../grid/foundations.md)). The compact
direction is spatial: a large number of cells wrapped into a
closed surface. Confirmation comes from the measured dispersion
relation, ω² = c²k_x² + ω₀², in which the compact-direction
momentum enters on the **mass** side with a plus sign — the
signature of a spatial direction.

So §9's success and §10's failure are not inconsistent. The clock
came from path geometry because a clock's rate is a property of a
single path. A length is a property of the *relationship between
two* paths, and that is not geometry. It is dynamics.

---

## 11. Where length contraction does come from

### The distinction that matters

Two rockets accelerate identically, side by side, connected by a
taut string. What happens to the string?

In the lattice frame the rockets' separation never changes — they
followed identical trajectories. But the string's *natural*
length, the length at which it sits unstressed, contracts by γ. So
the string is stretched beyond its natural length, and it snaps.

This is **Bell's spaceship paradox**, and it is the cleanest
available demonstration that two things often conflated are
genuinely different:

- **the separation between two objects** — kinematics, a property
  of trajectories
- **the natural length of a bound object** — dynamics, a property
  of whatever holds it together

Only the second is length contraction. §10 computed something
about trajectories, which is why it could not produce it.

### The resonance argument

So the ruler has to come from the binding. Take two particles held
at separation d by signals passing between them — which on a
lattice is the only option, since everything that propagates does
so at the lattice speed c.

**At rest.** Equilibrium at d₀ is set by a resonance condition:
the round-trip time for a signal crossing and returning, 2d₀/c,
matches the bound state's internal period T₀.

**In motion at v.** Two things have changed, and both have already
been computed.

The round trip between the two particles now takes (2d/c)·γ² —
this is §5, the chase-the-receding-mirror calculation, applied to
the bound state's own internal signalling rather than to a
laboratory apparatus.

The internal period has become γT₀ — this is §9, the helix.

For the bound state to remain the same bound state, the resonance
must still hold:

<!-- (2d/c) gamma^2 = gamma T0 = gamma (2 d0 / c)  ->  d = d0 / gamma -->
$$
\frac{2d}{c}\,\gamma^{2} = \gamma\,T_{0} = \gamma\cdot\frac{2d_{0}}{c}
\quad\Longrightarrow\quad
d = \frac{d_{0}}{\gamma}
$$

**Contraction by exactly 1/γ.** Requirement 1 of §8 is met.

Run the same argument transversely and the crossing takes only
(2d/c)·γ (§7), so matching γT₀ requires **no** contraction at all
— requirement 2, with the asymmetry Michelson–Morley needs.

A useful way to see the same thing: §7's transverse clock ticks at
γT₀, and §5's longitudinal clock, *with no contraction*, would
tick at γ²T₀. If both existed and disagreed, comparing them would
reveal motion through the lattice — Michelson–Morley would have
succeeded. Demanding that they agree is what forces the
longitudinal length down by exactly γ.

### How an object gets there: Born rigidity

The resonance argument says where the equilibrium is. A separate
question is how an object reaches it, and the answer explains why
Bell's string breaks while a real object does not.

An extended object cannot be accelerated rigidly. A push applied
at one end propagates through at the material's signal speed,
never faster than c. Different parts therefore start moving at
different times — the acceleration crosses the object as a wave.

For an object to accelerate without internal stress, the trailing
end must accelerate **harder** than the leading end, by

<!-- a(x) = a0 / (1 + a0 x / c^2) -->
$$
a(x) = \frac{a_{0}}{1 + a_{0}x/c^{2}}
$$

This is **Born rigidity**. An object accelerated by its own
internal binding follows this profile automatically, because the
binding is what does the accelerating and the binding propagates
at finite speed. An object whose ends are pushed *identically* by
external agents does not — which is precisely Bell's setup, and
precisely why the string fails.

So contraction is not something that happens to an object at an
instant. It is the equilibrium an object relaxes into, given an
acceleration history and a binding that communicates at c.

---

## 12. The third requirement: universality

The specification of §8 listed three numbers. The condition that
accompanies them is this:

> **The same γ, for every clock and every ruler, regardless of
> what it is made of or what holds it together.**

The reason is visible in §6. The entire mechanism is two errors
whose product cancels a delay. If a ruler contracts by γ while a
clock dilates by some γ′ ≠ γ, the product is no longer γ² and the
residue is measurable.

Worse, failure of universality does not even need light to detect.
Two clocks of different construction — one governed by
electromagnetic binding, one by nuclear — placed side by side, run
against each other. If they dilate by different factors, they
drift apart as the laboratory's velocity changes through the day
and the year. No interferometer required.

This is exactly what the real precision tests do. Clock-comparison
experiments pit caesium against hydrogen masers, and electronic
transitions against nuclear ones, watching for annual and diurnal
drift. The bounds sit around 10⁻²⁷.

**Universality is where a lattice is most vulnerable.** Different
excitations sit at different wavelengths, and §2 showed that
lattice corrections depend on wavelength. There is no general
reason for two different bound states to pick up the same
correction.

The GRID measurement bears this out. Testing whether a particle's
rest mass stays constant under a boost — equivalently, whether its
clock dilates by the right factor — gives:

| momentum k_x | light mode | heavy mode |
|---|---|---|
| 0.05 | −0.005% | −0.003% |
| 0.20 | −0.501% | −0.059% |
| 0.80 | −116% | −2.2% |

The two sectors do **not** dilate identically. They converge only
as k → 0, where both errors vanish together. So universality holds
in the long-wavelength limit and is lost at the lattice scale.

One structural feature of the forma framework helps considerably
here, and is worth making explicit. §9 derived time dilation from
a wave circulating on a compact dimension — and if *every*
particle is such a circulating wave, then every clock is that kind
of clock, and every one of them dilates by exactly γ with no
appeal to its internal details. The framework's "matter is trapped
light" thesis is doing real work: it converts universality of time
dilation from an extra assumption into a consequence.

The corresponding statement for rulers is weaker. §11's resonance
argument also referenced only c and the lattice, which is
encouraging, but it assumed a particular resonance condition. How
far that generalizes across binding mechanisms is open.

---

## 13. Simultaneity is a convention, not an ingredient

A natural objection to everything above: relativity is famous for
a third effect, the relativity of simultaneity — observers in
motion disagree about which distant events happen at the same
time. §8's specification does not mention it. Is it missing?

It is not, and the reason is worth understanding, because it
closes an apparent gap.

Simultaneity is not a phenomenon the lattice must supply. It is a
**consequence of the procedure an observer uses to synchronize
distant clocks.**

Here is the procedure, because there is only one available. To set
a clock at the far end of a rod against a clock at the near end,
send a light pulse down, bounce it, and assume it took equal time
each way. Declare the reflection simultaneous with the midpoint of
the near clock's reading. There is no alternative — any other
method requires already knowing the one-way light speed, which is
what synchronization is needed to measure.

Follow it through in the lattice frame. The trip out really took
L/(c − v) and the trip back L/(c + v) — §5 again. The observer
splits the difference, which puts the reflection at (L/c)·γ² in
lattice time while the real reflection happened at L/(c − v). The
discrepancy:

<!-- L/(c-v) - (L/c) gamma^2 = L v / (c^2 - v^2) = (L v / c^2) gamma^2 -->
$$
\frac{L}{c-v} - \frac{L}{c}\gamma^{2}
  = \frac{Lv}{c^{2}-v^{2}}
  = \frac{Lv}{c^{2}}\,\gamma^{2}
$$

Converting to the observer's own slow clock (divide by γ) and
their own rest length (L = L₀/γ) leaves

> offset = **L₀ v / c²**

which is exactly the position-dependent term in the Lorentz
transformation. The act of synchronizing by light signals, carried
out by an observer whose rod is contracted and whose clock is
slow, *produces* the relativity of simultaneity.

So the accounting is:

> contraction by γ + dilation by γ + synchronizing with light
> = the full Lorentz transformation

with the relativity of simultaneity, and the reciprocity of time
dilation between two observers, as **theorems** rather than
further assumptions.

Reciprocity deserves a sentence, since it is the part that seems
most paradoxical on a lattice. A particle moving through the
lattice genuinely ticks slow — an absolute effect. Yet relativity
requires the moving observer to see the *stationary* observer's
clock as slow too, symmetrically. What delivers the symmetry is
the simultaneity offset just derived: the moving observer's notion
of "at the same time" is tilted, by precisely the amount that
makes the comparison come out even.

---

## 14. Lorentz ether theory: an undetectable frame is not a refutation

One loose end remains, and tying it off substantially lowers the
bar a lattice has to clear.

Sections 5 through 13 assembled contraction, dilation, and
light-signal synchronization into the Lorentz transformation. But
the synchronization step was a *choice*. Suppose an observer
declined it, and instead set their distant clocks to agree with
the lattice frame's own time — absolute simultaneity. What then?

Every result in this primer survives. Round trips still come out
to c, because §5 through §7 used a single clock. Moving clocks
still run slow by γ. Michelson–Morley still comes out null.

The only thing that changes is the **one-way** light speed, which
such an observer would find to be c − v in one direction and c + v
in the other.

And that quantity is not measurable. Measuring a one-way speed
requires synchronized clocks at two places; synchronizing them
requires knowing the one-way speed. The circle does not open. The
one-way light speed is fixed by convention, not by experiment —
this is Reichenbach's conventionality of simultaneity, and it is
why §3 noted that every real experiment is a closed loop.

The theory that results — a real preferred frame, genuine
contraction and dilation, absolute simultaneity — is **Lorentz
ether theory**, and it was built by Lorentz, FitzGerald and
Poincaré before Einstein. It is *empirically indistinguishable
from special relativity*. Einstein's contribution was not to show
the ether was detectable; it was to show it was superfluous.

The consequence for a lattice model is substantial:

> **GRID does not have to eliminate its rest frame. It has to
> make it undetectable.** A lattice frame that no experiment can
> find is not a defect — it is Lorentz ether theory, and that
> theory passes every test special relativity passes.

This is a lower and far more tractable bar than "derive the
absence of a preferred frame," which is not even the right target.
The target is the three numbers of §8 plus the universality
condition of §12.

---

## 15. Scoreboard: measured, derived, assumed, open

Honest bookkeeping on where the GRID framework actually stands
against the specification.

| Ingredient | Status |
|---|---|
| One wave speed, every direction | **Measured.** Anisotropy 2.8 × 10⁻¹¹ at ~300-cell wavelength, falling as ~(spacing/λ)⁴ |
| One wave speed, every wavelength | **Measured.** Linear dispersion in the long-wavelength limit; deviations ~k² |
| Hyperbolic dispersion ω² = c²k² + ω₀² | **Measured.** Holds to 0.003% at small k |
| Time dilation by γ | **Derived** (§9), from isotropy plus the compact-circulation picture of mass. Not yet verified on a simulated bound state. |
| Universality of time dilation | **Derived conditionally** (§12) — follows if every particle is a circulating wave, which is a framework posit |
| Length contraction by γ, longitudinal | **Measured** — 0.1% agreement for v ≤ 0.8c on a discrete sine-Gordon chain; residual at higher v shown to be discreteness, scaling as (spacing/width)². Caveat: that chain is grid-matter's *reduction* of the compact sector, not the raw scatter. |
| No transverse contraction | **Argued** (§11); not yet measured — needs a 2D run |
| Universality across sectors | **Measured to fail at the lattice scale.** Light and heavy modes drift differently away from k → 0 |
| Coasting without radiating | **Measured** — energy constant to 2 × 10⁻⁵ over six internal periods, speed correct to 0.1%. No radiation, no deceleration, no Peierls–Nabarro trapping. Same reduction caveat as above. |
| Relativistic velocity addition | **Not independent.** Additivity of rapidity is algebraically equivalent to constancy of ω² − c²k², so the boost row already covers it for a free particle |
| Reciprocity / simultaneity | **Derived** (§13) as a theorem of the above, not an extra requirement |

The contraction and coasting rows were the two load-bearing
gaps, and both have now been measured — see
[grid/sim-lorentz/](../grid/sim-lorentz/). What remains open:

- **Transverse contraction.** The specification requires
  contraction along the motion and *none* across it. Only the
  first has been measured; the second needs a genuinely
  two-dimensional run.
- **Born-rigid acceleration.** The measurements boost a state that
  is already moving. They do not watch one *accelerate* into the
  contracted configuration. Accelerating a bound pair through its
  own internal coupling, and checking that the separation relaxes
  to d₀/γ, is Bell's string run on a lattice — and it tests the
  §11 mechanism rather than only its endpoint.
- **Whether the lattice produces the sector being tested.** The
  contraction and coasting runs use a discrete sine-Gordon chain,
  which is a *reduction* of the compact-phase sector with an
  on-site term added by hand. That the sector is Lorentzian is now
  measured; that the GRID scatter yields that sector is a separate
  open question.

A note on how to read the negative entries. "Measured to fail at
the lattice scale" is a statement about where the approximation
ends, not a refutation. Every discrete-substrate model predicts
Lorentz violation at its own scale; that is a prediction, and the
experimental programs hunting for it (gamma-ray-burst timing,
vacuum birefringence bounds) currently find nothing down to and
past the Planck scale.

---

## 16. The essential insight

Strip away the algebra and one idea remains.

A moving observer's measurement of the speed of light is **not** a
measurement of how fast light goes relative to them. It is the
ratio of two quantities, both of which are distorted by their
motion through the lattice, in a proportion that happens to be
exactly the distortion in the light's transit time.

Light really does take γ² longer to cross a moving rod and come
back. The rod really is shorter by γ. The clock really is slower
by γ. Nothing in the laboratory is undistorted, so nothing in the
laboratory can see the distortion — and the number that comes out
is c.

The lattice frame exists. It is simply that every instrument built
to find it is made of the same stuff that hides it.

What makes this a research program rather than a story is that the
required distortions are *specific numbers*, not a vague
conspiracy: 1/γ longitudinal, 1 transverse, 1/γ on clocks, the
same γ for everything. A lattice either produces those or it does
not, and the question is settled by computation rather than by
argument.

---

## What's next

The computational tests named in §15 are tracked in
[grid/sim-lorentz/](../grid/sim-lorentz/).

Related background: [metric.md](metric.md) for the geometric view
of the same structure, [kaluza-klein.md](kaluza-klein.md) for
compact dimensions and how they produce mass,
[bloch-band-structure.md](bloch-band-structure.md) for how
dispersion relations on a lattice are computed, and
[grid/foundations.md](../grid/foundations.md) for the axioms —
especially A1 (lattice and tick) and A2 (the single causal
dimension), which this primer leans on throughout.
