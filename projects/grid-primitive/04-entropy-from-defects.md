# Chapter 4 — Entropy from Topological Defects

**Status:** outline — sections are framed but not yet infilled. This is the project's fail-fast chapter on gravity. Awaiting review before the algebra is written out.

This chapter takes the cylinder primitive established in [01-foundation.md](01-foundation.md) and the wave dynamics of [02-wave-on-a-primitive.md](02-wave-on-a-primitive.md) and asks the load-bearing question for theory 7 of [README.md](README.md):

> *Do topological vortex defects in the 2D stress vector field supply the entropy density that Jacobson's argument requires for the lattice to produce 1/r gravity?*

The chapter is structured to **fail fast**. If the topological-defect mechanism does not deliver an entropy that matches GRID's ζ = 1/4 bit per cell at the right scaling, the project triggers the fallback in ground rule 8 — pivot to a discrete phase-based primitive — before continuing to chapters 5–8.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | What Jacobson's argument requires from the entropy account |
| 2 | The 2D stress vector field and its target-space topology |
| 3 | Vortex defects: structure, winding number, energy cost |
| 4 | Vortex statistics and the BKT regime |
| 5 | Entropy density per unit area on a 2D lattice of primitives |
| 6 | Matching to GRID's ζ = 1/4 bit per cell |
| 7 | The fail-fast verdict: success, partial success, or pivot |
| 8 | Backup mechanisms if defects alone do not suffice |
| 9 | Summary of givens |

---

## 1. What Jacobson's argument requires

Goal: state precisely what entropy mechanism Jacobson's derivation needs, so the chapter knows what target it is matching.

*To infill:* a brief recap of [grid/gravity.md](../../grid/gravity.md). Jacobson (1995) argues that if every causal horizon carries entropy *S* = ζ · *A* (entropy proportional to area, with coefficient ζ), then applying *δQ* = *T* · *δS* to energy flowing through the horizon forces the geometry to satisfy Einstein's field equations. The key inputs are:

- Entropy density per unit area: *S*/*A* = ζ (not per unit volume).
- The entropy must be local — attached to the horizon, not a global property.
- ζ = 1/4 is the value GRID derives from cell geometry (axiom A5).

The chapter's task: show that the cylinder primitive's vortex defects, when assembled into a 2D lattice, produce an entropy with this scaling and (ideally) this coefficient.

---

## 2. The 2D stress vector field and its target-space topology

Goal: set up the field-theoretic structure on which defects live.

*To infill:* on a 2D lattice of cylinders (chapter 5's setting, taken here as anticipation), the stress vector field becomes ψ(*x*, *y*, *t*) where (*x*, *y*) are the two extended spatial coordinates of the lattice and *t* is time. The target space is ℝ² ≅ ℂ. Topology of the target with the origin removed: π₁(ℝ² \ {0}) = ℤ.

The field configuration at any instant is a map from the 2D spatial lattice (taken as continuous in the long-wavelength limit) to ℝ². Vortices are points in the 2D spatial domain where ψ = 0 with nonzero winding number. Their worldlines trace through (*x*, *y*, *t*) space.

---

## 3. Vortex defects — structure, winding, and energy

Goal: characterize vortex defects in this field theory.

*To infill:*

- **Structure.** Near a vortex at position (*x*_0, *y*_0), the field has the form ψ ~ (*z* − *z*_0)^*n* with *z* = *x* + *iy* and integer winding *n*. Magnitude vanishes at the core; phase rotates 2π*n* around it.
- **Winding number** *n* is a topological invariant; it can only change by creation/annihilation of opposite-sign defects.
- **Energy** of an isolated vortex grows logarithmically with system size: *E*_vortex ~ *πK* log(*L*/*a*), where *K* is an effective stiffness (built from the chapter 1/2 stiffness matrix entries *K*_ee, *K*_φφ, *K*_eφ) and *a* is a UV cutoff (the cylinder length *L* or some lattice scale).
- **Vortex–antivortex pair energy** stays finite as system size grows (the two log divergences cancel at large separation, reduced to log of the pair separation).

This is standard 2D XY model physics; the chapter cites the canonical results rather than re-deriving them.

---

## 4. Vortex statistics and the BKT regime

Goal: determine the equilibrium population of vortices at the relevant temperature.

*To infill:*

- **Berezinskii–Kosterlitz–Thouless (BKT) transition.** At temperature *T* < *T*_BKT, vortices and antivortices are bound in pairs; at *T* > *T*_BKT, they unbind and proliferate freely. The critical temperature is *T*_BKT = π *K* / 2 in the canonical normalization.
- **Vortex density** as a function of *T*. In the unbound phase, the equilibrium density of free vortices ξ⁻² (where ξ is the correlation length) determines the entropy.
- **Which regime is the lattice in?** This is the substantive question. The chapter uses the stiffness scales pinned in chapter 3 to estimate where the lattice sits relative to *T*_BKT — specifically, whether the entropy from defects is in the dilute (bound-pair) regime or the dense (unbound) regime.

The chapter does not need to compute *T*_BKT exactly; it needs to determine the qualitative regime, because that determines the entropy scaling.

---

## 5. Entropy density per unit area

