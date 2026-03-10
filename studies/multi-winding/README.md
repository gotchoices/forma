# R8. Multi-Winding Electron  *(draft)*

Find the torus geometry — size, aspect ratio, and winding
number — that produces all four measurable electron properties:
charge, mass, spin, and magnetic moment.

## Motivation

R7 showed that the Coulomb self-energy of charge e at the
Compton scale is only ~1% of m_e c²/2.  A Compton-scale torus
cannot store enough electrostatic energy to account for the
electron's charge.

The fix: a **smaller torus** with a **multi-winding path**.
The photon winds many times around the major circle, so the
total path length is still λ_C (giving the correct mass) even
though the torus itself is much smaller (giving the correct
Coulomb energy).

## Physical picture

The photon travels on a path that **locally resembles WvM's
(1,2) helix** — for every two trips around the ring, it makes
approximately one trip around the tube.  But the path doesn't
quite close after one (1,2) circuit.  It precesses slightly,
so each double-orbit is offset by a small angle.  After many
double-orbits, the path finally closes.

This is a **(p, q) torus knot** with p/q ≈ 1/2.  The winding
ratio ~1:2 preserves the spin-½ character of the standard WvM
model.  The large winding number allows the torus to be small.

## The two constraints

### 1. Mass constraint (path length)

The photon's wavelength is λ_C = h/(m_e c).  The path must fit
one (or an integer number of) wavelengths:

    ℓ = λ_C

For a (p, q) knot on a torus with major radius R and minor
radius a:

    ℓ = √((p × 2πa)² + (q × 2πR)²)

With p, q large and p/q ≈ 1/2, this simplifies to:

    ℓ ≈ q × 2πR × √(1 + (a/(2R))²)

### 2. Charge constraint (Coulomb energy)

The electrostatic energy of charge e at a characteristic
distance R must equal m_e c²/2:

    U_Coulomb = e²/(4πε₀ R) = m_e c²/2

This gives R = r_e, the classical electron radius:

    r_e = e²/(4πε₀ m_e c²) ≈ 2.82 × 10⁻¹⁵ m

### What the constraints determine

Combining both constraints:

    q ≈ λ_C / (2πR) ≈ λ_C / (2π r_e) = 1/α ≈ 137

The winding number is not put in by hand — it falls out of
requiring both the correct mass and the correct charge.

| Parameter | Value | Source |
|-----------|-------|--------|
| R | ~r_e ≈ 2.8 × 10⁻¹⁵ m | charge constraint |
| q | ~1/α ≈ 137 | mass + charge |
| p | ~q/2 ≈ 69 | winding ratio for spin ½ |
| a | depends on aspect ratio | to be determined |
| ℓ | λ_C ≈ 2.4 × 10⁻¹² m | mass constraint |

## Spin from the winding ratio

The premise of this study: **spin ½ emerges from the local
winding ratio p:q ≈ 1:2**, just as in WvM.

At any point on the path, the photon is spiraling once around
the tube for every two trips around the ring — exactly the
(1,2) helical structure that produces half-integer angular
momentum in WvM.  The precession is a small perturbation
(~5° per double-orbit) that doesn't change the local winding
character.

This is analogous to a screw thread: the pitch (and hence the
mechanical advantage) is determined by the local helix angle,
not by whether the screw is 1 cm or 100 cm long.

The study treats this as a working hypothesis and checks it by
computing the angular momentum of the resulting field
configuration.

## The (p, q) torus knot

For a single connected path, p and q must be coprime.  Since
p/q ≈ 1/2 but (p, 2p) has gcd = p, the exact winding numbers
must be slightly off from the 1:2 ratio.  Candidates:

| (p, q) | p/q | gcd | ≈ (1,2) circuits |
|--------|-----|-----|------------------|
| (68, 137) | 0.4964 | 1 | 68.5 |
| (69, 139) | 0.4964 | 1 | 69.5 |
| (34, 69)  | 0.4928 | 1 | 34.5 |

The exact (p, q) will be determined by which winding number
gives a self-consistent solution.  The slight deviation from
exactly 1:2 is the precession.

