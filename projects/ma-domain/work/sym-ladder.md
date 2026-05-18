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

---

## 5. The leakage mechanism — reading the ladder dynamically

The §3 negative result rests on a static reading: each leg is treated as a closed cavity whose eigenmodes are stable particle states. Under that reading the heavy-quark masses must be exact eigenvalues of the proton-Δ's three legs, and three legs cannot supply enough geometric freedom to fit all six quark masses (§3.4).

A dynamic reading reverses this. The ladder is not three independent cavities; it is a single connected manifold whose legs share dims. **A mode on a leg is stable iff no lower-energy mode is accessible to it through any shared-dim channel.** Charged closure modes on the side legs of the proton-Δ have a lower-energy target available (u, d on the base leg), so they decay. The "negative result" of §3 is then re-read: it says exactly that there are no stable charged eigenstates on the side legs *because* energy on those legs flows out to the base leg. That's the prediction, not the failure.

The same reading carries through every sector of the ladder: stable particles sit on a leg whose ground-state mode has no accessible-lower target; unstable particles sit on legs whose modes have such targets.

### 5.1 Statement of the principle

The leakage principle, restated for use throughout the rest of this document:

> **A closure mode |ψ_A⟩ on a pair A is dynamically stable if and only if no lower-energy mode |ψ_B⟩ exists on any pair B such that A and B share at least one dim and the matrix element ⟨ψ_B | V | ψ_A⟩ is non-zero. Otherwise the mode decays with rate Γ_{A → B} set by the matrix element and the density of states on B.**

The decay is not exotic; it is the standard route for energy to find a more favorable configuration in any coupled-cavity system. The "more favorable" criterion is energetic (lower mass) and the "accessible" criterion is geometric (shared dim with a non-zero overlap integral).

### 5.2 Empirical credibility

Observed particle decays are universal: every massive particle heavier than the lightest in its sector decays, with no known exceptions among the unstable particles in the Standard Model. The lifetimes range over 26 orders of magnitude, from t-quark (10⁻²⁵ s) to free neutron (~880 s), but the *fact* of decay is robust whenever a lower-energy state with the right quantum numbers exists. The standard model attributes this to weak interactions mediated by W, Z exchange; the sym-ladder reading attributes it to mode leakage through shared dims. Both pictures predict the same observable: lighter target → finite decay rate.

So the leakage mechanism is not a speculative addition. It is the *expected* behavior of any geometrically-connected mode spectrum. The non-trivial task is to show that the geometric leakage rates match the observed lifetimes — that is the test, not the postulate.

### 5.3 Geometric basis

Three ingredients together produce a non-zero leakage rate from pair A to pair B:

1. **A shared dim m_k.** The two pairs must overlap geometrically at at least one dim. Without overlap there is no matrix element.

2. **Mode-overlap at the shared dim.** The wavefunctions ψ_A(x_k) and ψ_B(x_k) must have non-zero overlap integral on the shared dim. For Bloch-labeled modes this means matching k_θ values modulo the relevant Bloch sector mismatch; off-diagonal σ-coupling provides the required sector mixing.

3. **Energy ordering.** E_B < E_A. The rate vanishes by Fermi's golden rule if there is no available lower target.

The rate takes the schematic form

<!-- Γ_{A → B} = (2π/ℏ) · |⟨ψ_B | V_k | ψ_A⟩|² · ρ_B(E_A) -->
$$
\Gamma_{A \to B} \;=\; \frac{2\pi}{\hbar} \,\bigl| \langle \psi_B \,|\, V_k \,|\, \psi_A \rangle \bigr|^2 \, \rho_B(E_A)
$$

where V_k is the coupling operator at the shared dim m_k and ρ_B(E_A) is the density of states on pair B at the source energy. The matrix element depends on:

- L_k (the size of the shared dim — affects mode normalisation)
- σ values on both pairs (the off-diagonal m_t mixing strength)
- Cross-section shape on both pairs (the lobe/saddle geometry at the junction)
- The Bloch sector mismatch (no leakage if the sectors are orthogonal and σ does not mix them)

When the source mode is charged and the target is uncharged, charge must be carried away by a byproduct (lepton + neutrino in the Standard Model picture). The byproduct's existence requires that an even-further sheet (typically the electron-Y) couples in the same channel. This is what makes β-decay a *three-sheet process* rather than a two-sheet process in the sym-ladder.

### 5.4 The leakage channel map

