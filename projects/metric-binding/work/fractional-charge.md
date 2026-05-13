# fractional-charge.md — fractional charge as partial knots

**Status:** Exploratory work file. Captures the hypothesis that fractional charges (the ±1/3, ±2/3 of quarks) emerge as a structural feature of *partial* knots — incomplete topological configurations that satisfy closure only when joined into a multi-component compound. Sister to [quark-flavor.md](../../sheet-proton/work/quark-flavor.md), [mass-from-cancellation.md](mass-from-cancellation.md), [color-confinement.md](color-confinement.md).

**Tone:** This is genuinely speculative — neither MaSt nor the Standard Model currently has a structural explanation for *why* quark charges are thirds. This file develops the candidate explanation rather than confirming it.

---

## 1. The question

The Standard Model treats quark charges (+2/3, −1/3) as primitive — they're just the values the theory inputs. There's no derivation of *why* the constituents come in thirds rather than halves or sevenths. The empirical fact that three quarks make integer-charge baryons constrains the constituents to have charges that are 1/3-fractions of integer values, but the constraint itself isn't derived.

MaSt's current state is similar: R64's empirical fit gives composite (3, +2) for the proton with three (1, ±2) constituents. The "3" in (3, +2) — both the m-sum and the Z₃ confinement number — is taken as input.

**Hypothesis:** Fractional charges are what *incomplete* knots carry. A closure-satisfying configuration on T² (a "full" knot) has integer winding numbers. A partial knot — a configuration that has not yet closed — carries fractional winding. When three partials combine into a full closed knot, their fractional windings sum to an integer.

