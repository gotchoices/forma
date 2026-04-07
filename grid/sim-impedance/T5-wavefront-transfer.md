# Track 5: Wavefront transfer — coherent signal coupling at a shared node

**Status:** Framing

---

## The question

A wave propagates on the 2D hexagonal lattice.  At a node
shared with the 3D diamond lattice, some fraction of the
wave's energy transfers onto the 3D lattice and continues
propagating in the same direction.  The rest reflects back
or scatters.

**What fraction transfers?  Is it 1/137?**

This is different from Tracks 3-4:
- Track 3 asked: do edges align? (binary)
- Track 4 asked: how much energy projects per edge? (scalar)
- Track 5 asks: how much of a coherent WAVEFRONT transfers
  through a shared node while maintaining its propagation
  direction? (tensor)

---

## The physics: scattering at a shared node

### Wave states on each lattice

**On the 2D hexagonal lattice:** a propagating wave in
direction k̂ distributes its phase across the 3 wye edges
at a node.  The amplitude on edge k is:

> a_k = ê_wye_k · k̂

where ê_wye_k is the unit vector along wye edge k.  The
three amplitudes (a₁, a₂, a₃) fully describe the local
wave state.  A wave in the forward direction has large
amplitude on the forward-pointing edge and smaller
(possibly negative) amplitude on the two backward-leaning
edges.

**On the 3D diamond lattice:** a propagating wave in the
same direction k̂ distributes its phase across the 4 jack
edges.  The amplitude on edge j is:

> b_j = ê_jack_j · k̂

The four amplitudes (b₁, b₂, b₃, b₄) describe the 3D
wave state.

**For the two waves to be "the same wave"** — the same
disturbance propagating in the same direction on both
lattices — the 2D amplitudes and 3D amplitudes must be
CONSISTENT.  The 2D wave seen from the 3D lattice must
look like a 3D wave.  The 3D wave seen from the 2D
lattice must look like a 2D wave.

### The projection matrix

The matrix that connects 2D amplitudes to 3D amplitudes
is the **projection matrix** M:

> M_jk = ê_jack_j · ê_wye_k

This is a **4×3 matrix** (4 jack edges × 3 wye edges).
Each entry is the cosine of the angle between one jack
edge and one wye edge.  It depends on the relative
orientation (θ, φ, ψ) of the wye plane in the jack.

**What M tells you:**

- **Column k of M:** how wye edge k projects onto the 4
  jack edges.  If wye edge k carries amplitude a_k, the
  induced amplitude on jack edge j is M_jk × a_k.

- **Row j of M:** how jack edge j receives from all 3
  wye edges.  The total signal arriving at jack edge j
  from the wye is Σ_k M_jk × a_k.

- **M × a:** the 4-vector of jack amplitudes induced by
  the wye wave state a.  This is the 3D projection of
  the 2D wave.

- **Mᵀ × b:** the 3-vector of wye amplitudes induced by
  the jack wave state b.  This is the 2D projection of
  the 3D wave.

### What "coupling" means

A 2D wave with state a arrives at the shared node.  It
projects onto the jack as M × a = b_projected.  But the
"correct" 3D wave state (propagating in direction k̂) is
b = (ê_jack_j · k̂).

The coupling efficiency asks: how much of b_projected
matches b?  In other words, how much of the 2D wave's
projection onto 3D has the RIGHT amplitude pattern to
continue as a coherent wavefront?

> η(k̂, θ, φ, ψ) = |b_projected · b|² / (|b_projected|² × |b|²)

This is the **cosine similarity squared** between the
projected amplitudes and the desired amplitudes.  It
ranges from 0 (no overlap — the projection goes in the
wrong pattern entirely) to 1 (perfect match — the
projection IS the correct 3D wave pattern).

### The energy transfer

The total energy that leaves the wye and enters the jack
is |M × a|² / |a|².  But not all of this energy continues
as a forward-propagating wave — some goes in the wrong
direction (scatters).  The fraction that continues
forward is η.