The shared-dim topology of the ladder defines exactly which leakage transitions are geometrically allowed. Reading off the diagram in §1:

| Source pair | Target pair | Shared dim | Physical process |
|---|---|---|---|
| Ma(1, 2) [proton-Δ side] | Ma(2, 3) [proton-Δ base] | m2 | Heavy-quark decay to u/d on the base |
| Ma(1, 3) [proton-Δ side] | Ma(2, 3) [proton-Δ base] | m3 | Heavy-quark decay to u/d on the base |
| Ma(1, 2) | Ma(1, 3) | m1 | Inter-side-leg transfer (cross-leg charm/strange interconversion candidate) |
| Ma(1, 2) | Ma(2, 4) [electron-Y top] | m2 | Cross-sector: proton-Δ → electron-Y |
| Ma(1, 3) | Ma(3, 4) [electron-Y top] | m3 | Cross-sector: proton-Δ → electron-Y |
| Ma(2, 3) | Ma(2, 4) | m2 | Base → electron-Y top (β-decay precursor) |
| Ma(2, 3) | Ma(3, 4) | m3 | Base → electron-Y top (β-decay precursor) |
| Ma(2, 4), Ma(3, 4) [electron-Y top] | Ma(4, 5) [electron stable] | m4 | τ, μ → e decay |
| Ma(2, 4) | Ma(3, 4) | m4 | μ ↔ τ cross-leg |
| Ma(4, 5) | Ma(5, 6), Ma(5, 7) | m5 | Electron-Y → neutrino-Δ (emission of ν) |
| Ma(5, 6), Ma(5, 7), Ma(6, 7) | each other | m5, m6, m7 | Neutrino oscillation |

This is a complete catalogue: every shared dim is an allowed channel; every pair-pair leakage in the Standard Model corresponds to one or a chain of these.

### 5.5 Reframing the §3 negative result

Under the dynamic reading, the §3 Tests A and B are correctly diagnostic — they show that no exact mass eigenvalues for c, s, b, t are realized on the proton-Δ as stable modes. The Standard Model agrees: c, s, b, t are never observed as free stable particles. The framework is consistent with that observation. What §3 misses is that the *transient* resonances at the c, s, b, t energies need not be exact mass eigenvalues — they are quasi-stable peaks whose finite lifetime is set by the leakage rate.

The new question — replacing "do the masses fit?" — is **"do the leakage rates match the observed lifetimes?"** Specifically:

- τ_c ≈ 10⁻¹² s
- τ_s (in bound states) ≈ 10⁻¹⁰ s
- τ_b ≈ 10⁻¹² s
- τ_t ≈ 10⁻²⁵ s

If the geometric Γ values from the formula in §5.3 reproduce these lifetimes within reasonable tolerance, the reframing is validated and §3's "negative result" becomes a positive structural prediction.

---

## 6. Development strategy

Five phases, ordered to minimize new computation in early phases (using already-fitted L and σ values where possible) and to maximize falsifiability.

### 6.1 Phase 1 — Formalize the leakage rate

Derive a concrete formula for Γ_{A → B} in terms of the ladder's geometric parameters. The Fermi's-golden-rule expression in §5.3 is the right starting point but needs to be unpacked:

- **Express V_k explicitly.** The coupling operator at the shared dim m_k comes from the Laplacian's boundary condition at the junction between pairs A and B. For pairs sharing one dim, the natural continuity condition is the wavefunction and its normal derivative matching at x_k = 0. The matrix element ⟨ψ_B | V_k | ψ_A⟩ is then an integral over the shared dim of ψ_A* ψ_B times a junction factor.

- **Express ρ_B(E_A) explicitly.** Density of states on pair B at energy E_A. For a 2D Helmholtz spectrum, ρ_B(E) scales as L_T · L_R / E (Weyl law in 2D). Refinements include the specific Bloch sector and cross-section shape.

- **Identify the small parameters.** The Bloch-sector mismatch between (m_t^A, m_r^A) on pair A and accessible (m_t^B, m_r^B) on pair B is the leading suppression. Without σ-coupling the matrix element is identically zero for mismatched sectors; with σ ≠ 0 it scales as σ^|Δm_t| (multiplicative in successive sector hops).

- **Account for charge conservation.** If E_A is a charged-mode energy and E_B is uncharged, then the process needs a byproduct (lepton + neutrino) to carry the charge. In the ladder this means *the matrix element is non-zero only if a further pair (the electron-Y for fractional → integer transitions, the neutrino-Δ for integer → zero-charge transitions) is also coupled in the same step.* The full Γ is the product of overlaps at every intermediate sheet, picking up a small factor per shared-dim hop.

