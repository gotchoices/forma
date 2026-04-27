# R64 Track 17 — Pool item ac: σ_pS_tube residual sweep at moderate magnitudes

**Status: complete.  Result: NEGATIVE.  σ_pS_tube + H2 at moderate
magnitudes (well inside signature band, not at the edge) gives
NO V(r) trough at all — kinetic-style term dominates everywhere,
cross term is too weak to compete.  Only the singular edge gives
attractive V(r), and that fails the QM gate (Track 13b).
σ_pS_tube cannot be the source of nuclear volume binding in any
honest regime.**

Script:
[`scripts/track17_pool_ac_residual_sweep.py`](scripts/track17_pool_ac_residual_sweep.py)
Output:
[`outputs/track17_pool_ac_residual_sweep.csv`](outputs/track17_pool_ac_residual_sweep.csv)

---

## Premise

After Track 13b ruled out σ_pS_tube + H2 at the singular edge
(σ_eff_tube = −116) on QM grounds, and Track 15 showed nuclear
binding decomposes as Ma compound + SEMF residual with a missing
~7 MeV/n volume term, the user proposed: **maybe σ_pS_tube only
needs to provide the 7 MeV/n volume contribution, not the full
binding force.**  At smaller σ_pS_tube (away from the singular
edge), the V(r) trough would be shallower, possibly avoiding the
QM-gate failure.

This track tests that hypothesis directly: sweep σ_pS_tube at
moderate magnitudes (0.001 to 0.115) and check whether any value
gives:
- A reasonable V(r) trough (depth ~ a few MeV consistent with the
  per-nucleon volume term)
- The right deuteron behavior (1 bound state, not 3)
- Sensible mean-field volume contribution

Plus: scan σ_pS_ring alongside for comparison (Phase 10a found
ring is α-inert; this checks whether ring contributes to nuclear
binding at moderate magnitudes).

## Method

For each candidate σ_pS_tube (and separately σ_pS_ring) value at
Point A:
1. Build metric with σ_pS_tube + H2 (or σ_pS_ring without H2 since
   ring is α-inert by itself)
2. Compute σ_eff_tube via Schur reduction
3. Compute V(r) for pn channel at Point A parameters
4. Find V_min and r_min
5. Estimate mean-field volume contribution: ρ_sat · ∫V(r) d³r
6. Apply QM gate to count bound states

## Results

### F17.1.  No V(r) trough at moderate σ_pS_tube

Across σ_pS_tube ∈ [0.001, 0.115] (well inside the signature
band):

| σ_pS_tube | σ_eff_tube | V_min(pn) (MeV) | r_min (fm) | bound states |
|---:|---:|---:|---:|---:|
| 0.001 | −0.001 | **+0.10** (no trough) | 20.0 (boundary) | 0 |
| 0.005 | −0.005 | +0.10 | 20.0 | 0 |
| 0.01 | −0.010 | +0.10 | 20.0 | 0 |
| 0.025 | −0.026 | +0.10 | 20.0 | 0 |
| 0.05 | −0.06 | +0.10 | 20.0 | 0 |
| 0.075 | −0.12 | +0.10 | 20.0 | 0 |
| 0.10 | −0.28 | +0.10 | 20.0 | 0 |
| 0.115 | −0.74 | **+0.08** (still no trough) | 20.0 | 0 |

**At every moderate σ_pS_tube value, V_eff(r) > 0 throughout the
range tested.**  No attractive trough.  No bound states.  No
deuteron formed via the σ_pS_tube V(r) mechanism.

The mean-field volume estimate at saturation density gives
**+395 to +400 MeV/nucleon** (positive — repulsive).  This is
the kinetic-like `4·(ℏc)²/r²` term dominating; the cross term
σ_eff·n_pt·k integrand is too small to give attractive volume
binding.

### F17.2.  Why this happens — structural argument

For an attractive trough to form, the attractive cross term must
compete with the repulsive kinetic-like term.  Set them equal:

```
|σ_eff · n_pt · ℏc / r| > 4·(ℏc)² · k² / 2  (V_eff ≈ ... / 2m_Ma)
|σ_eff · n_pt| > 2·ℏc / r
```

For n_pt = 6 at r = 1 fm: **|σ_eff| > 66 MeV** is required.

But at moderate σ_pS_tube (0.001 to 0.115), σ_eff_tube ranges
from 0.001 to 0.74 — **two orders of magnitude too small** to
compete with the kinetic term.

