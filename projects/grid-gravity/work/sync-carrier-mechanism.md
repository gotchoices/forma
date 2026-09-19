# Mechanism 3 — synchronized clocks with a lattice carrier (proposal)

**Status:** Proposal / working hypothesis, **under validation** — plan and
state in [STATUS.md](STATUS.md); steps 1–4 passed.
Unlike mechanisms 1 and 2, this one **extends the substrate** — it adds
degrees of freedom GRID does not currently specify. That is deliberate (the
project is hypothetical by design, and the block on mechanism 2 was a
foundations gap), and every addition is listed in the ledger of §2 so the
mechanism can be compared with others on what it explains per thing it adds.

Grades: **[posit]** (added to the substrate), **[argument]** (follows from the
posits by standard reasoning), **[expectation]** (anticipated, not computed),
**[speculative]**, **[open]**.

**Vocabulary.** Three words are used in fixed senses throughout:

- **Carrier** — the *role*: a lattice degree of freedom that is stored, shared
  between neighbours, never lost locally, and sourced by energy. This is the
  README's own term ("a massless, neutral, propagating carrier"). What
  physically fills the role is left open; candidates are listed in §2 and §8.
- **Local-time field q(x)** — the carrier's value at a place. This is the
  gate's own symbol (every mechanism must produce a local-time field q). Where
  the contrast with its gradient matters it is called the **local-time
  potential**: the clock rate follows q, and the pull on a body follows the
  gradient of q — the same relation as voltage to electric field.
- **Stress, strain** — reserved for one *candidate* carrier (elastic edges) and
  for the spatial deformation of the lattice (§11, item 2). In elasticity these
  are gradient-side quantities, which is exactly why they are not used as the
  name of the role.

---

## 1. The idea in brief

The thesis is the project's own: mass, a standing wave in a compact dimension,
slows local time, and a gradient in the rate of local time is gravity. What is
new is *how the slowing reaches a distance*.

The picture is a field of metronomes standing on a table that is **pliable
rather than rigid**:

- Each node (or edge) of the lattice has its own clock. There is **no master
  clock**. Neighbours trigger and pull on each other, and so fall into step —
  the way metronomes on a shared surface synchronize.
- The lattice members can also **hold a stored quantity** in addition to their
  scattering function. The lattice so equipped is the "table"; the stored
  quantity is the carrier.
- A node carrying a standing wave (a mass) is **loaded**. The load biases its
  rate. The loaded node pulls against its neighbours; the neighbours, coupled
  through the table, are pulled in turn; the disturbance spreads outward at a
  finite speed.
- Remove the load and the region relaxes back.

Simplified setting: one extended dimension x, one compact dimension c, and
time — the same mass-only frame the rest of the project uses
([simplified-model-and-mast.md](simplified-model-and-mast.md)).

## 2. Substrate ledger — what this mechanism adds to GRID [posit]

| # | Addition | What it buys |
|---|---|---|
| P1 | **Neighbour-triggered clocks.** A node fires on its neighbours' activity; no master clock. | A shared tick without a scheduler. Answers "what triggers a node to act?" ([local-time.md](local-time.md)). |
| P2 | **A carrier.** Each lattice member stores a variable q, exchanged with neighbours, never lost locally. *Refined by step 4:* the scatter's registers carry the carrier's rate of change and its gradient; the potential q itself is the **running sum of the node value**, held at each node. | A second stored quantity — what turns a spreading disturbance into a propagating wave (§3). The carrier the project lacked. |
| P3 | ~~**Load biases the local rate**, in proportion to the energy of the resident standing wave, always with the same sign.~~ | *Retired as a posit:* derived from the action — if the rate depends on the carrier, the wave must source the carrier, ∝ energy, with one sign ([action-and-gamma.md](action-and-gamma.md) §4). |
| P4 | **A dead band, not a set-point.** Within a range, a node has no preferred rate of its own; only differences from neighbours matter. | Masslessness → unlimited range (§6). |
| P5 | **The local rate follows q, not the gradient of q** (the potential, not the pull). | The right power law: a 1/r potential rather than 1/r² (§5). |
| P6 | **Every member stores.** Nodes carry a storage register (returning its share with the same sign); extended edges carry one too (returning it inverted); the carrier loads both equally. | The full light bending, γ = 1. The equality is the impedance-matched, reflectionless loading — not a tuned number ([action-and-gamma.md](action-and-gamma.md) §2). |
| P7 | **The compact loop is loaded once.** A clock's compact circulation closes through a node and is not loaded by the storage on space edges. | Makes clocks slow half as much (in the logarithm) as light — the other half of γ = 1. |

