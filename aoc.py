"""Advent of Code 2025 - Common utilities."""

from pathlib import Path


def load_input(day: int, example: bool = False) -> str:
    """Load input data for a given day.

    Args:
        day: The day number (1-12)
        example: If True, load the example input instead of the real input

    Returns:
        The input data as a string (without trailing newline)
    """
    suffix = "_example" if example else ""
    filename = f"day{day}{suffix}.txt"
    return Path(filename).read_text().strip()


def load_lines(day: int, example: bool = False) -> list[str]:
    """Load input data as a list of lines."""
    return load_input(day, example).splitlines()
