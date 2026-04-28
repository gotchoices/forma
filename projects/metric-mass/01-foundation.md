# Chapter 1 — Foundation

This chapter establishes the *manifold*, *metric*, and *field* on
which the rest of the project rests. It is the only chapter where
we **assume** things; every later chapter must derive its claims
from what is stated here.

---

## Concepts introduced in this chapter

The chapter introduces the following ideas in order. They are listed
here so you know what's coming.

| § | Concept | Brief description |
|---|---------|-------------------|
| 1 | Manifold | An abstract space we can put coordinates on |
| 2 | Real numbers ℝ and the circle S¹ | The two "shapes" our coordinates will live on |
| 3 | The cylinder M = ℝ × ℝ × S¹ | Our three-coordinate manifold |
| 4 | Metric (refresher) | The recipe for converting coordinate-differences into distance |
| 5 | The bare metric | The starting metric for this project |
| 6 | Off-diagonal terms — an open question | Whether cross-terms must be zero or not |
| 7 | Units choice | Why we keep ℏ and c explicit (SI-like) |
| 8 | Scalar field | What φ is and what notation describes it |
| 9 | Wave equation and the d'Alembertian □ | The equation φ obeys |
| 10 | Periodicity in u | What single-valuedness on a circle means |
| 11 | Light-in-1D question | Why our 1D extended space isn't a problem |
| 12 | Explicit non-assumptions | What we are NOT allowing ourselves to assume |
| 13 | Summary of givens | The five items the rest of the project rests on |

---

## 1. What is a manifold?

A **manifold** is an abstract space we can put coordinates on. The
word sounds technical, but the intuition is mundane: it's any space
where you can label points with numbers and the labels vary smoothly
as you move around.

Familiar examples:

- A flat sheet of paper is a 2D manifold. Coordinates: (x, y).
- The surface of a sphere is a 2D manifold. Coordinates:
  (latitude, longitude).
- 3D space is a 3D manifold. Coordinates: (x, y, z).
- 4D spacetime is a 4D manifold. Coordinates: (t, x, y, z).

A manifold can be flat (paper, 3D space) or curved (sphere, the
spacetime around a star). It can be infinite (paper extending
forever) or finite (sphere). It can have multiple "shapes" combined.

For this project we will use the symbol **M** to refer to the
particular manifold we work on. Whenever you see "M" in the math,
it just means "the manifold we set up in §3."

---

## 2. The shapes ℝ and S¹

We need two basic shapes to build M.

**The real number line, ℝ.** This is the symbol for "all real
numbers from −∞ to +∞." If a coordinate lives in ℝ, it can take any
real value — no boundaries, no wraparound. Time is like this:
t = 5 seconds and t = 1000 seconds are different moments. Distance
along an infinite axis is like this too.

When we write `t ∈ ℝ`, we read it as *"t is an element of ℝ"* —
i.e., t is allowed to be any real number.

<!--EC Is S^1 going to be confused with our space dimension S?  Maybe S^1 is conventional enough that we should stick with it anyway? >
**The circle, S¹.** This is the symbol for "a one-dimensional
circle." (The "S" is for *sphere*; the superscript "1" indicates one
dimension, so S¹ is a 1-sphere = an ordinary circle. S² would be a
2-sphere = the surface of a ball.) A coordinate on S¹ lives on a
loop: you can move around it, but if you move far enough you come
back to where you started.

Think of an angle θ on a clock face: θ = 0° and θ = 360° are the
same position, even though the numbers are different. The clock's
angular position is on S¹.

**Why these matter for our project.** Time and one direction of
space are unbounded → ℝ. The mass-generating compact dimension u is
a circle of finite circumference → S¹.

---

## 3. The manifold M = ℝ × ℝ × S¹

Now we combine the shapes. The symbol "×" between two shapes means
*Cartesian product* — we list one coordinate from each shape and
treat the result as a single point.

- ℝ × ℝ is a flat 2D plane: every point has an (x, y) pair where
  both x and y can be any real number.
  <!--EC Seems confusing.  Our 2 R's are S and t, yes?  Which axis will we project time into, z?  So we will be looking at Space in x and time in t?.  Just seems a bit of a diversion introducing R, R, S1 when what we're really talking about is t, S, u.  Push back if you disagree.  Maybe what you're saying is these are descriptions of the domain for each of our variables.>
