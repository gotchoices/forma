# Particle Spectrum from Flat Extra Dimensions

**Status:** outline

---

### Model card

| | |
|---|---|
| **Framework** | Maxwell's equations on a flat 10D manifold Ma × S × t |
| **Topology** | Ma = three flat tori (Ma_e × Ma_ν × Ma_p), S = ℝ³, t = ℝ |
| **Inputs** | m_e, m_p, Δm²₂₁, α (three masses fix torus scales; α fixes within-plane shears given aspect ratios) |
| **Pinned by observation** | r_p = 8.906 and σ_ep = −0.091 (jointly by neutron + muon, R27 F18), s₃₄ = 0.022 (ν oscillations) |
| **Effective free parameters** | 2 (r_e, r_ν); MeV predictions insensitive to both |
| **Outputs** | 6 particle masses to < 1.2% with no adjustment (7 within ~1.2%); three lepton masses accommodated; nuclear masses to < 1% (R29) |
| **Failures** | τ (5.6%), π⁺ (14%), Ω⁻ (structurally forbidden), ghost modes (~14k charge −1 spin ½ levels vs 3 observed leptons) |
| **Testable** | Σm_ν = 116–120 meV (depends on r_ν), normal ordering, Ma_ν ring L₄ ≈ 42 μm (within reach of short-range gravity experiments if gravity propagates in Ma_ν) |

---

## Outline

### 1. Model summary

One paragraph: photons on a compact flat manifold.
Lagrangian: free Maxwell on Ma × S × t (one line).
Mode energies = particle masses.  Four inputs (m_e, m_p,
Δm²₂₁, α) set the geometry; everything else is output.

The spectrum table goes here — predicted vs observed for
all matched particles.  This is what the reader came for.

### 2. Geometry and mode spectrum

The Ma manifold: three flat tori with independent scales.
Mode energy formula: E(n₁…n₆) from the Ma metric.
21 metric components; 8 constrained by data.  11 cross-shears
are formally free but irrelevant (all zero, R28).  Effective
free parameters: 2 (r_e and r_ν).

### 3. Spin, charge, and mass

Spin ½ from 1:2 winding ratio (topological, exact).
Charge from the shear integral — the α(r,s) formula.
g = 2 from photon spin / fermion spin.
Mass = mode eigenfrequency on Ma.
Each derivation self-contained and checkable.

### 4. The neutron

Three-sheet mode (0,−2,+1,0,0,+2) spanning Ma_e × Ma_ν × Ma_p
(R27 F15–F16).  Charge: Q = −n₁ + n₅ = 0 (exact, both zero).
Spin ½ from neutrino ring winding n₃ = 1.
m_n > m_p is geometric: cross-sheet modes always cost
more energy than single-sheet modes.
Decay products (p + e⁻ + ν̄) = the three input particles —
the mode "unravels" along its three resident sheets.
r_p and σ_ep jointly pinned by neutron mass + muon mass (R27 F18).

### 5. Neutrino mass splittings

Three modes on Ma_ν.  Mass-squared ratio depends on
one parameter: R = (3 − 2s₃₄)/(4s₃₄).
s₃₄ = 0.022 gives R = 33.6 (experiment: 33.6 ± 0.9).
Σm_ν = 116–120 meV depending on r_ν (≥ 3.2); asymptotes
to 116.4 meV as r_ν → ∞ (R26 F2).  Below cosmological
bound ~120 meV for all allowed r_ν.
Normal mass ordering predicted (R26 F33).

### 6. Three generations

Three charge −1, spin ½ modes match the observed leptons:
e (input), μ (exact, jointly pins r_p with neutron), τ (5.6% off).  Three
neutrino modes on Ma_ν match the Δm² ratio exactly.

Candor required: the Ma spectrum contains ~14,000 charge −1,
spin ½ levels below 10 GeV and ~1,000 weakly-charged neutrino
species.  The model accommodates three generations (the masses
match) but does not predict why only three are realized.  This
is the ghost mode problem — the same issue as §8 — and solving
it would automatically explain the generation count.

### 7. Predictions and failures

Full table of untuned predictions (R27 F31, R28 F10):

| Particle | Mode | Error | Source |
|----------|------|------:|--------|
| K⁺ | (−4,−8,+1,0,−3,−1) | 1.2% | R27 F31 |
| K⁰ | (−3,−8, 0,0,−3,+1) | ~1.2% | R27 F31 |
| η | (−5,−8, 0,0,−5,+1) | 0.6% | R27 F31 |
| η′ | (−3,−8, 0,0,−3,+2) | 0.3% | R27 F31 |
| φ | (−7,−8, 0,0,−7,+2) | 0.8% | R27 F31 |
| Λ | (−12,−15,+1,0,−12,−2) | 0.9% | R28 F10 |
| Σ⁺ | (−14,−15, 0,0,−13,+2) | 0.3% | R28 F14 |

Specific failures with geometric explanations:
- τ: 5.6% — structural gap on proton-ring ladder (R27 F22)
- π⁺: 14% — lightest meson poorly matched (R27 F29)
- Ω⁻: structurally forbidden — charge −1, spin 3/2 is
  impossible as a single Ma mode (R27 F35)

Nuclear scaling law (R29): n_φp = A, n_θp = 2A matches
nuclei from deuteron to ⁵⁶Fe at < 1%.  Nuclear spins
predicted correctly for 9 of 11 tested nuclei.

Predictive horizon: spectrum too dense above ~2 GeV (R28 F5);
W/Z/Higgs match trivially (any mass would).

### 8. Open problems

- **α not derived** from first principles.  r_e ≈ 0.50
  preferred by membrane energy minimisation (R37 F7) but
  the minimum is broad.  Moduli potential unknown.
- **Ghost modes:** ~14,000 charge −1, spin ½ levels below
  10 GeV (R38 F1); ~900 modes with |Q| ≤ 2 below 2 GeV
  vs ~40 known particles (R28 F5–F6).  R33 selection
  rules reduce ghosts to ~4 per charged sheet, but the
  selection rule (WvM) conflicts with the current charge
  formula (KK).  Ghost suppression is the central open
  problem.
- **No QFT formulation yet.**  Vertex calculations, running
  couplings, and decay rates require a quantized field
  theory on Ma × S × t that does not yet exist.
- **Three generations** accommodated but not predicted.
  Resonance capture hypothesis (R38 Track 5) could gate
  charged leptons at 3 with cavity Q ≈ 30, but neutrino
  overcounting (~1,000 species vs 3) remains open.

---

## Notes on tone and strategy

- Lead with numbers, not philosophy.
- State the Lagrangian explicitly (it's one line).
- Every derivation must be reproducible by a skeptic.
- Do not claim Theory of Everything.
- Do not criticize the Standard Model.
- Address failures before the reader finds them.
- Target length: 10–12 pages.
