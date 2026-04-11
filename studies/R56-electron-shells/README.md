# R56: Electron shell structure from geometric packing

**Status:** Framed
**Questions:** Can distributed-charge electrons, packed around a
nucleus by energy minimization, reproduce the 2, 8, 18 shell
structure without invoking the Pauli exclusion principle?
**Type:** compute
**Depends on:** R53 (electron Compton scale), model-E (electron
as near-spherical torus)

---

## Motivation

Standard quantum mechanics derives the shell structure 2, 8, 18,
32 from the degeneracy of spherical harmonics in a 1/r Coulomb
potential, combined with the Pauli exclusion principle (no two
electrons share the same quantum state).  The exclusion principle
is an axiom — it is not derived from anything deeper.

Model-E provides a different starting point.  The electron is not
a point particle — it is a nearly-spherical torus with tube
circumference ≈ Compton wavelength (~4,700 fm ≈ 4.7 pm).  At
ε = 397, the torus hole is negligible and the charge distribution
is effectively a spherical shell.  The electron's spatial extent
is a significant fraction of the Bohr radius (53 pm):

> R_electron / R_Bohr ≈ 0.75 pm / 53 pm ≈ 1/70

This means electrons in an atom are not points orbiting far from
each other — they are extended objects that overlap significantly
in the inner shells.

**Hypothesis:** the shell structure (2, 8, 18) may emerge from
the geometric packing of distributed-charge spheres around a
point nucleus, minimized for total energy, without requiring
the Pauli exclusion principle as a separate axiom.  The
exclusion principle would then be a CONSEQUENCE of geometry:
only so many extended electrons fit in each shell before it's
energetically cheaper to start a new one.


## The electron's spatial size

At ε = 397, the electron torus is almost spherical.  Two
candidate radii for the effective charge sphere:

| Model | R_eff | Diameter | Source |
|-------|-------|----------|--------|
| A | 751 fm (0.75 pm) | 1.50 pm | L_tube / 2π (model-E) |
| B | 386 fm (0.39 pm) | 0.77 pm | ℏ / m_e c (reduced Compton) |

Both will be tested.  They differ by ~2× because L_tube ≈ 2λ_C.
The shell-closing numbers (2, 8, 18) are expected to be robust
to this choice; the exact energy minima may differ.


## Approach: shell-by-shell energy minimization

Rather than throwing N electrons at a nucleus and hoping shells
emerge, we build up shell by shell and test whether energy
minima occur at the observed electron counts.

### Shell 1: the polar pair

Place N electrons around a +Ze nucleus with Z large enough to
bind them.  Model each electron as a spherical shell of charge
−e at radius R_eff.

- N = 1: one electron at distance r from nucleus.  Trivial.
- N = 2: two electrons settle on opposite sides (north/south
  poles).  This is the lowest-energy configuration for any
  repulsive pair around an attractor.
- N = 3, 4: test whether adding a third/fourth electron to the
  polar region costs more energy than starting a new shell.

**Expected minimum: N = 2** (helium configuration).  The "groove"
between the two polar electrons is the equatorial plane.

### Shell 2: the equatorial ring

Fix 2 electrons on the poles (shell 1 full).  Place additional
electrons in the equatorial ring.  The ring radius adjusts
to balance nuclear attraction against polar + mutual repulsion.

- Vary N_ring = 2, 4, 6, 8, 10, 12
- At each N_ring, minimize total energy over: ring radius,
  angular positions around the ring
- Look for an energy minimum per additional electron

**Expected minimum: N_ring = 8** (neon = 2 + 8 = 10).  The
equatorial ring at ~8 electrons should be energetically stable
because adding a 9th is more expensive than starting shell 3.

### Shell 3: the groove rings

Fix 2 polar + 8 equatorial.  The resulting geometry creates
two groove rings at roughly ±45° latitude (between the polar
caps and the equatorial belt).

- Place N electrons in each groove ring (symmetric above/below)
- Vary N_groove = 2, 3, 4, 5, 6 per ring (total = 2 × N_groove)
- Minimize total energy

**Expected minimum: N_groove = 4 per ring → 8 total**
(argon = 2 + 8 + 8 = 18).

Note: the standard shell 3 holds 18 electrons (2 + 6 + 10 in
s + p + d orbitals), but chemical shell closing occurs at 8
(the noble gas configuration).  The geometric packing model
should reproduce the CHEMICAL shell closing (8, not 18) if it's
driven by spatial packing rather than angular momentum degeneracy.


## Computational model

Each electron is a uniform spherical shell of charge −e at
radius R_eff, centered at position **r_i** in 3D space.
The nucleus is a point charge +Ze at the origin.

### Energy terms

**Electron-nucleus attraction:**
For a shell of charge at distance d from a point charge,
the interaction is the same as point-point if d > R_eff
(shell theorem), and modified if d < R_eff (electron
"encloses" the nucleus).

**Electron-electron repulsion:**
For two spherical shells at separation d:
- d > 2R_eff: same as point-point (shell theorem)
- d < 2R_eff: shells overlap; the repulsion is SOFTER than
  point-point.  Computed by integrating the Coulomb kernel
  over both shells.

The soft repulsion at overlap is what makes this different
from the point-charge Thomson problem.  It's the MaSt
contribution: the electron has physical extent.

### Optimization

At each shell configuration:
1. Parameterize electron positions (radii + angles)
2. Compute E_total analytically or by numerical integration
3. Minimize over all free parameters
4. Record equilibrium energy per electron

### Deliverables

- Energy per electron vs N for each shell
- Equilibrium configurations (coordinates) at each N
- Clear identification of energy minima (shell closures)
- Comparison: do minima occur at 2, 8, 8 (matching noble gases)?
- Sensitivity to R_eff (model A vs B)
- Visualization: top and side views of each configuration


## What success looks like

**Strong success:** energy minima at exactly N = 2 (shell 1),
8 (shell 2), 8 (shell 3 chemical), reproducing He, Ne, Ar
configurations from pure geometry + energy minimization.

**Moderate success:** minima at approximately the right numbers
(e.g., 2, 6–10, 6–10) showing that shell structure EMERGES
from packing but doesn't exactly reproduce QM.

**Failure:** no clear minima, or minima at wrong numbers.  This
would mean shell structure is NOT a packing phenomenon and
genuinely requires the Pauli principle as an independent axiom.

Any of these outcomes is informative.
