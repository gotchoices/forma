# Theory of the Universe

## Goal

Build a geometric model of fundamental particles from pure
electromagnetic energy — no fundamental charges, no point
particles.

**Near-term:** Find a set of compact-dimension parameters
(topology, aspect ratio, scale) that reproduces all measured
properties of the electron: charge, mass, spin, and magnetic
moment.

**Medium-term:** Extend the framework to the proton and neutron
(and the quarks that compose them).

**Long-term:** Determine whether forces and particles can emerge
entirely from the geometry of dimensions — periodic, compact,
and interacting — with no inputs beyond energy and topology.

## Guiding principle

**Energy and geometry are the only fundamentals.**

Mass, charge, spin, and magnetic moment are all emergent:

| Property  | Emerges from                          |
|-----------|---------------------------------------|
| Mass      | Energy confined in periodic geometry  |
| Charge    | Field winding number on compact T²    |
| Spin      | Winding ratio of geodesic (p:q)       |
| Mag. mom. | Geometric projection of compact field |

Conservation laws are emergent too — but exact.  Mass
conservation is energy conservation.  Charge conservation
is topological winding-number conservation (you can't
smoothly unwrap a path on T²).  Spin conservation is
geodesic topology.  These are exact because topology is
exact.

The only true inputs are: (1) the existence of energy
(photons), (2) the existence and shape of compact
dimensions, and (3) the rules of propagation (Maxwell's
equations).  Everything else — the particle zoo, their
properties, their interactions — should follow.

See [`studies/QUESTIONS.md`](studies/QUESTIONS.md) Q27, Q32
for discussion.

## Foundation

The starting point is a 1997 paper by Williamson and van der
Mark ([PDF][wvm]) proposing that an electron is a single photon
confined to a (1,2) torus knot.  The model reproduces spin ½
(exact, topological) and charge ≈ 0.91e (approximate, geometric).

This project extends the WvM model into a compact-dimension
framework: the photon lives on a flat torus T² (two periodic
dimensions), and the electron's properties emerge from the
geometry of that surface.  Key results so far:

- Charge e arises from the EM field configuration on T²,
  projected into 3+1D.  Charge is emergent, not fundamental.
- Mass m_e comes from the resonance condition (path length = λ_C).
  Mass is confined photon energy.
- Spin ½ is topological (the (1,2) winding number).
- The magnetic moment comes from B's net axial projection on the
  torus.
- The fine-structure constant α is a geometric ratio of the
  compact space, not an independent coupling constant.

See [`ref/charge-from-energy.md`](ref/charge-from-energy.md) for
the conceptual framework and [`studies/STATUS.md`](studies/STATUS.md)
for the current state of work.

[wvm]: https://fondationlouisdebroglie.org/AFLB-222/MARK.TEX2.pdf

## Structure

- `ref/` — Reference material, primers, and the WvM paper.
- `studies/` — Individual studies, each in its own folder.
  See [`studies/README.md`](studies/README.md) for workflow and
  conventions.
