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
   but so do nearby values (within a few percent).  Is there
   an additional constraint that selects it exactly?


## Scripts

- [`scripts/geometry_search.py`](scripts/geometry_search.py) —
  Track 1: shape factor computation and geometry sweep