Goal: compute *S*/*A*, the entropy contribution from defects per unit lattice area.

*To infill:*

- **Counting argument.** The entropy of a 2D field with *N*_v vortex defects in area *A* is roughly *S* ~ *N*_v · *k*_B · log(*A*/*N*_v) — vortices act as quasi-particles whose configurational entropy is positional.
- **Dilute regime.** In the bound-pair regime, free vortices are exponentially suppressed; entropy from defects alone is small. In this regime the project must rely on the bound-pair "internal" entropy or on the backup mechanisms of chapter 1 §4.
- **Dense regime.** In the unbound regime, entropy from defects scales as *S*/*A* ~ *k*_B / ξ². If ξ scales with the Planck length (lattice spacing), this gives entropy proportional to area in Planck units — the right scaling.
- **The coefficient.** Whether the prefactor matches ζ = 1/4 is the substantive check. The chapter computes this from the cylinder's stiffness scales (pinned in chapter 3) and compares.

This is the longest section of the chapter and the most technically demanding.

---

## 6. Matching to GRID's ζ = 1/4 bit per cell

Goal: stand the result of §5 next to GRID's required value.

*To infill:* GRID derives ζ = 1/4 from the simplicial cell geometry — each 3D tetrahedral cell has 4 face-sharing neighbors, so each cell contributes 1/4 bit per neighbor pair (see [grid/foundations.md](../../grid/foundations.md) §A5). For the 2D primitive lattice, the analogous count gives a value to be worked out. The chapter compares the *S*/*A* from §5 to this geometric value.

Three possibilities, each leading to a different §7 outcome:

- **Exact or near-exact match.** Defect entropy = ζ at the required coefficient. Theory 7 succeeds.
- **Right scaling, wrong coefficient.** *S*/*A* is proportional to area but with a coefficient different from 1/4. Possibly fixable by accounting for additional contributions; possibly a small mismatch tolerable as approximation.
- **Wrong scaling.** *S*/*A* does not scale linearly with area, or scales as area but with parameters that don't match the lattice. Theory 7 fails.

---

## 7. The fail-fast verdict

Goal: declare success, partial success, or pivot.

*To infill, scenario by scenario:*

- **Success.** Defect entropy matches ζ in scaling and coefficient. The chapter records this and returns control to the chapter sequence (5–8 proceed as planned). Theory 7 of the README is upgraded from "load-bearing bet" to "established."

- **Partial success.** Scaling is right; coefficient is off. The chapter examines whether the backup mechanisms (§8) can supplement, and either (a) declares qualified success with a flagged residual or (b) escalates to pivot.

- **Failure.** Scaling is wrong, or no defects exist in the equilibrium regime, or the entropy is parametrically too small. The chapter triggers ground rule 8: the project pivots to a discrete phase-based primitive in the spirit of the viz model. README's theory 7, theory 9, and the chapter sequence past chapter 4 are all rescoped at this point.

---

## 8. Backup mechanisms if defects alone do not suffice

Goal: lay out the secondary entropy candidates from chapter 1 §4 in case the primary defect mechanism fails.

*To infill:*

- **Longitudinal Fourier modes** of *e* and *φ* along each cylinder give a tower of oscillator modes per edge — exactly the structure that supplied [grid/sim-gravity-2/](../../grid/sim-gravity-2/)'s working entropy reservoir. Adopting this requires extending the primitive to support multiple modes per cylinder (an enrichment of chapter 1's two-DoF commitment), but it is well-tested in the existing GRID framework.

- **Non-trivial winding sectors of *φ(x)* along a single cylinder.** Each cylinder can carry a winding-number sector indexed by the integer ∮ d*φ*/2π along its length. This is a discrete invariant per cylinder and contributes a finite entropy per primitive.

- **Hybrid.** Defects + Fourier modes + winding sectors combined may match where defects alone fall short.

The chapter notes which combination is required if defects alone do not match.

---

## 9. Summary of givens

Goal: consolidate the chapter's findings.

*To infill:* a brief statement of what the chapter establishes:

- The 2D stress vector field supports vortex defects with integer winding number.
- Defect equilibrium statistics (BKT regime, density) are determined by the stiffness scales pinned in chapter 3.
- The defect entropy density either matches, partially matches, or fails to match GRID's ζ.
- The verdict for theory 7 (success / partial / pivot).
- The backup mechanisms available if defects alone do not suffice.

If the verdict is success or partial success, the chapter closes by handing off to chapter 5 (assembling the 2D lattice). If the verdict is pivot, the chapter closes with the rescoping that is required and the next steps for the project.

---

## Decisions to confirm before infill

1. **BKT-regime calculation depth.** Compute *T*_BKT and the equilibrium vortex density explicitly from the chapter-3 stiffness scales? Or treat BKT as a black box from the literature and focus on whether the *scaling* of *S*/*A* matches Jacobson's requirement?
2. **2D lattice anticipation.** Chapter 5 assembles the 2D periodic lattice; chapter 4 needs to anticipate this for defect counting. How explicit should chapter 4 be about lattice details — fully assume chapter 5's setup, or work in a generic 2D continuum limit?
3. **Failure protocol.** If the verdict is "pivot," chapter 4 should describe the rescoping in enough detail that the project can resume with a discrete primitive. How much of that rescoping belongs in chapter 4 vs in a revised README?
4. **Length and pacing.** Chapter 4 is technically the most demanding chapter so far — BKT, defect statistics, entropy matching. Aim for chapter-1 length (~300 lines), or longer if the algebra requires?
