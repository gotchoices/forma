# ma_model.py — Design Spec

Next-generation Ma model engine.  Lives alongside `ma.py`
(unchanged) in `lib/`.  Old scripts keep working; new scripts
can import from either.


## Motivation

`ma.py` is correct and tested but architecturally primitive:

- **Brute-force scan.** `scan_modes` and `find_modes` enumerate
  (2n+1)⁶ modes.  At n_max = 5 this is 1.8M; at n_max = 10
  it is 350M.  Most are immediately discarded by the energy
  ceiling.

- **No state.**  Every function takes the full parameter set.
  Rebuild the metric, recompute L, re-invert G̃ on every call.

- **No decomposition.**  The energy is computed as a single
  scalar.  There is no way to ask "how much comes from Ma_e
  vs Ma_p vs cross-coupling?"

- **No sensitivity.**  No Jacobian, no gradient.  Parameter
  searches use `differential_evolution` (black-box optimizer)
  wrapping the brute-force scan.

- **No true inverse.**  "Going backwards" (masses → geometry)
  requires brute-force sweeps of the parameter space.

The mathematical structure — a quadratic form on a lattice —
supports far better algorithms.  This spec describes what
`ma_model.py` will provide.


## Non-goals

- Replace `ma.py`.  All existing scripts keep their imports.
- Change the static model's physics.  Same metric, same energy
  formula, same charge and spin rules.  The dynamic model (Feature
  10) solves for the torus shape from scratch using force balance
  — it is a self-consistent calculation, not a perturbation.  The
  static flat-torus model emerges as the α → 0 limit (perfectly
  reflecting wall).  Results happen to be close to the static
  values (corrections are O(α²)), but this is an output of the
  calculation, not an assumption baked in.
- Be framework-heavy.  No PyTorch, no JAX.  NumPy + SciPy only.


## Architecture

```
┌──────────────────────────────────────────────────┐
│  Ma  (the model object)                          │
│                                                  │
│  State (static — always present):                │
│    r_e, r_ν, r_p     aspect ratios               │
│    s₁₂, s₃₄, s₅₆    within-plane shears         │
│    σ_ep, σ_eν, σ_νp  cross-plane shears          │
│    L[6]              circumferences (fm)          │
│    G̃[6,6]           dimensionless metric         │
│    G̃⁻¹[6,6]         inverse metric               │
│    M[6,6]            energy-space kernel          │
│    Chol[6,6]         Cholesky of M (for scan)     │
│                                                  │
│  State (dynamic — when dynamic=True):            │
│    dynamic            bool flag                   │
│    _harm_cache        {(n_tube,n_ring,r) → harm}  │
│                                                  │
│  Core:                                           │
│    energy(n)         mode energy (MeV)            │
│                      static or dynamic per flag   │
│    energy_static(n)  always the flat-torus E      │
│    charge(n)         electric charge              │
│    spin(n)           spin-½ count                 │
│    energy_decomp(n)  energy by sheet + cross       │
│    jacobian(n)       ∂E/∂params                   │
│                                                  │
│  Dynamic:                                        │
│    pressure_harmonics(n_tube, n_ring, r)          │
│    wall_shape(n_tube, n_ring, r)                  │
│    dynamic_correction(n)    δE/E for mode n       │
│    filter_factor(n)         suppression vs fund.  │
│                                                  │
│  Scan:                                           │
│    modes(E_max, charge, spin, ...)                │
│      → fast ellipsoid enumeration                 │
│                                                  │
│  Inverse:                                        │
│    fit(targets)      masses+modes → params        │
│    sensitivity(n)    which params matter?         │
│                                                  │
│  I/O:                                            │
│    to_dict() / from_dict()                       │
│    summary()         human-readable printout      │
│                                                  │
│  Compat:                                         │
│    from_ma_py(Gti, L)  wrap legacy outputs        │
│    to_ma_py()          export for legacy code      │
│                                                  │
└──────────────────────────────────────────────────┘
```


## Feature 1: Stateful geometry object

### What

A single `Ma` instance holds the full geometry state.
Construction computes and caches everything downstream.

### Interface

```python
m = Ma(r_e=6.6, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906)

m.L          # ndarray(6,) — circumferences in fm
m.Gt         # ndarray(6,6) — G̃
m.Gti        # ndarray(6,6) — G̃⁻¹
m.s12        # float — electron within-plane shear
m.params     # dict of all parameters
```

