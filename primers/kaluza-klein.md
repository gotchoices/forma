# Kaluza-Klein Theory — A Ground-Up Introduction

A self-contained introduction to Kaluza-Klein (KK) theory: how
electromagnetism falls out of geometry once you allow spacetime to
have a small, compact extra dimension.

**Prerequisite:** [metric.md](metric.md). The metric primer covers
the geometry foundations — distance recipes, the metric as a
matrix, off-diagonal terms, position-dependent metrics, light
cones, geodesics, and compact dimensions. This primer takes those
as given and concentrates on KK theory itself. If any concept here
feels unmotivated, the metric primer almost certainly has the
background.

---

## Concepts introduced in this primer

| § | Concept |
|---|---------|
| 1 | The Kaluza-Klein hypothesis |
| 2 | Going from 4D to 5D: what changes? |
| 3 | The 5×5 metric and its three regions |
| 4 | The four-potential A_μ — a refresher |
| 5 | Identifying cross terms with the EM potential |
| 6 | What the cross terms do physically |
| 7 | Klein's contribution: compactification |
| 8 | What falls out — equations and quantities |
| 9 | Charge conservation from symmetry |
| 10 | Geodesics in 5D: where the force comes from |
| 11 | An analogy: the tilted conveyor belt |
| 12 | What is established vs. what is hypothetical |
| 13 | The essential insight |
| Appendix A | Deriving the Lorentz force from the 5D metric |

---

## 1. The Kaluza-Klein hypothesis

In 1921, Theodor Kaluza asked a striking question:

> *What if spacetime has one more dimension than we observe?*

We observe four dimensions: three of space (x, y, z) and one of
time (t). Maybe there is a fifth dimension — call it *w* — that we
can't see, perhaps because it is too small.

The hypothesis is geometric, not exotic: just one more direction
to move in, governed by the same kind of metric and geometry as the
four we already use. The interesting part is what we get for free
when we add it.

In 1926, Oskar Klein added the second piece of the story: the
fifth dimension is **compact**, meaning it wraps around like a
circle (see [metric.md §12](metric.md)). If you move far enough
in the w direction, you come back to where you started.

Together, **Kaluza-Klein theory** is the proposal that spacetime is
4D extended × 1D compact. The remarkable result, which we will
walk through, is:

> **Adding one compact extra dimension to gravity automatically
> produces electromagnetism.**

The rest of this primer unpacks how that works.

---

## 2. Going from 4D to 5D: what changes?

Adding one dimension to spacetime changes a few specific things and
leaves most of the machinery unchanged.

**What changes.**

- The number of coordinates goes from 4 to 5: from (t, x, y, z) to
  (t, x, y, z, w).
- The metric, which was a 4×4 symmetric matrix, becomes a 5×5
  symmetric matrix.
- A 5×5 symmetric matrix has 15 independent entries (5 diagonal +
  10 off-diagonal — symmetric so each off-diagonal pair counts as
  one). The 4×4 case had 10. So we have 5 new entries to make
  sense of.

**What stays the same.**

- The metric still measures distance the same way: ds² = g_AB dx^A
  dx^B with the indices now running over 5 coordinates instead of
  4.
- The metric still has Lorentzian signature (one negative
  eigenvalue, four positive — the time eigenvalue is still
  negative).
- Geodesics are still the paths free particles follow.

**Index notation note.** When we move to 5D, the convention is to
use *uppercase* indices A, B, ... = 0, 1, 2, 3, 4 to indicate "ranges
over all 5 coordinates," and *lowercase* indices μ, ν, ... = 0, 1, 2, 3
to indicate "ranges over the 4 spacetime coordinates only." We
will follow this convention. So:

- Sum over μ, ν → 4×4 = 16 terms (spacetime only)
- Sum over A, B → 5×5 = 25 terms (full 5D)
- An entry like g_μ5 has one spacetime index and one fifth-dim
  index — that's a "cross" entry, mixing 4D with the new direction.

---

## 3. The 5×5 metric and its three regions

The new 5×5 metric naturally splits into three regions, each with a
distinct physical role.

**Visualizing the split.** Picture the 5×5 metric matrix with its
rows and columns ordered (t, x, y, z, w). Four of the indices are
the familiar spacetime indices (t, x, y, z); one is the new w. We
can draw the matrix with a horizontal and vertical line separating
the spacetime indices from the w index:

```
        t   x   y   z  | w
       ─── ─── ─── ─── | ───
   t    .   .   .   . | .
   x    .   .   .   . | .
   y    .   .   .   . | .
   z    .   .   .   . | .
       ─── ─── ─── ───┼───
   w    .   .   .   . | .
```

Three regions:

1. **The 4×4 spacetime block** (top-left, with both indices
   spacetime): 10 independent entries. This is the *ordinary 4D
   metric* you already know.
2. **The single 1×1 corner entry g_55** (bottom-right, both indices
   = 5): 1 entry. This describes the metric in the w direction
   alone.
3. **The cross block g_μ5** (top-right and bottom-left, one
   spacetime index and one w index): 4 entries (since the matrix
   is symmetric, the top-right strip and the bottom-left strip
   carry the same 4 numbers).

So 5×5 with symmetry = 10 + 1 + 4 = 15 entries, matching what we
counted in §2.

**Writing the split as ds².** Instead of writing ds² as one big
sum of 25 terms, we group the contributions by which region they
come from:

<!-- ds² = g_μν dx^μ dx^ν (gravity) + g₅₅ dw² (scalar) + 2 g_μ5 dx^μ dw (EM) -->
$$
ds^2 = \underbrace{g_{\mu\nu}\,dx^\mu\,dx^\nu}_{\text{spacetime block}}
     + \underbrace{g_{55}\,dw^2}_{\text{w-alone}}
     + \underbrace{2\,g_{\mu 5}\,dx^\mu\,dw}_{\text{cross block}}
$$

The factor of 2 on the cross term comes from the symmetric matrix
convention (see [metric.md §6](metric.md)): the entries g_μ5 and
g_5μ are equal and both contribute, so they add up to 2 g_μ5 dx^μ dw.

**The three roles.**

| Region | Entries | Role |
|--------|---------|------|
| g_μν (spacetime block) | 10 | Ordinary 4D metric → gravity |
| g₅₅ (single corner) | 1 | Scalar (the "dilaton") |
| g_μ5 (cross block) | 4 | **Electromagnetism** |

The first two are familiar and unsurprising once you've absorbed
ordinary general relativity (see [metric.md §9](metric.md)). The
remarkable claim is the third: the four cross entries g_μ5 are
electromagnetism. The next two sections explain what that means
and why it is true.

---

## 4. The four-potential A_μ — a refresher

To explain the third claim of §3, we need a brief refresher on how
electromagnetism is described mathematically. (For a full treatment
see [maxwell-primer.md](maxwell-primer.md).)

In ordinary electromagnetism, you can specify the entire E and B
field configuration with just **four numbers** at every point in
spacetime — the **four-potential**:

<!-- A_μ = (φ/c, A_x, A_y, A_z) -->
$$
A_\mu = \left( \frac{\phi}{c},\; A_x,\; A_y,\; A_z \right)
$$

Reading the components:

- **φ** is the *scalar potential* — what a voltmeter measures. The
  φ/c is unit-conversion to put it on the same footing as the
  other three.
- **A_x, A_y, A_z** are the spatial (x, y, z) components of the
  *vector potential*, a vector field whose curl gives the magnetic
  field.

**Why does φ/c sit in the time slot?** The pairing isn't arbitrary
— it follows the same pattern as every other 4-vector in special
relativity. Position is (ct, x, y, z); energy-momentum is
(E/c, p_x, p_y, p_z); the time component is always the "scalar"
quantity and the spatial components are always the vector
quantity. The pattern works for A_μ because of what φ and **A** do
to a charged particle:

| Quantity | Time-component | Space-components | What it produces |
|---|---|---|---|
| Position | ct | x, y, z | — |
| Energy-momentum | E/c | p_x, p_y, p_z | — |
| Four-potential A_μ | φ/c | A_x, A_y, A_z | (force, below) |

The energy of charge q in the potential is **U = qφ**. The momentum
of charge q in the potential is **p = qA**. Energy and time are
canonically paired (energy is the time-component of momentum);
momentum and space are canonically paired (each spatial momentum is
the conjugate of the corresponding spatial coordinate). So φ ↔
energy ↔ time, and **A** ↔ momentum ↔ space. The four-potential
is just packaging "energy per charge" and "momentum per charge"
into one 4-vector.

