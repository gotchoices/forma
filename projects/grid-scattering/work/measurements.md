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
