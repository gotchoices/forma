# Studies Registry

See [`../STATUS.md`](../STATUS.md) for electron objectives and project snapshot.  
See [`../qa/`](../qa/) for open physics questions and detailed problem analysis.

---

## Active

### R8. Multi-winding electron
**Study:** [`multi-winding/`](multi-winding/)
**Questions:** [Q18](../qa/Q18-deriving-alpha.md)  **Type:** compute  **Depends on:** R7

Find the torus geometry (R, a, winding number q) that produces the electron's
charge, mass, spin, and magnetic moment on a sheared T². R7 showed the torus
must be ~100× smaller than Compton scale. A multi-winding path (~1/α major orbits,
local 1:2 ratio) fits λ_C of path length on a torus of radius ~r_e. R/r_e ≈ 0.989
is robust across resolutions. Spin ½ is exact from the local winding ratio (68:137).
q remains a free parameter — determining what fixes it is the open edge.

### R13. KK charge from flat T³
**Study:** [`kk-charge-t3/`](kk-charge-t3/)
**Questions:** [Q18](../qa/Q18-deriving-alpha.md), [Q29](../qa/Q29-variational-principle-alpha.md), [Q32](../qa/Q32-energy-geometry-fundamentals.md)  **Type:** compute  **Depends on:** R8, R11, R12, R14-Track0

Compute the 4D effective charge of a photon on a geodesic of flat T³ using
Kaluza-Klein field decomposition — without using e as input. The goal: derive
the apparent charge from geometry alone, then check whether the self-energy
constraint (= m_e c²/2) fixes the T³ shape. If it does, α becomes a geometric
prediction rather than an input. Originally framed for T²; upgraded to T³ after
R14 Track 0 showed three compact dimensions are required for hadron linking.
See [`kk-charge-t3/README.md`](kk-charge-t3/README.md) for the full study plan.

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
If compact dimensions are intrinsically flat, how do the photon's fields project
into 3+1D as a Coulomb-like potential? The 6D decomposition from R1 provides the
framework; what remains is explicitly working out the field projection. This is
partly what R13 addresses — it may be subsumed by R13's results.

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
| 6 | **R3. Dual visualizer** [`dual-visualizer/`](dual-visualizer/) | Interactive side-by-side 3D torus + 2D flat rectangle with synchronized photon animation. Shows geodesics as straight lines on the flat T². |
| — | **R5. Flat space → curved appearance** *(retired)* | *Not started. Subsumed by R13: deriving the 4D effective field from flat T³ via KK decomposition directly answers this question.* |
| 7 | **R6. Guided-wave field profile** [`field-profile/`](field-profile/) | S2's r = 6.60 is not self-consistent. Self-consistent solution: r ≈ 4.29, R ≈ 8.2 × 10⁻¹⁴ m. All profile shapes give q = e; actual profile requires solving the wave equation on T². |
| 8 | **R7. Charge from torus geometry** [`torus-capacitance/`](torus-capacitance/) | Coulomb field energy is ~α × target for all aspect ratios at Compton scale. WvM energy-balance approach overestimates by ~1/α. "Magic ratios" from S2/R6 were artifacts. Correct charge mechanism remains open. |
| — | **R9. Precession causes** *(number retired)* | *Number pre-assigned but study never started. Question lives on in backlog as "Precession of torus axis (Q19)".* |
| — | **R10. Precessing orbit / volume-filling** *(number retired)* | *Number pre-assigned but study never started. Question lives on in backlog as "Orbit precession and volume-filling (Q23)".* |
| 9 | **R11. Prime resonance** [`prime-resonance/`](prime-resonance/) | Eight tracks: no mechanism selects q = 137 from energy cost or primality. q ~ 1/α is partly tautological (follows from using e as input). Real free parameter is r (aspect ratio), not q. → R12. |
| 10 | **R12. Self-consistent fields** [`self-consistent-fields/`](self-consistent-fields/) | Flat T² has no eigenmodes at ω_C (spectral gap ~137×). Curved-torus geodesics give q ≈ 193 — compact space must be intrinsically flat. R8's charge calculation is internally inconsistent (mixes flat-T² and 3D-Coulomb). Correct approach: KK decomposition from flat T². → R13. |
