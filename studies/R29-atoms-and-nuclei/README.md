# R29. Atoms and nuclei — from T⁶ modes to multi-body physics

**Questions:** Q28 (photon absorption / energy levels), Q16
**Type:** theoretical + compute  **Depends on:** R27, R15, R19
**Status:** Complete (4 tracks, 27 findings)


## Motivation

R27 showed that the T⁶ compact space accounts for the
single-particle spectrum with zero free parameters at MeV
scale.  But nature is not isolated particles — atoms exist,
nuclei are stable, electrons occupy discrete energy levels.

This study bridges single-mode T⁶ physics to multi-body
systems.  The central question: does the T⁶ geometry that
predicts particle masses also predict their interactions?


## The dimensional picture

| Dims | Space | What lives there | Status |
|------|-------|-----------------|--------|
| 6 | T⁶ (compact) | Particle identity: mass, charge, spin | R27: solved |
| 3 | R³ (spatial) | Positions, separation, binding | This study |
| 1 | R¹ (time) | Dynamics, decays, transitions | Deferred |
| **9** | **T⁶ × R³** | **Static multi-body** | **Minimum for atoms** |
| 10 | T⁶ × R³⁺¹ | Full dynamics | Future |


## Key insight: the gauge field IS the geometry

In Kaluza-Klein theory, the 4D electromagnetic potential
A_μ is the off-diagonal metric component g_{μi} between
extended (μ) and compact (i) dimensions.  The full 9D
metric has the structure:

    ┌             ┐
    │  g_R³    A  │
    │   Aᵀ   G_T⁶│
    └             ┘

where G_T⁶ is the compact metric from R27, g_R³ is flat
Euclidean, and A is a 3×6 block encoding gauge fields.

A charged T⁶ mode at position x₀ in R³ generates nonzero
A(x), which is the Coulomb potential.  Another mode at x₁
feels this field.  The Coulomb interaction emerges from the
9D geometry — it is not assumed separately.

R19 derived the coupling constant: α = 1/137 from the
shear mechanism on T².  R29 must show that this same α
governs the inter-particle interaction.


## Approach — tracks ordered by computability

Structure is flexible.  Early tracks address computable
prerequisites; later tracks tackle deeper conceptual
problems.  New intermediate tracks may be inserted as
earlier results clarify the path.

### Guiding principle: geometry predicts, theories explain

The neutron was not predicted by an intermediate theory of
proton-electron binding — it was found directly as a T⁶
mode.  We adopt the same posture throughout R29:

- **We use the T⁶ solver to search for modes that match
  observed composite systems** (nuclei, atoms).
- **Intermediate theories** (KK gauge fields, Coulomb, QM)
  are useful for building intuition and cross-checking, but
  we do not require them.  If a T⁶ mode at 1876 MeV with
  Q = +1, S = 1 exists, that IS the deuteron, regardless of
  whether we can derive the nuclear force.
- **Predictive power comes from the geometry**, not from
  any particular reduction framework.


### Track 1 — KK reduction: from 9D to Coulomb  ✔ Complete

**Result:** Coulomb 1/r potential emerges from the zero-mode
gauge field.  α = 1/137 verified from R19 shear on both
electron and proton sheets.  Six U(1) gauge fields identified,
including a proton-tube gauge boson (52 MeV, 3.8 fm range)
as a nuclear force candidate.

See findings F1–F8.


### Track 2 — Hydrogen from T⁶ geometry  ✔ Complete

**Result:** E₁ = −13.6 eV and a₀ = 0.53 Å reproduced from
the Coulomb term.  Yukawa corrections from KK massive modes
are orders of magnitude too large under the naive uniform-
coupling assumption — indicating that the simple KK gauge
picture does not hold quantitatively.  The tension
(F11–F14) motivates the direct-mode approach adopted in
subsequent tracks.

See findings F9–F15.


### Track 3 — Light nuclei as T⁶ modes

**Goal:** Search for T⁶ modes that directly reproduce
observed nuclear systems, without assuming any intermediate
force theory.

**Rationale:** The neutron was discovered as a T⁶ mode, not
derived from a proton-electron force.  Nuclei may follow the
same pattern — a deuteron might be a single oscillation
in the T⁶ compact space, not two particles bound together.

**Method:**
1. Search for modes matching the deuteron (1875.6 MeV,
   Q = +1, S = 1), helium-3 (2808.4 MeV, Q = +2, S = 1/2),
   helium-4 / alpha (3727.4 MeV, Q = +2, S = 0), and
   other light nuclei.
