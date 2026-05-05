# Chapter 2 — Wave on a Single Primitive

This chapter takes the foundation established in [01-foundation.md](01-foundation.md) — a cylinder with two coupled fields *e(x, t)* and *φ(x, t)* and a stiffness matrix *M* — and derives the wave dynamics on a single primitive. The goal is to characterize the propagating modes, locate the stability boundary, identify the natural value of the shear, and prove that the medium propagates waves symmetrically in both directions despite its chirality.

The math runs through coupled second-order PDEs, an eigenvalue problem, and a dispersion relation. None of it requires more than calculus and 2 × 2 matrix algebra; we go step by step and motivate each stage with a mechanical analog where one helps.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The cylinder's energy: kinetic and elastic |
| 2 | Equations of motion from Newton's law on a slice |
| 3 | Looking for wave solutions: the sinusoidal trial |
| 4 | Two propagation speeds: the dispersion relation |
| 5 | The two natural modes: how strain and direction combine |
| 6 | Stability boundary and the degenerate limit χ̃ → 1 |
| 7 | The natural shear value χ̃ = 1/√2 |
| 8 | Left-going and right-going waves travel at equal speeds |
| 9 | Linear superposition: pulses pass through each other |
| 10 | Summary of givens |

---

## 1. The cylinder's energy: kinetic and elastic

The cleanest starting point for working out how the cylinder moves is its *energy* at each position along its length. A cylinder primitive of length *L* has two fields varying with position *x* and time *t*: the stress magnitude *e(x, t)* and the azimuthal direction *φ(x, t)* (chapter 1 §3). Each contributes kinetic energy when it moves in time and elastic potential energy when it varies in space.

We work with energy *per unit length* of cylinder (an energy *density*) and integrate along the cylinder to get the total. Two contributions, each familiar from undergraduate mechanics.

### Kinetic density

When the fields change in time, they carry kinetic energy of the standard "(½) × inertia × velocity²" form:

<!-- T̃ = (1/2) ρ (∂_t e)² + (1/2) I_φ (∂_t φ)² -->
$$
\widetilde{T} = \tfrac{1}{2}\rho\,(\partial_t e)^2 + \tfrac{1}{2} I_\varphi\,(\partial_t \varphi)^2
$$

Each term is just *(½ × inertia × velocity²)* per unit length, applied to each field separately. The two coefficients are the relevant "inertias":

- ρ — the **longitudinal mass density** of the cylinder (mass per unit length, kg/m for an actual rod). This is what resists changes in *e*.
- *I_φ* — the **rotational moment of inertia per unit length**. For a real elastic rod of cross-section radius *r*, *I_φ* would scale roughly as (mass per length) × *r*². It is what resists changes in the azimuthal direction *φ*.

Both ρ and *I_φ* are real material constants of the primitive. We do not commit to a relation between them at this stage; if a later chapter forces one, it will be flagged explicitly.

### Elastic potential density

When the fields *vary* in space along the cylinder, the cylinder stores elastic energy — the same way stretching a spring stores energy. The relevant deformation here is the spatial *gradient* (∂_x e, ∂_x φ): if neither field varies along *x*, no elastic energy is stored. The energy cost of variation depends on the cylinder's stiffness:

<!-- Ṽ = (1/2)[K_ee (∂_x e)² + 2 K_eφ (∂_x e)(∂_x φ) + K_φφ (∂_x φ)²] -->
$$
\widetilde{V} = \tfrac{1}{2}\!\left[\,K_{ee}(\partial_x e)^2 + 2 K_{e\varphi}(\partial_x e)(\partial_x \varphi) + K_{\varphi\varphi}(\partial_x \varphi)^2\right]
$$

This same expression in compact matrix form, using the stiffness matrix *M* introduced in chapter 1 §6:

<!-- Ṽ = (1/2) (∂_x e, ∂_x φ) M (∂_x e, ∂_x φ)^T -->
$$
\widetilde{V} = \tfrac{1}{2}
\begin{pmatrix} \partial_x e & \partial_x \varphi \end{pmatrix}
M
\begin{pmatrix} \partial_x e \\ \partial_x \varphi \end{pmatrix}
$$

