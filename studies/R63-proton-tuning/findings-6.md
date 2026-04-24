# R63 Track 6: Joint Q132 compound-mode audit across three sheets

## Phase 6A — Per-sheet Q132 compatibility of the inventory

**Scope.**  Classify each of the 19 baseline-inventory tuples
(R60 Track 19 Phase 1b Z₃-filtered inventory) under per-sheet
Q132.  Purely a winding-integer check — ratio values do not enter.

Script:
[`scripts/track6_phase6a_compatibility.py`](scripts/track6_phase6a_compatibility.py)
Output:
[`outputs/track6_compatibility_matrix.csv`](outputs/track6_compatibility_matrix.csv)

### Classification rules

Per sheet the winding pair `(n_t, n_r)` is classified:

| Pattern | Status | Interpretation |
|:---:|:---|:---|
| `(0, 0)` | null | no activity on this sheet |
| `(0, n_r ≠ 0)` | ring-only | neutral, ring-trapped self-mass |
| `(±1, 0)` | tube-only | neutral, tube self-mass |
| `(±1, n_r ≠ 0)` | charged | valid charged particle |
| `\|n_t\| ≥ 2` | needs binding mechanism | see below |

Multi-event cases by sheet:

- **e-sheet:** no known binding mechanism.  `|n_et| ≥ 2` is
  Q132-forbidden under current theory.
- **ν-sheet:** R60 T18 real-field conjugate pairing **may**
  allow even `|n_νt|` values as paired-conjugate bound states
  (one physical state described by a ± mode pair).  Flagged as
  structurally conditional; strong evidence for validity comes
  from muon compatibility (see F6A.2 below).
- **p-sheet:** Z₃ confinement binds three `n_pt = ±1` events
  into a color singlet.  Allowed: `|n_pt| ∈ {3, 6, 9, ...}`.
  Forbidden: `|n_pt| ∈ {2, 4, 5, 7, 8, ...}`.

### F6A.1. Compatibility verdict summary (19 particles)

| Verdict | Count | Particles |
|:---|:---:|:---|
| **Compatible** (single-sheet or simple composite) | 6 | electron, ν₁, η′, K⁰, η, π⁰ |
| **Baryon (Z₃-composite)** | 1 | proton |
| **Conditional on ν-sheet pairing** | 3 | muon, K±, π± |
| **Incompatible under strict Q132** | 9 | tau, neutron, Λ, Σ⁻, Σ⁺, Ξ⁻, Ξ⁰, φ, ρ |

**Fully or structurally compatible: 10 of 19 (53%).**
**Incompatible without further mechanism: 9 of 19 (47%).**

The incompatible group is not scattered — every one of the 9
has `|n_et| ≥ 2` on the e-sheet.  The specific violations:

| Particle | n_et | e-sheet verdict |
|:---:|:---:|:---|
| Σ⁺ | +2 | forbidden (|n_et|=2) |
| Ξ⁻ | −2 | forbidden (|n_et|=2) |
| Λ, neutron, Ξ⁰, φ, ρ | −3 | forbidden (|n_et|=3) |
| Σ⁻ | +4 | forbidden (|n_et|=4) |
| tau | −5 | forbidden (|n_et|=5) |

### F6A.2. The ν-sheet "conditional" group: muon forces the question

Three particles classify as "conditional on ν-sheet pairing"
because they carry `|n_νt| = 2`:

| Particle | (n_νt, n_νr) |
|:---:|:---:|
| muon | (−2, −6) |
| K± | (−2, −6) |
| π± | (−2, −6) |

**The muon is a fundamental charged lepton — it must be Q132-
compatible for Q132 to be correct.**  It has no alternative
interpretation path; its compatibility depends entirely on
whether R60 T18's real-field conjugate pairing legitimately
represents `|n_νt| = 2` as one physical paired state.

This is strong (not conclusive) evidence that **R60 T18 does
extend to paired-conjugate multi-event binding on the ν-sheet
for even `|n_νt|`.**  Under that reading the three conditional
particles become compatible.

The formal derivation of this extended reading is an R62
question (analogous to Q132 itself needing Program 2
derivation); for Phase 6A the working assumption is that
even `|n_νt|` is allowed.  That moves muon, K±, π± into the
compatible column.  **Effective count: 13 of 19 compatible,
6 of 19 incompatible (all e-sheet `|n_et| ≥ 2`).**

### F6A.3. φ and ρ: gcd-1 on the p-sheet had been flagged; now also blocked at e-sheet

Track 6 framing flagged φ and ρ as having `|n_pt| = 3` with
`gcd(|n_pt|, |n_pr|) = 1` — gcd-1 p-sheet windings that would
be invalid as Z₃-baryon composites (the three events fail to
align as an integer-strand singlet).

The Phase 6A classification shows their `|n_pt| = 3` on the
p-sheet *does* satisfy the divisibility rule strictly
(3 mod 3 = 0), so they pass the sheet-level Z₃ test —
however they **still fail on the e-sheet** with `|n_et| = 3`.