The net transfer efficiency is:

> T(k̂, θ, φ, ψ) = (|M × a|² / |a|²) × η

This is the FRACTION of the incoming 2D wave energy that
exits the shared node as a properly directed 3D wave.

---

## The computation

### Step 1: The M matrix and its properties

Compute M(θ, φ, ψ) for a grid of orientations.  Analyze:

- **Singular values** of M.  The SVD M = U Σ Vᵀ gives 3
  singular values (σ₁ ≥ σ₂ ≥ σ₃).  These are the
  "principal coupling strengths" — the maximum transfer
  along the three principal directions.

  The sum σ₁² + σ₂² + σ₃² = Tr(MᵀM) is the total
  transfer power.  From Track 4's analytical result:
  this sum equals 4 (constant, by the tetrahedral
  identity).  But the INDIVIDUAL singular values may
  vary with orientation — meaning the coupling is
  ANISOTROPIC even though the total is constant.

- **Condition number** σ₁/σ₃.  If all three singular
  values are equal (condition number = 1), the coupling
  is isotropic — all wave directions transfer equally.
  If the condition number is large, some directions
  couple strongly and others weakly.

### Step 2: Transfer efficiency vs propagation direction

For each orientation (θ, φ, ψ), compute T(k̂) for a
sweep of propagation directions k̂ within the wye plane.

The propagation direction k̂ is parameterized by a single
angle γ within the wye plane (since k̂ must lie in the
plane).  Sweep γ from 0° to 360°.  The transfer
efficiency T(γ) tells you: for a wave propagating in
direction γ on the 2D sheet, how much transfers to 3D?

**Key outputs:**
- T_avg(θ, φ, ψ) — average over all propagation
  directions γ
- T_max and T_min — directional extremes
- Whether T is isotropic (same in all directions) or
  anisotropic (preferential transfer in certain
  directions)

### Step 3: Orientation sweep

Map T_avg(θ, φ, ψ) over the full orientation sphere.

**Key questions:**
- Is T_avg constant (like the cos² sum in Track 4)?
- If not, where are the maxima and minima?
- How does T_avg at the ⟨111⟩ magic angles compare to
  generic angles?
- What is the global average ⟨T_avg⟩ over all
  orientations?

### Step 4: The torus integral

Compute the average transfer efficiency over a torus
surface:

> α_torus(ε) = (1/A) ∮ T_avg(θ(s), φ(s), ψ(s)) dA

where the torus geometry (ε, embedding orientation)
determines the path through orientation space.

Sweep ε from 0.1 to 2.0.  Look for ε where α_torus
= 1/137.

---

## Why this might work (where Tracks 3-4 didn't)

**Track 4's analytical result:** Σ cos²(θ_kj) = 4
(constant for all orientations) killed the total-energy
projection approach.  But this identity is about the
SUM of squared projections.  The COHERENT transfer
efficiency — how much of the projection has the right
pattern to propagate forward — is NOT constrained by
this identity.

**Example:** at the magic angle, the 3 wye edges project
cleanly onto 3 of 4 jack edges (each at 19.47° off).
The projected pattern closely matches a wave propagating
perpendicular to the ⟨111⟩ face.  High η.

At a generic angle, the 3 wye edges project onto all 4
jack edges in a messy pattern that doesn't match any
coherent propagation direction.  Low η.

