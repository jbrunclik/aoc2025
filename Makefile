.PHONY: lint format typecheck setup scaffold

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

scaffold:
ifndef DAY
	$(error DAY is required.)
endif
	@sed 's/__DAY_NUMBER__/$(DAY)/g' templates/day.py.template > day$(DAY).py
	@touch data/day$(DAY).txt
	@touch examples/day$(DAY).txt
