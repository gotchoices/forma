# Q107. Wave translation of atomic physics: Ma for identity, S for arrangement

**Status:** Open — conceptual framework
**Related:**
  [Q105](Q105-atoms-as-cross-sheet-modes.md) (atoms as modes — tested, partially negative),
  R51 (compound eigenmode tests — negative for bilinear metric),
  R29 (nuclei as Ma modes — confirmed),
  R31 (hydrogen not a Ma eigenvalue — confirmed, correctly),
  [`grid/maxwell.md`](../grid/maxwell.md) (Coulomb derived from lattice),
  [`papers/atoms-from-geometry.md`](../papers/atoms-from-geometry.md) (Paper 3 — two-tier picture)

---

## 1. The reframing

We are not overturning standard atomic physics.  We are
replacing the **particle model** with a **wave model**
and translating every standard physics result into the
language of torus modes (Ma) and lattice dynamics (GRID).

Standard physics describes atoms as "point particles with
properties (mass, charge, spin) interacting through forces
(Coulomb, exchange) in 3D space."

The MaSt/GRID translation: atoms are **torus modes with
properties (from Ma) arranged as standing waves in a
Coulomb potential (from GRID) in 3D space (S).**

The physics is the same.  The ontology is different.
"What is an electron?" changes.  "How does an electron
behave in a hydrogen atom?" does not — because the
Coulomb potential is the same (derived from GRID), the
wave mechanics is the same (Schrödinger equation in that
potential), and the quantum numbers are the same (just
understood differently).


## 2. The translation table

Every concept in standard atomic physics has a Ma/GRID
translation.  The table below maps them:

| Standard physics (3D) | Ma/GRID translation | What determines it |
|----------------------|--------------------|--------------------|
| **The electron** | (1,2) standing wave on Ma_e | Torus topology |
| **Electron mass m_e** | Eigenfrequency of the (1,2) mode | Sheet circumference L₂ |
| **Electron charge −e** | One 2π phase winding through the tube | GRID axiom A3 (phase periodicity) |
| **Electron spin ½** | Odd tube winding (n₁ = 1) | Torus topology (topological spin rule) |
| **The proton** | (1,3) standing wave on Ma_p | Torus topology |
| **Coulomb potential V = −α/r** | Gauge field emerging from GRID lattice phase dynamics | maxwell.md Steps 2-6; not assumed, derived |
| **α = 1/137** | Impedance mismatch between 2D sheet and 3D lattice | GRID axiom A6 (measured, not derived) |
| **Kinetic energy ℏ²/(2mr²)** | Confinement cost: compressing the torus mode's spatial extent in S increases its frequency | Fourier bandwidth limit on the GRID lattice |
| **Bohr radius a₀** | Spatial extent where confinement cost = Coulomb gain | Equilibrium in GRID-derived potential |
| **Ionization energy 13.6 eV** | ½α²m_e — Coulomb binding of the (1,2) mode in the GRID potential | Standard QM in GRID-derived potential |
| **Angular momentum ℓ** | Number of angular nodes in the mode's spatial projection in S | SO(3) symmetry of the 3D embedding |
| **Magnetic quantum number m_ℓ** | Orientation of angular nodes relative to an external axis | SO(3) → SO(2) symmetry breaking by external field |
| **Spin-orbit coupling** | Interaction between the torus topology (spin) and the spatial projection (ℓ) | Relativistic correction: Ma identity meets S arrangement |
| **Shell capacity 2(2ℓ+1)** | Spin degeneracy (2, from Ma topology) × angular degeneracy (2ℓ+1, from SO(3) of S) | Joint Ma × S structure |
| **Pauli exclusion** | Two (1,2) modes can share the same spatial state (orbital) only if their tube windings have opposite orientation (opposite spin) | Fermion topology: the mode requires two circuits to return to its starting value |
| **Screening / shielding** | Inner harmonics form matched mode (electron charge balances nuclear charge at that level); outer electron sees only the unmatched residual | Topological charge cancellation (GRID: winding number conservation) |
| **Chemical bonds** | Two atoms share a spatial region where their electron modes overlap; the combined mode has lower energy than separated modes | Standard Coulomb + exchange, with electrons understood as torus modes |
| **Photon emission/absorption** | The electron mode transitions between spatial arrangements (different ℓ, different n) in the Coulomb potential; the energy difference is emitted/absorbed as a GRID lattice photon | Mode transition in S, photon propagation on GRID |


