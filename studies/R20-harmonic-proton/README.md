# R20. Harmonic Proton  *(complete)*

Can the proton be modeled as the electron's fundamental mode plus
higher harmonics on the same geodesic — adding mass without charge?

**Answer: yes.**  Five tracks confirm the construction works
kinematically.  The model is descriptive but not yet predictive —
the harmonic spectrum is underdetermined.  Predictivity requires
embedding curvature to select the spectrum and potentially produce
quarks (→ R21).

## Background

R19 established the electron as a (1,2) mode on the sheared electron sheet, with
charge arising from the n₁ = 1 selection rule (F30): only modes
with n₁ = 1 produce nonzero charge.  All other modes are electrically
silent.

R14 attempted to build hadrons from three topologically linked
photons on the 3-torus.  This failed: the charge mechanism depends on mode
numbers, not spatial arrangement (F18).  Linking cannot redistribute
charge.  All four mechanisms tested (localization, classical
interaction, KK gauge mixing, wavepacket superposition) fail to
produce fractional charges.

The harmonic approach takes a fundamentally different path: instead
of distributing charge across multiple photons, keep it in one mode
and add mass through uncharged harmonics.

## Core idea

### The electron

A photon on the (1,2) geodesic of the sheared electron sheet, with one wavelength
fitting the geodesic length L_e.  Energy m_e c², charge e, spin ½.
This is the fundamental — the base term of the series.

### Harmonics

A standing wave on the same (1,2) geodesic with n wavelengths
fitting in one traversal.  The nth harmonic has:

    wavelength:  λ_n = L_e / n
    energy:      E_n = n × m_e c²      (shorter wavelength → more energy)
    charge:      Q_n ≈ 0               (n₁ ≈ n ≠ 1 → uncharged by F30)

The charge claim needs verification: on the sheared electron sheet, the nth harmonic
of the geodesic decomposes into a superposition of material-sheet Fourier modes.
The dominant component is (n, 2n) with n₁ = n, which is uncharged.
But sub-dominant components may include n₁ = 1 terms, leaking
a small amount of charge.  Track 1 will compute this.

### The proton

The electron's fundamental plus some collection of harmonics:

    m_p = m_e + Σ E_n = m_e + Σ n_i × m_e

Total charge = e + 0 + 0 + ... = e.
The harmonics carry mass but not charge.

What selects the specific harmonics is left open for now.
The first goal is to verify that the construction *can* produce
the right mass and charge.

### The neutron

Two fundamentals with opposite winding — the electron (charge −e)
and its CPT conjugate (charge +e) — plus harmonics of both:

    Q_neutron = (−e) + (+e) + 0 + 0 + ... = 0
    m_neutron = 2m_e + Σ harmonic energies

### Neutron decay

    n → p + e⁻ + ν̄_e

The electron fundamental escapes the composite.  The remaining
positron-type fundamental plus harmonics is the proton.  The mass
difference m_n − m_p = 1.293 MeV ≈ 2.53 m_e provides the electron's
mass (0.511 MeV) plus kinetic energy shared between the electron
and antineutrino (0.782 MeV).

## How much harmonic energy makes a proton?

The proton mass is m_p = 1836.15 m_e.  The fundamental contributes
m_e, so the harmonics must total 1835.15 m_e.

Several harmonic spectra could reach this target:

**A. All harmonics 1 through N (complete series).**

    Σ_{n=1}^{N} n = N(N+1)/2

    N = 60:  1830     (0.3% short)
    N = 61:  1891     (3% over)

No exact integer N gives 1836.  But on a sheared torus the harmonic
energies are not exactly n × m_e (shear shifts the effective
wavelengths), so the actual sum may land closer.

**B. Incomplete series (specific subset).**

Many subsets of integers sum to 1835.  Without a selection rule,
the choice is underdetermined.

**C. Weighted series (amplitude spectrum).**

If each harmonic n has occupation f(n), the total mass is:

    m_p = Σ f(n) × n × m_e

For a thermal (Bose-Einstein) distribution f(n) = 1/(e^{n/T} − 1):

    m_p ≈ T² × π²/6 × m_e     (high-T limit)

Setting m_p = 1836 m_e gives T ≈ 33.4, meaning a characteristic
harmonic "temperature" of ~33 m_e ≈ 17 MeV.  The infinite series
converges (exponential suppression of high harmonics), and the
specific T determines the mass.

This is the most promising path to a convergent series, but
requires a physical justification for the thermal distribution.

**D. Single high harmonic.**

The proton as the n = 1836 harmonic (one mode, energy 1836 m_e).
Simple but problematic: its spin would be 1/(2 × 1836) ≈ 0.00027,
violating the spin quantization constraint (F10 requires integer
or half-integer spin in 3+1D).

## What this study does NOT attempt (yet)

- **Why these harmonics?**  What physical mechanism selects the
  proton's harmonic spectrum is deferred.  The goal is first to
  establish that the construction CAN reproduce the right mass
  and charge (the "how"), then investigate the selection mechanism
  (the "why").

