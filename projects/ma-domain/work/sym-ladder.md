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

### 5.3 Geometric basis — the leaky-resonance picture

A "particle" in the sym-ladder is a **pair-localized wavepacket**: a state concentrated mostly on one pair, with small-amplitude tails reaching through shared dims into adjacent pairs. Such a state is generally *not* an eigenstate of the full ladder's Laplace–Beltrami operator — its true eigenstates are delocalized across the whole connected manifold. Time-evolved under the full Hamiltonian, the localized wavepacket's amplitude on the source pair decays exponentially for short-to-medium times, at a rate set by the **complex resonance pole** of the full ladder's Green's function for that initial state:

<!-- Γ = -2 Im(E_resonance) / ℏ -->
$$
\Gamma \;=\; -\frac{2\,\mathrm{Im}(E_{\text{resonance}})}{\hbar}
$$

This is the Gamow / quasi-stationary state formalism. It is purely geometric — derived from the wave equation on the connected manifold without any external rate axiom.

Three ingredients together produce a non-zero Im(E_resonance):

1. **A shared dim m_k.** The two pairs must overlap geometrically at at least one dim. Without overlap the resonance pole stays on the real axis (no decay).

2. **Mode-overlap at the shared dim.** The wavefunctions ψ_A(x_k) and ψ_B(x_k) must have non-zero overlap integral on the shared dim. For Bloch-labelled modes this means matching k_θ values modulo Bloch-sector mismatch; off-diagonal σ-coupling provides the required sector mixing.

3. **Lower-energy targets accessible.** E_B < E_A for some target mode. Energy conservation forces Im(E_resonance) = 0 if no lower-energy continuum is available.

In the **weak-coupling limit** (small σ at junctions, narrow geometric overlap regions), the resonance-pole rate reduces analytically to the familiar Fermi's-golden-rule expression:

<!-- Γ_{A → B} ≈ (2π/ℏ) · |⟨ψ_B | V_k | ψ_A⟩|² · ρ_B(E_A) -->
$$
\Gamma_{A \to B} \;\approx\; \frac{2\pi}{\hbar} \,\bigl| \langle \psi_B \,|\, V_k \,|\, \psi_A \rangle \bigr|^2 \, \rho_B(E_A)
$$

FGR is a useful tool for hand calculation, but the **underlying object is the resonance pole** — FGR is its leading-order approximation, valid where the coupling is small and target spectra are dense. At strong coupling, near level crossings, or where target spectra are sparse, FGR breaks down and the resonance-pole formulation is needed directly.

The matrix element (or equivalently, the residue of the resonance pole) depends on:

- L_k (the size of the shared dim — affects mode normalisation)
- σ values on both pairs (the off-diagonal m_t mixing strength)
- Cross-section shape on both pairs (the lobe/saddle geometry at the junction)
- Bloch-sector mismatch (zero unless σ-coupling bridges the source and target sectors)

### 5.4 Channel classes

When the source mode is charged and the target is uncharged, charge must be carried away by a byproduct. Three byproduct classes give three channel classes, each carrying its own geometric prefactor in the rate formula:

- **Weak channels** — byproduct is one or more leptons (electron, neutrino). The decay path traverses the electron-Y and ν-Δ. The rate factors into per-sheet overlap integrals at each shared dim. The product is the geometric analog of the Fermi coupling G_F. Sargent-rule m⁵ scaling for 3-body decays emerges from the phase-space integration over the byproducts, not from G_F itself.

- **EM channels** — byproduct is one or more photons. The decay path traverses whatever sheet hosts EM modes ([model-F](../../../models/model-F.md) places these on dedicated photon sheets in the 11D architecture). The rate carries a factor of α. Under [model-F](../../../models/model-F.md), α is a **derived** geometric ratio (cross-section / ring radius on the photon sheet), not a free coupling constant. Validating this derivation is a sub-program of the rate calculation (see §8 open questions).

- **Strong channels** — internal rearrangement within a sheet's bound-state structure (e.g., quark hadronisation). The rate carries a factor of α_S, much larger than α, set by the quark-sheet's geometric structure.

