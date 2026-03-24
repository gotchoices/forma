# R29. Atoms and nuclei — from T⁶ modes to multi-body physics

**Questions:** Q28 (photon absorption / energy levels), Q16
**Type:** theoretical + compute  **Depends on:** R27, R15
**Status:** Not started


## Motivation

R27 showed that the T⁶ compact space accounts for the
single-particle spectrum: electron, proton, neutron, and
muon are exact eigenmodes; kaons, eta, and phi are
parameter-free predictions within 1.5%.

But nature is not a collection of isolated particles.
Atoms exist.  Nuclei are stable.  Electrons occupy energy
levels.  None of these phenomena can be addressed by a
model that finds one mode at a time.

The jump from "particles" to "atoms" is the hardest
conceptual leap in the entire program.  This study
confronts the open questions head-on.


## The central problem: T⁶ is not enough

A single T⁶ mode is a standing wave in 6 compact
dimensions.  It has a definite energy, charge, and spin —
it *is* a particle.  But:

- Two particles solved in the same T⁶ simultaneously are
  effectively one particle.  They share the same compact
  geometry.  There is no notion of "two objects at different
  places."

- An atom requires spatial separation: a proton *here*, an
  electron *there*, 0.5 Å apart.  That separation lives in
  the three extended spatial dimensions (R³), which T⁶ alone
  does not model.

- The binding energy (13.6 eV for hydrogen) is the energy
  cost of the particular spatial configuration.  It arises
  from the *interaction* between two T⁶ modes as a function
  of their R³ separation.

**Conclusion:** To model atoms, we need at minimum a
9-dimensional framework: the 6 compact dimensions (T⁶) plus
the 3 extended spatial dimensions (R³).


## Dimensional hierarchy

| Dimensions | What lives there | Current status |
|------------|-----------------|----------------|
| T⁶ (compact, 6D) | Particle identities: mass, charge, spin | R27: well-modeled, zero free parameters |
| R³ (spatial, 3D) | Spatial positions, separation, binding | Not yet modeled |
| R¹ (time, 1D) | Dynamics: decays, orbits, transitions | Not yet modeled |
| **T⁶ × R³** (9D) | Static multi-body configurations | Minimum for atoms |
| **T⁶ × R³ × R¹** (10D) | Full dynamics | Needed for decays, spectral transitions |

The full spacetime is 10-dimensional: T⁶ × R³⁺¹.  Our
current tools (lib/t6.py, lib/t6_solver.py) operate in the
T⁶ subspace only.  This study must extend into R³ and
eventually into R³⁺¹.


## What a 9D solver would do

A "9D solver" takes as input:
- Two (or more) T⁶ mode specifications (e.g. proton + electron)
- A trial 3D separation vector **r**

And computes:
- The total energy of the configuration as a function of **r**
- Stability: is there a minimum in E(**r**)?
- If so, the binding energy ΔE = E(∞) − E(r_min)

**For hydrogen:** Input a proton mode (0,0,0,0,1,2) and an
electron mode (1,2,0,0,0,0) separated by distance r in R³.
Find the r that minimizes total energy.  Check whether
ΔE ≈ 13.6 eV.

**For a nucleus:** Input a proton mode and a neutron mode.
Find the separation where they are bound.  The binding
energy (~2.2 MeV for deuterium) tests whether the T⁶
geometry produces nuclear forces.

**For energy levels:** Input a hydrogen ground state and
perturb.  The discrete allowed perturbations should reproduce
atomic spectral lines (Lyman, Balmer series).


## Open questions

These are the conceptual problems that must be resolved
before computation is possible.  Each is a potential track
or sub-study.

### OQ1. How do T⁶ modes interact in R³?

Two modes in the same T⁶ are one wave function.  Two modes
at different R³ positions are two wave functions that
interact through their fields.

What is the interaction energy?  In Kaluza-Klein theory, the
4D electromagnetic field emerges from the 5th-dimension
geometry.  In our model, charge arises from the shear
mechanism (R19).  The Coulomb interaction between two charged
modes must emerge from the T⁶ geometry — this connects
directly to R15 (the α problem).

