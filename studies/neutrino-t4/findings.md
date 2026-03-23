# R26 Findings

## Track 1a: Neutrino T² mode spectrum

### F1. Assignment A ratio — algebraically exact, r-independent

The mass-squared ratio for Assignment A (modes (1,1), (−1,1), (1,2)) is:

    Δm²₃₁/Δm²₂₁ = (3 − 2s) / (4s)

This depends **only** on shear s₃₄.  The aspect ratio r cancels completely.
Verified numerically at r = 0.5, 1, 2, 5, 10 — identical to 6 decimal places.

Required shear: **s₃₄ = 0.02199** for ratio = 33.60 (experimental value).

### F2. Assignment A has a cosmological mass problem

At physical scale (E₀ = √(Δm²₂₁/(4s)) = 29.26 meV):

| r | m₁ (meV) | m₂ (meV) | m₃ (meV) | Σm (meV) | Status |
|---|----------|----------|----------|----------|--------|
| 1.0 | 40.9 | 41.8 | 64.8 | 147.6 | ✗ exceeds 120 |
| 3.0 | 30.2 | 31.5 | 58.7 | 120.4 | ✗ marginal |
| r → ∞ | 28.6 | 29.9 | 57.9 | 116.4 | ✓ barely |

Assignment A's three neutrinos are **too heavy** at moderate r.  The
cosmological bound Σm < 120 meV is satisfied only for r ≳ 5, where the
1/r² term becomes negligible.  In this limit the three masses are almost
entirely determined by the ring quantum number n₄ and shear:

    m₁ ≈ E₀(1−s),  m₂ ≈ E₀(1+s),  m₃ ≈ E₀(2−s)
    Σm → E₀(4−s) ≈ 116.4 meV

This is a second problem for Assignment A, independent of the spin problem.

### F3. Assignment B — refined parameters

The README's initial estimate (s = −0.09, r = 1.0) gives ratio 33.71
(0.10 off target).  Grid search found the exact solution:

    **s₃₄ = −0.0253,  r = 1.926**  →  ratio = 33.603

At physical scale (E₀ = 5.64 meV):

| Mode | Mass (meV) | Spin |
|------|-----------|------|
| (1,2) = ν₁ | 11.80 | ½ F |
| (3,2) = ν₂ | 14.65 | ½ F |
| (17,2) = ν₃ | 51.67 | ½ F |
| **Σm** | **78.1** | **✓** |

Σm = 78.1 meV — well within the cosmological bound.

### F4. Assignment B — 26 sterile neutrinos (much worse than expected)

The README estimated ~6 intermediate spin-½ modes.  The full catalog
reveals **26 intermediate spin-½ fermion modes** between ν₂ and ν₃.

This happens because each odd |p| value produces four modes:
(+p,+2), (−p,+2), (+p,−2), (−p,−2), grouped into two mass doublets:
- (+p,+2) and (−p,−2):  μ² = p²/r² + (2−ps)²
- (−p,+2) and (+p,−2):  μ² = p²/r² + (2+ps)²

For |p| ∈ {5, 7, 9, 11, 13, 15}: 6 × 4 = 24 modes.
Plus (−17,+2) and (+17,−2): 2 more modes just below ν₃.
Total: 26 intermediate spin-½ fermions.

If these thermalize, each contributes to N_eff.  The Standard Model has
N_eff = 3.044.  Planck constrains N_eff < 3.29 (95% CL).  Even one extra
species thermalizing would violate this bound.  26 sterile neutrinos is
catastrophic unless a suppression mechanism exists.

### F5. Mode proliferation — thousands of sub-eV modes

Both assignments produce enormous numbers of modes below 1 eV:

| Assignment | r | Modes < 1 eV | Spin-½ fermions |
|-----------|---|-------------|----------------|
| A | 1.0 | 3,670 | 68 |
| A | 3.0 | 11,020 | 204 |
| B | 1.926 | 3,720 | 60 |

Most modes are non-fermion (spin-1 fermions, bosons, or higher-spin).
The spin-½ fermion count is manageable IF a selection rule prevents them
from coupling to the weak interaction.  Without such a rule, any of
these modes could be produced in decays.

### F6. Physical scales

| Assignment | E₀ (meV) | L₄ (μm) |
|-----------|---------|--------|
| A | 29.26 | 42.4 |
| B | 5.64 | 219.7 |

Assignment B requires a much larger neutrino T² — L₄ ≈ 220 μm.  This
is within the current experimental bound on deviations from Newtonian
gravity (~ 50 μm), but only if gravity does not propagate in these
compact dimensions.

### F7. Summary of Assignment A vs B scorecard

| Criterion | Assignment A | Assignment B |
|-----------|-------------|-------------|
| Δm² ratio | ✓ exact (r-free) | ✓ exact (at s,r) |
| All spin-½ | ✗ two spin-1 | ✓ all spin-½ |
| Σm < 120 meV | ✗ (needs r ≳ 5) | ✓ (78 meV) |
| Sterile neutrinos | many (all spin types) | 26 spin-½ fermions |
| Parameter freedom | 1 free (r) | 0 free (s,r both fixed) |
| Falsifiability | testable via Σm | testable via sterile ν |

Assignment B is better on spin and cosmology but worse on sterile
neutrinos.  Neither assignment is clean.  Tracks 1b–1f investigate
whether the mode menu can be changed (non-coprime modes, revised spin/
charge formulas) to find a better solution.
