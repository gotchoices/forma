# metric-charge / work

Exploratory documents for hypotheses being tested before they qualify
for chapter-level material. Per project convention
([forma CLAUDE.md](../../../CLAUDE.md)): if things are unclear,
develop working hypotheses in a work folder.

The trigger for this folder was the recognition that metric-charge's
main arc was developed in production mode without an exploratory
buffer, and that adding a 2D harmonic-oscillator bridge (parallel to
[metric-mass Ch 9](../../metric-mass/09-harmonic-oscillator-bridge.md))
would benefit from being worked through informally first.

## Current explorations

- **[ho-bridge-2d.md](ho-bridge-2d.md)** — 2D harmonic-oscillator
  bridge for metric-charge. Translation table for the (m, n) mode
  family, U(1)×U(1)/SU(2) symmetry analysis at the isotropic point
  ε = 1, coherent-state knot framing, and tests of two physical
  reframings (incremental mass, charge-requires-prior-mass) against
  the Chapter 2 derivation. Candidate for a follow-up appendix to
  metric-charge.

- **[angular-momentum-as-mass.md](angular-momentum-as-mass.md)** —
  Formalize "standing-wave momentum around a compact loop is
  quantized angular momentum, viewed externally as rest mass."
  Decide whether the reframing belongs as a back-edit to
  [metric-mass Chapter 2](../../metric-mass/02-mass-from-u.md), as a
  paragraph in the metric-mass Ch 9 HO bridge, as part of the
  prospective metric-charge HO bridge, or in more than one of those
  places.

- **[higher-order-charges.md](higher-order-charges.md)** —
  Forward-looking extension to N compact directions. SU(N) at full
  isotropy as the natural geometric candidate for color (N = 3); why
  baryon number probably belongs to a different (winding-count)
  mechanism. Not appendix-grade; aimed at later work in ma-domain
  and [metric-binding](../../metric-binding/).

- **[per-arc-curvature-as-charge.md](per-arc-curvature-as-charge.md)** —
  Bridge that grounds sheet-proton's per-arc fractional charge reading
  (Q_lobe = +2/3, Q_saddle = −1/3 from integrated geodesic curvature)
  in the framework's existing charge mechanism, under one explicit
  working hypothesis **G1**: the continuum-limit normal-E-field leakage
  density along a curve on a bent surface equals (1/2π) κ_g. Carries
  G1 in the same pattern that ch. 8 §7 carries k as input and metric-
  mass ch. 9 carries the HO bridge as translation. With G1 the chain
  runs through cleanly (Steps 1–5): per-arc Q_i is a real local charge
  contribution; sign tracks convex/concave; per-arc fractions sum to
  integer closed-loop totals by Gauss–Bonnet; standalone fractions
  forbidden but locally probable to short-wavelength probes; long-
  wavelength probes see only the integer monopole. Aligns structurally
  with ch. 8 §7's per-knot reading as complementary axes of the same
  confinement principle. The 2026-05-25 broader survey found that
  grid/ already supports G1 for the uniform-circulation case
  (charge-emergence.md L96 — 2π wrap = unit charge; F12 §F2 —
  Gauss–Bonnet on the lattice; F12 §F3 and T12 — charge per radian =
  e/(2π) as operational premise). **The remaining gap is locality** —
  extending the per-radian density pointwise to curves with varying
  κ_g. Two promotion routes identified: discrete-lattice locality work
  in grid-primitive, or a lighter Berry-phase / holonomy route that
  may close locality automatically from differential-geometric
  structure.

## Status convention

Each file ends with an explicit **Status** block stating whether
the exploration is ready to become chapter-grade material, needs
further work, or should land somewhere other than where this folder
sits.
