# R56: Electron shell structure — Findings

See [README.md](README.md) for track framing, prior work, and
open directions.

---

## Track 1: Classical packing of distributed-charge electrons

### F1. Shell structure does NOT emerge from geometric packing

Energy minimization of Compton-scale charged spheres around a
point nucleus produces a smooth energy landscape with no
discontinuities at 2, 8, or 18 electrons.

| N | ΔE per electron (keV), model A |
|---|---|
| 1 | −38.4 |
| 2 | −36.7 |
| 3 | −35.5 |
| 4 | −33.8 |
| 5 | −8.1 |

No sharp closure at N=2.  Both size models (R = 751 fm and
R = 386 fm) give the same qualitative result.

### F2. Why classical packing fails

The distributed charge makes close-range repulsion SOFTER,
which makes packing EASIER — the opposite of what's needed
for shell closure.  No mechanism in classical packing makes
one specific electron count per shell energetically special.

### F3. Conclusion: shell structure is genuinely quantum

The MaSt insight (electrons have Compton-scale spatial extent)
is real but insufficient to derive shell structure.  The Pauli
exclusion principle is not a geometric consequence of packing.

---

## Track 2: Couplet packing

### F4. Electron couplets: charge −2, spin 0, no magnetic moment

Two electrons at the same S coordinate with opposite tube
winding (+1 and −1) form a couplet:

| Property | Couplet | Single electron |
|----------|---------|----------------|
| Charge | −2e | −e |
| Spin | 0 | ½ |
| Magnetic moment | 0 (dipoles cancel) | ±μ_B |

### F5. The first couplet encloses the nucleus

At Z = 10, a single couplet optimizes at r = 1.66 pm — INSIDE
its own effective radius of 7.51 pm.  The electron bubble wraps
around the nucleus.

### F6. Couplet packing shows weak structure, not clean shells

At Z = 18 free packing: ΔE at N=7 and N=9 shows some
structure, but results are noisy.  All couplets sit at nearly
the same radius (~7.5 pm).  Not definitive.

### F7. The core+ring assumption was the problem (see Track 3b)

---

## Track 3: Diameter sweep

### F8. The marginal energy ratio is exactly 0.50 — independent of R_eff

For the ring-around-core geometry, ΔE_5 / ΔE_4 = 0.50 at
EVERY electron diameter tested, from 10 fm to 15,000 fm.
This is a geometric identity, not a function of electron size.

### F9. Shell 2 closure at 5 ring couplets (ΔE_6 goes positive)

The 6th ring couplet costs energy.  Geometric ring capacity =
5 couplets (10 electrons).  Close to but not exactly 8.

### F10. The electron's EM diameter does NOT affect shell structure

The marginal energy fractions are purely geometric.  Shell
structure comes from Coulomb geometry in S, not from the
electron's internal structure on Ma.

### F11. The core+ring assumption is WRONG

A comparison of 5-couplet configurations at Z = 10:

| Configuration | Energy (keV) | Rank |
|---|---|---|
| 2 polar + 3 equatorial (bipyramid) | −142.03 | **1 (best)** |
| 1 core + 4 ring (Track 3 assumption) | −131.67 | **5 (worst)** |

The core couplet migrates out to join the ring.  All couplets
prefer equal distance from the nucleus.

---

## Track 4: Free 3D couplet packing

### F12. All couplets collapse to one shell at R_eff

With free 3D optimization, all couplets settle at the SAME
radius (~7.5 pm = R_eff).  No second shell forms.  The shell
theorem (constant potential inside a uniform sphere) erases
radial differentiation.

### F13. ΔE decreases smoothly — no shell closure

At Z = 18, the marginal energy per couplet decreases from
−54.9 keV (N=4) to −12.4 keV (N=11) with no sharp
discontinuity.

### F14. The uniform-sphere model may be too soft

A ring or torus of charge (rather than a uniform sphere) has
non-constant interior potential and might produce different
packing physics.  Not yet tested.

### F15. Bimodal structure appears at small Z

At Z = 2N (neutral atoms), N = 4 (Z=8) and N = 5 (Z=10)
show bimodal radius distributions — some couplets closer,
some farther.  At N = 6+ this collapses to one shell.

---

## Track 5: Torus standing waves and orientation packing

### F16. Shell radii ARE the Bohr radii — same physics, physical object

The standing-wave condition 2πr = nλ_dB gives r = n² a₀/Z.
In MaSt: the electron is a physical torus fitting integer
wavelengths around the nucleus, not a point with an abstract
wave property.  At n=1, ~70 torus diameters fit around the
orbit.

### F17. Solid-angle packing does NOT give n²

A torus at the Bohr radius subtends ~6×10⁻⁴ sr.  Maximum
non-overlapping count is ~20,000 at n=1 — vastly more than
n² = 1.  Physical packing does not constrain the angular count.

### F18. The n² IS a closure condition — same as Ma quantization

The constraint l < n (angular nodes < radial wavelengths) is
the SAME closure condition that quantizes modes on the Ma
torus: the pattern must return to its starting point.  On Ma →
particle masses.  In S → shell structure.  One mechanism, two
domains.

### F19. Summary: what MaSt explains and what it doesn't

**Derived from MaSt:**
- The factor of 2 (tube winding topology: n₁ = ±1)
- The Bohr radii (standing-wave closure of a physical torus)
- The l < n constraint (angular closure = Ma closure in S)
- Unification: Ma quantization and S shell quantization are
  the same mechanism

**Not derived from MaSt (standard QM, reinterpreted):**
- The n² angular count (spherical harmonics)
- The Madelung filling order (4s before 3d)
- Wavefunction antisymmetry (Pauli beyond the factor of 2)
