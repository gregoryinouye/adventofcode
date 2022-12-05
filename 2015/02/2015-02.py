#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 1588178
part_two_answer = 3783758


def parse(input_path: Path) -> list[tuple[int]]:
    packages = input_path.read_text().strip().split('\n')
    return [tuple(map(int, package.split('x'))) for package in packages]


def part_one(packages: list[tuple[int]]) -> int:
    paper = 0

    for length, width, height in packages:
        side_a = 2 * height * length
        side_b = 2 * height * width
        side_c = 2 * length * width
        minimum = min(side_a, side_b, side_c) // 2

        paper += side_a + side_b + side_c + minimum

    return paper


def part_two(packages: list[tuple[int]]) -> int:
    ribbon = 0

    for length, width, height in packages:
        sorted_lengths = sorted([length, width, height])
        ribbon += 2 * (sorted_lengths[0] + sorted_lengths[1]) + length * height * width

    return ribbon


if __name__ == '__main__':
    paths = [test_filename] if len(sys.argv) <= 1 else sys.argv[1:]

    for path_str in paths:
        print(f'\n{path_str}:')
        puzzle_input = parse(Path(path_str))

        part_one_actual = part_one(puzzle_input)
        part_two_actual = part_two(puzzle_input)

        result_one = '\u2705 ' if part_one_actual == part_one_answer else '\u274c '
        result_two = '\u2705 ' if part_two_actual == part_two_answer else '\u274c '

        print(result_one, 'Part One:', part_one_actual)
        print(result_two, 'Part Two:', part_two_actual)
