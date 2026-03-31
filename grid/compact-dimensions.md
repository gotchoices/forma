# Compact Dimensions from GRID Lattices

**Status:** Complete — computational study finished.
Conclusion: α is a designer's choice within discrete lattice
steps; geometry does not uniquely determine it.

How do MaSt's compact material dimensions arise from the GRID
lattice?  This document proposes that the material sheets are
**2D simplicial sub-lattices** (triangular grids) embedded in
the 4D spacetime lattice, and investigates whether wrapping
them into tori with a shear constrains α.

---

## The dimensional hierarchy

The D-simplex is the minimal cell in D dimensions.  In each
case, it has D+1 vertices and D+1 faces, giving D+1 neighbors
(one per face).  Using the self + neighbors counting:

| Dimension | Simplex | Neighbors | Self + neighbors | ζ = 1/(z+1) |
|-----------|---------|-----------|-----------------|-------------|
| 1 | Line segment | 2 | 3 | 1/3 |
| 2 | Triangle | 3 | 4 | **1/4** |
| 3 | Tetrahedron | 4 | 5 | 1/5 |
| 4 | Pentachoron | 5 | 6 | 1/6 |

The 2D case gives ζ = 1/4 — the Bekenstein-Hawking value.

### A multi-scale lattice

MaSt's full arena is Ma × S × t (6+3+1 = 10 dimensions).
Perhaps different dimensions use different lattice structures:

| Component | Dimensions | Lattice type | Role |
|-----------|-----------|-------------|------|
| t (time) | 1 | 1D chain (segments) | Causal ordering; one tick per Planck time |
| S (space) | 3 | 3D simplicial (tetrahedra) | The three large spatial dimensions |
| Ma (material) | 6 = 3×2 | Three 2D simplicial sheets (triangles) | Compact dimensions where particles live |

Each material sheet (Ma_e, Ma_ν, Ma_p) is a 2D triangular
lattice — a sheet of equilateral triangles with edge length
equal to the Planck length L.  This is the simplest possible
2D packing.

**Key observation:** the 2D sheet has ζ = 1/4.  If the
entropy bound is set by the dimensionality of the material
sheets (where information is stored), rather than the full
4D spacetime, then ζ = 1/4 follows from **the material sheets
being 2D simplicial lattices**.

This would reconcile the Bekenstein-Hawking value (1/4) with
the 4D simplicial lattice value (1/6): the BH entropy counts
bits on the 2D horizon cross-section, which is a triangular
lattice.

---

## Wrapping a triangular sheet

A flat triangular lattice is described by two basis vectors:

<!-- a₁ = a(1, 0),  a₂ = a(1/2, √3/2) -->
$$
\mathbf{a}_1 = a\,(1,\, 0), \qquad
\mathbf{a}_2 = a\,\bigl(\tfrac{1}{2},\, \tfrac{\sqrt{3}}{2}\bigr)
$$

where a = L = 1 (Planck length).  The angle between basis
vectors is 60°.  Every vertex has 6 nearest neighbors.  Every
triangular cell has 3 edge-sharing neighbors.

### Making a cylinder

To wrap the sheet into a cylinder, identify each point **r**
with **r** + **C**, where the **chiral vector** is:

<!-- C = n a₁ + m a₂ -->
$$
\mathbf{C} = n\,\mathbf{a}_1 + m\,\mathbf{a}_2
$$

for integers (n, m).  This is exactly the construction used
for **carbon nanotubes** (Iijima 1991, Dresselhaus 1995).

The integers (n, m) completely determine the cylinder:

**Circumference:**

<!-- |C| = a √(n² + nm + m²) -->
$$
|\mathbf{C}| = a\,\sqrt{n^2 + nm + m^2}
$$

**Radius:**

<!-- R = |C| / (2π) = a √(n² + nm + m²) / (2π) -->
$$
R = \frac{|\mathbf{C}|}{2\pi}
= \frac{a\,\sqrt{n^2 + nm + m^2}}{2\pi}
$$

**Chiral angle** (shear angle relative to the zigzag
direction):

<!-- θ = arctan(√3 m / (2n + m)) -->
$$
\theta = \arctan\!\left(\frac{\sqrt{3}\,m}{2n + m}\right)
$$

The chiral angle ranges from 0° (zigzag, m = 0) to 30°
(armchair, n = m).

### Special cases

| Type | Condition | Chiral angle | Shear |
|------|-----------|-------------|-------|
| Zigzag | m = 0 | 0° | None |
| Armchair | n = m | 30° | Maximum |
| Chiral | 0 < m < n | 0° < θ < 30° | Intermediate |

### Making a torus

MaSt's material sheets are periodic in both directions — they
are tori, not open cylinders.  A torus requires **two**
wrapping vectors:

