# R46: Electron filter — aperture effects on a toroidal cavity

**Status:** Framing
**Questions:** [Q100](../../qa/Q100-aperture-moment-enhancement.md) (aperture moment enhancement),
  [Q53](../../qa/Q53-anomalous-magnetic-moment.md) (g − 2),
  [Q94](../../qa/Q94-compton-window-and-dark-modes.md) (Compton window / ghost filtering)
**Type:** compute / grid simulation
**Depends on:** R44 (g − 2 negative result), R45 (on hold),
  R33 (ghost mode selection), R40 (dynamic torus)

---

## Motivation
The MaSt model, up to this point, has been pretty good at predicting much of observed results.
However, it is off in small to medium amounts in several areas.
One most notable area is in calculating observed anomalous magnetic moments.

It has been noted that a discontinuity (slot, aperture, finite-impedance wall) in a
toroidal cavity modifies the resonant modes in three ways:

1. **Moment enhancement** — the E field bulges through the
   opening, extending the effective current loop area
2. **Mode filtering** — modes with field maxima at the
   aperture drain preferentially; the aperture is a low-pass
   filter via Bethe's (a/λ)⁴ scaling
3. **Charge modification** — the surface integral changes
   when the surface is no longer closed

These may be three aspects of a single mechanism: a discontinuity in the surface of the toroid.

## Questions to be Answered
Some steps are dependent upon the output of prior questions.
- Is a slot a viable alternative to internal shear as a sole mechanism for producing charge?  Or does the slot supplement shear (shear creates the charge distribution on the surface; the slot lets some of it escape into S)?
- If a single slot at a single locus were the sole source of a particle's charge, would this present an assymetric charge distribution?  Is the answer substantially different if the slot were on the inside or outside equator?
- If so, are two slots viable?  **Caution:** Two slots 180° apart in the ring are at the same tube position on opposite sides of the donut — on initial inspection this looks geometrically problematic for centering the charge (both slots on the "outside," no compensation at 90° or 270°).  The even/odd n₂ discrimination argument (in-phase vs anti-phase leakage) may still hold mathematically, but the 3D geometry needs scrutiny.  A more viable approach may be to identify existing asymmetries in the wave function (see R44 F2–F3) and place a single slot to compensate, gaining both symmetry improvement and filtration.
- What about a single slot on the inside equator on a horn (or nearly horn) torus?  Should eliminate electric dipole?  Probably depends on how tall the slot ends up being?
- Is our current model (straight wave equation shear, but no slot) uniform?  Or is it a dipole?  One earlier study (R44?) seemed to indicate that it might not be uniform.  If it is not, maybe a slot on the outside equator that compensates for the shear-induced assymetries (and also has filtration benefits)?
- According to standard methods established for EM wave guides and resonant cavities, what are the equations for charge and magnetic field generated through a slot of a given rectangular dimension.?
- Can we solve for a rectangular slot that produces both the anomalous magnetic moment and observed charge?
- If not, can we solve for a slot that produces observer magnetic moment and then adjust shear to achieve observed charge?
- How many variables are needed to fully characterize a toroid with a vertical filter slot?
- How many can we determine from observed data?
- How many remain free variables remain?
- How does magnetic moment vary with slot dimensions (height and width)?
- Measured alpha is 1/137.036.  Is there any chance that 1/137 (shear) produces expected moment and 1/0.036 (slot) produces the additional anomalous part?
- What general effect will the gap have on frequency response (assuming low pass of some sort)?
- Does our lib/ma_model.py modules have what we need?  Or does it have a bunch of MaSt assumptions baked in?  We may need either a) our own local wave function generator or b) preferably, clean up ma_model so that it _can_ be operated with only fundamental assumptions.

## Strategy
- Go back to fundamentals, don't use, as inputs, any values dervied from past MaSt studies.  For example
  don't put in the size of the electron torus, other than specifying the correct Compton wavelength.
- Calculate the wave function on the slotted torus sheet given known inputs.  This requires the full E/B vector field treatment, not the scalar ψ — charge comes from E_normal through the slot, moment from the Poynting vector.
- Identify which variables are still free
- If necessary, sweep free variables and search domain for key minima
- Generate SVG graphs for user consumption showing key performance
- Attempt to solve for measured anomalous magnetic moment
- Determine if observed charge correct?
- Determine if both charge and moment are a combination of shear and aperture?
- Determine the resulting frequency response of the cavity.  What modes will still ring?  Which ones are blocked?
- If too many open variables to determine slot dimensions, try setting it to desired height to block unwanted ghost modes (the 1,1 ghost in particular is lighter than the electron and problematic).
- Iterate with further tracks if necessary to try to solve as much as possible for the electron.
- If could be helpful to plot the trajectories (particle model) of the three generations on the flat sheet.  Wherever there is resulting gaps is a good candidate for a slot.

## Answers That do not Need Calculation:

**Q: Single slot → asymmetric charge? (line 34)**
Yes, by Gauss's law.  If the only opening is at one location, all
E-field flux exits there.  At large distances the monopole (total Q)
dominates and the charge looks point-like, but the charge center is
offset from the geometric center by roughly the torus radius.  We
estimated the resulting electric dipole moment at ~6 × 10⁻³² C·m,
which is 10¹⁸× the experimental electron EDM limit.  This rules out
a single localized slot as the **sole** source of charge.  However,
if shear produces charge distributed over the full surface (leaking
through a finite-impedance wall), and the slot is a small
perturbation on top of that, the slot-induced asymmetry could be
tiny — a correction to the shear-induced charge, not the whole thing.

