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
1. **KK charge from flat T² (R13, backlog):**
   R12 showed the charge calculation must be done entirely from
   the flat-T² perspective (KK decomposition), not by mixing
   flat-T² path lengths with 3D-embedded Coulomb energies.
   Set up 6D field equations on M₄ × flat T², compute the 4D
   effective charge and self-energy from KK modes, and check
   whether requiring self-energy = m_e c²/2 constrains the
   shear without using e as input.

Closed leads (R11):
- *Variational / energy cost:* Coulomb energy favors low q
  (monotonic, no minimum at 137).  See Q29.
- *Prime q / harmonic avoidance:* five linear tests found no
  prime/composite distinction.  See Q30.

Key insights:
- **The shear MUST exist** (independent of its value).  On
  an unsheared T², the geodesic slope IS the spin ratio.  You
  cannot simultaneously have exact spin-½ AND dense torus
  coverage.  The shear decouples these — its existence is
  forced, only its magnitude is undetermined.
- **q ~ 1/α is partly tautological.**  The model uses the
  measured charge e as input.  Since α = e²/(4πε₀ℏc), the
  charge constraint forces R ~ r_e and the mass constraint
  forces q ~ 1/α.  The value ~137 is a restatement of the
  input, not a prediction.  The real free parameter is
  **r (the aspect ratio)**, not q.
- Breaking the circularity requires deriving the shear from
  field self-consistency WITHOUT using e as input.

On the running of α: α runs in QED (1/137 → ~1/128 at Z-mass),
but q must be an odd integer (discrete), so the geometric α
can't vary continuously.  The running likely reflects vacuum
polarization screening in 3+1D, not compact geometry changes.
The bare α is fixed; the dressed α runs.
*Source: toroid-geometry F6, R7, R8 Tracks 4–5, R1 (gravity
too weak), R11 (tautology analysis)*
R12 results (COMPLETE):
- Track 1: flat-T² wave equation has no modes at ω_C (spectral
  gap of ~137×).  Shear unconstrained.
- Track 2: curved-torus geodesics give q ≈ 193 (not 137);
  holonomy is zero.  Confirms compact space must be
  intrinsically flat.
- Key insight: R8's charge calculation mixes flat-T² (mass/spin)
  with 3D-embedded (Coulomb) physics — inconsistent.  The correct
  approach is KK decomposition from the flat T².

*Status: → R13 (KK charge from flat T², backlog)*

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
*Status: open (backlog — string theory parallels study)*

Q25. **Digital periodicity.** A number on a counter that rolls
over (modular arithmetic) is the simplest compact dimension.
A sinusoid on this counter is a standing wave. Is a "particle"
just a resonance in a periodic register? Does this connect to
simulation-theory ideas?
*Source: user question*
*Status: open (backlog — string theory parallels study)*

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
**Shared geometry hypothesis (Q32, R14):** If all particles
share one T², fractional charges must arise from topological
linking of multiple photons on the same geometry — not from
different a/R values.  This is far more constraining and
would fix the free parameter r.  See R14 (draft).
*Source: user question, knot-zoo F3*
*Status: → R14 (draft, not yet active)*

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

**Refined framing (from Q32 analysis):** The axioms may reduce
to just two fundamental ingredients: **energy** and **geometry**
(including topology).  All particle properties — mass, charge,
spin, magnetic moment — are emergent.  See Q32.
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

**"Least-expensive path" framing:** A photon with fixed
energy, velocity, and Compton frequency is trapped in a
periodic geometry.  It must return to its starting point
in phase — constructive self-interference is required for
a stable resonance.  The "cheapest" path is the one that
minimizes phase mismatch per circuit, maximizes field
uniformity (lowest multipole moments), and concentrates
all energy in the fundamental Compton mode.  Solving for
this on the sheared T² should yield the shear that selects
q.  The primality constraint (Q30) acts as a filter: only
prime q avoids sub-harmonic leakage.
*Source: user question*
*Status: partly addressed by R11 (Coulomb cost favors low q,
no minimum at 137).  R12 found that the flat-T² wave equation
provides no constraint on shear; the variational approach
requires a richer energy functional.  The KK self-energy
(sum over the mode tower on M₄ × flat T²) is the natural
candidate for such a functional.  → R13 (backlog)*

