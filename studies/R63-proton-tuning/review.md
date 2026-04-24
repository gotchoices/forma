# R63 Review — Tracks 1–8 and proposed next track

## The arc, one line per track

1. **T1 — Proton-sheet ghost audit at baseline.**  Applied R60 T16
   Z₃ discipline to the p-sheet; baseline came up clean — no
   light ghosts at `(ε_p, s_p) = (0.55, 0.162)`.
2. **T2 — Viable-region grid.**  Swept `(ε_p, s_p)`; confirmed
   the analytical ghost-free bound `μ(3, 6) ≤ 8.09` held across
   88% of the grid.
3. **T3 — Fitness heat map (Phase A flat / Phase B width-weighted).**
   Phase B's natural-line-width thresholds relocated the peak to
   `(0.80, 0.05)` with fitness 4.95/7 and a near-exact π⁰ match
   (0.038%).
4. **T4 — E-sheet ghost audit.**  Exposed a multi-event tower
   (`|n_et| = 2, 3, 4, …`) and the `(0, −1)` 104-MeV ghost that
   the strict R33 rule forbade.
5. **T5 — E-sheet under Q132 v2.**  Re-render after the
   promotion-chain rule was refined to bright/dark via gcd + ω-sum:
   0 ghosts across 2296 grid points, R53 Solution D confirmed as
   near-peak on a wide `ε_e` ridge.
6. **T6 — Q132 v2 compound-mode audit.**  14 of 19 baseline tuples
   pass v2 charge arithmetic unchanged; 5 (τ, Λ, Σ⁻, Ξ⁻, Ξ⁰)
   find v2-compatible replacements at comparable mass accuracy.
   Marginal ratio scans confirm model-F baseline as the joint
   inventory optimum; ν-sheet is passive for hadronic fit.
7. **T7 — Compound-mode vs. spatial separation, H→Pb.**  Walked
   the compound-mode miss-vs-binding curve up the stable chain;
   miss scales with binding and the compound mode remains the
   cheapest configuration through Fe, with a crossover against
   the separated-nucleons cost estimate in the heavy-A regime.
8. **T8 — Decay-conservation audit + additive-composition refinement.**
   β-decay identity pinned the neutron tuple to `(1, 2, −1, −1,
   3, 6)`; adopting it plus additive nuclear composition
   (`Z·p + (A−Z)·n`) improved 20 of 22 nuclei by a mean of
   0.37 pp.  Decay audit across 19 hadron decays: charge
   conserves universally under the ingredient-sum rule; winding
   conserves for β decay and has structured, meaningful
   residuals elsewhere (chiral anomaly, strong/weak hadronic,
   flavor-changing leptonic).  The residual nuclear miss (~0.87%
   at ⁵⁶Fe ≈ 453 MeV) is now a clean numerical target for the
   binding mechanism: observed B(⁵⁶Fe) = 492 MeV.

**Net at Track 8 close.**  R63 has delivered a refined rule set
(Q132 v2 + ingredient-sum composite charge + additive nuclear
composition + β-decay-consistent neutron), a clean inventory
mass match, and a sharp residual that *is* the nuclear binding
energy.  The next track's job is to close that residual from
first principles.

---

## Proposed Track 9 — Nuclear binding from Ma-state energy minimization

**Hypothesis** (carried forward from the Track 8 wrap-up
discussion): *Forces in S result from lowest-energy states in
Ma.*  Nuclear binding is the 4D projection of a Ma-domain cost
function: nuclei exist as stable configurations when the
compound-mode Ma energy is lower than the spatially-separated
nucleon configuration, and the difference — currently showing up
as T7+T8's ~0.87% residual at Fe — is the binding energy.

### What this track can accomplish

- **Derive nuclear binding from MaSt rather than insert it.**
  T8's additive residual is the right quantity to explain; the
  task is to find the Ma mechanism that produces it.
- **Pin the previously unconstrained cross-sheet σ parameters.**
  `σ_ep, σ_eν, σ_νp` have been pool item **h** since R60 T7.
  Nuclear binding gives ~250 mass data points against a small
  number of cross-shear parameters — a massive constraint
  upgrade over the particle inventory alone.
- **Convert BW-like phenomenology into structural MaSt
  statements.**  Each Bethe-Weizsäcker term (volume, surface,
  Coulomb, asymmetry, pairing) should map to a specific Ma
  feature if the hypothesis is right; mapping them is the
  substantive test.
