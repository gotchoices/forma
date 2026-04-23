# Q132: The promotion-chain principle — what each compact dimension produces, and why `|n_tube| = ±1`

**Status:** Open — working hypothesis.  Proposes a foundational
principle that unifies R33's empirical "n_tube = ±1" rule,
the order-of-compactification framework (Q127), and the
ghost-suppression behavior exposed by R63 Tracks 1–4.  Not yet
derived from GRID axioms; formalization is an R62 derivation
target.

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
  [R63](../studies/R63-proton-tuning/) Tracks 1–4 (ghost audits that exposed the need for this principle).

---

## 1. The principle

**Each compact dimension promotes its input to the next-order
observable, subject to specific rules about what constitutes a
completed promotion.**

The three levels at work in model-F:

| Level | Compact structure | Input | Output |
|:-----:|:-----------------:|:------|:-------|
| 0 | — (non-compact) | — | raw information / phase |
| 1 | aleph (S¹) | information | **light / energy** (photon) |
| 2 | ring (first T² cycle) | energy | **mass** |
| 3 | tube (second T² cycle) | mass | **charge** |

Each level is a compact 2π closure, and each 2π closure counts
as **one discrete promotion event**.  Multiple 2π closures on the
same cycle are not amplifications of one event — they are
**separate events** producing separate objects.

## 2. Mass vs charge role: shear-determined

A trapped photon produces mass regardless of whether it's trapped
in the ring or the tube direction — any confined EM energy has a
rest frame and therefore a mass.  **The asymmetry between "ring as
mass producer" and "tube as charge producer" is set by the SHEAR
geometry**, not by an intrinsic difference between the two cycles.

On the e-sheet, the extreme shear (s_e ≈ 2) makes the (1, 2)
family shear-resonant, concentrating mass in the ring direction
and designating the tube as the "charge counter."  On the p-sheet,
s_p ≈ 0.16 and the (n, 2n) structure similarly picks out one
direction as primary-mass, the other as charge.  On the ν-sheet,
R60 T18's real-field conjugate-pair averaging nullifies the
charge-producing mechanism even when tube winding is present.

This shear-based role designation is an empirical observation
from the sheet geometries that model-F has converged on; the
deeper reason *why* shear plays this role is an open derivation
target.

## 3. Particle-creation events

The principle is sharpest on the tube:

> **Each 2π tube closure is one particle-creation event.**

- `|n_tube| = 1` is one event → one particle.
- `|n_tube| = 2` is two events → two particles (not one composite
  unless bound by Z₃-style mechanisms, in which case each
  constituent strand still has `|n_tube| = 1`).
- `|n_tube| = 0` is no event → no particle from the tube, but
  other cycles may still produce a (neutral) particle.

## 4. Typology of single-sheet modes

Combining the promotion chain and the per-event rule gives a
clean classification of single-sheet `(n_tube, n_ring)` tuples:

| Pattern | Mechanism | Physical result |
|:-------:|:----------|:---------------|
| (0, 0) | no activity on either cycle | no particle |
| **(0, n_r ≠ 0)** | ring traps photon → mass; no tube closure → no charge | **neutral massive particle** |
| **(1, 0)** | tube traps photon — but with no ring to provide ring-derived mass, the tube acts as its own ring (self-generated mass); no mass-to-charge promotion available | **neutral massive particle** |
| (1, n_r ≠ 0) | ring provides mass; tube 2π promotes mass to charge | **charged particle** |
| (\|n_tube\| ≥ 2, any n_r) | multiple 2π tube closures → multiple particle events | **forbidden as a single compound** (may appear as Z₃-style composite of n strands) |

**Key clarification.**  Both (0, n_r ≠ 0) and (1, 0) are valid
particles — both involve a confined photon, both produce mass.
The distinction is whether a second-order promotion to charge
can occur: it requires a mass input available to the tube
(which the ring provides), AND a successful tube 2π closure
(which promotes that mass).  If either is missing, the mode
is neutral.

## 5. What this principle explains

### a. R33's empirical "n_tube = ±1" rule — derived

R33 observed from the charge formula that real particles have
`|n_tube| = 1` but did not derive it from first principles.
Under the per-event rule, this is immediate: a particle
corresponds to one creation event, which is one 2π tube closure.
Any observed stable particle therefore has exactly `|n_tube| = 1`
on its active charged sheet.

### b. Z₃ confinement on the p-sheet — absorbed

R60 T16 derived that `n_pt ≡ 0 (mod 3)` is required for free
p-sheet modes (density-fluctuation cancellation).  Under the
promotion-chain principle with the per-event rule, this becomes:

- A free composite must be a Z₃ triplet of strands, each with
  `|n_pt| = 1` (so each strand is one particle-creation event).
- The composite has three events (three "quarks") bound together.
- The composite's apparent `|n_pt| = 3` is the count of its
  constituents, not a single-particle tube winding.

This is consistent with R60 T16 and strengthens the
interpretation: the (3, 6) proton is three quark strands, each
with its own 2π tube closure, bound by Z₃.

### c. The e-sheet's absence of a Z₃ analog — explained

The e-sheet's `|n_et|=1` behavior does not require Z₃
confinement; it requires only the per-event rule.  A single
electron is `(1, 2)` with one tube event; the muon is `(1, 1)`,
the tau is `(1, 15)` (per R63 Track 4, contra R53's high-n
claim).  All three are single-event leptons.

### d. The `(1, 0)` ν-sheet "ghost" — reinterpreted

