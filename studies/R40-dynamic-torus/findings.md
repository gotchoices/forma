# R40. Self-consistent dynamic torus — Findings

**Date:** 2026-03-28 (Tracks 1–5), 2026-03-01 (Tracks 6–8)
**Status:** COMPLETE — Dynamic Ma deformation is negligible (F23)
**Scripts:** `track1_pressure_profile.py`, `track2_self_consistent_shape.py`,
  `track3_mode_spectrum.py`, `track4_per_mode_shapes.py`,
  `track5_surface_tension.py`, `track6_clairaut_geodesic.py`,
  `track8_free_r_optimization.py`
**Library:** `lib/ma_model.py`, `lib/embedded.py`


## Geometry

The proton sheet geometry is fully determined by r_p = 8.906
(R27 F18).  The embedded torus has:

| Parameter | Value | Note |
|-----------|-------|------|
| L_tube | 23.48 fm | tube circumference |
| L_ring | 2.637 fm | ring circumference |
| a (tube radius) | 3.738 fm | L_tube / 2π |
| R (ring radius) | 0.420 fm | L_ring / 2π |
| a/R | 8.906 | self-intersecting (a >> R) |

The photon is a (1,2) mode — one tube winding, two ring windings.
On the flat torus it is a uniform plane wave.  On the 3D embedding
it follows a helical path whose curvature varies with position.


## F1. The photon pushes outward against the tube wall everywhere (Track 1)

The (1,2) geodesic curves in 3D as it spirals around the tube.  The
curvature vector points toward the tube axis (center of curvature).
The centrifugal reaction force — the radiation pressure on the tube
wall — pushes **outward**, radially away from the tube axis, at every
point along the path.

There are no regions of inward push.  The confining medium must
supply an inward restoring force everywhere on the tube wall.

The 3D curvature magnitude varies from 0.24 fm⁻¹ (at the outer
equator, θ₁ = 0) to 1.10 fm⁻¹ (at the top/bottom, θ₁ = π/2),
but the **radial** component (the part that pushes on the wall)
is more uniform: 0.24–0.30 fm⁻¹.  The large total curvature at
the top/bottom is mostly tangential to the surface (it bends the
path along the surface, not away from it).


## F2. The pressure is 26% non-uniform — circular cross-section is NOT in equilibrium (Track 1)

The outward radial force on the tube wall, averaged by tube angle
θ₁, varies by 26% RMS around its mean.  The peak-to-trough ratio
is 2.3:1 (strongest at θ₁ = 0, π; weakest at θ₁ = π/2, 3π/2).

A perfectly circular tube cross-section would require uniform
inward restoring pressure.  The 26% non-uniformity means either:

1. The tube deforms until the pressure becomes uniform on the
   new shape, or
2. The confining medium supplies a non-uniform restoring force
   that exactly matches the pressure profile

Either way, the circular cross-section is an approximation, not
an equilibrium.


## F3. The dominant deformation is elliptical — k=2 at 37% of mean (Track 1)

Fourier decomposition of the pressure profile P(θ₁):

| k | Physical meaning | Amplitude/mean | Drives what? |
|---|-----------------|----------------|--------------|
| 0 | Uniform (mean pressure) | 100% | Overall confinement |
| 1 | Off-center shift | 0.07% | Negligible |
| **2** | **Elliptical** | **36.9%** | **Dominant: squeezes circle into ellipse** |
| 3 | Triangular | 0.09% | Negligible |
| 4 | Square | 3.6% | Small correction |
| 6 | Hexagonal | 0.7% | Negligible |

The k=2 harmonic (cos 2θ₁) is overwhelmingly dominant among the
non-uniform components.  Odd harmonics (k=1, 3, 5, 7) are
negligible — the pressure has a clean top-bottom symmetry.

The physical meaning: the photon pushes hardest against the wall
at the "equators" (θ₁ = 0 and θ₁ = π, where the path is most
aligned with the ring direction and the 3D curvature is smallest)
and least at the "poles" (θ₁ = π/2 and 3π/2, where the path
bends most sharply around the tube).

This pressure pattern drives an **elliptical deformation** of the
tube cross-section: elongated along the equatorial axis (the ring
plane) and compressed along the polar axis.


## F4. The even-harmonic dominance is a consequence of the (1,2) symmetry

The (1,2) geodesic visits each tube angle θ₁ twice per period —
once on the "outward" ring half and once on the "inward" half.
The two visits contribute identical radial forces (by symmetry
of the embedded torus under θ₂ → θ₂ + π).  This means the
pressure at θ₁ equals the pressure at θ₁ (same point, different
visit), so no asymmetry is introduced between visits.

