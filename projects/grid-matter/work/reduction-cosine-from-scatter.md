# Reduction attempt: the on-site cosine from the impedance scatter

**Question (Ch 2's load-bearing gap):** is U(φ) = m²(1 − cos φ) — the potential
that makes a compact-phase field focusing+saturating (sine-Gordon) — *derivable*
from the GRID impedance scatter, or must it be *posited*?

**Verdict (honest): Ch 2 is a *conditional* derivation.** The scatter gives the
kinetic term; the cosine is **forced** once you grant *one* premise — that the
field value is a **compact phase (a circle), not a bounded amplitude (an
interval)**. That premise is a forma **foundational posit** (the ℵ-line for GRID
itself; a U(1) sheet-field for a particle), **not** a consequence of the bare
scatter. Given it, everything downstream follows rigorously.

## Two different "compact" things — keep them separate

| | compact **coordinate** | compact **field value** |
|---|---|---|
| what | a periodic *position* dimension | the *field's value* lives on a circle |
| examples | the c-ring; a **particle Ma sheet** (2D torus) | the **ℵ-line** phase; a sheet's **U(1)** phase (charge = winding) |
| gives | a **KK mass** m_n = n·(2π/L) — *quadratic* (½m²φ²) | a **periodic** potential — the cosine |
| alone → | a *linear* massive Klein–Gordon field → **disperses** (no breather) | nonlinear; the sine-Gordon ingredient |

This is the crux the early work missed: a **compact coordinate alone is KK →
quadratic mass → linear → disperses** (exactly the immobile/dispersing winding
results). The **breather needs the field *value* to be a phase.** The mass *scale*
comes from a compact coordinate; the *periodic form* comes from a compact
field-value.

## Step 1 — the scatter gives the kinetic term, and only that

S = (2/N)J − I is **linear** in the edge amplitudes. A linear map has **no on-site
potential**. In the continuum limit it is the coupling/Laplacian (∂²ₓφ) — the
"spring" between neighbours (established: it is what gives Maxwell/KG, and the
discrete sine-Gordon's coupling term). **The scatter cannot, by itself, produce any
on-site cosine** — nonlinearity is not in it.

## Step 2 — the topological fork the scatter does *not* fix

What *is* the edge's field value?

- **A bounded amplitude** — an interval [−b, b] (the **value-bound / saturation**).
  Its confining potential is a **wall** → *hardening* → **defocusing**. (This is
  the refuted entry hypothesis, and this is *why* it fails — a wall, not a well.)
- **A compact phase** — a circle [0, 2π) (the **ℵ-line**; a sheet's U(1)). Its
  potential must be **periodic** → the cosine → *softening* → **focusing**.

Interval vs. circle is a **topological choice of what the field value is**, and the
**bare scatter does not fix it.** Choosing the circle is the ℵ-line/sheet-phase
posit. *This single distinction resolves the whole "is saturation focusing?"
confusion: a clipped **amplitude** is defocusing; a compact **phase** is focusing.*

## Step 3 — given the circle, the cosine is *forced* (not an extra posit)

Grant that the field value is a phase φ ∈ [0, 2π), with φ ≡ φ+2π. Then **any**
potential must satisfy U(φ) = U(φ+2π) — periodic. If a compact *coordinate* also
gives the mode a **mass** m² (KK, Step-0 fact), that mass is the curvature of U at
its vacuum, U ≈ ½m²φ² near φ=0. The **minimal periodic potential with curvature m²
at 0 is**

    U(φ) = m²(1 − cos φ)   [since m²(1−cos φ) ≈ ½m²φ²],

with higher harmonics (cos 2φ, …) subleading. **So the cosine form is not a
separate assumption — it is the unique minimal periodic completion of the KK mass,
demanded by the phase (circle) topology.** Focusing (−φ⁴/24) + saturating (+φ⁶/720)
then follow by Taylor, and sine-Gordon gives **breather = mass, kink = charge**.

## What is derived vs. the one irreducible posit

- **Derived:** kinetic term (scatter); the mass scale m² (compact coordinate, KK);
  the cosine *form* and hence focusing+saturating (given the phase topology);
  breather/kink (sine-Gordon).
- **Posited (irreducible, from the bare scatter):** *the field value is a compact
  phase (a circle), not a bounded amplitude.* This is a **forma foundational
  input** — the ℵ-line is *defined* as a compact phase in the framework
  (grid-primitive), and a particle sheet must carry a **U(1)** for charge = winding
  ([metric-charge](../../metric-charge/)). It is not new or arbitrary, but it is
  **not derivable from S**.

## ℵ vs. a general compact dimension (per the standing distinction)

The cosine mechanism is **scale-blind — it applies to any compact *phase***:
- the **ℵ-line** (GRID's own, Planck scale) → a Planck-mass sine-Gordon sector
  (relevant to the photon/substrate level, not ordinary mass);
- a **particle Ma sheet's U(1)** (particle scale) → the real-mass breather/kink.
The *form* (cosine, focusing+saturating, breather=mass/kink=charge) is identical;
the *scale* is set by the compact coordinate's size (m ∝ 1/L). So a massive particle
is a breather/kink on **its sheet's phase**, not on the ℵ-line.

## Consequence for Ch 2 drafting

Ch 2 must be written as a **conditional derivation**, and honestly so:

> *Premise (foundational):* the compact field value is a phase (circle) — the
> ℵ-line for GRID, a U(1) for a particle sheet.
> *Then:* periodicity forces the KK mass into U = m²(1−cos φ) (focusing+saturating);
> sine-Gordon gives breather = mass and kink = charge; the scatter supplies the
> kinetic term.

That is a legitimate, rigorous chapter — it just states its one premise up front
rather than pretending S alone forces it. The **deep open question** (could some
GRID dynamics *force* the circle over the interval?) is flagged, not claimed.
