# R64: Nuclear structure as a harmonic stack on the p-sheet

**Premise.** All forces in spacetime (S) are geometric realities in
the compact manifold (Ma).  The strong force is the outstanding
gap.  R63 falsified six Ma-internal binding mechanisms within the
existing single-primitive p-sheet picture (cross-shear dressing,
non-additive tuples, high-n mass corrections, Pauli phase coherence,
Slater-determinant exchange, complementary-shear compound, and
curved-donut geometry).  All six tests assumed:
- The neutron lives across all three sheets `(1, 2, −1, −1, 3, 6)`.
- The proton's three p-sheet quark strands are identical `(1, 2)`
  primitives.

R64 flips both assumptions.  The new working hypothesis:

> **Nuclear structure is a harmonic stack of u/d quark primitives
> living entirely on the p-sheet, with the shear `s_p` creating
> the proton/neutron asymmetry.**

The **u quark** is the `(1, +2)` p-sheet primitive; the **d quark**
is the `(1, −2)` primitive.  Their masses differ by the shear's
interaction with the ring direction.  Z₃ confinement (R60 T16) is
preserved automatically: every baryon is `(3·k, ...)` after additive
composition, regardless of the u/d mix.

Under this hypothesis:
- **Proton (uud)** → `(1+1+1, +2+2−2)` = `(3, +2)` on p-sheet.
- **Neutron (udd)** → `(1+1+1, +2−2−2)` = `(3, −2)` on p-sheet.
- **Deuteron (uud + udd)** → `(6, 0)` on p-sheet.
- **Heavier nuclei** stack as `(3·A, k_p · 2 − k_n · 2)` with
  `k_p + k_n = A` and `k_p = Z`.

The cross-sheet neutron is what the on-sheet neutron *degenerates
to* via β decay (the `(3, −2)` mode releasing a `(1, 2)` lepton
plus an antineutrino, leaving a proton at `(3, +2)`) — not a
fundamental representation.

R64's job is to test this picture and develop it into a working
nuclear model if it survives.

---

## Mission

Test whether a single `(ε_p, s_p)` parameter point hosts:

1. The **proton** at `(3, +2)` with mass 938.272 MeV.
2. The **neutron** at `(3, −2)` with mass 939.565 MeV (slightly
   heavier; close to but not exactly stable in isolation).
3. The **rest of the hadron inventory** (mesons, hyperons) within
   model-F's accuracy when re-derived under flavor-aware u/d
   composition.
4. **Light nuclei** (²H, ³He, ⁴He, ⁶Li, ¹²C) as additive harmonic
   stacks at the matching mass.
5. **The Fe region** (⁵⁶Fe ≈ 52,103 MeV) as the upper validation
   target before considering heavier nuclei.

The shear `s_p` is the structural asymmetry between (n_pt = 3,
n_pr = +2) and (n_pt = 3, n_pr = −2).  R64's central question is
whether *any* `(ε_p, s_p)` exists that delivers the observed
proton/neutron mass split, and if so, whether the same point
preserves the inventory and predicts the harmonic stack
correctly.

---

## How R64 differs from R63

| Aspect | R63 | R64 |
|:---|:---|:---|
| Goal | Refine model-F (the g-candidate) | Test a different model (h-candidate) |
| Neutron | Cross-sheet `(1, 2, −1, −1, 3, 6)` | On-sheet `(0, 0, 0, 0, 3, −2)` |
| Quarks | Single primitive `(1, 2)` | Two primitives: u = `(1, 2)`, d = `(1, −2)` |
| Binding | Inherited from compound-mode mass formula | Inherited from harmonic-stack additive rule |
| Inventory pinning | Anchored on electron + proton | Anchored on proton + neutron mass split |
| Discipline rule | "No observable-anchored sweeps" | Observable-anchored sweep IS the search |

R63 closes cleanly at its current state.  Its findings stay valid
as findings *about the cross-sheet model* (model-F / g-candidate);
they document what doesn't deliver binding under those assumptions.
R64 picks up with an explicit alternative.

---

## Discipline constraints (R64-specific)

1. **Observable anchoring is allowed** for the proton/neutron mass
   pair specifically — that's the search's premise.
2. **Inventory preservation is the hard gate.**  The magic
   `(ε_p, s_p)` must keep the 13-particle hadron inventory within
   5% (model-F precision baseline) under flavor-aware u/d
   composition.  If it doesn't, R64 closes.