<!-- C₁ = n₁ a₁ + m₁ a₂  (first circumference) -->
<!-- C₂ = n₂ a₁ + m₂ a₂  (second circumference) -->
$$
\mathbf{C}_1 = n_1\,\mathbf{a}_1 + m_1\,\mathbf{a}_2
\qquad\text{and}\qquad
\mathbf{C}_2 = n_2\,\mathbf{a}_1 + m_2\,\mathbf{a}_2
$$

with four integers (n₁, m₁, n₂, m₂).  The constraint is that
**C₁** and **C₂** must be linearly independent (they span
different directions on the sheet).

This gives:
- Two radii R₁, R₂ (the "aspect ratio" r = R₁/R₂ in MaSt)
- A relative angle between the two wrapping directions
  (the "shear" s in MaSt)

All edges remain Planck length.  The geometry is exact —
no stretching, no approximation.

---

## The shear-alpha connection

In MaSt, the shear parameter s of the electron sheet is
directly related to the fine-structure constant α through
the charge mechanism (R15, R19).  The formula α(r, s) gives
a one-parameter family: every aspect ratio r has a
self-consistent shear s.

If the sheet is a triangular lattice wrapped into a torus,
then the shear is **not a continuous parameter** — it is
determined by the four integers (n₁, m₁, n₂, m₂).  This
discretizes the space of allowed geometries.

**The question:** among all valid (n₁, m₁, n₂, m₂) wrappings,
does any combination give a shear s such that α(r, s) ≈ 1/137?

If yes: α is determined by the lattice wrapping — a discrete
geometric quantity.  There might be a unique solution, a small
finite set, or a dense spectrum.

If no: the triangular lattice wrapping does not explain α,
and some other mechanism is needed.

### What makes this computable

The problem reduces to:

1. **Enumerate** integer quadruplets (n₁, m₁, n₂, m₂) up to
   some reasonable size (the electron sheet is ~pm scale,
   so R ~ 10²² Planck lengths — large integers).

2. **For each**, compute:
   - Aspect ratio r = R₁/R₂
   - Shear angle θ (from the relative orientation of C₁, C₂)
   - Map θ to MaSt's shear parameter s

3. **Apply** the α(r, s) formula from MaSt studies (R15, R19)
   to check whether α ≈ 1/137 for any wrapping.

4. **Check** whether solutions are unique, sparse, or dense.

The main subtlety: the mapping between the lattice shear angle
θ and MaSt's shear parameter s needs to be established
carefully.  They should be the same geometric quantity viewed
from different descriptions.

---

## Are all sheets periodic?

Yes — periodicity is essential.  A material sheet that is not
periodic has boundaries.  Boundaries would mean:

- Particles (standing waves on the sheet) would reflect or
  leak at the edges
- The mode spectrum would depend on boundary conditions, not
  just topology
- There would be preferred locations (near/far from edges)

Periodicity (torus topology) eliminates all of these.  It
also ensures that every cell is equivalent — there are no
special cells, no edges, no corners.  This is the lattice
analog of translational symmetry.

The periodicity of the triangular lattice on a torus is
guaranteed by the integer wrapping vectors (n₁, m₁, n₂, m₂):
the lattice tiles the torus exactly, with no leftover cells
or mismatched edges.

---

## Different sheets, different wrappings

MaSt has three material sheets at vastly different scales:

| Sheet | Size | Wrapping integers | Approx. cells around |
|-------|------|-------------------|---------------------|
| Ma_p (proton) | ~1 fm = 10¹⁹ L | ~10¹⁹ | ~10¹⁹ |
| Ma_e (electron) | ~1 pm = 10²² L | ~10²² | ~10²² |
| Ma_ν (neutrino) | ~1 μm = 10²⁹ L | ~10²⁹ | ~10²⁹ |

The wrapping integers are enormous.  But the shear angle
(which determines α) depends on the *ratio* m/n, not the
absolute size.  So the physically interesting quantity — the
chiral angle — is determined by a ratio of large integers,
which can approximate any real number to arbitrary precision.

This means:  for very large sheets, the discreteness of the
wrapping is extremely fine-grained.  There WILL be wrappings
near any target shear angle, including the one that gives
α ≈ 1/137.

The real question is not "does a solution exist?" (it does,
for large enough integers) but rather:
- **Is there a selection principle** that picks one wrapping
  over others?
- **Does the lowest-energy or simplest wrapping** happen to
  give α ≈ 1/137?
- **Is there a topological constraint** (e.g., the wrapping
  must be compatible with the three-sheet architecture)?

---

## What this would explain

If the material sheets are triangular lattices wrapped into
tori, and the wrapping determines α:

1. **ζ = 1/4** follows from the 2D triangular packing (not
   assumed — derived from the sheet geometry)
