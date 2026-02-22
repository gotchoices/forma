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
broader question (can sub-structure explain the deficit?) remains open.

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

## F6. WvM Sensitivity to Geometric Assumptions

**Script:** `scripts/06_wvm_sensitivity.py`
**Bears on:** All propositions (robustness of the target S ≈ 1.0985)

The WvM charge formula q = (1/2π)√(3ε₀ℏc) comes from equating the
average E-field inside a cavity to the Coulomb field at a characteristic
radius. Two free geometric choices set the result:

- **Cavity volume V** — determines the average field from the photon
  energy via u = hc/(λV)
- **Charge radius r_c** — where ⟨E⟩ is matched to the Coulomb field

General relation: q(V, r_c) = 4πε₀ r_c² √(hc/(ε₀λV)), so q ∝ r_c²/√V.

### Results by variation

**A. Cavity shape (torus vs sphere):**
A toroidal cavity with major radius R = λ/(2π) and tube radius a makes
things *worse*, not better. For any physically reasonable a/R ≤ 1, the
torus volume is 4–15% of the sphere, concentrating the field and giving
q = 2–47× e (far too large). To get q = e, the tube radius would need
a/R ≈ 2.34, meaning the tube is wider than the hole — geometrically
degenerate. The spherical approximation is actually *generous*.

**B. Charge radius:**
With the spherical cavity, only a 4.8% increase in r_c (from r̄ to
1.048 r̄) closes the deficit entirely. The charge is very sensitive
to this parameter — q ∝ r_c².

**C. E-B energy partition (corrected):**
WvM explicitly set U_E = U_B = U/2 (§3 of the paper). The derivation
is correct: the factor of ½ from U_E = U/2 cancels with the ½ in
W_E = ε₀E²/2, giving E² = u_total/ε₀. There is no free parameter
here. (An earlier version of this analysis incorrectly treated the
E-B partition as a tunable parameter.)

### Key numbers

| Route to q = e | Required change |
|----------------|-----------------|
| Shrink V only | V → 0.83 × V_sphere (torus a/R = 2.34, degenerate) |
| Increase r_c only | r_c → 1.048 × r̄ (5% shift) |

### Implications

The 9% deficit is **within the geometric uncertainty** of WvM's
approximations. A ~5% shift in the charge radius eliminates it. This
means:

1. The deficit is not a robust, high-confidence prediction. It depends
   sensitively on exactly where you evaluate the Coulomb field.
2. A more careful field calculation (actual toroidal EM modes rather
   than uniform density in a sphere) could shift q/e in either
   direction and might eliminate the deficit entirely.
3. The series hypothesis remains viable if we take WvM's specific
   geometry at face value, but we should be aware that the target
   itself carries ≈5–10% systematic uncertainty.

This tempers the interpretive weight of any exact match to named
constants. A fit to r = 1/11 (0.14% error) looks impressive, but the
target it's fitting has ~5% structural uncertainty.

---

## F7. Toroidal Cavity EM Modes (Maxwell's Equations)

**Script:** `scripts/07_toroidal_modes.py`
**Bears on:** All propositions — challenges the premise of the study

Solved Maxwell's equations (Helmholtz equation) for the lowest
resonant mode of a toroidal cavity, replacing WvM's uniform-field-
in-a-sphere with the actual field distribution.

**Method:** Used axial symmetry to reduce 3D → 2D, then the
substitution φ = √ρ·ψ to obtain a symmetric eigenvalue problem
on the tube cross-section. Solved with finite differences (N = 81)
and scipy's sparse eigensolver. Validated against the known
straight-waveguide limit (j₀₁² = 5.783, error < 0.6%).

### Results

For every tube radius a/R from 0.10 to 0.95:

| a/R | q/e | F (concentration) |
|-----|-----|-------------------|
| 0.10 | 127.6 | 3.73 |
| 0.30 | 42.5 | 3.73 |
| 0.50 | 25.5 | 3.74 |
| 0.70 | 18.3 | 3.76 |
| 0.90 | 14.3 | 3.80 |
| 0.95 | 13.6 | 3.82 |

The charge is always q ≫ e. No tube radius gives q ≤ e.

The field concentration factor F ≈ 3.7–3.8 means the fundamental
mode peaks at the tube center (transport radius R) about 3.8× the
volume average — this is the expected J₀ profile of a circular
cavity's fundamental mode. This makes q even larger than a
uniform-field-in-torus estimate.

The azimuthal mode number (n = 0, 1, or 2) barely matters —
the charge changes by less than 2%.

### Why this happens

The toroidal volume is 15–200× smaller than WvM's sphere (diameter λ):

    V_sphere = πλ³/6 ≈ 7.5 × 10⁻³⁶ m³
    V_torus(a/R=0.5) ≈ 3.6 × 10⁻³⁸ m³   (ratio: ~200×)

