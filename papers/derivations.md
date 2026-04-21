# Derivations — From Photon to Particle

**Status:** Program 1 kinematic arc complete (D1–D10).  D7
(spin) has four derivations (7a/7b/7c/7d); **D7d — per-sheet
Dirac–Kähler — is the working selection** based on R60 Track 20
empirical confirmation and architectural coherence with GRID's
photon sector.  The magnetic-moment derivation (pool item g)
is now unblocked in principle.

A roadmap and index for the analytical derivations that put
MaSt on a first-principles foundation.  Each derivation is a
self-contained proof, building on the ones before it.  The
full algebra lives in the study files (linked below); this
paper provides the overview, the "why this step," and the
logical dependencies.

---

## 1. What we derive and from what

### The question

MaSt models particles as standing electromagnetic waves on
compact 2-tori.  The model postulates a mass formula, charge
assignments, spin rules, and coupling constants — and these
postulates successfully reproduce 18 of 20 known particle
masses from 4 inputs.  But postulates are not proofs.

**Can the postulates be derived from more basic principles?**

### The inputs

The entire derivation chain uses only:

| Input | Source | Role |
|-------|--------|------|
| Special relativity | Einstein 1905 | 4-momentum, Lorentz invariance |
| E = hf | Planck 1900 / Einstein 1905 | Converts wavelength to energy (the one quantum input) |
| Standing-wave boundary conditions | Classical wave physics | Single-valuedness on compact domains |
| Differential geometry | Mathematics | Metrics, Christoffel symbols, geodesics |
| The cylinder condition | Klein 1926 | Fields don't vary along compact directions |

No quantum field theory.  No Lagrangians.  No gauge groups
postulated.  No Higgs mechanism.  The gauge structure (U(1)
symmetries, charge conservation, Lorentz force) emerges from
the geometry.

### What falls out

| Derived quantity | Which derivation | Status |
|-----------------|-----------------|--------|
| Rest mass from confinement | D1 (Track 1) | **Complete** |
| Quantized angular momentum | D1 (Track 1) | **Complete** |
| Inertial mass = rest mass | D1 (Track 1) | **Complete** |
| U(1)×U(1) gauge structure | D2 (Track 2) | **Complete** |
| Two-charge Lorentz force | D2 (Track 2) | **Complete** |
| Internal shear as new physics | D2 (Track 2) | **Complete** |
| Photon-on-torus mass formula | D3 (Track 3) | **Complete** |
| Mass-charge mixing from shear | D3 (Track 3) | **Complete** |
| MaSt mass formula μ² = (n_t/ε)² + (n_r − s n_t)² | D4 (Track 4) | **Complete** |
| Charge = tube compact momentum | D5 (Track 5) | **Complete** |
| Universal charge formula Q = −n₁ + n₅ | D5 (Track 5) | **Complete** |
| Dark conservation laws (ring momenta) | D5 (Track 5) | **Complete** |
| Lorentz force on standing-wave states | D6 (Track 6) | **Complete** |
| Minimal coupling derived (not postulated) | D6 (Track 6) | **Complete** |
| Shear is mass-only at centroid level | D6 (Track 6) | **Complete** |
| Spin quantum number (single-sheet) | D7d (per-sheet Dirac–Kähler) | **Selected** — supersedes 7a/7b/7c |
| Compound-mode spin (SU(2) AM composition) | D7d + R60 Track 20 | **Derived** (empirically validated) |
| Standard Model taxonomy (1-/2-/3-sheet ↔ lepton/meson/baryon) | D7d + R60 Track 20 | **Derived structurally** |
| Compound modes on T⁴ (two sheets, cross-shears) | D8 (Track 8) | **Complete** |
| Cross-shears preserve abelian Killing structure | D8 (Track 8) | **Complete** |
| Schur-complement form of mass mixing | D8 (Track 8) | **Complete** |
| Scale-invariance of the KK-on-torus formula | D9 (Track 9) | **Complete** |
| UV consistency (EFT validity window) | D9 (Track 9) | **Complete** |
| Mass formula on full T⁶ (three sheets) | D10 (Track 10) | **Complete** |
| Iterated-Schur form of 6×6 inverse metric | D10 (Track 10) | **Complete** |
| Universal charge Q = e(−n_1 + n_5) from three tube-couples conventions | D10 (Track 10) | **Complete** |
| Magnetic moment from charge + spin (tree level) | *\<future\>* | Planned — pool item g, gated on D7 resolution |

---

