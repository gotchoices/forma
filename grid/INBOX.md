# GRID Inbox

Raw ideas, hypotheses, and open threads not yet formalized
into study documents.  Items here may be promoted to their own
files or absorbed into existing documents as they mature.

---

## 2026-03-31: The cell as a processor on a string

### The computational picture

The GRID lattice looks like a **distributed processor on a
graph network**.  Each node and edge is an independent
computational unit:

- **Node register:** each cell holds an internal register
  storing a fractional bit (ζ = 1/4 for 2D triangular).
  This is the phase θ ∈ [0, 2π).

- **Edge registers:** each of the 3 edges (in the 2D
  triangular case) also stores state — the link phase /
  gauge connection A_μ.  These are the "wires" between
  processors.

- **Clock cycle:** every Planck time, each processor:
  1. Reads its own state and the state of its 3 edges
  2. Advances its own phase (node update)
  3. Advances the state of each of its edges (link update)
  4. The update rule is the lattice equation of motion —
     a "micro-coded instruction set" hardwired into the
     geometry

- **Phase periodicity and carries:** the state registers
  are periodic (θ wraps at 2π).  When a phase accumulates
  past 2π it wraps — analogous to a carry bit.  Where does
  the carry propagate?  Presumably to the edges (gauge
  connection absorbs the wrap, maintaining gauge
  invariance).  This might be the microscopic mechanism of
  charge quantization: a topological carry.

### Sub-state resolution

**Question:** is it "legal" for nodes/edges to do internal
bookkeeping at higher resolution than the ζ = 1/4 bit?

The 1/4 bit is the **externally accessible** information per
cell — what a horizon observer can extract.  Internally, the
phase θ is a continuous variable (or at least finer-grained
than 1/4 bit).  So yes — the cell's internal state can have
higher resolution than what it contributes to the collective
entropy.  Call this **sub-state resolution**: the precision
"right of the decimal place" in the fractional bit.

Analogy: a floating-point register has a fixed number of bits
visible to the bus, but internal pipeline stages may carry
extra guard bits for rounding.

The ζ = 1/4 bound is about the **entropy** (how many
distinguishable macrostates), not the internal state space.
The cell can have a rich internal life as long as the
*externally distinguishable* information per cell is ζ.

### The internal dimension as a string

What if the sub-state lives in an **internal 1D space** — a
tiny periodic dimension attached to each node?

- Each node is a **self-connected string** — a 1D periodic
  loop (a tiny torus) rendered at the lattice site.  It
  supports standing waves whose amplitudes encode the
  node's state.

- Each edge is a **linear string** connecting neighboring
  nodes.  It also supports standing waves that encode link
  state (the gauge connection).

- At the 3 connection points (where edge strings meet the
  node loop), there is a natural **additive junction** —
  the standing waves on the edge and node combine.  This
  is the microscopic version of the covariant derivative
  D_μθ = ∂_μθ − eA_μ: the phase gradient on the node
  (∂_μθ) plus the link contribution (A_μ) combine at the
  junction.

This picture looks like a **graphene sheet** — hexagonal
nodes connected by bonds, with vibrational modes on both.
Graphene could be a sympathetic macro-scale analog of the
fundamental lattice.

### Connection to string theory

This internal 1D dimension — a string-like degree of freedom
at each lattice site — is reminiscent of the **11th dimension**
in M-theory.  String theory says the fundamental objects are
1D strings; here, the "strings" are the internal state space
of nodes and edges.

If the node loop has a circumference related to the Planck
length, and the edge strings have a length of one lattice
spacing (also Planck), then the string tension and mode
spectrum would be set by the lattice geometry.  The standing
wave modes on the node loop would be quantized — giving
discrete internal states despite the continuous phase.

**Status:** purely conceptual.  May be functional (could
lead to a computational model) or may be just a useful
mental picture.

### Potential next step

Build a Python model of a small triangular lattice where:
- Each node has an internal 1D periodic register (mode
  amplitudes)
- Each edge has a 1D linear register
- Update rules propagate state per clock cycle
- Test whether the lattice can store a superposition of
  plane waves going in arbitrary directions (which is what
  is needed to host Maxwell's equations, and likely
  gravity via the thermodynamic route)

### Clifford embedding of Ma tori in S

The MaSt material sheets (Ma) are 2-tori embedded in the 3D
spatial lattice (S).  The current treatment may be too
abstract — the embedding might be more **literal** than
previously assumed.

**Problem:** embedding a flat 2-torus in 3D Euclidean space
necessarily introduces extrinsic curvature (you get a donut
shape, which stretches the surface).  A **Clifford torus**
embeds a flat torus in 4D (specifically in S³ ⊂ R⁴) with
zero extrinsic curvature — it sits "flat" in the higher-
dimensional space.

**Questions:**
- Can we embed the Ma 2-torus into 3D+1 (S × t) via a
  Clifford-like construction without warping?
- Does the (1,3) signature of spacetime help or hurt?  In
  Minkowski space, the extra dimension is timelike — this
  changes the geometry of the embedding.
- If the torus must embed in 3D (not 4D), is the extrinsic
  curvature physical?  Does it contribute to the particle's
  mass or energy?
- Does MaSt as currently formulated implicitly assume a flat
  embedding, and if so, does that need to be revisited?

**Status:** open question.  May need a focused study if the
embedding geometry affects the physics.

---

## 2026-03-31: Flat grid, warped embedding, dual-bubble law

**Promoted to** [dual-bubbles.md](dual-bubbles.md).

Core idea: the flat Ma torus forces the ambient S lattice to
deform (→ gravity), and the product λ_C × r_s = 2L_P² =
1/(2ζ) is a conservation law linking internal compactness to
external curvature.

---

## 2026-03-31: Two planned simulation studies

Both are substantial enough to warrant their own folders
inside `grid/`.  Design notes below; execution is future
work.

### Study A: Gravity from embedding (`sim-gravity/`)

**Question:** does embedding a rigid flat structure in a
relaxed lattice produce a deformation field that falls off
as 1/r?

See [dual-bubbles.md](dual-bubbles.md) for motivation.
Detailed design in [sim-gravity/README.md](sim-gravity/README.md).

### Study B: Wave propagation on the lattice (`sim-maxwell/`)

**Question:** can a small triangular lattice support
directional wave propagation and superposition — the
minimum conditions for hosting Maxwell's equations?

Two candidate approaches:
1. **Standard lattice gauge theory** — use the Wilson
   action equations of motion as the update rule.  This is
   proven to work (it's how lattice QCD is done), but it
   imports formalism rather than testing the "processor"
   picture from scratch.
2. **String-register model** — each node holds a circular
   standing wave (phase state), each edge holds a linear
   standing wave (link state), and the update rule is local
   superposition at junctions.  This tests whether the
   processor/string picture from the INBOX entry above is
   *functional* or merely *conceptual*.

Approach 2 is riskier but more informative.  If it works
(supports directional propagation, not just diffusion), it
validates the micro-instruction picture.  If it fails
(energy sloshes isotropically), it tells us the string
picture needs more structure.

Detailed design in [sim-maxwell/README.md](sim-maxwell/README.md).
