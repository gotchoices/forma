# R47: Proton filter — (1,3) mode hypothesis with 3-slot geometry

**Status:** Active (Track 0)
**Questions:** [Q90](../../qa/Q90-ephemeral-mode-decomposition.md) (quarks as sub-modes),
  [Q53](../../qa/Q53-anomalous-magnetic-moment.md) (g − 2)
**Type:** compute / interactive
**Depends on:** R46 (electron filter methodology — Tracks 3–4)

---

## Motivation

R46 established a successful framework for the electron: a scalar
eigensolver on the torus surface, phase-locked standing waves, and
elliptical slots that kill the ghost while preserving the desired
mode and producing the anomalous magnetic moment.

The proton is the next target.  Prior studies (R26, R27) assumed the
proton is a **(1,2) mode on Ma_p**, mirroring the electron on Ma_e.
This study tests a different hypothesis:

**The proton is a (1,3) mode.**

### Why (1,3)?

1. **Three-fold symmetry is natural.**  A (1,3) standing wave has
   3 antinodes around the ring — three energy concentrations at
   0°, 120°, 240°.  These form a scaffold more natural for quarks.  A (1,2) mode has 2-fold
   symmetry, which never naturally produces three domains.

2. **Three slots at 120° kill both ghosts.**  With q_eff ≈ 3 for
   the target mode:
   - (1,1): sin²(1 × 120°) = 0.75 → **killed**
   - (1,2): sin²(2 × 120°) = 0.75 → **killed**
   - (1,3): sin²(3 × 120°) = 0.00 → **survives**

   The electron needed 4 shear-corrected slots to kill one ghost.
   The proton's geometry kills two ghosts with only 3 slots at
   exact 120° spacing — simpler and more symmetric.

3. **Quark decomposition.**  Q90 proposed quarks as ephemeral
   sub-modes.  For (1,3), three (1,9) sub-modes tile the ring
   in thirds (3 × 3 = 9 ring windings each occupying 120°).
   The slots sit at the boundaries between quark domains.


## Ground rules

This study returns to fundamentals.  We do **not** assume:
- r_p = 8.906 (from R27 — derived under (1,2) assumption)
- Any prior proton geometry from R26/R27
- Any MaSt-derived values except the eigensolver framework (R46)

We **do** assume:
- The proton is a standing wave on a 2D periodic sheet (Ma_p)
- The scalar Sturm-Liouville eigensolver from R46 Track 3
- The phase-locked node constraint model from R46
- α = 1/137.036 determines shear given ε
- Compton wavelength = h/(m_p c) determines absolute scale
- the _real_ quark is a (1,3) excitation. This means the old "size" of the proton sheet was wrong.

## Deriving particle geometry from known inputs

Given a hypothesized mode (n₁, n₂) and a known particle mass m,
what can we determine — and what remains free?

**Known inputs:**
- Particle mass m → reduced Compton wavelength ƛ = ℏ/(mc)
- Fine structure constant α = 1/137.036
- Mode winding numbers (n₁, n₂) — for the proton hypothesis: (1, 3)

**Derivation chain:**

1. **α pins shear as a function of ε.**  The α formula α = f(ε, s)
   with q_eff = n₂ − s·n₁ has one equation and two unknowns (ε, s).
   For any chosen ε, there is a unique s that reproduces α = 1/137.
   So s = s(ε).

2. **Mass gives the eigenvalue.**  The dimensionless eigenvalue
   μ = √((n₁·ε)² + (n₂ − n₁·s)²) depends only on ε (since s is
   determined by step 1).

3. **Compton wavelength + eigenvalue → tube circumference.**
   L_θ = ƛ × μ(ε).  This is the tube circumference, determined
   once ε is chosen.

4. **ε → ring circumference.**  L_φ = L_θ / ε.

5. **Absolute dimensions.**  Tube radius a = L_θ/(2π),
   ring radius R = L_φ/(2π), sheet area = L_θ × L_φ.

**What is determined:**  Given ε, everything follows — shear,
circumferences, absolute radii, area.  All are computable
functions of the single free parameter ε.

**What is NOT determined:**  ε itself.  Mass alone does not
pin the aspect ratio.  The electron illustrates this: we know
m_e, we know (1,2), we know α, yet ε_e remains unconstrained.
Some additional physics must select ε — ghost-killing
constraints, charge overlap requirements, or a future
energy-minimization principle.

This is why Track 1 sweeps ε: we are searching for the
constraint that nature uses to pick the proton's aspect ratio.

---

## Tracks

### Track 0: Torus Lab support for proton mode

**Status:** Complete (verified interactively)

**Goal:** Extend Torus Lab so it can work with arbitrary target
modes, not just the hardcoded electron (1,2).

**Current limitations:**
- `alphaFormula` hardcodes q = 2 − s (electron's n₂ = 2)
- `electronIdx` / `ghostIdx` hardcode (1,2) and (1,1)
- Optimize button assumes electron mode
- Spectrum labels, metrics, derived panel all say "electron"

**Required changes:**
- When particle = "proton", use q = 3 − s in `alphaFormula`
  (the α formula relates to the *target mode's* n₂, since that
  mode's charge must equal e)
- Make `targetIdx` and `ghostIdx` (plural — there may be multiple
  ghosts) depend on the selected particle
- Optimize button: place nodes at target mode's standing-wave
  nodes (180°/q_eff_target spacing)
- Labels and metrics: show survival for the target and all ghosts

**Depends on:** Nothing.


### Track 1: Proton (1,3) mode analysis

**Status:** Complete

**Goal:** Characterize the (1,3) proton mode across a range of
aspect ratios ε.  Determine what ε values give viable physics.

**Method:**
1. Sweep ε from 0.1 to 10
2. At each ε, solve shear from α(ε, s) = 1/137.036 using
   q = 3 − s (proton's n₂ = 3)
3. Compute all resonant modes and their properties:
   - Mass spectrum (relative to the (1,3) fundamental)
   - Charge overlap C for each mode
   - Mode density f(θ₁) at inner equator
4. Place 3 nodes at 120° (shear-adjusted: 180°/q_eff)
5. Compute survival scores for all modes
6. Identify which ε values:
   - Kill both ghosts (1,1) and (1,2)
   - Preserve the (1,3) target
   - Have reasonable charge overlap values

**Outputs:**
- Survival of (1,3), (1,2), (1,1) vs ε (sweep plot)
- Shear vs ε curve
- Charge overlap vs ε
- Absolute dimensions vs ε: tube radius a, ring radius R, sheet area
- Recommended ε range for Torus Lab exploration

**Key questions:**
- Does the shear correction at 120° matter as much as it did
  for the electron?  (For q_eff ≈ 3, spacing = 60° per node,
  and 120° is exactly 2 nodes — should be exact at s = 0)
- At what ε does the (1,3) mode localize toward the outer
  equator?  Does this affect slot placement?
- Are there any ε values where additional charged modes
  (1,4), (1,5), etc. are also killed by the 3-slot geometry?

**Depends on:** Track 0 (Torus Lab proton support).

**Findings:** See [findings.md](findings.md), Track 1.


---

## Notes
