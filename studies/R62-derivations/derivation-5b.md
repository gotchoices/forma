# Derivation 5b — Charge under phase-lock (Q132 v2 refinement)

Refine the single-sheet charge identification of derivation-5.  F14
took the standing-wave quantization `P_4 = n_t h / L_t` as the only
input and concluded `Q = e × n_t`.  For `|n_t| = 1` that answer is
right.  For `|n_t| ≥ 2` it is incomplete: the mode's closed primitive
path loops the tube multiple times, and the charge contributions at
successive tube closures accumulate with ring-dependent phases.
Summing those contributions gives the **ω-sum** over roots of unity.
The result splits `|n_t| ≥ 2` modes into two clean classes:

- **Bright:** primitive `(±1, p_r ≠ 0)` after gcd reduction — charge
  fires at `Q = e·p_t` per primitive, with k-copy multiplicity for
  `k = gcd(|n_t|, |n_r|) > 1`.
- **Dark:** primitive `(|p_t| > 1, p_r ≠ 0)` with `gcd = 1` — charge
  cancels exactly by root-of-unity summation; mass survives, charge
  does not.

This is the KK-native content of [Q132 v2](../../qa/Q132-promotion-chain-principle.md).
Nothing is postulated beyond what F4–F14 already provide; the
refinement is the observation that F14's single-closure quantization
needs to integrate over the *full* primitive path when the tube winds
more than once per primitive period.

---

## Inputs

1. **F4** (derivation-2): two Killing momenta `P_4, P_5` on T².
2. **F11** (derivation-4): tube/ring parametrization `g_44 = ε²,
   g_55 = 1/ε² + s², g_45 = ε s`, with index 4 = tube, 5 = ring.
3. **F14** (derivation-5): under the tube-couples convention
   `B_μ ≡ 0`, `Q = e × n_t` with `e = h/(L_t e_0)` from a
   single-closure standing-wave reading.
4. **F14 D.4 standing-wave quantization**: `P_a = n_a h / L_a`,
   `n_a ∈ ℤ`.

No new conventions are introduced in 5b.  The refinement is purely
a computation of F14's result over the full primitive period.

---

## Section A — What F14's single-closure shortcut omits

### A.1 — The primitive period of a `(n_t, n_r)` mode

> *Purpose: identify the path whose full circumnavigation defines
> the mode.*

A standing-wave eigenstate with compact-momentum quantum numbers
`(n_t, n_r)` has wavefunction
`ψ ∝ exp(i·2π·(n_t·x_t/L_t + n_r·x_r/L_r))` on T².  The classical
primitive closed path — the shortest closed geodesic on which this
wavefunction returns to its starting phase — winds the tube
`|n_t|` times and the ring `|n_r|` times.  Writing the primitive
in reduced form via gcd,

<!-- k = gcd(|n_t|, |n_r|);   p_t = n_t/k;   p_r = n_r/k -->
$$
k \;\equiv\; \gcd(|n_t|, |n_r|),
\qquad
p_t \;\equiv\; n_t/k,
\qquad
p_r \;\equiv\; n_r/k,
\qquad
\gcd(|p_t|, |p_r|) \;=\; 1,
$$

the full `(n_t, n_r)` mode is **k identical copies** of the primitive
`(p_t, p_r)`: geometrically the trajectory retraces the primitive
path k times before returning to its starting phase.  Mass satisfies
`μ(k p_t, k p_r) = k · μ(p_t, p_r)` exactly (F11 linearity), and the
k copies are identified physically in §E below.

### A.2 — The single-closure shortcut in F14

F14's step C.4 writes `P_4 = n_t h / L_t` and identifies this with
`Q/e_0`.  This is valid **per tube closure** — standing-wave
quantization makes any single compact momentum an integer multiple
of `h/L`.  F14 then treats the whole `(n_t, n_r)` mode as one
particle carrying that one integer n_t.

For primitive `|p_t| = 1` the primitive path has exactly one tube
closure, and F14's shortcut is exact: `Q = e·p_t`.

