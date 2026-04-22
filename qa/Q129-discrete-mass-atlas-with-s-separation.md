# Q129: Is there a computable discrete mass atlas — Ma modes plus S separation?

**Status:** Open — framing document.  The Ma-only mode
spectrum is enumerable in principle, but some putative
"single-mode" high-n states would be energetically dominated
by spatially separated multi-particle configurations in S.
A complete atlas requires S in the energy accounting.

**Related:**
  [Q16](Q16-what-sets-photon-energy.md) (photon-energy / mass problem),
  [Q85](Q85-harmonic-ladder-and-threshold.md) (harmonic ladder and threshold),
  [Q91](Q91-compact-volume.md) (compact volume),
  [Q108](Q108-shell-capacity-from-knot-saturation.md) (shell capacity from knot saturation),
  [Q109](Q109-mode-stability-and-composite-fission.md) (mode stability, gcd criterion),
  [Q116](Q116-three-sheets-vs-one-six-torus.md) (three sheets vs one T⁶),
  [R27](../studies/R27-bound-states/) (Ma oscillation patterns),
  [R28](../studies/R28-particle-spectrum/) (Ma spectrum below 2 GeV),
  [R50](../studies/R50-filtered-particle-search/) (filtered multi-sheet search),
  [R54](../studies/R54-compound-modes/) (compound modes on T⁶),
  [R56](../studies/R56-electron-shells/) (shell routing — Ma vs S),
  [R57](../studies/R57-energy-routing/) (Ma-vs-S energy routing engine).

---

## 1. The setup

QFT treats a photon's energy as quantized (`E = ℏω`) while
treating `ω` as continuous.  The apparent "quantum +
continuum at once" is a finite-vs-infinite distinction, not
a deep physical one: in a box of size L, `ω_n = 2πnc/L` is
discrete.

MaSt makes Ma the box.  The three torus sheets are
intrinsically compact, so their modes are intrinsically
discrete.  Mass is the rest-frame side of the same energy
relation,

<!-- E² = p²c² + m²c⁴ -->
$$
E^2 = p^2c^2 + m^2c^4
$$

with `m` drawn from a discrete Ma-mode set and `p` varying
continuously in S.  Concretely, for a single-sheet mode
`(n_t, n_r)` under the R49 convention,

<!-- μ²(n_t, n_r, ε, s) = (n_t/ε)² + (n_r − n_t·s)² -->
$$
\mu^2(n_t, n_r, \varepsilon, s) = (n_t/\varepsilon)^2 + (n_r - n_t \cdot s)^2,
\qquad m = E_0 \sqrt{\mu^2}.
$$

The shears are generically irrational (`s_ν = 0.022`,
`s_e ≈ 2.004`, …), so √μ² is irrational — but that affects
*commensurability*, not *enumerability*.  The mode set
remains countable and finite below any mass ceiling.

This suggests a concrete object worth computing: the
**complete discrete mass atlas** of MaSt — a ranked list of
every allowed eigenmode, spanning all three sheets, their
compound combinations, and their cross-sheet couplings, with
each mass a specific `√μ² × E₀` determined by the geometry.

## 2. What "computable" would mean

Given model-F parameters (three sheet radii, six internal
shears, cross-shears, Z₃ selection, spin-statistics filter):

1. Enumerate all 6-tuples
   `(n_et, n_er, n_νt, n_νr, n_pt, n_pr)` up to some
   `|n| ≤ N_max`.
2. Apply mode-existence filters (winding constraints,
   `n_pt ≡ 0 (mod 3)` for free p-sheet modes,
   spin/statistics from [Q124](Q124-spin-in-mast.md)).
3. Solve the joint metric eigenvalue problem for each
   allowed tuple.
4. Output: a sorted list of masses `m_i = E₀ × √μ²_i`.

Partial versions exist:
  [R27](../studies/R27-bound-states/) (discovery engine),
  [R28](../studies/R28-particle-spectrum/) (~48 bands, ~900
  modes below 2 GeV),
  [R50 T8](../studies/R50-filtered-particle-search/) (20-
  particle viability sweep across four sign branches),
  [R54](../studies/R54-compound-modes/) (18-of-20 compound
  modes spin-correct).

What nobody has produced yet: a **single mass axis** with
all of Ma's allowed modes plotted on it, meta-structure
(gaps, clusters, approximate commensurability) characterized,
observed particles located, and predictions read off.

## 3. Why Ma alone isn't enough — S must enter

The atlas above treats every mode as a single confined
excitation.  At high enough `n`, this fails energetically.

Consider a high-harmonic mode on the electron sheet.  As `n`
grows, `m = E_0^e × √μ²` grows.  At some point

<!-- E_split = Σ m_lower + V_S(separation) < E_single -->
$$
\underbrace{E_{\text{single}}(\mathbf{n})}_{\text{one stacked mode}}
\;>\;
\min_{\text{splits}} \Big[\; \sum_i m_{\text{lower}}(\mathbf{n}_i)
\;+\; V_S(\text{positions}) \;\Big].
$$

Beyond that threshold the putative high-`n` mode is not
realized — energy routes instead to multi-particle
configurations sitting at distinct points in S with a
Coulomb / weak / elastic separation cost.

