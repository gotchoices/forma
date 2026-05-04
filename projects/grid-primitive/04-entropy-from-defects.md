# Chapter 4 — The Entropy Account

This chapter takes up the load-bearing question of [README.md](README.md)'s theory 7:

> *Does the cylinder primitive's stress vector field on a 2D lattice supply the entropy that Jacobson's argument requires for the lattice to produce 1/r gravity?*

The chapter started life expecting that topological vortex defects would have to do the work — that the entropy would come from the topology of the field, with vortex–antivortex condensation in a Berezinskii–Kosterlitz–Thouless regime supplying the right scaling. As the math is worked out, and as direct simulation tests are run alongside it, a simpler picture emerges: the *linear* theory's ordinary Gaussian fluctuations already produce the entropic 1/r force scaling. Topological defects turn out to be a *refinement* for the coefficient — possibly required for the precise match to ζ = 1/4 — but they are not the source of the scaling.

We follow the discovery in the order the math reveals it.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | What Jacobson's argument requires from the entropy |
| 2 | The starting hypothesis — topological defects, and why we look more carefully |
| 3 | The 2D Laplacian Green's function |
| 4 | The cylinder primitive in equilibrium satisfies the 2D Laplace equation |
| 5 | From log potential to 1/r force law |
| 6 | Thermal fluctuations and the variance shadow |
| 7 | What three independent simulation tests confirm |
| 8 | The coefficient question — what is left for downstream work |
| 9 | Where topological defects could still matter |
| 10 | Summary of givens |

---

## 1. What Jacobson's argument requires from the entropy

Before deciding whether the cylinder primitive supplies the right entropy, we need to be precise about what *kind* of entropy account Jacobson's argument requires. A condensed sketch of [grid/gravity.md](../../grid/gravity.md):

Jacobson (1995) showed that if every causal horizon in spacetime carries entropy proportional to its area,

*S* = ζ · *A*

with ζ a dimensionless coefficient (ζ = 1/4 in GRID, from axiom A5), then the *Clausius relation*

δ*Q* = *T* · δ*S*

— heat flowing through the horizon equals the horizon temperature times the change in horizon entropy — combined with the geometric relation between area changes and curvature (the Raychaudhuri equation), forces the geometry to satisfy Einstein's field equations. The Newtonian limit then gives gravity's force law: in 3D, *F* ∝ 1/r²; in 2D, *F* ∝ 1/r.

Three things are required for this argument to run:

