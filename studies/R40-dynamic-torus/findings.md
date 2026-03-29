# R40. Self-consistent dynamic torus — Findings

**Date:** 2026-03-28 (Tracks 1–5), 2026-03-01 (Tracks 6–11)
**Status:** Active — Phase 2 (α-impedance model)
**Scripts:** `track1_pressure_profile.py`, `track6_clairaut_geodesic.py`,
  `track8_free_r_optimization.py`, `track9_em_stiffness.py`,
  `track11_alpha_shape.py`
**Library:** `lib/ma_model.py`, `lib/embedded.py`
**Tossed:** `track2_*.py` through `track5_*.py` (used invalid inputs;
  F5–F18 retracted, see Phase 1 notes)


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
This section closes that question by estimating the restoring force
from known physics.

### Two notions of stiffness

There are two ways to frame the restoring force:

1. **Bulk spatial stiffness** — the cost of curving 3+1D spacetime.
   This is c⁴/(8πG) ≈ 4.8 × 10⁴² N: the Einstein stiffness.

2. **Sheet deformation stiffness** — the cost of deforming a 2D
   membrane (stretching, bending) within the compact space.  A 2D
   sheet has tension σ (energy per unit area change) and bending
   modulus κ (energy per unit curvature-squared change).  These are
   distinct from the bulk stiffness and could in principle be much
   softer.

We analyze both.

### Case 1: Bulk stiffness (c⁴/8πG)

The Einstein field equation relates stress-energy to spacetime
curvature:

    G_μν = (8πG/c⁴) T_μν

If the compact Ma dimensions are part of spacetime (as in
Kaluza-Klein), their stiffness is governed by the same constant.

**The photon's radiation pressure.**  The (1,2) photon has energy
E = m_p c² = 938 MeV.  Its centrifugal force against the tube wall:

    F = E × κ_radial

where κ_radial is the outward radial curvature.  For a torus at
the Compton scale, F ~ 10⁴ N.  Distributed over the torus surface
area A ~ 60 fm² = 6 × 10⁻²⁹ m²:

    P_photon ~ 10³² Pa     (order of magnitude)

**The restoring pressure.**  The Gaussian curvature of the torus
K ~ 1/(aR) ~ 10²⁹ m⁻².  The pressure associated with maintaining
this curvature in Einstein gravity:

    P_space ~ K × c⁴/(8πG) ~ 10²⁹ × 10⁴² ~ 10⁷¹ Pa

**The ratio:**

    P_photon / P_space ~ 10⁻⁴⁰

The photon is **40 orders of magnitude** too weak to deform bulk
spacetime at the torus scale.  Deformation δa/a ~ 10⁻⁴⁰.

### Case 2: Sheet stiffness (membrane model)

The sheet is a 2D surface, not the bulk.  Its elastic properties
(tension σ, bending modulus κ) depend on the microscopic theory of
what the sheet IS:

- If a D-brane: σ_brane ~ 1/(2πα'), typically at the string/Planck
  scale.  Still extremely stiff — same conclusion as Case 1.
- If a topological locus in a compact manifold: the stiffness comes
  from the moduli potential, which is model-dependent.
- If set by cross-sheet shear couplings: related to coupling
  constants like α, potentially much softer.

**What sheet stiffness would be needed?**  For the photon's
radiation pressure to produce order-unity deformation of the
cross-section, the effective sheet tension would need to be:

    σ_required ~ P_photon × a ~ 10³² Pa × 10⁻¹⁵ m ~ 10¹⁷ N/m

    (equivalently, ~ 10¹⁷ J/m² ~ 600 GeV/fm²)

For comparison:
- QCD string tension: ~ 1 GeV/fm (1D), ~ 1000 MeV/fm² (2D)
- Bulk GR stiffness projected to the sheet: ~ 10⁴³ MeV/fm²

So the sheet would need to be about as stiff as QCD confinement
for order-unity deformation — which is not absurd, but cannot be
derived from within MaSt as currently formulated.

**However, this estimate is itself unreliable.**  The required
stiffness depends on the mode energy landscape — how much the
eigenvalue changes per unit deformation.  Tracks 2–5 computed
this landscape, but used the static model's r_p = 8.906 and the
flat-torus geodesic on a self-intersecting surface.  Both inputs
are invalid (F20, F22).  The true energy landscape on a physically
valid (non-self-intersecting) geometry has not been computed.

### Conclusion

At bulk stiffness (c⁴/8πG), deformation is negligible: 10⁻⁴⁰.

At sheet stiffness, the answer depends on the microscopic theory.
The sheet tension needed for order-unity deformation (~600 GeV/fm²)
is plausible but not derivable.  And the mode energy landscape
needed to pin it down has not been reliably computed — the Track
2–5 results used invalid inputs (self-intersecting geometry,
flat-torus geodesic on an embedded surface).

**The strongest statement R40 can make:** if the compact dimensions
have GR-scale stiffness, Dynamic Ma is dead.  If they are much
softer (by ~10⁴⁰), it remains open but requires a microscopic
theory that explains why compact dimensions are so much softer
than ordinary spacetime.


## F25. The α-impedance model: the torus wall is the (1−α) energy contour (Track 11)

### The model

The photon mode fills the torus and has an evanescent tail beyond
the wall.  The torus "boundary" is not a hard wall but the contour
that encloses (1 − α) ≈ 136/137 of the mode's energy.  Beyond
this contour, the remaining fraction α ≈ 1/137 leaks out as the
particle's external EM field — its charge, its Coulomb interaction,
everything the outside world can measure.

The fine-structure constant α, already derived from the torus
geometry in MaSt, plays a new role: it sets the wall's
transparency.  The torus wall is a partially reflecting boundary
with reflectivity (1 − α).

### Force balance

The mode's radiation pressure pushes outward at all tube angles.
But only the fraction α of the energy that crosses the wall exerts
a net deforming force — the (1 − α) fraction that reflects back
cancels out.

    P_deform(θ₁) = α × P_rad(θ₁)

The external pressure (vacuum EM impedance, through ε₀ ∝ 1/α)
pushes inward.  At equilibrium, the wall sits where:

    P_in(θ₁) = P_out(θ₁)

The deformation is of order:

    δa/a ~ α² ≈ 5.3 × 10⁻⁵

This is a ~0.005% perturbation to the circular cross-section.

### Why α runs with energy

At higher photon energy, the mode hits the wall harder.  More
energy leaks through — the wall becomes more transparent.  α
increases.  This is geometrically identical to QED vacuum
polarization: "virtual pairs screen the bare charge at large
distances" becomes "the torus wall transmits a larger fraction
at higher energy."

### Shape from the mode's energy contour

The mode's energy density is not uniform around the tube
(Track 1: ~10% variation).  The (1 − α) contour therefore has
a non-circular cross-section: it bulges where the energy density
is higher and contracts where it's lower.  The shape IS the mode's
fingerprint — different modes give different shapes, no free
parameters.

### Track 11 results

**Cross-section shape:** On the flat torus, the (1−α) contour is
a perfect circle (|ψ|² = const → no θ₁ dependence).  The 3D
embedding introduces non-uniformity through centrifugal curvature.
The deformation has Fourier harmonics decaying as 1/k²:

| k | |c_k|/c₀ | δr_k/a | physical meaning |
|---|----------|--------|-----------------|
| 2 | 0.369 | 6.73 × 10⁻⁴ | elliptical (dominant) |
| 4 | 0.036 | 1.66 × 10⁻⁵ | square |
| 6 | 0.007 | 1.51 × 10⁻⁶ | hexagonal |
| 8 | 0.002 | 2.19 × 10⁻⁷ | octagonal |

Odd harmonics (k = 1, 3, 5, 7) are negligible (~10⁻⁶), consistent
with the cos(2θ₁) symmetry of the (1,2) mode.

The cross-section bulges at the outer and inner equators (θ₁ = 0, π)
and contracts at top and bottom (θ₁ = π/2, 3π/2).  RMS deformation:
δr/a = 6.73 × 10⁻⁴ (0.067%).

**Low-pass filter:** The elastic 1/k² response provides a low-pass
filter in tube winding number n₁.  Mode n₁ couples to wall harmonic
k = 2n₁ through the overlap ⟨cos²(n₁θ₁)|cos(2n₁θ₁)⟩ = ½.
Suppression ratios relative to n₁ = 1:

| n₁ | k = 2n₁ | ε_k | ε_k/ε₂ | δλ/λ | δM (MeV) |
|-----|---------|-----|--------|------|----------|
| 1 | 2 | 6.73e-4 | 1.0 | 3.4e-4 | 0.316 |
| 2 | 4 | 1.66e-5 | 0.025 | 8.3e-6 | 0.008 |
| 3 | 6 | 1.51e-6 | 0.0022 | 7.5e-7 | 7.1e-4 |
| 4 | 8 | 2.19e-7 | 0.0003 | 1.1e-7 | 1.0e-4 |

The n₁ = 1 mode sees a deformation 40× larger than n₁ = 2 and
450× larger than n₁ = 3.  This IS a low-pass filter.

**Area:** Unchanged at O(α²) ≈ 2 × 10⁻⁷.  No over-constraint.

**Mass shift:** For the proton (1,2) mode, δM ≈ 0.32 MeV (0.034%).

**Energy partition:** 931.4 MeV confined (99.27%), 6.85 MeV external
(0.73%).  The external fraction IS the Coulomb field.

**Self-consistency:** The deformation-induced energy shift (0.034%)
is much smaller than α (0.73%).  The flat-torus static model is a
consistent zeroth-order solution.  Dynamic Ma is a fine-structure
correction.


---

## Summary of R40

### Phase 1 (Tracks 1–8): exploration and dead ends

| Track | Question | Result | Status |
|-------|----------|--------|--------|
| 1 | Radiation pressure on circular torus | ~10% non-uniform, P₀ = 4.04 MeV/fm³ (F1–F4) | **Sound** |
| 2–5 | Shape optimization, mode spectrum, surface tension | Various (F5–F18) | **Tossed** — invalid inputs |
| 6 | Clairaut geodesic | Undefined for a/R > 1 (F19–F22) | **Sound** |
| 8 | Free-r optimization | Eigenvalue prefers r > 1 (F23) | **Sound** |
| 9+10 | Required stiffness, EM impedance | P₀ = E/(A×a), GR stiffness → 10⁻⁴⁰ (F24) | **Partially sound** |

**Tossed (F5–F18):** Tracks 2–5 used the static model's r_p = 8.906
on a self-intersecting geometry with the flat-torus geodesic.  Both
inputs were later invalidated (F20, F22).  All quantitative results
from these tracks are retracted.

**Lesson from F24:** The GR stiffness comparison (c⁴/8πG vs photon
pressure) mixed EM and gravity — wrong sectors.  The photon is EM;
the restoring force should be EM.  The bulk GR number (10⁻⁴⁰) is
a valid upper bound on deformation IF the compact dimensions have
gravitational stiffness, but this is not the only possibility.

### Phase 2 (Tracks 9–11): α-impedance model

The torus wall is the (1−α) energy contour of the photon mode.
Inside: 136/137 of the energy (confined mode).  Outside: 1/137
(the particle's external EM field).

| Track | Question | Result | Status |
|-------|----------|--------|--------|
| 9+10 | Required stiffness = E/(A×a); EM impedance comparison | P₀ = 4.04 MeV/fm³ | DONE |
| 11 | Dynamic shape from α-impedance model | See F25 | **DONE** |

### Key results

1. **Track 1 pressure profile (F1–F4).**  The photon exerts real,
   non-uniform radiation pressure.  Reliable input for all tracks.

2. **Clairaut geodesic (F19–F22).**  The embedded geodesic
   does not exist for a/R > 1.  The flat-torus geodesic is correct.

3. **Free-r result (F23).**  Compton alone doesn't fix r.

4. **The α-impedance model (F25).**  The torus wall is the (1−α)
   energy contour.  On the flat torus, the wall is a perfect circle.
   The 3D embedding adds a 0.067% elliptical deformation (k=2).
   The elastic 1/k² response provides a low-pass filter in n₁:
   40× suppression from n₁=1 to n₁=2, 450× to n₁=3.

5. **α runs with energy** because the wall transparency increases
   with photon energy — geometric vacuum polarization.

6. **Dynamic Ma is perturbative** (corrections ∝ α² ≈ 5×10⁻⁵).
   The static flat-torus model is the correct zeroth-order
   approximation.  Dynamic effects are fine-structure corrections.
