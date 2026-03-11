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
dynamical test.


---

## Track 8: Mode spectrum and degeneracy on the sheared T²

### F13. Mode spectrum is analytically exact

The sheared T² is flat, so the scalar Helmholtz equation has
exact plane-wave solutions.  Mode frequencies:

    ω(n,m) = √(n²/r² + (m − n/(2q))²)    [units: c/R]

Every mode has an exact time-reversal partner: ω(n,m) = ω(−n,−m).
This gives min_gap = 0 for ALL q (trivial double degeneracy).


### F14. No prime/composite distinction in mode spectrum

Four analyses were performed:

**(a) Basic statistics:** Mode count, mean gap, and std gap
vary smoothly with q (through r = a/R).  No prime/composite
signal.

**(b) Near-degeneracy pairs:** At ε = 0.001, the pair count
tracks N_modes/2 (dominated by trivial time-reversal pairs).
At ε = 0.01, q = 137 has MORE close pairs (336) than q = 135
(239) — the OPPOSITE of Q30's prediction.

**(c) Beat frequency test (strongest test):** For composite
q = 135 (divisors {3,5,9,15,27,45}), the count of mode pairs
at divisor beat frequencies shows NO enhancement:

| d  | divisor? | Δω     | pairs (q=135) | pairs (q=137) |
|----|----------|--------|---------------|---------------|
| 3  | ÷ 135   | 0.0222 | 20            | 12            |
| 5  | ÷ 135   | 0.0370 | 16            | 24            |
| 7  | no      | 0.0519 | 32            | 12            |
| 9  | ÷ 135   | 0.0667 | 20            | 36            |

The pair count at divisor frequencies is NOT systematically
higher than at non-divisor frequencies.  For q=141 (divisors
{3,47}), the divisor d=3 gives 36 pairs while non-divisor
d=7 gives 52.  The counts are determined by the lattice
geometry (aspect ratio r), not by q's factorization.

**(d) Direct comparison q=135 vs q=137:** Mode counts are
nearly identical (534 vs 540).  Non-trivial near-degeneracies
are indistinguishable.


### F15. Why the mode spectrum is blind to primality

The mode frequencies ω(n,m) depend on q only through the
shear term −n/(2q).  Since 1/(2q) varies smoothly and
monotonically with q, the spectrum shifts continuously.  The
integer factorization of q does not enter the frequency
formula — only the VALUE of q matters.

This is the same root cause as Track 7: on the flat sheared
T², the wave equation is linear, and its solutions depend on
q as a continuous parameter.  The distinction between q = 135
and q = 137 is a smooth shift of 1/(270) vs 1/(274) in the
shear, not a structural change.


### F16. Revised scope of the primality hypothesis

Five tests have now failed to find prime/composite distinction:

| Track | Test                    | Domain        | Result |
|-------|-------------------------|---------------|--------|
| 1     | Path topology           | geometry      | None   |
| 2     | Coulomb energy          | static energy | None   |
| 7     | Wave superposition      | linear waves  | None   |
| 8a    | Mode degeneracy         | linear modes  | None   |
| 8c    | Beat frequency pairs    | linear modes  | None   |

All five are LINEAR analyses on the flat (or nearly flat) T².

**For primality to matter, ALL of the following must hold:**
1. The coupling mechanism must be NONLINEAR (mode-mode
   interaction, not just mode existence)
2. The nonlinearity must be sensitive to the INTEGER
   factorization of q, not just its numerical value
3. The effect must survive on the actual CURVED torus
   (not just the flat approximation)

The most promising remaining mechanism is the CURVED torus
metric: the factor (1 + r cos θ) creates an effective
potential that modulates the wave equation.  This modulation
has period 2π in θ and couples modes differing by Δn = ±1.
Through chains of such couplings, energy can flow between
modes.  Whether the RATE of this flow depends on q's
factorization is an open question that requires solving the
coupled nonlinear system.

Alternatively, primality may not matter in this model.  The
selection of q = 137 might come entirely from the geometric
floor (minimum viable q from the R8 constraints) combined
with the Coulomb cost (lower q is cheaper).


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
| Geodesic Coulomb (converged) | Lower q = cheaper (monotonic) |
| Wave superposition (linear) | No prime/composite distinction |
| Mode spectrum (linear) | No prime/composite distinction |
| Beat frequency pairs | No enhancement at divisor frequencies |
| **All linear tests** | **Blind to primality** |