### Construction options

```python
# From aspect ratios (derives L, s, builds metric)
Ma(r_e=6.6, r_nu=5.0, r_p=8.906)

# With cross-shears
Ma(r_e=6.6, r_nu=5.0, r_p=8.906,
   sigma_ep=-0.0906, sigma_enu=0.0, sigma_nup=0.0)

# With asymmetric cross-shears (12 independent entries)
Ma(r_e=6.6, r_nu=5.0, r_p=8.906,
   cross_shears={(0,4): -0.08, (0,5): -0.10, ...})

# Self-consistent (iterate L until m_e, m_p exact)
Ma(r_e=6.6, r_nu=5.0, r_p=8.906,
   sigma_ep=-0.0906, self_consistent=True)

# Wrap legacy ma.py output
Ma.from_legacy(Gtilde_inv=Gti, L=L)
```

### Mutability

Immutable after construction.  To explore a different geometry,
create a new `Ma`.  This avoids stale-cache bugs and makes it
safe to pass instances across functions.

To make parameter sweeps ergonomic:

```python
m2 = m.with_params(sigma_ep=-0.10)   # new Ma, one param changed
m3 = m.with_params(r_p=9.0)          # new Ma, different r_p
```

`with_params` returns a new `Ma` with the specified parameters
changed and everything re-derived.


## Feature 2: Fast mode enumeration

### Problem

The energy bound E ≤ E_max defines an ellipsoid in integer-
lattice space:

    nᵀ M n ≤ R²

where M_ij = G̃⁻¹_ij / (L_i L_j) and R = E_max / (2πℏc).

The brute-force approach scans a hypercube of side 2n+1 and
tests each point.  The ellipsoid occupies a tiny fraction of the
cube when the scale hierarchy is large (L_ν/L_e ~ 10⁸).

### Algorithm: Fincke–Pohst enumeration

1. Cholesky-decompose M = LLᵀ.
2. Enumerate lattice points inside the ellipsoid dimension by
   dimension, using the Cholesky rows to bound each coordinate
   given the others.
3. At each level, compute the residual radius and only recurse
   if the remaining budget is positive.

This visits only points inside the ellipsoid.  For a 6D lattice
with ~14,000 modes below 10 GeV, the algorithm visits ~14,000
points instead of ~1.8M (at n_max = 5) or ~900M (at n_max = 15).

### Interface

```python
modes = m.modes(E_max_MeV=10000)
# Returns: list of Mode namedtuples, sorted by energy

modes = m.modes(E_max_MeV=2000, charge=-1, spin=1)
# Filtered: only Q = -1, spin-½
```

### Mode object

```python
Mode = namedtuple('Mode', ['n', 'E_MeV', 'charge', 'spin_halves'])
```

Lightweight, sortable, hashable.  No back-reference to the `Ma`
instance (keeps it cheap to store thousands).


## Feature 3: Energy decomposition

### What

Break the total E² into contributions from each sheet and each
cross-coupling.  The quadratic form decomposes naturally:

    E² = E²_e + E²_ν + E²_p + 2·E²_eν + 2·E²_ep + 2·E²_νp

where E²_e = (2πℏc)² ñ_e^T [G̃⁻¹]_{ee} ñ_e  (the 2×2 electron
block), and E²_ep = (2πℏc)² ñ_e^T [G̃⁻¹]_{ep} ñ_p  (the cross
block), etc.

### Interface

```python
d = m.energy_decomp(n=(0, -2, 1, 0, 0, 2))
# d.total       938.3 MeV
# d.e_sheet      23.1 MeV²  (fraction of E²)
# d.nu_sheet      0.0 MeV²
# d.p_sheet     912.5 MeV²
# d.ep_cross      2.7 MeV²
# d.enu_cross     0.0 MeV²
# d.nup_cross     0.0 MeV²
# d.fractions   {'e': 0.025, 'nu': 0.0, 'p': 0.973, ...}
```

This tells you immediately that the neutron is 97% proton-sheet,
2.5% electron-sheet, and the cross-coupling provides the mass
splitting from the proton.


## Feature 4: Analytical Jacobian

### What

