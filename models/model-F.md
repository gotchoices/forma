# Model: model-F (11D α-derivable architecture) ⟵ ACTIVE

**Status:** Active — R60 complete through Track 20; R62 derivation 7d closes the spin story
**Code:** [`studies/R60-metric-11/scripts/track1_solver.py`](../studies/R60-metric-11/scripts/track1_solver.py) (primitives) plus R60 tracks
**Study range:** R59 (architecture), R60 (spectrum + Z₃ + spin + re-sweep), R62 (spin derivation)
**Supersedes:** [model-E](model-E.md)

---

## TL;DR

Model-F is model-E's spectrum architecture on an 11D metric
(T⁶ × S³ × t × ℵ) with three structural mechanisms that
model-E lacked:

1. **Geometric α coupling** via a `tube ↔ ℵ ↔ t` chain.  Gives
   α structurally universal across sheets, modes, compounds,
   and nuclei (α_Coulomb = Z² α exactly).
2. **Z₃ confinement on the p-sheet**, making (3, 6) the
   observable proton as a three-quark bound state of (1, 2)
   constituents.  Derived from 2ω density-fluctuation
   cancellation (R60 Track 16).
3. **Per-sheet Dirac–Kähler spin**.  Each 2-torus sheet hosts
   a spin-½ fermion tower; compound modes compose via SU(2)
   angular-momentum addition.  The Standard Model taxonomy
   (1-/2-/3-sheet ↔ lepton/meson/baryon) falls out
   structurally.  (R62 derivation 7d, confirmed empirically by
   R60 Track 20.)

**What is derived from geometry:**

- The α-coupling chain (structure, not value)
- σ_ra = (sε)·σ_ta from shear algebra (R60 Track 7)
- α universality across sheets and modes (structural)
- α_Coulomb = Z² α for Z-nuclei (floating-point exact)
- Single-k symmetry k_e = k_p = k_ν = 1.1803/(8π)
- Z₃ selection rule `n_pt ≡ 0 (mod 3)` for free p-sheet modes
  (R60 Track 16)
- Z₃ exemption on the e-sheet via R_loc < 1 (R60 Track 17)
- ν charge = 0 from real-field conjugate-pair structure
  (R60 Track 18)
- Per-sheet spin ½ and SU(2) compound composition (R62 7d)
- Standard Model particle taxonomy from sheet-count
  (R60 Track 20)

**What remains observational input:**

- The *value* α = 1/137.036 (enters as σ_ta = √α)
- Three mass anchors: m_e, m_p, Δm²₂₁
- Geometric inputs from R53/R49/R61: (ε, s) per sheet

**Headline:** model-F matches 14 of 16 non-input inventory
particles within 2%, matches or improves on model-E for every
non-pion particle, gives α = Z² α exactly for nuclei d–⁵⁶Fe
within 1.4%, and produces the Standard Model particle taxonomy
from sheet-count + SU(2) structurally.

Pion desert (10–13% on π⁰, π±) remains the only material
failure; inherited from model-E, candidate for a focused
follow-up study.

---

## Quick facts

**Dimensions and indices.** 11D, ordered
`ℵ, p_t, p_r, e_t, e_r, ν_t, ν_r, S_x, S_y, S_z, t` (R59
convention).

**Baseline configuration** (R60 Track 12 + Track 15 Option A):

| Parameter | Value | Source |
|---|---|---|
| ε_e, s_e | 397.074, 2.0042 | R53 Solution D |
| ε_p, s_p | 0.55, 0.162037 | Model-E |
| ε_ν, s_ν | 2.0, 0.022 | R61 #1 / R49 oscillation constraint |
| k (all sheets) | 1.1803/(8π) = 0.04696 | Emergent single-k |
| g_aa, σ_ta, σ_at | 1, √α, 4πα | R59 F59 natural |
| σ_ra per sheet | (sε)·σ_ta | R60 Track 7 structural |
| σ_ta signs | e: +1, p: −1, ν: +1 | Model-F convention |
| L_ring_e, L_ring_p, L_ring_ν | 54.83, 47.29, 1.96×10¹¹ fm | Calibrated from m_e, m_p, m_ν |

**Primary proton:** (3, 6) on p-sheet as three Z₃-bound (1, 2)
"quark" constituents (R60 Track 15).  Nuclear scaling
`n_pt = 3A, n_pr = 6A, n_et = 1 − Z` (R60 Track 15/19).

**Parameter count:**

