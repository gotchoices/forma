# Q144. Euclidean vs. Lorentzian orthogonality in the (x, compact) plane

**Status:** Answered — the two constructions give **reciprocal**
answers, γ² apart, with opposite-sign time offsets. Which one is
physical is decided entirely by the metric signature, so length
contraction cannot be read off path geometry. A concrete instance
of [Q76](Q76-origin-of-metric-signature.md): the signature is not
a convention, and here is a case where it changes a number.
**Related:**
  [Q76](Q76-origin-of-metric-signature.md) (origin of metric signature — this is a worked instance),
  [Q138](Q138-time-as-peer-dimension-or-bookkeeping-balance.md) (time as peer dimension vs. bookkeeping balance),
  [Q142](Q142-absolute-lattice-frame-vs-relativity.md) (why contraction is required at all),
  [Q117](Q117-relativistic-effects-from-velocity-partition.md) (the velocity-partition triangle),
  [`primers/relativity-on-a-lattice.md`](../primers/relativity-on-a-lattice.md) §9–§11,
  [`grid/foundations.md`](../grid/foundations.md) (A2 — one timelike dimension)

---

## 1. The question

A particle in forma is a mode winding a compact direction. Picture
the compact direction as the circumference of a cylinder and
ordinary space x as its length. At rest, the particle circles the
tube. In motion along x, it traces a **helix**.

Two particles a distance d apart along x are a measuring rod. At
rest their paths are two circles separated by d. In motion they are
two helices. As the motion gets faster the helices stretch out, and
the *nearest* distance between them — the perpendicular, now
slanted off the x-axis — shrinks. In the limit v → c the helices
unwind into lines and appear to touch.

This is an attractive construction. It gets a γ out of pure
geometry, it is easy to picture, and it seems to deliver length
contraction from the same figure that delivers time dilation.
**Does it?**

## 2. The calculation, which is correct

Unroll the cylinder into a flat strip: x one way, arc length around
the compact direction the other. Each helix becomes a straight line
at angle α from the x-axis, with

> cos α = v/c,  and therefore  sin α = 1/γ

Two particles offset by d along x trace two **parallel** lines. The
perpendicular distance between parallel lines offset by d along one
axis is d·sin α:

> perpendicular distance = d · sin α = **d / γ**

The factor is exactly right. Checked numerically: at v = 0.6c the
construction gives 0.800000 for d = 1 against d/γ = 0.800000; at
v = 0.99c, 0.141067 against 0.141067.

So the arithmetic is not in question. What is in question is
whether the quantity computed is a *length*.

## 3. Two reasons it is not a length

**The separation along x never changes.** Parametrise the paths:
particle 1 at (vt, v_c t), particle 2 at (d + vt, v_c t + offset).
The x-separation is d at every instant, at every velocity, forever.
Stretching the helices does not draw them together — it unwinds
them into *parallel* lines, not the same line. The apparent
touching at v → c is the two lines becoming parallel to each other
and to the x-axis, not coincident.

**The perpendicular connects two different times.** Dropping the
perpendicular from particle 1's position onto particle 2's path
lands on a point that particle 2 occupies at time −vd/c², not at
the same moment. The perpendicular distance is the distance between
two **events separated in time**. A length is a separation measured
at *one* moment.

That second objection is the one that generalises, and it points at
the real issue.

## 4. The signature trap

Projecting onto the slice perpendicular to a worldline is the right
*idea* — it is how relativity defines a moving object's rest
length. But "perpendicular" has to be defined by the right
geometry.

The unrolled (x, compact) strip is a plane of two **spatial**
directions. Perpendicularity there is ordinary Euclidean
perpendicularity: the one that makes the dot product vanish with
all plus signs. Relativity's simultaneity slices are defined by the
**spacetime** metric, which carries a minus sign on the time
component. The two prescriptions give different answers — and not
slightly different:

| | Euclidean perpendicular | Minkowski-orthogonal slice |
|---|---|---|
| time offset of the landing point | −vd/c² | +γ²·vd/c² |
| resulting separation | **d/γ** | **γd** |

The answers are **reciprocal**. At v = 0.9c that is 0.436 against
2.294 — a factor of γ² = 5.3 apart, with opposite signs on the
offset.

The factor γ appears in both because both descend from the same
right triangle. **Which side of the fraction it lands on is decided
entirely by whether the hypotenuse relation carries a plus or a
minus.** That is the whole content of "signature," made numerical.

### This failure mode has a literature

