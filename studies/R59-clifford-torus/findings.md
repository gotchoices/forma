# R59 Findings

R59 tests whether adding a time dimension to the Ma metric produces
the Coulomb coupling α = 1/137 through off-diagonal entries.  The
study ran seven tracks (1, 1b, 1c, 1d, 1e, 3, 3b).  **Net result:
negative** — direct Ma-t coupling and ℵ-mediated Ma-ℵ-t both fail
to produce α at the spatial level on model-E's geometry.  However,
Track 3b Part 7 found a positive signal from tube-based ℵ mediation
on a shearless metric, which is the motivation for a possible follow-on
(R60 / model-F).

Track index:

| Track | Scope | F-range | Status |
|-------|-------|---------|--------|
| 1 | Direct Ma-t on model-E | F1–F8 | complete |
| 1b | ℵ-mediated Ma-ℵ-t (11D) | F9–F14 | complete |
| 1c | Minimal single electron sheet | F15–F18 | complete |
| 1d | Two sheets (e + p) | F19–F21 | complete |
| 1e | Root-selection diagnostics (F4 resolved) | F22–F27 | complete |
| 3 | Shear architecture test bed (9 architectures) | F28–F33 | complete |
| 3b | Spatial field solve (Coulomb test) | F34–F42 | complete |

---

## Track 1: Direct Ma-t coupling on model-E

**Scope:** Extend model-E's 6D Ma metric to 10D (6 Ma + 3 S + 1 t),
add Ma-t off-diagonal entries, tune σ so that a mass-shell-derived
"α_eff" matches observed α.  Script:
[track1_metric_with_time.py](scripts/track1_metric_with_time.py).

### F1. Sanity check: bare 10D metric reproduces model-E

The 10D metric (6 Ma + 3 S + 1 t, g_tt = -1) with no off-diagonal
coupling gives identical particle masses to model-E.  Three
independent methods agree: model-E library, Schur complement on
time, and full mass-shell condition.

This confirms the foundation is sound.  The non-trivial part: when
coupling is turned on (F3), the Schur and mass-shell methods diverge
— so their agreement here establishes the baseline.

### F2. Tube coupling is catastrophic; ring coupling works

Ma-t coupling on TUBE dimensions produces wild mass shifts even at
σ = 0.001 (−40% electron, +28% proton).  This is the same tube
saturation from R55 (e-tube at PD boundary).  Tube coupling is
ruled out at the direct Ma-t level.

Ring coupling is well-behaved: smooth, controllable shifts
proportional to σ².

**Open question:** the charge formula Q = −n₁ + n₅ uses TUBE winding
numbers, but the coupling goes through RING dimensions.  By what
mechanism does a tube-winding mode feel the ring-mediated field?

### F3. Schur complement and mass-shell disagree — different questions

At σ = 0.1 (ring), the Schur complement gives ~0.35% mass shift
while the mass-shell condition gives ~7%.  A factor of 20× difference.

**The disagreement is NOT because one is wrong.**  They answer
different questions:

- Schur on time imposes k_t = 0 (effective metric on the massless slice).
  For a massive mode, k_t = E ≠ 0, so this is the wrong constraint.
- Mass-shell solves g^{μν} k_μ k_ν = 0 with k_t = ω ≠ 0 — the full
  Lorentzian dispersion relation.

R55 used Schur on ℵ (Euclidean, no conjugate energy), which was
appropriate for that context.  **R55's numbers were not wrong** —
R55 answered a different question.  The mass-shell condition is the
right tool for Lorentzian t-coupling.

### F4. Mass DECREASES — a threat to the hypothesis (later resolved, F22)

The Ma-t coupling DECREASES mode masses: for the electron at
σ = 0.00863, E_bare = 0.511 MeV → E_coupled = 0.507 MeV (−0.73%).

**This is the wrong direction.**  The observed Coulomb self-energy
of the electron INCREASES its mass by ~α × mc².

This was flagged as a serious concern.  Track 1e (F22) resolved it
as a root-selection error.  See below.

### F5. Mass-shell quadratic gives TWO roots (particle/antiparticle)

The dispersion relation is quadratic in ω.  Both roots are physical:

| Mode | E_low (MeV) | E_high (MeV) | Splitting (MeV) |
|------|------------|-------------|----------------|
| electron | 0.5073 | 0.5148 | 0.0076 |
| proton | 931.56 | 945.18 | 13.63 |
| deuteron | 1863.10 | 1890.37 | 27.25 |

