# Q132: The promotion-chain principle — phase-locked 2π closures and the (bright, dark, multiple) typology of modes

**Status:** Open — working hypothesis, **v2 (refined)**.
Proposes a foundational principle that unifies R33's empirical
"n_tube = ±1" rule, the order-of-compactification framework
(Q127), and the ghost-suppression behavior exposed by R63
Tracks 1–4.  Not yet derived from GRID axioms; formalization
is an R62 derivation target.

**Related:**
  [Q127](Q127-orders-of-compactification.md) (orders of compactification),
  [Q128](Q128-detecting-compact-universe.md) (α as leakage rate),
  [Q130](Q130-non-standing-photons-in-t6.md) (non-standing photons in T⁶),
  [Q131](Q131-dark-energy-as-unpromoted-information.md) (dark energy as unpromoted information),
  [R33](../studies/R33-ghost-selection/) (ghost-mode selection),
  [R60 T16](../studies/R60-metric-11/findings-16.md) (Z₃ confinement on p-sheet),
  [R60 T17](../studies/R60-metric-11/findings-17.md) (e-sheet Z₃ exemption),
  [R60 T18](../studies/R60-metric-11/findings-18.md) (ν-sheet charge = 0),
  [R62 Program 1](../studies/R62-derivations/) (electron from light),
  [R63](../studies/R63-proton-tuning/) Tracks 1–6 (ghost audits and refinement).

---

## 0. Brief history

**Q132 v1 (initial draft, now superseded).**  The original
formulation asserted per-sheet rules:
(a) charge requires both `n_tube ≠ 0` AND `n_ring ≠ 0` on the
*same* sheet; (b) `|n_tube| ≥ 2` is forbidden as a single
particle (multi-event rule), allowed only via sheet-specific
binding (Z₃ on p, T18 pairing on ν).  This successfully cleaned
the pure-e-sheet ghost tower (R63 Track 4), but applied to
R60 T19's compound-mode inventory it flagged 9 of 19 particles
as Q132-incompatible on their e-sheet — forcing speculative
"e-sheet binding mechanism" rescues.  v1 was **too restrictive**:
it forbade modes that phase-cancellation naturally handles
without invoking a new binding mechanism.

v2 below replaces the per-sheet forbidding with a cleaner
gcd-based classification: multi-event modes decompose into
bright copies of a primitive, or are *dark* (mass-only) when
the primitive's two windings don't phase-lock.  Every v1
conclusion that used mode enumeration or dark-mode reinterpretation
still holds under v2.

---

## 1. The principle

**Each compact dimension promotes its input to the next-order
observable.  A 2π closure is one promotion event.  A second
axis can receive a promotion from the same photon only when its
own 2π completes in phase with the first.**

The three levels at work in model-F:

| Level | Compact structure | Input | Output |
|:-----:|:-----------------:|:------|:-------|
| 0 | — (non-compact) | — | raw information / phase |
| 1 | aleph (S¹) | information | **light / energy** (photon) |
| 2 | ring (first T² cycle) | energy | **mass** |
| 3 | tube (second T² cycle) | mass | **charge** |

On a single sheet the tube and ring are the two cycles of a
T² torus.  Both can promote a trapped photon at once — energy
becomes mass via the ring, mass becomes charge via the tube —
but only if the two 2π closures are **phase-locked**: the
ring must have completed an integer number of cycles at the
moment the tube first closes.  This is the central added
content of v2.

## 2. Physical mechanism — first-closure promotion

Consider a single-sheet mode `(n_t, n_r)` tracing a closed path
on the sheet's T².  As the path advances, tube and ring phases
wind at rates proportional to `n_t` and `n_r`.  The path's full
primitive period closes after the tube has wound `n_t` times
and the ring `n_r` times.

**At the first 2π tube closure** (1/n_t of the way through the
primitive period) the ring phase is `2π · (n_r/n_t)`.  Two
cases:

- **Integer ratio** (`n_t | n_r`, i.e., the ring has completed
  an integer number of 2π closures at that moment).  The tube's
  promotion from mass to charge has a fully formed mass quantum
  (supplied by the ring) to act on.  Charge emerges.  Bright.
- **Non-integer ratio.**  The tube closes without the ring
  having completed its own 2π, so there is no clean mass
  quantum available to be promoted.  The promotion fails at
  first closure and the mode settles as mass only.  **Dark.**

The picture is one-shot: the *first* closure decides.  If
charge fails to fire at the first tube 2π, it cannot recover
at later closures because the phase relationship is fixed by
the winding ratio, not by opportunity.

