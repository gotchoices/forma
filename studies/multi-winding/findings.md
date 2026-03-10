# R8. Multi-Winding Electron — Findings

## Track 1: Geometry sweep

### F1. Method

The Coulomb self-energy of a uniform surface charge Q on a
torus scales as:

    U = Q² × g(r) / (4πε₀ R)

where g(r) is a dimensionless shape factor depending only on
the aspect ratio r = a/R.  We computed g(r) by direct pairwise
Coulomb summation at unit scale (R = 1, a = r, Q = 1), then
derived the physical geometry analytically.

Setting U = m_e c²/2 with Q = e:

    R = 2 g(r) × r_e

where r_e = e²/(4πε₀ m_e c²) ≈ 2.82 × 10⁻¹⁵ m is the
classical electron radius.

The winding number follows from the path constraint ℓ = λ_C
for a (p, q) ≈ (q/2, q) knot:

    q(r) = 1 / (2α × g(r) × √(1 + r²/4))


### F2. The solution curve

Every integer q from ~100 to ~287 has a valid geometry.  The
solution is a continuous curve in (q, r) space:

| q | p | r = a/R | R (m) | R/r_e | a (m) |
|---|---|---------|-------|-------|-------|
| 100 | 49 | 0.10 | 3.86 × 10⁻¹⁵ | 1.37 | 3.88 × 10⁻¹⁶ |
| 120 | 59 | 0.20 | 3.19 × 10⁻¹⁵ | 1.13 | 6.38 × 10⁻¹⁶ |
| 137 | 68 | 0.31 | 2.79 × 10⁻¹⁵ | 0.99 | 8.60 × 10⁻¹⁶ |
| 139 | 70 | 0.32 | 2.75 × 10⁻¹⁵ | 0.98 | 8.90 × 10⁻¹⁶ |
| 150 | 73 | 0.41 | 2.54 × 10⁻¹⁵ | 0.90 | 1.04 × 10⁻¹⁵ |
| 200 | 99 | 0.83 | 1.79 × 10⁻¹⁵ | 0.64 | 1.49 × 10⁻¹⁵ |
| 250 | 123 | 1.52 | 1.23 × 10⁻¹⁵ | 0.44 | 1.87 × 10⁻¹⁵ |

Key observations:

- **The torus is thin** (r ≈ 0.3 for q ≈ 137, meaning a ≪ R).
  This contrasts sharply with S2/R6 which predicted fat tori
  (r ≈ 4–7).  Those were artifacts of the energy-balance error
  exposed in R7.

- **R ≈ r_e for q ≈ 137.**  The classical electron radius is
  the natural scale.  At q = 137, R/r_e = 0.990 — within 1%.

- **Every integer q works.**  Nothing selects a specific q from
  the charge and mass constraints alone.  The winding number is
  a free parameter at this stage, to be fixed by the precession
  mechanism.


### F3. The q = 137 solution

The point q = 137 is noteworthy: R is almost exactly r_e.

| Property | Value |
|----------|-------|
| q (major windings) | 137 |
| p (minor windings) | 68 |
| Torus knot | (68, 137), gcd = 1 |
| p/q ratio | 0.4964 (≈ 1/2) |
| R (major radius) | 2.79 × 10⁻¹⁵ m (0.990 r_e) |
| a (minor radius) | 8.60 × 10⁻¹⁶ m |
| r = a/R | 0.308 |
| Path length | λ_C = 2.43 × 10⁻¹² m |
| Coulomb energy | m_e c²/2 (by construction) |

Whether q = 137 is "the answer" or just one point on the
solution curve is an open question.  But it is the only point
where R coincides with a named physical constant (r_e).


---

## Track 2: Exact spin from sheared T²

### F4. The problem with standard torus knots

On a standard (rectangular) flat T², a (p, q) torus knot with
p/q = exactly 1/2 requires gcd(p, q) > 1.  For example,
(68, 136) has gcd = 68 — it is 68 separate (1,2) loops, not a
single path.  Only coprime pairs like (68, 137) give a single
connected path, but their physical ratio (0.4964) is not
exactly 1/2.

If spin ½ requires an exact 1:2 ratio, this is a problem.


### F5. The sheared T² resolves it

On a sheared T² — where the compact dimensions are slightly
tilted (non-orthogonal) — the situation is different.

The lattice is defined by two basis vectors:

    e₁ = (L_θ, 0)
    e₂ = (δ, L_φ)

where δ is the shear (offset in the θ direction per φ
circuit).  The space is still flat.

