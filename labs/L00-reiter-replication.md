# L00: Threshold Absorption — Replication and Characterisation

**Status:** Proposed — prerequisite for all storage experiments
**Tests:** Threshold model (continuous absorption, quantized emission)
**T⁶ sheet:** Electron T² (88 keV gamma ≈ 17% of the 511 keV
  electron-mass threshold)
**Source paper:** Reiter, E.S. "New Experiments Call for a Continuous
  Absorption Alternative to Quantum Mechanics — The Unquantum Effect."
  *Progress in Physics*, Vol. 10, Issue 2, pp. 82–88 (2014).
**Related:** [storage-in-t6](../papers/storage-in-t6.md) §3
  (threshold theory foundation)

---

## 0. Why this comes first

The entire compact-dimension storage hypothesis rests on two
pillars: the T⁶ geometry model and Reiter's threshold model.
If threshold absorption is not real — if energy is truly
quantized at absorption, not just at emission — then
sub-threshold storage in compact-dimension modes is impossible
by definition.  Reiter's experiment has not been independently
replicated.  Before investing in THz write/read experiments
(L01), we should establish whether the foundational claim
survives independent scrutiny.

**Note on T⁶ sheet assignment:** The 88 keV gammas interact with
detector atoms via the photoelectric effect — coupling to atomic
electrons.  In T⁶ language, the sub-threshold pre-loaded state
is energy sitting in electron-T² modes.  The electron T²
fundamental mode is at 511 keV (m_e c²), so 88 keV is deeply
sub-threshold.  All tracks in this lab operate on the electron
T².  The neutrino T² (mode energies ~6–90 meV, THz frequencies)
is unreachable with gamma-ray equipment — that requires L01.

---

## Tracks

| # | Name | Question | Depends on |
|---|------|----------|------------|
| 1 | Tandem replication | Does Re/Rc ≫ 1 reproduce? | — |
| 2 | Pre-load persistence | How long does the pre-loaded state survive? | Track 1 |
| 3 | Controlled write/read | Can we load a known energy and read it back? | Track 2 |
| 4 | Geometry and source variants | Beam-split, Na-22 triple, alpha split | Track 1 |

---

---

# Track 1: Tandem replication

## 1.1 Hypothesis

Energy absorption in matter is continuous (not quantized).
Detectors accumulate sub-threshold energy from previous
absorptions.  When a gamma ray is split between two detectors,
both detectors can fire simultaneously if each had accumulated
enough pre-loaded energy to reach threshold with only a partial
gamma — producing coincidence rates that exceed the chance
prediction of quantum mechanics.

## 1.2 Predicted outcome (threshold model)

Coincidence rate Re significantly exceeds the chance rate Rc:

    Re/Rc ≫ 1

Reiter reports Re/Rc = 33.5 for Cd-109 in tandem geometry, and
Re/Rc = 963 for Na-22 triple-coincidence.

## 1.3 Null outcome (standard QM)

    Re/Rc = 1

A single gamma photon goes to one detector or the other, never
both.  Coincidences occur only by chance (two independent
gammas arriving within the time window).

## 1.4 What Reiter did (reference protocol)

### 1.4.1 Gamma-ray beam-split (tandem geometry)

**Source:** Cd-109 (88 keV gamma, single emission per decay via
electron capture to stable Ag-109).  License-exempt activity
level.  Also tested: Co-57 (122 keV), Am-241 (59.6 keV),
Na-22 (511 keV pair-annihilation), Mn-54, Cs-137.

**Detectors:** Two NaI(Tl) scintillation crystals coupled to
photomultiplier tubes (PMTs):
- Detector #1 (front): custom 4 mm thick, 40×40 mm NaI(Tl)
- Detector #2 (behind): 1.5-inch Bicron NaI-PMT

"Tandem geometry": source → thin detector #1 → thick detector #2.
The thin front detector partially absorbs the gamma; the
remainder passes through to the thick rear detector.

**Shielding:** Lead enclosure reducing background rate by 31×.

**Electronics per channel:**
- Ortec 460 shaping amplifier
- Ortec 551 single-channel analyzer (SCA)
- HP 5334 counter (singles rate)
- Lecroy LT344 4-channel digital storage oscilloscope (DSO)
  with histogram software (pulse-height and Δt histograms)

**SCA window:** Lower level (LL) set to ~2/3 of the Cd-109
characteristic 88 keV pulse height.  This ensures both
detectors record only full-energy (or near-full-energy)
events — ruling out frequency down-conversion as an
explanation.

