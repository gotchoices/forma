# Project Status

**Mission:** Build a geometric model of fundamental particles from pure EM
energy — no fundamental charges, no point particles. See [`README.md`](README.md).

**Studies roadmap:** [`studies/STATUS.md`](studies/STATUS.md)  
**Open questions:** [`qa/INBOX.md`](qa/INBOX.md) — [`qa/README.md`](qa/README.md) for index

---

## Electron objectives

| # | Objective | Status |
|---|-----------|--------|
| 1 | Spin ½ | **SOLVED** — exact, topological; (1,2) winding on T² |
| 2 | Mass m_e | **SOLVED** (as input) — path length = λ_C fixes scale |
| 3 | Charge e | **OPEN — strong lead** — mechanism understood; q still free |
| 4 | Magnetic moment | **SOLVED** — net axial projection of B on T² |
| 5 | g-factor ≈ 2.0023 | **SOLVED** — WvM energy-partition argument |
| 6 | Zero free parameters | **ESTABLISHED** — topology + e + m_e fully determines geometry |

**What remains for the electron:** determine what selects q (≈ 1/α ≈ 137) —
equivalently, what fixes the shear δ of the T². This is the α problem.

---

## What has been established

- Spin ½ is topological and exact — not an approximation, not an input.
  The (1,2) winding number on a flat T² forces it.
- Charge e is emergent: the time-averaged field of a photon on a (1,2)
  geodesic projects into 3+1D as a Coulomb field. No fundamental charge
  is introduced.
- Mass is confined photon energy. The resonance condition (path = λ_C)
  fixes the scale.
- Magnetic moment and g-factor follow from WvM's energy-partition argument
  (co-rotating vs. non-rotating field components).
- Zero continuous free parameters: given (1,2) topology + e + m_e, the
  geometry is fully determined.
- The compact space must be intrinsically flat (T², not an embedded donut).
  Curved-torus geodesics give wrong results (R12).
- KK gravitational charge is ~10⁻²² × e at the Compton scale — ruled out
  as the charge mechanism (R1).
- The 9% charge deficit in WvM's original formula is an artifact of
  geometric approximations, not a real target (S1).
- Three compact dimensions (T³) are required — T² cannot support
  topological linking needed for hadrons (R14 Track 0).
- m_p = 3 × 612 × m_e to 0.008% (R14 Track 0 result).

---

## Active front

Three studies are currently open:

**R8. Multi-winding electron** ([`studies/multi-winding/`](studies/multi-winding/))  
Finding the torus geometry that self-consistently produces charge, mass,
spin, and magnetic moment. A sheared T² with q ≈ 1/α major orbits and
local 1:2 ratio resolves the Compton path-length constraint. R/r_e ≈ 0.989
is robust. q remains a free parameter — this is still the open edge.

**R13. KK charge from flat T³** ([`studies/kk-charge-t3/`](studies/kk-charge-t3/))  
Compute the 4D effective charge of a photon on a flat T³ geodesic via
Kaluza-Klein field decomposition. The goal: derive apparent charge from
field geometry alone, without using e as input. If the self-energy
constraint (= m_e c²/2) determines the T³ geometry, α becomes a
prediction, not an input.

**R14. Universal geometry — shared T³** ([`studies/universal-geometry/`](studies/universal-geometry/))  
Can a single compact T³ host all particles? Track 0 established that T³
is necessary (T² lacks the topological linking dimension). Three linking
planes map to three color charges. Proton mass checks out. Pending R13.

---

## The central unsolved problem

**What selects q?**

The shear δ of the T² determines q (number of major orbits per Compton
cycle) and hence α = δ/R. The model currently takes q ≈ 137 from the
measured charge — this is circular (R11). Ruled-out mechanisms: EM
self-force, KK gravitational back-reaction, Berry phase. The remaining
lead is R13: derive the charge and self-energy entirely from the KK
field decomposition on flat T³, without using e as input. If that
constrains the geometry, α becomes a geometric prediction.

