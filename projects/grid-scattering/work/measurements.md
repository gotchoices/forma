# Measurements — grid-scattering

Every run below is reproducible from the command line given, with
[`../scripts/cylinder.py`](../scripts/cylinder.py). Framing:
[../README.md](../README.md). Checklist: [STATUS.md](STATUS.md).

**Arena.** A cylinder: one extended direction x, one compact direction c, as a
product lattice. Four registers per node — `+x`, `−x`, `+c`, `−c`. Rings at
neighbouring x are joined along x, so anything made on a ring can travel.

**Two sectors, kept apart throughout.**

- The **linear sector** is the ordinary GRID scatter `S = (2/N)J − I` pooled over
  all four registers (`--linear pooled`, the default). It is what carries a
  mode once it exists.
- The **nonlinear sector** is this project's posit: where a register group's
  total `|T|` exceeds the ceiling `--sat`, the excess rotates between the x and
  c register pairs. This is the only channel that moves energy *between* the
  sectors.

**Energy metric.** Compact-sector energy is Parseval-normalised FFT power over
both compact registers. "Winding" means the `k_c ≠ 0` part — the part that
circulates. `k_c = 0` is uniform around the ring and carries no winding.

---

## M1 — The rule conserves energy exactly

```
python3 scripts/cylinder.py --nc 24 --omega 0.1849 --amp 1.0
```

A random probe through one full tick (scatter, overflow, propagate):

| quantity | value |
|---|---|
| energy in → out | 3844.939854 → 3844.939854 |
| relative drift | **1.2 × 10⁻¹⁶** |

The crossing is an orthogonal rotation of register pairs, so this is exact by
construction rather than by tuning. It accounts for whatever the ring already
holds. **An earlier rule moved *amplitude* instead**, which destroyed energy on
every overflow — most of it off resonance — and corrupted a whole round of
measurements, including a reported 50–100× resonance. All of that is withdrawn.

## M2 — The linear sector moves nothing across, at any amplitude

With the ceiling off, so the overflow channel is dead, and the background off,
so nothing but the drive is present. The drive is uniform around c, i.e. pure
`k_c = 0` — unwound, a photon.

```
for a in 0.5 1.0 2.0 4.0 8.0; do
  python3 scripts/cylinder.py --nc 24 --omega 0.1849 --amp $a --sat 0 --zpe 0
done
```

| drive amplitude | 0.5 | 1.0 | 2.0 | 4.0 | 8.0 |
|---|---|---|---|---|---|
| winding energy | **0** | **0** | **0** | **0** | **0** |

Exactly zero — not small, zero — however hard the drive is pushed. This is not
a property of the posit; it is forced. On a translation-invariant lattice `k_c`
is a Bloch label, so **no** linear rule mixes `k_c = 0` with `k_c ≠ 0`, the
pooled scatter included.

**This is why the linear half of the original posit is withdrawn.** It claimed
that keeping space and a sheet from exchanging below the ceiling was a
distinguishing choice. It is not a choice at all. The posit now says something
about the **nonlinear channel only** (§M4).

## M3 — The linear sector already gives Kaluza–Klein motion

Exact Bloch spectrum of one tick. The closed form is
`cos Ω = (cos k_x + cos k_c)/2`, giving a lattice light speed `c = 1/√2`.

```
python3 scripts/cylinder.py --bloch --nc 24 --n 1
```

At `nc = 24`, winding `n = 1`, rest frequency `Ω₀ = 0.184855`:

| k_x | −0.30 | −0.20 | −0.10 | 0.00 | +0.10 | +0.20 | +0.30 |
|---|---|---|---|---|---|---|---|
| Ω | 0.2815 | 0.2329 | 0.1980 | 0.1849 | 0.1980 | 0.2329 | 0.2815 |
| error vs √(c²k² + ω₀²) | 0.1% | 0.1% | 0.0% | 0.0% | 0.0% | 0.1% | 0.1% |

| | |
|---|---|
| even in k_x | **exactly** — Ω(−0.1) = Ω(+0.1) = 0.197985 |
| group velocity at k_x = 0 | **+0.00000000** — a mode at rest is at rest |
| light (`k_c = 0`) | Ω = 0.0000, 0.0707, 0.2117 at k = 0, 0.1, 0.3 — **massless**, speed 1/√2 |
| mass tower, n = 1, 2, 3 | 0.1849 / 0.3681 / 0.5480 — ratios 1 : 1.99 : 2.96 |

