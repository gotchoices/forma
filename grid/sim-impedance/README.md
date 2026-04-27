# sim-impedance: Lattice junction coupling

**Status:** Tracks 1, 5–10 complete.  Tracks 2-4 framing only.

**Question:** when two lattices of different structure or
orientation interface, what determines the coupling between
them?  Can the fine-structure constant α ≈ 1/137 emerge
from the geometry of this interface?

**Motivation:** the [alpha-in-grid](../../primers/alpha-in-grid.md)
primer frames α as the impedance mismatch between the 2D
material sheet (Ma) and the 3D spatial lattice (S).  A
particle's Coulomb energy is α times its Compton (wave)
energy — only 1/137 of the internal standing-wave energy
couples through the junction into the ambient grid.  This
folder investigates whether that fraction has a geometric
origin in the lattice structures themselves.

---

## Tracks

| Track | Premise | Status | Files |
|-------|---------|--------|-------|
| **1** | 2D-in-2D: two triangular lattices rotated in the same plane | Complete — negative (rate ~1/20, not 1/137) | [T1](T1-planar-rotation.md), [F1](F1-planar-rotation.md) |
| **2** | 2D-in-3D continuum: hexagonal sheet in truncated-octahedral lattice, sweeping orientation | Framing | [T2](T2-3d-lattice.md) |
| **3** | 2D-in-3D discrete: hexagonal rings on a Planck-scale 3D lattice, exact edge matching | Framing | [T3](T3-discrete-embedding.md) |
| **4** | Projection coupling: what fraction of 2D signal projects onto 3D edges? | Framing | [T4](T4-projection-coupling.md) |
| **5** | Wavefront transfer: coherent signal coupling through a shared 2D/3D node (projection matrix, SVD, directional efficiency) | Framing | [T5](T5-wavefront-transfer.md) |
| **6** | 4D Lorentzian lattice: node coincidence of 2D hexagonal in 4D simplex lattice | Steps 0-1 complete | [T6](T6-4d-lorentzian-lattice.md), [F6.0](F6-step0-euclidean4d.md), [F6.1](F6-step1-lorentzian.md) |
| **7** | The ε → 0 limit: do exact coincidences exist? | Complete — negative (rate → 0; no exact coincidences) | [T7](T7-epsilon-limit.md), [F7](F7-epsilon-limit.md) |
| **8** | Aperture coupling: E-field leakage from bending a hexagonal lattice into a torus | Complete — confirms charge selection rule; does not derive α | [T8](T8-aperture-coupling.md), [F8](F8-aperture-coupling.md) |
| **9** | Junction escape fraction: geometric energy leakage at a single curved node | Complete — f_esc depends on lattice resolution; does not derive α | [T9](T9-junction-escape.md), [F9](F9-junction-escape.md) |
| **10** | Propagation leakage: iterative signal propagation with normal escape at each junction | Complete — normal fraction still ~1/N²; does not derive α | [T10](T10-propagation-leakage.md), [F10](F10-propagation-leakage.md) |
| **11** | Vector energy deficit: proper leakage fraction from non-coplanar junctions; four scattering models (GRID S-matrix, equal split, angle-weighted, pure geometry); iterative walk on actual lattice | Complete — convergent invariants found (N²×f → const); resolution-dependent; α not derived | [T11](T11-vector-energy-deficit.md), [F11](F11-vector-energy-deficit.md) |
| **12** | Charge per radian: top-down (distribute known e across junctions); equal-edge lattice with genuine shape distortion; Fourier decomposition shows d₁/d₀ ≈ 0.99 on equal-edge lattice; blocked by fixed-connectivity lattice limitation | Complete — d₁ dominant but not convergent; α not derived | [T12](T12-charge-per-radian.md), [F12](F12-charge-per-radian.md) |

**Track 1** established that 2D-in-2D coincidence counting
gives a smooth, featureless coupling rate dominated by
geometric probability — no structure near 1/137.

**Track 2** introduces the 3D truncated-octahedral lattice,
which has discrete "magic angles" (4 hexagonal face families
along ⟨111⟩ directions).  The coupling function C(θ,φ) is
zero except at these magic angles.  A torus embedded in the
lattice sweeps through the magic angles in proportion to its
surface area — the integral may give α at a specific ε.

**Track 3** goes to the Planck-discrete foundation.  All
edges are exactly L (no tolerance).  The question becomes:
at how many DISCRETE angles can a hexagonal ring share nodes
with a 3D lattice?  A staircase of partial coupling levels
(0 to 6 shared edges) emerges, and the ratio of coupled to
uncoupled angles may converge to 1/137 as the torus size
grows.  If so, α is a pure integer-geometry ratio.

---

## What we learned

### Junction geometry does not produce α

The study systematically tested every static geometric
relationship between a 2D hexagonal lattice and a 3D/4D
simplex lattice:

- **Coincidence counting** (Tracks 1, 3, 6.0, 7): the
  coincidence rate depends entirely on an arbitrary tolerance
  parameter ε.  As ε → 0, the rate goes to zero — the
  lattices are incommensurate and share no exact node or edge
  coincidences at generic orientations.  The value 1/137
  appears at a different ε for each test, with no common
  geometric origin.

- **Per-junction coupling** (Tracks 4, 5, 6.1): the spherical
  2-design theorem proves that all quadratic coupling measures
  (cos², projection, SVD, transfer efficiency) are exactly
  constant at all orientations for any regular simplex lattice
  in any Euclidean dimension.  The η² = I identity extends
  this to Lorentzian reinterpretation.

**No static geometric property of the lattice junction
produces a non-trivial, parameter-free coupling fraction.**

