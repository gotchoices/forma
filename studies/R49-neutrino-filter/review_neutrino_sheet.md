# R49 Review: What does the neutrino sheet fit actually prove?

The neutrino sheet in model-E uses three modes on a torus
at ε_ν = 5.0, s_ν = 0.022 to predict neutrino masses,
oscillation ratios, and absolute mass scale.  This review
examines what is constrained, what is predicted, and what
is uncertain.

---

## What was measured (inputs)

Only TWO experimental values are used:

| Input | Value | Source | Precision |
|-------|-------|--------|-----------|
| Δm²₂₁ | 7.53 × 10⁻⁵ eV² | Solar neutrino oscillations | ~2% |
| Δm²₃₁/Δm²₂₁ | 33.6 ± 0.9 | Atmospheric / solar ratio | ~3% |

These are mass-squared DIFFERENCES, not absolute masses.
Nobody has measured an absolute neutrino mass.  The best
bounds are:

- KATRIN (direct, kinematic): m(ν_e) < 0.8 eV
- Cosmology (Planck): Σm_ν < 0.12 eV (sum of all three)

Both are upper limits, not measurements.

## What MaSt derived

**The shear s_ν = 0.022** — from the RATIO Δm²₃₁/Δm²₂₁ = 33.6
alone.  The formula:

> Δm²₃₁/Δm²₂₁ = (μ₃² − μ₁²) / (μ₂² − μ₁²) = (3 − 2s) / (4s)

At s = 0.022: ratio = 33.6 exactly.  This is one equation,
one unknown.  The fit is guaranteed — it has zero predictive
content on its own.

**The ring circumference L_ring_ν** — from Δm²₂₁ combined with
the mode energies μ₁ and μ₂ (which depend on ε_ν and s_ν).
At Family A (ε_ν = 5.0): L_ring_ν ≈ 42 μm.

**The absolute neutrino masses** — these are PREDICTIONS:

| Neutrino | Mode | Mass (Family A) | Mass (Family B/C) |
|----------|------|------------------|--------------------|
| ν₁ | (1, 1) | 29.2 meV | ~5 meV |
| ν₂ | (−1, 1) | 30.5 meV | ~10 meV |
| ν₃ | (1, 2) | 58.2 meV | ~50 meV |
| **Σm_ν** | | **117.8 meV** | **~65 meV** |

The absolute masses are derived from the geometry, not from
any mass measurement.  No other physics framework derives
them from first principles in this way (though various
seesaw and flavor symmetry models make their own predictions).

## The Family uncertainty

R49 found three viable families with different ε_ν values:

| Family | ε_ν | Modes | Σm_ν | ν₁ freq (THz) | Sterile count |
|--------|-----|-------|------|----------------|---------------|
| **A** | 5.0 | (1,1),(−1,1),(1,2) | 118 meV | 7.06 | ~26 |
| B | 0.1 | (±1,2),(±2,2),(±10,1) | 65 meV | 1.23 | 120+ |
| C | 0.2 | (0,2),(−1,2),(±6,1) | 64 meV | 0.82 | 73–82 |

**Why Family A leads:**
1. Fewest sterile modes (~26 vs 120+) — cosmology constrains
   extra light species (N_eff = 3.04 ± 0.02)
2. Cleanest waveguide propagation at ε = 5.0
3. Simplest modes — (1,1), (−1,1), (1,2) are the three
   lowest-order spin-½ modes on any torus

**Family A's risk:** Σm_ν = 118 meV is just below the
cosmological bound (~120 meV).  If future surveys tighten
the bound below ~110 meV, Family A is ruled out and
Family B/C would take over.  CMB-S4, DESI, and Euclid
may resolve this within a few years.

## What the ν-sheet actually predicts (testable)

