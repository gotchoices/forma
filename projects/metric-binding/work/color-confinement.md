# color-confinement.md — Z₃ confinement as structural

**Status:** Exploratory work file. Targets the structural origin of the Z₃ confinement that gives baryons exactly 3 constituents and mesons exactly 2. Sister to [fractional-charge.md](fractional-charge.md) and [quark-flavor.md](../../sheet-proton/work/quark-flavor.md).

**Tone:** Deepest of the work files. The Z₃ confinement is a profound feature of QCD; deriving it from MaSt geometry would be a substantial theoretical contribution. Even partial progress is valuable.

---

## 1. The question

QCD's Z₃ structure (color triality) is one of its deepest features:
- Baryons have exactly 3 quarks (color singlets via SU(3)_c)
- Mesons have exactly 2 quarks (color singlets via 3 ⊗ 3̄)
- Exotic states (4q, 5q, qqg, etc.) exist but are rarer
- Free quarks don't exist (confinement)

In QCD this comes from SU(3) color gauge symmetry: gauge-singlet combinations require specific color compositions. The Z₃ center of SU(3) governs the allowed multiplicities.

In MaSt: the Z₃ structure shows up empirically (R60 Track 16 derives Z₃ confinement on the proton sheet; R64 fits baryons as 3-quark composites). But the structural reason — *why* three rather than two or seven — is not derived; it's read off from QCD.

**The question:** Can MaSt's geometry produce the Z₃ structure intrinsically, without borrowing SU(3) from QCD?

---

## 2. Why this matters

If MaSt can derive Z₃ confinement structurally:
- It explains *why* baryons are three-quark and mesons are qq̄
- It explains *why* fractional charges (per [fractional-charge.md](fractional-charge.md)) come in thirds specifically
- It strengthens the entire framework — Z₃ is one of QCD's most empirically confirmed features
- It distinguishes the framework from "just relabeling QCD with new vocabulary"

If MaSt *cannot* derive Z₃ structurally:
- The framework imports Z₃ as an empirical input (like α)
- The "wave-only, derived-from-geometry" promise is partial
- The Z₃ structure remains a postulate

This is the project's most ambitious target. Even partial progress (e.g., showing 3 is *natural*, even if not forced) is valuable.

---

## 3. Candidate structural origins

### 3a. From the torus topology directly

T² = S¹ × S¹ has fundamental group π₁(T²) = ℤ × ℤ. The Z₃ structure isn't an obvious feature of this — ℤ doesn't have a special 3. Some candidate paths:

- **Three-fold symmetry of a specific knot class.** Trefoil knots T(2, 3) have three-fold symmetry. Could the proton's wrap geometry pick out trefoils specifically? The closure rule of [chapter 4](../../metric-charge/04-the-closure-condition.md) rules out T(2, 3) as a closure-satisfying primitive (gcd(2,3)=1, so it's a "genuine torus knot" that fails closure). But the *multi-component* T(3, 3n') = 3 × T(1, n') is closure-satisfying.
  
  So the natural closure-satisfying multi-link at gcd = 3 is the 3-component link. Why three? Because that's where closure first allows non-trivial multi-components on T². The closure rule "m divides n" plus the requirement that components be primitives (gcd = 1) creates a hierarchy where 1-component is single-primitive and 2-component is the simplest multi-link with k = 2.

  **TODO:** Is there a structural reason that 3 is special among 2, 3, 4, ...? Or is 3 just one option among many that QCD happens to pick?

### 3b. From the framework's mode spectrum

If the proton-sheet mode spectrum has a natural 3-fold structure (e.g., a triply-degenerate set of primitive modes), then bound states with three constituents are favored. Possible mechanisms:
- σ_uw shear has a 3-cycle symmetry at specific (ε, s) values
- The sheet's harmonic spectrum has a natural three-fold gap

**TODO:** examine the proton-sheet mode spectrum at R64 parameters for triple-degeneracy structure. Look for resonances at multiples of 3.

### 3c. From the σ_uw shear coupling

The shear σ_uw mixes the two compact directions and breaks symmetries (per [metric-charge chapter 6](../../metric-charge/06-handedness-and-pairs.md)). Could it produce a Z₃ structure as a remnant symmetry of the broken metric?

This is structurally analogous to QCD's SU(3) color: the unbroken symmetry of QCD has SU(3) as one factor; here, an emergent residual symmetry might be Z₃ after shear breaks a higher symmetry.

**TODO:** examine the symmetry group of the proton-sheet metric (with σ_uw ≠ 0). What discrete subgroups remain?

### 3d. From the constraint that compounds must be net-neutral under closure