The splitting represents a charge-dependent mass offset (later F22
shows the high root is the particle).

### F6. Near-universal α_eff with 1.83% gap — one-parameter fit

At σ = 0.00860 (ring coupling, no ν-ring entry):

| Mode | α_eff | α_eff/α |
|------|-------|---------|
| electron | 7.30×10⁻³ | 1.000 (tuned) |
| proton | 7.16×10⁻³ | 0.982 |
| deuteron | 7.16×10⁻³ | 0.982 |
| ν₁ | 9.3×10⁻⁴ | 0.127 (indirect, not coupled) |

**Universality gap: 1.83%** between electron and proton.

**Important caveats:**

1. **One-parameter fit.**  σ is tuned to match α_eff(e) = α.  Every
   other species' α_eff is then determined by the fixed geometry.
2. **α_eff ≡ |ΔE/E| is an operational proxy, not α itself.**  To
   establish that this IS α, Track 3 must show the Ma-t coupling
   produces a Coulomb field in S of the standard strength.  (Later
   done by Track 3b, with negative result — F35.)
3. **Charge signs are hand-coded.**

### F7. R55 vs R59 — not apples-to-apples

| Property | R55 (ℵ, spatial) | R59 (time, Lorentzian) |
|----------|-----------------|----------------------|
| Method | Schur on Euclidean ℵ | Mass-shell on Lorentzian t |
| σ parameter | 0.290 | 0.00860 |
| α_eff(e) | 1.000α | 1.000α |
| α_eff(p) | 0.964α | 0.982α |
| Gap | 3.6% | 1.83% |
| Mass direction | Increases | Decreases (F4, later F22) |

The gap improvement (3.6% → 1.83%) may reflect the change in
computation method rather than geometry.  Not yet disentangled.

### F8. Neutrino coupling is NOT emergent — it's hand-coded or indirect

With ν-ring coupled by hand at +σ: α_eff(ν) = 1.035α (INPUT, not
prediction).  Without: α_eff(ν) = 0.127α via cross-sheet leakage
(indirect, ~8× weaker).  Cannot cite F8 as evidence for or against
L05 without a physical argument for the ν-ring entry.

**Track 1 status:** Complete.  Achieves 1.83% universality gap at
the mass-shell level.  Caveats: mass decrease (F4), α_eff proxy (F6),
R55 comparison not controlled (F7), neutrino hand-coded (F8).

---

## Track 1b: ℵ-mediated time coupling (11D)

**Scope:** Route the Ma-t coupling through ℵ: Ma ↔ ℵ ↔ t chain on
the 11D metric.  Script:
[track1b_aleph_time.py](scripts/track1b_aleph_time.py).

### F9. Masses INCREASE — correct direction

The ℵ link is Euclidean (+1 diagonal); only the final ℵ-t leg is
Lorentzian.  The double indirection flips the sign relative to
Track 1.  Result: all masses INCREASE by ~0.7% — the correct
direction for Coulomb self-energy.  **Track 1b resolves the F4
sign problem** (mass-shell reading).

### F10. Universality gap is 5.24% — worse than Track 1

| Mode | α_eff/α |
|------|---------|
| electron | 1.000 (tuned) |
| proton | 1.044 |
| deuteron | 1.044 |
| Σ⁻ | 1.055 |

The gap is wider because the coupling goes through two hops
(Ma-ℵ and ℵ-t), interacting non-trivially with internal shears.

### F11. Signs are inherited from R55 geometry

Effective Ma-t entries (from integrating out ℵ):
- e-ring → t: +0.041
- ν-ring → t: −0.041
- p-ring → t: −0.041

Signs emerge from R55's Ma-ℵ geometry × σ_{ℵt}.  However the sign
convention is reversed relative to charge convention.

### F12. Neutrino couples at 0.92α — inherited from R55

The ν-ring was coupled at +1/(2π) in R55's Ma-ℵ block.  Through the
ℵ-t chain, this produces α_eff(ν₁) = 0.92α.  Inherited, not emergent.

### F13. The bare 11D metric has a 1% baseline shift

Even at σ_{ℵt} = 0, the 11D metric produces masses ~1% higher than
model-E, because R55's Ma-ℵ entries (±1/(2π)) perturb the Ma metric.
σ_{ℵt} tuning acts ON TOP of this baseline shift.