| Prediction | Value (Family A) | How to test |
|-----------|------------------|-------------|
| Σm_ν | 117.8 meV | Cosmological surveys |
| Normal mass ordering | m₁ < m₂ < m₃ | JUNO, DUNE, Hyper-K |
| Majorana nature | Yes (from C-conjugate mixing, Q105) | 0νββ at \|m_ββ\| ~ 10–30 meV |
| Absolute m₁ | 29.2 meV | KATRIN upgrades, Project 8 |
| THz absorption at ν₁ | 7.06 THz | L04 experiment |

These are genuine predictions — none is an input.

## Could the sheet be smaller or larger?

**Yes.** The ring circumference L_ring_ν depends on ε_ν and
the mode assignment:

| Family | L_ring_ν | L_tube_ν | Sheet "size" |
|--------|----------|----------|-------------|
| A | ~42 μm | ~210 μm | macroscopic |
| B | ~8 μm | ~0.8 μm | sub-micron |
| C | ~10 μm | ~2 μm | micron-scale |

A factor of ~5 uncertainty in the sheet size.  The RATIO
Δm²₃₁/Δm²₂₁ is fixed regardless — it depends only on s_ν.

## Are the L04 frequencies correct?

**Not precisely — they depend on which Family is correct.**
The uncertainty spans nearly an order of magnitude:

| Eigenstate | Family A (THz) | Family B (THz) | Family C (THz) |
|-----------|----------------|----------------|----------------|
| ν₁ | 7.06 | 1.23 | 0.82 |
| ν₂ | 7.37 | 2.44 | 2.25 |
| ν₃ | 14.07 | 12.11 | 12.28 |

L04 is designed to scan all four frequency sets (0.82–14.07
THz) precisely because the absolute frequencies are uncertain.
Finding a signal at one set would SIMULTANEOUSLY:
1. Confirm the absolute neutrino masses
2. Pin ε_ν (determine which Family)
3. Demonstrate EM-to-ν coupling (beyond Standard Model)

## Are other frequencies ruled out?

Not rigorously.  R49 searched ε_ν from 0.1 to 10 with
low-order modes.  Higher-order modes or ε_ν outside this
range could give different frequencies.  The four families
are the most natural, low-order candidates — not proven
exclusive.

## Could more than one Family be true at once?

No.  A single torus has one (ε_ν, s_ν).  All three neutrinos
share the same sheet geometry.  The Families are mutually
exclusive.

## What nature had to "cooperate" on

| Feature | Guaranteed? | Evidence? |
|---------|------------|-----------|
| Δm² ratio fit | Yes (1 eq, 1 unknown) | No — input |
| **Real s_ν exists** | Not guaranteed | Mild (some ratios have no solution) |
| **Σm_ν < cosmological bound** | **No** — comes from geometry | **Testable** |
| **Normal ordering** | **No** — from mode assignment | **Testable** |
| **Majorana nature** | **No** — from C-conjugate structure | **Testable (0νββ)** |
| **Same mechanism as e-sheet** | **No** — independent sheet | **Structural** |
| **Integer winding → exact ratio** | **No** — could have been irrational | **Elegant** |

The Δm² ratio fit is an input (1 parameter, 1 constraint).
But the absolute masses, ordering, Majorana nature, and
consistency with cosmological bounds are genuine predictions
that could fail and haven't.

## Connection to R57 (energy routing)

R57 Track 2 found that the ν-sheet hosts 1,322 modes below
1 MeV, of which only 3 are active neutrinos and 1,319 are
dark/sterile.  The 440:1 dark-to-active ratio means that
THz radiation at ν frequencies would preferentially populate
dark modes rather than active neutrinos.

R57 Track 5 showed that resonant input at exactly the ν₁
frequency accumulates energy in dark modes even with symmetric
Ma-S coupling (α both ways), because the Q factor creates an
input/leakage asymmetry.

If L04 finds anomalous absorption at one of the four
frequency sets WITHOUT a corresponding change in nuclear
decay rates, this would confirm: (a) the coupling exists,
(b) energy routes to dark modes (440:1 preference),
(c) the absolute frequency (and therefore mass) is correct.

---

*Studies: R26 (original ν derivation), R49 (ε_ν sweep,
three families), R57 (dark mode routing), L04 (THz experiment)*
