# R37 Findings — Membrane mechanics at the T²/R³ interface

Study: [`README.md`](README.md)

**Honesty note:** Tracks 2–3 attempted to "derive" gravity from
membrane mechanics.  The gravity results are tautological —
they restate GR in membrane vocabulary.  The genuine, non-trivial
results are: computable elastic constants (Track 1), the aspect
ratio selection (Track 2b), and the electron-sheet stiffness
constraint (Track 5).

---

## Track 1 — Radiation stress tensor on the T² surface

### F1. The (1,2) mode stress is anisotropic and uniform

The momentum fractions on T² are:

    f₁ (tube) = r²/(r² + q₂²)
    f₂ (ring) = q₂²/(r² + q₂²),   q₂ = 2−s

For a running wave, the energy density ρ = m_e c²/A is constant
over T² — no spatial pattern, only directional anisotropy.
The isotropic crossover is at r ≈ 2.  For r < 2 the stress is
ring-dominated; for r > 2, tube-dominated.

### F2. Elastic constants σ_m and μ_m are computable

At any point on the alpha curve, α fixes s (via R19), which
determines the anisotropic stress ΔP = ρ|f₁ − f₂|:

    μ_m = ΔP / s     (shear modulus — r-dependent)
    σ_m = ρ/2 = P_iso  (surface energy density — from F4)

These are determined by the mode geometry and α — no free
parameters.

---

## Track 2 — Force balance and particle stability

### F3. Stable equilibrium exists in L₁

E_photon ∝ 1/L₁ balances E_surface ∝ L₁².  At equilibrium:

    σ_m = E/(2A) = P_iso,   E_surface = E_photon/2

d²E/dL₁² > 0 for any σ_m > 0 — unconditionally stable.

### F4. Isotropic membrane equilibrium gives r = 1/(2−s)

Setting ∂E/∂r = 0 with isotropic σ_m gives:

    μ² = 2/r²  →  (2−s)² = 1/r²  →  r = 1/(2−s)

This is a second constraint in the (r, s) plane, independent
of the alpha curve.

### F5. Self-gravity is negligible

    δg₀₀(R₂) ≈ 10⁻³⁵

Validates treating T² as flat in all calculations.

### F6. Gravity is tautological and blind to r

The Schwarzschild metric follows from the equivalence principle
for any localised energy source.  It depends only on total mass
m_e c², not on (r, s).  Gravity cannot distinguish different
torus aspect ratios and cannot be used to infer r.

---

## Track 2b — Aspect ratio selection

### F7. Two independent constraints select r ≈ 0.53

The alpha curve (R19 charge integral):

    alpha_kk(r, s) = 1/137

and the isotropic membrane equilibrium (F4):

    r = 1/(2−s)

are independent constraints in the (r, s) plane.  Their
intersection is the unique point where both the electromagnetic
coupling and the energy balance are simultaneously satisfied:

    r = 0.5304,  s = 0.1146,  α = 1/137  ✓

This is a fat torus (ring ≈ 53% of tube).  A mirror solution
exists at r = 0.631, s = 0.415 (large-shear branch, near a
zero of sin²(2πs) — likely less physical).

This is the first physical mechanism that selects a specific
point on the alpha curve rather than leaving r as a free
parameter.

**Script:** `scripts/track2b_aspect_ratio_selection.py`

### F8. The selected r is in the fat-torus regime, far from 6.6

The historical r = 6.6 (from S2) was always weakly motivated
and was later flagged as inconsistent by R6.  The membrane
equilibrium selects r < 1 — a qualitatively different geometry.

At r = 6.6, the membrane equilibrium constraint gives
r_membrane = 1/(2−0.010) = 0.503, confirming that r = 6.6
is NOT an energy minimum.  It would require anisotropic
physics or external constraint.

### F9. Caveat: isotropic limit only

The membrane constraint used isotropic surface tension.  The
actual stress is anisotropic (F1).  With anisotropy included,
the equilibrium r would shift.  The r = 0.53 result establishes
the REGIME (fat torus, r < 1) but not the precise value.

---

## Track 5 — Synthesis and R35 connection

### F10. Electron sheet too stiff for direct molecular coupling

Total shear spring constant of the electron T²:

    k_e = μ_m × A ~ 10⁷ eV  (r-dependent)

R35's Goldilocks window requires ~17 eV stiffness.  The electron
sheet is ~10⁶× too stiff.  Biological coupling (R35 Hypothesis I)
cannot go through direct modulation of the electron T².

### F11. Neutrino sheet stiffness not computable from R37

R37's membrane constants characterise the electron sheet only.
The neutrino sheet stiffness depends on the T⁶ moduli potential
— the same open question as R35 F28.

### F12. The Goldilocks window is thermodynamic, not geometric

K ∈ [1/F_ATP, 0.1/kT] is set by the ratio F_ATP/kT ≈ 19.
The membrane picture adds no constraint beyond R35.

---

## Summary table

| Finding | Content | Genuine? |
|---------|---------|----------|
| F1 | Anisotropic, uniform stress; crossover at r ≈ 2 | Yes |
| F2 | σ_m, μ_m computable from mode geometry + α | Yes |
| F3 | Stable equilibrium in L₁ | Yes |
| F4 | Isotropic membrane gives r = 1/(2−s) | Yes |
| F5 | Self-gravity negligible | Yes — consistency check |
| F6 | Gravity tautological and blind to r | Tautological |
| **F7** | **Alpha curve ∩ membrane equilibrium → r = 0.53** | **Yes — key result** |
| F8 | Selected r is fat-torus regime, far from 6.6 | Yes |
| F9 | Isotropic limit caveat | Honest limitation |
| F10 | Electron sheet too stiff for R35 coupling | Yes |
| F11 | ν-sheet stiffness not computable here | Honest negative |
| F12 | Goldilocks is thermodynamic | Dimensional analysis |