**Status:** R15 has the formula α(r,s) but no way to select
r.  Solving hydrogen might *be* the constraint that selects r:
demand that the interaction gives 13.6 eV at the Bohr radius.

### OQ2. Are there shears between T⁶ and R³?

The T⁶ metric has within-plane and cross-plane shears.
Could there also be shears between compact and extended
dimensions?  In standard Kaluza-Klein theory, such
off-diagonal metric components are the gauge fields — the
electromagnetic potential A_μ is literally the g_{μ5}
component of the higher-dimensional metric.

If shears between T⁶ and R³ exist, they *are* the
electromagnetic (and possibly nuclear) fields.  The 9D
metric would be:

    ┌           ┐
    │ g_3D   A  │
    │  Aᵀ  G_T⁶│
    └           ┘

where A is a 3×6 block encoding the gauge fields and G_T⁶
is the T⁶ metric from R27.  This is exactly the Kaluza-Klein
ansatz generalized to 6 compact dimensions.

**Status:** Not explored.  This may be the key to everything.

### OQ3. When does time enter?

A static 9D solver finds equilibrium configurations —
atoms in their ground state.  But:

- **Decays** are inherently time-dependent: a neutron's mode
  evolves into proton + electron + neutrino modes over ~15
  minutes.
- **Orbits** require time: the electron's wave function has
  a time-dependent phase.
- **Spectral transitions** require time: photon absorption
  changes the electron's mode.

A full treatment needs the 10D wave equation
(T⁶ × R³ × R¹).  The time coordinate may also couple to
the compact dimensions — in particular, if the compact
geometry oscillates in time, that oscillation *is* the
particle's quantum mechanical phase (de Broglie wave).

**Status:** Entirely unexplored.  Probably the last step.

### OQ4. What is a "two-particle state" in T⁶ × R³?

In quantum mechanics, a two-particle state is a wave function
ψ(x₁, x₂) in the tensor product of two single-particle
Hilbert spaces.  What is the T⁶ analog?

Options:
- **Option A — Single wave on T⁶ × R³:**  One wave function
  in 9D, with the "two particles" being two localized peaks
  in the 3D projection.  Each peak has a T⁶ mode profile.
  The interaction is mediated by the 9D wave equation.

- **Option B — Two waves on T⁶, coupled through R³:**  Each
  particle has its own T⁶ mode.  Their coupling is through
  the R³ fields they generate (electromagnetic, gravitational).
  This is closer to the classical Kaluza-Klein picture.

- **Option C — Modified T⁶ at each R³ point:**  The T⁶
  geometry varies across R³.  Near a proton, the compact
  dimensions are deformed in a way that creates a potential
  well for the electron.  The electron "sees" a modified T⁶
  at each point in space.

Each option leads to a different computational strategy.

### OQ5. Does a 9D solver expose electron energy levels?

If we can compute E(r) for the proton-electron system, the
discrete energy levels should emerge from the boundary
conditions — analogous to the particle-in-a-box quantization
but in the radial separation coordinate.

In standard QM, hydrogen energy levels are E_n = −13.6/n² eV.
These come from the Coulomb potential + angular momentum
quantization.  In a 9D picture, the same levels should emerge
from the T⁶ × R³ wave equation, with the Coulomb potential
being a derived quantity (from the T⁶ geometry) rather than
an input.

**The test:** If the 9D model reproduces E_1 = −13.6 eV, the
Balmer series, and fine structure splitting (which involves α),
it would simultaneously solve the α problem (R15) and
validate the entire framework from compact dimensions to
atomic physics.

### OQ6. Nuclear binding without nuclear force

In the T⁶ model, the neutron is a cross-sheet mode
(0, −2, 1, 0, 0, +2) that involves both the electron and
proton T² sheets.  Inside a nucleus, the neutron and proton
modes overlap in the compact dimensions.

Could nuclear binding emerge from the T⁶ geometry without
invoking a separate "strong nuclear force"?  The proton mode
(0,0,0,0,1,2) and neutron mode (0,−2,1,0,0,+2) share the
proton-sheet quantum numbers (n₅, n₆).  Their overlap in the
compact dimensions might create an effective potential in R³.

