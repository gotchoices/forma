# Micro rule → macro field: the honest derivation

**Status:** Working note (derivation attempt). Starts from an explicit
microscopic node/edge rule — the premise, stated before any coarse-graining
— and derives the effective macroscopic equation for the proper-time field,
reading off whether gravity (massless 1/r) follows and under exactly what
conditions. Unlike the sims ([falloff-sim-result.md](falloff-sim-result.md),
[dispersion-sim-result.md](dispersion-sim-result.md)), nothing about the
field is imposed; the failure modes are allowed to appear.

Grades: **[rule]** (a stated modeling choice), **[derived]**, **[assumed]**
(leading-order / not yet derived), **[forced]** (required by an external
fact), **[open]**.

---

## 1. The micro rule, stated explicitly

Three pieces. This is the premise; it is on the table.

**(R1) Node scatter [rule].** Each node applies the equal-impedance
scatter, outgoing_i = (2/N)·Σ(incoming) − incoming_i, instantaneously. This
is GRID's confirmed linear wave rule (→ Maxwell in the continuum). It is
lossless and, alone, non-dispersive.

**(R2) Finite processing capacity [rule].** A node can *clear* at most κ
units of signal activity per tick (finite information throughput). Let L_n
be the activity arriving at node n. If L_n ≤ κ it is cleared in one tick
(transit time 1). If L_n > κ, only κ is cleared and the surplus is
**buffered and cleared on later ticks** — nothing is dropped. The transit
time through the node is therefore

<!-- tau_n = max(1, L_n / kappa) -->
$$
\tau_n = \max\!\big(1,\; L_n/\kappa\big),
$$

and the proper-time deficit (the delay beyond the free 1 tick) is
q_n = τ_n − 1. Buffering makes this **lossless** (delay, no loss) and
**nonlinear** (τ depends on load) and **irreversible** (ordering) — the trio.

**(R3) Coupling to a mass [rule].** A compact-dimension standing wave (the
mass) resides at node n₀. Maintaining its self-consistency requires the node
to (i) spend capacity on the wave, κ_eff = κ − L_wave, and (ii) **broadcast
its state to neighbours each tick** to keep the shared node consistent —
injecting spatial activity at rate S ∝ L_wave ∝ ω_Compton ∝ the mass-energy.
Piece (ii) is the "maintaining consistency of both x and c activity"
of the original premise, made explicit.

The observable is the field q(x): the local proper-time deficit, i.e. how
much slower a clock (any confined-light clock) runs at x.

## 2. Coarse-graining to the effective equation [derived, given §3 caveats]

