# quark-search.md — Three quark generations on three Ma dimensions

**Status:** Rough cut. Sets up the mass-formula structure for 6 quarks on 3 dim-pairs of (m1, m2, m3), works the analytical structure to see whether the dim-sharing leaves enough freedom to fit, and reports honestly on what does and does not close.

**Working ground rules** (per user, this thread):
1. **Only lowest-energy closure modes.** Each pair hosts its 2 lowest closure modes; those 2 modes are the 2 quarks of one generation.
2. **Custom shear per pair.** Each pair (i, j) has its own σ_{ij}.
3. **Custom clover per pair.** Each pair has its own χ_{ij} = r_saddle / r_lobe.
4. **τ ∈ {±1/3, ±2/3} per pair.** Discrete choice.
5. **Quarks live on 3 dims**: m1, m2, m3.

The deliverable here is a *rough cut*; the formalization moves to `ma-6/` proper if the rough cut closes (per [STATUS.md](STATUS.md) Phase 5).

---

## 1. Setup

Three Ma dims with sizes L₁ < L₂ < L₃ (size-ordered per [architecture.md §1](architecture.md)). Three pairs:

| Pair | Smaller | Larger |
|---|---|---|
| P_{12} | m1 | m2 |
| P_{13} | m1 | m3 |
| P_{23} | m2 | m3 |

Each dim appears in exactly **2** pairs. This sharing is the structural feature that will dominate the analysis below.

Each pair (i, j) carries a triplet (σ_{ij}, τ_{ij}, χ_{ij}) per [architecture.md §3.4](architecture.md). The mass formula (adapted from [sheet-proton clover-mass.md §4](../../sheet-proton/work/clover-mass.md)) on a pair, in terms of mode windings (m_t, m_r):

<!-- m² = (2πℏc)² · ((m_t / L_a)² + ((m_r − σ_eff · m_t) / L_b)²) -->
$$
m^2 \;=\; (2\pi \hbar c)^2 \cdot \left[ \left(\frac{m_t}{L_a}\right)^2 \;+\; \left(\frac{m_r - \sigma_{\mathrm{eff}}\, m_t}{L_b}\right)^2 \right]
$$

where for pair (i, j):
- **L_a** = larger dim of pair (plays "tube circumference" in the cross-term/twist structure)
- **L_b** = smaller dim of pair (plays "ring circumference")
- **σ_eff = σ_{ij} + 2 τ_{ij}** is the effective cross-term coefficient

*Note on convention.* The tube/ring assignment here follows the R53 charged-lepton regime where ε = L_tube / L_ring can be > 1 (fat torus); the smallest-as-tube rule from [architecture.md §3.2](architecture.md) is the *proton-sheet* convention but does not survive to ε >> 1. For the quark fit below we keep "L_a > L_b" so ε = L_a/L_b > 1 always.

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

Free parameters: L₁, L₂, L₃ (3 dim sizes) + σ_{12}, σ_{13}, σ_{23} (3 cross-term shears) + χ_{12}, χ_{13}, χ_{23} (3 clover corrugations).

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

- L₁ appears as the **smaller** dim in P_{12} and P_{13} ⇒ both pairs have L_b = L₁.
- L₂ appears as the **smaller** in P_{23} and as the **larger** in P_{12} ⇒ L_b = L₂ in one pair, L_a = L₂ in another.
- L₃ appears as the **larger** in P_{13} and in P_{23} ⇒ both have L_a = L₃.

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

**The constraint that breaks every assignment.** P_{12} and P_{13} both have L_b = L₁. Whichever two generations sit on these two pairs, the ratio of their lighter quarks is fixed at f_{12}/f_{13}. *And both f's are independently fixed by the within-pair (down-type / up-type) mass ratios.* Let me work the three possible assignments:

| Assignment | gens on P_{12}, P_{13} | required f_{12}/f_{13} from m_lighter ratio | predicted f_{12}/f_{13} from within-pair ratios | OK? |
|---|---|---:|---:|:---:|
| A | (u,d) on P_{12}, (s,c) on P_{13} | m_u/m_s = 2.16/95 = 0.023 | f for r=2.17 / f for r=13.7 = 0.314/0.067 = 4.7 | ✗ |
| B | (u,d) on P_{12}, (b,t) on P_{13} | m_u/m_b = 2.16/4180 = 5.2e−4 | 0.314/0.024 = 13.1 | ✗ |
| C | (s,c) on P_{12}, (b,t) on P_{13} | m_s/m_b = 95/4180 = 0.023 | 0.067/0.024 = 2.8 | ✗ |

