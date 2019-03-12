VERSION := {{ cookiecutter.version }}
RELEASE := master

# Include custom config if it is available
-include Makefile.config

# Application
APP_ROOT := $(CURDIR)
APP_NAME := {{ cookiecutter.project_slug }}

# guess OS (Linux, Darwin, ...)
OS_NAME := $(shell uname -s 2>/dev/null || echo "unknown")
CPU_ARCH := $(shell uname -m 2>/dev/null || uname -p 2>/dev/null || echo "unknown")

# Anaconda
CONDA := $(shell command -v conda 2> /dev/null)
ANACONDA_HOME := $(shell conda info --base 2> /dev/null)
CONDA_ENV := $(APP_NAME)

# Configuration used by update-config
HOSTNAME ?= localhost
HTTP_PORT ?= 8094
OUTPUT_PORT ?= 8090

# choose anaconda installer depending on your OS
ANACONDA_URL = https://repo.continuum.io/miniconda
ifeq "$(OS_NAME)" "Linux"
FN := Miniconda3-latest-Linux-x86_64.sh
else ifeq "$(OS_NAME)" "Darwin"
FN := Miniconda3-latest-MacOSX-x86_64.sh
else
FN := unknown
endif

TEMP_FILES := *.egg-info *.log *.sqlite

# Docker
DOCKER_IMAGE := birdhouse/$(APP_NAME)
DOCKER_CONTAINER := $(APP_NAME)

# end of configuration

.DEFAULT_GOAL := all

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

.PHONY: all
all: help

.PHONY: help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 {{ cookiecutter.project_slug }} tests

test: ## run tests quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	pytest
{%- else %}
	python setup.py test
{%- endif %}

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	coverage run --source {{ cookiecutter.project_slug }} -m pytest
{%- else %}
	coverage run --source {{ cookiecutter.project_slug }} setup.py test
{%- endif %}
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/{{ cookiecutter.project_slug }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.project_slug }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

.PHONY: version
version:
	@echo "Version: $(VERSION)"

.PHONY: info
info:
	@echo "Informations about your Bird:"
	@echo "  OS_NAME             $(OS_NAME)"
	@echo "  CPU_ARCH            $(CPU_ARCH)"
	@echo "  Anaconda Home       $(ANACONDA_HOME)"
	@echo "  Conda Environment   $(CONDA_ENV). Use \`source activate $(CONDA_ENV)' to activate it."
	@echo "  Conda Prefix        $(CONDA_ENV_PATH)"
	@echo "  APP_NAME            $(APP_NAME)"
	@echo "  APP_ROOT            $(APP_ROOT)"
	@echo "  DOWNLOAD_CACHE      $(DOWNLOAD_CACHE)"
	@echo "  DOCKER_IMAGE        $(DOCKER_IMAGE)"

## EMU ##

## Helper targets ... ensure that Makefile etc are in place

.PHONY: backup
backup:
	@echo "Backup custom config ..."
	@-test -f custom.cfg && cp -v --update --backup=numbered --suffix=.bak custom.cfg custom.cfg.bak

.PHONY: .gitignore
.gitignore:
	@echo "Setup default .gitignore ..."
	@curl "https://raw.githubusercontent.com/bird-house/birdhousebuilder.bootstrap/$(RELEASE)/dot_gitignore" --silent --insecure --output .gitignore

.PHONY: bootstrap.sh
bootstrap.sh:
	@echo "Update bootstrap.sh ..."
	@curl "https://raw.githubusercontent.com/bird-house/birdhousebuilder.bootstrap/$(RELEASE)/bootstrap.sh" --silent --insecure --output bootstrap.sh "https://raw.githubusercontent.com/bird-house/birdhousebuilder.bootstrap/$(RELEASE)/bootstrap.sh"
	@chmod 755 bootstrap.sh

custom.cfg:
	@echo "Using custom.cfg for buildout ..."
	@test -f custom.cfg || cp -v custom.cfg.example custom.cfg

.PHONY: downloads
downloads:
	@echo "Using DOWNLOAD_CACHE $(DOWNLOAD_CACHE)"
	@test -d $(DOWNLOAD_CACHE) || mkdir -v -p $(DOWNLOAD_CACHE)

.PHONY: init
init: custom.cfg downloads

bootstrap-buildout.py:
	@echo "Update buildout bootstrap-buildout.py ..."
	@test -f boostrap-buildout.py || curl https://bootstrap.pypa.io/bootstrap-buildout.py --insecure --silent --output bootstrap-buildout.py

## Conda targets

.PHONY: check_conda
check_conda:
ifndef CONDA
		$(error "Conda is not available. Please install miniconda: https://conda.io/miniconda.html")
endif

.PHONY: conda_env
conda_env: check_conda
	@echo "Updating conda environment $(CONDA_ENV) ..."
	"$(CONDA)" env update -n $(CONDA_ENV) -f environment.yml

