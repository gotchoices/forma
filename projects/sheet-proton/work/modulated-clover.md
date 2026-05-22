# modulated-clover.md — proton and neutron as tracks on a modulated-twist clover

**Status:** Working hypothesis (opened 2026-05-21). A construction for realizing the
proton and neutron as closed tracks on a corrugated tube whose cross-section is a
smooth [tube-function](../../ma-domain/work/tube-function.md) clover with **three major
and three minor lobes**, swept around the ring with a **half-twist** and a synchronized
**major↔minor parameter modulation**. The cross-section curvature budget (§2) and the
surface closure (§3) are worked out and hold. The proton and neutron tracks (§4) are
parallel (n_t, n_r) = (1, 2) curves on the surface; making their *net experienced curvature* land on
+2π and 0 is a curvature-tuning problem, set up for solution in §6.

**Origin.** The arc-clover baryon paths do not close: [clover-quarks.md §3.2/§12.2](clover-quarks.md)
derive the (1,2)/(1,1) closure numbers by summing per-arc *turning angles* (lobe 240°,
saddle 120°) and feeding them into the *φ-displacement* closure formula — two different
measures. A literal-arc proton (2 lobes + 1 saddle) covers φ-displacement 2φ_L + φ_S,
which lies in (2π/3, 4π/3) for every geometry and is never a whole tube wrap, so it
cannot close. [clover-quarks.md §14](clover-quarks.md) open questions 3–4 already flag
this. This file replaces the piecewise-arc clover with the smooth harmonic family of
[tube-function.md](../../ma-domain/work/tube-function.md) and adds two new ingredients
(twist + modulation) to attack closure directly.

**Tone:** Geometric construction first. Solid results and open problems are labelled as
such. The neutron track is the central unknown.

---

## 1. The idea

Three moves, taken together:

1. **Six equal pieces.** Use a tube-function cross-section with 3 *major* and 3 *minor*
   lobes. Cut it into six equal angular pieces, each one lobe flanked by two valley
   halves. Tune the shape so each major-lobe piece has net convex curvature (u-like,
   Q = +2/3) and each minor-lobe piece has net concave curvature (d-like, Q = −1/3).

2. **Half-twist.** Sweep the cross-section around the ring with a twist of 180° per
   ring revolution.

3. **Major↔minor modulation.** As the ring angle θ advances, modulate the shape
   parameters so that over one ring revolution every major lobe becomes a minor lobe
   and vice versa.

The hoped-for outcome: a **proton track** (visiting 2 major + 1 minor pieces, net
charge +1) and a **neutron track** (2 minor + 1 major, net charge 0), each closing on
the surface.

---

## 2. The six-piece cross-section

### 2.1 The shape

Use the harmonic tube-function ([tube-function.md §2](../../ma-domain/work/tube-function.md))
at N = 3:

<!-- z(t) = R e^{i t} [ 1 + a1 cos(3t) + a2 cos(6t) + i ( b1 sin(3t) + b2 sin(6t) ) ] -->
$$
z(t) \;=\; R\,e^{i t}\,\Bigl[\, 1 + a_1\cos(3t) + a_2\cos(6t) \;+\; i\bigl(\,b_1\sin(3t) + b_2\sin(6t)\,\bigr) \,\Bigr]
$$

The first harmonic a₁cos(3t) is 3-fold; the second a₂cos(6t) is 6-fold. With both
present, the three lobes where cos(3t) > 0 grow (**major**) and the three where
cos(3t) < 0 stay small (**minor**) — a 3-major / 3-minor clover. Splits b₁, b₂ reshape
the curve between the symmetry points without moving the lobe peaks.

Starting point from [viz/tube-lab](../../viz/tube-lab.md) (user, 2026-05-21,
approximate): N = 3, a₁ ≈ 0.62, b₁ ≈ −0.015, a₂ ≈ 0.340, b₂ ≈ 0.030. These produce the
3-major / 3-minor shape; they are not yet tuned to the curvature targets of §2.3.

### 2.2 Six equal pieces

Major lobes sit at t = 0, 2π/3, 4π/3; minor lobes at t = π/3, π, 5π/3; valley midpoints
at t = π/6 + kπ/3. Cutting at the valley midpoints gives **six pieces equal in the
parameter t** (extent π/3 each), every piece holding one lobe plus two valley halves —
three *major-pieces* and three *minor-pieces*.

Equal pieces is the key improvement over the arc-clover, where a lobe and a saddle have
unequal, geometry-dependent φ-extents. Here "half the tube = exactly three pieces" holds
for any parameter choice.

### 2.3 The curvature budget — solid

