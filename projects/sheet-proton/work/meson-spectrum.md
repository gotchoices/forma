# meson-spectrum.md — light mesons as 2-component compounds

**Status:** Exploratory work file. Catalogs candidate identifications of QCD light mesons (π, K, η, ρ, ω, φ, ...) with 2-component qq̄ compounds in the MaSt framework. Sister to [strong.md](strong.md) (where the pion serves as mediator), [quark-flavor.md](quark-flavor.md), [color-confinement.md](../../metric-binding/work/color-confinement.md).

**Tone:** Exploratory. The meson spectrum is empirically well-measured; this file's job is to see whether MaSt's compound-mode framework reproduces it.

**Substrate note.** This file uses R64's round-tube proton sheet for its baseline analysis. The corrugated-clover substrate ([clover-quarks.md](clover-quarks.md), [clover-mass.md](clover-mass.md)) has been developed for baryons (proton, neutron) but **not yet extended to qq̄ mesons**. The qq̄ → (0, 0) summed-winding structure (and hence the pion-mass-from-zero problem) is the same in both substrates — see §9 below.

---

## 1. The question

In QCD, mesons are quark-antiquark bound states. The light meson zoo includes:

| Meson | qq̄ content | Mass (MeV/c²) | Spin-parity |
|---|---|---|---|
| π⁺ | ud̄ | 140 | 0⁻ |
| π⁻ | dū | 140 | 0⁻ |
| π⁰ | (uū − dd̄)/√2 | 135 | 0⁻ |
| K⁺ | us̄ | 494 | 0⁻ |
| K⁰ | ds̄ | 498 | 0⁻ |
| η | (uū + dd̄ − 2ss̄)/√6 | 548 | 0⁻ |
| η' | ... | 958 | 0⁻ |
| ρ | (uū − dd̄)/√2 | 770 | 1⁻ |
| ω | (uū + dd̄)/√2 | 782 | 1⁻ |
| φ | ss̄ | 1020 | 1⁻ |

In MaSt: mesons are 2-component compounds T(m, n) + T(m', n') on the proton sheet (or related sheet). Specifically, for a meson with content qq̄, the natural identification is:
- q = T(m, n) (some primitive)
- q̄ = T(−m, −n) (full sign-reflection — the antiparticle)
- Meson = T(m, n) + T(−m, −n) → summed winding (0, 0)

But (0, 0) summed winding gives naive dispersion mass zero, not 140 MeV. So the meson's mass must come from something other than naive dispersion. Two candidates:

- **Internal phase / relative orientation** between the q and q̄ components contributes energy.
- **The (0, 0) summed winding gives zero rest energy at tree level**, but second-order effects (binding energy, sheet anisotropy, σ_uw shear) lift the mass. This is structurally similar to QCD's chiral-symmetry-breaking mechanism for the pion.

---

## 2. The structural setup

Under R64's quark assignment:
- u = T(1, +2)
- d = T(1, −2)
- ū = T(−1, −2)
- d̄ = T(−1, +2)

Then:
- π⁻ = dū = T(1, −2) + T(−1, −2) → summed (0, −4)
- π⁺ = ud̄ = T(1, +2) + T(−1, +2) → summed (0, +4)
- π⁰ ≈ (uū − dd̄)/√2: each term has summed winding (0, 0), but the linear combination has internal structure.
- ρ⁰ ≈ (uū − dd̄)/√2 with spin-1: same content as π⁰ but different spin state, suggesting different relative-phase structure.

So the meson winding numbers under R64's assignment are:
- π⁺, π⁻ at (0, ±4)
- π⁰, ρ⁰, ω, η at (0, 0) (linear combinations of (uū) and (dd̄) terms)

Mass dispersion at (0, ±4) and (0, 0) using R64 proton-sheet parameters (ε = 0.073, s = 0.194):

| (n_t, n_r) | μ² formula | μ² value | μ |
|---|---|---|---|
| (0, +4) | 0² + (4 − 0)² = 16 | 16 | 4 |
| (0, −4) | 0² + (−4 − 0)² = 16 | 16 | 4 |
| (0, 0) | 0² + 0² = 0 | 0 | 0 |

μ = 4 in framework units, where μ_proton ≈ 41 ≈ 938 MeV. So μ = 4 maps to ≈ 92 MeV. The observed π⁺ mass is 140 MeV — about 50% off but in the ballpark.

