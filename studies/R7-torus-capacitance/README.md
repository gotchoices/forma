# R7. Charge from Torus Geometry  *(concluded)*

Find the torus aspect ratio that produces q = e by computing
the exact 3D field of a circularly polarized photon on a (1,2)
geodesic.

## Physical picture

The photon is circularly polarized on the (1,2) geodesic.  Its
polarization rotation is synchronized with the geometric winding
around the minor circle: as the surface normal rotates by 2π in
3D, the circular polarization rotates by 2π in the opposite
sense.  These cancel, producing an E field that is always normal
to the torus surface with constant magnitude E₀ at the photon's
location.

(See [`primers/charge-from-energy.md`](../../primers/charge-from-energy.md)
§2 for the derivation.)

The photon travels along the (1,2) geodesic — a 1D curve on the
torus surface.  It is NOT spread over the entire surface.  The
torus surface itself is just a visualization of the Ma_e (the electron sheet) topology;
it has no physical existence.  Only the path carries the field.

## Strategy

We use q = e as an input and find the geometry that is
consistent with it.  This is "backing in" — we set the charge
and solve for the aspect ratio r = a/R.

Once we know r, we examine whether it has a clean geometric
form (multiples of π, etc.) that might suggest a deeper
principle.  If so, a future study could attempt to run the
logic in reverse: derive r from that principle and predict e.

## What this study computes

Given a torus with major radius R, minor radius a, and
aspect ratio r = a/R:

1. **Path constraint (mass).**  The geodesic path length equals
   one Compton wavelength:

       ℓ = 2π√(4R² + a²) = λ_C

   This fixes R and a as functions of r:

       R(r) = λ_C / (2π√(4 + r²))
       a(r) = r × R(r)

2. **Line source along the geodesic.**  Distribute total charge
   Q = e uniformly along the (1,2) torus knot path.  At each
   point on the path, the E field contribution points along the
   local surface normal n̂ (from synchronized CP).

3. **3D field computation.**  Sum the E field contributions from
   all path segments to get E(P) at any point P in 3D space.
   This is a direct integration — no surface charge, no BEM,
   no assumed volumes.

4. **Energy check.**  Compute the total E-field energy:

       U_E = ½ε₀ ∫ E² dV

   The correct geometry satisfies U_E = m_e c²/2.

5. **Sweep r.**  Repeat steps 1–4 for a range of aspect ratios.
   Find r where U_E(r) = m_e c²/2.  This is the electron's
   geometry.

## Why this is better than previous approaches

| Method | Source model | Arbitrary choices |
|--------|-------------|-------------------|
| WvM    | Uniform field in sphere | Volume, matching radius |
| S2/R6  | Uniform field in torus volume | Effective volume formula |
| This   | Line source along geodesic | None |

The field profile is physically determined: a circularly
polarized photon on a specific path.  The 3D field follows from
direct integration.  No assumed distributions, no matching.

## Energy integral and the cutoff

For a line source, E ~ 1/d near the path (d = distance to the
nearest point on the geodesic).  The energy density E² ~ 1/d²,
and the volume element in cylindrical coordinates around the
path goes as d·dd·ds.  The energy integral therefore has a
logarithmic divergence:

    U_E ~ (Q²/ℓ) × ln(D/d_min)

where D is the outer scale (~R) and d_min is the inner cutoff.

The divergent near-field energy is geometry-independent — it
depends only on d_min, not on R or a.  The geometry-dependent
part (the interaction between different segments of the path)
is finite.  Therefore:

- The value of r where U_E = m_e c²/2 is insensitive to d_min
  (changing d_min shifts U_E by a constant for all r).
- Numerically, using a finite grid spacing as d_min is adequate.

## Looking ahead: deriving e

This study uses q = e as input.  A more ambitious goal would
be to predict q from the geometry alone (without feeding in e).
The forward calculation is:

1. Fix r → geometry from path constraint
2. Place a line source with unknown E₀ along the geodesic
3. Compute total field energy: U(E₀, r) = E₀² × f(r)
4. Set U = m_e c²/2 → determines E₀(r)
5. Compute total flux → q(r)

This gives q as a function of r.  But nothing in the current
model selects a specific r — that would require a third
constraint (stability, quantization, gravitational
self-consistency) equivalent to deriving α from first
principles.  This is a long-term open problem.

If the aspect ratio from this study turns out to be a clean
geometric expression, that would be a strong hint toward
identifying the missing third constraint.

## Open question: mode structure

The synchronized CP picture requires the polarization rotation
to match the geometric winding (one-to-one).  On flat Ma_e with
a (1,2) geodesic, a simple plane-wave mode has ψ = θ + 2φ,
giving multiple oscillations per circuit — not perfectly
synchronized.

This study proceeds under the assumption that the synchronized
state exists (as WvM describes).  The mechanism might involve
waveguide-like behavior (phase fronts determined by the minor-
circle geometry while energy propagates along the geodesic), or
the material space might have curvature from the embedded energy.
Resolving this is a separate problem.

## References

- Charge-from-energy primer:
  [`primers/charge-from-energy.md`](../../primers/charge-from-energy.md)
- R6 (self-consistent geometry):
  [`R6-field-profile/findings.md`](../R6-field-profile/findings.md)
- S2 (energy-balance charge):
  [`S2-toroid-geometry/findings.md`](../S2-toroid-geometry/findings.md)
- R1 (KK charge comparison):
  [`R1-kk-charge/findings.md`](../R1-kk-charge/findings.md)
