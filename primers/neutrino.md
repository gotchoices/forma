# Neutrinos

What we know, what we don't, and what we measure — written
for an engineer encountering neutrino physics for the first
time.

---

## 1. What a neutrino is

A neutrino is the lightest known massive particle.  It has
no electric charge, no color charge (the "charge" of the
strong force), and interacts with other matter only through
the **weak force** and gravity.  This makes it extraordinarily
difficult to detect: a typical neutrino can pass through a
light-year of solid lead without interacting.

About 400 trillion solar neutrinos pass through your body
every second.  You never notice.

Neutrinos come in three **flavors**: electron (νₑ), muon
(νμ), and tau (ντ).  Each flavor is defined operationally
— not by some intrinsic label on the neutrino, but by which
charged particle appears when the neutrino interacts:

| Flavor | Produced with | Example reaction |
|--------|--------------|-----------------|
| νₑ | Electron or positron | Neutron decay: n → p + e⁻ + ν̄ₑ |
| νμ | Muon | Pion decay: π⁺ → μ⁺ + νμ |
| ντ | Tau | Tau decay (rare, requires high energy) |

Each flavor has an antiparticle (ν̄ₑ, ν̄μ, ν̄τ).
Whether neutrinos and antineutrinos are truly distinct
particles or the same particle in two states (the
Dirac vs Majorana question) is unknown — see §7.


## 2. Core concepts

Several terms from quantum mechanics appear throughout
neutrino physics.  This section defines them in plain
language before they're needed.

### Eigenstates and eigenvalues

An **eigenstate** of some quantity (mass, energy, flavor)
is a state where measuring that quantity gives one definite
answer every time.  The definite value you get is the
**eigenvalue**.

Example: a particle in a "mass eigenstate with eigenvalue
0.05 eV" will always measure 0.05 eV if you weigh it.
A particle NOT in a mass eigenstate will sometimes measure
0.05 eV, sometimes 0.009 eV, sometimes 0.05 eV again —
probabilistically.

The word "eigen" is German for "own" or "characteristic."
A mass eigenstate is a state with its own characteristic
mass.

**Why this matters for neutrinos:** neutrinos have two
relevant sets of eigenstates that are NOT the same:

- **Mass eigenstates** (ν₁, ν₂, ν₃): states with definite
  mass.  These propagate through space in a simple way —
  each one travels with a definite frequency determined
  by its mass.

- **Flavor eigenstates** (νₑ, νμ, ντ): states with definite
  flavor.  These are what get produced and detected,
  because the weak interaction creates a definite flavor.

A neutrino cannot be in both a mass eigenstate and a flavor
eigenstate at the same time.  A νₑ (definite flavor) is a
mixture of ν₁, ν₂, and ν₃ (indefinite mass).  A ν₂
(definite mass) is a mixture of νₑ, νμ, and ντ
(indefinite flavor).

**Measurement forces a choice.**  Detecting a neutrino via
a charged-current interaction (§8) forces it into a flavor
eigenstate — the flavor becomes definite.  But this
necessarily makes the mass indefinite.  The neutrino then
propagates as a superposition of mass eigenstates again,
each component accumulating phase at a different rate.
This produce-propagate-detect cycle is what drives
oscillation.

**This is the same structure as the uncertainty principle.**
Position and momentum are "conjugate" quantities: measuring
one precisely makes the other uncertain.  Flavor and mass
are conjugate in the same way.  A neutrino with definite
flavor has uncertain mass; one with definite mass has
uncertain flavor.  You cannot pin down both.

### Superposition

**Superposition** means a state is described as a sum of
other states with specific amplitudes.  When we write:

> νₑ = 0.82 ν₁ + 0.54 ν₂ − 0.15 ν₃

this means: a νₑ is 82 parts ν₁, 54 parts ν₂, and 15
parts ν₃ (roughly — the actual coefficients come from the
PMNS matrix).  The squares of these amplitudes give the
probability of finding each mass eigenstate if you were
to "measure the mass" of a νₑ.

The amplitudes are **complex numbers** — they carry both a
magnitude (how much) and a **phase** (a clock-like angle
that advances over time).  The phase is critical: if
superposition were just a set of probabilities (real
numbers), the components couldn't interfere and there
would be no oscillation.  The oscillation IS the beating
between the phases of the three components as they drift
at different rates.

### Mixing angles