The top-bottom symmetry (P(θ₁) = P(−θ₁)) comes from the torus
being symmetric under z → −z.  This kills all odd Fourier
components.

Together: only even harmonics (k = 0, 2, 4, 6, ...) survive.
The k=2 (elliptical) is the first and largest.

**For a different mode — say (1,3) — the symmetry is different,
and the pressure profile would have odd harmonics too.  This
means different modes drive different deformations.**


## Implications

### For the self-consistent shape (Track 2)

The 37% k=2 pressure harmonic is large.  The equilibrium shape
will be measurably elliptical.  Track 2 will find the actual shape
by minimizing mode energy over the Fourier shape parameters.

### For ghost suppression

Different modes have different pressure profiles.  A mode whose
pressure profile is incompatible with the equilibrium shape
(e.g., it drives k=3 triangular deformation on an elliptical
surface) would be geometrically frustrated — it cannot exist as a
stable particle on this surface.  Track 3 will test this.

### For the confining medium

The pressure profile P(θ₁) is now measured data.  Whatever
restoring force the confining medium supplies must match this
profile at equilibrium.  If the equilibrium shape is known
(Track 2), the restoring pressure at each point is fully
determined: P_in(θ₁) = P_rad(θ₁) on the equilibrium shape.
This reverses the problem — instead of assuming a rigidity model,
we can read it off from the self-consistent calculation.


## F5. The energy-minimizing shape is 14.5% lower than circular (Track 2)

At constant geodesic path length (the Compton constraint), the (1,2)
mode eigenvalue on a deformed cross-section is significantly lower
than on a circle:

| Shape | a₂/a | a₄/a | λ | Δλ/λ_circ |
|-------|------|------|---|-----------|
| Circular | 0 | 0 | 0.7238 | — |
| Best a₂ only | +0.50 | 0 | 0.6372 | −11.9% |
| Optimized (a₂, a₄) | +0.056 | −0.196 | 0.6191 | **−14.5%** |

The energy drop is not perturbative — it is a substantial 14.5%
reduction from the circular shape.  The photon strongly prefers
the deformed geometry.


## F6. The optimal cross-section has a 4-lobed structure (Track 2)

The dominant deformation is a₄ (cos 4θ₁), not a₂ (cos 2θ₁).
This creates a cross-section with four lobes at θ₁ = 45°, 135°,
225°, 315° (the diagonal positions), with compressions at the
equators (θ₁ = 0°, 180°) and poles (θ₁ = 90°, 270°):

    r(θ₁) at key angles (a_circle = 3.74 fm):

    | θ₁ | r_opt (fm) | Δr/a | Description |
    |----|-----------|------|-------------|
    | 0° (outer eq.) | 2.92 | −22% | Compressed |
    | 30° | 3.91 | +5% | Lobe |
    | 90° (top) | 2.50 | −33% | Compressed |
    | 150° | 3.91 | +5% | Lobe |
    | 180° (inner eq.) | 2.92 | −22% | Compressed |
    | 270° (bottom) | 2.50 | −33% | Compressed |

The cross-section looks like a rounded square rotated 45° relative
to the torus plane, with 33% compression at the poles (where the
photon path curves most sharply in 3D) and lobes at the diagonals.


## F7. The optimization has not fully converged — deeper minima likely exist (Track 2)

The 2-parameter search (a₂, a₄) found −14.5%.  Adding more Fourier
harmonics (a₆, a₈, ...) would likely find a deeper minimum, since
the k=6 component of the pressure was 0.7% of the mean (small but
nonzero).

The a₂-only sweep showed the energy still descending at the boundary
(a₂/a = 0.4, −11.1%) before turning over at a₂/a ≈ 0.5 (−12.0%).
The 2-parameter optimizer found a qualitatively different minimum
with small a₂ but large a₄, suggesting the energy landscape is
multimodal.

A more complete optimization (3+ parameters, global search) should
be done before quoting final numbers.  But the qualitative result
is clear: **the self-consistent shape is measurably non-circular
with an energy reduction of order 10–15%.**


## Implications

### The circular torus was never the right shape

Every study from R1 through R39 used a circular cross-section.  The
14.5% energy shift means mode energies, charge integrals, and
multipole moments all carry systematic errors of this order.  The
good news: many results (like charge = integer, spin = ½) are
topological and survive the deformation.  The quantitative results
(mass predictions, suppression factors) may shift.

### The moduli potential has structure

R37 F7 found a broad minimum at r ≈ 0.5 from energy minimization
along the α curve.  Track 2 shows the energy landscape has
additional structure IN the cross-section shape.  The full moduli
potential is a function of both r (aspect ratio) AND the shape
parameters (a₂, a₄, ...).  This higher-dimensional landscape may
have a sharper minimum than the r-only slice.

