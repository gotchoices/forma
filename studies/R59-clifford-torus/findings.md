# R59 Findings

## Track 1: Build the metric with time

### F1. Sanity check: bare 10D metric reproduces model-E

The 10D metric (6 Ma + 3 S + 1 t, g_tt = -1) with no
off-diagonal coupling gives identical particle masses to
model-E.  Three independent methods agree: model-E library,
Schur complement on time, and full mass-shell condition.

This confirms the foundation is sound.  The non-trivial
part: when coupling is turned on (F3), the Schur and mass-shell
methods diverge — so their agreement here establishes the
baseline.


### F2. Tube coupling is catastrophic; ring coupling works

Ma-t coupling on TUBE dimensions produces wild mass shifts
even at σ = 0.001 (−40% electron, +28% proton).  This is
the same tube saturation from R55 (e-tube at PD boundary).
Tube coupling is ruled out.

Ring coupling is well-behaved: smooth, controllable shifts
proportional to σ².

**Open question for Track 3:** the charge formula Q = −n₁ + n₅
uses TUBE winding numbers, but the coupling goes through RING
dimensions.  By what mechanism does a tube-winding mode feel
the ring-mediated field?  The tube creates the topology
(charge); the ring mediates the energy transfer (coupling).
These are different entries in the metric — why would the
tube topology "see" the ring coupling?


### F3. Schur complement and mass-shell disagree — different questions

At σ = 0.1 (ring), the Schur complement gives ~0.35% mass
shift while the mass-shell condition gives ~7%.  A factor
of 20× difference.

**The disagreement is NOT because one is wrong.**  They answer
different questions:

- Schur on time imposes k_t = 0 (effective metric on the
  massless slice).  For a massive mode, k_t = E ≠ 0, so
  this is the wrong constraint.
- Mass-shell solves g^{μν} k_μ k_ν = 0 with k_t = ω ≠ 0 —
  the full Lorentzian dispersion relation.

R55 used Schur on ℵ (Euclidean, no conjugate energy), which
was appropriate for that context.  **R55's numbers were not
wrong** — R55 answered a different question (spatial coupling
through ℵ) using the right tool for that question.  The mass-
shell condition is the right tool for Lorentzian t-coupling.


### F4. Mass DECREASES — a threat to the hypothesis

The Ma-t coupling DECREASES mode masses.  For the electron at
σ = 0.00863: E_bare = 0.511 MeV → E_coupled = 0.507 MeV
(−0.73%).

**This is the wrong direction.**  The observed Coulomb self-
energy of the electron INCREASES its mass by ~α × mc²:

- Bare electron mass: ~0.511 MeV (what model-E computes)
- EM self-energy: +α × 0.511 ≈ +0.0037 MeV
- Observed mass: ~0.511 MeV (self-energy is already included
  in the measured mass)

The Ma-t coupling should ADD to the mass, not subtract.  The
Lorentzian sign (g_tt = -1) causes the Schur complement to
ADD to the Ma metric (A_eff = A + bbᵀ), making G̃ larger and
G̃⁻¹ smaller, reducing E.

**This is a serious concern.**  Either:
- The α_eff = |ΔE/E| identification is measuring the wrong
  thing (the mass shift is not the coupling constant)
- The sign convention needs revision (perhaps the coupling
  should be on g_tt = +1 with spatial entries −1, i.e.,
  the (−,+,+,+) vs (+,−,−,−) signature choice)
- The physical coupling acts through a different mechanism
  than what the mass-shell condition computes

This must be resolved before the Ma-t picture is considered
established.


### F5. Mass-shell quadratic gives TWO roots (particle/antiparticle)

The dispersion relation is quadratic in ω.  Both roots are
physical:

| Mode | E_low (MeV) | E_high (MeV) | Splitting (MeV) |
|------|------------|-------------|----------------|
| electron | 0.5073 | 0.5148 | 0.0076 |
| proton | 931.56 | 945.18 | 13.63 |
| deuteron | 1863.10 | 1890.37 | 27.25 |

The splitting represents a charge-dependent mass offset:
particles and antiparticles have slightly different masses
in the Ma-t coupled metric.  This is a known feature of KK
theory (charge-mass coupling) but needs physical
interpretation in MaSt.

The low root was used for the α_eff computation.  The high
root gives the antiparticle mass.


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

