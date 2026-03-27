# Guided-Wave Field Profile  *(concluded)*

Investigate the photon's field profile on the Ma_e (the electron sheet) geometry.
Replace the uniform-field approximation from S2 with a physical
mode shape and check what changes.

## Motivation

S2 derived a/R = 1/√(πα) by assuming:
1. Uniform E-field inside a toroidal volume V = 2π²Ra²
2. Orbital radius R = λ_C/(4π) (the WvM thin-torus value)
3. Matching the average field to Coulomb at r_c = R

But R2 showed that R depends on r = a/R via the path-length
constraint. When r ≈ 6.60, R is much smaller than λ_C/(4π).
This creates a self-consistency problem: the charge formula
was derived with one R, but the geometry demands another.

## Key questions

1. **Self-consistency:** What is the actual self-consistent
   (r, R) pair that satisfies both the path constraint and the
   charge formula simultaneously?

2. **Field profile shape:** What does the field actually look
   like? Is it Gaussian, exponential, Bessel, or something else?
   How does the shape affect the charge integral?

3. **Fresnel zone connection:** The diffraction scale √(λ_C R)
   is numerically close to the tube radius a. Is this exact or
   coincidental?

4. **Multiple modes:** Are there other mode solutions with
   different effective field extents? (Connects to quarks, R11.)

## Approach

### Part A: Self-consistency analysis (scripts/)

Solve the coupled equations:
- Path constraint: √(4L_φ² + L_θ²) = λ_C
- Charge formula: q = e with physical R (not WvM R)
- Geometry: r = a/R = L_θ/L_φ

### Part B: Profile comparison (scripts/)

For several field profile shapes (uniform, Gaussian, exponential),
compute the charge as a function of profile width. Determine
what width gives q = e for each shape.

### Part C: Diffraction analysis (scripts/)

Check the Fresnel zone conjecture: does the natural transverse
spread of a wave on a curved path match the field extent?

## References

- S2 (charge derivation): [`S2-toroid-geometry/findings.md`](../S2-toroid-geometry/findings.md)
- R2 (geometry): [`R2-electron-compact/findings.md`](../R2-electron-compact/findings.md)
- WvM paper: [`reference/WvM.pdf`](../../reference/WvM.pdf)
