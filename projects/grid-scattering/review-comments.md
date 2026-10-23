# grid-scattering — is there a gap, and can the project be rescued?

**Context.** After several rounds of review, four questions were put:

1. Other GRID models scatter uniformly at every node. Light in space does not drop into a compact dimension to form a particle without some energetic event, and once a particle exists it does not readily evaporate back into space. If a uniform-scattering sheet is rolled into an (x, c) cylinder, information seems to flow freely between x and c. Have past models actually explained the two behaviours, or is there a gap that grid-scattering could fill?
2. Is there a sound way to rescue grid-scattering, so that some threshold has to be exceeded before energy moves between x and c?
3. If so, is that a grid-level effect (the node's scattering rule) or better treated as a large-scale (macro) effect?
4. Answers should be given at the grid or engineering level, not by naming formulas or theories.

**Short answers.**
- The uniform scatter, as written and simulated, already stops both unwanted behaviours: light does not turn into a particle, and a particle does not turn back into light. It does this by ruling out conversion *entirely*. Even an energetic event cannot make a particle with it. That is not a rule anyone wrote in; it follows mechanically from the scatter being linear (§1). That is the gap, and it is real. Nothing in forma has filled it yet.
- A rescue exists, but it reverses the project's question. A gate is not what is missing; the uniform scatter has a strong one. What is missing is a **key**, a way for an energetic collision to open the gate, and a **latch** that holds the result once it is made. forma has probably posited both already, in other projects (§2).
- The **ingredients** belong at the grid level, in the node rule. The **thresholds** come out at the larger scale of a ring and a collision. A hard per-node ceiling puts the threshold at the wrong level, which is the main reason the earlier attempts kept failing.

---

## 0. What made the questions necessary

Four things in the earlier material were left unclear, and the questions grew out of them. Stating them first makes the answers easier to follow.

1. **Edge traffic and patterns were run together.** Under the uniform scatter, a node sends part of every arrival down every edge, so energy plainly reaches the compact edges at every tick. Read that way, "energy flows freely between x and c" sounds right, and something seems needed to stop it. The relevant question is a different one: whether the *pattern* the energy forms can change from "travelling along x" to "circulating round the ring". Edge traffic is constant; pattern change is forbidden (§1). The earlier reviews talked in terms of patterns without saying that this is a different and stricter thing than traffic.
2. **More dimensions looked like more leakage.** A node in the full forma picture (three electron sheets, three hadron sheets, a neutrino line, space) has many more edges than the four in the simplified cylinder. Under the uniform scatter a single arrival is shared out more thinly. Most of it bounces back and each other edge gets a sliver. That thinning-out was a large part of what motivated grid-scattering. Whether it actually lets energy escape into other sheets was never stated plainly (§1, "Many dimensions").
3. **"Doesn't evaporate" covered two separate questions.** A particle could disappear by turning back into light, or by smearing out along x until it is no longer a lump. The uniform scatter prevents the first. It does **not** prevent the second, and the earlier answer did not separate them (§1, "Two ways a particle could go away").
4. **"The grid is linear" was too strong.** The uniform scatter is linear, but forma's substrate is not committed to being linear. grid-gravity's working premise already builds in a nonlinearity, and the rescue should use it rather than invent a new one (§1, "The scatter is linear; the substrate need not be").

---

## 1. What the uniform scatter already does

### Ruled out by consequence, not by decree

The uniform scatter is a fixed recipe: each outgoing signal is the same fixed blend of the incoming ones, every tick, whatever their size. Nobody added a rule saying "no conversion". Two mechanical consequences of using a fixed blend do the work:

- **Signals pass through each other untouched.** As in a passive resistor network, two signals present at once each behave as though the other were absent. Put a sine wave in and the output is a sine wave of the same frequency. A fixed blend cannot make a new frequency, any more than a resistor divider can make harmonics.
- **A symmetric input gives a symmetric output.** If every node round a ring receives the same thing, every node does the same thing, so the ring as a whole cannot start circulating.

Together these give the three locks below. They have been measured, not only argued: grid-matter ran a ring-uniform light wave on the uniform cylinder, and **exactly zero** energy entered circulating patterns, however long the run ([grid-matter results-m1-m2.md](../grid-matter/work/results-m1-m2.md), M1). The only actual choice was the fixed blend itself, and it was made because it reproduces light correctly.

### Traffic between x and c is not the same as conversion

Energy *does* move onto the c-edges at every tick. What matters for particles is the **pattern** that traffic forms, and three things keep a light wave's pattern separate from a particle's:

- **Shape lock.** Light travelling along x is the same all the way round the ring. The c-edges carry traffic, but it arrives equally from both sides and adds up to no net circulation. A particle is a pattern that *goes round* the ring, and uniform traffic cannot add up to one.
- **Rhythm lock.** A pattern circulating round the ring has a natural rhythm set by the ring's size: the time for a ripple to go once round. It cannot oscillate slower than that. In signal terms, the ring is a **tuned tank circuit** and light is a carrier on a transmission line running past it. A carrier below the tank's frequency cannot ring it, however strong.
- **Push lock.** Light moving along x always carries forward push in proportion to its energy. A particle at rest has energy but no push along x. Light cannot become a resting particle, and a resting particle cannot become a single light wave, because nothing is there to take up or supply the push. A flywheel spinning in space cannot turn itself into a thrown ball, because it has nothing to push against.

### The cable picture

A multi-conductor cable (coax, triax, an "11-ax") is the right mental model, with one refinement. In a real coax the layers are nested shells. In the GRID picture, every point along the cable carries **all** of the small loops at once: one loop for each compact direction, all present at every point, rather than one wrapped around another. Space is the long axis of the cable, and the cross-section is the combined set of small loops.

- **Light** is a signal that travels along the cable and is the same all the way round every loop. It uses the compact edges, since the fields fill the whole cross-section, but only in the *along-the-cable* sense, never circulating. This matches a real coax's main mode, whose field is the same all the way round the circumference.
- **A particle** corresponds to a coax's **higher-order modes**: field patterns that vary *around* the circumference. Real cables have these, and each one has a **cutoff frequency** set by the circumference:
  - below cutoff the mode cannot travel at all;
  - exactly at cutoff it rings in place without travelling, which is a particle at rest;
  - above cutoff it travels, but slower than the main signal, which is a particle in motion moving slower than light.

  This is the engineering picture of mass the framework uses.
- **Mode conversion.** In a perfectly round, uniform cable the main mode never turns into a higher-order mode. In RF practice, conversion comes only from a **defect** (a bend, a dent, a connector) or a **nonlinear** component. A uniform grid has no defects. The only way in is therefore a nonlinearity, and §2 is about that.

### Many dimensions: the edges thin out, but no leak opens

The thinning-out is real. With N edges at a node, the uniform scatter bounces back a share of 1 − 2/N of a single arrival and sends only 2/N on along each of the other edges. At 4 edges half bounces back; at 22 edges (eleven dimensions, two edges each) roughly nine-tenths does. Each other edge gets less than a tenth.

A travelling wave, though, is not one arrival. It is a coordinated front arriving on many edges at once. For a front moving along the cable and uniform round every loop, the sideways shares from opposite sides of each loop cancel, and the bounced shares from successive nodes add up to a front that keeps moving along the cable. Thinning changes:
- **how fast** the front moves, counted in nodes per tick: it is slower with more edges, which is a matter of calibration (grid-matter measured about 0.62 nodes per tick at 4 edges);
- **how grainy** short waves look on the lattice.

It does **not** change whether the front's energy is diverted into circulating patterns. The shape lock holds separately for each loop: a front that is uniform round loop A, loop B, and so on stays uniform round every one of them. With more edges the energy is spread more thinly across more edges, but no new route to conversion appears. The intuition behind grid-scattering, that the thinning had to be stopped, was aimed at edge traffic, and edge traffic was never the route by which light becomes matter.

### Two ways a particle could go away

- **Turning back into light.** The uniform scatter rules this out. A circulating pattern at rest has the wrong shape, the wrong push, and a rhythm no light wave at rest can share. Energy that a ring node sends down its x-edges belongs to the same circulating pattern: neighbouring rings receive it as circulation, not as light. Getting rid of a particle needs a second pattern circulating the *opposite* way. Their circulations cancel, their pushes can balance, and the pair can leave as two light waves going in opposite directions. That is annihilation, and it is the only way out that all three locks allow, once something can mix (§2).
- **Smearing out along x.** The uniform scatter does *not* prevent this, and the concern is well founded. Picture a particle circulating on c built from Y nodes. Every tick, each node passes some of the circulation on to its x-neighbours, so the circulation spreads in both x directions, much as a wavefront would. In cable terms, a short burst of a higher-order mode near cutoff is made of slightly different frequencies just above cutoff, which travel at slightly different slow speeds, so the burst stretches out along the cable. Nothing in a fixed-blend scatter holds it together. grid-matter states the same thing as its starting point: on the linear substrate "a localized massive mode … spreads … Binding therefore requires a nonlinearity that holds the mode together" ([grid-matter ch. 2](../grid-matter/02-why-simple-binding-fails.md)).

  So "doesn't evaporate" holds in the sense that the particle does not turn into light. It fails in the sense that the particle does not stay a lump. The second is the **binding** problem, and it needs a nonlinearity just as creation does.

  One qualification: whether a free particle *should* stay a lump is a separate question. In quantum mechanics a free particle's wave does spread; what stays whole is what a detector records. grid-matter's quantum-mechanics chapters take that reading. Either way, a nonlinearity is what makes a localized, self-holding lump possible, and grid-matter's compact-phase chapter ([ch. 3](../grid-matter/03-compact-phase-focusing.md)) supplies one: on the (x, c) lattice it produces a long-lived, mobile lump that pulls itself together instead of spreading.

### The scatter is linear; the substrate need not be

Several projects already conclude that the GRID cannot be linear all the way down. grid-gravity's working premise is a **finite-bandwidth bound**: a node can change its state only so fast, a fixed number of bits per tick ([grid-gravity README](../grid-gravity/README.md), working premise; [ledger](../grid-gravity/work/ledger.md) B). Its gravity is the steady, rectified part of the substrate's own response to that bound.

In engineering terms this is a **slew-rate limit**, the maximum rate at which an amplifier's output can change. A slew-limited stage behaves perfectly linearly for signals that are small or slow, and distorts, generating new frequencies, for signals that are large *and* fast. What triggers it is the signal's steepest slope, which grows with both its height and its frequency. grid-gravity also found independently that a bound on the signal's *value* gives light a mass, while a bound on its *rate* does not. That is the same failure the third review measured for a constant x↔c rotation.

So the conclusion "the uniform grid can never convert" holds for the scatter as written and simulated. It does not hold for forma's substrate, which is already committed to a nonlinearity. That changes the rescue. The key may not need inventing at all.

### The answer to question 1

Past models explain both observed behaviours through the linear scatter, and they explain them too well. Light never becomes matter, **even in an energetic collision**. Matter never becomes light, **even when particle meets antiparticle**. Both conversions happen in nature. A localized particle also spreads along x unless something holds it together.

The gap is therefore not "why is the gate shut?" but "**what opens it, and only in an energetic event?**", together with the related question "**what holds a made particle together?**" forma has the pieces but has not put them together:
- grid-matter's pair-production attempt (M2) came back negative, using clip and spillover responses;
- grid-matter's compact-phase chapter produces self-holding wound objects but leaves their creation from light as future work;
- grid-gravity's bandwidth nonlinearity has only been applied to gravity;
- grid-scattering's attempts so far have tried to *build* a gate, and the uniform scatter already has one.

grid-scattering's original instinct, that something special happens when energy piles up at a node, is aimed at the right place.

---

## 2. A rescue: mixer, tuning, latch

In engineering terms, three components are needed. The tuning is free, because the ring provides it. The other two are node properties, and each has already been posited elsewhere in forma.

### The mixer: a node that responds differently to large, fast signals

A linear network cannot convert anything because it cannot **mix**. In a radio, two signals fed into a non-linear part (a diode, say) produce new frequencies, their sum and their difference, and whatever tuned circuit sits downstream picks out the one it responds to.

The GRID version is a node whose response changes slightly when it is heavily loaded. One mechanical picture: the ring edges at a node are springs that stiffen slightly when a lot of energy is passing through the node. The slew-limit picture from grid-gravity has the same effect. Ordinary light barely notices either. Where two strong waves meet head-on, the node is driven hard, and its ring response stiffens and relaxes in step with the combined wave.

That rhythmic stiffening is how a child pumps a swing: standing and squatting changes the swing's effective stiffness **twice per swing**. Because the stiffening is the same all the way round the ring, it does not push the ring in either direction. It pumps clockwise and anticlockwise circulation equally, so what grows is a **matched pair** of opposite circulations. That is the right bookkeeping for a particle and its antiparticle: net circulation zero, as it must be when two light waves are the starting point.

A swing pumped this way needs a tiny initial wobble to amplify; a perfectly still swing stays still. The grid's background fluctuation supplies the wobble. The project has already adopted that posit (Appendix B, P5).

The economical hypothesis is that **the mixer is grid-gravity's bandwidth nonlinearity**: one substrate nonlinearity whose steady part is gravity and whose twice-rhythm part pumps pairs. grid-gravity already lists "a resonant second harmonic" among that nonlinearity's side effects. A twice-rhythm response is exactly what pumping needs. A slew limit also triggers on height *and* frequency, which bears directly on the earlier objection that pair creation depends on photon energy rather than field strength: high-frequency signals hit a rate limit at much lower amplitude than slow ones. Whether the two roles really are one nonlinearity is a hypothesis to test, not a result.

### The tuning: where the energy threshold comes from

Pumping only works at the right rhythm, twice the swing's own. For the ring, the collision has to drive the stiffness at twice the ring's natural rhythm, and that happens when each incoming light wave oscillates at the ring's rhythm. Below that the pumping is out of step and nothing grows, however strong the beams. Well above it, the extra energy has to go somewhere, and it goes into the pair moving apart.

This is the observed threshold for making a pair from light: each photon has to bring at least one particle's worth of energy. Here it comes from rhythm matching, with no ceiling to tune. It also explains, in plain terms, why an intense optical laser makes no pairs: pumping a swing at a slow, wrong rhythm achieves nothing, however hard the pushing.

### The latch: why a made particle stays made

Pumping alone is not enough. When the collision is over, a ring that is only *swinging* can hand its energy back through the same mixer, run in reverse. Something has to hold the result.

The mechanical latch is a **pendulum pushed over the top**. Small pushes make it swing and come back. A push past the top turns it into a rotor that keeps going round, and the number of times it has gone round is locked in: stopping it means pushing it back over the top the other way. If a node's ring register is a **dial**, a value on a circle like a pendulum's angle, rather than a value on an unbounded line, a ring pumped hard enough reaches a point where its pattern goes over the top. From then on it is a locked circulation and cannot quietly drain back into space. Removing it takes either a large push of its own or an opposite circulation to cancel against, which is annihilation.

This gives a second, genuine threshold, the **lock-in**. Below it the ring rings during the collision and empties afterwards, leaving no particle. Above it the ring locks and a particle remains. It also gives the all-or-nothing character in a classical grid: a circulation count is a whole number by its nature, so there is no half a lock.

The dial is grid-matter's compact-phase premise, and in grid-matter that same premise is what **holds a lump together**: the dial's periodic restoring force pulls a localized mode inward instead of letting it spread. So one ingredient addresses both lock-in and the smearing-out problem of §1.

As a check: a field strong enough can force the pendulum over the top regardless of rhythm, which matches the expectation that sufficiently extreme fields tear pairs out without frequency matching. This is a qualitative consistency check, not a prediction.

### How the original intuition fits

The originating notes reasoned that a bounded register overflows and the excess must go somewhere. A bounded register more naturally **wraps** than spills, and wrapping is exactly the dial: a register that wraps on overflow *is* a pendulum that can go over the top. So the rescue does not abandon the overflow idea. It reads overflow as **wrap**, which gives the latch, rather than as **spill**, which gave the ceiling that failed. Saturation becomes a **limit on how fast a node can respond**, which gives the mixer, rather than a clip, which is a wall. Both readings stay close to the original thinking and avoid the specific failures recorded in the review files.

---

## 3. Grid-level or macro-level?

Both, at different layers:

| Layer | What lives there | Why |
|---|---|---|
| **Node (grid level)** | The mixer: the node's response changes slightly under heavy, fast load. The latch: the ring register is a dial, not a line. | These are local, mechanical properties of one node. A node can have them without knowing anything about rings or particles. |
| **Ring and collision (macro level)** | The energy threshold (rhythm match to the ring), the lock-in threshold (enough pumping to go over the top), and the conversion rate (mixing strength, multiplied by the strength of both beams). | These depend on the ring's size and on two waves arriving together. No single node has that information. |

This is why the per-node ceiling kept failing. A ceiling asks one node to decide whether a particle should form, but the node cannot know the ring's rhythm, whether the energy fits, or whether a partner wave is present. A node should supply only **behaviour**: a response that changes under heavy, fast load, and a value that wraps. Thresholds are **emergent**. They are what that behaviour does to a ring of a given size during a head-on collision. The engineering parallel is a radio receiver: the diode does not know which station is wanted; the tuned circuit after it decides.

There is one partial exception, and it is worth noting because it is close to the original idea. A slew limit *does* act as a per-node threshold, in signal height combined with frequency. Below it a node is exactly linear. So there is a legitimate grid-level threshold, for when mixing **can** happen. Whether a particle **does** form is still settled at the ring.

The same split explains why conversion is **rare**. If the mixing is weak, a node property, an energetic collision usually passes straight through and only occasionally pumps a pair to lock-in. That gives a natural place for small coupling rates to come from.

---

## 4. What this would mean for the work

- **Keep the uniform scatter.** It already supplies the shape, rhythm and push locks, and it already gives particles proper motion and inertia on this lattice (grid-matter ch. 4). The edge-grouping posit of README §2 makes no observable difference in linear running (review-4, M1), and it caused the motion problems across the last three rounds.
- **Recast the question** from "what keeps energy out of the sheet?" (already answered) to "**what lets an energetic collision put a locked pair into the sheet, and what sets how often?**"
- **Experiments, cheapest first, with expectations stated in advance:**
  1. *Gate check.* On the uniform cylinder, drive single beams and head-on beams at a range of rhythms, with no mixer. Expected: nothing circulates, ever. This already holds, and it is the control for everything else.
  2. *Mixer and tuning.* Add a rate-limited (slew-limited) node response and a small background. Collide two beams head-on and measure how fast circulating content **grows** while the drive is on, across a range of beam rhythms. Expected: growth only near the rhythm that matches the ring; growth rate rising with the strength of both beams together; a single beam does nothing.
  3. *Latch.* Make the ring register a dial. After the drive stops, does the circulation drain back (no lock) or stay (lock)? Expected: a sharp step in what is retained as drive strength rises. That step is the particle threshold.
  4. *Coherence.* Does a locked circulation stay a lump in x, or spread? Expected, from grid-matter ch. 3: with the dial it holds together; without it, it spreads.
  5. *Annihilation.* Bring a locked clockwise ring and a locked anticlockwise ring together. Expected: the locks cancel and the energy leaves as light going both ways.
  6. *Above threshold.* Drive above the matching rhythm. Expected: the pair forms and moves apart, with the extra energy appearing as motion, not as a heavier object at rest.

### Where the work should live

The project's charter was to test a scattering function that is **not uniform**. Every attempt made it non-uniform *across edges* (grouping by sheet, junction rules, a fixed x↔c rotation), and those attempts are the failures the reviews recorded. The rescue keeps the edges uniform but makes the scattering function **non-constant in the signal**: a node whose response depends on how hard and how fast it is driven. Three homes are possible:

- **grid-scattering, re-chartered.** Its subject stays the node scattering function, which is what the name describes. The re-charter changes "non-uniform across edges" to "non-constant under load". The failed geometric attempts become a short, legitimate negative record: what does *not* need to be added to the scatter, and why. This is the piece that sits *between* the other two projects: grid-gravity owns the nonlinearity's steady effect, grid-matter owns the dial and binding, and neither has the conversion channel in scope.
- **grid-matter.** It owns the cylinder testbed, the dial, binding, and the open M2 pair-production line, so the physics fits naturally. However, its matter half is recorded as largely done and its frontier has moved to quantum mechanics. Adding creation and annihilation would reopen a finished part of its arc.
- **grid-gravity.** It owns the bandwidth nonlinearity, but it is parked, and its open problem (range) is unrelated.

The assessment here is that the first option fits best. The open question is a node-scattering question, and it is the missing link between two other projects rather than an extension of either. If grid-scattering is re-chartered, the README would read best rebuilt around mixer, tuning and latch, with the current material compressed into an appendix of negative results. The choice, including whether to park and start fresh, is a scoping decision for the project owner.

---

## 5. What remains uncertain

- **Posits, possibly none new.** The dial is grid-matter's compact-phase premise, and the mixer may be grid-gravity's bandwidth bound. If both identifications hold, the rescue adds no new foundational assumption; it puts existing ones together. If the mixer turns out to need to be something other than the bandwidth bound, that is one new posit, and it should be stated as such. grid-matter notes that the dial does not follow from the bare scatter, so it remains a posit in either case.
- **One dimension only.** The cylinder has one space direction. A locked circulation that is a compact, localized particle in three dimensions has not been shown anywhere in forma (grid-matter ch. 5 lists it as owed). The latch makes the circulation permanent and, in one dimension, self-holding; three-dimensional localization is a further step.
- **Size of the quantum.** The latch makes circulation come in whole counts. It does not set the energy of one count in physical units; that runs through the ring size and the action-per-cycle scale carried by other projects, consistent with the principle-versus-scale distinction the repo already draws.
- **Risk to light.** A nonlinearity strong enough to make pairs also makes ordinary light interact with ordinary light, and observation allows only extremely weak effects of that kind. grid-gravity lists the same hazard for its own nonlinearity. That caps the mixer's strength. Checked against the observed conversion rates, the cap may squeeze the mechanism hard, so it should be checked early, and once, for both projects together.
