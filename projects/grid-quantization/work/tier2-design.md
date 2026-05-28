# Tier 2 design + the bound-state finding

Working notes: what Tier 1 found (including a surprise that reshapes
the conjecture), and how Tier 2 should be built. Nothing here is
settled physics; it is the planning layer for
[Q140](../../../qa/Q140-light-quantization-from-recirculation.md).

## 1. Tier 1 recap (verified)

| Measurement | Result | Bearing on Q140 |
|---|---|---|
| loop | per-junction transmission **T = 2/3** exactly (ratio 1.000 for k=1–3); isolated single-loop energy return **(2/3)¹² = 1/129.75** | α-leakage: 1/129.75 sits inside α's running range (1/137 … 1/128) |
| bound | a generic circulating hexagon excitation deposits **~51%** into a **non-radiating compact localized state**; rest radiates in one tick | loops genuinely TRAP energy — see §2 |
| circ | trapped loop circulation ≈ 6×, propagating wave ≈ 2× | circulation concentrates in trapped energy, cancels for propagation |
| disp | linear ω ≈ 0.41·k, non-dispersive (long-wavelength) | injected static perturbation → travelling oscillation with a definite dispersion relation |

## 2. The surprise: a compact localized (bound) state

The pre-simulation guess was that a single hexagon is a strongly
*overdamped* resonator (single-pulse retention (2/3)¹² ≈ 0.008 per
loop, Q ≈ 1) — so quantization could not rest on resonant trapping
and would have to be purely topological.

**The simulation says otherwise.** Excite the *whole* hexagon as a
coherent circulating mode and the loop energy does **not** ring down:
it drops to ~51% in the first tick and then **holds indefinitely**
(flat to t = 300 on 64×64; verified wraparound-free to t ≈ 60 on
96×96, where radiated energy cannot return). The surviving state is a
fixed standing pattern on the 6 loop edges with amplitudes ±1/√3 and
∓(1−1/√3).

That is a **non-radiating bound mode — a compact localized state
(CLS)** of the edge-wave scattering network. Physical reading:

- A generic circulating excitation is ~half bound eigenmode, ~half
  radiation. The bound half stays on the hexagon forever; the
  radiating half leaves in one tick and never comes back.
- So **loops can trap energy permanently**, not just transiently.
  The "photon vs massive particle = low-Q vs high-Q loop" picture
  from Q140 §3a now has a concrete bound end: the CLS is a genuine
  localized, persistent excitation — the standing / massive-like
  limit — coexisting with the propagating (free-photon) band.

**Caveat / what it is NOT (yet).** One localized eigenmode at a fixed
site is not "quantization of light at every frequency." It shows the
*premise* (loops trap energy) is real; it does not by itself give
integer occupation or ℏω-per-quantum. That linkage is Tier 2.

**Why this is plausible here but not in textbook honeycomb.**
Graphene tight-binding (state on *vertices*) has Dirac cones and no
flat band. This model puts the state on *edges* with junction
scattering — a wave/quantum-graph network, which can and evidently
does carry a flat (dispersionless = localized) band. Confirming that
flat band is the first recommended computation below.

## 3. Band structure — DONE (`band_structure.py`)

Computed the one-tick Bloch operator U(k) **empirically** from
`scatter_step` (applying it to the 6 per-cell Bloch basis states and
reading an interior reference cell — convention-agnostic, unitary to
3e-16). Cross-checked against full real-space diagonalization on a
10×10 torus (unitary to 8e-17).

**Result (confirmed two independent ways):**

> The honeycomb edge-network has **2 flat bands (ω = 0 and ω = π) +
> 4 dispersive bands.** Exactly 1/6 of all states pile up at ω=0 and
> 1/6 at ω=π. Max propagating group velocity ≈ 0.86.

- The **flat bands** (group velocity 0) host the **compact localized
  states** — this is what §2's bound mode is. The bound test's
  trapped mode lives on the **ω=0 flat band** (a *static* CLS: its
  loop amplitude never changes sign, confirmed). So the bound state
  is real and now *explained*: it is a flat-band CLS.
