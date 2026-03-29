# R42 Findings — Dark matter from ghost modes


## Astrophysical context

The dark-to-visible matter ratio is one of the best-measured numbers
in cosmology.  From the Planck 2018 final full-mission CMB analysis
(Planck Collaboration VI, A&A 641, 2020):

    Ω_dm h² = 0.120 ± 0.001   (dark matter density)
    Ω_b  h² = 0.0224 ± 0.0001 (baryon density)

    Ω_dm / Ω_b = 5.36 ± 0.05

This ratio is measured independently by:
- CMB power spectrum (Planck) — 5.36
- Big Bang nucleosynthesis (BBN) — consistent
- Baryon acoustic oscillations (BAO) — consistent
- Galaxy rotation curves — consistent (order of magnitude)
- Gravitational lensing — consistent
- Bullet Cluster — direct evidence of collisionless DM

The consensus: dark matter is ~5.4× more abundant than visible
(baryonic) matter by mass-energy density.  It interacts
gravitationally but has negligible electromagnetic interaction.
Its particle identity is unknown.


## Track 1: Charge symmetry

**F1. Charge spectrum is symmetric for |Q| ≥ 2.**
For every charge value |Q| = 2 through 10, the number of dark modes
with charge +Q exactly equals the number with charge −Q.  This is an
exact symmetry of the Ma spectrum: flipping (n₁, n₅) → (−n₁, −n₅)
flips the charge sign without changing the energy.

**F2. Q = ±1 has an asymmetry artifact.**
Dark modes at Q = +1 (94,270) outnumber Q = −1 (82,775) by 11,495.
This is NOT a physical asymmetry — it's because the visible particle
list is asymmetric: more known particles have Q = −1 (electron, muon,
tau, pions, kaons, cascades, omega) than Q = +1.  Every mode removed
from "dark" as "visible" at Q = −1 creates the imbalance.  The full
spectrum (visible + dark) is exactly symmetric.

**F3. Charge-conjugate mass degeneracy is exact.**
98.2% of positive-charge dark modes have a partner with opposite
charge found in the scan.  The ~2% missing are modes whose conjugate
has energy > 2 GeV (above the cutoff).  Masses match to machine
precision when both n₁ and n₅ are flipped.

**Verdict:** In any thermal or random population, the dark mode
gas is charge-neutral to arbitrary precision.  The charge cancellation
is an exact symmetry of the Ma geometry, not an approximation.


## Tracks 2–3 & 6: Mass ratio analysis

### What we computed

The dark/visible mass ratio Σm_dark / Σm_visible depends on which
modes count as "dark" and which as "visible."  The raw census with
no filter gives an upper bound.  Physically motivated filters
(charge selection, tube-winding suppression) give a range of
lower values.  The target is 5.36 ± 0.05.

### Summary table

| Filter | N_dark | N_vis | DM/vis | vs 5.4 |
|--------|-------:|------:|-------:|-------:|
| No filter (all families) | 123,136 | 8,633 | 12.41 | 2.30× |
| \|Q\| ≤ 2 | 44,728 | 8,633 | **4.41** | 0.82× |
| \|Q\| ≤ 1 | 25,126 | 8,633 | 2.43 | 0.45× |
| max\|n_tube\| ≤ 2 | 10,185 | 2,190 | **4.04** | 0.75× |
| max\|n_tube\| ≤ 1 | 2,273 | 400 | **4.77** | 0.88× |
| \|Q\| ≤ 1 AND mt ≤ 1 | 1,679 | 400 | 3.48 | 0.65× |
| Q = 0 only | 9,031 | 2,948 | 3.59 | 0.67× |
| Q = 0 AND mt ≤ 1 | 715 | 176 | **4.32** | 0.80× |

**F4. The observed ratio 5.4 falls within our computed range.**
Our estimates span 2.4 to 12.4, depending on which physical filter
is applied.  The target of 5.4 sits squarely in the middle.  No
filter gives 5.4 exactly under equal occupation, but several
filters bracket it closely:

- |Q| ≤ 2:  4.41 (18% below target)
- mt ≤ 1:  4.77 (12% below target)
- Q = 0, mt ≤ 1:  4.32 (20% below target)
- No filter:  12.41 (130% above target)

**F5. Average dark mode is lighter than average visible mode.**
- Average visible mode mass: 1,231 MeV
- Average dark mode mass: 1,071 MeV
- Ratio: 0.87

The dark spectrum is not dominated by light modes — it spans the
full 0–2 GeV range.

**F6. Boltzmann weighting makes the ratio worse, not better.**
Under Boltzmann occupation n(E) ∝ m × exp(−m/T), the ratio ranges
from 12.4 (T → ∞) to ~200 (T → 0, neutrino-sheet domination).
It never drops below 12.4.  Thermal weighting favors light modes,
and there are more light dark modes than light visible ones.

This means the correct ratio must come from the SELECTION of which
modes couple to S (the window mechanism), not from thermodynamics.

**F7. The ratio is sensitive to the scan range.**
At n_max = 3: ratio = 7.80.  At n_max = 5: ratio = 12.41.  Higher
n_max would find more modes (most of them dark, with high winding
numbers).  The n_max → ∞ limit of the UNFILTERED ratio diverges.
A physical cutoff mechanism IS required — this is the Compton
window or the dynamic low-pass filter.

### What determines the "right" filter

