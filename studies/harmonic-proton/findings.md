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

---

## Track 3: Neutron model and decay

**Script:** [`scripts/track3_neutron_model.py`](scripts/track3_neutron_model.py)


### F8. The neutron as a charge-neutral composite

The neutron can be modeled as two opposite-charge fundamentals
plus uncharged harmonics:

    neutron = (-1,-2) [Q = +e] + (1,2) [Q = -e] + harmonics [Q = 0]
    total charge = 0

The charge magnitudes are equal (|Q| = e for both fundamentals),
and the signs are opposite by CPT symmetry — opposite-winding
modes carry opposite charges.

The (1,2) + (-1,-2) pair is the only option using physical
spin-1/2 modes with unit charge.  Other charge-cancellation
pairs (e.g., (1,1)+(-1,-1)) have either forbidden spins or
non-integer charges.


### F9. Beta decay energetics match exactly

    n → p + e⁻ + ν̄_e

| Component | Mass (m_e) | Mass (MeV) |
|-----------|-----------|------------|
| Neutron | 1838.684 | 939.565 |
| Proton | 1836.153 | 938.272 |
| m_n − m_p | 2.531 | 1.293 |
| Emitted electron | 1.000 | 0.511 |
| Available KE | 1.531 | 0.782 |

The neutron has 1.531 m_e more harmonic energy than the proton.
In the decay, the electron fundamental (1 m_e) escapes, and the
excess harmonic energy (1.531 m_e = 0.782 MeV) is released as
kinetic energy shared between the electron and antineutrino.

The endpoint energy 0.782 MeV matches the experimental value.


### F10. Proton stability vs neutron instability

The proton has one charged fundamental and no way to shed it:
uncharged harmonics cannot spontaneously acquire charge (n₁ ≠ 1
→ Q = 0, exact).  The proton is stable.

The neutron contains a charged pair (+e and −e) that can separate.
The separation is energetically favorable (m_n > m_p + m_e), so
the neutron is unstable.  The long lifetime (879 s) implies a
substantial barrier to the electron's escape.


### F11. The neutron-proton mass difference

    m_n − m_p = 2.531 m_e = extra electron fundamental (1 m_e)
                            + extra harmonic energy (1.531 m_e)

In the thermal model, the neutron's harmonic temperature is
T'_n = 33.869 m_e versus the proton's T'_p = 33.855 m_e — a
0.041% temperature difference.  The neutron is "slightly hotter."


### F12. Spin compatibility

All (n, 2n) harmonics have winding ratio n/(2n) = 1/2, so each
is spin-1/2.  The proton (one fundamental + N harmonics) and
neutron (two fundamentals + N' harmonics) each combine many
spin-1/2 components.  The total spin-1/2 sector is always
accessible regardless of N or N'.  The spin constraint is
compatible with any harmonic spectrum but does not select one.


### F13. Open questions from Track 3

**(a) The antineutrino.**  The model accounts for the decay
energy but does not predict the specific decay products.  The
0.782 MeV is shared between electron and antineutrino, but
what IS the neutrino in this framework?  Possibly a burst of
harmonic energy that escapes the composite, or a separate
topological object.

**(b) The binding mechanism.**  What prevents the electron
fundamental from escaping instantly?  The 879 s lifetime
requires an energy barrier or tunneling probability.

**(c) The selection rule for the mass difference.**  What
determines the neutron's extra 1.53 m_e of harmonic energy?
In the thermal picture, a 0.04% temperature difference is
tiny but nonzero.


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
| F8 | Neutron = two opposite-charge spin-1/2 fundamentals + harmonics; Q = 0 exactly |
| F9 | Decay energetics match: 0.782 MeV available KE for electron + antineutrino |
| F10 | Proton stable (1 fundamental), neutron unstable (charged pair can separate) |
| F11 | m_n − m_p = 1 m_e (extra fundamental) + 1.53 m_e (extra harmonics); ΔT/T = 0.04% |
| F12 | Spin 1/2 compatible for both proton and neutron with any harmonic count |
| F13 | Open: antineutrino identity, binding mechanism, mass-difference selection rule |


## Scripts

- [`scripts/track1_harmonic_spectrum.py`](scripts/track1_harmonic_spectrum.py)
  — Harmonic energies, charges, mode catalog, mass sums, energy formula comparison
- [`scripts/track3_neutron_model.py`](scripts/track3_neutron_model.py)
  — Neutron charge cancellation, decay energetics, spin, stability
