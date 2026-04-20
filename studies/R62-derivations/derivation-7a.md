# Derivation 7a — Spin from the 2×2 internal torus metric

**Status: See also derivation-7b.md for an alternative
approach.**

This derivation asked whether spin-½ can be produced by the
metric structure (Killing vectors, holonomy) of a single flat
2-torus.  The answer is correctly negative: the flat T² metric
has trivial holonomy and an abelian Killing algebra, neither
of which can generate spin-½.

Derivation 7b takes a different approach: instead of looking
for spin in the metric structure, it examines the CP
polarization vector's rotation rate on the torus and arrives
at spin = n_t/n_r (the Williamson–van der Mark ratio rule).
The two derivations address different questions — 7a asks
about the manifold's intrinsic structure, 7b asks about the
field's behavior on that manifold — and reach different
conclusions about whether spin-½ is derivable.

The mathematical content of 7a (Killing algebra dimension
count, holonomy calculation on flat T²) is correct as
mathematics.  Whether the metric-based approach or the
field-polarization approach is the physically relevant one
for MaSt's standing-wave particles is an open question.

---

*Original abstract (preserved for reference):*

Determine which spin values can be carried by standing-wave
eigenstates of a photon on the sheared 2-torus of derivations
2–6, and identify the geometric mechanism (if any) that
produces each.  Three sub-questions are answered, in order:

1. **Spin-1** on T² — derived cleanly from 1-form (vector)
   modes plus 4D Lorentz, exactly as one would expect from
   the Horoto–Scholtz framework applied to T².
2. **Spin-½** on T² via the Killing-vector route — does
   *not* produce spin-½ by a Lie-algebra dimension count:
   T² has only two commuting Killing vectors, but spin-½
   requires three with so(3) brackets.
3. **Spin-½** on T² via the holonomy / Berry-phase route —
   does *not* produce spin-½ by a topological count:  a
   flat 2-torus (even with shear) has zero Riemann
   curvature, so Levi-Civita parallel transport around any
   closed loop on T² is the identity, producing no rotation
   phase.  Equivalently: π_1(T²) = ℤ × ℤ is abelian and
   admits no Z₂ quotient that could give the (−1) on a 2π
   rotation that defines a spinor.

The result is therefore **spin-1 derived; spin-½ not
determined by the 2-torus metric alone through either of
the two mechanisms tested**.  Note this does *not* mean
spin-½ fields are forbidden on T² — T² admits four
inequivalent ℤ₂ spin structures, so spin-½ fields live on
it once a spin structure is chosen as an additional input;
the metric simply doesn't pick one out.  Section F
enumerates the three geometric extensions that could
produce spin-½ from intrinsic structure in later work —
extending the internal space (Horoto–Scholtz's S³
approach), invoking cross-sheet coupling on MaSt's full
T⁶, or introducing a Wess–Zumino topological term — and
identifies the most natural for MaSt to pursue.
Derivation 7b takes a different route on the same T²:
instead of the metric, it counts the rotation of the CP
electric-field vector and arrives at the WvM ratio rule
s = n_t/n_r.

---

## Attribution

The strategic framework — *charge follows from internal-space
symmetry, spin follows from spacetime symmetry, both as
Killing-vector charges* — is due to:

> L. Horoto and F. G. Scholtz, *A New Perspective on
> Kaluza–Klein Theories*, arXiv:2404.05302 [gr-qc] (2024),
> University of Stellenbosch.

Their §5 ("Spin as spacetime symmetry") gives an explicit
Killing-vector derivation of spin-1 from 3D Euclidean
rotational isometries (their Eq. 215–220) and of spin-½ from
a 4D-Euclidean Killing structure on the unit 3-sphere with
Hopf coordinates (their Eq. 224–227).  We adopt their
framework wholesale in §B–§D below, citing specific equations
where used.  The summary in `reference/horoto-scholtz-summary.md`
expands on the relationship between their work and this
program.

The novel parts of this derivation are:

- The *application* of the framework to the sheared 2-torus
  (which Horoto–Scholtz do not consider — their U(1)×U(1)
  internal space in §4.2.1 is conformally flat with no
  off-diagonal entries).
- The explicit holonomy calculation on the sheared T²
  (§E) and the resulting verdict on MaSt's empirical
  parity-of-tube-windings rule for spin-½.
- The identification of the precise topological obstruction
  to spin-½ from T² alone, and the enumeration of the
  geometric extensions that would bridge it (§F).

---

## Inputs

In addition to the inputs of derivations 1–6:

1. **F4** (Track 2): metric ansatz for M⁴ × T² with
   U(1)×U(1) gauge structure, conserved compact momenta
   P_a = g_ab w^b for a, b ∈ {4, 5}.
2. **F8** (Track 3): standing-wave compact-mode eigenstates
   on T²,

   $$
   \Phi_{n_{t}, n_{r}}(x^{4}, x^{5})
   \;=\; \frac{1}{\sqrt{L_{t}\,L_{r}}}
         \exp\!\left[
           2\pi i\!\left(
             \frac{n_{t}\,x^{4}}{L_{t}}
             + \frac{n_{r}\,x^{5}}{L_{r}}
           \right)
         \right],
   $$

   labelled by integers (n_t, n_r) and orthonormal under
   the flat measure on T².
3. **F11–F13** (Track 4): the (ε, s) parametrization of the
   internal metric,

   $$
   g_{ab}
   \;=\;
   \begin{pmatrix}
   \varepsilon^{2} & \varepsilon\,s \\[4pt]
   \varepsilon\,s & \tfrac{1}{\varepsilon^{2}} + s^{2}
   \end{pmatrix},
   \qquad
   \det g_{ab} = 1.
   $$

   Convention: index 4 is the *tube* direction, index 5 the
   *ring* direction; L_5 = ε L_4.
