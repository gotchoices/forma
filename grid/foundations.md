# GRID Foundations

The axioms, notation, and free parameters of the Geometric Relational
Interaction Domain.

## Notation and conventions

| Symbol | Meaning | Value (natural units) |
|--------|---------|----------------------|
| L | Lattice grain size (= Planck length) | 1 |
| c | Propagation speed (one cell per time step) | 1 |
| ℏ | Reduced Planck constant | 1 |
| k | Boltzmann constant | 1 |
| ζ | Resolution — bits per Planck cell | 1/4 |
| α | Fine-structure constant | ≈ 1/137.036 |

"Natural units" throughout GRID means c = ℏ = k = 1, with L = 1
defining the length scale.  The Planck length is the grain size,
not a derived quantity.

**Convention:** all GRID derivations work in natural units.  SI
conversions are deferred to the end and clearly marked when they
appear.

---

## The axioms

Six statements.  The first four define the lattice structure.  The
fifth sets the information content.  The sixth sets the interaction
strength.

### A1. Four-dimensional causal lattice

Space is a regular array of identical cells in four dimensions.
Each cell has a characteristic size L (the grain size).

Disturbances propagate from cell to cell at one cell per time step.
This propagation speed, in the continuum limit, is the speed of
light c.

*This axiom gives us: dimensionality (4), a length scale (L),
and a speed (c = L/τ where τ is the time step).*

### A2. Lorentzian signature (1,3)

Of the four lattice dimensions, exactly one is **timelike** — it
carries a causal ordering.  Information flows forward along this
dimension only.  The remaining three dimensions are spatial and
have no preferred direction.

In the continuum limit, the metric signature is (−, +, +, +).
The minus sign on the time component is not put in by hand — it
is the statement that the causal dimension behaves differently
from the spatial ones.

*This axiom gives us: the distinction between time and space,
the light-cone structure, and the impossibility of backward
signaling.*

### A3. Periodic internal phase

Each cell carries an internal degree of freedom: a **phase**
θ ∈ [0, 2π).  This is the simplest possible compact continuous
variable — a point on a circle.

The phase is not directly observable.  Only **phase differences**
between neighboring cells have physical meaning.

*This axiom gives us: U(1) symmetry (the circle group), and the
seed from which electromagnetic gauge structure will grow.*

### A4. Local gauge invariance

The physics is unchanged under arbitrary local relabeling of the
phase:

<!-- θ(x) → θ(x) + χ(x) for any smooth function χ -->
$$
\theta(x) \;\to\; \theta(x) + \chi(x)
$$

for any smooth function χ(x).  Since only phase differences
matter (A3), a *uniform* shift is trivially irrelevant.  Gauge
invariance extends this to *non-uniform* shifts: even if I
relabel each cell's phase by a different amount, the physics
must remain the same — provided I simultaneously adjust the
**connection** between cells to compensate.

This compensating connection, in the continuum limit, is the
electromagnetic four-potential A_μ.  It is part of the grid's
state, stored on the **links** between cells (not on the cells
themselves).  A_μ is not a new parameter — it is dynamic memory
on each link, determined by the equations of motion.  Its
existence is *forced* by gauge invariance; its dynamics produce
the electromagnetic field.  A propagating disturbance in the
link states is a photon
(see [maxwell.md](maxwell.md) for the full derivation).

*This axiom gives us: the gauge field A_μ, from which the
electromagnetic field tensor F_μν is constructed.*

### A5. Information resolution ζ = 1/4

Each cell contributes ζ = 1/4 bit to the collective information
content of the lattice.  Equivalently: it takes 1/ζ = 4 cells to
encode one bit of physical information.

This is the **Bekenstein-Hawking factor**.  A causal horizon of
area A (measured in Planck units, L = 1) carries entropy:

<!-- S = ζ · A = A/4 -->
$$
S = \zeta \cdot A = \frac{A}{4}
$$

No single cell holds a complete bit.  The phase θ is a collective
variable defined over a minimum patch of ~4 cells — like a pixel
requiring a 2×2 sub-pixel grid to resolve.  This is an
anti-aliasing constraint: no excitation can have spatial frequency
higher than 1/(4L).

The resolution ζ directly determines the gravitational constant:

<!-- G = 1/(4ζ) = 1 in natural units -->
$$
G = \frac{1}{4\zeta} = 1 \quad \text{(natural units)}
$$

This is derived, not postulated — see [gravity.md](gravity.md).

*This axiom gives us: the entropy bound, the Planck area, the
gravitational constant, and the UV cutoff of the lattice.*

### A6. Electromagnetic coupling α ≈ 1/137

