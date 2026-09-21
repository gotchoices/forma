# Closing the loop — two lumps make a field and fall into it

**Status:** Simulation result. **Step 5c of the mechanism 3 validation plan
([STATUS.md](STATUS.md)), separate-channel branch: passed.** With the loop
closed — waves source the deflection, the deflection loads the lattice by the
linear-delay rule, the waves respond — two lumps released at rest move toward
each other, each following the ray law in the field they jointly produce, with
accelerations in inverse ratio to their masses and total momentum conserved.
Nothing in the run tells a lump to move.

Script: [`../scripts/closed_loop.py`](../scripts/closed_loop.py).
Figure: [`../outputs/closed_loop.png`](../outputs/closed_loop.png).

Grades: **[simulated]**, **[assessment]**.

---

## 1. What is closed, and what is approximated

Steps 1–4 each held one side of the loop fixed. Here neither is fixed:

- **Waves → deflection.** The deflection q obeys a wave equation sourced by the
  node-rate energy of whatever waves are present — the rest-mass form of the
  source derived from the action
  ([action-and-gamma.md](action-and-gamma.md) §4).
- **Deflection → lattice.** Each member's delay factor is 1 + q/2
  (requirement R9, [requirements-and-dof.md](requirements-and-dof.md) §7): node
  and space-link stores are both set from the local q, equally.
- **Lattice → waves.** The waves run on the canonical scatter with those stores,
  as in step 3.

Approximations, all first-order harmless and stated in the script: the source
uses its slow-lump form; the deflection propagates by a plain wave equation at
the unloaded light speed (step 4 showed the scatter carries it at light speed;
the difference is second order in q); the lumps are circulating compact modes,
so their source is steady (no breathing — requirement R10 is met by
construction, not tested). One extended dimension only, so a lump's static
deflection is a tent, linear in |x| — a constant pull rather than 1/r² — and its
uniform part rises steadily. Both are properties of one dimension, not of the
mechanism; the coupling is kept small enough that q stays well below 1.

## 2. Result [simulated]

Two lumps, masses 1 and 3, released at rest 1200 nodes apart; 7000 ticks;
deflection reaching q = 0.16 at most; the waves' norm conserved to 10⁻¹³.

| lump | moved (simulation) | moved (ray law, in the field actually produced) | ratio |
|---|---|---|---|
| 1 (mass 1) | +20.18 nodes | +20.23 | 0.998 |
| 2 (mass 3) | −6.23 nodes | −6.17 | 1.011 |

- **They fall toward each other.** Each lump sits still until the other's
  deflection front reaches it, then accelerates.
- **Each follows the ray law** — Hamilton's equations for the local spectrum —
  in the deflection the pair generated, to about 1%.
- **Action and reaction.** The source strengths are in the ratio 2.92 (mass
  ratio 3); the late accelerations in the ratio 3.22; the two lumps' wave
  momenta are equal and opposite to 0.8%.
- **The small departures are the expected strong-field corrections** and shrink
  with the field: at a quarter of the coupling (q ≤ 0.04) the source ratio is
  2.98, the acceleration ratio 3.06, the momentum imbalance 0.4%.
- **Equal masses** move symmetrically (acceleration ratio 1.000; trajectories
  ±12.93 nodes against ±12.9 predicted).

## 3. A measurement trap, recorded [assessment]

The first runs used a light, narrow packet (the defaults of step 3). Over 7000
ticks it spreads from a width of 60 nodes to about 200, its tails cross the
midpoint used to tell the lumps apart, and the measured centroids drift off the
ray law by 10–35% late in the run — while agreeing closely early on. A heavier
mode and a wider packet spread far less; with those, and a larger separation,
the agreement above is obtained. An even earlier run had the coupling ten times
too large (q reached 1.2) and is not a weak-field test at all. Neither affects
the result; both are why the script's defaults are what they are.

## 4. What this establishes, and what it does not [assessment]

**Established.** The pieces fit together dynamically and stably: a lump of wave
energy produces a deflection, the deflection slows the lattice around it, and
another lump falls into that slowing — with Newton's third law and momentum
conservation emerging from "the source is energy, and so is inertia". No
runaway, no instability, exact conservation of the waves' norm under
time-varying stores.

**Not established.**
- **Three dimensions.** A 1/r² pull between two *localized* lumps needs lumps
  that stay localized in 3D, which the wave theory here does not supply (it is
  grid-matter's open problem). Steps 2–4 cover the 3D content separately: the
  response to a gradient, and the 1/r field of a source.
- **The same-channel branch.** Here the deflection was a separate field with a
  free coupling. In the same-channel branch it is the zero-frequency part of the
  one wave, and a faithful simulation needs the exact nonlinear lattice rule —
  in particular what is held fixed when a store's weight changes (the stored
  amplitude, or its conjugate). That has to be derived from the action before it
  is simulated; an ad hoc choice would not conserve energy.
- **The source's exact form at second order** (the factor K′ and the split
  between node-rate and tension energy), which is where the few-percent
  departures at q ≈ 0.16 come from.

## Grades summary

- **[simulated]** Mutual attraction from rest; ray-law agreement 0.998 / 1.011;
  acceleration ratio → mass ratio as the field weakens (3.22 → 3.06); momentum
  balance 0.8% → 0.4%; symmetric equal-mass case; norm conserved to 10⁻¹³.
- **[assessment]** The spreading-packet trap; what remains (3D, same-channel
  rule, second-order source).
