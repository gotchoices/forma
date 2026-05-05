# Chapter 3 — Shear and *c*

This chapter takes the wave dynamics derived in [02-wave-on-a-primitive.md](02-wave-on-a-primitive.md) and confronts them with the lattice signal speed *c* required by GRID axiom A1. The cylinder turned out to support *two* natural propagating modes at different speeds *c*_+ and *c*_−. The lattice has just one signal speed *c*. Reconciling the two introduces a real algebraic constraint on the cylinder's symbolic constants. The question of this chapter is: *what does that constraint pin down, and what does it leave free?*

This chapter settles open question 1 of [README.md](README.md).

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The constraint: cylinder transit speed must equal *c* |
| 2 | Two mode speeds, one *c* — which is which? |
| 3 | Three candidate identifications, two eliminated |
| 4 | Imposing the constraint algebraically |
| 5 | Combining with the natural shear χ̃ = 1/√2 |
| 6 | What pins, what stays free |
| 7 | The slow mode and the vacuum-Maxwell tension |
| 8 | Summary of givens |

---

## 1. The constraint: cylinder transit speed must equal *c*

Mechanically, the cylinder primitive is a short transmission line of length *L*. Information injected at one end takes some amount of time *τ* to reach the other end. The lattice has its own opinion about how long that should take: from GRID axiom A1, the lattice signal speed is *c* (one cell per tick, one Planck length per Planck time), so by the definition of speed,

*τ* = *L*/*c*

This is just unit conversion — given the lattice cadence and the cylinder's length, the transit time follows.

But the cylinder also has its *own* internal physics that determines how fast a perturbation actually traverses it. Chapter 2 derived this from the stiffness matrix *M*, the inertias ρ and *I_φ*, and the chiral shear *K_eφ*. Whatever propagation speed the cylinder's internal wave equation predicts must agree with the lattice cadence: a perturbation cannot take *more* than *L*/*c* (that would be slower than light, breaking the lattice cadence) or *less* (that would be faster than light, breaking causality).

In short: the cylinder must propagate waves at speed *c*, where *c* is the speed GRID's axiom sets.

This sounds tautological — but it is not. Chapter 2 expressed the cylinder's natural wave speeds as functions of its symbolic constants. Forcing those speeds to equal the lattice's *c* is one real algebraic equation among five symbolic constants. The substantive question is what combination of the constants the equation pins down.

---

## 2. Two mode speeds, one *c* — which is which?

Chapter 2 §4 derived the dispersion relation. The result was *two* propagating modes, not one:

ω²(*k*) = *k*² · λ_±,    *c*_± = √λ_±

with λ_+ > λ_− whenever the chiral coupling *K_eφ* > 0. The two modes are different mixings of stress magnitude and azimuthal direction: a fast mode at speed *c*_+ and a slow mode at speed *c*_−. Both are real propagating waves; they differ in their polarization (which mix of *e* and *φ* is oscillating).

Now there is a question of identification. The lattice signal speed *c* is a *single* number. The cylinder has two mode speeds. So "the cylinder propagates at *c*" is ambiguous — which of the cylinder's modes is what we call light?

This is a modeling question, not a mathematical one. The math gives us two speeds; we have to decide what role each plays.

---

## 3. Three candidate identifications, two eliminated

Three candidates present themselves.

### Candidate A: the fast mode is light

*c*_+ = *c*. The fast mode is identified with the lattice signal speed. The slow mode is *something else* — a separate propagating excitation at a slower speed. It might be a heavy/massive mode that doesn't show up as long-wavelength radiation, or be screened in the continuum limit, or correspond to some other physical degree of freedom we have to make sense of. The slow mode exists as a real wave on the cylinder, but it isn't what the lattice scale calls light. This is the *working hypothesis* — what we will explore.

### Candidate B: the slow mode is light

*c*_− = *c*. The slow mode is light, and the fast mode is some superluminal excitation faster than *c*. This breaks GRID axiom A1 directly: the axiom states that nothing propagates faster than the lattice signal speed. A faster mode would violate causality on the lattice — perturbations could outrun the cell-by-cell update cadence. **Eliminated.**

### Candidate C: both modes have the same speed

*c*_+ = *c*_− = *c*. The two modes propagate at the same speed. For that to happen, the two eigenvalues λ_+ and λ_− would have to coincide.

Look at the eigenvalue formula from chapter 2 §4:

<!-- λ_± = (1/2)[K_ee/ρ + K_φφ/I_φ ± √D] where D = (K_ee/ρ − K_φφ/I_φ)² + 4 K_eφ²/(ρ I_φ) -->
$$
\lambda_{\pm} = \tfrac{1}{2}\!\left[\,\frac{K_{ee}}{\rho} + \frac{K_{\varphi\varphi}}{I_\varphi}
\;\pm\; \sqrt{\!\left(\frac{K_{ee}}{\rho} - \frac{K_{\varphi\varphi}}{I_\varphi}\right)^{\!2}
+ \frac{4\,K_{e\varphi}^{2}}{\rho\, I_\varphi}}\,\right]
$$

