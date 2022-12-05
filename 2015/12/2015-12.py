#!/usr/bin/env python3
import json
import re
import sys
from io import StringIO
from pathlib import Path
from typing import Union

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 191164
part_two_answer = 87842


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def part_one(line: str) -> int:
    regex = re.compile(r'-?\d+')
    numbers = regex.findall(line)
    return sum(map(int, numbers))


def sum_numbers(input_object: Union[dict, list, str, int]) -> int:
    if type(input_object) is dict and 'red' not in input_object.values():
        return sum(map(sum_numbers, input_object.values()))
    elif type(input_object) is list:
        return sum(map(sum_numbers, input_object))
    elif type(input_object) is str:
        pass
    elif type(input_object) is int:
        return input_object
    return 0


def part_two(line: str) -> int:
    json_obj = json.load(StringIO(line))
    return sum_numbers(json_obj)


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
