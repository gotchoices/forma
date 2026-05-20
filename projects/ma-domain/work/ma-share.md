# ma-share.md — Compact Ma dimensions shared across MaSt sheets

**Status:** Historical hypothesis (predates the current candidate analysis). Companion to [3-torus.md](3-torus.md) (the per-sheet 3D extension) — proposes that the 3-torus framework's apparent 9-dim count (3 sheets × 3 dims) collapses to a smaller count (originally N = 6) under a sheet-sharing topology, with each pair of sheets sharing exactly 1 dim. The observed mass clustering across particle types (tau ≈ proton ≈ charm ≈ bottom at ~1 GeV; muon ≈ strange at ~100 MeV; electron ≈ u ≈ d at ~MeV) becomes a *structural prediction* of which dims are shared.

The current working topologies in [candidates.md](candidates.md) supersede this file's specific bare-mode predictions, but the *dim-sharing across sheets* hypothesis carried forward and motivates the wye/delta structures of all three candidates. Pair notation in this file uses prose-only labels (S_ep, U_e, etc.) rather than the `Ma(i, j)` convention; for the current candidate topologies see [candidates.md](candidates.md).

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

The specific claim being tested: **the lightest p-sheet mode and the heaviest e-sheet mode share a dimension**. Under the topology above, the shared dim is **S_ep**. The lightest plane on the p-sheet is the one with the *largest* min(L_a, L_b); the heaviest plane on the e-sheet is the one with the *smallest* min(L_a, L_b). For both to live on the shared S_ep, S_ep needs to be (a) the LARGEST of the p-sheet dims (so p-modes there are lightest) and (b) the SMALLEST of the e-sheet dims (so e-modes there are heaviest). In other words: **S_ep is "small for e but large for p"** — the bridging dimension between the two sheets' length-scale hierarchies.

The analogous statement for **S_eν** (shared between e and ν): bridges the e-sheet's largest dim with the ν-sheet's smallest dim. Whether this works numerically is exactly what §4 examines.

---

## 3. Structural predictions

Under the 6-dim shared topology with each pair-shared dim at the bridging scale:

1. **Tau (heaviest charged lepton) and proton (lightest p-sheet hadron) share their dominant compact direction.** Same 1/L scale, modulated by windings and other dims. *Observation: tau/proton = 1.89, within the natural modulation range.* ✓

2. **The ~1 GeV cluster is a structural consequence**, not numerical accident. Other ~1 GeV particles (c, b) also live primarily on the S_ep dim. The cluster width (~5×) measures how much 2D-mode windings can spread masses around the shared 1/L scale.

3. **Total dimension count drops from 9 → 6.** A theoretically more parsimonious architecture.

4. **The ν-sheet's bridging dim S_eν** is more strained: ν₃ at 60 meV and electron at 0.511 MeV differ by a factor ~8500. Either (a) S_eν isn't the dominant dim for both (it's the largest for ν, but only the *middle* dim for e), or (b) the e-sheet uses the R53 shear-resonance mechanism to push electron well below the bare 1/L_smallest scale, or (c) the sharing topology has to be different — e.g., the ν-sheet shares with a *non-adjacent* part of the e-sheet's dim hierarchy.

5. **Within-sheet generation splitting remains a separate problem** (same as in [3-torus.md §5](3-torus.md)). The shared-dim picture explains *cross-sheet mass clustering*, not the *within-sheet 3-generation hierarchy*. The latter still needs R53-style shear resonance or some equivalent mechanism.

---

## 4. What the test found

A bare-mode mass calculator (a script, since removed as superseded by [cand_solver.py](../scripts/cand_solver.py)) implemented this 6-dim topology and enumerated the 2D-planar mode towers per sheet at low windings with **no shear resonance** — a deliberately bare sanity check, not a full fit. Across four L-value variants it confirmed the **e–p sharing** structurally: tau landed within 1% of observation, and the heavy p-sheet modes (proton-region, charm, bottom, top) all preferred mode-planes containing the shared S_ep dim, making the ~1 GeV cluster a structural consequence rather than a numerical accident. It failed on two counts, both expected — the **ν-sheet** modes came out 5–7 orders of magnitude too heavy (the ν-sheet cannot inherit its meV scale by simple sharing; it needs its own length scale or the R53 shear-resonance mechanism), and **within-sheet 3-generation splitting** did not appear (three coordinate planes give only two distinct bare-mode scales under the min(L_a, L_b)-dominated formula; the third generation needs shears — the same gap [3-torus.md §5.3](3-torus.md) identified). No bare-mode variant fit more than 4 of 12 fermions within a factor of 3, as expected for a test that deliberately omits the shear mechanism the current architecture relies on.

| Claim | Status |
|---|---|
| (a) e-sheet and p-sheet share a dim placing tau ≈ proton/charm/bottom at one scale | **✓ Confirmed structurally.** |
| (b) The ~GeV mass cluster is a structural consequence of the shared S_ep dim | **✓ Confirmed.** |
| (c) Total compact-dim count drops from 9 (independent 3-toruses) to 6 (sharing) | **✓ Topology consistent** — though [candidates.md](candidates.md) later settled on 8 dims for Candidate C. |
| (d) ν-sheet shares a dim with e-sheet, relating ν₃ (60 meV) to the electron (511 keV) | **✗ Fails** in the bare mode formula; the ν-sheet needs an independent length scale or shear resonance. |
| (e) Within-sheet 3-generation splitting follows from the 3 coordinate planes per sheet | **✗ Fails** (inherited from [3-torus.md §5.3](3-torus.md)); needs shears. |

**What carried forward.** The cross-sheet *bridging via shared dims* is the durable result. It is the conceptual seed of the dim-pool topology used by every candidate in [candidates.md](candidates.md), and it makes model-F's L_ring_e ≈ L_ring_p near-coincidence a structural fact rather than an accident. The specific 6-dim triangle and the bare-mode mass predictions were superseded; the dim-sharing idea was not. The orthogonal within-sheet 3-generation problem remained open in the same place it always was — see [candidates.md](candidates.md) for the current treatment.

---

## 5. Cross-references

- [3-torus.md](3-torus.md) — companion file: each sheet as a 3-torus (sets up the 2D-planar mode classification that this file's "shared planes" rely on).
- [sheet-proton 3-gen.md §12–§13](../../sheet-proton/work/3-gen.md) — Phase 3/4 negative results on the multi-generation hierarchy from a single-sheet picture; motivates looking at cross-sheet structure.
- [models/model-F.md](../../../models/model-F.md) — current model architecture with L_ring_e and L_ring_p (the suggestive ~15% match between the two ring radii).
- [studies/R53-three-generations](../../../studies/R53-three-generations) — the in-sheet shear-resonance mechanism that handles within-sheet generation splitting.
