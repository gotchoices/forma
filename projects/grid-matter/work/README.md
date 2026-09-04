# grid-matter / work — the reasoning, indexed

> **Terminology (read first):** "compact dimension" is generic — a **Ma sheet**
> for a massive particle (size sets the mass), the **ℵ-line** for the Planck/photon
> level. Older docs say "ℵ-line" where they mean "the relevant compact dimension";
> the mechanism is scale-blind. See **[promotion-hierarchy.md](promotion-hierarchy.md)**
> for the convention and the mass→charge "promotion ladder" (which our results
> support).

This folder is the full record of the project's thinking, in **work mode** — sims
and reasoning, not yet the finished derivations. When any strand is ready to become
a main derivation, this index is the map of *how we got there* and *what is
proven vs. posited*.

## The working arc (the map — for building the derivations later)

**Act 1 — the particle (largely done).** Can GRID bind a particle? Several local
mechanisms fail; the answer is the **compact phase** → sine-Gordon **breather
(mass)** / **kink (charge)**. GRID is intrinsically focusing. Confirmed:
relativistic **matter waves + de Broglie + KK mass tower** (measured); free-space
stability needs a **conserved winding** (Q-ball). Ties to the **promotion ladder**
(light→mass→charge). *Proven in sim; the one posited link is the on-site cosine
from the literal edge-scatter (the "reduction gap").*

**Act 2 — measurement (frontier, entered).** Two-slit interference + single-lump
build-up on a GRID lab; **collapse dissolved** (breather = hidden-variable lump);
**single-particle Born done** as consistency (energy density ∝ |ψ|² + whole-quantum
absorption + linear detection ⇒ P ∝ |ψ|², no steering —
[born-single-particle.md](born-single-particle.md), derivation-ready). **Bell
structure** confirmed (non-local fiber = QM, no signaling). *One hard core owed:
entangled/multi-particle Born — needs non-local hidden variables; a closed/periodic
geometry is one feasible placeholder (not a single asserted theory).*

**When to promote to a derivation:** Act 1's breather/de-Broglie/mass-tower and
Act 2's **single-particle Born** are the ripest — measured or consistency-derived,
only the reduction gap posited. The **entangled Born / Bell** core is not yet
derivation-ready.

## The arc, in order (detailed)

1. **[results-m1-m2.md](results-m1-m2.md)** — the opening sim campaign on the
   (x,c) cylinder. **M1 (KK decoupling) verified.** M2 (pair production from
   saturation) came out **negative**: a vacuum-seeded head-on collision under
   clip/spillover pumps no persistent compact mode, and the **trap test** shows
   the value-bound is **defocusing** — it cannot self-bind a particle. Also the
   discreteness probe (crude `--quantize`) and the S→c "0.7%≈α?" artifact.

2. **[binding-evaluation.md](binding-evaluation.md)** — with binding unsolved, a
   **gate** (criteria any mechanism must satisfy) was set and the candidates
   scored, rather than guessing. Verdict at the time: topology + instantiation
   look complementary; lattice-gas dominated.

3. **[phase-winding-results.md](phase-winding-results.md)** — the topological
   route tested: a U(1) phase field. The winding is protected and localized **but
   immobile** (a flat band) — not a genuine particle on the 1D ring.

4. **[responsive-medium.md](responsive-medium.md)** — the "edges react to load"
   program (Wheeler loop at the substrate): knob A (speed/index → g₀₀) and knob B
   (contraction/strain → gᵢⱼ). Neither *binds* a particle (both fail
   containment), but **knob B's strain field is a real gravity-carrier
   candidate** — a possible grid-gravity revival, kept separate from binding.

5. **[soliton-result.md](soliton-result.md)** — after several binding failures, the
   common gap is named: a **missing focusing nonlinearity**. A clean (borrowed,
   non-GRID) **Q-ball** with focusing+saturating binds a stable, mobile,
   charge-conserving particle — proving the *option* exists, and posing the crux:
   *can GRID supply focusing?*

6. **[focusing-from-phase.md](focusing-from-phase.md)** — **the key result.**
   GRID's bound is a compact **phase** (ℵ-line), and a phase's potential is
   periodic: U = m²(1−cos φ) is **focusing + saturating for free** → **sine-Gordon
   breather = particle**, **kink = charge**. Confirmed on the discrete (x,c)
   lattice (stable, mobile, survives Peierls–Nabarro); dimensionality settled
   (Derrick — 1 extended dimension). *Open:* derive the cosine from the literal
   edge-scatter.

7. **[foundation-de-broglie-harmony.md](foundation-de-broglie-harmony.md)** — the
   shared foundation: the compact **Compton clock** (mass) phase-locked to the
   open **de Broglie wave** gives **λ = h/p**, GRID-native. Plus the spectrum
   duality (open→continuous→sinc photon; compact→discrete→periodic particle). Not
   a rival hypothesis — an ingredient all of them need.

