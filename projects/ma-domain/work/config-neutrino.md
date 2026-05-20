# config-neutrino.md — neutrino-sector topology configurations

**Purpose:** catalog the topology configurations available for producing 3 neutrino mass eigenstates at the observed meV scale, with oscillation behavior modelled by the structure of the substrate the modes live on.

**Neutrino sector requirements:** host 3 mass eigenstates (m_ν₁ ≈ 30 meV, m_ν₂ ≈ 33 meV, m_ν₃ ≈ 60 meV — span ~2×) with **no EM charge** (Q = 0) and **Majorana-like equivalence** of particle and antiparticle (or, at minimum, an architecture that doesn't *forbid* Majorana behavior). The meV scale requires a macroscopic substrate (min L ≳ 4 cm) — far larger than the fm-to-mm dim sizes that suffice for quark and electron sectors.

**Labelling convention (local to this file):** dims are named `m_a`, `m_b`, … abstractly. The configs say nothing about which globally-labelled dims they map onto — that is a candidate-level choice ([candidates.md](candidates.md)).

**Scope note:** numbers reported here come from sector-internal fits on *fresh dims only* — no cross-sector inheritance. Where a config is under-determined within its sector, the description gives DOF analysis rather than a single point on the solution manifold.

---

## NS — Neutrino Sheet (2D pair)

Single pair topology `Ma(a, b)` — one 2D sheet hosting all three ν mass eigenstates via multiple closure modes on the one pair.

```mermaid
%%{init: { "flowchart": { "nodeSpacing": 25, "rankSpacing": 40, "curve": "basis" }, "themeVariables": { "fontSize": "12px" } } }%%
graph LR
    ma[m_a]
    mb[m_b]

    %% --- neutrino sector (green, 2D torus pair) ---
    ma ==>|ν| mb
    linkStyle 0 stroke:green
```

### NS.1 — Topology and DOF

| Element | Count |
|---|---:|
| Dims | 2 (m_a, m_b) |
| Pairs | 1 |
| Closure modes hosted | 3 (one per ν mass eigenstate) |
| Continuous params | 3 (L_a, L_b, σ_eff) |
| Mass constraints | 3 |
| Sector-internal DOF | 0 (just-determined) |

### NS.2 — How three mass eigenstates emerge

A single 2D pair under the strict closure-mode rule ([architecture.md §3.3.1](architecture.md)) has only **two** modes at m_t = 1: T(1, 1) and T(1, 2). Three ν mass eigenstates require either:

- **Sign-flipped m_t modes.** Per [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md), the closure rule `m_t | m_r` with both nonzero admits T(1, n) for n ∈ ℤ \ {0} — *including negative m_t*. The trio T(1, 1), T(−1, 1), T(1, 2) (or similar) gives three distinct closure-satisfying modes with three distinct detunings δ = m_r − σ_eff·m_t when σ_eff ≠ 0. This is the mechanism used by model-F's R49 ν-sheet.
- **Shear-resonance trio (R49-style).** With σ_eff tuned to a specific near-integer value, the three nearby modes (T(1, 1), T(1, 2), T(2, 3) or similar) give three close-but-distinct masses. Structurally the same as the shear-resonance mechanism R53 uses for charged leptons, applied at much smaller σ_eff and much larger L.

Both mechanisms live on a single 2D pair — no extra dims required. Oscillation phenomenology is modelled by the relationships between the three modes and their detunings, in spirit consistent with the existing R49 / model-F treatment.

### NS.3 — Geometric requirements

For meV-scale masses, the mass formula m ≈ 2πℏc·max(1/L_T, δ/L_R) requires at least one of L_a, L_b to be macroscopic:

- **Fat-torus, δ ≈ 0.1:** L_R ≈ 2πℏc·δ/m ≈ 4 × 10⁹ fm ≈ **4 mm**
- **Fat-torus, δ ≈ 0.001 (near-resonance):** L_R ≈ **40 μm**
- **Thin-torus:** L_T ≈ **4 cm**

Both L_a, L_b are free parameters of NS; at least one must satisfy the macroscopic floor. The other can be anywhere from sub-fm to macroscopic depending on the mode mechanism (sign-flipped vs near-resonance).

### NS.4 — Fit status (sector-internal)

**Sign-flipped m_t modes, spot-checked on fresh dims.** A least-squares spot-check with sign-flipped modes admitted and L varied across cm-dm scales:

| L_a (fm) | Best max \|Δ%\| | L_b (fm) | Mode trio |
|---:|---:|---:|---|
| 1 × 10¹⁰ | 167% | 1 × 10¹⁵ | T(±1, n) — wrong assignment |
| 4 × 10¹⁰ (4 cm) | **1.05%** | 2.3 × 10¹¹ | T(−1, 1), T(1, 1), T(−1, 2) |
| 1 × 10¹¹ (10 cm) | **0.74%** | 4.3 × 10¹⁰ | T(−1, 1), T(1, 1), T(1, 2) |

NS is viable to roughly ~1% with sign-flipped modes on a fresh single pair at the cm scale. A canonical least-squares script for NS with closure-mode admittance has not been formalized yet; the spot-check is preliminary.

### NS.5 — Verdict

**Working approximately at ~1%** with sign-flipped modes; precision is limited by the spot-check not having been refined. Architecturally simple (1 pair, 2 dims). The Q = 0 result is consistent but not *automatic* — it relies on the σ_eff = 0 reading of the closure rule (uncharged when modes are sign-symmetric pairs). Majorana-like equivalence emerges from the pairing of T(1, n) and T(−1, n) modes, not from a structural feature.

---

## NC — Neutrino Curve (1D shaped substrate)

Single 1D closed curve on dim `m_a` — no pair, no 2D structure. The closed curve has an N-fold symmetric shape `r(φ) = R[1 + a₁·cos(Nφ) + a₂·cos(2Nφ)]` and hosts three modes from its **band structure**.

```mermaid
%%{init: { "flowchart": { "nodeSpacing": 25, "rankSpacing": 40, "curve": "basis" }, "themeVariables": { "fontSize": "12px" } } }%%
graph LR
    e1[" ⋯ "]
    e2[" ⋯ "]
    e3[" ⋯ "]
    ma[m_a]

    %% --- neutrino sector (green, dotted = non-pair coupling to other sectors) ---
    e1 -.-|ν| ma
    e2 -.-|ν| ma
    e3 -.-|ν| ma
    linkStyle 0,1,2 stroke:green,stroke-dasharray:5 3

    style e1 fill:transparent,stroke:#888,stroke-dasharray:3 3
    style e2 fill:transparent,stroke:#888,stroke-dasharray:3 3
    style e3 fill:transparent,stroke:#888,stroke-dasharray:3 3
```

The ellipsis nodes represent *some other dims* outside this sector. The dotted edges represent *non-pair couplings* — m_a is a standalone 1D substrate, so its relation to other sectors is not via 2D sheets but via whatever cross-sector coupling the framework supports (TBD; one of the open structural questions in [neutrino-1D.md](neutrino-1D.md)).

### NC.1 — Topology and DOF

| Element | Count |
|---|---:|
| Dims | 1 (m_a, standalone) |
| Pairs | 0 |
| Continuous params | 1 L + shape (a₁, a₂, N) (≈ 3–4) |
| Mass constraints | 3 |
| Sector-internal DOF | 0–1 |

### NC.2 — How three mass eigenstates emerge

The closed 1D curve has natural modes labelled by a single integer winding n (the analogue of m_t / m_r on a 2D pair). On a *featureless* circle the spectrum is m_n ∝ |n|/L — equally spaced. On a *shaped* curve with N-fold symmetry, the spectrum has **band structure**: modes group into bands separated by gaps determined by the shape parameters (a₁, a₂, N).

The lowest three bands give three masses with the observed hierarchy m_ν₁ ≈ m_ν₂ < m_ν₃, and the mixing structure (PMNS-like) emerges from the shape symmetry. Full development in [neutrino-1D.md](neutrino-1D.md).

Two physical pictures of the substrate:

- **Embedding picture:** the curve is a closed loop in a 2D embedding plane. Modes obey the Jensen-Koppe / da Costa effective Hamiltonian with a geometric potential V_geom(s) = −(ℏ²/8m)·κ(s)² where κ is the curvature.
- **Intrinsic picture:** the curve is an abstract 1D manifold with a non-uniform metric ds = g(φ)dφ. Modes are eigenfunctions of the Laplacian Δψ = (1/g)·d/dφ((1/g)·dψ/dφ) on this manifold.

### NC.3 — Q = 0 and Majorana fall out structurally

**Q = 0 falls out from the dim count.** EM charge in the metric-charge framework is a topological label of a *two*-dimensional Bloch state (the boundary winding k_θ = m_r − τ·m_t, plus the cross-section's per-region turning ledger). A 1D periodic dim has only one winding number and no closure rule in the metric-charge sense — so there is no slot for an EM-charge label to occupy. Uncharged-ness is *structural*, not engineered with σ and τ.

**Majorana equivalence falls out from the substrate.** On a 1D circle, modes ψ_n ∝ exp(2πi·n·s/L) and ψ_(−n) are degenerate (mass ∝ |n|), and any real combination ψ_n + ψ_(−n)* is its own complex conjugate. The ψ ↔ ψ̄ distinction has no geometric content at the level of the substrate; particle and antiparticle equivalence is structural rather than imposed.

### NC.4 — Geometric requirements

The substrate's circumference L_a must satisfy L_a ≳ 4 cm (~4 × 10¹⁰ fm) for the lowest mode to be at the meV scale. The shape parameters (a₁, a₂, N) control band gaps and thus the splittings ν₁–ν₂ and ν₂–ν₃.

### NC.5 — Fit status

Script: [scripts/neutrino_1d_fit.py](../scripts/neutrino_1d_fit.py); output: [outputs/neutrino_1d_fit.txt](../outputs/neutrino_1d_fit.txt). The script solves the intrinsic Laplace-Beltrami operator on the closed shaped curve.

**The wall (no flux): ~6%.** With a plain C_N-symmetric curve r(φ) = R[1 + a₁cos Nφ + a₂cos 2Nφ], the lowest three nonzero modes lock to a **1 : 1 : 2** pattern — an n = ±1 degenerate doublet plus the n = −2 mode at twice the mass. Best max |Δ%| ≈ 6%; the optimizer cannot produce the ~10% m₁–m₂ doublet split the observed hierarchy needs.

**Why the wall exists — the doublet is symmetry-protected.** The n = ±1 doublet is degenerate because the curve's C_N symmetry plus time-reversal protect it. *No* C_N-symmetric shape perturbation — any choice of (a₁, a₂, N), including the harmonic-curve split knobs of [tube-function.md](tube-function.md) — can lift it. Diagnostic: a pronounced limaçon r = R(1 + 0.5cos φ) splits the doublet by only ~10⁻⁵ relative, because a 1-fold shape harmonic is mostly a rigid *displacement*, invisible to an operator that senses only the arc-length metric. The wall is the symmetry, not the shape.

**The fix — a Wilson-loop flux: ~1.5%.** A flux Φ threaded through the closed loop enters the operator as a covariant derivative D_s = ∂_s + iA_s, shifting mode n to (n + f) with f = Φ/2π. The lowest three nonzero modes become (1−f) : (1+f) : (2−f) — the doublet splits **linearly in f**, a first-order effect a shape harmonic cannot supply. Physical origin: per [grid-primitive ch.9](../../grid-primitive/09-chirality-asymmetry.md), a small substrate antisymmetric chirality χ_anti is equivalent to a built-in background gauge field that, on any compact wrap, contributes a gauge-invariant Wilson-loop phase. The closed neutrino loop is exactly such a wrap.

Fitting (R, a₁, a₂, f) to the (30, 33, 60) meV targets, N = 3:

| Quantity | Value |
|---|---|
| Best max \|Δ%\| | **1.47%** |
| flux fraction f = Φ/2π | 0.051 |
| R | 2.8 × 10⁹ fm ≈ 0.28 cm |
| ν masses (predicted) | 29.68, 32.87, 60.88 meV |

The result is N-independent (N = 2, 3, 4 all reach ≈1.47%), confirming the flux — not the lobe count — does the work. The fitted f ≈ 0.051 is close to the f ≈ 0.048 that the (1−f):(1+f):(2−f) scaling predicts analytically for a 1 : 1.1 hierarchy.

**The residual ~1.5% sits on m₃.** Circle + flux gives m₃/m₁ = (2−f)/(1−f) ≈ 2.05 against the target 2.00; the C_N shape harmonics have weak leverage on the low-mode ratios and pull it only partway. The residual is comparable to the precision of the (30, 33, 60) meV targets themselves, which are *project working values*, not sharp data.

**Predicted light state.** With f ≠ 0 the n = 0 mode is no longer massless; it acquires m₀ ∝ f ≈ 1.6 meV. The fit assigns the three observed neutrinos to n = −1, +1, −2 and skips n = 0. Whether this light n = 0 state is a physical fourth light neutrino or a substrate zero-mode without particle interpretation is an open question.

### NC.6 — Verdict

**NC is a working config: ~1.5% with the Wilson-loop flux.** Q = 0 and Majorana-like structure fall out of the 1D dim count (§NC.3); the doublet split — the structural failure that produced the 6% wall — is resolved by a flux that is *not a free parameter* but the loop-integral of the substrate's antisymmetric chirality χ_anti ([grid-primitive ch.9](../../grid-primitive/09-chirality-asymmetry.md)). The same χ_anti is independently expected to source δ_CP and the matter/antimatter axis, so one substrate constant links the doublet split, θ₁₃, and CP violation — the linkage [neutrino-1D.md §4.3](neutrino-1D.md) anticipated.

The flux is candidate 3 ("small chirality / shear") of [neutrino-1D.md §4.3](neutrino-1D.md), now realized and tested. It is mechanically distinct from — and stronger than — the δ shape-harmonic (candidate 1) the earlier fit used: a flux splits the doublet at first order, a shape harmonic only at second order. It also supersedes the rescue paths an earlier draft of this section listed (embedding-κ² potential, exotic topology, tiny extra dims): the flux is a cleaner mechanism and keeps the substrate purely 1D.

**On Majorana.** A flux breaks time-reversal — which is exactly what splits ψ₊ₙ from ψ₋ₙ — so exact structural Majorana (§NC.3) is traded for a slightly-broken version. This is consistent with the framework's own expectation of δ_CP ≠ 0, and with the empirical fact that exact Majorana-ness of neutrinos is not established. The load-bearing structural result, **Q = 0, is untouched**: it follows from the 1D dim count, which the flux does not change.

**Open refinements.** The residual ~1.5% on m₃ and the interpretation of the predicted light n = 0 state remain. Neither is a structural obstruction; both are downstream work.

---

## ND — Neutrino Delta (de-emphasized)

3-dim triangle topology `Ma((a, b), (a, c), (b, c))`. Each pair hosts one ν mass eigenstate at T(1, 2). Each dim participates in two of the three pairs.

```mermaid
%%{init: { "flowchart": { "nodeSpacing": 25, "rankSpacing": 40, "curve": "basis" }, "themeVariables": { "fontSize": "12px" } } }%%
graph LR
    ma[m_a]
    mb[m_b]
    mc[m_c]

    %% --- neutrino sector (green) ---
    ma ===|ν| mb
    ma ===|ν| mc
    mb ===|ν| mc
    linkStyle 0,1,2 stroke:green
```

**Status: documented for completeness; currently de-emphasized.** Active candidates that previously used ND are being reconsidered in favor of NS or NC. This config is retained as a fallback and to provide a structural decomposition for the existing candidate-level fits that adopt the three-pair pattern.

### ND.1 — Topology and DOF

| Element | Count |
|---|---:|
| Dims | 3 (m_a, m_b, m_c) |
| Pairs | 3 |
| Continuous params | 6 (3 L's + 3 σ_eff) |
| Mass constraints | 3 |
| Sector-internal DOF | 3 (underdetermined within sector) |

Same topological structure as ED in the electron sector, but at the macroscopic L scale required for meV masses.

### ND.2 — Sector-internal anchors

- **Macroscopic L scale.** The lightest neutrino mass m_ν₁ ≈ 30 meV requires the corresponding ring to satisfy L ≈ 2πℏc·δ/m_ν₁. With δ ≈ 0.05 this gives L ≈ 4 × 10⁹ fm ≈ 4 mm; with δ ≈ 1 this gives L ≈ 4 cm or larger. Either way, all three dims are macroscopic.
- **No structural Q = 0 mechanism.** Unlike NC, ND is a multi-pair 2D-sheet topology. Q = 0 has to be argued pair-by-pair (each pair's σ_eff or boundary identification must yield k_θ = 0 on the relevant mode). Not automatic.
- **No structural Majorana mechanism.** Particle-antiparticle equivalence on a 2D-pair sheet is the same Dirac/Majorana ambiguity as in any 2D sheet — not a structural feature.

### ND.3 — Fit status (sector-internal, fresh dims)

Numerically, ND closes to machine precision on the 3-DOF underdetermined manifold using three fresh dims at the macroscopic scale. A representative point: with m_a ≈ 7 cm, m_b ≈ 2 cm, m_c ≈ 4 cm, the three (T(1, 2)) modes match the observed (30, 33, 60) meV trio at < 0.01% per mass. The specific (L, σ_eff) values depend on which point of the manifold the optimizer selects.

### ND.4 — Verdict

**Working numerically but de-emphasized.** The 0.01% fit is trivial under the existing underdetermination. The structural appeal (free Q = 0, free Majorana) of NC and the parsimony (one pair) of NS both look stronger than ND's "three-fresh-dims" approach. ND is documented for completeness and to enable structural decomposition of legacy candidate topologies, but is not the preferred direction for new development.

---

## NY — Neutrino Wye (placeholder)

4-dim star topology `Ma((a, h), (b, h), (c, h))`, mirror of QY/EY structure for the ν sector. Three rings, one shared hub. Each pair hosts one ν mass eigenstate at T(1, 2).

**Status: placeholder; not pursued.** No current candidate uses NY. Documented here for symmetry with the other sectors. If a downstream argument forces a multi-pair ν topology with the wye specifically (rather than the delta), NY can be filled out with the same DOF / fit-status treatment as ND.

---

## Comparison

| Feature | NS | NC | ND | NY |
|---|:---:|:---:|:---:|:---:|
| Dims used | 2 | 1 | 3 | 4 |
| Substrate | 2D pair (torus) | 1D shaped closed curve | 3 × 2D pair (delta) | 4 × 2D pair (wye) |
| Mass-eigenstate mechanism | 3 closure modes on one pair | 3 lowest bands of shaped curve | 1 mode per pair (T(1, 2)) | 1 mode per pair (T(1, 2)) |
| Continuous parameters | 3 | ~4 | 6 | 7 |
| Sector-internal DOF | 0 | 0–1 | 3 | 4 |
| Best fit (sector-internal) | ~1% (spot-check) | **1.5%** (Wilson-loop flux) | < 0.01% (trivially, given DOF) | not run |
| Q = 0 | from σ_eff = 0 / mode pairing | **structural** (no 2D closure rule) | per-pair, not automatic | per-pair, not automatic |
| Majorana | from sign-flipped mode pairs | structural, mildly broken by the flux | not automatic | not automatic |
| Macroscopic dim required | yes, ≳ 4 cm | yes, ≳ 4 cm | yes, all three | yes, all four |
| Status | preferred | working | de-emphasized | placeholder |

NS and NC are the two preferred directions: NS for empirical accessibility (sign-flipped modes fit at ~1% today), NC for structural elegance (Q = 0 falls out of the dim count for free, and the doublet split — once the config's blocker — is now resolved by a Wilson-loop flux at ~1.5%). ND is documented for completeness and for decomposing legacy candidates; NY is a placeholder.

---

## Cross-references

- [candidates.md](candidates.md) — active combinations; maps these abstract labels to global dim indices
- [architecture.md §3.3.1](architecture.md) — closure-mode inventory per pair (T(1, n) for n ∈ ℤ \ {0})
- [metric-charge ch. 4](../../metric-charge/04-the-closure-condition.md) — full closure rule including sign-flipped m_t
- [neutrino-1D.md](neutrino-1D.md) — full development of the NC substrate, band-structure math, and Majorana derivation
- [grid-primitive ch.9](../../grid-primitive/09-chirality-asymmetry.md) — substrate antisymmetric chirality χ_anti; the physical origin of the Wilson-loop flux used in §NC.5
- [scripts/cand_solver.py](../scripts/cand_solver.py) — general candidate solver; fits one-particle-per-sheet configs (ND, NY). The multi-mode-per-pair NS and the 1D-substrate NC are not yet supported by it.
- [scripts/neutrino_1d_fit.py](../scripts/neutrino_1d_fit.py) — NC intrinsic-operator + Wilson-loop-flux fit script
- [config-quark.md](config-quark.md), [config-electron.md](config-electron.md) — sibling sector configs
