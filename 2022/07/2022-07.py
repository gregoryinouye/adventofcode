#!/usr/bin/env python3

from __future__ import annotations
import sys
from pathlib import Path
from typing import Optional

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 1348005
part_two_answer = 12785886


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


class Node:
    def __init__(self, name: str, parent: Optional[Node]):
        self.name = name
        self.files = []
        self.directories = {}
        self.parent = parent

    def size(self) -> int:
        return sum(map(lambda file: file[1], self.files)) \
            + sum(map(lambda directory: directory.size(), self.directories.values()))


def build_filetree(commands: list[str]) -> Node:
    root_directory = pwd = Node('/', None)

    for command in commands:
        match command.split(' '):
            case ['$', 'cd', '/']:
                pwd = root_directory
            case ['$', 'cd', '..']:
                pwd = pwd.parent
            case ['$', 'cd', directory_name]:
                pwd = pwd.directories[directory_name]
            case ['$', 'ls']:
                continue
            case ['dir', directory_name]:
                pwd.directories[directory_name] = Node(directory_name, pwd)
            case [size_str, filename]:
                pwd.files.append((filename, int(size_str)))
            case _:
                raise Exception(f'unexpected command: {command}')

    return root_directory


def part_one(lines: list[str]) -> int:
    root_directory = build_filetree(lines)
    directories = [root_directory]
    size_sum = 0

    while directories:
        current_directory = directories.pop()
        size = current_directory.size()
        if size < 100000:
            size_sum += size
        directories.extend(current_directory.directories.values())

    return size_sum


def part_two(lines: list[str]) -> int:
    root_directory = build_filetree(lines)
    directories = [root_directory]
    total_space = 70_000_000
    space_for_update = 30_000_000
    required_space = space_for_update - (total_space - root_directory.size())
    size_to_delete = float('inf')

    while directories:
        current_directory = directories.pop()
        size = current_directory.size()
        if size > required_space:
            size_to_delete = min(size_to_delete, size)
        directories.extend(current_directory.directories.values())

    return size_to_delete


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
