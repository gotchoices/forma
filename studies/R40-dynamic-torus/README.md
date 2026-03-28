# R40. Self-consistent dynamic torus — shape from force balance

**Status:** COMPLETE — Dynamic Ma deformation negligible (F24); flat torus vindicated
**Depends on:** R17 (radiation pressure), R18 (torus stiffness),
  R19 (shear-charge / α formula), R33 (ghost modes), R37 (membrane mechanics)
**Motivates:** Q90 (ephemeral mode decomposition / dynamic torus),
  Q77 (ghost selection), Q34 (α derivation), Q86 (three generations)


## Premise: Dynamic Ma

**This study departs from the flat-torus Ma used in R26–R39.**

Studies R1–R39 treat each material sheet as an intrinsically flat
torus T² with metric G̃.  Modes are plane waves exp(i n·θ), and the
3D embedding is a visualization tool, not the physics.

This study takes the opposite view: **the 3D embedding IS the
physics.**  The torus is a real surface in 3D space, shaped by the
balance between two forces:

1. **Outward:** the photon circulating on the geodesic exerts
   radiation pressure against the tube wall (centrifugal force from
   the curved 3D path).
2. **Inward:** the rigidity of the compact spatial dimension pushes
   back — likely with both a normal component (resistance to
   stretching) and a surface tension component (resistance to
   bending).

The photon's pressure is non-uniform around the tube.  If space is
rigid but finite, the surface deforms until a balance is reached.
**The equilibrium shape is not a perfect torus** — it is a warped
surface of revolution whose cross-section depends on the mode.

This is the "containment force" that Williamson and van der Mark
identified as necessary but could not specify.  The premise is:
energy bends spacetime (GR), so energy bends MaSt too.  The mode's
energy density creates a non-uniform stress on the compact geometry,
and the geometry responds.

### What this changes

- The mode and the geometry are **mutually determined** — a nonlinear
  eigenvalue problem.  The shape depends on the mode, and the mode
  depends on the shape.
- The geodesic on the deformed surface differs from the flat-torus
  geodesic.  The path, the mode energy, and the charge integral all
  shift.
- Different modes deform the surface differently.  Each particle
  lives on its own self-consistent shape.
- The deformation may act as a **band filter**, suppressing modes
  whose pressure patterns are incompatible with the equilibrium
  (ghost suppression).


## Question

Given a (1,2) photon mode on an embedded torus:
1. What is the radiation pressure profile on the tube wall?
2. What cross-section shape balances it?
3. Which other modes can live on this shape?
4. Does the shape flexibility act as a low-pass (or band) filter
   on the mode spectrum?


## Why this matters

1. **Ghost suppression.**  The flat torus supports ~14,000 charged
   modes below 10 GeV (R33, R38).  Nature shows ~40 particles.  A
   self-consistent dynamic torus may act as a geometric filter: only
   modes whose pressure pattern admits a stable equilibrium shape can
   persist.  Higher harmonics may create pressure patterns that no
   shape can balance.

2. **α from geometry.**  R15, R31, R32 all failed to derive α — the
   flat-torus formula α(r, s) has a free parameter r.  The self-
   consistent shape might select a specific r (and therefore α),
   because only one shape simultaneously supports the mode and
   balances the forces.

3. **Ephemeral particles (Q90).**  Surface deformations that don't
   match a stable eigenmode are transient.  Their lifetimes depend on
   how far they are from equilibrium.  This could explain particle
   lifetimes and potentially produce ephemeral quark-like sub-modes.

4. **The moduli potential.**  R31 and R37 both identified the vacuum
   energy as a function of shape as the critical unknown blocking
   progress.  This study computes it directly.

