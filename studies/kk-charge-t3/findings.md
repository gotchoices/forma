# R13. KK Charge from Flat T³ — Findings

## Track 1: KK mode spectrum and the electron's identity

**Script:** [`scripts/track1_kk_charge.py`](scripts/track1_kk_charge.py)

### F1. The electron is NOT a KK momentum mode

The KK mode (n₁, n₂, n₃) on T³ with circumferences L₁, L₂, L₃
has mass:

    m_KK c² = 2πℏc × √((n₁/L₁)² + (n₂/L₂)² + (n₃/L₃)²)

The electron wraps 68 times around the minor circle and 137
times around the major circle.  Its KK mode would be (68, 137, 0),
with mass:

    m_KK(68,137,0) ≈ 18 GeV

This is ~36,000 times the electron mass (0.511 MeV).

Even the simplest non-trivial KK mode has mass far above the
electron:

| Mode     | KK mass    | Ratio to m_e |
|----------|------------|--------------|
| (0,1,0)  | 71 MeV     | 139          |
| (1,0,0)  | 229 MeV    | 449          |
| (1,2,0)  | 270 MeV    | 528          |
| (68,137,0)| ~18 GeV   | ~36,000      |

The electron sits in the spectral gap between the zero mode
(massless, the 4D photon) and the first excited KK mode
(~71 MeV).  This is the same gap identified in R12 Track 1:
ω_C / ω_min ~ α.


### F2. KK mass ≠ Compton mass

The KK mass and the Compton mass are DIFFERENT formulas:

    E_KK = 2πℏc × √(Σ (n_a/L_a)²)   [√ of sum of squares]
    E_C  = 2πℏc / √(Σ (n_a L_a)²)    [1/√ of sum of squares]

For the electron geometry (L₁ = 2πa, L₂ = 2πR):

    E_KK(1,2,0)  = 270 MeV
    E_Compton     = 0.511 MeV

The Compton formula (path length = wavelength) gives the
correct electron mass.  The KK formula gives the mass of a
heavy mode that is NOT the electron.

The two formulas agree only when all circumferences are equal
(L₁ = L₂ = L₃).  For the electron's aspect ratio r ≈ 0.31
(L₁ ≈ 0.31 × L₂), they differ by orders of magnitude.


### F3. The electron is a WINDING mode

In string theory, states on compact spaces are characterized
by two types of quantum numbers:
- **Momentum** quantum numbers n_a: how many wavelengths fit
  around each circle.  KK modes.
- **Winding** quantum numbers w_a: how many times the string
  wraps around each circle.  Topological.

These have OPPOSITE scaling with the circumference L:
- Momentum mode mass ∝ n/L  (lighter at large L)
- Winding mode mass  ∝ wL   (lighter at small L)

The electron's compact space is very small (L ~ 10⁻¹⁵ m).
In this regime, winding modes are light and momentum modes
are heavy.  The electron is a winding mode:
- Winding numbers: (p, q) = (68, 137) on T²
- Effective compact momentum: ~zero (n_eff ~ 10⁻³)
- Mass from Compton condition: ℏc/(path length) = m_e c²

The key distinction: the electron's mass comes from the TOTAL
PATH LENGTH (how far the wave travels before closing), not
from its compact momentum (how many wavelengths fit on one
circumference).


### F4. Standard KK charge does NOT apply

In standard KK theory, the 4D electric charge of a particle
comes from its compact momentum:

    e_KK = g₄ × 2πn/L

where g₄ = g_D/√V is the 4D gauge coupling, n is the compact
momentum quantum number, and L is the circumference.

The electron has effectively zero compact momentum (n ~ 10⁻³).
The standard KK charge formula gives ~zero charge.

This is NOT a failure — it correctly tells us that the electron
is not a momentum-charged particle.  Its charge comes from a
different mechanism.


### F5. Charge from field configuration (WvM mechanism)

The electron's charge comes from the EM FIELD CONFIGURATION,
not from compact momentum.  Specifically:

The photon propagating along the geodesic has a polarization
vector (E-field direction) transverse to the propagation
direction.  As the photon winds around the compact space, the
polarization rotates relative to the 3+1D coordinate axes.
The time-averaged field has a net monopole moment — this IS
the charge.

