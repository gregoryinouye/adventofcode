#!/usr/bin/env python3

from math import floor
from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 3262358
part_two_answer = 4890696


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def calculate_fuel(weight: int) -> int:
    return max(floor(weight / 3) - 2, 0)


def part_one(lines: list[str]) -> int:
    return sum(calculate_fuel(int(weight)) for weight in lines)


def part_two(lines: list[str]) -> int:
    total_fuel = 0
    weights = list(map(int, lines))

    while weights:
        current = weights.pop()
        fuel = calculate_fuel(current)
        total_fuel += fuel
        if fuel > 0:
            weights.append(fuel)

    return total_fuel


if __name__ == '__main__':
    paths = [test_filename] if len(sys.argv) <= 1 else sys.argv[1:]

    for path_str in paths:
        print(f"\n{path_str}:")
        puzzle_input = parse(Path(path_str))

        part_one_actual = part_one(puzzle_input)
        part_two_actual = part_two(puzzle_input)

        result_one = '\u2705 ' if part_one_actual == part_one_answer else '\u274c '
        result_two = '\u2705 ' if part_two_actual == part_two_answer else '\u274c '

        print(result_one, 'Part One:', part_one_actual)
        print(result_two, 'Part Two:', part_two_actual)
