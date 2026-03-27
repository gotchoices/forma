# R31. The origin of α and the nature of atomic binding

**Questions:** Q34 (what selects α), Q28 (photon absorption), Q18 (deriving α)
**Type:** theoretical + compute  **Depends on:** R19, R26, R27, R29, R30
**Status:** Complete


## Motivation

The T⁶ model takes α = 1/137 as an input.  Given any r > 0.26,
the shear formula α(r, s) is solved for s, and the geometry is
built.  This is circular: any α works.  But nature picks ONE
value.  Something in the geometry must select it.

The circularity is visible in R30's α sweep (F22): sweeping s
and computing hydrogen with Yukawa corrections, the perturbation
grows monotonically with α.  No "sweet spot" emerges.  Atoms
are stable for ALL α > 0 (in non-relativistic QM), so atom
stability alone cannot pin α.

Simultaneously, R29 dissolved the nuclear force by showing
nuclei are T⁶ modes.  This raises the same radical question
about atoms: is the electron-proton relationship really a
Coulomb force across R³?  Or could it be a T⁶ phenomenon?
The neutron already answers one version: when electron and
proton windings merge in T⁶, you get a neutron — not a
hydrogen atom.


## The problem

The model currently has a circular structure:

    Input α → solve for s → build geometry → verify α

Any α works because we're only computing kinematics (spectra).
The dynamics (what selects the geometry) are missing.

To predict α, we need to break this circle with an independent
constraint on s.  Possible approaches:

1. **Geometric principle** — the T⁶ vacuum energy (Casimir)
   or some other functional of the geometry has a minimum
   at specific s values.

2. **Observable constraint** — a precision measurement
   (Lamb shift, proton charge radius, g−2) pins r_e, and
   α follows from α(r_e, s_e).

3. **Full 9D self-consistency** — solve the electron-proton
   system on T⁶ × R³ without KK reduction; the effective
   coupling that emerges IS α.


## Key prior results

- **R19:** α(r, s) formula.  Every r > 0.26 has a self-consistent
  s.  The product r²s² → 0.00465 at large r.

- **R26 F73:** Casimir energy (cross-shears) wants maximal
  coupling; mass spectrum wants minimal.  This tension could
  select cross-shear values.  Not yet extended to within-plane
  shears (which determine α).

- **R29:** Nuclei are T⁶ modes.  Atoms are NOT (two-tier
  physics).  The Coulomb potential derives from KK reduction.
  Yukawa corrections from KK massive modes are problematic
  at r_e = 6.6 (~7–9% of Coulomb binding).

- **R30 F23:** Atom existence requires r_e < 68.5 (Bohr radius
  must exceed tube circumference).  Combined with R19:
  0.26 < r_e < 68.5.

- **R30 F24:** If the Yukawa calculation is correct, hydrogen
  spectroscopy pushes r_e < ~2 (open tension with R29).


## Context for the questions

### Why atoms don't pin α

In quantum mechanics, atoms are stable for ALL α > 0.  At
larger α: tighter orbit, stronger binding.  At smaller α:
wider orbit, weaker binding.  The electron never "falls in"
(quantum uncertainty prevents it) and never "flies away"
(any attraction creates a bound state).  Atoms only fail
at α > 1 (Dirac threshold for Z = 1), far from 1/137.

So "atoms must exist" requires α < 1 — not α = 1/137.
The specific value of α determines the SIZE of atoms and
the richness of chemistry, but not their existence.

### Was deriving hydrogen tautological?

Partially.  The NON-tautological result (R29 Track 1): the
T⁶ × R³ geometry produces a 1/r Coulomb potential via KK
reduction.  This explains WHY there's an inverse-square force
— it's a consequence of the compact geometry, not a postulate.

The tautological part: once V = −α/r with α input, the
hydrogen spectrum (E₁ = −13.6 eV) follows from standard QM.
We proved the mechanism, not the number.

### The neutron as "merged" electron + proton

