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
- If so, are two slots viable?  It may be difficult to get two slots that don't kill the fundamental.  Note: two slots 180° apart in the ring direction may naturally discriminate even-n₂ modes (electron (1,2) — in-phase leakage) from odd-n₂ modes (the (1,1) ghost — anti-phase, partial cancellation).
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


## Tracks




---

## Notes

