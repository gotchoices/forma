# The Ghost in the Machine
### How a theory of matter accidentally predicted dark matter

**Status:** draft — model-D era analysis
**Model era:** [model-D](../models/model-D.md). Ghost mode census
based on waveguide cutoff (R46) and charge selection (R48).
[Model-E](../models/model-E.md) eliminates ghosts differently —
by shear ordering rather than waveguide cutoff — but the dark
matter picture (neutral modes carrying mass without charge) is
preserved.  For current results see [model-E](../models/model-E.md).


## The dark matter problem

Galaxies spin too fast.

This is not a subtle discrepancy.  The stars at the outer edges of spiral galaxies orbit at the same speed as the stars near the center.  By every known law of gravity, they should be flying off into space.  The visible matter — stars, gas, dust — does not have nearly enough mass to hold them in orbit.

Fritz Zwicky noticed the problem first, in 1933, studying galaxy clusters.  They moved as if they contained far more mass than anyone could see.  He called the missing substance *dunkle Materie* — dark matter — and the physics community largely ignored him.

Four decades later, Vera Rubin made it impossible to ignore.  She measured the rotation curves of spiral galaxies with painstaking precision and showed the same pattern in galaxy after galaxy: the curves were flat where they should have been falling.  Something massive and invisible formed a halo around each galaxy, extending far beyond the visible disk.

The search for this invisible mass has consumed decades and billions of dollars.  WIMPs, axions, sterile neutrinos, primordial black holes — physicists have proposed dozens of candidates and built increasingly sensitive detectors.  None has been found.

What we do know, we know precisely.  The Planck satellite, measuring the cosmic microwave background — the afterglow of the Big Bang — pinned the ratio: dark matter is 5.36 times more abundant than visible matter, by mass-energy density.  Multiple independent measurements agree.  We know exactly how much is out there.  We have no idea what it is.


## The little balls problem

Meanwhile, an entirely unrelated line of inquiry was running into its own trouble.

MaSt — Material-Space-Time — is a framework that proposes matter is not made of point particles but of light.  Electromagnetic energy, trapped in the geometry of six compact dimensions called material sheets.  Each particle is a resonant mode: a standing wave on a tiny, closed surface, the way a guitar string vibrates at specific frequencies determined by its length and tension.

The electron, in this picture, is a (1,2) mode — one winding around the tube of the sheet, two around the ring — on a surface roughly the size of the electron's Compton wavelength.  The proton is a mode on a different sheet.  The neutrino, on a third.

The framework works surprisingly well.  Particle masses are computable from the geometry.  Charge emerges from the topological winding of each mode.  Spin comes from the parity of the tube winding number.  Nuclear masses follow a simple scaling law across the periodic table.

But there is a question.


## The ghost problem

When you solve the wave equation on a closed surface, you do not get one solution.  You get all of them.

A rectangular surface with two dimensions supports every combination of winding numbers: (1,1), (1,2), (1,3), (2,1), (2,3), and on and on.  Each is a valid standing wave with a definite energy.  MaSt has three sheets with two dimensions each, and the mode count explodes: below 2 GeV, the model predicts roughly 200–400 modes with definite mass, charge, and spin.

Nature has about 19 observed particles in that energy range.

The ratio is roughly 10–20 to 1.  For every particle that exists, the geometry produces many that have never been observed.  These were called **ghost modes**: mathematically valid solutions with no apparent physical counterpart.

The ghost problem was the model's first hard question.  The geometry produced everything it was supposed to, plus a large surplus.


## Killing the charged ghosts

A series of studies attacked the problem systematically.  Each one applied a new filter and peeled away another layer of excess.  Together, they finished the job for charged modes.

The first insight came from studying how charge works.  In MaSt, charge is not a label attached to a particle — it is a topological invariant: the number of times the wave's phase winds around the tube of the torus.  The GRID lattice can only detect this winding when the tube winding number is exactly |n₁| = 1.  Modes with |n₁| = 0 have no net circulation.  Modes with |n₁| ≥ 2 oscillate so rapidly that positive and negative contributions cancel (R48).  They carry mass, but no charge.

This single rule eliminated the vast majority of ghost modes.

A second filter came from spin.  Spin ½ arises when the tube winding number is odd — a topological fact, not a dynamical rule.  Only modes with odd tube winding on exactly one charged sheet produce the spin-½ fermions that match known particles.

These two filters left only a handful of charged modes per sheet.  The electron IS the (1,2) mode.  But the (1,1) mode — lighter, charged — has no known counterpart.

