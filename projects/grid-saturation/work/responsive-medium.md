# The responsive medium — mass and gravity from edges that react to load

**Status:** active direction (opened after the phase-winding flat-band result).
This is the design/intent record for the "edges react to their load" program, so
the reasoning is not lost between sims. Tests live in
[`../scripts/responsive_medium.py`](../scripts/responsive_medium.py); the gate is
[binding-evaluation.md](binding-evaluation.md).

## The core move

Everything tried before acted on the **value** carried by an edge (clip,
spillover, quantize) or assumed a **fixed** geometry. Here the substrate itself
**responds** to what it carries: an edge changes its properties under load. This
is the Wheeler loop rendered at the node/edge level —

> traffic tells the edge how to curve; the curved edge tells the traffic how to move

— i.e. the **metric becomes dynamical**, sourced by the field. It is the natural
GRID-native way to get a metric at all: the metric *is* the state of the lattice.

## Two knobs = the two halves of the GR metric

Weak-field metric: **ds² = −(1 + 2Φ/c²)c²dt² + (1 − 2Φ/c²)(dx²+dy²+dz²)**.

- **Knob A — speed / propagation delay** ↔ the **time** part **g₀₀**. A loaded
  edge propagates slower = a slowed clock = a higher optical index. **Local.**
  Delivers: Newtonian gravity, Shapiro delay, *half* of light-bending, and — the
  point for us — **containment**: the particle sits in the time-well it digs
  itself, and because the field digs it, the well **co-moves** (a mobile,
  self-bound soliton — the very thing the flat-band winding could not be).
- **Knob B — physical contraction** ↔ the **space** part **gᵢⱼ**. Distances get
  denser near the load — a "pinch." **Cannot be local:** shortening one edge
  forces neighbours to take up the slack, so the deformation **propagates as
  elastic strain**. The static elastic Green's function in 3D is **1/r** — the
  same 1/r as the Newtonian potential. This is the long-range carrier.

Knob A is an optical index (no propagation, no tail). Knob B is a genuine metric
strain (elastically coupled, 1/r tail). **Containment wants A; gravity needs B.**

## Why this is a real grid-gravity revival route

[grid-gravity](../../grid-gravity/) parked on: "a 1/r field needs a massless,
neutral, propagating carrier, and GRID's fixed spectrum has none," and named the
revival condition as *"a substrate-level result making the ℵ-line size a massless
field."* Knob B, applied to the **compact dimension**, makes the ℵ-line
circumference a **dynamical field sourced by mass and propagating elastically** —
*exactly* that condition. The missing carrier is the **lattice's own strain
field**, available only once the lattice is allowed to deform.

This is the **"world crystal"** picture (spacetime as an elastic crystal,
curvature as strain/defects; Kleinert and others). We reach it from GRID's
foundations rather than importing it — convergence, a good sign.

## Honest ledger (do not oversell)

- **New degree of freedom.** The lattice goes from fixed scaffold to **dynamical
  elastic medium**; field and lattice back-react (a coupled, nonlinear, GR-like
  system). Natural, but it is new machinery — count it.
- **The tensor bar.** Scalar contraction gives 1/r (Newton) and *a* bending term,
  but full GR is tensorial. Expect **Newton + partial GR**; matching the exact
  light-bending factor of 2 and the rest is a separate, higher bar. **Claim
  Newton first; do not pre-promise Einstein.**
- **Sign of the well.** Whether a pinch traps or expels depends on which
  dimension deforms and the sign — e.g. pinching *c* raises a winding's KK energy
  (∝ 1/R) and would push the throat *open* (wrong way). Containment likely wants
  the **x-dimple (knob A / g₀₀)**; contraction is reserved for the long-range
  tail. This sign work is real, not automatic.
- **Runaway → but discreteness saves it.** A well that deepens with load could
  collapse; but an edge **cannot contract below one node spacing** → a built-in
  minimum length, a natural Planck cutoff, **no singularity**. A feature.
- **Self-consistency.** The coupled field+lattice system must be evolved
  stably and conservatively.

## The payoff (why it is worth the new DOF)

One substrate property — *edges react to load, in two modes* — yields **both**
**containment** (A: local, self-dug, co-moving time-well → the mobile particle)
**and** **gravity** (B: elastic strain, 1/r, long-range). Mass and gravity from
the *same* reaction. That parsimony is the prize.

## Staging and tests

1. **Knob A — self-binding + mobility (do first, cheap, decisive).** Load-
   dependent propagation delay only. Does an x-wavepacket **stop dispersing**
   (self-bind) while **still moving** (kick it — does the well follow)? This
   directly kills-or-cures the flat-band failure. Sign/strength swept; watch for
   collapse vs. a stable soliton window.
   - *Confirm:* a localized packet that persists AND translates at ~constant
     speed without spreading. *Refute:* it disperses regardless, or only binds
     when pinned (immobile), or collapses/blows up with no stable window.
2. **Add knob B — the 1/r tail (later, only if A binds).** Edges physically
   contract; neighbours relax elastically. Test for a **1/r strain tail**, that a
   **second particle feels it** (attraction = gravity), and whether the compact
   pinch sharpens containment.
3. **Combine with III (winding) and I (instantiation)** for the full gate:
   winding = charge (protected), knob-A well = mass/containment (mobile),
   instantiation = whole-quantum click.

