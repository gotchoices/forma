# Chapter 2 — Wave on a Single Primitive

This chapter takes the foundation established in [01-foundation.md](01-foundation.md) — a cylinder with two coupled fields *e(x, t)* and *φ(x, t)* and a stiffness matrix *M* — and derives the wave dynamics on a single primitive. The goal is to characterize the propagating modes, locate the stability boundary, identify the natural value of the shear, and prove that the medium propagates waves symmetrically in both directions despite its chirality.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The Lagrangian density of the cylinder |
| 2 | Wave equations for *e(x, t)* and *φ(x, t)* |
| 3 | Plane-wave ansatz and the eigenvalue problem |
| 4 | The dispersion relation — two branches |
| 5 | The two natural modes (eigenvectors of *D⁻¹M*) |
| 6 | Stability boundary and the degenerate limit χ̃ → 1 |
| 7 | Equipartition and the natural shear χ̃ = 1/√2 |
| 8 | Bidirectional propagation symmetry |
| 9 | Linear superposition and pulse pass-through |
| 10 | Summary of givens |

---

## 1. The Lagrangian density of the cylinder

A *Lagrangian* is the standard tool for deriving equations of motion in classical mechanics. It is a single scalar quantity *L* = *T* − *V* (kinetic energy minus potential energy) whose time integral, the action *S* = ∫*L* d*t*, is extremized along the system's actual trajectory. The principle of least action says: physical motion is the trajectory that makes *S* stationary. The mechanics that follows from this — the **Euler–Lagrange equations** — produces the system's equations of motion automatically once *L* is specified. Choosing *L* is the substantive modeling step; the derivation of the equations of motion is then mechanical.

