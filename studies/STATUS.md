# Project Status

Priority-ordered work queue. Pick from the top of Backlog.

**Workflow:** See `README.md` for conventions.

---

## Active

*(nothing active)*

---

## Backlog

### B-field and magnetic dipole
**Question:** Q8  **Type:** research

Close out open question about how the B-field direction and
magnetic dipole emerge from the (1,2) orbit. Mostly answered
by the WvM summary revision (§7, §8); needs a final pass to
confirm and write up.

### Gauss's law charge integral (flat-torus approach)
**Type:** compute  **Depends on:** R6

Replace the WvM energy-balance approximation with an exact
Gauss's law integral.  Key idea: compute in the flat-rectangle
picture, then wrap.

On the flat T² (a rectangle with periodic boundaries), the
photon is a diagonal plane wave.  Its E field emanates
perpendicular to the rectangle — into the non-compact 3+1D
spacetime.  Since the rectangle is compact (tiny), all the flux
converges to look like a point charge from far away.  The total
perpendicular flux through the rectangle IS the charge:

    q = ε₀ × ∫∫_rectangle E_perp dA

This eliminates two arbitrary choices from WvM's method (the
averaging volume V and the Coulomb-matching radius).  The
remaining unknown is the perpendicular field extent δ — how far
E reaches into 3D before the compactness of the dimensions
constrains it.  Possible routes to determine δ:

- The compact dimensions themselves limit δ (field wraps back)
- Solve the wave equation for the mode on T² × ℝ³ to get the
  perpendicular profile from first principles
- Energy conservation: U_E = ½ε₀ ∫ E² dV over all space

If δ is determined by the geometry, the system closes: path
constraint + Gauss's law + energy conservation → (R, a)
with no free parameters.

Build a numerical integrator that:
1. Models the photon as a traveling wave on the (1,2) geodesic
2. Computes E_perp at each point on the rectangle
3. Integrates total flux to get q
4. Sweeps geometry to find q = e

### Amend R2 with self-consistent geometry
**Type:** revision  **Depends on:** R6

R6 found the self-consistent r ≈ 4.29 (not 6.60).  Update R2's
findings and verify script with the corrected values.  The
framework and conclusions are sound; only numerics change.

### Wave equation on T²
**Question:** Q9  **Type:** compute  **Depends on:** R6

R6 found the self-consistent (r, R) for several assumed profiles
but could not determine which profile is physical. The next step
is solving the actual scalar/vector wave equation on the T²
geometry to see what mode shapes emerge. This would determine:

- The physical field profile and its width σ
- Whether α is predicted or must be input
- Whether multiple modes exist with different σ (→ quarks)

### Flat space → curved appearance
**Question:** Q2  **Type:** reason

If compact dimensions are flat, how do the photon's fields
project into 3+1D? The 6D decomposition from R1 provides the
framework; what remains is working out the field projection.

### Quadrupole correction
**Question:** Q10  **Type:** compute  **Depends on:** R6

Full calculation of charge including the (1,2) orbit's ~2.5%
field anisotropy (quantified in S2 F5).

### Derive α from geometry
**Question:** Q18  **Type:** compute

Can a/R be derived from an independent physical argument
(boundary matching, energy minimization, self-consistent
confinement)? Major open problem.

### Precession of torus axis
**Question:** Q19  **Type:** compute

What drives axis precession? Does it restore spherical symmetry?

### Orbit precession and volume-filling
**Question:** Q23  **Type:** compute

Does a precessing (1,2) orbit reproduce WvM's volume-filling
energy flow (Fig. 2)?

### Quarks from geometry
**Type:** compute  **Questions:** Q12, Q13

Can fractional charges (e/3, 2e/3) arise from the same
framework? S3 showed the WvM formula admits them via different
a/R multiples (1.5×, 3× the electron's). Possible mechanisms:

- Different guided-wave modes on the same T²
- Different T² geometries (three compact dimensions?)
- Multi-photon states with correlated phases (color charge?)
- Non-toroidal compact manifolds

Also: quark confinement — quarks are never free. Does the
geometry explain this, or is it a separate mechanism?

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