- The **dispersive bands** are the propagating (free-photon-like)
  modes; the measured ω ≈ 0.41·k phase velocity is the small-k slope
  of the lowest dispersive band.

**Methodological note (cost me an iteration).** The first detector —
per-band *bandwidth* over the BZ — wrongly reported "no flat band",
because the flat bands at ω=0,π are coincident with the dispersive
band *edges*, so sorting smeared them. The correct detector is the
**density of states**: a flat band is a δ-spike holding ~1/6 of all
eigenphases. Real-space diagonalization (degeneracy ≈ L² + localized
eigenvectors, participation ratio ≈ one hexagon) is the ground truth
that caught the error.

### Answer to "Q vs frequency / bigger loop more lossy"

The band structure settles the question raised when this was run:

- **Q is NON-monotonic in ω.** It is effectively *infinite* at the
  flat-band frequencies ω = 0 and ω = π (group velocity 0 ⇒ localized
  ⇒ non-radiating) and *low* mid-band, where group velocity peaks and
  modes propagate/radiate most. So neither "Q down with frequency"
  nor "Q up with frequency" holds globally — Q is high at the band
  extremes and low in between.
- **Bigger loop more lossy?** Only for a single *traveling pulse*
  (returns (2/3)^(2P), exponential). For the *coherent circulating
  mode* the answer is **no** — see the scale-invariance result below,
  which corrects my first guess that larger loops trap less.

### Scale-invariance of the trapped fraction (`loop_scaling.py`)

Exciting the boundary of a K-hexagon patch as a coherent circulating
mode and measuring the non-radiating fraction (wraparound-free):

| hexagons | perimeter P | trapped fraction |
|---:|---:|---:|
| 1 | 6 | 0.509 |
| 7 | 20 | 0.507 |
| 19 | 34 | 0.509 |
| 37 | 46 | 0.509 |

**The trapped fraction is ~½, independent of loop size** (drift even
shrinks with P). So the binding efficiency is the same at every loop
size — i.e. at every frequency scale, since loop size ↔ resonant
frequency. This is a concrete instance of the **self-similarity /
scale-invariance** the h-universality argument rests on (Q140 §3a,
foundations Q1). It is *supportive* — a scale-invariant trapped
fraction is necessary for, but does not by itself prove, a
frequency-independent per-cycle action (h). That proof is still the
Tier 2 job (§4). My earlier intuition that bigger loops trap less was
wrong; the flat bands hold a fixed (1/3 of all) modes at every scale,
and a circulating excitation's overlap with them is size-independent.

**Is the ~½ the zero-point ½? No** (`mode_projection.py`). Projecting
excitations exactly onto the bound subspace: random → 0.337 (= the
1/3 flat-band dimension fraction), hexagon circulation → **0.571**
(not 0.5; the dynamics' 0.51 is just the loop-edge part, the rest of
the bound mode sits on spokes), bound pattern → 1.000. So the value
is not 0.5 and is excitation-dependent — there is no structural ½.
The ZPE ½ (zpe_derivation.md) is a spectral-average vacuum quantity,
a different mechanism. The real, scale-invariant statement is:
**a circulating (photon-like) excitation couples to the bound sector
~1.7× more than random.**

## 4. Tier 2 central test: is h frequency-independent?

The load-bearing Q140 claim: the per-cycle action carried by the
recirculatory dressing is the same at every frequency **iff** the
lattice is a block-spin RG fixed point (foundations Q1). That is what
would make h universal rather than ω-dependent.

**Infrastructure needed (why Tier 2 ≠ Tier 1):**

1. **Complex/phasor amplitudes.** Integer phase *winding* around a
   loop (the single-valuedness that quantizes) is invisible to real
   scalar amplitudes. The scatter rule is already linear, so it runs
   unchanged on complex arrays; the work is in the measurement.
2. **Symmetric/helical mode decomposition.** At each N=3 junction the
   three edges decompose by the cube-roots of unity (fields.md):
   mode 0 = (1,1,1) symmetric/E-like; modes 1,2 = (1,ω,ω²),(1,ω²,ω)
   helical = E ± iB = the two circulations. The recirculatory dressing
   lives in modes 1,2.

**Protocol (draft):**

