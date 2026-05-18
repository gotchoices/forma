# candidates.md — Three current topology candidates, side by side

**Status:** Comparison of the three ma-domain topology candidates we are actively considering. Each is characterized by its quark / electron / neutrino dim-pair layout. Preliminary fits are computed by [scripts/candidate_fits.py](../scripts/candidate_fits.py); the full output is in [outputs/candidate_fits.txt](../outputs/candidate_fits.txt).

**Notation.** Dim labels m1..m_N are size-ordered within the original quark-region set (m1 is the smallest of m1..m4, m4 is the largest). The added dim m5 (introduced for the e-sector) is NOT size-ordered after the natural-scale refactor — it lands at L_5 ≈ 0.7 fm, smaller than m4 (5740 fm), m3 (181 fm), and m2 (0.91 fm). A future re-labeling pass should reorder the labels strictly; for now we keep the existing m1..m5 labels to minimize churn. A dim-pair is written `Ma(i, j)` with `i < j`; a topology (set of pairs) is written `Ma((i,j), (k,l), …)`. Mode-windings on a pair are written `T(m_t, m_r)` per metric-charge ch. 4. See [architecture.md §2.1](architecture.md).

**Mode convention (per [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md)):** closure-satisfying modes are exactly T(1, n) for n ∈ ℤ \ {0} (m_t divides m_r, both nonzero). The lowest two |m_t| = 1 modes per pair are **T(1, 1)** and **T(1, 2)**.

---

## 1. The three candidates

| | **A — wye + path** | **B — wye + delta** | **C — wye + delta + delta** |
|---|---|---|---|
| Quark | `Ma((1,4), (2,4), (3,4))` | `Ma((1,4), (2,4), (3,4))` | `Ma((1,4), (2,4), (3,4))` |
| Electron | `Ma((1,2), (1,5), (4,5))` | `Ma((3,4), (3,5), (4,5))` | `Ma((3,4), (3,5), (4,5))` |
| Neutrino | `Ma(5, 6)` | `Ma(5, 6)` | `Ma((6,7), (6,8), (7,8))` — *proposed; old m5-shared design broken by e-refactor* |
| Quark shape | wye (hub at m4) | wye (hub at m4) | wye (hub at m4) |
| Electron shape | **4-dim path** (m2—m1—m5—m4) | **delta on {m3, m4, m5}** | **delta on {m3, m4, m5}** |
| Neutrino shape | single pair | single pair | **delta on {m6, m7, m8}** (proposed) |
| Total dims | 6 | 6 | **8** (was 7 before ν decoupling) |

All three candidates share the **same quark wye** after size-ordered relabeling: hub at m4 (the largest of the quark-region dims, ~5740 fm), spokes at m1, m2, m3 (the rings, sized 0.007, 0.91, 181 fm respectively).

Candidates B and C share the **same electron delta** as well. The difference between them is whether the neutrino sector is a single pair (B, on a `Ma(5, 6)`-style placement) or a third delta (C, originally on `Ma((5,6),(5,7),(6,7))` but now proposed on fresh dims after the natural-scale e-refactor — see §3).

Candidate A differs in the electron sector only: its electron topology is a 4-dim path (m2—m1—m5—m4) rather than a 3-dim delta. The path uses one dim from each end of the quark hierarchy (m1 small, m4 large) plus the small m2 and the new m5, in a non-regular shape.

**On the e-delta dims.** The e-delta in B and C now uses the *larger* two quark dims (m3 = 181 fm and m4 = 5740 fm) plus a new dim m5. Earlier this file recorded the e-delta as `Ma((1,2), (1,5), (2,5))` — using the *smallest* two quark dims — which fitted to machine precision only because σ_eff was driven to within ~10⁻⁶ of the R53 resonance value 2 (extreme fine-tuning, mismatched scales). The natural-scale refactor (this version) closes with σ_eff ≈ 1.93, 1.00, 1.94 — all in the same range as the quark sector's σ_eff values, no R53 fine-tuning needed. See §3.

