# Derivation step 1 — closed-form per-arc charge integral

**Status:** First mathematical derivation step under the C1–C6 hypothesis
chain of [derived-clover.md](derived-clover.md). Goal: express the
per-arc charge Q(t₀) of a closed track on the substrate as an explicit
function of the substrate's modulation parameters, then read off the
constraints that pick the proton/neutron-correct modulation.

This file is the worked derivation; [derived-clover.md](derived-clover.md)
remains the strategic frame.

---

## 1. Substrate setup (no pre-commit to half-twist)

Substrate cross-section (harmonic, N = 3, from C1 + C2):

<!-- w(t; θ) = 1 + a1(θ) cos 3t + a2 cos 6t + i (b1(θ) sin 3t + b2 sin 6t) -->
$$
w(t;\theta) \;=\; 1 + a_1(\theta)\cos 3t + a_2\cos 6t
\;+\; i\bigl(b_1(\theta)\sin 3t + b_2\sin 6t\bigr)
$$

The 3-fold harmonics a₁(θ), b₁(θ) are the **modulation**; the 6-fold
backbone a₂, b₂ is held constant in θ. The embedded surface is

<!-- zeta(t; θ) = rho · e^{i (alpha(θ) + t)} · w(t; θ) -->
$$
\zeta(t;\theta) \;=\; \rho\,e^{i(\alpha(\theta)+t)}\,w(t;\theta),
\qquad \alpha(\theta) \text{ is the twist (TBD).}
$$

embedded in 3-space by **(x, y, z) = ((R + Re ζ) cos θ, Im ζ, (R + Re ζ) sin θ)**
with ring radius R.

## 2. Closure → allowed twists (C3 in concrete form)

The surface closes as a torus iff ζ(t, θ + 2π) = ζ(t + s, θ) for some
constant t-shift s. Setting equal and matching harmonic content:

  *   Real "+1" term forces e^{i(2π τ − s)} = 1, so **s = 2π τ mod 2π**.
  *   Matching the cos 3t coefficient forces **sin 3s = 0**, so
      s ∈ {0, π/3, 2π/3, π, 4π/3, 5π/3} (multiples of π/3).
  *   Combined: **τ is a multiple of 1/6**.

Within this, two sub-cases split by the cos 3s sign:

| τ (mod 1) | s | cos 3s | Modulation constraint |
|---|---|---|---|
| 0       | 0       | +1 | a₁(θ+2π) = a₁(θ) (2π-periodic) |
| 1/6     | π/3     | −1 | a₁(θ+2π) = −a₁(θ) (antiperiodic) |
| 1/3     | 2π/3    | +1 | 2π-periodic |
| 1/2     | π       | −1 | antiperiodic (the half-twist of modulated-clover) |
| 2/3     | 4π/3    | +1 | 2π-periodic |
| 5/6     | 5π/3    | −1 | antiperiodic |

**Which twist is selected** depends on what we want of the tracks — see
§3. The derivation proceeds in parallel for the half-twist (τ = 1/2,
antiperiodic modulation, (1/2, 1) tracks each covering 3 of 6 pieces)
and the third-twist (τ = 1/3, periodic modulation, (1/3, 1) tracks
each covering 1 of 6 pieces) candidates; the half-twist gets explicit
treatment first because it is the case we have charge-correct
coefficients for.

## 3. Track structure on the half-twist surface

A track t(θ) = t₀ + θ/2 advances at twist rate ½. Over one ring
revolution θ ∈ [0, 2π] it advances Δt = π — half the cross-section
(3 of 6 pieces). The half-twist identification (t, θ+2π) ~ (t + π, θ)
identifies the track's endpoint back to its start, so the track
closes in one ring revolution.

Two distinct phase-offset tracks at t₀ ∈ {−π/6, +π/6} (separated by
one piece, π/3 apart) give proton and neutron candidates. By the
half-twist's Z₂ × Z₃ structure (when modulation respects it), three
phases of each (offset by 2π/3 along t) are equivalent under the
ring-axis symmetry, giving 3 proton + 3 neutron = 6 baryon replicas
in one Z₂ × Z₃ orbit.

## 4. The per-arc charge integral