### F14. Comparison: Track 1 vs Track 1b

| Property | Track 1 (direct Ma-t) | Track 1b (ℵ→t) |
|----------|----------------------|-----------------|
| Dimensions | 10D (no ℵ) | 11D (with ℵ) |
| Knobs | 1 σ + 6 hand-coded entries | 1 σ_{ℵt} + R55 entries |
| Signs | Hand-coded | Inherited from R55 |
| Mass direction | Decrease (wrong, pre-F22) | Increase (correct) |
| Universality gap | 1.83% | 5.24% |
| Baseline shift | None | 1% from R55 Ma-ℵ |
| ν coupling | 0.127α (indirect) | 0.92α (from R55) |

Track 1 wins on universality; Track 1b on mass direction (before F22).

**Track 1b status:** Complete.  ℵ mediation produces correct mass
direction but wider gap.

---

## Track 1c: Minimal electron sheet + ℵ + S + t

**Scope:** Strip the metric to a single electron sheet and test both
coupling approaches (D1 direct, D2 ℵ-mediated) on this minimal system.
Script: [track1c_minimal_electron.py](scripts/track1c_minimal_electron.py).

### F15. Neither coupling approach touches particle-spectrum entries

On the minimal system, both D1 and D2 achieve |Δm|/m = α without
modifying:
- The tube dimension (any entry in row/column 0)
- The internal shear (s_e = 2.004, the tube-ring off-diagonal)

Coupling lives entirely on ring-t (or ring-ℵ + ℵ-t) entries.  Tube
and shear entries remain free for particle spectrum tuning when
other sheets are added.

### F16. Two approaches, same α, opposite mass direction

| Approach | Parameter | Mass direction | Entry touched |
|----------|-----------|---------------|--------------|
| D1 (direct ring-t) | σ = 0.00855 | Down (pre-F22) | G̃[ring, t] |
| D2 (ℵ-mediated) | σ_{ℵt} = 0.258 | Up (correct) | G̃[ring, ℵ] + G̃[ℵ, t] |

D2 gets the sign right because the coupling goes through ℵ
(Euclidean) before reaching t (Lorentzian).  The double hop flips
the sign relative to D1.

### F17. Generation structure is preserved

All modes on the electron sheet shift by the same fractional amount
(~0.5–0.9%), so mass RATIOS are preserved.  Generation mechanism
(shear resonance) is unaffected because coupling is on the ring,
not the shear.

| Mode | Bare ratio to (1,2) | D2 coupled ratio |
|------|-------------------|-----------------|
| (1,1) | 205.0 | 206.0 |
| (1,3) | 203.3 | 204.3 |
| (3,5) | 206.8 | 207.8 |

### F18. The ℵ-mediated approach has structural advantages

D2 (ℵ-mediated) is cleaner than D1 because:
1. Mass goes up (pre-F22).
2. The ℵ-t entry is SHARED across all sheets (one parameter for
   universality, not one per sheet).
3. Each sheet adds only its own ring-ℵ entry.
4. ℵ can be "switched off" by setting all Ma-ℵ entries to zero.

**Track 1c status:** Complete.  Coupling entries do not conflict
with particle spectrum entries.  Generation structure is preserved.

---

## Track 1d: Two sheets (electron + proton) — universality

**Scope:** Add the proton sheet to the minimal system.  Test whether
cross-sheet coupling interferes.  Script:
[track1d_two_sheets.py](scripts/track1d_two_sheets.py).

### F19. Two-sheet results match single-sheet — no cross-sheet interference

Adding the proton sheet does not change the electron's coupling or
vice versa.  Gaps essentially identical to single-sheet and full
model-E results:

| Approach | 1-sheet gap | 2-sheet gap | Full model-E gap |
|----------|-----------|-----------|-----------------|
| D1 (direct) | N/A | 1.84% | 1.83% |
| D2 (ℵ-med) | N/A | 4.23% | 5.24% |

Confirms F15: coupling entries don't conflict with particle spectrum.

### F20. The tradeoff is structural (pre-F22)

Neither approach alone gave both tight universality AND correct
mass direction — at the time.  Universality gap is a geometric
property of sheet aspect ratios, not coupling architecture.  (F22
later resolved the mass-direction side of this tradeoff.)

### F21. The D2 coupling is non-monotonic

