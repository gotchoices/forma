# 2D harmonic-oscillator bridge for metric-charge

**Status:** Exploratory. Not chapter-grade. See
[work/README.md](README.md) for context.

## Scope

Test whether the harmonic-oscillator (HO) translation that
[metric-mass Chapter 9](../../metric-mass/09-harmonic-oscillator-bridge.md)
introduces for the 1D compact case extends usefully to the 2D
compact sheet of metric-charge. If clean, it would land as a
follow-up appendix to metric-charge, structurally parallel to
metric-mass Ch 9 but with 2D-specific payoffs.

This file does not write the appendix. It works out whether the
appendix can be written cleanly and what would need to be in it.

## What metric-charge already has

[Chapter 2 §3](../02-modes-on-a-sheet.md) derives the 2D rest mass

<!-- m_(m,n) = (ℏ/c) · √((2πn/L_u)² + (2πm/L_w)²) -->
$$
m_{(m,n)} \;=\; \frac{\hbar}{c}\,\sqrt{\left(\frac{2\pi\,n}{L_u}\right)^2 + \left(\frac{2\pi\,m}{L_w}\right)^2}
$$

as the **Pythagorean combination** of the two single-direction
masses. Equivalently:

<!-- m² = m_u(n)² + m_w(m)² -->
$$
m^2 \;=\; m_u(n)^2 + m_w(m)^2
$$

where m_u(n) = ℏ|n|/(R_u c) and m_w(m) = ℏ|m|/(R_w c) are the
"u-only" and "w-only" rest masses that each direction would produce
in isolation. The (m, n) mode family is identified with topological
winding pairs (Ch 2 §5.3); compact-direction momenta p_u, p_w are
identified with Kaluza-Klein conserved charges (Ch 2 §5.1, Ch 5).

**Convention used throughout this file:** (m, n) = (w-direction
winding, u-direction winding) per Ch 2. The tube count m goes with
w; the ring count n goes with u. Ladder operators and joint
occupation numbers are ordered the same way: a_w paired with the
m label, a_u paired with the n label.

## Interpretive status of the bridge

Before the translation, one interpretive choice has to be made
explicit. Quantising the wave equation on T² admits two distinct
ladder structures, and which one the bridge adopts determines what
the bridge actually claims.

- **Picture A (QFT on T²).** Canonical quantisation of the field
  on T² gives **one ladder per mode** — operator pair
  (a_{m,n}, a†_{m,n}) for every winding pair (m, n) ∈ ℤ². The
  Fock space is the tensor product over all (m, n). Single-quantum
  states have one quantum in some specific mode; multi-quantum
  states populate multiple modes. The continuous symmetries of the
  spectrum are the U(1) × U(1) of compact-direction translations,
  plus a discrete dihedral group acting on the (m, n) integer
  lattice at R_u = R_w. There is **no** continuous SU(2).

- **Picture B (2D HO overlay).** Treat the system as a 2D
  harmonic oscillator with **two ladders** (a_w, a_u), one per
  compact direction. The joint occupation (m, n) is the number of
  quanta of each ladder. The Fock space is the tensor product of
  two single-oscillator Fock spaces. The continuous symmetries
  include U(1) × U(1) and, at ω_u = ω_w (equivalent to R_u = R_w
  for the massless wave), a full continuous SU(2) mixing the two
  ladder operators.

The two pictures share the same one-quantum-per-mode spectrum
({(m, n)} ↔ {|m, n⟩}) but **differ at multi-quantum level and in
their continuous-symmetry algebras.** Picture A is what canonical
quantisation of the wave equation gives directly; picture B is a
structural overlay that imports HO algebraic content onto the
spectrum.

