# Chapter 3 — Shear and *c*

This chapter takes the wave dynamics derived in [02-wave-on-a-primitive.md](02-wave-on-a-primitive.md) — two propagating modes with speeds *c*₊ and *c*₋, generally unequal when the chiral coupling *K_eφ* > 0 — and confronts them with the lattice signal speed *c* required by GRID axiom A1. The question is whether matching the cylinder's internal dynamics to the lattice cadence pins the primitive's parameters uniquely or leaves a family of solutions.

This chapter settles open question 1 of [README.md](README.md).

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The constraint: cylinder transit time matches lattice cadence |
| 2 | Two mode speeds, one *c* — which is which? |
| 3 | Three candidate identifications |
| 4 | Imposing the constraint algebraically |
| 5 | Combining with equipartition (χ̃ = 1/√2) |
| 6 | What pins, what stays free |
| 7 | The two-modes vs vacuum-Maxwell tension |
| 8 | Summary of givens |

---

## 1. The constraint — cylinder transit time matches lattice cadence

GRID axiom A1 fixes a single propagation speed for the lattice: one cell per tick, one Planck length per Planck time. Call this speed *c*. Inside the cylinder primitive, a perturbation entering at one end takes some real amount of time *τ* to reach the other end. Two relations hold a priori:

- **Definitional.** *τ* = *L*/*c*. This is just unit conversion: the *cadence* of the lattice (one cell per tick) measured against the cylinder's length *L*.
- **Substantive.** *τ* = *L* / *c*_internal, where *c*_internal is whatever speed the cylinder's *own* dynamics propagate a perturbation. This is an algebraic statement about the cylinder's stiffness matrix, mass density, and shear coupling.

Both are facts about the same *τ*, so they must agree:

*c*_internal = *c*

This is not a tautology. The left-hand side is determined by the cylinder's symbolic constants (the entries of *M*, the inertias ρ and *I_φ*, and the geometry *r*). The right-hand side is a single number set by the lattice. Forcing one to equal the other is a real constraint on the primitive.

The substantive question of this chapter is: *what does this constraint pin down, and what does it leave free?*

---

## 2. Two mode speeds, one *c* — which is which?

Chapter 2 derived the dispersion relation for waves on a single cylinder. The result was *two* propagating modes per primitive:

ω²(*k*) = *k*² · λ_±,    *c*_± = √λ_±

with λ_± the two eigenvalues of the matrix *D*⁻¹*M*, where *D* = diag(ρ, *I_φ*). When the off-diagonal *K_eφ* is nonzero (which is required for propagation at all — chapter 2 §7), the two eigenvalues split:

*c*_+ > *c*_−

Both are real; both correspond to physical waves; they differ in which polarization (which mix of strain magnitude and azimuthal direction) is propagating.

The lattice signal speed *c* is, by contrast, a *single* number. So the equation "*c*_internal = *c*" is ambiguous: which mode is "the internal speed"? The cylinder has two. We have to decide what to identify *c* with.

This is not a mathematical question — it is a *modeling* question, asking which of the cylinder's modes plays the role of "light" at the lattice scale.

---

## 3. Three candidate identifications

Three candidates present themselves.

**Candidate A.** *c*_+ = *c*. The fast mode is identified with the lattice signal speed. The slow mode is something else — a second physical excitation that propagates more slowly than light at every point. It might decouple from the photon sector (a heavy mode), or be a massive matter-like excitation, or be screened in the continuum limit. It exists, but it is not what we call light.

**Candidate B.** *c*_− = *c*. The slow mode is identified with light. The fast mode is some superluminal excitation. This is incompatible with GRID axiom A1, which states that nothing propagates faster than *c*: information travels strictly at one cell per tick along causal directions. A faster mode would violate causality on the lattice. Candidate B is therefore not viable.

**Candidate C.** *c*_+ = *c*_− = *c*. Both modes propagate at the same speed. This requires the two eigenvalues λ_+ and λ_− to be equal — the matrix *D*⁻¹*M* must be a scalar multiple of the identity. For our 2 × 2 *M* with positive *K_ee* and *K_φφ*, the only way to make the eigenvalues coincide is for the discriminant in the quadratic formula to vanish:

(*K_ee*/ρ − *K_φφ*/*I_φ*)² + 4 *K_eφ*² / (ρ *I_φ*) = 0

Both terms are non-negative, so the only solution is *K_ee*/ρ = *K_φφ*/*I_φ* AND *K_eφ* = 0. But *K_eφ* = 0 contradicts chapter 2's theorem 2 (shear is necessary for propagation): the two channels would decouple and waves could not propagate as coupled stretch-and-twist motions. Candidate C is therefore inconsistent with the propagation requirement.

Candidates B and C are eliminated. **Candidate A is the working hypothesis.**

That choice has a downstream cost: the cylinder primitive carries a second propagating mode at a different (slower) speed than light. Whether this contradicts vacuum Maxwell at the lattice scale, or is reconciled by the lattice assembly in later chapters, is taken up in §7.

---

## 4. Imposing the constraint algebraically

With Candidate A fixed, the constraint is:

*c*² = λ_+

Substituting from chapter 2 §4:

<!-- c² = (1/2)[K_ee/ρ + K_φφ/I_φ + √((K_ee/ρ − K_φφ/I_φ)² + 4 K_eφ²/(ρ I_φ))] -->
$$
c^2 = \tfrac{1}{2}\!\left[\,\frac{K_{ee}}{\rho} + \frac{K_{\varphi\varphi}}{I_\varphi}
\;+\; \sqrt{\!\left(\frac{K_{ee}}{\rho} - \frac{K_{\varphi\varphi}}{I_\varphi}\right)^{\!2}
+ \frac{4\,K_{e\varphi}^{2}}{\rho\, I_\varphi}}\,\right]
$$

This is one equation in five symbolic constants: *K_ee*, *K_φφ*, *K_eφ*, ρ, *I_φ*. It is a real constraint; it pins one combination of these five.

To make the structure visible without losing the substance, take the simplifying special case where the longitudinal and azimuthal "natural frequencies" coincide:

ρ = *I_φ*       and       *K_ee* = *K_φφ* ≡ *K*

This is not a derivation; it is a working assumption that strips the algebra to one symbolic stiffness *K* and one symbolic inertia ρ. The general case has the same structural conclusion (one constraint, several free parameters), but the formulas are messier. We will note where the general case differs from the special case and flag any conclusion that depends on the assumption.

Under this special case, the eigenvalues simplify to (chapter 2 §6):

λ_± = (*K*/ρ)(1 ± χ̃),    where χ̃ = *K_eφ* / √(*K_ee* · *K_φφ*) = *K_eφ*/*K*.

The constraint *c*² = λ_+ becomes:

*c*² = (*K*/ρ)(1 + χ̃)