Reading the components:

- *K_ee* and *K_φφ* (the diagonal entries of *M*) are the "self-stiffnesses" — what would happen if each field were on its own. They behave like spring constants: the bigger they are, the more energy a gradient costs.
- *K_eφ* (the off-diagonal entry) is the *coupling* between the two fields. If *K_eφ* = 0, the two terms involving *K_ee* and *K_φφ* are independent — the cylinder would behave like two parallel, unrelated springs. If *K_eφ* > 0, a gradient in *e* and a gradient in *φ* affect each other through the cross term, like two springs with cross-bracing between them.

The chiral coupling introduced in chapter 1 §7 is exactly this *K_eφ* — what makes the cylinder a wave-supporting medium rather than two decoupled springs.

The cylinder's total energy at any instant is the integral of the two densities:

E_total(*t*) = ∫₀^*L* (T̃ + Ṽ) d*x*

Together, ρ, *I_φ*, *K_ee*, *K_φφ*, and *K_eφ* are the five symbolic constants that parameterize all the cylinder's mechanics. The next section uses this energy to derive the equations of motion.

A brief note on terminology. In classical mechanics, the combination *L̃* = *T̃* − *Ṽ* is called the **Lagrangian density**, and there is a general procedure (the Euler–Lagrange equations) for deriving equations of motion from any Lagrangian. We do not need to invoke the procedure abstractly — Newton's second law applied directly to a small slice of cylinder gives the same equations of motion, more transparently. We do that next.

---

## 2. Equations of motion from Newton's law on a slice

To find how the cylinder evolves in time, take a small slice of cylinder of width d*x* at position *x* and apply Newton's second law to it. There are two fields on the slice (*e* and *φ*), so we write a separate Newton equation for each. The argument is a routine continuum-mechanics calculation, the same one used to derive the wave equation for a stretched string.

### Equation for *e*

The slice has linear mass ρ d*x* attached to the longitudinal coordinate *e*. The mass times its acceleration ∂_t² *e* is the inertial term:

(inertial force on slice) = ρ d*x* · ∂_t² *e*

The elastic force on the slice comes from the *difference* in internal stress at the two ends of the slice. Reading off the elastic potential Ṽ from §1, the *e*-channel internal stress at any cross-section *x* is

σ_e(*x*, *t*) = *K_ee* (∂_x e) + *K_eφ* (∂_x φ)

— the sum of the field's own gradient times its self-stiffness, plus a cross-coupling contribution from the other field's gradient. This is just the engineer's "stress equals stiffness times strain," generalized to a chirally-coupled medium.

The net force on the slice is the difference between σ_e at *x* + d*x* and at *x*:

(net elastic force) = σ_e(*x* + d*x*) − σ_e(*x*) = (∂_x σ_e) · d*x* = [*K_ee* (∂_x² *e*) + *K_eφ* (∂_x² *φ*)] · d*x*

Setting the inertial force equal to the net elastic force and dividing through by d*x*:

<!-- ρ ∂_t² e = K_ee ∂_x² e + K_eφ ∂_x² φ -->
$$
\rho\, \partial_t^2 e \;=\; K_{ee}\, \partial_x^2 e \;+\; K_{e\varphi}\, \partial_x^2 \varphi
$$

That is the equation of motion for *e*. Reading it back: mass density times acceleration equals the sum of the *e*-field's own restoring force (first term, like a stretched string) and the cross-coupling force from the *φ*-field's curvature (second term).

### Equation for *φ*

The same argument for the azimuthal field gives a parallel equation. The slice has rotational moment of inertia *I_φ* d*x* attached to *φ*. The conjugate stress is σ_φ = *K_eφ* (∂_x e) + *K_φφ* (∂_x φ). The net torque from the gradient of σ_φ gives the elastic restoring force:

<!-- I_φ ∂_t² φ = K_eφ ∂_x² e + K_φφ ∂_x² φ -->
$$
I_\varphi\, \partial_t^2 \varphi \;=\; K_{e\varphi}\, \partial_x^2 e \;+\; K_{\varphi\varphi}\, \partial_x^2 \varphi
$$