Same photon energy in a much smaller volume → much higher energy
density → much stronger E-field → much larger apparent charge.
The F ≈ 3.8 mode concentration further amplifies this.

### Implications — this is the key finding

**WvM's choice of a sphere of diameter λ is what makes q ≈ e.**
It's not a minor approximation — it's the central reason the charge
comes out close to the elementary charge. The actual toroidal
geometry gives q = 14–128× e, nowhere near 0.91e.

This reframes the study. The question is no longer "what series
corrects a 9% deficit?" but rather:

1. **Why does a sphere of diameter λ give such a good charge
   estimate?** Is there a deeper reason, or is it coincidental?
2. **Is the WvM charge derivation physically meaningful at all?**
   If the geometry that actually matches the model's topology gives
   q ≫ e, the charge derivation may be capturing something other
   than the literal field distribution.
3. **Should the study pivot?** The series hypothesis assumed the
   9% deficit was a precise, physically meaningful number. F7 shows
   it's an artifact of a geometric choice (sphere vs torus) that
   swings q by a factor of 15–140.

### F7 addendum: What script 07 does and does not compute

Script 07 solves for the lowest **standing-wave eigenmode of a
hard-walled toroidal cavity**. This is NOT the same as WvM's model,
which describes a photon **propagating** as a traveling wave along
a double-loop geodesic. The differences:

| | WvM photon | Script 07 cavity mode |
|---|---|---|
| Wave type | Traveling wave, energy flows around torus | Standing-wave eigenmode |
| E-field | Always radially inward (topological) | Oscillating cavity pattern |
| Boundary | Self-confinement, fields decay smoothly | Hard wall at tube radius a |
| Cross-section | Guided-wave profile (Gaussian-like?) | J₀ cavity profile (F ≈ 3.8) |

The cavity mode overstates the field concentration (F ≈ 3.8 vs ~1
for a uniform or Gaussian profile), but the dominant effect is the
**volume**: any toroidal confinement region gives q ≫ e because the
torus is 15–200× smaller than WvM's sphere. This holds regardless
of the cross-sectional profile.

---

## F8. What WvM Gets Right vs. What Depends on Geometry

**No script** — analytical review of the WvM paper (ref/WvM.pdf §2–5)

WvM derive three electron properties. Their robustness differs
fundamentally:

### Spin: exact (topological, no geometric assumptions)

The double-loop topology gives L = ½ℏ (Eq. 6):

    L = r × p = (λ/4π)(hν/c) = ℏ/2

This depends only on the path length being λ and the double-loop
structure. It does NOT depend on the field distribution, the cavity
shape, or any geometric approximation. It is the model's strongest
and cleanest prediction.

### g-factor: near-exact (depends on topology + energy partition)

