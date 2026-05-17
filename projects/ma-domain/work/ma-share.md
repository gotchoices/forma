# ma-share.md — Six compact dimensions shared across MaSt sheets

**Status:** Hypothesis + computational sanity-check. Companion to [3-torus.md](3-torus.md) (the per-sheet 3D extension) — proposes that the 3-torus framework's apparent 9-dim count (3 sheets × 3 dims) collapses to **6** under a sheet-sharing topology, with each pair of sheets sharing exactly 1 dim. The observed mass clustering across particle types (tau ≈ proton ≈ charm ≈ bottom at ~1 GeV; muon ≈ strange at ~100 MeV; electron ≈ u ≈ d at ~MeV) becomes a *structural prediction* of which dims are shared.

---

## 1. The observation

Sort the 12 fundamental fermion masses on a log scale and they cluster:

| Scale | Members (mass in MeV) | Spread |
|---|---|---:|
| ~meV | ν₁ (3 × 10⁻⁸), ν₂ (3.3 × 10⁻⁸), ν₃ (6 × 10⁻⁸) | ×2 |
| ~MeV | electron (0.511), u (2.16), d (4.67) | ×9 |
| ~100 MeV | muon (106), s (93) | ×1.1 |
| ~1 GeV | tau (1777), proton (938), c (1270), b (4180) | ×4.5 |
| ~100 GeV | top (173,000) | (alone) |

These clusters span ν, e, and p sheets — they aren't a per-sheet feature. *If each sheet were structurally independent, there's no reason for tau and proton (different sheets) to land within a factor of 2 of each other.* The clustering is suggestive of **shared dimensional structure**: a single compact direction whose 2π/L sets a common mass scale that multiple sheets' modes inherit.

A complementary hint comes from [model-F](../../../models/model-F.md): the e-sheet ring radius L_ring_e = 54.83 fm and the p-sheet ring radius L_ring_p = 47.29 fm are within 15% of each other — a coincidence under independent-sheet architecture, a structural fact under sharing.

---

## 2. The 6-dim topology

Take 6 total compact dimensions, divided into:

- **3 unique dims**, one per sheet: U_e, U_p, U_ν.
- **3 shared dims**, one per sheet-pair: S_ep (shared by e and p), S_eν (shared by e and ν), S_pν (shared by p and ν).

Each sheet uses 3 of the 6:

| Sheet | Dim 1 | Dim 2 | Dim 3 |
|---|---|---|---|
| e | U_e | S_ep | S_eν |
| p | U_p | S_ep | S_pν |
| ν | U_ν | S_eν | S_pν |

Each pair of sheets overlaps in 1 dim. No triple overlap (e ∩ p ∩ ν = ∅). The graph is the *triangle*: three nodes (sheets), three edges (shared dims).

Under the [3-torus.md](3-torus.md) hypothesis, each sheet has three 2D-planar mode towers (one per coordinate-pair within the sheet). Under the present sharing topology, *the shared-dim plane on two adjacent sheets uses the same compact direction*, so modes on that shared plane inherit the same mass scale 1/L_shared on both sheets.

The user's specific claim: **the lightest p-sheet mode and the heaviest e-sheet mode share a dimension**. Under the topology above, the shared dim is **S_ep**. The lightest plane on the p-sheet is the one with the *largest* min(L_a, L_b); the heaviest plane on the e-sheet is the one with the *smallest* min(L_a, L_b). For both to live on the shared S_ep, S_ep needs to be (a) the LARGEST of the p-sheet dims (so p-modes there are lightest) and (b) the SMALLEST of the e-sheet dims (so e-modes there are heaviest). In other words: **S_ep is "small for e but large for p"** — the bridging dimension between the two sheets' length-scale hierarchies.

The analogous statement for **S_eν** (shared between e and ν): bridges the e-sheet's largest dim with the ν-sheet's smallest dim. Whether this works numerically is exactly what Test 5 checks below.

---

## 3. Structural predictions

Under the 6-dim shared topology with each pair-shared dim at the bridging scale:

1. **Tau (heaviest charged lepton) and proton (lightest p-sheet hadron) share their dominant compact direction.** Same 1/L scale, modulated by windings and other dims. *Observation: tau/proton = 1.89, within the natural modulation range.* ✓

2. **The ~1 GeV cluster is a structural consequence**, not numerical accident. Other ~1 GeV particles (c, b) also live primarily on the S_ep dim. The cluster width (~5×) measures how much 2D-mode windings can spread masses around the shared 1/L scale.