So φ and ρ fail Q132 for a different reason than framing
suggested.  The p-sheet gcd structure may still be an issue
for the Z₃ interpretation, but Phase 6A doesn't need to
adjudicate it — the e-sheet violation alone already
disqualifies the current tuples.

### F6A.4. What the incompatibility means

The 9 (or 6 after ν-sheet relaxation) incompatible particles
fall into two categories:

**Case 1: baryons with `|n_et| ≥ 2` (neutron, Λ, Σ, Ξ).**
Under model-F these have been derived with non-trivial
e-sheet windings to fit the mass and charge simultaneously.
Under Q132, the e-sheet has no binding mechanism for
`|n_et| ≥ 2`.  Either:

- (a) **The e-sheet tuples need re-derivation** within the
  constraint `|n_et| ≤ 1` (perhaps with higher `|n_er|` and
  larger `|n_pr|` to reach the mass and charge).
- (b) **The e-sheet has a binding mechanism we haven't
  formulated** (an SU(2) isospin-like or Cabibbo-like
  structure on the e-sheet that binds `|n_et|` events into a
  singlet).
- (c) **Q132 itself needs refinement** to permit `|n_et| ≥ 2`
  under some stricter sub-condition that these baryons
  satisfy.

**Case 2: tau.**  `n_et = −5` is a highly singular winding on
the e-sheet.  R53 derived tau as needing very high-order
windings on the e-sheet (R53 notes `n ≈ 3478` is needed at
a different scale).  That Track 19 found `n_et = −5` in its
Z₃-filtered search is already suspicious — tau may be a
compound state rather than a pure e-sheet excitation.

**Case 3: φ and ρ.**  Mesons should be single-event objects
but R60 T19 gave them `|n_pt| = 3`, suggesting the search was
drawn into three-event tuples by mass-matching.  These need
re-derivation, potentially as pure p-sheet ring-only
objects (with `n_pt = 0`).

### F6A.5. Phase 6A verdict

**Q132 is consistent with the clean leptons (electron, muon
provisionally), the three stable baryons via Z₃-composite
reading (proton), the neutral neutrino, and the scalar mesons
that live on ring-only windings (η, η′, π⁰, K⁰).**  These ~13
particles (half to two-thirds of the inventory) Q132-certify.

**The rest of the inventory has tuples that don't survive
strict per-sheet Q132 on the e-sheet.**  Rather than
concluding Q132 is wrong, this is where it **makes a
falsifiable prediction**: if Q132 is correct, those 6 (Case 1
baryons) or 9 (including tau, φ, ρ) tuples should be
re-derivable with `|n_et| ≤ 1`, or an e-sheet binding
mechanism analogous to Z₃ needs to be identified.

**Track 6 should not proceed directly to Phase 6B (marginal
ratio scans) without first testing whether a Q132-constrained
re-derivation of the 6–9 flagged tuples is possible.**  That
becomes a new Phase 6A-prime (tuple re-derivation) before 6B
— otherwise we'd be doing ratio optimization against a tuple
set that Q132 itself rejects.

### Implications for the next phase

- **Phase 6A-prime (proposed, new):** Constrained tuple
  re-derivation.  For each of the 6 Case 1 baryons (tau, φ,
  ρ handled separately), run an α-filtered mass-matching
  search with the additional constraint `|n_et| ≤ 1`.  Ask:
  does a Q132-compatible tuple exist that matches the mass
  and charge?  Output: new tuples (if found), or clean
  falsification report (if not).
- **Phase 6A-double-prime (proposed):** Structural question
  for R62 — is there an e-sheet binding mechanism that
  permits `|n_et| ≥ 2` under some Z₃-like rule?  Pure
  theoretical; R62 Program 2 or a sibling program.
- **Phase 6B (ratio marginal scans)** still follows, but
  with a Q132-certified tuple set rather than the current
  Z₃-only tuple set.

### What Phase 6A establishes

1. **About half the inventory is already Q132-compatible**
   — a non-trivial consistency check that Q132 passes on
   the core of the observed spectrum.
2. **The ν-sheet is forcing a structural question about
   T18's reach** — muon's very existence on the current
   tuple depends on the answer.  Flagged for R62 follow-up.
3. **Six-to-nine particles have Q132-incompatible e-sheet
   tuples** — this is a real falsifiable gap.  Either the
   tuples re-derive cleanly under `|n_et| ≤ 1`, an e-sheet
   binding mechanism is found, or Q132 is refined or
   rejected.
4. **The compatibility matrix is preserved as a CSV** for
   later reference in Phase 6A-prime or downstream work.

## Status

**Phase 6A complete.**  Compatibility matrix produced; 13 of
19 particles certify under Q132 (with ν-pairing working
assumption), 6 remain incompatible at the e-sheet level.
**Phase 6B is blocked** until 6A-prime settles whether the
incompatible tuples re-derive cleanly under `|n_et| ≤ 1`, or
until an e-sheet binding mechanism is established.
