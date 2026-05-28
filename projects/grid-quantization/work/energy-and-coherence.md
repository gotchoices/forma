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
from *energetics and information*: if a cell is **bounded and
periodic** (at any resolution) and energy is carried by transitions,
then a wave's energy is forced to scale with its frequency, and the
quantum of action ℏ becomes a unit set by the substrate's bounds. The
two routes meet at the same place — a per-mode integer enforced by
single-valuedness on a compact phase, with ℏ a substrate unit — and
the topological route supplies the candidate that closes the gap.

## 1. Primitive postulate: a bounded *periodic* cell, transitions cost work dW [postulate]

The load-bearing requirement is **not** a particular alphabet size. It
is two structural properties of a cell:

- **Periodic (compact).** The cell's value lives on a circle — axiom
  A3's phase θ. A point on a circle has *fixed magnitude*; only its
  position (phase) varies. This **pins the magnitude**, leaving phase
  as the only free quantity — which is what forces the energy–frequency
  relation (§3).
- **Bounded resolution.** The circle is resolved into finitely many
  positions (a dial ℤ_d), so states are discrete and countable.

**Any resolution d ≥ 2 works** — §3–§5 use only "periodic + bounded."
**Base-2 (±1, the ℤ₂ dial: phase 0 ↔ +1, π ↔ −1) is just the
minimal-*hardware* special case** — one bit per cell, no internal
structure. The arguments below are written in ±1 for concreteness, but
nothing depends on d. What must be *avoided* is an **amplitude** ladder
(levels like {−1, 0, +1} read as *magnitudes*), which re-introduces a
magnitude degree of freedom and breaks the pinned-magnitude argument; a
*phase* dial of any size does not. The resolution d also sets the
per-cell occupation-ladder height — the dual of ℤ_d is ℤ_d, and d → ∞
(a continuous phase, U(1)) recovers QFT's unbounded integer ladder
([countability-from-information.md](countability-from-information.md)
§5). So the *bounded-ladder* prediction is a statement about d.

Postulate: a transition (one step of the dial) costs a fixed quantum
of work **dW**, and the substrate is **lossless** (frictionless) —
once paid, that work is conserved and free to propagate.

