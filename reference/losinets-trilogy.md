# Losinets trilogy — notes and connection to MaSt/GRID

Three papers by Losinets form a coherent program: a continuum-mechanical substrate (Kelvin–Voigt medium), a free-photon model as a vortex ring in that substrate, and a baryon / compound-particle model built from the same vortex primitives. Read together, they map onto MaSt and GRID at three different layers of the same architecture.

Source PDFs (not committed; kept in `tmp/`):

- `losinets_EfD.pdf` — the Maxwell / elastic-from-dynamics paper. Substrate.
- `losinets_photon.pdf` — free photon as a vortex ring. What gets confined.
- `losinets_baryon.pdf` — baryons and compound particles as vortex assemblies.

## Layer map

| Layer | Losinets | GRID | MaSt |
|---|---|---|---|
| Substrate | Continuum K–V vacuum with effective mass density and dissipation | Discrete Planck lattice with impedance η₀ | Assumed smooth 5-manifold M⁴ × Ma |
| Free photon | Vortex ring, Γ = h/m_vac, ρ(ω) = √(ℏ/(m_vac·ω)) | Lattice excitation with η₀, α-set coupling | Primitive — "a photon" |
| Confined photon | (not addressed) | (not addressed) | Photon wrapped on Ma torus knot |
| Compound particles | Multi-ring vortex assemblies | (not addressed) | Multi-winding modes on Ma_e, Ma_p, Ma_ν |

The three frameworks are not competitors — they cover different slices. Losinets gives the mechanical substrate and the free-photon geometry that MaSt treats as a primitive. GRID gives the discrete lattice underneath the continuum. MaSt gives the compactification geometry that turns continuous polarization into discrete winding.

## Free photon → confined photon: the polarization-to-winding map

Losinets parameterizes a free photon ring by two angles (a, b) on the Poincaré sphere, with continuous values allowed. Confinement on Ma forces those angles to close — only discrete wraps survive. The correspondence:

| Free photon (Losinets) | Confined photon (MaSt) |
|---|---|
| Continuous polar angle b | Discrete tube winding n_tube |
| Continuous azimuth a | Discrete ring winding n_ring |
| b = 0 or π (circular) | Odd tube winding → spin ½ |
| b = π/2 (linear) | Even tube winding → spin 0 |
| Γ = h/m_vac (one quantum) | n_tube = ±1 (one winding) |

WvM's (1,2) electron, in Losinets language: a vortex ring with intrinsic Γ providing the "1" (odd tube winding → spin ½), wrapped twice around the ring direction of Ma_e providing the "2" (even ring winding, no extra spin). Charge ±e emerges from the unit tube winding detected as net topological flux against the GRID lattice.

## What MaSt may fix for Losinets

Losinets' m_vac (effective vacuum mass density scale) is explicitly undetermined in his framework — he flags it as an open problem. MaSt has specific confinement scales (L₁…L₆). If the confined mode radius equals the free-ring radius ρ(ω) at the particle's natural frequency, MaSt's scales pin m_vac.

Rough back-of-envelope using the electron:
- ω_e = m_e c² / ℏ ≈ 7.8 × 10²⁰ rad/s
- MaSt's L₂ (e-sheet ring) = 11.9 fm → ρ = L₂/(2π) ≈ 1.9 fm
- m_vac = ℏ / (ω · ρ²) ≈ 3 × 10⁻²⁵ kg ≈ 200 GeV/c²

That lands near the electroweak scale. Worth a careful derivation — the mapping between "free ring radius" and "confinement scale" needs to respect the wrapping, and the ω to use for a confined mode is not obvious. But if the number survives scrutiny at the right order of magnitude, m_vac is no longer a free parameter.

## What Losinets may fix for MaSt

**Near-field Ez prediction.** Losinets predicts a free photon has non-zero longitudinal field in the near zone for tilted polarization (b ≠ 0), scaling as sin²(b), confined to Δr ≲ r₀. For MaSt confined modes this should generalize:

- Neutrino (circular analog, b = 0): no near-field Ez. ✓ (compatible with neutrality)
- Charged scalar/spin-0 (linear analog, b = π/2): maximum near-field Ez. Measurable on charged pions at sub-Compton distances.
- Proton (compound mode): complex near-field with multiple Ez harmonics, connecting to form-factor structure.

**Mass–frequency derivation.** MaSt's white-paper intuition "m = hf/c² for the confined-photon circulation frequency" is a verbal statement of Losinets' mechanical derivation E_n = nℏω from Γ_n = nh/m_vac. Losinets supplies the mechanics MaSt asserted.

**g-factor recomputation caveat.** Earlier notes suggested μ ∝ Γ² from the baryon paper could fix MaSt's Q114 g_bare problem. Reading the photon paper constrains this: for an elementary ring Γ = h/m_vac is fixed at one quantum, so μ variation comes from r₀ and ρ, not from Γ. For composite particles with multiple wraps the combination rule needs care — Σ Γᵢ² vs (Σ Γᵢ)² is a derivation to do, not assume.

## Open questions this trilogy surfaces

1. Does MaSt's confinement geometry fix Losinets' m_vac? Careful derivation replacing the back-of-envelope above.
2. Does Losinets' charge formula Q = ρ₀ r₀ Γ in SI match GRID's e = √(4πα)? The ratio should be α-related.
3. Does each MaSt particle mode have a predicted near-field Ez structure, and does it match observed multipole moments?
4. Can the proton's Hofstadter two-scale structure (r_m / r_c ≈ 5.2) be derived from the compound-mode projection of model-E to 3D charge density?

Question 3 is the strongest cross-check: if MaSt particle modes have predicted longitudinal near-field structures matching observed multipoles, that's a quantitative agreement between three frameworks at once.

## Relation to existing project docs

- `reference/WvM-summary.md` — WvM's (1,2) knot is the discretized electron mode; Losinets gives the continuous primitive that gets discretized.
- `qa/Q26-hadrons-photon-knots.md`, `qa/Q114` (g-factor) — the confined-mode magnetic moment needs the combination rule referenced above.
- `grid/foundations.md`, `primers/alpha-in-grid.md` — the GRID layer sits below Losinets' continuum; α should emerge as an impedance ratio between K–V bulk (set by m_vac) and compact-Ma topology.
- `papers/little-balls.md`, `papers/universe-as-mode.md` — the "what is a particle" thread Losinets makes mechanically concrete.
