# Project Status

**Mission:** Build a geometric model of fundamental particles from pure EM
energy — no fundamental charges, no point particles. See [`README.md`](README.md).

**Current model:** [**model-F**](models/model-F.md) (active — 11D
architecture with geometric α-coupling, Z₃ confinement on the
p-sheet, per-sheet Dirac–Kähler spin, and Standard Model
taxonomy from sheet-count + SU(2); α itself still input).
**Latest quantitative predictions:** see [`models/model-F.md`](models/model-F.md)
(14 of 16 compound particles within 1.12%, nuclear scaling d → ⁵⁶Fe
at ≤ 1.4%, R60 Tracks 15–20).
**All models:** [`models/README.md`](models/README.md)

**Studies roadmap:** [`studies/STATUS.md`](studies/STATUS.md)
**GRID (substrate layer):** [`grid/STATUS.md`](grid/STATUS.md) — derives Maxwell + G from a discrete lattice
**Open questions:** [`qa/INBOX.md`](qa/INBOX.md) — [`qa/README.md`](qa/README.md) for index

---

## What has been established

For full details — architecture, inventory tables, mode
assignments, parameter census — see
[`models/model-F.md`](models/model-F.md).  For the framework
reference (dimensions, geometry, mechanisms, particle catalog),
see [`studies/Taxonomy.md`](studies/Taxonomy.md).

**Key results (model-F)** — see [`models/model-F.md`](models/model-F.md)
for detailed architecture and references.

- **Geometric α coupling** — `tube ↔ ℵ ↔ t` chain makes α
  structurally universal across sheets, modes, compounds, and
  nuclei.  α_Coulomb = Z² × α exactly for Z-nuclei.  (Value of
  α is still input.)
- **Z₃ confinement on the p-sheet** — (3, 6) proton as a three-
  quark bound state of (1, 2) constituents, derived from 2ω
  density-fluctuation cancellation (N = 3 is the minimum
  cancelling copy count).  Selection rule: free p-sheet modes
  require n_pt ≡ 0 (mod 3).  Nuclear scaling `n_pt = 3A,
  n_pr = 6A, n_et = 1 − Z`.
- **e-sheet geometric exemption** — R_loc = m·L/ℏc < 1 on the
  e-sheet means the electron mode is delocalized across the
  sheet; Z₃ binding cannot form, so the electron propagates as
  a free single (1, 2) mode.  Derived, not postulated.
- **Per-sheet Dirac–Kähler spin** (R62 derivation 7d) — each
  flat 2-torus sheet hosts a spin-½ fermion tower; compound
  modes compose via SU(2) angular-momentum addition.  The
  Standard Model particle taxonomy (1-/2-/3-sheet ↔ lepton/
  meson/baryon) falls out structurally, not postulated.
- **ν charge = 0 derived** — real-field KK modes are tube-
  conjugate-symmetric; absent a symmetry-breaker (which e and
  p sheets have, ν does not), the tube-direction charge
  averages to zero automatically.
- **Particle spectrum:** 14 of 16 non-input particles within
  1.12% under Z₃-compliant + composite-α search (R60 Track 19,
  several beating model-E).  Pions halved (22–25% → 10–13%)
  but still the persistent failure mode.
- **Three lepton generations** inherited from R53 Solution D;
  mass ratios algebraically exact.
- **Neutrino masses:** Δm²₃₁/Δm²₂₁ = 33.59, analytically
  s_ν = 0.022 uniquely from the ratio.  ε_ν is free; two
  viable candidates (R61 #1, R49 Family A).
- **Single-k symmetry**: k = 1.1803/(8π) uniform across all
  three sheets; structural fixed point, closed form open.

### Deriving G from geometry (R37 → GRID) ✅

**Resolved by GRID:** the [GRID sub-project](grid/README.md)
derives both Maxwell's equations and Einstein's field equations
from a minimal discrete lattice with one geometric constant
(ζ = 1/4) and one measured input (α). See
[`grid/synthesis.md`](grid/synthesis.md) for the full summary.

---

## What remains open

For detailed discussion of each open problem, see
[model-F open questions](models/model-F.md#open-questions).

- **Pion mass desert.**  π⁰ and π± land at ~105–120 MeV
  instead of 135–140 MeV.  Halved by R60 Track 19 (22–25% →
  10–13%) but not closed.  Candidate for a focused follow-up.
- **Single-k closed form.**  R60 Track 14 confirmed
  k = 1.1803/(8π) is a structural fixed point; closed-form
  derivation of its specific value is open.
- **Per-sheet Dirac–Kähler axiomatization.**  R62 derivation 7d
  takes per-sheet Dirac–Kähler as given; a GRID-level lattice
  derivation via staggered fermions is a pool item.
- **Photon on GRID — rigorous derivation.**  Companion to 7d
  for the gauge-boson sector; to be added as a future R62
  derivation.
- **Specific spin within SU(2)-allowed sets.**  Compound-spin
  rule gives allowed sets (2-sheet: {0, 1}; 3-sheet: {½, 3/2});
  which specific spin is realized depends on internal structure
  not yet derived.
- **The hierarchy:** why is gravity ~10⁴⁰× weaker than EM?
- **Flavor:** u/d flavor split within the (1, 2)-quark/(3, 6)-
  proton architecture not yet derived.
- **ν-sheet (1, 0) ghost audit.**  At R61 #1 geometry, (1, 0) ν
  is lighter than (1, 1).  External filter assumed (R61
  pair-cancellation or dark-mode mechanism); not formalized.
- **Cross-sheet structural prescription (pool item h).**  If
  compound fine-tuning requires cross-sheet σ entries, extending
  Track 7's σ_ra prescription is an open task.

---

## Possible future investigations

| Area | Key question | Status | Reference |
|------|-------------|--------|-----------|
| Geometric phase / holonomy | Parallel transport on embedded torus → ghost selection? | Open | Q93 Path 1 |
| Dark matter from ghost modes | Charge cancellation + Compton window → mass ratio 5.4? | **Plausible** | R42, Q94 |
| Strong force from internal EM | α_s ≈ 1 as full internal field? | **Plausible** | Q95 |
| Matter–antimatter asymmetry | Shear chirality → CP violation → baryogenesis? | **Plausible** | Q97, Q32 |
| Force carriers | W/Z as transient reconfigurations; sin²θ_W ≈ 3/13? | Partial | Q96, R43 |
| Fusion as mode transition | Geometry change on Ma rather than particle collision? | **Plausible** | Q89, viz/fusion |
| Moduli potential | What selects the Ma shape (r_e, r_ν)? | Open | Q34, R37 |
| Biological coupling | Can the neutrino sheet serve as an information substrate? | Open | Q78–Q83 |
| α from first principles | Dispersive or geometric derivation of s ≈ 0.01? | Open | Q18, R34 |
