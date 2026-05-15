# clover-modes-analytical.md — Where do lobe and saddle modes live in the Hill spectrum?

**Status:** Mathematical analysis of the Hill equation's effective potential, asking whether lobe-localized and saddle-localized standing waves exist on the clover corrugated torus, and where they sit in the spectrum relative to whole-circumference modes. Done analytically with WKB-flavored reasoning; no numerics required.

**Reference:** [clover-mass.md §2](clover-mass.md) for the Hill equation in u-coordinates and the Liouville substitution.

---

## 1. Schrödinger form of the Hill equation

The Hill equation from clover-mass §2 is

<!-- ψ'' + (P_x'/(R+P_x)) ψ' + (c²ω² − k_v²c²/(R+P_x)²) ψ = 0 -->
$$
\psi''(u) + \frac{P_x'(u)}{R + P_x(u)}\,\psi'(u) + \left[c^2\omega^2 - \frac{k_v^2 c^2}{(R + P_x(u))^2}\right]\psi(u) = 0
$$

Liouville substitution ψ = (R+P_x)^{-1/2} φ and rescaling ξ = c·u converts this to

<!-- -φ_ξξ + U(ξ) φ = ω² φ -->
$$
-\,\partial_\xi^2 \varphi + U(\xi)\,\varphi = \omega^2\,\varphi
$$

with effective potential

<!-- U(ξ) = k_v²/w² + (1/2)(w_ξξ/w) − (1/4)(w_ξ/w)² where w(u) = R + P_x(u) -->
$$
U(\xi) \;=\; \frac{k_v^2}{w(u)^2} \;+\; \frac{1}{2}\frac{w_{\xi\xi}}{w} \;-\; \frac{1}{4}\left(\frac{w_\xi}{w}\right)^2,
\qquad w(u) \equiv R + P_x(u)
$$

The leading term k_v²/w² is the dominant structure; the correction terms are smaller by O(η²) where η = r_lobe/R_major. We analyze the leading term.

**Crucial observation: U(ξ) vanishes identically at k_v = 0.** Localization is a k_v ≠ 0 phenomenon. The k_v = 0 Bloch sector has free-particle modes only (plane waves in ξ).

---

## 2. What P_x(u) actually looks like

The clover profile P(u) has 3-fold rotational symmetry as a *2D vector*: P(u + 2π/3) = R_{2π/3} P(u). But P_x — the radial component along the torus axis normal — is **not** 3-fold-symmetric in u, because R_{2π/3} mixes the x and y components:

$$
P_x(u + 2\pi/3) \;=\; -\tfrac{1}{2}P_x(u) - \tfrac{\sqrt{3}}{2}P_y(u)
$$

Per [clover-mass §6.2](clover-mass.md), P_x has Fourier support on q ≡ ±1 (mod 3) only — no q ≡ 0 mod 3 component. This is consistent with the lack of period-2π/3 symmetry.

Evaluating at the 6 special points around the profile (with lobe-1 placed at the +x axis):

| Feature | Azimuth | Position | P_x |
|---|---|---|---|
| Lobe-1 apex | 0° | (r_max, 0) | r_max = 2r_lobe + r_saddle |
| Saddle-1 trough | 60° | (r_lobe/2, r_lobe√3/2) | r_lobe/2 |
| Lobe-2 apex | 120° | (−r_max/2, r_max√3/2) | −r_max/2 |
| Saddle-2 trough | 180° | (−r_lobe, 0) | −r_lobe |
| Lobe-3 apex | 240° | (−r_max/2, −r_max√3/2) | −r_max/2 |
| Saddle-3 trough | 300° | (r_lobe/2, −r_lobe√3/2) | r_lobe/2 |

The 3 lobe apexes have **different** P_x values (r_max, −r_max/2, −r_max/2). The 3 saddle troughs likewise (r_lobe/2, −r_lobe, r_lobe/2). The Hill equation's effective potential at fixed k_v therefore has only D_2 (reflection) symmetry in u, not D_3.

**Global structure of P_x(u):** the maximum is unambiguously at lobe-1 apex (P_x = r_max). The minimum of P_x along the profile is *not* at a saddle trough — it's on the side of lobe-2 or lobe-3 (specifically at ψ_L = ±60° on those lobes' arcs, where P_x = −(3r_lobe + r_saddle)/2). This is the global minimum of P_x.

So in terms of the effective potential U = k_v²/(R + P_x)²:

- **Single global minimum (well)** at lobe-1 apex, where w = R + r_max is maximum.
- **Two global maxima (barriers)** on the side of lobes 2 and 3, where w = R − (3r_lobe + r_saddle)/2 is minimum.
- Saddles are at intermediate U values, not the highest barriers.

The 3-fold symmetry of the surface manifests in the Bloch sector structure (k_v ∈ {0, 1/3, 2/3} mod 1), not in any direct period-2π/3 structure of U(u).

---

## 3. Well depth at lobe-1 vs HO spacing

Local expansion of P_x at lobe-1 apex (using the parameterization of [clover-quarks §7.6](clover-quarks.md)):

$$
P_x(u) \;\approx\; r_{\max} - \tfrac{1}{2}\, r_{\mathrm{lobe}}\,(2+\chi)^2\,\delta u^2, \qquad \delta u = u - u_{\mathrm{apex}}
$$

where χ ≡ r_saddle/r_lobe. The second derivative of U at apex (in ξ-variable with ξ = c·u, c = r_lobe(2+χ)):

$$
\left.\frac{d^2 U}{d\xi^2}\right|_{\mathrm{apex}} \;=\; \frac{2\,k_v^2}{c^2\,w_{\mathrm{apex}}^3}\,|w_{uu}|_{\mathrm{apex}} \;=\; \frac{2\,k_v^2}{r_{\mathrm{lobe}}\,(R + r_{\max})^3}
$$

Using r_lobe = ε/(2+χ) and r_max = ε (with R = 1):

$$
\left.\frac{d^2 U}{d\xi^2}\right|_{\mathrm{apex}} \;=\; \frac{2\,k_v^2\,(2+\chi)}{\varepsilon\,(1+\varepsilon)^3}
$$

Harmonic-oscillator ground-state spacing (lowest excitation above U_min):

$$
\Delta\omega^2_{\mathrm{HO}} \;=\; \sqrt{2\,U''} \;=\; \sqrt{\frac{4\,k_v^2\,(2+\chi)}{\varepsilon\,(1+\varepsilon)^3}} \;=\; \frac{2\,|k_v|}{\sqrt{\varepsilon\,(1+\varepsilon)^3/(2+\chi)}}
$$

Well depth (U at deepest barrier minus U at lobe-1 apex):

$$
U_{\max} - U_{\min} \;=\; k_v^2\left[\frac{1}{(R - (3r_{\mathrm{lobe}}+r_{\mathrm{saddle}})/2)^2} - \frac{1}{(R + r_{\max})^2}\right]
$$

For bound states to exist, we need Δω²_HO ≪ U_max − U_min.

**Evaluation at representative points** (k_v = 1/3, R = 1):

| ε | χ | r_lobe | r_max | well_depth | Δω²_HO | bound states? |
|---|---|---|---|---|---|---|
| 0.5 | 1.0 | 0.167 | 0.5 | 0.05 | 0.89 | No — HO spacing > well depth |
| 1.0 | 1.0 | 0.333 | 1.0 | 0.30 | 0.50 | Marginal |
| 1.5 | 1.0 | 0.500 | 1.5 | 1.76 | 0.24 | Yes — ~7 levels fit |
| 1.9 | 1.0 | 0.633 | 1.9 | 44 | 0.18 | Yes — many levels |
| 0.5 | 3.0 | 0.100 | 0.5 | 0.07 | 1.49 | No |
| 0.5 | 10  | 0.042 | 0.5 | 0.10 | 3.07 | No |

**Conclusion 1.** At small ε (≲ 1) the lobe-1 well is too shallow to host bound states, regardless of χ. Increasing χ deepens the well only marginally because the *barrier* moves outward in u but doesn't get much higher (it's limited by the minimum value of P_x on the profile). And increasing χ also *increases* the HO spacing through the (2+χ) factor in U''. The net effect of increasing χ at fixed ε does not produce bound states.