- Drive a monochromatic wave at ω (complex source); reach steady state.
- Decompose the field into symmetric vs helical content per junction.
- Define the **per-cycle action** of the helical (recirculatory)
  dressing — candidate: (helical energy density) / ω, integrated over
  a wavelength, per cycle. The precise definition is the main design
  risk and must be fixed before coding (see §5).
- Sweep ω. **Pass:** the per-cycle action is flat in ω (⇒ h universal;
  fixed point). **Fail:** it drifts with ω (⇒ h would be
  scale-dependent — a real problem the framework must confront).

Cross-check: the same flatness is the block-spin invariance of
foundations Q1 — measurable independently by coarse-graining the
junction rule 2×/4× and checking the effective T, ζ, coupling return
to the same values. If both the action-flatness and the block-spin
invariance agree, that is strong, redundant evidence.

## 4a. Resolving §5.1 on paper — and a wall it hits

Trying to *define* "per-cycle action" rigorously (the §5.1 gate)
surfaces a problem that no choice of definition fixes, and it is
important to state plainly rather than code around:

**A classical linear lattice cannot quantize a free wave's energy.**
A linear field mode at frequency ω has energy ∝ A²ω² with amplitude A
a *free, continuous* parameter — so its "action per cycle" (∝ E/ω)
can be any value. There is no h. Quantization into ℏω quanta is
**second quantization** (promote the mode amplitude to ladder
operators, impose [a,a†]=1) — the same canonical/de-Broglie input
standard QM makes (cf. metric-mass ch. 9's HO bridge; Postulate 1 in
zpe_derivation.md, explicitly *postulated, not derived*). Our scatter
rule is linear (sim-maxwell confirmed exact superposition), so the
dynamics are classical-linear and carry no amplitude quantization.

**Doesn't winding save it?** No. The compact-U(1) phase (axiom A3)
*does* quantize winding — but winding-around-a-loop quantizes
**charge** (vortices), exactly as maxwell.md derives. Photon *number*
(occupation of a mode) is a different quantity; the loop topology
does not fix it. So the §3a "integer winding ⇒ quantized per-cycle
action" step conflates charge quantization with energy quantization.

**Consequence for Q140.** The recirculation programme genuinely
delivers: the photon's **mode structure** (bands, dispersion), its
**spin/polarization** (the helical E±iB junction eigenmodes), **α**
(single-loop leakage 1/129.7), and **bound modes** (flat-band CLS).
That is a lot. But it does **not** derive **h**: the leap from a
classical field to discrete quanta remains the standard
second-quantization input. h is still as much an input here as in
ordinary QM — unless it comes from somewhere the classical sim cannot
see (the finite-information axiom A5/ζ — bounded phase + finite
bits-per-cell — which *is* a genuine non-classical ingredient, but
its link to amplitude quantization is unexplored; cf. Q135's
Landauer-cost thread).

**So the well-posed, lattice-derivable question is not "measure h"
but "is the substrate scale-invariant?"** — because scale-invariance
is the property that would make h *universal* (frequency-independent)
*if* h emerges. That part is computable and is what we test.

### Scale-invariance result (`scale_invariance.py`)

The photon (acoustic) band is **linear, ω = v·k with v ≈ 0.41**, to
within: 0.1% deviation at λ ≈ 9 L, 1% at λ ≈ 4 L, 10% at λ ≈ 2 L. The
deviation falls as ~k² toward long wavelength. Real photons have
λ/L_P ≳ 10²⁰, so the dispersion is scale-free (no preferred scale) to
~10⁻⁴⁰ at any observable frequency — an excellent **IR fixed point**,
with scale-invariance breaking only at the lattice (Planck) scale,
exactly where new physics is expected anyway. So *if* a quantum
emerges, it is frequency-independent to fantastic precision; the
substrate supplies the universality, not the quantum.

### §4b — Principle vs scale (a correction to the "wall" framing)

The "we didn't derive h" framing above was too gloomy, and conflated
two different things. **ℏ's numerical value is a *unit*** (the action
unit, = 1 by construction, exactly like c is the speed unit) — not a
dimensionless prediction. Expecting the *scale* to "fall out" was a
category error; GRID takes α (dimensionless) as input and ℏ = c = 1
by convention. The meaningful target is the dimensionless *principle*
of quantization, which decomposes:

| Piece of "light is quantized" | Source |
|---|---|
| **P1** which frequencies exist (spectrum/dispersion) | grid-derived |
| **P2** each mode is a *harmonic* (linear) oscillator | grid-derived (exact superposition) |
| **P3** occupation is *countable* (n ∈ ℤ at all) | the one genuine import |
| **P4** quanta are *uniform* (ℏω each) and ℏ *universal* across ω | grid-derived (harmonic ⇒ even ladder; §4a scale-invariance ⇒ universal) |
| scale of ℏ | a unit, not a prediction |

P2 + P4 are not trivial: harmonic oscillators quantize into **even**
ladders, which is *why* every photon of frequency ω is identical with
energy exactly ℏω; an anharmonic medium would give uneven rungs and
no clean photon. The grid's exact linearity guarantees the clean
photon picture, and scale-invariance makes ℏ the same at every ω.

So the only genuinely-imported piece is **P3 — countability** (the
[a,a†]=1 step). The grid is not short of integers (winding → charge,
compact-mode number → spectrum); the sharp open question is whether
**A5's finite information (¼ bit/cell, bounded U(1) phase) forces
occupation to be countable.** If yes, P3 is grid-native too and the
quantization of light is fully GRID-derived up to the unit ℏ.

**Revised verdict:** not "failed to derive h" but **"reduced the
quantum to one dimensionless question (does A5 ⇒ countability?) plus
one unit (ℏ)."** The grid supplies the entire quantization
*structure*; P3 is the lone frontier.

## 5. Open design questions / risks (resolve before coding Tier 2)

1. **Definition of "per-cycle action."** Energy/ω is the obvious
   candidate but must be pinned to something gauge-invariant and
   independent of normalization, or the flatness test is vacuous.
   This is the single most important thing to get right.
2. **Steady-state vs transient.** A driven open network reaches a
   steady state with standing + radiated parts; the measurement must
   isolate the dressing, not the drive or the radiation.
3. **Does the bound state contaminate the dressing measure?** The CLS
   (§2) is a zero-group-velocity mode; a monochromatic drive at the
   CLS frequency will pump it resonantly. The action measurement must
   either avoid that frequency or account for it.
4. **Lattice anisotropy.** Phase velocity along x (0.41) need not
   equal other directions; the action measure should be
   direction-averaged or the anisotropy quantified.

## 6. Recommended order (revised after §4a)

1. ~~`band_structure.py` — confirm the flat band, map the propagating
   band(s).~~ **Done (§3):** 2 flat bands (ω=0, π) + 4 dispersive.
2. ~~Resolve §5.1 (per-cycle-action definition).~~ **Done (§4a):** the
   honest resolution is that the quantity isn't well-posed in a
   classical linear lattice — the lattice gives modes, not quanta.
   The well-posed surrogate (scale-invariance) is measured
   (`scale_invariance.py`): an excellent IR fixed point.
3. ~~Complex-amplitude per-cycle-action ω-sweep.~~ **Shelved** — it
   would measure a classically-unquantized quantity. Not worth coding
   until/unless the quantization source (item 4) is identified.
4. **The real open frontier — the quantization source.** Does GRID's
   finite-information axiom (A5: ζ = ¼ bit/cell; A3: bounded U(1)
   phase) quantize a mode's amplitude into ℏω quanta — i.e. derive
   second quantization rather than import it? This is *foundational*,
   not a quick sim. Candidate concrete sub-question (cf. Q135): is the
   Landauer cost of registering one cycle of phase advance one fixed
   unit of action, independent of ω? If yes, that unit is h and the
   IR scale-invariance (§4a) makes it universal.

Still-available clean follow-ups (smaller, optional):
- **Construct the CLS explicitly** from the ω=0 flat-band states;
  check whether *larger* CLS exist (bears on the Q140 §3a loop tower).
- **Block-spin / decimation** (integrate out one sublattice ⇒
  effective S·M(k) coin) to test the RG fixed point directly, a more
  rigorous version of the dispersion-linearity scale-invariance.
