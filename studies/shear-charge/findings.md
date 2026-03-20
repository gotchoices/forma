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

## Summary table

| # | Finding |
|---|---------|
| F1 | α = C(r) × sin²(2πs)/(2−s)², where C(r) = r²/(4π√(r²+4)) — clean dimensionless formula |
| F2 | Critical aspect ratio r_crit ≈ 0.54: shear mechanism requires r > 0.54 |
| F3 | For r = 1: s ≈ 1/(2π), δ ≈ a — shear displacement equals tube radius |
| F4 | The lattice angle deviation (~9° from orthogonal) is stable across r |
| F5 | Full E₀ normalization gives clean result; κ-suppression kills the mechanism |
| F6 | Formula has one equation in two unknowns (r, s) — one more constraint needed |