| Category | Count |
|---|---:|
| Measured dimensional scales (m_e, m_p, Δm²₂₁) | 3 |
| Measured dimensionless (α) | 1 |
| Geometric inputs from prior studies (ε, s per sheet) | 6 |
| Structural (derived): k, σ_ra per sheet | 4 |
| Fixed at natural form (σ_at, g_aa) | 2 |

Same measured input count as model-E (4).

---

## Architectural principles

Each principle is established by a specific R60 track or R62
derivation; see the referenced finding for the full argument.

### 1. Geometric α coupling (R59 F59, R60 Track 9)

The `tube ↔ ℵ ↔ t` Kaluza–Klein-style chain with natural-form
values (σ_ta = √α, σ_at = 4πα, g_aa = 1) delivers α-strength
coupling from Ma-sheet windings to spacetime.  The coupling
STRUCTURE is derived; the coupling VALUE α = 1/137 is still
input.

### 2. σ_ra structural cancellation (R60 Track 7)

In-sheet shear s creates a ring-to-time leak via
(ring→tube→ℵ→t).  Adding a direct ring↔ℵ entry at
σ_ra = (sε)·σ_ta cancels the leak exactly.  Derivation: in
the 4×4 sub-metric, `det(A)` becomes independent of u = sε.
σ_ra is derived from existing geometry, not a free knob.

### 3. Single-k symmetry (R60 Tracks 7b, 14)

The diagonal scale k = 1.1803/(8π) is the SAME for all three
sheets, confirmed across 6+ tested geometries.  R60 Track 14
confirmed k is a structural fixed point (solver converges
from any init at or above K_NATURAL).  Closed-form derivation
is open; best near-natural candidate (1+4πα)² is 0.97% off.

### 4. Z₃ confinement on the p-sheet (R60 Track 16)

A single (1, 2) "quark" mode on the p-sheet has charge density
that oscillates at 2ω.  Summing N copies at uniform phase
offsets cancels the 2ω fluctuation iff N does not divide 2.
N = 3 is the minimum cancelling N; 120° offsets are a
dynamical energy minimum.  The resulting selection rule:

> **Free p-sheet modes require n_pt ≡ 0 (mod 3).**

(1, 2), (2, 4) are confined "quark" constituents; (3, 6) is
the free proton composite.  Exactly parallels QCD's
"no free quarks, no diquarks, color-singlet triplets only"
— derived from density-fluctuation cancellation on the torus
rather than postulated as a separate SU(3) symmetry.

### 5. Composite α rule (R60 Track 15, 19)

For modes with gcd(|n_pt|, |n_pr|) > 1, the α-sum formula
divides p-tube by gcd:

    α_sum_composite = n_et − n_pt/gcd + n_νt

For gcd = 1 modes (most of model-F's inventory), composite =
bare rule; backward-compatible.  For Z₃-bound triplets like
(3, 6), composite gives α = α (proton sees Coulomb α), while
bare gives 9α (the three-strand sum).  Under the composite
interpretation, the proton has "per-strand charge" of 1·e,
matching observation.

### 6. Z₃ exemption on the e-sheet (R60 Track 17)

Z₃ binding requires the mode's Compton wavelength to fit
inside the sheet's ring circumference:

    R_loc = m_mode · L_ring / ℏc > 1   (binding active)

On the p-sheet: R_loc ≈ 75 (active).  On the ν-sheet:
R_loc ≈ 50 (geometrically permitted — see principle 7 for
why it doesn't bind).  On the e-sheet: **R_loc ≈ 0.14**
(binding suppressed — electron mode is delocalized over the
sheet).  Mechanism is the CONJUNCTION of extreme ε AND magic
shear (|s − n_r/n_t| ≲ 0.035).  The e-sheet's (ε = 397,
s = 2.004) satisfies both; no other sheet does.

Consequence: the electron propagates as a free single (1, 2)
mode (not a three-quark composite), consistent with
observation.

### 7. ν-sheet charge = 0 from real-field structure (R60 Track 18)

Under 7b's real-field picture (adopted after 7c was set
aside), each KK mode is real-valued: Re[exp(i(n_t·y_t/R_t +
n_r·y_r/R_r − ωt))] automatically includes both +n_t and
−n_t components.  The observable state has ⟨n_t⟩ = 0 and
therefore zero tube-direction charge — IF no symmetry-breaking
mechanism distinguishes the +/− tube components.

