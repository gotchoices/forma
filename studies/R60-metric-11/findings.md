# R60 Findings — index

Detailed findings per track are in separate files below.  This
document is a brief summary only.  See [README.md](README.md) for
framings, [metric-terms.md](metric-terms.md) for the parameter
reference, and [metric-terms.csv](metric-terms.csv) for the full
entry-by-entry grid.

## Track index

| Track | Focus | F-range | Outcome | Details |
|------:|:------|:--------|:--------|:--------|
| 1 | Solver infrastructure (11D metric builder, signature check, mode energy, α extractor, least-squares fitter + smoke tests) | F1–F4 | All four smoke tests pass. Solver validated against R59 F59 and model-E at floating-point precision. | [findings-1.md](findings-1.md) |
| 2 | Electron sheet viability map — (ε_e, s_e) region under R59 F59 α | F5–F10 | Signature OK iff `s·ε ≤ 3/√2` (exact closed form). Ghost-order requires `s ≥ 3/2`. Overlap is a bounded triangle with corner (ε=√2, s=3/2). Model-E's s·ε ≈ 796 is 375× over the bound. | [findings-2.md](findings-2.md) |
| 3 | Proton sheet viability map — (ε_p, s_p) under R59 F59 α at joint e+p | F11–F16 | Joint signature bound tightens to `(sε_e)² + (sε_p)² ≤ 7/2`. **Critical surprise:** α universality breaks when shears are on (α_p/α_e drifts to 8.78× at some anchors). R59 F59's clean-metric claims don't survive shears at constant k. | [findings-3.md](findings-3.md) |
| 4 | Per-sheet diagonal compensation — free k_x per sheet to rescue α universality | F17–F21 | Joint 4×4 solve (L_e, k_e, L_p, k_p) against (m_e, m_p, α_e, α_p) converges cleanly in 66% of tested (ε, s) configs. Two failure modes: signature cliff, and α-decoupling at R53 generation resonance. | [findings-4.md](findings-4.md) |
| 5 | Proton viability under shearless electron + closed-form α-decoupling locus | F22–F26 | Derived `Q = 0 ⟺ n_r/n_t = sε + 1/(sε)` for any single-sheet mode (validated to 10⁻³¹). Key rules: **(1, 1) modes never decouple**, (1, 2) decouples at sε = 1, (1, 3) at sε ≈ 0.382 or 2.618. With shearless e, proton region is 72.7% viable. | [findings-5.md](findings-5.md) |
| 6 | Joint e+p+ν solver with ν architecturally coupled (sign_nu = +1) on R61 candidate ν-sheet geometries | F27–F31 | Joint 6×6 solve converges for 3 of 4 R61 candidates at R59 F59 defaults. **But α is mode-dependent within sheared sheets** (ν₁ targeted at α but ν₂ lands at 1.19α, ν₃ at 0.91α — 28% spread). Problem surfaces. | [findings-6.md](findings-6.md) |
| 7, 7b | Ring↔ℵ structural cancellation (add σ_ra = sε·σ_ta per sheet) + re-solve on augmented metric | F32–F38 | Cancellation works exactly: **ν-mode spread collapses from 28% to 0%**. Re-solve gives all targets at α to floating-point precision with k_e = k_p = k_ν = 0.04696 = 1.1803/(8π). Untargeted ν₂, ν₃ land at α automatically. R60 architecture validated on both axes. | [findings-7.md](findings-7.md) |
| 7c | Inter-sheet shear compatibility check — test whether activating Ma cross-sheet σ entries preserves α universality | F39–F41 | **Negative.** Most cross-sheet activations break signature OR α universality. Track 7's per-sheet fix doesn't extend freely. Cross-sheet σ is not a free knob — pool item **h** would derive an extended prescription if Track 8 needs it. | [findings-7.md](findings-7.md) |
| 7d | Magic-shear baseline re-solve — use s_e = 2, s_p = 3 to make target modes lightest on each sheet | F42–F45 | **Clean win** on e and p: joint solve converges at same single-k value (1.1803/(8π)); all targets met; α universal across sheets AND across modes; ghost ordering ✓ on e and p. ν-sheet (1, 0) ghost persists (handle via R61 filter, pool item **j**). Track 8 baseline established. | [findings-7.md](findings-7.md) |
| 8 | Compound mode search (μ, τ, neutron) on Track 7d baseline | F46–F50 | **Mixed.** Discovered compound α is exactly quantized: `α/α = (n_et − n_pt + n_νt)²`. Clean tau match (2,−6,−2,*,1,−1) at 0.37% off with α = α; clean neutron match (−1,6,−1,*,−1,−3) at 0.14% off with α = α. **Muon blocked** by mass desert 50–200 MeV — no low-order compound reaches it on this metric. Model-E tuples don't survive the L-scale transition. | [findings-8.md](findings-8.md) |

## Current R60 baseline (Track 7d magic-shear)

Working metric for Track 8 (compound modes):

| Parameter | Value |
|-----------|-------|
| Sheet inputs (ε, s) | e: (0.4, 2.0); p: (0.4, 3.0); ν: (2.0, 0.022) |
| ν mode triplet | R61 #1: (+1,+1)(−1,+1)(+1,+2) |
| k (all three sheets) | 4.696 × 10⁻² = 1.1803/(8π) |
| L_ring_e | 27,990 fm |
| L_ring_p | 15.24 fm |
| L_ring_ν | 1.96 × 10¹¹ fm |
| g_aa | 1 |
| σ_ta (tube↔ℵ) | √α (signs +1/−1/+1 for e/p/ν) |
| σ_ra (ring↔ℵ) | **derived**: σ_ra_x = (sε)_x · σ_ta_x |
| σ_at (ℵ↔t) | 4πα |

All targets (three masses, three α = α) met at floating-point
precision.  Δm²₃₁/Δm²₂₁ = 33.59 cross-checks against R49's 33.6.
Ghost ordering achieved on e and p sheets (target mode is lightest
by magic shear); ν-sheet (1, 0) ghost handled by external filter
(pool item **j**).

## Status

Tracks 1–7b complete.  Architecture validated.  Ready for Track 8
(compound modes — μ, τ, neutron, hadrons) on the above baseline.
