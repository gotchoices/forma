# GRID reproduces relativistic matter waves + the de Broglie relation

**Work item #1, done** (see [foundation-de-broglie-harmony.md](foundation-de-broglie-harmony.md)).
Sim: [`../scripts/grid_dispersion.py`](../scripts/grid_dispersion.py); figure
[`../outputs/grid_dispersion.png`](../outputs/).

## Method (exact, not a fit)

The impedance scatter S=(2/N)J−I followed by propagation acts on a plane wave
exp(i(kx·x + kc·c − ω·t)) as one linear operator **M(kx,kc) = P·S**, P =
diag(e^{i kx}, e^{-i kx}, e^{i kc}, e^{-i kc}). Its eigenvalues are e^{−iω}, so
**ω(k) = −arg(eig M)** is GRID's *exact* dispersion — the dynamics diagonalized. A
short time-domain run of the actual cylinder update confirms it (eig Ω = 0.2775 vs
time-FFT Ω = 0.2765, 0.4%). The propagating modes sit at the band edge ω≈π (the
scatter's −1 eigenvalue = a staggered background); the **physical frequency is
Ω = π − ω**.

## Results (nc = 24)

- **Photon (n=0):** massless — Ω = c·kx to **<1%** for kx < 0.2π. Lattice
  **light-speed c = 0.7007** nodes/tick (cf. sim-maxwell's ~0.7).
- **Massive modes (winding n, kc = 2π n/nc): relativistic.** Ω² = c²·kx² + ω₀²
  holds to **<2% out to kx ≈ 0.4π**, with the **same c ≈ 0.70** as the photon
  (Lorentz-consistent across the massless and massive sectors — an SR check the
  lattice was not built to pass).
- **KK mass tower:** ω₀(n) = 0.185, 0.368, 0.548 for n = 1,2,3 ≈ **n·(2π/nc)·c** —
  mass = compact wavenumber × light-speed, the Kaluza–Klein relation, straight
  from the geometry.
- **de Broglie phase harmony:** v_phase · v_group = c² to **1–6%** (1.012, 1.030,
  1.059 for n=1,2,3). This is the signature that the compact Compton clock and the
  open de Broglie wave stay in phase — i.e. **λ = h/p**.

## Lattice-Lorentz-breaking (quantified)

GRID is relativistic in the **continuum / low-k** regime and deviates near the
lattice scale: the relativistic law holds to <2% for **kx ≲ 0.4π**, and deviations
grow both with kx (toward the zone boundary) and with n (heavier modes deviate
sooner — 2.07% at n=1's window edge vs 0.25% at n=3 in the fit window, and the
de Broglie ratio drifts 1.01→1.06). So the "GRID relativistic regime" is
kx below ~0.4× the lattice cutoff; beyond it, discreteness shows.

## Significance

- **GRID reproduces special-relativistic matter waves and the de Broglie relation
  natively** — a foundation stone, from the (x,c) lattice, not assumed. The
  compact/open split *produces* λ = h/p via phase harmony, as the foundation note
  predicted.
- **The KK mass tower is concrete** (ω₀ = n·(2π/nc)·c) — this **revives
  [metric-mass](../../metric-mass/)** with a measured spectrum: masses are set by
  the compact ring size nc (bigger ring → lighter tower).
- **Honest scope:** λ = h/p is near-automatic for *any* plane wave; the *content*
  here is that the dispersion is **relativistic** (non-trivial for a discrete
  lattice), that **c is shared** across sectors, that **v_p·v_g = c²**, and that
  the **breakdown scale is quantified**. Those are the GRID-native, non-obvious
  facts.

## Next

- **nc-dependence of the tower:** sweep nc, confirm ω₀(n) = n·(2π/nc)·c and read
  off how ring size sets the mass scale (hand to metric-mass).
- **Boosted phase-harmony in real space:** show a moving compact-mode wavepacket
  carries an open-dimension modulation at λ = h/p (the picture-level de Broglie
  wave), complementing this spectral proof.