4. **Standard 4D Lorentz representation theory.**  The
   irreducible representations of the proper orthochronous
   Lorentz group SO⁺(1,3), labelled by (j₁, j₂) with j₁,
   j₂ non-negative half-integers, give scalars (0,0),
   left/right Weyl spinors (½,0)/(0,½), 4-vectors (½,½),
   etc.
5. **The Horoto–Scholtz Killing-eigenstate equation** for
   internal-symmetry-induced spin (their Eq. 191):

   $$
   \xi_{i}^{\nu}\,\partial_{\nu} A_{i\,\mu}
   \;+\; \partial_{\mu}\xi_{i}^{\nu}\,A_{i\,\nu}
   \;=\; 0,
   $$

   where {ξ_i} is a set of Killing vector fields forming a
   representation of some Lie algebra and A_{iμ} is a
   1-form invariant under the corresponding isometries.
   The matrix part of the transformation (∂_μ ξ_i^ν acting
   on the components A_iν) gives the spin operator.

Conventions: signature (−, +, +, +, +, +); index ranges as
in F4 (μ = 0,…,3 for spacetime; a, b = 4, 5 for compact);
"spin" means the eigenvalue of the Casimir J² = J·J of the
4D rotation subgroup of SO⁺(1,3) acting in the rest frame
of the eigenstate.

---

## Section A — What "spin" means for an eigenstate on T²

### A.1 — The operational definition

> *Purpose: state precisely what we are trying to derive,
> so that the success/failure of each route can be judged
> unambiguously.*

In standard 4D physics, the spin of a particle is the
eigenvalue (more precisely, j(j+1) ℏ²) of the Casimir
J² = J·J of the rotation subgroup SO(3) ⊂ SO⁺(1,3),
evaluated in the particle's rest frame.  Equivalently, the
particle's wavefunction transforms in some irreducible
(j₁, j₂) representation of SO⁺(1,3), and the spin is the
total angular momentum j = j₁ + j₂ (in the rest frame).

For an eigenstate of the photon-on-2-torus from F8, the
question "what is the spin?" is the question "in which
(j₁, j₂) representation does the eigenstate transform under
4D Lorentz?"

Two operationally different things are usually conflated
under "spin":

| Object | Generator | Casimir |
|--------|-----------|---------|
| **External spin** | SO(3) acting on x^μ (μ = 1,2,3) | J²_ext |
| **Internal angular momentum** | A subgroup of GL(N) acting on field components | J²_int |

In 4D field theory these two are linked because the field
components transform under both the spacetime rotation (their
arguments rotate) and an internal "matrix" rotation (their
components mix).  This is the content of Horoto–Scholtz Eq.
194: A_{iμ}(x) → A_{iμ}(x) + ε^j (∂_μ ξ_j^ν A_{iν} +
ξ_j^ν ∂_ν A_{iμ}).

The question splits into two:

- **(Q1)** Under 4D Lorentz, in which representation does
  the eigenstate Φ_{n_t, n_r} transform?
- **(Q2)** Is there an *additional* internal symmetry of T²
  that acts non-trivially on the eigenstate's components,
  contributing additional spin-like quantum numbers?

A.2 answers Q1 as a function of what kind of field we are
quantizing on T²; B–C answer Q2.

### A.2 — Spin depends on the field type, not just on the geometry

> *Purpose: separate the trivial part (spin from the field
> type alone) from the substantive part (spin from the
> internal geometry).*

Let Ψ_M^{...}(x^A) be a generic tensor or spinor field on
M⁴ × T² with index range A = (μ, a).  The **field type**
(scalar, vector, spinor, …) sets the trivial baseline for
its 4D Lorentz transformation:

| Field type on M⁴ × T² | 4D Lorentz rep of compact eigenstate |
|---|---|
| Scalar Ψ(x) | (0, 0) — spin-0 |
| 1-form A_M(x) → 4D part A_μ(x) | (½, ½) — spin-1 |
| 6D spinor ψ(x) → 4D Weyl pieces | (½, 0) ⊕ (0, ½) — spin-½ |
| 6D 2-form B_MN(x) → 4D part B_μν | (1, 0) ⊕ (0, 1) — spin-1, anti-symmetric |

The (n_t, n_r) labelling of the compact eigenstate is
**orthogonal** to the 4D Lorentz rep: the same compact mode
exists for any choice of higher-dimensional field type, and
the 4D Lorentz transformation acts on the 4D components of
the field, *not* on the (n_t, n_r) labels.

This makes the question well-posed.  *If* the only thing
quantized on T² is a scalar wave (the F8 ansatz), then the
4D-Lorentz spin of the resulting eigenstate is automatically
**zero** — every (n_t, n_r) eigenstate is a 4D scalar, and
no choice of T² geometry can change that.

To get higher spin, the higher-dimensional field type must
itself carry tensor or spinor structure.  The natural
question for MaSt is then:

> Which *higher-dimensional field type* should be quantized
> on M⁴ × T² to give an eigenstate that is electromagnetic
> charged, has the F11 mass spectrum, *and* has the 4D
> Lorentz spin appropriate to a known particle (½ for
> electrons, 1 for the photon, 0 for hypothetical scalars)?

For tracks 1–6, the answer was implicit:  use a 6D scalar
(Klein–Gordon field) to get the cleanest mass and charge
algebra.  This works for spin-0 particles (e.g., the Higgs,
or hypothetical scalar dark-matter candidates) but gives
nothing relevant to the electron, which is spin-½.

For the present derivation, the relevant higher-dimensional
field types are:

- **6D 1-form A_M** — gives spin-1 in 4D (covers the photon).
- **6D spinor ψ** — gives spin-½ in 4D (covers the electron).

Sections C and D treat these in turn.

### A.3 — The "spin from internal geometry" question, sharpened

The original motivating question — *can a scalar field on
a sheared T² produce spin-½ for some windings?* — is now
seen to reduce to:

> Can the internal geometry of T² provide an additional
> Killing-vector / holonomy structure that, combined with a
> 6D scalar Klein–Gordon field, transforms in a non-trivial
> 4D Lorentz representation?

This is the Horoto–Scholtz route applied to T².  Sections
B–E address it.  The answer is **no, for a single 2-torus**,
for two independent reasons (Killing-algebra obstruction in §D,
holonomy obstruction in §E).  This is the central technical
content of this derivation.

---

## Section B — Killing vectors of T² and their representations

### B.1 — The two commuting U(1) Killing vectors

> *Purpose: enumerate the isometries of T² with the (ε, s)
> metric and identify what algebraic structure they form.*

The 2-torus T² with the metric g_ab from F11 is *flat*: a
direct calculation of the Riemann tensor of the constant
metric

$$
g_{ab} \;=\;
\begin{pmatrix}
\varepsilon^{2} & \varepsilon\,s \\[4pt]
\varepsilon\,s & \tfrac{1}{\varepsilon^{2}} + s^{2}
\end{pmatrix}
$$

gives R^a_{bcd} = 0 identically, because all metric
components are constants on T² (no x^4 or x^5 dependence)
and so the Christoffel symbols Γ^a_{bc} = ½ g^{ad}(∂_b g_{cd}
+ ∂_c g_{bd} − ∂_d g_{bc}) all vanish.  The flat 2-torus
admits the maximal number of Killing vectors compatible
with its compactness: two translation generators

$$
\xi_{4} \;=\; \partial_{4},
\qquad
\xi_{5} \;=\; \partial_{5}.
$$

These satisfy the Killing equation L_{ξ_a} g_{cd} = 0
trivially (since g_{cd} is constant), and their Lie bracket
vanishes:

$$
[\xi_{4},\,\xi_{5}] \;=\; 0.
$$

So {ξ_4, ξ_5} forms an **abelian** Lie algebra,
isomorphic to u(1) ⊕ u(1) ≅ ℝ² (the Lie algebra of
U(1) × U(1)).

> *Note on the role of shear.*  The shear s ≠ 0 changes the
> *metric* of T² (and therefore the inner product on its
> tangent space, and therefore the lengths and angles of
> the closed cycles) but does not change the *isometry
> group*.  A constant-metric 2-torus has the same
> two-parameter abelian isometry group regardless of the
> values of g_44, g_55, g_45.  This is the first hint that
> the shear cannot generate a non-abelian structure of the
> kind needed for spin-½.

### B.2 — Eigenvalues of {ξ_4, ξ_5}: the (n_t, n_r) labels

> *Purpose: identify the U(1) × U(1) charges as the
> conserved internal momenta from F4, and confirm they
> label the F8 eigenstates.*

By Horoto–Scholtz Eq. 191, a 1-form A_iμ that is invariant
under ξ_a satisfies

$$
\xi_{a}^{c}\,\partial_{c} A_{i\,\mu}
\;+\; \partial_{\mu}\xi_{a}^{c}\,A_{i\,c}
\;=\; 0.
$$

The second term vanishes for ξ_a = ∂_a (no x-dependence
of the components ξ_a^c = δ_a^c), so the equation reduces
to

$$
\partial_{a} A_{i\,\mu} \;=\; 0
\quad\text{i.e.}\quad
\xi_{a} A \;=\; 0.
$$

For a momentum eigenstate Φ_{n_t, n_r} ∝ exp(2π i (n_t x^4
/L_t + n_r x^5/L_r)), this is replaced by the eigenvalue
equation:

$$
\xi_{4}\,\Phi_{n_{t}, n_{r}}
\;=\; \frac{2\pi i\,n_{t}}{L_{t}}\,\Phi_{n_{t}, n_{r}},
\qquad
\xi_{5}\,\Phi_{n_{t}, n_{r}}
\;=\; \frac{2\pi i\,n_{r}}{L_{r}}\,\Phi_{n_{t}, n_{r}}.
$$

So the (n_t, n_r) labels **are** the eigenvalues of the
two Killing vectors of T², up to the conventional 2π/L
factor.  Restoring physical units (P_a = ℏ × eigenvalue)
recovers F8: P_4 = n_t h/L_t, P_5 = n_r h/L_r.

### B.3 — These are charge-type, not spin-type

> *Purpose: state explicitly that the U(1) × U(1)
> eigenvalues are abelian phases, not spin matrices.*

The Horoto–Scholtz framework distinguishes two roles for
Killing-vector eigenstates:

- **Phase (abelian) part.**  A Killing vector ξ acts on
  the eigenstate as a phase: Ψ → e^{iα} Ψ.  The
  eigenvalue is a single complex number.  This is the
  origin of *charge* in their framework.
- **Matrix (non-abelian) part.**  Multiple Killing vectors
  with non-trivial Lie brackets [ξ_i, ξ_j] = C^k_{ij} ξ_k
  cannot be simultaneously diagonalized; they act on
  multiple field components as matrices τ_i.  This is the
  origin of *spin* in their framework.

For T², the two Killing vectors have *vanishing* Lie
brackets (B.1), so they fall entirely in the phase
category.  Their eigenvalues label *charge-type* quantum
numbers, not spin.  This is a direct application of the
Horoto–Scholtz dichotomy — and it tells us that spin from
T²'s isometries alone is mathematically impossible.

The next two sections quantify this.  §C handles the
positive case (spin-1 from a 1-form on T²), §D handles
the negative case (spin-½ requires non-abelian Killing
structure that T² lacks).

---

## Section C — Spin-1 from 1-form modes on T² (the positive result)

### C.1 — A 6D 1-form decomposed under M⁴ × T²

> *Purpose: produce a concrete spin-1 eigenstate on T² by
> using a 1-form (vector) field instead of a scalar.*

