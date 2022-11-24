#!/usr/bin/env python3

import sys
from typing import Optional
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem.split('_')[0] + '.txt'
test_filepath = filepath.parent / test_filename


def parse(input_path: Path):
    return input_path.read_text().strip()


def part_one(parentheses: str) -> (int, Optional[int]):
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
        print(f"\n{path_str}:")
        puzzle_input = parse(Path(path_str))

        print('Part One:', part_one(puzzle_input))
        print('Part Two:', part_two(puzzle_input))
