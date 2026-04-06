# L02: Threshold-Mediated Nuclear Loading via Neutrino Compton Window

**Status:** Proposed
**Tests:** Loading hypothesis
  ([threshold-theory](../primers/threshold-theory.md) §5;
   [Q89](../qa/Q89-fusion-as-mode-transition.md) §11–12;
   [Q95](../qa/Q95-strong-force-as-internal-em.md) §5)
**Related:** R35 F1–F34 (threshold detection statistics),
  R49 F1–F10 (neutrino mode spectrum, 22 candidate triplets),
  [L01](L01-thz-write-read.md) (THz write/read — shares
  equipment and target frequencies)

---

## 1. Hypothesis

The neutrino Compton window (~42 μm / 7 THz) allows far-IR
radiation to couple energy into the neutrino sheet (Ma_ν) of
nuclei containing neutrons.  Per the loading hypothesis (Planck
1911, Reiter 2014, Q89 §11), this energy accumulates
continuously in sub-threshold modes on a particle sheet until
crossing the 0.782 MeV neutron-formation threshold, at which
point a proton converts to a neutron via a topological cascade.
The neutron, being electrically neutral, can then fuse with
a similar nearby nucleus without Coulomb barrier.

Specifically:

1. Deuterium is used as the target because its neutron already
   has a neutrino-sheet component (n₃ = odd), so the Compton
   window is open without requiring σ_νp ≠ 0 for bare protons
   (Q89 §12.5).

2. Far-IR radiation near 42 μm deposits energy through the
   open window.  The energy accumulates on the proton sheet
   via cross-sheet coupling.

3. When the accumulated energy crosses threshold, one of the
   deuterium's nearby protons converts to a neutron, which
   subsequently fuses — releasing MeV-scale energy as heat,
   gammas, and neutrons.

4. The effect is:
   - Present in deuterium, absent in protium (isotope selective)
   - Sharply peaked near ~42 μm (frequency selective)
   - Absent below a minimum pump power (threshold behavior)

These three signatures distinguish the mechanism from all
conventional effects.


## 2. Predicted outcome

- **D₂O irradiated at ~42 μm** produces measurable excess heat
  (more thermal energy out than IR energy in) and/or nuclear
  radiation (gammas at 2.224 MeV, neutrons).
- **H₂O under identical conditions** produces no excess heat
  and no radiation (no neutrino window — protium has no neutrons).
- The effect is **sharply frequency-dependent**: present at
  ~42 μm, absent at 30 μm or 55 μm.
- The effect has a **power threshold**: below some minimum
  pump power, nothing happens (dissipation exceeds loading).
  Above threshold, the rate increases with pump power.


## 3. Null outcome

D₂O and H₂O produce indistinguishable results at all
wavelengths and powers.  No excess heat, no radiation above
background.  This would mean either: (a) the neutrino Compton
window does not couple to far-IR radiation at detectable
strength, (b) the loading mechanism does not work on nuclear
mode spectra (energy dissipates faster than it accumulates),
or (c) the threshold theory framework is wrong.

A null result still constrains the coupling efficiency η —
the most important unknown parameter.  If X watts of tuned IR
for Y seconds produces no detectable nuclear events in Z moles
of D₂O, then η < (detection threshold) / (X × Y × Z).


---

## 4. Target frequencies

The neutrino mode spectrum (R49, Assignment A: ε_ν = 5.0,
s_ν = 0.022, E₀ = 29.26 meV) predicts:

| Mode (n₃, n₄) | Energy (meV) | Frequency (THz) | λ (μm) | Identity |
|---|---|---|---|---|
| (±1, 0) | 5.9 | 1.42 | 211 | Lowest tube mode |
| (0, ±1) | 29.3 | 7.07 | 42.4 | Ring fundamental |
| (1, 1) | 29.2 | 7.06 | 42.4 | ν₁ mass eigenstate |
| (−1, 1) | 30.5 | 7.37 | 40.7 | ν₂ mass eigenstate |
| (1, 2) | 58.2 | 14.07 | 21.3 | ν₃ mass eigenstate |

The **primary target** is ~7 THz (42 μm), where the ring
fundamental and ν₁ eigenstate nearly coincide.  The neutron's
neutrino component (n₃ = odd, n₄ = unknown) determines which
frequency is optimal.

