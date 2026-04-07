# L03: Detection of the Neutrino Scaffold

**Status:** Proposed
**Tests:** Neutrino scaffold hypothesis
  ([Q106](../qa/Q106-neutrino-scaffold-and-morphogenetic-field.md) —
  coherent dark-mode structure as morphogenetic field)
**Related:**
  [Q78](../qa/Q78-neutrino-sheet-access.md) (neutrino-cell coupling),
  [Q79](../qa/Q79-cellular-resonators-and-levin.md) (Levin / cellular resonators),
  [Q81](../qa/Q81-regeneration-and-trophic-memory.md) (regeneration and trophic memory),
  [L01](L01-thz-write-read.md) (THz write/read — shares some equipment)

---

## Overview

Q106 proposes that biological organisms maintain a
morphogenetic scaffold — a coherent cluster of neutrino-
sheet dark modes occupying the same spatial volume as the
organism but invisible to electromagnetic experiments.
The scaffold persists after tissue destruction and guides
regeneration.

This lab tests whether the scaffold can be detected by
its leaked near-field — an oscillating E field at ~7 THz
(42 μm wavelength) produced by the neutrino modes'
AC coupling through the Compton window.

The experiment is staged into four tracks of increasing
ambition.  Each track builds on the previous and can be
stopped if the preceding result is negative.


## Equipment

### Track 1 only (validation of up-conversion chain)

| Component | Specific model | Est. cost |
|-----------|---------------|----------:|
| THz source (known, for calibration) | Globar (SiC element) + bandpass filter at 7 THz, OR Virginia Diodes WR-0.15 multiplier chain (~5-7.5 THz) | $2,000–$8,000 |
| Nonlinear crystal | GaSe, 10×10 mm, 1 mm thick (Eksma Optics or Del Mar Photonics) | $3,000 |
| Pump laser | Lumibird/Teem Photonics PNP microchip Nd:YAG, frequency-doubled to 532 nm, ~1 ns pulses, ~10 μJ, 1-10 kHz | $12,000 |
| Pump beam optics | Thorlabs dielectric mirrors (BB1-E02 ×4), plano-convex lens (f=150 mm), half-wave plate, polarizer | $1,000 |
| THz collection optics | 2× Thorlabs gold off-axis parabolic mirrors (MPD249-M01), 1× TPX window (Tydex, 25 mm dia) | $1,500 |
| Pump rejection filters | 3× OptiGrate BragGrate notch at 532 nm + 1× Semrock bandpass 525-530 nm | $5,000 |
| Detector | Excelitas SPCM-AQRH-14-FC silicon SPAD (65% QE at 528 nm, <25 dark counts/sec) | $4,000 |
| Lock-in amplifier | Stanford Research Systems SR830 (used) or SR860 | $5,000 |
| Optical chopper | Thorlabs MC2000B + blade | $1,300 |
| Optical breadboard | Thorlabs 2'×3' breadboard + posts, clamps, mounts | $2,500 |
| BNC cables, connectors, misc | — | $1,000 |
| **Track 1 total** | | **~$38,000** |

### Track 2 adds (biological sample)

| Component | Purpose | Est. cost |
|-----------|---------|----------:|
| Sample chamber | Custom enclosure with TPX windows (Tydex, ×2), blackened interior, N₂ purge ports | $500 |
| Biological samples | Fresh leaves (plant nursery), salamander limbs (if available through biology collaborator) | $200 |
| Surgical tools | Scalpel, forceps, cutting board — for clean tissue severing | $100 |
| **Track 2 incremental** | | **~$800** |

### Track 3 adds (time-series and spatial scanning)

| Component | Purpose | Est. cost |
|-----------|---------|----------:|
| Translation stage | Thorlabs MTS50/M-Z8E motorized linear stage (50 mm travel) ×2 for XY scanning | $4,000 |
| Stage controller | Thorlabs BSC203 3-axis controller | $3,000 |
| Data acquisition | National Instruments USB-6003 DAQ for synchronizing SPAD counts with stage position | $500 |
| Automation software | Python script using Thorlabs APT + NI-DAQmx libraries | $0 |
| **Track 3 incremental** | | **~$7,500** |

