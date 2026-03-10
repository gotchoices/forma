# Research Questions

Raw capture log. Add questions as they arise, tagged with source.

**Workflow:**
- Add questions here as they come up.
- Quick answers: answer inline, mark `answered`.
- Needs real work: create a `STATUS.md` entry (R*N*), mark `→ R<N>`.
- Full answers (too long for inline): write in `answers/A<N>-<topic>.md`.

---

## Open

Q2. **Flat space inside, curved appearance outside.** If photons
travel a straight line inside the compact space, would they
manifest fields in xyz as though their flat space is toroidal?
Is the toroidal shape something we impose, or a consequence of
how flat compact dimensions embed in 3+1D?
*Source: user question*
*Status: → R5*

Q3/Q4. **Dimensionality of the compact space.** The compact space
is 2D (φ, θ). The radial field profile is transverse mode
structure, not a third compact dimension. Remaining subtlety:
does this hold when the field equations are solved
self-consistently?
*Source: user question, corrected twice*
*Status: largely resolved; residual question folded into R2*

Q5. **Size and independence.** If a compactified space fits inside
the diameter of uncertainty of the resultant particle, can it
still be toroidal and qualify as orthogonal to xyz?
*Source: user question*
*Status: answerable — yes, orthogonality is metric-based, not
size-dependent. Standard KK result.*

Q6. **Orthogonality and transforms.** Is there a transform that
connects xyz to the compactified dimension? Does the new
dimension need to be orthogonal to xyz to avoid requiring a
confinement mechanism?
*Source: user question*
*Status: largely answered by A7 (KK metric). Residual detail
folded into R1/R5.*

Q8. **B-field and magnetic dipole.** Does the B-field always point
toward the poles? Is the magnetic moment an integral or average
over all positions? What did WvM say about getting a single N/S
dipole from the toroidal orbit?
*Source: user question*
*Status: → R4*

Q9. **Guided-wave decay profile.** What is the actual E-field
falloff from the orbit? How does a guided-wave mode (vs uniform
sphere) affect the charge derivation?
*Source: toroid-geometry F5*
*Status: → R6*

Q10. **Quadrupole correction.** The (1,2) orbit has ~2.5%
anisotropy at the rotation horizon. Does a full calculation shift
q/e by a few percent?
*Source: toroid-geometry F5*
*Status: → R7*

Q11. **Why only q = 1 and q = 2?** Is there a physical selection
rule eliminating torus knots with q ≥ 3?
*Source: knot-zoo F1*
*Status: answerable — spin-statistics theorem requires integer or
half-integer spin. q ≥ 3 gives non-standard spins, ruled out.*

Q12. **Multi-photon states and color charge.** Could three confined
photons with correlated phases each contribute 1/3 of the charge?
*Source: knot-zoo F3*
*Status: open — needs investigation*

Q13. **Three compact dimensions.** The three distinct a/R values
for charges (e, 2e/3, e/3) suggest three compact dimensions. Is
this connected to three color charges?
*Source: knot-zoo F4*
*Status: open — speculative, needs framework from R1/R2 first*

Q14. **Neutrino topology.** q = 0 requires a/R → ∞ (unphysical).
Is the neutrino a fundamentally different topology? A (3,2) knot
has spin ½ and zero charge, but does this identification hold?
*Source: knot-zoo F3, F4*
*Status: open*

Q15. **Generations as harmonics.** m_μ/m_e ≈ 206.8 is not an
integer. Does this rule out the simplest harmonic model?
*Source: knot-zoo F2*
*Status: partially answered — simplest harmonic model is
falsified for leptons. Anharmonic or relativistic corrections
not explored.*

Q16. **What sets the photon energy?** In the compact dimension
model, mass = photon energy / c². What determines which photon
energies are allowed?
*Source: knot-zoo F2*
*Status: open — this is the mass problem*

Q17. **Kaluza-Klein charge quantum.** In standard KK theory,
q = nℏ/(R_KK·c). Does the WvM a/R relationship reduce to this?
*Source: implied by knot-zoo F2, F4*
*Status: → R1*

Q18. **Can α be derived from geometry?** R8 Track 4 found
δ ≈ αR (within ~6%) near q ≈ 137.  Track 5 showed this is
approximate, not exact.  The shear selects q and hence α —
but what selects the shear?

Ruled out mechanisms:
- *EM self-force:* photons don't couple to EM fields.
- *KK gravitational self-consistent metric:* R1 showed
  Gm_e/(Rc²) ~ 10⁻⁴³, which is 41 orders of magnitude too
  weak.  The 6D Einstein equations would return "flat T², no
  shear" to extreme precision.
- *Berry phase:* wrong scaling (R8 Track 4).

Active leads:
1. **EM self-consistency (wave equation on sheared T²):**
   The WvM charge mechanism is purely electromagnetic (no G).
   Solving Maxwell's equations on the sheared T² might show
   that self-consistent EM solutions exist only for specific
   shear values, determining α from boundary conditions alone.
2. **Feasibility function for α:** see Q29.

Key insight: **the shear MUST exist** (independent of its
value).  On an unsheared T², the geodesic slope IS the spin
ratio.  You cannot simultaneously have exact spin-½ AND dense
torus coverage.  The shear is the unique mechanism that
decouples these, so its existence is forced — only its
magnitude is undetermined.

On the running of α: α runs in QED (1/137 → ~1/128 at Z-mass),
but q must be an odd integer (discrete), so the geometric α
can't vary continuously.  The running likely reflects vacuum
polarization screening in 3+1D, not compact geometry changes.
The bare α is fixed; the dressed α runs.
*Source: toroid-geometry F6, R7, R8 Tracks 4–5, R1 (gravity
too weak)*
*Status: EM self-consistency is the concrete next step*