**Candidate realizations of the carrier (P2).** The mechanism needs the role
filled, not any particular filler:

- *elastic edges* — q is an edge deformation and the edges resist differences
  in it (the "stressed table" of the metaphor);
- *a local stretch of the compact circumference R_ℵ* (§8);
- *a rate or phase variable of the clocks themselves*, if one can be found
  that survives §4's objection (locked clocks share one rate);
- *mechanism 1's backlog* ([congestion-falloff.md](congestion-falloff.md)),
  revisited with the active, lossless sourcing it lacked.

Inherited unchanged from the project: mass as a compact standing wave; clock =
confined light (Commitment 3 of [local-time.md](local-time.md)); coordinate
time is gauge, proper time is local (Commitment 4).

## 3. Why two stored quantities: diffusion versus a wave [argument]

If neighbouring clocks merely pull each other's rates together, a disturbance
*diffuses*: it spreads as √t, with no definite speed. Gravity's influence
travels at a definite speed.

A wave needs two stored quantities that trade back and forth — in electrical
terms the inductance and capacitance of a ladder line, in mechanical terms
mass and spring. The node rate is one; the **carrier (P2) is the other**. With
both, a disturbance propagates at a definite speed c_s set by the ratio of the
carrier's stiffness to the inertia of the rate variable. With ρ the load,

<!-- ∂²q/∂t² = c_s² ∇²q − ρ -->
$$
\frac{\partial^2 q}{\partial t^2} \;=\; c_s^2\,\nabla^2 q \;-\; \rho .
$$

Whether c_s equals the speed of light is *not* automatic — see §11.

## 4. What synchronization does, and what it cannot do [argument]

A loaded node fighting its neighbours is an injection-locking problem, and it
has three possible outcomes:

1. **Lock.** The bias is within the lock range. The loaded node is entrained;
   *every node runs at the same rate*. The bias survives only as a static
   pattern of phase lag (inner nodes fire slightly late) and as a static
   disturbance held in the table around the load.
2. **Slip.** The bias exceeds the lock range. The loaded node free-runs.
   Neighbours then feel an alternating, beat-frequency disturbance, which in a
   coupled medium dies off exponentially with distance. The effect stays local.
3. **Graded rates.** Rates stay persistently different and shade off smoothly
   with distance. **This is what gravitational time dilation requires** — a
   clock near a mass runs slow *forever* relative to a distant one.

Phase-locking cannot produce outcome 3, because locking means equal rates. More
generally, any network in which each firing waits on its neighbours settles to
**one common tick rate**. And the static lag pattern of outcome 1, although it
falls off as 1/r, is only a relabelling of simultaneity: an inward hop takes
slightly longer, an outward hop slightly shorter, and every round trip is
unchanged. Nothing falls.

So the roles divide:

- **Synchronization supplies the common coordinate tick** — a global time
  label with no master clock. This is Commitment 4 of
  [local-time.md](local-time.md) obtained from the substrate rather than
  assumed, and it repairs that note's objection that asynchronous firing is
  ill-posed.
- **The dilation must come from the carrier** — from q setting how far a wave
  advances per tick at each place, the way a pendulum's rate depends on where
  it stands, not on what its neighbours are doing.

## 5. The carrier holds a 1/r potential [argument, given P2 and P5]

A point load on a medium that resists *differences* between neighbours leaves a
static pattern. Let q_i be the carrier's value at node i, and let each edge
resist a difference in q between its ends with stiffness κ. In equilibrium the
pulls on each node balance the load ρ_i on it:

<!-- κ Σ_j (q_j − q_i) = ρ_i   →   κ ∇²q = ρ   →   q(r) = −M / (4π κ r) -->
$$
\kappa \sum_{j \in \mathrm{nbrs}(i)} (q_j - q_i) \;=\; \rho_i
\quad\longrightarrow\quad
\kappa\,\nabla^2 q = \rho
\quad\longrightarrow\quad
q(r) = -\frac{M}{4\pi\kappa\, r}\ \ \text{(3D)} .
$$