For a continuous system like the cylinder, we work with a Lagrangian *density* *L̃*: energy per unit length along the cylinder. The total Lagrangian is *L* = ∫₀^*L* *L̃* d*x*, and the action is the double integral *S* = ∫∫*L̃* d*x* d*t*. Euler–Lagrange applied to *L̃* gives the wave equations. (Note: the symbol *L* denotes both the cylinder's length and the Lagrangian; context makes which is meant unambiguous, and we will avoid using both in the same sentence.)

For the cylinder, *L̃* has two contributions.

**Kinetic density.** The two fields *e* and *φ* both move in time. The longitudinal motion has an associated mass density ρ (per unit length); the azimuthal motion has an associated rotational moment of inertia *I_φ* (per unit length). The kinetic energy per unit length is the standard quadratic form:

<!-- T̃ = (ρ/2)(∂_t e)² + (I_φ/2)(∂_t φ)² -->
$$
\widetilde{T} = \tfrac{1}{2}\rho\,(\partial_t e)^2 + \tfrac{1}{2} I_\varphi\,(\partial_t \varphi)^2
$$

Both ρ and *I_φ* are kept symbolic. They are independent of each other: the rubber-cylinder picture suggests that longitudinal mass and rotational inertia are different physical properties of the cylinder material, and the project does not commit to a relation between them at this stage. If a later chapter forces a relation, it will be flagged explicitly.

**Potential density.** The potential energy comes from spatial *gradients* of the fields. A perturbation that varies along the cylinder costs energy proportional to how steeply it varies, weighted by the stiffness matrix *M*:

<!-- V̄ = (1/2) (∂_x e, ∂_x φ) · M · (∂_x e, ∂_x φ)ᵀ -->
$$
\widetilde{V} = \tfrac{1}{2}
\begin{pmatrix} \partial_x e & \partial_x \varphi \end{pmatrix}
M
\begin{pmatrix} \partial_x e \\ \partial_x \varphi \end{pmatrix}
= \tfrac{1}{2}\!\left[\,K_{ee}(\partial_x e)^2 + 2 K_{e\varphi}(\partial_x e)(\partial_x \varphi) + K_{\varphi\varphi}(\partial_x \varphi)^2\right]
$$

The cross term 2*K_eφ*(∂_x *e*)(∂_x *φ*) is what couples strain and phase together. Without it (*K_eφ* = 0), the two fields would have independent potential energies and no shared dynamics — the cylinder would behave like two decoupled springs, neither of which could pull the other along.

The Lagrangian density is the difference:

*L̃* = *T̃* − *Ṽ*

This is the energy bookkeeping for one cylinder, parameterized by the symbolic constants ρ, *I_φ*, *K_ee*, *K_φφ*, *K_eφ*. The next section converts *L̃* into equations of motion.

---

## 2. Wave equations for *e(x, t)* and *φ(x, t)*

The Euler–Lagrange equations applied to a Lagrangian density of two fields take the form:

<!-- ∂L̃/∂q_a − ∂_t (∂L̃/∂(∂_t q_a)) − ∂_x (∂L̃/∂(∂_x q_a)) = 0 -->
$$
\frac{\partial \widetilde{L}}{\partial q_a}
- \partial_t\!\left(\frac{\partial \widetilde{L}}{\partial(\partial_t q_a)}\right)
- \partial_x\!\left(\frac{\partial \widetilde{L}}{\partial(\partial_x q_a)}\right) = 0
$$

where *q_a* runs over the fields (here *q*₁ = *e*, *q*₂ = *φ*). Our *L̃* depends only on the derivatives ∂_t *q_a* and ∂_x *q_a*, not on *q_a* itself, so the first term vanishes. Working out the time-derivative term and the space-derivative term for each field gives:

<!-- ρ ∂_t² e = K_ee ∂_x² e + K_eφ ∂_x² φ -->
<!-- I_φ ∂_t² φ = K_eφ ∂_x² e + K_φφ ∂_x² φ -->
$$
\begin{aligned}
\rho\, \partial_t^2 e &= K_{ee}\, \partial_x^2 e + K_{e\varphi}\, \partial_x^2 \varphi \\
I_\varphi\, \partial_t^2 \varphi &= K_{e\varphi}\, \partial_x^2 e + K_{\varphi\varphi}\, \partial_x^2 \varphi
\end{aligned}
$$

These are a coupled pair of second-order partial differential equations — one for each field — connecting the time-evolution at any point to the curvature in space at that point. Each field's evolution depends on the second spatial derivative of *both* fields, mixed by the stiffness matrix.

In matrix form, with **u** = (*e*, *φ*)ᵀ and *D* = diag(ρ, *I_φ*):

<!-- D ∂_t² u = M ∂_x² u -->
$$
D\, \partial_t^2\, \mathbf{u} = M\, \partial_x^2\, \mathbf{u}
$$

This is the master equation for the cylinder. Two features worth marking now:

- **Linear.** Each term is at most linear in **u** and its derivatives. There is no *e*², no *e*·*φ* without derivatives, no nonlinearity. Linearity is what underwrites the superposition arguments in §9.

- **Coupled.** The off-diagonal entry *K_eφ* in *M* ties the two equations together. A second derivative in *e* drives *φ*, and vice versa. With *K_eφ* = 0 the two equations decouple into two independent wave equations.

The cross-coupling has a clean physical reading: when the stress-magnitude field has curvature in space (nonzero ∂_x² *e*), it drives the azimuthal-direction field, rotating where the stress points; symmetrically, a curvature in *φ* drives changes in stress magnitude. This is the formal expression of "magnitude and azimuth drive each other" — the off-center longitudinal load propagates as a coupled (magnitude, direction) wave.

The wave equations are linear in the polar coordinates (*e*, *φ*); for small perturbations around a non-zero background stress, this linearization is well-defined. The polar-coordinate singularity at *e* = 0 (chapter 1 §3) is not encountered as long as the perturbations stay away from the origin of the stress vector — which is the small-perturbation regime where chapter 2's analysis lives. For the full nonlinear topology including defects, see chapter 4.

---

## 3. Plane-wave ansatz and the eigenvalue problem

To find the propagating modes of the cylinder, we look for solutions that have the form of a traveling plane wave. A plane wave varies sinusoidally in both space and time:

<!-- u(x, t) = A exp(i(kx − ωt)) -->
$$
\mathbf{u}(x, t) = \mathbf{A}\, e^{i(k x - \omega t)}
$$

where:
- **A** = (*A_e*, *A_φ*)ᵀ is a constant complex two-vector — the *amplitude* of the wave in each field.
- *k* is the **wavenumber** — how many radians of phase fit per unit length along the cylinder. *k* > 0 corresponds to a wave moving in the +*x* direction; *k* < 0 to one moving in −*x*.
- ω is the **angular frequency** — how many radians of phase pass at a fixed point per unit time.

This ansatz makes the two derivative operations into multiplications:
- ∂_t² **u** picks up a factor (−*i*ω)² = −ω² .
- ∂_x² **u** picks up a factor (*i k*)² = −*k*² .

Substituting into the master equation *D* ∂_t² **u** = *M* ∂_x² **u** and cancelling the common exponential factor and minus sign:

<!-- ω² D A = k² M A -->
$$
\omega^2\, D\, \mathbf{A} = k^2\, M\, \mathbf{A}
$$

Multiplying both sides by *D*⁻¹ from the left puts this in the form of a standard eigenvalue problem:

<!-- (ω²/k²) A = D⁻¹ M A -->
$$
\frac{\omega^2}{k^2}\, \mathbf{A} = D^{-1} M\, \mathbf{A}
$$

The amplitude vector **A** is an eigenvector of *D*⁻¹*M*; the ratio ω²/*k*² is the corresponding eigenvalue. Because both *D* and *M* are real and positive-definite, *D*⁻¹*M* has two real positive eigenvalues, so the equation gives two distinct real values of ω² for each *k* — these are the two branches of the dispersion relation, derived next.

---

## 4. The dispersion relation — two branches

A brief refresher on what eigenvalues and eigenvectors mean.

A square matrix *A* acts on vectors. For most vectors **v**, the action *A***v** rotates and rescales **v**. But for special vectors — *eigenvectors* — *A* only rescales, without rotating: *A***v** = λ**v**. The factor λ is the *eigenvalue*. A 2 × 2 matrix has up to two eigenvectors, each with its own eigenvalue, and they form a "natural basis" for the matrix's action: any vector decomposes as a sum of eigenvectors, and *A* acts on each piece by simple scaling.

For our problem, *A* is the matrix *D*⁻¹*M*. Its two eigenvectors **v**₊ and **v**₋, with eigenvalues λ₊ and λ₋, are the natural mode shapes of the cylinder primitive. From the plane-wave ansatz, ω²/*k*² = λ_± at each *k*. Therefore:

<!-- ω²(k) = k² · λ_± -->
$$
\omega^2(k) = k^2 \cdot \lambda_{\pm}
$$

This gives two dispersion branches, one for each eigenvalue. Both branches give a frequency that scales linearly with |*k*|, so the phase speed for each mode is constant (independent of *k*):

*c*₊ = √λ₊,  *c*₋ = √λ₋

The medium is **non-dispersive** — waves of different wavelengths propagate at the same speed within each branch. This is essential for faithful wave transmission: a localized pulse, which is a superposition of many wavenumbers, will keep its shape as it propagates because all its components travel together. A dispersive medium would cause pulses to spread; the cylinder primitive does not.

The eigenvalues λ_± follow from the characteristic equation det(*D*⁻¹*M* − λ*I*) = 0. Writing it out for our 2 × 2 matrix gives a quadratic in λ. After algebra:

<!-- λ_± = (1/2)[K_ee/ρ + K_φφ/I_φ ± √((K_ee/ρ − K_φφ/I_φ)² + 4 K_eφ²/(ρ I_φ))] -->
$$
\lambda_{\pm} = \tfrac{1}{2}\!\left[\,\frac{K_{ee}}{\rho} + \frac{K_{\varphi\varphi}}{I_\varphi}
\;\pm\; \sqrt{\!\left(\frac{K_{ee}}{\rho} - \frac{K_{\varphi\varphi}}{I_\varphi}\right)^{\!2}
+ \frac{4\,K_{e\varphi}^2}{\rho\, I_\varphi}}\;\right]
$$

The two natural mode speeds are *c*_± = √λ_±. For *K_eφ* = 0 (no shear) the cross term vanishes and the two speeds reduce to √(*K_ee*/ρ) and √(*K_φφ*/*I_φ*) — strain and phase propagate independently, each at its own speed. As *K_eφ* grows, the cross term grows and the two speeds split further apart, with *c*₊ increasing and *c*₋ decreasing.

---

## 5. The two natural modes

The eigenvectors **v**₊ and **v**₋ of *D*⁻¹*M* describe the *shapes* of the two propagating modes — that is, what mix of strain and phase oscillates in unison along each branch.

For *K_eφ* = 0 (decoupled limit), the eigenvectors point along the coordinate axes:
- **v**₊ = (1, 0)ᵀ — pure strain, oscillating with no phase content
- **v**₋ = (0, 1)ᵀ — pure phase, oscillating with no strain content

The two modes are simply the strain mode and the phase mode, propagating independently at their respective speeds.

For *K_eφ* > 0, the eigenvectors tilt away from the axes. Each natural mode now contains *both* strain and phase, in a fixed ratio determined by the stiffness matrix entries:

<!-- v_+ ∝ (cos θ, sin θ)ᵀ, v_− ∝ (−sin θ, cos θ)ᵀ -->
$$
\mathbf{v}_+ \propto \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}, \qquad
\mathbf{v}_- \propto \begin{pmatrix} -\sin\theta \\ \cos\theta \end{pmatrix}
$$

where the mixing angle θ depends on *K_ee*, *K_φφ*, *K_eφ*, ρ, *I_φ*. As *K_eφ* grows toward the stability limit, θ rotates from 0 toward π/4 (45°). At equipartition (χ̃ = 1/√2 — see §7), the mixing is moderate; at the stability boundary (χ̃ → 1), the slow mode's eigenvalue collapses to zero.

Mechanical reading: in each natural mode, the stress-magnitude oscillation at one position is locked to a rotation of the stress's azimuthal direction at the same position. The fast mode oscillates magnitude and direction in phase (the stress vector "stretches and rotates" together); the slow mode oscillates them out of phase (stretching cancels rotation, partially), and the partial cancellation slows the propagation.

A useful physical analog: in optics, a chiral medium (such as a sugar solution) has two natural modes — left-circular and right-circular polarized light — that propagate at slightly different speeds. The cylinder primitive's two natural modes correspond exactly to L-circular and R-circular polarizations of the stress vector: two linearly independent ways the 2D stress vector can rotate as the wave passes. When the cylinder lattice is later coarse-grained to recover Maxwell (chapter 6), these two modes play the role of the two photon polarizations.

---

## 6. Stability boundary and the degenerate limit χ̃ → 1

Recall the dimensionless shear ratio from chapter 1:

χ̃ = *K_eφ* / √(*K_ee* · *K_φφ*)

The stability requirement *K_eφ*² < *K_ee* · *K_φφ* translates to χ̃ < 1. The closer χ̃ is to 1, the more strongly the off-diagonal coupling competes with the diagonal stiffnesses.

Examining the smaller eigenvalue λ₋ from §4 in the limit χ̃ → 1: in the simplifying special case ρ = *I_φ* and *K_ee* = *K_φφ* ≡ *K* (which we adopt for clarity here; the general algebra reaches the same conclusion), the eigenvalues reduce to:

<!-- λ_± = (K/ρ)(1 ± χ̃) -->
$$
\lambda_{\pm} = \frac{K}{\rho}\,(1 \pm \tilde{\chi})
$$

So the slow-mode speed is *c*₋ = √(*K*(1 − χ̃)/ρ). As χ̃ → 1, *c*₋ → 0.

At exactly χ̃ = 1, the matrix *M* has determinant zero — it is no longer positive-definite — and there is a direction in (*e*, *φ*)-space along which the potential energy is flat, costing nothing to deform. A perturbation along that direction has no restoring force, so it cannot oscillate. It just sits at whatever value it was set to. The slow mode has been "frozen" — it has been replaced by a static zero mode that does not propagate at all.

This is the **degenerate limit**. It marks the upper edge of the parameter range where the cylinder primitive supports two propagating waves. For χ̃ > 1, *M* loses positive-definiteness entirely; its smaller eigenvalue becomes negative, and ω² becomes negative on that branch. The would-be oscillation is exponentially growing instead of bounded — an instability that signals the model has broken down.

The cylinder primitive's natural operating regime is therefore χ̃ ∈ (0, 1) *strictly* — bounded below by 0 (decoupled, no propagation in the off-diagonal channel) and above by 1 (degeneration, slow mode collapses). This confirms theory 3 of [README.md](README.md): stability bounds the shear.

---

## 7. Equipartition and the natural shear χ̃ = 1/√2

Inside the stable range (0, 1), no value of χ̃ is preferred over any other on the basis of stability alone. To find a *natural* value we ask a different question: at what value of χ̃ does each propagating mode carry equal energy in its strain and phase channels?

For a plane-wave solution **u** = **A** exp(*i*(*kx* − ω*t*)), the time-averaged energy density splits into pieces associated with each field:

- A **strain channel** energy combining ⟨*T̃*⟩ and ⟨*Ṽ*⟩ contributions involving *e*.
- A **phase channel** energy combining ⟨*T̃*⟩ and ⟨*Ṽ*⟩ contributions involving *φ*.
- A cross-coupling energy from the *K_eφ* term in *Ṽ*.

The natural definition of equipartition is that the strain-channel and phase-channel energies are equal in time average. Working through the algebra with the mode amplitude (*A_e*, *A_φ*) determined by the eigenvalue problem, this condition reduces to a single equation in the stiffness entries:

*K_eφ*² = (1/2) *K_ee* · *K_φφ*

or equivalently:

<!-- χ̃ = K_eφ / √(K_ee K_φφ) = 1/√2 -->
$$
\tilde{\chi} = \frac{K_{e\varphi}}{\sqrt{K_{ee}\, K_{\varphi\varphi}}} = \frac{1}{\sqrt{2}} \approx 0.707
$$

This is the *geometric mean* point of the stable range — halfway between 0 and 1 in log-scale. At this value the two natural mode speeds are most evenly balanced and energy is equipartitioned between the two channels.

A parallel argument from thermodynamic equilibrium gives the same answer. In a chiral medium where left-circular and right-circular populations carry equal energy on average (which holds in equilibrium when no external mechanism distinguishes the two), the off-diagonal coupling that keeps the populations equipartitioned is precisely *K_eφ* = (1/√2) √(*K_ee* · *K_φφ*). The mechanical and thermodynamic arguments converge on the same value because both express the same balance principle from different vantage points.

A note on what this does and does not establish. The equipartition argument identifies χ̃ = 1/√2 as the *natural* value — the value at which the medium is most "balanced." It does not prove that the cylinder primitive *must* sit there; nothing in chapter 2 alone forces χ̃ to take any particular value within (0, 1). The further question of whether the lattice signal speed *c* (from GRID axiom A1) supplies an additional constraint is taken up in the next chapter.

---

## 8. Bidirectional propagation symmetry

A central question for the cylinder primitive: does the chiral shear, which we have just established splits the two natural modes into different speeds, *also* introduce a preference for one direction of propagation over the other?

The answer is no, and the proof is direct. The dispersion relation derived in §4 is:

ω²(*k*) = *k*² · λ_±

The right-hand side depends on *k* only through *k*². Therefore for each branch:

<!-- ω²(k) = ω²(−k) -->
$$
\omega^2(k) = \omega^2(-k)
$$

Taking the positive square root gives ω(*k*) = ω(−*k*) up to sign convention. The phase speed |ω/*k*| = *c*_± and the group speed |dω/d*k*| = *c*_± are both independent of the sign of *k*. Waves moving in the +*x* direction (*k* > 0) and waves moving in the −*x* direction (*k* < 0) propagate at exactly the same speed for each mode.

This is a strong claim, and it is worth distinguishing carefully from other directional asymmetries that can arise in waves on chiral media:

- **Mode handedness vs propagation direction.** The chiral shear *does* split the two natural modes into different speeds (*c*₊ ≠ *c*₋). This is the cylinder's analog of *optical activity* in optics — left-circular and right-circular polarized light traveling at slightly different speeds in a chiral solution. Mode handedness is split by chirality. But the choice of mode is a property of the *polarization* — what mix of strain and phase is oscillating — not of which way the wave is going. A given mode (say **v**₊) propagates at *c*₊ regardless of whether it is moving left or right.

- **Direction-dependent media.** Some media really do have direction-dependent propagation. The *Faraday effect*, for example, has a magnetic field along the propagation axis make left-circular light travel faster than right-circular light, with the effect *reversing* if the wave is run backward through the medium. But the Faraday effect requires breaking *time-reversal symmetry* — typically by an external magnetic field — and a passive chiral medium does not do this. A static chirality, like the helical fibers of the cylinder primitive, preserves time-reversal symmetry, and a wave traversing it picks up the same phase shift in either direction.

The cylinder primitive's chirality is of the static, time-reversal-symmetric kind. The shear *K_eφ* is a real symmetric off-diagonal entry in *M* and does not introduce any complex phase or direction-dependent term. Consequently, the dispersion is even in *k* and bidirectional propagation symmetry holds. This confirms theory 5 of [README.md](README.md).

A *negative-result candidate* worth flagging: if the algebra had produced a term linear in *k* in the dispersion (a 2*k* difference between ω(*k*) and ω(−*k*)), the cylinder primitive would have failed this test, and would be incompatible with vacuum Maxwell, where photons of given polarization travel at *c* in either direction. The check passes because *M* is real and symmetric. A complex-valued or non-symmetric *M* would break this — a possibility worth keeping in mind for any later extension that introduces such a term.

---

## 9. Linear superposition and pulse pass-through

The wave equation *D* ∂_t² **u** = *M* ∂_x² **u** is linear: each term is at most linear in **u** and its derivatives. Linearity has a strong consequence — if **u**₁(*x*, *t*) and **u**₂(*x*, *t*) are both solutions, then any linear combination **u**₁ + **u**₂ is also a solution. The proof is one line: substitute **u**₁ + **u**₂ into the equation, distribute the linear operators, and use the fact that each piece satisfies the equation separately.

Physically: two waves moving along the same cylinder do not interfere with each other in any nonlinear sense. They simply add. To see what this means for opposing pulses, construct two plane-wave packets, one launched from the left end and one from the right:

<!-- u_L(x, t) = A_L f(x − c t) -->
<!-- u_R(x, t) = A_R g(x + c t) -->
$$
\mathbf{u}_L(x, t) = \mathbf{A}_L\, f(x - c\, t),
\qquad
\mathbf{u}_R(x, t) = \mathbf{A}_R\, g(x + c\, t)
$$

with *c* the wave speed of the relevant mode (we use a single *c* for clarity; the same applies to any combination of modes), and *f*, *g* arbitrary smooth pulse shapes. Each is a solution of the wave equations of §2. Their sum:

**u**(*x*, *t*) = **u**_L(*x*, *t*) + **u**_R(*x*, *t*)

is also a solution.

As time advances, the right-going pulse with shape *f* moves right at speed *c*, and the left-going pulse with shape *g* moves left at speed *c*. They will meet somewhere in the middle, *overlap* during a transient interval, and then continue past each other.

During the overlap, the field **u** at any point is the sum of the two pulse profiles at that point. There is no scattering of one pulse off the other, no exchange of energy, no distortion of either waveform. After the pulses separate, each one carries its original shape — *f* moving right, *g* moving left — exactly as it would have if the other were absent.

This is the **linear superposition** property. It is essential for the cylinder primitive to be a faithful wave medium: any complicated wave pattern, no matter how it is constructed, can be analyzed as a sum of independently propagating pieces.

The viz model demonstrated this empirically with its Δ2 preset ([viz/grid-lab.md](../../viz/grid-lab.md)): two delta-function pulses launched from opposite ends of a chain pass through each other and emerge with their original shapes intact. The continuous cylinder primitive reproduces this behavior at the level of the underlying wave equation, where it follows from a single property — linearity — rather than from a per-cell update rule.

---

## 10. Summary of givens

The cylinder primitive's wave dynamics, established in this chapter:

- The Lagrangian density *L̃* = *T̃* − *Ṽ* encodes the cylinder's mechanics, with kinetic terms in (∂_t *e*, ∂_t *φ*) weighted by ρ and *I_φ*, and potential terms in (∂_x *e*, ∂_x *φ*) weighted by the stiffness matrix *M*.
- Euler–Lagrange applied to *L̃* produces a coupled pair of linear second-order PDEs: *D* ∂_t² **u** = *M* ∂_x² **u**.
- The plane-wave ansatz reduces the PDEs to a generalized eigenvalue problem ω² *D* **A** = *k*² *M* **A** with two real positive eigenvalues at every *k*.
- The dispersion relation has two branches, ω²(*k*) = *k*² · λ_±, both linear in |*k*|. The medium is non-dispersive — pulses propagate without spreading.
- The two natural modes are mixings of strain and phase governed by the eigenvectors of *D*⁻¹*M*. They are the cylinder primitive's analog of left-circular and right-circular polarizations.
- Stability requires χ̃ ∈ (0, 1) strictly. The upper limit χ̃ = 1 is degenerate: the slow mode's wave speed collapses to zero.
- Equipartition between strain and phase channels selects χ̃ = 1/√2 as the natural value within the stable range. The same value emerges from a thermodynamic equilibrium argument.
- The dispersion is even in *k*, so left-going and right-going waves propagate at identical speeds. Chirality splits *mode* speeds (optical activity) but not *direction* speeds (no Faraday effect). The cylinder is direction-symmetric.
- The wave equations are linear, so any two solutions can be superposed. Two opposing pulses pass through each other and emerge with original waveforms intact.

These properties are what a viable primitive substrate must have to support Maxwell-style wave physics. The next chapter takes up the question of whether the lattice signal speed *c* — the cadence at which the GRID lattice transmits information — pins the cylinder's parameters more tightly, or leaves a one-parameter family in play.
