# R45: Magnetic moments from cross-sheet coupling

**Status:** Framed
**Questions:** Q53 (anomalous magnetic moment), Q34 (α derivation)
**Type:** compute
**Depends on:** R19 (charge from shear), R27 (cross-shear σ_ep, proton sheet
parameters), R28 (mode spectrum), R33 (ghost modes), R44 (negative result —
single-sheet moment is order r, not order α)

---

## Motivation

R44 showed that single-sheet geometric effects (charge-mass separation,
torus-knot wobble) produce order-r corrections to the magnetic moment —
far too large and wrong sign for the electron's α/(2π) ≈ 0.001, and
not even the right mechanism for the proton's huge g_p ≈ 5.586.

The topological argument gives g = 2 for any (1,2) mode on any sheet.
The proton (0,0,0,0,1,2) on Ma_p and the electron (1,2,0,0,0,0) on
Ma_e both get g = 2, yet:

| Particle | g (measured) | g (topological) | Discrepancy |
|----------|-------------|-----------------|-------------|
| Electron | 2.00232     | 2               | 0.12% too high |
| Proton   | 5.586       | 2               | 180% too high  |
| Neutron  | −3.826 (in μ_N) | 0 (neutral) | nonzero from zero |

These three anomalies differ by orders of magnitude.  No single-sheet
mechanism can explain all three.

---

## The mechanism: geometric orbit tilting

### Cross-shear tilts the geodesic into other sheets

The cross-shear σ_ep = −0.091 (R27 F18) makes the 6D metric
non-block-diagonal.  On a block-diagonal metric, the proton mode
(0,0,0,0,1,2) travels purely in the Ma_p directions (θ₅, θ₆).
With σ_ep ≠ 0, the geodesic tilts — the photon's velocity acquires
components in the Ma_e directions (θ₁, θ₂).

The geodesic tangent vector is determined by the inverse metric:

<!-- v_i ∝ G̃⁻¹_ij n_j -->
$$
v_i \propto \tilde{G}^{-1}_{ij}\, n_j
$$

When G̃⁻¹ has off-diagonal blocks (from σ_ep), the velocity v has
Ma_e components even for a purely Ma_p mode vector n = (0,0,0,0,1,2).
The photon physically moves in Ma_e space.

### Charge is topological — moment is geometric

This is the crucial asymmetry that makes the mechanism work:

- **Charge** is set by the winding number n₅ = 1.  It is a
  topological invariant — you cannot partially wind around the
  tube.  The proton has charge +e exactly, regardless of σ_ep.

- **Magnetic moment** depends on WHERE that charge orbits in
  physical 3D space.  If the geodesic tilts onto Ma_e, the
  charge sweeps through a larger effective area (Ma_e radius
  is ~400× Ma_p radius).

| Quantity | Depends on | Changes with σ_ep? |
|----------|-----------|-------------------|
| Charge Q | Winding number n₅ (topological) | **No** — integer, exact |
| Energy E | Metric eigenvalue n̄ᵀ G̃⁻¹ n̄ | Yes — continuous |
| Moment μ | Current × orbit area (geometric) | **Yes** — amplified by R_e/R_p |

A small geometric tilt produces a large moment correction with
zero charge change.

### The scaling argument

For a charge e orbiting at radius R:

| Quantity | Formula | R-dependence |
|----------|---------|-------------|
| Charge   | Q = e   | none |
| Moment   | μ = e v R / 2 | **linear in R** |

The moment-to-charge ratio scales as R.  The relevant radii:

| Sheet | Orbit radius R | Ratio to R_p |
|-------|---------------|-------------|
| Ma_p  | L₆/(2π) ≈ 0.42 fm | 1 |
| Ma_e (r_e ≈ 1) | L₂/(2π) ≈ 160 fm | **~380** |
| Ma_ν  | L₄/(2π) ≈ 6.7 μm | **~1.6 × 10⁷** |

If the cross-shear tilts a fraction f of the proton's geodesic
velocity onto Ma_e, the moment gains:

<!-- Δμ/μ_naked ≈ f × R_e/R_p ≈ f × 380 -->
$$
\frac{\Delta\mu}{\mu_\text{naked}} \approx f \times
\frac{R_e}{R_p} \approx f \times 380
$$

