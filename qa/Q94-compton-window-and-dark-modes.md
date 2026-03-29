# Q94: The Compton window — dark modes as dark matter and energy reservoir

**Status:** Open — testable with existing tools
**Study:** R42 (dark matter from ghost modes — charge cancellation and mass census)
**Related:**
  Q93 (relativistic effects — Paths 2 and 6 moved here),
  Q85 (threshold theory / energy accumulation on Ma),
  Q77 (ghost suppression),
  Q86 (three generations),
  R33 (ghost mode selection),
  R41 (dynamic model / low-pass filter),
  R28 (spectrum and predictive horizon),
  R35 (threshold detection and Ma-S coupling),
  R19 (shear-induced charge)

---

## The hypothesis

The physical dimensions of each Ma sheet define a resonant aperture
— a **Compton window** — between Ma and S.  A mode whose spatial
wavelength matches the sheet dimensions couples efficiently to S
and is observable as a particle.  A mode whose wavelength does not
match couples weakly or not at all.  Such modes still exist as valid
eigenstates with real mass-energy, but S cannot excite them, detect
them, or scatter off them through electromagnetic interactions.

These are not "ghost" modes (a problem to be solved).  They are
**dark modes** — a feature of the geometry.

---

## 1. The antenna analogy

An antenna of length L radiates efficiently at λ ≈ 2L and poorly
at other wavelengths.  The Ma sheet is an antenna into S:

- The sheet's ring circumference (2πR) and tube circumference (2πa)
  set the aperture size.
- The fundamental (1,2) mode's field pattern matches this aperture
  — it projects cleanly as a monopole (charge) and dipole (magnetic
  moment).
- Higher harmonics and off-resonance modes have complex field
  patterns that partially cancel when integrated over the aperture.
  Their net projection into S is suppressed.

This is already partially confirmed:
- **R19:** Charge requires |n₁| = 1.  Modes with |n₁| > 1 have
  oscillating fields that integrate to zero charge — the window
  filters out spatial frequencies that don't fit.
- **R21:** Parity selection rule — sin-like modes project charge,
  cos-like modes don't.  Another spatial filter.
- **R33 Track 8:** ω⁴ radiation efficiency gives the (1,1) ghost
  ~1/16× the electron's Larmor power.

What is new here is making this the **universal** coupling mechanism:
not just for charge, but for all interaction with S.  A mode that
doesn't fit the window has mass but is invisible to EM.


## 2. The Q factor of the Compton window

The antenna analogy is suggestive, but to make it quantitative the
window needs a **quality factor Q** — the ratio of center frequency
to bandwidth.  Q determines which modes fit through and which don't.

### What Q controls

A resonant aperture with quality factor Q centered on frequency ω₀
transmits modes within a bandwidth Δω ≈ ω₀/Q.  For the Compton
window:

- ω₀ = m_e c²/ℏ (the fundamental mode frequency)
- Δω = ω₀/Q (the passband)
- A mode at frequency ω couples with strength ~ 1/[1 + Q²(ω/ω₀ − ω₀/ω)²]

At Q ≈ 1 (no resonance), everything couples — no dark modes.
At Q → ∞ (perfect resonance), only the exact fundamental passes.
The physically interesting regime is Q ~ 10–100, where the
fundamental and nearby modes (muon, tau) pass but the (1,1) ghost
at ω/ω₀ ≈ 0.5 is strongly suppressed.

Note: R38 Track 5 already explored resonance capture with a cavity
Q factor and found that Q ≈ 30 naturally excludes a 4th generation
while keeping e, μ, τ.  The Compton window Q may be the same
quantity, now with a physical mechanism behind it.

### Candidate mechanisms for Q

The Q factor must arise from the geometry of the Ma/S interface.
Three candidates, in order of concreteness:

**Mechanism A: Impedance mismatch at the Ma/S boundary.**
The α-impedance model (R40) already proposes that the Ma wall
acts as a partially reflecting boundary with transmission
coefficient ~ α ≈ 1/137.  A partially reflecting cavity has
Q ∝ 1/T where T is the transmission per round trip.  For a
photon completing one full geodesic per Compton period:

    Q ~ 1/α ≈ 137