## 2. The roadmap

The derivations build in three stages: first the compact
(Ma) physics, then the junction with spacetime (St), and
finally the substrate dimension (ℵ) that links them through
time.

```
══════════════════════════════════════════════════════════
 STAGE 1: Physics on the compact dimensions (Ma, 6D)
══════════════════════════════════════════════════════════

D1: Confined photon → mass + angular momentum  [DONE]
│
│   (special relativity + E = hf + boundary conditions)
│
▼
D2: Kaluza-Klein on a 2-torus                  [DONE]
│
│   (differential geometry + cylinder condition)
│
├──────────────────┬──────────────────┐
▼                  ▼                  ▼
D3: Mass           D5: Charge         D7a/b/c:
[DONE]             [DONE]             Spin
│                  │                  (three alt.
▼                  │                   under eval.)
D4: MaSt μ²        │                      │
[DONE]             │                  <future>:
│                  │                  pool g — mag moment
└─────────┬────────┘                  (gated on D7)
          ▼                               │
       D6: Lorentz force  [DONE] ─────────┘
          │
          ▼
    D8: Two 2-tori with cross-shears  [DONE]
    (compound modes on T⁴, Schur-
     complement mass mixing)
          │
          ▼
    D9: Scale-invariance of the      [DONE]
    KK-on-torus derivations
    (Klein quantization at non-
     Planck scales; hierarchy
     deferred to GRID layer)
          │
          ▼
    D10: Full 6D MaSt on T⁶          [DONE]
    (three sheets, 21-parameter
     internal metric, universal
     Q = e(−n₁ + n₅))


══════════════════════════════════════════════════════════
 STAGE 2: Junction with spacetime (Ma + St = 10D)
══════════════════════════════════════════════════════════

        D10 (6D Ma block established)
              │
              ▼
     ┌────────────────────┐
     │  Spacetime block   │
     │  (3 S + 1 t = 4D)  │
     │  = standard GR     │
     │  Minkowski metric   │
     └────────┬───────────┘
              │
              ▼
     Ma-St off-diagonal block
     (how compact modes source
      fields in spacetime)
              │
              ▼
     Coulomb force, EM radiation,
     gravitational coupling


══════════════════════════════════════════════════════════
 STAGE 3: The ℵ substrate (Ma + ℵ + St = 11D)
══════════════════════════════════════════════════════════

     ┌──── Ma (6D) ────┐
     │                  │
     │   Ma-ℵ coupling  │
     │   (per-sheet     │
     │    ring entries) │
     │                  │
     └──────┬───────────┘
            │
            ▼
     ┌──── ℵ (1D) ─────┐
     │                  │
     │  ℵ diagonal = 1  │
     │  (Planck-scale   │
     │   substrate)     │
     │                  │
     │   ℵ-t coupling   │◄── the seat of α (?)
     │   (links compact │
     │    modes to time) │
     │                  │
     └──────┬───────────┘
            │
            ▼
     ┌──── St (4D) ────┐
     │                  │
     │  3 S + 1 t       │
     │  (flat spacetime) │
     │                  │
     └──────────────────┘
```

**Stage 1** (D1–D10) derives the physics that lives ON the
compact dimensions: mass, charge, the mass formula, compound
modes on T⁴ and T⁶, and the scale-invariance of the whole
construction.  This is the particle spectrum.  Only spin (D7)
remains open, with three alternative derivations (D7a
metric-route, D7b CP-polarization-ratio, D7c 6D Dirac KK) under
evaluation pending a discriminator.

**Stage 2** joins the 6D Ma block to the 4D spacetime block,
producing the 10D metric.  The spacetime block IS standard
GR (Minkowski in the flat limit).  The off-diagonal Ma-St
entries encode how compact modes produce observable effects
in spacetime — the Coulomb field, electromagnetic radiation,
and gravitational coupling.

**Stage 3** adds the ℵ dimension (11D total).  ℵ is the
Planck-scale substrate on which the GRID lattice lives.  It
mediates the Ma-St coupling through time: the Ma-ℵ entries
connect compact modes to the substrate, and the ℵ-t entry
connects the substrate to the time dimension.  Whether ℵ is
the seat of α = 1/137 — the single coupling constant that
sets the strength of electromagnetism — is an open question
explored in R55 and R59.  The derivation of α from geometry
remains the outstanding unsolved problem.

