# Maxwell's Equations — A Ground-Up Review

What electromagnetic fields are, where they come from, and how
they're described mathematically. Assumes calculus (derivatives,
integrals, vectors). Builds to the four-potential A_μ, which is
the bridge to Kaluza-Klein theory (`kaluza-klein.md`).

---

## 1. Two fields, one force

Electromagnetism has two fields:

- **E** — the electric field. A vector (arrow) at every point in
  space. It points in the direction a positive charge would be
  pushed.
- **B** — the magnetic field. Also a vector at every point. It
  pushes moving charges sideways (perpendicular to their velocity).

The total force on a charge q moving with velocity **v** is:

    F = q (E + v × B)

This is the **Lorentz force law**. The electric part (qE) pushes
charges regardless of whether they're moving. The magnetic part
(q**v** × **B**) only acts on moving charges, and pushes them
sideways.

**v × B** is a cross product: it produces a vector perpendicular
to both **v** and **B**, with magnitude |**v**||**B**| sin θ,
where θ is the angle between **v** and **B**. When the charge
moves perpendicular to the field (θ = 90°, sin θ = 1), the force
is maximum. When it moves parallel to the field (θ = 0°,
sin θ = 0), the force is zero. This is why magnetic fields make
charges spiral rather than accelerate in a straight line — the
force is always sideways, never along the direction of motion.


## 2. Field lines: the visual picture

An electric field around a positive charge points outward in all
directions, like spikes on a sea urchin. The field strength falls
off as 1/r²:

    |E| = q / (4πε₀ r²)

where ε₀ is the permittivity of free space (a constant that sets
the strength of electric interactions) and r is the distance from
the charge.

A magnetic field around a wire carrying current forms loops that
circle the wire. The field strength falls off as 1/r:

    |B| = μ₀ I / (2π r)

where μ₀ is the permeability of free space and I is the current.

These patterns — radial lines for E, loops for B — are what
Maxwell's equations describe.


## 3. Divergence and curl: two ways a field can "do something"

To state Maxwell's equations, we need two operations on vector
fields. Both ask: "what is this field doing at a given point?"

### Divergence: ∇ · F — does the field spread out?

The divergence measures whether field lines are **emanating from**
(positive divergence) or **converging to** (negative divergence)
a point. Think of it as measuring sources and sinks.

- The E field around a positive charge: field lines radiate
  outward → positive divergence at the charge location.
- A uniform E field (same everywhere): no spreading, no
  converging → zero divergence.

Mathematically, for a vector field **F** = (F_x, F_y, F_z):

    ∇ · F = ∂F_x/∂x + ∂F_y/∂y + ∂F_z/∂z

Each term asks: "is the x-component increasing in the x
direction?" (and similarly for y and z). If all components are
increasing along their own directions, the field is spreading
out — positive divergence.

The result is a scalar (single number) at each point: how much
net "outflow" there is.

### Curl: ∇ × F — does the field circulate?

The curl measures whether field lines **rotate** around a point.
Think of placing a tiny paddlewheel in a flowing river: if the
flow is faster on one side than the other, the wheel spins. The
curl is the axis and rate of that spin.

- The B field around a wire: field lines loop around the wire
  → nonzero curl at the wire location.
- A uniform B field: no looping → zero curl.

Mathematically:

    ∇ × F = ( ∂F_z/∂y − ∂F_y/∂z ,
              ∂F_x/∂z − ∂F_z/∂x ,
              ∂F_y/∂x − ∂F_x/∂y )

Each component checks whether the field is "swirling" around
that axis. The result is a vector: the direction and magnitude
of the rotation.

### The gradient: ∇φ — the slope of a scalar field

One more operation we'll need. If φ is a scalar field (a single
number at each point, like voltage or temperature), its gradient
is:

    ∇φ = (∂φ/∂x, ∂φ/∂y, ∂φ/∂z)

The gradient points in the direction of steepest increase and has
magnitude equal to the slope. For voltage: ∇φ points "uphill"
from low voltage to high voltage, so −∇φ points "downhill" — the
direction a positive charge would move.


## 4. Maxwell's equations

Four equations that govern all of electromagnetism. Each one says
something specific about divergence or curl of E or B.

### Equation 1: Gauss's law (divergence of E)

    ∇ · E = ρ / ε₀

The divergence of E (how much E spreads out) equals the charge
density ρ divided by ε₀. In words: **electric field lines
emanate from charges.** Where there's positive charge, E points
outward. Where there's negative charge, E points inward. Where
there's no charge, E has zero divergence (field lines pass
through without spreading or converging).

### Equation 2: No magnetic monopoles (divergence of B)

    ∇ · B = 0

The divergence of B is always zero. In words: **magnetic field
lines never emanate from a point — they always form closed
loops.** There are no magnetic "charges" (monopoles). Every
magnetic field line that goes out somewhere must come back in
somewhere else.

### Equation 3: Faraday's law (curl of E)

    ∇ × E = −∂B/∂t

The curl of E (how much E circulates) equals the negative time
derivative of B. In words: **a changing magnetic field creates a
circulating electric field.** This is how generators work: spin a
magnet (changing B), and an electric field appears that pushes
current through a wire.

### Equation 4: Ampère-Maxwell law (curl of B)

    ∇ × B = μ₀ J + μ₀ ε₀ ∂E/∂t

The curl of B equals μ₀ times the current density J, plus μ₀ε₀
times the time derivative of E. In words: **magnetic field
lines circulate around currents and around changing electric
fields.** The first term is Ampère's original law (current creates
magnetic field). The second term is Maxwell's addition (changing
E also creates B). Together they allow electromagnetic waves.


