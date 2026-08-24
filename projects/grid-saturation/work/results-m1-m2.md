# Cylinder sim — first results (M1 verified; M2 negative-so-far)

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

## M2 — pair production (energy S → c): **negative so far, three solid findings**

The goal: drive two photons head-on into saturation and see whether energy
transfers into a **persistent** compact (n≥1) mode — a particle at rest. What
the runs actually established, in order of how they corrected each other:

1. **Symmetry must be broken — and the seed cannot ride the beam.** A perfectly
   c-uniform collision makes *zero* compact structure (symmetry forbids it). An
   early run with a c-structured *source* seed (`--cseed`) seemed to show
   spillover growing the compact fraction by +0.8% while clip did not — but that
   was an **artifact**: the n≥1 seed is **gapped and does not co-propagate**
   with the n=0 photon (exactly the KK decoupling M1 verified), so it **stays at
   the source** and never reaches the collision. Interior (collision-region)
   E(n≥1) was ~0 (machine epsilon) the whole time. **The symmetry-breaking must
   be present *at* the collision** — which is physical: real pair production is
   seeded by **vacuum fluctuations**, not carried in on the beam. (Added
   `--zpe`: a vacuum-noise field on every edge.)

2. **Head-on does not raise the per-edge amplitude.** Counter-propagating
   photons occupy *different directed edges* (+x vs −x), so per-edge saturation
   triggers at nearly the same amplitude for one photon as for two. The
   collision's specialness lives in the **node** (larger scatter sum T), not on
   any single edge — so there is no clean "single-below / collision-above"
   bound. The right test is **saturated vs linear control at identical
   parameters**, differencing out everything the saturation didn't cause.

3. **With a vacuum seed, saturation does NOT pump a trapped mode — at any tested
   frequency.** Control (`--sat none`) vs `clip` vs `spillover`, same seed,
   bound driven well into saturation (lost ≈ 17): interior E(n≥1) after the
   photons exit is **identical across all three** (retained ≈ 81% — but that
   81% is just the **static vacuum-noise floor**: gapped n≥1 modes don't
   propagate, so the noise *sits still*; it is **not** a created particle). A
   frequency sweep (ω = 0.2 … 1.4, same-seed differencing so the floor cancels)
   gives `spillover − control` ≈ **0 to slightly negative everywhere** — no
   resonance, no trapping. Saturation redirects/loses energy per tick, but the
   **linear scatter re-mixes c-edge energy back toward x on the next tick**, so
   nothing accumulates into the compact sector.

### What this means (non-dogmatically)

- **The n≥1 sector exists and is stable** — the vacuum floor persists because
  n≥1 is a gapped, non-propagating eigenmode of the scatter. **A trapped
  particle *could* live there.** The good news is real.
- **What's missing is a *pump*.** Clip and spillover are *per-edge, per-tick*
  responses; they do not phase-lock energy into the stable n≥1 eigenmode, and
  the linear scatter undoes their redirection each tick. Pair production needs a
  nonlinearity that **coherently pumps** the compact eigenmode, which these two
  do not provide.
- This is **"not yet," not "refuted."** The thesis (saturation → S→c transfer →
  a rest particle) is intact; the specific *clip/spillover* realizations don't
  pump. The obstruction is named and concrete.

### Honest caveats

- Only two saturation models tried (clip, spillover); **storage/temporal** and
  **node-state** nonlinearities are untested.
- The frequency sweep varied the *photon* ω; the true resonance may involve the
  c-circumference (nc), amplitude, and pulse shape jointly — a wider space.
- `--quantize` (discrete levels as the symmetry-breaker / trap) is untested.

## Next steps

1. **Directly excite an n≥1 mode at high amplitude** (the `winding` scenario)
   and ask the simpler precursor question: under saturation, is a compact mode
   **stable as a particle**, and does it stay put? (Tests the *trap* before the
   *pump*.)
2. **Build a pump:** a saturation response that couples n=0 → n≥1 **coherently**
   — e.g. a **storage/temporal** node (release phase-locked to the compact
   eigenmode), or an explicit **node-state mode-coupling** term. Re-run the
   control-differenced collision.
3. **Widen the resonance search:** sweep nc and amplitude jointly, not just ω.
4. **Quantization as trap:** run `--quantize 2` (±1) and larger — does
   discreteness itself pin energy into a compact level?
5. Only if a pump is found: **momentum & pair check** (zero net x-momentum;
   ±winding = particle/antiparticle).