**This file works in picture B**, parallel to
[metric-mass Ch 9](../../metric-mass/09-harmonic-oscillator-bridge.md)'s
adoption of the 1D HO overlay. The choice is interpretive, not
derivational: the wave equation does *not* require picture B.
What picture B buys is algebraic machinery (continuous SU(2) at
isotropy, coherent states, etc.) that picture A does not carry;
what it gives up is strict equivalence with the canonical
quantisation. **Where picture B's predictions are specific (e.g.,
continuous SU(2) at ε = 1), they are overlay-conditional, not
derived consequences of the wave equation.** Any appendix has to
say this up front.

## The 2D HO translation

Working in picture B (per the previous section), the u- and
w-pieces of the separated wave equation are each treated as 1D
simple harmonic oscillators in the same overlay sense
[metric-mass Ch 9 §2](../../metric-mass/09-harmonic-oscillator-bridge.md)
made explicit for the single-direction case. Promoting to operator
algebra gives two independent ladders, one per compact direction:

<!-- [a_w, a_w†] = 1,  [a_u, a_u†] = 1,  [a_w, a_u] = [a_w, a_u†] = 0 -->
$$
[\,a_w,\;a_w^\dagger\,] = 1,
\qquad
[\,a_u,\;a_u^\dagger\,] = 1,
\qquad
[\,a_w,\;a_u\,] = [\,a_w,\;a_u^\dagger\,] = 0
$$

Joint occupation numbers (m, n) label basis states |m, n⟩ on the
tensor-product Fock space: m quanta of the w-ladder, n quanta of
the u-ladder.

Translation, line by line:

| Classical wave reading (Chapter 2) | 2D HO overlay reading |
|---|---|
| Mode function e^{i(m w/R_w + n u/R_u)} | Number eigenstate \|m, n⟩ |
| Winding pair (m, n) = (w, u) from periodicity on both cycles | Joint occupation numbers (m, n) |
| Compact momenta p_w = ℏm/R_w, p_u = ℏn/R_u | Canonical momenta of the two ladders |
| Rest mass m² = m_u² + m_w² (Pythagorean *sum of squares* of two single-direction rest masses) | Spectrum collapses to the same one-quantum-per-mode values; *not* the HO additive sum ℏω_w m + ℏω_u n |
| Off-diagonal metric h_μw on extended spacetime | KK gauge *field* B_μ — a 1-form on extended spacetime that the dimensional reduction reads off h_μw ([Ch 5](../05-metric-self-consistency.md)) |
| Compact-direction momentum p_w | Conserved U(1) *charge*, eigenvalue of the w-tower generator; couples to B_μ |

The structural shift from 1D to 2D is the appearance of a
**second ladder**. Everything that was a single-tower story in
metric-mass becomes a joint-tower story here.

(One feature of the Ch 2 reading that does not transfer cleanly
into picture B: the ±n traversal-orientation distinction of Ch 2
§5.1. In picture A each (m, n) and (m, −n) is a separate mode
with its own ladder; in picture B the u-ladder occupation n is
non-negative, and the sign-of-winding information is carried by a
separate orientation label. The R_u- vs R_J-symmetrisation
constructions of Ch 5–6 belong naturally to picture A, not to the
bare picture B; importing them into the overlay requires extra
structure not specified here.)

### One reconciliation worth being explicit about

The non-relativistic HO spectrum is *linear additive* in occupation
numbers:

E_HO = ℏω_u (n + 1/2) + ℏω_w (m + 1/2)

whereas the relativistic Klein-Gordon dispersion gives a *Pythagorean*
combination m² = m_u² + m_w² of effective rest masses. These differ
because they are different physical setups (non-relativistic harmonic
potential vs. relativistic massless wave). **The HO bridge holds at
the level of mode counting, ladder structure, and symmetry algebras
— not at the level of energy formulas.** Any appendix should state
this distinction up front so a reader does not expect E = ℏω_u n +
ℏω_w m to drop out of the 2D wave equation.

## Hypothesis A: incremental mass (Layered construction)

**Hypothesis (project-direction):** Dim 1 produces a rest mass m_1
from circulating light; dim 2 then "disposes m_1" and produces a
new, second-order mass m_2 that depends on m_1.

