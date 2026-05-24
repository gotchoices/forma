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

## The 2D HO translation

The u- and w-pieces of the separated wave equation are each 1D simple
harmonic oscillators in the same sense
[metric-mass Ch 9 §2](../../metric-mass/09-harmonic-oscillator-bridge.md)
made explicit for the single-direction case. Promoting to operator
algebra: two independent ladders, one per compact direction:

<!-- [a_u, a_u†] = 1,  [a_w, a_w†] = 1,  [a_u, a_w] = [a_u, a_w†] = 0 -->
$$
[\,a_u,\;a_u^\dagger\,] = 1,
\qquad
[\,a_w,\;a_w^\dagger\,] = 1,
\qquad
[\,a_u,\;a_w\,] = [\,a_u,\;a_w^\dagger\,] = 0
$$

Joint occupation numbers (n, m) label basis states |n, m⟩ on the
tensor-product Fock space.

Translation, line by line:

| Classical wave reading (Chapter 2) | 2D HO reading |
|---|---|
| Mode function e^{i(n u/R_u + m w/R_w)} | Number eigenstate \|n, m⟩ |
| Winding pair (m, n) from periodicity on both cycles | Joint occupation numbers (n, m) |
| Compact momenta p_u = ℏn/R_u, p_w = ℏm/R_w | Canonical momenta of the two ladders |
| Rest mass m² = m_u² + m_w² (Pythagorean) | Sum of two ladder-energy contributions, *squared* |
| KK gauge potential B_μ from h_μw ([Ch 5](../05-metric-self-consistency.md)) | Generator of the w-tower U(1) under dimensional reduction |
| Standing-wave (R_u-symmetrized) particle | Symmetric superposition of ±n number states on the u-tower |

The structural shift from 1D to 2D is the appearance of a **second
ladder**. Everything that was a single-tower story in metric-mass
becomes a joint-tower story here.

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
the rest mass of a 1D-compact particle, then put it in motion along
the (now treated as kinematic) w-direction. The relativistic
dispersion gives

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

**Test against Ch 4.** The closure condition is that **both**
windings be nonzero. Ch 2 §4.2 names (m, 0) and (0, n) "single-axis
modes" that produce mass without observable EM. Ch 4 develops the
m | n synchronization criterion within the both-nonzero family. So:
charge requires non-trivial winding in *both* compact directions.

The hypothesis's "prior mass" reading is one way to narrate the
closure condition: dim 1 winding gives the first ladder a
non-trivial state ("prior mass"), dim 2 winding gives the second
ladder a non-trivial state, and only joint excitation supports the
chirality structure that the closure condition tests.

**Conclusion.** The hypothesis maps cleanly onto the existing
closure condition as a re-narration. It does not introduce a new
mechanism. It does provide an intuitive sequential story —
*build mass first, then add charge by adding a second
winding* — that is appendix-grade pedagogy.

## Symmetry payoffs (the real prize)

**Generic anisotropic case (L_u ≠ L_w): U(1) × U(1).** Each ladder
carries its own phase symmetry; the two associated Noether-conserved
charges are p_u and p_w. The KK identification of compact momenta
with charge that Ch 2 §5 and Ch 5 already use is exactly this
U(1) × U(1).

The two U(1)'s are independent because the spectrum
m² = m_u² + m_w² has no cross term that would couple them at the
free-wave level.

**Isotropic case (L_u = L_w, i.e., ε = 1): SU(2).** When the two
radii are equal, the spectrum m² ∝ n² + m² is degenerate under any
SO(2) rotation of the (n, m) plane and, more strongly, under
arbitrary unitary mixing of the two ladders. The unitary group is
U(2) = U(1) × SU(2); the extra SU(2)/U(1) generators that this
brings are **invisible in the classical wave reading** of Ch 2 and
arise only once the operator-algebra perspective is in place.

[Chapter 7](../07-aspect-ratio-and-character.md) currently treats
ε = 1 as the boundary between thin-sheet and fat-sheet regimes. The
HO reading sharpens this:

> **ε = 1 is a structurally distinguished point — a degeneracy line
> in the spectrum and a symmetry-enhancement line in the operator
> algebra.**

Whether this SU(2) is realized as any framework target (a candidate
for weak isospin? a different internal symmetry? not realized at all
because no physical mechanism enforces ε = 1?) is open and deferred.
The geometric fact that the symmetry appears at ε = 1 is robust.

## Coherent-state knots

A single (m, n) mode is delocalized over the entire sheet. The HO
reading provides **coherent states** |α_u, α_w⟩ that are joint
eigenstates of the lowering operators (a_u, a_w), are
minimum-uncertainty Gaussian wavepackets on T², and trace classical
trajectories without spreading. This is the natural formalism for
talking about a *knot as a localized wavepacket on T²*, rather than
as a plane-wave Fourier mode.

[Chapter 3](../03-knots-on-the-torus.md) currently reframes the
(m, n) modes geometrically as knots traversing the sheet. The
geometry is built on plane-wave mode functions. A coherent-state
upgrade would let "where on T² the knot is" become a well-defined
question rather than a metaphor.

Not developed here. Flagged as a candidate appendix paragraph, or as
a follow-up that may want its own short chapter.

## Open questions before an appendix is writable

1. **Energy-formula reconciliation.** Make the
   additive-vs-Pythagorean distinction explicit so the reader is
   not misled. (Resolved here in principle; needs careful prose.)

2. **What does the ε = 1 SU(2) actually generate geometrically?**
   The unitary mixing a_u ↔ a_w must correspond to some
   transformation of the wrap basis. Is it a continuous rotation of
   the (u, w) coordinate frame? A relabeling of which direction is
   tube vs. ring? Something else? Work this out before writing
   "SU(2) at ε = 1" as a clean appendix claim.

3. **Coherent-state knot dynamics.** What is the equation of motion
   of a coherent-state knot on T²? Does it reduce to closed-orbit
   motion along the (m, n) torus knot? If so, this gives a clean
   "knot as classical orbit, particle as coherent quantum state of
   the orbit" reading. Open whether this stays as an appendix
   paragraph or becomes its own chapter.

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

The 2D HO bridge is conceptually ready. Three things should be
settled before an appendix is written:

- Resolution of open question 2 (geometric content of the ε = 1
  SU(2))
- Decision on coherent-state knot framing's scope (appendix
  paragraph vs. its own chapter)
- Decision on whether any of this lands as back-edits to existing
  chapters rather than as a new appendix

Hypotheses A and B (incremental mass, charge requires prior mass)
are both valid **pedagogical re-narrations** of derivations that
Chapter 2 and Chapter 4 already contain. They are appendix-grade if
treated honestly as narration; they should not be presented as new
derivations producing new content.
