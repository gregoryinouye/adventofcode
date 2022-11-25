#!/usr/bin/env python3

import hashlib
from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 282749
part_two_answer = 9962624


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def part_one(prefix: str) -> int:
    for i in range(2000000):
        hash_value = hashlib.md5(f'{prefix}{i}'.encode('utf-8')).hexdigest()
        if hash_value[0:5] == '00000':
            return i


def part_two(prefix: str) -> int:
    for i in range(10000000):
        hash_value = hashlib.md5(f'{prefix}{i}'.encode('utf-8')).hexdigest()
        if hash_value[0:6] == '000000':
            return i


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