g = 2(1 + α'/2π) where α' = (q/e)²α (Eq. 12–13). This matches
first-order QED. It comes from the fraction of energy in the
non-rotating external field, not from the internal geometry. For
q ≈ e, g ≈ 2.0023 regardless of how q is calculated.

### Charge: approximate (depends entirely on geometry)

q = (1/2π)√(3ε₀ℏc) ≈ 0.91e (Eq. 5). This is the ONLY prediction
that depends on the choice of confinement volume V and comparison
radius r_c. WvM acknowledge this explicitly (§3): "It depends on
the detailed distribution of the internal fields and also on the
precise value we choose for the effective charge radius."

**The model's structure is therefore: topology → spin (exact) and
g-factor (near-exact); geometry → charge (approximate).**

### Why the sphere might be physically correct

WvM's "rotation horizon" at r = λ/2 is not arbitrary — it is the
maximum distance at which paths of length λ can contribute to the
circulation. Any path beyond this radius cannot close in one
wavelength and therefore cannot participate in the energy flow.

The photon orbits at R = λ/(4π), which is small compared to λ/2
(R/r_horizon ≈ 0.16). At distances ≫ R from the torus center, the
time-averaged field of a charge circulating at speed c is nearly
spherically symmetric — the toroidal structure is "smeared out" by
the ultra-relativistic orbit. This is the same physics that makes
the time-averaged field of a classical circulating charge approach
a monopole at distances larger than the orbit radius.

So WvM's sphere of diameter λ may be the right choice: it is the
**rotation horizon** (the physically motivated outer boundary), and
the field inside it is approximately uniform because the photon
moves at c and averages over the toroidal structure.

### Degenerate torus: the bridge between torus and sphere

A torus with tube radius a much larger than major radius R degenerates
toward a sphere-like shape. Using the torus volume formula V = 2π²Ra²
and q ∝ 1/√V (with uniform field at r_c = R):

| a/R | Outer edge | V/V_sphere | q/e |
|-----|-----------|------------|-----|
| 1.0 (horn) | 0.159 λ | 0.019 | 6.60 |
| 5.28 | 0.500 λ (= horizon) | 0.530 | 1.25 |
| 6.60 | 0.605 λ | 0.828 | 1.00 ← |
| 7.26 | 0.657 λ | 1.000 | 0.91 (= WvM) |

At a/R ≈ 5.28, the tube's outer edge exactly reaches the rotation
horizon. The charge at this geometry is q ≈ 1.25e — 25% too high,
but within a factor of 2 and converging toward e.

At a/R ≈ 6.60, q = e exactly, with the outer edge at 0.605λ — about
21% beyond the rotation horizon. At a/R ≈ 7.26, we recover WvM's
0.91e (sphere volume).

This smooth continuum from torus (q ≫ e) to sphere (q ≈ 0.91e)
shows that the charge prediction interpolates between two limits.
The "right" answer depends on how much of the volume within (and
slightly beyond) the rotation horizon is actually filled by the
field. WvM's sphere corresponds to the field filling the entire
horizon volume — which is physically plausible for a photon
circulating at c.

### Reframing the 9% deficit

If WvM's sphere is justified by the rotation horizon argument, then
the 9% deficit (q = 0.91e, not e) may reflect the fact that the
field distribution is not perfectly uniform within the horizon sphere.
The inner region (near the toroidal orbit) has higher field density
than the outer region. This non-uniformity could plausibly account
for a 9% correction — which is, intriguingly, back in the range
where the series hypothesis operates.

However, this interpretation differs from the original series
hypothesis: instead of "nested sub-tori add charge," the correction
would come from "non-uniform field distribution within the rotation
horizon modifies the effective average." These might be equivalent
descriptions of the same physics.

---

## F9. The Degenerate Torus and Why the Sphere May Be Physical

**Visualization**: `torus_viz.html` (interactive 3D, slider for a/R)

The "tube radius" a in the WvM model is not a hard wall — it
describes how far the photon's E-field extends from the geodesic
orbit. The photon orbits at R = λ/(4π); the field radiates outward
and decays with distance. Three geometric regimes:

- **Ring** (a < R): Field concentrated near the orbit. Region of
  significant field strength is toroidal with a visible hole.
- **Horn** (a = R): Field reaches the symmetry axis. Hole closes.
- **Spindle** (a > R): Field extends past the axis. As a geometric
  surface, the torus self-intersects (not embeddable in 3D). But
  as a field distribution, this is perfectly physical — the field
  just fills a blob that encompasses the center and looks
  increasingly spherical.

There is no blowup at a = R. The parametric equations remain valid;
the surface simply folds through itself. The geodesic orbit also
continues — it passes through the center axis when a > R.

### Key a/R values

| a/R  | Geometry           | Outer edge    | q/e   |
|------|--------------------|---------------|-------|
| 0.50 | Thin ring          | 0.119 λ       | 13.2  |
| 1.00 | Horn (hole closes) | 0.159 λ       |  6.6  |
| 5.28 | Outer = horizon    | 0.500 λ       |  1.25 |
| 6.60 | q = e (exact)      | 0.605 λ       |  1.00 |
| 7.26 | V = V_sphere (WvM) | 0.657 λ       |  0.91 |

### Physical picture

The photon orbits at R ≈ 0.08λ — tiny compared to the rotation
horizon at λ/2. At distances ≫ R, the time-averaged field of a
charge circulating at c is nearly spherically symmetric. The
toroidal structure is "smeared out" by ultra-relativistic
circulation, just as a classical orbiting charge produces a
monopole-like time-averaged field at large distances.

WvM's sphere of diameter λ corresponds to the rotation horizon —
the maximum distance at which paths of length λ can close. This is
a physically motivated boundary, not an arbitrary choice. The field
fills this sphere because the photon moves at c and averages over
the toroidal orbit.

The "degenerate torus" picture makes this concrete: a torus with
a/R ≈ 7.26 has the same volume as WvM's sphere. The shape is no
longer a donut — it's an oblate blob that approximates a sphere.
The charge at this volume is 0.91e. At a/R ≈ 6.60, q = e exactly.

---

## Open Questions After F1–F9

1. **Can we model the field falloff from the orbit?** Rather than
   hard walls at arbitrary a, compute the field of a guided wave
   on the toroidal geodesic and see how it decays with distance
   from the orbit. Does it fill the rotation horizon sphere
   approximately uniformly?

2. **Is the non-uniform distribution quantifiable?** If the field
   is denser near the orbit and sparser near the horizon, does
   this non-uniformity produce a correction factor close to 1/0.91
   ≈ 1.099? If so, the series hypothesis might describe this
   correction rather than literal sub-tori.

3. **What fixes the effective volume?** The value a/R ≈ 6.60 gives
   q = e exactly. Is there a self-consistency condition (e.g., the
   field at the horizon matches the external Coulomb field, or the
   energy density at the boundary equals zero) that selects this
   value?

4. **Does the geodesic orbit change with a/R?** In the spindle
   regime, the orbit passes through the center. Does this alter the
   photon dynamics, or is the orbit purely determined by the major
   radius R regardless of the field extent?
