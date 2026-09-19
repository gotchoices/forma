# Review — the three-axis dispersion used in Chapter 7 is wrong

> **RESOLVED 2026-09-18 — verified, then fixed via Option 2.**
> The finding was independently confirmed three ways: (i) analytically, by
> carrying the general scalar condition already in
> [work/dispersion-analytic.md](work/dispersion-analytic.md) through to d axes,
> which gives Σ_a 1/(cos k_a + cos ω) = 0 and collapses to a mean of cosines only
> at d = 2; (ii) numerically, with a from-scratch Bloch operator reproducing
> [scripts/dualslit.py](scripts/dualslit.py)'s literal update to 3.5×10⁻¹⁶ and
> showing the sole propagating branch at c² = 2/3 on-axis, with no mode at the
> assumed value; (iii) empirically, by FFT of the field.
>
> **Option 2 was taken.** The lab now runs on the canonical scatter, which is
> isotropic in three axes; the mean-of-cosines relation is therefore *correct*
> there, and the originally published λ = 8.07 / 11.18 and ω₀ = 0.300 stand —
> now confirmed by measurement to 0.7% / 1.5%. The fringe spacings changed with
> the medium (photon 5.9 → 26.2, matter 13.8 → 32.8), and λL/d, previously off
> by a factor ~3, now holds to +11% / +0.6%. Two further defects found during
> the fix are recorded in §8.
>
> Current state: [work/dualslit-matter-result.md](work/dualslit-matter-result.md)
> §Revision record.

**Found:** while cross-checking scatter conventions for
[grid-gravity](../grid-gravity/work/uniform-q-theorem.md) (its §4).
**Severity:** medium · not fatal · fixable. **Scope:** Chapter 7's quoted
wavelengths, light speed and rest frequency, and the formula behind them.
**Not affected:** every two-axis (x, c) result — Chapters 3, 4, 8 and the
original two-slit on a plain (x, y) lattice.

---

## 1. What is wrong

The matter-wave two-slit ([07-two-slit-lab.md](07-two-slit-lab.md),
[work/dualslit-matter-result.md](work/dualslit-matter-result.md),
[scripts/dualslit.py](scripts/dualslit.py)) runs on a **three-axis** lattice
(x, y, compact c; N = 6). Its de Broglie wavelengths were computed from an
*assumed* dispersion relation — the "obvious" generalization of Chapter 4's
two-axis result:

> assumed: cos Ω = (cos k_x + cos k_y + cos k_c)/3  → c = 1/√3, isotropic.

That relation was never derived or checked for three axes. **It is not the
dispersion of the update rule the script runs.** The exact relation for that
rule, for any number of axes d, is

<!-- Σ_a 1/(cos k_a − cos Ω) = 0 -->
$$
\sum_{a=1}^{d} \frac{1}{\cos k_a - \cos\Omega} \;=\; 0 ,
$$

which reduces to the mean-of-cosines form **only for d = 2** (where
1/A + 1/B = 0 means A + B = 0). For d = 3 it is a quadratic in cos Ω, with two
branches, and it is **anisotropic at leading order**:

| direction of k | speed² (this rule, 3 axes) | assumed |
|---|---|---|
| along a lattice axis | **2/3** | 1/3 |
| along a face diagonal | **1/2** and **1/6** (two branches) | 1/3 |

## 2. Why — two scatter conventions

The repo contains two update rules that look alike and are not the same:

- **Canonical** ([grid-duality/models/scattering.md](../grid-duality/models/scattering.md)):
  each node's registers are *edge end-registers*; the node overwrites each with
  V minus that register's content; each edge then swaps its two ends. In
  direction-of-travel terms: out[d] = V − in[−d].
- **This project's sim code**: registers are labeled by *direction of travel*
  and out[d] = V − in[d].

(V = (2/N)·Σ registers in both.) The two give the same physics in **two** axes —
both isotropic with c² = 1/2, related by Ω ↔ π − ω — which is why nothing in
the (x, c) work is affected. In **three** axes the canonical rule is isotropic
with c² = 1/3, and this project's rule is the anisotropic one above.

## 3. Evidence

1. **Exact eigenvalues** of the one-tick operator (k = 0.3 along x, three
   axes): this project's rule gives Ω = 0.2446 (c² = 0.665); the canonical rule
   gives Ω = 0.1728 (c² = 0.332). Along the diagonal (0.3, 0.3, 0): this rule
   gives 0.1728 and 0.3000; the canonical rule 0.2446 (isotropic).
   Reproduce with
   `grid-gravity/scripts/carrier_dispersion.py --dims 3` (rows Y = 0;
   convention `repo` is this project's rule, `tlm` the canonical one).
2. **Independent time-domain run** of this project's update rule (plane wave
   along x, k = 0.2992, three axes, 4096 ticks): the spectral peak sits at
   ω = 2.897 = π − 0.244, the c² = 2/3 value. The assumed relation predicts
   ω = 2.969; there is no peak there.