Compute ∂E/∂θ for any mode, where θ is any geometry parameter
(r_e, r_ν, r_p, σ_ep, s₁₂, etc.).

### Math

Since E² = (2πℏc)² ñᵀ G̃⁻¹ ñ:

    ∂E/∂θ = (2πℏc)² / (2E) · ñᵀ (∂G̃⁻¹/∂θ) ñ

For cross-shears, ∂G̃⁻¹/∂σ is computed via the matrix identity:

    ∂A⁻¹/∂θ = −A⁻¹ (∂A/∂θ) A⁻¹

Since ∂G̃/∂σ_ep has only four nonzero entries (the e-p block),
the full Jacobian is a rank-4 perturbation — cheap to compute.

For aspect ratios, the chain is longer (r → L → G̃ → G̃⁻¹) but
still analytical.

### Interface

```python
J = m.jacobian(n=(0, -2, 1, 0, 0, 2))
# J['r_e']       ∂E/∂r_e   (MeV per unit r_e)
# J['r_p']       ∂E/∂r_p
# J['sigma_ep']  ∂E/∂σ_ep
# ...

# Vectorized: Jacobian for multiple modes at once
J_matrix = m.jacobian_matrix(modes, params=['r_e', 'r_p', 'sigma_ep'])
# shape: (len(modes), 3)
```

### Use cases

- **Sensitivity analysis:** Which parameters does the neutron
  mass depend on?  (Answer: mostly σ_ep and r_p.)
- **Error propagation:** If r_e is uncertain by ±0.1, how much
  does the electron mass move?
- **Gradient-based fitting:** Replace `differential_evolution`
  with Gauss–Newton or Levenberg–Marquardt.


## Feature 5: Inverse solver (fit)

### What

Given a set of target particles (mass, mode assignment), find
the geometry parameters that best reproduce them.

### Interface

```python
targets = [
    Target(n=(1, 2, 0, 0, 0, 0),   mass_MeV=0.511),     # electron
    Target(n=(0, 0, 0, 0, 1, 2),   mass_MeV=938.272),    # proton
    Target(n=(0, -2, 1, 0, 0, 2),  mass_MeV=939.565),    # neutron
    Target(n=(-1, 5, 0, 0, -2, 0), mass_MeV=105.658),    # muon
]

result = Ma.fit(
    targets,
    free_params=['r_e', 'r_p', 'sigma_ep'],
    fixed_params={'r_nu': 5.0},
)
# result.params    {'r_e': 6.600, 'r_p': 8.906, 'sigma_ep': -0.0906}
# result.residuals [0.000, 0.000, 0.001, 0.832]  (MeV errors)
# result.ma        Ma instance at the optimal point
# result.jacobian  Jacobian at the solution
# result.cov       Parameter covariance matrix
```

### Algorithm

1. Start from initial guess (or current Ma state).
2. At each iteration:
   a. Compute energies for all target modes.
   b. Compute Jacobian (Feature 4).
   c. Levenberg–Marquardt step on the residual vector.
3. Converge when residuals are below tolerance.

Because the energy formula is smooth and the Jacobian is cheap,
this should converge in ~5–20 iterations for well-conditioned
problems (fewer free parameters than targets).

### Degeneracies

When free parameters > targets, the problem is underdetermined.
The solver should detect this and report the null space (which
parameter combinations leave all targets unchanged).


## Feature 6: Sensitivity report

### What

For a given mode, report which parameters it depends on and how
strongly.  Wraps the Jacobian into a human-readable format.

### Interface

```python
m.sensitivity(n=(0, -2, 1, 0, 0, 2))
# Neutron (0,−2,+1,0,0,+2)  E = 939.6 MeV
#   r_e:        ∂E/∂r_e  = −0.02 MeV/unit   (weak)
#   r_p:        ∂E/∂r_p  = −48.3 MeV/unit   (strong)
#   sigma_ep:   ∂E/∂σ_ep = −14.2 MeV/unit   (strong)
#   r_nu:       ∂E/∂r_ν  =  0.00 MeV/unit   (negligible)
```


## Feature 7: Spectrum queries

### What

Rich filtering and grouping over the enumerated mode spectrum.

### Interface

