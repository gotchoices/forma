# R47: Proton geometry — mode, slots, and anomalous moment

**Status:** Active (Tracks 4–6)
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

The proton is the next target.

### Mode hypothesis history

**Tracks 1–3 explored the (1,3) hypothesis** — motivated by
three-fold quark symmetry and clean 3-slot ghost-killing geometry.
However, the WvM spin formula gives spin = n₁/n₂ = 1/3 for (1,3).
The proton has spin ½.  Quarks have fractional charge (⅓, ⅔),
not fractional spin — quarks all have spin ½.  The (1,3) hypothesis
is therefore **abandoned**.  Tracks 1 and 3 are nullified; Tracks 0
and 2 remain valid as tool infrastructure.

**Track 4 returns to (1,2)** — the proton is a (1,2) mode on Ma_p,
same topology as the electron on Ma_e.  Spin = n₁/n₂ = ½. ✓

The proton's anomalous magnetic moment (κ_p = 1.793, g_p = 5.586)
is explored through a **spindle torus** hypothesis: the proton has
ε > 1, causing the torus to self-intersect.  The self-intersecting
surface cannot project charge outward, but the photon's current
loop is unaffected — enhancing μ/Q.


## Deriving particle geometry from known inputs

Given a hypothesized mode (n₁, n₂) and a known particle mass m,
what can we determine — and what remains free?

**Known inputs:**
- Particle mass m → reduced Compton wavelength ƛ = ℏ/(mc)
- Fine structure constant α = 1/137.036
- Mode winding numbers (n₁, n₂) = (1, 2) for the proton

**Derivation chain:**

1. **α pins shear as a function of ε.**  The α formula α = f(ε, s)
   with q_eff = n₂ − s·n₁ has one equation and two unknowns (ε, s).
   For any chosen ε, there is a unique s that reproduces α = 1/137.
   So s = s(ε).

2. **Mass gives the eigenvalue.**  The dimensionless eigenvalue
   μ = √(1/ε² + q_eff²) depends only on ε (since s is
   determined by step 1).

3. **Compton wavelength + eigenvalue → tube circumference.**
   L_θ = ƛ × μ(ε).  This is the tube circumference, determined
   once ε is chosen.

4. **ε → ring circumference.**  L_φ = L_θ / ε.

5. **Absolute dimensions.**  Tube radius a = L_θ/(2π),
   ring radius R = L_φ/(2π), sheet area = L_θ × L_φ.

---

## Tracks

### Track 0: Torus Lab support for proton mode

**Status:** Complete — tool infrastructure, still valid.


### Track 1: Proton (1,3) mode analysis

**Status:** Null — (1,3) gives spin ⅓, not ½.  Proton has spin ½.

**Findings:** See [findings.md](findings.md), Track 1.  The mode
survival computations are mathematically correct but physically
inapplicable since the proton cannot be (1,3).


### Track 2: Torus Lab generalization

**Status:** Complete — tool infrastructure, still valid.

The lab now supports arbitrary target modes via shear presets and
`lowestSurvivorIdx()`.  Works for (1,2) proton just as well.


### Track 3: Proton (1,3) slot geometry

**Status:** Null — depends on (1,3) hypothesis (Track 1).

**Findings:** See [findings.md](findings.md), Track 3.  Slot
sizing computations correct but physically inapplicable.


### Track 4: Spindle torus and proton anomalous moment

**Status:** Active

**Goal:** Test whether a spindle torus (ε > 1) can explain the
proton's anomalous magnetic moment through geometric charge
obscuration.

**Hypothesis:**

The proton is a **(1,2) mode** on Ma_p (spin ½, same topology
as the electron).  Its torus has aspect ratio **ε = a/R > 1** —
a spindle configuration where the tube radius exceeds the ring
radius and the surface self-intersects.

In the self-intersecting region (near the inner equator, where
1 + ε cos θ₁ < 0), the surface normal flips.  We hypothesize
that this hidden surface **cannot project charge outward** — it
is geometrically obscured.  However, the photon's energy still
circulates around the full loop, generating magnetic moment from
the entire current path.

The result: charge is reduced (hidden surface excluded from
charge integral), but moment is not proportionally reduced
(current uses full loop).  The ratio μ/Q is enhanced, producing
an anomalous magnetic moment.

**Target:**

