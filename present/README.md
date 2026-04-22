# Presentations

Slide decks built with [Marp](https://marp.app/) — plain markdown compiled to HTML, PDF, or PPTX.

## Quick Start

### Prerequisites

```bash
npm install -g @marp-team/marp-cli @mermaid-js/mermaid-cli
```

These install to `~/.npm-global/bin/` (user-local, not system-wide).

### Workflow

Each presentation lives in its own sub-folder:

```
presentations/
  sample/
    deck.md              # slide source (Marp markdown)
    images/
      energy-flow.mmd    # diagram source (Mermaid)
      energy-flow.svg    # auto-generated from .mmd (git-ignored)
      sample-figure.png  # static images you provide
    Makefile             # build commands
    build/               # output (git-ignored)
```

### Writing Slides

- Slides are separated by `---` on its own line
- First slide's front-matter (`---` block) sets Marp options
- Images use standard markdown: `![alt](images/file.png)`
- Math uses `$$` blocks (MathJax) — same notation as our papers

### Diagrams (Mermaid)

Author diagrams as `.mmd` files in `images/`. The Makefile auto-renders them to SVG before building the deck.

```bash
# Render diagrams only
make diagrams

# Or just build — diagrams render automatically
make html
```

In the slide markdown, reference the SVG output (not the `.mmd` source):

```markdown
![center w:600](images/energy-flow.svg)
```

### Build Commands

From a presentation folder (e.g. `presentations/sample/`):

| Command | What it does |
|---------|-------------|
| `make html` | Build self-contained HTML slide deck |
| `make pdf` | Build PDF (requires Chrome/Chromium) |
| `make pptx` | Build PowerPoint file |
| `make all` | Build all three formats |
| `make serve` | Live-preview in browser (auto-reloads on save) |
| `make diagrams` | Render `.mmd` → `.svg` only |
| `make clean` | Delete `build/` and generated SVGs |

### Live Preview (Recommended for Authoring)

```bash
cd presentations/sample
make serve
```

Opens a browser window that hot-reloads on save.

### Sharing

Only the **author** needs `marp` and `mmdc` installed. The built HTML file is self-contained — anyone with a browser can view it, no installs needed.

### VS Code / Cursor integration — live preview (recommended)

1. Install the **Marp for VS Code** extension (`marp-team.marp-vscode`) in Cursor (same as VS Code).
2. Open a `deck.md` (e.g. `present/mast-intro/deck.md`).
3. Open the **Marp** preview:
   - **Command palette** (`Cmd+Shift+P` / `Ctrl+Shift+P`) → *Marp: Open Preview* (splits the editor), or
   - The **Marp** icon in the top-right of the editor, or
   - Right-click the tab → *Open Preview* if the extension adds that.

The preview is **WYSIWYG** for HTML export: you see 16:9 slide boundaries, tables, and MathJax like the built deck. If a slide still clips, tighten `style:` in the deck front-matter (smaller `font-size` on `section`, or add `class: tight` to individual slides) or split the slide at `---`.

**CLI alternative:** from the deck folder, `make serve` runs `marp --preview` in the browser (requires global `marp` CLI).

## Embedding Figures from `viz/`

For 3D figures built in `viz/`:

1. **Static snapshot** — capture a PNG from the viz, save to `images/`
2. **Animated** — record a GIF of the viz, embed in the slide
3. **Interactive link** — link to the live viz on GitHub Pages

## Conventions

- One folder per presentation
- Commit source (`deck.md`, `images/*.mmd`, `images/*.png`) but git-ignore `build/` and generated SVGs
- Name the main file `deck.md` for consistency
- Keep image paths relative (`images/foo.png`)
