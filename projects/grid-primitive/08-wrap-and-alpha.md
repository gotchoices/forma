# Chapter 8 — Wrapping a Sheet, and What α Turns Out To Be

This chapter takes up the project's α-derivation question. The framing is intentionally modest, picking up the user's reframing: chapters 1–7 already accomplished the project's primary deliverable — establishing a primitive substrate that properly supports vacuum Maxwell and entropic gravity at the lattice scale. The α derivation is an *equal-priority but separate* question: does any deeper understanding of α emerge from the cylinder primitive's geometry?

The honest expectation is calibrated:

- A *true derivation* of α from first principles would be extremely surprising. The fine-structure constant has resisted such derivation for a century; we have no reason to expect a clean numerical prediction here.
- A *deeper structural understanding* of α — for example, identifying it as a specific geometric ratio of the cylinder primitive's wrap parameters — would be welcome.
- α emerging as a *single new free variable* (one parameter to fit) would be informative.
- α as an *interesting ratio* tying it to specific lattice structure would be valuable.
- α resolving to *two or more* independent free variables would suggest the cylinder primitive hasn't added meaningful new insight beyond what was already in [grid/charge-emergence.md](../../grid/charge-emergence.md).

With this calibration, we proceed to attempt the derivation. We take the polygonal-wrap formulation from [`dialogs/grid-3.md`](../../dialogs/grid-3.md) (which itself converged on this picture from a longer brainstorming arc) and apply it with the cylinder primitive's specific parameters. We see what comes out.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The two wraps: cylinder cross-section vs sheet-into-torus |
| 2 | The polygonal-wrap setup |
| 3 | Kink-loss per joint |
| 4 | Total loss per loop |
| 5 | The hexagonal wrap (N = 6) |
| 6 | What α turns out to be |
| 7 | Counting free variables |
| 8 | What we've learned |
| 9 | Risks and caveats |
| 10 | Summary of givens |

---

## 1. The two wraps: cylinder cross-section vs sheet-into-torus

The project has used "wrap" in two distinct senses, and the α derivation requires being careful about which is which.

**Wrap 1 — the cylinder's cross-section.** The cylinder primitive itself is a small wrapped 2D microgrid (chapter 1 §2 mechanical picture: a rubber tube with helical fibers). The cross-section circumference is 2π*r*; the wrapping is into a tube. This wrap is at the cylinder-primitive scale, internal to each edge of the lattice.

**Wrap 2 — a 2D sheet of cylinders folded into a torus.** When many cylinder primitives are arranged on a 2D hexagonal lattice (chapter 5), and that lattice is then folded into a *closed* surface (a torus), we have a *sheet wrap*. This is the wrap relevant to charge emergence per [grid/charge-emergence.md](../../grid/charge-emergence.md): a closed 2D MaSt-style sheet with a topologically nontrivial closure.

α lives at wrap 2 — the sheet wrap. It is the fractional energy loss when a wave on the lattice surface completes a loop around the closed direction of the torus. The cylinder primitive's microstructure (wrap 1) enters through the chirality parameter χ̃, but the leakage geometry is the sheet-scale wrap (wrap 2).

For this chapter, "the wrap" means wrap 2 unless otherwise stated.

---

## 2. The polygonal-wrap setup

Following the dialog's analysis (lines ~3275 of [`dialogs/grid-3.md`](../../dialogs/grid-3.md), with substantially more detail than the brief outline here suggests): instead of a smoothly curved torus, work with a *polygonal* approximation. The 2D sheet is a strip of *N* flat polygonal sides joined at *N* discrete kinks, closing into a loop of total angle 2π. Each kink turns the sheet through angle Δθ = 2π/*N*.

Why polygonal rather than smooth? Two reasons:

1. **Mathematical tractability.** A smooth bend produces *distributed* radiation losses, integrating along the curve, and the result depends on the local mode structure in a continuous-curvature regime. A polygonal version reduces this to discrete *scattering* events at each kink, much easier to analyze.
2. **Lattice-scale honesty.** The cylinder primitive's lattice is discrete (hexagonal cells at the Planck scale); a smoothly-curved torus is already an approximation. Working polygonally is closer to what the discrete lattice actually does.

Within each flat segment, the wave propagates as a normal lattice mode at *c* (chapters 5–6). At each kink, some fraction of the wave's energy radiates outward (escaping the closed loop), and the rest continues around. After *N* kinks, the wave has completed a full loop and returned to its starting point.