1. **Area scaling.** *S*/*A* must be a finite number — the entropy is proportional to the *area* of the horizon, not its volume. (In 2D, "area" means length of a 1D curve.)
2. **Locality.** The entropy is attached to the horizon itself, not to the bulk on either side. It is a property of the surface.
3. **Universality.** Every horizon, regardless of where in the lattice it is or what it bounds, carries the same coefficient ζ.

Two things are *not* required:
- A specific microscopic mechanism. Jacobson's argument is about the existence and scaling of the entropy, not about what physical degrees of freedom carry it.
- The exact value of ζ. Any positive ζ gives Einstein's equations, just with a different effective Newton's constant. The specific value ζ = 1/4 is needed for the *correct numerical strength* of gravity, but the *force law itself* (1/r in 2D, 1/r² in 3D) is an inevitable consequence of the area scaling.

So our task is twofold: (i) show that the cylinder primitive's lattice supports an entropy with area scaling, and (ii) compute the coefficient and compare to ζ = 1/4. Goal (i) is the *scaling* question; goal (ii) is the *coefficient* question.

---

## 2. The starting hypothesis — topological defects, and why we look more carefully

The natural first guess for what supplies the entropy is **topological vortex defects** in the 2D stress vector field.

The reasoning: the cylinder primitive's state at each cross-section is a 2D vector ψ ∈ ℝ². The map ψ : (lattice) → ℝ² has nontrivial homotopy when the origin is excluded — π₁(ℝ² \\ {0}) = ℤ — so there are integer-winding vortices wherever the field passes through zero with non-trivial circulation around it. In thermal equilibrium on a 2D field of this type, vortex–antivortex pairs proliferate, and their configurational entropy (positions, signs, orientations) supplies a per-area entropy. This is the standard 2D XY-model story (Berezinskii–Kosterlitz–Thouless physics), and it gives entropy proportional to area in the unbound regime — exactly what Jacobson needs.

This is the picture that motivated theory 7 of [README.md](README.md). It is plausible. But before working through the BKT calculations, two observations should make us look more carefully:

**Observation 1 — the cylinder primitive is linear.** The wave equations of chapter 2 are linear in (ψ_R, ψ_I); the field can pass through zero smoothly without any energy cost beyond the local elastic cost. There is no Mexican-hat potential V(|ψ|), no constraint |ψ| = const. Vortex defects, as topological objects with protection from smooth deformation, require either a constraint (XY model) or a potential that suppresses ψ = 0 (Higgs-like). Without one of these, the field's zeros are *coordinate singularities of polar parameterization*, not topologically protected defects. They can untie themselves through ψ = 0 by smooth deformation.

**Observation 2 — we have a Laplacian.** Chapter 2 §3 worked out that the wave equation for the cylinder primitive is *D* ∂_t² **u** = *M* ∂_x² **u**, with both *D* and *M* positive-definite. In static equilibrium (∂_t = 0), this reduces to ∇² **u** = 0 — each component of ψ independently satisfies the 2D Laplace equation. The 2D Laplacian Green's function is logarithmic, and a log potential is exactly what gives a 1/r force in 2D.

The second observation suggests that the *linear* theory may already produce 1/r scaling, without needing the topological-defect machinery to get there. If so, the entropy story would not be about defects at all — it would be about ordinary Gaussian thermal fluctuations of a field with a log Green's function.

This is worth working out carefully before committing to the BKT picture. We do that in §3–§7.

---

## 3. The 2D Laplacian Green's function

The Green's function *G*(**x**, **x**₀) of the 2D Laplacian solves

∇² *G*(**x**, **x**₀) = δ²(**x** − **x**₀)

— the response at point **x** to a unit point source at **x**₀. By translation symmetry it depends only on the separation *r* = |**x** − **x**₀|, and by rotational symmetry only on its magnitude.

To find *G*(*r*), integrate ∇²*G* = δ²(**x**) over a disk of radius *r* centered at the source. The right-hand side integrates to 1 (the source has unit weight). The left-hand side, by the divergence theorem, becomes the flux of ∇*G* through the boundary circle:

<!-- ∮ (∂G/∂r) dl = 2πr · (∂G/∂r) -->
$$
\oint \frac{\partial G}{\partial r}\, d\ell \;=\; 2\pi r \cdot \frac{\partial G}{\partial r} \;=\; 1
$$

so

∂*G*/∂*r* = 1/(2π *r*)

Integrating once with respect to *r*:

<!-- G(r) = (1/2π) log(r) + const -->
$$
G(r) = \frac{1}{2\pi}\log r + \text{const}
$$

The constant is fixed by boundary conditions. In an infinite plane, *G* diverges logarithmically at infinity — a feature of 2D, not a bug, and unavoidable for any massless scalar field there. On a finite domain with Dirichlet boundary at radius *R*, the constant is fixed so *G*(*R*) = 0:

<!-- G(r) = (1/2π) log(r/R) -->
$$
G(r) = \frac{1}{2\pi}\log\frac{r}{R}
$$

