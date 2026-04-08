# L04: Beta Decay Rate Modification via THz Resonance

**Status:** Proposed
**Tests:** EM-to-neutrino-sheet coupling hypothesis
  ([neutrino primer](../primers/neutrino.md);
   [Q89](../qa/Q89-fusion-as-mode-transition.md) §11)
**Related:** R49 F1–F10 (22 candidate triplets),
  R26 F1–F9 (neutrino sheet mode spectrum),
  [L01](L01-thz-write-read.md) (THz write/read — shares
  equipment and source technology),
  [L02](L02-threshold-nuclear-loading.md) (nuclear loading —
  same coupling channel, different observable)

---

## 1. Hypothesis

Beta decay (n → p + e⁻ + ν̄ₑ) requires populating an
outgoing neutrino mode.  If the neutrino sheet (Ma_ν) is a
physical structure with discrete standing-wave modes, and if
those modes couple (however weakly) to the electromagnetic
field through the shared lattice substrate, then an external
EM field at a neutrino mode frequency should modify the
transition rate.

Specifically: coherent THz radiation at a frequency matching
one of the three neutrino mass eigenstates could either
**stimulate** the transition (enhance the rate, analogous to
stimulated emission in a laser) or **suppress** it (if the
driven field is out of phase with the decay channel).

The Standard Model predicts exactly zero effect of THz
radiation on beta decay rates.  Any statistically significant
rate change at a predicted frequency — absent at nearby
off-resonance frequencies — would be extraordinary.


## 2. The frequency table

MaSt (R49) identifies 22 viable mode triplets on the
neutrino sheet that reproduce the measured Δm² ratio of
~33.6.  These 22 triplets collapse to **4 distinct frequency
sets** because many triplets share the same energies (they
differ only in the sign of mode quantum numbers).

### Conversion

Mode energy E in meV converts to frequency and wavelength:

> f (THz) = E (meV) × 0.2418
> λ (μm) = 1240 / E (meV)

### The 4 distinct frequency sets

**Set 1 — Family A** (1 triplet: ε_ν = 5.0, s = 0.022)

| Eigenstate | Mode (n₃,n₄) | Mass (meV) | Frequency (THz) | λ (μm) |
|:---:|:---:|:---:|:---:|:---:|
| ν₁ | (1, 1) | 29.2 | 7.06 | 42.5 |
| ν₂ | (−1, 1) | 30.5 | 7.37 | 40.7 |
| ν₃ | (1, 2) | 58.2 | 14.07 | 21.3 |

Σm = 117.8 meV.  Tight against cosmological bound.

**Set 2 — Family B** (16 triplets: ε_ν = 0.1, s = 0.001–0.4)

| Eigenstate | Mode (n₃,n₄) | Mass (meV) | Frequency (THz) | λ (μm) |
|:---:|:---:|:---:|:---:|:---:|
| ν₁ | (±1, 2) | 5.1 | 1.23 | 243 |
| ν₂ | (±2, 2) | 10.1 | 2.44 | 123 |
| ν₃ | (±10, 1 or 2) | 50.1 | 12.11 | 24.8 |

Σm = 65.3 meV.  Comfortable margin.  16 triplets have
identical masses (differ only in sign combinations of
n₃).

**Set 3 — Family C low-mass** (4 triplets: ε_ν = 0.2, s = 0.3–0.4)

| Eigenstate | Mode (n₃,n₄) | Mass (meV) | Frequency (THz) | λ (μm) |
|:---:|:---:|:---:|:---:|:---:|
| ν₁ | (0, 2) | 3.4 | 0.82 | 365 |
| ν₂ | (−1, 2) | 9.3 | 2.25 | 133 |
| ν₃ | (±6, 1 or 2) | 50.8 | 12.28 | 24.4 |

Σm = 63.5 meV.

**Set 4 — Family C high-mass** (1 triplet: ε_ν = 0.2, s = 0.3)

| Eigenstate | Mode (n₃,n₄) | Mass (meV) | Frequency (THz) | λ (μm) |
|:---:|:---:|:---:|:---:|:---:|
| ν₁ | (1, 2) | 29.6 | 7.16 | 41.9 |
| ν₂ | (−1, 2) | 30.8 | 7.45 | 40.3 |
| ν₃ | (−2, 2) | 57.9 | 14.00 | 21.4 |

Σm = 118.3 meV.  Nearly identical to Set 1 (within ~2%).

### Consolidated target frequencies

