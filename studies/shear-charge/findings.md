# R19 Findings — Shear-induced charge on T²

Study: [`README.md`](README.md)

---

## Track 1. Backwards: derive required shear from known α

Script: [`scripts/track1_backwards_shear.py`](scripts/track1_backwards_shear.py)


### F1. The analytical formula for α from shear

The Gauss's-law integral on the torus surface with the sheared
(1,2) mode gives:

    Q(s) = ε₀ E₀ a²π × sin(2πs) / (2 − s)

where s = δ/(2πa) is the fractional shear, and E₀ is the field
amplitude from total energy m_e c².

Setting Q = e and dividing by 4πε₀ℏc:

    α = C(r) × sin²(2πs) / (2 − s)²

where

    C(r) = r² / (4π √(r² + 4))

This is a **clean, dimensionless equation** in two parameters:
the aspect ratio r = a/R and the fractional shear s.  Given r,
it uniquely determines the required s (or vice versa).  No other
constants enter — everything reduces to geometry.


### F2. Critical aspect ratio

The function sin²(2πs)/(2−s)² has a finite maximum (~0.65
over s ∈ (0, 1)).  For the equation α = C(r) × max to hold,
C(r) must be large enough.  This yields a critical aspect ratio:

    r_crit ≈ 0.54

For r < r_crit:  Q_max < e for any shear.  No solution exists.
For r ≥ r_crit:  a shear s exists that gives Q = e.

This is a **new constraint on the aspect ratio** that was not
available from any previous study.  R11 and R12 left r completely
free.  If the shear mechanism is correct, r > 0.54 is required.


### F3. For r = 1: the shear displacement equals the tube radius

At r = 1 (a = R, the "square" torus):

    s_required = 0.15712
    δ/a = 2πs = 0.987 rad ≈ 56.6°
    q_eff = 1.843

Since δ = s × 2πa = 0.987a, the linear shear displacement
is almost exactly equal to the tube radius:

    **δ ≈ a**

More precisely, s ≈ 1/(2π) to 1.3% accuracy (s/[1/(2π)] = 0.987).
The lattice angle between e₁ and e₂ is 81.1° — a 8.9° deviation
from orthogonal.

This is a **geometrically natural** result.  The shear
displacement equals the tube size, which is the only intrinsic
length scale available in the compact space.


### F4. The ~9° lattice angle is stable across aspect ratios

| r    | s_required | δ/a (deg) | q_eff  | Lattice angle | Off-90° |
|------|------------|-----------|--------|---------------|---------|
| 0.75 | 0.647 *    | 233° *    | 1.353  | (2nd lobe)    | —       |
| 1.00 | 0.157      | 56.6°     | 1.843  | 81.1°         | 8.9°    |
| 1.25 | 0.123      | 44.3°     | 1.877  | —             | —       |
| 1.50 | 0.103      | 37.3°     | 1.897  | —             | —       |
| 2.00 | 0.081      | 29.2°     | 1.919  | 80.8°         | 9.2°    |
| 3.00 | 0.061      | 21.8°     | 1.939  | —             | —       |
| 4.00 | 0.051      | 18.2°     | 1.949  | —             | —       |

(*) At r = 0.75, only the second-lobe solution exists (large shear).

The lattice angle deviation from 90° stays near ~9° for r ≥ 1.
As r increases, the required s decreases (smaller shear fraction)
but δ/a also decreases proportionally, keeping the lattice
geometry similar.


### F5. Normalization uncertainty — the Track 3 question

R15 Track 1 found that the line-source model with U = m_e c²
predicts Q_max ≈ 8e — far too much charge.  The actual electron
has Q = e, implying only fraction κ ≈ α of the E-field energy
couples to 3D as Coulomb field.

If this κ-suppression applies to the shear mechanism:

| Coupling κ     | Q_max/e (r=1) | Solution? |
|----------------|---------------|-----------|
| 1 (full E₀)   | 1.78          | ✓ s=0.157 |
| √α ≈ 0.085    | 0.52          | ✗         |
| 2α ≈ 0.015    | 0.22          | ✗         |
| α ≈ 0.0073    | 0.15          | ✗         |