The (1,1) was eliminated by **waveguide cutoff** (R46).  Each torus is a physical cavity: modes below a frequency threshold cannot propagate and are evanescent.  The (1,1) sits below this cutoff.  The (1,2) electron sits above it.  The geometry itself selects which modes can exist as stable standing waves.  This is not a fitted parameter — it is a consequence of the GRID substrate's reflection coefficient (~0.993, close to a conducting wall).

A further mechanism addresses modes with higher winding numbers.  The **irreducibility criterion** (Q109, R33): a mode (n₁, n₂) with gcd(n₁, n₂) > 1 decomposes into gcd copies of a simpler mode, which then repel each other via Coulomb repulsion and fly apart.  Only modes with gcd = 1 are stable.  On the electron sheet, this means only (1,2) and its antiparticle survive — exactly the electron and positron.  All other charged modes either fail the waveguide cutoff, fission via Coulomb repulsion, or carry the wrong spin.

The charged ghost problem is solved.


## The pivot

With charged ghosts eliminated, the remaining surplus is entirely **electrically neutral modes** — valid standing waves that carry mass but have no tube winding on either charged sheet (n₁ = 0, n₅ = 0).  They cannot radiate, absorb, or scatter electromagnetically.  They are invisible to every detector that relies on electric charge.

The question shifts: are these neutral ghosts a problem, or a prediction?

They are dark matter.


## Why neutral modes are dark matter

Consider what a neutral ghost mode actually is.  It is a valid eigenstate of the wave equation on the material sheets — a real standing wave with a definite, computable mass-energy.  This is not assumed or tuned; it follows directly from the geometry.  A collection of such modes gravitates.  It curves spacetime.  It would show up in galaxy rotation curves.

And it is invisible, by construction.  Charge is topological winding on the tube dimension.  A mode with n₁ = 0 and n₅ = 0 has zero winding on both charged sheets.  It does not interact electromagnetically.  It does not radiate, absorb, or scatter light.  No photon-based detector can see it.

The analogy is an antenna.  An antenna radiates efficiently at wavelengths close to its own physical size and poorly at all others.  The material sheet IS the antenna.  Charged modes fit the aperture and couple to the electromagnetic field.  Neutral modes do not — they interact only gravitationally.

Modes with mass but no electromagnetic interaction.  That is the definition of dark matter.

Neutrality is not merely statistical.  It is exact.  These modes carry zero charge by topology (n₁ = n₅ = 0), not by cancellation of positive and negative contributions.  Every dark mode is individually neutral, not just neutral in aggregate.

Then there is the mass ratio.  The observed dark-to-visible ratio is 5.36 ± 0.05.  The raw mode count ratio overstates the problem, because mode count is not the same as mass-weighted density.  Visible matter is dominated by the proton at 938 MeV.  Many dark modes are lighter.  When you weight by mass and apply physically motivated coupling filters, the computed ratio spans a range that brackets the observed value.  A simple resonant window model with quality factor Q ≈ 350 gives 5.54 (R42).

The ratio has not been derived from first principles.  But it has been shown to be achievable, and the bracket squarely contains 5.4.


## What the dark modes predict

If neutral ghost modes are dark matter, several things follow immediately — all computable, none requiring new parameters.

Dark matter is not a single mystery particle.  It is a forest of discrete states spanning the full energy range from sub-eV (neutrino sheet modes) through tens of keV (electron sheet modes) to roughly 2 GeV (proton sheet modes).  Every candidate mass is computable from the geometry.  Every spin is fixed by the winding numbers.

Dark modes on the same material sheet share a common compact geometry and can interact with each other through mode-mode coupling — energy exchange internal to the compact space, invisible to external observers.  This gives dark matter self-interactions, a feature that some astrophysical observations actually seem to require.  Galaxy rotation curves in certain dwarf galaxies show flat central density profiles ("cores") rather than the sharp peaks ("cusps") that collisionless dark matter simulations predict.  Self-interacting dark matter resolves this.  Dark modes provide it naturally.


## What remains to be done

The hypothesis passes its first quantitative tests, but several pieces remain open.

**The dark mode census.**  R50 catalogs ~200–400 modes below 2 GeV, but the definitive neutral-mode inventory under the (−,−) shear branch and full waveguide filtering has not been compiled.  A clean census — listing every stable neutral mode, its mass, and its spin — is the next concrete step.

**Dark mode stability.**  Some neutral modes may decay to lighter dark modes through internal coupling, altering the spectrum over cosmological time.  The stable endpoint spectrum could differ significantly from the initial one.  The gcd fission criterion applies to charged modes; whether an analogous instability exists for neutral modes is unexplored.

