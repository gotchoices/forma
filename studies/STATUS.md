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

### R6. Guided-wave field profile
**Question:** Q9  **Type:** compute  **Depends on:** R2

What is the actual E-field falloff from the orbit? Replaces
WvM's uniform-field-in-a-sphere with a proper mode profile.
May provide a first-principles derivation of a/R = 1/√(πα).

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

### R2. Electron from geometry  *(concluded)*
**Study:** [`electron-compact/`](electron-compact/)

Confirmed: a photon of energy m_e c² on a (1,2) geodesic in a T²
produces q = e, s = ½, g ≈ 2.0023. The geometry is fully
determined: r = a/R = 1/√(πα) ≈ 6.60 (from charge), absolute
scale from mass (ℓ = λ_C). Zero free continuous parameters.

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