- **DIS compatibility.**  Deep inelastic scattering reveals three
  charged scattering centers inside the proton.  The harmonic
  model predicts one charged center (the fundamental) plus many
  neutral ones.  Reconciling this likely requires reinterpreting
  what DIS measures (R14 F19 exit A).  This is a stretch goal,
  not a prerequisite.

- **Binding mechanism.**  On a flat material sheet with linear Maxwell
  equations, eigenmodes are decoupled — a superposition is not
  a bound state.  A physical proton requires mode-mode coupling
  (from embedding curvature, nonlinear effects, or quantum
  discreteness).  Deferred.

## Planned approach

### Track 1: Harmonic spectrum and charge on sheared electron sheet  ✓

**Result (F1–F7):** The (n, 2n) harmonics are exactly uncharged
for n ≥ 2 (by the n₁ selection rule — no leakage).  In the
momentum picture (E = ℏc|k|), E(n,2n) = n × m_e, and convergent
infinite series (thermal T' ≈ 34 m_e, geometric x ≈ 0.98) reach
the proton mass.  A pure thermal distribution fails because it
gives Q ≈ 33e; the fundamental must have occupation f(1) = 1
exactly (F3).

**Energy formula resolved (F5):** The correct energy is E = ℏc|k|
(standard QFT for a massless field on a torus).  Harmonics are
heavier (n × m_e).  The "winding energy" E = hc/L_geo used in R13
was a correct simplification for the fundamental mode but does not
generalize to higher modes.  A remaining question (F6): the momentum
picture predicts lighter charged modes with non-integer charges
(spin-1 bosons at ~0.6–0.7 m_e with Q ≈ 1.6–2.2e).  These are
not observed; charge quantization or instability may forbid them.

### Track 2: Proton mass from harmonic sums  ✓

**Result:** Covered by Track 1, sections 4a–4e.  Multiple
convergent series reach 1836 m_e (F4).  The (n, 2n) harmonic
energies are exactly n × m_e with no shear correction (F5),
so step 3 is trivially satisfied.  The distribution is
underdetermined — many spectra work, none uniquely selected.

### Track 3: Neutron model and decay  ✓

**Result (F8–F13):** The neutron = two opposite-charge spin-1/2
fundamentals (+e and -e) plus uncharged harmonics.  Total charge
is exactly 0.  Beta decay energetics match: the endpoint energy
0.782 MeV is reproduced.  Proton stability (one fundamental,
nothing to annihilate) and neutron instability (charged pair can
separate) have natural explanations.  The mass difference
m_n - m_p = 2.53 m_e splits as 1 m_e (extra fundamental) +
1.53 m_e (extra harmonics, a 0.04% thermal temperature shift).

**Open:** antineutrino identity, binding mechanism, what sets
the 1.53 m_e harmonic excess.

### Track 4: Neutrino mass and spin  ✓

**Result (F14–F18):** The neutrino cannot be a mode on the
electron sheet — the lightest uncharged spin-1/2 mode is (2,4)
at 2 m_e, six orders of magnitude too heavy.  A separate
neutrino sheet with L_ν ≈ 1.5 μm (at the KATRIN bound) is experimentally
allowed.  Near-degeneracies between high modes on the electron
sheet naturally produce sub-eV energy splittings (0.29 eV at
E < 100 m_e), showing the neutrino mass scale emerges from
the torus geometry without tuning.

**Bonus (F17):** The muon and tau fit naturally as "hot electrons"
— same (1,2) fundamental + uncharged harmonics.  Decay = harmonic
evaporation.  Proton stability (no lighter +e particle) and
muon/tau instability (can shed harmonics to bare electron) are
both explained by charge conservation.

**Open:** neutrino identity (separate neutrino sheet, geometry fluctuation,
or created in decay).

### Track 5: Three-mode neutrino packet  ✓

**Result (F19–F20):** No triplet of uncharged modes from the
electron sheet sums to the neutron excess (1.531 m_e).  The
lightest triple is 3 × (0,1) = 1.44 m_e — 0.09 m_e short,
and the next option overshoots.  The Δm² ratio test could
not be performed (no triplets to test).

More fundamentally, every uncharged mode has rest mass
≥ 0.48 m_e = 245 keV, while the neutrino is < 0.8 eV.
No wave packet construction closes this 10⁵ gap.  F18c
(neutrino as ejected harmonics on electron sheet) is now
ruled out.  F18a (separate neutrino sheet) and F18b (geometry
fluctuation) remain viable.

## Dependencies

- **R19 (complete):** Charge formula, s₁₂ ≈ 0.165, n₁ = 1
  selection rule, electron as (1,2) mode.
- **R14 (closed, negative):** Established that linking cannot
  redistribute charge.  Positive results carried forward: F10
  (spin quantization), F30 (only n₁ = 1 carries charge).
- **R13 (complete):** Electron is a winding mode on the electron sheet.

## Relation to other questions

- Q16: what sets the photon energy / mass spectrum
- Q26: multi-photon hadrons
- Q28: photon absorption and excited electrons (harmonics as
  excitations of the same geodesic)
- Q32: energy and geometry as only fundamentals

## Model status after R20

### What is determined

| Quantity | Value | Set by |
|----------|-------|--------|
| Electron mode | (1,2) on sheared electron sheet | R13 |
| Shear s₁₂ | ≈ 0.165 (at r = 1) | R19: α(1,2) = 1/137 |
| Charge rule | only \|n₁\| = 1 modes carry charge | R19 F30 |
| L₁ | λ_C × √(1 + (2−s)²/r²) ≈ 2.09 λ_C at r = 1 | E(1,2) = m_e c² |
| L₂ | r × L₁ | by definition |
| Proton charge | +e (from (−1,−2) fundamental) | R20 F2 |
| Neutron charge | 0 (two opposite fundamentals) | R20 F8 |
| Decay endpoint | 0.782 MeV (matches experiment) | R20 F9 |
| Stability | proton stable, neutron unstable | R20 F10 |
| Spin | 1/2 for all baryons and leptons | R14 F10 |

Note: once r is chosen, s₁₂ is fixed by α = 1/137, and then
L₁, L₂ follow from m_e c².  The absolute torus size is NOT free
— it is set by the electron mass.  At r = 1:
L₁ ≈ L₂ ≈ 5.1 × 10⁻¹² m,  a ≈ R ≈ 8.1 × 10⁻¹³ m.

### Free parameters

1. **Aspect ratio r = L₂/L₁.**  The single continuous free
   parameter.  Currently set to r = 1 for simplicity.
   Different r values give different s values (all producing
   α = 1/137) and different mode spectra.  Nothing in the
   model fixes r — it would need to come from an energy
   minimization or stability argument.

2. **Harmonic spectrum.**  Which uncharged modes compose the
   proton (and neutron) is underdetermined.  Many distributions
   reproduce 1836 m_e — thermal (T' ≈ 34 m_e), geometric
   (x ≈ 0.98), truncated sums, or mixtures.  A selection rule
   requires understanding mode-mode coupling from embedding
   curvature (→ backlog: natural harmonic spectrum study).

### Open structural questions

3. **Why (1,2)?**  Why the electron has winding numbers (1,2)
   rather than (1,1) or (1,3) is not derived.  The answer
   likely involves spin quantization (only half-integer spin
   modes are fermions) and charge quantization (only (1,2)
   gives Q = e exactly), but this hasn't been proven.

4. **Binding mechanism.**  On a flat material sheet, eigenmodes are
   orthogonal and don't interact.  Embedding curvature
   breaks this orthogonality, potentially binding modes
   into composites.  Without binding, the model is
   kinematic (correct numbers) but not dynamical.

5. **Charge coupling to 3D.**  The R19 charge integral
   computes a 2D quantity.  How this couples to the
   external Coulomb field in 3D is not derived from first
   principles.  R15/R16/R17/R18 attempted this and
   identified the difficulty.

6. **Neutrino mechanism.**  The neutrino cannot live on the
   electron sheet (F14).  A separate neutrino sheet at ~1.5 μm or a
   geometry fluctuation are the remaining options (F18).

7. **DIS compatibility.**  Deep inelastic scattering shows
   three charged scattering centers in the proton.  The
   model has one (the fundamental).  This is the largest
   long-term risk.

8. **Non-integer charged modes.**  The spectrum predicts
   spin-1 bosons lighter than the electron with charges
   ~1.6e and ~2.2e (F6).  These are unobserved and need
   a suppression mechanism.

### Lightest modes on the electron sheet

Complex geodesics (high winding numbers) do not help.  On
a flat material sheet, every excitation decomposes into plane-wave modes
(n₁, n₂) with E = ℏc|k(n₁,n₂)|.  Higher mode numbers
always give higher |k| and higher energy.  The lightest
uncharged mode is (0,±1) at 0.479 m_e = 245 keV.  Proof:

- n₁ = 0: lightest is |n₂| = 1 → E = 0.479 m_e
- |n₁| ≥ 2: n₁² ≥ 4, so E ≥ √(4/4.37) m_e = 0.957 m_e

No mode on this lattice — regardless of complexity — can
be lighter than 245 keV.  Sub-eV particles require either
a much larger torus or a non-KK mechanism.

### What would make the model predictive

The current model is **descriptive**: it shows that the
right masses, charges, and spins can be constructed, but
doesn't uniquely predict them (the harmonic spectrum is
free).  To become **predictive**, the model needs:

1. A principle selecting r (fixes the geometry completely).
2. Mode-mode coupling from embedding curvature (selects the
   harmonic spectrum → predicts m_p, m_n, m_μ, m_τ).
3. A neutrino mechanism (completes the lepton sector).

The first two are addressed by the backlog item "Natural
harmonic spectrum from mode coupling."
