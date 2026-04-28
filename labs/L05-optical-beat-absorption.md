# L05: Optical Beat Absorption at Neutrino Frequencies

**Status:** Proposed
**Tests:** Dark mode absorption at MaSt-predicted neutrino
  frequencies using optical heterodyne beating
**Related:** [L04](L04-beta-decay-thz-resonance.md) (direct
  THz approach), [R57](../studies/R57-energy-routing/findings.md)
  (dark mode routing), [R49](../studies/R49-neutrino-filter/)
  (neutrino sheet modes)

---

## 1. Concept

Two near-infrared laser beams at frequencies f₁ and f₂ are
combined and focused into a transparent sample.  Where the
beams overlap, the electromagnetic intensity beats at the
difference frequency f₁ − f₂.  By tuning f₁ and f₂, the
beat frequency is set to exactly 7.06, 7.37, or 14.07 THz
(the MaSt-predicted neutrino mass eigenstate frequencies for
Family A) — or to any of the other Family candidates.

**The THz frequency is never generated in a crystal and never
propagates through air.**  It exists only as an intensity
modulation at the point where the beams cross.  This avoids
the Reststrahlen band problem that blocks QCL and DFG
approaches at 7–14 THz.

**This is a SAFER, SIMPLER predecessor to L04.**  No
radioactive tritium source.  No nuclear processes.  The
observable is anomalous optical absorption — a change in
transmitted laser power when the beat frequency matches a
predicted neutrino frequency.  If absorption is found, it
establishes the coupling mechanism before attempting any
nuclear experiments.


## 2. What to look for

**A narrow absorption dip** at one or more of the predicted
beat frequencies, with these characteristics:

1. **Narrow:** sharper than any phonon band in the sample
   material (phonon bands are ~0.5–2 THz wide; the neutrino
   mode should be < 100 MHz wide at Q > 10⁵)

2. **Frequency-specific:** disappears when the beat is detuned
   by a few percent

3. **Material-independent:** the SAME absorption frequency in
   silicon, diamond, water, and air.  Phonon bands are
   material-specific; neutrino frequencies are universal

4. **Not attributable to known spectroscopy:** no molecular
   line, no phonon band, no electronic transition at that
   frequency in the sample material

Material-independence is the decisive test.  If the same
7.06 THz absorption appears in every material tested, it
cannot be phonons — it must be something universal.


## 3. Laser setup

### Fixed reference

One single-mode telecom laser at 1550 nm (193.5 THz).
Standard DFB or ECL, 10–50 mW.

### Three tunable partners

Each partner produces one beat frequency against the
reference.  All three can illuminate the sample simultaneously,
probing ν₁, ν₂, and ν₃ at once.

**Family A targets (leading candidate):**

| Beat | Target (THz) | Partner wavelength | Laser type |
|------|-------------|-------------------|-----------|
| ν₁ | 7.06 | 1609.1 nm | Tunable ECL, C+L band |
| ν₂ | 7.37 | 1611.8 nm | Tunable ECL, C+L band |
| ν₃ | 14.07 | 1672.0 nm | Extended InGaAs / thulium |

**To test other families:** retune the three partners.
The reference stays at 1550 nm.

| Family | ν₁ partner | ν₂ partner | ν₃ partner |
|--------|-----------|-----------|-----------|
| A | 1609 nm | 1612 nm | 1672 nm |
| B | 1560 nm | 1570 nm | 1654 nm |
| C | 1557 nm | 1569 nm | 1655 nm |
| D | 1610 nm | 1613 nm | 1671 nm |

One set of tunable lasers covers ALL families.

### Frequency stability

The dark mode linewidth at Q = 10⁶ is ~7 MHz.  The beat
frequency must stay within this window.

| Laser type | Relative jitter | Adequate? | Cost (pair) |
|-----------|----------------|-----------|-------------|
| Free-running DFB | ~10 MHz | Marginal | $2–4K |
| **External cavity (ECL)** | **~100 kHz** | **Yes** | **$10–20K** |
| Phase-locked pair | <1 kHz | Yes (overkill) | $15–25K |

**Recommendation:** ECLs for the discovery phase.  100 kHz
jitter is 70× below the mode acceptance bandwidth.


## 4. Sample and detection

### Sample choices (transparent at 1550 nm, no 7 THz phonon)