A geodesic in the exact (1,2) physical direction has slope
L_θ/(2L_φ) on the universal cover.  It closes at the lattice
point (n, m) where:

    n = m × (1/2 − δ/L_θ)

For δ/L_θ = 1/274 and m = 137:

    n = 137 × (1/2 − 1/274) = 137 × 136/274 = 68

So the lattice winding numbers are **(n, m) = (68, 137)**,
with gcd(68, 137) = 1.  This is a **single connected closed
geodesic**.

The physical displacement is:

    (nL_θ + mδ, mL_φ) = (68L_θ + L_θ/2, 137L_φ)
                       = (68.5 L_θ, 137 L_φ)

The physical winding ratio is 68.5/137 = **exactly 1/2**.

The "half-winding" (68.5 instead of 68 or 69) is absorbed by
the shear — the lattice identification takes care of the
fractional part.


### F6. Spin is exactly ½

At every point on the path, the photon spirals with exact 1:2
ratio: one minor-circle traversal per two major-circle orbits.
This is the same local geometry that produces spin ½ in the
standard WvM (1,2) model.

Since the spin-½ character comes from the local helical
winding (the Berry phase from the 1:2 helix), and the winding
ratio is exactly 1:2 everywhere, **spin ½ is exact** — not
approximate.

The sheared T² eliminates the tension between:
- exact 1:2 ratio (needed for spin)
- coprime winding numbers (needed for a single path)
- large winding count (needed for small torus)


### F7. Nearby solutions also work

The same construction works for any odd q (where (q−1)/2 and q
are automatically coprime):

| q | n | gcd | δ/L_θ | R/r_e |
|---|---|-----|-------|-------|
| 135 | 67 | 1 | 1/270 | 1.01 |
| 137 | 68 | 1 | 1/274 | 0.99 |
| 139 | 69 | 1 | 1/278 | 0.98 |
| 141 | 70 | 1 | 1/282 | 0.96 |

All are within ~2% of r_e and all have exact 1:2 physical
winding ratio.  The shear δ/L_θ = 1/(2q) is tiny — the compact
dimensions are barely tilted.


---

## Track 3: Magnetic moment and g-factor

### F8. The classical current-loop approach fails

Modeling the photon as a charge e circulating at speed c along
the path gives a classical magnetic moment:

    μ_classical = I × (effective enclosed area)
                = (ec/ℓ) × q × πR²

For the standard WvM (1,2) model (q = 2, R = λ_C/(4π)):

    μ = μ_B/2    →    g = 1

For multi-winding (q = 137, R ≈ r_e):

    μ ≈ α × μ_B    →    g ≈ 2α ≈ 0.015

Both are wrong.  The classical approach gives g = 1 for WvM
(known to be off by a factor of 2) and g ≈ 2α for
multi-winding (off by a factor of ~137).  A direct B-field
integral (Biot-Savart) would reproduce these classical results
and also be wrong.

The failure is fundamental: the g-factor is a quantum property
of spin-½ particles that cannot be derived from classical
electrostatics or magnetostatics.


### F9. The g = 2 argument (geometry-independent)

The correct magnetic moment comes from the quantum relationship
between spin angular momentum and the gyromagnetic ratio.

**Step 1: Spin.**  The electron spin is S = ℏ/2.  This is
established in Track 2 — the exact 1:2 winding ratio on the
sheared T² gives spin ½ regardless of q.

**Step 2: g-factor.**  For a spin-½ particle, the Dirac
equation gives g = 2.  In the WvM framework, this has a
physical interpretation: the photon is a spin-1 boson carrying
angular momentum ℏ.  The electron spin is ℏ/2 (from the 1:2
topology).  The ratio:

    g = L_photon / S_electron = ℏ / (ℏ/2) = 2

The factor of 2 reflects the fact that a photon's spin
produces twice as much magnetic moment per unit angular
momentum compared to orbital motion.  This is independent
of the torus geometry — it depends only on the photon being
spin-1 and the electron being spin-½.

**Step 3: Magnetic moment.**

    μ = g × (e/2m_e) × S = 2 × (e/2m_e) × ℏ/2 = eℏ/(2m_e) = μ_B

This is the Bohr magneton — the correct leading-order result.


### F10. Direction of the B field

The net magnetic moment points along the torus symmetry axis
(the spin axis).  This follows from the symmetry of the
winding:

- B is tangent to the compact surface, perpendicular to the
  photon's path direction (from k̂ × E).
- At each point on the (1,2)-like helix, B has an axial
  component (along the torus z-axis) and an azimuthal
  component (around the ring).