.PHONY: envclean
envclean: check_conda
	@echo "Removing conda env $(CONDA_ENV)"
	@-"$(CONDA)" remove -n $(CONDA_ENV) --yes --all

.PHONY: spec
spec: check_conda
	@echo "Updating conda environment specification file ..."
	@-"$(CONDA)" list -n $(CONDA_ENV) --explicit > spec-file.txt

## Build targets

.PHONY: bootstrap
bootstrap: check_conda conda_env bootstrap_dev
	@echo "Bootstrap ..."

.PHONY: bootstrap_dev
bootstrap_dev:
	@echo "Installing development requirements for tests and docs ..."
	@-bash -c "$(CONDA) install -y -n $(CONDA_ENV) -c conda-forge pytest flake8 sphinx bumpversion gunicorn psycopg2"
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && pip install -r requirements_dev.txt"

.PHONY: install
install: bootstrap
	@echo "Installing application ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && python setup.py develop"
	@echo "\nStart service with \`make start'"

.PHONY: start
start: check_conda
	@echo "Starting application ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && $(APP_NAME) start -d"

.PHONY: stop
stop: check_conda
	@echo "Stopping application ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && $(APP_NAME) stop"

.PHONY: status
status: check_conda
	@echo "Show status ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && $(APP_NAME) status"

.PHONY: clean
clean: srcclean envclean
	@echo "Cleaning generated files ..."
	@-for i in $(TEMP_FILES); do \
  	test -e $$i && rm -v -rf $$i; \
  done

.PHONY: srcclean
srcclean:
	@echo "Removing *.pyc files ..."
	@-find $(APP_ROOT) -type f -name "*.pyc" -print | xargs rm

.PHONY: distclean
distclean: clean
	@echo "Cleaning ..."
	@git diff --quiet HEAD || echo "There are uncommited changes! Not doing 'git clean' ..."
	@-git clean -dfx -e *.bak -e custom.cfg

.PHONY: passwd
passwd: custom.cfg
	@echo "Generate Phoenix password ..."
	@echo "Enter a password with at least 8 characters."
	@bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV); python -c 'from IPython.lib import passwd; pw = passwd(algorithm=\"sha256\"); lines = [\"phoenix-password = \" + pw + \"\\n\" if line.startswith(\"phoenix-password\") else line for line in open(\"custom.cfg\", \"r\")]; file = open(\"custom.cfg\", \"w\"); file.writelines(lines); file.close()'"
	@echo ""
	@echo "Run \`make install restart' to activate this password."

## Test targets

.PHONY: test
test: check_conda
	@echo "Running tests (skip slow and online tests) ..."
	@bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV);pytest -v -m 'not slow and not online'"

.PHONY: testall
testall: check_conda
	@echo "Running all tests (including slow and online tests) ..."
	@bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && pytest -v"

.PHONY: pep8
pep8: check_conda
	@echo "Running pep8 code style checks ..."
	@bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV) && flake8"

##  Sphinx targets

.PHONY: docs
docs: check_conda
	@echo "Generating docs with Sphinx ..."
	@-bash -c "source $(ANACONDA_HOME)/bin/activate $(CONDA_ENV);$(MAKE) -C $@ clean html"
	@echo "open your browser: firefox docs/build/html/index.html"

.PHONY: linkcheck
linkcheck:
	@echo "Run link checker on docs..."
	$(MAKE) -C docs linkcheck

.PHONY: doc8
doc8:
	@echo "Running doc8 doc style checks ..."
	$(CONDA_ENV_PATH)/bin/doc8 docs/

.PHONY: selfupdate
selfupdate: bootstrap.sh .gitignore
	@curl "https://raw.githubusercontent.com/bird-house/birdhousebuilder.bootstrap/$(RELEASE)/Makefile" --silent --insecure --output Makefile

## Supervisor targets

.PHONY: start
start:
	@echo "Starting supervisor service ..."
	bin/supervisord start

.PHONY: stop
stop:
	@echo "Stopping supervisor service ..."
	-bin/supervisord stop

.PHONY: restart
restart:
	@echo "Restarting supervisor service ..."
	bin/supervisord restart

.PHONY: status
status:
	@echo "Supervisor status ..."
	bin/supervisorctl status


## Docker targets

.PHONY: Dockerfile
Dockerfile: bootstrap
	@echo "Update Dockerfile ..."
	bin/buildout -c custom.cfg install docker

.PHONY: dockerrmi
dockerrmi:
	@echo "Removing previous docker image ..."
	docker rmi $(DOCKER_IMAGE)

.PHONY: dockerbuild
dockerbuild: Dockerfile
	@echo "Building docker image ..."
	docker build --rm -t $(DOCKER_IMAGE) .

.PHONY: dockerrun
dockerrun: dockerbuild
	@echo "Run docker image ..."
	docker run -i -t -p 9001:9001 --name=$(DOCKER_CONTAINER) $(DOCKER_IMAGE) /bin/bash
