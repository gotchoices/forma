# Q115. Three generations, metric structure, and the muon problem

**Status:** Open — working plan for next studies
**Related:**
  R50 (Tracks 8–11), [Q114](Q114-bare-magnetic-moment-convention.md),
  [model-D](../models/model-D.md), [next-steps](../work/next-steps.md)
**Source:** Session 2026-04-09/10 — R50 Tracks 8–11, user observations

---

## 1. Context: what Tracks 8–11 established

R50 Tracks 8–11 tested every avenue available in the current MaD
formalism for the muon and pions:

| Track | Approach | Result |
|-------|----------|--------|
| 8 | Viability search (3 M modes, 4 branches, σ_eν grid) | 16/20 particles viable; muon NOT viable |
| 9 | Spin-singlet pair sums | K± rescued at 0.73%; muon, pions still fail |
| 10 | Decay-product composition + cross-shear boost | ν sheet too large to contribute; σ_eν boosts 2.5× before singularity (need 207×) |
| 11 | High ring-winding modes | **Muon = (1, 506) at 0.049%!** But 500 ghost modes |
| 11b | Balanced harmonics | No clean-ratio mode near 105.7 MeV — sheet scale gap too large |

**Bottom line:** The muon IS in the linear spectrum as (1, 506,
0, 0, 0, 0) — a high ring-winding mode on the e-sheet.  The
"mass desert" was an artifact of the n₂ ≤ 10 search range.  But
this creates a severe ghost problem: ~500 Q = −1 spin-½ modes
between the electron and muon, each spaced by ~0.209 MeV.

---

## 2. User observations and questions

These observations emerged during the Tracks 8–11 session and
are recorded here for future reference.

### O1. Back-reaction / fabric tension is ad hoc if only the muon needs it

If the muon requires a mechanism (sheet compression, compound
back-reaction) that no other particle uses, the mechanism is
suspect.  All other particles are found as straightforward
modes on the metric.  The muon should be too.

**Resolution:** Track 11 confirmed this — the muon IS a
straightforward mode (1, 506).  No special mechanism needed.

### O2. High ring winding solves the mass but creates ghosts

Mode (1, 506) gives 105.607 MeV (0.049% off), and (1, 8512)
gives 1776.846 MeV for the tau (0.0008% off).  The neutral
pion (0, 647) gives 135.060 MeV (0.062% off).  But every
integer n₂ from 2 to 8512 is a valid mode.

**Key question:** What selects n₂ = 2, 506, and 8512 out of
the ~8500 available Q = −1 spin-½ modes?

### O3. The off-diagonal metric is vastly under-explored

The Ma 6×6 metric has 15 off-diagonal entries.  We model 6
(3 within-plane shears + 3 scalar cross-shears).  Each cross-
sheet block is a 2×2 matrix with 4 independent entries; we
collapse each to one scalar.  Additionally, 18 Ma-S cross terms
exist and are all set to zero.

| Level | Off-diagonal entries | Currently modeled |
|---|---|---|
| Within Ma (6×6) | 15 | 6 |
| Ma ↔ S (6×3) | 18 | 0 |
| **Total** | **33** | **6** |

### O4. In-sheet shear may be wrongly assigned

Currently, the fine-structure constant α = 1/137 determines the
in-sheet shears s_e and s_p via the R19 formula.  But α is
fundamentally the coupling between the material sheet (Ma) and
spatial lattice (S).  It should come from a **Ma-S cross term**,
not an in-sheet term.

If α is relocated to Ma-S cross terms, then in-sheet shears
become **free** to determine generation mass ratios — exactly as
the neutrino shear s₃₄ determines the three neutrino mass
eigenstates.

### O5. Three generations from in-sheet shear (the neutrino precedent)

On the ν sheet, shear s₃₄ = 0.022 splits three low-order modes
into three mass eigenstates matching observed Δm² splittings.
Could the same mechanism work on the e sheet?

At s_e ≈ 2 (not 0.096), the mode (1, 2) becomes anomalously
light because n₂ − n₁·s = 2 − 2 ≈ 0 (near-cancellation).
Other modes (1, 3), (1, 19), etc. don't cancel and stay heavy.
Rough estimates at s_e ≈ 2, ε_e ≈ 207 give mass ratios
~1 : 207 : ~3500, approximately matching e : μ : τ.

### O6. The ghost problem may reduce to mode stability

If the three charged leptons are (1, 2), (1, 3), (1, 19) at a
high shear, the ghost problem becomes: why are (1, 4) through
(1, 18) not observed?  Possible answers:

- **gcd fragmentation:** gcd(1, n) = 1 for all n, so this
  doesn't help directly.  But higher-n₁ modes like (2, 4) have
  gcd = 2 and fragment.
- **Resonance selection:** Only modes near a "resonance
  condition" (like n₂ ≈ s for cancellation) are long-lived.
- **Waveguide-like cutoff at high n₂:** Perhaps modes above
  some winding density threshold are evanescent.
- **Prime winding numbers:** (1, 2), (1, 3), (1, 19) — the
  ring windings are all prime.  (1, 4) = (1, 2²) is composite.
  Could primality be a stability criterion?