This isn't hypothetical.
[R56](../studies/R56-electron-shells/) showed it for atomic
shells: when the Ma torus at a given Bohr radius fills
(`l(l+1) < n²` capacity), the next electron routes to S
(next shell) because separation is ~2.5× cheaper than
promoting to the next harmonic — reproducing shell
capacities `2n²` exactly.
[R57](../studies/R57-energy-routing/) generalized this as
an energy-routing engine: given an input energy and a
starting configuration, predict whether energy accumulates
in Ma (dark modes, higher harmonics) or forges new
particles in S.

**Consequence:** a complete atlas needs a per-mode ceiling
computed against the best split-and-separate alternative.
The atlas is not just a solve-and-sort; it's a recursion.

## 4. What "S in the metric" means here

MaSt's current metric is 9D internal (three sheets × three
internal directions, with cross couplings).  S is treated
separately as the ambient 3+1D manifold where modes
propagate.  For the atlas question S must enter the energy
accounting — not as a compactified internal direction, but
as a degree of freedom that competes with Ma stacking.

Operationally the extension is modest:

- S stays continuous (no compactification required).
- Add a separation-energy term `V_S(positions)` to the
  Hamiltonian of any candidate multi-mode configuration.
- Compute `E_split` and `E_single` for every mode and
  retain whichever is lower.

What `V_S` contains depends on which forces are active:
Coulomb for charged sub-modes, contact / weak for neutral
ones, possibly a GRID-derived gravitational term at extreme
mass.  A minimal viable model would be Coulomb-only — the
dominant contribution for any charged split — and flag
neutral splits as upper-bound estimates.

## 5. Concrete questions the atlas could answer

1. **Mass gaps.**  Are there mass ranges where *no* atlas-
   stable mode exists?  These are falsifiable negative
   predictions ("no new particle will be found between X
   and Y MeV").
2. **Clustering.**  Do observed particles sit at
   conspicuous positions — local minima of mode density,
   intersections of sheet ladders, or near-rational
   multiples of `E_0^ν`?
3. **Effective continuity above a threshold.**  R28 hit a
   predictive horizon near 2 GeV.  Is this the spectrum
   going operationally continuous via compound mixing, or
   just a finite-`N_max` artifact?
4. **Stable-mode filter.**  A mode is *atlas-stable* iff
   (a) its tuple passes selection rules AND (b) it beats
   every split-and-separate alternative by some margin ε.
   This converts the raw Ma enumeration into a "physical"
   atlas.
5. **Undiscovered particles.**  Any atlas-stable mode below
   current experimental reach that doesn't match a known
   particle is a prediction — or, if no such modes exist,
   that is itself a non-trivial closure statement.
6. **Quantum-of-mass check.**  Is there an approximate base
   unit such that most atlas-stable masses lie near integer
   (or simple rational) multiples of it?  Exact
   commensurability is blocked by shear irrationality, but
   approximate clustering is an empirical question.

## 6. Obstacles and prerequisites

Before promoting this to a study:

1. **A defensible `V_S` model.**  Coulomb for charged modes
   is straightforward.  Neutral modes (e.g., neutrino-only
   splits) need a contact or weak-range cost that MaSt does
   not currently supply in derivable form.  An initial
   upper-bound estimate is fine but needs to be labeled as
   such.
2. **Recursion convention.**  Atlas-stability depends on
   which lower modes are available to split into — which in
   turn depends on atlas-stability.  Probably: iterate to
   fixed point starting from the observed particle set as
   the seed of "definitely stable" modes.
3. **Enumeration cutoff.**  `N_max` is bounded by
   computational cost and by the physical ceiling
   (R28's ~2 GeV horizon is a natural first choice).
4. **Visualization.**  Log-scale mass axis with all
   atlas-stable modes marked, observed particles labeled,
   density structure highlighted.  The atlas is useful only
   if its structure is legible.

If all four are tractable, a focused study is warranted
(candidate R63 — see
[studies/STATUS.md](../studies/STATUS.md) Backlog).

## 7. Relation to prior framings

The atlas sits at the junction of several existing threads:

- **Ma mode enumeration** (R27, R28, R50, R54) — gives the
  raw mode set.  Never synthesized into a single 1D scale
  with meta-structure analysis.
- **Energy routing** (R56, R57) — gives the Ma-vs-S
  tradeoff mechanism.  Applied case-by-case (shells, p→n
  transition), not as a general filter over the full mode
  set.
- **Composite fission / gcd criterion** ([Q109](Q109-mode-stability-and-composite-fission.md))
  — identifies one specific failure mode for high-`n` modes
  (gcd > 1 admits a cleaner lower-energy factor).  A piece
  of the split-and-separate logic, not the whole of it.
- **Shell saturation** ([Q108](Q108-shell-capacity-from-knot-saturation.md))
  — the atomic analogue.  Atlas-level version would apply
  the same reasoning to elementary-particle modes.

The atlas is the object where these threads converge.

## 8. Status

Framing only.  The Ma-only enumeration is computable
today with existing infrastructure (model-F parameters +
R54's compound-mode solver).  The Ma+S extension requires
the `V_S` model of §6 before a full atlas can be produced.
The conceptual payoff — a single 1D discrete scale
containing the predicted rest-mass spectrum of MaSt, with
gaps and clusters that observation can check — is high
enough to warrant developing the prerequisites before
attempting the computation.
