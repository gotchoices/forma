# R36. Geometric tilt — α from T²/R³ embedding without KK

**Status:** Complete  
**Questions:** Q77 (α as impedance), Q76 (metric signature),
Q18 (deriving α)  
**Type:** compute + theoretical  
**Depends on:** R19 (shear-charge), R26 (T⁶), R34 (midpoint
coupling)


## Motivation

Every KK-based prediction in the T⁶ model has either been
circular (α formula requires s as input) or failed (Yukawa
corrections ruled out, running of α wrong).  Meanwhile, the
T⁶ model's successes — the particle mass spectrum, nuclear
scaling law, predictive horizon — use the compact geometry
directly and never invoke KK.

KK theory claims that the off-diagonal metric components
between compact and non-compact dimensions ARE gauge fields.
This is an interpretation, not a necessity.  The wave
equation on T⁶ × R³ can be solved without naming any metric
component a "gauge field."

This study explores an alternative geometric picture:

1. Each T² has ORTHOGONAL internal axes (within-plane
   shear s = 0)
2. The T² plane is TILTED relative to R³ — its axes have
   a small component along R directions
3. The tilt angle θ determines how much R³ "sees" of the
   compact modes
4. The coupling constant α = f(θ) — a geometric property
   of the embedding, not a KK gauge coupling

This replaces the mechanism:
  s (T-T shear) → mode charge → KK gauge field → α

with:
  θ (T-R tilt) → R-projection of compact momentum → α

No gauge fields.  No photon as a metric fluctuation.
Electromagnetic interaction is a direct consequence of
how the periodic dimensions are oriented relative to
the spatial dimensions.

The photon, in this picture, is not a gauge boson but a
propagating disturbance in the vacuum — energy inserted
into R³ that travels through the elasticity of the 10D
geometry.  The torus is how R³ "renders" or "interprets"
the periodic T² subspace.


## The designer's-choice hypothesis

α may not be derivable from geometry.  It may be a free
parameter — a "designer's choice" — that sets the coupling
strength between compact and spatial physics.  A different
α would give a differently scaled universe that still works.

By analogy:
- R_t is designed to create time (metric signature −)
- R³ is designed to create space (metric signature +,+,+)
- T⁶ is designed to create matter from energy in R³
- α is the coupling knob: how much R³ perceives T⁶

If this is correct, then the fruitless search for a
derivation of α (R15, R31, R32, R34) was asking the wrong
question.  The right question is: given a tilt angle θ,
does the physics come out right?


## Prior results

- **R19 F35–F43**: α = r²μ sin²(2πs)/(4π(2−s)²).
  The shear s is free; α is an input.
- **R31**: α remains un-derived.  Dynamics needed.
- **R32**: KK running is catastrophic.  Ghost modes need
  ~10⁵ suppression.
- **R34 F23**: The shear is continuous, no selection.
  The formula provides mechanism, not value.
- **R34 F13**: T⁶ known-particle VP runs 2.4× too fast —
  the KK particle content gives wrong running.
- **Q77**: α as impedance mismatch between T⁶ and R³.
- **Q76**: Dimensions have character: temporal, spatial,
  compact.  Each perceives others differently.


## Key questions

1. In a simplified (R¹ + T²) model, does a tilt angle θ
   produce a coupling α(θ) with the same form as the KK
   formula α(r, s)?  Or is it structurally different?
2. Do two modes on a tilted T² interact with a 1/r
   potential in R³?  What determines the coefficient?
3. Does the tilt picture handle ghost modes — do different
   winding patterns project differently onto R³?
4. Is the tilt angle θ any more constrained than the
   within-plane shear s?  Or is it equally free?
5. Can the mass spectrum be preserved exactly (masses
   come from T⁶ geometry, which is unchanged by the tilt)?


## Tracks


### Track 1 — Tilt-angle formalism and mode projection  **Complete**

Work in a simplified model: 1 spatial dimension R¹ and
one compact T² (2 periodic dimensions with circumferences
L₁, L₂ and aspect ratio r = L₁/L₂).

The T² axes are orthogonal to each other (s = 0).
Introduce a tilt: the T² plane is rotated by angle θ in
the (R¹, T²) hyperplane, so that compact motion has a
small R¹ component.

**Result:** The tilt preserves masses exactly (F1) but
produces no interaction between modes (F4).  It is
mathematically equivalent to a constant KK gauge potential
(Wilson line) — which has zero field strength (F3).  Ghost
mode suppression is absent: all modes with nonzero windings
are charged, with no cancellations (F5).  Shear and tilt
are structurally different parameters serving different
roles (F6).  KK is not an assumption imposed on the model
— it emerges from solving the wave equation on compact ×
non-compact space (F8).  Findings F1–F8.


### ~~Tracks 2–4~~ **Answered by Track 1**

Track 1 proved that the tilt is mathematically equivalent
to a constant KK gauge potential, which produces no
interactions (F4), no ghost suppression (F5), and no mass
shift (F1).  This resolves all remaining tracks:

- **Track 2** (mode-mode coupling): impossible without
  gauge field fluctuations, which IS KK.
- **Track 3** (ghost mode projection): tilt gives no
  suppression — charge is linear in n, all modes charged.
- **Track 4** (mass preservation): exact, by construction
  (tilt is a coordinate rotation).


## Summary

**Result: Null (but clarifying).**  Track 1 is definitive.  A uniform
tilt of T² relative to R³ is mathematically equivalent to a constant
KK gauge potential (Wilson line), which has zero field strength and
produces no interactions.  Interactions require the cross-term to VARY
in space — and a spatially varying metric cross-term IS a dynamical KK
gauge field.  KK is therefore not an external assumption; it emerges
from solving the wave equation on compact × non-compact space.

The "designer's-choice" hypothesis for α survives: the shear s (or
equivalently the tilt angle θ) is a free parameter that sets the
coupling strength.  Nothing in the geometry selects its value.


## What success looks like (pre-study)

- **Strong result**: The tilt angle θ produces the same
  coupling α as the KK formula, the 1/r Coulomb potential
  emerges from mode-mode overlap, ghost mode suppression
  follows from winding-direction projection, and the mass
  spectrum is preserved.  The tilt picture is equivalent
  to KK at this level but provides a cleaner physical
  interpretation.  α remains a free parameter (the tilt
  angle), consistent with the designer's-choice hypothesis.

- **Breakthrough**: The tilt angle θ is CONSTRAINED by the
  embedding geometry (e.g., by Ricci flatness or a
  topological condition).  This would derive α — contrary
  to the designer's-choice hypothesis, but a much bigger
  result.

- **Moderate result**: The tilt picture works qualitatively
  but differs quantitatively from KK (different functional
  form, different ghost mode behavior).  The two frameworks
  make different predictions, opening testable differences.

- **Null result**: The tilt picture is mathematically
  equivalent to KK (just a coordinate transformation).
  No new physics, but clarifies interpretation.