Q30. **Prime q and harmonic avoidance.**  137 is prime.  Is
that functional — not coincidental?

On the torus, the photon completes q major orbits per Compton
cycle.  Each orbit is a sub-cycle whose rotating E-field
contributes to the total field.  If q is composite
(e.g. q = 136 = 2³ × 17), then every divisor d of q creates
a sub-period: after q/d orbits the field pattern has partial
closure, a sub-harmonic mode that can siphon energy from the
fundamental (full Compton-cycle) resonance.

| q   | Factorization | # divisors | Sub-resonances |
|-----|---------------|------------|----------------|
| 131 | prime         | 2          | 0              |
| 135 | 3³ × 5       | 8          | 6              |
| 136 | 2³ × 17      | 8          | 6              |
| 137 | prime         | 2          | 0              |
| 139 | prime         | 2          | 0              |
| 140 | 2² × 5 × 7   | 12         | 10             |

For prime q, the only divisors are {1, q}.  No intermediate
sub-harmonics exist — all field energy is forced into the
fundamental mode.

This is a standard engineering principle: prime numbers are
used in turbine blade counts, gear ratios, and antenna
arrays specifically to prevent resonant coupling between
sub-systems.

**Three-part selection of q:**
1. Coulomb self-energy → q in range ~100–287
2. Primality → no energy leakage to sub-harmonics
3. Energy minimization (Q29) → selects which prime

**Proposed computation:** overlay q phase-shifted copies of
the wave — one per major orbit, each shifted by 2π/q.
For prime q, the superposition should destructively
interfere everywhere except at the fundamental period
(the full Compton cycle).  For composite q, constructive
interference at sub-harmonic periods should be visible —
representing energy leakage channels.  This is a direct,
computable discriminant.

Note: primality also guarantees gcd(p, q) = 1 for ANY
choice of minor winding p — the single-path topology is
automatic and maximally robust.  For composite q, only
specific p values avoid splitting into multiple loops.
*Source: user question*
*Status: CLOSED (R11 — negative).  Eight tracks found no
prime/composite distinction in any linear analysis.  q enters
the flat-T² spectrum as a continuous parameter, not through
its factorization.  The hypothesis remains viable only in the
nonlinear/curved-torus regime.*

Q31. **Discrete T² and digital counter hypothesis.**  What if
the compact space is not continuous but has a finite number of
discrete states — a digital counter?

**Core idea:** Represent T² as a single integer counter with
N total states that wraps (modular arithmetic).  Assign the
low-order bits to the minor circumference (a-dimension) and
the high-order bits to the major circumference (R-dimension).
This naturally produces:

- **Wrapping:** the counter is periodic by definition.
- **Shear:** upper bits only increment when lower bits roll
  over (like an odometer).  The carry propagation IS the
  shear — the seam offset arises from hierarchical counting,
  not from an imposed boundary condition.
- **Full coverage:** every state in the counter is visited
  exactly once per full cycle, so the entire T² domain is
  scanned.
- **Two periodicities:** the lower bits cycle at a higher
  frequency (minor circumference) while the upper bits cycle
  at a lower frequency (major circumference), consistent with
  the (p, q) winding structure.

**The 128 question:** If the counter uses binary, the natural
modulus is a power of 2.  128 = 2^7 is suggestive because the
measured 1/α(M_Z) = 127.951 ± 0.009 — within 0.04% of 2^7.
In QED, vacuum polarization screens the bare charge, making
the effective coupling weaker (1/α larger) at low energy.  If
α_bare = 1/128, the dressed α at zero energy could be ~1/137
via standard running.

**Preliminary calculation (one-loop perturbative QED):**

Using the known fermion spectrum (e, μ, τ, u, d, s, c, b)
with one-loop vacuum polarization:

| Scale         | 1/α (perturbative) |
|---------------|---------------------|
| 0 (measured)  | 137.036             |
| ℏc/r_e        | 134.8               |
| m_c           | 132.5               |
| m_b           | 130.9               |
| 10 GeV        | 129.7               |
| 33 GeV        | 128.0               |
| M_Z (91 GeV)  | 126.6               |

