# Chapter 1 — Foundation

This chapter establishes the *manifold*, *metric*, and *field* on
which the rest of the project rests. It is the only chapter where
we **assume** things; every later chapter must derive its claims
from what is stated here.

**Prerequisite:** [primers/metric.md](../../primers/metric.md). The
metric primer covers the general machinery — the metric as a
distance recipe, position-dependent metric components, off-diagonal
terms, light cones, the d'Alembertian, and compact dimensions. This
chapter assumes you have read it (or can refer back to it as needed)
and concentrates on *applying* that machinery to the specific
minimal setup of this project.

The chapter is paced deliberately slowly — once a concept is
defined here, it is used as-is throughout the rest of the project.
If you are fluent with differential geometry, parts will feel
basic. That is intentional.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | Our coordinates: t, S, u and their domains |
| 2 | The bare metric: ds² = −c² dt² + dS² + du² |
| 3 | Off-diagonal terms — the open question |
| 4 | Units choice (SI-like) |
| 5 | The wave field φ |
| 6 | The wave equation on our manifold |
| 7 | Periodicity in u |
| 8 | The light-in-1D question |
| 9 | Explicit non-assumptions |
| 10 | Summary of givens |

---

## 1. Our coordinates

We work with three coordinates: **t**, **S**, and **u**. Each one's
domain (the set of values it can take) is given below.

| Coordinate | Symbol | Domain | What this means |
|---|---|---|---|
| Time | t | All real numbers | t can be any real value, no wraparound |
| Spatial extension | S | All real numbers | S can be any real value, no wraparound |
| Compact (mass-generating) | u | u ∈ [0, L_u), wraps | u runs from 0 up to L_u, then wraps back to 0 |

The length L_u is the circumference of the compact direction. It
has units of length and we leave its numerical value symbolic for
now.

**A note on notation.** In differential-geometry shorthand, this
combination of domains is written

$$
M = \mathbb{R} \times \mathbb{R} \times S^1
$$

which just packages the three domains together: ℝ ("real number
line") for t, ℝ for S, and S¹ ("the 1-sphere," math name for an
ordinary circle) for u. We will call the manifold **M**, but the
formal product notation is just shorthand for the table above.
Don't worry if it looks abstract — the substance is the table.

(Heads-up: **S** is our coordinate for spatial extension; **S¹** is
the math symbol for "circle." The superscript ¹ is the only thing
distinguishing them in print. They are different things.)

**Why these three and not others.** This is the smallest set of
coordinates on which mass-from-compactification can be derived:

- *Time* is needed to talk about anything dynamic.
- *One extended spatial dimension S* is needed for a wave to
  propagate "somewhere" we can call "space."
- *One compact dimension u* is needed for the momentum
  quantization that produces mass (next chapter).

Adding more extended dimensions, more compact dimensions, or more
elaborate topology will be deferred to later chapters or other
projects.

**Note on visualization.** When we render M to a screen later, we
embed (t, S, u) as Cartesian (x = S, y = u, z = t). The Cartesian
display axes (x, y, z) carry no metric meaning — they are just
where on the screen each coordinate goes.

---

## 2. The bare metric

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

(For what a metric is and why we write it this way, see
[metric.md §1–§4](../../primers/metric.md).)

Reading the matrix:

- **g_tt = −c².** The diagonal entry for time. The negative sign
  is what distinguishes time from space (Lorentzian signature; see
  [metric.md §7](../../primers/metric.md)). The c² is there because
  we measure time in seconds and space in meters; the c² is the
  conversion factor that makes the units of ds² come out as
  length².
- **g_SS = 1.** Ordinary Euclidean weight for the extended spatial
  direction.