The "+" and "−" branches differ only by the sign in front of the square root. They coincide when that square root is zero, i.e. when the *discriminant* (the quantity under the root) vanishes:

<!-- (K_ee/ρ − K_φφ/I_φ)² + 4 K_eφ²/(ρ I_φ) = 0 -->
$$
\Big(\frac{K_{ee}}{\rho} - \frac{K_{\varphi\varphi}}{I_\varphi}\Big)^{\!2}
+ \frac{4\,K_{e\varphi}^{2}}{\rho\, I_\varphi}
\;=\; 0
$$

Both terms on the left are non-negative (the first is a real square; the second is a square divided by a positive quantity). Their sum is zero only if *both* are individually zero, which forces

- *K_ee*/ρ = *K_φφ*/*I_φ* (the diagonal channels have equal "bare" speeds), and
- *K_eφ* = 0 (no chiral coupling).

But *K_eφ* = 0 contradicts the structural requirement of chapter 2 §7 that the chiral coupling be nonzero — without it, the strain and azimuthal-direction channels propagate as decoupled, independent waves rather than as the coupled modes that the cylinder primitive is committed to. **Eliminated.**

### Working with Candidate A

That leaves Candidate A. The cost of this choice is that the cylinder primitive has a second propagating mode at a different (slower) speed than light. We will need to make sense of this in §7.

---

## 4. Imposing the constraint algebraically

With Candidate A fixed (*c*_+ = *c*), the constraint is

*c*² = λ_+

Substituting the closed-form expression for λ_+ from chapter 2 §4:

<!-- c² = (1/2)[K_ee/ρ + K_φφ/I_φ + √((K_ee/ρ − K_φφ/I_φ)² + 4 K_eφ²/(ρ I_φ))] -->
$$
c^{2} = \tfrac{1}{2}\!\left[\,\frac{K_{ee}}{\rho} + \frac{K_{\varphi\varphi}}{I_\varphi}
\;+\; \sqrt{\!\left(\frac{K_{ee}}{\rho} - \frac{K_{\varphi\varphi}}{I_\varphi}\right)^{\!2}
+ \frac{4\,K_{e\varphi}^{2}}{\rho\, I_\varphi}}\,\right]
$$

This is one equation in five symbolic constants — *K_ee*, *K_φφ*, *K_eφ*, ρ, *I_φ*. One equation, five unknowns: it pins one combination of them, not all five.

### Simplifying assumption

To make the structure visible without the algebra getting overwhelming, take the simplifying special case where the longitudinal and azimuthal channels have equal "bare" properties:

ρ = *I_φ*       and       *K_ee* = *K_φφ* ≡ *K*

This is not a derivation; it is a working assumption that compresses the algebra to one symbolic stiffness *K* and one symbolic inertia ρ, plus the chiral coupling *K_eφ*. The general case has the same structural conclusion (one constraint, several free parameters), but with messier formulas. We note where the general case differs.

Under this special case, the eigenvalues from chapter 2 §6 collapse to:

λ_± = (*K*/ρ)(1 ± χ̃)

where χ̃ = *K_eφ* / √(*K_ee* · *K_φφ*) = *K_eφ*/*K* is the dimensionless shear from chapter 1.

The constraint *c*² = λ_+ becomes:

*c*² = (*K*/ρ)(1 + χ̃)

— a single equation in three unknowns (*K*, ρ, χ̃). This is the special-case form of the constraint we will combine with chapter 2's natural shear value next.

---

## 5. Combining with the natural shear χ̃ = 1/√2

Chapter 2 §7 identified χ̃ = 1/√2 ≈ 0.707 as the *natural* shear value — the geometric mean of the stable range (0, 1), at which the chiral coupling is well-engaged but the stability margin is substantial. Treat this as an additional input (independent of the *c* constraint of §4) and substitute into the special-case relation:

*c*² = (*K*/ρ)(1 + 1/√2)

Solve for *K*/ρ:

*K*/ρ = *c*² / (1 + 1/√2)

The right-hand side simplifies if we rationalize the denominator. Multiply numerator and denominator by √2:

*K*/ρ = *c*² · √2 / (√2 + 1)

then by (√2 − 1) on top and bottom:

*K*/ρ = *c*² · √2(√2 − 1) / [(√2 + 1)(√2 − 1)] = *c*² · √2(√2 − 1) / 1 = *c*² · (2 − √2)

So

<!-- K/ρ = c² · (2 − √2) ≈ 0.586 c² -->
$$
\frac{K}{\rho} \;=\; c^{2}\,(2 - \sqrt{2}) \;\approx\; 0.586\, c^{2}
$$

The ratio *K*/ρ — the squared "diagonal" speed of the cylinder — is now pinned in terms of *c* alone.