The perturbative calc overshoots the measured running by
~1.4 units (gives 126.6 at M_Z vs. measured 127.95) because
light-quark contributions require non-perturbative QCD
treatment (dispersion relations with e+e- → hadrons data).
After correcting for this, 1/α = 128 likely falls near
M_Z or slightly below.

**Assessment:**
- 1/α(M_Z) = 127.951 is close to 128 but ~5σ below it.
  Tantalizing, not conclusive.  Scheme-dependent (MS-bar
  vs. on-shell) at the ~0.1 level.
- The direction of running is correct: bare α larger
  (1/α smaller), dressed α smaller (1/α larger).
- The digital counter elegantly explains the shear as carry
  propagation rather than an externally imposed boundary
  condition.
- The deeper question — why would spacetime be discrete at
  the torus scale (~10⁻¹⁵ m), far above the Planck scale
  (~10⁻³⁵ m) — is unanswered.
- If taken seriously, the bit allocation between minor and
  major dimensions would fix the winding ratio, providing a
  fundamentally different mechanism for selecting q.

**Relation to other questions:**
- Q18 (derive α): if α_bare = 1/128, the "derivation" becomes
  explaining why the counter is 2^7 states, plus standard QED
  running.
- Q30 (prime q): 137 is prime, but 128 = 2^7 is maximally
  non-prime.  If the bare q is 128, the primality of 137 is
  accidental (an artifact of the running correction).

*Source: user hypothesis*
*Status: open — conceptual.  The numerical coincidence
1/α(M_Z) ≈ 128 is real.  A formal study would require:
(1) precise calculation of QED running from α_bare = 1/128
using dispersion-relation hadronic data, checking if α(0)
matches 137.036 exactly; (2) a theoretical framework for
why spacetime has discrete states at this scale.*

Q32. **Energy and geometry as the only fundamentals.**  In
the WvM framework, charge is not a fundamental substance —
it is an EM field configuration that masquerades as charge
when viewed from 3+1D.  Mass is not fundamental either —
it is photon momentum confined in a periodic orbit.  If
both are emergent, then only two things are truly
fundamental: **energy** and **geometry** (topology of space).

**The emergent hierarchy:**

| Property  | Emergent from                         |
|-----------|---------------------------------------|
| Mass      | Energy confined in periodic geometry  |
| Charge    | Field winding number on compact T²    |
| Spin      | Winding ratio of geodesic (p:q)       |
| Mag. mom. | Geometric projection of compact field |
| g-factor  | Energy partition (co- vs non-rotating)|

**Conservation laws are also emergent:**
- *Mass conservation* = energy conservation (fundamental)
- *Charge conservation* = winding number conservation
  (topological: you can't smoothly unwrap a path on T²)
- *Spin conservation* = topology of the geodesic
  (can't change the knot type by smooth deformation)

These emergent conservation laws are exact — not
approximate — because topology is exact.  But their
*reason* is different from the standard picture.  In
standard physics, charge conservation follows from U(1)
gauge symmetry (Noether's theorem).  In the WvM picture,
it follows from the impossibility of changing winding
number without tearing the field configuration.  The
only processes that change winding are topological
transitions: pair creation (winding + anti-winding from
zero) and annihilation (winding + anti-winding → zero).
Both conserve net winding = net charge.

**Implications for the α problem:**  If charge is not an
input but an emergent property of geometry, then using e
in the charge calculation (R8) is circular in a deep
sense.  The correct approach: derive the field pattern
from the geometry alone, compute the apparent charge from
the 3+1D projection, and check whether the geometry is
self-consistent.  This is exactly what R13 (KK charge
from flat T²) attempts.  α is not "the coupling strength
between fundamental charges" — it is a geometric ratio
characterizing the compact space.

**Historical context:** This view is in the lineage of
Wheeler's "charge without charge" and "mass without mass"
(geometrodynamics, 1950s–60s), Kaluza-Klein theory
(charge from the 5th dimension), and string theory
(particles from compactification geometry).  The WvM
model adds the specific claim that a single photon on T²
suffices for the electron.
*Source: user insight*
*Status: open — conceptual.  This is a framing principle
rather than a testable calculation, but it sharpens the
direction for R13 and informs Q27 (foundational axioms).*

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
