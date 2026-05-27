# Quark substructure as Wannier functions on the (1/2, 1) track

**Status:** *Exploratory record (demoted 2026-05-26).* The
Wannier-function machinery was explored as a possible formalisation of
the "3 superimposed wave packets per track" picture. It agreed with the
simpler "3 arc-pieces in series along one closed (1/2, 1) track"
reading without adding new predictive content, so the chapter arc
reverts to the simpler picture (see [README.md](../README.md) §Framing).
The one durable finding from this exploration is recorded below as
the **piecewise-circular vs smooth-Fourier distinction**, which is
the basis for Chapter 5's stated position on per-quark fractional
charges. The Wannier construction itself remains available if a future
chapter (mesons, magnetic moments, form factors) needs interference
machinery between quark wave packets.

## What the construction does

[`scripts/wannier_track.py`](../scripts/wannier_track.py)

1. Build the closed (1/2, 1) proton and neutron tracks on the
   Z₂ × Z₃-symmetric Step-7 substrate. Track length ≈ 227.6 (proton)
   and 227.3 (neutron) in script units; L_p / L_n = 1.0013785 matches
   the observed m_n / m_p ratio.
2. Solve the 1-D LB on each closed track: −d²ψ/ds² = λ ψ with periodic
   BC. The lowest band of 3 modes is the constant ψ_0 = 1/√L and
   the lowest cos / sin pair at λ = (2π/L)².
3. Construct 3 **Wannier functions** w_k(s) (k = 0, 1, 2) centered at
   the 3 arc-midpoints s_k = (k + 1/2) L / 3:

   <!-- w_k(s) = (1/√3) [ψ_0(s) + √2 cos(2π(s - s_k)/L)] -->
   $$
   w_k(s) \;=\; \frac{1}{\sqrt{3}}\!\left[\psi_0(s) + \sqrt{2}\,
   \cos\!\Big(\tfrac{2\pi(s - s_k)}{L}\Big)\right]
   $$

   Each w_k is a Z₃-symmetric Gaussian-like packet peaked at site s_k
   with tails extending into the adjacent sites — exactly the
   "overlapping tails" the user's framing predicted.
4. For each Wannier centre s_k, identify which cross-section arc-piece
   the (1/2, 1) track is sitting in at that s. Compute (a) the
   **naive** unmodulated value (+2/3 lobe, −1/3 saddle) and (b) the
   **actual** cross-section per-arc winding at that (t, θ) on our
   substrate.

## Results

### Arc-sequence structure (passes)

The 3 Wannier centres on each closed track sit exactly where the user's
geometric picture predicts:

| Particle | Wannier site 0     | Site 1            | Site 2            |
| -------- | ------------------ | ----------------- | ----------------- |
| Proton   | lobe at t ≈ 0     | saddle at t ≈ π/3 | lobe at t ≈ 2π/3  |
| Neutron  | saddle at t ≈ π/3 | lobe at t ≈ 2π/3  | saddle at t ≈ π   |

So the proton track has a *uud* arc-sequence and the neutron a *udd*
sequence, with each quark naturally localised at one arc-midpoint
under the Wannier construction. The structural picture passes.

### Per-quark fractional charges (does not pass — informatively)

The actual per-arc cross-section winding at each Wannier centre is
computed by integrating (d/dt) arg(∂_t ζ) at fixed θ over the arc
(an interval of length π/3 in t).

| Particle | Wannier site k | Arc       | q_naive | q_arc (modulated) |
| -------- | -------------- | --------- | ------- | ----------------- |
| Proton   | 0              | lobe (u)  | +2/3    | +0.588            |
| Proton   | 1              | saddle (d)| −1/3    | +0.588            |
| Proton   | 2              | lobe (u)  | +2/3    | +0.592            |
| Neutron  | 0              | saddle (d)| −1/3    | −0.257            |
| Neutron  | 1              | lobe (u)  | +2/3    | −0.259            |
| Neutron  | 2              | saddle (d)| −1/3    | −0.259            |

On the *unmodulated* backbone (a₁ = b₁ = 0, just a₂ cos 6t + b₂ sin 6t)
every arc gives +1/6 — completely uniform — instead of ±2/3 / ∓1/3.

So neither the modulated nor the unmodulated Fourier cross-section
delivers the ±2/3 / ∓1/3 per-arc structure. The lobe / saddle
distinction is washed out **in the per-arc integral on a smooth
cross-section**.

## Why — and what this means

The ±2/3 / ∓1/3 derivation in [`per-arc-curvature-as-charge.md`](../../metric-charge/work/per-arc-curvature-as-charge.md)
explicitly assumes a **piecewise-circular** cross-section: a 240°
lobe arc of constant geodesic curvature κ = +1/r and a 120° saddle
arc of constant κ = −1/r, meeting tangentially under the kissing-circles
construction. With those assumptions