On the e-sheet, extreme shear breaks this conjugate symmetry
(electron and positron are distinguishable).  On the p-sheet,
Z₃ quark-color structure breaks it (baryons and antibaryons
are distinguishable).  On the ν-sheet, neither breaker is
present — the conjugate pair remains symmetric, giving
ν charge = 0 structurally.

Track 18 also confirmed the three-mode ν interpretation (R61
#1 triplet) reproduces Δm²₃₁/Δm²₂₁ = 33.59 analytically
(s_ν = 0.022 uniquely determined by the ratio 33.6; ε_ν free).

### 8. Per-sheet spin-½ from Dirac–Kähler (R62 derivation 7d)

Each Ma sheet is a flat 2-torus, which admits a Dirac–Kähler
field as privileged fermion content.  KK-reducing gives a
tower of 4D Dirac spinors labeled by winding (n_t, n_r), each
of spin ½ independent of (n_t, n_r).  Three independent
sheets give three fermion families — no index theorem
required.

This is the per-sheet restriction of 7c (the 6D bulk Dirac
attempt).  Advantages: standard flat-T² math (Ivanenko–Landau
1928 / Becher–Joos 1982 / Kogut–Susskind 1975), no chirality
or generation-counting pathologies, compatible with GRID-style
lattice substrates via the staggered-fermion construction.

### 9. Compound spin from SU(2) angular-momentum addition (R60 Track 20)

Multi-sheet compound particles have total spin given by
tensor-product SU(2) composition of per-sheet spin-½
contributions:

| Active sheets | Allowed spins | Particle class |
|:-:|:-:|:---|
| 1 | ½ | **Leptons** |
| 2 | 0 or 1 | **Mesons** (pseudoscalar → 0, vector → 1) |
| 3 | ½ or 3/2 | **Baryons** (octet → ½, decuplet → 3/2) |

**This is the Standard Model particle taxonomy** — not
postulated, emerges structurally from the sheet architecture
+ SU(2) composition.

R60 Track 20 derived this rule empirically by auditing 12
candidate compound-spin rules; unit-per-sheet AM emerged as
the winner (14 of 16 non-input particles within 2%, Standard
Model taxonomy fell out).  R62 derivation 7d provides the
theoretical underpinning.

See [Q124](../qa/Q124-spin-in-mast.md) for the full narrative
of how the spin story was settled.

---

## Inventory

Track 19 produced a Z₃-compliant + composite-α + parity-rule
inventory on the (3, 6) baseline.  Full table in
[R60 findings-19.md](../studies/R60-metric-11/findings-19.md).
Summary:

- **Anchors** (m_e, m_p, ν₁): exact by calibration
- **Single-sheet leptons** (muon, tau): within 0.12% (tau
  via 3-sheet substitute; 1-sheet tau needs mode numbers
  beyond |n| ≤ 6 search, R53 resonance expected to supply)
- **3-sheet baryons** (neutron, Λ, Σ⁻, Σ⁺, Ξ⁻, Ξ⁰):
  within 0.02–0.72%
- **2-sheet mesons** (η, η′, φ, ρ, K⁰, K±): within 0.25–1.12%
- **Pions** (π⁰, π±): 10.4% and 13.3% — the persistent
  "pion desert" (halved from model-E's 22–25% but still out)

All 16 matched tuples satisfy n_pt ≡ 0 (mod 3) (Z₃ rule) and
α = α under the composite rule.

### Nuclear scaling

Scaling law `n_pt = 3A, n_pr = 6A, n_et = 1 − Z` (R60 Track
15/19):

| Nucleus | primary Δm/m | α/α |
|---|:-:|:-:|
| d (²H) | 0.05% | 1 |
| ⁴He | 0.85% | 4 |
| ¹²C | 1.16% | 36 |
| ⁵⁶Fe | 1.37% | 676 |

α_Coulomb = Z² × α exactly for every Z tested (structural).

---

## Three generations

Inherited from model-E / R53 Solution D.  Mass ratios
algebraically determined by (ε_e, s_e) with no free parameters.

Under per-sheet Dirac–Kähler (R62 7d), the three generations
are three KK modes at different (n_t, n_r) windings on the
e-sheet — each spin ½ independent of winding.  The generation
resonance of R53 selects which specific KK excitations are
realized as observable leptons at specific masses.

---

## Open questions

For the full discussion see [R60 findings index](../studies/R60-metric-11/findings.md)
and linked per-track findings.

- **Pion mass desert.**  Persists through all R60 tracks.
  Halved by Track 19 (23% → 10–13%) but not closed.
  Candidate for a focused follow-up study.
- **Single-k closed form.**  k = 1.1803/(8π) confirmed
  structurally; analytical derivation of its specific value
  remains open (R60 Track 14).
- **ν-sheet (1, 0) ghost.**  At R61 #1 geometry, (1, 0) ν
  is lighter than (1, 1).  External filter assumed (R61
  pair-cancellation); pool item.
- **Specific spin within SU(2)-allowed sets.**  R60 Track 20's
  rule gives a SET of allowed spins (e.g., 2-sheet = 0 or 1).
  Which specific spin realized depends on internal structure;
  derivation of the specific-spin selection is a pool item.
- **Per-sheet Dirac–Kähler axiomatization.**  R62 7d treats
  per-sheet Dirac–Kähler as given; a deeper axiomatic
  derivation (likely via GRID lattice staggered fermions) is
  a pool item.
- **Muon tuple ambiguity.**  Track 19 Z₃ search found muon at
  3-sheet (1, 1, −2, −6, 0, 0); Track 20 unit-per-sheet AM
  search found muon at 1-sheet (1, 1, 0, 0, 0, 0) with
  similar mass accuracy.  Under 7d the 1-sheet tuple is the
  physically clean assignment (lepton as 1-sheet particle);
  the 3-sheet tuple is a search artifact.  True lepton
  generations need R53 resonance machinery not implemented
  in the brute-force search.
- **Photon on GRID — rigorous derivation.**  The
  compactification-determines-spin principle extends to
  GRID's aleph (S¹) giving the photon (spin 1), but the
  explicit GRID → Maxwell derivation is a future track (R62
  derivation 11 target).

---

## Comparison to model-E

| Property | Model-E | Model-F |
|---|:-:|:-:|
| Metric dimensionality | 9D | **11D (+ ℵ)** |
| α coupling | Per-mode, geometry-dependent (R19) | **Structural via tube↔ℵ↔t chain** |
| α universality | Not structural | **Structural — same α for every charged particle** |
| Proton mode | (1, 3) bare | **(3, 6) as Z₃-bound (1, 2) triplet** |
| Spin derivation | Parity rule (ad hoc) | **Per-sheet Dirac–Kähler + SU(2) AM** (R62 7d) |
| Standard Model taxonomy | Not derived | **Sheet-count ↔ lepton/meson/baryon structural** |
| Nuclear α_Coulomb | N/A | **Z² α exact** |
| Inventory accuracy | 16/18 at 0.0–1.84% (pions 23–25%) | 14/16 at 0.02–1.12% (pions 10–13%) |
| Nuclear d→⁵⁶Fe | ≤ 1.1% | ≤ 1.4% |
| Measured inputs | 4 (m_e, m_p, Δm²₂₁, α) | 4 (same) |

Model-F has the same measured input count as model-E and the
same pion desert.  What's added: a derivation for the α-
coupling mechanism, a derivation for compound-mode spin (R62
7d), a principled confinement structure for the proton (Z₃ on
p-sheet), a derived charge-zero mechanism for neutrinos, and
halved pion error.

---

## Studies and references

| Study | Focus |
|---|---|
| R59 | Architecture discovery (σ_ta = √α, σ_at = 4πα, g_aa = 1, tube↔ℵ↔t chain) |
| R60 | Full spectrum + Z₃ confinement + spin + inventory re-sweep (Tracks 1–20) |
| R61 | Neutrino sheet candidates |
| R62 | Derivations (1–10 kinematics, 7d spin) |

**Core references:**

- [R60 findings index](../studies/R60-metric-11/findings.md) — all 20 tracks
- [R60 Track 15](../studies/R60-metric-11/findings-15.md) — (3, 6) viability
- [R60 Track 16](../studies/R60-metric-11/findings-16.md) — Z₃ confinement
- [R60 Track 17](../studies/R60-metric-11/findings-17.md) — e-sheet exemption
- [R60 Track 18](../studies/R60-metric-11/findings-18.md) — ν charge and oscillation
- [R60 Track 19](../studies/R60-metric-11/findings-19.md) — inventory re-sweep
- [R60 Track 20](../studies/R60-metric-11/findings-20.md) — compound spin rule
- [R62 derivation 7d](../studies/R62-derivations/derivation-7d.md) — per-sheet Dirac–Kähler spin
- [Q124](../qa/Q124-spin-in-mast.md) — spin story narrative
- Predecessor: [model-E](model-E.md)
