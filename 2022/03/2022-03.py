#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 7821
part_two_answer = 2752


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def get_priority(letter: str) -> int:
    ord_num = ord(letter)
    return ord_num - 96 if ord_num >= 97 else ord_num - 38


def part_one(lines: list[str]) -> int:
    count = 0

    for line in lines:
        half = len(line) // 2
        compartments = map(set, (line[0:half], line[half:]))
        char = set.intersection(*compartments).pop()
        count += get_priority(char)

    return count


def part_two(lines: list[str]) -> int:
    count = 0

    for i in range(0, len(lines), 3):
        sacks = map(set, lines[i:i + 3])
        badge = set.intersection(*sacks).pop()
        count += get_priority(badge)

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