This would give a fractional bandwidth Δω/ω₀ ~ 1/137 ≈ 0.7%.
The (1,1) ghost at ω/ω₀ ≈ 0.5 would be suppressed by a factor
of ~ 1/[1 + 137²×(0.5 − 2)²] ≈ 2×10⁻⁵.  The muon at
ω/ω₀ ≈ 207 would also be far off-resonance — but the muon
lives on the SAME sheet with the SAME aperture, just at a
different mode.  The muon's own Compton wavelength defines its
own window on Ma_e.  So each visible mode may define its own
resonance, with Q ~ 137 for each.

**Mechanism B: Geometric form factor (multipole projection).**
The coupling of mode (n₁, n₂) to S depends on how much of
its field pattern survives integration over the torus surface.
The fundamental (1,2) has a net monopole (charge) and dipole
(magnetic moment).  Higher modes have higher multipoles that
fall off as r^(−ℓ−1) in the far field.  The effective Q is
set by the ratio of monopole to next-surviving multipole:

    Q_eff ~ (R_sheet / R_observation)^ℓ

At observation distances >> sheet size, only the monopole
survives, and the "Q" is effectively infinite for modes whose
lowest multipole is ℓ > 0.  This is not a single number but a
mode-dependent suppression factor — equivalent to computing
the window coupling W(n₁, n₂) from §1.

**Mechanism C: Evanescent coupling (waveguide below cutoff).**
If the Ma/S interface acts like a waveguide transition, modes
whose transverse wavelength exceeds the aperture size are
evanescent — they decay exponentially in the S direction with
a penetration depth δ ∝ λ.  The coupling strength goes as
exp(−d/δ) where d is an effective barrier width.

For a mode with n tube windings, the transverse wavelength
is λ_⊥ = 2πa/n.  The aperture "width" is set by the tube
circumference 2πa.  Modes with n > 1 have λ_⊥ < 2πa and
propagate; modes with n = 1 are at cutoff; modes with n < 1
don't exist.  This mechanism naturally explains the n₁ = ±1
selection (R19/R33) but gives Q = ∞ for |n₁| > 1 — too sharp.

### What determines Q: a computable test

The three mechanisms make different predictions for the mode-
dependence of the coupling:

| Mode | Mechanism A (Q~137) | Mechanism B (multipole) | Mechanism C (evanescent) |
|------|--------------------:|------------------------:|-------------------------:|
| (1,2) electron | 1 | 1 | 1 |
| (1,1) ghost | ~2×10⁻⁵ | depends on ℓ | 1 (same n₁) |
| (2,4) | ~2×10⁻⁵ | ~10⁻⁴ (quadrupole) | ~0 (evanescent) |
| (1,3) muon | ~10⁻⁴ | ~1 (same ℓ=0) | 1 (same n₁) |

Computing the actual projection integral W(n₁, n₂) for the
first ~20 modes would distinguish these mechanisms and pin
down the effective Q.  This is the most important near-term
calculation for Q94.


## 3. Dark modes as dark matter

If dark modes have mass but negligible EM coupling to S, they are
dark matter by definition.

### Mass spectrum

Dark matter would not be a single particle but a **forest of discrete
states** with a computable mass spectrum.  The spectrum is completely
determined by the Ma geometry — no new parameters.

- Lightest dark modes: sub-eV states on Ma_ν (neutrino sheet)
- Intermediate: MeV-scale modes on Ma_e (electron sheet)
- Heaviest (below 2 GeV): GeV-scale modes on Ma_p (proton sheet)

### Abundance ratio

Raw mode count below 2 GeV: ~900 total, ~40 visible.  Mode count
ratio ~860/40 ≈ 21.  The observed dark-to-visible matter ratio is
~5.4 by mass.

These are order-of-magnitude compatible.  The factor-of-4 gap can
be accounted for by:

1. **Mass weighting.**  Visible matter is dominated by the proton
   (938 MeV).  Many dark modes are lighter — the (1,1) ghost on Ma_e
   is ~0.26 MeV.  If the average dark mode mass is ~1/4 the average
   visible particle mass, the ratio drops from 21 to ~5.
2. **Stability.**  Some dark modes may decay to lighter dark modes
   plus radiation, reducing the count of stable species.
