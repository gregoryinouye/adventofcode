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


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


class Node:
    def __init__(self, name: str, parent: Optional[Node]):
        self.name = name
        self.files = []
        self.directories = {}
        self.parent = parent

    def size(self) -> int:
        return sum(map(lambda file: file[1], self.files)) \
            + sum(map(lambda directory: directory.size(), self.directories.values()))

    def __str__(self):
        return f'<{self.name}, {self.directories}, {self.files}>'

    def __repr__(self):
        return self.__str__()

def build_filetree(commands: list[str]) -> Node:
    main_dir = Node('/', None)
    pwd = main_dir

    for command in commands:
        if command == '$ cd /':
            pwd = main_dir
        elif command == '$ cd ..':
            pwd = pwd.parent
        elif command.startswith('$ cd'):
            prev_pwd = pwd
            _, _, pwd_name = command.split(' ')
            if pwd_name not in pwd.directories:
                prev_pwd.directories[pwd_name] = Node(pwd_name, prev_pwd)
            pwd = pwd.directories[pwd_name]
        elif command.startswith('$ ls'):
            pass
        elif command.startswith('dir'):
            _, dir_name = command.split(' ')
            pwd.directories[dir_name] = Node(dir_name, pwd)
        else:
            size_str, filename = command.split(' ')
            size = int(size_str)
            pwd.files.append((filename, size))
    return main_dir


def part_one(lines: str) -> int:
    commands = lines.split('\n')
    main_dir = build_filetree(commands)

    stack = [main_dir]

    count = 0
    while stack:
        curr: Node = stack.pop()
        if curr.size() < 100000:
            count += curr.size()
        stack.extend(curr.directories.values())
    return count


def part_two(lines: str) -> int:
    commands = lines.split('\n')
    main_dir = build_filetree(commands)

    stack = [main_dir]

    empty_space = 70000000 - main_dir.size()
    target = 30000000 - empty_space

    smallest_dir = float('inf')
    while stack:
        curr: Node = stack.pop()
        if curr.size() > target:
            smallest_dir = min(smallest_dir, curr.size())
        stack.extend(curr.directories.values())
    return smallest_dir


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