For g_p ≈ 5.6 (Δμ/μ_naked ≈ 1.8): need **f ≈ 0.5%**.  A
half-percent tilt of the geodesic.  With σ_ep = −0.091 (~9%
metric coupling), this is geometrically plausible.

### Self-consistent α

The R19 charge formula was derived for a single sheet (σ_ep = 0).
With σ_ep ≠ 0, the metric changes and the charge integral gets
a small correction:

<!-- α(r, s, σ_ep) = α(r, s, 0) + O(σ_ep²) -->
$$
\alpha(r, s, \sigma_{ep}) = \alpha(r, s, 0) + O(\sigma_{ep}^2)
$$

The measured α already includes this correction.  The within-plane
shear s adjusts at order σ_ep² to compensate, keeping α = 1/137.036
exactly.  The code uses the measured α = 7.2973525693 × 10⁻³ (not
the rounded 1/137).

This means the moment correction from σ_ep is NOT in tension with
the α value — the model self-consistently absorbs the charge
correction into the shear.

### Why proton is huge, electron is tiny

| Particle | Couples to | Radius ratio | σ coupling | Expected Δg |
|----------|-----------|-------------|-----------|------------|
| Proton   | Ma_e (UP) | R_e/R_p ≈ 380 | σ_ep = 0.091 | ~0.5% × 380 ≈ **large** |
| Electron | Ma_ν (UP) | R_ν/R_e ≈ 10⁷ | σ_eν ≈ ? | tiny × huge = **tiny** |
| Electron | Ma_p (DOWN) | R_p/R_e ≈ 1/380 | σ_ep = 0.091 | ~9% × 0.003 = **tiny** |

The proton's anomaly is large because it couples UP to a much
larger sheet.  The electron's anomaly is tiny because its coupling
to Ma_ν is extremely weak (σ_eν unconstrained but negligible per
R28), and its coupling DOWN to Ma_p suppresses the moment instead
of amplifying it.

---

## Can dark modes contribute?

**Directly: no.**  An uncharged mode (n₅ = 0 on Ma_p, or n₁ = 0
on Ma_e) has no current and cannot produce a magnetic dipole moment.
μ = (1/2) ∫ (r × J) dV, and J = 0 for uncharged modes.

**Indirectly: possibly.**  Dark modes modify the energy density
landscape, which could change the effective geometry that the charged
mode orbits in.  If dark modes create density "bumps" that shift
the charged mode's orbit to larger or smaller radii, they change
the moment.  But this is a second-order effect (dark mode amplitude
× charged mode amplitude × geometry factor) and hasn't been
computed.

Dark modes are more relevant to **DIS** (three scattering centers)
than to the magnetic moment.  A 3-fold-symmetric dark mode
superimposed on the (1,2) proton mode could create lobes visible
in scattering without directly affecting the moment.

---

## Tracks

### Track 1: Proton moment from geodesic tilting

The core computation.  Use the existing 6D metric (ma.py) with
σ_ep = −0.091 and r_p = 8.906:

1. **Build the full metric** G̃ with cross-shear.  Compute G̃⁻¹.

2. **Geodesic velocity** for mode n = (0,0,0,0,1,2):
   v_i = G̃⁻¹_ij n_j (unnormalized).  Decompose into Ma_e
   components (v₁, v₂) and Ma_p components (v₅, v₆).

3. **Velocity fraction on Ma_e:** f_e = |v_e|² / |v|² — the
   fraction of the photon's velocity in the Ma_e directions.

4. **Effective moment:** the charge +e orbits with velocity
   fraction f_e at radius R_e and fraction (1−f_e) at radius R_p.
   Compute μ_z from the combined orbit.

5. **Extract g_p** = 2m_p μ_total / (e × ℏ/2).

6. **Compare** to measured g_p = 5.586.

**No free parameters** — σ_ep, r_p, and all sheet dimensions are
already determined by the neutron mass and α.

**Output:** g_p from the cross-sheared geodesic.

### Track 2: Neutron moment — the crucial test

The neutron IS the cross-mode (1,2,0,0,1,2).  Its geodesic
inherently spans both Ma_e and Ma_p — no perturbation theory
needed.

1. **Geodesic velocity** for n = (1,2,0,0,1,2).  Decompose into
   Ma_e and Ma_p components.