**Coincidence window:** τ = 185 ns.

**Key measurement:**
- Singles rates: R₁ = 291/s, R₂ = 30/s
- Chance rate: Rc = R₁ × R₂ × τ = 0.0016/s
- Background (no source): 0.0004/s
- Measured coincidence rate: Re = 295/5500s − 0.0004/s = 0.053/s
- **Result: Re/Rc = 33.5**

### 1.4.2 Additional findings from Reiter

- **Chemical state sensitivity:** Cd-109 in salt (crystalline)
  form produced 5× more coincidences than Cd-109 electroplated
  as metal onto platinum wire.  Conventional gamma spectroscopy
  showed no difference between the two forms.
- **Distance sensitivity:** Longer-wavelength gammas (Am-241)
  showed enhanced effect at closer range; shorter-wavelength
  (Cs-137) showed enhanced effect at greater range.
- **Temperature sensitivity:** Liquid-nitrogen-cooled aluminum
  beam splitter produced 50% more coincidences.
- **Crystal orientation:** Coincidence rate varied with crystal
  angle — a new form of crystallography distinct from Bragg
  diffraction.
- **Triple coincidence (Na-22):** Positron annihilation produces
  two 511 keV gammas.  Third detector catches the accompanying
  1.27 MeV gamma.  One of the two annihilation gammas was split
  in tandem.  Re/Rc = 963.
- **Alpha-ray split (Am-241):** 5.5 MeV alpha through gold leaf.
  Two silicon surface-barrier detectors.  Re/Rc = 105.  Six
  coincident pulse pairs exceeded particle-energy conservation
  (both pulses above half the characteristic alpha energy).

---

## 1.5 Replication protocol

### 1.5.1 Minimum viable replication

Reproduce the Cd-109 tandem-geometry gamma test with
off-the-shelf nuclear instrumentation.

**Source:**
- Cd-109 sealed source, ~1 μCi (license-exempt in most
  jurisdictions).  Available from Spectrum Techniques or
  Eckert & Ziegler.  ~$50–200.

**Detectors:**
- Detector #1: thin NaI(Tl) crystal, 3–5 mm thick, ~40 mm
  diameter, coupled to PMT.  Custom order from Saint-Gobain
  or Hilger Crystals.  ~$1,000–3,000.
- Detector #2: standard 1.5" or 2" NaI(Tl) detector assembly
  (e.g., Ortec 905 series or Saint-Gobain 2M2/2).  ~$2,000–4,000.

**Electronics:**
- 2× shaping amplifier (Ortec 572A or CAEN N568B)
- 2× single-channel analyzer (Ortec 550A or 551)
- Coincidence unit (Ortec 414A) with adjustable τ
- 2× counter/scaler (Ortec 994 or CAEN N1145)
- Multichannel analyzer or DSO for pulse-height verification
  (e.g., Ortec EASY-MCA or any 100+ MHz oscilloscope)

**Shielding:**
- Lead castle: 2" thick lead bricks surrounding the detector
  assembly.  Available from nuclear lab suppliers.  ~$500–1,000.

**Approximate total cost:** $5,000–15,000 (less if borrowing from
a university nuclear physics teaching lab, which typically has
all of this equipment).

### 1.5.2 Procedure

1. **Calibrate detectors.**  Place Cd-109 source directly in
   front of each detector separately.  Record the 88 keV
   photopeak on the MCA.  Set each SCA window: LL at ~2/3 of
   the photopeak centroid, UL at ~4/3.  This accepts only
   full-energy events.

2. **Background measurement.**  No source.  Record coincidence
   rate for ≥10 hours.  This establishes the accidental +
   cosmic-ray baseline.

3. **Control: facing geometry.**  Place source between the two
   detectors facing each other (covering ~4π).  Measure
   coincidence rate.  Expected: Re/Rc ≈ 1 (confirms only one
   gamma emitted per decay; Reiter verified this).

4. **Tandem measurement.**  Source in collimator in front of
   detector #1.  Detector #2 directly behind #1.  Record
   singles rates R₁, R₂ and coincidence rate Re for ≥2 hours.
   Compute Rc = R₁ × R₂ × τ.  Compute Re/Rc.

5. **Vary τ.**  Repeat tandem measurement with τ = 50, 100, 200,
   500 ns.  If the effect is real, Re/Rc should be roughly
   constant (the coincidences are genuinely simultaneous, not
   time-smeared); if artifact, Re/Rc may depend on τ.

