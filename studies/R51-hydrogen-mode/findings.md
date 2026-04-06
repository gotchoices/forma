# R51 Findings

Study: [`README.md`](README.md)

---

## Track 1: Energy cost of adding an electron to a proton

Script: `scripts/track1_electron_addition.py`

Sweeps σ_ep over [−0.30, +0.30] at 301 points for both
proton hypotheses.  At each σ, the model is self-consistently
calibrated so E(electron mode) = m_e and E(proton mode) = m_p
exactly.  The compound hydrogen mode (1,2,0,0,n₅,n₆) is then
evaluated, and two quantities derived:

- ΔE_add = E(hydrogen) − E(proton): the energy cost of
  adding one electron quantum to the proton mode
- I.E. = E(electron) + E(proton) − E(hydrogen): the
  separation energy (freeing the electron mode from the
  compound)


### F1 — Zero-coupling baseline confirmed

At σ_ep = 0 (block-diagonal metric, no cross-sheet coupling),
both proton hypotheses give identical results:

| Quantity | Value | Theory |
|:---|:---:|:---:|
| ΔE_add | 139.149 eV | m_e²/(2m_p) = 139.149 eV |
| I.E. | 510,860 eV | m_e − m_e²/(2m_p) = 510,860 eV |

These confirm the quadrature baseline derived in the README.
The compound mode energy at σ=0 is √(m_e² + m_p²), exactly
as expected from a block-diagonal quadratic form.

The zero-coupling ΔE_add (139 eV) is only 10.2× the hydrogen
ionization energy (13.6 eV) — dramatically closer than R31's
reported 2,830× gap, which was based on comparing to m_e
(511 keV) rather than m_e²/(2m_p).


### F2 — Cross-sheet coupling dominates the compound mode energy

At σ_ep ≠ 0, only the compound mode energy shifts.  The bare
proton and bare electron energies are unchanged at all σ
because the model recalibrates L_ring_e and L_ring_p at each
σ to fix their reference masses.  This is physically correct:
the electron and proton define the sheet geometry, and the
compound mode is a prediction.

The energy decomposition at σ_ep = −0.28 for (1,3):

| Mode | E² components | Cross-sheet |
|:---|:---|:---|
| Proton (0,0,0,0,1,3) | p: 8.804 × 10⁵ MeV² | none |
| Electron (1,2,0,0,0,0) | e: 0.261 MeV² | none |
| Hydrogen (1,2,0,0,1,3) | e: 0.261, p: 8.804 × 10⁵ | **ep: 489.5 MeV²** |

The cross-sheet term (ep) contributes 489.5 MeV² to E² ≈
880,554 MeV² — a 0.056% correction.  But because E² is
quadratic and E is ~938 GeV, even this small fractional change
produces a ~261 keV shift in E.  The cross-sheet coupling is
far too strong to produce eV-scale effects.


### F3 — ΔE_add is roughly linear in σ_ep

The data shows ΔE_add is approximately linear in σ, with
slope ~920 keV per unit σ near σ = 0:

| σ_ep | ΔE_add (eV) | Δ from σ=0 |
|:---:|:---:|:---:|
| 0 | +139.1 | — |
| +0.001 | −781.8 | −920.9 |
| −0.002 | +1,981.0 | +1,841.9 |
| −0.13 | +120,149 | +120,010 |
| −0.28 | +260,956 | +260,817 |

Negative σ increases ΔE_add (makes adding an electron more
expensive).  Positive σ decreases it (makes adding an electron
cheaper and eventually energetically favorable — negative
ΔE_add).


### F4 — ΔE_add crosses 13.6 eV, but at σ ≈ 0

ΔE_add technically crosses 13.6 eV for both hypotheses,
because the range spans [−280 keV, +280 keV].  The crossing
occurs between σ = 0 (ΔE_add = 139 eV) and σ = +0.001
(ΔE_add = −782 eV).  Interpolating linearly:

**ΔE_add = 13.6 eV at σ_ep ≈ +0.00014**

This is essentially zero coupling.  The particle-fitted
σ_ep values (−0.13 to −0.28) are ~2,000× larger in magnitude.
The match is fine-tuned: a 0.001 change in σ shifts ΔE_add by
~920 eV, so hitting 13.6 eV requires σ precision of ~0.00001.


### F5 — I.E. never approaches 13.6 eV

The separation energy I.E. = E_e + E_p − E_H stays in the
range [231 keV, 791 keV] across the full σ sweep:

| Hypothesis | Min I.E. | at σ | Max I.E. | at σ |
|:---:|:---:|:---:|:---:|:---:|
| (1,3) | 230,935 eV | −0.30 | 790,868 eV | +0.30 |
| (3,6) | 224,767 eV | −0.30 | 797,040 eV | +0.30 |

The closest approach to 13.6 eV is ~231 keV — 17,000× too
large.  The separation metric cannot match hydrogen binding.

