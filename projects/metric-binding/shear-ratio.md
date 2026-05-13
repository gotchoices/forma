# Sheet parameters from numerical testing

Aspect ratio ε ≡ L_u / L_w and shear σ_uw are the two metric parameters that distinguish particle sheets in this framework (see [README §"Coordinates and notation"](README.md) and [Chapter 1](01-foundation.md)). This file records the (ε, σ_uw) combinations that the production R-track studies (notably [R60-metric-11](../../studies/R60-metric-11/), [R63-proton-tuning](../../studies/R63-proton-tuning/), and [R64-nuclear-harmonic-stack](../../studies/R64-nuclear-harmonic-stack/)) have estimated as producing the distinctive qualities of each candidate particle sheet.

These are *empirical estimates* from numerical model-G fitting against multi-observable target sets (mass spectra, oscillation behaviour, nuclear binding curves), not parameters derived from the metric-charge framework's own structural arguments. They are reported here for cross-reference; metric-charge itself treats (ε, σ_uw) as free parameters of each sheet.

Note on naming: the studies abbreviate the shear coefficient as **s**, consistent with the closed-form mass spectrum

<!-- μ² = (n_t / ε)² + (n_r − s · n_t)² -->
$$
\mu^2 \;=\; \left(\frac{n_t}{\varepsilon}\right)^2 \;+\; (n_r - s\, n_t)^2
$$

Within metric-charge this same coefficient is the σ_uw cross-term of the sheet metric.

## Current values

| Sheet | ε (aspect) | σ_uw (shear) | Source | Status |
|---|---|---|---|---|
| **Electron** | 397.074 | 2.004 | R60 model-F fit | Pinned; carried unchanged into R64 |
| **Neutrino** | 2.0 | 0.022 | R60 (oscillation constraints) | Pinned; not revisited in R64 |
| **Proton (Point A)** | 0.073 | 0.194 | R64 Track 1 (deuteron + p/n mass ratio at m_u ≈ 315 MeV) | Conjectured |
| **Proton (Point B)** | 0.2052 | 0.025 | R64 Track 3 (Ca → Sn binding curve) | Conjectured |

## Notes

- The electron sheet is structurally distinguished by an extreme aspect ratio (ε ≈ 400 — the L_u direction roughly 400× longer than L_w) and a substantial shear (σ_uw ≈ 2). These together place the electron sheet in the "very thin / strongly sheared" corner of the (ε, σ_uw) plane.
- The neutrino sheet is near-square (ε ≈ 2) with very small shear (σ_uw ≈ 0.022). Its observable behaviour comes through the mass-mixing oscillation channel rather than charge-coupling channels.
- The proton sheet is the unconverged case. The two Point-A / Point-B fits each match a different observable cleanly but cannot be reconciled: Point A under-binds heavy nuclei by ~7×, Point B over-binds the deuteron by ~8×. R64 leaves the unification as an open architectural question; some Pool items (Clifford embedding) may bear on its resolution.

The metric-charge project's structural arguments do not, on their own, force any of these values. They are reported here as the current best numerical estimates from the production studies, useful when downstream chapters or follow-up projects need a concrete (ε, σ_uw) point to evaluate against.