Let A_M(x^A) be a 6D 1-form on M⁴ × T².  The index M
ranges over both spacetime (μ = 0, …, 3) and compact (a =
4, 5) directions.  Decompose A_M into its 4D and compact
parts:

$$
A_{M} \;=\; (A_{\mu},\;A_{a})
\;=\; (A_{0}, A_{1}, A_{2}, A_{3},\;A_{4}, A_{5}).
$$

Under 4D Lorentz, the spacetime block A_μ transforms as a
4-vector (½, ½) representation, while A_4 and A_5 are 4D
scalars (one per compact direction).

> *Note.*  The 6D 1-form A_M is the natural higher-dimensional
> generalization of the 4D photon.  It carries no extra
> structure — it is the simplest non-scalar field on M⁴ × T²
> after the Klein–Gordon scalar Ψ used in derivations 1–6.
> Below we expand it in T² compact modes and read off the
> 4D spin of each mode independently.

### C.2 — Compact-mode expansion

> *Purpose: write each component of A_M as a sum over the
> F8 eigenstates and check that the (n_t, n_r) labels carry
> over.*

For each component A_M, expand in the F8 basis:

$$
A_{\mu}(x^{\nu}, x^{4}, x^{5})
\;=\; \sum_{n_{t}, n_{r}}
        A_{\mu;\,n_{t}, n_{r}}(x^{\nu})\,
        \Phi_{n_{t}, n_{r}}(x^{4}, x^{5}),
$$

and similarly for A_a.  The 4D fields A_{μ; n_t, n_r}(x^ν)
are now ordinary 4D vector fields, one per (n_t, n_r)
sector.  The compact-mode wavefunctions Φ are 4D scalars
(they depend only on x^4, x^5).

The U(1) × U(1) Killing eigenvalues (B.2) act on the
*compact-mode wavefunction* Φ, not on the 4D components
A_μ.  So:

- The (n_t, n_r) labels carry the U(1) × U(1) charges
  exactly as in §B (and as in F4 / F14: P_4 generates
  electromagnetic charge in the tube-couples convention).
- The 4D Lorentz structure is determined by the 4D
  index μ, independently of (n_t, n_r).

### C.3 — 4D Lorentz transformation of the (n_t, n_r) sector

> *Purpose: read off the spin of each (n_t, n_r) sector.*

A 4D Lorentz transformation Λ ∈ SO⁺(1, 3) acts on x^μ but
leaves x^4, x^5 unchanged (they are inert under 4D Lorentz
in the cylinder-condition setting; F4).  The transformation
of A_M is the standard 1-form rule applied only to the 4D
indices:

$$
A'_{\mu}(\Lambda x^{\nu}, x^{4}, x^{5})
\;=\; (\Lambda^{-1})^{\rho}{}_{\mu}\,
       A_{\rho}(x^{\nu}, x^{4}, x^{5}),
\qquad
A'_{a}(\Lambda x^{\nu}, x^{4}, x^{5})
\;=\; A_{a}(x^{\nu}, x^{4}, x^{5}).
$$

In each (n_t, n_r) sector, the compact mode Φ is a scalar
under Λ, so the transformation reduces to:

$$
A'_{\mu;\,n_{t}, n_{r}}(\Lambda x^{\nu})
\;=\; (\Lambda^{-1})^{\rho}{}_{\mu}\,
       A_{\rho;\,n_{t}, n_{r}}(x^{\nu}),
$$

$$
A'_{a;\,n_{t}, n_{r}}(\Lambda x^{\nu})
\;=\; A_{a;\,n_{t}, n_{r}}(x^{\nu}).
$$

So:

- A_{μ; n_t, n_r} transforms as a 4-vector — i.e., in the
  (½, ½) representation of SO⁺(1, 3) — i.e., **spin-1**.
- A_{a; n_t, n_r} (one for each a = 4, 5) transforms as a
  4D scalar — i.e., in the (0, 0) representation —
  i.e., **spin-0**.

This is exactly the Horoto–Scholtz §5 spin-1 derivation
(their Eq. 215–220), now applied to the compact-mode
expansion on T².  The novel part for MaSt is the
labelling: the spin-1 mode comes with two additional
internal quantum numbers (n_t, n_r), which by F11 set its
mass and by F14 set its charge.

### C.4 — Result: spin-1 carrier on T² is fully determined

> *Purpose: state the result for the spin-1 sector
> compactly.*

Each (n_t, n_r) sector of A_μ on M⁴ × T² is a 4D field of:

- Spin **j = 1** (from C.3).
- Mass **m²c² = h^{ab} P_a P_b** with P_a = (n_t h/L_t,
  n_r h/L_r) (from F7).
- Charge **Q = e × n_t** under the tube-couples convention
  (from F14).

Together, these are precisely the quantum numbers of a
*massive* photon-like state with charge.  The masslessness
of the physical photon corresponds to (n_t, n_r) = (0, 0)
— the only sector with zero compact momentum and therefore
zero 4D rest mass.  All higher (n_t, n_r) sectors are
massive vector bosons.  The (1, 0) sector with positive n_t
is a charged massive vector boson, like a W⁺ in form
(though with mass set by L_t, not by electroweak scales).

This is a clean derivation of spin-1 from photon-on-2-torus,
and a successful application of the Horoto–Scholtz framework
to MaSt's compactification.

> **Box: Lemma F20 (spin-1 sector of T²).**  A 6D 1-form
> A_M on M⁴ × T² decomposes into 4D (n_t, n_r) sectors that
> are massive spin-1 vector bosons with mass and charge
> given by F7 and F14, respectively.  The spin-1 character
> follows from the 4-vector index μ; the (n_t, n_r) labels
> are the U(1) × U(1) charge eigenvalues from §B and are
> orthogonal to the 4D spin assignment.

---

## Section D — The Killing-vector route does not produce spin-½ on T²

### D.1 — What Horoto–Scholtz's spin-½ construction requires

