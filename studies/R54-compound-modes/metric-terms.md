# R54 Metric Terms — Complete 9×9 Reference

All values for the model-E geometry.

## Visual layout

The 9×9 symmetric metric.  Lower-left mirrors upper-right.
Each cell shows the entry name, its physics role, and value/status.

```
                e-tube    e-ring    ν-tube    ν-ring    p-tube    p-ring    S_x       S_y       S_z
              ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
   e-tube     │ L₁²     │         │         │         │         │         │         │         │         │
              │ 4717 fm │  s_e    │    0    │    0    │    0    │    0    │    0    │    0    │    0    │
              │         │ GEN     │ inact.  │ inact.  │ inact.  │ inact.  │ inact.  │ inact.  │ inact.  │
              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   e-ring     │         │ L₂²     │         │         │         │         │         │         │         │
              │         │ 11.9 fm │  σ₂₃   │  σ₂₄   │  σ₂₅   │  σ₂₆   │  −σ_α  │  −σ_α  │  −σ_α  │
              │         │         │ OPEN    │ OPEN    │ NEUTRON │ NEUTRON │  CHARGE │  CHARGE │  CHARGE │
              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   ν-tube     │         │         │ L₃²     │         │         │         │         │         │         │
              │         │         │ 2e11 fm │  s_ν   │    0    │    0    │    0    │    0    │    0    │
              │         │         │         │ GEN     │ inact.  │ inact.  │ inact.  │ inact.  │ inact.  │
              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   ν-ring     │         │         │         │ L₄²     │         │         │         │         │         │
              │         │         │         │ 4e10 fm │  σ₄₅   │  σ₄₆   │    0    │    0    │    0    │
              │         │         │         │         │ NEUTRON │ NEUTRON │ NEUTRAL │ NEUTRAL │ NEUTRAL │
              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   p-tube     │         │         │         │         │ L₅²     │         │         │         │         │
              │         │         │         │         │ 2.45 fm │  s_p   │  +σ_α  │  +σ_α  │  +σ_α  │
              │         │         │         │         │         │ GEN+α  │  CHARGE │  CHARGE │  CHARGE │
              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   p-ring     │         │         │         │         │         │ L₆²     │         │         │         │
              │         │         │         │         │         │ 4.45 fm │  +σ_α  │  +σ_α  │  +σ_α  │
              │         │         │         │         │         │         │  CHARGE │  CHARGE │  CHARGE │
              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   S_x        │         │         │         │         │         │         │    1    │         │         │
              │         │         │         │         │         │         │  flat   │    0    │    0    │
              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   S_y        │         │         │         │         │         │         │         │    1    │         │
              │         │         │         │         │         │         │         │  flat   │    0    │
              ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
   S_z        │         │         │         │         │         │         │         │         │    1    │
              │         │         │         │         │         │         │         │         │  flat   │
              └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

**Legend:**

| Label | Meaning | Count |
|---|---|---|
| **GEN** | In-sheet shear → generation structure | 3 |
| **GEN+α** | s_p: generation structure + α consistency at small ε | 1 |
| **NEUTRON** | Cross-sheet → compound modes (neutron, hadrons) | 4 active |
| **OPEN** | Active cross-sheet, not yet constrained | 2 |
| **CHARGE −** | Ma-S coupling, negative sign → negative charge | 3 |
| **CHARGE +** | Ma-S coupling, positive sign → positive charge | 6 |
| **NEUTRAL** | Zero Ma-S coupling → electrically dark | 3 |
| **inact.** | Dimension too large → entry ≈ 0 | 12 |
| **flat** | Flat 3D space | 6 |

**Reading the layout:**

- **Diagonal** (top-left to bottom-right): circumferences L₁–L₆ and flat S
- **GEN entries** (just off diagonal within each sheet): s_e, s_ν, s_p
- **NEUTRON cluster**: where e-ring row and ν-ring row cross the p columns
- **CHARGE columns** (rightmost 3): the Ma-S block, with **−** signs in the e rows and **+** signs in the p rows
- **NEUTRAL row**: ν-ring → S is zero (neutrinos don't couple to EM)
- **Inactive L-shape**: e-tube row and ν-tube row are almost entirely zero (dimensions too large to couple)
- The active physics lives in 4 dimensions: **e-ring, ν-ring, p-tube, p-ring**

---

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
| 28–30 | σ(e-ring, S) | e-ring → S_{x,y,z} | ~ **−**O(α) | **working assumption (NEGATIVE sign → negative charge)** |
| 31–33 | σ(ν-tube, S) | ν-tube → S_{x,y,z} | ≈ 0 | inactive (L₃ huge) |
| 34–36 | σ(ν-ring, S) | ν-ring → S_{x,y,z} | ≈ 0 | **zero (neutrinos electrically neutral)** |
| 37–39 | σ(p-tube, S) | p-tube → S_{x,y,z} | ~ **+**O(α) | **working assumption (POSITIVE sign → positive charge)** |
| 40–42 | σ(p-ring, S) | p-ring → S_{x,y,z} | ~ **+**O(α) | **working assumption (POSITIVE sign → positive charge)** |

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