(Where the predicted f's are derived from solving (1−f)/f = observed within-pair mass ratio.)

In every case the *required* f-ratio (from observed lighter-mode-of-each-pair masses) is off from the *predicted* f-ratio (from observed within-pair mass ratios) by factors of 100 to 25,000. The sharing constraint is *not* satisfiable.

Similar analysis for P_{13} and P_{23} (which share L_a = L₃ but not L_b) gives constraints on the *heavier* modes through 1/L_a contributions — but these only loosen the bind a little because in the pure-ring regime the 1/L_a contribution to mass is subdominant.

---

## 5. What this proves

The user's working ground rules — lowest two closure modes per pair, per-pair (σ, τ, χ), 3 dims for quarks — together **cannot fit the 6 observed quark masses**. The structural reason is the *dim-sharing constraint*: P_{12} and P_{13} have the same L_b, so their lighter-mode mass ratio is determined by their detuning ratio, which is independently determined by their within-pair mass ratios. Both come out, and they disagree by 2–4 orders of magnitude.

This is a *clean negative result* — not "we don't have enough computational power to find a solution," but "the analytical structure has no solution under these constraints."

---

## 6. What relaxes the constraint, in order of intrusion

The user's rules can be relaxed in several ways; each unlocks one or more orders of magnitude of fit freedom.

1. **Allow `m_t = 2` (or higher) as the second-lowest mode.** Doubles the within-pair mass-ratio reach at fixed L's, because (m_t = 2, m_r = round(2 σ_eff)) gives a mode at m ≈ 2·1240/L_a = 2480/L_a regardless of ε — independent of L_b. Still in the "lowest energy windings" family (just slightly higher). Cheapest relaxation. **Recommended first move.**

2. **Allow within-pair χ to perturb mass beyond leading order.** χ enters mass at O(η²) where η = r_lobe/R (see [clover-mass.md §6](../../sheet-proton/work/clover-mass.md)). For deep corrugation (χ ~ 0.01 or χ ~ 100), this can be a *significant* contribution. Adds 3 continuous DOF that were previously fitting-irrelevant. Lifts the 6→9 unknowns vs 6 equations problem to 9→9, with χ-dependence as the third effective lever.

3. **Allow 4 dims (m1, m2, m3, m4) for quarks.** Adds 1 dim and up to 3 more pairs. Drops the strict sharing constraint between P_{12} and P_{13}. Mildly violates the "3 dims" rule.

4. **Allow 6 dims with each quark on its own pair.** 6 pairs from 6 dims — no sharing forces a correlation, every pair fits its own quark independently. Trivially has enough DOF but loses the "structural 3 generations" payoff.

5. **The dual-role pair-shape mechanism per [architecture.md §3.4](architecture.md).** If the simple-clover working hypothesis (pair-triplet (σ, τ, P)) is wrong and a different mechanism is right (mode-resolution filtering, GRID lattice fingerprint, etc.), the math under a different mechanism may close where this one does not.

---

## 7. Numerical verification of the negative result

Spot-check via [scripts/quark_search_sharing_check.py](../scripts/quark_search_sharing_check.py); output in [outputs/quark_search_sharing_check.txt](../outputs/quark_search_sharing_check.txt).

For each of the three (P_{12}, P_{13}) assignments, solve for f from the observed within-generation mass ratio, then solve for L_b from each pair's lighter-mode mass. Sharing requires the two L_b values to coincide.

| Assignment | gen on P_{12} | gen on P_{13} | f_{12} | f_{13} | L_b from P_{12} | L_b from P_{13} | Ratio | OK? |
|---|---|---|---:|---:|---:|---:|---:|:---:|
| A | (u, d) | (s, c) | 0.316 | 0.068 | **181.5 fm** | **0.910 fm** | 200× | ✗ |
| B | (u, d) | (b, t) | 0.316 | 0.024 | **181.5 fm** | **0.007 fm** | 25,900× | ✗ |
| C | (s, c) | (b, t) | 0.068 | 0.024 | **0.910 fm** | **0.007 fm** | 130× | ✗ |

The negative result is confirmed. The smallest sharing-inconsistency (Assignment C, 130×) is itself 2+ orders of magnitude — there's no chance of closing the gap with subleading effects (χ-corrections at O(η²), shear-corrections at O(σ_eff²), etc.).

---

## 8. Recommendation

The math + numerical verification together say **the strict ground rules don't work** — and the failure margin is wide enough that this isn't a borderline result that small tweaks might rescue.

Three relaxations are worth considering, ranked by how much they perturb the user's ground rules:

1. **Allow m_t = 2 as the second-lowest mode per pair** (Relaxation 1 from §6). Cheapest. Still "lowest-energy windings" in a slightly broader sense. The m_t = 2 mode has mass ~ 2·1240/L_a (in the pure-ring regime), independent of L_b — so it breaks the sharing correlation that defeated the m_r-±1 assignment. ~1 day of scripting; if it works, great; if not, we know much more about what's going on.

2. **Drop the "3 dims for quarks" rule.** 4 or 5 dims removes the strict pairwise sharing that makes the L_b values coincide. Mild architectural shift; the "3 quark generations" payoff is unchanged because we still pick 3 generation-bearing pairs from a larger pool.

3. **Drop the simple-clover working hypothesis.** Per [architecture.md §3.4](architecture.md), the pair-shape mechanism is one of several candidates; if mode-resolution filtering, GRID lattice fingerprint, or another alternative is the correct deeper structure, the mass-fit problem has different boundary conditions and may close where this one does not.

**My recommendation: try Relaxation 1 first.** It's the cheapest and the most directly informative — either the m_t = 2 mode breaks the obstruction (and we have a working quark sector), or it doesn't (and we have a stronger structural statement about why 3 dims is insufficient).

If you agree, the natural follow-up is a `quark-search-2mt.md` extension implementing the m_t = 2 mode allowance. Until then, the [STATUS.md](STATUS.md) Phase 1 checklist should reflect that the simplest version of the quark sector did not close, and the next move is Relaxation 1.

---

## 9. The user's alternative topology — closes the fit at < 1% accuracy

The user proposed the alternative topology

  **quark pairs: (1, 3), (2, 3), (3, 4)**

with **dim 3 common to all 3 pairs**, and 4 total quark-region dims (1, 2, 3, 4) instead of 3. This is *structurally different* from the §1 topology in a decisive way: dim 3 can play the **tube** (larger) role in every pair, with dims 1, 2, 4 each playing **ring** in their respective pairs.

### 9.1 Why this works where §1 failed

The §1 topology (1,2)(1,3)(2,3) shared L_b (the smaller, ring-role dim) between pairs P_{12} and P_{13}. That forced two pairs' lighter-mode masses into a fixed ratio set by their f-detunings — the §4 obstruction.

The user's topology has all three pairs share **L_T (the larger, tube-role dim)**. In the pure-ring regime (L_T ≫ L_R), the mass formula

  m² ≈ (2π ℏc)² · ((1/L_T²) + (δ²/L_R²)) ≈ (2π ℏc)² · δ²/L_R²

is dominated by 1/L_R, *not* 1/L_T. **A shared L_T does not couple the lighter-mode masses across pairs.** Each pair has its own L_R, giving its own mass scale independently.

### 9.2 The fit

Compute f per pair from the within-pair mass ratio (1−f)/f, then solve for L_R per pair from the lighter quark mass. Script: [scripts/quark_search_user_topology.py](../scripts/quark_search_user_topology.py); output: [outputs/quark_search_user_topology.txt](../outputs/quark_search_user_topology.txt).

| Pair | Quarks | within-pair ratio | f | L_ring (fm) |
|---|---|---:|---:|---:|
| (1, 3) | (u, d) | 2.17 | 0.3163 | **L_1 = 181.5** |
| (2, 3) | (s, c) | 13.65 | 0.0682 | **L_2 = 0.9096** |
| (3, 4) | (b, t) | 41.39 | 0.0236 | **L_4 = 0.007** |

L_3 (the common tube) only needs to be large enough that L_T ≫ L_R/f in each pair — the strictest is L_3 ≫ 574 fm. **Pick L_3 = 5740 fm** (10× margin).

### 9.3 Verification — all 6 quark masses fit to < 1%

Using the **full** mass formula (not just the pure-ring approximation):

| Pair | Mode | δ | m predicted | m observed | % error |
|---|---|---:|---:|---:|---:|
| (1, 3) | u (lighter) | 0.3163 | 2.171 MeV | 2.16 MeV | **+0.50%** |
| (1, 3) | d (heavier) | 0.6837 | 4.675 MeV | 4.67 MeV | **+0.11%** |
| (2, 3) | s (lighter) | 0.0682 | 93.0 MeV | 93.0 MeV | **+0.00%** |
| (2, 3) | c (heavier) | 0.9318 | 1270 MeV | 1270 MeV | **+0.00%** |
| (3, 4) | b (lighter) | 0.0236 | 4180 MeV | 4180 MeV | **+0.00%** |
| (3, 4) | t (heavier) | 0.9764 | 173,000 MeV | 173,000 MeV | **+0.00%** |

**Maximum |Δ%| = 0.499%** (the u quark; the rest are below 0.2%). All six quark masses are reproduced from a structural geometry plus 3 free f-values (equivalently, 3 free σ-shears per pair) and a small (sub-percent) approximation correction from the L_T residual.

### 9.4 The fitted geometry

The 4 quark-region dim sizes (sorted smallest → largest):

| Dim role | Size | Note |
|---|---:|---|
| L_4 (b/t ring) | 0.007 fm | ≈ top-quark Compton wavelength |
| L_2 (s/c ring) | 0.91 fm | ≈ charm Compton wavelength |
| L_1 (u/d ring) | 181 fm | ≈ electron-scale (!) |
| L_3 (common tube) | ≳ 5740 fm | ≈ μm-scale; "fat" dim shared across all 3 pairs |

The L_3 lower bound (5740 fm) is set by the pure-ring regime; larger values work equally well. So L_3 is one continuous free parameter, with the fit determining only L_1, L_2, L_4, and 3 f-values.

### 9.5 Architectural implication: per-pair tube/ring choice (not size-determined)

This result invalidates the architecture.md §3.1 "smaller = tube" convention. The user's topology requires the **larger** dim (L_3) to play tube in all 3 quark pairs (the R53-style fat-torus regime, applied per-pair to a single common tube). The tube/ring assignment is therefore a **per-pair structural choice**, not determined by which dim is smaller.

To be reflected in architecture.md: §3.1 needs revision to make tube/ring assignment per-pair-free, with the user's topology providing the existence proof.

### 9.6 Generalization to electron and neutrino sectors — open

The user's full proposal:

- e pairs: (2, 4), (3, 5), (4, 5)
- ν pair: (5, 6)

With dims 2, 3, 4 inherited from the quark fit, this constrains the electron L's to (L_2 = 0.91 fm, L_3 = 5740 fm, L_4 = 0.007 fm) — the quark values must continue to apply in the electron pairs they appear in. L_5 (and L_6) are free.

The electron sector then has to fit (m_e, m_μ, m_τ) using these inherited L's plus L_5 and per-pair (σ, τ, χ). This is the next phase 2 deliverable; not yet computed.

### 9.7 What this resolves and what's next

**Resolved (the immediate Phase 1 goal):**

- A 4-dim quark sector (not 3-dim) with the user's topology fits all 6 quark masses to < 1%.
- The lowest-energy windings (m_t = 1, m_r = closest integer to σ_eff) suffice — no need to invoke higher modes.
- The simple clover (per [architecture.md §3.4](architecture.md)) is consistent; χ values can be anything (the fit doesn't constrain them at leading order).
- The smaller-as-tube convention is *not* universal; per-pair tube/ring is the correct architectural rule.

**Open next steps:**

1. **Update [architecture.md §3.1](architecture.md)** to remove the smaller-as-tube assumption; replace with per-pair-choice convention.
2. **Phase 2 (electron sector)**: solve for L_5 + e-pair (σ, τ, χ) values that reproduce (m_e, m_μ, m_τ) with the inherited L_2, L_3, L_4 from the quark fit.
3. **Phase 3 (neutrino sector)**: check whether L_5, L_6 + ν-pair structure works for the 3 neutrino masses.
4. **Mathematical formalization** (Phase 5 per STATUS.md): if Phases 2 and 3 also close, write up the unified architecture in `ma-6/` proper as a derivation, not a fit.

---

## 8. Cross-references

- [architecture.md](architecture.md) — sets the per-pair (σ, τ, χ) free-parameter structure used here.
- [STATUS.md](STATUS.md) Phase 1 — this file is the first Phase 1 deliverable.
- [sheet-proton clover-quarks.md §11](../../sheet-proton/work/clover-quarks.md) — per-arc charge derivation (the Q_lobe = +2/3, Q_saddle = −1/3 result is preserved across any choice of L's and σ's and is the within-pair u/d distinction; it does *not* set the within-pair mass split).
- [sheet-proton clover-mass.md §4](../../sheet-proton/work/clover-mass.md) — mass formula μ² = (m_r − σ_eff m_t)² + (m_t/ε)² adopted here.
- [3-torus.md §5.1](3-torus.md) — the original "2-scale obstruction" from the bare 2D-planar mode structure on a single 3-torus; the present §4 is the sharper, fit-level version of the same obstruction.