**The transfer efficiency T = energy_fraction × pattern_match
can vary with orientation** even though the energy_fraction
(Track 4's sum) is constant.  The pattern_match (η) is
what varies.

---

## What would each result mean

**T_avg is constant at all orientations:**
Same situation as Track 4 — the geometry is too symmetric
to produce orientation dependence.  α cannot emerge from
the wye-jack coupling alone.  Would need additional
physics (mode structure, resonance, lattice periodicity).

**T_avg varies but ⟨T_avg⟩ ≠ 1/137:**
The coupling IS orientation-dependent, but the average
over the sphere (or the torus at any ε) doesn't match α.
The wye-jack geometry contributes to α but doesn't fully
determine it.

**T_avg varies and the torus integral = 1/137 at some ε:**
Alpha is determined by the torus geometry in the 3D
lattice.  The coupling fraction (the impedance mismatch)
emerges from the wavefront transfer efficiency at the
torus's specific orientation sweep.  This would be the
geometric derivation.

---

## The scattering rule at a shared node

The above treats the coupling as a projection (how the
2D amplitudes map onto 3D edge directions).  The actual
coupling involves the SCATTERING RULE at the node — what
happens when 3 + 4 = 7 edges meet at a single point.

In the standard lattice gauge theory scattering rule,
each outgoing edge gets:

> out_i = (2/N) × Σ_all_in - in_i

where N is the number of edges.  At a shared node with
7 edges (3 wye + 4 jack), the scattering rule mixes
ALL edges.  A signal arriving on a wye edge scatters
into all 7 outgoing edges (including back onto the wye
and onto the jack).

The fraction that scatters FROM the 3 wye edges ONTO
the 4 jack edges (and continues forward) is the physical
coupling.  This can be computed exactly from the
scattering matrix.

**The 7-edge scattering matrix:**

For N = 7 edges at a junction, the scattering matrix is:

> S_ij = (2/7) - δ_ij

This means: each outgoing edge gets 2/7 of the total
input minus its own input.  The fraction of incoming wye
energy that scatters onto jack edges is:

> Fraction onto jack = (4 jack edges) × (2/7)² × ... 

Actually, the computation is:
- Total input from 3 wye edges: E_in = Σ_k a_k²
- Each jack edge j receives: out_j = (2/7) Σ_all a_i - a_j
  (where a_j = 0 since the signal is on wye edges only)
  = (2/7) × Σ_wye a_k
- Total energy onto 4 jack edges:
  4 × (2/7)² × (Σ a_k)²

This gives the transfer fraction as:

> T = 4 × (2/7)² × (Σ a_k)² / (Σ a_k²)

For a uniform input (a₁ = a₂ = a₃ = 1):
> T = 4 × 4/49 × 9 / 3 = 4 × 4/49 × 3 = 48/49 ≈ 0.98

That's nearly perfect transfer — because the scattering
rule distributes energy almost equally across all edges.

For a directional input (a₁ = 1, a₂ = a₃ = 0):
> T = 4 × 4/49 × 1 / 1 = 16/49 ≈ 0.33

This is the 1/3 from Track 4 again.

**But this scattering rule doesn't account for edge
DIRECTIONS.**  The standard (2/N − δ) rule treats all
edges as equivalent.  On the actual lattice, the edges
point in specific directions, and wave propagation
depends on constructive/destructive interference along
those directions.  The DIRECTIONAL scattering — how
much signal scatters into a jack edge AND continues
propagating in the right direction — is what the
projection matrix M and the transfer efficiency T
capture.

The full computation combines the scattering fraction
(from the N = 7 junction rule) with the directional
match (from the projection matrix M).  The product is
the net transfer efficiency.

---

## Connection to earlier work

- **sim-maxwell** verified that directional wave
  propagation emerges from the scattering rule on a
  hexagonal lattice (not from Maxwell being input).
  Track 5 asks: does the same scattering physics produce
  a specific coupling fraction when 2D and 3D lattices
  share a junction?

- **Track 3 F4** found that the fundamental angular gap
  between the wye (120°) and jack (109.47°) is 19.47°.
  Track 5 asks: given this gap, what fraction of a
  coherent wavefront survives the transfer?

- **Track 4** found that the total energy projection
  (cos² sum) is constant at 4/3 per edge.  Track 5
  separates this into "energy that transfers" (constant)
  and "energy that transfers IN THE RIGHT DIRECTION"
  (variable — this is the new content).

---

**Script:** `scripts/track5_wavefront_transfer.py` (planned)
