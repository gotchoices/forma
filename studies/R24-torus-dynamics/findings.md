# R24 Findings

## Track 1: T³ mode structure and neutrino flavors

### F1. Automatic charge neutrality
Modes with n₁ = 0 on T³ carry zero charge (follows from R19: charge
requires n₁ = ±1).  These are natural neutrino candidates living on
the *same* compact geometry as the electron — no separate space needed.

### F2. Lightest uncharged modes are pure θ₃
With the third dimension much larger than the first two (L₃ >> L₁, L₂),
the lightest uncharged modes are (0, 0, n₃) with mass ∝ n₃/L₃.
Mixed modes (0, n₂≠0, n₃) have mass ~ m_e/r ~ 100 keV — far too heavy
for neutrinos.

### F3. Integer mass-squared ratio — parameter-free prediction
For modes (0,0,n_a), (0,0,n_b), (0,0,n_c):

    Δm²₃₁/Δm²₂₁ = (n_c² − n_a²) / (n_b² − n_a²)

This depends ONLY on integers.  No continuous parameter.

Experimental target: 33.60 ± 0.9

Best integer solutions:

| (n_a, n_b, n_c) | ratio | deviation | σ   |
|------------------|-------|-----------|-----|
| (7, 10, 42)      | 33.63 | +0.02     | 0.03 |
| (1, 8, 46)       | 33.57 | −0.03     | 0.03 |
| (2, 8, 45)       | 33.68 | +0.08     | 0.09 |
| (2, 7, 39)       | 33.71 | +0.11     | 0.12 |
| (1, 2, 10)       | 33.00 | −0.60     | 0.67 |

The (7,10,42) solution matches the experimental ratio to 0.03σ.
The minimal solution (1,2,10) is at 0.7σ — acceptable but not precise.

Consecutive modes (n, n+1, n+2) give max ratio 8/3 = 2.67.
The experimental ratio 33.6 REQUIRES a gap between ν₂ and ν₃.

### F4. Third dimension size — independent of Ma_e parameters
L₃ is fixed entirely by Δm²₂₁ and the mode assignment:

    L₃ = hc × √((n_b² − n_a²) / Δm²₂₁)

| Assignment | L₃ (μm) | L₃/(2π) (μm) |
|------------|---------|---------------|
| (1, 2, 10) | 247     | 39            |
| (7, 10, 42)| 1082    | 172           |

L₃ does NOT depend on r, s₁₂, or any Ma_e parameter.

### F5. Predicted neutrino masses

For the (1, 2, 10) assignment:
- m₁ = 5.01 meV,  m₂ = 10.02 meV,  m₃ = 50.10 meV
- m₂/m₁ = 2 exactly,  m₃/m₁ = 10 exactly
- Σm = 65 meV  (cosmological bound < 120 meV ✓)

For the (7, 10, 42) assignment:
- m₁ = 8.51 meV,  m₂ = 12.15 meV,  m₃ = 51.03 meV
- Σm = 72 meV  (below bound ✓)

### F6. T³ shear does not modify the θ₃ spectrum
Pure θ₃ modes (n₁ = n₂ = 0) have effective wavevector q₃ = n₃ regardless
of s₁₃ or s₂₃.  Shear only affects modes with nonzero n₁ or n₂.
The mass-squared ratio is immune to all continuous parameter variation.

### F7. Parameter counting — over-determined system
T³ free continuous parameters: r, s₁₃, s₂₃  (3 total).
After using α → s₁₂(r), m_e → L₁, Δm²₂₁ → L₃.

Remaining observables: θ₁₂, θ₂₃, θ₁₃, δ_CP  (4 constraints).

4 constraints on 3 parameters → over-determined → r is predicted.
Model is falsifiable: if the mixing angles cannot be simultaneously
reproduced by any (r, s₁₃, s₂₃), the model fails.

### Open questions from Track 1

**Q1 (critical). Spin of (0,0,n₃) modes.**
Neutrinos are spin-½.  In WvM, spin-½ arises from (1,2) winding
topology.  Mode (0,0,n₃) has no winding → spin mechanism unclear.
If T³ = Ma_e × S¹ (direct product), these modes are spin-0.  A non-trivial
T³ fibration might provide spinor structure.  Must be resolved before
the model is viable.

