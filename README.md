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

See [`qa/Q27-foundational-axioms.md`](qa/Q27-foundational-axioms.md) and
[`qa/Q32-energy-geometry-fundamentals.md`](qa/Q32-energy-geometry-fundamentals.md)
for discussion.

## Foundation

The starting point is a 1997 paper by Williamson and van der
Mark ([PDF][wvm]) proposing that an electron is a single photon
confined to a (1,2) torus knot.  The model reproduces spin ½
(exact, topological) and charge ≈ 0.91e (approximate, geometric).

This project extends the WvM model into a compact-dimension
framework: the photon lives on a flat torus T² (two periodic
dimensions), and the electron's properties emerge from the
geometry of that surface.

See [`primers/charge-from-energy.md`](primers/charge-from-energy.md) for
the conceptual framework and [`STATUS.md`](STATUS.md) for results,
active work, and open problems.

[wvm]: https://fondationlouisdebroglie.org/AFLB-222/MARK.TEX2.pdf

## Structure

- `reference/` — Source material by others and recorded conversations.
- `primers/` — Self-contained tutorials on topics needed to follow the studies.
  See [`primers/README.md`](primers/README.md) for the list (matrix notation, Maxwell, KK theory, charge-from-energy).
- `papers/` — Authored documents presenting theories, results, and proofs. *(None yet.)*
- `qa/` — Physics questions answered by logic and existing theory (no computation).
  See [`qa/README.md`](qa/README.md) for the index.
- `studies/` — Questions that require a computational model to answer.
  See [`studies/README.md`](studies/README.md) for workflow and conventions.
- `viz/` — Interactive browser-based visualizations. See [`viz/index.html`](viz/index.html).

## Navigation

| File | Purpose |
|------|---------|
| [`STATUS.md`](STATUS.md) | Where we are: objectives, results, active front, open problems |
| [`studies/STATUS.md`](studies/STATUS.md) | Study-by-study registry: active, backlog, done |
| [`qa/README.md`](qa/README.md) | Index of answered and open physics questions |
| [`qa/INBOX.md`](qa/INBOX.md) | Capture queue for new questions |
| [`primers/README.md`](primers/README.md) | Four tutorials: matrix notation, Maxwell, KK theory, charge-from-energy |
| [`reference/WvM-summary.md`](reference/WvM-summary.md) | Living summary of the foundational WvM paper |
| [`viz/index.html`](viz/index.html) | Browser launcher for all interactive visualizations |