**Deliverable:** A closed-form expression Γ_{A → B}(L_A, L_B, σ_A, σ_B, shape, sector) suitable for numerical evaluation.

### 6.2 Phase 2 — Test on the electron wye (lepton lifetimes)

The electron-Y is the cleanest test bed:

- **Geometry is already fixed.** [candidates.md §3](candidates.md) reports a 0.000% mass fit for (e, μ, τ) on the Y, so the L_i and σ_ij for the electron sector are known modulo the residual lepton↔pair-assignment ambiguity.

- **Decay rates are precisely measured.** τ_τ = (2.903 ± 0.005) × 10⁻¹³ s, τ_μ = (2.197 ± 0.000) × 10⁻⁶ s. These pin Γ to better than 1% relative.

- **No QCD complications.** Lepton decays are dominated by the weak interaction in the Standard Model; the geometric version is equivalently dominated by mode leakage. No bound-state corrections muddy the comparison.

- **Same mechanism, different sector.** τ → e + ν̄_e + ν_τ goes Ma(τ-leg) → Ma(4, 5) via m4 → Ma(5, ν-leg) via m5. Three sheets, two shared-dim hops, byproduct e + ν̄ + ν.

**Predictions to test:**

1. **Magnitude.** Does the Γ formula from §6.1, evaluated on the fitted Y geometry, give τ_τ ≈ 0.3 ps and τ_μ ≈ 2 μs? Order-of-magnitude agreement is the first hurdle; few-percent agreement is the success criterion.

