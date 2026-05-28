# Q140: Can light quantization (and h, and α) emerge from GRID recirculation loops alone — no MaSt sheets?

**Status:** Open — **largely answered, and reframed** (developed in
[`projects/grid-quantization/`](../projects/grid-quantization/)).
GRID recirculation yields the photon's mode structure, spin, an
**α-scale leakage coupling** (single-hexagon energy return 1/129.7,
inside α's running range — *not* a closed derivation of α, which is
an axiom A6), genuine **bound modes**, and the quantization
*structure*: modes are harmonic ⇒ uniform quanta, and the substrate
is scale-invariant (IR fixed point) ⇒ ℏ universal. Deriving ℏ's
*scale* was never the target — it is a unit (like c), not a
dimensionless prediction. The lone genuinely-imported piece is
**countability** (that occupation is integer at all — the [a,a†]=1
step), and that now has a **candidate derivation** from A3 + A5 via
the dual-of-a-circle theorem (U(1)↔ℤ), resting on one interpretive
reading of A5 — *plausibly the same finite-information principle that
underwrites GRID's gravity, though that the two readings literally
coincide is unproven* (§7). So finite information may be a shared root
of gravity and quantum discreteness. Net: the quantum is *reduced* to
one interpretive question + one unit; countability is sketched (not
yet all of QM), and ℏ's scale is a unit, not a prediction.

**Source:** User question (recirculation at every scale as the
quantizer of light).

**Related:**
  [photon-from-aleph.md](../grid/photon-from-aleph.md) (photon as ℵ-line KK zero mode — the *spin* story),
  [maxwell.md](../grid/maxwell.md) (junction → Maxwell; charge as 2π vortex),
  [hexagonal.md](../grid/hexagonal.md), [fields.md](../grid/fields.md) (Y-junction scattering, helical E±iB eigenmodes),
  [sim-maxwell/](../grid/sim-maxwell/) (directional propagation from junction scattering),
  [foundations.md](../grid/foundations.md) Q1 (is the junction rule a block-spin RG fixed point?),
  [zpe_derivation.md](../projects/ma-domain/work/zpe_derivation.md) (Postulate 1: action per cycle = h),
  [INBOX.md](../grid/INBOX.md) items C/D/F (α from junction leakage / impedance ratio),
  [compact-dimensions.md](../grid/compact-dimensions.md) (α from torus wrapping — the *other* route, which found α a "designer's choice"),
  [Q18](Q18-deriving-alpha.md), [Q137](Q137-alpha-as-aleph-aspect-ratio.md) (α-derivation fronts).

---

## 1. The question

The existing GRID/MaSt account quantizes light in two unrelated
places:

- **Spin** comes from the ℵ-line compactification: a U(1) 1-form on
  S¹, KK-reduced, gives a 4D spin-1 photon
  ([photon-from-aleph.md](../grid/photon-from-aleph.md)).
- **Per-mode occupation** (n photons of frequency ω) is asserted via
  the de Broglie postulate "action per cycle = h"
  ([zpe_derivation.md](../projects/ma-domain/work/zpe_derivation.md)
  Postulate 1), the same place standard QM inserts h.

Neither *derives* the quantization, and a single spatial compact
dimension only quantizes one fundamental frequency and its
harmonics — it cannot, by itself, give every free-space frequency
its own ℏω bucket.

**The conjecture:** light quantization is a GRID substrate
phenomenon arising from **recirculation loops** in the lattice,
with no appeal to MaSt sheets. Specifically:

> A static perturbation injected on a lattice edge propagates as a
> wave (junction scattering = discrete wave equation). At every Y
> junction the wave splits into a forward-propagating component and
> a *recirculating* component that can close a loop (6 turns close
> one hexagon; larger loops close at every scale — the lattice is
> self-similar). The recirculation structure is what quantizes the
> wave.

This is the photon as a **promotion phenomenon of the substrate
itself** (level 0 → 1 in the
[photon-from-aleph](../grid/photon-from-aleph.md) hierarchy),
prior to and independent of any sheet.

---

## 2. Why injected information becomes an oscillating wave

This part is essentially settled by existing GRID results, not
conjecture. The equal-impedance junction scattering rule
([sim-maxwell](../grid/sim-maxwell/), [hexagonal.md](../grid/hexagonal.md))

