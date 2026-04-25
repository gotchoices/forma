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

## Track 5 — Two-line nuclear binding model: Ma harmonic stack + S-separation Coulomb

**Status: framed; pending execution.**

A reframed direction following Track 4's structural lesson (the
inventory under R64's pure-p-sheet picture cannot be obtained by
transplanting R63's tuples) and the realization that the Fe peak
in nuclear binding requires a SECOND curve crossing R64's first.

### Premise

The user's observation is that the Fe peak in B/A vs A is the
crossover of two trends:

- **Line 1 (strong, Ma-internal)**: R64's harmonic stack on the
  p-sheet, captured by Point B's chain-fit.  Gives ~constant
  per-nucleon binding 8.6 MeV/A.
- **Line 2 (Coulomb, S-emergent)**: protons separated by spatial
  distance r in S have potential energy `α·ℏc/r`.  This is real
  but expressed in the S frame.  Aggregated over a nucleus with
  Z protons of average S-separation r ≈ r₀·A^(1/3), this gives
  the standard Bethe-Weizsäcker Coulomb term with no manual
  α-scaling needed (α is already in the formula).

Crossing of the two curves at Fe produces the binding peak.
Embracing Coulomb as a real S-energy emerging from Ma charge
geometry is consistent with the "all S-forces are Ma geometry"
premise: the geometric reality of charge IS in Ma, but the
*energy associated with spatial separation* is measured in S.

### Goals

1. **Test if R64-Ma + S-Coulomb produces the Fe peak.**  Compute
   the binding curve under `m_total = m_R64-Ma + E_Coulomb(Z, A)`
   and check whether the resulting B/A predictions reproduce the
   observed rise-and-fall with a peak near Fe.
2. **Refit Point B if needed.**  When Coulomb is added explicitly,
   the chain-fit Point B may no longer be optimal — some of what
   Point B was implicitly fitting may now be Coulomb.  Re-fit
   `(ε_p, s_p)` jointly with Coulomb and report the new working
   point.
3. **Diagnose remaining residuals.**  Even with R64 + Coulomb,
   there may be light-A deviations (the ⁴He over-binding pattern
   from Phase 3e).  Document where the model still misses, in
   what shape.

### Phases

- **Phase 5a — Add Coulomb to R64's mass formula.**  Compute
  `m(Z, A) = m_R64(Z, A) + E_Coulomb(Z, A)` at fixed Point B
  parameters with `a_C = 0.71 MeV` (standard Bethe-Weizsäcker).
  Plot predicted B/A vs A; compare to observation.  Identify Fe
  peak if present.
- **Phase 5b — Re-fit (ε_p, s_p) jointly with Coulomb.**  Sweep
  `(ε_p, s_p)` and re-anchor K_p at each point; minimize global
  residual against `m_observed(Z, A) = m_pred-Ma + E_Coulomb`.
  Report the new optimum and how far it has shifted from Point B.
- **Phase 5c — Light-A diagnostic.**  At the Phase 5b optimum,
  examine the pattern of residuals for A ≤ 12.  If light nuclei
  still over-bind, characterize the shape (which would then be
  attacked in a future track via additional structure).

### Success / failure criteria

- **Success**: R64 + Coulomb produces a B/A curve with a clear
  peak near Fe (within ±10 MeV of observed) and matches the heavy
  chain (Pb, U) within ~5%.
- **Partial**: Fe peak emerges but light-A residuals persist —
  document and queue follow-up.
- **Failure**: no Fe peak emerges, or the chain fit shatters.
  Returns R64 to Track-3-end status; reframing needed.

### Reusable assets

- R64 Track 3 nuclear-chain data (84 stable isotopes, AME2020
  masses).
- R64 Track 1 Phase 1c magic-point search infrastructure (re-anchor
  K_p in Newton iteration).
- Bethe-Weizsäcker Coulomb formula with `a_C = 0.71 MeV` (SM
  standard).

### Outputs

- `outputs/track5_phase5a_coulomb_added.csv`
- `outputs/track5_phase5a_binding_curve.png`
- `outputs/track5_phase5b_joint_refit.csv` (if 5b runs)

---

## Track 7 — Strong force from a 7-tensor: 6 Ma + 1 S spatial dimension

**Status: framed; Phase 7a executing.**

