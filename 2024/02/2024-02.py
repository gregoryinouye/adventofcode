#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 516
part_two_answer = 561


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def get_reports(lines: list[str]) -> list[list[int]]:
    split_lines = map(lambda line: line.split(), lines)
    reports = [list(map(int, num)) for num in split_lines]

    return reports


def evaluate_report(report: list[int]) -> bool:
    is_inc = True
    is_dec = True

    for i in range(1, len(report)):
        magnitude = report[i] - report[i - 1]
        is_dec = is_dec and magnitude < 0
        is_inc = is_inc and magnitude > 0
        if not ((is_inc or is_dec) and 0 < abs(magnitude) <= 3):
            return False

    return True


def part_one(lines: list[str]) -> int:
    reports = get_reports(lines)
    count = 0

    for report in reports:
        if evaluate_report(report):
            count += 1

    return count


def part_two(lines: list[str]) -> int:
    reports = get_reports(lines)
    count = 0

    for report in reports:
        for i in range(-1, len(report)):
            sub_report = report[:]
            if (i > -1):
                del sub_report[i]
            if evaluate_report(sub_report):
                count += 1
                break

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