Your hunch about derivatives also pays off: when you compute the
electric field

$$
\mathbf{E} = -\nabla\phi - \frac{\partial \mathbf{A}}{\partial t}
$$

the φ contribution comes from a *spatial* gradient and the **A**
contribution comes from a *time* derivative. So the two
contributions to E are sourced by derivatives in the
"perpendicular" direction relative to where each potential lives in
A_μ. That cross-coupling is exactly the kind of structure encoded
when we write the field tensor F_μν = ∂_μ A_ν − ∂_ν A_μ
(see [maxwell-primer.md](maxwell-primer.md) and Appendix A.4).

The actual electric and magnetic fields are derivatives of A_μ:

- E = −∇φ − ∂**A**/∂t  (E points "downhill" from high voltage,
  with a correction from time-varying **A**)
- B = ∇ × **A**  (B is the "swirl" of **A**)

So six field components (three of E, three of B) are determined by
just four numbers (the components of A_μ) once you know how to
take their derivatives. A_μ is the *underlying* object;
the E and B fields are derived from it.

The key fact for KK: **electromagnetism is fully encoded in a
4-vector A_μ, one number per spacetime direction**.

---

## 5. Identifying cross terms with the EM potential

Now we make the central identification of Kaluza-Klein theory.

The cross block of the 5×5 metric, g_μ5, contains 4 numbers (one
for each spacetime direction μ = t, x, y, z). The four-potential
A_μ also has 4 numbers. Kaluza's identification:

> **The cross-block of the 5D metric IS the electromagnetic
> four-potential.**

<!-- g_μ5 = A_μ -->
$$
g_{\mu 5} = A_\mu
$$

(The exact identification has a unit-conversion factor in front of
A_μ that depends on conventions; the order-of-magnitude story is
what matters. We will use the convention-light form for clarity.)

This is one identification, four equations (one per μ).

What it says, structurally:

- The metric component that mixes time with the compact w direction
  is the scalar potential: g_t5 ↔ φ.
- The metric components that mix the three spatial directions with
  w are the vector potential: g_x5 ↔ A_x, g_y5 ↔ A_y, g_z5 ↔ A_z.

If you know the 5D metric, you know the EM four-potential. And if
you know A_μ, you know the cross-block of the 5D metric. They are
the same mathematical object, viewed two ways.

**Why is this surprising?** Because nothing in the construction
"forces" the cross terms to be electromagnetism. We just added a
fifth dimension and asked what the metric matrix looks like. The
four off-diagonal entries that mix the new direction with the four
old ones happen to have *exactly* the right structure to play the
role of A_μ. The 5D Einstein equations, when worked out, give
Maxwell's equations for these entries. The 5D geodesic equation,
when projected to 4D, gives the Lorentz force. (Both of these
results we will sketch in later sections; appendix A works through
the geodesic-to-Lorentz derivation explicitly.)

This is the punchline of KK: **electromagnetism is not separate
from geometry; it is geometry, encoded in metric components we
hadn't been able to see before.**

---

## 6. What the cross terms do physically

This section is KK-specific: it takes the general "off-diagonal
terms mix coordinates" idea (covered in
[metric.md §6](metric.md)) and works out what that mixing means
*specifically* for the cross block g_μ5 of the 5×5 KK metric. The
factorization below — where ds² rearranges into a clean square
involving (dw + A_μ dx^μ) — only works because the cross block has
the special structure of being identified with A_μ.

The g_μ5 cross terms are not just a formal identification — they
have a clear physical interpretation in terms of how motion mixes.

**When A_μ = 0.** The cross terms vanish and the 5D metric
factorizes: ds² is just the 4D piece plus dw² alone. Motion in w
doesn't influence motion in spacetime, and vice versa. The
compact dimension is decoupled.

**When A_μ ≠ 0.** The cross terms mix spacetime motion with motion
in the compact direction. The 5D distance formula can be rewritten
as:

<!-- ds² = g_μν dx^μ dx^ν + (dw + A_μ dx^μ)² -->
$$
ds^2 = g_{\mu\nu}\,dx^\mu\,dx^\nu + \left(dw + A_\mu\,dx^\mu\right)^2
$$

