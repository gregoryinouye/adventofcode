#!/usr/bin/env python3

from collections import Counter
import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 1879048
part_two_answer = 21024792


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def get_sorted_locations(lines: list[str]) -> (list[int], list[int]):
    split_lines = map(lambda line: line.split(), lines)
    transposed_lines = zip(*split_lines)
    column1, column2 = [map(int, num) for num in transposed_lines]

    return sorted(column1), sorted(column2)


def part_one(lines: list[str]) -> int:
    list1, list2 = get_sorted_locations(lines)
    return sum([abs(id1 - id2) for id1, id2 in zip(list1, list2)])


def part_two(lines: list[str]) -> int:
    list1, list2 = get_sorted_locations(lines)
    counter = Counter(list2)
    return sum([num * counter[num] for num in list1])


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