ℵ-mediated α_eff passes through a minimum near σ_{ℵt} ≈ 0.10
(where α_eff ≈ 0.09α).  Schur complement through ℵ (Euclidean)
and through t (Lorentzian) partially cancel at intermediate values,
producing a near-zero coupling.  Electron and proton pass through
zero at slightly different σ_{ℵt}, creating the universality gap.

**Track 1d status:** Complete.  Multi-sheet coupling is
non-interfering; gap is structural.

---

## Track 1e: Root-selection diagnostics — F4 resolved

**Scope:** Investigate the F4 mass-direction puzzle.  Script:
[track1e_f4_diagnostics.py](scripts/track1e_f4_diagnostics.py).

### F22. The F4 sign problem was a ROOT SELECTION ERROR

Tracks 1–1d took min(|E₁|, |E₂|) — the smaller-magnitude root.
This is the antiparticle root (ω < 0).  The particle root (ω > 0)
has LARGER energy.

For D1 at σ = 0.00855:
- Antiparticle root (ω < 0): E = 0.5073 MeV (mass DOWN) ← was reported
- Particle root (ω > 0): E = 0.5148 MeV (mass UP) ← correct

The Coulomb self-energy ADDS to the particle mass.  **F4 is
resolved: the mass direction was wrong because we were reading the
antiparticle root.**

### F23. BOTH D1 and D2 give correct mass direction

When the positive-ω root is used:
- D1 (direct): ΔE/E = +0.74% = 1.01α (UP)
- D2 (ℵ-mediated): ΔE/E = +0.73% = 1.00α (UP)

Both increase the mass.  The D1/D2 sign dichotomy (F14/F16) was
entirely due to wrong root selection.

### F24. The splitting IS the coupling (with caveats later from F35)

The two roots are E_particle = E_bare + δE and E_antiparticle =
E_bare − δE.  The splitting 2δE is proportional to the Ma-t coupling
strength.

For the electron at σ = 0.00855: splitting = 0.0075 MeV, δE/E_bare
= 0.74% ≈ α.

At this point the splitting was claimed to be α itself.  **Later
F35 and F38 showed this claim was wrong** — the splitting is a
mass-shell quantity, not the spatial Coulomb coupling.  But F24
correctly identifies that the splitting ≈ α × mc² numerically.

### F25. Signature convention doesn't matter

Flipping from mostly-plus to mostly-minus gives identical |E₁| and
|E₂|.  The sign of the mass shift depends on which root is the
particle, not on metric signature.  F4 was not a signature artifact.

### F26. Recomputed universality on the particle root

For D1 (direct ring-t), σ = 0.00843:

| Mode | E_bare | E_particle | ΔE/E | α_eff/α |
|------|--------|-----------|------|---------|
| electron | 0.5110 | 0.5147 | +α | 1.000 (tuned) |
| proton | 938.27 | 945.00 | +0.982α | 0.982 |

**Gap: 1.81%** (vs 1.84% on antiparticle root — essentially
unchanged).  Gap is structural and independent of root selection.

### F27. The gap is symmetric across roots

The ~1.8% gap appears on both roots because the splitting is nearly
symmetric around the bare mass.  Gap comes from sheet geometry
(ε_e = 397 vs ε_p = 0.55), not root selection or coupling architecture.

**Track 1e status:** Complete.  F4 resolved as root-selection error.
Both direct and ℵ-mediated architectures give correct mass direction.
Universality gap of ~1.8% is structural.

---

## Track 3: Shear architecture test bed

**Scope:** Systematic test bed over nine shear architectures.  For
each, compute three α_eff measures and check signature + spectrum
preservation.  Script: [track3_testbed.py](scripts/track3_testbed.py).

Note: the earlier Track 3 narrative attempts were replaced by this
test bed (old scripts deleted).

### F28. Four of nine architectures break the Lorentzian signature

Setting a shear of magnitude α at the following locations produces
a metric with two negative eigenvalues instead of one:

| Arch | Where | Result |
|------|-------|--------|
| 1 | Ma_e-tube ↔ Ma_p-tube (internal cross) | 2 neg eigs |
| 2 | Ma_tube ↔ S (direct spatial) | 2 neg eigs |
| 3 | Ma↔ℵ=1, ℵ↔S=α (ℵ-mediated to S) | 2 neg eigs |
| 4 | Ma↔ℵ=1, ℵ↔t=α (strong Ma-ℵ) | 2 neg eigs |

