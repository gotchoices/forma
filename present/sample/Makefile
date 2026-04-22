DECK   := deck.md
NAME   := $(basename $(DECK))
OUTDIR := build

HTML := $(OUTDIR)/$(NAME).html
PDF  := $(OUTDIR)/$(NAME).pdf
PPTX := $(OUTDIR)/$(NAME).pptx

MMD_SRC := $(wildcard images/*.mmd)
MMD_SVG := $(MMD_SRC:.mmd=.svg)

.PHONY: html pdf pptx all clean serve diagrams

diagrams: $(MMD_SVG)

images/%.svg: images/%.mmd
	mmdc -i $< -o $@

html: diagrams $(HTML)
pdf:  diagrams $(PDF)
pptx: diagrams $(PPTX)
all:  html pdf pptx

$(OUTDIR):
	mkdir -p $(OUTDIR)
	ln -sfn ../images $(OUTDIR)/images

$(HTML): $(DECK) $(MMD_SVG) | $(OUTDIR)
	marp --no-stdin $(DECK) -o $@ --html

$(PDF): $(DECK) $(MMD_SVG) | $(OUTDIR)
	marp --no-stdin $(DECK) -o $@ --html --allow-local-files

$(PPTX): $(DECK) $(MMD_SVG) | $(OUTDIR)
	marp --no-stdin $(DECK) -o $@ --html --allow-local-files

serve: diagrams
	marp --no-stdin $(DECK) --preview --html

clean:
	rm -rf $(OUTDIR)
	rm -f images/*.svg
