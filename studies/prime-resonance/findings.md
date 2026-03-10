# R11. Prime Resonance — Findings

## Track 1: Divisor spectrum and sub-harmonic structure

### F1. No sub-periodic geodesic closure on the sheared T²

On a sheared T² with δ = L_θ/(2q), the 1:2 geodesic closes
at lattice winding (n, m) when n = m(q−1)/(2q) is an integer.
Since gcd(q, q−1) = 1, the smallest m giving integer n is
always m = q — regardless of whether q is prime or composite.

**The path always makes exactly q orbits before closing.**
No sub-periodic closures exist for any q.  Verified
analytically and numerically for q = 131, 135, 136, 137,
139, 140.

This means the prime/composite distinction does NOT affect
the geodesic path topology.  If primality matters physically,
it must enter through the field structure (mode coupling,
radiation spectrum, or energy), not the path geometry.


### F2. Divisor spectrum across the solution range

94 odd q values in [100, 287].  36 are prime, 58 composite.

Sub-harmonic score S_sub (weighted divisor count, excluding
trivial divisors 1 and q):
- Primes: S_sub = 0 for all (by definition)
- Composites: S_sub ranges from 0.006 (q = 169 = 13²) to
  0.179 (q = 105 = 3 × 5 × 7), mean 0.083

The highest sub-harmonic scores cluster around multiples of
3 × 5 (q = 105, 135, 165, 195, ...) which have 8 divisors.

Primes within ±10 of 137: {127, 131, 137, 139}.


---

## Track 2: Geodesic Coulomb self-energy

### F3. Method

For each q, charge e is distributed along the (p, q) torus
knot with p = (q−1)/2, placed on a 3D torus of unit major
radius (R = 1, a = r).  The Coulomb self-energy is computed
by direct pairwise summation of N = q × (pts_per_orbit)
point charges.

The geodesic shape factor G(r, q) is defined by:

    U_geodesic = G × e² / (4πε₀ R)

The uniform-surface-charge shape factor g(r) gives:

    U_uniform = g × e² / (4πε₀ R) = m_e c²/2  (by R8 construction)

The excess is G/g − 1: how much MORE energy the geodesic
distribution has compared to the uniform case.


### F4. ~~Minimum near q ≈ 137~~ — RETRACTED (resolution artifact)

The original Track 2 result (20 pts/orbit) showed a minimum
excess near q ≈ 137–139.  **Track 2c proved this was a
numerical artifact of insufficient resolution.**

Convergence study (excess % at q = 137):

| Resolution   | q=113  | q=125  | q=137  | q=139  | q=149  |
|--------------|--------|--------|--------|--------|--------|
| 20 pts/orbit | +16.9% | +13.5% | +12.6% | +12.5% | +13.2% |
| 40 pts/orbit |  +7.3% |  +7.0% |  +7.8% |  +8.0% |  +9.5% |
| 80 pts/orbit |  +4.0% |  +4.8% |  +6.3% |  +6.6% |  +8.5% |
| 120 pts/orbit|  +3.3% |  +4.4% |  +6.1% |  +6.4% |  +8.4% |
| extrap (h→0) |  +1.9% |  +3.6% |  +5.6% |  +5.9% |  +8.1% |

The minimum-excess q shifts with resolution:

| Resolution   | Minimum at |
|--------------|------------|
| 20 pts/orbit | q = 139    |
| 40 pts/orbit | q = 125    |
| 80 pts/orbit | q = 113    |
| 120 pts/orbit| q = 113    |
| Extrapolated | q ≤ 113    |

**At every resolution ≥ 40 pts/orbit, excess is monotonically
increasing from the lowest q sampled.**  There is no local
minimum in the physically interesting range.

The convergence rate (ratio of successive corrections) is
~0.30–0.35, consistent with 1/N convergence from the
Coulomb singularity.  Lower q converges slower because the
path is tighter and the nearest-neighbor regularization
contributes a larger fraction of the total energy.

**Conclusion:** the pairwise Coulomb sum on a discretized
geodesic has a systematic bias that depends on q through
the local point density.  This bias created an artificial
minimum at 20 pts/orbit that vanishes at higher resolution.
The naive geodesic Coulomb energy does NOT select q ≈ 137.


### F5. Physical interpretation (revised)

The geodesic charge distribution is always more concentrated
than uniform surface charge (G > g for all q), because the
charge sits on a 1D curve rather than a 2D surface.  The
excess energy measures how efficiently the winding pattern
distributes charge.

At higher resolution, the excess is monotonically increasing
with q across the sampled range (q = 113–161).  This means
lower q always has lower excess — the sparse winding pattern
on a thin torus is energetically cheaper than dense winding on
a fat torus, for this 1D-vs-2D comparison.

The original interpretation (optimal balance of coverage and
curvature at q ≈ 137) was an artifact of resolution-dependent
bias at 20 pts/orbit.

Note: the physical significance of this ratio (1D geodesic vs
2D uniform) is itself uncertain.  The real electron's charge
is presumably associated with the field, not concentrated on
the photon's classical path.  A more physical observable may
be needed.


### F6. What selects q?  (open question)

With the Coulomb minimum retracted, no computation in this
study selects q ≈ 137.  The electron properties (mass, charge,
spin, g-factor) are all satisfied for any q in the solution
family.

