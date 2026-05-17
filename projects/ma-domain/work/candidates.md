# candidates.md — Three current topology candidates, side by side

**Status:** Comparison of the three ma-domain topology candidates we are actively considering. Each is characterized by its quark / electron / neutrino dim-pair layout. Preliminary fits are computed by [scripts/candidate_fits.py](../scripts/candidate_fits.py); the full output is in [outputs/candidate_fits.txt](../outputs/candidate_fits.txt).

**Mode convention (per [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md)):** closure-satisfying modes are exactly T(1, n) for n ∈ ℤ \ {0} (m_t divides m_r, both nonzero). The lowest two |m_t| = 1 modes per pair are **T(1, 1)** and **T(1, 2)**.

---

## 1. The three candidates

| | **A — original** | **B — wye + delta** | **C — wye + delta + delta** |
|---|---|---|---|
| Proton | (1,3) (2,3) (3,4) | (1,2) (2,3) (2,4) | (1,2) (2,3) (2,4) |
| Electron | (2,4) (3,5) (4,5) | (3,4) (3,5) (4,5) | (3,4) (3,5) (4,5) |
| Neutrino | (5,6) | (5,6) | (5,6) (5,7) (6,7) |
| Proton shape | wye (dim 3 hub) | **wye (dim 2 hub)** | wye (dim 2 hub) |
| Electron shape | 4-dim, no pure shape | **delta on dims {3, 4, 5}** | delta on dims {3, 4, 5} |
| Neutrino shape | single pair | single pair | **delta on dims {5, 6, 7}** |
| Total dims | 6 | 6 | **7** |

Candidates B and C share the same proton + electron topology. The difference is whether the neutrino sector is a single pair (B) or a third delta (C).

---

## 2. Mode assignments per sector (all three candidates)

**Quark sector (wye/star).** All three candidates use the same star with 4 dims: one hub plays tube in every pair, three spokes are rings. Each pair hosts 2 quarks (one generation), with the lighter at T(1, 2) and the heavier at T(1, 1). The within-pair mass ratio is set by σ_eff per pair.

| Pair | Lighter / Heavier | Modes | σ_eff |
|---|---|---|---:|
| (hub, spoke_1) | u / d | (1, 2) / (1, 1) | 1.684 |
| (hub, spoke_2) | s / c | (1, 2) / (1, 1) | 1.932 |
| (hub, spoke_3) | b / t | (1, 2) / (1, 1) | 1.976 |

Quark hub dim: A uses index 3, B and C use index 2 (relabeling). Numerics identical.

**Electron sector (B and C: delta triangle).** Each of the three pairs (3, 4), (3, 5), (4, 5) hosts one charged lepton at its lowest closure mode T(1, 2) — no within-pair doublet on leptons (Q = ±1 doesn't need the lobe/saddle split that quark fractional charges require). With per-pair σ_eff and per-pair tube/ring assignment as free parameters, the fit finds the assignment τ → (3, 4), μ → (3, 5), e → (4, 5).

Candidate A's electron sector uses 4 dims in a non-regular shape and was not fit here (it's a structurally different problem).

**Neutrino sector (C only: delta triangle).** Analogous to electrons: each pair hosts one ν mass eigenstate at T(1, 2), with per-pair σ_eff and L_6, L_7 as free parameters. The fit closes cleanly.

For A and B, the ν sector is a single pair. *Strict reading* (only T(1, 1) and T(1, 2) per pair = 2 modes) cannot host 3 ν masses. *Relaxed reading* (sign-flipped m_t admitted: T(1, 1), T(−1, 1), T(1, 2) are 3 distinct closure-satisfying modes) can host 3 masses — see §4.

---

## 3. Preliminary fit results

All numerics from [outputs/candidate_fits.txt](../outputs/candidate_fits.txt).

| Sector | Candidate A | Candidate B | Candidate C |
|---|---|---|---|
| **Quarks (all 6)** | max **0.499%** | max **0.499%** | max **0.499%** |
| **Electrons (e, μ, τ)** | not fit (4-dim irregular) | max **0.000%** | max **0.000%** |
| **Neutrinos (ν₁, ν₂, ν₃)** | not viable, single pair | not viable, single pair (*) | max **0.000%** |

(*) See §4 — sign-flipped modes can rescue B's ν sector to ~1%.

**Quark fits — all 3 candidates equivalent.** The wye structure is topologically the same; only dim labels differ. Reproduces all 6 quark masses (u, d, s, c, b, t including within-generation asymmetries m_d/m_u = 2.17, m_c/m_s = 14, m_t/m_b = 41) to < 0.5% using only T(1, 1) and T(1, 2) closure modes plus 3 per-pair σ_eff values. Dim sizes:

  - hub (common tube): L ≳ 5740 fm
  - spoke for u/d: L = 181.5 fm
  - spoke for s/c: L = 0.910 fm
  - spoke for b/t: L = 0.007 fm

**Electron fit (B and C).** The three e-sheet pairs use inherited L_3 = 0.91 fm and L_4 = 0.007 fm from the quark fit, plus a new L_5 that the fit determines. All three (e, μ, τ) masses match to machine precision, with the script finding L_5 ≈ 0.18 mm (1.83 × 10⁵ fm). The assignment is τ on (3, 4), μ on (3, 5), e on (4, 5) — heavier lepton lives on the pair with smaller dims.

**Neutrino fit (C).** Inherits L_5 from e-fit; fits L_6, L_7, and 3 σ_eff's to the 3 ν masses. Closes to machine precision with L_6 ≈ 30 mm and L_7 ≈ 60 cm. All ν₁, ν₂, ν₃ match.

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

**Candidate A** is the original starting point. Its electron sector is structurally awkward (4 dims in a non-regular shape); its ν sector has the same single-pair issue as B. Not preferred.

---

## 6. Recommendation

**Adopt Candidate C as the working topology.** Cleanest geometric story (wye + delta + delta), strict closure modes work in every sector, no caveats needed. The 7th dim is a structural cost but the payoff is a fully-closed fit across all 12 fermions to machine precision (modulo the 0.5% u-quark residual which is structural, from the full mass formula).

**Hold Candidate B as a fallback** in case the 7-dim picture runs into trouble in the mathematical formalization phase (Phase 5 of [STATUS.md](STATUS.md)). B works for quarks + leptons; its ν resolution via sign-flipped modes is a known mechanism (R49 / model-F uses it).

**Drop Candidate A** as superseded by B (same dim count, cleaner topology in B).

---

## 7. Cross-references

- [quark-search.md §9](quark-search.md) — quark sector fit, full derivation (applies to all 3 candidates with relabeling).
- [architecture.md §3.3.1](architecture.md) — metric-charge §4 closure rule for valid (m_t, m_r) modes.
- [outputs/candidate_fits.txt](../outputs/candidate_fits.txt) — full numerical fit output for all 3 candidates.
- [scripts/candidate_fits.py](../scripts/candidate_fits.py) — the fit driver.