---

## Long-horizon goals

- **Hadrons from photon knots.** Proton and neutron as three photons
  topologically linked on compact T³. Quark confinement = Borromean
  linking; quarks = per-photon field contributions. (Q26, R14)
- **Mass spectrum.** Why m_e and not some other value? Quantization
  condition from periodic boundary conditions? (Q16)
- **Photon absorption / excited states.** In this model the electron IS
  a photon on T². What does absorbing another photon mean? Does it predict
  discrete spectra? (Q28)
- **Derive α from geometry.** (Q18, Q32, R13)
- **Baryogenesis.** Neutral atoms can form directly from photons (total
  winding zero). No antimatter required. (Q32)

---

## Housekeeping — todo list

Organizational improvements identified. Review and approve before executing.

### 1. Create top-level `qa/` folder  *(done)*
- [x] Create `qa/README.md` explaining purpose and naming convention
- [x] Move `studies/QUESTIONS.md` → `qa/INBOX.md`
- [x] Move `studies/answers/A7-flat-compact-dimensions.md` → `qa/Q07-flat-compact-dimensions.md`
- [x] File questions with substantial content as individual `Q<N>-slug.md` files
- [x] Update all cross-references that point to `studies/QUESTIONS.md` or `studies/answers/`

**Questions ready to be filed individually** (currently buried in INBOX):

| File | Topic | Status |
|------|-------|--------|
| `Q01-compact-dimension-topology.md` | Topological vs. geometric compactification | Answered → A7 |
| `Q05-orthogonality-and-size.md` | Can a sub-uncertainty compact space be orthogonal? | Answerable (standard KK) |
| `Q07-flat-compact-dimensions.md` | Can a compact dimension be flat? | Answered → A7 |
| `Q11-spin-statistics-filter.md` | Why only q = 1 and q = 2? | Answerable (spin-statistics theorem) |
| `Q22-path-closure.md` | Does exact path closure matter? | Largely answered (analytical) |
| `Q33-gravity-vs-charge.md` | Can gravity and charge both arise from photons? | Answered inline — deserves own file |
| `Q18-deriving-alpha.md` | What selects q? (the α problem) | Open but rich — move out of INBOX |
| `Q32-energy-geometry-fundamentals.md` | Energy and geometry as the only fundamentals | Open but rich — move out of INBOX |

### 2. Create `totu/STATUS.md` *(done — this file)*

### 3. Rewrite `studies/STATUS.md` as a clean study registry  *(done)*
- [x] Strip to one job: Active | Backlog | Done
- [x] Objectives table and deep-problem analysis moved to root STATUS.md / qa/
- [x] Crossed-out backlog entries removed
- [x] Done section condensed to one-line table; full record stays in findings.md

### 4. Update `totu/README.md`  *(done)*
- [x] Remove the "Key results so far" bullet list (now in STATUS.md)
- [x] Update Structure section to include `qa/`
- [x] Q27/Q32 pointers already updated in prior step
- [x] Add Navigation table pointing to key entry-point files

### 5. Fix phantom study numbers  *(done)*
- [x] R4 retired (answered in D1/R2), R5 retired (subsumed by R13)
- [x] R9, R10 numbers stripped; questions remain as unnamed backlog items
- [x] Retirement rows added to studies/STATUS.md Done table; qa/INBOX.md updated

### 6. Minor study hygiene  *(done)*
- [x] Added `*(active)*` tag to `kk-charge-t3/README.md`
- [x] Created minimal `README.md` for `dual-visualizer/`

### 7. Separate rich question entries from the capture queue  *(done)*
- [x] Q18, Q29, Q30, Q31, Q32 entries already reduced to Filed table rows (done in prior step)
- [x] Split INBOX.md Filed section into "Answered/Closed" and "Open" subsections; Q30 now in correct section