### Track 4 adds (imaging via EMCCD)

| Component | Purpose | Est. cost |
|-----------|---------|----------:|
| EMCCD camera | Andor iXon Life 888 (1024×1024, >90% QE, single-photon, cooled to −80°C) | $30,000 |
| Imaging lens | Thorlabs achromatic doublet (f=100 mm) for imaging the sum-frequency output onto the EMCCD | $200 |
| Additional filters | Semrock short-pass at 530 nm (×2) for extra pump suppression in imaging mode | $600 |
| **Track 4 incremental** | | **~$31,000** |

### Cumulative budget

| After track | Total investment | What you can do |
|-------------|----------------:|-----------------|
| 1 | ~$38,000 | Validate the up-conversion chain with a known THz source |
| 2 | ~$39,000 | Search for 7 THz signal from biological tissue and severed tissue |
| 3 | ~$46,000 | Spatial scanning + time-series of scaffold persistence |
| 4 | ~$77,000 | Full 2D imaging — photograph the scaffold |


---

## Track 1: Validate the up-conversion optical chain

### Hypothesis

Sum-frequency generation in GaSe can up-convert a 7 THz
signal to ~528 nm (visible blue-green) with sufficient
efficiency and pump rejection to detect it with a silicon
SPAD.

### Why this track comes first

The biological signal (~10⁻²⁰ W) is extraordinarily weak.
Before looking for it, we must confirm that the optical
chain works with a STRONG 7 THz source.  If the chain
can't detect a known milliwatt-level THz source, it
certainly can't detect a femtowatt-level scaffold.

### Predicted outcome

- With a known 7 THz source (globar or multiplier),
  SPAD count rate increases when the THz source is ON
  vs OFF, after all pump rejection filters.
- The signal disappears when the pump laser is blocked
  (confirming it is sum-frequency, not scattered pump
  or thermal noise).
- The signal disappears when the THz source is blocked
  (confirming it is up-converted THz, not pump
  fluorescence from the crystal).
- The count rate scales linearly with THz source power.

### Null outcome

- No detectable count rate difference between THz ON
  and OFF → the up-conversion efficiency is too low, or
  the pump rejection is insufficient.  Diagnose which
  and iterate (thicker crystal, better filters, higher
  pump power).

### Procedure

1. **Assemble the pump path.**  Set up the 532 nm
   microchip laser on the breadboard.  Steer with mirrors
   into the GaSe crystal.  Verify beam quality and
   polarization (GaSe requires specific polarization for
   phase matching — typically ordinary-polarized pump for
   type-I SFG).

2. **Assemble the THz path.**  Mount the globar or
   multiplier source.  Collimate with the first OAP
   mirror.  Focus into the GaSe crystal with the second
   OAP.  Verify THz power at the crystal position with
   a pyroelectric detector (borrow or rent one for
   calibration — Gentec-EO or Ophir sell THz power
   meters).

3. **Align for phase matching.**  Tilt the GaSe crystal
   to find the phase-matching angle for 7 THz + 532 nm
   → 528 nm.  The published angle is ~12–20° external
   tilt from the c-axis (varies with crystal thickness).
   Monitor the SPAD while tilting — count rate should
   peak at the phase-matching angle.

4. **Install pump rejection filters.**  Place the three
   BragGrate notch filters and the bandpass filter between
   the crystal and the SPAD.  Verify pump rejection: with
   THz source blocked, the SPAD count rate should drop to
   dark counts (~25 per second) regardless of pump power.
   If not, add filters or realign.

5. **Measure the up-conversion signal.**  Chop the THz
   source at ~1 kHz with the optical chopper.  Feed the
   SPAD output and the chopper reference to the lock-in
   amplifier.  The lock-in extracts the THz-synchronous
   component of the SPAD signal, rejecting all other
   noise.  Record:
   - Lock-in signal vs THz power (should be linear)
   - Lock-in signal vs pump power (should be linear)
   - Lock-in signal vs crystal angle (should peak at
     phase-matching)
   - Dark measurement: THz OFF, pump ON → lock-in
     should read zero

