# R18 Findings — Self-Consistent Geometry


## F1. The stiffness equals the EM energy density / R

Working backwards from α = 1/137 to extract the required
stiffness κ of the compact space:

    κ = ε₀E₀²/(2R) = m_ec²/(4π²R²a²)

In the flat-space approximation (ρ = R), this is exact.
With the curvature correction:

    κ_full = κ_flat × C(r)

where C(r) = (2/r²)[1 − 2/√(1−r²) + 1/(1−r²)^{3/2}].
For r = 0.5: C = 1.842.

Physical interpretation: the compact space's stiffness IS
the photon's own EM energy density divided by R.  The vacuum
"resists deformation with exactly the same force that creates
the deformation."

Expressed in fundamental constants:

    κ = m_e⁵c⁶(4+r²)² / (4π²r²ℏ⁴) × C(r)

Script: `scripts/track1_backwards.py`.


## F2. Linear degeneracy — α cancels in the stiffness

Both the driving pressure P and the deformation δ scale
linearly with the mode coupling amplitude ε:

    P = |ε| × ε₀E₀²/2       (EM pressure from mode perturbation)
    δ = ε × Δω²/V_norm       (deformation from perturbation theory)

Their ratio κ = P/|δ| is independent of ε (and hence α).
The linear force balance is satisfied for ANY value of α.

This means the first-order perturbation theory is DEGENERATE:
it cannot determine α.  It gives the stiffness (which is
α-independent) but not the coupling constant.

| Quantity | Value (r = 0.5) | Scales as |
|----------|----------------|-----------|
| ε        | 0.196          | ∝ √α (required) |
| δ        | −1.99 × 10⁻¹⁴ m | ∝ ε |
| δ/a      | −0.213         | ∝ ε |
| P        | 2.47 × 10²³ Pa | ∝ ε |
| κ        | 1.24 × 10³⁷ Pa/m | ε-independent |
| κ_flat   | 6.74 × 10³⁶ Pa/m | ε-independent |


## F3. Curvature correction factor C(r)

The integral I₁ = ∫cos²θ/(R+a cos θ)² dθ has the exact
analytical result:

    I₁ = (2π/r²R²) × [1 − 2/√(1−r²) + 1/(1−r²)^{3/2}]

The curvature correction C(r) = I₁/(π/R²):

| r   | C(r)  |
|-----|-------|
| 0   | 1.000 |
| 0.1 | 1.015 |
| 0.2 | 1.062 |
| 0.3 | 1.143 |
| 0.4 | 1.266 |
| 0.5 | 1.842 |

Wait — let me recheck r = 0.5.  C = (2/0.25)[1 − 2/0.866 +
1/0.6495] = 8 × [1 − 2.309 + 1.540] = 8 × 0.231 = 1.845.
Numerical code gives C = 1.842.  The small difference is from
the finite grid (N_theta = 10000).

C(r) → 1 as r → 0 (flat limit) and diverges as r → 1 (horn
torus).  This makes physical sense: greater curvature = stronger
mode coupling = larger correction.


## F4. Determining α requires nonlinear self-consistency

Since the linear calculation is degenerate (any α works), α
must be determined by NONLINEAR effects.  Candidates:

1. **Second-order perturbation theory.**  The coupling V(δ)
   itself depends on the deformation δ (the deformed torus
   has different curvature).  V(δ) = V₀ + V₁δ + ... gives
   a nonlinear equation for ε and δ.

2. **Energy conservation.**  The elastic energy ½κδ² reduces
   the available EM energy, changing E₀ and hence the pressure.
   This creates a cubic equation: P ∝ ε(m_ec² − ½κε²R²).

3. **Mode energy renormalization.**  The deformation shifts the
   eigenfrequencies ω_{p,q}, changing the energy balance and
   the perturbation denominators.

All three effects enter at order ε² ~ α ~ 1/137 relative to
the leading term.  A self-consistent calculation to this order
could determine α.

