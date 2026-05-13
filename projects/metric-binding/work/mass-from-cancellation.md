# mass-from-cancellation.md — mass from residual full-ring terms

**Status:** Exploratory work file. Captures the hypothesis that composite-particle mass emerges from the *residual* (un-cancelled) full-ring components of a multi-knot compound after partial-turn cancellations between constituents. Sister to [quark-flavor.md](../../sheet-proton/work/quark-flavor.md), [fractional-charge.md](fractional-charge.md), [strong.md](../../sheet-proton/work/strong.md).

**Tone:** Exploratory. Connects the standing-wave reading (chapter 5 of metric-mass) to the multi-component closure picture (chapter 4 of metric-charge).

---

## 1. The question

Composite-particle masses in QCD have a peculiar feature: most of the proton's mass (~938 MeV) is *not* from the constituent quark rest masses (sum ~10 MeV) — it's from the QCD binding energy / gluon dynamics. The naive picture "mass = sum of constituent masses" fails by two orders of magnitude.

In MaSt the question becomes: if a proton is a compound of three primitives, what mathematical operation gives its observed mass? Two extreme readings:

- **Additive:** mass(composite) = sum of constituent dispersion masses. Predicts proton mass = 3 × (mass of a single primitive). Doesn't match the harmonic-stack picture R64 uses.
- **Composite-dispersion:** mass(composite) = dispersion evaluated at summed windings. R64's reading: mass(3, +2) is computed from the dispersion at (n_t = 3, n_r = 2), not from three separate (1, ±2) masses. This works empirically but doesn't have a clear structural reason.

The hypothesis here: **the composite mass is what's left after partial-turn cancellations between constituents**. Specifically:

- Each primitive carries certain "internal" structure (partial turns, oscillation phases).
- When primitives combine in a compound, components of the internal structure cancel pairwise (the partial-turn cancellation analogous to the n-linear cross-term cancellation in metric-mass chapter 5).
- The components that survive cancellation are the "full-ring" components — the ones that wrap fully around the compact direction.
- The full-ring components dispersively combine according to summed windings.
- The resulting composite mass is the dispersion at the *summed-winding* signature, with cancelled components contributing nothing.

Under this hypothesis, R64's empirical formula μ²(n_t = 3, n_r = 2) for the proton is the result of: three (1, ±2) primitives have their "partial" contributions cancel, leaving only the full-ring (3, +2) signature to dispersively contribute.

---

## 2. Connection to existing cancellation results

The framework already has *one* cancellation result: [metric-mass chapter 5 §7](../../metric-mass/05-metric-self-consistency.md). There, the ±n superposition of a standing wave makes the n-linear cross-terms of the stress-energy cancel exactly:

- T_tu and T_Su (which depend linearly on n) cancel between +n and −n components
- T_tt, T_SS, T_uu (which depend on n²) double instead of cancel
- T_tS (which doesn't depend on n) doubles too

The cancellation is *structural*, not a coincidence: it arises because the +n and −n components have opposite "compact-direction currents" that algebraically cancel in the sum.

This is the prototype for the more general mechanism. The hypothesis is that *the same kind of cancellation* applies to multi-component compounds:

- Each component has a "current"-like part and a "magnitude"-like part (in some basis decomposition)
- Currents cancel pairwise across components with opposite signs
- Magnitudes don't cancel; they combine according to composite-dispersion rules
- The composite mass = dispersion of the un-cancelled magnitudes

What's "current-like" and what's "magnitude-like" in a multi-component compound is what this work file needs to formalize.

---

## 3. The structural setup

For a compound of multiple primitives {T(m_i, n_i)} with summed windings (M, N) = (Σm_i, Σn_i):

The composite's stress-energy is a sum over all single-component contributions plus cross-terms between different components:

<!-- T_total = Σ_i T_ii + Σ_{i≠j} T_ij -->
$$
T_{\mathrm{total}} \;=\; \sum_i T_{ii} \;+\; \sum_{i \neq j} T_{ij}
$$

For the standing-wave (±n) compound, the cross-terms T_ij either vanish (for n-linear entries) or contribute (for n-zero entries). The general question: for a 3-component compound with primitives (m_1, n_1), (m_2, n_2), (m_3, n_3), which T_ij cross-terms vanish, and which contribute?

**Conjectured rule:** T_ij vanishes when (m_i + m_j, n_i + n_j) summed-winding component is "purely directional" — i.e., it's an antisymmetric combination that integrates to zero over the compact direction. T_ij survives when it's "purely magnitudinal" — symmetric, doesn't integrate to zero.

This is exactly the n-linear vs n-quadratic distinction of metric-mass chapter 5 §7, generalized to multi-component compounds with mixed (m, n) windings.

**TODO:** formalize this conjecture. What's the algebraic criterion for T_ij to vanish vs survive?

---

## 4. Worked example: the proton at R64 (3, +2)

R64's proton fit: three primitives (1, +2), (1, +2), (1, −2). Composite winding (3, +2).

Stress-energy contributions to evaluate:

| Term | Origin | n-structure | Cancels? |
|---|---|---|---|
| T_11 | self of first (1,+2) | quadratic in (1,+2) | No |
| T_22 | self of second (1,+2) | quadratic in (1,+2) | No |
| T_33 | self of (1,−2) | quadratic in (1,−2) | No (but with sign-flipped n) |
| T_12 | cross of two (1,+2)'s | symmetric in n=+2 | No |
| T_13 | cross of (1,+2) and (1,−2) | linear in n=2 (because n's differ by 4) | Cancels? |
| T_23 | cross of (1,+2) and (1,−2) | same as T_13 | Cancels? |

If T_13 and T_23 cancel (because they have linear-in-n components with opposite signs from the (1,±2) pair structure), then the surviving stress-energy is T_11 + T_22 + T_33 + T_12 — three "magnitude" terms plus one cross-term between the matching pair.

This gives a residual stress-energy whose dispersion is *not* simply the sum of three primitive masses, but is some composite that depends on the surviving components only. Under summed-winding (3, +2), if the surviving components dispersively combine as μ²(3, +2), then R64's empirical formula falls out.

**TODO:** verify this computation explicitly. Compute T_12, T_13, T_23 for the specific (1,+2)+(1,+2)+(1,−2) compound. Check whether T_13 and T_23 cancel and whether the surviving stress-energy gives μ²(3, +2).

---

## 5. Predictions to test

If the partial-turn cancellation mechanism is right, it should predict:

1. **For matching-flavor compounds (like 3 × (1,+2)):** all primitives identical, cross-terms don't have sign-flipped components, no cancellation. Mass should be dispersion at (3, 3·n').

2. **For mixed-flavor compounds (like (1,+2)+(1,+2)+(1,−2)):** the unmatched primitive has sign-flipped n cross-terms with each matched primitive. These cancel pairwise. Surviving mass is dispersion at summed winding (3, +2).

3. **For compounds with m-flips (like (1,+2)+(1,+2)+(−1,+2)):** m-linear cross-terms cancel between (1,+2) and (−1,+2). Surviving mass is dispersion at summed winding (1, +6). Different formula than (3, +2).

4. **For neutron (udd = (1,+2)+(1,−2)+(1,−2)):** by symmetry with proton, two cancellations (from the matching (1,−2) pair) and one surviving cross-term. Mass dispersion at (3, −2).

The proton-neutron mass split (m_n − m_p = 1.293 MeV) under this picture should come from the difference between μ²(3, +2) and μ²(3, −2) at the same proton-sheet parameters — exactly R64's reading.

So the hypothesis is *consistent* with R64's empirical formula, and gives a structural reason for *why* the formula has the form it does.

---

## 6. Key questions

1. **Is the n-linear cross-term cancellation of metric-mass chapter 5 §7 really the universal mechanism?** That chapter proved cancellation for 2-component (±n) standing waves on a 1D compact dimension. Generalizing to multi-component compounds on 2D T² requires checking that the analogous algebra works.

2. **What's the "current" vs "magnitude" decomposition for a multi-component compound?** In chapter 5 it was the n-linear vs n-quadratic split. For mixed-(m, n) compounds, it might be more complex — possibly an (m, n) → ((m+m'), (n+n')) cross-term structure.

3. **Does the surviving stress-energy actually disperse as μ²(M, N)?** This is the claim that needs verification. If the surviving terms dispersively combine differently (e.g., as a sum of contributions, or with some interference), the empirical R64 formula wouldn't fall out.

4. **How does this interact with the mass-vs-energy interpretation in the framework?** Mass in metric-mass is the rest-frame frequency of a standing wave. In a compound, multiple primitives contribute multiple frequencies. The dispersion at (M, N) gives one frequency. How does this single composite frequency emerge from multiple primitive frequencies?

---

## 7. Computational plan

1. **Stress-energy of 3-component compounds.** Compute T_total for the specific compound (1,+2) + (1,+2) + (1,−2). Identify which cross-terms vanish.

2. **Verify dispersion at composite winding.** Compute the dispersion μ²(3, +2) from R64 parameters and compare to the empirical proton mass. (R64 has already done this, but here we recompute under the cancellation hypothesis to verify the same formula applies.)

3. **Test the user's alternative.** Compute T_total for (1,+2) + (1,+2) + (−1,+2) per [quark-flavor.md](../../sheet-proton/work/quark-flavor.md)'s mapping. Check the surviving cross-terms and the dispersion at (1, +6).

4. **Compare predictions to observations.** Proton-neutron mass split, magnetic moments, charge structure under each cancellation pattern.

---

## 8. Cross-references

- [metric-mass chapter 5 §7](../../metric-mass/05-metric-self-consistency.md) — the prototype n-linear cancellation
- [metric-charge chapter 4](../../metric-charge/04-the-closure-condition.md) — multi-component compound decomposition
- [quark-flavor.md](../../sheet-proton/work/quark-flavor.md) — different quark mappings produce different cancellation patterns
- [fractional-charge.md](fractional-charge.md) — partial-knot picture is related; cancellation between partials might be the underlying mechanism
- [R64](../../../studies/R64-nuclear-harmonic-stack/) — empirical formula μ²(3, +2) for proton; this hypothesis is the structural reason
