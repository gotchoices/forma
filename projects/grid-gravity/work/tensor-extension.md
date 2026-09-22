# The dynamic sector — a dictionary to the metric, and what a per-link memory does and does not give

**Status:** Derivation (paper work, with a symbolic check). First pass at the
project's main open task ([STATUS.md](STATUS.md)): the single scalar deflection of
mechanism 3 reproduces the *static* weak field, but gravitational waves are
observed to be tensor and moving masses drag frames. Question asked: if each
link kept its **own** memory, would the link loadings form a tensor carrier?

**Outcome.** (1) An exact dictionary between the lattice's loadings and the metric
of general relativity — under which mechanism 3's posits P6 and P7 turn out to be
*general relativity's static solution, transcribed*. (2) A clean **negative** for
the naive per-link memory. (3) The feeding rule that *does* reproduce the
linearized field equations. (4) A sharper statement of what is still missing: not
more degrees of freedom, but a **local symmetry**.

Grades: **[rigorous]** (algebra, checked symbolically), **[standard]** (textbook
general relativity), **[reading]**, **[open]**.

---

## 1. The dictionary [rigorous]

Write the metric as flat plus a small perturbation h. For a wave ψ on that
background the Lagrangian is −½√(−g)·g^{μν}∂_μψ∂_νψ, and the compact direction
adds −½√(−g)(∂_cψ)². Expanding to first order and reading off what multiplies
each square gives the lattice quantities directly. Two equivalent ways of writing
it matter, related by multiplying the whole Lagrangian by a common factor (which
changes no ray, only amplitudes and reflection):

