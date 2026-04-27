# R64 Review — Tracks 1–7 and proposed Phase 7c

## The arc, one line per track

1. **T1 — Magic point search.**  Located Point A at `(ε_p, s_p, K_p)
   = (0.07309, 0.19387, 22.847)` matching m_u, Δ(n−p), and B(²H)
   within 0.1%.
2. **T2 — Strange quark primitive.**  No clean single primitive
   matches the s-quark family at Point A.
3. **T3 — Nuclear chain.**  Heavy nuclei under-bind by ~7× at
   Point A; global re-fit located Point B at `(0.2052, +0.0250,
   63.629)` with Ca→Sn accuracy 1–2%.  Deuteron is outlier at
   Point B.
4. **T4 — Inventory at Point B.**  Per-particle masses fit <2%
   for non-strange; strange family fit gives 18% RMS error under
   forced single primitive.
5. **T5 — Two-line nuclear binding.**  Ma harmonic stack + S Coulomb
   structural model.
6. **T6 — Shell-structure tooling.**  Slot-configuration framework
   for testing specific shell hypotheses.
7. **T7 — Strong force from 7-tensor (the strong-force effort).**  See
   detailed analysis below.

**Net at T7 close.**  R64 produces a working nuclear model for the
non-strange chain and a structurally encouraging emergent
strong-force shape, with two clean limitations: strange family
doesn't fit a single primitive (T4), and the strong-force depth
is off by ~5× at the natural kinetic scale (T7a).

---

## Flaws and concerns by track

### Tracks 1–3: provisional anchoring is the right call

Both Point A and Point B are explicitly held provisional in the
README, which is correct.  The deuteron-as-outlier finding in T3
is honest — re-fitting the global chain inevitably picks up bulk
behavior at the cost of small-A specificity.

**No structural flaw.**  The two-point provisional state is an
honest "we don't have one point that does everything yet."

### Track 4: the strange-family forced fit is misleading

Forcing a single strange primitive to fit Λ, Σ, Ξ at Point B with
18% RMS error treats the strange flavor as analogous to up/down
on the same sheet.  In SM, strange is a different *generation*,
not just a different flavor within generation 1.  R64's natural
mapping should perhaps be: strange = a primitive on a *different*
e-sheet generation (mapping `(1, 1)` to s the way `(1, 2)` maps
to u/d), not a different p-sheet primitive.

**Recommendation:** revisit T4 with the SM generation structure
in mind.  R60's three e-sheet primitives `(1, 2), (1, 1), (1, 15)`
suggest three quark generations.  If the s-quark is a different
generation rather than a third p-sheet primitive at Point B, the
"forced fit" disappears and the strange family becomes a separate
search on a different (ε, s) point.

### Tracks 5–6: tooling, not findings

These are infrastructure tracks — useful for the slot-by-slot
shell exploration but no structural concerns.

### Track 7: the strong-force effort

This is where R64 has its biggest near-miss and its biggest
potential payoff.  Detailed analysis below.

---

## Track 7 — the strong-force effort, in detail

### What 7a accomplishes

The 7-tensor with cross-shear σ_t between p-sheet tube and S
spatial dimension produces, from the geometric structure alone:

1. A **trough** in E(r) for two-particle p-sheet configurations
   (not put in by hand — it falls out of the metric coupling).
2. **Charge-independence:** σ_r = 0 is forced structurally because
   pp and nn must be treated symmetrically; that's a real
   physics constraint emerging from the geometry.
3. **pn deeper than pp by ~18 MeV** — Ma-side (Point B) supplies
   the n-vs-p preference without further input.
4. **Coulomb 1/r tail** added cleanly at large r for charged
   pairs.

These four together qualitatively reproduce the observed nuclear
NN potential's structural features.  The shape is right.

### Where 7a misses