**Dependency summary.**  D3, D5, D7 are independent given D2 —
they can be done in any order.  D6 needs both D3 and D5 (mass
+ charge).  D8 generalizes D2–D6 to two 2-tori.  D9 documents
the scale-invariance that applies to all of D1–D10.  D10
carries D8's machinery to three sheets.  Pool g (magnetic
moment) needs D7 resolved.  Stages 2 and 3 build on Stage 1's
completed 6D block.

---

## 3. The derivations

### D1 — Mass and angular momentum from a confined photon

**File:** [`studies/R62-derivations/derivation-1.md`](
../studies/R62-derivations/derivation-1.md)
**Status:** Complete
**Uses:** SR, E = hf, standing-wave boundary conditions

A photon bouncing between two mirrors (Part A) or orbiting a
ring (Part B) has rest mass m = nh/(Lc) in the cavity's rest
frame.  This mass is also the inertial mass — the system
resists acceleration with coefficient m.

The ring case additionally produces quantized angular momentum
L_z = nℏ from the photon's tangential motion.  The gyroscopic
stability is standard.

**Key results (F1-F3):**
- F1: linear cavity → rest mass + inertia
- F2: ring → rest mass + angular momentum nℏ
- F3: the 2-torus is the natural next step (two confinement
  directions with cross-coupling)


### D2 — Kaluza-Klein on a 2-torus

**File:** [`studies/R62-derivations/derivation-2.md`](
../studies/R62-derivations/derivation-2.md)
**Status:** Complete
**Uses:** D1 + differential geometry, cylinder condition

Generalize KK from one compact circle to a 2-torus (T²).
The 6×6 metric (4 spacetime + 2 compact) produces two
independent U(1) gauge fields (A_μ and B_μ) from the
off-diagonal entries.  Two conserved compact momenta P_4, P_5
are identified as charges.

The genuinely new ingredient vs 5D KK: the **internal shear**
g_45, the off-diagonal entry within the 2×2 compact block.
When g_45 ≠ 0:
- The two gauge fields cross-couple in the Christoffel symbols
- Conserved charges P_a and kinetic velocities w^b are related
  by a non-diagonal matrix
- A pure-charge eigenstate has nonzero kinetic velocity in the
  OTHER compact direction (the origin of MaSt's n_r − s n_t)

**Key results (F4-F6):**
- F4: U(1)×U(1) gauge structure with two conserved charges
- F5: two-charge Lorentz force from the 6D geodesic projection
- F6: shear cross-coupling (new physics with no 5D analog)


### D3 — Photon on a 2-torus: 4D mass from compact momentum

**File:** [`studies/R62-derivations/derivation-3.md`](
../studies/R62-derivations/derivation-3.md)
**Status:** Complete
**Uses:** D1 + D2 + 6D null condition

Replace D2's massive test particle with a photon (null
trajectory in 6D).  The 6D null condition G_AB k^A k^B = 0
splits into:

> η_μν k^μ k^ν = −g_ab k^a k^b

The left side is the 4D mass-shell; the right side is the
compact momentum norm.  Therefore:

> **m²c² = h^ab P_a P_b**

The 4D rest mass is the inverse-internal-metric quadratic
form of the two conserved compact momenta.

For a diagonal, equal-radii torus: m = (h/Lc)√(n₄² + n₅²)
— the Pythagorean mass formula.

With shear: the mass formula has off-diagonal terms that mix
the two compact momenta — mass eigenstates differ from charge
eigenstates.  This is the structural origin of MaSt's
(n_r − s n_t) combination.

**Key results (F7-F10):**
- F7: general mass formula m²c² = h^ab P_a P_b
- F8: Pythagorean special case
- F9: mass-charge mixing from shear
- F10: inertia and Lorentz covariance confirmed


### D4 — Recovery of the MaSt mass formula

**File:** [`studies/R62-derivations/derivation-4.md`](
../studies/R62-derivations/derivation-4.md)
**Status:** Complete
**Uses:** D3 (F7, F8, F9) + explicit parametrization of g_ab in terms of (ε, s)

Map D3's general quadratic form h^ab P_a P_b to MaSt's
empirically-found formula μ² = (n_t/ε)² + (n_r − s n_t)²
by choosing the parametrization g_ab(ε, s).  This closes
the loop: **the MaSt mass formula is derived, not postulated.**

The derivation picks the internal metric
h_{ab} = R²·diag(1/ε², 1) with an off-diagonal shear entry
g_{45} = εs, inverts to get h^{ab}, and substitutes into F7.
The result reproduces MaSt's dimensionless mass formula
exactly.  The derivation also clarifies that MaSt's s
parameter is a **kinematic** shear (a mixing angle in the
compact momentum basis), not the same as the geometric shear
angle of an arbitrary 2×2 metric — they agree on the sheared
direction but differ on normalizations.

