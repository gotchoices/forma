# quark-flavor.md — quark structure as canceling primitives

**Status:** Exploratory work file. Captures candidate mappings between Standard Model quarks (u, d, s, c, b, t — though this file focuses on u and d) and MaSt primitives on the proton sheet. Sister to [strong.md](strong.md) and [mass-from-cancellation.md](../../metric-binding/work/mass-from-cancellation.md).

**Tone:** Catalog candidate mappings, evaluate against observables, mark which match and which don't.

---

## 1. The question

Standard Model: proton is uud, neutron is udd. The u and d quarks have charges +2/3 and −1/3 and masses ~2.2 MeV and ~4.8 MeV. They differ in flavor (isospin), in charge, and in mass slightly.

MaSt: particles are knots/compounds on the proton sheet, labeled by (m, n) winding pairs. What (m, n) assignments to u and d give the right proton (uud) and neutron (udd) structure?

R64's current empirical fit: u = T(1, +2), d = T(1, −2). Both have m = +1 (positive matter); flavor is encoded in the sign of n. Proton = (1, +2) + (1, +2) + (1, −2) → composite (3, +2).

Alternative hypothesis (user's): u = T(1, +2), d = T(−1, +2). The m-sign is flipped (not the n-sign). Proton = (1, +2) + (1, +2) + (−1, +2) → composite (1, +6).

Both give net charge consistent with proton +1 (under different conventions). They differ in structural interpretation. This work file catalogs candidate mappings and tests which holds up.

---

## 2. Candidate mappings

For each mapping, list:
- u quark assignment
- d quark assignment
- Proton composite (uud) and net winding
- Neutron composite (udd) and net winding
- Whether it's closure-satisfying as a compound
- Structural interpretation of u vs d

### Mapping R64 (current): n-flipped flavor

| Particle | (m, n) | Comment |
|---|---|---|
| u | (1, +2) | matter, "+chirality" |
| d | (1, −2) | matter, "−chirality" |
| ū | (−1, −2) | antimatter of u |
| d̄ | (−1, +2) | antimatter of d |
| Proton uud | (1,+2) + (1,+2) + (1,−2) | composite (3, +2) |
| Neutron udd | (1,+2) + (1,−2) + (1,−2) | composite (3, −2) |

**Structural interpretation:** u and d are both matter (positive m). Flavor = sign of n-winding direction. The n-difference distinguishes u from d at the same charge-sign level.

**Closure:** k × T(1, n') uniform multi-link doesn't apply (the three components aren't identical). Mixed-flavor compound; chapter 4 doesn't currently certify but R64 treats as valid via Z₃ confinement.

### Mapping User-1: m-flipped flavor

| Particle | (m, n) | Comment |
|---|---|---|
| u | (1, +2) | matter, "+charge" |
| d | (−1, +2) | partial m-mirror of u |
| Proton uud | (1,+2) + (1,+2) + (−1,+2) | composite (1, +6) |
| Neutron udd | (1,+2) + (−1,+2) + (−1,+2) | composite (−1, +6) |

**Structural interpretation:** Flavor is encoded in m-sign. d-quark is the m-mirror of u-quark (same chirality, opposite charge direction).

**Concerns:**
- (1, +2) + (−1, +2) is matter + partial-antimatter pair (the (-m, n) sibling). Should they annihilate or coexist? Per metric-mass chapter 5: ±n components in a standing wave coexist (they're not antimatter); but ±m might be different. **TODO:** check whether (m,n) → (−m,n) is annihilation-related or coexistence-compatible.
- The neutron's composite (−1, +6) has *negative* m, suggesting it's "anti-matter-like" net. But neutron is matter. Structural mismatch.

### Mapping User-2: doubly-flipped antimatter analog

| Particle | (m, n) | Comment |
|---|---|---|
| u | (1, +2) | matter |
| d | (−1, −2) | full antimatter sign-flip |
| Proton uud | (1,+2) + (1,+2) + (−1,−2) | composite (1, +2) |

**Concern:** d = full antiparticle of u? That's just an antiquark in standard model language; can't be the d quark which is matter.

This mapping fails the "d is matter" check.

### Mapping Alternative-3: independent primitives

| Particle | (m, n) | Comment |
|---|---|---|
| u | T(1, +2) | one primitive in the inventory |
| d | T(1, +3) | a different primitive in the inventory |
| Proton uud | (1,+2) + (1,+2) + (1,+3) | composite (3, +7) |

**Structural interpretation:** u and d are entirely different primitives, no sign-flip relationship. Flavor = which primitive.

**Concerns:**
- Doesn't naturally give u/d as "near-identical" (their masses are very close in SM, differing by ~3 MeV).
- The proton (3, +7) mass would be different from R64's (3, +2) fit.

---

## 3. Tests to apply

For each mapping, check:

1. **Net charge prediction.** Sum the m-windings or apply the framework's charge formula. Compare to proton +1, neutron 0.

2. **Composite mass prediction.** Plug into the dispersion μ²(n_t, n_r) at R64 parameters. Does it give 938 MeV (proton) and 939.5 MeV (neutron)?

3. **Mass split prediction.** m_n − m_p = 1.293 MeV experimentally. Does the mapping reproduce this?

4. **Closure compatibility.** Is the compound closure-satisfying under metric-charge chapter 4 (or an appropriate extension)?

5. **Structural-coherence with R64.** R64 has done extensive empirical work pinning u/d to (1,±2). Does the alternative mapping require revising that, or can it coexist as a relabeling?

6. **Decay pathway.** Neutron decay n → p + e⁻ + ν̄. Under each mapping, what does the decay look like as a structural decomposition? Does (1,+2) → (1,+2) work? Or (−1,+2) → (1,+2) + (e⁻ + ν̄ accounting)? Or something else?

7. **Antiparticle prediction.** Antiproton p̄ = ūūd̄ should have charge −1 and the correct mass. Sign-flips must be consistent.

8. **Magnetic moment prediction.** Proton μ_p = +2.793 μ_N, neutron μ_n = −1.913 μ_N. Naive constituent-quark prediction: μ_p ≈ +3, μ_n ≈ −2 in nuclear magnetons. Does the mapping reproduce this with correct signs?

---

## 4. Open structural questions

- **Is m-sign or n-sign the flavor coordinate?** Equivalent: does flavor correspond to chirality reflection (n-sign) or charge-direction reflection (m-sign)? The empirical pattern of QCD's isospin should match one of these specifically.

- **What's the structural difference between (m, n) and (−m, n)?** [metric-charge chapter 6](../../metric-charge/06-handedness-and-pairs.md) discusses handedness pairs. If (1, +2) and (−1, +2) are handedness-flipped versions of the same particle, they're different from "matter and antimatter." But they're also not the same particle. What are they?

- **Why three components?** Whatever the (m, n) assignment, baryons in QCD have exactly three constituents. The Z₃ confinement structure is what enforces this. Is the choice of (m, n) assignment compatible with Z₃ confinement? See [color-confinement.md](../../metric-binding/work/color-confinement.md).

- **How does this affect strong.md's mediator search?** The pion (a qq̄ compound) depends on which quark mapping is right. R64 mapping: pion = (1, +2) + (−1, −2) → (0, 0) compound. User-1 mapping: pion = (1, +2) + (−1, −2) → also (0, 0). Same form but different physical interpretation of the components.

---

## 5. Computational plan

Scripts to write:

1. `quark-mapping-spectrum.py` — for each candidate mapping, compute the predicted mass of the proton (uud) and neutron (udd) composites under R64's dispersion. Output a table of (mapping, predicted_p_mass, predicted_n_mass, observed_p, observed_n, mass_split).

2. `quark-mapping-decay.py` — for each candidate mapping, compute the structural decomposition of neutron β-decay n → p + e⁻ + ν̄. Identify which components flip, what changes, and whether the decay is structurally clean.

3. `quark-mapping-antiparticle.py` — verify antiparticle predictions for each mapping. p̄ should have charge −1 and mass ≈ proton mass. Antineutron similarly.

4. `quark-mapping-magnetic-moment.py` — naive constituent-quark moment calculation for each mapping. Predict proton and neutron magnetic moments; compare to observed.

---

## 6. Next actions

1. Implement `quark-mapping-spectrum.py` and run all four candidate mappings.
2. Rank mappings by empirical match (mass + mass split).
3. Check closure compatibility of the top-ranked mapping(s).
4. Feed result into [strong.md](strong.md) (mediator structure depends on quark mapping) and [meson-spectrum.md](meson-spectrum.md) (meson masses depend on qq̄ composition).

---

## 7. Cross-references

- [metric-charge chapter 4](../../metric-charge/04-the-closure-condition.md) — closure rule (currently restricted to uniform k × T(1, n'))
- [metric-charge chapter 6](../../metric-charge/06-handedness-and-pairs.md) — handedness pairs
- [R64](../../../studies/R64-nuclear-harmonic-stack/) — empirical fit u = (1, +2), d = (1, −2)
- [R53](../../../studies/R53-three-generations/) — three-generation structure (relevant if mapping extends to s, c, b, t)
- [strong.md](strong.md) — mediator structure depends on quark mapping
- [mass-from-cancellation.md](../../metric-binding/work/mass-from-cancellation.md) — mass mechanism under each mapping
