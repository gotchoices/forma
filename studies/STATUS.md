# Studies Registry

See [`../STATUS.md`](../STATUS.md) for electron objectives and project snapshot.  
See [`../qa/`](../qa/) for open physics questions and detailed problem analysis.

---

## Active

### R15. Forward charge calculation — deriving α
**Study:** [`R15-forward-charge/`](R15-forward-charge/)
**Questions:** [Q18](../qa/Q18-deriving-alpha.md), Q34 Path 7  **Type:** compute  **Depends on:** R7, R13

R7 computed U_Coulomb = α × m_e c² and called it a failure. R8 "fixed" it by
shrinking the torus, requiring R8-multi-winding (68,137). R13 showed R8-multi-winding
breaks WvM charge (monopole = 0, exactly). This revives (1,2) at Compton scale —
the only model where charge works. R15 runs R7's calculation *forward*: input
energy m_e c² and (1,2) topology, compute the far-field Coulomb flux, read off
charge Q, and check whether Q²/(4πε₀ℏc) ≈ 1/137. If so, α is derived from
energy and topology alone.

**Open sub-problem:** the formula α(r,s) produces a one-parameter family of
solutions — every r > ~2 has a self-consistent s.  Nothing currently selects r.

### R27. Ma (the six-dimensional material space) oscillation patterns — particles, atoms, and nuclei
**Study:** [`R27-bound-states/`](R27-bound-states/)
**Questions:** Q16, Q28, Q32  **Type:** compute/analytical  **Depends on:** R26, R19, R15

Discovery engine (`lib/ma_solver.py`) searches for Ma modes matching known particles.
7 tracks complete (54 findings).  Neutron and muon pin r_p = 8.906 and σ_ep = −0.0906,
leaving zero free parameters at MeV scale.  Parameter-free predictions: kaon (1.2%),
eta (0.6%), eta prime (0.3%), phi (0.8%), kaon neutral (1.2%).  Lifetime-gap correlation
r = −0.84 (p = 0.009) for weak decays supports off-resonance hypothesis.  Reaction
energetics: 17/21 decays pass.  Tau at 5.6% (structural gap), pion at 14% (rough).
Ω⁻ structurally forbidden (spin-3/2 + odd charge).  Hydrogen and nuclear stability
deferred to future study (requires multi-mode formalism).  **Substantially complete.**

### R28. Ma spectrum refinement  **Complete**
**Study:** [`R28-particle-spectrum/`](R28-particle-spectrum/)
**Questions:** Q16, Q32  **Type:** compute  **Depends on:** R27

4 tracks, 22 findings.  σ_eν and σ_νp irrelevant (neutrino sheet decouples).
~48 energy bands below 2 GeV, ~900 modes at physical charges vs ~40 known
particles — consistent with off-resonance hypothesis.  **Strange baryon sign
flips resolved**: extending search range to n_max=15 gives Λ at 0.9%, Σ⁺ at
0.3%, all 4 sign flips fixed (21/21 reactions).  W/Z/Higgs match trivially
at high energy — Ma spectrum non-predictive above ~2 GeV (band spacing
< 5 MeV).  Predictive horizon established.

### R29. Atoms and nuclei — from Ma modes to multi-body physics  **Complete**
**Study:** [`R29-atoms-and-nuclei/`](R29-atoms-and-nuclei/)
**Questions:** Q28, Q16  **Type:** theoretical + compute  **Depends on:** R27, R15

4 tracks, 27 findings.  Coulomb potential derived from Ma × S (the three spatial dimensions) (α = 1/137, hydrogen
E₁ = −13.6 eV).  KK boson approach fails for nuclear binding (Yukawa corrections 10⁴×
too large).  Pivoted to direct Ma mode search: nuclei ARE Ma modes.  Scaling law
n₅ = A, n₆ = 2A matches all nuclei d→⁵⁶Fe to < 1%.  Deuteron: 0.02% error, 86% of
binding captured.  Nuclear spins predicted (9/11).  Free neutron ≠ nuclear neutron
(explains nuclear stability).  Two-tier physics: Ma = particles + nuclei (MeV);
S = atoms + stability (eV).  r_e unconstrained by nuclear data.