- **Explain saturation and range.**  If the binding-per-nucleon
  plateau above Fe comes from cross-shears that decay in
  "compound-mode distance," the decay length is the
  compactification scale; extracting it and comparing to
  `L_p` is a clean independent check of the hypothesis.

### How to do it

**Phase 9a — Compound vs. separated energy under cross-shear
dressing.**  Write `E_Ma(compound)` and `E_Ma(separated)` for a
single (A, Z) including the derivation-10 F31 iterated
Schur-complement corrections.  At leading order
`μ(3A, 6A) = 3A · μ(1, 2)` gives zero binding (µ is linear in k);
binding has to live in the cross-shear dressing.  Single nucleus,
algebra only — establish that the difference can be nonzero and
identify which σ entries enter.

**Phase 9b — Binding curve across the chart, H → Pb.**  Evaluate
`E_Ma(compound) − Σ E_Ma(nucleon)` for the Track 7/Track 8
isotope chain under cross-shear dressing.  Plot against observed
`B(A, Z)`; if the shapes match with reasonable cross-shear
magnitudes, the hypothesis closes.  If they differ, the
deviation pattern says which BW term isn't captured and points
at what needs extending.

**Phase 9c — Decompose the match into BW-like terms.**  Fit the
MaSt prediction to the five-term Bethe-Weizsäcker decomposition.
Each term's cross-shear origin is recorded.  Cross-shears that
were unconstrained by R60 get specific numerical values pinned
by the binding curve, with residuals reported.

**Phase 9d (optional) — Magic numbers as Ma-cost-function
minima.**  Scan the tuple lattice for (A, Z)-tuples where the
cross-shear-dressed compound energy has a local minimum.  Check
whether the minima align with 2, 8, 20, 28, 50, 82, 126.  If
yes — a major positive result (magic numbers from first
principles).  If no — shell closure is orthogonal to Ma's
binding mechanism and belongs in a separate track.

### What to watch for

- **Don't over-fit.**  With five BW terms and multiple
  cross-shear parameters a match is almost guaranteed.  The test
  is whether each cross-shear gets a separately constrained
  value and still reproduces the full curve.  Compute the
  cross-shear from two or three nuclei; check it against the
  other ~247.
- **Coulomb is not a new prediction.**  `Z²α/R` is standard; it
  should fall out of e-sheet/p-sheet charge-and-radius structure
  but is not where the hypothesis is tested.  The asymmetry and
  pairing terms are the most informative — they couple N vs. Z
  and even/odd structure, respectively, and should pin specific
  Ma features.
- **Range ≈ saturation ≈ L_p.**  If the fit's exponential decay
  length in compound-mode distance matches the independently
  known p-sheet compact radius, that's independent confirmation.
  If the two values disagree materially, the hypothesis or the
  geometry needs adjustment.
- **T8 flagged `σ_ep` explicitly.**  FR-4 of Track 8's
  closeout suggested cross-sheet σ_ep as the candidate
  mechanism for the neutron p-n mass deficit (−1.3 MeV) and by
  extension the nuclear binding residual.  Track 9 should carry
  σ_ep as the first cross-shear to fit — it's structurally
  motivated and numerically consequential.

### Reusable assets

- Track 7's infrastructure for walking (A, Z) across the isotope
  chain.
- Track 8's additive-composition tuples and ingredient-sum
  charge rule — the correct composite representation for nuclei.
- Derivation-10's F30/F31 Schur-complement machinery — the
  vehicle for propagating cross-shear corrections into the
  compound mass formula.
- The binding-curve residual at ⁵⁶Fe (453 MeV predicted vs. 492
  MeV observed) as the sharp numerical benchmark.

### Scope boundaries

Track 9 is about **nuclear binding in model-F / Q132 v2 / T8's
refined framework**.  It does **not** re-open Q132 v2, does not
touch particle inventory tuples beyond nuclei, and does not
attempt the PMNS bookkeeping (T8 FR-2) or the chiral-anomaly
mechanism (T8 FR-3).  Those are separate tracks or successor
studies.  If Track 9 requires framework extension (e.g., S-space
overlap of T8 FR-4 second bullet), that's a finding, not a
default.