### Ghost suppression mechanism

If the equilibrium shape is 4-lobed, only modes whose pressure
patterns are compatible with this 4-fold symmetry can be stable.
Modes that drive 3-fold or 5-fold deformations would fight the
equilibrium shape and dissipate.  Track 3 should test this by
computing which modes are compatible with the Track 2 shape.

### Next steps

- **Track 3**: Compute mode spectrum on the optimal shape.  Which
  modes survive?  How many ghosts are suppressed?
- **Higher-parameter optimization**: Add a₆, a₈ and use global
  search to find the true minimum.
- **Recompute R39**: What does the near-field interaction look like
  on the deformed torus?  The 33% compression at the poles changes
  the charge distribution significantly.


## F8. Most modes are lowered by the deformation — the ghost filter is weak (Track 3)

Of 49 mode families tested (n₁ = 0..3, n₂ = 0..6):

| Category | Count | Fraction |
|----------|-------|----------|
| Energy lowered (> 0.5%) | 33 | 67% |
| Energy raised (> 0.5%) | 14 | 29% |
| Roughly unchanged | 2 | 4% |

The deformation benefits most modes, not just the (1,2) fundamental.
The shape is not a selective filter that suppresses ghosts.

**However, the pattern of which modes are raised is informative.**


## F9. Pure ring modes (n₁=0) are systematically raised (Track 3)

The clearest split is by tube winding number n₁:

| n₁ | Typical shift | Interpretation |
|----|--------------|----------------|
| 0 | +3% to +18% | **Raised** — punished by the shape |
| 1 | −15% to +24% | **Mixed** — depends on n₂ |
| 2 | −2% to −7% | **Lowered** — compatible |
| 3 | −2% to −15% | **Lowered** — compatible |

The n₁ = 0 modes (pure ring windings, no tube winding) are
consistently penalized.  These are bosonic (spin 0) modes with no
charge.  The deformation, which is driven by the (1,2) mode's tube
winding, disfavors modes that don't wind around the tube.

This is not ghost suppression (ghosts have n₁ ≠ 0), but it IS a
mode selection effect — the shape preferentially stabilizes modes
with tube windings.


## F10. High-n₂ modes with n₁=1 flip from lowered to raised (Track 3)

For n₁ = 1 (the charge-carrying tube winding):

| n₂ | Shift | Note |
|----|-------|------|
| 0 | −21.8% | Strongly lowered |
| 1 | −17.5% | Strongly lowered |
| 2 | −14.5% | Lowered (this is the proton/electron) |
| 3 | +8.3% | **Raised** |
| 4 | +23.6% | **Strongly raised** |
| 5 | +17.6% | Raised |

The crossover happens at n₂ ≈ 3.  Modes with many ring windings
(n₂ > 2) are penalized by the deformed shape.

This IS a ghost suppression signal for the (1,q) family: the (1,2)
electron/proton is stabilized, but (1,4), (1,5), (1,6) — which
would be ghost charged particles at higher energies — are
destabilized.  The shape acts as a **bandpass filter on n₂**.

The cutoff at n₂ ≈ 3 is suggestive.  If only (1,1) and (1,2) modes
survive as stable charged particles, that naturally limits the
spectrum.  The (1,1) mode has spin 1 — it could be a W-like boson.


## F11. All modes see the same pressure pattern — k=2 dominant (Track 3)

The Fourier decomposition of the radiation pressure shows that
every (n₁ ≠ 0, n₂) mode drives a cos 2θ₁ (elliptical) pressure
pattern.  The amplitude grows with n₂:

| Mode | |A₂|/A₀ | |A₄|/A₀ |
|------|---------|---------|
| (1,1) | 17% | 0.8% |
| (1,2) | 37% | 3.6% |
| (1,3) | 48% | 6.4% |
| (1,4) | 54% | 8.3% |

Higher ring windings drive stronger elliptical deformation.
This explains F10: modes with large n₂ "want" a more strongly
deformed shape than the (1,2) equilibrium provides.  They're
geometrically frustrated.

The (0,n₂) modes have anomalous pressure profiles (all harmonics
equal), reflecting their purely ring-winding character.  They don't
couple to the tube geometry at all.


## Implications (updated)

### Ghost suppression: partial, not complete

The deformed shape doesn't kill ghosts by wholesale elimination.
Instead, it creates a **bandpass on ring winding number**: modes
with n₂ ≤ 2 are stabilized, modes with n₂ ≥ 4 are destabilized.
This is a significant reduction — it cuts the ghost count
substantially — but doesn't explain why only ~40 particles exist.

