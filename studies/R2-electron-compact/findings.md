# Electron from Geometry — Findings

Study R2. Assembles the results of S1–S3 and R1 into a single
framework, verifies mutual consistency, and identifies the minimal
specification that produces an electron.

Every formula is verified numerically in
[`scripts/verify.py`](scripts/verify.py).

---

## F1. The setup

Six coordinates: (t, x, y, z, φ, θ). The first four are ordinary
spacetime. The last two are compact — periodic with
circumferences L_φ and L_θ:

    φ ~ φ + L_φ          (major circle)
    θ ~ θ + L_θ          (minor circle)

The compact space is a flat torus T² = S¹ × S¹. A photon travels
on a geodesic (straight line) in this space.


## F2. The (1,2) geodesic

The electron geodesic is a (1,2) torus knot: it winds once around
θ for every two times around φ. On the flat rectangle (with
opposite edges identified), this is a straight line at slope
L_θ / (2 L_φ).

The path length — the distance traveled before the geodesic
closes on itself — is:

    ℓ = √( (2 L_φ)² + L_θ² )                ... (1)

The winding numbers are n_φ = 2, n_θ = 1.


## F3. Four electron properties

### Property 1: Mass

The photon must fit one complete wavelength around the closed
path (periodic boundary condition). So the photon wavelength
equals the path length:

    λ = ℓ = √(4 L_φ² + L_θ²)

The photon energy is E = hc/λ and the mass is:

    m = E / c² = h / (λ c) = h / (ℓ c)      ... (2)

Setting m = m_e gives ℓ = λ_C (the electron Compton wavelength):

    √(4 L_φ² + L_θ²) = λ_C                  ... (mass constraint)

This is one equation with two unknowns. Parameterize by the
aspect ratio r = L_θ / L_φ:

    L_φ(r) = λ_C / √(4 + r²)
    L_θ(r) = r × L_φ(r) = r λ_C / √(4 + r²)

For any r > 0, these give a valid T² with path length λ_C.

The orbital radius (mean distance from the torus axis in the
3D embedding) is:

    R(r) = L_φ(r) / (2π) = λ_C / (2π √(4 + r²))

Note: when r = 0 (L_θ → 0), the path degenerates to a circle
of circumference 2L_φ = λ_C, giving R = λ_C/(4π) — exactly
the WvM value. So WvM's orbital radius is the r → 0 limit.


### Property 2: Spin

The (1,2) geodesic winds twice around φ before closing. The
photon must traverse the full path twice to return to its starting
orientation (because after one traversal, the field vectors have
rotated 360° around the tube, not returned to their original
orientation). The angular frequency of rotation is therefore
ωs = 2ω, and:

    L = E / ωs = ℏω / (2ω) = ℏ/2            ... (3)

This is spin ½. It depends only on the winding number n_φ = 2,
not on L_φ, L_θ, or r. It is exact and topological.


### Property 3: Charge

From S2 (S2-toroid-geometry, finding F6): the WvM charge formula
with a toroidal field volume V = 2π²Ra² gives q = e when:

    a / R = 1 / √(πα)                        ... (4)

where a is the tube radius (field extent around the minor
circle) and R is the orbital radius (major circle).

In the compact-dimension picture, the tube circumference IS the
minor circumference: L_θ = 2πa. The major circumference gives
R = L_φ/(2π). Therefore:

    a/R = L_θ/L_φ = r                        ... (5)

The charge condition (4) becomes a constraint on r:

    r = 1/√(πα) ≈ 6.6045                     ... (charge constraint)

This fixes the aspect ratio. Combined with the mass constraint:

    L_φ = λ_C / √(4 + r²) = λ_C / √(4 + 1/(πα))
    L_θ = r L_φ = λ_C / √(4πα + 1)
    R   = L_φ / (2π)
    a   = L_θ / (2π)

All four geometric quantities are fully determined.

