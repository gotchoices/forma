# Figures for projects/metric-mass.
#
# Each .py script produces one or more PNG/SVG outputs of the same
# stem name. New figures: drop the script in this directory and add
# its expected output(s) to the OUTPUTS list below.
#
# Usage:
#   make            # regenerate any out-of-date figures
#   make all        # same
#   make clean      # remove all generated figures
#   make wave-modes.png   # build a single figure

PYTHON := ../../../.venv/bin/python

OUTPUTS := \
	wave-modes.png

.PHONY: all clean

all: $(OUTPUTS)

# Each PNG comes from the .py script of matching stem.
%.png: %.py
	$(PYTHON) $<

clean:
	rm -f $(OUTPUTS)