For primitive `|p_t| ≥ 2` the primitive path has `|p_t|` tube
closures; F14 silently sums over them with equal weight.  §B shows
that the correct sum is **not** uniform — successive closures carry
relative phases fixed by `p_r/p_t`, and the sum generically
cancels.

---

## Section B — The ω-sum over tube closures

### B.1 — Phase at the j-th tube closure

> *Purpose: identify the relative phase that each successive tube
> closure contributes to the charge.*

Parametrize the primitive path by arc-length fraction
`λ ∈ [0, 1]`, with `λ = 0, 1` at the start and end of the primitive
period.  The tube phase winds linearly: `φ_t(λ) = 2π p_t λ`, and
the ring phase `φ_r(λ) = 2π p_r λ`.  The tube closes (returns to
`0 mod 2π`) at `λ_j = j/|p_t|` for `j = 1, …, |p_t|`.

At each tube closure `λ_j` the ring phase is

<!-- φ_r(λ_j) = 2π · j · p_r / p_t -->
$$
\varphi_r(\lambda_j) \;=\; 2\pi \cdot j \cdot \frac{p_r}{p_t}.
$$

This is the phase relationship between the ring oscillation and
the j-th tube closure.  Under the tube-couples convention (F14
B.1), charge promotion at the tube event couples to the ring's
mass-quantum field as `exp(i·φ_r)`: the tube fires its
promotion-to-charge event, and the mass field it acts on carries
that ring-dependent phase.  The total charge accumulated by the
primitive is

<!-- Q_net = e · Σ_{j=1}^{|p_t|} exp(i · 2π · j · p_r / p_t) -->
$$
Q_{\text{net}} \;=\; e \cdot \sum_{j=1}^{|p_t|}
\exp\!\bigl(\,i \cdot 2\pi \cdot j \cdot p_r/p_t\,\bigr).
$$

### B.2 — The sum as roots of unity

Let `ω ≡ exp(i · 2π · p_r / p_t)`.  Then `Q_net = e · Σ_{j=1}^{|p_t|} ω^j`.
Two cases:

**Case (i):** `ω = 1`, which happens iff `p_t | p_r`.  Because
`gcd(|p_t|, |p_r|) = 1` by construction, this case reduces to
`|p_t| = 1`.  Every term in the sum is 1, giving

<!-- Q_net = e · |p_t| = e · p_t    (for |p_t| = 1, this is ±e) -->
$$
Q_{\text{net}} \;=\; e \cdot p_t, \qquad |p_t| = 1.
$$

**Case (ii):** `ω ≠ 1`, i.e. `|p_t| ≥ 2`.  The geometric series
evaluates as

<!-- Σ_{j=1}^{|p_t|} ω^j = ω · (1 - ω^{|p_t|}) / (1 - ω) -->
$$
\sum_{j=1}^{|p_t|} \omega^j
\;=\; \omega \cdot \frac{1 - \omega^{|p_t|}}{\,1 - \omega\,}.
$$

The exponent `ω^{|p_t|} = exp(i · 2π · p_r) = 1` for integer `p_r`.
So the numerator vanishes identically, giving

$$
Q_{\text{net}} \;=\; 0, \qquad |p_t| \ge 2 \text{ with } \gcd = 1.
$$

The intuition: the ring phases at successive tube closures form the
`|p_t|`-th roots of unity, which sum to zero by the root-of-unity
identity `Σ_{j=0}^{n-1} ζ^j = 0` for any primitive n-th root
`ζ ≠ 1`.  The charge either fires coherently (Case i) or cancels
exactly (Case ii).  There is no intermediate.

### B.3 — Equivalence to a first-closure decision

An alternative reading: inspect the ring phase at **the first**
tube closure, `λ_1 = 1/|p_t|`.  Ring phase there is
`2π · p_r/p_t`.  For `|p_t| = 1` the ring has completed an integer
number of cycles (`p_r` of them), and the tube's first closure
finds the ring at an integer phase — the promotion fires.  For
`|p_t| ≥ 2` with `gcd = 1`, the ring's phase is a non-trivial
rational multiple of 2π; the promotion fails at first closure, and
the ω-sum formalizes the subsequent closures as exact phase
cancellation.

