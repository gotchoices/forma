# Electrostatic Charge from Torus Self-Capacitance  *(draft)*

Compute the electron's charge from exact electrostatics rather
than WvM's energy-balance approximation.

## Motivation

All previous charge calculations (WvM, S2, R6) use the same
energy-balance shortcut: assume a field distribution, compute
average E, match to Coulomb at some radius, extract q.  This
involves arbitrary choices (volume, matching radius, profile
shape) and gives different answers depending on those choices
(S2: r = 6.60, R6: r = 4.29).

This study replaces the shortcut with exact electrostatics.

## Approach

### Physical setup

The photon is a (1,2) plane wave on the flat T².  Its E field
is uniform on the rectangle and points perpendicular to it —
into 3+1D spacetime.  When the T² is embedded as a torus in 3D,
this maps to a known surface charge distribution (uniform on T²,
non-uniform on the 3D torus due to the Jacobian of the
embedding).

### The computation

1. **Define the torus geometry.**  Major radius R, minor radius a,
   parameterized by aspect ratio r = a/R.  Path constraint:
   2π√(4R² + a²) = λ_C.

2. **Solve the electrostatic problem.**  Place the known surface
   charge distribution on the torus.  Solve Laplace's equation
   (∇²φ = 0) outside the torus to get the potential and E field
   everywhere in 3D.  This is a standard boundary-value problem
   in toroidal coordinates using Legendre functions, or
   numerically via boundary element methods.

3. **Compute self-capacitance.**  C(R, a) = Q / V_surface, where
   V_surface is the potential at the torus surface for total
   charge Q.  This is a purely geometric quantity (times ε₀).

4. **Extract the charge.**  The E field energy of charge q on a
   surface with self-capacitance C is U_E = q²/(2C).  Setting
   U_E = m_e c²/2:

       q(r) = √(m_e c² × C(R(r), a(r)))

   where R(r) and a(r) come from the path constraint.  This
   gives q as a function of aspect ratio r.

5. **Find r for q = e.**  Sweep r to find the value where
   q(r) = e.  This is the rigorous self-consistent geometry.

### What this improves over WvM/S2/R6

| Method | Arbitrary choices | Field geometry |
|--------|-------------------|----------------|
| WvM    | Volume V, matching radius R | Uniform in sphere |
| S2/R6  | Effective volume formula | Uniform in torus |
| This   | None (exact electrostatics) | Solved from Laplace's equation |

The only remaining assumption is the surface charge distribution
(uniform on T², from the plane-wave mode).

### What this does NOT do

This calculation still requires setting q = e to determine the
aspect ratio.  It does not independently predict q or α.  The
aspect ratio r remains a free parameter fixed by the charge
condition.  An independent prediction of r (and hence α) would
require solving the wave equation to determine the mode profile
from first principles — a harder problem (see backlog: "Wave
equation on T²").

## Key questions

1. **Does the exact self-capacitance give a different r than
   R6's approximate formula?**  R6 found r ≈ 4.29 using the
   WvM volume formula.  The exact electrostatics may shift this.

2. **Is the required r a clean expression?**  If r turns out to
   be a simple geometric constant (involving only π), that would
   be a clue toward deriving α.

3. **Does the spindle torus (a > R) cause problems?**  For
   r > 1, the 3D embedding self-intersects.  Electrostatic
   solutions for spindle tori may need special handling.

4. **How sensitive is q to the aspect ratio?**  A steep q(r)
   curve means the geometry is tightly constrained; a flat curve
   means small changes in the model could shift q significantly.

## Implementation

The self-capacitance of a torus can be computed via:

- **Analytical:** Toroidal coordinates (η, θ, φ) with Legendre
  functions Q_{n-½}.  Known results exist for conducting tori.
  Our non-uniform distribution requires modification.
- **Numerical:** Boundary element method (BEM) — discretize the
  torus surface, place charge elements, solve for potentials.
  Straightforward to implement in Python.

The BEM approach is more flexible (handles any a/R, including
spindle tori) and avoids the analytic complexity of toroidal
harmonics.  Recommended as the primary method, with analytic
formulas as a cross-check for a/R < 1.

## References

- R6 (self-consistent geometry):
  [`field-profile/findings.md`](../field-profile/findings.md)
- S2 (charge formula):
  [`toroid-geometry/findings.md`](../toroid-geometry/findings.md)
- Charge-from-energy primer:
  [`ref/charge-from-energy.md`](../../ref/charge-from-energy.md)