## 3. What Ma provides vs what S provides

The two-tier structure is not "particles plus space."
It is "wave identity plus wave arrangement":

### Ma determines: WHAT the electron is

- Mass (eigenfrequency of the torus mode)
- Charge (topological winding number — integer, universal)
- Spin (tube winding parity — ½ for odd, 0 or 1 for even)
- Magnetic moment (ring windings — bare moment ∝ n_ring)
- Anomalous moment (defect cost back-reaction — α/(2π))
- Particle identity (which sheet, which mode numbers)
- Charge universality (all electrons have exactly −e
  because they are the same (1,2) mode on the same sheet)

### S determines: HOW the electron arranges itself

- Orbital shape (spherical harmonic pattern in 3D)
- Angular momentum ℓ (spatial nodes — requires 3D
  rotational symmetry, which Ma does not have)
- Binding energy (Coulomb potential from GRID × standard
  wave mechanics)
- Atomic radius (equilibrium of confinement cost vs
  Coulomb gain)
- Shell structure (filling order determined by angular
  momentum states in 3D)
- Molecular geometry (spatial overlap of electron modes
  from different atoms)

### GRID connects them

- Derives the Coulomb potential (V = −α/r from lattice
  gauge field)
- Derives α (the coupling strength — measured, but its
  meaning as impedance mismatch is understood)
- Provides the lattice on which photons propagate
  (emission, absorption, scattering)
- Provides the gravitational field (G from entropy —
  determines large-scale structure)


## 4. Why angular momentum is an S property

R51 Track 1c F21 showed that the flat 2-torus has uniform
degeneracy of 2 — it cannot produce the [2, 6, 10, 14]
subshell capacities that come from the 2ℓ+1 angular
degeneracy in 3D.

This is because angular momentum is a **spatial** quantum
number:

- ℓ counts angular nodes in the standing wave's
  distribution around the nucleus in 3D
- The degeneracy 2ℓ+1 comes from SO(3) — the rotational
  symmetry of 3D space
- A 2-torus has U(1) × U(1) symmetry, not SO(3)
- No choice of torus geometry can produce angular
  degeneracies

The shell capacities are 2 × (2ℓ+1):
- The factor 2 is from Ma (spin degeneracy: two
  orientations of the tube winding)
- The factor 2ℓ+1 is from S (angular degeneracy: how
  many ways the wave can wrap around the nucleus in 3D)

**Shell structure is a JOINT product of Ma and S** — the
spin from torus topology times the angular states from
spatial geometry.  Neither alone produces it.


## 5. What R51 actually showed

R51's negative results are now understood correctly:

**R51 asked:** can the Ma metric ALONE produce atomic
binding?

**Answer:** no.  The bilinear metric E² = n G̃⁻¹ n has no
cross-sheet pathway at the eV scale.

**The correct interpretation:** atomic binding comes from
the GRID-derived Coulomb potential in S, not from Ma
metric cross-terms.  R51 was trying to eliminate S from
atomic physics.  It proved that S is essential — you
cannot get 13.6 eV from the Ma metric alone.

This is not a failure of the framework.  It is a
clarification: Ma provides identity, S provides
arrangement, GRID connects them through the Coulomb
potential.  All three are needed.


## 6. What this means for Q105

Q105 proposed atoms as cross-sheet modes.  R51 tested
this at the bilinear metric level and got a negative
result.  The translation framework says: Q105 was
partially right and partially wrong.

