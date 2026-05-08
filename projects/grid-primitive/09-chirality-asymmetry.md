# Chapter 9 — Chirality Asymmetry

This chapter revisits the matched-chirality commitment of [chapter 1 §8](01-foundation.md). Earlier chapters took matched chirality as exact — the cylinder's elastic and kinetic chiralities have the *same* magnitude, governed by a single parameter χ̃, with both *M* and *D* real symmetric. Under that exact match plus bare-speed equality, the cylinder's wave dynamics are fully direction-symmetric: ω²(*k*) = ω²(−*k*), no preferred direction of propagation, both polarizations at *c* (chapter 2 §8).

That commitment is a *simplifying assumption*, not a derivation. Nothing in the cylinder's microstructural picture forces the elastic and kinetic chiralities to coincide *exactly*. Generically, the two would differ by some small amount, and the cylinder primitive would have a small antisymmetric component in its stiffness or inertia (or both). Exact matching is a special, measure-zero point in parameter space; perturbations away from it are the natural case.

The question this chapter takes up: **what does the cylinder primitive look like if matched chirality is admitted to be only approximate?** The answer is developed in two layers.

The first layer (§§1–5) is mathematical. The chapter parameterises a small antisymmetric perturbation, derives the resulting dispersion relation, identifies the perturbation at the matter-field level with a built-in background gauge field, and traces the perturbation's signature through to the gauge-sector quantities *E* and *B* that grid/maxwell.md uses.

The second layer (§§6–8) is interpretive and increasingly speculative. The chapter argues — using the standard Aharonov-Bohm distinction between topologically trivial and non-trivial regions — that the perturbation is unobservable in extended (open) space but produces gauge-invariant Wilson-loop phases on compact wraps (§§6–7; this part is mathematically firm). §8 is more speculative: it offers anomalous magnetic moments as a *possible* macroscopic interpretation of those Wilson-loop phases, while leaving open whether the interpretation is correct. Whether observed anomalous moments actually arise from this mechanism — in part, in full, or not at all — is for downstream work in [metric-charge](../metric-charge/) or its successors to settle.

The chapter does not pin χ_anti to a value, does not claim matched chirality is wrong (chapters 1–8 still hold under the matched commitment), and does not derive specific particle-level predictions. What it establishes is that *if* a small mismatch is admitted, the mathematical consequences are tractable and structurally clean, with a natural place — compact-wrap topology — for the asymmetry to manifest if it manifests anywhere.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | Matched chirality as an assumption, not a derivation |
| 2 | A small antisymmetric perturbation: setup |
| 3 | The modified dispersion relation |
| 4 | Matter-field reading: a built-in background gauge field |
| 5 | From substrate (*M*, *D*) to gauge sector (*E*, *B*) |
| 6 | Aharonov-Bohm pure-gauge invisibility on extended space |
| 7 | Wilson-loop observability on compact wraps |
| 8 | A speculative reading: anomalous magnetic moments |
| 9 | Closing pointer |

---

## 1. Matched chirality as an assumption, not a derivation

Chapter 1 §8 introduced the matched-chirality commitment and was explicit that the commitment is postulated rather than derived. Quoting that section:

> *Matched chirality is a self-consistency assumption: the chirality is one physical thing (a helical structure), and it manifests in both elastic energy and kinetic energy with the same magnitude. We are not deriving matched chirality from a deeper theory; we are choosing it as a property of the cylinder we are designing.*

Two facts follow that this chapter wants to keep separately in view.

**First**, exact matching means *K_eφ*/√(*K_ee K_φφ*) = *D_eφ*/√(ρ *I_φ*) = χ̃, with no residual mismatch between the elastic chirality (in *M*) and the kinetic chirality (in *D*). Both off-diagonal entries are real, both share the same dimensionless ratio. Any departure from matching is a *separate* dimensionless parameter, not a value of χ̃.

**Second**, both *M* and *D* are real *symmetric* matrices: *K_eφ* = *K_φe* and *D_eφ* = *D_φe*. The off-diagonal entries are equal across the two off-diagonal positions. This is the symmetry that chapter 2 §8 invoked to prove direction symmetry ω²(*k*) = ω²(−*k*) — the proof's load-bearing step is that *M* and *D* are real-symmetric, which makes the wave equation's eigenvalue problem self-adjoint and gives ω² that depends on *k* only through *k*².