R49 found 22 candidate mode triplets across three families.
A frequency sweep from 15–60 μm covers all predictions.  The
wavelength at which the effect peaks (if any) discriminates
between triplet families.

**Do we need all three frequencies simultaneously?**  Maybe.
For now, we are loading a single neutrino mode, not creating
oscillations.  Pump at ONE frequency — the sweep identifies
which.  If this fails, we may consider a three-frequency approach.


## 5. Target material

| Material | Why | Notes |
|---|---|---|
| **D₂O** (heavy water) | Deuterium has 1 neutron per atom → neutrino window open | Strong far-IR absorption; use thin layer or gas phase |
| **D₂ gas** (1–10 atm) | Same advantage; much more transparent at 42 μm | Lower target density; longer path length needed |
| **Pd loaded with D₂** | Classic LENR substrate; lattice may enhance coherence | Adds complexity; defer to later tracks |
| **H₂O** (control) | No neutrons → no neutrino window | Should show zero effect |
| **H₂ gas** (control) | Gas-phase null comparison | Matched geometry to D₂ gas |

**Recommended first target:** D₂ gas at ~5 atm in a stainless
steel cell with far-IR-transparent windows (diamond or
polyethylene).  Gas phase avoids the strong liquid-water
absorption that would compete with the neutrino coupling.

**Control:** H₂ gas at the same pressure and geometry.


---

## 6. Equipment

| Item | Purpose | Approx. cost | Notes |
|---|---|---|---|
| Tunable far-IR source (20–60 μm) | Pump beam | $20–100K | QCL, BWO, or FEL access |
| D₂O (1 kg, 99.9%) | Target material | ~$500–1K | Commercial (Sigma-Aldrich) |
| D₂ gas (lecture bottle) | Gas-phase target | ~$200–500 | Commercial |
| Gas cell with IR windows | Containment | ~$1–3K | Diamond or polyethylene windows |
| Precision calorimeter (μW resolution) | Track 1 excess heat | ~$2–5K | Commercial |
| NaI(Tl) scintillation detector + MCA | Track 2 gamma spectroscopy | ~$3–5K | Look for 2.224 MeV line |
| He-3 proportional counter + moderator | Track 2 neutron detection | ~$5–10K | Polyethylene-wrapped |
| H₂O / H₂ gas (control) | Null comparison | ~$0 | Standard lab supplies |
| Temperature sensors (±0.01°C) | Calorimetry | ~$100–500 | Pt RTD or thermistor |


**Overlap with L01:** The same far-IR source and spectrometer
serve both L01 (THz write/read of Ma_ν modes) and L02 (nuclear
loading).  Running both experiments during the same facility
access period is efficient.


---

## 7. Procedure

### Track 1: Anomalous heat search

**Hypothesis:** IR at ~42 μm deposits energy in D₂ through
the neutrino Compton window, producing excess heat from
nuclear events.

**Predicted outcome:** D₂ cell shows more heat output than
IR input; H₂ cell shows heat equal to IR input (no excess).

**Null outcome:** Both cells show identical heat equal to IR
input.

**Procedure:**

1. Prepare two identical gas cells: one with D₂, one with H₂,
   both at 5 atm.  Each cell is instrumented with a precision
   temperature sensor and enclosed in identical insulation.

2. Record baseline temperatures for 1 hour (thermal stability
   check).

3. Irradiate both cells simultaneously with the far-IR source
   at ~42 μm (7 THz).  Record beam power with a calibrated
   power meter.

4. Monitor temperature rise in both cells over 1–24 hours.

5. Compare: ΔT(D₂) vs ΔT(H₂).  Compute heat output from
   each cell and subtract the known IR input.

6. Repeat at 30 μm and 55 μm (off-resonance) to verify
   frequency specificity.

7. Swap cells (D₂ into position B, H₂ into position A) and
   repeat to control for geometric asymmetry.


### Track 2: Radiation signature search

**Hypothesis:** Nuclear events in D₂ produce characteristic
radiation (gammas, neutrons) correlated with IR pump state.

