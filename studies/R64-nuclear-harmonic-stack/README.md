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

**Quick reference:**
- [`metric-terms.md`](metric-terms.md) — every entry in the 11×11
  metric: pinned/free/derived flags, current values, source.
  CSV form: [`metric-terms.csv`](metric-terms.csv).
- [`zoo.md`](zoo.md) — particle inventory match table (mass and
  α-attribution status for every entry).
- [`findings-11.md`](findings-11.md) — Track 11: strong force
  rescued in the metric.

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

**Status: Phases 7a, 7b, 7c, 7d, 7e, 7f, 7g, 7h complete.**

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

### Phase summary

- **Phase 7a — Minimal 7-tensor sweep.**  Done.  Trough
  emerges at the right shape but ~5× too shallow with the
  natural `A = (ℏc)²` kinetic coefficient.  Charge-independence
  forces σ_r = 0 structurally; pn deeper than pp by ~17 MeV
  from the Ma-side at Point B.
- **Phase 7b — Yukawa fit.**  Done.  V(r) is essentially exact
  polynomial `A₂/r² + A₁/r` (R² = 0.9998).  Yukawa exponential
  cannot emerge from the metric-coupling formalism — that
  requires propagator physics (queued as pool item m).
- **Phase 7c — Two-body kinematic correction.**  Done.  k_S =
  1/r is the *relative* momentum of two nucleons in COM frame,
  so `A = 4·(ℏc)²` (relativistic two-body invariant-mass
  relation).  With the fix, pn trough lands at r = 1.135 fm
  with depth −50.2 MeV — inside the observed NN-potential band
  (40–60 MeV).  σ_t = −116.1 sits as MaSt's α_s analog
  (no clean structural relation to α, ε_p, s_p, K_p).
  See [findings-7.md](findings-7.md).

**Net at 7c:** the 7-tensor at R64 Point B with corrected
two-body kinematics produces strong-force *shape* and *scale*
at intermediate r from one empirical cross-shear σ_t.  The
polynomial form (vs Yukawa) is a known limitation at large r.

### Phase 7d — Schrödinger validation of V(r)

**Status: complete.  Result: V(r) fails QM observables decisively
— polynomial 1/r tail dominates.**

Phase 7c's V(r) reproduces the static NN-potential trough.
Phase 7d tests whether the same V(r) gives the right
**quantum-mechanical observables** when solved as a Schrödinger
two-body problem.

**Goal.**  Compute, from V(r) at Phase 7c parameters:

| Observable | Channel | Observed |
|:---|:---|:-:|
| Deuteron binding energy B(²H) | pn S-wave (³S₁) | 2.224 MeV |
| Triplet scattering length a_t | pn S-wave (³S₁) | +5.42 fm |
| Singlet scattering length a_s | NN S-wave (¹S₀) | −23.7 fm |

If V(r) reproduces these to ~10–20%, Track 7's claim upgrades
from "shape and scale match" to "shape, scale, and bound-state
+ scattering data match" — much stronger.  In particular, B(²H)
agreement would resolve R64's standing deuteron outlier
(Point B's m(6, 0) over-binds by 15 MeV at the *Ma-side
algebraic* level; the Schrödinger ground state of V(r) is a
*different* prediction and may land closer).

**Strategy.**  Solve the radial Schrödinger equation with the
reduced-mass Hamiltonian:

<!-- −ℏ²/(2μ) ∇² ψ + V(r) ψ = E ψ -->
$$
-\frac{\hbar^2}{2\mu}\nabla^2\psi + V(r)\,\psi = E\,\psi
$$

with `μ = m_p/2` (equal-mass nucleon reduced mass), `V(r) =
A₂/r² + A₁/r` (+ Coulomb for pp), and the boundary conditions
appropriate for bound states (decay at infinity, regular at
origin) or scattering states (free-wave asymptotic).

**Tactics.**

- Implement a numerical radial-equation solver (Numerov method
  or scipy.integrate) — no existing solver in studies/lib.
- Compute B(²H) as the lowest E < 0 eigenvalue in the pn
  channel with V(r) at Phase 7c σ_t = −116.1.
- Compute a_t and a_s by integrating to large r and matching
  the asymptotic phase-shift form `r·u(r) → sin(kr + δ)`,
  taking k → 0 limit for scattering length.
- Repeat for pp (with Coulomb) — predict zero-energy resonance
  structure if any.

**Result summary.** All five acceptance criteria failed except
a_t (right sign, order of magnitude OK).  The polynomial 1/r
tail produces a Coulomb-like Rydberg series of bound states
(3 states each in pn, nn, pp channels) with effective coupling
~0.37 (50× α).  Total B(²H) = 30 MeV vs observed 2.22 MeV
(factor 13.5 off).  See findings-7.md F7d.1–F7d.7 for full
analysis.

**Verdict.** Phase 7c V(r) gives the right *static* trough but
fails *quantum-mechanical* observables.  σ_t cannot be retuned
to fix this — it's the functional form (polynomial vs Yukawa)
that's wrong.  Pool item m (propagator-based Yukawa extension)
is the natural next step.

**Outputs.**

- [`outputs/track7_phase7d_results.csv`](outputs/track7_phase7d_results.csv)
- [`outputs/track7_phase7d_potential_and_wavefunctions.png`](outputs/track7_phase7d_potential_and_wavefunctions.png)
- [findings-7.md](findings-7.md) F7d section updated with full results.

### Reusable assets

- R64 Point B Ma metric parameters
- R60 11D metric construction (for off-diagonal structure
  reference)
- α = 1/137.036 as an input (per GRID)
- Track 3's nuclear chain (84 stable isotopes) as the comparison
  data

---

## Track 8 — Hub-and-spoke test: aleph-spatial coupling for the strong force

**Status: Phases 8a, 8b, 8c complete.  See [findings-8.md](findings-8.md).**

**Net result:** Hub-and-spoke architecture confirmed for the
metric.  σ_aS at α-magnitude completes EM with the magnetic
vector potential.  Strong force does NOT live in the metric —
pivots to propagator-based formalism (pool item m).  Phase 8d
(Schrödinger) not needed — there's no candidate V(r) to
validate.

**Premise** (from [Q135](../../qa/Q135-aleph-as-common-mediator.md)).
The metric's existing structure — sheets coupled to aleph, aleph
coupled to time, no direct cross-sheet entries, EM emergent at α —
suggests aleph is the universal mediator of inter-coordinate
coupling.  Phase 7c's empirical σ_pS_tube (direct p-sheet → S
spatial) bypasses aleph and was shown by Phase 7e to perturb α
universality.  An alternative architectural choice: **the strong
force is also aleph-mediated**, via a new `σ_aS` entry (aleph ↔
S spatial) that R60 has at zero by default and that has not been
tested.

If σ_aS produces the strong-force trough AND preserves α
universality, the metric architecture simplifies significantly:
no direct cross-coordinate entries are needed; aleph mediates
everything.

### Goal

Test numerically whether `σ_aS` (placed at G[ℵ, S_x], G[ℵ, S_y],
G[ℵ, S_z], symmetrically) can:

1. Preserve α universality across the model-F inventory (the
   gating constraint from Phase 7e).
