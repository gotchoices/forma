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
