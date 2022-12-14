#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 1198
part_two_answer = 3120


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def find_index_of_consecutive_unique_chars(chars: str, n: int) -> int:
    for i in range(len(chars)):
        if len(set(chars[i:i + n])) == n:
            return i + n
    return -1


def part_one(lines: str) -> int:
    return find_index_of_consecutive_unique_chars(lines, 4)


def part_two(lines: str) -> int:
    return find_index_of_consecutive_unique_chars(lines, 14)


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