**Key results (F11-F13):**
- F11: recovery of MaSt's empirical formula μ² = (n_t/ε)² + (n_r − s n_t)²
- F12: geometric meaning of the (ε, s) parameters (aspect ratio + shear)
- F13: full mode spectrum and ordering (which (n_t, n_r) modes exist and at what mass)


### D5 — Charge identification

**File:** [`studies/R62-derivations/derivation-5.md`](
../studies/R62-derivations/derivation-5.md)
**Status:** Complete
**Uses:** D2 (F4, F5, F6) + one convention (tube-couples)

Adopt one convention: of the two U(1) gauge potentials the
2-torus generates, only the TUBE potential is physical; the
ring potential vanishes (B_μ = 0).  This is motivated by the
empirical observation that only one EM force exists, and it
can always be arranged by a basis rotation on the compact
plane.

With this convention, the U(1)×U(1) of D2 collapses to a
single electromagnetic U(1).  The conserved tube Killing
momentum P_4 IS the electric charge Q, automatically
integer-quantized by standing-wave periodicity:

> Q = e × n_t,  where e = h/(L_t e₀)

Extending to MaSt's three sheets (electron, neutrino, proton)
with per-sheet Ma-S coupling signs (σ_e = −1, σ_ν = 0,
σ_p = +1) recovers the universal charge formula:

> **Q = −n₁ + n₅**

The ring momenta P_2, P_4, P_6 remain conserved but couple to
no 4D field — they are "dark" conservation laws.  They
contribute to mass (via the (n_r − s n_t) term) and to the
discrete particle spectrum, but are electromagnetically
invisible.  These are the geometric origin of generation
labels and non-electromagnetic quantum numbers.

**Key results (F14-F16):**
- F14: charge = tube Killing momentum, quantized as Q = e × n_t
- F15: universal formula Q = −n₁ + n₅ on T⁶ (three sheets)
- F16: ring momenta are conserved but dark (no EM coupling)


### D6 — Lorentz force on the standing-wave state

**File:** [`studies/R62-derivations/derivation-6.md`](
../studies/R62-derivations/derivation-6.md)
**Status:** Complete
**Uses:** D2 (F4, F5) + D3 (F7) + D4 (F11) + D5 (F14) +
  6D massless Klein-Gordon equation + weak external field

The operational closure of the single-sheet arc.  Place a
(n_t, n_r) standing-wave eigenstate in a weak external EM
field A_μ^ext.  In KK, this field IS a metric perturbation
(the off-diagonal G_μ4 = A_μ^ext).

Separate variables on the 6D massless Klein-Gordon equation.
The compact-mode wavefunction factors out, leaving a 4D
effective wave equation for the spacetime envelope ψ:

> D^μ D_μ ψ = (m²c²/ℏ²) ψ

where D_μ = ∂_μ − i(Q/ℏ) A_μ^ext is the gauge-covariant
derivative, m is the F7 mass, and Q is the F14 charge.

**The minimal-coupling structure D_μ = ∂_μ − i(Q/ℏ)A_μ is
NOT postulated — it falls out of the 6D separation of
variables.**  This is one of KK's deepest results, here
extended to the 2-torus.

Taking the eikonal (WKB) limit of this wave equation yields
the relativistic Lorentz-force equation for the centroid:

> m d²x^μ/dτ² = Q F^μ_ν^ext ẋ^ν

with the SAME m and Q derived in earlier tracks.  No new
parameters.

A notable finding: the internal shear g_45 enters only the
mass formula (which modes have which masses), NOT the
gauge-covariant derivative.  Shear is a spectrum effect, not
a force effect.  Mass-charge mixing (F9) determines which
(n_t, n_r) pairs exist; the Lorentz force acts on the
resulting (m, Q) values without further shear dependence.

**Key results (F17-F19):**
- F17: Lorentz force m ẍ = Q F · ẋ with derived m and Q
- F18: minimal coupling D_μ = ∂_μ − iQA/ℏ is geometric, not postulated
- F19: shear affects spectrum only, not the centroid force


### D7 — Spin (resolved by D7d)

