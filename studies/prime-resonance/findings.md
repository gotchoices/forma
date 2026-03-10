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


---

## Track 7: Wave superposition / sub-harmonic test

### F9. Method

For each q, the photon's q orbits each contribute a wave at
the observation point.  Orbit k arrives at minor angle
θ_k = 2πpk/q with Compton phase exp(2πik/q).  The observed
signal is:

    a_k = K(θ_k) / (1 + r cos θ_k) × exp(2πik/q)

where K is a Gaussian proximity kernel and the 1/(1+r cos θ)
factor captures flux conservation on the torus.

The DFT of {a_k} gives the power spectrum.  Frequency n = 1
is the fundamental Compton mode.  For composite q = d×m,
frequency n = q/d is the sub-harmonic at period d.


### F10. No prime/composite distinction in LINEAR wave superposition

The linear superposition test shows no spectral distinction
between prime and composite q.  Fair comparison at the SAME
frequencies (n = 3, 5, 9, 15, 27, 45) for all q:

| q   | P? | n=3 power | n=5 power | n=9 power | sum      |
|-----|----|-----------|-----------|-----------|----------|
| 133 |    | 0.44991%  | ~0        | ~0        | 0.44991% |
| 135 |    | 0.44839%  | ~0        | ~0        | 0.44839% |
| 137 | ★  | 0.44688%  | ~0        | ~0        | 0.44688% |
| 139 | ★  | 0.44539%  | ~0        | ~0        | 0.44539% |

Power at n = 3 varies smoothly with q, showing zero dependence
on whether 3 divides q.  Robust across all kernel widths.


### F11. Mathematical explanation (linear case)

Since gcd(p, q) = 1 for ALL q, the orbit positions always
form a complete residue system mod q.  The power spectrum is:

    |A(n)|² = q² |ĉ(np⁻¹ mod q)|²

— a permutation of the kernel's Fourier coefficients.  Power
at any frequency depends on which kernel coefficient gets
mapped to it, not on whether n divides q.


### F12. Limitations of Track 7 — why the test may be too weak

Track 7 proved that **linear, static** observables are blind
to primality.  But the Q30 hypothesis is about **dynamical
energy transfer**, which Track 7 did not test:

1. **Linear vs nonlinear.**  In a linear system, modes never
   exchange energy — they are independent by definition.  The
   Q30 hypothesis requires nonlinear mode coupling (or
   parametric resonance), which is a fundamentally different
   regime.  Track 7's DFT is purely linear.

2. **Snapshot vs evolution.**  Track 7 analyzed an imposed
   wave at one instant.  Energy leakage is a process that
   unfolds over time — the growth rate of parasitic modes
   depends on coupling coefficients, not static spectra.

3. **Imposed vs self-consistent.**  The wave was prescribed
   externally, not a self-sustaining resonance.  A real
   electron's field must reinforce itself after q orbits.
   Self-consistency could have different stability properties
   for prime vs composite q.

4. **Smooth kernel hid structure.**  The Gaussian kernel has
   Fourier coefficients ~exp(−σ²m²/2), which are negligible
   at m ~ q/d (the divisor frequencies).  A realistic EM field
   falls off as ~1/r, giving coefficients ~1/|m| — much larger
   at high harmonics.

**Track 7 proved:** any observable depending only on the SET
of orbit positions (not their temporal ordering or dynamics)
is blind to primality.

**Track 7 did NOT test:** whether the temporal ordering of
orbits creates resonant mode coupling at divisor frequencies
in a dynamical system.  For composite q = d×m, the sequence
of orbit positions has periodic sub-structure at interval m
(every m orbits, the angular position is related by d-fold
symmetry).  In a nonlinear system, this periodic driving can
parametrically excite the d-th harmonic.  For prime q, no
such periodic sub-structure exists.