### R30. Minimal material geometry — is a material sheet necessary?
**Study:** [`R30-minimal-geometry/`](R30-minimal-geometry/)
**Questions:** Q34, Q16  **Type:** theoretical + compute  **Depends on:** R19, R26, R27

Each material sheet represents a curve, not an area.  The persistent r-degeneracy
(r_e free, r_ν ≥ 3.2, only r_p pinned) and 20× ghost-mode over-prediction
suggest possible over-parameterization.  Can a circle reproduce particle
properties?  Is the charge mechanism irreducibly 2D?  What about Klein bottle
identification?  Hierarchical compactification?  Non-uniform circle?  5 tracks.

### R31. The origin of α and the nature of atomic binding  **Complete**
**Study:** [`R31-alpha-derivation/`](R31-alpha-derivation/)
**Questions:** Q34, Q28, Q18  **Type:** theoretical + compute  **Depends on:** R19, R26, R29, R30

6 tracks, 24 findings.  Hydrogen atom is NOT a Ma mode (spectrum
2,830× too coarse).  Casimir energy cannot select α (no minimum).
**Naive KK Yukawa ruled out** — corrections 10³–10⁶× too large for
Lamb shift, requiring KK massive mode coupling suppressed by ≥10⁵.
Ma merging always costs energy (neutron 0.78 MeV heavier than H).
α remains an input; deriving it requires a dynamics/moduli potential
not yet in the model.  r_e confirmed as a geometric constant, not
per-electron.

### R32. The running of α and the UV coupling  **Complete**
**Study:** [`R32-alpha-running/`](R32-alpha-running/)
**Questions:** Q77, Q18, Q47  **Type:** compute + theoretical  **Depends on:** R19, R27, R28, R31

4 tracks.  Tests the hypothesis that α is the impedance mismatch between Ma
and S.  **Result:** Moderate-to-null.  Naive KK running is catastrophic
(157,000× SM), confirming ~10⁵ ghost mode suppression.  Volume dilution gives
α_bare ≈ 1/5, not 1/24.  The Dedekind η²⁴ is the strongest connection to 24.
The α formula's 4π IS the 3D solid angle; the shear sin²(2πs) dominates.
"Why α = 1/137?" reduces to "why s ≈ 0.01?" — the shear is currently reverse-
engineered from α, not independently determined.  F1–F23.  Track 2: volume
dilution and the bare UV coupling.  Track 3: why 24? — geometric relationships
between torus lattices and the number 24 (modular functions, kissing numbers,
refraction geometry).  Track 4: impedance/transmission coefficient at the
Ma/S interface via waveguide/cavity QED.

### R34. The midpoint coupling — bidirectional modulation of α  **Complete**
**Study:** [`R34-midpoint-coupling/`](R34-midpoint-coupling/)
**Questions:** Q77, Q18  **Type:** compute + theoretical  **Depends on:** R19, R31, R32

4 tracks.  R32 found the weighted gauge partition gives 1/80 = (137+24)/2
to 99.8%.  Tests whether this is a geometric base coupling with bidirectional
Kramers-Kronig dispersion: Ma modes as absorption resonances modulate α
upward (IR → 137) and downward (UV → 24) from the midpoint.  Track 1:
dispersive integral.  Track 2: locate the resonance scale.  Track 3: derive
the shear from 1/80 instead of 1/137.  Track 4: clockwise/counterclockwise
interference on the torus as the bidirectional mechanism.


### R35. Threshold detection and material-dimension coupling  **Complete**
**Study:** [`R35-threshold-coupling/`](R35-threshold-coupling/)
**Questions:** Q78, Q32  **Type:** compute + theoretical  **Depends on:** R26, R19, R27, R33

