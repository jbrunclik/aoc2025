#!/usr/bin/env python3
"""Day 4: Rolls of paper"""

from aoc import load_lines

ACCESSIBLE_THRESHOLD = 4
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
EMPTY = "."
ROLL = "@"


def parse_grid(lines: list[str]) -> list[list[str]]:
    """Convert input into a grid."""
    return [list(line) for line in lines]


def count_adjacent_rolls(grid: list[list[str]], x: int, y: int) -> int:
    """Count how many rolls are adjacent to the cell."""
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == ROLL:
            count += 1
    return count


def part1(grid: list[list[str]]) -> int:
    """Count accessible rolls."""
    accessible = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (
                grid[y][x] == ROLL
                and count_adjacent_rolls(grid, x, y) < ACCESSIBLE_THRESHOLD
            ):
                accessible += 1
    return accessible


def part2(grid: list[list[str]]) -> int:
    """Repeatedly remove accessible rolls."""
    total_removed = 0
    while True:
        to_remove = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if (
                    grid[y][x] == ROLL
                    and count_adjacent_rolls(grid, x, y) < ACCESSIBLE_THRESHOLD
                ):
                    to_remove.append((x, y))
        if not to_remove:
            break
        for x, y in to_remove:
            grid[y][x] = EMPTY
        total_removed += len(to_remove)
    return total_removed


if __name__ == "__main__":
    lines = load_lines(4)
    grid = parse_grid(lines)
    print(part1(grid))
    print(part2(grid))
