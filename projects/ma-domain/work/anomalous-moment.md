# anomalous-moment.md — the anomalous magnetic moment as substrate chirality on a shaped tube

**Status:** Hypothesis / scoping file. Frames where a particle's anomalous magnetic moment could come from in the MaSt picture, sets out a single computational model that subsumes the two candidate mechanisms, and — importantly — identifies what is computable now versus what is gated on machinery the framework has not yet built. No results yet.

---

## 1. The observable

A charged particle that carries spin behaves as a small magnet. The **g-factor** is the dimensionless number relating that magnetic moment to the spin: a structureless point particle obeying the Dirac equation has **g = 2** exactly. Measurement gives slightly more — for the electron g/2 = 1.001 159 652…, for the muon g/2 = 1.001 165 920…. The **anomaly**

  a = (g − 2) / 2

is that excess, ≈ 0.001 16. In quantum electrodynamics it is a series in the fine-structure constant, a = ½(α/π) + … — each successive term one more virtual-photon correction (the series is asymptotic, though its first terms behave well).

Two features of the data set the targets for any model:

- **The leading anomaly is universal.** ½(α/π) ≈ 0.001 161 is the same for the electron and the muon; the two measured values differ only at the fourth significant figure, and that difference is a *subleading* effect.
- **Composite particles sit far from g = 2.** The proton has g ≈ 5.59; the neutron has a magnetic moment despite being electrically neutral. These large "anomalies" are read, in the Standard Model, as direct evidence that nucleons are *built from* charged constituents — they are not the small radiative anomaly of a fundamental particle.

---

## 2. Two hypotheses for the origin of *a*

**H1 — the cross-section shape alone.** A MaSt particle is a closure mode winding on a tube whose cross-section is not a circle (an ellipse for charged leptons, a clover for quarks — see [tube-function.md](tube-function.md)). A non-circular charge distribution could, on its own, shift g away from 2.

**H2 — substrate chirality applied to the shape.** The shape interacts with a *handed* (chiral) grid substrate. The anomaly is the product of the cross-section profile and the substrate's handedness; the leptons' simple convex ellipse gives a small anomaly, the quarks' folded clover packs more effective profile per cross-section and gives a larger one, with a sign set by the direction the lattice is wrapped.

**H2 is the stronger hypothesis, and H1 is its zero-chirality limit.** Three reasons:

1. **Sign.** A symmetric profile — and both the ellipse and the clover are reflection-symmetric — integrates with its odd-harmonic contributions cancelling: it can yield a *magnitude*, but it has no handedness, so it cannot yield the definite *sign* the anomaly has. H1 alone is therefore structurally incomplete. The substrate handedness in H2 is what supplies the sign.
2. **Magnitude contrast.** A folded clover carries far more curvature content per cross-section than a convex ellipse, so H2 naturally predicts a larger anomaly for quark-sector tubes than for leptons — matching the order-1 nucleon moments against the order-α lepton anomaly. H1 gives no natural reason for that contrast.
3. **Unification with charge sign.** The wrapping direction H2 invokes for the anomaly's sign is plausibly the *same* wrapping that already sets the charge sign (clover τ = 1/3 → +2/3, −1/3; ellipse → −1). One substrate handedness would then set both — predicting a correlation between a particle's charge sign and the sign of its anomaly.

---

## 3. The unifying model — chirality as a knob

Rather than testing H1 and H2 separately, model them as one object: introduce a **chirality parameter χ** that the substrate contributes to the moment integral. By construction χ = 0 recovers H1 (shape only) and χ ≠ 0 is H2. χ is a **single universal parameter** — one substrate, one handedness, shared by every sheet, lepton and quark alike; that sharing is what gives the model predictive teeth (§5).

This is a clean design, with one honesty caveat to keep in front: **χ is a posited phenomenological parameter, not a derived one.** The framework has no concrete model of the grid substrate's handedness yet, so the script can *fit* a χ that reproduces data within an assumed coupling — it cannot *derive* the grid's chirality. Likewise, "χ = 0 gives g = 2" is true *by construction* (χ is built as the only anomaly source); it is a property of the model, not an independent validation. The model's real content is entirely in the χ ≠ 0 prediction.

