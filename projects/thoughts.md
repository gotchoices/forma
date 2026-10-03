# More thoughts on GRID

## Do GRID nodes access all sheets/dimensions?
- In a recent project, we contemplated whether GRID nodes scatter light 
  (propagating information) equally across all dimensions.  IOW, does every
  node have access to every sheet and dimension?
- In early forma models, S and Ma were quite separate notions.  We hypothesized
  that they were coupled at a rate of alpha (1/137) by some unknown mechanism.
  We created a metric to try to model this connection and pondered some type of
  _leakage_ that occurs between different spaces.
- We are in the middle of grid-gravity.  I think we abandoned the idea of nodes
  accessing all sheets.  I'd like to be refreshed on what we came to instead.
- I'm still intrigued by several ideas:
  - Gamma rays of the correct energy, colliding in S can produce particle pairs
    (electron/positron) on the electron sheet (Ma).  There is clearly some
    interaction between S and Ma.
  - A neutron decays into proton, electron, neutrino, plus/minus a little energy
    that can manifest as momentum in S.  It is clear that interaction extends
    also to the Hadron sheets, not just S and leptons.
  - A proton can take on an electron and neutrino to become a neutron (promotion,
    anti-decay, what would we call this?)
  - Likewise electron and positron can collide to become light in S.
  - Either there are separate GRIDs for each sheet/domain and the separate GRIDs
    somehow leak or interact with each other, or, they are all part of the same
    grid.
  - But if they are all part of the same grid, we have determined that the
    simple scattering function (node update rules) can't just apply equally to
    all sheets/domains.

## An alternative node model
- Imagine that each node _does_ have access to every dimension.  For sake of
  the argument, we'll assume dimensions and sheets roughly as outlined in
  projects ma-domain: Multiple dimensions where sheets are the intersection of
  two dimensions.
