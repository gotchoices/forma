# Agent Guidance

## Mission
- To assist the user perform scientific inquiry and discovery

## Audience
- Assume user has college level general engineering experience but is not necessarily a physics expert
- Do not assume the reader has special knowledge about the topic other than what exists in the project
- Explain new terms, variables, acronyms, conventions, principles etc where they might not be known or remembered

## Common Code
- Make use of common code and virtual environment where useful (./lib)

## Studies
- Frame and perform individual studies (./studies/*) for each granular area of study

## Visualizations
- Build tools to help the user visualize and understand difficult concepts (./viz)

## Formula Notation

All markdown files in this repo use a hybrid formula format for maximum readability in both raw source and rendered output:

**Simple inline expressions** — write directly in prose using Unicode:
> ε₀, μ₀, α ≈ 1/137, c = 1/√(ε₀μ₀), ∇·E = ρ

**Complex multi-level formulas** — a `$$` TeX display block preceded by a Unicode approximation in an HTML comment:
```
<!-- α(μ) = α₀ / (1 − (2α₀/3π) ln(μ/mₑ)) -->
$$
\alpha(\mu) = \frac{\alpha_0}{1 - \frac{2\alpha_0}{3\pi}\ln\frac{\mu}{m_e}}
$$
```
The comment is invisible when rendered but readable in raw source. The `$$` block renders as typeset math in any math-aware viewer (GitHub, Obsidian, etc.).

## Tickets (tess)

This project uses [tess](tess/) for AI-driven ticket management.
Read and follow the ticket workflow rules in tess/agent-rules/tickets.md.
Tickets are in the [tickets/](tickets/) directory.

## Editorial Comments
The user may edit comments into markdown files for agent consumption using the form:
<!--EC -->
When present, follow the enclosed instructions and/or integrate relevant content into the document where appropriate and then remove the comment.

## READMEs
- README files should contain relevant hyperlinks so that the site is navigable on github pages
