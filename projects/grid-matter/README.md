# grid-matter

**Does GRID produce matter *and* quantum mechanics — beyond EM and gravity?**

**Type:** Exploratory, computational-first project (see [../README.md](../README.md)).

*Formerly `grid-saturation`.* The entry hypothesis — that the **saturation bound**
makes particles — was **refuted**: the value-bound is *defocusing* and cannot bind.
The real answer is the **compact phase**, and the project grew into the broader
question above. The old name pointed at a dead branch; this one names the trunk.

**Testbed.** The (x, compact-c) cylinder: a photon is the c-uniform **n=0** mode; a
particle lives in the compact **n≥1** sector. Everything here comes from a sim,
graded honestly, then pushed toward derivation.

---

## The arc (chapter outline)

Status flags — **[D]** derivable now (clean analytics; the sims are proof-of-concept
in advance) · **[C]** computationally demonstrated (continuum-analytic where noted)
· **[P]** posited link (a gap) · **[O]** open.

**Ch 0 — Question & testbed**
- GRID = the causal impedance-scatter lattice; can it give matter + QM, not just Maxwell?
- The (x, compact-c) cylinder; photon = n=0, particle = compact sector.
- Method: model computationally, then derive; every claim sim-graded.

### Act 1 — GRID makes matter *(largely done)*

**Ch 1 — Why the obvious mechanism fails (the instructive negatives)**
- A clip/wall on a *linear amplitude* is **defocusing** (frequency rises with amplitude) → cannot bind. **[D]**
- **Seven** local mechanisms fail: clip, spillover, crude-quantize, Kerr-index (knob A), strain (knob B), phase-winding (flat-band/immobile). **[C]**
- Repo-wide survey: *no* prior forma study showed dynamical containment ⇒ the missing ingredient is a **focusing** nonlinearity. (These negatives are load-bearing — they are the argument for Ch 2.)

**Ch 2 — The compact phase is intrinsically focusing (the key result)**
- A compact dimension *is a phase* → periodic potential **U = m²(1 − cos φ)**.
- Taylor: quartic **−m²/24 (focusing)** + sextic **+m²/720 (saturating)** — the soliton recipe, from periodicity alone. **[D]**
- **Sine-Gordon:** breather = neutral **mass**, kink = **charge** (winding); stable, mobile, energy-conserving on the discrete lattice (survives Peierls–Nabarro). **[C]**
- Gap: derive the on-site cosine from the *literal directed-edge scatter*. **[P]**

**Ch 3 — Matter waves, mass, de Broglie**
- GRID's exact dispersion = **eigenvalues of M = P·S** (the dynamics diagonalized). **[D]**
- Photon **massless** (Ω=ck); massive KK modes **relativistic** (Ω²=c²k²+ω₀²), same c across sectors (Lorentz-consistent), to <2% for k<0.4π. **[D small-k + C]**
- **KK mass tower** ω₀(n) = n·(2π/nc)·c ∝ 1/R. **[D]**
- **de Broglie:** phase harmony v_p·v_g = c² ⇒ **λ = h/p**. **[D]**

**Ch 4 — Stability & dimensionality (a particle is a winding)**
- Free 2D space: a real-scalar lump **disperses** (linear) or **collapses** (Derrick). **[D]**
- **Stability = a conserved winding:** Q-ball stable, oscillon slowly radiates. **[C + Q-ball D]**
- One extended dimension for a breather; the winding-charge lifts it to higher-D.