2. **α ≈ 1/137** follows from the specific wrapping of Ma_e
   (possibly selected by energy minimization or topological
   constraint)
3. **Both free parameters of GRID** (ζ and α) become geometric
   consequences — zero free parameters remain
4. The **nanotube-like** discrete spectrum of allowed shears
   might explain why α has the specific value it does

---

## Computational results

Scripts in [`scripts/`](scripts/) enumerate triangular lattice
torus wrappings and evaluate α_ma(r, s) from the MaSt charge
formula (R19 Track 8, `studies/lib/ma.py`).

### Mapping from lattice to MaSt conventions

Given wrapping vectors C₁ = n₁a₁ + m₁a₂ (tube) and
C₂ = n₂a₁ + m₂a₂ (ring), the MaSt parameters are:

- **Shear:** s = (C₁·C₂) / |C₁|²
- **Aspect ratio:** r = |C₁| / |C₂_⊥| where C₂_⊥ is the
  component of C₂ perpendicular to C₁
- **Torus size:** |det(C₁, C₂)| cells in the fundamental domain
  (1 cell = 2 triangles = ½ bit at ζ = 1/4)

### Key findings

**1. Matches exist at all four α landmarks.**

With wrapping integers |n|, |m| ≤ 25, the simplest torus
(fewest cells) matching each α target to within 0.5%:

| Target | Wrapping | Cells | r | s | 1/α | Error |
|--------|----------|------:|------|------|-----:|------:|
| 1/137 | (−2,−1)×(+25,+14) | 3 | 2.69 | −12.9 | 137.2 | −0.14% |
| 1/128 | (−2,−1)×(+23,+13) | 3 | 2.69 | −11.9 | 128.0 | −0.03% |
| 1/80 | (−2,−2)×(+18,+23) | 10 | 1.39 | −10.3 | 80.0 | −0.05% |
| 1/24 | (−4,+1)×(−23,+4) | 7 | 2.14 | +5.9 | 24.0 | +0.13% |

The 1/137 and 1/128 matches share the SAME tube direction
(−2,−1) and differ only in the ring vector.  This is
suggestive — they are "the same geometry" at two scales.

**2. The solution space is dense — α is a designer's choice.**

With 714,317 unique geometries at max-n = 25, matches within
0.5% of any target are abundant (~700–1200 per target).  No
single wrapping is singled out by rarity alone.

**3. The spectrum is discrete but fine-grained.**

The 3-cell torus has a remarkably regular spectrum: in the
range 1/α ∈ [100, 180], there are 18 distinct values, all
sharing the same aspect ratio r ≈ 2.694.  They form pairs
separated by a gap of ~1.31, with pair-to-pair spacing of
~9.2.  The nearest neighbor to 1/α = 137.036 is 137.23
(0.14% error); the next value beyond that is 138.55.

For larger tori the spectrum fills in rapidly:

| Cells | Triangles | Bits (ζ=¼) | Values in [120,150] | Median gap | Closest to 137.036 | Error |
|------:|----------:|----------:|-----------:|----------:|-------------------:|------:|
| 3 | 6 | 1.5 | 7 | 7.88 | 137.232 | 0.14% |
| 9 | 18 | 4.5 | 14 | 1.94 | 136.996 | 0.030% |
| 24 | 48 | 12 | 21 | 0.62 | 137.043 | 0.005% |
| 36 | 72 | 18 | 48 | 0.41 | 136.996 | 0.030% |
| 48 | 96 | 24 | 49 | 0.31 | 137.307 | 0.20% |
| 60 | 120 | 30 | 49 | 0.47 | 137.016 | 0.015% |

The median gap in the [120, 150] window scales roughly as
1/N (where N is the number of unit cells).  By 60 cells
the gap is ~0.5, and sub-0.01% precision is available.

**4. First appearance of landmarks vs torus size.**

How small can the torus be and still reach each coupling
value?

| Landmark | < 10% | < 1% | < 0.1% | < 0.01% |
|----------|------:|-----:|-------:|--------:|
| 1/24 (GUT) | 2 cells | 2 cells | 5 cells | 35 cells |
| 1/80 (high-E) | 3 cells | 5 cells | 7 cells | 55 cells |
| 1/128 (Z mass) | 3 cells | 3 cells | 3 cells | — |
| 1/137 (low-E) | 3 cells | 3 cells | 9 cells | 24 cells |

Weak coupling (1/α > 100) does not appear until 3 cells
(6 triangles, ~1.5 bits).  This is the minimum complexity
threshold — below it, only strong coupling is available.

**5. No magic shear values.**

The shear values producing each target form a dense, irregular
set without clear periodic spacing.  There is no "magic
sequence" of equally-spaced shears mapping to known α values.

**6. Running coupling may be encoded in ring length.**

