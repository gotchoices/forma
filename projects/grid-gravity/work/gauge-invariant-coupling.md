# The photon–mass coupling, redone gauge-invariantly — the repair

**Status:** Derivation / repair. Redoes the central calculation of
[mode-coupling-derivation.md](mode-coupling-derivation.md) respecting the
photon's **established** gauge invariance (masslessness), which that note's
own problem (c) invokes but does not enforce. Outcome: the "photon mass ∝ ρ_E"
is a **gauge artifact**; the admissible coupling is a **refractive index**
(kinetic / metric-like), non-dispersive at low ω, sourced by energy — the
structure gravity needs. **Mechanism 2 is not refuted.** What is *not* repaired
is **range (b)**: the index is local/contact, so the original make-or-break
returns — now sharpened to a mediator question with a GRID-native candidate.

Grades: **[established]** (a confirmed forma result), **[derived]**,
**[standard QFT]**, **[open]**.

---

## 1. The fact that settles problems (a) and (c) before any algebra [established]

The n=0 mode is the **gauge connection A_μ⁽⁰⁾** and is **massless by axiom A4**
([grid/photon-from-aleph.md](../../grid/photon-from-aleph.md); Maxwell
reproduced, [grid/sim-maxwell](../../grid/sim-maxwell/)). Masslessness is
**confirmed**, not assumed. Therefore whatever the true ℵ-line nonlinearity is,
it **does not give the photon a mass** — otherwise Maxwell would already be
broken.

