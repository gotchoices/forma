# Research Question Queue

Open questions that arise during studies. Review this queue when
closing a study to decide what to investigate next.

**Workflow:**
- Add questions as they arise, tagged with source.
- When a question becomes a study, mark it `→ study-name/` and move
  to the Promoted section.
- When a question is answered without a full study, note the answer
  briefly and move to Answered.
- Concrete study proposals live in the "Future Study Ideas" section
  of `README.md`. Questions here are the raw material that feeds
  those proposals.

---

## Open Questions

### Tier 1 — Answerable from established physics (no computation)

Q5. **Size and independence.** If a compactified space fits inside
the diameter of uncertainty of the resultant particle (electron), can
it still be toroidal (or some other shape) and still qualify as
orthogonal (independent of xyz)?
*Source: user question*
*Status: answerable — yes, orthogonality is metric-based, not
size-dependent. Standard KK result.*

Q11. **Why only q = 1 and q = 2?** Is there a physical selection rule
that eliminates torus knots with q ≥ 3 (which would give non-standard
spins like 1/3)? Or could exotic particles with fractional spin exist?
*Source: knot-zoo F1*
*Status: answerable — the spin-statistics theorem requires integer
or half-integer spin. q ≥ 3 is ruled out by established physics.*

Q15. **Generations as harmonics.** If generations (e/μ/τ, u/c/t,
d/s/b) are energy harmonics on the same compact path, the mass ratios
should be rational (m_n = n·m_1). m_μ/m_e ≈ 206.8 and m_τ/m_e ≈ 3477
are not integers. Does this rule out the simplest harmonic model? Or
could the quantization be more complex (anharmonic, relativistic
corrections, etc.)?
*Source: knot-zoo F2*
*Status: partially answerable — m_μ/m_e = 206.768, not close to any
integer. Simplest harmonic model is falsified for leptons.*

Q22. **Does exact path closure matter?** The (1,2) geodesic is
exactly closed (rational winding ratio → the path retraces every
cycle). But is exact closure necessary for the electron's properties?
Charge comes from the topology (one twist per wavelength +
double-loop commensurability) — a local property at each point
along the path. Spin ½ comes from the (1,2) winding ratio. Mass
comes from photon energy. Magnetic moment and g-factor come from
circulating current and external field energy. None of these
derivations appear to require the path to close exactly. If so, a
precessing (1,2) orbit would preserve all five properties.
*Source: user question, prompted by analysis of path closure*
*Status: answerable — analytical argument suggests exact closure is
not required. All five properties derive from (1,2) topology and
local commensurability, not from global periodicity. The one
subtlety is WvM's constructive self-interference argument (§2),
which implicitly assumes phase matching at closure — but in the
diffractive limit, small spatial shifts may not degrade interference
significantly. See ref/WvM-summary.md §4.*

### Tier 2 — Answerable with some algebra or paper review

Q3/Q4. **Dimensionality of the compact space.** WvM describes "a
family of nested toroidal surfaces" (§2, Fig. 2) — the EM field
fills a 3D volume. Each individual streamline is a (1,2) geodesic
on its own toroidal surface at fixed tube radius r. Streamlines do
not move radially; the path periodicity comes entirely from the two
angular coordinates φ (wraps) and θ (wraps). The radial direction
is a transverse mode profile — like the radial intensity of a
waveguide mode — not a propagation direction.
*Source: user question, corrected twice — first from 2D to 3D, then
refined: r is a transverse mode coordinate, not a compact dimension*
*Status: largely resolved. The compact space is 2D (φ, θ). The
radial structure is the field's transverse extent. The remaining
subtlety is whether this interpretation holds when the field
equations are solved self-consistently (rather than assumed). See
ref/WvM-summary.md §4.*