> outgoing_i = (2/N)·(total incoming) − incoming_i

is, in the continuum limit, the discrete wave equation
∂²a/∂t² = c²∇²a. The **negative self-coupling** (−1/3 reflection on
the honeycomb, N=3) is the restoring term: a static edge excitation
cannot stay static because the rule leaves a sign-flipped residue
behind while transmitting forward. Oscillation is structural in the
scattering matrix. sim-maxwell confirms directional propagation at
v_lat ≈ 0.73 c on the honeycomb with exact energy conservation and
exact linear superposition. **This is standard wave mechanics
emerging from junction geometry** — no quantum content yet.

---

## 3. Where the quantization might come from

Three lattice facts, then the conjecture.

**Fact 1 — every wavelength has a natural recirculation perimeter.**
A wave taking a "turn" branch at each junction traces a closed loop;
the smallest is one hexagon (perimeter 6 L_P). The fractal loop
hierarchy means that for any frequency ω there is a loop scale s
whose round-trip time matches one wave period. The wavelength
*selects* its resonant loop.

**Fact 2 — single-valuedness forces integer winding.** This is the
same argument [maxwell.md](../grid/maxwell.md) already uses for
charge: ∮∂θ·dx = 2πn, n ∈ ℤ. Applied to a recirculation loop, the
captured phase must wind an integer number of times. (GRID
framework, not standard physics — the lattice makes this a property
of *any* closed phase path, not only spatial vortices.)

**Fact 3 — propagation and recirculation are coupled at every
junction.** [fields.md](../grid/fields.md): the three edges at a Y
node decompose into one symmetric mode (E / propagation) and two
helical modes (E ± iB / circulation). The junction rule reshuffles
energy between them every tick. A propagating packet is always
dressed by a recirculatory component.

**The conjecture (GRID framework, not derived):** a free wave at
frequency ω carries a recirculatory dressing at its resonant loop
scale (Fact 1, 3) whose phase winding is integer (Fact 2). The
action stored per cycle is therefore quantized. The propagating
part is continuous (any ω); the recirculatory part is integer-wound;
their coupling forces integer action quanta per cycle. **If this
works it is a GRID-only derivation of Postulate 1** — the de Broglie
relation as a theorem of lattice topology.

### 3a. The near-infinite tower of virtual compact dimensions

A recirculation loop is, for wave purposes, a virtual S¹ — a closed
path a wave winds around. The fractal lattice supplies a near
continuum of them with fundamentals ω₁^(s) = 2π v_lat/(6 s L_P).
Consequences:

- **Every frequency gets a quantizer.** A dense tower of virtual
  compact dimensions covers all frequencies — solving the
  "one compact dim quantizes only one frequency" problem.
- **Self-similarity ⇒ frequency-independent h.** A photon at 2ω
  resonates with a loop half the size; if the lattice is
  **scale-invariant** (the junction rule is a block-spin fixed
  point — exactly the open question Q1 in
  [foundations.md](../grid/foundations.md)), the recirculatory
  dressing is the *same structure rescaled*, so the action per
  cycle is identical. **h is universal iff GRID is an RG fixed
  point.** The two questions are one.
- **Photon vs massive particle = low-Q vs high-Q loop.** A MaSt
  compact dimension confines *all* energy (perfect resonator,
  standing wave, rest mass). A recirculation loop captures only the
  recirculatory fraction (leaky, the wave keeps moving). Same loop
  topology, same integer-winding quantization; the difference is
  leakiness. This unifies the spin-1 photon and spin-½ matter
  without invoking the ℵ-line.
- **Spin / polarization for free.** The two helical Y-junction modes
  (1, ω, ω²) and (1, ω², ω) — [fields.md](../grid/fields.md) — are
  left/right circulation = the two photon helicities. Recirculation
  *is* angular momentum; its handedness *is* spin. In the ℵ-line
  story spin and quantization are separate compactifications; here
  they are one object.
- **Vacuum-energy bill.** Each virtual compact dimension carries a
  ½ℏω₁^(s) zero-point energy
  ([zpe_derivation](../projects/ma-domain/work/zpe_derivation.md)).
  Summed over the tower this is large but finite (hard UV cutoff at
  the 1-hexagon loop, ω_max ~ v_lat/L_P), reconnecting to the
  cosmological-constant problem and [Q130](Q130-non-standing-photons-in-t6.md)/[Q131](Q131-dark-energy-as-unpromoted-information.md).

