# modulated-clover.md — proton and neutron as tracks on a modulated-twist clover

**Status:** Working hypothesis (opened 2026-05-21). A construction for realizing the
proton and neutron as closed tracks on a corrugated tube whose cross-section is a
smooth [tube-function](../../ma-domain/work/tube-function.md) clover with **three major
and three minor lobes**, swept around the ring with a **half-twist** and a synchronized
**major↔minor parameter modulation**. The cross-section curvature budget (§2) and the
surface closure (§3) are worked out and hold. The proton and neutron tracks (§4) are
the two (1/2, 1) half-tube tracks, each closing in one ring revolution. **Step 3 done
(2026-05-22):** a single modulation profile closes the proton track at charge Q = +1 and
the neutron at Q = 0 on a simple, smooth surface — the **charge** construction works
(§4.5). **Mass** is the open next step (§6 step 4).

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

### 2.3 The curvature budget

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

**Realizability.** The +4π/3 / −2π/3 split is the *idealized target* — what the proton
would net if its track saw three pieces at full contrast. It is **not** a constraint the
static cross-section must satisfy: per §4.3–§4.4 the operative charge is the modulated
track integral, not the static piece split. And T_maj = 4π/3 is in any case **not
reachable** by the smooth tube-function family — it is the κ → ∞ cusp limit (the
arc-clover). A numerical scan ([scripts/modulated_clover.py](../scripts/modulated_clover.py),
[outputs/modulated_clover_crosssection.txt](../outputs/modulated_clover_crosssection.txt))
finds the smooth family caps near Q_maj ≈ 0.63 (T_maj ≈ 3.95) before the major lobe
degenerates to a cusp; moderate, well-behaved shapes reach Q_maj ≈ 0.55–0.59. What the
static cross-section actually needs is strong major/minor **contrast**; the modulation
(§3) and the track tuning (§6) do the rest.

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

**The closure is a half-twist.** Carrying z(t; θ) through the modulation and twist gives,
for every θ, the exact identity

  z(t; θ+2π) = z(t+π; θ)

— the e^{iπ} twist composes with the a₁ → −a₁ swap and the clover's C₃ symmetry into a
parameter shift of π. So the (t, θ) coordinate chart glues as

  (t, θ+2π) ~ (t+π, θ).

The surface closes in one ring revolution, but with a **half-twist**: going once around
the ring shifts the tube coordinate by π — half the tube. This is the modulated-clover
analogue of the clover-torus's 1/3-twist identification; here it is a 1/2-twist. (An
earlier draft of this file wrongly called the monodromy trivial — it is not, and the
half-twist is exactly what makes §4 close.)

---

## 4. Tracks and closure

### 4.1 A track closes in one ring revolution

A track riding the twist advances in t at the twist rate, t(θ) = t₀ + θ/2. After one
ring revolution its endpoint is (t₀ + π, 2π), which the §3.3 half-twist gluing
identifies with (t₀ + 2π, 0) ≡ (t₀, 0) — the start. **So a twist-riding track closes
after a single ring revolution**, having advanced t by π: it traverses **half the tube,
three of the six pieces**.

In (tube, ring)-winding language the track is **(n_t, n_r) = (1/2, 1)** — one ring
winding and a *half* tube winding. The half-integer tube winding is forced by the
half-twist gluing, the modulated-clover counterpart of the third-integer momenta the
1/3-twist forces on the clover-torus ([clover-quarks.md §11](clover-quarks.md)).

### 4.2 What a closed track is, and what its charge means

A closed twist-riding track is the **(1/2, 1) curve** of §4.1: one ring revolution,
three pieces, half the tube. It does *not* cover all six pieces — the half-twist gluing
(§3.3) supplies the other half of the closure. This resolves the long-standing puzzle
(how can a proton, less than a full trip around the tube, close?): on the half-twisted
surface a three-piece track is a genuine closed loop.