| Property           | q = 137        | q = 139        |
|--------------------|----------------|----------------|
| R / r_e            | 0.989          | 0.973          |
| r = a/R            | 0.308          | 0.323          |
| Orbits to close    | 137            | 139            |
| Shear δ/L_θ        | 1/274          | 1/278          |
| Mass               | exact (= m_e)  | exact (= m_e)  |
| Charge             | exact (= e)    | exact (= e)    |
| Spin               | exact ½        | exact ½         |

Candidate selection mechanisms (none yet confirmed):

1. **Magnetic self-energy.**  The current geometry differs
   between q values.  The Biot-Savart energy has NOT been
   computed and does not suffer from the same 1D-vs-2D
   comparison issue.  This remains a viable discriminant.

2. **Wave propagation / phase coherence.**  A scalar or EM
   wave on the sheared T² would test whether self-consistency
   (constructive interference after q orbits) selects a
   specific q.  Most complete but hardest to implement.

3. **R/r_e proximity.**  At q = 137, R = 0.989 r_e.  This
   near-coincidence might reflect deeper physics, but we lack
   a principle that demands R = r_e.

4. **Per-orbit cost.**  Fewer orbits = lower dynamical cost.
   Favors lower q, not specifically 137.  Would need to be
   balanced against some increasing cost to create a minimum.


### F7. Prime/composite distinction in Coulomb energy

The prime/composite distinction is NOT visible in the Coulomb
self-energy.  At the same q, primes and composites have
nearly identical excess (confirmed across all resolutions).
The charge distribution depends on the torus geometry (R, a)
and the total number of windings, not on q's factorization.

If primality matters, it must enter through a mechanism beyond
static Coulomb energy — likely involving the wave dynamics
(mode coupling, radiation, or phase coherence).


### F8. Methodological lesson: Coulomb sums on 1D curves

The Track 2 → 2c progression revealed that pairwise Coulomb
sums on discretized curves converge as ~1/N, much slower than
the 1/N² expected for smooth 2D charge distributions.  This
is because the 1D Coulomb self-energy has a logarithmic
divergence: the sum over nearest-neighbor pairs grows as
ln(N), and only the DIFFERENCE between the geodesic and
reference distributions converges.  But even this difference
converges slowly when the two distributions have different
dimensionality (1D curve vs 2D surface).

Any future energy comparison between geodesic and uniform
distributions should either:
- Use analytic regularization (subtract the known ln(N) divergence)
- Compare distributions of the same dimensionality
- Use spectral / Ewald methods adapted for the torus topology


---

## Summary of findings

| Finding | Result |
|---------|--------|
| Sub-periodic closure | Impossible on sheared T² for any q |
| Geodesic Coulomb excess | ~~Minimum at q ≈ 137~~ — **retracted** (resolution artifact) |
| Geodesic Coulomb (converged) | Monotonically increasing with q; does NOT select q ≈ 137 |
| Prime vs composite (Coulomb) | No distinction |
| Prime vs composite (path topology) | No distinction |

**The big result from Track 2c:** the apparent Coulomb minimum
at q ≈ 137 from Track 2 was a numerical artifact.  Higher
resolution (up to 120 pts/orbit + extrapolation) shows the
excess is monotonically increasing with q.  The pairwise
Coulomb sum does NOT select q ≈ 137.

**What remains viable:** magnetic self-energy, wave propagation
/ phase coherence, and R/r_e proximity are still untested
selection mechanisms.  The Coulomb result tells us that
*static electric* energy is not the selector — we need either
the magnetic term or dynamical (wave) physics.


## Next steps

1. **Track 3: Magnetic self-energy** — compute the
   Biot-Savart magnetic self-energy of the geodesic current.
   Unlike Coulomb energy, this compares a 1D current to a 1D
   current (no 1D-vs-2D mismatch), so it may converge better.
   The current geometry differs between q values, making it a
   genuine candidate discriminant.

2. **Track 4: Multipole decomposition** — decompose the
   geodesic charge distribution into azimuthal harmonics.
   Even if total energy doesn't distinguish prime from
   composite, the spatial structure might.

3. **Track 5: Wave propagation / phase coherence** — the
   most complete test.  Propagate a scalar wave along the
   geodesic and compute the accumulated phase error and
   self-consistency.  This is where a "per-orbit cost" would
   emerge from first principles rather than being assumed.

4. **Track 6: Continuous δ sweep** — for q = 137, sweep δ
   continuously and check whether the energy minimum matches
   the spin-½ value.


## Scripts

- [`scripts/track1_divisor_spectrum.py`](scripts/track1_divisor_spectrum.py)
  — Track 1: number theory + geodesic closure analysis
- [`scripts/track2_geodesic_energy.py`](scripts/track2_geodesic_energy.py)
  — Track 2: geodesic Coulomb self-energy scan (20 pts/orbit)
- [`scripts/track2c_hires.py`](scripts/track2c_hires.py)
  — Track 2c: high-resolution scan (40 pts/orbit + 60-pt convergence check)
- [`scripts/track2c_convergence.py`](scripts/track2c_convergence.py)
  — Track 2c: convergence study (20/40/80/120 pts/orbit + extrapolation)