The mechanical picture is a spring lattice with a point force on it: the
displacement persists and falls as 1/r.

**A trap.** The *gradient* of q — what an elastic picture would call the strain
or stress — falls as 1/r². If waves were slowed in proportion to that gradient,
the potential would be 1/r² and the force 1/r³: the wrong law. The rate must
follow q itself (P5). Because only differences in q are observable (a uniform
shift of q rescales every clock together and cannot be detected), this is
consistent with the symmetry that keeps the carrier massless (§6).

## 6. Conditions for unlimited range [argument]

**No preferred rate (P4).** Suppose each node also pulled back toward a value
of its own with strength γ. The equilibrium equation gains an on-site term,

<!-- (−∇² + γ/κ) q = −ρ/κ   →   q ∝ e^(−r/ξ) / r,   ξ = a·√(κ/γ) -->
$$
\Bigl(-\nabla^2 + \frac{\gamma}{\kappa}\Bigr) q = -\frac{\rho}{\kappa}
\quad\longrightarrow\quad
q \;\propto\; \frac{e^{-r/\xi}}{r},
\qquad \xi = a\sqrt{\kappa/\gamma}
$$

(a = lattice spacing). That is a short-range Yukawa field. Gravity shows no
cutoff out to roughly 10⁶¹ Planck lengths, which would require
γ/κ ≲ 10⁻¹²² — effectively zero. A natural rate is harmless as a *unit* (the
unloaded rate); it is fatal as a *restoring pull* on the quantity that carries
the far field. The surviving form is a **dead band**: inside a range the node
is indifferent, which is exactly massless; the band edges matter only in the
saturated core next to the mass.

**No local leak.** "Remove the load and the region relaxes" must mean the
stored disturbance **radiates away as a wave**. If a node can quietly bleed its
share off on the spot, that leak is a loss channel, and the project's linchpin
applies: loss ⟺ shunt ⟺ Yukawa ([shunt-check.md](shunt-check.md)).

## 7. The falloff is geometric [argument]

The 1/r does not come from neighbours tolerating only a small skew. It comes
from conservation: the total flux of the carrier's gradient through any closed
shell around the mass is fixed, and it is shared over a shell area that grows
as 4πr². A limit on skew per edge shapes only the core — and the project
already found that core saturation does not screen the far field
([falloff-sim-result.md](falloff-sim-result.md)).

## 8. A candidate carrier: the compact circumference [speculative]

[range-from-foundations.md](range-from-foundations.md) states what would
revive the mechanical route: the ℵ-line size R_ℵ must become "a dynamical,
spatially-varying, massless degree of freedom sourced by energy." The carrier
of P2 could be exactly that — q as a local stretch of the compact
circumference:

- **Sourcing.** A standing wave presses on the cavity that holds it. That
  radiation pressure is proportional to the wave's energy and always has the
  same sign. This would turn P3 from a posit into a mechanism.
- **Clock rates.** The Kaluza–Klein mass is m_n = nℏ/(R_ℵ c). A larger R_ℵ
  lowers every such frequency, so every massive clock nearby runs slower — the
  right sign, and universal for matter.
- **Falloff.** Neighbouring edges share the stretch elastically → 1/r (§5).

Not covered by this candidate: light's own index (R_ℵ does not obviously slow a
photon), and hence the light-bending factor (§11).

*After step 3:* this candidate is disfavoured as the carrier's whole effect. A
stretch of R_ℵ alone slows clocks but not light — no light bending at all — and
the sourcing it was meant to explain now follows from the action without it
([action-and-gamma.md](action-and-gamma.md) §5).

## 9. Against the gate (anticipated, not yet tested)

