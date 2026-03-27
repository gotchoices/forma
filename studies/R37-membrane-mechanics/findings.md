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

### F7. Constrained energy minimisation selects r ≈ 0.50 (broad)

After substituting the L₁ equilibrium (F3), the total energy
along the alpha curve reduces to:

    E_total(r) ∝ μ(r, s(r))^(2/3) × r^(1/3)

where s(r) is fixed by alpha_ma(r,s) = 1/137.  Numerically
minimising this gives:

    r ≈ 0.50,  s ≈ 0.120,  α = 1/137  ✓

This is a fat torus (ring ≈ 50% of tube).  The minimum is
**very broad**: r = 0.4 to 0.6 lies within 0.5% of the
minimum energy, while r = 6.6 is 91% higher — decisively
ruled out.

This is the first physical mechanism that prefers a specific
region of the alpha curve rather than leaving r as a free
parameter.  It selects the fat-torus regime (r < 1) but does
not sharply pin a value.

**Script:** `scripts/track2b_aspect_ratio_selection.py`

### F8. r = 6.6 is decisively ruled out

The historical r = 6.6 (from S2) was always weakly motivated
and was later flagged as inconsistent by R6.  The membrane
energy minimisation confirms it is far from equilibrium:

    Cost(r=0.50) = 1.556   (minimum)
    Cost(r=6.6)  = 2.973   (+91%)

The electron is a fat torus (r < 1), not a thin one (r > 1).

### F9. Anisotropic correction requires the moduli potential

The membrane constraint used isotropic surface tension
(E_boundary = σ_m × A).  The actual boundary energy depends
on how the T² shape maps to the vacuum energy of the compact
manifold — the **moduli potential**.  This is the same deep
unknown that blocks computing R35's Goldilocks K (F11).

The Casimir energy of the T² is calculable but negligible
(~10⁻⁹ of the mode energy).  Any stronger anisotropic
restoring force must come from the full moduli potential,
which is not derivable within the current framework.

The isotropic result establishes the REGIME (fat torus, r < 1)
but the precise value of r awaits the moduli potential.

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
The neutrino sheet stiffness depends on the Ma moduli potential
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
| **F7** | **Energy min along alpha curve → r ≈ 0.50 (broad)** | **Yes — key result** |
| F8 | r = 6.6 decisively ruled out (+91% energy) | Yes |
| F9 | Anisotropic correction requires moduli potential | Honest limitation |
| F10 | Electron sheet too stiff for R35 coupling | Yes |
| F11 | ν-sheet stiffness not computable here | Honest negative |
| F12 | Goldilocks is thermodynamic | Dimensional analysis |