(For simplicity we've absorbed unit factors and set g_55 = 1 in
this form; the exact coefficients depend on conventions.)

Expanding the squared term:

<!-- (dw + A_μ dx^μ)² = dw² + 2 A_μ dw dx^μ + A_μ A_ν dx^μ dx^ν -->
$$
\left(dw + A_\mu\,dx^\mu\right)^2 = dw^2 + 2\,A_\mu\,dw\,dx^\mu + A_\mu A_\nu\,dx^\mu\,dx^\nu
$$

The middle term (2 A_μ dw dx^μ) is the cross term — the one that
mixes dimensions. The last term (A_μ A_ν dx^μ dx^ν) is a small
correction to the spacetime metric from the EM field's energy.

**Physical picture: the conveyor-belt analogy.** Imagine walking on
a conveyor belt that runs at an angle to your path. Your forward
motion in spacetime carries you partly sideways into the w
direction (and vice versa). How much you drift depends on your
speed and the belt's tilt — and the belt's tilt is exactly A_μ.

If you also have momentum in the w direction (which we will
identify with charge in §7), the belt now accelerates you in
spacetime. That acceleration is what we observe as the
electromagnetic force.

So electromagnetism, in the KK picture, is a *mixing* between
ordinary spacetime motion and motion in a compact direction we
cannot directly see.

---

## 7. Klein's contribution: compactification

Klein's 1926 contribution was to make the fifth dimension compact:

<!-- w ~ w + L -->
$$
w \;\sim\; w + L
$$

The coordinate w wraps with circumference L. (This is the standard
compact dimension of [metric.md §12](metric.md), now applied
specifically to the KK extra dimension.)

This has a profound consequence: **quantization of charge**.

**Why quantization?** A particle's wavefunction ψ(t, x, y, z, w)
must be **single-valued**: going around the compact direction and
returning must give the same value. So:

<!-- ψ(w + L) = ψ(w) -->
$$
\psi(w + L) = \psi(w)
$$

The solutions of a wave equation with this periodicity have a very
restricted form in the w direction. The allowed w-dependence is:

<!-- ψ(w) ∝ e^(i n 2π w / L) -->
$$
\psi(w) \;\propto\; e^{i\,n\,2\pi w / L}
\qquad \text{for } n = 0, \pm 1, \pm 2, \ldots
$$

where n is an integer. (The integer n is what makes the solution
single-valued — fractional values would not return to the same
value after w → w + L.)

The momentum in the w direction is then quantized:

<!-- p_w = n ℏ / R    where R = L / (2π) -->
$$
p_w = \frac{n\,\hbar}{R}, \qquad R = \frac{L}{2\pi}
$$

R is the *compact radius* — the radius of the circle if you
imagine the compact direction as drawn on a cylinder.

**The key identification: charge IS quantized momentum in w.** A
particle's electric charge q is proportional to its w-momentum:

- n = 0: no momentum in w → no electric charge → neutral particle.
- n = +1: one unit of w-momentum → carries elementary charge +e.
- n = −1: one unit of w-momentum the other way → carries charge −e.
- n = ±2: would carry charge ±2e (no fundamental particle of pure
  EM nature has this; in nature only n = 0 and n = ±1 are observed
  for elementary particles).

The elementary charge is then:

<!-- e = ℏ / (R c) -->
$$
e = \frac{\hbar}{R\,c}
$$

(modulo unit-conversion conventions). Solving for R using the
known value of e gives R ≈ 2 × 10⁻³⁴ m — extraordinarily small,
far below anything we can probe experimentally. That smallness is
why we don't see the compact dimension directly.

So compactification produces, all at once:

- The discrete spectrum of allowed charge values (charge
  quantization).