A complete ghost filter likely requires BOTH the shape selectivity
(this study) AND an additional mechanism (perhaps the Q-factor
bandwidth from R38, or the WvM coupling form factor from R33).

### The (1,1) boson is stabilized

The (1,1) mode (charge ±1, spin 1) drops 17.5% in energy on the
deformed shape.  This is a candidate for the W boson.  Its
stabilization by the shape is a positive sign.

### Next steps

- **Self-consistent shape for EACH mode**: Track 2 found the shape
  optimal for (1,2).  But each mode would deform the shape
  differently.  A mode is truly stable only if its own
  self-consistent shape exists.  Test: compute the optimal shape
  for (1,3), (1,4) and see if they have valid equilibria.
- **Multi-mode equilibrium**: In reality, the shape is determined
  by the mode that occupies the torus (the particle).  Different
  particles live on differently-shaped tori.  The mass spectrum
  should be recomputed with each particle on its own optimal shape.
- **Add more Fourier terms** to the Track 2 optimization for a
  better equilibrium shape before drawing final conclusions.


---

## Library design notes

The self-consistent shape computation should become reusable library
code.  Notes for a future `lib/dynamic_torus.py` (or extension to
`embedded.py`):

### Core data structure: DeformedSheet

Like `EmbeddedSheet` but with a non-circular cross-section.
Parameterized by Fourier coefficients (a₀, a₂, a₄, ...).

```
DeformedSheet
  State:  a₀, [a₂, a₄, ...], R_major
  Derived: cross-section curve r(θ₁), surface metric, geodesic paths

  Core:
    cross_section(theta1)    → r values
    torus_point(theta1, theta2) → (x, y, z)  [override EmbeddedSheet]
    geodesic(n1, n2, N, phi) → positions     [on deformed surface]
    path_length(n1, n2)      → float

  Eigenvalue:
    solve_mode(n2, n_eigs)   → eigenvalues, eigenvectors
    mode_energy(n1, n2)      → float (single mode)
    mode_spectrum(n2_max, n1_max) → table

  Pressure:
    pressure_profile(n1, n2) → P(θ₁) array
    pressure_fourier(n1, n2, k_max) → Fourier coefficients
    pressure_nonuniformity(n1, n2) → RMS/mean

  Shape optimization:
    optimal_shape(n1, n2, k_max, constraint='path_length')
        → DeformedSheet at energy minimum
    energy_landscape(n1, n2, param_name, values)
        → array of eigenvalues vs shape parameter
```

### Key design decisions

1. **Immutable** like `Ma` and `EmbeddedSheet`.  `with_coeffs()`
   for parameter sweeps.

2. **The Sturm-Liouville solver is the inner loop.**  It must be
   fast.  The current implementation (dense matrix eigenvalue) is
   O(N³).  For N=256 this is fine (~ms per solve).  For N=1024
   it may need banded solvers.

3. **The path-length constraint** is what makes this physical.  The
   photon's energy is fixed (= particle mass), so the Compton
   wavelength is fixed.  The shape must adjust to maintain constant
   path length.  This is enforced via rescaling a₀ at each step.

4. **Multiple constraint options**:
   - `constraint='path_length'`: fix the geodesic path length
     (Compton condition, used in Track 2)
   - `constraint='area'`: fix the torus surface area
   - `constraint='volume'`: fix the enclosed volume
   Different constraints give different equilibria — worth
   exploring.

5. **Should compose with EmbeddedSheet**, not replace it.
   `DeformedSheet.charge_segments()` etc. should work so that
   R39-style near-field calculations can be rerun on the deformed
   geometry.

6. **The pressure computation reuses embedded.py's curvature
   calculation** but needs the tube-radial decomposition (Section 2
   of Track 1).  Factor this out as a `curvature_decomposition()`
   method.

7. **The eigenvalue solver should cache results** since the same
   shape gets queried for multiple (n₁, n₂) modes in Track 3.

8. **Per-mode optimization needs to be efficient** — Track 4 shows
   each mode has its own optimal shape.  A `batch_optimize()` method
   that runs Nelder-Mead for a list of modes would be useful.  The
   key optimization: reuse the path-length rescaling (brentq on a₀)
   across modes since it's the most expensive step.


## F12. Every mode can find a stabilizing shape — no absolute suppression (Track 4)

All 12 modes tested find a cross-section deformation that lowers
their eigenvalue.  No mode is geometrically forbidden in the
sense of having no valid equilibrium.

| Mode | Δλ/λ on own optimal shape |
|------|---------------------------|
| (1,1) | −21.7% |
| (1,2) | −14.5% |
| (1,3) | −10.7% |
| (1,4) | −47.0% |
| (1,5) | −55.7% |
| (1,6) | −61.3% |