- The azimuthal components cancel by the rotational symmetry
  of the path: opposite sides of the torus contribute
  oppositely.
- The axial components all point the same direction (determined
  by the helicity) and accumulate.

This argument holds for both the standard (1,2) and the
multi-winding path — the local structure is the same.


### F11. The anomalous moment

The leading-order result is g = 2.  The measured value is
g ≈ 2.0023, with the correction:

    g − 2 ≈ α/π ≈ 0.00232

In QED, this comes from virtual photon loops.  In WvM's
framework, it is attributed to the fraction of field energy
in the non-co-rotating (external) component.  Whether this
fraction depends on the torus geometry (thin vs fat, Compton
vs r_e scale) is an open question — but since the local
winding structure is the same, the correction is expected
to carry over.


---

## Summary

| Property | Standard WvM | R8 multi-winding | Status |
|----------|-------------|------------------|--------|
| Mass m_e | Path = λ_C | Path = λ_C | ✓ same |
| Charge e | Coulomb energy too low | Coulomb energy = m_e c²/2 | ✓ fixed |
| Spin ½ | From (1,2) topology | From exact 1:2 on sheared T² | ✓ exact |
| μ = μ_B | From g = 2, S = ℏ/2 | From g = 2, S = ℏ/2 | ✓ same |
| g ≈ 2.0023 | α/π correction | Expected same | ○ open |
| Torus radius | ~10⁻¹³ m (Compton) | ~3 × 10⁻¹⁵ m (r_e) | — |
| Winding number | 2 | ~137 | — |
| Compact space | Flat T² (rectangular) | Flat T² (sheared) | — |

All four fundamental electron properties (mass, charge, spin,
magnetic moment) are reproduced by the multi-winding model.
The Coulomb energy shortfall from R7 is resolved by the smaller
torus (r_e scale), while spin and magnetic moment are preserved
by the exact 1:2 local winding ratio.

### What remains open

1. **What selects q?**  Every odd q from ~100 to ~287 has a
   valid geometry.  The mass and charge constraints don't pick
   a unique q — something else must.  The shear δ/L_θ is the
   free parameter.

