# Chapter 3 — Examining the modes

**Status:** Bare outline. Each section is one sentence describing
the work that section will perform. To be filled out once the
outline is approved.

[Chapter 2](02-mass-from-u.md) derived the mode structure of the
wave equation on M and identified a discrete rest-mass spectrum
m_n = ℏ|n|/(R_u c). This chapter takes that result and looks at
what each mode family is *like* — what shape the modes take in
spacetime, how they move, and what visualizing them on the (t, S,
u) manifold reveals. New visualization figures (cylinder
embeddings, light cones, helical phase contours of massive modes)
belong here.

The chapter is examination, not derivation. It does not introduce
new givens or prove new identities; it asks what the result of
Chapter 2 *means* by looking at it carefully.

---

## Bare outline

### 1. The lowest mode (n = 0): light

Brief comparison/setup section, kept short. Most of the n = 0
content is already established in
[Chapter 2 §4–§6](02-mass-from-u.md): ω = c|k_S|, v_p = v_g = c,
no rest energy, no u-structure. This section's job is just to
set the picture cleanly — n = 0 is ordinary light, with no
internal structure to examine — so the contrast in §2 (the mode
that *does* have internal structure) lands well. If no new
insight beyond Chapter 2 emerges, this section stays short.

### 2. The massive modes (n ≠ 0): wave + winding, not particle on a spiral

Examine the n ≠ 0 modes in detail. Distinguish carefully between:

- **The particle's worldline.** A wave packet's center moves
  through S at v_g, tracing a *straight line* in (S, t). The
  particle is delocalized in u (uniform amplitude around the
  compact circle), so it has no u-position. The worldline does
  not spiral.
- **The wave's phase structure.** At every (S, t) where the wave
  has support, its phase winds n times around u; surfaces of
  constant phase are *helical sheets* in the (t, S, u) volume.
  The helix lives in the wave's geometry, not in any spatial
  trajectory.

The right picture is *a circling wave in u progressing through
space*. The phase circles around u (encoding the rest energy
that gives the mode its mass); the wave packet moves through S
(spatial motion); the u-winding rides along with the packet as
it propagates. **Mass is the energy stored in the
compact-direction phase structure**, not a literal spiraling
path.

Important not to conflate this with charge. If a particle's
*worldline* were genuinely spiraling around u (i.e., the
particle's trajectory had a nonzero du/dτ component), that motion
would couple to off-diagonal metric components — exactly the
standard KK picture for charge. In our setup the particle is
delocalized in u (no u-trajectory) and only the wave's phase
winds. That is mass, not charge. The distinction will matter
again in [Chapter 4](04-metric-self-consistency.md) when we ask
whether off-diagonals get sourced.

Side-thread (worth at least a brief aside when this section is
fleshed out): this picture restores something close to
Schrödinger's original "wave is real" reading of ψ. The wave
nature of a massive particle, in our setup, is not a mysterious
particle/wave duality nor a purely probabilistic amplitude — it
is a literal wave with a frequency and wavelength on the
manifold M, with rest mass arising from a specific structural
feature (winding around u) of that wave. The "wave-particle
duality" mystery becomes a concrete geometric statement: every
massive object has a real wave, and the wave's compact-direction
winding is what makes it massive.

### 3. The ±n distinction: what direction of u-winding carries

Examine what physical content (if any) is carried by the *sign*
of n. Mass depends only on |n|, so m_{+n} = m_{−n} for any
integer n; the two modes have the same rest mass but opposite
winding direction around u. Open question: what is the analog,
in our mass-only setup, of standard KK's "charge sign" reading
of ±n? Candidates include particle-vs-antimatter distinction,
internal chirality, an unobserved internal quantum number, or no
physical distinction at all on this minimal manifold. To be
examined.

### 4. Visualization on the cylinder

Build the (t, S, u) Cartesian rendering. Show the n = 0 mode as
a flat sheet (no u-structure), the n = 1 mode at rest as a wave
whose phase winds around u while the packet sits at fixed S, and
the n = 1 mode in motion as a wave packet moving along S while
its phase contour traces a helical sheet through the (t, S, u)
volume. Possibly add a comparison figure showing the same
particle at different speeds.

**Visualization tooling.** Two complementary routes:

- **Static figures** for the chapter (matplotlib 3D, like the
  existing [figures/](figures/) scripts). The (t, S, u) volume
  is rendered as a 3D scene viewed from a fixed camera angle —
  actual 3D geometry projected to a 2D PNG, not a hand-drawn
  flat picture. The cylinder appears as a translucent
  surface; wavefronts as colored phase contours inside it.
  Probably 2–3 panels per figure (e.g., n=0 / n=1 rest /
  n=1 moving).
- **Interactive 3D explorer** for live exploration. The
  [mass-uni.md](mass-uni.md) spec describes this; once built
  it becomes `viz/mass-uni.html`, linked from this section.
  Real 3D rendering with camera controls, parameter sliders,
  multiple particles.

The static figures should be sufficient for the chapter prose;
the interactive viewer is a richer companion for readers who
want to manipulate parameters themselves.

### 5. End of Chapter 3

Summarize what examining the modes has revealed beyond what
Chapter 2 derived: the qualitative pictures of light vs. massive
modes, the wave-vs-worldline distinction, the open question
about ±n, and any visualization-driven intuitions worth carrying
forward. Note explicitly that the chapter has not introduced any
new physics — every claim it makes is a consequence of
Chapter 2's derivation, made visual.

---

## What's next

For the next chapter and the rest of the project arc, see the
project [README's table of contents](README.md#chapters).