Q19. **Precession causes.** If the torus axis precesses, what
drives it? Is it a natural consequence of the equations of motion?
*Source: toroid-geometry F5*
*Status: → R9*

Q20. **5D geodesic formulation.** Can the (1,2) path be understood
as a geodesic on a 5D manifold? If so, charge, spin, and mass
emerge from the geometry.
*Source: synthesis of knot-zoo F2 and KK theory*
*Status: → R2 (partial)*

Q21. **Orbit constraints and uniqueness.** Can we derive or solve
for orbit shapes that produce E-outward, B-polar, spin ½, and
angular momentum simultaneously? Is (1,2) unique?
*Source: user question*
*Status: open — needs computation*

Q22. **Does exact path closure matter?** All five electron
properties derive from (1,2) topology and local commensurability,
not from global periodicity. A precessing orbit should preserve
them all.
*Source: user question*
*Status: largely answered — analytical argument says exact closure
is not required. The one subtlety is constructive
self-interference, which implicitly assumes phase matching.*

Q23. **Precessing orbit and volume-filling.** Does a precessing
(1,2) orbit reproduce WvM's volume-filling energy flow pattern?
*Source: user question*
*Status: → R10*

Q24. **String theory parallels.** A string is a 1D vibrating
object on compact geometry; our photon is a 1D wave on a closed
geodesic. How deep is the analogy? Is our T² model a special
case of string compactification?
*Source: user question*
*Status: → R12*

Q25. **Digital periodicity.** A number on a counter that rolls
over (modular arithmetic) is the simplest compact dimension.
A sinusoid on this counter is a standing wave. Is a "particle"
just a resonance in a periodic register? Does this connect to
simulation-theory ideas?
*Source: user question*
*Status: → R12*

Q26. **Multi-photon hadrons and knot confinement.** Could
protons and neutrons be multi-photon states on a compact
geometry, rather than bound states of quarks?  The strongest
version of this idea: three photons in a **knotted**
configuration on the compact T² — topologically linked so that
no single photon can be extracted without cutting through
another.  "Quarks" would be features of each photon's
contribution to the combined field; quark confinement would
be automatic because the knot cannot be untied within the
compact topology.  Consider:
- Three photons (matching the three valence quarks)?
- Could each photon's winding topology produce the 1/3 and 2/3
  charge fractions seen in the quark model?
- The proton (charge +e, spin ½, 938 MeV) and neutron (charge 0,
  spin ½, 940 MeV) would need different knotting or mode
  configurations of the same three-photon system.
- Deep inelastic scattering sees three point-like scattering
  centers.  Can a three-photon knot reproduce this?
- S3 found that the WvM charge formula maps specific a/R values
  to fractional charges — potentially reflecting per-photon
  contributions rather than separate particles.
*Source: user question, knot-zoo F3*

Q28. **Photon absorption and excited electrons.** In standard
QM, an orbiting electron absorbs a photon and jumps to a higher
energy level.  In the compact-dimension model, the electron IS
a photon on T².  What does "absorb another photon" mean?
Possible pictures:
- The second photon enters the compact space and adds energy to
  the existing mode — a higher harmonic or larger amplitude on
  the same T².  The compact space now holds more energy, giving
  a heavier/more-energetic electron.
- The compact geometry itself changes (dimensions shift) to
  accommodate the extra energy, analogous to a resonant cavity
  whose shape depends on the stored energy.
- The second photon remains in 3+1D but couples to the electron's
  compact field, creating a composite state.
If excited electrons are simply "more energy loaded into the same
compact space," this should predict a discrete spectrum (only
certain energy increments fit the periodic boundary conditions).
Does this reproduce the hydrogen energy levels?
*Source: user question*

Q27. **Foundational axioms.** The model rests on a minimal set
of assumptions.  Candidates for explicit axioms:
- Certain dimensions exist (at least 3+1 non-compact + 2 compact)
- Some dimensions can be compactified (periodic)
- Fields exist
- Energy in the form of photons (EM field disturbances) can be
  introduced
- Energy propagates according to dimensional constraints
Can all particle properties be derived from these alone?
*Source: user question*

Q29. **Variational principle for α.**  Every other quantity in
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
- **Shear stiffness** — if deforming the T² from rectangular
  to sheared costs energy, this penalizes large δ (low q)

If E_total(q) has a minimum at a specific q, the electron's
ground state selects that q — and hence α = δ/R.  This is the
same logic by which atoms have ground states: nature finds the
lowest-energy configuration consistent with the constraints.

In string theory this is exactly how compact-dimension shapes
are fixed: the "moduli" (shape parameters) settle to the
minimum of an effective potential.  Our shear is a modulus of
the T², and E(δ) is its effective potential.

This approach is complementary to the EM self-consistency
approach (Q18): the wave equation gives the allowed modes, and
the variational principle selects which mode nature occupies.
*Source: user question*
*Status: open — could start by computing E_total(q) across the
existing R8 solution family to see if a minimum exists*

---

## Answered

Q1. **Geometric vs topological compactification.** Would a
compactified dimension manifest as a toroid in 3-space, or is
"toroidal" only topological?
**Answer:** Topological only. "Toroidal" means the coordinates
wrap (S¹ × S¹), not that there is a donut shape in physical space.
→ [A7](answers/A7-flat-compact-dimensions.md)

Q7. **Flat compact dimensions and transforms.** Can an extra
dimension be intrinsically flat yet finite and boundary-free?
**Answer:** Yes. A compact dimension is a periodic coordinate —
flat, no curvature, straight-line geodesics. Translation in the
compact direction gives charge conservation (Noether's theorem).
→ [A7](answers/A7-flat-compact-dimensions.md)
