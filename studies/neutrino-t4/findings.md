# R26 Findings

## Track 1a: Neutrino T² mode spectrum

### F1. Assignment A ratio — algebraically exact, r-independent

The mass-squared ratio for Assignment A (modes (1,1), (−1,1), (1,2)) is:

    Δm²₃₁/Δm²₂₁ = (3 − 2s) / (4s)

This depends **only** on shear s₃₄.  The aspect ratio r cancels completely.
Verified numerically at r = 0.5, 1, 2, 5, 10 — identical to 6 decimal places.

Required shear: **s₃₄ = 0.02199** for ratio = 33.60 (experimental value).

### F2. Assignment A has a cosmological mass problem

At physical scale (E₀ = √(Δm²₂₁/(4s)) = 29.26 meV):

| r | m₁ (meV) | m₂ (meV) | m₃ (meV) | Σm (meV) | Status |
|---|----------|----------|----------|----------|--------|
| 1.0 | 40.9 | 41.8 | 64.8 | 147.6 | ✗ exceeds 120 |
| 3.0 | 30.2 | 31.5 | 58.7 | 120.4 | ✗ marginal |
| r → ∞ | 28.6 | 29.9 | 57.9 | 116.4 | ✓ barely |

Assignment A's three neutrinos are **too heavy** at moderate r.  The
cosmological bound Σm < 120 meV is satisfied only for r ≳ 5, where the
1/r² term becomes negligible.  In this limit the three masses are almost
entirely determined by the ring quantum number n₄ and shear:

    m₁ ≈ E₀(1−s),  m₂ ≈ E₀(1+s),  m₃ ≈ E₀(2−s)
    Σm → E₀(4−s) ≈ 116.4 meV

This is a second problem for Assignment A, independent of the spin problem.

### F3. Assignment B — refined parameters

The README's initial estimate (s = −0.09, r = 1.0) gives ratio 33.71
(0.10 off target).  Grid search found the exact solution:

    **s₃₄ = −0.0253,  r = 1.926**  →  ratio = 33.603

At physical scale (E₀ = 5.64 meV):

| Mode | Mass (meV) | Spin |
|------|-----------|------|
| (1,2) = ν₁ | 11.80 | ½ F |
| (3,2) = ν₂ | 14.65 | ½ F |
| (17,2) = ν₃ | 51.67 | ½ F |
| **Σm** | **78.1** | **✓** |

Σm = 78.1 meV — well within the cosmological bound.

### F4. Assignment B — 26 sterile neutrinos (much worse than expected)

The README estimated ~6 intermediate spin-½ modes.  The full catalog
reveals **26 intermediate spin-½ fermion modes** between ν₂ and ν₃.

This happens because each odd |p| value produces four modes:
(+p,+2), (−p,+2), (+p,−2), (−p,−2), grouped into two mass doublets:
- (+p,+2) and (−p,−2):  μ² = p²/r² + (2−ps)²
- (−p,+2) and (+p,−2):  μ² = p²/r² + (2+ps)²

For |p| ∈ {5, 7, 9, 11, 13, 15}: 6 × 4 = 24 modes.
Plus (−17,+2) and (+17,−2): 2 more modes just below ν₃.
Total: 26 intermediate spin-½ fermions.

If these thermalize, each contributes to N_eff.  The Standard Model has
N_eff = 3.044.  Planck constrains N_eff < 3.29 (95% CL).  Even one extra
species thermalizing would violate this bound.  26 sterile neutrinos is
catastrophic unless a suppression mechanism exists.

### F5. Mode proliferation — thousands of sub-eV modes

Both assignments produce enormous numbers of modes below 1 eV:

| Assignment | r | Modes < 1 eV | Spin-½ fermions |
|-----------|---|-------------|----------------|
| A | 1.0 | 3,670 | 68 |
| A | 3.0 | 11,020 | 204 |
| B | 1.926 | 3,720 | 60 |

Most modes are non-fermion (spin-1 fermions, bosons, or higher-spin).
The spin-½ fermion count is manageable IF a selection rule prevents them
from coupling to the weak interaction.  Without such a rule, any of
these modes could be produced in decays.