- The interpretation of charge as a kind of momentum.
- An explanation for why the extra dimension is hidden from us
  (it's tiny).

---

## 8. What falls out — equations and quantities

When you take the 5D Einstein equations (the equations of motion
for the 5×5 metric in the presence of stress-energy) and project
them down to 4D using the three-region split of §3, three sets of
equations emerge:

| 5D equations component | 4D result |
|------------------------|-----------|
| Spacetime-spacetime (g_μν) | Einstein's equations (gravity) |
| Spacetime-w (g_μ5) | **Maxwell's equations** (electromagnetism) |
| w-w (g_55) | Scalar field equation (dilaton) |

When you take the 5D geodesic equation (the equation of motion for
a free particle in 5D) and project it down, you get:

> 4D geodesic (gravity) + Lorentz force (electromagnetism)

A free particle in 5D, which just follows a straight line, looks
like a charged particle being deflected by electromagnetic fields
in 4D. (Appendix A walks through this projection explicitly.)

These results are **exact** — not approximations, analogies, or
heuristics. They are mathematical consequences of having a 5×5
metric with the structure of §3. Maxwell's equations are literally
the Einstein equations applied to the off-diagonal block.

**Summary of identifications:**

| Physical concept | KK geometric origin |
|------------------|---------------------|
| EM potential A_μ | Off-diagonal metric g_μ5 |
| Electric charge | Momentum in compact dimension |
| Charge quantization | Periodicity of compact dimension |
| Charge conservation | Translation symmetry in w (Noether) |
| Lorentz force | Geodesic equation in 5D |
| Maxwell's equations | Einstein equations in 5D |
| Gauge transformation | Coordinate shift in w |

Each of these connections is a precise mathematical statement — the
KK identification turns each electromagnetic concept into a
geometric one.

---

## 9. Charge conservation from symmetry

A particularly elegant consequence comes from **Noether's theorem**:
every continuous symmetry of the physics corresponds to a conserved
quantity.

In ordinary 3D space:

- Translation symmetry in x → momentum p_x is conserved.
- Translation symmetry in y → momentum p_y is conserved.
- Rotation symmetry → angular momentum is conserved.

Apply the same theorem to the compact direction:

- Translation symmetry in w → momentum p_w is conserved.
- But p_w **is** electric charge.
- Therefore **electric charge is conserved**.

This is not a separate postulate — it follows automatically from
the geometry. If the metric doesn't depend on w (the compact
dimension "looks the same" everywhere along its circumference),
then momentum in w is conserved, which means charge is conserved.

This is the same reason momentum is conserved: space looks the
same at every point (translation symmetry). Charge conservation
and momentum conservation are the same theorem applied to
different dimensions.

---

## 10. Geodesics in 5D: where the force comes from

Consider a particle with momentum p_w = q c in the compact
direction (i.e., a particle of charge q), moving through a region
where A_μ ≠ 0. The 5D geodesic equation (shortest path in 5D)
produces, when projected to 4D:

<!-- (4D acceleration) = (gravitational terms) + q (E + v × B) -->
$$
\text{(4D acceleration)} = \text{(gravitational terms)} + q\,\bigl(\mathbf{E} + \mathbf{v} \times \mathbf{B}\bigr)
$$

The second term is the **Lorentz force** — the force on a charge q
in electric field E and magnetic field B, where v is the
particle's velocity. This is exact.

The particle isn't being pushed by a force in the 5D picture —
it's following a straight line (a geodesic) in 5D. But because the
compact dimension is tilted by the EM field (A_μ ≠ 0), a "straight
line" in 5D projects to a curved path in 4D. We interpret that
curvature as the effect of an electromagnetic force, just as we
interpret the curvature of an orbit around Earth as the effect of
gravitational force.

Appendix A works through the algebra showing exactly where the
electromagnetic field tensor F_μν and the Lorentz force appear
from the 5D Christoffel symbols.

---

## 11. An analogy: the tilted conveyor belt

Imagine a long hallway with a moving floor (like an airport
walkway), but the walkway runs at an angle to the hallway. The
floor's velocity field is A(x) — it varies along the hallway.

- A person standing still in the walkway direction (p_w = 0,
  neutral) is not affected by the walkway's angle — they don't
  move.
- A person walking in the walkway direction (p_w ≠ 0, charged)
  gets carried sideways by the angle — they experience a force.
- The faster they walk in the walkway direction (more charge),
  the stronger the sideways deflection.
- If the walkway angle varies along the hallway (A changes with
  position), the deflection varies — this is the electromagnetic
  field.

This analogy captures the essential mechanism: charge is motion in
a hidden direction, and the electromagnetic force is a geometric
consequence of that direction being tilted relative to the
directions we can see.

---

## 12. What is established vs. what is hypothetical

**Established (proven mathematically, not disputed):**