**Q: Is the shear-only charge distribution uniform? Where are the asymmetries? (line 37)**
R44 F2–F3 found the charge density is cos(θ₁ + q_eff θ₂) with
q_eff ≈ 2.  This varies in **both** directions on the sheet:

- **Around the tube (θ₁, north-south):** At any fixed ring
  position, the charge oscillates once per cycle — negative at the
  outer equator (θ₁ = 0), positive at the inner equator (θ₁ = π).
- **Around the ring (θ₂, equatorial orbit):** At any fixed tube
  position, the charge oscillates ~2 times per lap (q_eff ≈ 2).
  It crosses zero and **changes polarity** at specific θ₂ values.

The full pattern is diagonal stripes on the unrolled sheet, with
alternating positive and negative regions.  The net charge is −e
only because the torus metric (ρ = R + a cos θ₁) gives more area
weight to the outer equator where the charge is predominantly
negative.

The ring-direction oscillation is significant: there are specific
ring positions where the charge density crosses zero.  These zero
crossings are natural candidates for slot placement — the slot
sits at a "quiet spot" in the charge pattern, minimizing its
perturbation to the net charge while potentially rebalancing
asymmetries and providing filtration.

**Important caveat:** The above is from R44, which this study
should not take as given.  Track 1 will independently compute the
full E-field pattern from first principles and verify (or correct)
this picture.

**Q: How many variables? (lines 41–43)**
Geometric parameters for a torus + one vertical slot: aspect ratio
r = a/R (1), shear s (1), slot ring-position θ₂ (1), slot height h
in tube direction (1), slot width w in ring direction (1) = **5
parameters**.  Compton wavelength is an input from measurement.
Measured constraints: charge = e (1), g − 2 = α/(2π) (1) = **2
constraints** → 3 free.  Additional demands (suppress (1,1) ghost,
allow 3 generations) add constraints but are inequality-type, not
exact — they constrain a region, not a point.

**Q: General frequency response of the gap? (line 46)**
A slot in a cavity wall is a high-pass coupler from the cavity's
perspective: shorter-wavelength (higher-frequency) modes leak more
efficiently.  Bethe's small-aperture scaling gives power ∝ (a/λ)⁴,
where a is the slot size and λ is the mode wavelength.  From the
cavity's perspective this acts as a **low-pass filter on the
resonance spectrum** — the fundamental (longest λ) has the highest Q
while higher harmonics are progressively damped.  This is based
directly on Maxwell's equations for apertures in conducting walls
and does not depend on MaSt-specific assumptions.  Caveat: Bethe
assumes a ≪ λ; if the slot is not small compared to the wavelength,
the scaling changes and must be computed numerically.


## Shared code

This study uses local shared code (`scripts/torus_model.py`) rather
than `lib/*.py`.  The local model is built from first principles —
Maxwell's equations on a torus surface with periodic boundary
conditions — without importing MaSt-specific assumptions.

Each track produces both **SVG plots** for visual inspection and
**data files** (`.npz`) with computed field arrays, so downstream
tracks can load results without re-running.


## Tracks

### Track 1: Baseline EM field on an unslotted torus

**Goal:** Establish the full vector EM field of the (1,2) and (1,1)
eigenmodes on a torus with no slot, as a function of aspect ratio r.

**Method:**
- Solve for the EM eigenmode on a flat periodic rectangle (the
  unrolled torus sheet) with metric g_ij from the torus embedding
- Compute at each surface point: E_normal (perpendicular to
  surface), B_tangential (along surface), Poynting vector S = E × H
- Integrate to get: total charge Q, magnetic dipole moment μ,
  energy distribution
- Reproduce R44 F1–F3 as a validation checkpoint
- Repeat for the (1,1) ghost mode

**Outputs:**
- 2D field maps on the unrolled sheet for E_normal, |B_tangential|,
  |S| — for both (1,2) and (1,1), at several values of r
- Charge density profile (θ₁ cross-section, integrated over θ₂)
- SVG plots for user review

**Inputs:** Compton wavelength (from m_e), aspect ratio r (swept),
shear s (from the α(r,s) relation, R19).  No other MaSt-derived
quantities.

**Depends on:** Nothing — this is the starting point.


### Track 2: Slot coupling — E flux through a rectangular aperture

**Goal:** For the field maps from Track 1, compute what happens
when a rectangular slot of dimensions h × w is placed at various
positions on the torus surface.

**Method:**
- At each candidate slot position (θ₁_center, θ₂_center), extract
  the local E_normal and B_tangential from Track 1
- Integrate E_normal over the slot area → effective charge leakage
  ΔQ for that slot
- Estimate the moment contribution from the fringing Poynting
  vector at the slot (this may require an approximation for the
  fringing field depth — flag if so)
- Compute the same for the (1,1) ghost mode → ghost leakage ΔQ_ghost
- Define a discrimination ratio: ΔQ_ghost / ΔQ_electron — higher
  means the slot filters the ghost more than it affects the electron

**Outputs:**
- Maps of ΔQ(θ₁, θ₂) and discrimination ratio across the torus
  surface, for several slot sizes
- Identification of "sweet spots" where the ghost leaks heavily
  but the electron is minimally affected
- SVG plots showing slot position vs. charge leakage and ghost
  discrimination

**Inputs:** Track 1 field maps, slot dimensions h × w (swept).

**Depends on:** Track 1.




---

## Notes