The structural option this chapter explores is to relax the *symmetry* requirement on *M* and *D* by a small antisymmetric piece, while keeping χ̃ in its stable range (0, 1). This is a different perturbation from changing χ̃: it adds a new degree of freedom (a small antisymmetric perturbation parameter) rather than tuning the existing one.

Microstructurally, what this would correspond to is a helical fiber arrangement in the cylinder wall whose chirality is not perfectly time-reversal-symmetric — the helix itself has a small intrinsic preference for one rotational sense over the reverse. Whether such an asymmetry is forced by the underlying microstructure (the fractal-recursion picture acknowledged in chapter 1 §1) or is excluded by it is not settled by this chapter; the cylinder primitive's microstructure is acknowledged but not pursued in detail (ground rule 3). The chapter takes the small antisymmetric option as a *parameter*, characterises its consequences, and hands the question of its origin to either further development of the microstructure or to downstream observation.

---

## 2. A small antisymmetric perturbation: setup

Define a single small dimensionless parameter

<!-- χ_anti = (K_eφ - K_φe) / (2 √(K_ee K_φφ)) -->
$$
\chi_{\mathrm{anti}} \;=\; \frac{K_{e\varphi} - K_{\varphi e}}{2\sqrt{K_{ee}\, K_{\varphi\varphi}}}
$$

— the dimensionless asymmetry between the two off-diagonal entries of the stiffness matrix, normalised to the diagonal stiffness scale. The matched commitment of chapter 1 §8 is χ_anti = 0; this chapter develops the consequences of χ_anti ≠ 0 with |χ_anti| ≪ 1.

The stiffness matrix decomposes into its symmetric and antisymmetric parts:

<!-- M = M_sym + ε J -->
$$
M \;=\; M_{\mathrm{sym}} \;+\; \varepsilon_M\, J, \qquad
J \;=\; \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
$$

where *M_sym* is the symmetric matrix of chapter 1 (with *K_eφ* = *K_φe* = the symmetric part) and ε_M = √(*K_ee K_φφ*) · χ_anti is the antisymmetric stiffness scale. The matrix *J* is the 2D rotation generator: *J*² = −*I*, *J^T* = −*J*.

For the inertia matrix *D*, two natural choices are available.

**Choice A (matched antisymmetric perturbation).** Both *M* and *D* acquire antisymmetric pieces in the same proportion: *D* = *D_sym* + (ε_M / *c*²) *J*. Then *M* = *c*² *D* is preserved. This corresponds to a microstructural picture in which whatever produces the elastic asymmetry produces a matched kinetic asymmetry, generalising the matched-chirality argument of chapter 1 §8 to the antisymmetric piece.

**Choice B (stiffness-only perturbation).** Only *M* acquires an antisymmetric piece; *D* remains symmetric. Then *M* ≠ *c*² *D*, and the wave dynamics develop a more complex structure including polarization-dependent speeds.

This chapter develops choice A, both because it is the natural microstructural extension of the matched-chirality argument and because it produces the cleanest observable signature (a single parameter modifying the dispersion in one specific way). Choice B is a separate structural option not pursued here.

Under choice A, the wave equation becomes

<!-- (D_sym + (ε_M/c²) J) ∂_t² u = (M_sym + ε_M J) ∂_x² u -->
$$
\bigl(D_{\mathrm{sym}} + \tfrac{\varepsilon_M}{c^2} J\bigr)\, \partial_t^2\, \mathbf{u}
\;=\;
\bigl(M_{\mathrm{sym}} + \varepsilon_M J\bigr)\, \partial_x^2\, \mathbf{u}
$$

with **u** = (*e*, *φ*)^T as before.

---

## 3. The modified dispersion relation

The plane-wave ansatz **u** = **A** exp(*i*(*kx* − ω*t*)) substitutes into the wave equation to give an algebraic eigenvalue problem at each (ω, *k*):

<!-- ω² (D_sym + (ε_M/c²) J) A = k² (M_sym + ε_M J) A -->
$$
\omega^2 \bigl(D_{\mathrm{sym}} + \tfrac{\varepsilon_M}{c^2} J\bigr) \mathbf{A}
\;=\;
k^2 \bigl(M_{\mathrm{sym}} + \varepsilon_M J\bigr) \mathbf{A}
$$

