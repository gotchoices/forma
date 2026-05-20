# wye-ladder.md — Two-wye ladder with shared rings

**Status:** Tested and deprioritized. Replaces sym-ladder's failed proton-delta with a proton-wye, and uses a matching electron-wye that *shares ring dims* with the quark wye. The neutrino sector was to live on a 1D shaped substrate per [neutrino-1D.md](neutrino-1D.md). The architecture's headline appeal was a *unified R53 mechanism* across all charged leptons. **The numerical e-wye fit (§3.3) does not support that appeal** — the σ_eff values come out scattered (one extremely fine-tuned to 1.9994), wider in range than Candidate C's. Wye-ladder is documented here as a tested alternative; Candidate C remains the working topology. See §7 for the net assessment and conditions under which wye-ladder should be re-pursued.

**Cross-references:**
- [sym-ladder.md](sym-ladder.md) — previous ladder candidate; its proton-delta failed (Test A 137%, Test B 1784%). The structural lessons learned there motivate the wye-only ladder here.
- [candidates.md](candidates.md) — current working topology (Candidate C: wye + delta + delta) that wye-ladder competes with.
- [neutrino-1D.md](neutrino-1D.md) — 1D shaped-substrate model for the neutrino sector used here.
- [electron-tube.md](electron-tube.md) — convex-tube R53-mechanism that makes T(1, 2) the lightest mode on a sheet with σ_eff ≈ 2.
- [quark-search.md §9](quark-search.md) — the wye-fit result that establishes the quark wye works at < 1% across all 6 quark masses.

---

## 1. Structure

```
        m3
        |
        p
        |
        m4
       /  \
      p    p
     /      \
    m1       m2
     \      /
      e    e
       \  /
        m5
        |
        e
        |
        m6

        m7   (neutrino — 1D shaped substrate; see neutrino-1D.md)
```

**Quark wye** (hub m4): `Ma((1, 4), (2, 4), (3, 4))`
- (t, b) on Ma(1, 4) — L_1 = 0.007 fm (smallest ring, heaviest pair)
- (c, s) on Ma(2, 4) — L_2 = 0.91 fm
- (u, d) on Ma(3, 4) — L_3 = 181 fm
- L_4 ≳ 5740 fm (common tube; hub)

**Electron wye** (hub m5): `Ma((1, 5), (2, 5), (5, 6))`
- τ on Ma(1, 5) — uses m1 as ring (SHARED with quark wye where it hosts (t, b))
- μ on Ma(2, 5) — uses m2 as ring (SHARED with quark wye where it hosts (c, s))
- e on Ma(5, 6) — uses new dim m6 as ring; mass set primarily by 1/L_5

**Neutrino sector**: 1D shaped substrate on m7. Per [neutrino-1D.md](neutrino-1D.md), a closed 1D curve with N-fold symmetric shape r(φ) = R[1 + a₁cos(Nφ) + a₂cos(2Nφ)]. The 3 ν mass eigenstates emerge from the curve's band structure; charge = 0 and Majorana symmetry fall out from the dim count (no 2D closure rule to admit a charge label).

**Total dim count: 7** (m1..m7). One fewer than Candidate C's 8.

In the ladder, **the top is not the heaviest** — the structure folds so m1, m2 (at the bottom of each wye sub-graph) are the smallest dims and host the heaviest particles. Energy *falls* down each wye toward the stable center: through the heavy quark legs to the stable proton sheet `Ma(3, 4)`; through τ, μ to the stable electron sheet `Ma(5, 6)`. Heavy particles serve as transient transport states; light particles are the stable destinations.

### 1.1 Relation to candidates.md labels

Wye-ladder labels are LOCAL to this file and differ from the post-relabel convention used in [candidates.md](candidates.md). The mapping:

| candidates.md (post-relabel) | wye-ladder | Role | L (fm) |
|---|---|---|---:|
| m1 | m1 | b/t ring AND τ ring | 0.007 |
| m3 | m2 | c/s ring AND μ ring | 0.91 |
| m4 | m3 | u/d ring | 181 |
| m5 | m4 | quark wye hub | ≳ 5740 |
| — | m5 | e-wye hub | ≈ 2400 (estimated) |
| — | m6 | e dim | free, ~1000s of fm (estimated) |
| — | m7 | ν 1D substrate | ≈ cm-scale (per neutrino-1D.md) |

