# Containment achieved — a stable, mobile Q-ball from focusing+saturating

> **Provenance / honest status.** The Q-ball is **Coleman's** (1985) — textbook
> non-topological soliton physics; **no new physics was derived here**, and this
> sim is a **continuum PDE with a *posited* cubic-quintic potential — it bypasses
> GRID's scatter/lattice entirely.** Its value was diagnostic: it isolated that
> forma's universal gap is a *focusing* nonlinearity. The GRID-native follow-up —
> deriving that GRID's compact phase (ℵ-line) is *intrinsically* focusing — is in
> [focusing-from-phase.md](focusing-from-phase.md), which supersedes this as the
> load-bearing result.

**The first dynamical demonstration of particle containment in forma.** Sim:
[`../scripts/soliton_test.py`](../scripts/soliton_test.py). Figure:
[`../outputs/soliton_qball_rest.png`](../outputs/).

## Context

Every prior dynamical containment test in the repo dispersed or froze — the
grid-matter 1D cylinder (7 mechanisms), R24's 2D-torus wave sim, sheet-proton's
2D clover. The obstruction named everywhere was a **missing focusing (attractive)
nonlinearity**. forma had tried the *saturating* half alone (defocusing: clip,
value-bound) and pure nonlinearities that disperse (R24) or repel (R15 Coulomb),
but **never the standard stable-soliton recipe: focusing + saturating together**.

## The test

A clean **complex relativistic (nonlinear Klein-Gordon)** field in 1D — faithful
to GRID (2nd-order/relativistic, a mass gap like KK, a conserved U(1) charge
Q = the winding/charge) — decoupled from the scatter lattice so we test the
*mechanism*, not lattice artifacts:

    phi_tt = phi_xx - ( m^2  - 2 g |phi|^2  + 3 q |phi|^4 ) phi
                        mass    FOCUSING(g)   SATURATING(q)

## Results

| case | g | q | outcome |
|---|---|---|---|
| linear | 0 | 0 | **DISPERSES** (width ×3, peak decays) — the baseline |
| focusing only | 1 | 0 | **COLLAPSES / blows up** (→ nan) — no stabilizer |
| **focus + saturate** | 1 | 0.3 | **STABLE, localized, charge-conserving** |

The focus+saturate lump sheds an initial radiation halo, then **contracts to a
tight core (rms width ~8) and holds it out to 8000 steps**; peak |phi|^2 steady at
~1.68; charge Q conserved to ~2%. A **Q-ball**.

**Mobility (the make-or-break the flat-band winding failed):** boosted (`--kx`),
the Q-ball **translates as a coherent charged lump** — centroid moves, core peak
|phi|^2 stays ~1.7, charge conserved (kx = 0.1–0.2). At large boost (kx = 0.4) it
starts shedding, but the core survives. Unlike the winding (speed = 0.000, frozen),
this particle **moves and carries momentum**.

## What this establishes (and what it does not)

- **Containment is possible.** "Particle = a stable, mobile, localized, charge-
  carrying contained wave" is now **demonstrated dynamically**, not asserted. The
  seven prior negatives were not evidence against the contained-wave picture —
  they were the absence of the **focusing+saturating** nonlinearity. The user's
  instinct ("a wave on a sheet is a strong candidate for a particle") holds.
- **This is realist, not Copenhagen.** The Q-ball is a real, always-localized,
  simulable object. Born would be *derivable* (energy density ∝ |phi|^2), not
  assumed. It needs no observer and no collapse. It is the opposite of "no locality
  until observed."
- **What is NOT shown: that GRID supplies this nonlinearity.** This used a *posited*
  cubic-quintic potential. Everything GRID has been shown to provide so far is
  **defocusing/repulsive** (saturation-clip, Coulomb self-energy). So the whole
  binding question now sharpens to one crux:

> **Can the GRID substrate produce a FOCUSING (attractive) self-interaction —
> focusing at low amplitude, saturating at high amplitude? If yes, particles are
> Q-balls and containment is solved. If GRID is fundamentally defocusing, the
> contained-wave picture cannot be realized on it, and something else (mechanism I)
> must carry locality.**

## Gate impact

**G3 (containment + persistence + mobility) is SATISFIABLE** — by a Q-ball, given
focusing+saturating. It also naturally carries **G5 (charge, conserved Q; ±Q =
particle/antiparticle)** and **G6 (mass/spectrum: Q-balls have a mass–charge
relation)**. The contained-wave (call it mechanism **IV**) now dominates II and
competes with I+III — *conditional on GRID sourcing the nonlinearity*.

## Next

1. **The crux experiment:** does any GRID-native process give an *attractive*
   self-interaction? Candidates to examine: mode–mode coupling on a saturating
   substrate below the clip (does second-order coupling come out attractive?);
   the metric/strain response with the *right* sign; back-reaction through the
   compact dimension. This is now the central question.
2. **Q-ball ↔ winding:** the Q-ball's conserved charge Q should be identified with
   the ℵ-line **winding number** (mechanism III) — unify the contained-wave with
   the topological charge. Test a Q-ball built on a phase-winding field.
3. **Born from the Q-ball:** detection ∝ |phi|^2 energy density — the M4 route,
   now on a genuinely localized object.