**The primality hypothesis remains viable** — but requires a
dynamical test (Track 8).


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
| Geodesic Coulomb (converged) | Monotonically increasing with q; lower q = cheaper |
| Wave superposition (linear) | No prime/composite distinction |
| Track 7 scope | Proved: linear/static tests blind to primality |
| Track 7 scope | Did NOT test: dynamical mode coupling |

**Track 2c:** Lower q = less excess Coulomb energy.  This is
a real physical result: fewer orbits is energetically cheaper.

**Track 7:** The linear superposition test found no spectral
distinction.  However, the test has significant limitations
(F12): it only probes linear, static observables.  The Q30
primality hypothesis is about dynamical energy transfer
(parametric mode coupling), which Track 7 did not address.
**The hypothesis remains viable.**

**What we know:**
- Lower q is cheaper (Coulomb) — pushes toward low q
- Some geometric floor must exist (path must fit λ_C)
- Linear/static observables are blind to primality (proven)
- Dynamical mode coupling is untested

**The selection picture (working hypothesis):**
1. Geometric floor → minimum viable q
2. Coulomb cost → pushes q to the floor
3. Mode stability (if confirmed) → prime q more stable
4. Convergence → lowest prime above the floor = 137 ?


## Next steps

1. **Track 8: Mode spectrum and degeneracy on the sheared T²**
   The sheared T² is flat, so the scalar Helmholtz equation
   is analytically solvable.  The mode frequencies are:

       ω(n,m) = c√(n²/a² + (m − n/(2q))²/R²)

   For each q, compute:
   (a) the mode spectrum (all eigenfrequencies up to a cutoff)
   (b) the number of modes near-degenerate with the Compton
       fundamental (within Δω/ω < ε)
   (c) whether the degeneracy count differs for prime vs
       composite q

   **Why this matters:** Near-degenerate modes are the channels
   through which the fundamental can lose energy (through any
   coupling mechanism, however weak).  More channels = less
   stable resonance = more expensive.  If composite q has more
   near-degenerate modes, prime q is demonstrably cheaper.

   This is the key intermediate step between Track 7 (linear,
   no dynamics) and a full dynamical simulation.  It answers:
   "even granting that coupling exists, does q's factorization
   affect how many modes the fundamental can leak to?"

   *Sub-step 8a (conceptual):* Prove that energy in non-Compton
   modes is parasitic.  Argument: the electron IS the Compton
   resonance (mass = hν_C/c²).  Energy in a different mode
   doesn't contribute to the mass at ν_C, so the system needs
   more total energy to maintain m_e.  Therefore: more leakage
   channels = higher cost.

2. **Track 3: Magnetic self-energy** — compute the
   Biot-Savart magnetic self-energy of the geodesic current.
   Unlike Coulomb energy, this compares a 1D current to a 1D
   current (no 1D-vs-2D mismatch), so it may converge better.

3. **Track 6: Continuous δ sweep** — for selected q, sweep δ
   continuously and check whether a phase-coherence optimum
   coincides with the spin-½ value δ = L_θ/(2q).

4. **Geometric floor analysis** — determine the minimum q
   allowed by the R8 constraints and whether q = 137 is
   special in that context (e.g., lowest prime where R ≈ r_e).


## Scripts

- [`scripts/track1_divisor_spectrum.py`](scripts/track1_divisor_spectrum.py)
  — Track 1: number theory + geodesic closure analysis
- [`scripts/track2_geodesic_energy.py`](scripts/track2_geodesic_energy.py)
  — Track 2: geodesic Coulomb self-energy scan (20 pts/orbit)
- [`scripts/track2c_hires.py`](scripts/track2c_hires.py)
  — Track 2c: high-resolution scan (40 pts/orbit + 60-pt convergence check)
- [`scripts/track2c_convergence.py`](scripts/track2c_convergence.py)
  — Track 2c: convergence study (20/40/80/120 pts/orbit + extrapolation)
- [`scripts/track7_wave_superposition.py`](scripts/track7_wave_superposition.py)
  — Track 7: wave superposition / sub-harmonic test (Q30 hypothesis)