**Test against Ch 2.** The closed-form rest-mass formula is
Pythagorean, m² = m_u² + m_w², not sequential. The two windings
contribute symmetrically; neither is functionally computed from the
other.

**Where the layered intuition is valid as a re-derivation.** The
same Pythagorean answer can be reached sequentially: treat m_u as
the rest mass of a 1D-compact particle, then add a second compact
direction w carrying its own Kaluza-Klein momentum p_w = ℏ·2πm/L_w.
(The w-direction stays *compact* throughout — it is not promoted to
an extended/non-compact direction; the layering is over how the
mass formula is assembled, not over whether w is geometrically
compact.) The relativistic dispersion gives

<!-- E² = (p_w c)² + (m_u c²)² -->
$$
E^2 \;=\; (p_w c)^2 + (m_u c^2)^2
$$

and at p_S = 0 with p_w = ℏ·2πm/L_w:

<!-- m_rest² = m_u² + m_w² -->
$$
m_{\text{rest}}^2 \;=\; m_u^2 + (p_w/c)^2 \;=\; m_u^2 + m_w^2
$$

— the same answer as the symmetric joint-quantization picture, just
derived from a "build mass on dim 1, then put it in motion on dim 2"
viewpoint.

**Conclusion.** The incremental reading is a **valid pedagogical
narration** of the same derivation. It does not produce a new
formula, and it is not a multi-level mechanism in which mass
compounds. Its value is interpretive: each new compact direction's
winding contributes an additional rest-energy term that combines in
quadrature with the previous one — and the operator-algebra reading
makes this concrete (each direction = a new ladder; total energy
combines over ladders).

Worth including in the appendix if accompanied by the honest
statement that symmetric and sequential readings yield identical
results.

## Hypothesis B: charge requires prior mass

**Hypothesis (project-direction):** The 2π enclosure on dim 2
creates observable EM charge only if the previous layer had its own
winding (its own "mass").

**Test against Ch 4.** The closure condition has two parts:
- **Necessary condition (Ch 2 §4.2):** both windings be nonzero.
  Single-axis modes (m, 0) and (0, n) produce mass without
  observable EM.
- **Sufficient condition (Ch 4):** within the both-nonzero family,
  the m | n synchronisation criterion must also hold.

So the correct headline is: **charge requires non-trivial winding
in both compact directions** *and* **the m | n synchronisation
that Ch 4 develops within the both-nonzero family.** The "prior
mass" hypothesis captures the necessary half of this, not the
sufficient half.

The hypothesis's "prior mass" reading is one way to narrate the
necessary part: dim 1 winding gives the first ladder a non-trivial
state ("prior mass"), dim 2 winding gives the second ladder a
non-trivial state, and only joint excitation provides the
chirality structure that the synchronisation criterion can then
test.

**Conclusion.** The hypothesis maps cleanly onto the existing
closure condition as a re-narration. It does not introduce a new
mechanism. It does provide an intuitive sequential story —
*build mass first, then add charge by adding a second
winding* — that is appendix-grade pedagogy.

## Symmetry payoffs (overlay-conditional)

**Generic anisotropic case (L_u ≠ L_w): U(1) × U(1) — robust in
both pictures.** Each ladder carries its own phase symmetry; the
two associated Noether-conserved charges are p_w and p_u. The KK
identification of compact momenta with charge that Ch 2 §5 and
Ch 5 already use is exactly this U(1) × U(1). This is realised in
*both* pictures (A and B) and is structural, not
overlay-conditional.

**Isotropic case (L_u = L_w, ε = 1): continuous SU(2) in picture
B only.** At equal radii the 2D-HO Hamiltonian becomes invariant
under arbitrary unitary mixing of the two ladder operators
(a_w, a_u) → U·(a_w, a_u). The unitary group is
U(2) = U(1) × SU(2); the extra SU(2)/U(1) generators act on the
overlay's ladder operators.

