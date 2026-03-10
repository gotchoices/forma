# Charge from Torus Geometry  *(draft)*

Compute the torus dimensions that produce q = e, using exact
electrostatics with the field profile determined by the
synchronized circular polarization mechanism.

## Physical picture

The photon is circularly polarized on the (1,2) geodesic.  Its
polarization rotation is synchronized with the geometric winding
around the minor circle: as the surface normal rotates by 2π in
3D, the circular polarization rotates by 2π in the opposite
sense.  These cancel, producing a field that is always normal
to the torus surface with constant magnitude E₀.

(See [`ref/charge-from-energy.md`](../../ref/charge-from-energy.md)
§2 for the derivation.)

This is equivalent to a **uniform surface charge distribution**
on the torus.  The charge is real (nonzero Gauss's law flux),
not an artifact of an energy-matching approximation.

## What this study computes

Given a torus with major radius R and minor radius a
(aspect ratio r = a/R):

1. **Self-capacitance C(R, a).**  Place uniform charge Q on the
   torus surface.  Solve for the potential in 3D.  Compute
   C = Q / V_surface.  This is a purely geometric quantity
   (times ε₀) — it doesn't depend on Q.

2. **Charge as a function of geometry.**  The E-field energy of
   charge q on a surface with self-capacitance C is U_E = q²/(2C).
   Setting U_E = m_e c²/2:

       q(r) = √(m_e c² × C(R(r), a(r)))

   where R(r) and a(r) come from the path constraint
   2π√(4R² + a²) = λ_C.

3. **Aspect ratio for q = e.**  Sweep r to find the value where
   q(r) = e.  This is the self-consistent geometry — the electron.

## Why this works

The synchronized CP mechanism eliminates the arbitrary choices
in previous approaches:

| Method | Arbitrary choices | Field profile |
|--------|-------------------|---------------|
| WvM    | Volume V, matching radius | Uniform in sphere |
| S2/R6  | Effective volume formula   | Uniform in torus volume |
| This   | None                       | Uniform on surface (from synchronized CP) |

The surface field profile is physically determined by the
circular polarization mechanism.  The self-capacitance captures
exactly how that surface field extends into 3D and stores energy.
No assumed volumes, no matching radii, no δ.

## Path constraint

The photon's geodesic path length equals one Compton wavelength:

    ℓ = 2π√(4R² + a²) = λ_C

This fixes R as a function of r:

    R(r) = λ_C / (2π√(4 + r²))
    a(r) = r × R(r)

## Self-capacitance of a torus

For a torus with uniform surface charge, the self-capacitance
depends on the aspect ratio r = a/R:

- **Ring torus (r < 1):** Analytic solutions exist using
  toroidal coordinates (η, θ, φ) and half-integer Legendre
  functions Q_{n-½}.  Well-studied problem.

- **Spindle torus (r > 1):** The 3D embedding self-intersects.
  The analytic toroidal-coordinate approach breaks down.
  Numerical methods (BEM) are needed.

Previous studies found r ≈ 4–7, so we expect to be deep in the
spindle regime.  The BEM approach handles this naturally.

## Implementation

**Primary: Boundary Element Method (BEM)**

1. Discretize the torus surface into N panels
2. Place a point charge at each panel center
3. Compute the N×N influence matrix (potential at panel i due
   to unit charge at panel j)
4. Solve for the charge distribution that produces uniform
   potential on the surface → conductor capacitance
5. Also compute capacitance for uniform charge distribution
   (our physical case — may differ from conductor result)
6. Sweep r from 0.1 to 10+, computing C(r) at each value
7. Combine with path constraint to get q(r)
8. Find r where q = e

**Cross-check: Analytic (r < 1 only)**

For a conducting torus with a < R, the self-capacitance can be
expressed as a series involving Q_{n-½}(cosh η₀).  Compare
with BEM results in the ring-torus regime.

## Key questions

1. **What aspect ratio gives q = e?**  This is the main result.
   Previous approximations gave r ≈ 6.60 (S2) or r ≈ 4.29 (R6).
   The exact electrostatics should give a definitive value.

2. **Is r a clean geometric expression?**  If r involves simple
   factors of π, that would be a clue toward deriving α from
   geometry.

3. **How does the uniform-charge C compare to the conductor C?**
   The synchronized CP gives uniform surface charge, not the
   equilibrium (conductor) distribution.  If these give very
   different capacitances, the charge mechanism matters.  If
   similar, the result is robust.

4. **How sensitive is q to r?**  The slope dq/dr at the solution
   tells us how tightly the geometry is constrained.

## Open question: mode structure

The synchronized CP picture requires the polarization rotation
to match the geometric winding (one-to-one).  On flat T² with
a (1,2) geodesic, a simple plane-wave mode has ψ = θ + 2φ,
giving multiple oscillations per circuit — not perfectly
synchronized.

This study proceeds under the assumption that the synchronized
state exists (as WvM describes).  The mechanism might involve
waveguide-like behavior (phase fronts determined by the minor-
circle geometry while energy propagates along the geodesic), or
it might require the compact space to have slight curvature.
Resolving this is a separate problem.

## References

- Charge-from-energy primer:
  [`ref/charge-from-energy.md`](../../ref/charge-from-energy.md)
- R6 (self-consistent geometry):
  [`field-profile/findings.md`](../field-profile/findings.md)
- S2 (energy-balance charge):
  [`toroid-geometry/findings.md`](../toroid-geometry/findings.md)
- R1 (KK charge comparison):
  [`kk-charge/findings.md`](../kk-charge/findings.md)
