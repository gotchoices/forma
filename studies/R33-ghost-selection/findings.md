# R33 Findings

## Summary

Three tracks completed (1, 8, 9), one killed (7), five
deferred (2–6).  20 findings.

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

**Harmonic modes (n, 2n) don't exist as free particles**
(Track 9): Coulomb self-energy makes them unstable to fission
(F17), and the gcd criterion (F20) shows they are reducible
into separable strands.  The charge formula question (F16) is
not settled — KK gives charge −n, WvM gives 0 — but fission
instability applies regardless.  The proton (1,3) avoids
fission: gcd = 1 makes it irreducible (antinodes, not
strands), and its internal coupling is at the full Ma field
strength (Q95).  Multi-electron states exist only in atoms
where nuclear confinement provides external binding (F19).

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


## Track 9 — Coulomb fission of harmonic electron modes

Script: `scripts/track9_harmonic_fission.py`

Tracks 1–8 address modes with different winding *ratios*.
Track 9 asks about the harmonic series: modes (n, 2n) with
the same ratio as the electron (1:2) but at higher winding
numbers.  Why don't (2,4), (3,6), ... exist as free particles?

### F15. Harmonic mode masses are exactly n × m_e

On the sheared electron torus (r_e = 6.6, s_e = 0.0103),
the dimensionless energy μ(n, 2n) = n × μ(1, 2) exactly.
The shear cross-term (−n₁ × s) cancels when both quantum
numbers are scaled by the same factor.

| Mode | μ | Mass (MeV) | Mass / m_e |
|:---:|:---:|:---:|:---:|
| (1, 2) | 1.995 | 0.511 | 1.000 |
| (2, 4) | 3.991 | 1.022 | 2.000 |
| (3, 6) | 5.986 | 1.533 | 3.000 |
| (5, 10) | 9.977 | 2.555 | 5.000 |
| (10, 20) | 19.955 | 5.110 | 10.000 |

The (n, 2n) harmonic has exactly n times the electron's rest
energy — indistinguishable (in mass) from n electrons at rest.


### F16. Charge of (n, 2n) harmonics: n units from GRID's 2π rule

GRID's charge quantization (A3, charge-from-energy §3) derives
charge from the topology of the standing wave: each 2π tube
winding contributes one unit of charge (±e).  A mode with n₁
tube windings carries charge |Q| = n₁.  This is stated
explicitly for harmonic modes:

> "The (Z, 2Z) harmonic has Z cycles → charge Ze."
> — charge-from-energy §11

A (2,4) electron mode therefore carries charge −2e and mass
2m_e — two quanta of electron energy and charge on the same
torus.  A (3,6) mode carries −3e, etc.

On the proton sheet, the same rule gives nuclei their charge:
a (Z, 3Z) proton mode (under the (1,3) hypothesis) has Z tube
windings → charge +Ze.  Helium (2, 6) has charge +2, carbon
(6, 18) has charge +6, etc.  This is consistent with the R29
nuclear scaling law.

The WvM charge integral (F1, Track 1) gives a different result
for |n₁| ≥ 2: Q_WvM = 0.  This may reflect coupling
*strength* (how efficiently the mode radiates into S) rather
than topological charge.  The distinction between "carries
charge" and "couples to photons" is not yet resolved but does
not affect this track — the Coulomb fission argument (F17)
applies directly from the GRID charge assignment.


### F17. Coulomb self-energy makes composites unstable

By GRID's 2π charge rule, the (n, 2n) mode carries n units
of like charge (−ne on Ma_e).  The Coulomb self-energy of
these n charges at the mode's Compton radius makes the
composite strictly higher-energy than n separated (1,2)
electrons.

Using the reduced Compton wavelength ƛ_C/n as the confinement
radius (characteristic size of the composite):

| n | r_conf (fm) | E_self (keV) | E_self / m_e |
|:---:|:---:|:---:|:---:|
| 2 | 193 | 7.5 | 0.015 |
| 3 | 129 | 33.6 | 0.066 |
| 5 | 77 | 186 | 0.365 |
| 10 | 39 | 1,678 | 3.28 |

The fission energy ΔE = E_self is always positive (repulsive)
and grows rapidly — roughly as n²(n−1)/2 × α × m_e.

No confining force exists on Ma_e.  The only internal coupling
is electromagnetic (strength α ≈ 1/137), which is repulsive
for like charges.  There is no mechanism analogous to the
strong force's linear confinement that could bind electrons
into a composite.

Therefore: the separated state (n free electrons) is always
energetically favored over the composite (n, 2n) mode.


### F18. Proton (1,3) is stable — irreducibility + full Ma coupling

The same fission analysis applied to the proton sheet gives the
*opposite* conclusion, for two independent reasons.

**Reason 1: Irreducibility.**  Under the (1,3) proton
hypothesis, gcd(1, 3) = 1 — the mode is irreducible.  Its
three-fold structure (three energy antinodes at 0°, 120°,
240° around the ring) consists of features of one standing
wave, not independent sub-modes.  There are no "strands" to
separate.  You cannot peel an antinode off a wave, so the
fission pathway does not exist.

