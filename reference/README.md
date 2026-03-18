# Reference

Source material by others, and recorded conversations that have informed the project.

## Contents

- `WvM.pdf` — Williamson & van der Mark, "Is the electron a photon with toroidal topology?", *Annales de la Fondation Louis de Broglie*, Vol. 22 No. 2, 1997. The foundational paper for this project.
- `WvM-summary.md` — Living summary of the WvM paper: core claims, geometry, what it does and does not address, and corrections to earlier misreadings. Updated as understanding evolves.
- `gemini-tensors-compton-toroid.md` — Gemini conversation exploring tensors, the Compton wavelength, toroidal electron models, and a proposed "Harmonic Toroidal Fractal Theory."
- `claude-photon-knots-particle-structure.md` — Claude conversation starting from single-photon emitters and dipole radiation, ending with a substantive discussion of the refined WvM model: photon knots for electron/proton/neutron (no quarks), the 1/137 fine-structure-constant connection, and suggestions for next steps.
- `claude-epsilon-mu-alpha.md` — Claude conversation building ε₀ and μ₀ from first principles, through Maxwell's equations in natural units, the derivation and running of the fine structure constant α, coupling constant unification at the GUT scale, and the renormalization group perspective on "which α is fundamental."

## Formatting Conventions for Dialog Files

Dialog markdown files use a hybrid formula format optimized for both raw readability and rendered output:

**Simple inline expressions** — written directly in prose using Unicode:
> ε₀, μ₀, α ≈ 1/137, c = 1/√(ε₀μ₀), ∇·E = ρ

**Complex multi-level formulas** — display blocks with a Unicode approximation in an HTML comment on the preceding line (Variant B):
```
<!-- α(μ) = α₀ / (1 − (2α₀/3π) ln(μ/mₑ)) -->
$$
\alpha(\mu) = \frac{\alpha_0}{1 - \frac{2\alpha_0}{3\pi}\ln\frac{\mu}{m_e}}
$$
```
The comment is invisible when rendered (GitHub, Obsidian, etc.) but readable in raw source. The `$$` block renders as a typeset formula in any math-aware viewer.

**Saving source dialogs:** Save the `.html` page from the browser — it contains the original LaTeX source embedded in KaTeX annotation tags, which is needed for accurate formula recovery. Plain text copy-paste mangles all formulas and is not sufficient.