Wye-ladder does NOT use candidates.md's m2 (the lepton-scale dim ≈ 0.7 fm) — the leptons here reuse the quark rings rather than getting their own dedicated lepton dim. This is the structural difference that yields the dim-count savings.

---

## 2. Why wye-ladder

### 2.1 What sym-ladder taught us

Sym-ladder used a proton-delta `Ma((1,2), (1,3), (2,3))` for the quark sector. Two of its three pairs share a ring dim, forcing a fixed mass-ratio between their lighter modes — the [quark-search.md §4 obstruction](quark-search.md). Numerical tests confirmed: simple 2D modes failed at 137%, compound 3D modes with chained-shear cross-coupling failed at 1784%. The 3-dim delta cannot host 6 quarks under any tested mode-selection scheme without giving up fit quality.

The structural reason: a 3-dim delta has 3 free L's, but 6 observed quark masses span 5 orders of magnitude (m_u = 2 MeV to m_t = 173 GeV). The same L's must simultaneously serve incompatible scale regimes — and they can't.

**The wye's escape** was adding a 4th dim (the hub) whose only job is to be a common tube. The 3 ring L's become independent. The wye fits all 6 quarks at 0.499% with σ_eff in a natural range. This success is preserved in Candidate C and reused here.

### 2.2 The wye-ladder insight

If the wye works for quarks, **use a wye for the electron sector too**. Sym-ladder used a wye for electrons (hub m4 in its labeling) but kept the proton sector as a delta. Wye-ladder is symmetric: both sectors are wyes.

The further insight: the smallest dims (m1, m2) — which are the quark rings hosting the heaviest quarks — *also* serve naturally as rings for the heaviest leptons in the e-wye. The geometric reason: heavy mass ∝ 1/L_R in the pure-ring regime, so heaviest particles want tightest rings. The same tight ring that gives m_t ≈ 173 GeV in the quark wye gives m_τ ≈ 1.8 GeV in the electron wye when paired with a different (larger) e-wye hub. **The same dim plays ring for two different particles in two different sectors.**

This is consistent with [architecture.md §3.4](architecture.md)'s pair-triplet (σ, τ, P) hypothesis — the cross-section shape function P is per-mode, not per-pair-geometry. The dim-pair Ma(1, 4) hosts a clover-shaped mode (quark machinery, σ_eff = 1.976); the dim-pair Ma(1, 5) hosts an ellipse-shaped mode (R53 electron machinery, σ_eff ≈ 1.99). Same m1, different partners, different cross-sections.

### 2.3 Appealing properties

1. **Bypasses the delta problem.** No 3-dim delta anywhere; the proton-delta fit obstruction is moot.

2. **Unified R53 mechanism.** All three charged leptons (e, μ, τ) live on wye pairs with their respective σ_eff near 2 (the R53 magic-shear value). Different from Candidate C, where τ ends up at σ_eff ≈ 1.0 (a different mode center). Wye-ladder gives a *single* mechanism for all charged leptons.

3. **Stability hierarchy is structural.** The ladder folds so heaviest particles are on smallest dims (m1 hosts t and τ); stable particles live at the bottom of each wye (proton/neutron sheet Ma(3, 4); electron sheet Ma(5, 6)). Transient particles (heavy quarks, μ, τ) are on the legs. Energy *falls* from the legs to the stable centers — matches the empirical pattern of heavy fermions weak-decaying to lighter ones.

4. **Strong shared-ring coupling for β-decay.** The same m1, m2 are quark rings AND lepton rings. β-decay (n → p + e + ν̄) requires structural coupling between the quark sector and the electron sector; sharing rings provides this naturally. Stronger than Candidate C, which only shares a single hub-spoke pair (m4, m5) between sectors.

5. **Fewer dims** (7 vs 8 for Candidate C). The 1D neutrino substrate saves dims relative to a ν-delta on 3 fresh dims.

6. **Neutrino charge = 0 and Majorana symmetry fall out structurally.** No fine-tuning needed; the 1D substrate has no 2D closure rule to admit a charge label, and the ψ_n ↔ ψ_−n degeneracy on a periodic 1D dim makes particle-antiparticle equality structural rather than imposed.

---

## 3. Per-sector analytical estimates

### 3.1 Quark wye

Identical to Candidate C's quark sector. See [quark-search.md §9](quark-search.md) for the full derivation. Result: 6 quarks fit at max |Δ%| = 0.499% with σ_eff = 1.976 (t/b), 1.932 (c/s), 1.684 (u/d). Geometry: L_1 = 0.007 fm, L_2 = 0.91 fm, L_3 = 181 fm, L_4 ≳ 5740 fm.

