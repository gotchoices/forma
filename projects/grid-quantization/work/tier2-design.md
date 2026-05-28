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

## 6. Recommended order

1. ~~`band_structure.py` — confirm the flat band, map the propagating
   band(s).~~ **Done (§3):** 2 flat bands (ω=0, π) + 4 dispersive.
2. **Next:** resolve §5.1 (the per-cycle-action definition) on paper —
   the gate for the whole Tier 2 measurement.
3. Complex-amplitude lattice + helical decomposition (`clib.py` or
   extend `lib.py`); verify the two circulations are eigenmodes (the
   ω=π flat band may be one of them — worth checking which flat band
   carries which circulation).
4. The ω-sweep action-flatness test (the h-universality / fixed-point
   experiment), with the block-spin cross-check.

A smaller, clean follow-up also now available: **construct the CLS
explicitly** as localized combinations of the ω=0 flat-band Bloch
states and confirm they are the hexagon bound mode — and check
whether *larger* CLS exist (would bear on the "loop tower" of
Q140 §3a).