2. **Charge distribution:** the neutron has n₅ − n₁ = 1 − 1 = 0
   total charge, but the Ma_e component carries charge −1 (n₁ = 1)
   and the Ma_p component carries charge +1 (n₅ = 1).  These
   orbit at different radii.

3. **Magnetic moment from partial cancellation:** the Ma_e
   contribution (charge −1 at large radius) and Ma_p contribution
   (charge +1 at small radius) partially cancel.  The net moment
   is negative if the Ma_e term dominates.

4. **Compare** to measured μ_n = −1.913 μ_N.

The **negative sign** is the hardest test — it demands that the
larger-radius Ma_e orbit dominates despite carrying opposite charge.

**Output:** g_n.  A match validates the entire cross-sheet picture.

### Track 3: Self-consistent multi-sheet solution

The individual tracks (1, 2, 4) compute moments using the FIXED
metric — σ_ep = −0.091 from R27, shears from α_measured.  But this
misses the feedback loop: each particle's existence funds
oscillations on other sheets, which change the environment for
other particles.

**The cascade:**
- A proton on Ma_p, through σ_ep, excites oscillations on Ma_e.
  The proton can't exist without keeping Ma_e "warm."
- An electron on Ma_e, through σ_eν, excites oscillations on Ma_ν.
  You can't have an electron without funding neutrino-sheet modes.
- Energy flows downhill: heavy → light.  Each heavier particle
  drives the sheets below it.

**The dressed-particle picture:**
What we call "the electron" is not the bare (1,2,0,0,0,0) mode
on Ma_e — it is that mode PLUS whatever it necessarily funds on
Ma_ν through σ_eν, PLUS any tiny Ma_p contribution through σ_ep.
The measured mass m_e = 0.511 MeV is the total energy of this
composite.  The measured charge e is the total charge.  When we
set L_θe = ℏc/m_e, we're implicitly absorbing the cross-sheet
energy into the calibration.

**Charge is not exempt from dressing:**
The charge formula Q = −n₁ + n₅ (R19) was derived for isolated
sheets with within-plane shear only.  On the full coupled 6D
torus, cross-shear mixes sheet dimensions, and the Gauss's-law
flux integral over a cross-section of the coupled torus may give
a different answer than the single-sheet formula.  The funded
oscillations on Ma_ν are not independent neutrino modes with their
own winding numbers — they are excitations driven by the electron
through the cross-shear coupling.  Whether they carry some small
effective charge is an open question that Track 3 must answer by
re-deriving the charge integral on the coupled metric.

We can't tell the charge is "off" because e is defined by
measurement, and the measurement already includes all cross-sheet
effects.  What we CAN check is whether dimensionless RATIOS
(μ_p/μ_n, μ_e/μ_p, g-factors) come out right — those don't
depend on the definition of e.

**Geometric charge renormalization:**
This is the MaSt analog of charge renormalization in QED:
- QED: bare charge + virtual photon cloud = measured charge e
- MaSt: bare Ma_e charge + funded cross-sheet oscillations = measured charge e
The mechanism is geometric rather than perturbative, but the
structure is identical.  The anomalous moment arises because the
dressed particle orbits on multiple sheets at different radii,
and the moment (linear in R) picks up contributions that charge
(topological, 0th moment) does not — or picks up differently.

**The computation:**

1. Start with bare parameters: the 6D metric (σ_ep, σ_eν, r_p,
   r_e, r_ν, all shears) and bare winding numbers.

2. Solve the wave equation on the full coupled 6D torus.  The
   eigenmodes are NOT products of single-sheet modes — they are
   mixed states spanning all three sheets.

3. Identify the eigenmode closest to (1,2,0,0,0,0) — this is
   the dressed electron.  Its wavefunction has support on Ma_e
   (dominant), Ma_ν (small), and Ma_p (tiny).

4. Compute the Gauss's-law charge integral for this eigenmode
   on the coupled metric.  This gives the dressed charge.

5. Compute the magnetic moment from the current distribution
   of this eigenmode across all three sheets.

6. **Adjust bare parameters** (shears, aspect ratios) until
   the dressed observables match: m_e = 0.511 MeV, α = 1/137.036,
   m_p = 938.3 MeV, m_n = 939.6 MeV, etc.