This means ghost suppression cannot come from shape optimization
alone.  If each particle can freely choose its torus shape, all
modes are viable.


## F13. Modes prefer DRAMATICALLY different shapes (Track 4)

The optimal shape parameters vary widely across modes:

| Parameter | Range across modes | Interpretation |
|-----------|-------------------|----------------|
| a₂/a | −0.17 to +0.79 | From mildly 4-lobed to strongly elliptical |
| a₄/a | −0.22 to +0.47 | From 4-lobed inward to 4-lobed outward |

The spread (0.96 in a₂, 0.68 in a₄) is enormous — each mode
wants a fundamentally different torus shape.

**Key pattern**: low-n₂ modes (1,1), (1,2) prefer **4-lobed**
shapes (negative a₄).  High-n₂ modes (1,4), (1,5), (1,6) prefer
**strongly elliptical** shapes (large positive a₂, positive a₄).

This means different particles would live on differently shaped
material sheets.  The flat-torus model (one geometry for all
modes) is qualitatively wrong — each particle reshapes its own
torus.


## F14. The high-n₂ energy drops are suspiciously large (Track 4)

The (1,4) through (1,6) modes show energy reductions of 47–61%
on their optimal shapes.  This is enormous — much larger than the
(1,2) mode's 14.5%.

These modes achieve this by extreme deformation: a₂/a ≈ +0.79,
making the cross-section strongly elongated.  On such a shape,
the ring circumference effectively increases (the path wraps
around a longer, thinner profile), reducing the energy per ring
winding.

This needs scrutiny:
- Are the optimal shapes physically valid?  (The cross-section
  stays positive, but does it make geometric sense?)
- Does the 2-parameter optimization (a₂, a₄ only) give reliable
  results at such large deformations?
- Would a more refined model (surface tension, volume constraint)
  prevent these extreme shapes?

If the large energy drops are real, they have a striking
implication: high-n₂ "ghost" modes that were 2–4× heavier than
the proton on the circular torus become comparable in mass on
their optimal shapes.  **The ghost problem gets WORSE, not better.**


## F15. The ghost filter must come from shape TRANSITIONS, not shape optimization (Track 4)

Track 3 showed that modes are raised or lowered on the (1,2)
shape — a filter exists IF all modes must live on the same torus.
Track 4 shows that each mode can escape the filter by finding its
own shape.

The resolution: **shape is not free.**  The torus shape is
determined by the mode that occupies it.  A proton's torus has the
(1,2)-optimal 4-lobed shape.  For a ghost mode to appear, it
must either:

1. **Nucleate on the existing (1,2) shape** — and Track 3 shows
   high-n₂ modes are penalized on this shape (+24% for (1,4)).
2. **Reshape the torus** — which costs energy (the deformation
   energy of the confining medium).

The ghost suppression mechanism is therefore a **barrier**: the
energy cost of reshaping the torus from the (1,2) equilibrium to
a ghost mode's equilibrium.  If this barrier exceeds the available
energy, the ghost cannot form.

This is directly computable: the barrier height is
|E_mode(1,2 shape) − E_mode(own shape)| × (some stiffness factor).
Track 3 already has E_mode(1,2 shape).  Track 4 has E_mode(own shape).
The stiffness factor is the missing piece — it comes from the
confining medium's rigidity, which this study intentionally left
unspecified.

**This connects back to Q90:** ephemeral particles (quarks, excited
baryons) might be modes that partially reshape the torus for a
brief time, decaying back to the ground-state shape.  The reshape
time ≈ the particle lifetime.


## F16. Surface tension is NOT a consistent single-parameter model (Track 5)

Estimating σ from the ratio of driving pressure to deformation
amplitude at each harmonic:

    σ = Pₖ × a₀² / ((k²−1) × aₖ)

gives wildly inconsistent values:

    σ from k=2: 11.5
    σ from k=4: 0.066
    Ratio: 0.006

A 175× discrepancy.  Pure surface tension (P_restore ∝ κ) does
not explain the Track 2 equilibrium.  The actual restoring force
has a different functional form — it penalizes k=4 deformations
much LESS than surface tension would predict.

This makes physical sense: the confining medium is not a soap
film.  It's the rigidity of a compact spatial dimension, which
likely has its own dynamics (bending stiffness, metric elasticity,
etc.).


## F17. All modes drive k=2 (elliptical) — no k-based mode filtering (Track 5)

Every (n₁, n₂) mode tested has k=2 as its dominant pressure
harmonic.  The amplitude increases with n₂ (17% for (1,1), 60%
for (1,6)), but the harmonic identity doesn't change.