> *Purpose: state precisely what algebraic structure
> Horoto–Scholtz §5 spin-½ uses, so we can check whether
> T² provides it.*

In Horoto–Scholtz's §5, the spin-½ derivation (their Eq.
221–227) requires:

1. **Three Killing vector fields** {ξ_1, ξ_2, ξ_3} of the
   form ξ_i = C^μ_{iν} x^ν ∂_μ.
2. **Their Lie brackets close as so(3)**:

   $$
   [\xi_{i},\,\xi_{j}] \;=\; \varepsilon^{k}{}_{ij}\,\xi_{k}.
   $$

3. **The associated matrices τ_i** with components τ_i^ν_μ
   = i C^ν_{iμ} are anti-symmetric and have **only two
   distinct eigenvalues**, so they form the **2-dimensional
   (spin-½) representation of su(2)**.

Their explicit Killing vectors (their Eq. 224) are

$$
\xi_{i} \;=\; \tfrac{1}{2}
   \!\left(
     x^{5}\,\partial_{i} - x^{i}\,\partial_{5}
     + \varepsilon^{k}{}_{ij}\,x^{j}\,\partial_{k}
   \right),
$$

with i, j, k running over 1, 2, 3.  The first two terms
*mix the internal direction x^5 with the spatial directions
x^i*.  This mixing is essential — without it, the Lie
brackets do not close as so(3), and the τ matrices do
not have the right eigenvalue structure for spin-½.

The Killing vectors live on a 4D Euclidean space (the
unit 3-sphere S³ embedded in ℝ^4 via the constraint
(x^1)² + (x^2)² + (x^3)² + (x^5)² = 1), with the natural
Hopf coordinates (β, α, γ) bringing them into a canonical
form (their Eq. 228).

### D.2 — Why these Killing vectors do not exist on T²

> *Purpose: show explicitly that Horoto–Scholtz's spin-½
> generators have no analog on T².*

For Horoto–Scholtz's ξ_i to exist on M⁴ × T² with x^5 a
compact ring coordinate, we would need x^5 to mix with
the *spatial* components x^i (i = 1, 2, 3) via Killing
vectors of the form ξ_i = (1/2)(x^5 ∂_i − x^i ∂_5 + …).

For ξ_i to be a Killing vector of the metric on M⁴ × T²,
the Killing equation L_{ξ_i} G_{AB} = 0 must hold.  Two
problems arise:

1. **The mixing term x^5 ∂_i changes the spatial
   coordinates by an amount proportional to x^5.**  Since
   x^5 is compact (range [0, L_5)), this generates only
   bounded translations.  Unbounded — actually
   *Killing-vector* — translations of x^i by amounts
   continuous over the entire 4D spatial range require x^5
   to be unbounded (extended like a position coordinate
   in ℝ^4 Euclidean), not compact.
2. **The mixing term −x^i ∂_5 attempts to shift the
   compact x^5 by an amount proportional to x^i.**  For
   this to be a true Killing vector of T² (which requires
   single-valued action on the compact x^5), the shift
   must be an integer multiple of L_5 — *uniformly* in
   x^i, which forces x^i = 0.

So: the mixing structure that Horoto–Scholtz use to generate
the so(3) brackets on S³ is **incompatible with x^5 being a
compact direction**.  This is not a calculational
difficulty; it is a structural obstruction.  T²'s Killing
algebra is u(1) ⊕ u(1) (B.1), and there is no way to
extend it to so(3) without de-compactifying x^5 (turning
T² into ℝ²) or adding additional manifold structure.

### D.3 — Lie algebra dimension count, summarized

> *Purpose: a one-paragraph version of D.2 for
> reference.*

The minimum requirement for Horoto–Scholtz's spin-½
construction is three Killing vector fields whose Lie
brackets close as so(3).  T² admits exactly **two** Killing
vectors (B.1); they commute, forming the abelian Lie
algebra u(1) ⊕ u(1).  No subset, extension, or combination
of these two abelian generators can satisfy the
non-abelian so(3) brackets.  This is a finite-dimensional
linear algebra fact, independent of choice of metric on
T² (the shear s and aspect ratio ε do not change the
Killing algebra; B.1 note).

> **Box: Lemma F21 (Killing-vector obstruction to spin-½ on
> T²).**  The Killing algebra of any constant-metric flat
> T² is u(1) ⊕ u(1), regardless of the shear s and aspect
> ratio ε.  This algebra is abelian and 2-dimensional.
> Horoto–Scholtz's geometric spin-½ construction requires a
> 3-dimensional non-abelian Killing algebra (so(3)).  No
> such algebra exists on T², so spin-½ cannot arise from
> Killing-vector eigenstates on a single 2-torus.

---

## Section E — The holonomy / Berry-phase route does not produce spin-½ on T²

### E.1 — What a "spin-½ holonomy" would have to look like

> *Purpose: state the operational test for the holonomy /
> Berry-phase mechanism, so we can check it concretely.*

Even without an so(3) Killing structure, a *topological*
mechanism could in principle produce a (−1) phase under a
2π rotation — the operational signature of a spinor.  The
candidate mechanism (the original pool-item-f hypothesis)
is:

> Parallel-transport a tangent frame around a closed loop
> γ on T² in the presence of the shear g_45 = εs.  If the
> resulting holonomy h(γ) is a rotation by an *odd*
> multiple of π (i.e., h(γ) = e^{iπ × odd} = −1 in some
> 2-component representation), then a spinor field on T²
> picks up a (−1) phase on traversing γ.  For windings
> consistent with MaSt's parity-of-tube rule, this would
> reproduce the empirical electron spin assignment.

The operational test is: **compute the Levi-Civita
holonomy of the metric in F11 around the basic cycles γ_t
(tube) and γ_r (ring) of T², and ask whether the result is
a non-trivial element of SO(2) for any (ε, s)**.

