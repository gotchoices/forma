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


### Track 2 — Volume dilution and the high-energy coupling  **Complete**

Compute the T⁶ sheet areas and KK volume dilution.

**Result:** The "bare" coupling α_bare = α × r × μ₁₂²
gives 1/α_bare ≈ 5.1 (electron sheet) and 3.8 (proton
sheet).  NOT 1/24.  The two sheets give different bare
couplings because they have different aspect ratios.
The neutrino sheet volume ratio does NOT explain weak
interaction strength (off by 11 orders of magnitude).
Findings F8–F12.


### Track 3 — Why 24?  Geometric relationships  **Complete**

Survey all known mathematical contexts where 24 appears
and assess connection to T⁶.

**Result:** Cataloged 8 contexts.  The Dedekind eta
function η(τ)²⁴ is the strongest candidate: it is the
unique modular-invariant cusp form, and modular
invariance of the T² partition function forces it to
appear.  However, the naive T⁶ scalar partition function
contains |η|⁶ (not |η|²⁴), and no combination of the
model's aspect ratios produces 24.  The most promising
path: compute the gauge coupling normalization from the
modular-invariant partition function and check for 1/24.
Findings F13–F17.


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
