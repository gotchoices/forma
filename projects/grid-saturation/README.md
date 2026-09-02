# grid-saturation

**Type:** Exploratory, computational-first project (see [../README.md](../README.md))

**Question (refocused).** Can GRID support **more than EM and gravity** — a
**particle**, and the **quantum phenomena** (dual slit, single detection, the
Born rule)? Can the same substrate that gives Maxwell also give *matter* and
*measurement*? (Entry point: whether the **bounded/saturating** substrate does
it. The answer turned out to be subtler — see the arc.)

**Testbed.** A minimal **1D-space × 1D-compact (x, c) cylinder** — x along the
axis, c periodic around it. A photon is the **c-uniform (n=0)** mode propagating
in x; a particle involves the **compact (n≥1)** sector. Every result here comes
from a sim, graded honestly (this project has a standing rule against
asserting).

---

## The headline

**A particle can be a *contained wave*, and GRID is *intrinsically* able to bind
one — but not through the saturation bound.** The arc:

1. **The value-bound is *defocusing*.** The saturation/clip we started from
   flattens peaks; it (and six other local mechanisms) **cannot** bind a
   particle. A repo-wide survey confirmed *no* forma study had ever demonstrated
   dynamical containment.
2. **The missing ingredient is a *focusing* nonlinearity.** Supplying the
   standard focusing+saturating recipe binds a stable, mobile particle (a
   Q-ball) — but that recipe was borrowed, non-GRID.
3. **GRID supplies it natively — through the compact *phase*.** A compact
   dimension is a phase, and a phase's potential is periodic: **U = m²(1 − cos φ)**,
   whose expansion is **focusing (−φ⁴) + saturating (+φ⁶) for free**. This is
   **sine-Gordon**; its **breather** is a stable, mobile, energy-conserving
   particle (confirmed on the discrete (x,c) lattice), and its **kink** is a
   phase **winding = charge**. One compact-phase potential gives **mass
   (breather) and charge (kink)**. *(The mechanism is scale-blind: the relevant
   compact dimension is a **Ma sheet** for a massive particle — its size sets the
   mass, ω₀∝1/R; the **ℵ-line** is the Planck-scale one, relevant to the photon's
   substrate/gauge, not to ordinary mass. See [work/promotion-hierarchy.md](work/promotion-hierarchy.md).)*
4. **The de Broglie relation is GRID-native.** The compact **Compton clock**
   (mass) stays in **phase harmony** with the open-dimension wave, giving
   **λ = h/p** from the geometry.

This is **Act 1 (the particle) — done.** It also confirmed the **promotion
ladder** (light→mass→charge; [grid-duality ch.7](../grid-duality/07-wrap-promotion-modeling.md))
dynamically, with **stability = a protected winding** (Q-ball stable vs oscillon
radiating). See [work/promotion-hierarchy.md](work/promotion-hierarchy.md).

**Act 2 (measurement) — the frontier, entered.** On a 2D GRID lab (barrier =
mass-blocked nodes, slit = open GRID), a wave passes **both** slits and
**interferes** (fringe spacing = the de Broglie λ), and **single whole-quantum
lumps rebuild the fringes** (corr→0.97). Under the *breather-as-a-real-lump*
reading, **collapse is dissolved** — a detection *reveals* a hidden-variable
center, it doesn't collapse. A toy **Bell test** confirms the model's *structure*:
a **local** shared-fiber phase is capped at CHSH=2 (classical), while a
**non-local fiber** (global self-consistency) reaches **CHSH=2√2 = QM with no
signaling** — Bohm-like non-locality with the compact fiber as carrier.
Details: [dual-slit-result](work/dual-slit-result.md) · [measurement-and-bell](work/measurement-and-bell.md) · [bell-test-result](work/bell-test-result.md).

**Single-particle Born is done** (as consistency): energy density ∝ |ψ|² (a wave
fact) + whole-quantum absorption (grid-quantization) + linear detection ⇒
P(click) ∝ |ψ|² — the semiclassical "detection ∝ intensity," **no steering, no
collapse** ([work/born-single-particle.md](work/born-single-particle.md),
derivation-ready). **One hard core remains: entangled/multi-particle Born** (the
Bell correlations), which needs *non-local* hidden variables. We need only exhibit
**one feasible placeholder** — e.g. **S itself closed/periodic** (need not be 3D,
could be smaller than it looks; its periodic-BC global self-consistency is a
genuine non-local constraint) — to show non-locality is *feasible* on a
GRID-compatible geometry (the toy Bell test already shows such a structure reaches
QM with no signaling). Deriving the *exact* cos(a−b) from a specific closed
geometry is the open core.

