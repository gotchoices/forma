# Q84: MaSt — terminology and naming conventions

**Status:** Draft — terminology proposal (v2)
**Related:**
  [Q27](Q27-foundational-axioms.md) (foundational axioms),
  [Q32](Q32-energy-geometry-fundamentals.md) (energy and geometry),
  [matter-from-light](../papers/matter-from-light.md) (matter as standing waves)

---

## 1. The problem

The framework uses "T⁶" for the six compact dimensions
(from "torus").  But "T" also means "time" in every other
branch of physics.  Superscripted dimension counts (T⁶, T²,
S³) collide with standard mathematical notation (3-sphere,
mass-squared).

More broadly, we lack a consistent naming scheme that
conveys what the dimensions *are*, not just their topology.

---

## 2. MaSt — the naming convention

Einstein fused space and time into spacetime.  This
framework adds a lower layer: the six compact dimensions
where matter IS — particles are standing waves on these
dimensions.  Energy flows through the full
Material-Space-time continuum.

**MaSt** = **Ma**terial – **S**pace – **t**ime.

The lowercase t follows the physics convention (time is
always *t* in equations) and signals that time is the
familiar dimension — the new ingredient is Ma.

The framework may be referred to as "the MaSt model" or
"the MaSt Universe" in external communication.

---

## 3. Notation

### 3.1 Core symbols

| Symbol | Name | Dimensions | Description |
|--------|------|:----------:|-------------|
| Ma | Material space | 6 | The compact dimensions; decomposes into 3Ma |
| 3Ma | Three sheets | 3 × 2 | The three-sheet decomposition of Ma |
| Ma_e | Electron sheet | 2 | Periodic plane for electron-family modes |
| Ma_ν | Neutrino sheet | 2 | Periodic plane for neutrino modes |
| Ma_p | Proton sheet | 2 | Periodic plane for proton/hadron modes |
| S | Space | 3 | The three large spatial dimensions |
| t | Time | 1 | Time |

The full arena: **Ma × S × t** (6 + 3 + 1 = 10 dimensions).

Ordinary spacetime is S × t — the familiar four-dimensional
block.  Ma is the new part: six material dimensions at every
point of S × t.

### 3.2 Design principles

**No superscript dimension counts.**  Each symbol refers to
a structure of fixed, known dimensionality.  Ma is *always*
six-dimensional; Ma_e is *always* two-dimensional; S is
*always* three-dimensional.  When the count matters, spell
it out in prose: "Ma is the six-dimensional material space."

This avoids collisions with exponents (M², S³) and standard
mathematical objects (S³ = 3-sphere, T¹ = circle).

**Subscript = label.**  Always a letter or particle symbol
identifying a specific sheet.

**Leading numeral = structural count.**  3Ma means "three
material sheets" (not "three dimensions").  The arithmetic:
3Ma = Ma_e × Ma_ν × Ma_p = six material dimensions = Ma.

### 3.3 ASCII and code conventions

Greek letters are not available on all keyboards.  In code,
filenames, and ASCII-only contexts, spell out Greek:

| Rich text | Code / ASCII | Avoid |
|-----------|-------------|-------|
| Ma_ν | Ma_nu, ma_nu | Ma_v (v = velocity) |
| σ_ep | sigma_ep | |
| φ_e | phi_e | (same pattern: phi_nu, phi_p, theta_nu, theta_p) |
| θ_e | theta_e | |
| ψ | psi | θ (conflicts with tube axis) |

Standard file and identifier names:

| Old | New |
|-----|-----|
| t6.py | ma.py |
| t6_solver.py | ma_solver.py |
| T6Solver | MaSolver |
| alpha_kk | alpha_ma |

---

## 4. The three material sheets

Ma decomposes into three sheets (3Ma):

| Symbol | Name | Circumference | Mode energy | Particle family |
|--------|------|--------------|-------------|-----------------|
| Ma_ν | Neutrino sheet | ~42–200 μm | ~meV (THz) | Neutrinos |
| Ma_e | Electron sheet | ~pm | ~MeV | Electron, muon, tau |
| Ma_p | Proton sheet | ~fm | ~GeV | Proton, hadrons |

### 4.1 Within-sheet axes

Each sheet has two periodic axes — a ring (the major circle) and a tube (the minor
circle).  Following standard torus convention, φ (phi) names the toroidal/ring angle
and θ (theta) names the poloidal/tube angle.  The sheet subscript identifies which
sheet:

| Sheet | Ring axis (φ) | Tube axis (θ) |
|-------|--------------|--------------|
| Ma_e | φ_e | θ_e |
| Ma_ν | φ_ν | θ_ν |
| Ma_p | φ_p | θ_p |