The charge also depends on the knot type. From S3 (S3-knot-zoo,
finding F3): only the (1,2) knot produces nonzero charge. All
other (p,2) knots cancel by symmetry. This is a topological
selection rule.


### Property 4: g-factor

WvM derive the anomalous magnetic moment (WvM-summary §8). The
electron's magnetic moment is:

    μ = g × (e / 2m_e) × s

with:

    g = 2(1 + α'/(2π))                       ... (6)

where α' = (q/e)²α. With q = e (from Property 3), α' = α:

    g = 2(1 + α/(2π)) ≈ 2.00232

This depends on α = e²/(4πε₀ℏc) — a ratio of fundamental
constants. It does NOT depend on L_φ, L_θ, r, R, or a.

The physical origin: a fraction α/(2π) of the photon's total
energy resides in the external (non-rotating) Coulomb field.
This modifies the internal oscillation frequency and hence the
ratio of magnetic moment to angular momentum.


## F4. Counting constraints vs unknowns

### Unknowns

| # | Variable | Meaning |
|---|----------|---------|
| 1 | L_φ | Major circumference |
| 2 | L_θ | Minor circumference |
| 3 | E | Photon energy |

Three unknowns. (The topology (1,2) is a discrete choice, not
continuous. And a = L_θ/(2π), R = L_φ/(2π) — they are not
independent of L_φ and L_θ.)

### Constraints

| # | Constraint | Equation | Fixes |
|---|-----------|----------|-------|
| 1 | Mass = m_e | √(4L_φ² + L_θ²) = λ_C | Relates L_φ and L_θ |
| 2 | Charge = e | r = L_θ/L_φ = 1/√(πα) | Fixes r (shape) |
| 3 | Spin = ½ | (automatic from (1,2)) | Nothing — always true |
| 4 | g ≈ 2.0023 | g = 2(1 + α/(2π)) | Nothing — always true |

E is trivially fixed by mass: E = m_e c². Constraint 2 fixes
the ratio L_θ/L_φ. Constraint 1 then fixes the absolute scale.

Result: **3 unknowns, 3 constraints. Zero free parameters.**


## F5. The fully determined electron

With r = 1/√(πα) and ℓ = λ_C, every geometric quantity is
determined:

    r   = 1/√(πα) ≈ 6.6045
    L_φ = λ_C / √(4 + 1/(πα)) ≈ 3.516 × 10⁻¹³ m
    L_θ = λ_C / √(4πα + 1)    ≈ 2.322 × 10⁻¹² m
    R   = L_φ / (2π)           ≈ 5.596 × 10⁻¹⁴ m
    a   = L_θ / (2π)           ≈ 3.695 × 10⁻¹³ m

| Quantity | Value | Fixed by |
|----------|-------|----------|
| Mass | m_e = 0.511 MeV/c² | Path length = λ_C (resonance) |
| Spin | ℏ/2 | (1,2) winding (topological) |
| Charge | e | r = 1/√(πα) (shape) |
| g-factor | 2(1 + α/(2π)) | α (fundamental constant) |
| L_φ | 3.516 × 10⁻¹³ m | Mass + charge together |
| L_θ | 2.322 × 10⁻¹² m | Mass + charge together |
| R | 5.596 × 10⁻¹⁴ m | L_φ/(2π) |
| a | 3.695 × 10⁻¹³ m | L_θ/(2π) |

### Physical meaning

The electron's shape AND scale are fully determined:

- **Shape** (r ≈ 6.60): fixed by the charge condition. The torus
  is highly elongated — the tube radius a is 6.6 times the
  orbital radius R. (In 3D embedding, this is a spindle torus
  that self-intersects.)

- **Scale** (ℓ = λ_C): fixed by the mass. The photon's wavelength
  must equal the closed geodesic path length (resonance). A
  heavier particle → shorter wavelength → smaller torus.

- **Resonance frequency**: the photon completes one full orbit
  in time T = λ_C/c = h/(m_e c²). This is the Compton period.
  The photon is in exact resonance with the geometry — one EM
  oscillation per circuit.

### Note on the WvM limit

The original WvM model effectively takes r → 0 (zero tube size),
which gives R = λ_C/(4π). This is NOT consistent with q = e,
which requires r = 1/√(πα) ≈ 6.60. The S2 correction (using
the proper toroidal field volume with finite a) resolved this.


## F6. The electron recipe

### Inputs

1. **Topology:** two compact periodic dimensions (T²)
2. **Geodesic type:** (1,2) torus knot
3. **Photon energy:** E = m_e c² = 0.511 MeV
4. **Fine-structure constant:** α ≈ 1/137

### Outputs (numerically verified)

| Property | Value | How |
|----------|-------|-----|
| Mass | 0.511 MeV/c² | Path length = λ_C (resonance) |
| Spin | ½ | Double winding, topological |
| Charge | e | r = a/R = 1/√(πα) |
| g-factor | 2.00232 | External field fraction α/(2π) |
| Magnetic moment | 9.285 × 10⁻²⁴ J/T | μ = g(e/2m)(ℏ/2) |
| Major radius R | 5.596 × 10⁻¹⁴ m | From L_φ |
| Tube radius a | 3.695 × 10⁻¹³ m | From L_θ |

### What the framework requires

- Two compact dimensions (the minimum for spin ½ — one dimension
  only gives integer spin, per R1/theory.md)
- Electromagnetic fields that propagate in these dimensions
- Periodic boundary conditions (single-valued wavefunction)

### What it does NOT require

- Gravity (charge is electromagnetic, not KK gravitational)
- A confinement mechanism (geodesics on compact space are
  automatically closed)
- Any free parameters (everything is determined)


## F7. What remains open

These are not free parameters — they are open questions about
why the framework works:

1. **Deriving α.** The charge requires r = 1/√(πα), which
   encodes α. We use α as an input. Deriving it from a deeper
   geometric principle (energy minimization, self-consistency,
   boundary matching) would be a major result. (R8)

2. **The field profile.** S2 computed the charge using a uniform
   field inside a toroidal volume. A first-principles guided-wave
   mode profile should show how the field actually distributes
   and whether the uniform-volume approximation holds. (R6)

3. **The spindle torus.** With a/R ≈ 6.60, the torus heavily
   self-intersects in a 3D embedding (a spindle torus). This
   is fine for the flat T² (which needs no 3D embedding), but
   raises questions about the physical field distribution in xyz.

4. **Other particles.** Do the muon, tau, quarks, and neutrino
   fit this framework? Different photon energies give different
   masses. Different knots give different spins. Different a/R
   ratios give different charges (S3 showed clean algebraic
   ratios for 1/3 and 2/3 charges). But the mass spectrum is
   not simply harmonic (m_μ/m_e ≈ 206.77, not an integer).


## F8. Conclusions

### The main result

**A photon of energy m_e c² on a (1,2) geodesic in a T² produces
a particle with all measured electron properties: q = e, s = ½,
m = m_e, g ≈ 2.0023. The geometry is fully determined — there
are zero free continuous parameters.**

The electron is specified by:

- The topology: (1,2) knot → spin ½
- The energy: E = m_e c² → path length λ_C → absolute scale
- The fine-structure constant: α → r = 1/√(πα) → shape

### What this framework is

A complete specification for particles from geometry:

    compact dimensions + geodesic topology + photon energy
    → mass, spin, charge, magnetic moment, geometry

The compact dimensions provide the stage. The geodesic provides
the quantum numbers. The photon energy provides the mass. The
charge condition fixes the shape of the stage. The mass fixes
its scale. No forces, no confinement mechanism, no point
particles, no free parameters.

---

*Numerical verification: [`scripts/verify.py`](scripts/verify.py)*