## 3. Mathematical form — the ω-sum

The first-closure story is equivalent to a cumulative
phase-sum that gives the same classification.  At each tube
closure `j = 1 … n_t` the charge contribution has phase
`exp(i · 2π · j · n_r / n_t)`.  Total charge:

<!-- Q_net = Σ_{j=1}^{n_t} exp(i · 2π · j · n_r / n_t) -->
$$
Q_{\text{net}} \;=\; \sum_{j=1}^{n_t} e^{\,i\,2\pi\,j\,n_r/n_t}
$$

Letting ω = exp(i · 2π · n_r/n_t):

- If **ω = 1** (equivalent to `n_t | n_r`): every term is 1,
  `Q_net = n_t`.
- If **ω ≠ 1**: the geometric series collapses using
  `ω^(n_t) = exp(i · 2π · n_r) = 1`, giving
  `Q_net = ω · (1 − ω^(n_t)) / (1 − ω) = 0`.

The ring's phases at successive tube closures form the n_t-th
roots of unity, which sum to zero.  **Charge either adds
coherently (ω = 1) or cancels exactly (ω ≠ 1).  There is no
intermediate.**

Both views are equivalent; the first-closure view is a
one-shot decision rule, the ω-sum view is the same decision
expressed as exact cancellation across all closures.

## 4. Classification of single-sheet modes

Reduce `(n_t, n_r)` by gcd to its primitive `(p_t, p_r)` with
`gcd(p_t, p_r) = 1`; the original mode is `k` copies of the
primitive where `k = gcd(|n_t|, |n_r|)`, and `μ(n_t, n_r) = k ·
μ(p_t, p_r)` exactly.

| Primitive | Result | Multiplicity | Classification |
|:--:|:--|:--:|:--|
| `(0, 0)` | nothing traps | — | no particle |
| `(0, p_r ≠ 0)` | ring traps photon → mass; no tube → no charge promotion | k | **neutral massive particle (ring-only)** |
| `(p_t ≠ 0, 0)` | tube closes but no ring-supplied mass to promote | k | **neutral massive particle (tube-only, self-mass)** |
| `(±1, p_r ≠ 0)` | one tube closure with ring at integer phase → charge fires | k | **k bright charged particles** |
| `(p_t, p_r)` with \|p_t\| > 1, gcd=1 | first tube closure finds ring off-integer → charge fails; ω-sum cancels | k | **k dark massive particles (mass only, Q = 0)** |

### Worked examples

| Mode | gcd | Primitive | Result |
|:---:|:---:|:---:|:---|
| (1, 2) | 1 | (1, 2) | 1 charged particle (electron on e-sheet) |
| (1, 15) | 1 | (1, 15) | 1 charged particle (tau on e-sheet) |
| (2, 4) | 2 | (1, 2) | 2 charged particles (2 electrons) |
| (3, 6) | 3 | (1, 2) | 3 charged particles (on p-sheet, 3 quarks via Z₃) |
| (2, 3) | 1 | (2, 3) | 1 dark massive particle (ω = e^(i3π) ≠ 1) |
| (3, 2) | 1 | (3, 2) | 1 dark massive particle |
| (4, 6) | 2 | (2, 3) | 2 dark massive particles |
| (3, 5) | 1 | (3, 5) | 1 dark massive particle |
| (0, 5) | 5 | (0, 1) | 5 ring-only neutrals — or equivalently one 5-ring-wound neutral (no tube interaction to distinguish) |
| (1, 0) | 1 | (1, 0) | 1 tube-only neutral |

The gcd reduction is a mathematical identity (not an
interpretation choice): the μ-value of any non-primitive mode
is an exact integer multiple of its primitive's μ-value.  The
physical meaning of k-multiplicity depends on binding:

- No binding (e-sheet) → k separate free particles in the
  observed spectrum.  E.g., (2, 4) on e-sheet means "2
  electrons," not a new |Q| = 2 particle.
- Binding mechanism available (p-sheet Z₃, ν-sheet T18) →
  k bound constituents of a composite.  E.g., (3, 6) on
  p-sheet means "3 quarks bound into a baryon."

## 5. Compound modes and cross-sheet charge arithmetic

A compound mode has a winding pair `(n_t, n_r)` on each of the
three sheets.  Classify each sheet's contribution by the
section-4 table, then sum charges:

<!-- Q_compound = Q_e + Q_ν + Q_p -->
$$
Q_{\text{compound}} \;=\; Q_e \;+\; Q_\nu \;+\; Q_p
$$

with per-sheet contribution:

- **Bright primitive `(±1, p_r ≠ 0)`, k copies:** contributes
  `±k` units of charge (sign fixed by the sheet's tube
  direction convention).
- **Dark primitive (\|p_t\| > 1, gcd = 1):** contributes 0 (Q_net
  cancels by ω-sum).
- **Tube-only `(±1, 0)`, k copies:** contributes 0 (no ring
  → no mass quantum to promote).
- **Ring-only `(0, p_r ≠ 0)`, k copies:** contributes 0 (no
  tube event).
- **Null `(0, 0)`:** contributes 0.

The ν-sheet has an additional reduction: R60 T18's real-field
conjugate-pair averaging zeroes the ν-sheet's charge
contribution regardless of windings.  So effectively
`Q_ν = 0` always for the neutrino sheet.

This produces `Q_compound` as a single integer matching the
particle's observed charge.  A compound with all-dark sheets
is valid and is a **massive neutral particle** — mass from
ring-trapped photons on one or more sheets, charge zero by
phase cancellation on each.

## 6. Discipline constraint for model-building

A correct rule for charged particles must satisfy:

1. **Every observed charged particle is predicted** at the
   nearest v2-allowed bright mode.  Exact agreement is expected
   for stable and long-lived particles.  Short-lived (ephemeral)
   particles may sit a little above their nearest allowed mode;
   that offset is the particle's echo-from-underlying-mode
   signature and is expected to scale with the particle's
   ephemerality (pseudo-Goldstone behavior on the p-sheet,
   routing-dominated decay on the e-sheet lepton ladder).
2. **No stable unobserved charged particle is predicted.**
   Predicted bright modes that don't correspond to observed
   stable leptons or hadrons are interpreted as short-lived
   resonances (routing-suppressed per R56/R57); v2 predicts
   their masses, and experimental non-observation as stable
   states is consistent with that reading.