The relationship between the flavor basis and the mass
basis is a **rotation** in an abstract 3D space.  A mixing
angle is literally a rotation angle.

In two dimensions: if you have two coordinate systems (x,y)
and (x',y') rotated by angle θ relative to each other, then
any vector can be described in either system using sin θ and
cos θ.  A "mixing angle" of θ = 0° means the two systems
are aligned — each flavor IS a mass eigenstate, and no
oscillation occurs.  A mixing angle of 45° means maximum
mixing — each flavor is a 50/50 combination of two mass
eigenstates.

In three dimensions, you need three rotation angles to
relate two coordinate systems (just like Euler angles for
orienting a rigid body).  The neutrino mixing angles
θ₁₂, θ₂₃, θ₁₃ are these three rotations:

| Angle | Value | What it rotates |
|-------|-------|----------------|
| θ₁₂ ≈ 33° | Large | ν₁ ↔ ν₂ (solar sector) |
| θ₂₃ ≈ 49° | Near-maximal | ν₂ ↔ ν₃ (atmospheric sector) |
| θ₁₃ ≈ 8.6° | Small | ν₁ ↔ ν₃ (reactor sector) |

The rotation matrix that converts between the two bases is
the **PMNS matrix** (Pontecorvo-Maki-Nakagawa-Sakata).  It
is parameterized by these three angles plus one CP-violating
phase δ (see §6).

**A striking fact:** unlike quarks, where the equivalent
matrix (CKM) is nearly diagonal (small mixing, angles of
~2°, ~2°, ~0.2°), neutrino mixing angles are large.  The
flavor and mass bases are substantially rotated relative to
each other.  Why neutrinos mix so much more than quarks is
an open question.


## 3. What we observe

This section covers the experimental facts — what detectors
actually measure, separated from theoretical interpretation.

### Flavor change in flight

A neutrino produced as νₑ (identified by the electron in the
production reaction) can be detected as νμ (identified by
the muon in the detection reaction) after traveling some
distance.  The probability of this flavor change depends on
two variables:

- **L:** the distance traveled (baseline), in km
- **E:** the neutrino's energy, in GeV

The measured oscillation probability follows a specific
pattern:

<!-- P(νₑ → νμ) = sin²(2θ) sin²(1.267 Δm² L / E) -->
$$
P(\nu_e \to \nu_\mu) = \sin^2(2\theta)\,
\sin^2\!\left(\frac{1.267\,\Delta m^2\, L}{E}\right)
$$

(simplified two-flavor version).  The probability oscillates
sinusoidally as a function of L/E, with an amplitude set by
the mixing angle θ and a frequency set by Δm² (a parameter
with units of eV²).

### Two distinct oscillation frequencies

The oscillation pattern contains two distinct frequencies,
revealed by experiments at different L/E ratios:

| Splitting | Δm² (eV²) | Oscillation length (1 GeV) |
|-----------|-----------|--------------------------|
| Solar (1↔2) | 7.53 × 10⁻⁵ | ~33,000 km |
| Atmospheric (2↔3) | 2.45 × 10⁻³ | ~1,000 km |

The atmospheric splitting is ~33× larger than the solar
splitting.  At any given L/E, typically only one frequency
is visible — the other is either too fast to resolve (it
averages out) or too slow to have developed.

### Different experiments, different parameters

The experiment's L/E ratio determines which splitting it
measures:

| Experiment type | L | E | Sensitive to |
|----------------|---|---|-------------|
| Solar | 1.5 × 10⁸ km | ~1–10 MeV | θ₁₂, Δm²₂₁ |
| Reactor ~180 km (KamLAND) | 180 km | ~3 MeV | θ₁₂, Δm²₂₁ |
| Reactor ~1 km (Daya Bay) | 1 km | ~3 MeV | θ₁₃, Δm²₃₁ |
| Atmospheric | 15–13,000 km | ~1–10 GeV | θ₂₃, Δm²₃₂ |
| Accelerator (T2K, NOvA) | 300–800 km | ~1 GeV | θ₂₃, θ₁₃, δ_CP |

### Matter effects

Neutrinos oscillate differently when passing through dense
matter (the Sun, the Earth).  Electron neutrinos experience
an extra interaction — forward scattering off electrons in
the medium — that muon and tau neutrinos do not (because
the medium contains electrons but not muons or taus).  This
extra interaction modifies the effective mixing angle and
oscillation frequency.

