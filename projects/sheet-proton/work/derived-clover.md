# Derived clover — toward a first-principles modulated-clover

**Status:** Hypothesis chain (C1–C6) defined; computational
verification that the chain hits all targets exactly in the
Z₂ × Z₃-symmetric subspace (see Finding). Ready to attempt the
mathematical derivation under the named hypotheses.

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

## Derivation chain

A hypothesis stack (parallel to Ch 11's G1/H1 naming). Each Cn names
an input the chain depends on; the derivation produces a concrete
substrate once C1–C6 are accepted.

- **C1. Substrate topology.** The substrate is a 2D compact
  surface — a torus T² with one ring direction θ and one tube
  direction t. (Inherited from metric-charge Ch 1.)
- **C2. Color → cross-section 3-fold symmetry.** The cross-section
  curve (at any fixed θ) has exact 3-fold rotational symmetry in t,
  realised through harmonic content cos 3t, cos 6t (and imaginary
  sin 3t, sin 6t parts).
- **C3. Closure → surface twist.** The proton and neutron *tracks*
  must close as 1-D loops on the substrate (otherwise no standing
  wave, no charge). Closure requires the surface to support a twist
  α(θ) such that the track's t-rate plus the surface's twist
  identifies the track endpoints. Solving the closure condition
  with the harmonic ansatz of C1+C2 yields a discrete family of
  *allowed* twist rates τ = α′(θ) — multiples of 1/6, broken into
  two sub-cases by the modulation's θ-periodicity (see [derivation
  file] for the full enumeration). The **half-twist** τ = 1/2
  (with antiperiodic modulation in θ) is one candidate; the
  **third-twist** τ = 1/3 (with 2π-periodic modulation, giving
  single-piece tracks) is another. Which is selected — and
  whether one is forced by additional physics — is part of what
  the derivation has to settle. This C3 is no longer a
  pre-commitment to half-twist; it is the closure requirement,
  with the twist value an output rather than an input.
- **C4. Ring-axis 3-fold symmetry.** *(Promoted from soft to hard
  per the Finding below.)* The 3D-embedded surface is invariant
  under 120° rotation around the central (ring) axis. This pins the
  modulation harmonics a₁(θ), b₁(θ) to (cos, sin)((2k+1)θ/2) with
  (2k+1) ∈ {3, 9, 15, …} — only the 3-fold-compatible half-integer
  harmonics. **Caveat:** willing to relax to soft if downstream
  physics gives a compelling reason (e.g. multipole structure
  needed for the residual nuclear force).
- **C5. Per-arc charge under G1.** Along each (1/2, 1) track, the
  integrated geodesic curvature normalised by 2π gives the integer
  KK winding number; signed contributions from convex (κ_g > 0) and
  concave (κ_g < 0) sub-arcs sum to the integer total.
- **C6. Proton / neutron identification.** The two distinct
  (1/2, 1) tracks (offset by π/3 in t, one piece) are the proton
  and neutron modes; the Z₂ × Z₃ orbit of one fundamental track is
  the 6 baryon replicas (3 proton phases + 3 neutron phases).

Derivation chain:

1. **C1 + C2** → cross-section family is the N = 3 harmonic
   tube-function: w(t) = 1 + a₁ cos 3t + a₂ cos 6t + i(b₁ sin 3t +
   b₂ sin 6t).
2. **C1 + C3** → twist α(θ) = θ/2; surface identification
   (t, θ + 2π) ~ (t + π, θ); (1/2, 1) tracks close in one ring
   revolution.
3. **C4** → modulation a₁(θ), b₁(θ) restricted to k=1 (and higher,
   if needed) symmetric half-integer harmonics.
4. **C5 + C6** → per-arc charge integrals along the two tracks fix
   Q_proton = +1, Q_neutron = 0 — pins the modulation coefficients.
5. **Path-length mass mechanism** → m_n / m_p = L_proton / L_neutron;
   R_major tunes the ratio to the observed value.

The Finding below establishes that this chain is concretely
realisable with exact charge match and exact mass-ratio match in
the symmetric subspace (R_major ≈ 36.17, only k=1 harmonics
needed). Reconciliation with [modulated-clover.md](modulated-clover.md):
the unconstrained Step-7 solution is one charge-correct point in
the full harmonic family; the symmetric-constrained solution
derived here is the cleaner one that respects C4.

---

## Inverse-problem formulation (modes-first)

The constructive chain C1–C5 builds the substrate forwards from
hypotheses. The same target can be stated **inversely** — what we
are really looking for is:

> A compact substrate metric whose Laplace-Beltrami spectrum has
> **two low modes** with the following properties:
>
> - KK winding (+1, 0) — i.e. mode charges m_p = +1, m_n = 0.
> - Characteristic curves of length-ratio L_p / L_n = m_n / m_p
>   (observed nucleon mass ratio).
> - Per-arc κ_g profile along each characteristic curve summing
>   to the integer global charge (+1 for proton, 0 for neutron),
>   under hypothesis G1.
> - The substrate is invariant under Z₂ × Z₃ (3-fold ring
>   symmetry + the half-twist modulation flip).
> - Lowest free-parameter count compatible with the above.

This is the **inverse spectral problem** — "find a substrate
whose spectrum looks like this." The constructive chain C1–C5 is
*one candidate route* into this inverse problem. There may be
others (different cross-section ansätze, different twists,
3D-cavity rather than 2D-surface substrate). Holding both
formulations in view lets us tell *forced* features (those that
fall out of the inverse problem's constraints) from *chosen*
features (those that come from the C1–C5 ansatz alone).

---

## Physical reading — helix-on-helix interpretation

Recording the physical reading the construction sits inside, as
motivation rather than derivation. (None of these is load-bearing
for the math; they are framework-consistent restatements.)

- **Mass = standing wave in a compact dimension, viewed as a
  helix through time.** A real standing wave φ_n + φ_{−n} carries
  *equal and opposite* handedness around the compact loop. Mass
  depends on |n|, so it is unsigned — and gravity, sourced by
  mass-energy, is correspondingly unsigned. (Metric-mass Ch 2.)
- **Charge = second-order helix, on a second compact direction
  orthogonal to the mass one.** Its handedness *is* signed — the
  sign of the second-direction winding m is the sign of EM
  charge under the KK identification. (Metric-charge Ch 5.)
- **Fractional charge = micro-structure of the second helix.**
  When the helix's cross-section is non-round, its convex and
  concave regions carry locally + and − signed contributions to
  the integrated charge. (Per-arc reading under G1; Ch 11 §6.)
- **Force (gravity / EM) = mutual spacetime warping.** A wave
  warps spacetime via its stress-energy (gravity); via the
  off-diagonal compact-direction metric components (EM, by KK
  reduction). Two waves interact through this warping, and the
  resulting trajectory deflections *are* the forces.

These readings are the physical narrative *of* the framework
content, not extra commitments.

---

## A candidate brainstorm: unifying Coulomb with the residual
## nuclear force via micro-multipole structure

Out of the readings above falls a forward-looking candidate worth
flagging:

- A nucleon-as-modulated-clover surface has an integer **+1 monopole
  charge** (per-arc integral around its characteristic curve).
- It *also* has a non-trivial **multipole structure**: small
  concave (−) pockets nested between large convex (+) lobes, in
  3-fold symmetry.
- At large separations between two such nucleons, the
  monopole–monopole interaction dominates → ordinary Coulomb
  repulsion (+1 vs +1).
- At small separations (≲ characteristic substrate size), the
  higher multipoles dominate over the monopole. Two clovers
  rotated by 60° relative to each other would have their + lobes
  geometrically *interlocking with the other's − pockets* → short-
  range attractive force, with 3-way Z₃ alignment.
- This mechanism would unify Coulomb with the **residual nuclear
  force** between nucleons — same EM-via-KK channel, but
  multipole-dominated at short range and monopole-dominated at
  long range.

**What this is and is not.** This is *not* a unification with the
fundamental colour force of QCD (which is a Yang–Mills gauge
theory, a different mechanism). It is a candidate unification
with the *residual* nuclear force — the force between colourless
nucleons, which in QCD is itself an effective theory built from
exchange of mesons (pions, ω, …) carrying various multipole
moments. The candidate here says the modulated-clover surface
*directly carries* those multipole moments via its concave-
convex cross-section structure, with the same EM-KK channel
mediating both long- and short-range interactions.

Worth flagging as a downstream calculation target once the
derived-clover substrate is in hand: compute the monopole +
leading multipole moments of the proton/neutron modes, and check
whether the short-range potential they produce qualitatively
matches the observed nucleon–nucleon potential (binding around
~1 fm, hard repulsive core inside).

---

## Open questions for the math derivation

Items still open. Resolved items have been folded into the chain or
the Finding.

- **Particle-on-surface vs wave-in-cavity framing.** Cavity is
  primary at the wave level; particle-on-track is the semi-classical
  projection along the mode's characteristic curve. Pick which the
  formal derivation leads with — they coincide at the (1/2, 1) tracks
  but differ in how the math is set up.
- **What is "the proton" relative to the 3 phases?** Three readings
  to choose between: (a) a single phase = one proton, (b) a
  superposition over the 3 phases = one proton (color superposition),
  (c) a color-singlet combination = one baryon (à la QCD's
  colour-singlet baryon). The mathematical setup for the per-arc
  charge integral and the mass-ratio formula doesn't distinguish
  (a)–(c) at the substrate level, but downstream physics (matrix
  elements, magnetic moments) will.
- **Is the (1/2, 1) topology forced or chosen?** C3 is currently an
  *input* hypothesis. Whether anything upstream (e.g. a spin-1/2
  requirement enforced at the wave-equation level) *forces* the
  half-integer winding, or whether it remains an input choice, is the
  cleanest hypothesis-shrinking question.
- **Can the cross-section's harmonic content be derived from a
  variational principle** rather than postulated? Would graduate
  C2 + C3 from ansatz to derived. (Possible angle: minimise some
  combination of intrinsic-curvature integral + closure-constraint
  Lagrange multipliers under the Z₂ × Z₃ symmetry.)
- **Reconcile with Ch 8 §7's k = 3 component-link mechanism.** Both
  give 3-fold structure but on different structural axes (per-knot
  vs per-arc). Are they the same physics in different language, or
  two complementary mechanisms?
- **Operational meaning of "quark" in the derivation.** If the
  proton = single (1/2, 1) track covering 3 cross-section pieces,
  the 3 pieces are *candidate* quarks. How rigid is this
  identification, and what SM quark properties (colour assignment,
  flavour identification, current-quark masses) does the
  identification have to match?
- **R_major as the mass-ratio knob.** Currently the only free
  parameter that survives the constrained construction. Is there an
  independent input that pins R_major (e.g., the Compton scale of
  the lightest stable baryon), or does R_major stay free?

---

## Finding — Z₂ × Z₃ symmetry is fully compatible with all targets

(Computational result, 2026-05-26. `scripts/modulated_clover.py --step 7
--symmetric` plus an R_major sweep.)

Restricting the modulation to the Z₂ × Z₃-symmetric subspace (only the
k=1 half-integer harmonics cos(3θ/2), sin(3θ/2) for both a₁(θ) and
b₁(θ); the k=0 cos(θ/2), sin(θ/2) terms set to zero) gives a 7-parameter
construction (vs 9 for the unconstrained Step 7) that **simultaneously
hits every target**:

| Quantity | Value | Status |
|---|---|---|
| Q_proton | +1.0000000 | exact (under G1) |
| Q_neutron | −0.0000000 | exact (under G1) |
| L_p / L_n | 1.0013784 | exact (= observed m_n/m_p) at R_major ≈ 36.17 |
| Charge-error magnitude | 4.9 × 10⁻⁹ | numerical noise |
| Z₂ × Z₃ ring symmetry | exact | by construction |

Best-fit symmetric coefficients (at R_major = 36.17 for mass-ratio
match; modulation coefficients found by DE):

  Ac = [0,  −0.48765];  As = [0, +0.65694]
  Bc = [0,  −0.00038];  Bs = [0, +0.00032]
  a2 = 0.32994;  b2 = +0.03201;  R_major ≈ 36.17

So **S3 (3-fold ring symmetry) can be promoted from soft to hard**: it
costs nothing relative to the unconstrained construction — same exact
charges, same exact mass ratio — and reduces the parameter count by 2
while making the symmetry structure clean. The (proton, neutron) pair
is now a literal Z₂ × Z₃ orbit of one fundamental track.

This also rules in S5 (first-principles derivation): the symmetric
subspace can be derived from the (color → 3-fold) hypothesis C1
without further ad-hoc choices.

R_major remains the 1-parameter knob that tunes the mass ratio (same
status as in the unconstrained construction); the symmetric subspace
doesn't remove this — it just fixes the modulation harmonic content
to the minimal symmetric family.

---

## Hypothesis dependency

The chain depends on the following named hypotheses:

- **C1.** Substrate topology = T² (inherited from metric-charge Ch 1).
- **C2.** Color → cross-section 3-fold symmetry (cos 3t, cos 6t
  harmonic content). *Input.*
- **C3.** Spin → half-integer t-winding → half-twist surface
  (α(θ) = θ/2). *Input.*
- **C4.** Ring-axis 3-fold symmetry → symmetric modulation harmonics.
  *Derived from C2 if we additionally assume the embedded surface
  inherits the cross-section symmetry; otherwise an independent
  input. Currently hard, with caveat for relaxation.*
- **C5 / G1.** Per-arc curvature = charge density (Ch 11 §6). *Input.*
- **C6.** Proton and neutron are the two distinct (1/2, 1) tracks
  on the substrate. *Identification; physical content of "what is
  a baryon."*
- **R_major** is a free real parameter that tunes the mass ratio.
  Not derived. Could in principle be pinned by an independent input
  (e.g., a Compton-scale identification for the lightest stable
  baryon), but currently a free knob.

Once C1–C6 are committed, the construction is parameterised by
the symmetric modulation coefficients (Ac₁, As₁, Bc₁, Bs₁), the
backbone (a₂, b₂), and R_major. The first four are pinned by
demanding Q_proton = +1, Q_neutron = 0. R_major is set by the
mass-ratio match. The construction is then complete.
