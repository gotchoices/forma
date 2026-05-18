# candidates.md — Three current topology candidates, side by side

**Status:** Comparison of the three ma-domain topology candidates we are actively considering. Each is characterized by its quark / electron / neutrino dim-pair layout. Preliminary fits are computed by [scripts/candidate_fits.py](../scripts/candidate_fits.py); the full output is in [outputs/candidate_fits.txt](../outputs/candidate_fits.txt).

**Notation.** Dim labels m1..m_N are size-ordered, smallest first. After the natural-scale relabeling pass the size hierarchy is:

| Label | L (fm) | Role |
|---|---:|---|
| m1 | 0.007 | quark ring — hosts (t, b) |
| m2 | 0.7 | electron-sector dim — sets τ Compton scale |
| m3 | 0.91 | quark ring — hosts (c, s) |
| m4 | 181 | quark ring — hosts (u, d) |
| m5 | ≳ 5740 | quark wye hub (common tube) |
| m6..m8 | cm scale | ν-delta dims (Candidate C only) |

A dim-pair is written `Ma(i, j)` with `i < j`; a topology (set of pairs) is written `Ma((i,j), (k,l), …)`. Mode-windings on a pair are written `T(m_t, m_r)` per metric-charge ch. 4. See [architecture.md §2.1](architecture.md).

**Mode convention (per [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md)):** closure-satisfying modes are exactly T(1, n) for n ∈ ℤ \ {0} (m_t divides m_r, both nonzero). The lowest two |m_t| = 1 modes per pair are **T(1, 1)** and **T(1, 2)**.

---

## 1. The three candidates

| | **A — wye + path** | **B — wye + delta** | **C — wye + delta + delta** |
|---|---|---|---|
| Quark | `Ma((1,5), (3,5), (4,5))` | `Ma((1,5), (3,5), (4,5))` | `Ma((1,5), (3,5), (4,5))` |
| Electron | `Ma((1,3), (1,2), (2,5))` | `Ma((2,4), (2,5), (4,5))` | `Ma((2,4), (2,5), (4,5))` |
| Neutrino | `Ma(6, 7)` | `Ma(6, 7)` | `Ma((6,7), (6,8), (7,8))` |
| Quark shape | wye (hub at m5) | wye (hub at m5) | wye (hub at m5) |
| Electron shape | **4-dim path** (m3—m1—m2—m5) | **delta on {m2, m4, m5}** | **delta on {m2, m4, m5}** |
| Neutrino shape | single pair (fresh dims) | single pair (fresh dims) | **delta on {m6, m7, m8}** |
| Total dims | 7 | 7 | **8** |

All three candidates share the **same quark wye**: hub at m5 (the largest of the quark-region dims, ~5740 fm), spokes at m1, m3, m4 (the rings, sized 0.007, 0.91, 181 fm respectively). Index m2 is reserved for the electron-sector dim (~0.7 fm) and is not in the quark sector.

Candidates B and C share the **same electron delta** `Ma((2,4), (2,5), (4,5))` — using the lepton-scale m2, the u/d ring m4, and the quark hub m5. The difference between B and C is whether the neutrino sector is a single pair (B) or a third delta (C).

Candidate A differs in the electron sector only: its electron topology is a 4-dim path `Ma((1,3), (1,2), (2,5))` (chain m3—m1—m2—m5) rather than a 3-dim delta. The path uses the b/t ring m1, the s/c ring m3, the lepton dim m2, and the hub m5 in a non-regular shape.

### 1.1 Topology diagrams

In the diagrams below, nodes are Ma dims (m1..m_N), edges are dim-pairs labelled by sector: `p` = quark/proton, `e` = electron, `v` = neutrino. Shared dims appear in both the sub-graphs they participate in (so the same `m1` in the quark wye is the same `m1` in the electron sector below it).

**Candidate C — wye + e-delta + ν-delta** (quark wye and e-delta SHARE the pair (m4, m5) — that pair carries both a `p` edge (quark clover mode hosting u, d) and an `e` edge (electron ellipse mode hosting electron), as different cross-section modes coexisting on the same dim-pair geometry; the ν-delta is decoupled onto fresh dims m6, m7, m8):

```
   Quark wye + e-delta (shared edge m4–m5):

           m1                 m3
            \                 /
             p               p
              \             /
               \           /
              ┌─m5(hub)──p──m4
              │   \         │
              e    e        e          (e-delta closes via m2-m5, m2-m4)
              │     \       │
              │      \      │
              └──── m2 ─────┘
                    │
                    (m2 = 0.7 fm — lepton-scale dim, between m1 and m3 in size)

   Neutrino delta (decoupled — fresh dims):

           m6 ── v ── m7
             \       /
              v     v
               \   /
                m8
```

