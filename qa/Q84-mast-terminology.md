# Q84: MaST Universe — terminology and naming conventions

**Status:** Draft — terminology proposal
**Related:**
  [Q27](Q27-foundational-axioms.md) (foundational axioms),
  [Q32](Q32-energy-geometry-fundamentals.md) (energy and geometry),
  [matter-from-light](../papers/matter-from-light.md) (matter as standing waves)

---

## 1. The problem

The framework uses "T⁶" for the six compact dimensions
(from "torus").  But "T" also means "time" in every other
branch of physics.  The collision causes confusion,
especially for newcomers.

More broadly, we lack a consistent naming scheme that
conveys what the dimensions *are*, not just their
topology.

---

## 2. MaST Universe — the naming convention

**Ma** — Material dimensions (where matter lives)
**S**  — Space (the three large dimensions we navigate)
**T**  — Time
**U**  — Universe (the full 10D arena)

The compact dimensions are not abstract mathematical
structures.  They are the dimensions where matter IS —
particles are standing waves on these dimensions.  Calling
them "material dimensions" encodes the central thesis in
the vocabulary.

The familiar intuition: matter moves through spacetime.
MaST says: energy moves through Material-Space-Time.

The framework may be referred to as "the MaST Universe
model" in external communication.

---

## 3. Dimension inventory

| Symbol | Name | Count | Description |
|--------|------|-------|-------------|
| U¹⁰ | Universe | 10 | The full arena: M⁶ × S³ × T¹ |
| M⁶ | Material space | 6 | The compact dimensions; 3M (three M² sheets) |
| S³ | Space | 3 | The large spatial dimensions (x, y, z) |
| T¹ | Time | 1 | Time |

Decomposition: U¹⁰ = M⁶ × S³ × T¹ (9 spatial + 1 temporal).

Ordinary "spacetime" is S³ × T¹ — the familiar 4D block.
M⁶ is the new part: six material dimensions at every point.

### 3.1 Conventions

**Superscript = dimension count.**  Always.

| Symbol | Reads as |
|--------|----------|
| U¹⁰ | "the ten-dimensional universe" |
| M⁶ | "six material dimensions" |
| M² | "a two-dimensional material sheet" (generic) |
| M²_ν | "the neutrino material plane" |
| S³ | "three-dimensional space" |
| T¹ | "one-dimensional time" |

**Subscript = label.**  Always a letter or particle symbol
identifying a specific sheet or axis.

**Prefixed numeral = count of structural units.**  3M means
"three sheets," not "three dimensions."  The arithmetic:
3M = three M² sheets = M⁶ (3 sheets × 2 dimensions each).

| Symbol | Meaning |
|--------|---------|
| M⁶ | The six material dimensions (the space) |
| 3M | The three-sheet decomposition (the structure) |
| M² | One sheet (two dimensions) |
| M²_ν | The neutrino sheet specifically |

### 3.2 Convention clash: S³

In standard mathematics, S³ denotes the 3-sphere.  In MaST
notation, S³ means flat 3-space (ℝ³).  Within the project,
S³ always means flat space.

### 3.3 Convention clash: U vs U(1)

In gauge theory, U(1) denotes the unitary symmetry group of
electromagnetism.  In MaST, U¹⁰ denotes the full 10D
manifold.  The superscript and context disambiguate:
U(1) always has parentheses and refers to a symmetry group;
U¹⁰ has a superscript and refers to a space.

---

## 4. The three material sheets

M⁶ decomposes into three M² subplanes:

| Symbol | Name | Circumference | Mode energy | Particle family |
|--------|------|--------------|-------------|-----------------|
| M²_ν | Neutrino sheet | ~42–200 μm | ~meV (THz) | Neutrinos |
| M²_e | Electron sheet | ~pm | ~MeV | Electron, muon, tau |
| M²_p | Proton sheet | ~fm | ~GeV | Proton, hadrons |

### 4.1 Within-sheet axes

Each M² has two periodic axes (a ring and a tube):

