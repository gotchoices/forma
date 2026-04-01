# Across and Through: Nature's Conjugate Pattern

**Status:** Draft
**Audience:** Anyone with basic science literacy (no circuits or
EM background assumed)
**Purpose:** On-ramp to understanding why the GRID lattice
naturally produces electromagnetic behavior

---

## 1. The pattern in everyday experience

Push a box across the floor.  Two things determine how much
work you're doing: how hard you push, and how fast the box
moves.  Push hard on a stationary box — no work.  A box
sliding freely with no push — no work being done on it.
Work requires both: force AND motion, happening together.

Now think about a garden hose.  Two things determine how
much water-energy you're delivering: the pressure behind the
water, and how fast it flows.  Pinch the nozzle — high
pressure, low flow.  Open it wide — low pressure, high flow.
The power delivered is pressure × flow rate.

Notice the structure.  In both cases there are two variables,
and neither one alone carries energy.  You need both,
multiplied together, to get power.  This is not a
coincidence.  It is a pattern that runs through all of
physics.

The two variables have names.  The "push" — force, pressure,
voltage — is called the **across** variable (it acts across
the system, from one side to the other).  The "flow" —
velocity, current, flow rate — is called the **through**
variable (it passes through the system).  Their product is
always power.

---

## 2. The pattern across domains

Here's the remarkable thing: this isn't just a feature of
boxes and garden hoses.  The same paired structure appears in
every domain of physics where energy moves through a medium.

| Domain | Across variable | Through variable | Power |
|--------|:---------------:|:----------------:|:-----:|
| Pushing a box | Force | Velocity | F × v |
| Water in a pipe | Pressure | Flow rate | P × Q |
| Sound in air | Pressure variation | Air velocity | p × u |
| Rope or string | Tension | Transverse velocity | T × v |
| Electric circuit | Voltage | Current | V × I |
| Electromagnetic wave | Electric field (E) | Magnetic field (H) | E × H |
| Heat flow | Temperature | Entropy flow rate | T × dS/dt |

Seven domains.  Seven instances of the same structure.
In every case:

- **Across × through = power.** This is the definition of
  the conjugate pair.  You can verify it experimentally in
  each domain.

- **The medium determines the ratio.**  A stiff medium
  (steel, high-pressure pipe, vacuum) relates a given
  "push" to a smaller "flow."  A soft medium (rubber, wide
  pipe, lossy cable) relates the same push to a larger flow.
  This ratio — across divided by through — is a property
  of the medium.  It has a name: **impedance**.

- **Waves carry both, simultaneously.**  A sound wave is not
  pure pressure or pure air motion — it is both, oscillating
  together, peaking at the same moment.  A wave on a rope is
  not pure tension or pure displacement — it is both.  In a
  traveling wave, the two variables rise and fall in lockstep.
  This is what it means to carry power in one direction:
  across × through is always positive, so energy flows
  steadily forward.

  (Standing waves are different — there the two variables
  ARE 90° out of phase, energy sloshes back and forth, and
  no net power flows.  This distinction matters later: in
  the MaSt framework, particles are standing waves — trapped
  energy oscillating between across and through storage on
  compact geometry.)

This is not a loose analogy.  The equations governing each
domain have the same mathematical form.  A sound wave in a
pipe and a voltage wave in a cable obey identical equations
with different variable names.  Physicists call this an
**isomorphism** — a structural identity, not a resemblance.

---

## 3. What impedance means

Impedance deserves its own section because it is the key to
everything that follows.

### The concept

Imagine a long line of people passing buckets of water.  How
fast the line moves buckets (the "through") depends on how
heavy the buckets are and how strong the people are.  That
combination — the relationship between effort and flow — is
the impedance of the bucket line.

In physics: impedance is how much "across" you need to
produce a given "through."  It is a property of the medium, not of
the wave.  The same wave entering two different media will
produce different ratios of across to through — because the
media have different impedances.

A few examples of what impedance feels like:

| Medium | Impedance feels like... |
|--------|------------------------|
| Steel rod | Tap it: huge force, tiny motion.  **High impedance.** |
| Rubber band | Pull it: small force, large stretch.  **Low impedance.** |
| Narrow pipe | Small flow, high pressure.  **High impedance.** |
| Wide pipe | Large flow, low pressure.  **Low impedance.** |
| Vacuum (for light) | Specific ratio of E to H: Z₀ ≈ 377 Ω.  **Measured and finite.** |

