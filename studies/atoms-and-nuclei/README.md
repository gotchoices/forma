# R29. Atoms and nuclei — from T⁶ modes to multi-body physics

**Questions:** Q28 (photon absorption / energy levels), Q16
**Type:** theoretical + compute  **Depends on:** R27, R15, R19
**Status:** Active


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


### Track 1 — KK reduction: from 9D to Coulomb

**Goal:** Show that the T⁶ × R³ wave equation reduces to
4D electrodynamics with α = 1/137.

**Method:**
1. Write the scalar wave equation on T⁶ × R³:
   (Δ_R³ + Δ_T⁶) ψ = −(ω/c)² ψ
2. Expand ψ in T⁶ eigenmodes: ψ(x,θ) = Σ_n f_n(x) φ_n(θ)
3. Each T⁶ mode gives a 4D field with mass m_n = E_n/c²
4. The zero mode (n = 0) is massless → mediates 1/r potential
5. Massive modes give Yukawa corrections ~ exp(−m_n r)/r

The coupling constant between two charged modes (electron
and proton) via the zero-mode exchange is α.  Compute it
from the T⁶ geometry and verify α = 1/137.

Also compute the leading Yukawa correction at the Bohr
radius (0.53 Å).  The dominant correction comes from the
lightest massive KK mode.  If the correction depends on
r_e (the last free parameter from R15), this could
constrain r_e.

**Deliverable:** V(r) for the electron-proton system,
decomposed into Coulomb + Yukawa corrections.  Verification
that the Coulomb coupling matches R19.

**Addresses:** OQ1 (mode-mode interaction), OQ2 (T⁶-R³
shears as gauge fields).


### Track 2 — Hydrogen from T⁶ geometry

**Goal:** Derive the hydrogen ground state energy from
the T⁶ × R³ model.

**Method:**
1. Use V(r) from Track 1 as the electron-proton potential
2. Solve the radial Schrödinger equation for the bound state
3. Compare: E₁ = −13.6 eV?  a₀ = 0.53 Å?

If V(r) = −α ℏc/r exactly, this is textbook QM — the result
is guaranteed.  The value is in showing the chain:
T⁶ geometry → particle charges → Coulomb → hydrogen.

If the Yukawa corrections from Track 1 are nonzero, solve
with the full V(r) and report the deviation from 13.6 eV.

**Deliverable:** Hydrogen binding energy derived from
compact-dimension geometry.

**Addresses:** OQ5 (energy levels from 9D).


### Track 3 — The r_e constraint from atomic spectra

**Goal:** Determine whether the hydrogen spectrum depends
on r_e (electron aspect ratio) and, if so, pin its value.

**Method:**
The Yukawa corrections from Track 1 depend on the T⁶
circumferences, which depend on r_e.  For different values
of r_e, compute:
1. The shift in hydrogen ground state energy
2. The shift in the Lamb shift (2S₁/₂ − 2P₁/₂)
3. The shift in fine structure

Compare to measured precision (~10⁻¹² for the 1S-2S
transition).  If the Yukawa corrections are large enough
to be constrained by experiment, r_e is determined.

**Deliverable:** r_e constraint from atomic spectroscopy,
or a finding that the corrections are too small to measure.

**Addresses:** The α problem (R15) — r_e is the last
undetermined parameter.


### Track 4 — Mode census of the gauge sector

**Goal:** Enumerate the gauge fields that emerge from T⁶.

**Method:**
The KK reduction of T⁶ gives up to 6 independent U(1)
gauge fields (one per compact dimension).  The physical
electromagnetic field is a specific linear combination:
A_μ^EM = −A_μ^1 + A_μ^5 (from Q = −n₁ + n₅).

Questions:
- What are the other 5 gauge fields?  Do any correspond
  to known forces (weak, strong)?
- What are the masses of these gauge bosons?  (If they
  acquire mass from the T⁶ geometry, they are short-range.)
- Does the neutrino sector (A_μ^3, A_μ^4) produce a force
  that could explain nuclear binding?

**Deliverable:** Classification of the T⁶ gauge sector.

**Addresses:** OQ6 (nuclear binding mechanism).


### Track 5 — Deuterium binding

**Goal:** Determine whether the T⁶ geometry produces
nuclear binding.

**Method:**
The proton mode (0,0,0,0,1,2) and neutron mode
(0,−2,1,0,0,+2) share proton-sheet quantum numbers.
Their interaction may include:
- Coulomb repulsion (if both charged — but neutron is
  neutral, so V_EM = 0)
- Non-EM gauge forces from Track 4 (neutrino-sector
  gauge fields?)
- Direct overlap in the compact dimensions at nuclear
  separations (~2 fm ≈ L₆, the proton ring circumference)

At separations comparable to the T⁶ size, the KK reduction
breaks down and the full 9D structure matters.  This is
where the "9D solver" is truly needed.

**Deliverable:** p-n interaction potential at nuclear scales.
Comparison to 2.224 MeV (deuterium binding energy).

**Addresses:** OQ6 (nuclear binding), OQ7 (neutron stability).


### Track 6 — Nuclear stability  *(deferred)*

Why a neutron in a nucleus doesn't decay.  Requires Tracks
4–5 results.


### Track 7 — Hydrogen energy levels  *(deferred)*

Full hydrogen spectrum, fine structure, Lamb shift.
Requires Track 2–3 results.


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

Scripts go in `atoms-and-nuclei/scripts/`.


## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R27   | Single-mode T⁶ spectrum; pinned parameters |
| R19   | Shear-charge mechanism → α formula; the source of EM |
| R15   | The α problem → r_e undetermined; Track 3 may solve it |
| R26   | T⁶ framework, metric infrastructure |