The trough only emerges when σ_eff is amplified enormously by
proximity to the singular metric edge.  At σ_pS_tube = 0.12505
(Track 11), σ_eff = 116 — barely enough to compete with kinetic
at r = 1 fm, giving the −32 MeV trough that Track 13b then
showed fails QM.

**There is no honest regime where σ_pS_tube + H2 V(r) gives an
attractive trough that passes QM.**

### F17.3.  σ_pS_ring also fails (separately)

Tested σ_pS_ring at moderate magnitudes (no H2 needed; ring is
α-inert per Phase 10a).  For pn (n_pr = 0), the cross term
σ_pS_ring · n_pr is **identically zero** because the ring
windings cancel for the deuteron.  V_eff(r) for pn is unchanged
from baseline at any σ_pS_ring magnitude.

| σ_pS_ring | σ_eff_ring | V_min(pn) | bound states |
|---:|---:|---:|---:|
| 0.001 | −0.001 | +0.10 (unchanged) | 0 |
| 0.05 | −0.06 | +0.10 (unchanged) | 0 |
| 0.10 | −0.28 | +0.10 (unchanged) | 0 |
| 0.122 | −2.48 | +0.11 (slight upward) | 0 |

σ_pS_ring contributes nothing to deuteron physics regardless of
magnitude.

(For pp/nn, σ_pS_ring has nonzero coupling because n_pr = ±4.
Phase 10a covered this; not re-tested here since the deuteron
is the diagnostic case.)

### F17.4.  No σ_pS_tube candidate gives both good deuteron AND volume

The primary search question — "does any σ_pS_tube value give
B(²H) = 2.22 MeV with single bound state AND volume contribution
~14 MeV/n?" — yields **no candidates**.

No σ_pS_tube value produces an attractive V(r) at all in the
tested range.

## What this finding establishes

1. **σ_pS_tube + H2 cannot be the volume-binding mechanism.**
   At moderate σ, no trough forms.  At edge, V(r) fails QM
   (Track 13b).  No middle ground exists.
2. **σ_pS_ring contributes nothing to deuteron physics.**
   The ring-cancellation `n_pr = 0` zeros the cross term
   identically.
3. **The kinetic-style `4·(ℏc)²·k²` term in the m² formula is
   structurally repulsive** and dominates at moderate σ.  This
   isn't a fitting issue; it's how the formula scales.
4. **Pool item ac (σ_pS_tube residual sweep) is closed
   negatively.**  Pool item m (Yukawa propagator) cannot be
   ruled out as the architecturally indicated path for the
   volume term.
5. **R29's earlier conclusion** that the residual binding "may
   represent S mode interactions" is now backed by independent
   evidence — but the SPECIFIC S mechanism (σ_pS_tube V(r)) we
   tested does not work.

## What this finding does NOT establish

- Whether *some other* metric off-diagonal (untested) could
  deliver volume binding without the trough-shape problem.
- Whether a different kinematic embedding (not the
  `4·(ℏc)²·k²` form) would change the picture.
- Whether the volume term might emerge from many-body effects
  (Pauli statistics, mean-field cooperative effects) that don't
  show up in 2-body V(r) at all.

## Implications for architecture

The volume-binding mechanism for nuclear physics is **not in
σ_pS_tube** in any tested regime.  The honest list of remaining
candidates:

1. **Pool item m (Yukawa propagator-based)**: a different cross-
   term form with exponential cutoff.  The geometric reading
   (compactification scale, not particle exchange) keeps it
   structural.
2. **Different kinematic embedding**: replace `4·(ℏc)²·k²` with
   something less repulsive at small r.  Would change V(r)
   shape qualitatively.
3. **Many-body cooperative binding**: the volume term might be
   inherently a many-body effect not capturable in 2-body V(r).
   Mean-field Hartree-Fock with appropriate effective interaction
   gives the SEMF coefficients in standard nuclear physics.
4. **Standard nuclear physics overlay**: accept that V(r) is
   imported from data (e.g. Argonne v18 or chiral EFT); MaSt
   provides the substrate (modes, masses, EM, weak); nuclear
   physics handles binding.

## Status

**Track 17: complete and negatively decisive.**  σ_pS_tube V(r)
is genuinely not the strong-force / volume-binding mechanism at
any magnitude tested.  Pool item ac is closed.

The architecturally indicated next test is **pool item m** with
the geometric reinterpretation, OR acceptance that nuclear
binding is a separate-from-MaSt problem (overlay rather than
derivation).