| Sheet | Axis 1 | Axis 2 |
|-------|--------|--------|
| M²_ν | θ₃ | θ₄ |
| M²_e | θ₁ | θ₂ |
| M²_p | θ₅ | θ₆ |

When referencing a specific axis: M_ν₁ and M_ν₂ (the two
dimensions of the neutrino sheet), etc.

---

## 5. Geometric parameters

These are the numbers that define the shape, size, and
relationships of the material dimensions.

### 5.1 Per-sheet parameters

| Parameter | Symbol(s) | What it controls | Example |
|-----------|-----------|-----------------|---------|
| **Circumferences** | L₁…L₆ | Physical size of each compact direction; sets the energy scale | L₂ → electron mass |
| **Aspect ratio** | r_e, r_ν, r_p | Ratio of the two circumferences on each sheet (r = L₁/L₂) | r_p = 8.906 → proton mass |
| **Within-plane shear** | s_e, s_ν, s_p | Skew between the two axes on one sheet; deforms the M² from rectangle to parallelogram | s_e ≈ 0.010 → α = 1/137 |
| **Compact energy scale** | E₀ | ℏc/L for each sheet — the fundamental mode energy | E₀(ν) ~ meV, E₀(e) ~ MeV |

### 5.2 Inter-sheet parameters

| Parameter | Symbol(s) | What it controls | Example |
|-----------|-----------|-----------------|---------|
| **Cross-shear** | σ_ep, σ_eν, σ_νp | Coupling between axes on *different* sheets; off-diagonal entries in the M⁶ metric | σ_ep ≈ −0.091 → neutron mass |

Cross-shears determine which modes can have quantum numbers
on more than one sheet simultaneously (cross-plane modes).
The full cross-shear between two sheets has four components
(e.g., σ₁₅, σ₁₆, σ₂₅, σ₂₆ for the electron-proton pair).

### 5.3 Embedding parameters

| Parameter | Symbol | What it controls | Example |
|-----------|--------|-----------------|---------|
| **R-M tilt** | θ | Orientation of an M² plane relative to S³; determines how much S³ "sees" of compact modes | θ → background gauge potential |

The tilt does NOT deform the sheet (masses unchanged).
It rotates the sheet's orientation in the full 10D space.
A uniform tilt produces no force (equivalent to a constant
Wilson line with zero field strength).

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

A **mode** is a standing wave on M⁶, specified by six
integers (n₁, n₂, n₃, n₄, n₅, n₆) — the winding numbers
around each compact axis.

| Term | Definition |
|------|-----------|
| **Winding number** | Integer count of wave cycles around a compact axis (nᵢ) |
| **Tube winding** | Winding around the smaller circumference of an M² |
| **Ring winding** | Winding around the larger circumference |
| **Fundamental mode** | Coprime winding pair — e.g. (1,2) is fundamental; (2,4) is a harmonic of (1,2) |
| **Harmonic** | Non-coprime winding pair: d × (p,q) where d > 1; same spin class, d× energy |
| **Single-sheet mode** | Nonzero windings on only one M²; zero on others |
| **Cross-plane mode** | Nonzero windings on more than one M²; exists only when cross-shear σ ≠ 0 |

### 6.1 Mode properties

| Property | How determined | Key formula |
|----------|--------------|-------------|
| **Mass** | Eigenvalue of M⁶ wave equation | m² = E₀² μ², where μ = √((n₁/r)² + (n₂ − n₁s)²) per sheet, plus cross-shear corrections |
| **Charge** | Shear-dependent integral over mode wavefunction on deformed M² | Q = −n₁ + n₅ (charge rule on M⁶) |
| **Spin** | Tube winding number | s = ½ for odd tube winding (fermion); s = 0 or 1 for even (boson) |

### 6.2 Charge-spin linkage

On a single M², charge and spin are both controlled by
the tube winding number.  "Uncharged fermion" is impossible
on one sheet.  The neutrino requires a cross-plane mode
or a second sheet — this drove the move from T² to T⁶ (R25).

---

