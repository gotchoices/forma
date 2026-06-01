# k5-manifold.md — the K5 five-torus reframing of ma-domain

**Status:** Exploratory hypothesis under active development. Proposed as a generalization track parallel to [cand-QY-ED.md](cand-QY-ED.md) (the K4 candidate). K4's mass-fit results survive unchanged inside K5 as the dominant low-energy 2-torus modes; K5 adds a fifth dim (the neutrino circle), opens new substrates, and reframes the conservation laws as broken-U(1) survivors. Where K4 *assumes* the sheet model and fits, K5 *derives* the sheet model as the energy-optimal mode-support pattern on a single 5-torus.

This file sets the framework. Subsequent work files will run the mode sweep, work the conservation case, and address specific target particles.

---

## 1. Hypothesis

The Ma substrate of [architecture.md §1](architecture.md) is treated, for this track, as a single 5-torus on (d1, d2, d3, d4, d5). There are no sheets, curves, or lower-dimensional substrates *imposed* on the manifold. Every particle is a closure-satisfying mode on the 5-torus, with integer windings on each dim. A mode that happens to have nonzero windings on only two dims is what the existing project calls "a 2-torus sheet mode"; a mode with one nonzero winding is a "1D-curve mode" (the NC neutrino picture); a mode with three or more nonzero windings is a multi-dim mode the existing project has not catalogued.

**Two consequences fall out immediately:**

- The "sheet restriction" in [architecture.md §3.3](architecture.md) is reread as an empirical *result* — most low-energy modes have support on exactly two dims because that minimizes total energy under the closure rule. It is not a structural ban on higher-dim modes; those exist but are typically heavier.
- The R1 rule from [candidates.md](candidates.md) (no two sheets on one pair) becomes irrelevant. Conflicts between modes that would otherwise overlap are resolved energetically (the lower-energy mode is realized) rather than structurally.

---

## 2. Naming convention: d1..d5, size-ordered

K5 adopts `d` (dim) labels instead of K4's `m` labels, both to mark the framework change and to restore the size-ordering convention of [architecture.md §1](architecture.md#L29-L33) that K4 broke locally. **By convention: d1 smallest, d5 largest.**

### 2.1 Translation table from K4 to K5

| K5 label | Role | Size (K4 best-fit combo) | K4 label |
|---|---|---|---|
| d1 | b/t quark spoke | ≈ 0.0073 fm (pinned) | m3 |
| d2 | s/c quark spoke | ≈ 0.91–1.05 fm | m2 |
| d3 | quark hub | ≈ 181–493 fm | m4 |
| d4 | u/d quark spoke | ≥ 2400 fm (range) | m1 |
| d5 | neutrino circle | ≥ 4 cm | (new) |

### 2.2 The d4 < d5 stipulation

K4's manifold permits m1 (= d4) up to ~10¹⁵ fm, which would let d4 exceed d5's ~4 cm floor in some range. K5 stipulates **d4 < d5** as a structural assumption, justified by:

- No observed particle is lighter than the lightest neutrino mass eigenstate (~30 meV). If d5 is to set the neutrino mass floor and the framework's stability story (§5) anchors stability at the lowest available substrate, the neutrino dim should be the largest.
- It puts d4/d3 ≈ 12 (sensible ratio) and keeps the electron's required L ≳ 2400 fm comfortably inside d4's range.

If the mode sweep produces a conflict (e.g., a low-energy mode that requires d4 > d5), the assumption is revisited.

---

## 3. Mode descriptor and substrate notation

### 3.1 The 5-tuple

A mode is labelled by integer windings on each dim:

> {n₁, n₂, n₃, n₄, n₅}