Q6. **Orthogonality and transforms.** Is there a way to study the
orthogonality of xyz and extend this to a compactified dimension? Is
there some transform that should be derivable? Does the new dimension
need to be orthogonal to xyz in order to be considered a "dimension"
(i.e., not requiring a confinement mechanism)?
*Source: user question*
*Status: partially answerable from KK metric. The 5D metric
ds² = g_μν dx^μ dx^ν + (dx⁵ + A_μ dx^μ)² builds in orthogonality.
Full treatment requires working through the KK reduction.*

Q2. **Flat space inside, curved appearance outside.** If photons are
traveling a straight line inside the compact space, would they
manifest fields in xyz as though their flat space is toroidal in xyz?
Is the toroidal shape something we impose, or is it a consequence of
how flat compact dimensions embed in 3+1D?
*Source: user question*
*Status: partially answerable. In KK, the compact dimension can be
flat (periodic boundary conditions). The "toroidal orbit" in xyz is
a projection of a straight-line geodesic in higher-dimensional space.*

Q8. **B-field and magnetic dipole.** The E-field from the (1,2) knot
points outward (monopole-like), but does the B-field really point
toward the poles always? Is this a requirement? Will the magnetic
moment of the orbiting photon be the integral of all positions in the
knot, or some kind of average? What did WvM say about how we get a
single N/S dipole from the toroidal orbit?
*Source: user question*
*Status: partially answerable by reviewing WvM paper §4–5, which
derives g ≈ 2 from the circulating energy current.*

Q17. **Kaluza-Klein charge quantum.** In standard KK theory, the
charge quantum is q = nℏ/(R_KK·c). Does our a/R relationship
reduce to this? If so, the three a/R values might correspond to
different KK radii or different winding numbers in the compact
dimension.
*Source: implied by F2, F4*
*Status: answerable with algebra — compare WvM charge formula
against standard KK charge quantization.*

### Tier 3 — Need computation or substantial investigation

Q21. **Orbit constraints and uniqueness.** WvM's (1,2) double-loop
produces E always pointing outward (monopole-like), B always pointing
toward the poles (magnetic dipole), spin ½, and angular momentum.
Can we derive or solve for orbit/knot shapes that satisfy all four
constraints simultaneously? Is the (1,2) path the unique solution,
or are there other topologies that also produce E-outward, B-polar,
spin ½, and net angular momentum? If others exist, do they correspond
to known particles?
*Source: user question, prompted by WvM re-read*
*Status: needs computation — would require parameterizing general
closed paths in a 3D compact space and computing the resulting
time-averaged E and B field multipole moments.*

Q23. **Precessing orbit and volume-filling.** If the (1,2) path
precesses (drifts on the torus surface between cycles due to
self-field perturbation or geometric imperfection), does the
time-averaged field reproduce the volume-filling energy flow pattern
of WvM Fig. 2? Does the time-averaged field of a precessing orbit
match observed electron properties better or worse than the static
closed path? What determines the precession rate?
This is distinct from Q19 (axis precession), which asks about the
whole torus rotating in space to eliminate the quadrupole. Here the
torus orientation is fixed, but the photon's path drifts on the
torus surface.
*Source: user question, prompted by discussion of path closure*
*Status: needs computation — would require simulating a (1,2) orbit
with a small perturbation that breaks exact closure, then computing
the time-averaged E and B field and comparing to the static case.*

Q9. **Guided-wave decay profile.** What is the actual E-field falloff
from the orbit? WvM assume uniform field inside a sphere, but a
guided-wave mode would have a smooth decay. How does this affect the
charge derivation?
*Source: toroid-geometry F5 open question*
*Status: needs electromagnetic computation (guided-wave mode solver)*

Q10. **Quadrupole correction.** The (1,2) orbit has ~2.5% anisotropy
at the rotation horizon. Does a full calculation (including
non-spherical field distribution) shift q/e by a few percent? Is
quantum spin superposition sufficient to eliminate the quadrupole?
*Source: toroid-geometry F5*
*Status: needs computation (multipole expansion of time-averaged
field from the (1,2) orbit)*