In WvM's original derivation (on an embedded torus), the
curvature of the embedding causes the polarization to rotate.
The net radial E-field, integrated over the torus surface,
gives charge e.


### F6. The flat-T³ tension

On a flat T³, geodesics are straight lines in the covering
space.  Parallel transport along a straight line on a flat
manifold preserves vectors exactly — there is NO rotation.

This creates a tension:
- **Flat T³:** no curvature → no polarization rotation →
  no net monopole → no charge
- **Embedded torus:** curvature → polarization rotation →
  net monopole → charge e

The charge mechanism seems to require the photon's field to
"know about" the 3D embedding — specifically, how the compact
coordinates map to 3+1D spatial directions.  On a flat T³
with no embedding information, the field has no reason to
develop a monopole moment.

**This is the deepest version of the R12 inconsistency.**
R12 showed that mixing flat-T² and 3D-embedded physics is
inconsistent.  Track 1 shows that pure flat-T³ physics gives
no charge at all, while the embedded picture gives the right
charge but is inconsistent with the flat-T³ framework used
for mass and spin.

**Possible resolutions:**
1. The compact space is NOT perfectly flat — it has a small
   curvature that provides the polarization rotation.  The
   curvature would have to be specifically tuned to give the
   right charge.
2. The connection between compact and spatial dimensions is
   part of the metric (KK off-diagonal terms), and the charge
   arises from this connection, not from curvature.
3. The charge mechanism is not polarization rotation but
   something else entirely — perhaps related to the topology
   of the field configuration (winding number itself carries
   charge) rather than the geometry.
4. The field equation in 7D has cross-terms that couple compact
   and spatial degrees of freedom, even when the compact space
   is flat.  The charge might arise from these couplings.


---

## Conceptual implications

### F7. Winding vs momentum — a fundamental distinction

The KK framework assumes particles are momentum modes of
compact dimensions.  The WvM electron is a winding mode.
These are qualitatively different:

| Property       | Momentum mode     | Winding mode       |
|---------------|-------------------|---------------------|
| Mass           | ∝ n/L (heavy at small L) | ∝ wL/ℓ (light at small L) |
| Charge         | ∝ n/L (KK charge) | From field topology  |
| Quantization   | n = integer        | w = integer          |
| Light when     | L is large         | L is small           |

The electron is light because the compact space is small —
exactly the winding-mode regime.  This is why the electron
mass (0.511 MeV) is far below the KK gap (~71 MeV).

String theory's T-duality relates the two: momentum modes on
a circle of radius R ↔ winding modes on a circle of radius
α'/R.  This suggests there may be a dual description of the
electron as a momentum mode on a LARGE dual circle — but this
introduces the string tension α' as a new parameter.


### F8. What the correct calculation requires

To compute the electron's charge from first principles on T³,
we need to:

1. Write the full EM field of a photon propagating along the
   (68,137) geodesic on flat T³
2. Determine how the compact-space field couples to the 3+1D
   spatial dimensions (the embedding/metric question)
3. Compute the resulting 3+1D field at large distances
4. Extract the monopole moment = apparent charge

Step 2 is the crux.  It requires specifying how the compact
dimensions relate to the spatial dimensions — which is NOT
determined by the flat-T³ geometry alone.  It is additional
physical input.

In KK theory, this information lives in the metric's
off-diagonal components (the gauge connection A^a_μ).  In the
WvM picture, it comes from the 3D embedding.  These may be
equivalent descriptions of the same physics.


## Summary

| Finding | Result |
|---------|--------|
| Electron as KK mode | NO — mass is ~36,000× too high |
| Standard KK charge | Does not apply (zero compact momentum) |
| Electron identity | Winding mode (topological, not dynamical) |
| Charge mechanism | Field configuration / WvM, not KK momentum |
| Flat T³ charge | ZERO (no polarization rotation) |
| Key tension | Charge requires compact↔spatial coupling not present in flat T³ |

**The electron's charge cannot be computed from flat-T³ geometry
alone.**  Additional structure — either curvature, a metric
connection between compact and spatial dimensions, or a
non-geometric mechanism — is needed to generate the monopole
moment.

