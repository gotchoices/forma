# R32. The running of α and the high-energy coupling

**Questions:** Q77 (α as impedance), Q18 (deriving α), Q47 (running of α)
**Type:** compute + theoretical  **Depends on:** R19, R27, R28, R31
**Status:** Active


## Motivation

R31 tried to derive α = 1/137 by looking INSIDE T⁶ (Casimir
energy, moduli stabilization) and failed — no mechanism
within the compact space selects the shear.

Q77 reframes the problem: α might not be an internal T⁶
parameter.  It might be the **impedance mismatch** between
T⁶ and R³ — a refractive index measuring how efficiently
electromagnetic energy crosses from compact to spatial
dimensions.

If α is a refractive index, it should exhibit **dispersion**:
the coupling should change with probe energy, just as the
refractive index of glass depends on wavelength.  This is
the running of α, observed experimentally:

    α(0)    ≈ 1/137.036   (Thomson limit)
    α(m_Z)  ≈ 1/127.9     (LEP measurement at 91 GeV)

In the Standard Model, the running comes from vacuum
polarization — virtual charged particles screening the bare
charge.  In the T⁶ model, the running would come from
the KK mode spectrum: each charged T⁶ mode contributes to
the screening, and the T⁶ has ~900 modes below 2 GeV (R28).

The central question: if we sum the contributions of ALL
charged T⁶ modes, does α converge to a recognizable
geometric constant at the compact scale (the high-energy
limit, often called "UV" in physics — by analogy with the
electromagnetic spectrum, where ultraviolet = short
wavelength = high energy)?  In particular, does it
converge to **1/24**, the value where gauge couplings
unify in GUT physics?


## Prior results

- **R28 Track 2**: ~29,000 raw modes, ~900 distinct below
  2 GeV.  Full mode census available.
- **R28 Track 4**: Predictive horizon at ~2 GeV (band
  spacing < 5 MeV).
- **R31 Track 3**: Casimir energy has no minimum — cannot
  select α from within T⁶.
- **R31 Track 4**: Naive KK Yukawa ruled out by 10⁵ — the
  massive KK tower couples far more weakly than the zero
  mode.
- **Q77**: α as impedance mismatch / refractive index
  hypothesis.


## Key questions

1. Does the T⁶ mode spectrum reproduce the observed running
   of α between 0 and m_Z?
2. What value does α converge to at the compact scale
   (E ~ 467 MeV, the proton ring energy)?
3. Is that value geometrically recognizable (1/24, 1/4π,
   or a lattice constant of T⁶)?
4. Does the number 24 have a natural geometric relationship
   to toroidal compactification?
5. Can the T⁶/R³ interface be modeled as an impedance
   boundary with a computable transmission coefficient?


## Approach: 4 tracks

### Track 1 — KK mode running of α  **Complete**

Enumerate all charged (Q ≠ 0) T⁶ modes and compute their
one-loop vacuum polarization contribution.

**Result:** CATASTROPHIC.  78,608 charged modes produce
running ~157,000× faster than the SM.  Landau pole at
~1 MeV.  This independently confirms R31 Track 4: ghost
modes cannot couple to the electromagnetic field at full
strength.  Suppression factor ~10⁵ required, consistent
with the Lamb shift constraint.  Findings F1–F7.


### Track 2 — Volume dilution and the high-energy coupling

Compute the T⁶ volume (excluding the neutrino sheet,
which decouples for charged-mode physics):

    V_eff = L₁ × L₂ × L₅ × L₆

The KK relationship between the effective 4D and higher-D
couplings is:

    α₄ = α_D / V_eff

Compute α_D (the "bare" coupling) and check whether it is
a recognizable constant.

Also check: does the full volume (including neutrino sheet)
give a different result, and does the decoupling of the
neutrino sheet explain the separation between
electromagnetic and weak scales?


### Track 3 — Why 24?  Geometric relationships

Investigate the number 24 in the context of torus geometry:

- **Modular properties**: The Dedekind eta function η(τ)²⁴
  governs modular invariance on tori.  The 24th power
  appears because the partition function must be invariant
  under modular transformations (τ → τ+1 and τ → −1/τ).
  Does the T⁶ partition function involve η²⁴?

- **Lattice kissing number**: In 4D, the kissing number
  (maximum number of non-overlapping unit spheres touching
  a central sphere) is 24, realized by the D₄ root lattice.
  Does the T⁶ lattice have D₄ structure?

- **Euler characteristic**: χ(K3) = 24 for the K3 surface
  (simplest Calabi-Yau 4-fold).  Is there a connection
  between T⁶ and K3?

- **Combinatorial**: 24 = 4! = permutations of the 4 non-
  compact dimensions (R³ × R¹).  Is α related to a
  symmetry factor from the non-compact sector?

- **Refraction geometry**: A field refracting off a toroidal
  surface encounters a geometry that varies with position.
  The tube has curvature 1/a, the ring has curvature 1/R.
  The total solid angle subtended, or the integrated
  Gaussian curvature, or the number of independent
  refraction directions — could any of these produce 24?

**Output**: Catalog of geometric appearances of 24 in
torus-related mathematics.  Assessment of which (if any)
connect naturally to the T⁶ lattice.


### Track 4 — Impedance at the T⁶/R³ interface

Model the T⁶/R³ coupling as an impedance boundary.  A
photon (or more precisely, a gauge field fluctuation) in
R³ encounters the compact space.  The compact space has
a different effective impedance because:

- The metric is different (sheared, periodic)
- The mode density is discrete (not continuous)
- The boundary conditions are periodic (not open)

The transmission coefficient at a waveguide-to-free-space
junction is well-known in microwave engineering.  A
toroidal cavity radiating into free space has a quality
factor Q and a radiation resistance R_rad.  The coupling
efficiency is:

    η = R_rad / (R_rad + R_loss)

Compute R_rad for the electron T² (a toroidal cavity with
known dimensions) radiating into R³.  Does the coupling
efficiency equal α?

Alternative approach: the Fresnel equations give the
reflection/transmission at an interface between media
with different wave speeds.  If c_T⁶ ≠ c_R³, the
transmission coefficient T depends on the ratio.  Solve
T = α for c_T⁶/c_R³ and check if the ratio is
geometrically meaningful.

**Output**: Numerical coupling efficiency from waveguide/
cavity QED calculation.  Comparison to α = 1/137.


## What success looks like

- **Strong result**: Track 1 reproduces α(m_Z) ≈ 1/128
  from the T⁶ mode spectrum, AND α converges to 1/24 at
  the compact scale, AND Track 3 identifies WHY 24 appears
  in torus geometry.  This would connect T⁶ to GUT
  unification and provide a geometric origin for the
  running.

- **Moderate result**: Track 1 gives a sensible running
  (monotonically increasing α with energy) but the UV
  value is not 1/24.  The UV value might still be a
  recognizable geometric constant, providing a new
  constraint.

- **Null result**: The running is pathological (wrong
  sign, divergent, or unreasonably fast) — which would
  mean the ghost modes don't contribute to vacuum
  polarization as assumed, constraining their physical
  status.

- **Track 4 payoff**: If the impedance calculation
  independently produces α = 1/137 from the T² geometry,
  this would be the derivation of α we've been looking
  for — not from within T⁶, but from the T⁶/R³ interface.
