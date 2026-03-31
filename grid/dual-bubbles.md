# The Dual-Bubble Conservation Law

**Status:** Framing — a geometric interpretation of a known
identity, placed within the GRID/MaSt context.  No new
computational predictions yet.

---

## The observation

Every massive object defines two characteristic length
scales:

**The Compton wavelength** (EM / quantum bubble):

<!-- λ_C = ℏ / (mc) -->
$$
\lambda_C = \frac{\hbar}{m\,c}
$$

This is the quantum extent of the object — the scale below
which its wave nature dominates.  In MaSt, it corresponds
to the physical size of the compact torus (the material
sheet wrapping).

**The Schwarzschild radius** (gravitational bubble):

<!-- r_s = 2Gm / c² -->
$$
r_s = \frac{2\,G\,m}{c^2}
$$

This is the gravitational extent — the scale at which the
object's mass produces order-unity spacetime curvature.

These two radii are inversely related through mass: as m
increases, λ_C shrinks and r_s grows.  They bracket the
Planck mass symmetrically.

---

## The conservation law

The product of the two radii is **independent of mass**:

<!-- λ_C × r_s = (ℏ/mc)(2Gm/c²) = 2ℏG/c³ = 2 L_P² -->
$$
\lambda_C \times r_s
  = \frac{\hbar}{m\,c} \cdot \frac{2\,G\,m}{c^2}
  = \frac{2\,\hbar\,G}{c^3}
  = 2\,L_P^2
$$

The mass cancels exactly.  The product is always twice the
Planck area — a constant set by the fundamental constants
ℏ, G, and c.

In natural units (ℏ = c = 1):

<!-- λ_C × r_s = 2G = 1/(2ζ) -->
$$
\lambda_C \times r_s = 2G = \frac{1}{2\zeta}
$$

using the GRID result G = 1/(4ζ) from
[gravity.md](gravity.md).

**The dual-bubble product is set by the lattice resolution
ζ alone.**

---

## Examples

| Object | Mass (kg) | λ_C (m) | r_s (m) | Product |
|--------|-----------|---------|---------|---------|
| Electron | 9.11 × 10⁻³¹ | 3.86 × 10⁻¹³ | 1.35 × 10⁻⁵⁷ | 2 L_P² |
| Proton | 1.67 × 10⁻²⁷ | 2.10 × 10⁻¹⁶ | 2.48 × 10⁻⁵⁴ | 2 L_P² |
| Planck mass | 2.18 × 10⁻⁸ | 1.62 × 10⁻³⁵ | 3.23 × 10⁻³⁵ | 2 L_P² |
| Earth | 5.97 × 10²⁴ | 5.89 × 10⁻⁶⁸ | 8.87 × 10⁻³ | 2 L_P² |
| Sun | 1.99 × 10³⁰ | 1.77 × 10⁻⁷³ | 2.95 × 10³ | 2 L_P² |

For m < m_P (particles, atoms): the EM bubble dominates.
Quantum effects are enormous; gravity is negligible.

For m > m_P (planets, stars): the gravitational bubble
dominates.  Gravity rules; quantum effects are negligible.

At m = m_P: the two radii are equal (up to a factor of 2).
This is the only scale where both effects matter equally —
the domain of quantum gravity.

---

## The embedding mechanism

### Flat grid, warped embedding

In GRID/MaSt, a material sheet (Ma) is a flat 2D triangular
lattice wrapped into a torus.  "Flat" means all edges are
Planck length, all triangles are equilateral — the internal
geometry is undistorted.

When this torus is embedded in the 3D spatial lattice (S),
the sheet's flatness is preserved.  It is the **ambient
spatial lattice** that must accommodate the embedded
object.  The ambient lattice rearranges around the torus,
and this rearrangement is what we observe as spacetime
curvature.

This inverts the usual causal framing of general relativity.
We normally say "mass-energy curves spacetime" and leave the
mechanism unspecified.  The GRID picture proposes a specific
mechanism:

1. A particle is a flat compact torus embedded in the
   spatial lattice
2. The torus has rigid internal geometry (equilateral
   triangles, edge length = L_P)
3. The ambient lattice deforms to fit the torus
4. The deformation has an entropy cost (δS = ζ δA)
5. The Jacobson argument converts the entropy cost into
   the Einstein equations

The Compton wavelength λ_C is the **internal** scale —
the size of the torus.  The Schwarzschild radius r_s is
the **external** scale — the extent of the ambient
deformation.

### Conservation of geometric disturbance

The dual-bubble law λ_C × r_s = 1/(2ζ) then becomes:

> **(internal geometry) × (external deformation) = constant**

