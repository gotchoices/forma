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

---

## Track 3: Proton-to-neutron cross-sheet pathway

### F8. The compound dark mode desert is also empty

Between 0.1 and 100 MeV, there are ZERO Q = 0 multi-sheet
modes in the search range (|n_t| ≤ 3, |n_r| ≤ 10).  All 96
compound modes found are at 100+ MeV (dominated by one e-ring
winding at ~104 MeV).  The energy desert between ν-scale and
e-scale persists for compound single-modes.

### F9. The single-step pathway dismantles the proton to zero

The greedy pathway (changing one quantum number at a time)
goes: proton → unwind all p-ring windings (938 → 0 MeV) →
add ν content (free) → rebuild e-ring and p-ring as neutron
(0 → 939 MeV).  14 steps, net +0.624 MeV.

This is NOT a viable physical pathway — it requires releasing
938 MeV then re-supplying 939 MeV.  The single-step picture
cannot find a low-barrier route because every intermediate
mode is either at the proton scale (~938) or near zero.

### F10. The DIRECT transition costs only 0.624 MeV

If all 6 quantum numbers change simultaneously:

> proton (0, 0, 0, 0, 1, 3) → neutron (0, −4, −1, 2, 0, −3)
> ΔE = +0.624 MeV
> Δn = (0, −4, −1, +2, −1, −6)

No barrier.  The cost is purely the n-p mass difference.
The Coulomb barrier for electron capture in S is ~3.7 keV;
in Ma, there is no spatial approach — the rearrangement is
purely a mode change on T⁶.

### F11. The multi-mode picture is necessary

The single-mode picture (one 6-tuple at a time) cannot find
a low-energy p → n transition because it changes one quantum
number per step, forcing the proton through zero.

The MULTI-mode picture: if an electron (providing e-sheet
content n₁ = 1, n₂ = 2) and neutrino dark modes (providing
ν-content n₃, n₄) are CO-LOCATED with the proton (providing
p-sheet content n₅ = 1, n₆ = 3), the combined system already
has the quantum numbers of a neutron.  The "transition" is
not building the neutron from scratch — it's the existing
co-located modes RECOGNIZING that they form a neutron.

The energy cost is the net mass difference (0.624 MeV) plus
any reorganization cost.  This is dramatically less than the
Coulomb barrier (164 keV for p-p fusion, 3.7 keV for
electron capture) because the particles don't need to
approach each other in S — they're already co-located.

### F12. What co-location means physically

In atoms, the electron IS co-located with the proton — the
(1, 2) mode at the Bohr radius encloses the nucleus (R56 F5).
Neutrino dark modes at ~0.03 keV are everywhere (the ν-sheet
is 42 μm across).  So every hydrogen atom already has:

- A proton (p-sheet content)
- An electron (e-sheet content, enclosing the proton)
- Ambient neutrino dark modes (ν-sheet content)

The question is: why doesn't every hydrogen atom spontaneously
become a neutron?  The answer: the ENERGY.  The neutron has
0.624 MeV more mass than the proton.  The co-located modes
can't rearrange unless 0.624 MeV is supplied.  In free hydrogen,
this energy isn't available.  In a system where external energy
is pumped in (compressed lattice, intense EM field, etc.), it
might be.

### F13. Implications for cold fusion / LENR

The Ma-pathway for p → n:
1. The quantum numbers are already present (p + e + ν)
2. The cost is 0.624 MeV (just the mass difference)
3. No Coulomb barrier (the transition is in Ma, not S)
4. The 0.624 MeV can come from: lattice energy (~eV per mode,
   need ~20,000 accumulated dark modes), kinetic energy of
   the electron, or external EM radiation

The bottleneck is supplying 0.624 MeV to the co-located system.
In Fleischmann-Pons type experiments (palladium loaded with
deuterium), the lattice provides a dense environment where
protons and electrons are co-located at nuclear distances.
If dark modes accumulate in this environment (~20,000 dark
bosons at 0.03 keV each = 0.6 MeV), the p → n transition
threshold is reached.

### Track 3 status

**Complete.**  The single-mode pathway dismantles the proton
(not viable).  The direct transition costs 0.624 MeV with no
Coulomb barrier.  Co-location of p + e + ν is the mechanism.
The bottleneck is energy supply (0.624 MeV from accumulated
dark modes or external source).

