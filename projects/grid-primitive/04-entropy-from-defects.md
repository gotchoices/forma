# Chapter 4 — The Entropy Account

This chapter takes up the load-bearing question of [README.md](README.md)'s theory 7:

> *Does the cylinder primitive's stress vector field on a 2D lattice supply the entropy that Jacobson's argument requires for the lattice to produce 1/r gravity?*

The chapter started life expecting that the answer would have to come from topological vortex defects in the field — that entropy would be packed into the discrete winding-number invariants of vortex configurations in thermal equilibrium. As the math is worked out (and, alongside it, three direct simulation tests are run), a simpler picture emerges: the *linear* theory's ordinary thermal fluctuations already produce the entropic 1/r force scaling. Topological defects turn out to be a *refinement* — possibly required for the precise numerical coefficient — but they are not the source of the scaling.

We follow the discovery in the order the math reveals it.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | What Jacobson's argument requires from the entropy |
| 2 | The starting hypothesis — topological defects, and why we look more carefully |
| 3 | The 2D Laplacian Green's function — a derivation from the divergence theorem |
| 4 | The cylinder primitive in equilibrium satisfies the 2D Laplace equation |
| 5 | From a logarithmic potential to a 1/r force law |
| 6 | Thermal fluctuations and the variance shadow |
| 7 | What three independent simulation tests confirm |
| 8 | The coefficient question — what is left for downstream work |
| 9 | Where topological defects could still matter |
| 10 | Summary of givens |

---

## 1. What Jacobson's argument requires from the entropy

Before we can decide whether the cylinder primitive supplies "the right entropy," we need to be precise about what Jacobson's argument actually needs.

A condensed sketch of [grid/gravity.md](../../grid/gravity.md):

A **causal horizon** is a surface across which information can flow only one way — like the boundary of a black hole, but the construction works for any one-way surface in spacetime. Standard black-hole physics tells us that horizons carry an entropy proportional to their area:

*S* = ζ · *A*

with ζ a dimensionless coefficient. (In GRID, ζ = 1/4 — a value derived from cell geometry in axiom A5. The Bekenstein-Hawking formula gives the same value for black-hole horizons in the standard theory.)

Now combine this with thermodynamics. When heat δ*Q* flows across the horizon at temperature *T*, the entropy on the horizon changes by

δ*S* = δ*Q* / *T*

— the **Clausius relation**, familiar from any introductory thermodynamics course. Combined with the area-scaling of *S*, this means heat flow correlates with area change.

Jacobson's insight is that area changes of horizons in spacetime are determined by *spacetime curvature* — there is a precise geometric relationship between how a horizon's area changes as you move along it and the curvature of the spacetime around it. Plugging the entropy-area relation and the Clausius relation into this geometric statement gives, after some algebra (the technical part of the derivation, which we will not redo), Einstein's field equations. From Einstein's equations, the Newtonian limit gives the familiar gravitational force law: *F* ∝ 1/r² in 3D space, or *F* ∝ 1/r in 2D space.

The takeaway is the structure of the argument:

> *If the lattice has horizons that carry area-proportional entropy, gravity follows automatically.*

This means our task as primitive-builders is narrow. We need to show that the cylinder primitive's lattice supports an entropy account with two key features:

1. **Area scaling.** *S*/*A* must be a finite number — entropy proportional to area, not volume. (In 2D, "area" is the length of a 1D curve; that's the relevant "area" for a 2D-spacetime horizon.)
2. **Locality.** The entropy is attached to the horizon itself, not to the bulk of the field on either side of it.

Two things we *do not* need:

- **A specific microscopic mechanism.** Jacobson's argument is about the existence and scaling of entropy, not about which physical degrees of freedom carry it. Any mechanism that gives area-scaling local entropy will do.
- **The exact value of ζ.** Any positive ζ gives Einstein's equations, just with a different effective Newton's constant. The specific value ζ = 1/4 sets the *strength* of gravity, but the *force law itself* (1/r in 2D, 1/r² in 3D) is an inevitable consequence of area-scaling regardless of ζ.

So our task splits into two questions:

- **(i) Scaling.** Does the cylinder primitive's lattice support an entropy with area scaling? — what we will call the *scaling question*.
- **(ii) Coefficient.** Does the coefficient match ζ = 1/4? — the *coefficient question*.

This chapter settles (i) and identifies what is needed to settle (ii) downstream.

---

## 2. The starting hypothesis — topological defects, and why we look more carefully

The natural first guess for what supplies the entropy is **topological vortex defects** in the 2D stress vector field.

The reasoning, recalling chapter 1 §4: the cylinder primitive's state at each cross-section is a 2D vector ψ. As you trace a closed loop in (*x*, *t*) space, the stress vector rotates; the net rotation, divided by 2π, is an integer called the *winding number*. Around a point where the field passes through zero with non-trivial circulation — a *vortex* — the winding number is nonzero. Vortices come paired with antivortices (opposite winding); in thermal equilibrium they proliferate, and their configurational entropy (positions, signs, orientations) supplies a per-area entropy. This is the standard story for a 2D theory of this type, and it gives entropy proportional to area in the appropriate regime — exactly what Jacobson needs.

This was the picture motivating theory 7 of [README.md](README.md). It is plausible. But before working through the defect-statistics calculations, two observations should make us look more carefully.

**Observation 1 — the cylinder primitive is linear.** The wave equations of chapter 2 are linear in the field. In the Cartesian form (ψ_R, ψ_I), the field can pass through zero smoothly — there is no energy penalty for the magnitude vanishing at a point. Vortices can therefore *untie themselves* through ψ = 0 by smooth deformation; they are not topologically protected the way they would be in a constrained model where |ψ| is held fixed. Chapter 1 §4 made this distinction explicit: in the linear model, "vortices exist as configurations but are not robust." That undermines the standard defect-statistics story.

**Observation 2 — we already have a Laplacian.** Chapter 2 §2 derived the wave equation for the cylinder primitive: *D* ∂_t² **u** = *M* ∂_x² **u**. In *static* equilibrium (∂_t² **u** = 0), this reduces to *M* ∇² **u** = 0 — and since *M* is invertible (positive-definite, by chapter 2 §6), this is just ∇² **u** = 0, the standard 2D Laplace equation. That is the equation whose Green's function is logarithmic, and a logarithmic potential gives a 1/r force in 2D — exactly the scaling Jacobson's argument expects.

The second observation suggests a much simpler story: the *linear* theory may already produce 1/r scaling, without needing topological defects to do anything. If so, the entropy account is not about defects — it is about ordinary thermal fluctuations of a field whose Green's function is logarithmic.

This is worth working out carefully before committing to the defect picture. We do that in §3–§7.

---

## 3. The 2D Laplacian Green's function — a derivation from the divergence theorem

To make precise what "the field around an inclusion" looks like, we derive the *Green's function* of the 2D Laplacian.

A Green's function is the response of a linear field equation to a unit point source. Solve

∇² *G*(**x**, **x**₀) = δ²(**x** − **x**₀)

— the equation says: at every point in the plane, the Laplacian of *G* is zero, *except* at the source point **x**₀, where the right-hand side is a Dirac delta function (a spike of unit total weight, infinitely tall, infinitely narrow). The solution *G* is the field produced by injecting unit "charge" at **x**₀.

Why bother with a Green's function? Because once you know it, you know the response to *any* source distribution — you just convolve the source with *G*. The Green's function is the building block.

To find *G*(*r*) (using *r* = |**x** − **x**₀| as the distance from the source), we use rotational symmetry: by symmetry, *G* depends only on *r*, not on direction. Then we integrate the defining equation ∇² *G* = δ² over a disk of radius *r* centered at the source:

- The right-hand side integrates to 1 (the source has unit total weight).
- The left-hand side, by the **divergence theorem** (the 2D version: ∫ ∇²*G* d*A* = ∮ ∇*G* · *n̂* d*ℓ*, the integral of a Laplacian over a region equals the flux of the gradient through the region's boundary), becomes the flux of ∇*G* through the boundary circle of radius *r*. Because *G* is radially symmetric, ∇*G* points radially outward with magnitude ∂*G*/∂*r*, and the boundary circle has circumference 2π*r*:

<!-- ∮ (∂G/∂r) dl = 2πr · (∂G/∂r) = 1 -->
$$
\oint \frac{\partial G}{\partial r}\, d\ell \;=\; 2\pi r \cdot \frac{\partial G}{\partial r} \;=\; 1
$$

so

∂*G*/∂*r* = 1/(2π *r*)

Integrating once with respect to *r*:

<!-- G(r) = (1/2π) log(r) + const -->
$$
G(r) = \frac{1}{2\pi}\,\log r + \text{const}
$$

That's the result: **the 2D Laplacian Green's function is logarithmic in *r***. The integration constant is fixed by the boundary conditions of whatever specific problem we are solving.

A quick consistency check on dimensions: log *r* is dimensionless if *r* is in some chosen length units, and the constant absorbs the choice of units. In an infinite plane, the value of *G* diverges logarithmically as *r* → ∞ — this is a well-known feature of 2D, not a bug, and is unavoidable for any massless scalar field there. On a finite domain with a Dirichlet boundary at radius *R* (where *G* = 0), the constant is fixed:

<!-- G(r) = (1/2π) log(r/R) -->
$$
G(r) = \frac{1}{2\pi}\,\log\frac{r}{R}
$$

This is a logarithmic profile that goes from large negative values near the source (where *r* is small and log(*r*/*R*) is large negative) to zero at the boundary. Equivalently, the field deviation from background, in a domain with a localized inhomogeneity, decays as log(*R*/*r*) from the inhomogeneity.

Anything that satisfies ∇²ψ = 0 with a localized source carries this logarithmic profile.

---

## 4. The cylinder primitive in equilibrium satisfies the 2D Laplace equation

The next step is to show that the cylinder primitive on a 2D lattice has its stress vector field satisfy this same Laplace equation in equilibrium. The argument is short, but it requires being careful about which coordinates we work in.

### A note on coordinates: linearization around a non-zero background

Chapters 1–2 set up the cylinder primitive with two fields *e(x, t)* (stress magnitude) and *φ(x, t)* (azimuthal direction), parameterizing a 2D internal stress vector ψ in polar form. Chapter 2's wave equation *D* ∂_t² **u** = *M* ∂_x² **u** with **u** = (*e*, *φ*)ᵀ is the small-perturbation linearization in those polar coordinates. For a polar linearization to be well-defined the background magnitude must be non-zero — there must be some equilibrium ψ₀ with |ψ₀| ≠ 0 around which the small fluctuations (δ*e*, δ*φ*) are taken. (At ψ₀ = 0 the polar parameterization is singular and the linear theory in (*e*, *φ*) does not apply.)

For this chapter's analysis we therefore *assume* such a background is present — a state in which the lattice carries a non-zero stress vector field — and work with small fluctuations around it. This is the natural regime: a localized inclusion (the next paragraph's setup) is precisely a place where ψ takes a definite non-zero value, so the surrounding lattice acquires a non-zero stress-vector field, and small-fluctuation analysis around that field is well-defined.

Around such a background, polar fluctuations (δ*e*, δ*φ*) and Cartesian fluctuations (δψ_R, δψ_I) are related by a fixed linear transformation (the tangent-space basis change at ψ₀):

δψ_R = cos(φ₀)·δ*e* − e₀ sin(φ₀)·δ*φ*,  δψ_I = sin(φ₀)·δ*e* + e₀ cos(φ₀)·δ*φ*

