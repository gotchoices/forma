# quark-search.md — Three quark generations on quark-sector dim-pairs

**Status:** Rough cut. Sets up the mass-formula structure for 6 quarks on a candidate dim-pair topology, works the analytical structure to see whether the dim-sharing leaves enough freedom to fit, and reports honestly on what does and does not close.

**Sections.** §1–§8 document the **first-cut failure**: a 3-dim triangle topology `Ma((1,2), (1,3), (2,3))` on local dim indices (not tied to the project-wide size-ordered labels) cannot fit all 6 quarks under the strict ground rules — the sharing constraint between pairs that have the same smaller dim is a hard analytical obstruction. §9 documents the **working positive result**: a 4-dim wye/star topology `Ma((1,5), (3,5), (4,5))` (project-wide size-ordered labels; m2 reserved for the electron sector) with m5 as the common hub fits all 6 quarks to **< 0.5%** using only T(1, 1) and T(1, 2) closure modes. §10 documents a parallel relaxation path that also closes (4% accuracy, more elaborate). §11 raises a ν-sector viability concern that motivated subsequent work in [candidates.md](candidates.md).

**Working ground rules for §1–§8** (the first-cut attempt):
1. **Only lowest-energy closure modes.** Each pair hosts its 2 lowest closure modes; those 2 modes are the 2 quarks of one generation.
2. **Custom shear per pair.** Each pair `Ma(i, j)` has its own σ_{ij}.
3. **Custom clover per pair.** Each pair has its own χ_{ij} = r_saddle / r_lobe.
4. **τ ∈ {±1/3, ±2/3} per pair.** Discrete choice.
5. **Quarks live on 3 dims**: m1, m2, m3 (triangle `Ma((1,2), (1,3), (2,3))`).

The deliverable here is a *rough cut*; the formalization moves to `ma-domain/` proper if the rough cut closes (per [STATUS.md](STATUS.md) Phase 5).

---

## 1. Setup

Three Ma dims with sizes L_1 < L_2 < L_3 (size-ordered per [architecture.md §1](architecture.md)). The triangle topology `Ma((1,2), (1,3), (2,3))` gives three pairs:

| Pair | Smaller dim | Larger dim |
|---|---|---|
| `Ma(1, 2)` | m1 | m2 |
| `Ma(1, 3)` | m1 | m3 |
| `Ma(2, 3)` | m2 | m3 |

Each dim appears in exactly **2** pairs. This sharing is the structural feature that will dominate the analysis below.

Each pair `Ma(i, j)` carries a triplet (σ_{ij}, τ_{ij}, χ_{ij}) per [architecture.md §3.4](architecture.md). The mass formula (adapted from [sheet-proton clover-mass.md §4](../../sheet-proton/work/clover-mass.md)) on a pair, in terms of mode windings (m_t, m_r):

<!-- m² = (2πℏc)² · ((m_t / L_a)² + ((m_r − σ_eff · m_t) / L_b)²) -->
$$
m^2 \;=\; (2\pi \hbar c)^2 \cdot \left[ \left(\frac{m_t}{L_a}\right)^2 \;+\; \left(\frac{m_r - \sigma_{\mathrm{eff}}\, m_t}{L_b}\right)^2 \right]
$$

where for pair `Ma(i, j)`:
- **L_a** = larger dim of pair (plays "tube circumference" in the cross-term/twist structure)
- **L_b** = smaller dim of pair (plays "ring circumference")
- **σ_eff = σ_{ij} + 2 τ_{ij}** is the effective cross-term coefficient

*Note on convention.* The tube/ring assignment here follows the R53 charged-lepton regime where ε = L_tube / L_ring can be > 1 (fat torus); the smallest-as-tube rule held under the older proton-sheet convention but does not survive to ε >> 1 (see [architecture.md §3.1](architecture.md)). For the quark fit below we keep "L_a > L_b" so ε = L_a/L_b > 1 always.

In MeV·fm units (ℏc = 197.327, so 2πℏc ≈ 1239.8):