5. **Cross-sheet filtering (future study).**  The three material
   sheets (Ma_e, Ma_ν, Ma_p) are coupled by cross-shears (σ_ep,
   σ_eν, σ_νp).  Shape deformations on one sheet could leak to
   another.  Low-frequency components on the electron sheet might
   drain into the neutrino sheet (which has larger circumferences
   and lower mode energies).  High-frequency components might leak
   upward to the proton sheet, producing phase shifts.  This
   cross-sheet filtering is a separate mechanism from the within-
   sheet band filter studied here, but could combine with it to
   further constrain the physical mode spectrum.  See Q87, Q89.


## Caveats

**Self-intersection.**  The proton sheet has a/R = 8.906.  The 3D
embedding self-intersects: the tube passes through itself at the
inner equator (ρ = R + a cos θ₁ < 0 for most θ₁).  The surface
normal, outward pressure, and cross-section deformation are all
ill-defined in the self-intersection zone.  Tracks 1–5 handle this
by using |ρ|, which is mathematically stable but geometrically
questionable.  Results should be validated on a non-self-intersecting
torus (r ~ 2–5, the electron sheet range).

**Geodesic approximation.**  Tracks 1–5 use the flat-torus geodesic
(θ₁ = n₁t, θ₂ = n₂t) on the deformed surface.  On a deformed
surface of revolution, the actual geodesic follows Clairaut's
relation and is a different path.  Track 6 should correct this.


## Approach

### No assumed rigidity model

Previous studies (R17, R18, R37) assumed specific restoring mechanisms
(centrifugal balance, elastic constants, membrane tension).  This study
does NOT assume a restoring model.  Instead:

1. Compute the outward radiation pressure P_rad(θ₁) from the mode.
2. The equilibrium condition is simply P_in(θ₁) = P_rad(θ₁).
3. Whatever P_in turns out to be, that's the data.  We examine it
   for structure: is it uniform?  Does it look like curvature
   (surface tension)?  Like a gradient (elastic)?  Like something
   else entirely?

The restoring force is an OUTPUT of the calculation, not an input.

### The self-consistent iteration

Even without assuming P_in, we can find the self-consistent shape
by requiring that the total energy (mode + surface) is stationary:

1. **Parameterize** the cross-section as a Fourier series:

       r(θ₁) = a₀ + Σₖ aₖ cos(kθ₁)

   Circular cross-section: a₀ = a (minor radius), all others zero.

2. **Constraint:** Fix the total path length of the geodesic
   to λ_C (the Compton wavelength).  This is the photon confinement
   condition — the energy is fixed.

3. **Solve the wave equation** on the current surface for the (n₁,n₂)
   mode.  Sturm-Liouville in θ₁ with the metric factor from the
   parameterized surface (R21 Track 1 already solved this for
   the embedded torus).

4. **Compute the radiation pressure** at each θ₁ from the mode's
   energy density — centrifugal force from the photon's curved
   3D path, projected onto the surface normal.

5. **Find the equilibrium shape** by minimizing the mode energy
   over the Fourier coefficients, subject to the path-length
   constraint.

6. **Read off P_in** from the converged shape:  P_in(θ₁) = P_rad(θ₁)
   at equilibrium.  Examine its structure.


## Tracks

### Track 1. Outward pressure profile on a circular torus [DONE]

Compute P_rad(θ₁) on the standard circular cross-section.
Script: `scripts/track1_pressure_profile.py`

**Result:** Pressure is highly non-uniform.  Dominated by k=2
(elliptical) harmonic.  The circular torus is not in force balance
(F2).  See findings.md F1–F4.

### Track 2. Self-consistent shape (energy minimization) [DONE]

Find the cross-section that minimizes mode energy for the (1,2)
mode, subject to path-length constraint.
Script: `scripts/track2_self_consistent_shape.py`

**Result:** Equilibrium is a 4-lobed (a₂-dominated) shape with
14.5% lower energy than the circular torus (F5, F6).

**Known issue:** Uses the flat-torus geodesic on the deformed
surface.  The actual geodesic on a surface of revolution follows
Clairaut's relation and is a different path.  Track 6 should fix
this.  The 14.5% energy shift may change.

### Track 3. Mode spectrum on the self-consistent shape [DONE]

