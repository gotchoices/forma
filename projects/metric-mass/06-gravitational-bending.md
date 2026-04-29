# Chapter 6 — Gravitational bending and the ±n cancellation question

[Chapter 4](04-mode-interactions.md) computed that a static ±n
superposition has rest energy 2 m_n c² — twice that of a single
mass mode, not zero. [Chapter 5](05-metric-self-consistency.md)
computed that the off-diagonal metric components sourced by such
a superposition cancel under Einstein's equations, but the
diagonal components (energy density, pressure) double.

The remaining question is gravitational: if mass on M bends
spacetime, does the static ±n superposition also bend twice as
much, or does the off-diagonal cancellation extend to the
gravitational coupling?

This chapter is intentionally short. The answer falls out of a
postulate that standard physics imports without derivation
(Einstein's equations); the chapter's job is to apply the
postulate, note where alternative mechanism programs would
say something different, and move on.

---

## 1. Why this chapter is brief

Standard general relativity treats Einstein's equations as a
postulate:

<!-- G_μν = (8πG/c⁴) T_μν -->
$$
G_{\mu\nu} = \frac{8\pi G}{c^4}\,T_{\mu\nu}
$$

The equation says energy and stress (T_μν) source curvature
(G_μν). It does not tell us *why* energy curves spacetime, only
that it does. There is no underlying mechanism in GR — energy
curving spacetime is the foundational fact, not a derived
consequence.

This means that asking "what bends spacetime, and how?" inside
standard GR has a single answer: T_μν, by Einstein's equations.
There is nothing further to derive. Two implementation choices
(linearized GR vs. Newtonian limit) differ only in their level
of approximation, not in their physics.

Because the result is a known consequence of a known postulate,
this chapter does not re-derive any of the underlying
mechanics. It applies the postulate to our specific
configuration, reports the consequence, and uses the remaining
space to note alternative-mechanism programs that *do* attempt
to derive bending from below — including a programmatic
direction (entropic / thermodynamic gravity) consistent with
the GRID picture.

---

## 2. Two approaches converge to the same result

For a slowly-moving, weakly-gravitating mass distribution, two
standard tools give the bending.

**Newtonian gravity (proxy).** A point mass M sources the
gravitational potential

<!-- Φ(r) = -GM/r -->
$$
\Phi(r) = -\frac{G\,M}{r}
$$

A test particle's acceleration is −∇Φ. Bending of a light
ray's path or a test particle's trajectory follows from
integrating ∇Φ along the path. Bending strength is proportional
to M.

**Linearized GR.** The metric is g_μν = η_μν + h_μν with h
small, sourced by T_μν via the linearized Einstein equation
□ h̄_μν ∝ T_μν. For a slowly-moving mass with rest energy mc²,
the dominant T entry is T_tt = mc² δ³(x) (concentrated source),
and the dominant h entry is h_tt = 2Φ/c² with Φ the Newtonian
potential. Bending of a test particle follows from the geodesic
equation in this metric, which reduces to the Newtonian limit
in the slow-and-weak regime.

Both tools agree at leading order: **bending is proportional
to M = total energy / c²**.

For the project's central question, both tools give the same
answer:

- Single mass mode at rest: M = m_n. Bending strength ∝ m_n.
- Static ±n superposition at rest: M = 2 m_n
  ([Chapter 4 §6–7](04-mode-interactions.md), confirmed by the
  diagonal contribution in [Chapter 5 §7](05-metric-self-consistency.md)).
  Bending strength ∝ 2 m_n.

The bending **doubles** in the ±n superposition. It does not
cancel.

This is the gravitational analog of the inertia result of
Chapter 4: energy adds linearly, gravitational mass = E/c²
also adds linearly, and the cancellation hypothesis fails at
the gravitational level for the same reason it fails at the
inertial level.

---

## 3. Why cancellation does not occur

Cancellation would require gravity to couple to the *sign* of
n (or to some other handedness label) rather than to the total
energy. Standard physics does not allow this:

- The equivalence principle ties gravitational mass to inertial
  mass; both are E/c².
- Energy is a Lorentz scalar (one component of T_μν, but
  positive in any frame for a physical configuration).
- Recent experiments (ALPHA-g at CERN, 2023) directly confirmed
  that antihydrogen falls under gravity the same way ordinary
  hydrogen does, ruling out negative-gravitational-mass models
  for antimatter.

So under standard physics, the configurations that produced
off-diagonal cancellation in Chapter 5 §7 do not carry that
cancellation over to the gravitational coupling. The
*off-diagonal* T entries (T_tu, T_Su) cancel for the
superposition, but the *diagonal* T entries (T_tt, T_uu) double
— and gravity couples to all of T, with the diagonal entries
dominating the bending in the slow-and-weak limit.

This is the resolution of the user-stated question about
"non-destructive inertial elimination": the picture turns out
to be the same at the gravitational level as at the inertial
level. The off-diagonal couplings (which would have been the
KK-style "field-mediated" effects) are cancelled, but the
diagonal energy density — which gravity sees at leading order
— is doubled.

Compactly:

- ±n superposition cancels the *KK-style off-diagonal*
  coupling to mass.
- ±n superposition does *not* cancel the *gravitational*
  (energy-driven) coupling.
- Gravitational bending of a static ±n pair is twice that of a
  single mode.

#### Gravity couples at full strength

Worth observing explicitly, because it sets up the future
charge project: **gravitational coupling has no fractional
factor**. Bending is sourced by the full T_μν, not by an
α-weighted (or otherwise reduced) version of it. Whatever
mass-energy a configuration carries enters Einstein's
equations at full strength.

This contrasts with the electromagnetic channel, where the
fine-structure constant α ≈ 1/137 appears as a coupling
parameter — the strength at which charge couples to the
photon field. In the GRID two-pathway picture
([primers/physics-from-fabric.md](../../primers/physics-from-fabric.md)),
this difference is structural: gravity emerges from the
entropy/heat pathway, where coupling is universal and
proportional to all energy (full strength); electromagnetism
emerges from the causal-information pathway, where the
coupling constant α governs how the carrier of charge
interacts with photons. The two pathways have independent
coupling parameters (G and α), and one is *not* a fraction
of the other.

The implication for the future charge project: when some
fraction of a wave's underlying energy is "promoted" to
charge (with the charge magnitude scaling as α or √α of the
underlying energy, depending on the convention used), the
*full energy* still gravitates at full strength. Charge does
not somehow "remove" energy from the gravitational source;
α is a parameter of the EM channel, not a reduction of the
gravitational source. So when the charge project later asks
what is the gravitational mass of a charged particle, the
answer remains: the full E/c², regardless of how much of E is
present as the charge channel's coupling to the EM field
(which itself contributes to T_μν via its own field energy).

This is the foundation: **gravitational mass = full energy /
c², always**. The charge project will need to handle the
α-coupling separately, on the EM channel side.

---

## 4. Lower-level mechanism candidates

The chapter could end at §3. But it is worth flagging two
directions where the *mechanism* of gravitational bending is
treated as something to be derived rather than imposed.

**Entropic gravity (Verlinde, Jacobson).** Verlinde and Jacobson
(in different ways) have shown that Einstein's equations can
be derived as thermodynamic equations of state on local
horizons — gravity emerges from the requirement that horizon
entropy obey the first law. In this picture, the bending of
spacetime is not a fundamental fact; it is the consequence of
information-theoretic / entropic balance across horizons. Mass
"bends spacetime" because mass shifts the entropy across nearby
information surfaces, and the metric responds to maintain
local thermodynamic balance.

**The GRID picture.** The broader GRID framework
([primers/physics-from-fabric.md](../../primers/physics-from-fabric.md))
proposes two complementary pathways from a discrete substrate
to physics:

- A **causal information network** pathway, which yields
  Maxwell's equations and electromagnetism via local information
  propagation rules.
- An **entropy / heat / temperature** pathway, which yields
  gravity via thermodynamic balance — closely aligned with
  the entropic-gravity programs above.

Under this picture, gravitational bending and electromagnetic
fields would arise from *separate* substrate mechanisms even
though both are encoded in metric structure. Gravity is the
thermodynamic limit of substrate dynamics; electromagnetism is
the causal-information-network limit. Both can be present
simultaneously, but they have different microscopic origins.

For our chapter's question — does ±n cancel gravitational
bending? — the substrate-level mechanism does not change the
answer. The total energy of the configuration is what
gravitates (or what shifts horizon entropy, in the entropic
picture), and that total energy is 2 m_n c² regardless of which
mechanism mediates the bending. The mechanism programs reframe
*why* gravity exists, not *how much* mass at a location
bends spacetime.

This chapter does not commit to any of these mechanism
pictures. It notes that they exist, that they are consistent
with the standard answer (otherwise they would not reproduce
GR in the appropriate limit), and that their existence does
not modify the cancellation question's resolution.

---

## 5. What this chapter does not address

A few questions worth flagging for follow-up work, none of
which are settled here:

- **Whether charge has its own gravitational signature.** Once
  charge enters the picture (in a future project that adds
  the second compact dimension w), the EM field has stress-
  energy and therefore gravitates. The natural question:
  is charge's effect on spacetime entirely accounted for by
  the EM field's stress-energy contribution to T_μν, or is
  there a separate "charge bends spacetime" term? Standard
  physics says the former — charge gravitates only via its
  EM field's energy. But the GRID picture's separation
  between Maxwell-pathway and gravity-pathway suggests it
  may be worth asking the question more carefully, especially
  since the EM and gravity microscopic origins differ in that
  framework. This is out of scope for the current project but
  flagged for the charge project to take up.
- **Whether the entropic / GRID mechanism gives quantitatively
  different predictions.** All known mechanism programs
  (Verlinde, Jacobson, GRID) reproduce GR in the appropriate
  limit. Whether they predict any departure from GR at extreme
  scales (sub-Planckian, near horizons, in strong fields) is
  a research frontier outside this project.
- **Whether the off-diagonal cancellation of ±n in
  [Chapter 5 §7](05-metric-self-consistency.md) has any
  mechanism-level interpretation.** That cancellation was a
  consequence of T_μν being bilinear in n; the off-diagonal
  cancellation is the standard linear-superposition result.
  Whether mechanism programs read this cancellation as
  "physically interesting" (e.g., suggesting a distinct
  thermodynamic interpretation) or as a routine algebraic
  identity is unclear from this project's vantage point.

---

## 6. End of Chapter 6

#### What was confirmed

- Under standard general relativity, gravitational bending is
  proportional to total energy / c². Newtonian and linearized
  GR approaches agree at leading order.
- A static ±n superposition has rest energy 2 m_n c² and
  therefore bends spacetime twice as much as a single mass
  mode.
- The off-diagonal cancellation found in
  [Chapter 5 §7](05-metric-self-consistency.md) does not carry
  over to gravity: gravity couples to the (doubled) diagonal
  energy, not to the (cancelled) off-diagonal stress-energy.

#### What was not derived

- The mechanism by which energy bends spacetime. Standard GR
  takes this as a postulate. Mechanism programs (entropic
  gravity, GRID's two-pathway picture) attempt derivation
  from below; this chapter notes their existence but does not
  develop any of them.

#### What remains open

- Whether the GRID two-pathway picture (Maxwell from causal
  network, gravity from entropy) gives a quantitatively
  different prediction for any aspect of gravitational
  bending in our framework. This project is not equipped to
  evaluate this, and the broader GRID development sits in
  separate studies.
- Whether charge, when introduced in a future project, has a
  spacetime-bending contribution beyond its EM field's
  stress-energy. Standard physics says no; the GRID picture's
  separation of mechanisms makes this worth re-checking when
  the charge project takes up the question.

---

## What's next

For the next chapter and the rest of the project arc, see the
project [README's table of contents](README.md#chapters).