**Files:**
[`derivation-7a.md`](../studies/R62-derivations/derivation-7a.md),
[`derivation-7b.md`](../studies/R62-derivations/derivation-7b.md),
[`derivation-7c.md`](../studies/R62-derivations/derivation-7c.md),
[`derivation-7d.md`](../studies/R62-derivations/derivation-7d.md) **(selected)**
**Status:** D7d is the working selection after R60 Track 20
empirical confirmation.  7a, 7b, 7c remain as historical
alternatives with specific domains of validity.
**Uses:** D2 (all four), plus D6/D8 machinery (7b, 7c, 7d)

Four derivations of spin on the 2-torus have been executed.
After extensive empirical evaluation in R60 Track 20 and
architectural alignment with GRID's photon sector
([`grid/photon-from-aleph.md`](../grid/photon-from-aleph.md)),
**D7d is selected as the canonical spin derivation.**  The
earlier three are retained as context and for specific
single-mode domain rulings.

**D7a — Metric route (Killing vectors + holonomy).**  Asks
whether the flat T² metric alone produces spin-½ via a
Killing-algebra dimension count or a Berry / Levi-Civita
holonomy.  Result: neither mechanism works — the Killing
algebra is abelian (u(1)⊕u(1), not so(3)) and the flat-T²
holonomy is trivial.  Spin-1 on T² does follow cleanly from
1-form modes + 4D Lorentz, but spin-½ **is not determined by
the T² metric alone**.  T² nonetheless admits spin-½ fields
once a spin structure is supplied as an external input.
*GRID-native* (uses only bosonic scalar/1-form content).
Lemmas F20–F23.

**D7b — CP field-polarization route (WvM ratio rule).**  Counts
how many times the circularly polarized electric-field vector
rotates per ring circuit.  Arrives at s = n_t/n_r, the
Williamson–van der Mark (1997) ratio.  For the electron (1,2)
and proton (3,6): spin ½.  For the (1,3) proton mode: spin ⅓,
which rules out that mode.  *GRID-native* (uses only the CP
photon, directly realized by GRID's phase field); aligns with
[`papers/matter-from-light.md`](matter-from-light.md) §4.2.
Lemmas F20–F22.

**D7c — 6D Dirac KK-reduction route.**  Decomposes a 6D Dirac
spinor field on M⁴ × T² into 4D Dirac spinors.  Every compact
mode is uniformly spin-½, with mass and charge determined by
the winding numbers exactly as in D3 / D5.  Spin becomes a
field-type label rather than a torus quantum number — it no
longer depends on (n_t, n_r).  **Not GRID-native as written:**
posits a Grassmann (fermionic) Dirac spinor, which is not
part of GRID's axioms.  Retained as the "ambitious 6D bulk"
version of the same idea that D7d realizes more cleanly
per-sheet.  Lemmas F20–F24.

**D7d — Per-sheet Dirac–Kähler (selected).**  Each flat 2-torus
Ma sheet admits a Dirac–Kähler field as its privileged fermion
content.  KK-reducing produces a tower of 4D Dirac spinors
labeled by winding (n_t, n_r), each spin ½ independent of
winding.  Three sheets → three fermion families; compound
particles compose via SU(2) angular-momentum addition
across active sheets.  The Standard Model taxonomy
(1-sheet ↔ lepton, 2-sheet ↔ meson, 3-sheet ↔ baryon) emerges
structurally.  Lemmas F25–F28.

**Why D7d was selected.**  R60 Track 20 evaluated 12 candidate
compound-spin rules empirically and found that the "unit-per-
sheet AM addition" rule best fits the observed particle
inventory (14 of 16 non-input particles within 2%, Standard
Model taxonomy falls out by sheet count).  D7d is the
theoretical underpinning of that empirical winner.  D7d also
parallels GRID's photon derivation ([`grid/photon-from-aleph.md`](
../grid/photon-from-aleph.md)) — both are instances of the
same "compact topology → privileged field type → 4D spin"
principle, applied to different compactifications.

**Status of the alternatives.**  D7a's negative result (no
spin from the metric alone) is preserved and consistent with
D7d (spin comes from the field type, not the metric).  D7b's
ratio rule is demoted from a spin derivation to a mode-
structure rule within its single-sheet domain (identifying
(n, 2n) modes as having special CP-polarization properties,
but not uniquely setting spin).  D7c's bulk Dirac is
recognized as the "global" version of D7d's cleaner per-sheet
restriction.  See [`Q124`](../qa/Q124-spin-in-mast.md) for the
narrative of how the spin question was settled.


### D8 — Two 2-tori with cross-shears (compound modes on T⁴)