## 7. Key mechanisms

| Mechanism | Description | Reference |
|-----------|-------------|-----------|
| **Shear-induced charge** | Within-plane shear s ≠ 0 breaks φ-symmetry of mode wavefunctions; the net asymmetry is electric charge; α = f(r, s) | R19 |
| **Cross-shear coupling** | Inter-sheet shear σ ≠ 0 allows modes to span multiple sheets; determines neutron mass splitting, PMNS-like mixing | R26 |
| **KK gauge field** | Off-diagonal metric between M and S dimensions; fluctuations in S³ propagate as electromagnetic field; emerges from the wave equation, not imposed | R36 F9 |
| **Wilson line** | A constant (non-varying) gauge potential on M²; shifts momenta uniformly, produces no force (F = 0); equivalent to a uniform R-M tilt | R36 F3 |
| **Ghost mode suppression** | Most M⁶ modes are unobserved; ~10⁵ coupling suppression required; mechanism under investigation | R32, R33 |
| **Off-resonance hypothesis** | Unstable particles are excitations not exactly on eigenmodes; gap to nearest mode correlates with lifetime | R27 |
| **Predictive horizon** | Above ~2 GeV, M⁶ mode spectrum is so dense that hits cease to be discriminating | R28 |

---

## 8. Named structural objects

| Name | What it is | MaST notation |
|------|-----------|---------------|
| **Electron** | (1,2) mode on M²_e | Mode (1,2,0,0,0,0) |
| **Proton** | (0,0,0,0,1,2) mode on M²_p | Single-sheet proton mode |
| **Neutron** | Cross-plane mode spanning M²_e × M²_p | e.g. (1,2,0,0,1,2) with Q = −1+1 = 0 |
| **Neutrino mass eigenstates** | Three modes on M²_ν with Δm² ratio ~33.6 | Assignment A or B (R26) |
| **Nucleus** | M²_p mode with winding numbers scaling as mass number A | n₅ = A, n₆ = 2A (R29 scaling law) |

---

## 9. Comparison: old notation → MaST

| Old | MaST | Improvement |
|-----|------|-------------|
| T⁶ | M⁶ | No collision with time |
| T² | M² | Same |
| T²_ν | M²_ν | Reads as "neutrino material plane" |
| "the three T² sheets" | 3M | Compact; arithmetic is transparent (3M = M⁶) |
| R³ | S³ | "Space" more intuitive than ℝ³ |
| R³ × T⁶ | U¹⁰ = S³ × M⁶ | Named universe; parses as "space and material" |
| "compact dimensions" | "material dimensions" | States the thesis |
| "the neutrino T²" | M_ν or "the neutrino sheet" | Shorter, clearer |
| "cross-shear" | (unchanged) | Already clear |
| "within-plane shear" | (unchanged) | Already clear |

---

## 10. The MaST Universe name

**MaST** = Material-Space-Time.
**MaST Universe** = the full framework and its 10D arena.

- Pronounceable, memorable
- States the ingredients: Material, Space, Time
- Claims "material" is on equal footing with space and
  time — not derivative, not emergent, but a fundamental
  geometric ingredient
- "Universe" names the arena (U¹⁰) and completes the
  vocabulary

---

## 11. Open questions

1. **Migration scope.** Adopting MaST requires updating
   all existing files.  Defer until terminology is settled.

2. **"Material" vs. "Matter."**  "Material" chosen because
   it functions as an adjective ("material dimensions").
   "Matter" is a noun for the stuff itself.  Open to
   alternatives.

3. **Symbol for the 9D spatial manifold (M⁶ × S³, no
   time).**  Candidates: Σ⁹, or simply M⁶S³.

4. **Does T¹ need a dedicated symbol?**  Time is already
   universally "t."  T¹ is mainly for completeness in
   the dimension table.

5. **Subscript conventions for cross-shear.**  Currently
   σ_ep means "electron-proton cross-shear."  In MaST
   this could stay as-is or become σ_{M_e M_p}.  The
   former is shorter.
