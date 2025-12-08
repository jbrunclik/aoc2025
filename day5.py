#!/usr/bin/env python3
"""Day 5: Fresh ingredients."""
from dataclasses import dataclass
from aoc import load_lines


@dataclass
class IDRange:
    """Fresh ingredients range."""

    start: int
    end: int


def parse_instructions(instructions: list[str]) -> tuple[list[IDRange], list[int]]:
    """Parse instructions into fresh ID ranges and inventory."""
    ranges = []
    inventory = []

    for line in instructions:
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append(IDRange(start, end))
        elif line.isdigit():
            inventory.append(int(line))

    return ranges, inventory


def part1(fresh: list[IDRange], inventory: list[int]) -> int:
    """Count fresh ingredients in the inventory."""
    num_fresh = 0
    for item in inventory:
        for id_range in fresh:
            if id_range.start <= item <= id_range.end:
                num_fresh += 1
                break

    return num_fresh


def part2(fresh: list[IDRange]) -> int:
    """Count total fresh IDs."""
    deduplicated = []
    for id_range in sorted(fresh, key=lambda r: r.start):
        if not deduplicated:
            deduplicated.append(id_range)
        else:
            last = deduplicated[-1]
            if id_range.start <= last.end + 1:
                last.end = max(last.end, id_range.end)
            else:
                deduplicated.append(id_range)

    num_fresh = 0
    for id_range in deduplicated:
        num_fresh += id_range.end - id_range.start + 1

    return num_fresh


if __name__ == "__main__":
    instructions = load_lines(5)
    fresh, inventory = parse_instructions(instructions)
    print(part1(fresh, inventory))
    print(part2(fresh))