| Condition | Anticipated outcome | Note |
|---|---|---|
| (0) Vacuum field | passes | The carrier itself holds the field; nothing else need be present. |
| (1) Massless 1/r, isotropic | passes **by construction** | P2 + P4 put a Laplacian in by hand, so the 1/r is a property of the posit, not evidence for it. Isotropy of a massless field on the hexagonal lattice was already shown ([falloff-sim-result.md](falloff-sim-result.md), [loops-and-range.md](loops-and-range.md)). |
| (2) Non-dispersive | **shown** ([uniform-q-theorem.md](uniform-q-theorem.md)) | If what is rescaled is the rate at which *every* wave advances, all frequencies slow identically. Mechanism 2 managed this only for ω ≪ ω₀, with clocks at the Compton frequency sitting on its resonance. |
| (3) Coupling ∝ mass-energy | posited (P3) | Becomes a derived property if §8 holds. |

Because condition (1) is built in, the informative tests are elsewhere: §11.

## 10. Strong field: a horizon as a slipped region [speculative]

A horizon is where the local rate goes to zero relative to distant clocks. In
this mechanism that is a region driven past the edge of the dead band: it
loses lock with the surrounding lattice.

- **The exterior field must survive** — a black hole still gravitates. It
  does: the flux outside is conserved, so the exterior knows only the total
  mass M. The region is slipped inside but still attached through its boundary
  flux.
- **A scaling test.** If slip is triggered when the *gradient* of q (∝ M/r²)
  reaches a limit, the horizon radius grows as √M — wrong. If it is triggered
  when q itself (∝ M/r) reaches its floor, the radius grows as M — right. So
  the horizon must be set by the same quantity that sets the time dilation
  (P5), which is a consistency check on the mechanism.
- **Area law.** The edges that have lost lock lie on a surface, so their
  number grows with its area — the form of axiom A5 (S = ζ·A), and a possible
  bridge to the statistical route ([entropic-route.md](entropic-route.md) §5).
- **Open:** a slipped region is cut off in both directions, while a horizon is
  one-way (things still fall in); spin and charge on the boundary.

## 11. Open hurdles

1. **The wave speed must equal c exactly.** Gravitational and light signals
   from the same event arrive together to about one part in 10¹⁵. Here c_s is
   set by stiffness over inertia (§3); it has to come out of the same scatter
   that carries light, not be tuned to match. *Resolved in principle:* a
   carrier that is an amplitude moved by the same scatter has the identical
   spectrum, loaded or not ([uniform-q-theorem.md](uniform-q-theorem.md) §5).
2. **The factor of 2 in light bending.** A rate-only effect bends light half as
   much as observed (the 1911 value). The other half is spatial: a physical
   contraction of edges under load — a genuine lattice *strain*, the "pinch",
   knob B of
   [grid-matter/work/responsive-medium.md](../../grid-matter/work/responsive-medium.md).
   The two parts must come out equal, not be set equal. *Resolved at first
   order:* the spatial half is storage on extended edges, and "equal" is the
   impedance-matching condition ([action-and-gamma.md](action-and-gamma.md)).
3. **Why load slows the rate, ∝ energy.** *Resolved:* it follows from the
   action ([action-and-gamma.md](action-and-gamma.md) §4).
4. **One gravity, not two.** GRID already obtains the Einstein equations by
   Jacobson's argument ([grid/gravity.md](../../../grid/gravity.md)). This
   mechanism must be the microscopic realization of that result — ideally
   supplying the entropy law it assumes — not an additional scalar force
   beside it.
5. **Reconcile with the synchronous lattice** (README ground rule 5): show
   that neighbour-triggered clocks reproduce the confirmed Maxwell results.

## 12. Charge cannot ride the tick — a signed offset instead [argument + open]

A tick-rate field moves *everything*, neutral matter included. The
electromagnetic force does not. So charge cannot act by slowing or speeding
the local clock.

There is, however, a precise sense in which both forces are "effects on time".
A wave whose local frequency ω depends on position is steered according to

<!-- dk/dt = −∂ω/∂x -->
$$
\frac{d\mathbf{k}}{dt} \;=\; -\,\nabla \omega ,
$$

the ray equation: a wave packet drifts toward the region where its frequency
is lower. The two forces differ in the *kind* of frequency shift:

| | Gravity | Electromagnetism |
|---|---|---|
| Shift | **fractional**: δω ∝ ω | **additive**: δω = ±(charge × electric potential)/ℏ |
| Seen by | every wave | only modes carrying a compact winding (charge) |
| Sign | always the same (source is energy, even in amplitude) | set by the winding's handedness (odd) |
| GRID home | this project's local-time field q | the A4 link phases; the sign-flipping Wilson-loop shift of [grid-primitive ch. 9](../../grid-primitive/09-chirality-asymmetry.md) |

**Shielding follows for free:** signed offsets can cancel (a neutral body
presents no net offset), fractional pulls cannot. This is the even/odd split
already noted in [aleph-grounding.md](aleph-grounding.md) and
[qa/Q33](../../../qa/Q33-gravity-vs-charge.md). It also points at
[metric-charge](../../metric-charge/)'s untouched time–compact shears (σ_tu,
σ_tw) as the continuum counterpart. Whether the lattice has a signed,
winding-selective carrier alongside its universal one is **open** — this is
the project's EM stretch slot, developed further in [em-slot.md](em-slot.md)
(charge as a time *shear*; why a signed *rate* would make likes attract; a test
ladder).

## 13. Validation plan

The ordered plan, with pass / fail criteria and the state of each step, is kept
in [STATUS.md](STATUS.md). In outline: (1) a concrete rule and the uniform-q
theorem; (2) a drop test as its cross-check; (3) a lattice action and the
light-bending parameter; (4) switch-on of a source in 3D; (5) the strong field.
What is *not* on the list is anything the posits deliver by construction — the
static 1/r, its isotropy, the Yukawa failure modes — and the question of
whether clocks that trigger each other can hold graded rates: a network in
which each firing waits on its neighbours has a single cycle time (a standard
result for timed event networks), so they cannot (§4).

**Step 1 is done** ([uniform-q-theorem.md](uniform-q-theorem.md)). The rule:
each node gets one *storage register* of weight Y whose share returns to the
same node a tick later — a lossless "detour". With the carrier setting Y, a
uniform Y maps every mode's frequency through one universal relation,
sin(ω_Y/2) = sin(ω_0/2)/√(1 + Y/N): light speed, rest frequency and inertia
slow together, with 1 − q = 1/√(1 + Y/N). The same calculation shows that
returning the share *inverted* gives the photon a mass, and that a carrier
riding the same scatter travels at exactly light's speed. It also fixes the
target for step 3: this rule alone gives half the observed light bending.

**Step 2 is done** ([drop-test-result.md](drop-test-result.md)). With a static
gradient of Y imposed, packets of different mass fall together toward the
slower region at a = −c·dc/dx, light is delayed rather than reflected, and
moving packets follow the ray equations of the local spectrum to 0.02%. The
profile was imposed by hand; that a mass *produces* it is step 3.

**Step 3 is done, at first order** ([action-and-gamma.md](action-and-gamma.md)).
One action for wave and carrier gives the source — ∝ energy, one sign, always
attractive, light counting double — with no separate posit. Loading nodes and
extended edges *equally* gives the full light bending, γ = 1, and that equality
is exactly the condition that the lattice's impedance match is undisturbed (a
matched step barely reflects). Cost: posits P6 and P7 above. Flags: a purely
standing wave is a breathing source; β awaits the nonlinear completion.

**Step 4 is done** ([switch-on-result.md](switch-on-result.md)). Run forward from
nothing, a steady source on the 3D scatter builds q = 6s/(4πr) behind a front
moving at exactly the lattice light speed — predicted amplitude to four figures,
isotropic, no drift — and the potential leaves as a wave when the source is
removed. Steps 1–4 tested the pieces with the loop open; closing it is step 5.

## Grades summary

- **[posit]** P1–P5 (§2).
- **[argument]** Wave vs diffusion (§3); synchronization equalizes rates, lag
  pattern is gauge (§4); the 1/r potential and the potential-vs-gradient trap
  (§5); on-site pull → Yukawa, leak → Yukawa (§6); geometric falloff (§7);
  tick universality excludes charge, ray-equation reading (§12).
- **[speculative]** R_ℵ as the carrier, with radiation-pressure sourcing (§8);
  horizon as slipped region (§10).
- **[open]** Which realization fills the carrier role; c_s = c; factor of 2;
  derivation of P3; identity with the Jacobson result; Maxwell reconciliation;
  a signed carrier for charge.
