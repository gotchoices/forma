# Charge from Energy

How does a packet of electromagnetic energy become an apparent
electric charge?  This primer develops the physical picture
step by step, starting from a photon and ending with a charged
particle — without ever introducing a fundamental charge.

---

## 1. A photon's fields

A photon is a traveling electromagnetic wave.  It carries two
fields:

- **E** (electric) — perpendicular to the propagation direction
- **B** (magnetic) — perpendicular to both E and propagation

For a photon in vacuum, E and B are always perpendicular to each
other, always transverse to the direction of travel, and always
equal in energy: U_E = U_B = U/2, where U is the total photon
energy.  This is exact for any EM wave, not an approximation.

A photon has no net charge.  If you put a Gauss's law surface
around it, the E field entering one side exits the other.  The
total outward flux is zero.

## 2. Topology changes everything

Now confine the photon to a closed path — specifically, a (1,2)
torus knot (once around the tube, twice around the ring).

### Why a linearly polarized photon gives zero charge

A linearly polarized photon has E oscillating sinusoidally:
positive on one half-wavelength, negative on the other.  On any
closed path, the outward and inward halves cancel — the net
E flux through any enclosing surface is zero.  Gauss's law:
no net flux → no charge.

### Circular polarization changes the picture

A circularly polarized photon is different: |E| is constant
everywhere — it never passes through zero.  What changes is
the *direction* of E, which rotates once per wavelength.

On the torus, as the photon winds once around the minor circle
(θ: 0 → 2π), the outward normal to the surface also rotates
by 2π in 3D space.  If the circular polarization rotates in
the opposite sense to this geometric rotation, the two
rotations cancel.  The result:

**E has constant magnitude and always points normal to the
torus surface — outward everywhere, at all times.**

Verified directly: for left-circular polarization with phase
synchronized to the geometric angle θ,

    E = E₀[cos θ · n̂(θ) − sin θ · ê_θ(θ)]

Expanding n̂ and ê_θ in 3D cylindrical coordinates:

    E · ρ̂ = E₀(cos²θ + sin²θ) = E₀     (constant, always outward)
    E · ẑ = 0                             (no vertical component)

This is WvM's key insight: circular polarization on a closed
winding path produces a field that never flips.  A photon in
free space has E rotating in all directions → zero net flux →
no charge.  The same photon on a (1,2) path has E always
pointing outward → net flux → apparent charge.

The photon is still a photon.  It still has zero "fundamental
charge."  But from outside, the E field looks exactly like a
point charge.

### Electron vs positron

What determines which way E points — inward (electron) or
outward (positron)?  Two things together:

1. **The photon's polarization handedness** — right vs left
   circular polarization determines which face of the compact
   surface E exits from.
2. **The orientation of the compact dimensions relative to xyz**
   — how T² "sits" in the full spacetime determines which 3D
   direction that corresponds to.

Neither alone fixes the charge sign; it's the combination.
Flipping either one (reversing the polarization, or mirroring
the compact-dimension orientation) flips the charge — this is
charge conjugation (C).

The dimensional orientation is axiomatic — it's part of how the
universe is wired, like the perpendicularity of x and y.  The
photon's handedness is a degree of freedom within that structure.

## 3. The flat-rectangle picture

In the compact-dimension framework, the photon lives on a flat
rectangle with periodic boundary conditions (opposite edges
identified).  This is a flat torus T² — topologically equivalent
to the 3D donut, but without curvature.

On this rectangle:

- The photon travels **diagonally** (for a (1,2) knot: slope
  L_θ/L_φ, completing two horizontal and one vertical crossing
  per cycle).
- **E extends perpendicular to the rectangle**, out into our
  3+1D spacetime.  The rectangle is the compact dimensions;
  "perpendicular" is the non-compact space we live in.
- **B is tangent to the rectangle**, perpendicular to the photon's
  path within the plane.

For circular polarization, E spirals around the propagation
direction: the perpendicular component (out of the plane) and
the in-plane transverse component oscillate 90° out of phase,
each with amplitude E₀.  In the flat picture, the perpendicular
component oscillates sinusoidally — positive, then negative,
then positive again along the path.