Every decay rate factors as

<!-- Γ = (geometric coupling factor) × (phase space) × (matrix-element overlap) -->
$$
\Gamma \;=\; (\text{geometric coupling factor}) \,\times\, (\text{phase space}) \,\times\, (\text{matrix-element overlap})
$$

with the first factor distinguishing weak/EM/strong, the second purely kinematic, and the third capturing the wavefunction overlap at shared dims. Many empirical regularities (Sargent's rule, the α-suppression of radiative decays, the α_S enhancement of hadronic widths) are statements about *which factor dominates* in a given channel — they're not separate inputs in the geometric framework.

This is what makes β-decay a *three-sheet process* rather than a two-sheet process in the sym-ladder: the neutron's downward transition on Ma(2, 3) emits both an electron (path through the e-Y) and an antineutrino (path through the ν-Δ), so the matrix element is a product of overlap integrals at *two* shared-dim hops, not one.

### 5.5 The leakage channel map

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

### 5.6 Reframing the §3 negative result

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

### 6.1 Phase 1 — Formalize the leakage rate from the resonance pole

The fundamental object is **the resonance pole of the Green's function** for a pair-localized initial state, evaluated on the full ladder's Laplace–Beltrami operator (§5.3). Phase 1 is the mathematical derivation of this pole structure in a form usable for the rest of the program.

Two equivalent formulations are available, with different trade-offs:

**Formulation A — direct resonance pole.** Construct the Green's function G(E) for the full ladder's wave operator, find its complex pole nearest to each pair-localized state's unperturbed energy, and extract Γ = −2 Im(E_pole) / ℏ. This is exact at any coupling strength but typically requires either complex-scaling techniques or numerical contour analysis.

**Formulation B — Fermi's-golden-rule limit.** Assume weak coupling between pairs and dense target spectra; expand the resonance pole's imaginary part to leading order in the coupling. This recovers

<!-- Γ_{A → B} ≈ (2π/ℏ) · |⟨ψ_B|V_k|ψ_A⟩|² · ρ_B(E_A) -->
$$
\Gamma_{A \to B} \;\approx\; \frac{2\pi}{\hbar} \,\bigl| \langle \psi_B \,|\, V_k \,|\, \psi_A \rangle \bigr|^2 \, \rho_B(E_A)
$$

which is analytically tractable for closed-form sheet geometries (ellipse, clover, Fourier polar curves).

**Phase 1 approach: use Formulation B as the working tool, validate against Formulation A in test cases.** FGR is *not* an external axiom — it is a derived consequence of Formulation A in the weak-coupling regime. Treat it as a tool, not as a foundation. Once Formulation B's predictions agree with Formulation A in a tractable test geometry (e.g., two pairs sharing one dim with a single mode each), trust FGR for the rest of the calculations.

The unpacking work that Phase 1 must produce, in either formulation:

- **Express V_k (or the equivalent junction operator) explicitly.** The coupling at the shared dim m_k comes from the Laplacian's matching condition at the junction between pairs A and B — wavefunction and normal derivative continuous at x_k = 0. The matrix element ⟨ψ_B | V_k | ψ_A⟩ is then an integral over the shared dim of ψ_A* ψ_B times a junction factor.

- **Express ρ_B(E_A) explicitly.** Density of states on pair B at energy E_A. For a 2D Helmholtz spectrum, ρ_B(E) scales as L_T · L_R / E (Weyl law in 2D). Refinements include the specific Bloch sector and cross-section shape.

- **Identify the small parameters.** The Bloch-sector mismatch between (m_t^A, m_r^A) on pair A and accessible (m_t^B, m_r^B) on pair B is the leading suppression. Without σ-coupling the matrix element is identically zero for mismatched sectors; with σ ≠ 0 it scales as σ^|Δm_t| (multiplicative in successive sector hops).

- **Factor by channel class.** Following §5.4, write Γ explicitly as the product (channel-class coupling factor) × (phase-space integral) × (overlap matrix element). For weak channels the coupling factor is the geometric G_F analog (a product of per-sheet overlaps at the byproducts' sheets); for EM channels it carries α (geometric on a photon sheet, see §8 open questions); for strong channels it carries α_S.

- **Verify Sargent emergence.** For 3-body lepton decays (μ → e + 2ν, τ → e + 2ν, β-decay), check that the phase-space integral reproduces Sargent's m⁵ / 192π³ scaling without it being put in by hand. This is a structural prediction: if m⁵ does not fall out of the geometric phase-space integration, the formulation is wrong.

**Deliverable:** A closed-form expression for Γ that factors transparently into (geometric coupling factor, phase space, matrix element), with each factor traceable to a specific geometric ingredient. Suitable for analytical evaluation on the e-Y in Phase 2.

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

7. **Connection to the wye and to candidates B/C.** Candidates B/C use a wye for quarks plus a delta for electrons; sym-ladder reverses this. If both turn out to admit consistent leakage interpretations, the choice between them rests on which one reproduces the full lifetime hierarchy with fewer parameters. Note also that candidates.md's electron sector is a **Δ** on (m1, m2, m5), while sym-ladder's electron sector is a **Y** on (m2, m3, m4, m5). The Y's tighter "all three pairs share m4" constraint may or may not still admit a 0.000% mass fit for (e, μ, τ); confirming this is **Step 0** of the actual program, before any leakage calculation begins.

8. **Resonance-pole vs FGR — when does the approximation fail?** Phase 1 uses FGR (Formulation B in §6.1) as the working tool, validated against the exact resonance pole (Formulation A) in test geometries. The known failure modes of FGR are: (i) strong coupling, where higher-order corrections in σ become significant; (ii) near-degeneracies between source and target energies, where level repulsion dominates; (iii) sparse target spectra, where the continuum-density approximation breaks down. Cataloguing where in the ladder these regimes apply — and computing Formulation-A corrections where they do — is a separate sub-program of Phase 1.

9. **α from geometry — required for EM channels.** The §5.4 channel-class decomposition assigns α as the geometric coupling factor for EM channels, and assumes that α is *derived* from sheet geometry rather than fitted ([model-F](../../../models/model-F.md) claims this derivation). Validating model-F's geometric-α derivation is a prerequisite for trusting any EM-mediated decay rate in this framework. If model-F's α derivation does not survive scrutiny, EM-channel rates would need α as an input — reducing the framework's predictive power for radiative decays. This is the single open question with the largest impact on the strategy: a working geometric α makes the framework genuinely predictive; a failed one shifts EM-channel rates into the "fitted with one parameter per channel class" regime.

10. **What if FGR-equivalent Γ fails Phase 2?** The strategy assumes that the leakage mechanism, evaluated on the e-Y, will reproduce τ_τ and τ_μ at the right order. If it does not — e.g., gives Γ wrong by 10⁵× — the diagnosis is one of: (a) the Y geometry is wrong (electron sector is actually a Δ, per candidates B/C); (b) the FGR limit is not valid here (need Formulation A); (c) the matrix element is missing a structural factor (e.g., spin/Dirac–Kähler structure, see open question 3); (d) α is not what model-F says it is. The Phase-2 calculation should be designed so that its failure mode is diagnostic — i.e., the residual ratio identifies which of (a)-(d) is responsible.

---

## 9. Next concrete step

The single highest-leverage computation is **§6.2 Phase 2 on the electron wye**: take the fitted L_i and σ_ij values from candidates.md's e-Y solution, write down the §6.1 formula, evaluate it for τ → e and μ → e, and compare to observed lifetimes. If the result is within an order of magnitude, the mechanism is real and the rest of the program is worth pursuing. If it is off by ten orders of magnitude, the formula or the geometry is wrong and the framework needs work before the rest of the strategy makes sense.

This is one script, using existing fitted parameters. No new geometry, no new architecture decision. Just the leakage formula applied to the cleanest test bed available. It is the right place to start.
