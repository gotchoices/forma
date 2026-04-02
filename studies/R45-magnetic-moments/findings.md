# R45 Findings

## Track 1: Proton moment from geodesic tilting — misguided

Script: `scripts/track1_proton_moment.py`


### F1. The geodesic tilting premise is wrong

Track 1 modeled the proton as a classical charge orbiting on the
torus and asked how cross-shear redistributes its velocity between
sheets.  This is the wrong picture.

The proton is a standing wave ψ = exp(i(n₅θ₅ + n₆θ₆)) on the
torus.  The charge density |ψ|² is uniform — nothing is "moving."
There is no classical velocity, no orbiting charge, no current
loop.  The formula μ = evR/2 does not apply.

The magnetic moment of a wave mode comes from its angular momentum:

    L̂ᵢ = −iℏ ∂/∂θᵢ
    ⟨L₆⟩ = ℏn₆ = 2ℏ

    μ = (e/2m_p) × ℏn₆ = 2μ_N  →  g = 4

This depends on the winding number n₆ — a topological integer —
not on the metric, the cross-shear, or any velocity.  σ_ep cannot
change n₆ from 2 to something else.  The geodesic tilting mechanism
is dead.


### F2. What this means for the remaining tracks

**Tracks 2 and 4 are dead** — they use the same geodesic tilting
premise.

**Track 3 (self-consistent dressed particles) survives.**  The
dressed proton is a composite: the bare (0,0,0,0,1,2) mode plus
cross-sheet excitations with their own winding numbers.  The total
angular momentum of the composite is the sum of all component
winding numbers weighted by their amplitudes — and that sum need
not be an integer.  This is a different physics from tilting the
geodesic of a single mode.

| Track | Status | Notes |
|-------|--------|-------|
| 1. Proton geodesic tilting | **DEAD** | Wrong premise |
| 2. Neutron moment | **DEAD** | Same premise |
| 3. Self-consistent multi-sheet | **Viable** | Different physics |
| 4. Electron moment | **DEAD** | Same premise |
| 5. Dark modes / DIS | Unchanged | |
| 6. Three-mode proton | Unchanged | |