**The "always outward" effect is hidden in the flat picture.**
When the rectangle is wrapped into a torus, the fixed
"perpendicular" direction of the flat picture becomes the
*local* surface normal n̂(θ), which rotates with θ.  The
sinusoidal oscillation of E_perp and the rotation of n̂ cancel
each other — producing the constant outward field described in
§2.  The flat picture is valid; the charge mechanism just isn't
visually obvious until you wrap.

This gives a clean separation:

| Field | Direction         | What it becomes in 3+1D       |
|-------|-------------------|-------------------------------|
| E     | Out of the plane  | Electric charge (monopole)    |
| B     | In the plane      | Magnetic moment (dipole)      |

Since the rectangle is compact (tiny — dimensions of order
10⁻¹³ m), from any macroscopic distance it collapses to a point.
All the E flux leaving the rectangle converges and looks like the
field of a point charge.

## 4. B gives the magnetic moment

B stays in the plane of the rectangle, perpendicular to the
photon's diagonal path.  When the rectangle is wrapped into a
torus and embedded in 3D:

- The "in-plane" direction becomes tangent to the torus surface.
- The cross product B = (1/c) k̂ × E, where k̂ spirals along the
  (1,2) geodesic and E points radially toward the torus axis,
  produces a B with a strong component along the torus symmetry
  axis (the spin axis).
- The axial component accumulates as the photon spirals; the
  azimuthal components circulate and cancel on average.

The result: B has a net direction along the torus axis — a
magnetic dipole.  This is WvM's result (§2 of the paper),
arrived at here from the field equations rather than the
twisted-strip visualization.

**Important:** the magnetic dipole does NOT arise from a
circulating charge.  No charge moves around the torus — a photon
is electrically neutral.  The "charge" is an apparent effect
(net E flux from the topology).  The magnetic moment comes
directly from the photon's own B field: its direction in the
plane, when mapped to the 3D torus, has a net component along
the symmetry axis.  This is a geometric projection, not a
current loop.

## 5. Why geometry determines charge

The total E field energy is fixed:

    U_E = hc / (2λ_C) = m_e c² / 2

This is half the photon's energy, and it doesn't depend on the
geometry at all.  So why does the charge depend on the torus
dimensions?

Because **energy and flux are different things.**

