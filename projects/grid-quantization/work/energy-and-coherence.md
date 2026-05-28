# A bounded-substrate route to light-quantization

Working notes (hypothesis). A second route to **P3** (that occupation
is countable) and to the *scale* of ℏ, built from a bounded/discrete
substrate and the observation that energy is carried by transitions.
Companion to [countability-from-information.md](countability-from-information.md)
(the topological U(1)↔ℤ route) and to
[tier2-design.md](tier2-design.md) §4a (why a linear continuum cannot
quantize a free wave). Each step is graded **[postulate] /
[rigorous] / [interpretive] / [conjecture]** so the load-bearing
assumptions stay visible. Nothing here is settled physics.

## 0. What this route adds

[countability-from-information.md](countability-from-information.md)
derives integer occupation from the *topology* of a compact phase
(the dual of the circle U(1) is ℤ). This note reaches the same target
from *energetics and information*: if the substrate has a finite
per-cell alphabet and energy is carried by transitions, then a wave's
energy is forced to scale with its frequency, and the quantum of
action ℏ becomes a unit set by the substrate's bounds. The two routes
meet at one open hinge — coherence across a coarse-graining window —
and the topological route supplies the candidate that could close it.

## 1. Primitive postulate: a two-state cell, flipping costs work dW [postulate]

Take the coarsest substrate consistent with A5's finite information:
each cell carries a **two-state** value s ∈ {+1, −1}. This is A3's
compact phase resolved to two positions (phase 0 ↔ +1, phase π ↔ −1)
— the group ℤ₂. There is no separate "rest" value; rest is the
disordered regional average ⟨s⟩ = 0, exactly as in an Ising magnet.

Postulate: changing a cell's state costs a fixed quantum of work
**dW**, and the substrate is **lossless** (frictionless) — once paid,
that work is conserved and free to propagate.

Why two states, not three (±1, 0): the two-state cell **pins the
magnitude** (|s| = 1 always), so the only free quantity at the cell
level is the sign/phase. With no cell-level amplitude to vary, *all*
dynamics is phase change — which is what forces the energy–frequency
relation in §3. A third (zero) state re-introduces a cell-level
amplitude and blurs that argument; it is not needed. (Dynamics on a
±1 alphabet need a bit-conserving lattice-gas-style rule rather than
naive rounding, or quantization noise accumulates — see
[../../grid-duality/grid-quantizing.md](../../grid-duality/grid-quantizing.md)
§6.2.)

## 2. Energy lives in transitions — derived, not postulated [rigorous, given §1]

The work expended over any history is dW × (number of flips). A
static configuration (no flips) costs nothing — consistent with A3
(a uniform phase is gauge; only differences are physical), and
correcting the naive Σ(value²) energy measure, which wrongly charges
a static offset. (The scatter sim's `edge_energy = a_fwd² + a_bwd²`
has this defect for a uniform state — harmless for the wave studies,
which carry no static component, but the distinction matters for any
held/DC excitation.)

In the continuum this is the familiar field energy: "dW per flip"
with flips at rate ∝ ω is power ∝ dW·ω, i.e. energy density ∝
(∂s/∂t)² + (∇s)² — energy in the time-derivative and the gradient,
not in the value. "Energy in the transitions" is the discrete image
of "energy in the derivatives."

## 3. A pinned magnitude forces E ∝ ω [rigorous, given §1 + a fixed window]

Because |s| is pinned, frequency is the only knob left. A wave at
angular frequency ω reverses each participating cell at a rate ∝ ω
(one cycle = two sign reversals); equivalently, in space, its
domain-wall density ∝ wavenumber k ∝ ω. So in a region of fixed
extent W (cells, or ticks):

> energy in window ≈ dW × (transitions in window) ∝ dW · ω · W

Hence, at fixed substrate bounds, **energy in a fixed window is
proportional to frequency**:

> E_window = ℏ_eff · ω,  with  ℏ_eff ∝ dW × W

This is Planck's *scaling*, obtained with no free amplitude to trade
against ω. A continuum-amplitude wave evades it (lower ω can be hidden
in a gentler amplitude); the pinned magnitude does not allow that.

**Caveat (load-bearing).** E_window is a window/power-like quantity,
not the per-packet energy of a free photon (which is ℏω for a packet
of *any* length). The two coincide only if W is a *fixed physical*
quantity, not an observer's choice — otherwise ℏ_eff would depend on
the window, which is unphysical. A5 is what fixes W (the holographic
information resolution; the tensor window of foundations Q1). So this
route delivers the *scaling* and locates ℏ; it does not by itself
deliver per-packet ℏω until W is pinned (this section) and coherence
holds (§5).

## 4. ℏ is a unit set by the bounds; resolution ⊥ quantum-size [rigorous / interpretive]