The neutron mode (1, −2, 1, 0, 0, 2) has both electron-tube
(n₁ = 1) and proton-tube (n₅ = 0, but n₃ = 1 for spin)
windings.  It IS an electron+proton merged in T⁶:

- Hydrogen (R³ binding): separate modes, 938.783 MeV total
- Neutron (T⁶ merger): single mode, 939.565 MeV

The atom is 0.8 MeV LIGHTER than the neutron.  This explains:
- Hydrogen is stable (lower energy than neutron)
- Free neutrons decay (higher energy → p + e + ν̄)
- Atoms don't collapse into neutrons (need 0.8 MeV to merge)


## Approach — tracks

### Track 1 — Is the atom a T⁶ mode?  **Complete**

Search for T⁶ modes near hydrogen mass (938.783 MeV) with
Q = 0, spin = ½.  **Result:** NO.  Closest mode is 661,354 eV
away — 48,629× the binding energy.  The T⁶ spectrum has no
eV-scale structure (finest step: 38,494 eV).  Atomic binding
is irreducibly R³.  Findings F1–F3.

### Track 2 — T⁶ merging: neutron, helium, and beyond  **Complete**

Search for merger modes beyond the neutron.
**Result:** Multi-electron mergers exist (e.g., 2e+2p at
939.9 MeV) but ALL are heavier than separated particles.
No mode can match helium's 79 eV binding.  T⁶ merging
always costs energy — atoms cannot be mergers.
Findings F12–F14.

### Track 3 — What selects the shear?  (Casimir energy)  **Complete**

Sweep within-plane shear s₁₂ and compute Casimir energy.
**Result:** Full T⁶ Casimir is neutrino-dominated, independent
of s₁₂.  Electron-sheet Casimir varies monotonically (prefers
maximum α).  NO interior minimum — Casimir alone cannot select α.
The missing ingredient is the energy COST of shear (moduli
potential).  Findings F4–F7.

### Track 4 — Hydrogen fine structure constrains r_e  **Complete**

Compute Yukawa Lamb shift correction as function of r_e.
**Result:** The naive KK Yukawa correction is catastrophically
large — 324× to 750,000× the entire Lamb shift across all
viable r_e.  This RULES OUT the assumption that KK massive
modes couple with strength α.  The coupling must be suppressed
by at least ~10⁵.  This resolves the R29 F11 "Critical Tension"
and is itself a model prediction.  Findings F15–F18.

### Track 5 — R³ vs T⁶: the electron-proton energy landscape  **Complete**

Compute energy at all separations from infinity to merger.
**Result:** Hydrogen (R³ bound, 938.783 MeV) is 0.782 MeV
lighter than neutron (T⁶ merged, 939.565 MeV).  The merger
barrier is 57,500× the binding energy — atoms are stable.
The Bohr radius (53,000 fm) and electron tube (32,000 fm)
are surprisingly close (factor 1.7).  Complete two-tier
picture established.  Findings F8–F11.

### Track 6 — Multi-electron atoms and the Pauli principle  **Complete**

Analyze how multi-electron atoms work in T⁶ + R³.
**Result:** r_e is a geometric constant (one value for all
electrons).  Pauli exclusion operates entirely in R³ (orbital
+ spin quantum numbers).  Multi-electron atoms work naturally:
Z copies of the same T⁶ mode, distinguished by R³ states.
The 37,000× scale separation between particle identity (MeV)
and atomic binding (eV) guarantees atomic physics works.
Findings F19–F22.


## Infrastructure

Scripts in `R31-alpha-derivation/scripts/`.  Uses `lib/ma.py`
and `lib/ma_solver.py`.  The Casimir computation uses the
existing `epstein_zeta()` function, extended to sweep
within-plane shears.

## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R15   | Forward charge calculation — complementary path to α |
| R19   | Shear-charge formula α(r, s) — the function to invert |
| R26   | Casimir energy machinery, F73 tension |
| R27   | Particle spectrum — baseline for mode searches |
| R29   | Two-tier physics, nuclei as modes, hydrogen derivation |
| R30   | r_e bounds, α sweep, geometry constraints |
