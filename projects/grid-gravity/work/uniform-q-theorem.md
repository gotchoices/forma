# The uniform-q theorem — a lossless local rule that slows every mode alike

**Status:** Derivation + exact numerical check. **Step 1 of the mechanism 3
validation plan ([STATUS.md](STATUS.md)): passed.** A concrete, local, lossless
rule exists under which a uniform carrier value rescales the *whole* spectrum
through one universal map — light speed, rest frequency and inertia together.
That is what separates time dilation from an optical medium. The same
calculation shows which variants fail, and how.

Script: [`../scripts/carrier_dispersion.py`](../scripts/carrier_dispersion.py).
Figure: [`../outputs/carrier_dispersion.png`](../outputs/carrier_dispersion.png).

Grades: **[rigorous]** (exact algebra, confirmed numerically to fit precision),
**[argument]**, **[open]**.

---

## 1. What has to be shown

[Mechanism 3](sync-carrier-mechanism.md) needs a rule by which the carrier's
value q at a place slows propagation there. For the slowing to be *time
dilation*, a **uniform** q must be unobservable from inside: every clock —
whether built from light bouncing between mirrors or from the rest frequency of
a massive mode — must slow by the same factor. In terms of the spectrum, a mode
with wavenumber k_x along space and k_c around the compact dimension must obey

<!-- Ω² = c_q² (k_x² + k_c²),  with one c_q for everything -->
$$
\Omega^2 \;=\; c_q^2\,(k_x^2 + k_c^2)
$$

with a *single* c_q: the photon speed (k_c = 0), the rest frequency
ω₀ = c_q·k_c (k_x = 0), and the inertia (the coefficient of k_x² for a massive
mode) all set by the same number. If they scale differently, the loaded region
is an optical medium and clocks of different construction disagree.

This requirement is also the carrier's shift symmetry (P4 of the mechanism
note): if a uniform q is a pure rescaling of time, a uniform shift of q is
unobservable, which is what keeps the carrier massless.

## 2. The rule [posit, now concrete]

The scatter is GRID's canonical one
([grid-duality/models/scattering.md](../../grid-duality/models/scattering.md)):
each node holds N end-registers, one per edge. *Inhale:* the node forms its
value V and overwrites each register with V minus that register's content.
*Exhale:* each edge swaps its two end-registers.

**Addition.** Give each node one more register — a **storage register** of
weight Y ≥ 0 — that takes part in the inhale like any other but is not attached
to an edge: its content simply **returns to the same node on the next tick**.
With a the stored amplitude,

<!-- V = 2(Σ r_j + √Y·a)/(N+Y);  r_j ← V − r_j;  a ← √Y·V − a -->
$$
V = \frac{2\,(\sum_j r_j + \sqrt{Y}\,a)}{N+Y},
\qquad r_j \leftarrow V - r_j,
\qquad a \leftarrow \sqrt{Y}\,V - a .
$$

This is a reflection about the unit vector (1,…,1,√Y)/√(N+Y), so it is exactly
orthogonal — **lossless for every Y** (checked: error ~10⁻¹⁶). In
transmission-line language it is a node loaded with an open stub; in the
project's own language it is the "detour" of mechanism 2 made exact — a wave
spends part of each tick parked off the lattice and is returned, delayed, not
absorbed. Y is how much is parked. The carrier sets Y (§5).

## 3. The spectrum, in closed form [rigorous]

For a plane wave with wavenumbers k_a along the d lattice axes (N = 2d), the
one-tick eigenvalue e^(−iω) of the loaded lattice satisfies

<!-- cos ω = (2 Σ_a cos k_a + Y) / (N + Y) -->
$$
\cos\omega \;=\; \frac{2\sum_a \cos k_a \;+\; Y}{N+Y} .
$$

(Derivation: write the inhale as 2ûûᵀ − X, with X the swap of each ± pair, and
solve 1 = 2ûᵀ(λ + PX)⁻¹Pû; each axis contributes 2(λcos k_a − 1)/(λ² − 1) and
the storage register Y/(λ + 1).) At Y = 0 this is the known unloaded relation
cos ω = (Σ cos k_a)/d. The storage register enters **exactly like one more axis
held at k = 0** with weight Y/2 — a compact loop one node long.

Two consequences:

**(a) Low frequency.** Expanding for small k,

<!-- ω² = (1/d)·(Σ k_a²) / (1 + Y/N) -->
$$
\omega^2 \;=\; \frac{1}{d}\,\frac{\sum_a k_a^2}{1 + Y/N} ,
$$

isotropic, with one speed c_Y = c₀/√(1 + Y/N) for every direction, compact or
extended. So the photon speed, the rest frequency and the inertia all carry the
same factor. Numerically (2 axes; 3 axes identical in form):

