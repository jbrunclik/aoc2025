#!/usr/bin/env python3
"""Day 2: Invalid IDs."""
from aoc import load_lines


def parse_instructions(instructions: list[str]) -> list[tuple[int, int]]:
    """Parse ID ranges into (start, end) tuples."""
    ranges = instructions[0].split(",")
    return [(int(i), int(j)) for i, j in (r.split("-") for r in ranges)]


def is_repeating_twice(n: int) -> bool:
    """Check if the ID is a sequence repeating twice."""
    s = str(n)
    length = len(s)

    if length % 2 != 0:
        return False

    half = length // 2
    return s[:half] == s[half:]


def is_repeating(n: int) -> bool:
    """Check if the ID is a repeating sequence."""
    s = str(n)
    length = len(s)

    for seq_len in range(1, length // 2 + 1):
        if length % seq_len != 0:
            continue

        pattern = s[:seq_len]
        if pattern * (length // seq_len) == s:
            return True

    return False


def part1(ranges: list[tuple[int, int]]) -> int:
    """Find IDs with a sequence repeating twice."""
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_repeating_twice(n):
                total += n
    return total


def part2(ranges: list[tuple[int, int]]) -> int:
    """Find IDs with a repeating sequence."""
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_repeating(n):
                total += n
    return total


if __name__ == "__main__":
    instructions = load_lines(2)
    ranges = parse_instructions(instructions)
    print(part1(ranges))
    print(part2(ranges))