### F6. Physical scales

| Assignment | E₀ (meV) | L₄ (μm) |
|-----------|---------|--------|
| A | 29.26 | 42.4 |
| B | 5.64 | 219.7 |

Assignment B requires a much larger neutrino T² — L₄ ≈ 220 μm.  This
is within the current experimental bound on deviations from Newtonian
gravity (~ 50 μm), but only if gravity does not propagate in these
compact dimensions.

### F7. Summary of Assignment A vs B scorecard

| Criterion | Assignment A | Assignment B |
|-----------|-------------|-------------|
| Δm² ratio | ✓ exact (r-free) | ✓ exact (at s,r) |
| All spin-½ | ✗ two spin-1 | ✓ all spin-½ |
| Σm < 120 meV | ✗ (needs r ≳ 5) | ✓ (78 meV) |
| Sterile neutrinos | many (all spin types) | 26 spin-½ fermions |
| Parameter freedom | 1 free (r) | 0 free (s,r both fixed) |
| Falsifiability | testable via Σm | testable via sterile ν |

Assignment B is better on spin and cosmology but worse on sterile
neutrinos.  Neither assignment is clean.  Tracks 1b–1f investigate
whether the mode menu can be changed (non-coprime modes, revised spin/
charge formulas) to find a better solution.

### F8. Assignment A is the electron's mode pattern, downscaled

Assignment A's triplet (1,1), (−1,1), (1,2) is the same mode pattern
that exists on the electron T²: the electron is (1,2), and the two
nearest modes with the same tube winding are (1,1) and (−1,1).
Assignment A places this pattern on a separate T² at a larger scale.

This means Assignment A is equivalent to asking: "at what scale does
the electron's mode pattern produce the neutrino mass splittings?"
The answer is E₀ ≈ 29 meV (L₄ ≈ 42 μm) — the same mode geometry,
10⁸× larger.

### F9. The μm torus size is a hard constraint, not a modeling choice

A neutrino mass eigenstate is a particle at rest with energy m_ν c².
In the WvM framework, this rest energy IS the mode energy on the
compact space: E = E₀√((n₃/r)² + (n₄ − n₃s)²).  Because the mode
energy and mode differences both scale linearly with E₀ = ℏc/L₄,
you cannot make the modes high-frequency while keeping the differences
small — everything scales together.

The neutrino cannot be a "beat" between high-frequency modes on a
smaller torus.  A beat frequency determines the oscillation rate
(which is Δm²/E), but the particle's rest mass is the individual
mode energy, not the beat.  Experiment bounds each neutrino mass to
≲ 50 meV, which requires E₀ ~ meV, which requires L₄ ~ μm.

This makes the μm neutrino T² one of the model's most distinctive
predictions — and one of its most testable.  Short-range gravity
experiments probing below 50 μm could detect the extra dimensions
if gravity propagates there.

---

## Track 1b: All-spin-½ triplet search

### F10. 175 of 286 triplets match the ratio — non-selective

Searched all C(13,3) = 286 triplets of odd p values from 1 to 25.
175 triplets (61%) produce a (s, r) solution matching Δm²₃₁/Δm²₂₁ =
33.6 ± 0.9.  The ratio constraint alone does not select a unique
mode assignment — many triplets work.

### F11. No clean solution exists

**No triplet with p ≤ 25 achieves both zero sterile neutrinos and
Σm < 120 meV.**

The minimum sterile counts are:

| Min N_sterile | Triplets | Σm status |
|--------------|----------|-----------|
| 2 | (7,11,13), (9,11,13), (1,3,5), ... | All ✗ (Σm = 140–510 meV) |
| 6 | **(3,7,11)**, **(3,9,13)**, ... | Some ✓ |
| 10 | (5,9,15), (1,9,15), ... | Most ✓ |

The two best viable candidates:

| Triplet | s | r | Σm (meV) | N_sterile | L₄ (μm) |
|---------|------|------|---------|----------|---------|
| (3,7,11) | 0.379 | 9.17 | 96.3 | 6 | 56.7 |
| (3,9,13) | 0.292 | 8.51 | 117.4 | 6 | 50.3 |

### F12. The sterile count is structural — cannot reach zero

The minimum achievable sterile count for any triplet that also
satisfies the cosmological bound is **6**.  This is structural:

1. **Gap modes:** Between p₂ and p₃ there is always at least one
   odd integer (since p₃ − p₂ ≥ 4 for the ratio to be large enough).
   Each intermediate odd |p| produces 4 modes: (±p, ±2).
2. **Low-p modes:** The p = 1 modes (±1, ±2) are lighter than most
   triplet members and often fall in the ν₂–ν₃ gap.
3. **Scaling law:** N_sterile ≈ 4 × (number of odd integers between
   p₂ and p₃) + boundary contributions.

The ratio ≈ 33.6 requires μ²(p₃)/μ²(p₁) ≫ 1, which forces a large
span p₃ − p₁.  Narrowing the span to minimize sterile modes pushes
the individual masses up (larger E₀), violating the cosmological bound.
These two constraints work against each other, producing an irreducible
minimum of 6 sterile spin-½ fermion modes.

### F13. Consecutive-p triplets minimize sterile count but fail cosmology

Triplets with smallest p₃ − p₂ gap (consecutive odd: p₃ = p₂ + 2)
achieve N_sterile = 2, but all require Σm > 140 meV, exceeding the
cosmological bound.  Examples:

    (7,11,13): Σm = 307 meV,  N_sterile = 2
    (1, 3, 5): Σm = 151 meV,  N_sterile = 2
    (1, 7, 9): Σm = 140 meV,  N_sterile = 2

The conflict: consecutive p values give small splittings only at large
s (strong shear) and large r, which pushes E₀ high and Σm above the
cosmological bound.

### F14. Track 1b conclusion — Assignment B definitively fails

The sterile neutrino problem cannot be solved within the all-spin-½
(p, 2) framework:

- Zero-sterile solutions do not satisfy cosmology
- Cosmology-satisfying solutions have ≥ 6 sterile neutrinos
- The conflict is structural (scaling law), not accidental
- Extending to p > 25 makes things worse (more intermediate modes)

This closes Assignment B.  The remaining paths are:
- Track 1c: non-coprime or cross-plane modes (different mode menu)
- Track 1d: revised spin formula (rescue Assignment A)
- Track 1e: revised charge formula (change which modes are uncharged)
- Track 1f: direct spin resolution for Assignment A

---

## Track 1c: Non-coprime and higher-order modes

### F15. Non-coprime modes are harmonics, not new fundamentals

A non-coprime mode (n₃, n₄) with d = gcd(|n₃|, |n₄|) > 1 decomposes
as d × (p, q) where (p, q) is a coprime fundamental.  It has:

- **Same spin** as the fundamental: L_z = ℏ/|q|
- **d × the energy** of the fundamental (d wavelengths fit in the path)
- **Same fermion/boson classification** (determined by |p| odd/even)

Example: mode (2,4) is the 2nd harmonic of (1,2).  It has spin-½ and
twice the electron's mass, not a new particle type.

### F16. Non-coprime modes worsen the sterile neutrino problem

Including non-coprime modes in the spectrum adds 472 additional spin-½
fermion modes below 1 eV (at Assignment A parameters), on top of the
200 coprime spin-½ fermions.  Total: 672 spin-½ fermion modes below 1 eV.

Non-coprime harmonics fill in the gaps between coprime modes, making
the spectrum denser.  A triplet like (1,2), (2,4), (10,20) — all
harmonics of (1,2) — gives ratio ≈ 33 but has **88 intermediate
spin-½ fermion modes**, far worse than the coprime search (minimum 6).

### F17. Cross-plane modes on T⁶ are too heavy to be neutrinos

A cross-plane mode has nonzero winding on two or more T² subplanes.
In the zero-cross-shear limit, its energy is:

    E² = E²_e(n₁,n₂) + E²_ν(n₃,n₄) + E²_p(n₅,n₆)