The two equations are coupled through the *K_eφ* terms that appear on the right-hand side of each: a curvature in *e* drives *φ*, and a curvature in *φ* drives *e*.

### In matrix form

It helps to write the pair compactly. Define the column vector **u**(*x*, *t*) = (*e*, *φ*)ᵀ and the diagonal inertia matrix *D* = diag(ρ, *I_φ*):

<!-- D ∂_t² u = M ∂_x² u -->
$$
D\, \partial_t^2\, \mathbf{u} \;=\; M\, \partial_x^2\, \mathbf{u}
$$

This is the master equation for the cylinder — a single matrix PDE that contains both equations above. Two features worth marking:

- **Linear.** Every term is at most linear in **u** and its derivatives. There is no *e*², no *e*·*φ*, no nonlinearity. Linearity will underwrite the superposition arguments in §9.
- **Coupled.** The off-diagonal entry *K_eφ* of *M* ties the two equations together. With *K_eφ* = 0, the matrix *M* is diagonal and the two equations decouple into two independent wave equations — strain and azimuthal direction would not influence each other.

The cross-coupling has a clean physical reading: when the stress-magnitude field has spatial curvature (nonzero ∂_x² *e*), it drives the azimuthal direction to rotate; when the azimuthal direction has spatial curvature, it drives the stress magnitude. This is the "stretch drives twist, twist drives stretch" coupling of chapter 1 §7. The off-center longitudinal load propagates as a coupled (magnitude, direction) wave along the cylinder.

The wave equations are valid as long as the field stays away from the origin of the stress vector, where the polar coordinates would become singular (chapter 1 §3). For the small-perturbation regime where chapter 2's analysis lives, the polar parameterization is well-defined and the equations are linear in (*e*, *φ*).

---

## 3. Looking for wave solutions: the sinusoidal trial

The master equation *D* ∂_t² **u** = *M* ∂_x² **u** is a second-order PDE with constant coefficients. To find the simplest waves it supports, we use a familiar engineering trick: look for sinusoidal traveling-wave solutions.

A sinusoidal traveling wave looks like

*e*(*x*, *t*) = *A_e* cos(*kx* − ω*t* + α_e)
*φ*(*x*, *t*) = *A_φ* cos(*kx* − ω*t* + α_φ)

— two real waves with separate amplitudes (*A_e*, *A_φ*), a common spatial wavenumber *k* (radians of phase per unit length, so *k* > 0 means the wave moves in the +*x* direction), a common angular frequency ω (radians per unit time), and individual phase offsets (α_e, α_φ).

A more compact form combines amplitude and phase offset for each component into a single complex amplitude. Define **A** = (*A_e* exp(*i*α_e), *A_φ* exp(*i*α_φ))ᵀ; then both waves are

<!-- u(x, t) = A exp(i(kx − ωt)) -->
$$
\mathbf{u}(x, t) = \mathbf{A}\, e^{i(k x - \omega t)}
$$

with the understanding that we take the real part to get the physical fields. This is the standard phasor representation familiar from electrical engineering.

The advantage of the complex form: the time and space derivatives become multiplications:

- ∂_t **u** brings down a factor of (−*i*ω); ∂_t² **u** brings down (−*i*ω)² = −ω².
- ∂_x **u** brings down a factor of (*i k*); ∂_x² **u** brings down (*i k*)² = −*k*².

Substituting **u** = **A** *e^{i(kx − ωt)}* into the master equation:

−ω² *D* **A** *e^{i(kx − ωt)}* = −*k*² *M* **A** *e^{i(kx − ωt)}*

The exponential factor cancels from both sides, as does the minus sign, leaving an algebraic equation for the amplitude **A**:

<!-- ω² D A = k² M A -->
$$
\omega^2\, D\, \mathbf{A} \;=\; k^2\, M\, \mathbf{A}
$$

The PDE has been reduced to a 2 × 2 matrix equation. Multiplying both sides by *D*⁻¹ from the left:

