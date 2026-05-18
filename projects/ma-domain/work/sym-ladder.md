# sym-ladder.md — A symmetric-ladder topology candidate

**Status:** Working hypothesis. Proposes a 7-dim layout in which each fermion sector has a "stable center, unstable legs" structure linked by shared dims into a vertical ladder. Compared to Candidate C ([candidates.md](candidates.md)), the proton and electron sectors swap topology types (proton becomes a delta, electron becomes a wye); the neutrino sector is the same delta as in C.

The proton-delta sub-problem (whether the delta can fit 6 quark masses comparably to the wye) is the load-bearing question. It is analyzed in §3.

---

## 1. Structure

```
         m1
        /  \
       p    p
      /      \
    m2 --p-- m3        (proton delta)
     \      /
      e    e
       \  /
        m4
        |
        e
        |
        m5             (electron wye)
       /  \
      v    v
     /      \
    m6 --v-- m7        (neutrino delta)
```

Three sectors stacked vertically as a ladder; shared dims at each junction:
- m2, m3 are shared between the proton Δ and the electron Y.
- m4 is the hub of the electron Y.
- m5 is shared between the electron Y and the neutrino Δ.

## 2. Sector-by-sector reading

### 2.1 Proton delta

- Δ on dims m1, m2, m3 with pairs `Ma((1,2), (1,3), (2,3))`.
- We earlier decided ([quark-search.md §4](quark-search.md)) that the proton Δ is unfavorable because two of its pairs share a ring dim and that forces a fixed mass-ratio that doesn't match the observed quark hierarchy. That analysis assumed the "smaller-as-tube" convention and disallowed compound modes. §3 below revisits both relaxations.
- The wye we currently use ([quark-search.md §9](quark-search.md)) uses 4 dims to host 3 pairs:
  ```
           m1
           |
           p
           |
           m2
          /  \
         p    p
        /      \
       m3      m4
  ```
- This "uses up 4 dimensions to create 3 sheets instead of 3." But in EE there is *always* a transformation between Δ and Y configurations. We don't yet have an analogous transformation here — and §3 will show the Δ requires an algebraic enrichment (compound modes) to recover the Y's fit quality. Worth characterizing the transformation if one exists.
- One conceptual advantage of the Δ: there is a clear "stable proton/neutron sheet" — the leg `Ma(2,3)` (at the base of the triangle). Modes occurring at higher energy on the legs `Ma(1,2)` and `Ma(1,3)` would *prefer* to fall to lower-energy modes on `Ma(2,3)` (or even further), if highly-stable configurations aren't found.
- Under this reading, `Ma(1,2)` would presumably host (t, b) and `Ma(1,3)` would host (c, s). These serve as high-energy temporary storage devices (imagine a capacitor or inductor) until energy can find a stable mode.

### 2.2 Electron wye

- The electron is shown as a Y, primarily so it can interface symmetrically with the proton Δ.
- The `Ma(2,4)` leg would be τ.
- The `Ma(3,4)` leg would be μ.
- The `Ma(4,5)` leg would be the electron.
- τ and μ serve as conduits for funneling energy into the stable electron leg. They could also pass energy *up* to the proton Δ (proton/neutron construction, β-decay).
- As in the proton picture, the upper two legs are not stable modes — they serve as transport up or down as the case may be.

### 2.3 Neutrino delta

- We have historically built the neutrino on a single sheet (here that would be a single pair `Ma(6,7)`), using internal shear to produce the three characteristic neutrino frequencies that explain oscillation.
- The Δ structure on (m5, m6, m7) offers an alternative: the three ν mass eigenstates could each live on one leg of the Δ (no internal-shear trio required). This is the same arrangement Candidate C uses.

### 2.4 Neutrino sheet (alternative)

- As an alternative to the ν-delta, we might consider a single vertical sheet `Ma(5,6)` (i.e., a single pair below the electron). But this is the extremely-tiny-tube model for the neutrino, which has unresolved problems.

## 3. The proton delta problem

This section analyzes whether the delta `Ma((1,2), (1,3), (2,3))` can fit the 6 observed quark masses. Three increasingly elaborate mode-selection schemes are tested by [scripts/sym_ladder_proton.py](../scripts/sym_ladder_proton.py); full numerics in [outputs/sym_ladder_proton.txt](../outputs/sym_ladder_proton.txt).