### The tolerance has no geometric justification

Track 7 is the capstone result.  Earlier tracks noted that
1/137 appeared "at ε ≈ X" — but Track 7 shows this is
not meaningful.  The coincidence rate is a smooth monotonic
function of ε that passes through every positive value.
Selecting the ε that gives 1/137 is circular — it assumes
the answer to derive the answer.  Without a first-principles
derivation of "how close is close enough," coincidence
counting cannot constrain α.

### α is topological, not per-junction (a structural lesson)

The sin² energy-projection models in F9 (f_esc) and F11 (vector
deficit) are **per-junction** quantities — and per-junction quantities
are lattice-dependent.  Per-junction values shrink as 1/N² while the
junction count along a 1D 2π loop grows only as N, so the total
vanishes as 1/N in the continuum limit.  α cannot be that.

For a 2π wrap distributed over N junctions, the trade-off between
"many small bends" (fine grid) and "few large bends" (coarse grid)
gives an invariant total only when the per-junction leakage is
**linear** in the bend angle, not quadratic:

| Model | Per-junction | Total over 2π loop |
|---|---|---|
| Linear (sin θ ≈ θ) | 2π/N | **2π — invariant** |
| Quadratic (sin² θ ≈ θ²) | (2π/N)² | 4π²/N → 0 |

[F12 F3](F12-charge-per-radian.md) implicitly uses the linear model
and recovers a clean per-radian charge rate of √(α/π).  This is
consistent with α being a topological invariant of the 2π wrap.
The quadratic (sin²) model used in F9/F11 was appropriate for
*energy projection* but not for *charge accumulation* — charge is
linear in winding (Q = e · n_winding), so the per-radian quantity
is the right level for α.

**Implication:** future α-derivation work should target per-2π-wrap
(topological) quantities, not per-junction (geometric) ones.  The
closed-circle problem in F12 (α sets L → L sets geometry → geometry
sets α) is specifically an artifact of the per-junction framing;
a per-2π-wrap topological calculation does not need to fix L and
so does not close the circle.  This aligns the program with A6
(α as the cost of the *minimal vortex* — the topological object,
not its lattice rendering), with R19/R55/R59 (wrapping integers
on compact dimensions), and with [`foundations.md`](../foundations.md)
Q2 (ζ–α consistency — both topological quantities).

### Viable pathways remain

The sim-impedance study tested junction geometry, not all
possible mechanisms.  See [F7](F7-epsilon-limit.md) §F6 for
the full list.  The approaches that remain open:

1. **Internal sheet geometry** — α from the wrapping/shear
   of the triangular lattice on the torus (MaSt R15, R19)
2. **Topological defect energy** — α from the lattice action
   cost of a minimal vortex (GRID A6)
3. **Dynamic wave scattering** — α from the transmission
   amplitude of waves at sheet-lattice junctions
4. **Multi-junction collective effects** — interference or
   coherence across extended interfaces

---

## Files

| File | Contents |
|------|----------|
| [T1-planar-rotation.md](T1-planar-rotation.md) | Track 1 framing |
| [F1-planar-rotation.md](F1-planar-rotation.md) | Track 1 findings |
| [T2-3d-lattice.md](T2-3d-lattice.md) | Track 2 framing (continuum 3D) |
| [T3-discrete-embedding.md](T3-discrete-embedding.md) | Track 3 framing (discrete 3D) |
| [F3-step1-single-node.md](F3-step1-single-node.md) | Track 3 Step 1 findings |
| [scripts/track1_planar_rotation.py](scripts/track1_planar_rotation.py) | Track 1 script |
| [scripts/track3_step1_single_node.py](scripts/track3_step1_single_node.py) | Track 3 Step 1 (coarse) script |
| [scripts/track3_step1_fine.py](scripts/track3_step1_fine.py) | Track 3 Step 1 (fine resolution) script |
| [F5-wavefront-transfer.md](F5-wavefront-transfer.md) | Track 5 findings |
| [scripts/track5_wavefront_transfer.py](scripts/track5_wavefront_transfer.py) | Track 5 script |
| [F6-step0-euclidean4d.md](F6-step0-euclidean4d.md) | Track 6 Step 0 findings (Euclidean 4D coincidence) |
| [F6-step1-lorentzian.md](F6-step1-lorentzian.md) | Track 6 Step 1 findings (Lorentzian per-junction) |
| [scripts/track6_step0_euclidean4d.py](scripts/track6_step0_euclidean4d.py) | Track 6 Step 0 script |
| [scripts/track6_step1_lorentzian.py](scripts/track6_step1_lorentzian.py) | Track 6 Step 1 script |
| [T7-epsilon-limit.md](T7-epsilon-limit.md) | Track 7 framing |
| [F7-epsilon-limit.md](F7-epsilon-limit.md) | Track 7 findings |
| [scripts/verify_epsilon_to_zero.py](scripts/verify_epsilon_to_zero.py) | Track 7 script |
| [T9-junction-escape.md](T9-junction-escape.md) | Track 9 framing |
| [F9-junction-escape.md](F9-junction-escape.md) | Track 9 findings |
| [scripts/track9_junction_escape.py](scripts/track9_junction_escape.py) | Track 9 script |
| [scripts/track9b_total_escape.py](scripts/track9b_total_escape.py) | Track 9b follow-up script |
| [T10-propagation-leakage.md](T10-propagation-leakage.md) | Track 10 framing |
| [F10-propagation-leakage.md](F10-propagation-leakage.md) | Track 10 findings |
| [scripts/track10_propagation_leakage.py](scripts/track10_propagation_leakage.py) | Track 10 script |
| [output/](output/) | Plots and data |