| Material | Reststrahlen (THz) | Transparent at ν₁? | Notes |
|----------|-------------------|-------------------|-------|
| Silicon | 15.6 | **Yes** (7 THz is well below) | Standard IR window |
| Diamond | 40 | **Yes** | Very clean — no absorption below 30 THz |
| CaF₂ | 7.3 | **Near ν₁!** — good control | Phonon at 7.3 vs ν₁ at 7.06 |
| ZnSe | 6.2 | **Yes** | Good far-IR window material |
| Air / vacuum | none | **Yes** | Ultimate material-independence test |

### Detection

Monitor transmitted power on each of the four beams with
InGaAs photodetectors.  If the beat frequency resonantly
excites a dark mode, energy is removed from the beams →
transmitted power drops.

Alternatively: monitor TOTAL transmitted power with a
broadband detector.  Any resonant absorption should show
as a dip when the beat sweeps through the target frequency.

**Modulation technique:** slowly sweep one partner laser
across the target beat frequency (e.g., ±500 MHz around
7.06 THz).  Lock-in detection at the sweep frequency gives
high sensitivity to narrow absorption features.


## 5. Protocol

### Phase 1: Single-material scan (1–2 weeks)

1. Set up reference + one partner in a silicon sample
2. Sweep the beat frequency across 6.5–7.5 THz in 10 MHz steps
3. At each step, record transmitted power (1 s integration)
4. Look for any dip > 3σ above the noise floor
5. If found: narrow the sweep, increase integration, verify

### Phase 2: Material-independence test (1–2 weeks)

6. Repeat the scan in diamond, ZnSe, CaF₂, and air
7. If the dip appears at the SAME frequency in all materials:
   → candidate neutrino absorption signal
8. If the dip shifts with material → it's a phonon or
   molecular feature (not neutrino)

### Phase 3: All three frequencies (1 week)

9. Add partners 2 and 3 to probe ν₂ and ν₃ simultaneously
10. Verify all three frequencies in the positive material(s)

### Phase 4: Family discrimination (1 week)

11. Retune partners to Family B, C, D frequencies
12. Find which family produces the signal (if any)


## 6. Possible outcomes

| Observation | Meaning |
|-------------|---------|
| Narrow dip at 7.06 THz in all materials | **Strong evidence** for ν dark mode absorption |
| Dip at 7.06 THz in some materials only | Material-dependent → phonon feature, not neutrino |
| Dip at a DIFFERENT frequency, material-independent | Unknown universal absorber — investigate |
| No dip at any frequency | Coupling too weak for intensity-beat excitation; try L04 (direct THz field) |
| Dips at Family B frequencies but not Family A | Family B is correct; neutrino masses are ~5/10/50 meV |


## 7. Why the beat should work: medium coupling, not antenna coupling

The beat produces an intensity modulation at f_beat, not an
oscillating E-field.  Initially this seemed like a limitation.
On closer analysis (Q118), it's not — because the Ma-S
coupling is a medium-to-medium energy transfer, not an
antenna phenomenon.

**The beat HAS a wavelength.** The intensity modulation
travels through space as a wave at f_beat = 7.06 THz with
spatial wavelength λ = c/f_beat = 42.5 μm — the SAME
wavelength as a real THz photon.  This matches the ν-sheet
ring circumference (L_ring_ν ≈ 42 μm for Family A).

**The coupling is through the metric, not through free
charges.**  The Ma-S junction connects to the energy-momentum
tensor T_μν, whose 00-component is the energy density.  The
beat modulates the energy density at exactly the right
frequency and wavelength.  We are coupling S light into Ma
light at frequency match, with impedance mismatch α.

**This is NOT an antenna problem** (where an E-field must
push charges).  It IS a medium-coupling problem (where energy
at the right frequency transmits through a junction).  The
beat is a legitimate energy source for this purpose.

See [Q118](../qa/Q118-optical-beating-and-dark-mode-coupling.md)
for the full analysis.


## 8. Equipment and cost