The lightest cross-plane mode involving the neutrino T² has
E ≥ √(m_e² + m_ν²) ≈ 511 keV — ten billion times heavier than
the neutrino.  Even with cross-shear, the mixing amplitude is
suppressed by (m_ν/m_e)² ~ 10⁻¹⁷.  Cross-plane modes cannot
create new light states.

Cross-plane modes are relevant for PMNS mixing (perturbative
coupling) and heavy sterile neutrinos (MeV–GeV), but not for
the three light mass eigenstates.

### F18. Track 1c conclusion — the mode menu is closed

No non-coprime mode or cross-plane mode provides a new spin-½
neutrino candidate.  The complete spin-½ fermion menu on the
neutrino T² is:

    (p, ±2)  with p odd,  for all p = ±1, ±3, ±5, ...

This was already fully explored in Track 1b.  The mode menu
cannot be expanded to solve the sterile neutrino problem.
Remaining paths: Tracks 1d–1f (revise the spin/charge formulas,
or rescue Assignment A).

---

## Track 1d: Spin formula at finite a/R

### F19. The thin-torus spin formula breaks down dramatically at finite ε

The orbital angular momentum of a photon on a (p,q) geodesic at
finite ε = a/R is:

    ⟨L_z⟩ = hqπ(2 + ε²) / I²(ε)

where I(ε) = ∫₀²π √(p²ε² + q²(1+ε cos pt)²) dt is the path
length in units of R.  The spin correction factor S(ε) = ⟨L_z⟩/(ℏ/q)
deviates from 1 as soon as ε > 0.1:

| Mode | S(0) | S(0.5) | S(1.0) | S(2.0) | S(6.6) |
|------|------|--------|--------|--------|--------|
| (1,2) | 1.00 | 1.05 | 1.06 | 0.88 | 0.73 |
| (1,1) | 1.00 | 0.88 | 0.66 | 0.45 | 0.35 |
| (3,2) | 1.00 | 0.70 | 0.42 | 0.25 | 0.19 |
| (5,2) | 1.00 | 0.43 | 0.20 | 0.11 | 0.08 |

Higher tube winding (p) causes faster decay of S(ε).

### F20. The tube winding p DOES affect spin at finite ε

Contrary to the thin-torus formula L = ℏ/q (p-independent), the
orbital angular momentum at finite ε depends strongly on p.  At
ε = 6.6 (electron):

    (1,2): L_z/ℏ = 0.365
    (3,2): L_z/ℏ = 0.095
    (5,2): L_z/ℏ = 0.039

These are radically different.  The thin-torus prediction (0.500
for all) is qualitatively wrong at the electron's aspect ratio.

### F21. The (1,1) mode crosses spin-½ at ε ≈ 1.6

L_z/ℏ for (1,1) decreases monotonically from 1.000 at ε = 0 to
~0.338 as ε → ∞.  It passes through 0.500 at **ε ≈ 1.6**.

This means: at aspect ratios ε > 1.6, the (1,1) mode has orbital
angular momentum closer to ℏ/2 (spin-½) than to ℏ (spin-1).
Since (1,1) is a fermion (p = 1, odd), the nearest allowed quantum
spin is ½.  **Assignment A's spin problem may be resolved at
finite ε.**

### F22. All modes converge at large ε

At large ε, all modes' orbital angular momentum converges to a
common limit near ~0.34ℏ:

    ε = 10:  (1,2) → 0.360,  (1,1) → 0.343,  (3,2) → 0.093

The (1,2) and (1,1) modes converge tightly.  Higher-p modes
converge to smaller values.  At the regime relevant for Assignment A
(ε > 5), both (1,1) and (1,2) have similar L_z ≈ 0.35ℏ — both
closer to spin-½ than to any other value.

### F23. Higher-p modes lose spin-½ character at finite ε

Track 1b's search relied on (p,2) modes with p = 3, 5, ..., 17
all being spin-½.  At finite ε, this fails:

| Mode | L_z/ℏ at ε=1.93 | L_z/ℏ at ε=6.6 | Nearest ½-integer |
|------|-----------------|----------------|-------------------|
| (1,2) | 0.444 | 0.365 | ½ |
| (3,2) | 0.130 | 0.095 | ½ (but barely) |
| (5,2) | 0.055 | 0.039 | ½ (nominal only) |
| (17,2) | 0.005 | 0.004 | ½ (indistinguishable from 0) |

While fermions (odd p) must have half-integer spin, a mode with
L_z/ℏ = 0.005 is spin-½ only in the most formal sense.  It
carries negligible angular momentum and would not behave as a
spin-½ particle in interactions.  The practical spin-½ sector
at finite ε is much smaller than the thin-torus prediction.

### F24. Assignment A is rehabilitated; Assignment B is undermined

The finite-ε calculation reverses the thin-torus spin assessment:

**Assignment A — improved:**
- (1,1) crosses spin-½ at ε ≈ 1.6
- At ε > 5 (needed for cosmology), both (1,1) and (1,2) have
  L_z ≈ 0.35ℏ — effectively the same spin-½ fermion
- The spin problem that blocked Assignment A at ε = 0 dissolves
  at realistic aspect ratios

**Assignment B — undermined:**
- (3,2), (5,2), (17,2) have negligible angular momentum at finite ε
- Calling them "spin-½" is formally correct (fermions, nearest
  half-integer) but physically hollow
- Assignment B relied on the thin-torus spin classification, which
  is not valid at ε > 0.5

### F25. Caveat — point-particle orbital angular momentum only

This calculation computes the ORBITAL angular momentum of a
point-particle photon on a geodesic.  The photon's intrinsic spin
(helicity ±ℏ) has a z-projection that averages to zero for integer p.
The full EM field calculation may include additional contributions
from the field structure (polarization distribution, evanescent
coupling).  The point-particle result should be viewed as establishing
the DIRECTION and MAGNITUDE of finite-ε corrections, not as the final
word on quantum spin.

Crucially: the electron (1,2) at ε = 6.6 has L_z = 0.365ℏ, below
the expected 0.500ℏ.  The electron IS spin-½ experimentally.  This
implies either: (a) the embedded-torus orbital angular momentum is
not the full picture (field contributions restore L_z to ℏ/2), or
(b) the electron's ε is lower than 6.6 (S2's value used a/R for
field extent, not orbit).  Either way, the qualitative finding —
finite-ε corrections are large and p-dependent — is robust.

---

## Track 1e: Charge via parallel transport

### F26. Geodesic torsion confirms p turns per circuit

The geometric phase (rotation of the surface normal n̂ relative to
a parallel-transported frame) for a (p,q) curve on a thin torus
equals exactly p full rotations per circuit, independent of q:

| Mode | Geometric turns | Expected |
|------|----------------|----------|
| (1,2) | 1.0000 | 1 |
| (3,2) | 2.9998 | 3 |
| (5,2) | 4.9987 | 5 |
| (7,2) | 6.9961 | 7 |
| (1,1) | 1.0000 | 1 |
| (1,3) | 1.0000 | 1 |
| (2,1) | 1.9997 | 2 |

This is the geodesic torsion integral: τ_g = p.  The wave phase
makes exactly 1 rotation per circuit.  For net charge (⟨cos φ⟩ ≠ 0),
the wave and geometric rotations must be commensurable.  This
selects p = 1 modes as charged, p > 1 as uncharged.

### F27. Frenet and surface transport agree for (p,2) modes

For all (p,2) modes at thin torus (ε = 0.01), the normalized charge
fractions from both transport laws agree to < 0.001:

| Mode | Q_geom | Q_frenet | Match |
|------|--------|----------|-------|
| (1,2) | 1.0000 | 1.0000 | ✓ |
| (3,2) | −0.0001 | −0.0000 | ✓ |
| (5,2) | −0.0003 | −0.0000 | ✓ |
| (7,2) | −0.0006 | +0.0000 | ✓ |
| (2,1) | −0.0003 | −0.0000 | ✓ |