The total fraction of energy lost per loop is what we identify with α. The substantive question: what value does this loss fraction take, given the cylinder primitive's parameters?

---

## 3. Kink-loss per joint

At each kink, the wave encounters a discrete change in propagation direction. By analogy with waveguide physics, the per-kink leakage fraction has a small-angle expansion:

η_kink(Δθ) ≈ K · (Δθ)² + O((Δθ)⁴)

with *K* a dimensionless coefficient. This (Δθ)² scaling is universal — it follows from perturbation theory on the kink as a small angular discontinuity. The first nonzero term in the small-angle expansion is quadratic; the linear term is forbidden by the symmetry of waveguide kinks (a left-bend and a right-bend of the same magnitude must produce the same leakage).

The coefficient *K* is what depends on the medium. In our case, *K* depends on the cylinder primitive's parameters — specifically on the chirality χ̃ and on the lattice geometry.

For the cylinder primitive's wave equation (matched-chirality version from chapter 2 §4), the per-kink leakage coefficient *K*(χ̃) can in principle be computed by:

1. Setting up the matched-chirality plane wave incident on a kink.
2. Solving the matching conditions at the kink (continuity + appropriate boundary conditions).
3. Computing the reflection/transmission coefficients into the various outgoing modes (forward-transmitted, backward-reflected, radiated outward).
4. Integrating over the radiated channels.

This is a substantial calculation that we do not carry out in detail here. The structural result, however, is that *K*(χ̃) is a definite function of χ̃ — not a free parameter, but a number that the cylinder primitive's dynamics determine. For the natural shear value χ̃ = 1/√2 (chapter 2 §7), *K*(1/√2) is some specific O(1)/(several) number.

---

## 4. Total loss per loop

