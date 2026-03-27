# Project Status

**Mission:** Build a geometric model of fundamental particles from pure EM
energy — no fundamental charges, no point particles. See [`README.md`](README.md).

**Studies roadmap:** [`studies/STATUS.md`](studies/STATUS.md)  
**Open questions:** [`qa/INBOX.md`](qa/INBOX.md) — [`qa/README.md`](qa/README.md) for index

---

## Electron objectives

| # | Objective | Status |
|---|-----------|--------|
| 1 | Spin ½ | **SOLVED** — exact, topological; (1,2) winding on the material sheet |
| 2 | Mass m_e | **SOLVED** (as input) — path length = λ_C fixes scale |
| 3 | Charge e | **OPEN — strong lead** — mechanism understood; q still free |
| 4 | Magnetic moment | **SOLVED** — net axial projection of B on the material sheet |
| 5 | g-factor ≈ 2.0023 | **SOLVED** — WvM energy-partition argument |
| 6 | Zero free parameters | **ESTABLISHED** — topology + e + m_e fully determines geometry |

**What remains for the electron:** determine what selects q (≈ 1/α ≈ 137) —
equivalently, what fixes the shear δ of the material sheet. This is the α problem.

---

## What has been established

- Spin ½ is topological and exact — not an approximation, not an input.
  The (1,2) winding number on a flat material sheet forces it.
- Charge e is emergent: the time-averaged field of a photon on a (1,2)
  geodesic projects into 3+1D as a Coulomb field. No fundamental charge
  is introduced.
- Mass is confined photon energy. The resonance condition (path = λ_C)
  fixes the scale.
- Magnetic moment and g-factor follow from WvM's energy-partition argument
  (co-rotating vs. non-rotating field components).
- Zero continuous free parameters: given (1,2) topology + e + m_e, the
  geometry is fully determined.
- The material space must be intrinsically flat (a material sheet, not an embedded donut).
  Curved-torus geodesics give wrong results (R12).
- KK gravitational charge is ~10⁻²² × e at the Compton scale — ruled out
  as the charge mechanism (R1).
- The 9% charge deficit in WvM's original formula is an artifact of
  geometric approximations, not a real target (S1).
- Three material dimensions (T³) are required — a single material sheet cannot support
  topological linking needed for hadrons (R14 Track 0).
- m_p = 3 × 612 × m_e to 0.008% (R14 Track 0 result).

---

## Active front

Three studies are currently open:

**R8. Multi-winding electron** ([`studies/R8-multi-winding/`](studies/R8-multi-winding/))  
Finding the torus geometry that self-consistently produces charge, mass,
spin, and magnetic moment. A sheared material sheet with q ≈ 1/α major orbits and
local 1:2 ratio resolves the Compton path-length constraint. R/r_e ≈ 0.989
is robust. q remains a free parameter — this is still the open edge.

**R13. KK charge from flat T³** ([`studies/R13-kk-charge-t3/`](studies/R13-kk-charge-t3/))  
Compute the 4D effective charge of a photon on a flat T³ geodesic via
Kaluza-Klein field decomposition. The goal: derive apparent charge from
field geometry alone, without using e as input. If the self-energy
constraint (= m_e c²/2) determines the T³ geometry, α becomes a
prediction, not an input.

**R14. Universal geometry — shared T³** ([`studies/R14-universal-geometry/`](studies/R14-universal-geometry/))  
Can a single material T³ host all particles? Track 0 established that T³
is necessary (a single material sheet lacks the topological linking dimension). Three linking
planes map to three color charges. Proton mass checks out. Pending R13.

---

## The central unsolved problem

**What selects q?**

The shear δ of the material sheet determines q (number of major orbits per Compton
cycle) and hence α = δ/R. The model currently takes q ≈ 137 from the
measured charge — this is circular (R11). Ruled-out mechanisms: EM
self-force, KK gravitational back-reaction, Berry phase. The remaining
lead is R13: derive the charge and self-energy entirely from the KK
field decomposition on flat T³, without using e as input. If that
constrains the geometry, α becomes a geometric prediction.

---

## Long-horizon goals

- **Hadrons from photon knots.** Proton and neutron as three photons
  topologically linked on material T³. Quark confinement = Borromean
  linking; quarks = per-photon field contributions. (Q26, R14)
- **Mass spectrum.** Why m_e and not some other value? Quantization
  condition from periodic boundary conditions? (Q16)
- **Photon absorption / excited states.** In this model the electron IS
  a photon on the material sheet. What does absorbing another photon mean? Does it predict
  discrete spectra? (Q28)
- **Derive α from geometry.** (Q18, Q32, R13)
- **Baryogenesis.** Neutral atoms can form directly from photons (total
  winding zero). No antimatter required. (Q32)