### E.2 — The Levi-Civita connection on a flat 2-torus

> *Purpose: compute the connection 1-forms of T² with the
> sheared metric and confirm they vanish.*

For the metric g_ab from F11, the Christoffel symbols are

$$
\Gamma^{a}{}_{bc}
\;=\; \tfrac{1}{2}\,g^{ad}
       \left(
         \partial_{b} g_{cd}
         + \partial_{c} g_{bd}
         - \partial_{d} g_{bc}
       \right).
$$

All metric components g_44, g_55, g_45 are constants
(independent of x^4 and x^5 — this is the cylinder
condition on T² itself, separate from the 4D cylinder
condition on g_μν).  Therefore every partial derivative
∂_b g_{cd} = 0, and

$$
\Gamma^{a}{}_{bc} \;=\; 0
\qquad\text{for all } a, b, c \in \{4, 5\}.
$$

The connection 1-forms

$$
\omega^{a}{}_{b} \;=\; \Gamma^{a}{}_{bc}\,dx^{c}
\;=\; 0
$$

vanish identically.  The Riemann tensor

$$
R^{a}{}_{bcd}
\;=\; \partial_{c}\Gamma^{a}{}_{bd} - \partial_{d}\Gamma^{a}{}_{bc}
   + \Gamma^{a}{}_{ce}\Gamma^{e}{}_{bd}
   - \Gamma^{a}{}_{de}\Gamma^{e}{}_{bc}
\;=\; 0
$$

vanishes identically — confirming what was already noted in
B.1: the sheared T² is flat.

### E.3 — Holonomy of a flat connection on a flat torus

> *Purpose: compute the holonomy around the basic cycles
> and confirm it is the identity.*

The holonomy of parallel transport along a closed curve γ
is

$$
h(\gamma) \;=\; \mathcal{P}\!\exp\!\left(
   -\!\oint_{\gamma}\,\omega
\right),
$$

where 𝒫 denotes path-ordering.  With ω^a_b = 0
everywhere (E.2), this reduces to

$$
h(\gamma) \;=\; \mathcal{P}\,\exp(0) \;=\; \mathbb{1}
$$

for **any** closed curve γ on T², including the basic
cycles γ_t (constant x^5, x^4 traversing [0, L_t]) and γ_r
(constant x^4, x^5 traversing [0, L_r]).  The holonomy is
the identity element of the rotation group, regardless of
the values of (ε, s).

Equivalently: the connection is flat, the manifold is
simply connected when lifted to its universal cover (the
plane ℝ²), and any flat connection on a manifold has
trivial holonomy along contractible loops.  The basic
cycles of T² are not contractible, but their non-triviality
manifests in the global topology (π_1(T²) = ℤ × ℤ), not in
the local connection — and for a flat connection, the
holonomy depends only on the connection, not on the global
topology.

> *Subtlety.*  A non-flat metric on T² (e.g., one where
> g_ab depends on x^4 and x^5) could produce non-trivial
> holonomy.  But such a metric breaks the cylinder
> condition that the entire MaSt construction (F4 onward)
> depends on for charge conservation, mass quantization,
> and the F11 mass formula.  Allowing g_ab(x^4, x^5)
> would also remove the U(1) × U(1) Killing structure
> (B.1), invalidating the F14 charge identification.  So
> the holonomy alternative is locked out by the same
> structural choices that make F4–F19 work.

### E.4 — π_1(T²) is abelian — no Z₂ quotient

> *Purpose: explain the topological reason why the
> obstruction is fundamental, not removable by a different
> connection choice.*

For a manifold M, the existence of "fermionic" (spin-½
type) field configurations is governed by H¹(M, ℤ₂) — the
first cohomology with ℤ₂ coefficients, which classifies
the inequivalent ℤ₂ flat bundles.  Equivalently, it is
governed by group homomorphisms π_1(M) → ℤ₂.

For T², π_1(T²) = ℤ × ℤ.  The non-trivial homomorphisms
ℤ × ℤ → ℤ₂ are:

- (n_t, n_r) ↦ n_t mod 2  (parity of tube winding)
- (n_t, n_r) ↦ n_r mod 2  (parity of ring winding)
- (n_t, n_r) ↦ (n_t + n_r) mod 2  (parity of total winding)

So the abstract topological structure *would* support a
"parity of n_t" assignment — exactly MaSt's empirical rule.
However, picking out one of these three homomorphisms as
the "physical" one requires **additional structure** — a
choice of spin structure on T².  The choice is not unique
(there are four distinct spin structures on T²), and none
of them is selected by the metric alone.

For the choice to be physically meaningful — i.e., for it
to act on a wavefunction with the (−1) under 2π rotation
that defines a spinor — the rotation must be the action of
**an external symmetry** that is somehow linked to the
internal cycle.  On a Riemannian manifold this link is
provided by the spin connection lifted to the spin bundle.
But for a flat metric the spin connection vanishes (E.3),
so no link exists.

The conclusion: T² admits ℤ₂ flat bundles, but none of
them is induced by the metric.  The choice of spin
structure is an **extra** input, not determined by the
geometric data (g_ab) of MaSt's framework.

### E.5 — Neither shear nor aspect ratio changes the verdict

> *Purpose: emphasize that the obstruction does not depend
> on the parameters (ε, s) — it is a structural fact
> about T².*

Throughout E.1–E.4, the argument made no use of the
specific values of ε and s, only of the fact that the
metric is constant on T² (no x^4, x^5 dependence).  This
constancy is precisely the cylinder condition that all of
F4–F19 invokes.  As long as F4 holds, the holonomy
mechanism is blocked for **every** choice of (ε, s), not
just for some special values.