At a critical density (the **MSW resonance**, named for
Mikheyev, Smirnov, and Wolfenstein), the effective mixing
becomes maximal regardless of the vacuum mixing angle.
This is what happens inside the Sun: νₑ produced in the
dense core undergo a smooth conversion as they travel
outward through decreasing density.

Matter effects have determined one fact that oscillation
in vacuum cannot: **m₂ > m₁** (the sign of Δm²₂₁ is
positive).


## 4. How the oscillation is modeled

The experimental observations in §3 are well described by
a specific theoretical framework.  This section explains
that framework and notes where it is a model rather than
a direct observation.

### The superposition model

The standard explanation for neutrino oscillation:

1. A neutrino is produced in a flavor eigenstate (e.g., νₑ).
2. This flavor state is a superposition of three mass
   eigenstates (ν₁, ν₂, ν₃), as specified by the PMNS
   matrix.
3. Each mass eigenstate propagates with a slightly different
   frequency, because at the same momentum p, a heavier
   component has slightly more energy: E ≈ p + m²/(2p).
4. Over distance L, the three components accumulate phase
   at different rates.  The phase difference between
   components i and j after distance L is:

   > Δφᵢⱼ = (m²ᵢ − m²ⱼ) L / (2E) = Δm²ᵢⱼ L / (2E)

5. At the detector, the changed phase relationships produce
   a different flavor mixture than what was emitted.

**What is directly observed vs what is modeled:**

| Element | Status |
|---------|--------|
| Flavor change occurs | Observed (many experiments) |
| Oscillation depends on L/E | Observed |
| Two distinct Δm² values | Observed |
| Three mixing angles | Measured (fit to data) |
| Flavor states = superposition of mass states | Model (fits all data, but this is a framework, not a direct observation) |
| PMNS matrix is 3×3 unitary | Assumed (consistent with data; would break if sterile neutrinos exist) |
| Three and only three light neutrinos | Strongly supported (Z boson width measures N_ν = 2.984 ± 0.008) |

The superposition model is not in any experimental trouble
— it fits all data with high precision.  But it is a
theoretical framework applied to the observations, not itself
an observation.  An alternative framework that reproduces the
same oscillation pattern (same L/E dependence, same Δm²
values, same mixing angles) would be experimentally
indistinguishable.

### The three-frequency picture

An equivalent and sometimes more intuitive description:
the neutrino is a compound signal with three frequency
components.  Each component has a slightly different
frequency (determined by its mass).  As the signal
propagates, the three components drift in and out of
phase — like three tuning forks at slightly different
pitches producing a slow beat pattern.

The "flavor" of the neutrino at any point is determined
by the instantaneous phase relationship between the three
components.  When the phases align one way, it looks like
νₑ; aligned another way, νμ; a third way, ντ.

This is mathematically identical to the superposition model.
The Δm² values set the beat frequencies.  The mixing angles
set the amplitudes of the three components.  Whether you
call the components "mass eigenstates in superposition" or
"frequency components of a compound signal" is a matter of
language, not physics.


## 5. The mass eigenstates

### What is measured

Oscillation experiments measure only **mass-squared
differences**, not absolute masses:

| Parameter | Value | Meaning |
|-----------|-------|---------|
| Δm²₂₁ | (7.53 ± 0.18) × 10⁻⁵ eV² | m₂² − m₁² |
| \|Δm²₃₂\| | (2.453 ± 0.033) × 10⁻³ eV² | \|m₃² − m₂²\| |
| Ratio | ~33 | The atmospheric splitting is ~33× the solar |

This is a fundamental limitation: oscillation depends on
phase differences between components, not absolute phases.
You can measure how far apart the frequencies are, but not
the frequencies themselves.

### Mass ordering

The sign of Δm²₂₁ is known (positive, from MSW effects in
the Sun): **m₂ > m₁**.

The sign of Δm²₃₂ is NOT known.  Two possibilities:

**Normal ordering (NO):** m₁ < m₂ < m₃.  Two light states
close together, one heavier state well above.  Currently
preferred at 2–3σ.

**Inverted ordering (IO):** m₃ < m₁ < m₂.  One light state
below, two heavier states close together above.

### Absolute mass scale

The lightest neutrino could be massless.  Current
constraints:

| Source | Constraint |
|--------|-----------|
| Minimum Σm (normal ordering, lightest = 0) | ~59 meV |
| Minimum Σm (inverted ordering, lightest = 0) | ~100 meV |
| Cosmology (Planck + BAO) | Σm < 120 meV |
| Direct measurement (KATRIN, tritium endpoint) | m_β < 800 meV |

The cosmological bound is already squeezing the inverted
ordering, whose minimum sum (~100 meV) is close to the
limit.  Next-generation experiments aim for ~40 meV
sensitivity.


## 6. What is NOT known

| Question | Status | Path to resolution |
|----------|--------|-------------------|
| Absolute mass scale | Only Δm² measured | KATRIN, Project 8, cosmology |
| Mass ordering (normal vs inverted) | Normal preferred, 2–3σ | JUNO, DUNE |
| CP phase δ_CP | Hints of ~200°, not definitive | DUNE, Hyper-K |
| Dirac vs Majorana (see §7) | Unknown | Neutrinoless double beta decay |
| Sterile neutrinos | Anomalies exist, contested | Short-baseline experiments |
| Why masses are so small | No accepted explanation | Theoretical |
| Why mixing angles are so large | Unknown | Theoretical |

### The CP phase

In addition to the three mixing angles, the PMNS matrix
has a **CP-violating phase** δ_CP.  If δ_CP ≠ 0 and ≠ 180°,
then neutrinos and antineutrinos oscillate at different
rates:  P(νₑ → νμ) ≠ P(ν̄ₑ → ν̄μ).  This asymmetry between
matter and antimatter in the neutrino sector could help
explain why the universe contains more matter than antimatter.

Current hints from T2K favor δ_CP near 270° (maximal CP
violation), but the measurement is not definitive.  The
DUNE experiment is designed to settle this.


## 7. The Dirac vs Majorana question

Every other known fermion (electron, quark, etc.) is a
**Dirac particle**: the particle and antiparticle are
distinct.  An electron is not a positron.  They differ in
charge sign, which provides an unambiguous label.

The neutrino is unique: it has no charge.  This means there
is no charge label to distinguish neutrino from antineutrino.
Two possibilities exist:

**Dirac neutrino:** ν and ν̄ are still distinct, distinguished
by some other quantum number (lepton number).  There exist
right-handed neutrinos and left-handed antineutrinos, but
they don't interact via the weak force and have never been
observed.

**Majorana neutrino:** ν and ν̄ are the same particle.  What
we call "antineutrino" is just the neutrino in the opposite
spin state.  Lepton number is not conserved.

### How to tell the difference

The test is **neutrinoless double beta decay** (0νββ).
Certain nuclei undergo double beta decay:

> (A, Z) → (A, Z+2) + 2e⁻ + 2ν̄ₑ   (standard, observed)

If neutrinos are Majorana, the two neutrinos can annihilate
internally:

> (A, Z) → (A, Z+2) + 2e⁻   (neutrinoless — no ν emitted)

The signature: in standard double beta decay, the two
electrons share the energy with the neutrinos (continuous
spectrum).  In neutrinoless, the two electrons carry ALL
the energy (sharp peak at the Q-value).

Current best limit (KamLAND-Zen): half-life > 2.3 × 10²⁶
years.  No signal observed yet.


## 8. Neutrino interactions and detection

### Why detection is so hard

Neutrinos interact only via the weak force.  The
cross-section for a typical MeV-scale neutrino is
~10⁻⁴⁴ cm².  A photon interacting with an atom has
cross-section ~10⁻²⁴ cm² — twenty orders of magnitude
larger.

The mean free path of a 1 MeV neutrino in water is about
3 light-years.  Even in lead, it's about 1 light-year.

To detect neutrinos, experiments use enormous target masses
(thousands of tons) and count rare events.  A typical solar
neutrino experiment detects a few events per day out of
~10¹⁴ neutrinos passing through per second.

### Interaction types

**Charged-current (CC):** the neutrino converts into its
partner charged lepton via W boson exchange:

> νₑ + n → e⁻ + p
> νμ + n → μ⁻ + p

The outgoing lepton identifies the flavor.  This is how
flavor is defined experimentally.

**Neutral-current (NC):** the neutrino scatters via Z boson
exchange and remains a neutrino:

> ν + N → ν + X

NC interactions are identical for all flavors and cannot
identify which flavor participated.  SNO used NC on
deuterium to measure the total neutrino flux regardless
of flavor.