| Frequency (THz) | λ (μm) | Which sets | Which eigenstate |
|:---:|:---:|:---:|:---:|
| **0.82** | 365 | Set 3 | ν₁ |
| **1.23** | 243 | Set 2 | ν₁ |
| **2.25** | 133 | Set 3 | ν₂ |
| **2.44** | 123 | Set 2 | ν₂ |
| **7.06** | 42.5 | Set 1 | ν₁ |
| **7.16** | 41.9 | Set 4 | ν₁ |
| **7.37** | 40.7 | Set 1 | ν₂ |
| **7.45** | 40.3 | Set 4 | ν₂ |
| **12.11** | 24.8 | Set 2 | ν₃ |
| **12.28** | 24.4 | Set 3 | ν₃ |
| **14.00** | 21.4 | Set 4 | ν₃ |
| **14.07** | 21.3 | Set 1 | ν₃ |

**12 distinct frequencies** spanning 0.82–14.07 THz
(wavelengths 21–365 μm).  Sets 1 and 4 are nearly
degenerate; Sets 2 and 3 have similar ν₃ frequencies.
A scan across 0.8–14.5 THz covers all candidates.


## 3. The experiment

### 3.1 Source

A tritium sample (³H).  Tritium undergoes beta decay with
a well-characterized half-life of 12.32 years (decay rate
~1.78 × 10⁻⁹ s⁻¹ per atom).  It is used in KATRIN and
many other precision experiments.  The endpoint energy is
18.6 keV — low enough that the electron spectrum is
sensitive to neutrino mass effects.

**Why tritium:**
- Simplest beta emitter (superallowed transition)
- Half-life measured to 0.04% precision
- Available commercially in sealed sources
- Extensively characterized by KATRIN collaboration

**Alternative:** ⁶³Ni (half-life 100 years, endpoint 67 keV)
or ²⁴¹Pu (half-life 14.3 years, endpoint 21 keV).  Longer
half-lives mean lower count rates but more stable baselines.

### 3.2 THz cavity

The tritium sample sits inside a resonant cavity tuned to
the test frequency.  The cavity serves two purposes:

1. **Build up field strength** — a high-Q cavity at frequency
   f stores energy, amplifying the field at the sample beyond
   what the source alone provides.

2. **Ensure frequency precision** — the cavity resonance is
   narrow, guaranteeing that the field at the sample is at
   the intended frequency and not a broad continuum.

At THz frequencies, Fabry-Pérot cavities using metal mesh
reflectors or dielectric mirrors can achieve Q factors of
10²–10⁴.  The cavity length is adjusted to resonate at
each target frequency in turn.

### 3.3 Detector

An electron counter (silicon surface-barrier detector,
plastic scintillator, or Si(Li) detector) surrounding the
sample.  The experiment counts total beta decay events per
unit time — it does not need energy resolution.  A simple
counting experiment with high statistics.

At typical laboratory tritium activities (~GBq), count
rates of ~10⁹ decays/s are achievable.  Statistical
precision of 10⁻⁵ (10 ppm) is reached in ~10¹⁰ counts
(~10 seconds).  Systematic precision (temperature
stability, detector efficiency drift) is the limiting
factor, not statistics.

### 3.4 Protocol

**For each of the 12 target frequencies:**

1. Tune cavity to test frequency.  Verify with wavemeter.
2. Record baseline decay rate for 1 hour (THz off).
3. Turn on THz source.  Record decay rate for 1 hour.
4. Turn off THz source.  Record decay rate for 1 hour.
5. Repeat steps 2–4 for 10 cycles (on/off/on/off...).
6. Compute: ΔR = (rate_on − rate_off) / rate_off.
7. Detune cavity by 10% (off-resonance control) and repeat.

**Additional controls:**
- Run the full protocol with cavity empty (no tritium) to
  verify zero count-rate artifact from the THz source
- Run with THz power but cavity blocked (sample not
  illuminated) to check for electrical interference
- Sweep continuously across 0.5–15 THz in coarse steps
  (0.1 THz) to look for ANY rate anomaly, not just at
  predicted frequencies

### 3.5 What to look for

| Observation | Meaning |
|---|---|
| ΔR > 0 at a predicted frequency, ΔR = 0 off-resonance | Stimulated beta decay at a neutrino mode |
| ΔR < 0 at a predicted frequency | Suppressed decay (driven field interferes destructively) |
| ΔR ≠ 0 at ALL frequencies | Systematic artifact (THz heating, electrical pickup) |
| ΔR = 0 everywhere | No EM-to-neutrino coupling at this sensitivity |
| ΔR ≠ 0 at a frequency NOT in the table | Unknown resonance — possibly a mode not in the R49 survey |


## 4. Predicted outcome (MaSt)

If the neutrino sheet couples to EM radiation through the
lattice substrate:

- **Rate change at one (or more) of the 12 frequencies.**
  The magnitude of ΔR is unknown — it depends on the
  coupling strength (suppressed by at least α, possibly
  α²).  Even ΔR ~ 10⁻⁶ (1 ppm) would be detectable
  with sufficient integration.

- **The resonance is narrow.**  The mode on the sheet has a
  specific frequency; detuning by a few percent should
  eliminate the effect.  This distinguishes it from thermal
  or broadband artifacts.