**Q2. Sterile neutrinos.**
For (1,2,10): modes n₃ = 3–9 exist between ν₂ and ν₃.  If thermalized,
N_eff ≈ 6.1, excluded at >18σ by CMB data (N_eff = 2.99 ± 0.17).
For (7,10,42): the problem is worse (35 intermediate modes).
Need: either a selection rule suppressing their coupling, or evidence
they don't thermalize.

**Q3. PMNS matrix from T³ shear.**
Explicit derivation needed to map (r, s₁₃, s₂₃) → (θ₁₂, θ₂₃, θ₁₃, δ_CP).
If successful, r is predicted and the model becomes fully constrained.

**Q4. Gravity constraint.**
L₃ ~ 250–1080 μm exceeds the ~50 μm range of current gravity tests.
If gravity propagates in the third dimension, these sizes are excluded.
The model requires gravity to be confined to 3+1D non-material dimensions.

---

## Track 2: Wave dynamics on embedded Ma_e

### F8. Linear impulse = eigenmode decomposition
On the flat torus, Fourier modes are eigenmodes and conserve energy
individually.  An impulse rings at all eigenfrequencies simultaneously.
The impulse response IS the eigenvalue spectrum, viewed in the time domain.

### F9. Curvature mixes θ₁ modes within θ₂ sectors
On the embedded torus (ε = 1/r), the θ₁-dependent metric couples
different m values within each θ₂ sector n₂.  Power oscillates
between m values over time, while the total power per sector stays
approximately constant (exact axial symmetry).

This is a direct visualization of the Sturm-Liouville eigenmode
structure from R22: the eigenmodes are not pure Fourier modes but
linear combinations of different m, explaining the observed power flow.

### F10. Position-dependent excitation
An impulse at the outer equator (θ₁ = 0) excites different mode
mixtures than one at the inner equator (θ₁ = π).  The outer equator
is where curvature concentrates eigenmodes (R21 F1), so pulses there
couple more strongly to the localized modes.

### F11. Defocusing nonlinearity does not select modes
With a defocusing cubic term −λψ³ (modeling electromagnetic self-repulsion):
- At λ = 0.5 (artificially strong): energy redistributes between modes
  but does NOT concentrate.  The low-mode fraction E_low/E_tot stays
  between 0.92–0.98 over 50 periods.  No mode selection occurs.
- At physical coupling λ = α ≈ 0.007: the nonlinearity slightly shifts
  eigenfrequencies, producing phase differences relative to the linear
  system.  But no net energy redistribution between mode sectors.

### F12. Conclusion on impulse-based mode selection
The impulse + cubic nonlinearity does NOT solve the r-selection problem.
Defocusing self-interaction disperses energy rather than concentrating it.

Mode selection would require one of:
- A focusing (attractive) nonlinearity
- Energy dissipation (coupling to external degrees of freedom)
- A more physical self-interaction than simple |ψ|²ψ (e.g., long-range
  Coulomb coupling between charge-carrying modes)
- An external constraint from the T³ structure (Track 1's parameter
  over-determination)

---

## Track 3: Aspect ratio selection — closed (pre-empted by F12)

### F13. Track 3 pre-empted
Track 3 was contingent on Track 2 finding mode selection via nonlinear
dynamics, then sweeping over r to find which aspect ratios are stable.
Track 2 found no mode selection (F11–F12): defocusing self-interaction
disperses energy rather than concentrating it.  Track 3's premise does
not hold.

### F14. The r-selection path forward
F12 rules out simple impulse dynamics but points to Track 1's T³
over-determination as the viable alternative.  The parameter-counting
argument (F7) shows 4 observables (PMNS mixing angles) constraining
3 free parameters (r, s₁₃, s₂₃).  If the PMNS mapping can be derived,
r is predicted without needing dynamical mode selection.

The critical path is:
1. **Q1 — Spin:** Do (0,0,n₃) modes carry spin-½?  This is a gate.
   If they're spin-0, the T³ neutrino model fails entirely.
   Requires analytical work on the T³ fibration topology.
2. **Q3 — PMNS from shear:** Derive the mapping
   (r, s₁₃, s₂₃) → (θ₁₂, θ₂₃, θ₁₃, δ_CP).
   This is a well-defined calculation but requires understanding how
   the (0,0,n₃) modes couple to the charged leptons via the weak
   interaction analog in this model.
3. **r prediction:** If Q1 and Q3 succeed, solving the PMNS equations
   yields r (and with it, the full T³ geometry).

Each step depends on the previous.  Step 1 is analytical and cannot
be resolved by simulation — it requires understanding what "spin"
means for a field mode on T³.