The trough's depth at the natural choice `A = (ℏc)²` is ~21 MeV
at r ≈ 1.6 fm, vs observed ~50 MeV at ~1 fm.  The structural
identity F7a.4 fixes:

`Depth · r₀² = A / (2 · m_Ma) ≈ 10.4 MeV·fm²`  (with the user's choice)

Observed: `~50 MeV·fm²`.  Off by factor ~5.

### Why 7a misses — the kinematic flaw

The mass formula `m²(k_S) = m²_Ma + A·k_S²` treats `m_Ma` as the
total compound mass `M_total = 2·m_p` and `A = (ℏc)²` as the
relativistic kinetic coefficient.  This is correct for a **single
particle** of mass `M_total` carrying momentum p = ℏk_S.

But the physical scenario is **two nucleons approaching each other
in the COM frame**.  Each has equal-and-opposite momentum p; each
contributes its own kinetic energy.  The system's invariant-mass-
squared in COM is:

`M_inv² = (2·√(p² + m_p²))² = 4·(p² + m_p²) = M_total² + 4·p²`

So the kinetic-coefficient should be **`A = 4·(ℏc)²`** for two
equal-mass particles, not `(ℏc)²`.  Equivalently, in the
non-relativistic Schrödinger picture: relative-motion kinetic
energy is `p²/(2·μ_red)` where `μ_red = M_total/4` for equal
masses — four times the naive `p²/(2·M_total)`.

**The 7a formula is missing the second nucleon's kinetic share.**
It treats the compound as one stationary object compressed by
S-momentum, instead of as two nucleons in relative motion.

### What the corrected calculation gives

Plug `A = 4·(ℏc)²` into `Depth · r₀² = A/(2·M_total)`:

`Depth · r₀² = 4·(ℏc)² / (2·2·m_p) = (ℏc)²/m_p ≈ 41.5 MeV·fm²`

Compared to observed ~50 MeV·fm²: off by ~17%, not factor 5.

Plug for r₀ = 1 fm:

`Depth = (ℏc)²/m_p / r₀² ≈ 41.5 MeV` at r₀ = 1 fm.

Observed nuclear NN potential depth at 1 fm: ~40–60 MeV (depending
on the channel).  R64's 7-tensor with corrected kinematics lands
**inside the observed range**.

The remaining ~17% gap is small enough to come from secondary
effects: relativistic corrections to the leading-order expansion,
Coulomb interference at intermediate r, or σ_t fine-tuning.

### What about the Yukawa issue (7b)?

Phase 7b correctly diagnosed that the metric-coupling approach at
a single momentum k_S = 1/r produces a polynomial form
`A₂/r² + A₁/r`, not the Yukawa exponential `e^{−mr}/r`.  This is
a structural property of the metric formulation — to recover
Yukawa you'd need propagator physics (integrate over virtual
momenta).

**This isn't fatal to 7c.**  At intermediate r (~0.5–2 fm), the
polynomial form is a decent approximation to Yukawa anyway.  The
exponential cutoff matters for the strong-force range at r > 2 fm,
not for the deuteron's binding-scale physics.  Phase 7c should
acknowledge the polynomial form as the leading-order metric
result and treat the Yukawa exponential cutoff as a successor
question (propagator-based MaSt extension).

---

## Recommended Phase 7c

