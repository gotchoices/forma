# R45: Magnetic moments from cross-sheet coupling

**Status:** On hold — see Q100 (aperture-based moment enhancement)
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

## The geodesic tilting hypothesis — REFUTED (Track 1)

The original hypothesis was that cross-shear σ_ep tilts the
proton's geodesic onto Ma_e, causing the charge to sweep a larger
area and amplifying the moment.  This treated the proton as a
classical charged particle orbiting on the torus.

**Track 1 showed this is the wrong picture.**  The proton is a
standing wave ψ = exp(i(n₅θ₅ + n₆θ₆)) with uniform charge
density |ψ|² everywhere on the torus.  Nothing orbits.  There is
no velocity to redistribute between sheets.

The magnetic moment of a wave mode comes from its angular momentum:

<!-- ⟨L₆⟩ = ℏn₆ -->
$$
\langle\hat{L}_6\rangle = \hbar\, n_6
$$

<!-- μ = (e/2m_p) ℏn₆ = n₆ μ_N -->
$$
\mu = \frac{e}{2m_p}\,\hbar\,n_6 = n_6\,\mu_N
$$

This depends on the winding number n₆ — a topological integer.
Cross-shear cannot change n₆.  The geodesic tilting mechanism
is dead.  See `findings.md` F1.

---

## Tracks

### Track 1: Proton moment from geodesic tilting — DEAD

Wrong premise.  See `findings.md` F1.

### Track 2: Neutron moment — DEAD (same premise)

Same error.  The neutron (0,−2,1,0,0,2) has Q = 0, so no
single-mode magnetic moment exists at all.  The measured
μ_n = −1.913 μ_N requires composite structure (Track 3).

### Track 3: Self-consistent multi-sheet solution

Track 3 is now the primary path.  Unlike Tracks 1/2/4, it does
not treat the proton as a single mode on a fixed metric.  Instead,
it treats the proton as a composite: the bare mode plus cross-sheet
excitations with their own winding numbers.  The total angular
momentum — and hence the magnetic moment — depends on the
superposition, not on any single n₆.

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

### Track 4: Electron moment — DEAD (same premise as Track 1)

### Track 5: Dark mode census on Ma_p — DIS connection

Dark modes can't add magnetic moment (uncharged → no current),
but they CAN explain DIS scattering centers.  This track is about
proton structure, not the moment.

1. Enumerate uncharged (n₅ = 0) modes on Ma_p up to ~2 GeV.
   Lightest: (0,0,0,0,0,1) at ~466 MeV (one ring winding).

2. Superposition (1,2) + (0,3): does it produce 3-lobed field
   patterns?  (Challenge: (0,3) costs ~1400 MeV — heavier than
   the proton.  Would need to be virtual.)

3. Momentum fractions: if dark modes carry ~50% of proton
   momentum (like gluons in QCD), what modes are required?

**Status:** Secondary.  Worth cataloging for the DIS question
but doesn't directly address the magnetic moment.

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

**Status:** Speculative.  Tracks 1–2 are dead, so this could
be revisited, but the parameter constraints from R27 are tight.

---

## Reference data

**Proton sheet geometry** (R27 F18):

| Parameter | Value |
|-----------|-------|
| r_p       | 8.906 |
| σ_ep      | −0.091 |
| L₅ (tube) | 23.66 fm |
| L₆ (ring) | 2.657 fm |
| s₅₆       | from α(r_p, s) = α_measured |

**Fine-structure constant** (measured, used in code):

α = 7.2973525693 × 10⁻³  (not 1/137)

---

## What success looks like

| Outcome | Value |
|---------|-------|
| Self-consistent solve converges (T3) | Dressed-particle picture is internally coherent |
| g_p ≈ 5.6 from dressed proton (T3) | First non-quark derivation of proton moment |
| g_n ≈ −3.8 from dressed neutron (T3) | Independent validation; tests sign |
| q_ν < 10⁻¹⁵ e from reverse coupling (T3) | Consistency with reactor neutrino bounds |

## What failure looks like

| Outcome | What it means |
|---------|--------------|
| Self-consistent solve diverges or has multiple fixed points (T3) | Dressed-particle picture is underdetermined |
| q_ν > 10⁻¹⁵ e (T3) | Cross-sheet charge dressing too strong; mechanism falsified |
| g_p wildly wrong from dressed solve (T3) | Cross-sheet excitations don't produce right angular momentum |

---

## Files

| File | Description |
|------|-------------|
| `README.md` | This file — study design |
| `scripts/track1_proton_moment.py` | Track 1 (dead) — kept for reference |
| `scripts/track3_self_consistent.py` | Track 3 — dressed-particle solve |
| `scripts/track5_dark_modes.py` | Dark mode census; DIS connection |
| `findings.md` | Results and interpretation |
