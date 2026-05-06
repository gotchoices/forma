# Chapter 8 — Wrapping a Sheet, and What α Might Turn Out To Be

This chapter takes up the project's α question. The framing is intentionally modest: chapters 1–7 already accomplished the project's primary deliverable — establishing a primitive substrate that properly supports vacuum Maxwell and entropic gravity at the lattice scale. The α exercise is an *equal-priority but separate* question: does any deeper understanding of α emerge from the cylinder primitive's geometry?

The honest expectation is calibrated:

- A *true derivation* of α from first principles would be extremely surprising. The fine-structure constant has resisted such derivation for a century; we have no reason to expect a clean numerical prediction here.
- A *deeper structural understanding* of α — for example, identifying it as a specific geometric ratio of the cylinder primitive's wrap parameters — would be welcome.
- α emerging as a *single new free variable* (one parameter to fit) would be informative.
- α as an *interesting ratio* tying it to specific lattice structure would be valuable.
- α resolving to *two or more* independent free variables would suggest the cylinder primitive hasn't added meaningful new insight beyond what was already in [grid/charge-emergence.md](../../grid/charge-emergence.md).

A summary upfront, since the result is conditional. We attempt the derivation along the polygonal-wrap formulation from [`dialogs/grid-3.md`](../../dialogs/grid-3.md). Two limitations of that approach surface in §4 — the (Δθ)² perturbative expansion is not controlled at *N* = 6, and the assumed incoherent-kink-summation rule does not apply to a coherent closed loop. Both are the regime relevant to α. The chapter therefore arrives at an *inconclusive* result: a candidate physical picture for α (a kink-loss fraction on a closed wrap) and a sharpened target for a future calculation, but no controlled structural form for α at the *N* of interest. We mark the leading-order expressions as conditional throughout and collect the limitations explicitly in §10.

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
| 9 | The fractal recursion: another wrap one level down |
| 10 | Limitations |
| 11 | Summary of givens |

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

## 4. Total loss per loop — and the limits of the leading-order treatment