| Item | Spec | Cost |
|------|------|------|
| Reference laser | 1550 nm ECL, 50 mW | $5–8K |
| Partner 1 (ν₁) | Tunable ECL, 1600–1620 nm | $5–10K |
| Partner 2 (ν₂) | Tunable ECL, 1600–1620 nm | $5–10K |
| Partner 3 (ν₃) | Extended InGaAs, 1650–1680 nm | $5–10K |
| Fiber combiner | 1×4 PM coupler | $500 |
| InGaAs detectors (×4) | 1500–1700 nm, low noise | $2–4K |
| Lock-in amplifier | Standard | $3–5K |
| Samples | Si, diamond, ZnSe, CaF₂ windows | $1–3K |
| Optics (lenses, mounts) | Standard | $2–3K |
| **Total** | | **$30–55K** |

Versus L04: $170–400K (needs THz source + tritium handling).
L05 is 5–10× cheaper and has no radioactive materials.


## 9. Relation to other experiments

| Experiment | Method | Observable | Risk |
|-----------|--------|-----------|------|
| **L05 (this)** | Optical beat in transparent sample | Absorption dip at ν frequency | Intensity coupling might not work |
| L04 | Direct THz + tritium | Beta decay rate change | Expensive, radioactive |
| L02 | THz + palladium-deuterium | Nuclear events | Expensive, nuclear safety |

L05 is the FIRST experiment to run: cheapest, safest,
fastest.  A positive result motivates L04 and L02.  A
negative result rules out intensity-coupling but leaves
field-coupling open for L04.


## 10. Specific equipment candidates

### Reference laser (1550 nm, fixed)

The reference must be extremely stable — all beat frequencies
are measured relative to it.  Fixed-wavelength, narrow
linewidth, fiber-coupled.

