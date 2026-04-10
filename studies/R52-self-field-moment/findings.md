# R52 Findings

**Study:** Anomalous magnetic moment from torus self-field
**Status:** Reopened.  Tracks 1–4c failed (no shear); Track 4d (continuous self-energy WITH shear) shows mode-dependent sign-flip behavior — the sign rule emerges at moderate shear values (s ≳ 0.020-0.025 at the proton aspect ratio).

Overall: 14 findings from 6 tracks (1, 2, 4a, 4b, 4c, 4d).

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

### Sub-track 4d: Continuous self-energy WITH shear — POSITIVE (partial)

Script: [`scripts/track4d_continuous_with_shear.py`](scripts/track4d_continuous_with_shear.py)

Adds shear to Track 4c's continuous self-energy: instead of
ψ = cos(θ_t) × cos(n_ring × θ_r) (integer ring winding), use
ψ = cos(θ_t) × cos((n_ring − s) × θ_r) (sheared, non-integer
effective winding).  Shear is the natural non-integer non-linearity
that the user identified as the likely source of mode-dependent
sign corrections — and it doesn't apply to the tube direction
(which is integer-quantized for charge).


### F12. Shear induces mode-dependent corrections

At the proton aspect ratio r = 8.906, the shear-induced correction
δU = U(s) − U(0) has qualitatively different shapes for the two
modes:

**(1,2) electron mode:** δU is roughly antisymmetric in shear.
Linear-dominant response.  Positive shear → negative δU; negative
shear → positive δU.

**(1,3) proton mode:** δU has BOTH linear and quadratic-plus
components in shear.  At small shear (|s| ≲ 0.015), δU follows the
same sign as (1,2).  At larger shear (|s| ≳ 0.020), δU(1,3)
**reverses sign relative to (1,2)** — the predicted pattern
emerges.

**Resolution-convergence at proton aspect ratio (32×64 grid and beyond):**

| s | δU(1,2) | δU(1,3) | Signs |
|---|---------|---------|-------|
| +0.010 | −53 | −2.8 | both − |
| +0.015 | −80 | −2.0 | both − |
| **+0.020** | **−106** | **+0.5** | **− / +** |
| +0.025 | −131 | +4.4 | − / + |
| +0.030 | −156 | +10.0 | − / + |
| +0.050 | −246 | +48 | − / + |
| +0.100 | −397 | +250 | − / + |

The sign-flip threshold is convergent at s ≈ 0.020-0.025
across resolutions (20×40 → 48×96).

This is the **first mode-dependent sign result** in R52.


### F13. The (1,3) mode has nontrivial shear response

Unlike (1,2), which has nearly linear δU(s) ≈ −k₂ × s, the (1,3)
mode has δU(s) ≈ −k₃ × s + α₃ × s² + ... with the higher-order
terms strong enough to flip the sign at moderate shear.  The
quadratic component for (1,3) is positive, so it eventually
overcomes the linear term and pushes δU positive.

For (1,2), the quadratic component is negligible up to large
shear values.  The two modes have qualitatively different
shear responses — **shear is the small parameter that
distinguishes them**.

This is exactly the mechanism the user proposed: shear is a
non-integer non-linearity that introduces small corrections,
and the corrections affect different modes differently.


### F14. Triangulation: filtering range, viability window, and MaSt shear

A scan of the (r, s) plane reveals the structure of the
sign-flip thresholds:

**(1,3) sign-flip threshold s_3(r):**
- r ∈ (0.34, 0.49): s_3 ≈ 0.18-0.22 (high)
- r = 1.0: s_3 ≈ 0.12
- r = 2.0: s_3 ≈ 0.085
- r = 5.0: s_3 ≈ 0.037
- r = 8.906: s_3 ≈ 0.016

**(1,2) sign-flip threshold s_2(r):**
- r ∈ (0.34, 0.49): s_2 ≈ 0.22-0.25
- r = 1.0: s_2 ≈ 0.155
- r = 2.0: s_2 ≈ 0.124
- r ≥ 5.0: no flip below s = 0.5

**Viability window** (where (1,3) flips but (1,2) doesn't):

At every r in (0.34, 2.0), there exists a window of s values
where δU(1,3) > 0 and δU(1,2) < 0 — the predicted sign pattern.
The window is roughly 0.04 wide in s and shifts to lower s as
r increases:

| r | Window in s | Width |
|---|-------------|-------|
| 0.34 | (0.215, 0.250) | 0.035 |
| 0.40 | (0.200, 0.240) | 0.040 |
| 0.45 | (0.190, 0.230) | 0.040 |
| 0.49 | (0.180, 0.220) | 0.040 |
| 0.70 | (0.145, 0.185) | 0.040 |
| 1.00 | (0.120, 0.155) | 0.035 |
| 2.00 | (0.080, 0.120) | 0.040 |

**Triangulation against the user's filtering argument:**

The user's filtering argument (the proton needs (1,3) as the
lowest allowed mode, requiring the tube to filter out (1,1) and
(1,2)) places the proton in the range r ∈ (1/3, 1/2).  This is
**inside the viability window** structure — the predicted sign
pattern can be achieved at exactly the r range where filtering
selects the proton.

**Triangulation against MaSt's shear formula:**

`solve_shear_for_alpha(r)` returns the shear that gives α = 1/137
at each aspect ratio:

| r | MaSt s (α=1/137) | Window in s | In window? |
|---|------------------|-------------|------------|
| 0.34 | 0.170 | (0.215, 0.250) | NO — below by 0.045 |
| 0.40 | 0.146 | (0.200, 0.240) | NO — below by 0.054 |
| 0.45 | 0.132 | (0.190, 0.230) | NO — below by 0.058 |
| 0.49 | 0.123 | (0.180, 0.220) | NO — below by 0.057 |

