# R34. The midpoint coupling — bidirectional modulation of α

**Status:** Framed  
**Questions:** Q77 (α as impedance), Q18 (deriving α)  
**Type:** compute + theoretical  
**Depends on:** R19 (shear-charge), R31 (alpha derivation),
R32 (alpha running)


## Motivation

R32 Track 4 found that the weighted gauge field partition
(weighting each KK dimension by 1/L²) gives an EM coupling
fraction of 1/80.  This is the arithmetic mean of 1/137
(the observed low-energy α) and 1/24 (the hypothesized
high-energy α) to 99.8% accuracy:

    (137 + 24) / 2 = 80.5

The modulation is exactly symmetric:

    1/α(E) = 80.5 ± 56.5

with +56.5 at low energy (→ 137) and −56.5 at high energy
(→ 24).  This suggests a BIDIRECTIONAL modulation of a base
coupling, analogous to a dispersive refractive index near a
resonance.

In optics, a Kramers-Kronig dispersion curve near a resonance
has exactly this shape:

    n(ω) = n₀ + δn × cos(φ(ω))

Below resonance (φ → 0): n > n₀ (normal dispersion, coupling
weaker, 1/α large).  Above resonance (φ → π): n < n₀
(anomalous dispersion, coupling stronger, 1/α small).

If α is the refractive index of the T²/R³ interface (Q77),
then the T² modes are the absorption resonances, and the
dispersion of α with energy follows from Kramers-Kronig
relations — a bidirectional modulation from a geometric base.

Meanwhile, the shear s that determines α is currently NOT
independently determined — it is reverse-engineered from
α = 1/137 via `solve_shear_for_alpha(r)`.  The α formula
is a tautology until s can be derived from geometry.  This
study tests whether the shear can be backed into from the
midpoint coupling 1/80.


## Prior results

- **R19 F35–F43**: α = r²μ sin²(2πs) / (4π(2−s)²).
  The shear s controls α, but s is a free parameter.
- **R31 F7, F23**: No kinematic mechanism selects s.
  Dynamics (variational principle) needed.
- **R32 F18**: 24 gauge field components = 3 sheets × 8
  per sheet (4 non-compact × 2 compact).
- **R32 F19**: The 4π in the formula IS the 3D solid angle.
- **R32 F23**: Weighted gauge partition (by 1/L²) gives
  1/80, matching (137+24)/2 to 99.8%.
- **R32 F14**: The Dedekind η²⁴ is forced by modular
  invariance on any torus.
- **Q77**: α as an impedance mismatch / refractive index
  between T⁶ and R³.


## Key questions

1. Is 1/80 the geometric base coupling, with energy-dependent
   modulation in both directions?  Or is it a coincidence?
2. Can Kramers-Kronig dispersive running, using T⁶ modes
   as resonances, reproduce 1/α from 137 (IR) to 24 (UV)?
3. What energy scale is the "resonance" where φ = π/2 and
   1/α = 80?  Does it correspond to a T² geometric scale?
4. Can the shear s be derived from the base coupling 1/80
   instead of from the observed α = 1/137?
5. What is the second mechanism?  The shear provides ONE
   modulation direction.  What provides the other?


## Tracks


### Track 1 — Kramers-Kronig dispersive model

