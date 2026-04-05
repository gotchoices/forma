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

Neutrinos come in three **flavors**: electron (ν_e), muon
(ν_μ), and tau (ν_τ).  Each flavor is defined operationally
— not by some intrinsic label on the neutrino, but by which
charged particle appears when the neutrino interacts:

| Flavor | Produced with | Example reaction |
|--------|--------------|-----------------|
| ν_e | Electron or positron | Neutron decay: n → p + e⁻ + ν̄_e |
| ν_μ | Muon | Pion decay: π⁺ → μ⁺ + ν_μ |
| ν_τ | Tau | Tau decay (rare, requires high energy) |

Each flavor has an antiparticle (ν̄_e, ν̄_μ, ν̄_τ).
Whether neutrinos and antineutrinos are truly distinct
particles or the same particle in two states (the
Dirac vs Majorana question) is unknown.


## 2. Why neutrinos matter

Neutrinos are the only known particles that change identity
in flight.  An electron neutrino produced in the Sun can
arrive at Earth as a muon or tau neutrino.  This phenomenon
— **neutrino oscillation** — proved that neutrinos have mass,
which the original Standard Model did not predict.

The discovery of oscillation won two Nobel Prizes (2015:
Kajita for atmospheric oscillation at Super-Kamiokande,
McDonald for solar oscillation at SNO) and opened some of
the deepest questions in physics:

- Why are neutrino masses so small (at least 500,000× lighter
  than the electron)?
- Do neutrinos violate CP symmetry (behave differently from
  antineutrinos)?  This could help explain why the universe
  has more matter than antimatter.
- Are neutrinos their own antiparticles?


## 3. A brief history

**1930 — Pauli proposes the neutrino.**  Beta decay (n → p +
e⁻) seemed to violate energy, momentum, and spin conservation
simultaneously.  The electron's energy spectrum was continuous
(not a single sharp line as expected for a two-body decay),
and the spins didn't add up.  Pauli proposed an invisible
neutral particle to carry the missing energy and spin.  He
called it the "neutron" (the actual neutron hadn't been
discovered yet); Fermi later renamed it the "neutrino"
(little neutral one).

**1956 — Cowan and Reines detect the neutrino.**  Using a
nuclear reactor as a source (reactors produce ~10²⁰
antineutrinos per second per gigawatt), they detected inverse
beta decay: ν̄_e + p → e⁺ + n.  The signature was a
"delayed coincidence" — a prompt positron annihilation
(two 511 keV gammas) followed ~5 μs later by neutron capture
on cadmium (~9 MeV gamma cascade).  This two-pulse pattern
was distinctive enough to extract from backgrounds.

**1968–2001 — The solar neutrino problem.**  Ray Davis built a
detector in the Homestake gold mine (615 tons of dry cleaning
fluid) and measured solar neutrinos via ν_e + ³⁷Cl → ³⁷Ar +
e⁻.  He consistently found only ~1/3 of the predicted flux.
For over 30 years, nobody could determine whether the Sun's
model was wrong, the experiment was wrong, or something was
happening to the neutrinos in transit.

**1998 — Super-Kamiokande discovers oscillation.**  A 50,000-ton
water detector in Japan measured atmospheric neutrinos (produced
by cosmic rays hitting the upper atmosphere).  Muon neutrinos
coming from below (having traveled ~13,000 km through the
Earth) were depleted compared to those from above (~15 km path).
Electron neutrinos showed no such asymmetry.  The pattern fit
ν_μ → ν_τ oscillation precisely.

**2001 — SNO resolves the solar problem.**  The Sudbury
Neutrino Observatory, using 1,000 tonnes of heavy water (D₂O),
could measure three separate reactions:

| Reaction | Sensitive to | Result |
|----------|-------------|--------|
| ν_e + d → p + p + e⁻ (charged-current) | Only ν_e | ~1/3 of predicted flux |
| ν + d → p + n + ν (neutral-current) | All flavors equally | Full predicted flux |
| ν + e⁻ → ν + e⁻ (elastic) | All, but ν_e enhanced | Intermediate |