7. Read off: α, μ_p, μ_n, μ_e, m_ν from the converged solution.

**Why this gives "strange off-integer" moments:**
Each dressed particle orbits partly on its own sheet and partly
on the sheets it funds.  The moment is a weighted sum over all
sheets, each contributing at its own radius.  There's no reason
this sum should give a round number — it gives whatever the
coupled geometry dictates.

**Why the sheet scales shift slightly:**
If some of m_e lives on Ma_ν, then L_θe (calibrated from m_e)
is currently absorbing that cross-sheet energy.  The self-consistent
solve would separate them: a slightly different "bare" L_θe for the
Ma_e component, plus the Ma_ν contribution that makes up the
total.  The shift is small (order σ_eν²) but conceptually
important — it means the current parameter values are effective,
not fundamental.

**Funded oscillations are not clean integer modes:**
The cross-sheet excitations driven by the electron on Ma_ν are
forced oscillations at the electron's frequency (~MeV), not free
neutrino modes at their natural frequency (~meV).  They don't
have well-defined integer winding numbers — their amplitudes are
small continuous values ε₃, ε₄ determined by σ_eν and the
off-resonance suppression factor.

**Neutrino charge as consistency check:**
Cross-shear couples both directions: Ma_e → Ma_ν (electron funds
neutrino oscillations) and Ma_ν → Ma_e (neutrino drives electron-
sheet oscillations).  The reverse coupling is suppressed by the
energy ratio: a ~meV neutrino trying to drive ~MeV Ma_e modes
gives an amplitude suppression of (m_ν/m_e)² ~ 10⁻¹⁸.  This
predicts a tiny neutrino charge:

<!-- q_ν ~ σ_eν × (m_ν/m_e)² × e ~ 10⁻²⁰ e -->
$$
q_\nu \sim \sigma_{e\nu} \times \left(\frac{m_\nu}{m_e}\right)^2
\times e \;\sim\; 10^{-20}\,e
$$

The experimental bound is q_ν < 10⁻¹⁵ e (reactor experiments),
so the prediction is safely below.  This is a one-way check: if
Track 3's charge integral gave q_ν > 10⁻¹⁵ e, it would falsify
the mechanism.

**This track subsumes Tracks 1, 2, and 4** — they become stepping
stones (the "zeroth iteration" where cross-sheet dressing is
ignored).  Track 3 is the full self-consistent solve.

**Output:** self-consistent α, μ_p, μ_n, μ_e, m_ν from the
coupled 6D system.  All from geometry — no free parameters beyond
those already pinned by R27 (which itself would be re-derived in
the coupled framework).

### Track 4: Electron moment from cross-sheet coupling

Apply geodesic tilting to the electron (1,2,0,0,0,0):

1. **Coupling DOWN to Ma_p** (σ_ep = −0.091): the geodesic
   tilts into Ma_p directions.  Ma_p has a SMALLER radius, so
   the moment DECREASES.  This gives g < 2 — **wrong sign**.

2. **Coupling UP to Ma_ν** (σ_eν unknown): the geodesic tilts
   into Ma_ν directions.  Ma_ν has an ENORMOUS radius, so even
   a tiny tilt produces a large moment.  Need f_ν × R_ν/R_e ≈
   α/(2π) ≈ 0.001.  This constrains σ_eν.

3. **Predict σ_eν** from matching α/(2π).  Is the predicted value
   physical (small enough to be consistent with R28's finding that
   σ_eν is negligible for MeV-scale physics)?

4. **Sign check:** does coupling UP to Ma_ν give g > 2?

**Output:** σ_eν prediction; viability of cross-sheet mechanism
for the electron anomaly.

### Track 5: Dark mode census on Ma_p — DIS connection

Dark modes can't add magnetic moment (see analysis above), but
they CAN explain DIS scattering centers.  This track is about
proton structure, not the moment.

1. Enumerate uncharged (n₅ = 0) modes on Ma_p up to ~2 GeV.
   Lightest: (0,0,0,0,0,1) at ~466 MeV (one ring winding).

2. Superposition (1,2) + (0,3): does it produce 3-lobed field
   patterns?  (Challenge: (0,3) costs ~1400 MeV — heavier than
   the proton.  Would need to be virtual.)