6. **Vary SCA window.**  Repeat with LL at 1/2 and 3/4 of
   photopeak.  Reiter's prediction: higher LL (stricter energy
   window) should still show Re/Rc ≫ 1, ruling out
   down-conversion.

7. **Source chemical state (if resources allow).**  Prepare
   Cd-109 in salt form (evaporate isotope solution) and metal
   form (electroplate onto wire).  Compare Re/Rc.  Reiter
   reports 5× difference.

### 1.5.3 Statistical requirements

At Reiter's rates (Re ≈ 0.053/s, Rc ≈ 0.0016/s), achieving
5σ significance requires:

    N = (5/√N)² → N ≈ 25 events at Re
    Time = 25 / 0.053 ≈ 470 seconds ≈ 8 minutes

This is remarkably fast.  A single afternoon of data collection
should establish or refute the effect at high statistical
significance.  The main time investment is calibration and
systematics.

---

## 1.6 Potential artifacts to control for

| Artifact | Mechanism | Control |
|---|---|---|
| Pile-up | Two independent gammas within τ | Compute Rc from R₁, R₂, τ; this IS the pile-up rate; Re/Rc ≫ 1 rules it out |
| Compton scatter | Gamma Compton-scatters in #1, scattered photon hits #2 | SCA window rejects scattered photons (lower energy than 88 keV) |
| Fluorescence | Gamma excites NaI fluorescence in #1, fluorescence photon hits #2 | NaI fluorescence is ~30 keV (iodine K-edge), well below LL at ~59 keV |
| Cosmic rays | Cosmic muon traverses both detectors | Background subtraction; cosmic rate is ~1/min/cm², orders below Re |
| PMT afterpulsing | PMT #1 fires, afterpulse triggers PMT #2 | Detectors are separate assemblies with no electrical coupling; DSO pulse-shape verification |
| Source contamination | Cd-109 sample contains other isotopes | Check singles spectrum on MCA for unexpected peaks |
| Cross-talk | Electrical cross-talk between detector channels | Shield cables; use separate amplifier/SCA units; test with pulser |

---

---

# Track 2: Pre-load persistence

*Requires:* Track 1 succeeds (Re/Rc ≫ 1).
*Uses:* Same equipment as Track 1.

## 2.1 Hypothesis

The sub-threshold pre-loaded state in a detector crystal
persists for a measurable duration — it is not merely a
transient excitation that decays in nanoseconds.  In T⁶
language: energy deposited into electron-T² modes below the
511 keV emission threshold remains trapped in those modes
until either (a) additional energy pushes it over threshold
or (b) it leaks out via cross-shear coupling to other T²
subplanes or thermal radiation.

## 2.2 Predicted outcome

The coincidence rate Re/Rc remains elevated even when the
pre-loading source is removed for a controlled delay before
the probe source is applied.  The persistence time reveals
the storage lifetime of sub-threshold energy on the
electron T².

Possible regimes:
- **Nanoseconds:** pre-load is a transient electronic
  excitation (not compact-dimension storage)
- **Microseconds–milliseconds:** consistent with phonon-mediated
  relaxation in the crystal lattice
- **Seconds–hours:** strong evidence for a protected mode (compact
  dimension or long-lived metastable state)
- **Days+:** extraordinary — would imply near-perfect isolation

## 2.3 Null outcome

Coincidence rate drops to Re/Rc ≈ 1 immediately when the
source is removed — the pre-loaded state has zero persistence.
This would not invalidate Track 1 (threshold absorption can
still work if the pre-load is continuously replenished by
ambient radiation) but would constrain the storage hypothesis:
retention requires active maintenance, not passive memory.

## 2.4 Procedure

1. **Establish baseline.**  Run Track 1 to confirm Re/Rc ≫ 1
   in tandem geometry with continuous Cd-109 source.

2. **Two-source protocol.**  Use two separate Cd-109 sources:
   - Source A ("pre-loader"): placed in front of detector #1
     for a controlled exposure time T_load.
   - Source B ("probe"): a second, identical source used to
     test the detector after Source A is removed.
   Use separate collimators so each source only illuminates
   detector #1 and can be inserted/removed independently.

3. **Load–wait–probe cycle.**
   - **Load phase:** Expose detector to Source A for T_load
     (e.g. 60 seconds at the standard ~300/s singles rate).
   - **Remove source:** Physically remove Source A (shutter or
     retraction).
   - **Wait phase:** Delay Δt (variable: 0, 1s, 10s, 60s,
     5min, 30min, 2hr).
   - **Probe phase:** Insert Source B and measure Re/Rc for a
     fixed probe duration (e.g. 60 seconds).

