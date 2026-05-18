# candidates.md — Three current topology candidates, side by side

**Status:** Comparison of the three ma-domain topology candidates we are actively considering. Each is characterized by its quark / electron / neutrino dim-pair layout. Preliminary fits are computed by [scripts/candidate_fits.py](../scripts/candidate_fits.py); the full output is in [outputs/candidate_fits.txt](../outputs/candidate_fits.txt).

**Notation.** Dim labels m1..m_N are size-ordered, smallest first (m1 is the smallest compact circumference, hosting the heaviest mass scales). A dim-pair is written `Ma(i, j)` with `i < j`; a topology (set of pairs) is written `Ma((i,j), (k,l), …)`. Mode-windings on a pair are written `T(m_t, m_r)` per metric-charge ch. 4. See [architecture.md §2.1](architecture.md).

**Mode convention (per [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md)):** closure-satisfying modes are exactly T(1, n) for n ∈ ℤ \ {0} (m_t divides m_r, both nonzero). The lowest two |m_t| = 1 modes per pair are **T(1, 1)** and **T(1, 2)**.

---

## 1. The three candidates

| | **A — wye + path** | **B — wye + delta** | **C — wye + delta + delta** |
|---|---|---|---|
| Quark | `Ma((1,4), (2,4), (3,4))` | `Ma((1,4), (2,4), (3,4))` | `Ma((1,4), (2,4), (3,4))` |
| Electron | `Ma((1,2), (1,5), (4,5))` | `Ma((1,2), (1,5), (2,5))` | `Ma((1,2), (1,5), (2,5))` |
| Neutrino | `Ma(5, 6)` | `Ma(5, 6)` | `Ma((5,6), (5,7), (6,7))` |
| Quark shape | wye (hub at m4) | wye (hub at m4) | wye (hub at m4) |
| Electron shape | **4-dim path** (m2—m1—m5—m4) | **delta on {m1, m2, m5}** | **delta on {m1, m2, m5}** |
| Neutrino shape | single pair | single pair | **delta on {m5, m6, m7}** |
| Total dims | 6 | 6 | **7** |

All three candidates share the **same quark wye** after size-ordered relabeling: hub at m4 (the largest of the quark-region dims, ~5740 fm), spokes at m1, m2, m3 (the rings, sized 0.007, 0.91, 181 fm respectively).

Candidates B and C share the **same electron delta** as well. The difference between them is whether the neutrino sector is a single pair (B) or a third delta (C).

Candidate A differs in the electron sector only: its electron topology is a 4-dim path (m2—m1—m5—m4) rather than a 3-dim delta. The path uses one dim from each end of the quark hierarchy (m1 small, m4 large) plus the small m2 and the new m5, in a non-regular shape.

### 1.1 Topology diagrams

In the diagrams below, nodes are Ma dims (m1..m_N), edges are dim-pairs labelled by sector: `p` = quark/proton, `e` = electron, `v` = neutrino. Shared dims appear in both the sub-graphs they participate in (so the same `m1` in the quark wye is the same `m1` in the electron sector below it).

**Candidate C — wye + e-delta + ν-delta** (all-in-one: quark wye flows into e-delta via shared m1, m2; e-delta flows into ν-delta via shared m5):

```
         m3
         |
         p
         |
         m4         (hub of quark wye; plays tube in all 3 p-edges)
        /  \
       p    p
      /      \
    m1 --e-- m2     (m1, m2 also host e-edges in the e-delta)
     \      /
      e    e
       \  /
        m5          (shared between e-delta and ν-delta)
       /  \
      v    v
     /      \
    m6 --v- m7
```

**Candidate B — wye + e-delta + ν pair** (same as C above the ν section; ν is a single edge m5–m6 instead of a delta):