— a single equation in *K*, ρ, and χ̃. One constraint, three quantities — two combinations remain free.

---

## 5. Combining with equipartition (χ̃ = 1/√2)

Chapter 2 §7 identified χ̃ = 1/√2 as the *natural* shear value — the equipartition point at which the propagating modes carry equal energy in their strain and azimuthal channels. Equipartition is a property of the system at thermodynamic balance; it is not something that the static dispersion relation alone forces, but it is the value the system would settle into under typical thermal conditions.

Treating equipartition as a separate input (in addition to the *c* constraint of §4) and substituting χ̃ = 1/√2 into the special-case relation:

*c*² = (*K*/ρ)(1 + 1/√2)

so:

<!-- K / ρ = c² / (1 + 1/√2) = c² · 2(√2 − 1) ≈ 0.586 · c² -->
$$
\frac{K}{\rho} = \frac{c^{2}}{1 + 1/\sqrt{2}} = c^{2} \cdot 2(\sqrt{2} - 1) \approx 0.586\, c^{2}
$$

The ratio *K*/ρ — the natural mode speed squared in the decoupled limit — is now fixed in terms of *c*.

Together with χ̃ = 1/√2 (which pins *K_eφ*/*K*), all *dimensionless* stiffness ratios in the special case are now determined:

- *K_eφ* / *K* = 1/√2
- *K*/ρ = *c*²/(1 + 1/√2)

What is *not* pinned: the absolute scale of *K* (and correspondingly ρ); the cylinder length *L*; the cross-section radius *r*.

---

## 6. What pins, what stays free

Collecting the parameters and their status after the *c* constraint and equipartition:

| Parameter | Status |
|---|---|
| Dimensionless shear χ̃ = *K_eφ*/√(*K_ee K_φφ*) | **Pinned**: χ̃ = 1/√2 (equipartition) |
| Speed-squared ratio *K*/ρ | **Pinned**: *K*/ρ = *c*² · 2(√2 − 1) |
| Absolute scale of *K* (and correspondingly ρ) | **Free** |
| Cylinder length *L* | **Free** |
| Cylinder cross-section radius *r* | **Free** |
| Slow-mode speed *c*_− | **Determined**: *c*_− = √(*K*/ρ) · √(1 − 1/√2) ≈ 0.414 · *c* — see §7 |

Three free parameters survive — an overall stiffness scale, *L*, and *r* — beyond what the lattice cadence and equipartition alone determine. Whether further physical constraints (the entropy account, Maxwell recovery, the kink-loss derivation of α) fix any of these is a downstream question.

A note on the simplifying assumption ρ = *I_φ*, *K_ee* = *K_φφ*. In the general case, the *c* constraint pins one combination of (*K_ee*, *K_φφ*, *K_eφ*, ρ, *I_φ*), but the specific combination is more elaborate than *K*/ρ. Equipartition adds another constraint. The conclusion that "two ratios are pinned and three parameters remain free" carries over (4 ratios − 1 *c* constraint − 1 equipartition = 2 pinned, several free). The clean special-case formulas of §4–§5 are the simplest expression of this structure; the general case has the same shape.

---

## 7. The two-modes vs vacuum-Maxwell tension

Candidate A leaves the slow mode at a definite speed:

*c*_− = √(*K*/ρ) · √(1 − χ̃) = *c* · √((1 − 1/√2) / (1 + 1/√2)) ≈ 0.414 · *c*

A genuine second propagating mode at about 0.41 *c* is not what vacuum Maxwell looks like. Vacuum Maxwell has two photon polarizations both propagating at *c*; there is no second, slower wave. So either the cylinder primitive is making a wrong prediction, or the slow mode is not the *photon* polarization at all — it is something else that the lattice scale either doesn't see or doesn't call light.

Three resolutions are conceivable, each of which is a downstream question to be addressed (or rejected) elsewhere:

1. **The slow mode decouples in the continuum limit.** If the slow mode picks up a mass (a gap in the dispersion relation) once the lattice is assembled, it will not propagate as a long-wavelength wave at any speed — it will sit as a localized excitation. Maxwell at the long-wavelength scale would see only the fast mode (photon polarizations).

2. **Lattice assembly averages the two speeds.** Coupling many primitives in a 2D periodic lattice may produce collective modes whose speed is some effective combination of *c*_+ and *c*_−. Whether that combination equals *c* is a 2D-lattice calculation, not a single-primitive one.

3. **The slow mode is a real prediction.** Some media — magneto-optical materials, certain crystals — do support birefringent propagation. If the cylinder primitive predicts a tiny deviation from the vacuum Maxwell two-equal-speed claim, that is an empirically falsifiable feature. Existing laboratory bounds on photon-polarization birefringence in vacuum are very tight, however, so this option is unlikely to survive observational scrutiny.

The chapter does not resolve the tension. It flags it, identifies the candidate resolutions, and notes that the next chapters (assembly into a 2D lattice, then bridge to Maxwell) are where it has to be addressed. The cylinder primitive itself does not fail at this stage — but it carries an obligation to its successor chapters.

---

## 8. Summary of givens

The cylinder primitive's parameters, after this chapter:

- The lattice signal speed *c* (axiom A1) pins the cylinder's fast-mode speed: *c*_+ = *c*.
- Combined with the equipartition shear χ̃ = 1/√2 (chapter 2 §7), the dimensionless stiffness ratios *K_eφ*/*K* and *K*/ρ are both determined by *c* alone.
- An overall stiffness scale, the cylinder length *L*, and the cross-section radius *r* remain as free parameters of the primitive.
- The slow mode *c*_− is determined by the same constraints to be ≈ 0.414 *c*. Its physical role is unresolved at this chapter; resolution is an obligation for the lattice-assembly and Maxwell-bridge chapters that follow.

The next chapter takes up whether the cylinder primitive's stress vector field, assembled into a 2D periodic lattice and excited at finite temperature, supplies the entropy that Jacobson's argument requires for entropic gravity.