This means surface tension's k² low-pass filter does NOT
discriminate between modes by harmonic number — they all drive
the same harmonic.  The filter would suppress all modes equally.

The mode discrimination seen in Track 3 (F10: high-n₂ modes
penalized on the (1,2) shape) comes from the AMPLITUDE of the
k=2 pressure, not from driving a higher harmonic.  A (1,6) mode
wants a more strongly elliptical shape than (1,2), so it's
frustrated on the (1,2)-optimal shape — but it's not fighting a
higher-k restoring force.


## F18. Surface tension smooths the shape toward elliptical (Track 5)

Adding a surface tension penalty (σ_eff × ΔPerimeter) to the
energy minimization:

| σ_eff | a₂/a | a₄/a | Shape character |
|-------|------|------|-----------------|
| 0.00 | +0.056 | −0.196 | 4-lobed (Track 2 result) |
| 0.01 | +0.033 | −0.184 | 4-lobed (slightly softer) |
| 0.05 | +0.377 | +0.069 | Elliptical |
| 0.10 | +0.217 | −0.010 | Elliptical (a₄ ≈ 0) |
| 0.50 | +0.159 | −0.012 | Mildly elliptical |
| 1.00 | +0.152 | −0.010 | Mildly elliptical |

At σ_eff ≈ 0.05–0.10, the a₄ component is suppressed and the
shape becomes a clean ellipse (a₂ only).  At higher σ, the
ellipticity itself is moderated.

The transition from 4-lobed to elliptical happens at σ_eff ≈ 0.05.
Below this, the k=4 deformation is energetically favorable.  Above
it, surface tension kills k=4 and only k=2 survives.

**Note:** At high σ_eff (> 0.5), the total energy goes negative
because the perimeter DECREASES relative to the circle (the
elliptical shape is actually shorter than a circle at the same
enclosed area).  This means the σ_eff × ΔPerimeter model breaks
down at high σ — a more physical model would use a different
functional (e.g., deviation from a specific reference shape, or
bending energy rather than perimeter).


## F19. The embedded geodesic is 34–58% shorter than the flat-torus geodesic (Track 6)

On a surface of revolution, the true geodesic follows Clairaut's
relation (ρ sin α = C) rather than the flat-torus straight line
(θ₂ = 2θ₁).  The Clairaut geodesic concentrates ring winding near
the inner equator (where ρ is smallest) and barely advances in θ₂
near the outer equator.  For the (1,2) mode:

| a/R | ΔL/L (Clairaut vs flat) | C/ρ_min |
|-----|------------------------|---------|
| 0.50 | −33.8% | 1.000 |
| 0.70 | −45.0% | 0.999 |
| 0.90 | −55.1% | 0.959 |
| 0.95 | −57.0% | 0.867 |
| 0.99 | −58.0% | 0.516 |

The Clairaut geodesic is the TRUE shortest path on the embedded
surface.  The flat geodesic is the intrinsic geodesic painted onto
the embedding — it is not length-minimizing in 3D.


## F20. The Clairaut geodesic doesn't exist for self-intersecting tori (Track 6)

For a/R > 1, ρ(θ₁) = R + a cos θ₁ passes through zero.  At ρ = 0,
g₂₂ = ρ² = 0 and the metric degenerates.  No closed geodesic with
n₂ ≠ 0 can traverse ρ = 0 — the geodesic would need to wind
infinitely many times in θ₂ to pass through the singularity.

For the proton sheet (a/R = 8.906):
- ρ = 0 at θ₁ = 96.4° and 263.6°
- 46% of the tube has ρ < 0

**All known particles** in MaSt have a/R > 1 (r_e ≈ 6.6, r_p ≈ 8.9).
The embedded Clairaut geodesic is undefined for all of them.

This is not a computational limitation but a structural consequence
of the self-intersecting embedding: the 3D surface passes through
itself at ρ = 0, and the surface metric degenerates there.


## F21. The flat-geodesic optimization naturally reduces the discrepancy (Track 6)

When Track 2's shape optimization produces negative a₂ (compressing
the cross-section at the equators), ρ_min increases and the
geometry moves toward non-self-intersection.  On these optimized
shapes, the flat-Clairaut path-length difference drops dramatically:

| a/R | ΔL/L on circle | ΔL/L on Track 2 shape |
|-----|----------------|-----------------------|
| 0.5 | −33.8% | −3.5% |
| 0.7 | −45.0% | −4.6% |
| 0.9 | −55.1% | −6.3% |

The optimization gravitates toward geometries where the two geodesic
types converge.  This partially validates Tracks 1–5: even though
they use the flat geodesic, the self-consistent shapes they find are
ones where that approximation is best.


