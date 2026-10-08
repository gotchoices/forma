# grid-scattering

**What sets the rate at which energy crosses between GRID's compact sectors — and into space?**

**Type:** Exploratory project (see [../README.md](../README.md))

**Status: parked, with one result and one refutation.** The mechanism's
nonlinear channel does have a ceiling and does carry energy across it, but the
frequency selection the project was built around is **refuted** — it was an
artifact of the simulation box (§4). Motion is **not** this project's result:
the ordinary pooled scatter supplies it exactly, and the project's own channel
destroys it above a threshold. Checklist: [work/STATUS.md](work/STATUS.md).
All numbers with provenance: [work/measurements.md](work/measurements.md).

**Scope.** The point is to test one mechanism: **saturation and overflow as the
means by which energy crosses a sheet boundary.** The project is not required to
stay harmonious with earlier forma work — where it departs, it says so and the
departure is part of what is tested. Supporting material:
[Appendix.md](Appendix.md).

---

## 1. The question

Energy demonstrably moves between forma's domains. Two gamma rays make an
electron–positron pair; a neutron becomes a proton, an electron and an
antineutrino; a charged particle radiates into space. The rates differ by many
orders of magnitude and the framework does not say why.

forma has the gap written down twice.
[ma-domain leakage-rate.md](../ma-domain/work/leakage-rate.md) files a caveat
against its own working assumption — coupling without a shared dimension
*"demonstrably exists"*, so *"the leakage graph is richer than the
metric-sharing graph"* — and
[threshold-dynamics.md](../ma-domain/work/threshold-dynamics.md) sits parked on
its §6.2: by what physical mechanism does energy reorganise from a background
band into a discrete mode? This project proposes a node-level answer and tests
it.

## 2. The posit

A node where space meets a compact direction carries four registers — two
space, two compact. The only genuine per-node constraint is **unitarity**:
energy in equals energy out. Momentum need not balance at a node, because the
lattice is fixed and absorbs it; that is what crystal momentum means.

Being discrete and finite forces a **bound**: a register holds only so much. It
does not force the excess to **redirect** into the other group rather than being
clipped away or wrapped. That redirection is the posit:

> **Below the ceiling, the overflow channel is shut. Above it, overflow carries
> energy across in bulk, between a node's space group and its sheet group.**

The partition is **space against a sheet**, not dimension against dimension, so
within space the ordinary scatter applies unchanged and Maxwell is untouched.

**The posit is about the nonlinear channel only.** An earlier version also
claimed that keeping space and a sheet from exchanging *below* the ceiling was a
distinguishing choice. It is not a choice at all: on a translation-invariant
lattice the compact wavenumber is a Bloch label, so no linear rule mixes wound
and unwound content — the pooled scatter included. Measured as exactly zero at
every drive amplitude ([§M2](work/measurements.md)). That half of the posit is
**withdrawn**, and with it the reason the project built bespoke junction rules
at all. Working file: [work/junction-geometry.md](work/junction-geometry.md).

**The ceiling is not a free parameter.** Any ordinary travelling photon is by
definition below it — otherwise light would saturate as it propagates and the
vacuum would not be transparent. So the ceiling is calibrated by an observable:
*light must pass*. Three things follow with no further assumption. A lone photon
never saturates, which is why pair production needs **two** photons, or a photon
plus a nucleus's field standing in for the second. A collision is special
precisely because two amplitudes sum at one node. And the **Schwinger limit
becomes a prediction** rather than an input — it is where a single field, with
no collision, finally reaches the ceiling alone.

## 3. The arena, and what crosses

A **cylinder**: one extended direction x and one compact direction c as a
product lattice, so every node sits on both the x line and the c ring through
it, and rings at neighbouring x are joined along x. That last point is what lets
anything made on a ring afterwards move.

*(An earlier arena hung a ring off each x position at a single point. That was
wrong twice: it gave every ring a privileged attachment, breaking the
translation symmetry along c whose conserved quantity is the winding; and its
ring nodes had no x-edges, so nothing made there could ever travel.)*

**What the overflow does.** Where a group's total exceeds the ceiling, the
excess rotates out of the saturating group into the other, at the node where it
happens, and runs both ways around the ring to meet itself on the far side. The
rotation is exactly orthogonal, so the crossing conserves energy to machine
precision and accounts for whatever the ring already holds. Both directions run:
space → sheet makes a particle, sheet → space returns it.

**What forms.** Two counter-propagating waves on the ring. Equal energy both
ways around a loop is a standing wave, and a standing wave captive on a loop is
what [metric-mass](../metric-mass/) commits to as a particle at rest — the ±n
superposition, one particle rather than two.