4. **Plot Re/Rc vs. Δt.**  Fit an exponential decay to extract
   the pre-load lifetime τ_preload.

5. **Controls:**
   - No-load control: probe without prior loading (expect
     Re/Rc at whatever level Track 1 established with a
     fresh detector — there is always some ambient pre-load).
   - Temperature variation: repeat at room temperature and
     with detector cooled (LN₂ or Peltier) to see if
     τ_preload changes (threshold model predicts longer
     lifetime at lower temperature — less thermal leakage).

---

# Track 3: Controlled write/read

*Requires:* Track 2 shows τ_preload ≫ probe duration.
*Uses:* Same equipment plus a multichannel analyzer (MCA) for
spectral resolution.

## 3.1 Hypothesis

A specific quantity of sub-threshold energy can be
deliberately loaded ("written") into a detector crystal, and
the amount of stored energy can be inferred ("read") from the
subsequent coincidence rate or from shifts in the pulse-height
spectrum.

## 3.2 Predicted outcome

- **Write:** Exposing a detector to N gamma pulses at a
  controlled rate deposits a predictable amount of
  sub-threshold energy.  The coincidence rate Re/Rc
  increases monotonically with N (more pre-load → easier to
  reach threshold from a split gamma).
- **Read:** The pulse-height spectrum of the pre-loaded
  detector shows a subtle upward shift in the photopeak
  centroid, or a broadening of the peak toward higher
  energies, because some events start from a pre-loaded
  baseline.
- **Destructive read:** A sufficiently intense probe beam
  "reads out" all the stored pre-load by pushing it over
  threshold, and the coincidence rate returns to the
  fresh-detector baseline.  The integrated excess
  coincidences during readout correspond to the total
  stored energy.

## 3.3 Null outcome

No correlation between prior loading history and subsequent
coincidence rate or spectral shape.  Each detection event is
independent of previous history.  This would be consistent
with standard QM and would argue against addressable storage.

## 3.4 Procedure

1. **Dose-response curve.**  Load the detector with Source A
   for varying durations (1s, 5s, 15s, 60s, 300s).  After
   each loading, immediately probe with Source B and record
   Re/Rc.  Plot Re/Rc vs. T_load.  Threshold model predicts
   a saturation curve (pre-load fills up to just below
   threshold).

2. **Spectral shift.**  Record the full MCA spectrum of
   detector #2 during the probe phase, for various T_load
   values.  Look for a shift in the photopeak centroid
   compared to the no-load control.

3. **Depletion ("destructive read").**  Load the detector
   heavily (T_load = 300s).  Then probe with Source B at
   high rate.  Monitor Re/Rc over time.  If the pre-loaded
   state is being consumed, Re/Rc should start high and
   decay back to the fresh-detector baseline as the stored
   energy is read out.

4. **Repeated cycles.**  Perform load → read → load → read
   cycles.  If the coincidence rate recovers after each
   load and depletes after each read, this demonstrates
   reproducible write/read on the electron T².

---

# Track 4: Geometry and source variants

*Requires:* Track 1 succeeds.
*Uses:* Additional sources and detector configurations.

## 4.1 Beam-split geometry

Instead of tandem, use a scattering target (aluminum, silicon,
germanium crystal) to deflect part of the gamma beam to a side
detector.  This is more analogous to an optical beam splitter.
Compare Rayleigh (elastic) vs. Compton (inelastic) scattering
by examining the pulse-height spectrum of the side detector.

## 4.2 Na-22 triple coincidence

Use Na-22 (positron emitter).  Positron annihilation produces
two back-to-back 511 keV gammas.  Place two detectors in tandem
to catch one, and a third detector opposite to catch the other.
Triple coincidence.  Reiter reports Re/Rc = 963 — the strongest
signal.

## 4.3 Alpha-ray split

Am-241 alpha particles through gold leaf, detected by two
silicon surface-barrier detectors.  This extends the threshold
claim from electromagnetic radiation (gammas) to matter waves
(helium nuclei).  Requires a vacuum chamber.

## 4.4 Chemical state sensitivity

