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

Q5. **Size and independence.** → [Q05-orthogonality-and-size.md](Q05-orthogonality-and-size.md) *(answered)*

Q11. **Why only q = 1 and q = 2?** → [Q11-spin-statistics-filter.md](Q11-spin-statistics-filter.md) *(answered)*

Q12. **Multi-photon states and color charge.** Could three confined
photons with correlated phases each contribute 1/3 of the charge?
*Source: knot-zoo F3*
*Status: obsolete — R14 (closed negative) showed linking cannot
redistribute charge; R21 T2 showed curvature gives continuous
ratios, not quantized 1/3.  Quark charge mechanism remains open
(see Q62, Q64, Q66).*

Q14. **Neutrino topology.** q = 0 requires a/R → ∞ (unphysical).
Is the neutrino a fundamentally different topology? A (3,2) knot
has spin ½ and zero charge, but does this identification hold?
*Source: knot-zoo F3, F4*
*Status: partially answered — R20 F14 proved the neutrino
cannot be any KK eigenmode on the electron's T² (lightest
uncharged mode is 245 keV, neutrino < 0.8 eV).  Five
alternative directions analyzed in harmonic-proton/neutrino.md.
Most promising: harmonic beating (Direction B) and condensate
phonon (Direction A).  See Q70 and any future neutrino study.*

Q15. **Generations as harmonics.** m_μ/m_e ≈ 206.8 is not an
integer. Does this rule out the simplest harmonic model?
*Source: knot-zoo F2*
*Status: answered by R20 F17 — muon/tau are "hot electrons"
(same (1,2) fundamental + uncharged sin-like harmonics adding
mass), not simple overtones.  Mass ratios aren't integers
because the harmonic spectrum is thermal/free, not a single
overtone.  R21 F12 further constrains harmonics to sin-like
(odd parity) modes.*

Q16. **What sets the photon energy?** In the compact dimension
model, mass = photon energy / c². What determines which photon
energies are allowed?
*Source: knot-zoo F2*
*Status: open — this is the mass problem*

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

Q22. **Does exact path closure matter?** → [Q22-path-closure.md](Q22-path-closure.md) *(largely answered)*

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

Q50. **Shared compact space.** Is the compact T³ a single space
shared by all particles — each particle a distinct topological
feature of one global manifold — or does each particle carry
its own private subspace? A shared T³ makes entanglement and
interactions geometric; independent subspaces push the mystery
down a level. The dialog notes that all mature frameworks
(AdS/CFT, string theory, LQG) favor a single shared space.
What does the WvM/T³ model imply?
*Source: claude-photon-knots-particle-structure.md*
*Status: open — conceptual/foundational*

Q35. **Entanglement as topological knot-linking in T³.** When two
electrons approach in 3D, their toroidal knots overlap in the
shared compact space. If the knots become topologically linked
(like interlocked rings), that link persists after the particles
separate in 3D — because T³ topology is independent of 3D
distance. Measurement resolves one knot's configuration and
instantly determines the other's. This gives entanglement a
concrete geometric mechanism that standard QM simply postulates.
What topological invariant encodes the link? What severs it?
*Source: claude-photon-knots-particle-structure.md, user question*
*Status: open — needs topological framework*

Q36. **Coulomb force as a subspace proximity effect.** We can
model a point charge (E-field lines radiating from a point in 3D),
but it is less clear why two separated charges exert a force on
each other across empty 3D space. If both charges live as knots
in a shared T³, the force might be a T³ geometric effect rather
than a 3D field effect. Is the Coulomb potential the macro-space
projection of knot-knot interaction energy in T³? How does this
relate to what R13 is computing via KK decomposition?
*Source: user question*
*Status: open — may be addressed by R13 results*

Q37. **Are attraction/repulsion and entanglement the same
phenomenon?** Conjecture: when two knots are in T³ proximity
they interact — this manifests in 3D as the Coulomb force.
When they separate, a residual topological link may persist —
this manifests as entanglement. Same T³ mechanism, different
regimes. If so, the force law and the entanglement statistics
should share a common derivation. Is Coulomb force the
"classical limit" of knot-knot interaction, and entanglement
its topological residue?
*Source: user question*
*Status: open — speculative but testable in principle*

Q38. **Decoherence as topological link dilution.** In the knot
model, decoherence would correspond to the topological link
between two knots being transferred to — and spread across —
environmental knots. The entanglement isn't destroyed, just
dispersed into an ever-larger web of T³ connections. Does this
reproduce the observed decoherence timescales? Does the knot's
internal structure confer any resistance to decoherence (a
natural isolation mechanism)?
*Source: claude-photon-knots-particle-structure.md*
*Status: open — qualitative picture only*

Q39. **Particle/antiparticle annihilation as topological
cancellation.** A positron may be the same (1,2) toroidal knot
wound in the opposite sense. Annihilation = the two
oppositely-wound knots unwinding each other, releasing the
confined photon as free propagation. This reframes annihilation
as topological cancellation rather than matter destruction. Is
this consistent with energy/momentum conservation? Does it
predict anything about the emission angles or polarizations of
the annihilation photons?
*Source: claude-photon-knots-particle-structure.md*
*Status: open — qualitative; testable prediction may exist*

