# R54 Status and Scorecard

**Study status:** Framed — waiting for R53 Tracks 5–7

---

## Parameter budget

### Inputs (from experiment — 4 total, unchanged from model-D)

| # | Parameter | Value | Sets |
|---|-----------|-------|------|
| 1 | m_e | 0.51099895 MeV | L_ring_e |
| 2 | m_p | 938.27208 MeV | L_ring_p (or predicted from quarks) |
| 3 | Δm²₂₁ | 7.53 × 10⁻⁵ eV² | L_ring_ν |
| 4 | α | 1/137.036 | TBD — relocated from in-sheet shear |

### Sheet geometry (from R53 — 6 parameters, 3 sheets × 2 each)

| # | Parameter | Value | Source | Status |
|---|-----------|-------|--------|--------|
| 5 | ε_e | ~330 or TBD | R53 Track 1 | **pending precision** |
| 6 | s_e | ~3.004 or TBD | R53 Track 1 | **pending precision** |
| 7 | ε_ν | 5.0 | R49 (Family A) | constrained |
| 8 | s_ν | 0.02199 | R26 (Δm² ratio) | constrained |
| 9 | ε_p | ~0.5 or TBD | R53 Track 4 | **pending precision** |
| 10 | s_p | ~2.0 or TBD | R53 Track 4 | **pending precision** |

### Cross-dimensional coupling (R54 territory — 12 individual entries)

The metric is symmetric (G_ij = G_ji), so 15 off-diagonal entries
exist.  3 are the within-sheet shears (above).  The remaining 12:

```
         e_tube  e_ring  ν_tube  ν_ring  p_tube  p_ring
e_tube  [  ·      s_e     σ₁₃     σ₁₄     σ₁₅     σ₁₆  ]
e_ring  [         ·       σ₂₃     σ₂₄     σ₂₅     σ₂₆  ]
ν_tube  [                  ·      s_ν     σ₃₅     σ₃₆  ]
ν_ring  [                          ·      σ₄₅     σ₄₆  ]
p_tube  [                                  ·      s_p   ]
p_ring  [                                          ·    ]
```

**e ↔ ν coupling (4 entries):**

| # | Entry | Couples | Value | Status |
|---|-------|---------|-------|--------|
| 11 | σ₁₃ | e-tube ↔ ν-tube | 0 | **free** |
| 12 | σ₁₄ | e-tube ↔ ν-ring | 0 | **free** |
| 13 | σ₂₃ | e-ring ↔ ν-tube | 0 | **free** |
| 14 | σ₂₄ | e-ring ↔ ν-ring | 0 | **free** |

**e ↔ p coupling (4 entries):**

| # | Entry | Couples | Value | Status |
|---|-------|---------|-------|--------|
| 15 | σ₁₅ | e-tube ↔ p-tube | 0 | **free** |
| 16 | σ₁₆ | e-tube ↔ p-ring | 0 | **free** |
| 17 | σ₂₅ | e-ring ↔ p-tube | ≈ −0.06 | **soft — neutron is near-miss, not a pin** |
| 18 | σ₂₆ | e-ring ↔ p-ring | ≈ −0.03 | **soft — neutron is near-miss, not a pin** |

**ν ↔ p coupling (4 entries):**

| # | Entry | Couples | Value | Status |
|---|-------|---------|-------|--------|
| 19 | σ₃₅ | ν-tube ↔ p-tube | 0 | **free** |
| 20 | σ₃₆ | ν-tube ↔ p-ring | 0 | **free** |
| 21 | σ₄₅ | ν-ring ↔ p-tube | 0 | **free** |
| 22 | σ₄₆ | ν-ring ↔ p-ring | 0 | **free** |

Note: model-D collapsed each 2×2 block to one scalar (σ_ep,
σ_eν, σ_νp).  R54 uses all 12 individually because the
directional selectivity (e.g., e-tube↔p-tube ≠ e-ring↔p-ring)
is likely what differentiates compound modes.

### Ma-S coupling (not yet modeled — 18 parameters)

| # | Parameter | Couples | Value | Status |
|---|-----------|---------|-------|--------|
| 23–28 | g(Ma_i, S_x) | each Ma dim ↔ S_x | 0 | **unexplored** |
| 29–34 | g(Ma_i, S_y) | each Ma dim ↔ S_y | 0 | **unexplored** |
| 35–40 | g(Ma_i, S_z) | each Ma dim ↔ S_z | 0 | **unexplored** |

α = 1/137 may live in these entries (R53 F7).

### Summary

| Category | Count | Status |
|----------|------:|--------|
| Measured inputs | 4 | fixed |
| Sheet geometry (ε, s) | 6 | **R53 pending precision** |
| Cross-dimensional (individual) | 12 | **R54 free** |
| Ma-S coupling | 18 | unexplored (default 0) |
| **Total metric parameters** | **40** | |
| **Active in R54** | **22** | 4 fixed + 6 from R53 + 12 free |
| **Soft-constrained** | **2** | σ₂₅ ~ −0.06, σ₂₆ ~ −0.03 — region where neutron near-miss exists. NOT pinned: neutron is unstable (τ = 880 s) so it SHOULD be slightly off-eigenmode. These values indicate the neighborhood, not the address. |
| **Note** | The neutron constrains a REGION of (σ₂₅, σ₂₆) space, not a point. Stable particles (proton, electron) should provide hard pins. Other constraints (e.g., Λ baryon, Σ, hadron spectrum) may tighten the region later. |