---

## 4. h is not currently derived — this would be the first derivation

Worth stating plainly, because it is easy to assume otherwise:
**GRID does not derive h.** It is set to 1 by the natural-unit
convention c = ℏ = k = 1 ([foundations.md](../grid/foundations.md)),
and in the gravity chain it is an *input*: the Unruh temperature
T = ℏa/2πck_B, the entropy S = c³A/4ℏG, and the SI grain size
L_P = √(ℏG/c³) all carry ℏ as given
([gravity.md](../grid/gravity.md)). The Jacobson argument derives
the *relationship* G = 1/(4ζ) while holding ℏ fixed. Postulate 1
also assumes h. GRID currently takes h as primitive in two
independent places and derives it nowhere. The recirculation route
would be the first place h is an **output** (in terms of L_P,
v_lat, ζ), closing the one constant the gravity derivation borrowed.

---

## 5. The α coincidence — single-loop leakage

A propagating wave does not form one loop; at **every junction it
passes it spawns a new loop**, leaving a linear array of low-Q loops
along its path. Each leaks a small fraction back into the forward
wave. This is the lattice picture of a **per-vertex coupling
constant** — one loop = one interaction factor; the array along the
path = the Dyson series dressing the propagator. The single-loop
leakage fraction *is* the coupling.

Compute it on the honeycomb (N=3, amplitude transmission 2/3 per
outgoing edge). A wave traversing one hexagon passes 6 vertices, so
the amplitude that completes the loop is (2/3)⁶ and the **energy
returned** is:

<!-- (2/3)^12 = 4096/531441 = 0.0077073 = 1/129.75 -->
$$
\left(\tfrac{2}{3}\right)^{12} = \frac{4096}{531441}
   = 0.0077073 = \frac{1}{129.75}
$$

Compare to α at its running landmarks:

| Quantity | Value | vs (2/3)¹² |
|---|---|---|
| (2/3)¹² single-hexagon energy return | 1/129.75 | — |
| α(M_Z), Z-mass | 1/128 | **−1.3%** |
| α(low energy) | 1/137.036 | +5.6% |
| exponent x with (2/3)ˣ = 1/137.036 | 12.13 | (hexagon gives 12) |

The bare single-loop value lands *inside* the physical running
range of α, closest to the Z-mass value. Conceptually this is
expected, not arbitrary: the smallest closed phase circulation (one
hexagon) is the smallest topological vortex = the unit of charge
([maxwell.md](../grid/maxwell.md)). "Energy fraction completing the
smallest loop" and "coupling between a photon and a unit charge" are
the same quantity. The **running** then has a natural reading: the
bare 1/129.7 (near the high-energy end) dressed by the full
linear array of loops at all scales flows to 1/137 at low energy —
the same "running encoded in loop count/ring length" noted in
[compact-dimensions.md](../grid/compact-dimensions.md) finding 6,
but from junction leakage rather than torus wrapping.

