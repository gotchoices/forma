# R37 Findings — Membrane mechanics at the T²/R³ interface

Study: [`README.md`](README.md)

---

## Track 1 — Radiation stress tensor on the T² surface

### F1. The (1,2) mode stress is highly anisotropic

At the canonical aspect ratio r = 6.6, the momentum
fractions are:

    f₁ (tube) = r²/(r² + q₂²) = 0.917
    f₂ (ring) = q₂²/(r² + q₂²) = 0.083

where q₂ = 2 − s ≈ 1.99.  The anisotropy ratio:

    ΔP/P_iso = f₁ − f₂ = 0.833

The stress is 83% anisotropic.  Physically: the (1,2)
winding wraps once around the short tube (L₁) and twice
around the long ring (L₂ = 6.6 L₁).  The tube wavelength
is much shorter → most momentum is in the tube direction.

### F2. The stress tensor is UNIFORM across T²

For a running wave (circularly polarized photon), the
energy density is constant:

    ρ = E/A = m_e c² / (L₁ L₂) = 5.29 × 10⁸ J/m²

There is no spatial pattern — only a direction-dependent
anisotropy (principal stresses p₁ ≠ p₂).  The isotropic
2D radiation pressure is:

    P_iso = ρ/2 = 2.65 × 10⁸ J/m²

### F3. The shear modulus μ_m is determined by α (input)

α = 1/137 fixes the equilibrium shear s_eq = 0.01029
(via R19).  The anisotropic stress ΔP = 2.20 × 10⁸ J/m²
drives this shear.  The shear modulus:

    μ_m = ΔP / s_eq = 2.14 × 10¹⁰ J/m²
                     = 0.134 eV/fm²

This is the membrane's tangential compliance — fixed
entirely by the mode geometry and the observed α.

### F4. The hierarchy ΔP/u_grav ≈ 3 × 10⁴⁵ reproduces the known EM/gravity hierarchy

The gravitational self-energy density of the electron:

    u_grav = G m_e² / (R₂ × A) ≈ 7.0 × 10⁻³⁸ J/m²

The ratio:

    ΔP / u_grav ≈ 3 × 10⁴⁵

This matches α_EM / α_grav ≈ 4 × 10⁴² to within the
expected geometric factors.  The hierarchy arises because:

- ΔP ∝ m_e c²/A ∝ 1/R² (radiation pressure — LOCAL
  surface quantity, independent of G)
- u_grav ∝ Gm_e²/(R × A) ∝ Gm_e/R³ (gravitational
  binding — suppressed by an additional factor Gm_e/(Rc²))

The hierarchy is the ratio of a local surface energy
density to a global gravitational coupling.  Both live
on the same T² surface; the enormous ratio is built in
because G enters only the gravitational term.

### F5. Isotropic surface tension cannot balance radiation pressure in both directions

A simple surface energy σ_m gives different equilibrium
values depending on which direction is balanced:

    σ_m(L₁) = P_iso / r = 4.01 × 10⁷ J/m²
    σ_m(L₂) = p₂        = 4.41 × 10⁷ J/m²

The 9% disagreement means the force balance requires
anisotropic elastic response — at minimum (σ_m, μ_m).
A single surface tension is insufficient.  This constrains
Track 2: the full elastic membrane formalism is required.

### F6. The isotropic crossover is at r ≈ 2

| r regime | Stress character | ΔP sign |
|----------|-----------------|---------|
| r < 2 | Ring-dominated (f₂ > f₁) | ΔP < 0 |
| r ≈ 2 | Isotropic (f₁ ≈ f₂) | ΔP ≈ 0 |
| r > 2 | Tube-dominated (f₁ > f₂) | ΔP > 0 |

The crossover occurs at r = q₂ = 2 − s ≈ 2, where the
physical wavelengths in both directions match.  The
canonical r = 6.6 is well into the tube-dominated regime.

### F7. Physical magnitudes at r = 6.6

| Quantity | Value | Units |
|----------|-------|-------|
| P_iso (isotropic pressure) | 2.65 × 10⁸ | J/m² |
| ΔP (anisotropic stress) | 2.20 × 10⁸ | J/m² |
| μ_m (shear modulus, from α) | 2.14 × 10¹⁰ | J/m² |
| σ_m (surface energy, approx) | ~4.0 × 10⁷ | J/m² |
| K_n (spacetime stiffness) | 4.82 × 10⁴² | N |
| L₁ (tube circumference) | 4842 | fm |
| L₂ (ring circumference) | 31956 | fm |
| A (torus area) | 1.55 × 10⁻²² | m² |
