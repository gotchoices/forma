# R23 Findings

## Track 1: Near-degenerate triplet search

Script: `scripts/track1_triplet_search.py`

### Setup

On the sheared T² with aspect ratio r and shear s (fixed by α = 1/137),
the uncharged modes (|n₁| ≥ 2) have energies

    E(n₁,n₂) = √(n₁² + ((n₂ − n₁s)/r)²) / √(1 + ((2−s)/r)²)   [in m_e]

The neutrino Δm² ratio Δm²₃₁/Δm²₂₁ = 33.57 maps to the mode
energy-splitting ratio ΔE₃₁/ΔE₂₁ in the near-degenerate limit
(ΔE ≪ E, which holds since ΔE ~ eV while E ~ MeV).

The search builds the mode catalog up to E_max = 100 m_e, finds
near-degenerate pairs, and for each pair binary-searches for a
third mode at the target ratio distance.

### F1. Ratio 33.6 is trivially achieved at keV-scale splittings

At E_max = 100 m_e, the mode density is ~686 modes/m_e (one mode
per 745 eV).  At this density, for any pair of modes with ΔE < 5 keV,
there is ALWAYS a third mode whose distance gives ratio ≈ 33.57 to
4+ decimal places.  At r = 1.0, over 1.7 million such triplets exist.

This is true at EVERY r value scanned (0.5–15).  The ratio test is
not selective at keV-scale splittings because the mode density is
high enough to match ANY target ratio.

### F2. Test becomes non-trivial at sub-eV splittings

The physically relevant regime is where ΔE₂₁ is small enough that
the beat frequency corresponds to neutrino oscillations.  The pair
statistics at r = 1, E_max = 100 m_e:

| Threshold (eV) | Pairs  | Avg ΔE (eV) |
|:----------------|-------:|:-------------|
| 10,000          | 1.2M   | 5005         |
| 1,000           | 121k   | 497          |
| 100             | 12,653 | 48           |
| 10              | 1,308  | 5.3          |
| 1               | 85     | 0.53         |
| 0.1             | 7      | 0.04         |

At ΔE < 1 eV, only 85 pairs exist — sub-eV near-degeneracies are
rare Diophantine coincidences, not fine-tuning.

### F3. Best triplet matches by splitting scale (r = 1)

| Inner threshold | Best ratio | Miss (%) | ΔE₂₁ (eV) | Significance |
|:----------------|:-----------|:---------|:-----------|:-------------|
| < 1000 eV       | 33.5724    | 0.0000   | 620        | trivial      |
| < 100 eV        | 33.5729    | 0.0014   | 99         | 1.6 expected |
| < 10 eV         | 33.5882    | 0.047    | 5.5        | 0.30 exp     |
| < 1 eV          | 32.6433    | 2.77     | 0.82       | 0.17 exp     |

"Significance" is the expected number of random matches at least as
good, assuming a uniform random spectrum with the same mode density.
Values < 1 indicate the match is unlikely by chance.

The 10 eV threshold gives the best balance: a 0.047% match with 0.30
expected random matches (~1.2σ).  The sub-eV match is 2.77% off but
only has 85 pairs to work with.

### F4. Triplet quality vs r at 10 eV inner splitting

| r    | Pairs | Best ratio | Miss (%)  |
|:-----|------:|:-----------|:----------|
| 1.0  | 1,308 | 33.5882    | +0.047    |
| 1.5  |   855 | 33.6219    | +0.148    |
| 2.0  | 1,073 | 33.6592    | +0.259    |
| 2.5  | 1,051 | 33.5523    | −0.060    |
| 3.0  | 1,187 | 33.5852    | +0.038    |
| 5.0  | 2,076 | 33.5743    | +0.006    |
| 7.0  | 3,373 | 33.5767    | +0.013    |
| 10.0 | 6,945 | 33.5713    | −0.003   |

All r values produce matches within 0.3% of the target.  The match
quality improves with mode count (larger r → more modes → tighter
Diophantine approximations).  No specific r is singled out.

