#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 72017
part_two_answer = 212520


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n\n')


def part_one(lines: list[str]) -> int:
    elves = [line.split('\n') for line in lines]
    elves_calories = [sum(map(int, items)) for items in elves]

    return sorted(elves_calories)[-1]


def part_two(lines: list[str]) -> int:
    elves = [line.split('\n') for line in lines]
    elves_calories = [sum(map(int, items)) for items in elves]

    return sum(sorted(elves_calories)[-3:])


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
