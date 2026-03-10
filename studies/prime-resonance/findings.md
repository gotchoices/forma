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
by direct pairwise summation of N = 20q point charges.

The geodesic shape factor G(r, q) is defined by:

    U_geodesic = G × e² / (4πε₀ R)

The uniform-surface-charge shape factor g(r) gives:

    U_uniform = g × e² / (4πε₀ R) = m_e c²/2  (by R8 construction)

The excess is G/g − 1: how much MORE energy the geodesic
distribution has compared to the uniform case.


### F4. The excess energy has a minimum near q ≈ 137

| q   | P? | r     | g_unif | G_geod | G/g   | excess |
|-----|----|-------|--------|--------|-------|--------|
| 101 | ★  | 0.105 | 0.677  | 0.838  | 1.237 | +23.7% |
| 113 | ★  | 0.160 | 0.604  | 0.707  | 1.169 | +16.9% |
| 127 | ★  | 0.241 | 0.536  | 0.607  | 1.133 | +13.3% |
| 131 | ★  | 0.267 | 0.518  | 0.585  | 1.128 | +12.8% |
| 133 |    | 0.281 | 0.510  | 0.575  | 1.126 | +12.6% |
| 135 |    | 0.294 | 0.502  | 0.566  | 1.126 | +12.6% |
| **137** | **★** | **0.308** | **0.494** | **0.556** | **1.126** | **+12.6%** |
| **139** | **★** | **0.323** | **0.487** | **0.547** | **1.125** | **+12.5%** |
| 141 |    | 0.337 | 0.479  | 0.539  | 1.126 | +12.6% |
| 145 |    | 0.367 | 0.465  | 0.524  | 1.128 | +12.8% |
| 151 | ★  | 0.413 | 0.444  | 0.504  | 1.133 | +13.3% |
| 163 | ★  | 0.509 | 0.407  | 0.471  | 1.155 | +15.5% |
| 181 | ★  | 0.667 | 0.359  | 0.435  | 1.211 | +21.1% |
| 211 | ★  | 0.936 | 0.294  | 0.416  | 1.416 | +41.6% |
| 251 | ★  | 1.562 | 0.215  | 0.307  | 1.429 | +42.9% |

**The excess Coulomb energy is minimized in the range
q ≈ 135–141, with the lowest value at q = 139 (+12.50%)
and q = 137 just above (+12.56%).**

The energy rises steeply for both lower q (sparse winding,
concentrated charge) and higher q (fat torus, high aspect
ratio).  The minimum is broad — the ~0.1% difference between
q = 137 and q = 139 is within numerical uncertainty at 20
points per orbit.

The Coulomb energy alone selects the NEIGHBORHOOD of q ≈ 137
but does not pin the exact value.  Discriminating 137 from
139 (or 135, 141) requires additional physics.


### F5. Physical interpretation

The geodesic charge distribution is always more concentrated
than uniform surface charge (G > g for all q), because the
charge sits on a 1D curve rather than a 2D surface.  The
excess energy measures how efficiently the winding pattern
distributes charge.

At low q (thin torus, sparse path): few windings leave large
gaps in surface coverage → high excess.

At high q (fat torus, dense path): the torus aspect ratio r
grows with q, and the charge becomes concentrated near the
inner edge of the torus where the path's curvature radius is
smallest → high excess.

The minimum at q ≈ 137 represents the optimal balance: enough
windings to cover the surface reasonably well, on a torus thin
enough that the path curvature doesn't concentrate charge.

This is R ≈ r_e (the classical electron radius), the same
coincidence noted in R8.


### F6. The 137/139 discrimination problem

All four electron properties (mass, charge, spin, g-factor)
are equally satisfied at q = 137 and q = 139.  Neither is
"more electron-like."  The Coulomb excess is nearly identical.
So what could discriminate them?

| Property           | q = 137        | q = 139        |
|--------------------|----------------|----------------|
| R / r_e            | 0.989          | 0.973          |
| r = a/R            | 0.308          | 0.323          |
| Orbits to close    | 137            | 139            |
| Shear δ/L_θ        | 1/274          | 1/278          |
| Mass               | exact (= m_e)  | exact (= m_e)  |
| Charge             | exact (= e)    | exact (= e)    |
| Spin               | exact ½        | exact ½         |
| Coulomb excess     | +12.56%        | +12.50%        |