```python
# All charge −1 fermions below 2 GeV, grouped by spin
spec = m.spectrum(E_max_MeV=2000, charge=-1, spin=1)

# Count modes by charge
m.mode_count(E_max_MeV=10000, by='charge')
# {-2: 45, -1: 14312, 0: 98021, 1: 14312, 2: 45}

# Nearest mode to a target mass
m.nearest(mass_MeV=1776.86, charge=-1, spin=1)
# Mode(n=(-1,5,0,0,-2,-4), E_MeV=1876.4, ...)
```


## Feature 8: Serialization

### What

Save/load a geometry to/from a plain dict (JSON-compatible).
Useful for recording the exact geometry used in a study.

### Interface

```python
d = m.to_dict()
# {'r_e': 6.6, 'r_nu': 5.0, 'r_p': 8.906,
#  'sigma_ep': -0.0906, 'sigma_enu': 0.0, 'sigma_nup': 0.0,
#  'self_consistent': True, 'L': [4.396, 0.666, ...], ...}

m2 = Ma.from_dict(d)
assert m2.energy((1,2,0,0,0,0)) == m.energy((1,2,0,0,0,0))
```


## Feature 9: Compatibility layer

### What

Interoperate with legacy `ma.py` / `ma_solver.py` code without
any changes to those files.

### Interface

```python
# Import a legacy metric into the new model
from lib.ma import build_scaled_metric
Gt, Gti, L, info = build_scaled_metric(r_e=6.6, r_nu=5.0, r_p=6.6)
m = Ma.from_legacy(Gtilde_inv=Gti, L=L)

# Export for use with legacy functions
Gti, L = m.to_legacy()
from lib.ma import mode_energy
E = mode_energy((1,2,0,0,0,0), Gti, L)  # same as m.energy(...)
```


## Feature 10: Dynamic model (α-impedance)

Established in R40.  The static model treats the torus as a fixed
flat geometry.  The dynamic model says the torus wall responds to
the mode: the wall IS the (1−α) energy contour.  This introduces
mode-dependent cross-section shapes, eigenvalue corrections, and
a natural low-pass filter.

The dynamic model solves for the torus shape from first principles:
the wall sits where inward vacuum pressure balances outward mode
pressure.  The shape, the mode, and the energy are all outputs of
this self-consistent calculation — no static baseline is assumed.

Two solution methods are implemented:

- **`dynamic='full'`** (or `dynamic=True`): Iterative force-balance
  solve.  Starting from a circular cross-section, repeats:
  compute 3D geodesic curvature on the current shape → Fourier-
  decompose the pressure → compute equilibrium deformation → update
  the cross-section.  Converges when the shape stops changing
  (|Δε_k| < tol).  This IS the self-consistent solution: the code
  discovers that corrections are small rather than assuming it.
  Convergence is geometric with ratio ~α ≈ 0.007, so 2–3 iterations
  suffice.

- **`dynamic='shortcut'`**: One-shot perturbation.  Computes pressure
  on the undeformed (circular) cross-section and applies the
  equilibrium formula once: E_dynamic = E_static × (1 + δE/E).
  This is iteration zero of the full solve.  Fast but does not
  capture the feedback between shape and pressure.  Agrees with
  the full solve to O(α⁴) in energy for known particles.

For `dynamic=False` (default), no corrections are applied and
all methods return the flat-torus (static) results.


### Physical picture

A standing wave (mode) on a flat torus has |ψ|² = const — the
energy density is perfectly uniform.  The (1−α) contour is a
circle at every tube angle.

On the 3D-embedded torus, the geodesic curvature and path speed
vary with the tube angle θ₁ because ρ(θ₁) = R + a cos θ₁.
Where curvature is higher, centrifugal pressure pushes the wall
outward.  The elastic wall resists with a restoring force that
scales as k² for the k-th Fourier harmonic (thin-shell elasticity).

Equilibrium: δr_k/a = α × (|c_k|/|c₀|) / k².

The mode with tube winding n₁ couples to wall harmonic k = 2|n₁|
through the selection rule ⟨ψ|δV_k|ψ⟩ ∝ δ_{k,2|n₁|}.  Higher
tube-winding modes couple to higher (weaker) harmonics, giving a
natural low-pass filter in tube winding number.