**Predicted outcome:** Gamma counts at 2.224 MeV and/or
neutron flux increase when IR is on, return to background
when IR is off.  No radiation from H₂ cell.

**Null outcome:** No radiation above background in either
cell, regardless of IR state.

**Procedure:**

1. Same setup as Track 1, with radiation detectors added:
   - NaI(Tl) detector positioned adjacent to D₂ cell
   - He-3 neutron counter (polyethylene-moderated) on
     opposite side
   - Lead or water shielding between cells to prevent
     cross-talk

2. Run alternating cycles: 1 hour IR-on, 1 hour IR-off.
   Record gamma spectrum and neutron count rate in each
   interval.

3. Compute statistical significance of on/off difference.

4. If gammas are detected: check energy spectrum for the
   2.224 MeV deuteron line, 6.257 MeV tritium line, and/or
   511 keV annihilation peak.

5. If neutrons are detected: estimate neutron rate and
   compare to expected fusion rate from the measured
   excess heat (Track 1).

**Safety note:** If nuclear events occur at detectable
rates, appropriate shielding must be in place before
sustained operation.  Begin at low power and short
duration.  Monitor personnel dosimetry.


### Track 3: Frequency selectivity — the decisive test

**Hypothesis:** The effect (heat or radiation) is sharply
peaked near 42 μm, corresponding to the neutrino Compton
window.

**Predicted outcome:** Effect rate vs wavelength shows a
resonance peak.  Peak position matches one of the R49
mode predictions.

**Null outcome:** Effect (if any) is flat across wavelength
or peaks at a wavelength unrelated to neutrino predictions.

**Procedure:**

1. Sweep the IR source from 15 μm to 60 μm in steps of
   ~2 μm (or finer near predicted peaks).

2. At each wavelength, run for a fixed duration (same as
   the duration that produced a signal in Tracks 1/2).
   Record excess heat and radiation counts.

3. Plot effect rate vs wavelength.

4. Compare peak position to the R49 predictions:
   - 42.4 μm (7.07 THz) — ring fundamental / ν₁
   - 40.7 μm (7.37 THz) — ν₂ eigenstate
   - 21.3 μm (14.07 THz) — ν₃ eigenstate

5. The peak width indicates the mode's Q factor and
   coupling strength.

**Why this is decisive:** A sharp peak at a predicted
wavelength, absent a few microns away, has no conventional
explanation.  Molecular absorption features of D₂ are
well-characterized and occur at different wavelengths.
A new feature at exactly the predicted neutrino Compton
wavelength would be extraordinary evidence.


### Track 4: Power threshold identification

**Hypothesis:** The loading mechanism has a power threshold
(pump rate must exceed dissipation rate of pre-loaded state).

**Predicted outcome:** Below some power P_min, the effect
is zero.  Above P_min, the effect rate increases with
power.  This is qualitatively different from a linear
(quantum) response where every photon has a chance.

**Null outcome:** Effect rate is proportional to power at
all levels (linear response, no threshold).  This would
be consistent with quantum absorption but inconsistent
with loading/threshold theory.

**Procedure:**

1. At the resonant wavelength (Track 3), vary IR power
   from 10% to 100% of maximum in ~10 steps.

2. At each power, run for a fixed duration.  Record excess
   heat and radiation rate.

3. Plot effect rate vs power.  Look for:
   - A threshold power below which the rate is zero
   - Above threshold: increasing rate (possibly nonlinear)

4. Estimate the pre-loaded state dissipation rate from
   P_min and the known photon energy.


### Track 5: Current harvesting (radiation → electricity)

**Hypothesis:** Charged products from nuclear events can be
captured as electrical current.

**Predicted outcome:** Measurable current between electrodes
during IR irradiation, absent when IR is off.

**Null outcome:** No current above noise.

**Procedure:**

1. Insert planar electrodes (copper or tungsten) on
   opposite sides of the D₂ gas cell.

2. Apply a small bias voltage (10–100 V) to collect
   charge.

3. Measure current with a picoammeter during IR-on and
   IR-off cycles.

4. If a magnetic field is applied (for nuclear moment
   alignment per Q89 §12.4), the MHD effect separates
   charges from fast fusion products — enhancing current.

5. Measure current vs pump power to confirm correlation.