A single-branch travelling packet confirms it dynamically. Each (k_x, k_c)
carries a **conjugate pair** of eigenvalues with the same Ω and opposite group
velocity — a mode and its time-reverse — so the branch must be selected by the
sign of the eigenphase, not by frequency alone.

```
for k in -0.3 -0.2 -0.1 -0.05 0.05 0.1 0.2 0.3; do
  python3 scripts/cylinder.py --packet --nx 400 --nc 24 --n 1 --kx $k \
    --steps 300 --sat 0 --zpe 0 --amp 0.3
done
```

| k_x | −0.2985 | −0.2042 | −0.0942 | −0.0471 | +0.0471 | +0.0942 | +0.2042 | +0.2985 |
|---|---|---|---|---|---|---|---|---|
| v measured | −0.535 | −0.424 | −0.236 | −0.123 | +0.123 | +0.236 | +0.424 | +0.535 |
| vs KK `c²k/Ω` | +0.6% | −2.6% | −1.4% | −1.6% | −1.6% | −1.4% | −2.6% | +0.6% |

Antisymmetric in k_x, within 2.6% of Kaluza–Klein everywhere, energy conserved
to all printed digits. A long run at one (k_x, k_c), seeded with a single branch's eigenvector,
confirms the spectrum dynamically:

```
for k in 0.0 0.1 0.2 0.3; do
  python3 scripts/cylinder.py --timeseries --nc 24 --n 1 --kx $k --steps 8192
done
```

| k_x | 0.0 | 0.0982 | 0.1963 | 0.2945 |
|---|---|---|---|---|
| Ω measured | 0.1848 | 0.1979 | 0.2316 | 0.2784 |
| Ω exact | 0.1849 | 0.1975 | 0.2314 | 0.2786 |
| error | −0.01% | +0.18% | +0.12% | −0.08% |

A ring mode seeded at rest stays at rest:

```
python3 scripts/cylinder.py --seed-ring --nc 24 --n 1 --amp 0.5 --steps 400 --sat 0.8 --zpe 0
```

> centroid moved **+0.0000 nodes in 400 ticks**, with the overflow channel on.

**This result is not new to this project.** It is the ordinary pooled scatter,
and [grid-matter ch. 4](../../grid-matter/04-matter-waves-and-de-broglie.md)
measures the same thing. It is recorded here because the project spent three
rounds building bespoke couplings to obtain it, and the pooled rule gives it
for free while also being **node-local** and **reciprocal**, which none of the
bespoke rules were. See §M6.

## M4 — The nonlinear channel: a threshold, and a seed requirement

This is the project's own claim, and it reduces to two findings.

**It needs the ceiling.** Below the ceiling nothing fires and nothing crosses;
above it, winding appears. At `sat = 0.8`:

```
for a in 0.50 0.55 0.60 0.65 0.70 0.75; do
  python3 scripts/cylinder.py --nc 24 --omega 0.1849 --amp $a
done
```

| drive amplitude | 0.50 | 0.55 | 0.60 | 0.65 | 0.70 | 0.75 |
|---|---|---|---|---|---|---|
| overflow events | 0 | 0 | 76 | 328 | 1753 | 18050 |
| winding energy | 1.626 | 1.626 | 1.630 | 1.693 | 4.362 | 18.54 |

1.626 is the background floor, untouched. The channel switches on between
amplitude 0.55 and 0.60 — at the ceiling, as posited — and winding departs the
floor just above it.

**It needs a seed.** With the background switched off, the overflow channel
makes **no winding at all**, however hard it is driven:

```
for a in 1.0 2.0 4.0; do python3 scripts/cylinder.py --nc 24 --omega 0.1849 --amp $a --zpe 0; done
for a in 1.0 2.0 4.0; do python3 scripts/cylinder.py --nc 24 --omega 0.1849 --amp $a;          done
```

| drive amplitude | 1.0 | 2.0 | 4.0 |
|---|---|---|---|
| overflow events, no background | 55 176 | 475 512 | 1 041 480 |
| winding, no background | **0** | **0** | **0** |
| winding, with background | 28.4 | 207 | 2512 |

Over a million overflow events produce exactly zero winding. The reason is
**equivariance**: the drive is uniform around c, the overflow rule is itself
c-translation-invariant, and a symmetric state under a symmetric rule stays
symmetric exactly. Something has to break the ring's symmetry, and the
background is the only candidate present.

So the symmetry is broken by the **state**, never by the rule — which is what
keeps winding a conserved label. The background's *magnitude* has no meaning in
these units (§3a of the README), so this says the seed is **necessary**, not how
big the real one is.