This is the natural restriction of [architecture.md §2](architecture.md#L40-L51)'s 11-tuple to the Ma block. Modes are sorted by the number of *nonzero* entries:

- **1-winding modes** — exactly one n_i ≠ 0. Live on a single dim. Spin 0 candidates (no second dim to twist over → integer spin).
- **2-winding modes** — exactly two n_i ≠ 0. The familiar 2-torus sheets. Spin ½ candidates (the (1, 2) WvM construction).
- **3-winding modes** — three n_i ≠ 0. Cross-sheet bound states (target case: doubly-charmed baryons).
- **4-, 5-winding modes** — heavier still; expected to be rare or absent in the observed spectrum.

### 3.2 Substrate-support notation

The existing `Ma(i, j)` pair notation extends naturally:

- `Ma(i)` — a 1-winding mode's support (a single closed dim — what NC calls a "1D curve")
- `Ma(i, j)` — a 2-winding mode's support (a 2-torus — the current sheet model)
- `Ma(i, j, k)` — a 3-winding mode's support (a 3-torus)
- `Ma(i, j, k, l)`, `Ma(1..5)` — higher

### 3.3 Closure on multi-dim substrates — open

The 2-torus closure rule `m_t | m_r` (from [architecture.md §3.3.1](architecture.md#L104-L119)) is derived for one tube + one ring. The analogue for 3-tori and higher is open. The mode sweep cannot run rigorously without it; a working stand-in for v1 is "every pair of nonzero windings within a multi-dim mode independently satisfies m_t | m_r," but this may over- or under-count.

---

## 4. Substrate inventory

C(5, 2) = 10 pairs; C(5, 3) = 10 triples; C(5, 4) = 5 quadruples; one 5-torus.

### 4.1 The 10 pairs Ma(i, j) — what K4 occupies and what's new

| Pair | Role in K4 | Status in K5 |
|---|---|---|
| Ma(d1, d2) | electron μ-leg (b/t × s/c spokes) | occupied — μ at T(1, 2) |
| Ma(d1, d3) | quark b/t sheet | occupied — b at T(1, 2), t at T(1, 1) |
| Ma(d1, d4) | electron e-leg (b/t × u/d spokes) | occupied — e at T(1, 2) |
| Ma(d2, d3) | quark s/c sheet | occupied — s at T(1, 2), c at T(1, 1) |
| Ma(d2, d4) | electron τ-leg (s/c × u/d spokes) | occupied — τ at T(1, 2) |
| Ma(d3, d4) | quark u/d sheet | occupied — u at T(1, 2), d at T(1, 1) |
| **Ma(d1, d5)** | — | **new** — candidate ν host (smallest companion → heaviest ν) |
| **Ma(d2, d5)** | — | **new** — candidate ν host |
| **Ma(d3, d5)** | — | **new** — open candidate (hub × ν) |
| **Ma(d4, d5)** | — | **new** — candidate ν host (largest companion → lightest ν) |

K4's 6 sheets are exactly the C(4, 2) = 6 pairs on (d1..d4), filled at machine precision. K5's 4 new pairs all involve d5. **All 10 pairs are admissible substrates by default**; the sweep decides which actually host observed modes. No a-priori exclusions in v1 — the model has no current reason to forbid any pair. If the sweep produces a low-energy charged mode on a pair that doesn't correspond to a known particle (a "ghost"), that is the cue to look for a structural exclusion reason; until then, every pair stays in.

**Future exclusion criterion to keep in mind:** if any two dims turn out to be *co-planar* under the spatial-relationships reading of §6, that would be a structural argument to forbid their 2-torus pair. No such determination is made in v1.

### 4.2 3-tori Ma(i, j, k) — first targets

The 10 triples are all candidate substrates for cross-sheet modes. First targets:

- **Ma(d2, d3, d4)** — combines two quark sheets via shared hub. Natural home for doubly-charmed baryons (Ξcc-like, ucc) that K4 cannot host on any single 2-torus. (§7)
- **Ma(d1, d3, d4)** — analogous for bottom + up generations.
- **Ma(d3, d4, d5)** — quark hub × u/d spoke × neutrino. Potential channel for weak interactions involving u/d and ν.

The other 7 triples are open until a sweep shows whether any hosts an observed mode.

### 4.3 Higher substrates

4-tori and the full 5-torus are admissible by the framework; no specific targets identified yet. Expected to be heavy or absent.

---

## 5. Stability model

**All observed particles are eigenmodes — exact, not approximate.** The "exact match → stable / near-miss → unstable" rule of the R-series studies is replaced by:

> **A mode is stable if no combination of lower-energy modes plus photons (or other massless quanta) can sum to its energy while conserving every survived quantum number (§6). Otherwise it decays through whichever such channel is open.**

Worked applications:

- **Lightest ν eigenstate.** No mode below it. Stable.
- **Electron.** Energetically could become ~10⁵ neutrinos; blocked by charge conservation. Stable.
- **Proton.** Energetically could become e + ν's; blocked by baryon-number conservation (§6). Stable.
- **Neutron.** A nearby mode on the quark substrate. Lower modes (proton + electron + ν̄) sum to ~939 MeV against neutron's ~940 MeV; channel is open and all quantum numbers conserved. Decays.
- **Higher-mass modes.** A decay channel almost always exists; the question is rate, not whether.

This shifts the framework's central question from "do the eigenmode energies match observed masses?" (already yes, by construction) to "**which mode is realized as the lowest in each conserved-quantum-number sector?**"

---

## 6. Conservation laws — a later track

**K5 v1 does not pursue conservation laws.** The mode sweep (§8) enumerates modes and matches them to particles; the conservation-laws track begins only after particle locations on the manifold are known.

The working hypothesis the later track will pursue: each compact dim d_i carries its own SO(2)/U(1) rotation symmetry, so in the absence of cross-coupling the manifold has full U(1)⁵ symmetry and the five winding numbers are five independently conserved integer quantum numbers. The cross-term content of the metric — the (σ, τ, P) triplets per pair from [architecture.md §3.4](architecture.md#L121-L164) — breaks some of this symmetry by mixing rotations on coupled dims. What survives the breaking pattern would be the conserved quantum numbers.

**The dictionary the later track will try to fill in:**

- **Charge (Q)** — a U(1) acting on whichever sub-manifold carries the WvM (1, 2) construction
- **Lepton number (L)** — a U(1) preserved across the lepton substrates; geometrically, the momentum on one lepton sheet would be offset by an opposite momentum on the paired ν sheet
- **Baryon number (B)** — a U(1) tied to the quark substrates, plausibly an angular-momentum invariant tied to d3 (the quark hub)
- **Color** — a Z₃ or U(1) subgroup carried by the per-sheet τ = 1/3 twist of the clover cross-section in [clover-quarks](../../sheet-proton/work/clover-quarks.md)
- **Spin** — angular momentum on the substrate of the mode itself; spin 0 from 1-winding modes, spin ½ from 2-winding modes with the (1, 2) double-cover

The prerequisite for this work is the sweep: once each particle is located on a specific substrate, the cancellation pattern between sheets can be examined directly ("how does the electron sheet's angular momentum offset the ν sheet's?"). Until then, the framework here is stated, not derived.

If it holds, the payoff is concrete: charge quantization in integer units (each dim's U(1) is compact → integer-labelled representations), and a structural reason for *why* the SM's internal U(1)s exist — they would be rotation symmetries on the manifold rather than independent labels.

---

## 7. Target cases

### 7.1 The three neutrino mass eigenstates as 2D sheets

The K4 + NC picture hosts ν as a 1D-curve mode on a single extra dim. K5 replaces this with **three new 2-tori**: `Ma(d1, d5)`, `Ma(d2, d5)`, `Ma(d4, d5)`. Each hosts one ν mass eigenstate. Implications:

- **Spin ½ recovered structurally.** A 2-torus admits the WvM (1, 2) construction; ν spin ½ falls out the same way the electron's does, instead of needing NC's separate accounting.
- **Q = 0 from σ_eff = 0**, by the same mechanism as [config-neutrino.md §NS.5](config-neutrino.md#L81-L83) — sign-symmetric ±n mode pairs cancel charge. Applied per-sheet across the three new sheets.
- **Mass ordering tied to dim sizes.** Heaviest ν on the sheet with the smallest companion dim (Ma(d1, d5), since d1 is smallest), lightest on Ma(d4, d5). This is a *prediction* — the assignment of ν₁/ν₂/ν₃ to the three sheets is structurally pinned, not a fit choice. Whether it produces normal or inverted ordering is checked by the fit.
- **Constrains d4.** With three ν sheets all anchored to d5, the d4 dim's size enters the lightest-ν mass directly — gives a path to pinning d4 that K4 lacked.
- **Ma(d3, d5) — open candidate.** The fourth d5-pair (quark hub × ν) is not assigned to any neutrino mass eigenstate, but is admissible in the sweep (§4.1). Whether anything observed lives there is a sweep question.
- **NC's status.** Becomes an alternative reading rather than the working model. If the three-sheet picture fits, NC is the 1D-limit interpretation of the same modes; if it doesn't, NC remains in play.

### 7.2 Higgs — included in the sweep, not tuned for

The Higgs is spin 0 and ~125 GeV. Spin 0 fits naturally as a 1-winding mode (no second dim → no double-cover → integer spin), and the energy scale 2πℏc/d1 ≈ 170 GeV at d1's K4-fit size is in the right neighborhood — suggestive but not load-bearing. The sweep should include 1-winding modes across all five dims and report whatever lands near 125 GeV, or nothing.

**The model is not contorted to make the Higgs appear.** If the sweep finds a near-match on a regular-range dim, that's a hit. If not, the Higgs's home is an open question — possibly outside K5, possibly indicating a dim size K4 left under-constrained. Pinning a dim *to* the Higgs's mass is acceptable only if it doesn't displace particles already accounted for on that dim.

### 7.3 Doubly-charmed baryons (Ξcc-like)

Ξcc = ucc has two charm quarks (which K4 places on Ma(d2, d3) at T(1, 1)) and one up quark (Ma(d3, d4) at T(1, 2)). The two sheets share d3 but not d2 or d4, so K4 has no single 2-torus that hosts all three quarks. The natural K5 substrate is the 3-torus **Ma(d2, d3, d4)** — windings on d2 (for the c content), d3 (the shared hub), and d4 (for the u content). The exact mode structure (the analogue of the proton's T(3, 6) on this 3-torus) is the work to do.

---

## 8. Mode sweep — the immediate next step

**What's needed:** enumerate all closure-satisfying modes {n₁..n₅} up to an energy cutoff on the K5 manifold with the dim sizes of §2.1, compute each mode's mass, and report matches and misses against the observed particle spectrum (charged leptons, quarks, neutrinos, mesons, baryons, and at minimum the Higgs).

**Existing scripts:**

- [scripts/torus3d_modes.py](../scripts/torus3d_modes.py) — already enumerates 3-torus modes classified by number of nonzero windings and tests three candidate EM-coupling integrals. **The closest ancestor.** Generalizing from 3 dims to 5 is the natural starting point.
- [scripts/cand_solver.py](../scripts/cand_solver.py) — fits a pre-specified sheet topology to observed masses. *Not* a mode enumerator; useful only after the sweep identifies which modes to assign to which particles.

**Recommended approach:** extend `torus3d_modes.py` to general N-dim (or write a focused `k5_mode_sweep.py` modeled on it), parameterize the 5 dim sizes via argparse, enumerate up to a winding-magnitude cutoff, output a sorted spectrum CSV plus a particle-match report.

---

## 9. Open questions

1. **Closure rule on 3+-tori** — the multi-dim analogue of m_t | m_r. (§3.3)
2. **d4 vs d5 ordering** — stipulated d4 < d5 here; verify the sweep doesn't force the opposite. (§2.2)
3. **Pair-exclusion criteria** — none applied in v1, all 10 pairs admissible. Co-planar dim arrangements (under the spatial-relationships reading) would be a future reason to forbid a pair. (§4.1)
4. **Cross-term pattern on the full 5×5 d-block** — needed for the conservation-law track (deferred to follow-on work). (§6)
5. **NC's status** — alternative reading of the three new 2-torus ν sheets, or independent picture retained? (§7.1)
6. **What fills the 3-tori, 4-tori, 5-torus** — most are open until the sweep runs. (§4)
7. **Decay rates and lifetimes** — §5 says "channel open ⇒ decays," but the rate depends on mode-overlap integrals not yet specified.
8. **Higgs location** — if the sweep doesn't surface it at K4's existing dim sizes, where it lives is an open question. (§7.2)

---

## 10. Relation to K4 and the rest of ma-domain

K5 does not invalidate K4. K4's six 2-torus sheets are exactly six of the ten Ma(d_i, d_j) pairs in §4.1, and their machine-precision fits stand unchanged. What K5 adds:

- A reframing of the substrate (one 5-torus, not separate sheets and curves)
- Four new admissible 2-tori (the d5-involving pairs)
- Higher-dim substrates as legitimate (not energy-penalized exceptions)
- A structural account of conservation laws via U(1)⁵-breaking
- Specific target cases (Higgs, Ξcc, the three ν 2-torus sheets)

K4 stays as the validated low-energy 2-torus picture; K5 is the framework that aspires to derive it.

---

## 11. Cross-references

- [architecture.md](architecture.md) — Ma substrate, mode nomenclature, (σ, τ, P) pair-triplet
- [cand-QY-ED.md](cand-QY-ED.md) — the K4 candidate K5 generalizes
- [candidates.md](candidates.md) — R1 (becomes irrelevant in K5)
- [config-neutrino.md](config-neutrino.md) — NS (precedent for σ_eff = 0 → Q = 0); NC (1D ν curve, alternative reading)
- [neutrino-1D.md](neutrino-1D.md) — full NC development
- [electron-tube.md](electron-tube.md) — (1, 2) WvM construction inherited for the 2-torus ν sheets
- [config-quark.md](config-quark.md), [config-electron.md](config-electron.md) — sector configs
- [3-torus.md](3-torus.md) — plane-over-diagonal energy argument (recontextualized in §1)
- [scripts/torus3d_modes.py](../scripts/torus3d_modes.py) — ancestor script for the K5 sweep
- [scripts/cand_solver.py](../scripts/cand_solver.py) — post-sweep fitter