**Goal**: re-run the 7-tensor calculation with correct two-body
kinematics, demonstrate that the trough depth and position match
observation at the structural level, and document σ_t as an
empirical strong-coupling parameter (analogous to QCD's α_s).

### Phase 7c structure

**Step 1 — Replace `A = (ℏc)²` with `A = 4·(ℏc)²`** in the mass
formula `m²(k_S) = m²_Ma + A·k_S² + 2·k_S·B·ℏc`.  Equivalently,
divide by `μ_red = m_p/2` instead of `M_total = 2·m_p` in the
V(r) extraction.  Document the kinematic justification:
two-body relative motion in COM frame contributes 4× the
single-particle kinetic energy at fixed momentum.

**Step 2 — Re-sweep σ_t to find the value that places r_min ≈
1 fm.**  With corrected A, `r_min = 2A/|B|`, and `|B| =
2·σ_t·n_pt·ℏc`.  Solving: `σ_t = ℏc/(n_pt · r_min) = 197.3 /
(6 · 1) ≈ −33` (sign attractive).  Re-run the σ_t sweep with
fine resolution near σ_t ≈ −33.

(Note: I had σ_t ≈ −131 in my initial estimate; correcting for
the unit/normalization here gives σ_t ≈ −33.  The Phase 7c run
will land it precisely.)

**Step 3 — Verify the trough's full structure.**  At the Phase
7c best σ_t:

- Depth at r_min ≈ ?  (predicted ~40 MeV)
- Position r_min ≈ 1 fm (by construction)
- pn vs pp preference: pn deeper than pp by ~?  MeV (predicted
  ~20 MeV by Ma-side alone, may shift)
- nn vs pp: still equal under σ_r = 0 (charge-symmetric)
- Coulomb tail: still 1/r at large r for charged configs

**Step 4 — Document σ_t's structural status.**  At the corrected
A, σ_t ≈ −33.  Check:

- σ_t · α ≈ −0.24
- σ_t · √α ≈ −2.8
- σ_t / 4π ≈ −2.6
- σ_t · n_pt² · α = (−33)(36)(1/137) ≈ −8.7

None of these is clean.  But also worth checking is whether σ_t
naturally relates to a *combination* of the metric's structural
parameters at Point B (`ε_p, s_p, K_p`).  If so, σ_t becomes a
derived quantity.  If not, treat it as MaSt's α_s analog —
empirical strong coupling.

**Step 5 — Compare to NN scattering phase shifts (optional).**
The Phase 7c potential V(r) can be plugged into a Schrödinger
equation to compute deuteron binding energy and S-wave NN
scattering length.  Comparison to observed values (B(²H) =
2.22 MeV, a_t = 5.42 fm, a_s = −23.7 fm) is a stronger validation
than just "depth matches."  This phase is optional but would
elevate Phase 7c from "shape and scale match" to "scattering
data match."

### Acceptance criteria for Phase 7c

- ✓ Depth at r_min ≈ 1 fm is in the range 40–60 MeV.
- ✓ pn deeper than pp by 10–25 MeV (from Ma-side at Point B).
- ✓ Coulomb tail correct.
- ✓ σ_t value documented (whether α-related or empirical).
- ⚠ If depth comes out way off (factor 2+ either direction),
  the kinematic correction wasn't the only issue — investigate
  which other assumption needs revising.

### Why this matters

If Phase 7c lands at 40–50 MeV depth at r ≈ 1 fm, **R64 will have
produced an emergent strong-force shape AND scale from MaSt's
geometric structure**.  That's something neither R63 nor any prior
work has done; it would be R64's signature contribution.

The Yukawa exponential cutoff at large r remains as a separate
follow-on question (propagator-based extension), but the
intermediate-r physics — which is where deuteron binding lives —
would be derivable from 7-tensor geometry with one parameter
(σ_t) playing the role of QCD's α_s.

That's a genuinely new kind of result for MaSt, and it lives
within the 7-tensor's existing structure once the kinematic
correction is applied.

### Closing note

Track 7 is currently labelled "structurally encouraging, off by
factor ~2-5" in the findings.  After Phase 7c the label could
upgrade to "right shape and scale at Point B with one empirical
coupling, polynomial form (not Yukawa)."  That's a substantively
stronger claim and worth spending one phase to nail down.

---

## Phase 7c — executed; follow-up needed on full-metric consistency

**What 7c delivered.**  With `A = 4·(ℏc)²` instead of `(ℏc)²`,
the σ_t sweep landed σ_t = −116.1, giving trough depth 50.2 MeV
at r = 1.135 fm — inside the observed NN-potential band.  pn
deeper than pp by 18.9 MeV (Ma-side at Point B), charge symmetry
preserved, Coulomb tail correct.  All four acceptance criteria
met.  Track 7 has the right shape AND right scale at intermediate
r with one empirical cross-shear σ_t.

**One structural concern 7c didn't address.**  σ_t is dimensionless
in the same way R60's metric entries are.  Compare:

| Entry | Value | Channel |
|:---|---:|:---|
| σ_ta (R60 EM) | √α ≈ 0.0854 | p-tube → aleph → S |
| σ_t (7c strong) | −116.1 | p-tube → S directly |

σ_t is **~1360× stronger** than σ_ta.  R60's architecture routes
ALL Ma↔S coupling through aleph; 7c's σ_t bypasses aleph
entirely.  This is either (a) a legitimate new metric channel
(strong force as a separate Ma↔S pathway from EM), or (b) a
phenomenological effective coupling that doesn't correspond to a
real metric entry.  7c didn't distinguish between these.

**At single-particle k_S = 0, σ_t vanishes** (the cross-coupling
term is `2·k_S·σ_t·n_pt·ℏc`, linear in k_S).  So single-proton
calibration is unaffected at leading order.  But Schur-complement
dressing of compound modes could leak σ_t into observables that
R60 already pinned, particularly α universality across the e and
p sheets.

### Next steps (suggestions)

**Phase 7d — full 11D consistency check.**  Add σ_t = −116.1 to
the R60 11D metric as an extra off-diagonal entry between
p-tube and S spatial.  Check:

1. **Signature** — still one negative eigenvalue?
2. **Single-particle masses** — m_e, m_p, m_n, m_ν₁ unshifted
   at model-F precision?
3. **α universality** — composite α across (e, p) still equal
   to 1?  (R60 T7c is the comparison.)
4. **R60 T19 inventory** — 13 hadrons still inside width-
   weighted envelopes?

If 7d passes all four: σ_t is a legitimate new metric channel,
analogous to SM's SU(3) × U(1) separation.  R64 then has
identified a structural parameter (the strong coupling) that
extends R60's architecture without breaking it.

If 7d fails at step 3 or 4: σ_t doesn't sit cleanly in the 11D
metric.  Two readings to investigate:

- **σ_t needs its own auxiliary dimension** (analog of aleph
  for the strong channel).  This would be a genuine new
  architectural piece — extra compact dimension for strong
  force mediation, paralleling aleph's role for EM.
- **σ_t is an effective coupling, not a metric entry.**
  Like QCD's running α_s, it emerges from a more fundamental
  structure but isn't directly a metric off-diagonal.  The
  fundamental mechanism stays open.

**Other open questions visible from 7c:**

- **σ_t structural derivation.**  F7c.4's table showed no clean
  α-relation.  Worth re-checking with Point B's specific
  parameters: σ_t · ε_p ≈ −23.8, σ_t · s_p ≈ −2.9, neither
  particularly natural — but a search over `σ_t · f(ε_p, s_p,
  K_p, n_pt, α)` might surface a structural identity.

- **Yukawa cutoff at large r.**  7b's polynomial form is
  adequate at r ~ 1 fm but lacks the exponential cutoff at r >
  2 fm.  Propagator-based extension is the natural follow-on.
  This sits as a recognized limitation regardless of how 7d
  resolves.

- **Strange-family fit at 7d's augmented metric.**  T4 found
  the strange family doesn't fit at Point B under the single-
  primitive hypothesis.  If 7d works out, the augmented metric
  might shift hadron predictions enough that the strange family
  also re-fits — worth checking.

7c's phenomenological achievement (right shape, right scale at
intermediate r) stands either way.  7d settles the question of
whether σ_t is part of MaSt's structural inventory or an
imported empirical coupling.

