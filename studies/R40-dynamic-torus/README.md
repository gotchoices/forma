# R40. Self-consistent dynamic torus — shape from force balance

**Status:** COMPLETE (Phase 2)
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

### Phase 1: Exploratory (Tracks 1–8)

Phase 1 established the radiation pressure profile, explored shape
optimization, and tested two stiffness models (surface tension,
Einstein bulk stiffness).  **Track 1 is reliable.  Tracks 2–5
used invalid inputs** (static model's r_p on a self-intersecting
geometry with flat-torus geodesic) — qualitative insights only.
Tracks 6 and 8 are reliable independent analyses.

Phase 1 ended with F24: bulk stiffness c⁴/(8πG) gives 10⁻⁴⁰
deformation.  But this compared EM radiation pressure against
gravitational stiffness — mixing two different sectors.  The
photon is an EM phenomenon; the restoring force should be EM too.

| Track | Question | Status | Reliable? |
|-------|----------|--------|-----------|
| 1 | Radiation pressure profile | DONE | Yes |
| 2 | Energy-minimizing shape | DONE | No — invalid inputs |
| 3 | Mode spectrum on (1,2) shape | DONE | No — built on Track 2 |
| 4 | Per-mode optimal shapes | DONE | No — built on Track 2 |
| 5 | Surface tension as restoring model | DONE | No — built on Track 2 |
| 6 | Clairaut geodesic | DONE | Yes |
| 7 | Non-self-intersecting control | SUPERSEDED | — |
| 8 | Free-r optimization | DONE | Yes |

Detailed results: see findings.md F1–F24.


### Phase 2: α-impedance model (Tracks 9–11)

Phase 1's F24 compared EM radiation pressure against gravitational
stiffness c⁴/(8πG) — mixing two different sectors.  Phase 2
replaced the gravitational restoring force with an EM model.

#### Track 9+10. Required stiffness and EM impedance [DONE]

Computed the mean radiation pressure P₀ = 4.04 MeV/fm³ in
physical units.  Found P₀ = E/(A×a) (a geometric identity).
Compared against EM impedance constants μ₀, ε₀.  Conclusion:
μ₀ and ε₀ are conversion factors, not independent restoring
forces.  The required fields (~9000× Schwinger) are in the
deep non-perturbative QED regime.

#### Track 11. α-impedance shape [DONE]

The torus wall is the (1−α) energy contour of the photon mode.
Inside the wall: 136/137 of the energy (confined mode).
Outside: 1/137 (the particle's external EM field).

Results:
- On the flat torus (intrinsic geometry), the contour is a
  perfect circle.  No deformation.
- The 3D embedding introduces a k=2 (elliptical) deformation
  at δr/a = 6.7 × 10⁻⁴ (0.067%).
- The elastic 1/k² wall response provides a **low-pass filter**
  in tube winding number n₁: 40× suppression from n₁=1 to
  n₁=2, 450× to n₁=3.
- Mass shift for proton: δM ≈ 0.32 MeV (0.034%).
- Area unchanged at O(α²) ≈ 2 × 10⁻⁷.
- α runs with energy because wall transparency increases —
  geometric realization of vacuum polarization.
- **r is still free** (F26): the equilibrium determines
  V_compact from r, not the reverse.  All key results
  (low-pass filter, α interpretation, running of α) hold
  regardless of r.  See Q91 for the open problem of
  deriving V_compact independently.


## Tools

- **Sturm-Liouville solver** for ψ(θ₁) on a surface of revolution
  with arbitrary cross-section.  Extended from R21 Track 1.
- **lib/embedded.py** — torus geometry.
- **lib/ma_model.py** — flat-torus spectrum for comparison.
- **SciPy minimize** — shape optimization with constraints.
- **R17 Track 4** — centrifugal force decomposition.
