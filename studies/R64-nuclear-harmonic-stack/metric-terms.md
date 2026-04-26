# R64 Metric Terms — knobs, values, and constraints

Reference for every entry in the 11×11 metric used by R64 (the
post-Track-11 architecture).  For each entry: what it controls,
what value (if any) is assigned, and whether it is **pinned**
(structural, derived from first principles) or **free** (fit to
data).

Companion CSV: [`metric-terms.csv`](metric-terms.csv) — same
data, spreadsheet-friendly.

R64 inherits the R60 model-F architecture.  The Track 11
additions live entirely in (P_TUBE ↔ S) and (ALEPH ↔ S)
off-diagonals, plus the A1 charge-attribution rule for R64's
u/d quark composition.

---

## Index ordering

Identical to R60.  Smallest-scale → largest:

| Index | Symbol | Type | Scale |
|-------|--------|------|-------|
| 0 | ℵ | Compact (sub-Planck) | smallest (GRID lattice edge) |
| 1 | p_t | Compact | ~fm (proton tube) |
| 2 | p_r | Compact | ~fm (proton ring) |
| 3 | e_t | Compact | ~pm (electron tube) |
| 4 | e_r | Compact | ~pm (electron ring) |
| 5 | ν_t | Compact | ~μm to mm (neutrino tube) |
| 6 | ν_r | Compact | ~μm to mm (neutrino ring) |
| 7 | S_x | Extended | macroscopic |
| 8 | S_y | Extended | macroscopic |
| 9 | S_z | Extended | macroscopic |
| 10 | t | Extended | time (Lorentzian) |

---

## Visual layout

Symmetric metric — only upper triangle + diagonal shown.

Notation:
- `1` = identity diagonal (ℵ or S)
- `k` = per-sheet Ma diagonal scale = **2^(1/4)/(8π) ≈ 0.04732**  *(structural; R60 fit value 0.04696 is 0.75% off)*
- `k·sε` = in-sheet shear off-diagonal
- `k·(1+(sε)²)` = ring diagonal of sheet block
- `T_p, T_e, T_ν` = sheet-tube ↔ ℵ entries (signed by sheet convention)
- `R_p, R_e, R_ν` = sheet-ring ↔ ℵ entries (σ_ra prescription, derived)
- `A` = ℵ ↔ t coupling = σ_at = 4πα
- `**X**` *(new in R64)* = σ_pS_tube on the (p_t, S_i) entries
- `**Y**` *(new in R64)* = σ_aS on the (ℵ, S_i) entries via H2 prescription
- `.` = zero
- **Bold** = pinned (architectural, cannot be tuned)
- *Italic* = derived (closed-form from another pinned/free entry)
- ~strikethrough~ = tested and ruled out

```
           ℵ      p_t     p_r     e_t     e_r     ν_t     ν_r     S_x     S_y     S_z     t
         ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐
   ℵ   0 │ **1** │ -T_p  │ R_p   │ +T_e  │ R_e   │ +T_ν  │ R_ν   │ *Y*   │ *Y*   │ *Y*   │ **A** │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   p_t 1 │       │   k   │ k·sε_p│   .   │   .   │   .   │   .   │ **X** │ **X** │ **X** │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   p_r 2 │       │       │k(1+sε²)│  .   │   .   │   .   │   .   │   .   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   e_t 3 │       │       │       │   k   │ k·sε_e│   .   │   .   │   .   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   e_r 4 │       │       │       │       │k(1+sε²)│  .   │   .   │   .   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   ν_t 5 │       │       │       │       │       │   k   │ k·sε_ν│   .   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   ν_r 6 │       │       │       │       │       │       │k(1+sε²)│  .   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   S_x 7 │       │       │       │       │       │       │       │  +1   │   .   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   S_y 8 │       │       │       │       │       │       │       │       │  +1   │   .   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   S_z 9 │       │       │       │       │       │       │       │       │       │  +1   │   .   │
         ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
   t  10 │       │       │       │       │       │       │       │       │       │       │  -1   │
         └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘
```

**New in R64 (vs R60 model-F):**

- `**X**` = σ_pS_tube  ≈ −0.12505 (set to give σ_eff_tube = −116 at signature edge)
- `*Y*`  = σ_aS = b · σ_pS_tube,  with closed-form b = −8π·√α·2^(−1/4) ≈ −1.819
- `R_p, R_e, R_ν` were already in R60 via the σ_ra prescription; unchanged in R64

