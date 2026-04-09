# R52 Findings

**Study:** Anomalous magnetic moment from torus self-field
**Status:** Closed — negative.  All five tracks (1, 2, 4a, 4b, 4c) fail to produce the three-phase sign rule at the proton's actual aspect ratio.

Overall: 11 findings from 5 tracks (1, 2, 4a, 4b, 4c).

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

---

## Track 4: Sign rule test (multiple sub-experiments)

**Goal:** Find any consistent set of assumptions under which the
self-interaction calculation reproduces the sign pattern: additive
(+) for n_ring = 2 (electron) and subtractive (−) for n_ring = 3
(proton).  Common assumptions: standing-wave basis ψ = cos(n_tube θ_tube)
× cos(n_ring θ_ring), 2*n_ring antinodes alternating ±, chord
distances through 3D, signed charge density (NOT |ψ|²).


### Sub-track 4a: Pairwise antinode Coulomb energy — NEGATIVE

Script: [`scripts/track4a_pairwise_coulomb.py`](scripts/track4a_pairwise_coulomb.py)

Treats each antinode as a point charge with sign s_k = (−1)^k and
sums pairwise Coulomb energies.  At all aspect ratios tested
(r ∈ [0.1, 20]):

| r | U(n=2) | U(n=3) | Same sign? |
|---|---|---|---|
| 0.5 | −1.219 | −2.691 | yes (−) |
| 2.0 | −0.609 | −1.345 | yes (−) |
| 8.906 | −0.185 | −0.407 | yes (−) |

The ratio U(n=2)/U(n=3) is exactly **0.4530** at every aspect
ratio — a constant determined purely by the angular geometry of
the antinodes (independent of R, a).  Both modes are dominated by
nearest-neighbor opposite-sign pairs, giving negative U.

The simplest pairwise picture **does not differentiate the modes**.


### F7. Pairwise antinode Coulomb gives same-sign for both modes

Both n_ring = 2 and n_ring = 3 give negative pairwise Coulomb
energy at all aspect ratios.  The closest neighbors are always
opposite-sign (alternating + −), so the pairwise sum is always
dominated by the negative contributions.  The ratio is constant
at U(n=2)/U(n=3) ≈ 0.453, reflecting the angular geometry but
giving no sign-flipping.


### Sub-track 4b: Coaxial tube-loop mutual inductance — NEGATIVE

Script: [`scripts/track4b_loop_inductance.py`](scripts/track4b_loop_inductance.py)

Treats each tube winding as a circular current loop in 3D and
computes the mutual inductance between loops via Neumann's formula.
At the proton aspect ratio (r = 8.906):

- n_ring = 2: off-diagonal M_ij sum = **−503.8**
- n_ring = 3: off-diagonal M_ij sum = **−371.2**

Both negative.  At small aspect ratios (r = 0.5), both are slightly
positive (+0.18 and +0.96).  The sign flip from positive to
negative happens at low r for both modes simultaneously — at no r
do the signs differ.


### F8. Loop mutual inductance also gives same-sign for both modes

The Neumann inductance integral between adjacent tube loops is
dominated by the wire segments that point in opposite directions
across the gap, producing a negative cross term.  This is true
for both n_ring = 2 and n_ring = 3 at all r > 0.5.  The
classical mutual-inductance picture cannot reproduce the sign rule.


### Sub-track 4c: Continuous standing-wave self-energy — NEGATIVE (with caveat)

Script: [`scripts/track4c_continuous_self_energy.py`](scripts/track4c_continuous_self_energy.py)

Treats ψ = cos(θ_tube) × cos(n_ring × θ_ring) as a real-valued
classical charge density (signed, NOT |ψ|²) and computes its
Coulomb self-energy by double integral over the embedded torus
surface.  Cell-cell distances use the 3D chord through space.