4 tracks (all complete, F1–F34).  Motivated by the unified mode-density
picture (Q85 §14): threshold "continuity" is mode-hopping on the
neutrino sheet's dense ladder.  Track 1 (F1–F7): Cd-109 Re/Rc = 33
reproduced via SCA upper-limit mechanism.  Na-22 constrains pre-load.
Track 2 (F29–F34): reframed around elastic torus (g_EM = 0).  Storage
10–324 bits/cell.  Write ~70 ps/hop (ATP-driven).  Read ~3 ps
(passive, SNR ~ 10⁷).  Fidelity > 99.99%.  THz can't directly drive
ν-modes; revised L01 uses thermal degradation.  Reiter's source
saturates pre-load (fill/leak ~ 10¹²).
Track 3 (F8–F21): three-layer protection is direction-independent
(F15) and symmetric (F16).  Elastic torus resolves I/O (F17).
Coulomb field = monopole projection of material-dimension structure
(F19).  Non-uniform voltage on cell membrane (F20) — Levin's Vmem
is the DC component of a harmonic pattern (F21).
Track 4 (F22–F28): flat Ma coupling exactly zero (F22).  Elastic
torus shifts I/O to geometry (F23).  Goldilocks: F_write/kT > 10
(F24).  ATP opens window K ∈ [0.043, 0.080] eV⁻¹ (F27).  Writing
REQUIRES metabolic energy.

### R36. Geometric tilt — α from Ma_e/S embedding without KK  **Complete**
**Study:** [`R36-geometric-tilt/`](R36-geometric-tilt/)
**Questions:** Q77, Q76, Q18  **Type:** compute + theoretical  **Depends on:** R19, R26, R34

Drops KK entirely.  Ma_e axes are orthogonal internally (s=0), but the Ma_e
plane is tilted relative to S by angle θ.  The tilt determines how much S
"sees" of material modes — α = f(θ).  Electromagnetic interaction emerges
from the S-projection of material-dimension momentum, not from gauge fields.  α may
be a free "designer's choice" parameter rather than a derivable constant.
Track 1: tilt formalism and mode projection.  Track 2: mode-mode coupling
(does 1/r Coulomb emerge?).  Track 3: ghost mode projection.  Track 4:
mass spectrum preservation.

### R37. Membrane mechanics — gravity and stability from the Ma_e/S interface  **Complete**
**Study:** [`R37-membrane-mechanics/`](R37-membrane-mechanics/)
**Questions:** Q2, Q76  **Type:** theoretical + compute  **Depends on:** R19, R26, R17, R18, R31, R35, R36

12 findings.  Gravity "derivation" (Tracks 2–3) tautological (GR restated).
KEY RESULT (F7): constrained energy minimisation along the alpha curve
gives r ≈ 0.50 — a broad minimum (r = 0.4–0.6 within 0.5% of optimal),
but r = 6.6 is 91% higher, decisively ruling out thin-torus geometries.
First physical mechanism to prefer a specific region of the alpha curve.
Anisotropic correction requires the **moduli potential** (the vacuum energy
of Ma_e as a function of shape) — the same deep unknown that blocks
computing R35's Goldilocks K.  Other genuine results: computable elastic
constants (F2), electron sheet ~10⁶× too stiff for R35 coupling (F10),
self-gravity negligible (F5).

### R33. Ghost mode selection — why most Ma modes are dark  **Paused**
**Study:** [`R33-ghost-selection/`](R33-ghost-selection/)
**Questions:** Q77, Q34  **Type:** compute + theoretical  **Depends on:** R19, R27, R28, R31, R32

8 tracks (2 complete, 1 dead, 5 deferred).  15 findings.  The n₁ = ±1
selection rule (F1) kills 88% of modes.  The spin-statistics filter (F3,
spin = n₁/n₂) kills most of the rest.  Result: ~860 ghosts reduced to 4
per charged sheet — the (1,±1) spin-1 bosons and (1,±2) spin-½ fermions.
The (1,1) boson at half the electron mass is the critical remaining
tension: unobserved but charged with valid spin.  Track 8 (wave-optics)
found ω⁴ radiation suppression gives it ~1/16× the electron's radiation
efficiency (F10), but this is model-dependent (F14).  Track 7 (r_e scan)
is dead — the charge integral cannot pin r_e (F8).  Remaining: Track 6
(spin derivation) could change the ghost landscape entirely; Tracks 2–5
are cleanup.  Neutrino-sheet ghosts are a feature, not a bug (Q85 §8).