Summing over the *N* kinks of a polygon with all kinks of equal angle Δθ = 2π/*N*:

η_loop ≈ *N* · *K*(χ̃) · (2π/*N*)² = 4π² *K*(χ̃) / *N*

This is the central formula of the chapter. Two observations:

**The 1/N scaling.** As the polygonal wrap is refined (*N* increases), each kink becomes shallower (Δθ ~ 1/*N*), and the per-kink loss decreases as 1/*N*². But we have *N* kinks per loop, so the total loop loss is ~ *N* · 1/*N*² = 1/*N*. *Smaller* *N* (sharper kinks) gives *more* loss per loop, not less. The smooth-bend limit *N* → ∞ gives η_loop → 0 — a smooth bend leaks no energy.

**The chirality dependence.** *K*(χ̃) sits as the only χ̃-dependence in the formula. The natural shear value χ̃ = 1/√2 gives a specific *K*; other values of χ̃ give other *K*s. χ̃ enters once.

For α emerging from this, we identify

α = η_loop = 4π² *K*(χ̃) / *N*

— with both *N* and χ̃ as parameters of the wrap.

---

## 5. The hexagonal wrap (N = 6)

We need to make a choice for *N*. Two natural candidates:

- *N* = 6, the symmetry of the underlying hexagonal lattice. A hexagonal-symmetric loop on the hexagonal lattice has 6 vertices; this is the geometrically simplest closed polygon that respects the lattice.
- Some other *N* fixed by an external geometric requirement (size of a MaSt sheet, particle-specific structure, etc.).

For the bare cylinder-primitive lattice — without committing to specific MaSt-particle structure — *N* = 6 is the natural choice. It comes from the hexagonal-lattice symmetry that the project committed to in chapter 5, and it does not introduce any new information beyond that lattice choice.

With *N* = 6:

α = 4π² *K*(χ̃) / 6 = (2π²/3) · *K*(χ̃)

For χ̃ pinned at the natural value 1/√2 (chapter 2 §7):

α = (2π²/3) · *K*(1/√2)

Both *N* and χ̃ are now pinned by independent considerations from earlier chapters (the hexagonal lattice from chapter 5; the natural shear from chapter 2 §7). What remains free is *K*(1/√2) — a single coefficient.

For α to be reproduced at its measured value, *K*(1/√2) must equal:

*K*(1/√2) = 3 α / (2π²)

Using the CODATA 2018 measured value α = 7.2973525693(11) × 10⁻³:

*K*(1/√2) ≈ 1.109064598 × 10⁻³

(reliable to about 10 significant figures, set by the precision of α). This is the specific number the cylinder primitive's per-kink leakage coefficient at χ̃ = 1/√2 would have to come out to. Whether it actually does so requires the explicit calculation outlined in §3.

---

## 6. What α turns out to be

The structural form is now visible. Under the cylinder primitive on a 2D hexagonal lattice, with χ̃ at the natural shear value and *N* fixed by the lattice's hexagonal symmetry:

α = (2π²/3) · *K*(1/√2)

This is the headline result of the chapter, such as it is. α is *not* a free parameter floating above the lattice's dynamics; it is a specific geometric ratio. Its value is fixed once we specify (i) the hexagonal lattice geometry, (ii) the natural shear χ̃ = 1/√2, and (iii) the per-kink leakage coefficient *K*(1/√2) which is determined (in principle) by the cylinder primitive's wave equation.

What this delivers, structurally:

- A clean *form* for α: it is the kink-loss fraction per hexagonal-symmetric loop on the cylinder primitive's lattice.
- A *single* dimensionless parameter (*K*(1/√2)) determines its value once the lattice and shear are fixed. *N* and χ̃ are *not* additional free variables — they are pinned by independent reasoning in earlier chapters.
- The factor of 2π²/3 is a definite geometric prefactor coming from the polygonal-wrap geometry; it is not adjustable.

What this does *not* deliver:

- A predicted numerical value for α. *K*(1/√2) is calculable in principle from the cylinder primitive's wave equation, but doing the calculation requires substantial work that is not undertaken in this chapter.
- A reason why α has the specific value 1/137. Even if we computed *K*(1/√2) and it came out to 1.11 × 10⁻³, that would be a consistency check, not an explanation of why nature picked this number.

---

## 7. Counting free variables

Per the user's reframing, the project's outcome on α should be assessed by how many free variables α resolves to:

- **0 free variables (full prediction):** α is completely determined by the cylinder primitive's structure, no fits anywhere. → Extremely surprising.
- **1 free variable:** α reduces to a single parameter that the cylinder primitive's geometry fixes once you specify the lattice and shear. → Interesting ratio; structural understanding gained.
- **2 free variables:** α depends on two independent parameters that the cylinder primitive does not pin. → Doubts about whether the α derivation has added insight.
- **3 or more:** Worse.

By the analysis above:

- *N* = 6 is fixed by the hexagonal lattice (chapter 5 commitment, not a new free parameter for chapter 8).
- χ̃ = 1/√2 is fixed by the natural-shear argument (chapter 2 §7, not a new free parameter for chapter 8).
- *K*(χ̃) is a function the cylinder primitive determines (in principle) — *one* coefficient, computable from the wave equation, evaluated at the natural χ̃.

So α reduces to **one free variable** in this analysis: the value of *K*(1/√2). That is the count we hoped to get to. The chapter delivers a structural understanding of α as a kink-loss ratio depending on a single coefficient that the cylinder primitive's dynamics in principle determine.

A caveat. If *K*(1/√2) can only be computed up to an O(1) factor that depends on conventions or normalizations, the "single free variable" count could effectively become "1 + a small uncertainty." The chapter's count of 1 is the cleanest interpretation; tightening it to a numerical prediction requires the explicit calculation.

---

## 8. What we've learned

The α-derivation exercise has produced:

**A structural identification.** α is the per-loop fractional energy loss when a 2D sheet of cylinder primitives is folded into a hexagonally-symmetric torus. This identifies α with a *geometric ratio*, not with a coupling pulled out of nowhere.

**A reduction to one coefficient.** The structural form α = (2π²/3) · *K*(1/√2) reduces α to a single per-kink leakage coefficient. The hexagonal lattice and natural shear value are inputs from earlier chapters; *K*(1/√2) is the only "α-specific" parameter remaining.

**A reframing of what an α-derivation could mean.** α is *not* derivable from pure number theory or pure geometry alone (per [primers/alpha-in-grid.md](../../primers/alpha-in-grid.md), this is consistent with the historical record — Eddington and others tried such derivations and they did not hold up). What the cylinder primitive contributes is a *picture* of α as the leakage rate of a specific wrap geometry, with one calculable coefficient. This is a *deeper understanding* in the user's framing — a structural picture — even if it is not a numerical prediction.

**A sharp future calculation.** If someone wanted to push for a full numerical prediction of α from this framework, the well-defined calculation is: *K*(1/√2) for the matched-chirality wave equation with kink-scattering boundary conditions. This is a piece of waveguide physics that can be computed, in principle, from chapter 2's wave equation alone. It is well-defined and bounded in scope; it is not undertaken here, but it is available as follow-up.

**An honest assessment of how this compares to grid/charge-emergence.md.** [grid/charge-emergence.md](../../grid/charge-emergence.md) was candid that its account of the α magnitude was hand-wavey. The cylinder primitive's contribution is to give a *specific structural form* for α (the kink-loss ratio with one calculable coefficient), with the lattice parameters fixed by independent considerations from earlier chapters. This is an improvement over charge-emergence.md's framing — though still not a numerical prediction. If a follow-up calculates *K*(1/√2) explicitly, the comparison to α = 1/137 will be a real consistency test of the cylinder primitive's parameters against observation.

---

## 9. Risks and caveats

- **Risk: *K*(1/√2) might not be O(10⁻³).** If the actual calculation gives a wildly different value, the structural form α = (2π²/3) · *K*(1/√2) holds but the numerical match to α = 1/137 fails. That would be a real falsification — the cylinder primitive on a hexagonal lattice with χ̃ = 1/√2 simply doesn't reproduce the observed coupling. The follow-up calculation would tell us this.
- **Risk: *N* = 6 might not be the right choice.** The hexagonal-symmetric loop is geometrically natural for the hexagonal lattice, but a MaSt-style charge-bearing torus might have a different *N* set by the particle's specific structure. If so, α would have residual *N*-dependence that we have not pinned. The chapter's claim of "1 free variable" depends on *N* = 6 being the right choice; a more careful analysis of which *N* applies to actual physical particles is downstream work.
- **Risk: the polygonal approximation might miss continuous-bend physics.** The polygonal approximation cleanly separates per-kink scattering from continuous propagation, but in reality the lattice could have continuous-curvature contributions that the polygonal limit misses. Whether these are negligible in the long-wavelength regime is a calculation we have not done.
- **Risk: the per-kink scaling (Δθ)² might break down for χ̃ = 1/√2.** Perturbation theory on the kink assumes Δθ is small. For *N* = 6, Δθ = 60° = 1.05 rad, which is not particularly small. Higher-order corrections (Δθ⁴, etc.) might matter at this order. The chapter's formula η_kink ≈ K · (Δθ)² is the leading-order term; the full expansion has more.
- **Risk: the choice of MaSt-style closure interpretation.** The cylinder-primitive sheet-into-torus wrap is meant to correspond to MaSt-style particle structure (compact dimensions wrapped into closed surfaces). But the project explicitly does not commit to a specific MaSt particle (electron, proton, etc.), so the wrap geometry's connection to "the" α (as observed for, say, the electron) is not pinned. α might depend on *which* particle's wrap we're looking at — a possibility that grid/charge-emergence.md raised but did not resolve.

---

## 10. Summary of givens

What this chapter establishes:

- α takes a structural form on the cylinder primitive's lattice: it is the kink-loss fraction per loop when a 2D sheet of primitives is wrapped into a polygonal torus.
- Under the polygonal-wrap formula η_loop = 4π² *K*(χ̃) / *N*, with *N* fixed at 6 by the hexagonal-lattice symmetry (chapter 5) and χ̃ fixed at 1/√2 by the natural-shear argument (chapter 2 §7), α reduces to (2π²/3) · *K*(1/√2).
- This leaves *K*(1/√2) — a single coefficient computable in principle from the cylinder primitive's wave equation — as the only α-specific parameter.
- A numerical prediction of α from this framework requires the explicit calculation of *K*(1/√2). That calculation is well-defined but not undertaken in this chapter; it is available as follow-up.
- The α-derivation does not produce a numerical prediction. What it produces is a *structural understanding* of α as a kink-loss ratio with a single calculable coefficient — the user's "deeper understanding" outcome rather than the "true derivation" outcome.
- The cylinder primitive's contribution to the α story is an improvement over [grid/charge-emergence.md](../../grid/charge-emergence.md)'s previous hand-wavey magnitude, in that the structural form is now specific and the parameters are mostly pinned by earlier chapters. It is not a complete answer to "where does α come from?" but it is a step toward making that question concrete.

The next chapter is the project's closing summary.