Prepare Cd-109 in salt form (evaporate isotope solution) and
metal form (electroplate onto platinum wire).  Compare Re/Rc
between the two.  Reiter reports a 5× difference — salt
(crystalline) form produces more coincidences.  Replication
of this finding would be a strong confirmation that the effect
is physically real and not instrumental, since the
conventional singles spectrum shows no difference between
the two forms.

---

# Shared sections

## Equipment (all tracks)

### Core (Tracks 1–3)

- **Source:** Cd-109 sealed source, ~1 μCi (license-exempt).
  Available from Spectrum Techniques or Eckert & Ziegler.
  ~$50–200.  Two identical sources for Track 2–3 two-source
  protocol.
- **Detector #1:** Thin NaI(Tl) crystal, 3–5 mm thick, ~40 mm
  diameter, coupled to PMT.  Custom order from Saint-Gobain
  or Hilger Crystals.  ~$1,000–3,000.
- **Detector #2:** Standard 1.5" or 2" NaI(Tl) detector assembly
  (e.g., Ortec 905 series).  ~$2,000–4,000.
- **Electronics (per channel):** Shaping amplifier (Ortec 572A),
  single-channel analyzer (Ortec 550A), counter/scaler
  (Ortec 994).
- **Coincidence unit:** Ortec 414A with adjustable τ.
- **MCA or DSO:** Multichannel analyzer (Ortec EASY-MCA) or
  100+ MHz oscilloscope for pulse-height verification.
- **Shielding:** Lead castle (2" thick lead bricks).

### Additional (Track 4)

- **Na-22 source** and third detector for triple coincidence.
- **Am-241 source**, gold leaf, two silicon surface-barrier
  detectors, vacuum chamber for alpha-ray split.
- **Scattering targets** (Al, Si, Ge crystals) for beam-split
  geometry.

### Budget

| Scope | Estimated cost |
|-------|---------------|
| Track 1 only | $5,000–15,000 |
| Tracks 1–3 | $6,000–18,000 (add second source + MCA) |
| All tracks | $15,000–35,000 (add vacuum chamber, extra detectors) |
| Using university lab | ~$0 (most equipment already available) |

## Feasibility assessment

| Factor | Assessment |
|---|---|
| Equipment | Standard nuclear physics teaching lab equipment |
| Budget | $5,000–35,000 depending on scope (or ~$0 using existing university lab) |
| Expertise | Undergraduate nuclear physics lab level |
| Time to result | Track 1: ~1 week.  Tracks 2–3: ~2 weeks additional.  Track 4: ~1 month. |
| Risk of false positive | Moderate (pile-up, cross-talk); controlled by standard nuclear spectroscopy practices |
| Risk of false negative | Low (if Reiter's effect is real, the signal is large: Re/Rc = 33) |
| Replication value | Extremely high — no independent replication of this claim exists |

This is likely the cheapest, fastest, and most consequential
experiment in the entire project.

---

## What results would mean

**Track 1 — Re/Rc ≫ 1 (replicates Reiter):**

The threshold model gains independent experimental support.
Sub-threshold energy accumulation is real.  The storage
hypothesis retains its second pillar.  This result would also
be independently publishable as the first independent
replication of a deeply heterodox claim.  Proceed to Track 2.

**Track 1 — Re/Rc ≈ 1 (fails to replicate):**

The threshold model loses its only experimental support.
Compact-dimension storage may still be possible under standard
quantum mechanics (modes can hold integer quanta), but the
unique advantages of the threshold model — continuous analog
storage, sub-quantum access, invisibility to standard
measurement — are lost.  Stop here; reassess before spending
further.

**Track 2 — τ_preload measurable (seconds or longer):**

Sub-threshold energy is a stable, protected state.  Storage
on compact dimensions is not just possible in principle — it
happens spontaneously in ordinary matter exposed to radiation.
This dramatically strengthens the case for neutrino-sheet
storage and motivates L01 (THz write/read on T²_ν).

**Track 2 — τ_preload ~ nanoseconds or undetectable:**

Pre-load exists (Track 1) but decays instantly.  Storage
requires continuous energy input, not passive retention.
The biological storage hypothesis weakens unless cells
actively maintain the stored state.

**Track 3 — Reproducible write/read cycles:**

Controlled, addressable storage on the electron T² is real.
The same physics should apply to the neutrino T² at different
energy scales.  L01 becomes a matter of equipment, not
principle.

**Track 3 — No write/read correlation:**

Threshold absorption is real but not controllable.  The
pre-loaded state may be too chaotic or distributed to
function as addressable memory.  The storage hypothesis
needs a mechanism for order.
