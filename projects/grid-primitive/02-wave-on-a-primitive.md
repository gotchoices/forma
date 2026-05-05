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

When the fields change in time, they carry kinetic energy. For a generic two-channel medium it is the standard quadratic form, but with the chirally-coupled inertia matrix *D* introduced in chapter 1 §8 — the medium's helical microstructure produces inertia couplings as well as stiffness couplings:

<!-- T̃ = (1/2) (∂_t e, ∂_t φ) · D · (∂_t e, ∂_t φ)ᵀ
   = (1/2)[ρ (∂_t e)² + 2 D_eφ (∂_t e)(∂_t φ) + I_φ (∂_t φ)²] -->
$$
\widetilde{T} = \tfrac{1}{2}
\begin{pmatrix} \partial_t e & \partial_t \varphi \end{pmatrix}
D
\begin{pmatrix} \partial_t e \\ \partial_t \varphi \end{pmatrix}
= \tfrac{1}{2}\!\left[\rho\,(\partial_t e)^2 + 2 D_{e\varphi}\,(\partial_t e)(\partial_t \varphi) + I_\varphi\,(\partial_t \varphi)^2\right]
$$

The three coefficients are:

- ρ — the **longitudinal substrate-level inertia** for the *e* channel. By analogy with continuum mechanics this would be a "mass density" (kg/m for an actual rod), but the analogy is loose: this is a substrate coefficient that pairs with ∂_t² *e*, not the rest mass of any particle.
- *I_φ* — the **azimuthal substrate-level inertia**. By analogy this is "moment of inertia per unit length," but again the cylinder primitive is at the lattice substrate scale, well below where particles or their rest masses exist.
- *D_eφ* — the **chiral cross-inertia**. The helical microstructure that produces the stiffness chirality also couples the kinetic energies of stretching and twisting.

A clarification worth making explicit. "Mass," "inertia," and "moment of inertia" are continuum-mechanics terms we are borrowing because the wave equation has the same algebraic form. But the cylinder primitive is at the Planck-scale lattice substrate, and at this scale **no particle rest mass exists** — particle rest mass is a metric-mass-style emergent quantity, structural to how the lattice carries particles, not a property of the lattice substrate itself. So our ρ, *I_φ*, and *D_eφ* are *substrate coefficients* that determine the medium's propagation speed; they are not particle rest masses.

In GRID's natural units (*c* = ℏ = 1), the matched-chirality + bare-speed condition reduces *M* and *D* to the *same* matched-chirality matrix (chapter 1 §8). The separate-matrix presentation here is for pedagogical clarity — the matched-chirality condition is more visible when *D* and *M* are written out separately than when they are folded into one. But at the substrate level, "mass" and "stiffness" are two views of the same structural quantity, not separate physics.

By the **matched chirality** commitment of chapter 1 §8, the cross-inertia is not an independent parameter: it is fixed by the same chirality ratio χ̃ that governs the stiffness matrix:

D_eφ / √(ρ · *I_φ*) = χ̃

A diagonal *D* (with *D_eφ* = 0) corresponds to χ̃ = 0 in the inertia, which is *inconsistent* with χ̃ > 0 in the stiffness. Earlier drafts made the diagonal-*D* simplification implicitly; the matched-chirality formulation is the consistent one.

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

### The inertial momentum and the elastic force

Now the inertia is a 2 × 2 matrix, so the slice's "momentum" couples both fields. Define the column **u** = (*e*, *φ*)ᵀ. The slice's *generalized momentum* per unit length is *D* ∂_t **u**, and its *generalized inertial force* per unit length is *D* ∂_t² **u**. In components:

(inertial force on slice in *e* channel) = (ρ ∂_t² *e* + *D_eφ* ∂_t² *φ*) d*x*
(inertial force on slice in *φ* channel) = (*D_eφ* ∂_t² *e* + *I_φ* ∂_t² *φ*) d*x*

The cross terms come from *D_eφ*: a coupled-channel medium has cross-inertia exactly because acceleration in one channel produces inertial response in the other.

