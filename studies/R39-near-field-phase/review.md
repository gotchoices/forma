# R39 Review

Scripts executed and output verified 2026-03-28.  All three scripts
run cleanly on the current lib (ma_model.py, embedded.py).  Results
are numerically reproducible.

---

## What's correct

**F2 (phase symmetry) is the most important result and is mathematically
rigorous.**  For a (1,2) geodesic, t → t+π maps θ₁ → θ₁+π and
θ₂ → θ₂+2π ≡ θ₂.  The curve maps to itself.  Therefore U(d, Δφ) =
U(d, Δφ+π) exactly.  This kills the Q88 "anti-phase cancellation"
hypothesis for the electron and proton (both are (1,2) modes).
The numerical confirmation (max error ~10⁻¹⁶) validates the code.

**F3 (geometric suppression) is real and well-computed.**  At d < a,
the charge distributions interpenetrate.  The concavity of 1/r
guarantees that the distributed-charge interaction is less than the
point-charge value.  The 74% suppression at 1 fm and 55% at 2 fm
are physically reasonable for a charge extent of ±3.7 fm.

**F7 (no attraction) follows from the suppression picture.**
Distributing positive charge over a volume reduces repulsion but
cannot create attraction.  The code confirms this numerically.

**The choice to use the proton sheet rather than the electron sheet
was correct.**  The README framing (Tracks 1-3 for electron, Track 4
for proton) predates the understanding that r_e is free.  The proton
sheet gives a parameter-free result (r_p = 8.906 is pinned).  Any
electron-sheet computation would depend on the assumed r_e.  The
findings should note this explicitly — the electron sheet was skipped
because it requires a free parameter, not because it's uninteresting.

---

## Issues found

### 1. Separation direction not explored

All sweeps separate along z (axis=2, the default).  For a torus
centered at the origin with the ring in the xy-plane, z is the tube
axis.  The proton torus has a/R = 8.9 (highly oblate in ring
coordinates), so the charge distribution is NOT spherically symmetric.
The suppression factor will differ depending on whether the second
proton approaches along z vs along x (radial in the ring plane).

At minimum, the findings should state that results are for z-axis
separation.  Ideally, Track 2 should include a comparison sweep along
x to quantify the directional dependence.  If the variation is small
(<10%), it's a footnote.  If large, it's a finding.

### 2. Self-intersecting torus acknowledged but not assessed

The proton torus has a/R = 8.9, meaning it folds through itself.  The
3D Cartesian embedding used by embedded.py places charge segments at
positions that include the self-intersection zone (the inner part of
the torus where R + a cos θ₁ < 0).  These segments have physically
meaningless 3D positions — they're "inside out."

This doesn't cause numerical errors (the Coulomb sum handles any
positions), but it means the geometric suppression factors (F3) are
artifacts of a self-intersecting embedding, not of a physical torus.

The findings flag this as Open Question 3 but present the suppression
numbers (F3) without caveat.  The suppression numbers should carry a
note: "computed on the 3D embedding including self-intersection;
the physical torus may not self-intersect."

### 3. The d⁻² power law (F6) is probably an artifact

The expected quadrupole falloff is d⁻⁵ (for energy, from a d⁻³
potential correction).  The observed d⁻² is anomalously slow.  The
findings attribute this to poor multipole convergence at a/R = 8.9.
This is plausible — the multipole expansion requires d >> charge
extent, and d > 5a = 19 fm barely satisfies this.

But the more likely explanation is the self-intersection.  A
self-intersecting torus is NOT well-approximated by a multipole
expansion at any distance, because the "charge radius" is not
well-defined (the charge distribution wraps through the origin).  The
d⁻² slope may simply be a non-convergent regime of the expansion.

The findings should downgrade F6 from a measured power law to "the
multipole expansion has not converged in this regime."

### 4. Findings accurately reflect script output

I verified each finding against the actual script output:

| Finding | Claimed | Computed | Match? |
|---------|---------|----------|--------|
| F1 monopole q₀₀ | 0.282 | 0.2821 | Yes |
| F1 dipole | ~10⁻¹⁶ | 1.3e-16 to 6.3e-16 | Yes |
| F1 quadrupole eigenvalues | 3.4, 10.0, 13.4 | 3.404, 9.953, 13.358 | Yes |
| F2 symmetry | U(Δφ) = U(Δφ+π) | max err 2.2e-16 | Yes |
| F3 suppression at 1 fm | 74% | 73.9% | Yes |
| F3 suppression at 2 fm | 55% | 55.1% | Yes |
| F3 suppression at 3 fm | 36% | 35.6% | Yes |
| F5 crossover | 5.5 fm | 5.48 fm | Yes |
| F5 peak overshoot | 1.23 at 7.4 fm | 1.229 at 7.45 fm | Yes |
| F6 power law | d⁻² | d⁻²·⁰² | Yes |
| F7 no attraction | all U > 0 | confirmed | Yes |

All numbers match.  No misinterpretation of script output.

### 5. Missing: electron sheet justification

The README says "Track 4: Repeat Tracks 1-3 for the proton sheet
instead of the electron sheet."  The scripts only compute the proton
sheet.  The findings don't explain why.  Add a note to the findings:

> The electron sheet was not computed because r_e is a free parameter
> (R30 F11).  Any electron result would depend on the assumed r_e.
> The proton sheet (r_p = 8.906, pinned by R27 F18) gives the only
> parameter-free near-field computation.

### 6. Minor: findings quote |A₁|/A₀ at d=2 fm as 3.6%

The Track 3 output shows |A₁|/A₀ = 0.0349 at d/a = 0.68 (d ≈ 2.5 fm),
not exactly at d = 2.0 fm.  The findings table says 3.6% at d = 2.0.
This is interpolated, not directly from a sampled point.  Not wrong,
but the table should note the values are from the nearest sampled
distance.

---

## Summary

The study is correctly executed.  The scripts use the library properly,
the numerics are clean, and the findings accurately reflect the
computed output.  The two main results (π-periodicity killing the
anti-phase hypothesis, and geometric suppression at nuclear scales)
are solid.

The primary caveat is the self-intersecting torus geometry (a/R = 8.9),
which makes the 3D embedding unphysical and the multipole expansion
unreliable.  The suppression numbers are real within the embedding
model but should carry this caveat.  A future study could explore
intrinsic flat-torus distances as an alternative to 3D embedding.
