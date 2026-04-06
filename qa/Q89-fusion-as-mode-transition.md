# Q89: Is fusion a mode transition on Ma rather than a particle collision?

**Status:** Open — reframes nuclear fusion within MaSt
**Related:**
  [Q88](Q88-phase-dependent-nuclear-force.md) (phase-dependent nuclear force — partially falsified by R39),
  [Q95](Q95-strong-force-as-internal-em.md) (strong force = internal EM at torus overlap — provides the driving mechanism),
  [Q82](Q82-entanglement-as-ma-geometry.md) (entanglement as phase locking),
  [Q87](Q87-cross-shear-phase-coupling.md) (cross-sheet phase coupling),
  R27 F15–F18 (neutron as three-sheet mode, r_p and σ_ep pinned),
  R29 F16–F21 (nuclei as Ma modes, no nuclear force needed),
  R39 (electromagnetic near-field: geometric suppression but no attraction)

---

## 1. The problem with the collision picture

R39 computed the full electromagnetic interaction between two
proton-tori at nuclear distances.  Results:

- Geometric suppression reduces Coulomb repulsion by 78% at 1 fm
  (including magnetic interaction at v = c)
- No attraction at any orientation, phase, or charge model
- The residual barrier (~0.3 MeV at 1 fm) is still positive

This means pp Coulomb barrier penetration is not how fusion
works in MaSt.  But we already knew this from R29: the deuteron
is a Ma mode (1,n₂,1,0,2,4), not "two particles bound by a
force" (R29 F16, F21).  The "nuclear force" is emergent — an
effective description of the geometry's preference for certain
mode configurations.

The question is: if fusion is a mode transition, not a collision,
what is the pathway and what determines the rate?


## 2. The neutron pathway

### 2.1 The neutron is a three-sheet mode

R27 F15 established that the neutron is the mode:

    Electron sheet:  n₁ = 0, n₂ = −2  (tube winding, no ring)
    Neutrino sheet:  n₃ = odd, n₄ = any
    Proton sheet:    n₅ = 0, n₆ = +2  (tube winding, no ring)

It is not "a proton plus an electron."  It is a single standing
wave spanning all three material sheets, held together by the
cross-sheet coupling σ_ep = −0.0906 (R27 F18).

### 2.2 The alternative pathway

Instead of:

    p + p → d + e⁺ + ν_e     (requires pp Coulomb barrier crossing)

consider:

    Step 1:  p + e + ν → n    (mode transition via σ_ep coupling)
    Step 2:  n + p → d        (mode transition, no Coulomb barrier)

Step 1 involves opposite charges (p and e attract) — no Coulomb
barrier.  Step 2 involves a neutral particle — no Coulomb barrier.
The pp barrier is never encountered.

### 2.3 In wave terms

The state of Ma at a given S location is a superposition of all
modes present:

    Ψ(θ₁...θ₆) = Σ_k  A_k · exp(i n_k · θ + i φ_k)

"Separate particles" means uncorrelated phases (random φ_k).
"Neutron" means specific quantum numbers (0,−2,odd,n₄,0,+2)
with all three sheets phase-locked.  "Deuteron" means quantum
numbers (1,n₂,1,0,2,4) — the proton mode wound twice.

Fusion is not "smashing two particles together."  It is the
wave configuration of Ma evolving from one mode pattern to
another:

    Initial:  p(0,0,0,0,1,2) + p(0,0,0,0,1,2) + e(−1,2,...) + ν(...)
    Final:    d(1,n₂,1,0,2,4) + ν(...)

The transition does not require the proton modes to "collide"
in S.  It requires the three standing waves (on their respective
sheets) to achieve the right phase conjunction at a shared S
location.


## 3. What determines the transition rate

### 3.1 The coupling: σ_ep

The cross-sheet coupling σ_ep = −0.0906 enters the Ma metric
off-diagonally, connecting the electron tube (dimension 2) to
the proton ring (dimension 5).  This is the parameter that
allows modes to span sheets.

In the collision picture, σ_ep maps to the "weak interaction
coupling."  In the wave picture, it determines how strongly the
electron and proton sheet waves influence each other.  A larger
|σ_ep| means faster mode transitions between sheets.

The transition amplitude scales as:

    |⟨n | H_coupling | p + e + ν⟩|² ∝ σ_ep²

With σ_ep ≈ 0.09, σ_ep² ≈ 0.008 — a small but nonzero
transition probability per "attempt."

### 3.2 Energy threshold

The neutron is heavier than its constituents:

    m_n − m_p − m_e = 1.293 − 0.511 = 0.782 MeV

This energy must be supplied for Step 1.  It is:
- An energy threshold, not a potential barrier (no tunneling)
- Smaller than the pp Coulomb barrier (0.782 vs 1.44 MeV)
- Much smaller than the barrier without geometric suppression

In a stellar core (kT ≈ 1.3 keV), this threshold is far
above thermal energy.  But the tail of the Maxwell-Boltzmann
distribution, combined with the enormous number of attempts
(~10⁵⁷ proton-electron pairs per second in the Sun), makes
the process possible.

### 3.3 Phase conjunction

For the mode transition to occur, the three standing waves
must achieve the right phase relationship — the specific
conjunction corresponding to the neutron mode's quantum
numbers.  In a thermal environment:

- Each mode oscillates at ω = E/ℏ (e.g., ω_p ≈ 1.4 × 10²³ Hz)
- Relative phases evolve rapidly and ergodically
- The conjunction occurs with probability ~1/(2π)^(number of
  independent phases)

The conjunction probability may be enhanced by:
- Cross-sheet coupling (σ_ep biases toward certain phase
  relationships)
- Lattice coherence (collective modes in a crystal)
- External perturbation (Q87 — energy injection into the
  neutrino sheet)


## 4. Connection to standard physics

### 4.1 The pp chain

In standard physics, solar fusion follows the pp chain:

    p + p → d + e⁺ + ν_e    (rate-limited by weak interaction)

The rate-limiting step is the weak interaction that converts
p → n.  The Coulomb barrier is surmounted by quantum tunneling
(probability ~10⁻²⁸), but even after tunneling, the weak
interaction rate is tiny (σ_weak ~ 10⁻⁴⁷ cm²).

In MaSt, this maps cleanly:
- "Weak interaction" → cross-sheet coupling σ_ep
- "Coulomb barrier tunneling" → geometric suppression (R39)
  and/or irrelevance (neutron pathway avoids it)
- "Rate-limiting step" → σ_ep² transition probability

### 4.2 Beta decay as the reverse process