With full E₀ normalization, the result is clean: s ≈ 1/(2π),
δ ≈ a.

With any significant κ-suppression, Q_max drops below e and
no solution exists.

**Interpretation:** This is the same normalization ambiguity
that has affected every charge calculation in this project.
Track 3 (normalization reconciliation) must determine which E₀
is correct.  However, the fact that the full-E₀ answer gives
the clean result δ ≈ a is suggestive — if the shear mechanism
is Nature's choice, the full E₀ normalization may be correct
(and the κ-suppression from R15 may be an artifact of the
localization-based approach, which shear supersedes).


### F6. The formula relates α, r, and s — reducing free parameters

Previously, the model had two free parameters: r (aspect ratio)
and σ (localization width), connected by α = exp(−4σ²).

The shear mechanism replaces σ with s (shear fraction) and gives
the constraint:

    α = r² sin²(2πs) / (4π√(r²+4) (2−s)²)

This is ONE equation in TWO unknowns (r, s).  It constrains
the model but doesn't fully fix it — one degree of freedom
remains.  To fully determine α, we need a second equation
relating r and s.  Candidates:
- The T³ geometry (R14) imposes constraints on all three shear
  parameters simultaneously
- An energy condition (Track 2) might select a preferred s
- The aspect ratio r might be fixed by some other physics
  (Q52, graviton consistency)

---

## Track 2. Energy balance: is non-zero shear stable?

Script: [`scripts/track2_energy_balance.py`](scripts/track2_energy_balance.py)

**The question:** If we take an unsheared torus and gradually
increase the shear, does the total energy go up (making shear
costly and disfavored) or down (making shear cheap and favored)?
And does the energy reach a minimum at some specific shear value,
which would pin the shear — and therefore α — automatically?


### F7. The photon energy is hc/L_geodesic, not the eigenmode energy

The (1,2) eigenmode of the torus has energy ℏc|k| = ℏc√(1/a² + 4/R²).
For r = 1, this is 5 m_e c² — five times the physical photon energy.
This confirms R12 F6: the photon is a traveling wave, not an eigenmode.

The physical photon has ONE wavelength (λ_C) along the full geodesic
path.  The eigenmode has √((r²+4)(1/r²+4)) ≈ 5 wavelengths per
geodesic for r = 1.


### F8. Shear is energetically cheap — it LOWERS the total energy

When we shear the T², two things happen:

1. **The geodesic path gets longer.**  On the sheared lattice, the
   (1,2) winding follows a longer straight line in the universal
   cover.  Since the photon energy is E = hc/L, a longer path means
   a lower-frequency photon — the mode energy DECREASES.

2. **Charge appears, adding Coulomb energy.**  The non-integer q_eff
   produces Q ≠ 0, and the resulting Coulomb field has self-energy
   E_C > 0.  This INCREASES the total energy.

The key result: **the energy saving from (1) is much larger than
the energy cost from (2).**

At the Track 1 solution (r = 1, s = 0.157, Q ≈ e):

    ΔE_photon = −6.6% of m_e c²   (saved — path got longer)
    E_Coulomb = +0.76% of m_e c²   (cost — charge appeared)
    Net:        −5.8% of m_e c²    (shear LOWERS total energy)

The photon energy saving is **8.6× larger** than the Coulomb cost.

**Plain language:** Shearing the torus is energetically favorable.
The system does not resist shear — it welcomes it.  Having charge
is "cheap" compared to the energy released by lengthening the
geodesic.  This means there is NO energetic barrier preventing
charge from appearing via shear.


### F9. The flat T² does not select a specific shear value

While shear is energetically favorable, E_total(s) keeps
decreasing as s increases — it never reaches a minimum and
turns back up.  There is no "valley" in the energy landscape
that would pin the shear at a specific value.

- At s = 0: dE_total/ds = −0.4 m_e c² per unit s (steep downhill).
- The Coulomb cost starts quadratically (Q ∝ s for small s),
  so it cannot resist the photon energy drop, which is linear.
- E_total continues to decrease all the way to s → 1.