| Product | Manufacturer | Linewidth | Power | Est. price | Notes |
|---------|-------------|-----------|-------|-----------|-------|
| **PLANEX** | [RIO Lasers](https://rio-lasers.com/1550nm-laser-diode/) | <3 kHz | 20 mW | $3–5K | Ultra-stable, designed as reference oscillator. OEM butterfly module. **Top choice.** |
| **SFL1550P** | [Thorlabs](https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=13653) | <50 kHz | 40 mW | ~$6K | Single-frequency, butterfly package, thermoelectric cooled. |

**Recommendation:** RIO PLANEX.  Purpose-built as a
frequency reference.  3 kHz linewidth is far beyond what we
need (7 MHz mode acceptance) but provides a rock-solid
anchor for all three beat measurements.


### Tunable partners for ν₁ and ν₂ (1550–1620 nm)

These cover ALL Family A/B/C/D candidates for ν₁ and ν₂.
The partner wavelength ranges from 1557 nm (Family C ν₁)
to 1613 nm (Family A ν₂) — well within standard C+L band
telecom laser tuning range.

| Product | Manufacturer | Linewidth | Power | Range | Est. price | Notes |
|---------|-------------|-----------|-------|-------|-----------|-------|
| **OSICS T100** (1520) | [EXFO](https://www.exfo.com/en/products/lab-manufacturing-testing/tunable-laser-sources/osics-t100/) | narrow | 7 dBm | 1520–1620 nm | ~$10–15K | Industry standard for telecom testing. 1 pm resolution. Often available refurbished. |
| **TSL-570** | [Santec](https://inst.santec.com/products/tunablelaser/tsl-570) | <0.1 pm | 13 dBm | 1500–1630 nm | ~$15–25K | Mode-hop free across full range. 90 dB side-mode suppression. Best-in-class tunable. |
| **CTL 1550** | [TOPTICA](https://www.toptica.com/products/tunable-diode-lasers/ecdl-dfb-lasers/ctl) | 10 kHz | 50 mW | 1480–1630 nm | ~$20–30K | Scientific grade. 10 kHz linewidth is 700× better than needed. |

**Recommendation:** Two EXFO T100 modules — one tuned to ν₁
partner wavelength, one to ν₂.  These are the workhorse of
telecom labs; refurbished units are widely available at
$5–8K each, halving the cost.  Either can be retuned to scan
all four families without hardware changes.


### Tunable partner for ν₃ (~1650–1680 nm)

This is the challenging wavelength.  Standard telecom lasers
stop at ~1630 nm.  The ν₃ partner wavelengths are:
- Family A: 1672 nm
- Family B: 1654 nm
- Family C: 1655 nm

Options:

| Product | Manufacturer | Linewidth | Power | Range | Est. price | Notes |
|---------|-------------|-----------|-------|-------|-----------|-------|
| **CTL 1650** | [TOPTICA](https://www.toptica.com/products/tunable-diode-lasers/ecdl-dfb-lasers/ctl) | 10 kHz | 40 mW | 1530–1750 nm | ~$25–35K | **Covers the full range** including all ν₃ candidates. The only commercial off-the-shelf tunable with narrow linewidth at 1672 nm. Could also serve as ν₁/ν₂ partner. |
| **Custom DFB** | [Eblana Photonics](https://www.eblana.com/) | ~100 kHz | 10 mW | custom single wavelength | ~$5–10K | Eblana manufactures custom DFB diodes at non-standard wavelengths. Would need to specify 1672 nm. Fixed wavelength — one diode per family's ν₃. |

**Recommendation:** if budget allows, TOPTICA CTL — one unit
covers ALL partner wavelengths (ν₁, ν₂, ν₃ for all families).
It could replace both EXFO T100s AND serve as the ν₃ source.
Two CTLs would provide simultaneous three-frequency coverage.

If budget is tight: Eblana custom DFB at 1672 nm for Family A
testing, with option to order additional diodes for other
families if results are positive.


### Photodetectors (1500–1700 nm)

Need four detectors (one per beam) to monitor transmitted
power.  InGaAs covers the full range.

| Product | Manufacturer | Type | Range | Bandwidth | Est. price | Notes |
|---------|-------------|------|-------|-----------|-----------|-------|
| **PDA20CS2** | [Thorlabs](https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=4) | Amplified InGaAs | 800–1700 nm | DC–10 MHz | ~$2K | Switchable gain (8 settings). Good general-purpose choice. |
| **PDA10DT** | [Thorlabs](https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=4) | Amplified InGaAs | 900–1700 nm | DC–10 MHz | ~$1.5K | Fixed gain. Slightly cheaper. |
| **APD430C** | [Thorlabs](https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=4047) | InGaAs avalanche | 900–1700 nm | DC–400 MHz | ~$5K | Highest sensitivity. Use for the weakest signal channel. |
| **G12183-010K** | [Hamamatsu](https://www.hamamatsu.com/jp/en/product/optical-sensors/photodiodes/ingaas-photodiode.html) | InGaAs PIN | 900–1700 nm | high speed | ~$200 | Bare diode — needs external TIA circuit. Cheapest per channel. |

**Recommendation:** 3× Thorlabs PDA20CS2 (main channels) +
1× Thorlabs APD430C (highest-sensitivity channel, used for
the weakest beam or the reference monitor).  Total: ~$11K.
The switchable gain on the PDA20CS2 is valuable during
initial setup when signal levels are unknown.


### Supporting equipment

| Item | Product / spec | Est. price | Notes |
|------|---------------|-----------|-------|
| Lock-in amplifier | Stanford Research SR830 or SR860 | $4–6K | Extracts weak absorption signal from noise. Essential for narrow-dip detection. |
| Fiber combiner | Thorlabs TW1550R5F1 (1×4 PM) | $500 | Combines all beams into one fiber for co-propagation. |
| Fiber collimator | Thorlabs F240APC-1550 (×2) | $400 | Launch into and collect from sample. |
| Sample mounts | Thorlabs cage system | $500 | Standard optomechanics. |
| Sample windows | Si, diamond, ZnSe, CaF₂ (25 mm dia) | $1–3K | Diamond is most expensive (~$1K) but cleanest spectrum. |
| Optical table | small breadboard (12"×18") | $500 | Or use existing table. |
| Function generator | for laser modulation sweep | $500 | Drives the tunable laser's wavelength modulation. |


### Build options

**Budget build (~$35K)**

| Item | Product | Cost |
|------|---------|------|
| Reference | RIO PLANEX 1550 nm | $4K |
| Partner 1 (ν₁) | EXFO T100 (refurbished) | $6K |
| Partner 2 (ν₂) | EXFO T100 (refurbished) | $6K |
| Partner 3 (ν₃) | Eblana custom DFB 1672 nm | $8K |
| Detectors | 3× PDA20CS2 + 1× APD430C | $11K |
| Supporting | lock-in, fibers, optics, samples | $8K |
| **Total** | | **~$43K** |

Covers Family A fully.  Other families require retuning
partners 1–2 (free) and ordering a new Eblana DFB for ν₃
(~$5K per family).

**Premium build (~$80K)**

| Item | Product | Cost |
|------|---------|------|
| Reference | RIO PLANEX 1550 nm | $4K |
| Partner 1+2+3 | 2× TOPTICA CTL (1530–1750 nm) | $55K |
| Detectors | 3× PDA20CS2 + 1× APD430C | $11K |
| Supporting | lock-in, fibers, optics, samples | $8K |
| **Total** | | **~$78K** |

Covers ALL families with no hardware changes — just retune
the CTLs.  10 kHz linewidth provides 700× margin over the
mode acceptance bandwidth.  Two CTLs allow simultaneous
illumination at all three frequencies.

**Minimum viable (~$20K)**

| Item | Product | Cost |
|------|---------|------|
| Reference | Thorlabs SFL1550P | $6K |
| Partner 1 | EXFO T100 (used) | $5K |
| Partner 3 | Eblana custom DFB 1672 nm | $5K |
| Detectors | 2× PDA10DT | $3K |
| Supporting | minimal optics, no lock-in | $2K |
| **Total** | | **~$21K** |

Tests ν₁ and ν₃ only (skips ν₂ which is close to ν₁).
No lock-in — relies on direct power measurement.
Proof-of-concept only; upgrade if signal found.


### NKT Photonics Koheras BASIK option (alternative all-Yb architecture)

The [Koheras BASIK](https://www.nktphotonics.com/products/single-frequency-fiber-lasers/koheras-basik/)
is an industrial OEM single-frequency fiber laser with
sub-kHz to sub-100 Hz Lorentzian linewidth, fiber-pigtailed,
and rack-integrable through the [ACOUSTIK](https://www.nktphotonics.com/products/single-frequency-lasers/koheras-acoustik/)
16-channel chassis.  Attractive as a single-vendor solution
for the entire laser front end.  The wavelength assignment
below differs from §3 because the BASIK gain bands force a
different reference choice — the beat physics is unchanged.

**Gain-band constraint.**  BASIK is offered only as Erbium
(X15/E15, 1535–1580 nm) or Ytterbium (Y10, 1030–1120 nm).
The maximum beat from two Er BASIKs is c·(1/1535 − 1/1580) ≈
5.56 THz — below every Family A target.  Only the **Y10
(Yb)** band reaches 7–14 THz, so all four modules must be
Y10.

**Four modules, not three.**  Three lasers produce three
beats {|f₁−f₂|, |f₁−f₃|, |f₂−f₃|}.  Hitting all three
Family A targets exactly would require 7.06 + 7.37 = 14.07,
but the actual sum is 14.43 — off by 0.36 THz, far outside
any BASIK's ±64 GHz tuning range.  The minimum count is
therefore one reference + three partners, as in §3.

**Family A wavelength assignment** (f = c/λ with c =
299 792.458 nm·THz):

| Role | Center λ to specify | f (THz) | Beat vs. ref |
|------|---------------------|---------|--------------|
| Reference | 1035.00 nm | 289.654 | — |
| ν₁ partner | 1060.85 nm | 282.594 | **7.060 THz** |
| ν₂ partner | 1062.01 nm | 282.284 | **7.370 THz** |
| ν₃ partner | 1087.83 nm | 275.584 | **14.070 THz** |

All four wavelengths sit inside 1030–1120 nm and at or below
1090 nm, where Y10 guarantees > 10 mW output regardless of
linewidth option.

**Y10 module specs:** linewidth < 20 kHz Lorentzian (standard)
or < 3 kHz (reduced); ±240 pm thermal tuning ≈ ±64 GHz at
1064 nm; 10 GHz fast wavelength modulation up to 20 kHz rate;
PM fiber output default; > 10 mW output (> 5 mW for reduced
linewidth above 1090 nm).  The ±64 GHz fine-tuning span is
~10⁴× wider than the predicted ν mode acceptance (~7 MHz at
Q = 10⁶), so scanning each candidate is straightforward.
Standard linewidth is more than adequate for L05.

**Detection.**  Both Si (cutoff ~1100 nm) and InGaAs photodiodes
work in 1030–1100 nm.  The Thorlabs PDA20CS2 / PDA10DT and
APD430C recommended above remain valid.

**Other families.**  Each BASIK is fixed-wavelength once
specified.  Retuning to Family B/C/D requires ordering new
partner modules at the family-appropriate centers (the 1035
nm reference can stay).  Computed analogously to the table
above for each family's three target beats.

**Single-vendor BASIK build (estimated $50–75K)**

| Item | Product | Cost (est.) |
|------|---------|-------------|
| Reference + 3 partners | 4× Koheras BASIK Y10 (custom center λ each) | $30–45K |
| Rack/control | Koheras ACOUSTIK 16-channel chassis | $5–10K |
| Detectors | 3× PDA20CS2 + 1× APD430C | $11K |
| Supporting | lock-in, fibers, optics, samples | $8K |
| **Total** | | **~$54–74K** |

Comparable to the premium TOPTICA build but with industrial
OEM hardware and full software control via NKTP CONTROL.
Trade-off: family-locked at order time vs. the wide-tunable
TOPTICA CTL which retunes across all four families in
software.


## 11. Track 5: Water as target medium

### Motivation

Phases 1–4 use transparent solids and air to test for
material-independent absorption.  This track asks a different
question: what happens when the beat frequency is delivered
into water — specifically, into the hydrogen atoms that are
bonded to oxygen?

The reasoning, from the MaSt perspective:

**Oxygen provides a local neutrino-sheet environment.**
Oxygen-16 has 8 neutrons.  In MaSt, each neutron is a
compound mode with an active neutrino-sheet component.  A
bare hydrogen atom (proton + electron, no neutron) has
neutrino-sheet winding numbers (0,0) — no neutrino mode
active.  But the hydrogen atoms in water sit ~1 Å from an
oxygen nucleus carrying 8 neutrino-sheet excitations.  If
cross-sheet coupling falls off with distance (as all field
couplings do), the oxygen's bound neutrino modes are vastly
more coupled to the adjacent hydrogen protons than any
passing free neutrino.  The hydrogen in water is bathed in
neutrino-sheet activity that free H₂ gas lacks entirely.

**Water self-moderates.**  If any fusion events occur
(however unlikely at these powers), the water thermalizes
stray neutrons within centimeters.  Thermalized neutrons
captured by hydrogen (n + p → d + γ, 2.2 MeV) make
deuterium — the fuel breeds itself.  The water is
simultaneously target, moderator, shield, and breeding
medium.

**Water absorbs gamma rays.**  Gammas from neutron capture
or fusion products are absorbed within tens of centimeters
of water.  No external shielding needed at the power levels
of this experiment.

### Challenge: THz absorption in water

Water is an extremely strong absorber at THz frequencies.
The optical beat at 7–14 THz would be absorbed within
micrometers of the focal volume.  This is a limitation
(no penetration depth) but also a feature: the energy
density at the focus is extremely high, concentrated in a
tiny volume.  The absorption length is comparable to the
neutrino Compton wavelength (~42 μm for Family A ν₁),
which may actually be the relevant scale.

Water's own vibrational modes overlap the region of interest:
librational modes at 12–25 THz, hindered translations at
5–6 THz.  These could cause background absorption that masks
the signal.  The material-independence test (Phase 2) is
essential as a control: any feature that appears in water
but not in silicon or diamond is likely water's own
spectroscopy, not a neutrino signal.

### Protocol

This track runs AFTER Phases 1–4 produce results:

1. **If material-independent absorption is found** in
   Phases 1–2: repeat the measurement with a thin water
   cell (path length ~100 μm, set by THz absorption depth).
   Compare the absorption strength in water to that in
   silicon — any enhancement in water above the universal
   baseline could indicate oxygen-mediated coupling.

2. **If NO absorption is found** in Phases 1–4: try water
   anyway.  The oxygen proximity effect might provide enough
   coupling enhancement to produce a signal that transparent
   solids lacked.

3. In either case, monitor for:
   - Anomalous heat (calorimetry on the water cell)
   - Tritium production (liquid scintillation counting on
     the water sample post-exposure)
   - Deuterium enrichment (mass spectrometry on the water
     sample post-exposure)

   At L05 laser powers (10–50 mW), none of these are
   expected.  But the measurements are cheap and the water
   is already there.

### Equipment additions

| Item | Spec | Cost |
|------|------|------|
| Thin water cell | ~100 μm path, CaF₂ windows | $200–500 |
| Thermocouple / RTD | monitor water temperature | $50–100 |
| Water samples | deionized H₂O, D₂O for comparison | $50 |

Total addition: < $1K.  Uses the same lasers and detectors
as the main experiment.
