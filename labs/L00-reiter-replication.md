# L00: Independent Replication of the Unquantum Beam-Split Coincidence Experiment

**Status:** Proposed
**Objective:** Independently replicate the gamma-ray and alpha-ray
  beam-split coincidence experiments reported by Eric S. Reiter.
**Source paper:** Reiter, E.S. "New Experiments Call for a Continuous
  Absorption Alternative to Quantum Mechanics — The Unquantum Effect."
  *Progress in Physics*, Vol. 10, Issue 2, pp. 82–88 (2014).
**Additional references:**
  Reiter, E.S. "Photon Violation Spectroscopy." viXra:1203.0094 (2012).
  Reiter, E.S. "A Serious Challenge to Quantization." viXra:1203.0092 (2012).
  Reiter, E.S. "Particle Violation Spectroscopy." viXra:1204.0032 (2012).

---

## Background

In a standard beam-split coincidence test, a single quantum
(photon or particle) is directed at a beam splitter.  Two
detectors measure coincident arrivals.  Quantum mechanics
predicts that a single quantum cannot trigger both detectors
simultaneously; the only coincidences should be accidental
(two independent quanta arriving within the coincidence
window).  The expected accidental coincidence rate is:

    Rc = R₁ × R₂ × τ

where R₁ and R₂ are the singles rates of each detector and
τ is the coincidence time window.

All prior beam-split coincidence tests (Givens 1946, Brannen
& Ferguson 1956, Clauser 1974, Grainger et al. 1986) used
visible light or x-rays and measured Re/Rc ≈ 1, confirming the
quantum prediction.

Reiter (2014) performed this test with gamma rays and alpha
rays.  He reports coincidence rates far exceeding chance:

| Experiment | Source | Re/Rc |
|------------|--------|-------|
| Cd-109 tandem | 88 keV γ | 33.5 |
| Na-22 triple coincidence | 511 keV γ | 963 |
| Am-241 alpha split | 5.5 MeV α | 105 |

These results, if reproducible, would contradict the single-
quantum prediction of quantum mechanics.  No independent
replication has been published.

---

## Tracks

| # | Name | Objective | Depends on |
|---|------|-----------|------------|
| 1 | Cd-109 tandem coincidence | Replicate Reiter's core γ-ray result (Re/Rc ≫ 1) | — |
| 2 | Sensitivity studies | Measure response to coincidence window, SCA window, source chemistry, and temperature | Track 1 |
| 3 | Na-22 triple coincidence | Replicate the strongest reported signal (Re/Rc = 963) | Track 1 |
| 4 | Beam-split geometry | Replace tandem with scattering-target geometry | Track 1 |
| 5 | Alpha-ray split | Extend to matter waves (He-4 nucleus) | Track 1 |

---

# Track 1: Cd-109 Tandem Coincidence

This is the core experiment.  It reproduces the setup described
in Reiter (2014) §2 and Reiter (2012, viXra:1203.0094) Fig. 6.

## 1.1 Claim under test

A single 88 keV gamma ray emitted by Cd-109 decay can trigger
coincident detections in two detectors arranged in tandem, at
a rate far exceeding the accidental chance rate.

## 1.2 Geometry

```
   ┌──────────┐     ┌──────────────┐     ┌──────────────────┐
   │  Cd-109  │     │ Detector #1  │     │   Detector #2    │
   │  source  │ ──► │ (thin, 4 mm) │ ──► │ (thick, 1.5 in)  │
   │  in Sn   │     │   NaI(Tl)    │     │    NaI(Tl)       │
   │collimator│     │              │     │                  │
   └──────────┘     └──────┬───────┘     └───────┬──────────┘
                           │                     │
                      Shaping amp           Shaping amp
                           │                     │
                         SCA #1                SCA #2
                           │                     │
                           └─────┬───────────────┘
                                 │
                          Coincidence unit
                                 │
                           Counter / DSO
```

"Tandem geometry": the source illuminates the thin front
detector.  The front detector partially absorbs the gamma;
the remainder passes through to the thick rear detector.
Both detectors are enclosed in a lead shield.

## 1.3 What Reiter measured

With the setup described above:

- Singles rate, detector #1: R₁ = 291/s
- Singles rate, detector #2: R₂ = 30/s
- Coincidence window: τ = 185 ns
- Chance coincidence rate: Rc = R₁ × R₂ × τ = 0.0016/s
- Background (no source, 40.1 ks): 0.0004/s
- Measured coincidence rate: Re = 295/5500s − 0.0004/s = 0.053/s
- **Result: Re/Rc = 33.5**

## 1.4 Procedure

### Step 1: Detector calibration

Place the Cd-109 source directly in front of each detector
individually.  Record the pulse-height spectrum on the MCA.
Identify the 88 keV photopeak.

Set each SCA window:
- Lower level (LL): ~2/3 of the photopeak centroid (~59 keV
  equivalent pulse height)
- Upper level (UL): ~4/3 of the photopeak centroid (~117 keV
  equivalent pulse height)

This window accepts only events consistent with full-energy
absorption of the 88 keV gamma.  It rejects:
- Compton-scattered photons (lower energy)
- NaI fluorescence x-rays (~30 keV, iodine K-edge)
- Noise

Record the photopeak centroid, FWHM, and SCA window settings
for each detector.  Verify that the SCA passes ~80–90% of the
photopeak events and rejects events below 59 keV.

### Step 2: Background measurement

Remove all sources.  Run in tandem geometry (both detectors
in position, lead shield closed) for ≥10 hours.  Record:
- Background singles rate for each detector
- Background coincidence rate
- MCA spectrum for each detector (to check for unexpected
  environmental peaks)

Expected background coincidence rate: < 0.001/s (dominated by
cosmic rays at ~1/min/cm²).

### Step 3: Single-emission verification (facing geometry)

Place the Cd-109 source between the two detectors, with
detectors facing each other to cover close to 4π solid angle.
Measure coincidence rate for ≥2 hours.

Expected: Re/Rc ≈ 1.  This confirms that Cd-109 emits only
one gamma per decay event.  If Re/Rc > 1 in this geometry,
the source may be contaminated or the electronics have
cross-talk.

### Step 4: Tandem coincidence measurement

Assemble the tandem geometry:
1. Place Cd-109 source in tin collimator.
2. Position collimator directly in front of detector #1
   (thin crystal).
3. Position detector #2 (thick crystal) directly behind
   detector #1, as close as possible.
4. Close lead shield around the assembly.

Set coincidence window τ = 185 ns.

Record for ≥2 hours:
- Singles rates R₁ and R₂ (from counters)
- Coincidence rate Re (from coincidence unit → counter)
- Δt histogram on DSO (time difference between coincident
  pulses)
- Pulse-height histograms on DSO for both channels

Compute:
- Rc = R₁ × R₂ × τ
- Re (corrected for background from Step 2)
- Re/Rc

**Reiter's claim is replicated if Re/Rc ≫ 1.**

### Step 5: DSO pulse verification

For every coincident event, examine the analog pulse shapes
on the DSO.  Verify:
- Both pulses are well-shaped (smooth rise, exponential
  decay, consistent with scintillation pulses)
- No misshapen pulses (double pulses, truncated pulses,
  or pulses from electronic ringing)
- The fraction of misshapen pulses is < 1%

This rules out electronic artifacts, pile-up, and PMT
anomalies as explanations for excess coincidences.

### Step 6: Δt histogram analysis

From the DSO, plot the time-difference histogram between
coincident pulses.  Expected features:
- A peak near Δt = 0 (genuine coincidences)
- A flat background (accidental coincidences)

If Re/Rc ≫ 1, the peak at Δt = 0 should be prominent above
the flat background.  The width of the peak indicates the
timing resolution of the system.

## 1.5 Expected results

| Outcome | Interpretation | Action |
|---------|---------------|--------|
| Re/Rc ≫ 1 (e.g. 10–50) | Reiter's core result replicated | Proceed to Tracks 2–5 |
| Re/Rc ≈ 1 | Result not replicated | Review systematics; consult Reiter's detailed protocols; attempt with different detector/source |
| 1 < Re/Rc < 5 | Ambiguous; possible small effect or systematic | Increase measurement time; vary geometry; investigate artifacts |

## 1.6 Potential artifacts

