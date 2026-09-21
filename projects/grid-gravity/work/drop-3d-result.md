# 3D drop — a body falls toward a source as 1/r²

**Status:** Simulation result; a direct check added to the mechanism 3
validation plan ([STATUS.md](STATUS.md), item 5g). Steps 2–3 showed how a body
responds to a gradient of the deflection (in one extended dimension); step 4
showed that a source builds a 1/r deflection in three. The inverse-square force
followed by putting the two together. This run does it in one piece: three
extended dimensions, the 1/r deflection of a point source, a massive body
released at rest at several distances.

Script: [`../scripts/drop_3d.py`](../scripts/drop_3d.py).
Figure: [`../outputs/drop_3d.png`](../outputs/drop_3d.png).

Grades: **[rigorous]** (the prediction), **[simulated]**, **[assessment]**.

---

## 1. Why the falloff is there at all

A steady tension arriving at a node is divided among the node's other edges by
the same scatter that handles everything else, and nothing is lost. So the total
crossing any closed shell around the source is fixed, while the number of edges
crossing the shell grows as r². Each edge therefore carries 1/r² of it; the
deflection — the running sum held at each node — falls as 1/r. Step 4 measured
both ([switch-on-result.md](switch-on-result.md)). In one extended dimension a
node has one edge in and one out, nothing is shared, and the pull is constant —
which is why the closed-loop run of step 5c, done in one dimension, showed no
falloff. That is geometry, not the mechanism.

## 2. Setup and prediction [rigorous]

Canonical scatter on a cubic lattice with a compact direction (carried exactly by
its Bloch phase) and a node store at every node. The deflection of a fixed point
source is imposed, q = A/r with A = 0.3 (softened inside r = 2), with the
linear-delay rule 1 + q/2 per member. Node stores only: link stores change the
light-bending coefficient, not the power law.

A packet in the compact n = 1 mode — a massive body, rest frequency ω₀ = 0.385,
width 7 nodes — is built from exact eigenvectors and released at rest at distance
r₀. Its energy centroid is tracked for 160 ticks, with a zero-field control run
subtracted (the packet construction leaves a tiny field-independent drift,
3×10⁻³ nodes, that would otherwise be 2% of the smallest fall).

Predictions, from the closed-form spectrum of
[uniform-q-theorem.md](uniform-q-theorem.md):

- weak field, low frequency: a = (c₀²/2)·A/r², with c₀² = 1/4 on this lattice;
- exact lattice: the same times 1/cos²(ω₀/2) = 1.038 for this packet's rest
  frequency (the lattice-scale departure from universality found in step 2), and
  times the momentum-spread factor 0.9835;
- full trajectory: Hamilton's ray equations for the exact local spectrum,
  integrated in three dimensions.

## 3. Result [simulated]

| r₀ | direction | fell (sim) | fell (ray) | a (sim) / a (ray) | a·r₀² |
|---|---|---|---|---|---|
| 24 | axis | 0.8151 | 0.8355 | 0.975 | 0.03640 |
| 32 | axis | 0.4749 | 0.4712 | 0.996 | 0.03743 |
| 40 | axis | 0.3058 | 0.3024 | 0.998 | 0.03765 |
| 48 | axis | 0.2128 | 0.2104 | 0.998 | 0.03777 |
| 64 | axis | 0.1200 | 0.1187 | 0.999 | 0.03790 |
| 40 | body diagonal | 0.3048 | 0.3024 | 0.997 | 0.03763 |

- **Inverse square.** The measured acceleration falls as **r^−1.96** over
  r = 24 – 64, and as r^−1.98 from 32 to 64. a·r² levels off at 0.0379, against
  0.0383 predicted for this packet.
- **The ray law holds in three dimensions** to 0.2 – 0.4% for r ≥ 32.
- **Isotropic.** A release on the body diagonal gives the same acceleration as
  one on an axis (0.997 against 0.998), and a body released on the diagonal moves
  exactly along it (sideways motion 10⁻¹⁵).
- **Where it departs, and why.** At r₀ = 24 the body's width (7 nodes, growing to
  about 12 during the run) is half its distance from the source, the field
  varies strongly across it, and the point-body ray law overestimates the fall
  by 2.5%. At r₀ = 16 the body is as wide as its distance and the overestimate is
  25%. These are extended-body effects, not departures from the force law; they
  are the reason the fitted exponent is −1.96 rather than −2.

## 4. What this adds [assessment]

The inverse-square law for a body is now shown directly on the lattice, in three
dimensions, rather than inferred by combining a 1D response with a 3D field. The
field here was imposed (step 4 is what shows a source produces it), and the body
is a slowly spreading packet rather than a bound particle — a bound, localized
3D particle remains grid-matter's open problem, not this project's.

## Grades summary

- **[rigorous]** The weak-field law and its exact-lattice correction.
- **[simulated]** a ∝ r^−1.96 (r^−1.98 beyond r = 32); agreement with the 3D ray
  equations to 0.2 – 0.4%; isotropy; the extended-body departures at small r.
