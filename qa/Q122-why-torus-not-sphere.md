# Q122. Why torus, not sphere?

**Status:** Answered — sphere structurally unsuitable
**Related:**
  [Q07](Q07-flat-compact-dimensions.md) (flat compact dimensions),
  [Q13](Q13-three-compact-dimensions.md) (three compact dimensions),
  [Q50](Q50-shared-material-space.md) (shared material space),
  [Q51](Q51-non-torus-embeddings.md) (non-torus embeddings)

---

## 1. The question

MaSt takes the compact material dimensions to be tori —
specifically, three 2-tori forming T⁶ = T²_e × T²_ν × T²_p.
Why tori in particular?  The 2-sphere S² is simpler, has
rotational symmetry built in, and embeds cleanly in 3D
without self-intersection.  What goes wrong if we use
spheres (or ellipsoids) instead?

## 2. The core problem: topology

The MaSt framework is built on **winding numbers**.  Every
particle is labeled by six integers (n_φe, n_θe, n_φν, n_θν,
n_φp, n_θp), the number of times its wave wraps around each
compact axis.  These are not measurements of some continuous
field — they are **topological invariants**.  On a closed
loop, you cannot continuously change a winding number without
passing through a singular (non-smooth) configuration.  This
integer rigidity is exactly why MaSt can claim:

- **Charge quantization** — a 2π phase winding on a charged
  sheet is topologically protected (an appeal to MaSt, but
  also the standard Kaluza-Klein picture)
- **Spin quantization** — tube-winding parity gives
  fermion vs. boson
- **Stable particle identity** — six integers cannot drift
  continuously into another configuration

All of this rests on the compact space having non-contractible
loops.

**The sphere is topologically trivial.**  Formally,
π₁(S²) = 0 (first homotopy group is trivial) — every closed
loop on a sphere can be continuously shrunk to a point.
There are no non-contractible loops, so there are no
topologically stable winding numbers.

On a torus: π₁(T²) = ℤ × ℤ — two independent integer
winding numbers per sheet, exactly what MaSt uses.  On a
sphere: zero.

### 2.1 What this breaks

| MaSt feature | What requires non-trivial π₁ | Status on S² |
|--------------|-----------------------------|--------------|
| Charge quantization | 2π ring-phase winding | Impossible — no stable winding |
| Spin from tube winding | Topologically distinct tube loops | Impossible — no tube |
| Six-integer mode labels | Z⁶ from π₁(T⁶) | Replaced by (ℓ, m) harmonic labels with ℓ(ℓ+1) eigenvalues — different algebra entirely |
| Topological charge conservation | Cannot smoothly unwrap a winding | Fails — all "windings" are contractible |

On a sphere the wave-equation eigenmodes are spherical
harmonics Y_ℓm with eigenvalues ℓ(ℓ+1)/R².  This is a
perfectly good mathematical spectrum, but it is not the
MaSt spectrum.  None of the model-E identifications
(electron (1,2), proton (1,2), neutron (1,2)×(1,2),
neutrino modes) translate directly.

## 3. Secondary problems

Even setting topology aside, spheres are the wrong shape
for the MaSt mechanisms:

**One intrinsic scale, not two.**  A round S² has a single
radius R.  A torus has two independent circumferences
L_φ, L_θ with free ratio.  Model-E's particle spectrum
depends on aspect ratios (ε_e, ε_p = 8.906, ε_ν ≥ 3.2) —
these have no sphere analog.  The ring/tube distinction —
which distinguishes charge direction from spin direction —
simply does not exist on a sphere.

**No shear.**  A flat torus admits parallelogram (sheared)
lattices.  The shear parameters (s_e, s_p, σ_ep = −0.091)
are load-bearing in model-E:

- s_e, s_p source charge in the sim-impedance picture
  (R19, sim-impedance Tracks 8–12)
- s_ν = 0.022 sets the neutrino mass ratio Δm²₃₁/Δm²₂₁
- σ_ep = −0.091 produces the neutron binding (R27 F18)
- Within-plane shear generates the lepton generation
  hierarchy (R53)

A sphere has no analog of global lattice skew.  All of the
above mechanisms would need to be rebuilt from different
geometric features — and none of the obvious sphere
features (curvature, spherical harmonics) maps onto them.

