# Studies Registry

See [`../STATUS.md`](../STATUS.md) for electron objectives and project snapshot.  
See [`../qa/`](../qa/) for open physics questions and detailed problem analysis.

---

## Active

### R15. Forward charge calculation — deriving α
**Study:** [`forward-charge/`](forward-charge/)
**Questions:** [Q18](../qa/Q18-deriving-alpha.md), Q34 Path 7  **Type:** compute  **Depends on:** R7, R13

R7 computed U_Coulomb = α × m_e c² and called it a failure. R8 "fixed" it by
shrinking the torus, requiring multi-winding (68,137). R13 showed multi-winding
breaks WvM charge (monopole = 0, exactly). This revives (1,2) at Compton scale —
the only model where charge works. R15 runs R7's calculation *forward*: input
energy m_e c² and (1,2) topology, compute the far-field Coulomb flux, read off
charge Q, and check whether Q²/(4πε₀ℏc) ≈ 1/137. If so, α is derived from
energy and topology alone.

### R16. Harmonic decomposition and the charge-producing mode  *(paused)*
**Study:** [`harmonic-charge/`](harmonic-charge/)
**Questions:** [Q18](../qa/Q18-deriving-alpha.md), Q34 Path 5  **Type:** analytical/compute  **Depends on:** R12, R13

The confined photon's field decomposes into Fourier modes of T². Only the
p = 1 component produces charge (WvM commensurability; R13). If the embedding
curvature redistributes energy from the (1,2) plane wave to a broad spectrum,
with the p = 1 sector retaining fraction α of the total energy, then
α = (charge-mode energy) / (total energy) — derived from geometry.
Complementary to R15 (numerical forward calc); R16 seeks the analytical
explanation.  *Paused:* R18 showed that curvature-induced mode mixing on an
axisymmetric torus still gives zero charge (φ-symmetry protection).  R16's
approach needs the φ-symmetry breaking that R18 provides.

### R18. Self-consistent geometry — deriving α from torus stiffness
**Study:** [`torus-stiffness/`](torus-stiffness/)
**Questions:** [Q18](../qa/Q18-deriving-alpha.md)  **Type:** compute/analytical  **Depends on:** R15, R17

The photon's EM field creates a cos(2φ) pressure that deforms the torus,
coupling the (1,2) mode to the charge-carrying (1,0) mode.  Track 1 (complete):
working backwards from α = 1/137 gives stiffness κ = ε₀E₀²/(2R) —
the EM energy density per unit major radius.  Both the pressure P and the
deformation δ scale linearly with the coupling ε, so κ is α-independent
at first order (linear degeneracy).  α is determined by the NONLINEAR
self-consistency (second-order PT, energy conservation).  Structure resembles
Landau theory: the quartic term in the free energy selects the order parameter.

### R14. Universal geometry — shared T³ for all particles
**Study:** [`universal-geometry/`](universal-geometry/)  *(draft)*
**Questions:** [Q13](../qa/Q13-three-compact-dimensions.md), [Q26](../qa/Q26-hadrons-photon-knots.md), [Q32](../qa/Q32-energy-geometry-fundamentals.md)  **Type:** compute/reason  **Depends on:** R13

**Track 0 result (complete):** T² cannot support topological linking — 2D surfaces
lack the extra dimension needed. T³ can, with three linking planes mapping to three
color charges. m_p = 3 × 612 × m_e to 0.008%.

Open: if all particles share a single compact T³, the three circumferences (L₁, L₂, L₃)
are constrained by multi-particle consistency — electron charge, fractional quark
charges (three linked photons), and proton/neutron masses must all fit simultaneously.
Quark confinement = Borromean linking (topological, automatic). If successful, the
T³ geometry is fully fixed by particle data, with no free parameters. Awaits R13.

---

## Backlog

Ordered roughly by priority. Items get an R-number when promoted to Active.

### Flat space → curved appearance  *(Q2)*
The compact space is intrinsically flat (photon sees Cartesian space), but
embedded in 3+1D with toroidal geometry.  The photon's fields project into 3D
through this embedding, producing the Coulomb-like potential.  This is now
understood as the correct physical picture (R12 F14 revised).  The explicit
field projection calculation is R13 Track 3.

### Quadrupole correction  *(Q10, depends on R6)*
The (1,2) orbit has ~2.5% field anisotropy at the rotation horizon (quantified in
S2 F5). A full charge calculation including this anisotropy may shift q/e by a few
percent. Low priority until the charge mechanism itself is settled (R13).

### Precession of torus axis  *(Q19)*
What drives axis precession, and does precession restore approximate spherical
symmetry for the electron's external field? Natural consequence of equations of
motion, or requires an external torque?

### Orbit precession and volume-filling  *(Q23)*
Does a precessing (1,2) orbit reproduce WvM's volume-filling energy flow pattern
(Fig. 2)? This would strengthen the connection between the compact-dimension model
and the original WvM paper's visual picture.

### Photon absorption and excited electrons  *(Q28)*
In this model the electron IS a photon on T². When a QM electron "absorbs a photon"
and jumps to a higher level, what happens in compact-dimension language? Candidate
pictures: extra energy loads into the compact space as a higher harmonic; or the
compact geometry reshapes to accommodate it. If periodic boundary conditions impose
discrete allowed energy increments, this should reproduce atomic spectral lines —
a strong test of the framework. See [`../qa/Q28-photon-absorption.md`](../qa/Q28-photon-absorption.md).

