# Q34. The charge mechanism problem: how does the electron have charge?

**Status:** open — Path 7 → R15, Path 5 → R16, Paths 4+5 → R17.
Remaining paths (1–3, 6, 8) await triage.
**Source:** R13 Track 3 conclusion, user brainstorm
**Connects to:** Q42, Q44 (wave-language versions of Path 5), Q47
(geometric interpretation of α running — connects to Path 3),
Q51 (mode-coupling route to α), Q52 (aspect ratio)

---

## The tension

R13 Track 3 showed that the R8 multi-winding (68, 137)
model breaks WvM's charge mechanism.  WvM's charge requires
p = 1 (one tube winding per wavelength = commensurability
between polarization rotation and frame rotation, so E always
points outward).  R8's multi-winding model has p = 68, destroying
this.  The root cause is α ≈ 1/137: at the Compton scale
(where p = 1 works), U_Coulomb = α × m_e c² — a factor of
~137 too small (R7).  Shrinking the torus to fix the Coulomb
energy forces multi-winding, which breaks charge.

## Eight candidate paths

**Path 1. Compact-space refractive index.** If c_sub < c in
the material space, a photon at Compton frequency has shorter
wavelength, fitting into a smaller torus with p = 1.  Need
c_sub/c ≈ α.  Waveguides routinely have effective speeds < c.
Could c_sub be determined by the geometry?

**Path 2. Compact metric scale factor.** Equivalent to Path 1
in KK language: a conformal factor in the material metric that
plays the role of α.

**Path 3. Membrane permeability.** If only a fraction of the
photon's field leaks into 3D, the apparent charge is reduced.
If the leakage fraction ≈ α, this explains U_Coulomb = α × m_e c²
at Compton scale.  The torus stays at Compton scale with p = 1,
preserving charge.  Charge = √α × e_bare.  Connects to running
of α (higher energy probes penetrate deeper into material space).

**Path 4. Geometric projection factor.** The solid angle
subtended by the torus tube, or the ratio of material to 3D
surface area at the embedding, could provide a geometric
suppression ≈ α.  Calculable from embedding geometry.

**Path 5. Harmonic decomposition of the confined photon.**
→ **R16** [`studies/R16-harmonic-charge/`](../studies/R16-harmonic-charge/).
The embedding curvature redistributes the (1,2) plane wave's
energy across Fourier modes; only the p = 1 component produces
charge; if that fraction = α, we have a derivation.
Complementary to R15 (numerical); R16 seeks the analytical
explanation.  "Two photons beating" version ruled out by
energy conservation — see R16 README for details.

**Path 6. Topological charge (winding number IS charge).**
Decouple charge from the commensurability argument entirely.
The winding number is a topological invariant that IS the
charge, with the coupling strength to 3D fields determined by
some geometric factor = α.  Needs a mathematical framework
beyond WvM.

**Path 7. Keep (1, 2) at Compton scale; reinterpret Coulomb
energy.** → **R15** [`studies/R15-forward-charge/`](../studies/R15-forward-charge/).
Run R7's calculation forward: energy + topology → charge → α.
See R15 README for full analysis of how R7 → R8 → R13 led
back here.

**Path 8. Different material topology.** The torus is WvM's
choice but not the only option.  Lens spaces, spheres, or more
exotic manifolds could have different charge mechanisms and
mode structures.
