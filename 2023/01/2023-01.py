#!/usr/bin/env python3

import math
import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 54877
part_two_answer = 54100


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def get_numbers(line: str) -> int:
    first = None
    last = None
    for char in line:
        if char.isnumeric():
            if first is None:
                first = char
            last = char
    return int(first + last)


numbers = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
]


def replace_numeric_words(line: str) -> str:
    replaced = line
    for word, number in numbers:
        left = line.find(word)
        right = line.rfind(word)
        if left >= 0:
            replaced = replaced[:left] + number + replaced[left + 1:]
        if right != left:
            replaced = replaced[:right] + number + replaced[right + 1:]
    return replaced


def part_one(lines: list[str]) -> int:
    return sum([get_numbers(line) for line in lines])


def part_two(lines: list[str]) -> int:
    return sum([get_numbers(replace_numeric_words(line)) for line in lines])


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