3. **The low-pass filter.**  R41 showed the dynamic model eliminates
   92% of modes (Category B — high tube harmonics).  If the window
   filter and the elastic low-pass filter work together, the effective
   dark mode count is reduced.

A quantitative test: enumerate all modes, compute masses, assume
a simple occupation model (equal, mass-weighted, or thermal), and
compute Σm_dark / Σm_visible.  If this lands near 5.4 for any
physically reasonable model, the hypothesis gains credibility.

### Interactions

- **Gravity:** Dark modes have mass → they curve spacetime.
  Gravitational interaction is automatic.
- **EM:** Suppressed by the window mismatch.  The residual coupling
  (the tail of the antenna pattern) determines the direct-detection
  cross-section.  This is computable and must be below current
  experimental bounds.
- **Self-interaction:** Dark modes on the same Ma sheet share the
  compact geometry and can interact via mode-mode coupling on Ma.
  This gives dark matter self-interactions — a feature that some
  astrophysical observations require (cusp-core problem, diversity
  problem in galaxy rotation curves).

### Testability

The mass spectrum is discrete, parameter-free, and computable.
A dark matter detection at a mass matching a predicted dark mode
(and not matching any known particle) would be a strong confirmation.
Conversely, a detection at a mass that does NOT match any Ma mode
would falsify this specific hypothesis.


## 4. Dark modes as threshold energy reservoir

This connects directly to Reiter's threshold theory (Q85, R35,
`papers/sub-quantum-memory.md`).

The threshold model proposes that a particle can accumulate energy
continuously between 1× and 2× its rest energy, invisible to
standard quantum measurements, until a threshold triggers a discrete
event (pair production at 2m_e).  The central question (Q85 §1) is:
WHERE does the sub-threshold energy go?

**Answer: dark modes.**

Dark modes are valid eigenstates of Ma with real energy, but they
don't couple to S.  They are invisible to standard measurements —
exactly the property threshold theory requires.  Energy absorbed by
a particle can distribute across the dark mode spectrum of its sheet:

- The dark modes share the same Ma geometry as the visible particle.
- Energy can flow into them via mode-mode coupling on Ma (internal
  to the compact space, invisible to S).
- The total capacity is bounded: when the total energy reaches 2m,
  the system has enough to excite a second copy of the fundamental
  → pair production.
- The distribution of energy across dark modes constitutes the
  "pre-load" state that Reiter's model requires.

### Energy regime distinction: sub-Compton vs. above-Compton

R35 and R37 concluded that threshold theory is not viable on the
electron or proton sheets because the thermal/biological energy
scale (~meV–eV) cannot bridge the ~MeV mode spacing on Ma_e.
That conclusion holds for low-energy perturbations from S.

**The above-Compton regime is different.**  A photon at or above
the electron Compton energy (~0.511 MeV) clears the energy barrier
and can in principle excite dark modes on Ma_e directly.  The
stiffness k_e ~ 10⁷ eV (R37 F10) blocks *geometric deformation*
of the sheet, not mode excitation at the right energy scale.  Once
you have enough energy to populate a mode, stiffness is irrelevant.

In this regime the governing filter is the Compton window W — the
projection integral of the dark mode's field pattern onto the Ma/S
aperture.  If W is small (as expected for dark modes), only a small
fraction W of above-Compton photon energy deposits into dark modes;
the remainder goes into ordinary Compton scattering or pair
production.  But even a small W, accumulated over many interactions,
constitutes threshold pre-loading invisible to S.

**Observational signature:** if above-Compton photons deposit a
fraction W of their energy into dark modes, the electron recoil
spectrum in Compton scattering would show a systematic energy
deficit relative to the Klein-Nishina prediction.  The Klein-Nishina
formula fits current data well, placing an upper bound on W for
Ma_e dark modes.  This is a computable and potentially falsifiable
constraint.

The same argument applies to Ma_p, shifted to the GeV scale
(proton Compton energy ~938 MeV), where deep inelastic scattering
already shows complex inelastic structure that MaSt's dark modes
could partially account for.

### Information storage

If the dark mode spectrum is dense (hundreds of states per sheet),
the pattern of energy distributed across them encodes information
(Q85 §8, Q31).  Each dark mode is a bit (or analog value) of
sub-quantum storage.  This resolves the question raised in R35:
what physical degrees of freedom hold the pre-load pattern?