Because this is a linear change of basis, the linear wave equation transforms covariantly: the matrix *M* in the (*e*, *φ*) basis becomes some matrix *M*' in the (ψ_R, ψ_I) basis (and similarly *D* → *D*'), with *M*' positive-definite iff *M* is. **The static-Laplacian argument does not depend on which basis we use** — *M*' is invertible iff *M* is, so multiplying the static equation *M*' ∇²**u**' = 0 by (*M*')⁻¹ gives ∇²**u**' = 0 component-wise, exactly as in (*e*, *φ*).

For the rest of this chapter we therefore work in whichever basis is more convenient. The simulations in §7 use the Cartesian basis (pinning ψ = (1, 0) at an inclusion is exactly the kind of non-zero background the linearization needs); the analytical arguments are basis-independent.

### The static Laplacian

Generalizing chapter 2's 1D wave equation to a 2D lattice — bonds going both in the *x* direction and the *y* direction, each carrying the same stiffness *M* — the equation becomes:

*D* ∂_t² **u** = *M* (∂_x² + ∂_y²) **u** = *M* ∇² **u**

(Here ∇² = ∂_x² + ∂_y² is the 2D Laplacian; we treat the lattice in its long-wavelength continuum limit for this argument. **u** is the 2-component fluctuation field — either (δ*e*, δ*φ*) or (δψ_R, δψ_I) — at every spatial point.)

In static equilibrium, the time-derivative term vanishes:

*M* ∇² **u** = 0

Now multiply both sides by *M*⁻¹ from the left. *M* is invertible because it is positive-definite (chapter 2 §6 — stability requires this). The result is

∇² **u** = 0

— each component of **u** independently satisfies the 2D Laplace equation. The chiral coupling *K_eφ*, which was central to chapter 2's *wave* dynamics, drops out of the *static* problem entirely.

This is a substantial structural result. The static behavior of the cylinder primitive on a 2D lattice is the same as the static behavior of a free 2D scalar field — regardless of the value of the chiral shear χ̃. Two consequences follow.

**Consequence A.** A localized inclusion (a region of the lattice pinned to a fixed nonzero ψ) creates a field that decays from the inclusion as log(*r*) — the Green's function of §3. The decay is independent of which polarization the inclusion is pinned to, and independent of χ̃.

**Consequence B.** Two such inclusions interact through the field, with an interaction energy that depends logarithmically on their separation — and a force *F* = −d*E*/d*r* that scales as 1/r. We derive this in §5.

---

## 5. From a logarithmic potential to a 1/r force law

If the field around a single inclusion is

ψ(*r*) = *q* · *G*(*r*) = (*q* / 2π) · log(*R*/*r*)

— a *q*-weighted version of §3's Green's function, where *q* is the inclusion's "charge" (the strength of the source) and *R* is the outer-boundary radius — then the spatial gradient is

∂ψ/∂*r* = −*q* / (2π *r*)

— a 1/r radial dependence. For two inclusions with charges *q*₁ and *q*₂ at separation *r*, the interaction energy is, in the absence of boundary effects,

*E*_int(*r*) = (*q*₁ *q*₂ / 2π) · log(*r* / *r*₀)

where *r*₀ is a reference scale (typically set by the inclusion size or the lattice spacing). This expression is just *q*₁ multiplied by the field that *q*₂ produces at *q*₁'s location — the standard "charge times field" interaction-energy formula.

The force between the two inclusions is the negative gradient of this energy with respect to separation:

*F*(*r*) = − d*E*_int/d*r* = ∓ *q*₁ *q*₂ / (2π *r*)

— magnitude scaling as 1/r. This is the **2D analog of the gravitational and Coulomb force law**. The sign depends on the product *q*₁ *q*₂ and on the boundary-condition convention; what is universal is the 1/r scaling.

That is the central derivation of the chapter: the 1/r force law is a generic consequence of the 2D Laplacian Green's function being logarithmic. It does not depend on chirality (M dropped out at static), on temperature, or on whether the field has topological defects. It is a feature of any 2D field whose static equilibrium satisfies the Laplace equation.

For 3D, the same calculation gives *G*(*r*) ∝ 1/*r* (rather than log *r*), and the force law becomes 1/r² — Newton's gravitational and Coulomb's electrostatic force in their familiar form. The cylinder primitive in a 3D lattice would generalize automatically.

---

## 6. Thermal fluctuations and the variance shadow

The §4–§5 result handles the *static* energy/Green's-function part of the entropy story. For Jacobson's argument we also need the *thermal* part — the per-area entropy of fluctuations on the lattice.

Recall how thermal physics works for a quadratic energy. If the energy is a quadratic function of the field — which it is, by chapter 2 §1 — then in thermal equilibrium at temperature *T*, every quadratic mode of the field carries average energy *kT*/2 (the equipartition theorem). The fluctuations are Gaussian: their statistics are completely characterized by their two-point correlation function. And that correlation function is *T* times the Green's function of the energy operator:

⟨ψ(*x*) ψ(*x*′)⟩ = *T* · *G*(*x*, *x*′)

This is a standard result for any quadratic-energy ("Gaussian") field theory at finite temperature. The factor of *T* is the strength of the thermal noise; *G* is the same Green's function from §3.

The variance of the field at any single site is the diagonal of this correlation function:

var(ψ(*x*)) = *T* · *G*(*x*, *x*)

For the bulk lattice with no inclusion present, *G*(*x*, *x*) is a position-independent constant (translation symmetry); the variance is the same at every site, equal to some bulk value var_bulk. With a pinned inclusion present, however, the inclusion enforces ψ = (constant) on its sites — a Dirichlet boundary condition. This *suppresses fluctuations* near the inclusion: a site near the pin has fewer accessible field configurations because nearby sites are partly constrained, and the variance is reduced. Far from the inclusion, the variance recovers to the bulk value.

The shape of the recovery follows from the same Green's function logic. With a pinned inclusion of size *a* at the center and a Dirichlet outer boundary at radius *R*, the variance at distance *r* from the inclusion is approximately

var(ψ(*r*)) ≈ var_bulk − (*T* / 2π) · log(*R* / *r*)

— reduced near the inclusion, recovering logarithmically toward bulk at large distance. We call this pattern the **variance shadow**: the inclusion casts a logarithmic shadow of reduced variance in the surrounding lattice.

The entropic interpretation is direct. For a Gaussian field, variance and entropy of fluctuations are monotonically related — a site with smaller variance has fewer accessible field configurations, lower local entropy. So the variance shadow is also an **entropy shadow**: the inclusion casts a logarithmic shadow of reduced entropy.

Now to the connection to Jacobson's argument. Pick any closed curve on the lattice (a horizon-analog) that surrounds the inclusion. We can integrate the entropy deficit along this curve. The deficit at any point on the curve is determined by the curve's distance from the inclusion (via the log profile above). For a curve of length *ℓ*, the *integrated* entropy deficit scales with the curve's length, plus a slowly varying logarithmic dependence on its average distance from the inclusion. To leading order, the integrated deficit is **linear in *ℓ*** — the *area scaling* (1D-area scaling, since 2D horizons are curves) that Jacobson's argument requires.

So the cylinder primitive's lattice does support an entropy account with linear-in-area scaling. The mechanism is not topological defects; it is ordinary thermal fluctuations of a linear field whose Green's function is logarithmic.

---

## 7. What three independent simulation tests confirm

The derivation of §3–§6 is paper-and-pencil. It predicts logarithmic field decay, logarithmic variance shadow, and a 1/r force law for like-pinned inclusions. To confirm that the discrete lattice's actual behavior agrees with the continuum prediction, three numerical tests have been run in [scripts/](scripts/).

**Test 1 — Static field decay** ([sim-defect-gravity.py](scripts/sim-defect-gravity.py)). On a 121 × 121 lattice with a circular inclusion at the center pinned to ψ = (1, 0), solve the discrete Laplace equation and measure |ψ(*r*)| versus distance from the center. The result:

|ψ(*r*)| ≈ 1.451 − 0.348 · log(*r*),    *R*² = 0.99997

The logarithmic fit is essentially perfect; the alternative power-law fit gives only *R*² = 0.89. Logarithmic decay confirmed at the percent level.

**Test 2 — Thermal entropy shadow** ([sim-entropy-shadow.py](scripts/sim-entropy-shadow.py)). On a 121 × 121 lattice at temperature *T* = 1, run heat-bath Monte Carlo and accumulate ⟨ψ⟩ and var(ψ) over thousands of sweeps. Both the mean field and the variance show logarithmic radial decay, with the variance increasing logarithmically away from the inclusion (positive log-slope, consistent with the variance-shadow recovery prediction) and the mean field log-slope matching the static result within Monte Carlo noise. Entropy shadow confirmed.

**Test 3 — Two-body force law** ([sim-two-body.py](scripts/sim-two-body.py)). On a 241 × 241 lattice, sweep the separation *r* between two pinned inclusions and compute the interaction energy *E*_int(*r*) directly (cleanly subtracting the position-dependent self-energies of each inclusion). For like-charge inclusions:

*E*_int(*r*) ≈ −1.10 + 0.195 · log(*r*),    *R*² = 0.989

The diagnostic *r* · *F*(*r*) — which would be a constant if *F* ∝ 1/r exactly — varies by only 7.6% across the asymptotic regime, confirming the 1/r force scaling.

Three independent measurements converge on the prediction of §3–§6: the cylinder primitive's static and thermal behavior on a 2D lattice produces the logarithmic Green's function structure and the 1/r force scaling that Jacobson's argument requires for entropic gravity in 2D.

---

## 8. The coefficient question — what is left for downstream work

The scaling question has been settled — both by derivation and by simulation. The *coefficient* question is more delicate.

The simulation result for the static field is |ψ(*r*)| ≈ 1.451 − 0.348 · log(*r*) (test 1). The continuum prediction for an inclusion of radius *a* in a box of outer radius *R* is

|ψ(*r*)| = log(*R*/*r*) / log(*R*/*a*)

— with slope d|ψ|/d(log *r*) = −1/log(*R*/*a*). For the simulation parameters *a* ≈ 4 and *R* ≈ 60 (the lattice half-width), log(*R*/*a*) = log 15 ≈ 2.71, giving a predicted slope of ≈ −0.37. The measured slope of −0.348 matches at the few-percent level — discrete-lattice and finite-box corrections are small but real.

This confirms the *form* of the response. To match the *coefficient* in Jacobson's expression *S* = ζ · *A* with ζ = 1/4, several normalizations need careful tracking:

- The cylinder primitive's stiffness scales must be matched to the lattice cadence *c* (chapter 3 partially does this).
- The "area" in *S* = ζ · *A* is in lattice units (Planck areas in GRID); the Gaussian-fluctuation entropy is in ordinary thermodynamic units. Converting between them requires a specific identification.
- The geometric prefactor 1/(2π) in the Green's function combines with the lattice geometry to produce a dimensionless coefficient that has to come out to ζ = 1/4.

This bookkeeping is non-trivial. It is the place where the *value* ζ = 1/4 (derived from cell geometry in [grid/foundations.md](../../grid/foundations.md) §A5) has to be matched against the cylinder primitive's continuum coefficient. We do not carry the calculation out in this chapter — it is a substantial calculation in its own right, and it belongs in the chapter that builds the bridge to [grid/gravity.md](../../grid/gravity.md). The point this chapter establishes is that the *scaling* is right; matching the *coefficient* is a downstream task.

---

## 9. Where topological defects could still matter

Theory 7 of [README.md](README.md) originally asked whether topological vortex defects supply the entropy. The answer of §3–§7 is: not at the level of *scaling*. The linear theory's thermal fluctuations already produce the right structure, and topological defects — which are not robust in the linear theory anyway, per chapter 1 §4 — are not needed for the scaling part.

However, defects could still play a role in three ways.

**Coefficient corrections.** In a constrained model where the field magnitude is held fixed (a nonlinear sigma model — for instance, the standard 2D XY model where ψ is forced to be a unit vector), defects become topologically protected and contribute additional entropy. The total entropy in such a model has both the Gaussian Green's-function part *and* a defect-density part. If the cylinder primitive is augmented with a potential that suppresses ψ = 0 (analogous to a Higgs-style "Mexican-hat" potential — a potential that has zero force at some preferred non-zero |ψ| and rises at both larger and smaller |ψ|), defects would re-enter the entropy account. Whether this contribution is necessary to match ζ = 1/4 exactly, or whether the linear-Gaussian theory already gets the coefficient right, is part of §8's downstream calculation.

**Charge emergence.** [grid/charge-emergence.md](../../grid/charge-emergence.md) proposes that charge is associated with topological winding around closed surfaces in the lattice. If the cylinder primitive is to support such windings, the topological-defect structure of the field becomes load-bearing for chapter 8 (the α derivation) — even though it is not load-bearing for the entropy account here.

**Refinements at lattice scale.** The Gaussian theory of §3–§6 is valid in the long-wavelength, weak-fluctuation regime — the regime where the linear approximation around small (ψ_R, ψ_I) is reliable. At lattice-scale or in strong-fluctuation regimes (large temperatures, where fluctuations push the field significantly away from zero), the linear approximation can fail and topological-defect effects may dominate. Whether the cylinder primitive operates in the linear regime or beyond it is set by the temperature and the stiffness scales.

The conclusion: defects remain in the picture as a *refinement* — not the engine of the entropy account, but a possible contributor to the coefficient and a structural element required for the charge story of chapter 8. Theory 7 of [README.md](README.md) reflects this: the load-bearing entropy mechanism is the linear theory's thermal fluctuations; topological defects are a downstream refinement.

---

## 10. Summary of givens

The cylinder primitive's contribution to the entropy account, as established in this chapter:

- In static equilibrium on a 2D lattice, each component of the stress vector field independently satisfies the 2D Laplace equation. The chiral coupling *K_eφ* drops out of the static problem (the matrix *M* is invertible, so it factors out).
- The 2D Laplacian Green's function is logarithmic: *G*(*r*) = (1/2π) log(*R*/*r*). The field around any localized inclusion decays as log(*r*); the gradient as 1/r.
- Two pinned inclusions interact with energy *E*_int(*r*) ∝ log(*r*) and a force *F*(*r*) ∝ 1/r — the 2D analog of gravity's 1/r² force law in 3D.
- At finite temperature, ordinary Gaussian fluctuations have variance *T* · *G*, producing a logarithmic *variance shadow* (and equivalently, an *entropy shadow*) around any pinned inclusion. Integrating the entropy deficit along any horizon-analog curve scales linearly with the curve's length — the area scaling that Jacobson's argument requires.
- Three independent simulation tests confirm the predictions: static field decay, thermal variance shadow, and direct two-body force-vs-separation measurements all show logarithmic structure and 1/r force at the percent level.
- The *scaling* matches Jacobson's requirement; the cylinder primitive on a 2D lattice supplies the entropic structure for theory 7. The *coefficient* ζ = 1/4 is a downstream calculation requiring careful normalization between the cylinder primitive's symbolic constants and the lattice geometry.
- Topological vortex defects — the original hypothesis for the entropy mechanism — are not needed for the scaling. They remain in the picture as a possible refinement for the coefficient and as a structural element for the charge derivation of chapter 8.

The next chapter takes up the assembly of cylinder primitives into a 2D periodic lattice and establishes the framework for the Maxwell-bridge and α-derivation chapters that follow.