---

## Phase 7e — executed; conclusion is conditional, recommend re-run

**What 7e delivered.**  Augmenting R60 model-F's 11×11 metric
with σ_pS_tube ∈ [−0.075, +0.075] (the signature-preserving
band) and computing α_Coulomb across 10 model-F inventory modes
showed that **the sectors are algebraically coupled**: α
deviates symmetrically and quadratically in σ, with different
modes shifting in different directions.  Universality holds
only at σ ≈ 0.  Method and implementation are sound — F7e.1's
baseline reproduction confirms the test setup before the
perturbation enters.

**The negative result is real but the conclusion is
conditional.**  Two unresolved issues weaken the bridge from
F7e's finding to "Yukawa pivot is forced":

### Issue 1 — unit translation never performed

7c's σ_t = −116.1 is in 7-tensor units (multiplies `n_pt · ℏc`
to give a coupling magnitude in MeV²·fm).  R60's 11D σ_pS_tube
is a dimensionless metric component.  The signature band
[−0.075, +0.075] reported by 7e is in 11D units.  **7e never
translates between the two**, so we don't know whether 7c's
σ_t corresponds to:

- A tiny 11D σ_pS_tube (deep inside the band, α perturbation
  negligible)
- A moderate 11D σ_pS_tube (inside band but perturbing α at
  the few-percent level)
