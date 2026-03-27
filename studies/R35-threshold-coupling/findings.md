# R35 Findings

## Track 1 — Threshold detection statistics

### F1. Compton asymmetry makes Cd-109 insensitive to pre-load

At 88 keV, the Compton max transfer is only 25.6%.  Detector 2
always receives ≥ 74.4% of E_γ, which exceeds the SCA lower level
(66.7%).  Det 2 fires on EVERY interaction event regardless of
pre-load.

Because both the enhanced coincidence rate (Re) and the det-1
singles rate (S1) are proportional to P(det 1 fires), this
probability cancels in the ratio:

    Re/Rc = 1/(2τR) ≈ 1667

independent of the pre-load distribution.  This over-predicts
Reiter's Cd-109 result (Re/Rc = 33) by 51×.

### F2. Na-22 (511 keV) is genuinely pre-load-sensitive

At 511 keV, η_max = 2/3.  Det 2 receives as little as 1/3 of
E_γ after maximum Compton scatter, which is below the SCA lower
level.  BOTH detectors need pre-load to fire.  Re/Rc depends
strongly on the pre-load distribution:

| Pre-load distribution | Re/Rc |
|-----------------------|-------|
| Uniform(0, 0.30)     | 400   |
| Uniform(0, 0.40)     | 848   |
| Uniform(0, 0.45)     | 997   |
| Uniform(0, 0.50)     | 1108  |
| Exp(mean = 0.20)     | 1318  |
| Beta(2, 5)           | 1432  |

A uniform distribution with max ≈ 0.43 × E_γ matches Reiter's
Na-22 Re/Rc ≈ 963.

### F3. The SCA upper limit resolves the Cd-109 over-prediction

The dynamic equilibrium Monte Carlo — where pre-loads evolve via
continuous filling and leakage — reproduces Cd-109 when atoms are
nearly fully loaded (⟨E_pre⟩/E_th ≈ 0.98).

At high pre-load, the SCA UPPER limit becomes active: total energy
E_pre + E_dep exceeds the photopeak window, rejecting events.  This
suppresses both singles and coincidences, bringing Re/Rc down from
1667 to ~33.

| fill_rate | leak_rate | ⟨preload⟩ | Re/Rc |
|-----------|-----------|-----------|-------|
| 0.010     | 10⁻⁵      | 0.976     | 33.5  |
| 0.010     | 10⁻⁴      | 0.977     | 34.8  |
| 0.010     | 10⁻³      | 0.977     | 33.5  |

The mechanism: most atoms are nearly fully loaded; only atoms with
moderate pre-load (neither too high nor too low) can produce a pulse
within the SCA window.  The fill_rate/leak_rate ratio determines
the steady-state pre-load level and hence Re/Rc.

### F4. Cd-109 and Na-22 probe different physics

The two isotopes constrain the model differently:

- **Cd-109 (88 keV):** Probes the SCA upper limit mechanism.
  The pre-load must be nearly maximal (⟨E_pre⟩ ≈ 0.98 E_th)
  for the model to work.  Re/Rc ≈ 33 requires that most atoms
  are "nearly full."

- **Na-22 (511 keV):** Probes the pre-load distribution shape.
  The pre-load must be moderate (⟨E_pre⟩ ≈ 0.4 E_th for the
  parametric model).  Re/Rc ≈ 963 requires that enough atoms
  have pre-load above the coincidence threshold, but not so
  many that Re/Rc saturates at 1/(2τR).

### F5. Joint constraint creates tension

Matching BOTH results simultaneously with the SAME physical
parameters requires energy-dependent scaling.  The absolute
fill rate (keV/s) should be identical in both experiments
(same detector material, same environment).  In normalized
units (fraction of E_γ):

| Isotope | E_γ (keV) | Required ⟨E_pre⟩/E_γ |
|---------|-----------|----------------------|
| Cd-109  | 88        | ~0.98                |
| Na-22   | 511       | ~0.40                |

