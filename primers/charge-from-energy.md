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

<!-- E = E₀[cos θ · n̂(θ) − sin θ · ê_θ(θ)] -->
$$
\mathbf{E} = E_0\bigl[\cos\theta\,\hat{n}(\theta) - \sin\theta\,\hat{e}_\theta(\theta)\bigr]
$$

Expanding n̂ and ê_θ in 3D cylindrical coordinates:

<!-- E · ρ̂ = E₀(cos²θ + sin²θ) = E₀ (constant, always outward); E · ẑ = 0 -->
$$
\begin{aligned}
\mathbf{E} \cdot \hat{\rho} &= E_0(\cos^2\theta + \sin^2\theta) = E_0 && \text{(constant, always outward)} \\
\mathbf{E} \cdot \hat{z}    &= 0 && \text{(no vertical component)}
\end{aligned}
$$

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
   circular polarization determines which face of the material
   surface E exits from.
2. **The orientation of the material dimensions relative to xyz**
   — how the material sheet "sits" in the full spacetime determines which 3D
   direction that corresponds to.

Neither alone fixes the charge sign; it's the combination.
Flipping either one (reversing the polarization, or mirroring
the material-dimension orientation) flips the charge — this is
charge conjugation (C).

The dimensional orientation is axiomatic — it's part of how the
universe is wired, like the perpendicularity of x and y.  The
photon's handedness is a degree of freedom within that structure.

## 3. The flat-rectangle picture

In the material-dimension framework, the photon lives on a flat
rectangle with periodic boundary conditions (opposite edges
identified).  This is a flat torus T² — topologically equivalent
to the 3D donut, but without curvature.

On this rectangle:

- The photon travels **diagonally** (for a (1,2) knot: slope
  L_θ/L_φ, completing two horizontal and one vertical crossing
  per cycle).
- **E extends perpendicular to the rectangle**, out into our
  3+1D spacetime.  The rectangle is the material dimensions;
  "perpendicular" is the spatial dimensions we live in.
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

<!-- U_E = hc / (2λ_C) = mₑc²/2 -->
$$
U_E = \frac{hc}{2\lambda_C} = \frac{m_e c^2}{2}
$$

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

<!-- u = U_E/(A·δ),  E = √(2u/ε₀),  Φ = E·A,  q = ε₀Φ = √(2ε₀ U_E A/δ) -->
$$
\begin{aligned}
u   &= \frac{U_E}{A \cdot \delta} \\[6pt]
E   &= \sqrt{\frac{2u}{\varepsilon_0}} \\[6pt]
\Phi &= E \cdot A \\[6pt]
q   &= \varepsilon_0\,\Phi = \sqrt{\frac{2\varepsilon_0\,U_E\,A}{\delta}}
\end{aligned}
$$

The charge goes as **√A** — the square root of the rectangle
area.  Same energy, bigger rectangle → weaker field but more
surface → more total flux → more charge.

This is why the aspect ratio matters.  The path-length constraint
fixes a relationship between L_φ and L_θ:

<!-- √(4 L_φ² + L_θ²) = λ_C -->
$$
\sqrt{4L_\phi^2 + L_\theta^2} = \lambda_C
$$

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

<!-- √(4 L_φ² + L_θ²) = λ_C = h/(mₑc) -->
$$
\sqrt{4L_\phi^2 + L_\theta^2} = \lambda_C = \frac{h}{m_e c}
$$

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

<!-- C = e²/(mₑc²) ≈ 3.13 × 10⁻²⁵ F -->
$$
C = \frac{e^2}{m_e c^2} \approx 3.13 \times 10^{-25}\,\text{F}
$$

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

<!-- q = ε₀ ∮ E · dA -->
$$
q = \varepsilon_0 \oint \mathbf{E} \cdot d\mathbf{A}
$$

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

## 10. From the WvM picture to the shear mechanism

The argument so far has been a specific physical story: a
circularly polarized photon on a (1,2) torus knot, its
polarization rotation canceling the geometric rotation of the
surface normal, producing a constant outward E field.  This is
WvM's insight, and it is the right intuition.  But it has a
limitation: **it treats the photon as a particle tracing a
path.**

