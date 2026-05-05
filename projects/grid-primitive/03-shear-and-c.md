# Chapter 3 — Shear and *c*

This chapter takes the wave dynamics derived in [02-wave-on-a-primitive.md](02-wave-on-a-primitive.md) and confronts them with the lattice signal speed *c* required by GRID axiom A1. Under the matched-chirality commitment of chapter 1 §8, the cylinder primitive supports a single propagation speed for both polarizations — a single *c*-value to match against the lattice cadence. The question of this chapter is: *what does that match pin down, and what does it leave free?*

This chapter settles open question 1 of [README.md](README.md).

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The constraint: cylinder propagation speed must equal *c* |
| 2 | The bare-speed condition |
| 3 | Matched chirality removes the slow-mode tension |
| 4 | Imposing the constraint algebraically |
| 5 | What pins, what stays free |
| 6 | Summary of givens |

---

## 1. The constraint: cylinder propagation speed must equal *c*

Mechanically, the cylinder primitive is a short transmission line of length *L*. Information injected at one end takes some amount of time *τ* to reach the other end. The lattice has its own opinion about how long that should take: from GRID axiom A1, the lattice signal speed is *c* (one cell per tick, one Planck length per Planck time), so by definition of speed,

*τ* = *L*/*c*

This is just unit conversion — given the lattice cadence and the cylinder's length, the transit time follows.

But the cylinder also has its own internal physics that determines how fast a perturbation actually traverses it. Chapter 2 derived this from the stiffness matrix *M*, the inertia matrix *D*, and the matched-chirality structure they share. Under matched chirality, the cylinder's internal wave equation supports a single propagation speed (no slow-mode split), and that speed must agree with the lattice cadence.

In short: the cylinder must propagate waves at speed *c*, where *c* is what GRID's axiom A1 sets. Forcing the cylinder's internal speed to equal *c* is a real algebraic constraint on the primitive's symbolic constants.

---

## 2. The bare-speed condition

Chapter 2 §4 derived that, under matched chirality, the cylinder's wave equation has a single propagation speed throughout the stable range — *provided* that the two diagonal channels have equal "bare speeds":

*K_ee*/ρ = *K_φφ*/*I_φ* ≡ *c*²

This says: the longitudinal channel's natural speed (the speed it would propagate if uncoupled, set by its own stiffness over its own inertia) equals the azimuthal channel's natural speed (similarly). When this bare-speed condition holds, matched chirality (*K_eφ* / √(*K_ee K_φφ*) = *D_eφ* / √(ρ *I_φ*) = χ̃) gives *M* = *c*² *D*, and both polarizations propagate at *c*.

The bare-speed condition is, like matched chirality itself, a self-consistency requirement of the cylinder primitive. The two channels are coupled by chirality, but their *un*coupled natural speeds must already match for the coupled medium to have a single propagation speed. If they didn't match — if *K_ee*/ρ ≠ *K_φφ*/*I_φ* — the medium would be elastically anisotropic between the two channels, and the matched-chirality reduction *M* = *c*² *D* would fail.

The bare-speed condition is part of "the qualities the cylinder requires." We posit it as an assumption of the model, motivated by the same reasoning as matched chirality: the cylinder's microstructure is one consistent thing, and it produces the same characteristic speed for both channels' diagonal responses.

---

## 3. Matched chirality removes the slow-mode tension

Earlier drafts of this project (and earlier chapters of this document, before chapter 1 §8 was formalized) worked with a *diagonal* inertia matrix *D* = diag(ρ, *I_φ*) and a non-diagonal stiffness matrix *M*. That setup produced two propagating modes at *different* speeds — a fast mode at *c*_+ = √λ_+ and a slow mode at *c*_− = √λ_− — and the slow mode at ≈ 0.414 *c* was incompatible with vacuum Maxwell, where both photon polarizations travel at *c*.

The matched-chirality commitment resolves this at the foundation level. With *D* properly accounting for the medium's chirality (the cross-inertia *D_eφ* matched in magnitude to the cross-stiffness *K_eφ*), and with the bare-speed condition holding, the two modes degenerate at *c*. There is no slow mode.

This is not a fix applied after the fact; it is the design of the cylinder primitive made consistent. The cylinder's microstructure (helical fibers in the wall) produces both elastic-energy chirality and kinetic-energy chirality from the same physical source. Putting one in but not the other was an inconsistency, and the chapter-3 slow-mode tension was the price of that inconsistency. Once both are in (with matched magnitudes — the only physically motivated choice), the tension is gone.

For the rest of this chapter, we work with matched chirality + the bare-speed condition, and identify the propagation speed with *c*.

---

## 4. Imposing the constraint algebraically

With matched chirality + bare-speed in place, the constraint *c*_internal = *c* becomes:

*K_ee*/ρ = *c*²    and    *K_φφ*/*I_φ* = *c*²

These are two equations relating four symbolic constants (*K_ee*, *K_φφ*, ρ, *I_φ*). They pin two ratios:

*K_ee* = *c*² ρ
*K_φφ* = *c*² *I_φ*

The chiral coupling is then determined by the chirality parameter χ̃:

*K_eφ* = χ̃ √(*K_ee* *K_φφ*) = χ̃ *c*² √(ρ *I_φ*)
*D_eφ* = χ̃ √(ρ *I_φ*)

So *K_eφ* = *c*² *D_eφ*, consistent with *M* = *c*² *D*.

To make the structure visible without losing the substance, take the simplifying special case ρ = *I_φ* ≡ ρ₀, *K_ee* = *K_φφ* ≡ *K*. Under this case, the constraints become:

*K* = *c*² ρ₀,    *K_eφ* = χ̃ *K*,    *D_eφ* = χ̃ ρ₀

Three constraints relate four symbolic quantities (*K*, ρ₀, χ̃, *D_eφ*) — but matched chirality means *D_eφ* is already determined by χ̃ and ρ₀, so really we have three independent quantities (*K*, ρ₀, χ̃) and three constraints, with *K*/ρ₀ pinned to *c*².