Naively summing over the *N* kinks of a polygon with all kinks of equal angle Δθ = 2π/*N*:

η_loop ≈ *N* · *K*(χ̃) · (2π/*N*)² = 4π² *K*(χ̃) / *N*

Before reading anything into this expression, two warnings about the regime in which it can be trusted.

### Warning 1 — the small-Δθ expansion is not controlled at N = 6

η_kink(Δθ) is the leading term of a power series

η_kink(Δθ) = *K*₂(χ̃) Δθ² + *K*₄(χ̃) Δθ⁴ + *K*₆(χ̃) Δθ⁶ + …

(the chapter's *K*(χ̃) is *K*₂(χ̃)). Summing over N kinks at Δθ = 2π/N gives

η_loop = *K*₂(χ̃)·(2π)²/*N* + *K*₄(χ̃)·(2π)⁴/*N*³ + *K*₆(χ̃)·(2π)⁶/*N*⁵ + …

The natural expansion parameter is (2π/*N*)². At *N* = 6 this is (π/3)² ≈ 1.10 — *order unity*, not small. Successive powers are 1.10, 1.21, 1.33, … — the geometric factor multiplying *K*₂ₙ does not shrink with *n*. For the leading-term truncation η_loop ≈ 4π²*K*₂(χ̃)/*N* to be the dominant contribution at *N* = 6, the higher-order coefficients *K*₄, *K*₆, … would have to fall off faster than the geometric factor grows. This chapter does not establish that they do.

So 4π²*K*(χ̃)/*N* is the leading term of a series whose *convergence at N = 6* is unestablished. In the smooth-bend limit *N* → ∞ the series is well-behaved and the leading term dominates, but the smooth-bend limit gives η_loop → 0 — no α. The interesting case (*N* = 6) is exactly the case where the perturbative formula is least trustworthy.

### Warning 2 — η_loop = N · η_kink assumes incoherent kink summation

The summation step "η_loop = *N* · η_kink" treats each kink as scattering independently — an *incoherent* sum of losses. On a closed loop where the wave phase-coheres around the polygon, kink scattering generally interferes (constructively or destructively) depending on the phase the wave accumulates between kinks. The correct expression is the modulus-squared of an N-step amplitude sum, not *N* times the single-kink loss.

For *N* = 6 with wavelengths comparable to the polygon size — the regime in which a single mode lives on the loop — interference is not negligible and η_loop ≠ *N* · η_kink in general. This chapter does not carry out the coherent-summation calculation.

### What survives the warnings

The structural observation — *that α can be cast as a kink-loss fraction per closed loop on a wrapped sheet* — survives. What does not survive without further work is the specific functional form 4π²*K*(χ̃)/*N* at *N* = 6.

For the rest of this chapter we carry the leading-order formula forward as a **structural sketch** rather than a controlled result, and we explicitly mark its conditional status when we write it down.

---

## 5. The hexagonal wrap (N = 6)

If we make a choice for *N*, two natural candidates appear:

- *N* = 6, the symmetry of the underlying hexagonal lattice. A hexagonal-symmetric loop on the hexagonal lattice has 6 vertices; this is the geometrically simplest closed polygon that respects the lattice.
- Some other *N* fixed by an external geometric requirement (size of a MaSt sheet, particle-specific structure, etc.).

For the bare cylinder-primitive lattice — without committing to specific MaSt-particle structure — *N* = 6 is the natural choice from the lattice symmetry of chapter 5.

Substituting *N* = 6 into the leading-order formula:

α ~ 4π² *K*(χ̃) / 6 = (2π²/3) · *K*(χ̃)        *(leading-order, conditional)*

For χ̃ tentatively at the natural midpoint 1/√2 (chapter 2 §7's arithmetic-midpoint argument):

α ~ (2π²/3) · *K*(1/√2)        *(leading-order, conditional)*

The "~" rather than "=" is deliberate. Both warnings of §4 apply: the (Δθ)² expansion is not controlled at *N* = 6 (Δθ² ≈ 1.10), and η_loop = *N* · η_kink assumes incoherent summation that is not appropriate for a coherent closed loop. We are writing what the leading-order formula gives if it were trustworthy at this *N*; we are not asserting that it is.

We do *not* back out a numerical value of *K*(1/√2) from the measured α. Even setting aside whether the calculation outlined in §3 produces a particular number, doing so would presume a controlled relationship between *K*(1/√2) and α that this chapter has not established.

---

## 6. What α might turn out to be

A structural sketch, under the conditional reading of §4–§5:

α ~ (2π²/3) · *K*(1/√2)        *(if the leading-order formula and incoherent summation applied at N = 6)*

This says: *if* the leading-order kink-loss expression were controlled at *N* = 6, *and* if the incoherent-summation rule applied, *then* α would take this form on the cylinder primitive on a 2D hexagonal lattice with χ̃ = 1/√2.

What the sketch identifies, conditional on those assumptions:

- A candidate *form* for α as a kink-loss fraction per hexagonal-symmetric closed loop.
- A reduction (within the conditional) to a single calculable coefficient *K*(1/√2).
- A definite geometric prefactor 2π²/3 if the leading-order treatment held.

What the sketch does *not* deliver:

- An established structural form for α. The two warnings of §4 — uncontrolled (Δθ)² expansion at *N* = 6, and incoherent-summation assumption inappropriate for a coherent loop — are not addressed in this chapter, and either could change the form qualitatively.
- A predicted numerical value for α.
- A reason why α has the specific value 1/137.

The cylinder primitive's contribution at this stage is therefore not the formula α = (2π²/3)·*K*(1/√2) but the more modest claim that *the question of α can be sharpened into a kink-loss-on-a-wrap calculation* — a calculation that becomes well-defined once a concrete lattice-level kink model and a coherent-summation treatment are supplied.

---

## 7. Counting free variables — conditional answer

Per the user's reframing, the project's outcome on α can be assessed by how many free variables α resolves to:

- **0 free variables (full prediction):** α is completely determined by the cylinder primitive's structure, no fits anywhere. → Extremely surprising.
- **1 free variable:** α reduces to a single parameter that the cylinder primitive's geometry fixes once you specify the lattice and shear. → Interesting ratio; structural understanding gained.
- **2 free variables:** α depends on two independent parameters that the cylinder primitive does not pin. → Doubts about whether the analysis has added insight.
- **3 or more:** Worse.

If the leading-order formula η_loop = 4π²*K*(χ̃)/*N* with incoherent kink summation were controlled at *N* = 6, the count would be 1: *N* fixed by the hexagonal lattice, χ̃ fixed by the chapter-2 midpoint argument, and *K*(1/√2) the lone calculable coefficient.

But §4 flagged that neither prerequisite is established. The actual count this chapter delivers is therefore:

- **In the controlled regime (large *N*, small Δθ):** 1 free variable — but in this regime η_loop → 0 and the wrap doesn't produce α.
- **At N = 6, where α-relevant physics would live:** unestablished. The leading-order count of 1 may underestimate the true number; the higher-order *K*₄, *K*₆, … carry their own χ̃-dependences, and coherent-summation interference adds N-specific structure that the leading-order formula doesn't capture. A faithful count at *N* = 6 awaits the calculation outlined in §3 plus a coherent-summation treatment.

The honest version of the chapter's result is therefore "the structural picture is suggestive of a single-parameter reduction, *if* the calculation goes through cleanly at *N* = 6." The chapter does not establish that it does.

---

## 8. What we've learned

The α exercise has produced something more modest than the chapter originally framed:

**A sharpening of the question.** The cylinder primitive lets us recast "where does α come from?" as "what is the per-loop fractional energy loss when a sheet of primitives is wrapped into a closed surface?" This is a sharpening — a kink-loss-on-a-wrap calculation, with a definite (if not yet specified) lattice-level kink model — not yet a structural form for α.

**An identification of the calculation that would settle the question.** Within this framework the well-defined calculation is the matched-chirality scattering problem at a lattice-level kink, plus a coherent-summation treatment around a closed N-kink loop. If carried out, this would either produce a definite structural form for α (best case) or reveal that the kink-loss picture doesn't survive coherent-loop physics at *N* = 6 (negative result).

**An identified obstacle.** At *N* = 6 the natural perturbative parameter (Δθ)² ≈ 1.10 is order unity, so the leading-order formula 4π²*K*(χ̃)/*N* is not a controlled approximation in the regime of interest. Combined with the incoherent-summation assumption being inappropriate for a coherent closed loop, this means the chapter's leading-order expressions are best read as a *placeholder* awaiting a non-perturbative or coherent-loop treatment.

**A reframing of what an α-derivation could mean.** α is not derivable from pure number theory or pure geometry alone (per [primers/alpha-in-grid.md](../../primers/alpha-in-grid.md), consistent with the historical record). What the cylinder primitive offers is a *candidate physical picture* — α as the leakage rate of a specific wrap geometry — that, *if* the underlying scattering and coherent-summation calculation goes through, would resolve to a structural form with a small number of parameters. The chapter does not establish that it goes through.

**Comparison to grid/charge-emergence.md.** [grid/charge-emergence.md](../../grid/charge-emergence.md) was candid that its account of the α magnitude was hand-wavey. This chapter does not yet improve on that — what it adds is a more concrete *target* for a future calculation, not a structural answer. If the §3 calculation is performed with a concrete kink model and the coherent-loop summation is done correctly, *that* result would be the real comparison to charge-emergence.md.

---

## 9. The fractal recursion: another wrap one level down

A brief observation that ties this chapter to the foundation. The cylinder primitive itself, viewed under the fractal-microgrid interpretation (chapter 1 §8), is a wrapped 2D microgrid — a sheet of microgrid wrapped into a tube of cross-section circumference 2π*r*. This is *another* 2π wrap, one fractal level below the sheet wrap that this chapter examines.

Two structural observations follow:

**The cross-section wrap produces mass-analog, not charge.** The cross-section is a 1D ring (the circumference, parametrized by an angular coordinate). Wrapping a 1D direction into a closed loop is the standard Kaluza-Klein topology that produces mass-analog through quantized transverse momentum — exactly the mechanism that gives the cylinder its substrate inertia in chapter 1 §8. It does *not* produce charge: charge requires a *two*-dimensional wrap of a sheet into a closed surface (the sheet wrap of this chapter), not a 1D wrap of an angular coordinate. So the cross-section wrap contributes a "dark mass" at the substrate level (in MaSt terminology — mass-analog from compact-wrap quantization, not coupled to electromagnetism), not a substrate-level charge.

**Any radial leakage at the cross-section level is dynamic, not static.** If we naively applied chapter 8's polygonal kink-loss formula at the cross-section scale, we would get some leakage rate per cross-section loop — but with the same controlled-regime caveats as the sheet-wrap calculation (and again with order-unity Δθ if the cross-section is approximated by a small-N polygon). Setting the controlled-regime question aside, this leakage is dynamic rather than static: it is tied to whatever signals are passing through the cylinder at any moment, and time-averages to zero. Even if the per-loop rate is nonzero, the time-averaged radial signature is zero, so there is no observable static field from the substrate-level wrap.

These observations are qualitative — they explain why the cross-section wrap doesn't *add* an unaccounted feature, not why it produces any specific quantitative result. The detailed cross-section dynamics — exactly how the microgrid produces *D*, what coefficients a microgrid analog of *K*(χ̃) would have — are deferred per ground rule 3.

---

## 10. Limitations

The following are *limitations* of the chapter's analysis, not just downstream risks. Most are flagged inline above; collected here for clarity.

- **The (Δθ)² expansion is uncontrolled at *N* = 6.** Natural expansion parameter (2π/*N*)² ≈ 1.10 at *N* = 6 is order unity. The leading-order formula 4π²*K*(χ̃)/*N* is not a controlled approximation in this regime; higher-order coefficients *K*₄(χ̃), *K*₆(χ̃), … contribute at the same order as the leading term and have not been computed.
- **Coherent-loop interference is not addressed.** η_loop = *N* · η_kink assumes incoherent kink summation. On a closed loop where the wave phase-coheres around the polygon, the correct expression is the squared magnitude of an *N*-step amplitude sum, not *N* times the single-kink loss. This chapter does not perform that summation.
- **Lattice-level kink model is not specified.** The "polygonal wrap" is described at the level of "*N* flat segments joined at *N* kinks of angle Δθ." How that maps to a concrete modification of the hexagonal-lattice cylinder primitive — which edges are bent, what matching conditions apply at the bend, what radiated channels exist — is not pinned down in this chapter. Without that specification the §3 calculation is not yet well-posed.
- **Whether *K* depends only on χ̃ is asserted, not shown.** Step 4 of the §3 calculation outline (integrate over radiated channels) is what would determine whether *K* is a function of χ̃ alone or whether it carries additional dependence on *N* or local kink geometry. This step is not performed.
- ***N* = 6 is a lattice-symmetry choice, not a physics-pinned value.** A MaSt-style charge-bearing torus might have a different *N* set by particle-specific structure, in which case α would have residual *N*-dependence beyond the lattice-symmetry choice.
- **χ̃ = 1/√2 is a "natural midpoint" choice, not a derived value.** Chapter 2 §7 explicitly states that nothing in chapter 2 alone pins χ̃; the arithmetic-midpoint argument identifies 1/√2 as natural, not necessary. Treating it as fixed in this chapter's α expression is a working choice, not a result.
- **The polygonal approximation may miss continuous-bend physics.** Even if the per-kink picture were controlled at *N* = 6, the lattice could have continuous-curvature contributions that the polygonal limit treats incorrectly.
- **The chapter does not commit to a specific MaSt particle.** The sheet-into-torus wrap is meant to correspond to MaSt-style particle structure, but no specific particle (electron, proton, etc.) is identified. The connection between "this wrap geometry" and "α as measured for the electron" is therefore not pinned; α might in principle depend on which particle's wrap is being considered.

---

## 11. Summary of givens

What this chapter establishes:

- A *candidate physical picture* for α: the per-loop fractional energy loss when a 2D sheet of cylinder primitives is wrapped into a closed polygonal surface.
- A *concrete target* for a future calculation: the matched-chirality scattering problem at a lattice-level kink, summed coherently around an *N*-kink closed loop.
- A leading-order formula η_loop ≈ 4π²*K*(χ̃)/*N* that *would*, if controlled, reduce α to a single calculable coefficient *K*(1/√2). The chapter does not establish that the formula is controlled at *N* = 6 — see §4 and §10 for the explicit limitations.

What this chapter does *not* establish:

- A controlled structural form for α at *N* = 6. The (Δθ)² expansion has order-unity expansion parameter at this *N*, and the incoherent-summation rule η_loop = *N* · η_kink is not appropriate for a coherent closed loop. Either limitation could change the leading-order form qualitatively.
- A numerical prediction of α.
- An improvement over [grid/charge-emergence.md](../../grid/charge-emergence.md)'s account of the α magnitude. What this chapter offers is a sharper *target* for follow-up work; the answer waits on that work.

The α exercise is therefore inconclusive: a candidate picture and a well-defined calculation, both contingent on prerequisites the chapter cannot satisfy. Whether α emerges from the cylinder primitive's geometry — and in what functional form — remains open.

The next chapter is the project's closing summary.