### Detection technologies

| Technology | Examples | Strengths |
|-----------|---------|-----------|
| Water Cherenkov | Super-K, SNO, Hyper-K | Huge volumes, directional, cheap per ton |
| Liquid scintillator | Daya Bay, KamLAND, JUNO | Excellent energy resolution (~3% at 1 MeV) |
| Liquid argon TPC | MicroBooNE, DUNE | Detailed 3D images of interactions |
| Ice Cherenkov | IceCube | 1 km³ volume, highest-energy neutrinos (TeV–PeV) |


## 9. Key numbers

### Masses and mixing

| Parameter | Value |
|-----------|-------|
| Δm²₂₁ (solar) | 7.53 × 10⁻⁵ eV² |
| \|Δm²₃₂\| (atmospheric) | 2.453 × 10⁻³ eV² |
| θ₁₂ (solar) | 33.4° |
| θ₂₃ (atmospheric) | 49° |
| θ₁₃ (reactor) | 8.6° |
| δ_CP | ~194° (poorly constrained) |
| Σm (cosmological limit) | < 120 meV |
| N_eff (light species count) | 2.984 ± 0.008 |

### Cross-sections

| Energy | Cross-section | Mean free path (water) |
|--------|--------------|----------------------|
| 1 MeV | ~6 × 10⁻⁴⁴ cm² | ~3 light-years |
| 1 GeV | ~7 × 10⁻³⁹ cm² | ~20 AU |
| 1 TeV | ~7 × 10⁻³⁶ cm² | ~3 × 10⁶ km |

### Solar neutrino flux

The Sun emits ~6.5 × 10¹⁰ neutrinos per cm² per second
at Earth's distance.

| Source | Flux (cm⁻² s⁻¹) | Max energy |
|--------|-----------------|-----------|
| pp | 6.0 × 10¹⁰ | 420 keV |
| ⁷Be | 4.9 × 10⁹ | 862 keV (line) |
| pep | 1.4 × 10⁸ | 1.44 MeV (line) |
| ⁸B | 5.5 × 10⁶ | ~15 MeV |
| CNO | ~5 × 10⁸ | ~1.7 MeV |

### Other notable numbers

- **Cosmic neutrino background:** ~336 relic neutrinos per
  cm³ (from the Big Bang, temperature ~1.95 K).  Never
  directly detected.

- **SN 1987A:** 24 neutrino events detected from a supernova
  168,000 light-years away — confirming that ~99% of a
  supernova's energy is emitted as neutrinos (~3 × 10⁵³ erg).


---

## Appendix: A brief history

**1930 — Pauli proposes the neutrino.**  Beta decay seemed
to violate energy, momentum, and spin conservation.  The
electron's energy was continuous (not sharp as expected for
two-body decay), and the spins didn't balance.  Pauli
proposed an invisible neutral particle to carry the missing
energy and spin.

**1956 — Cowan and Reines detect the neutrino** using a
nuclear reactor source.  They identified inverse beta decay
(ν̄ₑ + p → e⁺ + n) by its two-pulse signature: prompt
positron annihilation followed ~5 μs later by neutron
capture.

**1968–2001 — The solar neutrino problem.**  Ray Davis
measured solar neutrinos in the Homestake mine and
consistently found only ~1/3 of the predicted flux.  For 30
years, nobody could determine whether the Sun's model or the
experiment was wrong.

**1998 — Super-Kamiokande discovers oscillation.**  Muon
neutrinos coming up through the Earth (13,000 km path) were
depleted compared to those from above (15 km path).  Electron
neutrinos showed no such asymmetry.  The pattern fit
νμ → ντ oscillation.

**2001 — SNO resolves the solar problem.**  Using heavy water,
SNO measured the total neutrino flux (all flavors via
neutral-current) and found it matched predictions exactly.
The electron neutrinos were converting to other flavors, not
disappearing.  The solar model was right.  The neutrinos were
oscillating.

**2012 — Daya Bay measures θ₁₃.**  The last unknown mixing
angle, measured at 8.6° — nonzero, meaning CP violation in
the neutrino sector is in principle observable.

**2015 — Nobel Prize** to Kajita (Super-K) and McDonald (SNO)
for discovering neutrino oscillation.


---

## References

- Particle Data Group, neutrino mixing review (pdg.lbl.gov)
- NuFIT collaboration, global oscillation fits (nu-fit.org)
