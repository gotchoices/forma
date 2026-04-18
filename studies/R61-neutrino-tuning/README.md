# R61: Neutrino-sheet tuning — paired-mode zoo and Δm² comb

**Status:** Framed — Track 1 ready
**Type:** compute + analytical
**Depends on:** R49 (ν-sheet families, ε_ν/s_ν sweep, Majorana F16),
  R26 (Assignment A derivation), R57 (dark/active ratio 440:1),
  R60 next-track b (smallest-shear ν solution)

---

## Objectives

R49 identified the neutrino sheet as structurally the simplest of the
three Ma sheets (F26): the three mass eigenstates are the three lowest
spin-½ modes of an unfiltered torus at ε_ν = 5, s_ν = 0.022, matching
Δm²₃₁/Δm²₂₁ = 33.6 with one free parameter.  R49 F16 also noted that
±n_ring modes are C-conjugates, i.e. WvM-realized Majorana neutrinos.

R61 picks up a structural observation that R49 made in passing but did
not systematize: at any (ε_ν, s_ν) that produces the 33.6 ratio, **many
triplets beyond Family A reproduce the same ratio**, and **every
fermion-candidate mode (|n_r| ≥ 1) has a ±n_r partner at near-degenerate
mass**.  This suggests a different reading of the neutrino sheet — not
"three specific modes selected from a ghost-filled spectrum," but "a
zoo of near-degenerate ±paired triplets all producing the observed
ratio, of which three are 'loud' under some selection rule and the rest
are sterile (R57's 440:1)."

R61 asks:

1. Does a region of (ε_ν, s_ν) exist where the zoo of 33.6-ratio,
   all-paired, spin-½ triplets is populous AND the observed triplet
   sits cleanly among its lowest members?
2. What *comb* of Δm² features (predicted by the integer n_tube
   transition structure) does each (ε_ν, s_ν, E₀) calibration imply?
   Do reported oscillation anomalies (LSND, DANSS, reactor) land on
   the comb or miss it?
3. What selection rule — waveguide cutoff, cross-sheet coupling,
   energetic threshold, production matrix element — picks three
   "loud" triplets out of the zoo?
4. Under the pair-mandatory reading, does the Majorana superposition
   give zero net winding / zero charge under whichever charge
   mechanism (tube-winding per R48, ring-winding per Taxonomy) is
   taken as canonical?

If a clean zoo region exists and the comb lines up with any reported
anomaly, R61 delivers a testable re-reading of neutrino physics.  If
no selection rule cleanly isolates Family A from the zoo, R61
documents the gap and flags what the selection mechanism would need
to be.

Note on project-level framing: R61 ignores cosmological Σm and N_eff
bounds per user direction — only steady-state laboratory oscillation
constraints apply.

---

## Execution plan

Tracks are added one at a time.  Only the currently-executing track
is numbered; candidates for "next track" live in the pool below as
lettered items and get numbered when chosen.

### Track 1 — Zoo enumerator and comb predictor (framed)

**Goal.**  Build a self-contained toolkit that (a) enumerates
±n_r-paired fermion modes on Ma_ν, (b) finds all triplets matching
the 33.6 ratio, (c) outputs the predicted Δm² comb from n_tube
transitions under a given E₀ calibration.  No selection rules yet —
this track establishes the raw spectrum and its measurable
consequences.  Later tracks impose filters.

**Strategy.**

One script, five primitives, four tests.  Keep the API small and
scriptable so later tracks import rather than copy-paste.  No
dependency on `lib/` — everything stays local to R61 until stable.

**Tactics.**

1. **Mode enumerator.**  `enumerate_modes(eps, s, nr_max, nt_max)`
   returns a list of `(n_r, n_t, mu2)` tuples for all integer modes
   with |n_r| ≤ nr_max, 0 ≤ n_t ≤ nt_max, using

       mu2(n_r, n_t) = (n_r · eps)² + (n_t − n_r · s)²

2. **Pair filter.**  `paired_fermion_modes(modes, eps, s, delta)`
   keeps modes with |n_r| ≥ 1 whose ±n_r partner exists in the list
   with µ² splitting below `delta` (dimensionless tolerance on
   splitting/mean).  Excludes n_r = 0 (spin 1) and any splittings
   too large to support Majorana mixing.

3. **Triplet finder.**  `find_ratio_triplets(modes, target, tol)`
   returns all triplets (a, b, c) with µ_a² < µ_b² < µ_c² satisfying
   (µ_c² − µ_a²) / (µ_b² − µ_a²) within `tol` of `target`.  Each
   triplet is reported with its three modes and the exact ratio.

4. **Comb predictor.**  `delta_m2_comb(eps, s, E0_sq, max_dn)`
   computes the cluster of Δm² values from n_tube transitions
   (a, b) with 1 ≤ a < b ≤ max_dn, averaged over low n_r.  Returns
   a list of (n_t_from, n_t_to, Δm²_mean, Δm²_spread).  These are
   predictions — positions fixed by integer structure once (eps, s,
   E0_sq) are set.

5. **Zoo density sweep.**  `zoo_sweep(eps_grid, s_grid, delta, tol,
   ratio_target)` returns a 2D array of counts: at each (eps, s),
   how many 33.6-matching paired-fermion triplets exist.  Identifies
   the populous regions.

**Smoke tests (infrastructure only).**

| # | Test | Expected outcome |
|---|------|-----------------|
| T1 | `enumerate_modes(5.0, 0.022, 3, 5)` reproduces R49 Family A µ² values | (1,1) = 25.957, (−1,1) = 26.045, (1,2) = 28.913 to < 10⁻⁶ |
| T2 | `paired_fermion_modes` at Family A parameters includes (±1,1), (±1,2), (±2,1), excludes all (0, n_t) | list contents match expected |
| T3 | `find_ratio_triplets` at Family A reproduces Family A triplet AND at least 10 other 33.6-matching triplets | ≥ 11 triplets returned, Family A (1,1)(−1,1)(1,2) present |
| T4 | `delta_m2_comb` at (5.0, 0.022, E₀² calibrated to Δm²₃₁ = 2.53×10⁻³ eV²) | n_t: 1→2 cluster at 2.53×10⁻³ eV²; 1→3 cluster at ≈ 6.77×10⁻³ eV² |

**Deliverables.**

- `scripts/track1_zoo.py` — primitives + smoke tests + a reference
  zoo sweep over (ε_ν ∈ [1, 10], s_ν ∈ [0.005, 0.1]) with a
  heatmap output.
- `findings.md` entries F1–F4 recording smoke-test results and an
  initial characterization of the zoo-density map.

**Acceptance criteria.**

- All four smoke tests pass at stated tolerances.
- Zoo sweep output contains a usable density map and a printed
  table of (eps, s, triplet_count) for the top 10 densest points.
- API is small enough to document in the findings (five functions).

**Prototyping note.**  Script and helpers stay inside
[scripts/track1_zoo.py](scripts/) for R61.  Promotion to `lib/` is
deferred until at least two later tracks import the primitives
unchanged.

---

## Next-track pool

Candidates for the next track after Track 1.  Sequence decided from
Track 1's outcome.  Entries are sketches; the chosen one is
elaborated to full-track detail when promoted.

**a. Zoo-region characterization.**  For the densest (ε_ν, s_ν)
points from Track 1, characterize the triplets: typical µ² range,
whether Family A sits as the lowest-mass triplet or buried, spread
of n_r values, and whether the all-paired constraint is naturally
satisfied or needs a delta-tolerance tweak.

**b. Comb vs anomalies.**  Compare the Δm² combs from several
viable (ε_ν, s_ν, E₀) calibrations against reported sterile-neutrino
and oscillation anomalies (LSND at Δm² ≈ 1 eV², DANSS, reactor
antineutrino anomaly, MicroBooNE).  Identify which (if any)
anomalies land on a predicted cluster.

**c. Selection rule candidates.**  Apply filters one at a time and
measure how many triplets survive: (i) R49 waveguide cutoff n_r · ε
> n_t; (ii) soft energetic cutoff µ² < µ²_max; (iii) cross-sheet
coupling requirement σ_eν, σ_pν ≠ 0 on specific n_r, n_t; (iv)
spin-½ tolerance tighter than R49's 0.15.  Goal: find the minimal
rule (or combination) that isolates Family A or a near-equivalent
triplet from the zoo.

**d. Charge cancellation proof.**  Under each candidate charge
mechanism — tube-winding (R48 CP synchronization), ring-winding
(Taxonomy Q = −n₁ + n₅ generalized to ν-sheet), shear-induced (R19)
— verify quantitatively that the ±n_r Majorana superposition gives
zero net charge.  Required for the "pair-cancels-charge" argument
to be more than narrative.

**e. Small-ε waveguide regime.**  Re-examine R49 Family B (ε = 0.1)
with the zoo lens.  Under a softer cutoff than R49's literal formula
(e.g. evanescence-based, frequency-based), does Family B's
all-paired triplet (±1,2), (±2,2), (±10,1) survive as the
distinguished triplet?

**f. R60 handoff.**  When R60 settles on a ν-sheet geometry via
its track (b), re-run R61's zoo analysis on that geometry.  Provides
the paired-mode structure inside the R60 metric, whatever it turns
out to be.

**g. Production coupling.**  Derive (or bound) the β-decay matrix
element for each zoo triplet — which triplets can be populated by
standard weak processes, and which are genuinely sterile.  This
is the most physically motivated selection candidate but requires
a weak-coupling model, which MaSt does not currently have in
derivable form.

**z. Closeout.**  If a selection rule from track (c) or (e)
isolates a distinguished triplet consistent with observation:
document the refined Family A (or Family A′) assignment and any
testable comb predictions.  If no rule works, document the gap as
the precise blocking constraint so future work can target it.

---

## Files

| File | Purpose |
|------|---------|
| README.md | This framing document |
| scripts/ | Computation scripts (per track, local to R61) |
| findings.md | Results (after computation) |