### String theory parallels  *(Q24, Q25)*
A string is a 1D object vibrating on compact geometry; our photon is a 1D wave on
a closed geodesic. Both produce particle properties from winding and harmonics.
How deep is the analogy? Is the T² model a special case of string compactification
on a torus, and does string theory's machinery (modular invariance, T-duality) apply
or constrain our model?

---

## Done

Studies in chronological order of completion. Key result only — see each study's
`findings.md` for the full record.

| # | Study | Key result |
|---|-------|------------|
| 1 | **S1. Toroid series** [`toroid-series/`](toroid-series/) | Null result. The 9% charge deficit is an artifact of geometric approximations, not a real target. |
| 2 | **S2. Toroid geometry** [`toroid-geometry/`](toroid-geometry/) | a/R = 1/√(πα) ≈ 6.60 gives q = e in WvM's formula. Key algebraic result, but not self-consistent (see R6). |
| 3 | **S3. Knot zoo** [`knot-zoo/`](knot-zoo/) | Only (1,2) produces nonzero charge. Fractional charges (e/3, 2e/3) map to specific a/R multiples. Compact dimension hypothesis proposed. |
| 4 | **R1. KK charge comparison** [`kk-charge/`](kk-charge/) | KK gravitational charge is ~10⁻²² × e at Compton scale — ruled out. WvM mechanism is structurally different. 6D decomposition documented for reference. |
| 5 | **R2. Electron from geometry** [`electron-compact/`](electron-compact/) | Photon of energy m_e c² on (1,2) geodesic on T² gives q = e, s = ½, g ≈ 2.0023 with zero free continuous parameters. Framework sound; numerics use S2's r = 6.60 (later revised by R6). |
| — | **R4. B-field / magnetic dipole** *(retired)* | *Not started. Answered within R2: magnetic moment is the net axial projection of B on T². No separate study needed.* |
| — | **R3. Dual visualizer** *(not a study — see [`viz/dual-torus.html`](../viz/dual-torus.html))* | Interactive 3D torus + 2D flat rectangle with synchronized photon animation. Not a research study; reclassified as a visualization tool. |
| — | **R5. Flat space → curved appearance** *(retired)* | *Not started. Subsumed by R13: deriving the 4D effective field from flat T³ via KK decomposition directly answers this question.* |
| 7 | **R6. Guided-wave field profile** [`field-profile/`](field-profile/) | S2's r = 6.60 is not self-consistent. Self-consistent solution: r ≈ 4.29, R ≈ 8.2 × 10⁻¹⁴ m. All profile shapes give q = e; actual profile requires solving the wave equation on T². |
| 8 | **R7. Charge from torus geometry** [`torus-capacitance/`](torus-capacitance/) | Coulomb field energy is ~α × target for all aspect ratios at Compton scale. WvM energy-balance approach overestimates by ~1/α. "Magic ratios" from S2/R6 were artifacts. Correct charge mechanism remains open. |
| — | **R9. Precession causes** *(number retired)* | *Number pre-assigned but study never started. Question lives on in backlog as "Precession of torus axis (Q19)".* |
| — | **R10. Precessing orbit / volume-filling** *(number retired)* | *Number pre-assigned but study never started. Question lives on in backlog as "Orbit precession and volume-filling (Q23)".* |
| 9 | **R11. Prime resonance** [`prime-resonance/`](prime-resonance/) | Eight tracks: no mechanism selects q = 137 from energy cost or primality. q ~ 1/α is partly tautological (follows from using e as input). Real free parameter is r (aspect ratio), not q. → R12. |
| 10 | **R12. Self-consistent fields** [`self-consistent-fields/`](self-consistent-fields/) | Flat T² has no eigenmodes at ω_C (spectral gap ~137×). Curved geodesics give q ≈ 193 — photon sees flat space internally. Flat-for-mass / embedded-for-charge is the correct two-domain picture (not an inconsistency). Track 3 (propagation self-consistency) trivially satisfied on flat T². |
| 11 | **R13. Charge from the embedding** [`kk-charge-t3/`](kk-charge-t3/) | Electron is winding mode (not KK). Multi-winding (68,137) breaks WvM charge mechanism: p = 68 ≠ 1 destroys commensurability, E oscillates 67× relative to surface normal, monopole = 0 (exact). The α problem ≡ the charge mechanism problem: α ≈ 1/137 forces a tradeoff between correct Coulomb energy (multi-winding) and correct charge (p = 1). → Q34. |
| 12 | **R8. Multi-winding electron** [`multi-winding/`](multi-winding/) | (68,137) on sheared T² at r_e scale: mass ✓, spin ½ exact ✓, g = 2 ✓, R/r_e = 0.989 ✓. **Charge mechanism invalidated by R13** — multi-winding breaks WvM commensurability (Q = 0). Spin/g-factor results carry over to any (1,2)-local model. q was never selected; the premise (U_Coulomb = m_e c²/2) was the wrong target (see R15). |
| 13 | **R17. Radiation pressure** [`radiation-pressure/`](radiation-pressure/) | Centrifugal force from confined photon's curved 3D path cannot determine α. Track 4: tube deformation preserves φ-symmetry → charge = 0. Track 5: F ⊥ v (no clumping), σ_φ = const (breathing conservative), force is a consequence of confinement. Positive: force decomposition quantified; confirms model self-consistency. |