6. **Determine sensitivity floor.**  The minimum
   detectable THz power is where the lock-in signal
   equals the noise.  With a 1 Hz bandwidth lock-in and
   the SPAD dark count at ~25/s, the floor is set by
   shot noise.  Record this floor — it tells you the
   minimum number of coherent neutrinos needed for
   Track 2 to succeed.

### Equipment for this track

All items from the Track 1 equipment table.  No biological
samples needed.

### Duration

~2 weeks for assembly and alignment.  ~1 week for
systematic characterization.

### Decision point

If the sensitivity floor is < 10⁻¹⁸ W (corresponding to
~1000 coherent neutrinos): proceed to Track 2.
If 10⁻¹⁸ to 10⁻¹⁶ W: proceed with caution — the scaffold
signal may be below detection.
If > 10⁻¹⁶ W: the chain is not sensitive enough.
Investigate improvements (longer crystal, higher pump
power, better filters, TCSPC time-gating) before
proceeding.


---

## Track 2: Search for 7 THz emission from biological tissue

### Hypothesis

Living biological tissue emits a coherent 7 THz signal
from its neutrino scaffold.  Severed tissue retains a
residual signal from the scaffold in the empty volume
where tissue was removed.

### Predicted outcome

- **Living tissue:** SPAD count rate (lock-in extracted)
  is higher when the THz collection optics point at a
  leaf or tissue sample than at an empty reference volume.
- **Severed tissue:** immediately after cutting a leaf in
  half, a residual signal is present from the empty half
  — the volume where the leaf was, now absent.  The
  signal is weaker than the intact leaf but above the
  sensitivity floor.
- **Control volume:** a volume that never contained
  tissue shows no signal above the floor.

### Null outcome

- No difference between tissue, severed volume, and
  control → no scaffold signal at the sensitivity floor.
  Either the scaffold doesn't exist, the signal is below
  detection, or 7 THz is the wrong frequency.

### Procedure

1. **Prepare the sample chamber.**  A blackened enclosure
   with two TPX windows (one for THz collection, one for
   the pump beam if co-propagating) and N₂ purge ports
   (water vapor absorbs strongly at THz — purging with
   dry nitrogen removes this background).

2. **Baseline measurement.**  Empty chamber, no sample.
   Record the lock-in signal for ~30 minutes to establish
   the noise floor and any systematic drift.

3. **Living tissue.**  Place a fresh leaf (or a thin
   slice of biological tissue) in the chamber.  Align the
   THz collection optics to collect from the tissue.
   Record the lock-in signal for ~30 minutes.  Compare to
   baseline.

4. **Severing experiment.**  While recording, cut the
   leaf in half with a scalpel.  Remove the cut portion
   from the chamber.  Continue recording.  The lock-in
   signal should:
   - Drop when tissue is removed (less emitting area)
   - BUT not drop to baseline if the scaffold persists
     in the empty volume
   - Decay over time if the scaffold dephases without
     cellular reinforcement

5. **Time series.**  Continue recording for hours after
   severing.  Map the decay curve (if any).  Compare to
   Levin's regeneration timescale (hours to days for
   planaria and salamanders).

6. **Controls.**
   - Heated object (metal block at 37°C): produces
     broadband thermal THz, not narrowband.  The lock-in
     should show higher thermal background but NO
     narrowband 7 THz signal.
   - Dead tissue (boiled leaf): charged structure
     destroyed, scaffold may or may not persist.  Compare
     to fresh tissue.
   - Different frequencies: retune (if possible) to look
     for signal at 5 THz, 10 THz, 14 THz.  The scaffold
     signal should appear ONLY at neutrino mode
     frequencies, not broadband.

### Equipment

Track 1 equipment + Track 2 additions (sample chamber,
biological samples, surgical tools).

### Duration

~1 week for sample preparation and chamber setup.
~2 weeks for systematic measurements (multiple samples,
controls, time series).

### Decision point

