#!/usr/bin/env python3

from __future__ import annotations
import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem[:-2] + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 1348005
part_two_answer = 12785886


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def build_directories(commands: list[str]) -> dict[str, int]:
    directories = {}
    pwd = ['']

    for command in commands:
        match command.split(' '):
            case ['$', 'cd', '/']:
                del pwd[1:]
            case ['$', 'cd', '..']:
                pwd.pop()
            case ['$', 'cd', directory_name]:
                pwd.append(directory_name)
            case ['$', 'ls']:
                continue
            case ['dir', _]:
                continue
            case [size_str, _] if size_str.isdecimal():
                for i in range(len(pwd)):
                    directory_name = '/'.join(pwd[0:i + 1])
                    directories[directory_name] = directories.get(directory_name, 0) + int(size_str)
            case _:
                raise Exception(f'unexpected command: {command}')

    return directories


def part_one(lines: list[str]) -> int:
    directories = build_directories(lines)
    return sum(size for size in directories.values() if size < 100_000)


def part_two(lines: list[str]) -> int:
    directories = build_directories(lines)
    total_space = 70_000_000
    space_for_update = 30_000_000
    required_space = space_for_update - (total_space - directories[''])
    return min(size for size in directories.values() if size >= required_space)


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