**Candidate B — wye + e-delta + ν pair** (same quark+e structure as C; ν is a single pair on fresh dims):

```
   Quark wye + e-delta (shared edge m4–m5):

           m1                 m3
            \                 /
             p               p
              \             /
               \           /
              ┌─m5(hub)──p──m4
              │   \         │
              e    e        e
              │     \       │
              └──── m2 ─────┘
                    
   Neutrino pair (decoupled — fresh dims):
   
           m6 ── v ── m7
```

**Candidate A — wye + e-path + ν pair** (the e-sector is a 4-dim chain that wraps back through the quark hub m5, so it can't be drawn in a single clean spine — shown here as wye + horizontal path):

```
   Quark wye:                Electron path (4 dims, 3 e-edges):

         m4                    m3 --e-- m1 --e-- m2 --e-- m5
         |                     ↑        ↑                  ↑
         p                     (ring)   (ring)             (quark hub)
         |
         m5 (hub)            Neutrino pair:
        /  \                   m6 --v-- m7   (fresh dims)
       p    p
      /      \
    m1      m3
```

The visual awkwardness of A — the e-path reusing three of the four quark-region dims (m1, m3, m5) and threading through the lepton-scale m2 — is the same structural awkwardness called out in §5 below: A has no clean per-sector geometric shape, while B and C do.

---

## 2. Mode assignments per sector (all three candidates)

**Quark sector (wye/star).** All three candidates use the same wye with 4 dims: the hub m5 plays tube in every pair, the three spokes m1, m3, m4 play ring (m2 is reserved for the electron sector). Each pair hosts 2 quarks (one generation), with the lighter at T(1, 2) and the heavier at T(1, 1). The within-pair mass ratio is set by σ_eff per pair.

| Pair | Lighter / Heavier | Modes | σ_eff |
|---|---|---|---:|
| `Ma(1, 5)` | b / t | T(1, 2) / T(1, 1) | 1.976 |
| `Ma(3, 5)` | s / c | T(1, 2) / T(1, 1) | 1.932 |
| `Ma(4, 5)` | u / d | T(1, 2) / T(1, 1) | 1.684 |

(Ordering reflects the size convention: the smaller spoke holds the heavier generation, since mass scales as ~1/L_ring in the pure-ring regime. So m1 — the smallest ring at 0.007 fm — hosts the heaviest pair (t, b); m4 — the largest ring at 181 fm — hosts the lightest pair (u, d).)

**Electron sector (B and C: delta triangle on m2, m4, m5).** Each of the three pairs hosts one charged lepton at T(1, 2). With per-pair σ_eff and per-pair tube/ring as free parameters and L_4, L_5 inherited from the quark wye, the fit assigns:

| Pair | Lepton | Tube | Ring | σ_eff |
|---|---|---|---|---:|
| `Ma(4, 5)` | **e** | m5 (5740 fm) | m4 (181 fm) | **1.932** |
| `Ma(2, 4)` | **τ** | m4 (181 fm) | m2 (0.7 fm) | **1.000** |
| `Ma(2, 5)` | **μ** | m5 (5740 fm) | m2 (0.7 fm) | **1.941** |

All three σ_eff land in the natural range (1.0 to 1.94) — *same range* as the quark sector's σ_eff values (1.68, 1.93, 1.98). No R53 fine-tuning is required. The lepton-scale dim m2 ≈ 0.7 fm is set primarily by the τ mass via m_τ ≈ 2πℏc/L_2.

A noteworthy structural point: the pair `Ma(4, 5)` is shared between the quark wye (where it hosts u, d as a clover mode with σ_eff = 1.684) and the e-delta (where it hosts the electron as an ellipse mode with σ_eff = 1.932). Same dim sizes, two different cross-section structures, two different σ_eff values — consistent with the pair-triplet (σ, τ, P) hypothesis in [architecture.md §3.4](architecture.md), where the cross-section shape function P_{ij} is a property of the *mode*, not the *pair geometry*.

Candidate A's electron sector uses 4 dims in a non-regular path shape (m3—m1—m2—m5) and was not fit here (it's a structurally different problem).