Dark particles are unconstrained by current observation — any
number of dark modes may accumulate as predictions without
conflict, and they form a natural dark-matter / dark-resonance
candidate catalog (consistent with R42's framing).

v2's bright/dark split is built around this asymmetry:
predicted brights must correspond to observed particles (exactly
for stable ones, with an ephemerality offset for unstable ones);
predicted darks are free.

## 7. What v2 explains

### a. R33's empirical "n_tube = ±1" rule — still derived

R33 observed from the charge formula that real charged
particles have `|n_tube| = 1` on their active charged sheet.
Under v2 this is a corollary of the bright condition: any
primitive charged mode requires `|p_t| = 1`.  Multi-event
modes with `|n_t| > 1` either decompose (gcd > 1 → k electrons
on e-sheet) or phase-cancel (gcd = 1 → dark).  In both cases
no new `|Q| > 1` fundamental particle is produced from a
single e-sheet mode.

### b. Z₃ confinement on the p-sheet — natively compatible

The (3, 6) proton has gcd = 3 on the p-sheet, decomposing
into 3 × (1, 2) primitives.  Each primitive is a bright
charged strand — a quark with tube winding 1.  Z₃
confinement is the binding mechanism that holds the 3
strands together; v2 provides the strand-counting
(gcd decomposition).  Z₃ remains an independent structural
rule, but it now sits on top of a general gcd framework
rather than as a one-off exception.

### c. R63 Track 4 e-sheet ghost tower — dissolved

The (2, 4), (3, 6), (4, 8) "ghost tower" at multiples of m_e
was the motivating finding.  Under v2 these modes have
primitive (1, 2) (= electron) with multiplicity 2, 3, 4 — so
they are not new particles but 2, 3, 4 electrons.  Because
the e-sheet has no binding mechanism, these scatter as free
electrons rather than forming composites.  No new particles
are predicted; the ghost tower is gone.

### d. Multi-event dark modes — a new positive prediction

Modes with gcd = 1 and `|n_t| > 1` like `(2, 3)`, `(3, 2)`,
`(3, 5)`, `(5, 2)` are genuine particles in v2 — they have
mass (from the trapped EM energy) but zero charge (by ω-sum
cancellation).  These populate the **dark-mode catalog**
alongside ring-only and tube-only neutrals.  R42's dark-
matter framing naturally absorbs them.

### e. Compound all-dark modes — permitted

A compound whose every active sheet is primitively dark is a
valid heavy neutral particle.  R60 T19 tupled φ and ρ with
sheets that are all primitively dark under v2; this is
consistent with their observation as neutral vector mesons.
Whether these are the *correct* tuples for φ and ρ is a
separate question to be settled inside R63.

### f. ν-sheet (1, 0) — reinterpreted as tube-only neutral

The flagged ν-sheet ghost at `(n_νt, n_νr) = (1, 0)` is a
tube-only neutral under section 4 — a valid sterile-neutrino
candidate, not a ghost.  (R60 T18's charge-zero rule is
independent; it applies after v2 classification.)

## 8. Open questions and derivation targets

1. **Why does the first tube closure decide?**  The asymmetry
   between "failed at first closure → dark" vs "successful
   at first closure → charged, and subsequent closures
   contribute copies" deserves derivation from the underlying
   dynamics.  The ω-sum gives the same answer but via
   cumulative cancellation; a proof that these two pictures
   are equivalent at the level of GRID dynamics is an R62
   target.

2. **Why is a 2π tube closure one "promotion event"?**  GRID
   A6's "α as coupling per 2π" is consistent but not a proof.
   An R62 derivation from GRID axioms → KK reduction →
   "each 2π emits one quantum" would formalize the base unit.

3. **What sets the tube-vs-ring role?**  v2, like v1, relies
   on the sheet's shear geometry to designate which cycle is
   the "charge counter" and which the "mass counter."  A
   derivation of the role designation from shear magnitude is
   open.

4. **Is R60 T18's ν-sheet charge zero derivable from v2?**
   Currently it is an independent architectural feature.  If
   the real-field conjugate pairing on the ν-sheet is itself
   a consequence of the promotion chain (e.g., a symmetry of
   how ν's aleph maps to its ring), then the theory is
   unified; otherwise T18 remains a separate rule.

5. **Does the ω-sum generalize to more than one tube event per
   sheet with binding?**  Z₃ on the p-sheet handles k = 3
   strand binding; its generalization to larger k (nuclei with
   `n_pt = 3A, n_pr = 6A`) is already used empirically.  A
   clean statement of "bright multiplicity k is bound into one
   composite when a k-ary binding exists" is worth writing
   down explicitly.

## 9. Status and next steps

This Q file captures the principle; it does not derive it.

**Path to formalization:**

- A **new R62 derivation** (Program 2, "Promotion-chain
  principle — v2") starting from GRID axioms, KK reduction,
  and the phase-lock condition, producing as output:
  (a) the first-closure decision rule as a theorem,
  (b) the ω-sum as its mathematical form,
  (c) the shear-determined role asymmetry,
  (d) the typology of Section 4,
  (e) the compound charge arithmetic of Section 5.

- **Empirical validation** inside R63: Tracks 5 and 6 apply v2
  to the e-sheet landscape and the compound-mode inventory
  respectively.  Both passed under the §6 discipline reading:
  v2 predicts every observed charged particle at the nearest
  v2-allowed bright mode (exactly for stable particles; with an
  ephemerality offset for short-lived ones), and every predicted
  bright mode without an observed stable counterpart falls into
  the routing-suppressed short-lived-resonance interpretation.

- **Comparison with Q131's unpromoted-information proposal**:
  both Q131 (dark energy as unpromoted aleph information) and
  this principle (particle species as promotion results)
  share the same "promotion" framework and may unify under a
  single theory of compact-dimension physics.

## 10. Why this matters

If correct, the principle:

- Turns `|n_tube| = ±1` from an empirical rule into a
  **corollary** of the phase-lock condition;
- Explains **why particles are discrete** (each 2π = one
  event) and **why some are dark** (phase-cancellation when
  the primitive windings don't lock);
- Unifies **Z₃ confinement** (p-sheet), **winding restriction**
  (e-sheet), and **charge-zero pairing** (ν-sheet) under a
  single gcd-based counting rule;
- Converts the **R63 ghost list** from an architectural
  problem into a **predictive catalog** of dark and sterile
  states, with the bright catalog disciplined to match the
  observed charged inventory (exactly for stable particles;
  within each short-lived particle's ephemerality envelope);
- Provides a concrete tuple-validity filter (`n_t | n_r` for
  any sheet that is supposed to contribute charge) that
  focuses the search space for compound-mode tuples without
  introducing new binding mechanisms.

If wrong, v2's concrete predictions (the bright catalog must
match every observed charged particle, no more and no fewer)
make it falsifiable with the existing inventory, not with
speculative future observations.