3. **Z₃ confinement (R60 T16) is retained as default.**  Only
   re-evaluated if a specific test exposes a structural conflict.
4. **S-stability is hypothesized, not computed.**  Where the
   theory says "the neutron is unstable in isolation but stable
   inside a nucleus," that's a hypothesis.  We assume the energetic
   preferences without quantifying Ma-vs-S thresholds; tooling for
   that is deferred.
5. **Heavy-nucleus instability (Z = 137) is deferred.**  R64
   focuses on H → Fe; the impedance-overflow argument for Z > 137
   is interesting but not part of this study's sharp targets.
6. **Higher-generation quarks (s, c, b, t) are pool items.**  If
   the magic point delivers, the SM's flavor structure should
   extend naturally to other primitive classes.  Validating this
   is success's expected next phase.

---

## Track 1 — Locate the magic `(ε_p, s_p)` point for proton/neutron

**Goal.**  Find `(ε_p, s_p)` such that the closed-form mass formula

<!-- μ²(n_t, n_r) = (n_t/ε)² + (n_r − s·n_t)² -->
$$
\mu^2(n_t, n_r) \;=\; \left(\frac{n_t}{\varepsilon}\right)^2
                  + (n_r - s\,n_t)^2
$$

at `(3, +2)` and `(3, −2)` reproduces the proton and neutron masses
observed in nature, with appropriate calibration of the overall mass
scale `K_p`.

**Single-number target.**  Define the **mass ratio**

<!-- R(ε, s) = μ(3, -2) / μ(3, +2) -->
$$
R(\varepsilon, s) \;=\; \frac{\mu(3, -2)}{\mu(3, +2)}
                    \;=\; \sqrt{\frac{(3/\varepsilon)^2 + (-2 - 3s)^2}{(3/\varepsilon)^2 + (+2 - 3s)^2}}.
$$

Observed: `m_n / m_p = 939.565 / 938.272 = 1.001378`.

We want R(ε, s) = 1.001378 (to within ~10⁻⁵ for sharp pinning).

**Strategy.**

- **Phase 1a — Closed-form sweep.**  R(ε, s) is analytic.  At fixed
  ε, expand R as a function of s and solve `R(ε, s) = 1.001378` for
  s as a function of ε.  This gives a 1-D **viable curve** in the
  (ε, s) plane: the locus of points where the proton/neutron mass
  ratio lands on observation.  The curve is universal — it doesn't
  depend on K_p anchoring.
- **Phase 1b — Mass-scale anchoring.**  Along the viable curve,
  anchor K_p so `K_p · μ(3, +2) = 938.272`.  Compute `m_n =
  K_p · μ(3, −2)` and verify it matches 939.565 (it must, by
  construction).  Tabulate K_p along the curve.
- **Phase 1c — Inventory survival check.**  Pick a few
  representative points on the curve.  At each, re-render the
  13-particle hadron inventory under flavor-aware u/d composition
  and check whether it lands within 5% per particle.  This narrows
  the viable curve to a viable *region* (or eliminates it
  entirely).
- **Phase 1d — Light-nuclei stack check.**  At each surviving
  point, compute the additive-stack masses for ²H, ³He, ⁴He under
  flavor-aware composition and check against observed.

**Success criterion.**  At least one `(ε_p, s_p)` point exists
where the mass ratio matches observation, the inventory stays
within 5%, and the light-nuclei stack lands within ~10% (a coarse
gate; binding is a separate question).

