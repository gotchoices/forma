# Project Status

Priority-ordered work queue. Pick from the top of Next.

**Workflow:** See `README.md` for conventions.

---

## Active

### R4. B-field and magnetic dipole
**Question:** Q8  **Type:** research  **Depends on:** —

Close out open question about how the B-field direction and
magnetic dipole emerge from the (1,2) orbit. Mostly answered
by the WvM summary revision (§7, §8); needs a final pass to
confirm and write up.

---

## Backlog

### R5. Flat space → curved appearance
**Question:** Q2  **Type:** reason  **Depends on:** —

If compact dimensions are flat, how do the photon's fields
project into 3+1D? The 6D decomposition from R1 provides the
framework; what remains is working out the field projection.

### R6-next. Wave equation on T²
**Question:** Q9  **Type:** compute  **Depends on:** R6

R6 found the self-consistent (r, R) for several assumed profiles
but could not determine which profile is physical. The next step
is solving the actual scalar/vector wave equation on the T²
geometry to see what mode shapes emerge. This would determine:

- The physical field profile and its width σ
- Whether α is predicted or must be input (→ R8)
- Whether multiple modes exist with different σ (→ R11, quarks)

### R7. Quadrupole correction
**Question:** Q10  **Type:** compute  **Depends on:** R6

Full calculation of charge including the (1,2) orbit's ~2.5%
field anisotropy (quantified in S2 F5).

### R8. Derive α from geometry
**Question:** Q18  **Type:** compute  **Depends on:** R2, R6

Can a/R = 1/√(πα) be derived from an independent physical
argument (boundary matching, energy minimization, self-consistent
confinement)? Major open problem.

### R9. Precession of torus axis
**Question:** Q19  **Type:** compute  **Depends on:** R2

What drives axis precession? Does it restore spherical symmetry?

### R10. Orbit precession and volume-filling
**Question:** Q23  **Type:** compute  **Depends on:** R2

Does a precessing (1,2) orbit reproduce WvM's volume-filling
energy flow (Fig. 2)?

### R11. Quarks from geometry
**Type:** compute  **Depends on:** R6
**Questions:** Q12, Q13

Can fractional charges (e/3, 2e/3) arise from the same
framework? S3 showed the WvM formula admits them via different
a/R multiples (1.5×, 3× the electron's). Possible mechanisms:

- Different guided-wave modes on the same T² (from R6)
- Different T² geometries (three compact dimensions?)
- Multi-photon states with correlated phases (color charge?)
- Non-toroidal compact manifolds

Also: quark confinement — quarks are never free. Does the
geometry explain this, or is it a separate mechanism?

### R12. String theory parallels
**Type:** research  **Depends on:** —

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

### S1. Toroid series  *(concluded)*
**Study:** [`toroid-series/`](toroid-series/)

Null result. The 9% charge deficit is an artifact of geometric
assumptions, not a robust target for correction.

### S2. Toroid geometry  *(concluded)*
**Study:** [`toroid-geometry/`](toroid-geometry/)

a/R = 1/√(πα) ≈ 6.60 gives q = e exactly. The sphere is the
rotation horizon. Spin is exact (topological), charge depends
on field extent geometry. The key algebraic result of the project.

### S3. Knot zoo  *(concluded)*
**Study:** [`knot-zoo/`](knot-zoo/)

Only (1,2) produces charge (all other knots cancel by symmetry).
Fractional charges (e/3, 2e/3) map to clean a/R multiples.
Compact dimension hypothesis proposed.

### R3. Dual visualizer  *(concluded)*
**Study:** [`dual-visualizer/`](dual-visualizer/)

Side-by-side 3D torus + 2D flat rectangle view with synchronized
photon animation. Supports a/R slider, knot selection, speed
control. Shows how geodesics are straight lines on the flat T².

### R6. Guided-wave field profile  *(concluded)*
**Study:** [`field-profile/`](field-profile/)

Found that S2's a/R = 6.60 is not self-consistent: it assumed the
thin-torus R = λ_C/(4π), but the path constraint gives a smaller R.
The self-consistent solution gives r ≈ 4.29, R ≈ 8.2 × 10⁻¹⁴ m.
Different profile shapes (uniform, Gaussian, exponential) all yield
q = e but need different σ values. The actual profile requires
solving the wave equation on T² (→ R6-next).

### R2. Electron from geometry  *(concluded)*
**Study:** [`electron-compact/`](electron-compact/)

Confirmed: a photon of energy m_e c² on a (1,2) geodesic in a T²
produces q = e, s = ½, g ≈ 2.0023. The geometry is fully
determined: r = a/R = 1/√(πα) ≈ 6.60 (from charge), absolute
scale from mass (ℓ = λ_C). Zero free continuous parameters.
(Note: R6 found that r ≈ 4.29 when self-consistency is enforced.)

### R1. KK charge comparison  *(concluded)*
**Study:** [`kk-charge/`](kk-charge/)

KK gravitational charge is ruled out at the Compton scale
(~10⁻²² × e). WvM charge mechanism is structurally different
(no G, different scale). Compact topology still useful for
confinement and spin. The 6D decomposition (gravity + 2 gauge
fields + 3 scalars) is documented for reference.

### D1. WvM summary revision
**Type:** research  **Result:** [`ref/WvM-summary.md`](../ref/WvM-summary.md)

Revised to separate paper content from study results. Added
Zitterbewegung, harmony of phases, monopole exclusion, pair
creation, spin structure.
