# R52 Findings

**Study:** Anomalous magnetic moment from torus self-field
**Status:** Track 1 misguided, Track 2 negative result

Overall: 6 findings from 2 tracks.

---

## Track 1: Classical current-loop integral — MISGUIDED

Script: [`scripts/track1_bare_moment.py`](scripts/track1_bare_moment.py)

**Goal:** Verify that the 3D current-loop integral reproduces
the bare magnetic moments g = 2 (electron) and 3μ_N (proton).

**Result: MISGUIDED.** The bare moment is quantum (angular
momentum quantization L₂ = ℏn₂), not a classical field integral.
The current-loop integral gives a geometry-dependent answer
8–800× larger than the quantum prediction.


### F1. Classical current-loop integral does not give the bare moment

The analytical result for a charge Q traversing a (n₁, n₂) torus
knot is μ_classical/μ_quantum = (2R² + a²)/(2ƛ_C²), verified
numerically.  The ratio is 91× for the electron, 162× for the
proton at typical parameters.


### F2. The bare moment is topological

μ = eℏn₂/(2m) = n₂ × magneton depends only on winding number n₂
and charge-to-mass ratio.  Independent of r, R, a, s, ε.

---

## Track 2: B-field surface integral — NEGATIVE RESULT

Script: [`scripts/track2_bfield_distribution.py`](scripts/track2_bfield_distribution.py)

**Goal:** Adapt the R48 E-field charge integral to the B field.
See if the B-field distribution on the torus creates mode-dependent
corrections to the magnetic moment, with a sign that differs
between (1,2) and (1,3).

**Result: NEGATIVE.** The B-field integral, in both traveling-wave
and standing-wave formulations, gives corrections that are the
same sign for all modes.  The sign difference between the
electron and proton anomalous moments does not emerge from
this approach.


### F3. Traveling-wave B field has no +/− structure in the ring direction

For the CP traveling wave (R48 model) with n₁ = 1:

    B = (E₀/c)(k̂ × ρ̂)
    B_z = −n₂ρ / √(a² + n₂²ρ²)

B_z is constant in θ₂ and always negative.  There are no
positive/negative cancellation regions.  The Poynting angular
momentum integral ∫(x k̂_y − y k̂_x) dA gives a result that
increases with ε² for all modes — always additive.

The geometric correction is δμ/μ ≈ ε²(1 − 1/n₂²)/2, which is
positive for both n₂ = 2 (electron) and n₂ = 3 (proton).


### F4. Standing-wave B field has +/− regions but the integral is same-sign

The standing-wave component B_t = (E₀/c) sin(q_eff θ₂) directed
along k̂ has alternating positive and negative bands:
- (1,2): 4 bands (2 positive, 2 negative)
- (1,3): 6 bands (3 positive, 3 negative)

For integer q_eff, these cancel exactly (θ₂ orthogonality).
Shear (q_eff = n₂ − s ≠ integer) breaks the cancellation,
leaving a residual ∝ s²/n₂.

The residual is always positive for both modes.  At s = 0.01:

| Mode | δμ/μ (standing-wave correction) |
|------|--------------------------------|
| (1,2) | +2.19 × 10⁻⁴ |
| (1,3) | +1.66 × 10⁻⁴ |

The (1,3) correction is smaller than (1,2), consistent with
the 1/n₂ scaling of the shear residual.  But both are positive.


### F5. The standing-wave/traveling-wave ratio is independent of ε

The ratio of the standing-wave correction to the traveling-wave
moment is the same at all aspect ratios (0.1, 0.3, 0.5, 1.0).
This means the correction is a pure function of shear s, not
of the torus geometry.  The ε dependence cancels between
numerator and denominator.

This makes physical sense: the standing-wave correction comes
from the sin(q_eff θ₂) residual, which depends on s but is
multiplied by the same geometric factor as the bare moment.


### F6. The sign difference must come from elsewhere

The B-field surface integral technique — whether traveling-wave
or standing-wave, with or without shear — gives corrections
that are always additive (positive δμ) for all (1, n₂) modes.

Possible sources of the sign difference:
1. **Self-interaction:** the mode's Coulomb field distorts its
   own current pattern (Q103 defect-cost back-reaction).  This
   is a 3D S-space effect, not captured by the 2D field integral.
2. **Cross-sheet coupling:** interaction between Ma_e and Ma_ν
   (or Ma_p and Ma_ν) modifies the mode structure differently
   for single-phase and three-phase modes (R45 Track 3).
3. **Non-perturbative regime:** the proton's anomaly (−6.9%)
   is too large for a surface-integral correction — it may
   require a fundamentally different mechanism than the
   electron's (+0.12%).