| lattice quantity | "as it stands" | **with the compact loop unloaded** (mechanism 3's frame) |
|---|---|---|
| node inertia (slows everything through the node) | h̄₀₀ = h₀₀ + ½·trace | **h₀₀** |
| compliance of a space link along a | h̄ₐₐ = hₐₐ − ½·trace | **hₐₐ** |
| compact links | stiffened by ½·trace | **untouched** |
| links along face diagonals (absent on a cubic lattice) | h̄ₐ_b | hₐ_b |
| a *non-reciprocal* element acting on every wave (absent so far) | h̄₀ₐ | h₀ₐ — frame-dragging |

(trace = −h₀₀ + Σhₐₐ; the bar is the usual "trace-reversed" perturbation.) So:
**a node's loading is the time–time component of the metric perturbation, and a
link's loading is the space–space component along that link.** Loading the node
slows clocks; loading the links as well slows light further. The lattice has
always had the slots of a symmetric tensor; mechanism 3 filled them all from one
number.

## 2. General relativity, said in lattice words [standard + rigorous]

With U = GM/r the Newtonian potential (positive), the linearized solutions of
general relativity read, in the unloaded-compact frame:

| source | node | link along x | links along y, z | compact loop |
|---|---|---|---|---|
| a mass at rest | 2U | 2U | 2U | untouched |
| a beam of light along x | 4U | 4U | **0** | untouched |
| a gravitational wave along z ("plus" polarization) | 0 | +s | y: −s, z: 0 | untouched |

**The first row is mechanism 3's posits P6 and P7, exactly**: nodes and space
links loaded equally, the compact loop loaded by neither. They were introduced as
what it takes to get the full light bending; they are what general relativity's
static field *is*, on a lattice. In particular P7 — "a clock's compact loop is
loaded once" — is the lattice statement that four-dimensional gravity does not
act on the compact direction (the compact size is not a gravitational degree of
freedom). That does not derive P7, but it replaces an odd-looking premise with a
familiar one.

The other two rows show where a **single scalar** deflection departs from general
relativity:

- For a source whose stress is not isotropic — a light beam, a fast-moving body,
  a body under pressure — general relativity loads the node and the links *along
  the flow*, and leaves the transverse links alone. One scalar loads all links
  alike. The time–time part (clocks, Newtonian pull, "light counts double") is the
  same; the space–space part is not.
- A gravitational wave lives **only** in the links, with opposite signs on two
  perpendicular directions, and **not** in the node. One scalar has no such
  configuration. (The second, "cross" polarization needs links along face
  diagonals, which a cubic lattice lacks; other lattices have them.)

So the tensor carrier is not exotic on the lattice: it is *per-direction* link
loading. The question is what feeds it.

## 3. The naive per-link memory fails [rigorous]

Give each link its own memory, let it propagate as an ordinary wave, and let it be
fed — as the action of step 5c′ dictates when memories are independent — by the
energy *in that member*: the node's memory by the node-rate energy, a link's by
the tension energy along that link.

A mass at rest has no tension along any space link: its energy sits in the node
rate and in the compact circulation. So its space links are never fed. Only the
node is loaded, and the result is **γ = 0 — half the observed light bending**,
the same failure as step 1's node-only rule. Mechanism 3 escaped this by
*slaving* the links to the node's deflection (requirement R5); cut them loose and
the static sector breaks. **Independent, self-fed link memories are not the
answer.**

## 4. The feeding rule that works [rigorous + reading]

General relativity's linearized field equations, in these variables, are plain
wave equations for each loading — but the source of each is not the energy in
that member. It is

<!-- node:  (rate energy) − ½(rest energy);   link along a:  (tension energy along a) + ½(rest energy) -->
$$
\text{node:}\;\; \dot\psi^2 - \tfrac12(\partial_c\psi)^2 ,
\qquad
\text{link along } a:\;\; (\partial_a\psi)^2 + \tfrac12(\partial_c\psi)^2 ,
$$

where (∂_cψ)² is the energy of the compact circulation — the **rest energy**.
Check: a mass at rest has rate energy = rest energy = ρ, so node and every link
are fed ½ρ — equally, as row one of §2 requires. A light beam along x has no rest
energy: node ρ, x-link ρ, transverse links nothing — row two.

In words: **each space link is fed by the flow of energy along it, plus an equal
share of the rest energy at its node; the node is fed by its rate energy less
that share.** The second half has a natural reading: the compact circulation is
trapped radiation, and trapped radiation presses equally on everything that
confines it — every space link at the node, whatever its direction. (This is the
radiation-pressure picture of the mechanism note's §8, now in the role it fits:
not stretching the compact loop, but loading the links around it.) **[reading]**

With this rule, requirement R5 (equal loading) is no longer a posit about
slaving: it is what a *rest mass* produces, and other sources produce other
patterns.

## 5. What is still missing: a symmetry, not a degree of freedom [standard + open]

Suppose §4's rule is adopted and every loading propagates as its own
positive-energy wave. The static sector and the field equations are then right.
The **radiated energy** is not.

In general relativity only two combinations radiate — the two transverse,
trace-free polarizations. The other components (the node's loading, the trace of
the links', the frame-dragging part) obey wave equations too in a convenient
gauge, but they carry no energy away: they are tied to the source by constraints,
which exist because the theory has a **local symmetry** — the freedom to re-label
points and re-time clocks independently at every place. A lattice in which every
memory is an honest, independent, positive-energy wave has no such symmetry, and
an orbiting pair would radiate through the node's loading as well. Binary pulsars
fix the radiated power to a fraction of a percent of the two-polarization value,
so that extra radiation is excluded.

This is a known and strong result: a massless tensor field coupled to conserved
stress-energy, with positive radiated energy, *must* have that local symmetry,
and the symmetry fixes the dynamics to be Einstein's. So the dynamic sector does
not need more stores. It needs the lattice's existing global freedoms — the tick
is only bookkeeping; a uniform deflection is unobservable — to hold **locally**:
re-timing one node, or re-labelling one neighbourhood, must change nothing
physical. Axiom A4 does precisely this for phases, and Maxwell's equations follow
from it; the gravitational counterpart is the same move for times and labels.
Whether GRID's lattice can carry it is **open**, and it is the point where the
statistical (Jacobson) account — which delivers Einstein's equations whole —
acts as the guide to what the mechanical account must become.

Also open: the frame-dragging component needs a non-reciprocal element that acts
on *every* wave and is fed by momentum flow — the universal counterpart of the
winding-selective element in the [EM slot](em-slot.md).

## 6. Where this leaves mechanism 3

- Its static sector is general relativity's, transcribed (§2, row one).
- Its single scalar is the special case of §4's rule for sources that are at rest
  or isotropic; for anisotropic sources the space–space part differs from general
  relativity. No current observation probes that difference directly.
- Its radiation is the part that cannot be patched by adding memories; it needs
  the local symmetry of §5.

## Grades summary

- **[rigorous]** The dictionary (both frames); general relativity's three
  solutions in lattice words; P6 + P7 = the static solution; failure of self-fed
  link memories (γ = 0); the feeding rule of §4.
- **[standard]** Only two polarizations radiate; constraints follow from local
  symmetry; uniqueness of the massless tensor theory.
- **[reading]** Rest energy as trapped radiation pressing equally on the links.
- **[open]** A local re-timing / re-labelling symmetry on the lattice; the
  frame-dragging element; face-diagonal links for the second polarization.
