# R47 Findings

## Track 1: Proton (1,3) mode — ε sweep

### Setup

- Target mode: (1,3) — proton hypothesis
- Ghosts: (1,1) and (1,2)
- 3 slots on the inner equator (θ₁ = 180°), placed at the
  target mode's standing-wave nodes (shear-adjusted: every-other
  node at k × 360°/q_eff for k = 0, 1, 2)
- Swept ε from 0.05 to 0.95 (37 points)
- At each ε, solved shear s from α(ε, s) = 1/137.036 with
  q_eff = 3 − s, using μ = √(1/ε² + q²) (matching Torus Lab
  and R46 convention)

### Key results

| ε range | (1,3) target | (1,2) ghost | (1,1) ghost | Notes |
|---------|-------------|-------------|-------------|-------|
| 0.05–0.45 | **100%** | **4.8–5.7%** | **7.0–7.4%** | Both ghosts killed; target perfect |
| 0.47 | 100% | 6.2% | 7.4% | (1,2) starting to leak |
| 0.50 | 100% | 12.4% | 7.4% | (1,2) above 10% |
| 0.55 | 100% | 43.0% | 7.4% | (1,2) surviving |
| 0.65 | 100% | 93.3% | 11.4% | Both ghosts surviving |
| 0.80+ | 100% | ~100% | 90%+ | Slot geometry loses filtering power |

### Shear and q_eff

Shear varies with ε (unlike the buggy first run where it was flat):
- ε = 0.05: s = 0.032, q_eff = 2.968
- ε = 0.30: s = 0.069, q_eff = 2.931
- ε = 0.50: s = 0.078, q_eff = 2.922
- ε = 0.95: s = 0.084, q_eff = 2.916

At small ε the 1/ε² term in μ dominates, requiring less shear
to achieve α = 1/137.

### Charge overlap

|C(1,3)| decreases monotonically with ε:
- ε = 0.05: C = −1.77
- ε = 0.30: C = −1.57
- ε = 0.50: C = −0.94
- ε = 0.70: C = −0.46
- ε = 0.95: C = −0.21

Sign flip near ε ≈ 0.72 from tube profile symmetry crossing.

### Absolute dimensions (from m_p)

The proton's reduced Compton wavelength is ƛ_p = 0.2103 fm.
With the corrected formula μ = √(1/ε² + q²), the dimensions
now vary significantly with ε:

| ε | a (fm) | R (fm) | Area (fm²) | μ |
|---|--------|--------|------------|---|
| 0.05 | 0.677 | 13.54 | 361.6 | 20.22 |
| 0.10 | 0.349 | 3.49 | 48.1 | 10.43 |
| 0.20 | 0.194 | 0.97 | 7.4 | 5.81 |
| 0.30 | 0.149 | 0.50 | 2.9 | 4.44 |
| 0.40 | 0.129 | 0.32 | 1.6 | 3.85 |
| 0.50 | 0.119 | 0.24 | 1.1 | 3.54 |

For comparison, the proton charge radius (experiment) is
r_ch ≈ 0.84 fm.  At ε ≈ 0.05, the tube radius a ≈ 0.68 fm
is close to r_ch.  At ε ≈ 0.25, the ring radius R ≈ 0.66 fm
is in the same range.  Which (if either) corresponds to the
measured charge radius depends on how the 3D embedding maps
the sheet geometry to an observable radius.

### Extended mode survival at ε = 0.30

| Mode | Survival | Status |
|------|----------|--------|
| (1,1) | 7.4% | ✗ killed |
| (1,2) | 5.0% | ✗ killed |
| (1,3) | 100.0% | ✓ survives |
| (1,4) | 5.0% | ✗ killed |
| (1,5) | 11.8% | ⚠ weakened |
| (1,6) | 94.0% | ✓ survives |
| (1,7) | 63.9% | ⚠ weakened |

The 3-slot geometry at target nodes kills (1,1), (1,2),
and (1,4) — three ghosts with three slots.  (1,6) survives
because its q_eff is nearly 2× the target's, so slot positions
coincide with its nodes too.

### Torus Lab cross-check

When using the electron model in Torus Lab with 3 manually
placed slots at (0°, 124°, 250°), the user observed the same
qualitative behavior: (1,1) and (1,2) killed, (1,3)+ healthy.
The numerical survival values differ slightly because Torus Lab
uses the electron's α formula (q = 2−s, giving s ≈ 0.008)
rather than the proton's (q = 3−s, giving s ≈ 0.03–0.08).
With the electron's small shear, q_eff ≈ 2.99 for (1,3),
so 120° spacing nearly perfectly preserves it.  The qualitative
result is robust across both shear regimes.

### Findings table

| ID | Finding |
|----|---------|
| F1 | The (1,3) proton mode achieves 100% survival at shear-adjusted 3-slot positions across the full ε range (0.05–0.95). |
| F2 | Both ghosts (1,1) and (1,2) are killed (< 8%) for ε ≤ 0.47.  Viable range: **ε ∈ [0.05, 0.47]**. |
| F3 | The (1,4) ghost is also killed (~5%) at small ε — 3 slots kill 3 ghosts. |
| F4 | Shear varies from s = 0.032 (ε = 0.05) to s = 0.084 (ε = 0.95).  The 1/ε² term in μ makes the α formula ε-sensitive. |
| F5 | Tube radius ranges from a ≈ 0.68 fm (ε = 0.05) to a ≈ 0.10 fm (ε = 0.95). Ring radius R = a/ε. Both are in the sub-fm to fm range — consistent with proton scale. |
| F6 | At ε ≈ 0.05, a ≈ 0.68 fm (close to proton charge radius 0.84 fm).  At ε ≈ 0.25, R ≈ 0.66 fm.  The charge radius connection needs further study. |
| F7 | (1,6) survives at ~94% — its q_eff is ~2× the target's, aligning with slot node positions. |
| F8 | Ghost killing is qualitatively robust: same behavior seen in Torus Lab with electron shear and in the proton-specific calculation. |