For π⁰ at (0, 0): predicted mass 0, but observed 135 MeV. The naive dispersion gives zero; the structural mechanism for the observed pion mass is what this file needs to identify.

---

## 3. Key questions

1. **Why is the pion's mass ~140 MeV rather than zero?** The (0, ±4) summed winding gives ~92 MeV in the naive dispersion — not 140 MeV. The (0, 0) summed winding gives zero. What's the missing physics?

   Candidates:
   - σ_uw shear effects (the shear term in the dispersion contributes to mixed-component compounds in ways not captured by naive summed-winding dispersion)
   - Binding energy between the q and q̄ components
   - Chiral-symmetry-breaking analog (Goldstone-boson-like mass)
   - Compound stress-energy effects (per [mass-from-cancellation.md](../../metric-binding/work/mass-from-cancellation.md), the surviving stress-energy after partial cancellations might not disperse at summed winding)

2. **Why is the kaon ~500 MeV?** Kaons contain strangeness — they have a strange quark or antiquark. In MaSt this would require a third "flavor" beyond u and d, possibly on a different sheet or with different (m, n) windings. The strange quark might be T(1, +3) or similar. What MaSt primitive accounts for strangeness?

3. **Why does the η differ from the π⁰ if they have similar quark content?** Both involve uū and dd̄ mixtures. The η also has a strange component. The mass split (η at 548 vs π⁰ at 135) is large. What structural difference produces it?

4. **Why are vector mesons (ρ, ω, φ) much heavier than pseudoscalar mesons (π, K, η)?** In QCD: spin-spin interactions of constituent quarks. In MaSt: the spin-1 vs spin-0 difference would come from how the two compound components couple their angular momenta. Need to formalize.

5. **What's the structural difference between π, η, K?** In QCD: flavor content (which quarks). In MaSt: which primitives appear in the compound.

---

## 4. Identification attempt

Tentative assignments to test:

| Meson | qq̄ in MaSt | Summed winding | Naive μ | Predicted mass | Observed |
|---|---|---|---|---|---|
| π⁺ | T(1,+2) + T(−1,+2) | (0, +4) | 4 | ~92 MeV | 140 |
| π⁻ | T(1,−2) + T(−1,−2) | (0, −4) | 4 | ~92 MeV | 140 |
| π⁰ | (uū − dd̄)/√2 | (0, 0) — mixed | 0 (naive) | 0 (naive); needs mechanism | 135 |
| K⁺ | T(1,+2) + T(−1,+3)? | depends on s-quark assignment | ? | ? | 494 |
| ρ⁺ | spin-flipped π⁺ | (0, +4) | 4 | 92 (same as π⁺) | 770 |

**Concerns:**
- Naive mass predictions are 30–50% low for π and way off for ρ.
- The structural mechanism for π⁰'s mass (lifting from zero) is unknown.
- The strange quark's MaSt identification is unclear.
- Spin-0 vs spin-1 mass splittings aren't captured.

So this identification is **a starting point, not a final answer**. The naive dispersion gets the ballpark for charged pions but misses by significant factors for everything else.

---

## 5. What needs to be added

For the framework to predict the meson spectrum, several pieces are missing:

1. **The pion-mass-from-zero mechanism.** What lifts the (0, 0) compound from zero mass to ~140 MeV? Candidate: chiral-symmetry-breaking analog in MaSt's geometric language. See [strong.md §2 step 2a](strong.md) for related framing.

2. **Strangeness assignment.** Which MaSt primitive is the s quark? Possibilities:
   - T(1, +3) on the proton sheet (heavier than T(1, +2) = u quark)
   - Mode on a different sheet (the existing R-track structure has multiple sheets)
   - **TODO:** examine R-track studies for evidence on strangeness assignment.

3. **Spin coupling in compounds.** How does the 2-component compound's spin emerge from the constituent spins? For a single primitive, spin presumably comes from the wave's internal structure. For a 2-component compound: relative orientation of the constituents. Need formalization.

4. **Compound binding energy.** How much energy is needed to bind two primitives into a compound? This affects both meson and baryon masses. Connects to [mass-from-cancellation.md](../../metric-binding/work/mass-from-cancellation.md) and [strong.md](strong.md).

---

## 6. Computational plan

1. **Compute naive dispersion masses for all light mesons.** Under R64 parameters, compute μ for all qq̄ summed windings. Compare to observed masses. Establish where naive dispersion fits and where it doesn't.