After Track 6's review, the goal of *re-deriving* nuclear shell
structure from MaSt was deemed a structural re-invention of well-
understood SM physics (per
[primers/nuclear-scaling.md](../../primers/nuclear-scaling.md)).
What's *novel* in MaSt — and what would constitute genuine
first-principles work — is deriving the **strong force itself**
(its r-dependent shape and strength) from MaSt's geometric
structure.

The user's framing: build a 7-tensor (the T⁶ Ma block + 1
abstract S spatial dimension), assume Ma couples to S at the
known 1/α magnitude (analogous to how the photon couples
electromagnetism via aleph in the full 11-tensor), and sweep
remaining off-diagonal parameters to see if the natural energy
structure matches the observed nucleon-nucleon potential:

- a hard core (or repulsion) at very small r
- an attractive trough at r ≈ 1 fm with depth ~50 MeV
- a barrier / decay region beyond
- Coulomb tail (`α/r`) at large r

If this shape emerges from the 7-tensor with the standard 1/α
coupling assumption, MaSt would have produced the strong force's
r-dependent profile from geometric consistency rather than as
an empirical input.

### Victory criteria

Track 7 succeeds if the 7-tensor at some parameter point produces:

1. **Energy curve shape** matches the observed strong-force
   profile (trough at ~1 fm, depth ~50 MeV, range ~1.5 fm,
   Coulomb tail at large r).
2. **P-sheet supports both protons and neutrons** (R64's Point B
   already does this; verify it survives the 7-tensor extension).
3. **Shear explains the Fe-peak preference** (light nuclei
   prefer to grow toward heavier; binding-per-nucleon rises with
   A from below Fe).
4. **Marginal-nucleon preference is computable**: at a given
   (Z, N), the 7-tensor predicts whether the next nucleon prefers
   to be a proton or a neutron (matching the valley of stability).

If all four hold simultaneously, declare victory: MaSt has
derived the strong force from first principles plus the standard
α coupling assumption.

### Phases

- **Phase 7a — Minimal 7-tensor sweep.**  Build the 6 Ma + 1 S
  metric using R64 Point B parameters for the Ma block, the
  assumed 1/α magnitude for Ma↔S coupling, and treat any
  remaining off-diagonal terms as free.  Compute the energy of
  a two-particle p-sheet configuration as a function of S
  separation, sweeping the free parameters.  Plot E(r); look
  for the strong-force shape.
- **Phase 7b — Marginal-nucleon test.**  At a chosen working
  point from 7a, compute predicted Z/A optimum vs A across the
  nuclear chain.  Check the four victory criteria.
- **Phase 7c — Refine.**  If 7a/7b are encouraging, refine the
  parameter set and characterize uncertainties.

### Reusable assets

- R64 Point B Ma metric parameters
- R60 11D metric construction (for off-diagonal structure
  reference)
- α = 1/137.036 as an input (per GRID)
- Track 3's nuclear chain (84 stable isotopes) as the comparison
  data

---

## Track 6 — Flexible slot-configuration tool for shell-structure hypotheses

**Status: Phase 6a complete; Track PAUSED.**

Track 6 (revised after the previous mass-ordering iteration was
abandoned per user direction) builds a computational tool for
testing nuclear-shell-structure hypotheses against observed
nuclear physics, with no commitment to a specific MaSt
interpretation.  Each hypothesis is a **slot configuration**:
which (n_t, n_r) primitives serve as slots, the order in which
slots fill, the per-slot capacity per isospin, and any optional
additions (Coulomb, surface, shell-closure bonuses).  The tool
reports magic-A alignment, binding-curve fitness, and valley-of-
stability prediction.

Working under interpretation B3: each slot holds nucleons of one
isospin (proton or neutron, not mixed), with Pauli capacity 2 per
slot.  Magic numbers are per-isospin.

**Phase 6a tested three baseline hypotheses**:
- H1 (mass-ordered, no Coulomb): bulk binding curve fits 18%
  mean error but **valley wrong direction** (predicts proton-rich
  heavy nuclei).
- H2 (+ Coulomb): valley **correct direction** (Z/A drops from
  0.50 to 0.29 with A) but Coulomb double-counts at Point B,
  binding magnitude breaks (mean error 42%).
- H4 (+ shell-closure bonuses): bonuses are subleading; doesn't
  produce Fe peak.

**Key Phase 6a findings**:
- Tool framework is operational.
- Adding S-Coulomb gives the right valley direction; need joint
  refit to fix magnitude (= Track 5 Point C).