When the confined photon is modeled as what it actually is — a
standing wave (eigenmode) on the compact surface — the
circular-polarization argument does not carry over directly.
A standing wave does not "travel" along a geodesic; it fills
the entire surface simultaneously.  The WvM picture gives the
right answer for the right reason, but only in a
particle-trajectory approximation.  The full wave treatment
requires a different mechanism: **shear**.

### What shear means

On the flat rectangle (§3), the two periodic dimensions form
a perfect grid — vertical lines and horizontal lines at right
angles.  This is an unsheared lattice.  Now tilt the grid
slightly: slide the top edge of the rectangle sideways by a
small amount δ relative to the bottom edge.  The rectangle
becomes a parallelogram.

```
Unsheared (s = 0):       Sheared (s > 0):

  +----------+             +----------+
  |          |            / ←δ→      /
  |          |           /          /
  +----------+          +----------+
```

Mathematically, the fractional shear s is the offset divided
by the tube circumference: s = δ / L_tube.  It is a small
dimensionless number — typically a few percent.  The photon
still winds on the same topology — still (1,2), still one
wavelength per geodesic loop — but its path is tilted, and so
is the field pattern it carries.

### Why shear creates charge

On the unsheared torus, the (1,2) mode's E field has a
symmetric pattern: equal amounts of outward and inward flux
through any enclosing surface.  The Gauss's law integral is
zero.  No charge.

Shear breaks this symmetry.  The field pattern's nodes shift
asymmetrically, and the outward flux no longer cancels the
inward flux.  The Gauss's law integral becomes:

<!-- Q(s) ∝ sin(2πs) / (2−s) -->
$$
Q(s) \propto \frac{\sin(2\pi s)}{2 - s}
$$

At s = 0: sin(0) = 0, so Q = 0.  Any nonzero shear gives
nonzero charge.  The sin(2πs) factor is the symmetry-breaking
term — it vanishes when the lattice is orthogonal and grows
as the lattice tilts.

The full formula for the fine structure constant α (which
sets the ratio of charge to energy) is:

<!-- α = r² √(1/r² + (2−s)²) × sin²(2πs) / (4π(2−s)²) -->
$$
\alpha = r^2 \sqrt{\frac{1}{r^2} + (2-s)^2} \cdot \frac{\sin^2(2\pi s)}{4\pi(2-s)^2}
$$

where r is the aspect ratio of the material sheet.  This is
one equation in two unknowns (r and s).  For any aspect ratio
r > 0.26, there exists a unique shear s that gives exactly
α = 1/137.036 — the measured value.

### Shear is energetically free

An important result from R19: shearing the material sheet
does not cost energy.  In fact, it *saves* energy.  When
the lattice tilts, the (1,2) geodesic gets longer, which
lowers the photon's frequency and therefore its energy.
The Coulomb self-energy of the newly created charge adds
a small positive cost, but the path-length saving is about
8.6× larger.  The net effect: shear lowers the total energy.

The material sheet does not resist becoming sheared.  It
welcomes it.  Having charge is "cheap" — the energy cost of
the Coulomb field is far smaller than the energy saved by
lengthening the geodesic.

### Connection to the WvM picture

The WvM circular-polarization argument and the shear
mechanism are not competing explanations — they are two views
of the same physics.  WvM asks: "what kind of photon produces
a constant outward E field on a torus?"  Answer: one whose
circular polarization is synchronized with the geometric
winding.  The shear mechanism asks: "what geometric
deformation of the flat torus produces a nonzero E-flux
integral?"  Answer: any nonzero within-plane shear.

The shear picture is more general.  It gives a clean formula
for α in terms of geometry.  It applies to any mode on any
sheet, not just the electron's specific (1,2) configuration.
And it connects charge to a measurable geometric parameter —
the lattice angle of the compact dimensions.

Under the shear mechanism, the electron sheet's lattice
deviates from orthogonal by only a few degrees — the exact
angle depends on the aspect ratio r_e, which is currently a
free parameter.  A nearly rectangular lattice, with just
enough tilt to produce α = 1/137.


## 11. Quantum numbers and the mode spectrum

So far we have focused on a single mode — the electron, a
(1,2) standing wave on a material sheet.  But every closed
surface supports many standing waves, not just one.  Each is
a **mode**, labeled by its winding numbers, and each has
definite physical properties determined entirely by the
geometry.