---

## Particle scorecard

### Tier 1: Must match (stable or near-stable)

| Particle | Mass (MeV) | Q | Spin | Mode | Status |
|----------|-----------|---|------|------|--------|
| **electron** | 0.511 | −1 | ½ | (1, 2, 0, 0, 0, 0) | **R53 Sol D — input** |
| **proton** | 938.272 | +1 | ½ | (0, 0, 0, 0, 1, 3) | **R54 — match at σ=0 (input); shifts +1.3 MeV at neutron-optimized σ** |
| **neutron** | 939.565 | 0 | ½ | (−1, −2, ν, ν, −1, −3) | **R54 — near-miss at ~939.6 MeV in σ₂₅/σ₂₆ neighborhood; SHOULD be off-eigenmode (unstable)** |
| **ν₁, ν₂, ν₃** | ~meV | 0 | ½ | (1,1), (−1,1), (1,2) on ν | R49 — match |

### Tier 2: Should match (unstable leptons, light hadrons)

| Particle | Mass (MeV) | Q | Spin | Mode | Status |
|----------|-----------|---|------|------|--------|
| **muon** | 105.658 | −1 | ½ | (1, 1, −2, −2, 0, 0) | **R54 Track 1c — 0.83% (e+ν compound)** |
| **tau** | 1776.86 | −1 | ½ | (3, −6, 2, −2, 2, 3) | **R54 Track 1c — 0.05% (e+ν+p compound)** |
| **pi±** | 139.570 | ±1 | 0 | (−1, n₂, ±1, n₄, 0, 0) | **spin-charge SOLVED (e+ν dual tube); mass at 104.8 MeV (25% off)** |
| **pi⁰** | 134.977 | 0 | 0 | (0, −1, 0, n₄, 0, 0) | **104.3 MeV (23% off); 30% boost needed from cross-shears** |
| **K⁺** | 493.677 | +1 | — | (−1, −6, −2, 2, 0, 1) | **R54 Track 1c — 1.77%** |
| **K⁰** | 497.611 | 0 | 0 | (0, −4, −2, 2, 0, 1) | **R54 Track 1c — 1.04%** |

### Tier 3: Would like to match (broader inventory)

| Particle | Mass (MeV) | Q | Spin | Status |
|----------|-----------|---|------|--------|
| Λ | 1115.7 | 0 | ½ | pending |
| Σ⁺ | 1189.4 | +1 | ½ | pending |
| Ξ⁰ | 1314.9 | 0 | ½ | pending |
| Ω⁻ | 1672.5 | −1 | 3/2 | pending |
| η | 547.9 | 0 | 0 | pending |
| η′ | 957.8 | 0 | 0 | pending |
| ρ | 775.3 | ±1 | 1 | pending |
| Δ | 1232 | varies | 3/2 | pending |
| φ | 1019.5 | 0 | 1 | pending |

### Tier 4: Quarks (if they emerge as fundamental sheet modes)

| Quark | Mass (MeV) | Mode candidate | Status |
|-------|-----------|----------------|--------|
| up | 2.16 | (1, 3) on p-sheet | R53 Track 4 |
| down | 4.67 | TBD (compound?) | R54 Track 2 |
| charm | 1270 | (−1, 3) on p-sheet | R53 Track 4 |
| strange | 93.4 | TBD (compound?) | R54 Track 2 |
| top | 172,760 | (3, 9) on p-sheet | R53 Track 4 |
| bottom | 4180 | TBD (compound?) | R54 Track 2 |

---

## Decision log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-04-10 | R53: in-sheet shear sets generations, not α | α must be relocated to Ma-S cross terms (F7) |
| 2026-04-10 | R53: electron may be (1,3) not (1,2) | Shear resonance at s≈3 gives e/μ/τ (F1) |
| 2026-04-10 | R53: up quark = (1,3) at ε=0.5, s=2 | Thin-torus solution; u and proton share mode (F21) |
| 2026-04-10 | R54: proton mass is the primary test | Proton/neutron are the proof; quarks are the mechanism |
| 2026-04-10 | R54: down quarks may be compound e+p modes | Cross-shear provides 2nd degree of freedom (Q116) |
| 2026-04-10 | R54: σ₁₅, σ₁₆ go singular at R53 geometry | e-tube too large (L₁ ≈ 4700 fm); only σ₂₅, σ₂₆ are active e-p entries |
| 2026-04-10 | R54: neutron = (−1,−2,ν,ν,−1,−3) at 0.012 MeV off | e+ν+p compound = electron + neutrino + proton fused; decays to its components |
| 2026-04-10 | R54: proton-neutron tension | σ₂₅, σ₂₆ that nail neutron also shift proton by +1.3 MeV; resolved by using ν-p entries instead |
| 2026-04-10 | R54: ν-p entries decouple p from n | σ₄₅, σ₄₆ move neutron without moving proton (proton has no ν content) |
| 2026-04-10 | R54: 15/20 particles within 2% | Full inventory at σ₄₅=−0.18, σ₄₆=+0.10; Λ, η′, proton essentially exact |
| 2026-04-10 | R54: π± spin-charge constraint SOLVED | Two odd tube windings (e+ν sheets) give spin_count=2→spin 0 with Q=±1; mass still at 104.8 MeV (25% off target) |
| 2026-04-10 | R54: pion mass gap = 30% boost needed | All pion candidates at ~104 MeV (1× e-ring quantum); need cross-shear to reach 135 MeV |