| Quantity | Value |
|----------|-------|
| g_Dirac | 2 (spin-½ Dirac prediction) |
| g_proton | 5.5856 (measured: 2 × μ_p/μ_N) |
| Required enhancement | g_p / g_Dirac = 2.793 |
| Visible surface fraction | f = g_Dirac / g_p = 0.358 |

**Method:**

1. Sweep ε from 0.5 through ε > 1 (spindle regime).

2. At each ε, compute:
   - Shear s from α(ε, s) = 1/137.036 with q = 2 − s
   - The visible region: {θ₁ : 1 + ε cos θ₁ ≥ 0}
   - The charge integral over visible surface only (using
     flat-torus mode shape f(θ₁) = cos θ₁ as first approx)
   - The charge integral over full surface (for comparison)
   - The visible fraction by various metrics (area-weighted,
     charge-weighted)
   - Absolute dimensions from proton mass

3. Determine whether there exists an ε where the visible
   charge fraction matches the target f = 0.358.

4. At that ε, verify:
   - Shear can be adjusted to give Q_visible = +e
   - 4 slots on inner equator (like electron) are hidden
     in the self-intersecting region → no charge leakage
   - Absolute dimensions are physically reasonable

**Key questions:**
- Does the direction of the effect work as hypothesized?
  The hidden inner-equator surface contributes negatively
  to the charge integral — hiding it might INCREASE net
  charge rather than decrease it.  The script must check.
- Can the eigensolver be extended to ε > 1, or must we use
  a flat-torus mode approximation in the spindle regime?
- What happens to mode survival (ghost killing) when ε > 1?

**Script:** `scripts/track4_spindle_moment.py`

**Depends on:** Nothing — fresh approach.

**Findings:** See [findings.md](findings.md), Track 4.


### Track 5: Quark model moment check

**Status:** Framing

**Goal:** Verify the standard constituent-quark prediction
for the proton's magnetic moment using MaSt parameters.

This is a **calculation**, not a sheet-design hypothesis.
We treat the three quarks as independent Dirac particles
with their own charges and masses, combine their moments
using SU(6) spin-flavor weights, and compare to experiment.

**Preliminary result:**

For constituent quarks (mass m_p/3, charges +2e/3 and −e/3,
each with Dirac g = 2):

| Quark | Charge | Mass | μ_Dirac |
|-------|--------|------|---------|
| u | +2e/3 | m_p/3 | +2 μ_N |
| d | −e/3 | m_p/3 | −1 μ_N |

SU(6) combination for proton (uud, spin ↑):

μ_p = (4/3) μ_u − (1/3) μ_d = 8/3 + 1/3 = **3 μ_N**

Measured: **2.793 μ_N** (93% match).

To match exactly: g_q = 1.862 (slightly below Dirac).

**Method:**

1. Compute the SU(6) moment sum for proton and neutron.
2. Compare residuals: proton 7% high, neutron (udd)
   predicts −2 μ_N vs measured −1.913 μ_N (~4% high).
3. Explore whether the residual comes from binding
   corrections, slot apertures, or ε-dependent effects.

**Key distinction from Track 6:** This track treats quarks
as given entities and checks the moment arithmetic.  It
does not explain why quarks exist, why they have mass m_p/3,
or why they're confined.  Track 6 addresses those questions
through sheet design.

**Depends on:** Track 4 (spindle results for context).

**Findings:** See [findings.md](findings.md), Track 5.


### Track 6: Proton as (3,6) mode — confinement from filtering

**Status:** Framing

**Goal:** Test whether the proton's sheet is designed for a
(1,2) particle at **1/3 the proton mass**, with nodes that
block the (1,2) fundamental so that the first surviving
mode is **(3,6)** — requiring 3× the energy (a proton's
worth) to excite.

**Sheet design:**

The proton sheet (Ma_p) is sized so that a (1,2) mode has
mass m_p/3 ≈ 313 MeV (= constituent quark mass).  The
mode spectrum on this sheet:

| Mode | Eigenvalue | Mass | Identity |
|------|-----------|------|----------|
| (1,1) | μ₁₁ | ~m_p/6 | ghost |
| (1,2) | μ₁₂ | m_p/3 | quark |
| (2,4) | 2μ₁₂ | 2m_p/3 | ghost |
| (3,6) | 3μ₁₂ | m_p | **proton** |

Nodes (apertures) kill everything below (3,6).  The proton
is the **lowest surviving charged mode** — it takes 3× the
fundamental energy to make the sheet ring.

