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

### F8. Assignment A is the electron's mode pattern, downscaled

Assignment A's triplet (1,1), (−1,1), (1,2) is the same mode pattern
that exists on the electron T²: the electron is (1,2), and the two
nearest modes with the same tube winding are (1,1) and (−1,1).
Assignment A places this pattern on a separate T² at a larger scale.

This means Assignment A is equivalent to asking: "at what scale does
the electron's mode pattern produce the neutrino mass splittings?"
The answer is E₀ ≈ 29 meV (L₄ ≈ 42 μm) — the same mode geometry,
10⁸× larger.

### F9. The μm torus size is a hard constraint, not a modeling choice

A neutrino mass eigenstate is a particle at rest with energy m_ν c².
In the WvM framework, this rest energy IS the mode energy on the
compact space: E = E₀√((n₃/r)² + (n₄ − n₃s)²).  Because the mode
energy and mode differences both scale linearly with E₀ = ℏc/L₄,
you cannot make the modes high-frequency while keeping the differences
small — everything scales together.

The neutrino cannot be a "beat" between high-frequency modes on a
smaller torus.  A beat frequency determines the oscillation rate
(which is Δm²/E), but the particle's rest mass is the individual
mode energy, not the beat.  Experiment bounds each neutrino mass to
≲ 50 meV, which requires E₀ ~ meV, which requires L₄ ~ μm.

This makes the μm neutrino T² one of the model's most distinctive
predictions — and one of its most testable.  Short-range gravity
experiments probing below 50 μm could detect the extra dimensions
if gravity propagates there.

---

## Track 1b: All-spin-½ triplet search

### F10. 175 of 286 triplets match the ratio — non-selective

Searched all C(13,3) = 286 triplets of odd p values from 1 to 25.
175 triplets (61%) produce a (s, r) solution matching Δm²₃₁/Δm²₂₁ =
33.6 ± 0.9.  The ratio constraint alone does not select a unique
mode assignment — many triplets work.

### F11. No clean solution exists

**No triplet with p ≤ 25 achieves both zero sterile neutrinos and
Σm < 120 meV.**

The minimum sterile counts are:

| Min N_sterile | Triplets | Σm status |
|--------------|----------|-----------|
| 2 | (7,11,13), (9,11,13), (1,3,5), ... | All ✗ (Σm = 140–510 meV) |
| 6 | **(3,7,11)**, **(3,9,13)**, ... | Some ✓ |
| 10 | (5,9,15), (1,9,15), ... | Most ✓ |

The two best viable candidates:

| Triplet | s | r | Σm (meV) | N_sterile | L₄ (μm) |
|---------|------|------|---------|----------|---------|
| (3,7,11) | 0.379 | 9.17 | 96.3 | 6 | 56.7 |
| (3,9,13) | 0.292 | 8.51 | 117.4 | 6 | 50.3 |

### F12. The sterile count is structural — cannot reach zero

The minimum achievable sterile count for any triplet that also
satisfies the cosmological bound is **6**.  This is structural:

1. **Gap modes:** Between p₂ and p₃ there is always at least one
   odd integer (since p₃ − p₂ ≥ 4 for the ratio to be large enough).
   Each intermediate odd |p| produces 4 modes: (±p, ±2).
2. **Low-p modes:** The p = 1 modes (±1, ±2) are lighter than most
   triplet members and often fall in the ν₂–ν₃ gap.
3. **Scaling law:** N_sterile ≈ 4 × (number of odd integers between
   p₂ and p₃) + boundary contributions.

The ratio ≈ 33.6 requires μ²(p₃)/μ²(p₁) ≫ 1, which forces a large
span p₃ − p₁.  Narrowing the span to minimize sterile modes pushes
the individual masses up (larger E₀), violating the cosmological bound.
These two constraints work against each other, producing an irreducible
minimum of 6 sterile spin-½ fermion modes.