### The neutrino sheet as information substrate

Ma_ν has ~1,000 dark modes below its pair-production threshold
(R38 F6).  These are particularly interesting because:
- The neutrino sheet is large (~μm scale) — modes are densely spaced
- Coupling between sheets (σ_eν, σ_νp cross-shears) allows energy
  to flow from visible particles into neutrino dark modes
- R35 Track 2 showed viable read/write timescales (~70 ps write,
  ~3 ps read)
- The modes are thermally stable (THz frequencies, well above
  room-temperature noise)

This makes the neutrino sheet dark mode spectrum a candidate for
biological information storage (Q78–Q83).


## 5. Ghosts are a feature, not a bug

The ghost mode problem has been treated as the model's central
embarrassment — ~900 predicted modes vs ~40 observed.  The Compton
window reinterprets this:

| What was called | What it actually is |
|-----------------|---------------------|
| Ghost modes | Dark modes — dark matter candidates |
| The ghost problem | The dark matter solution |
| Over-prediction of particles | Prediction of DM mass spectrum |
| Sub-threshold energy storage | Energy in dark modes |
| Information capacity of Ma | Number of available dark modes |

The model doesn't predict too many particles.  It predicts the right
number of visible particles PLUS a specific dark matter spectrum
PLUS a mechanism for sub-quantum energy storage.  The "excess" modes
do three jobs at once.


## 6. Computable predictions

All of these are accessible with existing tools or modest extensions:

| Prediction | How to compute | Depends on |
|------------|---------------|------------|
| Window Q factor | Projection integral W(n₁,n₂) for ~20 modes; distinguish mechanisms A/B/C | R19 charge integral, Ma geometry |
| Dark mode mass spectrum | Enumerate modes, classify by window coupling | Q factor + Ma geometry |
| DM/visible mass ratio | Sum masses × occupation model | Mode spectrum + cosmology |
| Residual EM cross-section | Overlap integral of mode pattern with fundamental | R19 charge integral extended |
| Lightest stable dark mode | Enumerate, check decay channels | Mode spectrum |
| Self-interaction strength | Mode-mode coupling on Ma | R22 coupling matrix |
| Threshold capacity (bits) | Count dark modes per sheet | Mode spectrum |
| Pre-load distribution | Energy partition across dark modes | Coupling matrix + thermodynamics |


## 7. Key questions

1. **What is Q?**  Compute the projection integral W(n₁, n₂) for
   ~20 modes.  Fit a Lorentzian or appropriate response curve.
   Extract Q.  Does it match 1/α ≈ 137 (Mechanism A), or is it
   mode-shape-dependent (Mechanism B)?

2. **What is the window coupling factor for each mode?**  Define
   W(n₁, n₂) as the overlap integral between mode (n₁, n₂) and the
   fundamental (1,2) on the embedded torus.  W = 1 for the
   fundamental, W → 0 for high harmonics.  What is W for the (1,1)
   ghost?

3. **Does the mass-weighted dark/visible ratio match observation?**
   Enumerate all modes below 2 GeV.  Compute
   Σ(m × f(W)) / Σ(m × (1−f(W))) where f is a visibility function.
   Compare to 5.4.

4. **Is the lightest dark mode consistent with warm/cold DM bounds?**
   If the lightest stable dark mode is sub-keV, it may be ruled out
   as warm dark matter unless it has additional suppression.

5. **Can dark modes decay?**  If dark-to-dark decay channels exist,
   the spectrum evolves over cosmological time.  The final stable
   dark spectrum might be very different from the initial one.

6. **Does dark mode energy contribute to the cosmological constant?**
   Zero-point energy of dark modes contributes to vacuum energy.
   Is this related to the cosmological constant problem?

---

## Priority

This question should be investigated before further attempts at
ghost suppression (which may be solving the wrong problem).

Recommended sequence:
1. Determine the Q factor: compute the projection integral W(n₁, n₂)
   for the first ~20 modes to distinguish mechanisms A/B/C (§2)
2. With Q in hand, classify all modes below 2 GeV as visible/dark
3. Compute mass-weighted dark/visible ratio, compare to 5.4
4. Check cosmological consistency (freeze-out, warm DM bounds)
5. If viable, connect to threshold capacity calculation (Q85, R35)
