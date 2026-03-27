# R35 Findings

## Track 1 — Threshold detection statistics

### F1. Compton asymmetry makes Cd-109 insensitive to pre-load

At 88 keV, the Compton max transfer is only 25.6%.  Detector 2
always receives ≥ 74.4% of E_γ, which exceeds the SCA lower level
(66.7%).  Det 2 fires on EVERY interaction event regardless of
pre-load.

Because both the enhanced coincidence rate (Re) and the det-1
singles rate (S1) are proportional to P(det 1 fires), this
probability cancels in the ratio:

    Re/Rc = 1/(2τR) ≈ 1667

independent of the pre-load distribution.  This over-predicts
Reiter's Cd-109 result (Re/Rc = 33) by 51×.

### F2. Na-22 (511 keV) is genuinely pre-load-sensitive

At 511 keV, η_max = 2/3.  Det 2 receives as little as 1/3 of
E_γ after maximum Compton scatter, which is below the SCA lower
level.  BOTH detectors need pre-load to fire.  Re/Rc depends
strongly on the pre-load distribution:

| Pre-load distribution | Re/Rc |
|-----------------------|-------|
| Uniform(0, 0.30)     | 400   |
| Uniform(0, 0.40)     | 848   |
| Uniform(0, 0.45)     | 997   |
| Uniform(0, 0.50)     | 1108  |
| Exp(mean = 0.20)     | 1318  |
| Beta(2, 5)           | 1432  |

A uniform distribution with max ≈ 0.43 × E_γ matches Reiter's
Na-22 Re/Rc ≈ 963.

### F3. The SCA upper limit resolves the Cd-109 over-prediction

The dynamic equilibrium Monte Carlo — where pre-loads evolve via
continuous filling and leakage — reproduces Cd-109 when atoms are
nearly fully loaded (⟨E_pre⟩/E_th ≈ 0.98).

At high pre-load, the SCA UPPER limit becomes active: total energy
E_pre + E_dep exceeds the photopeak window, rejecting events.  This
suppresses both singles and coincidences, bringing Re/Rc down from
1667 to ~33.

| fill_rate | leak_rate | ⟨preload⟩ | Re/Rc |
|-----------|-----------|-----------|-------|
| 0.010     | 10⁻⁵      | 0.976     | 33.5  |
| 0.010     | 10⁻⁴      | 0.977     | 34.8  |
| 0.010     | 10⁻³      | 0.977     | 33.5  |

The mechanism: most atoms are nearly fully loaded; only atoms with
moderate pre-load (neither too high nor too low) can produce a pulse
within the SCA window.  The fill_rate/leak_rate ratio determines
the steady-state pre-load level and hence Re/Rc.

### F4. Cd-109 and Na-22 probe different physics

The two isotopes constrain the model differently:

- **Cd-109 (88 keV):** Probes the SCA upper limit mechanism.
  The pre-load must be nearly maximal (⟨E_pre⟩ ≈ 0.98 E_th)
  for the model to work.  Re/Rc ≈ 33 requires that most atoms
  are "nearly full."

- **Na-22 (511 keV):** Probes the pre-load distribution shape.
  The pre-load must be moderate (⟨E_pre⟩ ≈ 0.4 E_th for the
  parametric model).  Re/Rc ≈ 963 requires that enough atoms
  have pre-load above the coincidence threshold, but not so
  many that Re/Rc saturates at 1/(2τR).

### F5. Joint constraint creates tension

Matching BOTH results simultaneously with the SAME physical
parameters requires energy-dependent scaling.  The absolute
fill rate (keV/s) should be identical in both experiments
(same detector material, same environment).  In normalized
units (fraction of E_γ):

| Isotope | E_γ (keV) | Required ⟨E_pre⟩/E_γ |
|---------|-----------|----------------------|
| Cd-109  | 88        | ~0.98                |
| Na-22   | 511       | ~0.40                |

In absolute keV: Cd-109 needs ⟨E_pre⟩ ≈ 86 keV, while Na-22
needs ⟨E_pre⟩ ≈ 204 keV.  These are DIFFERENT absolute pre-loads,
which is physically plausible if the source contributes to the
fill rate (higher-energy gammas deposit more energy per event).

With the same absolute fill rate, the dynamic MC gives Na-22
Re/Rc ≈ 1200–1300 (vs. Reiter's 963).  A 30% discrepancy —
in the right ballpark but not a clean match.

### F6. The fill_rate/leak_rate ratio is the master parameter

The dynamic MC shows that Re/Rc is controlled by the steady-state
mean pre-load ⟨E_pre⟩/E_th.  This in turn depends on the ratio
fill_rate / leak_rate:

- High ratio → ⟨E_pre⟩ → 1 → SCA UL cuts in → low Re/Rc
- Low ratio → ⟨E_pre⟩ → 0 → no threshold events → Re/Rc = 0
- Moderate ratio → intermediate ⟨E_pre⟩ → Re/Rc ≈ 1/(2τR)

The Cd-109 match (Re/Rc ≈ 33) requires ⟨E_pre⟩ ≈ 0.98, which
means fill_rate ≫ leak_rate (atoms fill up much faster than they
leak).  The storage lifetime 1/leak_rate is not tightly constrained
by Track 1 alone — any leak_rate ≤ 10⁻³ per event interval works.

### F7. Connection to R35 Tracks 3–4

Track 1 establishes:

1. **The threshold model CAN reproduce Reiter's Cd-109 (Re/Rc ≈ 33)**
   via the SCA upper limit mechanism — but requires ⟨E_pre⟩/E_th ≈ 0.98.

2. **Na-22 (Re/Rc ≈ 963)** constrains the pre-load distribution:
   uniform max ≈ 0.43 E_γ, or exponential mean ≈ 0.3–0.4 E_γ.

3. **The master parameter is fill_rate/leak_rate.**  Track 3
   (cross-shear leakage) determines leak_rate.  Track 4 (coupling
   strength) determines fill_rate.  Together they predict whether
   the steady-state ⟨E_pre⟩ falls in the range needed for Cd-109.

4. **The SCA window width is critical.**  The upper limit mechanism
   depends on whether Reiter's actual SCA window was tight enough
   to reject events at ~1.5× E_γ.  This is an experimental detail
   that could be verified from Reiter's original setup description.