---

## 4. The g = 2 baseline — the spin account

The anomaly a = (g − 2)/2 is a deviation from a **baseline**, g = 2 — the Dirac value for a spin-½ particle. Computing a needs that baseline in place: the modes must carry spin ½.

They do, and the spin does **not** come from the winding ratio (m_t, m_r). It is a property of the *dimensional structure* a particle occupies. Under model-F's account ([R62 derivation 7d](../../../models/model-F.md)), every 2-torus sheet hosts a Dirac–Kähler field, yielding a spin-½ fermion tower **automatically — for every winding, the (1, 1) mode as much as the (1, 2)**. The photon's spin 1 comes from its different, grid-direct topology; compound particles (mesons, baryons) compose their per-sheet spins by SU(2) addition. Spin tracks the level of dimensional structure — single sheet, or compound — not the winding numbers.

This is the right account for a structural reason. The alternative — the Williamson & van der Mark reading, in which spin ½ is an artifact of the q = 2 ring winding of the (1, 2) mode — cannot give a (1, 1) mode a fermion's spin at all ([electron-tube.md §6.1](electron-tube.md): one ring wind returns the field after 360°, not 720° → boson-like). The per-sheet Dirac–Kähler account has no such problem: spin ½ attaches to the *sheet*, so the heavier (1, 1) quark of a generation is spin ½ exactly as the lighter (1, 2) one is.

So the g = 2 baseline is structural and already available — not a missing primitive. The anomalous-moment program is **not** gated on inventing spin. What it needs is to carry that per-sheet Dirac–Kähler account onto the candidate's shaped tubes and connect it to a magnetic-moment calculation. Two things there are genuinely open:

- a clean derivation of the magnetic moment, and of L = ℏ/2, for the Dirac–Kähler field on the *ellipse* and *clover* tubes specifically — [electron-tube.md](electron-tube.md) notes this is unwritten even for the ellipse;
- whether the per-sheet spin account survives unchanged in the K4 architecture, or needs revision.

What that leaves computable *now* is narrower than the moment itself — see §7. The one ungated, useful step is the §5 prerequisite: mapping the shape ranges the cross-section profiles are allowed.

---

## 5. Methodology — one universal χ against ranged profiles

The model's parameters are not symmetric in kind. **χ is a single universal number** — one substrate, one handedness — shared by every sheet. The cross-section profiles are *per-sector* and, importantly, **not pinned — only ranged**:

- the **ellipse** profile is constrained by the T(1, 2) floor / τ = 2 condition and by convexity ([electron-tube.md](electron-tube.md)) — to a range;
- the **clover** profile is constrained by the per-arc charges +2/3, −1/3 (the curvature integral ∫κ ds) and by the Z₃ three-lobe requirement ([tube-function.md](tube-function.md), [clover-quarks.md](../../sheet-proton/work/clover-quarks.md)) — but these fix only a *sub-locus*, not a point: a residual family of clover shapes all reproduce the charges.

So there is no "pin the profiles, then predict" — the profiles genuinely have ranges. The rigidity comes from elsewhere: **χ is shared across sectors.** Fix χ from one sector and the other sector's anomaly is constrained by χ together with that sector's profile range. The real test is therefore:

> Does *one* value of χ, combined with the independently-allowed ellipse and clover ranges, land *both* the lepton and the hadron anomaly?

Two disciplines keep that test honest:

1. **The profile ranges are whatever charge and closure independently allow — never widened to fit an anomaly.** Fitting the profiles to the anomalies would be circular; the ranges are an input from other physics, not an output of the AMM fit.
2. **The strength of the test scales with how narrow those ranges are.** If the clover range is wide, "one χ plus some clover in a wide range hits the hadron anomaly" proves little; if charge and Z₃ confine the clover tightly, a single χ working for both sectors is a strong, low-freedom result. Quantifying the clover range from the charge constraint is therefore a prerequisite, not a detail.

