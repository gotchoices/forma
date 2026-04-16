# Track 10: Propagation leakage

**Status:** Complete.  See [F10-propagation-leakage.md](F10-propagation-leakage.md).

**Premise:** inject a unit-amplitude signal at one edge of
a hexagonal lattice on a torus.  At each Y-junction, decompose
the incoming signal into three channels: two outgoing edges
and the surface normal.  Propagate the edge signals to the
next nodes and repeat.  Track the cumulative normal leakage
as the signal traverses the full torus.

**Key distinction from Track 9:**

| Track 9 | Track 10 |
|---------|----------|
| Single-node, single-step | Multi-node iterative propagation |
| No signal propagation | Signal hops from junction to junction |
| Independent per-node escape | Signal weakens as it leaks |
| Sums independent per-node values | Tracks coherent propagation with branching |

---

## Physical picture

A pulse enters the 2D lattice sheet.  At the first junction,
the pulse splits into two outgoing edges and a small normal
escape.  Each outgoing branch reaches the next junction,
splits again, leaks again.  After N steps, the signal has
traversed one full cycle around the torus, leaving behind
a trail of normal leakage at each junction.

The key question: what fraction of the input energy has
accumulated in normal components after a full circuit?

---

## The decomposition

### Frame 1 (input): one dimension
The incoming signal has scalar amplitude A on one edge.
The edge has a 3D unit direction ê_in.  The signal vector
is v = A × ê_in.

### Frame 2 (output): three dimensions
At the junction, three output channels:
- ê_a, ê_b: unit directions of the two outgoing edges
- n̂: unit surface normal at the node

Solve the 3×3 system:

    [ê_a | ê_b | n̂] · [a, b, n]ᵀ = v

This gives unique coefficients (a, b, n) that exactly
reconstruct the input vector.

### Energy accounting

On a flat sheet (edges at 120°), a = b = 1 and n = 0.
The sum a² + b² = 2 > 1, but the cross term
2ab cos(120°) = -1 restores |v|² = 1.  The individual
coefficients are NOT independent energy fractions.

To track energy correctly, we implement three methods:

**Method A — Raw decomposition:**
Propagate a and b directly.  Track energy diagnostics.
Amplitudes may grow (non-physical) but the normal
fraction is well-defined at each step.

**Method B — Energy-conserving normalization:**
After decomposition, rescale (a, b, n) so that
a² + b² + n² = A².  This forces energy conservation
at each step.

**Method C — S-matrix with direction tracking:**
Use the Y-junction S-matrix (transmitted = 2/3 each,
reflected = -1/3) for scalar amplitudes.  Track the
effective signal direction = amplitude × edge direction.
The normal component of this direction is the leakage.
This is the most physically grounded approach.

---

## Algorithm

1. Build honeycomb torus with N₁ × N₂ cells
2. Choose a starting edge and set amplitude = 1
3. At each timestep:
   a. For each active edge (j→i) with amplitude A:
      - Compute incoming vector v = A × ê_{j→i}
      - Find the two outgoing edges at node i (not back to j)
      - Solve the 3×3 system for (a, b, n)
      - Record normal leakage n
      - Create new active edges with amplitudes a, b
   b. Sum amplitudes from multiple paths arriving at same edge
   c. Record diagnostics: total in-plane energy, normal energy
4. Run for K_max steps (at least N₁ to complete one tube circuit)
5. Report: cumulative normal leakage / input energy

### Sweeps

| Parameter | Range | Purpose |
|-----------|-------|---------|
| N | 4, 6, 8, 10, 20 | Resolution dependence |
| ε = a/R | 0.3, 0.5, 0.7 | Curvature dependence |
| K_max | 2N to 4N steps | Convergence of leakage |
| Method | A, B, C | Sensitivity to normalization |

---

## Dependencies

numpy, matplotlib

---

## Files (planned)

| File | Purpose |
|------|---------|
| T10-propagation-leakage.md | This framing document |
| scripts/track10_propagation_leakage.py | Main computation |
| F10-propagation-leakage.md | Findings |
| output/track10_*.png | Visualizations |