**File:** [`studies/R62-derivations/derivation-8.md`](
../studies/R62-derivations/derivation-8.md)
**Status:** Complete
**Uses:** D2 (F4, F5, F6) + D3 (F7, F8, F9) + D6 (F17)

Generalize the single-torus KK analysis to two 2-tori (T⁴ =
T²_A × T²_B), each with its own intra-sheet shear, coupled
by an arbitrary 2×2 cross-shear block C in the 4×4 internal
metric h_{ab}.  The 4D mass formula still reads
m²c² = h^{ab} P_a P_b, but h^{ab} is now the inverse of a
block matrix and is expressed cleanly in Schur-complement
form.  Compound modes — standing waves that span both tori —
arise as the non-pure-A, non-pure-B eigenstates of the joint
system.  The abelian Killing structure survives: four
conserved compact momenta, four U(1) gauge fields, no new
spin content on T⁴.

Setting the cross-shear C = 0 recovers Track 2 as a diagonal
sub-case.  This is the analytical version of what R54 did
numerically (neutron, baryons, mesons as cross-sheet modes)
and is the immediate precursor to the full three-sheet T⁶
analysis in D10.

**Key results (F25-F28):**
- F25: generalized mass formula on T⁴ via Schur complement
- F26: compound modes from cross-shear (particle identity is
  a linear combination of pure-A and pure-B states)
- F27: kinematic mass-charge decoupling — charges remain the
  quantized compact momenta, masses mix via C
- F28: recovery of D2 / Track 2 when C = 0


### D9 — Klein quantization at non-Planck scales

**File:** [`studies/R62-derivations/derivation-9.md`](
../studies/R62-derivations/derivation-9.md)
**Status:** Complete
**Uses:** D1–D3 as inputs; compares against traditional KK
(which sets R ≈ ℓ_Planck)

Addresses an apparent tension: traditional 5D Kaluza-Klein
theory fixes the compact radius R near the Planck length
ℓ_Planck ≈ 1.6 × 10⁻³⁵ m because the compactification is
"pure gravity" and must reproduce Newton's constant G_N.
MaSt's empirical electron-sheet radius, by contrast, sits at
the Compton scale R_e ≈ ℏ/(m_e c) ≈ 4 × 10⁻¹³ m — 22 orders
of magnitude larger.  Does that invalidate the KK structure?

No.  The KK mass formula m = |n|ℏ/(Rc) is **scale-invariant**:
it places no constraint on R beyond "small compared to
experimentally probed length scales".  MaSt treats the
gauge and gravitational backgrounds as *external* fields, not
as compactified pure gravity, so the Planck-scale pinning of
traditional KK does not carry over.  D9 also checks UV
consistency: the effective field theory remains valid for
winding numbers up to N ≈ R / ℓ_Planck ≈ 10²², which is
astronomically larger than any mode MaSt uses (the proton's
largest winding number is 6).  The hierarchy ratio 𝒩 ≈ 10²²
is therefore **inherited as an empirical input**, the same way
the Compton mass of the electron is inherited.  Its ultimate
explanation is deferred to the GRID layer, where the dynamics
that select a specific per-sheet R must eventually live.

**Key result (F29):** the KK-on-torus derivations
(D2–D6, D8) are scale-invariant.  Traditional KK's Planck-scale
pinning is a consequence of its pure-gravity setup and is
not a feature of the kinematic KK machinery itself.  MaSt
inherits the hierarchy question as an open problem without
contradicting KK kinematics.


### D10 — Full 6D MaSt with three sheets

**File:** [`studies/R62-derivations/derivation-10.md`](
../studies/R62-derivations/derivation-10.md)
**Status:** Complete
**Uses:** D1–D6 + D8 (iterated to three blocks)

Extend D8 from two 2-tori to three: T⁶ = T²_e × T²_ν × T²_p
(electron, neutrino, proton sheets) with the full 6×6 internal
metric containing 9 intra-sheet parameters + 12 inter-sheet
cross-shear parameters = 21 independent entries.  The 4D
mass formula m²c² = h^{ab} P_a P_b is unchanged in form; the
6×6 inverse h^{ab} is expressed by an iterated Schur
complement that makes the three-level hierarchy (pure-sheet /
pairwise-compound / triple-compound modes) explicit.

Applying the tube-couples convention independently on each
sheet — with the R54-era empirical signs σ_e = −1, σ_ν = 0,
σ_p = +1 — yields a **universal** charge formula

> Q = e(−n_1 + n_5)