This does NOT invalidate the WvM model or the compact-dimension
framework.  It identifies the specific missing ingredient: the
coupling between compact and spatial degrees of freedom.


---

## Track 2: Four candidate charge mechanisms

**Script:** [`scripts/track2_charge_mechanisms.py`](scripts/track2_charge_mechanisms.py)

### F9. Resolution 4 (7D cross-terms) is RULED OUT

The 7D Maxwell equations on flat T³ give zero volume-averaged
4D current: ∫_T³ ∂_a F^aν d³y = 0 by periodicity.  A winding
mode on flat T³ produces NO long-range Coulomb field.  This
confirms F6 through a rigorous, independent argument.


### F10. Resolution 1 (curvature) — viable but needs non-standard gravity

Einstein gravity gives compact curvature ~10⁻¹⁶ m⁻².  The
embedded torus has curvature ~10²⁹ m⁻².  The ratio is ~10⁴⁵ —
standard gravity is hopelessly weak.

However, the required G_eff/G ratio (~10⁴⁵) is essentially
the same as the EM-to-gravity force ratio between electrons
(~4 × 10⁴²).  This is the hierarchy problem restated:
unifying charge with gravity at the compact scale requires
explaining why gravity is so weak compared to EM.

If solved, this resolution would unify EM and gravity through
7D geometry — the strongest possible outcome.


### F11. Resolution 2 (gauge connection) — explains quantization, not α

Off-diagonal KK metric terms can give winding modes a charge
proportional to their winding number.  This explains:
- Charge quantization (integer winding → integer charge units)
- Why only winding modes are charged
- The Aharonov-Bohm–like mechanism (Wilson line around compact dim)

But the value of α is encoded in a background gauge flux Φ₀,
which is a free parameter.  The problem shifts from "what
determines the geometry?" to "what determines the background
flux?"


### F12. Resolution 3 (topological charge) — most elegant, needs theorem

If winding number IS charge (analogous to how Chern number IS
magnetic monopole charge), then charge quantization and
conservation are automatic.  Fractional charges from T³ linking
are natural.

This requires a mathematical theorem: any smooth EM field on
M₄ × T³ with winding number w has 4D monopole moment ∝ w.
Whether such a theorem exists is an open question.  If it does,
it would be the strongest foundation for the model.

Does not determine α by itself — the "charge per winding" is
a separate question.


### F13. The combined picture

The three surviving resolutions are not mutually exclusive.
A combined picture:

1. The compact space has curvature (from some mechanism
   stronger than Einstein gravity)
2. This curvature creates off-diagonal metric terms coupling
   compact and spatial dimensions
3. Winding modes couple to these terms with strength ∝ winding
   number (topological charge quantization)

In this picture:
- Charge = winding number × curvature-dependent coupling
- α = f(compact curvature, geometry)
- Gravity and EM are both aspects of 7D geometry
- The hierarchy problem = why compact curvature is small


### F14. The key unknown

What determines the compact-space curvature?  Candidates:
- Flux compactification (string theory mechanism)
- Casimir energy of the compact space
- Topological stability constraint on winding modes
- Non-Einsteinian gravity at the compact scale


## Summary (Tracks 1 + 2)

| Finding | Result |
|---------|--------|
| Electron as KK mode | NO — winding mode, not momentum mode |
| Standard KK charge | Does not apply (zero compact momentum) |
| Flat T³ + Maxwell | ZERO charge (rigorously proven) |
| Curvature (Res. 1) | Viable if gravity is stronger at compact scale |
| Gauge connection (Res. 2) | Explains quantization, not α |
| Topological charge (Res. 3) | Elegant, needs mathematical theorem |
| 7D cross-terms (Res. 4) | RULED OUT (periodicity kills monopole) |
| Combined picture | Curvature + gauge connection + topological quantization |
| Key unknown | What determines compact-space curvature |
| Gravity connection | Hierarchy problem ↔ charge mechanism |


## Scripts

- [`scripts/track1_kk_charge.py`](scripts/track1_kk_charge.py)
  — KK mode spectrum, geodesic wave analysis, winding vs
  momentum identification
- [`scripts/track2_charge_mechanisms.py`](scripts/track2_charge_mechanisms.py)
  — Four charge mechanisms: curvature, gauge connection,
  topological, cross-terms
