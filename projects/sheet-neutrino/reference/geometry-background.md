# Geometry background

The mathematical ideas used to compare candidate hosts. Each section introduces its terms before using them.

## 1. Embedding

An **embedding** is a map from one space M into a larger space N that:
1. **is one-to-one:** two points of M never land on the same point of N, so the image never crosses itself;
2. **is smooth, with a nonzero derivative everywhere:** no corners or cusps. A map that meets 1 and 2 locally is an **immersion**;
3. **preserves nearness:** points close in the image came from points close in M. A figure-6 fails this, because the tail tip touches the loop.

A line embedded in a plane is a curve t ↦ (x(t), y(t)). The simplest case, t ↦ (t, 0), is the x-axis. There the plane splits cleanly into "along the line" × "across it," and the new direction really is independent of the line. In general, the curve bends, and the across-direction (the **normal**) changes from point to point. The number of extra dimensions, here 2 − 1 = 1, is the **codimension**.

## 2. Intrinsic and extrinsic properties

- **Intrinsic** properties can be measured from inside the space, by something living on it. For a curve, the only intrinsic property is its length.
- **Extrinsic** properties exist only because of the embedding. For a curve, the main one is **curvature** κ, the rate at which it turns in the plane.

An observer confined to a 1D curve cannot detect its curvature: a straight segment and an arc of the same length feel identical from inside.

Surfaces are richer. A sphere has **Gaussian curvature**, an intrinsic curvature that observers on it can detect, for example because triangle angles sum to more than 180°. A cylinder has none: it can be unrolled flat. Both look curved in 3D, but only the sphere is intrinsically curved. Gauss's *Theorema Egregium* (1827) established that Gaussian curvature is intrinsic. Riemann then defined geometry entirely from inside, with no surrounding space. General relativity uses that approach.

**Geodesic curvature** κ_g is the surface analog of a plane curve's curvature: how much a curve drawn on a surface bends *within* the surface. A **geodesic**, the straightest possible path on the surface, has κ_g = 0. Hypothesis G1 in [metric-charge Ch 11 §6](../../metric-charge/11-modeling-foundation.md) ties local charge density to κ_g.

## 3. Periodicity does not need an extra dimension

A **circle** is defined intrinsically as S¹ = ℝ/Lℤ: the real line with t and t + L declared to be the same point. On a lattice, a ring of n cells is a chain plus one rule: the neighbor of cell n−1 is cell 0. Both are statements about connectivity, not shape.

*Signals analogy:* a circular buffer. The index wraps as i mod n, and the layout of the memory chips plays no role.

A circle cannot be embedded in a line, so a 2D picture is needed to *draw* one. That is a limitation of flat drawing space, not a property of the circle.

### How a periodic dimension is perceived from inside

Perception is local: every observation arrives as a signal that traveled *within* the space. Locally, a periodic dimension looks exactly like an infinite one. There is no seam. The periodicity is a **global** fact, detected by **global** experiments:

1. **Return:** travel in one direction and arrive back at the start, as Magellan's circumnavigation did.
2. **Repeated images:** light travels around the closed direction, producing copies spaced L apart. Cosmologists have searched the cosmic microwave background for matched "circles in the sky" as a test of whether the universe is compact.
3. **Discrete modes:** only waves fitting a whole number of times survive, so wavenumbers form a comb k = 2πm/L.

*Signals analogy:* a pulse on a closed delay-line loop returns every L/v, and the spectrum is a comb with spacing v/L. Neither depends on how the cable is coiled.

**A flat torus**, such as the wrap-around screen of the video game Asteroids, is intrinsically flat: triangle angles sum to 180°. A donut drawn in 3D is curved, and a flat torus cannot be built smoothly in 3D at all. Adding an embedding to "explain" a wrap can give the space geometry it does not have.

In the Kaluza–Klein tradition and in MaSt, a compact dimension too small to see is perceived as a **quantized property**. Momentum around the loop takes only comb values and appears in ordinary space as mass (and, with winding, charge).

## 4. Closed curves in the plane: turning number

The **total signed curvature** of a closed curve is ∮ κ ds, with left turns positive and right turns negative.

- **Hopf's turning theorem (Umlaufsatz):** for any closed plane curve that does not cross itself, the total is exactly ±2π. The sign is the traversal direction. However the curve wiggles, its concave and convex parts net to exactly one full turn.
- If crossings are allowed (an immersion), the total is 2π·w for an integer **turning number** w. A figure-8 has w = 0. The **Whitney–Graustein theorem** says w is the only property that distinguishes closed plane curves under smooth deformation.
- By the Jordan–Schoenflies theorem, every non-crossing closed plane curve can be deformed into a round circle. Genuinely different shape classes, such as knots, first appear in 3D.

**Pattern:** local curvature is free and fractional, but the closed total is an integer. The same pattern, through the Gauss–Bonnet theorem, underlies per-arc fractional charge in [sheet-proton](../../sheet-proton/README.md).

**Consequence:** a static closed cross-section cannot be neutral by balancing concave and convex parts, because its total is always 2π. In sheet-proton, the neutron's neutrality comes from the cross-section *changing* around the ring, not from the cross-section's shape alone.