---

## Numerical values at R64 baseline (Track 11 architecture)

### Global knobs

| Symbol | Value | Pinned/Free | Source |
|--------|-------|:---:|--------|
| g_aa | 1 | **pinned** | R59 F59 (ℵ diagonal natural form) |
| σ_ta (magnitude) | √α ≈ 0.085425 | **pinned** | R59 F59 |
| σ_at | 4πα ≈ 0.091701 | **pinned** | R59 F59 |
| sign_e, sign_p, sign_ν | +1, −1, +1 | **pinned** | R60 sheet-sign conventions |
| k (single-k) | 2^(1/4)/(8π) ≈ 0.04732  *(R60 fit: 0.04696)* | *derived* | structural; R60 had 0.75% drift |
| σ_aS / σ_pS_tube | b = −8π·√α·2^(−1/4) ≈ −1.819 | *derived* | Phase 11d closed form (H2 prescription) |

### Per-sheet geometry (free fit values)

| Sheet | ε | s | sε | L_ring (fm) | Pinned/Free |
|-------|--:|--:|--:|---:|:---:|
| e | 397.074 | 2.004200 | 795.82 | 54.83 | free (R60 fit) |
| p (R64 Point B) | 0.2052 | 0.0250 | 0.005130 | 15.244 *(R60 value, needs R64 recalibration)* | free (Track 3 fit to nuclear chain) |
| ν | 2.0 | 0.022 | 0.044 | 1.9577 × 10¹¹ | free (R60 fit) |

**Note**: R64 changed (ε_p, s_p) from R60 model-F's (0.55, 0.16)
to Point B (0.2052, 0.025) to fit nuclear-chain data Ca→Sn within
1–2% (Track 3).  L_ring_p was carried over from R60 and is not yet
recalibrated for R64 baryons (pool item q).  K_p kinematic
prefactor in m_Ma formula = **63.629 MeV** (Point B; separate from
structural k).

### Derived ring↔ℵ entries (σ_ra prescription)

| Symbol | Formula | Value at R64 Point B |
|--------|---------|------:|
| σ_ra_e | +(sε)_e · σ_ta | +67.98 |
| σ_ra_p | −(sε)_p · σ_ta | −0.000438 |
| σ_ra_ν | +(sε)_ν · σ_ta | +0.003759 |

### New in R64: sheet-S coupling (strong-force activation)

| Symbol | Value | Pinned/Free | Source |
|--------|-------|:---:|--------|
| σ_pS_tube | ±0.125050 (signature edge) | free *(or "edge-pinned")* | Phase 11c — sets σ_eff_tube = ±116 |
| σ_aS | b · σ_pS_tube ≈ ∓0.227 | *derived* | H2 closed form (Phase 11d) |
| σ_pS_ring | 0 (zero in R64 baseline) | **pinned** | Phase 10a — adds nothing of value at edge |

**Edge-pinning interpretation**: σ_pS_tube is "free" in that we
choose to operate at the signature edge.  Once the edge methodology
is interpreted physically (pool item r), σ_pS_tube becomes pinned
to a structural value, removing one degree of freedom.

### A1 charge attribution (R64 quark composition)

| Function | Form | Pinned/Free | Source |
|----------|------|:---:|--------|
| f(n_pt, n_pr) | n_pt/6 + n_pr/4 | **pinned** | Phase 11a F11a.2 — uniquely determined by u = (1, +2) → +2/3 and d = (1, -2) → −1/3 |

---

## Pinned vs free count

### Pinned (structural / derived)

| Count | Description |
|------:|-------------|
| 1 | g_aa = 1 |
| 1 | σ_at = 4πα |
| 1 | σ_ta = √α (magnitude; signs are sheet conventions) |
| 1 | σ_ra prescription = (s·ε)·σ_ta per sheet |
| 1 | A = single-k symmetry: k = 2^(1/4)/(8π) |
| 1 | b = H2 closed form: σ_aS = −8π·√α·2^(−1/4) · σ_pS_tube |
| 1 | A1 charge attribution: f(n_pt, n_pr) = n_pt/6 + n_pr/4 |
| **7** | **total pinned constraints** |

### Free (fit to data)