```
         m3
         |
         p
         |
         m4         (hub)
        /  \
       p    p
      /      \
    m1 --e-- m2     (m1, m2 also host e-edges)
     \      /
      e    e
       \  /
        m5
        |
        v
        |
        m6
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

**Electron sector (B and C: delta triangle).** Each of the three pairs in the delta hosts one charged lepton at its lowest closure mode T(1, 2) — no within-pair doublet on leptons (Q = ±1 doesn't need the lobe/saddle split that quark fractional charges require). With per-pair σ_eff and per-pair tube/ring assignment as free parameters, the fit finds assignments such as τ → `Ma(1, 2)`, e → `Ma(1, 5)`, μ → `Ma(2, 5)`. The system is underdetermined (multiple lepton↔pair mappings and L_5 values fit to machine precision), so the specific arrangement reported by the script is one valid solution among several.

Candidate A's electron sector uses 4 dims in a non-regular path shape (m2—m1—m5—m4) and was not fit here (it's a structurally different problem).

**Neutrino sector (C only: delta triangle).** Analogous to electrons: each pair in the delta `Ma((5,6), (5,7), (6,7))` hosts one ν mass eigenstate at T(1, 2), with per-pair σ_eff and L_6, L_7 as free parameters (L_5 inherited from the e-sector fit). The fit closes cleanly.

For A and B, the ν sector is a single pair `Ma(5, 6)`. *Strict reading* (only T(1, 1) and T(1, 2) per pair = 2 modes) cannot host 3 ν masses. *Relaxed reading* (sign-flipped m_t admitted: T(1, 1), T(−1, 1), T(1, 2) are 3 distinct closure-satisfying modes) can host 3 masses — see §4.

---

## 3. Preliminary fit results

All numerics from [outputs/candidate_fits.txt](../outputs/candidate_fits.txt).

| Sector | Candidate A | Candidate B | Candidate C |
|---|---|---|---|
| **Quarks (all 6)** | max **0.499%** | max **0.499%** | max **0.499%** |
| **Electrons (e, μ, τ)** | not fit (4-dim path) | max **0.000%** | max **0.000%** |
| **Neutrinos (ν₁, ν₂, ν₃)** | not viable, single pair | not viable, single pair (*) | max **0.000%** |

(*) See §4 — sign-flipped modes can rescue B's ν sector to ~1%.

**Quark fits — all 3 candidates equivalent.** The wye structure is topologically the same in all three. Reproduces all 6 quark masses (u, d, s, c, b, t including within-generation asymmetries m_d/m_u = 2.17, m_c/m_s = 14, m_t/m_b = 41) to < 0.5% using only T(1, 1) and T(1, 2) closure modes plus 3 per-pair σ_eff values. Dim sizes (size-ordered):

  - **L_1 ≈ 0.007 fm** (b/t ring)
  - **L_2 ≈ 0.91 fm** (s/c ring)
  - **L_3 ≈ 181.5 fm** (u/d ring)
  - **L_4 ≳ 5740 fm** (common tube; hub of the wye)

**Electron fit (B and C).** The three e-sheet pairs use inherited L_1 = 0.007 fm and L_2 = 0.91 fm from the quark fit, plus a new L_5 that the fit determines. All three (e, μ, τ) masses match to machine precision; the script finds **L_5 ≈ 1.2 × 10⁵ fm ≈ 0.12 mm** in one valid solution (τ on `Ma(1, 2)`, e on `Ma(1, 5)`, μ on `Ma(2, 5)`). Different random seeds can land on other lepton↔pair mappings with comparable-scale L_5, since the e-fit has more freedom than it has constraints.

**Neutrino fit (C).** Inherits L_5 from e-fit; fits L_6, L_7, and 3 σ_eff's to the 3 ν masses. Closes to machine precision; one valid solution has **L_6 ≈ 2.6 × 10¹⁴ fm ≈ 260 m** and **L_7 ≈ 3.8 × 10¹⁰ fm ≈ 4 cm** (the labels of L_6 vs L_7 can swap across seeds — both are ν-region free parameters). All ν₁, ν₂, ν₃ match.

---

## 4. The ν caveat for Candidates A and B

Strictly counting only T(1, 1) and T(1, 2) as the available closure modes per pair, **a single pair hosts at most 2 modes**, but 3 ν mass eigenstates are observed. Candidates A and B's single-pair ν sector cannot fit all three under that strict reading.

**Relaxation: sign-flipped m_t.** Per metric-charge §4 the closure rule is m_t | m_r with both nonzero — which admits T(1, n) for n ∈ ℤ \ {0}, *including* negative m_t. The modes T(1, 1), T(−1, 1), T(1, 2) are all closure-satisfying and give 3 distinct masses when σ_eff ≠ 0 (since the detuning δ = m_r − σ_eff·m_t depends on the sign of m_t). Under this relaxation, a single pair *can* host 3 distinct ν masses — model-F's R49 ν-sheet uses exactly this trio.

A spot check with this relaxation (sign-flipped modes admitted, L_5 varied across cm–dm scales):

| L_5 (fm) | best max \|Δ%\| on ν fit | L_6 (fm) | mode trio |
|---:|---:|---:|---|
| 1 × 10¹⁰ | 167% | 1 × 10¹⁵ | T(±1, n) |
| 4 × 10¹⁰ (4 cm) | **1.05%** | 2.3 × 10¹¹ | T(−1,1), T(1,1), T(−1,2) |
| 1 × 10¹¹ (10 cm) | **0.74%** | 4.3 × 10¹⁰ | T(−1,1), T(1,1), T(1,2) |

So **Candidate B's ν sector is viable to ~1% with sign-flipped modes if L_5 ≳ 4 cm**. The L_5 found by the script's electron fit was 0.18 mm — too small. But the electron fit has freedom: there are many L_5 values that work for e/μ/τ; constraining L_5 ≥ cm and re-fitting electrons would tell us whether B can simultaneously close *all* of (quarks, leptons, neutrinos). Not yet done.

For Candidate A, the same logic applies, but the electron sector was not fit so we don't know what L_5 it would deliver.

---

## 5. Comparison summary

| Property | A | B | C |
|---|:---:|:---:|:---:|
| Quark fit closes (< 1%) | ✓ | ✓ | ✓ |
| Electron fit closes (< 1%) | ? | ✓ | ✓ |
| ν fit closes (strict modes) | ✗ | ✗ | ✓ |
| ν fit closes (sign-flipped modes, L_5 ≳ cm) | ? | likely (~1%) | not needed |
| Topology has clean geometric shape per sector | partial | **yes** | **yes** |
| Dim count | 6 | 6 | 7 |

**Candidate C is the cleanest:** every sector closes to machine precision under the strict closure-mode reading, every sector has a clean topological shape (wye / delta / delta), and the sign-flipped mode caveat is not needed for any sector. Cost: 1 extra dim (7 vs 6).

**Candidate B is competitive:** same quark and electron fits as C, ν fit requires either sign-flipped modes (which are admissible per metric-charge §4 but conceptually less clean — they're matter/antimatter sign-related) AND L_5 forced into cm range (which the e-fit allows but the spot-fit didn't naturally produce).

**Candidate A** is the original starting point. Its electron sector is structurally awkward (4 dims in a path shape rather than a clean 3-dim shape); its ν sector has the same single-pair issue as B. Not preferred.

---

## 6. Working choice

**Candidate C is the active topology.** Cleanest geometric story (wye + delta + delta), strict closure modes work in every sector, no caveats needed. The 7th dim is a structural cost but the payoff is a fully-closed fit across all 12 fermions to machine precision (modulo the 0.5% u-quark residual which is structural, from the full mass formula).

**Candidate B is held as a 6-dim fallback** in case the 7-dim picture runs into trouble in the mathematical formalization phase (Phase 5 of [STATUS.md](STATUS.md)). B works for quarks + leptons; its ν resolution via sign-flipped modes is a known mechanism (R49 / model-F uses it).

**Candidate A** is documented for reference (its quark wye is identical to B/C after size-relabeling; only the electron topology differs). Superseded by B at the same dim count, so not actively pursued.

---

## 7. Cross-references

- [quark-search.md §9](quark-search.md) — quark sector fit, full derivation (applies to all 3 candidates with identical wye structure).
- [architecture.md §2.1](architecture.md) — pair-label `Ma(i, j)` notation.
- [architecture.md §3.3.1](architecture.md) — metric-charge §4 closure rule for valid (m_t, m_r) modes.
- [outputs/candidate_fits.txt](../outputs/candidate_fits.txt) — full numerical fit output for all 3 candidates.
- [scripts/candidate_fits.py](../scripts/candidate_fits.py) — the fit driver.
