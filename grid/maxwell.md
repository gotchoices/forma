# Deriving Maxwell's Equations from the GRID Lattice

Starting from axioms A1–A4 and A6 of the
[foundations](foundations.md), this document derives all four of
Maxwell's equations without importing any electrodynamics.

All work is in natural units (c = ℏ = 1).

### Reading guide: index notation

This derivation uses **index notation**, standard in field theory.
A few conventions to keep in mind:

- **Greek indices** (μ, ν, ρ, ...) run over all four spacetime
  directions: 0 = time, 1 = x, 2 = y, 3 = z.
- **Latin indices** (i, j, k) run over the three spatial
  directions only: 1, 2, 3.
- **∂_μ** means "partial derivative with respect to coordinate
  x^μ."  So ∂₀ = ∂/∂t, ∂₁ = ∂/∂x, etc.
- **Repeated indices** imply summation.  For example,
  ∂_μ F^μν means ∂₀F^{0ν} + ∂₁F^{1ν} + ∂₂F^{2ν} + ∂₃F^{3ν}.
  (Einstein summation convention.)
- **Subscripts vs superscripts** (F_μν vs F^μν): these differ by
  signs from the metric.  The Minkowski metric η = diag(−1,+1,+1,+1)
  flips the sign of the time component when raising or lowering.
  For spatial indices, F^{ij} = F_{ij} (no sign change).  For mixed
  indices, F^{0i} = −F_{0i} (sign flip from the −1 in the time slot).
  Operationally: raising a time index costs a minus sign.

---

## Axioms used

Five of the six GRID axioms enter this derivation
(see [foundations.md](foundations.md) for full statements):

**A1. Four-dimensional causal lattice.**
Space is a regular array of cells in four dimensions, grain
size L = 1 (Planck length).  Disturbances propagate at one cell
per time step (speed of light c = 1).

**A2. Lorentzian signature (1,3).**
One dimension is timelike (causal ordering, forward only).
Three are spatial.  Metric: η_μν = diag(−1, +1, +1, +1).

**A3. Periodic internal phase.**
Each cell carries a phase θ ∈ [0, 2π).  Only phase differences
between neighboring cells are physical — the absolute phase at
any cell is unobservable.

**A4. Local gauge invariance.**
The physics is unchanged under arbitrary local relabeling of
the phase: θ(x) → θ(x) + χ(x), for any function χ(x).

**A6. Electromagnetic coupling α ≈ 1/137.**
The strength of the interaction between charged matter and the
electromagnetic field is set by a single measured constant, the
fine-structure constant.  The elementary charge is
e = √(4πα) ≈ 0.303 in natural units.

**Not used:** A5 (resolution ζ = 1/4).  Maxwell does not
depend on the information content of the lattice.

## What we do NOT assume

We do not assume electric or magnetic fields, charge, current,
ε₀, μ₀, or any field equation.  These will all emerge.

---

## Step 1: The phase field and its gradient

Zoom out far beyond the grain size.  The discrete phases on
individual cells blur into a smooth **scalar phase field**
θ(x), where x = (t, x¹, x², x³) labels a spacetime point.

The phase difference between neighboring cells at positions x
and x + dx becomes, in the continuum limit, the **gradient**:

<!-- ∂_μ θ = (∂θ/∂t, ∂θ/∂x¹, ∂θ/∂x², ∂θ/∂x³) -->
$$
\partial_\mu\theta
  = \Bigl(\frac{\partial\theta}{\partial t},\;
          \frac{\partial\theta}{\partial x^1},\;
          \frac{\partial\theta}{\partial x^2},\;
          \frac{\partial\theta}{\partial x^3}\Bigr)
$$

Here μ runs over {0, 1, 2, 3} labeling the four spacetime
directions.  The index is lowered using the Minkowski metric
η_μν = diag(−1, +1, +1, +1) from axiom A2.

At this stage θ is a real-valued field and ∂_μθ encodes
the local pattern of phase variation.  No physics yet — just
bookkeeping.

---

## Step 2: Gauge invariance demands a connection

Axiom A4 says the physics is unchanged under a local relabeling:

<!-- θ(x) → θ(x) + χ(x) -->
$$
\theta(x) \;\to\; \theta(x) + \chi(x)
$$

Under this transformation the gradient shifts:

<!-- ∂_μ θ → ∂_μ θ + ∂_μ χ -->
$$
\partial_\mu\theta \;\to\; \partial_\mu\theta + \partial_\mu\chi
$$

So ∂_μθ is **not** gauge-invariant — it changes when we
relabel.  Any physical quantity built from θ must be insensitive
to χ.

The remedy: introduce a **connection** A_μ(x) — a field that
lives on the links between cells and tells us how to compare
phases at neighboring cells despite arbitrary relabeling.
(Think of it as a "translation table" attached to each link.)
A_μ transforms as:

<!-- A_μ → A_μ + (1/e) ∂_μ χ -->
$$
A_\mu \;\to\; A_\mu + \frac{1}{e}\,\partial_\mu\chi
$$

where e is a coupling constant (to be identified with the
elementary charge).  Then the **covariant derivative**:

<!-- D_μ θ = ∂_μ θ − e A_μ -->
$$
D_\mu\theta = \partial_\mu\theta - e\,A_\mu
$$

is gauge-invariant:

<!-- D_μ θ → (∂_μ θ + ∂_μ χ) − e(A_μ + (1/e)∂_μ χ) = D_μ θ -->
$$
D_\mu\theta \;\to\;
  (\partial_\mu\theta + \partial_\mu\chi)
  - e\Bigl(A_\mu + \tfrac{1}{e}\,\partial_\mu\chi\Bigr)
  = D_\mu\theta
$$

On the discrete lattice, A_μ lives on the **links** between
cells.  Gauge invariance *demands* its existence — without it,
there is no way to compare phases at different cells in a
relabeling-invariant way.

A_μ is **part of the grid's state**, not a separate entity
floating above it.  The grid stores two kinds of information:

- **Cell phases** θ — the state at each node (matter)
- **Link phases** φ = eA_μL — the state on each connection
  (the electromagnetic field)

Both are part of what the grid holds.  A_μ is not a new
parameter (knob) — the only knob remains α.  It is part of the
grid's memory, determined at each point by the equations of
motion (Step 6).

The link phases modulate how neighboring cells interact — they
are dynamic coupling rules that the grid updates as it evolves.
A propagating wave in the link phases IS light.  A photon IS a
ripple in the grid's link states.  Maxwell's equations (derived
below) are the update rules for these link states.

The link state is not determined by the cell state.  If it
were (a "pure-gauge" configuration where A_μ = ∂_μθ/e), then
F_μν would vanish everywhere — no electromagnetic field, no
radiation, no photons.  The link phases carry independent
information, which is why the grid can store and transmit
electromagnetic energy.

---

## Step 3: The field tensor from closed loops

A_μ itself is not gauge-invariant (it shifts by ∂_μχ/e).  To
find the physical content, look at what happens around a
**closed loop**.

Consider a small rectangular loop in the μ-ν plane (a
"plaquette" in lattice language).  Transport the phase around
the loop: the accumulated connection going one way minus the
other way gives:

<!-- F_μν = ∂_μ A_ν − ∂_ν A_μ -->
$$
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu
$$

This is the **electromagnetic field tensor**.  Under a gauge
transformation:

<!-- F_μν → ∂_μ(A_ν + (1/e)∂_ν χ) − ∂_ν(A_μ + (1/e)∂_μ χ) = F_μν -->
$$
F_{\mu\nu} \;\to\;
  \partial_\mu\bigl(A_\nu + \tfrac{1}{e}\,\partial_\nu\chi\bigr)
  - \partial_\nu\bigl(A_\mu + \tfrac{1}{e}\,\partial_\mu\chi\bigr)
  = F_{\mu\nu}
$$

because partial derivatives commute: ∂_μ∂_νχ = ∂_ν∂_μχ.
The field tensor is gauge-invariant.  It is the **physical**
content of the lattice — the twist that cannot be removed by
any relabeling.

F_μν is antisymmetric: F_μν = −F_νμ.  In four dimensions this
gives 4×3/2 = **6 independent components**.

---

## Step 4: Identifying E and B