---

## Paths we are exploring (quantified)

### A. Binding — what localizes a particle (mechanisms *tested*)

| Mechanism | Idea | Verdict |
|---|---|---|
| Value-bound (clip) | hard amplitude bound | **Defocusing** — flattens peaks, cannot bind |
| Spillover | excess redirected edge→edge | No pump; no persistent S→c transfer |
| Discreteness (crude `--quantize`) | indivisible ±1 | **Inconclusive** — non-conserving, freezes the whole lattice |
| Kerr index (knob A) | load-dependent phase delay | Slows the wave but **does not bind** |
| Strain / metric (knob B) | load-dependent contraction | Captures/slows, **no confine**; but a *real* gravity-carrier (separable) |
| Topological winding (phase) | ℵ-winding soliton | Protected + localized but **immobile** (flat band) |
| Focusing+saturating (Q-ball) | *posited* cubic-quintic | **Works** — stable, mobile — but **borrowed, non-GRID** |
| **Compact-phase cosine (sine-Gordon)** | ℵ-line periodicity → U=m²(1−cos φ) | **✓ WORKS, GRID-native** — breather = particle, kink = charge |

Detail: [results-m1-m2](work/results-m1-m2.md) · [phase-winding-results](work/phase-winding-results.md)
· [responsive-medium](work/responsive-medium.md) · [soliton-result](work/soliton-result.md)
· [focusing-from-phase](work/focusing-from-phase.md). Scoring gate: [binding-evaluation](work/binding-evaluation.md).

### B. Interpretation — what a particle *is* and how it is measured (*working hypotheses, open*)

| Hypothesis | A particle is… | Handles | Open edge |
|---|---|---|---|
| **Contained-wave** | a soliton/breather, always localized | mass, charge, mobility — now demonstrated | may over-localize (free particles should spread) |
| **Wave-until-interaction** | a wave; localization is an *interaction event* | no containment needed; dual slit; Born via the bound | needs the collapse mechanism; nonlocality |
| **Double-solution** | a bulk (soliton) + pilot wave (walking droplet) | single-particle *everything*, locally | entanglement needs the fiber; Born emergent |
| **de Broglie harmony** *(foundation, shared)* | compact clock ⇌ open wave | **λ = h/p**, matter waves | not a rival — an ingredient all three need |

Measurement fork (forced by Bell): **(A) conserved collapse → mandatory
*non-signaling* nonlocality, whose GRID home is the compact fiber** (favored), vs
**(B) Reiter local loading → multi-click, disfavored by single-photon
anticorrelation**. Detail: [thesis-wave-until-interaction](work/thesis-wave-until-interaction.md)
· [thesis-double-solution](work/thesis-double-solution.md) · [foundation-de-broglie-harmony](work/foundation-de-broglie-harmony.md).

---

## What is verified vs. open

**Verified (from sims):**
- **M1 — KK decoupling.** Photons propagate in x, pass through each other; the
  compact sector is decoupled; the winding mode is massive/gapped. (First
  dynamical KK test in forma.)
- **Binding.** Sine-Gordon breather is stable, mobile, energy-conserving on the
  discrete (x,c) lattice; survives Peierls–Nabarro; a c-localized (2-extended-D)
  lump disperses (Derrick), so **(x, compact-c) is the right dimensionality**.
- **Relativistic matter waves + de Broglie.** GRID's exact dispersion (eigenvalues
  of the scatter+propagate operator) is **massless for the photon** and
  **relativistic (Ω²=c²k²+ω₀²) for the massive KK modes**, same c≈0.70 across
  sectors, to <2% for kx<0.4π; **de Broglie v_p·v_g=c²** holds (1–6%); and the
  **KK mass tower** ω₀(n)=n·(2π/nc)·c falls out. [work/de-broglie-dispersion-result.md](work/de-broglie-dispersion-result.md).