## 5. The wave equation: light

Maxwell's great discovery was that equations 3 and 4 together
predict waves.

In empty space (no charges, no currents: ρ = 0, J = 0):

    ∇ × E = −∂B/∂t       (changing B creates circulating E)
    ∇ × B = μ₀ε₀ ∂E/∂t   (changing E creates circulating B)

A changing E creates B, and a changing B creates E. They sustain
each other, propagating through space as a wave. The wave speed
turns out to be:

    c = 1 / √(μ₀ ε₀) = 299,792,458 m/s

This is the speed of light. Maxwell realized (1865) that light IS
an electromagnetic wave — E and B oscillating perpendicular to
each other and to the direction of travel.

For a photon:
- E and B are perpendicular to each other
- Both are perpendicular to the direction of travel
- |E| = c|B| at every point
- The energy travels at speed c (via the Poynting vector S = E × B / μ₀)


## 6. The scalar potential: voltage

Equation 1 says E emanates from charges. For a stationary charge
(nothing changing in time), we can describe E entirely with a
single number at each point — the **scalar potential** φ (voltage):

    E = −∇φ

The electric field points downhill from high voltage to low
voltage, with magnitude equal to the slope. This works because
in electrostatics, ∇ × E = 0 (equation 3 with ∂B/∂t = 0), and
any curl-free vector field can be written as the gradient of a
scalar.

Examples:
- Between the plates of a capacitor: φ changes linearly from one
  plate to the other → E is uniform between the plates.
- Around a point charge: φ = q/(4πε₀r) → E = −∇φ points radially
  outward, magnitude q/(4πε₀r²). The familiar Coulomb field.

φ is simpler than E: one number per point instead of three. It
encodes the same information (for static fields) in fewer numbers.


## 7. The vector potential: A

For magnetic fields, we need something similar. Equation 2 says
∇ · B = 0 (no magnetic monopoles — field lines always close).
Any divergence-free vector field can be written as the curl of
another vector field. So there exists a vector **A** such that:

    B = ∇ × A

**A** is called the **vector potential**. It's a vector (three
components) at every point in space. The magnetic field is its
curl — the "swirl" of **A** gives **B**.

What does **A** look like? Around a straight wire carrying
current, **B** loops around the wire. The **A** that produces this
B points along the wire (parallel to the current), and its
magnitude falls off as 1/r. The curl of this parallel flow gives
the looping B field.

**A** isn't unique: you can add the gradient of any scalar to
**A** without changing **B** (because ∇ × ∇φ = 0 — the curl of
a gradient is always zero). This freedom is called **gauge
invariance**, and it's a deep feature of electromagnetism.


## 8. The full picture: E and B from φ and A

When fields change in time, both potentials are needed:

    E = −∇φ − ∂A/∂t

    B = ∇ × A

The electric field has two sources:
- −∇φ: the familiar "downhill from high voltage" part
- −∂**A**/∂t: if the vector potential is changing in time, it
  creates an additional electric field. This is Faraday's law in
  potential form — a changing magnetic situation (encoded in **A**)
  produces an electric field.

The magnetic field has one source:
- ∇ × **A**: the curl (swirl) of the vector potential

These two equations replace all four of Maxwell's equations.
Equations 2 and 3 are automatically satisfied by any **A** and φ
(they're built into the definitions). Equations 1 and 4 become
equations for **A** and φ in terms of charges and currents.

So **four** equations about **six** field components (E and B)
reduce to **two** equations about **four** potential components
(φ and **A**). The potentials are the more fundamental description.


## 9. The four-potential: combining φ and A

In special relativity, time and space are unified. It turns out
that φ and **A** also unify into a single object with four
entries — one per spacetime coordinate:

    A_μ = (φ/c, A_x, A_y, A_z)

or equivalently, labeling the time component A_t = φ/c:

    A_μ = (A_t, A_x, A_y, A_z)

This is the **electromagnetic four-potential**. It transforms
under Lorentz boosts (changes of reference frame) as a single
object, mixing φ and **A** just as boosts mix time and space.

Why does this matter? Because the four-potential has exactly four
entries — one per spacetime dimension. And in Kaluza-Klein theory,
the 5D metric has exactly four cross terms between spacetime and
the compact dimension — also one per spacetime dimension. Kaluza's
identification:

    g_μ5 = A_μ

says these are the same object. The electromagnetic potential
isn't just described by geometry — it IS geometry. The four
numbers that encode all of electromagnetism are the four numbers
that describe how the compact dimension tilts relative to
spacetime.


## 10. Summary

| Layer | What it describes | Number of components |
|-------|-------------------|---------------------|
| E and B | Fields you measure (forces on charges) | 6 (3 + 3) |
| φ and A | Potentials (more fundamental, fewer numbers) | 4 (1 + 3) |
| A_μ | Four-potential (relativistic combination) | 4 |
| g_μ5 | Metric cross terms in KK (= A_μ) | 4 |

Each layer describes the same physics with increasing elegance.
Maxwell's equations govern E and B. The potentials φ and **A**
encode them more compactly. The four-potential A_μ unifies them
relativistically. And in KK, A_μ is revealed to be the shape of
an extra dimension.

---

*Continue to [`kaluza-klein.md`](kaluza-klein.md) §7–§8 to see
how the four-potential enters the 5D metric and produces the
Lorentz force from geometry.*