## M5 — Resonance is refuted: the structure belongs to the box, not the ring

The project claimed the drive frequency must resonate with the ring, so that
each sheet would carry its own threshold set by its own circumference. It does
not hold.

The seed sets the background, which is the only thing breaking the ring's
symmetry (§M4), so **seed-to-seed scatter is the error bar on any resonance
claim**. A single frequency, eight seeds:

| | |
|---|---|
| wound/total at Ω = 0.1849, 8 seeds | 0.074 … 0.324 — a factor **4.4** |

That spread is as wide as the entire frequency sweep, which is why the earlier
three-seed figure could not support a claim either way. Sweeping with error bars:

```
python3 scripts/cylinder.py --nc 24 --amp 1.0 --seeds 8 \
  --sweep 0.06,0.10,0.14,0.1849,0.22,0.26,0.30,0.3681,0.42,0.48,0.5480,0.60
```

| Ω | 0.06 | 0.10 | 0.14 | **0.1849** | 0.22 | 0.26 | 0.30 | **0.3681** | 0.42 | 0.48 | **0.5480** | 0.60 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wound/total | 0.276 | 0.032 | **0.391** | 0.176 | 0.013 | 0.173 | 0.094 | 0.064 | 0.042 | 0.262 | **0.010** | 0.011 |
| sd (8 seeds) | 0.034 | 0.002 | 0.037 | 0.062 | 0.001 | 0.053 | 0.030 | 0.007 | 0.008 | 0.066 | 0.001 | 0.001 |

Bold columns are the mass-tower frequencies, where the peaks were predicted.
There is strong structure — a 40× range, far outside the error bars — but it is
**not at the tower**. The tower's `n = 3` frequency is the sweep's *minimum*.

The decisive test is to move one thing at a time. Changing the **ring** moves
the tower; changing the **box** does not:

```
python3 scripts/cylinder.py --nc 36 --nx 201 --amp 1.0 --seeds 6 --sweep <same>
python3 scripts/cylinder.py --nc 24 --nx 301 --amp 1.0 --seeds 6 --sweep <same>
```

| Ω | 0.06 | 0.10 | 0.14 | 0.1849 | 0.22 | 0.26 | 0.30 | 0.3681 | 0.48 | 0.5480 |
|---|---|---|---|---|---|---|---|---|---|---|
| nc = 24, nx = 201 (tower 0.185 / 0.368 / 0.548) | 0.276 | 0.032 | 0.391 | 0.176 | 0.013 | 0.173 | 0.094 | 0.064 | 0.262 | 0.010 |
| **nc = 36**, nx = 201 (tower 0.123 / 0.246 / 0.368) | 0.280 | 0.033 | 0.366 | 0.190 | 0.013 | 0.190 | 0.115 | 0.063 | 0.280 | 0.011 |
| nc = 24, **nx = 301** (tower unchanged) | 0.309 | 0.057 | 0.140 | 0.356 | 0.020 | 0.280 | 0.384 | 0.193 | 0.187 | 0.074 |

Changing the ring from 24 to 36 nodes moves every tower frequency by a third
and leaves the sweep **unchanged within error bars**. Changing the box from 201
to 301 nodes leaves the tower alone and moves everything. The structure is a
property of the **x-box** — the drive's standing-wave pattern between the two
injection points — and knows nothing about the compact dimension.

**Withdrawn:** the ~5× resonance (previously "settled"), the earlier 12–58% and
50–100× figures, and the inference built on them — that the threshold would land
at the particle's own mass scale automatically, and hence that an intense
optical laser makes no pairs because it misses the electron ring's resonance.
That argument has no measurement behind it in this arena.

**What remains of the frequency question.** Nothing here rules resonance *out*
as physics; it rules out this arena's apparent resonance as evidence for it. A
real test needs a geometry whose box modes do not sit in the same range as its
ring modes.

## M6 — Motion survives the nonlinear channel only in a narrow window

With the linear sector supplying correct KK motion (§M3), the question is what
the overflow does to a mode that is already moving. A wound packet at
`k_x = +0.2042`, where `v_KK = +0.43495`, with the ceiling at 0.8:

```
for a in 0.6 0.7 0.8 0.9 1.0 1.2; do
  python3 scripts/cylinder.py --packet --nx 400 --nc 24 --n 1 --kx 0.2 \
    --steps 300 --sat 0.8 --zpe 0 --amp $a
done
```