This is because the zero-coupling I.E. is already ~m_e
(511 keV), and σ can only shift it by ~±280 keV.  To reach
13.6 eV, the entire electron mass would need to be almost
exactly cancelled by the cross-sheet coupling — an
implausible fine-tuning.


### F6 — Both proton hypotheses give nearly identical results

The (1,3) and (3,6) proton modes produce very similar
landscapes because the hydrogen binding physics depends
primarily on the electron-sheet quantum numbers (n₁=1, n₂=2),
which are the same in both cases.  The proton-sheet geometry
enters only through the cross-term coupling strength.

| σ_ep | (1,3) ΔE_add | (3,6) ΔE_add | Difference |
|:---:|:---:|:---:|:---:|
| 0.00 | 139.1 eV | 139.1 eV | 0.0 eV |
| −0.13 | 120,149 eV | 123,779 eV | 3,630 eV |
| −0.28 | 260,956 eV | 267,044 eV | 6,088 eV |

The (3,6) mode couples slightly more strongly (6 ring
windings vs 3), producing a ~2% larger shift.  But the
qualitative picture is identical.


### F7 — Assessment: simple compound mode does not reproduce hydrogen binding

**The simplest compound-mode picture — hydrogen as the
eigenmode (1,2,0,0,n₅,n₆) on the coupled 6-torus — does
not reproduce the 13.6 eV ionization energy at the same
σ_ep that matches particle masses.**

The core problem: the cross-sheet coupling (σ_ep) operates
at the MeV scale.  It shifts the compound mode energy by
hundreds of keV, not by eV.  The neutron mass difference
(1.293 MeV) and the hydrogen ionization energy (13.6 eV)
differ by a factor of ~95,000.  A single coupling constant
cannot produce both scales simultaneously.

At the particle-fitted σ_ep ≈ −0.28:
- ΔE_add ≈ 261 keV (19,200× target)
- I.E. ≈ 250 keV (18,400× target)


### F8 — Where does this leave the compound-mode hypothesis?

The result does NOT rule out atoms as tori phenomena.  It
rules out the simplest version: same σ_ep, same metric,
single compound mode.  Several avenues remain open:

1. **Scale-dependent coupling.**  If σ_ep is not a constant
   but depends on the mode structure (e.g., weaker for
   modes with small electron quantum numbers), the hydrogen
   mode could see a much smaller effective coupling.  The
   electron (n₁=1, n₂=2) might couple ~10,000× more weakly
   than the neutron (n₁=0, n₂=−4, n₅=−2) due to different
   tube/ring geometry.

2. **Neutrino-sheet mediation.**  Atomic binding might
   involve σ_eν (electron-neutrino coupling) rather than
   σ_ep (electron-proton coupling).  If the neutrino sheet
   mediates a much weaker interaction, the eV scale could
   emerge naturally.

3. **Multi-mode description.**  The hydrogen atom might not
   be a single eigenmode but a superposition or product of
   modes — an excitation spectrum rather than a single
   point.  The ionization energy would then emerge from the
   spacing between modes, not from a single eigenvalue.

4. **Second-order effects.**  The E² cross-term is first
   order in σ.  If the binding comes from a second-order
   (Schur complement) correction to the diagonal blocks —
   proportional to σ² and inversely proportional to some
   large quantity — the eV scale might appear naturally.
   This would require the diagonal blocks of G̃⁻¹ to shift
   at σ ≠ 0, which they do NOT in the current model (F2).
   The recalibration of L absorbs any such shift.  A model
   without recalibration might show this effect.

5. **The 139 eV coincidence.**  The zero-coupling ΔE_add =
   m_e²/(2m_p) = 139 eV is tantalizingly close to the
   hydrogen ionization energy (10.2× off).  This ratio
   10.2 ≈ 1/α (= 137) to 7% accuracy.  Whether this is
   numerology or a hint that α mediates the reduction from
   139 eV to 13.6 eV is worth exploring.  If ΔE_add at the
   physical coupling were m_e²/(2m_p) × α = 139 × (1/137)
   ≈ 1.02 eV, that would be the Rydberg energy (13.6 eV /
   13.3 ≈ 1.02 eV).  The Rydberg constant IS
   R∞ = m_e α² / 2 = m_e²α²/(2m_e), and for hydrogen
   E₁ = m_e α² / 2 = 13.6 eV.  So:
   - ΔE_add(σ=0) = m_e²/(2m_p) = 139 eV
   - Hydrogen E₁ = m_e α²/2 = 13.6 eV
   - Ratio: m_e/(m_p α²) = 511,000/(938,272,000 × (1/137)²)
     = 511,000/49,983 = 10.22

   This means: **ΔE_add(σ=0) / E₁ = m_e/(m_p α²) ≈ 10.2.**
   The hydrogen ionization energy is the zero-coupling
   addition cost scaled down by exactly m_p α² / m_e.
   Whether this relation has physical content (α enters
   through some coupling mechanism we haven't identified)
   or is coincidental is an open question for future tracks.