---

## Track 4: Multi-mode accumulation

### F14. Dark bosons stack without limit

Dark bosons (even tube winding, spin 0) obey Bose-Einstein
statistics: unlimited occupancy per mode.  A single dark
mode can hold any number of quanta, each adding one unit
of mode energy.  No Pauli exclusion.

230 distinct dark boson modes exist below 1 keV on the
ν-sheet.

### F15. Accumulation arithmetic

| Quantity | Value |
|----------|-------|
| Neutron threshold | 624 keV above (proton + electron) |
| Lightest dark boson | ~0.012 keV (30 meV) |
| Quanta needed | ~52 million (single mode) or ~230k per mode (spread across 230 modes) |

The count is large but finite.  Dark bosons accumulate
because they don't radiate (no EM coupling to S).

### F16. Accumulation rate at any nonzero coupling

At 1 mW THz source (7 THz = ν₁ frequency):

| Coupling | Dark mode rate | Time to threshold |
|----------|---------------|-------------------|
| α (1/137) | 1.6 × 10¹⁵ /s | sub-second |
| α² (5 × 10⁻⁵) | 1.2 × 10¹³ /s | sub-second |
| α³ (4 × 10⁻⁷) | 8.4 × 10¹⁰ /s | sub-second |

Even at α³ coupling, the accumulation rate vastly exceeds
the 624 keV threshold at 1 mW input.  The bottleneck is
NOT the accumulation rate — it's whether the coupling exists
at all and whether accumulated energy persists (no leakage).

### F17. Dark mode persistence is the critical question

If the ν-sheet Ma-S coupling is truly zero (model-E assumption
for neutral modes), dark bosons persist indefinitely.  Energy
accumulates without leakage.

If ANY nonzero ν-S coupling exists, dark modes slowly radiate.
The race is: input rate vs leakage rate.  At any coupling
where input > leakage, accumulation succeeds.

**This is testable by L04:** if THz at ν frequencies produces
anomalous absorption (energy disappears without visible
re-emission), dark modes are being populated and persisting.

### F18. The co-location scenario

In a hydrogen-loaded palladium lattice:
- Protons at interstitial sites (present)
- Electrons delocalized (present, co-located)
- Neutrino dark modes at ~0.03 keV (accumulating)

The p → n transition requires all three co-located plus
624 keV of accumulated energy.  Once triggered:

| Step | Process | Energy |
|------|---------|--------|
| 1 | Dark modes accumulate | +624 keV input |
| 2 | p + e + ν → n (mode rearrangement in Ma) | −624 keV consumed |
| 3 | n + p → d + γ (neutron fuses with neighbor) | +2,224 keV released |
| | **Net** | **+1,600 keV per event** |

Energy gain ratio: **3.6×** (output/input).

The 2.2 MeV gamma ray from deuteron formation is the
experimental signature.

### F19. Two unknowns determine feasibility

1. **Ma-S coupling for ν dark modes** — does external EM
   radiation populate dark modes at all?  R55 (framed) would
   derive this from the 9×9 metric.  L04 (proposed) would
   measure it.

2. **Dark mode leakage rate** — once populated, do dark modes
   persist or decay?  If ν-S coupling = 0 (model-E), they
   persist forever.  If nonzero, the leakage rate must be
   slower than the accumulation rate.

Both are measurable.  Neither has been measured.

### F20. Connection to experimental observations

The LENR literature reports:
- Excess heat in palladium-deuterium systems
- Occasional neutron and tritium production
- Irreproducibility (sometimes works, usually doesn't)

The MaSt interpretation:
- Excess heat = dark mode accumulation reaching threshold,
  triggering p → n → d fusion events
- Irreproducibility = accumulation depends on lattice geometry,
  loading fraction, and ambient ν dark mode density — all
  of which vary between experiments
- Neutron production = intermediate step (p → n before n + p → d)
- The 2.2 MeV gamma (d formation) should be the primary
  signature but is often not reported — possibly because the
  gamma is absorbed in the palladium lattice

### Track 4 status

**Complete.**  Multi-mode accumulation is energetically feasible
(3.6× gain), the arithmetic works at any nonzero coupling,
and the mechanism predicts specific experimental signatures.
The two unknowns (Ma-S coupling and dark mode persistence)
are testable by L04 and R55.