### 1.1 Topology diagrams

In the diagrams below, nodes are Ma dims (m1..m_N), edges are dim-pairs labelled by sector: `p` = quark/proton, `e` = electron, `v` = neutrino. Shared dims appear in both the sub-graphs they participate in (so the same `m1` in the quark wye is the same `m1` in the electron sector below it).

**Candidate C — wye + e-delta + ν-delta** (quark wye and e-delta now SHARE the pair (m3, m4) — that pair carries both a `p` edge (quark clover mode) and an `e` edge (electron ellipse mode), as different cross-section modes coexisting on the same dim-pair geometry; the ν-delta is decoupled onto fresh dims):

```
   Quark wye + e-delta (shared edge m3–m4):

           m1                 m2
            \                 /
             p               p
              \             /
               \           /
              ┌─m4(hub)──p──m3
              │   \         │
              e    e        e          (e-delta closes via m4-m5, m3-m5)
              │     \       │
              │      \      │
              └──── m5 ─────┘
                    │
                    (m5 = 0.7 fm — new e-sector dim, smaller than m4)

   Neutrino delta (decoupled — no longer shares m5):

           m6 ── v ── m7
             \       /
              v     v
               \   /
                m8
```

**Candidate B — wye + e-delta + ν pair** (same quark+e structure as C; ν is a single pair on fresh dims):

```
   Quark wye + e-delta (shared edge m3–m4):

           m1                 m2
            \                 /
             p               p
              \             /
               \           /
              ┌─m4(hub)──p──m3
              │   \         │
              e    e        e
              │     \       │
              └──── m5 ─────┘
                    
   Neutrino pair (decoupled — fresh dims):
   
           m6 ── v ── m7
```

**Candidate A — wye + e-path + ν pair** (the e-sector is a 4-dim chain that wraps back to the quark hub m4, so it can't be drawn in a single clean spine — shown here as wye + horizontal path):

```
   Quark wye:                Electron path (4 dims, 3 e-edges):

         m3                    m4 --e-- m5 --e-- m1 --e-- m2
         |                     ↑                 ↑         ↑
         p                     (quark hub)       (ring)    (ring)
         |
         m4 (hub)            Neutrino pair:
        /  \                   m5 --v-- m6
       p    p                  ↑
      /      \                 (shared with e-path)
    m1      m2
```

The visual awkwardness of A — the e-path having to reuse three of the four quark-region dims (m4, m1, m2) with a single new dim (m5) — is the same structural awkwardness called out in §5 below: A has no clean per-sector geometric shape, while B and C do.

---

## 2. Mode assignments per sector (all three candidates)

**Quark sector (wye/star).** All three candidates use the same wye with 4 dims: the hub m4 plays tube in every pair, the three spokes m1, m2, m3 play ring. Each pair hosts 2 quarks (one generation), with the lighter at T(1, 2) and the heavier at T(1, 1). The within-pair mass ratio is set by σ_eff per pair.

| Pair | Lighter / Heavier | Modes | σ_eff |
|---|---|---|---:|
| `Ma(1, 4)` | t / b | T(1, 1) / T(1, 2) | 1.976 |
| `Ma(2, 4)` | c / s | T(1, 1) / T(1, 2) | 1.932 |
| `Ma(3, 4)` | d / u | T(1, 1) / T(1, 2) | 1.684 |

(Ordering reflects the size convention: the smaller spoke holds the heavier generation, since mass scales as ~1/L_ring in the pure-ring regime. So m1 — the smallest ring at 0.007 fm — hosts the heaviest pair (t, b); m3 — the largest ring at 181 fm — hosts the lightest pair (u, d).)

**Electron sector (B and C: delta triangle on m3, m4, m5).** Each of the three pairs hosts one charged lepton at T(1, 2). With per-pair σ_eff and per-pair tube/ring as free parameters and L_3, L_4 inherited from the quark wye, the fit assigns:

| Pair | Lepton | Tube | Ring | σ_eff |
|---|---|---|---|---:|
| `Ma(3, 4)` | **e** | m4 (5740 fm) | m3 (181 fm) | **1.932** |
| `Ma(3, 5)` | **τ** | m3 (181 fm) | m5 (0.7 fm) | **1.000** |
| `Ma(4, 5)` | **μ** | m4 (5740 fm) | m5 (0.7 fm) | **1.941** |

All three σ_eff land in the natural range (1.0 to 1.94) — *same range* as the quark sector's σ_eff values (1.68, 1.93, 1.98). No R53 fine-tuning is required. The new e-sector dim m5 ≈ 0.7 fm — set primarily by the τ mass via m_τ ≈ 2πℏc/L_5.

A noteworthy structural point: the pair `Ma(3, 4)` is shared between the quark wye (where it hosts u, d as a clover mode with σ_eff = 1.684) and the e-delta (where it hosts the electron as an ellipse mode with σ_eff = 1.932). Same dim sizes, two different cross-section structures, two different σ_eff values — consistent with the pair-triplet (σ, τ, P) hypothesis in [architecture.md §3.4](architecture.md), where the cross-section shape function P_{ij} is a property of the *mode*, not the *pair geometry*.

Candidate A's electron sector uses 4 dims in a non-regular path shape (m2—m1—m5—m4) and was not fit here (it's a structurally different problem).