The local charge density along a curve on the substrate is
∂_tχ where χ = arg(∂_tζ) (the cross-section's tangent direction).
Per-arc charge along a closed track:

<!-- Q(t0) = (1/2pi) ∫ ∂_t chi dt -->
$$
Q(t_0) \;=\; \frac{1}{2\pi} \int_{\text{track}} \partial_t\chi\,dt
\;=\; \frac{1}{4\pi}\int_0^{2\pi} \partial_t\chi\bigl(t_0 + \tfrac{\theta}{2},\,\theta\bigr)\,d\theta
$$

(using dt = dθ/2 along the (1/2, 1) track).

### 4.1 Decomposing ∂_tχ

Write w = u + iv, A ≡ ∂_t(e^{−i(α+t)} ζ) / ρ = ∂_tw + iw. Then

<!-- ∂_t zeta = rho e^{i(alpha+t)} · A,  with  A = w' + iw -->
$$
\partial_t\zeta \;=\; \rho\,e^{i(\alpha+t)}\cdot A,
\qquad A \;=\; \partial_t w + i\,w.
$$

So χ = (α + t) + arg A, and

<!-- ∂_t chi = 1 + Im( A-bar · partial_t A ) / |A|^2 -->
$$
\boxed{\;\partial_t\chi \;=\; 1 \;+\; \frac{\mathrm{Im}\bigl(\bar A\,\partial_t A\bigr)}{|A|^2}\;}
$$

with ∂_tA = ∂_t²w + i ∂_tw.

### 4.2 The "half-base + modulation correction" identity

Substituting into the track integral:

<!-- Q(t0) = 1/2 + M(t0), where M(t0) = (1/4pi) ∫_0^2pi [Im(A-bar A')/|A|^2] d theta -->
$$
Q(t_0) \;=\; \tfrac{1}{2}
\;+\; M(t_0),
\qquad
M(t_0) \;=\; \frac{1}{4\pi}\int_0^{2\pi}
\frac{\mathrm{Im}\bigl(\bar A\,\partial_t A\bigr)}{|A|^2}
\Big|_{t=t_0+\theta/2}\,d\theta
$$

— so each (1/2, 1) track carries a **base charge of exactly ½** from
the e^{it} factor (the "half-turn in tangent direction over half the
cross-section"), plus a **modulation-dependent correction** M(t₀).

### 4.3 Charge targets translated into M

For Q_proton = +1 and Q_neutron = 0:

<!-- M(-pi/6) = +1/2,  M(+pi/6) = -1/2 -->
$$
M\bigl(-\tfrac{\pi}{6}\bigr) \;=\; +\tfrac{1}{2},
\qquad
M\bigl(+\tfrac{\pi}{6}\bigr) \;=\; -\tfrac{1}{2},
\qquad
M(-\tfrac{\pi}{6}) - M(+\tfrac{\pi}{6}) \;=\; 1.
$$

The modulation has to **deliver exactly ±½** on the two tracks. Without
modulation, the half-twist surface gives the same M ≈ 0 to every track
by 6-fold cross-section symmetry, so all tracks would have Q = ½ — the
"half-integer charge of a half-turn." The modulation breaks this
symmetry and provides the integer-completing correction.

## 5. Symmetric modulation — parameter count

Per C4 (3-fold ring-axis symmetry) with the half-twist (τ = 1/2,
antiperiodic modulation), the modulation harmonics are restricted to
(cos, sin)((2k+1)θ/2) with (2k+1) ∈ {3, 9, 15, …}. The minimal symmetric
family uses only k=1:

<!-- a1(θ) = alpha_c cos(3θ/2) + alpha_s sin(3θ/2);  b1(θ) = beta_c cos(3θ/2) + beta_s sin(3θ/2). -->
$$
a_1(\theta) \;=\; \alpha_c\cos\tfrac{3\theta}{2}+\alpha_s\sin\tfrac{3\theta}{2},
\qquad
b_1(\theta) \;=\; \beta_c\cos\tfrac{3\theta}{2}+\beta_s\sin\tfrac{3\theta}{2}.
$$

— four free parameters: (α_c, α_s, β_c, β_s).

### 5.1 One phase is absorbable

Write a₁(θ) = A cos(3θ/2 − φ_a) and b₁(θ) = B cos(3θ/2 − φ_b), so the
four real parameters re-organise as **two amplitudes** (A, B) and
**two phases** (φ_a, φ_b). Shifting the **origin of θ** by Δθ
re-phases both: φ_a → φ_a + 3Δθ/2 and φ_b → φ_b + 3Δθ/2 *together*.
Choose Δθ to set φ_a = 0:

<!-- a1(θ) = A cos(3θ/2),  b1(θ) = B cos(3θ/2 - phi) -->
$$
a_1(\theta) \;=\; A\,\cos\tfrac{3\theta}{2},
\qquad
b_1(\theta) \;=\; B\,\cos\bigl(\tfrac{3\theta}{2}-\phi\bigr),
$$

so the **symmetric subspace has 3 essential parameters**: A, B, and the
relative phase φ ≡ φ_b − φ_a. Plus the backbone (a₂, b₂) and R_major.
Total essential parameter count: **6** (down from 9 unconstrained
Step-7, then 7 symmetric Step-7, then 6 after phase absorption).

### 5.2 The two charge constraints

Q_proton = +1 and Q_neutron = 0 give **two equations** in (A, B, φ,
a₂, b₂). That leaves a **3-parameter family** of charge-correct
symmetric solutions. R_major then sets the mass ratio. Among the
remaining 2 free parameters, an additional principle (variational?
minimum-curvature? minimum-action?) would be needed to pick a unique
solution.

## 6. The integrand explicitly

Let τ = ½ (half-twist), α(θ) = θ/2. Along the track t = t₀ + θ/2:

  *   cos 3t = cos(3t₀ + 3θ/2), sin 3t = sin(3t₀ + 3θ/2)
  *   cos 6t = cos(6t₀ + 3θ), sin 6t = sin(6t₀ + 3θ)
  *   a₁(θ) = A cos(3θ/2), b₁(θ) = B cos(3θ/2 − φ)

Writing the cross-section harmonics in terms of T ≡ 3θ/2:

  *   cos 3t = cos(3t₀ + T) = cos 3t₀ cos T − sin 3t₀ sin T
  *   sin 3t = sin(3t₀ + T) = sin 3t₀ cos T + cos 3t₀ sin T
  *   cos 6t = cos(6t₀ + 2T), sin 6t = sin(6t₀ + 2T)
  *   a₁(θ) = A cos T, b₁(θ) = B cos(T − φ)

So the cross-section pieces become trigonometric polynomials in **T**
of low order (degree 3 in cos T, sin T overall, since the highest
combination is cos T · cos 2T = ½(cos 3T + cos T), and similar).

Plugging into A = ∂_tw + iw and computing Im(Ā ∂_tA)/|A|² yields a
**rational trigonometric function of T**:

<!-- M(t0) = (1/4pi) ∫_0^2pi [N(T; t0, A, B, phi, a2, b2)] / [D(T; t0, A, B, phi, a2, b2)] · (2/3) dT -->
$$
M(t_0) \;=\; \frac{1}{6\pi}\int_0^{3\pi}
\frac{N(T;\,t_0,\,A,\,B,\,\phi,\,a_2,\,b_2)}{D(T;\,t_0,\,A,\,B,\,\phi,\,a_2,\,b_2)}\,dT
$$

(after substituting dθ = (2/3) dT; integration range θ ∈ [0, 2π]
becomes T ∈ [0, 3π]).

N and D are trigonometric polynomials in T with coefficients that
depend on t₀ and the modulation. The integrand is **a rational
function of (cos T, sin T)** — exactly the class that
Weierstrass substitution u = tan(T/2) reduces to a rational
function of u, hence integrable in closed form by partial
fractions.

So **the integral M(t₀) admits an analytical evaluation in
principle**, via:

  1. Substitute T-harmonics → polynomial in (cos T, sin T).
  2. Weierstrass u = tan(T/2) substitution.
  3. Partial-fraction decomposition.
  4. Closed-form integration over u ∈ ℝ (since T ranges over the
     full period 3π, with u-poles on the real axis to be tracked
     carefully).

The cost: the partial-fraction decomposition lives in a function
field whose degree grows with the harmonic order (~ degree 12 in
the full case, since the trigonometric polynomial has degree
6 from cos 6t · cos 3t terms and the rational expression has
numerator/denominator both of bounded degree). The closed-form
exists but is large.

## 7. What remains

Three concrete next steps, in order of difficulty:

  1. **Verify M(t₀) symbolically.** Compute M(t₀) as a function of
     (t₀, A, B, φ, a₂, b₂) using a CAS (sympy or Mathematica). Match
     against the numerical track_charge values from the Step-7
     coefficients. If the symbolic result reproduces the numerics,
     the analytical machinery is sound and the closed form is
     established.

  2. **Solve the charge constraints analytically.** With M(t₀) in
     closed form, the system M(−π/6) = +½ and M(+π/6) = −½ is two
     equations in (A, B, φ, a₂, b₂). Solve for a 3-parameter family
     of (A, B, φ, a₂, b₂) satisfying both. The family's structure
     will tell us whether the framework over-constrains or
     under-constrains the modulation.

  3. **Add the third-twist alternative.** Repeat §§3–6 for τ = 1/3
     (periodic modulation, (1/3, 1) tracks each covering 1 piece).
     The "per-piece charge" reading there gives natural ±2/3, ∓1/3
     candidates without modulation correction. Compare which
     reading is structurally cleaner.

## 8. Provisional findings

  *   **Q(t₀) = ½ + M(t₀)** is the clean structural identity that all
      symmetric half-twist constructions satisfy. The half-integer
      "base" charge per (1/2, 1) track is a property of the
      half-twist closure alone; the integer baryon charges come from
      the modulation M(t₀) breaking the ±½ symmetry between tracks.
  *   **Allowed twists are multiples of 1/6**, with periodic or
      antiperiodic modulation depending on whether the twist is a
      "third-type" (k/3) or a "half-type" (k/3 + 1/6) value. C3 is
      now this closure constraint, not a half-twist pre-commitment.
  *   **The symmetric subspace has 3 essential parameters** (A, B, φ)
      plus the backbone (a₂, b₂), after one phase is absorbed by a
      θ-origin shift. With 2 charge constraints, this leaves a
      3-parameter family of charge-correct symmetric modulations
      (down from Step 7's 4 = 9 unconstrained minus 5 numerically
      pinned).
  *   **M(t₀) is in principle analytically integrable** via the
      Weierstrass substitution route — it's a rational
      trigonometric integral. The closed form is large but exists.
      Computational symbolic algebra (CAS) is the natural next
      tool.