- A large 11D σ_pS_tube (outside band, signature breaks)

The "is 7c's coupling safe to integrate?" question is **not
answered** until this translation is done.  F7e.7 acknowledges
the issue but understates its weight: the entire model-G
integration question hinges on which case applies.

### Issue 2 — test modes are model-F, not R64

7e's 10 test modes use R60 model-F tuples — proton at
`(0, 0, 0, 0, 1, 3)`, etc.  R64's u/d picture has the proton at
`(0, 0, 0, 0, 3, +2)` and the neutron at `(0, 0, 0, 0, 3, −2)`.

These are different objects with different `(n_et − n_pt +
n_νt)²` values.  7e is structured as a model-F regression test
("does adding σ_pS_tube break α at model-F's assignments?")
which is **the right question for "model-G must not regress
model-F"** — but **not the test of whether α universality
survives at R64's own frame**.  The latter is a separate
question that 7e doesn't address.

### Issue 3 — companion-entry prescription not enumerated

F7e.6 correctly identifies that σ_pS_tube might need a
structural prescription (analog of σ_ra = (s·ε)·σ_ta) — either
derived from existing α-architecture or via companion entries
that cancel the perturbation.  Neither is computed.  The
quadratic-in-σ deviation pattern (F7e.3) is actually a
Schur-complement-style mixing signature, suggesting companion
entries at second order could cancel it.  This is a real
structural lead that 7e left on the table.

### Recommended re-run (Phase 7e′ or 7e supplement)

Before pivoting to Yukawa or declaring the metric route closed,
two short follow-ups should sharpen 7e's conditional finding
into a definitive one:

**(i) Unit-translation calculation.**  Derive the dimensionless
11D σ_pS_tube that produces the same mass-formula coefficient
at compound (6, ±4) modes as Phase 7c's σ_t = −116 in 7-tensor
units.  Concretely: compute the cross-coupling correction to
m²((6, +4)) two ways — once via 7c's `2·k_S·σ_t·n_pt·ℏc` form
and once via the augmented 11D metric's Schur-complement
expansion at the same k_S — and solve for the σ_pS_tube value
that makes them equal.  Then locate that value in 7e's
[−0.075, +0.075] band.  Output: a single number, ~hours of
work, settles whether 7c's coupling is safely small or
problematically large in 11D units.