- Now imagine that nodes are more spacially aware than just treating all edges
  equally.  Rather, the edges of a node belong to a sheet.  A sheet is a plane 
  (we'll assume 2D for now) so that light/information can propagate in the
  same way as we have developed so far.  Light enters a node from one edge.  It
  is scattered back out on the other two connecting edges.  It does not go
  backward simply because of the "add back to the negative of previous value" rule.
- So nodes _can_ interact with multiple sheets.  But momentum is respected.
  And sheets are generally orthogonal to each other.  So light entering on an edge
  can only (normally) scatter to output edges in the same plane.  This perfectly
  preserves momentum because the two output legs each get half of the signal and
  they are disposed at complementary angles to each other.  They each get their
  share of the signal.
- Normally, orthogonal sheets (i.e. other domains) would see none of this energy.
  To get some of it, the momentum/direction of travel would have to make a 90
  degree turn which doesn't make sense intuitively nor from a conservation viewpoint.
- But now let's consider saturation.  When a node attempts to sum all its inputs
  and re-distribute the results, it can get more information in than it _might_
  be able to handle.  It overflows.  We have dealt with this proposition before
  in past studies but we haven't really determined what happens when a discrete
  and bounded computer gets more information than it can handle.
- In a mechanical or fluid analog, we can imagine an accumulator getting more
  force or pressure than it can contain.  It must spill out somewhere.  In a
  mechanical analog, where will it go?  Everywhere, including orthogonal 
  directions.  Momentum is preserved because, even if it makes a 90 degree turn,
  there is an equal amount of material/momentum also going in the opposite
  direction.  This is like a small explosion where extra energy has to go
  somewhere: out.
- In the case of our node, the energy escapes into other sheets.  The main rules:
  - Momentum is preserved so it enters a different sheet, it does so in both
    directions at once. (electron/positron)
  - The energy has to _fit_ into the new domain
  - Either it will be a direct fit (new particles will be created)
  - Or it will be a partial fit.
  - If it is less than a whole particle, the extra energy may merge in with the
    ZPE on that sheet.
  - If it is more than a whole particle, the particle may also be expelled in S
- I propose that, depending on how the electron sheet and neutrino lines are
  disposed relative to each other, it might also be possible to create an
  electron and neutrino at one time (Lepton symmetry/conservation)
  
## Implications for Decay Models
Under this approach, we could look at decay (for example neutron decay) in a
new light:
- The proton sheet has two tracks: proton and neutron
- One neutron quantum is stuck on its track.  At each node, momentum is preserved.
  There is no where for light to go except to stay on its sheet, which keeps it
  circulating around the torus forever.
- However, ZPE (and/or any other transient energy) is the random factor that makes
  it indeterminate.
- If ZPE consists of random fluctuations (can be thought of as virtual particles),
  then saturation is bound to occur in the proton sheet even in the case of a
  well behaved neutron (bound light quantum in a torus).
- When saturation does occur, where will the extra energy go?
- There are various degrees of freedom available, but the energy will have to "fit"
- But magically, the electron sheet and the neutrino line together contain roughly
  the same amount of energy as the difference between a neutron and proton.  So
  when all the random conditions align and saturation occurs, the neutron can
  fall down to a proton, shedding the extra energy and we see the new electron
  and neutrino launched due to the fact that the quanta sizes just "fit" their
  sheets (plus/minus any leftover delta expressed as momentum in S).

## Generalizing the model
- I'm imagining a ladder of energy
- It is most economical/preferrd for energy to live in S.  That is the "lowest"
  state.
- Next on the ladder is neutrinos
- Then electrons, then protons
- More complicated, there are three neutrino lines, three electron sheets and three
  proton (hadron) sheets, each one with its own respective energy requirements
  or levels.
- At the highest energies, it is pretty easy to find lower domains that can accept
  energy.  This makes the particles in those domains very short-lived.  Decay comes
  quickly because there is always somewhere lower to toss the energy into.
- When we get down low, it is harder.  Neutrons do decay but very slowly.  That is
  because there are only a few ways to shed the energy.
- Once you hit proton, you're done.  There is nothing lower unless you could 
  somehow produce a large number of electrons at one time.  Highly unlikely.
- Same thing with electrons and neutrinos.  There is no good outles for the
  energy that preserves momentum.  The only real exception is antimatter
  collisions which are rare simply because antimatter is not preferred by the
  sheet geometry and so is itself rare.
- Result: Ordinary matter (made of atoms) is durable in Ma.
- And there are lots of exotic high energy particles that form kind of a
  "capacitor" of energy storage at the top of the ladder.

## Responses
- Was it grid-gravity (or somewhere else) where we attempted models where
  nodes scatter to all dimensions equally?
- Was ma-domain parked and never really finished?  If so, would this be a
  good path to restart it?

Addressing your 'weaknesses' analysis
1. You're right, I conflate "energy" and "entropy.  Is it feasible to rephrase 
   the thoughts above to use "entropy" correctly?  And can the main premise
   be preserved?
2. My instinct is that baryon/lepton number conservation should be explained at 
   a lower level.  My personal guess: it is conservation of momentum under the
   hood and might be explainable by how the various sheets are disposed in
   relationship to each other.
3. I think I _might_ get fermion pairs to work out right if the sheets are 
   organized correctly.
4. Is there a way to rephrase/recalculate that is consistent?  Does it simply
   mean that extra energy into S is _always_ present?
5. Yes, but with our new geometry-aware nodes, I'm hoping to solve that

On "where it should live":
  - Do we unpark ma-domain for this?

On the pump test:
- I was envisioning the cylinder test (x, c) but x is S and c is the compact dimension
- We could launch two waves from different ends of x and let them collide (and
  saturate) at a collision point.  The extra amount over saturation could overflow
  into c (both directions).  Since the direction of a standing wave on c is
  indeterminate, I think we should get a particle (or two) even though the flow is
  in both directions at once (metric-mass).
- Another possible experiment: Inject all kinds or random energy into x and c that
  is not necessarily resonant in c.  What happens when a wave _not_ matching c's
  circumference is injected?  As it comes around to the starting point, it must be
  come self-consistent.  Does an overflow occur (or many)?  If this energy disperses
  back into x, what random activity continues to boil in c?  Does it resemble ZPE?
  If we could run simulations to see what non-resonant energy does in c, we might
  understand ZPE better.  Does it converge to an average of 1/2 the resonant
  fundamental?  BTW, we might only need to also assume that x is periodic (although
  very large) and we could explain ZPE in S (x) also.
- If these basic tests bear fruit, then some future possibilities:
  - Make a more complex model with Hadron sheets, Lepton sheets, Space
  - Try to model neutron decay


Other thoughts:
- In some past project, we posited a node that has "storage" so it could hang on to
  extra energy above the discrete saturation point and then leak it out on subsequent
  cycles.  This was our posit for how energy is conserved on a discrete GRID.
- But with the ladder o modes being proposed, extra energy is stored in compact
  dimensions (possibly in ZPE) and it can fall back down when there is "room" in
  the discrete numerical capacity.  We get: discrete _plus_ conservation