- ℝ × S¹ is an *infinite cylinder*: one direction extends forever
  (the ℝ part), the other wraps around (the S¹ part). Imagine a
  drinking straw that keeps going in one direction.
- ℝ × ℝ × S¹ is what we want: an *infinite cylinder of
  3-dimensions worth of points*. Two of the directions extend
  forever, the third wraps. We can also picture this as "an
  infinite plane, but every point has a tiny circular dimension
  attached to it."

Our manifold is M = ℝ × ℝ × S¹, and our three coordinates are:

| Coordinate | Symbol | Range | Shape |
|---|---|---|---|
| Time | t | t ∈ ℝ | Real line, no wraparound |
| Spatial extension | S | S ∈ ℝ | Real line, no wraparound |
| Compact (mass-generating) | u | u ∈ [0, L_u) | Circle of circumference L_u |

The notation `u ∈ [0, L_u)` means u runs from 0 (inclusive) to L_u
(exclusive) — i.e., u takes values 0, 0.001, ..., almost-L_u, and
then the next step wraps back to 0. The length L_u is the
circumference of the compact direction; it has units of length and
its numerical value is left symbolic for now.

**Why these and not others.** This is the smallest manifold on
which mass-from-compactification can be derived:

- *Time* is needed to talk about anything dynamic.
- *One extended spatial dimension S* is needed for a wave to
  propagate "somewhere" we can call "space."
- *One compact dimension u* is needed for the momentum
  quantization that produces mass (next chapter).


**Note on visualization.** When we render M to a screen later, we
embed (t, S, u) as Cartesian (x = S, y = u, z = t). The Cartesian
display axes (x, y, z) carry no metric meaning — they are just
where on the screen each coordinate goes.

---

## 4. The metric (a refresher)
<!--EC Let's do this:
- Strip metric intro from this project
- Create a file primers/metric.md that pulls all the info from the primers/kaluza-klein.md file but goes into a little more depth and is a bit more gentle and explanatory.
- Then we strip metric intro from kaluza-klien primer and just refer to it
- Kaluza-klein primer can now be a little more thorough on actual kk material
- This file can refer to both primers where applicable
>
A **metric** is a recipe that converts coordinate-differences into
actual physical distance. (We covered this in detail in
[primers/kaluza-klein.md](../../primers/kaluza-klein.md) §1–§3, and
in the conversation that led into this chapter.)

In a 2D Cartesian plane, the metric recipe is just the Pythagorean
theorem: ds² = dx² + dy². In polar coordinates the recipe changes
shape: ds² = dr² + r² dθ², because dθ is an angle (dimensionless)
and the *arc length* it represents depends on how far out you are.

The metric is conventionally written as a symmetric matrix g_μν.
Plugging a step (dx¹, dx², ...) into the recipe is done by
sandwiching:

<!-- ds² = sum over μ,ν of g_μν dx^μ dx^ν -->
$$
ds^2 = \sum_{\mu,\nu}\, g_{\mu\nu}\, dx^\mu\, dx^\nu
$$

For a 3-coordinate manifold like ours, μ and ν each run over the
three coordinates {t, S, u}. The matrix is 3×3 and the sum has 9
terms (though if g is diagonal, only 3 of them are nonzero).

The metric matrix is allowed to depend on position — that's what
made polar's `r²` entry a function of r. We will keep open the
possibility that our metric components are functions of (t, S, u),
even if for this chapter we start with a constant choice.

---

## 5. The bare metric

The starting metric for this project is the simplest possible
Lorentzian metric on M:

<!-- ds² = -c² dt² + dS² + du² -->
$$
ds^2 = -c^2\,dt^2 + dS^2 + du^2
$$

Or in matrix form, with coordinate ordering (t, S, u):

<!-- g = diag(-c², 1, 1) -->
$$
g_{\mu\nu} = \begin{pmatrix} -c^2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

Reading the matrix:

- **g_tt = −c².** The diagonal entry for time. The negative sign is
  what distinguishes time from space (Lorentzian signature, see
  [kaluza-klein.md §1](../../primers/kaluza-klein.md)). The c² is
  there because we measure time in seconds and space in meters; the
  c² is the conversion factor that makes the units match in ds².
- **g_SS = 1.** The diagonal entry for the extended spatial
  direction. Just the ordinary Euclidean weight.
