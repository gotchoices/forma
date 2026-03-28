description: Substantive errors found in studies that the findings did not acknowledge
dependencies: none
files:
  - studies/S3-knot-zoo/scripts/01_knot_survey.py
  - studies/R7-torus-capacitance/scripts/torus_charge.py
  - studies/R11-prime-resonance/scripts/track7_wave_superposition.py
  - studies/R11-prime-resonance/scripts/track8_mode_spectrum.py
  - studies/R12-self-consistent-fields/scripts/track2_curved_geodesics.py
  - studies/R19-shear-charge/scripts/track2_energy_balance.py
  - studies/R26-neutrino-t4/scripts/track1b_triplet_search.py
  - studies/R29-atoms-and-nuclei/scripts/track2_hydrogen.py
  - studies/R29-atoms-and-nuclei/scripts/track4_re_and_stability.py
  - studies/R32-alpha-running/scripts/track1_kk_running.py
  - studies/R34-midpoint-coupling/scripts/track5_known_particles.py
  - studies/R35-threshold-coupling/scripts/track2_elastic_torus.py
  - studies/R35-threshold-coupling/scripts/track3_three_layer.py
  - studies/R37-membrane-mechanics/scripts/track1_radiation_stress.py
  - studies/lib/ma.py
----

Full audit of all 37 studies (S1-S3, R1-R38) performed in chronological order.
Only errors the findings themselves were blind to are listed.
Studies not listed had no blind errors found.

---

## Shared library (studies/lib/)

### 1. mode_charge docstring contradicts code (ma.py:364-392)

The docstring says "odd tube windings" contribute charge, implying even
windings contribute zero.  The code implements `Q = -n[0] + n[4]` with no
parity check -- n1 = 2 would give Q = -2, not 0.  The **code is correct**
per the KK formula; the **docstring describes the older WvM mechanism**
that was superseded.  Any reader trusting the docstring would misunderstand
the charge rule.

### 2. compute_scales crashes on small r (ma.py:218-219)

`solve_shear_for_alpha(r)` returns `None` for r < ~0.25.
`compute_scales` passes this to `mu_12(r, None)`, which raises an opaque
`TypeError`.  No guard or meaningful error message.

### 3. geometric_sum(1.0, n) returns NaN (series.py:10)

Division by zero when r = 1.0.  Correct result is n + 1.

---

## S3 -- Knot Zoo

### 4. Wrong torus geometry for path lengths (01_knot_survey.py:87-88)

Uses a/R = 1/sqrt(pi*alpha) ~ 6.60 (the *field extent* parameter from S2)
as the physical tube radius for computing geodesic path lengths and mass
ratios.  The findings explicitly distinguish orbit from field extent (F1)
but the script uses the field extent value anyway.  Script 02 correctly
uses a/R = 0.01 (thin torus) for its charge calculation.

All mass-ratio numbers in the output table are quantitatively wrong.
The qualitative null result (no known particle mass ratios) likely survives
since no a/R value produces the needed 207x or 3477x ratios, but the
specific numbers reported are unreliable.

---

## R7 -- Torus Capacitance

### 5. Code does not implement the model described in the README (torus_charge.py:130-148)

The README describes E-field directed along the local surface normal
(synchronized circular polarization model).  The code distributes point
charges along the geodesic and computes standard isotropic Coulomb fields.
The `torus_normal` function (lines 55-62) is defined but never called.
Findings partially acknowledge this under "Possibility B" (F4) but do not
flag that the synchronized-CP model was never actually implemented.

---

## R11 -- Prime Resonance

### 6. r_approx(q) is 40% wrong at q = 137 (track7:215, track8:62)

The linear approximation `r_approx(q) = 0.0025*(q-100) + 0.10` gives
r(137) = 0.19; the correct value from R8 is ~0.31 (40% error).  Mode
spectra and beat-frequency pair counts in F10/F14 are computed at
incorrect aspect ratios.  Qualitative conclusions (no prime/composite
distinction) likely survive, but specific numerical values in the
findings tables are wrong.

---

## R12 -- Self-Consistent Fields

### 7. IndentationError prevents script execution (track2_curved_geodesics.py:400-408)

Lines 400-408 are indented one level deeper than line 399 with no
enclosing control structure.  This is a Python syntax error -- the
script cannot run as written.  Part F output could not have been
produced from this version.

### 8. Holonomy "verification" is a tautology (track2_curved_geodesics.py:356-373)

