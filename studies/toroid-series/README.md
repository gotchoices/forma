# Toroid Series  *(concluded)*

Can a geometric series of nested toroidal sub-dimensions correct the
WvM charge deficit (~9%) and converge to the measured electron charge?

## Result

**Null result.** The series hypothesis was well-formed and the geometric
series is uniquely selected by smoothness, but the 9% deficit it targets
is not a robust physical prediction — it is an artifact of WvM's choice
of a spherical cavity volume. A more accurate toroidal cavity calculation
gives q = 14–128× e, and the sphere turns out to be justified by the
"rotation horizon" argument, not the toroidal topology.

The deficit carries ~5–10% systematic uncertainty from geometric
assumptions, making any exact series fit to named constants unreliable.

## What Was Learned

- The smoothest N-term decomposition of any deficit is always geometric (F5).
- Named-constant ratios 1/11 and 4πα fit the 9% target to < 0.3% (F2).
- The Gemini dialog's specific claims (α-series, ϕ-scaling) are
  quantitatively wrong (F3, F4).

## Spawned Study

The geometric analysis that blocked this study raised a deeper question:
*what effective geometry reproduces q = e?* This is pursued in
`../toroid-geometry/`.

## Scripts

All scripts require the project virtual environment (`.venv` at the
repo root) and the shared library (`../lib/`). Run from the repo root:

    source .venv/bin/activate
    python studies/toroid-series/scripts/01_wvm_baseline.py

| Script | Findings | Description |
|--------|----------|-------------|
| `01_wvm_baseline.py` | F1 | Reproduces WvM Eq. 5 charge prediction (q ≈ 0.91e). Establishes the correction factor S ≈ 1.0985. |
| `02_series_scan.py` | F2 | Scans 18 named candidate ratios for a geometric series summing to S. Tests P1 (series hypothesis) and P2 (recognizable ratio). |
| `03_scaling_dimensions.py` | F3 | Counts nested layers to reach Planck length for each ratio. Tests P3 (finite terms) and P4 (dimensional correspondence). |
| `04_dialog_claims.py` | F4 | Verifies or refutes 8 quantitative claims from `reference/gemini-tensors-compton-toroid.md`. |
| `05_free_series.py` | F5 | Unconstrained optimization: finds the smoothest N-term decomposition of the deficit. Requires `scipy` and `numpy`. |

## Other Files

| File | Contents |
|------|----------|
| `theory.md` | Hypotheses, propositions P1–P4, mathematical framework, outcome |
| `findings.md` | Results F1–F5 and conclusion |
| `STATUS.md` | Task checklist (concluded) |
