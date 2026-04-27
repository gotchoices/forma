# R64 Track 14 — Nuclear binding from Ma compound mode mass deficit

**Status: complete.  Result: Ma compound formula at R64 Point A
delivers ~1 MeV/n binding constant across the chain, fully
explaining the deuteron (96% match) but only ~12% of heavy-nuclei
binding.  The remaining 88% lives in a "Δ_S residual" that
needs a separate mechanism.  Point B is the inverse: matches
heavy-nuclei chain ~98% but over-binds the deuteron by 8×.**

This is the energy-budget assessment requested in conversation
during the user's reframing of the strong force as "Ma compound
mass deficit + S-side residual, not a force."

Script:
[`scripts/track14_nuclear_compound_scan.py`](scripts/track14_nuclear_compound_scan.py)
Output:
[`outputs/track14_nuclear_compound_scan.csv`](outputs/track14_nuclear_compound_scan.csv)

---

## Premise

User's reframing (after Track 13b ruled out σ_pS_tube V(r) as
the strong-force mechanism): nuclear binding might be just the
energy budget of Ma compound mode formation, with whatever
residual deficit attributed to S-side without needing to know
literal spatial separations.

The decomposition:

```
B_obs = -Δ_Ma + (energy living in S)
Δ_Ma = m_Ma(compound) - M_free
Δ_S  = -Δ_Ma - B_obs    (residual)
```

If Δ_Ma alone explains B_obs (Δ_S ≈ 0), nuclear binding is
purely "Ma compound mass deficit" and no S-side mechanism is
needed.

## Method

For each nucleus (Z, N), compute:
- R64's u/d-composition tuple: `n_pt = 3·A`, `n_pr = 2·(Z − N)`
- Ma compound mass: `m_Ma = K · √[(n_pt/ε)² + (n_pr − s·n_pt)²]`
- Free-constituent sum: `M_free = Z·M_p + N·M_n`
- `Δ_Ma = m_Ma - M_free`
- Compare to observed binding `B_obs`

Repeat at Point A (Track 1: ε=0.073, s=0.194, K=22.85; calibrated
to nucleon properties) and Point B (Track 3: ε=0.205, s=0.025,
K=63.63; calibrated to nuclear chain Ca→Sn).

## Results

### F14.1.  Point A: deuteron explained, heavy nuclei missing 88%

At Point A, **Δ_Ma per nucleon is essentially constant at
~1.06 MeV/n** across A:

| Nucleus | A | Δ_Ma (MeV) | B_obs (MeV) | Ma fraction | Δ_S (MeV) |
|---|---:|---:|---:|---:|---:|
| ²H | 2 | −2.13 | −2.22 | **96%** | −0.10 |
| ³H | 3 | −2.82 | −8.48 | 33% | −5.67 |
| ⁴He | 4 | −4.25 | −28.30 | 15% | −24.05 |
| ⁶Li | 6 | −6.38 | −31.99 | 20% | −25.62 |
| ¹²C | 12 | −12.75 | −92.16 | 14% | −79.41 |
| ⁴⁰Ca | 40 | −42.51 | −342.05 | 12% | −299.54 |
| ⁵⁶Fe | 56 | −59.19 | −492.26 | 12% | −433.07 |
| ¹²⁰Sn | 120 | −123.80 | −1020.55 | 12% | −896.75 |

The deuteron's 1.11 MeV/n binding is matched almost exactly
by the Ma compound deficit (1.06 MeV/n).  This is the cleanest
result in any R64 phase — **the deuteron is structurally a
single Ma mode at its m_Ma value**.  No "force" needed.

For heavier nuclei, the Ma contribution is constant per nucleon
while the observed binding rises rapidly.  The Δ_S residual
grows from 0.1 MeV (deuteron) to 897 MeV (¹²⁰Sn), reaching
~88% of total binding.

### F14.2.  Point B: heavy-chain match, deuteron over-binds

At Point B, the pattern flips:

| Nucleus | A | Δ_Ma (MeV) | B_obs (MeV) | Ma fraction |
|---|---:|---:|---:|---:|
| ²H | 2 | −17.32 | −2.22 | **779% (8× over-bound)** |
| ⁴He | 4 | −34.63 | −28.30 | 122% |
| ⁵⁶Fe | 56 | −482.32 | −492.26 | 98% |
| ¹²⁰Sn | 120 | −1009.79 | −1020.55 | 99% |