1. **One-parameter fit.**  σ is tuned to match α_eff(e) = α.
   Every other species' α_eff is then determined by the fixed
   geometry (circumferences, shears).  The 1.83% gap is a
   property of those geometric ratios, not independent evidence
   that the mechanism is correct.

2. **α_eff ≡ |ΔE/E| is an operational proxy, not α itself.**
   The fine-structure constant governs the Coulomb interaction
   strength.  The fractional mass shift |ΔE/E| is a self-energy-
   like quantity.  Near-equality across species is necessary but
   not sufficient for universal EM coupling.  To establish that
   this IS α, Track 3 must show that the Ma-t coupling produces
   a Coulomb field in S of the standard strength.

3. **Charge signs are hand-coded.**  The sign pattern in the
   Ma-t vector (e-ring negative, p-ring positive) is an ansatz
   matching observed charges.  A first-principles coupling
   should derive the signs from the mode structure.


### F7. R55 vs R59 — not apples-to-apples

| Property | R55 (ℵ, spatial) | R59 (time, Lorentzian) |
|----------|-----------------|----------------------|
| Method | Schur on Euclidean ℵ | Mass-shell on Lorentzian t |
| σ parameter | 0.290 | 0.00860 |
| α_eff(e) | 1.000α | 1.000α |
| α_eff(p) | 0.964α | 0.982α |
| Gap | 3.6% | 1.83% |
| Mass direction | Increases | **Decreases** (F4 concern) |
| Needs ℵ? | Yes | No |

The gap improvement (3.6% → 1.83%) may reflect the change in
computation method (Schur vs mass-shell) rather than the change
in geometry (ℵ vs t).  To isolate the cause, one would need to
apply the mass-shell condition to R55's ℵ metric or the Schur
complement to R59's time metric.  This has not been done.


### F8. Neutrino coupling is NOT emergent — it's hand-coded or indirect

Two cases tested:

**With ν-ring coupled** (b_ν-ring = +σ, hand-coded):
α_eff(ν) = 1.035α.  This is an INPUT, not a prediction.

**Without ν-ring coupled** (b_ν-ring = 0):
α_eff(ν) = 0.127α.  This IS emergent — it comes from the
neutrino mode's ν-ring winding interacting with cross-sheet
shears (σ₄₅, σ₄₆) that connect to the p-ring, which IS
coupled to t.  The coupling is indirect and ~8× weaker than
the charged-particle coupling.

Whether the neutrino SHOULD couple through the ring dimension
is a physical question that this computation does not answer.
The hand-coded case assumes it does; the no-coupling case
shows indirect coupling at 0.127α through cross-sheet
leakage.  Neither result can be cited as evidence for or
against L05 without a physical argument for the ν-ring entry.


## Track 1 status

**Complete with caveats.**

The 10D Lorentzian metric with Ma-t ring coupling achieves a
1.83% universality gap — better than R55's 3.6%.  However:

1. **The mass decrease (F4) is the wrong direction** and
   threatens the physical identification of α_eff with α.

2. **The α_eff definition is ad hoc (F6 caveat 2)** — it
   matches a mass shift to the coupling constant without
   deriving the connection.

3. **The R55 comparison is not controlled (F7)** — the method
   changed along with the geometry.

4. **Neutrino coupling is not emergent (F8)** unless the
   indirect 0.127α through cross-sheet leakage is the
   physical answer.

Track 2 should address:
- Whether re-tuning ε compensates the spectrum shift
- Whether the particle/antiparticle splitting (F5) is physical
- The tube-charge / ring-coupling gap (F2 open question)


## Track 1b: ℵ-mediated time coupling (11D)

### F9. Masses INCREASE — correct direction

Track 1b routes the coupling Ma → ℵ → t.  The ℵ link is
Euclidean (+1 diagonal); only the final ℵ-t leg is Lorentzian.
The double indirection flips the sign relative to Track 1.

Result: all masses INCREASE by ~0.7%.  This is the correct
direction for Coulomb self-energy (charge adds energy to the
rest mass).  **Track 1b resolves the F4 sign problem.**


### F10. Universality gap is 5.24% — worse than Track 1

| Mode | α_eff/α |
|------|---------|
| electron | 1.000 (tuned) |
| proton | 1.044 |
| deuteron | 1.044 |
| Σ⁻ | 1.055 |

