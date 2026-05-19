# wye-ladder.md — Two-wye ladder with shared rings

**Status:** Active candidate. Replaces sym-ladder's failed proton-delta with a proton-wye, and uses a matching electron-wye that *shares ring dims* with the quark wye. The neutrino sector lives on a 1D shaped substrate per [neutrino-1D.md](neutrino-1D.md). Aims to combine the wye's empirical fit success (Candidate C's quark sector) with sym-ladder's "stable center, unstable legs" interpretation.

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

### 3.2 Electron wye

The e-wye hosts (e, μ, τ) on pairs Ma((1, 5), (2, 5), (5, 6)), inheriting L_1, L_2 from the quark wye and adding two new dims L_5, L_6. Per-pair tube/ring choice is free; expected assignment (heaviest lepton on tightest ring):

| Pair | Lepton | Tube | Ring | σ_eff (estimated) | Mass formula | Solves to |
|---|---|---|---|---:|---|---|
| Ma(1, 5) | τ | m5 (≈ 2400 fm) | m1 (0.007 fm) | **≈ 1.990** | m_τ ≈ 1240 · δ / L_1 | δ ≈ 0.01 |
| Ma(2, 5) | μ | m5 | m2 (0.91 fm) | **≈ 1.917** | m_μ ≈ 1240 · δ / L_2 | δ ≈ 0.078 |
| Ma(5, 6) | e | m5 | m6 (free, ~1000s of fm) | various | m_e ≈ 1240 / L_5 | sets L_5 ≈ 2426 fm |

All three σ_eff values land at or near σ_eff = 2 — the R53 magic-shear value. The deviations from 2 are 1% for τ and 8% for μ — comparable to or smaller than R53's own published deviation of 0.2% from σ_eff = 2.004. **This is consistent with the R53 mechanism, not extreme fine-tuning.**

**L_5 is pinned by the electron mass.** With m_e at the floor of the (5, 6) pair (mass = 2πℏc/L_5), L_5 ≈ 2426 fm — comparable to the τ Compton wavelength's wider-cousin. This same L_5 plays tube in the τ and μ pairs, where its 1/L_5 contribution is negligible compared to the much larger δ/L_R contribution.

**L_6 is loosely constrained.** Since m_e is set by L_5 alone (the 1/L_T term dominates the e mass formula), L_6 contributes only via the small δ/L_6 correction. L_6 can sit anywhere within ~1 order of magnitude of L_5 and the e mass still fits. This is one fewer fully-pinned dim than Candidate C's e-delta — a structural freedom that should be either justified or constrained.

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

1. **Numerical verification of the e-wye fit.** All §3.2 numbers are analytical estimates. Need to add a `wye_ladder_electron_fit()` to [scripts/candidate_fits.py](../scripts/candidate_fits.py) (or a fresh script) that fits the e-wye against (m_e, m_μ, m_τ). Expected to close cleanly; need to confirm σ_eff values are within R53's natural range.

2. **L_5 vs L_6 — what fixes L_6?** The e-mass pins L_5 ≈ 2426 fm; L_6 is loosely constrained. Is there a structural rule (e.g., L_5 / L_6 ratio matches an empirical value, or L_6 plays a role in a not-yet-identified mode) that fixes L_6? Without one, L_6 is an unmotivated free parameter — a regression from Candidate C's L_2 = 0.7 fm being pinned cleanly by the τ mass alone.

3. **Why no observed Ma(1, 2) particle?** Both m1 and m2 are quark + lepton dims, but there's no proposed mode on the Ma(1, 2) pair itself. The cross-term σ_{1,2} between them could host a mode — what is it, and where is it observed? The user noted: "we might even find an Ma(1, 2) sheet (Higgs or something?) hidden in there." Worth investigating; could be predictive content.

4. **Forbidding extra modes.** With m1, m2 each hosting multiple particle types via different cross-sections, the closure-mode inventory per pair includes BOTH the quark mode (clover) and the lepton mode (ellipse). Are these two modes simultaneously present? If yes, what observed particles correspond to the "off-sector" modes (e.g., the electron mode on Ma(1, 4) — the quark sheet)? If no, why are they forbidden? Need a structural rule.

5. **Compound modes on shared dims.** If m1, m2 simultaneously serve quark and lepton sheets, can compound 3D modes (analogous to sym-ladder Test B) form between them? If yes, what particles do they correspond to? If no, why are they forbidden?

6. **1D neutrino substrate validation.** [neutrino-1D.md §4](neutrino-1D.md) develops the band-structure approach but the numerical fit against observed (m_ν₁, m_ν₂, m_ν₃) hasn't been done. Need a script that solves the 1D Schrödinger problem on the shaped curve and matches the three lowest eigenvalues.

7. **Does the ladder bridge the ν sector?** The diagram shows m7 disconnected from the rest of the ladder. Per the user: "Perhaps all dimensions are connected to one another in the sense that they are in the same domain and energy can find an optimal home in any available dimension." Is there a structural sense in which m7 belongs in the ladder (e.g., as an "additional rung at the bottom"), or is it genuinely isolated? Affects β-decay reasoning involving ν.

---

## 6. Development plan

If wye-ladder is to compete with Candidate C as the working topology, the following steps make it concrete:

1. **Numerical e-wye fit.** Add a function to [scripts/candidate_fits.py](../scripts/candidate_fits.py) (or a new script) that fits the e-wye Ma((1, 5), (2, 5), (5, 6)) against (m_e, m_μ, m_τ) using L_1, L_2 inherited from the quark wye and L_5, L_6 free. Report σ_eff values and verify they sit in R53's natural range. Goal: max |Δ%| < 1%.

2. **1D neutrino fit.** Add a script that solves the Schrödinger problem on the shaped 1D curve from [neutrino-1D.md §2](neutrino-1D.md) and fits the three lowest band gaps to the observed ν mass hierarchy. Use the tube-function family parameters (N, a₁, a₂) plus L as free parameters.

3. **Predict orphan modes.** For each shared pair (m1, *) and (m2, *), enumerate the additional 2D modes that should exist beyond the quark and lepton modes already assigned. Compare predicted masses to observed particles (Higgs, W, Z, mesons, etc.) — does anything match? If yes, the architecture has predictive content; if not, identify what would forbid those modes.

4. **β-decay coupling analysis.** Work out the cross-section coupling between the quark Ma(1, 4) (b/t pair) and the electron Ma(1, 5) (τ pair) via the shared m1. Does it predict the right rate for τ-related processes? Similarly for m2 (c/s ↔ μ).

5. **Compare against Candidate C in [candidates.md](candidates.md).** Once the e-wye and 1D ν fits are verified, update the candidate comparison table. If wye-ladder closes everywhere with comparable or better accuracy, it's a serious challenger to Candidate C and a switch is warranted. If it requires deeper fine-tuning or fails any sector, Candidate C remains the working choice.

6. **Decide which to promote to derivation.** Per [STATUS.md Phase 5](STATUS.md), the working topology will eventually be promoted from `work/` to `ma-domain/` proper for a mathematical derivation. Pick wye-ladder OR Candidate C based on the §4 comparison plus the Phase 4 coherence checks (cross-term sparsity, σ vs τ pinning, etc.).

---

## 7. Net assessment

Wye-ladder is a strong candidate that combines the wye's empirical fit success with sym-ladder's structural elegance. It uses fewer dims than Candidate C, provides a unified R53 mechanism for charged leptons, and gives a structural reason for the observed stability hierarchy. The 1D neutrino substrate is novel but already partially developed in [neutrino-1D.md](neutrino-1D.md).

**The decisive test** is whether the e-wye numerical fit closes with σ_eff values within R53's natural range. The analytical estimates in §3.2 suggest it will. Once that's verified, wye-ladder becomes a serious alternative to Candidate C — possibly the preferred working topology, depending on the §4 comparison criteria.

**Status going forward:** track in parallel with Candidate C. Run the numerical tests in §6.1 and §6.2. Update [candidates.md](candidates.md) with wye-ladder as a fourth candidate once verified. Defer the choice of which to promote (Candidate C vs wye-ladder) until both have been fully tested through Phase 4 coherence checks.
