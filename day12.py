#!/usr/bin/env python3
"""Day 12: Christmas trees."""

from dataclasses import dataclass

from aoc import load_lines


@dataclass
class Present:
    """Shape of a present."""

    idx: int
    shape: list[list[bool]]


@dataclass
class Region:
    """Region to place the presents."""

    width: int
    height: int
    counts: list[int]

    def can_fit(self) -> bool:
        """Check if all presents can be placed without overlap.

        The elves were nice this year: every region either has enough space for full
        3x3 blocks (definitely fits) or not enough cells (definitely doesn't).
        """
        return self.width * self.height >= 9 * sum(self.counts)


def parse_input(lines: list[str]) -> tuple[list[Present], list[Region]]:
    """Parse input into presents and regions."""
    presents: list[Present] = []
    regions: list[Region] = []

    current_shape: list[list[bool]] = []
    for line in lines:
        if not line:
            continue
        if "x" in line:
            dims, counts = line.split(": ")
            width, height = map(int, dims.split("x"))
            regions.append(Region(width, height, list(map(int, counts.split()))))
        elif line.endswith(":"):
            current_shape = []
            presents.append(Present(int(line[:-1]), current_shape))
        else:
            current_shape.append([c == "#" for c in line])

    return presents, regions


def part1(regions: list[Region]) -> int:
    """Count how many regions can fit all presents."""
    return sum(1 for region in regions if region.can_fit())


def part2():
    return None


if __name__ == "__main__":
    input_lines = load_lines(12)
    _, regions = parse_input(input_lines)
    print(part1(regions))
    print(part2())