### F5. Sub-eV triplet quality vs r

| r    | Sub-eV pairs | Best ratio | Miss (%) |
|:-----|-------------:|:-----------|:---------|
| 1.0  |           85 | 32.64      | −2.77    |
| 2.5  |          213 | 36.13      | +7.61    |
| 4.0  |          366 | 36.73      | +9.41    |
| 5.0  |          237 | 34.14      | +1.69    |
| 7.0  |          298 | 32.59      | −2.92    |
| 10.0 |          753 | 33.82      | +0.75    |

At sub-eV scale, the best match is r = 10 (0.75% off, 753 pairs).
The statistics are too sparse for definitive conclusions — all
misses are within the range expected from limited sample size.

### F6. The ratio test alone does not fix r

The target ratio 33.57 is achievable at all r values at keV-scale
splittings.  At sub-eV scale, the match quality is dominated by
counting statistics (how many near-degenerate pairs exist), not by
geometry.  More modes (higher E_max) would improve all r values
roughly equally.

The ratio test does NOT falsify the beating model — good matches
exist.  But it does not uniquely determine r either, because the
match quality is limited by the number of available modes, not by
geometric incompatibility.

### F7. Path to a constraining test

Three approaches could make the ratio test definitive:

(a) **Higher E_max** (~500–1000 m_e): more modes → more sub-eV
    pairs → better statistics.  Computationally expensive but feasible.

(b) **Analytical Diophantine methods**: use continued fractions to
    find near-degeneracies analytically rather than by brute-force
    enumeration.  This bypasses the E_max limitation.

(c) **Joint constraint with phonon mass** (Track 2): the ratio test
    plus the absolute Δm² scale together provide two independent
    constraints on the geometry.  Even if the ratio alone doesn't
    fix r, the combination might.

---

## Track 2: Phonon coupling analysis

Script: `scripts/track2_phonon_coupling.py`

### Setup

The phonon model requires mode-mode coupling: a perturbation of
occupation numbers in the proton's harmonic condensate must propagate
as a collective excitation.  The coupling source is embedding
curvature — the metric ds² = a²dθ₁² + ρ(θ₁)²dθ₂² on the torus.

Track 2 asks: does this curvature provide the coupling needed for
a sub-eV phonon?

### F8. θ₂-momentum is conserved on the embedded torus

The embedded torus metric has NO θ₂ dependence (it depends only on
the poloidal angle θ₁).  Therefore:

- The Laplacian commutes with ∂/∂θ₂
- The θ₂-momentum p₂ is an exact quantum number
- Modes with different p₂ live in orthogonal subspaces
- Curvature cannot mix them — at ANY order of perturbation theory

This is exact, not a perturbative statement.  On the sheared T²,
the effective θ₂-momentum for mode (n₁, n₂) is p₂ = n₂.

### F9. Proton harmonics don't couple at fixed-background level

The proton's harmonics are (n, 2n) for n = 2, 3, 4, ...
These have n₂ = 4, 6, 8, ... — each a DIFFERENT value.  Since
curvature conserves n₂, these harmonics do NOT couple to each
other through embedding curvature.

No phonon can propagate through the harmonic spectrum at the
fixed-background level.  The phonon mechanism requires a coupling
source beyond embedding curvature.

### F10. Fixed-n₂ near-degeneracy is ~8 eV (not sub-eV)

If we restrict to modes with the SAME n₂ (where curvature coupling
exists), the tightest near-degeneracy at E_max = 100 m_e is:

    ΔE = 7.8 eV  at n₂ = 28:  modes (+5,28) and (+4,28)

Compare to the unfixed (any n₂) tightest pair from Track 1:
~0.001 eV.  The n₂ constraint removes a Diophantine degree of
freedom, making tight near-degeneracies ~10⁴× harder to find.

Moreover, the curvature coupling between adjacent Δn₁ = 1 modes
at fixed n₂ is V ~ ε × n₂² × E_mode, which at ε = 1 and n₂ = 28
gives V ~ 5 × 10⁹ eV — enormously larger than the level spacing.
These modes are STRONGLY mixed, not weakly perturbed.

