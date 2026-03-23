# R26. Three tori — electron, neutrino, proton on T⁶

**Questions:** Q14 (neutrino), Q16 (proton mass), Q18 (α / r-selection), Q32 (energy-geometry)
**Type:** compute/analytical  **Depends on:** R25, R24, R19, R20

## Core hypothesis

**Each stable particle type lives on its own T² subplane of a single
T⁶, at the scale of its Compton wavelength.**

| Domain | Particle | Scale | Dimensions |
|--------|----------|-------|-----------|
| 1 | electron/positron | ~pm (10⁻¹² m) | θ₁, θ₂ |
| 2 | neutrino (3 flavors) | ~μm (10⁻⁶ m) | θ₃, θ₄ |
| 3 | proton/neutron | ~fm (10⁻¹⁵ m) | θ₅, θ₆ |

Total spacetime: 3 + 1 + 6 = **10 dimensions** (matching the
critical dimension of superstring theory, though no string theory
is invoked).

On each T², spin-½ arises from (1,2) winding (the WvM mechanism).
Charge arises from within-plane shear (the R19 mechanism).
Inter-particle interactions arise from cross-plane shear coupling
the three T²s on T⁶.

**What this solves:** R25 showed that the WvM charge-spin linkage
makes uncharged fermions impossible on a single T² — both charge
and spin-½ require tube winding (n₁ ≠ 0).  Giving the neutrino its
own T² evades this: spin-½ comes from winding on the neutrino's tube
(n₃ = 1), while electromagnetic charge remains zero because n₁ = 0
on the electron's tube.

**What this predicts:**
1. Neutrino mass-squared splittings from mode spectrum on the
   neutrino T² (testable against experiment)
2. Three aspect ratios (r_e, r_ν, r_p) constrained by ≥16
   observables via 15 free parameters → over-determined system
3. The fine-structure constant α and particle mass ratios as
   consequences of geometry

## Motivation

Twenty-five studies have mapped the electron as a (1,2) photon on a
sheared T² at pm scale.  The proton and neutrino have resisted clean
modeling on that same T²:

- **Proton (R20):** Modeled as the electron fundamental plus ~1835 m_e
  of uncharged harmonics.  Kinematically correct but descriptive — the
  harmonic spectrum is underdetermined and nothing selects it.
- **Neutrino (R23–R25):** Every mechanism on the electron's T² or a
  shared T³ fails.  On T², mass floor is 245 keV (R20 F14).  On T³,
  modes have the right mass but spin 0 (R25 F4).  The charge-spin
  linkage blocks uncharged fermions on any single T².

Meanwhile, the free parameter r (aspect ratio) remains unconstrained.

This study proposes a different architecture: **separate T² planes**
for each particle, unified in a single T⁶ with cross-shear coupling.

## The three domains

### Domain 1: Electron T² (θ₁, θ₂) — pm scale

The electron is a (1,2) photon on a sheared T² with circumferences
L₁, L₂ at the Compton scale (~2.4 pm).  Established in R2/R19:

| Property | Value | Origin |
|----------|-------|--------|
| Mass | m_e = 0.511 MeV | Path length = λ_C |
| Spin | ½ | (1,2) winding, topological |
| Charge | e | Shear s₁₂ breaks φ-symmetry (R19) |
| g-factor | ≈ 2 | Spin-1 photon → spin-½ fermion |

**Constrained:** s₁₂ = s₁₂(r_e) by α.  One length by m_e.
**Free:** aspect ratio r_e = L₁/L₂.

### Domain 2: Neutrino T² (θ₃, θ₄) — μm scale

The neutrino is a photon on a second T² with circumferences
L₃, L₄ at the μm scale.

| Property | Value | Origin |
|----------|-------|--------|
| Mass | ~5–50 meV | E = ℏc√((n₃/L₃)² + ((n₄−n₃s)/L₄)²) |
| Spin | ½ | Requires q = n₄ = 2 winding on neutrino T² |
| EM charge | 0 | n₁ = 0 on the electron T² (R19) |

**Three flavors from three modes.**  The neutrino T² supports
multiple modes.  A triplet of modes provides three mass eigenstates.
Two mode assignments are candidates:

**Assignment A — mixed spin (clean ratio, spin problem):**
Modes (1,1), (−1,1), (1,2) on the neutrino T².  The mass-squared
splitting ratio simplifies to:

    Δm²₃₁ / Δm²₂₁ = (3 − 2s) / (4s)

This depends **only on shear** — the aspect ratio r cancels.
At s₃₄ ≈ 0.022, the ratio is 33.6 (experimental value, 0.03σ).

**Problem:** Modes (1,1) and (−1,1) have q = 1 → spin-1 by WvM
(L = ℏ/q = ℏ).  Only (1,2) has spin-½.  Neutrinos are spin-½
fermions.  Two spin-1 neutrinos contradict experiment (knot-zoo F1
already flags the (1,1) fermion as "unusual").

**Assignment B — all spin-½ (tunable ratio, sterile neutrino problem):**
Modes (p₁,2), (p₂,2), (p₃,2) with p odd (all spin-½ fermions).
The ratio depends on both s and r.  For (1,2), (3,2), (17,2) at
s₃₄ ≈ −0.09 and r_ν ≈ 1.0, the ratio is 33.6.

**Problem:** Six intermediate spin-½ modes (5,2) through (15,2) lie
between ν₂ and ν₃ — sterile neutrinos that violate N_eff if they
thermalize.

Resolving this tension is the primary objective of Track 1.

**Charge on the neutrino T²:**  The shear s₃₄ (whether 0.022 or
−0.09) is nonzero, so by R19's logic the neutrino T² produces a
gauge charge.  This is NOT electromagnetic charge (which requires
n₁ ≠ 0 on the electron T²).  If the R19 mechanism is universal,
each T² generates its own gauge interaction — the neutrino T²'s
"charge" would be a **weak-sector quantity**, distinct from electric
charge.  This is a structural prediction of the T⁶ model.

**Constrained:** s₃₄ by Δm² ratio (one equation), one length
combination by absolute neutrino mass scale.
**Free:** r_ν = L₃/L₄, overall L₃ scale (pending absolute mass
measurement or cosmological bound).

### Domain 3: Proton T² (θ₅, θ₆) — fm scale

The proton is a (1,2) photon on a third T² with circumferences
L₅, L₆ at the fm scale.  This replaces R20's harmonic model
(electron fundamental + 1835 uncharged harmonics) with a single
standing wave on its own geometry.

| Property | Value | Origin |
|----------|-------|--------|
| Mass | m_p = 938.3 MeV | Path length = λ_C(proton) ≈ 1.32 fm |
| Spin | ½ | (1,2) winding on (θ₅, θ₆) |
| Charge | +e | Shear s₅₆, same α formula as electron |

The proton and electron have the **same charge** (e), so the
shear-charge relationship α(r, s) from R19 applies to both: same
functional form, evaluated at the proton's aspect ratio r_p.

The proton Compton wavelength is 1.32 fm.  The measured charge
radius is 0.88 fm — same order.  If the charge radius scales with
the major radius R = L₅/(2π), this emerges naturally.

**Neutron:** Two (1,2) fundamentals on the proton T² with opposite
charge orientation, as in R20.  Total charge = +e + (−e) = 0.  Mass
slightly above the proton (the pairing adds a small energy).  Beta
decay: one fundamental escapes — how it becomes an electron on the
electron T² requires energy transfer between subplanes (Track 2).

**Constrained:** s₅₆ by α (same equation as electron), one length
by m_p.
**Free:** r_p = L₅/L₆.

## The unified T⁶

The three T²s are subplanes of a single compact space T⁶ with
six compact dimensions.

### Shear parameters

A general T⁶ lattice has C(6,2) = 15 shear parameters:

| Type | Count | Parameters | Physical role |
|------|-------|------------|---------------|
| Within-plane | 3 | s₁₂, s₃₄, s₅₆ | Gauge charge on each T² |
| Electron–neutrino | 4 | s₁₃, s₁₄, s₂₃, s₂₄ | PMNS mixing, ν production |
| Electron–proton | 4 | s₁₅, s₁₆, s₂₅, s₂₆ | Weak interaction? |
| Neutrino–proton | 4 | s₃₅, s₃₆, s₄₅, s₄₆ | ν–nucleon coupling |

