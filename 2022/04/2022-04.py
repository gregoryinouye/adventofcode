#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 494
part_two_answer = 833


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def part_one(lines: str) -> int:
    lines_split = lines.split('\n')
    count = 0
    for line in lines_split:
        pair1, pair2 = line.split(',')
        pair1start, pair1end = pair1.split('-')
        pair2start, pair2end = pair2.split('-')

        pair1start = int(pair1start)
        pair1end = int(pair1end)
        pair2start = int(pair2start)
        pair2end = int(pair2end)

        if pair1start <= pair2start and pair1end >= pair2end:
            count += 1
        elif pair2start <= pair1start and pair2end >= pair1end:
            count += 1

    return count


def part_two(lines: str) -> int:
    lines_split = lines.split('\n')
    count = 0
    for line in lines_split:
        pair1, pair2 = line.split(',')
        pair1start, pair1end = pair1.split('-')
        pair2start, pair2end = pair2.split('-')

        pair1start = int(pair1start)
        pair1end = int(pair1end)
        pair2start = int(pair2start)
        pair2end = int(pair2end)

        set1 = set()
        for i in range(pair1start, pair1end + 1):
            set1.add(i)
        set2 = set()
        for i in range(pair2start, pair2end + 1):
            set2.add(i)
        intersect = set1.intersection(set2)
        if len(intersect) != 0:
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
