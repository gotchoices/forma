# Chapter 4 — Matter waves, mass, and de Broglie

This is the firmest chapter — its results are exact and need no premise beyond the
scatter and a compact coordinate. It is also the most *corroborative*: it is
standard Kaluza–Klein physics on a lattice, confirming
[metric-mass](../metric-mass/) dynamically. So it is kept short: one derivation,
then citations.

## §1 The exact dispersion

For a plane wave e^{i(kx·x + kc·c − ωt)}, one tick acts by the linear operator
M = P·S, where S = ½J − I (N=4) and P = diag(e^{i kx}, e^{−i kx}, e^{i kc},
e^{−i kc}). The eigenvalue condition (worked in
[work/dispersion-analytic.md](work/dispersion-analytic.md), and by the standard
Bloch method of [grid-duality ch.7](../grid-duality/07-wrap-promotion-modeling.md))
collapses to a single closed form:

<!-- cos ω = − (cos kx + cos kc) / 2 -->
$$
\cos\omega \;=\; -\,\frac{\cos k_x + \cos k_c}{2}.
$$

The propagating modes sit at the band edge (ω≈π); writing the physical frequency
as Ω = π − ω gives cos Ω = (cos kx + cos kc)/2, from which everything below reads
off. **[D]**

## §2 The photon

For the c-uniform mode (kc = 0) at small kx, the relation gives Ω = kx/√2 — a
**massless**, linear dispersion with **lattice light-speed c = 1/√2 ≈ 0.707**. **[D]**

## §3 Massive modes and the KK tower

For a compact-momentum mode (kc = 2πn/nc), small-kx expansion gives the
**relativistic** form and the **Kaluza–Klein mass tower**:

<!-- Ω² = c² kx² + ω₀²,  ω₀(n) = c · kc = n·(2π/nc)/√2 -->
$$
\Omega^2 \;=\; c^2 k_x^2 + \omega_0^2, \qquad \omega_0(n) = c\,k_c = \frac{n}{\sqrt2}\cdot\frac{2\pi}{n_c} \;\propto\; \frac{1}{R}.
$$

Same c as the photon (a cross-sector Lorentz check), and a mass set by the compact
size R. This is the compact-standing-wave mass of [metric-mass](../metric-mass/),
now obtained dynamically and in closed form. **[D small-kc — corroborates metric-mass]**

Both the relativistic form and the linear-in-n tower are small-kc results: ω₀ = c·kc
is the leading term of the *exact* rest frequency Ω₀ = arccos((1+cos kc)/2), so the
tower is linear only for the low rungs and bends **sub-linear** higher up (≈5% low
by kc≈1.5). This does not bite the physics — real particles sit on large sheets
(nc huge, kc = 2π/nc tiny), where the linearization is excellent — but the exactness
is of the *closed form*, not of the n-linear tower.

## §4 de Broglie

From Ω² = c²k² + ω₀², the phase and group velocities satisfy

<!-- v_phase · v_group = c² -->
$$
v_\text{phase}\cdot v_\text{group} \;=\; \frac{\Omega}{k}\cdot\frac{c^2 k}{\Omega} \;=\; c^2,
$$

which is de Broglie's phase harmony, giving the **λ = h/p** *shape*. (ℏ enters only
as the units conversion p = ℏk, E = ℏΩ — a scale choice, not a derived constant;
per the project's principle-vs-scale rule.) **[D — cite de Broglie]**

## §5 Scope

This chapter rests on **only the scatter plus a compact coordinate** — no
field-value phase posit (contrast Chapter 3), which is why it is the firmest.
The exactness is small-k, however: the full lattice relation
cos ω = −(cos kx + cos kc)/2 is not boost-invariant, so Lorentz symmetry and the
shared c are **emergent at small k** — holding to within ~2% for kx < 0.4π and
degrading toward the zone boundary. **[C — quantified, honest]**

## §6 Confirmation

The closed form matches the exact scatter eigenvalues to machine precision, and
its small-k predictions (light-speed 1/√2, mass tower) match the time-domain
simulation to ~4 significant figures ([work/dispersion-analytic.md](work/dispersion-analytic.md)).
