# Derived clover — toward a first-principles modulated-clover

**Status:** Scaffold only. Brainstorming stage; the criteria list and a
sketch of the hypothesis chain. No derivation yet.

## Scope

- Attempt a hypothesis-driven derivation of the proton/neutron
  substrate from metric-charge Ch 11 foundations + sheet-proton's
  existing constructions.
- Goal: a refinement of modulated-clover whose harmonic / twist /
  modulation choices are *justified* rather than *chosen*, ideally
  with exact 3-fold ring symmetry.
- If the chain holds cleanly, the work file becomes the basis of a
  sheet-proton chapter arc.

---

## Criteria

Tagged **hard** (must hold for the construction to be acceptable) or
**soft** (desired; willing to relax if a hard constraint forces it).

### Hard

- **H1.** Toroidal substrate, periodic in 2 dimensions (consistent
  with metric-charge Ch 1).
- **H2.** Non-circular tube cross-section.
- **H3.** Cross-section has both convex and concave regions; convex
  → + charge density, concave → − (per-arc curvature reading,
  Ch 11 §6 under G1).
- **H4.** Two **distinguishable** fundamental modes correspond to the
  proton and the neutron paths on the substrate.
- **H5.** The two modes' rest energies match the observed nucleon
  masses to within the path-length / eigenmode mechanism's reach
  (at least sign of m_n − m_p; ideally the ratio).
- **H6.** Construction is consistent with metric-charge Ch 11 picture
  A (no contradiction with the foundation).

### Soft

- **S1.** Cross-section may depend on θ (ring angle) — modulation
  allowed.
- **S2.** All shape components expressible as sinusoids (harmonic
  tube-function family).
- **S3.** Exact 3-fold ring symmetry around the central axis —
  motivation: color SU(3) as a 3-fold geometric structure (open
  whether it should be hard).
- **S4.** Solution resembles modulated-clover (which already works
  for charge).
- **S5.** Derivation is from first principles or a named-hypothesis
  chain — not ad-hoc choices.
- **S6.** Mode topology: (1, 2) on a standard torus, or
  equivalently (1/2, 1) on a half-twisted torus.
- **S7.** Models quark substructure to the degree quarks are
  SM-provable; flexible on what exactly a "quark" is if the
  baryon-level model is solid.
- **S8.** Antiparticle / charge-conjugation operation should appear
  as a natural surface symmetry (can defer to metric-binding).
- **S9.** Lower parameter count is better; ad-hoc free parameters
  (e.g., R_major as the only mass-ratio knob) flagged honestly.
- **S10.** Adopt the "wave-in-cavity" framing where it clarifies
  (see brainstorm).

---

## Sketch derivation chain

A hypothesis stack (parallel to Ch 11's G1/H1 naming):

- **C1.** Color → 3-fold cross-section symmetry. The cross-section
  has exact 3-fold rotational symmetry in t.
- **C2.** Spin / closure → fractional t-winding. The
  particle-defining track traverses half the tube per ring
  revolution → half-twist identification.
- **C3.** Harmonic ansatz. Cross-section is in the tube-function
  family with minimal harmonic content compatible with C1.
- **C4.** Modulation in the symmetric subspace. a₁(θ), b₁(θ)
  restricted to (cos, sin)((2k+1)θ/2) with (2k+1) ∈ {3, 9, …},
  the harmonics preserving 3-fold ring symmetry.
- **C5.** Proton / neutron = the two phase-offset (1/2, 1) tracks.

Chain (sketch):

1. **C1 + C3** → cross-section harmonics = cos 3t, cos 6t (+
   imaginary b-parts).
2. **C2 + H1** → half-twist α(θ) = θ/2 is the minimal twist letting
   (1/2, 1) tracks close in one ring rev.
3. **C4** → modulation harmonics restricted to symmetric subspace.
4. **H3 (G1) + H4** → solve for modulation coefficients giving
   Q_proton = +1, Q_neutron = 0 within the constrained subspace.
5. **Path-length mass + H5** → verify the mass-difference sign;
   tune R_major for the ratio.
6. **Reconcile with modulated-clover.md** → the unconstrained
   Step-7 solution is one option in the full harmonic family;
   the symmetric-constrained solution is the candidate here.

---

## Brainstorming items to resolve before expanding the chain

- **Framing: "particle on surface" vs "wave in cavity"?** The
  framework's underlying picture (Ch 11 §1) is a wave equation on
  the compact substrate — the substrate is a cavity, the field
  oscillates in it, and a "particle" is one quantum of a mode.
  The cavity framing may be the more natural language for this
  derivation: separates the *geometric* question (what is the
  cavity?) from the *spectral* question (what modes does it
  support?). Carry through both languages and pick.
- **Is S3 (3-fold ring symmetry) hard or soft?** A color
  interpretation in which the 3 phases of a baryon are
  geometrically interchangeable requires exact symmetry. If the
  3-phase replicas are not load-bearing for the color story, S3
  can stay soft.
- **What is "the proton" relative to the 3 phases?** Three
  options worth listing: (a) a single phase = a single proton; (b)
  a superposition over the 3 phases = a single proton (color
  superposition); (c) a color-singlet combination of 3 phases =
  a single proton (color-singlet baryon, à la QCD). (a)–(c) imply
  different relations to "quark."
- **Is the (1/2, 1) topology forced by spin-1/2 or chosen
  independently?** Half-twist is convenient; whether anything
  upstream forces it (e.g., the framework's spin-1/2 hypothesis)
  is the question.
- **Does the constrained-symmetric search hit (Q_proton,
  Q_neutron) = (+1, 0) exactly with only the 3θ/2 harmonics?** Or
  do we need 9θ/2 (next 3-fold-compatible) harmonics too? A
  small computational exercise — a Step-7 analog restricted to
  the symmetric subspace.
- **Can the cross-section's harmonic content be picked by a
  variational / minimum-action principle** rather than chosen?
  That would graduate C3 from ansatz to derived.
- **How does this reconcile with Ch 8 §7's k = 3 component-link
  mechanism?** Both deliver 3-fold structure; whether they
  describe the same physics or two complementary mechanisms is
  open.
- **What does "quark" mean here?** If proton = single track on a
  3-fold-symmetric surface, the 3 cross-section pieces it covers
  may *be* the three quarks (per the per-arc-curvature reading).
  How rigid is this identification, and does it have to match SM
  quark properties beyond charge (e.g., colour, flavour, mass)?

---

## Open hypothesis IDs (to be assigned as the chain solidifies)

- **G1** (Ch 11 §6) underlies H3.
- **C1–C5** above are working hypotheses; promote to stable IDs
  once stable.
- The path-length mass mechanism's R_major as the free
  one-parameter mass-ratio knob is part of H5; needs its own ID
  if we want to flag it as an input the framework does not yet
  derive.