### What happens at a boundary

When a wave hits a boundary between two materials with
different impedances, some energy reflects and some
transmits.  This is why you see a faint reflection in a
window (glass and air have different optical impedances), why
an echo comes back from a canyon wall (rock and air have
different acoustic impedances), and why a signal bounces at
the end of a mismatched cable.

The rule is simple: the greater the impedance mismatch, the
more energy reflects.  Perfect impedance match = zero
reflection = all energy transmitted.  This is called
**impedance matching**, and engineers use it constantly — in
antenna design, audio systems, fiber optic connectors, and
anywhere energy needs to pass efficiently from one medium to
another.

The reason this matters for the GRID lattice: at every
junction in the lattice, energy arriving on one edge must
split among the outgoing edges.  How it splits depends on the
impedance match at the junction.  The junction scattering
rule IS impedance matching — and it produces wave
propagation, not diffusion, from pure geometry.

---

## 4. Electric circuits: the familiar case

If you have any engineering background, you already live
in one of these domains daily: electric circuits.

- **Across:** Voltage (V) — the "push" that drives charge
  through the circuit
- **Through:** Current (I) — the flow of charge
- **Power:** V × I (watts)
- **Impedance:** Z = V / I (ohms)

A resistor with high impedance: large voltage drop, small
current.  A thick copper wire with low impedance: small
voltage drop, large current.

Every rule from §3 applies.  Signals reflect at impedance
mismatches (every RF engineer knows this).  A traveling wave
on a transmission line carries voltage and current in phase
— both peak together — which is how it delivers power
steadily in one direction.  (In a resonant circuit, V and I
are 90° out of phase — energy sloshes between capacitor and
inductor, and no net power is delivered.  Same pattern as
§2: traveling = in phase, standing = 90° out.)

The point is not to teach circuits — it's to recognize that
circuits are one instance of the universal pattern.  Kirchhoff's
laws, Ohm's law, and transmission line theory are not special
properties of electricity.  They are the across/through
framework applied to charge flow in conductors.  The same
mathematics describes pressure pulses in arteries, sound in
a concert hall, and — as we'll see — light in a vacuum.

---

## 5. Electromagnetic waves: E and B

This is where the pattern leads somewhere surprising.

An electromagnetic wave — light, radio, X-rays, all of it —
consists of two oscillating fields traveling together:

- **E (electric field):** the force that pushes on charges.
  It acts *across* the wave — if the wave travels east, E
  points north-south.  E is the across variable: the "push."

- **B (magnetic field):** the circulation that accompanies
  moving charge.  It acts *through* the wave, perpendicular
  to both E and the direction of travel.  B is the through
  variable: the "flow."

Their product — specifically E × H, where H is the magnetic
field intensity closely related to B — gives the **Poynting
vector**: the power flow per unit area carried by the wave.
This is exactly across × through = power, the same pattern
as force × velocity, pressure × flow rate, and voltage ×
current.

The impedance of the medium the wave travels through is
Z = E / H.  For free space (vacuum), this is a measured,
known quantity:

> **Z₀ ≈ 377 ohms** (in SI units)

This number is as real and measurable as the impedance of a
coaxial cable.  In the natural units used by the GRID
framework (where the speed of light c = 1 and ε₀ = μ₀ = 1),
the impedance of free space simplifies to:

> **Z₀ = 1**

The vacuum has unit impedance.  It is the simplest possible
medium — and it is, unambiguously, a medium.  It has a
specific, measured ratio of "across" to "through."  Something
with no medium has no impedance.  The vacuum has impedance.

In a traveling light wave, E and B peak at the same time
and place — they are in phase.  The Poynting vector
(E × H) is always positive, always pointing forward.
Energy flows steadily in the propagation direction, just as
a sound wave carries pressure and air velocity in lockstep,
or a traveling pulse on a rope carries tension and
displacement together.

When light is trapped — reflected between mirrors, or
confined on the compact geometry of a MaSt material
sheet — it becomes a standing wave.  Now E and B are 90°
out of phase: energy oscillates between electric storage
and magnetic storage, back and forth, going nowhere.
That trapped, oscillating energy is what we call a
particle.  Mass is the frequency of that oscillation.