The neutral-current measurement proved that the total neutrino
flux from the Sun was exactly as predicted — the electron
neutrinos were converting to muon and tau neutrinos in transit.
The solar model was vindicated.  The neutrinos were oscillating.


## 4. Neutrino oscillation

### The basic idea

Neutrinos are produced and detected as **flavor states**
(ν_e, ν_μ, ν_τ) — defined by which charged lepton
appears in the interaction.  But they propagate through
space as **mass states** (ν₁, ν₂, ν₃) — states of
definite mass.

These are not the same basis.  Each flavor state is a
quantum-mechanical superposition of all three mass states:

> |ν_e⟩ = U_e1 |ν₁⟩ + U_e2 |ν₂⟩ + U_e3 |ν₃⟩

The coefficients U form the **PMNS matrix** (Pontecorvo-Maki-
Nakagawa-Sakata) — a 3×3 unitary matrix that converts between
the two bases.

### Why they oscillate

As a neutrino travels distance L with energy E, each mass
component accumulates phase at a rate proportional to its
mass squared:

> φ_i = m²_i L / (2E)

Because the three masses are different, the three components
drift out of phase with each other.  When the neutrino is
detected (in the flavor basis), the changed phase
relationships produce a different flavor mixture than what
was emitted.

The oscillation probability in the two-flavor approximation
(which works well when one mass splitting dominates):

<!-- P(ν_α → ν_β) = sin²(2θ) sin²(Δm² L / 4E) -->
$$
P(\nu_\alpha \to \nu_\beta) = \sin^2(2\theta)\,
\sin^2\!\left(\frac{\Delta m^2 L}{4E}\right)
$$

In practical units (L in km, E in GeV, Δm² in eV²):

<!-- P = sin²(2θ) sin²(1.267 Δm² L / E) -->
$$
P = \sin^2(2\theta)\,
\sin^2\!\left(\frac{1.267\,\Delta m^2\, L}{E}\right)
$$

**What this says physically:** the oscillation probability
depends on the ratio L/E — longer distances or lower energies
give more oscillation.  The oscillation length (one full
cycle) is:

> L_osc ≈ 2.48 × E(GeV) / Δm²(eV²) km

For the atmospheric splitting (Δm² ≈ 2.5 × 10⁻³ eV²): a
1 GeV neutrino oscillates over ~1,000 km.  For the solar
splitting (Δm² ≈ 7.5 × 10⁻⁵ eV²): a 3 MeV neutrino
oscillates over ~100 km.

### The PMNS matrix parameters

The PMNS matrix has four physical parameters: three mixing
angles and one CP-violating phase.

**θ₁₂ ≈ 33.4° (solar angle).**  Governs ν_e ↔ ν₁/ν₂
mixing.  Measured by solar neutrino experiments and the
KamLAND reactor experiment (180 km baseline).  This angle
determines how much of ν_e is in ν₁ vs ν₂.

**θ₂₃ ≈ 49° (atmospheric angle).**  Governs ν_μ ↔ ν_τ
mixing.  Measured by atmospheric neutrino experiments and
accelerator experiments (T2K at 295 km, NOvA at 810 km).
It is close to 45° — meaning ν₃ is approximately an equal
mixture of ν_μ and ν_τ.  Whether it is exactly 45° or
slightly above (the "octant" question) is not resolved.

**θ₁₃ ≈ 8.6° (reactor angle).**  The smallest angle.
Measured precisely by reactor experiments (Daya Bay, RENO)
in 2012.  It connects ν₃ to ν_e.  Its nonzero value was
crucial — if θ₁₃ were zero, CP violation in the neutrino
sector would be unobservable.

**δ_CP (CP-violating phase).**  If δ_CP ≠ 0 and ≠ π, then
P(ν_α → ν_β) ≠ P(ν̄_α → ν̄_β) — neutrinos and
antineutrinos oscillate differently.  Current hints from
T2K favor δ_CP near −π/2 (maximal CP violation), but the
measurement is not definitive (2–3σ).  The DUNE experiment
is designed to measure this.