The "first-closure" picture and the ω-sum picture give identical
case distinctions because the ω-sum is `0` exactly when `ω ≠ 1`,
which is exactly when the ring is off-integer at the first tube
closure.  Physical interpretation is one-shot; mathematical
bookkeeping is cumulative; both deliver the same answer.

---

## Section C — Bright and dark single-sheet modes

### C.1 — Classification

Combining §B with §A.1's primitive reduction:

| Primitive `(p_t, p_r)` | k copies | `Q_net` from one primitive | Name |
|:--:|:--:|:--:|:--|
| `(0, 0)` | — | — | null (no mode) |
| `(0, p_r ≠ 0)` | k | `0` | ring-only neutral |
| `(±1, 0)` | k | `0` (no ring → no mass quantum) | tube-only neutral |
| `(±1, p_r ≠ 0)` | k | `e · p_t = ±e` | **bright** — one primitive charged particle |
| `(|p_t| ≥ 2, p_r ≠ 0)`, gcd=1 | k | `0` (ω-sum cancels) | **dark** — mass only, Q = 0 |

### C.2 — Comparison to F14

F14's `Q = e × n_t` is recovered exactly in the bright case:
`|p_t| = 1 ⇒ Q = e · p_t = e · n_t / k`, and for k = 1 that's F14.
F14's silent assumption was `k = 1` and `|p_t| = 1`.  Modes
violating either assumption are handled by §C.1:

- `k > 1, |p_t| = 1`: k copies of the primitive, interpreted per
  §E below as multiplicity on a binding-free sheet.
- `|p_t| ≥ 2, gcd = 1`: dark; F14's shortcut mistakes these for
  `|Q| = |n_t|` particles.  They are Q = 0 by the ω-sum.
- `k ≥ 2, |p_t| ≥ 2`: multiplicity of dark primitives.

F14's formula is therefore a **correct special case** of §C.1, not
a different rule.  Derivation-5's F14 lemma box is superseded by
F14b (§F below) but its algebra is untouched — the refinement is
in the range of primitives it covers.

---

## Section D — Tube-only and ring-only neutrals

For completeness the `(±1, 0)` and `(0, p_r ≠ 0)` primitives are
both neutral under §C.1.  F14 treated `(±1, 0)` via its shortcut
and would have returned `Q = ±e`; the ω-sum caveat applies
indirectly here because **no ring mass quantum exists** (the ring
winding is zero), so the tube's promotion has nothing to act on.
Physically the tube closes but no mass is present at closure to
promote, so the event is inert.  Formally: set `p_r = 0` in §B and
the ω-sum collapses trivially, but the physical picture is
"promotion event without the prerequisite mass quantum."

Ring-only `(0, p_r ≠ 0)` is unambiguous: no tube event, no charge
promotion, but a nonzero Kaluza-Klein momentum in the ring
direction supplies mass via F7.  The result is a ring-trapped
photon: massive neutral particle.

Both map into the Q132 v2 typology directly: "tube-only neutral"
and "ring-only neutral" are the two flavors of neutral mass that
arise without a bright charged promotion.

---

## Section E — k-copy multiplicity on a binding-free sheet

### E.1 — Mass scaling

From F11, `μ(k p_t, k p_r) = k · μ(p_t, p_r)` by linearity in the
winding vector.  A `k = 2` copy of the electron primitive `(1, 2)`
has mass `2·m_e` exactly.

### E.2 — Physical interpretation

