# Mechanical readings of the requirements — no memory, a rigid ring in elastic space

**Status:** Interpretation note. It re-reads the requirements and posits of
mechanism 3 ([requirements-and-dof.md](requirements-and-dof.md),
[sync-carrier-mechanism.md](sync-carrier-mechanism.md)) in the language of a
mechanical lattice, where several things that looked awkward in the register
description — a memory at each node above all — turn out to be ordinary. Nothing
here changes a result; it changes what the results are pictures *of*. The
register scatter remains the right way to *compute* (it is exact and unitary); a
mechanical lattice is the right way to *picture* the statics.

Grades: **[reading]** (interpretation, consistent with the results),
**[standard]** (textbook mechanics), **[open]**.

---

## 1. "Memory" was an artifact of describing statics with rates [reading]

The scatter's registers carry travelling amplitudes — *rates*. A static
deformation is the time-integral of a rate, so in the register description it
appears as a running sum a node must keep (requirement R7). A mechanical lattice
has a position-like degree of freedom already: each node simply *is* where it
is. A stretched spring does not remember having been stretched; it is stretched.
Nothing stores anything, and nodes and edges interact only in the moment.

Step 4 already showed this ([switch-on-result.md](switch-on-result.md)): behind
the front the node rate returned to zero while the links held a static 1/r²
tension with no memory element at all. The only "memory" was the deflection q —
the node's static displacement.

**R7, restated:** *each node has a deflection that persists.* A mechanical lattice
supplies it for free.

## 2. The other requirements, in the same picture [reading + standard]

| requirement | register wording | mechanical reading |
|---|---|---|
| R4 / P4 (dead band) | no preferred rate; only differences from neighbours matter | nodes joined to their neighbours by springs and **not anchored to any background**. Anchoring springs are the on-site term that turns 1/r into a short-range Yukawa field. A lattice that *is* space has nothing to anchor to. |
| R1, and "remove the load and it relaxes" | lossless; relaxation by radiation, not by leak | a spring lattice: remove the point force and it springs back, the deflection leaving as a wave (step 4's switch-off) |
| R2 / P1 (no master clock) | equal transit times; junctions fire on arrival | passive junctions of equal lines; the tick is a transit time; nothing to synchronize — and the same absence of an external reference as R4 |
| R5 (equal loading of nodes and space links) | impedance unchanged, no reflection | general relativity's static field of a rest mass, transcribed ([tensor-extension.md](tensor-extension.md) §2) |
| R6 / P7 (compact loop loaded once) | a clock's circulation is not slowed by space-link storage | the compact ring is **rigid — held by the embedding space** — so a load on it is passed into S rather than stretching c (§3) |
| R8 / P5 (rate follows deflection, not tension) | potential, not gradient | a node's own displacement, not the strain of the springs around it |

## 3. The source: back-pressure of trapped light [reading]

A photon circulating in a ring pushes outward on the ring — radiation pressure on
a curved mirror. If the ring's circumference is held fixed by the embedding
space, that push is transmitted into the adjacent space links as a **static
stress**: proportional to the trapped energy, always outward, always the same
sign. That is the gravitational source with the properties the action derived
for it ([action-and-gamma.md](action-and-gamma.md) §4) — and it is a *causal*
account of where the source comes from, not a coupling constant.

It was found twice. Reading general relativity's linearized equations in lattice
variables ([tensor-extension.md](tensor-extension.md) §4), the rule that
reproduces them feeds each space link by the energy flowing along it *plus an
equal share of the rest energy at the node, whatever the link's direction* — which
is trapped radiation pressing equally on everything that confines it. The
mechanical picture and the field equations say the same thing.

This also gives P7 its mechanism: **rigid ring, elastic space.** The push goes
into S, not into c, because c is held.

## 4. The response: one nonlinearity, source and reaction together [reading + open]

Back-pressure explains why a particle *produces* stress. It does not by itself
explain why stress *slows* waves, with the right sign. Here the action closes
half the gap: in the one-field form
([same-channel-result.md](same-channel-result.md) §1) the source and the
response are a single nonlinearity K(q). If the field's inertia depends on its
static deflection, the wave both sources q (through K′) and is slowed by q
(through K); the two cannot be had separately. So the **one physical posit** of
the static sector is that nonlinearity — a lattice that *softens under load*.

For the link half (light) there is a suggestive sign argument **[standard]**: in
a pre-tensioned string lattice the wave speed is √(tension / mass per length).
Space pushing *inward* on a particle's surface puts the adjacent links in
compression, lowering their effective tension; waves there are slower. That is
the right sign, and it is the acoustoelastic effect — wave speed depends on
stress — which every real material shows.

For the node half (clocks) — the junction's effective inertia rising under load —
there is no mechanical story yet. **[open]** This is the one genuine gap in the
static sector's *causal* chain.

**Status of this gap (decided 2026-10-02).** It is interpretive, not blocking.
The behaviour is now an explicit posit — P9, "the field softens under load" — and
every static result follows from it through the action. Note also that the
*direction* is not separately at risk: in the action the response goes as K′², so
any dependence of inertia on deflection gives attraction, whichever sign it has.
The "compression usually stiffens" worry applies only to a particular mechanical
story (back-pressure → stress → slowing), not to the posited rule. A mechanism
would buy economy (e.g. a pre-tensioned net that particles relax locally, which
might turn the node and link halves into one effect), not validity.

## 5. The causal chain, as it now stands

| link in the chain | status |
|---|---|
| particle → static stress ∝ energy, one sign | mechanistic (back-pressure); derived from the action |
| stress spreads at c; tension 1/r², deflection 1/r | mechanistic (junctions divide it, nothing lost); measured (step 4) |
| stress slows everything alike | derived (step 1) |
| stress slows waves at all, right sign | **posited (P9)** — softening under load; sign follows from the action; string-tension reading for links, none for nodes (optional) |
| nodes and links loaded equally (full light bending) | GR's static solution; "rigid ring, elastic space" |
| only two polarizations radiate | **missing** — a local re-timing / re-labelling symmetry |

## 6. Two pictures, one model

The register model and the stress model are the same model seen from two ends.
The register scatter is exact, unitary and computable; it describes the *rates*.
The mechanical lattice — springs between unanchored nodes, rigid compact rings
pressing on them, a medium that softens under compression — describes the
*statics*, and it is where the causal reading lives. Neither replaces the other.

## Grades summary

- **[reading]** Memory → static deflection; unanchored lattice → massless field;
  rigid ring → P7; back-pressure → source; softening → response.
- **[standard]** Anchoring springs give a Yukawa field; radiation pressure on a
  curved mirror; wave speed in a string; acoustoelasticity.
- **[open]** A mechanical account of the node half of the response (clocks
  slowing); the local symmetry of the dynamic sector.