Its charge is **not** the track's own locus-bending. The operative charge is the
curvature *experienced* — the cross-section profile's turning ∂_t χ sampled at the
track's foot, integrated along the track (defined precisely in §4.3). Because the §3.2
modulation makes ∂_t χ at a given piece depend on θ, this is not pinned to a winding
number — which is what leaves room for a proton at +2π and a neutron at 0.

### 4.3 The experienced-curvature functional — definition

This pins what "charge of a track" means. The rest of the construction and the solver
(§6) depend on it.

**Setup.** Write a surface point as (t, θ): t the cross-section parameter, θ ∈ [0, 2π)
the ring angle (a track closes after one ring revolution, §4.1). The cross-section at
ring angle θ is the modulated, twisted tube-function

<!-- z(t;θ) = e^{i α(θ)} R e^{i t} [ 1 + a1(θ) cos3t + a2 cos6t + i(b1(θ) sin3t + b2 sin6t) ] -->
$$
z(t;\theta) \;=\; e^{i\alpha(\theta)}\,R\,e^{i t}\,\Bigl[\,1 + a_1(\theta)\cos 3t + a_2\cos 6t + i\bigl(b_1(\theta)\sin 3t + b_2\sin 6t\bigr)\,\Bigr]
$$

with twist α(θ) = θ/2 and modulation a₁(θ) = a₁cos(θ/2), b₁(θ) = b₁cos(θ/2) (§3).

**Profile tangent angle.** The tangent of the cross-section profile, at parameter t and
ring angle θ, points along ∂_t z. Its angle is

  χ(t; θ) = arg ∂_t z(t; θ).

The turning of any piece of the profile, *at fixed θ*, is the change Δχ across it; the
whole profile gives ∮ ∂_t χ dt = 2π (Gauss–Bonnet). The piece turnings T_maj, T_min of
§2.3 are exactly Δχ over a major / minor piece.

**A track** is a curve on the surface, (t(s), θ(s)) for a parameter s, winding the ring
once (θ: 0 → 2π); t advances by π — three pieces, half the tube — with the §3.3
half-twist gluing supplying closure.

**Definition — the experienced-curvature charge.** As the track advances, its foot moves
along the cross-section profile; the curvature it *experiences* is the profile's own
turning, ∂_t χ, evaluated in the cross-section shape at the track's *current* ring angle.
The track's charge is the accumulation of that turning, normalized:

<!-- Q_track = (1/2π) ∫_track ∂_t χ(t;θ) dt = (1/2π) ∫ (∂χ/∂t)(t(s),θ(s)) (dt/ds) ds -->
$$
Q_{\text{track}} \;=\; \frac{1}{2\pi}\int_{\text{track}} \partial_t\chi(t;\theta)\,dt
\;=\; \frac{1}{2\pi}\int_{0}^{s_{\text{end}}} \frac{\partial\chi}{\partial t}\bigl(t(s),\theta(s)\bigr)\,\frac{dt}{ds}\,ds
$$

**Three properties that make this the right object:**

1. **Static limit — the split is already there.** Freeze θ (no modulation): the proton
   track (three pieces, major–minor–major) integrates 2T_maj + T_min; the neutron track
   (minor–major–minor) integrates 2T_min + T_maj; the two sum to 2π. So even statically
   the tracks separate — ≈ (5.8, 0.5) at the Step-1 evaluation cross-section. The
   modulation only has to *sharpen* that to exactly (+2π, 0), not create it.

2. **The modulation sharpens the split.** Each track closes in one ring revolution, over
   which the modulation runs a full a₁ → −a₁ swing; the track watches its three pieces
   morph from full +contrast through the neutral midpoint to full −contrast. The proton
   and neutron tracks, offset by one piece, sample that morphing out of step — which is
   what tunes them from their static starting values (property 1) onto exactly +2π and 0.

