#!/usr/bin/env python3
"""Day 11: Toroidal reactor."""

from enum import StrEnum

from aoc import load_lines

Machines = dict[str, list[str]]
PathCache = dict[tuple[str, str], int]


class Machine(StrEnum):
    YOU = "you"
    OUT = "out"
    SVR = "svr"
    DAC = "dac"
    FFT = "fft"


def parse_machines(lines: list[str]) -> Machines:
    """Parse input lines into a machine graph."""
    machines: Machines = {}
    for line in lines:
        labels = line.split()
        machine = labels[0][:-1]
        machines[machine] = labels[1:]
    return machines


def count_paths(
    start: str, target: str, machines: Machines, path_cache: PathCache
) -> int:
    """Count all paths from start to target."""
    if start == target:
        return 1
    if start == Machine.OUT:
        return 0

    key = (start, target)
    if key in path_cache:
        return path_cache[key]

    total = 0
    for next_machine in machines[start]:
        total += count_paths(next_machine, target, machines, path_cache)

    path_cache[key] = total
    return total


def part1(machines: Machines) -> int:
    """Count all paths from 'you' to 'out'."""
    path_cache: PathCache = {}
    return count_paths(Machine.YOU, Machine.OUT, machines, path_cache)


def part2(machines: Machines) -> int:
    """Count all paths from 'svr' to 'out' visiting both 'dac' and 'fft'."""
    path_cache: PathCache = {}

    p1 = (
        count_paths(Machine.SVR, Machine.DAC, machines, path_cache)
        * count_paths(Machine.DAC, Machine.FFT, machines, path_cache)
        * count_paths(Machine.FFT, Machine.OUT, machines, path_cache)
    )

    p2 = (
        count_paths(Machine.SVR, Machine.FFT, machines, path_cache)
        * count_paths(Machine.FFT, Machine.DAC, machines, path_cache)
        * count_paths(Machine.DAC, Machine.OUT, machines, path_cache)
    )

    return p1 + p2


if __name__ == "__main__":
    input_lines = load_lines(11)
    machines = parse_machines(input_lines)
    print(part1(machines))
    print(part2(machines))