2. **Investigate σ_uw correction to meson masses.** R64's proton-sheet shear s_p = 0.194 contributes a cross-term to the dispersion. For zero-summed-winding compounds, the shear might lift mass from zero via the n_r · n_t term. **TODO:** compute this.

3. **Try strangeness as T(1, +3).** Compute kaon mass under this assignment. Compare to 494 MeV.

4. **Look for the pion-mass mechanism.** Try several candidates (chiral-symmetry-breaking, binding-energy, compound stress-energy) and see if any gives 140 MeV from MaSt's geometric inputs.

---

## 7. Cross-references

- [strong.md](strong.md) — uses the pion as mediator; meson-spectrum work is the structural backing
- [quark-flavor.md](quark-flavor.md) — which quark mapping is used affects the meson winding numbers
- [mass-from-cancellation.md](../../metric-binding/work/mass-from-cancellation.md) — mass mechanism for compounds
- [metric-charge chapter 8](../../metric-charge/08-shear-and-fractional-charge.md) — σ_uw shear effects on compound states
- [R53](../../../studies/R53-three-generations/) — three-generation structure, relevant for s, c, b assignments
- [R64](../../../studies/R64-nuclear-harmonic-stack/) — proton-sheet (ε, s) parameters

## 8. Next actions

1. Compute naive dispersion masses for all light mesons under R64 parameters.
2. Test whether σ_uw shear lifts (0, 0) compounds from zero mass to observed values.
3. Frame the strangeness assignment question; either commit to T(1, +3) or examine alternatives.
4. Identify whether the spin-0 vs spin-1 splitting can come from relative-phase structure in the 2-component compound.

---

## 9. Relationship to the clover substrate

[clover-quarks.md](clover-quarks.md) and [clover-mass.md](clover-mass.md) have developed an alternative proton-sheet geometry — a corrugated 3-lobed torus — that derives fractional charges and Z₃ confinement from cross-section geometry rather than from tuned (m, n) windings. The clover work has been carried far enough to make falsifiable mass predictions for baryons; for mesons it is not yet developed. This section records what's known about meson-clover compatibility.

### 9.1 Antiquark = sign-flipped wave-mode (matter/antimatter still works)

Per [quark-flavor.md Mapping Clover](quark-flavor.md), the mass formula μ²(n, m) = (n − 2m/3)² + (m/ε)² on the clover surface satisfies

μ²(−n, −m) = μ²(n, m)

so (n, m) and (−n, −m) are degenerate — same mass, opposite (k_θ, k_φ). This is exactly the matter/antimatter pairing structure. **q̄ = the sign-flipped wave-mode partner of q on the same corrugated surface.**

### 9.2 qq̄ compounds sum to (0, 0)

A meson built from q = (n, m) and q̄ = (−n, −m) has summed winding (0, 0) on the clover, identically to the round-tube case. Naive μ² = 0 from the zeroth-order formula. So the **pion-mass-from-zero question is structurally identical** in both substrates — the candidates in §3 (σ_uw shear, binding energy, chiral-symmetry-breaking analog, compound stress-energy) apply equally to either.

### 9.3 Open: what does the clover Hilbert space look like for qq̄?

The clover baryon picture identifies particles with wave-modes of a single corrugated torus. For mesons, three different physical pictures remain possible:

- **(M-a)** Mesons live on the same corrugated torus as baryons, but as different mode configurations (e.g., a wave that samples lobe + adjacent saddle in a particular phase relationship → a "qq̄ internal pair"). The naive dispersion mass would be computed by the same Hill equation but for these specific configurations.
- **(M-b)** Mesons live on a *different surface* — perhaps the round tube or a torus with different twist τ. In that case the work in §§1–8 of this file is the right framework, independent of clover.
- **(M-c)** Mesons are excited modes of the proton sheet whose collective behaviour mimics a "qq̄ compound" without being separable into two distinct constituents. Then "qq̄" is a useful but misleading language.

These are not yet distinguished. The first concrete test would be to compute the qq̄-like mode spectrum on the clover surface and compare to observed pion mass. **Not done.**

### 9.4 Open: spin-0 vs spin-1 splittings under clover

The clover work has not addressed angular momentum / spin structure of the wave modes. The pseudoscalar vs vector splittings (π vs ρ, etc.) need a spin assignment which clover-quarks.md and clover-mass.md do not currently provide.
