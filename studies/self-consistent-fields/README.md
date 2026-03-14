# R12. Self-Consistent Fields on the Sheared T²

Can the shear (and hence α) be derived from field
self-consistency alone — without using the measured charge
as an input?

## Motivation

R8 found a continuous family of electron geometries: every
odd q from ~100 to ~287 satisfies mass + charge + spin.
R11 showed that q ~ 1/α is partly tautological — it follows
from using the measured e in the Coulomb energy constraint.
No energy-cost or number-theoretic mechanism selects a
specific q.

The real free parameter is **r** (the aspect ratio a/R), not
q.  The two are related by:

    q(r) = 1 / (2α × g(r) × √(1 + r²/4))

To break the circularity, we need a constraint on r (or
equivalently δ, the shear) that does NOT use e as input.

## Approach

Solve the wave equation on a sheared T² parameterized by
the shear δ.  Determine which values of δ permit
self-consistent, single-valued, normalizable field
configurations.

If only discrete δ values work, the model predicts α from
geometry alone.  If a continuum of δ works, the model has a
genuine free parameter and needs additional physics.

## Tracks

### Track 1: Spectral structure of flat sheared T² ✓
**Type:** analytical + numerical
**Result:** The Compton frequency ω_C is ~137× below the
lowest torus eigenmode (ω_C/ω_min = 2gα ≈ α).  No
eigenmode exists at ω_C for any geometry or shear value.
The phase coherence condition is identical to the mass
condition.  **The flat-T² wave equation cannot constrain
the shear.**

Key insight: the photon is NOT a torus eigenmode.  It is
a propagating wave whose wavelength spans the entire path
(all q orbits).  The self-consistency question must be
reformulated as a propagation problem, not an eigenvalue
problem.

### Track 2: Propagating wave on curved torus *(next)*
**Type:** numerical

Track 1 showed eigenmodes are the wrong framework.  The
correct question: can a propagating EM wave at ω_C,
traveling along the geodesic on the CURVED torus,
maintain its field profile after q orbits?

The (1 + r cos θ) metric factor modulates the wave on
each orbit.  After q orbits, the transverse profile must
return to its starting shape (self-consistency).  This
constrains the allowed geometries.

### Track 3: Transverse waveguide modes *(future)*
**Type:** analytical + numerical

The curved torus metric creates an effective waveguide
in the θ direction.  Compute the transverse mode
structure and determine whether it constrains the aspect
ratio r.

### Track 4: Self-consistent boundary conditions *(future)*
**Type:** theoretical

Investigate whether the shear itself can emerge from the
field's back-reaction on the geometry — i.e., the field
determines the shear, and the shear determines the field.
This is the moduli-stabilization approach: the shear is a
modulus of the T² whose effective potential is generated
by the field energy.

## What we abstract

- **Geometry:** Sheared T² with shear δ as the free
  parameter (or equivalently r, since δ = πra/q for
  given R, a).
- **Field:** Start with scalar, promote to EM.
- **Constraint:** Self-consistent propagation at ν_C.

## Key question

Does the self-consistency condition constrain δ to a
discrete set?  If one of those values gives α ≈ 1/137,
the model is genuinely predictive.

## Dependencies

- R8 solution curve (geometry_search.py)
- R11 findings (esp. mode spectrum from Track 8)

## References

- R8: [`multi-winding/`](../multi-winding/)
- R11: [`prime-resonance/`](../prime-resonance/)
- Q18 (derive α), Q29 (variational principle)