The picture in which *everything moves at speed c through a
four-dimensional Euclidean space*, with ordinary motion being a
rotation of that velocity vector out of the time axis, reproduces
γ-factors in form and is appealing enough to be rediscovered
regularly — sometimes under the name "Euclidean relativity." It
diverges from special relativity on velocity addition and on the
invariant interval, for exactly the reason tabulated above.

Note that [Q117](Q117-relativistic-effects-from-velocity-partition.md)
§4 uses the same triangle: c² = v²_Ma + v²_S, with E² = (mc²)² +
(pc)² read off as a Pythagorean relation. That is a legitimate
reading of a *correct* relativistic identity, but it is worth
flagging that the triangle on its own does not know which signature
it belongs to; the physics is in the assignment, not the figure.

## 5. Which one is physical in GRID

In GRID the (x, compact) plane really is Euclidean, and this is not
a free choice:

- **Time in GRID is the tick.** Axiom A2 of
  [`grid/foundations.md`](../grid/foundations.md) gives the lattice
  exactly one timelike dimension, carrying the causal ordering.
  The compact direction is not it.
- **The compact direction is spatial** — a large number of cells
  wrapped into a closed surface.
- **The measured dispersion confirms it.** The Kaluza–Klein
  relation that falls out of the lattice is

> ω² = c²k_x² + ω₀²

  in which the compact-direction momentum enters on the **mass**
  side with a **plus** sign. A plus sign there is the signature of
  a spatial direction. A timelike compact direction would enter
  with a minus and give a tachyonic branch.

So the helix construction is doing correct Euclidean geometry in a
genuinely Euclidean plane. It computes a real quantity. That
quantity is simply not the rest length of a moving rod.

## 6. Why the clock argument survives and the ruler argument does not

This is the useful asymmetry, and it is worth stating because the
two arguments look like one argument.

Time dilation **does** come out of path geometry, and legitimately.
A particle's own clock rate is the rate at which it circulates the
compact direction. Its total speed through the lattice is capped at
c, so travelling in x leaves less speed for circulating, by exactly
the Pythagorean budget. That is a property of a **single path**,
and a single path is a geometric object.

A length is a property of the **relationship between two paths** at
a chosen moment. "At a chosen moment" is where the signature
enters, because choosing a moment for a moving object means
choosing a simultaneity slice. Geometry of the paths alone cannot
supply it.

> Dilation is kinematics of one worldline. Contraction is a
> statement about two worldlines plus a slicing — and the slicing
> is dynamics, not geometry.

Where contraction *does* come from in forma is round-trip
resonance: a bound state is a standing wave whose round-trip phase
must close, and when the medium's effective propagation becomes
directional under motion, the length that closes the loop is
shorter by γ. How an extended object *gets* to that length under
acceleration is Born rigidity. Both are developed in
[`primers/relativity-on-a-lattice.md`](../primers/relativity-on-a-lattice.md)
§11, and the result is now measured in
[`grid/sim-lorentz/F3`](../grid/sim-lorentz/F3-contraction-and-coasting.md)
at 1/γ to within 0.1% for v ≤ 0.8c.

## 7. What this contributes to Q76

[Q76](Q76-origin-of-metric-signature.md) asks what makes time
temporal — why the metric carries a minus sign on one component
rather than being positive-definite. It is marked open, and this
entry does not close it.

What it contributes is a **concrete, numerical instance** of the
signature doing physical work. It is sometimes tempting to treat
the minus sign as bookkeeping — a convention for separating the
dimension we happen to call time, with no consequence that a
careful Euclidean account could not reproduce. (That temptation is
precisely Reading B of
[Q138](Q138-time-as-peer-dimension-or-bookkeeping-balance.md).)

Here the sign changes an answer from d/γ to γd. Any account that
derives the signature rather than assuming it has to explain why
the physical slicing is the one with the minus sign, in a model
where the plane in question is manifestly spatial on both axes.
That is a sharper target than the general question.

---

*Appeal classification: §2 and §4 are geometry, checkable by hand
and confirmed numerically. The literature note in §4 and the
definition of the Minkowski-orthogonal slice are **standard
physics**. §5 is **GRID-specific** (A2, the measured dispersion).
§6 and §7 are framework-level readings.*

*Connects to: Q76 (signature), Q138 (peer dimension vs.
bookkeeping), Q142 (why contraction is required), Q117 (the same
triangle), primers/relativity-on-a-lattice.md §9–§11,
grid/sim-lorentz/F3*
