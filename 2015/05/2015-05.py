#!/usr/bin/env python3

import hashlib
from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem.split('_')[0] + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 258
part_two_answer = 53


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(strings: list[str]) -> int:
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    illegal = {'ab', 'cd', 'pq', 'xy'}

    for string in strings:
        vowel_count = 0
        has_double = False
        has_illegal = False

        for i, char in enumerate(string):
            if char in vowels:
                vowel_count += 1
            if i < len(string) - 1:
                next_char = string[i + 1]

                if char == next_char:
                    has_double = True

                if char + next_char in illegal:
                    has_illegal = True

        if vowel_count >= 3 and has_double and not has_illegal:
            count += 1

    return count


def part_two(strings: list[str]) -> int:
    count = 0

    for string in strings:
        has_duplicate_pair = False
        has_separated_pair = False
        pairs = {}

        for i, char in enumerate(string):
            if i < len(string) - 2 and char == string[i + 2]:
                has_separated_pair = True
            if i < len(string) - 1:
                if i - pairs.get(char + string[i + 1], i) > 1:
                    has_duplicate_pair = True
                pairs.setdefault(char + string[i + 1], i)

        if has_duplicate_pair and has_separated_pair:
            count += 1

    return count


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