### Parameter counting

**Free continuous parameters** (after within-plane constraints):

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
| CKM mixing angles (if quarks are proton-T² modes) | 4 |
| Proton charge radius | 1 |
| Neutron–proton mass difference | 1 |
| Neutrino absolute mass scale (cosmology) | 1 |
| Muon/tau masses (if excitations on electron or proton T²) | 2 |
| **Total** | **≥ 16** |

**16 observables vs 15 parameters → over-determined by at least 1.**

If even one observable cannot be accommodated, the model fails —
it is falsifiable.  If all fit, the geometry is essentially unique.
However, some observables may be degenerate — only explicit
computation can distinguish true over-determination from
apparent counting.

## Tracks

### Track 1 — The neutrino torus

**Goal:** Determine the geometry of a T² that produces three
neutrino mass eigenstates with correct splittings and spin ½.

This is the highest-risk track.  The spin-mass tension identified
above has no known resolution yet.  The track is organized as
sub-tracks to explore each candidate path:

**Track 1a — Verify the three-mode formula.**

1. Compute the full mode spectrum on the neutrino T² for both
   Assignment A (s ≈ 0.022) and Assignment B (s ≈ −0.09, r ≈ 1)
2. Verify the mass-squared ratio algebraically and numerically
3. Catalog all modes below 1 eV — identify sterile neutrinos
4. Compare predicted Σm with cosmological bound (120 meV)

**Track 1b — All-spin-½ search.**

Systematically search for mode triplets (p₁, 2), (p₂, 2), (p₃, 2)
with all pᵢ odd that reproduce Δm²₃₁/Δm²₂₁ = 33.6 ± 0.9 for
some (s₃₄, r_ν).

1. For each candidate triplet (p₁, p₂, p₃), solve for the (s, r)
   curve that gives ratio = 33.6.  Does a physical solution exist?
2. Count intermediate spin-½ modes between ν₂ and ν₃.
3. Assess N_eff constraints — can intermediate modes avoid
   thermalizing?  (Need a coupling selection rule.)
4. If no clean solution exists: quantify the best achievable match
   and its cost (sterile neutrino count, N_eff tension).

**Track 1c — Spin resolution for Assignment A.**

If 1b fails to produce a clean all-spin-½ solution:

1. Investigate whether cross-plane coupling on T⁶ modifies the
   effective spin of (1,1) modes.  The mixing amplitude scales
   as cross-shear × (energy ratio) — compute whether this can
   convert spin-1 to effective spin-½.
2. Re-examine the WvM spin formula L = ℏ/q for the q = 1 case.
   The knot-zoo noted this "may need refinement."  Does the
   embedded-torus geometry (finite a/R) modify the spin of (1,1)?
3. If neither works: can the neutrino be a spin-1 fermion?
   Is this experimentally excluded, or merely conventional?
   (Neutrino helicity measurements constrain this.)

**Possible outcomes:**
- 1b succeeds → three all-spin-½ modes with acceptable sterile
  spectrum → proceed to Tracks 2–4
- 1c succeeds → Assignment A is viable with modified spin → proceed
- Both fail → the neutrino T² model fails at the same spin gate
  as T³, and the neutrino remains an open problem

### Track 2 — The proton torus

**Goal:** Determine the geometry of a T² that produces a single
(1,2) standing wave at the proton mass.

Steps:
1. Apply R19's α formula to the proton T².  Same charge → same
   α(r, s) → solve for s₅₆(r_p).  Is the solution space the same
   one-parameter family as the electron?
2. Compute the proton charge radius from T² geometry.  On the
   electron's T², the charge radius ~ R (major radius).  Does
   this scaling give 0.841 fm for reasonable r_p?
3. Model the neutron as two opposite-charge (1,2) fundamentals.
   Compute the mass difference m_n − m_p = 1.293 MeV.
4. Address beta decay: n → p + e⁻ + ν̄.  One fundamental escapes
   the proton T² with energy ~470 MeV.  How does it become a
   0.511 MeV electron on the electron T²?  Where does the excess
   energy go?  (In R20, it redistributed among harmonics.  Here
   it must be radiated or absorbed by the T⁶ geometry.)