2. Produce a non-trivial NN potential `V(r)` with a trough at
   intermediate r, via the aleph-mediated path:

   `p-tube ─[σ_ta]→ aleph ─[σ_aS]→ S spatial`

3. Match Phase 7c's depth and position (~50 MeV at ~1 fm) at
   *some* value of σ_aS, ideally with a structurally-motivated
   magnitude (analogous to σ_ra's `(s·ε)·σ_ta` derivation).

### Strategy

The aleph-mediated coupling for two p-tube nucleons:

- Single-particle: charge `Q ∝ σ_ta · σ_at` (R62 D5, unchanged).
  σ_aS doesn't enter at single-particle level *if* the
  Schur-complement structure separates the time and spatial S
  coordinates.  This is testable.
- Two-particle: the cross-coupling between two p-tube modes via
  aleph and S spatial introduces an effective `σ_ta · σ_aS`
  coupling at second order.  This is the candidate strong-force
  channel.

### Phases

**Phase 8a — Single-knob test: σ_aS sweep at fixed σ_at = 4πα.**

1. Build augmented metric: R60 model-F baseline + σ_aS at
   G[ℵ, S_x], G[ℵ, S_y], G[ℵ, S_z] symmetrically; σ_at held at
   model-F value 4πα.
2. Sweep σ_aS over its signature-preserving range.
3. Compute α_Coulomb across the same 10 model-F inventory modes
   used in Phase 7e.
4. Check if α stays at baseline value (within 10⁻⁶) for any
   non-trivial σ_aS.

**Decisive criterion**: if α-universality holds for σ_aS ≠ 0
with σ_at fixed, sectors are fully decoupled at the simple level
(case A in the table below) and 8b can be skipped.  If 8a fails,
proceed to 8b.

**Phase 8b — Joint (σ_aS, σ_at) universality search.**

If 8a fails — that is, σ_aS at fixed σ_at perturbs α — then σ_at
might compensate jointly.  This is structurally analogous to how
R60 T7 derived σ_ra = (s·ε)·σ_ta as a constraint between aleph-row
entries that preserves universality, rather than independent free
knobs.

1. 2D grid sweep over (σ_aS, σ_at).
2. At each grid point, build augmented metric, check signature,
   compute α_Coulomb across the 10 inventory modes.
3. Score: max relative deviation of α/α(σ=0, σ_at=4πα) across modes.
4. Identify whether a 1D locus exists where universality holds
   (max deviation < 10⁻⁶), and what shape it takes.

**Decisive cases:**

| 8b outcome | Reading |
|:---|:---|
| Locus exists as scalar `σ_at = f(σ_aS)`, extends to large σ_aS | Hub-and-spoke holds with structural constraint between aleph-row entries; large σ_aS is admissible along the locus |
| Locus exists only near σ_aS ≈ 0 (α-magnitude) | Hub-and-spoke for magnetic vector potential only; strong force lives elsewhere |
| No locus for any σ_aS ≠ 0 | σ_aS needs *per-sheet* structure (analog of σ_ra's `(s·ε)` factor); requires Phase 8b' (per-sheet σ_aS variants) — captured as a follow-on item if reached |

**Phase 8c — Compute V(r) under aleph-mediated coupling.**

If 8a or 8b identifies an α-preserving σ_aS regime:

1. At the working point (or along the universality locus from 8b),
   derive V(r) for two-nucleon compounds (pp, pn, nn) following
   Phase 7c's machinery but with the cross-coupling computed from
   the augmented 11D metric's Schur decomposition rather than
   direct p-S.
2. Find σ_aS value(s) producing a trough at r ≈ 1 fm with depth
   in the 40–60 MeV range.
3. Check pn vs pp preference (still expected from Ma side).
4. Compare to Phase 7c's σ_t = −116.1 result.  If σ_aS lands at
   a structurally-natural value (e.g., σ_aS = √α, or some
   α-derived magnitude), hub-and-spoke is *strongly supported*.
   If σ_aS needs to be empirically large like σ_pS_tube did,
   the architectural choice is neutral on physics but cleaner
   structurally.

**Phase 8d (optional) — Schrödinger validation.**

If 8c lands a viable V(r), repeat Phase 7d's Schrödinger
calculation with the new V(r).  Same diagnostic as before: B(²H),
a_t, a_s.  The polynomial-vs-Yukawa concern from 7d may persist
or may not, depending on whether the aleph-mediated form differs
from the direct-coupling polynomial form.

### Success / failure criteria

| Outcome | Interpretation |
|:---|:---|
| 8a passes (σ_aS preserves α at fixed σ_at = 4πα) AND 8c produces trough at strong-force magnitude | **Hub-and-spoke confirmed for both EM and strong, sectors fully decoupled.**  Strong force is aleph-mediated at large σ_aS.  Cross-sheet entries truly zero by structure. |
| 8a fails, 8b finds a (σ_aS, σ_at) universality locus extending to large σ_aS, AND 8c produces trough along the locus | **Hub-and-spoke confirmed with structural constraint** between aleph-row entries (analog of σ_ra prescription).  Strong force aleph-mediated under joint constraint. |
| 8a or 8b passes, 8c doesn't produce trough at any σ_aS magnitude | **Hub-and-spoke confirmed for EM only.**  Aleph mediation is consistent with EM but cannot carry the strong sector at the metric level.  Strong force pivots to propagator-based formalism (pool **m** Route B). |
| 8a fails AND 8b finds no universality locus | Hub-and-spoke needs *per-sheet* refinement of σ_aS, OR aleph-S coupling is structurally forbidden.  R64 Phase 7e's framing of the strong-coupling-must-have-structure question generalizes to σ_aS with sheet structure. |
| **8b's universality locus exists only near σ_aS ≈ 0 (α-magnitude) AND no strong trough emerges at any σ_aS magnitude** | **Cleanest architectural outcome.**  Aleph mediates EM completely (both time-component Coulomb via σ_at and spatial-component magnetic via σ_aS at α-magnitude).  Strong force is structurally NOT a metric off-diagonal — it requires propagator physics (massive mediator, Yukawa).  This reading is consistent with Phase 7b's proof that pure-metric formalisms can't produce Yukawa form, and with Phase 7d's polynomial-form pathology.  Forces R64 to pivot strong-force formalism to pool **m** Route B (propagator-based), but completes EM with the magnetic vector potential MaSt was structurally missing. |

### Reusable assets

- R60's `build_aug_metric` (the model-F baseline) — already exists.
- Phase 7e's α-universality test infrastructure — already exists,
  modify to add σ_aS instead of σ_pS_tube.
- Phase 7c's V(r) extraction — needs adaptation to compute via
  aleph-mediated path rather than direct sheet-S.

### Outputs

- `outputs/track8_phase8a_alpha_universality.csv` — σ_aS sweep
  at fixed σ_at, α/α₀ across modes.
- `outputs/track8_phase8b_joint_universality.png` — 2D heatmap
  of universality deviation in (σ_aS, σ_at) plane; identified
  universality locus.
- `outputs/track8_phase8c_potential_curves.png` — V(r) for pp,
  pn, nn at the α-preserving σ_aS (or along the 8b locus).
- `findings-8.md` — full Phase 8a–8d writeup.

### Why this matters for R64 and R62

Phase 8 is small (single-script extension of 7e infrastructure)
and decisive (gates the architectural choice between hub-and-spoke
and direct-cross-coordinate prescriptions).  Running it before
either Yukawa pivot (7c pool **m**) or σ_pS_tube structural
prescription (7c pool **j**) prevents committing months of work
to either route until the architectural choice is settled.

If hub-and-spoke is supported, the R62 derivation roadmap
(`STATUS.md`) collapses meaningfully: cross-sheet σ entries
become zero by structure (Obstacle 1 closed), strong-force
coupling becomes σ_aS derivation (Obstacle 2 simplified), aleph
existence becomes mandatory (Obstacle 3 closed).  The architectural
simplification flows back into the broader derivation program.

---

## Track 9 — σ_pS structural-prescription search via universality constraint

**Status: framed; pending execution.**

**Premise.**  Phase 7e showed that a *single-parameter* σ_pS_tube
addition to the metric perturbs α universality mode-dependently.
Phase 8c showed that aleph-mediated σ_aS produces an α-suppressed
effective coupling too weak for the strong force.  Both are
honest negative results within their narrow scopes — but neither
exhausts the question of whether a **structurally prescribed**
direct sheet-S coupling can preserve α while delivering
strong-force-magnitude effective coupling.

R60 T7 set the precedent: σ_ra (ring↔aleph) appeared to break α
universality at first.  Solving the universality constraint
algebraically gave the structural prescription
**σ_ra = (s · ε) · σ_ta** — and at that prescription α stayed
universal.  The same machinery, applied to σ_pS, may or may not
admit an analogous prescription.  Track 9 does the systematic
search.

If a prescription exists, the metric carries the strong sector
directly without auxiliary dimensions or propagator formalism.
If none exists, we have a clean falsification — the strong force
genuinely sits outside the metric, and Q135's hub-and-spoke
principle is fully earned.

### Goal

Find σ_pS_tube as an explicit function of other R60 metric
entries (σ_ta, σ_at, σ_ra, ε_p, s_p, possibly more) such that:

1. α universality is preserved across the full inventory.
2. The function is non-trivial (σ_pS_tube ≠ 0 at general
   parameters).
3. At the working metric values, σ_pS_tube reaches a magnitude
   sufficient to produce a strong-force NN potential trough
   (per Phase 7c's reference: depth ~50 MeV at r ~ 1 fm).

If all three pass: the strong force lives in the metric via a
structural prescription, and direct sheet-S coupling is
architecturally legitimate.  If any fails, the negative result
narrows the structural options for where the strong force lives.

### Strategy

Phase 7e provided the data: σ_pS_tube perturbs α by mode-dependent
quadratic factors.  The shifts have specific structure
(electron up, proton down, etc.) that any prescription must
cancel.

The universality constraint is algebraic.  For each inventory
mode `i` with windings `n_i`, demand `α_i(σ_pS_tube, ...) =
α_baseline` to all orders in σ_pS_tube.  This gives a system of
equations.  Solving for σ_pS_tube as a function of the other
entries finds the prescription if one exists.

R60 T7 did this for σ_ra and got a closed-form result.  For
σ_pS_tube, the answer is unknown until the calculation is done.

### Phases

**Phase 9a — Algebraic universality constraint.**

Set up `α_Coulomb(mode, augmented metric)` symbolically with σ_pS
as a free variable.  Expand to second order in σ_pS.  Demand
α stays at baseline across the 10-13 inventory modes.  Output:
a system of constraint equations on σ_pS as a function of other
entries.

**Phase 9b — Solve for the prescription.**

Two cases:

- **Single-parameter solution exists**: σ_pS = f(σ_ta, σ_at,
  σ_ra, ε_p, s_p) — explicit formula that preserves α.
  Track 9 succeeds at this phase.
- **Single-parameter doesn't suffice**: enumerate companion
  entries (σ_pS_ring, modifications to σ_ra, etc.) and re-solve
  the larger system.  Either find a multi-parameter prescription
  or conclude none exists.

If the system is over-constrained (no consistent solution exists
across all inventory modes), the prescription doesn't exist —
direct sheet-S coupling is fundamentally incompatible with α
universality.  Q135 hub-and-spoke is then fully earned.

**Phase 9c — Numerical validation.**

If 9b found a prescription:

1. Plug into augmented metric.
2. Verify α universality numerically across the 13-mode inventory
   (target: same machine-precision as Phase 8b's locus).
3. Compute V(r) using the prescribed σ_pS at R64 Point B
   parameters with corrected two-body kinematics (Phase 7c
   convention, A_kin = 4·(ℏc)²).
4. Check whether the resulting trough has Phase 7c-magnitude
   depth (~50 MeV) at physical r (~1 fm).

**Phase 9d (conditional) — Schrödinger validation.**

If 9c lands a viable V(r), repeat Phase 7d's calculation with
the new V(r): B(²H), a_t, a_s.  Compare to observation.  Same
diagnostic that exposed Phase 7c's limitations may apply here
too.

### Acceptance criteria

| # | Criterion | Status |
|:-:|:---|:---|
| 1 | Universality-preserving prescription σ_pS = f(other entries) found | Phase 9b gates this |
| 2 | Prescription is non-trivial (not σ_pS ≡ 0) | Phase 9b checks |
| 3 | At working parameters, prescribed σ_pS reaches Phase 7c magnitude | Phase 9c |
| 4 | Resulting V(r) matches Phase 7c's trough at intermediate r | Phase 9c |
| 5 | (optional) Schrödinger observables land within band | Phase 9d |

### Possible outcomes

**Outcome A — Prescription found, delivers strong force.** σ_pS
gets a closed-form derivation analogous to σ_ra.  Strong force
emerges from the metric without new dimensions or propagator
machinery.  Hub-and-spoke is generalized: any metric off-diagonal
is allowed if it has the right structural prescription.

**Outcome B — Prescription found, but at uninteresting magnitude.**
σ_pS gets a formula, but plugging in the working parameters gives
a value too small for strong-force coupling (analogous to Phase
8c's α-suppression).  The metric carries the structural symmetry
but not the dynamical magnitude — strong force still requires
elsewhere.

**Outcome C — No prescription exists.**  The universality
constraint is over-determined.  Direct sheet-S coupling is
fundamentally incompatible with α universality at any
prescription.  Q135 hub-and-spoke is fully earned, and the
strong force is structurally not in the metric — propagator-
based formalism (R64 pool m) becomes the unavoidable next path.

**Outcome D — Partial / multi-parameter prescription.**  Several
companion entries needed (σ_pS, σ_pS_ring, etc., jointly
constrained).  Track 9 succeeds but with a richer architecture
than R60 T7's single σ_ra prescription.

Each outcome is informative; no single result aborts the
study.

### Why this is the right next track

You stated a preference for keeping the strong force inside the
metric formalism (no auxiliary dimensions, no propagator
machinery).  Track 9 is the **only systematic test** of whether
that's possible.  Phase 7e tested a single un-prescribed σ_pS
and found it broke α — but didn't try to find the right
prescription.  Phase 8c tested aleph-mediation and found it too
weak — but ruled in the *direct* path only by ruling out the
*aleph-mediated* path.  Track 9 closes this gap by going after
the direct path with the systematic constraint solver R60 T7
established as standard.

The work is bounded — single algebraic study with closed-form
output (or proof of non-existence).  R60 T7's σ_ra precedent
suggests the methodology works.  The only unknown is what the
prescription looks like (if any).

### Reusable assets

- R60 T7's σ_ra derivation as the methodological template.
- R60 Track 12's α-extraction infrastructure (already used
  in 7e and 8a/8b/8c for sweeping).
- Phase 7e's mode-by-mode α-shift data as the constraint
  input.
- Phase 7c's V(r) machinery (with corrected two-body
  kinematics from Phase 8c) for the numerical test if 9b
  succeeds.

### Outputs

- `outputs/track9_phase9b_prescription.txt` — the σ_pS
  formula or proof of non-existence.
- `outputs/track9_phase9c_universality_check.csv` —
  numerical verification of universality at prescription.
- `outputs/track9_phase9c_potential_curves.png` — V(r)
  at prescribed σ_pS, comparison to Phase 7c reference.
- `findings-9.md` — full Phase 9a/9b/9c writeup.

---

## Track 10 — Ring-S coupling: testing the mass-channel hypothesis for the strong force

**Status: framed; Phase 10a pending execution.  Other phases in pool.**

**Premise.**  Track 7–9 tested σ_pS_tube as the candidate strong-
force coupling and found it cannot deliver Phase 7c-class strength
under any compensation structure within signature constraints
(σ_eff capped at ~0.5; Phase 7c required ~116).  Every prior
attempt routed through the **tube** sheet entry — i.e., the
*charge*-promotion direction.

But the strong force has gravity-like phenomenology: always
attractive, charge-symmetric (pp ≈ nn ≈ pn under strong), much
stronger than Coulomb.  In MaSt's promotion chain:

- **Mass = ring** (first-order: light → mass via the ring 2π
  closure).  Always positive (`m² ≥ 0`).  Source of gravity.
- **Charge = tube** (second-order: mass → charge via the tube 2π
  closure).  Signed.  Source of Coulomb.

If the strong force is structurally "gravity-like" rather than
"Coulomb-like," it should originate in the **ring** sector, not
the tube sector.  Track 10 tests whether direct ring-S coupling
(σ_pS_ring) — not tube-S — is the right metric origin for the
strong force.

This reframe is a **simplification, not an addition**: it doesn't
introduce new dimensions, propagator formalism, or auxiliary
structure.  It just tests a different metric off-diagonal as the
primary entry.  σ_pS_ring has been a *companion* in prior phases
(Phase 9 H1, H3, H6) but has never been the *primary* coupling.

### Phase 10a — σ_pS_ring as primary direct coupling

**Status: pending execution.**

**Goal.**  Test whether direct p-sheet ring ↔ S spatial coupling
preserves α universality (with or without companion entries) and
produces an attractive, charge-symmetric V(r) at signature-OK
magnitudes.  Compare against Phase 9's σ_pS_tube primary results.

**Strategy.**

1. Replicate Phase 7e/9b's machinery with σ_pS_ring as the
   primary entry instead of σ_pS_tube.
2. Sweep σ_pS_ring alone first; observe α universality
   perturbation pattern and signature band.
3. If universality breaks (likely), search for compensating
   companion entries analogous to Phase 9b's H2 prescription
   (σ_aS = -1.819·σ_pS_tube).  Candidate companions:
   - σ_aS (aleph-mediated parallel)
   - σ_pS_tube as companion (inverse of Phase 9 H2 setup)
   - σ_eS_ring, σ_νS_ring (3-sheet symmetric)
4. At the prescription that preserves universality, sweep
   σ_pS_ring within signature band; compute V(r) for pp, pn,
   nn channels using Phase 7c's two-body kinematic formula
   with σ_eff extracted from the augmented 11D inverse metric.
5. Check phenomenology:
   - **Charge symmetry**: V(pp) ≈ V(nn) within Coulomb shift?
   - **Always attractive**: V_min < 0 across all three channels?
   - **Channel-symmetric strong contribution**: pn distinguished
     from pp/nn only by Ma-side offset?

**Acceptance criteria.**

| # | Criterion | Threshold |
|:-:|:---|:---|
| 1 | Signature band reaches σ_pS_ring with σ_eff ≥ 1 | Larger band than σ_pS_tube → progress |
| 2 | α universality preserved (with or without companions) | Spread < 10⁻⁹ |
| 3 | Three channels (pp, pn, nn) get attractive V(r) | All V_min < 0 at intermediate r |
| 4 | Strong contribution charge-symmetric | V_strong(pp) ≈ V_strong(nn) ≈ V_strong(pn) |
| 5 | At signature boundary, σ_eff approaches Phase 7c scale | σ_eff > 1, ideally → 116 |

**Possible outcomes.**

- **A — Ring-S delivers the strong force.**  σ_pS_ring at
  signature-permitted magnitudes produces an attractive,
  charge-symmetric V(r) trough at intermediate r.  The strong
  force lives in the metric via the ring (mass) channel.  The
  user's two-channel hypothesis is vindicated.
- **B — Ring-S preserves universality but at limited magnitude.**
  Same structural ceiling as σ_pS_tube (~σ_eff = 0.5).  The
  signature constraint is fundamental regardless of which
  off-diagonal carries the coupling.  Strong force confirmed
  outside metric.
- **C — Ring-S preserves universality AND delivers stronger
  σ_eff than tube-S, but still falls short of Phase 7c.**
  Partial structural progress; ring channel is "better" than
  tube channel for strong force but neither is sufficient.
- **D — Ring-S is structurally wrong** (universality breaks
  with no recoverable prescription).  Track 10 closes
  symmetrically with Track 9; both metric channels are
  exhausted; propagator route is the architectural inevitable.

**Reusable assets.**

- Phase 7e infrastructure (α-universality test machinery).
- Phase 9b's optimization framework (scipy.optimize for
  prescription search).
- Phase 7c's V(r) machinery with corrected two-body kinematics
  (Phase 8c convention, A_kinetic = 4·(ℏc)²).
- R64 Point B p-sheet calibration.

**Outputs.**

- `outputs/track10_phase10a_universality_sweep.csv`
- `outputs/track10_phase10a_potential_curves.csv`
- `outputs/track10_phase10a_potential_curves.png`
- `findings-10.md`

### Why this matters

If 10a returns Outcome A (ring-S delivers the strong force), R64
suddenly has a complete in-metric architecture: Coulomb via
tube → aleph → t (R62 D5 / R60 architecture); strong force via
ring → S (Track 10).  Two channels, structurally aligned with
Q132's promotion chain (mass = ring, charge = tube), no new
dimensions or propagator formalism.

If 10a returns Outcome B/C/D, the metric route to strong force is
genuinely exhausted across both tube and ring channels, and the
propagator-based approach (R64 pool item m) becomes the
unavoidable architectural path.

Either way, Phase 10a is decisive for the "two-channel metric
hypothesis" — and it's a single bounded test, not an expansion
of complexity.

---

## Track 11 — Quark-counting structural audit

**Status: Phases 11a and 11c complete.  Strong force confirmed in the metric.  See [findings-11.md](findings-11.md).**

**Net Track 11 result.**  The 11D metric formalism delivers the
strong force at full magnitude (σ_eff_tube = ±116) with charge-
symmetric V(r): pp, nn at −32 MeV (charge-symmetric within
~0.4 MeV), pn at −50 MeV at r ≈ 1.135 fm — exactly Phase 7c's
profile.  Two corrections together rescued the metric: (i)
A1 charge attribution `f(n_pt, n_pr) = n_pt/6 + n_pr/4`
resolving the factor-of-9 anomaly; (ii) measuring σ_eff at the
precise signature edge rather than at "safe distance" as Track
10 had done.  Phase 9b's H2 prescription (σ_aS = −1.819·σ_pS_tube)
combined with edge methodology completes the strong-force
architecture.  Pool item m (Yukawa propagator) is no longer
forced; the metric formalism is complete.

**Phase 11a result (summary).**  Two findings, both substantial:

1. **Pool item g resolved.**  The charge-function projection
   `f(n_pt, n_pr) = n_pt/6 + n_pr/4` (linear, derived from u →
   +2/3, d → −1/3) gives α universality at machine precision
   (5 × 10⁻⁸ spread) across the full R64 inventory: single
   quarks, baryons, two-nucleon compounds, leptons, neutrino.
   The factor-of-9 anomaly silently propagated since Phase 7g
   is corrected.
2. **Track 10's σ_eff cap was a measurement artifact.**  The
   Schur-effective σ_eff_ring grows divergently as σ_pS_ring
   approaches the signature boundary (0.1251).  Within the
   signature-OK band, σ_eff_ring is freely tunable from 0 to ∞.
   At σ_pS_ring ≈ 0.12505, σ_eff_ring = 116 (Phase 7c's target).

**The remaining obstruction is channel structure, not magnitude.**
At σ_eff_ring = 116, V(r) is qualitatively wrong: pp repulsive,
nn attractive (charge asymmetric), pn unaffected (n_pr = 0).
The ring channel is structurally tied to signed n_pr and cannot
give the charge-symmetric strong force of nature.  Phase 11b
(pairwise cross term) is the architecturally indicated next test.

**Premise.**  Track 10's combined verdict (Phases 10a, 10b, 10c)
was that the metric route to the strong force is exhausted: σ_eff
caps at ~1 across all tested couplings, vs Phase 7c's σ_t = 116
target.  Before declaring the metric formalism closed, audit
whether the gap reflects a **counting error** introduced by R64's
shift from R60 model-F primitives to a u/d quark decomposition.

**The R60 → R64 shift.**  R60 model-F treated the proton as a
single primitive at `(n_pt, n_pr) = (1, 3)`.  R64 decomposes it
into `u + u + d` with quark primitives `u = (1, +2)`, `d = (1, −2)`,
giving proton = `(3, +2)`.  Critical consequence:

- R60 proton: bare α/α₀ = (n_pt)² = 1.
- R64 proton: bare α/α₀ = (n_pt)² = **9**.

Phase 7g acknowledged this as "pool item g" (charge-attribution
rule needs derivation) but never resolved it.  The factor of 9
has been silently propagated through every R64 phase since.

**The structural question.**  Two issues compounded from the
quark decomposition:

1. **α-attribution.**  Q in the Coulomb formula is linear in the
   raw mode 6-tuple: `Q = n_Ma · G⁻¹[Ma, t] · (−G⁻¹[t, t])`.  At
   R64 the proton's effective charge is *physically* +1 e, not
   +3 e, but the formula reads `n_pt = 3` and produces 3× the
   charge.  The natural fix is a charge-projection that maps
   the R64 (n_pt, n_pr) onto the actual electric charge in units
   of e: `f(n_pt, n_pr) = n_pt/6 + n_pr/4` reproduces u = +2/3,
   d = −1/3, proton = +1, neutron = 0, deuteron = +1.
2. **Cross-term linearity.**  In the strong-force m² expression,
   the cross term is `2·k_S·σ_t·n_pt·ℏc` — *linear* in n_pt.
   The actual strong force is pairwise (gluon-mediated between
   quark pairs).  For two nucleons: 6 quarks total, but 9 cross-
   nucleon quark pairs.  A pairwise reformulation `σ·Σᵢⱼqᵢqⱼ`
   could give qualitatively different counting — and crucially,
   the deuteron (n_pr_total = 0 under the linear form, hence
   zero contribution from σ_pS_ring in Phase 10a) would receive
   nonzero attractive contribution from u·d pair products.

If either issue corrects to close the σ_eff gap, the metric
formalism is rescued.  If neither does, the pool item m
(propagator) path is genuinely the only architectural option.

### Phase 11a — α-attribution audit

**Status: pending execution.**

**Goal.**  Quantify the magnitude error in α/α₀ across R64's
u/d-decomposed inventory under the current attribution rule, and
test whether an alternative rule (signed-quark-charge projection)
recovers α universality at R64 tuples while preserving R60
model-F results.

**Strategy.**

1. Compute α/α₀ across R64 inventory (R64 proton (3, +2), neutron
   (3, −2), deuteron (6, 0), pp (6, +4), nn (6, −4), single u
   (1, +2), single d (1, −2)) under current `n_Ma · G⁻¹[Ma, t]`
   formula at R60 model-F metric calibration.  Tabulate α/α₀
   ratios.
2. Test attribution rule **A1**: replace `n_pt, n_pr` in α formula
   with `n_pt_eff = f(n_pt, n_pr) = n_pt/6 + n_pr/4` (signed
   electric charge in units of e).  Compute α/α₀ across the same
   inventory.
3. Test attribution rule **A2**: leave the formula intact but
   recalibrate the p-sheet σ_ta, σ_at to absorb the factor of 3
   (`σ_ta_p_R64 = σ_ta / 3`).  Check whether universality across
   e/ν sheets still holds.
4. If A1 or A2 succeeds, recompute the Schur-effective σ_eff_ring
   at signature boundary in Phase 10a's framework under the
   corrected calibration.  Compare to current 1.13.
5. Document where the factor of 3 (or 9) goes — does it shift
   σ_t target, σ_eff_ring boundary, or both?

**Acceptance criteria.**

| # | Criterion | Threshold |
|:-:|:---|:---|
| 1 | At least one attribution rule gives α/α₀ = 1 ± 10⁻⁶ at R64 proton | yes/no |
| 2 | The same rule gives α/α₀ = 0 (within numerical noise) at R64 neutron | yes/no |
| 3 | Universality across full R64 inventory (proton, neutron, deuteron, single u, single d, electron, ν, mesons) preserved | spread < 10⁻⁶ |
| 4 | Under corrected attribution, σ_eff at Phase 10a boundary changes by a factor that closes a measurable fraction of the 102.7× gap | report ratio |

**Possible outcomes.**

- **A — Attribution fix closes the gap.**  An alternative rule
  gives α universality at R64 tuples *and* rescales σ_eff at
  signature boundary by a factor that brings it within reach
  of Phase 7c's 116.  The metric formalism is rescued; the
  R64 → strong-force path is intact, just mis-calibrated by a
  quark-counting factor.
- **B — Attribution fix is real but doesn't close the gap.**
  An alternative rule fixes the α/α₀ = 9 anomaly (architecturally
  important — pool item g resolved) but σ_eff at signature
  boundary still doesn't reach 116.  Gap is structural, not
  calibration.  Phase 11b (pairwise cross term) becomes the
  next test.
- **C — No attribution rule gives universality at R64 tuples.**
  R64's u/d composition is structurally incompatible with the
  Coulomb α formula in its current form.  Either the formula
  needs revision or R64's primitive assignment is wrong (one
  more architectural option to surface).

### Phase 11c — σ_pS_tube + H2 at signature edge (charge-symmetric strong force)

**Status: pending execution.  Replaces Phase 11b after Phase 11a structural insight.**

**Premise.**  Phase 11a established two things: (i) σ_eff is tunable
up to ∞ at the signature edge (not capped at ~1 as Phase 10a's
"safe-boundary" measurement suggested); (ii) the ring channel
cannot deliver charge-symmetric strong force because n_pr is
signed.  But the tube channel uses n_pt, which is **6 for all
two-nucleon systems** (3 quarks × 2 nucleons), independent of
pp/pn/nn — automatically charge-symmetric.

Phase 9b found the H2 prescription σ_aS = −1.819·σ_pS_tube
preserves α universality.  Phase 9c measured σ_eff_tube at "safe
boundary" and got ~0.5 — but that's exactly the measurement choice
Phase 11a corrected.  The tube channel might naturally deliver
σ_eff = 116 at the H2 signature edge.

**Goal.**  Test whether σ_pS_tube + H2 prescription, measured at
the precise signature edge (Phase 11a methodology), gives:
1. σ_eff_tube reaching Phase 7c's target of 116
2. α universality preserved at the edge (under both R0 and A1
   attribution)
3. V(r) for pp/pn/nn that's attractive, charge-symmetric, and
   binds the deuteron

**Strategy.**

1. Build R60 metric at R64 Point B with σ_pS_tube + H2 companion
   active.
2. Fine-grained boundary scan (step 10⁻⁵ near the edge) to find
   the precise σ_pS_tube where signature breaks.
3. Walk back from the edge measuring σ_eff_tube via the Schur
   formula `−G⁻¹[p_t, S_x] · g_pp · g_SS`.
4. Verify A1 universality holds at the edge (the critical
   correctness check Phase 11a established).
5. At σ_pS_tube giving σ_eff_tube = 116, compute V(r) for pp,
   pn, nn channels using the corrected two-body kinematics and
   A1 charge attribution.
6. Compare V_min(pp), V_min(pn), V_min(nn) for charge symmetry
   and Phase 7c reference depth.

**Acceptance criteria.**

| # | Criterion | Threshold |
|:-:|:---|:---|
| 1 | σ_eff_tube reaches 116 within signature-OK band | yes/no |
| 2 | A1 universality preserved at signature edge | spread < 10⁻⁶ |
| 3 | All three channels (pp, pn, nn) attractive at σ_eff = 116 | V_min < 0 for each |
| 4 | Charge symmetry: V_min(pp) ≈ V_min(nn) | within Coulomb shift |
| 5 | Deuteron binding nonzero | V_min(pn) < V(∞) |
| 6 | V_min depth matches Phase 7c reference | ≈ −50 MeV at r ≈ 1.1 fm |

**Possible outcomes.**

- **A — Tube channel rescues the metric formalism.**  σ_pS_tube
  + H2 at signature edge gives charge-symmetric, deuteron-binding
  V(r) at the right magnitude.  Strong force lives in the metric;
  pool item m unforced.  The 11D metric is complete.
- **B — Magnitude reaches 116 but V(r) shape is wrong.**  σ_eff
  scales but kinematic structure (r_min, depth profile) doesn't
  match Phase 7c.  Working-point (ε_p, s_p) needs adjustment;
  Phase 11d (joint refit at edge) becomes the natural follow-on.
- **C — H2 prescription breaks at the edge.**  Universality fails
  near the signature boundary even with companion compensation.
  Different prescription needed (revisit Phase 9 H6, H10, or
  derive new structure).
- **D — Tube channel structurally insufficient.**  Even at edge,
  σ_eff_tube doesn't reach 116, or the cross term magnitude isn't
  what V(r) needs.  Then propagator route returns as the
  architectural option.

### Phase 11b — Pairwise vs linear cross term [pool, deprecated]

**Status: deprecated by Phase 11a structural analysis.**

A pairwise quark-quark cross term `σ·Σᵢⱼ qᵢqⱼ` factors back to
`(Σᵢ qᵢ)²` in any single-body metric formalism.  For pn (Σq = 0)
this gives zero contribution — the deuteron problem returns.
Single-body metrics cannot encode genuine pairwise structure;
that requires multi-body or propagator formalism.  Phase 11c
addresses charge-symmetry via the tube channel instead, which
uses n_pt (= 6 for all NN systems) as the natural always-on
quantity.

**Goal.**  Test whether replacing the linear cross term
`σ·n_pt` with a pairwise quark-quark sum `σ·Σᵢⱼ qᵢqⱼ` gives
qualitatively different V(r) for pp, pn, nn — particularly
rescuing the deuteron (currently zero contribution from
σ_pS_ring because n_pr(pn) = 0).

**Why bounded.**  This is a one-script investigation: re-run
Phase 10a's V(r) calculation with the cross-term substitution.
No new metric structure, no new dimensions.  If pairwise
counting changes the deuteron picture, that's a structural
finding regardless of whether σ_eff magnitude closes the gap.

### Why this is the right next track

Track 10 closed by declaring the metric route exhausted, but the
quark-counting question was raised explicitly by the user as a
plausible source of factor-of-3 (or factor-of-9) error.  Pool
item g has been silently deferred since Phase 7g.  Both Phase 11a
(attribution) and 11b (pairwise) are bounded single-script tests.
Worst-case outcome confirms metric exhaustion (no harm done);
best case rescues the metric formalism.

### Outputs

- `outputs/track11_phase11a_attribution_audit.csv`
- `outputs/track11_phase11a_alpha_ratios.png`
- `findings-11.md` — Phase 11a writeup, frames 11b if relevant.

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

## Track pool

All items are letter-keyed for flexible selection in any order.
Items marked **[model-G]** are gates on promotion to a model-G
candidate.  Categories are organizational only — pull any item
when ready.

### Goal alignment

The pool serves four overall goals:
1. **Solve the weak force** (complete the four-force scorecard).
2. **Make the metric principled and accurate** (every off-
   diagonal has a structural rationale; every "free" parameter
   is derived or pinned).
3. **Assemble model-G** (the working post-R64 model candidate).
4. **Derive every metric term from first principles** (deferred
   to a separate study once model-G is stable).

---

### Force completion (goal 1)

**u. Weak force from e-sheet → S coupling.**  **[model-G]**
By analogy with Track 11's strong-force discovery on the proton
sheet, weak force is hypothesized to live in σ_eS_tube + an
e-sheet H2 prescription analogous to the proton-sheet H2.  The
hub-and-spoke architecture provides cross-sheet routing
(charged-current e ↔ ν via aleph) for free.
**Test:** activate σ_eS_tube on the e-sheet; derive the e-sheet
H2 coefficient as `b_e = −G⁻¹[E_TUBE, t] / G⁻¹[ALEPH, t]` (Phase
11d framework, sheet-substituted).  Find signature edge.
Compute V(r) for ee, eμ systems and check for Yukawa profile
with mass scale.
**Yields:**
- A: Yukawa with M ≈ 80 GeV → weak force confirmed in metric.
- B: Yukawa with wrong mass scale → e-sheet → S delivers a force,
  scale needs additional input.
- C: not Yukawa-shaped → reconsider what e-sheet S-channel does.
- D: universality breaks → re-derive the e-sheet H2 form.

**t. Symmetric three-sheet → S activation.**  **[model-G]**
Broader companion to item u.  Activate σ_pS_tube + σ_eS_tube +
σ_νS_tube simultaneously, each with its own sheet-H2 prescription,
and identify what each sheet's S-coupling delivers
phenomenologically.  Confirms whether the architecture is
genuinely three independent Clifford-style embeddings + aleph
hub, vs. "p-sheet is special."
**Test:** find joint signature edge; verify A1 universality
survives; compute V(r) for representative ee, eμ, νe, νν systems
in addition to NN already covered.
**Yields:** sheet-by-sheet identification of force sector.
Strong on p (Phase 11c); weak/ν-current on e/ν per item u
results.

**v. Anomalous magnetic moments from H2 second-order leakage.**
**[model-G]**  Second-order σ_pS_tube² leakage in the H2 prescription
shifts the proton's α by 4 × 10⁻⁴ at the strong-force operating
point — exactly the order of magnitude of QED anomalous magnetic
moments.  The pattern matches qualitatively: large proton
anomaly (a_p ≈ 1.79), tiny electron anomaly (a_e ≈ 1.16 × 10⁻³),
explained by p-sheet activation vs. no-e-sheet activation in
current architecture.
**Test:** (i) translate the metric's σ_aS-induced second-order
G⁻¹[ALEPH, S_x] shift into a magnetic-moment correction in
physical units; (ii) compute predicted proton g/2 under
σ_pS_tube + H2 at edge; (iii) compute predicted electron g/2
under σ_eS_tube + e-H2 at edge (after item u); (iv) compare to
observed a_p, a_e.
**Yields:** if predictions match observed g-2 within an order
of magnitude, the anomaly emerges automatically from the same
H2 mechanism that delivers strong/weak forces — no QFT loop
calculation needed.  Major architectural finding.  R44 closed
g-2 from torus geometry but did NOT test this mechanism.

**z. Neutron lifetime from p-sheet shear + cross-sheet matrix
element.**  **[model-G]**  *(Highest-stakes outstanding test.)*
Tests whether MaSt predicts τ_n ≈ 880 s from structural ingredients.
The hypothesis (electroweak unification reframing): EM and weak
are two aspects of the same p-sheet structure — Coulomb is the
shear-symmetric (proton/neutron-equal) charge winding, while weak
is the *shear-asymmetric* mass detuning that makes the neutron
metastable.  β decay is the relaxation channel, with rate set by
mass gap + cross-sheet matrix element.
**Method**: (i) compute Q-value from MaSt
`m_Ma(3, −2) − m_Ma(3, +2) − m_e − m_ν` at the working point;
(ii) apply standard phase-space integral (universal physics);
(iii) construct the transition matrix element ⟨p, e, ν̄ \| H \| n⟩
from cross-sheet structural couplings (σ_eS_tube + e-H2 from pool
item u + σ_νS_tube + ν-H2); aleph mediates between sheets;
(iv) compare predicted τ_n to observed 880 s.  Step (i) and (ii)
are simple; step (iii) is the substantive new work.
**Yields**: if order-of-magnitude match, weak force is
"p-sheet shear + cross-sheet matrix elements" — the reframing
is validated, model-G is ready.  If far off, we learn whether
the matrix element formalism needs refinement or whether
calibration (s_p) needs joint refit against τ_n.

**w. Magnetic-channel preservation under Track 11 activation.**
**[model-G]**  Verify that σ_eff_aS (the magnetic Schur coupling)
at σ_pS_tube + H2 active still delivers α-magnitude magnetic
effects, despite the bare σ_aS being 31× α at the operating
point.  G⁻¹[ALEPH, S_x] = 9 × 10⁻⁵ suggests Schur cancellation
keeps magnetic at the right scale, but explicit verification is
owed.
**Test:** re-run R60/R64 Phase 8 magnetic vector-potential test
with σ_pS_tube + H2 active in place of σ_aS-only activation.
Compare resulting magnetic α to baseline.
**Yields:** sanity check on Track 11 architecture; should pass
or surface a magnetic-α anomaly that connects to item v.

---

### Metric principle / accuracy (goal 2)

**r. Edge-methodology physical interpretation.**  **[model-G]**
Phase 11a F11a.4 and Phase 11c showed σ_eff_tube reaches Phase
7c's −116 only at the precise signature boundary (σ_pS_tube ≈
−0.12505).  This is a "lightlike" calibration where one metric
eigenvalue approaches zero.  Whether the strong-force trough
sitting *exactly* at this edge is structurally meaningful or a
numerical convenience is open.
**Test:** (i) symbolic analysis of G⁻¹[p_t, S_x] near the
boundary; (ii) check edge maximum at different working points;
(iii) investigate the lightlike eigenvector's interpretation
(massless mode? confined direction?).
**Yields:** if structural, σ_pS_tube becomes pinned (one fewer
free parameter).  If artifact, strong-force calibration is
ad hoc and pool item m returns.

**s. Clifford embedding analysis per sheet.**  **[model-G]**
The metric's all-zero cross-sheet block suggests three
independent flat-torus embeddings of each Ma sheet into the
ambient slice, communicating only through aleph.  Each sheet's
(ε, s) should satisfy a Clifford embedding constraint.
**Test:** (i) write down the Clifford embedding equation for a
generic 2D torus into the 4D × ℵ ambient block; (ii) derive the
resulting (ε, s) curve analytically; (iii) compare to empirical
curves — Track 1 (R64) for (ε_p, s_p), R53 ridge for (ε_e, s_e),
R61 mass-ratio constraint for (ε_ν, s_ν).
**Yields:** if analytical curves match empirical fits, 6 sheet
parameters compress to 3 effective DOFs.  Bounded analytical
task; closed-form expected.

**p. Meson α-attribution extension.**  **[model-G]**
A1 attribution `f(n_pt, n_pr) = n_pt/6 + n_pr/4` (Phase 11a)
gives correct α for R64 single-sheet primitives but multi-sheet
mesons still carry the R60 "winding sum²" formula.
**Test:** generalize A1 to a sheet-symmetric attribution
function `f(n_et, n_er, n_νt, n_νr, n_pt, n_pr)` that maps every
inventory tuple to observed electric charge in units of e.  The
form (a/6 + b/4) on the p-sheet suggests analogous forms on
e/ν sheets.
**Yields:** unified A1' attribution that gives correct α
across the full hadron inventory (closes interpretive ◆ rows
in zoo.md).  Bounded analytical task.

**x. A1 closed-form derivation from first principles.**
**[model-G]**  Phase 11a found `f(n_pt, n_pr) = n_pt/6 + n_pr/4`
empirically by demanding `f(u) = +2/3` and `f(d) = −1/3`.  But
the *origin* of the 1/6 and 1/4 coefficients is not derived —
they're just the unique solution to the two-quark-charge
constraint.
**Test:** derive A1 (and item p's e/ν analogues) from the
geometric structure of the sheet.  Likely connects to Clifford
embedding (item s) and the proton sheet's (ε_p, s_p) values.
The 1/6 may come from a 6-fold symmetry; the 1/4 from a 4-fold.
**Yields:** A1 becomes a structural prescription rather than an
empirical fit.  Removes one "fit" from the architecture's
provenance.

**y. R60 k recalibration to structural 2^(1/4)/(8π).**
**[model-G]**  R60's empirical k = 1.1803/(8π) is within 0.75%
of the structurally clean `k = 2^(1/4)/(8π)` (per Phase 11d).
Test whether using the structural value (instead of the R60
fit) preserves all R60 results to acceptable precision.
**Test:** rebuild R60 model-F with k = 2^(1/4)/(8π); re-run
universality, mass spectrum, and Phase 7c trough fit.  Verify
nothing breaks.
**Yields:** removes the 0.75% fit-residue and converts k to a
purely structural number (`2^(1/4)` = 4th-root, suggestive of
tube-cycle quotient).  One free parameter pinned.

**10f. Ring-aleph parallel channel.**  σ_ra (ring↔aleph) is
already in R60 as a derived companion of σ_ta.  But what if it
should be a *primary* channel parallel to σ_ta?
**Test:** parameterize σ_ra independently from σ_ta and check
whether α universality can be preserved with two independent
aleph-row entries (one tube, one ring).  This generalizes R60's
σ_ra prescription, possibly opening new structural space.

---

### Model-G integration (goal 3)

**i. Synthesis & promotion to model-G.**  Combine completed
tracks: R60 model-F + Track 11 architecture (σ_pS_tube + H2 +
A1) + ε/s/K calibrations.  Items u (weak), v (anomaly), q
(L_ring) recommended before promotion; r/s/x are nice-to-have
refinements.

**k. Strange family on a different generation.**  **[model-G]**
R64 Track 4 found 18% RMS error forcing s, Λ, Σ, Ξ as a single
primitive on the p-sheet.  Likely strange is a different
*generation*, not a different flavor at Point B.
**Test:** search for an `(ε_s, s_s, K_s)` point hosting `(1, 1)`
or another primitive class as the s-quark at ~510 MeV
constituent mass.  Cross-validate against Λ, Σ, Ξ.

**o. Z₃ and unit-per-sheet AM cross-check at R64 Point B.**
**[model-G]**  Verify R64's u/d compounds are Z₃-compliant
(every baryon `(3·k, ...)` after composition) and spin
assignments under unit-per-sheet AM still match observed
spin-½ for nucleons, spin-0/1 for mesons, etc.

**q. R64 L_ring recalibration.**  **[model-G]**
Phase 11f showed mode_energy gives wrong masses for R64 baryons
(~5500 MeV vs 938) because L_ring_p was carried over from R60
model-F's proton at (1, 3).
**Test:** refit L_ring_p (and possibly L_ring_e, L_ring_ν) so
mode_energy at the R64 proton tuple returns 938.272 MeV.  Verify
the rest of the R60 inventory still matches.

---

### Particle-physics extensions (goal 3, follow-on)

**a. Light-A deviation diagnosis.**  R64 may over-bind light
nuclei (⁴He at 22%, ¹²C at 13%).  Phase 7d will likely partially
address this for the deuteron.  Higher-A residuals open —
possibly finite-stack correction or many-body machinery (item n).

**b. Quantum-number decoding (Ma analogs of n, l, m_l, m_s).**
Identify the Ma winding/orientation feature for each atomic
quantum number.  Provisional mapping: n ↔ harmonic level,
l ↔ phase separation, m_l ↔ orientation, m_s ↔ ring-winding
polarity.

**c. Electron-shell harmonic structure on the e-sheet.**
Apply item b's quantum-number decoding to predict observed
atomic shell energies.

**e. Higher-generation quark search.**  Beyond strange (item k):
c, b, t.  Same generation framework should host c, b, t by
analogous primitive classes.

**f. Full hadron inventory under unified framework.**  Once
quark generations are identified (items k, e), predict mesons
and hyperons via Ma composition rules.

**n. Nuclear reactions & scattering machinery.**  V(r) is static.
Reactions need cross-sections, branching ratios, decay rates.
Two routes: (n.1) embed V(r) in non-relativistic many-body
Hamiltonian; (n.2) build propagator formalism in MaSt.

---

### Completed (kept for reference)

- **~~g. Charge-attribution rule extension.~~** **[COMPLETE — Phase 11a]**
  A1 = f(n_pt, n_pr) = n_pt/6 + n_pr/4.
- **~~j. α-coupling integration test.~~** **[COMPLETE — Phases 11a/c/d]**
  Strong-EM coupling preserved with H2 + A1.
- **~~l. Joint refit of (ε_p, s_p, σ_t).~~** **[COMPLETE — Phase 11e]**
  Point B confirmed under σ_pS_tube + H2 active.
- **~~10b. Aleph-redundancy audit.~~** **[COMPLETE — Phase 10b]**
  Aleph is structurally required; cannot be removed.
- **~~10e. Closed-form derivation of −1.819.~~** **[COMPLETE — Phase 11d]**
  `b = −8π·√α·2^(−1/4)`.

### Obsolete (no longer pursued)

- **~~d. Nuclear shell structure and magic numbers.~~** Re-deriving
  SM shell structure is structural re-invention, not novel work.
- **~~h. Z = 137 impedance-overflow audit.~~** Deferred indefinitely.
- **~~m. Yukawa long-range extension (propagator-based).~~**
  Track 11 reversed the architectural need — strong force lives
  in the metric.  Keep on shelf only if item r flips the
  edge-methodology verdict.
- **~~10c. Direct ring-time coupling (gravity-channel test).~~**
  Gravity is St + GRID territory, **outside MaSt scope**.  No
  longer relevant to MaSt's force completion.
- **~~10d. Two-channel hybrid (tube-S Coulomb + ring-S strong).~~**
  Phase 10a/11c reversed the premise.  Strong is in tube-S.
- **~~Phase 11b. Pairwise quark-quark cross term.~~**  Deprecated
  by Phase 11a structural analysis (factors back to (Σq)² in
  single-body metric; deuteron problem returns).
- **~~Inventory re-derivation under flavor-aware composition.~~**
  Track 4 Phase 4a found incompatible with SM isospin.
- **~~Hybrid R63 tuples at R64 parameters.~~** Track 5 Phase 5a
  superseded.
- **~~S-stability tooling as separate prerequisite.~~** Superseded
  by Line 2.

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