- The 5D → 4D decomposition is exact.
- Maxwell's equations emerge from the 5D Einstein equations.
- Charge quantization follows from periodicity.
- Geodesics in 5D give the Lorentz force in 4D.
- Noether's theorem gives charge conservation.

These are mathematical facts — true regardless of whether nature
actually has compact dimensions.

**Hypothetical (not observed, not disproven):**

- Whether nature actually has compact extra dimensions.
- The size of any such dimensions.
- Whether the dilaton scalar field exists.

LHC searches constrain compact dimension sizes to be smaller than
~10⁻¹⁹ m. This doesn't rule them out — KK predicts R ~ 10⁻³⁴ m,
which is far smaller than current experimental reach.

**Known limitations:**

- The compact radius R is a free parameter. KK doesn't predict its
  value, and hence doesn't predict the value of e (or α).
- Simple KK (one compact dimension) only produces U(1) gauge
  symmetry — electromagnetism. The strong force (SU(3)) and weak
  force (SU(2)) require additional compact dimensions with more
  complex topology. This is part of the motivation for string
  theory's 6–7 extra dimensions.
- KK predicts a scalar field (dilaton) from g₅₅. This field has
  not been observed.

---

## 13. The essential insight

Kaluza-Klein theory says:

> **Electromagnetism is what gravity looks like when there is a
> small, compact extra dimension.**

The electromagnetic field is the shape of the extra dimension.
Charge is momentum in the extra dimension. The force on a charged
particle is the curvature of the shortest path through the extra
dimension. All of electromagnetism — fields, forces, charge
quantization, charge conservation, Maxwell's equations — is
geometry.

Whether nature actually works this way is unknown. But the
mathematical machinery is exact, and it provides a framework in
which questions about charge, confinement, and particle structure
can be formulated precisely.

---

## Appendix A: Deriving the Lorentz force from the 5D metric

Sections 7–10 stated that the electromagnetic field tensor and the
Lorentz force *emerge* from the 5D geodesic equation. This appendix
shows the algebra explicitly.

**Scope.** This appendix derives one of Kaluza's original results:
the Lorentz force on a charged particle, obtained by projecting the
5D geodesic equation into 4D spacetime. It does **not** cover:

- The derivation of Maxwell's equations from the 5D Einstein
  equations (a much longer calculation involving the 5D Ricci tensor).
- Klein's quantization of charge from compactification (covered
  conceptually in §7 of the main text).
- The dilaton field equation from the g₅₅ component.

Our goal is to show, with full algebra, exactly where the
electromagnetic field tensor F_ab arises from the 5D metric, and
how it produces the Lorentz force in the projected equation of
motion. The other results follow from similar (but lengthier)
manipulations of the same metric.

