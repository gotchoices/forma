# Q22: Does exact path closure matter for the electron properties?

**Status:** Largely answered  
**Source:** User question  
**Related:** [Q18](Q18-deriving-alpha.md), [Q07](Q07-flat-compact-dimensions.md)

**Short answer:** No. All five electron properties (charge, mass, spin,
magnetic moment, g-factor) derive from the (1,2) *topology* and *local*
winding ratio — not from global periodicity. A slowly precessing orbit
preserves them all.

---

## Question

The electron model uses a photon on a (1,2) geodesic on T². For the
winding numbers to be exactly (1,2), the orbit must close exactly after
one major revolution and two minor revolutions. But orbits that are
almost-closed (irrational winding numbers) could also exist.

Does exact closure matter? If the orbit precesses slowly, do the
electron's properties drift?

## Answer

### What each property depends on

| Property | What it depends on | Needs exact closure? |
|----------|--------------------|----------------------|
| Charge q | Integrated field topology (winding class) | No — topology is homotopy-invariant |
| Mass m | Total photon energy (E = mc²) | No — fixed by energy, not path length |
| Spin s | Local winding ratio p/q at any point | No — local geometry |
| Magnetic moment μ | Axial B-field projection integrated over orbit | No — converges over many orbits |
| g-factor | Ratio of angular momenta | No — ratio of local winding rates |

Every observable is either an integral over many orbit cycles (which
converges for any ergodic trajectory that covers the same region) or
a local quantity (which is independent of global closure).

### Topology is not exact closure

The charge is determined by the *homotopy class* of the path — which
winding number sector it belongs to. Two paths that are continuously
deformable into each other (same homotopy class) produce the same charge.
An orbit that precesses slowly stays in the (1,2) homotopy class as long
as it does not slip across a topological boundary, which requires a
discontinuous jump in winding number.

### The precession argument

If the torus axis precesses, the effective orbit in 3D space traces out
a filled solid of revolution rather than a single closed curve. This is
exactly the "volume-filling" picture in WvM's original paper (Fig. 2).
The time-averaged field from a precessing (1,2) orbit approaches the
spherically symmetric Coulomb field. Nothing in this averaging changes
the winding topology.

### Residual subtlety: constructive interference

One assumption embedded in the model is phase matching: the photon's
wave function must be single-valued on the compact space, which requires
the accumulated phase around one (1,2) orbit to be an integer multiple
of 2π. This is a *boundary condition*, not an exact-closure condition.

An irrational-slope geodesic never closes, so it has no well-defined
periodicity condition. In practice the quantization (energy = m_e c²,
winding = (1,2)) selects a specific path that does close — this is
how discrete particle properties emerge from a continuous geometry. The
model implicitly assumes exact closure through this energy quantization.
Whether a slightly irrational orbit is stable or unstable (and whether
it drifts back toward the rational orbit) is an open dynamical question,
but it does not affect the properties of the *exact* (1,2) state.

## Conclusion

Exact path closure is not needed for any of the five measured electron
properties. The properties are stable under slow precession. The one
place where closure enters is the energy quantization condition that
*selects* the (1,2) orbit from among all possible geodesics — this is
a feature, not a fragility.