This is speculative but testable: if the 9D solver shows a
bound state of proton + neutron at ~2.2 MeV (deuterium
binding energy), the strong force is emergent.

### OQ7. Why doesn't the neutron decay in a nucleus?

A free neutron decays in ~15 minutes.  Inside a nucleus, it
is stable.  In the T⁶ picture, this presumably means the
multi-mode configuration inside the nucleus has lower total
energy than the decay products.  The spatial confinement
(nuclear size ~1 fm) must raise the energy of the decay
products above the bound-state energy.

This is a concrete test for the 9D solver: compute the
energy of (proton + neutron at nuclear separation) versus
(proton + proton + electron + neutrino at nuclear separation).
If the former is lower, nuclear stability is explained.


## Computational prerequisites

Before R29 can proceed computationally, we need:

1. **A theory of mode-mode interaction.**  How does one T⁶
   mode create a potential felt by another?  This requires
   solving the α problem (R15) or at least adopting a
   working model for the Coulomb interaction in T⁶ × R³.

2. **A 9D metric ansatz.**  The 9×9 metric of T⁶ × R³ must
   be parameterized.  The T⁶ block is known (from R27).
   The R³ block is flat Euclidean.  The off-diagonal block
   (OQ2) encodes the gauge fields.

3. **A 9D wave equation solver.**  Given the metric, solve
   for the lowest-energy two-mode configurations as a
   function of R³ separation.

4. **Extension of lib/t6.py to 9D.**  The current library
   handles 6D metrics.  It must be generalized to handle
   the 9D case, with the R³ dimensions treated differently
   from the T⁶ dimensions (extended vs compact).

These are substantial extensions.  R29 may begin as a
primarily theoretical study (defining the formalism) before
becoming computational.


## Possible tracks (tentative)

### Track 1 — Formalism: T⁶ × R³ metric and wave equation

Derive the 9D metric, wave equation, and mode-mode
interaction energy from first principles (Kaluza-Klein
decomposition of the T⁶ × R³ manifold).

### Track 2 — The α connection

Use the mode-mode interaction formalism to compute the
effective coupling constant between two charged T⁶ modes.
Check whether it reproduces α ≈ 1/137.  This may resolve
R15 as a byproduct.

### Track 3 — Hydrogen ground state

Compute E(r) for proton + electron in 9D.  Find the minimum.
Compare ΔE to 13.6 eV and r_min to the Bohr radius (0.53 Å).

### Track 4 — Hydrogen energy levels

Solve for the discrete energy spectrum.  Compare to
E_n = −13.6/n² eV.  Check fine structure (α² corrections).

### Track 5 — Deuterium binding

Compute E(r) for proton + neutron.  Find the minimum.
Compare ΔE to 2.224 MeV and r_min to nuclear size (~2 fm).

### Track 6 — Nuclear stability

Test whether the neutron is stable inside the deuteron:
compare total energy of (p + n bound) vs (p + p + e + ν).


## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R27   | Single-mode particle spectrum; parameter pinning |
| R28   | Spectrum refinement; feeds better mode assignments |
| R15   | The α problem — likely solved as a byproduct of OQ1 |
| R19   | Shear-charge mechanism — the source of EM interaction |
| R26   | T⁶ framework, metric infrastructure |
| R20   | Harmonic proton — early multi-mode ideas |


## What this study could determine

**Best case:** The 9D framework reproduces the Coulomb
interaction from T⁶ geometry, predicts hydrogen's 13.6 eV
binding energy, reproduces spectral lines, explains nuclear
binding at 2.2 MeV, and explains nuclear stability.  This
would unify particle physics, atomic physics, and nuclear
physics from compact-dimension geometry.

**Partial success:** The formalism is sound but computational
limitations restrict us to hydrogen.  The binding energy is
close but α remains approximate.  Nuclear binding requires
nonlinear effects not captured at leading order.

**Null result:** Mode-mode interactions in T⁶ × R³ do not
reproduce the Coulomb potential.  This would indicate that
the charge mechanism (R19) does not extend to inter-particle
forces — the T⁶ model describes particle identities but not
interactions.
