# R34. The midpoint coupling — bidirectional modulation of α

**Status:** Complete  
**Questions:** Q77 (α as impedance), Q18 (deriving α)  
**Type:** compute + theoretical  
**Depends on:** R19 (R19-shear-charge), R31 (alpha derivation),
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


### Track 3 — Backing into the shear  **Complete**

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

**Result:** The shear scales as √α — changing the target
from 1/137 to 1/80 just rescales s by √(137/80) = 1.308,
identically on both sheets.  Neither shear matches a
geometric constant (though s_p(80) ≈ 1/100 to 0.1%).
The prefactor r²μ/(4π(2−s)²) is nearly s-independent,
so the formula reduces to α ≈ C(r) × (2πs)².  The
standard denominator 4π(2−s)² ≈ 50, not 24.  The shear
is a continuous free parameter with no selection
mechanism.  Findings F19–F23.


### Track 5 — Running with known particles only (no ghosts)

Track 2 included ~78,000 ghost modes at a uniform
suppression factor f.  But ghost modes are empirically
unobserved.  If nature does not select them as real
excitations, they should not participate as virtual
excitations either.  Virtual particles in QFT vacuum
polarization loops are drawn from the same spectrum as
real particles.  If ghost modes are absent from the
physical spectrum, they are absent from the loops.

**Premise:** The running of α should be computed using
ONLY the particles that T⁶ predicts AND that nature
confirms.  No ghosts.  No suppression factors.

This changes the calculation fundamentally.  In the
Standard Model, vacuum polarization comes from:
- 3 charged leptons (e, μ, τ)
- 6 quarks × 3 colors (u, d, s, c, b, t with
  fractional charges 2/3 and 1/3)
Total: ~21 charged Dirac fermions
Effective Σ Q² × N_c = 3 + 4 + 1 = 8 (quarks) + 3
(leptons) = 11

In T⁶, hadrons are fundamental — there are no quarks.
The vacuum polarization comes from the known T⁶ modes:
- Leptons: e⁻, μ⁻, τ⁻ (Q = −1)
- Mesons: π⁺, K⁺ (spin-0, Q = +1); ρ⁺, K*⁺ (spin-1,
  Q = +1)
- Baryons: p, Σ⁺, Δ⁺, N* resonances (Q = +1);
  Σ⁻, Ξ⁻, Δ⁻, Σ*⁻, Ξ*⁻, Ω⁻ (Q = −1);
  Δ⁺⁺ (Q = +2, contributes Q² = 4)
Plus antiparticles for each.

Key differences from SM:
1. No color factor ×3 (hadrons are fundamental, not
   composite)
2. No fractional charges (all Q = ±1 or ±2)
3. Many more charged species above ~140 MeV (pions,
   kaons, hyperons, deltas)
4. The Δ⁺⁺ with Q = +2 contributes 4× per unit

The effective Σ Q² for T⁶ particles is comparable to
the SM value but distributed very differently in mass:
- Below 100 MeV: only e (vs e + u,d quarks in SM)
- 100–1800 MeV: many hadrons enter (vs s,c quarks + μ)
- Above 1800 MeV: τ only (vs b,t quarks + τ in SM)

**Procedure:**
1. Enumerate all known T⁶ particles from R28 with their
   masses, charges, and spins
2. Assign vacuum-polarization coefficients:
   b = 4/3 for spin-1/2 fermions (Dirac)
   b = 1/3 for spin-0 scalars
   b = 7   for spin-1 vectors (Proca)
3. Compute one-loop running:
   1/α(E) = 1/α₀ + Σ_k (b_k Q_k²)/(3π) × ln(Λ/max(E,m_k))
   for all known charged particles k with m_k < Λ
4. Fit 1/α₀ so that 1/α(m_e) = 137.036
5. Check: does 1/α(m_Z) = 128?
6. Plot the full running curve and compare to SM

**Success criteria:**
- A bare coupling 1/α₀ ≈ 80 would validate the
  weighted gauge partition from R32
- 1/α(m_Z) matching 128 without tuning would be a
  strong result
- Any clean geometric value for 1/α₀ (even if not 80)
  would be interesting

**Result:** T⁶ known particles run α ~2.4× too fast.
Δ(1/α) from m_e to m_Z = 21.9 (vs measured 9.0),
giving 1/α(m_Z) = 115.  The T⁶ particle content has
Σ b×Q² = 44 vs SM's 10.7, driven by many charged
baryons, Δ⁺⁺ (Q=+2), and vector mesons (b=7).
Even minimizing the vector coefficient: Δ = 15.3,
still too large.  Cutoff for 1/α₀ = 80 is ~168 TeV.
Open question: should short-lived resonances (Γ ~ m)
contribute as sharp thresholds?  Findings F13–F18.


### ~~Track 4 — Bidirectional physics on the torus~~  **Retired**

Superseded by Track 2.  The bidirectional hypothesis
depended on the unverified UV endpoint 1/α → 24.
Track 2 uses only verified physics (QFT running from
a geometric base coupling).


---

## Summary — R34 complete

### Outcome: No model successfully reproduces the observed running of α from a geometric base

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

**Track 3 (backing into the shear):** The shear is a
continuous free parameter: changing the target α just
rescales s by √(α_new/α_old).  Neither the 1/137 nor
1/80 shear matches a geometric constant.  The formula
provides a mechanism (shear → coupling) but has no
selection principle for s.  The denominator 4π(2−s)² ≈ 50,
not 24.  One curiosity: s_p(80) ≈ 1/100 to 0.1%.

**Track 5 (known particles only):** T⁶ known particles
(no ghosts) run α 2.4× too fast: Δ(1/α) = 21.9 from
m_e to m_Z vs measured 9.0.  The overshoot comes from
many charged baryons (especially Δ⁺⁺ with Q²=4) and
vector mesons (ρ±, K*± with b=7).  However, 75% of the
excess comes from short-lived resonances (Γ ~ m) whose
treatment as sharp VP thresholds is questionable.

### Key clarifications

1. The T⁶ model provides a MECHANISM for α (R19-shear-charge
   coupling on the torus) but does not DERIVE the value
   1/137.  The shear s is reverse-engineered from α.

2. 1/80 from the weighted gauge partition is a real
   geometric property of the 10D metric.  Whether it
   connects to α (via running, impedance, or otherwise)
   remains open.

3. The hypothesis that 1/80 = (137 + 24)/2 depends on
   the unverified UV value 1/24.  Without it, 1/80 stands
   alone as a geometric number.

4. Ghost modes are empirically unobserved.  If they are
   absent from the physical spectrum, they should also be
   absent from virtual loops.  Track 5 confirms this
   premise but reveals that even the known T⁶ content
   runs too fast — the hadronic sector contributes 5×
   more screening than SM quarks.

5. The central open question is whether the T⁶ hadronic
   VP should be computed perturbatively (as done here)
   or requires non-perturbative treatment (as in the SM,
   where hadronic VP is extracted from e⁺e⁻ → hadrons
   data, not from quark loops).