**Conclusion 2.** At larger ε (≳ 1.5, in R_major = 1 units), the well becomes deep enough to host multiple bound states. The well depth grows as 1/(R − r_lobe-side-min)², which diverges as ε → 2 (the geometric limit where the cross-section reaches the torus axis and the surface becomes degenerate).

---

## 4. Energy of the lobe-localized ground state

When bound states exist, the lobe-localized ground state has

$$
\omega^2_{0,\mathrm{lobe}} \;=\; U_{\min} + \tfrac{1}{2}\sqrt{2\,U''}
\;=\; \frac{k_v^2}{(1+\varepsilon)^2} \;+\; \tfrac{1}{2}\sqrt{\frac{4\,k_v^2\,(2+\chi)}{\varepsilon\,(1+\varepsilon)^3}}
$$

For ε = 1.5, χ = 1, k_v = 1/3:

$$
\omega^2_{0,\mathrm{lobe}} \;\approx\; 0.044 + 0.12 \;\approx\; 0.16
$$

Compare to the lightest whole-circumference plane-wave mode in the same Bloch sector (k_v = 1/3, lowest excitation: n = 1, m = 1):

$$
\omega^2_{\mathrm{wc,\,min}} \;=\; (n - 2m/3)^2 + (m/\varepsilon)^2 \;=\; (1/3)^2 + (1/1.5)^2 \;=\; 0.111 + 0.444 \;=\; 0.555
$$

