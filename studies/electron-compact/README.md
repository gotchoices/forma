# Electron from Compact Dimensions  *(draft)*

Given the established results from S1–S3 and R1, write down all
unknowns and constraints for the electron and determine whether
they fix a unique geometry.

## What we know

From prior studies:

| Property | Value | Source | Status |
|----------|-------|--------|--------|
| Spin ½ | L = ℏ/2 | (1,2) topology | Exact (S3) |
| Charge | q = e | a/R = 1/√(πα) | Exact algebra (S2) |
| Mass | m_e = h/(λ_C c) | Path length = λ_C | WvM |
| g-factor | g ≈ 2(1 + α'/2π) | External field fraction | WvM |
| Charge mechanism | Electromagnetic, not KK gravitational | WvM ≠ KK | R1 |
| Charge uniqueness | Only (1,2) has nonzero charge | Symmetry cancellation | S3 |

## The picture

- Two compact dimensions (φ, θ), both periodic → flat torus T².
- A photon follows a straight-line geodesic in this flat space.
- In the 3D embedding, this geodesic is a (1,2) torus knot.
- The photon's energy determines the particle mass: m = E/c².
- The topology determines spin; the field extent determines charge.

## Unknowns

| Variable | Meaning | Constrained by |
|----------|---------|----------------|
| L_φ | Circumference of major circle | mass (path length = λ_C) |
| L_θ | Circumference of minor circle | mass (path length = λ_C) |
| r = L_θ/L_φ | Aspect ratio of T² | ? (free parameter?) |
| a | Field extent into non-compact space | charge (a/R = 1/√(πα) from S2) |
| E | Photon energy | mass: m = E/c² |

The path length constraint √(4L_φ² + L_θ²) = λ_C relates L_φ
and L_θ, leaving one free: the ratio r = L_θ/L_φ.

## Key questions

1. **Is the system determined?** We have:
   - Spin: automatic from (1,2) topology — no constraint on geometry
   - Mass: fixes path length = λ_C — one equation, two unknowns (L_φ, L_θ)
   - Charge: fixes a/R = 1/√(πα) — constrains field extent, not L_φ/L_θ
   - g-factor: depends on external field fraction — may constrain r

   So: path length fixes L_φ(r) and L_θ(r) for any r. Charge
   fixes a/R. The ratio r appears to be free unless the g-factor
   or another condition constrains it.

2. **What is "a" in the compact-dimension picture?** S2 treats
   a as the field extent — how far the photon's E-field reaches
   from the geodesic orbit. In a compact-dimension framework,
   this should emerge from the field equations (guided-wave decay
   profile), not be an input.

3. **Does the g-factor constrain r?** WvM derives
   g = 2(1 + α'/2π) from the energy fraction in the non-rotating
   external field. If the external field depends on the T² aspect
   ratio r, this could fix the remaining free parameter.

4. **Fixed T² vs per-particle T².** If T² is a property of
   spacetime (same for all particles), then mass comes purely from
   photon energy and different particles are different energy
   modes on the same geometry. If T² varies per particle, the
   geometry determines both mass and charge. S3 suggested fixed T²
   with mass from harmonics; this needs testing.

## Approach

1. Write down all equations explicitly (path length, charge,
   g-factor) as functions of (L_φ, L_θ, a, E).
2. Count independent constraints vs unknowns.
3. If under-determined: identify what additional physics could
   close the system.
4. If determined: solve and check consistency.
5. If over-determined: check whether the constraints are mutually
   consistent (a non-trivial test of the model).

## What success looks like

A self-consistent solution where the compact dimension sizes
and photon energy produce all four electron properties (q, m,
s, g) from a small number of inputs — ideally just the T²
geometry and the photon energy, with everything else following.
