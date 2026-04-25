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