In absolute keV: Cd-109 needs ⟨E_pre⟩ ≈ 86 keV, while Na-22
needs ⟨E_pre⟩ ≈ 204 keV.  These are DIFFERENT absolute pre-loads,
which is physically plausible if the source contributes to the
fill rate (higher-energy gammas deposit more energy per event).

With the same absolute fill rate, the dynamic MC gives Na-22
Re/Rc ≈ 1200–1300 (vs. Reiter's 963).  A 30% discrepancy —
in the right ballpark but not a clean match.

### F6. The fill_rate/leak_rate ratio is the master parameter

The dynamic MC shows that Re/Rc is controlled by the steady-state
mean pre-load ⟨E_pre⟩/E_th.  This in turn depends on the ratio
fill_rate / leak_rate:

- High ratio → ⟨E_pre⟩ → 1 → SCA UL cuts in → low Re/Rc
- Low ratio → ⟨E_pre⟩ → 0 → no threshold events → Re/Rc = 0
- Moderate ratio → intermediate ⟨E_pre⟩ → Re/Rc ≈ 1/(2τR)

The Cd-109 match (Re/Rc ≈ 33) requires ⟨E_pre⟩ ≈ 0.98, which
means fill_rate ≫ leak_rate (atoms fill up much faster than they
leak).  The storage lifetime 1/leak_rate is not tightly constrained
by Track 1 alone — any leak_rate ≤ 10⁻³ per event interval works.

### F7. Connection to R35 Tracks 3–4

Track 1 establishes:

1. **The threshold model CAN reproduce Reiter's Cd-109 (Re/Rc ≈ 33)**
   via the SCA upper limit mechanism — but requires ⟨E_pre⟩/E_th ≈ 0.98.

2. **Na-22 (Re/Rc ≈ 963)** constrains the pre-load distribution:
   uniform max ≈ 0.43 E_γ, or exponential mean ≈ 0.3–0.4 E_γ.

3. **The master parameter is fill_rate/leak_rate.**  Track 3
   (cross-shear leakage) determines leak_rate.  Track 4 (coupling
   strength) determines fill_rate.  Together they predict whether
   the steady-state ⟨E_pre⟩ falls in the range needed for Cd-109.

4. **The SCA window width is critical.**  The upper limit mechanism
   depends on whether Reiter's actual SCA window was tight enough
   to reject events at ~1.5× E_γ.  This is an experimental detail
   that could be verified from Reiter's original setup description.


## Track 3 — Cross-shear leakage rate

### F8. Neutrino modes are exactly uncharged (topological)

Charge on T⁶ is Q = −n₁ + n₅.  Neutrino modes have n₁ = n₅ = 0,
so Q = 0 EXACTLY.  Cross-shear changes the metric (eigenvalues)
but not the eigenfunctions (plane waves on a flat torus).  Charge
is topological, not geometric.

EM radiation rate: Γ_EM = 0 to all orders in σ_eν.
EM leakage is not a mechanism — ever.

### F9. Cross-shear shifts energies but does not mix modes

On a flat T⁶, modes are exact plane waves exp(i n·θ) regardless
of the metric.  Cross-shear modifies mode energies:

| σ_eν | Fractional shift δE/E |
|-------|----------------------|
| 0.001 | 2.1 × 10⁻⁶          |
| 0.01  | 2.1 × 10⁻⁴          |
| 0.05  | 5.4 × 10⁻³          |

The shift is proportional to σ_eν² and independent of mode
number — all modes shift by the same fraction.

### F10. Coupling matrix elements are tiny

The energy coupling V = ñ_e · δ(G̃⁻¹) · ñ_ν between neutrino
and electron modes is ~10⁻¹⁰ MeV² (for σ_eν = 0.01).  The
mixing coefficient c_mix = V/(E_ν² − E_e²) is ~10⁻⁹ because
the energy gap is enormous: E_e ≈ 0.5 MeV vs E_ν ≈ 0.03 meV
(ratio ~10⁷).

This gap makes ALL cross-sheet processes exponentially or
algebraically suppressed.

### F11. Thermal disruption — the candidate leakage mechanism

Naive kinetic model:

    γ_per_atom = f_collision × σ_eν² × exp(−ΔE/kT)
    γ_collective = γ_per_atom / N_atoms
    τ_store = 1/γ_collective

| σ_eν  | τ_store (f = 10¹²/s)  |
|--------|-----------------------|
| 0.001  | 3.2 years             |
| 0.005  | 46 days               |
| 0.01   | 12 days               |
| 0.02   | 2.9 days              |
| 0.05   | 11 hours              |

CAVEAT: This model assumes each thermal collision has
probability σ_eν² of affecting the neutrino-sheet state.
The actual mechanism is unclear — see F12.

### F12. The thermal coupling mechanism is an open question

The naive model assumes direct R³ → T²_ν coupling with
probability σ_eν².  But the physical coupling chain is:

    R³ thermal → electron T² → (σ_eν) → neutrino T²

Step 1 requires bridging a ~MeV energy gap (electron mode
spacing) with ~meV thermal energy.  This is Boltzmann-
suppressed by exp(−MeV/meV) ≈ 0.

If the thermal-to-neutrino pathway must go through the
electron sheet, the storage lifetime is exponentially longer
than the naive model — potentially geological or longer.

Possible alternative pathways:

(a) Phonon-metric coupling: atomic vibrations modulate the
    T⁶ metric, directly exciting neutrino modes.  Rate
    depends on the metric's "stiffness" (unknown).

(b) Direct R³ × T⁶ coupling through dimensional reduction.
    Uncharged modes couple gravitationally (negligible) or
    through unidentified mechanisms.

(c) Collective oscillation: the 10¹⁴-atom domain's
    neutrino state may have observable R³ effects that
    couple to the thermal bath.

This is the deepest open question in the storage program.

### F13. Three-layer protection

The neutrino-sheet state is protected by:

1. **Charge immunity** (exact): Q = 0, EM coupling = 0.
2. **Energy gap** (~10⁷ ratio): electron sheet at MeV,
   neutrino sheet at meV.  Thermal cross-talk requires
   bridging this gap.
3. **Collective averaging**: 10¹⁴ atoms per domain.
   Individual disruptions are negligible.

Combined: even the naive model gives biologically relevant
lifetimes (hours to years).  The energy-gap suppression
(F12) could extend this to geological timescales.

### F14. Storage lifetime is mode-independent

All neutrino modes have the same fractional energy shift
from cross-shear (δE/E ∝ σ_eν², independent of n₃, n₄).
All modes leak at the same rate.  Information encoded in
mode PATTERNS is uniformly protected — no vulnerable modes.

### F15. Protection is direction-independent (inside = outside)

The three-layer protection applies equally to radiation
originating INSIDE the neutrino domain (e.g., from the
co-located cell nucleus):

**Layer 1 (charge immunity):** topological, not spatial.
Q = 0 is a property of the mode's winding numbers,
independent of where the EM field originates.

**Layer 2 (energy gap):** energetic, not directional.
Sources inside the cell:

| Source              | Energy    | Can reach e-sheet? |
|---------------------|-----------|-------------------|
| DNA chemistry       | 1–5 eV   | No (need MeV)     |
| Metabolic (ATP)     | 0.1–1 eV | No                |
| Thermal vibrations  | 27 meV   | No                |
| K-40 decay          | 1.3 MeV  | Yes (but rare)    |

K-40: ~1 decay per cell per 300 years.  Each decay ionizes
~40,000 atoms.  With σ_eν² ≈ 10⁻⁴, that's ~4 ν-sheet
disruptions per decay on a 10¹⁴-atom domain — negligible.

**Layer 3 (collective):** no perimeter.  The domain is a
volume (~42 μm), not a shell.  The nucleus (~5–10 μm) is
fully embedded.  All atoms are equal members regardless
of position.

### F16. Shielding is symmetric: blocks reading equally

On a flat T⁶, mode energies are properties of the GEOMETRY,
not of which modes are occupied.  The neutrino-sheet quantum
state does not affect any electron-sheet observable.  No R³
measurement can detect the neutrino pattern.

This means:
- Writing is blocked (energy can't reach the ν-sheet)
- Reading is blocked (ν-state doesn't affect observables)
- Co-resonance is blocked (two cells with different ν-states
  are electromagnetically identical)

The flat T⁶ gives perfect retention + zero I/O.

### F17. The elastic torus (Hypothesis I) breaks the symmetry

If the neutrino-sheet occupation modulates the geometry
(elastic torus, Q85 §8a), then the state DOES affect
observables:

    ν-state → δr_ν → δE_electron → δ(molecular vibrations)

This bypasses all three protection layers because the
mechanism is GEOMETRIC, not electromagnetic:

- Charge immunity: irrelevant (geometry, not charge)
- Energy gap: bypassed (geometry change is adiabatic,
  no energy transfer across the MeV gap)
- Collective: actually HELPS (10¹⁴ atoms shift together
  → amplified geometric signal)

Both writing and reading become possible through the
same geometric channel:

**Writing:** molecular forces → geometry change →
  ν-state change.  Biochemistry inside the cell directly
  modulates the torus shape.

**Reading (co-resonance):** ν-state → geometry →
  molecular vibration spectrum.  Two cells with the same
  ν-pattern have matching vibration frequencies → resonance.
  Different patterns → frequency mismatch → no resonance.
  Operates at meV molecular scale; MeV gap irrelevant.

**Asymmetry:** writing requires energy input from
  biochemistry (active, inside the cell).  Reading is
  passive (sympathetic resonance, can cross cell
  boundaries).  This gives exactly the architecture a
  biological storage system needs: active internal write,
  passive external read, shielded from noise.

### F18. The Goldilocks parameter shifts

In the flat T⁶, the Goldilocks tradeoff was:
  σ_eν large → fast I/O but short lifetime
  σ_eν small → long lifetime but no I/O

In the elastic torus, the tradeoff shifts to the metric
stiffness K (compliance of the torus geometry):
  K small (stiff) → good retention, slow I/O
  K large (floppy) → fast I/O, noisy retention

The stiffness K replaces σ_eν as the master parameter.
Computing K requires the moduli potential of the T⁶
geometry — connected to the moduli stabilization problem
in string theory (Q85 §8a).

### F19. Coulomb field is the monopole projection of compact-dimension structure

The static electric field of a charged particle at
r >> λ_C = 2πR is the l=0 (monopole) term of a
multipole expansion over the compact T² coordinates.
The mode on the torus has angular structure ~ e^{i(n₁θ₁ + n₂θ₂)},
producing a field that is NOT uniform around the torus.

At r >> λ_C, only the total charge (integral over θ₁, θ₂)
survives — giving the symmetric 1/r² Coulomb law.  The
angular structure is invisible.

At r ~ λ_C, higher multipoles become resolvable.  These
are the KK tower: excited compact-dimension modes with
masses m_n ~ n/R ~ n × m_particle.  The field deviates
from 1/r² and encodes the torus topology (winding numbers,
shear).

The non-linearity arises because the KK gauge field comes
from the Einstein equations on the compact space, which
are non-linear.  At r >> R, linearized → Maxwell →
Coulomb.  At r ~ R, full non-linear geometry matters.

In the T⁶ model, R = λ_C/2π by construction.  The compact
structure becomes resolvable at EXACTLY the quantum-
mechanical Compton scale.  This is automatic, not a
coincidence — the compactification radius IS the Compton
wavelength.

Provocative question: could the known QED corrections at
the Compton scale (Uehling potential, vacuum polarization)
be KK tower effects?  Both appear at the same scale
(r ~ λ_C).  If they match, then QED radiative corrections
= compact-dimension geometry.  Computable (see Q85 §8a).

### F20. Neutrino-sheet modes project non-uniform voltage on the cell membrane

The neutrino Compton wavelength (≈ 42 μm) matches the cell
diameter.  A neutrino mode (n₃, n₄) is a standing wave
across the ~42 μm domain.  Higher harmonics have shorter
spatial wavelengths.

The cell membrane sits at the domain boundary and samples
this standing-wave pattern.  Through the elastic torus
(F17), different membrane positions experience different
geometric modulations → different electron-sheet energies
→ non-uniform voltage.

The voltage pattern on a single cell's membrane encodes
the harmonic content of the occupied neutrino modes:
- Fundamental (lowest winding): one lobe across the cell
- Higher harmonics: multiple nodes, finer structure
- Superposition of occupied modes: complex, information-
  rich 2D pattern on the membrane surface

The information capacity of this pattern is vastly greater
than a single scalar voltage:
- Scalar Vmem: ~1 number per cell (Levin's resolution)
- T⁶ prediction: thousands of harmonic coefficients,
  each encoding a mode occupation number

This is consistent with the Q85 §13 capacity estimate.

Important caveat: the neutrino modes are uncharged (F8).
The voltage pattern arises INDIRECTLY:
  ν-state → (elastic torus) → local geometry variation →
  charged-particle energy shifts → non-uniform E field
This requires the elastic torus hypothesis (F17).  On
a flat T⁶, the pattern is invisible (F16).

### F21. Connection to Levin: scalar Vmem vs. harmonic voltage map

Levin measures membrane voltage at cell-level resolution
across tissues: spatial patterns of Vmem where each cell
has one scalar value (-70 to +40 mV).  He observes that
these patterns are instructive for morphogenesis and
survive events that should destroy them.

The T⁶ model predicts that the information content is
MUCH richer than Levin's current resolution captures:
the voltage on a single cell's membrane has sub-cellular
spatial structure encoding the full neutrino mode
occupation.  Levin's scalar Vmem is the AVERAGE of
this rich pattern — the DC component, discarding all
AC harmonics.

This explains his results in the T⁶ framework:
- Vmem patterns ARE instructive (they encode neutrino-
  sheet information)
- The information survives cell death (the ν-sheet is
  the primary store, not the cells)
- But Levin's resolution doesn't reveal the full
  information content

Testable prediction: sub-micron voltage imaging of a
single cell's membrane should reveal specific harmonic
content — not random noise — with spatial frequencies
corresponding to the neutrino mode spectrum.

Writing via membrane voltage: Levin shows that changing
Vmem reprograms cell fate.  In the T⁶ picture:
  ΔVmem → changed ionic forces → mechanical stress →
  (elastic torus) → geometry modulation → ν-state change
This makes Vmem an indirect write channel to the
neutrino sheet, consistent with Levin's experimental
observation that voltage IS instructive.


## Track 4 — Coupling strength estimate

### F22. Flat T⁶ coupling is exactly zero

On a flat T⁶, the neutron-gateway coupling chain
(EM → e-T² → σ_eν → ν-T²) is broken at every step:

1. Neutrino modes are exactly uncharged (F8): Q = 0.
2. Cross-shear does not mix modes (F9): eigenstates
   remain exact plane waves.
3. The MeV gap blocks thermal coupling (F12):
   exp(-MeV/meV) ≈ 0.

The EM coupling g_flat = 0 (exact, to all orders in σ_eν).
No Goldilocks window exists on a flat T⁶.

### F23. The elastic torus shifts coupling from EM to geometry

Molecular forces → geometry change (δs₃₄ or δr_ν) →
neutrino mode energy shift → mode hop.  This bypasses
all three protection layers because the mechanism is
geometric, not electromagnetic:

- Charge immunity: irrelevant (no EM involved)
- Energy gap: bypassed (geometry change is adiabatic)
- Collective: HELPS (amplifies the geometric signal)

### F24. Shear channel dominates; Goldilocks is thermodynamic

Modes with n₃ = 0 are r_ν-independent (insensitive to
aspect ratio changes).  Modes with n₃ ≠ 0 respond to
s₃₄ with ∂E/∂s₃₄ ≈ E₀ ≈ 29 meV per unit shear.

Because ∂E/∂s₃₄ ≈ mode spacing, the Goldilocks condition
reduces to a purely thermodynamic criterion:

    mode_hops = K × F_energy × (amplification factor)

where the amplification factor ≈ 46.6 (ratio of |∂E/∂s|
to the actual minimum mode spacing of ~0.6 meV at r_ν=100).

The criterion for a Goldilocks window: F_write / kT > 10.

### F25. Read SNR is independent of compliance K

Both signal and noise scale with K → K cancels:
    SNR_single = E_mode / kT ≈ 1–3
    SNR_collective = √N × E_mode / kT ≈ 10⁷

Reading is ALWAYS viable with collective enhancement.
No constraint on K from read.  Even the lowest mode
(E ~ 29 meV) has collective SNR ~ 10⁷.

### F26. Passive vibrations cannot write

Molecular vibrations (50 meV) vs thermal noise (27 meV)
gives F/kT = 1.9 — far below the threshold of 10.
No value of K allows writing with passive vibrations while
retaining the stored state against thermal noise.

Ion channel gating (70 meV): F/kT = 2.6 — also insufficient.

### F27. ATP-driven write opens a Goldilocks window

ATP hydrolysis (0.5 eV) vs kT (27 meV) gives F/kT = 18.7,
exceeding the threshold of 10.

Goldilocks window: K ∈ [0.043, 0.080] eV⁻¹  (span 1.8×).
At mid-window (K ≈ 0.06), each ATP event shifts by ~1.4
mode hops — fast compared to biological timescales given
the ~10¹⁰ ATP/cell/s metabolic rate.

Biological predictions:
- Dead cells cannot write (no ATP) but can be read
- Metabolically active cells write faster
- Anesthesia (reduced ATP turnover) slows writing
- Writing is an active, ATP-consuming process
- The stored pattern persists without metabolic maintenance
  (retention is passive, protected by F13)

### F28. The metric compliance K is the master parameter

K must be in [0.043, 0.080] eV⁻¹ for ATP-driven storage.
Computing K from first principles requires the moduli
potential of the T⁶ geometry — the central open question
connecting this model to string theory's moduli
stabilization problem.


## Track 2 — Write/read dynamics (elastic torus reframing)

The original Track 2 was framed as a damped driven oscillator
(ä + γȧ + ω₀²a = gF) with EM coupling g.  Tracks 3–4
established g = 0 (F22) and that the elastic torus is the
I/O mechanism (F23).  Track 2 is therefore reframed around
stochastic mode hopping driven by ATP events, opposed by
thermal disruption.

### F29. Storage capacity: 10–324 bits per cell

Two capacity measures at r_ν = 100, with modes up to
E_max = 2m₁₂ ≈ 116 meV:

| Measure | Channels | Bits |
|---------|----------|------|
| Energy-bin (lower bound) | 5 thermally distinct | 10 |
| Pattern (upper bound) | 324 modes ON/OFF | 324 |

The lower bound groups modes into bins of width kT ≈ 27 meV;
only 5 bins fit below E_max.  The upper bound treats each
mode (n₃, n₄) as a binary channel, detectable through the
2D voltage map (F20).  True capacity depends on whether the
read mechanism resolves individual mode patterns or only
total energy.  Capacity is r_ν-INDEPENDENT above r_ν ~ 50
(the mode spectrum converges).

### F30. Write time: ~70 ps per mode hop

At K = 0.06 (mid-Goldilocks), each ATP event causes ~1.4
mode hops.  With R_ATP ≈ 10¹⁰/s:

    write rate ≈ 1.4 × 10¹⁰ hops/s
    τ(1 hop) ≈ 69 ps
    τ(full pattern, 5 channels) ≈ 344 ps

Writing is fast compared to ALL biological timescales.
The cell rewrites its entire ν-sheet pattern ~10⁹ times
per second.

### F31. Read time: ~3 ps per channel

SNR_collective = √N_atoms × E_mode/kT ≈ 10⁷ (K-independent,
confirming F25).  The read time is set by the molecular
vibration Q factor:

    τ_read ~ Q / f_vibration ~ 30 / 10¹³ Hz ≈ 3 ps

The write/read asymmetry is complete:
    Write: ~70 ps, requires ATP (active)
    Read:  ~3 ps, passive, always on
    Read is ~20× faster than write

Co-resonance between cells: two cells with matching
ν-patterns have identical molecular vibration spectra →
sympathetic resonance via gap junctions (Levin's "data bus").
Mismatch → no resonance.

### F32. Pattern fidelity > 99.99% (write/noise ratio ~ 10¹⁴)

Collective protection (1/N_atoms = 10⁻¹⁴) suppresses thermal
disruption so severely that W/N ≈ E_ATP/kT × (R_ATP/f_coll)
× N_atoms ~ 10¹⁴.  Pattern fidelity at steady state is
effectively unity.

However, the Goldilocks boundary (F24) is about PER-COLLISION
hop probability, not the collective ratio.  Storage lifetime
per channel (without active ATP rewriting):

| K (eV⁻¹) | τ_storage |
|-----------|-----------|
| 0.04 | 10 hr |
| 0.06 | 4.6 hr |
| 0.08 | 2.6 hr |
| 0.10 | 1.7 hr |

With active ATP rewriting (which refreshes the pattern at
~10¹⁰ hops/s), the effective storage is indefinite as long
as metabolism continues.  ATP cessation (cell death) starts
a ~3–10 hr degradation clock.

### F33. THz cannot directly excite neutrino modes

Because g_EM = 0 (F22), a THz source cannot resonantly drive
ν-modes.  THz energy is absorbed thermally (water absorption
coefficient ~100 cm⁻¹) and raises the local temperature.

A 1 mW THz source focused to 50 μm spot delivers ~10⁴× more
power than ATP per cell, but it is UNDIRECTED thermal energy.
THz acts as noise (raises kT), not signal.  The effect is:

    ΔT ~ 69 K/s → ~10 K rise in ~0.15 s

This shifts the Goldilocks boundary: at T+10 K, the retention
threshold moves to lower K, and stored patterns degrade faster.

Revised L01 experiment: THz heating → degraded retention →
detectable change in Levin's Vmem pattern.  Controls:
- Dead tissue: no change (pattern already frozen, no ATP)
- Gap-junction-blocked tissue: permanent degradation
  (cannot re-read pattern from neighbors after cooling)
- Normal tissue: transient degradation, ATP-driven recovery

### F34. Reiter's source saturates the ν-sheet pre-load

In the elastic torus framework, Reiter's experiment maps onto:

    gamma deposition → geometry modulation → ν-mode hopping

At K = 0.06, the Cd-109 source (300 γ/s × 88 keV) provides
~8 × 10⁷ hops/s — overwhelming thermal leak (~6 × 10⁻⁵
hops/s) by a factor of ~10¹².  The crystal is driven to
near-saturation, consistent with Track 1's finding (F3)
that ⟨E_pre⟩/E_th ≈ 0.98.

Even background radiation alone (1 ionizing event/cell/hr)
outpaces thermal leak by ~10⁴×, establishing a nonzero
baseline pre-load.  This explains why Reiter's effect is
robust: the fill/leak ratio is enormous for any measurable
radiation source.
