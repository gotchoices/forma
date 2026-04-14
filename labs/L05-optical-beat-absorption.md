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


## 7. Caveat: field vs intensity coupling

The beat produces an INTENSITY modulation at f_beat, not a
propagating electric field.  If dark modes couple to the
field amplitude (linear in E), the beat may not work — a
real THz source (L04) would be needed instead.

If dark modes couple to the energy density (quadratic in E,
as in stimulated Raman scattering), the beat works.

**We don't know which is correct.**  L05 tests the
intensity-coupling hypothesis at low cost.  If it fails,
L04 tests the field-coupling hypothesis at higher cost.
Running L05 first is the pragmatic approach.


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
