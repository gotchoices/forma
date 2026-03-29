# Hydrogen Fusion — MaSt Model

Interactive visualization of proton-proton fusion physics using the MaSt
(Material-Spacetime) framework from Q95.

## Features

### Left panel: Nuclear Potential V(r)
- Coulomb repulsion V_C = 1.44/r MeV (red)
- MaSt strong force: direct Ma-Ma coupling at torus overlap (blue)
- Total potential (white) showing barrier and well
- Thermal energy kT line (yellow dashed)
- Barrier height, well depth, turning points annotated

### Right panel: Fusion Rate vs Temperature
- Standard pp reaction rate ⟨σv⟩(T) via Gamow peak approximation
- WKB-enhanced rate for modified potential (cyan)
- Solar core temperature marked (orange)
- Current slider temperature highlighted (yellow)
- Temperature exponent ν displayed

### Controls
- **Temperature**: 10⁵ — 10¹⁰ K (log slider)
- **B field**: 0 — 1000 T (MaSt alignment effect)
- **Well depth**: 10 — 300 MeV (MaSt: ~150 MeV = coupling 137)
- **Range**: 0.5 — 4.0 fm (MaSt: proton λ_C ≈ 1.32 fm)
- **Presets**: MaSt (from Q95) / Empirical (fitted nuclear data)
- **Scenarios**: Solar / Tokamak / H₂ gas / H₂O electrolysis

### Info panel
- Barrier height, well depth, kT, Gamow peak energy
- Tunneling probability, alignment fraction, fusion rate
- Temperature exponent (stability indicator)
- Scenario-specific analysis (stability, cold fusion, water limiting)

## Physics

### Potential model (Woods-Saxon + Coulomb)
V(r) = 1.44/r − V₀/(1 + exp((r−R)/a)) + hard core

The MaSt strong force (Q95 §2-3) arises from direct Ma-Ma coupling
at torus overlap.  At r ~ λ_C the full internal fields interact,
137× the α-projected Coulomb field.

### Fusion rate
NACRE parametric fit for pp:
N_A⟨σv⟩ = 4.01×10⁻¹⁵ T₉⁻²/³ exp(−3.380/T₉¹/³) × f(T₉)

Enhanced by WKB tunneling ratio for modified barrier.

### Alignment (MaSt-specific)
External B field aligns proton magnetic dipoles, changing the
fraction of collisions with attractive (N-to-S) orientation.
Modeled via Langevin function of μ_N B / kT.

### Stability
Temperature exponent ν = d(ln⟨σv⟩)/d(lnT) ≈ 2/3 + τ/3.
When ν > 4 (exceeds radiative T⁴ loss), thermal runaway is
possible without confinement feedback.

## Related
- Q95: Strong force as internal EM
- Q89: Fusion as mode transition
- Q94: Compton window framework