- Shell-closure bonuses are subleading to bulk binding.
- Fe peak still not produced under any tested hypothesis (surface
  is missing).

See [findings-6.md](findings-6.md).

**Phase 6b candidates**: refit Point B → Point C with explicit
Coulomb in the tool's mass evaluation; test (1, ±1) exclusion
per user hint; test SOC nuclear-shell-model sequence as a
user-provided slot ordering; add surface term and check if Fe
peak emerges.  All directly supported by the tool.

---

## Track pool (after Track 6)

Items lettered for flexible selection.  Obsolete pool items
removed; remaining items in priority order.

**a. Light-A deviation diagnosis.**  Even with Coulomb added,
R64 may over-bind light nuclei (⁴He at 22%, ¹²C at 13% in Track
3 Phase 3e).  Investigate whether this is finite-stack effect
(the additive harmonic-stack rule needs corrections for small
A), surface effect (boundary nucleons have fewer neighbors),
or another mechanism.  The deuteron is the central case.

**b. Quantum-number decoding (Ma analogs of n, l, m_l, m_s).**
Identify the Ma winding/orientation feature for each atomic
quantum number.  Provisional mapping:
- n ↔ harmonic level (rung on the (n_t, n_r) lattice)
- l ↔ phase separation (relative phases of strands)
- m_l ↔ orientation (direction of angular structure)
- m_s ↔ ring-winding polarity (sign of n_r component)
Test against electron 1s, 2s, 2p quantum-state predictions.
Deliverable: complete Ma-side label for each electron shell
state.

**c. Electron-shell harmonic structure on the e-sheet.**  Apply
pool-b's quantum-number decoding to predict observed atomic
shell energies.  Find `(ε_e, s_e, K_e)` working point that
reproduces 1s, 2s, 2p, 3s, 3p, 3d energies for hydrogen and
multi-electron atoms; check periodic-table grouping; check
Pauli-saturation counts.

**d. Nuclear shell structure and magic numbers.**  Apply pool-b's
decoding to the p-sheet for nucleons.  Test:
- Magic numbers (2, 8, 20, 28, 50, 82, 126) as nuclear shell
  closures
- Specific stability of doubly-magic nuclei (⁴He, ¹⁶O, ⁴⁰Ca,
  ⁵⁶Ni, ¹³²Sn, ²⁰⁸Pb)
- Pairing energy from m_s polarity considerations

**e. Higher-generation quark identification.**  After mode-stacking
is understood (pool-b through pool-d), search for s/c/b/t
primitives within the unified Ma quantum-number framework.
Higher generations may correspond to specific (n, l) combinations
on the p-sheet, or cross-sheet structure, or both.  *Earlier
attempts (Track 2 Phase 2a, Track 4) tried this without
quantum-number decoding and found structural problems; not
repeated until pool-b lands.*

**f. Full hadron inventory under unified framework.**  Once
quark generations are identified, predict mesons (q-q̄) and
hyperons (qqq with at least one s/c/b/t) via the unified Ma
quantum-number rules.  Replaces R63's empirically-fit
inventory tuples with derived predictions.

**g. Charge-attribution rule extension.**  R64 currently uses a
provisional rule (u = +2/3, d = −1/3 from sign of n_pr).  This
needs derivation from a refined Q132 rule in light of the
quantum-number framework.

**h. Z = 137 impedance-overflow audit.**  Deferred.  Once
nuclear physics is settled, asking what happens at Z ≈ 137 is
the natural next limit test.

**i. Synthesis & promotion to model-G.**  Combine all completed
tracks.  Assess whether R64-extended is decisively better than
R63's framework across the full observable set: nuclear binding,
nuclear stability, hadron inventory, electron shells.  Recommend
promotion if criteria are met.

### Obsolete (kept for historical record, not pursued)

- ~~Inventory re-derivation under flavor-aware composition only on
  p-sheet~~ — found structurally incompatible with SM isospin
  near-symmetry (Track 4 Phase 4a).
- ~~Hybrid inventory using R63 tuples at R64 parameters~~ — found
  to mix incompatible frameworks (Track 5 Phase 5a as originally
  scoped, now superseded).
- ~~S-stability tooling as separate prerequisite~~ — superseded by
  Line 2 (S-Coulomb directly added to budget).

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