## F22. The Dynamic Ma premise has a self-intersection problem (Track 6)

The study's premise — "the 3D embedding IS the physics" — requires
the geodesic to be well-defined on the embedded surface.  But for
a/R > 1 (all known particles), the embedded surface self-intersects
and no closed tube-circling geodesic exists.

Three possible resolutions:

1. **The deformation resolves it.**  If the equilibrium shape reduces
   a/R below 1 (by dramatically deforming the cross-section), the
   self-intersection vanishes.  Track 2's results show deformations
   of ~20–30%, not enough to bring a/R = 8.9 below 1.

2. **The embedding is not toroidal.**  A different embedding (e.g.,
   a knotted tube, or a higher-genus surface) might avoid self-
   intersection while preserving the mode structure.

3. **The physics is intrinsic, not embedded.**  The "radiation
   pressure" computed in Tracks 1–5 is actually a hybrid quantity:
   the intrinsic geodesic (flat-torus straight line) painted onto
   the embedded surface, then computing extrinsic curvature.  This
   hybrid may be the correct physical interpretation — the mode
   lives on the intrinsic geometry, and the embedding responds.


## F23. The Compton constraint alone does not determine the torus dimensions (Track 8)

The Compton wavelength gives one equation in two unknowns:

    √((n₁ L_tube)² + (n₂ L_ring)²) = λ_C

This constrains a curve in (L_tube, L_ring) space.  Every point on
this curve gives the correct proton mass.  The aspect ratio
r = L_tube/L_ring is a free parameter.

Track 8 swept r from 0.05 to 20.0 and computed the embedded
Sturm-Liouville eigenvalue at each point, with and without shape
optimization (a₂, a₄).  Results:

| r | λ_SL (circular) | λ_SL (optimized) | Self-intersecting? |
|---|----------------|-----------------|-------------------|
| 0.1 | 9478 | 9477 | no |
| 0.5 | 1220 | 817 | no |
| 1.0 | divergent | 555 | boundary |
| 5.0 | 238 | 185 | YES |
| 8.9 | 240 | — | YES |

The eigenvalue minimum on a circular cross-section is at r ≈ 5.2.
With shape optimization, the minimum stays in the self-intersecting
regime (r ≈ 5).  The embedded metric breaks the flat-torus symmetry
between tube and ring: it strongly prefers r > 1 (fat tube, thin
ring), which is self-intersecting.

In the static flat-torus model, the second constraint comes from
cross-sheet coupling (neutron mass pins r_p = 8.906).  In Dynamic
Ma, to determine r from first principles, a second equation is
needed — either a restoring force model, the fine-structure constant
condition, or a re-derived cross-sheet constraint.


## F24. Einstein stiffness makes Dynamic Ma deformation negligible

The R40 study deliberately left the restoring force unspecified:
"The restoring force is an OUTPUT of the calculation, not an input."
Tracks 1–5 computed the photon's radiation pressure on the tube
wall and found the shapes that would balance it IF the restoring
force were zero or weak.

But space has a known stiffness.  In general relativity, the
Einstein field equation relates stress-energy to spacetime
curvature:

    G_μν = (8πG/c⁴) T_μν

The factor c⁴/(8πG) ≈ 4.8 × 10⁴² N is the stiffness of
spacetime — the force required to produce unit curvature.  If the
compact Ma dimensions are part of spacetime (as in Kaluza-Klein),
their stiffness is governed by the same constant.

### The photon's radiation pressure

The (1,2) photon has energy E = m_p c² = 938 MeV and follows a
curved 3D geodesic on the embedded torus.  Its centrifugal force
against the tube wall:

    F = E × κ_radial

where κ_radial ≈ 0.27 fm⁻¹ (Track 1) is the outward radial
curvature.  This gives:

    F ≈ 938 MeV × 0.27 fm⁻¹ ≈ 253 MeV/fm ≈ 4 × 10⁴ N

The force is distributed over the torus surface area
A = 4π²Ra ≈ 62 fm² = 6.2 × 10⁻²⁹ m²:

    P_photon ≈ F / A ≈ 6.5 × 10³² Pa

### The restoring pressure from spatial rigidity

The Gaussian curvature of the torus surface is
K ~ 1/(aR) ≈ 0.64 fm⁻² = 6.4 × 10²⁹ m⁻².

In Einstein gravity, the pressure associated with maintaining
this curvature is:

    P_space ~ K × c⁴/(8πG) ≈ 6.4 × 10²⁹ × 4.8 × 10⁴² ≈ 3 × 10⁷² Pa

### The ratio

    P_photon / P_space ≈ 10⁻⁴⁰