Candidate discriminants (none yet confirmed):

1. **R/r_e proximity.**  At q = 137, R = 0.989 r_e — nearly
   exact.  At q = 139, R = 0.973 r_e — 2.7% off.  r_e is the
   distance where Coulomb potential energy equals the rest
   energy; being AT r_e might have physical significance, but
   we lack a principle that demands R = r_e exactly.

2. **Per-orbit cost.**  The photon must maintain phase
   coherence over q orbits.  Fewer orbits = fewer coherence
   constraints = lower dynamical cost.  137 < 139.  But no
   known law directly penalizes winding number, and the cost
   per orbit has not been quantified.

3. **Magnetic self-energy.**  The current geometry differs
   between the two tori (different R, a).  The magnetic
   contribution to total energy has not been computed and
   could break the degeneracy.

4. **Wave propagation.**  A proper EM wave calculation on the
   sheared T² would capture both phase coherence and field
   self-consistency.  This is the most complete test but also
   the most difficult.


### F7. Prime/composite distinction in Coulomb energy

The prime/composite distinction is NOT visible in the Coulomb
self-energy.  At the same q, primes and composites have
nearly identical excess:

    Primes (17 values):    mean excess = +22.3%
    Composites (15 values): mean excess = +22.4%

The charge distribution depends on the torus geometry (R, a)
and the total number of windings, not on q's factorization.
Equally-spaced passes along the geodesic produce the same
charge pattern regardless of whether q has divisors.

If primality matters, it must enter through a mechanism beyond
static Coulomb energy — likely involving the wave dynamics
(mode coupling, radiation, or phase coherence).


---

## Summary of findings

| Finding | Result |
|---------|--------|
| Sub-periodic closure | Impossible on sheared T² for any q |
| Geodesic Coulomb excess | Minimum at q ≈ 135–141 |
| 137 vs 139 | Degenerate in Coulomb; 4 candidate discriminants identified |
| Prime vs composite (Coulomb) | No distinction |
| Prime vs composite (path topology) | No distinction |

**The big result:** the geodesic Coulomb self-energy selects
the neighborhood q ≈ 135–141 as the minimum-energy winding
number.  This is the first computation that picks a specific
range from the R8 solution family, confirming the "least
expensive path" hypothesis at the Coulomb level.

**What it doesn't explain:** why 137 specifically (vs 139 or
135 — all within the flat minimum), whether primality plays
any role, and what additional physics pins the exact q.


## Next steps

1. **Track 2c: Higher resolution** — rerun the Coulomb scan
   with 40–80 points per orbit, dense sampling near the
   minimum (every odd q from 129–149).  Determine whether
   the minimum genuinely favors 139 over 137 or whether the
   current 0.06% difference is numerical noise.

2. **Track 3: Magnetic self-energy** — compute the
   Biot-Savart magnetic self-energy of the geodesic current.
   This is the second physical energy term; the current
   geometry differs between q = 137 and 139, so it may break
   the Coulomb degeneracy.  Combined E_Coulomb + E_magnetic
   gives the total static field energy.

3. **Track 4: Multipole decomposition** — decompose the
   geodesic charge distribution into azimuthal harmonics.
   Even if total energy doesn't distinguish prime from
   composite, the spatial structure might.

4. **Track 5: Wave propagation / phase coherence** — the
   most complete test.  Propagate a scalar wave along the
   geodesic and compute the accumulated phase error and
   self-consistency.  This is where a "per-orbit cost" would
   emerge from first principles rather than being assumed.

5. **Track 6: Continuous δ sweep** — for q = 137, sweep δ
   continuously and check whether the energy minimum matches
   the spin-½ value.


## Scripts

- [`scripts/track1_divisor_spectrum.py`](scripts/track1_divisor_spectrum.py)
  — Track 1: number theory + geodesic closure analysis
- [`scripts/track2_geodesic_energy.py`](scripts/track2_geodesic_energy.py)
  — Track 2: geodesic Coulomb self-energy scan