| Count | Description |
|------:|-------------|
| 2 | (ε_e, s_e) — electron sheet geometry |
| 2 | (ε_p, s_p) — proton sheet geometry (Point B) |
| 2 | (ε_ν, s_ν) — neutrino sheet geometry |
| 1 | K_p — kinematic mass prefactor (Point B) |
| 1 | L_ring_e — electron-sheet ring scale |
| 1 | L_ring_p — proton-sheet ring scale (R60 carryover, needs R64 update) |
| 1 | L_ring_ν — neutrino-sheet ring scale |
| 1 | σ_pS_tube — strong-force activation magnitude (edge-pinned conjecturally) |
| **11** | **total free parameters** |

Plus 1 input constant: **α** (the fine structure constant).

### How close are we to "1 free variable (α)"?

| Stage | Free count | Notes |
|-------|----------:|-------|
| Today (R64 + Track 11) | 11 + α | Status quo |
| If Clifford embedding pins (ε, s) curves (pool item s) | 8 + α (effective 5) | 6 sheet params → 3 effective DOFs along curves |
| If σ_pS_tube edge-pinned (pool item r resolves) | 7 + α (effective 4) | Edge methodology becomes structural |
| If three-sheet → S architecture (item t + Track 12) | as above | Adds σ_eS_tube, σ_νS_tube each edge-pinned |
| If sheet-curve points derived from generation structure | 4 + α (effective 1) | Pool items k, e + sheet derivations |
| If L_ring values derived from sheet scales | 0 + α | **Goal achieved** |

(Note: gravity is **outside MaSt scope** — it lives in St + GRID.
The "1 free variable (α)" goal is for MaSt's internal-force
sector only.)

We are at **11 free parameters**.  Reducing each requires its own
structural derivation track.  Realistic intermediate target: **5
free parameters** by deriving the proton-sheet geometry and
edge-methodology interpretation (pool items l, q, r).  The
"only α" goal requires deriving generation structure on each
sheet — a major program that would supersede most of the current
fit work.

---

## Critical constraints (all satisfied at R64 baseline)

1. **Signature**: exactly one negative eigenvalue (the t direction).
2. **σ_ra prescription**: σ_ra_x = (s·ε)_x · σ_ta_x per sheet.
3. **H2 prescription**: σ_aS = −8π·√α·2^(−1/4) · σ_pS_tube
   (Phase 11d).  Required to keep α-universality preserved when
   the sheet-S strong-force coupling is activated.
4. **Single-k symmetry**: k_e = k_p = k_ν.  Empirical R60 value
   1.1803/(8π) is within 0.75% of the structural 2^(1/4)/(8π).
5. **A1 charge attribution**: at R64 quark composition, the
   p-sheet contribution to α is f(n_pt, n_pr) = n_pt/6 + n_pr/4.
   Replaces R0's raw n_pt projection.
6. **α-sum rule (multi-sheet compounds)**: α/α_target =
   (n_et − n_pt + n_νt)² for compounds touching multiple sheets.
   This is the R60 carryover formula and gives sums > 1 for
   mesons (a known limitation; pool item p).
7. **Edge methodology**: σ_eff_tube reaches Phase 7c's −116 only
   near the signature boundary (σ_pS_tube ≈ −0.12505).  Whether
   this is a structural or numerical artifact is open (pool
   item r).

---

## Historical / ruled-out entries (R64-specific)

R64 reaffirmed all R60 ruled-out entries.  Additionally, Track 10
ruled out:

| Entries | Status | Reference |
|---------|--------|-----------|
| Aleph-row removal entirely | ~breaks α magnitude (>30 orders below target)~ | Phase 10b |
| σ_ra → 0 | ~breaks signature; proton charge collapses to 0~ | Phase 10c |
| σ_pS_ring as primary strong-force channel | ~α-inert but channel-asymmetric (pp repulsive, nn attractive, pn unaffected)~ | Phase 10a, Phase 11a F11a.5 |
| Pairwise quark-quark cross term | ~factors back to (Σq)² in single-body metric — deuteron problem returns~ | Phase 11 framing analysis |

---

## See also

- [`metric-terms.csv`](metric-terms.csv) — full entry-by-entry grid
  with status flags
- [`zoo.md`](zoo.md) — particle inventory match table
- [`README.md`](README.md) — track narrative
- [`findings-11.md`](findings-11.md) — Track 11 details
  (architecture rescue)
- [`../R60-metric-11/metric-terms.md`](../R60-metric-11/metric-terms.md)
  — R60 model-F metric terms (R64 inherits this baseline)
