# Track 7: The ε → 0 limit — do exact coincidences exist?

**Status:** Complete

---

## Motivation

Tracks 1, 3, and 6.0 all measured "coincidence rates" — how
often nodes or edges from a 2D hexagonal lattice land near
nodes or edges of a 3D/4D ambient lattice.  In every case,
the rate depended on a **tolerance parameter** ε (or δ, or
tol_deg) that defines "near."  The value 1/137 appeared at
specific tolerances:

| Track | Quantity | ε at which 1/frac ≈ 137 |
|:---:|:---|:---:|
| 1 | Edge coincidence (2D-in-2D) | ε ≈ 0.005 |
| 3 | Angular alignment (wye-jack) | tol ≈ 2.2° |
| 6.0 | Node coincidence (2D-in-4D) | δ ≈ 0.167 |

These are three different tolerances for three different
geometric quantities.  The question Track 7 asks is:

> **If we send the tolerance to zero, does any coincidence
> rate converge to a nonzero value?**

If yes: there are exact coincidences, and their density could
be a geometric constant (possibly α).

If no: the lattices are incommensurate, zero nodes/edges
coincide exactly, and every previous "1/137" result was an
artifact of the chosen tolerance.

---

## Method

Script: `scripts/verify_epsilon_to_zero.py`

Three tests, all using ε values pushed far below the ranges
explored in earlier tracks:

### Test 1: Edge coincidence (Track 1 setup)

Two 80×80 triangular lattices (edge length 1) in the same
plane, rotated by 13.2°.  Count pairs of nodes (one from
each lattice) separated by distance 1 ± ε.  Normalize by
coordination number 6.

Tolerance range: ε = 0.2 down to 0.0001.

### Test 2: Node coincidence (Track 1 setup)

Same lattice pair.  Count how many nodes from lattice A
fall within ε of any node in lattice B.

Tolerance range: ε = 0.2 down to 0.0001.

### Test 3: Angular alignment (Track 3 setup)

A hexagonal wye (3 edges at 120°) and a tetrahedral jack
(4 edges at 109.47°) at the same origin.  Sweep all
orientations (θ, φ, ψ) on a 45×90×30 grid.  Count the
fraction of orientations where at least one wye edge is
within tol° of a jack edge.

Tolerance range: 5.0° down to 0.05°.

---

## What this tests

The key distinction: earlier tracks used a *fixed* tolerance
and varied orientation (angle, plane, etc.).  Track 7 fixes
the geometry and varies the tolerance, pushing it toward zero.

This directly tests whether any coincidences are **exact**
(surviving at ε = 0) or merely **approximate** (requiring a
nonzero tolerance window to appear at all).

If all coincidences are approximate, then the "coincidence
rate" is not a geometric constant — it is an arbitrary
function of ε, and any target value (including 1/137) can be
obtained by choosing the right ε.