**Dimensions versus parameters.** The clover cross-section z(t) = R·e^{it}[1 + a₁cos3t + a₂cos6t + i(b₁sin3t + b₂sin6t)] is intrinsically 1D and lives in a 2D plane, just as a circle does. It needs more **shape parameters** than a circle (about 5 instead of 1), not more dimensions.

## 5. Surfaces from a square: torus, Klein bottle, RP²

Glue the opposite edges of a flat square in pairs:

| Gluing | Result | Euler characteristic χ |
|---|---|---|
| Both pairs straight | Torus | 0 |
| One pair straight, one flipped | Klein bottle | 0 |
| Both pairs flipped | Real projective plane RP² | 1 |

Gluing one pair with a flip gives a Möbius strip. Closing the other pair straight then gives the Klein bottle.

The **Gauss–Bonnet theorem** says ∫ K dA = 2πχ: the total Gaussian curvature is fixed by topology. With χ = 0, the torus and the Klein bottle can both be perfectly **flat**. RP² cannot.

### The Klein bottle

Intrinsically, the flat Klein bottle is the plane with the identification **(x, y) ~ (x + L_ring, −y)** plus periodicity in y. Going once around the ring mirrors the tube direction.

- It is **non-orientable:** there is no consistent global handedness.
- It **cannot be embedded in 3D**; it can be in 4D. Every 3D picture is an immersion that crosses itself.
- **Two common drawings** show the same surface:
  - *Bottle:* the neck passes through the wall.
  - *Figure-8 "bagel":* a figure-8 cross-section, rotated 180° as it goes around the ring. Its two lobes are the two halves of **one** tube circle, and the 180° rotation swaps them every lap. The waist line where the drawing crosses itself is two separate circles (y = 0 and y = L_tube/2) drawn on top of each other; intrinsically they never touch.
  - Neither drawing is flat. The flat Klein bottle exists only intrinsically.
- **Double cover:** unrolled over two ring laps, the Klein bottle becomes an ordinary torus with ring length 2L_ring. A path parallel to the ring closes only after two laps, passing once through each "lobe." The two waist circles are the exceptions; they close in one lap.

### Modes on the flat Klein bottle

Write a mode as e^{ikx}·g(y). The identification requires f(x + L_ring, −y) = f(x, y). Splitting g into even and odd parts:

| Tube profile | Ring condition | Ring wavenumber k |
|---|---|---|
| Even, cos(qy) | returns unchanged after one lap | 2πm/L_ring (integer m) |
| Odd, sin(qy) | returns **inverted** after one lap | 2π(m + ½)/L_ring (half-integer) |

- Every mode with tube structure is a **standing wave** in the tube direction: an equal mix of clockwise and counterclockwise circulation. Net tube winding is exactly zero. [R48 F5](../../../studies/R48-helicity-charge/findings.md) identifies standing waves as carrying zero charge under the winding rule.
- Charge conjugation (flipping the sign of the tube winding) is built into the space, so every mode is its own conjugate. This is a natural Majorana realization.
- Shear along the flipped direction can be removed by shifting coordinates, so it has no physical effect.
- Because the space has no global handedness, its compatibility with the neutrino's definite helicity needs checking.

## 6. Twisted and antiperiodic closure

A field on a loop can close with a phase: **ψ(x + L) = e^{2πiδ}·ψ(x)**.

- δ = 0: **periodic**. Wavenumbers k = 2πn/L.
- δ = ½: **antiperiodic**, ψ(x + L) = −ψ(x). Wavenumbers k = 2π(n + ½)/L.
- General δ: wavenumbers k = 2π(n + δ)/L. The two circulation senses ±n are no longer degenerate: |n + δ| ≠ |−n + δ|. In physics this is the effect of a magnetic flux threading a ring (the Aharonov–Bohm effect, in which a charged particle's phase depends on enclosed flux even where the field is zero).

*Signals analogy:* a **ring oscillator**, an odd number of inverters in a loop. A signal returns inverted after one trip and restored after two. This is the antiperiodic case, and it matches the defining behavior of spin ½: a sign change after 360°, restored after 720°.

The twist lives in the **values of the field** (a phase or a sign), not in any surrounding space. A 1D line stays intrinsically 1D. Mathematically, the field is a section of a nontrivial **line bundle** over the circle; for δ = ½ it is the Möbius bundle.

**Open gap:** a sign change on going around an *internal* loop is not by itself spin ½ under rotations of *ordinary* space. A host using this route must show why a 360° rotation in space corresponds to one internal circuit.

## 7. A sheared torus is a stack of twisted rings

On a sheared torus, going once around one direction shifts the coordinate of the other direction by a fraction s of its length. As a result, a mode with winding number n in the first direction sees the second direction close with twist δ = n·s. (Which direction plays which role depends on convention; the R49/R61 mass formula offsets n_t by n_r·s.) Within each fixed-n sector, the second direction is a 1D twisted ring of §6. This is why the 2D torus spectrum can be read sector by sector as 1D twisted rings; see [work/host-candidates.md §2](../work/host-candidates.md).