The numerical verification integrates Gaussian curvature K over the
**entire torus** (always zero by Gauss-Bonnet for chi = 0), not over
the geodesic-enclosed region.  The theoretical conclusion is correct
but the numerical check verifies nothing beyond integral(K*dA) = 0.

---

## R19 -- Shear-Induced Charge

### 9. Hardcoded g_r = 0.5 for all aspect ratios (track2_energy_balance.py:98)

The Coulomb self-energy geometric factor `g_r` should depend on the
torus aspect ratio r.  Using 0.5 for all r (the scan covers r = 0.25
to 4.0) introduces a systematic error in the energy-balance minima
reported in F10.  The qualitative conclusion (shear is energetically
cheap) is robust; specific minimum locations may shift.

---

## R26 -- Three Tori (Ma)

### 10. Sterile mode exclusion over-counts by up to 3 (track1b_triplet_search.py:143-148)

The exclusion logic for removing triplet modes from the sterile count
only excludes positive-p, positive-q variants.  Antiparticle modes
(negative p or q) of the triplet are not excluded.  Inflates sterile
count by up to 3.  Does not change the conclusion (no zero-sterile
solution exists) since it makes the problem look worse.

---

## R29 -- Atoms and Nuclei

### 11. Yukawa sum includes non-mediating dimensions (track2_hydrogen.py:88-101)

The energy_shift() function sums Yukawa corrections from all 4
electron/proton dimensions (indices 0, 1, 4, 5).  In KK gauge theory,
A^2 (electron ring) does not mediate e-p interaction because the proton
has n2 = 0 (zero coupling).  Similarly for A^6.  Only A^1 and A^5
should contribute.  The electron-ring correction (-0.022 eV at r_e=6.6)
erroneously inflates the total by ~3%.  Since the findings already
identify the entire KK boson Yukawa as 10^4 too large (F15), this
did not change conclusions.

### 12. nuclear_mode_energy assumes scaling law without searching (track4_re_and_stability.py:57-91)

Hardcodes n5 = A, n6 = 2A and only optimizes n2, n3.  The scaling law
was discovered empirically in Track 3 at r_e = 6.6, but Track 4
applies it across the full r_e sweep without verifying it holds at
other r_e values.  The finding "r_e = X minimizes error" is really
"r_e = X minimizes error under the assumed scaling law."

---

## R32 -- Alpha Running

### 13. Beta function coefficients overestimate running by 4/3 (track1_kk_running.py:101-110)

Uses b = 4/3 for Dirac fermions and b = 1/3 for complex scalars.
The correct one-loop QED vacuum polarization coefficients (in the
convention Delta(1/alpha) = -b*Q^2/(3*pi)*ln(E/m)) are b = 1 for
Dirac and b = 1/4 for complex scalars.  The running is overestimated
by a factor of 4/3 for all species.  The suppression factor in F5
should be ~4.8e-6, not 6.4e-6.  Qualitative conclusion (catastrophic
running, need ~10^5 suppression) is unchanged.

---

## R34 -- Midpoint Coupling

### 14. Same beta coefficient error as R32 (track5_known_particles.py:92-96)

Uses the same overestimated b = 4/3 (Dirac) and b = 1/3 (scalar).
Absolute Delta(1/alpha) values in F13-F17 are ~33% too high.
**Internal inconsistency**: Track 2 (track2_log_running.py) uses
the correct b = 1 and b = 1/4, so Tracks 2 and 5 of the same study
use different conventions.

---

## R35 -- Threshold Coupling

### 15. Thermal disruption model conflates parameters (track2_elastic_torus.py)

Track 2 substitutes (K*kT*amplification)^2 for sigma_enu^2 in the
thermal disruption model, conflating an energy-based estimate with
a cross-shear coupling parameter.  The storage lifetime and W/N ratio
numbers in F32/F34 depend on this unvalidated substitution.

### 16. em_radiation_rate is dimensionally wrong (track3_three_layer.py)

The function is missing omega^2 and d^2 (dipole moment squared) factors.
The rate is stated to be zero for uncharged neutrino modes (correct),
so the dimensional error does not affect conclusions, but the printed
"hypothetical" comparison numbers are incorrect.

---

## R37 -- Membrane Mechanics

### 17. L1/L2 (tube/ring) labels swapped (track1_radiation_stress.py and others)

The R37 scripts compute L1 = 2*pi*lambda_bar_C*mu (which is the ring
circumference per the lib convention), then set L2 = r*L1 (the tube).
This is opposite to the lib where r = L_tube/L_ring = L1/L2.  All
numerical results are correct because they depend on the product
L1*L2 and the ratio r, but printed dimension labels have tube and
ring reversed throughout R37.