- **g_uu = 1.** The diagonal entry for the compact direction. Same
  Euclidean weight as g_SS.

The metric is **Lorentzian** (one negative eigenvalue → light cone
exists), **flat** (does not depend on position → no curvature), and
in this initial form **purely diagonal**.

---

## 6. Off-diagonal terms — an open question

This is the central question of the project, so it deserves its own
section.

In standard Kaluza-Klein, off-diagonal entries of the metric
(g_μ5, the entries that mix a 4D direction with the compact 5th
direction) are exactly the electromagnetic potential A_μ. So
off-diagonals encode "fields living on the manifold."

A reasonable question, and the one this project asks:

> When we put just light (no mass, no gravity, no charge) on the
> manifold M, **do we expect off-diagonal entries of the metric to
> remain zero, or does something force them to develop?**

Three possibilities to keep in mind:

1. **They stay zero.** Light alone doesn't source any field that
   couples to off-diagonals. The diagonal metric is consistent
   with itself. Mass appears purely from the boundary condition
   on u, and the metric never deforms.

2. **Some develop.** The wave equation on M has solutions with
   structure that *requires* the metric to develop position-
   dependence — for example, g_uu becoming a function of S (the
   "dilaton-style" possibility you raised: gravity in S emerging
   from geometry of u). This would be an off-diagonal-adjacent
   effect, or in some setups an actual cross term.

3. **All of them develop.** The light field is rich enough to
   source A_μ-like cross-terms even without charge. (Standard KK
   suggests this is *not* what happens for neutral fields, but
   we should verify on our specific manifold rather than assume.)

We do **not** prejudge between these. The starting metric
(§5 above) is the simplest possible — diagonal, constant — and it
is what we will use *as a starting point*. Whether the math forces
us off this starting point is what later chapters will determine.

So the bullet from earlier drafts that said "no off-diagonal
entries — period" should be read instead as: **no off-diagonals
*to begin with*; the question of whether any will be required is
exactly what this project is investigating.**

---

## 7. Units: SI-like, with c and ℏ explicit

We have a choice to make about units.

**Option A: Natural units.** Set c = 1 and ℏ = 1. Common in
particle physics and general relativity literature. Pro: equations
are very clean (e.g., E² = p² + m²). Con: easy to lose track of
where each constant entered, because they're invisible.

**Option B: Keep c and ℏ explicit (SI-like).** Time in seconds,
distance in meters, mass in kilograms. Pro: every formula
dimensionally checks; you can see exactly where each constant
enters. Con: more notation.

**Choice for this project: Option B.** We keep c and ℏ explicit
because the project is pedagogical. Seeing where c² enters the
metric (in g_tt) and where ℏ enters (only at the moment we identify
p = ℏk) is part of the intuition we are trying to build. We will
note when natural units would clean an expression up, but we will
not adopt them.

---

## 8. The wave field (light)

We assume the existence of a single **real scalar field** on M,
which we call φ.

Two pieces of vocabulary:

**Real-valued.** φ at any point of M is a single real number — a
single value with no direction, no magnitude+phase pair, no
multiple components. Compare:

- A *real scalar field* assigns a real number to each point: e.g.,
  the temperature in a room.
- A *vector field* assigns a vector to each point: e.g., the wind
  velocity in a room (each point has a direction and speed).
- A *tensor field* assigns a more elaborate object: e.g., the
  metric is a tensor field that assigns a 3×3 matrix to each point.

We are using the simplest of the three because it is sufficient to
derive mass-from-compactification. Adding spin and polarization
(which require vector or tensor fields) is a generalization that
does not change this project's argument.

**The notation φ : M → ℝ.** We write:

<!-- φ : M → ℝ -->
$$
\varphi : M \to \mathbb{R}
$$

This is shorthand for *"φ is a function whose input is a point on
M and whose output is a real number."* Read aloud: "phi is a map
from M to ℝ." It is a compact way of saying "for each (t, S, u),
there is a number φ(t, S, u)."

So φ is the project's stand-in for "light" — a propagating
disturbance whose value at every spacetime point is a real number.

---

## 9. The wave equation

φ obeys the **massless wave equation**:

<!-- □φ = 0 -->
$$
\Box\varphi = 0
$$
<!--EC I think you're saying that our wave is light-like (language that should be in our metric primer perhaps.  Should we have an introduction to the light cone in that primer so we understand that this equality means the property lives on the edge of the light cone?  If we do a good job in the primer, which will be a prequisite to this file, we can be more brief here.  I think we're just saying that ds = 0, correct? (in primer language))>
Three pieces of notation to unpack here.

**The d'Alembertian, □.** This is the operator that appears in the
wave equation in any number of dimensions. For 3+1D Cartesian
spacetime:

<!-- □ = -(1/c²)∂²/∂t² + ∂²/∂x² + ∂²/∂y² + ∂²/∂z² -->
$$
\Box = -\frac{1}{c^2}\frac{\partial^2}{\partial t^2} + \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}
$$

It's the spacetime version of the Laplacian (the operator that
gives wave-like dynamics). When □φ = 0, φ is a wave that propagates
at speed c.

**General form using the metric.** For an arbitrary metric, the
d'Alembertian is built from the inverse metric and the partial
derivatives:

<!-- □φ = sum over μ,ν of g^μν ∂_μ ∂_ν φ -->
$$
\Box\varphi = \sum_{\mu,\nu}\, g^{\mu\nu}\, \partial_\mu \partial_\nu\, \varphi
$$

Three notations to unpack:

- **∂_μ φ** means *"the partial derivative of φ with respect to
  the μ-th coordinate."* If μ = t, then ∂_μ = ∂/∂t. If μ = S,
  then ∂_μ = ∂/∂S. The lower index μ is just labeling which
  coordinate we differentiate by.
- **g^μν** (raised indices) is the **inverse** of the metric
  matrix g_μν (lowered indices). For the bare diagonal metric of
  §5, the inverse is also diagonal: g^tt = −1/c², g^SS = 1,
  g^uu = 1. Inverting a diagonal matrix is just inverting each
  diagonal entry.
- **The sum over μ, ν** runs over all coordinates. For our 3D
  manifold, μ and ν each take values in {t, S, u}, so there are
  3 × 3 = 9 terms in the sum. (If g is diagonal, only 3 of those
  are nonzero — the ones where μ = ν.)

(If you have seen "Einstein summation convention" — the rule that
repeated indices are implicitly summed — that is what is going on.
We are writing the sum out explicitly here for clarity. In later
chapters we may drop the explicit Σ and let repeated indices
indicate the sum.)

**Putting it together.** Plugging our diagonal bare metric into the
general form gives the explicit wave equation we will work with:

<!-- (-1/c²)∂²φ/∂t² + ∂²φ/∂S² + ∂²φ/∂u² = 0 -->
$$
-\frac{1}{c^2}\frac{\partial^2\varphi}{\partial t^2}
+ \frac{\partial^2\varphi}{\partial S^2}
+ \frac{\partial^2\varphi}{\partial u^2}
= 0
$$

Each term has a clear meaning:

- The first term is the time curvature of φ (how fast its
  oscillation is changing in time).
- The second is the spatial curvature in S.
- The third is the spatial curvature in u.

The equation says: when you add these three contributions up
(with the appropriate signs from the metric), you get zero. That is
what it means for φ to be a free wave on M.

---

## 10. Periodicity in u

Because u is a circle (S¹), the field φ must be **single-valued**:
moving around the compact direction by L_u and coming back to
"where you started" must give the same value.

<!-- φ(t, S, u + L_u) = φ(t, S, u) -->
$$
\varphi(t, S, u + L_u) = \varphi(t, S, u)
$$

Read this as: *"if you increase u by one full circumference,
the value of φ doesn't change — because that's the same point."*

This is a **boundary condition**, not a separate equation. It
restricts which solutions of the wave equation are allowed. A
solution that increases or decreases as you go once around u
would be multi-valued and is therefore not allowed.

This boundary condition is the entire reason mass will appear in
the next chapter. Without it, u would just be a third infinite
direction and the spectrum of solutions would be a continuous
3-parameter family (k_t, k_S, k_u). With it, the third parameter
becomes discrete: only certain integer-related values of k_u are
allowed. That discrete set will turn out to be the mass spectrum.

---

## 11. The light-in-1D question