The photon's radiation pressure is **40 orders of magnitude** weaker
than the spatial rigidity.  The deformation it produces is:

    δa/a ~ P_photon / P_space ~ 10⁻⁴⁰

This is zero for all practical purposes.  The 26% non-uniformity
of the radiation pressure (F2) is real, but the surface deformation
it drives is 10⁻⁴⁰ of the tube radius — undetectable by any
measurement and without physical consequence.

### Implications

1. **The circular cross-section IS the equilibrium** (to 10⁻⁴⁰
   precision).  Tracks 2–5 computed shapes that would arise if the
   restoring force were weak or absent.  With Einstein stiffness,
   those deformations do not occur.

2. **Ghost suppression via shape deformation does not work.**
   The band-filter mechanism (F10, F15) requires the torus to
   deform into a mode-dependent shape.  At 10⁻⁴⁰ deformation,
   no mode-dependent filtering occurs.

3. **The Dynamic Ma hypothesis is falsified** (in its current form).
   The premise was: the photon's radiation pressure deforms the
   torus, creating a self-consistent shape that filters modes.  If
   spatial rigidity is c⁴/(8πG), the photon cannot deform its
   cavity.

4. **An escape hatch exists** if the compact Ma dimensions have a
   stiffness much lower than c⁴/(8πG) — for instance, if they are
   stabilized by flux, brane tension, or some other mechanism with
   a characteristic scale far below the Planck scale.  This would
   require theoretical justification: why would the compact
   dimensions be 10⁴⁰ times softer than ordinary spacetime?

5. **The flat-torus model is vindicated.**  The rigidity result
   supports the assumption made in R1–R39: the torus geometry is
   fixed, and the mode is a perturbation on a rigid background.
   Whatever sets the torus shape (moduli stabilization, vacuum
   energy), it is not the photon's radiation pressure.


---

## Summary of R40

### Track inventory

| Track | Question | Result |
|-------|----------|--------|
| 1 | Radiation pressure on circular torus | 26% non-uniform, k=2 dominant (F1–F4) |
| 2 | Energy-minimizing shape at fixed path length | 4-lobed, 14.5% lower energy (F5–F7) |
| 3 | Mode spectrum on (1,2)-optimal shape | Band filter on n₂, crossover at n₂ ≈ 3 (F8–F11) |
| 4 | Per-mode optimal shapes | Every mode finds a stabilizing shape; shapes differ dramatically (F12–F15) |
| 5 | Surface tension as restoring model | Inconsistent; not the right functional form (F16–F18) |
| 6 | Clairaut geodesic on embedded torus | 34–58% shorter than flat geodesic; undefined for a/R > 1 (F19–F22) |
| 8 | Free-r optimization (no static-model input) | Eigenvalue prefers r ≈ 5 (self-intersecting); r undetermined by Compton alone (F23) |
| — | Einstein stiffness as restoring force | Deformation is 10⁻⁴⁰ — negligible; Dynamic Ma falsified in current form (F24) |

### What this study established

1. **The photon exerts real, non-uniform radiation pressure** on the
   torus wall (F1–F4).  The pressure profile is computable and
   mode-dependent.  This is solid physics regardless of the
   restoring force.

2. **IF the restoring force were weak**, the equilibrium shape would
   be non-circular, mode-dependent, and create a band filter on the
   mode spectrum (F5–F15).  These are conditional results — valid
   only if the stiffness is low enough for deformation to occur.

3. **The embedded geodesic does not exist** for any known particle
   (a/R > 1 for all).  The self-intersection problem is structural,
   not an artifact of the static model's r value.  Even with r as
   a free parameter, the embedded metric prefers r > 1 (F19–F23).

4. **Einstein's spatial stiffness kills the deformation hypothesis**
   (F24).  The photon's pressure is 10⁴⁰ times too weak to deform
   a compact dimension governed by c⁴/(8πG).  The torus shape is
   set by whatever mechanism stabilizes the compact geometry
   (moduli, vacuum energy), not by the photon.

### Conclusion

Dynamic Ma — the hypothesis that the photon's radiation pressure
shapes its own cavity — does not survive quantitative analysis.
The idea is physically well-motivated (energy does curve spacetime),
but the numbers are off by 40 orders of magnitude.  The torus is
rigid.

The flat-torus model used in R1–R39 is the correct approximation:
the mode is a perturbation on a fixed geometric background.  Ghost
suppression, if it exists, must come from a different mechanism —
perhaps the coupling form factor (R33), the cavity Q-factor (R38),
or a moduli potential (R37) that only supports specific geometries
in the first place.

The cross-sheet filtering idea (deformation modes leaking between
sheets via cross-shears) remains viable as a separate hypothesis,
but would need its own restoring-force analysis before proceeding.
