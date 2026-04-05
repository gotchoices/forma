# R49: Neutrino sheet — filtering, oscillation, and mode spectrum

**Status:** Framing
**Questions:** Q85, Q94, Q99
**Type:** compute / theoretical
**Depends on:** R46, R47

---

## Motivation

R46 and R47 established that the electron and proton sheets have
filtering mechanisms (waveguide cutoff, slots) that select the
observed modes and kill ghosts.  The neutrino sheet (Ma_ν) is
the remaining gap before a full particle search with improved
mode selection rules.

The neutrino is different from the electron and proton in
several important ways:

1. **No EM charge.**  The neutrino has no winding on the
   electron or proton sheets, so the EM charge mechanism
   (CP synchronization on Ma_e/Ma_p, R48 F1) does not
   apply.  Filtering mechanisms derived from EM charge
   (slots that break charge symmetry) may not operate on
   this sheet.

   Why the neutrino is neutral is itself an open question
   with at least two candidate explanations:

   **(a) Sheet too large (Q102).**  The neutrino sheet has
   circumferences of ~10²⁹ Planck lengths.  A 2π phase
   winding spread over that many cells produces a gradient
   of ~10⁻²⁸ rad/cell — possibly below the lattice's
   resolution limit.  The ambient 3D lattice cannot detect
   the winding, so no topological defect forms and no charge
   appears.  The neutrino has mass (the standing wave
   circulates) but the phase twist is too gentle to couple.

   **(b) Zero or near-zero shear.**  On Ma_e and Ma_p,
   shear s breaks the symmetry between clockwise and
   counter-clockwise circulation, producing charge via the
   α(ε, s) impedance formula.  If the neutrino sheet has
   s₃₄ = 0 (or negligibly small), there is no symmetry
   breaking and no net circulation → no charge.  Shear
   serves a dual purpose on the charged sheets: it sets
   the impedance coupling (α) AND determines the
   matter/antimatter preference.  A sheet with zero shear
   would have neither.

   These are not mutually exclusive — both could contribute.
   Whether the neutrino sheet has shear is testable in
   principle: if it does, there should be an asymmetry
   between neutrinos and antineutrinos in production and
   interaction rates.

2. **Unknown sheet geometry.**  The neutrino's aspect ratio
   ε_ν is not known.  It could be small (tube ≪ ring, like
   the electron at ε_e ≈ 0.5) or large (tube ≫ ring).
   The sheet scale is set by the neutrino mass (~meV), which
   gives a Compton wavelength ƛ_ν = ℏ/(m_ν c) ≈ 6.6 μm
   for m_ν ~ 30 meV.  The sheet circumferences are at this
   scale — μm, vastly larger than Ma_e (~pm) or Ma_p (~fm).

3. **Filtering vs storage tension.**  A smaller tube or
   ring eliminates low-frequency modes (fewer ghosts), but
   the neutrino's dense mode spectrum is hypothesized to be
   a **feature** — the substrate for information storage
   (Q85, R35).  If filtering is too aggressive, the storage
   hypothesis loses its mode ladder.  If filtering is too
   permissive, we cannot explain why only three mass
   eigenstates are observed.

4. **Oscillation.**  Neutrino oscillation is the strongest
   experimental handle.  Three mass eigenstates with
   Δm²₃₁/Δm²₂₁ ≈ 33.6 were observed in earlier modeling.  In the MaSt framework
   these should correspond to three modes on Ma_ν.  But the
   physical **mechanism** of oscillation — phase evolution,
   energy redistribution, or something else — has not been
   modeled.

5. **The (3,6) parallel.**  The proton (R47 Track 7) is a
   composite of three (1,2) strands.  Are the neutrino's
   three mass eigenstates similarly composite, or are they
   three independent modes?


## What we know (experimental)

| Observable | Value | Source |
|------------|-------|--------|
| Δm²₂₁ | 7.53 × 10⁻⁵ eV² | Solar + reactor |
| Δm²₃₁ | ≈ 2.53 × 10⁻³ eV² | Atmospheric |
| Δm²₃₁/Δm²₂₁ | 33.6 ± 0.9 | Combined |
| Mass ordering | Normal (preferred) | NOvA, T2K, SK |
| θ₁₂ (solar) | 33.4° | Solar + KamLAND |
| θ₂₃ (atmospheric) | ~49° | Atmospheric + LBL |
| θ₁₃ (reactor) | 8.6° | Daya Bay, RENO |
| Σm (cosmology) | < 120 meV | Planck (95% CL) |
| Spin | ½ | Established |
| EM charge | 0 | Established |
| Weak charge | Nonzero | β-decay coupling |
| Number of light species | 3 (N_eff ≈ 3) | BBN + CMB |