- **Test A — simple 2D modes per pair.** Each pair hosts one generation (lighter quark at T(1, 2), heavier at T(1, 1)), with per-pair tube/ring choice free. This is the "natural" interpretation of the delta: each leg = one generation. 6 free params (L_1, L_2, L_3, σ_12, σ_13, σ_23) vs 6 masses → just-determined; tested across all 48 gen-perm × tube/ring combinations.
- **Test B — compound 3D modes for heavy quarks.** u, d live on `Ma(2,3)` simple modes (T(1, 1), T(1, 2)). s, c, b, t live on compound 3D modes (1, n_2, n_3) on the (m1, m2, m3) torus with (n_2, n_3) ∈ {1, 2}². Closure is read per-pair-projection: T(1, n_2) on `Ma(1,2)` and T(1, n_3) on `Ma(1,3)` are each closure-valid for n_2, n_3 ≥ 1. The compound mode mass uses a chained-shear form `δ_3 = n_3 − σ_13 − σ_23·n_2` that breaks the separable "opposite-corners equal sum" constraint that the naive separable form imposes.
- **Test C — orphan 2D modes on the legs.** If Test B is the only fit that closes, then the upper legs `Ma(1,2)` and `Ma(1,3)` are *not* occupied by any individual quark — they only participate via the compound mode. The simple 2D modes T(1, 1) and T(1, 2) on each of these pairs (using the σ values from Test B) would be *orphan modes*, candidates for other observed particles. Report the predicted masses and compare to known particle masses.

### 3.1 Test A — simple 2D modes per pair

Each pair hosts one generation: lighter quark at T(1, 2), heavier at T(1, 1). Per-pair tube/ring is free. Six parameters (L_1, L_2, L_3, σ_12, σ_13, σ_23) vs six masses — just-determined.

**Result: best fit max |Δ%| = 137.2%.** All 48 configurations fail by more than 100%. The best representative:

| param | value |
|---|---|
| gen → pair | s/c → `Ma(1,2)`, u/d → `Ma(1,3)`, b/t → `Ma(2,3)` |
| tube/ring | `Ma(1,2)`.tube = m1, `Ma(1,3)`.tube = m3, `Ma(2,3)`.tube = m3 |
| L_1 | 4.7 × 10⁷ fm |
| L_2 | 0.88 fm |
| L_3 | 390 fm |
| σ_12 | +2.06 |
| σ_13 | +3.13 |
| σ_23 | −5.00 (hits bound) |

The optimizer is pushing σ values to the boundaries of the search range, which is the signature of a system whose algebraic structure cannot reach the target. **This confirms the [§4 obstruction](quark-search.md) even after lifting the smallest-as-tube convention** — per-pair tube/ring choice alone does not rescue the Δ. Two of the three pairs still end up with correlated mass scales that disagree with the observed quark hierarchy.