3. Momentum fractions: if dark modes carry ~50% of proton
   momentum (like gluons in QCD), what modes are required?

**Status:** Secondary to Tracks 1–4.  Worth cataloging for the
DIS question but doesn't directly address the magnetic moment.

### Track 6: Three-mode proton (neutrino analog) — speculative

The radical hypothesis: the proton sheet is ~3× larger than
currently assumed, hosting three sub-modes at ~313 MeV each
(from R14's m_p = 3 × 612 m_e coincidence).

**Challenges:**
- Changes L₆ from 2.657 fm to ~8 fm, breaking R27/R28 fits
- Requires re-deriving the entire hadron spectrum
- The current proton sheet size is well-constrained by the
  neutron mass + muon mass jointly (R27 F18)

**If pursued:** would need to show that the rescaled sheet
still produces m_n, m_μ, and the hadron spectrum.  This is a
major structural change, not a perturbative correction.

**Status:** Speculative.  Park unless Tracks 1–2 fail.

---

## Key formulas

**Geodesic velocity** on the 6D sheared torus:

For mode n = (n₁, ..., n₆) on metric G̃ with circumferences L:

<!-- v_i = Σ_j G̃⁻¹_ij (n_j / L_j) -->
$$
v_i = \sum_j \tilde{G}^{-1}_{ij}\,\frac{n_j}{L_j}
$$

The physical velocity in 3D decomposes into sheet contributions.
The Ma_e velocity fraction:

<!-- f_e = (v₁² L₁² + v₂² L₂²) / Σ(v_i² L_i²) -->
$$
f_e = \frac{v_1^2 L_1^2 + v_2^2 L_2^2}
{\sum_i v_i^2 L_i^2}
$$

**Proton sheet geometry** (R27 F18):

| Parameter | Value |
|-----------|-------|
| r_p       | 8.906 |
| σ_ep      | −0.091 |
| L₅ (tube) | 23.66 fm |
| L₆ (ring) | 2.657 fm |
| s₅₆       | from α(r_p, s) = α_measured |

**Moment scaling:**

| Sheet | Orbit radius R | Ratio to R_p |
|-------|---------------|-------------|
| Ma_p  | L₆/(2π) ≈ 0.42 fm | 1 |
| Ma_e (r_e ≈ 1) | L₂/(2π) ≈ 160 fm | ~380 |
| Ma_ν  | L₄/(2π) ≈ 6.7 μm | ~1.6 × 10⁷ |

**Fine-structure constant** (measured, used in code):

α = 7.2973525693 × 10⁻³  (not 1/137)

---

## What success looks like

| Outcome | Value |
|---------|-------|
| g_p ≈ 5.6 from geodesic tilting (T1) | First non-quark derivation of proton moment |
| g_n ≈ −3.8 from cross-mode structure (T2) | Independent validation; tests sign |
| Self-consistent solve converges (T3) | Dressed-particle picture is internally coherent |
| q_ν < 10⁻¹⁵ e from reverse coupling (T3) | Consistency with reactor neutrino bounds |
| σ_eν prediction from electron g−2 (T4) | Connects anomalous moment to cross-shear |

## What failure looks like

| Outcome | What it means |
|---------|--------------|
| f_e too small → g_p ≈ 2 (T1) | σ_ep doesn't tilt the geodesic enough |
| g_n wrong sign (T2) | Orbit geometry algebra is wrong |
| Self-consistent solve diverges or has multiple fixed points (T3) | Dressed-particle picture is underdetermined |
| q_ν > 10⁻¹⁵ e (T3) | Cross-sheet charge dressing too strong; mechanism falsified |
| σ_eν must be large (T4) | Would contradict R28; electron anomaly needs different mechanism |

---

## Files

| File | Description |
|------|-------------|
| `README.md` | This file — study design |
| `scripts/track1_proton_moment.py` | Geodesic tilting; g_p from σ_ep |
| `scripts/track2_neutron_moment.py` | Cross-mode neutron moment; g_n test |
| `scripts/track3_self_consistent.py` | Full coupled 6D solve; dressed particles |
| `scripts/track4_electron_moment.py` | Electron g−2 from cross-sheet coupling |
| `scripts/track5_dark_modes.py` | Dark mode census; DIS connection |
| `findings.md` | Results and interpretation |