## 4. Corrected numbers

Same run as reported (drive ω = 2.7 → Ω = 0.4416; n_c = 12; on-axis, k_y = 0):

| quantity | as written | corrected |
|---|---|---|
| lattice light speed (on-axis) | c = 1/√3 | c = √(2/3), and direction-dependent |
| rest frequency of the n = 1 mode | ω₀ = 0.300 | ω₀ = 0.426 (from cos Ω₀ = (1 + 2cos k_c)/3) |
| photon wavelength | 8.07 nodes | **11.57 nodes** |
| matter-wave wavelength | 11.18 nodes | **24.45 nodes** |
| wavelength ratio, matter/photon | 1.38 | **2.11** |

The corrected ratio (2.11) is *closer* to the measured fringe-spacing ratio
(13.8/5.9 = 2.34) than the old one was. The drive sits only just above the
corrected mass gap (0.4416 vs 0.426), which is why the matter wave is so long.

## 5. Where it appears

- [07-two-slit-lab.md](07-two-slit-lab.md) §2 — "11.18 versus 8.07 lattice
  nodes … read off exactly"; "c = 1/√3 here rather than 1/√2".
- [README.md](README.md) — Ch 7 arc bullet ("11.18 vs 8.07 nodes, exact from the
  dispersion").
- [work/dualslit-matter-result.md](work/dualslit-matter-result.md) — the stated
  dispersion relation, ω₀ = 0.300, both wavelengths, the results table.
- [work/README.md](work/README.md) — strand 10 (same numbers).
- [scripts/dualslit.py](scripts/dualslit.py) — `debroglie_lambda()` and the
  printed rest frequency use the assumed relation; the module docstring states
  it.

An earlier review pass "independently re-checked" these numbers — but against
the same assumed relation, so it could not catch this.

## 6. What stands, what falls

**Stands.** A massive compact-sector wave interferes in the two-slit on the same
lattice as the photon; its wavelength is longer than the photon's and its
fringes are coarser. That is the claim Chapter 7 needs, and the sim shows it
regardless of the formula. Chapter 7's caveats (classical linear-wave
interference; λL/d not fit) also stand — and the in-plane anisotropy is an
additional reason the absolute fringe spacing does not follow λL/d.

**Falls.** The specific wavelengths, the rest frequency, the light speed, and
the word "exact" attached to them. Also implicit: that the three-axis lab is an
isotropic medium. With this rule it is not.

## 7. Options

1. **Minimal.** Replace the assumed relation with the exact one in
   `dualslit.py`, correct the numbers in the five places of §5, and add a
   sentence that the three-axis lab is anisotropic under this project's scatter
   labeling.
2. **Better.** Re-run the two-slit on the **canonical** scatter (isotropic in
   three axes, c² = 1/3). The mean-of-cosines relation is then *correct*
   (cos ω = Σcos k_a / 3, band at ω ≈ 0), the lab is an isotropic medium, and
   the fringe geometry can be compared with λL/d on fairer terms.
3. **Optional, for completeness.** Note in Chapter 1 or 4 that the project's
   code uses the direction-labeled scatter, that it agrees exactly with the
   canonical one in two axes, and that it should not be used beyond two.

---

## 8. Addendum (2026-09-18) — two further defects found while fixing this

Both were in [scripts/dualslit.py](scripts/dualslit.py), both now fixed.

1. **The matter-wave field snapshot was numerically dead.** The snapshot summed
   over the compact axis (`snap.sum(axis=2)`), which annihilates any n ≥ 1 mode
   *exactly*, since Σ_c cos(2πnc/nc) = 0. Measured amplitude in that panel was
   **4.0×10⁻¹⁵** — floating-point residue — against 8.5×10⁻² for the properly
   projected field, so the published `dualslit_matter.png` was rendering noise at
   full colour scale. The detector pattern was never affected: it sums *squares*,
   which do not cancel. The snapshot is now projected onto the compact mode.

2. **The docstring claimed a measurement the code never performed.** It stated
   the script "measures the in-plane wavelength directly from the field snapshot
   (FFT along x, post-barrier) … not to an assumed drive→k mapping." There was no
   FFT in the file; λ came solely from the assumed mapping. This is plausibly why
   the error survived the earlier review pass — the docstring advertised the very
   check that would have caught it. The FFT measurement is now implemented, as a
   barrier-free CW calibration pass, and is reported alongside the analytic value.

A third, smaller point: the peak counter labelled any ≥3 maxima "INTERFERENCE
FRINGES", which cannot separate two-slit interference from single-slit
diffraction ripple — under the legacy rule the one-slit matter run was labelled
as fringes. The label is gone and the one-slit control is now run and reported;
under the canonical scatter both one-slit controls come out as clean single lobes.