3. **Two components — the charge is the tube one.** The change in the profile-tangent
   angle along the track splits as dχ = ∂_t χ dt + ∂_θ χ dθ: a **tube-direction**
   component (turning from moving along the profile) and a **ring-direction** component
   (turning from the shape morphing under the track). The proton/neutron charge is the
   *tube* component, Q_track above. The shape morphing is fully in the model — it enters
   the charge through the θ-dependence of ∂_t χ (the track samples the profile's turning
   in the *morphed* cross-section at its current ring angle), and the ring component
   ∮∂_θ χ dθ is a real, separate quantity computed alongside, not discarded. Neither
   component is the track's own geodesic curvature (the "locus turning" of §4.2, which
   would force Q = winding number); both are turnings of the cross-section profile.

4. **The two components sum to a topological integer.** Around the closed track,

     ∮ dχ = ∮ ∂_t χ dt + ∮ ∂_θ χ dθ = 2π·n,    n ∈ ℤ,

   where n is the winding number of the profile-tangent field ∂_t z around the loop.
   Each component alone is real-valued and continuously tunable; their *sum* is locked to
   2π·n. This is why the charge must be the **tube** component and not the total: the
   total ∮dχ is quantized and could never be tuned to land on +2π (proton) versus 0
   (neutron), whereas Q_track = (1/2π)∮∂_t χ dt is a genuine tunable functional. Once
   Q_track is fixed, the ring component follows: ∮∂_θ χ dθ = 2π(n − Q_track).

**Explicit form.** With z = e^{iα} R e^{it} w(t;θ), w the bracket, ∂_t z =
e^{iα} R e^{it}(i w + ∂_t w), so χ = α + t + arg(i w + ∂_t w) and

  ∂_t χ = 1 + Im[ (i ∂_t w + ∂_t² w) / (i w + ∂_t w) ].

This is explicit trigonometry in t with θ-dependent coefficients — the same closed-form
curvature machinery already in [harmonic_tube.py](../../ma-domain/scripts/harmonic_tube.py).

**Sudden-approximation shortcut.** If the track crosses each piece quickly compared with
the modulation timescale, ∂_t χ is evaluated at a nearly constant θ over each piece, and

  Q_track ≈ (1/2π) · Σ T_k(θ_k)   (k over the track's three pieces),

a sum of three closed-form piece-turnings T_k at the ring angles θ_k where the track
crosses them. A fast first estimate; the solver (§6) does the full integral.

### 4.4 Proton and neutron as the two half-tube tracks

The proton and neutron are the two **(1/2, 1) tracks** of §4.1, offset around the tube
by one piece (π/3 in t) — equivalently, by *where they start*:

- **proton** — starts on a major piece; covers major–minor–major;
- **neutron** — starts on a minor piece; covers minor–major–minor.

Each closes in one ring revolution. They share two of their three pieces and differ in
the third; because of the π/3 offset they cross corresponding pieces at modulation phases
one piece-width (2π/3 of θ) apart.

The construction succeeds if the cross-section shape and the modulation profile can be
tuned so the proton track nets ∫∂_t χ dt = +2π and the neutron track nets 0. Statically
the two already sit near (+2π, 0) — ≈ (5.8, 0.5) at the Step-1 cross-section (§4.3
property 1) — so the tuning sharpens rather than creates. This is the solver task of §6.

### 4.5 The proton↔neutron symmetry, and how the modulation breaks it

Worked out numerically in Step 3 ([scripts/modulated_clover.py](../scripts/modulated_clover.py),
[outputs/modulated_clover_tracks.txt](../outputs/modulated_clover_tracks.txt)). The result
is structural.

**The symmetry.** When the modulation profiles a₁(θ), b₁(θ) are built from **cos**
half-integer harmonics only, cos((2k+1)θ/2), they are *even in θ*. The surface then has a
reflection symmetry (t, θ) → (−t, −θ), under which z → z̄, and this reflection maps the
**proton track exactly onto the neutron track**. So with a θ-even modulation
Q_proton ≡ Q_neutron — the two charges are locked equal (numerically both = 1/2), and no
cos-modulation can separate them.

**Breaking it.** The fix is **odd-in-θ** modulation — sin((2k+1)θ/2) harmonics. They are
still antiperiodic (sin((2k+1)(θ+2π)/2) = −sin(...)), so the surface still closes (§3.3);
being odd in θ they break the (t,θ)→(−t,−θ) reflection and open D ≡ Q_proton − Q_neutron.

**The two roles.** The Step-3 solver makes the division of labour clean:

- **sin-harmonics set the charge *difference*** D = Q_proton − Q_neutron;
- **cos-harmonics set the charge *sum*** Q_proton + Q_neutron (θ-even, they shift both
  charges together without re-breaking the symmetry).

Exact (Q_proton, Q_neutron) = (+1, 0) needs **both**: D = 1 from the sin-harmonics and
sum = 1 from the cos-harmonics. A sin-only search reaches D ≈ 1 but leaves the sum near
0.7; adding the cos-harmonics lands the exact pair.

**Result.** With a₁ cos-harmonics ≈ (+0.19, −0.51) and sin-harmonics ≈ (+0.20, +0.67)
(b₁ = −0.015, a₂ = 0.34, b₂ = 0.03), the proton track nets Q = +0.999 and the neutron
Q = −0.001, on a cross-section simple at every ring angle (star-margin +0.26,
κ_max ≈ 15 — moderate, not a near-cusp). **The charge construction works.**

---

## 5. Fallback readings if the parallel-track tuning fails

**Update (2026-05-22): not needed — §4.4's tuning succeeded (§4.5). The fallbacks below
are retained for reference only.**

If §4.4's tuning cannot drive the proton-phase and neutron-phase curves to (+2π, 0)
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

1. **Characterize the cross-section's achievable contrast.** *(Done —
   [scripts/modulated_clover.py](../scripts/modulated_clover.py).)* Scan T_maj over the
   shape parameters. Result: T_maj = 4π/3 is the κ → ∞ cusp limit, not reachable with a
   smooth bounded-curvature curve; the smooth family caps near Q_maj ≈ 0.63. A
   moderate-curvature, strong-contrast simple cross-section is what Step 3 consumes.
