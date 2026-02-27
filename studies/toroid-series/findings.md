# Findings: Toroid Series Study

Running log of experiments, results, and their implications for the study.
Entries are chronological. Each entry references the script that produced it
and the propositions from `theory.md` that it bears on.

---

## F1. WvM Charge Baseline

**Script:** `scripts/01_wvm_baseline.py`
**Bears on:** All propositions (establishes the target)

Reproduced the WvM charge prediction from Eq. 5:

    q = (1/2π) √(3 ε₀ ℏ c) = 1.459 × 10⁻¹⁹ C

| Quantity | Value |
|----------|-------|
| q / e | 0.910345 |
| Deficit | 8.97% |
| Correction factor S = e/q | 1.098517 |

The analytic and numerical derivations agree to 6 digits. This correction
factor S ≈ 1.0985 is the fixed target for all subsequent work.

---

## F2. Geometric Series Scan

**Script:** `scripts/02_series_scan.py`
**Bears on:** P1 (series hypothesis), P2 (recognizable ratio)

Scanned 18 named candidate ratios for the geometric model
q_total = q₀ × Σ rⁱ. The exact ratio for an infinite geometric series
matching S is r = 0.08968.

Best candidates:

| Candidate | r | S(∞) | Error vs S |
|-----------|---|------|------------|
| 1/11 | 0.09091 | 1.10000 | 0.14% |
| 4πα | 0.09170 | 1.10096 | 0.22% |
| √α | 0.08542 | 1.09340 | 0.47% |

The Gemini dialog's claim that α itself provides the correction is
decisively wrong — α ≈ 0.00730 gives only a 0.74% correction, 13× too
small.

For the best candidates (r ~ 0.09), the series converges in 3–4 terms
(>99% of the sum from t₀ + t₁ + t₂). The number of "active" terms is
set by convergence speed, not by any external cutoff.

---

## F3. Dimensional Scaling Analysis

**Script:** `scripts/03_scaling_dimensions.py`
**Bears on:** P3 (finite terms), P4 (dimensional correspondence)

For scaling ratio r, counted how many nested layers are needed to
shrink from λ_C down to the Planck length l_P:

| Ratio | Layers to l_P | S(∞) | Charge error |
|-------|---------------|------|--------------|
| α (0.00730) | 11 | 1.0074 | 8.30% |
| 1/11 (0.0909) | 32 | 1.1000 | 0.14% |
| 4πα (0.0917) | 31 | 1.1010 | 0.22% |
| 1/ϕ (0.618) | 111 | 2.618 | 138% |

Key finding: for the best charge-fitting ratios (r ~ 0.09), the
Planck floor is reached after ~30 layers, but the series has already
converged by layer 3–4. The two constraints (charge sum and Planck
cutoff) are therefore *independent* — the Planck floor is not the
mechanism that terminates the series.

The Gemini dialog's claim that ϕ-scaling gives 11 layers is wrong
(it gives 111). Only α-scaling gives exactly 11 layers, but α fails
the charge test badly.

---

## F4. Dialog Claim Verification

**Script:** `scripts/04_dialog_claims.py`
**Bears on:** theory.md §3 (errors in the source material)

Tested 8 quantitative claims from `ref/dialog.md`:

| Claim | Verdict |
|-------|---------|
| α-series gives needed correction | REFUTED (13× too small) |
| 11th α-layer ≈ 64 × l_P | CONFIRMED |
| α⁻¹ ≈ 360/ϕ² | PARTIAL (0.05% off, no derivation) |
| ϕ-scaling gives 11 layers | REFUTED (gives 111) |
| Muon ≈ 200× electron mass | CONFIRMED (206.8×) |
| Tau ≈ 3500× electron mass | CONFIRMED (3477×) |
| λ_C ≈ 2.426×10⁻¹² m | CONFIRMED |
| WvM charge ≈ 0.91e | CONFIRMED |

Score: 5 confirmed, 2 refuted, 1 partial. The refuted claims are the
ones most central to the Gemini dialog's proposed mechanism, which
means the specific construction from the dialog does not hold — but the
broader question (can sub-structure explain the deficit?) remained open.

---

## F5. Unconstrained Series Decomposition

**Script:** `scripts/05_free_series.py`
**Bears on:** P1 (series hypothesis — is geometric the right form?)

Relaxed the geometric assumption entirely. For each N from 2 to 12,
used numerical optimization (scipy, Nelder-Mead) to find the smoothest
N-term decomposition of the deficit D = S − 1 ≈ 0.0985, penalizing
variance and jerk in the log-ratio sequence.

**Result:** Every optimum is perfectly geometric (σ of log-ratios = 0
to machine precision). The smoothness penalty hits zero for all N.

This is mathematically expected — constant ratios have zero variance
by definition — but it confirms an important point: *there is no
non-geometric series lurking as a competing smooth solution.* If the
real physics is non-geometric, it must be driven by a specific
physical mechanism, not by any generic notion of smoothness.

**Implication:** The study can focus entirely on identifying the
geometric ratio r from physical arguments. The form of the series is
settled.

---

## Conclusion: Why This Study Blocked

Follow-on analysis (now in `../toroid-geometry/`) revealed that the
9% charge deficit — the target this entire study was built to correct
— is not a robust physical prediction:

1. **Geometric sensitivity (→ toroid-geometry F1):** The WvM charge
   formula q ∝ r_c²/√V is very sensitive to the assumed cavity volume
   and charge radius. A ~5% shift in the charge radius eliminates the
   deficit entirely. The target S ≈ 1.0985 carries ~5–10% systematic
   uncertainty.

2. **Toroidal cavity modes (→ toroid-geometry F2):** Solving Maxwell's
   equations for standing-wave modes in a toroidal cavity gives
   q = 14–128× e (never close to 0.91e). The sphere of diameter λ —
   not the torus — is necessary to get q ≈ e.

3. **The sphere may be the rotation horizon (→ toroid-geometry F3–F4):**
   WvM's sphere may be physically justified as the "rotation horizon"
   — the boundary within which the photon's field exists. This is an
   interpretation, not a derivation from first principles.

**Consequence:** The series hypothesis (P1–P4) was predicated on the
9% deficit being a precise, physically meaningful number that demanded
a structural explanation. It is instead an artifact of WvM's geometric
approximations. The specific value depends on the choice of cavity
volume and comparison radius, both of which have significant
uncertainty. No series correction to an imprecise target can be
physically meaningful.

**What was learned:**

- The geometric series form is uniquely selected by smoothness (F5).
- Named-constant candidates (1/11, 4πα) fit the target well, but the
  target itself is unreliable.
- The Gemini dialog's specific claims (α-series, ϕ-scaling = 11 layers)
  are quantitatively wrong (F4).

**Spawned study:** `../toroid-geometry/` — investigates the deeper
question of what effective geometry reproduces q = e, which led to
the degenerate torus analysis and the rotation horizon argument.

---

## Open Avenues (Not Pursued)

These remain potentially interesting if the target can be sharpened by
an independent calculation:

- **QED expansion parameters:** Test whether the charge correction can
  be expressed as a rational polynomial in α/π (matching QED-style
  perturbative corrections).
- **Mixed-scale hybrid decomposition:** Allow the series ratio to
  change between layers (e.g., first few terms use one ratio, deeper
  terms use another).
- **Dimensional correspondence:** If a future calculation fixes the
  deficit precisely, check whether the number of terms matches
  string/M-theory dimension counts.