- **Free-space stability needs a winding.** 2D test: a real-scalar lump disperses
  (linear) or collapses (focusing); an **oscillon** (unprotected) quasi-stably
  radiates; a **Q-ball** (conserved winding) is stable. So *stability = a protected
  winding* ([work/soliton-result.md](work/soliton-result.md), 2D).
- **Two-slit interference + single-lump build-up.** On the GRID lab, a wave through
  both slits interferes (fringe spacing = de Broglie λ); single whole-quantum lumps
  rebuild the fringes (corr→0.97) — no collapse invoked. [work/dual-slit-result.md](work/dual-slit-result.md).
- **Bell *structure*.** A local shared-fiber phase gives CHSH=2; a non-local fiber
  reaches CHSH=2√2 (=QM) with no signaling. The fiber-non-locality is in the right
  class. [work/bell-test-result.md](work/bell-test-result.md).

**Verified (Act 2):**
- **Single-particle Born.** P(click) ∝ |ψ|² from energy density + whole-quantum
  absorption + linear detection — no steering, no collapse (consistency-level,
  derivation-ready). [work/born-single-particle.md](work/born-single-particle.md).

**Open (the frontier — one hard core + a loose end):**
- **Entangled / multi-particle Born (the Bell correlations).** Needs *non-local*
  hidden variables. A closed/periodic geometry (global self-consistency) is a
  *feasible* placeholder — structure confirmed (toy reaches QM, no signaling);
  deriving the *exact* cos(a−b) from a specific constraint is the open core.
  Plausibly its own project.
- **The reduction gap (loose end).** The scatter gives the *coupling* term; the
  on-site cosine is still *posited* — deriving it from the literal directed-edge
  scatter makes "GRID is focusing" first-principles.

## Concrete next work (ranked)

1. **Formalize single-particle Born** — make premise 4 (linear whole-quantum
   detection) a *lattice theorem* (detector = absorbing nodes; transfer rate linear
   in incident edge energy), turning [born-single-particle.md](work/born-single-particle.md)
   from consistency-level into a derivation. Ripest.
2. **Close the sine-Gordon reduction** — the on-site cosine from the directed-edge
   scatter (Act 1 loose end).
3. **Entangled Born from a closed-geometry constraint** — derive cos(a−b) from one
   concrete non-local placeholder (periodic S / closed manifold). The hard core;
   likely a separate project.
4. *(Optional)* **guidance test** — does a breather get *steered* to |ψ|² by its de
   Broglie wave? Not needed for Born (energy density suffices), but it would give
   deterministic per-particle trajectories (the stronger Bohmian program).
5. **Follow-on:** sweep nc to hand the KK mass tower to [metric-mass](../metric-mass/).

## Connective threads (why this is more than wishful)

- **grid-gravity lesson.** The value-bound gives a *mass* (contact), not a
  *metric* (long-range) — which blocked [grid-gravity](../grid-gravity/) but was
  the *right* flavour here. (And knob B's strain field is a live gravity-carrier
  candidate — a possible grid-gravity revival, tracked in [responsive-medium](work/responsive-medium.md).)
- **Reiter / threshold.** Single-photon anticorrelation (Grangier–Aspect 1986)
  disfavors Reiter's multi-click loading → GRID needs the conserved snap. See
  [primers/threshold-theory.md](../../primers/threshold-theory.md).
- **Bell + collapse = the same fiber.** The nonlocality collapse needs is the
  nonlocality Bell forces; the compact fiber is the candidate home for both.
- **Barandes.** Interference needs correlated (non-Markovian) fork-weights, not
  independent coin-flips — matching QM = indivisible stochastic process.

## Relation to other projects

- [grid-quantization](../grid-quantization/) — the bounded/sigma-delta substrate
  for occupation quantization; this project builds its dynamics.
- [metric-mass](../metric-mass/), [metric-charge](../metric-charge/) — mass =
  compact standing wave; charge = winding — now realized as sine-Gordon
  breather/kink. The de Broglie measurement (#1) would revive metric-mass.
- [grid-gravity](../grid-gravity/) — parked; knob B is a possible revival.
- [ma-domain](../ma-domain/) — its threshold-dynamics names γ→e⁺e⁻ as a test.

## The work/ folder

The full record of the reasoning — results, the scoring gate, the foundation
note, and the working hypotheses — is indexed in [work/README.md](work/README.md).
