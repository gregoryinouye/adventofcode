#!/usr/bin/env python3

import itertools
import re
import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 174960292
part_two_answer = 56275602


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def process_mul(command: str) -> int:
    (_, num1, num2, _) = re.split('[(,)]', command)
    return int(num1) * int(num2)


def process_commands(commands: list[str], use_flag: bool) -> int:
    is_enabled = True
    total = 0
    for command in commands:
        match command:
            case 'do()':
                is_enabled = True
            case "don't()":
                if use_flag:
                    is_enabled = False
            case _ if is_enabled:
                total += process_mul(command)
    return total


def get_and_process_commands(lines: list[str], use_flag: bool) -> int:
    commands = [re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line) for line in lines]
    commands_flat = list(itertools.chain(*commands))
    return process_commands(commands_flat, use_flag)


def part_one(lines: list[str]) -> int:
    return get_and_process_commands(lines, False)


def part_two(lines: list[str]) -> int:
    return get_and_process_commands(lines, True)


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