<!-- m [MeV] = 1240 · sqrt(m_t²/L_a² + (m_r − σ_eff m_t)²/L_b²)  with L in fm -->
$$
m\,[\mathrm{MeV}] \;=\; 1240 \cdot \sqrt{\left(\frac{m_t}{L_a}\right)^2 + \left(\frac{m_r - \sigma_{\mathrm{eff}} m_t}{L_b}\right)^2} \quad (\text{L in fm})
$$

---

## 2. Lowest two closure modes per pair

For (m_t = 1, m_r ∈ ℤ): the closure constraint is satisfied for any integer m_r. Detuning δ ≡ m_r − σ_eff. The two lowest detunings are:

- δ_A = σ_eff − round(σ_eff), with |δ_A| ≤ 1/2 — let f ≡ |δ_A| ∈ [0, 1/2]
- δ_B = δ_A ± 1, with |δ_B| = 1 − f

so the two lowest modes on a pair give masses

<!-- m_A² = 1240² · (1/L_a² + f²/L_b²) ;  m_B² = 1240² · (1/L_a² + (1−f)²/L_b²) -->
$$
m_A^2 \;=\; 1240^2 \cdot \left( \frac{1}{L_a^2} + \frac{f^2}{L_b^2} \right),
\qquad
m_B^2 \;=\; 1240^2 \cdot \left( \frac{1}{L_a^2} + \frac{(1 - f)^2}{L_b^2} \right)
$$

(For ε small enough that the m_t = 2 mode is lower than the m_r±1 mode in m_t = 1, the candidate "Mode B" changes; we set that case aside for the initial analysis and check it after the m_r-±1 case is found inadequate.)

**Bounding regimes.**

- **Pure-tube regime** (1/L_b ≪ 1/L_a, i.e., L_b ≫ L_a): both modes degenerate at m ≈ 1240/L_a, ratio ≈ 1. Useless for within-pair splits.
- **Pure-ring regime** (1/L_b ≫ 1/L_a, i.e., L_b ≪ L_a): m_A ≈ 1240·f/L_b, m_B ≈ 1240·(1−f)/L_b, ratio = (1−f)/f. This is the regime that gives any within-pair mass split.

For the quark fit, every pair will need to be in the pure-ring regime (L_b ≪ L_a, equivalently ε = L_a/L_b ≫ 1).

---

## 3. The fit: 6 masses, 9 free continuous + 3 discrete

Free parameters: L_1, L_2, L_3 (3 dim sizes) + σ_{12}, σ_{13}, σ_{23} (3 cross-term shears) + χ_{12}, χ_{13}, χ_{23} (3 clover corrugations).

Discrete: τ_{ij} ∈ {±1/3, ±2/3} per pair → 4³ = 64 configurations.

To leading order in the small-corrugation expansion, χ does not modify the mass — it modifies the within-pair charge structure (Q_lobe = +2/3 vs Q_saddle = −1/3, see [clover-quarks.md §11](../../sheet-proton/work/clover-quarks.md)) but the mass spectrum is set by (L, σ_eff). So **χ does not enter the 6-mass-fit at leading order**; the effective continuous DOF is 6 (3 L's + 3 σ's).

6 unknowns to fit 6 observables: **exactly determined**.

Observed quark masses (MeV, current-quark / PDG):

| | gen-1 | gen-2 | gen-3 |
|---|---:|---:|---:|
| **up-type** | u 2.16 | c 1270 | t 173,000 |
| **down-type** | d 4.67 | s 93 | b 4180 |

Within-generation ratios: m_d/m_u ≈ 2.17, m_c/m_s ≈ 13.7, m_t/m_b ≈ 41.4. **Three generations span ~80,000× in mass; within-generation splits span 2× to 41×.**

---

## 4. The sharing constraint forces correlations between pair masses

The 3 pairs share dims pairwise:

- L_1 appears as the **smaller** dim in `Ma(1, 2)` and `Ma(1, 3)` ⇒ both pairs have L_b = L_1.
- L_2 appears as the **smaller** in `Ma(2, 3)` and as the **larger** in `Ma(1, 2)` ⇒ L_b = L_2 in one pair, L_a = L_2 in another.
- L_3 appears as the **larger** in `Ma(1, 3)` and in `Ma(2, 3)` ⇒ both have L_a = L_3.

In the pure-ring regime, the lighter mode mass on a pair is:

<!-- m_A ≈ 1240 · f / L_b -->
$$
m_A \;\approx\; 1240 \cdot \frac{f}{L_b}
$$

For any *pair of pairs sharing the same L_b*, the ratio of their lighter modes is fixed by their f's:

<!-- m_A(P) / m_A(Q) = f_P / f_Q, when L_b(P) = L_b(Q) -->
$$
\frac{m_A^{(P)}}{m_A^{(Q)}} \;=\; \frac{f_P}{f_Q} \quad \text{when } L_b^{(P)} = L_b^{(Q)}.
$$

This is the **sharing constraint** — it ties together two pairs' lighter-mode masses through nothing more than their detuning ratio.

**The constraint that breaks every assignment.** `Ma(1, 2)` and `Ma(1, 3)` both have L_b = L_1. Whichever two generations sit on these two pairs, the ratio of their lighter quarks is fixed at f_{12}/f_{13}. *And both f's are independently fixed by the within-pair (down-type / up-type) mass ratios.* Let me work the three possible assignments:

| Assignment | gens on `Ma(1, 2)`, `Ma(1, 3)` | required f_{12}/f_{13} from m_lighter ratio | predicted f_{12}/f_{13} from within-pair ratios | OK? |
|---|---|---:|---:|:---:|
| A | (u,d) on `Ma(1, 2)`, (s,c) on `Ma(1, 3)` | m_u/m_s = 2.16/95 = 0.023 | f for r=2.17 / f for r=13.7 = 0.314/0.067 = 4.7 | ✗ |
| B | (u,d) on `Ma(1, 2)`, (b,t) on `Ma(1, 3)` | m_u/m_b = 2.16/4180 = 5.2e−4 | 0.314/0.024 = 13.1 | ✗ |
| C | (s,c) on `Ma(1, 2)`, (b,t) on `Ma(1, 3)` | m_s/m_b = 95/4180 = 0.023 | 0.067/0.024 = 2.8 | ✗ |

