# R35. Threshold detection and material-dimension coupling

**Questions:** Q78, Q32  **Type:** compute + theoretical
**Depends on:** R26, R19, R27, R33
**Supports:** L00 (Reiter replication), L01 (THz write/read)
**Status:** Complete (4 tracks, 34 findings)

---

## Motivation

The storage hypothesis requires three quantitative ingredients
that have not been computed:

1. Whether threshold detection statistics reproduce Reiter's
   Re/Rc ≫ 1 from a Ma (the six-dimensional material space)-informed pre-load model.
2. How fast energy can be written into and read from a Ma_ν
   mode, given a coupling strength.
3. What the coupling strength actually is, and whether a
   "Goldilocks window" exists (strong enough to write/read,
   weak enough to retain).

Each of these is computable with existing infrastructure
(Ma solver from R26) plus standard physics (driven oscillators,
Monte Carlo statistics, perturbation theory).

### The unified mode-density picture (Q85 §14)

The threshold "continuity" is not a separate mechanism — it
is what material-sheet mode-hopping looks like when the ladder is dense.
On the neutrino sheet (r_ν ≫ 1), thousands of modes fit in
[m, 2m], making energy steps unresolvable.  On the electron
and proton sheets (r ~ 7–9), the ladder is sparse — only a
handful of modes survive the spin filter (R33 F3), so energy
goes to S (the three spatial dimensions) momentum instead of mode-hopping.

This means threshold detection (Track 1) and storage (Tracks
2–4) are specifically neutrino-sheet phenomena.  The electron
and proton sheets contribute known discrete physics (quantum
jumps, nuclear resonances).  The "continuous" feel of Reiter's
model maps onto the neutrino sheet's quasi-continuum.

---

## Track 1. Threshold detection statistics

**Goal:** Model Reiter's beam-split coincidence experiment as
threshold detectors with Ma-informed pre-loaded states.
Compute Re/Rc and compare to Reiter's measured values.

**Model:**
- A detector crystal (NaI) has atoms whose Ma_e modes
  can accumulate sub-threshold energy.
