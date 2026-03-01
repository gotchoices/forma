# Electron from Compact Dimensions  *(draft)*

Given the compact-dimension framework, solve for a self-consistent
set of variables (geometry, energy) that reproduce the measured
electron properties: charge, mass, spin, magnetic moment.

**Depends on:** R1 (KK charge comparison) — determines whether
the framework is KK, WvM, or something hybrid.

## The picture

- Two compact dimensions (φ, θ), both periodic → flat torus T².
- A photon follows a straight-line geodesic in this flat space.
- In the 3D embedding, this geodesic is a (1,2) torus knot.
- The photon's energy determines the particle mass: m = E/c².
- The topology and geometry determine charge, spin, and g-factor.

## Unknowns

| Variable | Meaning | Constrained by |
|----------|---------|----------------|
| L_φ | Circumference of major circle | charge + mass |
| L_θ | Circumference of minor circle | charge + spin |
| p, q | Winding numbers | spin (must be (1,2)) |
| E | Photon energy | mass |
| Field profile | How E/B extend beyond the compact surface | charge, g-factor |

Some of these may not be independent. Part of the study is
determining which variables are free and which are fixed by
the constraints.

## Constraints

| Property | Measured value | WvM derivation |
|----------|---------------|----------------|
| Charge | q = e = 1.602 × 10⁻¹⁹ C | Topology + field geometry |
| Mass | m_e = 0.511 MeV/c² | Photon energy: m = h/(λc) |
| Spin | s = ½ | (1,2) winding: L = ℏ/2 |
| g-factor | g ≈ 2.0023 | External field energy fraction |

## Key questions

1. **Is the system determined?** Four constraints, roughly five
   unknowns. Is there a free parameter, or does the system
   over-determine (requiring consistency checks)?

2. **Does mass fix the geometry, or vice versa?** In WvM,
   R = λ_C/(4π) links the orbital radius to the mass. In the
   compact dimension picture, R is a property of spacetime
   (fixed for all particles). These can't both be true. R1
   should clarify which picture is correct.

3. **What sets L_φ and L_θ?** If the compact dimensions have
   fixed sizes, all particles on the same T² have the same
   geometry. Mass comes from photon energy (independent of
   geometry). Charge comes from the geometry (independent of
   energy). These decouple — but do they decouple cleanly?

4. **The g-factor constraint.** WvM derives g = 2(1 + α'/2π)
   from the energy in the external (non-rotating) Coulomb field.
   In the compact dimension picture, what is the "external" field?
   The field that extends into the non-compact dimensions (xyz)?
   This needs to be mapped carefully.

5. **Consistency with R1.** If R1 shows WvM ≈ KK, then charge
   comes from KK quantization (q = nℏ/(R_KK c)) and the compact
   radius is fixed by demanding q = e. If R1 shows WvM ≠ KK,
   the charge derivation is WvM's cavity argument and the
   compact radius is less constrained.

## Approach

1. Wait for R1 to establish the framework.
2. Write down the full set of equations (KK or WvM, per R1).
3. Count unknowns and constraints.
4. Solve, or identify what additional physics is needed to close
   the system.
5. Compare predictions to measured values.

## What success looks like

A self-consistent solution where the compact dimension sizes,
photon energy, and winding numbers produce all four electron
properties from a small number of inputs (ideally: just the
compact dimension sizes and the photon energy, with everything
else following from the framework).