*What ζ is — and is not.* GRID's A5 resolution ζ (= 1/4 in 3D, 1/3 on
a 2D sheet) is **not** the dial resolution d. It is set by the node
**coordination** — the number of edges meeting at a node — and counts
*cells per bit*: the **finest fractal windowing** (how information
aggregates across a node), not how finely one cell's phase is resolved.
So ζ governs the windowing hierarchy of §5, while d is a separate, free
choice; the two must not be conflated. (Discrete dynamics on the dial
need a bit-conserving lattice-gas-style rule, not naive rounding, or
quantization noise accumulates —
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

## 3. A pinned magnitude forces E ∝ ω; the fixed quantum is action [rigorous, given §1]

Because |s| is pinned, frequency is the only knob left. The cleanest
handle is the **single-cycle injection**: inject one square-wave
cycle. Energy lives in transitions (§2), and one cycle has *exactly
two* sign reversals — so per cycle the transition count is fixed, and
per unit time (or per unit length) the transition density ∝ ω ∝ 1/λ.
Hence:

> power (energy per unit time) ∝ dW · ω

A continuum-amplitude wave would evade this — it could hide a lower ω
in a gentler amplitude — but the pinned magnitude allows no such trade.
This is Planck's *scaling*, forced by the bound.

**What is the frequency-independent quantum, then? Not the energy —
the action.** The invariant is action per cycle (energy × time):

> (action per cycle) = E · T = h,  so  E = h/T = **ℏω**

So the energy bucket *shrinks* with frequency (ℏω = h/period): largest
at ω_max (shortest period, where one cycle ≈ a single flip ≈ dW) and
proportionally smaller below. **dW is the energy quantum only at the
top of the band**; the general energy quantum is ℏω. The substrate's
fixed grain is the *action*:

> ℏ ≈ dW · τ = (energy grain) × (time grain)

— the smallest energy step times the smallest time step (the area of
one phase-space cell). This is **window-independent**, and corrects an
earlier `dW × window` form: the window governs how *total* energy in a
region scales, not the action quantum.

This identification is **dimensionally forced**, not a choice. h has
units of action = **energy × time** (J·s). A substrate with a smallest
energy dW (J) and a smallest time τ (s) has exactly one combination
with the units of action — their product. So ℏ = dW·τ is the *only*
thing the two substrate grains can form with the right dimensions;
that h is "energy × time" is precisely why it must be (energy grain) ×
(time grain).

## 4. ℏ is a unit (the substrate action grain); resolution ⊥ quantum-size [rigorous / interpretive]

ℏ ≈ dW · τ is the substrate's quantum of action — a **unit** (like c),
not a dimensionless prediction. In substrate-natural units (energy in
dW, time in τ) it is **1 by construction**; in SI it carries its
familiar value. It is *not* a function of the windowing function — the
window entered the *scaling* of total energy with ω (§3), never the
action quantum. This matches the project's standing position: the
*scale* of ℏ is a unit, the dimensionless content (ζ, α) lives
elsewhere ([tier2-design.md](tier2-design.md) §4b).

**The constants are grain-combinations.** The substrate has three
grains — length L (spacing), time τ (tick), energy dW (transition) —
and the "fundamental constants" are just combinations of them:

> c = L / τ   (length grain / time grain)
> ℏ = dW · τ   (energy grain × time grain)

That is the Planck-unit structure, and it makes "ℏ and c are units"
concrete: measure in the grains and c = ℏ = 1 automatically. **ℏ alone
fixes only the product dW·τ**; fixing the *absolute* grain scale needs
a third dimensionful input, which GRID supplies through gravity,
G = 1/(4ζ) (foundations A5). *Given* the three identifications
(c ↔ L/τ, ℏ ↔ dW·τ, G ↔ 1/4ζ), the dimensional combination then yields
L = √(ℏG/c³) = √(ℏ/(4ζc³)), τ = L/c, dW = ℏ/τ — i.e. the grains come
out as the Planck units.

**This is a consistency, not a proof that the cell size *is* the
Planck length.** Identifying the grains with (c, ℏ, G) is the
framework's *posit* that the grid is the fundamental Planck-scale
substrate (and c ↔ L/τ holds only up to an O(1) lattice wave-speed
factor — the causal limit is one edge per tick, but wave packets move
slower). An absolute length cannot be *derived* from theory without one
dimensionful input, and the grain *is* that input — so "cell = Planck
length" is an identification, almost definitional given "the grid is
fundamental," not a theorem this route establishes. What GRID predicts
dimensionlessly is ζ and α; ℏ and c remain units.

Two quantities that are easy to conflate, and are orthogonal:

| quantity | what it is | set by |
|---|---|---|
| amplitude **resolution** | how many distinguishable levels a window holds (~√M under pooling) | window / cell count |
| quantum **size** | the action step ℏ = dW·τ (energy step ℏω) | substrate grains dW, τ |

Fine amplitude resolution and a fixed minimal quantum coexist:
resolution lives in the *count*, the quantum in the *grain*.

## 5. What conservation settles, and what is left [the gap, relocated]

A photon spans an enormous number of cells, and the coarse-grained
**magnitude** (the average ⟨s⟩) smooths to a continuum by the central
limit — the lattice-gas result
([../../grid-duality/grid-quantizing.md](../../grid-duality/grid-quantizing.md)
§5, §11). That once looked fatal. It is not, because **magnitude and
energy are different objects**:

- **magnitude** = an *average* of ±1 → continuous, washes out;
- **energy** = a *count* of transitions × dW → an **integer**, and
  integers do not wash out under averaging.

And energy is **conserved**. So a quantum injected as a discrete count
(you can only flip whole cells — §1 — so injection is quantized, not
postulated) is *transported* unchanged through dispersion: a large
stationary window measures a smooth, continuous-looking wave while the
conserved total stays exactly the discrete injected value. That is how
a single photon looks — smooth classical packet, exact total ℏω.
**Conservation, not coherence, preserves the discrete total** — so the
"washout" objection is answered for the *energy*, even though it holds
for the *magnitude*.

*Corollary — shape is free, energy is fixed.* Since v_p ≠ v_g for
every ω < ω_max (the project's measured phase vs group velocities),
the carrier slips through the envelope and the packet reshapes in
flight. "One wiggle" and "many wiggles" are *shapes* of one quantum
— differing in envelope width and carrier-envelope phase — all
carrying the same conserved ℏω. Shape is the continuous/classical
part; energy is the discrete invariant.

**What conservation does *not* settle** — two requirements remain:

1. **The dynamics must be a genuine discrete (bit-conserving) cellular
   automaton.** Energy is an exact integer count only if the evolution
   keeps cells on the ±1 alphabet, changing energy by whole dW steps.
   GRID's actual scatter rule (continuous 2/3 fractions) does *not* —
   under it energy is continuous. So the count-quantization needs the
   bit-conserving Boolean rule that grid-quantizing §6.2 asserts but
   never constructs. This is the concrete dynamical gate.
2. **Per-mode ℏω.** The substrate grain is the action ℏ = dW·τ; the
   *observed* quantum is per-mode (ℏω, and one cannot put a fractional
   photon into a single mode). Getting from a per-cell count to a
   per-mode integer is where a mode must act as one coherent
   oscillator — and that lock, to survive coarse-graining, must be
   **topological** (an integer winding, not an amplitude agreement,
   which the central limit erodes).

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

**Why this is quantization, stated plainly: periodicity ⇒ a discrete
spectrum.** A function on a *periodic* phase (a circle, θ ∈ [0,2π)) is
a Fourier *series* — Σ_n c_n e^{inθ} with **integer** n — exactly as a
time-periodic signal has a discrete line spectrum at integer harmonics
of its fundamental. That integer index *is* the occupation number. So
quantization comes from the **periodicity** of the phase, **not** from
the cell values being discrete: the phase values may be continuous,
yet its conjugate (occupation) is integer because the phase closes on
itself. This unifies the two routes and the two substrates:

- a **continuous** periodic phase (U(1), infinite information per cell)
  gives the *unbounded* integer ladder ℤ — ordinary QED;
- a **finite** dial (ℤ_d, A5's finite information) gives a *bounded*
  ladder of d rungs — the GRID-specific deviation.

They are the same circle at two resolutions; continuous is the d → ∞
limit. So the ±1 substrate's discreteness is *not* what does the
quantizing — periodicity is — it is what makes the ladder *bounded*
and supplies the substrate energy grain dW (§3). The clean statement
of the mechanism is the continuous one; the finite substrate is what
makes it GRID rather than textbook QED.

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
| bounded *periodic* cell (any resolution; ±1 = minimal hardware); transition costs dW; lossless | **postulate** |
| energy = dW × transitions (static = 0) | **rigorous** |
| pinned magnitude ⇒ power ∝ ω (Planck scaling), no amplitude escape | **rigorous** |
| fixed quantum is *action*; energy quantum = ℏω = h/period (dW only at ω_max) | **rigorous** |
| ℏ ≈ dW·τ is a unit, window-independent | **rigorous / interpretive** |
| resolution ⊥ quantum-size | **rigorous** |
| conservation transports a discrete *total* through dispersion | **rigorous** (given discrete-CA dynamics) |
| dynamics are a bit-conserving discrete CA (not the continuous 2/3 rule) | **the dynamical gate** (unbuilt) |
| per-mode ℏω from a per-cell count | needs a topological lock |
| loop-closure ⇒ discrete winding sectors (the lock) | **conjecture** |

**Bottom line.** A bounded ±1 substrate with a fixed flip-cost forces
the Planck *scaling* (E ∝ ω) and fixes ℏ's *scale* as the substrate
action unit (dW·τ) — both without a free-amplitude escape — and
*conservation* carries a discrete total through dispersion, so the
coarse-graining washout is not fatal to the energy (only to the
magnitude). What remains is sharper than before: the dynamics must be
a genuine discrete (bit-conserving) cellular automaton, and the
per-mode ℏω needs a topological lock (loop-closure sectors the
candidate). Progress toward P3, not a closure of it.

## 8. What would harden or test this

- A bit-conserving discrete scatter rule, to confirm the discrete
  dynamics reproduce the linear wave results without naive-rounding
  noise (grid-quantizing §6.2). **Concrete candidate — a sigma-delta /
  error-feedback node:** the junction computes the exact (fractional)
  scatter result, emits only the integer part on each edge, and
  *carries the remainder forward* in a small bounded accumulator. This
  resolves the 1/3 obstruction (no finite alphabet is closed under the
  literal 2/3 rule — denominators grow as 3ⁿ) by tracking the owed
  fraction exactly: edges stay integer (finite alphabet), the total
  (edge integers + carried remainders) is **conserved exactly**, and
  the continuous 2/3 scattering reappears as the noise-shaped
  time-average of the integer edge stream — the substrate version of
  how a 1-bit sigma-delta DAC reproduces a high-resolution signal.
  *Caveats:* the node carries a few bits of memory (bounded, but more
  than ζ's per-cell budget — it is a junction, not a counted cell),
  and error-feedback is not automatically reversible (it gives exact
  *conservation* — the load-bearing property — not microscopic
  time-reversal; an FHP-style rule would give both).
- A vertex / height-model formulation of the loop-closure constraints
  on the ±1 honeycomb, to test whether discrete winding sectors exist
  (the §6 conjecture). This is the first computational probe that would
  actually bear on the hinge.
- Pin the fixed window W to A5's resolution explicitly — the same task
  as [countability-from-information.md](countability-from-information.md)
  §8 step 1 (one reading of A5, shared with the gravity derivation).