**The cosmological production history.**  How dark modes are populated in the early universe — whether through direct coupling to the hot plasma or through internal Ma processes — determines their relic abundance and velocity distribution.

**Direct detection constraints.**  Neutral modes interact only gravitationally, but any residual coupling through the tail of the Compton window sets a scattering cross-section.  This must fall below the limits established by experiments like LUX-ZEPLIN and XENONnT.

**The ratio 5.4.**  The dark-to-visible mass ratio has been shown to be bracketable but has not been derived from first principles.  The derivation requires the full mode-dependent coupling function W(n), replacing ad hoc filters with geometry.


## The irony

At first glance, the ghost problem looks like the model's greatest weakness: the geometry predicts too many particles.  The natural impulse is to find ways to eliminate them.

But the charged ghosts — the genuinely problematic ones — have been eliminated by the physics itself.  Waveguide cutoff, charge topology, and Coulomb fission leave only the known charged particles.  No ad hoc filters were required.

What remains is the neutral surplus.  And a neutral surplus of massive modes with no electromagnetic interaction is not a problem.  It is a prediction — of a specific, discrete, parameter-free dark matter spectrum that no other theoretical framework has produced.  Every candidate mass is computable.  Every spin is fixed by the winding numbers.  If dark matter is ever detected at a mass that matches a predicted neutral mode — and does not match any known particle — it would be confirmation of a kind that no free-parameter model can offer.  Conversely, detection at a mass that matches no Ma mode would falsify the hypothesis cleanly.

The model does not predict too many particles.  It predicts the right number of visible particles, plus the dark matter.


## Connection to threshold theory

If dark modes are real, they serve a second purpose beyond cosmology.

A visible particle struck by a photon at or above its Compton energy can, in principle, deposit a fraction of that energy into dark modes on its own sheet.  The mechanism is internal mode-mode coupling — energy redistribution within the compact geometry, entirely invisible to external measurements.  The dark modes are valid energy eigenstates.  The energy is real.  But it cannot be detected from outside.

This is exactly what Reiter's threshold theory requires: a mechanism for sub-threshold energy accumulation in degrees of freedom that are invisible to standard quantum measurements.  Energy builds up in dark modes, distributed across the spectrum, until the total reaches twice the particle's rest mass — the threshold for pair production.  The dark mode spectrum provides the substrate.  The Compton window governs how much energy can enter.  The pair-production threshold provides the ceiling.

If this connection holds, neutral dark modes do three jobs simultaneously, with zero new parameters: they explain what dark matter is, they provide the physical mechanism for threshold-driven pair production, and their existence is not optional — the geometry demands them.

Three problems.  One geometric answer.


## Why there is more matter than antimatter

The same geometry that produces dark matter also addresses the oldest puzzle in cosmology: why is there anything at all?

The universe appears to contain far more matter than antimatter.  The Standard Model has no adequate explanation.  Its CP violation — the asymmetry between matter and antimatter processes — comes from a single phase in the quark mixing matrix.  It is measurable, but roughly ten billion times too small to account for the observed excess.

MaSt provides a different source.  The material sheets have a definite shear — a geometric tilt of the lattice that breaks the symmetry between left-wound and right-wound modes.  This is not a fitted parameter; it is the same shear that produces electric charge in the first place.  Without it, there would be no charged particles at all.

The shear has a direction.  The physics of +s and −s are identical — a universe sheared the other way would work exactly the same, with the labels "matter" and "antimatter" swapped.  Neither direction is preferred.  But once chosen, the chirality is frozen into the geometry.

CPT symmetry — the combined operation of flipping charge, reflecting space, and reversing time — is exact.  Every particle and its antiparticle have precisely the same mass.  In thermal equilibrium, their populations are equal.  Shear creates no thermodynamic bias.

But it does create a kinetic bias.  On a chiral sheet, the topological path from free photons to a wound mode is not mirror-symmetric.  The rate of creating matter differs from the rate of creating antimatter — not because one is energetically cheaper, but because the geometric transition is easier in one direction than the other.

This is CP violation from geometry.  Combined with the framework's natural baryon number non-conservation (total winding number, i.e. electric charge, is the only topological invariant — not baryon or lepton number) and the standard cosmological departure from equilibrium, all three Sakharov conditions for baryogenesis are met.

The Standard Model needs new physics to explain the matter excess.  MaSt needs only a sheared sheet — which it already has, for other reasons.

Four problems.  One geometric answer.
