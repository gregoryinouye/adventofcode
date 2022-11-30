#!/usr/bin/env python3

import re
import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 8997277
part_two_answer = 0


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def next_value(num: int) -> int:
    return (num * 252533) % 33554393


def part_one(line: str) -> int:
    row, col = map(int, re.compile(r'\d+').findall(line))
    n = row + col - 2
    completed_diagonals_count = (n ** 2 + n) // 2
    count = completed_diagonals_count + col - 1
    current = 20151125

    for i in range(count):
        current = next_value(current)

    return current


def part_two(line: str) -> int:
    pass


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
