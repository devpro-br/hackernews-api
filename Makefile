.ONESHELL:

ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")


.PHONY: help
help:                      ## Show this help
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


.PHONY: show
show:                      ## Show the current environment
	@echo "Current environment:"
	if [ -z "${ENV_PREFIX}" ]
	then
		if [ -d .venv ]; then
			echo "Virtualenv not activated"
			echo "Run:"
			echo "  source .venv/bin/activate"
		else
			echo "Virtualenv not created"
			echo "Run:"
			echo "  make virtualenv"
		fi
		exit 1
	fi
	@echo "Current environment:"
	@echo ">>> Running using '$(ENV_PREFIX)'"
	@$(ENV_PREFIX)python -V
	@$(ENV_PREFIX)python -m site


.PHONY: virtualenv
virtualenv:                ## Create a virtual environment
	@echo "creating virtualenv ..."
	@rm -rf .venv
	@virtualenv .venv
	@./.venv/bin/pip install -U pip
	@echo
	@echo "!!! Please run 'source .venv/bin/activate' to enable the environment !!!"


.PHONY: system-packages
system-packages:           ## Install SO dependencies
	@sudo apt install -y libpq-dev build-essential libssl-dev libffi-dev


.PHONY: python-packages
python-packages:           ## Install project dependencies (dev mode)
	@echo "Installing dependencies..."
	if [ -z "${ENV_PREFIX}" ]
	then
		echo "Virtualenv not activated"
		echo "Run:"
		echo "  make show"
		exit 1
	fi
	@$(ENV_PREFIX)pip install -r requirements-dev.txt
	@echo "Project dependencies installed!!!"


.PHONY: install
install: system-packages python-packages    ## Install all dependencies


.PHONY: clean
clean:                     ## Clean unused files
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache


.PHONY: code-fmt
code-fmt:                  ## Format code using black & isort
	$(ENV_PREFIX)isort hackernews/
	$(ENV_PREFIX)black -l 88 hackernews/


.PHONY: linter
linter:                    ## Run pep8, black
	$(ENV_PREFIX)pylint hackernews/**/*.py
	$(ENV_PREFIX)black -l 88 --check hackernews/


.PHONY: db-test-up
db-test-up:                ## Run Postgres for testing (using docker)
	@docker-compose -f docker-compose.test.yml up -d


.PHONY: db-test-down
db-test-down:              ## Stop Postgres (test instance)
	@docker-compose -f docker-compose.test.yml down


.PHONY: tests
tests: linter db-test-up   ## Run tests using pytest and docker DB
	@sleep 1
	$(ENV_PREFIX)pytest


.PHONY: db-up
db-up:                     ## Run Postgres for testing (using docker)
	@docker-compose up -d postgres_dev


.PHONY: db-down
dk-down:                   ## Stop Postgres (test instance)
	@docker-compose down


.PHONY: dk-clean
dk-clean:                  ## Docker Clean up (unused containers/volumes)
	@docker stop $(docker ps -a -q)
	@docker rm $(docker ps -a -q)
	@docker system prune --volumes
