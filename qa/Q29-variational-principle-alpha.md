# Q29: Variational principle for α

**Status:** Open — partially addressed by R11; richer functional needed  
**Source:** User question  
**Related:** [Q18](Q18-deriving-alpha.md), [Q30](Q30-prime-q-harmonic-avoidance.md), [R11](../studies/R11-prime-resonance/), [R13](../studies/R13-kk-charge-t3/)

**Question:** Can α be determined by minimizing a total energy functional E(δ) over
the shear parameter, the same way atoms find their ground states by minimizing energy?

---

physics is determined by extremizing something: particles follow
geodesics (least action), light takes the fastest path (Fermat),
fields extremize the Lagrangian.  Can α be determined the same
way — by minimizing a total energy functional E(δ) over the
shear parameter?

The electron model already has a family of valid geometries
(all odd q from ~100 to ~287, each with shear δ = L_θ/(2q)).
Each distributes the photon's field differently on the torus.
The total energy includes terms we can compute:
- **Coulomb self-energy** — depends on how uniformly charge
  covers the torus surface (varies with q)
- **Magnetic field energy** — same dependence
- **Multipole structure** — more uniform coverage (higher q)
  means lower multipole moments, potentially lower energy
- **Shear stiffness** — if deforming the material sheet from rectangular
  to sheared costs energy, this penalizes large δ (low q)

If E_total(q) has a minimum at a specific q, the electron's
ground state selects that q — and hence α = δ/R.  This is the
same logic by which atoms have ground states: nature finds the
lowest-energy configuration consistent with the constraints.

In string theory this is exactly how compact-dimension shapes
are fixed: the "moduli" (shape parameters) settle to the
minimum of an effective potential.  Our shear is a modulus of
the material sheet, and E(δ) is its effective potential.

This approach is complementary to the EM self-consistency
approach (Q18): the wave equation gives the allowed modes, and
the variational principle selects which mode nature occupies.

**"Least-expensive path" framing:** A photon with fixed
energy, velocity, and Compton frequency is trapped in a
periodic geometry.  It must return to its starting point
in phase — constructive self-interference is required for
a stable resonance.  The "cheapest" path is the one that
minimizes phase mismatch per circuit, maximizes field
uniformity (lowest multipole moments), and concentrates
all energy in the fundamental Compton mode.  Solving for
this on the sheared material sheet should yield the shear that selects
q.  The primality constraint (Q30) acts as a filter: only
prime q avoids sub-harmonic leakage.
*Source: user question*
*Status: partly addressed by R11 (Coulomb cost favors low q,
no minimum at 137).  R12 found that the flat-material-sheet wave equation
provides no constraint on shear; the variational approach
requires a richer energy functional.  The KK self-energy
(sum over the mode tower on M₄ × flat material sheet) is the natural
candidate for such a functional.  → R13 (backlog)*