### F11. Coupling desert

For a sub-eV phonon from modes at E ~ 50 m_e, the required
inter-harmonic coupling is ~10⁻⁹ × E_mode ≈ 0.025 eV.  The
available coupling mechanisms:

| Mechanism | Coupling (eV) | vs. required |
|:----------|:--------------|:-------------|
| Gravity (backreaction on spacetime) | 10⁻²⁴ | 10²³× too weak |
| EM 2nd-order (virtual photon) | model-dependent | uncertain |
| Proton backreaction on T² shape | unknown | requires R22 |

Gravity is negligible.  EM coupling between uncharged modes is
suppressed (no net charge → no direct photon coupling).  The
proton's backreaction on torus shape could break θ₂ symmetry,
but this requires the self-consistent calculation of R22.

### F12. The phonon model has a structural obstacle

The phonon-of-harmonics neutrino model is NOT viable at the
fixed-background level because:

1. θ₂ conservation prevents coupling between harmonics (F8, F9)
2. Modes that DO couple (same n₂) are not nearly degenerate (F10)
3. No known mechanism provides coupling at the required ~0.025 eV
   scale (F11)

The model could be rescued if the proton's backreaction on T²
breaks θ₂ symmetry (F13), but this is uncomputed.

### F13. Backreaction is the rescue path

The proton's energy is ~1836 m_e — far exceeding the geometric
stiffness scale.  The fixed-background approximation breaks down
entirely for the proton composite.  In a self-consistent calculation
(R22), the torus shape would deform in response to the harmonic
occupation, breaking θ₂ symmetry and potentially enabling
inter-harmonic coupling.

Whether this coupling has the right strength (~0.025 eV) is an
open question that depends on the details of R22.

### F14. Neutrino viability assessment

| Requirement | Phonon model | Moduli (shape) model |
|:------------|:-------------|:---------------------|
| Charge = 0 | ✓ automatic | ✓ automatic |
| Mass < 0.8 eV | ? (coupling unknown) | ? (stiffness unknown) |
| Three flavors | ? (ratio matches exist, F3) | ? (3 shape modes) |
| Spin ½ | ? (spin chain mechanism) | ✗ (spin 0 or 2) |
| Created in decay | ✓ occupation shift | ✓ geometry readjusts |
| Mode-mode coupling | ✗ θ₂ blocks it (F12) | N/A |

**Verdict:** The T² model does NOT yet have a viable neutrino.
The phonon model fails on coupling (F12); the moduli model
fails on spin.  The neutrino is the model's most serious open
problem.  Possible resolutions: proton backreaction (R22),
topological defects (neutrino.md Direction E), separate larger T²
(R20 option (a)), or physics beyond the T² framework.

### Summary table

| ID | Finding | Status |
|:---|:--------|:-------|
| F1 | Ratio trivially achieved at keV splittings | established |
| F2 | Test non-trivial only at sub-eV scale | established |
| F3 | Best <10 eV match: 33.59 (0.05% off, ~1.2σ) | established |
| F4 | Match quality improves with mode count, not r | established |
| F5 | Sub-eV best: r=10, ratio=33.82 (0.75% off) | established |
| F6 | Ratio alone does not fix r | established |
| F7 | Three paths to constraining test | identified |
| F8 | θ₂-momentum conserved on embedded torus | established |
| F9 | Proton harmonics don't couple (different n₂) | established |
| F10 | Fixed-n₂ near-degeneracy ~8 eV (not sub-eV) | established |
| F11 | Coupling desert between gravity and EM | established |
| F12 | Phonon model has structural obstacle (θ₂) | established |
| F13 | Backreaction (R22) is the rescue path | identified |
| F14 | T² model has no viable neutrino yet | established |

### Scripts

- `track1_triplet_search.py` — mode catalog, pair statistics,
  triplet search across r, scaling analysis
- `track2_phonon_coupling.py` — θ₂ conservation analysis,
  fixed-n₂ near-degeneracy, coupling estimates, viability
