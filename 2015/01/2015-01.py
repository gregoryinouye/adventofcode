#!/usr/bin/env python3

import sys
from typing import Optional
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 232
part_two_answer = 1783


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def part_one(parentheses: str) -> int:
    floor = 0

    for i, parenthesis in enumerate(parentheses):
        if parenthesis == '(':
            floor += 1
        elif parenthesis == ')':
            floor -= 1

    return floor


def part_two(parentheses: str) -> Optional[int]:
    floor = 0
    enters_basement = None

    for i, parenthesis in enumerate(parentheses):
        if parenthesis == '(':
            floor += 1
        elif parenthesis == ')':
            floor -= 1

        if floor < 0 and enters_basement is None:
            enters_basement = i + 1
            break

    return enters_basement


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
