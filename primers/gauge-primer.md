# Gauge Theory — A Vocabulary Primer

What physicists mean when they say "gauge," "local gauge invariance,"
"A_μ," "U(1)," "SU(3)," and "covariant derivative." This primer
teaches the language the Standard Model speaks, without committing
to any particular interpretation of what these objects *are*. The
goal is fluency: enough vocabulary to read modern physics literature
and to recognize where forma reuses the same words for the same
structures and where forma might read them differently.

**Audience:** general engineering background. Calculus, vectors,
and basic complex numbers (e^iθ) are assumed. No prior physics
beyond Maxwell-level intuition is required; relevant background is
introduced as needed. Familiarity with [maxwell-primer.md](maxwell-primer.md)
helps but is not required.

---

## Contents

1. [What "gauge" means as a word](#1-what-gauge-means-as-a-word)
2. [Symmetry, redundancy, and what's "real"](#2-symmetry-redundancy-and-whats-real)
3. [Global symmetry — the easy half](#3-global-symmetry--the-easy-half)
4. [Local symmetry — and what it forces](#4-local-symmetry--and-what-it-forces)
5. [The connection: enter A_μ](#5-the-connection-enter-a_μ)
6. [A note on subscripts: A_μ vs A_4 vs A_5 vs "A4"](#6-a-note-on-subscripts-a_μ-vs-a_4-vs-a_5-vs-a4)
7. [The covariant derivative](#7-the-covariant-derivative)
8. [Groups, gently](#8-groups-gently)
9. [U(1) — the circle group](#9-u1--the-circle-group)
10. [SU(2) — and the problem of isospin](#10-su2--and-the-problem-of-isospin)
11. [SU(3) — and the problem of color](#11-su3--and-the-problem-of-color)
12. [Abelian vs non-abelian](#12-abelian-vs-non-abelian)
13. [Reading "SU(3) × SU(2) × U(1)"](#13-reading-su3--su2--u1)
14. [Gauge bosons — the messengers](#14-gauge-bosons--the-messengers)
15. [How forma reuses this language](#15-how-forma-reuses-this-language)

---

## 1. What "gauge" means as a word

In everyday English, a *gauge* is a measuring standard: railway
gauge (distance between rails), wire gauge (thickness), pressure
gauge. It is the *choice of reference* against which something is
measured.

The physics usage descends from Hermann Weyl, who in 1918 proposed
a theory in which the *scale* (length-gauge) of objects could be
chosen freely at every point in space. Weyl's original proposal
was wrong as a theory of electromagnetism, but the word stuck. In
modern usage:

> A **gauge** is a free choice of reference that has no physical
> consequence. **Gauge invariance** is the statement that the
> physics doesn't depend on which choice is made.

The choice is typically a labeling — a number attached to each
point in space — that can be set arbitrarily without changing any
measurable quantity. The classic example is electric potential
(voltage): adding 100 V to *every* point in space changes nothing
that any voltmeter can measure, because voltmeters report
*differences*. The "ground" is a gauge choice.

Two senses of the word recur:

- **Gauge freedom** — the menu of allowed relabelings.
- **Gauge fixing** — picking one specific labeling out of that
  menu, usually for computational convenience.

A theory is *gauge-invariant* when its predictions are unchanged
by any allowed relabeling.


## 2. Symmetry, redundancy, and what's "real"

Gauge invariance is sometimes called a **redundancy** rather than
a true symmetry, because the relabeled and original descriptions
are the same physical state — not two distinct states related by
some operation. The relabeling is a change of *description*, not
of the world.

This distinction matters because it tells us what counts as
physically real:

> If two configurations differ only by a gauge transformation,
> they describe the *same* physical situation. Anything that
> changes under a gauge transformation is unobservable. Only
> gauge-invariant quantities are physically meaningful.

The classic example is in electromagnetism, where the same
physical situation can be described in two layers.

The **fields** are what instruments measure. The electric field
**E** is a vector at every point that says how much force a
positive test charge would feel; the magnetic field **B** is a
vector at every point that says how much sideways force a moving
charge would feel. A voltmeter and a magnetometer report quantities
built from **E** and **B**.

The **potentials** are a deeper layer of bookkeeping. The scalar
potential φ is a single number at each point — voltage, in the
static case. The vector potential **A** is a vector field at each
point. The fields are derived from the potentials by:

    E = −∇φ − ∂A/∂t
    B = ∇ × A

(See [maxwell-primer.md](maxwell-primer.md) for the step-by-step
derivation.) The rule that brings gauge invariance in: there are
infinitely many (φ, **A**) labelings that produce the *same* **E**
and **B**. Concretely, replacing

    φ → φ − ∂χ/∂t
    A → A + ∇χ

for any scalar function χ(x, t) leaves **E** and **B** unchanged.
The labeling (φ, **A**) is a gauge choice; the fields **E** and
**B** are the gauge-invariant content. A voltmeter reading depends
only on **E** and **B**, never on which (φ, **A**) was chosen to
encode them.

This is the prototype: the *fields* are real, the *potentials* are
labels. Section 5 introduces the relativistic four-vector A_μ that
packages φ and **A** into a single object; that is the gauge
field whose existence is forced by §4's argument.


## 3. Global symmetry — the easy half

Quantum mechanics describes a particle by a complex-valued *wave
function* ψ(x). The "complex-valued" part means each value of ψ
has a magnitude and a phase angle:

<!-- ψ(x) = |ψ(x)| · e^(iθ(x)) -->
$$
\psi(x) = |\psi(x)| \cdot e^{i\theta(x)}
$$

The magnitude squared |ψ|² gives the probability density of
finding the particle at x — this is what experiments measure. The
phase angle θ(x) does not appear by itself in any measurement.

So consider this transformation: rotate the phase of ψ by the
*same* angle α at every point in space:

<!-- ψ(x) → e^(iα) · ψ(x)    (α the same everywhere) -->
$$
\psi(x) \;\to\; e^{i\alpha} \cdot \psi(x) \qquad (\alpha \text{ the same everywhere})
$$

Magnitudes are unchanged, so |ψ|² is unchanged, so no experiment
can detect the rotation. This is a **global symmetry** — "global"
because the same α is used at every point. It costs nothing and
buys nothing.

Global phase symmetry is real but unsurprising. It says only that
the *absolute* phase of a wave function has no meaning, only
phase *differences* do. Compare this to electric potential: only
*differences* in voltage matter, never the absolute level.


## 4. Local symmetry — and what it forces

Now the move that creates gauge theory. Drop the requirement that
α be the same everywhere. Allow it to vary from point to point:

<!-- ψ(x) → e^(iα(x)) · ψ(x)    (α different at each point) -->
$$
\psi(x) \;\to\; e^{i\alpha(x)} \cdot \psi(x) \qquad (\alpha \text{ different at each point})
$$

This is a **local** transformation — "local" because the angle is
chosen independently at each point. The word "local" is doing all
the work: this is what makes a theory a *gauge* theory in the
modern sense.

Here is the surprise. The wave function's *value* at each point is
unaffected in magnitude, but the *derivatives* of ψ are now
broken. The derivative ∂_μ ψ measures how ψ changes from point to
neighboring point. If the phase has been independently rotated at
each point, the change from one point to its neighbor now includes
an artificial contribution from the relabeling — not a real
change in the wave function, just a change in *labels*.

Concretely, applying the chain rule to e^(iα(x)) ψ(x):

<!-- ∂_μ (e^{iα(x)} ψ) = e^{iα(x)} (∂_μ ψ + i (∂_μ α) ψ) -->
$$
\partial_\mu \left( e^{i\alpha(x)} \psi \right)
= e^{i\alpha(x)} \left( \partial_\mu \psi + i (\partial_\mu \alpha) \psi \right)
$$

The first term is what one would want — the original derivative,
re-phased. The second term, i (∂_μ α) ψ, is junk: it is purely an
artifact of the local relabeling. If the equations of motion
contained ∂_μ ψ directly, they would no longer be gauge-invariant —
a relabeling would produce a different equation, and the physics
would change.

The fix is to introduce a new field that *also* shifts under the
relabeling, in just the right way to cancel the junk. That field
is the **connection**.


## 5. The connection: enter A_μ

Postulate a new field A_μ(x) — a vector field with one component
per spacetime direction (μ = 0, 1, 2, 3) — and decree that under
the local phase relabeling, A_μ shifts as:

<!-- A_μ(x) → A_μ(x) − ∂_μ α(x) -->
$$
A_\mu(x) \;\to\; A_\mu(x) - \partial_\mu \alpha(x)
$$

Then the combination ∂_μ ψ + i A_μ ψ transforms cleanly: the
junk term from ψ's transformation cancels against the shift in
A_μ. This combination is the **covariant derivative**, written
D_μ ψ. Section 7 unpacks it.

The point for now is structural: insisting that the physics not
depend on local phase relabelings *forces* a new field A_μ to
exist on the same footing as the wave function. Not as an add-on
chosen for convenience — as a logical consequence of the demand
for local invariance. And the recipe for how A_μ shifts under
relabeling is exactly the recipe for the electromagnetic
four-potential under a *gauge transformation* in classical
electromagnetism.

What was once a vague observation in Maxwell's theory — "the
potentials φ and **A** can be shifted by a gauge transformation
without changing E and B" — turns out, when read backwards, to be
the *defining* feature of electromagnetism. Electromagnetism is
the field that has to exist to make local phase rotations
harmless.

| Object | What it is | How it transforms |
|---|---|---|
| ψ(x) | Complex wave function (matter) | ψ → e^(iα(x)) ψ |
| A_μ(x) | Connection (electromagnetism) | A_μ → A_μ − ∂_μ α |
| D_μ ψ | Covariant derivative | D_μ ψ → e^(iα(x)) D_μ ψ |

The covariant derivative transforms in the *same way* as ψ
itself — that is what "covariant" means here: the two move
together under the relabeling. Plain ∂_μ ψ doesn't have this
property; D_μ ψ does. Equations built from D_μ ψ are
gauge-invariant; equations built from ∂_μ ψ are not.


## 6. A note on subscripts: A_μ vs A_4 vs A_5 vs "A4"

The notation around A causes recurring confusion. Several
distinct uses share the letter:

**A_μ (with a Greek index μ).** The four-component
electromagnetic potential. The index μ ranges over the four
spacetime directions: μ = 0, 1, 2, 3 (or sometimes μ = 1, 2, 3, 4
in older conventions where the time component is listed last).
Components are A_0 = φ/c (the time component, related to
voltage), A_1 = A_x, A_2 = A_y, A_3 = A_z (the spatial
components).

**A_4 (with the literal numeral 4).** Two readings, depending on
context:

- *In some 4D conventions:* the time component when indices are
  numbered 1–4 instead of 0–3. Older European textbooks used
  this convention. Same object as A_0 in modern notation.
- *In Kaluza-Klein theory:* the component of A in the *fifth*
  dimension when the fifth dimension is indexed as 4 (because
  spacetime indices were 0–3). See [kaluza-klein.md](kaluza-klein.md)
  for the geometric meaning. In KK, A_4 (or A_5 in some
  notations) is sometimes interpreted as a scalar field separate
  from electromagnetism.

**A5 / A_5.** Same Kaluza-Klein object as the second reading of
A_4, just with the extra dimension indexed as 5 (so spacetime
runs 0–4, or 1–4, and the compact dimension is 5).

**"A4" with no subscript.** In forma's [grid/foundations.md](../grid/foundations.md),
"A1" through "A6" are *axiom labels*, not field components. A4
is the local gauge invariance axiom. When [projects/grid-primitive/01-foundation.md](../projects/grid-primitive/01-foundation.md)
writes "each link between cells carries a gauge connection A_μ
(A4)," the parenthetical "(A4)" is a citation to axiom 4, not a
component of A.

When in doubt, look at what is being subscripted (Greek index =
spacetime), the dimension count of the surrounding theory (4D vs
5D), and whether the "A" is followed by a numeral with or without
underscore. Context disambiguates almost every case; the
ambiguity is purely notational.


## 7. The covariant derivative

The combination introduced in §5,

<!-- D_μ ψ = ∂_μ ψ + i q A_μ ψ -->
$$
D_\mu \psi \;=\; \partial_\mu \psi + i q A_\mu \psi
$$

is the **covariant derivative**. The factor q is the **coupling
constant** — for electromagnetism, q is the electric charge of
the particle ψ describes. (Different particles have different
charges; the photon couples to all of them through this single
A_μ but with different q.)

The word "covariant" here does *not* mean the same thing it does
in general relativity (where it refers to invariance under
coordinate changes). In gauge theory, "covariant" means the
derivative *co-varies* with ψ under gauge transformations:
both pick up the same e^(iα(x)) factor, so equations built from
D_μ ψ behave as if no transformation had happened.

A useful mental picture: ∂_μ ψ asks "how much does ψ change from
this point to the next?" Without A_μ, that question is
ill-defined when local relabelings are allowed, because part of
the change might be a relabeling rather than a real change. A_μ
is the bookkeeping that subtracts off the relabeling, leaving
only the real change. It is a *connection* in the geometric
sense — it tells how to compare ψ at neighboring points after
they have been independently relabeled.

Replacing ∂_μ with D_μ everywhere in a theory's equations is
called **minimal coupling**. It is the recipe for converting a
theory of free matter into a theory of matter coupled to the
gauge field. The interaction between matter and electromagnetism
is, at its core, just the rewriting ∂_μ → D_μ.


## 8. Groups, gently

To extend gauge theory beyond electromagnetism, one more piece of
vocabulary is needed: **groups**.

A **group** is a set of operations that can be combined, where
combining always produces another operation in the set. The
combination has an identity (the "do nothing" operation) and
every operation has an inverse (an "undo"). Examples:

- Integers under addition: combining 3 and 5 gives 8 (in the
  set); the identity is 0; the inverse of 3 is −3.
- Rotations of a square that map it back to itself: the four
  90°-step rotations form a group of size 4.
- Rotations of a circle by *any* angle: a continuous group of
  size infinity.

A **Lie group** (pronounced "Lee," after Sophus Lie) is a group
whose operations form a smooth continuum. Rotations of a circle
are a Lie group; the integers are not. Lie groups are the kind
relevant to gauge theory because the relabelings α(x) used in
§4 vary continuously.

Each Lie group has a **dimension** — the number of independent
parameters needed to specify a group element. Rotations of a
circle have dimension 1 (just the rotation angle). Rotations of
a sphere in 3D have dimension 3 (three Euler angles, or
equivalently three components of an angular velocity vector).

Each Lie group also has a set of **generators** — basis elements
near the identity from which finite group elements are built by
exponentiation. The number of generators equals the dimension.
Generators matter for gauge theory because **each generator
gives rise to one gauge field** (one A_μ). One-dimensional Lie
group → one gauge field; three-dimensional → three gauge fields;
eight-dimensional → eight gauge fields.

The Lie groups that appear in physics are almost always denoted
by short names like U(N), SU(N), SO(N), Sp(N). The first letter
or two records the type of operation; the number records the size
of the object the operations act on.


## 9. U(1) — the circle group

**U(1)** stands for **Unitary group of dimension 1**. "Unitary"
means an operation that preserves the magnitude of complex
numbers: u·u* = 1 for the operation u, where u* is the complex
conjugate. The "dimension 1" means the operation acts on a
1-component complex object (a single complex number).

The full set of U(1) operations is: multiplication by e^(iα) for
any real angle α. That is exactly what was used in §3 and §4 to
relabel the wave function ψ. So:

> The gauge group of electromagnetism is U(1).

U(1) is the circle group: its operations are points on a circle
(parametrized by α ∈ [0, 2π)), and combining two operations
adds their angles. It has dimension 1 (one parameter α), so it
has one generator, and therefore one gauge field — the
electromagnetic A_μ.

This is the original example. Quantum electrodynamics (QED) is
the theory built from a complex matter field (the electron's
wave function) with U(1) gauge invariance enforced. The gauge
field A_μ that the symmetry forces into existence is the
photon, and the equations of motion that result are Maxwell's
equations coupled to the electron.

The motivating problem QED solved: Dirac had written down a
relativistic wave equation for the electron, but it described
only the electron in isolation. To make it interact with light,
something had to be added by hand. Demanding U(1) local gauge
invariance turned out to *uniquely* fix the form of that
addition — it must be A_μ coupled through the covariant
derivative, with strength set by the electron's charge.
Electromagnetism is not added to the electron; it is *required*
by the electron's local phase symmetry.


## 10. SU(2) — and the problem of isospin

**SU(2)** stands for **Special Unitary group of dimension 2**.
"Special" means the operations have determinant +1 (a technical
condition that excludes a redundant overall phase). "Dimension 2"
means the operations act on a 2-component complex object — a
*pair* of complex numbers.

A 2-component object can be written as a column:

    ψ = (ψ_1)
        (ψ_2)

An SU(2) operation is a 2×2 complex matrix that mixes ψ_1 and
ψ_2 while preserving |ψ_1|² + |ψ_2|². It has 3 independent real
parameters — the three Euler-angle-like rotations of a
2-component complex vector. So SU(2) has dimension 3, three
generators, and a gauge theory built on it has *three* gauge
fields.

The motivating problem (Yang and Mills, 1954): Heisenberg had
noticed that the proton and the neutron, despite their different
electric charges, have nearly identical masses and behave almost
identically under the strong nuclear force. He proposed that the
proton and neutron are two states of a single underlying entity
— a "nucleon" — distinguished by an internal label called
**isospin** that behaves like a 2-component complex vector
(proton on top, neutron on bottom). The strong force was
indifferent to which label was on top, suggesting a symmetry
under SU(2) rotations of the (proton, neutron) pair.

Yang and Mills asked: what if this isospin symmetry were
*local* — independently rotatable at each point? By the same
logic that produced electromagnetism from local U(1), they
found that local SU(2) requires not one but *three* gauge
fields, all interacting with each other (a feature absent in
U(1) electromagnetism — see §12). The original Yang-Mills paper
turned out not to describe the strong force directly, but the
*mathematical structure* it introduced became the template for
both the weak force (where SU(2) reappears as part of the
electroweak group) and the strong force (where SU(3) plays the
analogous role).


## 11. SU(3) — and the problem of color

**SU(3)** is the **Special Unitary group of dimension 3** —
operations on 3-component complex vectors that preserve their
total magnitude. It has 8 independent real parameters, so 8
generators, and a gauge theory built on it has *eight* gauge
fields.

The motivating problem: in the early 1960s, the Δ⁺⁺ baryon was
discovered. It contains three "up" quarks (uuu) all with their
spins aligned in the same direction. By Pauli's exclusion
principle, three identical fermions cannot occupy the same
quantum state — yet the Δ⁺⁺ apparently did exactly that. Either
Pauli was wrong (unthinkable) or the three quarks were
distinguished by some hidden label.

The hidden label was named **color**, with three values
conventionally called red, green, and blue (no relation to
optical color — the names are mnemonic). Each quark carries one
of three colors, so a "red up quark" and a "blue up quark" are
distinct states and Pauli is satisfied. The three colors form a
3-component complex vector that the strong force is indifferent
to — a global SU(3) symmetry.

Promoting this global SU(3) to a *local* SU(3) symmetry, by the
same Yang-Mills procedure that gave electromagnetism from U(1),
forces eight gauge fields into existence. These are the eight
**gluons** of the strong force. The resulting theory is
**quantum chromodynamics** (QCD), and it is the modern
description of how quarks are bound into protons, neutrons, and
all other hadrons.

Two things distinguish QCD from QED:

- The gauge fields (gluons) themselves carry color charge and
  interact with each other directly. This is the non-abelian
  feature (§12) and is responsible for *confinement* — the
  reason isolated quarks are never seen.
- There are eight gauge bosons instead of one, corresponding to
  the eight generators of SU(3).


## 12. Abelian vs non-abelian

A group is **abelian** (after the mathematician Niels Abel) if
combining operations in either order gives the same result:
A·B = B·A. It is **non-abelian** if order matters: A·B ≠ B·A
in general.

- U(1) is abelian. Multiplying by e^(iα) and then e^(iβ) gives
  e^(i(α+β)), the same as doing them in the other order.
- SU(2) and SU(3) are non-abelian. Two-by-two and three-by-three
  matrix multiplications generally do not commute.

The non-abelian feature has a striking physical consequence: the
gauge fields of a non-abelian theory carry the gauge charge
themselves and interact with each other. The photon (U(1)) is
electrically neutral and does not interact with other photons.
The gluons (SU(3)) carry color charge and interact with other
gluons. The Ws and Z (SU(2) part of electroweak) carry weak
charge and interact with each other.

This single difference — gauge bosons carrying their own charge —
distinguishes the long-range, additively-interfering character of
electromagnetism from the short-range, confining character of the
strong force. Both follow from local gauge invariance; the
difference is just which group is being made local.


## 13. Reading "SU(3) × SU(2) × U(1)"

The Standard Model of particle physics is summarized in one
expression:

    SU(3) × SU(2) × U(1)

This is the Standard Model's **gauge group**. The "×" means
"and also" — three gauge groups acting independently and
simultaneously. Each contributes its own set of gauge fields and
its own coupling constant:

| Factor | Force | Gauge fields | Number |
|---|---|---|---|
| SU(3) | Strong (color) | Gluons | 8 |
| SU(2) | Weak (isospin) | W and Z bosons | 3 |
| U(1) | Hypercharge | B field | 1 |

A one-line description of each force, in the Standard Model's
reading:

- **Strong force** — what binds quarks into protons and neutrons,
  and (as a residual leakage) binds protons and neutrons into
  atomic nuclei. Range ≈ 1 fm (size of a proton); strongest of
  the four forces at short range; characterized by *confinement*
  (quarks never appear in isolation).
- **Weak force** — what causes radioactive beta decay (a neutron
  turning into a proton plus an electron plus an antineutrino)
  and other particle-changing processes. Range ≈ 10⁻¹⁸ m
  (a thousand times smaller than a proton); weak at low energies
  but on equal footing with electromagnetism at high energies
  (hence "electroweak" unification).
- **Electromagnetism** (the U(1) factor, after electroweak
  mixing) — the long-range force between electric charges, the
  source of light, and the binding of electrons to nuclei in
  atoms. Range infinite; strength set by α ≈ 1/137.
- (**Gravity** is not in this group at all. It has no Standard
  Model description; general relativity treats it as spacetime
  curvature rather than a gauge field, and quantum gravity is an
  open problem.)

Total: 12 gauge fields. Three of them (the SU(2) Ws and one B
combination) mix to produce the photon and the W±, Z bosons of
the observed electroweak force; the other eight are the gluons.

(The U(1) factor in the Standard Model is not exactly the U(1)
of plain electromagnetism — it is a related "hypercharge" group
that mixes with SU(2) to produce the photon after spontaneous
symmetry breaking. The distinction matters for technical
calculations but not for reading the symbol.)

When the Standard Model is written as "SU(3) × SU(2) × U(1)",
the claim being made is: every fundamental force except gravity
is the gauge field forced into existence by demanding local
invariance under this group acting on the matter fields
(quarks and leptons). The forces are not added to nature; they
are *required* by the matter's local symmetries.


## 14. Gauge bosons — the messengers

Particles are quanta of fields. The matter fields (electrons,
quarks, neutrinos) have particle quanta called **fermions**. The
gauge fields (A_μ for U(1), the SU(2) and SU(3) versions) have
particle quanta called **gauge bosons**.

| Force | Gauge group | Gauge boson(s) | Mass | Range |
|---|---|---|---|---|
| Electromagnetism | U(1) | Photon (γ) | 0 | infinite |
| Weak | SU(2) | W⁺, W⁻, Z | ~80–91 GeV | ~10⁻¹⁸ m |
| Strong | SU(3) | 8 gluons | 0 | confined |
| Gravity | (general covariance) | Graviton (hypothetical) | 0 | infinite |

The pattern: each generator of the gauge group corresponds to
one gauge field, which corresponds to one type of gauge boson.
U(1) has 1 generator → 1 photon; SU(2) has 3 generators →
3 weak bosons; SU(3) has 8 generators → 8 gluons.

In the language of forces, gauge bosons are the **messengers**
exchanged between matter particles to convey the force. Two
electrons repel by exchanging photons; two quarks attract by
exchanging gluons. This "particle exchange" picture is the
quantum-field-theory reading of forces.

Whether *forces themselves are fundamentally exchanges of
messenger particles*, or whether the particle-exchange picture
is one of several valid descriptions of an underlying continuous
field interaction, is a question of interpretation. The
mathematics works either way.


## 15. How forma reuses this language

forma's GRID model uses the same gauge vocabulary, but the
*origin* of the gauge structure differs from the Standard Model's,
and forma's reading of the strong and weak forces departs from
the SM's in substantive ways.

### U(1) and A_μ — same equations, different origin

In [grid/foundations.md](../grid/foundations.md), axiom A3 gives
each lattice cell a phase θ ∈ [0, 2π) — a single angular
coordinate, valued in the circle group U(1). Axiom A4 then
demands that the physics be invariant under arbitrary local
relabelings of θ. The connection forced into existence by A4 is
called A_μ and lives on the *links* between cells, not on the
cells themselves. In the continuum limit, this A_μ becomes the
electromagnetic four-potential, and Maxwell's equations follow
([grid/maxwell.md](../grid/maxwell.md)).

So the chain U(1) → local symmetry → connection → A_μ → Maxwell
is the same chain QED uses. The difference is one of *origin*:

- In the Standard Model, U(1) is *postulated* as the matter
  field's symmetry group, and the connection A_μ is *required*
  by the postulate.
- In GRID, U(1) is the phase structure that *each cell already
  has* by axiom A3 (a compact internal coordinate). Local gauge
  invariance is then a statement about how the *labeling* of
  that pre-existing phase is unphysical.

In both readings, A_μ is a connection forced into existence by
local U(1) invariance. The Standard Model treats this as a
mathematical convenience that happens to describe nature; GRID
treats it as the lattice's *bookkeeping for relative phase
between neighboring cells*. The equations are identical; what
differs is whether A_μ is fundamental or emergent.

### Phase and connection on the same primitive

A working forma project, [projects/grid-primitive/](../projects/grid-primitive/),
goes one step further: it asks what the lattice cells and links
themselves are *made of*. Its hypothesis is that each link is a
2D cylindrical tube with two coupled fields — a longitudinal
strain *e(x, t)* and an azimuthal phase *φ(x, t)*. The phase φ
coarse-grains to the gauge field A_μ; the strain e plays the
role of the matter field. Crucially, e and φ are *not*
independent fields laid on top of one another — they are coupled
strain components of a single elastic structure, linked by a
shear coefficient *K_eφ*
(see [projects/grid-primitive/01-foundation.md](../projects/grid-primitive/01-foundation.md)
§7).

This means matter and gauge field, in the grid-primitive
reading, are *one geometric object* viewed along two axes. The
Standard Model's deep structural fact — that the gauge field is
forced to exist by the matter field's local symmetry — has a
direct mechanical realization: they cannot be separated because
they are two components of the same physical strain.

### Strong force — a non-standard interpretation

forma proposes a reinterpretation of the strong force as
electromagnetism without α-suppression
([qa/Q95-strong-force-as-internal-em.md](../qa/Q95-strong-force-as-internal-em.md)).
The argument:

- In forma's MaSt model, the electron and other charged
  particles are localized photon modes on a compact internal
  surface (Ma).
- The full internal electromagnetic fields on Ma are roughly
  1/α ≈ 137× stronger than what is measured externally; the
  external field is what *leaks out* through the Compton window.
- At distances much larger than a Compton wavelength,
  particles interact via the leaked external field — ordinary
  QED, with coupling α.
- At distances of order a Compton wavelength, the internal Ma
  surfaces overlap, and the *full* internal fields couple
  directly. The effective coupling strength jumps by a factor
  of 1/α.
- The observed ratio α_strong / α ≈ 137 is, in this reading,
  exactly 1/α — not a coincidence but the predicted ratio of
  internal-to-external EM coupling strengths.

In short: the strong force is the electromagnetic force seen
from *inside* Ma, without the α-projection. Nucleons bind
because once the Ma tori overlap, the lower-energy configuration
is a coupled mode rather than two separated particles. SU(3)
gauge theory, in this reading, is an effective low-energy
description; the underlying mechanism is geometric overlap of
internal field structures.

This is forma's working hypothesis, not a settled result.
Whether eight gluon-like modes emerge from the overlap geometry
in the way SU(3) requires is open.

### Weak force — a non-standard interpretation

forma also proposes a structural reading of the weak force, the
neutron's instability, and Fermi's coupling constant G_F
([studies/R64-nuclear-harmonic-stack/findings-13.md](../studies/R64-nuclear-harmonic-stack/findings-13.md)).

In MaSt, the neutron and proton are modes on a shared internal
sheet (the *p-sheet*), distinguished by which direction they
wind. They have nearly the same mass; the small mass difference
that makes the neutron decay-unstable is attributed to a
**shear** in the p-sheet metric — a small geometric detuning
parametrized by *s_p*. The headline numerical result:

<!-- G_F ≈ s_p · α² / m_p² -->
$$
G_F \;\approx\; s_p \cdot \frac{\alpha^2}{m_p^2}
$$

where s_p is the p-sheet shear, α is the fine-structure
constant, and m_p is the proton mass. Plugging in forma's
calibrated s_p ≈ 0.194 reproduces the measured Fermi constant
to within 0.5%, and the resulting neutron lifetime matches the
880-second observation. (As of R64's writeup this is described
as a "suggestive numerical relationship" rather than a derived
mechanism — the matrix-element derivation is still pending.)

The qualitative reading: there is no separate "weak force." The
weak interaction is what the *same* electromagnetic structure
looks like when sheet shear breaks the symmetry between two
otherwise-degenerate matter modes. β-decay is the relaxation
channel from the higher-energy mode (neutron) to the
lower-energy mode (proton plus byproducts). The W and Z bosons
of the SM may be effective field-theoretic descriptions of
mode-transition amplitudes, not exchanged elementary particles.

### SU(2) and SU(3) — partial commitments

For the gauge groups themselves, forma's positions are partial:

- **SU(2)** — The flavor symmetry that the SM treats as an
  abstract internal SU(2) (up vs down quark, proton vs neutron)
  is identified in R64 with a *geometric ring-direction* on the
  p-sheet: u and d quarks differ by which way they wind, not by
  an abstract internal label. Whether this geometric reading
  reproduces the full SU(2) algebra (and not just a Z_2 flip)
  is open.
- **SU(3)** — The three "colors" of the SM are speculated in
  Q95 §7 to correspond to the three matter sheets (Ma_e, Ma_ν,
  Ma_p), but this is flagged as far from established. SU(3)
  remains the gauge structure forma has the least committed
  reading of.

### The general pattern

Across all of these, the pattern is consistent: where the
Standard Model postulates a fundamental gauge field whose
existence is required by an abstract internal symmetry, forma
attempts to identify a *geometric or mechanical structure* that
both produces the symmetry and explains the observed dynamics.
The vocabulary of gauge theory — connections, generators, group
factors — is preserved, but the things the symbols name are
recast as features of compact geometry rather than as
fundamental fields in their own right.

A reader who knows the Standard Model's gauge language will
recognize forma's equations and conclusions. The point of
divergence is *what the symbols are about*: in one reading,
abstract internal symmetries that nature happens to respect; in
the other, the bookkeeping of an underlying geometric and
mechanical structure.

---

## Summary

| Term | Plain meaning |
|---|---|
| Gauge | A free reference choice with no physical consequence |
| Gauge invariance | Physics doesn't depend on the choice |
| Global symmetry | Same relabeling at every point |
| Local symmetry | Independent relabeling at each point |
| Connection | The field forced to exist by local symmetry |
| A_μ | The connection of U(1) gauge theory (= electromagnetic potential) |
| Covariant derivative D_μ | ∂_μ adjusted by A_μ to remain gauge-invariant |
| Coupling constant | The strength with which matter sees the gauge field (e.g., charge) |
| Group | A set of operations closed under combination |
| Lie group | A continuous group |
| Generator | A basis operation near the identity; one gauge field per generator |
| U(N) | Unitary operations on N-component complex vectors |
| SU(N) | U(N) with determinant 1 |
| Abelian | Operations commute (order doesn't matter) |
| Non-abelian | Operations don't commute; gauge bosons interact with each other |
| Gauge boson | The particle quantum of a gauge field (photon, gluon, W, Z) |
| Standard Model gauge group | SU(3) × SU(2) × U(1) — strong, weak, hypercharge |

---

## Where to go next

- [maxwell-primer.md](maxwell-primer.md) — the four-potential A_μ
  and how E and B are derived from it, in classical EM terms.
- [physics-from-fabric.md](physics-from-fabric.md) — GRID's own
  treatment of gauge invariance, connections, and Maxwell from
  the lattice axioms, in informal language.
- [kaluza-klein.md](kaluza-klein.md) — how A_μ can emerge from
  pure geometry (a tilted extra dimension) instead of being
  postulated as a gauge field.
- [grid/foundations.md](../grid/foundations.md) — the GRID
  axioms, including A3 (compact phase) and A4 (local gauge
  invariance), which together give U(1) and A_μ.
