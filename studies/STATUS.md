# Project Status

**Goal:** Build a geometric model of fundamental particles from
pure electromagnetic energy.  See top-level `README.md`.

**Workflow:** See `README.md` for conventions.

---

## Electron objectives

The near-term goal is a complete electron model.  Each objective
has a status and a note on what remains.

### 1. Spin ½
**Status: SOLVED** (S3, R2, R8 Track 2)

Exact, topological for the standard (1,2) knot.  R8 Track 2
confirmed spin ½ is exact on a sheared T²: the physical winding
ratio is exactly 1:2 (68.5/137) with coprime lattice numbers
(68, 137), preserving the local helical structure.

### 2. Mass m_e
**Status: SOLVED** (given input) (R2)

Path length = λ_C = h/(m_e c) fixes the absolute scale.  The
model does not predict WHY the electron has this mass — it takes
m_e as input and derives the geometry.  Predicting the mass
spectrum (why m_e, m_μ, m_τ?) is a long-term open problem.

### 3. Charge e
**Status: OPEN — strong lead** (S2, R6, R7, R8)

R8 resolved the R7 energy shortfall: a multi-winding path on a
sheared T² fits λ_C of path on a torus of radius R ≈ r_e,
where the Coulomb self-energy is m_e c²/2.  R/r_e ≈ 0.989 is
robust across resolutions.

However, q remains a free parameter.  Track 4 found δ ≈ αR
(within ~6%), suggesting EM self-interaction as the origin of
the shear, but Track 5 showed this is approximate, not exact.
**Remaining:** determine what selects q (and hence r and δ).

### 4. Magnetic moment
**Status: SOLVED** (WvM §5, charge-from-energy primer §4)

The direction is understood: B tangent to the compact surface
has a net axial component when mapped to 3D (geometric
projection of k̂ × E, not a current loop).  The g-factor
g ≈ 2(1 + α/2π) comes from WvM's energy-partition argument.
Documented in [`ref/charge-from-energy.md`](../ref/charge-from-energy.md) §4.

### 5. g-factor ≈ 2.0023
**Status: SOLVED** (WvM §5, R2)

Depends on α (fraction of energy in external non-rotating field),
not on geometry.  Near-exact match to QED first-order result.

### 6. Zero free parameters
**Status: ESTABLISHED** (R2, R6)