### 3.2 Electron wye — analytical estimate

The e-wye hosts (e, μ, τ) on pairs Ma((1, 6), (3, 6), (6, 7)) (candidates.md labels), inheriting L_1, L_3 from the quark wye and adding two new dims L_6, L_7. Per-pair tube/ring choice is free. **The analytical heuristic** (heaviest lepton on tightest ring; all σ_eff near R53 value 2):

| Pair | Lepton (predicted) | Tube | Ring | σ_eff (predicted) |
|---|---|---|---|---:|
| Ma(1, 6) | τ | m6 (≈ 2400 fm) | m1 (0.007 fm) | ≈ 1.990 |
| Ma(3, 6) | μ | m6 | m3 (0.91 fm) | ≈ 1.917 |
| Ma(6, 7) | e | m6 | m7 (free) | various |

**Predicted appeal:** all three σ_eff near 2 — unified R53 mechanism across the charged-lepton sector.

### 3.3 Electron wye — actual numerical fit (December 2025)

The e-wye fit was run by the now-retired `candidate_fits.py:electron_wye_fit()` routine; re-verification with the general solver [scripts/cand_solver.py](../scripts/cand_solver.py) (via a QY-EY spec) is pending. The recorded result: the fit closes (max |Δ%| = 0.000%) but **the σ_eff values do NOT support the unified-R53 prediction**:

| Pair | Lepton (FOUND) | Tube | Ring | σ_eff (FOUND) |
|---|---|---|---|---:|
| Ma(1, 6) | **μ** (not τ) | m6 | m1 | **1.9994** (extreme R53 fine-tuning, 0.06% off from 2) |
| Ma(3, 6) | **τ** (not μ) | m6 | m3 | **0.6964** (NOT R53; near T(1, 1) center) |
| Ma(6, 7) | e | m7 (large) | m6 | **1.2105** (mid-range, between T(1, 1) and T(1, 2) centers) |

L_6 (e-wye hub) ≈ 1916 fm; L_7 (e-region dim) ≈ 1.077 × 10⁵ fm (~0.1 mm — same scale as the *pre-refactor* C electron dim that we identified as unphysical).

**Three findings that undermine wye-ladder's claimed advantage:**

1. **σ_eff range (0.70 to 1.9994) is *wider* than Candidate C's (1.00 to 1.94)** — wye-ladder is *less* unified, not more.
2. **The 1.9994 fine-tuning on μ is more extreme than anything in Candidate C** — it's the same flavor of R53 over-tuning that motivated us to abandon the pre-refactor C electron placement.
3. **The fit is underdetermined** — 5 free continuous params (L_6, L_7, 3 σ_eff) vs 3 masses leaves a 2-parameter family of solutions; the optimizer returned one of them, not "the" solution. A different starting point could land elsewhere on the manifold.

**The "unified R53 mechanism" prediction in §3.2 was wrong.** The mathematical fit doesn't naturally pick out σ_eff ≈ 2 for all three leptons; the underdetermination gives the optimizer freedom to spread σ_eff across the full (0, 2) range, and it does so. Without an additional constraint (e.g., "all σ_eff must be near 2"), wye-ladder doesn't deliver on the structural unification it promised.

Candidate C is now strictly cleaner on the σ_eff naturalness comparison:

| Property | Candidate C | Wye-ladder |
|---|:---:|:---:|
| σ_eff range across all charged leptons | 1.00 to 1.94 | 0.70 to 1.9994 |
| Most-fine-tuned σ_eff | 1.94 (μ, 3% off from 2) | **1.9994 (μ, 0.06% off from 2)** |
| Fit underdetermination | 4 params for 3 masses (1 DOF) | 5 params for 3 masses (2 DOF) |
| Unified mechanism? | partial — τ at different center | no — σ_eff scattered |

### 3.3 Neutrino sector (1D substrate)

Per [neutrino-1D.md](neutrino-1D.md), the ν substrate is a 1D closed curve with N-fold symmetric shape on dim m7. The three mass eigenstates emerge from the curve's band structure (not from three separate 2D pairs as in Candidate C). Charge = 0 falls out from the dim count; Majorana symmetry falls out from the ψ_n ↔ ψ_−n degeneracy on a 1D periodic dim.

The numerical fit hasn't been done in this file; see [neutrino-1D.md §4](neutrino-1D.md) for the spectrum analysis.