> **Box: Lemma F22 (holonomy obstruction to spin-½ on T²).**
> For any constant-metric (flat, cylinder-condition) 2-torus,
> the Levi-Civita connection vanishes identically and the
> holonomy of parallel transport around any closed loop
> on T² is trivial.  No choice of shear s or aspect ratio
> ε produces a (−1) phase under transport along the basic
> cycles.  The topological prerequisite for spin-½ (a
> non-trivial ℤ₂ flat bundle linked to the metric) is not
> provided by T² alone; the four available spin structures
> on T² are independent of the metric and must be chosen
> as additional input.

---

## Section F — Verdict and path forward

### F.1 — Summary of what is and is not derived

> *Purpose: state the clean bottom line.*

After Tracks 1–7, the Program 1 single-sheet picture is:

| Quantity | Mechanism | Status |
|---|---|---|
| Mass | Compact momentum of confined photon (F7, F11) | **Derived** |
| Charge | Killing eigenvalue of tube direction (F14) | **Derived** |
| Lorentz force coupling | Geodesic of standing-wave centroid (F17) | **Derived** |
| Spin-1 sector | 1-form on T² + 4D Lorentz (F20) | **Derived** |
| **Spin-½ sector** | (a) Killing-vector route (F21) | **Blocked** |
|   | (b) Holonomy / Berry-phase route (F22) | **Blocked** |
| Magnetic moment | Corollary of charge + spin (gated by spin-½) | Pending spin-½ |

The spin-½ blockage is a real, structural fact about flat
T², not a calculational difficulty.  It does not invalidate
F1–F20 — those derivations all hold.  It does mean that
MaSt's empirical "odd n_t → spin-½" rule cannot be
derived from a single sheared 2-torus by the holonomy or
Killing-vector mechanisms.  The rule is therefore either an
empirical constraint of unknown geometric origin, or a
consequence of structure beyond a single T² (next
subsection).

### F.2 — Three geometric extensions that could produce spin-½

The standard literature on spin-½ from compactification
points to three distinct mechanisms.  Each requires
extending the geometry beyond a single 2-torus.

**Option 1 — Larger internal manifold (S³ or larger).**
The Horoto–Scholtz approach (their Eq. 224–227): take the
internal space to be the unit 3-sphere S³ embedded in 4D
Euclidean space via Hopf coordinates.  The SU(2) × SU(2)
isometry of S³ contains the so(3) Killing structure that
their spin-½ derivation requires.  *Cost for MaSt*: 4D
internal space (instead of 2D), changing the dimension of
the total spacetime from 6 to 7 per sheet, and triple
that for the three-sheet T⁶ → T⁶ × S³ structure.  Also,
S³ does not naturally split into "tube" and "ring" cycles
the way T² does — MaSt's mass and charge formulas would
need to be re-derived in the new geometry.  **Verdict for
MaSt**: high cost, large structural change; only worth
pursuing if no other option works.

**Option 2 — Cross-sheet coupling on the full T⁶.**  MaSt's
full geometry is M⁴ × T² × T² × T² (three 2-tori, one per
sheet) with cross-shears between sheets (R54).  The Killing
structure of T⁶ is u(1)⁶ on its own, but **cross-shears
that mix coordinates across sheets** can in principle
generate non-abelian relations between the per-sheet
Killing vectors.  Specifically, if a cross-shear ξ between
the e-sheet tube (∂_4^{(e)}) and the ν-sheet tube
(∂_4^{(ν)}) creates an effective generator
∂_4^{(e)} + ξ ∂_4^{(ν)}, the algebra of all such generators
across the 6 compact directions might close as a non-abelian
Lie algebra of dimension ≥ 3.  This is **plausible but not
yet shown**, and would be a substantial calculation.
*Cost for MaSt*: stays within the existing T⁶ framework;
requires a careful enumeration of which cross-shear
combinations close as su(2).  **Verdict for MaSt**:
the most natural option to pursue.

**Option 3 — Wess–Zumino–Witten topological term.**  A
WZW term added to the Lagrangian of a scalar field on T²
can effectively quantize the field as a fermion (this is
how the Skyrme model produces nucleons as fermions from a
bosonic chiral Lagrangian).  The relevant homotopy is
π_3(target space) → ℤ; for T² as the target, π_3(T²) = 0,
so the WZW term is identically zero and does not produce
fermions.  **Verdict for MaSt**: not viable for a single
T² target; would require a target with π_3 ≠ 0 (e.g.,
SU(2) ≅ S³).

### F.3 — Consequences for the empirical "odd n_t → spin-½" rule

The empirical parity-of-tube-windings rule that the MaSt
particle-classification work has used to assign spin-½ to
specific eigenstates is, given F21 and F22, **not a
consequence of the single-sheet 2-torus geometry**.  Three
options remain consistent with the rule's empirical
success:

1. **The rule is genuinely cross-sheet.**  The full MaSt
   geometry is M⁴ × T⁶ with cross-shears between the three
   sheets.  Cross-sheet structure can in principle generate
   the non-abelian Killing closure that single-sheet T²
   lacks (Option 2, F.2).  In this case, the parity-of-n_t
   rule would emerge as the projection of a cross-sheet
   spin-½ assignment onto the per-sheet quantum numbers.
   This is the explanation most consistent with MaSt's
   existing structure.

2. **The rule reflects an additional internal direction
   not yet in MaSt's geometry.**  Adopting Option 1 (F.2),
   each MaSt sheet would be replaced by T² × S¹ or by S³,
   with the additional direction providing the Killing
   structure needed for spin-½.  This would change the
   per-sheet dimension count from 2 to 3 or 4 and require
   re-deriving F7 / F11 / F14 in the new geometry.

3. **The rule is an empirical input not derivable from
   geometry.**  In this case, the parity-of-n_t rule
   stands as a postulate of the classification machinery,
   on the same footing as the per-sheet Ma–S coupling
   signs (σ_e, σ_ν, σ_p) that F14 also identified as
   empirical inputs.  This is the conservative reading
   and is consistent with the present level of derivation.