---

## Backlog

Ordered roughly by priority. Items get an R-number when promoted to Active.

### Flat space → curved appearance  *(Q2)*
The material space is intrinsically flat (photon sees Cartesian space), but
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
(Fig. 2)? This would strengthen the connection between the material-dimension model
and the original WvM paper's visual picture.

### Photon absorption and excited electrons  *(Q28)*
In this model the electron IS a photon on Ma_e. When a QM electron "absorbs a photon"
and jumps to a higher level, what happens in material-dimension language? Candidate
pictures: extra energy loads into the material space as a higher harmonic; or the
material geometry reshapes to accommodate it. If periodic boundary conditions impose
discrete allowed energy increments, this should reproduce atomic spectral lines —
a strong test of the framework. See [`../qa/Q28-photon-absorption.md`](../qa/Q28-photon-absorption.md).

### String theory parallels  *(Q24, Q25)*
A string is a 1D object vibrating on material geometry; our photon is a 1D wave on
a closed geodesic. Both produce particle properties from winding and harmonics.
How deep is the analogy? Is the material-sheet model a special case of string compactification
on a torus, and does string theory's machinery (modular invariance, T-duality) apply
or constrain our model?

---

## Done

Studies in chronological order of completion. Key result only — see each study's
`findings.md` for the full record.