Using *M_sym* = *c*² *D_sym* (from chapter 2 §4 / chapter 3 §2 under matched chirality + bare-speed equality), the matched antisymmetric perturbation makes the *full* matrices proportional:

<!-- M = M_sym + ε J = c²(D_sym + (ε/c²) J) = c² D -->
$$
M \;=\; c^2\, D
$$

— the proportionality survives the antisymmetric perturbation under choice A. This is what makes choice A the natural extension of matched chirality.

So the eigenvalue equation reduces to ω² *D* **A** = *k*² *c*² *D* **A**, giving:

<!-- ω² = c² k² -->
$$
\omega^2 \;=\; c^2\, k^2
$$

— exactly the same dispersion as the unperturbed case. *The matched antisymmetric perturbation does not change the dispersion at the level of the (e, φ) wave equation.*

This is at first surprising: the asymmetry seemed to introduce a directional preference, but the dispersion didn't change. The resolution is that the asymmetry is not in the dispersion of *bulk* waves on the cylinder; it is in the *wavefunction structure* — specifically, in the relationship between (*e*, *φ*) and the matter-field combination ψ = *e* exp(*iφ*). The next section makes this explicit by transforming the wave equation into the matter-field form.

---

## 4. Matter-field reading: a built-in background gauge field

The cylinder primitive's matter field is the complex combination ψ = *e* exp(*iφ*) introduced in [chapter 6 §2](06-base-for-maxwell.md). Under the unperturbed dynamics (matched chirality, no antisymmetric piece), ψ satisfies a free wave equation:

<!-- (∂_t² - c² ∂_x²) ψ = 0 -->
$$
\bigl(\partial_t^2 - c^2 \partial_x^2\bigr) \psi \;=\; 0
$$

The question is what equation ψ satisfies under the antisymmetric perturbation of §2.

The transformation from (*e*, *φ*) to ψ is non-linear, but for small perturbations around a uniform background ψ_0 = e_0 (real, constant), it linearises. Writing *e* = *e*_0 + δ*e* and *φ* = δ*φ* gives, to linear order,

<!-- δψ ≈ δe + i e_0 δφ -->
$$
\delta\psi \;\approx\; \delta e \;+\; i\, e_0\, \delta\varphi
$$

so that the (*e*, *φ*) components map onto the real and imaginary parts of δψ.

