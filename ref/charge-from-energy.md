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

WvM's key insight: because of the double-loop topology, when the
photon's E field rotates as it travels (circular polarization),
the commensurate twist and orbital motion conspire so that **E
always points radially inward** (or always outward).  It never
flips.  Visualize a twisted strip of paper whose ends are joined
into a double loop — one face always points outward.

A photon in free space has E pointing in all directions (it
rotates) → zero net flux → no charge.  A photon on a closed
(1,2) path has E always pointing the same way → net outward
flux → apparent charge.

The photon is still a photon.  It still has zero "fundamental
charge."  But from outside, the E field looks exactly like a
point charge.

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
radius.  The only unknown is the field profile — how E is
distributed over the surface.  Determining this profile (by
solving the wave equation on the compact geometry) is the key
open problem.

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
