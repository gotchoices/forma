# R38 Findings — Fourth-generation search

See [`README.md`](README.md) for motivation and study plan.


---

## Track 1: Charged lepton census

**Script:** [`scripts/track1_charged_lepton_census.py`](scripts/track1_charged_lepton_census.py)


### F1. The Ma spectrum is dense — no natural cutoff at three

Scanning all charge −1, spin ½ modes with |n_i| ≤ 15 at the
R27 parameter point (r_p = 8.906, σ_ep = −0.0906):

| Energy band | Distinct levels |
|-------------|-----------------|
| Below electron (0–0.5 MeV) | 3 |
| Electron to muon (0.5–106 MeV) | 66 |
| Muon to proton mass (106–938 MeV) | 1,095 |
| Proton to tau (938–1877 MeV) | 1,783 |
| Above tau (1877–10000 MeV) | 11,065 |
| **Total below 10 GeV** | **14,012** |

This is the ghost mode problem (R33) applied to generations.


### F2. The proton-scale energy ladder

The simplest charged lepton modes follow the proton-tube ladder:

    E(1, 2, 0, 0, 0, n₆) ≈ |n₆| × 469.8 MeV   (for |n₆| ≥ 1)

| n₆ | E (MeV) | Particle |
|----|---------|----------|
| 0 | 0.5 | electron |
| ±1 | 469.8 | — |
| ±2 | 939.6 | (neutron mass) |
| ±3 | 1409.4 | — |
| ±4 | 1879.2 | tau candidate (obs: 1776.9) |
| ±5 | 2349.0 | 4th lepton candidate |
| ±6 | 2818.8 | 5th lepton candidate |

The tau sits on the 4th rung (5.6% off).  The next candidate is
at ~2349 MeV — well above any observed lepton.


---

## Track 2: Neutrino mode census

**Script:** [`scripts/track2_neutrino_census.py`](scripts/track2_neutrino_census.py)


### F3. Ma_ν produces far more than 3 weakly-charged neutrino species

At R26 parameters, all modes with |n₃| = 1 carry weak charge
(R26 F35).  All are sub-eV.

| Cutoff | Independent species |
|--------|--------------------:|
| 0.1 eV | 7 |
| 1.0 eV | 69 |
| m_Z/2 = 45.6 GeV | 1,001 |


### F4. The 4th neutrino is (−1, 2) at 59.45 meV

| Mode | Mass (meV) | Status |
|------|------------|--------|
| ν₁ = (1, 1) | 29.21 | Identified |
| ν₂ = (−1, 1) | 30.47 | Identified |
| ν₃ = (1, 2) | 58.17 | Identified |
| **(−1, 2)** | **59.45** | **4th species** |

Only 1.28 meV above ν₃, weakly charged, not a CPT conjugate
of any identified neutrino.


### F5. Tension with the Z width

The Z width gives N_ν = 2.996 ± 0.007.  The model predicts
1,001 light weakly-charged species — a 140σ tension.

This may be resolvable: the weak coupling in MaSt is not yet
derived from geometry.  If the weak interaction has its own
selection rules (analogous to EM charge from shear), the count
could be restricted.  Alternatively, ghost mode suppression (R33)
could apply to neutrino modes as well.


---

## Track 3: Interpretation


### F6. Three generations are accommodated but not predicted

The model matches the three observed charged lepton masses
(electron exactly, muon exactly, tau at 5.6%) and the three
neutrino mass splittings.  This is a genuine achievement.

However, these three modes sit among thousands with identical
quantum numbers.  The question "why three?" reduces to the ghost
mode problem: why are most modes dark?  Solving R33 would
automatically resolve the generation count.


---

## Track 5: Resonance capture

**Script:** [`scripts/track5_resonance_capture.py`](scripts/track5_resonance_capture.py)


### F7. The proton-ring ladder has no geometric cutoff

The charged lepton ladder E(−1, +5, 0, 0, −2, n₆) continues
indefinitely.  Mode energies for the first 8 rungs:

| n₆ | E (MeV) | Particle |
|----|---------|----------|
| 0 | 105.7 | muon (matched) |
| ±1 | 476–487 | — |
| ±2 | 940–951 | — |
| ±3 | 1408–1419 | — |
| ±4 | 1876–1888 | tau (5.6% off) |
| ±5 | 2346–2357 | 4th candidate |
| ±6 | 2815–2827 | 5th candidate |

There is no mode-counting reason to stop at three.


### F8. Cavity Q determines whether the 4th generation is capturable

Modeling the Ma cavity as a Lorentzian resonator with quality
factor Q:  σ(E) ∝ 1/(1 + (2δ/Γ)²),  Γ = E_mode/Q.

From the tau's 99.6 MeV detuning:

| Tau capture efficiency | Required Γ | Implied Q |
|:----------------------:|:----------:|:---------:|
| 50% | 199 MeV | 9.4 |
| 25% | 115 MeV | 16 |
| 10% | 66 MeV | 28 |
| 1% | 20 MeV | 94 |