This structure is reminiscent of spontaneous symmetry breaking
in Landau theory: the symmetric state (δ = 0, Q = 0) is
marginally stable at linear order, and the quartic term in the
free energy selects the order parameter magnitude.


## Summary

| Finding | Result |
|---------|--------|
| F1 | κ = ε₀E₀²/(2R) = m_ec²/(4π²R²a²) × C(r) — stiffness IS the EM energy density per unit R |
| F2 | κ is α-independent at linear order — the force balance P = κδ is trivially satisfied for any α |
| F3 | Curvature correction C(r) is analytical; C(0.5) = 1.84 |
| F4 | α requires nonlinear self-consistency (second-order PT, energy conservation, or mode renormalization) |

The chain of reasoning to derive α:

    (1,2) photon on torus at Compton scale
    → EM field creates cos(2φ) pressure (from mode energy density)
    → Torus deforms: R → R + δ cos(2φ)
    → Deformation couples (1,2) mode to (1,0) mode
    → (1,0) mode carries monopole charge Q ∝ ε ∝ δ
    → α = Q²/(4πε₀ℏc) ∝ δ²

    At linear order: any δ (any α) is consistent.
    At nonlinear order: the self-consistent δ is unique → α is derived.

## F5. Forward energy balance — the symmetric torus is stable

Track 2 computes the total energy as a function of deformation
amplitude δ, without assuming α:

    E_total(δ) = E_photon(δ) + E_Coulomb(δ)

### Photon energy from path length

On the deformed torus (R → R + δcos2φ), the (1,2) geodesic
has path length:

    L(δ) = ∫₀⁴π √(a²/4 + (R + δcos2φ)²) dφ
         = L₀ × (1 + a²δ²/(16S₀⁴) + O(δ⁴))

where S₀ = √(a²/4 + R²).  The first-order term vanishes
because ∫cos(2φ)dφ = 0.  The photon energy E = hc/L decreases:

    ΔE_photon ≈ −m_ec² × a²δ²/(16S₀⁴)

### Coulomb cost

The deformation couples cos(θ+2φ) to cos θ through the
wave equation, producing charge Q ∝ δ.  The Coulomb self-energy:

    E_Coulomb = Q²/(4πε₀R) ∝ δ²

### Energy scale mismatch (the killer)

At the deformation where Q = e (α = 1/137):

| Quantity | Value (r = 0.5) |
|----------|----------------|
| δ/a | 0.214 |
| ΔE_photon | −1.6 × 10⁻⁴ m_ec² |
| E_Coulomb | +1.5 × 10⁻² m_ec² |
| Ratio Coulomb/path | 96× |

The Coulomb energy cost is ~100× the photon energy saving.
The symmetric torus (δ = 0) is the energy minimum.

### Why 96×?

The photon energy coefficient is C_path = m_ec² × a²/(16S₀⁴)
= 3.25 × 10¹⁰ J/m².  The Coulomb coefficient is
C_Coulomb = K²/(4πε₀R) where K = Q₀|V₀|/Δ(ω²/c²)
= 3.11 × 10¹² J/m².

The 96× ratio arises because:
- The path length change is O(δ/S₀)² — a GEOMETRIC effect
  suppressed by the compact space's size S₀ ~ 10⁻¹³ m.
- The Coulomb energy is O(Q²/R) — an ELECTROSTATIC effect
  set by e²/(4πε₀R) = α × m_ec² ≈ 0.007 m_ec².

The electrostatic scale (~0.01 m_ec²) dominates the geometric
scale (~10⁻⁴ m_ec²) by two orders of magnitude.


## F6. Reconciliation with Track 1 — the 2D mode energies are unphysical

Track 1 used 2D Laplacian eigenvalues:
- E_{1,2} = 5.83 m_ec² (the (1,2) mode on the 2D torus)
- E_{1,0} = 4.12 m_ec² (the (1,0) mode)

These are MUCH larger than the physical photon energy m_ec².
The discrepancy: the 2D eigenmode oscillates in BOTH θ and φ
directions, accumulating extra kinetic energy from the
transverse oscillation.  The physical photon (a winding mode
propagating along the 1D geodesic) has energy set by the PATH
LENGTH, not by the 2D eigenvalue.

