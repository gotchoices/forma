# The recirculation-loop route to quantization — a superseded attempt

**Status: dead end (superseded).** This is the project's *first*
hypothesis for why light is quantized: that closed recirculation loops
in the lattice, made self-consistent by single-valuedness, create the
quantum. It did not work. The boundedness-of-nodes route
([energy-and-coherence.md](energy-and-coherence.md)) and the
compact-phase countability route
([countability-from-information.md](countability-from-information.md))
replaced it.

This file is reconstructed from git history (the original README at
commit `cccabfa`, the negative result at `13a1944` "Run
grid-quantization to negative", and the refutation that still lives in
[tier2-design.md](tier2-design.md) §4a). It exists so the attempt — and
the one valuable by-product it left, the α-scale leakage value — has a
persistent home rather than being scattered across the README and
tier2-design.

---

## 1. The hypothesis

As a wave propagates through the honeycomb, every junction it passes
spawns a closed **recirculation loop**; the wave is "dressed" by a
linear array of these loops along (and flanking) its path — the lattice
form of a dressed propagator. Two conjectures were attached to this
picture (original README, `cccabfa`):

- **Quantization (the self-consistency idea).** A dense tower of loop
  sizes was read as a near-infinite set of *virtual compact dimensions*.
  Every frequency was assumed to find a resonant loop, and
  **single-valuedness** around each loop — the self-consistency
  condition ∮∂θ = 2πn, the same rule GRID uses for charge — would force
  **integer winding**, quantizing the action carried per cycle.
  Self-similarity across loop scales would then make the per-cycle
  action (i.e. h) frequency-independent (the foundations-Q1 block-spin
  fixed-point question).
- **Coupling.** The single-hexagon **energy-return fraction** is the
  bare coupling — see §2.

The intuition: the quantum of light would emerge from the *geometric
self-consistency* of the loops the photon dresses, with no second
quantization imposed by hand.

---

## 2. The one valuable by-product: the α-scale leakage value

This is the "interesting value in the range of α" — the **loop leakage**,
the fraction of flow that survives a full trip around one hexagonal loop.
It is **not lost**; it survives in [../README.md](../README.md)
(Headline, the phenomenon table, and the mechanism paragraph) and in
[tier2-design.md](tier2-design.md) §1. Recorded here for completeness:

- Per-junction transmission is **T = 2/3** exactly (the N=3
  equal-impedance rule), confirmed to machine precision for the first
  three junctions ([../outputs/loop_decay.csv](../outputs/loop_decay.csv);
  `../scripts/run_recirculation.py --test loop`).
- A full single-hexagon loop is 6 junctions; the amplitude return is
  (2/3)⁶ and the **energy return is (2/3)¹² = 1/129.75**.
- 1/129.75 sits **inside α's physical running range** (1/137 at low
  energy, 1/128 at the Z mass).

The value is **suggestive, not a derivation**: α's value is a GRID input
(axiom A6), and the exponent/entry-exit bookkeeping carries caveats
([Q140 §5](../../../qa/Q140-light-quantization-from-recirculation.md)).
The early open question — does a *row* of plaquettes accumulate the
coupling from 1/129.7 toward 1/137? — was never settled and lapsed when
the route was abandoned.

---

## 3. Why it was a dead end

Three independent failures, two conceptual and one computational
(refutation preserved in [tier2-design.md](tier2-design.md) §4a; the
band-structure contradiction in §3 there):

1. **Winding quantizes charge, not occupation.** Compact-U(1)
   single-valuedness around a loop gives an integer **winding number**,
   which is **charge** (the 2π vortex of
   [maxwell.md](../../../grid/maxwell.md)) — *not* photon number. The
   occupation of a mode is a different quantity that the loop topology
   does not fix. The hypothesis's central step, "integer winding ⇒
   quantized per-cycle action," conflates charge quantization with
   energy quantization.
2. **A classical linear lattice cannot quantize a free wave.** A linear
   mode at frequency ω has energy ∝ A²ω² with amplitude A a free,
   continuous parameter, so its action per cycle (∝ E/ω) can take any
   value — there is no h. Quantization into ℏω quanta is *second
   quantization* (impose [a, a†] = 1), the same de-Broglie/canonical
   input standard QM makes. The scatter rule is exactly linear
   (sim-maxwell confirmed superposition), so the dynamics carry no
   amplitude quantization for loop self-consistency to exploit.
3. **"A resonant loop at every frequency" is computationally false.**
   The Bloch band structure (`../scripts/band_structure.py`) puts the
   trapped/bound (flat-band, localized) modes **only at ω = 0 and
   ω = π**, not at a frequency-matched tower. So the
   virtual-compact-dimensions premise — a resonant loop for every
   frequency — is *contradicted*, not merely speculative.

Together: the loops are real and do real work (§4), but their
self-consistency does not, and cannot, supply the quantum.

---

## 4. What the route delivered, and what replaced it

The recirculation programme was not wholly negative — it left genuine
results that carried forward:

- the photon's **mode structure** (bands, linear dispersion ω ≈ 0.41·k);
- **spin/polarization** (the helical E ± iB Y-junction eigenmodes);
- the **α-scale leakage value** 1/129.7 (§2);
- **bound modes** (the flat-band compact-localized states).

What it could **not** deliver was the quantum itself — integer
occupation and ℏω. The project then relocated the source of quantization
*away from* loop self-consistency and *into the nodes*:

- [energy-and-coherence.md](energy-and-coherence.md) — boundedness of
  the node state (a bounded, periodic phase cell) forces E ∝ ω and fixes
  ℏ as a substrate unit;
- [countability-from-information.md](countability-from-information.md) —
  single-valuedness on a *mode's own oscillation phase* (not a spatial
  loop) as the integer-occupation candidate.

These are the productive successors; this loop route is retained only as
the record of the path not taken.
