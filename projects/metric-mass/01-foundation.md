# Chapter 1 — Foundation

This chapter establishes the manifold, metric, and field on which
the rest of the project rests. It is the only chapter where we
*assume* things; every later chapter must derive its claims from
what is stated here.

The chapter is organized as: **givens** (axioms we accept without
derivation), **immediate consequences** (things that follow
directly from the givens), and **explicit non-assumptions** (things
we are *not* assuming, to be derived later).

---

## 1. The manifold

We work on a 3-dimensional manifold M with coordinates (t, S, u):

| Coordinate | Range | Topology |
|---|---|---|
| **t** | t ∈ ℝ | Real line, no identification |
| **S** | S ∈ ℝ | Real line, no identification (1D extended space) |
| **u** | u ∈ [0, L_u) | Compact circle: u ~ u + L_u |

Topologically: M = ℝ × ℝ × S¹, an infinite cylinder of
circumference L_u.

**Why these and not others.** This is the smallest manifold on which
mass-from-compactification can be derived. Time is needed for any
dynamics. One extended spatial dimension S is needed to talk about
a wave propagating "somewhere." One compact dimension u is needed
for the momentum-quantization that produces mass. Adding more
extended dimensions, more compact dimensions, or non-trivial
topology will be deferred to later chapters or other projects.

**Note on visualization.** When we render M to a screen later, we
embed (t, S, u) as Cartesian (x=S, y=u, z=t). The Cartesian axes
x, y, z are *display* coordinates and have no metric meaning.

---

## 2. The metric

The bare metric on M is diagonal:

<!-- ds² = -c² dt² + dS² + du² -->
$$
ds^2 = -c^2\,dt^2 + dS^2 + du^2
$$

In matrix form, with coordinate ordering (t, S, u):

<!-- g = diag(-c², 1, 1) -->
$$
g_{\mu\nu} = \begin{pmatrix} -c^2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

**Properties to note.**

- **Signature.** One negative eigenvalue (the t entry). The metric
  is Lorentzian — there is a light cone at every point.
- **Constant.** g_μν does not depend on t, S, or u. The manifold
  is *flat* in the Riemannian sense — no curvature anywhere.
- **No off-diagonal entries.** None of the three coordinates "mix"
  with any other. Later chapters may turn cross-terms on; this
  chapter does not.
- **u is on equal footing.** The compact direction has the same
  diagonal entry (1) as the extended direction S. The only thing
  that distinguishes u is its periodic identification, not its
  metric weight.

**Why diagonal.** Off-diagonal entries encode physical fields
(see [kaluza-klein.md](../../primers/kaluza-klein.md) §3 and §7).
Adding any field — even a mass — can introduce off-diagonal
terms. Starting from a fully diagonal bare metric makes it
possible to identify, in later chapters, which off-diagonals are
forced by what.

---

## 3. The wave field (light)

We assume the existence of a single real scalar field φ on M:

<!-- φ : M → ℝ -->
$$
\varphi : M \to \mathbb{R}
$$

This field obeys the massless wave equation in the metric of §2:

<!-- □φ = g^μν ∂_μ ∂_ν φ = 0 -->
$$
\Box\varphi \;=\; g^{\mu\nu}\,\partial_\mu\partial_\nu\varphi \;=\; 0
$$

Expanding with the metric of §2:

<!-- (-1/c²)∂²φ/∂t² + ∂²φ/∂S² + ∂²φ/∂u² = 0 -->
$$
-\frac{1}{c^2}\frac{\partial^2\varphi}{\partial t^2}
+ \frac{\partial^2\varphi}{\partial S^2}
+ \frac{\partial^2\varphi}{\partial u^2}
= 0
$$

**Interpretation.** φ is the project's stand-in for "light" — a
massless propagating perturbation. We use a scalar field rather
than a vector or tensor field because the simplest possible carrier
is sufficient to derive mass-from-compactification. Adding spin and
polarization is a generalization that does not change the argument
this project is making.

**Single-valuedness on the compact direction.** Because u is a
circle, φ must satisfy:

<!-- φ(t, S, u + L_u) = φ(t, S, u) -->
$$
\varphi(t, S, u + L_u) = \varphi(t, S, u)
$$

This boundary condition is the entire reason mass will appear in
later chapters. Without it, u would just be a third infinite
direction and nothing distinguishing would happen.

---

## 4. Addressing the light-in-1D question

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

## 5. Explicit non-assumptions

The following are *not* given. They are to be derived.

- **Mass.** No object in M has been assigned a mass. The wave
  equation is the massless one. If something with rest energy
  emerges, it must come from φ-configurations and the topology of
  u — not from a mass term inserted by hand.
- **Particles.** No discrete entities are postulated. φ is a
  continuous field. Anything resembling a particle must arise as
  a localized or topologically-distinguished configuration of φ.
- **Quantum mechanics.** The wave equation is classical. We will
  invoke quantization-of-momentum at the boundary condition (4)
  but otherwise treat φ classically. ℏ enters only at the step of
  identifying p = ℏk for a wave of wavenumber k.
- **Gravity.** Einstein's equations are not in play. The metric is
  fixed; it is not sourced by anything. (In 1+1+1D vacuum gravity
  would be trivial anyway — see future chapters for why this is
  not a loss.)
- **Charge.** No second compact dimension is present. There is no
  EM field, no Lorentz force, no g_μ5 cross-terms in the
  Kaluza-Klein sense.
- **Off-diagonal metric components.** The metric is purely
  diagonal. If a configuration of φ requires the metric to
  develop off-diagonals, that will be a derived consequence, not
  a starting assumption.

---

## 6. Summary of givens

We have, in total:

1. A manifold M = ℝ × ℝ × S¹ with coordinates (t, S, u) and
   compact circumference L_u.
2. A constant diagonal Lorentzian metric
   ds² = −c² dt² + dS² + du².
3. A real scalar field φ on M.
4. The massless wave equation □φ = 0.
5. Periodicity of φ in u: φ(·, ·, u + L_u) = φ(·, ·, u).

That is the entire content of this chapter. Everything else in
the project must be derived from these five items.

---

## What's next

[Chapter 2](02-mass-from-u.md) — Derive the dispersion relation for
solutions of □φ = 0 on M, identify the n=0 modes as massless
S-propagation and the n≠0 modes as carrying rest energy, and
read off the mass spectrum m_n = n ℏ / (R_u c²) where R_u = L_u / 2π.
