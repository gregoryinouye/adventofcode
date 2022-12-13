#!/usr/bin/env python3

import json
from functools import cmp_to_key
from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 5503
part_two_answer = 20952


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n\n')


def compare(left, right) -> int:
    if type(left) == int and type(right) == int:
        return min(1, max(-1, left - right))

    if type(left) == int and type(right) == list:
        return compare([left], right)
    if type(left) == list and type(right) == int:
        return compare(left, [right])

    if type(left) == list and type(right) == list:
        for i in range(len(left)):
            if i == len(right):
                return 1
            comparison = compare(left[i], right[i])
            if comparison != 0:
                return comparison
        if len(left) < len(right):
            return -1
        return 0
    return -1


def part_one(lines: list[str]) -> int:
    indices = []
    for i, pair in enumerate(lines):
        left, right = map(json.loads, pair.split('\n'))
        if compare(left, right) == -1:
            indices.append(i + 1)
    return sum(indices)


def part_two(lines: list[str]) -> int:
    all_lines = [json.loads(packet) for line in lines for packet in line.split('\n')]
    divider_packet1 = [[2]]
    divider_packet2 = [[6]]
    all_lines.extend([divider_packet1, divider_packet2])
    all_lines.sort(key=cmp_to_key(compare))
    return (all_lines.index(divider_packet1) + 1) * (all_lines.index(divider_packet2) + 1)


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