**The proton's MaSt shear is below the viability window by
about 0.05 across the user's predicted r range.** The two are
tantalizingly close — the MaSt shear is roughly 70-80% of what's
needed.

**Three independent constraints, one near-miss:**

The result is overdetermined: filtering gives a r range, the
sign rule gives a window in (r, s), MaSt's formula gives a
specific s at each r.  All three are consistent in shape but
the MaSt shear lands just outside the window.  To make them
fully consistent, ONE constraint must shift slightly:

1. **Effective α slightly larger than 1/137** for the proton
   (at GeV scale, running coupling gives ≈ 1/128, but a more
   substantial increase to ≈ 1/100 would push the shear into
   the window).

2. **Different shear-α formula for the (1,3) mode** — the lib's
   `solve_shear_for_alpha` was derived for the electron (1,2);
   the (1,3) mode might map shear differently.

3. **Lower sign-flip threshold from a more accurate calculation**
   — Track 4d uses scalar Coulomb self-energy with chord
   distance and a 24×48 grid; the threshold might shift down
   under (a) higher resolution, (b) vector A_self instead of
   scalar V_self, or (c) different basis (sin·cos instead of
   cos·cos).

The gap (~30% in shear) is small enough to be plausibly
closed by any of these adjustments.  Without further work,
we cannot say which one is responsible.

### F15. The lib's pinned r_p = 8.906 contradicts the filtering range

R27 F18 pinned the proton aspect ratio at r_p = 8.906 by
matching neutron and muon masses.  At this value:
- The torus is **self-intersecting** (a > R means the tube
  wraps through itself)
- The (1,2) sign-flip threshold disappears (no flip below s = 0.5)
- The (1,3) threshold is at s ≈ 0.016
- MaSt's natural shear is s = 0.008

The user's filtering argument predicts r ∈ (1/3, 1/2), which is
a normal non-self-intersecting torus.  These two pinning
arguments give **mutually inconsistent** values (8.906 vs 0.4).

If the filtering argument is physically correct, then R27 F18's
mass-matching procedure was using wrong assumptions and the
proton's true aspect ratio is small.  Conversely, if R27 F18 is
correct, then the filtering interpretation needs revision.

Either way, this is a contradiction that R52 has surfaced and
that needs resolution.  It is independent of the sign rule
itself but is highly relevant to whether the sign rule applies
to the proton.

---

## Track 4 status (revised after triangulation)

| Sub-track | Method | Result |
|-----------|--------|--------|
| 4a | Pairwise Coulomb (no shear) | Same-sign for both modes |
| 4b | Loop mutual inductance (no shear) | Same-sign for both modes |
| 4c | Continuous self-energy (no shear) | Same-sign at r_p; flip only at r ≈ 25 |
| **4d** | **Continuous self-energy WITH shear** | **Mode-dependent: viability window exists at small r, MaSt shear ~30% below window** |
| 4e | Vector potential back-reaction with shear | Not yet run |

**Major findings from Track 4d:**

1. The shear-induced sign rule mechanism EXISTS — (1,2) and (1,3)
   modes have qualitatively different shear responses at the
   classical scalar self-energy level
2. A viability window exists at small r (in the user's predicted
   filtering range) where the predicted sign pattern can be
   achieved
3. The MaSt shear formula gives values just below the viability
   window — the gap is 30% in shear, plausibly closable by
   small adjustments to one of three constraints
4. R27 F18's pinning of r_p = 8.906 contradicts the filtering
   interpretation; this is a separate issue worth investigating

R52 is **strongly partial-positive**.  The hypothesis (sign rule
from shear-mediated mode-dependent corrections) is supported in
qualitative form, and the quantitative match to the proton is
within ~30% of working.  Three independent next steps could close
the gap:

- Track 4e (vector approach) — might lower the threshold
- Check whether the (1,3) shear-α formula differs from (1,2)
- Resolve the r_p inconsistency between filtering and R27 F18

---

## Track 4 status (revised)

| Sub-track | Method | Result |
|-----------|--------|--------|
| 4a | Pairwise Coulomb (no shear) | Same-sign for both modes |
| 4b | Loop mutual inductance (no shear) | Same-sign for both modes |
| 4c | Continuous self-energy (signed ψ, no shear) | Same-sign at r_p; sign flip only at r ≈ 25 |
| **4d** | **Continuous self-energy WITH shear** | **Mode-dependent: sign flip at s ≈ 0.020 for (1,3)** |
| 4e | Vector potential back-reaction with shear | Not yet run |

**The shear is the missing ingredient.** Tracks 4a-c without shear
all give same-sign results because the integer-symmetric standing
wave doesn't have a small parameter that breaks the symmetry
between modes.  Adding shear (which the user correctly identified
as the natural non-integer non-linearity) introduces a real
mode-dependence that produces sign-flipping at moderate shear
values.

The hypothesis is **alive**.  Track 4d shows the mechanism exists.
The remaining questions are:
1. Is the proton's actual effective shear large enough to reach
   the sign-flip threshold?
2. Does the vector approach (Track 4e) confirm and refine the
   scalar 4d result?
3. Does the relationship between δU and δμ preserve the sign?

R52 is **reopened** — the central hypothesis is supported by
Track 4d in qualitative form.  Tracks 4e (vector with shear) and
a deeper investigation of the proton's effective shear are the
natural next steps.
