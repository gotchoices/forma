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

Q7. **Topological wrapping vs geometric shape.** If we have a
transform equation and we specify that the edges of the dimension
wrap, does the dimension need to be spatially toroidal? Or is it
only mathematically so — like a wrapping digital number that repeats
and rolls over?
*Source: user question*
*Status: answerable from standard differential geometry / KK theory*

Q1. **Geometric vs topological compactification.** If a dimensional
space is compactified and is evident in our 3-space, would/could it
manifest as a toroid? Or is "toroidal" only a topological description
(both dimensions wrap) without requiring the physical shape of a
donut?
*Source: user question*
*Status: answerable — closely related to Q7*

Q4. **1D, 2D, or 3D compact space.** Would a compactified space be
1D (a circle), 2D (a torus surface), or 3D (a solid torus)? What
determines this? A 1D compact dimension (Kaluza-Klein circle) is the
simplest and produces charge naturally. Does WvM need more than 1D?
*Source: user question*
*Status: answerable — the (1,2) knot requires S¹ × S¹ (2D)*

Q3. **Dimensionality of the compact space.** Is the space inside the
toroid 2D or 3D? If the photon path is always on the surface, that
is a 2D space with both dimensions wrapped. Is that what WvM really
describes? Or does the photon trace paths through the internal
volume — not just the surface?
*Source: user question*
*Status: answerable — follows from Q4*

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

### Tier 2 — Answerable with some algebra or paper review

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

(none yet)