In the general case (without the simplifying ρ = *I_φ*, *K_ee* = *K_φφ*), the same structural conclusion holds: matched chirality + bare-speed equality gives the dimensionless stiffness ratios pinned in terms of *c* and χ̃. The specific formulas for the general case have more terms but the same shape.

---

## 5. What pins, what stays free

Collecting the parameters and their status:

| Parameter | Status |
|---|---|
| Dimensionless chirality χ̃ = *K_eφ*/√(*K_ee K_φφ*) = *D_eφ*/√(ρ *I_φ*) | **Free** within (0, 1); natural value χ̃ = 1/√2 (chapter 2 §7) |
| Speed-squared ratio *K_ee*/ρ = *K_φφ*/*I_φ* | **Pinned**: equal to *c*² (lattice cadence + bare-speed equality) |
| Cross-inertia *D_eφ* | **Pinned** by matched chirality once χ̃ and ρ, *I_φ* are chosen |
| Cross-stiffness *K_eφ* | **Pinned** by matched chirality once χ̃ and *K_ee*, *K_φφ* are chosen |
| Absolute scale of *K_ee* (and correspondingly ρ, etc.) | **Free** |
| Cylinder length *L* | **Free** |
| Cylinder cross-section radius *r* | **Free** |
| Slow-mode speed *c*_− | **Does not exist** — matched chirality removed it |

What is fixed: the dimensionless ratios that determine wave dynamics. *K_eφ*/*K* and *K*/ρ are both determined by *c* and χ̃ (with χ̃ free within the stable range).

What stays free: an overall stiffness scale (which sets *K* and ρ together while keeping their ratio fixed), the cylinder length *L*, and the cross-section radius *r*. These are not pinned by the lattice cadence alone; they may be constrained by other downstream physics (the entropy account in chapter 4, the Maxwell bridge in chapter 6, the kink-loss derivation of α in chapter 8).

A note on the simplifying assumption ρ = *I_φ*, *K_ee* = *K_φφ*. The qualitative conclusion (some ratios pinned by lattice cadence + matched chirality, an overall scale and geometry free) holds in the general case. The specific simple formulas of §4 are the simplest expression of this structure; the general case has the same shape with more terms.

---

## 6. Summary of givens

The cylinder primitive's parameters, after this chapter:

- Under matched chirality (chapter 1 §8) and the bare-speed condition (*K_ee*/ρ = *K_φφ*/*I_φ* = *c*², introduced in §2 of this chapter), the cylinder's wave equation has a single propagation speed *c* — the lattice signal speed of GRID axiom A1.
- The dimensionless stiffness ratios *K_eφ*/*K* and *K*/ρ are fixed by *c* together with the chirality value χ̃ ∈ (0, 1).
- The chirality value χ̃ is free within (0, 1); its natural value (chapter 2 §7) is 1/√2.
- An overall stiffness scale, the cylinder length *L*, and the cross-section radius *r* remain as free parameters of the primitive.
- There is no slow mode at the single-primitive level — matched chirality + bare-speed gave both polarizations the same speed *c*. The chapter-3 tension that appeared in earlier drafts is resolved.

The next chapter takes up whether the cylinder primitive's stress vector field, assembled into a 2D periodic lattice and excited at finite temperature, supplies the entropy that Jacobson's argument requires for entropic gravity.