This is a **different route to α** than
[compact-dimensions.md](../grid/compact-dimensions.md) (which used
N=6 triangular wrapping and concluded α was a designer's choice). It
pursues the open leakage route — [INBOX.md](../grid/INBOX.md) items
D ("if one geometry's invariant equals α, that's significant") and F
("leakage as impedance ratio"). It also sits alongside the ℵ-aspect
route [Q137](Q137-alpha-as-aleph-aspect-ratio.md); whether these are
the same number seen two ways is open.

### What is loose (so we don't fool ourselves)

1. **The exponent.** A hexagon's 6 edges give 12 energy factors and
   land at 1/130. But entry/exit bookkeeping (does coupling back
   into the forward wave add a 13th factor? do the −1/3 reflections
   at each vertex contribute?) could shift the exponent by ±1,
   moving 1/130 to 1/87 or 1/195. The naive count is right; a
   careful one might not be.
2. **Coherent vs incoherent summation** over the array, and the
   phase each loop carries — this decides whether the comb gives
   running, a fixed renormalization, or noise.
3. **Bare vs renormalized.** The 1.3–5.6% gap might *be* the running
   (a feature) or the count being slightly off (a bug). Undecidable
   without the dynamics.

---

## 6. The test

Two tiers, matching two questions:

**Tier 1 — α leakage (energy ratio).** Identify hexagonal
plaquettes, add a circulation/energy-return measurement (the Test 4
"circulation" item the grid/sim-maxwell README lists but never
implemented), and a loop-leakage test: inject a pulse, measure the
energy a single hexagon returns to the forward wave. Predictions:
(a) single-loop return ≈ 1/130; (b) cumulative coupling of a *row*
of plaquettes runs with path length toward 1/137. A dispersion
measurement (drive at several ω, read off λ) makes "why oscillating"
crisp at the same time. Real scalar amplitudes suffice for the
energy ratio.

> **Tier 1 implemented** (2026-05-27) — developed in the dedicated
> project [`projects/grid-quantization/`](../projects/grid-quantization/)
> (this conjecture's development home, kept out of grid/ since it is
> speculative). Script
> [`run_recirculation.py`](../projects/grid-quantization/run_recirculation.py)
> with a self-contained lattice `lib.py` (adapted from
> grid/sim-maxwell/run_hex.py; grid/ untouched). Results:
> - **Single-loop leakage confirmed.** A pulse sent around one
>   hexagon decays as exactly (2/3)ᵏ for the first three junctions
>   (ratio 1.000 to machine precision) → per-junction transmission
>   **T = 2/3**, so the isolated single-loop **energy return is
>   (2/3)¹² = 1/129.75**, inside α's running range. (Ticks 4–6 are
>   contaminated by returning short reflected walks; the clean
>   number is the early single-step transmission extrapolated as
>   T¹².)
> - **Compact localized (bound) state — a surprise.** A generic
>   circulating excitation on one hexagon deposits **~51% into a
>   non-radiating bound mode** (amplitudes ±1/√3, ∓(1−1/√3)) that
>   persists indefinitely (verified wraparound-free); the rest
>   radiates in one tick. This overturned the pre-sim guess that
>   loops are overdamped: **loops genuinely trap energy**, giving the
>   bound/standing (massive-particle-like) limit of §3a a concrete
>   realization, coexisting with the propagating photon band. (One
>   localized eigenmode is not yet integer occupation — that is
>   Tier 2.)
> - **Band structure confirms it.** Diagonalizing the one-tick Bloch
>   operator (empirically from scatter_step; cross-checked by
>   real-space diagonalization) gives **2 flat bands (ω=0, π) + 4
>   dispersive bands**. The flat bands (group velocity 0) host the
>   compact localized states; the bound mode is the **ω=0 flat-band
>   CLS** (static). The dispersive bands are the propagating modes
>   (small-k slope = the 0.41 phase velocity). ⇒ **Q is non-monotonic
>   in ω** — infinite at the flat bands (0, π), low mid-band where
>   group velocity peaks; not a simple "Q down with frequency."
> - **Scale-invariant trapped fraction** (`loop_scaling.py`): a
>   coherent circulating mode on the boundary of K hexagons traps
>   **~51% independent of loop size** (P = 6→46). Bigger loops are
>   not lossier for the coherent mode (only a single traveling pulse
>   is, exponentially). The binding efficiency is the same at every
>   loop size = every frequency scale — a concrete instance of the
>   §3a self-similarity the h-universality claim needs (supportive,
>   not proof; the per-cycle *action* is still Tier 2).
> - **Not the zero-point ½** (`mode_projection.py`): exact projection
>   onto the bound subspace gives random → 0.337 (= 1/3 flat-band
>   fraction), circulation → **0.571** (not 0.5; the dynamics' 0.51
>   is only the loop-edge part). Excitation-dependent, so no
>   structural ½; the ZPE ½ is a spectral-average vacuum quantity, a
>   different object. Real takeaway: a circulating excitation couples
>   to the bound sector ~1.7× more than random.
> - **Circulation test** (the never-built "Test 4"): trapped loop
>   mode carries ~6× the circulation of a propagating wavefront —
>   circulation concentrates in recirculating energy, cancels for
>   clean propagation.
> - **Dispersion**: linear ω ≈ 0.41·k, non-dispersive in the
>   long-wavelength regime — injected static perturbations become
>   travelling oscillations with a definite dispersion relation.
>
> Reassessed: prediction (b) (cumulative "running" coupling toward
> 1/137) is about the *virtual* recirculatory dressing, which a
> lossless scalar model does not expose as energy transfer — so it
> is a Tier 2 (phasor) question, not a clean Tier 1 one. Exponent is
> unambiguously 12 for the isolated path (T = 2/3 confirmed
> path-independent). Full design + next steps in
> [`projects/grid-quantization/work/tier2-design.md`](../projects/grid-quantization/work/tier2-design.md).