The net turning of a piece is ∫κ ds over it (κ the signed geodesic curvature, in
closed form from [tube-function.md §2.5](../../ma-domain/work/tube-function.md)). For a
closed curve ∮κ ds = 2π, so with three major-pieces (turning T_maj) and three
minor-pieces (T_min):

  3·T_maj + 3·T_min = 2π.

Imposing Q_major ≡ T_maj/2π = +2/3 forces:

<!-- T_maj = +4π/3,  T_min = -2π/3 -->
$$
T_{\mathrm{maj}} = +\tfrac{4\pi}{3}\;\;(Q=+\tfrac23),
\qquad
T_{\mathrm{min}} = -\tfrac{2\pi}{3}\;\;(Q=-\tfrac13)
$$

The major-piece is **net convex** (+4π/3) because the large lobe outweighs its valley
halves; the minor-piece is **net concave** (−2π/3) because the valley halves outweigh
the small lobe. Then:

- **Proton** = 3 consecutive pieces, 2 major + 1 minor: 2(4π/3) + (−2π/3) = **+2π → Q = +1**.
- **Neutron** = 2 minor + 1 major: 2(−2π/3) + 4π/3 = **0 → Q = 0**.

This is pure Gauss–Bonnet bookkeeping and is the same charge arithmetic as
[clover-quarks.md §12.3](clover-quarks.md); the only new thing is the repackaging into
six *equal* pieces.

**Tuning.** T_maj = 4π/3 is a *single* scalar condition (T_min then follows) on the four
shape parameters (a₁, b₁, a₂, b₂) — a 3-parameter family of solutions. Easily solved
(§6).

---

## 3. The swept surface

### 3.1 Twist

The cross-section rotates physically by α(θ) = θ/2 as the ring angle advances — a
**half-twist**, 180° per ring revolution.

### 3.2 Major↔minor modulation

The 3-fold-distinguishing harmonics carry the modulation; the 6-fold backbone is held
fixed:

  a₁(θ) = a₁·cos(θ/2),   b₁(θ) = b₁·cos(θ/2),   a₂, b₂ constant.

At θ = 0 the major lobes sit at t = 0, 2π/3, 4π/3. At θ = 2π, a₁ → −a₁, so cos(3t)
reverses sign and the major and minor lobes have swapped. At θ = π (mid-revolution)
a₁ = 0 and the cross-section is momentarily a plain six-equal-lobe shape — the **neutral
midpoint**, where the major/minor (u/d) distinction vanishes.

### 3.3 Surface closure — solid

At θ = 2π the cross-section equals the θ = 0 shape rotated by 180° with major↔minor
swapped. A 180° rotation carries each major-lobe position onto a minor-lobe position;
the major↔minor swap then restores majors to t = 0, 2π/3, 4π/3. Hence

  S(2π) = S(0):

the surface closes as a genuine torus of period 2π in θ. The seam is C¹ because
a₁′(2π) = a₁′(0) = 0 and α′ is constant.

**Note — the net monodromy is trivial.** The twist (180°) and the modulation
(major↔minor swap) cancel: the surface closes with *no* residual rotation of the
cross-section. Individual lobes, however, have period 4π — a given major lobe returns to
"major at its original position" only after two ring revolutions.

---

## 4. Tracks and closure

### 4.1 A twist-riding track closes in two ring revolutions

A track riding the twist gains ½ a tube-turn per ring revolution from the twist, plus
its own integer winding w. Over n ring revolutions the accumulated tube-turns are
n(w + ½). Closure needs this to be an integer **and** n even (the modulation has period
2 revolutions). The minimal solution is n = 2, giving 2w + 1 tube windings.

So every closed twist-riding track winds the tube an **odd** number of times
(1, 3, 5, …); the minimal one covers the full tube once over two ring revolutions.

### 4.2 What a closed track is, and what its charge means

A closed track on this surface is a **(n_t, n_r) = (1, 2) torus curve** — winding the
**tube once** and the **ring twice** (tube-first convention, [clover-quarks.md §0.2](clover-quarks.md)).
Riding the 180°-per-revolution twist, it returns to its start only after **two ring
revolutions** (§4.1), having covered the full tube — all six pieces — once. No closed track covers a
half-tube: closure forces the total tube angle to be a multiple of 2π, so "2 major + 1
minor" is never the literal piece-count of a closed track.

So **"proton = 2 major + 1 minor = +2π" is a statement about the track's net curvature
*experienced*, not its piece count.** The operative charge is

  Q_track = (1/2π) ∫_track κ(ψ; θ) — the cross-section curvature at the track's foot,
  integrated along the track.

Because the §3.2 modulation makes the curvature at a given piece depend on θ, this is
**not** equal to (locus turning) = (tube-winding number) × 2π. Under that naive identity
every closed track would have integer charge equal to its winding — proton +1, and no
neutron; the modulation is exactly what breaks the identity and reopens room for a
charge-0 track.

