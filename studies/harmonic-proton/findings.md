# R20. Harmonic Proton — Findings

See [`README.md`](README.md) for motivation and study plan.


---

## Track 1: Harmonic spectrum and charge on sheared T²

**Script:** [`scripts/track1_harmonic_spectrum.py`](scripts/track1_harmonic_spectrum.py)

Electron geometry: r = 1.0, s₁₂ = 0.16513, q_eff = 1.835.


### F1. Harmonics are uncharged (exact)

The (n, 2n) mode — the nth multiple of the electron's wavevector
on sheared T² — has charge exactly zero for n ≥ 2.  This is
a direct consequence of the n₁ selection rule (R19 F30): the
charge integral's θ₁ projection selects |n₁| = 1, and the
(n, 2n) mode has n₁ = n.

| n | mode | Q/Q_e | n₁ |
|---|------|-------|----|
| 1 | (1,2) | 1.000 | 1 |
| 2 | (2,4) | 0.000 | 2 |
| 3 | (3,6) | 0.000 | 3 |
| ... | ... | 0.000 | ... |

This confirms the core premise: adding (n, 2n) harmonics
to the electron adds mass without changing the total charge.


### F2. The CPT conjugate has exactly opposite charge

The (-1,-2) mode has Q/Q_e = -1.000 exactly.  This follows
from the general charge formula:

    Q(n₁, n₂) ∝ sin(2πs₁₂) / (n₂ - n₁ s₁₂)    for |n₁| = 1

For the electron (1,2): Q ∝ 1/(2-s).
For the conjugate (-1,-2): Q ∝ -1/(-2+s) = 1/(2-s) × (-1).

The ratio is exactly -1, confirming CPT symmetry on the sheared
torus.  Opposite-charge configurations are available for building
neutral composites.


### F3. Pure thermal distribution fails the charge constraint

A Bose-Einstein distribution f(n) = 1/(exp(n/T) - 1) at
temperature T ≈ 33.6 m_e (17 MeV) reproduces the proton mass.
But the fundamental mode is occupied f(1) ≈ 33 times, giving
total charge ≈ 33e instead of e.

The charge constraint **requires f(1) = 1** — exactly one
quantum of the charged fundamental.  A proton is NOT a
generic thermal excitation of the torus.


### F4. Convergent infinite series exist for the uncharged mass

With f(1) = 1 fixed, the remaining 1835 m_e must come from
uncharged harmonics (n ≥ 2).  Multiple convergent series work:

| Distribution | Parameter | Uncharged mass | Convergent? |
|-------------|-----------|----------------|-------------|
| Corrected thermal | T' ≈ 33.9 m_e | 1835.15 m_e | ✓ |
| Geometric | x ≈ 0.977 | 1835.15 m_e | ✓ |
| Complete (n=1..60) | N = 60 | 1830 m_e | N/A (finite) |

