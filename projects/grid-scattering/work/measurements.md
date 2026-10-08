# Measurements — cylinder arena, conserving rule

**Script:** [`../scripts/cylinder.py`](../scripts/cylinder.py). All runs below are reproducible from the command lines given. Supersedes [first-run.md](first-run.md), whose results are withdrawn.

Rule: product cylinder; x-group and c-group exchange nothing below the ceiling; above it an exactly energy-conserving rotation moves the excess across, in both directions. Local (every node tests its own totals) — the earlier non-local `--one-point` argmax is off by default, being both a departure from GRID locality and a suppressor of the effect it was meant to enable.

**Metric.** Compact-register energy with k_c ≠ 0, divided by total register energy. Both compact registers are kept and Parseval's 1/nc applied, so the fraction cannot exceed 1. An earlier metric used only f₊c + f₋c without normalisation, which discarded half the compact state and produced "fractions" above 1.

---

## M1 — Energy audit

`cylinder.py` audits `step()` on a random probe at start-up.

```
step() energy audit: 3843.587846 -> 3843.587846   drift 1.18e-16
```

The rule is exactly conserving. This is the condition the project's own Appendix G requires before any transfer claim, and it was not met by the superseded arena.

## M2 — Baselines

| run | command | winding energy |
|---|---|---|
| no drive, no background | `--no-drive --zpe 0` | exactly 0 |
| drive, below ceiling | `--cw --sat 0` | exactly 0 |
| background off, drive on | `--cw --zpe 0` | exactly 0 |

The last is the equivariance check: with a perfectly c-symmetric state and a c-symmetric rule, no winding can appear. The symmetry is broken by the **state** (the background), never by the rule.

## M3 — Resonance

`--cw --nc N --seed S`, drive wavelength λ = 24 nodes. Winding energy as a fraction of total:

| nc | nc/λ | seed 1 | seed 2 | seed 3 | mean |
|---:|---:|---:|---:|---:|---:|
| 20 | 0.83 | 0.0067 | 0.0058 | 0.0065 | 0.0063 |
| 22 | 0.92 | 0.0077 | 0.0126 | 0.0062 | 0.0088 |
| **24** | **1.00** | **0.0503** | **0.0641** | **0.0215** | **0.045** |
| 26 | 1.08 | 0.0077 | 0.0185 | 0.0168 | 0.0143 |
| 28 | 1.17 | 0.0073 | 0.0050 | 0.0066 | 0.0063 |

**Resonance is real at roughly 5×**, at the predicted circumference, with substantial seed-to-seed scatter (a 3× spread at nc = 24). It is not the 50–100× previously claimed; those figures came from a lossy rule whose losses were largest off-resonance.

Enough to establish that the ring selects, not yet enough to gate a threshold. More seeds and a width measurement are owed.

## M4 — Motion: the negative result

Two tests, both with the reverse channel active.

**A ring excitation at rest, no drive.** Seeded as a standing wave on one ring, at amplitudes from below the ceiling to twelve times it. Compact energy leaks away (e.g. 96 → 58 over 300 ticks at amplitude 2.0) but the **x-centroid does not move: 0.0000 in every case.** The excitation radiates symmetrically into ±x and decays in place.

**A ring excitation launched with x-momentum** — the "angled shot", compact content and +x content seeded together at the same nodes:

| ring amp | x amp | compact centroid | x centroid |
|---:|---:|---:|---:|
| 0.5 | 0.0 | 0.00 | 0.00 |
| 0.5 | 0.5 | **0.00** | **41.26** |
| 0.5 | 2.0 | 5.94 | 32.37 |

**The two parts shear apart.** The x content travels at roughly one node per tick and leaves; the compact content stays. The small compact drift in the third row is overflow depositing energy downstream as the x pulse passes, not a bound object translating — compact energy *grows* there (113 → 262), so it is being pumped, not carried.

**A particle made in this arena cannot move through space.**

---

## M5 — The gradient coupling: motion, with light still massless

Added after the park. The rule: the x↔c rotation angle is **g·(1 − cos k_c)** — a second difference along the compact direction, so it is exactly zero for a field that does not wind. A *constant* rotation (the earlier `--theta`) is a mass term and gives light a gap equal to the angle; a coupling carrying a c-difference is a *derivative* coupling and does not.

Energy audit with the coupling on: drift **3.55 × 10⁻¹⁶**.

### Dispersion, measured from a 4096-tick time series against exact Bloch

| n | k_x | ω simulated | ω exact (both branches) |
|---:|---:|---:|---|
| 0 | 0.0000 | 0.0000 | 0, 0 |
| 0 | 0.2945 | 0.2945 | 0, 0.2945 |
| 0 | 0.5890 | 0.5890 | 0, 0.5890 |
| 1 | 0.0000 | 0.0353 | 0.0350, **0.2968** |
| 1 | 0.2945 | 0.3820 | 0.1746, **0.3817** |
| 2 | 0.0000 | 0.7378 | 0.2139, **0.7375** |

Simulation and analysis agree to ~3 × 10⁻⁴.

**Light is exactly massless.** At n = 0 the frequency equals \|k_x\| to every digit, at every wavenumber. No gap.

**Wound modes have a rest frequency.** The upper branch at k_x = 0 gives ω₀ = 0.2968 (n = 1), 0.7375 (n = 2), 1.3329 (n = 3) — a mass tower.

**The dispersion is relativistic.** Against √(k_x² + ω₀²) on the upper n = 1 branch: 0.0%, 0.7%, 0.5%, −0.6% at k_x = 0, 0.03, 0.06, 0.10. Group velocity at k_x ≈ 0.07 is **+0.159** — between 0 and 1, which is what mass means.

### Two caveats, both real

**A second branch.** Each winding splits into two, a heavy one (the tower above) and a light one — ω = 0.0350 at n = 1, 0.2139 at n = 2. The random seed in the time-series run actually excited the light branch preferentially at k_x = 0. A nearly-massless wound state is not obviously wanted, and this is the same shape of problem as the unobserved-mode tower in [3-torus.md](../../ma-domain/work/3-torus.md). Unexplained.

**The rule is effectively, not strictly, local.** The coupling is applied in the c-Fourier basis where it is diagonal. Its real-space kernel decays quickly but is not finitely supported, so whether a genuine GRID node could implement it is open. And the angle was *chosen* to vanish at zero winding, so light staying massless is built in by design rather than derived — a legitimate design principle, but it should be read as one.

### What this does not yet show

A bound *packet* travelling has not been demonstrated. Three attempts failed on seeding — an arbitrary mixture excites both branches and interferes, and constructing a clean single-branch real packet on four registers defeated me. The dispersion above is nevertheless a direct property of the implemented rule, measured two independent ways, and a correct packet must follow it.

Saturation has not been run with the coupling on. All of the above is the linear sector.
