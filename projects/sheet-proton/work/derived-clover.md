# Derived clover — toward a first-principles modulated-clover

**Status:** Groundwork file. The C1–C6 hypothesis chain is defined,
the per-arc charge integral is set up analytically, the symmetric
construction has been computationally verified to hit every target
(see Finding), and the framework's discrete symmetries (chirality,
charge conjugation, multi-sheet caveat) are written down. The
exploratory work is complete; **the next step is the formal
mathematical derivation, which belongs in the parent sheet-proton
folder (chapter arc), not here.** This file's role is the
*ansatz / fit-derivation* (i.e., "what type of substrate could
host the observed quark-domain physics?") whose conclusions feed
the formal derivation.

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

## Per-arc charge integral — the analytical machinery

Under G1 (Ch 11 §6), the charge along a closed track is the
integrated geodesic curvature:

  Q(t₀) = (1/2π) ∫_track ∂_t χ dt,

where χ = arg(∂_t ζ) is the tangent direction of the cross-section
curve at fixed θ. For a (1/2, 1) track t(θ) = t₀ + θ/2 on the
half-twisted surface, ζ = ρ·e^{i(α+t)}·w(t;θ) with α(θ) = θ/2 and
A ≡ ∂_t w + i w; differentiation gives

  ∂_t χ = 1 + Im(Ā · ∂_t A) / |A|².

The "1" integrates trivially over the track to give the **base
charge ½ per track** (a "half-turn in cross-section tangent over
half the loop"). The modulation-dependent correction M(t₀) supplies
the integer-completing piece:

  **Q(t₀) = ½ + M(t₀)**,
  M(t₀) = (1/4π) ∫₀^{2π} [Im(Ā ∂_t A) / |A|²]|_{t=t₀+θ/2} dθ.

For (Q_proton, Q_neutron) = (+1, 0), the modulation must supply
M(−π/6) = +½ and M(+π/6) = −½ — a unit jump between the two
tracks. **This is the core analytical statement the construction
needs to satisfy.**

### Allowed twists from closure

The surface closes as a torus iff τ = α′(θ) is a multiple of 1/6.
Two sub-cases:

- **Periodic modulation** in θ: allowed twists τ ∈ {0, 1/3, 2/3, …}
  (multiples of 1/3).
- **Antiperiodic modulation** (a₁(θ+2π) = −a₁(θ)): allowed twists
  τ ∈ {1/6, 1/2, 5/6, …} (half-integer in units of 1/3).

τ = 1/2 (half-twist + antiperiodic modulation) is the **unique choice
compatible with symmetric per-baryon target charges (+½, −½) at
first-order perturbative modulation.** Other twists either don't
support the target topology or produce asymmetric magnitudes that
the perturbative formula can't accommodate.

### First-order constraint

A perturbative expansion around the unit-circle gives, to first
order in modulation amplitudes,

  M(t₀) ≈ (9A/4) cos 3t₀ + (3B/4) cos(3t₀ + φ),

where (A, φ_a) and (B, φ_b) are the amplitudes and phases of the
k=1 symmetric harmonics (cos(3θ/2), sin(3θ/2)) in a₁(θ) and b₁(θ),
with φ ≡ φ_b − φ_a (one phase absorbed by θ-origin shift). At
t₀ = ±π/6 the A-term vanishes; the constraint is then **B sin φ =
2/3**. The 6-fold backbone (a₂, b₂) does not contribute at first
order. The constraint requires non-small amplitudes, so the
quantitative match needs the full (non-perturbative) integral —
which the Finding below verifies numerically.

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

## Symmetries — chirality, C, multi-sheet

The construction natively supplies a **Z₂ × Z₂ space of discrete
internal symmetries** on each (m, n) baryon mode, organised as
*chirality × charge-conjugation*. Three Z₂ operations act on the
mode labels:

| Operation | (m, n) → | Identification |
|---|---|---|
| t-reflection (P_t) | (−m, n) | chirality flip |
| θ-reflection (P_θ) | (m, −n) | chirality flip (equivalently P_t) |
| Complex conjugation (C) | (−m, −n) | matter ↔ antimatter |

C is *not* (m, ±n) vs (m, ∓n); that pair has the same matter/antimatter
status but opposite *chirality*. The C-conjugate of a (+½, +1) RH
proton is (−½, −1), an RH antiproton — both signs flip.

Per (|m|, |n|), four distinct modes:

  (+½, +1) RH proton, (+½, −1) LH proton  — same matter/antimatter, opposite chirality.
  (−½, −1) RH antiproton, (−½, +1) LH antiproton  — C-conjugates of the above.

The framework's chirality is **geometric** (sign of relative winding
direction; equivalently, the helical sense of phase advance on the
torus). It is *not* yet γ⁵-chirality in the Dirac sense — that would
require promoting the scalar field to a spinor field with spin
structure on the substrate. The two pictures coincide at the
*combinatorial* level (4 modes organised as 2×2 = Z₂×Z₂); formal
identification with γ⁵ chirality needs the spinor upgrade and is
deferred.

### Multi-sheet caveat

The construction is single-sheet — u and d quarks both on this
substrate, heavier-quark sheets (s, c, b, t) presumed to live on
separate substrates per the framework's standard "one generation per
sheet" reading. But several observed hadrons require
**mixed-generation quark content**: Λ (uds), Σ (uds/uus/dds), Ξ
(uss/dss), Ω⁻ (sss). These cannot be hosted by a single-sheet
baryon construction without a *multi-sheet coupling* that lets a
wave mode span more than one substrate.

This is not a problem derived-clover has to solve; the multi-sheet
mechanism belongs to metric-binding. But it *is* a constraint
downstream: any future multi-sheet mechanism has to be compatible
with the single-sheet construction here, and the construction
should not depend on "every baryon lives on exactly one sheet"
anywhere load-bearing. Currently it does not.

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

---

## Wave / track reconciliation — status

The construction has been calibrated under the *particle-on-track*
reading: charge from the per-arc curvature integral along the
(1/2, 1) tracks, mass from the path-length formula
m = 2 π ℏ c / L_track. The companion *wave-on-substrate* reading
would derive the same numbers from the 2-D Laplace–Beltrami
spectrum of the modulated-clover surface itself.

The two readings are **not equivalent** on this surface, by direct
computation. See [lb-mode-localization.md](lb-mode-localization.md):

- No individual LB eigenmode (up to √λ ≈ 1.5) is appreciably
  track-localised — modes are stripes spanning the full (t, θ)
  parameter space, with enrichment E ≲ 1.07 against E_perfect ≈ 3.
- Allowing arbitrary low-energy superpositions does *not* rescue
  Reading α at the proton energy: the best superposition with
  √⟨H⟩ at the proton wavenumber (≈ 0.028) has enrichment depth
  < 1 %. Localisation depth crosses 5 % only at ~3 × proton
  energy, 30 % only at ~30 × proton energy.

The construction in this file remains the canonical *substrate*;
the calibration of charge and mass on it remains correct. What is
now closed is the question of whether the same numbers can be
derived from the 2-D wave equation by a semi-classical limit —
they cannot, on this surface, at this energy scale.

**No reconciliation is currently in hand.** Reading β
(multi-quantum, fermionic spinor upgrade) is a *reinterpretation*
that sidesteps the requirement rather than a derivation of
equivalence — three wave-quanta (one per phase track) replacing
one wave-quantum on three tracks, with each track-quantum now
carrying the constituent-quark mass and R_major rescaling by ~3×.
That keeps the framework wave-fundamental but does *not* recover
Reading α's calibration; the construction would need re-calibrating
under it.

Routes not yet tried that could in principle still close the
gap on this substrate: high-eigenvalue scarring on closed
geodesics (does not help the proton specifically); a *restricted*
Laplacian on a specific Z₃ irrep; phase-space (Husimi)
localisation; a sharper-tube metric on the same substrate.
None has been worked out. See the parent README's
"reconciliation gap — status" section.

---

## Open questions for the formal derivation

Items the parent-folder mathematical derivation should address.
Resolved items are folded into the chain, the per-arc machinery,
the Finding, the Symmetries, or the Wave/track reconciliation
sections above.

- **Particle-on-track vs wave-in-cavity framing.** The
  computation in [lb-mode-localization.md](lb-mode-localization.md)
  shows that the two framings give *different* physics at the
  proton's energy scale — they do not coincide on this surface.
  The construction's calibration uses the particle-on-track
  reading; the wave-on-substrate reading does not reproduce the
  same numbers semi-classically. The chapter arc must take a
  position on which reading the proton lives in. Reading β
  (multi-quantum / fermionic) is the natural resolution.
- **Is the (1/2, 1) topology forced or chosen?** C3 is currently
  *input*. Whether anything upstream (a spin-½ requirement at the
  wave-equation level) *forces* the half-integer winding is the
  cleanest hypothesis-shrinking question.
- **Can the cross-section's harmonic content be derived from a
  variational principle** rather than postulated? Would graduate
  C2 + C3 from ansatz to derived. (Possible angle: minimise an
  intrinsic-curvature functional under the Z₂ × Z₃ symmetry.)
- **Reconcile with Ch 8 §7's k = 3 component-link mechanism.**
  Both give 3-fold structure on different structural axes — same
  physics in different language, or two complementary mechanisms?
- **What is "the proton" relative to the 3 phases?** (a) single
  phase = one proton, (b) superposition over 3 phases = one
  proton, or (c) color-singlet combination = one baryon. The
  per-arc charge integral and the mass-ratio formula don't
  distinguish (a)–(c) at the substrate level; downstream
  observables (magnetic moments, matrix elements) will.
- **R_major as the only surviving free parameter.** Is there an
  independent input that pins R_major (e.g., a Compton-scale
  identification for the lightest stable baryon), or does it
  stay free? Without that, m_n/m_p is calibration, not
  prediction.
- **Promotion of geometric chirality to γ⁵ chirality** requires a
  spinor upgrade of the scalar field (spin structure on the
  substrate). Forward-looking; not in scope here.