**Neutrino sector — now decoupled in the refactored C.** The previous C used `Ma((5,6), (5,7), (6,7))` with L_5 inherited from the e-fit. That worked when L_5 was ≈ 0.18 mm (the original C's fine-tuned solution). After the natural-scale e-refactor, L_5 ≈ 0.7 fm — too small by ~10 orders of magnitude to host meV-scale ν modes (mass floor 2πℏc/L_5 ≈ 1770 MeV). So the new C uses a ν-delta on fresh dims `Ma((6, 7), (6, 8), (7, 8))`, completely decoupled from the e-sector. This pushes the dim count to 8 total. A working numerical fit for this ν-delta has not yet been re-run with the script.

For A and B, the ν sector remains a single pair on fresh dims. *Strict reading* (only T(1, 1) and T(1, 2) per pair = 2 modes) cannot host 3 ν masses. *Relaxed reading* (sign-flipped m_t admitted: T(1, 1), T(−1, 1), T(1, 2) are 3 distinct closure-satisfying modes) can host 3 masses — see §4.

---

## 3. Preliminary fit results

All numerics from [outputs/candidate_fits.txt](../outputs/candidate_fits.txt).

| Sector | Candidate A | Candidate B | Candidate C |
|---|---|---|---|
| **Quarks (all 6)** | max **0.499%** | max **0.499%** | max **0.499%** |
| **Electrons (e, μ, τ)** | not fit (4-dim path) | max **0.000%** (natural σ_eff) | max **0.000%** (natural σ_eff) |
| **Neutrinos (ν₁, ν₂, ν₃)** | not viable, single pair | not viable, single pair (*) | pending — old m5-shared design broken, ν-delta on fresh dims (m6, m7, m8) not yet fit |

(*) See §4 — sign-flipped modes can rescue B's ν sector to ~1%.

**Quark fits — all 3 candidates equivalent.** The wye structure is topologically the same in all three. Reproduces all 6 quark masses (u, d, s, c, b, t including within-generation asymmetries m_d/m_u = 2.17, m_c/m_s = 14, m_t/m_b = 41) to < 0.5% using only T(1, 1) and T(1, 2) closure modes plus 3 per-pair σ_eff values. Dim sizes (size-ordered within the quark set):

  - **L_1 ≈ 0.007 fm** (b/t ring)
  - **L_2 ≈ 0.91 fm** (s/c ring)
  - **L_3 ≈ 181.5 fm** (u/d ring)
  - **L_4 ≳ 5740 fm** (common tube; hub of the wye)

**Electron fit (B and C) — natural-scale placement.** The three e-delta pairs are `Ma((3, 4), (3, 5), (4, 5))`, inheriting L_3 = 181 fm and L_4 = 5740 fm from the quark fit. The fit pins **L_5 ≈ 0.698 fm** (a single value across seeds and across all three pairs that involve m5). All three (e, μ, τ) masses match to machine precision with the assignments and σ_eff values listed in §2 (electron sector). The σ_eff range is 1.0 to 1.94 — *consistent with the quark sector's σ_eff range* (no R53 fine-tuning required). L_5 ≈ 0.7 fm is roughly the τ Compton wavelength, set primarily by m_τ ≈ 2πℏc/L_5.

The earlier `Ma((1,2), (1,5), (2,5))` placement (which used L_1 = 0.007 fm and L_2 = 0.91 fm) also closed to machine precision but required σ_eff ≈ 1.999997 — extreme R53 fine-tuning. That earlier placement was an inherited audit oversight from the pre-size-ordered labeling and has been superseded by the natural-scale placement here.

**Neutrino fit (C) — broken; needs rework.** The previous Candidate C inherited L_5 ≈ 0.18 mm from the (then-fine-tuned) e-fit and used a ν-delta on `Ma((5,6), (5,7), (6,7))`, which closed at machine precision with L_6, L_7 in the cm–m range. After the e-refactor, L_5 ≈ 0.7 fm — and any pair containing m5 now has a mass floor of 1240/0.7 ≈ 1770 MeV, ~10 orders of magnitude above the meV ν scale. So Candidate C's old shared-m5 ν-delta is no longer viable. The proposed fix is to give the ν-delta its own fresh dims `Ma((6, 7), (6, 8), (7, 8))` (8 dims total). A re-fit on this decoupled structure is the immediate next task — the algebra should close to machine precision (same parameter count as before, just no shared L_5 constraint), but it needs to be verified by the script.

---

## 4. The ν caveat for Candidates A and B

Strictly counting only T(1, 1) and T(1, 2) as the available closure modes per pair, **a single pair hosts at most 2 modes**, but 3 ν mass eigenstates are observed. Candidates A and B's single-pair ν sector cannot fit all three under that strict reading.

**Relaxation: sign-flipped m_t.** Per metric-charge §4 the closure rule is m_t | m_r with both nonzero — which admits T(1, n) for n ∈ ℤ \ {0}, *including* negative m_t. The modes T(1, 1), T(−1, 1), T(1, 2) are all closure-satisfying and give 3 distinct masses when σ_eff ≠ 0 (since the detuning δ = m_r − σ_eff·m_t depends on the sign of m_t). Under this relaxation, a single pair *can* host 3 distinct ν masses — model-F's R49 ν-sheet uses exactly this trio.

After the natural-scale e-refactor, **Candidate B's ν pair must live on *fresh* dims** `Ma(6, 7)` (or wherever) — it cannot share m5 because m5 is now ≈ 0.7 fm. The sign-flipped 3-mode trio mechanism still works in principle on those fresh dims, as a spot-check with this relaxation (sign-flipped modes admitted, L_6 varied across cm–dm scales):

| L_6 (fm) | best max \|Δ%\| on ν fit | L_7 (fm) | mode trio |
|---:|---:|---:|---|
| 1 × 10¹⁰ | 167% | 1 × 10¹⁵ | T(±1, n) |
| 4 × 10¹⁰ (4 cm) | **1.05%** | 2.3 × 10¹¹ | T(−1,1), T(1,1), T(−1,2) |
| 1 × 10¹¹ (10 cm) | **0.74%** | 4.3 × 10¹⁰ | T(−1,1), T(1,1), T(1,2) |

So **Candidate B's ν sector is viable to ~1% with sign-flipped modes if L_6 ≳ 4 cm**. The relevant fit knob is now just (L_6, L_7) — no constraint from the e-sector — so the spot-fit shouldn't require any electron-sector compromise.

For Candidate A, the same logic applies, but the electron sector was not fit so we don't know what L_5 it would deliver (probably similar to B's, modulo the path-vs-delta structural difference).