**Neutrino sector — C uses a delta on fresh dims.** Candidate C uses `Ma((6, 7), (6, 8), (7, 8))` for the ν sector — three fresh dims that don't share with the e-sector or quark wye. With three pair-σ_eff values and three free L's (L_6, L_7, L_8), the system fits all three ν mass eigenstates to machine precision; one valid solution has L_6 ≈ 7 cm, L_7 ≈ 2 cm, L_8 ≈ 4 cm. (The historical earlier-C design shared m5 with the e-delta — that worked when the e-fit was R53-fine-tuned and produced L_5 ≈ 0.18 mm. After the natural-scale e-refactor pinned L_2 ≈ 0.7 fm, sharing is no longer viable; ν must live on fresh dims.)

For A and B, the ν sector remains a single pair on fresh dims `Ma(6, 7)`. *Strict reading* (only T(1, 1) and T(1, 2) per pair = 2 modes) cannot host 3 ν masses. *Relaxed reading* (sign-flipped m_t admitted: T(1, 1), T(−1, 1), T(1, 2) are 3 distinct closure-satisfying modes) can host 3 masses — see §4.

---

## 3. Preliminary fit results

All numerics from [outputs/candidate_fits.txt](../outputs/candidate_fits.txt).

| Sector | Candidate A | Candidate B | Candidate C |
|---|---|---|---|
| **Quarks (all 6)** | max **0.499%** | max **0.499%** | max **0.499%** |
| **Electrons (e, μ, τ)** | not fit (4-dim path) | max **0.000%** (natural σ_eff) | max **0.000%** (natural σ_eff) |
| **Neutrinos (ν₁, ν₂, ν₃)** | not viable, single pair | not viable, single pair (*) | max **0.000%** (ν-delta on fresh dims) |

(*) See §4 — sign-flipped modes can rescue B's ν sector to ~1%.

**Quark fits — all 3 candidates equivalent.** The wye structure is topologically the same in all three. Reproduces all 6 quark masses (u, d, s, c, b, t including within-generation asymmetries m_d/m_u = 2.17, m_c/m_s = 14, m_t/m_b = 41) to < 0.5% using only T(1, 1) and T(1, 2) closure modes plus 3 per-pair σ_eff values. Quark-region dim sizes:

  - **L_1 ≈ 0.007 fm** (b/t ring)
  - **L_3 ≈ 0.91 fm** (s/c ring)
  - **L_4 ≈ 181.5 fm** (u/d ring)
  - **L_5 ≳ 5740 fm** (common tube; hub of the wye)

(L_2 is reserved for the electron-sector dim.)

**Electron fit (B and C) — natural-scale placement.** The three e-delta pairs are `Ma((2, 4), (2, 5), (4, 5))`, inheriting L_4 = 181 fm and L_5 = 5740 fm from the quark fit. The fit pins **L_2 ≈ 0.698 fm** (a single value across seeds and across all three pairs that involve m2). All three (e, μ, τ) masses match to machine precision with the assignments and σ_eff values listed in §2 (electron sector). The σ_eff range is 1.0 to 1.94 — *consistent with the quark sector's σ_eff range* (no R53 fine-tuning required). L_2 ≈ 0.7 fm is roughly the τ Compton wavelength, set primarily by m_τ ≈ 2πℏc/L_2.

The pre-relabel placement on the two *smallest* quark dims (Ma using the b/t and s/c rings) also closed to machine precision but required σ_eff ≈ 1.999997 — extreme R53 fine-tuning. That earlier placement was an inherited audit oversight from the pre-size-ordered labeling and has been superseded by the natural-scale placement here.

**Neutrino fit (C) — decoupled ν-delta on fresh dims.** Candidate C uses `Ma((6, 7), (6, 8), (7, 8))` for the ν-delta, decoupled from the e-sector. Three free L's (L_6, L_7, L_8) and three pair σ_eff values fit all three ν masses to machine precision; one valid solution has **L_6 ≈ 7 × 10¹¹ fm ≈ 7 cm**, **L_7 ≈ 2 × 10¹⁰ fm ≈ 2 cm**, **L_8 ≈ 4 × 10¹⁰ fm ≈ 4 cm**. Decoupling from the e-sector was forced by the natural-scale e-refactor — the e-sector now pins L_2 ≈ 0.7 fm which is incompatible with the meV ν scale (any pair containing m2 has a mass floor of 1240/0.7 ≈ 1770 MeV). Total dim count: 8.

---

## 4. The ν caveat for Candidates A and B

Strictly counting only T(1, 1) and T(1, 2) as the available closure modes per pair, **a single pair hosts at most 2 modes**, but 3 ν mass eigenstates are observed. Candidates A and B's single-pair ν sector cannot fit all three under that strict reading.

