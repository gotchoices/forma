# Track 3, Step 1 Findings: Single-node wye-jack alignment

Scripts: `scripts/track3_step1_single_node.py` (coarse),
`scripts/track3_step1_fine.py` (fine resolution)

---

## F1. The magic angles are real — but NOT at 0° alignment

**Surprise result:** at the ⟨111⟩ magic angles, the three
jack edges that project into the wye plane ARE at exactly
120° separation — confirming the analytical prediction.
But the projected jack edges are NOT along the same
directions as the original jack edges.

The projection of a tetrahedral edge onto a face of the
tetrahedron has length √(2/3) ≈ 0.9428 of the original
edge, and the angle between the projected edge and its
original direction is **arccos(√(2/3)) ≈ 19.47°**.

This means: even at the "perfect" magic angle, the best
alignment between a wye edge and a jack edge is **19.47°**,
not 0°.  The wye edge lies in the same plane as the jack
projection, at the same 120° spacing — but the jack edge
itself points OUT of the plane by 19.47°.

**Implication:** a wye edge and a jack edge can never be
perfectly parallel (0° alignment) at the same node.  The
120° vs 109.47° angular mismatch prevents it.  The closest
approach is 19.47° — the angular gap between the planar
120° geometry and the tetrahedral 109.47° geometry.

**The 19.47° angle** is arccos(√(2/3)) = arctan(1/√2).
It appears as the angle between a tetrahedral edge and
its projection onto the opposite face.  It is a fixed
geometric constant of the tetrahedron, not adjustable.


## F2. Single-edge alignments DO exist — but they use different jack edges

The coarse and fine sweeps found orientations where a wye
edge aligns to within 0.5° of a jack edge.  These are NOT
at the ⟨111⟩ magic angles.  They occur at orientations
where the wye plane is tilted so that a wye edge direction
happens to coincide with one of the four jack directions
— not through projection, but by direct alignment.

At θ = 90° (wye plane containing the z-axis), a wye edge
pointing along [0,0,1] aligns perfectly with any jack
edge that has a significant z-component.  The jack
direction (+1,+1,+1)/√3 has z-component 1/√3 — the angle
between [0,0,1] and this direction is 54.74°.  Not close.

But a wye edge can point in ANY direction within its plane.
At the right (θ, φ, ψ), a wye edge can be rotated to
point exactly along a jack direction.  This gives 0°
alignment for that one edge — but the other two wye edges
(at ±120°) will NOT align with any jack edge.

**Result:** single-edge alignment (1 of 3 wye edges
matching 1 of 4 jack edges) exists at specific discrete
orientations.  Multi-edge alignment (2 or 3 edges) was
NOT found at any tolerance ≤ 5° except at the trivial
θ = 90°, Δθ = 90° case.


## F3. Alignment fraction scales as tolerance^1.75

The fraction of orientations with ≥1 aligned edge scales
as a power law in the angular tolerance:

| Tolerance (°) | Fraction | ≈ 1/N |
|---------------|----------|-------|
| 0.10 | 0.000049 | 20,250 |
| 0.25 | 0.000117 | 8,526 |
| 0.50 | 0.000426 | 2,348 |
| 1.00 | 0.001475 | 678 |
| 2.00 | 0.006093 | 164 |
| 3.00 | 0.013370 | 75 |
| 5.00 | 0.037500 | 27 |

Power law fit: fraction ∝ tolerance^1.75.

The fraction crosses 1/137 at **tolerance ≈ 2.2°**.

For a pure area-on-sphere scaling, the expected exponent
would be 2.0 (fraction ∝ solid angle ∝ δ²).  The measured
exponent 1.75 is slightly less than 2 — the alignment
opportunities are somewhat more clustered than uniform
random caps on the sphere.  The frac/tol² ratio stabilizes
at ~0.0015 for tolerances ≥ 0.5°, confirming near-
quadratic scaling at larger tolerances.


## F4. The magic angle alignment gap is exactly 19.47°

At the ⟨111⟩ magic angle (where the projected jack edges
form a perfect 120° pattern in the wye plane):

- All three wye edges are 19.47° from their nearest jack
  edge
- Rotating ψ (twist) at the magic (θ, φ) makes all three
  angles increase together — the minimum is at ψ = 0°
  (wye edges aligned with the projected jack edges)
- Tilting θ away from the magic angle improves one edge
  (toward 0°) while worsening the others (toward 20°+)
- At θ deviation = 35° from magic, one edge reaches its
  minimum (~5.3°) while the others are at ~54°

**The 19.47° gap is the fundamental barrier** between the
2D hexagonal geometry (120° nodes) and the 3D tetrahedral
geometry (109.47° nodes).  No single orientation
simultaneously brings all three wye edges to 0° alignment
with jack edges.  You can bring ONE to 0° (at the cost of
the other two), but not all three.


## F5. No multi-edge alignment exists (outside trivial cases)

Across 2,592,000 orientations tested at 7 tolerances,
**zero cases of 2-edge or 3-edge alignment** were found
at tolerances ≤ 5°.

The only 3-edge "alignment" is the magic angle at 19.47°
— where the projected directions match at 120° but the
actual 3D directions are offset by 19.47°.

This means: the coupling staircase (from the T3 framing)
has effectively only two populated levels:
- Level 0: zero edges aligned (generic angles)
- Level 1: one edge aligned (at specific discrete angles)
- Levels 2-6: empty (the angular mismatch prevents
  multiple simultaneous alignments below ~19°)


## F6. Assessment

**The single-node analysis reveals a fundamental geometric
barrier:** the 120° vs 109.47° mismatch means that a 2D
wye edge and a 3D jack edge at the same node are always
at least 19.47° misaligned if you want all three wye edges
to be in the ⟨111⟩ face plane — or you can bring ONE edge
to 0° alignment by sacrificing the other two.

**What 1/137 means at this level:** the fraction of
orientations where at least one edge aligns to within
~2.2° is 1/137.  This is the "natural tolerance" at which
the single-edge alignment probability equals α.  But 2.2°
is not derived from the lattice — it's a free parameter
(the tolerance chosen).

**What's needed for a derivation of α:** a mechanism that
SETS the tolerance at 2.2° from the lattice geometry
itself — not chosen by hand.  Possible sources:
- The lattice's own angular resolution (related to ζ = 1/4?)
- The thermal/quantum angular uncertainty at the Planck scale
- The dwell angle of the torus normal as it sweeps through
  the coupling region (set by ε)

**Or:** the approach may need to change entirely.  The
single-node analysis shows that perfect alignment doesn't
exist (19.47° barrier).  The extended lattice (Step 2)
might reveal that NEAR-alignments at distant nodes
constructively interfere to produce coupling — not from
a single perfect edge match, but from many imperfect ones
adding coherently.  This would be a different mechanism
from what T3 originally envisioned.


## F7. Status of Track 3

Step 1 is complete.  Key findings:
1. The 19.47° barrier prevents multi-edge alignment
2. Single-edge alignment exists at discrete orientations
3. The alignment fraction = 1/137 at tolerance ~2.2°
4. The tolerance is a free parameter, not derived

**Step 2 (extended lattice) is still viable** — the
question shifts from "do single edges align?" to "do
near-alignments across many nodes produce coherent
coupling?"  This is a constructive interference question,
not a coincidence-counting question.

**The user's next hypothesis** (mentioned before this
computation) may provide additional direction.
