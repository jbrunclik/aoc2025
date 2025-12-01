.PHONY: lint format check

lint: format check

format:
	venv/bin/black *.py

check:
	venv/bin/black --check *.py