The 1/137 and 1/128 matches both use tube vector (−2,−1) and
differ only in the ring vector — effectively the same tube
probed at different ring circumferences.  This is consistent
with the running of α being a change in the effective geometry
at different energy scales, not a change in the underlying
lattice structure.

---

## Assessment

### What the lattice achieves

The triangular-lattice torus construction succeeds in providing
a concrete geometric mechanism that:

1. **Discretizes α.** The coupling constant becomes a function
   of four integers (n₁, m₁, n₂, m₂), not a continuous
   parameter.
2. **Connects to MaSt.** The lattice wrapping maps cleanly
   onto MaSt's shear and aspect ratio parameters.
3. **Provides ζ = 1/4.** The 2D triangular lattice (self +
   3 neighbors = 4) naturally yields the Bekenstein-Hawking
   entropy factor.
4. **Accommodates all known α landmarks.** Low-energy (1/137),
   Z-mass (1/128), high-energy (1/80), and GUT-scale (1/24)
   all appear in the lattice spectrum.
5. **Imposes a minimum complexity threshold.** Weak coupling
   requires at least 3 unit cells (6 triangles, ~1.5 bits),
   suggesting a fundamental information requirement for EM.

### What the lattice does not achieve

The lattice does **not** uniquely determine α.  For any
reasonably sized torus, the allowed α values are dense enough
that virtually any coupling constant can be approximated.

This is an honest result:  **α is a designer's choice within
the available discrete steps.**  The lattice provides the
menu; something else picks the dish.

Possible selection principles (all speculative, none tested):

- **Energy minimization** — the wrapping that minimizes total
  energy for a given torus size
- **Topological constraint** — compatibility with the three-
  sheet architecture (Ma_e × Ma_ν × Ma_p)
- **Simplicity** — fewest cells in the fundamental domain
  (the 3-cell torus at 1/137 is the simplest weak-coupling
  option available)
- **Stability** — the wrapping must support stable standing-
  wave modes
- **Anthropic** — α ≈ 1/137 permits atoms, chemistry, and
  observers; other values may not

Whether any of these selects the observed value is a separate
investigation.

### What is interesting despite this

1. **The 3-cell torus** (6 triangles, 1.5 bits) is the
   smallest torus that supports weak coupling at all.  The
   fact that 1/α ≈ 137 appears at the minimum complexity
   threshold — rather than requiring a much larger lattice —
   is notable.  It is not a prediction of 137, but it is a
   structural coincidence worth flagging.

2. **The regular spacing** of the 3-cell spectrum (pairs
   separated by ~1.31, pair groups by ~9.2) comes from the
   fixed aspect ratio r ≈ 2.694 and the sin²(2πs) factor in
   α_ma.  The spacing is governed by the geometry of the tube,
   not an arbitrary parameter.

3. **Running coupling via ring length** — the shared tube
   direction for 1/137 and 1/128 suggests a physical picture
   where the energy scale corresponds to the resolution at
   which the ring circumference is probed.

---

## Open questions

1. **Is there a selection principle** for the wrapping?
   Energy minimization?  Topological constraint from the
   three-sheet architecture?  Stability?

2. **Can the different sheets have different lattice types?**
   All three are proposed as 2D triangular, but could Ma_p
   differ from Ma_e?

3. **How do the sheets embed in the 4D spacetime lattice?**
   The 2D sheets must fit consistently within the larger
   4D structure.  Does this constrain the wrapping?

4. **What sets the SIZE of each sheet?**  The wrapping
   integers determine R₁ and R₂ (hence the particle mass
   scale).  What selects the enormous integers ~10¹⁹ to 10²⁹?

5. **Does ζ = 1/4 follow rigorously** from the 2D sheet
   interpretation (2D simplex, self + 3 neighbors = 4)?

---

## Scripts

| Script | Purpose |
|--------|---------|
| [`triangular_wrapping.py`](scripts/triangular_wrapping.py) | Broad enumeration of wrappings, match search |
| [`magic_shears.py`](scripts/magic_shears.py) | Focused study of special shear values |
| [`simplest_alpha.py`](scripts/simplest_alpha.py) | Minimal-cell wrappings for each α landmark |
| [`small_tori.py`](scripts/small_tori.py) | Complete α spectrum for very small tori |
| [`alpha_density.py`](scripts/alpha_density.py) | Solution density and gap scaling analysis |

---

## Next steps

- [x] Establish the mapping between lattice geometry and MaSt
      shear parameter s
- [x] Write computational scripts to enumerate wrappings
      and evaluate α(r, s)
- [x] Study solution density and gap scaling vs torus size
- [ ] Investigate whether energy minimization selects the
      right wrapping (requires dynamics — future work)
- [ ] Investigate whether ζ = 1/4 follows rigorously from
      the 2D sheet interpretation
