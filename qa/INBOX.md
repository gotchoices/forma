# Q&A Inbox

Raw capture queue. Add questions here as they arise, tagged with source.

**Workflow:**
- Add questions here as they come up.
- Quick answers: answer inline, mark `answered`.
- Needs real work or substantial write-up: create `Q<N>-slug.md` in this folder,
  add to [`README.md`](README.md) index, and trim entry here to a pointer.
- Needs computation: create a study entry in [`studies/STATUS.md`](../studies/STATUS.md),
  mark `→ R<N>`.

---

## Open

Q2. **Flat space inside, curved appearance outside.** If photons
travel a straight line inside the compact space, would they
manifest fields in xyz as though their flat space is toroidal?
Is the toroidal shape something we impose, or a consequence of
how flat compact dimensions embed in 3+1D?
*Source: user question*
*Status: R5 retired — subsumed by R13 (KK field projection on flat T³)*

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
size-dependent. Standard KK result. Needs write-up.*

Q6. **Orthogonality and transforms.** Is there a transform that
connects xyz to the compactified dimension? Does the new
dimension need to be orthogonal to xyz to avoid requiring a
confinement mechanism?
*Source: user question*
*Status: largely answered by [Q07](Q07-flat-compact-dimensions.md) (KK metric). Residual detail
folded into R1/R13 (R5 retired).*

Q8. **B-field and magnetic dipole.** Does the B-field always point
toward the poles? Is the magnetic moment an integral or average
over all positions? What did WvM say about getting a single N/S
dipole from the toroidal orbit?
*Source: user question*
*Status: R4 retired — answered within D1/R2; magnetic moment is axial projection of B on T²*

Q9. **Guided-wave decay profile.** What is the actual E-field
falloff from the orbit? How does a guided-wave mode (vs uniform
sphere) affect the charge derivation?
*Source: toroid-geometry F5*
*Status: → R6 (concluded)*

Q10. **Quadrupole correction.** The (1,2) orbit has ~2.5%
anisotropy at the rotation horizon. Does a full calculation shift
q/e by a few percent?
*Source: toroid-geometry F5*
*Status: → R7 (concluded); backlog for full calculation*

Q11. **Why only q = 1 and q = 2?** Is there a physical selection
rule eliminating torus knots with q ≥ 3?
*Source: knot-zoo F1*
*Status: answerable — spin-statistics theorem requires integer or
half-integer spin. q ≥ 3 gives non-standard spins, ruled out.
Needs write-up.*

Q12. **Multi-photon states and color charge.** Could three confined
photons with correlated phases each contribute 1/3 of the charge?
*Source: knot-zoo F3*
*Status: open — folded into R14*

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
*Status: → R1 (concluded — KK gravitational charge ruled out;
algebraic mapping of WvM → KK not yet checked)*

Q19. **Precession causes.** If the torus axis precesses, what
drives it? Is it a natural consequence of the equations of motion?
*Source: toroid-geometry F5*
*Status: open — backlog (R9 number retired; study TBD)*

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
self-interference, which implicitly assumes phase matching.
Needs write-up.*

Q23. **Precessing orbit and volume-filling.** Does a precessing
(1,2) orbit reproduce WvM's volume-filling energy flow pattern?
*Source: user question*
*Status: open — backlog (R10 number retired; study TBD)*

Q24. **String theory parallels.** A string is a 1D vibrating
object on compact geometry; our photon is a 1D wave on a closed
geodesic. How deep is the analogy? Is our T² model a special
case of string compactification?
*Source: user question*
*Status: open (backlog)*

Q25. **Digital periodicity.** A number on a counter that rolls
over (modular arithmetic) is the simplest compact dimension.
A sinusoid on this counter is a standing wave. Is a "particle"
just a resonance in a periodic register? Does this connect to
simulation-theory ideas?
*Source: user question*
*Status: open (backlog — see also [Q31](Q31-discrete-torus-digital-counter.md))*

---

## Filed (promoted to individual files)

Questions with substantial content have been written up in this folder.
See [`README.md`](README.md) for the full index.

### Answered / Closed

| # | File | Note |
|---|------|------|
| Q1, Q7 | [Q07-flat-compact-dimensions.md](Q07-flat-compact-dimensions.md) | Compact dimensions can be flat; orthogonality is metric-based |
| Q13 | [Q13-three-compact-dimensions.md](Q13-three-compact-dimensions.md) | Three compact dims required for topological linking (R14 Track 0) |
| Q30 | [Q30-prime-q-harmonic-avoidance.md](Q30-prime-q-harmonic-avoidance.md) | Negative result — primality does not select q (R11) |
| Q33 | [Q33-gravity-vs-charge.md](Q33-gravity-vs-charge.md) | Both can arise from photons; different coupling channels |

### Open

| # | File | Status |
|---|------|--------|
| Q18 | [Q18-deriving-alpha.md](Q18-deriving-alpha.md) | Active front |
| Q26 | [Q26-hadrons-photon-knots.md](Q26-hadrons-photon-knots.md) | Open → R14 |
| Q27 | [Q27-foundational-axioms.md](Q27-foundational-axioms.md) | Framing |
| Q28 | [Q28-photon-absorption.md](Q28-photon-absorption.md) | Open |
| Q29 | [Q29-variational-principle-alpha.md](Q29-variational-principle-alpha.md) | Partially addressed → R13 |
| Q31 | [Q31-discrete-torus-digital-counter.md](Q31-discrete-torus-digital-counter.md) | Conceptual |
| Q32 | [Q32-energy-geometry-fundamentals.md](Q32-energy-geometry-fundamentals.md) | Framing → R13, R14 |