- **g_uu = 1.** Same Euclidean weight for the compact direction.
  The only thing that distinguishes u from S in the metric is the
  fact that u is compact (i.e., the manifold's topology), not the
  metric weight.

Three properties of this metric to keep in mind:

- **Lorentzian.** One negative eigenvalue (time entry) → light cone
  exists at every point.
  See [metric.md §8](../../primers/metric.md).
- **Flat.** g_μν does not depend on t, S, or u → no curvature
  anywhere.
- **Diagonal.** No cross-terms between coordinates *as a starting
  condition* — see §3 for why this is open.

---

## 3. Off-diagonal terms — an open question

This is a central question of the project, so it deserves its own
section.

In standard Kaluza-Klein, off-diagonal entries of the metric
(g_μ5, the entries that mix a 4D spacetime direction with the
compact 5th direction) are exactly the electromagnetic potential
A_μ. So off-diagonals encode "fields living on the manifold." See
[metric.md §6](../../primers/metric.md) and
[kaluza-klein.md](../../primers/kaluza-klein.md).

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
   structure that *requires* the metric to develop position
   dependence — for example, g_uu becoming a function of S (the
   "dilaton-style" possibility: gravity in S emerging from
   geometry of u). This would be an off-diagonal-adjacent effect,
   or in some setups an actual cross term.

3. **All of them develop.** The light field is rich enough to
   source A_μ-like cross-terms even without charge. (Standard KK
   suggests this is *not* what happens for neutral fields, but we
   should verify on our specific manifold rather than assume.)

We do **not** prejudge between these. The starting metric (§2) is
the simplest possible — diagonal, constant — and it is what we will
use *as a starting point*. Whether the math forces us off this
starting point is what later chapters will determine.

So when §2 lists "diagonal" as a property of the bare metric, read
that as **diagonal *to begin with*; the question of whether any
cross-terms will be required is exactly what this project is
investigating.**

---

## 4. Units: SI-like, with c and ℏ explicit

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

(See [primers/natural-units-and-alpha.md](../../primers/natural-units-and-alpha.md)
for a deeper discussion of natural-units conventions in physics.)

---

## 5. The wave field (light)

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
  metric is a tensor field that assigns a 3×3 matrix to each
  point.

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

## 6. The wave equation

φ obeys the **massless wave equation**:

<!-- □φ = 0 -->
$$
\Box\varphi = 0
$$

This says, in the language of the metric primer, that φ is a
**light-like field** — its disturbances propagate on light-like
paths (ds² = 0). See
[metric.md §11](../../primers/metric.md) for the d'Alembertian □
and its general form, and [§8](../../primers/metric.md) for the
light-cone classification of intervals.

Plugging our specific bare metric (§2) into the general form
g^μν ∂_μ ∂_ν φ = 0 gives the explicit wave equation we will work
with:

<!-- (-1/c²)∂²φ/∂t² + ∂²φ/∂S² + ∂²φ/∂u² = 0 -->
$$
-\frac{1}{c^2}\frac{\partial^2\varphi}{\partial t^2}
+ \frac{\partial^2\varphi}{\partial S^2}
+ \frac{\partial^2\varphi}{\partial u^2}
= 0
$$

Each term has a clear meaning:

- The first term is the second time-derivative of φ (how fast its
  oscillation is changing in time), with the −1/c² factor coming
  from g^tt.
- The second is the second derivative of φ along S.
- The third is the second derivative of φ along u.

The equation says: when you add these three contributions up
(with the appropriate signs from the inverse metric), you get
zero. That is what it means for φ to be a free (massless) wave on
our manifold.

---

## 7. Periodicity in u

Because u is compact, the field φ must be **single-valued** on the
compact direction: moving around by L_u and coming back to "where
you started" must give the same value.

<!-- φ(t, S, u + L_u) = φ(t, S, u) -->
$$
\varphi(t, S, u + L_u) = \varphi(t, S, u)
$$

Read this as: *"if you increase u by one full circumference, the
value of φ doesn't change — because that's the same point."*

This is a **boundary condition**, not a separate equation. It
restricts which solutions of the wave equation are allowed. A
solution that increased or decreased as you went once around u
would be multi-valued and is therefore not allowed.

This boundary condition is the entire reason mass will appear in
the next chapter. Without it, u would just be a third infinite
direction and the spectrum of solutions would be a continuous
3-parameter family (k_t, k_S, k_u). With it, the third parameter
becomes discrete: only certain integer-related values of k_u are
allowed. That discrete set will turn out to be the mass spectrum.

---

## 8. The light-in-1D question

Question (raised at the project's framing): *we say light travels
in a single linear dimension, but light should be able to travel in
any direction. Is restricting S to 1D a problem?*

Answer: **no.**

**Why "light in 1D" is fine.** Light, as a wave, is not intrinsically
1D — in 3D space a light wave is a genuinely 3D object, with field
values defined throughout space, transverse polarization, and the
ability to spread or focus. The "1D" picture is a feature of the
particle/photon model (a quantum of light traveling along its
wave-vector), not of the wave itself.

The real reason 1D-S works for us is simpler: **we have chosen a
manifold with only one extended spatial dimension**. The wave
equation □φ = 0 makes sense in any number of dimensions — 1, 2, 3,
or more — so a "light-like wave" can live in our 1D-S setup
without contradiction. We just have less space than reality
provides, and the wave fits whatever space we give it.

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

## 9. Explicit non-assumptions

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
  condition (§7) but otherwise treat φ classically. ℏ enters
  only at the step of identifying p = ℏk for a wave of
  wavenumber k.

- **Gravity.** Einstein's equations are not in play. The metric is
  fixed by us; it is not sourced by anything. (In 1+1D vacuum,
  Einstein's equations are trivial anyway — see future chapters
  if/when we need to discuss this.)

- **Charge.** No second compact dimension is present. There is no
  electromagnetic field, no Lorentz force, no g_μ5-style
  cross-terms in the Kaluza-Klein sense. Charge is the subject of
  a future project, not this one.

- **Off-diagonal metric components.** The bare metric (§2) is
  diagonal as a *starting* condition. Whether the math will force
  any cross-term to develop is the open question of §3, which
  later chapters will examine. We are not assuming the
  off-diagonals stay zero forever; we are starting them at zero
  and watching what happens.

---

## 10. Summary of givens

We have, in total:

1. A manifold M with coordinates (t, S, u) — t and S are real-line
   coordinates, u is a circle of circumference L_u.
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
the mass spectrum. Examine whether the bare diagonal metric remains
consistent with the solutions, or whether it has to be revised.