that collapses the six per-tube Killing momenta down to a
single electromagnetic U(1) shared across all three sheets.
The six-term generalized Lorentz force also follows, with
cross-sheet forces mediated entirely through the off-diagonal
cross-shears.  The mode catalog inventories the pure, pair,
and triple-compound candidates; matching these to the full
model-E particle inventory will occur in Program 1's closeout.

Setting specific cross-shear blocks to zero recovers D2, D8,
and D9 as sub-cases, confirming D10 is a strict generalization.

**Key results (F30-F33):**
- F30: mass formula on full T⁶ with the 6×6 internal metric
- F31: iterated Schur-complement structure (hierarchical mass
  mixing: intra-sheet → pairwise cross-sheet → triple
  compound)
- F32: universal charge formula Q = e(−n_1 + n_5) from three
  independent tube-couples conventions
- F33: consistency checks — recovery of D2, D8, D9 as
  sub-cases


### *\<future\>* — Magnetic moment from charge + spin (pool g)

**Status:** Planned.  Was gated on D7; **now unblocked** by
D7d's selection.  Not yet executed.

Once the spin mechanism (D7a / D7b / D7c) is selected, the
magnetic moment at tree level follows from Lorentz covariance
— electric and magnetic fields come as a matched set in F_μν,
so a charge-carrying state with a determined spin
automatically has a magnetic moment.  The KK-on-T²
(or T⁶) analog of the Dirac calculation is expected to give
**g = 2** with no free parameters.  This is the scope of
pool item g in Program 1.

The anomalous moment (g − 2) is explicitly **not** in scope
for Program 1.  Standard QED radiative corrections, which
MaSt inherits once it reproduces the tree-level structure,
handle the Schwinger α/2π term and its higher-order
extensions to ~10⁻¹² precision.  Any **MaSt-specific**
corrections from its KK tower would be a phenomenological
test in a separate R-study.

---

## 4. What remains open

Program 1's remaining work is a short, well-scoped list:

- **D7 — spin (resolved).**  D7d (per-sheet Dirac–Kähler) is
  the working selection, supported by R60 Track 20 empirical
  evaluation and architectural parallel with the photon
  derivation in [`grid/photon-from-aleph.md`](../grid/photon-from-aleph.md).
  D7d gives spin ½ for every single-sheet KK mode and SU(2)
  composition for compounds, reproducing the Standard Model
  particle taxonomy structurally.

- **Magnetic moment (pool g).**  Was gated on D7; now
  unblocked by D7d's selection.  Tree-level g = 2 from charge
  + spin via a KK-on-T² analog of the Dirac calculation.
  Not yet executed; remains in scope for Program 1 closeout.

- **Program 1 closeout (pool z).**  Synthesis of all
  derivations F1–F33 plus pool g, consolidating lemmas and
  identifying derived vs. inherited structure and open
  problems.

And even after those close, these structural questions remain
open and are **not** in Program 1's scope:

- **α = 1/137** is an input, not derived.  The coupling
  constant enters through the Ma-St off-diagonal entries.
  Studies R55 and R59 explored mechanisms but did not derive α
  from geometry alone.

- **The compact-dimension scales** (R_e, R_ν, R_p and the
  hierarchy ratio 𝒩 ≈ 10²²) are inputs.  D9 confirms that
  the KK construction is scale-invariant and places no
  independent constraint on these sizes.  The ultimate
  explanation must come from the GRID layer, which sets the
  dynamics that select the per-sheet R.  This is the
  hierarchy problem in MaSt's language.

- **The strong and weak forces** are partially addressed
  (D8 + D10 show that cross-sheet coupling lives in the
  inter-sheet shears, which is a plausible seat for the
  strong force; the neutrino sheet carrying σ_ν = 0 makes it
  electromagnetically dark, consistent with weak-only
  coupling) but not rigorously derived.  Their full
  derivation is beyond Program 1.

- **GRID ↔ MaSt reconciliation for spin.**  D7d uses per-sheet
  Dirac–Kähler on flat T² (Becher-Joos / staggered-fermion
  construction).  The lattice-level explicit construction in
  GRID's substrate is well-studied in lattice gauge theory but
  has not been formalized for MaSt.  This is the open
  derivation target that 7d's adoption leaves behind.

---

## 5. Relationship to other documents