If the sheet on which a k-copy mode lives has a **binding
mechanism** (Z₃ on the p-sheet per R60 T16, conjugate-pair
binding on the ν-sheet per R60 T18), the k copies are bound into
a single composite particle whose primitive charge is `p_t` and
whose composite mass is `k · μ(primitive)`.  The proton is the
canonical example: primitive `(1, 2)` on p-sheet, `k = 3`, Z₃ binds
three primitive strands into one composite with composite charge
`+e` (§F32b of derivation-10b) and composite mass `m_p = 3·μ(1,2)·K_p`.

If the sheet has **no binding mechanism** (the e-sheet, per R60
T17's Z₃ exemption), the k copies propagate as **k independent
primitive particles** — k scattered electrons, not one fused
|Q| = k object.  The "ghost tower" at (2, 4), (3, 6), (4, 8) on
the e-sheet that R63 Track 4 flagged is, under §E.2, the spectrum
of observed states containing 2, 3, 4 co-moving electrons
respectively.  No new particle species is predicted.

### E.3 — Why binding is the discriminator

The ω-sum of §B is a coherent phase sum over **one primitive
period**.  For k copies of the same primitive, the mass scales
`k · μ(prim)` but the ω-sum per copy is unchanged — each copy
independently fires (bright) or cancels (dark).  Whether the k
copies are observed as **one composite** or **k separate
primitives** depends on whether an additional binding holds them
together in spacetime; that question is independent of the ω-sum
itself.  Sections F and G of derivation-10b formalize how the
binding factor enters the compound-charge arithmetic.

---

## Lemma (Track 5b result)

We have shown:

> **(F14b) Charge under phase-lock (single 2-torus).**  Let
> `(n_t, n_r)` be the winding numbers of a standing-wave
> eigenstate on a single 2-torus under the tube-couples
> convention (F14 B.1).  Let `k = gcd(|n_t|, |n_r|)` and
> `(p_t, p_r) = (n_t/k, n_r/k)` be the primitive.  The
> charge of the primitive is
>
> $$
> Q_{\text{prim}} \;=\;
> \begin{cases}
>   e \cdot p_t & \text{if } |p_t| = 1 \text{ and } p_r \neq 0 \quad (\text{bright}) \\
>   0           & \text{otherwise} \quad (\text{dark, ring-only, tube-only, or null})
> \end{cases}
> $$
>
> The full mode is k copies of the primitive.  On a sheet with
> no binding mechanism the k copies propagate as k independent
> primitive particles, each carrying charge `Q_prim`.  On a sheet
> with a k-ary binding mechanism the k copies fuse into one
> composite of composite charge `Q_prim` and composite mass
> `k · μ(p_t, p_r)`.
>
> F14's result `Q = e × n_t` is recovered as the bright, k = 1
> special case; F14b extends it to the full primitive typology
> without further postulates, by computing F14's own
> standing-wave quantization over the primitive's full tube-
> closure path.  The ω-sum over roots of unity forces the
> bright/dark dichotomy as a theorem of standing-wave kinematics,
> not a new rule.

F14b is the derivation-side content of Q132 v2 Section 4 on a
single sheet.  The multi-sheet composition and the recovery of
MaSt's universal charge formula Q = e(−n_1 + n_5) under the v2
refinement are derivation-10b's content.

### What this does not add

- **No new dynamics.**  F14b is a closer reading of F14's own
  standing-wave construction.  The ω-sum is exact classical
  bookkeeping for a periodic path whose closure ratio is `p_r/p_t`.
- **No claim about first-closure causality.**  §B.3 notes the
  equivalence between the ω-sum and a "first-closure decides"
  picture.  Whether the physical dynamics prefers one picture as
  the causal story (the tube "tries" to promote and "succeeds" or
  "fails" based on ring coincidence) is a framing question; the
  math is the same.
- **No new elementary charge.**  F14's identification `e = h/(L_t
  e_0)` carries through verbatim; F14b only refines which modes
  carry charge in units of e and which carry zero.

### Status

**Complete.**  F14b supersedes F14's charge result for the full
primitive typology while preserving it as the bright-single-copy
special case.  Companion lemma F32b (multi-sheet compound
charge under phase-lock) in [derivation-10b.md](derivation-10b.md).
