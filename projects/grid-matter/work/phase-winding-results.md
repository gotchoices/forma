# Phase-field winding test — results (mechanism III)

Sim: [`../scripts/phase_cylinder.py`](../scripts/phase_cylinder.py) — the (x, c)
cylinder with **complex** edge amplitudes (a genuine U(1) phase / ℵ-line), the
minimal object needed to test candidate **III** (particle = topological phase
winding) against the gate ([binding-evaluation.md](binding-evaluation.md)).

## What passed

- **Topological protection (part of G5).** A unit c-winding stays **w = +1**
  through the whole run (start/end/min/max all +1), linear *and* under the
  value-bound. The phase cannot unwind — exactly the topological charge the real
  scalar could not carry. ✓ This is the genuine new thing a phase field buys.
- **A stable, localized, conserving winding *configuration exists*.** The
  all-edges winding IC holds **100% of its interior compact energy** out to 5000
  steps, conservation drift 0.004%, localized (rms width ~9). No dispersion, no
  loss. Strikingly stable — for a *linear* mode.

## What failed — the decisive test: mobility (G3)

That linear stability is the tell. **A localized mode in a translation-invariant
linear lattice can only stay localized if its group velocity is zero** — a flat
band. So the winding was tested for **mobility**: an x-momentum kick (`--kx`) on
the IC, sweeping kx = 0 → 1.0.

**Result: propagation speed = 0.000 at *every* kx.** The winding will not move.
It is an **immobile flat-band (compact-localized) state** — it cannot carry
momentum. A real particle must move (and Lorentz-boost); this cannot. So the
phase winding on the 1D-ring cylinder is **not a genuine particle**.

Corollaries:
- A **focusing** term (self-phase-modulation, `--focus 1`) does *not* rescue it —
  it **destabilizes**: the winding unwinds (w swings −2…+4) and the mode disperses
  (width 18 → 111). Strong SPM drives modulational instability, not a soliton.
- The value-bound (clip) leaves it immobile-and-stable (unchanged) — consistent
  with the defocusing finding: the bound neither binds nor mobilizes.

## Reading it (non-dogmatically)

The immobility traces to a structural fact of the **1D-ring** compact dimension:
the winding's stable energy lives on the **compact-circulating (±c) edges, which
have no x-transport channel** at all, while the x-transport (±x) edges radiate.
So the lattice offers only two winding states — **immobile-and-stable** or
**mobile-but-radiating** — never both. There is no *mobile, stable* winding.

This is **not** a refutation of mechanism III. It says the **1D ring is too
simple** — precisely the earlier concern that "c is merely a direction on a 2D
grid." A massive KK mode *should* disperse (ω² = k² + m², finite mass, mobile);
a **flat band (infinite effective mass)** is the artifact of the trivial compact
geometry. The natural fix is a **richer compact dimension — a 2D toroidal Ma
sheet** — whose own resonant modes could give the winding a real dispersion
(finite mass → mobility) while retaining topological protection.

## Gate status for III (updated)

| G1 | G2 | G3 contain | G4 | G5 charge | G6 mass | notes |
|----|----|-----------|----|-----------|---------|-------|
| ✓ | ✓✓ | ~ (localizes but **immobile** on 1D ring) | (needs I) | ✓ (winding protected) | ✗-so-far (flat band = ∞ mass, not a spectrum) | 1D ring too simple |

## Next test

Build the **2D-torus compact dimension** (replace the 1D c-ring with a 2D Ma
sheet) and repeat the winding **mobility** test: does a topological winding on
the torus acquire a **finite mass and move** (a real particle), while photons
still propagate and the winding stays protected? If yes, III is viable and the
1D-ring flat band was the artifact. If the winding is *still* immobile on the
torus, mechanism III has a deeper problem and the lattice-gas fallback (II)
returns. (G1 photon mobility is already established in
[cylinder.py](../scripts/cylinder.py) M1; the complex extension does not change
linear propagation.)
