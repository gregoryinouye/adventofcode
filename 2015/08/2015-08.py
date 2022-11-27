#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 1350
part_two_answer = 2085


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(escaped_input: list[str]) -> int:
    count = 0

    for line in escaped_input:
        skip = False

        for i, char in enumerate(line):
            if skip:
                skip = False
                continue

            char = line[i]

            if char == '"':
                count += 1
            if char == '\\' and i < len(line) - 1:
                next_char = line[i + 1]
                if next_char == 'x':
                    count += 3
                elif next_char == '"':
                    pass
                elif next_char == '\\':
                    skip = True
                    count += 1
                else:
                    count += 1

    return count


def part_two(escaped_input: list[str]) -> int:
    return sum(2 + line.count('\\') + line.count('"') for line in escaped_input)


if __name__ == '__main__':
    paths = [test_filename] if len(sys.argv) <= 1 else sys.argv[1:]

    for path_str in paths:
        print(f"\n{path_str}:")
        puzzle_input = parse(Path(path_str))

        print(puzzle_input)

        part_one_actual = part_one(puzzle_input)
        part_two_actual = part_two(puzzle_input)

        result_one = '\u2705 ' if part_one_actual == part_one_answer else '\u274c '
        result_two = '\u2705 ' if part_two_actual == part_two_answer else '\u274c '

        print(result_one, 'Part One:', part_one_actual)
        print(result_two, 'Part Two:', part_two_actual)