---

## 5. Comparison summary

| Property | A | B | C |
|---|:---:|:---:|:---:|
| Quark fit closes (< 1%) | ✓ | ✓ | ✓ |
| Electron fit closes (< 1%) with NATURAL σ_eff | ? | ✓ | ✓ |
| ν fit closes (strict modes) | ✗ | ✗ | pending re-fit on fresh dims |
| ν fit closes (sign-flipped modes, L_6 ≳ cm) | ? | likely (~1%) | not needed once fresh-dim delta closes |
| Topology has clean geometric shape per sector | partial | **yes** | **yes** |
| Dim count | 6 | 7 (was 6 before ν decoupling) | 8 (was 7) |

**Candidate C is still the cleanest geometric story** (wye + delta + delta), with the natural-scale e-delta now delivering σ_eff values in the same range as the quark sector. The pending re-fit of the ν-delta on fresh dims is the only loose numerical thread. Cost: 8 dims total.

**Candidate B is competitive but more conservative:** same quark and natural-scale electron fits as C. ν sector is one extra fresh pair (`Ma(6, 7)`) with sign-flipped modes for the 3 mass eigenstates — a known mechanism (R49 / model-F). 7 dims total.

**Candidate A** is the original starting point. Its electron sector is structurally awkward (4 dims in a path shape rather than a clean 3-dim shape); its ν sector has the same single-pair issue as B. Not preferred.