2. **Why is the T² sheared?**  The shear is a property of the
   compact space itself.  What determines δ?  Options include:
   self-consistency (the photon's energy curves the space),
   a discrete symmetry, or simply an axiom.

3. **Anomalous g-factor.**  The leading g = 2 is
   geometry-independent (Track 3).  The correction g − 2 ≈ α/π
   may depend on the field geometry; verifying it carries over
   to the multi-winding case is a future investigation.

4. **Does q = 137 have special status?**  It gives R ≈ r_e,
   but so do nearby values (within a few percent).  The
   geodesic Coulomb energy does NOT select q ≈ 137 (R11
   Track 2c: retracted).  Remaining candidates: (a) 137 is
   prime — harmonic avoidance (Q30), (b) magnetic self-energy,
   (c) wave/phase coherence (Q29).  The discrepancy between
   1/137 and measured 1/137.036 may be accounted for by
   higher-order shape corrections (Track 5).


---

## Track 4: Shear analysis

### F12. δ in absolute terms is nearly constant

The absolute shear δ = L_θ/(2q) varies surprisingly little
across the solution curve.  While q spans 83–263 (a factor of
3), δ stays within a factor of 3 and is remarkably flat in the
physically interesting range:

| q | r | R (m) | δ (m) | δ/(αr_e) |
|---|---|-------|-------|----------|
| 83 | 0.05 | 4.65e-15 | 8.81e-18 | 0.43 |
| 100 | 0.10 | 3.88e-15 | 1.22e-17 | 0.59 |
| 120 | 0.20 | 3.21e-15 | 1.68e-17 | 0.82 |
| 135 | 0.30 | 2.83e-15 | 1.98e-17 | 0.96 |
| **137** | **0.32** | **2.78e-15** | **2.01e-17** | **0.98** |
| 142 | 0.35 | 2.68e-15 | 2.08e-17 | 1.01 |
| 161 | 0.50 | 2.33e-15 | 2.28e-17 | 1.11 |
| 216 | 1.00 | 1.60e-15 | 2.32e-17 | 1.13 |

Near q ≈ 137, the absolute shear is:

    δ ≈ 2.0 × 10⁻¹⁷ m ≈ α r_e = α² λ̄_C

This is the fine-structure constant squared times the reduced
Compton wavelength.  It is a known length scale: the product of
α and the classical electron radius.


### F13. δ ≈ αR at q ≈ 1/α (approximate, not exact)

At 32×64 resolution, the ratio δ/(αR) appeared to cross 1.0
precisely at q ≈ 137, r ≈ 1/π.  Track 5 tested this at higher
resolution, revealing it to be an artifact of insufficient grid
size.

At 32×64 resolution, g(1/π) = 0.4924 happened to be close to
the target π/√(4π²+1) = 0.4938 (0.3% gap).  But with finer
grids, g(1/π) converges to ≈ 0.503, not 0.494 — the gap
grows to ~2%, ruling out the exact identity.

However, the **q = 137 solution itself is robust**:

| Resolution | r at q=137 | g | R/r_e |
|------------|-----------|---|-------|
| 24×48 | 0.308 | 0.4946 | 0.989 |
| 64×128 | 0.328 | 0.4944 | 0.989 |
| 192×384 | 0.336 | 0.4942 | 0.988 |

As the grid refines, r shifts (from 0.31 to 0.34) but R/r_e
stays at 0.989.  This stability is not accidental: q = 1/α
requires g√(1+r²/4) = 1/2, so R = 2gr_e ≈ r_e regardless
of which r satisfies this.

At the converged q = 137 solution (r ≈ 0.34):

    δ/(αR) = 2πr g √(1+r²/4) ≈ 1.06

So δ is within ~6% of αR — close, but not exact.  The
qualitative observation that δ is of order αR still holds,
suggesting the shear may have an electromagnetic origin,
but there is no exact identity.


### F14. Timescales and phase per circuit

The transit time per major circuit is:

    T_circuit = ℓ_per_circuit / c = λ_C / (qc) = α × T_Compton

The shear fraction per minor circumference is:

    δ/L_θ = 1/(2q) ≈ α/2

The phase advance per major circuit is:

    Δφ = 2π L_φ/λ_C ≈ 2πα

So each circuit takes time α × T_Compton and advances the
photon's phase by 2πα radians.  Only α of a wavelength fits
around the major circle.


### F15. Berry phase is not the mechanism

The geometric (Berry) phase per major revolution —
Ω = 2π(1 − cos θ_pitch) where θ_pitch is the helix angle —
does not match the required shear.  At q = 137:

    Berry phase / revolution  = 0.0122 × 2π
    Required δ/L_θ            = 0.00365
    Ratio                     = 3.35

The Berry phase is 3.35× too large.  This ratio varies
strongly with q (from 0.05 at q = 83 to 154 at q = 263),
ruling out a simple proportionality.  The shear does not come
from the geometric phase of photon propagation on a helix.


### F16. What changes during one crossing?

The photon completes one major circuit in time T = α T_Compton.
During this time:

- It traverses distance ℓ = λ_C/137 ≈ 1.77 × 10⁻¹⁴ m
- Its phase advances by Δφ = 2πα ≈ 0.046 rad (2.6°)
- Only α of a wavelength fits around the major circle
- L_φ/λ_C = α: the photon is ~137× "larger" than the torus
  circumference

The photon's own electromagnetic field permeates the entire
torus.  It is not localized to a point — it wraps around and
overlaps itself.  The Coulomb self-energy U = m_e c²/2 means
the field is strongly self-interacting at this scale.

The observation that δ ≈ αR (within ~6%) suggests the shear
may be caused by the photon's electromagnetic self-interaction:
on each circuit, the photon propagates through its own Coulomb
field, which shifts the effective boundary condition by a
distance of order α × R.  However, this has not been confirmed
as an exact relationship.


### F17. Track 5 resolution study

Track 5 tested the Track 4 hypothesis g(1/π) = π/√(4π²+1)
by computing g at increasing grid resolutions using a
φ-symmetry-reduced pairwise sum (O(N_θ² N_φ) instead of
O(N²)).

Key findings:

1. **g(r) increases with resolution at all r values** (by
   ~2-3% from 24×48 to 192×384), because finer grids better
   resolve the Coulomb near-singularity.

2. **g(1/π) ≈ 0.503, not 0.494.**  The 32×64 result (0.4924)
   was close to the target by accident.

3. **The q = 137 solution is robust** despite the g shift.
   As g increases, the solution moves to larger r, keeping
   R/r_e ≈ 0.989 stable across all resolutions (because
   q = 1/α forces g√(1+r²/4) = 1/2).

4. **r = 1/π has no special status.**  The converged q = 137
   aspect ratio is r ≈ 0.34, not 1/π = 0.318.

5. **δ/(αR) ≈ 1.06 at the converged solution**, not 1.00.
   Close enough to suggest electromagnetic origin, but not
   an exact identity.

The self-consistency argument (F17 in the previous version)
remains plausible as a qualitative picture — the shear IS of
order α and the EM self-interaction IS the right scale — but
it cannot be claimed as an exact, zero-free-parameter result.


---

## Updated summary

| Property | Value | Determined by |
|----------|-------|---------------|
| Mass m_e | Path = λ_C | Construction |
| Charge e | U = m_e c²/2 | Shape factor + R ≈ r_e |
| Spin ½ | Exact 1:2 on sheared T² | Track 2 |
| μ = μ_B | g = 2 from photon spin-1 | Track 3 |
| R ≈ r_e | R/r_e = 0.989 at q = 137 | Tracks 1, 5 |
| δ ≈ αR | δ/(αR) ≈ 1.06 | Track 4 (approximate) |
| r | ≈ 0.34 (at q = 137) | Track 5 (converged) |
| q | Free parameter (~100–287) | Not yet selected |


### What remains open

1. **What selects q (and hence the shear)?**  Every odd q
   from ~100 to ~287 has a valid geometry satisfying the mass
   and charge constraints.  The shear δ/L_θ = 1/(2q) is the
   one remaining free parameter.  Track 4 found δ ≈ αR
   (within ~6%) and ruled out the Berry phase as the mechanism.

   **Mechanisms ruled out:**
   - *EM self-force:* a classical photon doesn't couple to
     static EM fields (superposition principle).
   - *KK gravitational self-consistent metric:* R1 showed
     gravitational coupling at the electron scale is
     Gm_e/(Rc²) ~ 10⁻⁴³, which is 41 orders of magnitude
     too weak to produce δ/R ~ α ~ 10⁻².
   - *Berry phase:* wrong scaling (Track 4).

   **Active leads:**
   - *EM self-consistency:* The WvM charge mechanism is purely
     electromagnetic (no G).  Solving Maxwell's equations on
     the sheared T² might reveal that self-consistent EM
     solutions exist only for specific shear values.  This
     would determine α from EM boundary conditions alone.
   - *Variational principle / least-expensive path:* the
     photon must find the closed path on the sheared T² that
     minimizes phase mismatch, maximizes field uniformity,
     and concentrates all energy in the fundamental Compton
     mode.  Minimize E_total(q) across the R8 solution
     family.  See Q29.
   - *Prime q / harmonic avoidance:* 137 is prime.  For
     composite q, every divisor creates a sub-harmonic mode
     that can drain energy from the fundamental resonance.
     For prime q, no leakage channels exist — all energy
     stays in the fundamental.  See Q30.

   **R11 update (Track 2c):** The geodesic Coulomb self-energy
   does NOT select q ≈ 137.  The original Track 2 minimum was
   a numerical artifact of insufficient resolution (retracted).
   Static Coulomb energy is ruled out as a selector.  Magnetic
   self-energy and wave propagation remain untested.

2. **Anomalous magnetic moment.**  Track 3 established the
   leading-order result μ = μ_B (g = 2) from the photon's
   spin-1 nature and the electron's spin-½ topology.  The
   measured g − 2 ≈ α/π is attributed in WvM's framework to
   the fraction of field energy in the non-co-rotating
   (external) component.  Whether this fraction depends on
   the torus geometry — which changed drastically from WvM's
   fat Compton-scale torus to R8's thin r_e-scale torus — has
   not been checked.  A calculation of the external field
   fraction for the multi-winding geometry would test whether
   the α/π correction carries over.

3. **Higher-precision shape factor.**  Track 5 showed g(r)
   has not fully converged at 192×384 resolution (still
   drifting at ~0.1% per grid doubling).  The converged g
   values would sharpen the solution curve and pin down r at
   q = 137 more precisely.  Approaches include: analytical
   evaluation using toroidal harmonics, ring decomposition
   with elliptic integrals (requiring careful treatment of
   the ring self-energy), or Richardson extrapolation from
   the existing data.


## Scripts

- [`scripts/geometry_search.py`](scripts/geometry_search.py) —
  Track 1: shape factor computation and geometry sweep
- [`scripts/shear_analysis.py`](scripts/shear_analysis.py) —
  Track 4: shear δ analysis and hypothesis testing
- [`scripts/verify_g.py`](scripts/verify_g.py) —
  Track 5: high-resolution g(1/π) convergence study
- [`scripts/verify_crosscheck.py`](scripts/verify_crosscheck.py) —
  Track 5: cross-check symmetry-reduced vs full pairwise sum
- [`scripts/verify_curve.py`](scripts/verify_curve.py) —
  Track 5: solution curve at multiple resolutions