If a narrowband signal above baseline is detected from
living tissue: strong positive.  Proceed to Track 3 for
spatial mapping.
If a signal is detected from intact tissue but NOT from
the severed volume: the scaffold hypothesis is weakened
(the signal may come from the charged tissue, not the
dark scaffold).
If no signal above baseline from any sample: negative at
this sensitivity.  Assess whether improved sensitivity
(Track 4 EMCCD, or longer integration) could change the
result.


---

## Track 3: Spatial scanning and persistence mapping

### Hypothesis

The scaffold has spatial structure — it mirrors the shape
of the tissue it supports.  After severing, the scaffold
occupies the empty volume in the shape of the missing
tissue.  The scaffold persists for a characteristic time
before dephasing.

### Predicted outcome

- A spatial scan of the lock-in signal across the wound
  site shows higher counts in the volume where tissue
  was removed (the ghost volume) than in adjacent empty
  space.
- The ghost volume has a shape that matches the geometry
  of the removed tissue (a leaf-shaped region, not a
  diffuse cloud).
- The signal decays over time, with a characteristic
  timescale that matches regeneration timescales
  (minutes to hours for leaves, hours to days for animal
  tissue).

### Null outcome

- No spatial structure — signal (if any) is uniform
  across the wound site and control volumes.
- No persistence — signal disappears within seconds of
  severing (faster than any known regeneration).

### Procedure

1. **Install motorized stages.**  Mount the THz collection
   optics on the XY translation stages.  The stages scan
   the collection point across the sample volume in a
   grid pattern (~1 mm step size, covering ~5 cm × 5 cm).