<!-- (ω²/k²) A = D⁻¹ M A -->
$$
\frac{\omega^2}{k^2}\, \mathbf{A} \;=\; D^{-1} M\, \mathbf{A}
$$

This is a standard eigenvalue problem. The amplitude vector **A** is an eigenvector of the matrix *D*⁻¹*M*, and the ratio ω²/*k*² is the corresponding eigenvalue. Engineers will recognize this as the same eigenvalue problem that comes up in finding the natural modes of a coupled mass-spring-and-mass-spring system.

The sinusoidal trial only works for amplitude vectors that are eigenvectors of *D*⁻¹*M*; any other amplitude leaves a residual mismatch in the equation. So the natural propagating modes of the cylinder are exactly the eigenvectors of *D*⁻¹*M*, and their propagation speeds are the square roots of the eigenvalues.

(Brief reminder: an *eigenvector* of a square matrix *A* is a special vector **v** that *A* maps to a scalar multiple of itself — that is, *A***v** = λ**v** for some number λ called the *eigenvalue*. A 2 × 2 matrix has up to two eigenvectors, with two corresponding eigenvalues. They form a "natural basis" for the matrix's action: any vector decomposes as a sum of eigenvectors, and *A* acts on each piece by simple scaling.)

The next two sections solve this eigenvalue problem to find the speeds and shapes of the propagating modes.

---

## 4. Two propagation speeds: the dispersion relation

To get a feel for the eigenvalue problem before tackling the general case, consider what happens when the chiral coupling vanishes.

### Special case: no coupling (*K_eφ* = 0)

With *K_eφ* = 0, the matrix *M* is diagonal: *M* = diag(*K_ee*, *K_φφ*). Then *D*⁻¹*M* = diag(*K_ee*/ρ, *K_φφ*/*I_φ*), itself diagonal. Its two eigenvectors are simply **v**₁ = (1, 0)ᵀ and **v**₂ = (0, 1)ᵀ — the coordinate axes. Its two eigenvalues are *K_ee*/ρ and *K_φφ*/*I_φ*.

Two propagating modes:

- The strain mode: *A_φ* = 0, propagation speed *c*₁ = √(*K_ee*/ρ).
- The azimuthal mode: *A_e* = 0, propagation speed *c*₂ = √(*K_φφ*/*I_φ*).

These are independent uncoupled waves: a stretch wave that doesn't twist, and a twist wave that doesn't stretch. Each propagates at its own speed, set by its own stiffness-to-inertia ratio (the same √(stiffness/inertia) formula familiar from the wave equation for a stretched string).

This is the cylinder primitive without chirality. It is not yet what we want — chapter 2's hypothesis is that *K_eφ* > 0 is what supports coupled wave behavior — but it is a useful baseline to compare to.

### General case: with chiral coupling

Turn *K_eφ* back on. The matrix *D*⁻¹*M* now has off-diagonal entries:

<!-- D^{-1} M = ((K_ee/ρ, K_eφ/ρ), (K_eφ/I_φ, K_φφ/I_φ)) -->
$$
D^{-1} M = \begin{pmatrix} K_{ee}/\rho & K_{e\varphi}/\rho \\ K_{e\varphi}/I_\varphi & K_{\varphi\varphi}/I_\varphi \end{pmatrix}
$$

The eigenvalues come from the characteristic equation det(*D*⁻¹*M* − λ*I*) = 0:

<!-- (K_ee/ρ − λ)(K_φφ/I_φ − λ) − K_eφ²/(ρ I_φ) = 0 -->
$$
\Big(\frac{K_{ee}}{\rho} - \lambda\Big)\Big(\frac{K_{\varphi\varphi}}{I_\varphi} - \lambda\Big) - \frac{K_{e\varphi}^2}{\rho\, I_\varphi} = 0
$$

This expands to a quadratic in λ:

<!-- λ² − (K_ee/ρ + K_φφ/I_φ) λ + (K_ee K_φφ − K_eφ²)/(ρ I_φ) = 0 -->
$$
\lambda^2 - \Big(\frac{K_{ee}}{\rho} + \frac{K_{\varphi\varphi}}{I_\varphi}\Big)\, \lambda + \frac{K_{ee} K_{\varphi\varphi} - K_{e\varphi}^2}{\rho\, I_\varphi} = 0
$$

By the quadratic formula:

<!-- λ_± = (1/2)[K_ee/ρ + K_φφ/I_φ ± √((K_ee/ρ − K_φφ/I_φ)² + 4 K_eφ²/(ρ I_φ))] -->
$$
\lambda_{\pm} \;=\; \tfrac{1}{2}\!\left[\,\frac{K_{ee}}{\rho} + \frac{K_{\varphi\varphi}}{I_\varphi}
\;\pm\; \sqrt{\!\left(\frac{K_{ee}}{\rho} - \frac{K_{\varphi\varphi}}{I_\varphi}\right)^{\!2}
+ \frac{4\,K_{e\varphi}^2}{\rho\, I_\varphi}}\,\right]
$$

These are the two eigenvalues. Both are real (the term under the square root is a sum of two squares, always ≥ 0) and both are positive when *M* is positive-definite (which is the stability requirement of chapter 2 §6).

The two natural propagation speeds are *c*_± = √λ_±. Together with the eigenvalue equation, the dispersion relation — the relation between frequency ω and wavenumber *k* — is:

<!-- ω²(k) = k² λ_± -->
$$
\omega^2(k) \;=\; k^2\, \lambda_{\pm}
$$

— two branches, one for each eigenvalue. Both are linear in |*k*|: the speed *c*_± is independent of *k*.

This last observation is important. A wave whose speed is independent of wavelength is called **non-dispersive**: a localized pulse, which is a sum of many wavelengths, will propagate as a unit without spreading out. (A *dispersive* medium is one where different wavelengths travel at different speeds, so an initially-localized pulse spreads out over time; the cylinder primitive does not have this problem.)

For *K_eφ* = 0, the formula collapses to λ_+ = max(*K_ee*/ρ, *K_φφ*/*I_φ*) and λ_− = min(*K_ee*/ρ, *K_φφ*/*I_φ*), recovering the special-case result. As *K_eφ* grows from zero, the cross term inside the square root grows, and the two eigenvalues split further apart: the larger one (λ_+) increases, and the smaller one (λ_−) decreases. This splitting of the two natural mode speeds is the chiral coupling at work.

---

## 5. The two natural modes: how strain and direction combine

Each eigenvalue has a corresponding eigenvector. Solving (*D*⁻¹*M* − λ_± *I*) **v**_± = 0 gives, after a small amount of algebra, eigenvectors that can be written in the form

<!-- v_+ ∝ (cos θ, sin θ)^T, v_- ∝ (−sin θ, cos θ)^T -->
$$
\mathbf{v}_+ \propto \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}, \qquad
\mathbf{v}_- \propto \begin{pmatrix} -\sin\theta \\ \cos\theta \end{pmatrix}
$$

where the **mixing angle** θ is determined by the matrix entries. The two eigenvectors are orthogonal — perpendicular in the (*A_e*, *A_φ*) plane.

A useful way to read these: the mixing angle θ tells how much each natural mode involves strain versus azimuthal direction.

- At θ = 0 (which happens when *K_eφ* = 0): **v**_+ = (1, 0)ᵀ is pure strain, **v**_− = (0, 1)ᵀ is pure direction. This is the decoupled limit.
- At θ ≠ 0: each mode mixes strain and direction. The fast mode **v**_+ has both *A_e* and *A_φ* nonzero, so when the wave passes through, both fields oscillate together. Same for the slow mode, with the strain-direction mix swapped.
- At θ = π/4 (45°): each mode is a 50/50 mix of strain and direction.

For the simplifying special case where *K_ee*/ρ = *K_φφ*/*I_φ* (equal "bare" speeds for the two channels), the eigenvectors are exactly at θ = π/4 for any *K_eφ* > 0 — the symmetry forces a 50/50 mix. The general case has a θ that depends on the imbalance between the two channels' bare stiffnesses.

### Mechanical reading

In each natural mode, the stress-magnitude oscillation at any position is *locked* to the azimuthal direction's oscillation at the same position. The fast mode (**v**_+) oscillates the two together: when stress is high, direction is at one angle; when stress is low, direction is at the other angle. The slow mode (**v**_−) oscillates them oppositely: when stress is high, direction goes the *other* way; when stress is low, direction goes *back*. The partial cancellation in the slow mode is what makes its propagation speed lower than the fast mode's.

### Optical analog

In optics, a chiral medium (such as a sugar solution) has two natural modes — left-circular and right-circular polarized light — that propagate at slightly different speeds. The cylinder primitive has the same structure: two natural mode mixings of stress magnitude and azimuthal direction, traveling at slightly different speeds *c*_+ and *c*_−. This split in mode speeds is sometimes called *optical activity*. When the cylinder lattice is later coarse-grained to recover Maxwell, these two natural modes will play the role of the two photon polarizations.

---

## 6. Stability boundary and the degenerate limit χ̃ → 1

The dimensionless shear ratio from chapter 1 is

χ̃ = *K_eφ* / √(*K_ee* · *K_φφ*)

This packages the chiral coupling into a single dimensionless number, comparing the off-diagonal stiffness *K_eφ* to the geometric mean of the diagonal stiffnesses √(*K_ee* · *K_φφ*).

For *M* to be positive-definite (the stability requirement — energy must be bounded below), the determinant *K_ee* · *K_φφ* − *K_eφ*² must be positive. This translates to χ̃ < 1.

To see what happens as χ̃ approaches 1, take the simplifying special case ρ = *I_φ* and *K_ee* = *K_φφ* ≡ *K* (which strips the algebra to one symbolic stiffness scale). The eigenvalues simplify to:

<!-- λ_± = (K/ρ)(1 ± χ̃) -->
$$
\lambda_{\pm} = \frac{K}{\rho}\,(1 \pm \tilde{\chi})
$$

So *c*_+ = √(*K*(1 + χ̃)/ρ) and *c*_− = √(*K*(1 − χ̃)/ρ).

As χ̃ → 1 from below, the slow mode's eigenvalue λ_− → 0, and its speed *c*_− → 0. The slow wave is grinding to a halt.

At exactly χ̃ = 1, the matrix *M* has determinant zero. There is a direction in (*e*, *φ*)-space along which the elastic potential energy is *flat* — costing nothing to deform. A perturbation in that direction has no restoring force, so it does not oscillate; it just stays at whatever value it was set to. The slow mode has been replaced by a static, non-propagating zero mode.

For χ̃ > 1, *M* loses positive-definiteness entirely. The smaller eigenvalue becomes *negative*, meaning ω² < 0 on that branch, which means ω is imaginary. A would-be sinusoidal mode at imaginary ω is actually exponentially growing — an instability that signals the model has broken down.

So the cylinder primitive's stable, wave-supporting regime is χ̃ ∈ (0, 1) *strictly* — bounded below by 0 (no chiral coupling, no coupled wave) and above by 1 (degenerate, slow mode collapses). This confirms theory 3 of [README.md](README.md): stability bounds the shear.

---

## 7. The natural shear value χ̃ = 1/√2

The stable range (0, 1) is wide; nothing in §6 prefers any value of χ̃ over any other. To find a *natural* point in this range, we look for the geometric center.

The geometric mean of 0 and 1 — equivalently, the point halfway between them on a logarithmic scale — corresponds to *K_eφ*² being half the way to its stability ceiling *K_ee* · *K_φφ*:

*K_eφ*² = (1/2) *K_ee* · *K_φφ*

Equivalently, χ̃² = 1/2, so

<!-- χ̃ = 1/√2 ≈ 0.707 -->
$$
\tilde{\chi} = \frac{1}{\sqrt{2}} \approx 0.707
$$

What this point means physically:

- The chiral coupling is well-engaged (χ̃ is well away from zero, so the two channels are coupled and the medium supports propagating modes).
- The stability margin is also substantial (χ̃ is well below 1, so the slow mode is not near collapse).
- *M*'s determinant is exactly half the diagonal product: det(*M*) = *K_ee* · *K_φφ* − *K_eφ*² = (1/2) *K_ee* · *K_φφ*.

In the simplifying special case ρ = *I_φ*, *K_ee* = *K_φφ* = *K*, the two mode speeds at χ̃ = 1/√2 are:

*c*_+ = √(*K*(1 + 1/√2)/ρ) ≈ √(1.707 *K*/ρ)
*c*_− = √(*K*(1 − 1/√2)/ρ) ≈ √(0.293 *K*/ρ)