| amplitude | 0.6 | 0.7 | **0.8** | 0.9 | 1.0 | 1.2 |
|---|---|---|---|---|---|---|
| overflow events | 0 | 0 | **6 292** | 66 090 | 127 836 | 243 816 |
| v / v_KK | 0.974 | 0.974 | **0.974** | 0.605 | 0.207 | **0.000** |
| v / v_KK, ceiling off | 0.974 | 0.974 | 0.974 | 0.974 | 0.974 | 0.974 |

With the ceiling off the speed is amplitude-independent, as a linear rule
requires. With it on there is a **window** — amplitude ≈ 0.8 — where the
channel is live and motion is untouched. Above it the packet is **pinned**: by
amplitude 1.2 it does not translate at all, with energy still exactly conserved.
The overflow rotation angle depends on the local `|T|`, so at large amplitude it
acts as a strong amplitude-dependent local scatterer and localises what it
makes.

**A known defect of the overflow rule, with a bound.** The rotation pairs `+x`
with `+c` and `−x` with `−c`, the same non-reciprocal pairing that broke the
superseded gradient coupling (§M7). In the window it does no harm — the rule is
even in k_x to 5 × 10⁻⁵ — but in the pinned regime a residual asymmetry appears:

| amplitude | 0.8 | 0.9 | 1.0 |
|---|---|---|---|
| \|v(−k) + v(+k)\| | 0.00005 | 0.038 | 0.052 |

A reciprocal overflow, coupling each compact register to both x registers, is
the obvious next variant and has not been tried.

**So §M4's earlier flat negative — "a made particle does not translate" — is
superseded, and the replacement is narrower in both directions.** A wound mode
*does* move, correctly and exactly, but that is the linear sector's doing and
not this project's. What the project's own channel contributes is a threshold
above which it destroys the motion.

## M7 — Superseded coupling variants, kept for the record

Three attempts to supply motion before the pooled scatter was tried. All are
withdrawn; the script reproduces the third.

1. **A soliton bound by saturation at its core.** Contradicts the project's own
   ceiling calibration: by "light must pass", an electron's core sits *below*
   the ceiling.
2. **A constant rotation between the register groups.** Algebraically a *mass*
   term, so it gives light a gap equal to the rotation angle — measured, at
   θ = 0.1 light at k = 0 sits at ω = 0.1 instead of 0.
3. **A gradient coupling**, angle `g·(1 − cos k_c)`, zero for an unwound field.
   This kept light massless but was reported as resolving motion on the strength
   of samples taken only at `k_x ∈ [0, 0.10]`. Over the full range it fails:

```
python3 scripts/cylinder.py --bloch --linear separated --grad 3.0 --nc 24 --n 1
```

| k_x | −0.30 | −0.20 | −0.10 | 0.00 | +0.10 | +0.20 | +0.30 |
|---|---|---|---|---|---|---|---|
| Ω | 0.3176 | 0.2830 | 0.2884 | 0.2968 | 0.3112 | 0.3377 | 0.3849 |
| error vs KK | −24.8% | −20.9% | −7.9% | 0.0% | −0.6% | −5.7% | −8.8% |
| v_g | — | +0.044 | +0.066 | **+0.107** | +0.191 | +0.356 | +0.591 |

The band is **not even in k_x**, and the group velocity at k_x = 0 is **+0.107**:
a mode at rest drifts, so a ±n standing wave splits, its two halves going
opposite ways. The cause is the pairing — `+x` with `+c`, `−x` with `−c` — so
each compact direction hybridises with only one x direction. The 0.0–0.7%
agreement originally reported was the one place a tilted band and a fitted
hyperbola happen to cross. The rule was also applied in the c-Fourier basis, so
it was never strictly local, and its angle law is periodic, so the mass tower is
not monotonic in n at high winding.

This whole line was solving a problem the project created for itself: the
pooled scatter keeps the sectors apart automatically (§M2) and supplies the
motion (§M3).

---

## Status of each number

| § | claim | grade |
|---|---|---|
| M1 | exact energy conservation | **[rigorous]** — by construction, audited |
| M2 | linear sector crosses nothing, at any amplitude | **[rigorous]** — exactly zero, and forced by Bloch |
| M3 | pooled scatter gives KK motion, local and reciprocal | **[measured]** — two ways, ≤2.6% |
| M4 | nonlinear channel has an amplitude threshold and needs a seed | **[measured]** — the seed requirement is exact |
| M5 | resonance **refuted**; structure belongs to the box | **[measured]** — one-variable-at-a-time, with error bars |
| M6 | overflow preserves motion in a narrow window, pins it above | **[measured]** — single k_x, one ring size |
| M7 | three coupling variants fail | **[rigorous]** — exact Bloch |