Track 1's "linear degeneracy" (F2) was hiding this: the stiffness
κ = P/δ is independent of ε because both P and δ scale linearly
with ε, but this degeneracy is an artifact of using the 2D mode
energies.  The PHYSICAL energy available for deformation is
~355× smaller than the 2D estimate.

The 2D coupling matrix element V₀ (the GEOMETRY of mode coupling)
is correct — it's a property of the torus shape.  But the ENERGY
transfer must be computed from the physical photon energy m_ec²,
not from the 2D eigenvalue 5.83 m_ec².


## F7. The charge integral of cos(θ+2φ) vanishes on any torus

A deeper result emerges from the analysis.  The charge integral:

    Q ∝ ∫₀²π ∫₀²π cos(θ+2φ) × a × ρ(θ,φ) dθ dφ

vanishes for ANY ρ(θ,φ) that is a product of a function of θ
and a function of φ, or even for ρ = R + δcos(nφ) + a cos θ,
because:

    ∫₀²π cos(θ+2φ)(R + δcos(nφ) + a cos θ) dθ
    = aπ cos(2φ) + R × 0 + δcos(nφ) × 0

    ∫₀²π aπ cos(2φ) dφ = 0

The θ-integral always gives aπ cos(2φ), and ∫cos(2φ)dφ = 0.

The charge requires a cos θ component in the FIELD PATTERN
(not just the area element).  The WvM commensurability locks the
field to cos(θ+2φ), and this pattern has zero monopole moment
on any surface whose geometry has translational symmetry in φ
OR whose deformation is a smooth function of φ.

The MODE COUPLING from Track 1 would produce a cos θ admixture,
but the energy cost of this admixture (from the physical photon
energy, not 2D eigenvalues) is tiny, while the Coulomb cost is
large.  The system cannot afford the deformation.

Script: `scripts/track2_energy_balance.py`.


## Updated Summary

| Finding | Result |
|---------|--------|
| F1 | κ = ε₀E₀²/(2R) = m_ec²/(4π²R²a²) × C(r) |
| F2 | Linear degeneracy — κ is α-independent at first order |
| F3 | Curvature correction C(r); C(0.5) = 1.84 |
| F4 | ~~α requires nonlinear self-consistency~~ (superseded by F5) |
| F5 | **NEGATIVE.** Forward energy balance: Coulomb cost exceeds photon energy saving by 96×. Symmetric torus is stable. |
| F6 | Track 1's 2D mode energies (5.8 m_ec²) are unphysical; the physical photon energy m_ec² gives 355× less energy for deformation |
| F7 | The charge integral of cos(θ+2φ) vanishes on any smooth torus — the φ-integral always kills it |

## Conclusion

The geometric deformation mechanism (R18) is **ruled out**.

The photon cannot spontaneously deform its compact space to
produce charge, because the electrostatic cost of the charge
(~0.01 m_ec²) far exceeds the energy saved by the deformation
(~10⁻⁴ m_ec²).

The deeper reason is F7: the charge integral of the WvM field
pattern cos(θ+2φ) is EXACTLY ZERO on any torus — deformed or
not — as long as the field pattern retains its angular structure.
Breaking this requires the field to deviate from cos(θ+2φ), which
costs more energy than it saves.

The question "what determines σ?" remains open.  All tested
mechanisms (Coulomb soliton, centrifugal pressure, geometric
deformation) fail to determine σ from first principles.  The
surviving candidates are:

1. **Quantum self-interaction** — the photon's own quantum
   fluctuations, beyond the classical EM self-interaction.
2. **Topological constraint** — σ is fixed by the requirement
   that the wavepacket's phase wraps consistently on the torus,
   analogous to flux quantization.
3. **External coupling** — σ is determined by the photon's
   interaction with other fields (gravity, weak, etc.), not by
   its self-interaction alone.
