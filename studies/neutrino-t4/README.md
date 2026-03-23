# R26. Three tori — electron, neutrino, proton on T⁶

**Questions:** Q14 (neutrino), Q16 (proton mass), Q18 (α / r-selection), Q32 (energy-geometry)
**Type:** compute/analytical  **Depends on:** R25, R24, R19, R20

## Motivation

Twenty-five studies have mapped the electron as a (1,2) photon on a
sheared T² at pm scale.  The proton and neutron can be modeled on this same T2
only with great coersion.  The neutrino has resisted all efforts at
clean modeling on that same T²:

- **Proton (R20):** Modeled as the electron fundamental plus ~1835 m_e
  of uncharged harmonics.  Kinematically correct but descriptive — the
  harmonic spectrum is underdetermined and nothing selects it.
- **Neutrino (R23–R25):** Every mechanism on the electron's T² or T³
  fails.  On T², the mass floor is 245 keV (R20 F14).  On T³, modes
  have the right mass but spin 0 (R25 F4).  The charge-spin linkage
  blocks uncharged fermions on any single T².

Meanwhile, the free parameter r (aspect ratio of the electron's T²)
remains unconstrained through all studies.  The model is descriptive,
not predictive.

This study proposes a different architecture: **each stable particle
lives on its own T²**, at a scale set by its Compton wavelength.
The three T²s are not independent — they are subplanes of a single
T⁶, coupled by cross-shear.  The coupling provides interaction
channels (beta decay, neutrino production) and the combined geometry
may over-determine the free parameters.

## The three domains

### Domain 1: Electron T² (θ₁, θ₂) — pm scale

The electron is a (1,2) photon on a sheared T² with circumferences
L₁, L₂ at the Compton scale (~2.4 pm).  This is the established
model from R2/R19:

| Property | Value | Origin |
|----------|-------|--------|
| Mass | m_e = 0.511 MeV | E = ℏc/L, path length = λ_C |
| Spin | ½ | (1,2) winding ratio, topological |
| Charge | e | Shear s₁₂ ≈ 0.165 breaks φ-symmetry (R19) |
| g-factor | ≈ 2 | Spin-1 photon → spin-½ fermion |

**Constrained:** s₁₂ by α (one equation), one length by m_e.
**Free:** aspect ratio r_e = L₁/L₂.

### Domain 2: Neutrino T² (θ₃, θ₄) — μm scale

The neutrino is a (1,2) photon on a second T² with circumferences
L₃, L₄ at the μm scale.  This solves the problem that killed T³:
two large dimensions provide a (1,2) winding plane, giving spin ½
through the same WvM mechanism as the electron.

| Property | Value | Origin |
|----------|-------|--------|
| Mass | ~5–50 meV | E = ℏc √((1/L₃)² + (2/L₄)²) |
| Spin | ½ | (1,2) winding on (θ₃, θ₄), same mechanism as electron |
| Charge | 0 | n₁ = 0: no winding on electron's tube (R19 F30) |

**Three flavors from three modes.**  On a T² with small shear s,
the three lightest modes are (1,1), (−1,1), and (1,2), with energies:

    f(1,1)  = 1 + (1−s)²/r²
    f(−1,1) = 1 + (1+s)²/r²
    f(1,2)  = 1 + (2−s)²/r²

The mass-squared splitting ratio simplifies exactly:

    Δm²₃₁ / Δm²₂₁ = (3 − 2s) / (4s)

This depends **only on the shear** — the aspect ratio r cancels
completely.  The experimental value (33.6 ± 0.9) is reproduced at:

    s₃₄ = 3 / (4 × 33.6 + 2) ≈ 0.022

A nearly unsheared torus.  The shear is small enough that any
"charge" generated on the neutrino plane (if the R19 mechanism
applies there) would be proportional to sin(2π × 0.022) ≈ 0.14 —
but this may not be electromagnetic charge at all, since the
projection from μm-scale compact dimensions into 3D differs
qualitatively from the pm-scale projection.  Electric charge
neutrality is protected by n₁ = 0 regardless.

**Spin question:** The (1,1) and (−1,1) modes have winding ratio
1:1, giving spin 1 by the standard WvM mechanism.  Only (1,2) has
spin ½.  Whether the physical spin of neutrino flavors ν₁, ν₂, ν₃
matches these modes' geometric spin — or whether cross-plane
coupling on T⁶ modifies the effective spin — is a key question for
Track 1.

**Constrained:** s₃₄ by Δm² ratio (one equation), one length
combination by absolute neutrino mass scale.
**Free:** r_ν = L₃/L₄, overall L₃ scale (pending absolute mass
measurement or cosmological bound).

### Domain 3: Proton T² (θ₅, θ₆) — fm scale

The proton is a (1,2) photon on a third T² with circumferences
L₅, L₆ at the fm scale.  This replaces R20's harmonic model
(electron fundamental + 1835 uncharged harmonics) with a single
standing wave on its own geometry — directly analogous to the
electron, just smaller.

| Property | Value | Origin |
|----------|-------|--------|
| Mass | m_p = 938.3 MeV | E = ℏc/L, path length = λ_C(proton) ≈ 1.32 fm |
| Spin | ½ | (1,2) winding on (θ₅, θ₆) |
| Charge | +e | Shear s₅₆, same α formula as electron |

The proton and electron have the **same charge** (e), so the
shear-charge relationship α(r, s) from R19 applies to both.  If
the formula is universal, then s₅₆ = s₁₂(r_p) — the same functional
relationship, but evaluated at the proton's aspect ratio r_p.

The proton Compton wavelength is 1.32 fm.  The measured proton
charge radius is 0.88 fm — the same order of magnitude.  On the
electron's T², the charge radius is related to the major radius R,
which is of order the Compton wavelength.  If this scaling holds for
the proton, the charge radius emerges naturally.

**Neutron:** Two (1,2) fundamentals on the proton T² with opposite
charge orientation, as in R20.  Total charge = +e + (−e) = 0.
Mass slightly above the proton (the pairing adds a small energy).
Beta decay: one fundamental escapes as a proton-scale photon that
then... this raises a question about how the neutron-decay electron
emerges.  Track 2 must address this.

**Constrained:** s₅₆ by α (same equation as electron), one length
by m_p.
**Free:** r_p = L₅/L₆.

## The unified T⁶

The three T²s are subplanes of a single compact space
T⁶ = S¹ × S¹ × S¹ × S¹ × S¹ × S¹ with six compact dimensions.

Total spacetime: 3 (spatial) + 1 (time) + 6 (compact) = **10 dimensions**.

This is exactly the critical dimension of superstring theory.  The
model does not invoke string theory, but the coincidence is notable.

### Scale hierarchy

| Domain | Dimensions | Scale | Particle |
|--------|-----------|-------|----------|
| Proton T² | θ₅, θ₆ | ~fm (10⁻¹⁵ m) | proton, neutron |
| Electron T² | θ₁, θ₂ | ~pm (10⁻¹² m) | electron, positron |
| Neutrino T² | θ₃, θ₄ | ~μm (10⁻⁶ m) | ν_e, ν_μ, ν_τ |

Three scales spanning 9 orders of magnitude: fm → pm → μm.
Each scale is set by the corresponding particle's Compton wavelength.

### Shear parameters

A general T⁶ lattice has C(6,2) = 15 shear parameters:

| Type | Count | Parameters | Role |
|------|-------|------------|------|
| Within-plane | 3 | s₁₂, s₃₄, s₅₆ | Charge on each T² |
| Electron–neutrino cross | 4 | s₁₃, s₁₄, s₂₃, s₂₄ | PMNS mixing, ν production |
| Electron–proton cross | 4 | s₁₅, s₁₆, s₂₅, s₂₆ | Weak interaction? |
| Neutrino–proton cross | 4 | s₃₅, s₃₆, s₄₅, s₄₆ | ν–nucleon coupling |

### Parameter counting

**Free continuous parameters** (after using within-plane constraints):

| Parameter | Source | Count |
|-----------|--------|-------|
| r_e | Electron aspect ratio | 1 |
| r_ν | Neutrino aspect ratio | 1 |
| r_p | Proton aspect ratio | 1 |
| 12 cross-shears | Inter-plane coupling | 12 |
| **Total** | | **15** |

(Within-plane shears s₁₂, s₃₄, s₅₆ are determined by α and the
neutrino splitting ratio.  Absolute scales L₁, L₃, L₅ are set by
m_e, m_ν, m_p.)

**Available observables:**

| Observable | Count |
|------------|-------|
| α (fine structure constant) | 1 |
| m_p/m_e (mass ratio) | 1 |
| Neutrino Δm² ratio | 1 |
| PMNS mixing angles (θ₁₂, θ₂₃, θ₁₃, δ_CP) | 4 |
| CKM mixing angles (if quarks are modes on proton T²) | 4 |
| Proton charge radius | 1 |
| Neutron–proton mass difference | 1 |
| Neutrino absolute mass scale (from cosmology) | 1 |
| Muon/tau masses (if they are modes on the proton or electron T²) | 2 |
| **Total** | **≥ 16** |

**16 observables vs 15 parameters → over-determined by at least 1.**

If even one observable cannot be accommodated, the model fails —
it is falsifiable.  If all 16+ fit, the geometry is essentially
unique.

## Tracks

### Track 1 — The neutrino torus

**Goal:** Determine the geometry of a T² that produces three
neutrino-like modes with the correct mass splittings and (if
possible) spin ½.

Starting point: the three-mode result.  On a T² with shear s and
aspect ratio r, the modes (1,1), (−1,1), and (1,2) have mass-squared
splitting ratio:

    R = (3 − 2s) / (4s)

This is independent of r.  At s ≈ 0.022, R = 33.6 (experimental
value).  The absolute mass scale sets the T² circumferences at
~μm.

Steps:
1. Verify the three-mode frequency result computationally (not just
   algebraically)
2. Compute the full mode spectrum on the neutrino T² and check for
   unwanted light modes
3. Determine the neutrino T²'s aspect ratio r_ν from additional
   constraints (absolute mass scale, mixing angles)
4. Address the spin question: (1,1) and (−1,1) have spin 1 by WvM.
   Investigate whether cross-plane coupling on T⁶ can modify the
   effective spin, or whether a different mode triplet (all spin ½)
   can reproduce the 33.6 ratio
5. Compute predicted masses and compare with cosmological bounds
   (Σm < 120 meV) and upcoming experimental sensitivity (KATRIN,
   Project 8)

**Key question:** Is s₃₄ ≈ 0.022 compatible with neutrino charge
neutrality?  Electric charge is protected by n₁ = 0 on T⁶, but does
the neutrino plane's shear produce a different kind of gauge charge?

### Track 2 — The proton torus

**Goal:** Determine the geometry of a T² that produces a single
(1,2) standing wave at the proton mass.

The proton as a single (1,2) photon on its own T²:
- Compton wavelength: λ_C = h/(m_p c) = 1.32 fm → L₅, L₆ ~ fm
- Charge: +e → s₅₆ determined by α(r_p, s₅₆) from R19
- Spin: ½ from (1,2) winding

Steps:
1. Apply R19's α formula to the proton T².  Since the proton has the
   same charge as the electron, the same functional relationship
   α(r, s) holds.  Solve for s₅₆(r_p).  Is the solution space the
   same one-parameter family as the electron, or does the fm scale
   introduce new constraints?
2. Compute the proton charge radius from the T² geometry and compare
   with experiment (0.841 fm).  On the electron's T², the charge
   radius ~ R (major radius).  Does this scaling give the right
   proton charge radius for reasonable r_p?
3. Model the neutron as two opposite-charge (1,2) fundamentals on
   the proton T².  Compute the mass difference m_n − m_p = 1.293 MeV.
   What sets the pairing energy?
4. Address beta decay: n → p + e⁻ + ν̄.  One (1,2) fundamental
   escapes the proton T².  How does it become an electron on the
   electron T²?  This requires energy transfer between T² subplanes
   — the cross-shear coupling from Track 4.  The escaping photon
   has energy ~m_p c²/2 ~ 470 MeV, far more than m_e = 0.511 MeV.
   Where does the excess energy go?  (In R20, it was redistributed
   among harmonics.  In this model, it must be radiated or absorbed
   by the geometry.)
5. The muon (105.7 MeV) and tau (1777 MeV): are they excited states
   on the proton T²?  Higher harmonics?  Or do they live on the
   electron T² as in R20?

### Track 3 — Parameter census of the three domains

**Goal:** Catalog every constrained and free parameter across all
three T² subplanes.

For each domain, determine:
1. Which parameters are fixed by known physics (α, particle masses,
   measured radii)
2. Which are fixed by internal consistency (e.g., the same α formula
   must work on both the electron and proton T²s)
3. Which remain genuinely free
4. Which observables are predicted (not used as inputs)

Produce a single table:

| Parameter | Domain | Fixed by | Value | Status |
|-----------|--------|----------|-------|--------|
| s₁₂ | electron | α | 0.165 | constrained |
| r_e | electron | ? | ? | **free** |
| s₃₄ | neutrino | Δm² ratio | 0.022 | constrained |
| r_ν | neutrino | ? | ? | **free** |
| s₅₆ | proton | α(r_p) | f(r_p) | constrained (given r_p) |
| r_p | proton | ? | ? | **free** |
| ... | | | | |

Identify the minimum number of free parameters.  Count the
independent observables not used as inputs.  Determine if the
system is under-, exactly-, or over-determined.

### Track 4 — Unification on T⁶

**Goal:** Embed the three T²s in a single T⁶ with 12 cross-shear
parameters.  Determine whether the combined geometry is fully
constrained.

Steps:
1. Write the general T⁶ metric and mode spectrum as a function of
   all 15 shear parameters and 6 circumferences.  Verify that the
   three T² spectra emerge in the limit of zero cross-shear.
2. Map the 12 cross-shear parameters to physical observables:
   - s₁₃, s₁₄, s₂₃, s₂₄ → PMNS mixing (electron–neutrino coupling)
   - s₁₅, s₁₆, s₂₅, s₂₆ → electron–proton coupling (weak interaction?)
   - s₃₅, s₃₆, s₄₅, s₄₆ → neutrino–proton coupling
3. Determine if the PMNS and CKM mixing matrices jointly constrain
   enough cross-shears to fix the three free aspect ratios
   (r_e, r_ν, r_p).
4. Check for geometric consistency conditions on T⁶ that are not
   present on individual T²s.  Modular invariance, lattice
   self-consistency, or topological constraints may impose relations
   among the 15 shear parameters that further reduce the free
   parameter count.
5. If the system is over-determined: solve for all parameters and
   compute predictions (m_e, m_p, α, neutrino masses, mixing
   angles).  Every one that matches experiment without being used
   as input is a genuine prediction.
6. If the system is under-determined: identify which additional
   observable would close it.

**Key question:** Does 16 observables vs 15 parameters actually
over-determine the system, or are some observables redundant?  The
counting is suggestive but the actual constraint equations may have
degeneracies.  Only an explicit computation can answer this.

## Risk assessment

- **Track 1 (neutrino torus):** Low–medium risk.  The mass-squared
  ratio result is algebraically clean; computation is verification.
  Main risk: the spin question — if all three modes must be spin ½
  and the (1,1)/(−1,1) modes cannot acquire effective spin ½ through
  cross-plane coupling, the three-mode picture fails.

- **Track 2 (proton torus):** Medium risk.  The single-fundamental
  proton is conceptually simple, but beta decay becomes harder to
  explain — a 470 MeV photon must convert to a 0.511 MeV electron.
  The energy transfer mechanism is unclear.

- **Track 3 (parameter census):** Low risk.  This is bookkeeping —
  but essential bookkeeping.  Forces precise statements about what
  is known vs assumed.

- **Track 4 (T⁶ unification):** High risk, high reward.  Requires
  Tracks 1–3 to succeed.  The PMNS/CKM mapping is uncharted
  territory in this framework.  If it works, the model becomes
  fully predictive.  If it fails, it identifies exactly which
  structural element is missing.

## Relation to prior studies

| Study | Model | Status | R26 relationship |
|-------|-------|--------|-----------------|
| R20 | Proton = electron + harmonics on T² | Descriptive, harmonic spectrum free | Track 2 replaces with single fundamental |
| R23 | Neutrino from beating on T² | Failed (not selective) | Superseded by Track 1 |
| R24 | Neutrino on T³ | Kinematics ✓, spin ✗ | Track 1 inherits mass-squared formula |
| R25 | Spin analysis of T³ | Charge-spin linkage blocks neutrino | Evaded: spin from separate T² plane |
| R19 | Charge from shear on T² | α(r,s) formula, s₁₃ = 0 | Applied to all three T²s |
| R14 | Universal T³ for all particles | Linking ruled out, quarks open | Replaced by T⁶ with three T² subplanes |

## What this study does NOT address

- **Why six compact dimensions?**  The number 6 is motivated by
  requiring three particles × two dimensions each.  It happens to
  match the string theory critical dimension (10 total), but no
  deeper explanation is given.

- **Quarks and confinement.**  If quarks are localized modes on
  the proton T², their fractional charges and confinement remain
  open.  T⁶ provides geometric room but this study does not
  address quarks.

- **The scale hierarchy.**  Why fm ≪ pm ≪ μm (equivalently, why
  m_p ≫ m_e ≫ m_ν) is not explained.  The hierarchy is input.

- **Gravity at sub-mm scales.**  L₃, L₄ ~ μm would modify gravity
  below ~250 μm if gravity propagates in all compact dimensions.
  Current bounds (< 50 μm) may require a gravity-confining mechanism.