**Relaxation: sign-flipped m_t.** Per metric-charge §4 the closure rule is m_t | m_r with both nonzero — which admits T(1, n) for n ∈ ℤ \ {0}, *including* negative m_t. The modes T(1, 1), T(−1, 1), T(1, 2) are all closure-satisfying and give 3 distinct masses when σ_eff ≠ 0 (since the detuning δ = m_r − σ_eff·m_t depends on the sign of m_t). Under this relaxation, a single pair *can* host 3 distinct ν masses — model-F's R49 ν-sheet uses exactly this trio.

After the natural-scale e-refactor, **Candidate B's ν pair lives on *fresh* dims** `Ma(6, 7)`, decoupled from the e-sector. The sign-flipped 3-mode trio mechanism still works in principle, as a spot-check with this relaxation (sign-flipped modes admitted, L_6 varied across cm–dm scales):

| L_6 (fm) | best max \|Δ%\| on ν fit | L_7 (fm) | mode trio |
|---:|---:|---:|---|
| 1 × 10¹⁰ | 167% | 1 × 10¹⁵ | T(±1, n) |
| 4 × 10¹⁰ (4 cm) | **1.05%** | 2.3 × 10¹¹ | T(−1,1), T(1,1), T(−1,2) |
| 1 × 10¹¹ (10 cm) | **0.74%** | 4.3 × 10¹⁰ | T(−1,1), T(1,1), T(1,2) |

So **Candidate B's ν sector is viable to ~1% with sign-flipped modes if L_6 ≳ 4 cm**. The relevant fit knob is now just (L_6, L_7) — no constraint from the e-sector — so the spot-fit doesn't require any electron-sector compromise.

For Candidate A, the same logic applies, but the electron sector was not fit so we don't know what L_2 it would deliver (probably similar to B's, modulo the path-vs-delta structural difference).

---

## 5. Comparison summary

| Property | A | B | C |
|---|:---:|:---:|:---:|
| Quark fit closes (< 1%) | ✓ | ✓ | ✓ |
| Electron fit closes (< 1%) with NATURAL σ_eff | ? | ✓ | ✓ |
| ν fit closes (strict modes) | ✗ | ✗ | ✓ |
| ν fit closes (sign-flipped modes, L_6 ≳ cm) | ? | likely (~1%) | not needed |
| Topology has clean geometric shape per sector | partial | **yes** | **yes** |
| Dim count | 7 | 7 | 8 |

**Candidate C is the cleanest geometric story** (wye + delta + delta), with the natural-scale e-delta delivering σ_eff values in the same range as the quark sector. All three sectors close to machine precision under the strict closure-mode reading. Cost: 8 dims total.

**Candidate B is competitive but more conservative:** same quark and natural-scale electron fits as C. ν sector is one fresh pair (`Ma(6, 7)`) with sign-flipped modes for the 3 mass eigenstates — a known mechanism (R49 / model-F). 7 dims total.

**Candidate A** is the original starting point. Its electron sector is structurally awkward (4 dims in a path shape rather than a clean 3-dim shape); its ν sector has the same single-pair issue as B. Not preferred.

---

## 6. Working choice

**Candidate C remains the active topology.** Cleanest geometric story (wye + delta + delta), all three sectors close to machine precision under strict closure modes, σ_eff values across all twelve charged fermions (6 quarks + 3 leptons + 3 ν mass eigenstates) all sit in a comfortable natural range (1.00 to 1.98), no R53 fine-tuning needed in any sector. Dim count: 8 total (m1..m5 for quarks+leptons, m6..m8 for neutrinos).

**Candidate B is held as a 7-dim fallback** (quark wye + e-delta + ν pair on fresh dims). The ν resolution via sign-flipped modes is conceptually less clean than C's delta, but uses one fewer dim.

**Candidate A** is documented for reference. Its quark wye is identical to B/C; only the electron topology differs and was not fit. Superseded by B/C.

---

## 7. Cross-references

- [quark-search.md §9](quark-search.md) — quark sector fit, full derivation (applies to all 3 candidates with identical wye structure).
- [architecture.md §2.1](architecture.md) — pair-label `Ma(i, j)` notation.
- [architecture.md §3.3.1](architecture.md) — metric-charge §4 closure rule for valid (m_t, m_r) modes.
- [outputs/candidate_fits.txt](../outputs/candidate_fits.txt) — full numerical fit output for all 3 candidates.
- [scripts/candidate_fits.py](../scripts/candidate_fits.py) — the fit driver.
