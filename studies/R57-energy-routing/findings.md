# R57: Energy routing — Findings

## Track 1: Routing engine

**Complete.** Library modules `lib/metric.py` and `lib/routing.py`
built and verified.  Proton→neutron pathway found in 14 steps
through Ma mode space, net cost +0.6 MeV, no Coulomb barrier.

## Track 2: Neutrino-scale energy landscape

### F1. The ν-sheet is dense with dark modes: 440:1 ratio

Below 1 MeV, the ν-sheet hosts 1,322 modes:
- 3 active neutrinos
- 669 sterile fermions
- 650 dark bosons

For every active neutrino, there are 440 dark/sterile
alternatives.  The nearest dark mode to ν₁ is only 0.27%
away in energy.

### F2. Dark modes cluster at the neutrino energy scale

All ν-sheet modes sit at essentially the same energy (~0.03 keV).
Adding more ν-tube or ν-ring windings changes the energy by
fractions of a percent because the ν-sheet geometry (ε_ν = 5.0)
is moderate and the modes are closely packed.

### F3. The ν-to-electron energy desert

There is a factor of ~3.5 million between the ν energy scale
(0.03 keV) and the e energy scale (104 MeV per e-ring winding).
**No dark modes bridge this gap.**  All ν-sheet modes cluster
below 0.1 keV.  The first e-sheet modes start at ~104 MeV.

This means: **dark-mode accumulation on the ν-sheet alone
CANNOT gradually build to electron-scale energy.**  Pumping
energy at ν frequencies adds more ν modes at ~0.03 keV, not
higher-energy modes.  The energy stays at the neutrino scale.

### F4. The routing verdict: S wins below electron scale

At every energy between 0.03 keV and 511 keV, creating a
duplicate particle in S is cheaper than finding the next Ma
mode above the current energy.  The Ma mode landscape has a
desert between the ν and e scales.

| Energy | Next Ma mode | S duplication | Cheaper |
|--------|-------------|---------------|---------|
| 0.03 keV | ∞ (none in range) | 0.03 keV | S |
| 1 keV | ∞ | 1 keV | S |
| 100 keV | ∞ | 100 keV | S |
| 511 keV | 511.00 keV | 511.00 keV | Ma (barely) |

### F5. Cross-sheet modes may bridge the gap

The routing engine searched single-sheet modes.  COMPOUND modes
spanning multiple sheets (with small windings on each) might
fill the desert.  For example, a mode (0, 0, 3, 2, 0, 1) has
both ν and p content; its energy depends on cross-sheet
coupling terms that could place it between the ν and e scales.

The Track 1 proton→neutron pathway demonstrates that cross-sheet
paths exist and can traverse the full energy range.  The desert
is a single-sheet phenomenon, not necessarily a multi-sheet one.

### F6. Implications for THz experiments (L04)

If THz radiation at ν frequencies couples to the ν-sheet:
- It will populate dark modes (440:1 ratio favors dark over active)
- The dark modes accumulate energy AT THE ν SCALE (~0.03 keV)
- The energy does NOT climb to the electron scale
- L04 should look for energy ABSORPTION (heating) at ν frequencies,
  not nuclear rate changes (which require electron-scale energy)
- The null result for beta decay stimulation is the expected outcome
  if coupling exists but energy stays at the ν scale

### F7. The cold fusion question requires cross-sheet analysis

Track 2 shows that single-sheet accumulation can't reach nuclear
scales.  The p→n pathway from Track 1 works because it traverses
ACROSS sheets.  Track 3 should analyze whether cross-sheet dark
modes (compound modes with ν + p content) can provide the
stepping stones between the ν and nuclear energy scales.

### Track 2 status

**Complete.**  The ν-sheet is dense with dark modes but they
all cluster at the same energy.  Single-sheet accumulation
cannot bridge to the electron or nuclear scale.  Cross-sheet
compound modes are the path forward (Track 3).