The elastic force on the slice comes from the *difference* in internal stress at the two ends of the slice. Reading off the elastic potential Ṽ from §1, the internal stresses at any cross-section *x* are:

σ_e(*x*, *t*) = *K_ee* (∂_x *e*) + *K_eφ* (∂_x *φ*)
σ_φ(*x*, *t*) = *K_eφ* (∂_x *e*) + *K_φφ* (∂_x *φ*)

The net elastic forces on the slice in each channel are the gradients of these stresses, times d*x*.

### The equations of motion

Setting inertial force equal to net elastic force and dividing through by d*x*:

<!-- ρ ∂_t² e + D_eφ ∂_t² φ = K_ee ∂_x² e + K_eφ ∂_x² φ -->
<!-- D_eφ ∂_t² e + I_φ ∂_t² φ = K_eφ ∂_x² e + K_φφ ∂_x² φ -->
$$
\begin{aligned}
\rho\, \partial_t^2 e + D_{e\varphi}\, \partial_t^2 \varphi
\;&=\;
K_{ee}\, \partial_x^2 e + K_{e\varphi}\, \partial_x^2 \varphi
\\
D_{e\varphi}\, \partial_t^2 e + I_\varphi\, \partial_t^2 \varphi
\;&=\;
K_{e\varphi}\, \partial_x^2 e + K_{\varphi\varphi}\, \partial_x^2 \varphi
\end{aligned}
$$

These are coupled both ways now: in time-derivatives (through *D_eφ*) *and* in space-derivatives (through *K_eφ*). The medium's chirality has manifested in both kinetic and elastic responses, exactly as the matched-chirality commitment of chapter 1 requires.

### In matrix form

Define **u** = (*e*, *φ*)ᵀ and the matrices *D* and *M* from chapter 1. The pair of equations becomes:

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

### General case: with matched chirality

Turn *K_eφ* back on. By the matched-chirality commitment of chapter 1 §8, the cross-inertia *D_eφ* is also non-zero, with both controlled by the single chirality parameter χ̃:

*K_eφ* = χ̃ √(*K_ee* *K_φφ*),    *D_eφ* = χ̃ √(ρ *I_φ*)

This has a striking algebraic consequence. With matched chirality, *M* and *D* have the same off-diagonal *structure*, and they are proportional to each other when the bare-speed condition

