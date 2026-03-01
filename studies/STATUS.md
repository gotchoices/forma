# Project Status

Priority-ordered work queue. Pick from the top of Next.

**Workflow:** See `README.md` for conventions.

---

## Active

(none)

---

## Next

### R1. KK charge comparison
**Question:** Q17  **Type:** reason  **Depends on:** —
**Study:** [`kk-charge/`](kk-charge/)

Does WvM's charge derivation reduce to the Kaluza-Klein charge
quantum? If yes, the compact-dimension framework is on solid
theoretical ground. If no, we know exactly where the gap is.
Foundation for everything below.

### R2. Solve for electron properties
**Question:** Q20 (partial)  **Type:** compute  **Depends on:** R1
**Study:** [`electron-compact/`](electron-compact/)

Given the compact-dimension framework, write down the unknowns
(dimension sizes, winding, photon energy), the constraints
(q = e, m = m_e, s = ½, g ≈ 2.0023), and solve. This is the
main goal.

### R3. Dual visualizer (3D torus + 2D flat)
**Type:** compute  **Depends on:** —
**Study:** (not yet created)

Augment the existing torus visualizer to show a side-by-side 2D
flat rectangle with wrapping (Pac-Man style) alongside the 3D
torus. A (1,2) path is a straight line at a specific angle on
the flat view. Builds intuition for the compact-dimension picture.

### R4. B-field and magnetic dipole
**Question:** Q8  **Type:** research  **Depends on:** —

Close out open question about how the B-field direction and
magnetic dipole emerge from the (1,2) orbit. Mostly answered
by the WvM summary revision (§7, §8); needs a final pass to
confirm and write up.

---

## Backlog

### R5. Flat space → curved appearance
**Question:** Q2  **Type:** reason  **Depends on:** R1

If compact dimensions are flat, how do the photon's fields
project into 3+1D? Answerable from KK field projection once
R1 establishes the framework.

### R6. Guided-wave field profile
**Question:** Q9  **Type:** compute  **Depends on:** R2

What is the actual E-field falloff from the orbit? Replaces
WvM's uniform-field-in-a-sphere with a proper mode profile.
Affects charge derivation accuracy.

### R7. Quadrupole correction
**Question:** Q10  **Type:** compute  **Depends on:** R6

Full calculation of charge including the (1,2) orbit's ~2.5%
field anisotropy.

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

### D1. WvM summary revision
**Type:** research  **Result:** [`ref/WvM-summary.md`](../ref/WvM-summary.md)

Revised to separate paper content from study results. Added
Zitterbewegung, harmony of phases, monopole exclusion, pair
creation, spin structure.