**No shared dims with quark or electron sectors.** Neutrino oscillation phenomenology emerges from the 1D substrate's own band structure rather than from cross-sector couplings.

---

## 4. Comparison with Candidate C

| Property | Candidate C | Wye-ladder |
|---|:---:|:---:|
| Quark sector | wye | wye (identical) |
| Electron sector | delta on (m2, m4, m5) | wye on (m1, m5), (m2, m5), (m5, m6) |
| ν sector | delta on (m6, m7, m8) | 1D substrate on m7 |
| Total dims | 8 | 7 |
| Quark fit | 0.499% | 0.499% (identical) |
| Electron fit | 0.000% (verified) | not yet verified — needs script |
| Electron σ_eff range | 1.00 (τ), 1.93 (e), 1.94 (μ) | ≈ 1.99 (τ), ≈ 1.92 (μ), ≈ 2.00 (e) |
| Electron σ_eff unified? | no — τ at σ_eff=1 center, others at σ_eff=2 center | **yes** — all three near σ_eff=2 (unified R53) |
| Shared dims (quark ↔ e) | one pair: (m4, m5) | **two rings: m1 and m2** |
| Stability hierarchy | implicit (per-pair σ_eff) | **structural** (ladder folds toward stable centers) |
| ν mass mechanism | three 2D pairs with σ_eff per pair | single 1D substrate, band structure |
| ν charge=0 and Majorana | inherited assumption | falls out from dim count |

**Where wye-ladder wins:**
- Fewer dims (7 vs 8)
- Unified R53 mechanism across all charged leptons
- Stronger geometric coupling for β-decay (two shared rings vs one shared pair)
- Structural stability hierarchy (matches observed pattern)
- Neutrino charge = 0 and Majorana fall out structurally

**Where Candidate C wins (today):**
- All sectors numerically verified to machine precision
- No mild detuning needed (C's τ σ_eff = 1.0 exactly; wye-ladder's τ at 1.99 is 1% off resonance)
- ν fit doesn't depend on the unfamiliar 1D substrate machinery (still being developed)

**Where they're tied:**
- Quark fit (same wye topology)
- Geometric and architectural cleanliness of the quark sector

**Net:** wye-ladder is genuinely competitive *if* the e-wye numerical fit closes cleanly and the 1D ν substrate fit closes cleanly. The structural advantages (unified mechanism, fewer dims, stronger sharing, structural stability) outweigh the τ's mild R53 detuning.

---

## 5. Open questions and concerns

1. **Numerical verification of the e-wye fit.** All §3.2 numbers are analytical estimates. Write a QY-EY spec for the general solver [scripts/cand_solver.py](../scripts/cand_solver.py) and run it against (m_e, m_μ, m_τ). Expected to close cleanly; need to confirm σ_eff values are within R53's natural range.

2. **L_5 vs L_6 — what fixes L_6?** The e-mass pins L_5 ≈ 2426 fm; L_6 is loosely constrained. Is there a structural rule (e.g., L_5 / L_6 ratio matches an empirical value, or L_6 plays a role in a not-yet-identified mode) that fixes L_6? Without one, L_6 is an unmotivated free parameter — a regression from Candidate C's L_2 = 0.7 fm being pinned cleanly by the τ mass alone.

3. **Why no observed Ma(1, 2) particle?** Both m1 and m2 are quark + lepton dims, but there's no proposed mode on the Ma(1, 2) pair itself. The cross-term σ_{1,2} between them could host a mode — what is it, and where is it observed? The user noted: "we might even find an Ma(1, 2) sheet (Higgs or something?) hidden in there." Worth investigating; could be predictive content.

4. **Forbidding extra modes.** With m1, m2 each hosting multiple particle types via different cross-sections, the closure-mode inventory per pair includes BOTH the quark mode (clover) and the lepton mode (ellipse). Are these two modes simultaneously present? If yes, what observed particles correspond to the "off-sector" modes (e.g., the electron mode on Ma(1, 4) — the quark sheet)? If no, why are they forbidden? Need a structural rule.

5. **Compound modes on shared dims.** If m1, m2 simultaneously serve quark and lepton sheets, can compound 3D modes (analogous to sym-ladder Test B) form between them? If yes, what particles do they correspond to? If no, why are they forbidden?

6. **1D neutrino substrate validation.** [neutrino-1D.md §4](neutrino-1D.md) develops the band-structure approach but the numerical fit against observed (m_ν₁, m_ν₂, m_ν₃) hasn't been done. Need a script that solves the 1D Schrödinger problem on the shaped curve and matches the three lowest eigenvalues.

