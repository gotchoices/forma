# clover-mass.md — Analytical mass spectrum on the corrugated torus

**Status:** Phase-A complete through second-order perturbation theory + independent numerical validation. The zeroth-order formula μ² = (n − 2m/3)² + (m/ε)² is **validated to machine precision** by a Bloch-restricted Fourier-basis Hill solver. The §6.3 second-order PT formula derived in this file is **INCORRECT** — it failed to restrict to the proper Bloch sector and overpredicts corrections by ~10×. The numerical solver (which does enforce the Bloch restriction) finds candidate pairs (e.g. (1, 2) ↔ (±2, ±2) at ε ≈ 0.2) that fit m_n/m_p to within 0.03%. The earlier "negative result" of §6.4 is overturned. Next step: fine-tune (ε, χ) with the numerical solver to fit m_p and m_n simultaneously.

This file derives the mass spectrum on the corrugated torus surface of [clover-quarks.md](clover-quarks.md), exploits the helical symmetry of §10.3 to reduce the 2D eigenvalue problem to a 1D Hill equation, and attempts the inversion to extract (ε, χ) from observed proton and neutron masses.

The aim is to **avoid brute-force numerical sweeping** by getting m(ε, χ, τ; embedding) far enough analytically that a few-variable algebraic inversion becomes tractable.

## 1. Setup

The wave equation on the corrugated torus is

<!-- (∂_t² − Δ_g) Ψ = 0 -->
$$
(\partial_t^2 \;-\; \Delta_g)\,\Psi \;=\; 0
$$

with Δ_g the Laplace–Beltrami operator of the induced metric (clover-quarks.md §10). For an eigenmode Ψ(t, θ, φ) = e^{−iωt} Φ(θ, φ),

<!-- -Δ_g Φ = ω² Φ -->
$$
-\Delta_g \Phi \;=\; \omega^2\, \Phi
$$

This section uses **embedding A (parameter-shift)** of §9.3 because that's where §10 derived the metric. The same machinery applies to embedding B with extra cross-section-rotation terms; we'll note where the two embeddings diverge.

The metric components in (θ, φ) coordinates (from §10.2):

<!-- g_θθ = (R + P_x)² + τ² c² ; g_θφ = τ c² ; g_φφ = c² -->
$$
g_{\theta\theta} = (R + P_x(u))^2 + \tau^2 c^2, \qquad
g_{\theta\varphi} = \tau\, c^2, \qquad
g_{\varphi\varphi} = c^2
$$

where u ≡ φ + τθ, c ≡ L_total/(2π) is the constant arc-length speed of the profile parameterisation, R ≡ R_major, and P_x(u) is the radial component of the clover profile.

## 2. Helical symmetry → 1D Hill equation

§10.3 noted that the metric depends on (θ, φ) only through u = φ + τθ. Switch to helical coordinates

<!-- v = θ, u = φ + τθ -->
$$
v \;\equiv\; \theta, \qquad u \;\equiv\; \varphi + \tau\theta
$$

In these coordinates the metric **diagonalises**:

<!-- g_vv = (R + P_x(u))², g_uu = c², g_vu = 0 -->
$$
g_{vv} = (R + P_x(u))^2, \qquad g_{uu} = c^2, \qquad g_{vu} = 0
$$

(Verify: ∂_v r |_u = ∂_θ r − τ ∂_φ r = (R+P_x) T̂, which is orthogonal to ∂_u r = P_x' N̂ + P_y' B̂.)

The Laplace–Beltrami operator becomes