<!-- Q_lobe = (1/2π) (1/r) (4πr/3) = +2/3;  Q_saddle = (1/2π) (-1/r)(2πr/3) = -1/3 -->
$$
Q_{\text{lobe}} = \frac{1}{2\pi}\!\cdot\!\frac{1}{r}\!\cdot\!\frac{4\pi r}{3} \;=\; +\tfrac{2}{3}, \quad
Q_{\text{saddle}} = \frac{1}{2\pi}\!\cdot\!\Big(-\tfrac{1}{r}\Big)\!\cdot\!\frac{2\pi r}{3} \;=\; -\tfrac{1}{3}.
$$

A **smooth Fourier-series** cross-section (which is what
`modulated_clover.py` actually constructs) doesn't have constant κ on
each arc-piece — the curvature varies continuously around the
cross-section, and the per-arc integral redistributes away from
±2/3 / ∓1/3 toward more uniform values.

So we have a real tension:

- The framework's quark-charge identification (+2/3, −1/3) is *derived*
  from the piecewise-circular (kissing-circles) clover.
- The construction's modulated-clover surface is *built from* a
  smooth Fourier representation that approximates the
  piecewise-circular ideal but does not reproduce its per-arc
  curvature integrals.
- The (1/2, 1) track integration on the smooth substrate does deliver
  the correct *baryon* charges (Q_proton = +1, Q_neutron = 0) — the
  total is preserved by topology — but the **per-quark fractional
  charges +2/3, −1/3 do not literally appear** at the per-arc level.

The Wannier construction itself is sound: it gives 3 localised wave
packets per track with the correct arc-sequence. The packets *can*
be labelled by quark flavour (u for lobe-centred, d for saddle-centred),
and their integer sum on each track gives the right baryon charge.
The discrete +2/3 / −1/3 *values* per packet are a feature of the
piecewise-circular idealisation, not of any integral on the actual
smooth substrate.

## What to do about it

Three readings, none unique. Chapter 5 should commit to one or hold
them as alternatives.

**Reading 1 — Idealised quarks.** Adopt the user's quark picture as a
*structural label*: each Wannier wave packet *is* a u or d quark,
with charge ±2/3 / ∓1/3 by definition of "this is what a u-like /
d-like packet means," and the smooth-substrate per-arc integral is a
"dressed" / "renormalised" value that approaches the idealised
±2/3 / ∓1/3 in the piecewise-circular limit. The construction's
correct integer baryon charges are the framework's actual prediction;
the fractional charges live in a Platonic Z_6 dihedral that the
construction approximates.

**Reading 2 — Piecewise-circular substrate.** Switch the construction
to a piecewise-circular cross-section (3 lobe arcs of constant κ = +1/r,
3 saddle arcs of constant κ = −1/r, kissing-circles connection). The
per-arc charges become exactly ±2/3 / ∓1/3 by construction. The
closure / charge / mass-ratio analysis would need to be re-done in
this representation. Heavier lift — the existing Fourier machinery
in `modulated_clover.py` would need to be rebuilt around piecewise
arcs.

**Reading 3 — Smooth substrate, fractional charges as ratios.** Accept
that on the smooth substrate every arc has the same per-arc winding
within a track (proton: +0.59 each; neutron: −0.26 each), and that
the +2/3 / −1/3 framework values are a Z_6-symmetric idealisation.
The proton/neutron distinction lives in the *total* charge, not in
per-arc differentiation. Quark structure becomes a *labelling* of
3 Wannier packets per track without a literal per-arc fractional
charge readout.

## Implication for the chapter arc

Chapter 5 (and the README framing) currently states the per-quark
charges as +2/3 / −1/3 from "per-arc curvature under G1." This is
literally true only on a piecewise-circular substrate. On our
smooth Fourier construction the per-quark charges are different in
*value* (≈ +0.59 / −0.26) while still summing to the correct baryon
charge.

The chapter has to name this clearly:

> Under G1, a piecewise-circular N = 3 clover delivers exact per-arc
> charges +2/3 (lobe, u) and −1/3 (saddle, d), summing to +1 (proton)
> or 0 (neutron). Our smooth-Fourier construction approximates this
> idealisation: it preserves the integer baryon charges but distributes
> the per-arc contributions more uniformly. The discrete fractional
> charges are a feature of the idealisation; the smooth construction
> is a tractable working substrate.

This is honest and consistent with [feedback_no_verdicts_from_provisional_formalism]:
the +2/3 / −1/3 quark values are a *structural-formalism* claim, not
a numerical output of the current construction.

## Reproducibility

```
python scripts/wannier_track.py
```
Outputs `outputs/wannier_track_summary.txt`, `outputs/wannier_track.png`.