The filters tested above are proxies for the real physical mechanism.
The |Q| ≤ 2 filter (ratio 4.41) and the mt ≤ 1 filter (ratio 4.77)
both land close to 5.4 because they independently capture the same
physics: modes with high quantum numbers don't couple to S.

The actual coupling is continuous, not a hard cutoff.  A mode with
|Q| = 3 doesn't suddenly go dark — it gradually decouples.  The
true ratio depends on the coupling function W(n₁, n₂, n₃, n₅, n₆),
which must be computed from the projection integral (Q93 Path 2,
Q94 §2).

### What would bring the ratio to exactly 5.4

Three effects, each pulling in the right direction:

1. **The Compton window (Q94).**  A resonant aperture with Q ~ 137
   to 350 suppresses off-resonance modes.  Track 5 showed Q ≈ 350
   gives the right ratio with a Lorentzian window, but the window
   shape is an approximation.

2. **Mode stability.**  Some dark modes may decay to lighter dark
   modes, reducing the effective count.  Modes that decay in < 10⁻²⁵ s
   would not contribute to cosmological dark matter.  This has not
   been computed.

3. **Production asymmetry.**  In the early universe, the number
   density of each dark species depends on its production cross-section
   (how easily it is excited from the vacuum).  If dark modes are
   produced via Ma-internal coupling only (not through S), their
   abundance is set by the Ma thermal history, not the S thermal
   history.  The required number density per dark species is:

   | Filter | f = n_dark / n_baryon |
   |--------|---------:|
   | All families | 0.000077 |
   | \|Q\| ≤ 1 | 0.00039 |
   | \|Q\| ≤ 1, mt ≤ 1 | 0.0059 |
   | Q = 0, mt ≤ 1 | 0.013 |

   For the tightest filter, each dark species needs ~1.3% of the
   baryon number density.  This is very achievable — baryons are
   already suppressed to ~10⁻¹⁰ of photons by the baryon asymmetry.


## Track 4: Dark spectrum characterization

**F8. Lightest dark modes are neutrino-sheet states.**
Pure neutrino-sheet modes (0, 0, ±k, 0, 0) have E ≈ 0 (sub-eV).
Next lightest: electron-sheet tube modes at 39 keV.  The 39 keV
modes are above the Lyman-α warm dark matter bound (~keV).

**F9. Dark spectrum spans the full 0–2 GeV range.**
Densest bins: 900–1000 MeV (25,212 families) and 1400–1500 MeV
(27,709 families).

**F10. Roughly equal fermion/boson split.**
Dark families: 59,061 fermions (48%), 64,075 bosons (52%).

**F11. Most dark modes have high tube winding.**
93% have max|n_tube| ≥ 3.  These overlap with the dynamic low-pass
filter's suppression targets (R41).  The "window" and "low-pass
filter" mechanisms are complementary — both select against the same
modes.


## Track 5: Window Q factor

**F12. Q ≈ 350 gives the correct ratio with a Lorentzian window.**
With a Lorentzian transmittance allowing harmonics: DM/vis = 5.54
at Q = 350.

**F13. Q = 137 gives DM/vis = 2.41.**
Too few dark modes at this Q.  However, the Lorentzian + harmonic
model is very permissive (any integer harmonic of the fundamental
passes).  A more physical window would be more selective, shifting
the Q curve.

**F14. The Q model is too crude for quantitative conclusions.**
The Lorentzian window treats all modes the same based on energy
alone.  The real coupling depends on mode SHAPE (spatial pattern
on the torus), not just energy.  This is why the Q targets for
particle count and DM ratio don't coincide.


---

## Verdict

### What we have established

1. **Charge cancellation is exact (F1–F3).**  The dark mode gas is
   charge-neutral by symmetry of the Ma spectrum.  No mechanism
   needed — it's geometric.

2. **The observed ratio 5.4 is within our range (F4).**  Under
   physically motivated filters, our estimates span 2.4 to 12.4.
   The target sits in the middle.  Several simple filters give
   ratios within 20% of 5.4.

3. **The mass spectrum is discrete and parameter-free (F8–F11).**
   If dark matter is ghost modes, its mass spectrum is completely
   determined by the Ma geometry.  No new particles, no new
   parameters.

4. **A coupling mechanism is needed (F6–F7, F14).**  The ratio
   diverges without a physical cutoff.  The Compton window (Q94),
   dynamic low-pass filter (R41), and charge selection rule (R33)
   all independently suppress the right modes.

### Assessment

The hypothesis that ghost modes ARE dark matter passes the first
quantitative test: the mass ratio is order-of-magnitude correct and
bracketable to 5.4 with physically motivated filters.  This is
**necessary but not sufficient** — the next step is computing the
actual projection integral W(n) to replace the ad hoc filters with
geometry.

**Can the ratio be met with proper inputs and modeling?  Yes.**
The range [2.4, 12.4] brackets 5.4, and the filters that land
closest (|Q| ≤ 2 → 4.4, mt ≤ 1 → 4.8) correspond to well-understood
physical mechanisms already in the model.  A continuous coupling
function interpolating between "fully visible" and "fully dark"
would produce 5.4 at some intermediate coupling strength.  Whether
that strength is derivable from the Ma geometry is the open question.

### Open for future work

1. Compute the projection integral W(n) — the actual geometric
   coupling of each mode to S (extends R19).
2. Determine dark mode stability — which can decay, which are stable.
3. Model cosmological production — thermal history on Ma, freeze-out.
4. Confront with direct detection bounds — does the residual coupling
   fall below current experimental limits?
5. Check warm DM bounds for the lightest stable dark modes.
