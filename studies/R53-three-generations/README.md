# R53: Three generations from in-sheet shear

**Status:** Active — Tracks 1, 4 complete (solutions found for leptons and quarks)
**Questions:** Q115 (three generations and metric structure)
**Type:** compute / theoretical
**Depends on:** R50 (Tracks 8–11, mass desert, high ring-winding),
R49 (neutrino three-generation precedent), R19 (α–shear relation)

---

## Motivation

R50 Track 11 showed that the muon and tau can be matched by high
ring-winding modes on the electron sheet: (1, 506) at 0.049% and
(1, 8512) at 0.0008%.  But this creates ~8500 ghost modes between
the electron and tau, all with Q = −1 and spin ½, spaced by
~0.209 MeV.  No selection rule in the current formalism distinguishes
the muon at n₂ = 506 from its neighbors at 505 or 507.

Meanwhile, the neutrino sheet already demonstrates a
**three-generation mechanism**: in-sheet shear s₃₄ = 0.022 splits
three low-order modes — (1, 1), (−1, 1), (1, 2) — into three mass
eigenstates matching observed Δm² splittings exactly (R26 F33,
R49 Assignment A).  The shear creates asymmetry between modes
through the term (n_ring − n_tube · s) in the energy formula.

**The hypothesis of this study:** the same mechanism operates on
the electron sheet.  If the in-sheet shear s_e is large enough
(specifically, near a value that creates a near-cancellation for one
mode), then three low-order modes on the e sheet can reproduce the
charged lepton mass ratios m_e : m_μ : m_τ = 1 : 206.77 : 3477.2
— without requiring high ring winding or exotic mechanisms.

**The key insight:** when s_e ≈ n₂ for one mode (say s_e ≈ 2 for
the electron mode (1, 2)), that mode's ring energy contribution
(n₂ − n₁ · s)² nearly cancels, making it anomalously light.  Other
modes like (1, 3) or (1, 19) don't cancel and stay heavy.  The mass
hierarchy comes from the *mismatch* between each mode's n₂ and the
shear.


## Prerequisite: what changes from model-D?

Currently, s_e = 0.096 is determined by requiring α(ε_e, s_e) = 1/137
via the R19 formula.  At s_e = 0.096, the first few e-sheet modes
are all within a factor of ~1.3× of each other — nothing like the
207× ratio needed for the muon.

For in-sheet shear to produce three generations, s_e must be **much
larger** (order ~2, not ~0.1).  This means α = 1/137 can no longer
come from s_e.  The fine-structure constant would need to be
determined by a different metric component — most naturally a
**Ma-S cross term** (the coupling between the compact material
sheet and 3D space), which the current model sets to zero.

This study does NOT implement the α relocation.  It asks the
narrower question: **does a (ε_e, s_e) solution exist for the
three charged lepton masses?**  If yes, the α question becomes
urgent.  If no, the hypothesis fails and we move on.


## Philosophy

1. **The neutrino sheet is the template.**  What worked for three
   neutrinos (low-order modes + in-sheet shear → mass splittings)
   should work for three charged leptons.  Same physics, different
   sheet.

2. **Elegance over brute force.**  The electron should be (1, 2),
   not (1, 506).  The muon should be (1, 3) or (-1, 2) or some
   equally clean mode — not a 506th harmonic.

3. **Compute first, interpret later.**  Find the solutions
   numerically before worrying about what s_e ≈ 2 means physically.

4. **R50 is untouched.**  This study explores a different region of
   parameter space.  R50's results at (ε_e = 0.65, s_e = 0.096)
   remain valid.


## Tracks

### Track 1: Solve for (ε_e, s_e) from lepton mass ratios

**Status:** Complete — solution found (F1–F9)

**Goal:** For each candidate triple of e-sheet modes, solve for the
(ε_e, s_e) that reproduces the charged lepton mass ratios.

**Method:**

The dimensionless mode energy on a single sheet is:

> μ(n_t, n_r, ε, s) = √((n_t / ε)² + (n_r − n_t · s)²)

The mass ratio between two modes A and B at the same (ε, s) is:

> m_A / m_B = μ_A / μ_B

For three modes assigned to (electron, muon, tau), we have two
independent ratio equations:

> μ_e / μ_μ = m_e / m_μ = 1 / 206.768
> μ_e / μ_τ = m_e / m_τ = 1 / 3477.23