Compare to the electron harmonics:

| Mode | gcd | Structure | Fission? |
|:---:|:---:|:---|:---:|
| (1,3) proton | 1 | 3 antinodes (one wave) | impossible |
| (2,4) electron | 2 | 2 strands of (1,2) | always |
| (3,6) electron | 3 | 3 strands of (1,2) | always |

**Reason 2: Internal coupling strength (Q95).**  The "strong
force" is not an S-physics concept separate from EM — it IS
the electromagnetic field seen from inside Ma, without the
Compton-window attenuation.  At distances r >> λ_C, only the
α-projected field leaks into S (electromagnetism).  At
r ~ λ_C (torus overlap), particles couple through the full
internal Ma field at strength ~1, not ~1/137.

The ratio α_s / α ≈ 137 = 1/α is this attenuation factor.
It is not a coincidence — it IS 1/α.

The proton sheet's internal coupling is at the full field
strength because the mode's own internal fields never pass
through the Compton window.  The electron sheet has the same
internal field strength, but electron-electron repulsion
(between separate (1,2) modes at r >> λ_C) goes through S
and is α-attenuated.

| | Ma_e composites | Ma_p (1,3) |
|:---|:---:|:---:|
| Internal fields | ~1 (same) | ~1 (same) |
| Inter-mode coupling | α ≈ 1/137 (through S) | n/a (one mode) |
| Self-interaction | repulsive (same charge) | irreducible |
| Net stability | unstable | stable |

The proton is stable because (a) it cannot fission (irreducible)
and (b) its internal coupling is at the full Ma field strength.
Neither reason involves S-physics or the "strong force" as a
separate fundamental interaction.


### F19. Atoms provide external confinement — the two-tier picture

Multi-electron configurations DO exist in nature: atoms.  But
they are stable only because the nucleus provides external
Coulomb confinement.  Measured total ionization energies exceed
the electron self-repulsion at the Bohr radius by 2.5–5×:

| Z | E_ee at a₀ (eV) | Measured I.E. (eV) | Ratio |
|:---:|:---:|:---:|:---:|
| 2 | 27 | 79 | 2.9 |
| 6 | 408 | 1,030 | 2.5 |
| 10 | 1,225 | 3,952 | 3.2 |
| 26 | 8,844 | 42,944 | 4.9 |

Remove the nucleus and the electrons fly apart — the self-
repulsion has no counterbalance.

This validates the "two-tier picture":
- **Ma (material space)** defines particle identity: the
  electron is (1,2) on Ma_e, the proton is a mode on Ma_p.
- **S (spatial lattice)** defines binding: atoms are spatially
  bound configurations where nuclear attraction confines
  electrons.  The 3D Coulomb potential is S-physics, not
  Ma-physics.

Free (n, 2n) harmonics on Ma_e are Coulomb-unstable (ΔE > 0)
regardless of the charge formula.  They are n quanta of
electron energy that fission into n separate electrons in S.
Multi-electron states exist only in atoms, where nuclear
attraction provides the missing confinement.


### F20. The irreducibility criterion — gcd determines fission

The deepest selection rule for harmonic stability is the
greatest common divisor of the winding numbers.

A mode (n₁, n₂) with gcd(n₁, n₂) = g > 1 decomposes into g
copies of the reduced mode (n₁/g, n₂/g) at g evenly-spaced
phases.  Each copy is a valid, independently-propagating mode
(a "strand").  The composite's stability then depends on
whether inter-strand forces are attractive or repulsive.

A mode with gcd = 1 is irreducible.  Its internal structure
consists of antinodes (energy peaks of one standing wave),
not strands.  Antinodes cannot separate — destroying one
destroys the entire mode.  Fission is topologically forbidden.

| Particle | Mode | gcd | Structure | Fission? |
|:---|:---:|:---:|:---|:---:|
| Electron | (1, 2) | 1 | irreducible | n/a |
| 2 electrons | (2, 4) | 2 | 2 × (1,2) strands | YES |
| 3 electrons | (3, 6) | 3 | 3 × (1,2) strands | YES |
| Proton (1,3 hyp.) | (1, 3) | 1 | irreducible | NO |
| Proton (3,6 hyp.) | (3, 6) | 3 | 3 × (1,2) strands | needs confinement |

Under the (1,3) proton hypothesis, confinement is automatic:
three "quarks" are antinodes of one wave.  Under (3,6), an
external mechanism (waveguide cutoff) must prevent the strands
from separating — a known tension (R47 review, R50 F3).

For the electron sheet, all (n, 2n) harmonics with n ≥ 2 have
gcd = n ≥ 2 → reducible → strands → Coulomb fission.  The
only stable free mode on Ma_e is the fundamental (1, 2).

This is also why the "3-phase" character of the proton matters.
The (1,3) mode distributes energy in a three-fold symmetric
pattern around the ring — like 3-phase AC power with no zero
crossings.  The three phases are locked by the standing-wave
constraint; they cannot desynchronize or separate.  The
electron's (1,2) two-fold pattern is similarly locked, but
multi-electron composites (2,4), (3,6)... break this lock
because each strand has its own independent phase.
