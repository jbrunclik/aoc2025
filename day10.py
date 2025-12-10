#!/usr/bin/env python3
"""Day 10: Factory machines."""

from dataclasses import dataclass
from itertools import combinations

from aoc import load_lines


@dataclass
class Machine:
    lights: list[bool]
    buttons: list[list[int]]


def parse_machines(input_lines: list[str]) -> list[Machine]:
    """Parse input lines into machine manuals."""
    machines = []
    for line in input_lines:
        lights: list[bool] = []
        buttons: list[list[int]] = []

        parts = line.split()
        for part in parts:
            part_type = part[0]
            values = part[1:-1]

            if part_type == "[":
                lights = [s == "#" for s in values]
            elif part_type == "(":
                buttons.append(list(map(int, values.split(","))))

        machines.append(Machine(lights, buttons))
    return machines


def try_combination(lights: list[bool], buttons: list[list[int]]) -> bool:
    """Check if the given combination results in the target state."""
    state = [False] * len(lights)
    for button in buttons:
        for pos in button:
            state[pos] = not state[pos]
    return state == lights


def get_fewest_presses(machine: Machine) -> int:
    """Find the fewest presses to reach the target state."""
    for comb_length in range(1, len(machine.buttons) + 1):
        for comb in combinations(machine.buttons, comb_length):
            if try_combination(machine.lights, list(comb)):
                return comb_length
    return 0


def part1(machines: list[Machine]) -> int:
    """Sum of the fewest presses across all machines."""
    return sum(get_fewest_presses(machine) for machine in machines)


def part2() -> int:
    """TBD."""
    return 0


if __name__ == "__main__":
    input_lines = load_lines(10)
    machines = parse_machines(input_lines)
    print(part1(machines))
    print(part2())