**The lobe-localized ground state is LIGHTER than the lowest plane-wave whole-circumference mode** (ω² ≈ 0.16 vs 0.55).

This is the opposite of the user's hoped-for ordering. The reason is structural: in the Schrödinger problem, "localized in a small region" means "sitting at the bottom of a well in the effective potential U." Wells are *low* in U; the ground state in a well has *low* eigenvalue. Lobes are wells (because R + P_x is largest there, so k_v²/(R+P_x)² is smallest). So lobe-localized = low energy, not high energy.

The "1/r_lobe ~ high frequency" intuition is misleading here. That intuition would apply if the lobe acted as a tight cavity for a mode that must fit *inside* it — e.g., for an infinite-square-well problem with walls at the lobe boundaries. But in the Hill equation, the lobe is a *well*, not a cavity; the wavefunction at the well bottom can be any size, and the spacing between excitations is set by U'' (which is finite), not by 1/r_lobe.

---

## 5. Saddle-localized states — do they exist?

In the Hill potential U(u), saddle troughs are at *intermediate* U values, not extrema:

- U at saddle-2 trough: U = k_v²/(R − r_lobe)² = k_v²/(1 − ε/(2+χ))²
- U at lobe-2/3 side maxima: U = k_v²/(R − (3r_lobe+r_saddle)/2)² = k_v²/(1 − ε(3+χ)/(2(2+χ)))²
- U at lobe-1 well minimum: U = k_v²/(R + r_max)² = k_v²/(1 + ε)²

The saddle troughs are *not* local maxima of U — they're intermediate values. A wave with energy ω² > U_saddle is propagating through the saddle; only modes with ω² between U_saddle and U_lobe-2/3-side-max are quasi-localized at saddle-2 (the only true local-max of U near a saddle), and even those are in a thin energy window.

**Conclusion 3.** Saddle-localized states do *not* form a natural mode family in this Hill potential. The saddle troughs don't act as wells (they aren't local U-minima) and don't host bound states. The "saddle band" hoped for in [3-gen.md §3.3](3-gen.md) is structurally absent under Embedding A's Hill equation.

The closest thing to a saddle-localized state would be a "second-band" state — an above-the-gap state in a periodic potential, with most amplitude in the barrier regions. These exist as Bloch waves but they're not isolated to specific saddle regions; they're spread across the entire u-range with phase modulation that places nodes at the wells and antinodes at the barriers. They're not "the saddles host their own modes" in any localization sense.

---

## 6. The user's hoped-for hierarchy doesn't emerge

The user hoped for: ω_whole-circ < ω_lobe-localized < ω_saddle-localized.

What the math gives (when lobe-localized states exist at all):

$$
\omega_{0,\mathrm{lobe}} \;<\; \omega_{\mathrm{wc,\,min}}
$$

and no separate saddle-localized family exists. The ordering is **opposite** to the user's intuition, and the structure is **two-tier** (lobe-localized below plane-wave continuum) not **three-tier** (whole < lobe < saddle).