8. **[de-broglie-dispersion-result.md](de-broglie-dispersion-result.md)** — the
   foundation, *measured*. GRID's exact dispersion (eigenvalues of the
   scatter+propagate operator, confirmed time-domain) is **massless photon** +
   **relativistic KK modes** (Ω²=c²k²+ω₀², same c≈0.70), **de Broglie v_p·v_g=c²**,
   and the **KK mass tower** ω₀(n)=n·(2π/nc)·c — to <2% for kx<0.4π
   (Lorentz-breaking quantified beyond). Revives metric-mass with a measured
   spectrum.

9. **[promotion-hierarchy.md](promotion-hierarchy.md)** — terminology (ℵ vs
   compact dimension) and grid-matter's *dynamical evidence* for grid-duality's
   **wrap-promotion ladder** (light→mass→charge). **Stability = a protected
   winding** (Q-ball stable vs oscillon radiating); the "ephemeral" particle zoo is
   real data (its quantum numbers = the ladder's observables), not to be discounted.

10. **[dual-slit-result.md](dual-slit-result.md)** — *Act 2 opens.* On a 2D GRID
    lab (barrier = mass-blocked nodes; slit = open GRID), a wave through **both**
    slits **interferes**, and **single whole-quantum lumps rebuild the fringes**
    (corr→0.97) — no collapse invoked. *(This first pass used the **massless/photon**
    field.)* **[dualslit-matter-result.md](dualslit-matter-result.md)** then extends
    it to a genuine **massive matter wave** (compact n=1): it interferes too, with a
    longer de Broglie λ (11.18 vs 8.07 nodes, exact from the dispersion) and coarser
    fringes — so the two-slit is a real *matter*-wave demo, not only the photon.

11. **[measurement-and-bell.md](measurement-and-bell.md)** — the refined
    measurement model: two unknowns (interference vs the specific draw = a hidden
    phase); measurement = interference with the observer; **collapse dissolved**;
    **Bell via the fiber as a globally self-consistent condition** (settings kept
    *free* — not superdeterminism).

12. **[bell-test-result.md](bell-test-result.md)** — toy CHSH test: a **local**
    fiber phase is capped at 2; a **non-local** fiber reaches **2√2 = QM, no
    signaling**. Structure confirmed viable; the cosine was *put in by hand* —
    deriving it from a real fiber equation is owed.

13. **[born-single-particle.md](born-single-particle.md)** — *derivation-ready.*
    Single-particle **Born from energy density**: P(click) ∝ |ψ|² from energy
    density ∝ |ψ|² + whole-quantum absorption (grid-quantization) + linear
    detection. **No steering, no collapse.** Entangled Born (the one hard core)
    needs non-local hidden variables — one *feasible placeholder* (closed/periodic
    S) shown, not a single asserted theory.

## The working hypotheses (what a particle is / how measurement works)

Held **open**, in parallel — pursue whatever bears fruit:

- **[thesis-wave-until-interaction.md](thesis-wave-until-interaction.md)** — a
  particle is a wave; localization is an *interaction event*; the bound quantizes
  the interaction into one |ψ|² click. Eliminates (extended-space) containment.
  The measurement fork (collapse+fiber vs Reiter) lives here.
- **[thesis-double-solution.md](thesis-double-solution.md)** — de Broglie's double
  solution / walking droplet: a contained **bulk** (soliton) steered by its own
  **pilot** wave. Dissolves single-particle collapse/FTL; rehabilitates the
  containment work; entanglement still needs the fiber.

## How the pieces relate (and what's ready to derive)

- **Act 1 / binding (strands 1–9): largely solved & measured.** The sine-Gordon
  breather (from the compact phase) is the particle; the kink is its charge;
  matter waves, de Broglie, and the KK mass tower are measured; stability = a
  protected winding; all consistent with the promotion ladder. **Derivation-ready**
  except the one **posited** link — the on-site cosine from the literal
  edge-scatter (the reduction gap, strand 6).
- **Act 2 / measurement (strands 10–13): mostly framed.** Collapse dissolved;
  **single-particle Born done** (energy density, derivation-ready, strand 13); Bell
  *structure* confirmed. The **one hard core owed** is **entangled Born** — needs
  non-local hidden variables, with a closed/periodic geometry as a *feasible
  placeholder* (not a single asserted theory).
- **Interpretation** (the hypotheses) stays **open**: contained bulk (double
  solution) vs delocalized wave (wave-until-interaction); both use the de Broglie
  foundation, and Act 2's results fit the double-solution reading best.

**If promoting to a main derivation next:** Act 1's breather → mass/charge and the
de Broglie / mass-tower results are ripest (measured, only the reduction gap
posited). The measurement/Bell derivations need the two owed constructions first.