The total geometric footprint of any object — the product
of its compact size and its ambient imprint — is fixed by
the lattice resolution.  You can trade internal compactness
for external curvature (increase mass: smaller torus, bigger
gravitational bubble) or vice versa, but the product is
locked.

This resembles a **geometric uncertainty principle**:

- You cannot make an object both internally small (high
  mass, small Compton wavelength) and gravitationally
  invisible (small Schwarzschild radius)
- The lattice does not have enough information capacity to
  simultaneously resolve both scales beyond the Planck
  limit
- The minimum of the product, 2 L_P², is set by ζ

### Conjugate variables

The Compton wavelength and the Schwarzschild radius behave
like **conjugate variables**:

| Property | λ_C (Compton) | r_s (Schwarzschild) |
|----------|---------------|---------------------|
| Origin | Quantum / EM | Gravitational |
| Scales as | 1/m | m |
| Domain | UV (short distances) | IR (long distances) |
| GRID source | Compact torus geometry | Ambient lattice deformation |
| MaSt role | Sets particle size, modes | Sets gravitational field |
| Product | 2 L_P² | 2 L_P² |

This is the **UV/IR connection** — a well-known feature of
quantum gravity theories.  GRID gives it a concrete
geometric interpretation: the UV (compact torus) and IR
(ambient deformation) are two aspects of the same lattice.
The information that defines the torus (its compactness) is
"borrowed" from the ambient lattice (creating curvature).

---

## What this is and what it isn't

### What it is

This document is a **framing** — a geometric interpretation
of a known identity (λ_C × r_s = 2 L_P²) within the GRID
lattice picture.  The identity itself is a straightforward
consequence of the definitions of λ_C, r_s, and L_P.  The
new content is the proposed *mechanism*: the flat torus
forces ambient deformation, and the conservation law reflects
the finite information capacity of the lattice.

The dual-bubble law is **exact** and follows from:
- The definition of the Compton wavelength (QM)
- The definition of the Schwarzschild radius (GR)
- The Planck length L_P = √(ℏG/c³)

No additional assumptions are needed for the identity itself.

### What it isn't

This is **not** a new prediction or derivation.  The identity
λ_C × r_s = 2 L_P² is dimensional analysis — it holds in any
theory that has ℏ, G, and c.  The GRID interpretation adds
physical meaning (flat torus vs ambient deformation) but does
not produce a testable consequence beyond what GR + QM
already give.

To go beyond framing, we would need:
- A computational model of the embedding (how specifically
  does the ambient lattice deform around a flat torus?)
- A derivation that the entropy cost of the deformation
  gives exactly δS = ζ δA (connecting the embedding to the
  Jacobson argument)
- A prediction that differs from standard GR + QM (e.g., a
  correction to the gravitational field of a particle due
  to the discrete lattice structure)

---

## Connections

| Concept | Reference | Relationship |
|---------|-----------|--------------|
| Compton-Schwarzschild correspondence | Carr, 2015; Lake, 2019 | Same identity, interpreted as mass-dependent duality |
| UV/IR connection | Susskind, 1995; Cohen et al., 1999 | The short-distance / long-distance link in quantum gravity |
| Israel junction conditions | Israel, 1966 | How a thin shell of matter (flat inside) curves the ambient spacetime |
| Braneworld models | Randall-Sundrum, 1999 | Flat brane embedded in curved bulk — structurally similar |
| GRID entropy mechanism | [gravity.md](gravity.md) | δS = ζ δA drives Einstein's equations |
| MaSt particle geometry | [compact-dimensions.md](compact-dimensions.md) | Particles as wrapped flat tori |

---

## Open questions

1. **Is the embedding literal?**  Does the Ma torus
   physically sit inside the S lattice as a geometric
   sub-structure, or is the "embedding" only topological
   (identification of lattice sites)?

2. **Does the ambient deformation reproduce Newtonian
   gravity at large r?**  If so, the 1/r² law should
   emerge from the geometry of the deformation around a
   flat torus in a 3D lattice.

3. **Is the dual-bubble product exactly 2 L_P², or could
   lattice corrections modify it?**  At the Planck scale,
   the continuum definitions of λ_C and r_s break down.
   The lattice might impose corrections of order L_P.

4. **Can this be simulated?**  A small 2D lattice with an
   embedded "particle" (a closed loop of fixed-length edges)
   could be relaxed to find the equilibrium ambient
   configuration.  The entropy of that configuration could
   be compared to ζ δA.

5. **Does the conjugate-variable structure imply a
   commutation relation?**  If λ_C and r_s are truly
   conjugate in the lattice, there might be an operator
   algebra [λ̂_C, r̂_s] ∝ L_P² analogous to [x̂, p̂] = iℏ.
