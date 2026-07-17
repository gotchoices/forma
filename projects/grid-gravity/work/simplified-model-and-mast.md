# The simplified model vs. real MaSt — and how the reasoning generalizes

**Status:** Scoping / reasoning note. Situates this project's simplified
model against the full Material-Space-Time (MaSt) manifold, states which
conclusions are robust under dimensional generalization and which must be
re-derived in the full 10/11D, 2D-sheet setting. Keeps the simplification in
context as the work proceeds.

---

## 1. What the simplified model assumes

| Element | This project (simplified) | Real MaSt |
|---|---|---|
| Compact geometry | a **1D** loop (one cycle) | **2D sheets** (tori); 6 compact dims = 3 sheets (Ma_e, Ma_ν, Ma_p) |
| Particle | a standing wave / loop-constraint | a 2D-sheet mode (knot; windings on *two* cycles) — [metric-mass](../metric-mass/), [metric-charge](../metric-charge/) |
| What emerges | **mass only** | mass **and** charge |
| Spreading medium | 2D hex lattice (for the sims) | 3D space S + 1D time |
| Source | a static scalar loop-constraint | a dynamic sheet with internal (hexagonal) structure |

The compact **sheet itself is a hex lattice** (a 2D triangular lattice
wrapped to a torus — [compact-dimensions.md](../../grid/compact-dimensions.md)),
so a real mass is a mode with its own internal hexagonal circulation, not a
bare 1D loop.

## 2. Why the simplification is well-matched to gravity (not a crude cut)

Two structural facts make the 1D reduction the *right* one for gravity:

- **1D ⇒ mass-only.** Charge requires circulation **synchronized between the
  two dimensions of a sheet** (the closure condition; [metric-charge](../metric-charge/)).
  A single compact dimension cannot synchronize, so it yields **mass but no
  charge**. The 1D-compact model is therefore exactly the *mass-only*
  regime — precisely what gravity couples to. It excludes charge (this
  project's stretch slot) *by dimensional restriction*, cleanly.
- **Gravity is universal.** It couples to total energy, independent of which
  sheet, which winding, or charged-vs-neutral. So enriching the compact
  structure (1D → 2D sheet → multiple sheets in 10/11D) changes particle
  *identity* but should leave the gravity *mechanism* unchanged. This is the
  reason to expect the simplified-model results to carry over.

## 3. The mass/charge distinction *is* the source-character fork

The open question from [loops-and-range.md](loops-and-range.md) — does the
detour source on the mass's *scalar energy* (→ gravity) or its *winding*
(→ charge)? — is answered by MaSt's own structure:

- **mass = the standing-wave energy**, present for *any* configuration
  (charged or neutral);
- **charge = the *synchronized* winding** (closure met).

So gravity sources on the **scalar energy**, and it is universal *because
every standing wave carries energy regardless of whether its winding
satisfies charge-closure* — which is exactly why neutral particles gravitate.
The scalar-vs-winding fork is not merely consistent with MaSt; it **is** the
mass-vs-charge distinction. This retires the source-character question in the
model's favour (given the energy is presented as a scalar — see §5).

## 4. Same type, different roles — no conflation

The compact-sheet loops and the spatial hexagon loops are the same *kind* of
object (closed 1-cycles carrying a phase-closure constraint), but their
**roles differ**:

- **compact-sheet hexagons** host the mass (the source);
- **spatial hexagons** spread the effect (the lattice Green's function);
- the **shared node** couples the two.

The loop-size-independence result ([loops-and-range.md](loops-and-range.md))
is a statement about the *source*: whatever the compact loop's scale, it
spreads the same 1/r spatially. It does **not** equate where the mass lives
with the medium it spreads through. (A real mass, being a 2D-sheet mode with
internal hex circulation, is a *richer* source than a 1D loop; universality
says only its total energy should matter for the far-field spreading, but see
§5.)

## 5. Robust vs. needs-re-derivation in full 10/11D

**Robust (expected to carry over, on universality):**
- The **gravity mechanism**: scalar energy → spatial lattice Green's function.
  Universal, independent of the compact structure.
- The **1/r spreading**: a property of the spatial lattice operator, blind to
  the compact dimensions.
- The **scalar-vs-winding** separation (gravity vs charge) = mass vs charge.
- The **loop-unification** (all cycles are 1-cycles).

**Must be re-derived in the full setting (do not assume):**
- **Non-dispersivity.** The [detour-refractive.md](detour-refractive.md) §3
  argument used a *single* resonance ω_Compton. A 2D sheet has a **mode
  spectrum**; the detour delay is non-dispersive only for ω below the lowest
  sheet mode and may disperse near sheet resonances. Re-derive with the
  spectrum.
- **The coefficient (optional).** ζ is fixed by the *sheet* geometry (2D
  triangular → ζ = 1/4); the 1D-hex sims here implicitly sat near ζ ≈ 1/3.
  The *precise* coefficient (→ G = 1/(4ζ) / the PV form) is **not a validity
  gate** — G's value is largely a unit, and [grid/gravity.md](../../grid/gravity.md)
  does not predict it either (ζ = 1/4 is calibrated). What is needed is only
  that the coupling be a fixed constant ∝ mass-energy, consistent in
  direction/order with 1/(4ζ). Deriving the exact factor in the real
  dimensional context is a consistency bonus.
- **Source character, rigorously.** §3 argues the energy is presented as a
  scalar; confirming that the 2D-sheet mode (with internal structure)
  presents its energy to the shared node as a scalar source — rather than
  leaking winding — is the honest version of the §3 claim, and belongs in the
  full-sheet setting.

## 6. Implication for chapters

The simplified model is a legitimate **teaching / derivation ladder** for
gravity — the same posture [metric-mass](../metric-mass/) takes ("not
claiming 2+1D is fundamental — it's a teaching ladder"). A chapter arc may
build gravity on the simplified model, provided it:
1. states the reduction explicitly (this note), and
2. flags the two full-dimensional re-derivations (non-dispersivity with a
   mode spectrum; the coefficient with the sheet's ζ) as the bridge to real
   MaSt.

So the simplified results stand as the mechanism's *skeleton*; the full-D
work is the *calibration and spectrum check*, not a re-foundation.