**The wave equation on T² at R_u = R_w does *not* carry a
continuous SU(2).** Its spectrum m² ∝ m² + n² is invariant under
the discrete *dihedral* group D_4 (90° rotations + reflections of
the integer (m, n) lattice) plus a Z_2 of overall sign flip. A
continuous SO(2) acting on (m, n) as real coordinates would not
preserve the integer lattice — irrational rotations take integer
modes to non-existent intermediate values — so it is *not* a
symmetry of the actual mode spectrum.

So the SU(2) "prize" is overlay-conditional. Whether it is
physically realised depends on whether picture B is the right
quantisation of the geometry, not on the geometry alone.

[Chapter 7](../07-aspect-ratio-and-character.md) currently treats
ε = 1 as the boundary between thin-sheet and fat-sheet regimes.
The reading depends on the picture:

| Picture | What happens at ε = 1 |
|---|---|
| A (wave equation on T²) | Discrete D_4 lattice symmetry: a point of *finite-group* symmetry enhancement |
| B (2D HO overlay) | Continuous SU(2): a point of *Lie-group* symmetry enhancement |

Both pictures agree that ε = 1 is structurally distinguished; they
disagree on whether the enhancement is continuous or discrete.

Whether the continuous SU(2) of picture B is realised as any
framework target (a candidate for weak isospin? for spin? a
different internal symmetry?) cannot be settled until the picture-
faithfulness question is settled. The framework's existing
posture, mirrored in
[higher-order-charges.md](higher-order-charges.md), treats
isotropy-enhanced continuous symmetries as *structural shadows* —
real algebraic facts about the overlay, but not yet derived
symmetries of the physical geometry. The 2D SU(2) story belongs
in the same category.

## Coherent-state knots

A single (m, n) mode is delocalised over the entire sheet. Picture
B (the 2D HO overlay) provides **coherent states** |α_w, α_u⟩ —
joint eigenstates of the lowering operators (a_w, a_u) — that
are minimum-uncertainty Gaussian wavepackets on T² and trace
classical trajectories without spreading. Coherent states make
"where the wavepacket is on T²" a well-defined question, replacing
the plane-wave delocalisation with localised blobs.

**What coherent states do *not* automatically give:** the
classical trajectory of a standard 2D-HO coherent state is an
**ellipse** in (w, u) at frequencies ω_w and ω_u — *not* a torus
knot T(m, n). To produce a wavepacket that follows the T(m, n)
torus-knot trajectory you need a more specific construction
(e.g., a coherent state built from the (m, n)-momentum eigenmode
itself, which is *not* the standard 2D-HO coherent state), and
the construction depends on which classical orbit you want to
follow.

So the upgrade gives wavepacket *localisation* automatically;
*knot-trajectory tracking* is an additional construction not
supplied by the bare 2D-HO coherent state.

[Chapter 3](../03-knots-on-the-torus.md) currently reframes the
(m, n) modes geometrically as knots traversing the sheet, built
on plane-wave mode functions. The coherent-state upgrade is
useful for the localisation half of what Ch 3 needs; the
knot-trajectory half is an open construction, not a clean
translation.

Not developed here. Flagged as candidate appendix material whose
scope (wavepacket localisation, or also knot-trajectory tracking
once the construction is worked out) is itself an open question.

## Open questions before an appendix is writable

1. **Energy-formula reconciliation.** Make the
   additive-vs-Pythagorean distinction explicit so the reader is
   not misled. (Resolved here in principle; needs careful prose.)

2. **Is picture B (the 2D HO overlay) faithful to the physics, or
   only an algebraic structure laid over picture A?** The
   continuous SU(2) at ε = 1 is a property of picture B; the
   wave equation on T² (picture A) carries only discrete D_4 at
   the same point. For the SU(2) "prize" to land as a real
   geometric symmetry of the framework, one of two things has to
   happen: (a) the framework supplies a physical mechanism that
   upgrades the wave equation's D_4 to continuous SU(2), or
   (b) picture B is established as the *physically correct*
   quantisation of the geometry, not just an algebraic overlay
   that happens to share the one-quantum spectrum. Currently
   neither path is in scope. Until this is resolved, any appendix
   has to report the SU(2) as overlay-conditional rather than as
   a derived geometric symmetry. This is the most consequential
   open question in the file.