**(ii) Re-run 7e at R64 Point B with R64's u/d inventory.**
Replace 7e's 10 model-F test modes with R64's u/d compounds:
proton `(0, 0, 0, 0, 3, +2)`, neutron `(0, 0, 0, 0, 3, −2)`,
deuteron `(0, 0, 0, 0, 6, 0)`, the relevant mesons.  Use Point
B parameters `(ε_p, s_p, K_p) = (0.2052, 0.0250, 63.629)`.
Re-sweep σ_pS_tube and check α-universality across the R64
inventory.  Output: same kind of table as F7e.3, but
addressing R64's actual frame.  ~hours of work, single-script
extension of the existing 7e script.

**(iii) Companion-entry search (optional).**  If (i) places
7c's σ_t inside the band and (ii) shows the same coupling
pattern at R64 inventory, the next question is whether
companion entries (additional off-diagonal pairs) can cancel
the quadratic α-perturbation at second order.  The shape of
the deviations in F7e.3 is the input — if α(electron) rises
while α(proton) falls at the same σ, the companion needs to
oppose the e-sheet contribution to G⁻¹[Ma, t] specifically.
This is more involved (multi-day) but the F7e.3 data already
encodes the constraint; it's "solve for companion entries"
rather than "blind search."

### Net read

The "sectors are coupled" structural finding stands.  But
"σ_pS_tube needs structure" is a CONDITIONAL conclusion at the
moment, not an absolute one — conditional on 7c's σ_t
corresponding to a non-trivial 11D entry, and conditional on
the same coupling pattern existing at R64's frame.  Both
conditions are testable with short follow-ups.

Steps (i) and (ii) collectively determine whether the model-G
integration question is "find the structural prescription for
σ_pS_tube" (if 7c's coupling is large enough to need it) or
"σ_pS_tube is small enough that R60 stays effectively intact"
(if 7c's coupling is well below the band's threshold).  Either
outcome is informative.

The Yukawa pivot suggested in F7e.6 is a viable separate route,
but with the unit-translation gap unresolved, choosing it now
would forfeit information that 7e′ would surface cheaply.

---

## Phase 11 — re-run with QM gate; key claims need to walk back

Track 11 is presented as fully rescuing the metric route to the
strong force.  The findings claim "the strong force lives in the
11D metric" (F11c.5), "Pool item m is unforced" (F11c.5 #2), and
"no new formalism required" (Track 11 net result).  These are the
biggest claims in any R64 track, and they don't survive the
checks Track 7 already established.

### Concern 1 — Phase 7d's QM disqualifier was never re-applied