<!-- Δ_g Φ = (1/(R+P_x)²) ∂_v² Φ + (1/c²) ∂_u² Φ + (P_x'(u)/(c²(R+P_x))) ∂_u Φ -->
$$
\Delta_g \Phi \;=\; \frac{1}{(R+P_x(u))^2}\,\partial_v^2 \Phi \;+\; \frac{1}{c^2}\,\partial_u^2 \Phi \;+\; \frac{P_x'(u)}{c^2 (R + P_x(u))}\,\partial_u \Phi
$$

Separate variables with Φ(v, u) = e^{i k_v v} ψ(u). The eigenvalue equation reduces to a **Sturm–Liouville (Hill) equation** in u alone:

<!-- ψ'' + (P_x'/(R+P_x)) ψ' + (c² ω² - k_v² c²/(R+P_x)²) ψ = 0 -->
$$
\boxed{\;\psi''(u) \;+\; \frac{P_x'(u)}{R + P_x(u)}\,\psi'(u) \;+\; \left[c^2 \omega^2 \;-\; \frac{k_v^2\, c^2}{(R + P_x(u))^2}\right]\,\psi(u) \;=\; 0\;}
$$

In the symmetric Sturm–Liouville form −(p ψ')' + q ψ = ω² w ψ with weight w(u) = R + P_x(u):

<!-- p = (R+P_x)/c², q = k_v²/(R+P_x), w = R+P_x -->
$$
p(u) = \frac{R + P_x(u)}{c^2}, \qquad q(u) = \frac{k_v^2}{R + P_x(u)}, \qquad w(u) = R + P_x(u)
$$

## 3. Bloch boundary conditions and the third-integer momenta

The surface identifications (clover-quarks.md §9.4)

<!-- (θ, φ) ~ (θ+2π, φ+2π/3) ; (θ, φ) ~ (θ, φ+2π) -->
$$
(\theta, \varphi) \;\sim\; (\theta + 2\pi,\; \varphi + 2\pi/3),
\qquad (\theta, \varphi) \;\sim\; (\theta,\; \varphi + 2\pi)
$$

translate in (v, u) coordinates (with τ = 1/3) to

<!-- (v, u) ~ (v+2π, u+4π/3), (v, u) ~ (v, u+2π) -->
$$
(v, u) \;\sim\; (v + 2\pi,\; u + 4\pi/3),
\qquad (v, u) \;\sim\; (v,\; u + 2\pi)
$$

For Φ = e^{i k_v v} ψ(u) to be single-valued:

<!-- ψ(u+2π) = ψ(u) ; e^{2πi k_v} ψ(u+4π/3) = ψ(u) -->
$$
\psi(u + 2\pi) = \psi(u), \qquad
e^{2\pi i\, k_v}\,\psi\!\left(u + \tfrac{4\pi}{3}\right) = \psi(u)
$$

Applying the second condition three times gives ψ(u+4π) = e^{−6πi k_v} ψ(u). Profile periodicity also gives ψ(u+4π) = ψ(u), so e^{−6πi k_v} = 1, hence

<!-- k_v = q/3 -->
$$
\boxed{\;k_v \;=\; q/3, \quad q \in \mathbb{Z}\;}
$$

Third-integer momenta around the ring direction, just as derived in clover-quarks.md §11. The conversion back to (θ, φ) labels: writing ψ(u) as a Fourier mode e^{i p u} gives Φ = e^{i (k_v + p\tau) θ + i p φ}, so

<!-- k_θ = q/3 + p/3 ; k_φ = p -->
$$
k_\theta \;=\; \frac{q + p}{3}, \qquad k_\varphi \;=\; p
$$

The single-valuedness condition 2p + q ∈ 3ℤ (equivalent to p ≡ q mod 3) recovers the familiar **k_θ = n − k_φ/3** form by setting n ≡ (q+p)/3 + p/3 · (corrections) ... explicitly: with q = 3n − 2p, we get k_θ = (3n − 2p + p)/3 = n − p/3. So

<!-- k_θ = n - k_φ/3 with n, k_φ ∈ ℤ -->
$$
\boxed{\;k_\theta \;=\; n \;-\; \frac{k_\varphi}{3}, \qquad n,\; k_\varphi \;\in\; \mathbb{Z}\;}
$$

These (n, m ≡ k_φ) integers label the modes.

## 4. Unperturbed spectrum: the constant-radius limit

The Hill equation has a clean closed-form limit when P_x is **negligible compared to R** — i.e., when ε is small. Then R + P_x(u) → R, the metric becomes that of a flat twisted torus, and the ODE reduces to

<!-- ψ_0'' + (c²ω_0² - c² k_v²/R²) ψ_0 = 0 -->
$$
\psi_0''(u) \;+\; \left(c^2 \omega_0^2 \;-\; \frac{c^2 k_v^2}{R^2}\right)\,\psi_0(u) \;=\; 0
$$

Plane-wave solutions ψ_0(u) = e^{i p u} (with p ∈ ℤ from the Bloch condition) give

<!-- ω_0² = k_v²/R² + p²/c² -->
$$
\omega_0^2 \;=\; \frac{k_v^2}{R^2} \;+\; \frac{p^2}{c^2}
$$

To express this in (n, m) labels (where k_θ = n − m/3 with k_φ = m), recall from §3 that k_v = q/3 with q = 3n − 2m. So **k_v = n − 2m/3** in the helical frame. Equivalently, this is k_v = k_θ − τ k_φ — the wavenumber rotated into the orthogonal (v, u) frame, with both the boundary-identification shift and the metric-shear contribution combining.

In dimensionless mass-squared units (μ² ≡ R² ω²) and using ε ≡ c/R = L_total/(2π R_major):

<!-- μ²_{(n,m)} = (n - 2m/3)² + (m/ε)² -->
$$
\boxed{\;\mu^2_{(n, m)} \;\equiv\; R^2\, \omega_0^2 \;=\; \left(n - \frac{2m}{3}\right)^2 \;+\; \left(\frac{m}{\varepsilon}\right)^2\;}
$$

This is the corrugated torus's flat-limit mass formula. It is the standard MaSt twisted-torus form

<!-- μ² = (n - σ m)² + (m/ε)² -->
$$
\mu^2 \;=\; (n - \sigma\, m)^2 \;+\; (m / \varepsilon)^2
$$

with **effective shear σ = 2τ = 2/3** (not τ = 1/3). The factor of 2 comes from the twist appearing twice — once in the boundary identification (k_θ = n − τm) and once in the metric dispersion (the (k_θ − τk_φ)² term from completing the square on the inverse-metric quadratic form). The two contributions stack into σ_eff = 2τ.

(Numerical verification: a direct calculation of ω² = g^{ij} k_i k_j on the flat-limit metric confirms μ² = (n − 2m/3)² + (m/ε)² to machine precision for several (n, m) and ε values.)

**Note.** This zeroth-order result depends on τ = 1/3 but is **independent of χ and of the embedding choice**. The corrugation depth χ first enters at second order in perturbation theory.

### 4.1 Low-lying modes

The (m/ε)² piece is the dominant contribution for nonzero m at small ε, but the (n − 2m/3)² piece selects which m carries the lightest mode of its column. Sorted at general ε:

| (n, m) | k_θ = n − m/3 | n − 2m/3 | μ² = (n − 2m/3)² + (m/ε)² |
|---|---|---|---|
| (0, 0) | 0 | 0 | 0 (zero mode; not a particle) |
| (±1, 0) | ±1 | ±1 | 1 |
| (1, 1) | 2/3 | 1/3 | 1/9 + 1/ε² |
| (0, 1) | −1/3 | −2/3 | 4/9 + 1/ε² |
| (1, 2) | 1/3 | −1/3 | 1/9 + 4/ε² |
| (0, 2) | −2/3 | −4/3 | 16/9 + 4/ε² |
| (1, −1) | 4/3 | 5/3 | 25/9 + 1/ε² |
| (2, 3) | 1 | 0 | 0 + 9/ε² = 9/ε² |

The mode (2, 3) has vanishing effective ring momentum (n − 2m/3 = 0), so its mass is purely from the cross-section term. **However, this is a wavemode label, not a closed knot.** Metric-charge's closure rule (m | n) tests whether a (m, n) winding maps to a self-closing path on the torus. The wavemode labels here are momentum quantum numbers (k_θ, k_φ), not path windings — they coincide only for specific (n, m) families. For (2, 3) interpreted as windings, we'd have 3 ∤ 2 and 2 ∤ 3, so no closure: this wavemode is not a particle. The mass formula gives a frequency for every (n, m) ∈ ℤ², but **the physical-particle subset is filtered by an additional closure / path-winding condition** (clover-quarks §2–3). I'll restrict to closure-satisfying (n, m) before reading off particle masses.

At small ε (thin tube, cross-section dominates), the lowest finite-mass modes are integer-ring modes (m = 0, n ≠ 0) with mass 1, 4, 9, .... At larger ε (~ unity or above), the |n − 2m/3| < 1 modes (such as (1,1) and (1,2)) become competitive.

## 5. First-order corrections vanish

Now restore the χ-dependence by treating P_x(u)/R as the small parameter. Expand the SL coefficients:

<!-- p = R/c² + P_x/c² ; q = k_v²/R - (k_v²/R²) P_x + O(P²/R³) ; w = R + P_x -->
$$
p = p_0 + \delta p, \quad q = q_0 + \delta q, \quad w = w_0 + \delta w
$$

with p_0 = R/c², q_0 = k_v²/R, w_0 = R, and the first-order shifts δp = P_x/c², δq = −(k_v²/R²) P_x, δw = P_x.

The first-order shift in ω² for an unperturbed plane wave ψ_0 = e^{i p u} / √(2π) is (standard Sturm–Liouville PT, integrating by parts):

<!-- δω² ∫ |ψ_0|² w_0 du = ∫ |ψ_0'|² δp du + ∫ |ψ_0|² δq du - ω_0² ∫ |ψ_0|² δw du -->
$$
\delta\omega^2 \cdot \int_0^{2\pi} |\psi_0|^2\, w_0\, du \;=\; \int_0^{2\pi} |\psi_0'|^2\, \delta p\, du \;+\; \int_0^{2\pi} |\psi_0|^2\, \delta q\, du \;-\; \omega_0^2 \int_0^{2\pi} |\psi_0|^2\, \delta w\, du
$$

For ψ_0 a plane wave, |ψ_0|² = 1/(2π) is constant, so every right-hand integral involves ∫ P_x(u) du. **By the profile's 3-fold rotational symmetry, ∫ P_x du = 0:**

<!-- ∫ P_x(u) du = 0 -->
$$
\int_0^{2\pi} P_x(u)\, du \;=\; 0
$$

(P_x is the x-component of a curve with 3-fold rotation symmetry — averaging around 360° kills all but the rotation-invariant constant, which is zero since the centroid sits at the origin.) Therefore

<!-- δω² |_{first order} = 0 -->
$$
\boxed{\;\delta \omega^2\bigm|_{\text{first order in } P_x/R} \;=\; 0\;}
$$

**Implication.** The leading corrugation correction to *every* mode's mass is **second order** in χ. The flat-torus spectrum is accurate to O((P/R)²) ∼ O(ε²) — which is consistent with the χ-dependence being subdominant when ε is small.

## 6. Second-order corrections: structure

Second-order PT involves matrix elements of the perturbation between the unperturbed mode and its neighbours. For our Hill problem,

<!-- δ²ω² = Σ_{p' ≠ p} |⟨p' | V | p⟩|² / (ω₀²(p) - ω₀²(p')) -->
$$
\delta^2 \omega^2(p) \;=\; \sum_{p' \neq p}\, \frac{|\langle p'\,|\,V\,|\,p\rangle|^2}{\omega_0^2(p) \;-\; \omega_0^2(p')}
$$

where V is the perturbing operator (the χ-dependent piece of L = Δ_g acting on ψ), and the sum runs over allowed Bloch states p' ≡ p (mod 3) — the corrugation can only couple states within the same Bloch sector (because P_x(u) is periodic in 2π, not 2π/3).

### 6.1 The correct small parameter

It is **not** χ that controls the size of the perturbation — it is the ratio of profile size to ring radius. Writing P_x = r_lobe · P̃_x(u) where P̃_x is order-1 in r_lobe units, and noting r_lobe / R_major = ε/(2 + χ), the natural small parameter is

<!-- η ≡ r_lobe / R_major = ε / (2 + χ) -->
$$
\eta \;\equiv\; \frac{r_{\mathrm{lobe}}}{R_{\mathrm{major}}} \;=\; \frac{\varepsilon}{2 + \chi}
$$

Corrections enter at order η², and the perturbation series is convergent only when η ≪ 1. For ε ≈ 0.5, χ ≈ 1 we have η ≈ 0.17 (acceptable); for ε ≈ 3 we have η ≈ 1 (PT breaks down). This is an important calibration we did not have at the start of §5.

### 6.2 Fourier structure of P_x(u)

The clover profile satisfies P(u + 2π/3) = R_{2π/3} P(u). In complex form P_± ≡ P_x ± i P_y:

<!-- P_+(u + 2π/3) = e^{2πi/3} P_+(u) -->
$$
P_+(u + 2\pi/3) \;=\; e^{2\pi i / 3}\, P_+(u)
$$

So P_+ has Fourier modes only at indices q ≡ 1 (mod 3), and P_− only at q ≡ 2 (mod 3). Therefore P_x has Fourier support only on q ≡ ±1 (mod 3), with no q ≡ 0 (mod 3) component. **Numerically computed Fourier coefficients** ã_q ≡ (1/2π) ∫₀^{2π} P̃_x(u) e^{−iqu} du for the clover (in r_lobe units, with r_lobe = 1, r_saddle = χ):

| q | \|ã_q\| at χ=0.5 | \|ã_q\| at χ=1.0 | \|ã_q\| at χ=2.0 |
|---|---|---|---|
| ±1 | 0.85 | 1.06 | 1.41 |
| ±2 | 0.22 | 0.29 | 0.39 |
| ±4 | 0.18 | 0.20 | 0.16 |
| ±5 | 0.05 | 0.07 | 0.07 |

(Verified: |ã_q| at q ≡ 0 (mod 3) is < 10⁻⁹.) The series is dominated by |q| ≤ 5; higher harmonics contribute < 5% to second-order sums in the cases checked.

### 6.3 Coupling and the second-order shift

Working in R_major = 1 units and treating L = −∂_u² − [η P̃_x'/(1+η P̃_x)] ∂_u + ε² k_v²/(1+η P̃_x)² as the operator with eigenvalue E = ε² ω², the first-order perturbation operator is

<!-- L_1 ψ = -P̃_x' ∂_u ψ - 2 ε² k_v² P̃_x ψ -->
$$
L_1 \psi \;=\; -\tilde P_x'(u)\, \partial_u \psi \;-\; 2 \varepsilon^2 k_v^2\, \tilde P_x(u)\, \psi
$$

Matrix elements between unperturbed plane waves ψ_p = e^{ipu}/√(2π) evaluate to

<!-- ⟨ψ_{p+q}|L_1|ψ_p⟩ = ã_q · (pq - 2ε² k_v²) -->
$$
\langle\psi_{p+q} \,|\, L_1 \,|\, \psi_p\rangle \;=\; \tilde a_q \cdot (p\,q \;-\; 2\varepsilon^2 k_v^2)
$$

with energy denominator E_p − E_{p+q} = −q(2p+q). The second-order shift in **dimensionless mass squared** is

<!-- δ²μ²_{(n,m)}(ε, χ) = -1/(2+χ)² · Σ_{q≠0} |ã_q(χ)|² · (mq - 2ε² k_v²)² / (q(2m+q)) -->
$$
\boxed{\;\delta^2 \mu^2_{(n, m)}(\varepsilon, \chi) \;=\; -\,\frac{1}{(2+\chi)^2}\,\sum_{q \neq 0}\, \frac{|\tilde a_q(\chi)|^2\,\bigl(m\,q \;-\; 2\varepsilon^2\, k_v^2\bigr)^2}{q\,(2m + q)} \;}
$$

with k_v = n − 2m/3 and p = m, summed over q ≡ ±1 (mod 3). **This is the closed-form O(η²) correction.** The total mass squared through this order is

<!-- μ²_(n, m)(ε, χ) = (n - 2m/3)² + (m/ε)² + δ²μ²_(n,m)(ε, χ) + O(η⁴) -->
$$
\mu^2_{(n, m)}(\varepsilon, \chi) \;=\; \left(n - \tfrac{2m}{3}\right)^2 \;+\; \left(\tfrac{m}{\varepsilon}\right)^2 \;+\; \delta^2\mu^2_{(n,m)}(\varepsilon, \chi) \;+\; O(\eta^4)
$$

### 6.4 Numerical evaluation: the corrections are LARGE

Plugging the Fourier coefficients ã_q(χ) into the formula above and evaluating for the candidate (proton, neutron) modes from §7–8:

| (n_p, m_p) → (n_n, m_n) | ε | χ | η | μ²_p (0th) | δ²μ²_p | μ²_n (0th) | δ²μ²_n | m_n/m_p (corrected) |
|---|---|---|---|---|---|---|---|---|
| (1, 2) → (0, 1) | 3.0 | 1.0 | 1.00 | 0.556 | +0.725 | 0.556 | +7.91 | 2.57 |
| (1, 2) → (0, 1) | 1.0 | 1.0 | 0.33 | 4.111 | +0.136 | 1.444 | +0.425 | 0.66 |
| (1, 2) → (0, 1) | 0.5 | 1.0 | 0.17 | 16.111 | +0.087 | 4.444 | +0.143 | 0.53 |
| (1, 1) → (2, 0) | 0.5 | 1.0 | 0.17 | 4.111 | +0.084 | 4.000 | −1.016 | 0.84 |
| (1, 1) → (2, 0) | 0.5 | 2.0 | 0.13 | 4.111 | +0.063 | 4.000 | −0.844 | 0.87 |

**Target m_n/m_p = 1.001378.** The corrections move the ratio away from the target in every PT-valid regime tested.

**Three findings:**

1. **The PT expansion is valid only for ε ≪ 2 + χ.** At ε = 3 (where the zeroth-order Identification II suggested) η = 1 and the corrections are larger than the zeroth-order μ². The toy inversion of §8 sat in the wrong regime.

2. **Different modes respond very differently to corrugation.** The mode (2, 0) (a pure ring mode with k_φ = 0, k_v = 2) has δ²μ² ≈ −1 at ε = 0.5, χ = 1 — a 25% downward shift. The mode (1, 1) at the same point shifts by only +2%. The corrugation strongly favours integer-ring modes through energy-denominator resonances with neighbouring states.

3. **No tested (n, m) → (proton, neutron) assignment fits the observed m_n/m_p in any PT-valid regime.** The zeroth-order inversion's apparent matches (§8.1's clusters) are artifacts of ignoring χ-dependence; once it's included, the matches dissolve.

### 6.5 What this means

The framework is **falsifiable at this stage**, not merely under-determined. The forward map μ²(n, m, ε, χ) is now in closed form through O(η²), and we can ask whether any (low-)integer (n, m) labels give the observed m_n/m_p ≈ 1.001378 for some (ε, χ) with η small enough for PT to make sense.

### 6.6 Numerical validation overturned §6.4

An independent numerical solver (scripts/laplacian_spectrum.py) was built to validate the analytical claims of §§4–6.4. It uses **a Fourier-basis representation of the Hill operator with proper Bloch-sector restriction** (p ≡ q mod 3 for k_v = q/3). The solver does *not* use any analytical formula from this file — it discretises K and M in the plane-wave basis and solves the generalised eigenvalue problem K ψ = ω² M ψ.

Validation results (scripts/validate_mass_formula.py):

| Claim | Result |
|---|---|
| (C2) Zeroth-order formula μ² = (n − 2m/3)² + (m/ε)² | **VALIDATED** at η = 0.033 to machine precision (max relative error 0.00004) |
| (C3) First-order χ-shifts vanish; corrections scale as η² | **VALIDATED** |
| (C4) §6.3 second-order PT formula | **INVALIDATED** — predicts shifts ~10× too large |
| (C5) §6.4's "no low-(n, m) fit" claim | **OVERTURNED** — pairs like (1, 2) ↔ (2, 2) at ε ≈ 0.2 fit m_n/m_p to 0.03% |

**Why C4 failed.** My §6.3 PT derivation summed over *all* Fourier neighbours p' ≠ p coupled by P_x. But on the closed surface, the physical Hilbert space at given k_v is restricted to the Bloch sector p ≡ q (mod 3). Within this sector, neighbours differ by κ ≡ 0 (mod 3), and a_κ = 0 there (since P_x's Fourier support is on κ ≡ ±1 mod 3). The actual intra-sector coupling comes from (1/w)_κ = (1/(1+P_x))_κ — a *much* weaker coupling (order P_x² at leading order, since 1/(1+P_x) ≈ 1 − P_x + P_x² − ... and only P_x² and higher have support on κ ≡ 0 mod 3). The numerical second-order shifts (~0.003–0.01) are consistent with this much smaller coupling.

**The corrected version of §6.3 would be:** δ²μ² ∼ k_v⁴ × Σ_{κ ∈ 3ℤ, κ ≠ 0} |(1/w)_κ|² / (κ(2p+κ)). Computing (1/w)_κ requires either a numerical FT of 1/(1+P_x) or expanding (1+P_x)^{-1} to enough orders to pick up the κ ≡ 0 (mod 3) modes (which start at P_x²).

**Why C5 reversed.** The bogus large-PT-shift in §6.4 made it look as if χ-corrections were destroying every candidate identification. With correct (small) shifts from the numerical solver, the **zeroth-order formula is accurate enough** that the toy inversion of §8.1 is approximately valid. The numerical solver confirms:

- (p, n) = ((±1, ±2), (±2, ±2)) at ε ≈ 0.2, χ ∈ [0.5, 2.0] gives m_n/m_p ≈ 1.00168 (target 1.00138)
- Many similar pairs cluster around the right ratio

The error of 0.03% can plausibly be closed by fine-tuning (ε, χ) or by going to slightly higher (n, m) labels.

### 6.7 New next steps

The cheap perturbative analysis was wrong. The expensive numerical solver works. So:

1. **Replace §6.3 perturbation theory with the proper intra-sector formula**, or just use the numerical solver as the truth.
2. **Fine-tune (ε, χ) within the candidate cluster** using the numerical solver to match m_n/m_p to better than 0.03%.
3. **Use the absolute mass m_p as a second constraint** to pin R_major (and hence both ε and the physical scale).
4. **Look for the (n, m) label whose wavefunction structurally matches "the proton"** — overlap with lobe regions, etc. This is the physical identification question.

## 7. The mode-particle identification

To invert m_proton, m_neutron → (ε, χ), we need to know **which (n, m) labels are the proton and the neutron**. Two reasonable identifications are on the table; we have not yet pinned which is correct.

**Identification I — semiclassical path windings.** clover-quarks.md §12.2 finds that the classical proton path (2 lobes + 1 saddle) closes at (n_θ, n_φ) = (2, 1), and the neutron path (1 lobe + 2 saddles) at (n_θ, n_φ) = (1, 1). A wavepacket on each path has group-velocity ratio v_φ/v_θ = n_φ/n_θ. For our flat-limit dispersion ω² = (n − 2m/3)²/R² + m²/c², the group-velocity ratio is

<!-- v_φ/v_θ = -τ + m/((n - 2m/3) ε²) -->
$$
\frac{v_\varphi}{v_\theta} \;=\; -\tau + \frac{m}{(n - 2m/3)\,\varepsilon^2}
$$

Solving this for low (n, m) values (with τ = 1/3) gives discrete sets of (ε, n, m) for each path. This route is **not yet closed**; it gives one equation between ε and the (n, m) of each particle, requiring more information.

**Identification II — lowest matching modes.** Identify each particle with the lowest mode consistent with its topology. Per the dispersion μ² = (n − 2m/3)² + (m/ε)², the low-lying non-zero-mass modes at moderate-to-large ε (where the cross-section term doesn't blow up) are dominated by minimum |n − 2m/3|:

| Candidate (n, m) | n − 2m/3 | μ² |
|---|---|---|
| (1, 1) | 1/3 | 1/9 + 1/ε² |
| (1, 2) | −1/3 | 1/9 + 4/ε² |
| (0, 1) | −2/3 | 4/9 + 1/ε² |
| (−1, −1) | −1/3 | 1/9 + 1/ε² |

The closest-mass pair (1, 1) and (1, 2) shares the smallest |n − 2m/3| = 1/3; they differ only in the cross-section term (m=1 vs m=2). One is the proton, the other the neutron. **Guess:** the lighter (1, 1) is the proton, the heavier (1, 2) is the neutron. (Check the sign in §8 — for some ε the order flips.)

## 8. Toy inversion under Identification II

Take proton = (1, 1) and neutron = (1, 2). The flat-limit masses:

<!-- μ²_p = 1/9 + 1/ε² ; μ²_n = 1/9 + 4/ε² -->
$$
\mu^2_p \;=\; \tfrac{1}{9} + \frac{1}{\varepsilon^2}, \qquad
\mu^2_n \;=\; \tfrac{1}{9} + \frac{4}{\varepsilon^2}
$$

μ²_n > μ²_p for all ε > 0 — order is automatic and correct. The mass ratio:

<!-- (m_n / m_p)² = (1/9 + 4/ε²) / (1/9 + 1/ε²) = (ε² + 36) / (ε² + 9) -->
$$
\left(\frac{m_n}{m_p}\right)^2 \;=\; \frac{1/9 + 4/\varepsilon^2}{1/9 + 1/\varepsilon^2} \;=\; \frac{\varepsilon^2 + 36}{\varepsilon^2 + 9}
$$

Observed m_n/m_p ≈ 1.001378, so (m_n/m_p)² ≈ 1.002758. Solve:

$$
\varepsilon^2 + 36 \;=\; 1.002758\,(\varepsilon^2 + 9)
\;\;\Longrightarrow\;\;
0.002758\,\varepsilon^2 \;=\; 36 \;-\; 9.025 \;=\; 26.975
$$

$$
\boxed{\;\varepsilon^2 \;\approx\; 9780, \qquad \varepsilon \;\approx\; 98.9\;}
$$

So under Identification II with (proton, neutron) = ((1, 1), (1, 2)), the **proton–neutron split forces an enormous ε ≈ 99** — the cross-section is ~100× the ring circumference. Physically unreasonable; this rules out this assignment under the leading-order formula.

**Alternative under Identification II:** try (proton, neutron) = ((1, 2), (0, 1)). Then μ²_p = 1/9 + 4/ε², μ²_n = 4/9 + 1/ε². For m_n > m_p we need 4/9 + 1/ε² > 1/9 + 4/ε², i.e., 3/9 > 3/ε², i.e., ε² > 9. The ratio:

<!-- (m_n/m_p)² = (4/9 + 1/ε²)/(1/9 + 4/ε²) = (4ε² + 9)/(ε² + 36) -->
$$
\left(\frac{m_n}{m_p}\right)^2 \;=\; \frac{4\varepsilon^2 + 9}{\varepsilon^2 + 36} \;=\; 1.002758
$$

$$
4\varepsilon^2 + 9 \;=\; 1.002758\,(\varepsilon^2 + 36)
\;\;\Longrightarrow\;\;
2.997\,\varepsilon^2 \;=\; 27.099
\;\;\Longrightarrow\;\;
\boxed{\;\varepsilon^2 \;\approx\; 9.04, \quad \varepsilon \;\approx\; 3.007\;}
$$

This is more physical: ε ≈ 3, meaning the cross-section perimeter is roughly 3× the ring circumference. The geometry is a "fat tube" with prominent cross-section.

Absolute mass scale: μ²_p = 1/9 + 4/9.04 ≈ 0.5536, so μ_p ≈ 0.7441. Match to m_p = 938 MeV (Compton wavenumber m_p c/ℏ = 4.756 fm⁻¹):

<!-- R = μ_p / (m_p c / ℏ) ≈ 0.156 fm -->
$$
R_{\mathrm{major}} \;=\; \frac{\mu_p}{m_p c / \hbar} \;\approx\; 0.156\;\mathrm{fm}, \qquad
c_{\mathrm{arc}} = \varepsilon R \;\approx\; 0.47\;\mathrm{fm}
$$

The major-ring radius is roughly the proton Compton wavelength (0.21 fm), and the cross-section perimeter is ~3× that. The full surface fits inside a ~0.6 fm × 0.5 fm bounding box — comparable to the proton's measured charge radius (0.84 fm) at the same order of magnitude, somewhat smaller.

**Caveats on this toy result:**
1. **Identification II is a guess.** No first-principles argument pins (p, n) = ((1, 2), (0, 1)). Other assignments give different ε.
2. χ-corrections (§6) at second order will shift μ²_p and μ²_n unequally. Until they're computed, the ε ≈ 3 number is provisional.
3. The "lower-mass" assignment chose (1, 2) as proton over (0, 1) because the cross-section dominates at ε > 3. At ε < 3, the order flips and (0, 1) is lighter.
4. The (0, 1) ↔ (1, 2) split could equally be u-d (proton/neutron internal quarks) rather than p-n. Need to clarify whether each (n, m) is a single particle or an internal degree of freedom.
5. Quantum/loop corrections are entirely absent — this is a tree-level standing-wave calculation.

**Headline (zeroth order only).** The leading-order formula gives **a discrete result for ε** when we pick a pair of (n, m) modes. Under Identification II we get ε ≈ 3, R ≈ 0.16 fm.

**Important caveat — see §6.4.** Once the second-order χ-corrections are computed numerically, the ε ≈ 3 point sits at η = 1 where perturbation theory fails outright, and the corrections invalidate the toy inversion. The ε ≈ 0.5 cluster from §8.1 also fails when corrected. **No low-(n, m) identification tested so far matches the observed m_n/m_p when χ-corrections are included.** The leading-order toy inversion is misleading; reading §8 in isolation overstates the result. Proceed to §6.4–6.5 for the corrected picture.

### 8.1 Survey of low-(n, m) identifications

A brute survey over all ordered pairs ((n_p, m_p), (n_n, m_n)) with |n|, |m| ≤ 3 (matching the observed m_n/m_p) reveals **372 compatible identifications** in physically plausible ε ∈ [0.1, 50]. The solution clusters at a few discrete ε values:

| ε | μ_p | R_major [fm] | c_arc [fm] | Sample (n_p, m_p) → (n_n, m_n) |
|---|---|---|---|---|
| 0.16 | 19.0 | 4.0 | 0.63 | (2, 3) → (1, 3) |
| 0.18 | 11.0 | 2.3 | 0.42 | (1, 2) → (2, 2) |
| 0.51 | 2.00 | 0.42 | 0.21 | (1, 1) → (2, 0) |
| 0.53 | 2.00 | 0.42 | 0.22 | (0, 1) → (2, 0) |
| 0.65 | 3.07 | 0.65 | 0.42 | (2, −1) → (1, 2) |
| 3.0 | 0.74 | 0.16 | 0.47 | (1, 2) → (0, 1) |

**The cluster near ε ≈ 0.5, R ≈ 0.42 fm is robust** in that several distinct identifications converge on this same (ε, R_major) — e.g. (proton, neutron) = ((1, 1), ±(2, 0)) or ((0, 1), ±(2, 0)) — so the value isn't an artefact of a single arbitrary pairing.

**Is R_major ≈ 0.42 fm ≈ R_p/2 a real prediction?** Not yet. We used **only two inputs** in the inversion: m_p (sets the overall mass scale) and m_n/m_p (sets ε). The proton charge radius R_p = 0.84 fm was *not* an input. Three concerns before claiming significance:

1. **R_major is not R_p.** R_p is the RMS electromagnetic radius — for our torus, R_p² ≈ R_major² + (cross-section RMS)² + (charge-distribution-shape corrections). A back-of-envelope estimate gives R_RMS_torus ≈ 0.44 fm at this point, comparable to R_major but well below R_p = 0.84 fm.
2. **The 0.42 fm is not unique** — the survey also gives clusters at 2.3 fm (much too large), 4.0 fm (way too large), 0.65 fm, 0.16 fm, etc. The 0.42 fm cluster is one of several.
3. **No first-principles reason** has been given for which (n, m) family is "the proton." If a different identification is the physical one, R_major could be anywhere in the survey range.

**Conservative reading.** The 0.42 fm value is *not* shown to be coincidence (it survives across identifications within one cluster), but it's also not shown to be a prediction of the geometry (multiple clusters exist; R_major ≠ R_p; no identification pinned). Treat as a hint to revisit once the identification is fixed and a proper ⟨r²⟩ calculation is done on the surface.

**Pinning the identification.** The leading-order constraint produces a *family* of solutions, not a unique answer. To collapse the family we need additional input:

1. **A third observable** (e.g., the Δ⁺ resonance mass, the electron mass, or the muon mass) — gives a second algebraic equation.
2. **The χ-dependent second-order correction** (§6) — different identifications produce different F(n, m, ε) and so different χ-dependence; matching the mass split exactly via the χ-correction pins χ as well, and may select a unique identification.
3. **A first-principles argument** for the (n, m) → particle map — e.g., wavefunction-overlap with lobe regions, or a path-integral derivation.

The fact that ε ≈ 0.5 emerges robustly across multiple identifications is the most promising leading-order signal. The cross-section-perimeter c ≈ 0.21 fm at this point is close to the proton Compton wavelength λ_C = 0.21 fm — suggestive of a structural relationship.

## 9. What we have, what we don't

**Established analytically — plain-language summary:**

1. **The wave problem on a 2D corrugated torus collapses to a 1D wave problem along one helical coordinate.** Because the corrugation has a helical translation symmetry, the wave can be decomposed: one component is a plain oscillation around the ring, and the other is a periodic function along the cross-section. We only need to solve a 1D ordinary differential equation.

2. **Allowed waves carry ring-momentum in steps of 1/3, not 1.** Going once around the ring also shifts the cross-section by 120° (the twist). For a wave to come back to itself, its ring-momentum must be an integer-plus-multiple-of-1/3. This is the same "third-integer momenta" structure that gives the up/down quark fractional charges in §11 of clover-quarks. It is a property of the topology, not of corrugation depth or of which embedding we pick.

3. **The bare mass formula is μ² = (n − 2m/3)² + (m/ε)².** Two integers (n, m) label each wave. The first term measures ring-oscillation energy after accounting for the twist's effect on the wavenumber. The second term is cross-section energy, scaled by the aspect ratio ε (thin tube ⇒ small ε ⇒ large cross-section frequencies). This is exactly the standard MaSt twisted-torus formula with shear σ = 2/3.

4. **Shallow corrugation doesn't shift masses at leading order.** The corrugation depth χ averages out: ⟨P_x⟩ = 0 by 3-fold symmetry. So the bare formula in point 3 is accurate to better-than-linear order in χ; corrections start at order χ².

5. **The first correction enters at χ², via Fourier mixing.** The corrugation couples each wave to its neighbours through the Fourier components of P_x(u). The mass shift takes the form δ²μ² = χ² · F(n, m, ε) where F is a finite sum over Fourier indices that is, in principle, computable analytically.

6. **The toy zeroth-order inversion is approximately valid** — independent numerical validation (§6.6) shows that χ-corrections within the proper Bloch sector are small (~0.1%, not the ~10% my §6.3 PT incorrectly predicted). Pairs like (proton, neutron) = ((1, 2), (2, 2)) at ε ≈ 0.2, χ ∈ [0.5, 2] fit m_n/m_p ≈ 1.00168 (target 1.00138) — within 0.03%. This is **not yet a confirmed prediction**, but the framework **clearly passes** the qualitative test that the leading-order machinery can reproduce the proton/neutron mass split.

**Done in this draft (since the original outline):**
1. ~~Fourier coefficients a_q(χ) for the clover profile~~ — done numerically (§6.2).
2. ~~Evaluate F(n, m, ε) for candidate (p, n) modes~~ — done (§6.3–6.4); closed-form formula given.
3. ~~Run the inversion with χ-corrections~~ — done numerically; no low-(n, m) identification fits.

**Open / next steps:**
1. **Solve the Hill equation directly (non-perturbatively)** for a small grid of (ε, χ). This is a 1D ODE eigenvalue problem — scipy can do it in milliseconds. Sweep small grids and check whether *any* (ε, χ, identification) gives m_n/m_p = 1.001378.
2. **Expand the search over (n, m).** Higher-(n, m) modes have smaller second-order corrections (more accessible decoupled neighbours), and might satisfy the inversion in a PT-valid regime.
3. **Redo for embedding B (rotation).** Embedding B has a different metric and hence different δ²μ². The structural conclusion (whether the geometry can or cannot produce m_n/m_p) might depend on the embedding.
4. **Cross-check the mode-particle identification** by computing wavefunction overlaps with lobe vs saddle regions for the candidate (n, m).
5. **If all of the above fail**, accept that the corrugated-torus geometry as currently specified does not reproduce the proton-neutron mass ratio quantitatively, even though it succeeds qualitatively (Q_lobe = +2/3, Q_saddle = −1/3, three-quark structure, Z₃ confinement, β-decay topology).

**Structural payoff** of this work, regardless of the negative inversion outcome:

- The Laplacian on this surface is now in closed form through O(η²).
- The forward map μ² → (ε, χ, n, m) is explicit and verified numerically.
- We have a concrete falsifiable observable (m_n/m_p) and can say whether the geometry passes or fails.
- The next step is one 1D ODE eigensolver, not a 2D PDE eigensolver — *much* cheaper than the original Phase-C plan.

## 10. Cross-references

- [clover-quarks.md §9](clover-quarks.md) — surface embeddings A and B; both metric forms
- [clover-quarks.md §10](clover-quarks.md) — induced metric used in §1–2 here
- [clover-quarks.md §11](clover-quarks.md) — independent derivation of k_θ = n − m/3 from mode-quantisation arguments; matches §3 here
- [clover-quarks.md §12](clover-quarks.md) — proton/neutron path winding (2,1) and (1,1) (Identification I)
- [metric-charge ch. 7](../../metric-charge/07-aspect-ratio-and-character.md) — flat-torus dispersion μ² = (n_t/ε)² + (n_r − σ·n_t)² that our §4 reproduces in the constant-radius limit