| Artifact | Mechanism | How it is controlled |
|----------|-----------|---------------------|
| Pile-up | Two independent gammas arrive within τ | This IS the chance rate Rc; Re/Rc ≫ 1 rules it out by definition |
| Compton scatter | Gamma Compton-scatters in detector #1; scattered photon enters detector #2 | SCA rejects scattered photons (they have lower energy than 88 keV); LL at 59 keV excludes them |
| Iodine fluorescence | 88 keV gamma ejects iodine K-shell electron in detector #1; fluorescence x-ray (~30 keV) enters detector #2 | 30 keV is well below LL (59 keV); rejected by SCA |
| Cosmic rays | Cosmic muon traverses both detectors | Background subtraction (Step 2); rate is ~1/min/cm², orders below expected Re |
| PMT afterpulsing | PMT in detector #1 fires, electrical afterpulse triggers PMT in detector #2 | Detectors are separate assemblies with no shared electronics; DSO pulse-shape verification (Step 5) |
| Electrical cross-talk | Signal from channel 1 leaks into channel 2 via shared cables or ground loops | Separate amplifier and SCA units per channel; shielded cables; verify with electronic pulser (trigger one channel, confirm no response on other) |
| Source contamination | Cd-109 sample contains other isotopes that emit multiple gammas | Check singles spectrum on MCA for unexpected peaks; Cd-109 should show only the 88 keV peak and low-energy Ag x-rays |

---

# Track 2: Sensitivity Studies

*Requires:* Track 1 produces Re/Rc ≫ 1.

These measurements reproduce the sensitivity findings
reported by Reiter in viXra:1203.0094.

## 2.1 Coincidence window variation

Repeat the Track 1 tandem measurement with different
coincidence windows:

    τ = 50, 100, 185, 200, 500, 1000 ns

Record Re and compute Re/Rc for each τ.

**Expected (if effect is real):** Re/Rc should be roughly
constant across τ values, because the coincident events are
genuinely simultaneous (Δt ≈ 0).  The absolute coincidence
count increases with τ (wider window catches more accidentals
too), but the ratio Re/Rc should be stable.

**Expected (if artifact):** Re/Rc depends on τ, suggesting the
excess coincidences are time-smeared rather than simultaneous.

## 2.2 SCA window variation

Repeat the Track 1 tandem measurement with different SCA
lower-level settings:

    LL = 1/2, 2/3, 3/4, 5/6 of photopeak centroid

Record Re/Rc for each LL setting.

**Expected:** Re/Rc ≫ 1 at all LL settings, including the
strictest (5/6).  This rules out energy down-conversion as an
explanation — if the coincidences were due to a single gamma
splitting its energy between two detectors (half-energy in
each), a strict SCA window would reject them.

Reiter's key argument: the SCA window must be set high enough
that BOTH detectors record full-energy (or near-full-energy)
pulses.  This is only possible if the detectors had
sub-threshold energy already present.

## 2.3 Source chemical state

Prepare Cd-109 in two chemical forms:

- **Salt form:** Evaporate a Cd-109 isotope solution on a
  substrate.  The cadmium forms a crystalline salt.
- **Metal form:** Electroplate Cd-109 from solution onto the
  end of a platinum wire.

Using the same tandem geometry and electronics, measure Re/Rc
for each source form.

