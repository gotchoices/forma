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

## Writing approach

**Brief, and attribution-forward.** Where a chapter *corroborates* standard physics
(KK/Bloch bands, sine-Gordon solitons, semiclassical photodetection) or another
forma project (metric-mass, metric-charge, grid-duality, grid-quantization), it
**cites and states the result in a few lines — it does not re-derive it**. Prose and
proof are spent only on the **forma-specific content**: the binding-mechanism
diagnosis (Ch 3), the exact GRID dispersion (Ch 4), the negatives (Ch 2), and the
honest scoping of what's derived vs posited vs open. Chapter files are drafted first
as **bullet outlines** for review, then in-filled.

## The arc (chapter outline)

Status flags — **[D]** derivable now (clean analytics; the sims are proof-of-concept
in advance) · **[C]** computationally demonstrated (continuum-analytic where noted)
· **[P]** posited link (a gap) · **[O]** open.

**[Ch 1](01-foundation.md) — Question & testbed**
- GRID = the causal impedance-scatter lattice; can it give matter + QM, not just Maxwell?
- The (x, compact-c) cylinder; photon = n=0, particle = compact sector.
- Method: model computationally, then derive; every claim sim-graded.

### Act 1 — GRID makes matter *(largely done)*

**[Ch 2](02-why-simple-binding-fails.md) — Why the obvious mechanism fails (the instructive negatives)**
- A clip/wall on a *linear amplitude* is **defocusing** (frequency rises with amplitude) → cannot bind. **[D]**
- **Several** local mechanisms fail: clip, spillover, crude-quantize, Kerr-index (knob A), strain (knob B), phase-winding (flat-band/immobile). **[C]**
- Repo-wide survey: *no* prior forma study showed dynamical containment — which *motivates* (not deductively implies) the missing ingredient being a **focusing** nonlinearity (independently: focusing+saturating is the standard soliton recipe). (These negatives are load-bearing — they are the argument for Ch 3.)

