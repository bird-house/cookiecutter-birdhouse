COOKIES_DIR = $(CURDIR)/cookies
BAKE_OPTIONS ?= --no-input
NO_CRUFT = generated_with_cruft=n

.DEFAULT_GOAL := all

.PHONY: all
all: help

.PHONY: help
help:
	@echo "bake 	to generate project using defaults"
	@echo "test 	to test cookiecutter template generation"
	@echo "clean 	to remove baked cookies"
	@echo "docs   to generate Sphinx docs"

.PHONY: test
test:
	@echo "Running all tests"
	@bash -c 'pytest'

.PHONY: test-no-gdal
test-no-gdal:
	@echo "Running all tests"
	@bash -c 'pytest -m "not requires_gdal"'

.PHONY: clean
clean:
	test -d $(COOKIES_DIR) && rm -v -rf $(COOKIES_DIR);

.PHONY: bake
bake:
	@echo "Creating a new project with default settings"
	@mkdir -p "cookies"
	@bash -c 'cookiecutter $(BAKE_OPTIONS) . --output-dir $(COOKIES_DIR) --overwrite-if-exists $(NO_CRUFT)'

.PHONY: docs
docs:
	@echo "Generating docs with Sphinx ..."
	@-bash -c '$(MAKE) -C $@ clean html'
	@echo "Opening browser to: file:/$(CURDIR)/docs/build/html/index.html"
	@-bash -c 'xdg-open $(CURDIR)/docs/build/html/index.html'

# generate project using defaults and watch for changes
watch: bake
	watchmedo shell-command -p '*.*' -c 'make bake -e BAKE_OPTIONS=$(BAKE_OPTIONS)' -W -R -D \{{cookiecutter.project_slug}}/
#
# replay last cookiecutter run and watch for changes
# replay: BAKE_OPTIONS=--replay
# replay: watch
# 	;
