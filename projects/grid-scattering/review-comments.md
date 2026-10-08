# grid-scattering — is there a gap, and can the project be rescued?

**Context.** After several rounds of review, four questions were put:

1. Other GRID models scatter uniformly at every node. Light in space does not drop into a compact dimension to form a particle without some energetic event, and once a particle exists it does not readily evaporate back into space. If a uniform-scattering sheet is rolled into an (x, c) cylinder, information seems to flow freely between x and c. Have past models actually explained the two behaviours, or is there a gap that grid-scattering could fill?
2. Is there a sound way to rescue grid-scattering, so that some threshold has to be exceeded before energy moves between x and c?
3. If so, is that a grid-level effect (the node's scattering rule) or better treated as a large-scale (macro) effect?
4. Answers should be given at the grid or engineering level, not by naming formulas or theories.

**Short answers.**
- The uniform grid already prevents both unwanted behaviours: light does not turn into a particle, and a particle does not evaporate. It manages this by forbidding conversion *entirely*. Even an energetic event cannot make a particle on it. That is the gap, and it is real. Nothing in forma has filled it yet.
<!--EC When you say "forbidding conversion", do you mean by a stated rule (i.e. fiat)?  Or is there some physical interpreation by which conversion is found to be impossible? -->
- A rescue exists, but it reverses the project's question. A gate is not what is missing; the uniform grid has a strong one. What is missing is a **key**: a way for an energetic collision to open the gate, plus a **latch** that holds the result once it is made.
- The **ingredients** belong at the grid level, in the node rule. The **thresholds** come out at the larger scale of a ring and a collision. A hard per-node ceiling puts the threshold at the wrong level, which is the main reason the earlier attempts kept failing.

---

## 1. What the uniform grid already does

### Traffic between x and c is not the same as conversion

On a uniform-scattering cylinder, every node splits its arrivals among all four edges, so energy *does* move onto the c-edges at every tick. That is true at the level of edge traffic. What matters for particles, though, is the **pattern** that traffic forms, and three things keep a light wave's pattern separate from a particle's pattern:
<!--EC What happens if the GRID is used to model all of forma (3 electron sheets, a neutrino line, 3 Hadron sheets)?  Seems like the node would need to have a lot more than 4 edges, maybe 10 or 11.  That means information is diluted much more than in our 4-edge simplified model.  That seems like the very problem I was trying to overcome with grid-scattering project. -->

- **Shape lock.** Light travelling along x is the same all the way around the ring. Every node at a given x does exactly what its ring neighbours do. The c-edges carry traffic, but it arrives equally from both sides and adds up to no net circulation. A particle is a pattern that *goes round* the ring. A uniform node fed a uniform input can only return a uniform output, so no amount of uniform traffic adds up to circulation. grid-matter checked this directly: a ring-uniform light wave on the uniform cylinder put **exactly zero** energy into circulating patterns, however long it ran ([grid-matter results-m1-m2.md](../grid-matter/work/results-m1-m2.md), M1).
<!--EC So in an 11 dimension grid, am I envisioning a complex cylinder with many compact contours and space as the linear dimension?  In a 1D space with many compact dimensions, I'm thinking of a mult-axial cable (coax, triax, 11-ax).  Is that the right picture?  Signals traveling through space are carried on the compact grids as well as the spacial grid, but in the "space direction" and not _around_ the circumference? -->
- **Rhythm lock.** A pattern circulating round the ring has a natural rhythm set by the ring's size: the time for a ripple to go once round. It cannot oscillate slower than that. In signal terms the ring is a **tuned tank circuit** and light is a carrier on a transmission line that runs past it. A carrier below the tank's frequency cannot ring it, however strong the carrier is.
- **Push lock.** Light moving along x always carries forward push in proportion to its energy. A particle at rest has energy but no push along x. Light cannot become a resting particle, and a resting particle cannot become a single light wave, because nothing is present to take up or supply the push. It is like a flywheel spinning in space: it cannot turn itself into a thrown ball, because it has nothing to push against.

### The same locks explain why particles don't evaporate

A circulating pattern at rest has the wrong shape, the wrong push, and a rhythm that no light wave with zero push can share. On the uniform grid it simply stays, and grid-matter's M1 saw exactly that: the circulating mode sat in place, decoupled. To get rid of one, a second pattern circulating the *opposite* way has to arrive. Their circulations cancel, their pushes can balance, and the pair can leave as two light waves going in opposite directions. That is annihilation, and it is the only way out that all three locks allow.
<!--EC This is the one that troubles me.  If I imagine a particle circulating on c and the sheet is made up of Y nodes (our typical GRID format), it seems like the light will be scattering out in both +x and -x at all times (like a propagating wavefront).  I don't see any force keeping the particle coherent at a single location in x. -->

### The answer to question 1

Past models explain both observed behaviours, but too well. A uniform grid is a **linear passive network**: signals pass through one another unchanged, and no signal ever makes a new frequency or a new shape. So in the uniform grid:

- light never becomes matter, **including in an energetic collision**;
- matter never becomes light, **including when particle meets antiparticle**.
<!--EC Actually, I think several studies have claimed that the GRID _must_ be nonlinear at some point (have finite range) in order for the gravity aspects to work. -->

Both conversions happen in nature. The gap is therefore not "why is the gate shut?" but "**what opens it, and only in an energetic event?**" Nothing in forma has answered that:
- grid-matter's pair-production attempt (M2) came back negative;
- grid-matter's compact-phase chapter ([03-compact-phase-focusing.md](../grid-matter/03-compact-phase-focusing.md)) produces stable wound objects, but names their creation from light as future work, not as a result;
- grid-scattering's attempts so far have tried to *build* a gate, and the uniform grid already has one.

The gap is real, it is central, and grid-scattering's original instinct, that something special happens when energy piles up at a node, is aimed at the right place.

---

## 2. A rescue: mixer, tuning, latch

In engineering terms, three components are needed. The tuning is free, because the ring already provides it. The other two have to be supplied at the node.

### The mixer: a node whose stiffness depends on its load

A linear network cannot convert anything because it cannot **mix**. In a radio, two signals fed into a non-linear part (a diode, say) produce new frequencies: their sum and their difference. Whatever tuned circuit sits downstream then picks out the one it responds to.

The GRID version is a node whose behaviour depends a little on how heavily it is loaded. The simplest mechanical picture: the ring edges at a node are springs, and their stiffness rises slightly when a lot of energy is passing through that node along x. One ordinary light wave barely changes the stiffness, so its effect is negligible. Where two strong waves meet head-on, the node is loaded hard and its ring springs stiffen and relax in step with the combined wave.

That rhythmic stiffening is exactly how a child pumps a swing: by standing and squatting, which changes the swing's effective stiffness **twice per swing**. Because the stiffening is the same all round the ring, it does not push the ring in either direction. It pumps clockwise and anticlockwise circulation equally, so what grows is a **matched pair** with opposite circulation. That is the right bookkeeping for a particle and its antiparticle: net circulation zero, as it must be when two light waves are the starting point.

A swing being pumped this way needs a tiny initial wobble to amplify. A perfectly still swing stays still. The grid's background fluctuation supplies that wobble, and the project has already adopted that posit (Appendix B, P5).

### The tuning: where the energy threshold comes from

Pumping only works at the right rhythm: twice the swing's own. For the ring, the collision has to stiffen the springs at twice the ring's natural rhythm, and that happens when each incoming light wave oscillates at the ring's rhythm. Below that, the pumping is out of step and nothing grows, however strong the beams are. Well above it, the extra energy has to go somewhere, and it goes into the pair moving apart.

This is the observed threshold for making a pair from light: each photon has to bring at least one particle's worth of energy. Here it falls out of rhythm matching, with no ceiling to tune. It also explains, in plain terms, why an intense optical laser makes no pairs: pumping a swing at a slow, wrong rhythm achieves nothing, however hard the pushing.

### The latch: why a made particle stays made

Pumping alone is not enough. When the collision is over, a pumped ring that is only *swinging* can hand its energy back through the same mixer, run in reverse. Something has to hold the result.

The mechanical latch is a **pendulum pushed over the top**. Small pushes make it swing and come back. A push past the top turns it into a rotor that keeps going round, and the number of times it has gone round is locked in: stopping it means pushing it back over the top the other way. If a node's ring register is a **dial**, a value on a circle like a pendulum's angle, rather than a value on an unbounded line, a ring pumped hard enough reaches a point where its pattern goes over the top. After that it is a locked circulation, and it cannot quietly drain back into space. Removing it needs either a large push of its own or an opposite circulation to cancel against, which is annihilation.

This gives a second, genuine threshold: the **lock-in**. Below it the ring rings during the collision and empties afterwards: energy flows in and back out and leaves no particle behind. Above it the ring locks and a particle remains. It also gives the all-or-nothing character in a classical grid: a circulation count is a whole number by its nature, so there is no such thing as half a lock.

As a check: a field strong enough can force the pendulum over the top regardless of rhythm. That matches the fact that sufficiently extreme fields are expected to tear pairs out without any frequency matching. This is a qualitative consistency check, not a prediction.

### How the original intuition fits

The originating notes reasoned that a bounded register overflows and the excess must go somewhere. The earlier reviews pointed out that a bounded register more naturally **wraps** than spills. Wrapping is exactly the dial. A register that wraps on overflow *is* the pendulum that can go over the top. So the rescue does not abandon the overflow idea. It reads overflow as **wrap**, which gives the latch, rather than as **spill**, which gave the ceiling that failed. Saturation can also be read as **stiffening under load** (the mixer) rather than clipping (a wall). Both readings stay close to the original thinking, and both avoid the specific failures recorded in the review files.

---

## 3. Grid-level or macro-level?

Both, at different layers:

| Layer | What lives there | Why |
|---|---|---|
| **Node (grid level)** | The mixer: ring stiffness depends slightly on the node's load. The latch: the ring register is a dial, not a line. | These are local, mechanical properties of one node. A node can know them without knowing anything about rings or particles. |
| **Ring and collision (macro level)** | The energy threshold (rhythm match to the ring), the lock-in threshold (enough pumping to go over the top), and the conversion rate (how strong the mixing is, multiplied by both beams). | These depend on the ring's size and on two waves arriving together. No single node has that information. |

This is why the per-node ceiling kept failing. A ceiling asks one node to decide whether a particle should form, but the node cannot know the ring's rhythm, whether the energy fits, or whether a partner wave is present. A node should only supply **behaviour**: mild stiffening under load, and a value that wraps. Thresholds are **emergent**. They are what that behaviour does when it acts on a ring of a given size during a head-on collision. The engineering parallel is a radio receiver: the diode does not know which station is wanted; the tuned circuit after it decides.

The same split explains why conversion is **rare**. If the mixing is weak, which is a node property, an energetic collision usually passes straight through, and only occasionally pumps a pair up to lock-in. That gives a natural place for small coupling rates to come from.

---

## 4. What this would mean for grid-scattering

- **Keep the uniform scatter.** It already supplies the shape, rhythm and push locks, and it already gives particles proper motion and inertia on this lattice (grid-matter ch. 4). The edge-grouping posit of §2 makes no observable difference in linear running (review-4, M1), and it was the source of the motion problem across the last three rounds. Dropping it removes that whole branch of difficulty.
- **Recast the question** from "what keeps energy out of the sheet?" (already answered) to "**what lets an energetic collision put a locked pair into the sheet, and what sets how often?**"
- **Experiments, cheapest first, with expectations stated in advance:**
  1. *Gate check.* On the uniform cylinder, drive single beams and head-on beams at a range of rhythms with no mixer. Expected: nothing circulates, ever. This already holds, and it is the control for everything else.
  2. *Mixer and tuning.* Add load-dependent ring stiffness and a small background. Collide two beams head-on and measure how fast circulating content **grows** while the drive is on, across a range of beam rhythms. Expected: growth only near the rhythm that matches the ring; growth rate rising with the product of the two beam strengths; a single beam does nothing.
  3. *Latch.* Make the ring register a dial. After the drive stops, does the circulation drain back (no lock) or stay (lock)? Expected: a sharp step in what is retained as drive strength rises. That step is the particle threshold.
  4. *Annihilation.* Bring a locked clockwise ring and a locked anticlockwise ring together. Expected: the locks cancel and the energy leaves as light going both ways.
  5. *Above threshold.* Drive above the matching rhythm. Expected: the pair forms and moves apart, with the extra energy appearing as motion and not as a heavier object at rest.

---

## 5. What remains uncertain

- **Two new posits.** The dial-valued register and load-dependent stiffness are both posits. grid-matter already posits the dial (its compact-phase premise) and records that it does not follow from the bare scatter. The two projects would then share one foundational assumption, which is better than two independent ones but should be stated plainly.
- **One dimension only.** The cylinder has one space direction. A locked circulation that is a compact, localized particle in three dimensions has not been shown anywhere in forma (grid-matter lists it as owed). The latch makes the circulation permanent; it does not by itself make it small in space.
- **Overlap with grid-matter.** grid-matter's M2 line names this event in almost the same words: "pair production = a whole-quantum / ±1-winding creation event at a saturation collision". Which project owns the experiments is a scoping decision. The physics question is the same in either home.
- **Size of the quantum.** The latch makes circulation come in whole counts. It does not set the energy of one count in the units physics uses; that runs through the ring size and the action-per-cycle scale, which other projects carry. This matches the principle-versus-scale distinction the repo already draws.
- **Risk to light.** If the mixing is too strong, ordinary light crossing ordinary light would start to interact, and observation allows only extremely weak light-on-light effects. That puts a ceiling on mixer strength. Measured against the observed conversion rates, it may squeeze the mechanism hard, and that is worth checking early.

<!--EC The purpose of grid-scattering was to investigate a model where the scattering function is _not_ uniform.  You have outlined how to "rescue" the project, but I wonder if what you're really saying is that we should be investigating explanations for particle production and anihallation under a uniform system.  I wonder if this project should be parked and the work should continue in a different project.  Is there an existing, open project where this work would best live?  Or is your opinion that this project should be adapted to the task.  It is really filled with a lot of failed attempts at non-uniform scattering (at the moment). -->