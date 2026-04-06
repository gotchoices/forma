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


---

## Track 1a: Per-sheet energy decomposition and the α² question

Script: `scripts/track1a_decomposition.py`

Four analyses probing the structure of the cross-sheet
coupling, motivated by the review's observation that Track 1
asked about the total eigenvalue when it should have asked
about the coupling cost and whether α² appears in it.


### F9 — The off-diagonal G̃⁻¹ block has no α² structure

The review hypothesized that s_e and s_p are O(α), so
s_e × s_p ∝ α², which would produce α² naturally in the
cross-sheet coupling.  This is wrong.  The shears are:

| Parameter | Value | Ratio to α |
|:---:|:---:|:---:|
| s_e | 0.0959 | 13.1× α |
| s_p | 0.1110 | 15.2× α |
| s_e × s_p | 0.01065 | 200× α² |
| α² | 5.325 × 10⁻⁵ | — |

The shears are O(0.1), not O(α) = O(0.007).  They are
geometric parameters set by the aspect ratio, not by α.
The solve_shear_for_alpha function tunes s to REPRODUCE α
via a nonlinear integral, but the resulting s is not
proportional to α — it's much larger.

The off-diagonal block of G̃⁻¹ has all four components ≈ 0.34,
with no structure that would produce α².  The metric is
dominated by the cross-shear σ_ep, not by the within-sheet
shears.


### F10 — E_cross does NOT scale as α²

Varying α by factors of 0.5× to 2× while keeping ε and
σ_ep fixed:

| α/α₀ | E_cross (eV) | E_cross/α² |
|:---:|:---:|:---:|
| 0.50 | 266,248 | 2.00 × 10¹⁰ |
| 0.70 | 263,881 | 1.01 × 10¹⁰ |
| 1.00 | 260,780 | 4.90 × 10⁹ |
| 1.50 | 256,158 | 2.14 × 10⁹ |
| 2.00 | 251,649 | 1.18 × 10⁹ |

E_cross/α² varies by 246% — far from constant.  When α
doubles, E_cross changes by only 3.5%.  **The cross-sheet
energy is effectively independent of α.**

The α² hypothesis from F8 is ruled out.  The cross-term is
set by σ_ep and the mode windings, not by the shear-derived
α dependence.  The numerical coincidence ΔE_add(σ=0) / E₁ =
m_e/(m_p α²) ≈ 10.2 is exactly that — a coincidence.


### F11 — Schur complement corrections are MeV/keV-scale, not eV

The fixed-L computation (no recalibration of L_ring at each
σ) exposes the raw Schur complement effect on all modes.
At σ_ep = −0.28:

| Mode | ΔE from σ=0 |
|:---|:---:|
| Electron (1,2,0,0,0,0) | +88,478 eV (+88 keV) |
| Proton (0,0,0,0,1,3) | +164,966,116 eV (+165 MeV) |
| Hydrogen (1,2,0,0,1,3) | +165,279,259 eV (+165.3 MeV) |

The proton shifts by **165 MeV** because the metric changes
and L_ring_p is no longer tuned to pin m_p.  The electron
shifts by **88 keV**.  There is **no eV-scale physics** hidden
by recalibration.  The Schur complement operates at the same
scale as the primary coupling — keV to MeV.

The review's hypothesis (F8 point 4) that recalibration might
absorb a eV-scale diagonal binding effect is ruled out.  The
diagonal corrections are 10⁴× to 10⁷× larger than 13.6 eV.


### F12 — Hydrogen and neutron have comparable cross-terms

The review expected the hydrogen cross-term to be much smaller
than the neutron's due to smaller winding numbers.  The actual
comparison at σ_ep = −0.28 for (1,3):

| Mode | E²_ep (MeV²) | E_cross (eV) | Winding product |
|:---|:---:|:---:|:---:|
| Hydrogen (1,2,0,0,1,3) | 489.5 | 260,780 | 12 |
| Neutron (−2,−4,−2,−1,−2,0) | 740.7 | 396,663 | 12 |

**The winding products are identical (12).** The hydrogen mode
has n₁n₅ + n₁n₆ + n₂n₅ + n₂n₆ = 1+3+2+6 = 12, and the
neutron has (−2)(−2) + 0 + (−4)(−2) + 0 = 4+8 = 12.

The cross-term energies differ by only 1.5×, not the 10⁵×
expected.  There is no scale separation between hydrogen and
neutron in the ep cross-sheet coupling.


### F13 — The fundamental barrier: the proton scale

The cross-sheet energy for the hydrogen mode breaks down as:

| Component | E²_contrib (MeV²) | E (eV) |
|:---|:---:|:---:|
| tube_e × tube_p | 80.7 | 43,000 |
| tube_e × ring_p | 132.6 | 70,700 |
| ring_e × tube_p | 104.5 | 55,700 |
| ring_e × ring_p | 171.7 | 91,500 |

All four components are enormous (43–92 keV each).  The reason:
n_p/L_p is O(1) because L_ring_p ≈ 4.5 fm is set by the
proton mass (938 MeV).  When the electron couples to the
proton through the off-diagonal metric block, it inherits the
MeV energy scale from the proton mode.

**Any cross-sheet coupling involving the proton mode will
produce keV-to-MeV effects, not eV effects.**  This is a
structural barrier, not a parameter-tuning problem.  The
proton's n/L values are O(1) fm⁻¹, and (2πℏc)² ≈ 1.54 × 10⁶
MeV²·fm², so the cross-term is inherently ≫ keV.


### F14 — Assessment: the ep coupling cannot produce atomic binding

Track 1a conclusively shows that the electron-proton cross-
sheet coupling (σ_ep) is structurally incapable of producing
eV-scale effects:

1. No α² structure in the metric (F9, F10)
2. No hidden eV-scale Schur complement (F11)
3. No scale separation between hydrogen and neutron (F12)
4. The proton scale (MeV) dominates all cross-terms (F13)

**However**, this does not close all compound-mode avenues.
One path remains unexplored: the **electron-neutrino coupling
(σ_eν)**.  The neutrino sheet has L_ring_ν ≈ 5.7 × 10⁹ fm
(set by the ~meV neutrino mass scale), making n_ν/L_ν
extremely small.  Cross-terms involving the neutrino sheet
would be:

E_cross(eν) ∝ (n_e/L_e) × (n_ν/L_ν) × σ_eν

Since n_ν/L_ν ∝ 1/L_ring_ν ∝ m_ν, these terms scale with
the neutrino mass — naturally producing eV or sub-eV
energies.  If the neutrino sheet mediates atomic binding
(the electron couples to the nucleus THROUGH the neutrino
sheet, not directly), the eV scale could emerge.

This would mean: atoms are NOT electron-proton compounds
but electron-neutrino-proton compounds, with the neutrino
sheet acting as the binding intermediary at the correct
energy scale.