---

## 6. Why the GRID lattice produces Maxwell's equations

Now the payoff.  The GRID framework models spacetime as a
hexagonal lattice — a rigid 2D sheet (in the simplest case)
of hexagonal cells with fixed-length edges, like a honeycomb
or a sheet of graphene.

This lattice has two geometric features that map directly to
the across/through duality:

### Forward paths (the across variable)

Each edge of the lattice connects two nodes.  Energy can
propagate along an edge from one node to the next.  The
**phase gradient** along an edge — how much the internal
phase changes from one node to the next — is the lattice
version of the electric field E.  It is the "push" that
drives energy forward.

### Circulation loops (the through variable)

The edges bound hexagonal faces.  Energy can circulate
*around* a face — a closed loop.  The total phase
accumulated around a loop is the lattice version of the
magnetic field B.  It is the "circulation" that accompanies
the forward push.

### The scattering rule

At each node, three edges meet (it's a hexagonal lattice,
so each node has three connections).  When energy arrives on
one edge, it must distribute among the outgoing edges.  The
rule that governs this distribution is derived from a single
principle: **energy conservation with equal impedance on all
edges.**

This is impedance matching at a junction — exactly the same
physics as a T-splitter in a microwave circuit or a branch
point in a pipe network.  The rule is:

> Each outgoing edge gets the average of all incoming
> amplitudes, minus what that edge contributed.

Nothing about this rule references Maxwell, electromagnetism,
or any field theory.  It is pure geometry: energy arrives,
energy conserves, impedances match.

### What comes out

When you simulate this lattice (as the GRID project has
done), the result is:

- **Directional wave propagation.**  Energy doesn't slosh
  randomly — it travels in coherent wavefronts, at a
  well-defined speed (~0.7 edges per time step on a
  hexagonal lattice).

- **Perfect linear superposition.**  Two crossing waves
  pass through each other with zero distortion (tested to
  machine precision, ~10⁻¹⁵ residual).

- **Both E-like and B-like excitations.**  Forward-path
   amplitudes and circulation-loop amplitudes both appear in
   the propagating wave, in phase — exactly the across/through
   structure of a traveling electromagnetic wave.

These are the defining properties of Maxwell's equations.
The lattice produces them because it is a medium with
across variables (path amplitudes), through variables (loop
circulations), and a well-defined impedance (the scattering
rule at each junction).  Maxwell's equations are not input.
They emerge.

This is the across/through framework's deepest consequence:
**any medium with conjugate variables and impedance will
produce wave equations**.  The specific wave equations depend
on the geometry.  For a hexagonal lattice with the GRID
axioms, the specific equations that emerge are Maxwell's.

---

## 7. The elephant in the room: the aether

Every domain in the table from §2 has a medium.  Sound waves
have air.  Water waves have water.  Waves on a string have
the string.  In every case, the impedance is a property of
the medium, and "no medium" means "no waves."

Electromagnetic waves are the one case where modern physics
says there is no medium.  But the across/through pattern
says: if there is impedance, there is a medium.  Free space
has a measured impedance (Z₀ ≈ 377 Ω in SI units).  So the
pattern implies there IS a medium.  Historically, this medium
was called the **aether**.

### Why the aether was "disproven"

In 1887, Michelson and Morley set up an experiment to detect
Earth's motion through the aether.  The logic was
straightforward: if light travels through a stationary
medium and the Earth moves through that medium, then the
speed of light should be slightly different in the direction
of Earth's motion versus perpendicular to it — the same way
a swimmer's speed relative to shore depends on whether they
swim with or against a river current.

They measured no difference.  The speed of light was the
same in every direction, to very high precision.  This was
taken as proof that the aether does not exist.

### What the experiment actually proved

Michelson-Morley proved that **you cannot detect motion
relative to the medium by measuring the speed of light.**
This is not the same as proving there is no medium.  It
proves that the medium — if it exists — has a specific
property: measurements made inside it cannot detect it.

The experiment assumed that the aether was something you
move THROUGH — like air or water — and that your measuring
instruments (rulers and clocks) are unaffected by that
motion.  Both assumptions turn out to be wrong in GRID:

1. **You don't move through the lattice.**  Particles are
   not objects passing through a medium.  They are wave
   patterns ON the medium — like a ripple on a pond.  The
   ripple doesn't move through the water in the Michelson-
   Morley sense; the ripple IS a configuration of the water.

2. **Your instruments ARE the medium.**  Rulers are bound
   states (standing waves) on the lattice.  Clocks are
   oscillations on the lattice.  When a ruler moves, the
   standing wave Lorentz-contracts — the ruler gets shorter
   by exactly the factor γ (gamma), a number that depends on
   speed.  When a clock moves, its oscillation slows by
   exactly the same factor γ.  The speed of light measured
   by the moving ruler and clock is:

       c_measured = (shorter distance) / (slower time)
                  = (L/γ) / (T/γ) = L/T = c

   The γ factors cancel perfectly.  Not because the universe
   is conspiring, but because the ruler and the light are
   made of the same stuff.  You cannot detect the medium
   because your detector IS the medium.

### Why the old aether experiments asked the wrong question

The Michelson-Morley experiment — and every aether-detection
experiment since — asked: "Can we measure our velocity
relative to the medium?"  The answer is no.  But this is the
wrong question.  The right question is: "Is there a medium?"

Consider an analogy.  Imagine intelligent fish who have never
encountered the surface of the ocean.  They try to detect
"water" by measuring the speed of sound in different
directions, reasoning that if they're swimming through a
medium, sound should be faster in one direction.  They
measure carefully and find: the speed of sound is the same
in every direction.  They conclude: there is no water.

But of course there is water.  The fish are made of water.
Their ears are made of water.  Their rulers (if they had
them) are pressure waves in water.  Every instrument they
build is made of the medium they're trying to detect.  The
medium is undetectable from inside not because it's absent,
but because there is no "outside" reference to compare
against.

The 19th-century aether model imagined matter as something
separate from the aether — solid objects floating in a
luminiferous jelly.  In that picture, you could reasonably
expect to detect your motion through the jelly.  But if
matter is not separate from the medium — if particles are
standing waves on it, rulers are built from those waves,
and clocks tick by those waves — then undetectability is
not a surprise.  It is a geometric certainty.

### The across/through perspective

The across/through framework makes this concrete.  In every
domain, the medium defines the impedance.  You can measure
the impedance from inside the medium — but you cannot detect
your motion through it by measuring wave speed, because your
measuring instruments are also governed by that impedance.

The aether wasn't disproven.  The wrong kind of aether was
disproven — a passive background that things move through
while remaining unaffected.  GRID proposes a different kind:
a medium that everything is made of, whose properties
(impedance, across/through structure) produce the wave
equations we observe, and whose undetectability is not a
mystery but a geometric consequence.

---

## 8. The deep point

The across/through pattern is not an analogy between
unrelated domains.  It is the same mathematical structure
appearing wherever energy flows through a medium.  Circuits,
sound waves, water pipes, and electromagnetic waves all obey
the same conjugate-variable framework because they are all
instances of energy propagation in a medium with impedance.

The GRID lattice is a medium.  It has impedance.  Therefore
it supports waves.  Those waves turn out to be Maxwell's
equations — not because we put Maxwell in, but because any
medium with across and through variables and well-defined
impedance will produce wave equations.

The historical rejection of the aether was the rejection of
a specific (and wrong) model — a passive substance that
things float through.  The across/through pattern points to
a different possibility: a medium that everything is made
FROM, whose conjugate structure produces the physics we
observe, and whose existence has been hiding in plain sight
inside the impedance of free space.

Every time you use a radio, measure a signal on an
oscilloscope, or see a rainbow, you are watching across and
through variables alternate on a medium with 377 ohms of
impedance.  The medium has a name, a geometry, and a set of
rules — and the primer you have just read is the first step
toward understanding it.

---

## References

- GRID hexagonal lattice: [grid/hexagonal.md](../grid/hexagonal.md)
- Wave propagation simulation: [grid/sim-maxwell/](../grid/sim-maxwell/)
- Maxwell derivation from lattice: [grid/maxwell.md](../grid/maxwell.md)
- Natural units and impedance: [natural-units-and-alpha.md](natural-units-and-alpha.md)
- GRID as aether: [grid/INBOX.md §aether](../grid/INBOX.md)
- Lorentz invariance as theorem: [grid/INBOX.md §lorentz](../grid/INBOX.md)
