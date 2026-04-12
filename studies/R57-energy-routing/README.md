# R57: Energy routing between Ma and S

**Status:** Complete — Tracks 1–5
**Questions:** When energy is added to a system, does it
accumulate in Ma (higher modes, dark modes) or forge new
particles (separation in S)?  Can Ma-domain energy accumulation
bypass Coulomb barriers that block S-domain processes?
**Type:** theoretical + compute
**Depends on:** R56 (routing principle), R54 (compound modes),
R49 (ν-sheet modes), model-E

---

## Motivation

R56 Track 6 established a routing principle: energy routes to
the lowest-cost destination.  In electron shells, this means
filling Ma modes until the torus is full, then overflowing to
the next spatial shell.  The same principle should apply to
ALL energy transitions — not just electron packing.

**The core insight:** the universe has two domains for storing
energy — Ma (compact modes) and S (spatial separation).  Every
physical process is a routing decision: does the next quantum
of energy go into Ma (exciting a higher mode, populating a dark
mode, building toward a heavier particle) or into S (creating
spatial separation, kinetic energy, radiation)?

**The practical question:** if we can populate Ma modes
directly (e.g., by THz radiation at neutrino frequencies),
can we build up enough energy in Ma to trigger nuclear
processes WITHOUT the extreme temperatures needed to overcome
Coulomb barriers in S?  In S, fusion requires ~keV kinetic
energy to force two protons close enough.  In Ma, the proton
and neutron are different modes on the SAME torus — the
transition doesn't require spatial approach, just mode
rearrangement.

This is the theoretical foundation for cold fusion: if the
transition p → n happens in Ma (mode change on the p-sheet +
e-sheet + ν-sheet) rather than in S (spatial collision), there
is no Coulomb barrier to overcome.


## Objectives

### 1. Generalized routing engine

Build a computational tool that, given:
- A starting configuration (set of occupied modes on T⁶)
- An amount of input energy
- The full 9×9 metric

predicts WHERE the energy goes: which new mode gets populated,
or whether a new particle separates in S.  The engine computes
the energy cost of each available transition and selects the
cheapest.

This should be a library module (`lib/routing.py` or similar)
usable across multiple analyses.

### 2. Energy landscape between particle scales

Map the mode landscape at three scales:

**Neutrino → electron (~0.03 meV to 0.511 MeV):**
The ν-sheet has 198 modes below μ = 5, of which 195 are dark
or sterile.  Can dark-mode accumulation gradually build to
electron-scale energy?  Or does the energy bleed into S
(radiation) before reaching the electron threshold?

**Electron → proton (~0.511 MeV to 938 MeV):**
The gap between the e-sheet and p-sheet energy scales.  Are
there dark-mode stepping stones?  Or is the gap too large
for gradual accumulation?

**Proton → neutron (~938.3 to 939.6 MeV):**
Only 1.3 MeV separates them.  The neutron is the proton +
electron + neutrino fused into one 6D knot.  Can this
transition happen in Ma without spatial collision?

### 3. Proton-to-neutron transition in Ma

The neutron mode in R54 is (0, −4, −1, 2, 0, −3) — an
e+ν+p compound.  The proton is (0, 0, 0, 0, 1, 3).  The
transition requires:

- Adding e-sheet content: n₁ goes from 0 to some value,
  n₂ from 0 to −4
- Adding ν-sheet content: n₃ from 0 to −1, n₄ from 0 to 2
- Shifting p-sheet: n₅ from 1 to 0, n₆ from 3 to −3

