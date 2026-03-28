# R40. Self-consistent dynamic torus — shape from force balance

**Status:** Active — framing
**Depends on:** R17 (radiation pressure), R18 (torus stiffness),
  R19 (shear-charge / α formula), R33 (ghost modes), R37 (membrane mechanics)
**Motivates:** Q90 (ephemeral mode decomposition / dynamic torus),
  Q77 (ghost selection), Q34 (α derivation), Q86 (three generations)


## Question

All Ma studies model the material sheet as a perfect torus — circular
cross-section, uniform geometry.  The photon mode is computed on this
fixed shape.  But the confined photon exerts radiation pressure outward
on the surface, and something must push back.

Don't assume what the restoring force is.  Just compute the outward
radiation pressure from the (1,2) mode at each surface element, then
ask: **what inward pressure profile would balance it?**  Whatever that
profile is, it defines the physics of the confining medium.

If the required inward pressure is non-uniform (it will be, because
the mode amplitude is non-uniform), then either:
- The surface deforms until the balance is restored (dynamic torus), or
- The confining medium supplies a non-uniform restoring force (rigid
  but shaped space)

Either way, the result is a non-circular cross-section.  The shape and
the mode must be self-consistent.


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

       r(θ₁) = a₀ + Σₖ aₖ cos(kθ₁) + bₖ sin(kθ₁)

   Circular cross-section: a₀ = a (minor radius), all others zero.
   Truncate at k_max = 8 (~16 shape parameters).

2. **Constraint:** Fix the total path length of the (1,2) geodesic
   to λ_C (the Compton wavelength).  This is the photon confinement
   condition — the energy is fixed.

3. **Solve the wave equation** on the current surface for the (1,2)
   mode.  Sturm-Liouville in θ₁ with the metric factor from the
   parameterized surface (R21 Track 1 already solved this for
   the embedded torus).

4. **Compute the radiation pressure** at each θ₁ from the mode's
   energy density:

       P_rad(θ₁) ∝ |ψ(θ₁)|² × (local curvature correction)

   R17 Track 4 computed the force decomposition — the centrifugal
   force from the photon's curved 3D path.  Extend this to the
   general surface.

5. **Find the equilibrium shape** by minimizing the total energy
   over the Fourier coefficients, subject to the path-length
   constraint.  The shape that minimizes energy is the one where
   the mode sits most comfortably — i.e., where the pressure is
   most uniformly distributed.

6. **Read off P_in** from the converged shape:  P_in(θ₁) = P_rad(θ₁)
   at equilibrium.  Examine its structure.


## Tracks

### Track 1. Outward pressure profile on a circular torus

Before deforming anything, compute P_rad(θ₁) on the standard circular
cross-section.  This is the baseline — how non-uniform is the pressure
even before the shape responds?

**Method:**
1. Build the (1,2) mode on the proton-sheet torus (r_p = 8.906,
   geometry from R27).
2. Solve the Sturm-Liouville eigenvalue problem for ψ(θ₁) on the
   embedded torus (as in R21 Track 1).
3. Compute |ψ(θ₁)|² — the energy density vs tube angle.
4. Compute the outward radiation pressure at each θ₁:
   - Centrifugal: P_cent = E × κ_normal (curvature of the 3D path
     projected onto the surface normal).  R17 Track 4 computed this.
   - Electromagnetic: P_EM = ε₀ E² / 2 (Maxwell stress).
5. Plot P_rad(θ₁).  Decompose into Fourier modes.

**Deliverables:**
- P_rad(θ₁) profile on the undeformed torus
- Fourier spectrum of the pressure (which harmonics dominate?)
- Ratio of pressure variation to mean pressure (how non-uniform?)
- The inward pressure profile P_in(θ₁) that would be needed to
  hold this shape in equilibrium

**Key question answered:** How far from uniform is the force balance
on the circular torus?  If the pressure is nearly uniform, the
circular shape is nearly self-consistent and deformation is small.
If the pressure has large harmonics, the torus must deform
significantly.


