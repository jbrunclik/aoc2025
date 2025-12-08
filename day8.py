#!/usr/bin/env python3
"""Day 8: Junction boxes."""

import math
from dataclasses import dataclass
from math import sqrt

from aoc import load_lines


@dataclass(frozen=True)
class Box:
    x: int
    y: int
    z: int

    def __sub__(self, other: "Box") -> float:
        """Compute Euclidean distance between two boxes."""
        return sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )


@dataclass
class Circuit:
    boxes: list[Box]


def parse_boxes(input_lines: list[str]) -> list[Box]:
    """Parse input lines into box coordinates."""
    boxes = []
    for line in input_lines:
        x, y, z = map(int, line.split(","))
        boxes.append(Box(x, y, z))
    return boxes


def compute_all_distances(boxes: list[Box]) -> list[tuple[float, Box, Box]]:
    """Precompute all box distances."""
    pairs = []
    for i, box in enumerate(boxes):
        for other in boxes[i + 1 :]:
            pairs.append((box - other, box, other))
    pairs.sort()
    return pairs


def find_circuit(box: Box, circuits: list[Circuit]) -> Circuit | None:
    """Find which circuit a box belongs to."""
    for c in circuits:
        if box in c.boxes:
            return c
    return None


def part1(boxes: list[Box]) -> int:
    """Return product of the sizes of the 3 largest circuits after 1000 connections."""
    circuits: list[Circuit] = []
    pairs = compute_all_distances(boxes)

    for _ in range(1000):
        if not pairs:
            break
        _, box, other = pairs.pop(0)

        left = find_circuit(box, circuits)
        right = find_circuit(other, circuits)

        if left is None and right is None:
            circuits.append(Circuit([box, other]))
        elif left is None and right is not None:
            right.boxes.append(box)
        elif right is None and left is not None:
            left.boxes.append(other)
        elif left is not None and right is not None and left is not right:
            left.boxes.extend(right.boxes)
            circuits.remove(right)

    circuits.sort(key=lambda c: len(c.boxes), reverse=True)
    return math.prod([len(c.boxes) for c in circuits[:3]])


def part2(boxes: list[Box]) -> int:
    """Return product of X coordinates of the last two boxes connected to make a single circuit."""
    circuits: list[Circuit] = []
    pairs = compute_all_distances(boxes)

    while pairs:
        _, box, other = pairs.pop(0)

        left = find_circuit(box, circuits)
        right = find_circuit(other, circuits)

        if left is None and right is None:
            circuits.append(Circuit([box, other]))
        elif left is None and right is not None:
            right.boxes.append(box)
        elif right is None and left is not None:
            left.boxes.append(other)
        elif left is not None and right is not None and left is not right:
            left.boxes.extend(right.boxes)
            circuits.remove(right)

        if len(circuits) == 1 and len(circuits[0].boxes) == len(boxes):
            return box.x * other.x

    return 0


if __name__ == "__main__":
    input_lines = load_lines(8)
    boxes = parse_boxes(input_lines)
    print(part1(boxes))
    print(part2(boxes))