**Right:** electrons in an atom ARE harmonics of the
(1,2) mode on Ma_e.  Adding Z electrons IS incrementing
the mode number to (Z, 2Z).  Charge quantization,
spin, and electron identity come from Ma.

**Wrong (or at least incomplete):** the binding between
electrons and nucleus does NOT come from the Ma metric
cross-terms.  It comes from the Coulomb potential in S.
The spatial arrangement (orbitals, angular momentum,
shell structure) is a 3D property that the torus
geometry alone cannot provide.

**The synthesis:** atoms are Ma-defined particles
(identity from torus modes) bound in S by GRID-derived
forces (Coulomb from lattice gauge field).  The periodic
table is a map of which torus harmonics (Ma) occupy which
angular momentum states (S) at each nuclear charge.

This is the two-tier picture from Paper 3, now stated
more precisely: not "particles plus space" but **"wave
identity from Ma, wave arrangement from S, coupling from
GRID."**


## 7. What changes from standard physics

Almost nothing in the predictions.  The Schrödinger
equation, the hydrogen spectrum, the periodic table, the
chemical bond — all are unchanged.  What changes:

| Question | Standard answer | MaSt/GRID answer |
|----------|----------------|-----------------|
| What is an electron? | Point particle with m_e, −e, spin ½ | (1,2) torus mode on Ma_e |
| Why is charge quantized? | Postulated | Topological (phase winding on GRID lattice) |
| Why is charge universal? | Postulated | All electrons are the same mode on the same sheet |
| Where does V = −α/r come from? | Postulated (Coulomb's law) | Derived from GRID lattice gauge field |
| Where does α come from? | Measured, unexplained | Measured, understood as impedance mismatch |
| What is a photon? | Quantum of the EM field | Propagating disturbance on the GRID lattice |
| What holds the atom together? | Coulomb force | Same — but Coulomb is now derived, not assumed |
| Why ½α²m_e = 13.6 eV? | Schrödinger equation + Coulomb | Same — but both are derived from GRID |
| Where does spin come from? | Intrinsic angular momentum (postulated) | Tube winding parity (topological, derived) |
| What is angular momentum? | Rotation in 3D | Spatial structure of mode projection in S |
| Why 2(2ℓ+1) per shell? | Angular momentum algebra | Spin from Ma (2) × angular states from S (2ℓ+1) |


## 8. Open questions

1. **Can the 2ℓ+1 degeneracy be connected to the torus
   embedding?**  The torus lives IN 3D space.  Its
   embedding has SO(3) symmetry.  The angular momentum
   states of the electron orbital might emerge from how
   the torus mode projects into the 3D embedding, rather
   than from the Schrödinger equation alone.  This would
   deepen the connection between Ma and S without
   eliminating S.

2. **Is the Schrödinger equation derivable from GRID?**
   GRID derives Maxwell's equations.  The Schrödinger
   equation for a charged particle in an EM field is a
   non-relativistic limit of the Dirac equation, which
   follows from the lattice gauge theory.  In principle,
   the entire chain GRID → Maxwell → Dirac → Schrödinger
   → hydrogen spectrum is derivable.  Whether this has
   been done explicitly within the GRID framework is
   open.

3. **Does the Ma mode structure constrain the filling
   order?**  The Aufbau principle (1s, 2s, 2p, 3s, 3p,
   4s, 3d, ...) is derived from the Schrödinger equation
   with screening corrections.  If the torus mode
   spectrum on Ma_e has features that correspond to this
   order, there would be a deeper geometric reason for
   the filling sequence.

4. **Where does exchange interaction come from?**  The
   exchange interaction (which determines spin pairing and
   Hund's rules) is a quantum mechanical effect with no
   classical analogue.  In the torus mode picture, two
   (1,2) modes with opposite spin orientations can share
   a spatial state (Pauli exclusion allows it).  The
   exchange energy depends on the spatial overlap of the
   modes.  Whether this has a clean torus interpretation
   is unknown.
