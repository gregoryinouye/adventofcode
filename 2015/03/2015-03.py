#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 2081
part_two_answer = 2341


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def part_one(directions: str) -> int:
    x, y = 0, 0
    visited = {(x, y)}

    for direction in directions:
        if direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        elif direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        visited.add((x, y))

    return len(visited)


def part_two(directions: str) -> int:
    x, y, x1, y1 = 0, 0, 0, 0
    visited = {(x, y)}

    for i, direction in enumerate(directions):
        if direction == '>':
            if i % 2 == 0:
                x += 1
            else:
                x1 += 1
        elif direction == '<':
            if i % 2 == 0:
                x -= 1
            else:
                x1 -= 1
        elif direction == '^':
            if i % 2 == 0:
                y += 1
            else:
                y1 += 1
        elif direction == 'v':
            if i % 2 == 0:
                y -= 1
            else:
                y1 -= 1

        if i % 2 == 0:
            visited.add((x, y))
        else:
            visited.add((x1, y1))

    return len(visited)


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