2. Fix the modulation a₁(θ), b₁(θ) and twist α(θ) = θ/2; confirm S(2π) = S(0) and the
   C¹ seam analytically.
3. **Solve for the modulation that closes the charges.** *(Done — 2026-05-22,
   [scripts/modulated_clover.py](../scripts/modulated_clover.py) `--step 3`.)* A
   symmetry-breaking sweep over the sin-harmonics, then a zoom-refinement over the sin-
   and cos-harmonics, found a modulation profile for which the proton track nets
   Q = +0.999 and the neutron Q = −0.001, on a cross-section simple at every ring angle
   (§4.5). The **charge** construction works.
4. **Mass.** *(Metric derived — §7; eigensolver built and validated; the
   mode↔track identification is the open conceptual problem.)* Mass is the spectrum of a
   *wave* on the modulated-clover surface — the 2-D Laplace–Beltrami problem of §7. The
   eigensolver is built ([scripts/modulated_clover.py](../scripts/modulated_clover.py)
   `--step 4`, cotangent Laplacian on a triangle mesh) and validated (constant mode at
   μ² = 0). But Step 4 also **falsified** the §7.5-draft "cos-only degenerate nucleon
   doublet" idea: a ℤ₂ reflection gives even/odd singlets, not degeneracy. The genuine
   open problem (§7.5): the proton and neutron are two tracks — the same knot — on one
   surface; assigning them two distinct masses from one wave spectrum needs a mode↔track
   identification not yet in hand. The charge construction (steps 1–3) is unaffected.

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

## 7. Mass — the induced metric and the eigenvalue problem

§§2–6 settle the **charge** construction. **Mass** (§6 step 4) is a *wave* on the
modulated-clover surface. This section derives the surface's induced metric and states
the mass eigenvalue problem precisely — the "derive first" step before any numerics.

### 7.1 The embedding

The cross-section, with the twist and modulation baked in (§3, §4.3), is the complex
coordinate