Q12. **Multi-photon states and color charge.** Could three confined
photons with correlated phases each contribute 1/3 of the charge,
yielding fractional apparent charge and naturally connecting to three
color charges?
*Source: knot-zoo F3*
*Status: needs investigation — would require modeling multi-photon
interference on a compact dimension*

Q13. **Three compact dimensions.** The three distinct a/R values
(6.60, 9.91, 19.81) for charges (e, 2e/3, e/3) suggest three compact
dimensions. Is this connected to three color charges? What determines
the number and sizes of compact dimensions?
*Source: knot-zoo F4*
*Status: speculative — needs theoretical framework before computation*

Q14. **Neutrino topology.** q = 0 requires a/R → ∞ in the charge
formula, which is unphysical. Is the neutrino a fundamentally
different topology? A (3,2) knot has spin ½ and zero charge (the
right quantum numbers), but does this identification hold under
scrutiny?
*Source: knot-zoo F3, F4*
*Status: needs investigation — the (3,2) knot's zero charge was
shown in the Frenet frame model but the physical meaning of this
zero (vs the neutrino's zero) is unclear*

Q16. **What sets the photon energy?** In the compact dimension model,
mass = photon energy / c². But what determines which photon energies
are allowed? Simple standing-wave quantization (λ = L/n) gives
integer mass ratios. The observed ratios are not integers. What
mechanism selects the actual masses?
*Source: knot-zoo F2*
*Status: needs theoretical work — this is the mass problem*

### Tier 4 — Substantial research programs

Q18. **Can α be derived from geometry?** Study 2 showed a/R = 1/√(πα)
gives q = e. This is algebraically exact but derived by demanding
q = e. Can an independent physical argument (boundary matching,
energy minimization, self-consistent confinement) select this ratio,
thereby deriving α from geometry?
*Source: toroid-geometry F6*
*Status: major open problem — would be a significant physics result
if achievable*

Q19. **Precession causes.** If the torus axis precesses (restoring
spherical symmetry), what drives it? Classically: spin-orbit coupling,
self-interaction, Thomas precession analog? Mathematically: is it a
natural consequence of the equations of motion?
*Source: toroid-geometry F5*
*Status: needs theoretical and possibly computational investigation*

Q20. **5D geodesic formulation.** Can the (1,2) path be understood as
a geodesic on a 5D manifold (3 space + 1 time + 1 compact)? If so,
the WvM model becomes a specific solution of 5D general relativity,
and charge, spin, and mass emerge from the geometry of the manifold.
*Source: synthesis of F2 and KK theory*
*Status: major theoretical undertaking — essentially asking whether
WvM reduces to Kaluza-Klein theory*

---

## Promoted to Study

(none yet)

---

## Answered

Q7. **Flat compact dimensions and transforms.** Can an extra spatial
dimension be intrinsically flat (a photon experiences straight-line
motion) yet finite and boundary-free, because the coordinate is
periodic? If so, the "toroidal" shape we use to visualize it is a
drawing aid, not a physical shape. What are transforms in this
context, and how does the familiar xyz machinery (translations,
rotations, conservation laws) generalize to compact dimensions?
**Answer:** Yes. A compact dimension is a periodic coordinate —
flat, no curvature, straight-line geodesics. The torus/circle is
only a visualization. Translation in the compact direction gives
charge conservation (Noether's theorem), exactly as translation in
x gives momentum. The EM field is the off-diagonal metric mixing
the compact dimension with spacetime (Kaluza-Klein theory).
→ [Full answer](answers/A7-flat-compact-dimensions.md)

Q1. **Geometric vs topological compactification.** Would a
compactified dimension manifest as a toroid in our 3-space, or is
"toroidal" only a topological description?
**Answer:** Topological only. See A7 §2 — "toroidal" means the
coordinates wrap (S¹ × S¹), not that there is a donut shape in
physical space. A flat torus has zero curvature; the donut shape
is an embedding artifact.
→ [Answered by A7](answers/A7-flat-compact-dimensions.md)