A compound on T² must satisfy a net-charge-closure condition. If the framework's per-primitive charge unit is *not* an integer of the observed electron charge, then closure requires *multiple* primitives to combine before the net charge becomes integer-observable. Specifically:
- If each primitive has "internal charge" 1/3 of an observable unit, then three primitives are required to close to an integer.
- The "1/3" comes from the structural relation between MaSt primitive winding and observable charge.
- The "three" is then forced.

This is the natural complement to [fractional-charge.md](fractional-charge.md). The Z₃ structure and the fractional-charge structure are two views of the same fact: the framework's "atomic" charge unit is 1/3 of the observable unit, and three primitives are needed to satisfy integer-charge closure.

**TODO:** verify that R64's per-primitive charge attribution f(n_pt, n_pr) = n_pt/6 + n_pr/4 (the A1 charge attribution) is consistent with this picture. Does it give 1/3-units in some natural normalization?

---

## 4. Connections to other work files

- [fractional-charge.md](fractional-charge.md) — fractional charges and Z₃ confinement are the same fact. Decisive progress on one likely yields the other.
- [quark-flavor.md](../../sheet-proton/work/quark-flavor.md) — the (m, n) assignments depend on whether Z₃ structure is fundamental or emergent.
- [mass-from-cancellation.md](mass-from-cancellation.md) — the cancellation mechanism for compound masses presumes a specific composite structure; Z₃ tells us why three components.

---

## 5. Key questions

1. **Is 3 special in MaSt's torus geometry?** The closure rule "m divides n" doesn't single out 3. The mode spectrum at typical (ε, s) doesn't single out 3 either. Where does 3 come from structurally?

2. **Why don't bosons require Z₃?** Mesons are 2-component compounds (qq̄), satisfying closure with 2 components. Why is 2 enough for mesons but 3 required for baryons?

   Answer in QCD: bosons are color-singlet via 3 ⊗ 3̄ = 1 ⊕ 8 (the singlet is the bound meson); baryons are color-singlet via 3 ⊗ 3 ⊗ 3 = 1 ⊕ ... (the singlet is the bound baryon). Both are SU(3) singlets, but the multiplicities differ.

   Answer in MaSt: meson = q + q̄ (particle + antiparticle) → net summed winding (0, 0), so net "charge" is zero. Baryon = three primitives → net summed winding (3, ±2) at R64. **TODO:** examine why mesons are 2 and baryons are 3 in the closure-decomposition language. Both must give integer-net-winding compounds.

3. **What's the spin statistics?** Baryons are fermions (spin-1/2 from 3 quarks); mesons are bosons (spin-0 or spin-1 from qq̄). The Z₃ structure has to be compatible with the spin assignment.

4. **Exotic states.** QCD predicts tetraquarks (qq̄qq̄), pentaquarks (qqqqq̄), glueballs (gg). Some have been observed. Does MaSt naturally predict these as higher-component composites? Are their predicted masses and structures consistent?

---

## 6. Computational plan

Difficult to make concrete without choosing a candidate structural origin. Tentative plan:

1. **Test 3a (closure-rule path).** Catalog all 2-component, 3-component, 4-component, ... closure-satisfying multi-links on T². Which counts of components have natural compound-mode structures? Is 3 special?

2. **Test 3b (mode spectrum path).** Compute mode spectrum at R64 parameters and look for triple-degenerate structures.

3. **Test 3c (residual symmetry path).** Compute the proton-sheet metric's symmetry group at R64 (ε, s). Identify discrete subgroups; look for Z₃.

4. **Test 3d (fractional-charge path).** Verify that A1 charge attribution gives 1/3-fractional units; check whether this forces three-component closure.

---

## 7. Cross-references

- [metric-charge chapter 4](../../metric-charge/04-the-closure-condition.md) — closure rule
- [metric-charge chapter 6](../../metric-charge/06-handedness-and-pairs.md) — handedness and symmetry breaking
- [R60 Track 16](../../../studies/R60-metric-11/findings-16.md) — Z₃ derivation in R60
- [R64](../../../studies/R64-nuclear-harmonic-stack/) — empirical baryon structure
- [primers/gauge-primer.md](../../../primers/gauge-primer.md) — gauge theory vocabulary
- [fractional-charge.md](fractional-charge.md) — partial-knot picture is the natural complement
- [quark-flavor.md](../../sheet-proton/work/quark-flavor.md) — flavor assignment depends on Z₃ structure

## 8. Next actions

1. Pick one candidate origin (3a-3d) and develop it concretely.
2. Test against R60 Track 16's existing Z₃ derivation — what mechanism did that use?
3. Check whether progress here feeds [fractional-charge.md](fractional-charge.md) or vice versa.
