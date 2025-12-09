#!/usr/bin/env python3
"""Day 1: Dial Wheel."""

from enum import Enum
from aoc import load_lines

TOTAL_POINTS = 100
START_POINT = 50


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"


def parse_instruction(instruction: str) -> tuple[Direction, int]:
    """Split an instruction into direction and steps."""
    return Direction(instruction[0]), int(instruction[1:])


def rotate(point: int, direction: Direction, steps: int) -> int:
    """Rotate the dial in the given direction."""
    match direction:
        case Direction.LEFT:
            return (point - steps) % TOTAL_POINTS
        case Direction.RIGHT:
            return (point + steps) % TOTAL_POINTS


def count_zeros_crossed(point: int, direction: Direction, steps: int) -> int:
    """Count crossing 0 during a rotation."""
    match direction:
        case Direction.LEFT:
            first_cross = point if point > 0 else TOTAL_POINTS
        case Direction.RIGHT:
            first_cross = TOTAL_POINTS - point if point > 0 else TOTAL_POINTS

    if steps < first_cross:
        return 0
    return (steps - first_cross) // TOTAL_POINTS + 1


def part1(instructions: list[str]) -> int:
    """Count how many times we ended at zero."""
    count = 0
    point = START_POINT
    for instruction in instructions:
        direction, steps = parse_instruction(instruction)
        point = rotate(point, direction, steps)
        if point == 0:
            count += 1
    return count


def part2(instructions: list[str]) -> int:
    """Count how many times we touched zero."""
    count = 0
    point = START_POINT
    for instruction in instructions:
        direction, steps = parse_instruction(instruction)
        count += count_zeros_crossed(point, direction, steps)
        point = rotate(point, direction, steps)
    return count


if __name__ == "__main__":
    instructions = load_lines(1)
    print(part1(instructions))
    print(part2(instructions))
