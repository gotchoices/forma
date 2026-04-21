# L01: THz Write/Read of Neutrino-Sheet Modes

**Status:** Proposed
**Tests:** Material-dimension storage hypothesis
  ([sub-quantum-memory](../papers/sub-quantum-memory.md) §5, §7, §§8–9,
   §16.1)
**Related:** R26 F1–F9 (neutrino sheet mode spectrum),
  [Q78](../qa/Q78-neutrino-sheet-access.md) (cell access mechanisms)

---

## 1. Hypothesis

The neutrino sheet (Ma_ν) supports standing-wave modes at
specific frequencies in the THz / far-infrared band.  If
material-dimension storage is real, then:

1. Narrowband THz radiation at a predicted mode frequency can
   deposit energy into the corresponding Ma_ν mode via the
   neutron-gateway coupling (through neutrons in the target
   material).
2. The deposited energy persists after the source is removed —
   longer than any conventional molecular relaxation timescale.
3. The stored energy can be detected by a subsequent spectral
   measurement (destructive readout).

## 2. Predicted outcome

- **On-resonance** THz illumination (at a predicted mode
  frequency) produces a persistent spectral signature — an
  absorption or emission feature that remains detectable for
  seconds to hours after the source is removed.
- **Off-resonance** illumination (between predicted mode
  frequencies, same power and duration) produces no persistent
  signature.
- The persistent feature appears at the exact frequency of the
  written mode, not at any conventional molecular absorption
  line of the target material.

## 3. Null outcome

On-resonance and off-resonance illumination produce
indistinguishable results.  No persistent spectral feature is
observed beyond conventional molecular relaxation timescales
(~ps–ns).  This would mean either: (a) material-dimension modes
do not exist at these frequencies, (b) the neutron-gateway
coupling is too weak to detect with available equipment, or
(c) the storage hypothesis is wrong.

A null result at known sensitivity still constrains the coupling
strength, which is the most important unknown parameter in the
entire storage hypothesis.

---

## 4. Target frequencies

The Ma_ν mode spectrum (Assignment A: E₀ = 29.26 meV, r ≈ 5,
s = 0.022) has its lowest modes at:

| Mode (n₃, n₄) | Energy (meV) | Frequency (THz) | λ (μm) | Identity |
|---|---|---|---|---|
| (±1, 0) | 5.9 | 1.42 | 211 | Lowest mode |
| (±2, 0) | 11.8 | 2.85 | 105 | |
| (0, ±1) | 29.3 | 7.07 | 42.4 | Ring fundamental |
| (1, 1) | 29.2 | 7.06 | 42.4 | ν₁ mass eigenstate |
| (−1, 1) | 30.5 | 7.37 | 40.7 | ν₂ mass eigenstate |
| (1, 2) | 58.2 | 14.07 | 21.3 | ν₃ mass eigenstate |
| (0, ±2) | 58.5 | 14.14 | 21.2 | Ring 2nd harmonic |

The full addressable spectrum spans approximately **1.4–24 THz**
(wavelengths 12–212 μm, the far-infrared to mid-infrared band).

**Primary targets for the first experiment:**
- 7.06 THz (ν₁ mode) — strongest prediction, matches neutrino
  mass eigenstate
- 7.37 THz (ν₂ mode) — 300 GHz above ν₁, tests frequency
  selectivity
- 5.0 THz (between modes) — off-resonance control

The ν₁/ν₂ pair is ideal: two modes separated by only 300 GHz,
both predicted to store energy, with a control frequency midway
between them.

---

## 5. Target material

The neutron-gateway hypothesis predicts that coupling strength
scales with neutron density in the target.  Preferred target
materials:

| Material | Why | Neutron density | IR transparency |
|---|---|---|---|
| BaF₂ crystal | Heavy (Ba: 81 neutrons); IR-transparent to ~50 μm | Very high | Good |
| CaF₂ crystal | Moderate weight; transparent to ~100 μm | Moderate | Excellent far-IR window |
| Bone fragment | Biologically relevant; calcium + phosphorus | Moderate–high | Poor (absorptive) |
| Heavy water (D₂O) | Deuterium has 1 neutron per atom; IR-active | Low | Moderate |
| Hydrogen-free control | e.g., pure silicon | ~14 neutrons/atom | Excellent |

**Recommended first target: BaF₂ window** (1 mm thick,
polished).  Barium has 81 neutrons per atom, providing maximum
gateway density.  BaF₂ is transparent from visible through
~50 μm (6 THz), with known absorption features that can be
subtracted.  For frequencies above 6 THz, use CaF₂ or a thin
polyethylene window.