Model-E's Ma metric sits close to the PD boundary (smallest
eigenvalue ~10⁻³, driven by s_e = 2.004).  Adding cross-couplings
at tube entries, Ma-S entries, or large Ma-ℵ entries pushes it over.

**This is a real geometric obstruction.**  Architectures that look
simple on paper are unphysical on model-E's geometry.

### F29. Only Ma–t (ring) architectures survive signature AND spectrum

| Arch | Where | Spectrum dev | Notes |
|------|-------|--------------|-------|
| 0 | Baseline (model-E only) | 0% | No α coupling (sanity) |
| 5 | Ma_tube ↔ t = α | 988% / 490% | Catastrophic — F2 |
| 6 | Ma_tube ↔ t = √α | 12,500% / 6,700% | Worse |
| 7 | Ma_ring ↔ t = α | 0.63% / 0.62% | **Passes** |
| 8 | Ma_ring ↔ t = √α | 8.1% / 7.9% | Spectrum broken |

**Only Arch 7 passes both tests.**  This is essentially Track 1's
architecture.

### F30. α_eff measures disagree — none is unambiguously "the Coulomb α"

For the surviving architectures, the three α_eff measures give
different numbers for the same metric:

| Arch | α_eff (a) mass-shell | α_eff (b) inverse-metric |
|------|---------------------|--------------------------|
| 7 (σ=α) | 6.3×10⁻³ (0.87α) | 3.9×10⁻⁵ (0.0054α) |
| 8 (σ=√α) | 8.1×10⁻² (11α) | 5.3×10⁻³ (0.73α) |

Measure (a) scales as σ; measure (b) scales as σ².  Cannot both be
the Coulomb α.  Distinguishing them requires a spatial-field solve
(Track 3b).

### F31. Arch 7 reproduces Track 1 without tuning

With σ = α (plugged in, not tuned):

| Mode | E_bare (MeV) | E_particle (MeV) | Δ/E | Ratio to α |
|------|--------------|------------------|------|-----------|
| electron | 0.5110 | 0.5142 | 0.63% | 0.865 |
| proton | 938.27 | 944.09 | 0.62% | 0.849 |

Universality: |α_e − α_p|/α ≈ 1.8%, matching Track 1's 1.83%.
The ~13% deficit (0.87α instead of α) is a geometric factor from
model-E's aspect ratios.

### F32. Signature-breakage rules out shear-only α via Ma-S or internal

The first three test configurations (internal cross, Ma-S,
ℵ-mediated to S) all fail signature.  The only working block is
Ma-t (rings only, not tubes).

### F33. What the test bed did NOT test

The test bed measures α_eff at a single spatial point.  It does
not solve the 10D linearized Einstein equations for δg(r) in S,
compute the force between two charges, or integrate field energy.
These are the pieces needed to identify α_eff as the Coulomb
coupling.  Track 3b addresses them directly.

**Track 3 status:** Complete.  Surviving architecture narrowed to
Arch 7.  Three α_eff measures disagree; spatial-field solve required
to resolve.

---

## Track 3b: Spatial field solve — the Coulomb test

**Scope:** Compute the spatial Coulomb-like field δg_{Ma,t}(r)
directly, extract the 1/r coefficient, compare to α.  Script:
[track3b_spatial_solve.py](scripts/track3b_spatial_solve.py).  Parts
1–5 cover direct Ma-t and ring-based ℵ mediation.  Parts 6–7 cover
tube-based ℵ mediation on model-E and on a clean (shearless) metric.

### F34. The 1/r spatial profile is confirmed

At r > 10 × w_src, the field matches C/(4πr) to 10⁻¹⁶ residual
(floating-point precision).  The 3D Laplacian Green's function
works as expected — whatever source strength the metric gives, it
falls off as 1/r at large r.

**The qualitative Coulomb profile is confirmed.**  What remains is
the coefficient.

### F35. Direct Ma-t: coefficient wrong by ~5 orders of magnitude

Arch 7 with σ = α at ring entries:

| Source | C (direct) | α_Coulomb = C²/(4π) | Ratio to α |
|--------|-----------|---------------------|-----------|
| electron | +1.23 × 10⁻³ | 1.20 × 10⁻⁷ | 1.6 × 10⁻⁵ |
| proton | −4.92 × 10⁻³ | 1.92 × 10⁻⁶ | 2.6 × 10⁻⁴ |