**Key question:** if an electron is co-located with a proton
(both at the same S coordinate), is there a least-energy path
through Ma mode space that transforms p + e + ν → n?  The
Coulomb barrier that blocks this in S (the electron must
penetrate the proton's charge cloud) does not exist in Ma
(the mode transition is a rearrangement of winding numbers,
not a spatial approach).

### 4. Dark mode accumulation pathway

At any point on the T⁶, the metric supports dark modes (even
tube winding, zero charge).  These modes carry energy but no
electromagnetic signature.  If energy from an external source
(e.g., THz radiation, thermal vibration) can populate dark
modes, they accumulate energy in Ma without any observable
effect in S.

**The hypothesis:** dark mode accumulation is the mechanism
behind anomalous nuclear phenomena (cold fusion, LENR).
Energy accumulates silently in Ma until it reaches the
threshold for a nuclear transition (p → n), at which point
the transition happens in Ma without a Coulomb barrier.

The external energy source doesn't need to provide the full
1.3 MeV at once — it can be accumulated gradually through
many small dark-mode excitations, each below any detection
threshold.

### 5. Least-energy-path visualization

Plot the mode landscape as an energy surface with:
- Ma modes on one axis (discrete quantum numbers)
- S separation on another axis (distance between particles)
- Energy cost on the vertical axis

The least-energy path from one configuration to another is a
path on this surface.  Fusion in S follows the high-mountain
route (over the Coulomb barrier).  Fusion in Ma follows the
low-valley route (through dark-mode stepping stones).

If the Ma route exists and is lower than the S route, Ma-domain
nuclear transitions are energetically favored — they just need
a mechanism to populate the intermediate modes.


## Connection to prior work

| Study | Contribution | Status |
|-------|-------------|--------|
| R56 Track 6 | Routing principle (modes fill, then overflow to S) | Complete |
| R54 Track 1 | Neutron as e+ν+p compound mode on T⁶ | Complete |
| R49 | ν-sheet mode catalog (198 modes, 195 dark/sterile) | Complete |
| L04 | THz experiment at neutrino frequencies | Proposed |
| L02 | Threshold nuclear loading via ν coupling | Proposed |

R57 provides the THEORETICAL framework that connects these:
- R56 says energy routes to the cheapest mode
- R49 says the ν-sheet is full of dark modes
- R54 says the neutron IS a compound Ma mode
- L04 and L02 propose EXPERIMENTAL tests of the coupling

R57 asks: is there a continuous, lowest-energy path through
Ma mode space from {proton + electron + neutrino} to {neutron}?


## Tracks (preliminary)

### Track 1: Routing engine

**Status:** Complete

Built two library modules:

**`lib/metric.py`** — pluggable Metric class with:
- Named presets: `Metric.model_E()`, `Metric.model_D()`
- Custom construction with any (ε, s, σ) values
- Immutable after construction (safe for searches)
- `with_sigma()` for parameter variation
- Mode energy, charge, spin, sheet classification

**`lib/routing.py`** — RoutingEngine with:
- `mode_census()` — enumerate all modes below an energy ceiling
- `modes_near()` — find modes near a target energy
- `transitions_from()` — single-step transitions (±1 on any quantum number)
- `find_pathway()` — greedy least-energy path between two modes
- `promote_vs_separate()` — compare Ma excitation vs S separation
- `energy_landscape()` — 1D energy scan along any dimension

Verified: proton → neutron pathway found in 14 steps through
Ma mode space.  Net energy cost: +0.6 MeV (the n-p mass
difference).  No Coulomb barrier in the path — the transition
is pure mode rearrangement.

### Track 2: Neutrino-scale landscape

Map the ν-sheet mode density and routing.  When energy
enters at ν₁ frequency, what modes does it populate?
How much energy can accumulate before it bleeds to S?

### Track 3: Proton-to-neutron pathway

Compute the least-energy path from proton + electron +
neutrino (three separate modes) to neutron (one compound
mode).  Compare the Ma route (mode rearrangement) to the
S route (Coulomb barrier penetration).

### Track 4: Cold fusion feasibility

Given the routing engine and the p → n pathway:
- What energy input is needed?
- Can it be supplied by ν-sheet dark mode accumulation?
- What experimental signature would it produce?
- How does this compare to L02's proposed threshold loading?


## What success looks like

**Strong:** A continuous least-energy path exists through Ma
mode space from p + e + ν → n, with an energy barrier lower
than the Coulomb barrier.  The intermediate modes are
identifiable dark modes on the ν-sheet.  This provides a
theoretical mechanism for LENR.

**Moderate:** The path exists but requires coordinated
excitation of multiple modes simultaneously (not gradual
accumulation).  This limits practical applications but still
explains the physics.

**Negative:** No Ma pathway exists below the Coulomb barrier.
The S route is always cheaper.  Cold fusion has no Ma-domain
mechanism.  This is informative — it constrains what Ma-domain
physics can and cannot do.


## Why this matters beyond physics

If Ma-domain nuclear transitions are possible, they represent
a fundamentally different approach to nuclear energy:
- No extreme temperatures or pressures
- No Coulomb barrier to overcome
- Energy input through EM radiation at specific frequencies
- Controlled by mode selection, not brute force

The practical barrier is whether the Ma-S coupling is strong
enough to allow external energy to populate Ma modes.  L04
is designed to test exactly this coupling.