### Track 6: Fusion product identification

**Hypothesis:** The nuclear events produce identifiable
fusion products (tritium, helium).

**Predicted outcome:** Tritium and/or helium-3 accumulate
in the gas cell over hours to days of irradiation.

**Null outcome:** No tritium or helium above background.

**Procedure:**

1. Run the D₂ cell at the resonant wavelength and optimal
   power (Tracks 3/4) for an extended period (hours–days).

2. Collect the gas from the cell.

3. **Tritium:** Dissolve collected gas in scintillation
   cocktail; count with a liquid scintillation counter.
   Tritium β⁻ (18.6 keV, t₁/₂ = 12.3 yr) is detectable
   at extremely low levels (~1 Bq).

4. **Helium:** Mass spectrometry of collected gas.
   Look for He-3 (from d+d → He-3 + n) and He-4
   (from subsequent reactions or d+d → He-4 + γ).

5. Compare quantities to the integrated radiation rate
   from Track 2 for consistency.


### Track 7: Integrated system — water to power

**Hypothesis:** The full cycle (electrolysis → D₂ →
IR-pumped fusion → energy harvesting) is net exothermic.

**Predicted outcome:** Thermal and/or electrical output
exceeds all inputs (electrolysis power + IR pump power).
Energy multiplication factor ~7× (Q89 §14.1).

**Null outcome:** Output ≤ input.  The coupling efficiency
η is below the ~7% break-even threshold.

**Procedure:**

1. **Electrolysis stage:** Electrolyze D₂O to produce D₂
   gas on demand.  No stored hydrogen — safety feature.
   Measure electrical input precisely.

2. **Reaction chamber:** D₂ gas in a cell with electrodes
   and radiation shielding (water jacket per Q89 §19).
   IR pump at resonant frequency and optimal power.

3. **Energy harvesting:**
   - Water jacket captures gammas and neutrons → hot water
   - Electrodes capture charged products → electricity
   - Thermoelectric junction on hot water → electricity

4. **Energy accounting:** Measure ALL inputs (electrolysis
   + IR pump) and ALL outputs (heat + electricity) with
   calibrated instruments.  Report net energy balance.

5. **Control knob test:** Vary IR pump power.  Verify that
   reaction rate tracks pump power (inherently safe — no
   runaway possible; Q89 §14.4).


---

## 8. Risk assessment

**Safety:**
- D₂ gas is flammable (same precautions as H₂).
- If nuclear events occur, ionizing radiation (gammas,
  neutrons) is produced.  Shielding required from Track 2
  onward: ≥ 30 cm water jacket or equivalent for sustained
  operation.
- Begin at low power and short duration.  Monitor with
  dosimetry.
- D₂O is non-toxic and non-radioactive.

**False positive risks:**
- Chemical reactions producing heat → controlled by H₂/H₂O
  comparison and radiation confirmation (Track 2)
- Cosmic ray background in gamma detector → controlled by
  on/off correlation and energy spectrum analysis
- Detector artifacts → swap detector positions; use two
  independent detector types

**False negative risks:**
- IR source not reaching 42 μm → verify source spectrum
  independently
- Coupling efficiency η too low → try higher power, longer
  duration, different medium (Pd/D lattice)
- Wrong neutrino mode assignment → the frequency sweep
  (Track 3) covers all 22 R49 candidates


---

## 9. What a result would mean

**Positive result (excess heat + nuclear radiation,
frequency-selective, in D₂ but not H₂):**

This would establish three things simultaneously:
1. The neutrino Compton window is real and accessible by
   far-IR radiation
2. The loading/threshold mechanism works on nuclear mode
   spectra
3. Controlled nuclear fusion is achievable via IR pumping

The peak wavelength would also identify which neutrino
mode triplet (of the 22 candidates from R49) is correct —
a measurement that no other experiment can make.

**Null result at stated sensitivity:**

Constrains the product (σ_νp × η) from above: the coupling
through the neutrino window is weaker than the detection
threshold allows.  This bound is useful for all predictions
that depend on cross-sheet coupling strength.

Does NOT falsify the Ma model generally — only the specific
loading pathway.  Other pathways (e.g., direct proton-sheet
coupling at gamma wavelengths) remain untested.
