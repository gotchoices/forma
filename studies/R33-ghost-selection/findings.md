# R33 Findings

## Summary

Two tracks completed (1, 8), one killed (7), five deferred
(2–6).  15 findings.

**The ghost problem is reduced from ~860 modes to ~4 per
charged sheet** by two complementary mechanisms:

1. **n₁ = ±1 selection rule** (F1): the WvM charge integral
   gives zero charge to all modes with |n₁| ≠ 1.  Kills 88%.

2. **Spin-statistics filter** (F3): if spin = n₁/n₂ (WvM),
   only integer and half-integer spin modes are physical.
   Kills all n₂ ≥ 3 and n₂ = 0 modes.  Reduces survivors
   to (1,±1) spin-1 bosons and (1,±2) spin-½ fermions.

**The remaining tension is the (1,1) boson** — a charged
spin-1 particle at half the electron mass, unobserved.
Track 8 found that ω⁴ radiation suppression reduces its
observable coupling to ~1/8× the electron (F12), but this
is model-dependent (F14).

**The neutrino sheet is not a ghost problem** — its dense
mode spectrum is the hypothesized storage medium (Q85 §8).

**Open for future work:**
- Track 6 (spin derivation): could change the entire filter
  if spin ≠ n₁/n₂
- Tracks 2–5: cleanup tracks, reduced in urgency
- QFT vertex calculation: would settle the ω⁴ question

---

## Track 1 — Charge integral per mode

### F1. n₁ = ±1 selection rule is the primary ghost killer

The R19 charge integral (θ₁_phys integral) selects |n₁| = 1
only.  All modes with n₁ = 0, ±2, ±3, ... have ZERO charge
from the WvM integral.  On a 17×17 mode grid, this eliminates
255 of 289 modes (88%) on each sheet.

This is the single strongest ghost suppression mechanism.
It reduces the charged mode population from ~900 to ~34 per
sheet before any other filter is applied.

### F2. Charge coupling ENHANCES low-n₂ modes

Among the surviving n₁ = 1 modes, the coupling scales as:

    α(1, n₂)/α(1, 2) ≈ [(2-s)/(n₂-s)]² × [μ(n₂)/μ(2)]

| Mode   | α/α_electron | Mass/m_e |
|--------|-------------|----------|
| (1, 0) | 2844×       | 0.076    |
| (1, 1) | 2.03×       | 0.502    |
| (1, 2) | 1.00×       | 1.000    |
| (1, 3) | 0.66×       | 1.500    |
| (1, 4) | 0.50×       | 2.000    |
| (1, 8) | 0.25×       | 4.006    |

The charge integral does NOT prefer the electron.  It creates
a hierarchy favoring LOW n₂, with a divergent pole at n₂ = s.
The electron sits in the middle, not at the top.

### F3. Spin filter + charge integral = 4 survivors per sheet

Combining the n₁ selection rule, the charge integral, and the
spin-statistics filter (spin = n₁/n₂):

| Mode   | Spin  | Coupling | Mass/m_e | Status      |
|--------|-------|----------|----------|-------------|
| (1, 0) | undef | ∞        | 0.076    | KILLED      |
| (1, 1) | 1     | 2.03×    | 0.502    | SURVIVES    |
| (1,-1) | 1     | 1.99×    | 0.512    | SURVIVES    |
| (1, 2) | ½     | 1.00×    | 1.000    | ELECTRON    |
| (1,-2) | ½     | 0.99×    | 1.010    | SURVIVES    |
| (1, 3) | 1/3   | 0.66×    | 1.500    | KILLED      |
| (1, n) | 1/n   | ~1/n²    | ~n/2     | KILLED      |

Four modes survive per sheet (counting ±n₂ separately).
The ghost problem reduces from ~860 modes to 4 per sheet.

### F4. The (1,1) boson is the critical remaining tension

On the electron sheet, the (1,1) mode is:
- Spin-1 charged boson (valid quantum numbers)
- Mass ≈ 0.50 m_e ≈ 0.26 MeV
- EM coupling 2× stronger than the electron
- Charge −1

No such particle has been observed.  On the proton sheet,
the analogous mode (1,1) is at ~470 MeV with charge +1 and
2× proton coupling — also unobserved.

### F5. High-n₂ modes are strongly suppressed

The coupling scales as ~1/n₂² for large n₂.  Modes with
n₂ = 10 have 1/25th the electron's coupling.  This is a
natural geometric suppression independent of the spin filter.
For modes that survive the spin filter (none above n₂ = 2),
this is redundant — but it provides a second line of defense.

