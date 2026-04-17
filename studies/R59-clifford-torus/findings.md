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
- The mass-decrease sign problem (F4)
- Whether re-tuning ε compensates the 0.7% spectrum shift
- Whether the particle/antiparticle splitting (F5) is physical
- The tube-charge / ring-coupling gap (F2 open question)