Energy partition: fraction (1−α) of the mode energy is confined
inside the wall; fraction α leaks out as the external EM field
(the particle's Coulomb field).  α runs with energy because
higher-energy modes push harder against the wall, increasing
transparency — this is vacuum polarization in geometric language.


### Mode-dependent cross-section

The wall shape r(θ₁)/a = 1 + Σ_k δr_k cos(kθ₁ − φ_k) depends
on the mode's winding numbers and the sheet's aspect ratio:

- **Same n₁, different n₂:** The dominant harmonic is always k=2
  (from the cos 2θ₁ variation of torus curvature), but the
  amplitude |c₂/c₀| depends on n₂/n₁ through the speed weighting.
  Ring-dominated modes (high n₂/n₁) have larger ρ-variation →
  stronger elliptical deformation.  Tube-dominated modes (high
  n₁/n₂) are more circular.

  Example on the proton sheet (r=8.906):
    (1,2): |c₂/c₀| ≈ 0.37  → δr₂/a ≈ 6.7×10⁻⁴
    (1,4): |c₂/c₀| larger  → more elliptical
    (3,1): |c₂/c₀| smaller → nearly circular

- **n_tube = 0 (ring-only winding):** The mode has no θ₁
  dependence → couples to k=0 (DC component) → no eigenvalue
  correction from this sheet.

- **Cross-sheet modes (e.g., neutron):** Each sheet's torus
  deforms independently based on that sheet's (n_tube, n_ring).
  The total correction is a weighted sum over sheets, weighted
  by E² fractions from energy_decomp().


### Pressure harmonics computation

For a mode with tube winding n₁ and ring winding n₂ on a sheet
with aspect ratio r = a/R:

1. Parameterize the 3D geodesic using the flat-torus path
   (θ₁ = n₁t, θ₂ = n₂t) projected onto the embedding.  R40 F19-F22
   established that the Clairaut (surface-intrinsic) geodesic does
   not exist for a/R > 1 (all known particles).  The flat-torus
   geodesic is the physically correct path — the photon sees flat
   space internally.
     x(t) = ρ cos(n₂t),  y(t) = ρ sin(n₂t),  z(t) = a sin(n₁t)
   where ρ(t) = R + a cos(n₁t).

2. Compute the path speed:
     v(t) = |dr/dt| = √((n₁a)² sin²(n₁t) + (n₂ρ(t))²  + ...)
   (full 3D derivative of position).

3. Compute the Frenet curvature vector κ_vec = dT̂/ds and project
   onto the tube-radial unit vector ê_r.  The centrifugal reaction
   (outward pressure) is κ_outward = −κ_radial.

4. Speed-weight: P(θ₁) ∝ κ_outward(θ₁) × v(θ₁).  This accounts
   for the energy flux through each tube angle.

5. Bin P by θ₁ ∈ [0, 2π) and Fourier-decompose:
     P(θ₁) = c₀ + Σ_k [A_k cos(kθ₁) + B_k sin(kθ₁)]
   with amplitudes c_k = √(A_k² + B_k²), phases φ_k = atan2(B_k, A_k).

The harmonics depend only on (n₁, n₂, r) — not on absolute scale,
not on cross-shears, not on the other sheets.  They can be cached.

Symmetry: by the θ₁ → −θ₁ symmetry of the torus, B_k = 0 and
only even harmonics are non-negligible for the (1,2) fundamental.
Odd harmonics arise only from numerical noise or symmetry-breaking
windings.


### Eigenvalue correction

For a 6D mode n = (n₁, n₂, n₃, n₄, n₅, n₆):

1. Identify the active sheets (those with non-zero tube winding):
     electron: n₁ ≠ 0 → (n₁, n₂) on torus with r_e
     neutrino: n₃ ≠ 0 → (n₃, n₄) on torus with r_ν
     proton:   n₅ ≠ 0 → (n₅, n₆) on torus with r_p

2. For each active sheet, compute the deformation harmonics
   δr_k/a = α × (|c_k|/|c₀|) / k² using pressure_harmonics().

3. The eigenvalue shift from sheet S:
     (δE/E)_S = ε_{2|n_tube|} / 2
   where ε_k = δr_k/a.  The factor of 1/2 comes from first-order
   perturbation theory: δλ = ⟨ψ|δV|ψ⟩ and the overlap integral
   ⟨cos²(n₁θ₁)|cos(2n₁θ₁)⟩ = 1/2.

4. Weight by the sheet's E² fraction (from energy_decomp):
     δE/E = Σ_S  w_S × (δE/E)_S
   where w_S = E²_S / E²_total.

5. Dynamic energy:

   **Shortcut** (`dynamic='shortcut'`):
     E_dynamic = E_static × (1 + δE/E).
     Steps 1–4 run once on the circular (undeformed) cross-section.
     Valid when δE/E << 1 (all known particles: δE/E ~ 10⁻⁴).

   **Full** (`dynamic='full'` or `dynamic=True`):
     Iterate steps 1–4 with the 3D geodesic recomputed on the
     deformed cross-section at each iteration:
       a. Start with circular cross-section: r(θ₁)/a = 1.
       b. Compute pressure harmonics on current shape.
       c. Compute equilibrium deformation δr_k from the pressure.
       d. If max|δr_k^new − δr_k^old| < tol, stop.
       e. Update cross-section: r(θ₁) = a(1 + Σ δr_k cos(kθ₁ − φ_k)).
       f. Go to (b).
     The 3D path on the deformed torus uses:
       ρ(θ₁) = R + a(1 + ε(θ₁)) cos θ₁
       z(θ₁) = a(1 + ε(θ₁)) sin θ₁
     with analytical derivatives (da/dθ₁ terms) for the tangent
     and curvature computation.

     Convergence: geometric with ratio ~α.  Iteration 0 = shortcut.
     Iteration 1 corrects to O(α⁴).  Typically 2–3 iterations to
     reach machine precision.


### Low-pass filter

The filter suppression factor for a mode relative to the
fundamental (1,2) on the same sheet:

  F(n₁) = ε_{2|n₁|} / ε₂

For the proton sheet (r = 8.906):
  n₁=1: F = 1.0     (reference)
  n₁=2: F ≈ 0.025   (40× suppression)
  n₁=3: F ≈ 0.002   (450× suppression)
  n₁=4: F ≈ 0.0003  (3000× suppression)

The suppression goes as ~1/(2n₁)² from the elastic response,
modulated by the harmonic content |c_{2n₁}|/|c₀|.  This is a
soft low-pass filter — it shifts eigenvalues rather than imposing
a hard cutoff.  Whether this constitutes "ghost suppression"
depends on the magnitude of the shift relative to observational
constraints.


### Per-tile wave function (future refinement)

The current model uses the flat-torus mode (|ψ|² = const) as the
energy density.  The non-uniformity comes entirely from the 3D
curvature weighting.

A more refined approach: solve the wave equation per tile of area
on the deformed cross-section.  On a deformed surface, the mode
IS non-uniform — energy concentrates where the cross-section is
wider (lower effective potential) and rarefies where it narrows.
This creates a feedback loop: the energy density shapes the wall,
and the wall shapes the energy density.

For the fundamental (1,2) mode this is a small correction (the
flat-torus mode is uniform by definition, and the deformation is
O(α²)).  For higher harmonics, especially those with large n₁
where the tube winding drives strong θ₁ dependence, the per-tile
solution could differ significantly from the flat-torus
approximation.

Implementation: solve the Sturm-Liouville problem on the deformed
cross-section using the α-impedance wall shape from R40 F25 as the
boundary.  The Sturm-Liouville solver from R21 Track 1 handles
arbitrary cross-sections.  The extension is to iterate:
shape → mode → pressure → shape until self-consistent.


### Running α(E)

Wall transparency increases with mode energy.  Higher-energy
modes push harder against the wall → more energy leaks through
→ effective α increases.  This is the geometric realization of
vacuum polarization.

Quantitative formula: TBD.  The self-consistent equation is
α(E) = α₀ × f(E/E₀) where f encodes the energy-dependent
penetration depth.  R41 Track 2 should derive the functional
form from the force balance.


### API

```python
# Construction
m = Ma(r_e=0.5, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906,
       dynamic='full')          # iterative force-balance solve
# dynamic=True  → same as 'full'
# dynamic='shortcut' → one-shot perturbative (fast, approximate)
# dynamic=False → static (no corrections)

# Energy
m.energy((1, 2, 0, 0, 0, 0))         # dynamic energy (MeV)
m.energy_static((1, 2, 0, 0, 0, 0))  # flat-torus energy (MeV)

# Dynamic correction
corr = m.dynamic_correction((1, 2, 0, 0, 0, 0))
# corr.delta_E_over_E   → float (δE/E)
# corr.per_sheet        → dict: 'e'→δE/E_e, 'p'→δE/E_p, ...
# corr.dominant_k       → int (coupling harmonic)
# corr.filter_factor    → float (suppression vs fundamental)

# Pressure harmonics (per-sheet)
# When dynamic='full': converged harmonics from iterative solve
# When dynamic='shortcut' or False: computed on circular cross-section
harm = m.pressure_harmonics(n_tube=1, n_ring=2, r=8.906)
# harm.c_k         → ndarray, Fourier amplitudes
# harm.delta_r_k   → ndarray, wall deformation per harmonic
# harm.phi_k       → ndarray, phases

# Wall shape (cross-section at N angles)
shape = m.wall_shape(n_tube=1, n_ring=2, r=8.906)
# shape.theta       → ndarray (N,)
# shape.r_over_a    → ndarray (N,), the r(θ₁)/a profile
# shape.eccentricity → float

# Dynamic method introspection
m.dynamic          # True/False (are corrections enabled?)
m.dynamic_method   # 'off', 'shortcut', or 'full'

# Filter suppression relative to (1,2) fundamental
m.filter_factor((3, 1, 0, 0, 0, 0))   # float ≈ 0.002

# Scanning uses dynamic energies when dynamic=True
modes = m.scan_modes(n_max=3, E_max_MeV=2000)
# Mode namedtuples include E_MeV (dynamic) and delta_E_MeV

# Fitting uses dynamic energies when dynamic=True
result = Ma.fit(targets, free_params=['r_p', 'sigma_ep'],
                dynamic=True)
```


### Integration with existing features

- **energy()**: When `dynamic='full'` (or `True`), iterates the
  force-balance shape to convergence, then computes the eigenvalue
  correction from the self-consistent harmonics.  When
  `dynamic='shortcut'`, uses one-shot perturbation on the circular
  cross-section.  When `dynamic=False` (default), returns E_static.
  Backward compatible — all existing code continues to work.

- **energy_static()**: New method.  Always returns the flat-torus
  energy.  Identical to the current energy() when dynamic=False.

- **scan_modes()**: Uses energy() — so scans use dynamic energies
  when `dynamic=True`.  The Mode namedtuple gains an optional
  `delta_E_MeV` field (None when static).

- **fit()**: Accepts a `dynamic=True` kwarg.  When set, the
  residuals and finite-difference Jacobian use dynamic energies.
  The self-consistency iteration targets dynamic m_e and m_p.
  This is the reverse solver: given observed masses and mode
  assignments, find the geometry parameters that reproduce them
  using the full force-balance model.  The static fit provides
  a good starting point — the dynamic fit solves self-consistently
  from there.

- **jacobian()**: When `dynamic=True`, includes ∂(δE)/∂r
  contributions.  The dynamic correction depends on r through
  the pressure harmonics, so the chain rule extends:
    ∂E_dynamic/∂r = ∂E_static/∂r × (1 + δ) + E_static × ∂δ/∂r

- **to_dict() / from_dict()**: Records `dynamic` flag.

- **summary()**: Reports dynamic corrections for electron and
  proton modes when dynamic=True.


### Computation cost

The pressure harmonics computation requires integrating the 3D
geodesic (~4000 sample points), computing curvature, and a
Fourier transform.  This is O(N × N_harm) per call.

For `dynamic='full'`, each (n_tube, n_ring, r) triple requires
2–3 iterations (geometric convergence with ratio ~α).  Cost is
2–3× the shortcut per unique triple.

The harmonics depend only on (n_tube, n_ring, r) and the method,
and are cached in a dict keyed by this triple.  For a scan of
~14,000 modes, most modes share sheets (same r), and many share
winding numbers.  Cache hit rate should be high.

The dynamic correction for one mode is a lookup + weighted sum —
negligible cost once harmonics are cached.


## Implementation plan

### Phase 1: Core (minimum viable)

1. `Ma` class with construction from aspect ratios + shears.
2. `energy()`, `charge()`, `spin()` — delegating to `ma.py`
   functions internally at first.
3. `to_dict()` / `from_dict()` / `from_legacy()`.
4. `summary()` printout.
5. `with_params()` for immutable updates.

Validates: all existing study results reproduce exactly.

### Phase 2: Fast scan

6. Implement `M` (energy-space kernel) and its Cholesky.
7. Fincke–Pohst lattice enumeration.
8. `modes()` with filtering.
9. Benchmark against `scan_modes` — should be 100–1000× faster
   at n_max ≥ 5.

### Phase 3: Decomposition + Jacobian

10. `energy_decomp()` from block partition of G̃⁻¹.
11. Analytical `∂G̃/∂θ` for all parameters.
12. `jacobian()` and `jacobian_matrix()`.
13. `sensitivity()` wrapper.

### Phase 4: Inverse solver

14. `Target` dataclass.
15. `Ma.fit()` using Gauss–Newton with the analytical Jacobian.
16. Degeneracy detection (null space of the Jacobian).
17. Parameter covariance from the Fisher information matrix.

### Phase 5: Spectrum queries

18. `spectrum()` with grouping.
19. `mode_count()` with `by` parameter.
20. `nearest()` for quick lookups.

### Phase 6: Dynamic model (R41)

21. `pressure_harmonics()` — 3D geodesic curvature, speed-weighted
    Fourier decomposition.  Cached by (n_tube, n_ring, r).
22. `wall_shape()` — reconstruct r(θ₁)/a from harmonics.
23. `dynamic_correction()` — per-sheet eigenvalue shifts, weighted
    sum for cross-sheet modes.
24. `filter_factor()` — suppression relative to fundamental.
25. Wire `dynamic=True` flag through `energy()`, `scan_modes()`,
    `fit()`, `jacobian()`, `to_dict()`, `summary()`.
26. `energy_static()` — always returns flat-torus energy.
27. Self-consistency iteration with dynamic energies.


## Testing strategy

Every phase must pass:

1. **Regression:** For the standard geometry (r_e=6.6, r_ν=5.0,
   r_p=8.906, σ_ep=−0.0906), the new code must reproduce the
   same energies as `ma.py` to machine precision.

2. **Known particles:** Electron, proton, neutron, muon masses
   must match PDG values to the documented error (< 1.2%).

3. **Self-consistency:** `Ma(..., self_consistent=True)` must
   give E(electron) = 0.511 MeV, E(proton) = 938.272 MeV to
   12 digits.

4. **Roundtrip:** `Ma.from_dict(m.to_dict())` reproduces all
   outputs exactly.

5. **Speed:** `modes(E_max_MeV=10000)` at effective n_max ≥ 10
   completes in < 1 second (vs hours for brute force).

Phase 6 (dynamic model) additionally requires:

6. **Static backward compat:** `Ma(..., dynamic=False)` produces
   identical results to the pre-dynamic code.

7. **R40 Track 11 match:** For the proton (1,2) mode at r=8.906,
   `pressure_harmonics(1, 2, 8.906)` must reproduce Track 11's
   Fourier coefficients (|c₂/c₀| ≈ 0.37, dominant k=2).
   `dynamic_correction` must give δE/E ≈ 3.4×10⁻⁴.

8. **Magnitude check:** For all modes below 10 GeV,
   |δE/E| < α ≈ 0.0073.  The force-balance solution produces
   corrections of this order — confirming the static model is a
   good zeroth-order approximation, not assuming it.

9. **Symmetry:** Modes related by CPT (n → −n) must have
   identical |δE/E| (same magnitude, possibly different sign).

10. **No-tube-winding rule:** Modes with n_tube = 0 on all sheets
    must have exactly zero dynamic correction.


## Dependencies

- `numpy` (already used by `ma.py`)
- `scipy.linalg` for Cholesky decomposition
- `scipy.optimize` for Levenberg–Marquardt (Phase 4)
- No new external dependencies


## File layout after completion

```
lib/
  index.md          ← you are here (library guide)
  ma-model.md       ← this file (design spec)
  constants.py      unchanged
  wvm.py            unchanged
  series.py         unchanged
  ma.py             unchanged
  ma_solver.py      unchanged
  ma_model.py       the model engine (static + dynamic)
  test_ma_model.py  regression tests (static + dynamic)
```