2. **Ratio.** Γ_τ / Γ_μ ≈ 1.7 × 10⁷ in observation. The geometric prediction scales as (m_τ / m_μ)⁵ ≈ 4.5 × 10⁵ from phase space alone (Sargent's rule); the rest comes from coupling and matrix element scaling. Does the geometric formula reproduce both the m⁵ phase-space factor AND the additional ~40× from couplings?

3. **Branching.** μ has only one significant decay channel (μ → e + 2ν, ~100% branching). τ has many (e channel, μ channel, hadronic channels). The geometric mechanism predicts the e- and μ-channels via the leakage map; the hadronic channels require the proton-Δ to also be coupled in. Does the framework predict ~17% e-channel + ~17% μ-channel + ~64% hadronic for τ, as observed?

**Deliverable:** A script that takes (L_i, σ_ij from candidates.md) as input and outputs Γ_τ, Γ_μ, plus τ branching ratios. Comparison to PDG values is the test.

### 6.3 Phase 3 — Transplant to the proton delta (heavy-quark lifetimes)

If Phase 2 succeeds, the same formula machinery applies to the proton-Δ side legs. The proton-Δ geometry under sym-ladder is not yet fitted (per §3 the static fit fails); but if §6.1's formula is general, it can be inverted from observed lifetimes to *infer* the L_i, σ_ij values that make the heavy-quark transients consistent with observation.

**Observed lifetimes (representative bound-state values):**

- D meson (cū): τ_D ≈ 4 × 10⁻¹³ s → effective Γ_c ≈ 2.5 × 10¹² s⁻¹
- B meson (bū): τ_B ≈ 1.5 × 10⁻¹² s → effective Γ_b ≈ 7 × 10¹¹ s⁻¹
- top (free): τ_t ≈ 5 × 10⁻²⁵ s → Γ_t ≈ 2 × 10²⁴ s⁻¹
- K meson (sū): τ_K ≈ 10⁻⁸ s → Γ_s ≈ 10⁸ s⁻¹

**Predictions to test:**

1. **Strange/charm/bottom/top hierarchy.** Γ scales steeply with mode energy via phase space and density of states. Geometric Γ(c) / Γ(s) should be ≈ 10⁴; Γ(t) / Γ(b) should be ≈ 10¹². Reproducing this 12-order spread is the main test.

2. **Why t doesn't bind.** τ_t ≈ 10⁻²⁵ s is shorter than the QCD timescale (~10⁻²³ s for hadronization). In the geometric reading, this means the t-mode leaks faster than it can localise into a bound state. The framework should predict the *exact* energy above which leakage outpaces localisation, and that energy should fall between b and t.

3. **No stable heavy proton.** A "uudt" baryon would, in the static reading, be a stable bound state of three quarks on the proton-Δ. The geometric reading predicts its lifetime ≈ Γ_t⁻¹ ≈ 10⁻²⁵ s, far below any bound-state formation time. So heavy baryons are predicted *not to exist* as stable particles — exactly what is observed.

**Deliverable:** Inverse fit of the proton-Δ geometry (L_1, L_2, L_3, σ_12, σ_13, σ_23) from heavy-quark lifetime data. Sanity check: does this geometry also reproduce the u/d masses on the base leg under the standard mass formula (since Ma(2,3) is the stable leg)?

### 6.4 Phase 4 — Cross-sector decays (β-decay)

β-decay is the canonical multi-sheet leakage: n → p + e⁻ + ν̄_e. Under sym-ladder:

- Source: T(1, 1) on Ma(2, 3) (neutron, heavier base-leg mode)
- Target: T(1, 2) on Ma(2, 3) (proton, lighter base-leg mode) + e on Ma(4, 5) + ν̄ on neutrino-Δ
- Path: Ma(2, 3) → Ma(2, 4) or Ma(3, 4) [via m2 or m3] → Ma(4, 5) [via m4] → emission of ν̄ on neutrino-Δ [via m5]

**Predictions to test:**

1. **Lifetime.** τ_n ≈ 880 s in observation. Geometric Γ from the formula in §6.1, with the *full three-sheet path*, should give Γ_n ≈ 10⁻³ s⁻¹.

2. **Q-value.** The decay Q-value (kinetic energy released) is 0.78 MeV, the n-p mass difference. The framework already reproduces this to within 0.03% from the wye fit ([clover-mass.md §8](../../sheet-proton/work/clover-mass.md)). The leakage picture is consistent with this — it only constrains the *rate*, not the mass difference.

3. **Why n is so long-lived.** Of all known unstable particles, the neutron has the longest lifetime by 8+ orders of magnitude. In the geometric reading, this is because n → p requires a *three-sheet* transition (proton-Δ → electron-Y → neutrino-Δ) — the matrix element picks up a small factor at every hop. Most other decays are one- or two-sheet (μ → e is one-sheet within the electron-Y, modulo the ν emission). The hierarchy of lifetimes should track the number of sheet-hops required.

### 6.5 Phase 5 — Predictions

If Phases 2–4 close to within their measurement precision, the framework will have made a non-trivial structural prediction. The fifth phase extracts predictions that go beyond reproducing known observations:

- **Forbidden decays as missing channels.** Any decay not enumerated in §5.4's table is predicted *not* to occur (or to occur only at higher loop order, with small rates). Examples: lepton-flavor-violating decays like μ → e + γ require a path that the ladder does not provide at tree level.

- **Neutrino oscillation rates.** The Δ-on-(m5, m6, m7) admits internal mixing among ν_e, ν_μ, ν_τ via shared dims within the ν-Δ. The mixing matrix elements come from the same §6.1 formula applied with all three pairs of the ν-Δ. PMNS-matrix elements (specifically θ_12, θ_23, θ_13, δ_CP) are predicted in terms of L_5, L_6, L_7, σ_56, σ_57, σ_67. This is a 3-parameters-from-3-observations test.

- **Cross-section structure.** Particle decays are not just rates — they have angular distributions, polarisations, kinematic correlations. The geometric mechanism predicts these via the wavefunction overlap integrals, not just the |⟨B|V|A⟩|² magnitude. Some are directly testable against existing collider data (e.g., the parity-violation structure of τ → e + ν̄_e + ν_τ).

- **The dark sector.** If the leakage mechanism is the complete story for energy flow in the ladder, then anything not captured by the §5.4 table is genuinely undecaying. Pure ring modes (m_t = 0 on any pair) are non-closure, so they're not particles in the standard sense — but they may carry energy through the sheets in a non-radiative way. These are candidates for the "dark" sector (cold dark matter or its cosmological-constant analog).

---

## 7. Empirical anchors

Reference values to test against during development. All in standard PDG conventions; lifetimes are particle rest-frame.

| Particle | Mass (MeV) | Lifetime (s) | Path in ladder |
|---|---:|---:|---|
| u | 2.16 | stable | Ma(2,3) ground (T(1, 2)) |
| d | 4.67 | stable | Ma(2,3) excited (T(1, 1)) |
| s (in K) | 93 | ~10⁻⁸ | Ma side → Ma(2,3) via m2 or m3 |
| c (in D) | 1270 | ~4 × 10⁻¹³ | Ma side → Ma(2,3) via m2 or m3 |
| b (in B) | 4180 | ~1.5 × 10⁻¹² | Ma side → Ma(2,3) via m2 or m3 |
| t (free) | 173000 | ~5 × 10⁻²⁵ | Ma side → Ma(2,3) via m2 or m3 |
| e | 0.511 | stable | Ma(4, 5) ground (T(1, 2)) |
| μ | 105.7 | 2.20 × 10⁻⁶ | Ma(?, 4) → Ma(4, 5) via m4 |
| τ | 1776.9 | 2.90 × 10⁻¹³ | Ma(?, 4) → Ma(4, 5) via m4 |
| ν₁, ν₂, ν₃ | < 1 eV | stable (mass eigenstates) | ν-Δ |
| n | 939.6 | 880 | Ma(2,3) T(1,1) → T(1,2) + 3-sheet |

The lifetime span is 26 orders of magnitude. The framework must reproduce this dynamic range from one formula evaluated on different ladder geometries.

---

## 8. Open questions

1. **Does the wye remain in play?** §6.3 asks the proton-Δ geometry to also reproduce u/d masses on Ma(2,3) under the standard mass formula. If yes, the wye and the proton-Δ become *complementary* views: the wye says where the mass eigenvalues are; the sym-ladder says which are stable and which decay. If no, the proton-Δ geometry inferred from lifetimes contradicts the u/d mass fit, and one of the two must be wrong. Worth doing this check early in Phase 3.

2. **Bound states.** Quarks are never observed free; they appear in hadrons. The leakage mechanism is computed at the level of free quark modes. Translating to D, B, K meson lifetimes requires either a bound-state correction (additional factor from hadronization probability) or a derivation directly on the bound-state geometry. The latter is cleaner but adds work.

3. **Cross-section structure not yet in the formula.** §6.1's Γ formula uses scalar matrix elements. Real decays have spin structure, angular distributions, and helicity dependence. Including these requires extending the mass-formula derivation to spinor fields (Dirac-Kähler-style on the sheets, per [model-F.md](../../../models/model-F.md)).

4. **What does Mechanism B (Relaxation-1, m_t = 2) become in this picture?** §3.2's compound modes and Relaxation-1's m_t = 2 modes are *higher-energy excitations* on side legs. In the leakage picture they would be expected to decay even faster than the m_t = 1 modes (more available targets, shorter lifetime). Are they observed as ultra-short resonances at the right energies? This is a falsifiable prediction worth checking against collider data.

5. **The neutrino sector.** The ν-Δ admits internal cross-leakage (§5.4), which the framework should predict as PMNS oscillation. The PMNS parameters are measured (θ_12 ≈ 33°, θ_23 ≈ 49°, θ_13 ≈ 8.6°, δ_CP ≈ 195°). Whether the ν-Δ geometry can simultaneously fit (a) the three ν masses, (b) the PMNS angles, and (c) the cross-sector emission rates in β-decay is a 3+3+1 = 7-observation test of a 6-parameter sub-geometry — tight but tractable.

6. **What sets the scale of σ values?** σ ∈ [0, 5] is the search range in current scripts. The leakage rate depends on σ through the matrix element. Are there structural constraints (gauge-symmetry-like, or geometric like the rolled-leaf intrinsic shear in [clover-quarks §1.3](../../sheet-proton/work/clover-quarks.md)) that fix σ values from first principles?

7. **Connection to the wye and to candidates B/C.** Candidates B/C use a wye for quarks plus a delta for electrons; sym-ladder reverses this. If both turn out to admit consistent leakage interpretations, the choice between them rests on which one reproduces the full lifetime hierarchy with fewer parameters. The Phase-2 calculation on the electron-Y is identical for both architectures (both have an electron-Y); Phase 3 is where they diverge.

---

## 9. Next concrete step

The single highest-leverage computation is **§6.2 Phase 2 on the electron wye**: take the fitted L_i and σ_ij values from candidates.md's e-Y solution, write down the §6.1 formula, evaluate it for τ → e and μ → e, and compare to observed lifetimes. If the result is within an order of magnitude, the mechanism is real and the rest of the program is worth pursuing. If it is off by ten orders of magnitude, the formula or the geometry is wrong and the framework needs work before the rest of the strategy makes sense.

This is one script, using existing fitted parameters. No new geometry, no new architecture decision. Just the leakage formula applied to the cleanest test bed available. It is the right place to start.
