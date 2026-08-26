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
3. **GRID supplies it natively — through the compact *phase*.** The ℵ-line is a
   compact phase, and a phase's potential is periodic: **U = m²(1 − cos φ)**,
   whose expansion is **focusing (−φ⁴) + saturating (+φ⁶) for free**. This is
   **sine-Gordon**; its **breather** is a stable, mobile, energy-conserving
   particle (confirmed on the discrete (x,c) lattice), and its **kink** is a
   phase **winding = charge**. One compact-phase potential gives **mass
   (breather) and charge (kink)**.
4. **The de Broglie relation is GRID-native.** The compact **Compton clock**
   (mass) stays in **phase harmony** with the open-dimension wave, giving
   **λ = h/p** from the geometry.

What remains genuinely open is **measurement**: how a delocalized wave yields a
single, |ψ|²-distributed click — and where the required Bell nonlocality lives.

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

**Open (the frontier):**
- **The reduction gap.** The scatter gives the *coupling* term; the on-site
  cosine is still *posited* as the phase potential — deriving it from the literal
  directed-edge scatter is the step that makes "GRID is focusing" first-principles.
- **Measurement (M3/M4).** Does the bound turn a wave–wave interaction into a
  **single |ψ|²-distributed click**? Where does Bell nonlocality live (the fiber)?
- **de Broglie in the lattice.** Is GRID's massive dispersion relativistic
  (ω²=c²k²+ω₀²) and does phase harmony survive a boost? (Lattices break Lorentz —
  this is a real test, not automatic.)

## Concrete next work (ranked by substance-per-effort)

1. ~~Matter-wave dispersion / de Broglie measurement~~ **DONE** — GRID gives
   relativistic matter waves, de Broglie v_p·v_g=c², and the KK mass tower
   ω₀(n)=n·(2π/nc)·c, to <2% for kx<0.4π.
   [work/de-broglie-dispersion-result.md](work/de-broglie-dispersion-result.md).
   *Follow-on: sweep nc to hand the mass tower to [metric-mass](../metric-mass/).*
2. **Close the sine-Gordon reduction** — derive the on-site cosine from the
   directed-edge scatter (what pins the phase / opens the gap).
3. **The Born / single-detection test** — two spread packets interact on the
   bounded lattice; do single quantized events appear ∝ |ψ|²? *(The prize; higher
   risk; do after 1.)*

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
