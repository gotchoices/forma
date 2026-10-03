# The ledger — what mechanism 3 assumes, what it derives, what it inherits

**Status:** Canonical. This file consolidates the posit ledger
([sync-carrier-mechanism.md](sync-carrier-mechanism.md) §2, P1–P9) and the
requirements list ([requirements-and-dof.md](requirements-and-dof.md) §3, R1–R11),
which grew step by step and came to overlap. Those tables are kept as the record
of how each item arose; **this file is what the chapters cite.**

Five posits, one branch choice. Everything else is inherited from GRID or derived.

---

## 1. Inherited from GRID (not posits of this project)

| | what | source |
|---|---|---|
| I1 | The canonical scatter: N equal lossless lines meeting at passive junctions; reflection (2/N − 1), transmission 2/N | [grid-duality](../../grid-duality/models/scattering.md); read physically in [requirements-and-dof.md](requirements-and-dof.md) §2 |
| I2 | Equal transit time on every line; the tick is a transit time | GRID's lattice; [grid-primitive](../../grid-primitive/)'s bare-speed equality |
| I3 | Compact dimensions; mass as light circulating in one | [metric-mass](../../metric-mass/); [grid-matter](../../grid-matter/) Ch 4 |
| I4 | Link phases and local phase invariance (axiom A4) → Maxwell | [grid/maxwell.md](../../../grid/maxwell.md) |
| I5 | Finite information per cell and the area law (axiom A5) → the Jacobson derivation | [grid/gravity.md](../../../grid/gravity.md) |

## 2. The posits

| # | posit | what it buys | mechanical reading (optional) |
|---|---|---|---|
| **L1** | **Stores.** Each node carries a lossless store whose share returns one tick later with the *same* sign; each space link carries one in series whose share returns *inverted*. | Slowing without loss and without breaking the junction timing. The two signs are the only gapless choices; the opposite in either place gives the photon a mass. | Node: a mass on the junction; link: compliance of the rod. |
| **L2** | **The field softens under load.** The store weights are set by the local static deflection q, with each member's delay factor 1 + q/2 — linear in q — and nodes and space links loaded *equally*. | Universal slowing (time dilation, not an optical medium); attraction (the response goes as K′², so the sign is not separately posited); γ = 1 with L3; β = 1; and, through the action, the source ∝ energy. Equal loading is the impedance-matched, reflectionless loading. | Space as a pre-tensioned net relaxed locally by a particle's back-pressure; the node half has no mechanical story yet. |
| **L3** | **The compact loop is untouched.** A clock's compact circulation is not loaded by the space-link stores. | Clocks slow half as much (in the logarithm) as light — the other half of γ = 1. With L2 this is exactly general relativity's static field of a rest mass, transcribed. | A rigid ring held by elastic space: the trapped light's outward push goes into S, not into stretching c. |
| **L4** | **The lattice is unanchored, and its deflection persists.** No member has a preferred value of q; only differences between neighbours carry energy. Each node's deflection is a position-like degree of freedom, not a memory. | A massless carrier: 1/r range, a field that leaves as a wave when its source is removed. (Any on-site anchoring gives a short-range Yukawa field.) | Springs between nodes and nothing tying the nodes to a background — a lattice that *is* space has nothing to anchor to. |
| **L5** | **One phenomenon, two levels.** The stores and the deflection are the microphysics of which the area-entropy law (I5), and through it the Jacobson derivation, is the statistical summary — not a second force beside it. | No double counting. The statistical account becomes a guide (what the mechanism must coarse-grain to), judged by consistency where both speak. | Molecules beneath thermodynamics. |

**Branch choice — what the deflection is.**
- **A (separate channel).** q is its own field with a stiffness κ; Newton's constant G = 1/(16πκ) is a calibration. Adds one wave channel.
- **B (one field) — preferred.** q is the steady (zero-frequency) part of the *same* field whose oscillation is light and matter; it is rectified by the field's own nonlinearity (L2). No added channel and no free coupling; brings two hazards (a resonant second harmonic, light-on-light scattering).

## 3. Derived — no longer posits

| result | where | formerly |
|---|---|---|
| No clock and no synchronization: junctions scatter each arrival on their own | [requirements-and-dof.md](requirements-and-dof.md) §2 | P1 |
| The source of the deflection is ∝ energy, has one sign, and light counts double | [action-and-gamma.md](action-and-gamma.md) §4 | P3 |
| Attraction, whatever the sign of the softening | [action-and-gamma.md](action-and-gamma.md) §4 | part of P9 |
| The carrier travels at exactly light's speed | [uniform-q-theorem.md](uniform-q-theorem.md) §5; [switch-on-result.md](switch-on-result.md) | §11 hurdle 1 |
| The conservative rule: momentum and link extension carry through a change of weight; back-reaction follows unasked | [same-channel-result.md](same-channel-result.md) §1 | R11 |
| Whether slowing is by storage or by longer transit at fixed impedance — equivalent at long wavelength | [requirements-and-dof.md](requirements-and-dof.md) §2 | R3 |
| A standing particle's pulsing source radiates only through its form factor — negligible above the Compton scale | [same-channel-result.md](same-channel-result.md) §4 | R10 |

## 4. Old numbering → new

| old | now |
|---|---|
| P1 | derived (§3) |
| P2, R7 | L4 |
| P3 | derived (§3) |
| P4 | L4 |
| P5, R8, R9, P9 | L2 |
| P6 | L1 (stores) + L2 (equal loading) |
| R1, R3, R4 | L1 |
| R2 | I2 |
| R5 | L2 |
| P7, R6 | L3 |
| P8 | L5 |
| R10 | derived (§3) |
| R11 | derived (§3) |

## 5. Degrees of freedom, net

Per node in a 3D lattice, beyond what GRID already has (two amplitudes per link,
link phases): **one node store, one store on each of its three space links, and
the node's deflection** — the last being ordinary position in a mechanical
lattice. Branch A adds a second wave channel; branch B adds nothing further. The
dynamic sector, if it is reached, needs no further stores (per-direction link
loading already supplies the tensor slots) but a **local symmetry** that the
ledger does not yet contain ([tensor-extension.md](tensor-extension.md) §5).