---

## 6. Scope of targets

- **Primary, clean — the universal lepton anomaly ½(α/π).** A single number, for fundamental particles, measured to extreme precision. This is the honest target for a single-χ, single-lepton-shape model.
- **Out of scope — the e/μ splitting.** The measured a_e and a_μ differ; a single-χ static model with one lepton shape predicts them *equal*. The difference is a subleading, neighborhood-dependent effect (mass-dependent running, or virtual leakage through shared dims — [mode-stability.md](mode-stability.md)); it is not what this model addresses.
- **Secondary, confounded — the quark sector.** Nucleon moments are properties of *three-quark composites*; this model computes a *single-sheet* quantity. The target on the quark side is the single-quark (clover-sheet) moment, with the assembly into a nucleon a separate composite step — and quark-level moments are themselves model-inferred, so the quark sector is aspirational, not a clean test.

---

## 7. Computable now vs gated

| Item | Status |
|---|---|
| Shape ranges the profiles are allowed — clover from the +2/3/−1/3 charges + Z₃, ellipse from τ = 2 + convexity | **computable now** — pure geometry on the harmonic family ([scripts/harmonic_tube.py](../scripts/harmonic_tube.py)); the §5 prerequisite, and the one ungated step with decision value |
| Magnetic moment of a winding current on a shaped cross-section | partially — a classical *orbital* moment is computable, but in isolation it is not g and not yet interpretable |
| Shape + χ modulation (the H1-vs-H2 study) | not yet — requires first *positing a mechanism* for how χ enters the moment integral; there is none |
| Absolute anomaly a = (g − 2)/2 | needs the per-sheet Dirac–Kähler spin account carried onto the candidate tubes and connected to the moment integral |
| The g = 2 Dirac baseline | structural — model-F's per-sheet Dirac–Kähler spin (R62 7d); open only as to its survival in K4 |
| χ derived from a substrate model (rather than fitted) | gated on a grid-substrate chirality model |
| Quark-level → nucleon moment | gated on a composite (bound-state) treatment |

---

## 8. Open questions

1. **Per-sheet spin on the candidate tubes.** The spin account exists — model-F's per-sheet Dirac–Kähler field (R62 7d): spin ½ per 2-torus sheet, every winding. What is open is a clean derivation of the magnetic moment and L = ℏ/2 for that field on the *ellipse* and *clover* tubes ([electron-tube.md](electron-tube.md) notes it is unwritten even for the ellipse), and whether the account survives unchanged in K4.
2. **A substrate-chirality model.** χ is phenomenological until the grid substrate's handedness is modelled from the [grid-primitive](../../grid-primitive/) level.
3. **Relation to leakage.** The anomaly may have a second contribution — *virtual* leakage through shared dims (an excursion that returns), the geometric analog of a radiative correction, using the same junction machinery as decay ([mode-stability.md §4](mode-stability.md)). Whether the intrinsic (shape + χ) account of this file and a leakage account are two effects or one description is itself open.
4. **The charge-sign / anomaly-sign correlation.** If one substrate handedness sets both (§2), the framework predicts a definite correlation — a falsifiable consequence to pin down once the model computes signs.

---

## Cross-references

- [tube-function.md](tube-function.md) — the harmonic cross-section family; ellipse and clover profiles and their curvature
- [scripts/harmonic_tube.py](../scripts/harmonic_tube.py) — the existing cross-section / curvature script the moment calculation would extend
- [electron-tube.md](electron-tube.md) — the ellipse profile and τ = 2 floor; §6 the Williamson & van der Mark spin reading and its (1, 1) failure
- [clover-quarks.md](../../sheet-proton/work/clover-quarks.md) — the clover and the per-arc charges that range its profile
- [mode-stability.md](mode-stability.md) — the leakage machinery a virtual-leakage anomaly would reuse (§4)
- [models/model-F.md](../../../models/model-F.md) — per-sheet Dirac–Kähler spin (R62 7d): the g = 2 baseline, spin ½ from the 2-torus sheet, not the winding ratio