Gap: 5.24% (vs Track 1's 1.83%, R55's 3.6%).

The gap is wider because the coupling goes through two hops
(Ma-ℵ and ℵ-t), and the Ma-ℵ entries (±1/(2π)) interact
non-trivially with the internal shears in the Schur complement.


### F11. Signs are inherited from R55 geometry

The effective Ma-t entries (from integrating out ℵ) are:
- e-ring → t: +0.041
- ν-ring → t: −0.041
- p-ring → t: −0.041

These signs emerge from R55's Ma-ℵ geometry × σ_{ℵt}, not
from hand-coding.  However, the sign convention is reversed
relative to the charge convention (e-ring positive, p-ring
negative).  Whether this is physically correct (the coupling
sign may differ from the charge sign) or an error in the
geometry needs investigation.


### F12. Neutrino couples at 0.92α — inherited from R55

The ν-ring was coupled at +1/(2π) in R55's Ma-ℵ block.
Through the ℵ-t chain, this produces α_eff(ν₁) = 0.92α.
This is inherited from R55's choice, not emergent.  If the
ν-ring Ma-ℵ entry were zero, the neutrino coupling would be
purely indirect (through cross-sheet leakage).


### F13. The bare 11D metric has a 1% baseline shift

Even at σ_{ℵt} = 0, the 11D metric produces masses ~1%
higher than model-E.  This is because R55's Ma-ℵ entries
(±1/(2π)) perturb the Ma metric when ℵ is present.  The
tuning of σ_{ℵt} acts ON TOP of this baseline shift,
which complicates the comparison with Track 1.


### F14. Comparison: Track 1 vs Track 1b

| Property | Track 1 (direct Ma-t) | Track 1b (ℵ→t) |
|----------|----------------------|-----------------|
| Dimensions | 10D (no ℵ) | 11D (with ℵ) |
| Knobs | 1 (σ) + 6 hand-coded entries | 1 (σ_{ℵt}) + R55 entries |
| Signs | Hand-coded | Inherited from R55 |
| Mass direction | Decrease (WRONG) | **Increase (CORRECT)** |
| Universality gap | **1.83%** | 5.24% |
| Baseline shift | None | 1% from R55 Ma-ℵ |
| ν coupling | 0.127α (indirect) | 0.92α (from R55) |

**Track 1 wins on universality (1.83% vs 5.24%).**
**Track 1b wins on mass direction and sign inheritance.**

Neither is fully satisfactory.  The ideal would combine
Track 1b's correct sign structure with Track 1's tighter
universality.  This might require adjusting the Ma-ℵ
coupling values (not exactly ±1/(2π)) or combining direct
Ma-t entries with ℵ mediation.


## Track 1c: Minimal electron sheet + ℵ + S + t

### F15. Neither coupling approach touches particle-spectrum entries

On the minimal system (one electron sheet + S + t ± ℵ),
both coupling approaches (direct ring-t and ℵ-mediated)
achieve |Δm|/m = α without modifying:
- The tube dimension (any entry in row/column 0)
- The internal shear (s_e = 2.004, the tube-ring off-diagonal)
- The tube-ring metric structure that sets the particle spectrum

The coupling lives entirely on the ring-t (or ring-ℵ + ℵ-t)
entries.  The tube and shear entries remain free for particle
spectrum tuning when proton and neutrino sheets are added.


### F16. Two approaches, same α, opposite mass direction

| Approach | Parameter | Mass direction | Entry touched |
|----------|-----------|---------------|--------------|
| D1 (direct ring-t) | σ = 0.00855 | DOWN (wrong) | G̃[ring, t] |
| D2 (ℵ-mediated) | σ_ℵt = 0.258 | **UP (correct)** | G̃[ring, ℵ] + G̃[ℵ, t] |

D2 gets the sign right because the coupling goes through ℵ
(Euclidean, +1 diagonal) before reaching t (Lorentzian, -1).
The double hop flips the sign relative to D1.


### F17. Generation structure is preserved

All modes on the electron sheet shift by the same fractional
amount (~0.5-0.9%), so mass RATIOS are preserved:

| Mode | Bare ratio to (1,2) | D2 coupled ratio |
|------|-------------------|-----------------|
| (1,1) | 205.0 | 206.0 |
| (1,3) | 203.3 | 204.3 |
| (3,5) | 206.8 | 207.8 |