The neutron's decay (n → p + e + ν̄, τ ≈ 880 s) is the reverse
of Step 1.  In MaSt, this is the three-sheet mode "unraveling"
back into separate single-sheet modes (R27 F15).  The lifetime
is determined by:

    Γ_decay ~ σ_ep² × (phase space) × (energy denominator)

The 880-second lifetime implies σ_ep² × (kinematic factors) is
very small, consistent with σ_ep = 0.09 being a weak coupling.

This provides a quantitative check: can we reproduce the
neutron lifetime from σ_ep = 0.09 and the Ma mode spectrum?


## 5. Implications for cold fusion

### 5.1 The reframe

Q88 analyzed cold fusion through the pp barrier:

    "How do two protons tunnel through a 550 keV barrier
     at room temperature?"

    Answer: they can't, even with geometric suppression (R39).

Q89 reframes:

    "How often do three standing waves (proton, electron,
     neutrino) achieve the phase conjunction for a neutron
     mode to form?"

This is a fundamentally different question.  There is no Coulomb
barrier to tunnel through.  The process is limited by:

1. Energy threshold (0.782 MeV for Step 1)
2. σ_ep coupling strength
3. Phase conjunction probability
4. Availability of a neutrino mode

### 5.2 The energy problem remains

At room temperature, kT ≈ 25 meV.  The energy threshold for
neutron formation is 0.782 MeV — a factor of 3 × 10⁷ above
thermal.  No single particle has enough energy.

Possible resolutions:
- **Collective modes**: in a crystal lattice, phonon energy
  can concentrate.  A cooperative transition involving many
  lattice sites could supply the threshold energy.
- **Screening**: in a metal, conduction electrons screen the
  proton, effectively modifying the energy balance.
- **Not the right pathway**: perhaps a different mode transition
  (not via neutron formation) has a lower threshold.

### 5.3 The neutrino mode question

Step 1 requires a neutrino mode (n₃ = odd).  Where does this
come from?  Options:

- The cosmic neutrino background provides ambient neutrino modes
  (extremely low density, ~330/cm³)
- The neutrino sheet already carries sub-threshold modes (Q83)
  that could participate without requiring a "real" neutrino
- The neutrino mode is created in the transition itself (as in
  standard beta decay, where the neutrino is emitted)

If the neutrino mode must be created, the energy threshold
rises (neutrino mass is small, so this is negligible for energy
but may matter for phase space).


## 6. The neutrino-triggered mechanism

### 6.1 The scenario

1. A neutrino mode on Ma_ν at some S location is pumped to
   just below 2× its fundamental energy (the threshold
   hypothesized in Q85 where a mode becomes unstable).
2. A proton and electron occupy the same S location — a
   hydrogen atom, or a lattice site in a metal.
3. The neutrino is pushed over the 2× threshold and its mode
   configuration becomes catastrophically unstable.
4. Through cross-sheet coupling (σ_eν, σ_νp), the
   reconfiguration propagates to Ma_e and Ma_p.
5. If the proton and electron modes have the right phase
   relationship at that instant, all three sheets snap into
   the neutron configuration (0,−2,odd,n₄,0,+2).

### 6.2 Why this is more than a trigger

The neutrino isn't just a catalyst — it is a **structural
component** of the neutron.  The neutron mode requires
n₃ = odd (neutrino ring winding).  When the neutrino crosses
its threshold, it doesn't merely dump energy — it reconfigures
its quantum numbers.  If it reconfigures into the specific
(n₃=odd, n₄) pattern that the neutron requires, it provides
both the missing quantum numbers AND a violent phase
perturbation that can lock the other two sheets into the
neutron configuration.

### 6.3 The phase sledgehammer

The 2× threshold transition is not a small perturbation.
Q88 §4.1 estimated that a ~keV perturbation shifts a proton's
phase by π in ~7 attoseconds.  A catastrophic mode
reconfiguration is vastly larger — it restructures the
cross-sheet coupling landscape entirely.  The proton and
electron modes, which were almost-but-not-quite in the neutron
phase conjunction, get violently shoved into the nearest basin
of attraction.  If they are pre-correlated (co-located in a
hydrogen atom), the neutron basin IS the nearest one.

### 6.4 The energy problem and virtual intermediates

The neutron is 0.782 MeV heavier than p + e + ν.  This energy
must come from somewhere.  Options:

**A. The neutrino's pumped energy supplies it.**  This requires
the neutrino mode at 2× threshold to carry ≥ 0.782 MeV.  The
neutrino sheet dimensions are not precisely known, so this
cannot be ruled out.

**B. Virtual intermediate state.**  The neutron is a virtual
intermediate that "borrows" 0.782 MeV via energy-time
uncertainty (ΔE × Δt ≳ ℏ).  The virtual neutron survives for
Δt ~ ℏ/(0.782 MeV) ~ 8 × 10⁻²² s.  If a second proton is
within ~1 fm, the deuteron forms in this time, releasing
2.2 MeV of binding energy — more than enough to pay back the
loan.  The full reaction:

    p + p + e + ν → d + ν'    (releases 1.44 MeV net)

is exothermic.  The virtual neutron need only survive long
enough for the second proton to join.

**C. The threshold IS the mass gap.**  If the neutrino's 2×
threshold energy is comparable to the 0.782 MeV mass gap,
then the neutrino mode at threshold naturally carries the
right amount of energy for neutron formation.  This would
be a remarkable coincidence — or a sign that the neutrino
sheet dimensions are constrained by nuclear physics.

### 6.5 Connection to electron capture

This mechanism is the MaSt reframe of **electron capture**
(p + e → n + ν_e), a well-established process in proton-rich
nuclei.  In standard physics, the electron must have enough
energy to supply the mass deficit, and the weak interaction
mediates the conversion.  In MaSt:

- "Electron energy" → kinetic energy + neutrino pump energy
- "Weak interaction" → cross-sheet coupling σ_ep, σ_eν, σ_νp
- "Neutrino emission" → the neutrino mode reconfigures
  (it was already present; it doesn't need to be created)

### 6.6 Requirements

For this mechanism to work:

1. **σ_eν and σ_νp must be nonzero.**  R27 F14 found them
   approximately zero, but with limited precision.  Even
   small values (10⁻³) could suffice if the perturbation
   is large (threshold explosion).

2. **The 2× threshold must exist.**  Q85 hypothesizes this
   from harmonic ladder theory; Q90 suggests the dynamic
   torus provides the instability mechanism.  Not derived.

3. **Pre-correlation helps but may not be required.**  In a
   hydrogen atom, the electron and proton wave functions
   already overlap at the nucleus.  In a metal lattice,
   conduction electrons screen the proton.  Either provides
   the spatial co-location needed for the three-sheet
   conjunction.


## 7. What's computable

### 7.1 Neutrino sheet energy scale

Determine the fundamental mode energy on Ma_ν.  If the (1,0)
neutrino mode energy is in the meV range, the 2× threshold is
too low to supply the neutron mass gap.  If it is in the keV–MeV
range, the §6.4C threshold mechanism becomes viable.  This
depends on L₃ and L₄ (neutrino sheet circumferences), which
are weakly constrained.

### 7.2 Transition energy landscape

Using ma_model.py, compute the energy of the Ma mode spectrum
as a function of a "mixing parameter" that interpolates between:

    Initial: separate proton + electron + neutrino modes
    Final: neutron mode (0,−2,odd,n₄,0,+2)

The energy along this path is the "reaction coordinate."  If
there is a smooth path without an energy maximum above the
threshold, the transition is energetically downhill (given
sufficient input energy).

### 7.3 Transition rate from σ_ep

Compute the matrix element ⟨neutron | H_σ | proton + e + ν⟩
where H_σ is the cross-sheet coupling Hamiltonian arising from
σ_ep ≠ 0 in the Ma metric.  Compare the resulting rate with
the measured neutron lifetime (880 s) as a consistency check.

### 7.4 Deuteron formation rate

Compute the matrix element for the full process:
proton + neutron → deuteron.  This is a within-sheet transition
(both are proton-sheet modes, one wound once and one wound
twice).  The rate should be fast (strong-scale, not weak-scale).

### 7.5 Alternative pathways

Search the Ma mode spectrum for intermediate states between
"two protons + electron + neutrino" and "deuteron + neutrino."
Are there lower-energy pathways that bypass the 0.782 MeV
neutron threshold?


## 8. Falsifiability

1. **Neutron lifetime from σ_ep**: if the MaSt transition rate
   (using σ_ep = 0.09) does not reproduce the 880-second neutron
   lifetime, the mapping between σ_ep and the weak coupling is
   wrong.

2. **Solar fusion rate**: the pp chain rate in the Sun is
   measured (solar luminosity → neutrino flux).  The MaSt
   prediction (using σ_ep, geometric suppression, and the mode
   spectrum) must match.

3. **No cold fusion below threshold**: if the energy threshold
   for mode transition is firm (0.782 MeV), MaSt predicts no
   fusion below this energy regardless of lattice structure or
   phase alignment.  Any confirmed cold fusion at energies
   << 0.782 MeV would require either a different pathway or a
   flaw in the threshold calculation.

4. **Neutrino-triggered fusion rate**: if the §6 mechanism
   is correct, the fusion rate should depend on the local
   neutrino flux and energy spectrum.  Environments with
   higher neutrino density or more energetic neutrinos
   should show enhanced electron capture rates — testable
   near nuclear reactors or in astrophysical environments.


## 9. Relationship to Q88 and R39

Q88 hypothesized that phase-dependent near-field effects could
reduce the pp Coulomb barrier, enabling fusion.  R39 tested
this and found:

- Geometric suppression is real (78% at 1 fm) — F3, F9
- Phase effects are secondary (~3–14%) — F4
- The (1,2) mode has π-periodicity, so "anti-phase" ≡ "in-phase" — F2
- No electromagnetic attraction at any orientation — F7, F9

Q88's specific mechanism (anti-phase multipole cancellation)
is falsified for the (1,2) proton mode.  But the underlying
intuition — that the near-field structure matters at nuclear
distances — is validated.

Q89 takes a different approach: instead of trying to push
protons through a barrier, it asks whether the barrier is
relevant at all.  If fusion is a mode transition (not a
collision), the Coulomb barrier is a feature of the wrong
picture.

---

## 11. The loading pathway (threshold theory)

Sections 5–6 treat the 0.782 MeV neutron threshold as a
hard wall: the energy must be delivered in a single quantum
or borrowed virtually.  Threshold theory
([primers/threshold-theory.md](../primers/threshold-theory.md))
offers a third possibility: **sub-threshold accumulation**.

### 11.1 Loading, not quantized delivery

In the threshold/loading picture (Planck 1911, Reiter 2014),
energy absorption is continuous.  A system can accumulate
energy gradually in its mode spectrum — distributing it
across non-fundamental modes as a "pre-loaded state" — until
the total crosses a threshold and the system pops into the
target mode.

Applied to the neutron formation step:

1. Energy arrives at Ma_p through some coupling channel
   (see §12 below) in small increments — meV per photon.
2. The energy distributes across non-fundamental modes on
   the proton sheet.  No single mode has enough energy to
   form a neutron — but the total accumulates.
3. When the total stored energy exceeds 0.782 MeV, the
   modes cascade (§5.3 of the threshold primer): energy
   reorganizes from many distributed modes into the neutron
   configuration.
4. The transition is sharp — topological quantization means
   the neutron mode is either fully occupied or not.  There
   is no gradual turning-on.

This removes the requirement for a single 0.782 MeV quantum.
The energy can arrive over many interactions, each far below
threshold, provided the pre-loaded state persists long enough
for the total to accumulate.

### 11.2 The linearity constraint

The torus boundary (the junction between the 2D sheet and
the 3D lattice) couples at 1/α ≈ 1/137.  This coupling is
**linear** — double the wave energy, double the Coulomb
field energy.  There is no nonlinear frequency mixing at
the boundary (sim-impedance finding).

This means the frequency-mixing pathway proposed by some
(inject two low frequencies, mix nonlinearly to produce a
high frequency) does not work.  The boundary is a linear
beam splitter, not a nonlinear mixer.

However, linearity does NOT prevent loading.  Loading is
not frequency conversion — it is energy accumulation across
many modes, followed by a topological cascade.  Each
individual deposit is linear.  The nonlinearity is in the
final step — the pop from distributed energy to coherent
mode — which is topological (winding number changes
discontinuously), not electromagnetic.

### 11.3 The pre-loaded lifetime question

For loading to work, the pre-loaded state (energy
distributed across non-fundamental modes) must persist
long enough for the total to reach threshold.  If the
modes dissipate faster than energy arrives, the pre-loaded
state never accumulates.

The dissipation rate depends on how strongly the
non-fundamental modes couple to the 3D lattice (leak
energy outward).  Each mode leaks at rate α — the same
impedance mismatch.  For a mode with energy E, the leak
rate is ~αE per coupling time.  If the pump rate exceeds
the leak rate, the pre-loaded state grows.

This is quantitatively analogous to laser physics:
pumping must exceed losses for population inversion
(threshold) to be reached.  The "cavity Q" of the proton
torus determines the minimum pump power.


## 12. The bootstrap: accessing the proton sheet

### 12.1 The problem

The proton's Compton window is at ~1.3 fm wavelength —
deep gamma-ray territory.  You cannot directly pump the
proton sheet with accessible radiation.  The neutrino
Compton window at ~42 μm (mid-infrared) is accessible,
but the bare proton has no neutrino-sheet component.
There is no handle to grip.

This is the bootstrap problem: to open the neutrino
window on a proton, you need a neutrino-sheet component;
to create a neutrino-sheet component, you need to access
the proton through some coupling channel.

### 12.2 The virtual fluctuation resolution

In quantum field theory, every particle has a cloud of
virtual excitations.  The proton constantly fluctuates
between its ground state and higher configurations,
including states with cross-sheet components.  In MaSt
terms: the cross-sheet coupling σ_νp, even if very small,
gives the proton a nonzero amplitude on the neutrino
sheet.

If σ_νp ≠ 0 — even at 10⁻⁶ — then every proton has an
ephemeral neutrino-sheet component.  This component
flickers in and out of existence as a quantum fluctuation.
It is not a stable excitation; it is a virtual tail of the
proton's wave function extending onto Ma_ν.

**IR pumping at ~42 μm could resonantly enhance this
fluctuation.**  By driving the neutrino-sheet component
at its natural frequency (~7 THz), the fluctuation is
sustained — its lifetime is extended from a virtual blip
to a quasi-stable excitation.  This opens the Compton
window.

Once the window is open, additional energy can be loaded
through it onto the proton sheet.  Each IR photon delivers
~30 meV through the sustained neutrino-sheet coupling.
The energy accumulates in pre-loaded modes on Ma_p.

### 12.3 The value of σ_νp

R27 F14 found σ_eν and σ_νp to be approximately zero,
but with limited precision.  The neutron and muon fits
constrain σ_ep = −0.091 but leave the other cross-shears
weakly bounded.

The question "is σ_νp exactly zero or merely very small?"
is critical.  If exactly zero, the bootstrap is closed and
the only pathway is through deuterium (which already has
a neutron component — see §12.5).  If nonzero, every
proton is a potential seed.

This is constrainable from the Ma metric.  A dedicated
study could bound σ_νp by checking whether any known
observables (neutrino-proton scattering cross-sections,
proton charge radius corrections) are sensitive to it.

### 12.4 The hydrogen-to-helium pathway

If the bootstrap works (σ_νp ≠ 0, IR pumping sustains the
neutrino window), the full fusion pathway is:

**Step 1 — Open the window.**  Pump hydrogen gas (or
hydrogen in a metal lattice) with ~42 μm IR radiation.
This resonantly enhances the proton's virtual
neutrino-sheet component, opening the Compton window.

**Step 2 — Load the proton sheet.**  Continue pumping.
Energy accumulates on Ma_p through the sustained
neutrino coupling, distributing across pre-loaded modes.

**Step 3 — Neutron formation (the pop).**  When the
accumulated energy exceeds 0.782 MeV (the neutron mass
deficit), the pre-loaded state cascades into the neutron
mode.  The nearby electron is captured (providing the
Ma_e component).  A neutrino is emitted (the Ma_ν
component reconfigures).  The proton has become a
neutron.

**Step 4 — Coulomb barrier bypassed.**  The neutron is
electrically neutral.  No Coulomb repulsion with
neighboring protons.

**Step 5 — Magnetic alignment.**  An external DC magnetic
field aligns the neutron's magnetic moment.  Nearby
protons are also aligned.  The magnetic dipole-dipole
interaction, though weak, provides a gentle attractive
force between aligned neutral and charged particles at
close range.

**Step 6 — Nuclear assembly.**  The neutron, now adjacent
to a proton with no electrostatic barrier, merges into a
deuteron via a Ma_p mode transition (fast, strong-scale
coupling).  Further assembly: d + d → He-4 or d + p → He-3.

**Step 7 — Energy release.**  The fusion products have
less total mass than the inputs.  The mass deficit emerges
as kinetic energy of the products, photons, and neutrinos.
Net energy gain: ~24 MeV per helium-4 nucleus formed.

**Step 8 — Cascade.**  Each new neutron formed in Step 3
provides another neutrino window (the neutron has n₃ = 1).
This window can assist neighboring protons in their own
loading process, potentially creating a chain reaction
that is self-sustaining once initiated.

### 12.5 The deuterium seed alternative

If σ_νp = 0 (exactly zero), the virtual fluctuation
pathway is closed.  But natural hydrogen contains 0.015%
deuterium, and each deuterium nucleus already has a
neutron — which has the neutrino window.

The deuterium seed pathway:

1. IR at ~42 μm pumps the deuterium's neutron neutrino
   component
2. The loaded energy stays local to the deuterium nucleus
   (it does not reach neighboring bare protons — the modes
   are localized on Ma_p at the fm scale)
3. Additional energy converts the deuterium's proton to a
   second neutron, producing a dineutron
4. The dineutron, fully neutral, can approach a neighboring
   proton without Coulomb barrier → tritium
5. Tritium + deuterium → helium + neutron (known DT fusion,
   but now at lower temperature because Step 3-4 bypass the
   barrier)

This pathway is more constrained (requires deuterium, which
is rare) and does not bootstrap bare hydrogen.  It is the
fallback if σ_νp = 0.

### 12.6 Specific experimental parameters

If the loading pathway is viable, the experimental
requirements are specific and testable:

| Parameter | Value | Source |
|-----------|-------|--------|
| Pump wavelength | ~42 μm | Neutrino Compton window (Ma_ν circumference) |
| Pump frequency | ~7 THz | c / 42 μm |
| Photon energy | ~30 meV | hf at 7 THz |
| Photons to threshold | ~26,000 | 0.782 MeV / 30 meV |
| Target medium | H₂ gas, or H in Pd/Ni lattice | Standard LENR substrates |
| DC magnetic field | ~1–10 T | Alignment of nuclear moments |
| Expected signature | Neutron emission, then helium accumulation | Standard nuclear detection |

The pump wavelength (~42 μm) is in the mid-infrared,
accessible with CO₂ laser harmonics, free-electron lasers,
or quantum cascade lasers.  The total energy per neutron
conversion is 0.782 MeV (delivered as ~26,000 IR photons),
with a net gain of ~24 MeV per helium-4 — an energy
multiplication factor of ~30.


---

## 14. Energy accounting and self-sustaining cascade

### 14.1 The energy budget

The overall reaction (4 hydrogen → 1 helium) is the same
as the Sun's pp chain.  The endpoints are identical, so the
total energy release is identical regardless of pathway.
The question is whether the loading pathway is net
exothermic after accounting for the pump energy.

| Step | Reaction | Energy in | Energy out | Net |
|------|----------|----------|------------|-----|
| 1 | p → n (loaded via IR pump) | 1.804 MeV | — | −1.804 MeV |
| 2 | n + p → d | — | 2.224 MeV | +2.224 MeV |
| 3 | p → n (second conversion) | 1.804 MeV | — | −1.804 MeV |
| 4 | d + d → He-4 (or d+n→t, t+d→He-4) | — | ~23.8 MeV | +23.8 MeV |
| | **Total: 4p + 2e → He-4 + 2ν** | **3.608 MeV** | **~26.0 MeV** | **+22.4 MeV** |

Energy multiplication factor: **~7.2×**.

This is not a hypothesis — the nuclear masses are measured
to high precision and the energy balance follows from
mass-energy equivalence.  The only question is whether the
loading pathway can deliver the 3.6 MeV input efficiently
enough for the 22.4 MeV output to be harvested.

### 14.2 Where does the output energy go?

- **Kinetic energy of fusion products** — the helium nucleus
  and any ejected neutrons carry MeV-scale kinetic energy.
  In a solid or liquid medium, this thermalizes as heat.
  Harvestable.
- **Gamma rays** from nuclear de-excitation — harvestable
  by absorption in shielding material (also becomes heat).
- **Neutrino kinetic energy** — lost.  Neutrinos escape the
  apparatus.  In the Sun's pp chain, ~2% of the total energy
  escapes as neutrinos.  A similar fraction applies here.

### 14.3 Does one fusion enable the next?

Yes — through the **neutrino window cascade**, not through
energy feedback.

**What cascades (the window):**

Step 1 converts a proton to a neutron.  The neutron has a
neutrino-sheet component (n₃ = 1).  This component provides
a neutrino Compton window at ~42 μm.

Before Step 1, if σ_νp = 0 and no deuterium seed is
available, no proton has a neutrino window.  The bootstrap
problem is in effect.

After Step 1, the newly formed neutron (or the deuteron it
joins in Step 2) has a neutrino window.  This window can
assist the NEXT proton's loading process — the neutron's
Ma_ν component couples to neighboring protons through
whatever cross-sheet pathway exists.

Each subsequent neutron formation opens another window.
The number of available loading channels grows with each
reaction.  This is a cascade in accessibility, not in
energy.

**What does NOT cascade (the energy):**

The 2.224 MeV gamma from deuteron formation (Step 2)
does not efficiently reload the next proton.  The gamma
is a 3D lattice photon.  To load a proton sheet mode, it
must couple through the α junction (3D → Ma_p).  The
coupling efficiency is ~1/137 per hop, delivering only
~16 keV to Ma_p — well below the 0.782 MeV threshold.

Even if the gamma first couples to Ma_ν (3D → Ma_ν at
the neutrino Compton window) and then cross-couples to
Ma_p (Ma_ν → Ma_p via σ_νp), the two-hop efficiency is
α × σ_νp — extremely small.

**Conclusion:** the IR pump must stay on.  The reactions
are exothermic (7× energy gain), but the pump provides
the activation energy for each proton-to-neutron
conversion.  The system is analogous to a catalytic
reactor: the catalyst (neutrino window) cascades and
grows, but the feedstock (IR pump energy) must be
continuously supplied.

### 14.4 Self-sustaining vs pump-sustained

| Property | Fission (for comparison) | This pathway |
|----------|------------------------|-------------|
| Energy source | Nuclear binding energy | Nuclear binding energy |
| Chain mechanism | Each fission releases neutrons that trigger more fissions | Each neutron opens a neutrino window that enables more conversions |
| Self-sustaining? | Yes — neutrons carry the chain energy | No — windows enable access but don't carry the loading energy |
| External input | None after ignition (critical mass) | Continuous IR pump (~42 μm) |
| Control | Control rods absorb excess neutrons | Pump power controls reaction rate |
| Runaway risk | Yes (bomb) | No — turn off the pump, reactions stop |

The absence of runaway risk is a safety feature.  The
reaction rate is controlled by the pump power, not by a
chain reaction.  There is no critical mass.  Turning off the
IR laser stops the loading process immediately.  Any
neutrons already formed will either merge with nearby
protons (releasing energy) or decay back to protons (880 s
half-life) — both are safe.

### 14.5 Engineering viability (rough estimate)

The pump delivers 0.782 MeV per neutron as ~26,000 IR
photons at ~30 meV each.  The fusion output is ~22.4 MeV
per He-4 (requiring 2 neutron conversions, so 1.564 MeV
pump input per He-4).

The net gain per He-4: 22.4 − 1.6 = **20.8 MeV**.

If the IR-to-neutrino-window coupling efficiency is η
(the fraction of pump photons that actually deposit energy
on Ma_p through the neutrino channel), then the effective
pump cost is 1.6 / η MeV per He-4.

Break-even requires:

> η > 1.6 / 22.4 ≈ **7.1%**

If more than 7.1% of the IR pump energy reaches the
proton sheet, the process is net energy-positive.  Below
7.1%, the pump costs more than the fusion yields.

The coupling efficiency η depends on:
- σ_νp (the cross-sheet coupling — the most important
  unknown)
- The resonant enhancement from driving at the Compton
  frequency
- The geometry of the pump (focused vs diffuse, pulse
  vs CW)
- The medium (gas phase vs metal lattice — lattice
  coherence may enhance coupling)

Whether η exceeds 7.1% is not known.  It is the
engineering question that determines practical viability.


## 16. Output harvesting and system design

### 16.1 Heat output

When a helium nucleus forms with ~20 MeV of kinetic energy,
it collides with surrounding atoms and thermalizes — sharing
its energy with the medium until everything reaches the same
temperature.  In a gas, the gas heats up.  In a metal
lattice (palladium loaded with hydrogen), the metal heats up.

The heat can be harvested at various scales:

| Method | Efficiency | Complexity | Scale |
|--------|-----------|------------|-------|
| Thermoelectric (Seebeck) junction | ~5–10% | No moving parts | Tabletop to small appliance |
| Stirling engine | ~20–30% | Sealed, no consumables | Residential to industrial |
| Steam turbine | ~33–40% | Full infrastructure | Power plant |
| Direct heat (no conversion) | ~95% | Minimal | Home heating, process heat |

Thermoelectric junctions work the way RTGs (radioisotope
thermoelectric generators) power deep-space probes:
temperature difference across a bimetallic junction
generates electricity directly.  Low efficiency but extreme
simplicity and reliability.

### 16.2 Gamma output

The 2.224 MeV gamma from deuteron formation is ionizing
radiation — dangerous to biological tissue.  It must be
absorbed, not vented.

**Shielding converts gamma to heat.**  Dense material (lead,
tungsten, or water) surrounds the reaction chamber.  Gammas
interact with the shielding atoms via Compton scattering,
pair production, and photoelectric absorption, depositing
their energy as heat in the shielding material.  The gamma
becomes heat in the wall.

Shielding thickness for 2.224 MeV gammas:
- ~10 cm of lead → ~1000× attenuation
- ~50 cm of water → ~1000× attenuation

**Water shielding is particularly elegant.**  A water jacket
around the reaction chamber absorbs gammas AND neutrons (see
§16.3), heats up, and the hot water is directly useful for
heating or steam generation.  Water is cheap, self-healing
(no cumulative radiation damage), and provides shielding,
neutron moderation, and heat transport in one medium.

### 16.3 Neutron output

Some fusion pathways produce free neutrons (e.g.,
d + d → He-3 + n).  Free neutrons are ionizing radiation
and harder to shield than gammas — they pass through dense
materials because they have no charge.

Hydrogen-rich materials (water, polyethylene) are the best
neutron shields.  The hydrogen atoms have the same mass as
neutrons, so they absorb kinetic energy efficiently — like
billiard balls of equal mass.  Each collision transfers
roughly half the neutron's energy.

A water jacket handles both gammas and neutrons.  This is
the standard approach in nuclear engineering and is well
understood.

### 16.4 Waste products

| Output | Nature | Handling |
|--------|--------|---------|
| Helium | Inert gas, non-toxic, non-radioactive | Vent or collect (commercially valuable) |
| Neutrinos | Pass through everything | No handling needed (escape harmlessly) |
| Heat | Thermal energy in medium and shielding | Harvest via thermoelectric, Stirling, steam, or direct use |
| Gammas | Ionizing radiation, 2.224 MeV | Absorbed by water jacket → becomes heat |
| Neutrons | Ionizing radiation, MeV-scale | Absorbed by water jacket → becomes heat |

No carbon emissions.  No long-lived radioactive waste
(unlike fission — no transuranics, no spent fuel rods, no
geological storage).  The only radioactive outputs are the
transient neutrons and gammas, which are fully absorbed by
the water jacket during operation.  When the pump is turned
off, radiation stops immediately (no residual radioactivity
beyond any activated shielding material, which is minimal
for water).

### 16.5 Reaction control

The system has **two independent control inputs**:

**1. IR pump power (the throttle).**  More pump power → more
protons loaded to threshold → more neutrons formed → more
fusion.  Turn off the pump → loading stops → no new neutrons
→ reaction ceases.  Existing neutrons either fuse with
nearby protons (releasing energy, safe) or decay back to
protons (880 s half-life, safe).  The pump is the gas pedal.

**2. Hydrogen flow (the fuel line).**  No hydrogen → nothing
to fuse.  But hydrogen without the pump is inert — the
protons sit there doing nothing until loaded.  Hydrogen flow
controls the fuel supply; the pump controls the reaction
rate.

The reaction rate is:

> R = (pump power) × (coupling efficiency η) × (hydrogen
> density in reaction zone)

All three factors are independently controllable.  There is
no critical mass.  There is no chain reaction.  There is no
runaway risk.  The system is inherently stable: any loss of
pump power or fuel flow stops the reaction immediately.

### 16.6 Hydrogen from hydrolysis (no storage)

Stored hydrogen is explosive.  An alternative: electrolyze
water on demand to produce hydrogen, and feed it directly
into the reaction chamber.  No hydrogen storage, no
explosion risk.

The electrolysis energy cost is ~237 kJ/mol of H₂O split.
The fusion energy output is ~2.17 × 10⁹ kJ/mol of He-4
produced.  The electrolysis cost is ~0.01% of the fusion
output — negligible.

### 16.7 System schematic

A self-contained system:

```
Water in → Electrolyzer → H₂ gas
                            ↓
              Reaction chamber ← IR pump (42 μm laser)
              (H₂ in magnetic field)
                            ↓
              Fusion products (He, n, γ, ν, heat)
                            ↓
              Water jacket (shielding + heat capture)
              - Absorbs gammas → heat
              - Absorbs neutrons → heat
              - Contains all radiation
                            ↓
              Hot water
                            ↓
    ┌─────────────┬─────────────┬──────────────┐
    ↓             ↓             ↓              ↓
 Direct heat  Thermoelectric  Stirling     Steam turbine
 (simplest)   (no moving      (moderate)   (highest η)
              parts)
                            ↓
              Electricity + waste heat
              He gas vented or collected
```

**Inputs:** water, electricity (for electrolyzer and IR
pump).
**Outputs:** electricity (net positive if η > 7.1%), heat,
helium.
**Waste:** none that requires long-term management.

### 16.8 Scale considerations

The system could in principle operate at any scale:

| Scale | Pump source | Heat harvest | Application |
|-------|------------|-------------|-------------|
| Benchtop | QCL or FEL at 42 μm | Thermoelectric | Research demonstration |
| Residential | Tuned IR laser array | Stirling engine | Home power + heating |
| Industrial | High-power FEL | Steam turbine | Grid power |
| Portable | Miniature QCL | Thermoelectric | Remote/mobile power |

The key engineering challenge at every scale is the same:
coupling the 42 μm pump into the neutrino window efficiently
enough to exceed the 7.1% break-even threshold.

**The giant caveat remains:** this entire system depends on
the loading pathway working — which requires σ_νp ≠ 0 and
η > 7.1%.  If either fails, the system produces nothing but
warm hydrogen and wasted IR photons.  The output physics
(nuclear masses, energy balance, shielding requirements) is
established.  The input physics (loading through the
neutrino window) is the unproven link.


## 18. MHD direct conversion to electricity

### 18.1 The opportunity

The fusion products include He-4 nuclei — charge +2e,
kinetic energy ~20 MeV, moving at ~7% of the speed of
light.  These are charged particles moving through the
DC magnetic field that is already present in the system
(for nuclear magnetic alignment, §12.4 Step 5).

A charged particle moving through a magnetic field
experiences the Lorentz force, which deflects it
perpendicular to both its velocity and the field.  If
electrodes are placed on opposite walls of the reaction
chamber (perpendicular to both B and the particle flow),
the Lorentz force pushes positive ions to one electrode
and electrons to the other.  Current flows through the
external circuit.  This is **magnetohydrodynamic (MHD)
direct conversion** — electricity from moving charges
in a magnetic field, with no turbine, no steam, no
moving parts.

### 18.2 Why this fits the system naturally

The magnetic field is already there — it's required for
Step 5 (alignment).  The fast charged particles are
already there — they're the fusion products.  Adding
MHD extraction requires only electrodes on the chamber
walls.  No new hardware beyond what the reaction already
needs.

MHD theoretical efficiency is ~60–70%, far higher than
thermal conversion (33–40% for steam, 5–10% for
thermoelectric).  The challenge in conventional MHD
research has been sustaining a plasma.  This system
does not have a plasma — it has individual fusion events
producing fast alphas in a gas.  Lower power density
than plasma MHD, but far simpler.

The electrodes serve **triple duty**:

1. **Electrical** — collect Lorentz-separated charges,
   carry current to external circuit
2. **Gamma shielding** — dense metal (tungsten or copper)
   provides excellent gamma attenuation on the two faces
   that receive the most particle bombardment (the
   Lorentz force drives all fast alphas toward the
   electrodes).  A few cm of tungsten attenuates gammas
   comparably to lead.
3. **Structural** — form two walls of the reaction chamber

The remaining four faces still need the water jacket.
The electrode faces are self-shielding for gammas and
charged particles.

**Neutrons pass through the electrodes.**  Neutrons have
no charge — the Lorentz force does not affect them and
they interact minimally with heavy nuclei (a ping-pong
ball bouncing off a bowling ball barely slows down).
Neutrons that pass through the electrodes are caught by
the water jacket behind them.  This is a clean separation
of labor:

| Component | Stops gammas | Stops charged particles | Stops neutrons |
|-----------|-------------|------------------------|---------------|
| Metal electrodes (2 faces) | Yes | Yes | No — transparent |
| Water jacket (behind electrodes + 4 other faces) | Yes | Yes | Yes |

**Neutron activation.** Neutrons hitting electrode nuclei
can produce radioactive isotopes through neutron capture.
Tungsten has a relatively small capture cross-section, so
this is a low-rate process, but over extended operation
the electrodes could become mildly radioactive.  This is
a maintenance concern (periodic replacement or
monitoring), not a safety concern (the activation levels
are low and the isotopes are short-lived).  Copper has
lower activation risk but lower density (weaker gamma
shielding).  The electrode material is an engineering
tradeoff between density, conductivity, and activation.

Heat from the electrodes (both from absorbed gammas and
from alpha particle impacts) can be extracted through
cooling channels on the back face, adding to the thermal
output.  This heat can feed into the same water circuit
as the jacket, keeping the thermal design simple.

### 18.3 Self-powering hybrid

The most elegant configuration: MHD provides direct
electricity that powers the IR pump and the electrolyzer.
If the MHD electrical output exceeds the pump + electrolyzer
input, the system is **electrically self-sustaining** — it
powers its own activation from its own output.

The thermal energy (absorbed in the water jacket from
gammas, neutrons, and thermalized kinetic energy) is then
the **net product** — available for heating, steam
generation, or additional electrical conversion.

Energy flow in the hybrid:

```
    MHD electrodes ──→ Electricity
         ↓                 ↓
    Powers IR pump    Powers electrolyzer
         ↓                 ↓
    Loads protons     Produces H₂
         ↓                 ↓
    Fusion ─────────→ Fast He-4 ions
         ↓                 ↓
    Gammas + neutrons → Water jacket → Heat (net output)
         ↓
    Back to MHD (cycle)
```

Break-even for the MHD self-powering loop:

> MHD efficiency × fusion output > pump input + electrolysis

At 60% MHD efficiency: 0.6 × 22.4 MeV = 13.4 MeV of
electricity per He-4.  Pump input is 1.6/η MeV.
Electrolysis is negligible (~0.002 MeV).  Self-powering
requires:

> 13.4 > 1.6/η → η > 1.6/13.4 ≈ **12%**

So with MHD self-powering, break-even for η rises from
7.1% (thermal harvest) to ~12% (electrical self-sustain).
Still a modest threshold.  If η exceeds 12%, the system
runs itself and produces net heat.

### 18.4 Comparison of direct conversion mechanisms

| Mechanism | How it works | Efficiency | Viability for this system |
|-----------|-------------|-----------|--------------------------|
| MHD | Fast He-4 ions in B field → Lorentz EMF | ~60–70% | Best fit — uses existing B field |
| Betavoltaic | Beta electrons on semiconductor junction | ~2–5% | Wrong reaction — this pathway consumes electrons |
| Alphavoltaic | Alpha particles on wide-gap semiconductor | ~10–20% | Possible but radiation damage limits lifetime |
| Direct charge collection | Alphas deposit charge on collector | ~high V, ~nA | Impractical — tiny current |
| Photoelectric from gammas | 2.2 MeV gamma ejects electrons | < 1% | Terrible efficiency, material damage |
| IR photocatalysis (chemical) | Tuned IR lowers activation energy | N/A | Different technology — chemical, not nuclear |

MHD is the clear winner for this application.


## 19. Containment details

### 19.1 Water jacket thickness

Water shielding attenuation for 2.224 MeV gammas:

| Water thickness | Attenuation | Adequate for |
|----------------|-------------|-------------|
| 15 cm (6") | ~10× | Reduced dose, not eliminated |
| 30 cm (12") | ~100× | Short-term proximity |
| 50 cm (20") | ~1,000× | Continuous occupancy nearby |
| 75 cm (30") | ~10,000× | Essentially zero dose at surface |

For a residential unit, a 75 cm (30") water jacket around
a small reaction chamber makes the exterior surface
radiation-free for all practical purposes.  The unit would
be roughly the size of a water heater — and it IS a water
heater, functionally.

For a benchtop research device at low power (low reaction
rate = fewer gammas per second), thinner shielding suffices
because the dose rate is proportional to the reaction rate.

### 19.2 Labyrinth containment

Gamma rays travel in straight lines.  They cannot turn
corners.  A **labyrinth** (zigzag entrance) for plumbing
penetrations ensures no gamma has a straight-line path from
the reaction zone to the exterior.

The design principle: if you cannot see the reaction chamber
by looking through the entrance (no line of sight), then
gammas cannot reach you.  Each bend in the labyrinth
absorbs gammas in the wall material.

This is standard nuclear engineering — reactor facilities
use labyrinth corridors for personnel access.  No door is
needed for radiation containment.  The bends do the work.

For this system: crooked pipes for hydrogen input and
helium output contain all gammas.  Water-filled walls at
each bend handle neutrons (which can scatter around
corners but lose energy at each bounce).  Two to three
bends with water-filled walls provide complete containment.

### 19.3 Monitoring

Water shielding can be self-monitoring.  A small amount of
scintillating dye added to the water jacket causes the
water to emit visible light when absorbing radiation.  The
intensity of the glow is proportional to the radiation
level.  You can literally see whether the shielding is
working — and whether the reaction is running — by looking
at the water.

A photodetector on the water jacket provides continuous,
passive radiation monitoring with no additional equipment.

### 19.4 Neutron fate in the water jacket

Neutrons entering the water jacket undergo two steps:

**Moderation.**  The fast neutron (~MeV) collides with
hydrogen nuclei (protons) in the water.  Each collision
transfers roughly half the neutron's energy — equal-mass
billiard balls.  After ~20 collisions, the neutron has
thermalized (kinetic energy ~0.025 eV, matching water
temperature).  The recoiling protons deposit their kinetic
energy as heat.

**Capture.**  The thermal neutron is captured by a hydrogen
nucleus:

> n + ¹H → ²H + γ (2.224 MeV)

The hydrogen becomes **deuterium**.  The 2.224 MeV gamma
is absorbed by the surrounding water as heat.  Both
products (deuterium, gamma-heated water) are stable and
non-radioactive.  Oxygen capture (n + ¹⁶O → ¹⁷O + γ) has
a cross-section ~1700× smaller and is negligible.

**The water jacket produces deuterium.**  This is a
secondary effect worth noting: the shielding water
slowly enriches itself with deuterium over time.
Deuterium is the fusion fuel discussed in §12.5 — it
already has a neutron component with a neutrino Compton
window.

At low reaction rates (benchtop), the accumulation is
negligible.  At industrial rates sustained over months
or years, the deuterium concentration in the jacket water
would grow measurably.  In principle, this enriched water
could eventually be cycled back as fuel — the shielding
becomes a slow fuel enrichment system.  This is not a
near-term design feature, but it is a pleasant
closed-loop property of the system: the waste product
from shielding (deuterium) is the feedstock for easier
fusion (deuterium already has the neutrino window).


---

## 20. Caution (final)

This entry builds on:

1. Neutron as three-sheet mode (R27 — established, quantitative)
2. Nuclei as Ma modes (R29 — established, < 1% agreement)
3. R39 electromagnetic results (established, quantitative)
4. Mode transition rates from σ_ep (NOT computed — conjectural)
5. Phase conjunction probability (NOT computed — conjectural)
6. Neutrino trigger mechanism §6 (NOT computed — speculative)
7. Cold fusion implications (highly speculative)
8. Threshold/loading theory (§11 — theoretically grounded in
   Planck 1911 and Reiter 2014, but loading on nuclear mode
   spectra is undemonstrated)
9. Virtual neutrino-sheet fluctuation on proton (§12.2 —
   physically motivated by QFT, but σ_νp value unknown)
10. The hydrogen-to-helium pathway (§12.4 — logically coherent,
    entirely speculative, no computation performed)
11. Linearity of the 1/α coupling (sim-impedance — established;
    eliminates nonlinear frequency mixing but permits loading)
12. Energy budget (§14.1 — established from measured nuclear
    masses; the 7.2× multiplication is not speculative)
13. Window cascade vs energy cascade distinction (§14.3 —
    logically sound; the gamma-to-Ma_p coupling calculation
    is straightforward but the conclusion depends on it)
14. Break-even efficiency threshold η > 7.1% (§14.5 —
    derived from the energy budget; whether η exceeds this
    depends on σ_νp and resonant enhancement, both unknown)
15. Output harvesting and shielding (§16, §19 — established
    nuclear engineering; water jacket, thermoelectric,
    labyrinth containment are standard technology)
16. System schematic and control (§16.5–16.7 — engineering
    design, contingent on the loading pathway working but
    using only known technology for the output side)
17. No runaway risk (§14.4, §16.5 — follows logically from
    pump-sustained vs self-sustaining; no critical mass)
18. MHD direct conversion (§18 — established physics of
    charged particles in magnetic fields; the Lorentz force
    is not speculative, but the power density in this
    application is unknown)
19. Self-powering hybrid (§18.3 — engineering design;
    requires η > 12% for electrical self-sustaining, or
    η > 7.1% with external electrical input)
20. Containment geometry (§19 — labyrinth, water thickness,
    scintillating dye monitoring — all standard nuclear
    engineering)

**Confidence tiers:**

| Tier | Items | Status |
|------|-------|--------|
| Established physics | 1, 2, 3, 11, 12, 15, 18, 20 | Measured, computed, or standard engineering |
| Computable but not yet computed | 4, 5, 9, 13 | Could be resolved by a study |
| Theoretically motivated, undemonstrated | 6, 8 | Require new physics or new experiments |
| Logically coherent, fully speculative | 7, 10, 14, 16, 19 | Depend on all prior items being correct |
| Follows from the design | 17 | No runaway risk if pump-sustained (not chain) |

**The three critical unknowns:**

1. **σ_νp** — determines whether the bootstrap works at all.
   If zero, only the deuterium seed pathway remains.
   Constrainable from the Ma metric.

2. **Loading viability** — can sub-threshold energy
   accumulate on nuclear mode spectra long enough to reach
   the 0.782 MeV threshold?  Depends on the Q factor of
   proton-sheet modes (how fast they leak energy back to 3D).
   Potentially computable from the lattice model.

3. **Coupling efficiency η** — what fraction of 42 μm IR
   pump energy actually reaches Ma_p through the neutrino
   channel?  Must exceed 7.1% for net energy gain (thermal
   harvest) or 12% for electrical self-sustaining (MHD
   hybrid).  Depends on σ_νp, resonant enhancement, and
   medium properties.  Not currently computable without σ_νp.

**The pathway is a chain of "ifs."**  If σ_νp ≠ 0, and if
loading works on nuclear mode spectra, and if η > 7.1%, then
the process is a net energy source with a 7× multiplication
factor controlled by pump power (no runaway risk).  If
η > 12%, the MHD hybrid self-powers and the net output is
thermal.  Each "if" is physically motivated but unproven.
The most economical next step is determining σ_νp from the
Ma metric — this resolves the first "if" and constrains the
third.
