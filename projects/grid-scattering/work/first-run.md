# First run — RESULTS WITHDRAWN

> **Withdrawn 2026-10-07.** Everything measured in this file used an overflow
> rule that moved amplitude rather than energy. An external audit found it
> destroys 80–145 units of energy per run — more than the rings and the line
> hold together — and destroys **most where there is no resonance**. The
> headline ratios (50–100× at resonance, 12–58× over detuning) were therefore
> reading differential dissipation between the two arms being compared, not
> selection. This is the same selective-dissipation artifact recorded in
> [../Appendix.md](../Appendix.md) §E, and the project's own §G rule should
> have caught it.
>
> The arena was also wrong: a comb (one x line with a ring hung off each
> position at a fixed point) rather than the cylinder the framing describes.
> It gave every ring a privileged attachment point, breaking the translation
> symmetry along c whose conserved quantity is the winding, and left ring nodes
> with no x-edges, so nothing made there could travel.
>
> Re-measured on the cylinder with an exactly conserving rotation: transfer and
> one-point circulation hold up; **resonance survives at about 1.5×, not
> 50–100×**. See [../README.md](../README.md) §3. The script this file refers to
> has been replaced by [../scripts/cylinder.py](../scripts/cylinder.py).
>
> Kept for the record, and because the two bugs at the bottom are still worth
> knowing.

**Script:** `line_and_ring.py`, since deleted; replaced by [`../scripts/cylinder.py`](../scripts/cylinder.py)
**Status:** First real result. The mechanism transfers, the transfer is **resonant**, the resonance selects the predicted mode, and at the strongest resonance the reverse channel fires on its own.

---

## The topology, and the correction that made it work

The first attempt built the arena as an (nx × nc) grid. That is wrong, and the wrongness is instructive: an (nx × nc) grid is **nc parallel x-lines**, so a photon spread across them saturates every ring at once. The injection is then uniform all the way round each ring — winding 0, no circulation, no particle. Measured: 99.4% of transferred energy landed in the non-circulating mode.

The arena is instead **one** linear array x, with a **ring at every x coordinate**, each ring its own array of nodes. Line and ring are not connected; they connect only during an overflow, at a single point. With that fixed, ~89% of transferred energy circulates, with no seed needed — injecting at one point of a ring is inherently non-uniform, so the symmetry breaking is built into the topology rather than imported.

## Result 1 — the mechanism transfers

A sustained drive from both ends of the line, colliding at the midpoint. Peak |T| at the collision is 1.0000 against a ceiling of 0.8, so the collision and only the collision saturates: a single pulse reaches 0.5.

Energy crosses onto the ring. With no drive, or with the ceiling disabled, the ring stays at exactly zero.

## Result 2 — the transfer is resonant, and the resonance is sharp

Drive wavelength 12.0 nodes. A ring of nc nodes has a round-trip of nc ticks, so successive injections should add in phase when nc is a whole multiple of the wavelength.

| nc | nc/λ | ring energy |
|---:|---:|---:|
| 11 | 0.917 | 1.50e−02 |
| **12** | **1.000** | **1.26e+00** |
| 13 | 1.083 | 1.41e−02 |
| 18 | 1.500 | 2.68e−03 |
| 23 | 1.917 | 2.10e−02 |
| **24** | **2.000** | **1.44e+00** |
| 25 | 2.083 | 3.68e−02 |
| 35 | 2.917 | 2.16e−02 |
| **36** | **3.000** | **9.67e−01** |

Roughly **50–100× enhancement** at integer ratios, and one node either side kills it: nc = 23 → 0.021, nc = 24 → 1.44, nc = 25 → 0.037. Half-integer (nc = 18) does nothing. The forward event count is essentially the same (~13 800) in every case, so the *injection* is constant and the difference is entirely whether it accumulates coherently.

**This needs a periodic drive.** A single Gaussian pulse injects once and the ring simply holds it: ring energy was identical (2.3021e−02) at every circumference from 8 to 40, because there is no second injection to interfere with the first. Resonance is a property of sustained driving, not of a single collision.

## Result 3 — the resonance picks the predicted mode

| nc | expected n = nc/λ | strongest mode |
|---:|---:|---|
| 12 | 1 | **n = 1** (8.11e+00) |
| 24 | 2 | **n = 2** (1.54e+01) |
| 36 | 3 | **n = 3** (1.55e+01) |

Exactly the fit condition: the ring takes up the mode whose wavelength divides the circumference, and nothing else does.

## Result 4 — the reverse channel fires at the strongest resonance

At nc = 12: **1181 ring → line events.** The ring accumulated enough for its junction node to breach the ceiling and dump back into the line, with no separate rule added. This is the decay half of the mechanism operating on its own.

It is marginal, though — nc = 24 produced a single reverse event and nc = 36 none. The channel opens only at the strongest resonance.

## Caveats

- **The scatter-rule discriminator has not been re-run on this arena.** On the superseded grid topology, grouped registers gave exactly 0 c-content below the ceiling where the pooled N = 4 rule gave 3.5e+01 — a clean A/B. It needs repeating here, with a pooled junction node as the control arm, before it can be cited for this topology.
- **The ring is lossless**, so persistence is automatic and says nothing. The meaningful quantity is the build-up, not the retention.
- **Energy drift is not yet reported.** The background jitter is off by default now, so it is measurable — but the script does not print it.
- **Only one drive wavelength** has been tested. The resonance condition should be checked by holding nc fixed and sweeping ω.

## Bugs found and fixed

- **Odd launch separation.** With nx = 200 and pad = 30 the pulses were 139 nodes apart and crossed *between* nodes, never coinciding; nothing ever saturated. The script now reports peak |T| against the ceiling and warns on odd separation.
- **The N = 2 pooled formula is a swap, not a pass-through.** `S = (2/N)J − I` at N = 2 gives out[0] = in[1], which in direction-of-travel labelling is reflection. Pass-through is out[d] = in[d]. Same convention trap as the grid-matter three-axis scatter error — a formula carried from the pooled convention into a direction-labelled one.

## Next

1. Re-run the pooled-versus-grouped discriminator on this arena.
2. Hold nc fixed and sweep ω, to confirm the condition is nc = mλ rather than a coincidence of the sizes chosen.
3. Report energy drift, now that it is measurable.
4. Drive harder, or pick nc = 12, to exercise the reverse channel properly and see whether the ring empties in quanta or continuously.