The two axes are geometrically distinct: the ring circumference L_φ is always larger
than the tube circumference L_θ, and their ratio defines the aspect ratio r = L_φ/L_θ.

---

## 5. Geometric parameters

These are the numbers that define the shape, size, and
relationships of the material dimensions.

### 5.1 Per-sheet parameters

| Parameter | Symbol(s) | What it controls | Example |
|-----------|-----------|-----------------|---------|
| **Circumferences** | L_φe, L_θe, L_φν, L_θν, L_φp, L_θp | Physical size of each compact direction; sets the energy scale | L_θe → electron mass |
| **Aspect ratio** | r_e, r_ν, r_p | Ratio of ring to tube circumference per sheet (r = L_φ/L_θ) | r_p = 8.906 → proton mass |
| **Within-plane shear** | s_e, s_ν, s_p | Skew between the two axes on one sheet; deforms the sheet from rectangle to parallelogram | s_e ≈ 0.010 → α = 1/137 |
| **Compact energy scale** | E₀ | ℏc/L for each sheet — the fundamental mode energy | E₀(ν) ~ meV, E₀(e) ~ MeV |

### 5.2 Inter-sheet parameters

| Parameter | Symbol(s) | What it controls | Example |
|-----------|-----------|-----------------|---------|
| **Cross-shear** | σ_ep, σ_eν, σ_νp | Coupling between axes on *different* sheets; off-diagonal entries in the Ma metric | σ_ep ≈ −0.091 → neutron mass |

Cross-shears determine which modes can have quantum numbers
on more than one sheet simultaneously (cross-plane modes).
The full cross-shear between two sheets has four components
(e.g., σ_φeφp, σ_φeθp, σ_θeφp, σ_θeθp for the electron-proton pair).

### 5.3 Embedding parameters

| Parameter | Symbol | What it controls | Example |
|-----------|--------|-----------------|---------|
| **S–Ma tilt** | ψ | Orientation of a material sheet relative to S; determines how much S "sees" of compact modes | ψ → background gauge potential |

The tilt does NOT deform the sheet (masses unchanged).
It rotates the sheet's orientation in the full 10D space.
A uniform tilt produces no force (equivalent to a constant
Wilson line with zero field strength).

ψ (psi) is used rather than θ to avoid collision with the tube-axis angle θ.

### 5.4 The full metric

The 6×6 compact metric G̃ᵢⱼ (dimensionless, rescaled by
circumferences) encodes all per-sheet and inter-sheet
parameters.  It is block-diagonal in the absence of
cross-shears and develops off-diagonal blocks when
σ ≠ 0.

Parameter census (R26): 21 metric entries total, 15 free
after symmetry constraints.

---

## 6. Modes and quantum numbers

A **mode** is a standing wave on Ma, specified by six
integers — the winding numbers around each compact axis.
Tuple ordering: (n_φe, n_θe, n_φν, n_θν, n_φp, n_θp).

| Term | Definition |
|------|-----------|
| **Winding number** | Integer count of wave cycles around a compact axis (nᵢ) |
| **Tube winding** | Winding around the smaller circumference of a sheet |
| **Ring winding** | Winding around the larger circumference |
| **Fundamental mode** | Coprime winding pair — e.g. (1,2) is fundamental; (2,4) is a harmonic of (1,2) |
| **Harmonic** | Non-coprime winding pair: d × (p,q) where d > 1; same spin class, d× energy |
| **Single-sheet mode** | Nonzero windings on only one sheet; zero on others |
| **Cross-plane mode** | Nonzero windings on more than one sheet; exists only when cross-shear σ ≠ 0 |

### 6.1 Mode properties

| Property | How determined | Key formula |
|----------|--------------|-------------|
| **Mass** | Eigenvalue of Ma wave equation | m² = E₀² μ², where μ = √((n_φ/r)² + (n_θ − n_φ·s)²) per sheet, plus cross-shear corrections |
| **Charge** | Shear-dependent integral over mode wavefunction on deformed sheet | Q = −n_φe + n_φp (charge rule on Ma; ring windings) |
| **Spin** | Tube winding number | s = ½ for odd n_θ (fermion); s = 0 or 1 for even n_θ (boson) |

### 6.2 Charge-spin linkage

On a single sheet, charge and spin are both controlled by
the tube winding number n_θ.  "Uncharged fermion" is impossible
on one sheet.  The neutrino requires a cross-plane mode
or a second sheet — this drove the move from one sheet to
3Ma (R25).

---