Phase 11c's V(r) is *numerically identical* to Phase 7c's by
construction (F11c.3: "Phase 7c was right all along; σ_t = −116
was exactly the Schur σ_eff_tube at the σ_pS_tube + H2 signature
edge").  This is presented as a positive — the metric reproduces
the trough.  It is also a problem: Phase 7d already solved Phase
7c's V(r) as a Schrödinger problem and found:

- 3 bound states in pn (vs 1 deuteron observed)
- nn and pp both bound (vs unbound in nature)
- B(²H) = 30 MeV (vs 2.22 MeV — factor 13.5 too deep)
- a_s wrong sign (+22 fm vs −23.7 fm)

A V(r) that produces the same eigenvalue spectrum as Phase 7c's
V(r) inherits the same QM failures.  Track 11 does not re-run
Phase 7d on the metric-derived V(r); it doesn't acknowledge the
prior result; the verdict "Pool item m is unforced" follows from
"static trough matches" alone.  That inference is unsound.

What 11c actually demonstrates is *the static-potential trough is
reproducible from the metric*.  That is genuinely informative and
worth keeping.  But it does not show the metric formalism is
"complete" for the strong force, because the actual physical
disqualifier in Track 7 lived at the QM level, not the static
level.

### Concern 2 — pp/nn binding contradicts observation

F11c.2 reports V_min(pp) = −32.3 MeV and V_min(nn) = −32.7 MeV
and frames this as "charge-symmetric" ✓.  Charge symmetry is
preserved at the σ-coupling level, but the underlying claim is
that the metric reproduces the strong force, and nature has both
nn and pp unbound.  Reproducing depth ≈ 32 MeV in the nn channel
isn't a victory; it's a quantitative disagreement with
observation that the QM gate (Concern 1) would surface
immediately.  The findings don't flag it.

### Concern 3 — Phase 11e mis-labels extreme sensitivity as "stable"

The 11e CSV (track11_phase11e_point_b_stability.csv) shows
V_min(pn) sweep across (ε_p, s_p) near Point B:

| ε_p | V_min(pn) (MeV) |
|:-:|:-:|
| 0.18 | **+214** |
| 0.19 | +101 |
| 0.2052 (Point B) | −50 |
| 0.21 | −93 |
| 0.22 | −178 |
| 0.23 | **−255** |

Spread = 469 MeV across a 12% ε_p range.  The script's stability
threshold (5 MeV) is generous by two orders of magnitude relative
to the actual variation.  The verdict "stable around Point B" is
incompatible with these numbers.  The strong-force depth is
**fine-tuned**, not robust — Point B sits on a steep slope where
small parameter shifts move V_min by tens to hundreds of MeV.

### Concern 4 — Phase 11f mass-prediction setup is wrong

11f's CSV reports:

| Particle | Predicted (MeV) | Target (MeV) | Off by |
|:---|:-:|:-:|:-:|
| R64 proton | 5534 | 938.3 | 5.9× |
| R64 neutron | 5542 | 939.6 | 5.9× |
| η | 1841 | 547.9 | 3.4× |
| φ | 2077 | 1019 | 2.0× |

The script uses `track9_params()` (with R60 model-F's L_ring_p =
15.244 fm calibrated for the proton at *(1, 3)*) and feeds R64
tuples *(3, +2)* into `mode_energy`.  R64's mass calibration is
via `K_p · μ` (Track 1 Phase 1b), not via `2π·ℏc / (L · √k)`.
11f mixes the two conventions and produces nonsense masses for
R64 baryons.

The α-attribution test in 11f is independent of L_ring_p (it
depends only on G⁻¹ structure) and is valid.  But the mass
column is methodologically broken and is not flagged in the
findings.  As written, "full hadron inventory under the new
strong-force architecture" has not been validated; only the
α-attribution piece has.

### Concern 5 — F11d's structural-form claim mixes derivation and speculation

Phase 11d derives `b = −√α / k_p` from a clean first-order
perturbation argument.  This part is solid and matches Phase 9b's
empirical −1.81892 to 6 sig figs.  The findings then promote a
second boxed form `b = −8π·√α / 2^(1/4)` based on the observation
that R60's empirical k = 1.1803/(8π) is "within 0.75% of
2^(1/4) = 1.18921".

A 0.75% match is not a derivation.  The 2^(1/4) form would predict
b ≈ −1.8054, which Phase 9b's 6-sig-fig result (−1.81892) would
have caught as a 0.75% deviation — and did, by giving a different
answer.  The findings text says "agreeing to within the same
0.75%", which acknowledges the disagreement but boxes the
speculation anyway.  This should be hedged or removed; the
empirical k_p form is the supported result.

### Concern 6 — "Edge methodology" deserves scrutiny, not adoption

F11a.4 reports σ_eff_ring climbing as σ_pS_ring approaches the
signature boundary: 0.27, 0.74, 1.5, 2.5, 7.0, 12.6, 24.5, 65.7,
**116, 854**, ... over the last few thousandths of σ_pS_ring.
The metric becomes degenerate at the boundary (one eigenvalue
→ 0); G⁻¹ entries diverge there by definition.  Phase 11c
requires σ_pS_tube tuned to six decimal places (0.125050) to land
σ_eff_tube = 116.

This is the textbook signature of a singular limit.  Two
concerns:

- *Mathematical*: physical observables at a metric singularity
  are not well-defined.  Any value of σ_eff is reachable by
  picking where on the diverging curve you sit; this isn't
  derivation, it's choice of regulator.
- *Empirical*: tiny perturbations in σ_pS_tube (5th decimal)
  produce order-of-magnitude shifts in σ_eff (65 → 116 → 854).
  No physical theory should require parameter precision below
  the noise floor of the input parameters.

Track 10's σ_eff cap of ~1 was characterized as a "measurement
artifact" of taking a "safe distance" from the boundary.  An
equally fair characterization is that staying away from the
singular boundary is what makes σ_eff a *physical observable*
in the first place; pushing toward the boundary makes σ_eff a
*tunable artifact of regulator choice*.  Track 11's headline
σ_eff = 116 result rests on the second framing without
defending it.

### Concern 7 — Track 10 floor results conflated with the σ_eff cap

Track 10 had three substantive findings: 10a (ring-S is α-inert),
10b (aleph cannot be removed; charges collapse without it), and
10c (σ_ra cannot be removed; signature breaks).  Track 11
correctly reverses Track 10's σ_eff-magnitude cap, but the
findings' "Track 10's metric exhausted verdict is fully reversed"
phrasing erases the 10b/10c floor results that are independent
and still stand.  Findings-11.md should preserve this distinction
explicitly.

### What Track 11 has actually established

Strip the over-claims and Track 11 still has real content:

1. **A1 charge attribution** `f(n_pt, n_pr) = n_pt/6 + n_pr/4`
   gives α-universality at machine precision across R64's quark
   inventory.  This is a clean positive (pool item g closed).
2. **Phase 11d's b = −√α / k_p closed form** for the H2
   coefficient, derivable in a few lines of perturbation theory,
   matching Phase 9b numerical to 6 sig figs.  This is structural
   content even without the strong-force claim.
3. **Phase 7c's σ_t = −116 has a metric origin** (Schur σ_eff at
   the σ_pS_tube + H2 signature edge, R64 Point B).  The
   *static-potential* trough is reproducible from the metric.