— a logarithmic profile that goes from negative values near the source (where *r* is small and log(*r*/*R*) is large negative) to zero at the boundary. Equivalently, the field above a uniform background satisfying the Laplace equation in a domain with a localized inhomogeneity decays as log(*R*/*r*) from the inhomogeneity.

This is the Green's function. Anything that satisfies ∇²ψ = 0 in equilibrium with a localized source carries this logarithmic profile.

---

## 4. The cylinder primitive in equilibrium satisfies the 2D Laplace equation

The cylinder primitive, when assembled into a 2D lattice and brought to static equilibrium, has its stress vector field satisfy this same Laplace equation. The argument is short.

Chapter 2 derived the wave equations for a single cylinder:

*D* ∂_t² **u** = *M* ∂_x² **u**

where **u** = (ψ_R, ψ_I), *D* is the 2 × 2 inertia matrix, and *M* is the 2 × 2 stiffness matrix. Generalizing to a 2D lattice — bonds in both *x* and *y* directions — the equation becomes (with the same *M* on every bond):

*D* ∂_t² **u** = *M* (∂_x² + ∂_y²) **u** = *M* ∇² **u**

In static equilibrium, ∂_t² **u** = 0, so:

*M* ∇² **u** = 0

Because *M* is positive-definite (the stability requirement of chapter 2 §6), it is invertible. Multiply both sides by *M*⁻¹:

∇² **u** = 0

Each component of **u** independently satisfies the 2D Laplace equation. The off-diagonal coupling *K_eφ* — the chiral shear that was so central to chapter 2's wave dynamics — drops out of the static problem entirely.

This is a substantive structural result. The static behavior of the cylinder primitive on a 2D lattice is the same as the static behavior of a free 2D scalar field, regardless of the value of the chiral shear χ̃. Two corollaries follow.

**Corollary A.** A localized inclusion (a region pinned to a non-zero ψ) creates a field that decays from the inclusion as log(*r*) from §3's Green's function. The decay is independent of which polarization the inclusion is pinned to, and independent of χ̃.

**Corollary B.** Two such inclusions interact through the field, with an interaction energy that depends logarithmically on their separation — and a force F = −d*E*/d*r* that scales as 1/*r*. We derive this in §5.

---

## 5. From log potential to 1/r force law

If the field around an inclusion is ψ(*r*) = *q* · *G*(*r*) = (*q*/2π) log(*R*/*r*) for some "charge" *q*, the gradient is

∂ψ/∂*r* = −*q*/(2π *r*)

— a 1/*r* radial dependence. For two inclusions with charges *q*₁ and *q*₂ at separation *r*, the interaction energy in the absence of boundary effects is

*E*_int(*r*) = (*q*₁ *q*₂ / 2π) · log(*r*/*r*₀)

where *r*₀ is a reference scale (set by the inclusion size or the lattice spacing). The force is

*F*(*r*) = −d*E*_int/d*r* = ∓ *q*₁ *q*₂ / (2π *r*)

— magnitude scaling as 1/*r*, the 2D analog of the gravitational and Coulomb force law. The sign depends on the sign of the product *q*₁ *q*₂ and on the boundary-condition convention; the *scaling* is 1/*r* regardless. This is the central derivation result.

The 1/*r* force law is a generic consequence of the 2D Laplacian Green's function being logarithmic — nothing more. It does not depend on chirality, on temperature, or on whether the field has topological defects. It is a feature of any 2D field whose static equilibrium satisfies the Laplace equation.

For 3D, the same calculation gives *G*(*r*) ∝ 1/*r* (rather than log *r*), and the force law is 1/*r*² — Newton's gravitational and Coulomb's electrostatic force in their familiar form. The cylinder primitive in a 3D lattice would generalize automatically.

---

## 6. Thermal fluctuations and the variance shadow

The static result of §4–§5 is the energy/Green's function part of the story. For Jacobson's argument we need the *entropic* part: the per-area entropy of fluctuations on the lattice.

For a Gaussian field with a quadratic energy, finite-temperature fluctuations are exactly Gaussian and the propagator (the two-point correlation function) is *T* times the Green's function:

<u_i u_j> = T · G_ij

where *G*_ij is the discrete Green's function of the energy operator (the lattice version of the inverse Laplacian) restricted to the free sites. In particular, the diagonal *G*_ii is the variance of fluctuations at site *i*:

var(*u*_i) = T · *G*_ii

For the bulk lattice with no inclusion, *G*_ii is the bulk (translation-invariant) value, identical at every site. With a pinned inclusion, the Dirichlet boundary at the inclusion suppresses fluctuations nearby — *G*_ii is reduced — and the suppression follows the same logarithmic profile as the mean field:

var(*u*_i) ≈ var_bulk − (*T*/2π) · log(*R*/*r*_i)

where *r*_i is the distance from the inclusion. Fluctuations are reduced near the inclusion and recover logarithmically toward bulk at large distance. We call this pattern the **variance shadow**.

The entropic interpretation: variance is, for a Gaussian field, monotonically related to the entropy of fluctuations. A site with smaller variance has fewer accessible field configurations — lower local entropy. The variance shadow is an *entropy shadow*: the inclusion casts a logarithmic shadow of reduced entropy in the surrounding lattice.

For the connection to Jacobson's argument: pick any closed curve (a horizon-analog) that surrounds the inclusion. The *flux* of variance — the integrated entropy deficit along the curve — is, by the same Green's function logic, a function of the curve's length and its distance from the inclusion. For a curve of length *ℓ* at average distance *r*_avg from the inclusion, the entropy deficit is approximately *ℓ* · (*T*/2π) · (some function of *r*_avg). Crucially, it scales linearly with *ℓ* at leading order: this is the *area scaling* (1D-area scaling, since 2D horizons are curves) that Jacobson's argument requires.