The (1,3) signature (A2) splits the six components of F_μν
into two groups: those involving the time index (μ = 0 or
ν = 0) and those that are purely spatial.

**Electric field** — the time-space components:

<!-- E_i = F_{0i} for i = 1, 2, 3 -->
$$
E_i = F_{0i} \qquad (i = 1,\,2,\,3)
$$

Explicitly: E₁ = ∂₀A₁ − ∂₁A₀, and similarly for E₂, E₃.

**Magnetic field** — the space-space components:

<!-- B_i = −(1/2) ε_{ijk} F_{jk} -->
$$
B_i = -\tfrac{1}{2}\,\epsilon_{ijk}\,F_{jk}
$$

where ε_{ijk} is the Levi-Civita symbol (the fully
antisymmetric tensor in three dimensions, with ε₁₂₃ = +1).
Explicitly:

- B₁ = F₃₂ = ∂₃A₂ − ∂₂A₃
- B₂ = F₁₃ = ∂₁A₃ − ∂₃A₁
- B₃ = F₂₁ = ∂₂A₁ − ∂₁A₂

This decomposition is not a choice — it is forced by the
signature.  The one timelike dimension creates a natural split
of the six field components into a 3-vector E (how the field
changes in time) and a 3-vector B (how the field curls in
space).

Written as a matrix:

```
         t     x      y      z
    ┌                              ┐
t   │    0    −E₁    −E₂    −E₃   │
x   │   E₁     0    −B₃     B₂   │
y   │   E₂    B₃      0    −B₁   │
z   │   E₃   −B₂     B₁      0   │
    └                              ┘
```

The upper-right triangle is −E and −B; the lower-left is +E
and +B (antisymmetry).

---

## Step 5: The action

The dynamics come from the **principle of least action** — the
same variational principle used in classical mechanics.  The
idea: assign a single number S (the "action") to every possible
field configuration A_μ(x).  The physical configuration is the
one that makes S stationary (δS = 0).  This is the field-theory
generalization of "a ball rolls to the bottom of a hill."

We need the action S[A] to satisfy:

1. Gauge-invariant (must be built from F_μν, not A_μ alone)
2. Lorentz-invariant (same physics for all inertial observers)
3. Local (depends on fields at a point, not at a distance)

These three requirements follow from the axioms.  A fourth
is an additional assumption:

4. **Leading order in derivatives** — we take the lowest-order
   term in an expansion in powers of derivatives

This is not in the axioms.  Higher-order terms like
(F_μν F^μν)² are gauge-invariant and Lorentz-invariant.
The justification: on a lattice with grain size L, the
natural expansion parameter is (wavelength/L).  At scales
much larger than L (the regime where the continuum limit
applies), higher-derivative terms are suppressed by powers of
(L/wavelength)² and become negligible.  The leading term
dominates.  This is the same logic that makes Hooke's law
(F = −kx) valid for small deformations even though the true
atomic potential has cubic and quartic terms.

With these four requirements, the unique field action is:

<!-- S_EM = −(1/4) ∫ F_μν F^μν d⁴x -->
$$
S_{\text{EM}} = -\frac{1}{4} \int F_{\mu\nu}\,F^{\mu\nu}\; d^4x
$$

Here F^μν is F_μν with indices raised by the Minkowski metric
(see reading guide — this flips the sign whenever a time index
is involved, so F^{0i} = −E_i while F^{ij} = F_{ij}).  The
contraction F_μν F^μν sums over all index pairs, giving a
single number at each point.  Written in terms of E and B:

<!-- F_μν F^μν = 2(B² − E²) -->
F_μν F^μν = 2(**B**² − **E**²)

So the action measures the integrated difference between
magnetic and electric energy — a balance that nature
extremizes.

**Why unique?**  Gauge invariance eliminates A_μ A^μ and any
term containing A without a curl.  Lorentz invariance
eliminates anything that treats time or space directions
differently.  The only independent Lorentz scalar quadratic
in F is F_μν F^μν.  (There is one pseudo-scalar,
F_μν F̃^μν = F_μν ε^μνρσ F_ρσ, but it is a total derivative
and does not contribute to the equations of motion.)