## What we don't know

- **ε_ν** — the aspect ratio of the neutrino torus.  Could
  be ≪ 1, ~ 1, or ≫ 1.  No measurement constrains it
  directly.  The filtering landscape depends strongly on ε_ν.

- **Mode assignment** — which (n₃, n₄) modes correspond to
  the three mass eigenstates.  R24 and R26 proposed
  candidates; this study should derive constraints from
  first principles rather than assuming an assignment.

- **Shear s₃₄** — the within-plane shear on Ma_ν.  On the
  charged sheets, shear does double duty: it sets α (the
  impedance coupling) and breaks the matter/antimatter
  symmetry (preferred circulation direction).  On Ma_ν,
  shear affects mass splittings and may or may not be
  constrained by the Δm² ratio.  It is also possible that
  s₃₄ is zero or near-zero, which would be a second
  explanation for neutrino neutrality (in addition to the
  sheet-size argument of Q102).  The experimental question
  is whether neutrinos show any matter/antimatter asymmetry
  — if not, s₃₄ ≈ 0 is favored.

- **Spin mechanism at arbitrary ε** — the electron's spin-½
  comes from (1,2) winding with n₁ = 1.  On Ma_ν, the
  neutrino's spin-½ requires analogous winding (n₃ = odd).
  But the effective spin depends on ε_ν (R26 F19–F23 showed
  spin corrections at finite ε).  At what ε_ν values can
  modes maintain spin ½?

- **Whether Ma_ν has a "charge" analogue** — the neutrino has
  no EM charge, but it couples weakly.  Does the same CP
  synchronization mechanism on Ma_ν produce a "weak charge"?
  R26 F27 found that only (1,2) carries nonzero charge
  transport on a torus; higher (p,2) modes give zero.

- **Oscillation mechanism** — phase evolution (standard) vs
  energy redistribution (counting hypothesis) vs hybrid.


## Key questions

### Q1. What constraints does ε_ν face?

At different ε_ν values, different physics dominates:
- **Small ε_ν (≪ 1):** tube is much smaller than ring.
  Waveguide cutoff is aggressive — many modes killed.
  Few modes survive → less storage, but cleaner spectrum.
- **ε_ν ~ 1:** tube ≈ ring.  Moderate filtering.
- **Large ε_ν (≫ 1):** tube much larger than ring.
  Waveguide is permissive — almost all modes propagate.
  Dense mode spectrum → rich storage, but why only 3
  mass eigenstates observed?

Constraints on ε_ν might come from:
- Spin: requiring spin-½ for the mass eigenstates
- Σm < 120 meV: absolute mass scale
- N_eff = 3: no extra light species (limits sterile modes
  that couple to weak interactions)
- The Δm² ratio itself (does it constrain ε_ν, s₃₄, or
  both?)

### Q2. Does the neutrino sheet need filtering?

On Ma_e, the (1,1) ghost is a problem: it would be a
lighter charged particle — unobserved.  On Ma_ν, extra
modes have no EM charge.  They are invisible to EM
experiments.  Are they:
- **(a)** Real modes that form the dense storage spectrum?
- **(b)** Ghost modes that need a filter?
- **(c)** Physical modes that exist but are not populated
  by standard production mechanisms (β-decay)?

The answer may depend on ε_ν.  If ε_ν is large, most modes
propagate and the "filter" is not the geometry but the
**production mechanism** — β-decay populates only modes
that couple to Ma_e via cross-shear.

### Q3. What is the oscillation mechanism?

Standard model: flavor states are superpositions of mass
eigenstates.  Different masses → different phase velocities
→ flavor content oscillates.  P ∝ sin²(Δm²L/(4E)).

MaSt adds a new possibility: the neutrino's Compton window
(sheet scale ~ μm, potentially wide resonance) might allow
energy exchange with the environment.  If the neutrino
picks up or sheds small amounts of energy through this
window, the mode occupation could change — not just the
phase, but the actual energy distribution.