**Failure criterion.**  No `(ε_p, s_p)` on the viable curve passes
the inventory gate, OR the K_p anchor falls outside model-F's
range by more than 2× (suggesting the framework's mass-scale
constants don't admit this picture).

**Outcome.**  If success: R64 is greenlit; immediately build a
Q file capturing the working theory and provisional ground rules.
If failure: R64 closes; the harmonic-stack picture doesn't admit
even the simplest test.

**Reusable assets**:
- R63 Track 5/6 inventory tuples (re-interpreted under u/d
  composition).
- R60 / model-F mass-scale constants (`K_MODELF` from
  `track15_phase1_mass`).
- Closed-form mass formula from R62 derivation 4.

**Output**:
- `outputs/track1_viable_curve.csv` — `(ε_p, s_p, K_p)` along the
  proton/neutron mass-ratio curve.
- `outputs/track1_inventory_check.csv` — inventory predictions at
  candidate points.
- `outputs/track1_light_nuclei.csv` — H, ²H, ³He, ⁴He, etc.
- `outputs/track1_viable_curve.png` — visualization.

See [findings-1.md](findings-1.md) for results.

---

## Track 2 — Quark generation primitive identification

**Status: framed; pending execution.**

Track 1 landed positive on the foundational test: the magic point
`(ε_p, s_p) = (0.07309, 0.19387)` reproduces the proton, neutron,
and deuteron masses simultaneously with constituent m_u = 315 MeV.
Track 2 tests whether the same magic point hosts the **other five
quark types** (d, s, c, b, t — d already lands as the (1, −2)
ring-flip partner of u) as primitive classes on the p-sheet
lattice.

### Strategic rationale

In the SM, all hadrons are quark composites: mesons are q-q̄ pairs,
baryons are qqq triplets.  If MaSt's primitive lattice contains
the full 6-quark family at the magic point, every meson and
baryon becomes a *prediction* rather than a fit.  This is more
parsimonious than an inventory-by-particle audit (which would
require 13 separate fits and a working composition rule
simultaneously).

### Phases

- **2a — Strange quark.** Scan the Z₃-compatible primitive lattice
  for the class whose mass at the magic point matches m_s ≈ 510
  MeV (constituent).  Cleanest single-quark observable: **Ω⁻
  (sss)** at 1672 MeV — no u/d contamination, gives m_s = 557 MeV
  from the additive triplet.  Cross-check against kaons (us̄),
  Λ (uds), Σ (uus, dds), Ξ (uss, dss).  Charge attribution under
  the provisional R64 rule (sign of n_pr distinguishes +2/3 from
  −1/3) needs verification at strangeness.
- **2b — Charm quark.** Target m_c ≈ 1500 MeV.  Cleanest target:
  **J/ψ (cc̄)** at 3097 MeV → m_c ≈ 1549 MeV.  Test against D
  mesons (cū, cd̄, cs̄), Λ_c (udc).
- **2c — Bottom quark.** Target m_b ≈ 4700 MeV.  Cleanest target:
  **ϒ (bb̄)** at 9460 MeV → m_b ≈ 4730 MeV.  Test against B mesons.
- **2d — Top quark.** Target m_t ≈ 173,000 MeV (current ≈
  constituent because QCD effects negligible at top scale).
  Sparse hadron spectroscopy at this scale; the t identification
  is mostly structural (which primitive class hosts it) rather
  than empirically tested.
- **2e — Generation structure.** If 2a–2d each find a clean
  primitive, examine whether (u, c, t) and (d, s, b) form a
  structured family on the p-sheet lattice.  A natural progression
  (e.g., (1, ±2) → (2, ±n) → (3, ±n)) would predict the SM's
  3-generation structure as a consequence of p-sheet harmonics
  rather than an empirical input.

### Goal

A 6-quark family on the p-sheet, all at the magic point
`(ε_p, s_p, K_p) = (0.07309, 0.19387, 22.847)`, each matching its
observed constituent mass to within 5%.  Mesons and baryons
predicted from this family without further parameters.

### Success / failure criteria

- **Success**: 5 primitive classes (d already done as Track 1's
  ring-flip; s, c, b, t to be found) each within 5% of observed
  constituent mass.  Generation structure (Phase 2e) shows a
  clean progression on the lattice.
- **Failure**: no primitive class delivers s within 5% of 510 MeV,
  OR found primitives don't form a structured family.  R64
  closes if 2a fails decisively; structural reframing if 2a
  passes but 2e doesn't.

---

## Track pool (after Track 2)

Track 1 closed the foundational viability test.  Track 2 starts
the quark generation identification.  Other pool items remain.

**a. Inventory re-derivation under flavor-aware composition.**
After Track 2 identifies all 6 quarks, every meson and baryon
becomes a mechanical prediction.  This pool item is then a
*verification* of the predictions, not a fit.

**b. Light-nuclei harmonic stack quantitative.**  ²H, ³He,
⁴He, ⁶Li, ⁷Li, ⁹Be, ¹²C — masses, charges, magnetic moments
where Ma admits them.  Check against observed binding energies
*as predictions of the additive-stack mass formula*, not as a
constraint on the search.

**c. Mid-chain through Fe.**  ¹⁶O, ²⁴Mg, ²⁸Si, ³²S, ⁴⁰Ca,
⁵⁶Fe.  Validates that the harmonic stack scales correctly into
the heavy-binding regime.  ⁵⁶Fe is the most-bound nucleus per
nucleon and an obvious benchmark.

**d. Higher-generation quarks (strange, charm, bottom, top).**
Identify the p-sheet primitive class that hosts each generation.
Candidates: `(2, ±1)`, `(1, ±3)`, `(2, ±3)`, ... .  Each
generation should be a distinct primitive class on the p-sheet
(or possibly a dressed mode involving multiple sheets — to be
determined).

**e. Hyperon and meson re-derivation.**  Λ, Σ, Ξ, Ω as multi-
generation baryons (uds, dds, ssd, ...).  K, η, η′, φ as quark-
antiquark mesons.

**f. New-particle predictions.**  The harmonic stack predicts
specific compound modes that should exist.  Cross-check against
the SM's known particle list to identify novel predictions.

**g. Charge-attribution rule extension.**  Q132 v2 doesn't
currently distinguish (1, +2) from (1, −2) charges.  R64 needs
the rule extended — the natural form is that the sign of n_r at
the primitive level distinguishes +2/3 from −1/3 fractional
charge.  Derivation work is required.

**h. Electron-shell harmonic stack on the e-sheet.**  Optional —
could be a separate study (R65) or a Track of R64 if the p-sheet
work goes smoothly.  Test whether 1s, 2s, 2p, 3s, 3p, 3d levels
appear as harmonic modes on the e-sheet at appropriate `(ε_e,
s_e)`.

**i. Z = 137 impedance-overflow audit.**  Deferred.  Once
H → Fe works, asking what happens at Z ≈ 137 is the natural
next limit-test.  But the energetic argument (137 protons in Ma
exceeds 1 proton's S-energy) is qualitative for now.

**j. S-stability tooling.**  Deferred.  Required to *quantify*
when an Ma harmonic-stack compound is preferred over spatial
separation in S.  Currently we hypothesize preferences without
calculation.

**z. Closeout.**  After at least Tracks a, b, c run successfully:
recommend a **model-H** designation if the harmonic-stack picture
delivers across the H → Fe range.  If only Track 1 lands but the
inventory or light-nuclei break, closeout reports the magic
point as a structural curiosity without promoting to a model.

---

## Status

**Tracks 1, 2 (Phase 2a), 3 complete.**  Two distinct candidate
working points are now on the table within R64; both are
**explicitly provisional** — neither is yet a hard pin.

**Point A — magic point** (Track 1, deuteron-anchored):
- `(ε_p, s_p, K_p) = (0.07309, 0.19387, 22.847 MeV/μ)`
- Reproduces m_u, m_n−m_p, B(²H) within ~0.1% (anchor).
- **Heavy-nucleus binding under-predicts by ~7×** (Phase 3a).
- Strange quark search at this point (Phase 2a) gave
  structural problems (Σ off by 9–15%, K⁰ off by 17%).

**Point B — chain-fit point** (Track 3, body-of-chart-anchored):
- `(ε_p, s_p, K_p) = (0.2052, +0.0250, 63.629 MeV/μ)`
- m_u = 335 MeV, m_d = 336 MeV (matches SM constituent value).
- **Body of nuclear chart (Ca through Sn) fits within 1–2%**;
  ⁵⁶Fe within 2%, ¹²⁰Sn within 1%.
- **Deuteron is an outlier**: predicted B(²H) = 17 vs observed
  2.2 MeV.

The chain-fit Point B is the current preferred candidate, BUT
the deuteron's outlier status and the need to revalidate the
hadron inventory at the new point keep it provisional.  Lesson
from Track 3: don't pin too quickly to a single observable.

Working theory captured in
[Q134](../../qa/Q134-nuclear-harmonic-stack-on-p-sheet.md) (R64's
g-candidate, parallel to R63's g-candidate).

**Track 4 active — inventory audit at Point B.**  Hard gate
before Point B is treated as a pin.

R63 closed cleanly with respect to nuclear binding under the
cross-sheet model.  Its g-candidate findings remain valid for
that representation; R64 tests the alternative on-sheet
representation.  R63 and R64 are parallel candidates for
becoming model-G; promotion is deferred until one (or
neither) demonstrates clear superiority across multiple
criteria.
