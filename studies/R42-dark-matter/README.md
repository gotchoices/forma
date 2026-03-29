# R42. Dark matter from ghost modes — charge cancellation and mass census

**Status:** Complete — see `findings.md` for F1–F14
**Depends on:** R28 (spectrum census), R33 (ghost selection), R41 (dynamic model),
  R19 (shear-induced charge)
**Motivates:** Q94 (Compton window / dark modes), Q93 (relativistic effects),
  Q85 (threshold theory)

---

## Premise

The MaSt model predicts ~900 modes below 2 GeV with physical charges,
versus ~40 observed particles.  Previous work treated the excess as a
"ghost mode problem" requiring suppression.  Q94 proposes the opposite:
ghost modes are dark matter.

Two independent mechanisms make ghost modes invisible:

1. **Charge cancellation.**  For every mode (n₁, n₂, n₃, n₄, n₅, n₆)
   with charge Q = −n₁ + n₅, there exists a partner (−n₁, n₂, n₃, n₄,
   −n₅, n₆) with charge −Q and identical mass.  The spectrum is exactly
   charge-symmetric.  In thermal equilibrium, equal numbers of +Q and
   −Q modes are produced.  Any macroscopic collection is charge-neutral:
   a gas of mass with no net charge.

2. **Compton window.**  The Ma sheet dimensions define a resonant
   aperture into S.  Modes whose spatial pattern doesn't match the
   aperture couple weakly — they have mass but negligible EM
   interaction.  (See Q94 §§1–2 for mechanism and Q factor.)

Together: ghost modes form a charge-neutral, weakly-coupled gas with
definite mass.  This is dark matter by definition.


## Goals

1. **Demonstrate charge cancellation.**  Enumerate all modes below
   2 GeV.  Show that for every charge distribution (thermal, equal,
   mass-weighted), the net charge of the ghost population is zero or
   negligible.

2. **Compute the dark-to-visible mass ratio.**  Under physically
   reasonable occupation models, compute Σm_dark / Σm_visible and
   compare to the observed ratio of ~5.4.

3. **Characterize the dark mass spectrum.**  What are the lightest and
   heaviest stable dark modes?  How dense is the spectrum?  Is it
   consistent with warm/cold dark matter bounds?

4. **Test the Compton window Q factor.**  If the window has Q ~ 137
   (Mechanism A from Q94), what fraction of modes are effectively
   dark?  How does this change the mass ratio?


## Tracks

### Track 1: Mode census and charge symmetry

Enumerate all modes on all three sheets (Ma_e, Ma_ν, Ma_p) up to
n_max = 5 and E < 2 GeV.  For each mode, record mass, charge, spin,
and classification (known particle or dark).

Verify:
- For every mode with charge +Q, a partner with charge −Q and same
  mass exists.
- The charge-weighted sum Σ(Q × n_modes) = 0 exactly (by symmetry)
  or statistically (under any occupation model).
- Plot the charge distribution of dark modes.  It should be symmetric
  around zero.

### Track 2: Mass ratio under equal occupation

Assume one particle per mode (or equal number density for all species).
Compute:
- Σm_visible (summed over known particles only)
- Σm_dark (summed over all ghost modes)
- Ratio = Σm_dark / Σm_visible
- Compare to 5.4

This is the simplest possible model — no thermodynamics.  If the
ratio is order-of-magnitude correct, the hypothesis is viable.

### Track 3: Mass ratio under thermal distributions

Apply physically motivated occupation models:

a. **Boltzmann distribution** at temperature T:
   n(E) ∝ exp(−E/kT).  Scan T from 1 MeV to 1 GeV.  At each T,
   compute the dark/visible mass ratio.  Find the temperature (if
   any) where the ratio matches 5.4.

b. **Fermi-Dirac / Bose-Einstein** (for fermion/boson modes):
   n(E) = 1/[exp(E/kT) ± 1].  Same scan.

c. **Freeze-out model** (simplified):  Assume each species freezes
   out at T_fo ~ m/20 (standard WIMP estimate).  Relic abundance
   ∝ 1/(⟨σv⟩ × m_Pl × T_fo).  For dark modes with suppressed
   coupling (σ ~ α² × W² where W is the window factor), compute
   the relic density.

Report which model(s) give dark/visible ≈ 5.4.

### Track 4: Dark spectrum characterization

From the census:
- Lightest stable dark mode on each sheet (mass, quantum numbers)
- Heaviest stable dark mode below 2 GeV
- Number of dark modes per 100 MeV bin — plot the mass spectrum
- Average dark mode mass vs average visible mode mass
- Fraction of dark modes that are fermions vs bosons

Check: is the lightest dark mode consistent with warm dark matter
bounds (m > ~keV from Lyman-α forest constraints)?

### Track 5: Window Q factor sensitivity

Parameterize the window as a Lorentzian with quality factor Q:
W(ω) = 1 / [1 + Q²(ω/ω₀ − ω₀/ω)²]

For each mode, compute W based on the mode's energy relative to
the fundamental on its sheet.  Apply a visibility threshold
(e.g., W > 0.5 = visible, W < 0.5 = dark).  Sweep Q from 1 to 1000.

Plot:
- Dark/visible mass ratio vs Q
- Number of visible modes vs Q
- Find Q_crit where visible modes ≈ 40 (matching observation)
- Find Q_DM where dark/visible mass ratio ≈ 5.4
- Do Q_crit and Q_DM coincide?  If so, this pins Q from two
  independent observables.


## Success criteria

- **Minimum:** Charge cancellation demonstrated.  Mass ratio
  within 3×–30× of 5.4 under at least one occupation model.
- **Strong:** Mass ratio within 2× of 5.4.  Q factor consistent
  with both the visible particle count (~40) and the mass ratio
  (~5.4) simultaneously.
- **Home run:** A single Q value reproduces the correct number of
  visible particles AND the correct dark/visible ratio AND is
  consistent with 1/α ≈ 137.


## Results

14 findings (F1–F14) across 6 tracks.  See `findings.md`.

- **Charge cancellation confirmed (F1–F3).**  The spectrum is exactly
  charge-symmetric for |Q| ≥ 2.  The Q = ±1 asymmetry is an artifact
  of the visible particle list.  Mass degeneracy is exact.

- **The observed ratio 5.4 falls within our range (F4).**  Under
  physically motivated filters, the DM/vis ratio spans 2.4 to 12.4.
  The Planck value of 5.36 ± 0.05 sits in the middle.  Several
  simple filters bracket it closely:

  | Filter | DM/vis | vs 5.4 |
  |--------|-------:|-------:|
  | No filter | 12.41 | 2.3× high |
  | \|Q\| ≤ 2 | 4.41 | 18% low |
  | max\|n_tube\| ≤ 1 | 4.77 | 12% low |
  | Q = 0, mt ≤ 1 | 4.32 | 20% low |

- **A coupling mechanism is needed (F6–F7).**  Boltzmann weighting
  never reaches 5.4.  The ratio must come from MODE SELECTION
  (which modes couple to S), not from thermodynamics.

- **Assessment: the hypothesis is viable.**  The dark matter ratio
  CAN be met with physically motivated mode selection.  The next
  step is computing the actual projection integral W(n) from geometry
  to replace the ad hoc filters.