Force between electron source and proton test charge:
F_computed / F_Coulomb = ~10⁻⁴, constant across r from 19 fm to
19,000 fm.  **1/r² shape correct, magnitude wrong by 4–5 orders of
magnitude.**

### F36. Universality fails at the spatial level

Mass-shell universality (Track 3 measure a) was 1.8%.  Spatial
universality is a factor of 16 (α_e/α_p = 0.06).

Reason: the direct source strength depends on n_ring/L_ring, which
differs between modes (electron 2/11.88 = 0.168; proton 3/4.45 =
0.674).  At the mass-shell level these contributions partially
cancel; at the spatial level the n/L factor survives unmitigated.

**The mass-shell and spatial universalities measure different
things.**  Only the spatial universality corresponds to observed
Coulomb interactions.

### F37. Matching α would require σ ≈ 1.8 — metric-breaking

To match α at the spatial level:
σ² × (n_e n_p)/(L_e L_p) = α  →  σ ≈ 1.8.

At that magnitude the metric catastrophically breaks signature
(Arch 6 at σ = √α ≈ 0.085 already broke spectrum at 8%; σ = 1.8
is 20× larger).  **This is the classical KK hierarchy problem at
Compton-scale compact dimensions.**

### F38. Track 1's α identification was operational, not physical

The chain: Track 1 tuned σ so ΔE/E = α → Track 3 confirmed this
without tuning at σ = α → Track 3b shows the resulting spatial
field is 10⁻⁵ × α, not α.

**The mass-shell quantity ΔE/E is not the Coulomb coupling.**
It is a self-energy-like shift that happens to equal α numerically
when σ = α is plugged in.  Track 1's 1.8% universality at the
mass-shell level does not carry over to the spatial level.

### F39. Ring-based ℵ mediation (Ma-ring → ℵ → t) does not rescue the scaling

Scan of (Ma↔ℵ = 1/(2π), ℵ↔t, g(ℵ,ℵ)) configurations:

- At R55's values (ℵ↔t = α, g(ℵ,ℵ) = 1): α_Coulomb = 2.0 × 10⁻¹² α
  (worse than direct Ma-t).
- Required ℵ↔t for σ_eff ≈ 1.8 at g(ℵ,ℵ) = 1: ℵ↔t ≈ 11.3, signature
  OK, but spectrum broken at 1238%, and α_Coulomb = 1.4 × 10⁻¹⁴ α
  (even worse).
- Smaller g(ℵ,ℵ) breaks signature at ≤ 10⁻².

**Schur amplification fails:** the leading-order formula breaks
down at the large ℵ↔t values needed, and large entries destroy the
spectrum.  Ring-based ℵ mediation is strictly worse than direct
Ma-t at the spatial level.

### F40. S ↔ t coefficients — correctly zero

In flat Minkowski space g(S, t) = 0 by construction.  Nonzero g(S, t)
describes rotating frames / frame dragging, not Coulomb fields.  For
R59's static problem, zero is correct.  No test is missing here.

### F41. Tube-based ℵ mediation fails on model-E (all configs break signature)

Script Part 6: route the Ma↔ℵ shear on TUBE dimensions instead of
rings.  Motivated by MaSt's charge formula (charge = tube winding).

**Every tested configuration breaks signature**, even the smallest
(Ma↔ℵ = 0.01, ℵ↔t = 0.01, g(ℵ,ℵ) = 1).  Cause: model-E's s_e = 2.004
makes the e-tube near-singular via the internal shear (smallest
e-sheet eigenvalue ~10⁻³).  Any additional tube coupling pushes the
smallest eigenvalue past zero.

**Model-E's internal shears actively prevent tubes from carrying
additional couplings.**  This is a real geometric obstruction, not
a numerical artifact.

### F42. Clean (shearless) metric + tube→ℵ→t: structural universality, approaches α

Script Part 7: zero model-E's internal shears (s_e = s_ν = s_p = 0,
all cross-shears to zero) and test tube-based ℵ mediation on this
clean metric.

| (Ma↔ℵ, ℵ↔t, g(ℵ,ℵ)) | Sig | α_e / α | α_e / α_p |
|--------------------|-----|---------|-----------|
| (√α, √α, 1) | YES | 5.8×10⁻⁴ | **1.000** |
| (√α, 1.0, 1) | YES | **0.68** | **1.000** |
| (0.5, 0.5, 1) | YES | 54 | **1.000** |
| (0.1, 0.1, 1) | YES | 1.1×10⁻³ | **1.000** |
| (√α, √α, 0.1) | YES | 7.9 | **1.000** |
| (√α, √α, 0.01) | YES | 230 | **1.000** |