**Why (3,6)?**

- **Spin** = n₁/n₂ = 3/6 = **½** ✓
- **Topology:** gcd(3,6) = 3, so (3,6) is not a single
  strand — it is three phase-separated (1,2) geodesics,
  offset by 120°.  Each strand is a quark.
- **Magnetic moment** ≈ 3 μ_N (from 3× the ring radius of
  the fundamental (1,2) mode).  Measured: 2.793 μ_N (93%).
- **Constituent quark mass** = m_p/3 falls out of the sheet
  sizing — not an input.

**Confinement from filtering:**

This is the central prediction.  The same nodes that select
(3,6) as the surviving mode also **kill (1,2) quarks** when
they try to exist independently:

1. The sheet has nodes tuned to kill all modes below (3,6),
   including (1,2).
2. A high-energy probe decomposes (3,6) → 3 × (1,2) quarks.
3. Each (1,2) quark is a **ghost on this sheet** — it hits
   the node grid and dissipates.
4. Quarks exist briefly as part of the coherent (3,6) pattern
   (the nodes sit at the boundaries between quark domains
   and don't destroy the composite).  Once separated, each
   (1,2) fragment is destroyed by the same nodes.

This is the Q90 "destructive interference" confinement picture,
now with a concrete mechanism: the proton's aperture structure.

**Comparison to Track 5:**

Track 5 checks the quark-model moment arithmetic — it takes
quarks as given and computes their combined moment.

Track 6 explains **why quarks exist** (they are (1,2) modes
on a sheet sized for m_p/3), **why they have mass m_p/3**
(it's the sheet's fundamental), **why the proton has mass
m_p** (it's the 3rd harmonic), and **why quarks are confined**
(the nodes that select the proton kill individual quarks).

Both give ~3 μ_N.  Track 6 provides the physical mechanism.

**Method:**

1. Determine the node geometry that kills all charged modes
   below (3,6).  How many nodes are needed?  What is the
   spacing?

2. Verify that (3,6) survives these nodes (standing-wave
   pattern passes through nodes at zero crossings).

3. Compute the (3,6) moment:
   - Current-loop formula with 3× ring radius
   - Compare to (1,2) on the same sheet
   - Check whether g = 6 (from 3× winding enhancement)
     or some other value

4. Test confinement: compute survival scores for (1,2)
   sub-modes (quarks) on the (3,6)-filtered sheet.
   They should be killed.

5. Compute (3,6) charge: does the WvM polarization
   picture (E always outward) give charge e regardless
   of n₁, or does the scalar n₁ = ±1 selection rule
   suppress it?

6. Check the neutron: can a different spin alignment of
   the three (1,2) strands produce μ_n ≈ −2 μ_N?

**Key questions:**
- What node geometry filters for (3,6)?  How many
  apertures, and at what positions?
- Does the WvM charge mechanism work for n₁ = 3, or
  does the scalar n₁ = ±1 selection rule apply?
- Is the (3,6) moment exactly 3× the (1,2) moment,
  or does the winding structure modify it?
- How fast do separated (1,2) quarks dissipate on the
  node grid?  Does the timescale match hadronic physics?
- Can energy enter the sheet at the (1,2) level (quark
  creation in collisions) and then self-organize into
  (3,6) when enough energy is present?

**Open question — Waveguide cutoff as mode-selection
mechanism:**

The torus tube may act as a waveguide with a frequency
cutoff: modes whose wavelength exceeds the tube
circumference cannot propagate, becoming evanescent.
For a tube-to-ring ratio ε ≈ 1/3, the cutoff sits
near n₂ ≈ 6, which would make (3,6) the lowest
surviving mode — exactly the Track 6 hypothesis.

The original WvM paper supports this picture.  WvM
model the photon's energy as filling a 3D toroidal
**volume**, not just a surface (§4, Fig. 2).  Poynting
vector streamlines trace (1,2) geodesics on nested
toroidal shells, and the radial field profile is
explicitly called "transverse mode structure" — the
same language used for waveguide modes.  Nothing
propagates radially; the cross-section pattern is a
standing wave, while energy flows along the ring.
This is precisely how waveguide cutoff works: the
tube cross-section constrains which transverse
patterns can be sustained.

Our MaSt framework simplified the WvM picture to a
2D surface, which captures topology but drops the
transverse mode structure — and with it, the
waveguide cutoff.  The key unresolved tension:

- **2D view (photon on the sheet):** no tube wall,
  no cutoff.  All integer (p,q) modes are allowed.
  Mode selection requires explicit nodes / apertures.
- **3D view (WvM volume model):** tube cross-section
  enforces a waveguide cutoff.  Mode selection is
  automatic from geometry.  No hand-placed nodes
  needed.

If the 3D waveguide cutoff naturally selects (3,6)
at ε ≈ 1/3, it would be the most economical version
of the Track 6 hypothesis — confinement from geometry
alone, with no separate filtering mechanism.

**Depends on:** Track 4 (spindle/WvM charge model),
Track 5 (quark moment check for comparison).

**Findings:** See [findings.md](findings.md), Track 6.


### Track 7: Ring-circumference mode filter on the proton sheet

**Status:** Framing

**Goal:** Test whether the proton sheet's ring circumference
determines the lowest allowed n₂, and whether this selects
(1,2) or (3,6) as the first charged mode.

**Hypothesis:**

The same ring-circumference filter proposed for the electron
(R46 Track 5) applies to the proton sheet, but with different
tuning.  The proton sheet is ~1000× smaller than the electron
sheet.  If the ring is tuned so that:

- **Case A (proton = (1,2)):** The lowest ring resonance is
  n₂ = 2, giving ε ≈ 0.5 as for the electron.  The proton
  sheet is simply a scaled-down electron sheet.  Quarks would
  need a different explanation.

- **Case B (proton = (3,6)):** The ring is tuned to a higher
  cutoff: the lowest resonance is n₂ = 6 (or equivalently,
  the tube is tuned to the third harmonic with n₁ = 3).  This
  requires ε ≈ 1/3 (tube circumference = 1/3 of ring).  The
  three (1,2) sub-modes that compose (3,6) are quarks; they
  are individually below cutoff and cannot exist as free
  particles (confinement from filtering — see Track 6).

**What distinguishes the two cases:**

| Property | (1,2) proton | (3,6) proton |
|----------|-------------|-------------|
| ε | ~0.5 | ~1/3 |
| Spin | ½ ✓ | ½ ✓ |
| Charge | +1e ✓ | +1e (if n₁=3 still couples) — needs verification |
| Bare magnetic moment | 2 μ_N | 6 μ_N |
| Measured moment | 2.793 μ_N | 2.793 μ_N |
| Anomaly direction | +40% (enhancement) | −53% (suppression) |
| Quark structure | Not natural | Falls out (3 strands at 120°) |
| Confinement | Needs separate mechanism | From ring cutoff |

**Method:**

1. Compute the standing wave spectrum on the proton torus
   as a function of ε, identifying the cutoff n₂.

2. For ε ≈ 1/3: verify that (3,6) is the lowest surviving
   charged mode and that (1,2) is below cutoff.

3. For ε ≈ 0.5: verify that (1,2) survives and check which
   modes are filtered.

4. Compute the magnetic moment in both cases and compare to
   measured 2.793 μ_N.

5. For the (3,6) case: verify that the (1,2) charge mechanism
   (n₁ = ±1 selection rule) extends to n₁ = 3, or whether
   the WvM circular-polarization argument gives charge
   independently of the scalar selection rule.

6. Check whether the (3,6) mode has internal structure
   consistent with three quarks (three phase-separated (1,2)
   strands at 120°), and whether the quark charges (+2/3,
   −1/3) can be extracted from the strand geometry.

**Key question:** Do quarks fall out better from (3,6)?

Yes, in principle.  gcd(3,6) = 3 means the (3,6) mode
decomposes into 3 identical (1,2) strands offset by 120° in
the ring direction.  Each strand carries 1/3 of the total
energy (mass m_p/3 ≈ 313 MeV = constituent quark mass) and
1/3 of the total charge.  The fractional charges (+2/3, −1/3)
would need to come from the relative orientations of the
strands — this is not yet derived but is geometrically
plausible.

If the (1,2) hypothesis is correct, quarks require a separate
explanation (perhaps as excitation sub-modes, Q90).  The model
supports both possibilities for now.  This track aims to
determine which is more consistent with observation.

**Related:** Q103 (anomalous moment), R46 Track 5 (same test
on electron sheet), R47 Track 6 (3,6 confinement hypothesis).

**Depends on:** Track 4 (spindle results), Track 6 (3,6 mode
analysis).


---

## Notes