Model-F flagged `(1, 0)` on the ν-sheet as a ghost because it
predicted a neutral mode with no observed counterpart.  Under
the promotion-chain principle, it's **not a ghost — it's a
valid prediction** of a tube-only neutral particle.  Its mass
under R61 #1 geometry would be ~46% of ν₁, placing it at ~13–15
meV.  This is below cosmological detection thresholds, but the
prediction is clean and may connect to sterile-neutrino
phenomenology.

### e. Ring-only neutral modes — reinterpreted

Similarly, `(0, n_r ≠ 0)` modes on any sheet — previously flagged
as ghosts in R63 Tracks 1 and 4 — are valid predictions of
**neutral massive particles (ring-trapped photons)** under the
clarified principle.  Their non-observation in the observed
spectrum makes them **dark-mode candidates** (consistent with
R42's dark-matter framing of ghost modes).

### f. R63 Track 1 high-|Q| ghosts — killed

The p-sheet modes like `(3, 1), (3, 2), (3, 4), (3, 5)` with
gcd(n_pt, n_pr) = 1 have "per-strand" windings that would be
non-integer — so they cannot arise as integer-strand Z₃
composites.  Under the per-event rule, they are forbidden.

### g. R63 Track 4 high-|n_et| ghosts — killed

The e-sheet `(2, 4), (3, 6), (4, 8)` ghost tower at multiples
of m_e has `|n_et| ≥ 2` — multiple tube events → forbidden as
single particles.  Z₃ compositing is not structurally
available on the e-sheet (R60 T17's exemption), so these don't
reappear as composites either.

## 6. Net effect on R63's ghost inventory

Every single-sheet ghost R63 has identified is either:

- **eliminated** (multi-event modes; gcd-mismatched p-sheet
  modes with no integer strand decomposition);
- **reinterpreted as a valid neutral massive particle**
  ((0, n_r ≠ 0) modes, (1, 0) ν-sheet); these become dark-matter
  or sterile-neutrino candidates rather than problems;
- **handled by an existing mechanism** ((1, n_r ≠ 0) modes on
  the ν-sheet, which are tube+ring → would be charged but R60
  T18's real-field conjugate pairing neutralizes them).

## 7. Open questions and derivation targets

1. **Why does the shear determine the ring/tube role?**  The
   principle says the tube is the charge counter, but the
   underlying reason the shear-resonance direction plays the
   ring role and the tube-Killing direction plays the charge
   role is not derived.  Candidate mechanism: the shear
   resonance makes the ring direction's KK momentum near-zero,
   leaving only the tube direction to carry topological charge
   into 4D.  Needs explicit derivation.

2. **Why is a 2π tube closure one "event" and not zero, two, or
   a fraction?**  The principle asserts it; GRID A6's "α as
   coupling per 2π" is consistent but not a proof.  An R62
   derivation starting from GRID axioms → KK reduction → "each
   2π emits one quantum" would formalize this.

3. **What does tube-without-ring "self-promoting mass" actually
   mean mechanically?**  The (1, 0) mode's mass depends on the
   full metric via L_ring and the shear; the principle just
   says "mass exists," without specifying the ring-vs-tube
   mass-contribution breakdown.  An explicit derivation would
   show how the tube direction's trapped energy produces mass
   via the sheet geometry.

4. **How does multi-sheet compositing interact with the per-event
   rule?**  Multi-sheet compounds (pions, baryons, nuclei)
   should be bookkeeping-consistent with "N particle-creation
   events, bound together."  A full-audit of the existing
   model-F inventory against this interpretation is warranted.
   Particularly: the neutron `(−3, −6, 1, −6, −3, −6)` has
   `|n_et| = 3` and `|n_pt| = 3` — does this represent 3 strands
   on each sheet plus 1 ν event (7 total events)?  Or some
   other decomposition?

5. **Is the ν-sheet charge neutralization (R60 T18) derivable
   from the promotion chain, or is it an independent
   architectural feature?**  If the real-field conjugate pairing
   is a consequence of the same principle, the theory is
   complete; otherwise it's a separate rule.

## 8. Status and next steps

This Q file captures the principle; it does not derive it.

**Path to formalization:**

- A **new R62 derivation** (Program 2, "Promotion-chain
  principle") starting from GRID axioms, KK reduction, and
  the 2π-per-event counting, producing as output:
  (a) the per-event rule as a theorem,
  (b) the shear-determined role asymmetry,
  (c) the typology of Section 4,
  (d) the ghost-suppression results of Section 5.

- **Empirical validation** inside R63: Track 5 (if created)
  could apply the principle explicitly to re-score the e-sheet
  and p-sheet landscapes, treating the now-allowed neutral
  modes as valid predictions rather than ghosts.

- **Comparison with Q131's unpromoted-information proposal**:
  both Q131 (dark energy as unpromoted aleph information) and
  this principle (particle species as promotion results) share
  the same "promotion" framework.  They may unify as parts of
  a single theory of compact-dimension physics.

## 9. Why this matters

If correct, the principle:

- Turns `|n_tube| = ±1` from an empirical rule into a **theorem**;
- Explains **why particles are discrete** (each 2π = one event);
- Unifies **Z₃ confinement** (p-sheet) and **winding restriction**
  (e-sheet) under a single rule;
- Converts the **R63 ghost list** from an architectural problem
  into a **predictive catalog** of dark and sterile states;
- Slots cleanly above the existing **order-of-compactification**
  framework (Q127), which describes *what each level produces*
  but not *what a completed promotion looks like at each level*.

If wrong, the framework still exposes the specific questions
(items 1–5 in Section 7) that need answering — progress either
way.
