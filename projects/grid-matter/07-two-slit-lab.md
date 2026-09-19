# Chapter 7 — The two-slit lab

Act 2 asks whether GRID produces quantum mechanics, and the two-slit experiment is
where that question is traditionally staged. This chapter builds the apparatus in
substrate terms and shows interference — including, importantly, interference of a
genuine *matter* wave, not only light. It is deliberately honest that the
interference itself is still classical wave physics; the quantum content arrives in
Chapters 8–10.

## §1 The GRID reading of the apparatus

In substrate terms the apparatus is a single continuous network with obstacles. A
**barrier** is a region of nodes blocked by mass — encumbered, non-transmitting; a
**slit** is **open GRID** — an unencumbered channel that transmits freely. A
two-slit screen is therefore continuous GRID everywhere except two open channels,
and the whole lab sits *inside* one connected medium rather than being a source, a
mask, and a detector in otherwise empty space. **[forma framing]**

## §2 Interference — photon and matter

Running a broad coherent wavefront at the screen, the two transmitted beams overlap
and interfere at the backdrop: information from *both* slits reaches each detector
point. The important step, relative to earlier passes, is to do this for a matter
wave and not only for light. Two runs on the *same* GRID lattice
([work/dualslit-matter-result.md](work/dualslit-matter-result.md)) settle it:

- a **photon** — the massless, c-uniform mode, i.e. the Maxwell sector GRID already
  possessed — produces fringes; and **[C]**
- a **matter wave** — the compact n=1 mode, genuinely massive with rest frequency
  ω₀ = 0.30 — produces fringes too. The two-slit is thus a real matter-wave
  demonstration, not merely a restatement of classical optics. **[C]**

In both cases a **one-slit control** gives a single lobe with no fringes, so the
structure at the backdrop is two-slit interference and not single-slit
diffraction ripple — information from *both* slits reaches each detector point.
**[C]**

The pattern is **mass-dependent, in the direction de Broglie requires**. The
massive mode has a longer in-plane (de Broglie) wavelength than the photon —
**11.18 versus 8.07 lattice nodes** — and its fringes are correspondingly
**coarser** (fringe period 32.4 ± 4.6 versus 25.9 ± 2.9 nodes, by FFT of the
backdrop). Those wavelengths are obtained two ways
that agree: solved from the lab's dispersion relation, and **measured** by FFT of
the field, 11.35 ± 0.48 and 8.13 ± 0.25 nodes. **[C, and D for λ]**

(The lab needs two extended dimensions plus the compact c, so it runs on the
three-axis, N=6 generalization of Chapter 4's two-axis cylinder, with lattice
light-speed c = 1/√3 rather than 1/√2. The mass mechanism is identical — the
compact term cos k_c lowers the in-plane wavenumber, lengthening λ. Three axes
also make the *scatter convention* matter for the first time: the two register
labelings the repo carries agree at two axes but not beyond, and only one of them
is isotropic. The lab uses that one. See
[work/dispersion-analytic.md](work/dispersion-analytic.md) §d-axis generalization
and [review.md](review.md).)

## §3 Honest scope

Two honest limits keep this chapter from claiming too much. First, the interference
is **classical linear-wave behavior**: both the photon and the matter mode are
linear Bloch waves (Chapter 4), so the matter case follows from the photon case *by
linearity* rather than by anything new — it is necessary staging, not yet
distinctively quantum. The distinctively quantum content is the single
whole-quantum click (Chapter 8) and what that click implies about measurement
(Chapters 9–10). **[honest]**

Second, the paraxial two-slit law Δ = λL/d is now *consistent with* the lab but
not sharply tested by it. With the lab isotropic it predicts 23.6 nodes for the
photon and 32.6 for the matter wave, against measured fringe periods of
**25.9 ± 2.9 and 32.4 ± 4.6** — agreement within the measurement's resolution,
where the earlier anisotropic run missed by a factor ~3, far outside it. But the
resolution is only about one FFT bin (~10–15% at these periods), and the geometry
sits in the near-field (Fresnel number d²/λL ≈ 2), where λL/d is not strictly the
governing formula anyway. So this is a consistency check passed, not a precision
confirmation. The firmly supported claims remain the directional one (matter
interferes, coarser than the photon) and the de Broglie wavelength, which is now
both derived and measured. **[honest]**

## Attribution / dependencies

The de Broglie wavelength is Chapter 4's; the fringe geometry is standard wave
optics. The result feeds Chapters 8–10.