If so, oscillation is a physical process (energy
redistribution among modes on Ma_ν) rather than pure
quantum phase interference.  The neutrino's mass would
literally change between measurements.

Key constraint: SNO confirmed total neutrino flux is
conserved in solar oscillation.  Any energy-exchange model
must close the energy budget.  If energy redistributes
internally (between modes on Ma_ν, not radiated to S),
the external energy is unchanged.

### Q4. Do neutrinos emit at the transition frequencies?

Standard oscillation is unitary — no energy emitted.
If MaSt oscillation involves energy redistribution, there
might be emission at the mass-splitting frequencies.  But
if the energy stays on Ma_ν (internal shuffling, not
radiated to 3D space), no external photon is produced.

### Q5. Are the three mass eigenstates unique?

On a torus, many mode triplets can match Δm²₃₁/Δm²₂₁ =
33.6 (R24 found several).  What selects the actual three?
Possibilities:
- A filter selects specific survivors
- Production dynamics (β-decay) populates only certain modes
- The three modes have a structural relationship (composite,
  symmetry, topological constraint)

### Q6. Connection to (3,6) composites

The proton's (3,6) = three coherent (1,2) strands.
The neutrino has three mass eigenstates.  Structural
parallels?  Key difference: the proton's strands are
phase-locked (confinement); the neutrino's modes are
free-running (oscillation).

### Q7. The counting hypothesis

Q85 and R35 proposed that modes on Ma_ν accumulate
sub-threshold energy, functioning as a counter.  If the
oscillation modes are counters:
- Each mode accumulates energy from the environment
- The dominant mode determines the neutrino's "flavor"
- Transitions occur when one counter passes another
- The counting rate is set by the mode's frequency

This would unify oscillation and information storage as
the same physics.

### Q8. Shear, antimatter, and energy storage

On the charged sheets (Ma_e, Ma_p), shear determines the
matter/antimatter preference — one circulation direction
is energetically favored.  This is why positrons are rare:
the embedding chirality makes electron-direction winding
cheaper than positron-direction winding.

If the neutrino sheet has zero or near-zero shear, there
would be no such preference.  Neutrinos and antineutrinos
would be equally easy to create.  Experimentally, this is
roughly what we see — antineutrinos are produced as freely
as neutrinos (β⁻ produces ν̄_e, β⁺ produces ν_e, both
common).  By contrast, creating a positron requires pair-
production energy (1.02 MeV minimum), while antineutrinos
emerge from ordinary nuclear decays at keV–MeV scale.

If confirmed, a shearless (or low-shear) neutrino sheet
has an interesting implication for information storage:
a sheet where matter and antimatter modes are equally
accessible is a sheet where energy can be stored and
released by creating and annihilating mode pairs.  The
energy cost per bit is set by the mode energy (~meV),
far below the pair-production threshold on the charged
sheets.  If the neutrino sheet is closely coupled to
biological systems (Q85, R35), this could provide a
low-energy read/write mechanism.

Key experimental question: is there a measured CP
asymmetry in neutrino oscillation?  T2K and NOvA have
hints of CP violation (δ_CP ≠ 0, ≠ π), which would
imply nonzero shear.  But the measurement is not yet
definitive (2–3σ).  If δ_CP = 0, the neutrino sheet
may be genuinely shearless.


## Ground rules

1. The neutrino lives on Ma_ν, a 2-torus with modes
   (n₃, n₄) — tube winding n₃ and ring winding n₄.