2. If matches are found: compare predicted vs observed mass,
   assess whether the binding energy (mass deficit) emerges.
3. If NO matches: this is also informative — it means nuclei
   are genuinely multi-mode objects and require the R³
   interaction framework.

**Deliverable:** Catalog of nuclear T⁶ mode candidates,
or evidence that nuclei are not single T⁶ modes.

**Addresses:** OQ4 (multi-particle states), OQ6 (nuclear
binding).


### Track 4 — r_e from nuclear masses, stability, and atoms

**Goal:** Constrain r_e using the nuclear mode pattern,
test whether the model predicts nuclear stability, and
determine whether atoms are T⁶ modes or R³ phenomena.

**Method:**
1. **r_e sweep:** The nuclear scaling law (F16) uses n₂
   (electron ring winding) as an optimization parameter.
   The optimal n₂ depends on L₂, which depends on r_e.
   Sweep r_e = 1–20 and compute total nuclear mass error
   across all nuclei.  The minimum pins r_e.
2. **Valley of stability:** For each A = 1–30, compute
   mode energy for all Z and find the energetically
   preferred isotope.  Compare to observed stable nuclei.
3. **Atom test:** Atomic binding energy (~13.6 eV) is
   ~10⁻⁵ MeV.  Confirm this is below T⁶ energy
   resolution, establishing that atoms require R³.

**Deliverable:** r_e constraint from nuclear data; valley
of stability prediction; atoms vs nuclei in the T⁶
framework.

**Addresses:** R15's α problem (r_e), OQ6 (nuclear
stability).


### Track 5 — Helium and multi-electron atoms *(deferred)*

Helium atom = ⁴He nucleus (T⁶ mode) + 2 electrons bound
via Coulomb in R³.  Requires Track 1 Coulomb result plus
electron-electron repulsion.


### Track 6 — Electron energy shells *(deferred)*

Energy levels from the Coulomb potential.  The leading term
gives standard hydrogen levels (Track 1).  Fine structure
and Lamb shift require understanding why the KK boson
corrections from Track 2 are suppressed.


### Track 7 — Full atomic spectrum  *(deferred)*

Fine structure, Lamb shift, isotope shifts.  Depends on
Tracks 5–6.


## Open questions

Preserved from the initial framing.  Each is tagged with
the track most likely to address it.

| # | Question | Track |
|---|----------|-------|
| OQ1 | How do T⁶ modes interact in R³? | T1 |
| OQ2 | Are T⁶-R³ shears the gauge fields? | T1 |
| OQ3 | When does time (10D) enter? | Deferred |
| OQ4 | What is a two-particle state in T⁶ × R³? | T1-T2 |
| OQ5 | Does 9D expose electron energy levels? | T2-T3 |
| OQ6 | Nuclear binding without nuclear force? | T4-T5 |
| OQ7 | Why doesn't n decay in a nucleus? | T6 |


## On the question of a 7D (T⁶ × R¹) solver

A 1D spatial simplification is tempting but has a
fundamental limitation: the Coulomb potential in 1D is
NOT 1/r — it is |x| (linear confinement).  A 7D solver
would demonstrate binding and measure the coupling strength,
but would not reproduce hydrogen energy levels.

However, the coupling constant α is a property of the T⁶
geometry, independent of the spatial dimensionality.  So a
7D computation could still determine α without getting the
right energy spectrum.  This makes it a useful diagnostic
but not a substitute for 3D.

**Recommendation:** Begin with the KK reduction (Track 1),
which extracts α analytically without building a numerical
PDE solver.  If a PDE solver becomes necessary (Track 5,
nuclear binding), build it in 3D from the start.


## Infrastructure

### Existing tools (do not modify)
- `lib/t6.py` — T⁶ metric, mode energies, charge, spin
- `lib/t6_solver.py` — discovery engine, self-consistent metric

### New module: `lib/t6r3.py`
Multi-mode interaction library.  Imports from `lib/t6.py`
for the compact-dimension part and adds:
- KK mode decomposition of the T⁶ × R³ Green's function
- Effective 4D interaction potential V(r)
- Yukawa correction calculator
- (Later) Schrödinger solver for bound states

Scripts go in `R29-atoms-and-nuclei/scripts/`.


## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R27   | Single-mode T⁶ spectrum; pinned parameters |
| R19   | Shear-charge mechanism → α formula; the source of EM |
| R15   | The α problem → r_e undetermined; Track 3 may solve it |
| R26   | T⁶ framework, metric infrastructure |
