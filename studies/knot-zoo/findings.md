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

3. **Do higher-p knots on q = 2 correspond to heavier fermions?**
   (3,2) and (5,2) are spin-½ fermions. If they live on smaller
   tori (higher mass), could they be the muon and tau? What would
   set the mass ratio?

4. **Charge for different knots.** Does the charge derivation
   (q = e via a/R = 1/√(πα)) change for different (p,q)? Or is
   it universal? The field topology may differ for higher-p knots.

5. **Spin 1 bosons.** The (2,1) knot is a spin-1 boson. Could this
   model the photon (which IS a spin-1 boson)? That would be
   intriguingly circular: the WvM electron is a photon on a (1,2)
   knot, and the photon itself might be a photon on a (2,1) knot —
   or perhaps a free, unconfined photon is the trivial (0,1) or
   (1,0) case.