### 4.3 Proton and neutron as parallel tracks

The proton and neutron tracks are two **parallel (1, 2) curves**, offset around the tube
by 60° — one starting on a major lobe, the other on a minor lobe. This is the "where you
start" of the construction. Both cover all six pieces over their two-revolution closure;
they differ only in the **modulation phase** at which they cross each piece (the
neutron-phase curve is one piece-width — 2π/3 of θ — out of step with the proton-phase
curve).

The construction succeeds if the shape (a₁, b₁, a₂, b₂) and the modulation profile can
be tuned so the proton-phase curve nets ∫κ = +2π and the neutron-phase curve nets 0.
Because each curve crosses every piece at a *varying* modulation phase rather than at
full contrast, the cross-section must "overshoot" — start more extreme — so the
phase-averaged totals still land on +2π and 0. This is a well-posed tuning problem, and
it is the solver task of §6.

---

## 5. Fallback readings if the parallel-track tuning fails

If §4.3's tuning cannot drive the proton-phase and neutron-phase curves to (+2π, 0)
simultaneously, three alternative readings of the neutron remain:

**(a) Neutron as an out-and-back track.** A closed track with zero net tube winding must
reverse — cover a (d, u, d) half-tube forward, then return. Net locus turning 0 → Q = 0.
Topologically valid (winds the ring, nets zero tube). The modulation can make the
forward and return legs traverse different shapes, so the loop is not a degenerate
retrace.

**(b) Neutron does not close → it is an open track.** If the proton is the unique closed
(stable) track and the neutron is open, that *is* physical content: open ⇒ unstable ⇒
β-decay to the closed proton. Connects to the standing open question "why is the proton
stable and the neutron unstable" ([clover-quarks.md §12.5–12.6](clover-quarks.md),
[STATUS.md](STATUS.md)).

**(c) Proton and neutron as the two halves of one Q = +1 loop.** The minimal closed
track (two ring revolutions, full tube) is a (u, d, u) half on revolution 1 and a
(d, u, d) half on revolution 2 — the modulation flips it. Read the proton as revolution
1 and the neutron as revolution 2 of the same object: not independent loops. Reframes
what "a baryon" is.

---

## 6. What to solve

**Mathematical.**

1. Solve T_maj(a₁, b₁, a₂, b₂) = 4π/3 for the cross-section. One scalar equation; pick a
   convenient slice (e.g. b₁ = b₂ = 0, or the user's small-b values) and solve for
   (a₁, a₂). Verify T_min = −2π/3 and that all six pieces are simple, non-self-intersecting.
2. Fix the modulation a₁(θ), b₁(θ) and twist α(θ) = θ/2; confirm S(2π) = S(0) and the
   C¹ seam analytically.
3. Define the proton-phase and neutron-phase tracks as curves (θ(s), ψ(s)) on the
   surface. Choose the precise "experienced curvature" integrand (per §4.2–§4.3). Impose
   proton → +2π, neutron → 0 and solve for the modulation profile and tracks that
   realize both.

**Computational (fallback / verification).**

- Extend [harmonic_tube.py](../../ma-domain/scripts/harmonic_tube.py) (it already
  computes closed-form curvature and A_lobe loci) or add a sheet-proton script:
  compute per-piece net turning vs (a₁, b₁, a₂, b₂); root-find the curvature split.
- Build the modulated + twisted surface mesh; trace candidate tracks; numerically
  integrate the experienced-curvature functional; sweep the modulation parameters for
  the (+2π, 0) target.
- Visualization: [viz/tube-lab](../../viz/tube-lab.md) renders the static cross-section
  already; [viz/proton-lab](../../viz/proton-lab.md) is the natural host for the swept
  modulated surface and the tracks.

---

## 7. Cross-references

- [clover-quarks.md](clover-quarks.md) — arc-clover quark/baryon identification; §3.2/§12.2
  closure (the conflation this file routes around); §11.7 per-arc charge; §14 open
  questions 3–4.
- [tube-function.md](../../ma-domain/work/tube-function.md) — the smooth harmonic
  cross-section family; §2.5 closed-form curvature; §3 concave-saddle threshold.
- [harmonic_tube.py](../../ma-domain/scripts/harmonic_tube.py) — curvature / A_lobe
  verification script.
- [viz/tube-lab.md](../../viz/tube-lab.md), [viz/proton-lab.md](../../viz/proton-lab.md)
  — visualizers.
- [quark-flavor.md](quark-flavor.md), [STATUS.md](STATUS.md) — project context;
  proton-stable / neutron-unstable open question.
