# Findings: Toroid Geometry Study

Running log of experiments, results, and their implications.
Entries are chronological. Each entry references the script that
produced it and the propositions from `theory.md` that it bears on.

This study was spawned from `../toroid-series/`, which blocked when
the geometric analysis below revealed that the 9% charge deficit
was not a robust physical number.

---

## F1. WvM Sensitivity to Geometric Assumptions

**Script:** `scripts/01_wvm_sensitivity.py`
**Bears on:** P1 (rotation horizon), P4 (self-consistency)

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
q = 2–47× e (far too large). The spherical approximation is actually
*generous*.

**B. Charge radius:**
With the spherical cavity, only a 4.8% increase in r_c (from r̄ to
1.048 r̄) closes the deficit entirely. The charge is very sensitive
to this parameter — q ∝ r_c².

**C. E-B energy partition (corrected):**
WvM explicitly set U_E = U_B = U/2 (§3 of the paper). The derivation
is correct: the factor of ½ from U_E = U/2 cancels with the ½ in
W_E = ε₀E²/2, giving E² = u_total/ε₀. There is no free parameter
here.

### Key numbers

| Route to q = e | Required change |
|----------------|-----------------|
| Shrink V only | V → 0.83 × V_sphere |
| Increase r_c only | r_c → 1.048 × r̄ (5% shift) |

### Implications

The 9% deficit is **within the geometric uncertainty** of WvM's
approximations. A ~5% shift in the charge radius eliminates it. The
target S ≈ 1.0985 from the series study carries ~5–10% systematic
uncertainty. This is what blocked the predecessor study.

---

## F2. Toroidal Cavity EM Modes (Maxwell's Equations)

**Script:** `scripts/02_toroidal_modes.py`
**Bears on:** P1 (is the sphere justified?), P2 (field profile)

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
mode peaks at the tube center about 3.8× the volume average — the
expected J₀ profile of a circular cavity's fundamental mode.

### Why this happens

The toroidal volume is 15–200× smaller than WvM's sphere (diameter λ):

    V_sphere = πλ³/6 ≈ 7.5 × 10⁻³⁶ m³
    V_torus(a/R=0.5) ≈ 3.6 × 10⁻³⁸ m³   (ratio: ~200×)

Same photon energy in a much smaller volume → much higher energy
density → much stronger E-field → much larger apparent charge.

### What script 02 does and does not compute

Script 02 solves for the lowest **standing-wave eigenmode of a
hard-walled toroidal cavity**. This is NOT the same as WvM's model,
which describes a photon **propagating** as a traveling wave along
a double-loop geodesic. The differences:

| | WvM photon | Script 02 cavity mode |
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

### Key finding

**WvM's choice of a sphere of diameter λ is what makes q ≈ e.**
It's not a minor approximation — it's the central reason the charge
comes out close to the elementary charge.

---

## F3. What WvM Gets Right vs. What Depends on Geometry

**No script** — analytical review of the WvM paper (ref/WvM.pdf §2–5)
**Bears on:** P1 (rotation horizon justification)

WvM derive three electron properties. Their robustness differs
fundamentally:

### Spin: exact (topological, no geometric assumptions)

The double-loop topology gives L = ½ℏ (Eq. 6):

    L = r × p = (λ/4π)(hν/c) = ℏ/2

This depends only on the path length being λ and the double-loop
structure. It is the model's strongest and cleanest prediction.

### g-factor: near-exact (depends on topology + energy partition)