## Results

### Knob A (index/phase) — slows but does NOT self-bind (thorough negative)

[`../scripts/responsive_medium.py`](../scripts/responsive_medium.py), `packet`
scenario (a moving n=0 wavepacket; linear baseline disperses ~3× while mobile).
Knob A implemented as an intensity-dependent phase (index), exactly conserving.

- **The delay is real:** with knob A on, the packet's speed drops (0.32 → ~0.15
  nodes/tick) — a loaded region does propagate slower, as intended.
- **But no self-binding, anywhere.** Scanned gA = ±0.003 … ±2, amplitude 0.5–4,
  width 10–16, carrier ω = 0.3–2.1 (to catch any anomalous-dispersion window).
  Width growth stayed **3–4× at every setting** — the packet always disperses.
  A *uniform slowing* is not a *trapping well*; the refraction never becomes
  strong enough (or the right sign of dispersion never appears) to make a bright
  soliton on this lattice.

**Reading:** this joins a now-robust pattern — **no *local field-amplitude
response* binds a mobile particle on the (x,c) cylinder**: clip (defocusing),
spillover, quantize, focus-SPM, and now knob-A index all fail. The phase/index
was my simplification of the idea ("cleaner containment"); its failure suggests
containment needs the **geometric** version the original intuition actually
named — a real **physical contraction / dimple** (knob B), which refracts via
*actual geometry* and *propagates elastically*, not a mere phase. So **knob B is
promoted from "later, for gravity" to possibly essential for containment too** —
consistent with the original emphasis on physical contraction.

Two honest forks this opens:
- **(geometry)** build **knob B** (edges physically contract; neighbours relax)
  and test whether a self-dug *dimple* traps a mobile particle — and carries the
  1/r tail. The direction's real payoff, but a bigger build (dynamical lattice).
- **(reframe)** the repeated failure of "trap a wave into a particle" may be the
  signal that the particle is **not** a trapped wave at all but mechanism **I**'s
  whole-quantum **instantiation** (a click on a dispersing guide wave). Knob-A's
  result is also evidence *for* that reading.

### Knob B (dynamical strain field) — built in full; also does not bind

Implemented faithfully: a real strain field `s(x,c)` that is **sourced** by load,
**spreads** elastically (∇²s), and **relaxes** (lamB), back-reacting on the wave
in two modes — `phase` (index) and `delay` (strain physically slows transit, the
geometric version). Results:

- **Containment: negative, both modes.** A moving packet still disperses ~3.8×
  for all gB, both back-reactions. The `phase` mode inherits knob A's failure (a
  phase is a phase); the `delay` mode (blend of moved/held field — an approximate,
  and slightly suspicious, group-delay) also fails to bind. At gB≈0.2 the well
  *nearly stops* the packet (speed 0.28→0.05 — it is being *captured/slowed*) but
  never *confines* it. No stable-soliton window; strong coupling just blows the
  strain up (|s|→24, phase-wrapping).
- **Gravity-carrier: partial positive (and separable).** The strain field itself
  is **real, builds up, and spreads** (max|s| up to ~24 over a finite reach) — a
  genuine geometric field sourced by load and propagating to neighbours. So the
  *mechanism for a gravity carrier* (a spreading elastic strain) **exists in the
  sim**, even though it does not *contain the particle*. Its long-range law can't
  be judged here (this sim is 1D-in-space; the 1/r needs 3D) — that is a separate,
  later test.
- **Caveats:** rest objects can't be cleanly tested for knob-B trapping on this
  lattice (a static n=0 lump freezes half its energy on the non-transporting ±c
  edges; the winding is flat-band) — so knob B was only cleanly tested on a
  *moving* packet, which outruns a slow well. The delay-blend is not exactly
  conservative. These leave a *narrow* door open, but the weight of evidence is
  clear.

### The decisive pattern (seven mechanisms)

Nothing binds a mobile particle on the (x,c) cylinder: clip, spillover, quantize,
focus-SPM, knob-A index, knob-B phase, knob-B delay. Two readings survive, and
the second is now the more likely:

1. **The testbed is inadequate.** The cylinder has real pathologies (strong
   dispersion, a flat winding band, ±c energy-freezing). A cleaner or richer
   substrate (2D-torus compact dimension; or a proper 3D-space sim for the
   gravity tail) might behave differently.
2. **The particle is not a self-bound wave.** Seven failures is strong evidence
   that "trap a wave into a particle" is the wrong model, and that the particle
   is mechanism **I**'s whole-quantum **instantiation** — a discrete *click* on a
   guide wave that is *allowed* to disperse. This is where the weight now sits.

**Separation achieved:** the responsive-medium idea splits cleanly — its
**gravity half** (a real spreading strain carrier) is *alive* and worth a proper
(3D) test; its **containment half** (self-binding the particle) is *not working*
here, and points to mechanism I for what a particle is.

## Gate relevance

Knob A targets **G3** (containment + persistence) *with mobility* — the specific
thing mechanism III failed on the 1D ring. Result: index/phase knob A does not
deliver it. Knob B (geometric) is the next candidate; knob B also targets the
long-range gravity that is outside the particle gate but is the grid-gravity
revival.