## Precession mechanism: sheared T²

On a standard flat T² (rectangular lattice), geodesics are
straight lines that close exactly — a (1,2) path closes after
2 orbits with no precession.

For multi-winding to occur, the compact space must have a
**sheared identification**: the two compact dimensions are
slightly tilted (non-orthogonal).  Concretely, when the photon
crosses the φ boundary, it re-enters with a small offset δ in
the θ direction.

This is equivalent to a parallelogram lattice instead of a
rectangle.  The space is still flat (zero curvature) — only the
boundary identification changes.

The photon travels in a straight line, but each (1,2)-like
double-orbit, it misses the start by δ.  After N double-orbits:

    N × 2δ = L_θ    →    N = L_θ / (2δ)

The tilt ratio δ/L_θ is a property of the compact space.
Understanding why it has a particular value is a follow-up
question — this study just finds the geometry that works.

## Computational approach

### Key insight: the shape factor

The Coulomb self-energy of a uniform surface charge Q on a
torus scales as:

    U = Q² × g(r) / (4πε₀ R)

where g(r) is a dimensionless shape factor depending only on
the aspect ratio r = a/R.  It does NOT depend on the absolute
size — all distances scale with R.

This means: compute g(r) once per aspect ratio (at unit scale),
then derive everything else analytically.

### Step 1: Compute g(r)

For a torus at unit scale (R = 1, a = r) with unit total
charge distributed uniformly on the surface, compute the
Coulomb self-energy by direct pairwise summation:

    g(r) = Σ_{i<j} dq_i × dq_j / |r_i − r_j|

This reuses R7's surface charge discretization but replaces
the expensive 3D grid integration with a direct sum — much
faster and more accurate.

### Step 2: Derive the solution curve

Setting U = m_e c²/2 with Q = e:

    R = 2 g(r) × r_e

where r_e = e²/(4πε₀ m_e c²) is the classical electron radius.

The winding number follows from the path constraint ℓ = λ_C:

    q = λ_C / (2πR √(1 + r²/4))
      = 1 / (2α g(r) √(1 + r²/4))

This gives a continuous curve q(r).  Each aspect ratio r maps
to a specific winding number q.

### Step 3: Find integer solutions

Since q must be an integer, the solution is a discrete set of
points along the q(r) curve.  For each integer q, there is a
corresponding r (and hence R, a, p).

### Step 4: Examine the results

- What winding numbers fall in a physically reasonable range?
- Is there a clean geometric expression for the aspect ratio?
- Spin verification is a follow-up (angular momentum
  computation of the field).

## Follow-up questions (not part of this study)

These become relevant only after a working geometry is found:

- **What determines the precession?**  The sheared-T² mechanism
  provides a framework (the tilt ratio δ/L_θ), but why does the
  tilt have a particular value?  This might come from a
  self-consistency condition or a deeper symmetry.

- **Can α be derived?**  If the tilt ratio δ/L_θ has a geometric
  origin, α could follow.  This is a long-term goal.

- **Magnetic moment and g-factor.**  Should carry over from WvM
  if the local (1,2) structure is preserved.  Worth verifying.

## Comparison with previous models

| | WvM (1,2) | S2/R6 | R7 | R8 (this) |
|---|-----------|-------|-----|-----------|
| Torus scale | Compton | Compton | Compton | Classical e⁻ radius |
| Winding | 2 | 2 | 2 | ~137 |
| Coulomb energy | Assumed OK | Assumed OK | 1% of target | Target |
| Charge mechanism | Energy balance | Energy balance | Direct Coulomb | Direct Coulomb |
| Spin ½ | From q=2 | From q=2 | From q=2 | From ratio ~1:2 |

## References

- R7 findings:
  [`torus-capacitance/findings.md`](../torus-capacitance/findings.md)
- Charge-from-energy primer:
  [`ref/charge-from-energy.md`](../../ref/charge-from-energy.md)
- R6 (self-consistent geometry):
  [`field-profile/findings.md`](../field-profile/findings.md)
