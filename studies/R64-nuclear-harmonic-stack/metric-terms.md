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

### New in R64: sheet-S coupling — **status reduced post audit**

| Symbol | Value | Pinned/Free | Source |
|--------|-------|:---:|--------|
| σ_pS_tube | 0 in baseline; tested at ±0.125 (Track 11) | **untested as architectural feature** | Track 11 attempt; ruled out as strong-force mechanism (Tracks 13b, 17) |
| σ_aS | 0 in baseline; H2 prescription if σ_pS_tube active | derived from σ_pS_tube via b = −√α/k_p | Phase 11d (closed form), Phase 8 (α-magnitude reading) |
| σ_pS_ring | 0 in R64 baseline | **pinned** | Phase 10a — α-inert; channel-asymmetric |

**Status of σ_pS_tube + H2 (post audit, April 2026):**

The Track 11 reading — that σ_pS_tube + H2 at the signature edge
delivers the strong force — has been formally walked back.  Two
independent tests rule it out as a strong-force mechanism:

- **Track 13b** (QM gate): the V(r) trough at σ_eff_tube = −116
  produces 3 bound pn states (vs 1 deuteron observed), bound
  nn/pp (vs unbound), B(²H) ≈ 30 MeV (vs 2.22 observed) at both
  Points A and B.
- **Track 17** (moderate σ_pS_tube sweep): at any σ_pS_tube
  inside the signature band but away from the edge, V(r) is
  REPULSIVE everywhere (kinetic-style term dominates).  No
  attractive trough forms.  σ_pS_tube cannot be the volume-
  binding mechanism in any honest regime.

**What survives**: the H2 closed-form b = −√α/k_p as a
universality-preservation prescription if σ_pS_tube were ever
activated.  The math is real; the application as strong-force
mechanism is what's ruled out.

**Open**: pool item r (edge methodology — physical or regulator
artifact?), pool item m (Yukawa propagator with geometric
reading as compactification cutoff), pool item v (whether σ_pS
plays a role in magnetic anomaly via second-order effects).

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
| 1 | k empirical = 1.1803/(8π) (single-k symmetry).  *2^(1/4) speculation walked back per review.md.* |
| 1 | b = H2 closed form: σ_aS = −√α/k_p · σ_pS_tube  *(if σ_pS_tube ever activated)* |
| 1 | A1 charge attribution: f(n_pt, n_pr) = n_pt/6 + n_pr/4 |
| **7** | **total pinned constraints** |

### Free (fit to data)

| Count | Description |
|------:|-------------|
| 2 | (ε_e, s_e) — electron sheet geometry |
| 2 | (ε_p, s_p) — proton sheet geometry (Point A or Point B; **no unified value**) |
| 2 | (ε_ν, s_ν) — neutrino sheet geometry |
| 1 | K_p — kinematic mass prefactor (different at Point A vs B) |
| 1 | L_ring_e — electron-sheet ring scale |
| 1 | L_ring_p — proton-sheet ring scale (R60 carryover, needs R64 update — pool item q) |
| 1 | L_ring_ν — neutrino-sheet ring scale |
| **10** | **total free parameters** *(was 11 before σ_pS_tube was ruled out as architectural feature)* |

Plus 1 input constant: **α** (the fine structure constant).

**Note**: σ_pS_tube was previously listed here as "free, conjecturally
edge-pinned."  Post audit (Tracks 13b, 17), σ_pS_tube is reduced to
"tested and ruled out as strong-force mechanism."  It's not a
free parameter we activate; it's a candidate we eliminated.  The
strong-force mechanism is currently **unaccounted for** at the
metric level (above the deuteron compound mode).

### How close are we to "1 free variable (α)"?

| Stage | Free count | Notes |
|-------|----------:|-------|
| Today (post audit) | 10 + α | σ_pS_tube ruled out, not a free param |
| If Clifford embedding pins (ε, s) curves (pool item s) | 7 + α (effective 4) | 6 sheet params → 3 effective DOFs along curves |
| If a unified working point exists (pools k, l, ae) | as above | (ε_p, s_p, K_p) at one point satisfying both deuteron AND nuclear chain — currently no such point |
| If sheet-curve points derived from generation structure | 4 + α (effective 1) | Pool items k, e + sheet derivations |
| If L_ring values derived from sheet scales | 0 + α | **Goal achieved** |

(Note: gravity is **outside MaSt scope** — it lives in St + GRID.
The "1 free variable (α)" goal is for MaSt's internal-force
sector only.)

We are at **10 free parameters** post audit.  Reducing each
requires its own structural derivation track.  Realistic
intermediate target: **~5 free parameters** by deriving the
proton-sheet geometry (pool items l, q) and Clifford embedding
(pool s).  The "only α" goal requires deriving generation
structure on each sheet — a major program that would supersede
most of the current fit work.

**Important caveat**: even with 10 free + α, the strong-force
volume term (~7 MeV/n for heavy nuclei) is **not delivered by
any pinned or free parameter currently in the architecture**.
Resolving this requires either a new metric mechanism (pool m
revival), a new compound-mode formula (pool ae extension), or
acceptance of a nuclear-physics overlay outside MaSt.

---

## Critical constraints (all satisfied at R64 baseline)

1. **Signature**: exactly one negative eigenvalue (the t direction).
2. **σ_ra prescription**: σ_ra_x = (s·ε)_x · σ_ta_x per sheet.
3. **H2 prescription** (if σ_pS_tube ever activated): σ_aS =
   −√α/k_p · σ_pS_tube ≈ −1.81892 · σ_pS_tube (Phase 11d).
   Required to keep α-universality preserved.
   *(Note: the original write-up promoted a 2^(1/4) speculation
   to "structurally clean form."  This is walked back per
   review.md Concern 5; the supported form is empirical k_p.)*
4. **Single-k symmetry**: k_e = k_p = k_ν.  Empirical R60 value
   1.1803/(8π) ≈ 0.04696.
5. **A1 charge attribution**: at R64 quark composition, the
   p-sheet contribution to α is f(n_pt, n_pr) = n_pt/6 + n_pr/4.
   Replaces R0's raw n_pt projection.
6. **α-sum rule (multi-sheet compounds)**: α/α_target =
   (n_et − n_pt + n_νt)² for compounds touching multiple sheets.
   This is the R60 carryover formula and gives sums > 1 for
   mesons (a known limitation; pool item p).
7. ~~**Edge methodology**~~: post-audit (Track 17), the
   σ_eff_tube → −116 at signature edge is now strongly suspected
   to be a regulator artifact, not a structural feature.  At
   moderate σ_pS_tube the V(r) has no trough at all; only the
   singular-edge limit gives one, and that fails the QM gate
   (Track 13b).  Pool item r remains formally open but the
   architectural reading has shifted to "regulator artifact."

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
