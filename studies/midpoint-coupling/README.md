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


### Track 1 — Kramers-Kronig dispersive model  **Complete**

Model the T² mode spectrum as absorption resonances and
compute the dispersive running of α(E).

**Result:** Pure Kramers-Kronig cannot reach 1/24 — the
dispersive contribution vanishes at high E, leaving 1/α →
80.5.  A hybrid model (screening + running as complementary
functions) reduces to a Lorentzian dispersion:

    1/α(E) = 80.5 + 56.5 × (E*² − E²) / (E² + E*²)

Fitting to α(m_Z) gives E* ≈ 310 GeV (near the electroweak
scale).  The Lorentzian works below m_Z (within 3%) but
fails catastrophically above (wrong curvature — Lorentzian
vs logarithmic).  No T⁶ geometric scale gives the right E*.
Findings F1–F6.


### Track 2 — Logarithmic running from 1/α₀ = 80

Drop the speculative UV endpoint of 24.  Use only
verified physics:

- 1/α(0) = 137.036  (measured)
- 1/α(m_Z) = 128.0   (measured)
- 1/α₀ = 80          (T⁶ geometric base, from R32 F23)

The standard QFT one-loop running is:

    1/α(E) = 1/α₀ + Σ_k (b_k Q_k²)/(3π) × ln(Λ/max(E, m_k))

where the sum runs over all charged species (SM fermions
+ T⁶ ghost modes).  Each species contributes screening
above its mass threshold.

With SM fermions alone, the running rate is ~0.74 per
unit ln(E).  This gives only 9 units of screening by m_Z,
not nearly enough to reach 137 from 80 (needs 57 units).

But T⁶ ghost modes (~78,000 charged modes) contribute at
a suppressed level.  At suppression factor f:
    Effective rate = SM_rate × (1 + 157,000 × f)
    Need rate ≈ 5.75 × SM_rate to cover 57 units

Procedure:
1. Fit f so that 1/α(0) = 137 (using the full T⁶ mode
   spectrum from R32 Track 1)
2. With this f, compute 1/α(m_Z) — does it equal 128?
3. Report f and compare to the R31/R32 constraint (~10⁻⁵)

If the fitted f ≈ 3 × 10⁻⁵ AND the model matches 128
at m_Z, the ghost suppression factor is independently
derived from the running (not from Lamb shift), providing
a cross-check on the T⁶ model.

Also compute 1/α(E) at 10+ energy points and compare to
the SM predictions.  The T⁶ model should reproduce the
SM running at all measured energies, with the ghost modes
adding a small (but necessary) correction that shifts the
bare coupling from ~60 (SM at GUT scale) to 80.

**Result:** NULL.  f ≈ 6 × 10⁻⁵ fits 1/α(0) = 137
(right order for ghost suppression), but 1/α(m_Z) = 101,
not 128.  Root cause: ghost modes cluster below 2 GeV,
causing front-loaded running that exhausts most of its
screening before reaching m_Z.  The discrepancy shrinks
with higher cutoffs (119 at 1 PeV) but never fully
closes.  Findings F7–F10.


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


### ~~Track 4 — Bidirectional physics on the torus~~  **Retired**

Superseded by Track 2.  The bidirectional hypothesis
depended on the unverified UV endpoint 1/α → 24.
Track 2 uses only verified physics (QFT running from
a geometric base coupling).


---

## Summary — R34 complete

### Outcome: Open — null result for simplest models, but untested avenues remain

**Track 1 (Kramers-Kronig):** The Lorentzian dispersion
model has the right endpoints (137, 24) but the wrong
intermediate shape.  The fitted midpoint scale E* ≈ 310
GeV falls near the electroweak scale.  The UV endpoint
1/24 is unverified — only the IR (137) and one measured
intermediate point (128 at m_Z) are established.

**Track 2 (logarithmic running from 80):** With uniform
ghost suppression f ≈ 6 × 10⁻⁵, the model correctly
reaches 1/α(0) = 137 but gives 1/α(m_Z) = 101 (not 128).
Root cause: ghost modes cluster below 2 GeV, causing
front-loaded running.  The discrepancy shrinks with
higher cutoffs (119 at 1 PeV).  The uniform-f model
is ruled out, but mass-dependent suppression, winding-
number-dependent coupling, and inclusion of known T⁶
particles beyond e/p have not been tested.

**Track 3 (backing into the shear):** Not yet run.  Still
viable — solving s from 1/α₀ = 80 could reveal whether
the resulting shear has geometric significance.

### Key clarifications

1. The T⁶ model provides a MECHANISM for α (shear-charge
   coupling on the torus) but does not DERIVE the value
   1/137.  The shear s is reverse-engineered from α.

2. 1/80 from the weighted gauge partition is a real
   geometric property of the 10D metric.  Whether it
   connects to α (via running, impedance, or otherwise)
   remains open.

3. The hypothesis that 1/80 = (137 + 24)/2 depends on
   the unverified UV value 1/24.  Without it, 1/80 stands
   alone as a geometric number.

4. The uniform-f running model is ruled out, but the
   parameter space has not been exhausted.  Energy-
   dependent ghost suppression (from R33) could
   redistribute the running and fix the m_Z discrepancy.