Which modes can live on the (1,2)-optimized shape?
Script: `scripts/track3_mode_spectrum.py`

**Result:** Most modes are energetically lowered.  A bandpass
filter on n₂ (ring winding) is observed: modes with n₂ ≈ 2
benefit most, high-n₂ modes are penalized.  The (1,2) shape
acts as a band filter, not a simple low-pass (F10–F14).

### Track 4. Per-mode optimal shapes [DONE]

Each mode optimized independently — does every mode want the
same shape, or different shapes?
Script: `scripts/track4_per_mode_shapes.py`

**Result:** Different modes want dramatically different shapes
(F13).  Ghost suppression works through shape incompatibility:
the (1,2) mode's equilibrium shape penalizes high-n₂ modes.
Shape competition creates barriers between distinct particle
configurations (F15).

### Track 5. Surface tension as restoring model [DONE]

Test whether surface tension can provide the restoring force.
Script: `scripts/track5_surface_tension.py`

**Result:** Surface tension is not a consistent restoring model —
the tension needed is inconsistent across harmonics (F16).
However, a tension-like term does suppress high-k deformations,
making shapes smoother (F17).

### Track 6. Clairaut geodesic on embedded torus [DONE]

Compute the true geodesic (Clairaut's relation) on the embedded
surface and compare to the flat-torus approximation.
Script: `scripts/track6_clairaut_geodesic.py`

**Result:** For non-self-intersecting tori (a/R < 1), the embedded
geodesic is 34–58% shorter than the flat-torus path (F19).  Shape
optimization naturally reduces this discrepancy to 3–6% (F21).
For self-intersecting tori (a/R > 1), the Clairaut geodesic does
not exist — ρ passes through zero, creating a metric singularity
that blocks all (n₂ ≠ 0) closed geodesics (F20).

**Critical implication:** All known MaSt particles have a/R > 1.
The "3D embedding = physics" premise breaks down for all of them
(F22).

### Track 7. Non-self-intersecting control [SUPERSEDED]

Originally planned to run Tracks 1–2 on a non-self-intersecting
torus (r ~ 2–5).  Track 6's analysis of the Clairaut geodesic
across all r values, and Track 8's free-r sweep, cover this ground
more thoroughly.

### Track 8. Free-r optimization [DONE]

Treat the aspect ratio r = a/R as a free parameter (not imported
from the static model) and sweep across r to find the embedded
eigenvalue minimum.
Script: `scripts/track8_free_r_optimization.py`

**Result:** The Compton constraint alone does not determine r (F23).
The eigenvalue minimum falls at r ≈ 5 (self-intersecting), and with
shape optimization remains in the r > 1 regime.  A second constraint
(restoring force, α condition, or cross-sheet coupling) is needed
to pin r.

### Closing analysis: Einstein stiffness [in findings.md, F24]

Computed the ratio of the photon's radiation pressure to the
restoring pressure implied by GR's spatial stiffness c⁴/(8πG).
The photon is 10⁴⁰ times too weak to deform the torus.  Dynamic
Ma deformation is negligible.


## Outcome

The radiation pressure is non-uniform (26%), but the spatial
stiffness makes the resulting deformation ~10⁻⁴⁰ of the tube
radius.  The flat-torus model used in R1–R39 is vindicated: the
mode is a perturbation on a rigid geometric background.

Ghost suppression via shape deformation does not work.  Alternative
mechanisms to investigate: coupling form factors (R33), cavity
Q-factors (R38), moduli potentials (R37), cross-sheet filtering.


## Tools

- **Sturm-Liouville solver** for ψ(θ₁) on a surface of revolution
  with arbitrary cross-section.  Extended from R21 Track 1.
- **lib/embedded.py** — torus geometry.
- **lib/ma_model.py** — flat-torus spectrum for comparison.
- **SciPy minimize** — shape optimization with constraints.
- **R17 Track 4** — centrifugal force decomposition.