Under this hypothesis:
- Quark charge fractions are structural, not free
- The "thirds" specifically come from the three-fold closure requirement (Z₃)
- Free quarks are forbidden (would be partial knots, which don't satisfy closure)
- Confinement = the requirement that partials only exist within full knots

This is essentially the standard QCD confinement story, but with a geometric mechanism (partial-knot topology) rather than a color-charge SU(3) mechanism.

---

## 2. The structural setup

Define a **partial knot** as a configuration on T² that:
- Has a definite winding direction (locally — like an arc on the torus surface)
- Does *not* satisfy the closure condition by itself (the arc has loose endpoints, or the winding doesn't return to itself after one circumnavigation)
- *Can* close when joined with other partials of compatible structure

By contrast, a **full knot** is a closure-satisfying configuration (closed curve on T² with co-prime winding numbers (1, n')).

The mathematical question: what's the right formalization of "partial knot"?

Candidate formalizations:

### 2a. Fractional winding numbers

Allow m and n to be rational rather than integer for partials:
- u quark: (m, n) = (1/3, 2/3) or (2/3, 2/3) or similar
- d quark: (m, n) = (−1/3, 2/3) or similar
- Three partials sum to integer (m, n)

**Mathematical concern:** Fractional winding on T² isn't well-defined topologically — winding numbers are integer-valued by definition. A configuration with "fractional winding" isn't a closed loop on T²; it's something else.

### 2b. Arc configurations with synchronized endpoints

A partial knot is an open arc on T² with definite endpoints. Three such arcs share endpoints pairwise, forming a closed three-fold link. The arc's winding "fraction" comes from how much of a full loop it traces between its endpoints.

**Geometric realization:** Like the seams of a baseball (three arcs joining at common points to form a closed boundary). The arcs themselves are partial — none closes on its own — but together they tile a closed boundary.

This is closer to MaSt's natural geometry. The Z₃ structure emerges from the three-arc topology.

### 2c. Sub-windings of a parent closure

A partial knot is a *segment* of a larger closed configuration. The full closure has (k·m, k·n) winding for some integer k; each partial has (m, n) (the gcd-reduced primitive) and there are k of them.

**Connection to chapter 4:** This is essentially metric-charge's existing decomposition rule! T(k·m', k·n') decomposes into k disjoint copies of T(m', n'). The k = 3 case is the baryon: three primitives that together form one (3·m', 3·n') composite.

But chapter 4 treats the k primitives as *separate* closure-satisfying objects (each is its own T(m', n')). The user's hypothesis goes further: each primitive is a *partial* knot that doesn't close by itself. The composite is the only closure-satisfying object.

The distinction:
- Chapter 4: 3 × T(1, n') = three independent closed knots stuck together
- This hypothesis: a single T(3, 3n') = (3, 3n') closure that decomposes into three pieces, none of which is independently closed

### 2d. Quasi-particles on a constrained sheet

Treat partials as collective excitations on the sheet that can't be excited individually, only in compatible triples. Like phonons in a crystal — there's no "1/3 phonon," but specific collective modes only exist as group excitations.

**Mathematical structure:** define a constraint subspace on the sheet's wave equation that allows only Z₃-symmetric configurations. Partials are eigenmodes of the constrained equation.

---

## 3. Key questions

1. **Which formalization works?** 2a (fractional winding) is mathematically problematic. 2b (arcs with synchronized endpoints) is geometrically clean. 2c (sub-windings of parent closure) connects most directly to chapter 4. 2d (constrained quasi-particles) is most flexible but least specific.

2. **Why specifically thirds?** All four formalizations give some kind of *3-fold* structure for baryons. Why three, rather than two or five or seven? This is the deepest question. Some candidates:
   - Topological: π₁(T²) = ℤ² has a natural Z₃ subgroup? (No, ℤ² has no special 3.)
   - Geometric: a closed loop on T² has a natural three-fold decomposition? (Not in general.)
   - Algebraic: some structure on the sheet picks out three? (Z₃ confinement in QCD comes from SU(3) gauge symmetry; the analog here is unclear.)
   - **TODO:** find a structural reason that's intrinsic to MaSt, not borrowed from SU(3).

3. **What about pairs?** Mesons are 2-component (qq̄). Are these "two partials make a closed loop"? That seems easier (you can close a loop with two arcs more naturally than with three). But the 2-component structure of mesons is bosonic, while baryon 3-component is fermionic. Does the partial-knot picture distinguish them?

4. **Are fractional charges observable in isolation?** In QCD: no — quark confinement forbids free quarks. In partial-knot picture: yes by structural argument — a partial knot doesn't satisfy closure and therefore can't exist as a standalone particle. Confinement is structurally automatic.

5. **What happens at high energy?** QCD's asymptotic freedom says the strong coupling weakens at high energy; quarks behave more like free particles in deep inelastic scattering. In partial-knot picture: does the constraint relax at high energy?

---

## 4. Tests against observation

Specific predictions to check:

| Observation | Standard Model | Partial-knot prediction |
|---|---|---|
| Free quarks exist? | No (confinement, postulated) | No (closure violation, structural) |
| Baryon = 3 quarks | Yes (by SU(3) color) | Yes (by closure decomposition) |
| Meson = qq̄ | Yes | Yes if 2-partial closure works |
| Charge quantization (integer composites) | Yes (by charge conservation + Q ∝ 1/3) | Yes (by integer composite winding) |
| Exotic states (tetraquarks, pentaquarks) | Predicted by QCD; observed | Should fall out of 4-component and 5-component closures |
| Asymptotic freedom | Confirmed (DIS, jet physics) | Not yet predicted |

---

## 5. Computational plan

Difficult to make this concrete without choosing a formalization. Tentative steps:

1. **Choose a formalization.** 2c (sub-windings of parent closure) is the most computable. Adopt provisionally; revisit later.

2. **Map quark charges to sub-winding components.** Under 2c, the proton's composite (3, +2) decomposes into 3 × T(1, 2/3)? Or 3 × T(1, 2) where the *external* charge is per-component-times-1/3? Need to formalize what "fractional charge" means in MaSt language.

3. **Check Z₃ confinement.** Does the framework forbid free partials? Specifically: is there a closure-violation penalty that scales with isolation distance?

4. **Test exotic states.** Predict masses for 4-component and 5-component composites. Compare to observed tetraquark and pentaquark masses.

---

## 6. Open structural concerns

- **Mathematical rigor of "partial knot".** Need to choose a formalization that's both physically meaningful and mathematically well-defined. None of 2a-2d is fully developed.
- **Why three specifically?** The deepest question. Without a structural answer, the framework is reframing QCD's empirical Z₃ structure rather than deriving it.
- **Interaction with quark-flavor work.** Per [quark-flavor.md](../../sheet-proton/work/quark-flavor.md), the (m, n) labels for u and d affect the partial-knot decomposition. The two files have to converge on a consistent assignment.
- **Interaction with confinement work.** Per [color-confinement.md](color-confinement.md), the Z₃ structure of baryons should be derived from the framework rather than postulated. Partial knots and Z₃ confinement are the same question from different angles.

---

## 7. Next actions

1. Choose a formalization (2c is the most computable starting point).
2. Formalize "partial charge" mathematically — what does it mean for an arc on T² to carry fractional winding?
3. Verify the chapter-4 decomposition T(3, 3n') = 3 × T(1, n') matches the partial-knot picture.
4. Test the formalization against the proton/neutron mass predictions of [quark-flavor.md](../../sheet-proton/work/quark-flavor.md).

---

## 8. Cross-references

- [metric-charge chapter 4](../../metric-charge/04-the-closure-condition.md) — closure decomposition T(k·m', k·n') = k × T(m', n')
- [metric-charge chapter 8](../../metric-charge/08-shear-and-fractional-charge.md) — existing treatment of fractional charge in metric-charge
- [quark-flavor.md](../../sheet-proton/work/quark-flavor.md) — depends on the partial-knot framework chosen here
- [color-confinement.md](color-confinement.md) — Z₃ derivation; partial knots are the proposed mechanism
- [R60 Track 16](../../../studies/R60-metric-11/findings-16.md) — R60's Z₃ derivation; check whether partial-knot picture is compatible
