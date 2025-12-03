#!/usr/bin/env python3
"""Day 3: Battery Joltage"""
from aoc import load_lines


def part1(instructions: list[str]) -> int:
    """Find the maximum two-digit joltages."""
    total_joltage = 0
    for battery in instructions:
        pairs = set()
        for i in range(len(battery) - 1):
            for j in range(i + 1, len(battery)):
                pairs.add((battery[i], battery[j]))

        max_joltage = 0
        for pair in pairs:
            max_joltage = max(max_joltage, int("".join(pair)))

        total_joltage += max_joltage

    return total_joltage


def part2(instructions: list[str]) -> int:
    """Find the maximum 12-digit joltages."""
    total_joltage = 0
    for battery in instructions:
        num_remove = len(battery) - 12

        largest_number = []
        for digit in battery:
            while num_remove > 0 and largest_number and largest_number[-1] < digit:
                largest_number.pop()
                num_remove -= 1
            largest_number.append(digit)

        largest_number = largest_number[: len(largest_number) - num_remove]
        total_joltage += int("".join(largest_number))

    return total_joltage


if __name__ == "__main__":
    instructions = load_lines(3)
    print(part1(instructions))
    print(part2(instructions))