### Why different experiments measure different parameters

The key: the experiment's L/E ratio determines which Δm²
it is sensitive to.

| Experiment type | L | E | L/E | Sensitive to |
|----------------|---|---|-----|-------------|
| Solar | 1.5 × 10⁸ km | ~1–10 MeV | ~10¹⁰ km/GeV | θ₁₂, Δm²₂₁ |
| Reactor ~180 km (KamLAND) | 180 km | ~3 MeV | ~6 × 10⁴ km/GeV | θ₁₂, Δm²₂₁ |
| Reactor ~1 km (Daya Bay) | 1 km | ~3 MeV | ~300 km/GeV | θ₁₃, |Δm²₃₁| |
| Atmospheric | 15–13,000 km | ~1–10 GeV | ~10–10⁴ km/GeV | θ₂₃, |Δm²₃₂| |
| Accelerator (T2K, NOvA) | 300–800 km | ~0.6–2 GeV | ~300–500 km/GeV | θ₂₃, θ₁₃, δ_CP |

The two mass splittings differ by a factor of ~33, so at
any given L/E, typically only one oscillation frequency is
significant.  The other either averages out (too fast to
resolve) or hasn't had time to develop (too slow).  This
natural separation is why the two-flavor approximation works
so well for individual experiments.

### Matter effects (MSW)

When neutrinos travel through matter (the Sun, the Earth),
their oscillation is modified.  The reason: electron
neutrinos experience an additional interaction that muon and
tau neutrinos do not — **charged-current forward scattering**
off the electrons in the material.  The medium contains
electrons but not muons or taus, so ν_e gets an extra
effective potential:

> V = √2 × G_F × N_e

where G_F is the Fermi constant and N_e is the electron
number density.

This potential modifies the effective mixing angle and mass
splitting.  At a specific density (the **MSW resonance**),
the effective mixing becomes maximal regardless of the
vacuum mixing angle.  This is what happens to high-energy
solar neutrinos: they are produced in the dense core where
the density exceeds the resonance density, and they undergo
an adiabatic conversion as they travel through the
decreasing density toward the surface.  They emerge
predominantly as ν₂ (the heavier of the 1-2 pair).

Matter effects are important for two reasons:

1. They established that m₂ > m₁ (the sign of Δm²₂₁ is
   positive), because the resonance occurs for neutrinos
   only if the heavier state has a larger ν_e component.

2. They provide a way to determine the mass ordering
   (normal vs inverted), because the resonance in the
   atmospheric sector occurs for neutrinos in normal
   ordering but for antineutrinos in inverted ordering.
   This is how DUNE plans to resolve the ordering.


## 5. The mass eigenstates

### What is measured

Oscillation experiments measure only **mass-squared
differences**, not absolute masses:

| Parameter | Value | What it means |
|-----------|-------|--------------|
| Δm²₂₁ | (7.53 ± 0.18) × 10⁻⁵ eV² | Difference between ν₂² and ν₁² (solar splitting) |
| |Δm²₃₂| | (2.453 ± 0.033) × 10⁻³ eV² | Difference between ν₃² and ν₂² (atmospheric splitting) |
| Ratio | Δm²₃₁/Δm²₂₁ ≈ 33.6 | The atmospheric splitting is ~33× the solar splitting |

The sign of Δm²₂₁ is known to be positive (from MSW effects
in the Sun).  The sign of Δm²₃₂ is NOT known — this is the
mass ordering question.

### Normal vs inverted ordering

**Normal ordering (NO):** m₁ < m₂ < m₃.  Two light states
close together, one heavier state above.  Currently preferred
at 2–3σ.

**Inverted ordering (IO):** m₃ < m₁ < m₂.  One light state,
two heavier states close together above.

The ordering matters because it determines the pattern of
masses, affects matter oscillation, and constrains the
parameter space for neutrinoless double beta decay.

### Absolute mass scale

The lightest neutrino could in principle be massless.  The
minimum total mass is:

| Ordering | Minimum Σm | Individual masses (if lightest = 0) |
|----------|-----------|-------------------------------------|
| Normal | ~59 meV | m₁ ≈ 0, m₂ ≈ 8.7 meV, m₃ ≈ 50.3 meV |
| Inverted | ~100 meV | m₃ ≈ 0, m₁ ≈ 49.5 meV, m₂ ≈ 50.3 meV |

**Cosmological bound:** Planck + BAO gives Σm < 120 meV
(95% CL).  This already squeezes the inverted ordering
(minimum ~100 meV) and some analyses push the bound below
100 meV, which would exclude IO.

**Laboratory bound:** KATRIN (tritium endpoint) gives
m_β < 800 meV (90% CL), not yet sensitive to the expected
range.  Next-generation experiments aim for ~40 meV.


## 6. What is NOT known

| Question | Status | How it could be resolved |
|----------|--------|------------------------|
| Absolute mass | Only Δm² measured | KATRIN, Project 8, cosmology |
| Mass ordering | Normal preferred, 2–3σ | JUNO, DUNE, atmospheric experiments |
| CP phase δ_CP | Hints of ~−π/2, not definitive | DUNE, Hyper-K |
| Dirac vs Majorana | Unknown | Neutrinoless double beta decay (0νββ) searches |
| Sterile neutrinos | Anomalies exist, interpretation contested | Short-baseline program at Fermilab |
| Origin of mass | Why so small? Seesaw? Higgs? | Theoretical — no direct experimental path yet |

### The Dirac vs Majorana question

If neutrinos are **Dirac** particles (like electrons), then
neutrinos and antineutrinos are distinct and lepton number
is conserved.  If they are **Majorana** particles, they are
their own antiparticles — the first known fundamental
particle with this property.

The test: **neutrinoless double beta decay** (0νββ).  Certain
nuclei can undergo double beta decay: (A,Z) → (A,Z+2) + 2e⁻
+ 2ν̄_e.  If neutrinos are Majorana, the two neutrinos can
annihilate internally, giving (A,Z) → (A,Z+2) + 2e⁻ with
no neutrinos emitted.  The signature: the two electrons carry
ALL the decay energy (a sharp peak), vs the continuous
spectrum of the standard two-neutrino mode.

Current best limits (KamLAND-Zen): half-life > 2.3 × 10²⁶
years.  Next-generation experiments aim for sensitivity to
the entire inverted-ordering parameter space.


## 7. Neutrino interactions

### Why they're so hard to detect

Neutrinos interact only via the weak force.  The cross-section
for a typical MeV-scale neutrino is ~10⁻⁴⁴ cm².  For
comparison, a photon interacting with an atom has cross-section
~10⁻²⁴ cm² — twenty orders of magnitude larger.

The mean free path of a 1 MeV neutrino in water is about
**3 light-years**.  Even in lead, it's about 1 light-year.
Neutrinos from the Sun pass through the entire Earth at night
with negligible absorption.

To detect neutrinos despite these tiny cross-sections,
experiments use enormous target masses (thousands of tons) and
wait for the rare interactions.  A typical solar neutrino
experiment detects a few events per day out of the ~10¹⁴
neutrinos passing through it per second.

### Interaction types

**Charged-current (CC):** the neutrino exchanges a W boson
and converts into its corresponding charged lepton:

> ν_e + n → e⁻ + p
> ν_μ + n → μ⁻ + p
> ν_τ + n → τ⁻ + p

The outgoing charged lepton identifies the neutrino flavor.
This is how flavor is defined operationally.

**Neutral-current (NC):** the neutrino exchanges a Z boson
and remains a neutrino:

> ν + N → ν + X (hadronic products)

NC interactions are identical for all three flavors — they
cannot identify the flavor.  SNO used NC on deuterium to
measure the total neutrino flux (all flavors combined).

### Detection technologies