So the cylinder primitive's lattice does support an entropy account with linear-in-area scaling. The mechanism is not topological defects; it is ordinary Gaussian fluctuations of a linear field with a logarithmic Green's function.

---

## 7. What three independent simulation tests confirm

The derivation of §3–§6 is paper-and-pencil; it predicts logarithmic field decay, logarithmic variance shadow, and a 1/*r* force law for like-pinned inclusions. To confirm that the lattice's discrete behavior agrees with the continuum prediction, three numerical tests have been run; they live in [scripts/](scripts/).

**Test 1 — Static field decay** ([sim-defect-gravity.py](scripts/sim-defect-gravity.py)). On a 121 × 121 lattice with a circular inclusion at the center pinned to ψ = (1, 0), solve the discrete Laplace equation and measure |ψ(*r*)| versus distance from the center. The result: |ψ(*r*)| ≈ 1.451 − 0.348 · log(*r*) with *R*² = 0.99997, beating the power-law alternative (*R*² = 0.89). Logarithmic decay confirmed at the percent level.

**Test 2 — Thermal entropy shadow** ([sim-entropy-shadow.py](scripts/sim-entropy-shadow.py)). On a 121 × 121 lattice at temperature *T* = 1, run heat-bath Monte Carlo and accumulate ⟨ψ⟩ and var(ψ) over thousands of sweeps. Both the mean field and the variance show logarithmic radial decay, with the variance increasing logarithmically away from the inclusion as predicted (positive log-slope, matching the variance-shadow recovery), and the mean field log-slope matching the static result within MC noise. Entropy shadow confirmed.

**Test 3 — Two-body force law** ([sim-two-body.py](scripts/sim-two-body.py)). On a 241 × 241 lattice, sweep separations *r* between two pinned inclusions and compute the interaction energy *E*_int(*r*) directly (cleanly subtracting self-energies). For like-charge inclusions, *E*_int(*r*) ≈ −1.10 + 0.195 · log(*r*) with *R*² = 0.989, and the diagnostic *r* · *F*(*r*) approaches a constant value (variation 7.6% in the asymptotic regime). 1/*r* force law confirmed.

Three independent measurements converge on the prediction of §3–§6: the cylinder primitive's static and thermal behavior on a 2D lattice produces the logarithmic Green's function structure and the 1/*r* force scaling that Jacobson's argument requires for entropic gravity in 2D.

---

## 8. The coefficient question — what is left for downstream work

The scaling question has been settled — both by derivation and by simulation. The coefficient question is more delicate.

The simulation result for the static field is |ψ(*r*)| ≈ 1.451 − 0.348 · log(*r*) (test 1). The continuum prediction for an inclusion of radius *a* in a box of outer radius *R* is

|ψ(*r*)| = log(*R*/*r*) / log(*R*/*a*)

with slope d|ψ|/d(log *r*) = −1/log(*R*/*a*). For the simulation parameters *a* ≈ 4 and *R* ≈ 60 (the lattice half-width), log(*R*/*a*) = log 15 ≈ 2.71, giving a predicted slope of ≈ −0.37. The measured slope of −0.348 matches at the few-percent level — the discrete-lattice and finite-box corrections are small but real.

This confirms the *form* of the response. To match the *coefficient* in Jacobson's expression (the per-area entropy ζ = 1/4), several normalizations have to be tracked carefully:

- The cylinder primitive's stiffness scales must be matched to the lattice cadence *c* (chapter 3).
- The "area" in *S* = ζ · *A* is in lattice units (Planck areas in GRID); the Gaussian-fluctuation entropy is in ordinary thermodynamic units. Converting between them requires a specific identification.
- The geometric prefactor 1/(2π) in the Green's function combines with the lattice geometry to produce the dimensionless coefficient.

This bookkeeping is non-trivial. It is where the *value* ζ = 1/4 derived from cell geometry in [grid/foundations.md](../../grid/foundations.md) §A5 has to be matched against the cylinder primitive's continuum coefficient. We do not carry it out in this chapter; it is a substantial calculation in its own right and belongs in the chapter that builds the bridge to [grid/gravity.md](../../grid/gravity.md). The point this chapter establishes is that the *scaling* is right; the *coefficient* is a downstream calculation.

---

## 9. Where topological defects could still matter

Theory 7 originally asked whether topological vortex defects supply the entropy. The answer of §3–§7 is: not at the level of *scaling*. The linear theory's Gaussian fluctuations already produce the right structure, and topological defects — which are not topologically protected in the linear theory anyway — are not needed.

However, defects could still have a role.

**Coefficient corrections.** In the dense-defect regime of a constrained nonlinear sigma model (the 2D XY model), the entropy per area has both the Gaussian log-Green's-function part *and* a defect-density part. If the cylinder primitive is augmented with a Mexican-hat potential V(|ψ|) that suppresses ψ = 0 (or a hard constraint |ψ| = 1), defects become topologically protected and contribute additional entropy. Whether this contribution is necessary to match ζ = 1/4 exactly, or whether the linear-Gaussian theory already gets it right, is a coefficient question for §8's downstream calculation.

**Charge emergence.** [grid/charge-emergence.md](../../grid/charge-emergence.md) speculates that charge is associated with topological winding around closed surfaces in the lattice. If the cylinder primitive is to support such windings, the topological-defect structure of the field becomes load-bearing for chapter 8 (the α derivation) — even if it is not load-bearing for the entropy account here.

**Refinements at lattice scale.** The Gaussian theory of §3–§6 is valid in the long-wavelength, weak-fluctuation regime. At lattice-scale or in strong-fluctuation regimes, the linear approximation fails and topological defects may dominate. Whether the cylinder primitive operates in the linear regime or beyond it is set by the temperature and the stiffness scales.

The conclusion is that defects remain in the picture as a *refinement* — not as the engine of the entropy account, but as a possible contributor to the coefficient and as a structural element required for the charge story of chapter 8. Theory 7 of [README.md](README.md) should be updated to reflect this: the load-bearing entropy mechanism is the linear theory's Gaussian fluctuations; topological defects are a downstream refinement.

---

## 10. Summary of givens

The cylinder primitive's contribution to the entropy account, as established in this chapter:

- In static equilibrium on a 2D lattice, each component of the stress vector field satisfies the 2D Laplace equation. The chiral coupling *K_eφ* drops out of the static problem.
- The 2D Laplacian Green's function is logarithmic: *G*(*r*) = (1/2π) log(*R*/*r*), with the field around any localized inclusion decaying as log(*r*) and the gradient as 1/*r*.
- Two pinned inclusions interact with energy *E*_int(*r*) ∝ log(*r*) and a force *F*(*r*) ∝ 1/*r*. This is the 2D analog of gravity's 1/*r*² force law in 3D.
- At finite temperature, Gaussian fluctuations have variance *T* · *G*, producing a logarithmic *variance shadow* around any pinned inclusion. The flux of variance through any horizon-analog curve scales linearly with the curve's length — the area scaling that Jacobson's argument requires.
- Three independent simulation tests confirm the predictions: static field decay, thermal variance shadow, and direct two-body force-vs-separation measurements all show logarithmic structure and 1/*r* force at the percent level.
- The *scaling* matches Jacobson's requirement; the cylinder primitive on a 2D lattice supplies the entropic structure for theory 7. The *coefficient* ζ = 1/4 is a downstream calculation requiring careful normalization between the cylinder primitive's symbolic constants and the lattice geometry.
- Topological vortex defects — the original hypothesis for the entropy mechanism — are not needed for the scaling. They remain in the picture as a possible refinement for the coefficient and as a structural element for the charge derivation of chapter 8.

The next chapter takes up the assembly of cylinder primitives into a 2D periodic lattice and establishes the framework for the Maxwell-bridge and α-derivation chapters that follow.
