# Model: model-A (WvM / single-sheet lineage)

**Code / implementation:** Per-study scripts under `studies/S*`, `studies/R1-`…`R25-*/scripts/`; shared helpers in `studies/lib/` as each study added them. **No** unified six-dimensional metric engine — that begins with [`studies/lib/ma.py`](../studies/lib/ma.py) in the model-B era (R26+).  
**Study range (approximate):** **S1–S3**, then **R1 through R25** (chronologically before [`R26`](../studies/R26-neutrino-t4/README.md); see [`studies/STATUS.md`](../studies/STATUS.md) “Done” table up to and including R25).  
**Supersedes / superseded by:** Superseded by **model-B** (three material sheets, `ma.py`): [`model-B.md`](model-B.md) when drafted — conceptual handoff at **R26**.

---

## Summary

Model-A is the Williamson–van der Mark (WvM) toroidal photon picture, developed into a **single material sheet** (later named **Ma_e**) for the electron: (1,2) geodesic, shear-based charge (after R19), and a long series of refinements and null results. The program tried to hang **all** particle physics on that one sheet or on a **shared 3-torus** (e.g. R24–R25), without the **three separate sheets** (electron / neutrino / proton) and cross-shears of the successor model.

---

## Outcomes

*Skim here first; this era is mostly **closed** — strengths are qualitative and single-particle, ending in structural blockers for neutrinos.*

- **Electron on one sheet (strongest pillar):** With WvM + S2 geometry, **a/R = 1/√(πα)** ties torus shape to α and fixes charge in the WvM construction; R2 packages spin, mass, g-factor on **Ma_e** with **no free continuous parameters** once α and (1,2) are given ([`S2`](../studies/S2-toroid-geometry/README.md), [`R2`](../studies/R2-electron-compact/README.md)).
- **Knot / topology scan:** On a **single** torus, only the **(1,2)** knot class yields the WvM charge mechanism; other torus knots cancel ([`S3`](../studies/S3-knot-zoo/README.md)). A fixed torus cannot reproduce the full particle mass ladder ([`S3`](../studies/S3-knot-zoo/README.md) F1).
- **Series / deficit:** S1’s geometric-series fix for the ~9% charge deficit is a **null result** — the deficit is tied to cavity modeling, not a robust constant to sum ([`S1`](../studies/S1-toroid-series/README.md)).
- **Self-consistency:** S2’s headline **r ≈ 6.60** is not the self-consistent profile scale; R6 finds a different consistent geometry — the “magic ratio” is partly an artifact of what was held fixed ([`R6`](../studies/R6-field-profile/README.md)).
- **Charge mechanism vs multi-winding:** R8-style high winding can fix energy bookkeeping but **breaks** WvM commensurability → **zero** net charge in the same integral ([`R13`](../studies/R13-kk-charge-t3/README.md)); this frames the later α / charge tension carried into model-B.
- **Shear:** R19 gives a workable **shear-induced charge** story on Ma_e — KK as rigorous wave-theory upgrade to WvM’s classical picture ([`R19`](../studies/R19-shear-charge/README.md)).
- **Hadrons on one 3-torus:** R14’s three-photon linking model for quarks/protons is **ruled out**; charge follows **mode numbers**, not spatial linking of photons ([`R14`](../studies/R14-universal-geometry/README.md)).
- **Neutrino dead end (decisive):** On a single sheet, WvM links **charge and spin** to the same tube winding — **uncharged spin-½ fermions are impossible** ([`R25`](../studies/R25-neutrino-spin/README.md)). That structural result **forces** separate material sheets ([`R26`](../studies/R26-neutrino-t4/README.md)).

---

## Goals

- Explain the **electron** as a confined photon on a torus with **measured** charge, spin, mass, and g-factor.
- Test whether **geometric series**, **cavity shape**, and **knot class** resolve WvM’s charge deficit and the particle zoo on **one** torus.
- After R19: derive **α** from geometry where possible, and place **quarks / proton** on shared or harmonic constructions without importing the full Standard Model Lagrangian.
- Find a **neutrino** as a light fermion consistent with the same rules.

---

## Assumptions

- **WvM core:** Photon on a closed geodesic; charge from field / cavity geometry; spin from (1,2)-type double coverage where applicable.
- **Single electron sheet (Ma_e):** One 2-torus (two periodic angles) for the electron unless a study explicitly moves to a **3-torus** (R14, R24) for different physics questions.
- **α as input** for much of the era: fixing the torus requires a numerical α even when the *form* α(r, s) is derived later (R19).
- **Quark / proton programs** (R20–R22, etc.) assume modes or harmonics on **Ma_e** or embedding curvature — not yet the **proton sheet** Ma_p of model-B.

---

## Strategies / approach

- **S1–S3:** Baseline WvM charge, **a/R** scan, interactive **torus–sphere** visualization ([`viz/torus-explorer.html`](../viz/torus-explorer.html)), exhaustive **(p,q) knot** survey.
- **R1–R7, R11–R13, R17–R18:** KK vs WvM, capacitance / energy routes to α, **multi-winding**, **self-consistent fields**, stiffness — narrowing what can and cannot select the Compton-scale torus.
- **R19:** **Shear** on Ma_e as the symmetry-breaking route to charge and α(r, s).
- **R14:** One **3-torus** for all photons — topological linking hypothesis for hadrons (failed).
- **R20–R23:** Harmonics, curvature, **single-sheet** neutrino attempts — systematically blocked or underdetermined.
- **R24–R25:** **3-torus** kinematics for neutrino masses vs **spin** — closure at R25.

---

## Limitations

- **No unified Ma mode catalog** across electron, neutrino, and proton; **no** `ma.py`-style 6-tuple energies, charges, and spins in one matrix.
- **Proton** as electron + harmonics (R20) is descriptive; **quarks from shear** on one sheet fail (R19 tracks).
- **α** remains a **selection** problem: many routes sweep geometry without a unique *ab initio* α (documented through R15, R31, etc., mostly post–model-A in calendar time but the *single-sheet* root issue is already visible here).
- **R14** and **R24–R25** show that **adding dimensions** (3-torus) does not, by itself, fix neutrino spin without **splitting sheets**.

### Supersession

**R26** replaces the architecture: **Ma = three coupled material sheets** (Ma_e, Ma_ν, Ma_p) in a single **6D** material space, with **cross-shears** between sheets. That is the start of **model-B** (`ma.py`, later `ma_model.py`). The impetus is explicit in R26’s README: **R25** makes a neutrino on Ma_e **impossible** under WvM’s charge–spin linkage; giving the neutrino its **own sheet** is the minimal escape. Detailed writeup: [`model-B.md`](model-B.md) *(draft when added)*.

---

## References

- **Studies (primary):** [`S1`](../studies/S1-toroid-series/README.md), [`S2`](../studies/S2-toroid-geometry/README.md), [`S3`](../studies/S3-knot-zoo/README.md); **R1–R25** — see [`studies/STATUS.md`](../studies/STATUS.md) “Done” rows 1–23 (through **R25. Neutrino spin**); handoff at **R26**.
- **Papers / primers:** WvM source PDF and summary used from [`reference/`](../reference/) (e.g. linked in [`R2`](../studies/R2-electron-compact/README.md)).
- **Code / viz:** [`viz/torus-explorer.html`](../viz/torus-explorer.html) (S2); per-study `scripts/` under each study folder above.