Point B was calibrated to Ca→Sn binding (Track 3 fit).  At those
nuclei, the Ma compound formula matches observed binding within
1–2% — essentially the entire SEMF curve in the heavy-mass region.

But the deuteron is dramatically over-bound: Point B predicts
17.3 MeV deuteron binding vs the observed 2.22 MeV.  This is
the reason Point B fails the Track 1 calibration anchors.

### F14.3.  No single working point gives both

Point A and Point B are on a 1D viable curve in (ε_p, s_p) space
(Track 1 finding) — both satisfy the proton/neutron mass and
mass gap.  But they sit at very different points on that curve,
and along the curve, the Δ_Ma per nucleon varies from ~1 MeV/n
(Point A) to ~9 MeV/n (Point B).

**There is no point on the curve that simultaneously:**
- Gives 2.22 MeV deuteron binding (Point A: yes; Point B: 17 MeV)
- Gives 8 MeV/n heavy-nuclei binding (Point A: 12%; Point B: 98%)

The two requirements demand different per-nucleon Δ_Ma, but
the simple compound formula gives one value of Δ_Ma per A
that's constant across A.  **A single working point with a
simple compound formula cannot match both ends of the chain.**

### F14.4.  Implications

Three readings of this result:

1. **The Ma compound formula is incomplete.**  It captures the
   deuteron because the (6, 0) compound at small s_p has a
   special low-energy structure (n_pr = 0 minimizes the (n_pr −
   s·n_pt)² term).  But it doesn't capture the saturation
   physics that makes heavy nuclei bind at ~7 MeV/n volume
   density.  Some additional mechanism is needed.

2. **The compound formula is right; volume binding lives in S.**
   The user's energy-budget framework: Δ_Ma gives base, Δ_S
   provides the rest.  This is the framework Track 15 explored
   by fitting SEMF terms to the residual.

3. **R29 had the same result.**  R29's mass formula `n_5=A,
   n_6=2A` matched nuclear MASSES to <1% but explicitly noted
   (F19) that the binding fraction captured drops from 86% at
   deuteron to 8% at ⁵⁶Fe.  R29 attributed the residual to "S
   mode interactions" but never derived them.  Same pattern,
   same gap.

### F14.5.  What this enables for further analysis

Track 14's clean tabulation of Δ_Ma vs B_obs across the chain
is the foundation for:

- **Track 15** (SEMF residual fit): showed the residual fits
  SEMF coefficients within 15-20% of literature
- The user's "energy budget without literal distances" framing
- Architectural clarity: deuteron is special; heavy-nucleus
  binding requires a separate volume mechanism

---

## Numerical summary

At Point A across 18 nuclei (²H → ¹²⁰Sn):

| Quantity | Range |
|---|---|
| Ma fraction of total binding | 12% (heavy) – 96% (²H) |
| Δ_Ma per nucleon | constant ≈ −1.06 MeV/n |
| Δ_S residual per nucleon | 0 (²H) → ~7 MeV/n (heavy) |
| **Deuteron prediction** | **−2.13 MeV vs −2.22 observed (4% off)** |
| **¹²⁰Sn prediction (Ma alone)** | **−124 vs −1021 observed (88% missing)** |

At Point B:

| Quantity | Range |
|---|---|
| Ma fraction of total binding | 98–99% (heavy) – 779% (²H) |
| Δ_Ma per nucleon | grows with A, ~9 MeV/n at saturation |
| **Deuteron prediction** | **−17.3 MeV vs −2.22 observed (8× too deep)** |
| **¹²⁰Sn prediction** | **−1010 vs −1021 observed (1% off)** |

---

## Status

**Track 14: complete.**  Documents the foundational energy-budget
assessment that motivated Track 15's SEMF fit and the user's
"forces are Ma phenomena" reframing.

The Ma compound formula contributes ~1 MeV/n base binding at
Point A (matching deuteron exactly) and ~9 MeV/n at Point B
(matching heavy-nuclei chain).  Neither matches both.  **The
volume saturation physics that distinguishes light from heavy
nuclei is not captured by the simple compound formula at any
working point** — additional mechanism required.

This finding was the basis for:
- Track 15 (SEMF residual fit): showed the gap follows SEMF form
- Track 17 (σ_pS_tube residual sweep): showed σ_pS_tube is not
  the volume-binding mechanism at any moderate magnitude
- Pool item ae closure: R29's compound formula has the same gap
- Open architectural question: where does the volume term live
  structurally in MaSt?