<!-- ζ(t,θ) = ρ e^{i α(θ)} e^{i t} w(t;θ),  α(θ) = θ/2 -->
$$
\zeta(t,\theta) \;=\; \rho\,e^{i\alpha(\theta)}\,e^{i t}\,w(t;\theta),
\qquad \alpha(\theta) = \theta/2,
$$

with ρ the cross-section scale and w(t;θ) = 1 + a₁(θ)cos3t + a₂cos6t +
i(b₁(θ)sin3t + b₂sin6t). The real pair P_x = Re ζ, P_y = Im ζ is the cross-section
point. Sweeping it around a ring of radius R_major gives the corrugated-torus embedding

<!-- r(t,θ) = ( (R_major+P_x)cosθ, (R_major+P_x)sinθ, P_y ) -->
$$
\vec r(t,\theta) \;=\; \bigl(\,(R_{\rm major}+P_x)\cos\theta,\;\;
(R_{\rm major}+P_x)\sin\theta,\;\; P_y \,\bigr)
$$

(ring centreline R_major(cosθ,sinθ,0); outward normal N̂ = (cosθ,sinθ,0); binormal
B̂ = (0,0,1)). The twist is a *physical rotation* of the cross-section — embedding "B"
of [clover-quarks.md §9.3](clover-quarks.md) — carried inside ζ by the e^{iα(θ)} factor.

### 7.2 The induced metric

The first fundamental form is g_ij = ∂_i r⃗ · ∂_j r⃗, with i, j ∈ {t, θ}. Writing
ζ_t = ∂_t ζ and ζ_θ = ∂_θ ζ, and A = Re ζ_θ, W = R_major + P_x,

  ∂_t r⃗ = ( (Re ζ_t)cosθ, (Re ζ_t)sinθ, Im ζ_t ),
  ∂_θ r⃗ = ( A cosθ − W sinθ, A sinθ + W cosθ, Im ζ_θ ).

The cosθ/sinθ cross-terms collapse on taking dot products, leaving

<!-- g_tt = |ζ_t|² ;  g_tθ = Re(conj(ζ_t) ζ_θ) ;  g_θθ = |ζ_θ|² + (R_major + Re ζ)² -->
$$
g_{tt} = |\zeta_t|^2,\qquad
g_{t\theta} = \operatorname{Re}\!\bigl(\overline{\zeta_t}\,\zeta_\theta\bigr),\qquad
g_{\theta\theta} = |\zeta_\theta|^2 + (R_{\rm major}+\operatorname{Re}\zeta)^2 .
$$

g_tt and g_tθ are exactly the flat first-fundamental-form of the curve ζ in the plane;
g_θθ adds the ring-radius term (R_major + P_x)². **Sanity check:** a plain circular tube
ζ = ρe^{it} gives g_tt = ρ², g_tθ = 0, g_θθ = (R_major + ρcos t)² — the standard torus
metric. ✓

The partials, with α′ = 1/2 and w_θ = a₁′(θ)cos3t + i b₁′(θ)sin3t (a₂, b₂ are
θ-constant):

  ζ_t = ρ e^{iα}e^{it}(i w + w_t),   ζ_θ = ρ e^{iα}e^{it}(i α′ w + w_θ).

The e^{iα}e^{it} phase cancels in the metric — e.g.
g_tθ = ρ² Re[ (−i w̄ + w̄_t)(i α′ w + w_θ) ] — so every component is explicit
trigonometry in t with θ-dependent coefficients a₁(θ), b₁(θ) and their derivatives.

### 7.3 The mass eigenvalue problem

Mass-squared is the Laplace–Beltrami eigenvalue of a wave ψ on the surface (as in
[clover-mass.md §1](clover-mass.md)):

<!-- -Δ_g ψ = μ² ψ,  Δ_g ψ = (1/√g) ∂_i ( √g g^{ij} ∂_j ψ ) -->
$$
-\Delta_g\psi = \mu^2\psi,\qquad
\Delta_g\psi = \frac{1}{\sqrt g}\,\partial_i\!\bigl(\sqrt g\;g^{ij}\,\partial_j\psi\bigr),
$$

