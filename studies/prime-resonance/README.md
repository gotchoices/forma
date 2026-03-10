# R11. Prime Resonance / Least-Expensive Path

Study whether the winding number q is selected by resonance
quality, energy minimization, or number-theoretic constraints
(primality).

## Motivation

R8 found a one-parameter family of valid electron geometries:
every odd q from ~100 to ~287 satisfies the mass constraint
(path = λ_C) and the charge constraint (U_Coulomb = m_e c²/2).
Something else must select the specific q — and hence α.

Three hypotheses:

1. **Energy minimization.**  The Coulomb self-energy of charge
   along the actual geodesic path differs from the uniform
   surface charge assumed in R8.  The excess energy varies
   with q.  The minimum-energy q is the ground state.

2. **Resonance quality.**  The photon's EM field must
   constructively self-interfere after q orbits (one Compton
   cycle).  Some q values produce cleaner resonances with
   less energy leakage to non-fundamental modes.

3. **Primality filter.**  For composite q, every divisor
   creates a sub-period in the field pattern — a potential
   channel for energy to leak from the fundamental Compton
   resonance.  For prime q, no such channels exist.  137 is
   prime; its neighbors 135 = 3³×5, 136 = 2³×17, 138 = 2×3×23,
   140 = 2²×5×7 all have many divisors.

## What we abstract

- **Spin: LOCKED at 1:2.**  The geodesic slope is fixed.
  Exact spin-½ is maintained for all q.

- **Winding number q: SWEPT.**  This is the independent
  variable.  Each q implies a specific shear δ = L_θ/(2q),
  geometry (R, a), and charge distribution.

- **Geometry (R, a): DERIVED** from q via the R8 solution
  curve (mass + Coulomb energy constraints).

## Tracks

### Track 1: Divisor spectrum and sub-harmonic structure
**Type:** analytical / number theory

For each q in the solution range (~100–287):
- Factorize q, count divisors, compute sub-harmonic score
- Identify primes vs composites
- Analyze whether the sheared T² permits sub-periodic
  geodesic closure for composite q
- Compute divisor-weighted sub-harmonic coupling metric

### Track 2: Geodesic Coulomb self-energy
**Type:** numerical

For each q, compute the Coulomb self-energy of charge e
distributed along the actual (p, q) geodesic path on the
3D torus.  Compare to the uniform-surface-charge energy
(which is m_e c²/2 by construction for all q).

The geodesic charge distribution is more concentrated than
uniform, so U_geodesic > U_uniform.  The *excess* energy
U_excess(q) = U_geodesic − m_e c²/2 varies with q because
higher q covers the torus more densely.  If U_excess has a
minimum, that q is the ground state.

### Track 7: Wave superposition / sub-harmonic test
**Type:** numerical (Fourier analysis)

Test the Q30 hypothesis: do composite q leak energy to
sub-harmonic frequencies?  Superimpose the wave contributions
from all q orbits (with geometry-dependent amplitude
modulation) and compare the power spectrum for prime vs
composite q.

**Result: No distinction.**  Power at any frequency depends on
the kernel's Fourier structure, not q's divisibility.  Since
gcd(p,q) = 1 for all q, orbit positions always form a complete
residue system — the prime/composite structure is invisible.

### Track 3: Magnetic self-energy *(next)*

Compute the Biot-Savart magnetic self-energy of the geodesic
current.  This is a 1D-vs-1D comparison (no dimensionality
mismatch), so it may converge better than Coulomb.

### Track 8: Wave equation eigenvalues *(future)*

Solve the scalar Helmholtz equation on the sheared T² and
find which shear values permit standing-wave solutions.

### Track 6: Continuous δ sweep *(future)*

For selected q, sweep δ continuously and check whether the
phase-coherence optimum coincides with the spin-½ value
δ = L_θ/(2q).

## Dependencies

- R8 solution curve (geometry_search.py)
- `lib/constants.py` for physical constants

## References

- R8: [`multi-winding/`](../multi-winding/)
- Q29 (variational principle), Q30 (prime q)
