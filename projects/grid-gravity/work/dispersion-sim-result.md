# Simulation result — the dispersion leg passes (via losslessness)

**Status:** Result note. Records the go/no-go for the dispersion half of the
gate ([congestion-falloff.md](congestion-falloff.md) §6,
[local-time.md](local-time.md) Commitment 3). Together with
[falloff-sim-result.md](falloff-sim-result.md) it clears the gate.

Reproduce: `../scripts/gate_dispersion.py`.
Figure: [`../outputs/gate_dispersion.png`](../outputs/gate_dispersion.png).

---

## What was run

A wavepacket of centre frequency ω is driven through a loaded region and its
group delay is measured against a free run. Two edge models, side by side,
because the answer depends on the edge's character:

- **Lossy edge** — a leaky integrator u_i(t+1) = (1−a)u_i + a·u_{i−1}, a < 1:
  a finite-bandwidth edge *with loss*.
- **Lossless edge** — an energy-conserving wave u_tt = c(x)²u_xx with c
  tapered below 1 in the loaded region: a slowing *without loss*.

## A methodological caveat, handled

The leapfrog scheme carries its own **numerical (lattice) dispersion** at
short wavelengths, which masquerades as physical dispersion. Two controls
confirm and remove it:

- Raising the Courant number 0.5 → 0.95 (toward the 1D dispersion-free
  limit) collapsed the lossless delay's apparent frequency-spread from
  **38.5% → 7%** — proving the high-ω rise was numerical, not physical.
- Restricting to the **well-resolved band** (ω ≲ 0.25, ≳ 25 cells per
  wavelength) removes the residual.

Results are read in that well-resolved band.

## Results (well-resolved band, ω ≈ 0.04–0.26)

| | Lossy edge (a=0.6) | Lossless edge (c=0.6) |
|---|---|---|
| Transmission vs ω | **collapses** 0.76 → 0.003 | **≈ 1.0** (flat) |
| Group delay | measurable only in a vanishing passband | **flat ≈ 208 ticks** (±~2%) |
| Reading | strongly low-pass ⇒ **dispersive** | pure delay ⇒ **non-dispersive** |

(One peak-detection outlier at ω=0.12 inflates the reported spread to
~13%; the genuine variation across the band is ~2%.)

## What this establishes

1. **A lossless slowing is non-dispersive.** The lossless edge keeps
   transmission at unity (no attenuation) and delays every frequency by the
   same ~208 ticks — a uniform time-rescaling, which is exactly time
   dilation, not an optical medium.
2. **Dispersion is a symptom of loss.** The lossy edge disperses precisely
   because it attenuates (a low-pass). The dispersion is not intrinsic to
   "slowing"; it enters through the loss.
3. **Both gate conditions reduce to one commitment.** Losslessness was
   already required for the 1/r falloff ([shunt-check.md](shunt-check.md):
   shunt ⟺ loss ⟺ Yukawa). It is *also* what buys non-dispersivity here
   (loss ⟺ low-pass ⟺ dispersion). The single **lossless** commitment
   delivers both a massless 1/r field *and* a non-dispersive slowing.

## Honest limits

- **The lossless model realizes the slowing as a uniform reduced c**, which
  is non-dispersive by the continuum wave equation — so that half is partly
  by construction. What the sim genuinely shows is the *contrast*: the lossy
  realization disperses (transmission collapse, not built in), and
  losslessness (unit transmission) coexists with a flat delay once the
  numerical artifact is controlled.
- **1D, and a leapfrog scheme** whose numerical dispersion had to be
  managed; the physical (continuum) statement is the robust one.
- **Whether GRID's congestion realizes losslessly** (reduced-c / pure
  delay) rather than as a lossy filter is the same modeling commitment as
  before — now shown to control *both* gate conditions, not just the
  falloff.

## Verdict

The **dispersion leg PASSES**, conditional on losslessness: a lossless
congestion slowing is non-dispersive (time dilation), while a lossy one
disperses (optical medium). With the falloff + isotropy leg
([falloff-sim-result.md](falloff-sim-result.md)) this **clears the gate** —
both legs resting on the single losslessness commitment. Next: Objective 2,
the coefficient → G = 1/(4ζ).