with determinant g = g_tt g_θθ − g_tθ², inverse metric g^{tt} = g_θθ/g,
g^{θθ} = g_tt/g, g^{tθ} = −g_tθ/g, and area element dA = √g dt dθ. Δ_g is self-adjoint
with respect to ∫ ψ̄φ dA, so the spectrum {μ²} is real and ordered; m_proton and
m_neutron are particular eigenvalues μ.

### 7.4 Boundary conditions — the half-twist

Single-valuedness of ψ on the surface requires

  ψ(t + 2π, θ) = ψ(t, θ)        (tube periodicity),
  ψ(t, θ + 2π) = ψ(t + π, θ)    (ring, the half-twist gluing of §3.3).

A plane wave e^{i(k_t t + k_θ θ)} obeys these iff k_t ∈ ℤ and k_θ = k_t/2 + m, m ∈ ℤ —
**half-integer-related ring momenta**, the half-twist's Bloch structure (the counterpart
of the third-integer momenta the 1/3-twist forces on the plain clover,
[clover-quarks.md §11](clover-quarks.md)). The metric is not flat, so plane waves are
not eigenmodes; but they label the Bloch sectors the true eigenmodes decompose into.

### 7.5 What remains, and one structural point

To obtain masses: build g_ij(t,θ) from §7.2, discretise −Δ_g on the (t,θ) torus with the
§7.4 twisted boundary conditions, and compute the low eigenvalues. **No 1-D reduction is
available** — the modulation breaks the helical translation symmetry that gave
[clover-mass.md](clover-mass.md) its Hill equation — so this is a genuine 2-D sparse
eigenvalue problem.

Two things mass adds that charge did not:

- **Scale.** Charge was scale-invariant; mass is not. ρ and R_major (equivalently the
  aspect ratio ε ≈ ρ/R_major) set the mass scale and become fit parameters: can the
  modulation that gives the right charges also give m_p, m_n, and the ≈ 1.3 MeV split?
- **Mode ↔ track identification.** Which eigenmode is the proton and which the neutron —
  the modes in the Bloch sectors compatible with the (1/2, 1) proton/neutron tracks
  (§4.4). An identification step, not just computation.

**A conceptual gap, surfaced by the Step-4 computation.** §4.5's reflection
(t,θ) → (−t,−θ) makes the *classical tracks'* charges equal, Q_proton = Q_neutron,
because the reflection maps one track onto the other — two distinct objects, equal
charge. An earlier draft of this section carried that over to mass: "the reflection
forces m_proton = m_neutron, a degenerate nucleon doublet that the sin-harmonics split."
**That is wrong.** A ℤ₂ reflection does not force degeneracy — it only sorts the
Laplace–Beltrami eigenmodes into reflection-even and reflection-odd *singlets*. The
Step-4 cos-only spectrum ([scripts/modulated_clover.py](../scripts/modulated_clover.py)
`--step 4`) confirms it: no clean degenerate doublets appear.

The deeper issue the computation exposes: the proton and neutron are two *tracks* on
**one** surface — and the *same* knot (§4.4), heavily overlapping (they share two of
three pieces). One surface has one Laplace–Beltrami spectrum. **How that single spectrum
assigns the proton and the neutron two distinct masses is not yet well-posed.** Two
readings are open:

- the proton and neutron are two distinct low eigenmodes of the one surface, identified
  by a (1/2,1)-track ↔ mode link — m_n − m_p is the gap between them; or
- they are the symmetric/antisymmetric superpositions of two overlapping
  track-localized states (a two-level system) — m_n − m_p the bonding/antibonding split.

Either way the missing piece is the **mode ↔ track identification**, and the cos-only
"degenerate doublet" shortcut does not exist. The charge construction (§§2–4) stands;
the mass side needs this resolved before its numbers mean anything.

---

## 8. Cross-references

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