### F6. The (1,-2) mode is nearly degenerate with the electron

The antiparticle mode (1,-2) has:
- Spin ½ (same as electron)
- Mass 1.01 m_e (1% heavier due to shear)
- Coupling 0.99× (nearly identical)

This is the positron's mirror mode.  The slight mass
asymmetry (1%) is a prediction — the (1,2) and (1,-2) modes
are NOT exact CPT conjugates on the sheared Ma_e.

### F7. Cross-sheet ghosts introduce new tensions

The (1,1,0,0,1,2) cross-sheet mode has:
- Q_WvM = −1.01 (charged, despite Q_KK = 0)
- Mass ≈ 940 MeV (neutron-like)
- Spin 1 (from the combined 2/2)

The WvM charge integral gives this mode a charge of about −1,
because the electron-sheet (1,1) component contributes 2×
the electron's charge while the proton-sheet (1,2) component
contributes +1.  This is a cross-sheet ghost that the KK
formula would call neutral but the WvM integral says is
charged.

### F8. The charge integral cannot pin r_e

Q(1,1) = sin(2πs)/(1-s) is nonzero for all s ≠ 0.
Setting Q(1,1) = 0 requires s = 0, which also kills the
electron's charge.  The charge integral has no zero-crossing
for (1,1) at any finite s, and s is a monotonic function of
r_e.  Track 7 (r_e scan) therefore cannot use the charge
integral to pin r_e.

The (1,1) tension must be resolved by a different mechanism:
- The WvM spin assignment is wrong (spin = ½ per sheet)
- An additional topological selection rule forbids (1,1)
- The (1,1) boson is unstable (but to what?)
- **Wave-optics aperture suppression (Track 8):** See F9–F15.

## Track 8 — Wave-optics coupling through the shear aperture

### F9. The sinc aperture effect is negligible

The shear aperture (δ = s × L₂ ≈ 1% of ring) is so small
compared to ALL mode wavelengths that it treats them all
equally.  The sinc(πsn₂) factor differs by < 0.2% between
n₂ = 1 and n₂ = 2.  Pure aperture size is not the mechanism.

### F10. The ω⁴ Larmor factor is the key suppression

In the dipole radiation model (P ∝ ω⁴ |p|²), the mode
frequency determines radiation efficiency.  Since the (1,1)
mode has half the electron's energy:

    P(1,1)/P(1,2) ∝ (μ₁₁/μ₁₂)⁴ = (1.0/2.0)⁴ = 1/16

The (1,1) ghost radiates 16× less power than the electron.

### F11. Three of four models show low-n₂ suppression

| Model | Scaling | (1,1)/(1,2) coupling |
|-------|---------|---------------------|
| Geometric (Track 1) | n₂⁻² | 2.03× (enhanced) |
| Bethe (d/λ)⁴ | n₂⁺⁴ | 0.063× (suppressed) |
| Cavity-slit | n₂⁺² | 0.25× (suppressed) |
| Dipole+sinc | n₂⁺⁴ | 0.063× (suppressed) |

The geometric integral is the outlier.  It measures charge
structure but ignores radiation efficiency.

### F12. Observable coupling = charge × radiation efficiency

The geometric integral answers "how much charge does the
mode carry?"  The dipole model answers "how efficiently
does it radiate?"  The observable coupling is the product.
For (1,1): charge factor 2× × radiation factor 1/16 =
**net 1/8× the electron**.  The ω⁴ suppression overwhelms
the charge enhancement.

### F13. The same mechanism suppresses the proton-sheet ghost

The (1,1) mode on the proton sheet at ~470 MeV has μ ≈ 1.0
vs the proton's μ ≈ 2.0.  Same 1/16 suppression.

### F14. Critical caveat — ω⁴ may be classical artifact

The ω⁴ Larmor scaling applies to classical dipole radiation.
In QFT, the coupling between a charged particle and the
photon field depends on charge, not ω⁴.  Whether the ω⁴
factor is physical depends on whether the Ma_e → S coupling
is better described by:

- Classical radiation (ω⁴ applies): ghost suppressed ✓
- QFT vertex (charge only): Track 1 stands, ghost unsuppressed ✗

This is the deepest open question in the ghost selection
program.  A QFT-level calculation of the material sheet mode / S photon
vertex would resolve it definitively.