- Energy is ∫ E² dV — quadratic in E, integrated over volume.
- Flux is ∮ E · dA — linear in E, integrated over a surface.
- Charge = ε₀ × flux (Gauss's law).

Knowing the total energy does not determine the total flux.  You
need to know how the energy is *distributed* — which depends on
the geometry.

### The rectangle argument

On the flat rectangle (area A = L_φ × L_θ), the E field energy
fills the rectangle area and extends some distance δ perpendicular
to it (into 3+1D):

    Energy density:  u = U_E / (A × δ)
    Field strength:  E = √(2u / ε₀)
    Total flux:      Φ = E × A
    Charge:          q = ε₀ Φ = √(2 ε₀ U_E A / δ)

The charge goes as **√A** — the square root of the rectangle
area.  Same energy, bigger rectangle → weaker field but more
surface → more total flux → more charge.

This is why the aspect ratio matters.  The path-length constraint
fixes a relationship between L_φ and L_θ:

    √(4 L_φ² + L_θ²) = λ_C

Different aspect ratios give different rectangle areas, different
flux, and different charge — even though the total energy is
identical.

### A concrete comparison

Imagine squeezing the same photon energy into two different
rectangles:

| Rectangle  | Area    | E field   | Flux = E × A | Charge |
|------------|---------|-----------|--------------|--------|
| Small      | A       | Strong    | Moderate     | Lower  |
| Large      | 4A      | Half      | 2×           | Higher |

The large rectangle has a weaker field (energy spread thinner)
but four times the surface area.  The net flux is doubled, so the
charge is √4 = 2× larger.

## 6. The two constraints

To determine the electron's geometry, we have two independent
equations:

**1. Path constraint (determines mass):**

    √(4 L_φ² + L_θ²) = λ_C = h/(m_e c)

The photon must resonate — its path length equals one Compton
wavelength.  This ensures the confined photon has the electron's
mass.

**2. Charge constraint (determines shape):**

The total E-field flux through the compact surface must equal
e/ε₀.  Combined with the energy constraint, this fixes the
aspect ratio of the rectangle.

Two equations, two unknowns (L_φ and L_θ).  The electron's
geometry is fully determined — no free parameters.

## 7. What "charge" really is

In this picture, charge is not a fundamental property.  It is an
**accounting identity**:

    charge = ε₀ × (total E-field flux leaving the compact surface)

A photon in free space has zero net flux → zero charge.  The same
photon on a (1,2) topology has nonzero net flux → apparent charge.
The magnitude depends on the photon's energy and the geometry of
the compact dimensions.

The elementary charge e is not put in by hand.  It is the flux
that results when the geometry satisfies both the resonance
condition (mass) and the energy distribution (shape).

There may be no such thing as "charge" as a fundamental entity.
There is energy, there is topology, and there is geometry.  What
we call charge is how they combine to produce a net E-field flux
from a compact region.

## 8. Self-capacitance: the geometry–energy–charge bridge

Capacitance relates charge to energy: U_E = q²/(2C).  Since both
U_E and q are known, the required capacitance is determined:

    C = e² / (m_e c²) ≈ 3.13 × 10⁻²⁵ F

Self-capacitance is defined as the capacitance between an object
and a grounded shell at infinite distance.  In our picture, the
"object" is the compact surface (T²) and the "shell at infinity"
is the surrounding 3+1D space.  The E field radiating from the
compact surface into 3D is exactly the field between these two
"plates."

This gives a clean accounting of the electron's rest mass energy:

| Half of m_e c² | Field | Where            | What it produces |
|----------------|-------|------------------|------------------|
| U_E = m_e c²/2 | E    | Surface → ∞      | Charge (monopole)|
| U_B = m_e c²/2 | B    | On the surface   | Magnetic moment  |

The electrostatic energy q²/(2C) stored between the compact
surface and infinity equals exactly half the rest mass.  The
other half is the B field energy confined to the compact surface.
The entire rest mass is field energy — nothing left over.

The self-capacitance C is a purely geometric quantity (times ε₀).
Different compact surface shapes have different self-capacitances.
The electron is the shape whose C equals e²/(m_e c²).  This is
equivalent to the Gauss's law constraint — just repackaged
through capacitance.


## 9. Gauss's law vs the WvM energy balance

WvM computed the charge using an energy-balance shortcut:

1. Assume U_E fills a volume V uniformly
2. Compute the average field E_avg = √(2U_E / (ε₀ V))
3. Match E_avg to the Coulomb field at a radius R
4. Solve for q

This involves two arbitrary choices: the volume V and the
matching radius R.  Different choices give different charges
(WvM's sphere gives q ≈ 0.91e; a torus with a/R = 4.29 gives
q = e exactly).

The rigorous alternative is Gauss's law:

    q = ε₀ ∮ E · dA

over any closed surface.  No arbitrary volume, no matching
radius.

### The synchronized circular polarization resolves the field profile

If the circularly polarized photon's rotation is synchronized
with the geometric winding (§2), the field on the torus surface
is determined: E = E₀ n̂ (constant magnitude, always normal).
This is equivalent to a **uniform surface charge** on the torus.

The charge then depends on the torus geometry through
self-capacitance: U_E = q²/(2C), where C(R, a) is the
self-capacitance of the torus shape (§8).  Setting U_E = m_e c²/2
gives q = √(m_e c² · C).  Combined with the path constraint,
this determines the aspect ratio.

This is a well-posed electrostatics problem with no arbitrary
choices — the field profile is fixed by the circular polarization
mechanism, and the geometry is fixed by two constraints (mass
and charge).

---

## Summary

| Concept | Mechanism |
|---------|-----------|
| Charge | Total E flux from compact surface (Gauss's law) |
| Mass | Resonance condition: path length = λ_C |
| Spin ½ | (1,2) topology: double loop → half-integer angular momentum |
| Magnetic moment | B tangent to compact surface → net axial dipole |
| g ≈ 2.0023 | Fraction of energy in external (non-rotating) field |

All five properties arise from a single photon on a compact
(1,2) topology.  No fundamental charge.  No point particle.
Just energy, topology, and geometry.

---

## References

- WvM paper: [`WvM.pdf`](WvM.pdf),
  summary: [`WvM-summary.md`](WvM-summary.md)
- Maxwell primer: [`maxwell-primer.md`](maxwell-primer.md)
- R6 findings (self-consistency):
  [`studies/field-profile/findings.md`](../studies/field-profile/findings.md)
- S2 findings (charge from geometry):
  [`studies/toroid-geometry/findings.md`](../studies/toroid-geometry/findings.md)