g = 2(1 + α'/2π) where α' = (q/e)²α (Eq. 12–13). This comes from
the fraction of energy in the non-rotating external field, not from
the internal geometry.

### Charge: approximate (depends entirely on geometry)

q = (1/2π)√(3ε₀ℏc) ≈ 0.91e (Eq. 5). This is the ONLY prediction
that depends on the choice of confinement volume V and comparison
radius r_c. WvM acknowledge this explicitly (§3).

**The model's structure: topology → spin (exact), g-factor
(near-exact); geometry → charge (approximate).**

### Why the sphere might be physically correct

WvM's "rotation horizon" at r = λ/2 is not arbitrary — it is the
maximum distance at which paths of length λ can contribute to the
circulation. The photon orbits at R = λ/(4π), which is small compared
to λ/2 (R/r_horizon ≈ 0.16). At distances ≫ R, the time-averaged
field of a charge circulating at c is nearly spherically symmetric.

So WvM's sphere of diameter λ may be the right choice: it is the
**rotation horizon** (the physically motivated outer boundary), and
the field inside it is approximately uniform because the photon moves
at c and averages over the toroidal structure.

---

## F4. The Degenerate Torus: Bridging Torus and Sphere

**Visualization:** `torus_viz.html` (interactive 3D, slider for a/R)
**Bears on:** P2 (field falloff), P4 (self-consistency)

The "tube radius" a is not a hard wall — it describes how far the
photon's E-field extends from the geodesic orbit. Three regimes:

- **Ring** (a < R): Toroidal field region with a hole. q ≫ e.
- **Horn** (a = R): Hole closes. Still q ≫ e.
- **Spindle** (a > R): Field extends past the axis. The geometric
  surface self-intersects, but as a field distribution this is
  perfectly physical — the field fills a blob that looks increasingly
  spherical.

There is no blowup at a = R. The parametric equations remain valid;
the geodesic orbit continues unchanged (it depends on R, not a).
The E-field direction (radially from the orbit) is a topological
property of the photon's polarization and is preserved in all regimes.

### Key a/R values

| a/R  | Geometry           | Outer edge | q/e  |
|------|--------------------|------------|------|
| 0.50 | Thin ring          | 0.12 λ     | 13.2 |
| 1.00 | Horn (hole closes) | 0.16 λ     |  6.6 |
| 5.28 | Outer = horizon    | 0.50 λ     |  1.25|
| 6.60 | q = e exactly      | 0.61 λ     |  1.00|
| 7.26 | V = V_sphere (WvM) | 0.66 λ     |  0.91|

### Physical picture

The photon orbits at R ≈ 0.08λ, tiny compared to the rotation
horizon at λ/2. At distances ≫ R, the time-averaged field is nearly
spherically symmetric. WvM's sphere corresponds to the field filling
the entire rotation horizon — physically plausible for a photon
circulating at c.

A degenerate torus with a/R ≈ 7.26 has the same volume as WvM's
sphere. The shape is no longer a donut — it's an oblate blob
approximating a sphere. At a/R ≈ 6.60, q = e exactly.

### Reframing the 9% deficit

If WvM's sphere is justified, the 9% deficit (q = 0.91e) may reflect
non-uniform field distribution within the horizon sphere: denser near
the orbit, sparser near the edge. This non-uniformity could plausibly
account for a ~10% correction.

This is a different interpretation than the series study's "nested
sub-tori add charge." Instead: "non-uniform field distribution within
the rotation horizon modifies the effective average." The two
descriptions might be mathematically equivalent.

---

## Open Questions After F1–F4

1. **Can we model the field falloff from the orbit?** Rather than
   hard walls at arbitrary a, compute the field of a guided wave
   on the toroidal geodesic and see how it decays with distance
   from the orbit. Does it fill the rotation horizon sphere
   approximately uniformly?

2. **Is the non-uniform distribution quantifiable?** If the field
   is denser near the orbit and sparser near the horizon, does
   this non-uniformity produce a correction factor close to 1/0.91
   ≈ 1.099? If so, the correction has a clean geometric origin.

3. **What fixes the effective volume?** The value a/R ≈ 6.60 gives
   q = e exactly. Is there a self-consistency condition (e.g., the
   field at the horizon matches the external Coulomb field, or the
   energy density at the boundary equals zero) that selects this
   value?

4. **Does the geodesic orbit change with a/R?** In the spindle
   regime, the orbit passes through the center. Does this alter the
   photon dynamics, or is the orbit purely determined by the major
   radius R regardless of the field extent?