These three results are worth keeping.  What needs to walk back:

- "Strong force lives in the metric" → "static trough is
  reproducible; QM observables not yet checked at the new
  configuration."
- "Pool item m is unforced" → still forced, until the QM gate is
  re-applied.
- "Metric formalism is complete" → not established; Phase 7d-style
  validation on Phase 11c's V(r) is the missing test.

### Recommended re-runs

1. **Apply Phase 7d's Schrödinger machinery to Phase 11c's V(r)**.
   The V(r) is numerically the same as Phase 7c's, so the
   eigenvalue spectrum should be the same (3 bound states in pn,
   bound nn/pp, B(²H) ~ 30 MeV).  If so, F11c.5 needs to walk
   back; if surprisingly different, that's a new result worth
   investigating.
2. **Fix Phase 11f to use K_p · μ for masses** at R64 tuples, then
   re-run the inventory.  Report whichever masses survive at Point
   B; make the inventory check honest.
3. **Re-frame Phase 11e** with the actual V_min(pn) spread (~470
   MeV) and consider whether it disqualifies "structural"
   language for Point B.
4. **Trim F11d.1** to the supported `b = −√α / k_p` derivation
   and either drop or hedge the 2^(1/4) speculation.
5. **Address Concern 6 explicitly** — characterize whether σ_eff at
   the signature boundary is a physical observable or a
   regulator artifact.  This matters because Track 11's headline
   result depends on the answer.

### Net read

Track 11 contains real findings worth preserving (A1, the H2
closed form, the Schur identification of σ_t = −116).  But the
narrative around them — "metric formalism is complete", "strong
force is in the metric", "pool item m is unforced" — outpaces
what was actually demonstrated.  The QM gate that disqualified
the metric V(r) in Track 7 was never reapplied; until it is, the
disqualifier still applies.  The track needs a re-run pass with
the QM gate restored before the architectural claims can stand.