Beyond these quantitative mechanisms, shear is also the
geometric root of **non-commuting observables within the
compact space**.  Sheared axes mean misaligned eigenbases;
measuring one direction projects away components along
the other.  This is the same structure that produces
Heisenberg uncertainty relations (see Q121 §5a) and
structural non-separability in joint modes (see Q82 §2.6).
A sphere has no shear degree of freedom, so no intrinsic
basis misalignment within the compact space — another
reason sphere fails to support the quantum structure MaSt
builds on the torus.

**KK reduction changes gauge group.**  Standard Kaluza-Klein
on S¹ produces U(1) gauge theory (electromagnetism).  On S²
the isometry group is SO(3), so KK reduction gives a non-
abelian SU(2) gauge theory.  MaSt currently derives
electromagnetism from U(1)-like compact directions; wiring
up an SU(2) structure would be a very different model, more
akin to weak-force compactifications in grand-unified
theories.

**Eigenmode structure is wrong.**  Model-E's mass formula

<!-- mu^2 = (n_phi * epsilon)^2 + (n_theta - n_phi * s)^2 per sheet -->
$$
\mu^2 = (n_\phi \varepsilon)^2 + (n_\theta - n_\phi s)^2 \quad \text{per sheet}
$$

depends on integer winding numbers and the aspect ratio.  No
analog exists on S².  Spherical harmonic indices (ℓ, m) are
a completely different mathematical object.

## 4. Would egg-shapes (ellipsoids) help?

**No — not fundamentally.**  Distorting a sphere into an
ellipsoid (prolate/oblate spheroid, or tri-axial) recovers
*one* thing: a second scale (polar vs. equatorial radius).
So the "aspect ratio" intuition has a partial geometric
analog.

But distortion does not restore topology.  An ellipsoid is
still simply connected (genus 0).  Winding numbers still do
not exist.  And the other losses remain:

- Eigenfunctions become Lamé functions — no clean
  separation of variables, no tidy spectrum
- No analog of lattice shear
- The second scale is geometric, not topological — it
  cannot support a quantized winding number

Egg-shapes recover a geometric parameter (a second scale)
but not the structural feature (non-trivial π₁) that makes
torus the right choice for MaSt.

## 5. What might be gained (briefly)

A few cosmetic items are genuinely easier on spheres:

- **Embedding artifacts disappear.**  The inner/outer
  asymmetry, tube-ring mixing, and self-intersection
  problems that afflict 3D-embedded tori (see R59
  background) vanish on a sphere.  But the Clifford-
  torus framing (R59) already solves this intrinsically
  using the flat 2-torus without 3D embedding, so this
  is not a distinctive sphere win.
- **Fewer free parameters.**  One scale instead of two
  per sheet.  But MaSt already has only 2–4 effective
  free dimensionless parameters, and the ones it has
  (aspect ratios, shears) are load-bearing.  Removing
  them removes what the model needs to work.

Neither is enough to offset the loss of winding topology.

## 6. Directions that go the other way

If varying the topology productively is the goal, the
interesting moves go *away* from the sphere, not toward it:

- **Higher-genus surfaces** (genus g ≥ 2) — 2g independent
  non-contractible loops, richer winding structure.
  Drawback: negative curvature, not flat.
- **Lens spaces and ℤ_k quotients** — add discrete torsion.
  Could potentially relate to generation structure or
  flavor symmetries.
- **Non-orientable surfaces** (Klein bottle, RP²) — ℤ/2
  windings.  Could be interesting for parity / CP.
- **Product of circles S¹ × S¹ = T²** — which is what
  MaSt already uses per sheet.

None of these higher-topology alternatives are currently
explored in the project, but they represent a sensible
space of variations.  The **sphere specifically** is the
worst choice among closed 2-surfaces for MaSt, because
it is the only one with trivial π₁.

## 7. Conclusion

The torus is not a design convenience that MaSt can relax.
It is the minimal compact 2-surface that supports the
topological winding structure the framework requires.

- Sphere removes winding topology → kills charge, spin,
  and particle identity as used in MaSt.
- Egg-shapes (ellipsoids) recover one geometric parameter
  but no topology.
- Higher-genus or quotient alternatives are more
  interesting than spheres, but have not been explored.

Switching to a sphere is not a refinement of MaSt — it is
a rebuild on foundations that delete what MaSt is built on.
This question is recorded as **answered**: sphere-based
compactification is structurally incompatible with the
MaSt program.