- **The positive frequency identifies the correct triplet.**
  If a resonance appears at 7.06 THz but not at 1.23 THz,
  Set 1 (Family A, ε_ν = 5.0) is confirmed.  This
  simultaneously determines the neutrino sheet aspect
  ratio, the absolute neutrino masses, and the correct
  mode assignment — all from a tabletop experiment.


## 5. Null outcome

No rate change at any of the 12 frequencies at the achieved
sensitivity.  This constrains:

- The EM-to-neutrino coupling strength: if ΔR < 10⁻⁶ at
  power P, the coupling is below a calculable threshold.
- All 22 triplets equally (since all were tested).
- But does NOT rule out MaSt — the coupling could exist but
  be too weak for this method.  L01 and L02 test the same
  coupling through different observables and may have
  different sensitivity.


## 6. What a positive result would mean

A confirmed resonance at a predicted frequency would:

1. **Pin the absolute neutrino mass.**  The resonant
   frequency directly gives the mass eigenstate energy.
   No other experiment (KATRIN, cosmology, oscillation)
   provides this with comparable directness.

2. **Determine the neutrino sheet geometry.**  The matching
   frequency set uniquely identifies ε_ν and the mode
   quantum numbers, collapsing the 22-solution degeneracy
   to 1.

3. **Confirm EM-to-neutrino coupling.**  The Standard Model
   predicts zero effect.  Any nonzero ΔR at a predicted
   frequency and zero ΔR off-resonance is evidence for a
   coupling channel not present in the Standard Model.

4. **Establish the MaSt energy scale.**  The resonant
   frequency gives E₀ = ℏc/L₄, fixing the neutrino sheet
   size to a specific value in μm.

5. **Open the door to neutrino-sheet engineering.**  If the
   coupling is strong enough to modify decay rates, it may
   be strong enough for the loading applications explored
   in L02 (threshold-mediated nuclear events).


## 7. Equipment and cost

This experiment shares equipment with L01.  The additional
requirements are modest:

| Item | Purpose | Cost |
|---|---|---|
| Tritium source (sealed, ~GBq) | Beta emitter | $1–5K |
| Si surface-barrier detector | Electron counting | $2–5K |
| Counting electronics (MCA + scaler) | Pulse processing | $5–10K |
| THz source (DFG or QCL) | From L01 | (shared) |
| Fabry-Pérot cavity (adjustable) | Resonant field enhancement | $5–15K |
| Frequency reference / wavemeter | Verify THz frequency | $5–10K |
| Shielding (lead + mu-metal) | Reduce background counts | $2–5K |

**Incremental cost beyond L01:** ~$20–50K
**Standalone cost:** ~$170–400K (includes THz source)

### 7.1 THz source requirements

The consolidated frequency list spans 0.82–14.07 THz.  No
single source covers this range optimally:

| Range | Best source | Notes |
|---|---|---|
| 0.8–3 THz | QCL or photomixer | Sets 2, 3 low-frequency modes |
| 3–8 THz | DFG (GaSe or GaP) | Sets 1, 4 (the ~7 THz modes) |
| 8–15 THz | DFG or CO₂-pumped FIR laser | All ν₃ candidates |

A DFG system with GaSe crystal covers ~1–30 THz and is the
most versatile single source.  Supplementing with a QCL
improves power below 3 THz.


## 8. Experimental schedule

| Phase | Duration | Activity |
|---|---|---|
| 1 | 2 months | Equipment setup, cavity characterization |
| 2 | 1 month | Baseline decay rate measurement (THz off) |
| 3 | 3 months | Scan all 12 frequencies (1 week each + controls) |
| 4 | 1 month | Follow-up on any candidates (fine frequency scan) |
| 5 | 1 month | Analysis and writeup |

**Total: ~8 months from equipment delivery to result.**


## 9. Relation to other experiments

| Experiment | What it tests | Observable |
|---|---|---|
| **L04 (this)** | EM coupling to neutrino modes | Beta decay rate change |
| L01 | EM coupling to neutrino modes | Persistent THz spectral feature |
| L02 | Energy loading through neutrino window | Nuclear events in deuterium |
| L03 | Neutrino scaffold emission | Up-converted THz from biological tissue |
| KATRIN | Absolute neutrino mass | Tritium endpoint spectrum shape |

L04 and L01 test the same coupling through different
observables.  L04 has the advantage of binary signal
(rate change yes/no) and enormous statistics (10⁹
counts/s).  L01 has the advantage of spectral specificity
(feature at exact frequency).  A positive result in either
would motivate the other immediately.

If L04 identifies the correct frequency set, L02 can be
tuned to exactly that frequency for maximum loading
efficiency — removing the frequency uncertainty that is
L02's main practical obstacle.