**Control target: polyethylene (CH₂)ₙ** — mostly hydrogen
(zero neutrons) and carbon (6 neutrons).  Much lower neutron
density.  If the neutron-gateway hypothesis is correct, the
same illumination protocol should produce a weaker or absent
persistent signal in polyethylene vs. BaF₂.

---

## 6. Equipment

### 6.1 THz / far-IR source (write beam)

| Option | Range | Bandwidth | Power | Approx. cost | Notes |
|---|---|---|---|---|---|
| **DFG system** (two telecom lasers + GaSe crystal) | 0.5–30 THz tunable | ~GHz | ~μW–mW | $50–150K | Covers full range; best general-purpose option |
| **QCL** (quantum cascade laser) | 1–5 THz | ~MHz | ~mW | $30–80K | Higher power but limited range; needs cryocooling below ~3 THz |
| **OPO** (optical parametric oscillator) | 5–30 THz | ~GHz | ~mW | $50–120K | Good for mid-IR portion |
| **FEL** (free-electron laser) | 0.3–100+ THz | Tunable, narrow | ~kW peak | Facility access | Highest power; requires beam-time proposal |

**Recommended:** DFG system for tunability, supplemented by a
QCL if more power is needed at 1–5 THz.

### 6.2 Spectrometer (read system)

| Option | Range | Sensitivity | Resolution | Approx. cost |
|---|---|---|---|---|
| **FTIR spectrometer** (e.g., Bruker Vertex 80v) | 1–100+ THz | ~pW/√Hz with cooled bolometer | ~0.1 cm⁻¹ (~3 GHz) | $80–200K |
| **THz-TDS** (time-domain spectroscopy) | 0.1–10 THz | ~fW coherent | ~10 GHz | $60–150K |
| **Heterodyne receiver** | 0.5–5 THz | ~10⁻²⁰ W/Hz | ~MHz | $40–100K |

**Recommended:** FTIR spectrometer with a liquid-helium-cooled
Si bolometer.  Broadband coverage in a single scan; well-
understood calibration; commercially available.

### 6.3 Supporting equipment

| Item | Purpose | Approx. cost |
|---|---|---|
| Vacuum sample chamber | Eliminate water vapor absorption | $10–20K |
| Closed-cycle cryostat (4 K) | Reduce thermal background; kT drops from 25 meV to 0.4 meV | $20–40K |
| Optical chopper + lock-in amplifier | Modulated detection for signal extraction | $5–15K |
| Beam-steering optics (off-axis parabolic mirrors) | Focus write beam to ~100 μm spot | $5–10K |

### 6.4 Total estimated budget

| Configuration | Cost |
|---|---|
| Minimal (DFG + FTIR + vacuum chamber) | ~$150–350K |
| Full (add cryostat + lock-in + QCL) | ~$250–550K |
| Using existing university FTIR lab | ~$50–150K (source only) |

This is within the budget of a standard university experimental
physics or materials-science lab.

---

## 7. Procedure

### 7.1 Baseline characterization

1. Mount target (BaF₂ window) in vacuum chamber.
2. Record FTIR transmission spectrum from 1–25 THz at room
   temperature.  This is the baseline — all conventional
   absorption features of the target.
3. Cool to 4 K.  Record spectrum again.  Conventional features
   sharpen; thermal background drops.
4. Identify the predicted mode frequencies (7.06, 7.37, 14.07
   THz) on the baseline spectrum.  Note any pre-existing
   features at or near these frequencies.

### 7.2 Write

5. Tune DFG source to 7.06 THz (ν₁ mode).  Verify frequency
   with wavemeter or FTIR cross-check.
6. Illuminate target for a controlled duration.  Start with
   1 second; increase by decades (10 s, 100 s, 1000 s) in
   successive runs if no signal is observed.
7. Record the write beam power and total deposited energy at
   each duration.

### 7.3 Read (destructive)

8. Block the write beam.
9. Wait a controlled delay (1 s, 10 s, 100 s, 1000 s) to test
   persistence.
10. Record FTIR transmission spectrum.
11. Subtract the pre-write baseline.  Look for:
    - New absorption or emission feature at 7.06 THz
    - Amplitude of feature vs. write duration
    - Amplitude of feature vs. delay time (decay curve)
12. Repeat at the same power with off-resonance frequency
    (5.0 THz).  Record identical spectra.

### 7.4 Frequency selectivity test

13. Write at 7.06 THz.  Read the full 1–25 THz spectrum.
    Check whether a feature appears ONLY at 7.06 THz or also
    at other mode frequencies.  The model predicts strict
    frequency selectivity (energy goes only into the addressed
    mode).