If charged matter (the phase field θ with its topological
vortices) is present, there is a source term coupling the
current to the field.  On the lattice, vortices carry
quantized charge e = √(4πα) (from A6 — see the charge
quantization section below).  The minimal gauge-invariant
coupling is:

<!-- S_source = e ∫ j^μ A_μ d⁴x -->
$$
S_{\text{source}} = e \int j^\mu\,A_\mu\; d^4x
$$

where j^μ = (n, j¹, j², j³) is the **number current** density
(integer charge count per unit volume, and its flow).  The
physical charge-current density is J^μ = e j^μ.

The full action is:

<!-- S = −(1/4) ∫ F_μν F^μν d⁴x + e ∫ j^μ A_μ d⁴x -->
$$
S = -\frac{1}{4}\int F_{\mu\nu}F^{\mu\nu}\,d^4x
    \;+\; e\int j^\mu A_\mu\,d^4x
$$

The coupling constant α enters through e = √(4πα).  The single
physical parameter α controls how strongly charges couple to
the field.

**Why e² = 4πα and not some other relationship.**  The
−1/4 normalization of the free-field action is not arbitrary —
it is fixed by requiring that the energy density of the
electromagnetic field takes the standard form u = ½(E² + B²)
per unit volume.  Given this normalization, the only
dimensionless coupling that appears at a charge-field vertex
is e, and the dimensionless strength of the force between two
charges (the quantity that appears in scattering amplitudes
and in the Coulomb force law F = αq₁q₂/r²) is:

<!-- α = e² / (4π) -->
$$
\alpha = \frac{e^2}{4\pi}
$$

The 4π arises from the solid angle of a sphere in three
spatial dimensions — it is the geometric factor in Gauss's
law.  No other relationship is consistent with the action
structure: the quadratic free term fixes the field
normalization, and the linear source term then fixes how e
relates to the physical coupling α.

This is a standard result of U(1) gauge theory — it appears
in any quantum field theory reference.  GRID does not add a
new relationship here; it arrives at the same one from more
primitive assumptions (the lattice axioms A1–A4 produce the
U(1) gauge structure from which e² = 4πα follows).  The
derivation is independent of GRID's specific framework.

---

## Step 6: The equations of motion (inhomogeneous Maxwell)

Vary the action with respect to A_ν.  The field term
S_EM = −(1/4) ∫ F_μρ F^μρ d⁴x contributes:

<!-- δS_EM / δA_ν = −∂_μ F^μν -->
$$
\frac{\delta S_{\text{EM}}}{\delta A_\nu} = -\partial_\mu F^{\mu\nu}
$$

To see this: F_μρ = ∂_μA_ρ − ∂_ρA_μ depends on A linearly,
so the variation of F² pulls down two identical terms.  Then
integration by parts moves the derivative onto F, giving
−∂_μ F^μν.  (The factor 4 from the variation cancels the 1/4
in the action.)

The source term S_source = e ∫ j^μ A_μ d⁴x contributes simply
e j^ν.

Setting the total variation to zero:

<!-- −∂_μ F^μν + e j^ν = 0 -->
$$
\partial_\mu F^{\mu\nu} = e\,j^\nu
$$

Writing J^ν = e j^ν for the physical charge-current density:

<!-- ∂_μ F^μν = J^ν -->
$$
\boxed{\;\partial_\mu F^{\mu\nu} = J^\nu\;}
$$

This single covariant equation contains **two** of Maxwell's
four equations.  Expanding in components:

**ν = 0 (the time component):**

<!-- ∂_i F^{i0} = J^0 = ρ -->
$$
\partial_i F^{i0} = \rho
$$

Since F^{i0} = −F^{0i} = −(−E_i) = E_i (two sign flips: one
from antisymmetry, one from raising the time index), this is:

<!-- ∇ · E = ρ -->
$$
\boxed{\;\nabla \cdot \mathbf{E} = \rho\;}
\qquad\text{(Gauss's law)}
$$

Charge (ρ) creates diverging electric field lines.  In the
lattice picture: a topological vortex (where the phase winds
by 2π) is a source of electric flux.

**ν = j (a spatial component):**

<!-- ∂_0 F^{0j} + ∂_i F^{ij} = J^j -->

Expanding: F^{0j} = −E_j (raising the time index flips the sign)
and ∂_i F^{ij} = (∇ × **B**)_j (the spatial curl).  This gives:

<!-- −∂E_j/∂t + (∇ × B)_j = J_j -->
$$
\boxed{\;\nabla \times \mathbf{B} - \frac{\partial\mathbf{E}}{\partial t} = \mathbf{J}\;}
\qquad\text{(Ampère's law with displacement current)}
$$

Currents and time-changing electric fields create curling
magnetic fields.  The ∂E/∂t term (Maxwell's displacement
current) is not added by hand — it falls out automatically from
the Lorentz-invariant action.

---

## Step 7: The Bianchi identity (homogeneous Maxwell)

The remaining two Maxwell equations require no dynamics at all.
They are **identities** — automatic consequences of F_μν being
defined as a curl of A_μ.

Take the totally antisymmetric combination of derivatives of F:

<!-- ∂_μ F_νρ + ∂_ν F_ρμ + ∂_ρ F_μν = 0 -->
$$
\partial_\mu F_{\nu\rho}
  + \partial_\nu F_{\rho\mu}
  + \partial_\rho F_{\mu\nu} = 0
$$

This is the **Bianchi identity**.  To verify: substitute
F_νρ = ∂_νA_ρ − ∂_ρA_ν and expand.  Every term appears twice
with opposite signs (because partial derivatives commute), so
the sum vanishes identically.  No equation of motion needed —
this holds for any A_μ, in any configuration.

Expanding in components using the E/B decomposition:

**One time index, two spatial (μ = 0, ν = i, ρ = j):**

<!-- ∂_0 F_{ij} + ∂_i F_{j0} + ∂_j F_{0i} = 0 -->

This gives:

<!-- ∂B/∂t + ∇ × E = 0 -->
$$
\boxed{\;\nabla \times \mathbf{E} + \frac{\partial\mathbf{B}}{\partial t} = 0\;}
\qquad\text{(Faraday's law)}
$$

A time-changing magnetic field induces a curling electric field.
Electromagnetic induction — the basis of generators and
transformers — is a geometric identity of the lattice.

**Three spatial indices (μ = i, ν = j, ρ = k):**

<!-- ∂_i F_{jk} + ∂_j F_{ki} + ∂_k F_{ij} = 0 -->

This gives:

<!-- ∇ · B = 0 -->
$$
\boxed{\;\nabla \cdot \mathbf{B} = 0\;}
\qquad\text{(No magnetic monopoles)}
$$

Magnetic field lines have no endpoints.  In the lattice picture:
B is defined as the curl of A, and the divergence of a curl is
always zero.  Magnetic monopoles would require A_μ to be
ill-defined somewhere (a Dirac string) — the smooth lattice
phase field does not support this.

---

## Summary: the four equations

All four of Maxwell's equations, derived from the GRID axioms:

| # | Equation | Name | Origin |
|---|----------|------|--------|
| 1 | ∇ · **E** = ρ | Gauss's law | Action principle (Step 6, ν = 0) |
| 2 | ∇ × **B** − ∂**E**/∂t = **J** | Ampère + displacement | Action principle (Step 6, ν = j) |
| 3 | ∇ × **E** + ∂**B**/∂t = 0 | Faraday's law | Bianchi identity (Step 7, one time index) |
| 4 | ∇ · **B** = 0 | No monopoles | Bianchi identity (Step 7, three spatial indices) |

Equations 1–2 are **dynamical** — they follow from varying the
action and encode how sources create fields.  They depend on α
(through the coupling κ in the action).

Equations 3–4 are **topological** — they are identities that
follow from F = dA and hold regardless of the dynamics.  They
have no free parameters.

---

## What was used

| Axiom | Where it entered |
|-------|------------------|
| A1. 4D lattice | Continuum limit gives 4D spacetime, coordinates x^μ |
| A2. Signature (1,3) | Minkowski metric η_μν; splits F_μν into E and B |
| A3. Periodic phase | The field θ; gauge structure; periodicity gives charge quantization |
| A4. Gauge invariance | Forces grid to carry link phases (A_μ); builds F_μν; constrains action |
| A6. Coupling α | Determines e = √(4πα), the charge-field coupling strength |

**Not used:** A5 (resolution ζ).  The Maxwell derivation is
independent of the information content of the lattice.  Gravity
plays no role.

**Additional assumption (not in the axioms):**

Step 5 invokes **leading-order dominance** — the action is the
lowest-order gauge-invariant, Lorentz-invariant scalar in an
expansion in powers of derivatives.  Higher-order terms exist
but are suppressed at scales much larger than the grain size.
This is the standard continuum-limit argument and is well
justified, but it is not a consequence of A1–A6 alone.  If
future work finds this assumption problematic, it would need to
be promoted to an axiom or derived from the lattice structure.

---

## Charge quantization

One result that deserves emphasis because it costs nothing extra.

The phase θ is periodic: θ and θ + 2π are the same state (A3).
On the lattice, a **topological vortex** is a closed path of
cells around which the total phase change is a nonzero integer
multiple of 2π:

<!-- ∮ ∂_μ θ · dx^μ = 2πn, n ∈ ℤ -->
$$
\oint \partial_\mu\theta \;\cdot\; dx^\mu = 2\pi n,
\qquad n \in \mathbb{Z}
$$

You cannot have half a winding.  The integer n is the
**topological charge** — it counts how many times the phase
wraps around the circle as you traverse the loop.

In the continuum, this becomes:

<!-- ∮ A_μ dx^μ = (2π/e) n -->
$$
\oint A_\mu\,dx^\mu = \frac{2\pi}{e}\,n
$$

and the enclosed charge is:

<!-- Q = ne -->
$$
Q = n\,e
$$

Charge is **quantized** — it comes in integer multiples of the
elementary charge e = √(4πα) ≈ 0.303 (natural units).  This is
not imposed; it follows from the periodicity of the phase
variable.  A vortex with n = +1 is a particle of charge +e;
n = −1 is charge −e; n = 0 is neutral.

Conservation of charge is equally automatic: a vortex cannot
appear or disappear locally.  You can only create a
vortex-antivortex pair (n = +1 and n = −1) or annihilate one.
The total winding number is conserved.  In continuum language
this is the **continuity equation**:

<!-- ∂_μ J^μ = 0 -->
$$
\partial_\mu J^\mu = 0
$$

which also follows directly from the antisymmetry of F^μν:
∂_ν(∂_μ F^μν) = 0 identically (antisymmetric tensor contracted
with symmetric ∂_μ∂_ν), so if ∂_μ F^μν = J^ν then
∂_ν J^ν = 0.  Conservation of charge is a theorem, not an
axiom.

---

## Axiom audit

The derivation used five of the six axioms.  Here is what each
one is doing and whether it could be weakened:

**A1 (4D lattice):** provides the arena.  The derivation works
in any dimension D ≥ 2.  In D dimensions, F_μν has D(D−1)/2
components.  For D = 4 we get 6, which split into 3 + 3 under
the signature → the familiar E and B.  In D = 3 (2+1
dimensions), there would be 1 electric component and 1 magnetic
component — electrodynamics still exists but is simpler.  The
4D choice is needed for the correct physical E and B.

**A2 (signature):** splits F_μν into time-space (E) and
space-space (B).  Without a signature distinction, all six
components are on equal footing and there is no notion of
"electric" vs "magnetic."

**A3 (periodic phase):** provides the U(1) structure and charge
quantization.  If the phase were non-compact (a real number, not
an angle), charge would not be quantized — any real value of
charge would be allowed.

**A4 (gauge invariance):** this is the engine of the entire
derivation.  It forces the grid to carry link phases (A_μ) in
addition to cell phases (θ), builds F_μν from the link states,
and constrains the form of the action.  Without it, the grid
has only cell phases obeying a scalar wave equation — no
electromagnetism.

**A6 (coupling α):** sets the one free parameter.  If α → 0,
the coupling vanishes and the electromagnetic field decouples
from charges (free field only).  If α → ∞, the coupling is
infinitely strong and the lattice is dominated by the nearest-
neighbor interaction (confinement regime).  α ≈ 1/137 is in the
weak-coupling regime where the continuum limit is well-behaved.