**[Ch 3](03-compact-phase-focusing.md) — The compact-phase *field value* is intrinsically focusing (the key result)**
- If the field *value* (not the coordinate — that's Ch 4) is a compact phase — a
  circle: the **ℵ-line**, or a sheet's **U(1)** — its potential is periodic; the
  **minimal** periodic completion of a mass m² is **U = m²(1 − cos φ)**. *(A
  conditional premise: S does not force circle-over-interval; see reduction file.)*
- Taylor: quartic **−m²/24 (focusing)** + sextic **+m²/720 (saturating)** — focusing
  **if the lowest harmonic dominates** (higher harmonics could flip it). **[D, minimal-completion]**
- **Sine-Gordon:** breather = neutral **mass**; kink = a **topological (ℤ) winding = charge** (*not* a Q-ball Noether charge — the cosine gives both consistently). Stable, mobile, survives Peierls–Nabarro on the discrete lattice. **[C]**
- **Mass and charge are *different* excitations, not the same object twice:** mass = the **breather** (a winding-0 *oscillation*, the 1D minimal projection) / a compact-mode standing wave; charge = a **topological winding** (kink). On a 2D sheet both live together (the tube/ring cycles; [metric-charge](../metric-charge/)'s (m,n)), but as an oscillation-plus-winding — the sheet lift is a *different construction* from the 1D breather, deferred to metric-charge.
- Gap: derive the on-site cosine from the *literal directed-edge scatter*. **[P]**

**[Ch 4](04-matter-waves-and-de-broglie.md) — Matter waves, mass, de Broglie**
- GRID's exact dispersion = **eigenvalues of M = P·S** (the dynamics diagonalized). **[D]**
- Photon **massless** (Ω=ck); massive KK modes **relativistic** (Ω²=c²k²+ω₀²), same c across sectors (Lorentz-consistent), to <2% for k<0.4π. **[D small-k + C]**
- **KK mass tower** ω₀(n) = n·(2π/nc)·c ∝ 1/R. **[D]**
- **de Broglie:** phase harmony v_p·v_g = c² ⇒ the **λ = h/p** *shape* (ℏ enters as a units conversion p=ℏk, not derived — per the project's principle-vs-scale rule). **[D]**

**[Ch 5](05-stability-and-dimensionality.md) — Stability & dimensionality**
- Free 2D space: a real-scalar lump **disperses** (linear) or **collapses** (Derrick). **[D]**
- 1D solitons exist (breather, kink) and a **2D Q-ball** is stable — but the Q-ball's stabilizer is its **Noether** charge, which C1 disavowed as the GRID mechanism. So the Q-ball is only evidence that *some* wound object can be 3D-stable, **not** a proof for the adopted **topological** charge. **[C, borrowed]**
- **Localized-3D particles are owed — for charged *and* neutral.** A single U(1) winding is a **vortex line** (codim-2); a kink is a **domain wall** (codim-1); neither is a localized (codim-3) particle, and skyrmion/Hopfion protection needs **π₃** target topology a single compact phase does not supply. A GRID **sheet** (fixed-size compact structure + windings) plausibly localizes+stabilizes, but that construction is **[metric-charge](../metric-charge/)'s, not demonstrated here**. **[O]**
- **Open trade-off:** a Q-ball-style **Noether** charge *would* supply the 3D existence-proof — but readmitting it **reopens C1** (Noether ≠ topological winding). Topological-charge (resolves C1) vs Noether-charge (gives 3D stability) is an unresolved fork.

**[Ch 6](06-promotion-ladder.md) — The promotion ladder (light → mass → charge)**
- Each level = the previous **captured** (a winding in a new compact cycle); ties to [grid-duality ch.7](../grid-duality/07-wrap-promotion-modeling.md). **[D-narrative]**
- Stability = a protected winding; the **ephemeral particle zoo is data** (its quantum numbers = the ladder's observables).
- Consistency check (structural, not an independent prediction — charge *is* captured mass): **charged ⟹ massive** (electric only) — *caveat: rests on an untested reframe of gluons (massless, color) as binding-resonance, not ladder particles*.

### Act 2 — GRID makes quantum mechanics *(frontier)*

*Honest scope: the **distinctively-quantum, non-classical** content is
**entanglement/Bell (Ch 10), which is open**. Ch 7 is classical wave; Ch 8's single
whole-quantum click is genuinely quantum but its |ψ|² distribution is assumed. So
Act 2 is a **question**, and Ch 10's toy is an arithmetic consistency check, not
physics progress.*

**[Ch 7](07-two-slit-lab.md) — The two-slit lab (interference)**
- GRID slit-ontology: **barrier = mass-blocked nodes; slit = open GRID.**
- Both a **photon** (massless) and a **matter wave** (compact n=1, massive) interfere on the same lattice; the matter mode has a **longer de Broglie λ** (11.18 vs 8.07 nodes, exact from the dispersion) and coarser fringes. *This is **classical** linear-wave interference (matter follows from photon by linearity) — staging, not yet distinctively quantum; the absolute spacing is non-paraxial, so λL/d is not fit.* **[C]**

**[Ch 8](08-single-particle-born.md) — Single-particle Born**
- Energy density = ρ = |ψ|² (identity, scatter unitarity) + **whole-quantum single click** (grid-quantization — the genuine quantum piece) + **detection probability ∝ local energy**. ⇒ **P(click) ∝ |ψ|²**. **[D distribution — but the ∝-probability step is Born's content, the *universal* photodetection premise, *assumed*]**
- Single lumps rebuild the fringes (sim). **[C]**

**[Ch 9](09-measurement-ontology-fork.md) — Measurement: an open ontology fork (not "no collapse, settled")**
- Two readings, both consistent with the Born distribution: **(i) wave-until-interaction** (delocalized, localizes at detection) vs **(ii) double-solution** (a real **lump** + a delocalized **de Broglie pilot** through both slits). **[fork, open]**
- "No collapse" holds only in (ii), and **only if the bulk⟷pilot guidance dynamics work — which is owed/untested**. The paper must present the fork, not assert one.

**[Ch 10](10-entanglement-and-bell.md) — Entanglement & Bell (the one open core)**
- Local shared-phase → classical (CHSH=2); non-local → **QM (2√2), no signaling**. **[C toy]**
- Non-locality carrier: the **fiber / closed-geometry global self-consistency** (periodic BCs) — *feasibility, one placeholder*, not an asserted theory.
- **Open:** derive exact **cos(a−b)** from a concrete closed-geometry constraint — an *atemporal global-constraint* computation, likely its own project. **[O]**

---

## Derivation readiness (audited — pre-derivation work files done)

**Substantially derivable now, not narrative.** Three focused work files pinned
down exactly what proves out:

- **Ch 4 — fully derivation-ready, the firmest chapter.** The dispersion is
  **closed-form**: cos ω = −(cos kx + cos kc)/2 ⇒ light-speed **c = 1/√2**, KK mass
  tower **ω₀(n) = n·(2π/nc)/√2**, relativistic **Ω²=c²k²+ω₀²**, de Broglie
  **v_p·v_g=c²** — the closed form matches the exact eigenvalues to machine
  precision and the time-domain sim to ~4 sig figs; **no phase posit** (needs only
  the scatter + a compact *coordinate*). [work/dispersion-analytic.md](work/dispersion-analytic.md).
- **Ch 3 — a clean *conditional* derivation.** The scatter gives only the kinetic
  term; but **given one foundational premise — the compact field value is a *phase*
  (circle: the ℵ-line / a sheet U(1)), not a bounded *amplitude* (interval)** — the
  **minimal** periodic completion of the KK mass is m²(1−cos φ), which is
  focusing+saturating (assuming the lowest harmonic dominates); breather=mass and
  kink=**topological**-charge follow. The premise is foundational, not ad hoc; S
  does not fix interval-vs-circle (which also explains *why saturation failed*: a
  clipped amplitude is a wall, defocusing; a phase is periodic, focusing).
  [work/reduction-cosine-from-scatter.md](work/reduction-cosine-from-scatter.md).
- **Ch 8 — derivation-ready (Born distribution).** P(x) ∝ |ψ|² from: ρ = |ψ|² (an
  *identity* — the conserved energy density), linear capture (automatic for an
  absorbing node), and whole-quantum single click (grid-quantization). The one
  input — probabilistic capture ∝ local energy — is the *universal* photodetection
  premise, not GRID-specific. [work/born-detection-theorem.md](work/born-detection-theorem.md).

**Cited/standard (no new proof):** Ch 7 (linear-wave interference), Ch 5 (Derrick,
Q-ball), Ch 6 (grid-duality ch.7). **Open [O]:** Ch 5 localized-3D particles;
Ch 10 entangled Born.

So the **matter half** rests on **three** honestly-named items: the Ch 3 phase-topology
**premise**, the cosine-from-scatter reduction **[P]**, and **localized-3D particle
stability [O]** (charged and neutral). Ch 4 (matter waves/mass/de Broglie) is
exact and premise-free. The **QM half** is derivation-ready through Ch 8 **modulo the
assumed detection premise**, with two genuinely-open cores: **localized-3D particles**
and **entangled Born (Bell)**.

## Status, work record, relations

Full reasoning, results, and the working arc are indexed in
[work/README.md](work/README.md). Key results: [focusing-from-phase](work/focusing-from-phase.md)
· [de-broglie-dispersion-result](work/de-broglie-dispersion-result.md)
· [born-single-particle](work/born-single-particle.md) · [bell-test-result](work/bell-test-result.md)
· [dualslit-matter-result](work/dualslit-matter-result.md) · [promotion-hierarchy](work/promotion-hierarchy.md).

- [grid-quantization](../grid-quantization/) — the whole-quantum bound Ch 8 uses.
- [grid-duality](../grid-duality/) — the canonical promotion ladder (Ch 6).
- [metric-mass](../metric-mass/) / [metric-charge](../metric-charge/) — the
  continuum mass/charge derivations; Ch 4's mass tower corroborates metric-mass.
- [grid-gravity](../grid-gravity/) — parked; knob B's strain field (Ch 2) is a
  possible revival, tracked in [responsive-medium](work/responsive-medium.md).