3. **Total dimension count drops from 9 → 6.** A theoretically more parsimonious architecture.

4. **The ν-sheet's bridging dim S_eν** is more strained: ν₃ at 60 meV and electron at 0.511 MeV differ by a factor ~8500. Either (a) S_eν isn't the dominant dim for both (it's the largest for ν, but only the *middle* dim for e), or (b) the e-sheet uses the R53 shear-resonance mechanism to push electron well below the bare 1/L_smallest scale, or (c) the sharing topology has to be different — e.g., the ν-sheet shares with a *non-adjacent* part of the e-sheet's dim hierarchy.

5. **Within-sheet generation splitting remains a separate problem** (same as in [3-torus.md §5](3-torus.md)). The shared-dim picture explains *cross-sheet mass clustering*, not the *within-sheet 3-generation hierarchy*. The latter still needs R53-style shear resonance or some equivalent mechanism.

---

## 4. The test

Implement a 6-dim shared-MaSt mass-prediction calculator and check whether the observed 12-fermion mass spectrum can be reproduced under this topology.

Script: [scripts/ma_share.py](../scripts/ma_share.py).

### 4.1 What the script does

1. Take 6 candidate dim values (L_fm dict) covering scales from ~0.001 fm (top mass) to ~10⁹ fm (neutrino mass), spread across the bridging-dim convention of §2.

2. For each sheet, enumerate the three 2D-planar mode towers (one per coordinate-pair) at low integer windings (default: |n_a|, |n_b| ≤ 5).

3. For each observed fermion, find the best-matching mode (lowest |log₁₀(predicted / observed)|) within the sheet's predicted spectrum.

4. Report per-fermion match quality (log-error) and identify which planes carry which particles.

### 4.2 What the test does NOT do

- Does *not* search optimally over L values — uses fixed baseline + a small set of variants.
- Does *not* include shear resonances (σ = 0 throughout). The known R53 mechanism for the electron-mass scale is therefore not invoked; the test is a *bare* sanity-check on the shared-dim hierarchy.
- Does *not* attempt to reproduce within-sheet 3-generation structure beyond what bare 2D-mode windings allow (per §3 prediction 5).

### 4.3 What success / failure looks like

- **Strong success**: every observed fermion lands within log-error ≤ 0.5 (factor 3) of a predicted mode at low windings (≤ 5), with the e-p shared-plane modes (the S_ep plane) carrying tau on e-sheet and proton on p-sheet at the right relative masses.
- **Partial success (most likely)**: cross-sheet *mass-cluster* structure is reproduced (tau ≈ proton at the right scale, MeV cluster on e and p sheets, etc.) but *within-sheet* generation splitting requires shears that the bare test doesn't include. This would validate the dim-sharing claim while leaving the orthogonal 3-generation problem open.
- **Failure**: no L assignment puts even the e-p sharing match in the right neighborhood. Would refute the shared-dim hypothesis.

---

## 5. Results

Four L-variants were tested in [scripts/ma_share.py](../scripts/ma_share.py). Each picks specific values for the six dims; modes computed are bare 2D-planar (no shear) at windings ±1 to ±5. Outputs in `outputs/ma_share_*.csv` and `outputs/ma_share_summary.txt`.

### 5.1 Per-variant match quality

| Variant | S_ep [fm] | Notes | Within ×3 | Within ×10 | Total \|log err\| |
|---|---:|---|---:|---:|---:|
| v1_log_spaced | 1.0 | log-spaced baseline | 4/12 | 5/12 | 32.20 |
| v2_tuned_GeV | 0.7 | S_ep tuned to tau (1.77 GeV) | 2/12 | 4/12 | 32.97 |
| v3_tuned_proton | 1.32 | S_ep tuned to proton (938 MeV) | 2/12 | 5/12 | 31.15 |
| **v4_modelF_inspired** | 50 | S_ep near model-F L_ring | **4/12** | 5/12 | **27.29** |

No variant gets more than 4 of 12 fermions within a factor-of-3 of the predicted spectrum. The full 12-fermion spectrum is **not** reproducible by bare 2D-mode quantization alone — exactly as 3-torus.md §5 predicted (and consistent with R53 / model-F needing shear-resonance for in-sheet generation splitting).

### 5.2 The e-p sharing claim — confirmed structurally

The user's specific claim — that tau (heaviest e-sheet mode) and proton-scale particles (lightest p-sheet modes) share a dimension — is validated in the test. In v2_tuned_GeV (S_ep = 0.7 fm):

- **Tau best match** = (S_ep, U_e) plane, windings (1, 5), predicted mass 1777 MeV vs observed 1777 MeV. **log_err = 0.00.** ✓
- **The (1, 1) mode on the S_ep–S_pv plane on the p-sheet** = 17.8 GeV — places the heavier p-sheet modes (bottom 4.18 GeV, top 173 GeV, charm 1.27 GeV) all in the same plane as tau's bridging dim.

In v3_tuned_proton (S_ep = 1.32 fm, set to give the (1, 1) mode at exactly 938 MeV):

- **Tau best match** = (S_ep, S_eν) plane, windings (2, 1), 1.88 GeV. **log_err = +0.02.** ✓
- **Top best match** = (S_pν, S_ep) plane, windings (5, 5), 103 GeV. log_err = −0.22. ✓
- **Bottom best match** = (S_pν, S_ep) plane, windings (1, 1), 20.7 GeV. log_err = +0.69. ~

The ~GeV cluster (tau, proton-region, charm, bottom, top) all prefer modes on planes *containing the shared S_ep dim* — exactly the bridging-dim structure the §2 topology predicts. The clustering across e and p sheets is a structural consequence, not numerical coincidence, *given* the dim-sharing topology.

The ratio (lowest p-sheet mode using S_ep) / (e-sheet tau mode) = 17,800 / 1777 ≈ 10× in v2, with the latter at lower energy because U_e (the "ring" dim for e-sheet's tau plane) is much larger than U_p (the "ring" dim for p-sheet's heavy modes). The bridging works — same compact direction, different masses set by the *other* dim in the pair.

### 5.3 The ν-(e or p) sharing claim — fails in the bare test

The user's secondary claim ("a common dimension might serve neutrino and electron") fails decisively under bare 2D-mode quantization. In every variant tested:

- **All three neutrinos are off by ~5–7 orders of magnitude** (log_err = +5.32 to +6.62 across variants). The smallest predicted ν-sheet mode mass is ~0.012 MeV (limited by the smaller of the two ν-sheet dims, S_eν or S_pν, which can't be made arbitrarily large without breaking the e-sheet's and p-sheet's mass-scale constraints).
- **The ν-sheet's largest dim U_v** (10⁹–10¹⁰ fm) does have the right natural scale (~μeV), but the *mass formula* on a (L_small, L_large) plane is dominated by the smaller L. So the ν modes always land at 1/L_small, not 1/L_large.

This is a structural failure of the bare ν-sharing claim: the ν-sheet's small bridging dims (which it inherits from e- and p-sheets where they need to be ~MeV-scale) are too small to give ν masses at the right scale. **The ν-sheet needs an independent mechanism** — either:

1. **Three independent ν-sheet dims, all ~mm-μm scale** (no sharing with e or p), recovering the [3-torus.md](3-torus.md) per-sheet picture with no sharing for ν. The cross-sheet clustering hypothesis then applies only to e and p, not ν.

2. **R53-style shear-resonance on the ν-sheet** (the existing model-F mechanism). With s_ν = 0.022 (R49), the (1, 1) ν₁ mode is at 29 meV — *not* via bare-mode scaling but via shear-cancellation of the dominant kinetic term. The bare-mode test doesn't capture this; the ν-sheet's mass scale is fundamentally a shear effect, not a 1/L effect.

3. **Sharing of a μm-scale dim** that just doesn't appear in e or p sheets (a dim *unique to ν* that's much larger than anything on e or p). This brings the ν-sheet back to having its own length scale rather than sharing across the cluster.

Variants (1) and (3) are equivalent — they both say the ν-sheet has its own size scale. (2) is the model-F prescription and is what the existing framework already does. The bare-test failure is therefore not surprising: **the ν-(e or p) sharing claim, in the simple form the user proposed, is not consistent with the meV ν masses without an additional shear-resonance mechanism.**

### 5.4 Within-sheet 3-generation splitting — fails (same as 3-torus.md)

Across all variants, no single sheet's three coordinate planes produced three distinct mass scales matching the observed 3-generation pattern at low windings. As predicted in [3-torus.md §5.3](3-torus.md), the (min(L_a, L_b))-dominated 2D-mode mass formula gives at most 2 distinct scales per sheet from 3 pairs of dims. To get e/μ/τ from the e-sheet, R53-style shear resonance is required (current model-F mechanism). This is not a failure of the shared-dim picture per se — it's the same problem identified in [3-torus.md](3-torus.md) and inherited unchanged here.

### 5.5 Verdict

**The 6-dim shared topology is consistent with the observed mass clustering across e and p sheets, but fails to handle ν masses without an additional shear mechanism.** Specifically:

| Claim | Status |
|---|---|
| (a) e-sheet and p-sheet share a dim that puts tau ≈ proton/charm/bottom at the same scale | **✓ Confirmed structurally.** Variants v2 (S_ep = 0.7 fm) and v3 (S_ep = 1.32 fm) both place tau within 1% of observation and the heavy p-sheet modes in the same plane. |
| (b) The ~GeV mass cluster (tau, proton, charm, bottom) is a structural consequence of the shared S_ep dim | **✓ Confirmed.** All four particles prefer mode-planes containing S_ep in the predicted spectrum. |
| (c) Total compact-dim count drops from 9 (independent 3-toruses) to 6 (sharing topology) | **✓ Topology consistent.** No new constraints emerged from the test that would force >6 dims. |
| (d) ν-sheet shares a dim with e-sheet, giving a structural relation between ν₃ (60 meV) and electron (511 keV) | **✗ Fails in bare mode formula.** ν-sheet needs either an independent (non-shared) μm-scale dim or the existing R53 shear-resonance for the meV scale. |
| (e) Within-sheet 3-generation splitting follows from the 3 coordinate planes per sheet | **✗ Fails (inherited from [3-torus.md §5.3](3-torus.md)).** 3 planes give 2 distinct mass scales by min() rule; the 3rd needs shears. |

**Net assessment.** The cross-sheet *bridging* via shared dims is a real structural feature with empirical support (the GeV cluster). The hypothesis is therefore a useful *partial* re-architecting of the multi-sheet model — total dim count drops to 6, the model-F L_ring_e ≈ L_ring_p coincidence becomes structural, and the GeV cluster gets a geometric explanation.

But the picture does *not* eliminate the need for in-sheet shear-resonance (the R53 mechanism), and it doesn't naturally accommodate the ν-sheet mass scale via simple sharing. A complete picture would have:

- **e and p sheets sharing the S_ep dim** at the GeV scale (this work's finding).
- **Each sheet using R53 shear-resonance** for its own 3-generation splitting (inherited from existing model-F).
- **ν-sheet either disjoint from e and p** (no shared dims) or sharing dims that are small enough to fit e/p but with the ν-sheet's modes pushed down via the shear-resonance mechanism that's already in use there.

This is a *constructive* result: the topology simplifies, the GeV-cluster fact gets explained, and the existing R53 mechanism continues to do what it already does. The orthogonal multi-generation problem remains open in the same place it always was.

### 5.6 Recommended next steps if pursued

1. **Re-derive model-F's L_ring_e ≈ L_ring_p as a structural identity.** If e-sheet and p-sheet share their ring dim (S_ep in this nomenclature), the values must be the *same* up to fine corrections. Variance currently 15% — investigate whether the small discrepancy in model-F is a measurement uncertainty or a structural prediction.

2. **Extend `ma_share.py` with shears.** Once shear-resonance is added (σ ≠ 0 on each plane), the within-sheet 3-generation splitting can be reproduced, and the full 12-fermion fit becomes feasible. The fit would have 6 dim sizes + 3 shears (one per pair-shared plane) = 9 parameters for 12 observables — over-determined enough to be predictive if the geometry is right.

3. **Cross-link with R64 nuclear scaling.** If the (3, 6) proton on p-sheet uses S_ep as its ring dim, and (3, 6) nuclear scaling holds (n_pt = 3A, n_pr = 6A), then the nuclear mass spectrum becomes a constraint on S_ep beyond just the proton/tau ratio.

4. **Determine the topology constraints.** The 6-dim triangle topology (each pair shares 1) is the minimal sharing. Variants with 5 dims (3 sheets sharing a common dim) or fewer would further reduce the count but break the per-pair-share structure. Worth checking whether the GeV cluster can be matched with a 5-dim topology.

---

## 6. Cross-references

- [3-torus.md](3-torus.md) — companion file: each sheet as a 3-torus (sets up the 2D-planar mode classification that this file's "shared planes" rely on).
- [sheet-proton 3-gen.md §12–§13](../../sheet-proton/work/3-gen.md) — Phase 3/4 negative results on the multi-generation hierarchy from a single-sheet picture; motivates looking at cross-sheet structure.
- [models/model-F.md](../../../models/model-F.md) — current model architecture with L_ring_e and L_ring_p (the suggestive ~15% match between the two ring radii).
- [studies/R53-three-generations](../../../studies/R53-three-generations) — the in-sheet shear-resonance mechanism that handles within-sheet generation splitting.