7. **Does the ladder bridge the ν sector?** The diagram shows m7 disconnected from the rest of the ladder. Per the user: "Perhaps all dimensions are connected to one another in the sense that they are in the same domain and energy can find an optimal home in any available dimension." Is there a structural sense in which m7 belongs in the ladder (e.g., as an "additional rung at the bottom"), or is it genuinely isolated? Affects β-decay reasoning involving ν.

---

## 6. Development plan

If wye-ladder is to compete with Candidate C as the working topology, the following steps make it concrete:

1. **Numerical e-wye fit.** Write a QY-EY spec for [scripts/cand_solver.py](../scripts/cand_solver.py) (the e-wye is Ma((1, 5), (2, 5), (5, 6))) and run it. Report σ_eff values and verify they sit in R53's natural range. Goal: max |Δ%| < 1%.

2. **1D neutrino fit.** Add a script that solves the Schrödinger problem on the shaped 1D curve from [neutrino-1D.md §2](neutrino-1D.md) and fits the three lowest band gaps to the observed ν mass hierarchy. Use the tube-function family parameters (N, a₁, a₂) plus L as free parameters.

3. **Predict orphan modes.** For each shared pair (m1, *) and (m2, *), enumerate the additional 2D modes that should exist beyond the quark and lepton modes already assigned. Compare predicted masses to observed particles (Higgs, W, Z, mesons, etc.) — does anything match? If yes, the architecture has predictive content; if not, identify what would forbid those modes.

4. **β-decay coupling analysis.** Work out the cross-section coupling between the quark Ma(1, 4) (b/t pair) and the electron Ma(1, 5) (τ pair) via the shared m1. Does it predict the right rate for τ-related processes? Similarly for m2 (c/s ↔ μ).

5. **Compare against Candidate C in [candidates.md](candidates.md).** Once the e-wye and 1D ν fits are verified, update the candidate comparison table. If wye-ladder closes everywhere with comparable or better accuracy, it's a serious challenger to Candidate C and a switch is warranted. If it requires deeper fine-tuning or fails any sector, Candidate C remains the working choice.

6. **Decide which to promote to derivation.** Per [STATUS.md Phase 5](STATUS.md), the working topology will eventually be promoted from `work/` to `ma-domain/` proper for a mathematical derivation. Pick wye-ladder OR Candidate C based on the §4 comparison plus the Phase 4 coherence checks (cross-term sparsity, σ vs τ pinning, etc.).

---

## 7. Net assessment (updated after e-wye fit)

Wye-ladder PROMISED two main advantages over Candidate C:
1. **Unified R53 mechanism** across all charged leptons (single σ_eff regime ≈ 2)
2. **Fewer dims** (7 vs 8) via 1D neutrino substrate

The e-wye numerical fit (§3.3) **falsifies advantage #1**. The σ_eff values come out as (1.9994, 0.70, 1.21) — wider range than Candidate C's (1.94, 1.00, 1.93), with one value (1.9994 for μ) more fine-tuned than anything in C. The "unified mechanism" prediction was an analytical heuristic that the actual fit doesn't deliver — the fit is underdetermined (5 params for 3 masses) and the optimizer's preferred solution spreads σ_eff broadly.

Advantage #2 (fewer dims) is still potentially real, but it depends on the 1D neutrino substrate working — and developing/testing that machinery is a substantial new investment.

The remaining structural appeals (shared-ring β-decay coupling, structural stability hierarchy) are interpretively interesting but don't constitute fit-quality wins.

**Current status: tested and not preferred.** Candidate C remains the working topology. Wye-ladder is documented as a tested-and-deprioritized alternative.

**Conditions under which wye-ladder should be re-pursued:**
- An additional constraint emerges that picks out a more natural σ_eff solution from the e-wye solution manifold (e.g., "all σ_eff must lie in [1, 2]") and produces a unified R53 fit
- A different e-wye topology (different shared dims, or compound modes) gives σ_eff values cleaner than Candidate C's
- Candidate C runs into a structural obstruction in Phase 4 (cross-term sparsity, σ vs τ pinning) that wye-ladder's geometry avoids
- The 1D neutrino substrate proves so structurally compelling (charge=0 + Majorana falling out from dim count) that it's worth developing for its own sake — in which case wye-ladder could be revived as the natural quark+e+ν host

Until one of these holds, wye-ladder development is paused.
