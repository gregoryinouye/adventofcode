#!/usr/bin/env python3

import itertools
import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 664
part_two_answer = 640


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def process_utils(utils: list[str]) -> dict[str, dict[str, int]]:
    processed = {}

    for util in utils:
        util_split = util.split(' ')
        person = util_split[0]
        verb = util_split[2]
        units = int(util_split[3]) if verb == 'gain' else -int(util_split[3])
        neighbor = util_split[10][:-1]

        processed[person] = processed.get(person, {})
        processed[person][neighbor] = units

    return processed


def get_utils_delta(person_one: str, person_two: str, utils: dict[str, dict[str, int]]) -> int:
    return utils[person_one][person_two] + utils[person_two][person_one]


def part_one(lines: list[str]) -> int:
    utils: dict[str, dict[str, int]] = process_utils(lines)
    max_so_far = -float('inf')
    guest_count = len(utils.keys())

    for permutation in itertools.permutations(utils.keys(), guest_count):
        util_count = sum(get_utils_delta(permutation[i], permutation[i - 1], utils) for i in range(guest_count))
        max_so_far = max(max_so_far, util_count)

    return max_so_far


def part_two(lines: list[str]) -> int:
    utils: dict[str, dict[str, int]] = process_utils(lines)
    max_so_far = -float('inf')
    guest_count = len(utils.keys())

    for permutation in itertools.permutations(utils.keys(), guest_count):
        util_count = sum(get_utils_delta(permutation[i], permutation[i - 1], utils) for i in range(1, guest_count))
        max_so_far = max(max_so_far, util_count)

    return max_so_far


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
