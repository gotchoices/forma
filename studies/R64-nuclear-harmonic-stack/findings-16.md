# R64 Track 16 — Pool item v opening phase: magnetic anomaly proxy scan

**Status: opening phase complete.  Result: σ_pS_tube and σ_eS_tube
activations DO shift the metric quantities relevant to magnetic
coupling (G⁻¹[X_TUBE, S_x]), but the proxy I used is too crude to
extract anomaly values.  First-order shifts dominate (linear in σ),
which represent magnetic baseline coupling rather than QED-style
anomaly corrections.  A proper magnetic-α extraction (analogous to
α-Coulomb) is needed before quantitative comparison to a_e ≈ 1.16 ×
10⁻³ or a_p ≈ 1.79 is possible.  Pool item v requires a real
derivation, not a quick scan.**

Script:
[`scripts/track16_pool_v_anomaly_scan.py`](scripts/track16_pool_v_anomaly_scan.py)

---

## Premise

Track 11's σ_pS_tube + H2 activation produces a small (4 × 10⁻⁴)
second-order shift in α-Coulomb at the proton, suggestively close
to the order of magnitude of QED anomalous magnetic moments
(a_e ≈ 1.16 × 10⁻³, a_p ≈ 1.79).  Pool item v hypothesizes that
this second-order shift IS the source of the anomaly — and the
H2 mechanism that delivers strong-force trough also delivers g-2
without needing QFT loop calculations.

The opening phase: a quick numerical scan to see whether σ_pS
activation shifts any quantity that connects to the magnetic
sector at the right scale.  If yes, a full derivation is
warranted.  If no, σ_pS isn't the anomaly source.

## Method

Scan σ_pS_tube and σ_eS_tube at moderate-to-edge magnitudes;
compute G⁻¹[X_TUBE, S_x] for each particle's tube sector
(analogous to G⁻¹[X_TUBE, t] for α-Coulomb extraction).
Normalize by √α (a natural reference scale).  Compare to
observed g-2 anomalies.

## Results

### F16.1.  Activation does shift the magnetic-sector G⁻¹ entries

At σ_pS_tube = 0 (baseline), G⁻¹[X_TUBE, S_x] = 0 for every X.
This is expected: with no σ_xS coupling, sheets are decoupled
from the spatial S directions, and no magnetic-channel coupling
exists.

Activation at any nonzero σ_pS_tube produces nonzero
G⁻¹[p_t, S_x].  The shift grows essentially linearly with
σ_pS_tube at small magnitudes:

| σ_pS_tube | G⁻¹[p_t, S_x] | (shift)/√α |
|---:|---:|---:|
| 0.001 | 2.13 × 10⁻² | 0.249 |
| 0.005 | 1.07 × 10⁻¹ | 1.249 |
| 0.01 | 2.14 × 10⁻¹ | 2.509 |
| 0.025 | 5.55 × 10⁻¹ | 6.492 |
| 0.05 | 1.27 | 14.83 |
| 0.115 | 1.58 × 10¹ | 184.9 |
| 0.124 | 1.50 × 10² | 1755 |
| 0.12505 (edge) | 2.94 × 10³ | 34456 |

Linear at small σ; super-linear approaching the singular edge.

### F16.2.  The proxy is too crude for anomaly extraction

The shift values divided by √α range from 0.25 (at σ_pS_tube =
0.001) to 34000 (at edge).  Compared to a_p = 1.79, these proxy
values are "much too small" or "much too large" — never naturally
near a_p = 1.79 except by coincidence at one specific σ_pS_tube.

**This is because the proxy I built measures the FIRST-ORDER
shift in magnetic coupling.**  In QED:
- First-order shift = baseline magnetic coupling (sets g = 2)
- Second-order shift = anomaly (a = (g−2)/2 ≈ α/(2π))

My proxy doesn't distinguish first and second order; it just
measures the linear coupling growth.  An anomaly extraction
needs the *second-order* shift in a properly-defined magnetic-α
quantity, which requires more careful Schur reduction than a
linear scan provides.

### F16.3.  Cross-sheet propagation through aleph is small

Tested whether σ_pS_tube activation propagates through aleph
to affect the electron's magnetic-sector G⁻¹ entry:

| σ_pS_tube | σ_eS_tube | G⁻¹[e_t, S_x] | shift/√α |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0.01 | 0 | −1.4 × 10⁻⁸ | −1.7 × 10⁻⁷ |
| 0.05 | 0 | −8.5 × 10⁻⁸ | −1.0 × 10⁻⁶ |
| 0.10 | 0 | −4.0 × 10⁻⁷ | −4.6 × 10⁻⁶ |

Cross-sheet effects are tiny (10⁻⁸ to 10⁻⁶ at moderate σ_pS_tube).
At least at first order, sheets don't talk to each other very
much through the metric structure.

This is informative: if a_e (electron anomaly) requires e-sheet
activation to drive it (rather than p-sheet activation feeding
through aleph), then computing a_e requires explicitly
activating σ_eS_tube — not just σ_pS_tube.

## What this finding establishes

1. **σ_pS_tube and σ_eS_tube activations DO shift the metric
   quantities relevant to magnetic coupling.**  Architecturally
   the right structural piece is in place.
2. **The simple linear shift is not the anomaly.**  The
   anomaly is a second-order quantity.  My proxy can't extract
   it.
3. **Cross-sheet effects through aleph are small.**  Each
   sheet's anomaly likely needs its own sheet activation.

## What this finding does NOT establish

- Whether σ_pS_tube + H2 actually produces a_p ≈ 1.79 (proton
  anomalous magnetic moment).
- Whether σ_eS_tube + e-H2 produces a_e ≈ 1.16 × 10⁻³ (electron
  anomalous moment).
- Whether the "edge methodology" is required to extract the
  anomaly, or whether moderate σ values suffice.

These require the proper magnetic-α extraction (Phase 16b),
which I declined to write up as a quick scan.

## Implications

Pool item v is **not closeable** from this scan alone.  The
opening phase confirms the architecture has the right structural
piece (σ activation perturbs magnetic-sector G⁻¹) but doesn't
extract anomaly values.

For closing pool item v, three sequential steps remain:

1. **Phase 16b: derive the magnetic-α formula structurally.**
   Analog to α-Coulomb but using G⁻¹[Ma, S_x] column.  This is
   the substantive new derivation work.
2. **Phase 16c: compute second-order shift under H2 activation.**
   This is the anomaly proxy.
3. **Phase 16d: compare to a_e, a_p, a_μ.**

Estimated work: ~half-day analytical for 16b, hour-scale numerical
for 16c/16d.  Worth doing if model-G prioritizes magnetic-anomaly
account.  Currently deferred.

## Status

**Track 16 / Pool item v opening phase: complete.  Conclusion is
INCONCLUSIVE.**  Architecture has the right structural piece;
proper derivation needed to extract anomaly values.

This finding informed the user's "α scaling vs full strength"
question — if σ_pS is α-scaled, the second-order shift would
naturally be at α-anomaly scale; if full-strength, the
first-order shift dominates and the proxy is the "magnetic
baseline" not the anomaly.  Disambiguating the scaling is part
of the full magnetic-α extraction.
