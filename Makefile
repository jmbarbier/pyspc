# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
NBSOURCES := $(shell find $(SOURCEDIR) -name "*.ipynb" ! -name "*-download.ipynb" | grep -v checkpoints) 
NBPDFS := $(patsubst %.ipynb, %.pdf, $(NBSOURCES))

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help pdfs Makefile

	
www: Makefile
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	rsync -av --delete _build/html/ /home/eleve/www/

pdfs: $(NBPDFS)

$(NBPDFS): $(NBSOURCES)
%.pdf: %.ipynb
	(cd $(dir $<); jupyter nbconvert --to pdf $(notdir $<) --template classicm)
html: Makefile
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
epub: Makefile
	@$(SPHINXBUILD) -M epub "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
latexpdf: Makefile
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