Given (1,2) topology + charge e + mass m_e, the geometry is fully
determined.  No continuous free parameters.  The numerical values
depend on the charge calculation method (r ≈ 6.60 from S2's
approximate formula, r ≈ 4.29 from R6's self-consistent version).
Final values await objective 3.

---

## Deeper open problems

These go beyond "reproduce known properties" toward the
long-term goal.

- **Derive α from geometry.** (Q18, Q29, Q30)
  R8 Track 4 found δ ≈ αR (within ~6%).  The shear selects
  q and hence α.  But what selects the shear?

  **Ruled out:**
  - *EM self-force:* photons don't couple to EM fields
    (superposition principle).
  - *Gravitational self-force / KK self-consistent metric:*
    R1 showed KK gravity is ~10⁻²² × e at the electron scale.
    The gravitational back-reaction Gm_e/(Rc²) ~ 10⁻⁴³ is
    41 orders of magnitude too weak to produce δ/R ~ α ~ 10⁻².
  - *Berry phase:* wrong scaling (Track 4).

  **R11 result (COMPLETE):** Eight tracks of investigation
  found no mechanism that selects q = 137 from energy cost
  or primality.  Coulomb energy favors low q (monotonic).
  Five linear tests found no prime/composite distinction.
  **Crucially, q ~ 1/α is partly tautological** — it follows
  from the input charge e via dimensional analysis.  The real
  free parameter is r (aspect ratio), not q.

  **Remaining lead → R12:**
  - *EM self-consistency (wave equation on T²):* Solve
    Maxwell's equations (or a scalar proxy) on the sheared T²
    WITHOUT using e as input.  If self-consistent solutions
    exist only for specific shear values, α is predicted from
    geometry alone.  This is the path to breaking the
    circularity and making the model genuinely predictive.

  **Context on running of α:**
  α runs in QED (1/137 → ~1/128 at Z-mass), but q must be an
  odd integer, so the geometric α is discrete.  The running
  likely reflects vacuum polarization screening in 3+1D, not
  changes in compact geometry.  The bare α (from geometry) is
  fixed; the dressed α (measured) runs due to virtual-pair
  screening.
- **Mass spectrum.**  Why m_e and not some other value?
  Is there a quantization condition that selects discrete masses?
  (Q16)
- **Hadrons from multi-photon knots.**  Proton and neutron as
  three photons knotted on the compact T², with quark
  confinement arising from the topological linking.  (Q26)
- **Photon absorption / excited electrons.**  What does it
  mean for a photon-on-T² to absorb another photon?  Can
  excited states be modeled as more energy loaded into the
  compact space, and does this predict discrete spectra?
  (Q28)

### Resolved by axioms

- **~~Confinement mechanism.~~**  In WvM's 3+1D picture, the
  photon must somehow be forced into a loop — a real puzzle.
  In the compact-dimension framework, this dissolves: the photon
  travels in a straight line on a flat T² that is periodic.  It
  wraps because the space wraps.  If "compact dimensions exist"
  is axiomatic, no confinement mechanism is needed.  (See Q27.)

---

## Active

### R8. Multi-winding electron
**Study:** [`multi-winding/`](multi-winding/)
**Question:** Q18  **Type:** compute  **Depends on:** R7
**Advances:** objectives 1, 3 (spin, charge)

Find the torus geometry (R, a, winding number q) that produces
the electron's charge, mass, spin, and magnetic moment.  R7
showed the torus must be ~100× smaller than Compton scale; a
multi-winding path (~1/α major orbits, local 1:2 ratio) can
fit λ_C of path length on a torus of radius ~r_e.  Spin ½ is
expected from the local winding ratio.

### R12. Self-consistent fields on sheared T²
**Study:** [`self-consistent-fields/`](self-consistent-fields/)
**Question:** Q18, Q29  **Type:** compute  **Depends on:** R8, R11
**Advances:** deeper problem (derive α)

The key insight from R11: q ~ 1/α is tautological (follows
from using the measured charge as input).  To break the
circularity, solve for field configurations on the sheared T²
that are self-consistent WITHOUT assuming the value of e.

Approach: solve the wave equation (scalar first, then full
Maxwell) on a family of sheared T² geometries parameterized
by the shear δ (or equivalently the aspect ratio r).
Determine which shear values permit self-consistent,
single-valued, normalizable solutions.  If only discrete
shear values work, α is predicted from geometry alone.

---

## Backlog

Ordered roughly by priority.  Items get an R-number when
promoted to Active.

### ~~Wave equation on sheared T²~~ → PROMOTED to R12
**Absorbed into R12.**  Now the active study.

### ~~Variational principle for α~~ → partly addressed by R11
**Question:** Q29, Q30  **Type:** compute
**Advances:** deeper problem (derive α)

R11 tested energy-cost and primality approaches.  Result:
Coulomb cost favors low q (no minimum at 137); five linear
tests found no prime/composite distinction.  The variational
idea remains valid in principle but requires a richer energy
functional (e.g., including magnetic energy or shear
stiffness) that R12's field solutions may provide.

### ~~Prime resonance test~~ → DONE (R11, negative result)
**Question:** Q30  **Type:** compute

**Result:** R11 Tracks 1, 2c, 7, 8 — eight tracks total.
All linear analyses are blind to primality.  q enters the
flat-T² spectrum as a continuous parameter (1/(2q)), not
through its factorization.  The hypothesis remains viable
only in the nonlinear/curved-torus regime, which would
require a significantly more complex computation.


### Flat space → curved appearance
**Question:** Q2  **Type:** reason

If compact dimensions are flat, how do the photon's fields
project into 3+1D? The 6D decomposition from R1 provides the
framework; what remains is working out the field projection.

### Quadrupole correction
**Question:** Q10  **Type:** compute  **Depends on:** R6
**Advances:** objective 3 (charge)

Full calculation of charge including the (1,2) orbit's ~2.5%
field anisotropy (quantified in S2 F5).

### Precession of torus axis
**Question:** Q19  **Type:** compute

What drives axis precession? Does it restore spherical symmetry?

### Orbit precession and volume-filling
**Question:** Q23  **Type:** compute

Does a precessing (1,2) orbit reproduce WvM's volume-filling
energy flow (Fig. 2)?

### Hadrons from multi-photon knots
**Type:** compute/reason  **Questions:** Q12, Q13, Q26
**Advances:** deeper problem (other particles)

Can protons and neutrons be built from three photons
**topologically knotted** on the compact T²?  The key insight:
if three photons are linked in a knot configuration, no single
photon can be extracted without cutting through another —
giving automatic quark confinement as a topological property
rather than a dynamical force.  "Quarks" would be the
individual photon contributions to the composite field.

Open questions:
- Three photons in a Borromean or trefoil-like linking?
- Does each photon's winding topology produce the 1/3 and 2/3
  charge fractions?
- What knot/linking gives charge +e, spin ½, mass 938 MeV
  (proton) vs charge 0, spin ½, mass 940 MeV (neutron)?
- Deep inelastic scattering sees three point-like scattering
  centers.  Can a three-photon knot reproduce this?
- S3 found that the WvM charge formula maps specific a/R values
  to fractional charges — consistent with per-photon
  contributions.

### Photon absorption and excited electrons
**Type:** reason/compute  **Questions:** Q28
**Advances:** deeper problem (photon absorption)

In the compact-dimension model the electron IS a photon on T².
When a standard QM electron "absorbs a photon," what happens
in this picture?

Candidate mechanisms:
- The incoming photon enters the compact space and adds energy
  to the existing mode (higher harmonic, larger amplitude)
- The compact geometry reshapes to accommodate the extra energy
- The incoming photon remains in 3+1D, coupling to the compact
  field as a composite state

If excited electrons are "more energy in the same T²," the
periodic boundary conditions should impose discrete allowed
increments — potentially reproducing atomic energy levels.
This would be a strong test of the framework.

### String theory parallels
**Type:** research

Compare the photon-on-T² model with string theory:

- A string is a 1D object that vibrates; our photon is a 1D
  wave on a closed geodesic. Both are "something periodic on
  compact geometry" producing particle properties.
- String harmonics ↔ our winding numbers. String tension ↔
  our path-length constraint. How deep is the analogy?
- A periodic counter (modular arithmetic) is the simplest
  1D compact dimension: a number that increments and rolls
  over. A sinusoid on this counter is a standing wave. Our
  photon is exactly this — a wave whose phase rolls over
  after one circuit. Is a "particle" just a resonance in a
  periodic register?
- Explore whether the T² model is a special case of, or
  parallel to, string compactification on a torus.

---

## Done

Studies listed in chronological order of completion.

### 10. R11. Prime resonance / least-expensive path
**Study:** [`prime-resonance/`](prime-resonance/)

Explored whether q is selected by energy cost, resonance
quality, or primality.  Eight tracks of investigation.
**Key results:** (1) Coulomb energy favors low q — no minimum
at 137.  (2) Five linear tests found no prime/composite
distinction.  (3) q ~ 1/α is partly tautological — it follows
from using the measured charge as input.  **Strategic insight:**
the real free parameter is r (aspect ratio), not q.  Breaking
the tautology requires solving field equations on the T²
without using e as input (→ R12).

### 1. S1. Toroid series
**Study:** [`toroid-series/`](toroid-series/)

Null result. The 9% charge deficit is an artifact of geometric
assumptions, not a robust target for correction.

### 2. S2. Toroid geometry
**Study:** [`toroid-geometry/`](toroid-geometry/)

a/R = 1/√(πα) ≈ 6.60 gives q = e in WvM's formula (using the
thin-torus R).  The key algebraic result — but not self-consistent
(see #8, R6).

### 3. S3. Knot zoo
**Study:** [`knot-zoo/`](knot-zoo/)

Only (1,2) produces charge (all other knots cancel by symmetry).
Fractional charges (e/3, 2e/3) map to clean a/R multiples.
Compact dimension hypothesis proposed.

### 4. D1. WvM summary revision
**Result:** [`ref/WvM-summary.md`](../ref/WvM-summary.md)

Revised to separate paper content from study results. Added
Zitterbewegung, harmony of phases, monopole exclusion, pair
creation, spin structure.

### 5. R1. KK charge comparison
**Study:** [`kk-charge/`](kk-charge/)

KK gravitational charge is ruled out at the Compton scale
(~10⁻²² × e). WvM charge mechanism is structurally different
(no G, different scale). Compact topology still useful for
confinement and spin. The 6D decomposition (gravity + 2 gauge
fields + 3 scalars) is documented for reference.

### 6. R2. Electron from geometry
**Study:** [`electron-compact/`](electron-compact/)

Confirmed: a photon of energy m_e c² on a (1,2) geodesic in a T²
produces q = e, s = ½, g ≈ 2.0023. Zero free continuous
parameters. Used S2's r = 6.60; R6 later found r ≈ 4.29 when
self-consistency is enforced. Numerics need amendment; framework
is sound.

### 7. R3. Dual visualizer
**Study:** [`dual-visualizer/`](dual-visualizer/)

Side-by-side 3D torus + 2D flat rectangle view with synchronized
photon animation. Supports a/R slider, knot selection, speed
control. Shows how geodesics are straight lines on the flat T².

### 8. R6. Guided-wave field profile
**Study:** [`field-profile/`](field-profile/)

Found that S2's a/R = 6.60 is not self-consistent: it assumed the
thin-torus R = λ_C/(4π), but the path constraint gives a smaller R.
The self-consistent solution gives r ≈ 4.29, R ≈ 8.2 × 10⁻¹⁴ m.
Different profile shapes (uniform, Gaussian, exponential) all yield
q = e but need different σ values. The actual profile requires
solving the wave equation on T².

### 9. R7. Charge from torus geometry
**Study:** [`torus-capacitance/`](torus-capacitance/)

Computed the 3D Coulomb field of charge e distributed along the
(1,2) geodesic for a range of aspect ratios.  Found that the
field energy is ~1–2% of m_e c²/2 for all r tested — roughly α
times the target.  No geometry at Compton scale stores enough
Coulomb energy.  The WvM energy-balance approach to computing
charge overestimates by ~1/α.  The "magic ratios" from S2 and
R6 were artifacts of that assumption.  The correct charge
mechanism remains open.
