#!/usr/bin/env python3

from collections import namedtuple
import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 40
part_two_answer = 241


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


fields = ['id', 'children', 'cats', 'samoyeds', 'pomeranians', 'akitas', 'vizslas', 'goldfish', 'trees', 'cars',
          'perfumes']
SueStats = namedtuple(typename='SueStats', field_names=fields, defaults=(None,) * (len(fields) - 1))


def process_stats(stat_line: str):
    stat_line_split = stat_line.split(' ')
    kwargs = {}
    for i in range(0, len(stat_line_split), 2):
        key = 'id' if i == 0 else stat_line_split[i].rstrip(':')
        value = int(stat_line_split[i + 1].rstrip(':,'))
        kwargs[key] = value
    return SueStats(**kwargs)


def part_one(lines: list[str]) -> int:
    sue = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    is_sue = False
    for line in lines:
        sue_stats = process_stats(line)
        for prop, val in sue_stats._asdict().items():
            is_sue = True
            if val is None or prop == 'id':
                continue
            if val != sue[prop]:
                is_sue = False
                break
        if is_sue:
            return sue_stats.id
    return -1


range_props = {'cats', 'trees', 'pomeranians', 'goldfish'}


def part_two(lines: list[str]) -> int:
    ticker_tape = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    is_sue = False
    for line in lines:
        sue_stats = process_stats(line)
        for prop, val in sue_stats._asdict().items():
            is_sue = True
            if val is None or prop == 'id':
                continue
            if ((prop == 'cats' or prop == 'trees') and val <= ticker_tape[prop]) or \
                    ((prop == 'pomeranians' or prop == 'goldfish') and val >= ticker_tape[prop]) or \
                    (prop not in range_props and val != ticker_tape[prop]):
                is_sue = False
                break
        if is_sue:
            return sue_stats.id
    return -1


# 240 is too low

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