(For context: [quark-search.md §10](quark-search.md) found that *with* the additional Relaxation-1 mode flexibility — allowing m_t = 2 as a second-lowest mode per pair — the same delta closes to **3.97%**. So the strict-T(1, 1)/T(1, 2) reading is much tighter than the m_t-relaxed reading, and the simplest delta cannot match the wye's 0.5%.)

### 3.2 Test B — compound 3D modes for s, c, b, t

u, d live on `Ma(2,3)` simple modes; s, c, b, t live on compound modes (1, n_2, n_3) for (n_2, n_3) ∈ {1, 2}². The chained-shear form `δ_3 = n_3 − σ_13 − σ_23·n_2` provides a cross-coupling that breaks the separable-form "opposite-corners equal sum" constraint, so in principle the four compound masses can be fit independently. Six parameters vs six masses — just-determined.

**Result: best fit max |Δ%| = 1784%.** Every one of the 48 configurations fails by an order of magnitude or more. The best representative:

| param | value |
|---|---|
| (n_2, n_3) → quark | (1,1)→t, (1,2)→s, (2,1)→c, (2,2)→b |
| `Ma(2,3)` tube | m2 |
| L_1 | 892 fm |
| L_2 | 1.4 × 10⁸ fm |
| L_3 | 29 fm |
| σ_12 | −1.67 |
| σ_13 | −4.96 (near bound) |
| σ_23 | +1.05 |

**Why it fails — structural analysis.** The L's in the delta play multiple incompatible roles:

- L_2 must simultaneously be (i) the tube of `Ma(2,3)` (sets the baseline 1/L_T contribution for u, d ≈ 2 – 5 MeV) **and** (ii) a ring of the compound mode (sets a portion of the s↔c, b↔t mass splittings of order ~10² – 10⁵ MeV).
- L_3 similarly must double-serve as the ring of `Ma(2,3)` and a ring of the compound mode.

These two roles demand *very different* scales: u, d at ~1 fm vs heavy quarks at ~0.01 fm. No single L_2, L_3 simultaneously satisfies both.

Analytically: from `m_u² − m_d² = C·(3 − 2σ_23) ≈ −17 MeV²` (with C = (2πℏc/L_3)²), if we hit this constraint with σ_23 ∈ (−5, 5), then C ≤ ~30 MeV²/fm² and so L_3 ≥ ~200 fm. But for heavy-quark splittings like `m_c² − m_s² ≈ 1.6 × 10⁶ MeV²` to be reached with bounded δ_3, we need C ≥ ~10⁵ MeV²/fm², i.e. L_3 ≤ ~5 fm. **The two L_3 requirements are incompatible by 1–2 orders of magnitude.**

The chained-shear cross-coupling σ_23 cannot bridge this — it shifts the detunings but doesn't decouple the L_2, L_3 from their double role.

### 3.3 Test C — orphan 2D modes (not applicable)

Since Test B did not close, there is no consistent set of (L_1, L_2, L_3, σ_12, σ_13) from which to derive predicted T(1, 1) and T(1, 2) masses on `Ma(1, 2)` and `Ma(1, 3)` alone. If Test B had closed, those orphan modes would have been the natural candidates for non-quark observed particles (mesons, exotics) and would have been compared against the reference set (e, μ, π, K, η, ρ, ω, φ, τ, D, J/ψ, Υ, W, Z, H). That comparison can only be revisited if a future mode-selection scheme makes Test B close.

### 3.4 Net conclusion

**Neither scheme rescues the proton delta.** The simplest reading (one generation per leg) fails at 137%; the compound-3D-mode rescue fails at 1784%. The structural reason is the same in both: the delta has 3 dims that must collectively encode both the small-scale (u, d ~ MeV) and large-scale (t ~ 10⁵ MeV) physics through cross-terms alone, but the dims cannot simultaneously satisfy both regimes. The wye's escape was adding a 4th dim (the hub) whose only job is to be a common tube, freeing the other three dims to be independent rings.

**The EE Δ-Y transformation analogy does not survive** in the form the user hoped: the wye is not just a re-parameterization of the delta; it genuinely has more structural freedom. The 4th dim of the wye contributes a degree of freedom the delta cannot replicate with cross-couplings alone (at least not with the chained-shear or separable forms tested).

### 3.5 Caveats and what could still rescue it

- **Richer compound-mode cross-coupling.** The chained-shear form may be too restrictive. A bilinear cross-term D·δ_2·δ_3 introduced as an *independent* free parameter (rather than tied to σ_23) would give 7 parameters for 6 masses — underdetermined, so trivially fittable — but loses the parsimony that motivated the search in the first place. A richer parameterization would need a physical justification (where does D come from in the 3-torus metric?).
- **Full inverse-metric formulation.** I used the chained-shear analog of the standard pair formula. The "true" 3-torus inverse-metric mass formula is structurally similar but not identical. It might fit where the chained-shear doesn't — worth trying if this direction is pursued further.
- **Accepting larger residuals for heavy quarks.** If we accept that c, s, b, t are transient transport modes whose exact current-quark masses are not architectural predictions (the user's "high-energy temporary storage" interpretation), then Test A's 137% or Test B's 1784% become "approximate placeholders" rather than failure. This is a substantial reframing — gives up the 0.5% achievement of the wye — but is the natural philosophical move if the "stable center, unstable legs" pattern is taken seriously.
- **Higher modes.** Allowing m_t > 1 on the legs (Relaxation 1 in [quark-search.md §10](quark-search.md)) brought the simple delta to 4%. The same relaxation has not been combined with the compound-mode scheme.

## 4. General thoughts

- This model is appealing on several levels.
- It seems to provide a model for *why* some modes are stable and others are not: stable modes are "centered" on the graph (they have dual unstable legs in symmetric relationship), and unstable modes live on the legs that transport energy toward the centers.
- The shared dims (m2, m3 between proton-Δ and electron-Y; m5 between electron-Y and ν-Δ) give a geometric basis for cross-sector processes like β-decay.
- The hinge is §3: the proton-Δ must be able to host all 6 quarks comparably to the wye. If compound modes are required, the architecture's "plane over diagonal" rule ([architecture.md §3.3](architecture.md)) needs to be reframed — 3D-mixed modes would become the heavy-quark class rather than the dark/unobserved class.