2. **Acquire spatial map of intact tissue.**  Scan the
   lock-in signal across a leaf.  The map should show the
   leaf shape (higher signal where the leaf is, lower
   where it isn't).  This is the calibration — confirming
   the spatial scanning works.

3. **Sever and re-scan.**  Cut the leaf in half.  Remove
   the cut portion.  Immediately re-scan the same area.
   The ghost volume (where the leaf was) should show
   residual signal.

4. **Time-series scans.**  Repeat the spatial scan at
   intervals: immediately after cutting, 5 minutes, 15
   minutes, 30 minutes, 1 hour, 2 hours, 4 hours, 8
   hours.  Map the decay of the ghost signal.

5. **3D scan (optional).**  If the XY scan shows a ghost,
   add a Z stage and scan in three dimensions to verify
   the ghost has the correct THICKNESS (a leaf is ~0.3 mm
   thick — the ghost should be 0.3 mm thick too, not a
   2D projection).

### Equipment

Track 1 + Track 2 + Track 3 additions (motorized stages,
controller, DAQ, software).

### Duration

~1 week to install and calibrate stages.  ~2 weeks for
systematic scanning (multiple samples, time series).

### Decision point

If the ghost has the shape and thickness of the removed
tissue and decays over hours: proceed to Track 4 for
imaging.
If the ghost is shapeless or instant-decay: the scaffold
hypothesis in its current form is wrong.  Consider
whether a modified version (different spatial scale,
different decay mechanism) could fit.


---

## Track 4: Photograph the scaffold

### Hypothesis

The scaffold's spatial structure can be captured as a 2D
image by up-converting its 7 THz emission to visible
light and recording with an EMCCD camera.

### Predicted outcome

A long-exposure EMCCD image of the wound site shows a
faint blue-green image in the shape of the missing tissue
— visible photons at ~528 nm produced by sum-frequency
generation from the scaffold's 7 THz emission.

### Null outcome

No image above noise — either the scaffold is too weak
for imaging at this integration time, or the spatial
signal from Track 3 was an artifact of the scanning
procedure.

### Procedure

1. **Replace SPAD with EMCCD.**  Remove the SPAD and
   install the Andor iXon Life EMCCD with imaging optics
   (achromatic doublet, f=100 mm) to image the
   sum-frequency output of the crystal onto the camera.
   Add the extra Semrock short-pass filters for additional
   pump suppression (the EMCCD integrates over the full
   field, so scattered pump photons are more problematic
   than with the SPAD + lock-in).

2. **Focus and calibrate.**  With a known THz source,
   verify that the EMCCD produces an image of the THz
   source distribution after up-conversion.  The image
   should show the source shape, confirming that spatial
   information is preserved through the up-conversion.

3. **Image intact tissue.**  Place a leaf in the chamber.
   Expose the EMCCD for ~1 hour (EM gain on, maximum
   cooling).  The resulting image should show the leaf
   shape in the up-converted 7 THz channel.

4. **Image the ghost.**  Sever the leaf.  Remove the cut
   portion.  Expose the EMCCD for 1-8 hours.  A faint
   image of the missing leaf portion — the ghost — should
   appear.

5. **Control images.**  Same exposure with empty chamber
   (should show no structure), heated metal block (may
   show thermal glow but not a leaf shape), and boiled
   leaf (test whether scaffold survives tissue death).

### Equipment

Track 1 + Track 2 + Track 3 + Track 4 additions (EMCCD,
imaging lens, additional filters).

### Duration

~1 week to install and calibrate EMCCD.  ~2 weeks for
imaging runs (long exposures, multiple samples).

### Decision point

If the ghost image appears: this is the headline result.
A visible-light photograph of a dark-matter structure
that has no mass, no charge, and no thermal emission.

If no image: the signal is below the EMCCD sensitivity
at this integration time.  Consider: longer integration
(overnight exposures), cooler EMCCD (upgrade to
liquid-nitrogen cooling for lower dark current), or
higher pump power (upgrade to the Litron/Lumibird
pulsed Nd:YAG at ~$35,000).


---

## Risk assessment

### What could go wrong at each track

**Track 1:** the up-conversion efficiency may be too low
for practical detection.  GaSe at 7 THz should work (it's
well within the crystal's transparency window), but the
phase-matching bandwidth and pump-signal overlap in the
crystal must be optimized experimentally.

**Track 2:** the biological 7 THz signal may be
indistinguishable from thermal background.  The key
defense: the scaffold signal is NARROWBAND (specific mode
frequencies) while thermal is BROADBAND.  The lock-in +
chopper extracts the modulated component, rejecting DC
thermal.  But if the scaffold signal is truly continuous
(not modulated by any known process), the lock-in cannot
help and the experiment reduces to looking for a tiny
excess above thermal — much harder.

**Mitigation:** modulate the PUMP instead of the THz.
The sum-frequency output exists only when both pump and
THz are present simultaneously.  Chopping the pump at
1 kHz means the SPAD sees up-converted photons only
during the pump-ON half-cycle.  The lock-in extracts
this modulated signal regardless of whether the THz
source is continuous or modulated.

**Track 3:** the motorized scanning adds mechanical
complexity.  Vibrations from the stages could produce
spurious signals.  Mitigation: scan slowly, average
multiple passes, verify with stationary measurements
at key positions.

**Track 4:** the EMCCD integrates all photons (no
lock-in discrimination).  Scattered pump light at 532 nm
is the primary background.  The BragGrate notch filters
must provide >OD 14 total rejection.  If pump leakage
is too high, the image is washed out.  Mitigation: add
more notch filters, or use the EMCCD in photon-counting
mode with a threshold discriminator.

### The fundamental uncertainty

All tracks assume the scaffold exists and emits at 7 THz.
If the scaffold does not exist, or emits at a different
frequency, or is too sparse for detection, ALL tracks
produce null results.  Track 1 (validation with known
source) is the critical gate — if the optical chain works,
negative biological results are informative.  If the
chain doesn't work, negative results are ambiguous.


---

## References

- Q106: [`qa/Q106-neutrino-scaffold-and-morphogenetic-field.md`](../qa/Q106-neutrino-scaffold-and-morphogenetic-field.md)
- Q78: [`qa/Q78-neutrino-sheet-access.md`](../qa/Q78-neutrino-sheet-access.md)
- Q79: [`qa/Q79-cellular-resonators-and-levin.md`](../qa/Q79-cellular-resonators-and-levin.md)
- L01: [`L01-thz-write-read.md`](L01-thz-write-read.md) (shares THz optics and detection chain)
- Levin, M. (2021). "Bioelectric signaling: Reprogrammable circuits underlying embryogenesis, regeneration, and cancer." *Cell*.