So [mode-coupling-derivation.md](mode-coupling-derivation.md) §2's result —
the photon acquires δm² ∝ ρ_E — **cannot be the physical coupling**. It is an
artifact of the operator that note chose: a bare phase potential V(θ) acting on
the gauge mode. That note *noticed* the contradiction (its problem (c): "a
potential on the U(1) phase breaks gauge invariance") but drew the wrong
inference — "mechanism inconsistent → dead." The correct inference runs the
other way: **since gauge invariance is established, the mass-giving operator is
simply not in the theory**, and the admissible coupling must be found among the
operators that keep the photon massless.

## 2. The false dilemma, and the missing third option

The note posed a two-way choice and lost on both horns:

- **potential** V(θ) → nonlinear, gives a detour → **but a photon mass** (dead);
- **mere compactness** (free field on S¹) → gauge-safe → **but linear → no mode
  coupling → no detour** (dead).

The skipped third option is a nonlinearity in the **derivatives** — a
background-dependent coefficient of the photon *kinetic* term:

<!-- L ⊃ -1/4 epsilon(Phi_mass) (∂a_0)^2 -->
$$
\mathcal{L} \supset -\tfrac14\,\varepsilon(\Phi_{\text{mass}})\,(\partial a_0)^2 .
$$

This is (i) **gauge-invariant** — a₀ enters only through ∂a₀, so no mass, the
photon stays massless; and (ii) **nonlinear** — the coefficient ε responds to
the massive background Φ_mass. A background-dependent kinetic coefficient *is* a
refractive index / effective metric: ω = ck/√ε, so n = √ε. This is the
metric/kinetic structure gravity requires, and it is admissible **because** it
is built from ∂a₀ rather than a₀.

Is a *kinetic* (derivative) nonlinearity natural from GRID boundedness? Yes —
and it is the reading forma's congestion notes already use. Boundedness has two
readings:

- a bound on the **value** θ (the compact phase) → a **potential** → the
  mode-coupling note's mass. Gauge-illegitimate for the photon mode.
- a bound on the **rate / bandwidth** (finite bits per tick,
  [local-time.md](local-time.md) Commitment 2, [micro-to-macro.md](micro-to-macro.md)
  R2) → a bound on **∂θ** → a **kinetic** nonlinearity. Gauge-legitimate → an
  index.

The finite-bandwidth reading — the one the whole congestion line is built on —
bounds the *derivative*, not the value. So the gauge-consistent form of GRID
boundedness produces a kinetic nonlinearity → an index, not a photon mass. The
note picked the one reading of boundedness that the established masslessness
forbids.

## 3. The structure is fixed by the Ward identity, operator-independent [standard QFT]

One need not even settle which operator: gauge invariance fixes the *form* of
the answer. Integrating out the massive n≥1 modes gives the photon a self-energy
Σ^{μν}(q), and the Ward identity forces it **transverse**:

<!-- Sigma^{mu nu}(q) = (q^2 g^{mu nu} - q^mu q^nu) Pi(q^2) -->
$$
\Sigma^{\mu\nu}(q) = \big(q^2 g^{\mu\nu} - q^\mu q^\nu\big)\,\Pi(q^2).
$$

A transverse self-energy has **no mass pole**; it renormalizes the kinetic term
into a **dielectric function** ε(q²) = 1 + Π(q²). Reading it off:

- **No mass pole** → photon massless in vacuum, gauge intact — **(c) resolved.**
- **ε − 1 = Π ∝ (density of massive modes) ∝ ρ_E** → the index is sourced by
  **energy** — condition (3), and **(a) resolved**: a *kinetic* (metric-like)
  response, not a mass.
- **Low frequency ω ≪ ω₀**: Π is real and slowly varying → ε ≈ const → n ≈
  const → **non-dispersive**, condition (2).

This is the same Lorentz form n²(ω) = 1 + ρG²/(ω₀²−ω²) that
[energy-coupling.md](energy-coupling.md) already found — now seen to be
**required** by gauge invariance, not one of two options. The mass-term reading
contradicts the Ward identity and is discarded.

**So the three "fatal" problems the refutation rested on: (a) mass-not-index and
(c) gauge-breaking are gauge artifacts and dissolve. Only (b) survives.**

## 4. What is *not* repaired: range (b), untouched and sharpened [open — the real crux]

ε(x) = 1 + Π(x) is **local**: Π(x) ∝ ρ_E(x) is nonzero only where the massive
modes are. This is an ordinary dielectric — the index sits *on* the matter, like
glass, and does not extend into surrounding vacuum. So the refutation's problem
(b) — contact, not 1/r — **survives the repair intact**. It is the same
make-or-break flagged before the refutation (review §4/§5;
[loops-and-range.md](loops-and-range.md) *assumed* a spreading scalar source).

The repair sharpens *why* (b) is hard, and it is worse than "assumed":
integrating out **massive** modes is generically **short-range** (the Uehling
lesson — a massive loop's polarization falls off as e^{−2Mr}), and here the KK
masses are **Planck-scale** ([photon-from-aleph.md](../../grid/photon-from-aleph.md):
m_n = nℏ/R_ℵ). So the massive-mode index is not merely local — it is
Planck-contact. **Range cannot come from the massive modes at all; it requires a
genuinely massless mediator sourced by neutral energy.** The photon won't serve
(neutral matter carries no charge to source it).

**Candidate mediator, GRID-native.** forma already carries the right object: the
scalar zero-mode **A₅⁽⁰⁾ — the radion / dilaton — which is massless and "couples
to ℵ-line dilation"** ([photon-from-aleph.md](../../grid/photon-from-aleph.md)).
A localized mass that shifts the local ℵ-line dilation sources the radion; the
radion, being *massless*, spreads as a static **1/r** field; the shifted radion
sets the local compact size R_ℵ, hence ω₀ ∝ 1/R_ℵ, hence ε — so **δn(r) ∝ 1/r**.
This is a concrete candidate for the mediator [loops-and-range.md](loops-and-range.md)
had to assume — and, because the radion couples to the photon **kinetic** term
(∝ F², via R_ℵ), a radion-mediated index **does bend light** (unlike a Nordström
trace-scalar, which does not). Two open hurdles remain, neither cheap:

1. **Source character.** Does the massive standing wave source the radion as a
   **scalar monopole ∝ energy** (→ 1/r gravity), rather than only locally excite
   it? This is the scalar-vs-winding fork of [loops-and-range.md](loops-and-range.md)
   §2, now posed for a specific field. **[open]**
2. **The light-bending coefficient.** A radion/dilaton bends light, but
   reproducing GR's PPN γ = 1 (the factor-of-2) is the generic hard constraint of
   scalar-tensor gravity — not automatic, and the point where PV/optical-metric
   accounts are *fitted* rather than derived. **[open]**

## 5. Verdict

The cheap repair does exactly two things, both honest:

- **Overturns the refutation.** The photon-mass result was a gauge artifact of
  coupling a bare potential to the gauge mode. Gauge invariance — the photon's
  *established* masslessness — forces the physical coupling transverse: a
  **refractive index**, kinetic/metric-like, non-dispersive at ω ≪ ω₀, sourced
  by energy. Problems (a) and (c) dissolve. Mechanism 2 is **not** refuted.
- **Does not clear the gate.** The index is local (Planck-contact), so range (b)
  — the original make-or-break — is untouched. The mechanism returns to the
  standing it held *before* the refutation, with the range question now sharpened
  to: *does a massless, energy-sourced mediator (candidate: the radion A₅⁽⁰⁾)
  extend the local index to 1/r, and can it bend light with the right
  coefficient?*

**Corrected status: mechanism 2 is blocked, not dead** — one live crux (range
via a mediator), a concrete GRID-native candidate (the radion, already in
forma), and two sharp open hurdles. This supersedes
[mode-coupling-derivation.md](mode-coupling-derivation.md)'s "REFUTED": that
note's negative was drawn against a gauge-illegitimate operator. A scale-scoped
caveat, not adjudicated here: the KK masses are Planck-scale while the mass
oscillator was identified with ω_Compton — that tension belongs to
[metric-mass](../metric-mass/)'s winding picture and does not affect the
mass-vs-index structural result above.