ℏ_eff ∝ dW × W is the substrate's quantum of action — a **unit**
(like c), the area of the minimal phase-space cell (flip cost ×
window), not a dimensionless prediction. This matches the project's
standing position that the *scale* of ℏ is a unit and the
dimensionless content (ζ, α) lives elsewhere
([tier2-design.md](tier2-design.md) §4b).

Two quantities that are easy to conflate, and are orthogonal:

| quantity | what it is | set by |
|---|---|---|
| amplitude **resolution** | how many distinguishable levels a window holds (~W, or ~√M under incoherent pooling) | window size |
| quantum **size** | the energy of one flip | dW |

A window can have fine amplitude resolution **and** a fixed minimal
quantum at the same time: resolution lives in the *count*, the quantum
lives in the *flip*. They do not compete.

## 5. The open hinge: does the cell-level quantum survive coarse-graining? [the gap]

A photon spans an enormous number of cells. Two pooling regimes:

- **Incoherent** (cells independent): the coarse-grained amplitude
  smooths by the central limit (resolution ~1/√M), and the per-cell
  quantum **washes into a continuum** — the lattice-gas result
  ([../../grid-duality/grid-quantizing.md](../../grid-duality/grid-quantizing.md)
  §5, §11: a binary substrate yields continuous macro-physics). The
  quantum is lost.
- **Coherent** (cells locked): the window acts as one element, and the
  quantum **survives**.

So on this route, light-quantization reduces to a single question:
**what locks a window coherent?** Amplitude *agreement* is the wrong
kind of lock — it is exactly what the central limit erodes. A lock
that survives coarse-graining must be **topological**: a winding
number / loop-closure sector is an integer, and coarse-graining cannot
smear an integer into a fraction.

## 6. Candidate lock: loop-consistency on the discrete substrate [conjecture]

Each cell belongs to a near-infinite set of closed loops (its hexagon,
and every larger closure). On a *discrete* substrate, simultaneous
single-valuedness around all of them is a **constraint-satisfaction
problem** — the setting of vertex / ice models and dimer / height-
function models, which are known to organize discrete variables into
**topological sectors** with quantized invariants. The conjecture: a
±1 honeycomb under loop-closure constraints admits only discrete
winding sectors; a wave sits in one sector; the sector is the
coherence lock, and it survives coarse-graining because it is an
integer winding.

This is the *same* single-valuedness the topological route
([countability-from-information.md](countability-from-information.md)
§1) uses to get integer-ness — here repurposed as the mechanism that
keeps the §3 energy quantum coherent from the Planck scale up to a
photon. The two routes are one fact (single-valuedness on a compact
phase) seen from energy and from topology.

**Terminology.** The integer such a loop carries is a conserved
**winding / circulation** — angular-momentum-like in physical content.
It is *not* automatically "charge." In the GRID/MaSt promotion ladder
(substrate → light → mass → charge, one conserved observable per wrap;
[../../grid-duality/README.md](../../grid-duality/README.md) ch. 7–8)
electric charge is a high rung (a double-wrap); spin/helicity and
occupation are lower ones. The generic output of a single loop is a
winding, promoted to spin / mass / charge at successive closures.

## 7. Status

| Step | Grade |
|---|---|
| ±1 cell as the d=2 phase dial; flip costs dW; lossless | **postulate** |
| energy = dW × transitions (static = 0) | **rigorous** |
| pinned magnitude ⇒ E_window ∝ ω | **rigorous** (given a fixed W) |
| ℏ_eff ∝ dW × W is a unit | **rigorous / interpretive** |
| resolution ⊥ quantum-size | **rigorous** |
| per-packet ℏω (not just E_window ∝ ω) | needs W pinned **and** coherence |
| coherence survives coarse-graining iff topological | **the gap** |
| loop-closure ⇒ discrete winding sectors (the lock) | **conjecture** |

**Bottom line.** A bounded ±1 substrate with a fixed flip-cost forces
the Planck *scaling* (E ∝ ω) and fixes ℏ's *scale* as a substrate
unit (dW × window) — both without a free-amplitude escape. What it
does **not** yet deliver is the survival of that quantum under
coarse-graining to a photon; that reduces to one well-posed question
(coherence), for which the topological loop-closure sector is the
candidate answer. Progress toward P3, not a closure of it.

## 8. What would harden or test this

- A bit-conserving (lattice-gas/FHP-style) ±1 scatter rule, to confirm
  the ±1 dynamics reproduce the linear wave results without
  naive-rounding noise (grid-quantizing §6.2).
- A vertex / height-model formulation of the loop-closure constraints
  on the ±1 honeycomb, to test whether discrete winding sectors exist
  (the §6 conjecture). This is the first computational probe that would
  actually bear on the hinge.
- Pin the fixed window W to A5's resolution explicitly — the same task
  as [countability-from-information.md](countability-from-information.md)
  §8 step 1 (one reading of A5, shared with the gravity derivation).
