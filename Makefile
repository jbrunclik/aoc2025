.PHONY: lint format typecheck setup

lint: format typecheck

format:
	venv/bin/ruff format *.py
	venv/bin/ruff check --fix *.py

typecheck:
	venv/bin/mypy *.py --ignore-missing-imports

setup:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install mypy ruff
