#!/usr/bin/env python3
"""Day 10: Factory machines."""

from dataclasses import dataclass
from itertools import combinations

from pulp import LpInteger, LpMinimize, LpProblem, LpVariable, lpSum

from aoc import load_lines


@dataclass
class Machine:
    lights: list[bool]
    buttons: list[list[int]]
    joltages: list[int]


def parse_machines(input_lines: list[str]) -> list[Machine]:
    """Parse input lines into machine manuals."""
    machines = []
    for line in input_lines:
        lights: list[bool] = []
        buttons: list[list[int]] = []
        joltages: list[int] = []

        parts = line.split()
        for part in parts:
            part_type = part[0]
            values = part[1:-1]

            if part_type == "[":
                lights = [s == "#" for s in values]
            elif part_type == "(":
                buttons.append(list(map(int, values.split(","))))
            elif part_type == "{":
                joltages = list(map(int, values.split(",")))

        machines.append(Machine(lights, buttons, joltages))
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
    """Sum of the fewest presses to reach the target state."""
    return sum(get_fewest_presses(machine) for machine in machines)


def solve_joltage(machine: Machine) -> int:
    """Find minimum button presses using ILP solver."""
    prob = LpProblem("MinPresses", LpMinimize)

    # Variable for each button: how many times to press it
    x = [
        LpVariable(f"x{i}", lowBound=0, cat=LpInteger)
        for i in range(len(machine.buttons))
    ]

    # Objective: minimize total presses
    prob += lpSum(x)

    # Constraints: each counter must reach its target
    for counter_idx, target in enumerate(machine.joltages):
        # Sum of presses of buttons affecting this counter = target
        prob += (
            lpSum(x[i] for i, btn in enumerate(machine.buttons) if counter_idx in btn)
            == target
        )

    prob.solve()
    return int(sum(v.varValue or 0 for v in x))


def part2(machines: list[Machine]) -> int:
    """Sum of the fewest presses to reach the target joltages.

    Note: I didn't figure this one out myself. BFS was too slow, so I had to
    resort to Claude Code to help me recognize this as an ILP problem.
    """
    return sum(solve_joltage(machine) for machine in machines)


if __name__ == "__main__":
    input_lines = load_lines(10, example=False)
    machines = parse_machines(input_lines)
    print(part1(machines))
    print(part2(machines))