**Initial result was misleading.** A first scan with a coarse
16×32 grid appeared to show a sign flip near r ≈ 10 (just past
the proton's r_p ≈ 8.9), suggesting partial confirmation of the
sign rule.  Resolution convergence testing showed that this
"crossover near r_p" is a **discretization artifact**.  At
adequate resolution, both modes give positive self-energy at
the proton's aspect ratio.

**Resolution convergence at r = 8.906 (proton):**

| Grid | U(1,2) | U(1,3) | U2/U3 |
|------|--------|--------|-------|
| 16×32 | +9159 | +133 | 68.9 |
| 20×40 | +9687 | +674 | 14.4 |
| 24×48 | +10050 | +1019 | 9.9 |
| 32×64 | +10496 | +1453 | 7.2 |
| 40×80 | +10756 | +1720 | 6.3 |
| 48×96 | +10931 | +1896 | 5.8 |
| 64×128 | +11151 | +2115 | 5.3 |

As resolution increases, U(1,3) **grows** monotonically (from 133
toward ~3000+), and the ratio U2/U3 **decreases** but remains
positive throughout.  At no resolution does U(1,3) go negative
at the proton aspect ratio.

**Where the sign flip actually occurs:**

A high-resolution (32×64) scan at large aspect ratios shows the
crossover happens at r ≈ 25-30, far from the proton's r_p:

| r | U(1,2) | U(1,3) |
|---|--------|--------|
| 8.0 | +7431 | +1215 |
| 12.0 | +27155 | +2197 |
| 15.0 | +54875 | +2586 |
| 20.0 | +135005 | +1490 |
| 30.0 | +476826 | −15310 |
| 50.0 | +2334776 | −195719 |

The sign flip exists, but it happens at aspect ratios (r ≳ 25)
that are unphysical for the actual particle (r_p = 8.906).

**Conclusion:** the continuous signed-ψ self-energy does NOT
reproduce the sign rule at the proton's actual aspect ratio.
The three-phase hypothesis is not supported by this calculation.


### F9. Track 4c does not produce the sign rule at r_p (after resolution check)

Initial coarse-grid results suggested the sign rule emerged near
r_p, but this was a numerical artifact.  At converged resolution,
both (1,2) and (1,3) modes give positive U_self at r_p ≈ 8.9.
The crossover where U(1,3) goes negative does exist but occurs
at r ≈ 25-30, far from any physical aspect ratio for the proton.


### F10. The signed-ψ vs |ψ|² distinction does not save the result

Computing the same self-energy with the standard QM probability
density |ψ|² (always non-negative) gives:

| Mode | U_self (signed ψ) | U_self (|ψ|²) |
|------|-------------------|----------------|
| (1,2) at r_p | +10050 | +0.107 |
| (1,3) at r_p | +1019 | +0.094 |

With |ψ|², both modes give small positive values that are nearly
identical.  No sign flip ever occurs.  The signed-ψ interpretation
doesn't help either: it makes the magnitudes larger and produces
a very high sign-flip threshold (r ≈ 25-30) but does not give
the predicted sign pattern at any physical aspect ratio.


### F11. The three-phase hypothesis is not supported by classical field calculations

Combining all five computational tracks (1, 2, 4a, 4b, 4c):

| Track | Method | Differentiates n=2 vs n=3 by sign at r_p? |
|-------|--------|-------------------------------------------|
| 1 | Classical current loop | N/A (computes wrong quantity) |
| 2 | B-field surface integral | No |
| 4a | Pairwise antinode Coulomb | No |
| 4b | Loop mutual inductance | No |
| 4c | Continuous signed-ψ self-energy | No (sign flip exists but at r ≈ 25, not r_p ≈ 8.9) |

**No classical field calculation in this study reproduces the
three-phase sign rule at the proton's actual aspect ratio.**

The verbal three-phase argument is intuitive but does not survive
quantitative implementation.  The actual geometry of the
self-interaction on a torus does not produce the predicted
cancellation between three antinodes at 120° — at least not
at the proton's aspect ratio.

---

## Track 4 status

| Sub-track | Method | Result |
|-----------|--------|--------|
| 4a | Pairwise Coulomb (point antinodes) | Same-sign for both modes at all r |
| 4b | Loop mutual inductance | Same-sign for both modes at all r |
| 4c | Continuous self-energy (signed ψ) | Same-sign at r_p; sign flip exists but at r ≈ 25 |
| 4d | Vector potential back-reaction | Not run; would be more complex but is unlikely to differ qualitatively given that 4a-c all fail |

The three-phase sign rule, as a CLASSICAL self-interaction
phenomenon on a torus, is **not supported** by these
calculations.  The sign rule may still hold under some other
mechanism (genuine quantum lattice back-reaction, cross-sheet
coupling, or a non-classical effect), but the simple classical
versions tested here do not reproduce it at the proton aspect
ratio.

R52 should be **closed as negative**: the central hypothesis
(self-field back-reaction explains the sign of the residual
moment correction) is not supported by classical field
calculations on the embedded torus.  The study has produced
useful clarifications (Track 1: bare moment is topological;
Tracks 2, 4a-c: classical self-interaction does not differentiate
mode topology by sign), but it does not establish what was
hoped.

The three-phase sign rule remains an interesting verbal
argument, but it has not been demonstrated computationally and
should not be cited as an established MaSt prediction unless
a different (non-classical) approach succeeds.