---

## 6. Working choice

**Candidate C remains the active topology after the natural-scale e-refactor.** The e-delta now closes at machine precision with σ_eff values (1.93, 1.00, 1.94) — all in the natural range matching the quark sector (no R53 fine-tuning needed) — and the geometry makes physical sense (L_5 ≈ 0.7 fm matches the τ Compton wavelength). The cost is that the old m5-sharing structure between e-delta and ν-delta is broken; C now has a ν-delta on fresh dims (m6, m7, m8) for 8 dims total.

**Candidate B is held as a 7-dim fallback** (quark wye + e-delta + ν pair on fresh dims). The ν resolution via sign-flipped modes is conceptually less clean than C's delta, but uses one fewer dim.

**Candidate A** is documented for reference. Its quark wye is identical to B/C; only the electron topology differs and was not fit. Superseded by B/C.

### 6.1 Immediate to-do for C

1. Re-fit C's ν-delta on fresh dims `Ma((6, 7), (6, 8), (7, 8))` to machine precision (extend `scripts/candidate_fits.py`).
2. Apply a strict size-ordering pass — the post-refactor L_5 ≈ 0.7 fm breaks size-ordering and should trigger a relabeling cascade so dim indices match the size hierarchy (m1 = 0.007 fm; m2 = 0.7 fm ← new e-sector dim; m3 = 0.91 fm; m4 = 181 fm; m5 = 5740 fm; m6..m8 = ν dims).
3. Update topology labels throughout the project files to reflect the relabeling.

---

## 7. Cross-references

- [quark-search.md §9](quark-search.md) — quark sector fit, full derivation (applies to all 3 candidates with identical wye structure).
- [architecture.md §2.1](architecture.md) — pair-label `Ma(i, j)` notation.
- [architecture.md §3.3.1](architecture.md) — metric-charge §4 closure rule for valid (m_t, m_r) modes.
- [outputs/candidate_fits.txt](../outputs/candidate_fits.txt) — full numerical fit output for all 3 candidates.
- [scripts/candidate_fits.py](../scripts/candidate_fits.py) — the fit driver.