Of these, option 1 is structurally the smallest extension
and is the one this derivation recommends pursuing next.
Until that pursuit is carried out, the spin-½ assignment
should be treated as an empirical input on the same
footing as σ_e, σ_p — explicit in the model, but not yet
derived from first principles.

### F.4 — Why the negative result is informative

> *Purpose: argue that F22 is a useful result, not a
> disappointment.*

A naive reading of the original motivating hypothesis —
"spin-½ from sheared T² holonomy" — might suggest a
routine calculation waiting to be done.  This derivation
shows it is not — it is structurally blocked, and the
block has a clear topological origin (π_1(T²) abelian;
flat T² has trivial Levi-Civita holonomy; the four ℤ₂
spin structures on T² are not metric-induced).

The value of finding this out cleanly is that the
program's strategic direction can be set with full
information.  In particular:

- The magnetic-moment derivation is **gated**, not just
  "next" — it cannot proceed without first resolving
  spin-½, since the Lorentz-covariance argument that
  produces a magnetic moment from charge requires a
  non-zero spin to produce a moment proportional to.
- The case for studying cross-sheet coupling on the full
  three-sheet T⁶ is **strengthened** — that geometry is
  now the most natural place to look for spin-½, not just
  an aesthetic generalization.
- Other open questions (the Klein-scale issue, the
  Program-1 closeout) are unaffected by F21–F22.

The Horoto–Scholtz paper's central insight — that *charge
and spin are the same concept, distinguished by external
vs. internal symmetry* — also gains operational meaning in
this context: MaSt's failure to produce spin-½ from T²
alone is precisely the "internal symmetry isn't large
enough" failure that their framework would predict for
any internal space with abelian isometry group.  The fix
in their framework is to enlarge the internal symmetry
(Option 1).  The fix in MaSt's framework is more naturally
to invoke the cross-sheet structure that their framework
does not address (Option 2).  Both directions are
informed by the negative result derived here.

---

## Lemma (Track 7 result)

We have shown:

> **(F20) Spin-1 sector of T².**  A 6D 1-form A_M on
> M⁴ × T² decomposes into 4D (n_t, n_r) sectors that are
> massive spin-1 vector bosons.  In each sector, the spin
> is set by the 4-vector index μ (transformation in the
> (½, ½) representation of SO⁺(1, 3) — independent of the
> compact-mode labels), the mass by F7 / F11 (m²c² =
> h^{ab} P_a P_b), and the charge by F14 (Q = e n_t under
> the tube-couples convention).  The (0, 0) sector is
> massless and uncharged — the physical photon, recovered
> as a special case.  The construction is the Horoto–
> Scholtz §5 spin-1 derivation applied to the M⁴ × T²
> compactification.
>
> **(F21) The Killing-vector mechanism does not produce
> spin-½ on T².**  The Killing algebra of any
> constant-metric flat 2-torus is u(1) ⊕ u(1), regardless
> of the shear s and aspect ratio ε.  This algebra is
> abelian and 2-dimensional.  Horoto–Scholtz's geometric
> spin-½ construction (their Eq. 221–227) requires a
> 3-dimensional non-abelian Killing algebra (so(3)).  No
> such algebra exists on T² alone, so spin-½ cannot arise
> from Killing-vector eigenstates on a single 2-torus by
> the Horoto–Scholtz mechanism.  This is a statement about
> the *mechanism*, not about whether spin-½ fields can
> exist on T² at all — see F22.
>
> **(F22) Levi-Civita holonomy is trivial on T², but T²
> admits spin-½ fields under an external spin-structure
> choice.**  For any constant-metric (flat,
> cylinder-condition) 2-torus, the Levi-Civita connection
> vanishes identically.  The holonomy of parallel
> transport around any closed loop on T², including the
> basic cycles γ_t and γ_r, is the identity element of
> the rotation group, regardless of the values of the
> shear s and aspect ratio ε.  No phase of the form
> (−1)^{n_t} can be generated by Levi-Civita parallel
> transport on T².  However, T² admits four inequivalent
> ℤ₂ spin structures (one per homomorphism π₁(T²) = ℤ×ℤ →
> ℤ₂), so spin-½ fields *do* exist on T² once a spin
> structure is chosen as an additional input; the metric
> alone simply does not pick one out.  The physical
> content of F22 is therefore:  MaSt's empirical
> parity-of-tube-windings rule for spin-½ is not
> determined by the 2-torus metric, and must be traced
> either to a spin-structure choice, to a field-level
> mechanism (see derivation-7b), or to a feature of the
> larger T⁶ geometry (see F23).
>
> **(F23) Path forward for spin-½ in MaSt.**  Three
> geometric extensions are available:  (a) replace T²
> with S³ (Horoto–Scholtz's choice; high structural
> cost), (b) invoke cross-sheet coupling on T⁶ — the
> non-abelian closure of cross-sheared Killing generators
> across MaSt's three sheets is a candidate for an
> emergent so(3) algebra (low structural cost; the
> natural next direction within MaSt's existing
> framework), or (c) introduce a Wess–Zumino topological
> term (not viable for T² as target since π_3(T²) = 0).
> Option (b) is the most natural for MaSt to pursue.

F20 closes the spin-1 sector of the photon-on-2-torus
picture cleanly.  F21–F22 establish that spin-½ is not
determined by the sheared-2-torus metric alone: the
Killing and Levi-Civita mechanisms tested here cannot
produce it, though T² does admit spin-½ fields once a
spin structure is supplied as an external input.  F23
identifies cross-sheet coupling on the full T⁶ as the
most natural route forward for a *geometric* derivation
of spin-½ within MaSt.  Derivation 7b takes an
independent, field-polarization route on the same T²
and arrives at the Williamson–van der Mark ratio rule
s = n_t/n_r; the two derivations should be read
together.