*K_ee*/ρ = *K_φφ*/*I_φ* ≡ *c*²

holds (where *c* is the bare propagation speed common to both channels — chapter 3 will identify this with the lattice signal speed). Under both conditions:

<!-- M = c² D -->
$$
M \;=\; c^2\, D
$$

To see this directly: with *K_ee* = *c*² ρ and *K_φφ* = *c*² *I_φ*, the diagonal entries of *M* equal *c*² times those of *D*. For the off-diagonal:

*K_eφ* = χ̃ √(*K_ee* *K_φφ*) = χ̃ √(*c*² ρ · *c*² *I_φ*) = *c*² · χ̃ √(ρ *I_φ*) = *c*² *D_eφ*

so *K_eφ* = *c*² *D_eφ*. The two matrices are proportional throughout.

### What *M* = *c*² *D* does to the dispersion

Substitute into the eigenvalue problem:

ω² *D* **A** = *k*² *M* **A** = *k*² · *c*² *D* **A**

so

ω² *D* **A** = *c*² *k*² *D* **A**

Since *D* is invertible (positive-definite), divide by *D* on both sides:

<!-- ω² = c² k² -->
$$
\omega^2 \;=\; c^2\, k^2
$$

— **for every amplitude vector A**. There is no eigenvalue selection because every direction is an eigenvector with the same eigenvalue *c*². The dispersion relation is single-branch:

ω(*k*) = *c* |*k*|

The cylinder propagates at a single speed *c*, with no preferred polarization. Both real components of the stress vector — and any combination of them — propagate at the same speed. The chiral coupling is still present (it is what makes the cylinder a coupled-wave medium rather than two unrelated channels), but matched chirality removes any speed difference between polarizations.

### Why this matters

This is the key consequence of matched chirality for the wave dynamics. Without it (with *D* diagonal), the cylinder would have produced two propagating modes at different speeds — chiral splitting, like optical activity in a sugar solution. *With* matched chirality, the two modes degenerate at *c*, exactly as vacuum Maxwell expects for the two photon polarizations.

The cylinder primitive is not a chiral medium in the propagation sense (no birefringence, no slow mode); it is a chirally-coupled medium where the chirality enters internally (in how the channels interact at any given point) but does not split the propagation speeds.

A useful physical analog: in optics, a chiral medium splits left- and right-circular polarizations into different speeds (optical activity). The cylinder primitive is *not* such a medium. It is the chirally-coupled analog of vacuum, where both polarizations propagate at *c* despite the underlying chiral structure.

### Without matched chirality

For completeness, if matched chirality fails (independent chiralities in *D* and *M*), the analysis returns the two-eigenvalue problem of an earlier draft of this chapter — eigenvalues λ_± of *D*⁻¹*M*, with two distinct propagation speeds *c*_± = √λ_±. The earlier algebraic form (a quadratic in λ with discriminant determining the split) is the general case; matched chirality is the special case where the discriminant happens to vanish in such a way that the two eigenvalues coincide at *c*².

The cylinder primitive *commits* to matched chirality; the general two-speed case is not the model we are working with.

---

## 5. Polarizations: how strain and direction combine in the propagating wave

Under matched chirality (§4), every direction in the (*e*, *φ*) amplitude plane is an eigenvector with the same eigenvalue *c*². There is no preferred mode-shape; the cylinder propagates *all* polarizations at the same speed.

### Two independent polarizations

Although every amplitude direction propagates at *c*, we can still pick a basis of two orthogonal polarizations to describe a general wave. The natural choice is the two coordinate directions in the (*e*, *φ*) plane:

- **e-polarized wave**: *A* = (1, 0)ᵀ. The stress magnitude oscillates while the azimuthal direction stays at zero.
- **φ-polarized wave**: *A* = (0, 1)ᵀ. The azimuthal direction oscillates while the stress magnitude stays at zero.

A general wave is any linear combination of these two: *A* = (*A_e*, *A_φ*) = *A_e*(1, 0) + *A_φ*(0, 1). All combinations propagate at *c*.

This is exactly Maxwell's vacuum in 2D: two independent polarizations of a single wave field, both at *c*, with any superposition also at *c*.

### Circularly polarized waves

A particularly useful pair of polarizations is the **circular** combination:

- **R-circular**: *A* = (1, *i*)ᵀ /√2 — at any spatial point, as time advances the (*e*, *φ*) amplitude rotates clockwise (if we identify (*e*, *φ*) with (*x*, *y*) Cartesian coordinates).
- **L-circular**: *A* = (1, −*i*)ᵀ /√2 — counter-clockwise rotation.

Under matched chirality, both circular polarizations propagate at *c*. There is no chiral-medium-style splitting between them — no "optical activity" in the propagation. The cylinder is structurally chiral (*K_eφ* > 0, *D_eφ* > 0), but its chirality affects only the *internal* coupling between channels, not the propagation speed of any polarization.

### What chirality *does* affect

Even though all polarizations propagate at *c*, the chirality is not invisible. It enters in two ways:

1. **Coupling between the channels.** A pure-*e* perturbation injected at one end of the cylinder does not stay pure-*e* — the chirality redistributes amplitude into the *φ* channel as the wave evolves. Both channels participate in any actual wave because of *K_eφ* and *D_eφ* together.
2. **The kink-loss formula in chapter 8.** When the cylinder lattice is folded into a torus (the wrap relevant to charge emergence), the chirality enters the leakage rate per wrap. The functional form of α as a geometric ratio depends on χ̃.

So matched chirality does not erase the chirality from the model. It just localizes its effects — chirality matters for how the cylinder couples its two channels and for how a wrapped sheet of cylinders leaks energy at corners. It does not produce birefringence at the propagation level.

---

## 6. Stability boundary on the chirality

The dimensionless chirality from chapter 1 is

χ̃ = *K_eφ* / √(*K_ee* · *K_φφ*) = *D_eφ* / √(ρ · *I_φ*)

(matched chirality means both ratios equal the same χ̃). For both *M* and *D* to be positive-definite — energy must be bounded below in both elastic and kinetic forms — we need the determinant of each matrix to be positive:

det(*M*) = *K_ee* *K_φφ* − *K_eφ*² > 0,    det(*D*) = ρ *I_φ* − *D_eφ*² > 0

Both translate to the same condition on χ̃:

χ̃ < 1

So the stable range of chirality is χ̃ ∈ (0, 1), bounded below by 0 (no chiral coupling — the cylinder becomes two unrelated channels) and above by 1 (both *M* and *D* simultaneously become singular).

What happens at χ̃ = 1? Both matrices have determinant zero. *M* has a direction in (*e*, *φ*)-space along which the elastic potential is flat (no restoring force); *D* simultaneously has a direction along which the kinetic energy is flat (no inertial response). For χ̃ > 1 both lose positive-definiteness and the model breaks down: the kinetic and potential energies could each become negative for some perturbations, signaling unphysical instabilities.

A note on the propagation speed at the stability boundary. Under matched chirality (M = c² D), both modes propagate at *c* throughout the stable range — including at the χ̃ = 1 boundary, where the dispersion ω = c |k| still holds because the matrices remain proportional even as they go singular. (In an earlier-draft setup with diagonal D, the slow-mode speed would have collapsed to zero at χ̃ = 1; under matched chirality this collapse does not happen because both matrices degenerate together.)

So the χ̃ < 1 condition is a stability requirement in its own right (positive-definiteness of energy), not a wave-speed constraint. Both modes propagate at *c* throughout the stable range. Theory 3 of [README.md](README.md) is confirmed.

---

## 7. The natural shear value χ̃ = 1/√2

The stable range χ̃ ∈ (0, 1) is wide; nothing in §6 prefers any value of χ̃ over any other. To find a *natural* point in this range, we look for the geometric center.

The geometric mean of 0 and 1 — equivalently, the point halfway between them on a logarithmic scale — corresponds to *K_eφ*² being half the way to its stability ceiling *K_ee* · *K_φφ*:

*K_eφ*² = (½) *K_ee* · *K_φφ*

Equivalently, χ̃² = 1/2, so

<!-- χ̃ = 1/√2 ≈ 0.707 -->
$$
\tilde{\chi} = \frac{1}{\sqrt{2}} \approx 0.707
$$

What this point means structurally:

- The chiral coupling is well-engaged (χ̃ is well away from zero, so the two channels are genuinely coupled — the cylinder is a coupled-wave medium, not two unrelated channels).
- The stability margin is substantial (χ̃ is well below 1, so neither *M* nor *D* is anywhere near singular).
- The determinants are exactly half their diagonal products: det(*M*) = ½ *K_ee* *K_φφ*, det(*D*) = ½ ρ *I_φ*.

Under matched chirality, the value χ̃ = 1/√2 does *not* affect the propagation speed — both polarizations propagate at *c* throughout the stable range, by the matched-chirality result of §4. What χ̃ affects is the *internal coupling strength* between the channels: how strongly a perturbation in one channel drives a response in the other. At χ̃ = 1/√2, this coupling is "well-tuned" — neither so weak that the channels are effectively independent, nor so strong that the medium is near instability.

The χ̃ = 1/√2 value is sometimes referred to as an "equipartition" or "impedance-matched" point in the literature. The mathematical content is the geometric-mean argument above; the physical interpretations don't change the value.

A note on what this does and does not establish. The geometric-mean argument identifies χ̃ = 1/√2 as the *natural* value in the parameter space — but does not *force* the cylinder primitive to sit there. Nothing in chapter 2 alone pins χ̃ to any particular value within (0, 1). The further question of whether the lattice signal speed *c* (from GRID axiom A1) supplies an additional constraint that pins χ̃ is taken up in the next chapter.

---

## 8. Left-going and right-going waves travel at equal speeds

A check on the model: does the chiral coupling introduce a preference for one direction of propagation over the other?

The answer is no. The dispersion relation under matched chirality is

ω²(*k*) = *c*² *k*²

depending on *k* only through *k*². Since *k*² = (−*k*)², we have

<!-- ω²(k) = ω²(−k) -->
$$
\omega^2(k) = \omega^2(-k)
$$

The phase speed |ω/*k*| = *c* is independent of the sign of *k*. Waves moving in the +*x* direction (*k* > 0) and the −*x* direction (*k* < 0) propagate at the same speed.

The reason is structural: both *M* and *D* are real and symmetric. There is no term in the equations of motion that distinguishes +*x* from −*x*. A complex-valued or asymmetric *M* (or *D*) would break this — and in some real media (a magnetic field aligned with a propagation axis, for instance) such terms do appear, producing the *Faraday effect* in which left-circular light travels faster than right-circular light in one direction and slower in the reverse direction. The cylinder primitive's chirality is of a different, time-reversal-symmetric kind, and it does not produce direction-dependent propagation. This confirms theory 5 of [README.md](README.md).

A *negative-result candidate* worth flagging: if working through the algebra had produced a term linear in *k* in the dispersion (a difference between ω(*k*) and ω(−*k*)), the cylinder primitive would have failed this test — it would be incompatible with vacuum Maxwell, where photons of given polarization travel at *c* in either direction. The check passes because both *M* and *D* are real and symmetric.

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

- The cylinder's energy density has two parts: kinetic (from time-derivatives of the fields, weighted by the inertia matrix *D*) and elastic (from spatial gradients, weighted by the stiffness matrix *M*). Both matrices are non-diagonal under the matched-chirality commitment of chapter 1 §8.
- Newton's law applied to a slice of cylinder gives a coupled pair of linear second-order PDEs for *e* and *φ*, written compactly as *D* ∂_t² **u** = *M* ∂_x² **u**.
- The sinusoidal trial **u** = **A** *e^{i(kx − ωt)}* reduces the PDE to ω² *D* **A** = *k*² *M* **A**.
- Under matched chirality plus bare-speed equality (*K_ee*/ρ = *K_φφ*/*I_φ* = *c*²), the matrices satisfy *M* = *c*² *D*. The eigenvalue problem then has a single eigenvalue *c*² with every direction in (*A_e*, *A_φ*)-space being an eigenvector. The dispersion is single-branch: ω = *c* |*k*|.
- Both polarizations of the cylinder's stress vector — and any combination of them — propagate at the same speed *c*. The cylinder is the chirally-coupled analog of vacuum: chirality at the internal-coupling level, no birefringence at the propagation level.
- Stability requires χ̃ ∈ (0, 1) strictly — bounded above by simultaneous singularity of *M* and *D*. Both modes propagate at *c* throughout the stable range.
- The geometric mean of the stable range is χ̃ = 1/√2 ≈ 0.707 — a natural midpoint at which the chiral coupling is well-engaged but the stability margin is substantial. Under matched chirality, χ̃ governs internal coupling strength, not propagation speed.
- The dispersion ω² depends on *k* only through *k*², so left-going and right-going waves propagate at identical speeds. The cylinder is direction-symmetric (no Faraday effect).
- The wave equations are linear, so any two solutions can be superposed. Two opposing pulses pass through each other and emerge with original waveforms intact.

These properties are what a viable primitive substrate must have to support vacuum-Maxwell-style wave physics. The next chapter takes up the question of whether the lattice signal speed *c* — the cadence at which the GRID lattice transmits information — pins the cylinder's parameters more tightly, or leaves a one-parameter family in play.