## 7. Key mechanisms

| Mechanism | Description | Reference |
|-----------|-------------|-----------|
| **Shear-induced charge** | Within-plane shear s ≠ 0 breaks φ-symmetry of mode wavefunctions; the net asymmetry is electric charge; α = f(r, s) | R19 |
| **Cross-shear coupling** | Inter-sheet shear σ ≠ 0 allows modes to span multiple sheets; determines neutron mass splitting, PMNS-like mixing | R26 |
| **KK gauge field** | Off-diagonal metric between Ma and S dimensions; fluctuations in S propagate as electromagnetic field; emerges from the wave equation, not imposed | R36 F9 |
| **Wilson line** | A constant (non-varying) gauge potential on a sheet; shifts momenta uniformly, produces no force (F = 0); equivalent to a uniform S–Ma tilt | R36 F3 |
| **Ghost mode suppression** | Most Ma modes are unobserved; ~10⁵ coupling suppression required; mechanism under investigation | R32, R33 |
| **Off-resonance hypothesis** | Unstable particles are excitations not exactly on eigenmodes; gap to nearest mode correlates with lifetime | R27 |
| **Predictive horizon** | Above ~2 GeV, Ma mode spectrum is so dense that hits cease to be discriminating | R28 |

---

## 8. Named structural objects

| Name | What it is | MaSt notation |
|------|-----------|---------------|
| **Electron** | (1,2) mode on Ma_e | Mode (1,2,0,0,0,0) |
| **Proton** | (0,0,0,0,1,2) mode on Ma_p | Single-sheet proton mode |
| **Neutron** | Cross-plane mode spanning Ma_e × Ma_p | e.g. (1,2,0,0,1,2) with Q = −1+1 = 0 |
| **Neutrino mass eigenstates** | Three modes on Ma_ν with Δm² ratio ~33.6 | Assignment A or B (R26) |
| **Nucleus** | Ma_p mode with winding numbers scaling as mass number A | n_φp = A, n_θp = 2A (R29 scaling law) |

---

## 9. Migration: old notation → MaSt

| Old | MaSt | Improvement |
|-----|------|-------------|
| T⁶ | Ma | No collision with time; no superscript |
| T² | "a material sheet" or Ma_e etc. | No collision with mass-squared |
| T²_ν | Ma_ν | Reads as "neutrino material sheet" |
| "the three T² sheets" | 3Ma | Compact; arithmetic is transparent (3Ma = Ma) |
| R³ | S | "Space" — no superscript, no 3-sphere collision |
| R³ × T⁶ | Ma × S × t | Named from MaSt; parses as "material, space, time" |
| "compact dimensions" | "material dimensions" | States the thesis |
| "the neutrino T²" | Ma_ν or "the neutrino sheet" | Shorter, clearer |
| "cross-shear" | (unchanged) | Already clear |
| "within-plane shear" | (unchanged) | Already clear |
| alpha_kk | alpha_ma | Consistent with Ma notation |

---

## 10. The MaSt name

**MaSt** = **Ma**terial-**S**pace-**t**ime.

- Pronounceable, memorable
- States the three ingredients: Material, Space, time
- Claims "material" is on equal footing with space and
  time — not derivative, not emergent, but a fundamental
  geometric ingredient
- The lowercase t signals "time is the familiar part;
  Material is the new idea"
- Builds on Einstein's spacetime by adding a foundational
  layer: energy flows through the Ma-S-t continuum
- The notation derives directly from the name:
  Ma, S, t — no unexplained letters

---

## 11. Resolved questions

*(From v1 draft — resolved in v2.)*

1. **Migration scope.**  Adopting MaSt requires updating
   all existing files.  Tracked in ticket 3.

2. **"Material" vs. "Matter."**  "Material" chosen because
   it functions as an adjective ("material dimensions").
   Confirmed.

3. **Symbol for the 9D spatial manifold.**  Not needed.
   Say "Ma × S" when required.

4. **T¹ for time?**  Dropped.  Use lowercase t (standard).
   No dedicated symbol needed.

5. **Superscript dimension counts.**  Dropped.  Each symbol
   has a fixed dimensionality; spell out counts in prose
   when needed.

6. **S³ collision with 3-sphere.**  Resolved by dropping
   superscripts.  S (no superscript) is unambiguous.

7. **M² collision with mass-squared.**  Resolved by using
   Ma (two letters) instead of M.  Ma_e, Ma_ν, Ma_p for
   specific sheets.

8. **Keyboard access to ν.**  Use `nu` in code and ASCII
   contexts (Ma_nu).  Avoid `v` (velocity collision).