**It needs a seed, and the rule never supplies one.** A photon is uniform
around c, the overflow rule is itself symmetric around c, and a symmetric state
under a symmetric rule stays symmetric *exactly* — over a million overflow
events produce precisely zero winding with the background switched off
([§M4](work/measurements.md)). The symmetry must be broken by the **state**,
never by the rule, which is what keeps winding a conserved label — and winding
is charge once the field is complex. What this does not say is how big the real
seed is; the arena has no quantum, so the background's magnitude in these units
is arbitrary (§5).

## 4. What has been measured

On the cylinder, with an exactly energy-conserving overflow rule (drift
10⁻¹⁶). Full provenance and command lines:
[work/measurements.md](work/measurements.md).

**Established.**

- **The ceiling gates the channel.** At `sat = 0.8` nothing fires below drive
  amplitude 0.55; the channel switches on at 0.60 and winding leaves the
  background floor just above it.
- **The channel is the only way across.** With the ceiling off, winding is
  *exactly* zero at every amplitude tested, to more than ten times the threshold.
- **The crossing needs a symmetry-breaking seed**, and the rule cannot provide
  it. Exact, by equivariance.
- **The reverse channel runs unprompted**, which is what lets a ring shed
  energy.

**Refuted — frequency selection.** The project was built on the claim that the
drive must resonate with the ring, which would give each sheet its own threshold
set by its own circumference, landing it at the particle's own mass scale
automatically. A frequency sweep with proper error bars shows strong structure
but **not at the ring's mass tower** — the tower's n = 3 frequency is the
sweep's minimum. Moving one variable at a time settles it: changing the ring
from 24 to 36 nodes shifts every tower frequency by a third and leaves the sweep
*unchanged within error bars*, while changing the box from 201 to 301 nodes
leaves the tower alone and moves everything. **The structure belongs to the
x-box, not the ring.** Earlier figures of ~5×, 12–58% and 50–100× are all
withdrawn, along with the inference that an intense optical laser makes no pairs
because it misses the electron ring's resonance. Nothing here rules resonance
out as physics; it rules out this arena as evidence for it.

**Not the project's result — motion.** A wound mode moves correctly, with
Kaluza–Klein dispersion to 0.1% in exact analysis and 2.6% for a travelling
packet, even in k_x exactly, and with group velocity exactly zero at rest. But
that is the **ordinary pooled scatter**, which is also node-local and
reciprocal; [grid-matter ch. 4](../grid-matter/04-matter-waves-and-de-broglie.md)
measures the same thing. Three bespoke couplings were built before the pooled
rule was tried, and all three are withdrawn — the last of them, a gradient
coupling, was reported as resolving motion on the strength of samples taken only
at positive k_x below 0.10; over the full range its band is lopsided and a mode
at rest drifts at +0.107 ([§M7](work/measurements.md)).

**What the project's own channel contributes to motion is negative.** Above a
threshold the overflow **pins** a moving packet: by drive amplitude 1.2 it does
not translate at all, with energy still exactly conserved. There is a narrow
window — amplitude ≈ 0.8 — where the channel is live and motion is untouched,
and a reciprocal variant of the rule has not been tried.

## 5. What this arena cannot settle

Named here rather than discovered later.

- **Amplitude against frequency per quantum.** The ceiling must sit *below* two
  colliding 511 keV gammas and *above* a bright optical beam — and what
  separates them cannot be photon count, since the beam has vastly more. It has
  to be frequency. The bridge is that a single quantum ℏω localised in about one
  wavelength carries energy density ∝ ω⁴, hence amplitude ∝ ω²: a gamma then has
  ~10¹¹ times an optical photon's amplitude *per quantum*. Self-consistent, and
  it is what makes the calibration in §2 possible — but it imports ℏ into a
  classical arena. That is [grid-quantization](../grid-quantization/)'s
  territory, and by forma's principle-versus-scale rule ℏ enters as a unit
  rather than as something derived here.
- **The seed has no size.** Without a quantum there is no mapping from amplitude
  to ½ℏω, so the background's magnitude in simulation units is arbitrary. §4's
  seed result is a statement that one is *needed*.
- **Equipartition.** A classical nonlinear lattice relaxes toward equal energy
  per degree of freedom, which here would mean roughly half of all light
  becoming ring content — and the hard-driven runs do thermalise to about that.
  The state-density ordering that would prevent it ([Appendix.md](Appendix.md),
  P6) is a *quantum* counting argument and needs the quantum above. So the
  two-way-traffic equilibrium cannot be interpreted yet.