Both methods confirm: among (p,2) modes, only p = 1 carries charge.
The knot-zoo's Frenet frame result is correct for these modes.

### F28. Frenet and surface transport DISAGREE for different q values

The two transport laws give dramatically different charge magnitudes
when q varies:

| Mode | Q_geom (norm) | Q_frenet (norm) | Ratio |
|------|--------------|----------------|-------|
| (1,1) | 1.0000 | 8.6143 | 8.6× |
| (1,3) | 1.0000 | −0.2582 | −0.26× |

Both methods agree that (1,1) and (1,3) are CHARGED (p = 1), but
they disagree wildly on the relative magnitude.  The Frenet method
gives (1,1) 8.6× the charge of (1,2), while the surface transport
method gives them identical charge.

This matters for Assignment A, whose three modes are (1,1), (−1,1),
(1,2) — spanning q = 1 and q = 2.  The relative charge magnitudes
depend on which transport law is physical.

The discrepancy arises because the Frenet frame of a 3D curve depends
on the embedding curvature (both geodesic and normal curvature), while
the surface parallel transport depends only on the intrinsic surface
geometry (which is flat for T²).  For modes with the same q, the
embedding contributions largely cancel in the ratio; for different q,
they do not.

### F29. Finite a/R introduces charge leakage to higher-p modes

At large aspect ratios, the geometric method gives nonzero normalized
charge to (3,2) and (5,2) modes, while the Frenet method keeps them
at zero:

| ε = a/R | Q_geom(3,2) | Q_geom(5,2) | Q_frenet(3,2) | Q_frenet(5,2) |
|---------|-------------|-------------|---------------|---------------|
| 0.01 | −0.0001 | −0.0003 | 0.0000 | 0.0000 |
| 0.5 | 0.0140 | 0.0777 | 0.0000 | 0.0000 |
| 1.0 | −0.4713 | −0.4637 | 0.0000 | 0.0000 |
| 2.0 | 2.3827 | 2.5494 | 0.0000 | 0.0000 |

At ε ≥ 1, the geometric method shows ~50% charge leakage to p = 3
and p = 5 modes.  This is because the embedding curvature at large ε
distorts the relationship between wave phase and geometric phase: the
path is no longer geodesically "simple" on the embedded surface.

The Frenet method maintains zero charge for p > 1 at all ε.  Which
method is correct depends on the physical model:
- If the E-field rotates in the surface-normal frame → geometric
- If the E-field rotates in the Frenet frame of the 3D curve → Frenet

### F30. Track 1e conclusions

1. **Knot-zoo confirmed for (p,2) modes:** Both transport laws agree
   that only (1,2) is charged among modes with q = 2.  The charge
   mechanism is the commensurability between wave phase (1 turn) and
   geodesic torsion (p turns) — only p = 1 achieves resonance.

2. **Transport laws diverge across q values:** The (1,1) vs (1,2)
   charge ratio differs by 8.6× between methods.  This is a genuine
   physical ambiguity: the correct answer depends on whether
   polarization transport follows the surface geometry or the 3D
   Frenet frame.

3. **Assignment A charge coupling:** All three modes (1,1), (−1,1),
   (1,2) are charged in both methods (p = 1).  All couple to the
   weak interaction.  ✓

4. **Assignment B receives a third fatal blow:** Only (1,2) is
   charged; (3,2) and (17,2) are uncharged (p > 1).  Two of the
   three neutrino mass eigenstates would not couple to the weak
   force and could not be produced in beta decay.  Combined with
   the sterile neutrino problem (Track 1b) and the spin problem
   (Track 1d), Assignment B fails on three independent grounds.

5. **Open question for Track 1f:** The transport-law ambiguity
   affects Assignment A's phenomenology.  If (1,1) and (1,2) have
   identical weak charge (surface transport), they would be produced
   equally in weak processes.  If (1,1) has 8.6× the charge (Frenet),
   the production asymmetry changes the oscillation pattern.  This
   should be resolved by determining which transport law follows from
   the WvM Maxwell equations on T².