| Document | Role |
|----------|------|
| [`primers/kaluza-klein.md`](../primers/kaluza-klein.md) | Background: KK theory from scratch, including Lorentz force derivation (Appendix A).  D2 generalizes this to two compact dimensions. |
| [`primers/charge-from-energy.md`](../primers/charge-from-energy.md) | Intuitive narrative of the charge mechanism (bending → leakage → charge).  D5 makes it rigorous. |
| [`primers/size-matters.md`](../primers/size-matters.md) | The Compton view: mass as frequency, particles as cavities.  D1 proves this. |
| [`models/model-E.md`](../models/model-E.md) | The working model whose postulates the derivations aim to prove.  D4 derives its mass formula; D10 would reproduce its full inventory. |
| [`grid/charge-emergence.md`](../grid/charge-emergence.md) | GRID-level charge mechanism (junction leakage from bending).  Complements D5's KK-level derivation. |
| [`grid/photon-from-aleph.md`](../grid/photon-from-aleph.md) | GRID-level photon derivation as KK mode of the ℵ-line (S¹).  Companion to D7d for the photon sector — same compact-topology-determines-spin principle, applied to the substrate dimension. |
| [`Q124`](../qa/Q124-spin-in-mast.md) | Spin story narrative consolidating D7a/b/c/d and Track 20's empirical work. |
| [`papers/gut.md`](gut.md) | The narrative paper ("Good Unification Theory") that tells the story these derivations make rigorous. |
| [`studies/R62-derivations/`](../studies/R62-derivations/) | The study containing the actual derivation files and the full program framing. |

---

## References within the derivation chain

Each derivation produces numbered lemma results (F1, F2, ...)
that subsequent derivations cite.  The chain:

| Result | Statement | Used by |
|--------|-----------|---------|
| F1 | Linear cavity: m = nh/(2Lc), inertia | D3 |
| F2 | Ring: m = nh/(Lc), L_z = nℏ | D3 |
| F3 | 2-torus is the natural next step | D2 framing |
| F4 | U(1)×U(1) gauge structure | D3, D5, D7a |
| F5 | Two-charge Lorentz force | D5, D6, D8 |
| F6 | Shear cross-coupling | D3, D4, D5, D8 |
| F7 | Mass formula m²c² = h^ab P_a P_b | D4, D8, D10 |
| F8 | Pythagorean special case | D4 |
| F9 | Mass-charge mixing from shear | D4, D8 |
| F10 | Inertia on the 2-torus | D6 |
| F11 | MaSt's μ² = (n_t/ε)² + (n_r − s n_t)² recovered | D8, D10 |
| F12 | Geometric meaning of (ε, s) | D8, D10 |
| F13 | Mode spectrum and ordering | D8, D10 |
| F14 | Charge = tube Killing momentum, Q = e × n_t | D6, D10 |
| F15 | Universal charge formula Q = −n₁ + n₅ | D10 |
| F16 | Ring momenta conserved but dark | D6, D10 |
| F17 | Lorentz force with derived m, Q | D8, D10 |
| F18 | Minimal coupling is geometric | — (standalone result) |
| F19 | Shear is mass-only at centroid level | — (standalone result) |
| F20–F23 | Spin, metric route (D7a): Killing algebra is abelian, holonomy trivial — negative result, consistent with D7d (spin not from metric) | Context for D7d |
| F20–F22 | Spin, CP ratio route (D7b): s = n_t/n_r — demoted to single-sheet mode-structure rule | Context for D7d |
| F20–F24 | Spin, 6D Dirac KK route (D7c): bulk Dirac giving uniform spin ½ — superseded by D7d's per-sheet restriction | Context for D7d |
| F25–F28 | Spin, per-sheet Dirac–Kähler (D7d): each 2-torus hosts spin-½ KK tower; SU(2) AM composition for compounds; Standard Model taxonomy structural | **Selected** — used in pool g (magnetic moment) |
| F25 | Generalized mass formula on T⁴ (Schur complement) | D10 |
| F26 | Compound modes from cross-shear | D10 |
| F27 | Kinematic mass–charge decoupling on T⁴ | D10 |
| F28 | Recovery of D2 when C = 0 | — (consistency check) |
| F29 | KK-on-torus scale-invariance; hierarchy inherited, not contradicted | D10, "what remains open" |
| F30 | Mass formula on full T⁶ | pool z (closeout) |
| F31 | Iterated Schur-complement structure on T⁶ | pool z |
| F32 | Universal charge Q = e(−n_1 + n_5) on T⁶ | pool z |
| F33 | Recovery of D2, D8, D9 as sub-cases | — (consistency check) |