The energy cost of a minimal topological defect (a vortex — a
region where the collective phase winds through a full 2π) relative
to the natural lattice energy scale is set by a single dimensionless
number: the fine-structure constant α.

In the lattice action, α appears as the inverse of the coupling
constant κ:

<!-- κ = 1/(4πα) ≈ 1722 -->
$$
\kappa = \frac{1}{4\pi\alpha} \approx 1722
$$

so the electromagnetic Lagrangian density is:

<!-- L = −(1/4) κ F_μν F^μν = −1/(16πα) F_μν F^μν -->
$$
\mathcal{L} = -\frac{1}{4}\,\kappa\, F_{\mu\nu}F^{\mu\nu}
             = -\frac{1}{16\pi\alpha}\, F_{\mu\nu}F^{\mu\nu}
$$

From α, all electromagnetic quantities follow:

| Quantity | Expression | Natural units |
|----------|------------|---------------|
| Elementary charge e | √(4πα) | ≈ 0.3028 |
| Permittivity ε₀ | 1 | 1 |
| Permeability μ₀ | 1 | 1 |
| Impedance Z₀ | √(μ₀/ε₀) | 1 |

In SI units, ε₀ and μ₀ acquire their familiar values through the
unit conversions c, ℏ, and the definition of the ampere.  Their
apparent independence is an artifact of SI — they encode the same
single parameter α.

*This axiom gives us: the strength of electromagnetism, the value
of the elementary charge, and (through the lattice action) the
dynamics that produce Maxwell's equations.*

---

## What the axioms produce

| Emergent structure | From which axioms | Where derived |
|--------------------|-------------------|---------------|
| Maxwell's equations | A1–A4, A6 | [maxwell.md](maxwell.md) |
| Charge quantization | A3 (phase periodicity) | [maxwell.md](maxwell.md) |
| Gravitational constant G | A1, A5 | [gravity.md](gravity.md) |
| Einstein field equations | A1, A2, A5 | [gravity.md](gravity.md) |
| Spacetime stiffness c⁴/(8πG) | A1, A2, A5 | [stiffness.md](stiffness.md) |
| Arrow of time | A2, A5 | [gravity.md](gravity.md) |
| Speed of light | A1 (lattice propagation) | Given by construction |
| E and B field decomposition | A2 (signature splits F_μν) | [maxwell.md](maxwell.md) |
| ε₀ = μ₀ = 1 (natural units) | A1, A6 | [maxwell.md](maxwell.md) |

---

## What the axioms do NOT produce

These require additional structure beyond the minimal lattice:

- **The value of α** — the coupling is a measured input, not
  derived.  GRID takes α ≈ 1/137.036 as given.

- **Why ζ = 1/4** — the resolution is a free parameter.  The
  factor of 4 has been reproduced by multiple independent
  approaches (string theory, loop quantum gravity, entanglement
  entropy) but no first-principles derivation from pure
  combinatorics exists.

- **Non-abelian gauge groups** — the U(1) symmetry of axiom A3
  gives electromagnetism.  The SU(2) × SU(3) structure of the
  weak and strong forces requires richer internal degrees of
  freedom.  This is outside GRID's scope (and largely handled by
  MaSt's compact geometry).

- **Particle masses** — these are MaSt's domain.  GRID provides
  the field equations; MaSt provides the compact geometry that
  confines photons into massive particles.

---

## Open questions at the foundations level

**Q1. Does the tensor window size matter?**

A smooth tensor field (10 independent components, each requiring
meaningful precision) cannot live in a single cell that holds only
ζ = 1/4 bit.  The tensor description is a **sliding window** over
many cells — roughly ~4000 cells (~8 Planck lengths across) by
a naive estimate.  This window size may follow from ζ alone, or
it may be derivable from macro-scale observables, or it may be
an independent parameter.  We leave this aside unless the Maxwell
or G derivations require it.

**Q2. Are ζ and α related?**

Both are treated as independent inputs.  It is conceivable that
they are connected by a consistency condition (e.g. a Nyquist-like
constraint matching resolution to signal bandwidth), which would
reduce the free parameters to one.  This is noted but not assumed.

**Q3. Does the lattice require 4 dimensions?**

Axiom A1 asserts 4D.  Could a self-consistent causal lattice with
holographic entropy exist in other dimensions?  If 4 is the unique
consistent choice, one axiom becomes a theorem.

**Q4. Is the (1,3) signature derivable?**

If the causal structure (forward-only information flow) is the
fundamental input, does exactly one timelike dimension follow?
Some approaches to quantum gravity (Euclidean quantum gravity)
suggest the signature emerges from a phase transition.