### Track 2. Self-consistent shape (energy minimization)

Find the cross-section that minimizes total energy subject to the
path-length constraint.

**Method:**
1. Parameterize cross-section: Fourier coefficients a₀, a₁...a₈,
   b₁...b₈ (~17 parameters).
2. For each shape candidate:
   a. Build the surface of revolution.
   b. Compute the (1,2) geodesic path length on this surface.
   c. Scale the surface so path length = λ_C (Compton constraint).
   d. Solve the Sturm-Liouville problem for the (1,2) mode.
   e. Compute the mode energy (eigenvalue).
3. Minimize the mode energy over the shape parameters.
   (The shape that minimizes mode energy is the one where the
   photon is most stable — lowest radiation pressure, best balance.)
4. Use SciPy minimize with the Compton constraint enforced via
   a Lagrange multiplier or penalty term.

**Deliverables:**
- The self-consistent cross-section shape (Fourier coefficients)
- Visualization: overlay the deformed cross-section on the circle
- How much does the mode energy shift from the circular-torus value?
- The equilibrium P_in(θ₁) profile — what does it look like?
- Does a specific aspect ratio r emerge from the minimization?

**This is the core computation of the study.**


### Track 3. Mode spectrum on the self-consistent shape

Which modes can live on the deformed torus?

**Method:**
1. Take the converged shape from Track 2.
2. Solve the wave equation for modes (n₁, n₂) with n₁ = 0..6,
   n₂ = 0..6.
3. For each mode, compute the radiation pressure profile on the
   Track 2 shape.
4. Check: is the mode's pressure profile compatible with the Track 2
   shape?  (A mode is "compatible" if its pressure profile is close
   to the equilibrium P_in from Track 2.  A mode is "incompatible"
   if its pressure profile would require a very different shape.)
5. Compare to the flat-torus spectrum.

**Deliverables:**
- Mode energies: flat torus vs self-consistent shape
- Compatibility score for each mode (how well does its pressure
  match the equilibrium shape?)
- Ghost filter: how many charged modes are compatible vs incompatible?
- Whether the (1,1) spin-1 mode is stabilized or destabilized


### Track 4. Physical consequences

**Deliverables:**
- Does the self-consistent shape select r_e?  (Currently free.)
- Does the equilibrium α differ from the flat-torus α(r, s)?
- What is the moduli potential E(shape parameters)?
- Is there a natural Q-factor (bandwidth) for the cavity?
- What does P_in(θ₁) tell us about the physics of the confining
  medium?  Does it match any known model (surface tension, elastic,
  gravitational)?


## What we learn either way

**If the pressure is nearly uniform on the circular torus (Track 1):**
- The circular shape is already near equilibrium
- Deformation is perturbative — Track 2 gives small corrections
- The flat-torus approximation is validated for existing studies
- Ghost suppression must come from elsewhere

**If the pressure is highly non-uniform:**
- The torus must deform significantly to reach equilibrium
- Track 2 gives a qualitatively different shape
- Mode spectrum changes (Track 3) — potential ghost filter
- The form of P_in(θ₁) reveals new physics about the confining medium
- Ephemeral particles become plausible (Q90)


## Computational cost

- Track 1: seconds (one eigenvalue solve + force decomposition)
- Track 2: minutes (optimization over ~17 parameters, each step
  is one eigenvalue solve)
- Track 3: minutes (~36 eigenvalue solves on a fixed shape)
- Track 4: analysis

Total: well under an hour.


## Tools

- **Sturm-Liouville solver** for ψ(θ₁) on a surface of revolution
  with arbitrary cross-section.  Extend R21 Track 1's solver.
- **lib/embedded.py** — torus geometry (extend for non-circular
  cross-sections if needed).
- **lib/ma_model.py** — flat-torus spectrum for comparison.
- **SciPy minimize** — shape optimization with constraints.
- **R17 Track 4** — centrifugal force decomposition (adapt to
  general surface).