Applying this transformation to the wave equation under the antisymmetric perturbation (the algebra is straightforward but tedious; the key step is that *J* applied to (*e*, *φ*)^T corresponds to multiplication by *i* on δψ at the linearised level — the antisymmetric matrix is the matter-field's complex unit) yields:

<!-- (∂_t + i A_t)² ψ - c² (∂_x + i A_x)² ψ = 0 -->
$$
\bigl(\partial_t + i\, A_t\bigr)^2 \psi \;-\; c^2 \bigl(\partial_x + i\, A_x\bigr)^2 \psi \;=\; 0
$$

with the substrate-level gauge field

<!-- A_x = (ε_M / c²) · constant,   A_t = 0 -->
$$
A_x \;=\; \frac{\varepsilon_M}{c^2 \cdot e_0} \cdot (\text{geometric factor}), \qquad A_t \;=\; 0
$$

The exact normalization depends on the (*e*, *φ*) parameterisation conventions; the structural point is that the antisymmetric perturbation *is mathematically a covariant-derivative coupling of the matter field to a constant background gauge field*. The substrate-level *A_μ* is not generated by any matter source; it is a built-in feature of the medium, set by the antisymmetric chirality parameter χ_anti.

This is the central mathematical claim of the chapter. **A small antisymmetric chirality at the substrate level is structurally equivalent to a built-in constant background gauge field on the matter sector.** The cylinder primitive with χ_anti ≠ 0 is the cylinder primitive with χ_anti = 0 *plus* a substrate-level *A_μ* coupling.

Two things to note about this *A_μ*.

**It is constant.** A uniform substrate has no spatial inhomogeneity, so the built-in *A_μ* is a constant vector (or rather, a constant *A_x* along the cylinder axis; *A_t* vanishes by time-translation invariance of the matched antisymmetric perturbation). It does not satisfy any field equation; it is a fixed parameter, not a dynamical field.

**It is real.** χ_anti is a real dimensionless parameter, so *A_μ* (proportional to χ_anti) is a real vector. Real constant *A_μ* has the standard gauge-theory properties developed in §§6–7.

---

## 5. From substrate (*M*, *D*) to gauge sector (*E*, *B*)

The bridge to grid/maxwell.md (chapter 6) maps the cylinder primitive's matter field ψ onto the matter sector that grid/maxwell.md takes as input. The gauge-sector quantities *E* and *B* are derived from a separate gauge field *A_μ* whose introduction grid/maxwell.md inherits from axiom A4. *E* = −∂_t *A* − ∇*A*_t and *B* = ∇ × *A* (in standard notation).

Under the unperturbed cylinder primitive (matched chirality), the bridge is what chapter 6 establishes: ψ supplies the matter field; A4's gauge field supplies the gauge sector; Maxwell's equations follow. The substrate has no built-in *A_μ* of its own at this level.

Under the antisymmetric perturbation of §§2–4, the substrate *does* have a built-in *A_μ*. This built-in *A_μ* adds to the gauge field that A4 supplies, giving an effective gauge field

<!-- A_μ_eff = A_μ_A4 + A_μ_substrate -->
$$
A_\mu^{\mathrm{eff}} \;=\; A_\mu^{\mathrm{A4}} \;+\; A_\mu^{\mathrm{substrate}}
$$

The *E* and *B* fields derived from *A_μ^{eff}* therefore split into two contributions: a dynamical part sourced by charges and currents (the standard Maxwell theory built on *A_μ^{A4}*) and a built-in part determined by the substrate (set by *A_μ^{substrate}* ∝ χ_anti).

For the *symmetric* primitive (χ_anti = 0), the built-in part vanishes and the standard Maxwell construction is recovered exactly. For the asymmetric primitive (χ_anti ≠ 0), every region of space carries a small built-in *A_μ* in addition to whatever dynamical *A_μ* sources are present. *E* and *B* in such a substrate are not symmetric duals: they are tilted slightly by the built-in *A_μ*, in a way that depends on the specific geometric structure of the tilt.

The structural correspondence between substrate (*M*, *D*) and gauge sector (*E*, *B*) is therefore:

| Substrate parameter | Gauge-sector consequence |
|---|---|
| Matched chirality χ̃ ∈ (0, 1) | Vacuum impedance *Z*_0 = √(μ_0/ε_0); both polarizations at *c* |
| Antisymmetric χ_anti ≠ 0 | Built-in background *A_μ*; small built-in *E*-*B* asymmetry per region |

Whether the built-in *E*-*B* asymmetry is observable in any given region depends on the topology of that region — which is the content of the next two sections.

---

## 6. Aharonov-Bohm pure-gauge invisibility on extended space

A constant background *A_μ* in a topologically trivial region (open extended space, simply connected) is gauge-equivalent to zero. The argument is standard Aharonov-Bohm:

The local U(1) gauge transformation ψ → ψ exp(*i* Λ(*x*)) shifts *A_μ* → *A_μ* − ∂_μ Λ. For constant *A_μ*, the choice Λ(*x*) = *A*_μ *x*^μ gives ∂_μ Λ = *A*_μ, which subtracts the constant *A_μ* completely. After the transformation, *A_μ* = 0 and ψ is multiplied by the phase factor exp(*i A*_μ *x*^μ).

This is a pure phase rotation of the matter field at every point, with no observable consequence: probability densities |ψ|² are unchanged, energy expectation values are unchanged (the gauge transformation absorbs the *A_μ* into ψ in exactly the way the covariant derivative was constructed to permit), and any local measurement gives the same answer it would in a substrate with χ_anti = 0.

The extended-space conclusion: **a uniform substrate-level antisymmetric chirality is gauge-equivalent to zero on any topologically trivial region of the lattice.** No experiment confined to such a region can detect χ_anti.

This is what dissolves the apparent obstacle the chapter started with. The earlier worry was that a substrate-level directional preference would show up in the propagation of light through extended space, conflicting with the experimental isotropy of *c*. The resolution is that the directional preference in the substrate is gauge-equivalent to zero *exactly because* extended space is topologically trivial — it has no non-contractible loops on which the gauge transformation Λ(*x*) = *A*_μ *x*^μ would fail to be single-valued. So the directional preference simply does not exist as a propagation-level fact in extended space.

The macroscopic isotropy of *c* in 3D space is therefore *not in conflict* with a substrate-level antisymmetric chirality. The conflict was illusory; the gauge-theoretic structure of the matter field absorbs the substrate asymmetry as a global phase choice.

---

## 7. Wilson-loop observability on compact wraps

The same gauge transformation that absorbs constant *A_μ* on extended space *fails to be single-valued* on a compact wrap. This is the Aharonov-Bohm distinction between topologically trivial and non-trivial regions, and it is what makes χ_anti observable on torus wraps.

Consider a compact loop γ on a 2-torus (the L3 closure of [grid-duality](../grid-duality/) chapter 7). The candidate gauge transformation Λ(*x*) = *A*_μ *x*^μ requires ψ to pick up a phase ψ → ψ exp(*i* Λ) at every point, so that Λ must be defined globally on the torus. On a closed loop γ around one of the torus's non-contractible cycles, Λ accumulates a *non-trivial total phase*

<!-- ΔΛ = ∮_γ A_μ dx^μ -->
$$
\Delta\Lambda \;=\; \oint_\gamma A_\mu\, dx^\mu
$$

— the **Wilson-loop integral** of the gauge field around γ. For *A_μ* on extended space, this integral is zero (every loop is contractible to a point, so ∮ = 0 by Stokes' theorem applied to the trivially zero curl). For *A_μ* on a compact wrap, the integral is non-zero whenever γ is a non-contractible cycle: the cycle's length × the substrate's *A_μ* gives the accumulated phase.

The Wilson-loop integral is gauge-invariant — different choices of Λ on the wrap give the same value, because the gauge transformation must be single-valued, which forces ΔΛ to take a fixed value modulo 2π. **It is therefore a physical observable**: a wave-packet that wraps once around γ accumulates the phase ΔΛ and the phase is detectable in interference experiments.

For a torus T² with sides *L_u* and *L_w* (the metric-charge coordinates), and a substrate-level *A_μ* with components (*A_u*, *A_w*) = (χ_anti · *c*) · (*û*, *ŵ*) (some unit vector in the (*u*, *w*) plane, set by the helical fiber orientation), the two non-contractible cycles α and β have Wilson-loop phases

<!-- W_α = ∮_α A·dx = A_u L_u,    W_β = ∮_β A·dx = A_w L_w -->
$$
W_\alpha \;=\; A_u\, L_u, \qquad W_\beta \;=\; A_w\, L_w
$$

Both are dimensionless phases, both are gauge-invariant, both are proportional to χ_anti.

These two Wilson loops are the *substrate-level* phases that any wrapped excitation picks up by virtue of living on a compact torus with built-in *A_μ*. They are independent of the dynamical gauge field *A_μ^{A4}* that grid/maxwell.md uses — they are a separate, geometric contribution determined entirely by the substrate's antisymmetric chirality and the torus geometry.

The compact-wrap conclusion: **the substrate-level antisymmetric chirality is observable as Wilson-loop phases on compact wraps, with magnitude proportional to χ_anti.** This is where the asymmetry that §6 showed is invisible in extended space *does* show up, in exactly the location wrap-based particle physics already lives.

---

## 8. A speculative reading: anomalous magnetic moments

This section is more speculative than §§1–7. The Aharonov-Bohm structure of §§6–7 is mathematically firm; what follows is a *possible* macroscopic interpretation of that structure, offered as a target for downstream work rather than as a result this project supports. Whether the interpretation is correct — whether the substrate-level χ_anti developed here actually accounts for any observed anomalous magnetic moment — is for other projects to decide.

If one takes the Wilson-loop phases of §7 as contributing to the energy of any wavepacket that wraps around the torus, then for a torus knot with winding numbers (*m*, *n*) the contribution would take the form

<!-- ΔE_anomalous ∝ m W_α + n W_β -->
$$
\Delta E_{\mathrm{anomalous}} \;\propto\; m\, W_\alpha \;+\; n\, W_\beta
$$

— a contribution that depends on the winding pair (*m*, *n*) and on the substrate's χ_anti, and that *flips sign* under (*m*, *n*) → (−*m*, −*n*). Such a contribution would represent a "linear-in-(*m*, *n*) bias" breaking the (*m*, *n*) ↔ (−*m*, −*n*) symmetry — the matter / antimatter axis identified in the open-issues log of [metric-charge](../metric-charge/).

A coupling of the same contribution to the wave-packet's magnetic moment is plausible but not derived here. The detailed argument would require working through the matter-field coupling to *both* the substrate *A_μ* and the dynamical *A_μ^{A4}* in a specific wrap-based gauge theory; that calculation lives in metric-charge or a successor, not in grid-primitive. *If* such a coupling holds, then several speculative consequences would follow:

- A single substrate parameter χ_anti, with one sign, would produce a contribution to every torus knot's magnetic moment.
- The sign of the contribution would depend on the wrap orientation: opposite-orientation wraps would receive opposite-sign contributions.
- Different particle species would receive different magnitudes and signs of contribution, all proportional to the *same* underlying χ_anti.

These are conditional statements, not predictions this chapter establishes. They depend on the matter-field-to-gauge-field coupling argument that grid-primitive does not work through.

A coincidence worth flagging — without claiming it is more than a coincidence at this stage — is that the empirical signs of the small deviations from naive values in *measured* magnetic moments are *not* uniform across particle species. The electron's *g* sits slightly above the Dirac value of 2; the proton's *μ_p* / μ_N sits slightly below the naive constituent-quark estimate of 3. Whether this opposite-sign pattern is what one would expect from oppositely-oriented wraps under a single χ_anti, or whether it is unrelated, is exactly the kind of question downstream work would have to answer. The mere fact that *some* opposite-sign pattern exists in the data does not, by itself, support the χ_anti reading; many compositeness effects produce sign differences for unrelated reasons.

What this chapter *does* establish — and what it leaves open — is therefore:

- *Established (mathematically):* A small antisymmetric chirality perturbation at the substrate level is gauge-equivalent to a built-in background gauge field. On extended space it is unobservable. On compact wraps it produces gauge-invariant Wilson-loop phases.
- *Open (speculative):* Whether those Wilson-loop phases project onto observable magnetic moments in the way the conditional argument above suggests, whether any observed anomaly is partly or fully accounted for by this mechanism rather than by other contributions (QED loop corrections, compositeness, etc.), and what value (if any) χ_anti takes in nature — all of this is for follow-up work in metric-charge or its successors.

The chapter does not derive specific numerical values, does not pin χ_anti, does not assign wrap orientations to specific particle species, and does not work out the multi-link structure of composite particles. What it provides is a structural option that subsequent projects may invoke if and when the matter-field-to-gauge-field calculation is carried through.

---

## 9. Closing pointer

The cylinder primitive of [chapter 1](01-foundation.md) was committed to exact matched chirality and exact (*M*, *D*) symmetry — two simplifications that made the wave dynamics of [chapter 2](02-wave-on-a-primitive.md), the lattice cadence of [chapter 3](03-shear-and-c.md), and the bridges to grid/maxwell.md and grid/gravity.md (chapters 6–7) clean and tractable. Those simplifications survive intact: this chapter does not unwind them.

What this chapter does add is an explicit acknowledgement that the simplifications are choices, with a small structural parameter χ_anti available to relax them. The relaxation produces, mathematically, a built-in substrate-level gauge field on the matter sector. The built-in field is invisible in extended space (Aharonov-Bohm pure gauge) and produces gauge-invariant Wilson-loop phases on compact wraps. §8 raises anomalous magnetic moments and matter / antimatter sign asymmetry as *speculative* candidate macroscopic observables for those phases — possible interpretations to be tested in downstream work, not predictions this chapter establishes.

Whether χ_anti is non-zero in nature, what value it takes if so, and whether the speculative reading of §8 accounts for any observed anomaly are all open questions. The follow-up project [metric-charge](../metric-charge/) may invoke χ_anti as a structural input to its sheet-level treatment of charge if the speculative bridge proves useful; the bridge itself awaits the matter-field-to-gauge-field calculation that grid-primitive does not perform.

The chapter sequence is summarised in the project [README](README.md).
