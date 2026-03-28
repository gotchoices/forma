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


### Track 3. Interpretation

Combine Tracks 1–2 into a verdict:
- Does MaSt predict exactly 3 generations?
- If so, this is a genuine prediction with no SM counterpart.
- If not, what physics is needed to reconcile?
- Update Q86 and white-paper outline accordingly.


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
