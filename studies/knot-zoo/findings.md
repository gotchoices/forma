# Findings: Knot Zoo Study

Running log of experiments, results, and their implications.
Entries are chronological. Each entry references the script that
produced it and the propositions from `theory.md` that it bears on.

---

## F1. Torus Knot Survey

**Script:** `scripts/01_knot_survey.py`
**Bears on:** P1 (spin classification), P2 (charge), P3 (mass ratios)

Enumerated all coprime (p,q) torus knots with p,q ≤ 7 and computed
spin, fermion/boson classification, and mass ratios.

### Fermion/boson classification — clean result

Odd p (tube windings) → fermion (π-twist per traversal, needs 2
circuits to restore the E-field → half-integer spin).

Even p → boson (2π-twist, restores in 1 circuit → integer spin).

This is a purely topological result and should be robust.

### Spin values — only q = 1 and q = 2 give known spins

The angular momentum about the torus axis (in the a << R limit) is:

    L_z = ℏ/q

This gives:
- **q = 1** → spin 1 (bosons if p even, fermions if p odd)
- **q = 2** → spin ½ (the electron — WvM's (1,2) knot)
- **q = 3** → spin 1/3 (non-physical for elementary particles)
- **q ≥ 3** → non-standard spins

Only q = 1 and q = 2 produce spins that match known particles.
This strongly constrains the zoo: physically relevant knots are
likely limited to the q = 1 and q = 2 families.

| q | Spin | Statistics | Relevant knots |
|---|------|-----------|---------------|
| 1 | 1 | p odd → fermion, p even → boson | (1,1), (2,1), (3,1), ... |
| 2 | ½ | all fermion (p must be odd for coprime) | (1,2), (3,2), (5,2), ... |

Note: q = 1, p = 1 is the (1,1) knot — the simplest closed curve
on a torus, going once around each way. It is a fermion with spin 1,
which is unusual (fermions normally have half-integer spin). This
suggests the spin formula may need refinement, or (1,1) is exotic.

### Mass ratios — fixed torus doesn't work

On a single torus (fixed R, a), all knots with p > 1 or q > 2 have
longer path lengths than the (1,2) electron, meaning lower photon
energy and lower mass. All computed m/m_e ratios are < 1. This
cannot explain the muon (206.8× m_e) or tau (3477× m_e).

**Key realization:** In WvM, R = λ/(4π) is set by the particle's
own Compton wavelength. A heavier particle has a smaller Compton
wavelength and a smaller torus:

    R_{particle} = λ_{particle} / (4π) = h / (4π m c)

So R_μ = R_e/206.8 and R_τ = R_e/3477. Different particles live
on different-sized tori, not on the same one.

### Important distinction: orbit vs field extent

The a/R = 1/√(πα) ≈ 6.60 from study 2 describes the **field extent**
(how far the E-field reaches from the orbit), not the physical tube
of the torus. The photon orbits on a thin torus (a_orbit << R) and
the spin ½ comes from this tight orbit. The field extends much
further (to the rotation horizon), and this extended field determines
the charge.

For the spin calculation, the relevant parameter is the orbit, not
the field extent. So spin = ℏ/q holds even though a_field/R ≈ 6.6.

### Open questions from F1

1. **Why only q = 1, 2?** Is there a physical selection rule that
   eliminates q ≥ 3, or could exotic particles with non-standard
   spin exist?

2. **What determines the mass?** If different particles have different
   torus sizes, what selects the torus size (and hence the mass)?
   The WvM model does not answer this — mass is an input.
   **However:** if the torus is reframed as a fixed compact extra
   dimension (see F2 below), mass comes from photon energy, not
   torus size. This resolves the mass problem entirely. See the
   "compact dimension and mass spectrum" future study in
   `../README.md`.

3. **Do higher-p knots on q = 2 correspond to heavier fermions?**
   (3,2) and (5,2) are spin-½ fermions. On a fixed torus they are
   lighter (longer path), but higher harmonics (n > 1) of the same
   knot could be heavier. Alternatively, different particle types
   might live in different compact dimensions.

4. **Charge for different knots.** Does the charge derivation
   (q = e via a/R = 1/√(πα)) change for different (p,q)? Or is
   it universal? The field topology may differ for higher-p knots.
   Fractional charges (1/3, 2/3 for quarks) are a key test.

5. **Photon as trivial case.** The free photon is not a knot — it
   is the unconfined building block. A photon traversing ordinary
   (non-compact) space is massless and has spin 1 without any
   toroidal topology. Modeling it as a knot of itself is circular.

---

## F2. Compact Dimension Reframing

**No script** — conceptual analysis
**Bears on:** P3 (mass ratios), theory.md §4

### The confinement problem dissolves

WvM's biggest weakness is the unknown confinement mechanism: what
forces a photon into a toroidal orbit? This problem disappears under
a different interpretation:

**Interpretation A (WvM original):** The photon orbits in our 3D space.
Something confines it. No known force can do this.

**Interpretation B (compact dimension):** The torus IS an extra
dimension of spacetime — compact, fixed in size, orthogonal to (x,y,z).
The photon follows a geodesic (straight line) in this space. No force
is needed: a straight line on a compact space is already closed.

This is the Kaluza-Klein idea (1919–1926): charge emerges from momentum
in a compactified dimension. WvM's charge derivation is a specific
instance of this.

### Mass from photon energy, not torus size

Under interpretation B, the torus dimensions (R, a) are properties of
spacetime — fixed, shared by all particles. The photon's energy is a
separate parameter that determines the particle mass:

    m = E/c² = h/(λc)

The knot topology (p,q) determines quantum numbers (spin, charge).
The photon energy determines mass. These are independent.

Quantization: the photon wavelength must fit the closed path
(constructive interference). On a path of length L, allowed
wavelengths are λ = L/n, giving:

    m_n = nh/(Lc)    for n = 1, 2, 3, ...

The fundamental (n=1) is the lightest particle for that knot type.
Higher harmonics (n > 1) are heavier particles with the same quantum
numbers.

### Two sub-models

**Shared dimension:** All particles live on one fixed torus. Different
knots give different quantum numbers. Harmonics give the mass spectrum.
Testable prediction: lepton mass ratios should be integers
(m_μ/m_e ≈ 207, m_τ/m_e ≈ 3477). If not exact integers, the model
needs refinement.

**Per-particle dimensions:** Electron and quarks each have their own
compact dimension (a small number: perhaps 1 for leptons, 1 for
quarks). This is cleaner if mass ratios don't fit integer harmonics,
and it's still economical — 2 or 3 extra dimensions vs string theory's
6–7.

### Implications for this study

This reframing is significant enough to warrant its own study. The
knot-zoo study can continue with topological classification (spin,
charge, fermion/boson) without committing to either mass model. The
mass spectrum question — harmonics on a fixed torus vs separate
dimensions — should be explored in a dedicated "compact dimension"
study.

### Why this matters

If the compact dimension picture works:
- No confinement problem (geodesic on compact space)
- Mass from photon energy (not a free parameter per particle)
- Spin from topology (robust, not approximate)
- Charge from field geometry (as in study 2)
- Small number of extra dimensions (1–3, not 6–7)
- Particles are literally just photons on different paths