- **Nothing protects a particle.** A single real-valued ring has no conserved
  quantity shielding a mode, so any lifetime measured here is that of an
  unprotected neutral excitation — closer to a π⁰ than a neutron.
- **Carried over and still unanswered:** at 2× and 3× the threshold frequency
  the ring takes an n = 2 or 3 *rest* mode rather than a moving pair; two
  threshold photons make one ±n object where Bethe–Heitler needs a single photon
  of 2mₑc²; a resonance condition would use lab-frame frequencies rather than
  the invariant √(ω₁ω₂); and the Schwinger "prediction" is fixed by dimensional
  analysis up to a convention factor of about 16, so it is weaker than claimed.
- **Is the arena below the minimum?** A group is meant to be a *sheet*, meaning
  a plane. The 1D × 1D reduction makes each group a single line — deliberate,
  and fine for the crossing question, but a 2D compact sheet is needed before
  anything about sheet-internal structure can be said.

## 6. Objectives, and where each stands

1. **Make a particle, then get it back.** Creation is done; the return channel
   is seen but not characterised. **Partly met.**
2. **Make it move.** A wound mode moves, but by the pooled scatter, not by this
   project's mechanism — and the mechanism destroys the motion above a
   threshold. **Not met on the project's own terms.**
3. **Find out how fast it builds.** Whether repeated overflow accumulates, and
   how that depends on drive strength and ring size. A rate, not a final amount.
   **Not started.**
4. **Long-range: reach the observed rates.** Sargent's Q⁵ law, lepton
   universality and the neutron's 880 s lifetime are what
   [leakage-rate.md](../ma-domain/work/leakage-rate.md) already recovers from
   phase space. **Not reachable from this arena** — one ring, no lepton or
   hadron sheets, no neutrino line, no quanta — and no correspondence is stated
   between a classical overflow rate and "matrix element × phase space".

**Success** would be objective 2 end to end: a bound object that moves, with
inertia, under the full rule. The linear sector delivers the inertia for free;
the nonlinear sector currently subtracts from it.

**Deferred, and listed so the narrowing is visible.** The originating notes also
set out the energy ladder and the durability of ordinary matter, neutron decay,
simultaneous creation of an electron and a neutrino, and the stability ordering
across particle classes. None has an objective here: they need sheets this arena
does not have, and in most cases the quantum of §5.

## 7. Revival conditions

Parked rather than closed. Worth restarting on any of these:

1. **A reciprocal overflow rule.** The current rotation pairs `+x` with `+c` and
   `−x` with `−c`, which is what broke the superseded gradient coupling.
   Coupling each compact register to *both* x registers is a one-line change and
   is the most likely cause of the pinning in §4. Cheapest open experiment.
2. **A geometry whose box modes are out of range of its ring modes.** That is
   what would make a frequency test mean anything, given §4.
3. **A binding nonlinearity on the field value.** grid-matter's compact-phase
   potential already produces a mobile particle on this lattice; combining it
   with saturation as the transfer channel is the obvious experiment, and may
   belong in grid-matter rather than here.
4. **A reason the ceiling is not global.** A per-sheet or per-group ceiling
   would change what the calibration in §2 implies, and would need its own
   justification.

## 8. Relation to other projects

**Not a revival of grid-saturation.** grid-matter was renamed from
`grid-saturation` because its entry hypothesis — that the saturation bound
*binds a particle* — was refuted. This project concerns **transfer**, not
binding, and grid-matter's own work file keeps that distinction open: *"This is
'not yet,' not 'refuted.'"*

- [ma-domain](../ma-domain/) — the principal consumer:
  [leakage-rate.md](../ma-domain/work/leakage-rate.md) names the missing law,
  [threshold-dynamics.md §6.2](../ma-domain/work/threshold-dynamics.md) the
  missing mechanism.
- [grid-matter](../grid-matter/) — the saturation history, the (x, c) cylinder
  testbed, and **the binding half this project lacks**: its compact-phase
  potential produces a stable, mobile breather on this lattice. Its pooled
  scatter is the rule this project ended up adopting for its linear sector.
- [metric-mass](../metric-mass/) — the target object: a particle is a standing
  wave around the compact dimension, the ±n superposition.
- [grid-duality](../grid-duality/) — closed; the scatter, the candidate-model
  format and the test bench any new rule must pass.
- [grid-primitive](../grid-primitive/),
  [grid-quantization](../grid-quantization/) — the edge/node primitive, and the
  home for any zero-point question that survives.