| # | Study | Key result |
|---|-------|------------|
| 1 | **S1. Toroid series** [`S1-toroid-series/`](S1-toroid-series/) | Null result. The 9% charge deficit is an artifact of geometric approximations, not a real target. |
| 2 | **S2. Toroid geometry** [`S2-toroid-geometry/`](S2-toroid-geometry/) | a/R = 1/√(πα) ≈ 6.60 gives q = e in WvM's formula. Key algebraic result, but not self-consistent (see R6). |
| 3 | **S3. Knot zoo** [`S3-knot-zoo/`](S3-knot-zoo/) | Only (1,2) produces nonzero charge. Fractional charges (e/3, 2e/3) map to specific a/R multiples. Material dimension hypothesis proposed. |
| 4 | **R1. KK charge comparison** [`R1-kk-charge/`](R1-kk-charge/) | KK gravitational charge is ~10⁻²² × e at Compton scale — ruled out. WvM mechanism is structurally different. 6D decomposition documented for reference. |
| 5 | **R2. Electron from geometry** [`R2-electron-compact/`](R2-electron-compact/) | Photon of energy m_e c² on (1,2) geodesic on Ma_e gives q = e, s = ½, g ≈ 2.0023 with zero free continuous parameters. Framework sound; numerics use S2's r = 6.60 (later revised by R6). |
| — | **R4. B-field / magnetic dipole** *(retired)* | *Not started. Answered within R2: magnetic moment is the net axial projection of B on Ma_e. No separate study needed.* |
| — | **R3. Dual visualizer** *(not a study — see [`viz/dual-torus.html`](../viz/dual-torus.html))* | Interactive 3D torus + 2D flat rectangle with synchronized photon animation. Not a research study; reclassified as a visualization tool. |
| — | **R5. Flat space → curved appearance** *(retired)* | *Not started. Subsumed by R13: deriving the 4D effective field from flat Ma via KK decomposition directly answers this question.* |
| 7 | **R6. Guided-wave field profile** [`R6-field-profile/`](R6-field-profile/) | S2's r = 6.60 is not self-consistent. Self-consistent solution: r ≈ 4.29, R ≈ 8.2 × 10⁻¹⁴ m. All profile shapes give q = e; actual profile requires solving the wave equation on Ma_e. |
| 8 | **R7. Charge from torus geometry** [`R7-torus-capacitance/`](R7-torus-capacitance/) | Coulomb field energy is ~α × target for all aspect ratios at Compton scale. WvM energy-balance approach overestimates by ~1/α. "Magic ratios" from S2/R6 were artifacts. Correct charge mechanism remains open. |
| — | **R9. Precession causes** *(number retired)* | *Number pre-assigned but study never started. Question lives on in backlog as "Precession of torus axis (Q19)".* |
| — | **R10. Precessing orbit / volume-filling** *(number retired)* | *Number pre-assigned but study never started. Question lives on in backlog as "Orbit precession and volume-filling (Q23)".* |
| 9 | **R11. Prime resonance** [`R11-prime-resonance/`](R11-prime-resonance/) | Eight tracks: no mechanism selects q = 137 from energy cost or primality. q ~ 1/α is partly tautological (follows from using e as input). Real free parameter is r (aspect ratio), not q. → R12. |
| 10 | **R12. Self-consistent fields** [`R12-self-consistent-fields/`](R12-self-consistent-fields/) | Flat Ma_e has no eigenmodes at ω_C (spectral gap ~137×). Curved geodesics give q ≈ 193 — photon sees flat space internally. Flat-for-mass / embedded-for-charge is the correct two-domain picture (not an inconsistency). Track 3 (propagation self-consistency) trivially satisfied on flat Ma_e. |
| 11 | **R13. Charge from the embedding** [`R13-kk-charge-t3/`](R13-kk-charge-t3/) | Electron is winding mode (not KK). Multi-winding (68,137) breaks WvM charge mechanism: p = 68 ≠ 1 destroys commensurability, E oscillates 67× relative to surface normal, monopole = 0 (exact). The α problem ≡ the charge mechanism problem: α ≈ 1/137 forces a tradeoff between correct Coulomb energy (R8-multi-winding) and correct charge (p = 1). → Q34. |
| 12 | **R8. Multi-winding electron** [`R8-multi-winding/`](R8-multi-winding/) | (68,137) on sheared Ma_e at r_e scale: mass ✓, spin ½ exact ✓, g = 2 ✓, R/r_e = 0.989 ✓. **Charge mechanism invalidated by R13** — R8-multi-winding breaks WvM commensurability (Q = 0). Spin/g-factor results carry over to any (1,2)-local model. q was never selected; the premise (U_Coulomb = m_e c²/2) was the wrong target (see R15). |
| 13 | **R17. Radiation pressure** [`R17-radiation-pressure/`](R17-radiation-pressure/) | Centrifugal force from confined photon's curved 3D path cannot determine α. Track 4: tube deformation preserves φ-symmetry → charge = 0. Track 5: F ⊥ v (no clumping), σ_φ = const (breathing conservative), force is a consequence of confinement. Positive: force decomposition quantified; confirms model self-consistency. |
| 14 | **R18. Torus stiffness** [`R18-torus-stiffness/`](R18-torus-stiffness/) | Geometric deformation cannot produce charge. Track 1: backwards stiffness κ = ε₀E₀²/(2R), α-independent at linear order. Track 2: Coulomb cost exceeds photon energy saving by 96×. Symmetric torus is stable. Charge integral of cos(θ+2φ) vanishes on any smooth torus. |
| 15 | **R14. Universal geometry** [`R14-universal-geometry/`](R14-universal-geometry/) | Three-photon linking model for hadrons ruled out. Charge depends on mode numbers, not spatial arrangement (F18). All redistribution mechanisms fail. Positive: spin quantization protects electron (F10); uncharged modes can add mass (F8). |
| 16 | **R20. Harmonic proton** [`R20-harmonic-proton/`](R20-harmonic-proton/) | Proton/neutron as fundamental + uncharged harmonics on Ma_e. 5 tracks, 21 findings. Harmonics exactly uncharged (F1), decay energetics match (F9), stability explained (F10), muon/tau = "hot electrons" (F17), neutrino excluded from the electron sheet (F14). Descriptive model complete; predictivity requires embedding curvature (→ R21). |
| 17 | **R16. Harmonic charge** [`R16-harmonic-charge/`](R16-harmonic-charge/) | Paused indefinitely.  R18 showed axisymmetric curvature cannot mix modes into charge — needs φ-symmetry breaking.  Superseded by R19 (shear provides the symmetry breaking).  Analytical complement to R15 never materialized. |
| 18 | **R19. Shear-induced charge** [`R19-shear-charge/`](R19-shear-charge/) | Shear breaks φ-symmetry → first mechanism producing charge from delocalized wave.  α(r,s) formula derived (Tracks 1–3).  Quark program (Tracks 4–6) ruled out: single-photon quarks from shear definitively excluded (F24, F33).  3D integral predicts electron is lightest charged particle (F31).  Free parameter r remains open (→ R15).  **Track 8 (reopened):** KK convention reconciliation — α formula re-derived under correct KK Compton constraint (F35–F43).  KK is the rigorous wave-equation result; WvM was a classical approximation.  Same charge physics, updated s(r) curve. |
| 19 | **R21. Quarks from embedding curvature** [`R21-embedding-quarks/`](R21-embedding-quarks/) | Curvature concentrates modes, lifts ±n₁ degeneracy (T1).  Charge ratios continuous, not quantized — single-torus quarks insufficient (T2).  Parity selection rule: all harmonics must be sin-like; cos-like electron is unique charged mode (T5 F12).  Selects R20 harmonic spectrum. |
| 20 | **R22. Mode coupling** [`R22-mode-coupling/`](R22-mode-coupling/) | Spectral S-L solver: curvature makes harmonics heavier (δ/n ≈ 0.26 ε²), proton mass decreases slightly (ΔM ≈ −53 m_e at r=3).  Correction monotonic in r — does not select r (F4).  θ₂ symmetry preserved by backreaction (F5) — phonon neutrino definitively ruled out.  Tracks 2–3 deferred: R22-mode-coupling matrix cannot select spectrum without nonlinear dynamics. |
| 21 | **R23. Neutrino from harmonic beating** [`R23-neutrino-beating/`](R23-neutrino-beating/) | Δm² ratio 33.6 achievable by many triplets — not selective (T1).  θ₂-momentum conservation blocks phonon mechanism (T2).  R22 F5 closes last rescue path (backreaction preserves θ₂).  Single-sheet neutrino ruled out.  Neutrino mechanism remains open. |
| 22 | **R24. Torus dynamics** [`R24-torus-dynamics/`](R24-torus-dynamics/) | 3-torus neutrinos: modes (0,0,n₃) uncharged, mass ratio 33.63 from integers alone (0.03σ), Σm = 72 meV, system over-determined → r predicted (T1 F1–F7).  Wave dynamics: defocusing nonlinearity does not select modes (T2 F8–F12).  r-selection via dynamics pre-empted (T3).  Critical open: spin of (0,0,n₃) → R25. |
| 23 | **R25. Neutrino spin** [`R25-neutrino-spin/`](R25-neutrino-spin/) | Charge-spin linkage (F4): both charge (n₁ = ±1) and spin-½ (n₁ odd) are controlled by tube winding n₁.  "Uncharged" and "fermion" are mutually exclusive — WvM cannot produce neutrinos.  3-torus kinematic success (R24 T1) blocked at spin gate.  PMNS path to r-selection closed.  Neutrino mechanism remains the central open problem. |
| 24 | **R26. Three tori — Ma** [`R26-neutrino-t4/`](R26-neutrino-t4/) | Ma = the three material sheets (electron, neutrino, proton).  Neutrino mass ratio Δm²₃₁/Δm²₂₁ = 33.6 from shear s₃₄ = 0.022 (exact, r-independent).  Charge-neutral neutron mode (1,2,0,0,1,2) reproduces m_n at |σ_ep| ≈ 0.038.  Parameter census: 21 total, 15 free (3 aspect ratios + 12 cross-shears) — under-determined.  Casimir–mass tension (F73): vacuum energy wants maximal coupling, mass spectrum wants minimal — first candidate for a self-selecting principle.  75 findings across 4 tracks. |