### Winding numbers on a single sheet

A material sheet has two periodic dimensions — the tube
(minor circle) and the ring (major circle), introduced in §2.
A standing wave on the sheet is specified by two integers:

- **n₁** — the number of wave cycles around the **tube**
  (this is the quantum number that determines charge and spin)
- **n₂** — the number of wave cycles around the **ring**

The pair (n₁, n₂) is the mode's **quantum numbers**.  The
electron is (1, 2): one cycle around the tube, two around the
ring — the same (1,2) torus knot from §2.  But (1, 3),
(2, 1), (1, 1), (0, 2), and infinitely many others are also
valid standing waves on the same surface.

### Mass from winding numbers

Each mode's energy (and therefore its mass, via E = mc²)
comes from the eigenvalue of the wave equation on the sheet:

<!-- m²c⁴ = (2πℏc)² [(n₁/L₁)² + (n₂/L₂)²] -->
$$
m^2 c^4 = (2\pi\hbar c)^2 \left[\left(\frac{n_1}{L_1}\right)^2 + \left(\frac{n_2}{L_2}\right)^2\right]
$$

where L₁ and L₂ are the circumferences of the two dimensions.
(This is simplified — the full formula includes a shear
correction — but the essential dependence is clear.)

Higher winding numbers mean shorter wavelengths, higher
frequencies, and therefore higher mass.  The (1, 2) electron
mode is relatively light because its winding numbers are
small.  A (3, 5) mode on the same sheet would be much heavier.

The circumferences L₁ and L₂ set the overall energy scale
of the sheet.  The electron sheet has circumferences of order
picometers, giving mode energies in the MeV range.  The
proton sheet is ~1000× smaller, pushing energies into the
GeV range.

### Charge from n₁

Charge is determined by a single quantum number: n₁, the
winding on the charge-determining dimension.  The rule is
sharp:

| n₁ | Charge behavior |
|----|----------------|
| ±1 | Carries charge ±e (the Gauss's law integral is nonzero) |
| 0 | No winding → no field asymmetry → zero charge |
| ≥ 2 | Oscillating field pattern integrates to zero → zero charge |

This is the **n₁ = ±1 selection rule**: only modes with
exactly one winding on the first dimension carry electric
charge.  It eliminates 88% of all modes below 2 GeV from
the charged spectrum in a single step.

The electron (1, 2) has n₁ = 1, so it carries charge −1.
A mode like (0, 2) would have the same mass contribution
from n₂ but zero charge — it is electrically invisible.  A
mode like (2, 1) has |n₁| = 2, so its charge integral cancels
despite having nonzero winding.

### Spin from n₁

Spin also comes from n₁:

- **Odd n₁** → fermion (spin ½).  The wave function picks up
  a sign flip after one full trip around the dimension — it
  takes *two* complete circuits to return to its starting
  value.  This half-integer topology is the origin of spin ½.
- **Even n₁** (including zero) → boson (spin 0 or 1).  The
  wave function returns to itself after one circuit.

The electron's n₁ = 1 (odd) makes it a fermion.  A mode
with n₁ = 2 would be a boson.

### A mode catalog for one sheet

Here are the lowest-energy modes on the electron sheet, with
their properties:

| Mode (n₁, n₂) | Charge | Spin | Mass (relative) | Identity |
|----------------|--------|------|-----------------|----------|
| (1, 1)  | −1 | 1 (vector) | ~0.5× m_e | **Ghost** — no known particle |
| (1, 2)  | −1 | ½ | m_e (by definition) | **Electron** |
| (0, 1)  | 0 | 0 (scalar) | ~0.4× m_e | Neutral, invisible |
| (0, 2)  | 0 | 0 (scalar) | ~m_e | Neutral, invisible |
| (1, 3)  | −1 | ½ | ~1.5× m_e | Candidate for heavier lepton |
| (2, 1)  | 0 | 0 (scalar) | ~1.1× m_e | Charge integral cancels |

The (1, 1) mode — lighter than the electron, charged, but
with spin 1 instead of spin ½ — is the most stubborn "ghost
mode."  No such particle has ever been observed.  It survived
five independent attempts to eliminate it, and its eventual
reinterpretation as dark matter is one of the key developments
in the MaSt program.

### Three sheets, six quantum numbers

MaSt has three material sheets — electron, neutrino, and
proton — each with two dimensions.  A mode on the full
six-dimensional material space is labeled by six integers:

    (n₁, n₂, n₃, n₄, n₅, n₆)

where (n₁, n₂) are windings on the electron sheet, (n₃, n₄)
on the neutrino sheet, and (n₅, n₆) on the proton sheet.

**Charge** across sheets:

    Q = −n₁ + n₅

The electron sheet's n₁ contributes negative charge; the
proton sheet's n₅ contributes positive charge.  The neutrino
sheet contributes nothing to charge.  Some examples:

| Mode | Q | Particle |
|------|---|----------|
| (1, 2, 0, 0, 0, 0) | −1 | Electron |
| (0, 0, 0, 0, 1, 2) | +1 | Proton |
| (1, 2, 0, 0, 1, 2) | 0 | Neutron |
| (0, 0, 1, 1, 0, 0) | 0 | Neutrino |

The neutron is a **cross-plane mode** — it has nonzero
windings on both the electron and proton sheets
simultaneously.  Its charge is −1 + 1 = 0.  Cross-plane
modes exist only when the sheets are geometrically coupled
through a parameter called the cross-shear (σ_ep).

**Spin** across sheets follows the same rule: each odd n₁,
n₃, or n₅ contributes one unit of spin ½.  The electron has
one odd winding (n₁ = 1), giving spin ½.  The neutron has
two (n₁ = 1 and n₅ = 1), which combine to give spin ½ or 0.

**Mass** is computed from the full 6D wave equation, using
all six winding numbers plus the geometry (circumferences,
shears, and cross-shears) of the three sheets.

### The particle zoo from geometry

The remarkable feature of this scheme is that every known
particle can be assigned a specific six-number mode, and
its mass computed from the geometry — with no new parameters
beyond those already fixed by the electron, proton, neutron,
and muon.  Predicted masses for kaons, eta mesons, and
hyperons match observation to better than 2%.

The same geometry also predicts modes with no known particle
counterpart — the ghost modes.  Below 2 GeV, there are
roughly 900 of them, outnumbering known particles ~20 to 1.
These modes carry mass but couple weakly to light (suppressed
by the Compton window, Q94), and their charges cancel exactly
in any thermal population (R42).  Their predicted mass ratio
brackets the observed dark-to-visible ratio of 5.4.  Ghost
modes are now a leading candidate for dark matter within the
framework — and the subject of a companion paper.

---

## Summary

| Concept | Mechanism |
|---------|-----------|
| Charge | Total E flux from compact surface (Gauss's law) |
| Mass | Resonance condition: eigenvalue of wave equation on compact geometry |
| Spin ½ | Odd winding on charge-determining dimension → half-integer topology |
| Magnetic moment | B tangent to compact surface → net axial dipole |
| g ≈ 2.0023 | Fraction of energy in external (non-rotating) field |
| Shear → α | Lattice skew of material sheet controls charge magnitude; sin²(2πs) symmetry breaking |
| Quantum numbers | Six integers (n₁–n₆) specify any mode; charge, spin, mass all follow from geometry |

All properties arise from electromagnetic energy on a compact
topology.  No fundamental charge.  No point particle.  Just
energy, topology, and geometry — extended across three
material sheets with six compact dimensions.

---

## References

- WvM paper: [`WvM.pdf`](WvM.pdf),
  summary: [`WvM-summary.md`](WvM-summary.md)
- Maxwell primer: [`maxwell-primer.md`](maxwell-primer.md)
- R6 findings (self-consistency):
  [`studies/R6-field-profile/findings.md`](../studies/R6-field-profile/findings.md)
- S2 findings (charge from geometry):
  [`studies/S2-toroid-geometry/findings.md`](../studies/S2-toroid-geometry/findings.md)
- R19 findings (shear-induced charge):
  [`studies/R19-shear-charge/findings.md`](../studies/R19-shear-charge/findings.md)
- Taxonomy (quantum numbers, modes, parameters):
  [`studies/Taxonomy.md`](../studies/Taxonomy.md)