### F13. Consecutive-p triplets minimize sterile count but fail cosmology

Triplets with smallest p₃ − p₂ gap (consecutive odd: p₃ = p₂ + 2)
achieve N_sterile = 2, but all require Σm > 140 meV, exceeding the
cosmological bound.  Examples:

    (7,11,13): Σm = 307 meV,  N_sterile = 2
    (1, 3, 5): Σm = 151 meV,  N_sterile = 2
    (1, 7, 9): Σm = 140 meV,  N_sterile = 2

The conflict: consecutive p values give small splittings only at large
s (strong shear) and large r, which pushes E₀ high and Σm above the
cosmological bound.

### F14. Track 1b conclusion — Assignment B definitively fails

The sterile neutrino problem cannot be solved within the all-spin-½
(p, 2) framework:

- Zero-sterile solutions do not satisfy cosmology
- Cosmology-satisfying solutions have ≥ 6 sterile neutrinos
- The conflict is structural (scaling law), not accidental
- Extending to p > 25 makes things worse (more intermediate modes)

This closes Assignment B.  The remaining paths are:
- Track 1c: non-coprime or cross-plane modes (different mode menu)
- Track 1d: revised spin formula (rescue Assignment A)
- Track 1e: revised charge formula (change which modes are uncharged)
- Track 1f: direct spin resolution for Assignment A

---

## Track 1c: Non-coprime and higher-order modes

### F15. Non-coprime modes are harmonics, not new fundamentals

A non-coprime mode (n₃, n₄) with d = gcd(|n₃|, |n₄|) > 1 decomposes
as d × (p, q) where (p, q) is a coprime fundamental.  It has:

- **Same spin** as the fundamental: L_z = ℏ/|q|
- **d × the energy** of the fundamental (d wavelengths fit in the path)
- **Same fermion/boson classification** (determined by |p| odd/even)

Example: mode (2,4) is the 2nd harmonic of (1,2).  It has spin-½ and
twice the electron's mass, not a new particle type.

### F16. Non-coprime modes worsen the sterile neutrino problem

Including non-coprime modes in the spectrum adds 472 additional spin-½
fermion modes below 1 eV (at Assignment A parameters), on top of the
200 coprime spin-½ fermions.  Total: 672 spin-½ fermion modes below 1 eV.

Non-coprime harmonics fill in the gaps between coprime modes, making
the spectrum denser.  A triplet like (1,2), (2,4), (10,20) — all
harmonics of (1,2) — gives ratio ≈ 33 but has **88 intermediate
spin-½ fermion modes**, far worse than the coprime search (minimum 6).

### F17. Cross-plane modes on T⁶ are too heavy to be neutrinos

A cross-plane mode has nonzero winding on two or more T² subplanes.
In the zero-cross-shear limit, its energy is:

    E² = E²_e(n₁,n₂) + E²_ν(n₃,n₄) + E²_p(n₅,n₆)

The lightest cross-plane mode involving the neutrino T² has
E ≥ √(m_e² + m_ν²) ≈ 511 keV — ten billion times heavier than
the neutrino.  Even with cross-shear, the mixing amplitude is
suppressed by (m_ν/m_e)² ~ 10⁻¹⁷.  Cross-plane modes cannot
create new light states.

Cross-plane modes are relevant for PMNS mixing (perturbative
coupling) and heavy sterile neutrinos (MeV–GeV), but not for
the three light mass eigenstates.

### F18. Track 1c conclusion — the mode menu is closed

No non-coprime mode or cross-plane mode provides a new spin-½
neutrino candidate.  The complete spin-½ fermion menu on the
neutrino T² is:

    (p, ±2)  with p odd,  for all p = ±1, ±3, ±5, ...

This was already fully explored in Track 1b.  The mode menu
cannot be expanded to solve the sterile neutrino problem.
Remaining paths: Tracks 1d–1f (revise the spin/charge formulas,
or rescue Assignment A).