These are two equations in two unknowns (ε_e, s_e).  For each
candidate triple, solve numerically (2D root-finding on a grid,
refined by Newton's method or bisection).

**Candidate triples to test:**

The modes must all have |n_t| odd (for spin ½) and the same sign
of Q contribution from the e sheet (n₁ = ±1 for unit charge).
Candidates:

| Label | Electron | Muon | Tau | Notes |
|-------|----------|------|-----|-------|
| A | (1, 2) | (1, 3) | (1, n) | Same chirality, ascending ring |
| B | (1, 2) | (-1, 2) | (1, 3) | Opposite chirality for muon |
| C | (1, 2) | (-1, 2) | (-1, 3) | Mixed chiralities |
| D | (1, 2) | (1, 3) | (-1, 3) | Tau as anti-chirality of muon |
| E | (1, 2) | (1, 3) | (1, 5) | Ascending primes |
| F | (1, 2) | (1, 3) | (1, 7) | Ascending primes |
| G | (1, 2) | (-1, 2) | (1, n) | Muon as anti-electron |
| H | (1, 2) | (1, 4) | (1, n) | Larger muon ring |

For triples where n_τ is free (labels A, G, H), scan n_τ from 3
to 30 and report which integers produce real solutions.

**Deliverables:**
- Table of (triple, ε_e, s_e) solutions
- Predicted masses at each solution
- α from R19 formula at each (ε_e, s_e) (expected: NOT 1/137)
- Assessment: which triples produce clean solutions?

**Script:** `scripts/track1_generation_solve.py`


### Track 2: Ghost inventory at the generation-solving geometry

**Status:** Pending (depends on Track 1)

**Goal:** At each Track 1 solution, compute the full mode spectrum
below 2 GeV and characterize the ghost problem.

**Method:**
1. Enumerate all modes (n₁, n₂) with |n₁| ≤ 5, |n₂| ≤ 50 on the
   e sheet at the solved (ε_e, s_e).
2. Compute energy, charge, spin for each.
3. Tabulate by charge and energy band.
4. Compute gcd(|n₁|, |n₂|) for each — modes with gcd > 1 can
   fragment and may be unstable.
5. Flag modes whose ring winding is prime vs composite.
6. Compare ghost count to the high-n₂ picture from Track 11
   (~8500 ghosts) — is it better or worse?

**Deliverables:**
- Ghost census table at each Track 1 solution
- gcd and primality statistics
- Assessment: does the three-generation geometry reduce the ghost
  problem compared to the high-n₂ picture?

**Script:** `scripts/track2_ghost_inventory.py`


### Track 3: α diagnostic

**Status:** Pending (depends on Track 1)

**Goal:** At each Track 1 solution, compute what α the R19 formula
gives.  If α ≠ 1/137, this confirms that α must be relocated to a
different metric component.

**Method:**
1. Evaluate α(ε_e, s_e, n_t=1, n_r=2) at the Track 1 solution.
2. Also evaluate α for each of the three generation modes.
3. Report the discrepancy from 1/137.
4. Qualitative discussion: which Ma-S cross term could absorb α?

**Deliverable:** α diagnostic table and relocation assessment.

**Script:** incorporated into Track 1 output.


### Track 4: Three generations on the proton sheet

**Status:** Pending (depends on Track 1 to validate the method)

**Goal:** Apply the same method to the proton sheet.  Solve for
(ε_p, s_p) that produces three quark-like modes with mass ratios
matching one of the quark families.

**Target ratios:**
- d-type: d : s : b = 4.7 : 93 : 4180 MeV → 1 : 19.8 : 889
- u-type: u : c : t = 2.2 : 1275 : 173,000 MeV → 1 : 580 : 78,600

**Method:** Same 2D root-finding as Track 1, applied to the p sheet.

**Deliverables:**
- (ε_p, s_p) solutions for quark mass ratios
- Comparison: does the same mechanism work on both sheets?

**Script:** `scripts/track4_quark_generations.py`


## Possible outcomes

**Best case:** A clean (ε_e, s_e) solution exists for a low-order
triple like {(1,2), (1,3), (1,19)} or {(1,2), (-1,2), (1,3)}.
The three charged leptons emerge from three modes on a single sheet,
exactly paralleling the three neutrinos.  Ghost count is
dramatically reduced compared to the high-n₂ picture.  α must be
relocated but that's a feature, not a bug — it clarifies the
role of each metric component.

**Partial success:** A solution exists but requires extreme ε_e
(>> 1) or very fine-tuned s_e.  The mechanism works but the
geometry is unphysical or requires justification.

**Failure:** No real (ε_e, s_e) solution exists for any low-order
triple.  The three-generation structure on the e sheet cannot come
from in-sheet shear alone.  This would point toward cross-sheet
terms or a more radical restructuring (model-E).