**Three findings worth emphasizing:**

1. **Universality is EXACT** (α_e / α_p = 1.000 to floating-point
   precision).  Both modes have |n_tube| = 1 by the charge
   quantization, so the tube-based mechanism treats them identically
   BY CONSTRUCTION.  Structural, not tuned.

2. **Signature preserved.**  The failure on model-E (F41) was
   specifically because of s_e; without the shear, tubes can carry
   couplings.

3. **α_Coulomb reaches 0.68α** at (σ_Ma-ℵ, σ_ℵ-t, g_ℵℵ) = (√α, 1, 1).
   Close to observed α, within factor of 1.5, no tuning beyond
   those natural values.

**This is the one positive signal in R59's otherwise negative
outcome.**  It suggests that:
- Abandoning model-E's specific shears opens a viable route to α
- Tube-based ℵ mediation is the physically motivated architecture
  (charge = tube winding)
- Clifford embedding of the torus in St may provide the geometric
  structure that fixes the remaining parameters

Significant caveats:
- Spectrum is gone — no generations, no specific masses
- (√α, 1, 1) is 0.68α not α; exact tuning not yet found
- "Unit L" simplification used; real dimensions must be reintroduced

**Track 3b status:** Complete.  Direct Ma-t and ring-based ℵ
mediation both fail at the spatial level (F35, F39).  Tube-based ℵ
mediation fails on model-E (F41) but shows promise on a clean metric
(F42).  Motivates a follow-on study (R60 / model-F).

---

## R59 overall status

**Complete.  Negative result on the original claim.  Positive signal
from F42 motivates a possible follow-on study.**

### What R59 established (negative)

1. Direct Ma-t coupling on model-E does not produce Coulomb α at the
   spatial level (F35).  Mass-shell α_eff was a proxy, not the
   Coulomb coupling (F38).
2. Ring-based ℵ mediation is strictly worse than direct Ma-t (F39).
   Schur amplification fails when the full matrix inversion is done.
3. Tube-based ℵ mediation on model-E breaks signature for every
   config (F41).  Model-E's s_e = 2.004 makes the e-tube near-singular
   and blocks any additional tube coupling.
4. Getting observed α from a single metric off-diagonal requires
   σ ≈ 1.8, which breaks the metric (F37).  This is the KK hierarchy
   problem at Compton-scale compact dimensions.

### What R59 established (positive)

5. F4 (mass-direction threat) was a root-selection error (F22).  Both
   architectures give the correct Coulomb self-energy sign on the
   particle root.
6. Coupling entries on the ring don't disturb particle-spectrum
   entries on the tube (F15); generation structure is preserved (F17).
7. On a shearless clean Ma metric, tube-based ℵ mediation gives
   EXACT universality (α_e/α_p = 1.000) and α_Coulomb reaching 0.68α
   (F42).

### The central falsification

**R59's original claim — that adding time to the metric on
model-E's geometry produces the Coulomb coupling at strength α —
is falsified.**  Both direct and ring-based ℵ architectures fail
at the spatial level.

### The positive signal

**F42 is a real but partial positive result.**  The clean-metric
tube-ℵ-t mechanism reaches within a factor of 1.5 of α without
tuning, and delivers structural universality from charge
quantization.  This is not R59's original claim (that would require
staying on model-E), but it is a legitimate mechanism for α that
deserves a follow-on study.

### Recommended next steps

The positive signal in F42 motivates spinning off a new study
(R60 or "model-F exploration").  Proposed scope:

1. Precise parameter tuning to find α_Coulomb = α exactly on the
   clean metric.
2. Develop the Clifford-torus embedding in St explicitly (tube and
   ring circles mapped to orthogonal planes in the ambient
   spacetime).
3. Reintroduce physical scales (ε ratios, L circumferences) and
   check whether the mechanism survives.
4. Rebuild the particle spectrum on the new metric — electron,
   proton, muon, tau, hadrons, nuclei.

Decision point after step 3: if the mechanism doesn't survive
physical scaling, the model-F direction dies.  If it does, step 4
is the real work of a new model.

R59 itself closes here.