At Q ≈ 10, the tau is captured at ~47% efficiency and the 4th
generation could tolerate a gap up to ~125 MeV.  At Q ≈ 30,
the tau is barely captured (~9%) and the 4th generation would
need a gap smaller than the tau's to survive — a plausible
gating condition.


### F9. The lifetime-gap power law constrains 4th-generation stability

R27 F33/F39 found τ ∝ |gap|^(−2.7) for weak CC decays (r = −0.84).
Extrapolating from the tau (gap = 5.6%, τ = 2.9 × 10⁻¹³ s):

| Gap | Predicted lifetime | × shorter than tau |
|:---:|:------------------:|:------------------:|
| 10% | 6 × 10⁻¹⁴ s | 5× |
| 15% | 2 × 10⁻¹⁴ s | 14× |
| 30% | 3 × 10⁻¹⁵ s | 93× |
| 50% | 8 × 10⁻¹⁶ s | 370× |

A 4th lepton with 15–30% gap would live 10⁻¹⁴ to 10⁻¹⁵ s —
too short to detect with current methods but still above the
strong-decay scale.  The combination of a large gap (reducing
the capture cross-section) and a short lifetime (reducing
the detection window) could explain non-observation.


### F10. The hypothesis is viable but underdetermined

The resonance capture model requires one unknown parameter
(the cavity Q or equivalently the Ma-S coupling bandwidth).
With Q ≈ 30, the tau sits at the edge of capture and the 4th
generation is gated out.  But Q cannot yet be computed from
first principles.

The three charged lepton gaps are:
- e⁻: 0.0% (input)
- μ⁻: 0.0% (input)
- τ⁻: 5.6% (only predictive data point)

One data point cannot establish a trend.  Whether the gap
systematically grows with n₆ is the key open question.
Resolving it requires either:
1. A first-principles model of Ma-S coupling (gives Q)
2. Multi-mode or asymmetric shear analysis (explains the
   tau's 5.6% gap and predicts the 4th generation's gap)


---

## Note: Charge formula history

R19 derived a charge integral under the original WvM picture
(photon as an embedded torus with circularly polarized E-field).
That integral selects |n₁| = 1 per sheet and was the basis for
R33's ghost suppression (~4 ghosts per sheet).

The current model uses the full wave function on a sheared flat
geometry, where charge arises from KK compact momentum:
Q = −n₁ + n₅.  This gives correct integer charges for all R27
particle matches (muon, kaon, pion, baryons) — the WvM integral
gives the muon fractional charge (−0.40) and the kaon zero charge.

The KK formula is the right one for the current model.  Its
weakness is exactly the ghost problem: every mode with the right
quantum numbers carries integer charge, producing ~14,000 levels
where nature shows 3.  The R19 WvM integral may still describe
a coupling form factor (how strongly a mode radiates) rather than
the charge itself, which could contribute to ghost suppression,
but this is speculative.

Script: [`scripts/track4_charge_integral_6d.py`](scripts/track4_charge_integral_6d.py)
documents the comparison in detail.


---

## Summary table

| # | Finding |
|---|---------|
| F1 | 14,012 charge −1 spin ½ levels below 10 GeV — dense spectrum, no natural cutoff at three |
| F2 | Proton-scale ladder: 4th lepton candidate at ~2349 MeV (n₆ = ±5) |
| F3 | 1,001 weakly-charged neutrino species below m_Z/2 |
| F4 | 4th neutrino species: (−1, 2) at 59.45 meV, 1.28 meV above ν₃ |
| F5 | 140σ tension with Z width — may be resolvable via weak coupling derivation or ghost suppression |
| F6 | Three generations accommodated (masses matched) but not predicted (reduces to ghost problem) |
| F7 | Proton-ring ladder has no geometric cutoff — modes continue to arbitrary n₆ |
| F8 | Cavity Q ≈ 30 gates the tau at the edge of capture and excludes the 4th generation |
| F9 | Lifetime-gap power law: 4th lepton at 15% gap → τ ≈ 2 × 10⁻¹⁴ s (14× shorter than tau) |
| F10 | Resonance capture hypothesis is viable but underdetermined — needs Ma-S coupling model for Q |


## Scripts

- [`scripts/track1_charged_lepton_census.py`](scripts/track1_charged_lepton_census.py)
  — Charged lepton mode enumeration at R27 parameter point
- [`scripts/track2_neutrino_census.py`](scripts/track2_neutrino_census.py)
  — Neutrino mode census on Ma_ν
- [`scripts/track4_charge_integral_6d.py`](scripts/track4_charge_integral_6d.py)
  — WvM vs KK charge comparison (historical reference)
- [`scripts/track5_resonance_capture.py`](scripts/track5_resonance_capture.py)
  — Resonance capture model: cavity Q, lifetime extrapolation, gating analysis