2. The neutrino is spin-½ (experimental).  This constrains
   which modes are viable: likely requires odd n₃ (same
   mechanism as the electron's n₁ = 1), but the effective
   spin depends on ε_ν.

3. **ε_ν is a free parameter.**  Do not assume a value.
   Derive constraints from spin, masses, Σm, and N_eff.
   Sweep ε_ν across the full range (0.1 to 100) to
   understand the landscape.

4. **Mode assignment is open.**  Do not assume R26
   Assignment A or any prior candidate.  Derive which
   modes match experimental data at each ε_ν.

5. Use experimental data as input (table above).
   Derive everything else.

6. Dense mode spectrum on Ma_ν may be a feature (Q85
   storage hypothesis), not a ghost problem.  Keep this
   as a hypothesis to test, not an axiom.


## Tracks

### Track 1: Constraints on ε_ν

**Status:** Planned

**Goal:** Map out what ε_ν values are compatible with
the experimental data.  This is foundational — everything
else depends on it.

**Method:**

1. For ε_ν from 0.1 to 100 (logarithmic sweep), and
   s₃₄ from 0.001 to 0.49:

   a. Compute masses for all modes (n₃, n₄) with
      |n₃| ≤ 10, |n₄| ≤ 10.

   b. Find all mode triplets whose Δm²₃₁/Δm²₂₁ is
      within 1σ of 33.6.

   c. For each triplet, check:
      - All three modes have spin ½ (at this ε_ν)
      - Σm < 120 meV
      - Normal mass ordering (m₁ < m₂ < m₃)
      - Number of intermediate modes (sterile count)
        consistent with N_eff = 3

   d. Record the viable region in (ε_ν, s₃₄) space.

2. For each viable triplet, compute:
   - Absolute masses
   - Sheet dimensions L₃, L₄
   - Mode density in the [m₁, 2m₃] window (storage)
   - Waveguide cutoff: which modes propagate?

3. Identify whether ε_ν is constrained to a narrow range
   or broadly allowed.

**Success criteria:**
- Map of viable (ε_ν, s₃₄) parameter space
- Identified mode triplets at each point
- Whether ε_ν is bounded from above, below, or both

### Track 2: Mode spectrum and filtering assessment

**Status:** Planned

**Goal:** At representative ε_ν values (from Track 1),
characterize the full mode spectrum.  Determine whether
and how filtering operates.

**Method:**

1. At each representative ε_ν, enumerate all modes
   (n₃, n₄) and classify by:
   - Mass
   - Spin (finite-ε formula)
   - Waveguide propagation status (open and conducting)

2. Apply waveguide cutoff:
   - Open boundary: n₄ > n₃/ε_ν
   - Conducting: n₄ > p'(n₃)/ε_ν
   - Count survivors vs ε_ν

3. Assess the filtering landscape:
   - At small ε_ν: aggressive filtering, few survivors
   - At large ε_ν: permissive, nearly all propagate
   - Is there a "sweet spot" where the three mass
     eigenstates survive but ghosts are killed?

4. Count modes in energy windows relevant to storage.

**Success criteria:**
- Quantitative mode count vs ε_ν
- Whether waveguide cutoff plays any role on Ma_ν
- Storage capacity vs ε_ν

### Track 3: Oscillation — phase evolution baseline

**Status:** Planned

**Goal:** Implement the standard quantum-mechanical
oscillation model using Ma_ν eigenmodes.  Verify that
the torus mass eigenvalues reproduce observed oscillation.

**Method:**

1. Using the mass triplet(s) from Track 1, compute
   oscillation probabilities:
   P(ν_α → ν_β) = |Σᵢ U*_αi U_βi exp(−im²ᵢL/(2E))|²

2. Use experimental PMNS angles as input (not derived
   from cross-shears — that is a separate problem).

3. Plot P vs L/E for solar, reactor, atmospheric, and
   long-baseline channels.

4. Compare to published oscillation data.

**Success criteria:**
- Ma_ν masses reproduce correct oscillation lengths
- Oscillation curves are consistent with experimental
  data (this is a necessary condition, not sufficient)

### Track 4: Oscillation — energy redistribution hypothesis

**Status:** Planned

**Goal:** Test whether oscillation could involve actual
energy transfer between modes on Ma_ν, rather than (or
in addition to) pure phase evolution.

**Method:**

1. Compute the Compton window properties for Ma_ν:
   - ƛ_ν vs sheet dimensions at each ε_ν
   - Estimated Q factor (bandwidth) of the resonance
   - How does Q scale with ε_ν?

2. Estimate the energy absorption/emission rate from
   the ambient photon field (CMB, etc.) through the
   Compton window.  Compare to the oscillation frequency.

3. If rates are comparable: model the mode-hopping
   dynamics.  A neutrino in state ν₁ absorbs ΔE and
   hops to ν₂.  Compute transition rates and compare
   to standard oscillation patterns.

4. Check against SNO flux conservation and other
   constraints.

5. Assess whether "internal redistribution" (energy
   moves between modes on Ma_ν, not radiated to S)
   is distinguishable from standard phase evolution.

**Success criteria:**
- Quantitative comparison of absorption rate vs
  oscillation frequency
- If viable: predictions that differ from standard
  oscillation (testable)
- If not viable: clear statement of why

### Track 5: Uniqueness of the oscillation triplet

**Status:** Planned

**Goal:** Determine whether the three neutrino mass
eigenstates are uniquely selected among all possible
mode triplets on Ma_ν.

**Method:**

1. From Track 1, collect all viable triplets across
   the (ε_ν, s₃₄) parameter space.

2. For each, characterize:
   - Mode numbers and symmetry properties
   - Whether the triplet has a composite structure
     (gcd analysis, strand decomposition)
   - Number of sterile modes between the lightest
     and heaviest

3. Test for (3,6)-like composites: do any triplets
   consist of three copies of the same fundamental
   mode (phase-shifted)?

4. Assess whether the triplet is selected by:
   - Geometry (filter/cutoff)
   - Production (β-decay coupling)
   - Topology (only certain triplets are consistent
     with spin ½ and EM neutrality)

**Success criteria:**
- How many triplets match experimental data?
- Is there a unique or strongly preferred solution?
- Any structural parallel to the proton's (3,6)

### Track 6: Connection to information storage

**Status:** Planned

**Goal:** Quantify how the mode spectrum on Ma_ν relates
to the information storage hypothesis (Q85, R35).

**Method:**

1. At each ε_ν, compute the mode density in the
   energy window [m_ν₁, 2m_ν₃].

2. Estimate information capacity:
   - Number of distinct modes N
   - Bits per neutrino (if each mode is on/off)
   - Capacity if modes hold graded energy levels

3. Assess whether the oscillation modes serve double
   duty — structural (identity) and functional (storage).

4. Test the counting hypothesis: if oscillation IS
   mode-counting, oscillation and storage are the same
   physics.

**Success criteria:**
- Storage capacity vs ε_ν (does it match Q85 estimates?)
- Whether oscillation and storage can be unified


---

## Prior results (context, not assumptions)

These studies provide context but their specific
conclusions (mode assignments, ε values, etc.) are NOT
adopted as ground rules.

| Study | Relevant finding |
|-------|-----------------|
| R24 | Integer Δm² ratio from (0,0,n₃) modes on 3-torus; matched ratio to 0.03σ |
| R25 | Charge-spin linkage on 3-torus: uncharged fermion impossible (negative result) |
| R26 | Ma_ν as separate 2-torus; Assignment A proposed; spin at finite ε studied |
| R33 | Neutrino sheet modes may be storage, not ghost problem |
| R35 | Threshold coupling: mode-hopping as storage mechanism |
| R46 | Electron sheet: waveguide cutoff and slot filtering |
| R47 T7 | Proton sheet: (3,6) composite, SU(6) moments, confinement |
| R48 | n₁ = ±1 charge selection from CP synchronization |
| Q85 | Dense mode ladder on Ma_ν; capacity estimates |
| Q94 | Compton window as resonant aperture |
| Q102 | Neutrino neutrality may follow from sheet size — phase gradient too gentle for lattice to detect |

## Notes

- The neutrino may be the **only** particle where the
  sheet's dense mode spectrum is **functional** (storage)
  rather than problematic (ghosts).

- The tension between filtering and storage may resolve
  differently at different ε_ν: small ε_ν → aggressive
  filter, sparse modes; large ε_ν → permissive filter,
  dense modes.  The right ε_ν balances "three observed
  mass eigenstates" with "rich storage substrate."

- Neutrino oscillation frequency at typical energies
  (1 MeV solar): f₂₁ ~ Δm²c⁴/(4πℏE) ≈ 10⁻¹² Hz.
  The corresponding photon energy (~4 × 10⁻¹² eV) is
  far below any detection threshold.

- The largest uncertainty in this study is ε_ν.  Track 1
  (constraints on ε_ν) is foundational and should run
  first.

- The neutrino sheet's neutrality may have two independent
  causes: sheet size (Q102, phase gradient below lattice
  resolution) and zero shear (no symmetry breaking between
  circulation directions).  These are not mutually exclusive.
  If shear is zero, the neutrino sheet would show no
  matter/antimatter asymmetry, making it a uniquely
  accessible substrate for energy storage via mode
  creation/annihilation.  This connects directly to the
  biological coupling hypothesis (Q85, R35).
