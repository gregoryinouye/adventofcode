#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 492982
part_two_answer = 6989950


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def look_and_say(line: str) -> str:
    result = list(line)

    i = 0
    current = []

    while i < len(result):
        char = result[i]
        count = 1

        while i < len(result) - 1 and char == result[i + 1]:
            i += 1
            count += 1

        current.extend([str(count), char])
        i += 1

    result = current

    return ''.join(result)


def part_one(line: str) -> int:
    current = line
    for i in range(40):
        current = look_and_say(current)
    return len(current)


def part_two(line: str) -> int:
    current = line
    for i in range(50):
        current = look_and_say(current)
    return len(current)


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