Their ratio is *c*_+/*c*_− = √((1 + 1/√2) / (1 − 1/√2)) ≈ 2.41. The slow mode is roughly 0.41 times the fast mode.

This χ̃ = 1/√2 value is sometimes referred to as an "equipartition" or "impedance-matched" point in the literature, on the grounds that strain and azimuthal channels carry comparable shares of the wave's content there. The mathematical content is the geometric-mean argument above; richer physical interpretations of the same value (thermodynamic equilibration between left and right circular populations, for example) don't add to or change the value.

A note on what this does and does not establish. The geometric-mean argument identifies χ̃ = 1/√2 as the *natural* value in the parameter space — but does not *force* the cylinder primitive to sit there. Nothing in chapter 2 alone pins χ̃ to any particular value within (0, 1). The further question of whether the lattice signal speed *c* (from GRID axiom A1) supplies an additional constraint that pins χ̃ is taken up in the next chapter.

---

## 8. Left-going and right-going waves travel at equal speeds

A central question for the cylinder primitive: does the chiral shear, which we have just established splits the two natural modes into different speeds, *also* introduce a preference for one direction of propagation over the other?

The answer is no, and the proof is direct. The dispersion relation derived in §4 is

ω²(*k*) = *k*² λ_±

The right-hand side depends on *k* only through *k*². Since *k*² = (−*k*)², we have

<!-- ω²(k) = ω²(−k) -->
$$
\omega^2(k) = \omega^2(-k)
$$

for each branch ±. Taking the positive square root gives ω(*k*) = ω(−*k*) up to sign convention. The phase speed |ω/*k*| = *c*_± is independent of the sign of *k*. Waves moving in the +*x* direction (*k* > 0) and waves moving in the −*x* direction (*k* < 0) propagate at exactly the same speed for each mode.

It is worth distinguishing this from another notion that is easily confused with it: the chiral shear *does* split the two modes themselves into different speeds (*c*_+ ≠ *c*_−). That is the cylinder's analog of *optical activity* — the difference between left-circular and right-circular polarized light in a chiral solution. But the choice of mode is a property of the *polarization* (which mix of strain and direction is oscillating), not of which way the wave is going. A given mode propagates at the same speed in either direction.

The reason the medium has direction symmetry is structural: the stiffness matrix *M* is real and symmetric, the inertia matrix *D* is real and diagonal. There is no term in the equations of motion that distinguishes +*x* from −*x*. A complex-valued *M*, or an asymmetric *M*, would break this — and in some real media (a magnetic field aligned with a propagation axis, for instance) such terms do appear, producing the *Faraday effect* in which left-circular light travels faster than right-circular light in one direction and slower in the reverse direction. The cylinder primitive's chirality is of a different, time-reversal-symmetric kind, and it does not produce direction-dependent propagation. This confirms theory 5 of [README.md](README.md).

A *negative-result candidate* worth flagging: if working through the algebra had produced a term linear in *k* in the dispersion (a difference between ω(*k*) and ω(−*k*)), the cylinder primitive would have failed this test — it would be incompatible with vacuum Maxwell, where photons of given polarization travel at *c* in either direction. The check passes because *M* is real and symmetric.

---

## 9. Linear superposition: pulses pass through each other

The wave equation *D* ∂_t² **u** = *M* ∂_x² **u** is linear: every term is at most linear in **u** and its derivatives. Linearity has a strong consequence — if **u**₁(*x*, *t*) and **u**₂(*x*, *t*) are both solutions, then any linear combination of them is also a solution. Substitute **u**₁ + **u**₂ into the equation, distribute the linear operators over the sum, and use the fact that each piece satisfies the equation separately; the combination satisfies it too.

Physically: two waves travelling along the same cylinder do not interfere with each other in any nonlinear way. They add. To see what this means for opposing pulses, construct two wave packets — one moving right, one moving left:

<!-- u_L(x, t) = A_L f(x − c t),  u_R(x, t) = A_R g(x + c t) -->
$$
\mathbf{u}_L(x, t) = \mathbf{A}_L\, f(x - c\, t),
\qquad
\mathbf{u}_R(x, t) = \mathbf{A}_R\, g(x + c\, t)
$$

where *c* is the wave speed of the relevant mode (the same for both directions, by §8), *f* and *g* are arbitrary smooth pulse shapes, and **A**_L and **A**_R are amplitude vectors. Each is a solution of the wave equations of §2. Their sum **u**(*x*, *t*) = **u**_L + **u**_R is also a solution, by linearity.

As time advances, the right-going pulse with shape *f* moves right at speed *c*, and the left-going pulse with shape *g* moves left at speed *c*. They will meet somewhere in the middle, *overlap* during a transient interval, and then continue past each other.

During the overlap, the field **u** at any point is just the sum of the two pulse profiles at that point. There is no scattering of one pulse off the other, no exchange of energy, no distortion of either waveform. After the pulses separate, each one carries its original shape — *f* moving right, *g* moving left — exactly as it would have if the other were absent.

This linear-superposition property is what makes the cylinder primitive a *faithful* wave medium: any complicated wave pattern, no matter how it is constructed, can be analyzed as a sum of independently propagating pieces. Engineers will recognize this as the cornerstone of Fourier analysis — the reason linear systems can be analyzed one frequency at a time.

The viz model demonstrated this empirically with its Δ2 preset ([viz/grid-lab.md](../../viz/grid-lab.md)): two delta-function pulses launched from opposite ends of a chain pass through each other and emerge with their original shapes intact. The continuous cylinder primitive of this chapter reproduces the same behavior at the level of the underlying wave equation, where it follows from a single property — linearity — rather than from a per-cell update rule.

---

## 10. Summary of givens

The cylinder primitive's wave dynamics, established in this chapter:

- The cylinder's energy density has two parts: kinetic (from time-derivatives of the fields, weighted by the inertias ρ and *I_φ*) and elastic (from spatial gradients, weighted by the stiffness matrix *M*).
- Newton's law applied to a slice of cylinder gives a coupled pair of linear second-order PDEs for *e* and *φ*, written compactly as *D* ∂_t² **u** = *M* ∂_x² **u** with *D* = diag(ρ, *I_φ*).
- The sinusoidal trial **u** = **A** *e^{i(kx − ωt)}* reduces the PDE to a 2 × 2 eigenvalue problem (ω²/*k*²) **A** = *D*⁻¹*M* **A** with two real positive eigenvalues at every *k*.
- The dispersion relation has two branches, ω²(*k*) = *k*² λ_±, both linear in |*k*|. The medium is non-dispersive: pulses propagate without spreading.
- The two natural modes are mixings of strain and azimuthal direction governed by the eigenvectors of *D*⁻¹*M*. They are the cylinder primitive's analog of left-circular and right-circular polarizations.
- Stability requires χ̃ ∈ (0, 1) strictly. The upper limit χ̃ = 1 is degenerate: the slow-mode wave speed collapses to zero.
- The geometric mean of the stable range is χ̃ = 1/√2 ≈ 0.707 — a natural midpoint at which the chiral coupling is well-engaged but the stability margin is substantial.
- The dispersion ω² depends on *k* only through *k*², so left-going and right-going waves propagate at identical speeds. Chirality splits *mode* speeds (optical activity) but not *direction* speeds (no Faraday effect). The cylinder is direction-symmetric.
- The wave equations are linear, so any two solutions can be superposed. Two opposing pulses pass through each other and emerge with original waveforms intact.

These properties are what a viable primitive substrate must have to support Maxwell-style wave physics. The next chapter takes up the question of whether the lattice signal speed *c* — the cadence at which the GRID lattice transmits information — pins the cylinder's parameters more tightly, or leaves a one-parameter family in play.