| Y | c² along x | c² diagonal | ω₀²/k_c² | inertia α | predicted |
|---|---|---|---|---|---|
| 0 | 0.50000 | 0.50000 | 0.49999 | 0.50001 | 0.50000 |
| 1 | 0.40000 | 0.40000 | 0.40000 | 0.40000 | 0.40000 |
| 4 | 0.25000 | 0.25000 | 0.25000 | 0.25000 | 0.25000 |

**(b) All frequencies — a universal map.** Comparing the loaded and unloaded
relations at the same k gives, exactly,

<!-- sin(ω_Y/2) = sin(ω_0/2) / √(1 + Y/N) -->
$$
\sin\frac{\omega_Y}{2} \;=\; \frac{1}{\sqrt{1+Y/N}}\;\sin\frac{\omega_0}{2} .
$$

The loaded frequency depends on the mode **only through its unloaded
frequency** — not on its direction, not on whether it is light or a massive
mode. Every mode of a given frequency is slowed identically: universality is
exact, not a low-frequency approximation. What is *not* exact is the
proportionality: the slowing factor drifts with frequency by a fractional
amount ≈ (ω₀²/24)·(Y/N)/(1 + Y/N), i.e. of order (frequency × tick)². For any
observable frequency on a Planck-scale lattice that is the same ~10⁻⁴⁰ class of
correction that [qa/Q141](../../../qa/Q141-emergent-lorentz-invariance-from-grid.md)
finds for Lorentz invariance itself.

**Identification.** The clock-rate factor is

<!-- 1 − q = 1/√(1 + Y/N)   ⇒   Y ≈ 2N·q for small q -->
$$
1 - q \;=\; \frac{1}{\sqrt{1+Y/N}}
\qquad\Longrightarrow\qquad Y \approx 2N\,q \quad (q \ll 1).
$$

## 4. The variants that fail — and what each failure is [rigorous]

| Variant | Result | Reading |
|---|---|---|
| Stored share returns **inverted** (sign −1) | cos ω = (2Σcos k_a − Y)/(N+Y): at k = 0 the frequency is not zero — a **gap**, ω² ≈ 4Y/(N+Y) | The photon acquires a **mass**. This is the lattice form of the error in mechanism 2's first pass ([gauge-invariant-coupling.md](gauge-invariant-coupling.md)): a potential-like coupling gives a mass, a kinetic-like one gives an index. The two differ here by one sign. |
| Registers labeled by **direction of travel** (out[d] = V − in[d], the labeling in grid-matter's sim code) + storage | speed *rises* along the axes, c² = (2+Y)/(4+Y); unchanged along the diagonal; inertia no longer matches | Anisotropic at leading order — not a time dilation. |
| Same labeling, stored share inverted | no effect at leading order | No slowing. |

A side finding worth recording: the direction-labeled variant agrees with the
canonical scatter in **two** axes (both give c² = 1/2, isotropic), which is why
grid-matter's (x, c) results stand. In **three** axes it does not: the canonical
scatter is isotropic with c² = 1/3, while the direction-labeled one has
c² = 2/3 along an axis and two branches (1/2 and 1/6) along a diagonal.
Mechanism 3 work should use the canonical scatter.

## 5. What this does and does not settle

**Settled.**
- Gate condition (2), non-dispersive slowing: met from the rule, for all modes,
  with Planck-suppressed drift — stronger than mechanism 2's "for ω ≪ ω₀ only".
- The equivalence-principle requirement: light clocks and matter clocks slow
  together.
- The shift symmetry behind masslessness is realized: uniform Y is a pure
  rescaling of time.
- **The wave speed of the carrier [argument].** If the carrier is itself an
  amplitude moved by the same scatter (a second channel on the same registers,
  with Y a function of its node value), it obeys the same relation of §3 —
  loaded or not. Its speed equals light's identically, with nothing tuned, and
  it is delayed by a mass exactly as light is.

**Not settled.**
- **Non-uniform Y.** Storage changes the local wave impedance, so a gradient of
  Y partially reflects. For a slowly varying Y this should be negligible; the
  drop test (step 2) measures it, and measures the acceleration.
- **Light bending.** An isotropic slowing gives δln c = δln ω₀. Writing the
  coordinate light speed as c(1 + (1+γ)Φ) and the rest-clock rate as (1 + Φ),
  that is **γ = 0: half the observed light bending.** The observed γ = 1 needs
  propagation along the *extended* directions slowed twice as much (in the
  logarithm) as propagation around the *compact* one. A node-level storage
  register cannot do that alone; an additional slowing that acts on extended
  edges only — the spatial "pinch" — of equal size would. This is the target
  for step 3.
- **Dynamics of Y.** How the carrier is sourced by energy and how its value
  sets Y is the content of step 3 (the action).

## Grades summary

- **[rigorous]** Losslessness of the rule; the closed-form relation
  cos ω = (2Σcos k_a + Y)/(N+Y); the universal frequency map; the failure modes
  of §4.
- **[argument]** Carrier speed = light speed if the carrier rides the same
  scatter.
- **[open]** Reflection at gradients (step 2); γ (step 3); sourcing (step 3).
