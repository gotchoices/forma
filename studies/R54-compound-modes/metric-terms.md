# R54 Metric Terms — Complete 9×9 Reference

All values for the model-E geometry.

## Diagonal entries (9)

| # | Dimension | L (fm) | L² (fm²) | Source |
|---|-----------|--------|----------|--------|
| 1 | e-tube | 4716.7 | 2.225 × 10⁷ | ε_e × L_ring_e |
| 2 | e-ring | 11.882 | 141.18 | from m_e, μ_e(1,2) |
| 3 | ν-tube | 2.119 × 10¹¹ | 4.491 × 10²² | ε_ν × L_ring_ν |
| 4 | ν-ring | 4.238 × 10¹⁰ | 1.796 × 10²¹ | from Δm²₂₁ |
| 5 | p-tube | 2.450 | 5.999 | ε_p × L_ring_p |
| 6 | p-ring | 4.454 | 19.834 | from m_p, μ_p(1,3) |
| 7 | S_x | — | 1 (flat) | assumption |
| 8 | S_y | — | 1 (flat) | assumption |
| 9 | S_z | — | 1 (flat) | assumption |

## Off-diagonal: within-sheet shears (3)

| # | Entry | Couples | Value | Ratio | Source |
|---|-------|---------|-------|-------|--------|
| 10 | s_e | e-tube ↔ e-ring | 2.004200 | ≈ 2 + 1/238 | R53 (lepton generations) |
| 11 | s_ν | ν-tube ↔ ν-ring | 0.02199 | ≈ 1/45.5 | R26 (Δm² ratio = 33.6) |
| 12 | s_p | p-tube ↔ p-ring | 0.162037 | ≈ 1/6.17 | R19 (α = 1/137 at ε_p = 0.55) |

All three positive (same shear direction).

## Off-diagonal: cross-sheet (12)

### e ↔ ν block

| # | Entry | Couples | Value | Status |
|---|-------|---------|-------|--------|
| 13 | σ₁₃ | e-tube ↔ ν-tube | 0 | inactive (both dimensions huge) |
| 14 | σ₁₄ | e-tube ↔ ν-ring | 0 | inactive (e-tube huge) |
| 15 | σ₂₃ | e-ring ↔ ν-tube | 0 | active but open |
| 16 | σ₂₄ | e-ring ↔ ν-ring | 0 | active but open |

### e ↔ p block

| # | Entry | Couples | Value | Status |
|---|-------|---------|-------|--------|
| 17 | σ₁₅ | e-tube ↔ p-tube | 0 | inactive (e-tube huge) |
| 18 | σ₁₆ | e-tube ↔ p-ring | 0 | inactive (e-tube huge) |
| 19 | σ₂₅ | e-ring ↔ p-tube | 0 | active; neutron lever |
| 20 | σ₂₆ | e-ring ↔ p-ring | 0 | active; neutron lever |

### ν ↔ p block

| # | Entry | Couples | Value | Status |
|---|-------|---------|-------|--------|
| 21 | σ₃₅ | ν-tube ↔ p-tube | 0 | inactive (ν-tube huge) |
| 22 | σ₃₆ | ν-tube ↔ p-ring | 0 | inactive (ν-tube huge) |
| 23 | σ₄₅ | ν-ring ↔ p-tube | −0.18 | soft (neutron neighborhood) |
| 24 | σ₄₆ | ν-ring ↔ p-ring | +0.10 | soft (neutron neighborhood) |

**6 active entries** (σ₂₃, σ₂₄, σ₂₅, σ₂₆, σ₄₅, σ₄₆).
**6 inactive** (involve e-tube or ν-tube — dimensions too large).

## Off-diagonal: Ma ↔ S (18)

**Working assumption:** the Ma-S coupling determines α = 1/137.
The exact values require a derivation (see R55 framing).

Each Ma dimension has a coupling to each S direction.  Spatial
isotropy (no preferred direction in S) means the coupling to
S_x = S_y = S_z for each Ma dimension, reducing 18 → 6.

Of those 6, the 2 inactive Ma dimensions (e-tube, ν-tube)
contribute negligibly, leaving 4 effective Ma-S entries:

| # | Entry | Couples | Estimated | Status |
|---|-------|---------|-----------|--------|
| 25–27 | σ(e-tube, S) | e-tube → S_{x,y,z} | ≈ 0 | inactive (L₁ huge) |
| 28–30 | σ(e-ring, S) | e-ring → S_{x,y,z} | ~ O(α) | **working assumption** |
| 31–33 | σ(ν-tube, S) | ν-tube → S_{x,y,z} | ≈ 0 | inactive (L₃ huge) |
| 34–36 | σ(ν-ring, S) | ν-ring → S_{x,y,z} | ~ O(α) | **working assumption** |
| 37–39 | σ(p-tube, S) | p-tube → S_{x,y,z} | ~ O(α) | **working assumption** |
| 40–42 | σ(p-ring, S) | p-ring → S_{x,y,z} | ~ O(α) | **working assumption** |

## Off-diagonal: within S (3)

| # | Entry | Value | Source |
|---|-------|-------|--------|
| 43 | S_x ↔ S_y | 0 | flat space |
| 44 | S_x ↔ S_z | 0 | flat space |
| 45 | S_y ↔ S_z | 0 | flat space |

## Summary

| Category | Count | Determined | Open |
|----------|------:|----------:|-----:|
| Diagonal | 9 | 9 | 0 |
| Internal shears | 3 | 3 | 0 |
| Cross-sheet | 12 | 8 (6 inactive + 2 soft) | 4 |
| Ma-S coupling | 18 | 6 inactive | 12 (working assumption ~ O(α)) |
| Within S | 3 | 3 | 0 |
| **Total** | **45** | **29** | **16** |

Of the 16 open entries: 12 are Ma-S (constrained by α, pending
derivation) and 4 are active cross-sheet (σ₂₃, σ₂₄, σ₂₅, σ₂₆).