Together with χ̃ = 1/√2 (which pins *K_eφ*/*K*), all the *dimensionless* stiffness ratios in the special case are fixed:

- *K_eφ* / *K* = 1/√2
- *K* / ρ = (2 − √2) *c*²

What is *not* pinned: the *absolute* scale of *K* (and correspondingly ρ); the cylinder length *L*; the cross-section radius *r*.

---

## 6. What pins, what stays free

Collecting the parameters and their status after the *c* constraint and the natural-shear value:

| Parameter | Status |
|---|---|
| Dimensionless shear χ̃ = *K_eφ*/√(*K_ee K_φφ*) | **Pinned**: χ̃ = 1/√2 (chapter 2 §7) |
| Speed-squared ratio *K*/ρ | **Pinned**: *K*/ρ = (2 − √2) *c*² ≈ 0.586 *c*² |
| Absolute scale of *K* (and correspondingly ρ) | **Free** |
| Cylinder length *L* | **Free** |
| Cylinder cross-section radius *r* | **Free** |
| Slow-mode speed *c*_− | **Determined**: see §7 |

Three free parameters survive: an overall stiffness scale (which sets *K* and ρ together while keeping their ratio fixed), the cylinder length *L*, and the cross-section radius *r*. Whether further physical constraints — the entropy account in chapter 4, the Maxwell bridge in chapter 6, the kink-loss derivation of α in chapter 8 — pin any of these is a downstream question.

A note on the simplifying assumption ρ = *I_φ*, *K_ee* = *K_φφ*. In the *general* case, the *c* constraint pins one combination of (*K_ee*, *K_φφ*, *K_eφ*, ρ, *I_φ*), but the specific combination is more elaborate than just *K*/ρ. The natural-shear input adds a second constraint. The qualitative conclusion still holds (two relations are pinned; an overall scale, *L*, and *r* remain free); only the specific formulas change. The clean special-case formulas of §4–§5 are the simplest expression of this structure; the general case has the same shape with more terms.

---

## 7. The slow mode and the vacuum-Maxwell tension

Candidate A's choice (the fast mode is light) leaves the slow mode at a definite, determinable speed. From the eigenvalue formula in the special case:

*c*_− = √(*K*/ρ) · √(1 − χ̃)

Substituting χ̃ = 1/√2 and *K*/ρ from §5:

*c*_− = *c* · √((1 − 1/√2) / (1 + 1/√2))

The factor under the square root is roughly 0.293/1.707 ≈ 0.172, so:

*c*_− ≈ 0.414 · *c*

That is, the cylinder primitive predicts a *second* propagating wave at roughly 41% of the speed of light.

Vacuum Maxwell, by contrast, has two photon polarizations both propagating at exactly *c*. There is no second, slower wave in vacuum. So either the cylinder primitive is making a wrong prediction, or the slow mode is not a *photon* — it is something else that the lattice scale either does not see or does not call light.

This is a real tension. Three plausible resolutions, each of which is a downstream question to be addressed elsewhere:

1. **The slow mode picks up a mass when the lattice is assembled.** A "massive" mode has a gap in its dispersion relation: ω²(*k* = 0) ≠ 0. Such a mode does not propagate as a long-wavelength wave at all — at low frequencies it sits as a localized oscillation. If 2D-lattice assembly (chapter 5) gives the slow mode this gap, the Maxwell bridge at long wavelengths would see only the fast mode, with both photon polarizations at *c*. The slow mode might still exist as a separate massive excitation, possibly identifiable as a matter-like or non-photon physical entity at the lattice scale.

2. **Lattice assembly averages the two speeds.** Coupling many primitives in a 2D periodic lattice produces collective modes that may differ from single-primitive modes. The cylinder's two mode speeds *c*_+ and *c*_− might combine, in the lattice, into effective collective modes that all propagate at *c*. This is a computation that has to be done at the 2D-lattice level (chapters 5–6).

3. **The slow mode is a real prediction.** In some real media (certain crystals, magneto-optical materials), light propagates at different speeds for different polarizations — birefringence, optical activity. If the cylinder primitive predicts a tiny similar effect in vacuum, that is an empirically falsifiable feature. Existing laboratory bounds on photon-polarization birefringence in vacuum are very tight, however, so this option is unlikely to survive observational scrutiny.

This chapter does not resolve the tension. It identifies the candidate resolutions and notes that the next chapters — assembly into a 2D lattice, then the bridge to Maxwell — are where it has to be addressed. The cylinder primitive itself does not fail at this single-primitive level; what it carries is an obligation to its successor chapters.

---

## 8. Summary of givens

The cylinder primitive's parameters, after this chapter:

- The lattice signal speed *c* (axiom A1) pins the cylinder's fast-mode speed: *c*_+ = *c*.
- Combined with the natural shear χ̃ = 1/√2 (chapter 2 §7), the dimensionless stiffness ratios *K_eφ*/*K* and *K*/ρ are both determined by *c* alone — one is 1/√2, the other is (2 − √2) *c*².
- An overall stiffness scale, the cylinder length *L*, and the cross-section radius *r* remain as free parameters of the primitive.
- The slow-mode speed *c*_− ≈ 0.414 *c* is determined by the same constraints. Its physical role is unresolved at this chapter; reconciling it with vacuum Maxwell is an obligation for the lattice-assembly and Maxwell-bridge chapters that follow.

The next chapter takes up whether the cylinder primitive's stress vector field, assembled into a 2D lattice and excited at finite temperature, supplies the entropy that Jacobson's argument requires for entropic gravity.