5. Muon and tau: excited states on which T²?  Higher (p,2) modes
   on the electron T² (giving m_μ/m_e from winding ratio)?
   Or modes on the proton T²?

### Track 3 — Parameter census

**Goal:** Produce a single table of every parameter across all
three domains, its constraint source, and its status (fixed/free).

| Parameter | Domain | Fixed by | Value | Status |
|-----------|--------|----------|-------|--------|
| s₁₂ | electron | α | s₁₂(r_e) | constrained (given r_e) |
| r_e | electron | ? | ? | **free** |
| s₃₄ | neutrino | Δm² ratio | depends on assignment | constrained |
| r_ν | neutrino | ? | ? | **free** |
| s₅₆ | proton | α(r_p) | s₅₆(r_p) | constrained (given r_p) |
| r_p | proton | ? | ? | **free** |
| ... | cross-shears | ... | ... | ... |

Identify the minimum number of genuinely free parameters.  Count
independent observables not used as inputs.  Determine if the
system is under-, exactly-, or over-determined.

### Track 4 — Unification on T⁶

**Goal:** Embed the three T²s in a single T⁶ and determine
whether the combined geometry is fully constrained.

Steps:
1. Write the general T⁶ metric and mode spectrum as a function of
   all 15 shears and 6 circumferences.  Verify that the three T²
   spectra emerge in the zero-cross-shear limit.
2. Map the 12 cross-shears to physical observables:
   - s₁₃, s₁₄, s₂₃, s₂₄ → PMNS mixing
   - s₁₅, s₁₆, s₂₅, s₂₆ → electron–proton coupling
   - s₃₅, s₃₆, s₄₅, s₄₆ → neutrino–proton coupling
3. Determine if PMNS + CKM jointly constrain enough cross-shears
   to fix r_e, r_ν, r_p.
4. Check for T⁶ geometric consistency conditions (modular
   invariance, lattice self-consistency, topological constraints)
   that may reduce the free parameter count.
5. If over-determined: solve and compute predictions.
6. If under-determined: identify which observable would close it.

## Risk assessment

- **Track 1:** **High risk.**  The spin-mass tension has no known
  resolution.  The most likely outcome is that one sub-track
  partially succeeds with caveats (sterile neutrinos or modified
  spin).  A full failure is possible — it would close the T⁶
  neutrino path.

- **Track 2:** Medium risk.  The single-fundamental proton is clean,
  but beta decay becomes harder — a 470 MeV photon must convert to
  a 0.511 MeV electron.

- **Track 3:** Low risk.  Bookkeeping, but essential.

- **Track 4:** High risk, high reward.  Requires Tracks 1–3 to
  succeed.  If it works, the model becomes fully predictive.

## Relation to prior studies

| Study | Model | Status | R26 relationship |
|-------|-------|--------|-----------------|
| R20 | Proton = electron + harmonics on T² | Descriptive | Track 2 replaces with single fundamental |
| R23 | Neutrino from beating on T² | Failed | Superseded by Track 1 |
| R24 | Neutrino on T³ | Kinematics ✓, spin ✗ | Track 1 inherits mass-splitting approach |
| R25 | Spin analysis of T³ | Charge-spin linkage | Evaded: spin from separate T² |
| R19 | Charge from shear on T² | α(r,s) formula | Applied to all three T²s |
| R14 | Universal T³ for all particles | Linking ruled out | Replaced by T⁶ with three T² subplanes |

## What this study does NOT address

- **Why six compact dimensions?**  The number 6 is motivated by
  three particles × two dimensions each.  The match with string
  theory's critical dimension (10 total) is noted but unexplained.

- **Quarks and confinement.**  If quarks are localized modes on
  the proton T², their fractional charges and confinement remain
  open.

- **The scale hierarchy.**  Why fm ≪ pm ≪ μm (equivalently, why
  m_p ≫ m_e ≫ m_ν) is not explained.  The hierarchy is input.

- **Gravity at sub-mm scales.**  L₃, L₄ ~ μm would modify gravity
  below ~250 μm if gravity propagates in all compact dimensions.
  Current bounds (< 50 μm) may require a gravity-confining mechanism.