**Ch 5 — The promotion ladder (light → mass → charge)**
- Each level = the previous **captured** (a winding in a new compact cycle); ties to [grid-duality ch.7](../grid-duality/07-wrap-promotion-modeling.md). **[D-narrative]**
- Stability = a protected winding; the **ephemeral particle zoo is data** (its quantum numbers = the ladder's observables).
- Prediction: **charged ⟹ massive** (electric); the gluon/color caveat lives at L4.

### Act 2 — GRID makes quantum mechanics *(frontier)*

**Ch 6 — The two-slit lab (interference)**
- GRID slit-ontology: **barrier = mass-blocked nodes; slit = open GRID.**
- Wave through **both** slits interferes; fringe spacing = de Broglie λ (matches λL/d). **[C]**

**Ch 7 — Single-particle Born**
- Energy density ∝ |ψ|² (a wave fact) + **whole-quantum absorption** (grid-quantization) + linear detection ⇒ **P(click) ∝ |ψ|²**. **[D — derivation-ready]**
- Single lumps rebuild the fringes; **no steering, no collapse.** **[C]**

**Ch 8 — Measurement without collapse**
- The breather = a real **lump** (hidden-variable center); measurement **reveals**, not collapses. **[narrative]**
- Two unknowns: the interference envelope (|ψ|²) vs the specific draw (= single-particle Born, Ch 7, done).

**Ch 9 — Entanglement & Bell (the one open core)**
- Local shared-phase → classical (CHSH=2); non-local → **QM (2√2), no signaling**. **[C toy]**
- Non-locality carrier: the **fiber / closed-geometry global self-consistency** (periodic BCs) — *feasibility, one placeholder*, not an asserted theory.
- **Open:** derive exact **cos(a−b)** from a concrete closed-geometry constraint — an *atemporal global-constraint* computation, likely its own project. **[O]**

---

## Derivation readiness (audited — pre-derivation work files done)

**Substantially derivable now, not narrative.** Three focused work files pinned
down exactly what proves out:

- **Ch 3 — fully derivation-ready, the firmest chapter.** The dispersion is
  **closed-form**: cos ω = −(cos kx + cos kc)/2 ⇒ light-speed **c = 1/√2**, KK mass
  tower **ω₀(n) = n·(2π/nc)/√2**, relativistic **Ω²=c²k²+ω₀²**, de Broglie
  **v_p·v_g=c²** — all exact, verified to 6 digits, **no phase posit** (needs only
  the scatter + a compact *coordinate*). [work/dispersion-analytic.md](work/dispersion-analytic.md).
- **Ch 2 — a clean *conditional* derivation.** The scatter gives only the kinetic
  term; but **given one foundational premise — the compact field value is a *phase*
  (circle: the ℵ-line / a sheet U(1)), not a bounded *amplitude* (interval)** — the
  cosine is **forced** (periodicity + KK mass ⇒ the unique minimal periodic
  potential m²(1−cos φ)), and focusing+saturating + breather=mass + kink=charge
  follow. The premise is foundational, not ad hoc; S does not fix interval-vs-circle
  (which also explains *why saturation failed*: a clipped amplitude is a wall,
  defocusing; a phase is periodic, focusing). [work/reduction-cosine-from-scatter.md](work/reduction-cosine-from-scatter.md).
- **Ch 7 — derivation-ready (Born distribution).** P(x) ∝ |ψ|² from: ρ = |ψ|² (an
  *identity* — the conserved energy density), linear capture (automatic for an
  absorbing node), and whole-quantum single click (grid-quantization). The one
  input — probabilistic capture ∝ local energy — is the *universal* photodetection
  premise, not GRID-specific. [work/born-detection-theorem.md](work/born-detection-theorem.md).

**Cited/standard (no new proof):** Ch 6 (linear-wave interference), Ch 4 (Derrick,
Q-ball), Ch 5 (grid-duality ch.7). **Open [O]:** Ch 9 (entangled Born) — a separate
project. So a *complete* matter-half derivation is in reach today, resting on one
named foundational premise (Ch 2's phase-topology); the QM half is derivation-ready
through Ch 7, with Ch 9 the single genuinely-open core.

## Status, work record, relations

Full reasoning, results, and the working arc are indexed in
[work/README.md](work/README.md). Key results: [focusing-from-phase](work/focusing-from-phase.md)
· [de-broglie-dispersion-result](work/de-broglie-dispersion-result.md)
· [born-single-particle](work/born-single-particle.md) · [bell-test-result](work/bell-test-result.md)
· [promotion-hierarchy](work/promotion-hierarchy.md).

- [grid-quantization](../grid-quantization/) — the whole-quantum bound Ch 7 uses.
- [grid-duality](../grid-duality/) — the canonical promotion ladder (Ch 5).
- [metric-mass](../metric-mass/) / [metric-charge](../metric-charge/) — the
  continuum mass/charge derivations; Ch 3's mass tower corroborates metric-mass.
- [grid-gravity](../grid-gravity/) — parked; knob B's strain field (Ch 1) is a
  possible revival, tracked in [responsive-medium](work/responsive-medium.md).