The corrected thermal distribution has f(n≥2) = 1/(exp(n/T')-1)
with T' = 33.86 m_e (17.3 MeV).  The highest significantly
occupied harmonic is n ≈ 154.

The complete series (all harmonics up to N=60) gives 1830 m_e,
6 m_e short of the target.  No integer cutoff N hits 1836
exactly.

The specific distribution is underdetermined — the mass
target alone does not select a unique spectrum.


### F5. The correct energy formula is E = ℏc|k| (momentum picture)

R13/R19 set the electron's energy via E = hc/L_geodesic, treating
the photon's wavelength as equal to the geodesic path length.  This
is correct for the fundamental mode (one wavelength fits the path).
But it was wrongly generalized: the (n, 2n) mode does NOT have
wavelength nL_e.  It has wavelength L_e/n — it oscillates n times
faster in every direction, like a guitar string's nth overtone.

The correct dispersion relation for a massless field on a flat
torus is E = ℏc|k|, giving:

    E(n, 2n) = n × m_e     (harmonics are HEAVIER)

This is consistent with E = hc/λ where λ = L_e/n (shorter
wavelength = more energy), and with E = mc² (more energy = more
mass).  There is no physical regime where adding energy to a
mode makes it lighter.

The "winding energy" E = hc/L_geo = m_e/n is a misidentification:
it confuses the geodesic path length (nL_e) with the photon's
wavelength (L_e/n).  The two coincide only for the fundamental
(n = 1).

The R19 charge formula and the value of α are unaffected by this
correction — they depend on dimensionless ratios (r, s) and the
mode structure, not on the absolute energy scale.


### F6. Lighter charged modes in the spectrum

With E = ℏc|k| as the correct formula, several charged modes
(|n₁| = 1) are lighter than the electron:

| Mode | E/m_e | Q/Q_e | Spin (n₁/n₂) | Status |
|------|-------|-------|--------------|--------|
| (1,0) | 0.49 | −11.1 | 1/0 → ∞ | forbidden (no finite spin) |
| (-1,1) | 0.73 | −1.57 | 1 | spin-1 boson; Q ≈ 1.6e |
| (1,1) | 0.62 | +2.20 | 1 | spin-1 boson; Q ≈ 2.2e |
| (1,2) | 1.00 | +1.00 | 1/2 | **electron** |

The (1,0) mode is forbidden by spin quantization (undefined spin).
But (-1,1) and (1,1) have spin 1 (allowed) and are lighter than
the electron.  They carry non-integer charges (1.6e and 2.2e) —
no such particles have ever been observed.

This is a genuine constraint on the model.  Possible resolutions:

- **Charge quantization:** modes with non-integer Q/e may be
  unphysical.  The charge formula gives Q = e only for the (1,2)
  mode; all other charged modes have |Q| ≠ e.  If nature requires
  integer charge, only (1,2) and (-1,-2) are allowed.
- **Instability:** spin-1 bosons with |Q| > e could decay rapidly
  to electron + photons, making them unobservable.
- **The charge formula may not apply to off-diagonal modes.**
  R19 derived it for the (1,2) electron.  Modes in very different
  directions on the torus may couple differently to the external
  3D electromagnetic field.

This remains an open question but is not a showstopper for the
harmonic proton model, which uses only (n, 2n) harmonics —
all uncharged and all in the electron's direction.


### F7. The uncharged mode zoo

98 uncharged modes exist with E < 10 m_e.  These include:

| Mode | E/m_e (momentum) | Type |
|------|-------------------|------|
| (0,±1) | 0.48 | Pure θ₂ |
| (0,±2) | 0.96 | Pure θ₂ |
| (±2,0) | 0.97 | Pure θ₁ |
| (±2,±1) | 1.01 | Mixed |
| (2,4) | 2.00 | Harmonic #2 |
| (3,6) | 3.00 | Harmonic #3 |

The proton's uncharged mass need not come exclusively from
(n, 2n) harmonics.  Any uncharged mode (|n₁| ≠ 1) could
contribute.  This greatly expands the space of possible
proton models but also makes the model less predictive
without a selection rule.


---

## Summary table

| # | Finding |
|---|---------|
| F1 | (n, 2n) harmonics are exactly uncharged for n ≥ 2 — mass without charge confirmed |
| F2 | CPT conjugate (-1,-2) has exactly −Q_electron |
| F3 | Pure thermal distribution fails: f(1) ≈ 33 gives Q ≈ 33e |
| F4 | With f(1) = 1, convergent infinite series exist (thermal T' ≈ 34 m_e, geometric x ≈ 0.98) |
| F5 | Correct energy is E = ℏc\|k\| — harmonics are heavier (n × m_e); "winding energy" was a misidentification |
| F6 | Lighter charged modes exist (spin-1 with Q ≈ 1.6e, 2.2e) — need charge quantization or instability argument |
| F7 | 98 uncharged modes exist below 10 m_e — proton mass need not come from (n,2n) alone |


## Scripts

- [`scripts/track1_harmonic_spectrum.py`](scripts/track1_harmonic_spectrum.py)
  — Harmonic energies, charges, mode catalog, mass sums, energy formula comparison