(Where the predicted f's are derived from solving (1−f)/f = observed within-pair mass ratio.)

In every case the *required* f-ratio (from observed lighter-mode-of-each-pair masses) is off from the *predicted* f-ratio (from observed within-pair mass ratios) by factors of 100 to 25,000. The sharing constraint is *not* satisfiable.

Similar analysis for `Ma(1, 3)` and `Ma(2, 3)` (which share L_a = L_3 but not L_b) gives constraints on the *heavier* modes through 1/L_a contributions — but these only loosen the bind a little because in the pure-ring regime the 1/L_a contribution to mass is subdominant.

---

## 5. What this proves

The §1 ground rules — lowest two closure modes per pair, per-pair (σ, τ, χ), 3 dims for quarks — together **cannot fit the 6 observed quark masses**. The structural reason is the *dim-sharing constraint*: `Ma(1, 2)` and `Ma(1, 3)` have the same L_b, so their lighter-mode mass ratio is determined by their detuning ratio, which is independently determined by their within-pair mass ratios. Both come out, and they disagree by 2–4 orders of magnitude.

This is a *clean negative result* — not "we don't have enough computational power to find a solution," but "the analytical structure has no solution under these constraints."

---

## 6. What relaxes the constraint, in order of intrusion

The §1 rules can be relaxed in several ways; each unlocks one or more orders of magnitude of fit freedom.

1. **Allow `m_t = 2` (or higher) as the second-lowest mode.** Doubles the within-pair mass-ratio reach at fixed L's, because (m_t = 2, m_r = round(2 σ_eff)) gives a mode at m ≈ 2·1240/L_a = 2480/L_a regardless of ε — independent of L_b. Still in the "lowest energy windings" family (just slightly higher). Cheapest relaxation. **Recommended first move.**

2. **Allow within-pair χ to perturb mass beyond leading order.** χ enters mass at O(η²) where η = r_lobe/R (see [clover-mass.md §6](../../sheet-proton/work/clover-mass.md)). For deep corrugation (χ ~ 0.01 or χ ~ 100), this can be a *significant* contribution. Adds 3 continuous DOF that were previously fitting-irrelevant. Lifts the 6→9 unknowns vs 6 equations problem to 9→9, with χ-dependence as the third effective lever.

3. **Allow 4 dims (m1, m2, m3, m4) for quarks.** Adds 1 dim and up to 3 more pairs. Drops the strict sharing constraint between P_{12} and P_{13}. Mildly violates the "3 dims" rule.

4. **Allow 6 dims with each quark on its own pair.** 6 pairs from 6 dims — no sharing forces a correlation, every pair fits its own quark independently. Trivially has enough DOF but loses the "structural 3 generations" payoff.

5. **The dual-role pair-shape mechanism per [architecture.md §3.4](architecture.md).** If the simple-clover working hypothesis (pair-triplet (σ, τ, P)) is wrong and a different mechanism is right (mode-resolution filtering, GRID lattice fingerprint, etc.), the math under a different mechanism may close where this one does not.

---

## 7. Numerical verification of the negative result

Spot-check via [scripts/quark_search_sharing_check.py](../scripts/quark_search_sharing_check.py); output in [outputs/quark_search_sharing_check.txt](../outputs/quark_search_sharing_check.txt).

For each of the three (`Ma(1, 2)`, `Ma(1, 3)`) assignments, solve for f from the observed within-generation mass ratio, then solve for L_b from each pair's lighter-mode mass. Sharing requires the two L_b values to coincide.

| Assignment | gen on `Ma(1, 2)` | gen on `Ma(1, 3)` | f_{12} | f_{13} | L_b from `Ma(1, 2)` | L_b from `Ma(1, 3)` | Ratio | OK? |
|---|---|---|---:|---:|---:|---:|---:|:---:|
| A | (u, d) | (s, c) | 0.316 | 0.068 | **181.5 fm** | **0.910 fm** | 200× | ✗ |
| B | (u, d) | (b, t) | 0.316 | 0.024 | **181.5 fm** | **0.007 fm** | 25,900× | ✗ |
| C | (s, c) | (b, t) | 0.068 | 0.024 | **0.910 fm** | **0.007 fm** | 130× | ✗ |

The negative result is confirmed. The smallest sharing-inconsistency (Assignment C, 130×) is itself 2+ orders of magnitude — there's no chance of closing the gap with subleading effects (χ-corrections at O(η²), shear-corrections at O(σ_eff²), etc.).

---

## 8. Recommendation (historical) and what actually happened

The math + numerical verification together say **the §1 ground rules don't work** on the triangle `Ma((1,2), (1,3), (2,3))` — and the failure margin is wide enough that this isn't a borderline result that small tweaks might rescue.

Three relaxations from §6 were on the table:

1. Allow m_t = 2 as the second-lowest mode per pair (Relaxation 1).
2. Drop the "3 dims for quarks" rule.
3. Drop the simple-clover working hypothesis.

**What was tried:**

- **Relaxation 1 alone** on the original triangle: see §10. Closes at 3.97% with both m_t = 2 and per-pair tube/ring choice — viable but loose.
- **Relaxation 2 (4-dim wye)**: see §9. Closes at 0.499% using only the lowest two closure modes T(1, 1) and T(1, 2) per pair — clean and preferred.

The 4-dim wye is the working choice. Relaxation 1 on the 3-dim triangle is kept as a structurally simpler fallback.

---

## 9. The wye topology Ma((1,5), (3,5), (4,5)) — closes the fit at < 1% accuracy

After the §1–§8 obstruction, the topology was revised to a **wye/star** on 4 dims:

  **quark pairs: `Ma((1, 5), (3, 5), (4, 5))`**

with **m5 common to all 3 pairs**, and 4 total quark-region dims (m1, m3, m4, m5; m2 is reserved for the electron sector — see [candidates.md](candidates.md)). This is *structurally different* from the §1 triangle in a decisive way: m5 (the largest of the quark-region dims) can play the **tube** role in every pair, with m1, m3, m4 each playing **ring** in their respective pairs.

### 9.1 Why this works where §1 failed

The §1 triangle `Ma((1,2), (1,3), (2,3))` shared L_b (the smaller, ring-role dim) between two pairs. That forced two pairs' lighter-mode masses into a fixed ratio set by their f-detunings — the §4 obstruction.

The wye topology has all three pairs share **L_T (the larger, tube-role dim)** = L_5. In the pure-ring regime (L_T ≫ L_R), the mass formula

  m² ≈ (2π ℏc)² · ((1/L_T²) + (δ²/L_R²)) ≈ (2π ℏc)² · δ²/L_R²

is dominated by 1/L_R, *not* 1/L_T. **A shared L_T does not couple the lighter-mode masses across pairs.** Each pair has its own L_R, giving its own mass scale independently.

### 9.2 The fit — uses only the T(1, 1) and T(1, 2) closure modes per pair

Each pair hosts its two lowest **valid closure modes**: **T(1, 2) for the lighter quark and T(1, 1) for the heavier quark of each generation**. These are the natural closure-compatible windings inherited from [sheet-proton clover-quarks.md §12](../../sheet-proton/work/clover-quarks.md) (neutron path = T(1, 1), proton path = T(1, 2)).

With σ_eff in (1.5, 2), T(1, 2) sits closer to σ_eff (smaller detuning, lighter) and T(1, 1) sits further (larger detuning, heavier). Solve σ_eff per pair from within-pair mass ratio R = m_heavier/m_lighter:

  σ_eff = (2R + 1)/(R + 1)

then L_ring from m_lighter ≈ 2π·ℏc·(2−σ_eff)/L_ring. Size-ordered assignment: the **smallest** ring holds the **heaviest** generation (since m ~ 1/L_ring). The QY quark wye is fit within any candidate by [scripts/cand_solver.py](../scripts/cand_solver.py); see [outputs/cand_QY-ED.txt](../outputs/cand_QY-ED.txt).

| Pair | Generation (lighter, heavier) | Modes | within-pair ratio | σ_eff | L_ring (fm) |
|---|---|---|---:|---:|---:|
| `Ma(1, 5)` | (b, t) — generation 3 | b at T(1, 2), t at T(1, 1) | 41.39 | **1.9764** | **L_1 = 0.007** |
| `Ma(3, 5)` | (s, c) — generation 2 | s at T(1, 2), c at T(1, 1) | 13.65 | **1.9318** | **L_3 = 0.9096** |
| `Ma(4, 5)` | (u, d) — generation 1 | u at T(1, 2), d at T(1, 1) | 2.17 | **1.6837** | **L_4 = 181.5** |

(Note: in our convention T(1, 2) is the *lighter* mode of a pair — smaller detuning δ = 2 − σ_eff — and T(1, 1) is the *heavier* — larger detuning δ = 1 − σ_eff. Size-ordering of the ring dims puts the heaviest generation on the smallest ring m1: top and bottom both live on `Ma(1, 5)`. Index m2 is skipped because it is the lepton-scale dim, not part of the quark wye.)

Notice σ_eff for the heaviest pair `Ma(1, 5)` sits at **1.976** — essentially the same value as R53's e-sheet "magic shear" σ_eff ≈ 2.004 (which produces the electron at T(1, 2)). The quark sector's σ_eff values converge toward 2 as the generation gets heavier; the (t, b) pair is essentially at the R53 charged-lepton operating point. **This is suggestive of a structural relation** between the quark and electron sectors of the architecture.

L_5 (the common tube) only needs to be large enough that L_T ≫ L_R/f in each pair — the strictest is L_5 ≫ 574 fm. **Pick L_5 = 5740 fm** (10× margin).

### 9.3 Verification — all 6 quark masses fit to < 1%

Using the **full** mass formula (not just the pure-ring approximation), with all 6 quarks at (m_t, m_r) ∈ {(1, 1), (1, 2)}:

| Pair | Mode | Quark | δ = m_r − σ_eff | m predicted | m observed | % error |
|---|---|---|---:|---:|---:|---:|
| `Ma(4, 5)` | T(1, 2) | u | +0.3163 | 2.171 MeV | 2.16 MeV | **+0.50%** |
| `Ma(4, 5)` | T(1, 1) | d | −0.6837 | 4.675 MeV | 4.67 MeV | **+0.11%** |
| `Ma(3, 5)` | T(1, 2) | s | +0.0682 | 93.0 MeV | 93.0 MeV | **+0.00%** |
| `Ma(3, 5)` | T(1, 1) | c | −0.9318 | 1270 MeV | 1270 MeV | **+0.00%** |
| `Ma(1, 5)` | T(1, 2) | b | +0.0236 | 4180 MeV | 4180 MeV | **+0.00%** |
| `Ma(1, 5)` | T(1, 1) | t | −0.9764 | 173,000 MeV | 173,000 MeV | **+0.00%** |

**Maximum |Δ%| = 0.499%** (the u quark; the rest are below 0.2%). All six quark masses are reproduced from a structural geometry plus 3 free σ_eff-values per pair, with **every quark at one of the two valid closure modes T(1, 1) or T(1, 2)** — no exotic windings, no m_t > 1.

### 9.4 The fitted geometry

The 4 quark-region dim sizes (size-ordered; m2 is skipped, reserved for the e-sector):

| Dim | Size | Role | Note |
|---|---:|---|---|
| L_1 | 0.007 fm | (t, b) ring | ≈ top-quark Compton wavelength |
| L_3 | 0.91 fm | (c, s) ring | ≈ charm Compton wavelength |
| L_4 | 181 fm | (u, d) ring | ≈ electron-scale (!) |
| L_5 | ≳ 5740 fm | common tube (hub of wye) | ≈ μm-scale; "fat" dim shared across all 3 pairs |

The L_5 lower bound (5740 fm) is set by the pure-ring regime; larger values work equally well. So L_5 is one continuous free parameter, with the fit determining only L_1, L_3, L_4, and 3 f-values.

### 9.5 Architectural implication: per-pair tube/ring choice (not size-determined)

This result invalidates the older "smaller = tube" convention. The wye topology requires the **larger** dim (L_5) to play tube in all 3 quark pairs (the R53-style fat-torus regime, applied per-pair to a single common tube). The tube/ring assignment is therefore a **per-pair structural choice**, not determined by which dim is smaller. Reflected in [architecture.md §3.1](architecture.md).

### 9.6 Generalization to electron and neutrino sectors

The full multi-sector proposal is documented in [candidates.md](candidates.md). In brief: the electron sector adds a new lepton-scale dim m2 (≈ 0.7 fm) and uses three pairs in a delta `Ma((2, 4), (2, 5), (4, 5))` (Candidates B and C), reusing m4 and m5 from the quark sector. The neutrino sector either uses a single pair `Ma(6, 7)` on fresh dims (Candidates A/B) or a third delta `Ma((6, 7), (6, 8), (7, 8))` on its own ν-region dims (Candidate C, the working choice).

### 9.7 What this resolves and what's next

**Resolved (the immediate Phase 1 goal):**

- A 4-dim quark sector (not 3-dim) with the wye topology fits all 6 quark masses to < 1%.
- The lowest-energy windings (m_t = 1, m_r ∈ {1, 2}) suffice — no need to invoke higher modes.
- The simple clover (per [architecture.md §3.4](architecture.md)) is consistent; χ values can be anything (the fit doesn't constrain them at leading order).
- The smaller-as-tube convention is *not* universal; per-pair tube/ring is the correct architectural rule.

**Open next steps:**

1. **Update [architecture.md §3.1](architecture.md)** to remove the smaller-as-tube assumption; replace with per-pair-choice convention. ✓ done.
2. **Phase 2 (electron sector)**: documented in [candidates.md §2](candidates.md). Delta `Ma((2, 4), (2, 5), (4, 5))` fits (m_e, m_μ, m_τ) to machine precision with L_2 ≈ 0.7 fm and σ_eff values in the natural range (no R53 fine-tuning).
3. **Phase 3 (neutrino sector)**: documented in [candidates.md §3](candidates.md). Candidate C uses a ν-region delta `Ma((6, 7), (6, 8), (7, 8))` on fresh dims (decoupled from the e-sector), with L_6, L_7, L_8 in the cm-m range; closes to machine precision. The original concern (§11 below) — that a single ν pair couldn't host 3 mass eigenstates and would need a macroscopic L — was resolved by giving the ν sector its own delta on fresh dims.
4. **Mathematical formalization** (Phase 5 per STATUS.md): if Phase 4 coherence checks pass, write up the unified architecture in `ma-domain/` proper as a derivation, not a fit.

---

## 10. Parallel path: Relaxation 1 on the original triangle Ma((1,2), (1,3), (2,3))

The §1–§8 negative result was revisited with the "lowest energy windings" rule relaxed to allow **m_t = 2 as the second-lowest closure mode per pair**, AND the per-pair tube/ring choice now available from [architecture.md §3.1](architecture.md). Script: [scripts/quark_search_relaxation_1.py](../scripts/quark_search_relaxation_1.py); output: [outputs/quark_search_relaxation_1.txt](../outputs/quark_search_relaxation_1.txt).

### 10.1 What was tested

Sweep over (6 gen→pair) × (2³ mode-B per pair: `mr-shift` or `mt-2`) × (2³ tube/ring per pair: `smaller` or `larger`) = **384 configurations**. For each, attempt a least-squares fit of (L_1, L_2, L_3, σ_eff for each of the 3 pairs) — 6 free continuous unknowns vs 6 observed masses.

### 10.2 Result — Relaxation 1 does find fits, but worse than the wye

| Threshold | Configs hitting it |
|---|---:|
| < 200% | 64 / 384 |
| < 50% | 6 / 384 |
| < 10% | 5 / 384 |
| < 5% | 5 / 384 |
| < 1% | **0 / 384** |

**Best fit: max |Δ%| = 3.97%**, achieved by 4 mirror-equivalent configurations. One representative:

- **Assignment**: (u, d) → `Ma(1, 3)`, (s, c) → `Ma(2, 3)`, (b, t) → `Ma(1, 2)`
- **Mode-B per pair**: `Ma(1, 2)` = `mr-shift`, `Ma(1, 3)` = `mt-2`, `Ma(2, 3)` = `mr-shift`
- **Tube/ring**: all three pairs in **fat-torus** regime (larger dim as tube)
- **Dim sizes**: L_1 = 0.0073 fm, L_2 = 1.05 fm, L_3 = 80 μm — span 7 orders of magnitude
- **σ_eff per pair**: 0.92, 0.024, 0.00 — mix of near-resonance and mid-detuning

Notably:

- The fit *requires* both relaxations (m_t = 2 and per-pair tube/ring); neither alone closes the obstruction.
- Best 5 configs all have similar L's and σ's (mirror permutations), suggesting a unique solution up to relabeling.
- The 4% residual cannot be driven below ~3.9% without further relaxations — suggests the 3-dim topology is structurally tight even with both relaxations.

### 10.3 Comparison to the wye topology

| Topology | Best fit | Dims needed | Mode B per pair | Tube/ring per pair | DOF margin |
|---|---:|---:|---|---|---|
| Wye `Ma((1,5),(3,5),(4,5))` | **0.50%** | 4 (+ L_5 free) | uniform `T(1, 1)` (no relaxation) | uniform `larger` (hub as tube) | 1 free L |
| Triangle `Ma((1,2),(1,3),(2,3))` (+ relaxation) | 3.97% | 3 | mixed `mr-shift`/`mt-2` | uniform `larger` | 0 free |

**The wye topology is the clear winner.** It achieves an 8× tighter fit with the simpler "lowest 2 modes" rule (no m_t = 2 needed) and a uniform fat-torus convention across pairs. The 3-dim triangle with Relaxation 1 is feasible but tighter and structurally less clean.

### 10.4 Verdict on parallel paths

Both paths give viable quark sectors, but with different cost/quality trade-offs:

- **Path A (4-dim wye)**: ✓ confirmed working at 0.5%; preferred. Adopted by all three candidates in [candidates.md](candidates.md).
- **Path B (3-dim triangle with Relaxation 1)**: ✓ works at 4%; deprioritized but kept as a structurally simpler fallback if the 4-dim picture runs into trouble downstream.

---

## 11. ν-sector viability concern (raised when ν was planned to share dims with the e-sector)

This concern arose when the ν sector was planned as a single pair sharing the e-sector's new dim, with the other ν dim free.

ν mass scales: m_ν₁ ≈ 30 meV, m_ν₃ ≈ 60 meV. That's 3 × 10⁻⁸ to 6 × 10⁻⁸ MeV.

For a mode in any regime, the mass formula

  m ≈ 2πℏc × max(1/L_T, δ/L_R)

requires at least one of L_T or L_R to be at the macroscopic scale:

- **Fat-torus, δ = 0.1**: L_R = 2πℏc × δ / m = 1240 × 0.1 / 3 × 10⁻⁸ MeV ≈ **4 × 10⁹ fm = 4 mm**.
- **Fat-torus, δ = 0.001 (very near resonance)**: L_R ≈ **40 μm**.
- **Thin-torus**: L_T ≈ **4 cm** (much larger).

So any ν pair needs at least one dim at mm–cm scale.

If the e-sector pins its new dim L_2 ≈ 0.7 fm (which the natural-scale fit does — see [candidates.md §3](candidates.md)), then sharing m2 with the ν sector is no longer viable: any pair containing m2 has a mass floor of 2πℏc/L_2 ≈ 1770 MeV, ~10 orders of magnitude above the meV ν scale.

**Resolution: the ν sector lives on FRESH dims.** Candidate C adopts a ν-delta `Ma((6, 7), (6, 8), (7, 8))` on three fresh dims (m6, m7, m8), all free parameters. The fit closes to machine precision with L_6 ≈ 7 cm, L_7 ≈ 2 cm, L_8 ≈ 4 cm. The macroscopic L's are accepted as free architectural parameters; their structural justification (or whether the dim-size hierarchy admits an upper bound on adjacent ratios) remains open and is tracked in [STATUS.md Phase 3](STATUS.md).

Alternative resolution (Candidate B fallback): keep the single pair `Ma(6, 7)` on fresh dims, admit sign-flipped m_t modes per metric-charge ch. 4 (T(1, 1), T(−1, 1), T(1, 2) — 3 modes), and force L_6 ≳ 4 cm. Closes to ~1% — see [candidates.md §4](candidates.md).

---

## 12. Cross-references

- [architecture.md](architecture.md) — sets the per-pair (σ, τ, χ) free-parameter structure used here; pair-label `Ma(i, j)` convention in §2.1.
- [STATUS.md](STATUS.md) Phase 1 — this file is the first Phase 1 deliverable.
- [candidates.md](candidates.md) — full multi-sector elaboration of the §9 wye quark result.
- [sheet-proton clover-quarks.md §11](../../sheet-proton/work/clover-quarks.md) — per-arc charge derivation (the Q_lobe = +2/3, Q_saddle = −1/3 result is preserved across any choice of L's and σ's and is the within-pair u/d distinction; it does *not* set the within-pair mass split).
- [sheet-proton clover-mass.md §4](../../sheet-proton/work/clover-mass.md) — mass formula μ² = (m_r − σ_eff m_t)² + (m_t/ε)² adopted here.
- [3-torus.md §5.1](3-torus.md) — the original "2-scale obstruction" from the bare 2D-planar mode structure on a single 3-torus; the present §4 is the sharper, fit-level version of the same obstruction.
