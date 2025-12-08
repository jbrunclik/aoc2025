#!/usr/bin/env python3
"""Day 7: Tachyon manifold."""
from collections import Counter
from dataclasses import dataclass
from enum import Enum

from aoc import load_lines


@dataclass(frozen=True)
class Beam:
    x: int
    y: int


class Point(Enum):
    START = "S"
    EMPTY = "."
    SPLITTER = "^"


Manifold = list[list[Point]]


def parse_manifold(input_lines: list[str]) -> Manifold:
    """Parse the manifold diagram."""
    manifold = []
    for line in input_lines:
        manifold.append([Point(point) for point in line])
    return manifold


def get_initial_beams(manifold: Manifold) -> set[Beam]:
    """Find the initial beam position."""
    return {
        Beam(x, y)
        for y in range(len(manifold))
        for x in range(len(manifold[y]))
        if manifold[y][x] == Point.START
    }


def part1(manifold: Manifold) -> int:
    """Count number of times the beam was split."""
    beams = get_initial_beams(manifold)
    num_splits = 0
    while beams:
        new_beams: set[Beam] = set()
        for beam in beams:
            if beam.y + 1 > len(manifold) - 1:
                continue
            elif manifold[beam.y + 1][beam.x] == Point.EMPTY:
                new_beams.add(Beam(beam.x, beam.y + 1))
            elif manifold[beam.y + 1][beam.x] == Point.SPLITTER:
                new_beams.add(Beam(beam.x - 1, beam.y + 1))
                new_beams.add(Beam(beam.x + 1, beam.y + 1))
                num_splits += 1

        beams = new_beams

    return num_splits


def part2(manifold: Manifold) -> int:
    """Count number of timelines created."""
    beams: Counter[Beam] = Counter(get_initial_beams(manifold))
    num_timelines = 0
    while beams:
        new_beams: Counter[Beam] = Counter()
        for beam, count in beams.items():
            if beam.y + 1 > len(manifold) - 1:
                num_timelines += count
            elif manifold[beam.y + 1][beam.x] == Point.EMPTY:
                new_beams[Beam(beam.x, beam.y + 1)] += count
            elif manifold[beam.y + 1][beam.x] == Point.SPLITTER:
                new_beams[Beam(beam.x - 1, beam.y + 1)] += count
                new_beams[Beam(beam.x + 1, beam.y + 1)] += count
        beams = new_beams

    return num_timelines


if __name__ == "__main__":
    input_lines = load_lines(7, example=False)
    manifold = parse_manifold(input_lines)
    print(part1(manifold))
    print(part2(manifold))