The muon-range candidates remain in the right range.  The
generation mechanism (shear resonance) is unaffected because
the coupling is on the ring, not the shear.


### F18. The ℵ-mediated approach has structural advantages

D2 (ℵ-mediated) is cleaner than D1 (direct) because:
1. Mass goes UP (correct for Coulomb self-energy)
2. The ℵ-t entry is SHARED across all sheets (one parameter
   for universality, not one per sheet)
3. Each sheet adds only its own ring-ℵ entry (sign = charge)
4. ℵ can be "switched off" by setting all Ma-ℵ entries to zero
   (ℵ diagonal remains but is inert)

However, ℵ remains an open question.  D1 (direct) is simpler
(no extra dimension) even though the mass sign is wrong.  The
mass sign issue might resolve when the full KK reduction is
done (Track 3) — the sign may depend on whether we're
computing a self-energy or a coupling constant.


## Track 1 overall status

**Tracks 1, 1b, 1c complete.**

Key findings:
1. Ring coupling works; tube coupling doesn't (F2)
2. Mass-shell condition is the correct Lorentzian tool (F3)
3. Direct Ma-t: 1.83% universality gap but mass DECREASES (F4, F6)
4. ℵ-mediated: mass INCREASES (correct) but wider gap (F9, F10)
5. On the minimal electron sheet: coupling doesn't touch particle
   entries (F15) — proton/neutrino can be added without conflict
6. Generation structure preserved under coupling (F17)
7. The coupling parameter: σ ≈ 0.009 (direct) or σ_ℵt ≈ 0.26 (ℵ)
8. ℵ gives correct mass direction; direct gives better universality;
   both remain open approaches


## Track 1d: Two sheets (electron + proton) — universality

### F19. Two-sheet results match single-sheet — no cross-sheet interference

Adding the proton sheet to the minimal metric does not
change the electron's coupling or vice versa.  The gaps
are essentially identical to the single-sheet (Track 1c)
and full model-E (Track 1) results:

| Approach | 1-sheet gap | 2-sheet gap | Full model-E gap |
|----------|-----------|-----------|-----------------|
| D1 (direct) | N/A | 1.84% | 1.83% |
| D2 (ℵ-med) | N/A | 4.23% | 5.24% |

The two sheets are independent: each has its own ring entry,
and the coupling for one sheet doesn't affect the other.
This confirms F15 — the coupling entries don't conflict with
the particle spectrum entries.


### F20. The tradeoff is structural

| Property | D1 (direct ring-t) | D2 (ℵ-mediated) |
|----------|-------------------|-----------------|
| Gap | **1.84%** | 4.23% |
| Mass direction | DOWN (wrong) | **UP (correct)** |
| Parameters | 1 per sheet (ring-t) | 1 per sheet (ring-ℵ) + 1 shared (ℵ-t) |
| Signs | Hand-coded | Inherited |

Neither approach alone gives both tight universality AND
correct mass direction.  The gap is a geometric property of
the sheet aspect ratios and shears — it doesn't change with
the coupling architecture.


### F21. The D2 coupling is non-monotonic

The ℵ-mediated α_eff passes through a minimum near σ_ℵt ≈ 0.10
(where α_eff ≈ 0.09α for both sheets).  Below this, the
coupling increases with decreasing σ_ℵt.  Above it, the
coupling increases with increasing σ_ℵt.

This means the Schur complement through ℵ (Euclidean) and
through t (Lorentzian) partially cancel at intermediate
values, producing a near-zero coupling.  The electron and
proton pass through zero at slightly different σ_ℵt values,
which creates the universality gap.


## Track 1 series status

**Tracks 1, 1b, 1c, 1d complete.**

The bottom-up approach (1c → 1d) confirmed the top-down
results (1, 1b):
- Ring coupling works; tube coupling doesn't
- Direct Ma-t gives ~1.8% gap but wrong mass sign
- ℵ-mediated gives correct mass sign but ~4-5% gap
- Coupling doesn't touch particle-spectrum entries
- Generation structure is preserved
- The gap is structural (from sheet geometry), not
  from the coupling architecture

Next: add neutrino sheet (Track 1e) and/or investigate
whether the mass-sign issue in D1 is a real physical
problem or an artifact of the α_eff definition.