Q40. **Gravity as macro-space curvature sourced by T³ boundary
conditions.** Wheeler's geometrodynamics proposed particles as
spacetime topology — "mass without mass, charge without charge."
In our framework: each particle is a boundary between the
compact T³ and 3D macro-space; macro space curves around that
boundary; that curvature is gravity. This is distinct from Q33
(which asks whether gravity and charge arise from the same
photon — they don't). Here the question is specifically: is
gravity the 3D curvature induced at the T³/3D interface, and
can it be computed from the stress-energy of the confined photon?
*Source: claude-photon-knots-particle-structure.md*
*Status: open — Wheeler's program not yet translated into T³ language*

---
*Wave-language analog of WvM (Q41–Q46)*
*The questions below reformulate the photon-knot model in pure wave/field*
*terms. WvM uses a particle orbiting a torus; the wave analog replaces the*
*particle trajectory with a resonant EM standing wave in a compact cavity.*
*The ~137 sub-paths of R8 become harmonic numbers in the cavity mode spectrum.*

Q41. **Wave-language equivalent of the (1,2) geodesic.** In particle
language the electron is a photon tracing a (1,2) torus knot. In
wave language it should be an EM standing wave on T³ with specific
KK mode numbers — a superposition of Fourier modes whose spatial
pattern has (1,2) winding symmetry. What is the explicit mode
decomposition? Are the particle and wave pictures provably equivalent
descriptions of the same field configuration, or do they differ in
predictions?
*Source: user question*
*Status: open — translation between pictures not yet written down*

Q42. **Compton scale as the beat envelope of compact-space modes.**
The winding number q (a free parameter in the range ~100–200) means the
confined photon completes q major loops per Compton cycle. In wave
language: two adjacent compact-space harmonics (modes n and n+1) produce
a beat pattern — fast oscillation at n×f₀ inside the cavity, slow
modulation envelope at f₀. If the compact circumference L ≈ 2πR, the
beat wavelength is q×L ≈ λ_C. Hypothesis: the Compton-scale behavior
of the electron is the beat envelope of adjacent compact-space harmonics,
not the fundamental mode. Does this picture reproduce the correct energy
and charge for a range of q, or does it constrain q to a specific value?
Note: q ≈ 1/α ≈ 137 is an intriguing coincidence but is not yet
established as the required value — q is currently a free parameter (R8,
R11).
*Source: user question*
*Status: open — quantitative check needed; q is free*

Q43. **What selects the harmonic number q? (Wave-language α problem.)**
A compact-space cavity supports all harmonics in principle. The electron
corresponds to some harmonic n = q, where q is in the range ~100–200.
Lower harmonics would be higher-energy bound states; higher harmonics
lower-energy ones. What physical principle selects one particular q as
the stable ground state? Candidates: energy minimization within a
topological sector, self-consistency of the field (the mode must be its
own source), or boundary conditions imposed by the coupling to 3D.
This is the wave-language restatement of Q18 (what selects q?). Does
framing it as a cavity eigenvalue problem — find the self-consistent mode
— make it more tractable than the particle-path version?
*Source: user question*
*Status: open — wave reframing of the α problem; q is free, ~100–200*

Q44. **Sub-Compton cavity with high-harmonic resonance.** Hypothesis:
a cavity of size ~L_compact (some fraction of λ_C) supports standing
waves. The electron corresponds to harmonic n = q of this cavity, where
q is a free parameter (~100–200). A narrow superposition of modes near
n = q produces an envelope at q×L_compact ≈ λ_C. This gives a concrete
wave model: a small cavity oscillating at high harmonic, with
Compton-scale behavior emerging from the mode envelope rather than from
a large orbit. The cavity size and the harmonic number are related by
L_compact = λ_C/q. Can the electron's charge, spin, and magnetic moment
be derived from the field structure of this mode, independently of q?
Or does the field self-consistency condition fix q — which would be the
wave-language route to deriving α?
*Source: user question*
*Status: open — core wave-language hypothesis; q is free parameter*

Q45. **Charge as field-phase winding number (Chern number).** In
particle language, charge comes from the winding number of the path.
In wave language, the U(1) phase of the complex EM field can also wind
around the compact dimension — this is the first Chern number of the
U(1) bundle, and it is exactly how charge is topologically defined in
gauge theory. Can the WvM charge formula be rederived from the
topological winding of the field phase alone, without invoking a
particle trajectory? If the two definitions (path winding vs. field
phase winding) give the same integer, the wave and particle pictures
are truly equivalent.
*Source: user question*
*Status: open — likely answerable from gauge theory; needs explicit check*

Q46. **Multi-mode resonance and hadron masses: three coupled cavity
modes.** The proton is three photon-knots linked on T³ (R14 Track 0).
In wave language: three coupled resonant modes of the T³ cavity, phase-
locked and topologically entangled (Borromean resonances). The proton
mass = 3×612×m_e emerged geometrically from the particle picture. Can
the same result be derived from the resonance frequencies of three
mutually coupled cavity modes? Does the coupling between modes shift
the resonance frequency in a way that predicts the neutron-proton mass
difference (1.293 MeV)?
*Source: user question*
*Status: obsolete — R14 (closed negative) ruled out the three-photon
linking model.  R20 replaced it with the harmonic proton model
(single fundamental + uncharged harmonics).  The proton mass
prediction is now an R22 question (mode coupling selects spectrum).*

Q47. **Geometric interpretation of the running of α.**
The one-loop QED running is:

    1/α(μ) = 1/α₀ − (2/3π) ln(μ/m_e)

The coefficient 2/(3π) comes from the vacuum polarization
loop and decomposes as (4/3) × 1/(2π), where 4/3 = beta
coefficient (2 spin states, 1/3 from averaging over 3
spatial dimensions) and 1/(2π) from the loop integral.

In the torus model, these factors may have geometric meaning:
- **3** = number of spatial dimensions the field projects into
- **2** = number of polarization states (transverse directions)
- **π** = periodicity of compact dimensions (circular contour)
- **ln(μ/m_e)** = how deeply the probe penetrates toward the
  compact boundary (probe wavelength vs. compact size)

In KK theory, coupling constants change their running above
the compactification scale: from logarithmic (4D) to power-law
(higher-D).  If the compact space is at the Compton scale, the
transition happens at ~0.5 MeV.  All measured α values (atomic
to LEP at 200 GeV) span this transition.

Study could: (1) Write α running in 4+2D or 4+3D KK on T²/T³.
(2) Compare to standard 4D formula. (3) Check if compact dims
modify the β coefficient consistently with experiment. (4) See
if GUT convergence at 1/24 has a geometric interpretation.

Connection to Q34: if α runs because higher-energy probes
penetrate deeper into the compact space (seeing more of the
bare charge), this is the same physics as Q34 Path 3 (membrane
permeability).  The "leakage fraction" IS α, and it runs with
probe energy.

*Source: primer on natural units and alpha, reference dialog,
user brainstorm*
*Status: open — needs both theoretical analysis and comparison
with measured running*

Q48. **Why does E point outward and not B? (Electric vs.
magnetic charge selection.)** WvM hypothesizes that the
circularly polarized photon's E-field is always oriented
normal to the torus surface (outward), producing electric
charge.  But E and B are 90° out of phase in a circularly
polarized wave — they are symmetric partners.  If the
alignment were rotated 90°, B would point outward instead,
and we'd have a universe with magnetic monopoles and no
electric charge.

Questions:
- Is there a geometric reason (from the torus topology,
  the embedding, or the polarization-winding commensurability)
  that forces E outward rather than B?
- Or is it a convention / symmetry breaking — one of two
  degenerate ground states, with the other being the
  antiparticle (or a monopole)?
- If the answer is "nothing forces it," does this predict
  magnetic monopoles as a topologically allowed but perhaps
  energetically disfavored state?

This could be a key geometric constraint.  If the embedding
geometry or the boundary conditions at the compact/3D
interface select E over B, that selection mechanism likely
involves the same geometric factors that determine α.

*Source: user question*
*Status: open — may constrain the geometry; connects to Q34*

Q49. **Natural units reduce to length and energy — analogy
to the geometry+energy premise.** In natural units (ℏ = c = 1),
all physical quantities reduce to powers of two base units:
length (or equivalently time, via c = 1) and energy (or
equivalently mass, via E = mc²).  This is a striking parallel
to the model's foundational premise that particles are built
from only geometry (= length/topology) and energy.

If the parallel is more than coincidence, it suggests that
the model's two ingredients — compact geometry and confined
photon energy — are not just sufficient but *complete*: they
are the only two independent quantities that nature provides.
Every other physical property (charge, spin, mass, magnetic
moment) must be derivable from combinations of these two.

This is not a new question per se but a strengthening of the
axiom base.  See Q32 (energy and geometry as fundamentals)
and Q27 (foundational axioms).

*Source: user question, primers/natural-units-and-alpha.md*
*Status: noted — incorporate into Q27/Q32 when those are
next revised*

Q51. **Non-torus embeddings and the mode-coupling route to α.**
The compact space (flat T²) can be embedded in 3D as shapes
other than a standard torus.  A perfect torus has rotational
symmetry around its central axis, which forces the angular
mode number to be conserved — an n = 2 wave can never produce
the n = 0 component needed for net charge (R15 F3).

But other embeddings of the same flat T² break this symmetry:
- **Elliptical torus** — tube cross-section is an ellipse
- **D-shaped cross-section** — like a tokamak
- **Knotted ring** — the tube tied in a knot (trefoil, etc.)
- **Asymmetric deformation** — any smooth deformation that
  removes the rotational symmetry

On any of these shapes, the angular mode number is NOT
conserved.  The 3D field equations couple n = 2 directly to
n = 0, producing net charge without needing the photon to be
localized as a wavepacket.  The coupling strength depends on
the geometry of the deformation.

If α = (coupling coefficient from n = 2 to n = 0), then α
is determined by the embedding shape.  This could be computed
from the overlap integrals of the deformed geometry.

Questions:
- What is the simplest deformation that gives nonzero coupling?
- Does the coupling coefficient have a nice form?
- Can we recover α ≈ 1/137 from a specific deformation?
- Is the deformation determined by something physical (e.g.,
  the photon's own field backreacting on the embedding)?

**Key lead: the dipole radiation pattern.** A circularly
polarized wave (which is what WvM uses) has a non-isotropic
radiation pattern in 3D: intensity ∝ (1 + cos²θ)/2.  If
the photon's field leaks from the compact space into 3D
with this pattern, and if the field energy shapes the tube
cross-section (self-consistency), then the tube is NOT
circular — it is elongated or D-shaped, determined by
Maxwell's equations.  This chain:

  CP wave → non-isotropic radiation → non-circular tube
  → broken symmetry → n=2 couples to n=0 → charge
  → α = coupling strength = f(deformation)
  → deformation from Maxwell → α derived

would give α from Maxwell's equations and topology alone,
with no free parameters.  The deformation shape is not
arbitrary — it IS the dipole radiation pattern, which is
fundamental.

This may be the most direct path to deriving α: not "what
localizes the photon" but "what shape is the embedding,
given that the photon's own radiation pattern is
non-isotropic."

**Dimensional assignment is not arbitrary (Q52).** The
assignment of which flat-T² dimension becomes the tube (a)
vs. the ring (R) is forced by physics: the WvM charge
mechanism requires p = 1 in the tube (where the surface
normal rotates).  This means L₁ → tube, L₂ → ring, and
the two directions are physically distinct.  If a second
constraint fixes the aspect ratio r = a/R (e.g., equal
distance per winding → r = 1/2, or the radiation pattern
determining the tube shape), the entire geometry is fixed
with zero free parameters.

**Physical mechanism: centrifugal radiation pressure.**
The dipole radiation pattern is one source of tube deformation,
but there is a more fundamental one: the photon has momentum
(p = E/c), and on the curved (1,2) helix, centrifugal force
pushes the field outward from the center of curvature.  The
radiation pressure on the tube wall is stronger at the inner
equator (tighter curvature, R − a from ring center) and weaker
at the outer equator (R + a).  This non-uniform pressure
deforms the tube cross-section even on a perfect torus —
no external asymmetry is needed.

Both effects (centrifugal pressure + dipole radiation pattern)
contribute to the deformation and may reinforce each other.
→ **R17** [`studies/radiation-pressure/`](../studies/radiation-pressure/).

*Source: R15 F7 candidate 5, user question, dipole
radiation pattern observation, centrifugal force analysis*
*Connects to: Q34 Paths 4 and 8, R15, R16, R17, Q48, Q52*
*Status: open — → R17 (radiation pressure self-consistency)*

Q52. **Dimensional assignment constrains the aspect ratio.**
On flat T², the two periodic dimensions L₁ and L₂ are
internally symmetric.  But the embedding and the charge
mechanism break this symmetry: the WvM commensurability
condition (p = 1 → E always outward) requires the single
winding to be in the TUBE direction (where the surface
normal rotates).  This forces:

    L₁ = 2πa (tube, p = 1 winding)
    L₂ = 2πR (ring, q = 2 windings)

The assignment is NOT arbitrary — swapping gives p = 2 in
the tube, which destroys the charge mechanism (R13).

This established asymmetry may constrain the aspect ratio
r = a/R if we add a self-consistency requirement.  For
example:

- **Equal distance per winding:**
  tube: 2πa per 1 winding = 2πa
  ring: 2πR per 2 windings = πR
  Equal → 2πa = πR → r = 1/2

- **Equal transit time per winding:** same argument if v = c
  in both directions.  Gives r = 1/2.

- **Radiation pattern determines tube shape (Q51):** the
  non-isotropic leakage into 3D shapes the tube, fixing r
  through self-consistency with the field equations.

If any of these fix r, the entire geometry is determined:
R and a follow from the path constraint ℓ = λ_C, with zero
free continuous parameters.

Quick check for r = 1/2:
  R = λ_C / (2π√(4 + 1/4)) = λ_C / (2π√(17/4))
    = λ_C / (π√17) ≈ 5.93 × 10⁻¹⁴ m
  a = R/2 ≈ 2.97 × 10⁻¹⁴ m

Quick check results (check_r_half.py):
- R = λ_C/(π√17) ≈ 1.87 × 10⁻¹³ m ≈ 0.485 λ̄_C ≈ 66.5 r_e
- a = R/2 ≈ 9.37 × 10⁻¹⁴ m
- Equal distance per winding confirmed: 2πa/1 = 2πR/2 ✓
- Coulomb energy = α × m_e c² (same as every Compton-scale
  torus — r doesn't change this)
- Classical current-loop μ/μ_B = 2/(4 + r²) = 8/17 ≈ 0.471
  (but classical approach is wrong; g = 2 comes from the
  spin-1 → spin-½ topology, not from the loop area)
- Does NOT connect to α or any measured quantity

Verdict: r = 1/2 is a clean geometric choice (equal arc per
winding, R = λ_C/(π√17), etc.) and eliminates the aspect ratio
as a free parameter, but it does not determine α.  α still
requires deriving σ (R15) or the embedding deformation (Q51).
The value r = 1/2 is plausible as a background constraint.

*Source: user question on dimensional assignment*
*Connects to: R15 F5, Q51, Q34*
*Status: open — r = 1/2 checked; clean but doesn't determine α*

Q53. **Does the model predict the anomalous magnetic moment
(g = 2.002...)?** Our studies (R8 Track 3) established that the
model predicts the LEADING-ORDER g = 2 from topology: the
photon is spin-1 (carries ℏ), the electron is spin-½ (carries
ℏ/2), and the gyromagnetic ratio is their ratio = 2.  This is
geometry-independent — it works for any torus shape, any
winding number, any aspect ratio.

The measured value g ≈ 2.00232 includes the anomalous part
g − 2 ≈ α/π.  WvM claim this comes from the fraction of
field energy in the "non-co-rotating (external) component"
(the part of the EM field that doesn't travel with the
photon).  They write g = 2(1 + α'/(2π)) where α' = (q/e)²α.
With q = e (our current model), α' = α, and this reproduces
the Schwinger first-order correction exactly.

Key questions:
1. **Is the WvM g-factor argument a derivation or a match?**
   WvM's α/(2π) correction predates their model (it's
   Schwinger's 1948 result).  Did WvM derive it from the
   field structure, or fit a "field fraction" to match
   the known answer?
2. **What does our model predict at leading order?**
   - g = 1? No — that's the classical current-loop result
     (R8 F8), known to be wrong.
   - g = 2? Yes — from topology (R8 F9). This is solid.
   - g = 2.002...? Plausible but unverified in our framework.
3. **Should we expect the anomalous correction from geometry?**
   In QED, g − 2 comes from virtual photon loops (radiative
   corrections).  In our model, there are no "virtual photons"
   — but there IS a non-co-rotating external field component.
   If the energy fraction in this component equals α/(2π),
   we'd reproduce the Schwinger result.  But we haven't
   computed this fraction from our geometry.
4. **Does r = a/R affect the anomalous correction?**
   The leading g = 2 is r-independent.  But the correction
   might depend on r (R8 F11 notes this as open).  If our
   model gives a specific r (e.g., r = 1/2 from Q52), does
   the resulting field-fraction calculation reproduce α/(2π)?
5. **Higher-order terms:** QED computes g − 2 to ≈ 12 decimal
   places.  Does the photon-knot model offer any insight into
   the higher-order terms (α²/π², etc.)?

*Source: user question*
*Connects to: R8 Track 3, Q34 (α derivation), Q52 (aspect ratio)*
*Status: open — needs field-fraction calculation for our geometry*

Q57. **Does T³ (vs T²) break the φ-symmetry that protects
zero charge?**  On T², the charge integral of cos(θ+2φ)
vanishes because ∫cos(2φ)dφ = 0.  All mechanisms tested
(Coulomb soliton, centrifugal pressure, geometric deformation)
fail to break this protection.

On T³, three possibilities emerge:

**A. Richer knot topology.**  On T², the (1,2) curve's topology
is fully described by its winding numbers.  On T³, a (1,2,n₃)
curve can have SELF-LINKING — a topological invariant that
depends on the ratios L₁:L₂:L₃ and could provide charge
without wavepacket localization.  This is R15 F8 candidate #4,
never computed.

**B. Non-trivial fiber structure.**  If T³ is NOT a product
S¹ × S¹ × S¹ but has a twisted/fibered structure (the z-fiber
rotates as φ advances), the charge integral doesn't factorize.
Different z-slices see different effective φ-geometry, and the
cancellation that kills the T² charge may not occur.  A
Hopf-like fibration would couple z to φ intrinsically.

**C. R14 already requires T³.**  T³ is needed for topological
linking (quarks/confinement, R14 Track 0).  If T³ also provides
the charge mechanism — and the SAME fiber structure that enables
linking also breaks φ-symmetry — the model gains unity: quarks,
confinement, AND α from one geometric structure.

The critical sub-question: is the physical T³ a flat product
(in which case the z-integral factors out and gives zero, same
as T²) or a twisted/fibered space (in which case the charge
mechanism is fundamentally different)?

*Source: user question*
*Connects to: R14 (T³ for quarks), R15 F8 #4 (topology),
Q51 (mode coupling route to α), Q13 (three compact dims)*
*Status: open — promising new direction; no computation yet*

Q54. **Is the dipole radiation pattern route to α effectively
ruled out?**  R15 F8 Candidate 6 proposed: the circularly
polarized photon's radiation pattern (power ∝ (1 + cos²Θ)/2)
deforms the tube cross-section, breaking the θ-symmetry and
enabling mode coupling to the charge-carrying (1,0) mode.

R18 tested a closely related mechanism (cos(2φ) deformation
of the major radius) and found it fails: the Coulomb cost of
the charge exceeds the photon energy saving by 96×.

For the dipole radiation pattern specifically:
- The radiation pattern rotates WITH the photon along the
  (1,2) geodesic, so the deformation depends on (θ+2φ), the
  same combination as the mode itself.
- Products like cos(θ+2φ) × f(θ+2φ) × cos θ still integrate
  to zero over the full torus because the φ-integral kills
  any n ≠ 0 harmonic.
- Time-averaged field energy density on the symmetric torus
  is φ-UNIFORM (the oscillating part averages away), so the
  time-averaged tube deformation is also uniform — no
  symmetry breaking.

The mechanism likely falls to the same φ-symmetry protection
that kills R18.  But a direct computation of the NEAR-FIELD
radiation pattern (not the far-field dipole approximation)
on the curved torus surface has NOT been done.  The near-field
pattern could have contributions at harmonics other than
(θ+2φ), which might evade the protection.

Status: likely ruled out by the same φ-symmetry protection
(R18 F7), but not yet directly computed.  Low priority.

*Source: user question, R18 Track 2 analysis*
*Connects to: R15 F8 #6, R18 F7, Q51*
*Status: open — likely negative but uncomputed*

Q55. **Confinement without compact dimensions: is a self-
sustaining EM soliton possible in flat 3+1D spacetime?**
The WvM/photon-knot model confines a photon on a compact
manifold (T² or T³).  But what if the photon is not on a
compact space at all — just a self-sustaining standing wave
held together by some nonlinear mechanism?

Precedents for self-sustaining EM structures:
- **Wheeler's geons** (1955): self-gravitating EM wave packets.
  Unstable — gravitational self-energy is ~10⁻⁴³ too weak.
- **Kerr-Newman solutions**: charged rotating black holes whose
  gyromagnetic ratio matches the electron's (g = 2).  But mass
  ~Planck mass, not m_e.
- **Nonlinear QED (Euler-Heisenberg)**: at extreme field
  strengths (E ~ E_Schwinger), photon-photon scattering
  becomes significant.  Could photon self-interaction at
  Compton-scale field strengths confine a wave packet?
- **Ranada's knotted EM fields** (1989): topologically
  nontrivial solutions to Maxwell's equations in flat space.
  They are NOT stable equilibria — they disperse.

The standard result: in LINEAR Maxwell theory, there are no
stable localized solutions (no solitons).  All wave packets
disperse.  Confinement requires either nonlinearity (which
Maxwell doesn't have classically) or topology (compact space
provides reflecting boundary conditions).

The compact-dimension model's strength is that confinement is
TOPOLOGICAL — the photon can't escape a closed manifold.
Without this, no known mechanism confines a single photon in
flat space.  The strong force analogy is interesting: QCD's
confinement is also topological (flux tubes, not point forces).

*Source: user question*
*Connects to: Q27 (foundational axioms), Q32 (geometry + energy),
R14 (T³ for hadrons)*
*Status: open — foundational; answers "why compact dimensions?"*

Q56. **Natural-units analysis of the photon-knot model.**
In natural units (ℏ = c = 1), all physical quantities reduce
to powers of length and energy (or equivalently mass).  In the
photon-knot model, these correspond to:
- **Length** = compact geometry (R, a, σ)
- **Energy** = confined photon (m_ec²)

The model's dimensionless parameters:
- r = a/R (aspect ratio) — still free, plausibly 1/2 from Q52
- σ (wavepacket width in radians) — the unknow that determines α
- α = exp(−4σ²) — the fine-structure constant

In natural units:
- R ≈ 0.485/m_e (about half the reduced Compton wavelength)
- a ≈ 0.243/m_e (for r = 1/2)
- e²/(4π) = α ≈ 1/137 (the coupling constant)
- All torus dimensions are O(1/m_e) — the Compton scale

The energy budget (in units of m_e):
- Total: m_ec² = 1 (the photon)
- Kinetic localization: ~exp(−4σ²) ≈ α (from σ ≈ 1.1)
- Coulomb self-energy: α × 1 = α (from R7)
- Magnetic moment: g ≈ 2(1 + α/(2π))

Observation: every deviation from the "natural" value appears
with coefficient α.  The kinetic localization cost is α × m_ec².
The Coulomb energy is α × m_ec².  The g−2 correction is α/(2π).
This suggests α is the single parameter controlling ALL
perturbative effects in the model.

Does this pattern constrain σ?  If σ is determined by minimizing
the total energy including all O(α) corrections, the equilibrium
might fix α self-consistently.  This would be a variational
approach to the α problem (see Q29).

*Source: user question*
*Connects to: Q49 (natural units parallel), Q29 (variational α),
R15 F5 (α = exp(−4σ²))*
*Status: open — variational approach not yet attempted*

Q58. **Shear of the compact T² breaks φ-symmetry and produces
charge for the delocalized wave.**  On the unsheared T², the
(1,2) mode has q_eff = 2 (integer).  The charge integral
∫cos(2φ)dφ = 0 — the φ-protection that has blocked every
mechanism tested.

On a SHEARED T² (lattice vectors non-orthogonal, shear
displacement δ), the (1,2) mode has q_eff = 2 − δ/L₁ in the
embedding coordinates.  For δ ≠ 0 and δ ≠ nL₁, q_eff is NOT
an integer, and the charge integral becomes:

    Q ∝ sin(δ/a) / (2 − δ/(2πa))

which is NONZERO.

Key properties:
- **No wavepacket localization needed.**  The wave can be fully
  delocalized (σ = ∞) and still carry charge.  The symmetry
  breaking is geometric, not quantum-state.
- **R12 F5 showed the shear is internally unconstrained.**
  The flat-T² wave equation gives no constraint on δ — exactly
  the condition where an external constraint (T³ structure,
  embedding, topology) could determine it.
- **R12 F14 established the two-domain picture:** mass/spin are
  internal (shear-independent), charge is external (depends on
  how the compact fields project via the embedding).  Shear
  changes the projection → changes the charge.
- **Connects to T³ (Q57):** on T³, the shear between the three
  directions is part of the moduli space.  The T³ geometry
  needed for quark confinement (R14) constrains these shears.
  The same constraint could fix the shear that determines α.

The question "what determines σ?" becomes "what determines δ?"
— but δ is a GEOMETRIC parameter (compact-space metric), not a
quantum-state parameter.  → R19.

*Source: user question, R12 F5/F14, R15 F8 analysis*
*Connects to: R12 (shear unconstrained), R15 F8 (what determines
σ), Q57 (T³), R14 (T³ for quarks), Q52 (aspect ratio)*
*Status: → R19*

Q59. **Oval tube cross-section and elliptical ring — do they
constrain σ?**  In the discussion following R18's negative
result, two geometric deformations were proposed:

(a) **Oval tube** (cross-section becomes elliptical rather
than circular).  This changes the θ-mode structure but NOT
the φ-integration.  For the (1,2) mode cos(θ+2φ), the charge
integral still separates as ∫cos(2φ)dφ × (θ-integral).  The
φ-integral is zero regardless of tube shape.  → Does not help.

(b) **Elliptical ring** (major radius varies: R(φ) = R₀ +
δcos(2φ)).  This is exactly R18's cos(2φ) deformation.  The
amplitude modulation from the varying curvature might seem to
break φ-symmetry, but for a traveling wave, |ψ|² = 1 uniformly
around the ring.  The energy density is constant in φ regardless
of ring shape.  → φ-symmetry protection holds.

Both fall to the same obstruction: the (1,2) traveling wave
maintains uniform probability density around the ring.  Any
geometric deformation that preserves T² topology (without shear)
cannot break the integer-q condition that makes the charge
integral vanish.

*Source: user questions*
*Connects to: R18 (geometric deformation), Q58 (shear), R15 F8*
*Status: closed — both ruled out*

Q60. **3D geodesics on sheared T³: what is the charge formula?**
R19 Tracks 1–5 used the 2D charge formula for (1,m) modes
confined to a plane of T³.  But on T³, a photon can wind in
all three compact dimensions: (n₁, n₂, n₃) with all nᵢ ≠ 0.

*Source: R19 Track 4/5 discussion*
*Connects to: R19, R14, Q13 (three compact dimensions)*
*Status: answered by R19 Track 6 (F31) — the 3D charge
integral gives a selection rule: s₁₃ = 0 kills charge for
n₃ ≠ 0 modes.  No charged particle lighter than the electron
exists on T³.  Fractional charges from 3D geodesics are
ruled out.  See also Q63 (electron planarity).*

Q61. **Does the n=1 tube-winding constraint hold in 3D?**
On T², the WvM charge mechanism requires n = 1 (one tube
winding) for nonzero monopole moment (R19 F17, S3 F3).

*Source: R19 Track 4/5 analysis*
*Connects to: R19 F17, S3 F3*
*Status: answered by R19 Track 6 — the n₁ = 1 constraint
holds in 3D.  The 3D charge integral factorizes, and the
tube-winding selection rule (n₁ = 1 only for nonzero charge)
carries over from 2D to 3D.  R21 Track 2 (F6) extends this
further on the curved torus: only even-parity (cos-like)
n₁ = 1 modes carry charge.*

Q62. **Independent quark T² (Model B from S3): revisit with shear?**
S3 F4 proposed "Model B" — separate compact dimensions for
leptons and quarks.  The quark's own T² would have a/R = 9.91
(for Q = 2e/3) or 19.81 (for Q = e/3).  This was based on the
WvM charge formula without shear.  With shear, the quark T²
could have different dimensions and its own shear value,
decoupled from the electron.  This sacrifices multi-particle
consistency (no shared T³) but avoids the mass constraint
problem that killed Tracks 4–5.

Trade-off: fewer constraints (no T³ linking) but also fewer
predictions (independent geometries are less falsifiable).

*Source: S3 F4 Model B, R19 Track 4/5 failure*
*Connects to: S3, R19, R14*
*Status: open — possible fallback if T³ approaches fail*

Q63. **Why is the electron confined to a 2D plane on T³?**
R14 F2 assumed the electron uses 2 of 3 compact dimensions
with the third "inert."  This was never derived.

*Source: R19 Track 4/5 discussion*
*Connects to: R14 F2, R19, Q13*
*Status: answered by R19 F31 — the 3D charge integral on
sheared T³ gives a selection rule: s₁₃ = 0 (no shear in
the third dimension) kills charge for any mode with n₃ ≠ 0.
The electron must have n₃ = 0, confining it to a 2D plane.
Additionally, (1, 2, 0) has shorter geodesic length than
(1, 2, k) for k ≠ 0, making it the lowest-energy charged
spin-½ state.  Both energetic and charge-based arguments
agree: the electron is planar on T³.*

Q64. **Does topological linking modify the charge formula?**
R14 proposed that Borromean linking of three photons on T³
fractionalizes their charges.  This is a topological effect,
distinct from the kinematic shear formula Q ∝ sin(2πs)/(m−s).
If linking modifies the effective q_eff (e.g., by shifting the
winding number by a fractional amount), it could produce 1/3
and 2/3 charges even when the single-photon formula gives
integer charge.  The mathematical framework for computing
charge of linked geodesics has not been developed.

*Source: R14, R19 Track 4/5 discussion*
*Connects to: R14 F2, R19 F24*
*Status: open — possible Track 7 of R19 or new study*

Q65. **Quark photon energies: are they equal?**
R14 F3 assumed equal energy per quark photon (each at harmonic
n = 612, giving m_p = 3 × 612 × m_e to 0.008%).  But the
actual current quark masses are very different (m_u ≈ 2 MeV,
m_d ≈ 5 MeV), with 99% of the proton mass from gluon field
energy in QCD.  In the WvM framework (no gluons), the photon
energies ARE the mass — but they needn't be equal.  Unequal
quark photon energies would change the mass constraints on
the T³ geometry.  The 3 × 612 coincidence could be a guide
rather than a hard constraint.

*Source: R14 F3, R19 Track 4/5 analysis*
*Connects to: R14 F3, R19 F19*
*Status: open*

Q66. **Shear sets the charge scale (α); linking sets the
fractions (1/3, 2/3)?**  A hybrid model where:
- Shear determines the OVERALL coupling strength α = 1/137
  (derived from single-photon electron on T²/T³)
- Linking fractionalization determines the RELATIVE charges
  (quarks get 1/3, 2/3 of the electron charge)
- These are independent mechanisms operating simultaneously
This preserves the R19 electron result and the R14 quark
picture, with each addressing a different aspect.

*Source: R19 Track 5 conclusion*
*Connects to: R19, R14*
*Status: open — the most conservative next hypothesis*

Q67. **What fixes the aspect ratio r?**  The central free
parameter.  α(r, s) = 1/137 fixes s at each r, but nothing
pins r.  Potential second constraints: (a) energy extremality
or stability; (b) matching a second observable (muon mass
ratio, proton-electron mass ratio); (c) Q52's r = 1/2 from
equal arc per winding; (d) neutrino mass-squared splittings
(three near-degenerate mode triplet constraining r — see
neutrino study if created).  R21 Track 5 showed muon charge
does NOT constrain r (parity selection rule instead).
*Source: R21 Track 5 conclusion, project-wide assessment*
*Connects to: Q52, R19, R21*
*Status: open — highest priority free-parameter problem*

Q68. **Write up the electron model (paper).**  The model has
a complete electron: mass from T² periodicity, charge from
shear (R19), spin ½ from (1,2) winding, g = 2 from topology
(R8), α from one equation in (r, s).  A paper would consolidate
S1–R21 results, force confrontation with what's rigorous vs.
hand-waving, and establish priority.  Could frame as "single
photon on sheared T² reproduces electron properties" with the
free parameter r acknowledged.
*Source: project assessment after R21*
*Status: open — consolidation task*

Q69. **DIS and scattering predictions from the harmonic proton.**
R20's proton has internal structure (fundamental + uncharged
harmonics).  R21 Track 5 constrains harmonics to be sin-like.
What does deep inelastic scattering look like in this model?
Can we compute form factors or structure functions?  This tests
the model against hard experimental data without requiring
quarks.  The sin-like harmonics have specific spatial profiles
on the curved torus — these determine the scattering response.
*Source: project assessment after R21*
*Connects to: R20, R21, Q26*
*Status: open — could constrain the harmonic spectrum*

Q70. **Neutrino from beating harmonics.**  In beta decay,
three nearly-degenerate harmonics could form a beat pattern
that escapes the proton as a quasi-particle.  The beat
envelope has effective mass ~ ΔE (the splitting), naturally
sub-eV.  Three pairwise beats → three neutrino flavors.
The mass-squared splitting ratio Δm²₃₁/Δm²₂₁ ≈ 33.6 is
a dimensionless observable that could pin down r.
See neutrino.md Directions A (phonon) and B (beats).
*Source: user insight + R20 F16 (sub-eV mode splittings)*
*Connects to: R20 F14–F21, neutrino.md, Q14*
*Status: open — promising; could become R23*

Q34. **The charge mechanism problem: how does the electron have
charge?** R13 Track 3 showed that the multi-winding (68, 137)
model breaks WvM's charge mechanism.  WvM's charge requires
p = 1 (one tube winding per wavelength = commensurability
between polarization rotation and frame rotation, so E always
points outward).  R8's multi-winding model has p = 68, destroying
this.  The root cause is α ≈ 1/137: at the Compton scale
(where p = 1 works), U_Coulomb = α × m_e c² — a factor of
~137 too small (R7).  Shrinking the torus to fix the Coulomb
energy forces multi-winding, which breaks charge.

Eight candidate paths to resolve the tension:

**Path 1. Compact-space refractive index.** If c_sub < c in
the compact space, a photon at Compton frequency has shorter
wavelength, fitting into a smaller torus with p = 1.  Need
c_sub/c ≈ α.  Waveguides routinely have effective speeds < c.
Could c_sub be determined by the geometry?

**Path 2. Compact metric scale factor.** Equivalent to Path 1
in KK language: a conformal factor in the compact metric that
plays the role of α.

**Path 3. Membrane permeability.** If only a fraction of the
photon's field leaks into 3D, the apparent charge is reduced.
If the leakage fraction ≈ α, this explains U_Coulomb = α × m_e c²
at Compton scale.  The torus stays at Compton scale with p = 1,
preserving charge.  Charge = √α × e_bare.  Connects to running
of α (higher energy probes penetrate deeper into compact space).

**Path 4. Geometric projection factor.** The solid angle
subtended by the torus tube, or the ratio of compact to 3D
surface area at the embedding, could provide a geometric
suppression ≈ α.  Calculable from embedding geometry.

**Path 5. Harmonic decomposition of the confined photon.**
→ **R16** [`studies/harmonic-charge/`](../studies/harmonic-charge/).
The embedding curvature redistributes the (1,2) plane wave's
energy across Fourier modes; only the p = 1 component produces
charge; if that fraction = α, we have a derivation.
Complementary to R15 (numerical); R16 seeks the analytical
explanation.  "Two photons beating" version ruled out by
energy conservation — see R16 README for details.

**Path 6. Topological charge (winding number IS charge).**
Decouple charge from the commensurability argument entirely.
The winding number is a topological invariant that IS the
charge, with the coupling strength to 3D fields determined by
some geometric factor = α.  Needs a mathematical framework
beyond WvM.

**Path 7. Keep (1, 2) at Compton scale; reinterpret Coulomb
energy.** → **R15** [`studies/forward-charge/`](../studies/forward-charge/).
Run R7's calculation forward: energy + topology → charge → α.
See R15 README for full analysis of how R7 → R8 → R13 led
back here.

**Path 8. Different compact topology.** The torus is WvM's
choice but not the only option.  Lens spaces, spheres, or more
exotic manifolds could have different charge mechanisms and
mode structures.

*Source: R13 Track 3 conclusion, user brainstorm*
*Related: Q42, Q44 (wave-language versions of Path 5), Q47
(geometric interpretation of α running — connects to Path 3)*
*Status: open — Path 7 → R15, Path 5 → R16, Paths 4+5 → R17
(radiation pressure / centrifugal deformation).  Remaining
paths (1–3, 6, 8) await triage.*

Q71. **How does R³ perceive periodic, compactified dimensions?**
The T⁶ model says "space is just shaped that way" — compact
dimensions exist as geometric fact.  Based on relativity, the
photon "thinks" it travels a straight path; from R³, we see
periodicity.  What IS our perception of that periodicity?

In KK theory, the answer is known: R³ perceives T⁶ as particles
(modes = quantized masses) and forces (gauge fields from off-
diagonal metric terms).  But this raises the deeper question:
is this the ONLY way to perceive compact dimensions, or are
there phenomena that reveal the compact geometry more directly?

The Bohr radius (53,000 fm) and the electron tube (32,000 fm)
are within a factor of 1.7 (R31 F11).  The compact geometry is
NOT deeply hidden — it's just barely smaller than atomic scales.
Could precision atomic measurements (Lamb shift, g−2, proton
charge radius) reveal the compact geometry?  R31 Track 4 showed
the naive KK Yukawa is ruled out by 10⁵, but that rules out the
naive COUPLING, not the geometry itself.

*Source: user question (R31 discussion)*
*Connects to: R29 (KK reduction), R31 F11, F15–F18, Q36*
*Status: open — foundational; partially addressed by R29/R31*

Q72. **Is R³ itself periodic?  Is our universe toroidal to an
outside observer?**  If R³ is a very large T³, the distinction
between "space" and "internal structure" is one of scale, not
kind.  Consequences:

- Photons have a maximum wavelength (set by the cosmic T³ circumference)
- The universe has finite volume
- From a larger space, our universe is a set of modes — "particles"
- The hierarchy continues: T⁶ modes are particles to us;
  our R³ modes might be particles to an outer space

Cosmological bounds: the CMB constrains the T³ circumference to
be > the observable universe (~10⁴¹ fm) if the topology is
detectable.  But if R³ is a large T³, and T⁶ is a small T⁶,
the only difference is scale.  The scale hierarchy:

| Space | Circumference | Perceived as |
|-------|---------------|-------------|
| Proton T² | 3–24 fm | Hadrons, nuclei |
| Electron T² | 5,000–32,000 fm | Electron, charge |
| Neutrino T² | 10¹⁰–10¹¹ fm | Neutrino masses |
| R³ (if T³) | ~10⁴¹ fm? | Our universe |

*Source: user question (R31 discussion)*
*Connects to: Q7, Q50, R30 (minimal geometry)*
*Status: open — speculative but concrete; testable via CMB topology*

Q73. **Is there shear between R³ and T⁶?**  The electromagnetic
potential A_μ IS the off-diagonal metric component between R³
and the compact dimensions (standard KK result, used in R29
Track 1).  So the answer is YES — electromagnetism IS the R³-T⁶
shear.  The Coulomb force doesn't come from within T⁶ or R³;
it comes from their cross-term.

Open questions beyond this established result:
- Are there ADDITIONAL R³-T⁶ cross-terms beyond the gauge field?
- Do magnetic effects (velocity-dependent: F = qv×B) have a
  different geometric origin than electric effects?
- If the R³-T⁶ shear is electromagnetism, and within-plane
  shear determines α, is there a unified principle governing
  ALL shears (within-plane, cross-plane, R³-T⁶)?

*Source: user question (R31 discussion)*
*Connects to: R29 Track 1 (KK Coulomb), R19 (shear-charge formula),
R31 F7 (mechanisms for selecting α)*
*Status: partially answered — EM as R³-T⁶ shear is established;
additional cross-terms and unification are open*

Q74. **Cross-sheet perception: is there an analog between how
the electron sheet "sees" the proton sheet and how we (in R³)
see the neutrino sheet?**

The electron sheet perceives the proton sheet through σ_ep
(cross-shear ≈ −0.09).  This coupling produces the neutron
(a mode spanning both sheets) and affects particle masses.
The electron sheet doesn't know the proton sheet's geometry
directly — only the coupling.

Similarly, R³ perceives T⁶ through gauge fields (cross-terms
in the metric).  And we perceive the neutrino sheet through
neutrino masses and weak interactions.  The neutrino sheet is
10⁷× larger than the electron sheet — effectively decoupled
(R28 F1: σ_eν, σ_νp irrelevant).

The pattern: each "level" perceives others through couplings,
not geometry.  Geometry is invisible; only its consequences
(forces, masses, mode energies) are accessible.  This might
explain why the compact dimensions are not directly observable
— the same way the electron sheet cannot "observe" the proton
sheet's aspect ratio, only its coupling effects.

*Source: user question (R31 discussion)*
*Connects to: R28 F1 (neutrino decouples), R31 Q&A (r_e
sensitivity analysis), Q50 (shared compact space)*
*Status: open — conceptual; could inform how to interpret
the model's free parameters*

Q75. **Is α = 1/137 a contingent fact ("design choice") or
necessary ("the only way")?**

The T⁶ model currently treats α as contingent — any shear s
produces a valid geometry (R31 F4–F6).  But the model only has
kinematics (spectra), not dynamics (what holds the geometry in
shape).

The question maps to: does the moduli potential (distortion
energy + Casimir energy + any other contributions) have a
UNIQUE minimum?

- If YES: α is necessary — the geometry relaxes to one shape
- If NO (flat direction): α is contingent — a "choice" or
  initial condition, possibly varying across a multiverse

From standard physics: no derivation of α exists after 100+
years.  String landscape (~10⁵⁰⁰ vacua) suggests contingency.
Anthropic arguments note α must be NEAR 1/137 for chemistry
but don't explain the exact value.

In our model, the concrete next step is computing the moduli
potential: the energy cost of maintaining the shear on the
torus.  This requires a gravitational or elastic energy
functional not yet in the model (R31 F7, F23).

*Source: user question (R31 discussion)*
*Connects to: R31 F4–F7 (Casimir doesn't select α), F23
(dynamics needed), Q18 (deriving α), Q29 (variational α),
Q34 Path 7 (forward charge)*
*Status: open — the deepest open question in the model*

---

## Filed (promoted to individual files)

Questions with substantial content have been written up in this folder.
See [`README.md`](README.md) for the full index.

### Answered / Closed

| # | File | Note |
|---|------|------|
| Q1, Q7 | [Q07-flat-compact-dimensions.md](Q07-flat-compact-dimensions.md) | Compact dimensions can be flat; orthogonality is metric-based |
| Q2 | *(inline)* | Answered: two-domain picture (R12 F14, R13). Flat inside, toroidal embedding in 3D. |
| Q3/Q4 | *(inline)* | Answered: compact space is 2D (T²) or 3D (T³ for linking, Q13/R14). Radial profile is transverse mode structure. |
| Q5 | [Q05-orthogonality-and-size.md](Q05-orthogonality-and-size.md) | Orthogonality is metric, not size-dependent; standard KK result |
| Q6 | *(inline)* | Answered by [Q07](Q07-flat-compact-dimensions.md): KK metric provides the transform; orthogonality is metric-based. |
| Q8 | *(inline)* | Answered: B always axial (R2, R8 F10). Magnetic moment = net axial projection of B on T². |
| Q9 | *(inline)* | Concluded via R6. Field profile shape doesn't change q = e; actual profile needs wave eq. on T². |
| Q10 | *(inline)* | Concluded via R7. Quadrupole correction ~few %; backlog until charge mechanism settled. |
| Q11 | [Q11-spin-statistics-filter.md](Q11-spin-statistics-filter.md) | Spin-statistics theorem excludes free particles with q ≥ 3 |
| Q13 | [Q13-three-compact-dimensions.md](Q13-three-compact-dimensions.md) | Three compact dims required for topological linking (R14 Track 0) |
| Q17 | *(inline)* | Concluded via R1. KK gravitational charge ~10⁻²² × e — ruled out. WvM mechanism is different. |
| Q22 | [Q22-path-closure.md](Q22-path-closure.md) | Exact closure not needed; properties depend on topology, not global periodicity |
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