**The one solid positive result:** lower q costs less energy
(Track 2c).  This pushes the system toward the lowest viable q.

**Primality:** Five linear tests found no prime/composite
distinction (Tracks 1, 2, 7, 8a, 8c).  The root cause is
that q enters the flat-T² wave equation as a continuous
parameter (through the shear 1/(2q)), not through its integer
factorization.  **For primality to matter, the mechanism must
be nonlinear AND sensitive to integer factorization** (F16).

**The selection picture (updated):**
1. Geometric floor → minimum viable q (untested — key open question)
2. Coulomb cost → pushes q to that floor
3. Primality → requires nonlinear dynamics on the CURVED
   torus (not yet tested; may not apply)

The most important open question is now **the geometric floor**:
what sets the minimum q?  If the floor lands at or near 137,
we don't need primality at all.


## The tautology question

### F17. q ~ 1/α is forced by inputs, not predicted

The R8 model takes two measured inputs: m_e (electron mass)
and e (electron charge).  From these:

- The charge constraint (U = m_e c²/2) forces R ~ r_e
- The mass constraint (path = λ_C) then forces
  q ~ λ̄_C / r_e = 1/α ≈ 137

Since α = e²/(4πε₀ ℏc) is just a dimensionless repackaging
of the input e, the value q ~ 137 was **baked into the
inputs**.  The model gives this a geometric interpretation
(winding number), but the numerical value follows from
dimensional analysis once you assume "mass comes from EM
energy" and "path = Compton wavelength."

**What IS non-tautological:**

1. A self-consistent solution exists at all — mass, charge,
   and spin can be simultaneously satisfied on a torus with
   a physically reasonable geometry (r ~ 0.1–1, R ~ r_e).

2. Multi-winding is required.  q = 1 fails: a single-winding
   torus at the Compton scale has Coulomb energy ~ α × m_e c²,
   which is ~137× too small.  The photon MUST wind ~137 times.

3. Spin-½ emerges exactly from the 1:2 winding ratio on the
   sheared T², independent of q.

4. The geometry is physically reasonable — not Planck-scale
   or absurd.

**What IS tautological:**

- The specific value q ~ 137.  It is 1/α wearing a geometric
  hat.  Breaking this circularity requires deriving the shear
  from something other than the charge constraint — e.g., a
  self-consistency condition on the wave equation where e is
  NOT an input.  Then α = 1/(2gq) would be a genuine
  prediction.


### F18. The real free parameter is r (aspect ratio), not q

q and r are related by the R8 solution curve:

    q(r) = 1 / (2α × g(r) × √(1 + r²/4))

Since α is an input, q is DETERMINED by r.  The only genuine
freedom is the aspect ratio r ∈ (~0.05, ~5).  The range
q ~ 100–287 merely reflects g(r)√(1+r²/4) varying by ~3×
across that interval.

**The question "what selects q = 137" is really "what selects
r ≈ 0.31."**  This is a question about the compact geometry's
shape, not a number-theory question about 137.


---

## Study conclusions

R11 explored whether the winding number q could be selected
by energy cost, resonance quality, or number-theoretic
properties (primality).  After eight tracks of investigation:

**Negative results:**
- Coulomb self-energy does not select q ≈ 137 (Track 2c:
  monotonically increasing — lower q is always cheaper)
- No prime/composite distinction in any linear analysis
  (Tracks 1, 7, 8a, 8c — five independent tests)
- q ~ 1/α is partly tautological given the measured inputs
  e and m_e

**Positive results:**
- Lower q = lower excess energy (Track 2c) — a real physical
  tendency toward the minimum viable q
- The model's qualitative content is genuinely non-trivial:
  multi-winding is required, spin emerges from topology,
  the geometry is at the r_e scale

**Strategic insight:**
The real free parameter is not q but r (the aspect ratio).
Determining r requires a fundamentally different approach:
solving for self-consistent field configurations on the
sheared T², where the shear is constrained by the field
equations rather than put in by hand from the measured charge.
This is the subject of a new study (R12).

**Study status: COMPLETE.**


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
- [`scripts/track8_mode_spectrum.py`](scripts/track8_mode_spectrum.py)
  — Track 8: mode spectrum and degeneracy on the sheared T²