**Tier 2 — h / quantization. Reassessed (2026-05-27): hits a wall,
and it is an honest one.** Trying to *define* "per-cycle action"
rigorously shows the test isn't well-posed in a classical linear
lattice: a linear mode at ω has energy ∝ A²ω² with amplitude A free
and continuous, so action/cycle (∝ E/ω) is *any* value — there is no
h. Quantization into ℏω quanta is **second quantization** (impose
[a,a†]=1), the same input standard QM makes. And winding does **not**
rescue it: compact-U(1) winding quantizes **charge** (vortices, per
[maxwell.md](../grid/maxwell.md)), not photon *number* — so §3a's
"integer winding ⇒ quantized action" conflates the two.

So the recirculation programme derives the photon's **mode structure,
spin (helical junction modes), an α-scale leakage coupling (1/129.7,
inside α's running range), and bound modes** — but **not h**. The leap to discrete quanta remains the standard
second-quantization input *unless* it comes from GRID's
finite-information axiom (A5: ¼ bit/cell; A3: bounded U(1) phase),
which the classical sim cannot see and which is **unexplored** (cf.
[Q135](Q135-free-information-and-decoherence.md)'s Landauer thread —
is the cost of registering one cycle of phase advance a fixed unit of
action, independent of ω?). That is the real open frontier.

What *is* lattice-derivable — the **scale-invariance** that makes h
*universal* if it emerges — holds: the photon band is linear
(ω ≈ 0.41·k) to ~10⁻⁴⁰ at observable wavelengths, an excellent IR
fixed point (`scale_invariance.py`).

**Reframed (the sharper, less gloomy reading).** ℏ's *scale* is a
unit (like c), never a dimensionless prediction — so "h didn't fall
out" is expected, not a failure. The dimensionless *principle*
decomposes: which frequencies exist (P1, derived), modes are harmonic
(P2, derived), quanta uniform + ℏ universal (P4, derived via
harmonicity + scale-invariance), and **occupation countable (P3)** —
the lone genuine import (the [a,a†]=1 step). The grid supplies the
quantization *structure*; P3 now has a **candidate derivation**:
the dual of the compact U(1) phase (A3) is ℤ [rigorous] — the same
fact as charge quantization, applied to a mode's *oscillation* phase
(giving occupation number) rather than a spatial loop (giving charge)
— triggered by A5's *informational* state being a distribution over
that phase [interpretive]. Integer occupation follows. That A5
reading is *argued* to be the one gravity uses (gravity.md) — though
showing the two readings literally coincide is open (countability §8),
since gravity reads A5 as horizon-boundary entropy and the P3 sketch
reads it as a distribution over a mode's oscillation phase — so finite
information *may* be a **shared root of gravity and quantum
discreteness**. So the quantum is **reduced to one interpretive
question + one unit** (countability sketched, not yet all of QM).
Full assessment:
[`projects/grid-quantization/work/tier2-design.md`](../projects/grid-quantization/work/tier2-design.md)
§4a–§4b and
[`countability-from-information.md`](../projects/grid-quantization/work/countability-from-information.md).

---

## 7. Status and relationship to the promotion hierarchy

Open working conjecture. It is the substrate-level (level 0 → 1)
counterpart to the sheet-level promotion stories
([Q131](Q131-dark-energy-as-unpromoted-information.md),
[Q132](Q132-promotion-chain-principle.md),
[Q135](Q135-free-information-and-decoherence.md)): light is
information promoted by the lattice's own recirculation structure,
before any sheet exists. If Tier 1 returns ≈ 1/130 and Tier 2
returns ω-independent action at a fixed point, GRID would derive —
not assume — both h and α from junction geometry alone. If either
fails, the conjecture closes as a clean negative on a tempting
mechanism.
