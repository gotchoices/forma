# Cylinder sim — first results (M1 verified, M2 preliminary)

Sim: [`../scripts/cylinder.py`](../scripts/cylinder.py) — a 1D-space × 1D-compact
(x, c) cylinder with the N=4 equal-impedance scatter. Photon = c-uniform
(n=0) wave in x; mass = c-winding (n≥1). Figures in [`../outputs/`](../outputs/).

## M1 — the linear baseline: **verified**

Ran single, head-on, and winding injections with `--sat none`:

- **Photons propagate in x** at ~0.62 nodes/tick (the N=4 scatter speed; cf.
  sim-maxwell's ~0.7 for N=3). ✓
- **Two photons pass through each other** cleanly (head-on, linear). ✓
- **The compact sector is decoupled:** a c-uniform photon keeps E(n≥1) = 0.0000%
  exactly — nothing leaks into the winding modes. ✓ (This is the KK-decoupling
  check, never run dynamically in forma before.)
- **The winding (n=1) mode is massive/gapped:** injected, it does *not*
  propagate in x like the photon (speed ≈ 0) — correct KK behaviour. ✓
- Edge energy (the orthogonal-scatter conserved quantity Σin²) conserves to
  ~3% over the interior window (residual from window edges / sponge; the linear
  scatter is exactly orthogonal).

**M1 stands:** the cylinder is a faithful testbed — Maxwell-like propagation
in x with a compact dimension present, and the compact modes are decoupled and
gapped exactly as KK predicts.

## M2 — pair-production signal (energy S → c): **preliminary, two real findings**

Head-on collisions driven into saturation (`--sat clip|spillover`, amp above
the bound so the collision clips):

1. **Symmetry must be broken.** A *perfectly c-uniform* collision (`--cseed 0`)
   produces **exactly zero** compact structure even under heavy saturation —
   symmetry forbids it. Trapping into a c-structured mode requires a
   symmetry-breaking seed (c-structure, ZPE noise, or quantization to discrete
   c-levels). This is a genuine, clean result — not a failure — and it names
   what the mechanism needs.

2. **Spillover traps; clip does not.** With the seed on (`--cseed 0.3`), the
   **spillover** node (excess on a saturated edge redistributed to edges with
   headroom) **grows the compact-structure fraction by +0.7%** over the
   collision, while the lossy **clip** node grows it by **0.0%**. This is the
   predicted mechanism distinction: energy-*redirecting* saturation moves energy
   into the compact mode; energy-*discarding* saturation just loses it. The
   sign of the effect is right.

### Honest caveats on M2

- **Injection also saturates** at the parameters used (amp above bound at the
  source), muddying the pre-collision baseline. A clean run needs the single
  photon *below* the bound and only the *collision* above it — a tuning pass.
- **The effect is small (+0.7%)** and its *stability* is untested: whether the
  trapped c-structure **persists** as a standing wave (a particle) or **leaks
  back** into x is the real M2 question (threshold/resonance), not yet measured.
- The **c-edge energy Ec** is *not* a clean compact diagnostic — the isotropic
  4-way scatter puts ~50% of a photon's energy on the c-edges. The clean signal
  is the c-**structure** E(n≥1); use that.
- **spillover is a first model**; its exact energy-conservation is approximate
  (tracked, not proven). A properly energy-conserving spillover/storage node is
  the construction to nail.

## Next steps

1. **Tune the M2 amplitudes** so only the collision saturates (clean baseline),
   and add a **symmetry-breaking source** (ZPE noise and/or `--quantize`) rather
   than a hand-set `--cseed`.
2. **Measure persistence:** after the collision, does the c-structure survive
   (a particle) or decay back to x (transient)? Sweep the collision energy for a
   **threshold/resonance** (energy matching a c-eigenmode).
3. **Momentum & pair check:** confirm the trapped mode has ≈ zero net x-momentum
   (rest particle) and look for the ±winding (particle/antiparticle) split.
4. **Base-2 vs 8-bit:** run `--quantize 2` (±1) vs larger to see whether the
   *discreteness* itself provides the symmetry-breaking / trapping.
5. **Energy-conserving spillover/storage:** build the properly-conserving node
   so a real S→c *transfer* (not clip-loss) can be measured cleanly.