**Plain language:** The flat T² says "shear is fine, go ahead,"
but it doesn't say "stop here."  Shear is a free parameter —
a modulus — just like the aspect ratio r, which has also been
free in every study so far.  The flat T² imposes no constraint
on either one.

**This does NOT mean the mechanism is ruled out.**  It means
the specific shear value must come from outside the flat T²:
- The T³ geometry (needed for quark confinement, R14) has three
  shear parameters constrained by topology.
- Those topological constraints could fix the shear that
  determines α = 1/137.

Think of it this way: the shear mechanism provides the
*formula* (α depends on shear), while T³ topology would
provide the specific *input* (the shear value).


### F10. Hint at large aspect ratios: energy minima at r ≥ 3

At large aspect ratios (r ≥ 2.5) with **fixed** torus geometry,
the Coulomb energy becomes large enough that E_total does develop
local minima:

| r   | s_min  | E_total/m_ec² | Q/e    | α_eq     | α_eq/α  |
|-----|--------|---------------|--------|----------|---------|
| 3.0 | 0.569  | 0.553         | 1.117  | 0.00910  | 1.25    |
| 3.5 | 0.551  | 0.541         | 0.913  | 0.00608  | 0.83    |
| 4.0 | 0.540  | 0.532         | 0.763  | 0.00425  | 0.58    |

At r ≈ 3.2, the equilibrium charge passes through Q = e,
giving α = 1/137.

**Caveat:** These minima occur at E_total ≈ 0.55 m_e c² —
only 55% of the observed electron mass.  This is because the
geometry was held fixed at the s = 0 Compton constraint.  In
a self-consistent picture where the geometry adjusts, the
picture changes.  These are suggestive but not yet physical.


### F11. The EM self-energy is the right size

If the electron carries charge Q = e, the Coulomb field energy
stored around the torus is:

    E_EM = α g(r) √(r²+4) × m_e c² ≈ 0.8% of m_e c²

This is the electromagnetic contribution to the electron's
rest mass — and it matches what QED predicts: an O(α) correction
(about 1 part in 137).  The "bare" photon energy (without the
Coulomb field) is E_bare ≈ 0.992 m_e c².

**Plain language:** The shear mechanism produces the right
amount of charge, and that charge contributes the right amount
of energy to the electron's mass.  Everything is self-consistent.


### Track 2 overall assessment

The shear mechanism is **viable and energetically favorable**:
- Shear lowers the total energy (no barrier to charge appearing)
- The Coulomb self-energy at Q = e matches QED expectations
- Mass and spin are unaffected (topological, not metric)
- The mechanism does not contradict any known physics

What it does NOT do is select the specific shear value on its
own.  The flat T² treats shear as a free parameter.  This is
the same situation as the aspect ratio r — it has been free
throughout all studies.  Both may be determined by the same
external physics (T³ topology).


---

## Summary table

| # | Finding |
|---|---------|
| F1 | α = C(r) × sin²(2πs)/(2−s)², where C(r) = r²/(4π√(r²+4)) — clean dimensionless formula |
| F2 | Critical aspect ratio r_crit ≈ 0.54: shear mechanism requires r > 0.54 |
| F3 | For r = 1: s ≈ 1/(2π), δ ≈ a — shear displacement equals tube radius |
| F4 | The lattice angle deviation (~9° from orthogonal) is stable across r |
| F5 | Full E₀ normalization gives clean result; κ-suppression kills the mechanism |
| F6 | Formula has one equation in two unknowns (r, s) — one more constraint needed |
| F7 | Photon energy = hc/L_geodesic ≠ eigenmode energy (5× for r=1); confirms R12 F6 |
| F8 | Shear is energetically cheap: geodesic saving (6.6%) ≫ Coulomb cost (0.8%); shear is FAVORED |
| F9 | No specific shear selected on flat T² — shear is a free modulus, like r; external constraint needed |
| F10 | Local minima at r ≥ 3 (fixed geometry) pass through α at r ≈ 3.2 — suggestive but wrong mass |
| F11 | EM self-energy = O(α m_e c²), consistent with QED mass correction |