Question (raised at the project's framing): *we say light travels
in a single linear dimension, but light should be able to travel in
any direction. Is restricting S to 1D a problem?*

Answer: **no.**

**Light is intrinsically 1D.** A wave with a definite wave-vector k
propagates along *one* direction — the direction of k — regardless
of how many extended dimensions exist. In 3D space a beam of light
still travels along a line; the other two spatial directions provide
*polarization* and *transverse spread*, not propagation freedom.

**What 1D-S costs.** With only one extended spatial direction:

- No transverse polarization. In 3D, E and B are perpendicular to
  the propagation direction; with only one direction perpendicular
  to t, polarization collapses.
- No magnetic field in the conventional sense (B requires a
  perpendicular spatial dimension to "swirl" through).
- No spreading or refraction in a transverse direction.

**What 1D-S preserves.**

- Wave propagation at speed c.
- Constructive and destructive interference along S.
- The full dispersion relation we will derive in chapter 2.
- Standing waves in u, regardless of what S looks like.
- Quantization on the compact direction.

For the mass-derivation argument, none of the lost features matter.
The argument depends only on momentum quantization in u, which
works in any number of extended dimensions (including zero).

**Two complementary modes of motion.** φ can have:

- **Linear propagation along S.** A wave with definite k_S and no
  variation in u is "ordinary light traveling along S." This is
  the everyday picture of light.
- **Closed propagation around u.** A wave with no S-variation but
  non-trivial u-dependence circulates around the compact direction
  and (by single-valuedness) can only do so in integer multiples
  of 2π/L_u. This is the *winding mode*.

These are not different physical fields — they are different
*solutions* of the same wave equation. The standing-wave-in-u
picture and the linear-propagation-in-S picture are two faces of
the same φ, distinguished only by their k-content.

So: light can travel in any of the available directions, including
u. When it travels purely along u and closes on itself, what we
will see in the next chapter is that this configuration carries
energy at rest — and that energy is mass.

---

## 12. Explicit non-assumptions

The following are *not* given. They are to be derived (or shown to
arise from the givens), or stay out of scope for this project.

- **Mass.** No object on M has been assigned a mass. The wave
  equation is the massless one. If something with rest energy
  emerges, it must come from φ-configurations and the topology
  of u — not from a mass term inserted by hand.

- **Particles.** No discrete entities are postulated. φ is a
  continuous field. Anything resembling a particle must arise as a
  localized or topologically-distinguished configuration of φ.

- **Quantum mechanics.** The wave equation is classical. We will
  invoke quantization-of-momentum at the periodicity boundary
  condition (§10) but otherwise treat φ classically. ℏ enters
  only at the step of identifying p = ℏk for a wave of
  wavenumber k.

- **Gravity.** Einstein's equations are not in play. The metric is
  fixed by us; it is not sourced by anything. (In 1+1D vacuum,
  Einstein's equations are trivial anyway — see future chapters
  if/when we need to discuss this.)

- **Charge.** No second compact dimension is present. There is no
  electromagnetic field, no Lorentz force, no g_μ5-style cross-
  terms in the Kaluza-Klein sense. Charge is the subject of a
  future project, not this one.

- **Off-diagonal metric components.** The bare metric (§5) is
  diagonal as a *starting* condition. Whether the math will force
  any cross-term to develop is the open question of §6, which
  later chapters will examine. We are not assuming the
  off-diagonals stay zero forever; we are starting them at zero
  and watching what happens.

---

## 13. Summary of givens

We have, in total:

1. A manifold M = ℝ × ℝ × S¹ with coordinates (t, S, u) and
   compact circumference L_u.
2. A starting metric ds² = −c² dt² + dS² + du², diagonal and
   constant. (Subject to revision if later chapters force changes.)
3. A real scalar field φ : M → ℝ.
4. The massless wave equation □φ = 0.
5. Periodicity of φ in u: φ(t, S, u + L_u) = φ(t, S, u).

Plus the methodological commitments:

- Units are kept SI-like: c and ℏ remain explicit symbols.
- Off-diagonals of the metric are *open* — they start at zero, and
  whether they need to stay zero is what the project is asking.

That is the entire content of this chapter. Everything else in the
project must be derived from these five items and the
methodological commitments.

---

## What's next

[Chapter 2](02-mass-from-u.md) — Solve the wave equation on M.
Find the dispersion relation. Identify the n=0 modes as massless
S-propagation, the n≠0 modes as carrying rest energy, and read off
the mass spectrum. Examine whether the bare diagonal metric
remains consistent with the solutions, or whether it has to be
revised.