Signal activity is conserved by R1–R2 (buffered, never dropped). In steady
state the coarse-grained activity flux J obeys a continuity equation with a
source S (the mass's broadcast, R3-ii) and possibly a distributed loss L:

<!-- div J = S - L -->
$$
\nabla\cdot J \;=\; S\,\delta(x-x_0) \;-\; L.
$$

The delay field responds to the flux through a constitutive relation. To
leading order (weak load, linear response) activity flows down the
delay gradient with a mobility set by the spare capacity:

<!-- J = -D grad q,  D ∝ kappa -->
$$
J \;=\; -\,D\,\nabla q, \qquad D \propto \kappa .
$$

Substituting gives the effective field equation

<!-- D grad^2 q = -S delta + L -->
$$
\boxed{\;D\,\nabla^2 q \;=\; -\,S\,\delta(x-x_0) \;+\; L\;}
$$

Everything now hinges on two properties of the right-hand side, both of
which the derivation **exposes rather than assumes**.

## 3. Reading off the outcome — and the two forced conditions

**Condition A — the source must be a monopole (active broadcast), not a
passive capacity-defect. [forced]**

There are two readings of R3, and they give different physics:

- *Active source (R3-ii):* the mass **injects** activity S at n₀. Then
  D∇²q = −Sδ → **q ∝ 1/r (3D), log r (2D)** — a monopole potential. Gravity.
- *Passive defect only (R3-i alone):* the mass merely **lowers κ_eff** at
  n₀ with no injection. A localized conductance defect in a background flow
  is a **dipole** scatterer (the flow deflects around it), giving q ∝ 1/r²
  or faster — **not** gravity. And in true vacuum (no background flow) it
  produces **no field at all**.

The second reading fails, and it fails for a physical reason: **gravity
exists in vacuum** (an isolated mass has a field with nothing else around).
A passive consumer produces nothing in vacuum; only an active source does.
So "gravity in vacuum" *forces* the active-broadcast reading — the mass
must genuinely source consistency-traffic. This is not a free choice; it is
compelled, and it is exactly the R3-ii piece.

**Condition B — consistency-maintenance must be lossless (no distributed
consumption). [the linchpin, now precisely located]**

The loss term L decides massless vs screened:

- If maintaining consistency at each node **consumes** traffic (each node
  "reads" the broadcast and it is used up), then L ∝ q — a distributed
  sink — and the equation becomes (∇² − m²)q = −Sδ ⇒ **Yukawa
  e^(−r/ξ)/r**, short-range, not gravity.
- If the broadcast traffic merely **passes through** (read without
  consumption, conserved), then L = 0 ⇒ **massless ⇒ 1/r**.

This is the same losslessness the sims assumed — but the derivation pins it
to a sharp, physical statement: *is reading a consistency-broadcast lossless
or consuming?* That is a genuine property of the substrate's
information-processing, not a modeling knob, and it is where a shunt would
enter if it enters at all.

**With A (active monopole) and B (lossless), the effective equation is
D∇²q = −Sδ:**
- **Falloff:** q ∝ 1/r (3D) — massless, isotropic on the hex lattice
  (6-fold symmetry ⇒ isotropic ∇²).
- **Static ⇒ non-dispersive:** q is a steady field; a clock's rate is set
  by the local q, uniformly across frequency (a rescaling, not a filter),
  consistent with [dispersion-sim-result.md](dispersion-sim-result.md).

## 4. The coefficient [derived to a proportionality; value open]

Reading the magnitude: q_source ~ S/D. With S ∝ ω_Compton ∝ E (the
mass-energy, R3-ii) and D ∝ κ (node capacity), the field strength ∝ E/κ.
So the gravitational coupling scales as **1/κ** — weaker gravity for
higher-capacity nodes. Since the node capacity κ is the same
information-throughput that sets the resolution ζ (bits per cell), this is
the **direction of G = 1/(4ζ)**: more capacity/resolution → smaller G.
Turning "∝ 1/κ" into the numerical 1/(4ζ) requires the explicit relation
κ ↔ ζ and the O(1) factors — Objective 2, not settled here. **[open]**

## 5. What is derived, what is assumed, what is forced

| Element | Grade |
|---|---|
| Node scatter, finite capacity, buffering, standing-wave coupling | rule (the premise) |
| Conservation ⇒ continuity ∇·J = S − L | derived |
| Constitutive J = −D∇q (diffusive, leading order) | **assumed** — the remaining hard analytic step (deriving it from the 2/N scatter is not done) |
| Active-monopole source (else dipole / no vacuum field) | **forced** by gravity-in-vacuum |
| Losslessness of consistency-maintenance (else Yukawa) | **the linchpin** — a physical property of the substrate, now precisely located |
| Massless, isotropic 1/r given A + B | derived |
| Non-dispersive (static field, uniform clock rescale) | derived |
| Coefficient ∝ 1/κ ~ direction of 1/(4ζ) | derived to proportionality; value open |

## 6. Assessment — is this honest progress?

Yes, and it is different in kind from the sims. The sims *imposed* the
monopole source and the losslessness and confirmed the consequences. This
derivation **starts from the rule and finds** that gravity follows **iff**
two specific conditions hold, and it shows the concrete failure modes when
they don't (dipole/no-vacuum-field; Yukawa). Crucially:

- Condition A is **forced** (gravity-in-vacuum compels an active source) —
  a real, non-optional conclusion, not an assumption.
- Condition B (lossless consistency-maintenance) is now a **sharp physical
  question about the substrate**, not a generic "assume conservation."
- The coefficient's **origin** (∝ 1/κ ~ 1/ζ) is derived, matching the
  direction of G = 1/(4ζ).

The load remaining is honest and specific: (i) derive the constitutive
relation J = −D∇q from the 2/N scatter rather than assume it; (ii) settle
whether consistency-maintenance is lossless (Condition B) — the micro-rule
lattice sim (the "actual rules" sim) is the right instrument, now with a
*predicted* effective equation and coefficient to check against with no free
parameters; (iii) the coefficient value (κ ↔ ζ).

## 7. What this changes for chapters

Not yet ready for the mission chapters — but the target is now sharp. A
mission chapter would rest on: the effective equation (§2), the two
conditions (§3, one forced and one located), and the coefficient (§4). Two
of the three legs (constitutive relation; Condition B) are still open, and
they are exactly what the next micro-sim + the coefficient work must settle.
A *scaffolding* chapter documenting §1–§3 (the premise, the effective
equation, the two conditions) is defensible now, explicitly as the
conditional result it is.