**Water Cherenkov** (Super-K, SNO, Hyper-K): charged
particles moving faster than light in water emit Cherenkov
radiation in a cone.  Electrons produce fuzzy rings
(electromagnetic showering); muons produce sharp rings.
This allows flavor identification.  Very large and
relatively inexpensive per ton.

**Liquid scintillator** (Daya Bay, KamLAND, JUNO, Borexino):
organic liquid that emits light when a charged particle
deposits energy.  Much higher light yield than Cherenkov,
giving excellent energy resolution (~3% at 1 MeV).  No
directional information.

**Liquid argon TPC** (MicroBooNE, DUNE): ionization charges
drift in an electric field to wire planes, providing
detailed 3D images of interactions.  Excellent particle
identification.  Technically challenging at large scale.

**Ice Cherenkov** (IceCube): 1 km³ of Antarctic ice
instrumented with photomultipliers.  Sensitive to neutrinos
from ~100 GeV to beyond PeV — the highest-energy neutrinos
ever detected.


## 8. Key numbers

### Masses and mixing

| Parameter | Value |
|-----------|-------|
| Δm²₂₁ (solar) | 7.53 × 10⁻⁵ eV² |
| |Δm²₃₂| (atmospheric) | 2.453 × 10⁻³ eV² |
| θ₁₂ (solar) | 33.4° |
| θ₂₃ (atmospheric) | 49° |
| θ₁₃ (reactor) | 8.6° |
| δ_CP | ~194° (poorly constrained) |
| Σm (cosmological limit) | < 120 meV |
| N_eff (number of light species) | 2.984 ± 0.008 (consistent with 3) |

### Cross-sections and mean free paths

| Energy | Cross-section | Mean free path in water |
|--------|--------------|------------------------|
| 1 MeV | ~6 × 10⁻⁴⁴ cm² | ~3 light-years |
| 1 GeV | ~7 × 10⁻³⁹ cm² | ~3 × 10⁹ km (~20 AU) |
| 1 TeV | ~7 × 10⁻³⁶ cm² | ~3 × 10⁶ km |

### Solar neutrino flux

The Sun emits ~6.5 × 10¹⁰ neutrinos per cm² per second
at Earth's distance — predominantly from the pp fusion
reaction.  About 400 trillion neutrinos pass through a
human body every second.

The dominant components:

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


## 9. Connection to MaSt

In the MaSt framework, the three neutrino mass eigenstates
correspond to three standing-wave modes (n₃, n₄) on the
neutrino material sheet (Ma_ν) — a 2D torus with
circumferences at the micrometer scale.

Key MaSt-specific questions:

- **Why is the neutrino neutral?**  Two candidate
  explanations: the sheet is too large for the phase
  winding to couple (Q102), or the sheet has zero/near-zero
  shear (no circulation symmetry breaking).  See R49.

- **What is the oscillation mechanism?**  Standard physics:
  pure phase evolution.  MaSt adds a possibility: actual
  energy redistribution between modes on Ma_ν through the
  Compton window, making oscillation a physical process
  rather than abstract interference.

- **What selects the three observed modes?**  On a torus,
  many mode triplets can match the Δm² ratio of 33.6.
  Whether the selection comes from filtering (waveguide
  cutoff), production dynamics (β-decay populates only
  certain modes), or topological constraints is under
  investigation (R49).

- **The Δm² ratio as a constraint.**  The ratio
  Δm²₃₁/Δm²₂₁ ≈ 33.6 directly constrains which mode
  triplets on the torus are viable, which in turn constrains
  the sheet geometry (aspect ratio ε_ν and shear s₃₄).


---

## References

Standard physics references:
- Particle Data Group, neutrino mixing review (pdg.lbl.gov)
- NuFIT collaboration, global oscillation fits (nu-fit.org)

Project references:
- R49: [`studies/R49-neutrino-filter/`](../studies/R49-neutrino-filter/)
- Q102: [`qa/Q102-neutrino-neutrality-from-sheet-size.md`](../qa/Q102-neutrino-neutrality-from-sheet-size.md)
- Prior neutrino studies: R24, R25, R26 (mode assignments and
  geometry constraints)