The structural reason: the Hill equation's effective potential has lobes as *wells* (low U because R+P_x is large there) and saddle-type features as intermediate U values. Localization in a well lowers the energy below the free-particle continuum, not above it. "Smaller-radius cavity → higher frequency" is the wrong intuition for this problem — the relevant cavity is the well in U, whose energy scale is set by U'' (curvature of the potential), not by the geometric radius of the lobe.

---

## 7. What would have to change to get the user's picture

Three structural modifications could in principle produce the hoped-for hierarchy:

**(a) Inverted effective potential.** If the Schrödinger problem had saddles as wells and lobes as barriers, the ordering would be: free continuum (light) → saddle-localized (heavier, sits low in saddle wells). But this requires a different Hill equation than the one derived from the corrugated-torus metric.

**(b) Hard-walled cavities.** If the lobes and saddles acted as infinite square wells (hard walls at the junctions), the ground state energy would scale as 1/(cavity-size)², giving heavier states in smaller cavities. The Hill equation's wells are *soft* (smooth U(u) near the minimum), so the eigenvalue scale is set by U'' rather than by the geometric size. To get hard-walled behavior would require a singular metric or a different dynamical equation.

**(c) Embedding B (rotation embedding).** This file analyzes Embedding A only. Embedding B has the cross-section physically rotating with θ, producing additional g_θφ cross-terms in the metric (per [clover-quarks §9.3](clover-quarks.md), B's metric derivation was deferred). The Hill equation under Embedding B would have a structurally different effective potential. Whether it admits the hoped-for hierarchy is open. Worth checking before declaring the picture impossible structurally.

---

## 8. Verdict and what to do with the numerical sweep

Under the analytical framework of [clover-mass.md §2's Hill equation reduction](clover-mass.md) (Embedding A), the user's hoped-for picture (heavier modes localized at lobes; heaviest modes at saddles) does not emerge. The Hill equation produces:

- At small ε (≲ 1): only delocalized plane-wave-like modes; no localization.
- At larger ε (≳ 1.5): lobe-localized bound states that are *lighter* than the lowest plane-wave modes (because the lobe is a well in the effective potential, not a cavity).
- No saddle-localized family in any (ε, χ) regime.

The Phase 3 numerical sweep that found no compartmentalized band structure was therefore not failing for lack of resolution or coverage; it was probing a regime in which the analytical framework predicts no such bands exist. Pushing the numerics to deep corrugation (η ≪ 0.1) would not produce them, because the mathematical structure does not support them. The Phase 3 negative result is, in retrospect, predicted by the analysis here.

**Two implications:**

1. **The "lobe-localized = generation 2, saddle-localized = generation 3" picture of [3-gen.md Mechanism A](3-gen.md) is structurally ruled out under Embedding A.** It would require either Embedding B to behave qualitatively differently (open question — see §7c) or a different dynamical equation than the Hill reduction.

2. **Embedding B is the cheapest remaining check.** If Embedding B's metric is worked out and its Hill-equivalent equation produces the same lobe-as-well structure, the picture is structurally dead and the three-generations question must move to off-sheet mechanisms (per [clover-mass §6.7](clover-mass.md), [3-gen.md §12.5](3-gen.md)). If Embedding B has a qualitatively different effective potential — e.g., saddles becoming wells or lobes becoming cavities — the picture is salvageable and worth a focused numerical pass.

The math here is at the level of *back-of-envelope WKB estimates*, not a full eigenvalue calculation. A second pass would verify with explicit numerical solution of the Hill equation at the (ε, χ) points where the analysis predicts wells deep enough for bound states (ε ≳ 1.5), looking at the *full* eigenvalue ladder with the existing wavefunction classifier to confirm: do the lobe-localized states appear where predicted, and are they below the plane-wave continuum?

---

## 9. References

- [clover-mass.md §2](clover-mass.md) — Hill equation reduction in helical coordinates
- [clover-mass.md §6.2](clover-mass.md) — Fourier structure of P_x(u) (q ≡ ±1 mod 3)
- [clover-quarks.md §7.6](clover-quarks.md) — explicit parametric form of P(u)
- [clover-quarks.md §9.3](clover-quarks.md) — Embedding A (analyzed here) vs Embedding B (deferred)
- [3-gen.md §3](3-gen.md) — user's compartmentalized-modes intuition
- [3-gen.md §12](3-gen.md) — Phase 3 negative numerical result (consistent with the analysis here)
