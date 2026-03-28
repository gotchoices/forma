# R38. Fourth-generation search — does MaSt predict exactly three?

**Questions:** Q86  **Type:** compute  **Depends on:** R26, R27

## Motivation

MaSt produces three charged leptons (e, μ, τ) and three neutrinos
(ν₁, ν₂, ν₃).  The Standard Model offers no explanation for why
there are three generations and not more.  MaSt could:

1. Predict exactly three — a genuine success.
2. Predict more — a tension with the Z width measurement
   (N_ν = 2.996 ± 0.007) and the absence of a 4th charged lepton.
3. Be ambiguous — answer depends on unsolved parts of the model.

Both questions are computationally tractable with existing tools.

## Key constraints

- **Z width:** Exactly 3 light (m < m_Z/2 ≈ 45 GeV) neutrinos
  couple to the Z boson.  N_ν = 2.996 ± 0.007.
- **Direct searches:** No 4th charged lepton observed below ~100 GeV.
- **Tau gap:** The tau candidate is already 5.6% off.  If the 4th
  charged lepton has a larger gap, the off-resonance hypothesis
  predicts it would be far more unstable.


## Tracks

### Track 1. Charged lepton census above the tau

Enumerate all charge −1, spin ½ Ma modes from the tau candidate
(1876 MeV) to 45 GeV using the R27 solver at the pinned parameter
point (r_p = 8.906, σ_ep = −0.0906).

**Deliverables:**
- List of charge −1, spin ½ modes with energies up to ~45 GeV
- For each: mode quantum numbers, energy, gap to nearest observed
  particle (if any)
- The energy of the 4th, 5th, etc. charged lepton modes
- Whether the spectrum naturally terminates or continues indefinitely

**Tools:** `lib/ma_solver.py`, existing R27 parameter point.


### Track 2. Neutrino mode census on Ma_ν

R26 (Assignment A) identified three neutrinos: (1,1), (−1,1), (1,2)
on Ma_ν with s₃₄ = 0.02199 and ε = r = 5.  R26 counted modes
BELOW ν₃ and found zero effective sterile neutrinos.

But modes ABOVE ν₃ with |n₃| = 1 were not counted.  These carry
weak charge per R26 F35 and are sub-eV (light).  Examples:
- (−1, 2) at ~59.5 meV
- (1, 3) at ~87 meV
- (−1, 3) at ~89 meV

If these are independent weakly-charged species, the model predicts
N_ν > 3, contradicting the Z width measurement.

**Deliverables:**
- Complete enumeration of |n₃| = 1 modes on Ma_ν up to ~1 eV
- Count of independent weakly-charged neutrino species
- If N_ν > 3: assess whether a selection rule, coupling suppression,
  or KK momentum conservation could resolve the tension
- If N_ν = 3 exactly: explain the geometric mechanism


### Track 3. Interpretation and gating hypothesis

Combine Tracks 1–2 into a verdict:
- Does MaSt predict exactly 3 generations?
- If not, what physics could gate the generation count?

**Resonance capture hypothesis:** A photon must exceed 2m_e to enter
the Ma domain (pair production).  But a photon far above a cavity's
natural resonance cannot couple stably — it re-radiates.  If the
capture cross-section depends on the detuning between the photon
energy and the cavity mode, the generation count could be bounded
by the mode at which the detuning becomes too large for stable
capture.  The tau is already 5.6% off-resonance; the gap may grow
faster than the mode spacing above the 3rd generation.


### Track 5. Resonance capture

The resonance capture hypothesis: Ma acts as a cavity.  A photon
must exceed 2m_e to enter (pair production), but can only couple
to modes within the cavity's resonance bandwidth.  If the capture
cross-section depends on detuning, there is a natural stability
boundary that could gate the generation count.

**Deliverables:**
- Proton-ring energy ladder and Compton wavelengths vs cavity dimensions
- Cavity Q estimated from the tau's 5.6% off-resonance gap
- Lorentzian capture model: what Q gates the 4th generation?
- Lifetime-gap extrapolation (R27 F33 power law) to 4th generation

**Tools:** `lib/ma_solver.py` (self-consistent metric), R27 parameters.


### Note: Charge formula history

The early WvM model used a Gauss-law integral on an embedded torus,
which selects |n₁| = 1 per sheet (basis for R33's ghost suppression).
The current model uses the full wave function on a sheared flat
geometry, where charge is KK compact momentum: Q = −n₁ + n₅.  The
KK formula gives correct integer charges for all R27 matches; the
WvM integral gives the muon fractional charge (−0.40).  KK is the
current formula.  Its weakness is the ghost problem: ~14,000 modes
carry valid charge.  See `scripts/track4_charge_integral_6d.py` for
the detailed comparison.


## Parameters (all pre-determined)

| Parameter | Value | Source |
|-----------|-------|--------|
| r_p | 8.906 | R27 F18 (muon + neutron) |
| σ_ep | −0.0906 | R27 F18 |
| s₃₄ | 0.02199 | R26 F1 |
| ε (Ma_ν aspect ratio) | ≥ 3.2 (ref: 5.0) | R26 F32 |
| σ_eν, σ_νp | 0 | Default |


## Expected effort

Both tracks are enumerations using existing libraries.
Track 1: one script, ~50 lines.  Track 2: one script, ~30 lines.
Track 3: interpretation only.

Estimated time: 1–2 hours.
