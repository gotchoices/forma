# Chapter 5 — Stability and dimensionality

Chapter 3 bound a particle in the minimal setting: one extended dimension x plus
the compact phase. A real particle lives in three extended dimensions, and binding
in 1D does not automatically survive the lift. This is the arc's most exposed
chapter, so it is kept short and plain: for the localized 3D particle, the honest
status is *owed*.

## §1 The dimensional obstruction

The obstruction is **Derrick's theorem** (1964), which is a simple scaling
argument. Take a static lump of a real scalar field in d extended space dimensions
and shrink or stretch it by a factor λ. Its gradient (kinetic) energy and its
potential energy scale by different powers of λ, so the total energy usually has no
stationary point at finite size: for d ≥ 2 the lump either spreads until it
vanishes or collapses to a spike. A one-dimensional lump can sit at a stable size;
a two- or three-dimensional one, made of the same ingredients, cannot. So the 1D
success of Chapter 3 does not lift for free — dimensionality is a genuine physical
constraint, not a formality. **[cite Derrick; D]**

## §2 What each object is, dimensionally

It helps to speak of **codimension**: the number of space dimensions a defect does
*not* fill. A localized particle in 3D is codimension-3 (a point); a line is
codimension-2; a wall is codimension-1. The objects in hand are:

- The 1D **breather and kink** of Chapter 3, which live in one extended dimension.
  The **kink** is topologically protected (it carries a winding that cannot be
  undone); the **breather** is winding-0, so it is only *long-lived* — dynamically
  persistent, not protected — the same neutral-mass qualifier used in Chapter 3 §3
  and Chapter 6 §3. **[C]**
- The 2D **Q-ball**: a lump held together by a conserved **Noether charge** (a
  charge arising, by Noether's theorem, from a continuous internal symmetry — a
  field value that rotates in a complex phase). It resists dispersal by a
  "spin-faster-if-squeezed" mechanism and is stable in higher dimensions. But its
  stabilizer is Noether charge, which the C1 correction disavowed as GRID's
  mechanism — GRID's charge is a *topological* winding, not a Noether charge. So
  the Q-ball is a **borrowed** existence-proof: it shows that *some* wound object
  can be higher-dimensionally stable, not that the adopted one is. **[C, borrowed]**
- **Topological windings of a single phase**: a single U(1) winding threads space
  as a **vortex line** (codimension-2 — a line, not a point), and a kink is a
  **domain wall** (codimension-1 — a sheet). Neither is a localized,
  codimension-3 particle. **[forma]**

## §3 The gap: no demonstrated localized-3D particle

Whether a field can form a localized 3D lump that cannot be smoothly unwound is a
question of **homotopy** — of how the space of field *values* wraps around physical
space. The localized 3D solitons of standard field theory (skyrmions, Hopfions)
require the field's value-space to have a nontrivial **π₃** (a three-dimensional
"wrapping" class), which a single circle — one compact phase — simply does not
have. Consequently a localized-3D particle is **owed for both the charged and the
neutral case**: it is not demonstrated here. **[O]**

## §4 The resolution paths — a trichotomy, not a trap

Stated as a strict choice between a topological winding and a Noether charge, the
arc would look trapped. It is not a strict choice; there are three branches.

- **(i) Single-phase topological** (kink or vortex): consistent with the C1
  correction, but a single U(1) value-space (a circle, S¹) has trivial π₂ and π₃,
  so it yields **no localized 3D soliton**. **[O]**
- **(ii) Noether Q-ball**: localizes in 3D, but its stabilizer is a Noether charge,
  which **reopens C1**. **[borrowed]**
- **(iii) A richer target space**: a field whose values live on a **sphere** (S² or
  S³) admits skyrmions/Hopfions through π₂/π₃ and is therefore **both** localized in
  3D **and** topological — consistent with C1. This is the live hope. But it is not
  a free escape: a mere *product* of compact phases (a torus) is **aspherical** —
  its higher wrapping classes vanish — so it does **not** supply the needed
  topology. A spherical or non-abelian target is extra structure, and obtaining it
  from GRID is itself an open construction, deferred to
  [metric-charge](../metric-charge/). **[O]**

So the situation is open, not stuck: the branch that would deliver everything,
(iii), is a harder route rather than an unavailable one. **[forma]**

## §5 Where 3D localization would come from

The natural home for a localized 3D particle in the framework is a GRID **sheet** —
a fixed-size compact structure carrying windings — which plausibly localizes and
stabilizes the object where a bare phase cannot. That is
[metric-charge](../metric-charge/)'s construction, and its 3D localization is
deferred there rather than claimed here. **[cite metric-charge; O]**

## Attribution / dependencies

Derrick's theorem and the Q-ball/skyrmion catalog are standard field theory.
The 3D sheet construction belongs to [metric-charge](../metric-charge/). The 1D
objects are Chapter 3's.
