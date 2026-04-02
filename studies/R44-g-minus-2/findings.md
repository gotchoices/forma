# R44 Findings: Anomalous magnetic moment from torus geometry

## F1: Charge density verified (Track 1)

The R19 shear-charge formula gives a surface charge density on the
embedded torus:

σ(θ₁, θ₂) = ε₀ E₀ cos(θ₁ + q_eff θ₂)

where θ₁ is the physical tube angle, θ₂ is the ring angle, and
q_eff = 2 − s.  Numerical integration on a 500×500 grid confirms
∫σ dA = −e to better than 1% for all tested aspect ratios.

| r    | s        | q_eff    | Q_num / e  |
|------|----------|----------|------------|
| 1.00 | 0.165128 | 1.834872 | −0.993374  |
| 2.00 | 0.084941 | 1.915059 | −0.996662  |
| 4.00 | 0.052641 | 1.947359 | −0.997908  |
| 8.00 | 0.035395 | 1.964605 | −0.998571  |

No solution exists for r < r_crit ≈ 0.75 (consistent with R19).

## F2: Charge is an oscillating pattern, not a perturbation

The charge density σ is NOT a small perturbation on a uniform
background.  It is a full cos() wave that oscillates between large
positive and large negative values.  The net charge −e is the small
residual of massive cancellations:

| r    | Positive contribution | Negative contribution | Net     |
|------|-----------------------|-----------------------|---------|
| 1.00 | +0.236 e              | −1.230 e              | −0.993 e|
| 2.00 | +0.027 e              | −1.023 e              | −0.997 e|
| 3.00 | +0.009 e              | −1.006 e              | −0.997 e|

For r ≳ 2, the positive contribution is tiny — nearly all the
charge surface is negative, with the magnitude peaking at the outer
equator (θ₁ ≈ 0, where ρ = R + a is largest) and the small positive
patch sitting at the inner equator (θ₁ ≈ π, where ρ = R − a).

## F3: Negative charge concentrates at large radius

The θ₂ integral of σ gives an effective charge per unit tube angle
proportional to cos(θ₁ − πs) × ρ.  For the small shear values on
the α-curve (s ≈ 0.04–0.17), the negative charge peak sits near
θ₁ ≈ 0 (outer equator, ρ = R + a) and the positive peak near
θ₁ ≈ π (inner equator, ρ = R − a).

This means negative charge is concentrated where ρ is large, while
the sparse positive charge sits where ρ is small.

## F4: Magnetic moment has the wrong sign and wrong magnitude — order-1 effect

The magnetic dipole moment from the actual charge distribution was
compared against the moment from a uniform (positive) charge equal
to |Q| = e spread over the torus surface:

<!-- μ_actual = (c/2) ∫∫ σ_actual × 2ρ²/|v| × dA -->
$$
\mu_\text{actual} = \frac{c}{2}\iint \sigma_\text{actual}
\;\frac{2\rho^2}{|v|}\;dA
$$

| r    | μ_actual (A·m²) | μ_uniform (A·m²) | ratio    | ratio − 1 |
|------|-----------------|-------------------|----------|-----------|
| 1.00 | −7.27 × 10⁻²⁴  | +5.29 × 10⁻²⁴    | −1.375   | −2.375    |
| 2.00 | −6.22 × 10⁻²⁴  | +7.30 × 10⁻²⁴    | −0.852   | −1.852    |
| 4.00 | −6.08 × 10⁻²⁴  | +9.05 × 10⁻²⁴    | −0.672   | −1.672    |
| 8.00 | −6.23 × 10⁻²⁴  | +9.95 × 10⁻²⁴    | −0.626   | −1.626    |

The "correction" ratio − 1 is of order **−1.6 to −2.4**, roughly
**1400–2045 times α/(2π)**, and has the **wrong sign**.

## F5: Why the mechanism fails — the oscillating pattern is not a perturbation

The charge-mass separation hypothesis assumed that charge and mass
are "slightly" displaced, producing a small correction to the moment.
The actual situation is qualitatively different:

1. **The charge density oscillates** through zero.  It is not "charge =
   uniform + small correction."  It is "charge = large oscillating
   pattern whose integral barely survives."

2. **The negative charge dominates at large ρ.**  Since the moment
   integral weights by ρ², the negative contribution overwhelms the
   positive.  The actual moment is negative while the uniform moment
   is positive — the ratio is not 1 + ε but −0.6 to −1.4.

3. **The effect is geometric, not perturbative.**  The cos(θ₁ + q_eff θ₂)
   pattern correlates with ρ = R + a cos θ₁ at order 1, not order α.
   No choice of r can make this correction small.

This is a fundamental mismatch: the anomalous magnetic moment a_e ≈
α/(2π) ≈ 0.00116 is a 0.1% correction.  The charge-mass separation
from shear is a 100–200% effect with the wrong sign.

## F6: Remaining tracks are dead as framed

**Track 2 (g(r) from charge-weighted vs energy-weighted moment):**
Dead.  Track 1 already computed the charge-weighted moment.  The
order-1 magnitude and wrong sign make it impossible for the ratio
μ/L to give g ≈ 2.002 by this mechanism.  Any further refinement
of the energy-weighted L_z integral cannot rescue a factor-of-2
discrepancy.

**Track 3 (3D embedding curvature correction):**
Dead.  This was designed as a perturbative correction to Track 2's
result (matching the second-order QED term (α/π)²).  With the
base mechanism giving corrections of order 1, a perturbative
embedding correction is irrelevant.

**Track 4 (shear scan to pin r_e):**
Dead.  There is no value of r on the α-curve where the charge-mass
mechanism produces g − 2 ≈ α/(2π).  The correction monotonically
decreases from −2.4 (r = 1) toward −1.6 (r → ∞), never passing
through +0.001.

## F7: What this rules out (and what it does not)

**Ruled out:** The claim that the R19 shear-induced charge
distribution, treated as a classical surface current on the
embedded torus, produces the anomalous magnetic moment.

**Not ruled out:**
- The topological g = 2 (R8 F9) remains valid — it does not depend
  on the classical current-loop picture.
- The anomalous moment might arise from the **energy partition**
  between the confined mode (fraction 1 − α of total energy) and
  the external Coulomb field (fraction α).  This is closer to the
  WvM "field fraction" idea, but requires computing the angular
  momentum carried by the external 1/r² field — a different
  calculation from what R44 attempted.
- It might also arise from radiative corrections within MaSt's own
  framework (the analog of virtual photon loops in QED), which
  would require a perturbative field-theory calculation on the
  torus background.

## F8: Positive by-products

Despite the negative result for g − 2, the computation confirmed
several useful facts:

1. The R19 charge formula is numerically robust: ∫σ dA = −e holds
   across the full α-curve (F1).
2. The charge distribution is predominantly negative, concentrated
   at the outer equator, with a small positive patch at the inner
   equator (F2, F3).
3. The classical magnetic moment of the R19 charge distribution is
   well-defined and computable, even though it does not produce the
   anomalous moment (F4).
4. Any future attempt at g − 2 in MaSt must use a mechanism that
   produces an order-α correction, not an order-1 restructuring of
   the current pattern.