Model the T² mode spectrum as a set of absorption
resonances.  The refractive index (= coupling) follows:

    1/α(E) = 1/α₀ + (2/π) P∫ E'σ(E')/(E'² − E²) dE'

where σ(E') is the absorption cross-section at each mode
energy and α₀ = 1/80.5 is the base coupling.

For each T⁶ mode at energy E_k with oscillator strength f_k:
- Known particles (e, p, n, etc.): f_k = 1
- Ghost modes: f_k = 10⁻⁵ (suppressed)

Compute the dispersive integral and check:
- Does 1/α(0) → 137?  (IR screening)
- Does 1/α(∞) → 24?  (UV anti-screening)
- What energy gives 1/α = 80?  (resonance)

The sign structure is critical: Kramers-Kronig guarantees
that IF there is absorption (ghost modes absorb energy at
their resonant frequencies), the refractive index is
enhanced below the resonance and reduced above it.  This
is exactly the bidirectional modulation.


### Track 2 — The resonance scale

In standard QFT running, 1/α = 80 requires ~10³⁰ GeV —
unreachable.  So the "midpoint" is not a running value
but a geometric one.  What T⁶ scale corresponds to the
crossover?

Candidates:
- Proton ring energy: 467 MeV (strongest gauge field)
- Proton sheet geometric mean: 156 MeV
- Electron sheet geometric mean: 0.1 MeV
- Some function of circumference ratios

Compute φ(E) = π × f(E/E_resonance) for various
resonance scales and check which one gives the right
running shape (1/α going from 137 to 24 over the right
energy range).

Also check: does the "resonance" correspond to the
energy where the probing wavelength equals a T²
circumference?  At E = ℏc/L₆ ≈ 467 MeV (proton ring),
a probe fits exactly one wavelength around the ring.
Below this: the compact space is "invisible" (long-
wavelength limit).  Above this: the probe resolves the
internal structure.  The transition region is where the
dispersion occurs.


### Track 3 — Backing into the shear

The α formula α = r²μ sin²(2πs) / (4π(2−s)²) currently
uses s solved from α = 1/137.  Instead:

**Approach A**: Set the base coupling to 1/80 and solve
for s.  What shear gives α₀ = 1/80?  Is that shear
geometrically natural (e.g., related to 1/r, 1/2π, or
a modular invariant)?

**Approach B**: Set the denominator to 24 instead of
4π(2−s)².  What does this imply?  The 24 could be the
number of gauge field components (= 4 × 6), replacing
the 3D-specific 4π normalization with the full 10D
metric channel count.  Solve for the required numerator.

**Approach C**: Decompose α into two factors:
    α = α_base × modulation(E)
    1/α_base = 80.5
    modulation(E=0) = 80.5/137 = 0.588
    modulation(E→∞) = 80.5/24 = 3.354
What function of (r, s, E) gives this modulation?


### Track 4 — Bidirectional physics on the torus

On a T², a wave can propagate in two directions around
a cycle (clockwise and counterclockwise).  The shear
breaks the degeneracy: the two directions have different
effective path lengths (L vs L + δL where δL ∝ s).

The CHARGE is the asymmetry between the two directions.
The COUPLING is related to how much of the internal
energy leaks into R³ through this asymmetry.

At low energy (long wavelength), the probe averages over
both directions — the net coupling is REDUCED by
destructive interference between the two propagation
directions.  This is the IR screening that pushes
1/α up to 137.

At high energy (short wavelength), the probe resolves
the two directions separately — the net coupling is
ENHANCED because the interference is no longer complete.
This is the UV anti-screening that pushes 1/α down to 24.

Compute:
- The path length difference δL = s × L_tube for each sheet
- The interference visibility V(E) = |cos(2πE δL/ℏc)|
- The effective coupling: 1/α(E) = 1/α₀ + 56.5 × V(E)
- Does V(0) = +1 and V(∞) → −1?


## What success looks like

- **Strong result**: The dispersive model reproduces the
  running of α from 1/137 to ~1/128 (at m_Z) AND
  extrapolates to 1/24 at the compact scale.  The
  resonance scale is the proton ring energy (~467 MeV).
  The shear can be derived from 1/α₀ = 80 without
  reference to the observed α.

- **Moderate result**: The bidirectional model has the
  right qualitative shape but the wrong numerical values.
  The concept of a geometric base coupling modulated by
  dispersion is supported but the details need refinement.

- **Null result**: 1/80 ≈ (137+24)/2 is coincidence.
  The dispersive model produces the wrong sign, wrong
  magnitude, or no convergence.  The base coupling is
  not 1/80.

- **Structural insight**: Even a null numerical result
  could clarify WHERE α comes from: whether the shear
  has one or two independent modulation mechanisms, and
  whether the 4π in the formula should be 24 (gauge
  channels) or 4π (solid angle) or something else.
