# Simulation result — the falloff + isotropy leg passes

**Status:** Result note. Records the go/no-go simulation for the falloff and
isotropy half of the gate ([congestion-falloff.md](congestion-falloff.md),
[update-rule.md](update-rule.md)). The dispersion half is a separate
wave-propagation measurement, not covered here.

Reproduce: `../scripts/gate_falloff.py` (defaults, plus the runs below).
Figure: [`../outputs/gate_falloff.png`](../outputs/gate_falloff.png).

---

## What was run

The candidate mechanism as a **lossless, finite-bandwidth, conservative
transport** on a 2D triangular ("hex", 6-neighbour) lattice:

- conserved scalar s on nodes (the backlog; the proper-time field q ∝ s);
- edge flow = clip(κ·(s_i − s_j), −μ, μ) — linear diffusion below the
  bandwidth μ, **saturating** where the demanded flow exceeds μ (this is
  the congestion nonlinearity);
- persistent point injection S at the centre (the mass);
- absorbing boundary s = 0 (the only sink — no bulk loss, i.e. lossless).

Runs: radius 60 and 100 cells; κ = 0.2; μ = 0.05 (so total core drain
6μ = 0.30); S = 0.05 … 0.28. S = 0.28 drives the core **into saturation**
(near 6μ) while still converging — the informative nonlinear case.

## Results

| Quantity | r = 60 | r = 100 | Reading |
|---|---|---|---|
| log-fit R² (massless, s vs ln r) | 1.00000 | 1.00000 | straight line ⇒ **massless** (log r in 2D ↔ 1/r in 3D) |
| exp-fit R² (screened Yukawa) | 0.994 | — | worse ⇒ not screened |
| slope (∝ source) | −0.129 | −0.129 | scale-independent; ∝ S as a potential should be |
| 6-fold hexagonal anisotropy / field | 0.0023 | 0.0022 | **isotropic** (~0.2%) |
| non-radial residual RMS / field | 0.029 | 0.037 | discrete-node scatter, not coherent |

Convergence: max node change < 1e-6; centre value bounded (0.79, 0.87).

## What this establishes

1. **Massless, not Yukawa.** s vs ln r is a perfect straight line
   (R² = 1.00000) across the mid-range at two system sizes. A screened
   field would curve downward; it does not. This is the numerical form of
   the shunt-check result — lossless ⇒ no shunt ⇒ massless ⇒ 1/r-family.
2. **The nonlinearity does not screen.** Even with the bandwidth cap
   binding in the core (S ≈ 6μ), the far field is a clean log r. The
   saturated core acts only as a renormalised source — exactly the
   near-field-modified / far-field-massless prediction of
   [shunt-check.md](shunt-check.md) §3, now confirmed at full nonlinearity
   rather than at leading order.
3. **Isotropic on the hex lattice.** Genuine 6-fold anisotropy is ~0.2% of
   the field and does not grow with system size — the triangular lattice's
   6-fold symmetry gives an isotropic potential, as required. (The earlier
   6.75% "anisotropy" was radial variation within a finite annulus, an
   artifact of the metric, not physics.)

## Honest limits

- **Diffusive transport was built in, not tested.** The model *assumes*
  J ∝ −∇s (flow down the gradient). What was genuinely open and is now
  answered: whether the bandwidth **nonlinearity screens** (it does not)
  and whether the **hex lattice stays isotropic** (it does). Whether the
  real GRID substrate's congestion is diffusive-conservative remains the
  modeling commitment of [local-time.md](local-time.md), not something a
  transport sim can prove.
- **2D, and a proxy field.** The run is 2D (log r); the 3D substrate gives
  1/r by the same Green's-function argument (dimensionality changes the
  exponent, not the massless-vs-screened distinction the gate tests). s is
  the backlog, taken ∝ the delay q; a transit-time measurement would be the
  direct observable.
- **Dispersion untested here.** Non-dispersivity
  ([congestion-falloff.md](congestion-falloff.md) §6) needs wave
  propagation, not diffusion — a separate sim.

## Verdict

The **falloff + isotropy leg of the gate PASSES**: massless (1/r-family),
isotropic, and unscreened by the bandwidth nonlinearity. The remaining
go/no-go is the **dispersion leg** (is the load-dependent slowing uniform
across frequency?). Passing that clears the gate and opens Objective 2
(the coefficient → G = 1/(4ζ)).
