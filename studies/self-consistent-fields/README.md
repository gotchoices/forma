# R12. Self-Consistent Fields on the Sheared T²

**Status: COMPLETE** — see [`findings.md`](findings.md)

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

### Track 2: Geodesics on the curved torus ✓
**Type:** analytical + numerical
**Result:** The flat-torus (1,2) geodesic has angular
momentum L_flat > R − a, making it INCOMPATIBLE with
wrapping on the curved torus.  The actual curved geodesic
(L* ≈ R − a) concentrates near the inner equator, giving
q ≈ 193 (not 137).  Holonomy is zero (Gauss-Bonnet).
**Key insight:** the compact space MUST be intrinsically
flat (not the embedded curved torus) for the model to
give q ~ 1/α.

### Track 3: Self-consistent propagation *(closed — trivial)*

F7 asked whether propagation self-consistency could
constrain the geometry.  Under the corrected two-domain
picture (flat interior), this is trivially satisfied:
a traveling wave on flat T² experiences no curvature
modulation, no polarization rotation, and no profile
evolution.  The only condition is the mass condition
(phase matching), already satisfied by construction.

The non-trivial version (gravitational self-consistency,
where the wave's own energy influences the embedding)
is R13 Track 4.

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