14. Write at 7.37 THz (ν₂ mode).  Read again.  Look for a
    feature at 7.37 THz that is independent of any feature at
    7.06 THz.  This tests whether two modes can be addressed
    independently.

### 7.5 Material comparison

15. Repeat the full protocol with the control target
    (polyethylene).  Compare persistent-feature amplitude
    between BaF₂ (high neutron density) and polyethylene (low
    neutron density).
16. If signal scales with neutron density, this supports the
    neutron-gateway coupling mechanism.

---

## 8. Signatures and interpretation

### 8.1 Smoking gun: anomalous persistence

Conventional molecular/phonon excitations in the THz band relax
on timescales of picoseconds to nanoseconds.  A spectral feature
that persists for seconds or longer at a predicted Ma_ν mode
frequency, after the source is removed, has no conventional
explanation.

| Observation | Interpretation |
|---|---|
| Persistent feature at predicted frequency | Consistent with material-dimension storage |
| Feature persists for seconds–hours | Cross-shear leakage rate is slow (as predicted) |
| On-resonance ≫ off-resonance | Frequency selectivity confirms mode addressing |
| BaF₂ ≫ polyethylene | Neutron-gateway coupling confirmed |
| Feature at 7.06 THz independent of 7.37 THz | Mode independence confirmed |

### 8.2 Subtleties

- **Trapped charge or defect states** can produce long-lived
  spectral features in crystals.  Control for this by testing
  multiple BaF₂ samples, annealing between runs, and checking
  whether the feature frequency matches a known defect line.
- **Thermal effects** (slow heating of the crystal by THz
  absorption) can shift the baseline.  Control by monitoring
  sample temperature with a thermometer attached to the mount.
- **Stimulated emission from population inversion** is possible
  if the write deposits enough energy.  This would manifest as
  a narrow emission line rather than absorption — still a
  positive result, but with different implications for the
  storage mechanism.

---

## 9. Feasibility assessment

| Factor | Assessment |
|---|---|
| Equipment availability | All components commercially available |
| Budget | $150–550K; within university lab range |
| Expertise required | THz spectroscopy (active research field; many labs worldwide) |
| Time to first result | ~3–6 months from equipment delivery |
| Risk of false positive | Moderate (trapped-charge states mimic persistence); controlled by material comparison |
| Risk of false negative | High (coupling may be too weak for current sensitivity); a null result constrains coupling strength |
| Uniqueness | No existing experiment tests for persistent THz spectral features at predicted Ma_ν frequencies |

### 9.1 Existing facilities that could perform this

Many university and national-lab THz spectroscopy groups have
the required equipment already in place.  A collaboration with
an existing group would reduce the cost to essentially zero
(beyond consumables and student time).  Candidate facility
types:

- **THz spectroscopy labs** (common in physics and chemistry
  departments)
- **Synchrotron far-IR beamlines** (e.g., ALS, NSLS-II, SOLEIL,
  Diamond) — provide high-brightness broadband far-IR for both
  write and read
- **Free-electron laser facilities** (FELIX, Jefferson Lab FEL)
  — provide highest power for maximum write energy

### 9.2 A minimal first test

Before committing to the full protocol, a quick screening
experiment:

1. Use an existing FTIR spectrometer with a globar source
   (broadband thermal IR).
2. Record the transmission spectrum of a BaF₂ window at 4 K.
3. Illuminate the sample with a broadband THz source for 10
   minutes.
4. Record the spectrum again.
5. Look for ANY change at the predicted mode frequencies.

This costs essentially nothing if you have access to a
cryogenic FTIR setup.  A null result at this sensitivity is
unsurprising (the broadband source puts very little power into
any single mode frequency), but a positive result — even a
hint — would justify the full narrowband experiment.

---

## 10. What a result would mean

**Positive result (persistent feature at predicted frequency):**

This would be evidence that Ma_ν modes exist and can be
addressed by THz radiation.  It would not prove the full storage
hypothesis (which also requires threshold absorption, biological
coupling, and information encoding), but it would establish the
most fundamental prerequisite: that material-dimension modes at
the neutrino scale are physically real and accessible.

It would also constrain the coupling strength — the most
important unknown parameter in the entire Ma framework — by
measuring the write efficiency (energy deposited vs. energy in
the beam) and the decay rate (persistence timescale).

**Null result at stated sensitivity:**

This constrains the coupling strength from above: if no feature
is detectable with X watts of narrowband THz for Y seconds on
a BaF₂ target, the per-neutron coupling must be below Z.  This
bound is useful regardless of whether the storage hypothesis is
correct — it constrains ALL predictions of the Ma model that
depend on evanescent coupling between S and material dimensions.