*(Based on V. T. Toth's derivation,
[vttoth.com/CMS/physics-notes/118](https://www.vttoth.com/CMS/index.php?view=article&id=118).)*


### A.1 The 5D metric ansatz

We use uppercase indices A, B = 0…4 for five dimensions and
lowercase a, b = 0…3 for four-dimensional spacetime. The 5D metric
is written in block form:

<!-- G_AB = [[g_ab + g_44 A_a A_b, g_44 A_a], [g_44 A_b, g_44]] -->
$$
G_{AB} = \begin{pmatrix}
  g_{ab} + g_{44}\,A_a A_b & g_{44}\,A_a \\
  g_{44}\,A_b & g_{44}
\end{pmatrix}
$$

where g_ab is the ordinary 4D spacetime metric, A_a is an arbitrary
4-vector (which will turn out to be the electromagnetic potential),
and g₄₄ is the metric component in the compact direction. Writing
the metric in this specific "factored" form does not lose generality
— any 5×5 symmetric matrix can be put in this shape by absorbing
off-diagonal entries into A_a.


### A.2 The inverse metric

The inverse of G_AB is:

<!-- G^AB = [[g^ab, -A^a], [-A^b, 1/g_44 + A²]] -->
$$
G^{AB} = \begin{pmatrix}
  g^{ab} & -A^a \\
  -A^b & g_{44}^{-1} + A^2
\end{pmatrix}
$$

where A² = A_a A^a (the norm squared of the 4-vector, with index
raised by g^{ab}). This can be verified by direct multiplication:
G_AB G^{BC} = δ^C_A.


### A.3 Assumptions

Two assumptions simplify the Christoffel symbols enormously:

1. **g₄₄ = constant everywhere.** The scalar field component of the
   metric (the "dilaton") does not vary. This eliminates terms
   involving ∂g₄₄.

2. **The cylinder condition: ∂₄G_AB = 0.** Nothing in the metric
   depends on the fifth coordinate. Physically, the compact dimension
   "looks the same" at every point along its circumference. This is
   equivalent to saying the fifth direction is a Killing field — a
   direction of continuous symmetry.

These two conditions together kill several families of Christoffel
symbols: Γ_{a44} = Γ_{4b4} = Γ_{44c} = 0.


### A.4 The Christoffel symbols where F_ab appears

The Christoffel symbol (connection coefficient) is defined as:

<!-- Γ^C_AB = ½ G^CD (∂_A G_BD + ∂_B G_AD − ∂_D G_AB) -->
$$
\Gamma^C_{AB} = \tfrac{1}{2}\,G^{CD}
  \bigl(\partial_A G_{BD} + \partial_B G_{AD} - \partial_D G_{AB}\bigr)
$$

We now compute the mixed 4–5 component. Using the cylinder condition
(∂₄G_bd = 0) and the constant g₄₄:

<!-- Γ^c_4b = ½ g^cd (∂_b(g_44 A_d) − ∂_d(g_44 A_b)) = ½ g_44 g^cd (∂_b A_d − ∂_d A_b) -->
$$
{}^{(5)}\Gamma^c_{4b}
  = \tfrac{1}{2}\,g^{cd}
    \bigl(\partial_b(g_{44} A_d) - \partial_d(g_{44} A_b)\bigr)
  = \tfrac{1}{2}\,g_{44}\,g^{cd}
    \bigl(\partial_b A_d - \partial_d A_b\bigr)
$$

(The second equality holds because g₄₄ is constant — assumption 1
in §A.3 — so it factors out of both derivatives.)

The quantity in parentheses is exactly the **electromagnetic field
tensor** (sometimes called the Faraday tensor):

<!-- F_bd = ∂_b A_d − ∂_d A_b -->
$$
F_{bd} = \partial_b A_d - \partial_d A_b
$$

F_bd encodes both the electric and magnetic fields. Its components
are: F₀ᵢ = Eᵢ (electric field) and F_ij = ε_ijk B_k (magnetic
field). See [`maxwell-primer.md`](maxwell-primer.md) for details.

So the Christoffel symbol becomes:

<!-- Γ^c_4b = ½ g_44 F_b^c -->
$$
{}^{(5)}\Gamma^c_{4b} = \tfrac{1}{2}\,g_{44}\,F_b{}^c
$$

By the index symmetry of the Christoffel symbols (Γ^A_{BC} = Γ^A_{CB}),
the same calculation gives Γ^c_{a4} = ½ g₄₄ F_a^c. And Γ^b_{44} = 0
follows directly from the two assumptions above (every term in its
defining expression contains either ∂_4 of the metric or ∂ of g₄₄).

**This is the heart of the derivation:** the field tensor F_ab —
the mathematical object that encodes all of electromagnetism — falls
out of the Christoffel symbols of the 5D metric. It appears because
the off-diagonal metric entries A_a vary from point to point. Where
A_a is constant, F_ab = 0 and there is no field; where A_a varies,
the field is nonzero.

The purely-spacetime Christoffels Γ^c_{ab} also need to be computed
to get the gravitational part of the equation of motion. Their
calculation is straightforward but lengthier — they reduce to the
ordinary 4D Christoffels of g_ab plus correction terms involving
A_a A_b that account for the electromagnetic field's contribution
to gravity. We omit the explicit calculation here; only the mixed
terms Γ^c_{4b} are needed to see the Lorentz force appear.


### A.5 Projecting the geodesic equation to 4D

The 5D geodesic equation (equation of motion for a free particle)
is:

<!-- d²x^A/dτ² + Γ^A_BC (dx^B/dτ)(dx^C/dτ) = 0 -->
$$
\frac{d^2 x^A}{d\tau^2}
  + \Gamma^A_{BC}\,\frac{dx^B}{d\tau}\,\frac{dx^C}{d\tau} = 0
$$

where τ is the proper time along the particle's world-line. To get
the 4D equation, we take only the A = a (spacetime) components and
split the sum over B, C into 4D and 5th-dimension parts:

<!-- d²x^a/dτ² + Γ^a_bc u^b u^c + 2 Γ^a_4b u^4 u^b + Γ^a_44 (u^4)² = 0 -->
$$
\frac{d^2 x^a}{d\tau^2}
  + {}^{(5)}\Gamma^a_{bc}\,u^b u^c
  + 2\,{}^{(5)}\Gamma^a_{4b}\,u^4 u^b
  + {}^{(5)}\Gamma^a_{44}\,(u^4)^2
  = 0
$$

where u^b = dx^b/dτ is the 4-velocity and u⁴ = dx⁴/dτ is the
velocity in the compact direction.

Substituting the Christoffel symbols from §A.4:

- Γ^a_{44} = 0
- Γ^a_{4b} = ½ g₄₄ F_b^a (computed above)
- Γ^a_{bc} contains the gravitational terms (the 4D Christoffel of
  g_ab, plus small A_a A_b corrections we are not tracking explicitly)

The sum over B, C includes both (B=4, C=b) and (B=b, C=4).
Since Γ^a_{4b} = Γ^a_{b4} (Christoffel symmetry in the lower
indices), these two terms are equal.  Their sum is
2 × ½ g₄₄ F_b^a u⁴ u^b, and the 2 cancels the ½:

<!-- d²x^a/dτ² + Γ^a_bc u^b u^c = −g_44 u^4 F_b^a u^b -->
$$
\frac{d^2 x^a}{d\tau^2}
  + {}^{(5)}\Gamma^a_{bc}\,u^b u^c
  = -g_{44}\,\frac{dx^4}{d\tau}\;F_b{}^a\,\frac{dx^b}{d\tau}
$$

The left side is the 4D geodesic equation — the equation of motion
under gravity alone. The right side is an additional term: a force
proportional to the field tensor F_b^a, the 4-velocity u^b, and
the compact-direction velocity u⁴.

The quantity −g₄₄ dx⁴/dτ plays the role of the **charge-to-mass
ratio** q/m. A particle at rest in the compact direction
(dx⁴/dτ = 0) feels no electromagnetic force — it is neutral. A
particle with nonzero compact momentum feels a force proportional
to that momentum — it is charged.

Written in more familiar notation, the right-hand side is exactly
the **Lorentz force**:

$$
\frac{q}{m}\bigl(\mathbf{E} + \mathbf{v} \times \mathbf{B}\bigr)
$$

A free particle following a straight line in 5D looks like a charged
particle being deflected by electromagnetic fields in 4D — the
force is an artifact of projecting a 5D geodesic into 4D.


### A.6 What the derivation establishes

The computation above is purely mechanical — no physical
assumptions beyond the metric ansatz and the cylinder condition.
The results are:

1. **F_ab from geometry.** The electromagnetic field tensor is
   encoded in the Christoffel symbols of the 5D metric. It
   appears wherever the off-diagonal entries A_a vary in
   spacetime.

2. **Lorentz force from geodesics.** The equation of motion for a
   free 5D particle, projected to 4D, contains the Lorentz force
   term. The "force" is a geometric artifact.

3. **Charge = compact momentum.** The strength of the coupling to
   the field is proportional to dx⁴/dτ — momentum in the compact
   direction. Particles with zero compact momentum are neutral.

These results do not depend on any particular field configuration,
particle type, or energy scale. They are consequences of having a
5×5 metric with the assumed structure.

**A note on rigor.** The Γ^a_{bc} term on the left-hand side of
A.5's final equation is the *5D* Christoffel, not the pure 4D one.
The 5D version contains additional terms involving A_a A_b that we
have absorbed silently. A fully rigorous treatment would split
Γ^a_{bc} (5D) = Γ^a_{bc} (4D) + (correction terms from A_a A_b),
showing that the corrections represent the gravitational
back-reaction of the electromagnetic field on the spacetime
geometry. For the purpose of seeing the Lorentz force appear, this
extra accounting is unnecessary; for a physically complete
treatment in a curved spacetime carrying a real EM field, it
matters.

---

*See also: `studies/R1-kk-charge/theory.md` for how this framework
extends to two material dimensions and connects to the WvM electron
model.*