3. **Coherent-state knot dynamics.** A standard 2D-HO coherent
   state gives wavepacket localisation but follows an *elliptical*
   classical orbit, not a T(m, n) torus knot. What construction is
   needed for a wavepacket that follows the (m, n) torus-knot
   trajectory? If such a construction exists, this would give a
   clean "knot as classical orbit, particle as coherent quantum
   state of the orbit" reading. Open whether the localisation
   alone (without knot-trajectory tracking) is enough for the
   appendix, or whether the full construction has to be worked out
   first.

4. **Closure condition in operator language.** Does the m | n
   closure condition have a natural characterization in terms of
   ladder operators? Not obvious this is illuminating, but worth a
   one-paragraph attempt before dismissing.

5. **What pieces (if any) belong as back-edits to existing
   chapters?** The U(1) × U(1) framing is *already* implicit in
   Ch 2 §5 and Ch 5 — would small explicit additions to those
   chapters be cleaner than putting everything in a separate
   appendix? Open.

## Status

The 2D HO bridge is conceptually ready, with the major caveat that
the bridge works in **picture B (2D HO overlay)** rather than in
the canonical quantisation of the wave equation (picture A). Items
adjusted per
[ho-bridge-2d-review.md](ho-bridge-2d-review.md):

- New §"Interpretive status of the bridge" makes the picture-A vs
  picture-B choice explicit and identifies the file as working in
  picture B as an overlay, not a derivation (items 1, 9).
- Convention (m, n) = (w-direction winding, u-direction winding)
  per Ch 2 standardised throughout; ladders ordered (a_w, a_u) and
  joint occupation states written |m, n⟩ consistently (item 5).
- Translation table split the KK-gauge row into field (h_μw ↔ B_μ)
  and charge (p_w ↔ U(1) generator eigenvalue) (item 3); the
  ambiguous "Sum...squared" row replaced with explicit Pythagorean
  *sum-of-squares* language vs HO additive (item 4); a note added
  on the ±n / R_u-symmetrisation features of picture A that do not
  transfer cleanly into picture B.
- §"Symmetry payoffs" rewritten as overlay-conditional: U(1) ×
  U(1) is robust in both pictures; continuous SU(2) at ε = 1
  belongs to picture B only, while picture A carries only discrete
  D_4 at the same point. The "real prize" framing has been
  downgraded to match the same posture
  [higher-order-charges.md](higher-order-charges.md) takes toward
  SU(3) → color (structural shadow, not derived symmetry)
  (items 2, 9).
- §"Coherent-state knots" reconciled with Open Question 3:
  localisation is automatic; knot-trajectory tracking is a
  separate, open construction (item 6).
- §"Hypothesis A" reworded to make w's compact status explicit
  ("now treated as kinematic" replaced with KK-momentum framing)
  (item 7).
- §"Hypothesis B" headline augmented to include the Ch 4
  synchronisation criterion as the sufficient condition (necessary
  + sufficient now both present) (item 8).
- Open Question 2 updated to the sharper picture-faithfulness
  question that is now the file's chief open issue.

Three things should be settled before an appendix is written:

- **Resolution of OQ 2** (whether picture B is faithful or just
  algebraic overlay) — the most consequential.
- **Decision on coherent-state knot framing's scope** (localisation
  alone, or also knot-trajectory tracking once constructed).
- **Decision on whether any of this lands as back-edits to existing
  chapters** rather than as a new appendix.

Hypotheses A and B (incremental mass, charge requires prior mass)
remain valid **pedagogical re-narrations** of derivations that
Chapter 2 and Chapter 4 already contain. They are appendix-grade
if treated honestly as narration; they should not be presented as
new derivations producing new content.
