# 2D harmonic-oscillator foundation for metric-charge

**Status:** Foundation document for downstream HO-based modeling.
Not chapter-grade. See [work/README.md](README.md) for context.

## Scope and purpose

Establish a solid foundation for using harmonic-oscillator (HO)
algebra to model structure on metric-charge's 2D-compact sheet.
The need is forward-looking: downstream projects (spin,
weak-isospin and color candidates, modulated-clover work,
ma-domain extensions, metric-binding) are likely to lean on
operator-algebra structure — ladder operators, Fock space,
coherent states, continuous symmetries like SU(2) and SU(3) at
isotropy — that the wave-equation-on-T² picture of
[Chapter 2 §3](../02-modes-on-a-sheet.md) does not by itself
provide.

This file makes the foundation explicit by:

- separating cleanly what is **proven** (concrete results derived
  from metric-charge's actual physics) from what is **borrowed
  from a different physical model** as a modeling tool,
- stating the structural relationship between the wave-equation-
  on-T² picture (which *is* metric-charge's physics) and the 2D
  harmonic oscillator (a separate physical system whose algebra
  we use as a modeling tool),
- giving a principled criterion for when borrowing the 2D HO's
  algebra is appropriate, and when it is not.

**This is not a quantization of the wave equation.** The
canonical quantization of metric-charge's actual physics is the
QFT-on-T² picture (one ladder per mode), which is well-defined
and unambiguous and which this file refers to as **picture A**.
The 2D harmonic oscillator (**picture B**) is a *different*
physical system. The two systems share only their one-quantum-
per-mode spectrum labels; they differ in Hamiltonian, mode
functions, multi-quantum Fock structure, and continuous-symmetry
algebras.

The file uses picture B as a modeling tool because picture A
does not carry the algebraic structures (continuous SU(2)/SU(3),
coherent-state localization, occupation-number labelings) that
downstream modeling targets need to talk about. This is a
principled choice when the target is one of B's structural
features, *not* a claim that B is the physics.

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

## Two physical systems, one shared label structure

The basic structural fact, plainly: **the wave equation on T²
and the 2D harmonic oscillator are different physical systems.**
Each has its own canonical quantization. They share the same
integer-pair labels (m, n) at the one-quantum spectrum level,
but they differ in essentially everything else.

**Picture A — the wave equation on T² (Chapter 2's actual
physics).**

- Hamiltonian: the relativistic wave operator on the compact
  T², H² = c²(−Δ + m²).
- Mode functions: plane waves e^{i(m w/R_w + n u/R_u)} —
  periodic, delocalized over the sheet.
- Spectrum at rest: m² ∝ (m/R_w)² + (n/R_u)² (Pythagorean).
- Boundary condition: periodicity on each compact direction.
- Fock space: one ladder (a_{m,n}, a†_{m,n}) per integer
  winding pair (m, n) ∈ ℤ²; the full Fock space is the tensor
  product over all (m, n).
- Continuous symmetries at R_u = R_w: U(1) × U(1) of compact-
  direction translations plus the discrete dihedral group D_4
  acting on the (m, n) integer lattice. **No continuous SU(2).**

**Picture B — the 2D harmonic oscillator (a separate physical
system).**

- Hamiltonian: quadratic confining potential
  H = (p_w² + ω_w² w²)/2 + (p_u² + ω_u² u²)/2.
- Mode functions: Hermite functions on ℝ² — decaying at
  infinity, not periodic.
- Spectrum: E = ℏω_w(m + 1/2) + ℏω_u(n + 1/2) (linear additive).
- Boundary condition: square-integrability on ℝ²; no periodicity.
- Fock space: two ladders (a_w, a_u), one per oscillator;
  the Fock space is the tensor product of two single-oscillator
  Fock spaces.
- Continuous symmetries at ω_u = ω_w: U(2) = U(1) × SU(2),
  continuous mixing of the two ladder operators.

The two pictures **match at the one-quantum-per-mode label
level** — both have one basis state for each integer pair (m, n).
They **differ in everything else**: Hamiltonian, mode-function
geometry, multi-quantum Fock structure, spectrum shape
(Pythagorean vs additive), and continuous symmetry algebra
(D_4 vs SU(2) at isotropy).

**Picture A is metric-charge's physics, unambiguously.** The
mass formula, the closure condition, the KK gauge identification
in Ch 5 — all derived in picture A. There is no question about
which picture is the canonical quantization. It is A. Picture B
is a separate physical system, not a different reading of A.

## Why this file uses picture B as a modeling tool

Picture A is the physics. But picture A carries only the
discrete dihedral group D_4 at R_u = R_w. It does not carry
continuous SU(2), continuous SU(3), or any of the continuous-
symmetry structures that downstream projects want to model:
spin (SU(2)), weak isospin (SU(2)), color (SU(3)), and any
higher-rank candidate. The integer (m, n) lattice's symmetry is
discrete, full stop.

This is not a defect of picture A; it is what canonical
quantization of a wave equation on a compact manifold actually
delivers. If the framework wants to model continuous-symmetry
structures, it needs to look at a model that has continuous
symmetries by construction. Picture B is such a model.

**Principle for borrowing from picture B.** When the modeling
target is a structure that picture B carries and picture A does
not (continuous SU(2)/SU(3), coherent-state semiclassics,
occupation-number labeling beyond one-quantum), this file uses
picture B's algebra as the model. The borrowing is principled
because:

- Picture B is the smallest structurally well-defined system
  that carries the target structure.
- Picture B agrees with picture A at the one-quantum-per-mode
  level (so the borrowing connects to A's spectrum where the
  spectrum is what matters).
- Picture A is *not* an alternative source for the target — A
  does not carry continuous internal symmetries at all, so the
  choice between A and B for these targets isn't a contest.

**Limit on the borrowing.** When picture A's specific
predictions matter — spectrum, lattice symmetries, multi-quantum
Fock structure, the closure condition, the KK gauge
identification — this file defers to A. The borrowing does not
transfer to those predictions. Where A and B disagree (e.g.,
discrete D_4 vs continuous SU(2) at isotropy), A wins as
statements about metric-charge's actual physics. But A typically
doesn't *speak to* the modeling target in the first place,
which is exactly why B is being used.

**Why this is principled and not arbitrary.** The choice is not
"pick B because it's easier" or "pick the picture we prefer."
It is "pick the model that carries the structure being
modeled." If a downstream target lands in a structure A
carries, the file would not borrow from B for it. Concretely:
the U(1) × U(1) charge structure is a property of *both* A and
B (it lives in the translation symmetry of the compact
directions, which exists in both systems), so the U(1) × U(1)
story is robust and does not require any borrowing. The SU(2)
at isotropy is a property of B only; using it as a model is
principled when the downstream target is something SU(2)
naturally describes (e.g., spin), and the user of the model has
to know they are borrowing from B's algebra, not deriving from
A's wave equation.

**Same status as effective field theory or Lie-algebra methods.**
This is structurally the same move that effective field theories
make relative to underlying QFTs, that Lie-algebra methods make
in condensed-matter physics, and that the simple harmonic
oscillator approximation makes near the equilibrium of any
non-trivial potential. The model is not the underlying physics;
the model is what carries the structure being investigated.
Naming the model and its relationship to the underlying physics
is the work this section does.

## What this file establishes

Concrete results, separated from borrowed-from-B modeling
claims, so a downstream project knows what to cite as derived
vs what to cite as borrowed.

**Established (derived from picture A's physics):**

1. **Pythagorean mass combination.** The 2D rest mass is
   m² = m_u² + m_w² where m_u, m_w are the single-direction
   masses (Ch 2 §3). The two windings contribute symmetrically
   in quadrature.

2. **Hypothesis A equivalence.** The same Pythagorean answer is
   derived sequentially (treat m_u as a 1D rest mass, then add
   the second compact direction's KK momentum p_w). The
   sequential and joint-quantization routes give identical
   results — a proof of equivalence between two presentations
   of the same Ch 2 §3 result. *Proven in §"Hypothesis A" below.*

3. **Hypothesis B → necessary half of closure.** "Charge requires
   non-trivial winding in both compact directions" is the
   necessary condition of Ch 4's closure rule. The sufficient
   condition is the m | n synchronization that Ch 4 develops
   within the both-nonzero family. *Mapped in §"Hypothesis B"
   below.*

4. **U(1) × U(1) charge structure is robust in both pictures.**
   Each compact direction's phase rotation is a Noether symmetry;
   the two associated conserved charges are p_w and p_u. This is
   the structure Ch 2 §5 and Ch 5 already identify as KK charge.
   Available without borrowing from picture B.

5. **Picture A's lattice symmetry at R_u = R_w is discrete D_4
   on the integer (m, n) plane.** Mathematical fact about
   n² + m². Continuous SO(2) does not preserve the integer
   lattice and is not a symmetry of the actual mode spectrum.

6. **Picture B's algebra at ω_u = ω_w carries continuous
   SU(2).** Mathematical fact about the 2D harmonic oscillator
   with equal frequencies. *Property of picture B as a separate
   physical system, not of the wave equation.*

7. **Standard 2D-HO coherent states follow ellipses, not
   (m, n) torus knots.** Mathematical fact about coherent-state
   dynamics in picture B. Knot-trajectory tracking, if wanted,
   requires a construction beyond standard 2D-HO coherent
   states.

**Borrowed from picture B as a modeling tool:**

1. **Ladder-operator and Fock-space algebra is available for
   modeling excitation numbers and bosonic statistics on
   metric-charge's mode spectrum.** Picture A and picture B
   share this at the one-quantum-per-mode level; borrowing it
   is uncontroversial.

2. **Coherent-state localization on T² is available as a model
   for "where the wavepacket is."** Borrowed from picture B.
   The localization construction transfers to picture A at the
   level of Gaussian wavepacket states, but the
   knot-trajectory-tracking extension does not (see established
   result 7).

3. **Continuous SU(2) at ω_u = ω_w is available as a model for
   downstream continuous-symmetry targets** (candidate for spin,
   weak isospin, color via the higher-dimension extension).
   This is the file's most consequential borrowing. It is
   borrowed from picture B; it is *not* a property of the wave
   equation on T² (see established result 5). Downstream
   projects using this should cite it as a model whose source
   is picture B, not as a derived symmetry of metric-charge's
   geometry.

The U(1) × U(1) story (established result 4) lives in both
pictures and is the only continuous internal symmetry
metric-charge derives from picture A alone. Anything richer is
borrowed from picture B.

## The 2D HO translation

This section spells out the structural map between picture A's
mode spectrum and picture B's algebra. The map is what makes
"borrow from B's algebra" a concrete operation rather than a
slogan: it tells a downstream user which object in B corresponds
to which Ch 2 quantity, and where the correspondence breaks down.

Borrowing from picture B's algebra means working with two
independent ladders, one per compact direction:

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

| Picture A (Chapter 2's actual physics) | Picture B (the modeling tool we borrow from) |
|---|---|
| Mode function e^{i(m w/R_w + n u/R_u)} | Number eigenstate \|m, n⟩ |
| Winding pair (m, n) = (w, u) from periodicity on both cycles | Joint occupation numbers (m, n) |
| Compact momenta p_w = ℏm/R_w, p_u = ℏn/R_u | Canonical momenta of the two ladders |
| Rest mass m² = m_u² + m_w² (Pythagorean *sum of squares* of two single-direction rest masses) | Spectrum *labels* match at one-quantum-per-mode level; the HO additive sum ℏω_w m + ℏω_u n is *not* the metric-charge mass formula and should not be expected to drop out |
| Off-diagonal metric h_μw on extended spacetime | KK gauge *field* B_μ — a 1-form on extended spacetime that the dimensional reduction reads off h_μw ([Ch 5](../05-metric-self-consistency.md)) |
| Compact-direction momentum p_w | Conserved U(1) *charge*, eigenvalue of the w-tower generator; couples to B_μ |

The structural shift from 1D to 2D is the appearance of a
**second ladder**. Everything that was a single-tower story in
metric-mass becomes a joint-tower story here.

**Where the translation does not carry across.** Two features of
picture A do not have clean counterparts in picture B's bare
algebra; both should be cited explicitly by any downstream user:

- **The ±n traversal-orientation distinction (Ch 2 §5.1).** In
  picture A each (m, n) and (m, −n) is a separate mode with its
  own ladder. In picture B the u-ladder occupation n is non-
  negative, and sign-of-winding information would have to be
  carried by an additional orientation label not present in the
  bare 2D HO. Constructions that depend on the ±n distinction
  — including R_u-symmetrization, R_J-symmetrization, and the
  matter/antimatter axis of Ch 5–6 — belong naturally to picture
  A, not to picture B's bare algebra.

- **The energy formula.** Picture B's spectrum is linear
  additive: E = ℏω_w(m + 1/2) + ℏω_u(n + 1/2). Picture A's
  rest-mass formula is Pythagorean: m² = m_u² + m_w². These
  differ because the two systems have different Hamiltonians
  (quadratic confining potential vs relativistic wave on a
  compact manifold), and the difference is not a small
  correction. The translation is *spectrum-label-matching*, not
  *energy-formula-matching*. Any downstream use must take its
  energy formula from picture A (the actual physics), not from
  picture B's HO additive sum.

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

**Conclusion (this is established result 2 in the list above).**
The incremental reading is a **valid sequential re-derivation** of
the same Pythagorean answer the symmetric joint quantization
gives. The two routes have been shown to produce identical results.
This is a real proof — not a hypothesis being tested but a
demonstrated equivalence between two presentations of the same
Ch 2 §3 formula.

What the incremental reading does *not* establish is a multi-level
mechanism in which the second-direction mass functionally depends
on the first. The mass formula remains symmetric in the two
windings; the sequential narration is a way of arriving at the
symmetric formula, not evidence for an asymmetric mechanism. Its
pedagogical value is intact; its derivational value is the
equivalence proof.

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

**Conclusion (this is established result 3 in the list above).**
The hypothesis maps cleanly onto the necessary half of Ch 4's
closure condition; the sufficient half (m | n synchronization) is
*not* captured by the "prior mass" reading and remains Ch 4's
content. The hypothesis is a useful sequential narration of the
necessary condition; it does not introduce a new mechanism, and
it does not displace Ch 4's synchronization criterion.

## Continuous internal symmetries — A-native vs B-borrowed

This section pulls together what continuous internal symmetries
the two pictures actually carry, in one place, so a downstream
project knows which it can derive from picture A and which it has
to borrow from picture B.

**U(1) × U(1) is A-native.** Each compact direction's phase
rotation is a Noether symmetry of the wave equation on T²; the
two associated conserved charges are p_w and p_u. The KK
identification of compact momenta with charge that Ch 2 §5 and
Ch 5 already use is *this* U(1) × U(1). It is realized in
*both* pictures because it lives in the translation symmetry of
the compact directions, which both systems have. **Downstream
projects using U(1) × U(1) are deriving from A, not borrowing
from B.**

**Continuous SU(2) at ω_u = ω_w is B-borrowed only.** In the 2D
harmonic oscillator at equal frequencies, the Hamiltonian is
invariant under arbitrary unitary mixing of the two ladder
operators (a_w, a_u) → U·(a_w, a_u). The unitary group is
U(2) = U(1) × SU(2); the SU(2)/U(1) generators act on B's
ladder operators. This continuous symmetry exists in B by
construction.

**Picture A's actual symmetry at R_u = R_w is discrete dihedral
D_4.** The wave-equation spectrum m² ∝ m² + n² is invariant
under the integer-lattice symmetries of the (m, n) plane: 90°
rotations, reflections, and overall sign flip. A continuous
SO(2) acting on (m, n) as real coordinates does *not* preserve
the integer lattice — irrational rotations take integer modes
to non-existent intermediate values — so SO(2), let alone the
larger SU(2), is *not* a symmetry of A's actual mode spectrum.

There is no honest ambiguity here. Picture A does not have
continuous SU(2) at R_u = R_w. Picture B does have continuous
SU(2) at ω_u = ω_w. **Anyone wanting a continuous SU(2)
structure on metric-charge's spectrum is borrowing from B's
algebra, not deriving from A's wave equation.**

| | Picture A (the physics) | Picture B (the modeling tool) |
|---|---|---|
| **At generic anisotropy** | U(1) × U(1) | U(1) × U(1) |
| **At isotropy** | U(1) × U(1) plus discrete D_4 lattice symmetry | U(1) × U(1) × SU(2) |
| **A-native or B-borrowed?** | U(1) × U(1) is A-native; D_4 is A-native | The extra continuous SU(2) at isotropy is B-borrowed |

[Chapter 7](../07-aspect-ratio-and-character.md) currently
treats ε = 1 as the boundary between thin-sheet and fat-sheet
regimes. Both pictures agree that ε = 1 is structurally
distinguished — it is the symmetry-enhancement point in both —
but they disagree on the *kind* of enhancement: a finite-group
enhancement in A, a Lie-group enhancement in B.

**Use of the borrowed SU(2) by downstream projects.** When a
downstream project wants to model a candidate target as SU(2)
structure (e.g., one of the two MaSt readings of spin-1/2, or
a candidate for weak isospin), the principled stance is:

- The SU(2) algebra is borrowed from picture B as a modeling
  tool.
- The downstream model inherits B's structural features
  (continuous mixing of two ladder modes, two-state SU(2)
  representations, etc.).
- The downstream model does *not* inherit a claim that the
  wave equation on T² has continuous SU(2). It doesn't.
- If the downstream model wants an A-native source for SU(2)
  instead — e.g., from a spin structure on the compact
  manifold, or from a half-twist double cover (as in the
  modulated-clover work) — that is a different construction
  and the borrowing route does not preclude or substitute for
  it.

The framework's existing posture, mirrored in
[higher-order-charges.md](higher-order-charges.md)'s treatment
of SU(3) → color, treats isotropy-enhanced continuous
symmetries as **borrowed algebraic models** that serve as
calculational and pedagogical scaffolding but do not stand in
for the corresponding gauge or geometric structure of physics.
The 2D SU(2) story here is the same status one rank lower.

## Coherent-state localization (and what it doesn't give)

A single (m, n) mode is delocalized over the entire sheet.
Picture B's **coherent states** |α_w, α_u⟩ — joint eigenstates
of the lowering operators (a_w, a_u) — are minimum-uncertainty
Gaussian wavepackets that trace classical trajectories without
spreading. Borrowing this machinery from picture B gives
metric-charge a well-defined "where the wavepacket is" reading,
replacing plane-wave delocalization with localized blobs.

This borrowing is well-grounded: bosonic coherent-state
machinery transfers cleanly between systems that share a Fock-
space structure at the one-quantum-per-mode level, which A and
B do. *This is one of the cleaner uses of the borrowing.*

**What the borrowing does *not* give automatically.** The
classical trajectory of a standard 2D-HO coherent state is an
**ellipse** in (w, u) at frequencies ω_w and ω_u — *not* a
T(m, n) torus knot. To produce a wavepacket that follows the
torus-knot trajectory, the construction has to go beyond the
standard 2D-HO coherent state: e.g., a coherent state built
from the (m, n)-momentum eigenmode itself, which is *not* what
the standard a_w, a_u machinery produces. The construction also
depends on which classical orbit is wanted.

So the picture-B borrowing covers wavepacket *localization*
without controversy; *knot-trajectory tracking* is an additional
construction that does not fall out of the borrowing and would
have to be built separately (open question 1 below).

[Chapter 3](../03-knots-on-the-torus.md) currently reframes the
(m, n) modes geometrically as knots traversing the sheet, built
on plane-wave mode functions. The coherent-state borrowing is
useful for the localization half of what Ch 3 needs; the
knot-trajectory half is a separate open construction, not a
direct consequence of the borrowing.

## Open questions

(The picture-faithfulness question that previously sat here has
been settled by the §"Two physical systems" framing: picture A is
the canonical quantization; picture B is a different physical
system whose algebra is borrowed for specific modeling targets.
There is no remaining ambiguity to investigate. What remains
open is more concrete.)

1. **Knot-trajectory tracking via coherent states.** Standard
   2D-HO coherent states give wavepacket localization but follow
   *elliptical* classical orbits, not T(m, n) torus knots. What
   construction is needed for a wavepacket that follows the
   (m, n) torus-knot trajectory? Worth working out for any
   downstream project that wants particles-as-coherent-orbits
   semantics, but not blocking for borrowings that only need
   localization.

2. **B-borrowed vs A-native sources of SU(2).** When a downstream
   target wants SU(2) structure (e.g., one of the two MaSt
   readings of spin-1/2 noted in
   [angular-momentum-as-mass.md](angular-momentum-as-mass.md)),
   there are two sources to consider:
   - Borrow from picture B's algebra at isotropy (this file's
     route).
   - Derive A-native from a spin structure on the compact
     manifold, a half-twist double cover (as in the
     modulated-clover work), or another A-side mechanism.

   These are different constructions; the borrowing route does
   not preclude the A-native route, and the A-native route does
   not preclude the borrowing route. Which is the right source
   depends on what downstream physics the SU(2) is being asked
   to model. The framework would benefit from picking one (or
   both, with their domains of application) before any specific
   spin or weak-isospin work commits.

3. **What pieces (if any) belong as back-edits to existing
   chapters?** The U(1) × U(1) framing is *already* implicit in
   Ch 2 §5 and Ch 5 — would small explicit additions to those
   chapters be cleaner than putting everything in a separate
   appendix? Open and deferred until a downstream user starts
   leaning on the foundation in earnest.

## Status

The file is reframed as a **foundation document** for downstream
HO-based modeling, not as a hypothesis-testing bridge. The
picture-faithfulness question that earlier drafts treated as the
chief open issue has been settled by being stated plainly:
**picture A is metric-charge's actual physics; picture B is a
separate physical system whose algebra is borrowed as a modeling
tool when the target is one of B's structural features.**

What the file delivers to a downstream user:

- **A concrete list of established results** (the seven items in
  §"What this file establishes"), derived from picture A's
  physics, that downstream projects can cite without borrowing
  from B.
- **A concrete list of borrowed-from-B claims** (the three items
  in the same section), with picture B identified as the source
  and the limits of the borrowing stated.
- **A principled criterion** (§"Why this file uses picture B as
  a modeling tool") for when borrowing from B is appropriate
  and when picture A's predictions take precedence. The
  criterion: borrow from B when the modeling target is one of
  B's structural features (continuous internal symmetries,
  coherent-state semantics, occupation-number labeling beyond
  one-quantum); defer to A when picture A's specific
  predictions matter (spectrum, lattice symmetries,
  multi-quantum Fock structure, closure condition, KK gauge
  identification).
- **A clean translation table** between picture A's mode
  spectrum and picture B's algebra, with explicit notes on
  where the translation breaks down (±n orientation, energy
  formula) so a downstream user is not misled.
- **An A-native vs B-borrowed split for continuous internal
  symmetries** (§"Continuous internal symmetries"). U(1) × U(1)
  is A-native and robust; continuous SU(2) at isotropy is
  B-borrowed only. Anyone modeling spin, weak isospin, or
  related candidates as SU(2) structure is borrowing from B,
  and an A-native alternative source (spin structure, half-twist
  double cover) is a separate construction to be considered on
  its own merits.

**What this file is not.** It is not a quantization of the wave
equation (that's picture A, established in Ch 2). It is not a
claim that picture B is the physics (it isn't). It is not a
hypothesis being tested (the hypothesis-testing parts of earlier
drafts have settled into the established-results vs
borrowed-claims split). It is the foundation a downstream
HO-based modeling effort can stand on with the relationship to
metric-charge's actual physics made explicit.

**Edit history.** Items adjusted per
[ho-bridge-2d-review.md](ho-bridge-2d-review.md) and the
follow-up clarification that the file should pass over picture A
on the principled basis that A does not carry the target
structures, rather than on the arbitrary basis of preferring B's
algebra:

- Reframed as a foundation document, not a hypothesis-testing
  bridge.
- §"Two physical systems" replaces the prior "Interpretive
  status of the bridge"; the picture-faithfulness question is
  settled by acknowledging that A and B are genuinely different
  physical systems and the file is using B's algebra as a
  modeling tool, not as a quantization claim.
- §"Why this file uses picture B as a modeling tool" gives the
  principled criterion for the borrowing.
- §"What this file establishes" separates concrete results from
  borrowed claims.
- §"Continuous internal symmetries" replaces "Symmetry payoffs",
  with the A-native vs B-borrowed split made explicit.
- §"Coherent-state localization" reframed: borrowing for
  localization is uncontroversial; knot-trajectory tracking is
  a separate construction.
- Open questions reduced to the genuinely open items
  (knot-trajectory construction, A-native vs B-borrowed SU(2)
  source choice, chapter back-edits decision); the former
  picture-faithfulness OQ removed as settled.
- Convention (m, n) = (w-direction winding, u-direction
  winding), ladders ordered (a_w, a_u), joint occupation
  states |m, n⟩ — standardized throughout.
- Hypothesis A and B sections retain their math and now point
  explicitly at their corresponding established-result numbers.

Earlier rounds of edits (per the original review's eight items —
notation overload, rotational-energy gloss, gauge field/charge
distinction, etc.) remain in place; this pass restructures the
file's framing without revisiting them.