### O7. Charged pions remain the sole structural failure

π± require Q = ±1, spin = 0.  The topological spin-charge
constraint (odd Q forces spin ≥ ½) is independent of all metric
parameters.  No shear, cross-shear, or winding number avoids it.
This is the one particle the current formalism cannot host as
a single mode or balanced pair.

### O8. The proton sheet should also show three generations

If the e sheet has three lepton generations from in-sheet shear,
the p sheet should have three quark generations from s_p.  This
would give u/c/t or d/s/b mass ratios from geometry.

---

## 3. Attack plan

### Study A: Three-generation solve on the electron sheet

**Goal:** Find (ε_e, s_e) such that three low-order modes on
the e sheet reproduce the charged lepton mass ratios
m_e : m_μ : m_τ = 1 : 206.77 : 3477.2.

**Method:**
1. For each candidate triple of modes — e.g., {(1,2), (1,3),
   (1,n)} or {(1,2), (-1,2), (1,n)} — solve the two equations:
   - μ(mode_1) / μ(mode_2) = m_e / m_μ
   - μ(mode_1) / μ(mode_3) = m_e / m_τ
   numerically over the (ε_e, s_e) plane.
2. Report which triples have real solutions and what (ε_e, s_e)
   they require.
3. At each solution, check: what α does the R19 formula give?
   (Expected: not 1/137, confirming that α must be relocated.)
4. At each solution, count the full mode inventory below 2 GeV.
   How many ghosts?  What charges and spins?

**Deliverable:** A table of viable (mode triple, ε_e, s_e)
solutions with predicted masses, α values, and ghost counts.

**Estimated effort:** ~half day.

### Study B: Ghost inventory at high n₂

**Goal:** Characterize the ghost problem quantitatively at the
Track 11 solution and at Study A's solution.

**Method:**
1. At the baseline geometry (ε_e = 0.65, s_e = 0.096), compute
   all modes (n₁, n₂, 0, 0, 0, 0) with |n₁| ≤ 3 and |n₂| ≤
   10,000 below 2 GeV.  Tabulate by charge, spin, and energy band.
2. Repeat at Study A's (ε_e, s_e) solution.
3. For each mode, compute gcd(|n₁|, |n₂|).  Tabulate: how many
   have gcd = 1 (irreducible) vs gcd > 1 (fragmentable)?
4. Test whether primality of n₂ correlates with observed
   particles (electron n₂=2, muon n₂ from Study A, etc.).

**Deliverable:** Ghost census tables with stability annotations.

**Estimated effort:** ~1 hour per geometry.

### Study C: Relocating α to Ma-S cross terms

**Goal:** If Study A confirms that in-sheet shear at the
generation-solving value does NOT give α = 1/137, identify which
Ma-S metric component can independently produce α.

**Method:**
1. Extend the metric to include one Ma-S cross term (simplest:
   g(e-tube, S-x) = σ_eS).
2. Derive the modified energy formula with this term present.
3. Solve for σ_eS such that the coupling between a mode and the
   spatial lattice gives α = 1/137.
4. Check: does this σ_eS value conflict with any existing
   constraint?

**Deliverable:** A formula for α in terms of Ma-S cross terms,
or a no-go result showing why this relocation doesn't work.

**Estimated effort:** ~1 day (mostly algebra).

### Study D: Three generations on the proton sheet

**Goal:** Same as Study A, applied to the p sheet for quark mass
ratios.

**Method:** Same 2D root-finding approach.  Target ratios:
- d : s : b = 4.7 : 93 : 4180 MeV (ratio 1 : 19.8 : 889)
- or u : c : t = 2.2 : 1275 : 173,000 MeV (ratio 1 : 580 : 78,600)

**Deliverable:** Viable (mode triple, ε_p, s_p) solutions for
quark generations.

**Estimated effort:** ~half day.

**Depends on:** Study A (to validate the method).

---

## 4. Priority and sequencing

```
Study A (three-generation solve on e sheet)    ← DO FIRST
    │
    ├── if solution exists:
    │       Study B (ghost inventory at solution)
    │       Study C (relocate α)
    │       Study D (proton sheet quarks)
    │
    └── if no solution:
            Revise hypothesis
            (maybe the generation structure needs
             cross-sheet terms, not just in-sheet shear)
```

Study A is the gate.  If a clean (ε_e, s_e) exists for the
three charged leptons at low mode numbers, the rest follows.
If not, we reconsider.

---

## 5. Relationship to existing studies

- **R50 stays untouched.**  Studies A–D are new investigations
  alongside R50, not revisions of it.  R50's particle census
  remains valid at its parameter values.
- **Model-D vs model-E:** Studies A–D can be performed within
  model-D's codebase (`ma_model_d.py`).  If Study C requires a
  fundamentally different metric construction (Ma-S terms), that
  would motivate model-E.  Until then, model-D suffices.
- **White paper:** Updated to reflect Tracks 8–11 findings.
  Studies A–D results would feed into the next revision.
