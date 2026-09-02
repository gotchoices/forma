# Evaluating particle-binding mechanisms — a gate

The trap tests (M2·A/B/C in [results-m1-m2.md](results-m1-m2.md)) left **three
candidate mechanisms** for how GRID makes a bound particle, and no obvious way to
choose. Rather than pick, we set a **gate**: criteria any mechanism *must*
satisfy, each grounded in physics we already trust, each with a test. Then we
score the candidates honestly — including "unknown." This mirrors the shared gate
used in [grid-gravity](../../grid-gravity/).

## The gate — what a GRID binding mechanism must deliver

| # | Criterion | Why it is required | How to test |
|---|---|---|---|
| **G1** | **Maxwell preserved** | The one *confirmed* GRID result: massless, freely-propagating photons in the linear regime. Non-negotiable. | Photon still propagates at the lattice c; low-energy limit = sim-maxwell. |
| **G2** | **Single-quantum interference** | Double-slit fringes built from *individual* events — the defining quantum behaviour. Needs a genuine **phase**. | Two-slit fringe accumulates from many single instantiations. |
| **G3** | **Selective containment + persistence** | A particle stays localized and *persists*; a photon does not. | Trap test: localized object, retention→high over long time; photon control propagates. |
| **G4** | **Whole-quantum detection** | One quantum → one click (anticorrelation, Grangier–Aspect). Energy is a conserved integer count. | Single quantum → single instantiation; no multi-click. |
| **G5** | **Charge / pair structure** | Creation conserves charge; matter/antimatter as a ± label; a pair from photons nets to vacuum. | Pair creation nets zero; two species. |
| **G6** | **Mass / spectrum** | The bound object has a rest energy (gap), ideally a spectrum. | Rest-frame energy; mode spectrum vs winding/quantum number. |
| **G7** | **GRID-native (parsimony)** | Follows from existing primitives (nodes/edges/impedance scatter/compact phase) without importing foreign machinery. | Judgment: count new assumptions. |
| **G8** | **Cheaply falsifiable** | Can be simulated and killed at low cost. | Judgment: size of the build. |

## The candidates

- **I — Instantiation split.** Keep the continuous impedance scatter (waves
  disperse *and* interfere); put discreteness in a separate **whole-quantum
  instantiation** overlay. The particle is the **click** on a guide wave.
- **II — Lattice-gas.** Replace partial transmission with a conservative
  **integer/boolean collision** rule. Indivisible particles; winding clusters
  trapped by having no x-momentum.
- **III — Topological winding.** Give the compact dimension a genuine **U(1)
  phase (ℵ-line)**; the particle is a **phase winding**, stable by topology.

## Scoring (honest first pass — analysis, not yet simulated)

✓✓ strong · ✓ ok · ~ partial/unclear · ✗ fails

| | G1 Maxwell | G2 interfere | G3 contain | G4 whole-click | G5 charge/pair | G6 mass | G7 native | G8 cheap |
|---|---|---|---|---|---|---|---|---|
| **I** instantiation | ✓✓ | ✓✓ | ~ (a click is an *event*, not a persistent particle) | ✓✓ | ~ (punts charge to the wave) | ~ (mass from KK wave, not from instantiation) | ✓✓ | ✓ |
| **II** lattice-gas | ✗ (waves only in the continuum *average* → dispersion returns) | ✗ (classical gas: no single-particle self-interference) | ✓ | ✓✓ | ✓ (winding sign) | ✓ (circulation energy) | ~ (abandons the impedance scatter) | ~ |
| **III** topological | ✓ | ✓✓ (phase field is interference's natural home) | ✓✓ (soliton stable *without* focusing — protected) | ~ (topology quantizes **charge**, an integer — but not **energy**/clicks) | ✓✓ (winding ± = matter/antimatter; cleanest) | ✓ (winding energy = mass; spectrum from n) | ✓ (framework already: ℵ-line=phase, charge=winding) | ✗ (biggest build) |

## What the gate reveals: the options are complementary, not a bake-off

- **III covers G1, G2, G3, G5, G6** and gives integer **charge** quantization
  (winding number). Its one gap is **G4** — topology quantizes charge, not
  energy, so it does not by itself give whole-quantum *clicks*.
- **I covers exactly that gap: G4** (whole-quantum instantiation) plus the **Born
  rule**, on top of a wave that already satisfies G1/G2.
- **I + III together cover the entire gate:** III **binds** the persistent,
  interfering, charged, massive particle; I supplies the **whole-quantum
  detection** on top. They are not rivals — they are the *binding* half and the
  *measurement* half of one story.
- **II is dominated.** Its unique offering — field-level indivisibility — **fails
  G1 and G2** (Maxwell + single-particle interference), the very things I and III
  preserve. Its other strengths (containment, charge, mass) III already delivers
  without abandoning the impedance scatter. So II can be set aside — *unless* the
  winding-stability test for III fails, in which case II's "winding cluster has no
  x-momentum" mechanism becomes a fallback worth revisiting.

This also **corrects the earlier lean** toward I alone: the gate shows I is a
*detection* theory, not a *binding* theory — it needs III (or something) to say
what a persistent particle **is**.

## The decisive, cheap test before any big build

The whole I+III conclusion rests on **one unverified assumption**: that a
**topological winding is actually stable on the GRID impedance-scatter lattice**
(G3 for III). Everything else in III's column is standard phase-field physics;
this is the GRID-specific risk. So the next experiment is the **minimum** that
tests it:

1. **Minimal 2-component (phase) field on the existing cylinder.** Carry a
   complex/2-component amplitude per edge instead of a real one; the impedance
   scatter acts on each component. Cheapest possible U(1).
2. **Winding-stability test (G3):** initialize a **unit phase-winding** localized
   in x. Does it **stay localized and persist** (linear *and* with the bound), or
   disperse like the real-scalar mode did?
3. **Photon control (G1):** the n=0 mode still propagates at c.
4. **Interference smoke test (G2):** two phase-coherent sources still beat/fringe.

If the winding is stable → I+III is the path, and the instantiation overlay (I)
comes next for G4/Born. If the winding disperses too → topology alone is not
enough on this lattice, and II (indivisible-particle dynamics) returns as the
fallback for G3. Either way the gate, not a guess, decides.

## Status

Gate defined; first-pass scoring done (analysis). **II set aside (dominated).**
Phase-field winding test **run** ([phase-winding-results.md](phase-winding-results.md)):
III's winding is **topologically protected and localized** but **immobile** (a
flat-band state — speed 0 at every momentum) on the **1D-ring** cylinder, so it
is **not yet a genuine particle**. Diagnosis: the 1D ring is too simple (a flat
massive band = infinite mass). **Next: the 2D-torus compact dimension** — does a
winding there acquire finite mass and *move*? If not, II returns as fallback.