**Expected (Reiter's finding):** The salt (crystalline) form
produces approximately 5× more coincidences than the metal
form.  The conventional singles spectrum (MCA photopeak shape,
centroid, count rate) shows no measurable difference between
the two forms.

This finding is significant because:
- It cannot be explained by any electronic or geometric
  artifact (the electronics and geometry are unchanged)
- It demonstrates sensitivity to the source's solid-state
  structure
- It has no explanation in standard quantum mechanics

## 2.4 Temperature variation

Place an aluminum slab between the source and detector #1
(beam-split geometry; see Track 4).  Measure Re/Rc with:

- Aluminum at room temperature
- Aluminum cooled to 77 K (liquid nitrogen)

**Expected (Reiter's finding):** The LN₂-cooled aluminum
produces approximately 50% more coincidences than room-
temperature aluminum.

## 2.5 Distance variation

Vary the source-to-detector distance while maintaining tandem
geometry.  Test at 2, 5, 10, and 20 cm source-to-detector #1
distance.  Record Re/Rc at each distance.

**Expected (Reiter's finding):** The effect depends on the
ratio between the gamma wavelength and the spreading area of
the classical wave cone at the detector.  Longer-wavelength
sources (Am-241, 59.6 keV) show enhanced effect at closer
range; shorter-wavelength sources (Cs-137, 662 keV) show
enhanced effect at greater range.

---

# Track 3: Na-22 Triple Coincidence

*Requires:* Track 1 produces Re/Rc ≫ 1.

This replicates the experiment described in Reiter (2012,
viXra:1204.0032) which produced the strongest reported signal.

## 3.1 Principle

Na-22 decays by positron emission.  The positron annihilates
with an electron, producing two back-to-back 511 keV gamma
rays.  Na-22 also emits a 1.275 MeV gamma in the same decay.

The 1.275 MeV gamma is caught by a third detector as a timing
tag.  One of the two 511 keV annihilation gammas is directed
into a tandem detector pair.

The triple-coincidence chance rate is:

    Rc = R₁ × R₂ × R₃ × τ₁₂ × τ₂₃

## 3.2 Geometry

```
                              Detector #3
                           (1.275 MeV tag)
                                 ▲
                                 │
   ┌──────────┐     ┌───────────┼───────────┐
   │Detector#1│ ◄── │        Na-22          │ ──► │Detector#2│
   │  (thin)  │     │        source         │     │ (thick)  │
   │ NaI(Tl)  │     └───────────────────────┘     │ NaI(Tl)  │
   └──────────┘           tandem pair              └──────────┘
```

Detectors #1 and #2 are in tandem on one side of the source
to catch one of the 511 keV annihilation gammas.  Detector #3
is positioned to catch the 1.275 MeV gamma (or the opposite
511 keV gamma, depending on geometry).

## 3.3 Procedure

1. Calibrate all three detectors on their respective
   photopeaks (511 keV for #1 and #2; 1.275 MeV for #3).
2. Set SCA windows appropriately for each detector.
3. Record singles rates R₁, R₂, R₃.
4. Record triple-coincidence rate Re.
5. Compute Rc = R₁ × R₂ × R₃ × τ₁₂ × τ₂₃.
6. Compute Re/Rc.

## 3.4 Expected result

Reiter reports Re/Rc = 963 — the largest ratio in any of his
experiments.  The higher energy (511 keV vs. 88 keV) and
triple-coincidence requirement make this the most dramatic
test.

---

# Track 4: Beam-Split Geometry

*Requires:* Track 1 produces Re/Rc ≫ 1.

This replicates the scattering-target experiments described in
Reiter (2012, viXra:1203.0094) §4 and Figs. 12–18.

## 4.1 Principle

Instead of tandem geometry (thin detector as passive
splitter), a scattering target (metal or crystal) deflects
part of the gamma beam to a side detector.  The undeflected
remainder continues to a forward detector.

This is analogous to an optical beam splitter and allows
independent control of the split material.

## 4.2 Geometry

```
                       Detector #2
                       (scattered)
                            ▲
                           ╱
                          ╱ scattered γ
                         ╱
   ┌──────────┐     ┌───────┐     ┌───────────┐
   │  Cd-109  │ ──► │Target │ ──► │Detector #1│
   │  source  │     │(Al,Si,│     │(transmitted│
   │          │     │ or Ge)│     │    γ)      │
   └──────────┘     └───────┘     └───────────┘
```

## 4.3 Procedure

1. Position scattering target (aluminum slab, silicon
   crystal, or germanium crystal) in the beam path.
2. Position detector #1 behind the target (transmitted beam).
3. Position detector #2 at a scattering angle (e.g. 30°, 60°,
   90°) from the beam axis.
4. Calibrate SCA windows on each detector.
5. Record singles rates and coincidence rate.
6. Compute Re/Rc.

Test multiple target materials and scattering angles.

## 4.4 Crystal orientation (if using single-crystal targets)

For silicon or germanium single-crystal targets, repeat the
measurement at different crystal orientations (rotate the
crystal in the beam).  Record Re/Rc vs. crystal angle.

**Expected (Reiter's finding):** The coincidence rate varies
with crystal orientation, revealing a new form of
crystallography.  Reiter reports this is distinct from Bragg
diffraction — the periodicity corresponds to structures
smaller than inter-atomic distance.

## 4.5 Spectroscopic analysis

Using the MCA, record the full pulse-height spectrum of
detector #2 (scattered beam) for each target material.

- A non-shifted spectral peak indicates elastic (Rayleigh)
  scattering.
- A shifted spectral peak indicates inelastic (Compton)
  scattering.

Reiter used this as a spectroscopic technique ("Photon
Violation Spectroscopy") to characterise scatterer properties.

---

# Track 5: Alpha-Ray Split

*Requires:* Track 1 produces Re/Rc ≫ 1.

This replicates the alpha-ray experiments described in Reiter
(2014) §3 and viXra:1204.0032.

## 5.1 Principle

Am-241 emits a single 5.5 MeV alpha particle per decay.  If
the alpha is a classical matter wave (not an indivisible
particle), it could split at a target and trigger coincident
detections in two detectors.  Quantum mechanics predicts only
accidental coincidences.

The alpha split is significant because it extends the test from
electromagnetic radiation (gammas) to matter waves (helium
nuclei).  A helium nucleus requires ~7 MeV per nucleon to
break apart; at 5.5 MeV total kinetic energy, there is not
enough energy for conventional nuclear splitting.

## 5.2 Geometry

```
   ┌──────────┐     ┌─────────┐     ┌───────────┐
   │  Am-241  │ ──► │  Gold   │ ──► │Detector #2│
   │  source  │     │  leaf   │     │  (Si SBD) │
   └──────────┘     │(splitter│     └───────────┘
                    └────┬────┘
                         │ reflected α
                         ▼
                    ┌───────────┐
                    │Detector #1│
                    │  (Si SBD) │
                    └───────────┘

   (All inside vacuum chamber)
```

## 5.3 Procedure

1. Mount Am-241 source and two silicon surface-barrier
   detectors (SBDs) in a vacuum chamber.
2. Place two layers of 24-carat gold leaf over the front face
   of detector #2.  The gold leaf acts as the beam splitter.
3. Position Am-241 source to illuminate the gold leaf from
   the side, shaded from detector #1.
4. Evacuate chamber.
5. Set SCA lower level to 1/3 of the characteristic alpha
   pulse height.  (Reiter found that alpha splits usually
   maintain particle-energy conservation — most coincident
   pulse pairs show half-height pulses in each detector.)
6. Set coincidence window τ = 100 ns.

**Control measurement:** Position the two detectors at right
angles to each other with the source centred between them.
Measure coincidence rate for ≥2 hours.  Expected: only the
chance rate (confirms single alpha emission per decay).

**Split measurement:** Assemble beam-split geometry with gold
leaf.  Record singles and coincidence rates.  Record pulse-
height pairs for all coincident events.

7. Compute Re/Rc.
8. Plot coincident pulse-height pairs as a 2D scatter plot
   (detector #1 pulse height vs. detector #2 pulse height).
   Identify events where both pulses exceed half the
   characteristic alpha energy — these would violate
   particle-energy conservation.

## 5.4 Expected result

Reiter reports Re/Rc = 105 with gold leaf.  Six coincident
events exceeded particle-energy conservation (both detectors
above half-energy).  Counting only these six events still
gives Re/Rc = 3.97, which independently contradicts the
single-particle prediction.

---

# Equipment and Supplies

## Bill of materials — Tracks 1–2

These items are sufficient for the core replication (Track 1)
and sensitivity studies (Track 2).

### Radioactive sources

| Item | Specification | Supplier examples | Est. cost |
|------|--------------|-------------------|-----------|
| Cd-109 sealed source | ~1 μCi, license-exempt | Spectrum Techniques (#CD1U), Eckert & Ziegler | $50–200 |
| Cd-109 solution (Track 2.3) | ~0.5 μCi in HCl solution, for chemical-state preparation | Eckert & Ziegler custom order | $200–500 |

All sources are low-level, license-exempt under NRC 10 CFR
30.71 Schedule B (< 10 μCi for Cd-109).

### Detectors

| Item | Specification | Supplier examples | Est. cost |
|------|--------------|-------------------|-----------|
| Detector #1 — thin NaI(Tl) | 3–5 mm thick × 40 mm diameter NaI(Tl) crystal coupled to PMT; requires custom order | Saint-Gobain (custom), Hilger Crystals, Scionix | $1,500–3,000 |
| Detector #2 — standard NaI(Tl) | 1.5" or 2" diameter × 2" thick NaI(Tl), integrated with PMT | Ortec 905 series, Saint-Gobain 2M2/2, Scionix 38B51/2M-E1 | $2,000–4,000 |
| HV power supply (2 channels) | 0–2000 V DC, NIM standard | Ortec 556, CAEN N470A | $1,000–2,500 |

### Signal processing electronics (NIM standard)

| Item | Specification | Qty | Supplier examples | Est. cost (each) |
|------|--------------|-----|-------------------|-----------------|
| Shaping amplifier | Gaussian shaping, 0.5–10 μs shaping time | 2 | Ortec 572A, CAEN N568B | $800–1,500 |
| Single-channel analyzer (SCA) | Adjustable LL and UL window, NIM output | 2 | Ortec 550A, Ortec 551, CAEN N845 | $500–1,000 |
| Coincidence unit | 2+ inputs, adjustable resolving time τ (50–1000 ns) | 1 | Ortec 414A, CAEN N455 | $500–1,000 |
| Counter/scaler | ≥1 channel, gated input | 3 | Ortec 994, CAEN N1145 | $400–800 |
| NIM crate + power supply | Standard NIM bin, ±6V, ±12V, ±24V | 1 | Ortec 4001C + 4002D, Wiener UEP6021 | $800–1,500 |

### Data acquisition

| Item | Specification | Supplier examples | Est. cost |
|------|--------------|-------------------|-----------|
| Multichannel analyzer (MCA) | ≥1024 channels, USB interface | Ortec EASY-MCA-2K, Amptek MCA-8000D | $1,500–3,000 |
| Digital storage oscilloscope | ≥4 channels, ≥100 MHz bandwidth, histogram software | Lecroy (any current 4-ch model), Tektronix MDO3000 series, Keysight DSOX3000 | $3,000–8,000 or use existing lab scope |

### Shielding and mechanical

| Item | Specification | Est. cost |
|------|--------------|-----------|
| Lead bricks | 2" × 4" × 8", sufficient to build enclosure ~12" × 12" × 12" (~20 bricks, ~250 kg) | $400–800 |
| Tin collimator | Custom-machined tin cylinder with aperture; or tin sheet wrapped into tube, ~2 cm ID × 3 cm length | $50–100 (machine shop) |
| Detector mounting | Optical rail or custom bracket to hold detectors in tandem alignment | $100–300 |
| BNC cables | 50 Ω, various lengths | $50–100 |

### Consumables (Track 2.3, chemical state preparation)

| Item | Specification | Est. cost |
|------|--------------|-----------|
| Platinum wire | ~1 mm diameter, ~5 cm length, for electroplating | $30–80 |
| Substrate for salt preparation | Glass slide or ceramic dish | < $10 |
| Electroplating supplies | DC power supply (0–5 V, 0–1 A), beaker, leads | $50–100 (or use existing lab supply) |

### Budget summary — Tracks 1–2

| Scenario | Estimated total |
|----------|----------------|
| Purchase all new equipment | $13,000–30,000 |
| University lab (most NIM equipment available) | $2,000–5,000 (sources + custom thin detector) |
| Facility with existing nuclear spectroscopy setup | $500–1,500 (sources only) |

## Additional equipment — Track 3

| Item | Specification | Est. cost |
|------|--------------|-----------|
| Na-22 sealed source | ~1 μCi, license-exempt | $100–300 |
| Third NaI(Tl) detector + HV | 2" standard assembly | $2,000–4,000 |
| Additional SCA + amplifier + counter | One more NIM channel | $1,700–3,300 |

## Additional equipment — Track 4

| Item | Specification | Est. cost |
|------|--------------|-----------|
| Aluminum slab | ~5 mm thick, ~50 mm square, high purity | $20–50 |
| Silicon single crystal | ~5 mm thick, ~25 mm diameter, polished faces | $50–200 |
| Germanium single crystal | ~5 mm thick, ~25 mm diameter, polished faces | $100–300 |
| Rotation stage | Manual goniometer for crystal orientation | $200–500 |
| Liquid nitrogen + dewar (Track 2.4 / 4) | Standard lab supply | $50–100 per fill |

## Additional equipment — Track 5

| Item | Specification | Est. cost |
|------|--------------|-----------|
| Am-241 sealed source | ~1 μCi, license-exempt (also emits 59.6 keV γ, usable in Tracks 1–2) | $50–200 |
| Silicon surface-barrier detectors (SBDs) | 2 units, ~300 mm² active area, ~100 μm depletion depth | $1,000–2,000 each |
| Charge-sensitive preamplifiers | 2 units, matched to SBDs | $500–1,000 each |
| Vacuum chamber | ~30 cm diameter bell jar or cube, with feedthroughs for 4 BNC + HV | $2,000–5,000 |
| Vacuum pump | Rotary vane, ~10⁻² torr sufficient | $1,000–2,000 (or use existing) |
| Gold leaf | 24-carat, standard booklet (~80 mm square sheets, ~100 nm thick) | $30–60 |

## Budget summary — all tracks

| Scope | Estimated total (new purchase) | With existing lab |
|-------|-------------------------------|-------------------|
| Track 1 only | $13,000–30,000 | $500–5,000 |
| Tracks 1–2 | $13,500–31,000 | $700–5,500 |
| Tracks 1–4 | $17,000–39,000 | $1,500–7,000 |
| All tracks (1–5) | $22,000–48,000 | $4,000–12,000 |

---

# Statistical Analysis

## Primary metric

For each measurement, the primary metric is the coincidence
ratio:

    Re/Rc = (measured coincidence rate − background rate) /
            (R₁ × R₂ × τ)

## Significance threshold

The null hypothesis is Re/Rc = 1 (standard quantum mechanics).
To claim rejection of the null at 5σ:

    (Re − Rc) / √Re ≥ 5

At Reiter's rates (Re ≈ 0.053/s, Rc ≈ 0.0016/s), this
requires ≥25 coincidence events, achievable in ~8 minutes.

For conservative analysis, collect data for ≥2 hours per
measurement to accumulate ~380 coincidence events (if
Reiter's rates hold), giving statistical uncertainty of
±5% on Re/Rc.

## Systematic uncertainty

The dominant systematic is the measurement of R₁, R₂, and τ
that enter the Rc calculation.  These are measurable to < 1%
with standard NIM electronics.

The SCA window calibration contributes a systematic through
the acceptance fraction.  Record the MCA spectrum and the SCA
pass rate to quantify this.

---

# Data Deliverables

For each track, record and report:

1. **MCA spectra** — Full pulse-height spectra for each
   detector, with and without source, with SCA window
   boundaries marked.

2. **Singles rates** — R₁ and R₂ for each detector, with
   statistical uncertainty.

3. **Coincidence rate** — Re with statistical uncertainty,
   and the computed chance rate Rc.

4. **Δt histogram** — Time-difference distribution of
   coincident events, showing peak structure (if any) and
   flat accidental background.

5. **Pulse-shape gallery** — DSO screen captures of ≥20
   representative coincident pulse pairs, demonstrating
   pulse quality.

6. **Re/Rc ratio** — With propagated statistical and
   systematic uncertainties.

7. **Raw data files** — All counter readings, timestamps,
   and DSO data in machine-readable format.

---

# Feasibility Assessment

| Factor | Assessment |
|--------|-----------|
| Equipment | Standard nuclear physics teaching lab instrumentation (NIM) |
| Regulatory | All sources license-exempt at specified activities |
| Expertise required | Competence in nuclear spectroscopy; undergraduate or technician level |
| Time to first result | Track 1: ~1 week (including setup and calibration) |
| Time for all tracks | ~2 months |
| Lab space | Standard radiation bench with ventilation; no special facility required |
| Safety | Standard sealed-source handling procedures; lead shielding; dosimetry badges |
| Replication value | No independent replication of Reiter's results has been published; extremely high scientific value regardless of outcome |
