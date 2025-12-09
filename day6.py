#!/usr/bin/env python3
"""Day 6: Cephalopod math."""

from dataclasses import dataclass
from enum import Enum
from math import prod

from aoc import load_lines


class Operation(Enum):
    """Operation type."""

    ADD = "+"
    MULTIPLY = "*"


@dataclass
class Problem:
    """Math problem."""

    operation: Operation
    values: list[int]

    def __int__(self) -> int:
        if self.operation == Operation.ADD:
            return sum(self.values)
        elif self.operation == Operation.MULTIPLY:
            return prod(self.values)
        else:
            raise NotImplementedError(self.operation)


def part1(lines: list[str]) -> int:
    """Return sum of problems using traditional math."""
    rows = [line.split() for line in lines]

    problems = [
        Problem(
            Operation(rows[-1][i]),
            [int(rows[j][i]) for j in range(len(rows) - 1)],
        )
        for i in range(len(rows[0]))
    ]

    return sum(int(p) for p in problems)


def part2(lines: list[str]) -> int:
    """Return sum of problems using Cephalopod math."""
    empty_columns = [
        i for i in range(len(lines[0])) if all(line[i] == " " for line in lines)
    ]
    empty_columns.append(len(lines[0]))

    problems = []
    first = 0
    for i in empty_columns:
        numbers = [
            int(
                "".join(
                    lines[k][j] for k in range(len(lines) - 1) if lines[k][j].isdigit()
                )
            )
            for j in range(i - 1, first - 1, -1)
        ]
        problems.append(Problem(Operation(lines[-1][first]), numbers))
        first = i + 1

    return sum(int(p) for p in problems)


if __name__ == "__main__":
    input_lines = load_lines(6)
    print(part1(input_lines))
    print(part2(input_lines))
