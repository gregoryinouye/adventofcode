#!/usr/bin/env python3

import sys
from typing import Callable
from functools import reduce
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 211904
part_two_answer = 43364472


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def parse_numbers_part_one(row: str) -> list[int]:
    return list(map(int, row.split(':')[1].split()))


def parse_numbers_part_two(row: str) -> list[int]:
    return [int(''.join(row.split(':')[1].split()))]


def parse_races(rows: list[str], parser: Callable) -> list[(int, int)]:
    raw_races = map(parser, rows)
    return list(zip(*raw_races))


def calculate_wins(race: (int, int)) -> int:
    total_time, record = race
    wins = 0
    for speed in range(total_time):
        time = total_time - speed
        if is_win(speed, time, record):
            wins += 1
    return wins


def is_win(speed: int, time: int, record: int) -> bool:
    return speed * time > record


def part_one(lines: list[str]) -> int:
    races = parse_races(lines, parse_numbers_part_one)
    return reduce(lambda x, y: x * y, map(calculate_wins, races))


def part_two(lines: list[str]) -> int:
    races = parse_races(lines, parse_numbers_part_two)
    return reduce(lambda x, y: x * y, map(calculate_wins, races))


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