- A gamma ray (88 keV from Cd-109) is a classical wave packet
  that splits at the beam splitter (tandem geometry: fraction α
  transmitted, fraction 1−α absorbed by detector #1).
- Each detector has a pre-loaded state E_pre drawn from a
  distribution P(E_pre) shaped by the history of previous
  partial absorptions.
- A detector fires when E_pre + E_gamma_share ≥ E_threshold.
- Coincidence occurs when both detectors fire simultaneously.

**Inputs:**
- Source rate R (singles: ~300/s for Reiter's Cd-109 setup)
- Split fraction α (what fraction passes through the thin
  detector)
- Threshold energy E_th = 88 keV (the gamma energy)
- SCA window: LL at 2/3 × E_th (as Reiter set it)
- Pre-load distribution P(E_pre) — this is the key free
  function; derived from Ma cross-shear leakage rates

**Output:**
- Re/Rc as a function of the pre-load distribution shape
- Which distribution shapes produce Re/Rc ≈ 33 (Reiter's
  Cd-109 result) and Re/Rc ≈ 963 (Na-22 triple)
- Sensitivity to SCA window setting, split fraction, and
  source rate

**Method:** Monte Carlo simulation.  10⁶–10⁸ decay events.
Draw pre-load states, draw split fractions, apply threshold,
count coincidences.

**Script:** `scripts/track1_threshold_statistics.py`

**Result (Complete):** The Compton asymmetry at 88 keV makes Re/Rc =
1/(2τR) ≈ 1667, independent of pre-load (F1).  This over-predicts
Reiter's Cd-109 by 51×.  The SCA upper limit resolves this: atoms
nearly fully loaded (⟨E_pre⟩ ≈ 0.98 E_th) have pulses that exceed
the photopeak window, bringing Re/Rc to ~33 (F3).  Na-22 (511 keV)
IS pre-load-sensitive: uniform max ≈ 0.43 E_γ matches Re/Rc ≈ 963
(F2).  Joint Cd-109/Na-22 match is approximate (30% tension on
Na-22).  The fill_rate/leak_rate ratio is the master parameter (F6).
See findings F1–F7.

---

## Track 2. Write/read dynamics on Ma_ν

**Goal:** Model write/read dynamics on Ma_ν, including storage
capacity, write/read timescales, pattern fidelity, and
experimental predictions.

**Original model (superseded):** damped driven oscillator
(ä + γȧ + ω₀²a = gF) with EM coupling g.  Tracks 3–4
showed g = 0 (F22) and the elastic torus is the I/O mechanism.

**Reframed model:** Stochastic mode hopping on the neutrino
sheet, driven by ATP events (write) and opposed by thermal
disruption (noise).  Reading is passive co-resonance via
molecular vibration shifts (F25).

**Computed:**
- Storage capacity: 10–324 bits/cell (energy-bin vs. pattern)
- Write dynamics: ~70 ps/hop at mid-Goldilocks (K = 0.06)
- Read dynamics: ~3 ps/channel (K-independent, SNR ~ 10⁷)
- Dynamic Goldilocks: W/N ~ 10¹⁴, fidelity > 99.99%
- Storage lifetime (passive): 2.6–10.4 hr depending on K
- L01 revision: THz → thermal disruption (not direct drive)
- Reiter reinterpretation: source saturates ν-sheet pre-load

**Script:** `scripts/track2_write_read_dynamics.py`

**Result (Complete):** F29–F34.  Storage is 10–324 bits/cell.
Write takes ~70 ps/hop (ATP-driven, sub-μs for full pattern).
Read takes ~3 ps (passive, K-independent).  Fidelity > 99.99%
during active metabolism; passive storage lifetime 2.6–10 hr.
THz cannot directly drive ν-modes (g = 0); revised L01 uses
thermal degradation as the observable.  Reiter's source drives
pre-load to saturation (fill/leak ~ 10¹²), consistent with
the SCA upper-limit mechanism (F3).

---

## Track 3. Cross-shear leakage rate

**Goal:** Compute the rate at which energy in a Ma_ν mode leaks
into other modes via cross-shear coupling.  This sets the
damping rate γ for Track 2 and the storage lifetime.

**Model:** The Ma metric (from R26 Track 4a) with cross-shear
parameters σ_eν and σ_νp couples modes on different material-sheet
subplanes.  A pure neutrino mode (0,0,n₃,n₄,0,0) has a small
admixture of Ma_e and Ma_p modes due to the
cross-shear.  Energy leaks from the neutrino mode into these
admixtures at a rate proportional to σ².

**Computation:**
1. Build the Ma metric using `self_consistent_metric()` at
   various (σ_eν, σ_νp) values.
2. For each neutrino mode (n₃, n₄), compute the eigenvalue
   shift due to cross-shear (perturbation theory or direct
   diagonalization).
3. The imaginary part of the eigenvalue shift gives the decay
   rate γ.  (At first order, the shift is purely real — need
   second-order perturbation theory with the continuum of S
   states to get a width.)

**Alternative (simpler):** Fermi's golden rule applied to the
mode-mode coupling matrix element.  The rate of energy transfer
from neutrino mode |ν⟩ to Ma_e mode |e⟩ is:

    γ = (2π/ℏ) |⟨e| V_cross |ν⟩|² ρ(E)

where V_cross is the cross-shear perturbation and ρ(E) is the
density of final states.  Both can be computed from the Ma
metric.

**Inputs:**
- Ma metric parameters from R26 (all three material sheets, cross-shears)
- The cross-shear perturbation matrix V = G_full − G_block

**Output:**
- Leakage rate γ(n₃, n₄) for each neutrino mode as a function
  of (σ_eν, σ_νp)
- Storage lifetime τ_store = 1/γ for the lowest modes
- Which modes are longest-lived (likely the lowest, most
  isolated ones)

**Script:** `scripts/track3_leakage_rate.py`

**Result (Complete):** Neutrino modes are EXACTLY uncharged
(Q = 0, topological) — Γ_EM = 0 to all orders in σ_eν (F8).
Cross-shear shifts energies (δE/E ∝ σ_eν²) but does NOT mix
modes on a flat Ma (F9).  Naive thermal model gives τ ~ 12 days
(σ_eν = 0.01) to 3.2 years (σ_eν = 0.001) with collective
protection (F11).  The actual thermal pathway requires bridging
a MeV gap — exponentially suppressed (F12).  Three-layer
protection (charge + gap + collective) is direction-independent:
radiation from inside the cell (K-40, chemistry) is equally
blocked (F15).  Crucially, the shielding blocks READING equally —
on a flat Ma, the ν-state doesn't affect any observable (F16).
The elastic torus (Hypothesis I) resolves this: geometric
modulation bypasses all three layers, enabling active internal
write + passive external read (co-resonance) while maintaining
noise protection (F17).  The Goldilocks parameter shifts from
σ_eν to metric stiffness K (F18).  See findings F8–F18.

---

## Track 4. Coupling strength estimate

**Goal:** Estimate the strength of the neutron-gateway coupling
between S electromagnetic fields and Ma_ν modes.  Determine
whether a Goldilocks window exists.

**Model:** The neutron mode (1,2,0,0,1,2) bridges the Ma_e
and Ma_p subplanes.  Cross-shear parameters σ_eν and σ_νp
connect these to Ma_ν.  A 3+1D electromagnetic field at
frequency ω₀ (matching a Ma_ν mode) can transfer energy into
that mode via the chain:

    EM → Ma_e → σ_eν → Ma_ν

The coupling g is the product of:
- The EM-to-Ma_e coupling (related to α = 1/137)
- The Ma_e-to-Ma_ν coupling (related to σ_eν)

**Computation:**
1. From the Ma metric, compute the off-diagonal metric
   component coupling the Ma_e and Ma_ν sectors.
2. This gives the mode-mode coupling matrix element
   ⟨ν_mode | G_cross | e_mode⟩.
3. The per-neutron coupling g₁ is this matrix element times the
   EM-to-electron coupling (which is √α in natural units).
4. Aggregate coupling per cell: g_cell = g₁ × √N_neutrons
   (coherent sum) or g₁ × N_neutrons (incoherent sum),
   depending on whether the neutron gateways are phase-coherent.

**Output:**
- Per-neutron coupling g₁ as a function of (σ_eν, σ_νp)
- Aggregate coupling per cell g_cell
- Goldilocks constraints:
  - Write: g_cell × P_source × τ_write ≥ E_mode (can write one
    mode quantum)
  - Retain: γ_leakage × τ_life ≤ 1 (stored state persists)
  - Read: g_cell × E_stored ≥ P_noise (signal above detector
    noise)
- Parameter region in (σ_eν, σ_νp) space where all three
  constraints are simultaneously satisfied

**Script:** `scripts/track4_coupling_estimate.py`

**Result (Complete):** Flat Ma coupling is EXACTLY ZERO — neutrino
modes are uncharged, cross-shear doesn't mix modes, and the MeV gap
blocks thermal pathways (F22).  The elastic torus shifts I/O from EM
to geometry: molecular forces → δs₃₄ → mode energy shift (F23).
Shear sensitivity ∂E/∂s₃₄ ≈ E₀; Goldilocks reduces to F_write/kT > 10
(F24).  Read SNR is K-independent at ~10⁷ (F25).  Passive vibrations
CANNOT write (F/kT = 1.9, F26).  ATP hydrolysis (0.5 eV, F/kT = 18.7)
opens a Goldilocks window: K ∈ [0.043, 0.080] eV⁻¹ (F27).  Writing
REQUIRES metabolic energy — dead cells can't write but can be read.
See findings F22–F28.

---

## Expected deliverables

1. **Re/Rc predictions** (Track 1) that either match or fail to
   match Reiter's data — a computational test of threshold
   theory before the physical experiment.

2. **An "operating manual" for L01** (Track 2) — what source
   power and exposure time are needed for a detectable
   write/read cycle, as a function of coupling strength.

3. **Storage lifetime estimates** (Track 3) — does the Ma
   metric predict lifetimes of seconds, hours, or geological
   time?  This directly constrains the biological relevance.

4. **A Goldilocks assessment** (Track 4) — is there ANY region
   of parameter space where material-dimension storage is
   physically viable?  If no such region exists, the hypothesis
   can be retired on theoretical grounds alone, before spending
   money on experiments.
